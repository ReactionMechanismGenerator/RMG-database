#!/usr/bin/env python
# encoding: utf-8

name = "halogens_G4"
shortDesc = "G4 (B3LYP/GTBas3)"
longDesc = """
Small halogenated species calculated with G4 method (B3LYP/GTBas3) using Gaussian 16
"""

entry(
    index = 0,
    label = "HF",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    statmech = Conformer(E0=(-282.308,'kJ/mol'), modes=[IdealGasTranslation(mass=(20.0062,'amu')), LinearRotor(inertia=(0.809097,'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([4113.43],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 1,
    label = "HBr",
    molecule = 
"""
1 Br u0 p3 c0 {2,S}
2 H  u0 p0 c0 {1,S}
""",
    statmech = Conformer(E0=(-42.7435,'kJ/mol'), modes=[IdealGasTranslation(mass=(79.9262,'amu')), LinearRotor(inertia=(2.01444,'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([2635.59],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 2,
    label = "HCl",
    molecule = 
"""
1 Cl u0 p3 c0 {2,S}
2 H  u0 p0 c0 {1,S}
""",
    statmech = Conformer(E0=(-99.1327,'kJ/mol'), modes=[IdealGasTranslation(mass=(35.9767,'amu')), LinearRotor(inertia=(1.61406,'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([2956.35],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 3,
    label = "F2",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 F u0 p3 c0 {1,S}
""",
    statmech = Conformer(E0=(-5.50154,'kJ/mol'), modes=[IdealGasTranslation(mass=(37.9968,'amu')), LinearRotor(inertia=(18.2987,'amu*angstrom^2'), symmetry=2), HarmonicOscillator(frequencies=([1076.6],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 4,
    label = "FCl",
    molecule = 
"""
1 Cl u0 p3 c0 {2,S}
2 F  u0 p3 c0 {1,S}
""",
    statmech = Conformer(E0=(-65.0486,'kJ/mol'), modes=[IdealGasTranslation(mass=(53.9673,'amu')), LinearRotor(inertia=(33.221,'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([788.172],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 5,
    label = "FBr",
    molecule = 
"""
1 Br u0 p3 c0 {2,S}
2 F  u0 p3 c0 {1,S}
""",
    statmech = Conformer(E0=(-69.7456,'kJ/mol'), modes=[IdealGasTranslation(mass=(97.9167,'amu')), LinearRotor(inertia=(47.8909,'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([680.84],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 6,
    label = "Br2",
    molecule = 
"""
1 Br u0 p3 c0 {2,S}
2 Br u0 p3 c0 {1,S}
""",
    statmech = Conformer(E0=(25.0997,'kJ/mol'), modes=[IdealGasTranslation(mass=(157.837,'amu')), LinearRotor(inertia=(211.833,'amu*angstrom^2'), symmetry=2), HarmonicOscillator(frequencies=([318.225],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 7,
    label = "[O]F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 O u1 p2 c0 {1,S}
""",
    statmech = Conformer(E0=(102.686,'kJ/mol'), modes=[IdealGasTranslation(mass=(34.9933,'amu')), LinearRotor(inertia=(15.6231,'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([1151.69],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 8,
    label = "ClBr",
    molecule = 
"""
1 Br u0 p3 c0 {2,S}
2 Cl u0 p3 c0 {1,S}
""",
    statmech = Conformer(E0=(7.33056,'kJ/mol'), modes=[IdealGasTranslation(mass=(113.887,'amu')), LinearRotor(inertia=(113.734,'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([433.654],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 9,
    label = "[O]Br",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {2,S}
2 O  u1 p2 c0 {1,S}
""",
    statmech = Conformer(E0=(124,'kJ/mol'), modes=[IdealGasTranslation(mass=(94.9133,'amu')), LinearRotor(inertia=(40.0218,'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([729.614],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 10,
    label = "[O]Cl",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {2,S}
2 O  u1 p2 c0 {1,S}
""",
    statmech = Conformer(E0=(98.6689,'kJ/mol'), modes=[IdealGasTranslation(mass=(50.9638,'amu')), LinearRotor(inertia=(27.838,'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([845.543],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 11,
    label = "Cl2",
    molecule = 
"""
1 Cl u0 p3 c0 {2,S}
2 Cl u0 p3 c0 {1,S}
""",
    statmech = Conformer(E0=(-6.90468,'kJ/mol'), modes=[IdealGasTranslation(mass=(69.9377,'amu')), LinearRotor(inertia=(71.0956,'amu*angstrom^2'), symmetry=2), HarmonicOscillator(frequencies=([548.584],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 12,
    label = "OF",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 H u0 p0 c0 {2,S}
""",
    statmech = Conformer(E0=(-95.2653,'kJ/mol'), modes=[IdealGasTranslation(mass=(36.0011,'amu')), NonlinearRotor(inertia=([0.860315,18.4105,19.2708],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([1005.07,1417.2,3730.42],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 13,
    label = "OBr",
    molecule = 
"""
1 Br u0 p3 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 H  u0 p0 c0 {2,S}
""",
    statmech = Conformer(E0=(-71.8729,'kJ/mol'), modes=[IdealGasTranslation(mass=(95.9211,'amu')), NonlinearRotor(inertia=([0.831251,48.2697,49.101],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([636.644,1200.87,3777.61],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 14,
    label = "OCl",
    molecule = 
"""
1 Cl u0 p3 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 H  u0 p0 c0 {2,S}
""",
    statmech = Conformer(E0=(-84.4995,'kJ/mol'), modes=[IdealGasTranslation(mass=(51.9716,'amu')), NonlinearRotor(inertia=([0.832669,33.9301,34.7628],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([738.545,1277.46,3767.44],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 15,
    label = "FOF",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {3,S}
3 O u0 p2 c0 {1,S} {2,S}
""",
    statmech = Conformer(E0=(16.0257,'kJ/mol'), modes=[IdealGasTranslation(mass=(53.9917,'amu')), NonlinearRotor(inertia=([8.34135,45.8552,54.1965],'amu*angstrom^2'), symmetry=2), HarmonicOscillator(frequencies=([486.983,915.713,1034.58],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 16,
    label = "FOBr",
    molecule = 
"""
1 Br u0 p3 c0 {3,S}
2 F  u0 p3 c0 {3,S}
3 O  u0 p2 c0 {1,S} {2,S}
""",
    statmech = Conformer(E0=(58.9402,'kJ/mol'), modes=[IdealGasTranslation(mass=(113.912,'amu')), NonlinearRotor(inertia=([10.5825,124.105,134.687],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([307.891,623.789,907.824],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 17,
    label = "FOCl",
    molecule = 
"""
1 Cl u0 p3 c0 {3,S}
2 F  u0 p3 c0 {3,S}
3 O  u0 p2 c0 {1,S} {2,S}
""",
    statmech = Conformer(E0=(43.2732,'kJ/mol'), modes=[IdealGasTranslation(mass=(69.9622,'amu')), NonlinearRotor(inertia=([9.84142,81.8151,91.6564],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([377.172,701.522,907.894],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 18,
    label = "BrOBr",
    molecule = 
"""
1 Br u0 p3 c0 {3,S}
2 Br u0 p3 c0 {3,S}
3 O  u0 p2 c0 {1,S} {2,S}
""",
    statmech = Conformer(E0=(90.1461,'kJ/mol'), modes=[IdealGasTranslation(mass=(173.832,'amu')), NonlinearRotor(inertia=([14.5554,383.391,397.949],'amu*angstrom^2'), symmetry=2), HarmonicOscillator(frequencies=([180.336,536.291,605.336],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 19,
    label = "ClOCl",
    molecule = 
"""
1 Cl u0 p3 c0 {3,S}
2 Cl u0 p3 c0 {3,S}
3 O  u0 p2 c0 {1,S} {2,S}
""",
    statmech = Conformer(E0=(65.872,'kJ/mol'), modes=[IdealGasTranslation(mass=(85.9326,'amu')), NonlinearRotor(inertia=([11.806,142.077,153.883],'amu*angstrom^2'), symmetry=2), HarmonicOscillator(frequencies=([294.487,656.652,658.631],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 20,
    label = "[O]OF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u1 p2 c0 {2,S}
""",
    statmech = Conformer(E0=(15.6579,'kJ/mol'), modes=[IdealGasTranslation(mass=(50.9882,'amu')), NonlinearRotor(inertia=([6.28174,46.6771,52.9589],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([449.023,679.882,1504.5],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 21,
    label = "ClOBr",
    molecule = 
"""
1 Br u0 p3 c0 {3,S}
2 Cl u0 p3 c0 {3,S}
3 O  u0 p2 c0 {1,S} {2,S}
""",
    statmech = Conformer(E0=(77.9009,'kJ/mol'), modes=[IdealGasTranslation(mass=(129.882,'amu')), NonlinearRotor(inertia=([12.9442,222.573,235.517],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([236.026,567.779,666.708],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 22,
    label = "OD[C]F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {3,S}
2 O u0 p2 c0 {3,D}
3 C u1 p0 c0 {1,S} {2,D}
""",
    statmech = Conformer(E0=(-190.359,'kJ/mol'), modes=[IdealGasTranslation(mass=(46.9933,'amu')), NonlinearRotor(inertia=([2.65864,43.9175,46.5761],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([636.046,1085.22,1918.24],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 23,
    label = "Br[C]Br",
    molecule = 
"""
1 Br u0 p3 c0 {3,S}
2 Br u0 p3 c0 {3,S}
3 C  u0 p1 c0 {1,S} {2,S}
""",
    statmech = Conformer(E0=(326.272,'kJ/mol'), modes=[IdealGasTranslation(mass=(169.837,'amu')), NonlinearRotor(inertia=([13.3207,384.793,398.112],'amu*angstrom^2'), symmetry=2), HarmonicOscillator(frequencies=([192.051,594.308,627.129],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 24,
    label = "OD[C]Cl",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {3,S}
2 O  u0 p2 c0 {3,D}
3 C  u1 p0 c0 {1,S} {2,D}
""",
    statmech = Conformer(E0=(-34.0488,'kJ/mol'), modes=[IdealGasTranslation(mass=(62.9638,'amu')), NonlinearRotor(inertia=([3.25138,88.457,91.7083],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([341.955,585.363,1957.7],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 25,
    label = "Cl[C]Cl",
    molecule = 
"""
1 Cl u0 p3 c0 {3,S}
2 Cl u0 p3 c0 {3,S}
3 C  u0 p1 c0 {1,S} {2,S}
""",
    statmech = Conformer(E0=(215.803,'kJ/mol'), modes=[IdealGasTranslation(mass=(81.9377,'amu')), NonlinearRotor(inertia=([10.4516,140.137,150.588],'amu*angstrom^2'), symmetry=2), HarmonicOscillator(frequencies=([328.197,719.377,727.704],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 26,
    label = "ODCF",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,S} {2,D} {4,S}
4 H u0 p0 c0 {3,S}
""",
    statmech = Conformer(E0=(-394.294,'kJ/mol'), modes=[IdealGasTranslation(mass=(48.0011,'amu')), NonlinearRotor(inertia=([5.46358,42.889,48.3526],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([674.139,1050.3,1121.98,1395.32,1906.92,3070.52],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 27,
    label = "C#CF",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 C u0 p0 c0 {3,T} {4,S}
3 C u0 p0 c0 {1,S} {2,T}
4 H u0 p0 c0 {2,S}
""",
    statmech = Conformer(E0=(95.3311,'kJ/mol'), modes=[IdealGasTranslation(mass=(44.0062,'amu')), LinearRotor(inertia=(51.6236,'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([429.793,429.793,596.357,596.357,1107.96,2365.05,3506.88],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 28,
    label = "C#CBr",
    molecule = 
"""
1 Br u0 p3 c0 {3,S}
2 C  u0 p0 c0 {3,T} {4,S}
3 C  u0 p0 c0 {1,S} {2,T}
4 H  u0 p0 c0 {2,S}
""",
    statmech = Conformer(E0=(260.78,'kJ/mol'), modes=[IdealGasTranslation(mass=(103.926,'amu')), LinearRotor(inertia=(126.194,'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([311.446,608.017,611.781,651.471,2193.88,3510.45],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 29,
    label = "C#CCl",
    molecule = 
"""
1 Cl u0 p3 c0 {3,S}
2 C  u0 p0 c0 {3,T} {4,S}
3 C  u0 p0 c0 {1,S} {2,T}
4 H  u0 p0 c0 {2,S}
""",
    statmech = Conformer(E0=(212.868,'kJ/mol'), modes=[IdealGasTranslation(mass=(59.9767,'amu')), LinearRotor(inertia=(88.9511,'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([339.385,525.562,605.246,755.351,2216.61,3507.87],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 30,
    label = "ODCCl",
    molecule = 
"""
1 Cl u0 p3 c0 {3,S}
2 O  u0 p2 c0 {3,D}
3 C  u0 p0 c0 {1,S} {2,D} {4,S}
4 H  u0 p0 c0 {3,S}
""",
    statmech = Conformer(E0=(-195.913,'kJ/mol'), modes=[IdealGasTranslation(mass=(63.9716,'amu')), NonlinearRotor(inertia=([6.45406,84.1063,90.5605],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([445.967,720.87,950.292,1328.07,1875.69,3061.07],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 31,
    label = "FC#CF",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {4,S}
3 C u0 p0 c0 {1,S} {4,T}
4 C u0 p0 c0 {2,S} {3,T}
""",
    statmech = Conformer(E0=(-6.58462,'kJ/mol'), modes=[IdealGasTranslation(mass=(61.9968,'amu')), LinearRotor(inertia=(141.582,'amu*angstrom^2'), symmetry=2), HarmonicOscillator(frequencies=([284.265,284.265,295.939,295.939,811.153,1396.68,2594.35],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 32,
    label = "F[CH]F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {3,S}
3 C u1 p0 c0 {1,S} {2,S} {4,S}
4 H u0 p0 c0 {3,S}
""",
    statmech = Conformer(E0=(-256.71,'kJ/mol'), modes=[IdealGasTranslation(mass=(51.0046,'amu')), NonlinearRotor(inertia=([7.43413,45.9439,52.5803],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([549.125,1005.77,1195.1,1212.61,1359.42,3085.19],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 33,
    label = "[CH2]F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
""",
    statmech = Conformer(E0=(-42.5685,'kJ/mol'), modes=[IdealGasTranslation(mass=(33.0141,'amu')), NonlinearRotor(inertia=([1.91548,16.2277,17.9803],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([576.418,1180.5,1217.62,1485.55,3118.23,3268.88],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 34,
    label = "FC#CBr",
    molecule = 
"""
1 Br u0 p3 c0 {4,S}
2 F  u0 p3 c0 {3,S}
3 C  u0 p0 c0 {2,S} {4,T}
4 C  u0 p0 c0 {1,S} {3,T}
""",
    statmech = Conformer(E0=(146.838,'kJ/mol'), modes=[IdealGasTranslation(mass=(121.917,'amu')), LinearRotor(inertia=(334.075,'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([190.031,394.631,395.041,466.989,1221.39,2458.97],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 35,
    label = "FC#CCl",
    molecule = 
"""
1 Cl u0 p3 c0 {4,S}
2 F  u0 p3 c0 {3,S}
3 C  u0 p0 c0 {2,S} {4,T}
4 C  u0 p0 c0 {1,S} {3,T}
""",
    statmech = Conformer(E0=(102.809,'kJ/mol'), modes=[IdealGasTranslation(mass=(77.9673,'amu')), LinearRotor(inertia=(227.155,'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([220.296,382.131,383.096,595.447,1251.76,2478.96],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 36,
    label = "BrC#CBr",
    molecule = 
"""
1 Br u0 p3 c0 {3,S}
2 Br u0 p3 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,T}
4 C  u0 p0 c0 {2,S} {3,T}
""",
    statmech = Conformer(E0=(305.177,'kJ/mol'), modes=[IdealGasTranslation(mass=(181.837,'amu')), NonlinearRotor(inertia=([0.0136516,911.545,911.562],'amu*angstrom^2'), symmetry=2), HarmonicOscillator(frequencies=([144.674,292.494,340.656,340.698,848.891,2296.48],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 37,
    label = "[CH2]Br",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {2,S}
2 C  u1 p0 c0 {1,S} {3,S} {4,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
""",
    statmech = Conformer(E0=(154.071,'kJ/mol'), modes=[IdealGasTranslation(mass=(92.934,'amu')), NonlinearRotor(inertia=([1.84611,44.8453,46.6643],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([192.239,698.445,927.79,1379.44,3177.22,3336.09],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 38,
    label = "[C]DCBr",
    molecule = 
"""
multiplicity 3
1 Br u0 p3 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,D} {4,S}
3 C  u2 p0 c0 {2,D}
4 H  u0 p0 c0 {2,S}
""",
    statmech = Conformer(E0=(616.297,'kJ/mol'), modes=[IdealGasTranslation(mass=(103.926,'amu')), NonlinearRotor(inertia=([7.80224,110.951,118.676],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([314.669,508.852,597.732,1073.21,1186.08,3152.17],'cm^-1'))], spin_multiplicity=3),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 39,
    label = "[C]DCCl",
    molecule = 
"""
1 Cl u0 p3 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,D} {4,S}
3 C  u0 p1 c0 {2,D}
4 H  u0 p0 c0 {2,S}
""",
    statmech = Conformer(E0=(414.771,'kJ/mol'), modes=[IdealGasTranslation(mass=(59.9767,'amu')), NonlinearRotor(inertia=([8.05537,69.0342,77.0895],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([98.6439,689.146,742.323,1025.71,1654.67,3206.32],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 40,
    label = "[CH2]Cl",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {2,S}
2 C  u1 p0 c0 {1,S} {3,S} {4,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
""",
    statmech = Conformer(E0=(101.842,'kJ/mol'), modes=[IdealGasTranslation(mass=(48.9845,'amu')), NonlinearRotor(inertia=([1.83992,32.1128,33.9492],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([71.6564,833.938,988.217,1405.41,3177.25,3333.23],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 41,
    label = "ClC#CCl",
    molecule = 
"""
1 Cl u0 p3 c0 {3,S}
2 Cl u0 p3 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,T}
4 C  u0 p0 c0 {2,S} {3,T}
""",
    statmech = Conformer(E0=(214.946,'kJ/mol'), modes=[IdealGasTranslation(mass=(93.9377,'amu')), NonlinearRotor(inertia=([0.0016358,359.603,359.603],'amu*angstrom^2'), symmetry=2), HarmonicOscillator(frequencies=([182.447,352.518,352.525,478.545,999.704,2340.93],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 42,
    label = "ODC(F)F",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 O u0 p2 c0 {4,D}
4 C u0 p0 c0 {1,S} {2,S} {3,D}
""",
    statmech = Conformer(E0=(-618.61,'kJ/mol'), modes=[IdealGasTranslation(mass=(65.9917,'amu')), NonlinearRotor(inertia=([42.7382,43.0674,85.8056],'amu*angstrom^2'), symmetry=2), HarmonicOscillator(frequencies=([584.127,619.74,793.429,989.231,1281.66,1989.03],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 43,
    label = "F[CH]Cl",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {3,S}
2 F  u0 p3 c0 {3,S}
3 C  u1 p0 c0 {1,S} {2,S} {4,S}
4 H  u0 p0 c0 {3,S}
""",
    statmech = Conformer(E0=(-80.4491,'kJ/mol'), modes=[IdealGasTranslation(mass=(66.9751,'amu')), NonlinearRotor(inertia=([8.65695,86.6737,94.6951],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([402.152,715.689,848.488,1208.82,1304.11,3155.12],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 44,
    label = "ClC#CBr",
    molecule = 
"""
1 Br u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {3,S}
3 C  u0 p0 c0 {2,S} {4,T}
4 C  u0 p0 c0 {1,S} {3,T}
""",
    statmech = Conformer(E0=(259.994,'kJ/mol'), modes=[IdealGasTranslation(mass=(137.887,'amu')), LinearRotor(inertia=(547.148,'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([161.696,354.949,355.06,378.901,935.478,2319.13],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 45,
    label = "F[CH]Br",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {3,S}
2 F  u0 p3 c0 {3,S}
3 C  u1 p0 c0 {1,S} {2,S} {4,S}
4 H  u0 p0 c0 {3,S}
""",
    statmech = Conformer(E0=(-25.4646,'kJ/mol'), modes=[IdealGasTranslation(mass=(110.925,'amu')), NonlinearRotor(inertia=([9.14834,130.713,139.198],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([330.149,637.151,790.457,1208.7,1288.97,3147.38],'cm^-1'))], spin_multiplicity=2, optical_isomers=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 46,
    label = "Br[CH]Br",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {3,S}
2 Br u0 p3 c0 {3,S}
3 C  u1 p0 c0 {1,S} {2,S} {4,S}
4 H  u0 p0 c0 {3,S}
""",
    statmech = Conformer(E0=(177.336,'kJ/mol'), modes=[IdealGasTranslation(mass=(170.845,'amu')), NonlinearRotor(inertia=([13.1771,414.966,427.769],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([182.933,431.487,620.768,760.254,1176.22,3217.5],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 47,
    label = "Cl[CH]Cl",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {3,S}
2 Cl u0 p3 c0 {3,S}
3 C  u1 p0 c0 {1,S} {2,S} {4,S}
4 H  u0 p0 c0 {3,S}
""",
    statmech = Conformer(E0=(75.4383,'kJ/mol'), modes=[IdealGasTranslation(mass=(82.9455,'amu')), NonlinearRotor(inertia=([10.8395,152.824,163.314],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([300.015,471.545,752.601,875.281,1225.98,3221.05],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 48,
    label = "F[C](F)F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 F u0 p3 c0 {4,S}
4 C u1 p0 c0 {1,S} {2,S} {3,S}
""",
    statmech = Conformer(E0=(-483.19,'kJ/mol'), modes=[IdealGasTranslation(mass=(68.9952,'amu')), NonlinearRotor(inertia=([46.5949,46.5949,90.0934],'amu*angstrom^2'), symmetry=3), HarmonicOscillator(frequencies=([504.804,504.824,700.362,1092.66,1279.94,1279.95],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 49,
    label = "ODCD[C]F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {3,S}
2 O u0 p2 c0 {4,D}
3 C u1 p0 c0 {1,S} {4,D}
4 C u0 p0 c0 {2,D} {3,D}
""",
    statmech = Conformer(E0=(33.6712,'kJ/mol'), modes=[IdealGasTranslation(mass=(58.9933,'amu')), NonlinearRotor(inertia=([3.58812,117.154,120.742],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([280.764,365.894,563.98,866.433,1429.66,2068.95],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 50,
    label = "ODC(F)Br",
    molecule = 
"""
1 Br u0 p3 c0 {4,S}
2 F  u0 p3 c0 {4,S}
3 O  u0 p2 c0 {4,D}
4 C  u0 p0 c0 {1,S} {2,S} {3,D}
""",
    statmech = Conformer(E0=(-370.972,'kJ/mol'), modes=[IdealGasTranslation(mass=(125.912,'amu')), NonlinearRotor(inertia=([42.7562,163.132,205.888],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([340.955,381.714,631.407,725.551,1115.8,1941.34],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 51,
    label = "Cl[CH]Br",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {3,S}
2 Cl u0 p3 c0 {3,S}
3 C  u1 p0 c0 {1,S} {2,S} {4,S}
4 H  u0 p0 c0 {3,S}
""",
    statmech = Conformer(E0=(126.863,'kJ/mol'), modes=[IdealGasTranslation(mass=(126.895,'amu')), NonlinearRotor(inertia=([11.8295,238.782,250.25],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([241.769,449.78,664.437,843.488,1202.56,3218.64],'cm^-1'))], spin_multiplicity=2, optical_isomers=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 52,
    label = "ODC(F)Cl",
    molecule = 
"""
1 Cl u0 p3 c0 {4,S}
2 F  u0 p3 c0 {4,S}
3 O  u0 p2 c0 {4,D}
4 C  u0 p0 c0 {1,S} {2,S} {3,D}
""",
    statmech = Conformer(E0=(-424.498,'kJ/mol'), modes=[IdealGasTranslation(mass=(81.9622,'amu')), NonlinearRotor(inertia=([42.7554,97.1037,139.859],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([405.507,488.74,676.18,758.393,1132.89,1942.29],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 53,
    label = "ODC(Br)Br",
    molecule = 
"""
1 Br u0 p3 c0 {4,S}
2 Br u0 p3 c0 {4,S}
3 O  u0 p2 c0 {4,D}
4 C  u0 p0 c0 {1,S} {2,S} {3,D}
""",
    statmech = Conformer(E0=(-132.616,'kJ/mol'), modes=[IdealGasTranslation(mass=(185.832,'amu')), NonlinearRotor(inertia=([81.6672,409.459,491.126],'amu*angstrom^2'), symmetry=2), HarmonicOscillator(frequencies=([175.613,343.344,418.535,518.506,727.523,1906.4],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 54,
    label = "ODCD[C]Br",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {3,S}
2 O  u0 p2 c0 {4,D}
3 C  u1 p0 c0 {1,S} {4,D}
4 C  u0 p0 c0 {2,D} {3,D}
""",
    statmech = Conformer(E0=(210.198,'kJ/mol'), modes=[IdealGasTranslation(mass=(118.913,'amu')), NonlinearRotor(inertia=([0.000599134,300.294,300.294],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([468.552,490.907,1472.98,2203.84],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 55,
    label = "ODCD[C]Cl",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {3,S}
2 O  u0 p2 c0 {4,D}
3 C  u1 p0 c0 {1,S} {4,D}
4 C  u0 p0 c0 {2,D} {3,D}
""",
    statmech = Conformer(E0=(153.002,'kJ/mol'), modes=[IdealGasTranslation(mass=(74.9638,'amu')), NonlinearRotor(inertia=([4.56542,187.658,192.224],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([171.127,427.175,534.979,655.214,1366.65,2115.94],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 56,
    label = "ODC(Cl)Cl",
    molecule = 
"""
1 Cl u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {4,S}
3 O  u0 p2 c0 {4,D}
4 C  u0 p0 c0 {1,S} {2,S} {3,D}
""",
    statmech = Conformer(E0=(-234.96,'kJ/mol'), modes=[IdealGasTranslation(mass=(97.9326,'amu')), NonlinearRotor(inertia=([64.564,148.201,212.765],'amu*angstrom^2'), symmetry=2), HarmonicOscillator(frequencies=([297.21,435.335,562.966,587.836,818.535,1900.58],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 57,
    label = "[O]C(DO)F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {4,S}
2 O u1 p2 c0 {4,S}
3 O u0 p2 c0 {4,D}
4 C u0 p0 c0 {1,S} {2,S} {3,D}
""",
    statmech = Conformer(E0=(-381.43,'kJ/mol'), modes=[IdealGasTranslation(mass=(62.9882,'amu')), NonlinearRotor(inertia=([36.4335,44.7291,81.1626],'amu*angstrom^2'), symmetry=2), HarmonicOscillator(frequencies=([509.533,537.43,765.261,1011.27,1202.3,1550.29],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 58,
    label = "ODC(Cl)Br",
    molecule = 
"""
1 Br u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {4,S}
3 O  u0 p2 c0 {4,D}
4 C  u0 p0 c0 {1,S} {2,S} {3,D}
""",
    statmech = Conformer(E0=(-183.278,'kJ/mol'), modes=[IdealGasTranslation(mass=(141.882,'amu')), NonlinearRotor(inertia=([69.8291,243.662,313.491],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([235.845,367.338,510.227,552.362,776.783,1902.47],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 59,
    label = "F[C](F)Br",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {4,S}
2 F  u0 p3 c0 {4,S}
3 F  u0 p3 c0 {4,S}
4 C  u1 p0 c0 {1,S} {2,S} {3,S}
""",
    statmech = Conformer(E0=(-236.209,'kJ/mol'), modes=[IdealGasTranslation(mass=(128.915,'amu')), NonlinearRotor(inertia=([46.0096,175.865,218.527],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([302.62,314.974,582.634,664.124,1174.8,1255.93],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 60,
    label = "F[C](F)Cl",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {4,S}
2 F  u0 p3 c0 {4,S}
3 F  u0 p3 c0 {4,S}
4 C  u1 p0 c0 {1,S} {2,S} {3,S}
""",
    statmech = Conformer(E0=(-290.344,'kJ/mol'), modes=[IdealGasTranslation(mass=(84.9657,'amu')), NonlinearRotor(inertia=([46.183,103.887,146.915],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([356.428,411.5,598.635,736.746,1178.21,1264.7],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 61,
    label = "F[C](Cl)Br",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {4,S}
3 F  u0 p3 c0 {4,S}
4 C  u1 p0 c0 {1,S} {2,S} {3,S}
""",
    statmech = Conformer(E0=(-57.7131,'kJ/mol'), modes=[IdealGasTranslation(mass=(144.886,'amu')), NonlinearRotor(inertia=([73.3333,253.987,324.248],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([222.338,322.26,432.126,524.693,837.564,1203.03],'cm^-1'))], spin_multiplicity=2, optical_isomers=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 62,
    label = "F[C](Br)Br",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {4,S}
2 Br u0 p3 c0 {4,S}
3 F  u0 p3 c0 {4,S}
4 C  u1 p0 c0 {1,S} {2,S} {3,S}
""",
    statmech = Conformer(E0=(-5.47205,'kJ/mol'), modes=[IdealGasTranslation(mass=(188.835,'amu')), NonlinearRotor(inertia=([85.3637,422.134,504.244],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([168.453,306.578,370.915,475.267,776.547,1197.14],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 63,
    label = "F[C](Cl)Cl",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {4,S}
3 F  u0 p3 c0 {4,S}
4 C  u1 p0 c0 {1,S} {2,S} {3,S}
""",
    statmech = Conformer(E0=(-110.328,'kJ/mol'), modes=[IdealGasTranslation(mass=(100.936,'amu')), NonlinearRotor(inertia=([68.178,154.983,220.264],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([275.493,376.359,459.655,585.28,879.809,1210.06],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 64,
    label = "Br[C](Br)Br",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {4,S}
2 Br u0 p3 c0 {4,S}
3 Br u0 p3 c0 {4,S}
4 C  u1 p0 c0 {1,S} {2,S} {3,S}
""",
    statmech = Conformer(E0=(201.767,'kJ/mol'), modes=[IdealGasTranslation(mass=(248.755,'amu')), NonlinearRotor(inertia=([409.23,409.267,816.246],'amu*angstrom^2'), symmetry=3), HarmonicOscillator(frequencies=([157.432,157.452,238.325,313.71,753.872,754.045],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 65,
    label = "Cl[C](Cl)Cl",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {4,S}
3 Cl u0 p3 c0 {4,S}
4 C  u1 p0 c0 {1,S} {2,S} {3,S}
""",
    statmech = Conformer(E0=(53.3311,'kJ/mol'), modes=[IdealGasTranslation(mass=(116.907,'amu')), NonlinearRotor(inertia=([151.859,151.861,301.692],'amu*angstrom^2'), symmetry=3), HarmonicOscillator(frequencies=([269.097,269.125,326.781,481.886,874.947,875.024],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 66,
    label = "Cl[C](Br)Br",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {4,S}
2 Br u0 p3 c0 {4,S}
3 Cl u0 p3 c0 {4,S}
4 C  u1 p0 c0 {1,S} {2,S} {3,S}
""",
    statmech = Conformer(E0=(152.703,'kJ/mol'), modes=[IdealGasTranslation(mass=(204.806,'amu')), NonlinearRotor(inertia=([199.67,410.971,608.465],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([172.273,207.677,277.431,362.519,762.921,838.543],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 67,
    label = "Cl[C](Cl)Br",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {4,S}
3 Cl u0 p3 c0 {4,S}
4 C  u1 p0 c0 {1,S} {2,S} {3,S}
""",
    statmech = Conformer(E0=(103.335,'kJ/mol'), modes=[IdealGasTranslation(mass=(160.856,'amu')), NonlinearRotor(inertia=([151.261,277.484,426.635],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([220.011,231.901,306.266,420.528,813.104,867.128],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 68,
    label = "CF",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    statmech = Conformer(E0=(-246.136,'kJ/mol'), modes=[IdealGasTranslation(mass=(34.0219,'amu')), NonlinearRotor(inertia=([3.21737,19.5168,19.5168],'amu*angstrom^2'), symmetry=3), HarmonicOscillator(frequencies=([1097.73,1206.94,1206.96,1493.65,1493.66,1509.77,3011.42,3086.11,3086.13],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 69,
    label = "CBr",
    molecule = 
"""
1 Br u0 p3 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
""",
    statmech = Conformer(E0=(-45.7885,'kJ/mol'), modes=[IdealGasTranslation(mass=(93.9418,'amu')), NonlinearRotor(inertia=([3.24397,53.5654,53.5655],'amu*angstrom^2'), symmetry=3), HarmonicOscillator(frequencies=([598.906,962.174,962.209,1328.85,1472.19,1472.21,3087.13,3198.36,3198.39],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 70,
    label = "CCl",
    molecule = 
"""
1 Cl u0 p3 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
""",
    statmech = Conformer(E0=(-92.0054,'kJ/mol'), modes=[IdealGasTranslation(mass=(49.9923,'amu')), NonlinearRotor(inertia=([3.23068,38.5536,38.5536],'amu*angstrom^2'), symmetry=3), HarmonicOscillator(frequencies=([720.467,1022.71,1022.74,1374.98,1478.46,1478.48,3074.63,3177.63,3177.69],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 71,
    label = "FCF",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {3,S}
3 C u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
""",
    statmech = Conformer(E0=(-461.907,'kJ/mol'), modes=[IdealGasTranslation(mass=(52.0125,'amu')), NonlinearRotor(inertia=([10.1284,47.6239,54.4207],'amu*angstrom^2'), symmetry=2), HarmonicOscillator(frequencies=([531.881,1130.54,1136.09,1194.11,1273.86,1488.46,1538.71,3014.54,3074.22],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 72,
    label = "FCCl",
    molecule = 
"""
1 Cl u0 p3 c0 {3,S}
2 F  u0 p3 c0 {3,S}
3 C  u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H  u0 p0 c0 {3,S}
5 H  u0 p0 c0 {3,S}
""",
    statmech = Conformer(E0=(-274.243,'kJ/mol'), modes=[IdealGasTranslation(mass=(67.9829,'amu')), NonlinearRotor(inertia=([11.9723,90.1476,98.8128],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([376.936,724.433,1006.07,1127.84,1255.98,1373.33,1510.04,3071.91,3147.26],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 73,
    label = "FCBr",
    molecule = 
"""
1 Br u0 p3 c0 {3,S}
2 F  u0 p3 c0 {3,S}
3 C  u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H  u0 p0 c0 {3,S}
5 H  u0 p0 c0 {3,S}
""",
    statmech = Conformer(E0=(-221.099,'kJ/mol'), modes=[IdealGasTranslation(mass=(111.932,'amu')), NonlinearRotor(inertia=([12.5828,136.447,145.709],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([306.175,619.921,941.972,1128.01,1248.6,1332.8,1505.28,3081.84,3164.24],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 74,
    label = "BrCBr",
    molecule = 
"""
1 Br u0 p3 c0 {3,S}
2 Br u0 p3 c0 {3,S}
3 C  u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H  u0 p0 c0 {3,S}
5 H  u0 p0 c0 {3,S}
""",
    statmech = Conformer(E0=(-8.03713,'kJ/mol'), modes=[IdealGasTranslation(mass=(171.852,'amu')), NonlinearRotor(inertia=([19.1674,420.683,436.575],'amu*angstrom^2'), symmetry=2), HarmonicOscillator(frequencies=([168.009,574.099,629.845,815.319,1109.49,1215.27,1431.57,3137.6,3228.53],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 75,
    label = "ClCCl",
    molecule = 
"""
1 Cl u0 p3 c0 {3,S}
2 Cl u0 p3 c0 {3,S}
3 C  u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H  u0 p0 c0 {3,S}
5 H  u0 p0 c0 {3,S}
""",
    statmech = Conformer(E0=(-105.155,'kJ/mol'), modes=[IdealGasTranslation(mass=(83.9534,'amu')), NonlinearRotor(inertia=([15.7173,156.605,169.055],'amu*angstrom^2'), symmetry=2), HarmonicOscillator(frequencies=([278.667,704.675,730.864,896.886,1162.39,1281.79,1455.17,3120.24,3202.68],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 76,
    label = "[O]CF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {3,S}
2 O u1 p2 c0 {3,S}
3 C u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
""",
    statmech = Conformer(E0=(-220.7,'kJ/mol'), modes=[IdealGasTranslation(mass=(49.009,'amu')), NonlinearRotor(inertia=([8.89593,46.7012,52.3875],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([558.515,760.247,1040.95,1161.07,1162.34,1315.05,1378.4,2858.27,2872.23],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 77,
    label = "ClCBr",
    molecule = 
"""
1 Br u0 p3 c0 {3,S}
2 Cl u0 p3 c0 {3,S}
3 C  u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H  u0 p0 c0 {3,S}
5 H  u0 p0 c0 {3,S}
""",
    statmech = Conformer(E0=(-56.08,'kJ/mol'), modes=[IdealGasTranslation(mass=(127.903,'amu')), NonlinearRotor(inertia=([17.1541,244.273,258.153],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([222.206,596.371,725.016,851.856,1139.5,1246.82,1444.54,3128.97,3216],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 78,
    label = "[O]CBr",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {3,S}
2 O  u1 p2 c0 {3,S}
3 C  u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H  u0 p0 c0 {3,S}
5 H  u0 p0 c0 {3,S}
""",
    statmech = Conformer(E0=(17.2039,'kJ/mol'), modes=[IdealGasTranslation(mass=(108.929,'amu')), NonlinearRotor(inertia=([10.5859,135.969,143.34],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([297.668,532.854,562.411,988.481,1137.79,1189.73,1302.72,2927.39,2969.89],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 79,
    label = "[O]CCl",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {3,S}
2 O  u1 p2 c0 {3,S}
3 C  u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H  u0 p0 c0 {3,S}
5 H  u0 p0 c0 {3,S}
""",
    statmech = Conformer(E0=(-33.3793,'kJ/mol'), modes=[IdealGasTranslation(mass=(64.9794,'amu')), NonlinearRotor(inertia=([10.2479,90.1569,97.2096],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([378.783,650.242,651.901,1030.67,1153.86,1235.18,1310.46,2923.79,2961.37],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 80,
    label = "FC(F)F",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 F u0 p3 c0 {4,S}
4 C u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 H u0 p0 c0 {4,S}
""",
    statmech = Conformer(E0=(-707.987,'kJ/mol'), modes=[IdealGasTranslation(mass=(70.003,'amu')), NonlinearRotor(inertia=([48.8559,48.8561,89.1073],'amu*angstrom^2'), symmetry=3), HarmonicOscillator(frequencies=([506.193,506.206,703.466,1151.07,1179.84,1179.87,1414.02,1414.02,3086.64],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 81,
    label = "ODCDCF",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 O u0 p2 c0 {4,D}
3 C u0 p0 c0 {1,S} {4,D} {5,S}
4 C u0 p0 c0 {2,D} {3,D}
5 H u0 p0 c0 {3,S}
""",
    statmech = Conformer(E0=(-172.285,'kJ/mol'), modes=[IdealGasTranslation(mass=(60.0011,'amu')), NonlinearRotor(inertia=([9.01649,110.348,119.365],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([238.894,460.044,539.472,686.431,1048.64,1208.61,1432.92,2235.18,3235.83],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 82,
    label = "CD[C]F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {3,S}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u1 p0 c0 {1,S} {2,D}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    statmech = Conformer(E0=(96.664,'kJ/mol'), modes=[IdealGasTranslation(mass=(45.014,'amu')), NonlinearRotor(inertia=([4.28106,49.5096,53.7907],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([443.335,623.171,819.82,951.292,1166.86,1400.31,1729.5,3121.37,3250.42],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 83,
    label = "ODCDCBr",
    molecule = 
"""
1 Br u0 p3 c0 {3,S}
2 O  u0 p2 c0 {4,D}
3 C  u0 p0 c0 {1,S} {4,D} {5,S}
4 C  u0 p0 c0 {2,D} {3,D}
5 H  u0 p0 c0 {3,S}
""",
    statmech = Conformer(E0=(-4.32818,'kJ/mol'), modes=[IdealGasTranslation(mass=(119.921,'amu')), NonlinearRotor(inertia=([16.4471,243.624,260.072],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([155.466,442.342,517.061,538.93,744.559,1115.51,1303.19,2241,3262.15],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 84,
    label = "CD[C]Br",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {3,S}
2 C  u0 p0 c0 {3,D} {4,S} {5,S}
3 C  u1 p0 c0 {1,S} {2,D}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
""",
    statmech = Conformer(E0=(292.759,'kJ/mol'), modes=[IdealGasTranslation(mass=(104.934,'amu')), NonlinearRotor(inertia=([4.78824,126.193,130.981],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([314.231,499.039,575.8,871.836,979.078,1383.83,1679.99,3104.57,3194.3],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 85,
    label = "CD[C]Cl",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {3,S}
2 C  u0 p0 c0 {3,D} {4,S} {5,S}
3 C  u1 p0 c0 {1,S} {2,D}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
""",
    statmech = Conformer(E0=(243.459,'kJ/mol'), modes=[IdealGasTranslation(mass=(60.9845,'amu')), NonlinearRotor(inertia=([4.56487,87.8967,92.4617],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([351.067,530.645,703.675,864.669,999.572,1389.86,1687.13,3106.35,3206.48],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 86,
    label = "ODCDCCl",
    molecule = 
"""
1 Cl u0 p3 c0 {3,S}
2 O  u0 p2 c0 {4,D}
3 C  u0 p0 c0 {1,S} {4,D} {5,S}
4 C  u0 p0 c0 {2,D} {3,D}
5 H  u0 p0 c0 {3,S}
""",
    statmech = Conformer(E0=(-45.1093,'kJ/mol'), modes=[IdealGasTranslation(mass=(75.9716,'amu')), NonlinearRotor(inertia=([13.9949,169.001,182.996],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([182.759,478.163,528.798,591.079,812.41,1138.05,1325.57,2242.66,3251.53],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 87,
    label = "F[C]DCF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {4,S}
3 C u0 p0 c0 {1,S} {4,D} {5,S}
4 C u1 p0 c0 {2,S} {3,D}
5 H u0 p0 c0 {3,S}
""",
    statmech = Conformer(E0=(-58.4765,'kJ/mol'), modes=[IdealGasTranslation(mass=(63.0046,'amu')), NonlinearRotor(inertia=([18.6764,93.2568,111.933],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([203.406,408.59,750.559,801.84,1025.92,1150.34,1361.98,1782.01,3238.53],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 88,
    label = "[CH]DCF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 C u1 p0 c0 {2,D} {5,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
""",
    statmech = Conformer(E0=(105.848,'kJ/mol'), modes=[IdealGasTranslation(mass=(45.014,'amu')), NonlinearRotor(inertia=([5.5521,46.519,52.0711],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([479.323,636.63,751.886,824.049,1132.49,1303.18,1700.02,3107.67,3318.48],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 89,
    label = "FC(F)Cl",
    molecule = 
"""
1 Cl u0 p3 c0 {4,S}
2 F  u0 p3 c0 {4,S}
3 F  u0 p3 c0 {4,S}
4 C  u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 H  u0 p0 c0 {4,S}
""",
    statmech = Conformer(E0=(-494.235,'kJ/mol'), modes=[IdealGasTranslation(mass=(85.9735,'amu')), NonlinearRotor(inertia=([49.2457,106.319,146.25],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([358.282,399.757,600.628,774.067,1140.68,1179.5,1317.46,1394.06,3110.5],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 90,
    label = "FC(F)Br",
    molecule = 
"""
1 Br u0 p3 c0 {4,S}
2 F  u0 p3 c0 {4,S}
3 F  u0 p3 c0 {4,S}
4 C  u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 H  u0 p0 c0 {4,S}
""",
    statmech = Conformer(E0=(-436.27,'kJ/mol'), modes=[IdealGasTranslation(mass=(129.923,'amu')), NonlinearRotor(inertia=([49.418,177.881,217.709],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([309.169,309.87,585.766,692.202,1135.65,1180.42,1286.7,1388.31,3112.33],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 91,
    label = "[CH]DCBr",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,D} {4,S}
3 C  u1 p0 c0 {2,D} {5,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {3,S}
""",
    statmech = Conformer(E0=(302.998,'kJ/mol'), modes=[IdealGasTranslation(mass=(104.934,'amu')), NonlinearRotor(inertia=([9.25675,116.4,125.657],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([289.633,502.033,645.818,729.586,828.799,1149.59,1653.17,3226.96,3330.28],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 92,
    label = "[CH]DCCl",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,D} {4,S}
3 C  u1 p0 c0 {2,D} {5,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {3,S}
""",
    statmech = Conformer(E0=(259.373,'kJ/mol'), modes=[IdealGasTranslation(mass=(60.9845,'amu')), NonlinearRotor(inertia=([8.70984,79.4661,88.1758],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([343.177,646.109,658.02,778.79,845.932,1211.66,1645.12,3210.77,3316.41],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 93,
    label = "[O]C(F)F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 O u1 p2 c0 {4,S}
4 C u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 H u0 p0 c0 {4,S}
""",
    statmech = Conformer(E0=(-426.241,'kJ/mol'), modes=[IdealGasTranslation(mass=(66.9995,'amu')), NonlinearRotor(inertia=([47.2408,48.1768,88.2639],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([480.226,502.831,615.399,942.972,1118.44,1159.86,1274.53,1324.03,2842.12],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 94,
    label = "F[C]DCCl",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {3,S}
2 F  u0 p3 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,D} {5,S}
4 C  u1 p0 c0 {2,S} {3,D}
5 H  u0 p0 c0 {3,S}
""",
    statmech = Conformer(E0=(86.239,'kJ/mol'), modes=[IdealGasTranslation(mass=(78.9751,'amu')), NonlinearRotor(inertia=([26.6334,143.723,170.357],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([172.12,415.764,639.463,747.08,748.691,1077.28,1264.46,1757.92,3258.4],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 95,
    label = "FC(Cl)Cl",
    molecule = 
"""
1 Cl u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {4,S}
3 F  u0 p3 c0 {4,S}
4 C  u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 H  u0 p0 c0 {4,S}
""",
    statmech = Conformer(E0=(-296.618,'kJ/mol'), modes=[IdealGasTranslation(mass=(101.944,'amu')), NonlinearRotor(inertia=([72.6289,157.352,219.819],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([268.486,362.241,451.044,721.28,762.213,1141.75,1244.09,1339.23,3140.03],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 96,
    label = "FC(Br)Br",
    molecule = 
"""
1 Br u0 p3 c0 {4,S}
2 Br u0 p3 c0 {4,S}
3 F  u0 p3 c0 {4,S}
4 C  u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 H  u0 p0 c0 {4,S}
""",
    statmech = Conformer(E0=(-189.138,'kJ/mol'), modes=[IdealGasTranslation(mass=(189.843,'amu')), NonlinearRotor(inertia=([91.4215,419.778,500.35],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([164.71,294.328,352.983,611.885,674.333,1135.72,1180.18,1320.55,3147.24],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 97,
    label = "FC(Cl)Br",
    molecule = 
"""
1 Br u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {4,S}
3 F  u0 p3 c0 {4,S}
4 C  u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 H  u0 p0 c0 {4,S}
""",
    statmech = Conformer(E0=(-242.481,'kJ/mol'), modes=[IdealGasTranslation(mass=(145.893,'amu')), NonlinearRotor(inertia=([78.3286,255.572,323.414],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([216.567,308.946,419.417,642.262,745.663,1138.57,1211.85,1330.59,3143.81],'cm^-1'))], optical_isomers=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 98,
    label = "F[C]DCBr",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {3,S}
2 F  u0 p3 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,D} {5,S}
4 C  u1 p0 c0 {2,S} {3,D}
5 H  u0 p0 c0 {3,S}
""",
    statmech = Conformer(E0=(130.083,'kJ/mol'), modes=[IdealGasTranslation(mass=(122.925,'amu')), NonlinearRotor(inertia=([29.7714,214.415,244.187],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([145.327,405.16,540.882,681.375,728.259,1066.5,1220.54,1763.39,3266.68],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 99,
    label = "Br[C]DCBr",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {3,S}
2 Br u0 p3 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,D} {5,S}
4 C  u1 p0 c0 {2,S} {3,D}
5 H  u0 p0 c0 {3,S}
""",
    statmech = Conformer(E0=(315.084,'kJ/mol'), modes=[IdealGasTranslation(mass=(182.845,'amu')), NonlinearRotor(inertia=([45.6237,580.182,625.802],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([84.2335,338.191,463.718,547.722,636.435,722.919,1162.24,1689.51,3222.87],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 100,
    label = "BrC(Br)Br",
    molecule = 
"""
1 Br u0 p3 c0 {4,S}
2 Br u0 p3 c0 {4,S}
3 Br u0 p3 c0 {4,S}
4 C  u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 H  u0 p0 c0 {4,S}
""",
    statmech = Conformer(E0=(33.0731,'kJ/mol'), modes=[IdealGasTranslation(mass=(249.763,'amu')), NonlinearRotor(inertia=([415.055,415.068,817.488],'amu*angstrom^2'), symmetry=3), HarmonicOscillator(frequencies=([150.035,150.112,220.629,532.201,639.283,639.873,1161.47,1161.62,3194.16],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 101,
    label = "ClC(Cl)Cl",
    molecule = 
"""
1 Cl u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {4,S}
3 Cl u0 p3 c0 {4,S}
4 C  u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 H  u0 p0 c0 {4,S}
""",
    statmech = Conformer(E0=(-115.473,'kJ/mol'), modes=[IdealGasTranslation(mass=(117.914,'amu')), NonlinearRotor(inertia=([156.617,156.619,302.014],'amu*angstrom^2'), symmetry=3), HarmonicOscillator(frequencies=([256.159,256.159,362.546,664.93,741.878,742.288,1226.22,1226.28,3175.6],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 102,
    label = "Cl[C]DCCl",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {3,S}
2 Cl u0 p3 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,D} {5,S}
4 C  u1 p0 c0 {2,S} {3,D}
5 H  u0 p0 c0 {3,S}
""",
    statmech = Conformer(E0=(223.629,'kJ/mol'), modes=[IdealGasTranslation(mass=(94.9455,'amu')), NonlinearRotor(inertia=([33.8966,231.202,265.097],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([133.43,368.04,558.237,679.083,750.844,766.345,1219.1,1698.83,3225.49],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 103,
    label = "ODCDC(F)F",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 O u0 p2 c0 {5,D}
4 C u0 p0 c0 {1,S} {2,S} {5,D}
5 C u0 p0 c0 {3,D} {4,D}
""",
    statmech = Conformer(E0=(-323.721,'kJ/mol'), modes=[IdealGasTranslation(mass=(77.9917,'amu')), NonlinearRotor(inertia=([46.9849,128.952,175.938],'amu*angstrom^2'), symmetry=2), HarmonicOscillator(frequencies=([205.962,243.776,382.471,461.225,682.222,822,1318.38,1476.6,2266.44],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 104,
    label = "FC(F)(F)F",
    molecule = 
"""
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 F u0 p3 c0 {5,S}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    statmech = Conformer(E0=(-946.615,'kJ/mol'), modes=[IdealGasTranslation(mass=(87.9936,'amu')), NonlinearRotor(inertia=([88.4665,88.4666,88.467],'amu*angstrom^2'), symmetry=12), HarmonicOscillator(frequencies=([429.709,429.73,625.518,625.532,625.546,914.019,1289.73,1289.74,1289.75],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 105,
    label = "Cl[C]DCBr",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {3,S}
2 Cl u0 p3 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,D} {5,S}
4 C  u1 p0 c0 {2,S} {3,D}
5 H  u0 p0 c0 {3,S}
""",
    statmech = Conformer(E0=(267.267,'kJ/mol'), modes=[IdealGasTranslation(mass=(138.895,'amu')), NonlinearRotor(inertia=([39.5414,351.16,390.701],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([108.381,362.13,481.177,595.996,723.03,736.392,1170.73,1705.05,3234.21],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 106,
    label = "ClC(Cl)Br",
    molecule = 
"""
1 Br u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {4,S}
3 Cl u0 p3 c0 {4,S}
4 C  u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 H  u0 p0 c0 {4,S}
""",
    statmech = Conformer(E0=(-65.1787,'kJ/mol'), modes=[IdealGasTranslation(mass=(161.864,'amu')), NonlinearRotor(inertia=([156.485,282.794,427.66],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([210.351,216.893,326.197,592.586,705.48,743.323,1185.28,1224.6,3181.68],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 107,
    label = "ClC(Br)Br",
    molecule = 
"""
1 Br u0 p3 c0 {4,S}
2 Br u0 p3 c0 {4,S}
3 Cl u0 p3 c0 {4,S}
4 C  u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 H  u0 p0 c0 {4,S}
""",
    statmech = Conformer(E0=(-15.7508,'kJ/mol'), modes=[IdealGasTranslation(mass=(205.813,'amu')), NonlinearRotor(inertia=([205.739,415.693,609.345],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([163.175,196.746,276.41,561.362,641.456,729.183,1162.46,1204.54,3187.92],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 108,
    label = "[O]C(F)Cl",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {4,S}
2 F  u0 p3 c0 {4,S}
3 O  u1 p2 c0 {4,S}
4 C  u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 H  u0 p0 c0 {4,S}
""",
    statmech = Conformer(E0=(-234.491,'kJ/mol'), modes=[IdealGasTranslation(mass=(82.97,'amu')), NonlinearRotor(inertia=([47.4263,102.524,140.244],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([236.026,336.58,486.539,601.697,1043.41,1123.95,1198.19,1371.33,3042.18],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 109,
    label = "[O]C(Cl)Cl",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {4,S}
3 O  u1 p2 c0 {4,S}
4 C  u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 H  u0 p0 c0 {4,S}
""",
    statmech = Conformer(E0=(-44.4945,'kJ/mol'), modes=[IdealGasTranslation(mass=(98.9404,'amu')), NonlinearRotor(inertia=([70.0459,158.758,221.033],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([262.34,312.822,399.138,602.822,657.284,1015.95,1106.49,1133.98,2885.9],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 110,
    label = "F[C]DC(F)F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 F u0 p3 c0 {5,S}
4 C u0 p0 c0 {1,S} {2,S} {5,D}
5 C u1 p0 c0 {3,S} {4,D}
""",
    statmech = Conformer(E0=(-240.886,'kJ/mol'), modes=[IdealGasTranslation(mass=(80.9952,'amu')), NonlinearRotor(inertia=([44.73,134.434,179.163],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([204.684,238.859,485.685,497.762,618.309,927.207,1255.19,1318.81,1858.89],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 111,
    label = "[CH]DC(F)F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {3,S}
3 C u0 p0 c0 {1,S} {2,S} {4,D}
4 C u1 p0 c0 {3,D} {5,S}
5 H u0 p0 c0 {4,S}
""",
    statmech = Conformer(E0=(-92.0166,'kJ/mol'), modes=[IdealGasTranslation(mass=(63.0046,'amu')), NonlinearRotor(inertia=([43.4896,46.129,89.6186],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([420.994,524.562,552.014,640.304,746.121,978.508,1261.79,1779.04,3347.18],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 112,
    label = "ODCDC(F)Br",
    molecule = 
"""
1 Br u0 p3 c0 {4,S}
2 F  u0 p3 c0 {4,S}
3 O  u0 p2 c0 {5,D}
4 C  u0 p0 c0 {1,S} {2,S} {5,D}
5 C  u0 p0 c0 {3,D} {4,D}
""",
    statmech = Conformer(E0=(-129.203,'kJ/mol'), modes=[IdealGasTranslation(mass=(137.912,'amu')), NonlinearRotor(inertia=([88.6798,251.13,339.81],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([147.702,241.089,304.599,430.071,488.261,693.709,1089.85,1404.31,2243],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 113,
    label = "FC(F)(F)Br",
    molecule = 
"""
1 Br u0 p3 c0 {5,S}
2 F  u0 p3 c0 {5,S}
3 F  u0 p3 c0 {5,S}
4 F  u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    statmech = Conformer(E0=(-664.768,'kJ/mol'), modes=[IdealGasTranslation(mass=(147.914,'amu')), NonlinearRotor(inertia=([88.2065,244.61,244.611],'amu*angstrom^2'), symmetry=3), HarmonicOscillator(frequencies=([298.974,298.994,336.934,549.028,549.042,760.219,1072.79,1246.97,1246.97],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 114,
    label = "FC(F)(F)Cl",
    molecule = 
"""
1 Cl u0 p3 c0 {5,S}
2 F  u0 p3 c0 {5,S}
3 F  u0 p3 c0 {5,S}
4 F  u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    statmech = Conformer(E0=(-723.21,'kJ/mol'), modes=[IdealGasTranslation(mass=(103.964,'amu')), NonlinearRotor(inertia=([88.1549,153.839,153.841],'amu*angstrom^2'), symmetry=3), HarmonicOscillator(frequencies=([340.872,340.872,456.85,560.494,560.508,780.241,1086.03,1254.7,1254.71],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 115,
    label = "ODCDC(F)Cl",
    molecule = 
"""
1 Cl u0 p3 c0 {4,S}
2 F  u0 p3 c0 {4,S}
3 O  u0 p2 c0 {5,D}
4 C  u0 p0 c0 {1,S} {2,S} {5,D}
5 C  u0 p0 c0 {3,D} {4,D}
""",
    statmech = Conformer(E0=(-176.22,'kJ/mol'), modes=[IdealGasTranslation(mass=(93.9622,'amu')), NonlinearRotor(inertia=([76.9608,168.516,245.477],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([170.606,272.806,352.49,420.987,586.995,705.529,1123.02,1410.77,2248.73],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 116,
    label = "ODCDC(Br)Br",
    molecule = 
"""
1 Br u0 p3 c0 {4,S}
2 Br u0 p3 c0 {4,S}
3 O  u0 p2 c0 {5,D}
4 C  u0 p0 c0 {1,S} {2,S} {5,D}
5 C  u0 p0 c0 {3,D} {4,D}
""",
    statmech = Conformer(E0=(42.4481,'kJ/mol'), modes=[IdealGasTranslation(mass=(197.832,'amu')), NonlinearRotor(inertia=([210.78,430.091,640.872],'amu*angstrom^2'), symmetry=2), HarmonicOscillator(frequencies=([120.958,160.217,198.698,382.513,506.213,574.272,825.417,1309.34,2237.13],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 117,
    label = "ODCDC(Cl)Cl",
    molecule = 
"""
1 Cl u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {4,S}
3 O  u0 p2 c0 {5,D}
4 C  u0 p0 c0 {1,S} {2,S} {5,D}
5 C  u0 p0 c0 {3,D} {4,D}
""",
    statmech = Conformer(E0=(-41.6322,'kJ/mol'), modes=[IdealGasTranslation(mass=(109.933,'amu')), NonlinearRotor(inertia=([157.94,170.586,328.524],'amu*angstrom^2'), symmetry=2), HarmonicOscillator(frequencies=([150.251,239.623,252.575,488.08,524.214,623.351,913.686,1325.04,2244.44],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 118,
    label = "[O]C(F)(F)F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 O u1 p2 c0 {5,S}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    statmech = Conformer(E0=(-649.398,'kJ/mol'), modes=[IdealGasTranslation(mass=(84.9901,'amu')), NonlinearRotor(inertia=([83.2476,86.3025,90.6062],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([268.861,397.819,573.092,594.815,616.809,900.817,1178.75,1236.18,1267.81],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 119,
    label = "FC(F)(Cl)Cl",
    molecule = 
"""
1 Cl u0 p3 c0 {5,S}
2 Cl u0 p3 c0 {5,S}
3 F  u0 p3 c0 {5,S}
4 F  u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    statmech = Conformer(E0=(-508.716,'kJ/mol'), modes=[IdealGasTranslation(mass=(119.935,'amu')), NonlinearRotor(inertia=([123.466,195.729,231.288],'amu*angstrom^2'), symmetry=2), HarmonicOscillator(frequencies=([253.409,316.933,426.23,429.314,444.807,666.583,858.745,1128.63,1217.77],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 120,
    label = "F[C]DC(F)Cl",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {4,S}
2 F  u0 p3 c0 {4,S}
3 F  u0 p3 c0 {5,S}
4 C  u0 p0 c0 {1,S} {2,S} {5,D}
5 C  u1 p0 c0 {3,S} {4,D}
""",
    statmech = Conformer(E0=(-76.1758,'kJ/mol'), modes=[IdealGasTranslation(mass=(96.9657,'amu')), NonlinearRotor(inertia=([91.4126,150.11,241.523],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([173.856,276.834,392.235,448.724,570.689,665.888,1109.7,1278.82,1808.86],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 121,
    label = "[CH]DC(F)Cl",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {3,S}
2 F  u0 p3 c0 {3,S}
3 C  u0 p0 c0 {1,S} {2,S} {4,D}
4 C  u1 p0 c0 {3,D} {5,S}
5 H  u0 p0 c0 {4,S}
""",
    statmech = Conformer(E0=(80.3187,'kJ/mol'), modes=[IdealGasTranslation(mass=(78.9751,'amu')), NonlinearRotor(inertia=([46.2676,95.3974,141.665],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([340.441,427.237,526.235,598.35,676.215,751.712,1119.54,1731.58,3344.37],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 122,
    label = "[CH]DC(F)Br",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {3,S}
2 F  u0 p3 c0 {3,S}
3 C  u0 p0 c0 {1,S} {2,S} {4,D}
4 C  u1 p0 c0 {3,D} {5,S}
5 H  u0 p0 c0 {4,S}
""",
    statmech = Conformer(E0=(130.098,'kJ/mol'), modes=[IdealGasTranslation(mass=(122.925,'amu')), NonlinearRotor(inertia=([46.5239,157.343,203.867],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([295.703,347.858,496.963,594.76,603.545,731.898,1098.27,1734.69,3348.82],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 123,
    label = "FC(F)(Br)Br",
    molecule = 
"""
1 Br u0 p3 c0 {5,S}
2 Br u0 p3 c0 {5,S}
3 F  u0 p3 c0 {5,S}
4 F  u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    statmech = Conformer(E0=(-397.16,'kJ/mol'), modes=[IdealGasTranslation(mass=(207.833,'amu')), NonlinearRotor(inertia=([156.293,458.531,526.93],'amu*angstrom^2'), symmetry=2), HarmonicOscillator(frequencies=([159.404,277.466,324.211,329.836,362.859,630.116,784.95,1117.83,1202.12],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 124,
    label = "F[C]DC(F)Br",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {4,S}
2 F  u0 p3 c0 {4,S}
3 F  u0 p3 c0 {5,S}
4 C  u0 p0 c0 {1,S} {2,S} {5,D}
5 C  u1 p0 c0 {3,S} {4,D}
""",
    statmech = Conformer(E0=(-26.8778,'kJ/mol'), modes=[IdealGasTranslation(mass=(140.915,'amu')), NonlinearRotor(inertia=([112.974,214.612,327.587],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([147.362,278.521,327.225,420.459,546.896,580.12,1080.8,1276.79,1806.29],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 125,
    label = "ODCDC(Cl)Br",
    molecule = 
"""
1 Br u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {4,S}
3 O  u0 p2 c0 {5,D}
4 C  u0 p0 c0 {1,S} {2,S} {5,D}
5 C  u0 p0 c0 {3,D} {4,D}
""",
    statmech = Conformer(E0=(0.986715,'kJ/mol'), modes=[IdealGasTranslation(mass=(153.882,'amu')), NonlinearRotor(inertia=([168.68,282.065,450.744],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([133.618,208.413,218.594,440.363,497.213,610.212,871.433,1317.66,2240.77],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 126,
    label = "FC(F)(Cl)Br",
    molecule = 
"""
1 Br u0 p3 c0 {5,S}
2 Cl u0 p3 c0 {5,S}
3 F  u0 p3 c0 {5,S}
4 F  u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    statmech = Conformer(E0=(-452.627,'kJ/mol'), modes=[IdealGasTranslation(mass=(163.884,'amu')), NonlinearRotor(inertia=([131.819,304.366,348.259],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([208.045,290.807,326.704,402.444,432.064,647.672,824.744,1122.78,1210.32],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 127,
    label = "[CH]DC(Br)Br",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {3,S}
2 Br u0 p3 c0 {3,S}
3 C  u0 p0 c0 {1,S} {2,S} {4,D}
4 C  u1 p0 c0 {3,D} {5,S}
5 H  u0 p0 c0 {4,S}
""",
    statmech = Conformer(E0=(335.955,'kJ/mol'), modes=[IdealGasTranslation(mass=(182.845,'amu')), NonlinearRotor(inertia=([77.0995,413.016,490.117],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([172.453,278.723,400.958,433.105,569.237,632.518,731.273,1667.26,3333.91],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 128,
    label = "[CH]DC(Cl)Cl",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {3,S}
2 Cl u0 p3 c0 {3,S}
3 C  u0 p0 c0 {1,S} {2,S} {4,D}
4 C  u1 p0 c0 {3,D} {5,S}
5 H  u0 p0 c0 {4,S}
""",
    statmech = Conformer(E0=(243.669,'kJ/mol'), modes=[IdealGasTranslation(mass=(94.9455,'amu')), NonlinearRotor(inertia=([62.8947,151.348,214.243],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([284.862,333.246,457.975,573.3,622.178,670.979,833.744,1665.78,3326],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 129,
    label = "F[C]DC(Cl)Br",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {4,S}
3 F  u0 p3 c0 {5,S}
4 C  u0 p0 c0 {1,S} {2,S} {5,D}
5 C  u1 p0 c0 {3,S} {4,D}
""",
    statmech = Conformer(E0=(125.002,'kJ/mol'), modes=[IdealGasTranslation(mass=(156.886,'amu')), NonlinearRotor(inertia=([196.769,247.507,444.274],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([144.118,221.747,256.152,402.694,443.349,543.653,862.877,1164.32,1759.53],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 130,
    label = "[O]C(F)(F)Cl",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {5,S}
2 F  u0 p3 c0 {5,S}
3 F  u0 p3 c0 {5,S}
4 O  u1 p2 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    statmech = Conformer(E0=(-450.84,'kJ/mol'), modes=[IdealGasTranslation(mass=(100.961,'amu')), NonlinearRotor(inertia=([84.7204,150.692,153.084],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([269.09,279,389.159,555.848,569.876,583.308,908.783,1221.45,1337.46],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 131,
    label = "FC(Br)(Br)Br",
    molecule = 
"""
1 Br u0 p3 c0 {5,S}
2 Br u0 p3 c0 {5,S}
3 Br u0 p3 c0 {5,S}
4 F  u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    statmech = Conformer(E0=(-146.866,'kJ/mol'), modes=[IdealGasTranslation(mass=(267.753,'amu')), NonlinearRotor(inertia=([476.296,476.314,815.561],'amu*angstrom^2'), symmetry=3), HarmonicOscillator(frequencies=([145.16,145.23,212.83,304.988,305.043,393.596,710.015,710.488,1123.99],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 132,
    label = "[CH]DC(Cl)Br",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {3,S}
2 Cl u0 p3 c0 {3,S}
3 C  u0 p0 c0 {1,S} {2,S} {4,D}
4 C  u1 p0 c0 {3,D} {5,S}
5 H  u0 p0 c0 {4,S}
""",
    statmech = Conformer(E0=(289.042,'kJ/mol'), modes=[IdealGasTranslation(mass=(138.895,'amu')), NonlinearRotor(inertia=([68.0548,244.301,312.356],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([228.074,298.869,431.508,500.401,628.581,631.609,792.374,1669.76,3332.07],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 133,
    label = "F[C]DC(Br)Br",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {4,S}
2 Br u0 p3 c0 {4,S}
3 F  u0 p3 c0 {5,S}
4 C  u0 p0 c0 {1,S} {2,S} {5,D}
5 C  u1 p0 c0 {3,S} {4,D}
""",
    statmech = Conformer(E0=(171.193,'kJ/mol'), modes=[IdealGasTranslation(mass=(200.835,'amu')), NonlinearRotor(inertia=([206.552,442.252,648.803],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([134.208,169.154,237.408,349.532,397.041,543.521,805.277,1148.66,1755.88],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 134,
    label = "FC(Cl)(Cl)Cl",
    molecule = 
"""
1 Cl u0 p3 c0 {5,S}
2 Cl u0 p3 c0 {5,S}
3 Cl u0 p3 c0 {5,S}
4 F  u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    statmech = Conformer(E0=(-305.699,'kJ/mol'), modes=[IdealGasTranslation(mass=(135.905,'amu')), NonlinearRotor(inertia=([208.679,208.681,300.04],'amu*angstrom^2'), symmetry=3), HarmonicOscillator(frequencies=([238.693,238.714,341.976,393.221,393.277,524.186,802.673,803.069,1142.09],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 135,
    label = "FC(Cl)(Cl)Br",
    molecule = 
"""
1 Br u0 p3 c0 {5,S}
2 Cl u0 p3 c0 {5,S}
3 Cl u0 p3 c0 {5,S}
4 F  u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    statmech = Conformer(E0=(-252.299,'kJ/mol'), modes=[IdealGasTranslation(mass=(179.854,'amu')), NonlinearRotor(inertia=([210.39,343.929,432.995],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([197.399,211.309,296.043,331.552,387.798,493.393,755.143,795.659,1135.81],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 136,
    label = "FC(Cl)(Br)Br",
    molecule = 
"""
1 Br u0 p3 c0 {5,S}
2 Br u0 p3 c0 {5,S}
3 Cl u0 p3 c0 {5,S}
4 F  u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    statmech = Conformer(E0=(-199.501,'kJ/mol'), modes=[IdealGasTranslation(mass=(223.804,'amu')), NonlinearRotor(inertia=([267.955,472.145,612.997],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([156.48,191.204,260.631,306.314,339.087,457.891,719.703,771.81,1129.74],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 137,
    label = "F[C]DC(Cl)Cl",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {4,S}
3 F  u0 p3 c0 {5,S}
4 C  u0 p0 c0 {1,S} {2,S} {5,D}
5 C  u1 p0 c0 {3,S} {4,D}
""",
    statmech = Conformer(E0=(153.969,'kJ/mol'), modes=[IdealGasTranslation(mass=(112.936,'amu')), NonlinearRotor(inertia=([119.067,201.117,320.184],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([209.865,222.879,293.036,460.023,637.081,728.315,961.612,1136.77,1221.75],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 138,
    label = "BrC(Br)(Br)Br",
    molecule = 
"""
1 Br u0 p3 c0 {5,S}
2 Br u0 p3 c0 {5,S}
3 Br u0 p3 c0 {5,S}
4 Br u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    statmech = Conformer(E0=(82.6914,'kJ/mol'), modes=[IdealGasTranslation(mass=(327.673,'amu')), NonlinearRotor(inertia=([803.081,803.107,803.132],'amu*angstrom^2'), symmetry=12), HarmonicOscillator(frequencies=([123.298,123.312,181.655,181.697,181.697,264.583,643.54,643.79,644.297],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 139,
    label = "Br[C]DC(Br)Br",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {4,S}
2 Br u0 p3 c0 {4,S}
3 Br u0 p3 c0 {5,S}
4 C  u0 p0 c0 {1,S} {2,S} {5,D}
5 C  u1 p0 c0 {3,S} {4,D}
""",
    statmech = Conformer(E0=(348.413,'kJ/mol'), modes=[IdealGasTranslation(mass=(260.755,'amu')), NonlinearRotor(inertia=([365.509,859.649,1225.16],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([78.3929,152.306,162.126,240.901,409.875,463.51,678.132,727.239,1694.36],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 140,
    label = "Cl[C]DC(Cl)Cl",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {4,S}
3 Cl u0 p3 c0 {5,S}
4 C  u0 p0 c0 {1,S} {2,S} {5,D}
5 C  u1 p0 c0 {3,S} {4,D}
""",
    statmech = Conformer(E0=(211.418,'kJ/mol'), modes=[IdealGasTranslation(mass=(128.907,'amu')), NonlinearRotor(inertia=([137.657,340.476,478.13],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([128.152,194.621,260.041,388.853,450.53,581.849,817.278,861.002,1709.03],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 141,
    label = "ClC(Cl)(Cl)Cl",
    molecule = 
"""
1 Cl u0 p3 c0 {5,S}
2 Cl u0 p3 c0 {5,S}
3 Cl u0 p3 c0 {5,S}
4 Cl u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    statmech = Conformer(E0=(-116.439,'kJ/mol'), modes=[IdealGasTranslation(mass=(151.875,'amu')), NonlinearRotor(inertia=([296.629,296.631,296.636],'amu*angstrom^2'), symmetry=12), HarmonicOscillator(frequencies=([214.407,214.435,311.502,311.551,311.585,453.1,754.115,754.587,754.837],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 142,
    label = "ClC(Cl)(Cl)Br",
    molecule = 
"""
1 Br u0 p3 c0 {5,S}
2 Cl u0 p3 c0 {5,S}
3 Cl u0 p3 c0 {5,S}
4 Cl u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    statmech = Conformer(E0=(-65.9671,'kJ/mol'), modes=[IdealGasTranslation(mass=(195.825,'amu')), NonlinearRotor(inertia=([296.252,444.993,444.993],'amu*angstrom^2'), symmetry=3), HarmonicOscillator(frequencies=([187.135,187.155,242.526,292.07,292.084,416.32,694.508,748.517,748.74],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 143,
    label = "ClC(Cl)(Br)Br",
    molecule = 
"""
1 Br u0 p3 c0 {5,S}
2 Br u0 p3 c0 {5,S}
3 Cl u0 p3 c0 {5,S}
4 Cl u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    statmech = Conformer(E0=(-16.074,'kJ/mol'), modes=[IdealGasTranslation(mass=(239.774,'amu')), NonlinearRotor(inertia=([375.953,550.966,631.55],'amu*angstrom^2'), symmetry=2), HarmonicOscillator(frequencies=([151.063,171.78,227.769,238.734,260.979,376.721,661.082,712.009,745.184],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 144,
    label = "Cl[C]DC(Cl)Br",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {4,S}
3 Cl u0 p3 c0 {5,S}
4 C  u0 p0 c0 {1,S} {2,S} {5,D}
5 C  u1 p0 c0 {3,S} {4,D}
""",
    statmech = Conformer(E0=(256.539,'kJ/mol'), modes=[IdealGasTranslation(mass=(172.856,'amu')), NonlinearRotor(inertia=([244.96,365.272,610.228],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([105.526,195.1,216.094,374.207,426.32,479.99,765.907,854.224,1711.34],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 145,
    label = "Cl[C]DC(Br)Br",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {4,S}
2 Br u0 p3 c0 {4,S}
3 Cl u0 p3 c0 {5,S}
4 C  u0 p0 c0 {1,S} {2,S} {5,D}
5 C  u1 p0 c0 {3,S} {4,D}
""",
    statmech = Conformer(E0=(302.405,'kJ/mol'), modes=[IdealGasTranslation(mass=(216.806,'amu')), NonlinearRotor(inertia=([322.477,522.469,844.946],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([97.7689,164.578,183.211,288.445,411.854,478.316,727.69,800.221,1708.43],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 146,
    label = "ClC(Br)(Br)Br",
    molecule = 
"""
1 Br u0 p3 c0 {5,S}
2 Br u0 p3 c0 {5,S}
3 Br u0 p3 c0 {5,S}
4 Cl u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    statmech = Conformer(E0=(33.5218,'kJ/mol'), modes=[IdealGasTranslation(mass=(283.724,'amu')), NonlinearRotor(inertia=([583.68,583.707,804.897],'amu*angstrom^2'), symmetry=3), HarmonicOscillator(frequencies=([138.729,138.778,207.9,213.816,213.865,326.489,652.603,652.846,725.155],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 147,
    label = "[O]C(Cl)(Cl)Cl",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {5,S}
2 Cl u0 p3 c0 {5,S}
3 Cl u0 p3 c0 {5,S}
4 O  u1 p2 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    statmech = Conformer(E0=(-55.2396,'kJ/mol'), modes=[IdealGasTranslation(mass=(132.901,'amu')), NonlinearRotor(inertia=([199.161,209.472,309.836],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([194.892,224.102,314.599,361.553,363.296,459.78,549.341,739.85,1198.59],'cm^-1'))], spin_multiplicity=2),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 148,
    label = "CDCF",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u0 p0 c0 {1,S} {2,D} {6,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    statmech = Conformer(E0=(-153.05,'kJ/mol'), modes=[IdealGasTranslation(mass=(46.0219,'amu')), NonlinearRotor(inertia=([7.59478,47.6085,55.2033],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([482.184,740.114,880.476,949.569,983.363,1189.2,1343.65,1421.6,1725.69,3171.53,3191.61,3269.97],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 149,
    label = "CDCBr",
    molecule = 
"""
1 Br u0 p3 c0 {3,S}
2 C  u0 p0 c0 {3,D} {4,S} {5,S}
3 C  u0 p0 c0 {1,S} {2,D} {6,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {3,S}
""",
    statmech = Conformer(E0=(61.0948,'kJ/mol'), modes=[IdealGasTranslation(mass=(105.942,'amu')), NonlinearRotor(inertia=([9.1655,123.13,132.295],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([344.358,600.385,601.156,931.492,980.39,1014.18,1275.59,1406.09,1667.21,3153.4,3222.17,3248.52],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 150,
    label = "CDCCl",
    molecule = 
"""
1 Cl u0 p3 c0 {3,S}
2 C  u0 p0 c0 {3,D} {4,S} {5,S}
3 C  u0 p0 c0 {1,S} {2,D} {6,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {3,S}
""",
    statmech = Conformer(E0=(10.192,'kJ/mol'), modes=[IdealGasTranslation(mass=(61.9923,'amu')), NonlinearRotor(inertia=([8.77814,84.9789,93.7571],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([395.506,636.567,707.925,925.638,981.904,1035.12,1298.14,1405.66,1673.29,3161.3,3218.03,3255.31],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 151,
    label = "FCDCBr",
    molecule = 
"""
1 Br u0 p3 c0 {4,S}
2 F  u0 p3 c0 {3,S}
3 C  u0 p0 c0 {2,S} {4,D} {5,S}
4 C  u0 p0 c0 {1,S} {3,D} {6,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {4,S}
""",
    statmech = Conformer(E0=(-121.359,'kJ/mol'), modes=[IdealGasTranslation(mass=(123.932,'amu')), NonlinearRotor(inertia=([33.1123,205.723,238.835],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([167.495,433.765,564.911,752.99,754.622,893.372,1075.21,1253.5,1345.68,1719.95,3188.87,3251.92],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 152,
    label = "FCDCCl",
    molecule = 
"""
1 Cl u0 p3 c0 {4,S}
2 F  u0 p3 c0 {3,S}
3 C  u0 p0 c0 {2,S} {4,D} {5,S}
4 C  u0 p0 c0 {1,S} {3,D} {6,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {4,S}
""",
    statmech = Conformer(E0=(-169.728,'kJ/mol'), modes=[IdealGasTranslation(mass=(79.9829,'amu')), NonlinearRotor(inertia=([30.4867,136.826,167.313],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([196.288,458.982,658.541,760.726,809.333,892.914,1090.49,1267.59,1358.95,1728.22,3196.18,3245.73],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 153,
    label = "BrCDCBr",
    molecule = 
"""
1 Br u0 p3 c0 {3,S}
2 Br u0 p3 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,D} {5,S}
4 C  u0 p0 c0 {2,S} {3,D} {6,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {4,S}
""",
    statmech = Conformer(E0=(84.8032,'kJ/mol'), modes=[IdealGasTranslation(mass=(183.852,'amu')), NonlinearRotor(inertia=([58.4153,509.167,567.58],'amu*angstrom^2'), symmetry=2), HarmonicOscillator(frequencies=([105.901,384.006,471.739,576.002,691.292,752.073,898.643,1176.66,1275.23,1639.32,3202.43,3224.89],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 154,
    label = "ClCDCCl",
    molecule = 
"""
1 Cl u0 p3 c0 {3,S}
2 Cl u0 p3 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,D} {5,S}
4 C  u0 p0 c0 {2,S} {3,D} {6,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {4,S}
""",
    statmech = Conformer(E0=(-14.2336,'kJ/mol'), modes=[IdealGasTranslation(mass=(95.9534,'amu')), NonlinearRotor(inertia=([43.2736,206.492,249.766],'amu*angstrom^2'), symmetry=2), HarmonicOscillator(frequencies=([165.092,419.445,573.12,710.363,716.314,848.911,901.699,1207.46,1307.92,1657.95,3207.61,3229.33],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 155,
    label = "CDC(F)F",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 C u0 p0 c0 {4,D} {5,S} {6,S}
4 C u0 p0 c0 {1,S} {2,S} {3,D}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    statmech = Conformer(E0=(-361.617,'kJ/mol'), modes=[IdealGasTranslation(mass=(64.0125,'amu')), NonlinearRotor(inertia=([45.7027,48.2614,93.9642],'amu*angstrom^2'), symmetry=2), HarmonicOscillator(frequencies=([437.293,557.015,653.832,726.079,816.319,956,966.438,1345.56,1413.22,1792.31,3202.97,3303.55],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 156,
    label = "ClCDCBr",
    molecule = 
"""
1 Br u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {3,S}
3 C  u0 p0 c0 {2,S} {4,D} {5,S}
4 C  u0 p0 c0 {1,S} {3,D} {6,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {4,S}
""",
    statmech = Conformer(E0=(35.083,'kJ/mol'), modes=[IdealGasTranslation(mass=(139.903,'amu')), NonlinearRotor(inertia=([49.3361,313.847,363.182],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([135.986,400.347,511.005,644.227,704.571,812.798,900.102,1191.27,1293.02,1648.81,3202.61,3229.38],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 157,
    label = "FCDC(F)F",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 C u0 p0 c0 {1,S} {5,D} {6,S}
5 C u0 p0 c0 {2,S} {3,S} {4,D}
6 H u0 p0 c0 {4,S}
""",
    statmech = Conformer(E0=(-511.455,'kJ/mol'), modes=[IdealGasTranslation(mass=(82.003,'amu')), NonlinearRotor(inertia=([47.283,130.848,178.131],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([226.38,309.801,488.171,585.738,628.102,776.692,950.625,1195.27,1295.73,1386.74,1841.68,3239.84],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 158,
    label = "CDC(F)Cl",
    molecule = 
"""
1 Cl u0 p3 c0 {4,S}
2 F  u0 p3 c0 {4,S}
3 C  u0 p0 c0 {4,D} {5,S} {6,S}
4 C  u0 p0 c0 {1,S} {2,S} {3,D}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
""",
    statmech = Conformer(E0=(-180.623,'kJ/mol'), modes=[IdealGasTranslation(mass=(79.9829,'amu')), NonlinearRotor(inertia=([47.3103,99.8591,147.17],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([369.762,431.772,541.799,685.625,726.12,857.176,970.48,1203.96,1409.94,1729.39,3188.39,3293.76],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 159,
    label = "CDC(F)Br",
    molecule = 
"""
1 Br u0 p3 c0 {4,S}
2 F  u0 p3 c0 {4,S}
3 C  u0 p0 c0 {4,D} {5,S} {6,S}
4 C  u0 p0 c0 {1,S} {2,S} {3,D}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
""",
    statmech = Conformer(E0=(-126.329,'kJ/mol'), modes=[IdealGasTranslation(mass=(123.932,'amu')), NonlinearRotor(inertia=([47.2905,163.97,211.26],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([321.621,361.907,501.97,607.684,726.107,864.065,970.536,1188.49,1408.18,1720.53,3181.25,3291.01],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 160,
    label = "CDC(Br)Br",
    molecule = 
"""
1 Br u0 p3 c0 {4,S}
2 Br u0 p3 c0 {4,S}
3 C  u0 p0 c0 {4,D} {5,S} {6,S}
4 C  u0 p0 c0 {1,S} {2,S} {3,D}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
""",
    statmech = Conformer(E0=(88.8314,'kJ/mol'), modes=[IdealGasTranslation(mass=(183.852,'amu')), NonlinearRotor(inertia=([83.5658,406.181,489.746],'amu*angstrom^2'), symmetry=2), HarmonicOscillator(frequencies=([181.877,323.454,419.667,464.836,682.306,684.66,916.075,1071.89,1404.03,1659.63,3167.53,3261.49],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 161,
    label = "CDC(Cl)Cl",
    molecule = 
"""
1 Cl u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {4,S}
3 C  u0 p0 c0 {4,D} {5,S} {6,S}
4 C  u0 p0 c0 {1,S} {2,S} {3,D}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
""",
    statmech = Conformer(E0=(-12.2,'kJ/mol'), modes=[IdealGasTranslation(mass=(95.9534,'amu')), NonlinearRotor(inertia=([68.1039,150.516,218.62],'amu*angstrom^2'), symmetry=2), HarmonicOscillator(frequencies=([296.689,374.658,474.038,599.885,697.925,773.158,901.546,1092.57,1404.74,1672.62,3178.63,3275.4],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 162,
    label = "FC(F)DCCl",
    molecule = 
"""
1 Cl u0 p3 c0 {5,S}
2 F  u0 p3 c0 {4,S}
3 F  u0 p3 c0 {4,S}
4 C  u0 p0 c0 {2,S} {3,S} {5,D}
5 C  u0 p0 c0 {1,S} {4,D} {6,S}
6 H  u0 p0 c0 {5,S}
""",
    statmech = Conformer(E0=(-366.099,'kJ/mol'), modes=[IdealGasTranslation(mass=(97.9735,'amu')), NonlinearRotor(inertia=([46.9365,221.906,268.841],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([195.191,237.339,434.008,585.037,623.837,767.956,843.675,995.78,1218.59,1372.24,1794.83,3255.85],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 163,
    label = "FCDC(F)Br",
    molecule = 
"""
1 Br u0 p3 c0 {5,S}
2 F  u0 p3 c0 {4,S}
3 F  u0 p3 c0 {5,S}
4 C  u0 p0 c0 {2,S} {5,D} {6,S}
5 C  u0 p0 c0 {1,S} {3,S} {4,D}
6 H  u0 p0 c0 {4,S}
""",
    statmech = Conformer(E0=(-287.83,'kJ/mol'), modes=[IdealGasTranslation(mass=(141.923,'amu')), NonlinearRotor(inertia=([115.094,209.143,324.237],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([164.89,320.336,333.142,456.822,566.73,597.058,819.792,1172.66,1230.92,1305.38,1763.89,3209.47],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 164,
    label = "CDC(Cl)Br",
    molecule = 
"""
1 Br u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {4,S}
3 C  u0 p0 c0 {4,D} {5,S} {6,S}
4 C  u0 p0 c0 {1,S} {2,S} {3,D}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
""",
    statmech = Conformer(E0=(38.6372,'kJ/mol'), modes=[IdealGasTranslation(mass=(139.903,'amu')), NonlinearRotor(inertia=([72.8461,243.39,316.235],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([239.603,341.663,445.113,527.895,691.389,742.892,908.609,1081.98,1404.48,1666.39,3172.87,3269.29],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 165,
    label = "FCDC(F)Cl",
    molecule = 
"""
1 Cl u0 p3 c0 {5,S}
2 F  u0 p3 c0 {4,S}
3 F  u0 p3 c0 {5,S}
4 C  u0 p0 c0 {2,S} {5,D} {6,S}
5 C  u0 p0 c0 {1,S} {3,S} {4,D}
6 H  u0 p0 c0 {4,S}
""",
    statmech = Conformer(E0=(-340.364,'kJ/mol'), modes=[IdealGasTranslation(mass=(97.9735,'amu')), NonlinearRotor(inertia=([95.3932,144.092,239.485],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([195.079,319.996,395.992,493.49,588.009,683.5,818.257,1183.41,1237.58,1312.02,1774.37,3217.23],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 166,
    label = "FC(F)DCBr",
    molecule = 
"""
1 Br u0 p3 c0 {5,S}
2 F  u0 p3 c0 {4,S}
3 F  u0 p3 c0 {4,S}
4 C  u0 p0 c0 {2,S} {3,S} {5,D}
5 C  u0 p0 c0 {1,S} {4,D} {6,S}
6 H  u0 p0 c0 {5,S}
""",
    statmech = Conformer(E0=(-318.982,'kJ/mol'), modes=[IdealGasTranslation(mass=(141.923,'amu')), NonlinearRotor(inertia=([46.8773,350.753,397.629],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([167.175,211.705,370.977,575.286,629.136,757.58,769.845,982.786,1190.41,1361,1786.36,3261.36],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 167,
    label = "FC(Br)DCBr",
    molecule = 
"""
1 Br u0 p3 c0 {4,S}
2 Br u0 p3 c0 {5,S}
3 F  u0 p3 c0 {4,S}
4 C  u0 p0 c0 {1,S} {3,S} {5,D}
5 C  u0 p0 c0 {2,S} {4,D} {6,S}
6 H  u0 p0 c0 {5,S}
""",
    statmech = Conformer(E0=(-93.4274,'kJ/mol'), modes=[IdealGasTranslation(mass=(201.843,'amu')), NonlinearRotor(inertia=([59.7994,848.792,908.579],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([155.05,156.182,215.212,346.789,541.486,706.703,774.331,779.026,1087.17,1276.09,1708.55,3269.5],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 168,
    label = "FC(Cl)DCBr",
    molecule = 
"""
1 Br u0 p3 c0 {5,S}
2 Cl u0 p3 c0 {4,S}
3 F  u0 p3 c0 {4,S}
4 C  u0 p0 c0 {2,S} {3,S} {5,D}
5 C  u0 p0 c0 {1,S} {4,D} {6,S}
6 H  u0 p0 c0 {5,S}
""",
    statmech = Conformer(E0=(-145.523,'kJ/mol'), modes=[IdealGasTranslation(mass=(157.893,'amu')), NonlinearRotor(inertia=([55.1093,526.552,581.664],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([162.96,172.328,272.431,432.175,564.147,742.253,775.283,807.284,1097.19,1282.7,1718.09,3267.83],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 169,
    label = "FCDC(Cl)Cl",
    molecule = 
"""
1 Cl u0 p3 c0 {5,S}
2 Cl u0 p3 c0 {5,S}
3 F  u0 p3 c0 {4,S}
4 C  u0 p0 c0 {3,S} {5,D} {6,S}
5 C  u0 p0 c0 {1,S} {2,S} {4,D}
6 H  u0 p0 c0 {4,S}
""",
    statmech = Conformer(E0=(-183.092,'kJ/mol'), modes=[IdealGasTranslation(mass=(113.944,'amu')), NonlinearRotor(inertia=([124.556,208.774,333.33],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([199.934,267.923,279.848,462.142,464.996,661.784,850.002,947.083,1190.89,1324.34,1719.9,3221.5],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 170,
    label = "FCDC(Cl)Br",
    molecule = 
"""
1 Br u0 p3 c0 {5,S}
2 Cl u0 p3 c0 {5,S}
3 F  u0 p3 c0 {4,S}
4 C  u0 p0 c0 {3,S} {5,D} {6,S}
5 C  u0 p0 c0 {1,S} {2,S} {4,D}
6 H  u0 p0 c0 {4,S}
""",
    statmech = Conformer(E0=(-134.356,'kJ/mol'), modes=[IdealGasTranslation(mass=(157.893,'amu')), NonlinearRotor(inertia=([190.524,248.412,438.937],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([170.495,230.623,268.785,431.501,455.836,563.459,852.648,923.387,1186.19,1318.66,1711.42,3213.15],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 171,
    label = "FC(Cl)DCCl",
    molecule = 
"""
1 Cl u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {5,S}
3 F  u0 p3 c0 {4,S}
4 C  u0 p0 c0 {1,S} {3,S} {5,D}
5 C  u0 p0 c0 {2,S} {4,D} {6,S}
6 H  u0 p0 c0 {5,S}
""",
    statmech = Conformer(E0=(-192.724,'kJ/mol'), modes=[IdealGasTranslation(mass=(113.944,'amu')), NonlinearRotor(inertia=([55.1999,332.988,388.186],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([188.162,195.107,324.023,442.863,563.55,788.026,820.556,838.765,1112.06,1306.63,1725.12,3262.17],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 172,
    label = "FCDC(Br)Br",
    molecule = 
"""
1 Br u0 p3 c0 {5,S}
2 Br u0 p3 c0 {5,S}
3 F  u0 p3 c0 {4,S}
4 C  u0 p0 c0 {3,S} {5,D} {6,S}
5 C  u0 p0 c0 {1,S} {2,S} {4,D}
6 H  u0 p0 c0 {4,S}
""",
    statmech = Conformer(E0=(-86.5316,'kJ/mol'), modes=[IdealGasTranslation(mass=(201.843,'amu')), NonlinearRotor(inertia=([197.016,444.876,641.89],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([161.751,180.801,245.478,358.741,425.445,563.265,858.697,870.225,1178.37,1320.95,1702.27,3213.94],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 173,
    label = "BrCDC(Br)Br",
    molecule = 
"""
1 Br u0 p3 c0 {4,S}
2 Br u0 p3 c0 {5,S}
3 Br u0 p3 c0 {5,S}
4 C  u0 p0 c0 {1,S} {5,D} {6,S}
5 C  u0 p0 c0 {2,S} {3,S} {4,D}
6 H  u0 p0 c0 {4,S}
""",
    statmech = Conformer(E0=(114.213,'kJ/mol'), modes=[IdealGasTranslation(mass=(261.763,'amu')), NonlinearRotor(inertia=([325.868,852.327,1178.2],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([109.228,166.89,167.918,237.783,427.494,506.019,699.626,802.527,819.104,1235.5,1624,3232.6],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 174,
    label = "ClCDC(Cl)Cl",
    molecule = 
"""
1 Cl u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {5,S}
3 Cl u0 p3 c0 {5,S}
4 C  u0 p0 c0 {1,S} {5,D} {6,S}
5 C  u0 p0 c0 {2,S} {3,S} {4,D}
6 H  u0 p0 c0 {4,S}
""",
    statmech = Conformer(E0=(-31.7254,'kJ/mol'), modes=[IdealGasTranslation(mass=(129.914,'amu')), NonlinearRotor(inertia=([131.006,334.806,465.813],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([170.002,204.955,275.021,385.582,471.892,629.615,812.041,835.758,915.623,1264.57,1649.24,3236.27],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 175,
    label = "FC(F)DC(F)F",
    molecule = 
"""
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {6,S}
4 F u0 p3 c0 {6,S}
5 C u0 p0 c0 {1,S} {2,S} {6,D}
6 C u0 p0 c0 {3,S} {4,S} {5,D}
""",
    statmech = Conformer(E0=(-688.534,'kJ/mol'), modes=[IdealGasTranslation(mass=(99.9936,'amu')), NonlinearRotor(inertia=([91.6969,155.94,247.638],'amu*angstrom^2'), symmetry=4), HarmonicOscillator(frequencies=([198.559,203.927,398.069,428.925,524.86,551.48,555.021,803.576,1208.21,1359.53,1361.83,1918.98],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 176,
    label = "ClCDC(Br)Br",
    molecule = 
"""
1 Br u0 p3 c0 {5,S}
2 Br u0 p3 c0 {5,S}
3 Cl u0 p3 c0 {4,S}
4 C  u0 p0 c0 {3,S} {5,D} {6,S}
5 C  u0 p0 c0 {1,S} {2,S} {4,D}
6 H  u0 p0 c0 {4,S}
""",
    statmech = Conformer(E0=(65.8789,'kJ/mol'), modes=[IdealGasTranslation(mass=(217.813,'amu')), NonlinearRotor(inertia=([283.171,539.353,822.53],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([134.972,177.037,189.774,292.369,427.501,518.283,778.186,817.104,861.593,1262.22,1631.47,3227.74],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 177,
    label = "ClCDC(Cl)Br",
    molecule = 
"""
1 Br u0 p3 c0 {5,S}
2 Cl u0 p3 c0 {4,S}
3 Cl u0 p3 c0 {5,S}
4 C  u0 p0 c0 {2,S} {5,D} {6,S}
5 C  u0 p0 c0 {1,S} {3,S} {4,D}
6 H  u0 p0 c0 {4,S}
""",
    statmech = Conformer(E0=(17.0502,'kJ/mol'), modes=[IdealGasTranslation(mass=(173.864,'amu')), NonlinearRotor(inertia=([145.586,517.028,662.618],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([163.675,188.037,228.227,298.168,458.614,617.24,796.478,814.146,887.552,1265.4,1642.31,3238.26],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 178,
    label = "ClC(Cl)DCBr",
    molecule = 
"""
1 Br u0 p3 c0 {5,S}
2 Cl u0 p3 c0 {4,S}
3 Cl u0 p3 c0 {4,S}
4 C  u0 p0 c0 {2,S} {3,S} {5,D}
5 C  u0 p0 c0 {1,S} {4,D} {6,S}
6 H  u0 p0 c0 {5,S}
""",
    statmech = Conformer(E0=(16.5464,'kJ/mol'), modes=[IdealGasTranslation(mass=(173.864,'amu')), NonlinearRotor(inertia=([132.499,548.818,681.315],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([142.91,182.051,249.367,343.858,472.989,618.914,746.49,798.228,895.754,1238.82,1641.62,3240.95],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 179,
    label = "ClC(Br)DCBr",
    molecule = 
"""
1 Br u0 p3 c0 {4,S}
2 Br u0 p3 c0 {5,S}
3 Cl u0 p3 c0 {4,S}
4 C  u0 p0 c0 {1,S} {3,S} {5,D}
5 C  u0 p0 c0 {2,S} {4,D} {6,S}
6 H  u0 p0 c0 {5,S}
""",
    statmech = Conformer(E0=(65.0953,'kJ/mol'), modes=[IdealGasTranslation(mass=(217.813,'amu')), NonlinearRotor(inertia=([154.276,849.934,1004.21],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([140,166.411,200.253,261.173,458.239,603.704,705.786,799.374,857.655,1238.72,1634.2,3242.85],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 180,
    label = "FC(F)DC(F)Br",
    molecule = 
"""
1 Br u0 p3 c0 {6,S}
2 F  u0 p3 c0 {5,S}
3 F  u0 p3 c0 {5,S}
4 F  u0 p3 c0 {6,S}
5 C  u0 p0 c0 {2,S} {3,S} {6,D}
6 C  u0 p0 c0 {1,S} {4,S} {5,D}
""",
    statmech = Conformer(E0=(-473.215,'kJ/mol'), modes=[IdealGasTranslation(mass=(159.914,'amu')), NonlinearRotor(inertia=([117.385,355.053,472.436],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([157.314,160.786,310.058,362.803,364.192,514.498,571.328,673.062,1034.68,1233.14,1360.24,1837.2],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 181,
    label = "FC(F)DC(F)Cl",
    molecule = 
"""
1 Cl u0 p3 c0 {6,S}
2 F  u0 p3 c0 {5,S}
3 F  u0 p3 c0 {5,S}
4 F  u0 p3 c0 {6,S}
5 C  u0 p0 c0 {2,S} {3,S} {6,D}
6 C  u0 p0 c0 {1,S} {4,S} {5,D}
""",
    statmech = Conformer(E0=(-524.533,'kJ/mol'), modes=[IdealGasTranslation(mass=(115.964,'amu')), NonlinearRotor(inertia=([112.431,223.666,336.097],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([170.523,186.336,337.114,382.179,459.135,520.77,570.758,700.841,1064.96,1242.93,1365.08,1849.39],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 182,
    label = "FC(F)DC(Br)Br",
    molecule = 
"""
1 Br u0 p3 c0 {6,S}
2 Br u0 p3 c0 {6,S}
3 F  u0 p3 c0 {5,S}
4 F  u0 p3 c0 {5,S}
5 C  u0 p0 c0 {3,S} {4,S} {6,D}
6 C  u0 p0 c0 {1,S} {2,S} {5,D}
""",
    statmech = Conformer(E0=(-278.1,'kJ/mol'), modes=[IdealGasTranslation(mass=(219.833,'amu')), NonlinearRotor(inertia=([313.161,459.373,772.538],'amu*angstrom^2'), symmetry=2), HarmonicOscillator(frequencies=([140.681,151.515,167.689,285.098,324.878,402.444,599.642,622.608,878.878,1034.55,1348.28,1774.83],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 183,
    label = "FC(F)DC(Cl)Br",
    molecule = 
"""
1 Br u0 p3 c0 {6,S}
2 Cl u0 p3 c0 {6,S}
3 F  u0 p3 c0 {5,S}
4 F  u0 p3 c0 {5,S}
5 C  u0 p0 c0 {3,S} {4,S} {6,D}
6 C  u0 p0 c0 {1,S} {2,S} {5,D}
""",
    statmech = Conformer(E0=(-324.99,'kJ/mol'), modes=[IdealGasTranslation(mass=(175.884,'amu')), NonlinearRotor(inertia=([216.702,361.078,577.781],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([147.258,165.126,217.199,305.148,358.671,451.245,614.392,619.726,923.478,1047.67,1356.21,1783.95],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 184,
    label = "FC(F)DC(Cl)Cl",
    molecule = 
"""
1 Cl u0 p3 c0 {6,S}
2 Cl u0 p3 c0 {6,S}
3 F  u0 p3 c0 {5,S}
4 F  u0 p3 c0 {5,S}
5 C  u0 p0 c0 {3,S} {4,S} {6,D}
6 C  u0 p0 c0 {1,S} {2,S} {5,D}
""",
    statmech = Conformer(E0=(-372.669,'kJ/mol'), modes=[IdealGasTranslation(mass=(131.935,'amu')), NonlinearRotor(inertia=([197.599,230.015,427.613],'amu*angstrom^2'), symmetry=2), HarmonicOscillator(frequencies=([155.779,186.28,256.048,323.801,435.626,460.017,617.295,633.067,964.945,1058.39,1363.56,1793.31],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 185,
    label = "FC(Cl)DC(Cl)Br",
    molecule = 
"""
1 Br u0 p3 c0 {6,S}
2 Cl u0 p3 c0 {5,S}
3 Cl u0 p3 c0 {6,S}
4 F  u0 p3 c0 {5,S}
5 C  u0 p0 c0 {2,S} {4,S} {6,D}
6 C  u0 p0 c0 {1,S} {3,S} {5,D}
""",
    statmech = Conformer(E0=(-155.84,'kJ/mol'), modes=[IdealGasTranslation(mass=(191.854,'amu')), NonlinearRotor(inertia=([220.752,526.771,747.525],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([110.033,158.473,214.233,286.209,305.391,406.722,505.262,559.584,786.554,944.708,1201.08,1697.32],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 186,
    label = "FC(Cl)DC(Br)Br",
    molecule = 
"""
1 Br u0 p3 c0 {6,S}
2 Br u0 p3 c0 {6,S}
3 Cl u0 p3 c0 {5,S}
4 F  u0 p3 c0 {5,S}
5 C  u0 p0 c0 {3,S} {4,S} {6,D}
6 C  u0 p0 c0 {1,S} {2,S} {5,D}
""",
    statmech = Conformer(E0=(-108.055,'kJ/mol'), modes=[IdealGasTranslation(mass=(235.804,'amu')), NonlinearRotor(inertia=([397.261,540.72,937.971],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([104.957,137.875,169.661,276.118,283.591,358.907,461.607,558.785,778.186,893.532,1191.6,1685.87],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 187,
    label = "FC(Br)DC(Br)Br",
    molecule = 
"""
1 Br u0 p3 c0 {5,S}
2 Br u0 p3 c0 {6,S}
3 Br u0 p3 c0 {6,S}
4 F  u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {4,S} {6,D}
6 C  u0 p0 c0 {2,S} {3,S} {5,D}
""",
    statmech = Conformer(E0=(-56.2192,'kJ/mol'), modes=[IdealGasTranslation(mass=(279.753,'amu')), NonlinearRotor(inertia=([419.255,854.518,1273.76],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([90.7199,113.742,162.619,234.922,280.216,328.301,404.312,536.972,715.919,883.788,1174.97,1673.07],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 188,
    label = "FC(Cl)DC(Cl)Cl",
    molecule = 
"""
1 Cl u0 p3 c0 {5,S}
2 Cl u0 p3 c0 {6,S}
3 Cl u0 p3 c0 {6,S}
4 F  u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {4,S} {6,D}
6 C  u0 p0 c0 {2,S} {3,S} {5,D}
""",
    statmech = Conformer(E0=(-203.489,'kJ/mol'), modes=[IdealGasTranslation(mass=(147.905,'amu')), NonlinearRotor(inertia=([208.121,340.309,548.431],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([121.444,172.189,253.131,317.294,363.053,408.215,521.659,564.633,840.967,966.799,1208.53,1704.84],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 189,
    label = "BrC(Br)DC(Br)Br",
    molecule = 
"""
1 Br u0 p3 c0 {5,S}
2 Br u0 p3 c0 {5,S}
3 Br u0 p3 c0 {6,S}
4 Br u0 p3 c0 {6,S}
5 C  u0 p0 c0 {1,S} {2,S} {6,D}
6 C  u0 p0 c0 {3,S} {4,S} {5,D}
""",
    statmech = Conformer(E0=(148.38,'kJ/mol'), modes=[IdealGasTranslation(mass=(339.673,'amu')), NonlinearRotor(inertia=([793.772,916.305,1710.08],'amu*angstrom^2'), symmetry=4), HarmonicOscillator(frequencies=([55.9334,117.145,145.153,188.725,213.233,250.193,266.916,496.116,632.671,752.302,866.301,1587.25],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 190,
    label = "ClC(Cl)DC(Cl)Cl",
    molecule = 
"""
1 Cl u0 p3 c0 {5,S}
2 Cl u0 p3 c0 {5,S}
3 Cl u0 p3 c0 {6,S}
4 Cl u0 p3 c0 {6,S}
5 C  u0 p0 c0 {1,S} {2,S} {6,D}
6 C  u0 p0 c0 {3,S} {4,S} {5,D}
""",
    statmech = Conformer(E0=(-45.3751,'kJ/mol'), modes=[IdealGasTranslation(mass=(163.875,'amu')), NonlinearRotor(inertia=([295.924,367.599,663.523],'amu*angstrom^2'), symmetry=4), HarmonicOscillator(frequencies=([98.1647,176.398,236.908,293.244,312.419,347.164,448.266,538.764,775.262,891.705,968.279,1625.2],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 191,
    label = "ClC(Br)DC(Br)Br",
    molecule = 
"""
1 Br u0 p3 c0 {5,S}
2 Br u0 p3 c0 {6,S}
3 Br u0 p3 c0 {6,S}
4 Cl u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {4,S} {6,D}
6 C  u0 p0 c0 {2,S} {3,S} {5,D}
""",
    statmech = Conformer(E0=(100.142,'kJ/mol'), modes=[IdealGasTranslation(mass=(295.724,'amu')), NonlinearRotor(inertia=([546.297,863.541,1409.82],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([67.059,123.548,164.481,221.025,235.963,260.979,329.315,507.498,664.464,795.117,899.928,1596.78],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 192,
    label = "ClC(Cl)DC(Br)Br",
    molecule = 
"""
1 Br u0 p3 c0 {6,S}
2 Br u0 p3 c0 {6,S}
3 Cl u0 p3 c0 {5,S}
4 Cl u0 p3 c0 {5,S}
5 C  u0 p0 c0 {3,S} {4,S} {6,D}
6 C  u0 p0 c0 {1,S} {2,S} {5,D}
""",
    statmech = Conformer(E0=(51.361,'kJ/mol'), modes=[IdealGasTranslation(mass=(251.774,'amu')), NonlinearRotor(inertia=([544.378,546.61,1090.99],'amu*angstrom^2'), symmetry=2), HarmonicOscillator(frequencies=([78.6498,142.056,171.196,246.082,269.236,285.897,374.047,520.415,715.925,810.937,933.346,1606.58],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

entry(
    index = 193,
    label = "ClC(Cl)DC(Cl)Br",
    molecule = 
"""
1 Br u0 p3 c0 {6,S}
2 Cl u0 p3 c0 {5,S}
3 Cl u0 p3 c0 {5,S}
4 Cl u0 p3 c0 {6,S}
5 C  u0 p0 c0 {2,S} {3,S} {6,D}
6 C  u0 p0 c0 {1,S} {4,S} {5,D}
""",
    statmech = Conformer(E0=(3.23145,'kJ/mol'), modes=[IdealGasTranslation(mass=(207.825,'amu')), NonlinearRotor(inertia=([324.063,545.365,869.424],'amu*angstrom^2'), symmetry=1), HarmonicOscillator(frequencies=([87.692,154.043,216.851,267.125,282.063,316.509,415.417,528.548,737.885,864.898,949.118,1616.44],'cm^-1'))]),
    shortDesc = """B3LYP/GTBas3""",
    longDesc = 
"""

""",
)

