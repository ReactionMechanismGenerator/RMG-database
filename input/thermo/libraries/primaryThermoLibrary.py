#!/usr/bin/env python
# encoding: utf-8

name = "primaryThermoLibrary"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 0,
    label = "H2",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.895,6.975,6.994,7.009,7.081,7.219,7.72],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (31.233,'cal/(mol*K)','+|-',0.0007),
    ),
    shortDesc = u"""library value for H2""",
    longDesc = 
u"""

""",
)

entry(
    index = 1,
    label = "H",
    molecule = 
"""
multiplicity 2
1 H u1 p0 c0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.968,4.968,4.968,4.968,4.968,4.968,4.968],'cal/(mol*K)'),
        H298 = (52.103,'kcal/mol','+|-',0.001),
        S298 = (27.419,'cal/(mol*K)','+|-',0.0005),
    ),
    shortDesc = u"""library value for H radical""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "O2",
    molecule = 
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.0233,7.1986,7.4285,7.6673,8.0656,8.3363,8.7407],'cal/(mol*K)'),
        H298 = (-0.0010244,'kcal/mol'),
        S298 = (49.0236,'cal/(mol*K)'),
    ),
    shortDesc = u"""from GRI-Mech 3.0""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "O2(S)",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 O u0 p2 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.0233,7.1986,7.4285,7.6673,8.0656,8.3363,8.7407],'cal/(mol*K)'),
        H298 = (22.54,'kcal/mol'),
        S298 = (49.0236,'cal/(mol*K)'),
    ),
    shortDesc = u"""from absorption energy""",
    longDesc = 
u"""
H298 taken from absorption energy: 7882 cm^-1 = 22.54 kcal/mol
S and Cp taken from the values for triplet O2
ref: David R. Kearns, Physical and chemical properties of singlet molecular oxygen, Chemical Reviews 71(4) 1971, 395-427
""",
)

entry(
    index = 4,
    label = "CO3s1",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,D}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {1,S} {2,S}
4 O u0 p2 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.82,13.53,14.8,15.76,17.05,17.85,18.84],'cal/(mol*K)'),
        H298 = (-37.9,'kcal/mol'),
        S298 = (61.28,'cal/(mol*K)'),
    ),
    shortDesc = u"""Mebel et al (2004) http:""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "CO3t1",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 O u0 p2 c0 {1,D}
3 O u1 p2 c0 {1,S}
4 O u1 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.43,14.02,15.23,16.16,17.4,18.14,19.01],'cal/(mol*K)'),
        H298 = (-11.5,'kcal/mol'),
        S298 = (64.53,'cal/(mol*K)'),
    ),
    shortDesc = u"""Mebel et al (2004) http:""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "CO3t2",
    molecule = 
"""
multiplicity 3
1 C u1 p0 c0 {2,S} {3,D}
2 O u0 p2 c0 {1,S} {4,S}
3 O u0 p2 c0 {1,D}
4 O u1 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.48,14.83,15.83,16.59,17.62,18.26,19.05],'cal/(mol*K)'),
        H298 = (28.7,'kcal/mol'),
        S298 = (67.06,'cal/(mol*K)'),
    ),
    shortDesc = u"""Mebel et al (2004) http:""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "cyclopropene12diyl",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {3,D}
3 C u1 p0 c0 {1,S} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.32,13.42,15.16,16.58,18.74,20.29,22.63],'cal/(mol*K)'),
        H298 = (188.13,'kcal/mol'),
        S298 = (59.26,'cal/(mol*K)'),
    ),
    shortDesc = u"""doi:10.1016/j.chemphys.2008.01.057 and doi:10.1021/jp003224c""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "cyclopropynylidyne",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,T} {3,S}
2 C u0 p0 c0 {1,T} {3,S}
3 C u1 p0 c0 {1,S} {2,S} {4,S}
4 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.43,11.93,13.18,14.18,15.61,16.59,17.99],'cal/(mol*K)'),
        H298 = (169.8,'kcal/mol'),
        S298 = (57.47,'cal/(mol*K)'),
    ),
    shortDesc = u"""doi:10.1016/j.chemphys.2008.01.057 and doi:10.1021/jp003224c""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "OCCO(S)",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,D}
2 C u0 p0 c0 {1,D} {4,D}
3 O u0 p2 c0 {1,D}
4 O u0 p2 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.66,14.78,15.66,16.41,17.57,18.39,19.53],'cal/(mol*K)'),
        H298 = (18.31,'kcal/mol'),
        S298 = (90.63,'cal/(mol*K)'),
    ),
    shortDesc = u"""QCI""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "OCCO",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,T} {3,S}
2 C u0 p0 c0 {1,T} {4,S}
3 O u1 p2 c0 {1,S}
4 O u1 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.21,15.2,15.98,16.65,17.72,18.49,19.58],'cal/(mol*K)'),
        H298 = (5.6,'kcal/mol'),
        S298 = (61.18,'cal/(mol*K)'),
    ),
    shortDesc = u"""QCI""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "C3H2",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {3,S} {5,S}
3 C u0 p1 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.61,12.79,14.81,16.48,18.71,20.33,22.59],'cal/(mol*K)'),
        H298 = (113.99,'kcal/mol'),
        S298 = (56.44,'cal/(mol*K)'),
    ),
    shortDesc = u"""Burcat's recommended value for 16165-40-5: C3H2 CYCLOPROPENYLIDENE BI-RADICAL SINGLET on 3/25/2011 (MRH converted from NASA-7 to RMG format)""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "S2",
    molecule = 
"""
multiplicity 3
1 S u1 p2 c0 {2,S}
2 S u1 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.79,8.14,8.35,8.51,8.75,8.94,9.31],'cal/(mol*K)'),
        H298 = (30.74,'kcal/mol'),
        S298 = (54.54,'cal/(mol*K)'),
    ),
    shortDesc = u"""from Chase thermo database""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "S2(S)",
    molecule = 
"""
1 S u0 p2 c0 {2,D}
2 S u0 p2 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.81,8.17,8.4,8.54,8.7,8.78,8.87],'cal/(mol*K)'),
        H298 = (47.12,'kcal/mol'),
        S298 = (53.78,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 value A.G. Vandeputte""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "HCS",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,D} {3,S}
2 S u0 p2 c0 {1,D}
3 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.77,9.46,10.04,10.51,11.22,11.76,12.62],'cal/(mol*K)'),
        H298 = (71.7,'kcal/mol'),
        S298 = (56.37,'cal/(mol*K)'),
    ),
    shortDesc = u"""NIST value + B3LYP/cbsb7 entropy and heat cap A.G. Vandeputte""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "Ar",
    molecule = 
"""
1 Ar u0 p4 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,4.37967], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,4.37967], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""Burcat Thermo Data""",
    longDesc = 
u"""
Ar HF298=0.  REF=C.E. Moore 'Atomic Energy Levels' NSRDS-NBS 35 (1971) p.211
""",
)

entry(
    index = 16,
    label = "N2",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 N u0 p1 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53101,-0.000123661,-5.02999e-07,2.43531e-09,-1.40881e-12,-1046.98,2.96747], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.95258,0.0013969,-4.92632e-07,7.8601e-11,-4.60755e-15,-923.949,5.87189], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""Burcat Thermo Data""",
    longDesc = 
u"""
N2  HF298= 0.0 KJ  REF=TSIV  Max Lst Sq Error Cp @ 6000 K 0.29%
""",
)

entry(
    index = 17,
    label = "He",
    molecule = 
"""
1 He u0 p1 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,0.928724], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,0.928724], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""Burcat Thermo Data""",
    longDesc = 
u"""
McBride, Heimel, Ehlers & Gordon "Thermodynamic Properties to 6000 K", 1963.
""",
)

entry(
    index = 18,
    label = "C(S)",
    molecule = 
"""
1 C u0 p2 c0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.968,4.968,4.968,4.968,4.968,4.968,4.968],'cal/(mol*K)'),
        H298 = (200.397,'kcal/mol'),
        S298 = (33.393,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
H298: ATcT version 1.110
level of theory energy: CCSD(T)F12A/cc-pVQZ-F12//CCSD(T)/cc-pVQZ
level of theory frequency: B3LYP/6-311++g(d,p)//B3LYP/6-311++g(d,p)
""",
)

entry(
    index = 19,
    label = "C(T)",
    molecule = 
"""
multiplicity 3
1 C u2 p1 c0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.968,4.968,4.968,4.968,4.968,4.968,4.968],'cal/(mol*K)'),
        H298 = (171.336,'kcal/mol'),
        S298 = (35.576,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
H298: ATcT version 1.110
level of theory energy: CCSD(T)F12A/cc-pVQZ-F12//CCSD(T)/cc-pVQZ
level of theory frequency: B3LYP/6-311++g(d,p)//B3LYP/6-311++g(d,p)
""",
)

entry(
    index = 20,
    label = "CH2(S)",
    molecule = 
"""
1 C u0 p1 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.089,8.316,8.622,8.99,9.787,10.502,11.832],'cal/(mol*K)'),
        H298 = (102.541,'kcal/mol'),
        S298 = (45.197,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
H298: ATcT version 1.110
level of theory energy: CCSD(T)F12A/cc-pVQZ-F12//CCSD(T)/cc-pVQZ
level of theory frequency: B3LYP/6-311++g(d,p)//B3LYP/6-311++g(d,p)
""",
)

entry(
    index = 21,
    label = "CH2(T)",
    molecule = 
"""
multiplicity 3
1 C u2 p0 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.342,8.61,8.914,9.238,9.893,10.5,11.68],'cal/(mol*K)'),
        H298 = (93.559,'kcal/mol'),
        S298 = (46.636,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
H298: ATcT version 1.110
level of theory energy: CCSD(T)F12A/cc-pVQZ-F12//CCSD(T)/cc-pVQZ
level of theory frequency: B3LYP/6-311++g(d,p)//B3LYP/6-311++g(d,p)
""",
)

entry(
    index = 22,
    label = "CH4",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.621,9.648,10.941,12.344,14.887,16.967,20.535],'cal/(mol*K)'),
        H298 = (-17.814,'kcal/mol'),
        S298 = (44.473,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
H298: ATcT version 1.110
level of theory energy: CCSD(T)F12A/cc-pVQZ-F12//CCSD(T)/cc-pVQZ
level of theory frequency: B3LYP/6-311++g(d,p)//B3LYP/6-311++g(d,p)
""",
)

entry(
    index = 23,
    label = "NH(T)",
    molecule = 
"""
multiplicity 3
1 N u2 p1 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.95,6.945,6.962,7.006,7.173,7.387,7.891],'cal/(mol*K)'),
        H298 = (85.753,'kcal/mol'),
        S298 = (43.265,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
H298: ATcT version 1.110
level of theory energy: CCSD(T)F12A/cc-pVQZ-F12//CCSD(T)/cc-pVQZ
level of theory frequency: B3LYP/6-311++g(d,p)//B3LYP/6-311++g(d,p)
""",
)

entry(
    index = 24,
    label = "NH2(D)",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.055,8.227,8.467,8.762,9.435,10.083,11.402],'cal/(mol*K)'),
        H298 = (44.467,'kcal/mol'),
        S298 = (46.516,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
H298: ATcT version 1.110
level of theory energy: CCSD(T)F12A/cc-pVQZ-F12//CCSD(T)/cc-pVQZ
level of theory frequency: B3LYP/6-311++g(d,p)//B3LYP/6-311++g(d,p)
""",
)

entry(
    index = 25,
    label = "NH3",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.486,9.051,9.737,10.484,11.921,13.163,15.503],'cal/(mol*K)'),
        H298 = (-10.889,'kcal/mol'),
        S298 = (45.986,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
H298: ATcT version 1.110
level of theory energy: CCSD(T)F12A/cc-pVQZ-F12//CCSD(T)/cc-pVQZ
level of theory frequency: B3LYP/6-311++g(d,p)//B3LYP/6-311++g(d,p)
""",
)

entry(
    index = 26,
    label = "O(S)",
    molecule = 
"""
1 O u0 p3 c0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.968,4.968,4.968,4.968,4.968,4.968,4.968],'cal/(mol*K)'),
        H298 = (104.81,'kcal/mol'),
        S298 = (34.25,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
H298: ATcT version 1.110
level of theory energy: CCSD(T)F12A/cc-pVQZ-F12//CCSD(T)/cc-pVQZ
level of theory frequency: B3LYP/6-311++g(d,p)//B3LYP/6-311++g(d,p)
""",
)

entry(
    index = 27,
    label = "O(T)",
    molecule = 
"""
multiplicity 3
1 O u2 p2 c0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.968,4.968,4.968,4.968,4.968,4.968,4.968],'cal/(mol*K)'),
        H298 = (59.567,'kcal/mol'),
        S298 = (38.49,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
H298: ATcT version 1.110
level of theory energy: CCSD(T)F12A/cc-pVQZ-F12//CCSD(T)/cc-pVQZ
level of theory frequency: B3LYP/6-311++g(d,p)//B3LYP/6-311++g(d,p)
""",
)

entry(
    index = 28,
    label = "OH(D)",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.954,6.946,6.951,6.973,7.08,7.251,7.719],'cal/(mol*K)'),
        H298 = (8.863,'kcal/mol'),
        S298 = (43.958,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
H298: ATcT version 1.110
level of theory energy: CCSD(T)F12A/cc-pVQZ-F12//CCSD(T)/cc-pVQZ
level of theory frequency: B3LYP/6-311++g(d,p)//B3LYP/6-311++g(d,p)
""",
)

entry(
    index = 29,
    label = "H2O",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.038,8.18,8.379,8.624,9.195,9.766,11.019],'cal/(mol*K)'),
        H298 = (-57.797,'kcal/mol'),
        S298 = (45.084,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
H298: ATcT version 1.110
level of theory energy: CCSD(T)F12A/cc-pVQZ-F12//CCSD(T)/cc-pVQZ
level of theory frequency: B3LYP/6-311++g(d,p)//B3LYP/6-311++g(d,p)
""",
)

entry(
    index = 30,
    label = "Cl2",
    molecule = 
"""
1 Cl u0 p3 c0 {2,S}
2 Cl u0 p3 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.73638,0.00783526,-1.45105e-05,1.25731e-08,-4.13247e-12,-1058.8,9.44557], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.74728,-0.000488582,2.68445e-07,-2.43476e-11,-1.03683e-15,-1511.02,-0.344539], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""Burcat Thermo Data""",
    longDesc = 
u"""
Burcat Thermo Data

REFERENCE ELEMENT REF=Gurvich 1989 V1 py.1 p.177 HF298=0.00 kcal Max Lst 
Sq Error Cp @ 6000 **1.26%** (Cp @ 700 K 0.08%)
""",
)

entry(
    index = 31,
    label = "Cl",
    molecule = 
"""
multiplicity 2
1 Cl u1 p3 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.26062,0.00154154,-6.80284e-07,-1.59973e-09,1.15417e-12,13855.3,6.57021], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.94658,-0.000385985,1.36139e-07,-2.17033e-11,1.28751e-15,13697,3.1133], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""Burcat Thermo Data""",
    longDesc = 
u"""
Burcat Thermo Data

HF298=121.302+/-0.008 kJ HF0=119.633+/- 0.008 kJ  REF=JANAF  {HF298=121.302
+/-0.002 kJ  REF=ATcT A}
""",
)

entry(
    index = 32,
    label = "HCl",
    molecule = 
"""
1 Cl u0 p3 c0 {2,S}
2 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.46376,0.000476484,-2.00301e-06,3.31714e-09,-1.44958e-12,-12144.4,2.66428], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.75758,0.00145387,-4.79647e-07,7.77909e-11,-4.79574e-15,-11913.8,6.52197], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""Burcat Thermo Data""",
    longDesc = 
u"""
Burcat Thermo Data

HYDROCHLORIC ACID CALCULATED FROM ORIGINAL TABLES  REF=Gurvich 1989
HF298=-92.31 kJ {HF298=-92.17+/-0.006 kJ   REF=ATcT C}  Max Lst Sq Error Cp @ 
6000 K 0.17%
""",
)

entry(
    index = 33,
    label = "Ne",
    molecule = 
"""
1 Ne u0 p4 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,3.35532], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,3.35532], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""Burcat Thermo Data""",
    longDesc = 
u"""
McBride, Heimel, Ehlers & Gordon, "Thermodynamic Properties to 6000 K", 1963.
""",
)

entry(
    index = 34,
    label = "ONHN",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,S} {4,D}
3 H u0 p0 c0 {2,S}
4 N u1 p1 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.04618,-0.00333952,3.35365e-05,-4.57384e-08,2.0107e-11,36047.5,6.95758], Tmin=(10,'K'), Tmax=(708.753,'K')),
            NASAPolynomial(coeffs=[2.46943,0.0105681,-6.49838e-06,1.89046e-09,-2.10479e-13,36145.2,13.1342], Tmin=(708.753,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (299.723,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "O3",
    molecule = 
"""
1 O u0 p3 c-1 {2,S}
2 O u0 p1 c+1 {1,S} {3,D}
3 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.46261,0.00958278,-7.08736e-06,1.36337e-09,2.96965e-13,16061.5,12.1419], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.42937,0.00182038,-7.70561e-07,1.49929e-10,-1.07556e-14,15235.3,-3.26639], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Ozone
Taken from the GlarborgH2S thermo library,
in agreement with the data by Burcat et al. (H298 = 34.10 kcal/mol in GlarborgH2S vs. 33.89 kcal/mol in BurcatNS)
""",
)

entry(
    index = 36,
    label = "SO(S)",
    molecule = 
"""
1 S u0 p2 c0 {2,D}
2 O u0 p2 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.22,7.55,7.84,8.08,8.43,8.62,8.95],'cal/(mol*K)'),
        H298 = (23.74,'kcal/mol'),
        S298 = (53.01,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
H298 taken from absorption energy of O2: 7882 cm^-1 = 22.54 kcal/mol, and was added to H298 of SO(T)
S and Cp taken from the values for triplet SO
ref: R.J. Kee, F.M. Rupley, J.A. Miller, The Chemkin Thermodynamic Data Base, Sandia Report SAND87-8215, Sandia National
Laboratories, Livermore, California, 1991
""",
)

entry(
    index = 37,
    label = "HF",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.43657,0.000486021,-1.2524e-06,1.36475e-09,-4.09574e-13,-33800.1,1.20682], Tmin=(298,'K'), Tmax=(1250,'K')),
            NASAPolynomial(coeffs=[2.7813,0.00103959,-2.41735e-07,2.68416e-11,-1.09766e-15,-33504.2,5.0197], Tmin=(1250,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-281.113,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (37.4151,'J/mol/K'),
    ),
    shortDesc = u"""71STUPRO JANAF 2nd ed. (1971)""",
    longDesc = 
u"""
71STUPRO
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt which is described as
the updated NIST HFC mechanism in https://doi.org/10.1016/j.jfluchem.2019.05.002
"71STUPRO" presumably refers to the
JANAF Thermochemical Tables, Second Edition
by Daniel R. Stull and H. Prophet. (1971)
http://dx.doi.org/10.6028/NBS.NSRDS.37
""",
)

entry(
    index = 38,
    label = "F",
    molecule = 
"""
multiplicity 2
1 F u1 p3 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.90371,-0.000635296,2.64735e-07,7.69063e-11,-5.45254e-14,8672.27,2.70828], Tmin=(298,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[2.65117,-0.00014013,5.19236e-08,-8.84954e-12,5.9028e-16,8758.29,4.07857], Tmin=(1400,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (72.8916,'kJ/mol'),
        Cp0 = (20.7862,'J/mol/K'),
        CpInf = (20.7862,'J/mol/K'),
    ),
    shortDesc = u"""71STUPRO JANAF 2nd ed. (1971)""",
    longDesc = 
u"""
71STUPRO
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt which is described as
the updated NIST HFC mechanism in https://doi.org/10.1016/j.jfluchem.2019.05.002
"71STUPRO" presumably refers to the
JANAF Thermochemical Tables, Second Edition
by Daniel R. Stull and H. Prophet. (1971)
http://dx.doi.org/10.6028/NBS.NSRDS.37
which it does indeed match (p.679).
The data pre-date 1954.
""",
)

entry(
    index = 39,
    label = "Br2",
    molecule = 
"""
1 Br u0 p3 c0 {2,S}
2 Br u0 p3 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.34375,0.00634804,-1.36289e-05,1.31573e-08,-4.67761e-12,2531.64,9.07775], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.18756,-0.00138705,9.35013e-07,-2.07121e-10,1.41849e-14,2103.48,0.0761703], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (21.4067,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (37.4151,'J/mol/K'),
    ),
    shortDesc = """Burcat""",
    longDesc = 
"""
BrBr
7726-95-6
From Burcat's thermo http://garfield.chem.elte.hu/Burcat/BURCAT.THR
which has been matched to ATcT version 1.112 Core ARGONNE 4.2.2011
Br2  GAS  Calculated from CODATA Key Values and Gurvich's 89 Tables
HF298=30.88+/-0.11 kJ REF=ATcT C   {HF298=30.91 kJ HF0=45.705 kJ. REF= Gurvich.}
Max Lst Sq Error Cp @ 6000 K 0.36 %.
""",
)

entry(
    index = 40,
    label = "HBr",
    molecule = 
"""
1 Br u0 p3 c0 {2,S}
2 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.48118,0.000342734,-1.80533e-06,3.61181e-09,-1.74298e-12,-5355.37,4.01309], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.83372,0.00148518,-5.13137e-07,8.73711e-11,-5.72363e-15,-5176.21,7.43754], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-44.4806,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (37.4151,'J/mol/K'),
    ),
    shortDesc = """Burcat""",
    longDesc = 
"""
From Burcat's thermo http://garfield.chem.elte.hu/Burcat/BURCAT.THR
which has been matched to ATcT version 1.112 Core ARGONNE 4.2.2011
10035-10-6
HBr HYDROBROMIC ACID CALCULATED FROM ORIGINAL TABLES  REF=Shenyavskaya & Yougman
JPCRD 33,(2004),923  HF298=-35.85+/-0.15 kJ  REF=ATcT C  {HF298=-36.05+/-0.15 kJ
REF=Ruscic ATcT D;  HF298=-36.29+/-0.16 kJ  REF=Gurvich 89}  Max Lst Sq Error Cp 
@ 6000 K 0.33%
""",
)

entry(
    index = 41,
    label = "Br",
    molecule = 
"""
multiplicity 2
1 Br u1 p3 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.48422,0.000161406,-5.63461e-07,7.46724e-10,-2.58956e-13,12708.4,6.86657], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.08902,0.000711612,-2.69887e-07,4.15012e-11,-2.3138e-15,12855.6,9.07043], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (105.654,'kJ/mol'),
        Cp0 = (20.7862,'J/mol/K'),
        CpInf = (20.7862,'J/mol/K'),
    ),
    shortDesc = """Burcat""",
    longDesc = 
"""
From Burcat's thermo http://garfield.chem.elte.hu/Burcat/BURCAT.THR
which has been matched to ATcT version 1.112 Core ARGONNE 4.2.2011
10097-32-2
BR   Calculated by Ruscic ATcT C  HF298=111.852+/-0.06 kJ  REF=ATcT C
{HF298=111.86+/-0.06  REF=JANAF 82}  Max Lst Sq Error Cp @ 1200 K 0.19%
""",
)

entry(
    index = 42,
    label = "F2",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 F u0 p3 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.66955,0.00529418,-6.47091e-06,3.91833e-09,-9.38451e-13,-980.801,7.82659], Tmin=(298,'K'), Tmax=(1150,'K')),
            NASAPolynomial(coeffs=[4.05774,0.000600034,-2.19218e-07,4.31508e-11,-3.12588e-15,-1324.39,0.863214], Tmin=(1150,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-8.80492,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (37.4151,'J/mol/K'),
    ),
    shortDesc = u"""71STUPRO JANAF 2nd ed. (1971)""",
    longDesc = 
u"""
71STUPRO
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
FF
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt which is described as
the updated NIST HFC mechanism in https://doi.org/10.1016/j.jfluchem.2019.05.002
"71STUPRO" presumably refers to the
JANAF Thermochemical Tables, Second Edition
by Daniel R. Stull and H. Prophet. (1971)
http://dx.doi.org/10.6028/NBS.NSRDS.37
""",
)


entry(
    index = 43,
    label = "NOJ",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {2,D}
2 O u0 p2 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.97,7.06,7.2,7.37,7.72,8,8.46],'cal/(mol*K)'),
        H298 = (21.85,'kcal/mol'),
        S298 = (49.02,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 44,
    label = "NO2J",
    molecule = 
"""
multiplicity 2
1 N u1 p0 c+1 {2,D} {3,S}
2 O u0 p2 c0 {1,D}
3 O u0 p3 c-1 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.86,9.57,10.29,10.92,11.84,12.44,13.19],'cal/(mol*K)'),
        H298 = (8.33,'kcal/mol'),
        S298 = (57.31,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 45,
    label = "CO",
    molecule = 
"""
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.95,7.02,7.12,7.26,7.58,7.86,8.35],'cal/(mol*K)'),
        H298 = (-26.31,'kcal/mol'),
        S298 = (47.2,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 46,
    label = "OCCCO",
    molecule = 
"""
1 O u0 p2 c0 {4,D}
2 O u0 p2 c0 {5,D}
3 C u0 p0 c0 {4,D} {5,D}
4 C u0 p0 c0 {1,D} {3,D}
5 C u0 p0 c0 {2,D} {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs = [3.88307,0.00992983,2.02201e-05,-5.95807e-08,4.18218e-11,-12941.2,7.57621], Tmin = (10, 'K'), Tmax = (516.845, 'K'),),
            NASAPolynomial(coeffs = [4.29366,0.0133667,-8.95161e-06,2.80908e-09,-3.33808e-13,-13072,5.01164], Tmin = (516.845, 'K'), Tmax = (3000, 'K'),),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""G4 calculation""",
    longDesc = 
u"""
# Coordinates for 1 in Input Orientation (angstroms):
#   O    0.0883   -2.4210    0.0000
#   O    0.0883    2.4210    0.0000
#   C   -0.1785    0.0000    0.0000
#   C   -0.0285   -1.2648    0.0000
#   C   -0.0285    1.2648    0.0000

#   Enthalpy of formation (298 K)   =   -22.381 kcal/mol
#   Entropy of formation (298 K)    =    65.801 cal/(mol*K)

HarmonicOscillator(frequencies = ([55.6209, 577.002, 595.072, 598.128, 598.906, 801.916, 1644.01, 2280.9, 2412.53], 'cm^-1'))
""",
)

entry(
    index = 47,
    label = "C(Q)",
    molecule =
"""
multiplicity 5
1 C u4 p0 c0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.968,4.968,4.968,4.968,4.968,4.968,4.968],'cal/(mol*K)'),
        H298 = (1120.106,'kJ/mol'),
        S298 = (35.576,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
H298: ATcT version 1.110
ATcT id: 7440-44-0*3
entropy and heat capacity taken from "C(T)"
""",
)
