#!/usr/bin/env python
# encoding: utf-8

name = "LithiumPrimaryThermo"
shortDesc = ""
longDesc = """
Levels of theory used:

Conformers:       wb97x-d3/def2-tzvp, software: qchem (dft)
TS guesses:       wb97x-d3/def2-tzvp
Optimization:     wb97x-d3/def2-tzvp, software: qchem (dft) (using a fine grid)
Frequencies:      wb97x-d3/def2-tzvp, software: qchem (dft)
Single point:     ccsd(t)-f12/cc-pvdz-f12, software: molpro (wavefunction)
Rotor scans:      b3lyp/6-311++g(d,p), software: gaussian (dft)
Using p-type bond additivity corrections for thermo

Note that experimental data wasn't available to define BAC for Li-N or Li-C bonds
"""
entry(
    index = 0,
    label = "[Li]",
    molecule =
"""
multiplicity 2
1 Li u1 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,1.99051e-15,-1.1909e-17,2.10806e-20,-1.11018e-23,18206.2,2.43319], Tmin=(10,'K'), Tmax=(794.005,'K')),
            NASAPolynomial(coeffs=[2.5,1.52667e-14,-1.58445e-17,6.63089e-21,-9.62112e-25,18206.2,2.43319], Tmin=(794.005,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (151.375,'kJ/mol'),
        Cp0 = (20.7862,'J/(mol*K)'),
        CpInf = (20.7862,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
External symmetry: 1, optical isomers: 1

Geometry:
Li      0.00000000    0.00000000    0.00000000
""",
)

entry(
    index = 1,
    label = "C[CH2]",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,S} {7,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.99459,0.000106527,3.72371e-05,-4.84586e-08,2.04315e-11,13169.6,5.69996], Tmin=(10,'K'), Tmax=(614.746,'K')),
            NASAPolynomial(coeffs=[1.04451,0.0193016,-9.59845e-06,2.33163e-09,-2.23044e-13,13532.3,18.4971], Tmin=(614.746,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (109.494,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (153.818,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 5, 'C-C': 1}
1D rotors:
pivots: [1, 2], dihedral: [3, 1, 2, 6], rotor symmetry: 6, max scan energy: 0.25 kJ/mol (set as a FreeRotor)


External symmetry: 1, optical isomers: 1

Geometry:
C      -0.69131612   -0.00212838    0.00000000
C       0.79074015   -0.01731498    0.00000000
H      -1.10233219   -0.49237476   -0.88521749
H      -1.08740975    1.02387264    0.00000000
H      -1.10233219   -0.49237476    0.88521749
H       1.34752102    0.03693598   -0.92593771
H       1.34752102    0.03693598    0.92593771
""",
)

entry(
    index = 2,
    label = "[CH3]",
    molecule =
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9921,0.000373266,9.2987e-06,-1.05121e-08,3.94588e-12,16361.2,0.199302], Tmin=(10,'K'), Tmax=(673.408,'K')),
            NASAPolynomial(coeffs=[3.18361,0.00517557,-1.39823e-06,7.77165e-11,1.45007e-14,16470.1,3.7801], Tmin=(673.408,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (136.032,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 3}

External symmetry: 6, optical isomers: 1

Geometry:
C       0.00000000    0.00000000    0.00000000
H       1.07953380    0.00000000    0.00000000
H      -0.53976690    0.93490370    0.00000000
H      -0.53976690   -0.93490370    0.00000000
""",
)

entry(
    index = 3,
    label = "[H]",
    molecule =
"""
multiplicity 2
1 H u1 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,1.99051e-15,-1.1909e-17,2.10806e-20,-1.11018e-23,25553.1,-0.461069], Tmin=(10,'K'), Tmax=(794.005,'K')),
            NASAPolynomial(coeffs=[2.5,1.52667e-14,-1.58445e-17,6.63089e-21,-9.62112e-25,25553.1,-0.461069], Tmin=(794.005,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (212.46,'kJ/mol'),
        Cp0 = (20.7862,'J/(mol*K)'),
        CpInf = (20.7862,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
External symmetry: 1, optical isomers: 1

Geometry:
H       0.00000000    0.00000000    0.00000000
""",
)

entry(
    index = 4,
    label = "[Li]O",
    molecule =
"""
1 O  u0 p2 c0 {2,S} {3,S}
2 Li u0 p0 c0 {1,S}
3 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.47737,0.00136998,1.54213e-05,-3.64007e-08,2.39732e-11,-28861.9,3.98038], Tmin=(10,'K'), Tmax=(555.936,'K')),
            NASAPolynomial(coeffs=[4.0159,0.00259657,-1.65256e-06,5.79721e-10,-7.91253e-14,-29000.6,0.989438], Tmin=(555.936,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-239.98,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (54.0441,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'H-O': 1, 'Li-O': 1}

External symmetry: 1, optical isomers: 1

Geometry:
Li      0.00000000   -0.00008010    1.26774229
O       0.00000000    0.00008029   -0.31732408
H       0.00000000   -0.00040213   -1.26461597
""",
)

entry(
    index = 5,
    label = "[Li]OCC",
    molecule =
"""
1 O  u0 p2 c0 {2,S} {4,S}
2 C  u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3 C  u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4 Li u0 p0 c0 {1,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {3,S}
8 H  u0 p0 c0 {3,S}
9 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78527,0.0240446,-7.01043e-05,2.19126e-07,-2.15094e-10,-29415.9,8.82798], Tmin=(10,'K'), Tmax=(396.387,'K')),
            NASAPolynomial(coeffs=[1.22624,0.0300511,-1.78431e-05,5.10522e-09,-5.65326e-13,-29057.4,20.7696], Tmin=(396.387,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-244.588,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (199.547,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 5, 'C-O': 1, 'C-C': 1, 'Li-O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 2, max scan energy: 0.01 kJ/mol (set as a FreeRotor)
pivots: [3, 4], dihedral: [2, 3, 4, 7], rotor symmetry: 3, max scan energy: 15.00 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
Li      2.43610695   -0.64117775   -0.00171087
O       1.00196542    0.05106032    0.00100417
C      -0.24728768    0.61468689    0.00329746
C      -1.35935388   -0.43034363    0.00018317
H      -0.39130442    1.26555266    0.88499490
H      -0.39195220    1.27140880   -0.87393420
H      -1.27757695   -1.07037351    0.88268601
H      -1.27812348   -1.06453984   -0.88657734
H      -2.34945561    0.03586853    0.00197986
""",
)

entry(
    index = 6,
    label = "[Li]N",
    molecule =
"""
1 N  u0 p1 c0 {2,S} {3,S} {4,S}
2 Li u0 p0 c0 {1,S}
3 H  u0 p0 c0 {1,S}
4 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96541,0.0021667,2.85603e-05,-6.7189e-08,4.5766e-11,3299.87,2.9137], Tmin=(10,'K'), Tmax=(522.598,'K')),
            NASAPolynomial(coeffs=[4.51009,0.00558866,-3.04998e-06,9.30272e-10,-1.17229e-13,3139.28,-0.352375], Tmin=(522.598,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (27.4262,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'H-N': 2, 'Li-N': 1}

External symmetry: 2, optical isomers: 1

Geometry:
Li     -1.40647173    0.00028944    0.00007673
N       0.33083818   -0.00003900    0.00010084
H       0.95249706    0.79904741    0.00061353
H       0.95111847   -0.80020635    0.00061242
""",
)

entry(
    index = 7,
    label = "[Li]NCC",
    molecule =
"""
1  C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C  u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  N  u0 p1 c0 {1,S} {9,S} {10,S}
4  H  u0 p0 c0 {1,S}
5  H  u0 p0 c0 {1,S}
6  H  u0 p0 c0 {2,S}
7  H  u0 p0 c0 {2,S}
8  H  u0 p0 c0 {2,S}
9  Li u0 p0 c0 {3,S}
10 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.62017,0.0399853,-0.00012608,3.01413e-07,-2.52324e-10,2425.43,8.58931], Tmin=(10,'K'), Tmax=(417.684,'K')),
            NASAPolynomial(coeffs=[2.21841,0.031708,-1.84195e-05,5.18401e-09,-5.66887e-13,2731.83,16.3943], Tmin=(417.684,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (20.1555,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (224.491,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 5, 'C-C': 1, 'C-N': 1, 'H-N': 1, 'Li-N': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 10.68 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 5 1 2 3 F
pivots: [3, 4], dihedral: [2, 3, 4, 8], rotor symmetry: 3, max scan energy: 16.23 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
Li      1.61598454   -1.46502765    0.00501984
N       1.10985091    0.21136348    0.00059992
C      -0.24817169    0.70274217   -0.00063483
C      -1.23929028   -0.45268036   -0.00034931
H       1.73535955    1.00720241   -0.00148437
H      -0.47588165    1.33467780    0.87628836
H      -0.47465311    1.33316429   -0.87892590
H      -1.09890369   -1.07791260    0.88965586
H      -1.09905264   -1.07834767   -0.88999954
H      -2.27680449   -0.11034948   -0.00015054
""",
)

entry(
    index = 8,
    label = "[Li]N[C]C",
    molecule =
"""
1  C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C  u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  N  u0 p1 c0 {1,S} {2,S} {10,S}
4  H  u0 p0 c0 {1,S}
5  H  u0 p0 c0 {1,S}
6  H  u0 p0 c0 {1,S}
7  H  u0 p0 c0 {2,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {2,S}
10 Li u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7531,0.0206167,9.65698e-06,-2.3344e-08,9.64934e-12,7375.28,7.49013], Tmin=(10,'K'), Tmax=(887.72,'K')),
            NASAPolynomial(coeffs=[3.17172,0.0296543,-1.64586e-05,4.41267e-09,-4.61058e-13,7225.62,8.80134], Tmin=(887.72,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (61.2995,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (224.491,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 6, 'C-N': 2, 'Li-N': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 5], rotor symmetry: 3, max scan energy: 17.15 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 1 2 3 F
A 1 2 4 F
D 4 1 2 3 F
pivots: [2, 4], dihedral: [1, 2, 4, 8], rotor symmetry: 3, max scan energy: 17.17 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 1 2 3 F
A 1 2 4 F
D 3 1 2 4 F


External symmetry: 2, optical isomers: 1

Geometry:
Li      0.00595529   -2.15103649   -0.00003350
N       0.00044364   -0.40021868   -0.00021125
C      -1.17270703    0.43050164    0.00016685
C       1.17066327    0.43471251    0.00012940
H      -1.23182769    1.09747743   -0.88196923
H      -1.23221574    1.09621110    0.88324336
H      -2.09100323   -0.17038852   -0.00048172
H       1.22749112    1.10175809   -0.88210327
H       1.22778000    1.10070526    0.88314208
H       2.09114464   -0.16289273   -0.00039223
""",
)

entry(
    index = 9,
    label = "[Li]N[C]CC",
    molecule =
"""
1  N  u0 p1 c0 {2,S} {4,S} {5,S}
2  C  u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3  C  u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
4  C  u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
5  Li u0 p0 c0 {1,S}
6  H  u0 p0 c0 {2,S}
7  H  u0 p0 c0 {2,S}
8  H  u0 p0 c0 {3,S}
9  H  u0 p0 c0 {3,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {4,S}
12 H  u0 p0 c0 {4,S}
13 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79908,0.0200951,0.000159469,-6.25903e-07,8.05684e-10,2608.58,9.26321], Tmin=(10,'K'), Tmax=(196.514,'K')),
            NASAPolynomial(coeffs=[2.59611,0.0445811,-2.74322e-05,8.14873e-09,-9.33782e-13,2655.86,13.1096], Tmin=(196.514,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (21.7274,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (295.164,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 8, 'C-C': 1, 'C-N': 2, 'Li-N': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 6], rotor symmetry: 3, max scan energy: 14.31 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 4 1 2 3 F
pivots: [2, 4], dihedral: [1, 2, 4, 5], rotor symmetry: 1, max scan energy: 45.07 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 1 2 3 F
A 1 2 4 F
D 3 1 2 4 F
D 4 2 3 8 F
pivots: [4, 5], dihedral: [2, 4, 5, 11], rotor symmetry: 3, max scan energy: 14.75 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
Li     -0.08851893   -2.07505994    0.00220585
N      -0.53658562   -0.37361977    0.00064595
C      -1.83656637    0.23775385    0.00001126
C       0.48370435    0.63478980   -0.00022436
C       1.87875485    0.02544579    0.00020486
H      -2.63071593   -0.51783127    0.00072262
H      -2.01368797    0.88347823    0.88159085
H      -2.01360734    0.88176424   -0.88283414
H       0.40037474    1.30558390   -0.87910232
H       0.40044794    1.30702933    0.87755879
H       2.03118028   -0.59614673   -0.89089190
H       2.03130127   -0.59462827    0.89233791
H       2.66193765    0.78599006   -0.00050190
""",
)

entry(
    index = 10,
    label = "COC",
    molecule =
"""
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3 O u0 p2 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85987,0.0112332,1.1586e-05,-1.15885e-08,1.34249e-12,-23798.2,6.38105], Tmin=(10,'K'), Tmax=(668.558,'K')),
            NASAPolynomial(coeffs=[0.316621,0.0276457,-1.44981e-05,3.71236e-09,-3.74453e-13,-23217.5,22.8486], Tmin=(668.558,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-197.883,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (199.547,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 6, 'C-O': 2}
1D rotors:
pivots: [1, 2], dihedral: [4, 1, 2, 3], rotor symmetry: 3, max scan energy: 10.20 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 7], rotor symmetry: 3, max scan energy: 10.20 kJ/mol


External symmetry: 2, optical isomers: 1

Geometry:
C       1.16421999    0.00000000    0.19402258
O       0.00000000    0.00000000   -0.58622175
C      -1.16421999    0.00000000    0.19402258
H       1.21902514   -0.89084235    0.83472299
H       2.01686369    0.00000000   -0.48399760
H       1.21902514    0.89084235    0.83472299
H      -1.21902514    0.89084235    0.83472299
H      -1.21902514   -0.89084235    0.83472299
H      -2.01686369    0.00000000   -0.48399760
""",
)

entry(
    index = 11,
    label = "COCC",
    molecule =
"""
1  O u0 p2 c0 {2,S} {4,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96808,0.00373858,0.000316513,-1.73881e-06,3.43697e-09,-28531.2,7.77547], Tmin=(10,'K'), Tmax=(126.704,'K')),
            NASAPolynomial(coeffs=[3.08256,0.0316967,-1.45052e-05,3.04543e-09,-2.33897e-13,-28508.8,10.2181], Tmin=(126.704,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-236.391,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (270.22,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 8, 'C-O': 2, 'C-C': 1}
1D rotors:
pivots: [1, 2], dihedral: [5, 1, 2, 3], rotor symmetry: 3, max scan energy: 9.90 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 27.15 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 10], rotor symmetry: 3, max scan energy: 12.32 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       1.80204096   -0.03233937   -0.00002271
O       0.50491895    0.49706200    0.00004663
C      -0.48914379   -0.49900718    0.00002234
C      -1.84577464    0.16592995   -0.00002140
H       1.98581320   -0.64919868   -0.89032450
H       1.98592422   -0.64919519    0.89025923
H       2.49990277    0.80415082   -0.00007578
H      -0.37346856   -1.14254449    0.88536305
H      -0.37342531   -1.14253406   -0.88531961
H      -1.96298236    0.79382624   -0.88422186
H      -2.63795348   -0.58477258   -0.00009613
H      -1.96307973    0.79376894    0.88420371
""",
)

entry(
    index = 12,
    label = "CNCC",
    molecule =
"""
1  N u0 p1 c0 {2,S} {4,S} {13,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79045,0.0168707,8.5662e-05,-2.40096e-07,2.16944e-10,-7355.2,9.19228], Tmin=(10,'K'), Tmax=(280.539,'K')),
            NASAPolynomial(coeffs=[2.44487,0.0360565,-1.69217e-05,3.68237e-09,-2.96792e-13,-7279.7,13.9737], Tmin=(280.539,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-61.1912,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (295.164,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 8, 'C-C': 1, 'C-N': 2, 'H-N': 1}
1D rotors:
pivots: [1, 2], dihedral: [5, 1, 2, 3], rotor symmetry: 3, max scan energy: 12.16 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 27.25 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 11], rotor symmetry: 3, max scan energy: 12.72 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       1.86488401   -0.07217844    0.00415657
N       0.53285518    0.48524391    0.11728702
C      -0.51847961   -0.50138905   -0.04704255
C      -1.89105026    0.14162431    0.02546103
H       2.04109769   -0.61901644   -0.93629738
H       2.03957819   -0.76962675    0.82731435
H       2.60741326    0.72290524    0.08403085
H       0.40978949    1.22561771   -0.56099785
H      -0.41968920   -1.06208392   -0.99321343
H      -0.41246510   -1.23712791    0.75711167
H      -2.02835790    0.86724961   -0.78099612
H      -2.67834183   -0.60805057   -0.06892967
H      -2.01841438    0.66471982    0.97436685
""",
)

entry(
    index = 13,
    label = "O",
    molecule =
"""
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.0047,-0.000238494,9.50242e-07,1.26697e-09,-1.10572e-12,-30149.8,-0.122623], Tmin=(10,'K'), Tmax=(774.853,'K')),
            NASAPolynomial(coeffs=[3.50902,0.00114225,5.57963e-07,-3.5773e-10,5.15652e-14,-30037.6,2.37054], Tmin=(774.853,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-250.678,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'H-O': 2}

External symmetry: 2, optical isomers: 1

Geometry:
O       0.00000000    0.00000000    0.11614090
H      -0.76216398    0.00000000   -0.46423089
H       0.76216398    0.00000000   -0.46423089
""",
)

entry(
    index = 14,
    label = "N",
    molecule =
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.01812,-0.00106453,7.08425e-06,-2.05488e-09,-1.64936e-12,-6852.9,0.262236], Tmin=(10,'K'), Tmax=(659.777,'K')),
            NASAPolynomial(coeffs=[2.45293,0.00557484,-1.53126e-06,1.03884e-10,1.33093e-14,-6584.34,7.63254], Tmin=(659.777,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-56.9716,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'H-N': 3}

External symmetry: 3, optical isomers: 1

Geometry:
N       0.00000000    0.00000000    0.11052231
H       0.94155962    0.00000000   -0.25802850
H      -0.47077981    0.81541455   -0.25802850
H      -0.47077981   -0.81541455   -0.25802850
""",
)

entry(
    index = 15,
    label = "CCO",
    molecule =
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 O u0 p2 c0 {1,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93625,0.00710157,3.13947e-05,-4.08337e-08,1.53208e-11,-29841.9,7.98928], Tmin=(10,'K'), Tmax=(851.298,'K')),
            NASAPolynomial(coeffs=[1.25298,0.0262341,-1.38136e-05,3.57288e-09,-3.63953e-13,-29621.4,19.1139], Tmin=(851.298,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-248.113,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (199.547,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 5, 'C-C': 1, 'H-O': 1, 'C-O': 1}
1D rotors:
pivots: [1, 2], dihedral: [4, 1, 2, 3], rotor symmetry: 3, max scan energy: 13.16 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 9], rotor symmetry: 1, max scan energy: 5.99 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       1.21775139   -0.22084250   -0.00000335
C      -0.08508058    0.54451081    0.00001130
O      -1.14692004   -0.39454163    0.00001655
H       1.28541934   -0.85628876   -0.88421796
H       2.06625173    0.46578835   -0.00007661
H       1.28550258   -0.85621402    0.88426021
H      -0.14128855    1.19019667   -0.88608912
H      -0.14127160    1.19019371    0.88611416
H      -1.97962257    0.07880874   -0.00008544
""",
)

entry(
    index = 16,
    label = "CCN",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  N u0 p1 c0 {1,S} {9,S} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95773,0.00262709,7.97953e-05,-1.46788e-07,8.92875e-11,-7668.18,8.41926], Tmin=(10,'K'), Tmax=(419.983,'K')),
            NASAPolynomial(coeffs=[1.16703,0.029205,-1.51256e-05,3.87951e-09,-3.9529e-13,-7433.76,19.4618], Tmin=(419.983,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-63.7746,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (224.491,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 5, 'C-C': 1, 'C-N': 1, 'H-N': 2}
1D rotors:
pivots: [1, 2], dihedral: [4, 1, 2, 3], rotor symmetry: 3, max scan energy: 13.72 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 9], rotor symmetry: 1, max scan energy: 9.25 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       1.23304287   -0.26412473   -0.00000937
C      -0.04339220    0.57064619    0.00001899
N      -1.28996050   -0.18383159    0.00002034
H       1.27907816   -0.90656119   -0.88337211
H       1.27929724   -0.90630383    0.88353190
H       2.12371584    0.36913976   -0.00021498
H      -0.05288181    1.22858112   -0.87327180
H      -0.05283888    1.22856275    0.87332511
H      -1.34250677   -0.78444601    0.81274130
H      -1.34267374   -0.78415611   -0.81290621
""",
)

entry(
    index = 17,
    label = "[Li][H]",
    molecule =
"""
1 Li u0 p0 c0 {2,S}
2 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.51626,-0.00091266,5.1131e-06,-5.12269e-09,1.6301e-12,15869.3,0.594612], Tmin=(10,'K'), Tmax=(1005.64,'K')),
            NASAPolynomial(coeffs=[3.0417,0.00220199,-1.36295e-06,3.83801e-10,-4.04353e-14,15902.7,2.57825], Tmin=(1005.64,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (131.949,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'H-Li': 1}

External symmetry: 1, optical isomers: 1

Geometry:
Li      0.00000000    0.00000000    0.40139205
H       0.00000000    0.00000000   -1.20440546
""",
)

entry(
    index = 18,
    label = "C=C",
    molecule =
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.1031,-0.00685264,4.9964e-05,-5.8324e-08,2.24227e-11,5124.75,3.22268], Tmin=(10,'K'), Tmax=(779.263,'K')),
            NASAPolynomial(coeffs=[0.406063,0.0181128,-9.61865e-06,2.51084e-09,-2.57756e-13,5519.12,18.97], Tmin=(779.263,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (42.6329,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C=C': 1, 'C-H': 4}

External symmetry: 4, optical isomers: 1

Geometry:
C       0.66096083    0.00000000    0.00000000
C      -0.66096083    0.00000000    0.00000000
H       1.22953353    0.92300806    0.00000000
H       1.22953353   -0.92300806    0.00000000
H      -1.22953353   -0.92300806    0.00000000
H      -1.22953353    0.92300806    0.00000000
""",
)

entry(
    index = 19,
    label = "O=C",
    molecule =
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.03214,-0.00195561,9.08023e-06,2.89393e-09,-8.02984e-12,-14462.6,3.46835], Tmin=(10,'K'), Tmax=(597.026,'K')),
            NASAPolynomial(coeffs=[1.41059,0.00952508,-4.48035e-06,9.69366e-10,-7.72992e-14,-14041.1,15.6716], Tmin=(597.026,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-120.237,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 2, 'C=O': 1}

External symmetry: 2, optical isomers: 1

Geometry:
O       0.00000000    0.00000000    0.67105177
C       0.00000000    0.00000000   -0.52477764
H       0.93959967    0.00000000   -1.10994387
H      -0.93959967    0.00000000   -1.10994387
""",
)

entry(
    index = 20,
    label = "N=C",
    molecule =
"""
1 N u0 p1 c0 {2,D} {5,S}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.08222,-0.00485103,3.06851e-05,-3.08434e-08,1.0092e-11,9115.42,4.36611], Tmin=(10,'K'), Tmax=(928.953,'K')),
            NASAPolynomial(coeffs=[0.88766,0.0136924,-6.98856e-06,1.74155e-09,-1.70373e-13,9502.35,18.4306], Tmin=(928.953,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (75.812,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'H-N': 1, 'C=N': 1, 'C-H': 2}

External symmetry: 1, optical isomers: 1

Geometry:
N       0.66408216    0.15430198    0.00000000
C      -0.58307892   -0.02891041    0.00000000
H       1.16405843   -0.73379869    0.00000000
H      -1.24295926    0.83934702    0.00000000
H      -1.06787546   -1.01048983    0.00000000
""",
)

entry(
    index = 21,
    label = "[Li]OO[Li]",
    molecule =
"""
1 O  u0 p2 c0 {2,S} {3,S}
2 O  u0 p2 c0 {1,S} {4,S}
3 Li u0 p0 c0 {1,S}
4 Li u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91551,0.00550928,5.2339e-05,-1.40411e-07,1.02423e-10,-31219.3,6.36234], Tmin=(10,'K'), Tmax=(501.967,'K')),
            NASAPolynomial(coeffs=[5.37641,0.00977885,-7.96535e-06,2.82608e-09,-3.64069e-13,-31566.5,-1.67548], Tmin=(501.967,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-259.592,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'O-O': 1, 'Li-O': 2}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[3, 4]]) broke during the scan.Bond ([[2, 4]]) broke during the scan.The rotor scan has a barrier of 179.82 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 4, optical isomers: 1

Geometry:
Li      1.54954280    0.00150729   -0.00277754
O      -0.00076494    0.76554150    0.00096114
O       0.00076494   -0.76554150    0.00096114
Li     -1.54954280   -0.00150729   -0.00277754
""",
)

entry(
    index = 22,
    label = "[Li]OO",
    molecule =
"""
1 O  u0 p2 c0 {2,S} {3,S}
2 O  u0 p2 c0 {1,S} {4,S}
3 Li u0 p0 c0 {1,S}
4 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96243,0.00211417,3.29404e-05,-6.53666e-08,3.72714e-11,-21080.7,6.65108], Tmin=(10,'K'), Tmax=(614.26,'K')),
            NASAPolynomial(coeffs=[4.30533,0.00915105,-6.87994e-06,2.41891e-09,-3.15799e-13,-21297.7,3.74038], Tmin=(614.26,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-175.291,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'H-O': 1, 'O-O': 1, 'Li-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: The rotor scan has a barrier of 67.19 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 1, optical isomers: 2

Geometry:
Li     -0.68729143   -1.21360933    0.07695216
O      -0.62771607    0.49204230   -0.00516489
O       0.73494540   -0.08631905   -0.09704373
H       1.20180686    0.39642339    0.58672375
""",
)

entry(
    index = 23,
    label = "[Li]O[O]",
    molecule =
"""
multiplicity 2
1 O  u0 p2 c0 {2,S} {3,S}
2 O  u1 p2 c0 {1,S}
3 Li u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9853,0.000791066,1.72133e-05,-3.04125e-08,1.57387e-11,-11542,5.77239], Tmin=(10,'K'), Tmax=(645.692,'K')),
            NASAPolynomial(coeffs=[3.62553,0.00676415,-5.36101e-06,1.87601e-09,-2.40063e-13,-11573.6,6.74632], Tmin=(645.692,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-95.9724,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'O-O': 1, 'Li-O': 1}

External symmetry: 2, optical isomers: 1

Geometry:
Li     -0.01445384   -1.37193012    0.00000000
O      -0.65912994    0.26394999    0.00000000
O       0.66445460    0.25009861    0.00000000
""",
)

entry(
    index = 24,
    label = "O1C[=O]OC[=O]OCC1",
    molecule =
"""
1  O u0 p2 c0 {7,S} {8,S}
2  O u0 p2 c0 {6,S} {9,S}
3  O u0 p2 c0 {8,S} {9,S}
4  O u0 p2 c0 {8,D}
5  O u0 p2 c0 {9,D}
6  C u0 p0 c0 {2,S} {7,S} {10,S} {11,S}
7  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
8  C u0 p0 c0 {1,S} {3,S} {4,D}
9  C u0 p0 c0 {2,S} {3,S} {5,D}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82764,0.0275986,4.38428e-05,-8.10423e-08,3.52995e-11,-97706.6,12.7319], Tmin=(10,'K'), Tmax=(842.475,'K')),
            NASAPolynomial(coeffs=[5.60095,0.0428552,-2.54755e-05,7.16817e-09,-7.75196e-13,-98845.6,-0.50594], Tmin=(842.475,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-812.336,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 4, 'C-C': 1, 'C-O': 6, 'C=O': 2}

External symmetry: 1, optical isomers: 2

Geometry:
O       1.13540928   -0.37181530   -0.83967070
C       1.16318551    0.66559284    0.01662103
O       2.13511270    1.26871231    0.31067300
O      -0.05810228    1.04108498    0.49465966
C      -1.25065015    0.56041830   -0.02336501
O      -2.05235395    1.28980135   -0.48907183
O      -1.45560633   -0.74430636    0.14259921
C      -0.39732412   -1.54419380    0.66051689
C       0.71117125   -1.65176249   -0.35932412
H      -0.04800234   -1.13718615    1.61178609
H      -0.82932965   -2.52647640    0.84312001
H       1.56977714   -2.17476713    0.07014547
H       0.36900589   -2.18530635   -1.24446134
""",
)

entry(
    index = 25,
    label = "[Li]O[Li]",
    molecule =
"""
1 O  u0 p2 c0 {2,S} {3,S}
2 Li u0 p0 c0 {1,S}
3 Li u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97456,0.00399234,0.00012264,-1.41479e-06,4.77304e-09,-18163.9,-4.07923], Tmin=(10,'K'), Tmax=(106.637,'K')),
            NASAPolynomial(coeffs=[4.10859,0.00600986,-4.83842e-06,1.70562e-09,-2.19405e-13,-18170.8,-4.61367], Tmin=(106.637,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-147.25,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'Li-O': 2}

External symmetry: 2, optical isomers: 1

Geometry:
Li      1.61582311    0.00000000    0.00056511
O       0.00000000    0.00000000   -0.00003394
Li     -1.61582311    0.00000000    0.00056511
""",
)

entry(
    index = 26,
    label = "[Li]OCCCCC=O",
    molecule =
"""
1  C  u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C  u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C  u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C  u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
5  C  u0 p0 c0 {3,S} {15,D} {16,S}
6  O  u0 p2 c0 {4,S} {17,S}
7  H  u0 p0 c0 {2,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {1,S}
10 H  u0 p0 c0 {1,S}
11 H  u0 p0 c0 {3,S}
12 H  u0 p0 c0 {3,S}
13 H  u0 p0 c0 {4,S}
14 H  u0 p0 c0 {4,S}
15 O  u0 p2 c0 {5,D}
16 H  u0 p0 c0 {5,S}
17 Li u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.03994,0.106278,-0.000460212,1.19493e-06,-1.06436e-09,-48530.6,13.9765], Tmin=(10,'K'), Tmax=(385.952,'K')),
            NASAPolynomial(coeffs=[0.30392,0.0664286,-4.02583e-05,1.16492e-08,-1.29788e-12,-47811.4,31.1524], Tmin=(385.952,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-403.549,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (407.409,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-C': 4, 'C-H': 9, 'Li-O': 1, 'C=O': 1, 'C-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason:
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason:
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason:
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 7], invalidation reason:
* Invalidated! pivots: [6, 7], dihedral: [5, 6, 7, 8], invalidation reason:


External symmetry: 1, optical isomers: 2

Geometry:
Li      4.75834433   -0.79157140    0.09009533
O       3.35918620   -0.02542239    0.07025424
C       2.15732670    0.62648295    0.07135906
C       0.96965551   -0.32754210   -0.05927657
C      -0.37721365    0.38316869   -0.05552555
C      -1.55926583   -0.57941431   -0.18212545
C      -2.86743591    0.15010594   -0.27148816
O      -3.80759483   -0.02093898    0.45618054
H       2.01666012    1.21502973    0.99778918
H       2.09252310    1.35954847   -0.75530345
H       1.01448821   -1.04932093    0.76385646
H       1.08606019   -0.90097906   -0.98615754
H      -0.40972020    1.10759658   -0.87770052
H      -0.48410620    0.96242463    0.86778208
H      -1.60240110   -1.27729146    0.65598546
H      -1.44907402   -1.16325957   -1.10465156
H      -2.92587742    0.90716254   -1.08538314
""",
)

entry(
    index = 27,
    label = "[Li]O[CH]O",
    molecule =
"""
multiplicity 2
1 O  u0 p2 c0 {3,S} {6,S}
2 O  u0 p2 c0 {3,S} {4,S}
3 C  u1 p0 c0 {1,S} {2,S} {5,S}
4 Li u0 p0 c0 {2,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91552,0.00528612,7.25725e-05,-1.68262e-07,1.12648e-10,-34870.6,8.9915], Tmin=(10,'K'), Tmax=(523.507,'K')),
            NASAPolynomial(coeffs=[4.71329,0.0169448,-1.17046e-05,3.8448e-09,-4.77917e-13,-35197.4,3.33537], Tmin=(523.507,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-289.956,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'Li-O': 1, 'C-O': 2, 'H-O': 1, 'C-H': 1}
1D rotors:
* Invalidated! pivots: [3, 5], dihedral: [2, 3, 5, 6], invalidation reason:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 5], invalidation reason:


External symmetry: 1, optical isomers: 2

Geometry:
Li     -0.15627486   -1.52253293   -0.02699121
O      -1.16641808   -0.05989412    0.00576175
C      -0.13587218    0.69560201    0.11486395
H      -0.05176099    1.61194132   -0.49029306
O       1.10559924   -0.12715541   -0.07297121
H       1.82117899    0.27744762    0.41613997
""",
)

entry(
    index = 28,
    label = "[Li]OCCCC=O",
    molecule =
"""
1  C  u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C  u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C  u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C  u0 p0 c0 {2,S} {12,D} {13,S}
5  O  u0 p2 c0 {3,S} {14,S}
6  H  u0 p0 c0 {1,S}
7  H  u0 p0 c0 {1,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {2,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {3,S}
12 O  u0 p2 c0 {4,D}
13 H  u0 p0 c0 {4,S}
14 Li u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61287,0.0326431,2.81273e-05,-6.33642e-08,2.97717e-11,-50717.5,11.5047], Tmin=(10,'K'), Tmax=(754.635,'K')),
            NASAPolynomial(coeffs=[2.68573,0.0495084,-2.91516e-05,8.2237e-09,-8.96747e-13,-50917.8,13.4619], Tmin=(754.635,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-421.73,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-C': 3, 'C-H': 7, 'Li-O': 1, 'C=O': 1, 'C-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason:
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason:
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason:
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 7], invalidation reason:


External symmetry: 1, optical isomers: 2

Geometry:
Li      0.31013143   -1.94511519    0.51915314
O      -1.19982743   -1.18363460    0.35610820
C      -1.43265341   -0.17039093   -0.52522926
C      -0.91710687    1.19555214   -0.02804108
C       0.49033661    1.08662451    0.59734709
C       1.44568514    0.38154458   -0.30163589
O       1.73730554   -0.79618049   -0.21193977
H      -2.50601088   -0.04136811   -0.75828613
H      -0.95116900   -0.34369432   -1.51734982
H      -1.57342027    1.58379802    0.75489743
H      -0.91939360    1.92166209   -0.84803549
H       0.41387202    0.52860222    1.53081830
H       0.88328457    2.08570752    0.80642412
H       1.90812720    0.97256335   -1.11290449
""",
)

entry(
    index = 29,
    label = "[Li]OC[=O]OCCO",
    molecule =
"""
1  O  u0 p2 c0 {5,S} {7,S}
2  O  u0 p2 c0 {6,S} {13,S}
3  O  u0 p2 c0 {7,S} {8,S}
4  O  u0 p2 c0 {7,D}
5  C  u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
6  C  u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
7  C  u0 p0 c0 {1,S} {3,S} {4,D}
8  Li u0 p0 c0 {3,S}
9  H  u0 p0 c0 {5,S}
10 H  u0 p0 c0 {5,S}
11 H  u0 p0 c0 {6,S}
12 H  u0 p0 c0 {6,S}
13 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.64266,0.0457012,-2.2757e-05,9.66023e-10,1.67356e-12,-109923,12.8059], Tmin=(10,'K'), Tmax=(1207.82,'K')),
            NASAPolynomial(coeffs=[12.0945,0.0282172,-1.40915e-05,3.38504e-09,-3.17833e-13,-112731,-32.7379], Tmin=(1207.82,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-913.94,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-C': 1, 'Li-O': 1, 'C-H': 4, 'C-O': 4, 'C=O': 1, 'H-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason:
* Invalidated! pivots: [3, 5], dihedral: [2, 3, 5, 6], invalidation reason:
* Invalidated! pivots: [5, 6], dihedral: [3, 5, 6, 7], invalidation reason:
* Invalidated! pivots: [6, 7], dihedral: [5, 6, 7, 8], invalidation reason:
* Invalidated! pivots: [7, 8], dihedral: [6, 7, 8, 13], invalidation reason:


External symmetry: 1, optical isomers: 2

Geometry:
Li      3.37011424   -0.10173104    0.30392177
O       2.06057393    1.11484387   -0.19817360
C       1.31441003    0.11795154   -0.04892781
O       1.73946091   -1.01649200    0.30057438
O       0.00739231    0.30110496   -0.28302588
C      -0.85971290   -0.81487465   -0.07282414
C      -2.25925589   -0.31822019   -0.34635748
O      -2.63866420    0.71515743    0.53328124
H      -0.59081678   -1.63099224   -0.74751346
H      -0.76252897   -1.16394897    0.95689539
H      -2.33423243    0.00671712   -1.39220212
H      -2.96457685   -1.13790483   -0.19666941
H      -1.97714506    1.40818074    0.46106899
""",
)

entry(
    index = 30,
    label = "[Li]OCC[C]O[C]=O",
    molecule =
"""
multiplicity 2
1  C  u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C  u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C  u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  O  u0 p2 c0 {1,S} {6,S}
5  O  u0 p2 c0 {2,S} {13,S}
6  C  u1 p0 c0 {4,S} {14,D}
7  H  u0 p0 c0 {1,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {2,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {3,S}
12 H  u0 p0 c0 {3,S}
13 Li u0 p0 c0 {5,S}
14 O  u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.44077,0.0527628,-3.46786e-05,1.1153e-08,-1.41117e-12,-52043,13.2803], Tmin=(10,'K'), Tmax=(2086.54,'K')),
            NASAPolynomial(coeffs=[2.04842,0.0470161,-2.44972e-05,5.96686e-09,-5.58187e-13,-49630,25.4117], Tmin=(2086.54,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-432.769,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-C': 2, 'C-H': 6, 'Li-O': 1, 'C=O': 1, 'C-O': 3}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason:
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason:
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 12], invalidation reason:
* Invalidated! pivots: [4, 6], dihedral: [3, 4, 6, 7], invalidation reason:
* Invalidated! pivots: [6, 7], dihedral: [4, 6, 7, 8], invalidation reason:


External symmetry: 1, optical isomers: 2

Geometry:
Li     -0.32895577   -1.76609864    0.99451494
O      -1.79943411   -1.15411185    0.39164388
C      -1.66914768   -0.31099445   -0.66960687
C      -0.48735519    0.65135732   -0.47876161
C      -0.70509385    1.68771497    0.59582309
O       0.63026774   -0.24036922   -0.04226372
C       1.86486691    0.16473907   -0.25861191
O       2.85845435   -0.39182331    0.04916521
H      -2.55424351    0.33421142   -0.83486080
H      -1.50578521   -0.83957067   -1.63013661
H      -0.16203871    1.10291229   -1.41850942
H      -1.08320443    1.21263244    1.50192678
H      -1.45309178    2.40334210    0.25114755
H       0.21085236    2.23708753    0.82225426
""",
)

entry(
    index = 31,
    label = "[Li]OC=CO[C]=O",
    molecule =
"""
multiplicity 2
1 C  u0 p0 c0 {2,D} {3,S} {7,S}
2 C  u0 p0 c0 {1,D} {4,S} {6,S}
3 O  u0 p2 c0 {1,S} {5,S}
4 O  u0 p2 c0 {2,S} {8,S}
5 C  u1 p0 c0 {3,S} {9,D}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {1,S}
8 Li u0 p0 c0 {4,S}
9 O  u0 p2 c0 {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.56646,0.037661,-1.70295e-05,-2.40418e-08,2.3216e-11,-38642.8,12.069], Tmin=(10,'K'), Tmax=(607.685,'K')),
            NASAPolynomial(coeffs=[6.67914,0.0276514,-1.81888e-05,5.60717e-09,-6.55777e-13,-39214.6,-2.98952], Tmin=(607.685,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-321.347,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'Li-O': 1, 'C-H': 2, 'C=C': 1, 'C=O': 1, 'C-O': 3}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason:
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason:
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 7], invalidation reason:


External symmetry: 1, optical isomers: 1

Geometry:
Li     -0.59060294   -1.71604966   -0.00136418
O      -2.07544730   -0.78593107    0.00144188
C      -1.81120890    0.47974512    0.00226715
C      -0.57201158    1.00267127    0.00145203
O       0.46928451   -0.00139778   -0.00070000
C       1.73570751    0.36233534   -0.00116534
O       2.67180376   -0.35576026   -0.00282596
H      -2.64104928    1.19485047    0.00379901
H      -0.23553734    2.02401001    0.00158746
""",
)

entry(
    index = 32,
    label = "[Li]OC[=O]OC[[CH2]]C",
    molecule =
"""
multiplicity 2
1  C  u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C  u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C  u1 p0 c0 {1,S} {11,S} {12,S}
4  C  u0 p0 c0 {5,S} {6,S} {13,D}
5  O  u0 p2 c0 {1,S} {4,S}
6  O  u0 p2 c0 {4,S} {14,S}
7  H  u0 p0 c0 {1,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {2,S}
10 H  u0 p0 c0 {2,S}
11 H  u0 p0 c0 {3,S}
12 H  u0 p0 c0 {3,S}
13 O  u0 p2 c0 {4,D}
14 Li u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.39646,0.0554263,-3.78459e-05,1.14699e-08,-9.41838e-13,-70417.2,13.4331], Tmin=(10,'K'), Tmax=(1142.33,'K')),
            NASAPolynomial(coeffs=[11.096,0.0344988,-1.8288e-05,4.67932e-09,-4.67571e-13,-72569.9,-26.4601], Tmin=(1142.33,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-585.523,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-C': 2, 'Li-O': 1, 'C-H': 6, 'C=O': 1, 'C-O': 3}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason:
* Invalidated! pivots: [3, 5], dihedral: [2, 3, 5, 6], invalidation reason:
* Invalidated! pivots: [5, 6], dihedral: [3, 5, 6, 7], invalidation reason:
* Invalidated! pivots: [6, 7], dihedral: [5, 6, 7, 8], invalidation reason:
* Invalidated! pivots: [6, 10], dihedral: [5, 6, 10, 12], invalidation reason:


External symmetry: 1, optical isomers: 2

Geometry:
Li      3.07256023   -0.52886196    0.35909759
O       2.10337692    0.76144935   -0.54538212
C       1.12967661    0.16161981   -0.02837059
O       1.27066258   -0.85027937    0.71679472
O      -0.08680130    0.64742538   -0.29780747
C      -1.22448655   -0.02665330    0.26509907
C      -2.30496357    0.97770192    0.39087947
H      -3.32310763    0.65440386    0.55843923
H      -2.06624143    2.03079715    0.42656926
C      -1.61188802   -1.21907802   -0.59996950
H      -0.93062521   -0.39937570    1.25521732
H      -1.84085520   -0.89142153   -1.61507201
H      -2.49418749   -1.70995812   -0.18511950
H      -0.79607910   -1.94108396   -0.62777905
""",
)

entry(
    index = 33,
    label = "[Li]OC[F][CH]F",
    molecule =
"""
multiplicity 2
1 F  u0 p3 c0 {4,S}
2 F  u0 p3 c0 {5,S}
3 O  u0 p2 c0 {4,S} {6,S}
4 C  u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
5 C  u1 p0 c0 {2,S} {4,S} {8,S}
6 Li u0 p0 c0 {3,S}
7 H  u0 p0 c0 {4,S}
8 H  u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49837,0.0424733,-5.66606e-05,4.2944e-08,-1.36107e-11,-71028.4,11.9497], Tmin=(10,'K'), Tmax=(738.96,'K')),
            NASAPolynomial(coeffs=[7.41565,0.021269,-1.36183e-05,4.11255e-09,-4.73431e-13,-71607.3,-5.76385], Tmin=(738.96,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-590.621,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-C': 1, 'C-F': 2, 'Li-O': 1, 'C-H': 2, 'C-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason:
* Invalidated! pivots: [3, 5], dihedral: [2, 3, 5, 7], invalidation reason:


External symmetry: 1, optical isomers: 2

Geometry:
Li     -1.23650763    1.26258612   -0.79098760
O      -0.44247398    1.16065055    0.99607463
C      -0.04786550   -0.01283931    1.00312322
F      -1.15518071   -0.25320033   -1.43696281
C       0.83667041   -0.54734044    0.04051396
H       1.07502090   -1.59713567   -0.06031662
F       1.46093059    0.25424291   -0.78475790
H      -0.39528170   -0.72351380    1.76566476
""",
)

entry(
    index = 34,
    label = "[Li]NCCCC[CH2]",
    molecule =
"""
multiplicity 2
1  N  u0 p1 c0 {4,S} {7,S} {18,S}
2  C  u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
3  C  u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
4  C  u0 p0 c0 {1,S} {2,S} {12,S} {13,S}
5  C  u0 p0 c0 {3,S} {6,S} {14,S} {15,S}
6  C  u1 p0 c0 {5,S} {16,S} {17,S}
7  Li u0 p0 c0 {1,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {2,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {3,S}
12 H  u0 p0 c0 {4,S}
13 H  u0 p0 c0 {4,S}
14 H  u0 p0 c0 {5,S}
15 H  u0 p0 c0 {5,S}
16 H  u0 p0 c0 {6,S}
17 H  u0 p0 c0 {6,S}
18 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80119,0.0551629,-2.26884e-05,1.21082e-09,8.90838e-13,18331.8,12.4252], Tmin=(10,'K'), Tmax=(1619.06,'K')),
            NASAPolynomial(coeffs=[28.5932,0.0119151,7.00512e-07,-1.55227e-09,2.57068e-13,7944.29,-126.415], Tmin=(1619.06,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (152.373,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (432.353,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-C': 4, 'Li-N': 1, 'C-H': 10, 'C-N': 1, 'H-N': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason:
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason:
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason:
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 7], invalidation reason:
* Invalidated! pivots: [6, 7], dihedral: [5, 6, 7, 8], invalidation reason:


External symmetry: 1, optical isomers: 2

Geometry:
Li     -1.46015828   -2.10820754   -0.49388770
N      -2.39825394   -0.70956327   -0.01445316
C      -1.93389234    0.62163717    0.29691563
C      -0.55488649    0.90786655   -0.29214233
C       0.53740086   -0.05331041    0.16422343
C       1.94677689    0.39856023   -0.21657539
C       3.01308881   -0.54849723    0.19151704
H       3.97417919   -0.55833291   -0.30569424
H       2.90901784   -1.13476885    1.09715837
H      -3.39164468   -0.74327212    0.17628642
H      -2.60963565    1.40441312   -0.08454692
H      -1.86020307    0.81018571    1.38746610
H      -0.25373400    1.92435118   -0.01247946
H      -0.62126094    0.88776275   -1.38686434
H       0.47731680   -0.19315373    1.24943427
H       0.39738596   -1.05059159   -0.28035791
H       1.99817141    0.58035460   -1.29610542
H       2.12454412    1.38321035    0.24550484
""",
)

entry(
    index = 35,
    label = "[CH2]CCCCCN[Li]",
    molecule =
"""
multiplicity 2
1  N  u0 p1 c0 {6,S} {8,S} {21,S}
2  C  u0 p0 c0 {3,S} {4,S} {11,S} {12,S}
3  C  u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
4  C  u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
5  C  u0 p0 c0 {3,S} {7,S} {15,S} {16,S}
6  C  u0 p0 c0 {1,S} {4,S} {17,S} {18,S}
7  C  u1 p0 c0 {5,S} {19,S} {20,S}
8  Li u0 p0 c0 {1,S}
9  H  u0 p0 c0 {3,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {2,S}
12 H  u0 p0 c0 {2,S}
13 H  u0 p0 c0 {4,S}
14 H  u0 p0 c0 {4,S}
15 H  u0 p0 c0 {5,S}
16 H  u0 p0 c0 {5,S}
17 H  u0 p0 c0 {6,S}
18 H  u0 p0 c0 {6,S}
19 H  u0 p0 c0 {7,S}
20 H  u0 p0 c0 {7,S}
21 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.99525,0.106387,-0.000345755,8.32832e-07,-7.08193e-10,15525.5,14.4968], Tmin=(10,'K'), Tmax=(406.82,'K')),
            NASAPolynomial(coeffs=[0.0775589,0.0803222,-4.77735e-05,1.36997e-08,-1.52064e-12,16216,31.5174], Tmin=(406.82,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (129.055,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (507.183,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-C': 5, 'C-H': 12, 'H-N': 1, 'Li-N': 1, 'C-N': 1}
1D rotors:
* Invalidated! pivots: [1, 4], dihedral: [2, 1, 4, 5], invalidation reason:
* Invalidated! pivots: [4, 5], dihedral: [1, 4, 5, 6], invalidation reason:
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 7], invalidation reason:
* Invalidated! pivots: [6, 7], dihedral: [5, 6, 7, 8], invalidation reason:
* Invalidated! pivots: [7, 8], dihedral: [6, 7, 8, 9], invalidation reason:
* Invalidated! pivots: [8, 9], dihedral: [7, 8, 9, 10], invalidation reason:


External symmetry: 1, optical isomers: 2

Geometry:
C       4.03354134    0.37678961    0.05553249
H       3.99554295    1.45135046    0.18517273
H       5.00714732   -0.09087389   -0.01478067
C       2.79518838   -0.43983177    0.08463634
C       1.51069456    0.37317509   -0.04492297
C       0.24713462   -0.47635824    0.00537923
C      -1.03828725    0.33214054   -0.11777227
C      -2.31112886   -0.51880165   -0.07976643
N      -3.54343968    0.22906605   -0.17864851
Li     -4.84578402    0.43281788    0.96566786
H       2.75611313   -1.02179579    1.01984836
H       2.83241053   -1.19878317   -0.70866454
H       1.53485099    0.93476795   -0.98520797
H       1.47823696    1.12127684    0.75553448
H       0.23150022   -1.04247106    0.94523811
H       0.28448613   -1.22496122   -0.79533969
H      -1.02627502    0.89943143   -1.05698026
H      -1.09517703    1.07647118    0.68489066
H      -2.30545210   -1.08166823    0.86650377
H      -2.21546381   -1.28964168   -0.86679117
H      -3.55521144    0.67537458   -1.08957239
""",
)

entry(
    index = 36,
    label = "[Li][O]",
    molecule =
"""
multiplicity 2
1 O  u1 p2 c0 {2,S}
2 Li u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.51957,-0.00177315,1.71094e-05,-3.07253e-08,1.74681e-11,6363.96,4.68653], Tmin=(10,'K'), Tmax=(590.163,'K')),
            NASAPolynomial(coeffs=[3.47094,0.00207918,-1.63539e-06,5.63581e-10,-7.07655e-14,6308.35,4.37578], Tmin=(590.163,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (52.9114,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'Li-O': 1}

External symmetry: 1, optical isomers: 1

Geometry:
Li      0.00000000    0.00000000    1.23250091
O       0.00000000    0.00000000   -0.46218784
""",
)

entry(
    index = 37,
    label = "[Li]C",
    molecule =
"""
1 C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 Li u0 p0 c0 {1,S}
3 H  u0 p0 c0 {1,S}
4 H  u0 p0 c0 {1,S}
5 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9801,0.00128367,3.8126e-05,-7.82619e-08,5.13076e-11,11242.2,3.06968], Tmin=(10,'K'), Tmax=(472.733,'K')),
            NASAPolynomial(coeffs=[3.24035,0.0114201,-6.33956e-06,1.79439e-09,-2.04304e-13,11268.8,5.62609], Tmin=(472.733,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (93.4689,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 3, 'C-Li': 1}

External symmetry: 3, optical isomers: 1

Geometry:
Li      1.58833477    0.00002454    0.00004695
C      -0.38565076    0.00005576   -0.00005439
H      -0.81719341    0.95893631   -0.31775122
H      -0.81711843   -0.20434197    0.98925955
H      -0.81678794   -0.75500250   -0.67132287
""",
)

entry(
    index = 38,
    label = "[Li]Cl",
    molecule =
"""
1 Cl u0 p3 c0 {2,S}
2 Li u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49072,0.000510289,7.22654e-06,-1.44343e-08,8.06337e-12,-24640.6,5.33178], Tmin=(10,'K'), Tmax=(639.248,'K')),
            NASAPolynomial(coeffs=[3.63926,0.00194116,-1.66945e-06,6.19299e-10,-8.2738e-14,-24707.9,4.30445], Tmin=(639.248,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-204.878,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'Cl-Li': 1}

External symmetry: 1, optical isomers: 1

Geometry:
Li      0.00000000    0.00000000    1.72768185
Cl      0.00000000    0.00000000   -0.30488503
""",
)

entry(
    index = 39,
    label = "C1OC1",
    molecule =
"""
1 O u0 p2 c0 {2,S} {3,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C u0 p0 c0 {1,S} {2,S} {6,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.15854,-0.0108378,8.03707e-05,-1.00439e-07,4.09306e-11,-7420.6,5.89556], Tmin=(10,'K'), Tmax=(759.844,'K')),
            NASAPolynomial(coeffs=[-0.327926,0.0250278,-1.46093e-05,4.10729e-09,-4.4602e-13,-7092.37,23.9814], Tmin=(759.844,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-61.666,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 4, 'C-O': 2, 'C-C': 1}

External symmetry: 2, optical isomers: 1

Geometry:
C       0.72915410    0.00000000    0.36771981
O      -0.00000000   -0.00000000   -0.84539961
C      -0.72915410    0.00000000    0.36771981
H       1.26479655   -0.91897563    0.58763978
H       1.26479655    0.91897563    0.58763978
H      -1.26479655   -0.91897563    0.58763978
H      -1.26479655    0.91897563    0.58763978
""",
)

entry(
    index = 40,
    label = "C1NC1",
    molecule =
"""
1 N u0 p1 c0 {2,S} {3,S} {8,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C u0 p0 c0 {1,S} {2,S} {6,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.18715,-0.0131251,9.95e-05,-1.28248e-07,5.4051e-11,14332.7,6.66098], Tmin=(10,'K'), Tmax=(734.64,'K')),
            NASAPolynomial(coeffs=[-0.876427,0.0291911,-1.70103e-05,4.80424e-09,-5.25098e-13,14678.8,26.8201], Tmin=(734.64,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (119.203,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-N': 2, 'C-H': 4, 'H-N': 1, 'C-C': 1}

External symmetry: 1, optical isomers: 1

Geometry:
C       0.02406777   -0.39449704    0.73791224
N      -0.17270445    0.84850250   -0.00000000
C       0.02406777   -0.39449704   -0.73791224
H      -0.84690064   -0.74838888    1.27634562
H       0.96897456   -0.55419653    1.24565565
H       0.67597006    1.39961780   -0.00000000
H       0.96897456   -0.55419653   -1.24565565
H      -0.84690064   -0.74838888   -1.27634562
""",
)

entry(
    index = 41,
    label = "O=C1CCCCC1",
    molecule =
"""
1  O u0 p2 c0 {7,D}
2  C u0 p0 c0 {3,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {6,S} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {7,S} {14,S} {15,S}
6  C u0 p0 c0 {4,S} {7,S} {16,S} {17,S}
7  C u0 p0 c0 {1,D} {5,S} {6,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98527,0.000434723,0.000190545,-3.27525e-07,1.83817e-10,-29809.1,11.3318], Tmin=(10,'K'), Tmax=(459.284,'K')),
            NASAPolynomial(coeffs=[-4.25748,0.0722237,-4.39185e-05,1.28114e-08,-1.43999e-12,-29051.9,44.6846], Tmin=(459.284,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-247.86,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (407.409,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C=O': 1, 'C-H': 10, 'C-C': 6}

External symmetry: 1, optical isomers: 1

Geometry:
O      -2.28085098    0.35125960   -0.00000000
C      -1.15008009   -0.06787088   -0.00000000
C      -0.38997603   -0.34933497    1.27852198
C       1.00611728    0.28192291    1.25830837
C       1.77797042   -0.10309297    0.00000000
C       1.00611728    0.28192291   -1.25830837
C      -0.38997603   -0.34933497   -1.27852198
H      -0.98755522   -0.00214665    2.12109175
H      -0.29118132   -1.43840232    1.36376147
H       1.55596239   -0.01619612    2.15366486
H       0.90640171    1.37169545    1.30209744
H       1.96013668   -1.18423214    0.00000000
H       2.75837907    0.37898239    0.00000000
H       1.55596239   -0.01619612   -2.15366486
H       0.90640171    1.37169545   -1.30209744
H      -0.98755522   -0.00214665   -2.12109175
H      -0.29118132   -1.43840232   -1.36376147
""",
)

entry(
    index = 42,
    label = "O=C1CC1",
    molecule =
"""
1 O u0 p2 c0 {4,D}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
4 C u0 p0 c0 {1,D} {2,S} {3,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.1043,-0.00973475,0.00013257,-2.32507e-07,1.32647e-10,1058.28,7.35187], Tmin=(10,'K'), Tmax=(551.361,'K')),
            NASAPolynomial(coeffs=[1.18371,0.0284933,-1.77882e-05,5.34833e-09,-6.17852e-13,1121.33,17.3544], Tmin=(551.361,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (8.78948,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C=O': 1, 'C-H': 4, 'C-C': 3}

External symmetry: 2, optical isomers: 1

Geometry:
O       0.00000000    0.00000000    1.57300069
C       0.00000000    0.00000000    0.38289087
C       0.78107690    0.00000000   -0.85521854
C      -0.78107690    0.00000000   -0.85521854
H       1.28168734    0.91347312   -1.15437963
H       1.28168734   -0.91347312   -1.15437963
H      -1.28168734   -0.91347312   -1.15437963
H      -1.28168734    0.91347312   -1.15437963
""",
)

entry(
    index = 43,
    label = "[Li]O[C]1CC1",
    molecule =
"""
multiplicity 2
1 O  u0 p2 c0 {4,S} {5,S}
2 C  u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
3 C  u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4 C  u1 p0 c0 {1,S} {2,S} {3,S}
5 Li u0 p0 c0 {1,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {2,S}
8 H  u0 p0 c0 {3,S}
9 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92541,0.00438968,0.000101274,-1.94156e-07,1.13181e-10,7597.21,10.1151], Tmin=(10,'K'), Tmax=(558.745,'K')),
            NASAPolynomial(coeffs=[2.15404,0.0337949,-2.25639e-05,7.17083e-09,-8.67718e-13,7534.1,15.2938], Tmin=(558.745,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (63.1366,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-C': 3, 'Li-O': 1, 'C-H': 4, 'C-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformersCould not read energies


External symmetry: 1, optical isomers: 2

Geometry:
Li      1.46847910   -1.21810224   -0.02153035
O       1.36468792    0.52262286    0.11312445
C       0.19356543    0.28538961   -0.39473633
C      -1.14214135    0.62701271    0.06884978
C      -0.75712079   -0.86859429    0.05373887
H      -1.89668937    0.93825984   -0.64481975
H      -1.24070484    1.07980392    1.05250887
H      -0.68160770   -1.30693013    1.05293898
H      -1.27118386   -1.49876129   -0.66471434
""",
)

entry(
    index = 44,
    label = "O=C1OCCO1",
    molecule =
"""
1  O u0 p2 c0 {4,S} {6,S}
2  O u0 p2 c0 {5,S} {6,S}
3  O u0 p2 c0 {6,D}
4  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
5  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
6  C u0 p0 c0 {1,S} {2,S} {3,D}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.99067,0.000138568,0.000103653,-1.68456e-07,8.69454e-11,-63266.7,10.3586], Tmin=(10,'K'), Tmax=(573.934,'K')),
            NASAPolynomial(coeffs=[-0.752166,0.0415367,-2.63484e-05,7.87839e-09,-8.97063e-13,-62859.7,29.4095], Tmin=(573.934,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-526.042,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C=O': 1, 'C-H': 4, 'C-O': 4, 'C-C': 1}

External symmetry: 2, optical isomers: 2

Geometry:
O       0.00000000   -0.00000000    2.02881514
C       0.00000000   -0.00000000    0.84502848
O       0.09573356    1.10346204    0.07318854
C      -0.10560004    0.75551364   -1.29156783
C       0.10560004   -0.75551364   -1.29156783
O      -0.09573356   -1.10346204    0.07318854
H       0.61369341    1.29612152   -1.90357878
H      -1.11942034    1.03788927   -1.58286866
H      -0.61369341   -1.29612152   -1.90357878
H       1.11942034   -1.03788927   -1.58286866
""",
)

entry(
    index = 45,
    label = "[Li]O[C]1CCCCC1",
    molecule =
"""
multiplicity 2
1  O  u0 p2 c0 {7,S} {8,S}
2  C  u0 p0 c0 {3,S} {4,S} {11,S} {12,S}
3  C  u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
4  C  u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
5  C  u0 p0 c0 {3,S} {7,S} {15,S} {16,S}
6  C  u0 p0 c0 {4,S} {7,S} {17,S} {18,S}
7  C  u1 p0 c0 {1,S} {5,S} {6,S}
8  Li u0 p0 c0 {1,S}
9  H  u0 p0 c0 {3,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {2,S}
12 H  u0 p0 c0 {2,S}
13 H  u0 p0 c0 {4,S}
14 H  u0 p0 c0 {4,S}
15 H  u0 p0 c0 {5,S}
16 H  u0 p0 c0 {5,S}
17 H  u0 p0 c0 {6,S}
18 H  u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8358,0.0301701,6.53402e-05,-1.00256e-07,3.94888e-11,-19052.6,11.8891], Tmin=(10,'K'), Tmax=(894.009,'K')),
            NASAPolynomial(coeffs=[3.17063,0.0612979,-3.41209e-05,9.13542e-09,-9.50763e-13,-20058.7,8.73168], Tmin=(894.009,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-158.343,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (432.353,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 10, 'Li-O': 1, 'C-O': 1, 'C-C': 6}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason:


External symmetry: 1, optical isomers: 1

Geometry:
Li     -3.81992791   -0.00173183    0.04499010
O      -2.21273459   -0.00030174   -0.06822527
C      -0.89600115    0.00005326   -0.16705610
C      -0.18544948   -1.27945473    0.15824427
C       1.28904316   -1.25749629   -0.24197781
C       1.98400373    0.00049241    0.27042549
C       1.28850915    1.25815752   -0.24211028
C      -0.18596580    1.27978220    0.15819538
H      -0.25678018   -1.46884748    1.24805788
H      -0.70460685   -2.11373955   -0.32394165
H       1.36505356   -1.28497941   -1.33470439
H       1.79552326   -2.15160721    0.13338842
H       1.96817680    0.00046262    1.36769823
H       3.03665722    0.00068932   -0.02736734
H       1.36435952    1.28531101   -1.33485815
H       1.79474974    2.15248830    0.13299590
H      -0.25738416    1.46913119    1.24799196
H      -0.70545376    2.11382018   -0.32404509
""",
)

entry(
    index = 46,
    label = "[Li]O[C]1OCCO1",
    molecule =
"""
multiplicity 2
1  C  u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C  u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C  u1 p0 c0 {4,S} {5,S} {6,S}
4  O  u0 p2 c0 {1,S} {3,S}
5  O  u0 p2 c0 {2,S} {3,S}
6  O  u0 p2 c0 {3,S} {11,S}
7  H  u0 p0 c0 {1,S}
8  H  u0 p0 c0 {1,S}
9  H  u0 p0 c0 {2,S}
10 H  u0 p0 c0 {2,S}
11 Li u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83714,0.0168022,7.22802e-05,-1.36044e-07,7.04728e-11,-50977.7,11.7806], Tmin=(10,'K'), Tmax=(662.482,'K')),
            NASAPolynomial(coeffs=[3.31443,0.039908,-2.52069e-05,7.51437e-09,-8.55347e-13,-51346.2,10.783], Tmin=(662.482,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-423.873,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-O': 5, 'Li-O': 1, 'C-H': 4, 'C-C': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[3, 7]]) broke during the scan.


External symmetry: 1, optical isomers: 2

Geometry:
Li      1.89232775   -1.29939317   -0.38818616
O       1.89403888    0.45070065   -0.02514785
C       0.69545969    0.38805297    0.36544262
O       0.13096585   -1.04258149    0.19605211
C      -1.24044553   -0.92279716   -0.10992455
C      -1.51322772    0.57637093    0.05760253
O      -0.27289314    1.17398969   -0.24010159
H      -1.84007347   -1.53349604    0.56895659
H      -1.42736929   -1.24618904   -1.13907539
H      -2.25976695    0.95731946   -0.63732034
H      -1.81499544    0.80822262    1.08458449
""",
)

entry(
    index = 47,
    label = "[Li]OC1OCCC1",
    molecule =
"""
1  C  u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C  u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C  u0 p0 c0 {1,S} {5,S} {6,S} {11,S}
4  C  u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
5  O  u0 p2 c0 {3,S} {4,S}
6  O  u0 p2 c0 {3,S} {14,S}
7  H  u0 p0 c0 {2,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {1,S}
10 H  u0 p0 c0 {1,S}
11 H  u0 p0 c0 {3,S}
12 H  u0 p0 c0 {4,S}
13 H  u0 p0 c0 {4,S}
14 Li u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92089,0.00504173,0.000174249,-3.46302e-07,2.18934e-10,-53845.2,11.6977], Tmin=(10,'K'), Tmax=(474.985,'K')),
            NASAPolynomial(coeffs=[-0.769808,0.0582708,-3.71992e-05,1.13215e-08,-1.31983e-12,-53554.5,29.2054], Tmin=(474.985,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-447.714,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-O': 3, 'C-C': 3, 'C-H': 7, 'Li-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 4]]) broke during the scan.Bond ([[1, 2]]) broke during the scan.Bond ([[3, 7]]) broke during the scan.Bond ([[3, 8]]) broke during the scan.Significant difference observed between consecutive conformersBond ([[6, 7]]) broke during the scan.Bond ([[4, 5]]) broke during the scan.The rotor scan has a barrier of 567.44 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 1, optical isomers: 2

Geometry:
Li      1.83335934   -1.33297142   -0.49712635
O       1.94704410    0.37056426   -0.10887290
C       0.74548984    0.39269432    0.40749116
O       0.12940109   -1.05379161    0.23260994
C      -1.23535218   -0.97203811   -0.12558370
C      -1.63494142    0.49414403    0.04422156
C      -0.34023398    1.23307384   -0.25751110
H       0.71455570    0.52085242    1.50641759
H      -1.37199009   -1.28955549   -1.16773849
H      -1.82416558   -1.64126330    0.50839113
H      -2.46271976    0.77215899   -0.60909759
H      -1.94674749    0.68095937    1.07498879
H      -0.32455007    2.25326242    0.12740471
H      -0.13257969    1.26705064   -1.33069460
""",
)

entry(
    index = 48,
    label = "[Li]OC1OCCCC1",
    molecule =
"""
1  C  u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C  u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C  u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
4  C  u0 p0 c0 {2,S} {6,S} {7,S} {14,S}
5  C  u0 p0 c0 {3,S} {6,S} {15,S} {16,S}
6  O  u0 p2 c0 {4,S} {5,S}
7  O  u0 p2 c0 {4,S} {17,S}
8  H  u0 p0 c0 {3,S}
9  H  u0 p0 c0 {3,S}
10 H  u0 p0 c0 {1,S}
11 H  u0 p0 c0 {1,S}
12 H  u0 p0 c0 {2,S}
13 H  u0 p0 c0 {2,S}
14 H  u0 p0 c0 {4,S}
15 H  u0 p0 c0 {5,S}
16 H  u0 p0 c0 {5,S}
17 Li u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91052,0.00583153,0.000220235,-4.45364e-07,2.89139e-10,-58472.5,12.1113], Tmin=(10,'K'), Tmax=(453.537,'K')),
            NASAPolynomial(coeffs=[-2.02396,0.0722102,-4.57334e-05,1.38426e-08,-1.60801e-12,-58078.6,34.4577], Tmin=(453.537,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-486.184,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (407.409,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-O': 3, 'C-C': 4, 'C-H': 9, 'Li-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 4]]) broke during the scan.Bond ([[1, 2]]) broke during the scan.Bond ([[3, 8]]) broke during the scan.Bond ([[3, 9]]) broke during the scan.Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformersBond ([[2, 3]]) broke during the scan.The rotor scan has a barrier of 507.96 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 1, optical isomers: 2

Geometry:
Li      2.22008082   -1.21899049    0.67191350
O       2.22309420    0.38532527   -0.02080708
C       0.96341410    0.32280219   -0.39049774
O       0.45218010   -1.05113271    0.08447063
C      -0.87818729   -1.34304962   -0.27368391
C      -1.83832253   -0.32074549    0.31278457
C      -1.43795485    1.08898197   -0.11229889
C       0.02769472    1.35964938    0.21797880
H       0.79940038    0.27034925   -1.48956011
H      -0.96859066   -1.35307035   -1.37020403
H      -1.10312207   -2.35114701    0.08395125
H      -1.81382490   -0.40020224    1.40456882
H      -2.85784528   -0.55342535   -0.00751903
H      -2.08204244    1.82947313    0.36810568
H      -1.59423506    1.19643104   -1.19211446
H       0.19221128    1.35361470    1.30023394
H       0.34151814    2.33896639   -0.15087677
""",
)

entry(
    index = 49,
    label = "[Li]OC1OCC1",
    molecule =
"""
1  C  u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C  u0 p0 c0 {1,S} {4,S} {5,S} {8,S}
3  C  u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
4  O  u0 p2 c0 {2,S} {3,S}
5  O  u0 p2 c0 {2,S} {11,S}
6  H  u0 p0 c0 {1,S}
7  H  u0 p0 c0 {1,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {3,S}
10 H  u0 p0 c0 {3,S}
11 Li u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93288,0.00424663,0.000136317,-2.76483e-07,1.76972e-10,-44010.6,10.5997], Tmin=(10,'K'), Tmax=(479.292,'K')),
            NASAPolynomial(coeffs=[0.712286,0.0440019,-2.84028e-05,8.68886e-09,-1.01355e-12,-43849.8,22.2256], Tmin=(479.292,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-365.942,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-O': 3, 'C-C': 2, 'C-H': 5, 'Li-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: The rotor scan has a barrier of 90.27 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 1, optical isomers: 2

Geometry:
Li      1.33947206   -1.34810026    0.60912991
O       1.66007755    0.33271675    0.13695932
C       0.51078970    0.38897307   -0.44620822
O      -0.27673456   -1.02711709   -0.25435710
C      -1.44571795   -0.28956893    0.11132748
C      -0.71437199    1.04218698    0.22836750
H       0.52111616    0.51877645   -1.54206113
H      -1.91314735   -0.67454134    1.02206914
H      -2.18615342   -0.31855856   -0.69407773
H      -0.47136367    1.32127247    1.25359441
H      -1.14600096    1.89497054   -0.29474911
""",
)

entry(
    index = 50,
    label = "O=CCCO[Li]",
    molecule =
"""
1  C  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C  u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C  u0 p0 c0 {1,S} {9,D} {10,S}
4  O  u0 p2 c0 {2,S} {11,S}
5  H  u0 p0 c0 {1,S}
6  H  u0 p0 c0 {1,S}
7  H  u0 p0 c0 {2,S}
8  H  u0 p0 c0 {2,S}
9  O  u0 p2 c0 {3,D}
10 H  u0 p0 c0 {3,S}
11 Li u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88354,0.00884873,0.000164108,-4.47642e-07,3.82949e-10,-48868.4,10.5908], Tmin=(10,'K'), Tmax=(377.297,'K')),
            NASAPolynomial(coeffs=[2.81919,0.0379195,-2.21809e-05,6.47225e-09,-7.43456e-13,-48914.7,13.0104], Tmin=(377.297,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-406.303,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (249.434,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-O': 1, 'C-C': 2, 'C-H': 5, 'Li-O': 1, 'C=O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 89.87 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 2 3 4 10 F
D 2 3 4 5 F
A 2 3 4 F
A 4 5 6 F
D 9 3 4 11 F
D 10 4 5 6 F
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 105.67 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 3 4 10 F
A 4 3 8 F
D 2 3 8 4 F
A 4 5 6 F
D 7 2 3 8 F
D 10 4 5 6 F
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformersThe rotor scan has a barrier of 88.92 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 1, optical isomers: 2

Geometry:
O       1.53966491   -0.68272833    0.02367939
C       1.21478713    0.48067618    0.20826516
C       0.02329769    1.10745723   -0.39387658
C      -1.27615201    0.44396372    0.23789408
O      -1.32916871   -0.88154911    0.02181122
Li      0.02746946   -1.85574741   -0.31907723
H       1.81323396    1.07678961    0.91993496
H      -0.01398599    0.88352649   -1.46284254
H       0.03197558    2.18790257   -0.23938276
H      -1.29062878    0.71995065    1.31224104
H      -2.10708634    1.00618934   -0.22583976
""",
)

entry(
    index = 51,
    label = "[Li]OC1OC1",
    molecule =
"""
1 C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C  u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 O  u0 p2 c0 {1,S} {2,S}
4 O  u0 p2 c0 {1,S} {8,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {2,S}
8 Li u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93489,0.00421155,9.68902e-05,-2.08348e-07,1.38624e-10,-46768.8,8.7088], Tmin=(10,'K'), Tmax=(480.494,'K')),
            NASAPolynomial(coeffs=[2.45461,0.0289076,-1.8832e-05,5.80504e-09,-6.82805e-13,-46769.3,13.279], Tmin=(480.494,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-388.872,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-O': 3, 'C-C': 1, 'C-H': 3, 'Li-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 4]]) broke during the scan.Bond ([[3, 5]]) broke during the scan.Bond ([[4, 5]]) broke during the scan.Bond ([[2, 3]]) broke during the scan.Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformersCould not read energies


External symmetry: 1, optical isomers: 1

Geometry:
Li      0.15359250   -1.71744906    0.00031728
O      -1.36066853   -0.46655705    0.00109012
C      -0.79929452    0.61903822    0.00001227
O       1.32952293   -0.44810807   -0.00088421
C       0.69381253    0.73541656   -0.00125216
H      -1.40569919    1.54408640   -0.00029379
H       0.91243172    1.39704153   -0.87411977
H       0.91413185    1.39861824    0.86995157
""",
)

entry(
    index = 52,
    label = "O=CCO[Li]",
    molecule =
"""
1 C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C  u0 p0 c0 {1,S} {6,D} {7,S}
3 O  u0 p2 c0 {1,S} {8,S}
4 H  u0 p0 c0 {1,S}
5 H  u0 p0 c0 {1,S}
6 O  u0 p2 c0 {2,D}
7 H  u0 p0 c0 {2,S}
8 Li u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92713,0.00443012,9.16376e-05,-1.86216e-07,1.14963e-10,-46853.1,8.73538], Tmin=(10,'K'), Tmax=(534.634,'K')),
            NASAPolynomial(coeffs=[2.97344,0.0274504,-1.75172e-05,5.47027e-09,-6.5863e-13,-46978.2,10.6161], Tmin=(534.634,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-389.585,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-O': 1, 'C-C': 1, 'C-H': 3, 'Li-O': 1, 'C=O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 100.45 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 2 3 4 F
A 3 4 5 F
D 2 3 4 5 F
B 4 5 F
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Significant difference observed between consecutive conformersThe rotor scan has a barrier of 101.14 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 1, optical isomers: 1

Geometry:
O       1.36115159   -0.46550916   -0.00028525
C       0.79899030    0.61969161   -0.00011921
C      -0.69424198    0.73493243    0.00017701
O      -1.32904732   -0.44907746    0.00009748
Li     -0.15215519   -1.71761081   -0.00008420
H       1.40487975    1.54507553   -0.00025474
H      -0.91441634    1.39734857   -0.87168839
H      -0.91413074    1.39706715    0.87232004
""",
)

entry(
    index = 53,
    label = "[Li]OC[=O]OC",
    molecule =
"""
1 O  u0 p2 c0 {4,S} {5,S}
2 O  u0 p2 c0 {5,S} {6,S}
3 O  u0 p2 c0 {5,D}
4 C  u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,D}
6 Li u0 p0 c0 {2,S}
7 H  u0 p0 c0 {4,S}
8 H  u0 p0 c0 {4,S}
9 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65964,0.0337109,-6.80069e-05,1.54816e-07,-1.36627e-10,-86561.4,9.89961], Tmin=(10,'K'), Tmax=(405.174,'K')),
            NASAPolynomial(coeffs=[2.52792,0.0330547,-2.17858e-05,6.71084e-09,-7.84836e-13,-86372.6,15.5352], Tmin=(405.174,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-719.72,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (199.547,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-O': 3, 'C-H': 3, 'Li-O': 1, 'C=O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 4]]) broke during the scan.Bond ([[1, 2]]) broke during the scan.The rotor scan has a barrier of 352.68 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
pivots: [3, 5], dihedral: [2, 3, 5, 6], rotor symmetry: 2, max scan energy: 39.88 kJ/mol
pivots: [5, 6], dihedral: [3, 5, 6, 7], rotor symmetry: 3, max scan energy: 3.18 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
Li      2.32284608   -0.71577753   -0.00046298
O       1.39855048    0.88819669    0.00014018
C       0.40350293    0.12322936    0.00004781
O       0.50524507   -1.13575354   -0.00017499
O      -0.80374725    0.69940844    0.00007642
C      -1.92343122   -0.17595220   -0.00002471
H      -1.92330319   -0.81024787    0.88695871
H      -1.92337357   -0.80995368   -0.88721960
H      -2.80116502    0.46706571    0.00011493
""",
)

entry(
    index = 54,
    label = "[Li][CH2]",
    molecule =
"""
multiplicity 2
1 C  u1 p0 c0 {2,S} {3,S} {4,S}
2 Li u0 p0 c0 {1,S}
3 H  u0 p0 c0 {1,S}
4 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96956,0.00188154,2.92061e-05,-6.46579e-08,4.23053e-11,33594.1,3.69086], Tmin=(10,'K'), Tmax=(529.478,'K')),
            NASAPolynomial(coeffs=[4.19856,0.00688631,-4.05182e-06,1.24028e-09,-1.52138e-13,33475.4,1.84018], Tmin=(529.478,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (279.307,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-Li': 1, 'C-H': 2}

External symmetry: 2, optical isomers: 1

Geometry:
Li     -1.51921212    0.00003924    0.00000000
C       0.40395391    0.00027743    0.00000000
H       1.06792406    0.00069435   -0.87552771
H       1.06792406    0.00069435    0.87552771
""",
)

entry(
    index = 55,
    label = "[Li][CH]C",
    molecule =
"""
multiplicity 2
1 C  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C  u1 p0 c0 {1,S} {3,S} {7,S}
3 Li u0 p0 c0 {2,S}
4 H  u0 p0 c0 {1,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {1,S}
7 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83896,0.014641,-2.77573e-06,-2.91078e-09,1.21661e-12,31835.6,7.29131], Tmin=(10,'K'), Tmax=(1260.9,'K')),
            NASAPolynomial(coeffs=[5.23763,0.0140264,-6.59201e-06,1.51126e-09,-1.3685e-13,31179,-0.9857], Tmin=(1260.9,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (264.68,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (153.818,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-C': 1, 'C-H': 4, 'C-Li': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 5], rotor symmetry: 3, max scan energy: 5.58 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
Li      2.18648505   -0.51266855    0.00922212
C       0.46186842    0.35146065   -0.00199992
C      -0.94787801   -0.18041668   -0.00053411
H       0.40368633    1.45143534   -0.01143448
H      -1.52025030    0.17321966    0.87085441
H      -1.51744725    0.16028688   -0.87886530
H      -1.00460945   -1.27373269    0.00753775
""",
)

entry(
    index = 56,
    label = "[Li]N=C",
    molecule =
"""
1 N  u0 p1 c0 {2,D} {3,S}
2 C  u0 p0 c0 {1,D} {4,S} {5,S}
3 Li u0 p0 c0 {1,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83557,0.0141172,-2.70687e-05,4.40958e-08,-2.71128e-11,17218,4.88537], Tmin=(10,'K'), Tmax=(563.802,'K')),
            NASAPolynomial(coeffs=[3.23751,0.0124767,-7.05137e-06,1.91751e-09,-2.03003e-13,17379,8.25719], Tmin=(563.802,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (143.149,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 2, 'Li-N': 1, 'C=N': 1}

External symmetry: 2, optical isomers: 1

Geometry:
Li      2.05213685   -0.00062105   -0.00039192
N       0.33517664    0.00050873    0.00034250
C      -0.90883921   -0.00026548   -0.00018643
H      -1.52550321    0.92408078   -0.00046447
H      -1.52429411   -0.92539737   -0.00046062
""",
)

entry(
    index = 57,
    label = "[Li]N=[CH]",
    molecule =
"""
multiplicity 2
1 N  u0 p1 c0 {2,D} {3,S}
2 C  u1 p0 c0 {1,D} {4,S}
3 Li u0 p0 c0 {1,S}
4 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8009,0.0167863,-3.83386e-05,5.08562e-08,-2.60193e-11,30411.9,6.454], Tmin=(10,'K'), Tmax=(581.39,'K')),
            NASAPolynomial(coeffs=[4.68385,0.00714334,-4.25369e-06,1.21555e-09,-1.34455e-13,30369.6,3.19176], Tmin=(581.39,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (252.843,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 1, 'Li-N': 1, 'C=N': 1}

External symmetry: 1, optical isomers: 2

Geometry:
Li      1.97819865    0.02676427    0.00000000
N       0.23170233    0.03149534    0.00000000
C      -0.96609189   -0.15577133    0.00000000
H      -1.75486606    0.63803122    0.00000000
""",
)

entry(
    index = 58,
    label = "[Li][S]",
    molecule =
"""
multiplicity 2
1 S  u1 p2 c0 {2,S}
2 Li u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.48776,0.000701963,8.14522e-06,-1.80281e-08,1.0915e-11,14484.2,6.02553], Tmin=(10,'K'), Tmax=(604.669,'K')),
            NASAPolynomial(coeffs=[3.78943,0.00163453,-1.43209e-06,5.39883e-10,-7.3114e-14,14394.2,4.27926], Tmin=(604.669,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (120.423,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'Li-S': 1}

External symmetry: 1, optical isomers: 1

Geometry:
Li      0.00000000    0.00000000    1.81882624
S       0.00000000    0.00000000   -0.34083611
""",
)

entry(
    index = 59,
    label = "[Li][N]C",
    molecule =
"""
multiplicity 2
1 C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 N  u1 p1 c0 {1,S} {6,S}
3 H  u0 p0 c0 {1,S}
4 H  u0 p0 c0 {1,S}
5 H  u0 p0 c0 {1,S}
6 Li u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86489,0.0155446,-5.95928e-05,1.80001e-07,-1.70998e-10,30136,5.33235], Tmin=(10,'K'), Tmax=(397.225,'K')),
            NASAPolynomial(coeffs=[2.22119,0.01726,-1.0045e-05,2.81655e-09,-3.06131e-13,30383.6,13.2181], Tmin=(397.225,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (250.557,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (128.874,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 3, 'C-N': 1, 'Li-N': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 0.02 kJ/mol (set as a FreeRotor)


External symmetry: 1, optical isomers: 1

Geometry:
Li      2.16642962    0.00442068   -0.03466853
N       0.46222864    0.00769310    0.01381063
C      -0.94027949   -0.00487560    0.02982699
H      -1.38888223   -0.55698473    0.87533430
H      -1.41328968    0.99304064   -0.00838381
H      -1.29324600   -0.52719159   -0.87771683
""",
)

entry(
    index = 60,
    label = "[Li]OC=C",
    molecule =
"""
1 O  u0 p2 c0 {2,S} {4,S}
2 C  u0 p0 c0 {1,S} {3,D} {5,S}
3 C  u0 p0 c0 {2,D} {6,S} {7,S}
4 Li u0 p0 c0 {1,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98979,0.0116021,8.90767e-06,-1.54016e-08,5.39156e-12,-19251.8,8.24293], Tmin=(10,'K'), Tmax=(1105.97,'K')),
            NASAPolynomial(coeffs=[5.79537,0.014206,-7.01248e-06,1.66253e-09,-1.53777e-13,-20209.8,-3.17535], Tmin=(1105.97,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-160.027,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (153.818,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 3, 'Li-O': 1, 'C-O': 1, 'C=C': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 2, max scan energy: 0.09 kJ/mol (set as a FreeRotor)


External symmetry: 1, optical isomers: 1

Geometry:
Li      2.41820203   -0.51253326    0.00001356
O       0.92308402    0.09742846   -0.00000753
C      -0.33646448    0.45418498   -0.00007440
C      -1.40272194   -0.35593443   -0.00002042
H      -0.51409438    1.53731982   -0.00000833
H      -1.29276427   -1.43489140    0.00000876
H      -2.40046950    0.06168265    0.00002845
""",
)

entry(
    index = 61,
    label = "[Li]N[Li]",
    molecule =
"""
1 N  u0 p1 c0 {2,S} {3,S} {4,S}
2 Li u0 p0 c0 {1,S}
3 Li u0 p0 c0 {1,S}
4 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90065,0.00703115,5.12111e-05,-1.70111e-07,1.46039e-10,20038.7,4.93326], Tmin=(10,'K'), Tmax=(443.899,'K')),
            NASAPolynomial(coeffs=[5.91773,0.00619105,-4.53073e-06,1.58352e-09,-2.07286e-13,19688.9,-5.08363], Tmin=(443.899,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (166.604,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'Li-N': 2, 'H-N': 1}

External symmetry: 2, optical isomers: 1

Geometry:
Li      1.59909821   -0.47037659   -0.00013831
N      -0.00000054    0.22511536    0.00012908
Li     -1.59909955   -0.47036976   -0.00013831
H       0.00001630    1.24653648   -0.00066453
""",
)

entry(
    index = 62,
    label = "[Li]N[[Li]][Li]",
    molecule =
"""
1 N  u0 p1 c0 {2,S} {3,S} {4,S}
2 Li u0 p0 c0 {1,S}
3 Li u0 p0 c0 {1,S}
4 Li u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81383,0.0156267,1.58498e-05,-1.09407e-07,1.10781e-10,33331.5,5.22518], Tmin=(10,'K'), Tmax=(422.639,'K')),
            NASAPolynomial(coeffs=[6.00268,0.008477,-6.92386e-06,2.46572e-09,-3.19204e-13,33025.4,-4.88304], Tmin=(422.639,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (277.13,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'Li-N': 3}

External symmetry: 6, optical isomers: 1

Geometry:
Li      1.24388269    1.20065683   -0.00020422
N       0.00046802   -0.00069642    0.00011736
Li     -1.66153404    0.47568780   -0.00020573
Li      0.41938166   -1.67812095   -0.00020233
""",
)

entry(
    index = 63,
    label = "[Li]S[Li]",
    molecule =
"""
1 S  u0 p2 c0 {2,S} {3,S}
2 Li u0 p0 c0 {1,S}
3 Li u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86856,0.0141853,-3.65516e-05,5.18374e-08,-2.9536e-11,-4035.21,7.2714], Tmin=(10,'K'), Tmax=(428.812,'K')),
            NASAPolynomial(coeffs=[4.86051,0.00493221,-4.18398e-06,1.51581e-09,-1.98111e-13,-4120.28,3.32573], Tmin=(428.812,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-33.5416,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'Li-S': 2}

External symmetry: 1, optical isomers: 1

Geometry:
Li      1.96885897    0.00000000    0.49067031
S       0.00000000    0.00000000   -0.17847632
Li     -1.96885897    0.00000000    0.49067031
""",
)

entry(
    index = 64,
    label = "[Li][N][Li]",
    molecule =
"""
multiplicity 2
1 N  u1 p1 c0 {2,S} {3,S}
2 Li u0 p0 c0 {1,S}
3 Li u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.38986,0.0122067,-3.72193e-05,7.43691e-08,-6.12596e-11,47306.7,5.60971], Tmin=(10,'K'), Tmax=(297.569,'K')),
            NASAPolynomial(coeffs=[3.86841,0.0057739,-4.79238e-06,1.72024e-09,-2.23936e-13,47278.3,3.88106], Tmin=(297.569,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (393.338,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (54.0441,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'Li-N': 2}

External symmetry: 2, optical isomers: 1

Geometry:
Li      0.00000000   -0.00020175    1.75971927
N       0.00000000    0.00017294   -0.00000022
Li      0.00000000   -0.00020176   -1.75971876
""",
)

entry(
    index = 65,
    label = "[Lip]",
    molecule =
"""
1 Li u0 p0 c+1
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,1.99051e-15,-1.1909e-17,2.10806e-20,-1.11018e-23,63352,1.74004], Tmin=(10,'K'), Tmax=(794.005,'K')),
            NASAPolynomial(coeffs=[2.5,1.52667e-14,-1.58445e-17,6.63089e-21,-9.62112e-25,63352,1.74004], Tmin=(794.005,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (526.738,'kJ/mol'),
        Cp0 = (20.7862,'J/(mol*K)'),
        CpInf = (20.7862,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
External symmetry: 1, optical isomers: 1

Geometry:
Li      0.00000000    0.00000000    0.00000000
""",
)

entry(
    index = 66,
    label = "[Li]O[CH]OC",
    molecule =
"""
multiplicity 2
1 O  u0 p2 c0 {3,S} {4,S}
2 O  u0 p2 c0 {4,S} {5,S}
3 C  u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
4 C  u1 p0 c0 {1,S} {2,S} {9,S}
5 Li u0 p0 c0 {2,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {3,S}
8 H  u0 p0 c0 {3,S}
9 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63714,0.0350916,-7.124e-05,1.35265e-07,-1.01916e-10,-32694.7,10.5138], Tmin=(10,'K'), Tmax=(443.395,'K')),
            NASAPolynomial(coeffs=[3.22395,0.0290546,-1.77838e-05,5.22363e-09,-5.91509e-13,-32562.1,13.2535], Tmin=(443.395,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-271.849,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (203.705,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-O': 3, 'C-H': 4, 'Li-O': 1}
1D rotors:
* Invalidated! pivots: [3, 5], dihedral: [2, 3, 5, 6], invalidation reason: Bond ([[1, 5]]) broke during the scan.Bond ([[1, 2]]) broke during the scan.Bond ([[1, 3]]) broke during the scan.Bond ([[3, 5]]) broke during the scan.Significant difference observed between consecutive conformersCould not read energies
pivots: [5, 6], dihedral: [3, 5, 6, 7], rotor symmetry: 3, max scan energy: 4.16 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 5], invalidation reason: Significant difference observed between consecutive conformersCould not read energies


External symmetry: 1, optical isomers: 2

Geometry:
Li     -1.03857386   -1.50184097    0.00809784
O      -1.73352647    0.13140005   -0.06318938
C      -0.56669713    0.66784891   -0.07587473
H      -0.33829942    1.54358645    0.55714264
O       0.46040589   -0.37188841    0.15429302
C       1.77670709    0.06072398   -0.07599580
H       2.45412720   -0.76467364    0.14510036
H       2.02652553    0.90251337    0.57904743
H       1.90985604    0.37589994   -1.11558237
""",
)

entry(
    index = 67,
    label = "[Li]OCCC[CH2]",
    molecule =
"""
multiplicity 2
1  O  u0 p2 c0 {4,S} {6,S}
2  C  u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
3  C  u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
4  C  u0 p0 c0 {1,S} {2,S} {11,S} {12,S}
5  C  u1 p0 c0 {3,S} {13,S} {14,S}
6  Li u0 p0 c0 {1,S}
7  H  u0 p0 c0 {2,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {3,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {4,S}
12 H  u0 p0 c0 {4,S}
13 H  u0 p0 c0 {5,S}
14 H  u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.35709,0.070894,-0.000283588,7.45283e-07,-6.70718e-10,-10748.6,14.3032], Tmin=(10,'K'), Tmax=(387.288,'K')),
            NASAPolynomial(coeffs=[0.931357,0.0507798,-3.07456e-05,8.91367e-09,-9.95967e-13,-10221.9,28.0782], Tmin=(387.288,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-89.3964,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (320.107,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'Li-O': 1, 'C-H': 8, 'C-C': 3, 'C-O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 2, max scan energy: 0.01 kJ/mol (set as a FreeRotor)
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 22.89 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 12 5 6 7 F
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: Another conformer for [Li]OCCC[CH2] exists which is 13.51 kJ/mol lower.Another conformer for [Li]OCCC[CH2] exists which is 13.51 kJ/mol lower. But unable to propose troubleshooting methods.
pivots: [5, 6], dihedral: [4, 5, 6, 7], rotor symmetry: 2, max scan energy: 1.43 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
Li      2.65156680   -1.70789057    0.30718437
O       1.83310321   -0.36794508    0.02854412
C       1.16086153    0.80508387   -0.19358600
C      -0.28166293    0.77258504    0.31360080
C      -1.13869218   -0.27090054   -0.39648057
C      -2.50642918   -0.41383081    0.15735993
H      -3.31337560   -0.82997659   -0.43238641
H       1.13386102    1.05295006   -1.27218772
H       1.66639133    1.65735811    0.29426923
H      -0.73412464    1.76361142    0.19363369
H      -0.26454616    0.55606672    1.38839070
H      -1.19039080   -0.03881783   -1.46757237
H      -0.60407635   -1.23258534   -0.34162721
H      -2.70330945   -0.20459326    1.20218938
""",
)

entry(
    index = 68,
    label = "[Li]S",
    molecule =
"""
1 S  u0 p2 c0 {2,S} {3,S}
2 Li u0 p0 c0 {1,S}
3 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96923,0.0019845,1.99192e-05,-5.32821e-08,3.90783e-11,-5024.44,5.08461], Tmin=(10,'K'), Tmax=(504.914,'K')),
            NASAPolynomial(coeffs=[4.66999,0.00286084,-1.78023e-06,5.82381e-10,-7.59105e-14,-5177.14,1.37135], Tmin=(504.914,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-41.7832,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'Li-S': 1, 'H-S': 1}

External symmetry: 1, optical isomers: 1

Geometry:
Li      1.84021343   -0.04837003    0.00000000
S      -0.30984691    0.08578287    0.00000000
H      -0.56302646   -1.22984230    0.00000000
""",
)

entry(
    index = 69,
    label = "[Li]O[C]1CCCC1",
    molecule =
"""
multiplicity 2
1  O  u0 p2 c0 {6,S} {7,S}
2  C  u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
3  C  u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
4  C  u0 p0 c0 {2,S} {6,S} {12,S} {13,S}
5  C  u0 p0 c0 {3,S} {6,S} {14,S} {15,S}
6  C  u1 p0 c0 {1,S} {4,S} {5,S}
7  Li u0 p0 c0 {1,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {2,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {3,S}
12 H  u0 p0 c0 {4,S}
13 H  u0 p0 c0 {4,S}
14 H  u0 p0 c0 {5,S}
15 H  u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93752,0.0286225,3.48577e-05,-5.50632e-08,1.99394e-11,-13557,11.7049], Tmin=(10,'K'), Tmax=(1026.69,'K')),
            NASAPolynomial(coeffs=[6.51702,0.0432667,-2.2616e-05,5.68358e-09,-5.57074e-13,-15388.1,-7.14593], Tmin=(1026.69,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-112.619,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (357.522,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-C': 5, 'Li-O': 1, 'C-H': 8, 'C-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason:


External symmetry: 1, optical isomers: 2

Geometry:
Li     -3.54158338    0.00311757    0.17095482
O      -1.94125323    0.01045503   -0.01348004
C      -0.63838963    0.01973540   -0.18280423
C       0.20293966    1.22593114    0.10887890
C       1.62262727    0.73264867   -0.17533463
C       1.59216849   -0.74252280    0.25122025
C       0.18831035   -1.23673134   -0.13059194
H      -0.07732366    2.09640786   -0.49439304
H       0.10177795    1.53586568    1.16626735
H       2.39486644    1.30348604    0.34479756
H       1.82682018    0.80494636   -1.24781219
H       1.71618179   -0.80378973    1.33675718
H       2.39798069   -1.32747238   -0.19740416
H      -0.21404360   -1.94764786    0.60512411
H       0.19696832   -1.76962200   -1.09263082
""",
)

entry(
    index = 70,
    label = "[Li]O[C]1CCC1",
    molecule =
"""
multiplicity 2
1  O  u0 p2 c0 {5,S} {6,S}
2  C  u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
3  C  u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
4  C  u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
5  C  u1 p0 c0 {1,S} {3,S} {4,S}
6  Li u0 p0 c0 {1,S}
7  H  u0 p0 c0 {2,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {3,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {4,S}
12 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93888,0.0233308,2.54736e-05,-4.24544e-08,1.57e-11,-1104.3,10.353], Tmin=(10,'K'), Tmax=(1015.42,'K')),
            NASAPolynomial(coeffs=[6.28302,0.0333074,-1.76429e-05,4.48549e-09,-4.441e-13,-2570.74,-5.86875], Tmin=(1015.42,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-9.104,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-C': 4, 'Li-O': 1, 'C-H': 6, 'C-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Could not read energies


External symmetry: 1, optical isomers: 1

Geometry:
Li     -3.25237932   -0.00058684    0.16210418
O      -1.65036734    0.00124157   -0.03926158
C      -0.36231899    0.00039519   -0.25332717
C       0.63346917    1.09701247    0.04241226
C       1.72714666   -0.00124672    0.01941377
C       0.63180377   -1.09780903    0.04208321
H       0.73454791    1.91820676   -0.67498982
H       0.50017518    1.53917793    1.04310533
H       2.30237676   -0.00157985   -0.90648270
H       2.41816730   -0.00196854    0.86227331
H       0.49785262   -1.54001513    1.04268678
H       0.73164766   -1.91902109   -0.67549181
""",
)

entry(
    index = 71,
    label = "[Li]N[C]1CCC1",
    molecule =
"""
multiplicity 2
1  N  u0 p1 c0 {5,S} {6,S} {13,S}
2  C  u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
3  C  u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
4  C  u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
5  C  u1 p0 c0 {1,S} {3,S} {4,S}
6  Li u0 p0 c0 {1,S}
7  H  u0 p0 c0 {2,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {3,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {4,S}
12 H  u0 p0 c0 {4,S}
13 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83964,0.0229529,4.34231e-05,-7.20658e-08,2.98999e-11,27958,11.1235], Tmin=(10,'K'), Tmax=(854.242,'K')),
            NASAPolynomial(coeffs=[3.66685,0.0426371,-2.42848e-05,6.64068e-09,-7.03955e-13,27298.8,7.89894], Tmin=(854.242,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (232.487,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-C': 4, 'Li-N': 1, 'C-H': 6, 'H-N': 1, 'C-N': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for [Li]N[C]1CCC1 exists which is 2.19 kJ/mol lower.Another conformer for [Li]N[C]1CCC1 exists which is 2.19 kJ/mol lower. But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
Li      2.12137304   -1.20878198    0.39538403
N       1.73816105    0.46469490   -0.06760718
C       0.41006639    0.26847778   -0.26987465
C      -0.81764282    1.04886068    0.13975562
C      -1.61508070   -0.27261533    0.01699972
C      -0.28777320   -1.06173673   -0.09237307
H       1.99100428    1.44023735   -0.10077547
H      -0.77371387    1.41925941    1.17731508
H      -1.13934712    1.87780024   -0.49781578
H      -2.25117726   -0.52985237    0.86398655
H      -2.20621556   -0.33216598   -0.89626521
H      -0.06166060   -1.58574625    0.87540783
H      -0.22177374   -1.81252198   -0.89103837
""",
)

entry(
    index = 72,
    label = "[Li]N[C]1CC1",
    molecule =
"""
multiplicity 2
1  N  u0 p1 c0 {4,S} {5,S} {10,S}
2  C  u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
3  C  u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  C  u1 p0 c0 {1,S} {2,S} {3,S}
5  Li u0 p0 c0 {1,S}
6  H  u0 p0 c0 {2,S}
7  H  u0 p0 c0 {2,S}
8  H  u0 p0 c0 {3,S}
9  H  u0 p0 c0 {3,S}
10 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91514,0.00507845,0.00011502,-2.25656e-07,1.34999e-10,34629.6,10.4845], Tmin=(10,'K'), Tmax=(544.769,'K')),
            NASAPolynomial(coeffs=[2.11505,0.0369648,-2.41827e-05,7.60098e-09,-9.14215e-13,34548.7,15.533], Tmin=(544.769,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (287.894,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-C': 3, 'Li-N': 1, 'C-H': 4, 'H-N': 1, 'C-N': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformersBond ([[3, 5]]) broke during the scan.Significant difference observed between consecutive conformersThe rotor scan has a barrier of 149.32 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 1, optical isomers: 2

Geometry:
Li      1.44127103   -1.34532895    0.04945053
N       1.41392218    0.42178528   -0.11829191
C       0.16564039    0.24093601    0.40854955
C      -1.16129392    0.64999160   -0.05786186
C      -0.79415443   -0.83596650   -0.07951571
H       1.68844980    1.39187552   -0.11297016
H      -1.91348796    0.96332389    0.65791161
H      -1.24350692    1.12656757   -1.03269162
H      -1.31329625   -1.48441404    0.62025372
H      -0.69867618   -1.25380598   -1.08665912
""",
)

entry(
    index = 73,
    label = "[Li]O[C]1OC[F]C[F]O1",
    molecule =
"""
multiplicity 2
1  C  u0 p0 c0 {2,S} {4,S} {7,S} {9,S}
2  C  u0 p0 c0 {1,S} {5,S} {8,S} {10,S}
3  C  u1 p0 c0 {4,S} {5,S} {6,S}
4  O  u0 p2 c0 {1,S} {3,S}
5  O  u0 p2 c0 {2,S} {3,S}
6  O  u0 p2 c0 {3,S} {11,S}
7  F  u0 p3 c0 {1,S}
8  F  u0 p3 c0 {2,S}
9  H  u0 p0 c0 {1,S}
10 H  u0 p0 c0 {2,S}
11 Li u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.62801,0.034916,3.70735e-05,-1.12874e-07,6.72118e-11,-106338,13.6645], Tmin=(10,'K'), Tmax=(650.486,'K')),
            NASAPolynomial(coeffs=[6.95108,0.0383496,-2.58832e-05,8.05619e-09,-9.4442e-13,-107275,-4.81986], Tmin=(650.486,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-884.191,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-O': 5, 'Li-O': 1, 'C-F': 2, 'C-H': 2, 'C-C': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 2]]) broke during the scan.Bond ([[3, 4]]) broke during the scan.


External symmetry: 1, optical isomers: 2

Geometry:
Li      2.31216787   -1.02869677   -0.26921855
O       2.21551058    0.71788977    0.18177824
C       1.02915949    0.80141297   -0.19921834
O       0.54943282   -0.56168751   -0.86406925
C      -0.66106558   -0.88728198   -0.34335072
F      -0.50714801   -1.90574727    0.59952950
C      -1.13168119    0.37555729    0.38806052
F      -1.88199254    1.12964501   -0.48825733
O       0.01657502    1.01726482    0.75460292
H      -1.35910508   -1.25095412   -1.09810642
H      -1.74049887    0.17685648    1.26948942
""",
)

entry(
    index = 74,
    label = "[Li]O[C]1OC=CO1",
    molecule =
"""
multiplicity 2
1 C  u1 p0 c0 {4,S} {5,S} {6,S}
2 C  u0 p0 c0 {3,D} {4,S} {7,S}
3 C  u0 p0 c0 {2,D} {5,S} {8,S}
4 O  u0 p2 c0 {1,S} {2,S}
5 O  u0 p2 c0 {1,S} {3,S}
6 O  u0 p2 c0 {1,S} {9,S}
7 H  u0 p0 c0 {2,S}
8 H  u0 p0 c0 {3,S}
9 Li u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86412,0.00832872,0.000129066,-2.8319e-07,1.81422e-10,-37308.3,11.9635], Tmin=(10,'K'), Tmax=(537.332,'K')),
            NASAPolynomial(coeffs=[4.30212,0.0341831,-2.43855e-05,8.0357e-09,-9.91309e-13,-37775.6,6.2114], Tmin=(537.332,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-310.245,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-O': 5, 'Li-O': 1, 'C-H': 2, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 2]]) broke during the scan.Bond ([[3, 7]]) broke during the scan.Bond ([[1, 4]]) broke during the scan.


External symmetry: 1, optical isomers: 2

Geometry:
Li      1.76319420   -1.27108521    0.59906957
O       1.80575033    0.43882088    0.09017800
C       0.65821270    0.35580430   -0.42501099
O       0.05574337   -1.05778288   -0.22838511
C      -1.27321942   -0.83852019    0.02378339
C      -1.51157289    0.45695000    0.16269662
O      -0.37912860    1.20170468    0.04002300
H      -1.94223832   -1.68198988    0.06175783
H      -2.43518699    0.97874604    0.34905300
""",
)

entry(
    index = 75,
    label = "[Li]O[C]1OCC[C]O1",
    molecule =
"""
multiplicity 2
1  C  u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C  u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
3  C  u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C  u1 p0 c0 {5,S} {6,S} {7,S}
5  O  u0 p2 c0 {1,S} {4,S}
6  O  u0 p2 c0 {2,S} {4,S}
7  O  u0 p2 c0 {4,S} {14,S}
8  H  u0 p0 c0 {1,S}
9  H  u0 p0 c0 {2,S}
10 H  u0 p0 c0 {2,S}
11 H  u0 p0 c0 {3,S}
12 H  u0 p0 c0 {3,S}
13 H  u0 p0 c0 {3,S}
14 Li u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65683,0.029923,7.07203e-05,-1.6132e-07,9.43272e-11,-56409.8,12.7593], Tmin=(10,'K'), Tmax=(591.212,'K')),
            NASAPolynomial(coeffs=[3.28389,0.05154,-3.25697e-05,9.77914e-09,-1.12351e-12,-56699.4,11.5404], Tmin=(591.212,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-469.068,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (328.422,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-O': 5, 'Li-O': 1, 'C-H': 6, 'C-C': 2}
1D rotors:
pivots: [6, 7], dihedral: [5, 6, 7, 12], rotor symmetry: 3, max scan energy: 12.02 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
B 3 4 F
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformersCould not read energies


External symmetry: 1, optical isomers: 2

Geometry:
Li      2.50584525   -0.78828294   -0.69813951
O       2.12471544    0.86363316   -0.13337501
C       1.05088170    0.45406358    0.39004837
O       0.84507869   -1.05615155    0.12271651
C      -0.54104844   -1.27298426   -0.00465370
C      -1.16506117    0.07652894    0.37678146
C      -2.45642688    0.40047580   -0.33113096
O      -0.16122353    1.00144264    0.00526627
H      -0.86531864   -2.08034078    0.65665746
H      -0.79365219   -1.53520834   -1.03903616
H      -1.30273048    0.11634088    1.46483211
H      -3.22015929   -0.34013831   -0.08368654
H      -2.82208171    1.38216801   -0.02999007
H      -2.30794536    0.40301579   -1.41250983
""",
)

entry(
    index = 76,
    label = "[Li]O[C]1OCC[F]O1",
    molecule =
"""
multiplicity 2
1  C  u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C  u0 p0 c0 {1,S} {5,S} {7,S} {10,S}
3  C  u1 p0 c0 {4,S} {5,S} {6,S}
4  O  u0 p2 c0 {1,S} {3,S}
5  O  u0 p2 c0 {2,S} {3,S}
6  O  u0 p2 c0 {3,S} {11,S}
7  F  u0 p3 c0 {2,S}
8  H  u0 p0 c0 {1,S}
9  H  u0 p0 c0 {1,S}
10 H  u0 p0 c0 {2,S}
11 Li u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.60004,0.037174,6.60137e-06,-5.08416e-08,2.99966e-11,-80409.7,13.1049], Tmin=(10,'K'), Tmax=(714.515,'K')),
            NASAPolynomial(coeffs=[6.65142,0.0355835,-2.25818e-05,6.73166e-09,-7.64695e-13,-81241.2,-3.35774], Tmin=(714.515,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-668.604,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-O': 5, 'Li-O': 1, 'C-F': 1, 'C-H': 3, 'C-C': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[6, 7]]) broke during the scan.Significant difference observed between consecutive conformersCould not read energies


External symmetry: 1, optical isomers: 2

Geometry:
Li     -1.26224708   -1.74287019   -0.07749486
O      -2.24705125   -0.08783972    0.38609544
C      -1.32986025    0.51755803   -0.11841207
O      -0.39508197    1.18419749    0.52800235
C       0.85397382    1.17718982   -0.17643787
C       1.21291489   -0.29623927   -0.42241167
F       1.73938621   -0.78715959    0.80616903
O       0.14279799   -0.98020880   -0.78054098
H       0.74784282    1.70140718   -1.12836553
H       1.57015796    1.68280861    0.46530985
H       2.05229511   -0.37202505   -1.12911706
""",
)

entry(
    index = 77,
    label = "[Li]OC[=O]O[Li]",
    molecule =
"""
1 O  u0 p2 c0 {4,S} {5,S}
2 O  u0 p2 c0 {4,S} {6,S}
3 O  u0 p2 c0 {4,D}
4 C  u0 p0 c0 {1,S} {2,S} {3,D}
5 Li u0 p0 c0 {1,S}
6 Li u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87546,0.00795604,9.20845e-05,-2.28033e-07,1.58705e-10,-100788,8.62073], Tmin=(10,'K'), Tmax=(512.617,'K')),
            NASAPolynomial(coeffs=[5.46075,0.0201463,-1.54536e-05,5.28734e-09,-6.65984e-13,-101274,-1.11556], Tmin=(512.617,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-838.036,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'Li-O': 2, 'C-O': 2, 'C=O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 4]]) broke during the scan.Bond ([[1, 2]]) broke during the scan.The rotor scan has a barrier of 620.98 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
* Invalidated! pivots: [3, 5], dihedral: [2, 3, 5, 6], invalidation reason: Bond ([[4, 6]]) broke during the scan.Bond ([[5, 6]]) broke during the scan.The rotor scan has a barrier of 448.06 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 2, optical isomers: 1

Geometry:
Li      1.81473397   -0.88083680    0.00000911
O       1.12989196    0.79976099   -0.00000834
C       0.00001455    0.23703003    0.00000114
O      -0.00004293   -1.11668336   -0.00000212
O      -1.12980128    0.79987765    0.00000519
Li     -1.81478521   -0.88069470   -0.00002494
""",
)

entry(
    index = 78,
    label = "[Li]OC[=O]OC=[CH]",
    molecule =
"""
multiplicity 2
1 C  u0 p0 c0 {3,S} {4,S} {6,D}
2 C  u0 p0 c0 {3,S} {5,D} {7,S}
3 O  u0 p2 c0 {1,S} {2,S}
4 O  u0 p2 c0 {1,S} {8,S}
5 C  u1 p0 c0 {2,D} {9,S}
6 O  u0 p2 c0 {1,D}
7 H  u0 p0 c0 {2,S}
8 Li u0 p0 c0 {4,S}
9 H  u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76778,0.0163747,0.000145267,-4.11589e-07,3.24143e-10,-44555.7,11.4265], Tmin=(10,'K'), Tmax=(454.542,'K')),
            NASAPolynomial(coeffs=[5.99901,0.0321835,-2.3868e-05,8.0277e-09,-1.00158e-12,-45124.7,-1.60632], Tmin=(454.542,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-370.482,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (199.547,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-O': 3, 'Li-O': 1, 'C-H': 2, 'C=O': 1, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 4]]) broke during the scan.Bond ([[1, 2]]) broke during the scan.Bond ([[3, 5]]) broke during the scan.The rotor scan has a barrier of 814.73 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
pivots: [3, 5], dihedral: [2, 3, 5, 6], rotor symmetry: 2, max scan energy: 38.87 kJ/mol
pivots: [5, 6], dihedral: [3, 5, 6, 7], rotor symmetry: 1, max scan energy: 18.58 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
Li      2.76469604   -0.59357089    0.00002368
O       1.71366737    0.94278211   -0.00004256
C       0.78494466    0.10756293   -0.00000577
O       0.96874932   -1.13735830    0.00001336
O      -0.46960100    0.61863383    0.00003236
C      -1.52489604   -0.25973243    0.00007217
C      -2.76251998    0.15189037    0.00012965
H      -1.24193576   -1.31007574    0.00005316
H      -3.73574306   -0.30704369    0.00016804
""",
)

entry(
    index = 79,
    label = "[Li]OC[C][CH2]",
    molecule =
"""
multiplicity 2
1  C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C  u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C  u1 p0 c0 {1,S} {9,S} {10,S}
4  O  u0 p2 c0 {1,S} {11,S}
5  H  u0 p0 c0 {1,S}
6  H  u0 p0 c0 {2,S}
7  H  u0 p0 c0 {2,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {3,S}
10 H  u0 p0 c0 {3,S}
11 Li u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72382,0.0311581,-1.29153e-05,-7.09056e-10,1.27325e-12,-9408.72,12.8436], Tmin=(10,'K'), Tmax=(1261.68,'K')),
            NASAPolynomial(coeffs=[8.78445,0.0221228,-1.05061e-05,2.42097e-09,-2.19415e-13,-11243.5,-14.958], Tmin=(1261.68,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-78.236,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (245.277,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'Li-O': 1, 'C-H': 6, 'C-C': 2, 'C-O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 0.03 kJ/mol (set as a FreeRotor)
pivots: [3, 4], dihedral: [2, 3, 4, 7], rotor symmetry: 3, max scan energy: 15.25 kJ/mol
pivots: [3, 5], dihedral: [2, 3, 5, 10], rotor symmetry: 1, max scan energy: 3.55 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 6 2 3 5 F
D 3 5 10 11 F


External symmetry: 1, optical isomers: 2

Geometry:
Li     -2.68901305   -0.15270806    0.35428863
O      -1.15392112   -0.02771453   -0.05939556
C       0.18223127    0.06366786   -0.34924854
C       0.94812163   -1.16950408    0.15648782
C       0.79801589    1.32005926    0.17293184
H       0.33023049    0.07676425   -1.45333387
H       0.52608004   -2.07056494   -0.29381004
H       0.84799161   -1.24413110    1.24217681
H       2.01157315   -1.12002543   -0.09329970
H       0.15900161    2.13154310    0.49653513
H       1.86671261    1.49106420    0.10401218
""",
)

entry(
    index = 80,
    label = "[Li]OC=[CH]",
    molecule =
"""
multiplicity 2
1 O  u0 p2 c0 {2,S} {4,S}
2 C  u0 p0 c0 {1,S} {3,D} {5,S}
3 C  u1 p0 c0 {2,D} {6,S}
4 Li u0 p0 c0 {1,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93579,0.00411611,6.92523e-05,-1.56657e-07,1.05839e-10,7403.46,9.37372], Tmin=(10,'K'), Tmax=(498.449,'K')),
            NASAPolynomial(coeffs=[3.73565,0.0184865,-1.24049e-05,3.93322e-09,-4.73461e-13,7264.84,8.60934], Tmin=(498.449,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (61.5394,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'Li-O': 1, 'C-H': 2, 'C=C': 1, 'C-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 4]]) broke during the scan.Bond ([[1, 2]]) broke during the scan.Bond ([[3, 5]]) broke during the scan.The rotor scan has a barrier of 419.79 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 1, optical isomers: 2

Geometry:
Li     -0.24219556   -1.61565234    0.08711579
O      -1.10762387    0.06731978   -0.05277878
C       0.04086396    0.59876099    0.03551488
C       1.19131815   -0.21877609   -0.02333034
H       0.06777255    1.69047635    0.19514479
H       2.12271610    0.33940324   -0.12360749
""",
)

entry(
    index = 81,
    label = "O=[C]OC[F]C[F]O[Li]",
    molecule =
"""
multiplicity 2
1  C  u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C  u0 p0 c0 {1,S} {4,S} {7,S} {9,S}
3  O  u0 p2 c0 {1,S} {5,S}
4  O  u0 p2 c0 {2,S} {10,S}
5  C  u1 p0 c0 {3,S} {11,D}
6  F  u0 p3 c0 {1,S}
7  F  u0 p3 c0 {2,S}
8  H  u0 p0 c0 {1,S}
9  H  u0 p0 c0 {2,S}
10 Li u0 p0 c0 {4,S}
11 O  u0 p2 c0 {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.43712,0.0484992,4.0178e-05,-2.50676e-07,2.40768e-10,-105869,14.0789], Tmin=(10,'K'), Tmax=(424.323,'K')),
            NASAPolynomial(coeffs=[7.05273,0.0414265,-3.03037e-05,1.0078e-08,-1.24736e-12,-106419,-3.13012], Tmin=(424.323,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-880.259,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (253.591,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'Li-O': 1, 'C-O': 3, 'C-F': 2, 'C-H': 2, 'C=O': 1, 'C-C': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 40.00 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 4 6 9 F
A 9 6 11 F
D 2 3 4 10 F
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: rotor scan switching back and forth between conformers or trying to switch ot a non-isomorphic conformer invalidating rotorAnother conformer for O=[C]OC[F]C[F]O[Li] exists which is 0.95 kJ/mol lower. But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 6], dihedral: [3, 4, 6, 7], invalidation reason: rotor scan switching back and forth between conformers or trying to switch ot a non-isomorphic conformer invalidating rotorAnother conformer for O=[C]OC[F]C[F]O[Li] exists which is 6.23 kJ/mol lower. But unable to propose troubleshooting methods.
* Invalidated! pivots: [6, 8], dihedral: [4, 6, 8, 9], invalidation reason: Bond ([[6, 7]]) broke during the scan.Bond ([[7, 9]]) broke during the scan.The rotor scan has a barrier of 338.03 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.99310378   -0.71966885    0.22853163
C      -2.09512330   -0.11621907   -0.22641717
O      -0.84243667   -0.08977065    0.22790846
C       0.07536812    0.70970669   -0.48863120
F       0.13412276    1.93202869    0.09547586
C       1.43165396    0.00336365   -0.47769869
F       1.69560630   -0.10278970    1.11852035
O       1.44062386   -1.18400191   -0.92587638
Li      1.42014704   -1.87402022    0.74750256
H      -0.26847864    0.83206969   -1.51911196
H       2.24595251    0.69691541   -0.73199850
""",
)

entry(
    index = 82,
    label = "O=[C]OC[F]C=O",
    molecule =
"""
multiplicity 2
1 F u0 p3 c0 {5,S}
2 O u0 p2 c0 {5,S} {7,S}
3 O u0 p2 c0 {6,D}
4 O u0 p2 c0 {7,D}
5 C u0 p0 c0 {1,S} {2,S} {6,S} {8,S}
6 C u0 p0 c0 {3,D} {5,S} {9,S}
7 C u1 p0 c0 {2,S} {4,D}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.57376,0.0446862,-0.000101648,2.17166e-07,-1.95627e-10,-56377.8,13.387], Tmin=(10,'K'), Tmax=(341.243,'K')),
            NASAPolynomial(coeffs=[3.9893,0.0332948,-2.29127e-05,7.35019e-09,-8.89353e-13,-56368.2,12.3853], Tmin=(341.243,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-468.749,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-O': 2, 'C-F': 1, 'C-H': 2, 'C=O': 2, 'C-C': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: rotor scan switching back and forth between conformers or trying to switch ot a non-isomorphic conformer invalidating rotorAnother conformer for O=[C]OC[F]C=O exists which is 1.11 kJ/mol lower. But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: rotor scan switching back and forth between conformers or trying to switch ot a non-isomorphic conformer invalidating rotorAnother conformer for O=[C]OC[F]C=O exists which is 4.77 kJ/mol lower. But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 6], dihedral: [3, 4, 6, 7], invalidation reason: rotor scan switching back and forth between conformers or trying to switch ot a non-isomorphic conformer invalidating rotorAnother conformer for O=[C]OC[F]C=O exists which is 1.15 kJ/mol lower. But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.51938227   -0.26276432   -0.22829091
C      -1.36410872   -0.09165462   -0.28174873
O      -0.59173754    0.41245191    0.70696659
C       0.75906594    0.55479786    0.41185809
F       0.95482175    1.58832360   -0.45849137
C       1.40541545   -0.70008427   -0.18593122
O       0.98233421   -1.79957166   -0.00322524
H       1.24259359    0.80763160    1.35956411
H       2.32059986   -0.49259309   -0.77147514
""",
)

entry(
    index = 83,
    label = "O=[C]OC[F]CO[Li]",
    molecule =
"""
multiplicity 2
1  C  u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C  u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  O  u0 p2 c0 {1,S} {5,S}
4  O  u0 p2 c0 {2,S} {10,S}
5  C  u1 p0 c0 {3,S} {11,D}
6  F  u0 p3 c0 {1,S}
7  H  u0 p0 c0 {1,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {2,S}
10 Li u0 p0 c0 {4,S}
11 O  u0 p2 c0 {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.43415,0.0523497,-5.48659e-05,3.27426e-08,-8.56065e-12,-71983.2,15.299], Tmin=(10,'K'), Tmax=(832.286,'K')),
            NASAPolynomial(coeffs=[7.15891,0.0344484,-2.26032e-05,6.90001e-09,-7.98157e-13,-72603.2,-1.98707], Tmin=(832.286,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-598.552,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (245.277,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'Li-O': 1, 'C-O': 3, 'C-F': 1, 'C-H': 3, 'C=O': 1, 'C-C': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 37.64 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 15.58 kJ/mol
* Invalidated! pivots: [4, 6], dihedral: [3, 4, 6, 7], invalidation reason: Another conformer for O=[C]OC[F]CO[Li] exists which is 5.71 kJ/mol lower.Another conformer for O=[C]OC[F]CO[Li] exists which is 5.71 kJ/mol lower. But unable to propose troubleshooting methods.
pivots: [6, 7], dihedral: [4, 6, 7, 8], rotor symmetry: 1, max scan energy: 0.46 kJ/mol (set as a FreeRotor)
Troubleshot with the following constraints and 8.0 degrees resolution:
D 4 4 6 7 F


External symmetry: 1, optical isomers: 2

Geometry:
O      -3.23704678   -0.21207904   -0.10502209
C      -2.11631669    0.02699007   -0.36886036
O      -1.03643868   -0.32249573    0.31941470
C       0.20970479    0.13456277   -0.18735740
F       0.39699555    1.40834239    0.28196237
C       1.30424316   -0.79025266    0.30785232
O       2.51792238   -0.40051445   -0.15820543
Li      3.89798045    0.33168164   -0.53701179
H       0.16826893    0.19368225   -1.27770683
H       1.01699678   -1.80448750   -0.02099078
H       1.23844457   -0.78997447    1.41025220
""",
)

entry(
    index = 84,
    label = "O=[C]OCC[C]O[Li]",
    molecule =
"""
multiplicity 2
1  C  u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C  u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C  u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  O  u0 p2 c0 {2,S} {6,S}
5  O  u0 p2 c0 {1,S} {13,S}
6  C  u1 p0 c0 {4,S} {14,D}
7  H  u0 p0 c0 {1,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {2,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {3,S}
12 H  u0 p0 c0 {3,S}
13 Li u0 p0 c0 {5,S}
14 O  u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.43117,0.0521503,-3.48841e-05,1.13712e-08,-1.45731e-12,-50234.5,14.5367], Tmin=(10,'K'), Tmax=(2030.99,'K')),
            NASAPolynomial(coeffs=[7.54154,0.0374472,-1.91449e-05,4.60288e-09,-4.27002e-13,-50541.3,-4.85072], Tmin=(2030.99,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-417.739,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (320.107,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'Li-O': 1, 'C-O': 3, 'C-H': 6, 'C=O': 1, 'C-C': 2}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 41.06 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 2 3 4 5 F
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: rotor scan switching back and forth between conformers or trying to switch ot a non-isomorphic conformer invalidating rotorAnother conformer for O=[C]OCC[C]O[Li] exists which is 1.89 kJ/mol lower. But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: rotor scan switching back and forth between conformers or trying to switch ot a non-isomorphic conformer invalidating rotorAnother conformer for O=[C]OCC[C]O[Li] exists which is 40.40 kJ/mol lower. But unable to propose troubleshooting methods.
pivots: [5, 6], dihedral: [4, 5, 6, 12], rotor symmetry: 3, max scan energy: 14.01 kJ/mol
pivots: [5, 7], dihedral: [4, 5, 7, 8], rotor symmetry: 1, max scan energy: 0.10 kJ/mol (set as a FreeRotor)


External symmetry: 1, optical isomers: 2

Geometry:
O       3.08231176   -0.65658073   -0.22093650
C       2.01660616   -0.18793578   -0.41746657
O       1.20060774    0.35407846    0.45798592
C      -0.08069878    0.82073217   -0.02794507
C      -1.22812902   -0.09231429    0.39999715
C      -1.08920371   -1.48511271   -0.20762959
O      -2.39841718    0.51436153    0.03147798
Li     -3.81093204    1.12686913   -0.41624199
H      -0.22076414    1.80997961    0.40641125
H      -0.04519223    0.90003575   -1.11691008
H      -1.15744754   -0.19648590    1.49803670
H      -0.16579115   -1.98246090    0.09934853
H      -1.10681197   -1.42051222   -1.29948114
H      -1.92964695   -2.10395573    0.11149387
""",
)

entry(
    index = 85,
    label = "[Li]OC[=O]OC[CH]C",
    molecule =
"""
multiplicity 2
1  C  u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2  C  u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
3  C  u1 p0 c0 {1,S} {2,S} {12,S}
4  C  u0 p0 c0 {5,S} {6,S} {13,D}
5  O  u0 p2 c0 {1,S} {4,S}
6  O  u0 p2 c0 {4,S} {14,S}
7  H  u0 p0 c0 {1,S}
8  H  u0 p0 c0 {1,S}
9  H  u0 p0 c0 {2,S}
10 H  u0 p0 c0 {2,S}
11 H  u0 p0 c0 {2,S}
12 H  u0 p0 c0 {3,S}
13 O  u0 p2 c0 {4,D}
14 Li u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.06098,0.104104,-0.000477398,1.23891e-06,-1.12361e-09,-69993.7,14.5585], Tmin=(10,'K'), Tmax=(368.952,'K')),
            NASAPolynomial(coeffs=[2.36682,0.0533766,-3.43298e-05,1.03807e-08,-1.1959e-12,-69546,22.5885], Tmin=(368.952,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-582.003,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (320.107,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-O': 3, 'Li-O': 1, 'C-H': 6, 'C=O': 1, 'C-C': 2}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 4]]) broke during the scan.Bond ([[1, 4]]) broke during the scan. But unable to propose troubleshooting methods.
pivots: [3, 5], dihedral: [2, 3, 5, 6], rotor symmetry: 2, max scan energy: 37.74 kJ/mol
* Invalidated! pivots: [5, 6], dihedral: [3, 5, 6, 7], invalidation reason: Another conformer for [Li]OC[=O]OC[CH]C exists which is 0.79 kJ/mol lower.Another conformer for [Li]OC[=O]OC[CH]C exists which is 0.79 kJ/mol lower. But unable to propose troubleshooting methods.
pivots: [6, 7], dihedral: [5, 6, 7, 8], rotor symmetry: 1, max scan energy: 4.84 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 6 7 8 11 F
D 6 7 8 12 F
pivots: [7, 8], dihedral: [6, 7, 8, 12], rotor symmetry: 3, max scan energy: 1.64 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 10 6 7 11 F


External symmetry: 1, optical isomers: 2

Geometry:
Li      3.36776216   -0.05170088   -0.33267927
O       2.06216172    1.13221565    0.22973517
C       1.31644579    0.13748514    0.05001124
O       1.75021282   -0.97783374   -0.35624461
O       0.01605168    0.30086347    0.31133156
C      -0.83859751   -0.84232579    0.09400798
C      -2.23875517   -0.43666512    0.35138104
C      -2.85456477    0.67197314   -0.41689698
H      -0.70163441   -1.17300725   -0.94187998
H      -0.52153794   -1.65621030    0.74674582
H      -2.76078243   -0.86311715    1.19841843
H      -2.61957586    0.59294599   -1.48358423
H      -2.46365620    1.64394015   -0.08912465
H      -3.93872776    0.69498234   -0.30179528
""",
)

entry(
    index = 86,
    label = "[Li]OC[=O]OC[CH]F",
    molecule =
"""
multiplicity 2
1  C  u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C  u1 p0 c0 {1,S} {8,S} {9,S}
3  C  u0 p0 c0 {4,S} {5,S} {10,D}
4  O  u0 p2 c0 {1,S} {3,S}
5  O  u0 p2 c0 {3,S} {11,S}
6  H  u0 p0 c0 {1,S}
7  H  u0 p0 c0 {1,S}
8  F  u0 p3 c0 {2,S}
9  H  u0 p0 c0 {2,S}
10 O  u0 p2 c0 {3,D}
11 Li u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67422,0.0374098,0.000300027,-2.18322e-06,4.22361e-09,-88590.9,12.967], Tmin=(10,'K'), Tmax=(191.889,'K')),
            NASAPolynomial(coeffs=[5.36581,0.040814,-2.88378e-05,9.43147e-09,-1.15911e-12,-88727,5.74372], Tmin=(191.889,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-736.213,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (249.434,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-O': 3, 'Li-O': 1, 'C-F': 1, 'C-H': 3, 'C=O': 1, 'C-C': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 4]]) broke during the scan.Bond ([[1, 4]]) broke during the scan. But unable to propose troubleshooting methods.
pivots: [3, 5], dihedral: [2, 3, 5, 6], rotor symmetry: 2, max scan energy: 38.74 kJ/mol
* Invalidated! pivots: [5, 6], dihedral: [3, 5, 6, 7], invalidation reason: Another conformer for [Li]OC[=O]OC[CH]F exists which is 2.91 kJ/mol lower.Another conformer for [Li]OC[=O]OC[CH]F exists which is 2.91 kJ/mol lower. But unable to propose troubleshooting methods.
pivots: [6, 7], dihedral: [5, 6, 7, 8], rotor symmetry: 1, max scan energy: 23.22 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 6 7 8 11 F


External symmetry: 1, optical isomers: 2

Geometry:
Li      3.35504993   -0.25552923   -0.31649259
O       2.13792843    1.08932795    0.06735005
C       1.32314720    0.13762230    0.02420812
O       1.66836611   -1.05515726   -0.20635390
O       0.03312839    0.43296091    0.23751547
C      -0.88897858   -0.67174031    0.18330279
C      -2.25044346   -0.17913335    0.43973390
F      -2.87448247    0.41672876   -0.58212716
H      -0.83194638   -1.14471118   -0.79884822
H      -0.61471370   -1.41108706    0.93789668
H      -2.62112884    0.12711612    1.41017111
""",
)

entry(
    index = 87,
    label = "[Li]OC[=O]OC[F][CH]F",
    molecule =
"""
multiplicity 2
1  C  u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C  u1 p0 c0 {1,S} {8,S} {9,S}
3  C  u0 p0 c0 {4,S} {5,S} {10,D}
4  O  u0 p2 c0 {1,S} {3,S}
5  O  u0 p2 c0 {3,S} {11,S}
6  F  u0 p3 c0 {1,S}
7  H  u0 p0 c0 {1,S}
8  F  u0 p3 c0 {2,S}
9  H  u0 p0 c0 {2,S}
10 O  u0 p2 c0 {3,D}
11 Li u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.2531,0.0628784,-6.80592e-05,3.65095e-08,-7.79932e-12,-114295,14.431], Tmin=(10,'K'), Tmax=(1098.34,'K')),
            NASAPolynomial(coeffs=[13.9229,0.0240204,-1.49906e-05,4.29795e-09,-4.67425e-13,-116639,-38.0453], Tmin=(1098.34,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-950.378,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (245.277,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-O': 3, 'Li-O': 1, 'C-F': 2, 'C-H': 2, 'C=O': 1, 'C-C': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 4]]) broke during the scan.Bond ([[1, 2]]) broke during the scan.The rotor scan has a barrier of 259.03 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
pivots: [3, 5], dihedral: [2, 3, 5, 6], rotor symmetry: 2, max scan energy: 38.44 kJ/mol
pivots: [5, 6], dihedral: [3, 5, 6, 7], rotor symmetry: 1, max scan energy: 46.08 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 5 6 8 9 F
D 2 3 5 6 F
pivots: [6, 8], dihedral: [5, 6, 8, 9], rotor symmetry: 1, max scan energy: 16.30 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 6 8 9 11 F


External symmetry: 1, optical isomers: 2

Geometry:
Li      3.48184602   -0.45700838   -0.52227333
O       2.49702983    0.88193925    0.33365600
C       1.53841181    0.18482332   -0.05330402
O       1.65934830   -0.86239279   -0.73414595
O       0.30022427    0.62922664    0.29790176
C      -0.78304843   -0.17864630   -0.01497737
F      -0.93912167   -1.11725114    1.00030753
C      -1.97041382    0.69833868   -0.08672025
F      -3.06724771    0.13766758   -0.59152298
H      -0.62011013   -0.74757550   -0.93125431
H      -2.13941340    1.53321874    0.58108428
""",
)

entry(
    index = 88,
    label = "[Li]OC[=O]OC[F][CH2]",
    molecule =
"""
multiplicity 2
1  C  u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C  u1 p0 c0 {1,S} {8,S} {9,S}
3  C  u0 p0 c0 {4,S} {5,S} {10,D}
4  O  u0 p2 c0 {1,S} {3,S}
5  O  u0 p2 c0 {3,S} {11,S}
6  F  u0 p3 c0 {1,S}
7  H  u0 p0 c0 {1,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {2,S}
10 O  u0 p2 c0 {3,D}
11 Li u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.69471,0.0493902,-4.12142e-05,1.66166e-08,-2.64056e-12,-92020.1,12.6737], Tmin=(10,'K'), Tmax=(1446.52,'K')),
            NASAPolynomial(coeffs=[13.7451,0.0215983,-1.23948e-05,3.33442e-09,-3.45013e-13,-94927.7,-39.5238], Tmin=(1446.52,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-765.094,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (245.277,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-O': 3, 'Li-O': 1, 'C-F': 1, 'C-H': 3, 'C=O': 1, 'C-C': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 4]]) broke during the scan.Bond ([[1, 2]]) broke during the scan.Bond ([[3, 5]]) broke during the scan.The rotor scan has a barrier of 819.56 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
pivots: [3, 5], dihedral: [2, 3, 5, 6], rotor symmetry: 2, max scan energy: 37.98 kJ/mol
pivots: [5, 6], dihedral: [3, 5, 6, 7], rotor symmetry: 1, max scan energy: 46.10 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 5 6 8 11 F
D 2 3 5 6 F
pivots: [6, 8], dihedral: [5, 6, 8, 10], rotor symmetry: 2, max scan energy: 3.52 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
Li      3.07856075   -0.53733692   -0.21873064
O       2.04604248    0.86836532    0.43710318
C       1.11485782    0.17345570   -0.02087426
O       1.28859393   -0.91366272   -0.62705373
O      -0.13744343    0.66464504    0.15854292
C      -1.20955356   -0.13424772   -0.23238189
F      -1.48172392   -1.02673660    0.80554728
C      -2.38595243    0.72530372   -0.46101901
H      -0.93715876   -0.75329274   -1.08834681
H      -3.25941973    0.30781083   -0.93997557
H      -2.42312586    1.70946803   -0.01708330
""",
)

entry(
    index = 89,
    label = "[Li]OC[CH]C",
    molecule =
"""
multiplicity 2
1  C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C  u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C  u1 p0 c0 {1,S} {2,S} {10,S}
4  O  u0 p2 c0 {1,S} {11,S}
5  H  u0 p0 c0 {1,S}
6  H  u0 p0 c0 {1,S}
7  H  u0 p0 c0 {2,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {2,S}
10 H  u0 p0 c0 {3,S}
11 Li u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.51693,0.0537477,-0.000228072,6.03114e-07,-5.38826e-10,-8438.35,12.9396], Tmin=(10,'K'), Tmax=(392.076,'K')),
            NASAPolynomial(coeffs=[1.33208,0.0380321,-2.25456e-05,6.4118e-09,-7.04574e-13,-7974.9,25.1598], Tmin=(392.076,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-70.1823,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (249.434,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'Li-O': 1, 'C-H': 6, 'C-C': 2, 'C-O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 0.02 kJ/mol (set as a FreeRotor)
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Another conformer for [Li]OC[CH]C exists which is 1.20 kJ/mol lower.Another conformer for [Li]OC[CH]C exists which is 1.20 kJ/mol lower. But unable to propose troubleshooting methods.
pivots: [4, 5], dihedral: [3, 4, 5, 9], rotor symmetry: 3, max scan energy: 1.97 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
Li      2.39006454   -1.33050105   -0.15575866
O       1.32880536   -0.15135161    0.00045963
C       0.45686668    0.89779023    0.10918325
C      -0.96977347    0.56915265   -0.20316831
C      -1.53881871   -0.77536957    0.06051417
H       0.48119110    1.32217805    1.14009339
H       0.75337710    1.74472652   -0.53858346
H      -1.64983915    1.40382803   -0.34923198
H      -1.72447140   -0.94140550    1.13397517
H      -2.49053694   -0.92287189   -0.45418361
H      -0.84364137   -1.55667412   -0.25561951
""",
)

entry(
    index = 90,
    label = "[Li]OC[CH]F",
    molecule =
"""
multiplicity 2
1 C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C  u1 p0 c0 {1,S} {6,S} {7,S}
3 O  u0 p2 c0 {1,S} {8,S}
4 H  u0 p0 c0 {1,S}
5 H  u0 p0 c0 {1,S}
6 F  u0 p3 c0 {2,S}
7 H  u0 p0 c0 {2,S}
8 Li u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80494,0.0162487,4.36269e-05,-1.11702e-07,7.93727e-11,-30006.3,10.4182], Tmin=(10,'K'), Tmax=(369.712,'K')),
            NASAPolynomial(coeffs=[2.30703,0.032455,-2.21252e-05,6.86292e-09,-8.00862e-13,-29895.5,16.1542], Tmin=(369.712,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-249.501,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'Li-O': 1, 'C-F': 1, 'C-H': 3, 'C-C': 1, 'C-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformersThe rotor scan has a barrier of 55.35 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 51.28 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 1 2 3 F
D 3 4 5 8 F
D 1 2 3 4 F


External symmetry: 1, optical isomers: 2

Geometry:
Li     -0.18168932   -1.75818101   -0.06593475
O      -1.31052929   -0.49546158   -0.05438165
C      -0.76109450    0.74008371    0.09253753
C       0.70597988    0.75896110   -0.21007280
F       1.33940679   -0.44550273    0.09018487
H      -0.88545851    1.14552673    1.12552763
H      -1.21031049    1.51697870   -0.55971233
H       1.39127673    1.58749199   -0.06240866
""",
)

entry(
    index = 91,
    label = "[Li]OC[F][CH2]",
    molecule =
"""
multiplicity 2
1 C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C  u1 p0 c0 {1,S} {6,S} {7,S}
3 O  u0 p2 c0 {1,S} {8,S}
4 F  u0 p3 c0 {1,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {2,S}
8 Li u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79232,0.0185054,0.000103735,-4.24482e-07,4.7105e-10,-50900.2,10.1522], Tmin=(10,'K'), Tmax=(323.731,'K')),
            NASAPolynomial(coeffs=[4.74679,0.0256648,-1.72548e-05,5.51811e-09,-6.70931e-13,-51061.3,5.08999], Tmin=(323.731,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-423.181,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-F': 1, 'Li-O': 1, 'C-H': 3, 'C-C': 1, 'C-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[4, 8]]) broke during the scan.Significant difference observed between consecutive conformersThe rotor scan has a barrier of 307.48 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
* Invalidated! pivots: [3, 5], dihedral: [2, 3, 5, 7], invalidation reason: Bond ([[4, 8]]) broke during the scan.Bond ([[1, 2]]) broke during the scan.Significant difference observed between consecutive conformersThe rotor scan has a barrier of 329.62 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 1, optical isomers: 1

Geometry:
Li      1.16307452    1.16061753   -0.00048552
O      -0.77806585    1.12000451    0.00311583
C      -1.36400444    0.02573657    0.00297600
F       2.03357600   -0.22083445   -0.00378227
C      -0.68283567   -1.21584993    0.00015942
H      -2.46338295    0.02666598    0.00516271
H      -1.25604856   -2.13451817    0.00025593
H       0.41462532   -1.21329986   -0.00195690
""",
)

entry(
    index = 92,
    label = "O=[C]OCC[F]O[Li]",
    molecule =
"""
multiplicity 2
1  C  u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C  u0 p0 c0 {1,S} {4,S} {6,S} {9,S}
3  O  u0 p2 c0 {1,S} {5,S}
4  O  u0 p2 c0 {2,S} {10,S}
5  C  u1 p0 c0 {3,S} {11,D}
6  F  u0 p3 c0 {2,S}
7  H  u0 p0 c0 {1,S}
8  H  u0 p0 c0 {1,S}
9  H  u0 p0 c0 {2,S}
10 Li u0 p0 c0 {4,S}
11 O  u0 p2 c0 {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.56527,0.0394827,-2.051e-06,-3.96724e-08,2.51005e-11,-79687.7,13.2991], Tmin=(10,'K'), Tmax=(712.829,'K')),
            NASAPolynomial(coeffs=[6.82486,0.0351277,-2.22125e-05,6.60994e-09,-7.50274e-13,-80506.5,-3.80665], Tmin=(712.829,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-662.607,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'Li-O': 1, 'C-O': 3, 'C-F': 1, 'C-H': 3, 'C=O': 1, 'C-C': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for O=[C]OCC[F]O[Li] exists which is 10.15 kJ/mol lower.Another conformer for O=[C]OCC[F]O[Li] exists which is 10.15 kJ/mol lower. But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Bond ([[5, 6]]) broke during the scan.Bond ([[2, 8]]) broke during the scan.Significant difference observed between consecutive conformersBond ([[7, 8]]) broke during the scan.Bond ([[5, 7]]) broke during the scan.Could not read energies
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: Bond ([[2, 8]]) broke during the scan.Bond ([[7, 8]]) broke during the scan.Bond ([[5, 11]]) broke during the scan.Significant difference observed between consecutive conformersBond ([[5, 6]]) broke during the scan.Bond ([[2, 3]]) broke during the scan.Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformersCould not read energies
* Invalidated! pivots: [5, 7], dihedral: [4, 5, 7, 8], invalidation reason: Bond ([[5, 6]]) broke during the scan.Bond ([[2, 8]]) broke during the scan.Significant difference observed between consecutive conformersCould not read energies


External symmetry: 1, optical isomers: 2

Geometry:
O       2.42454753   -0.33008430    0.08330857
C       1.41228028    0.24132915    0.40141353
O       0.80022468    1.20299811   -0.24328016
C      -0.61196460    1.19888515    0.03645516
C      -1.17761899   -0.17898879   -0.39118297
F      -2.35130847   -0.31605676    0.38409169
O      -0.31096575   -1.14395523   -0.16316164
Li      1.19161994   -1.94836735   -0.05799879
H      -0.77799148    1.33123973    1.10605962
H      -1.03287435    2.03092698   -0.52146681
H      -1.54557836   -0.15687433   -1.42875612
""",
)

entry(
    index = 93,
    label = "[Li]OCC[CH2]",
    molecule =
"""
multiplicity 2
1  C  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C  u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C  u1 p0 c0 {1,S} {9,S} {10,S}
4  O  u0 p2 c0 {2,S} {11,S}
5  H  u0 p0 c0 {1,S}
6  H  u0 p0 c0 {1,S}
7  H  u0 p0 c0 {2,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {3,S}
10 H  u0 p0 c0 {3,S}
11 Li u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61574,0.0415593,-0.000129687,3.44444e-07,-3.13961e-10,-7920.44,13.7758], Tmin=(10,'K'), Tmax=(395.786,'K')),
            NASAPolynomial(coeffs=[1.50019,0.038176,-2.30109e-05,6.66906e-09,-7.46446e-13,-7559.02,24.4715], Tmin=(395.786,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-65.8684,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (249.434,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'Li-O': 1, 'C-H': 6, 'C-C': 2, 'C-O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 0.00 kJ/mol (set as a FreeRotor)
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Another conformer for [Li]OCC[CH2] exists which is 1.59 kJ/mol lower.Another conformer for [Li]OCC[CH2] exists which is 1.59 kJ/mol lower. But unable to propose troubleshooting methods.
pivots: [4, 5], dihedral: [3, 4, 5, 10], rotor symmetry: 1, max scan energy: 1.34 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
Li      2.44330720   -1.20177578   -0.33480474
O       1.34178395   -0.10294140    0.01504105
C       0.36685167    0.82205339    0.27217464
C      -0.98274243    0.44537800   -0.35148798
C      -1.53693661   -0.82558912    0.17226500
H       0.21003804    0.95064089    1.35909951
H       0.64378915    1.81963291   -0.11279275
H      -0.83479049    0.37463162   -1.44173117
H      -1.70217702    1.26241432   -0.20474164
H      -0.89381799   -1.52573985    0.68972020
H      -2.56801700   -1.10675770   -0.00207906
""",
)

entry(
    index = 94,
    label = "[Li]OCCCC[CH2]",
    molecule =
"""
multiplicity 2
1  O  u0 p2 c0 {5,S} {7,S}
2  C  u0 p0 c0 {3,S} {4,S} {10,S} {11,S}
3  C  u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
4  C  u0 p0 c0 {2,S} {6,S} {12,S} {13,S}
5  C  u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
6  C  u1 p0 c0 {4,S} {16,S} {17,S}
7  Li u0 p0 c0 {1,S}
8  H  u0 p0 c0 {3,S}
9  H  u0 p0 c0 {3,S}
10 H  u0 p0 c0 {2,S}
11 H  u0 p0 c0 {2,S}
12 H  u0 p0 c0 {4,S}
13 H  u0 p0 c0 {4,S}
14 H  u0 p0 c0 {5,S}
15 H  u0 p0 c0 {5,S}
16 H  u0 p0 c0 {6,S}
17 H  u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80249,0.0124438,0.000246174,-5.25033e-07,3.38854e-10,-13785.7,14.2583], Tmin=(10,'K'), Tmax=(507.792,'K')),
            NASAPolynomial(coeffs=[0.885816,0.074302,-5.14112e-05,1.6454e-08,-1.97521e-12,-13990.7,21.4169], Tmin=(507.792,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-114.678,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (394.937,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-C': 4, 'Li-O': 1, 'C-H': 10, 'C-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason:
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 58.00 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 3 4 5 13 F
D 3 4 5 6 F
D 11 4 5 6 F
D 12 5 6 14 F
A 1 2 3 F
D 1 2 3 4 F
D 10 4 5 12 F
D 15 6 7 17 F
D 4 5 6 15 F
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 54.11 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 6 7 17 16 F
D 8 3 4 10 F
A 1 2 3 F
D 1 2 3 4 F
D 15 6 7 17 F
D 4 5 6 15 F
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 7], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformersCould not read energies
pivots: [6, 7], dihedral: [5, 6, 7, 16], rotor symmetry: 1, max scan energy: 24.22 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 1 2 3 F
D 6 7 16 17 F
D 1 2 3 4 F
D 3 4 5 13 F


External symmetry: 1, optical isomers: 2

Geometry:
Li     -0.15055274   -2.31920966   -0.22631093
O      -1.26334673   -1.20539686    0.18370793
C      -1.68851794    0.09455695    0.20764954
C      -0.76418431    1.03318613   -0.57998569
C       0.56743112    1.36685673    0.09673089
C       1.40569015    0.18835341    0.59759253
C       1.80621840   -0.79889846   -0.43945528
H      -2.70394769    0.19679657   -0.21719216
H      -1.76687693    0.48350650    1.24334960
H      -1.28045775    1.98000104   -0.77630570
H      -0.59065054    0.56985472   -1.55862607
H       1.17916291    1.96199713   -0.59115349
H       0.36782071    2.01374539    0.95700521
H       0.87132998   -0.32336339    1.40585855
H       2.32012860    0.58439206    1.06611804
H       2.48522071   -1.60745368   -0.17800741
H       1.70916843   -0.56577375   -1.49473404
""",
)

entry(
    index = 95,
    label = "[Li]OCCCCC[CH2]",
    molecule =
"""
multiplicity 2
1  O  u0 p2 c0 {6,S} {8,S}
2  C  u0 p0 c0 {3,S} {4,S} {11,S} {12,S}
3  C  u0 p0 c0 {2,S} {5,S} {13,S} {14,S}
4  C  u0 p0 c0 {2,S} {6,S} {9,S} {10,S}
5  C  u0 p0 c0 {3,S} {7,S} {15,S} {16,S}
6  C  u0 p0 c0 {1,S} {4,S} {17,S} {18,S}
7  C  u1 p0 c0 {5,S} {19,S} {20,S}
8  Li u0 p0 c0 {1,S}
9  H  u0 p0 c0 {4,S}
10 H  u0 p0 c0 {4,S}
11 H  u0 p0 c0 {2,S}
12 H  u0 p0 c0 {2,S}
13 H  u0 p0 c0 {3,S}
14 H  u0 p0 c0 {3,S}
15 H  u0 p0 c0 {5,S}
16 H  u0 p0 c0 {5,S}
17 H  u0 p0 c0 {6,S}
18 H  u0 p0 c0 {6,S}
19 H  u0 p0 c0 {7,S}
20 H  u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.75174,0.127161,-0.000430466,9.00425e-07,-6.83135e-10,-16500,16.0112], Tmin=(10,'K'), Tmax=(429.265,'K')),
            NASAPolynomial(coeffs=[3.64193,0.0669991,-3.89966e-05,1.09807e-08,-1.20109e-12,-16098.5,18.0355], Tmin=(429.265,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-137.218,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (461.453,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-C': 5, 'C-H': 12, 'C-O': 1, 'Li-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 22.05 kJ/mol
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 23.82 kJ/mol
pivots: [5, 6], dihedral: [4, 5, 6, 7], rotor symmetry: 1, max scan energy: 23.52 kJ/mol
pivots: [6, 7], dihedral: [5, 6, 7, 8], rotor symmetry: 1, max scan energy: 22.00 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 6 7 8 19 F
pivots: [7, 8], dihedral: [6, 7, 8, 19], rotor symmetry: 1, max scan energy: 0.60 kJ/mol (set as a FreeRotor)


External symmetry: 1, optical isomers: 2

Geometry:
Li      4.80455328   -1.00451361   -0.00659419
O       3.47259062   -0.13096403    0.00469097
C       2.31044992    0.59254306    0.01477914
C       1.06201976   -0.28906282   -0.00431183
C      -0.24037327    0.50002056    0.00823461
C      -1.48530648   -0.37773173   -0.01341922
C      -2.78792823    0.41604851    0.00421055
C      -4.00938108   -0.42605887   -0.00388082
H       2.25345233    1.27620521   -0.85351245
H       2.24924627    1.24439623    0.90692041
H       1.10449408   -0.92672417   -0.89510467
H       1.10123144   -0.95984039    0.86202244
H      -0.26353946    1.17786948   -0.85372386
H      -0.26843124    1.14161169    0.89738887
H      -1.46782574   -1.05500444    0.84815952
H      -1.46652924   -1.01595612   -0.90376667
H      -2.79492688    1.07245345    0.88906993
H      -2.80807592    1.10771658   -0.84955044
H      -3.95142080   -1.49479654    0.16114714
H      -4.99087504    0.01816096   -0.10827383
""",
)

entry(
    index = 96,
    label = "[Li]NCC[CH2]",
    molecule =
"""
multiplicity 2
1  N  u0 p1 c0 {2,S} {5,S} {10,S}
2  C  u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3  C  u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  C  u1 p0 c0 {3,S} {11,S} {12,S}
5  Li u0 p0 c0 {1,S}
6  H  u0 p0 c0 {2,S}
7  H  u0 p0 c0 {2,S}
8  H  u0 p0 c0 {3,S}
9  H  u0 p0 c0 {3,S}
10 H  u0 p0 c0 {1,S}
11 H  u0 p0 c0 {4,S}
12 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9438,0.00363095,0.000164015,-3.21935e-07,2.03491e-10,22168.9,11.245], Tmin=(10,'K'), Tmax=(408.105,'K')),
            NASAPolynomial(coeffs=[-1.7392,0.0593373,-4.07532e-05,1.25983e-08,-1.4583e-12,22632.7,33.5684], Tmin=(408.105,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (184.31,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (270.22,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'Li-N': 1, 'C-H': 6, 'H-N': 1, 'C-C': 2, 'C-N': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 43.06 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 1 2 3 F
A 1 2 6 F
D 6 1 2 3 F
D 3 4 5 12 F
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 51.30 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 4 5 12 11 F
A 1 2 3 F
A 1 2 6 F
D 1 2 3 4 F
D 3 4 5 12 F
pivots: [4, 5], dihedral: [3, 4, 5, 11], rotor symmetry: 1, max scan energy: 34.22 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 1 2 3 F
A 1 2 6 F
D 4 5 11 12 F
D 1 2 3 4 F
D 2 3 4 10 F


External symmetry: 1, optical isomers: 2

Geometry:
Li     -0.37860140   -1.86290000   -0.40527788
N      -1.38982359   -0.46185315   -0.01627942
C      -0.68569426    0.77791805    0.18963996
C       0.73033656    0.64515062   -0.37019965
C       1.49259587   -0.45157667    0.28565807
H      -2.35945586   -0.34203999    0.24210802
H      -0.57971275    1.05858245    1.25729157
H      -1.16354790    1.64612312   -0.29525585
H       0.67828099    0.48433126   -1.45528501
H       1.27894176    1.59235832   -0.23835649
H       1.38780398   -0.58828090    1.35805437
H       2.39399073   -0.85225118   -0.16996233
""",
)

entry(
    index = 97,
    label = "[Li]NCCC[CH2]",
    molecule =
"""
multiplicity 2
1  N  u0 p1 c0 {3,S} {6,S} {13,S}
2  C  u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
3  C  u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
4  C  u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
5  C  u1 p0 c0 {4,S} {14,S} {15,S}
6  Li u0 p0 c0 {1,S}
7  H  u0 p0 c0 {2,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {3,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {4,S}
12 H  u0 p0 c0 {4,S}
13 H  u0 p0 c0 {1,S}
14 H  u0 p0 c0 {5,S}
15 H  u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71756,0.0250431,0.000110549,-2.92723e-07,2.36861e-10,20632.3,11.4601], Tmin=(10,'K'), Tmax=(317.921,'K')),
            NASAPolynomial(coeffs=[1.28629,0.0556327,-3.37775e-05,9.92202e-09,-1.12682e-12,20786.9,20.4034], Tmin=(317.921,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (171.539,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (357.522,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-C': 3, 'Li-N': 1, 'C-H': 8, 'H-N': 1, 'C-N': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 6]]) broke during the scan.Bond ([[1, 6]]) broke during the scan. But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Bond ([[1, 6]]) broke during the scan.Bond ([[1, 2]]) broke during the scan.Bond ([[1, 6]]) broke during the scan. But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: Bond ([[1, 6]]) broke during the scan.Bond ([[1, 2]]) broke during the scan.Bond ([[1, 6]]) broke during the scan. But unable to propose troubleshooting methods.
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 14], invalidation reason: Another conformer for [Li]NCCC[CH2] exists which is 2.77 kJ/mol lower.Bond ([[1, 6]]) broke during the scan.Another conformer for [Li]NCCC[CH2] exists which is 2.77 kJ/mol lower. But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
Li     -0.04288009   -1.85348713   -0.71120594
N      -1.41266345   -0.83279675   -0.22950882
C      -1.21924621    0.43755679    0.42797934
C      -0.04183477    1.21586776   -0.16694584
C       1.20285281    0.36526435   -0.44770053
C       1.54927192   -0.63534673    0.60004898
H      -2.36323415   -1.13488837   -0.06158385
H      -2.09881627    1.09556742    0.35730982
H      -1.03537727    0.33757241    1.51811070
H      -0.35152393    1.67146796   -1.11178296
H       0.22833856    2.03211307    0.51109163
H       1.08223440   -0.12621904   -1.43131499
H       2.06762384    1.02042506   -0.62371831
H       1.03540624   -0.63046013    1.55267361
H       2.48986705   -1.17430009    0.54187706
""",
)

entry(
    index = 98,
    label = "[Li]O[S][=O][C]C",
    molecule =
"""
multiplicity 2
1  S  u1 p0 c0 {2,S} {3,D} {4,S} {5,S}
2  O  u0 p2 c0 {1,S} {6,S}
3  O  u0 p2 c0 {1,D}
4  C  u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
5  C  u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
6  Li u0 p0 c0 {2,S}
7  H  u0 p0 c0 {4,S}
8  H  u0 p0 c0 {4,S}
9  H  u0 p0 c0 {4,S}
10 H  u0 p0 c0 {5,S}
11 H  u0 p0 c0 {5,S}
12 H  u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.44078,0.0580181,0.00015115,-1.26331e-06,2.0644e-09,-43950.8,14.1143], Tmin=(10,'K'), Tmax=(251.615,'K')),
            NASAPolynomial(coeffs=[8.03258,0.03617,-2.35274e-05,7.41888e-09,-8.97993e-13,-44343.7,-4.91991], Tmin=(251.615,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-365.397,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'Li-O': 1, 'C-H': 6, 'O=S': 1, 'C-S': 2, 'O-S': 1}
1D rotors:
* Invalidated! pivots: [3, 5], dihedral: [2, 3, 5, 7], invalidation reason: Significant difference observed between consecutive conformersCould not read energies
* Invalidated! pivots: [3, 6], dihedral: [2, 3, 6, 10], invalidation reason: Another conformer for [Li]O[S][=O][C]C exists which is 0.05 kJ/mol lower.Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformersBond ([[1, 6]]) broke during the scan.The rotor scan has a barrier of 72.61 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Could not read energies


External symmetry: 1, optical isomers: 2

Geometry:
Li      1.18091327   -0.30829697   -0.84121264
O       0.19128545    1.08336533   -0.03406052
S      -0.76607289    0.02287916    0.48897041
O      -0.25961070   -1.27234899   -0.12709594
C      -2.25094251    0.34512170   -0.46698017
C       3.47402340    0.09417506   -0.04030328
H      -2.64044977    1.32251345   -0.18241748
H      -1.98103429    0.33165898   -1.52401334
H      -2.98129011   -0.43349128   -0.24731717
H       3.49723898   -0.84576387    0.49606042
H       4.19947749    0.27551827   -0.82089921
H       2.87896560    0.91466741    0.34447750
""",
)

entry(
    index = 99,
    label = "[Li]OC[=O]",
    molecule =
"""
1 O  u0 p2 c0 {3,S} {4,S}
2 O  u0 p2 c0 {3,D}
3 C  u0 p0 c0 {1,S} {2,D} {5,S}
4 Li u0 p0 c0 {1,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96476,0.00222446,4.9425e-05,-1.03857e-07,6.68737e-11,-59837.8,6.7387], Tmin=(10,'K'), Tmax=(501.15,'K')),
            NASAPolynomial(coeffs=[3.21811,0.0151586,-1.01645e-05,3.18424e-09,-3.77695e-13,-59850.5,8.95115], Tmin=(501.15,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-497.529,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 1, 'Li-O': 1, 'C=O': 1, 'C-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 4]]) broke during the scan.Bond ([[1, 2]]) broke during the scan.The rotor scan has a barrier of 505.04 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 2, optical isomers: 1

Geometry:
Li      0.00025902   -1.54247119    0.00000000
O      -1.10529344   -0.02948707    0.00000000
C      -0.00012241    0.57041887    0.00000000
O       1.10525781   -0.02909878    0.00000000
H      -0.00034105    1.67443662    0.00000000
""",
)

entry(
    index = 100,
    label = "[Li]OC1OCCO1",
    molecule =
"""
1  O  u0 p2 c0 {4,S} {6,S}
2  O  u0 p2 c0 {5,S} {6,S}
3  O  u0 p2 c0 {6,S} {7,S}
4  C  u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
5  C  u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
6  C  u0 p0 c0 {1,S} {2,S} {3,S} {12,S}
7  Li u0 p0 c0 {3,S}
8  H  u0 p0 c0 {4,S}
9  H  u0 p0 c0 {4,S}
10 H  u0 p0 c0 {5,S}
11 H  u0 p0 c0 {5,S}
12 H  u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91129,0.00556233,0.000151798,-3.05964e-07,1.92283e-10,-71002.4,11.6055], Tmin=(10,'K'), Tmax=(498.121,'K')),
            NASAPolynomial(coeffs=[0.592316,0.0494619,-3.2335e-05,9.98508e-09,-1.17397e-12,-70885.7,23.1568], Tmin=(498.121,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-590.373,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-O': 5, 'Li-O': 1, 'C-H': 5, 'C-C': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for [Li]OC1OCCO1 exists which is 3.61 kJ/mol lower.Bond ([[3, 7]]) broke during the scan.Bond ([[1, 7]]) broke during the scan.Bond ([[3, 4]]) broke during the scan.Another conformer for [Li]OC1OCCO1 exists which is 3.61 kJ/mol lower. But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
Li      1.52332333   -1.35783346   -0.79274127
O       1.74491772    0.32416913   -0.35538829
C       0.77203128    0.32731816    0.49020672
O      -0.30174200    1.22054453    0.26857579
C      -1.27357127    0.58297312   -0.52099370
C      -1.30235801   -0.82006906    0.06478985
O       0.05283414   -1.06334769    0.37529971
H       1.03707195    0.41671072    1.55363260
H      -2.21652715    1.11942255   -0.41875960
H      -0.98396027    0.56981725   -1.58042992
H      -1.91005829   -0.85237795    0.97523525
H      -1.67205480   -1.57346283   -0.63585105
""",
)

entry(
    index = 101,
    label = "C",
    molecule =
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.04124,-0.00245745,1.10814e-05,3.91058e-09,-9.35922e-12,-9994.97,-0.425359], Tmin=(10,'K'), Tmax=(619.895,'K')),
            NASAPolynomial(coeffs=[0.663112,0.0116704,-4.54442e-06,7.5489e-10,-3.66003e-14,-9428.78,15.4454], Tmin=(619.895,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-83.0877,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 4}

External symmetry: 12, optical isomers: 1

Geometry:
C       0.00000000    0.00000000    0.00000000
H       0.62870862    0.62870862    0.62870862
H      -0.62870862   -0.62870862    0.62870862
H      -0.62870862    0.62870862   -0.62870862
H       0.62870862   -0.62870862   -0.62870862
""",
)

entry(
    index = 102,
    label = "CF",
    molecule =
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.08661,-0.00497302,3.04898e-05,-2.98028e-08,9.43571e-12,-29517.5,3.85517], Tmin=(10,'K'), Tmax=(967.865,'K')),
            NASAPolynomial(coeffs=[0.719339,0.0141806,-7.31137e-06,1.8256e-09,-1.78034e-13,-29110.9,18.7231], Tmin=(967.865,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-245.399,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 3, 'C-F': 1}

External symmetry: 3, optical isomers: 1

Geometry:
C       0.00000000    0.00000000    0.63094005
F       0.00000000    0.00000000   -0.74935730
H       1.03202425    0.00000000    0.98597153
H      -0.51601212    0.89375921    0.98597153
H      -0.51601212   -0.89375921    0.98597153
""",
)

entry(
    index = 103,
    label = "CCl",
    molecule =
"""
1 Cl u0 p3 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.07315,-0.00495697,3.80808e-05,-4.55749e-08,1.79783e-11,-11099.5,5.07436], Tmin=(10,'K'), Tmax=(756.145,'K')),
            NASAPolynomial(coeffs=[1.36674,0.0136388,-7.29667e-06,1.91652e-09,-1.97851e-13,-10812.6,16.5659], Tmin=(756.145,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-92.2711,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 3, 'C-Cl': 1}

External symmetry: 3, optical isomers: 1

Geometry:
C       0.00000000    0.00000000    1.12067701
Cl      0.00000000    0.00000000   -0.65479116
H       1.02930668    0.00000000    1.46847645
H      -0.51465334   -0.89140574    1.46847645
H      -0.51465334    0.89140574    1.46847645
""",
)

entry(
    index = 104,
    label = "O=C=O",
    molecule =
"""
1 O u0 p2 c0 {3,D}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,D} {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53618,-0.00349639,3.85354e-05,-6.90829e-08,4.05639e-11,-48507.4,5.38073], Tmin=(10,'K'), Tmax=(535.548,'K')),
            NASAPolynomial(coeffs=[2.7554,0.00713403,-4.67975e-06,1.44412e-09,-1.69344e-13,-48492.5,8.01749], Tmin=(535.548,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-403.316,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (62.3585,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C=O': 2}

External symmetry: 2, optical isomers: 1

Geometry:
O       0.00000000    0.00000000   -1.15628105
C       0.00000000    0.00000000    0.00000000
O       0.00000000    0.00000000    1.15628105
""",
)

entry(
    index = 105,
    label = "[Li]OCO",
    molecule =
"""
1 O  u0 p2 c0 {3,S} {4,S}
2 O  u0 p2 c0 {3,S} {7,S}
3 C  u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
4 Li u0 p0 c0 {1,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90799,0.00741544,7.61269e-05,-2.07885e-07,1.72674e-10,-53302.6,8.55141], Tmin=(10,'K'), Tmax=(389.343,'K')),
            NASAPolynomial(coeffs=[3.31581,0.0222007,-1.43588e-05,4.45385e-09,-5.28639e-13,-53322.4,10.0028], Tmin=(389.343,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-443.178,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-O': 2, 'C-H': 2, 'H-O': 1, 'Li-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 4]]) broke during the scan.The rotor scan has a barrier of 203.72 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 7], invalidation reason: Bond ([[1, 4]]) broke during the scan.The rotor scan has a barrier of 130.02 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 1, optical isomers: 2

Geometry:
Li     -0.17635125   -1.55210447    0.02881330
O      -1.17256044   -0.11473417    0.00720275
C      -0.14328864    0.69757968   -0.00251405
O       1.11622510   -0.19267435   -0.05081489
H      -0.04893121    1.33911932   -0.89702753
H      -0.00456425    1.31163500    0.90942333
H       1.88194102    0.26781907    0.29074813
""",
)

entry(
    index = 106,
    label = "O=S[=O][C]CC[CH2]",
    molecule =
"""
multiplicity 2
1  S u0 p0 c0 {2,D} {3,D} {4,S} {6,S}
2  O u0 p2 c0 {1,D}
3  O u0 p2 c0 {1,D}
4  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {4,S} {7,S} {10,S} {11,S}
6  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
7  C u1 p0 c0 {5,S} {15,S} {16,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.22642,0.0698165,-0.000101594,1.22147e-07,-6.62699e-11,-28695.2,15.2993], Tmin=(10,'K'), Tmax=(515.783,'K')),
            NASAPolynomial(coeffs=[4.91842,0.0510175,-3.04127e-05,8.80302e-09,-9.88502e-13,-28794.3,8.98866], Tmin=(515.783,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-238.633,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (365.837,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 9, 'O=S': 2, 'C-C': 2, 'C-S': 2}
1D rotors:
pivots: [2, 4], dihedral: [1, 2, 4, 8], rotor symmetry: 3, max scan energy: 8.50 kJ/mol
pivots: [2, 5], dihedral: [1, 2, 5, 6], rotor symmetry: 1, max scan energy: 16.73 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 5 6 7 16 F
pivots: [5, 6], dihedral: [2, 5, 6, 7], rotor symmetry: 1, max scan energy: 26.65 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 5 6 7 16 F
pivots: [6, 7], dihedral: [5, 6, 7, 15], rotor symmetry: 1, max scan energy: 1.05 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       0.97181462   -1.01270534    1.13663948
S       0.83315689   -0.16582387   -0.01442540
O       0.95841772   -0.72356173   -1.33168395
C       2.00880156    1.14991895    0.13296778
C      -0.74080489    0.66299890    0.09111838
C      -1.88335886   -0.34609417   -0.00345906
C      -3.21281070    0.31249091    0.02337244
H       2.98789563    0.67684404    0.06739918
H       1.89466821    1.63692058    1.09939250
H       1.87730473    1.85191917   -0.68804298
H      -0.76128648    1.19784400    1.04217729
H      -0.77780726    1.38224274   -0.72975318
H      -1.79545493   -1.07077928    0.80950442
H      -1.76002736   -0.92133045   -0.93265255
H      -3.36195946    1.27898979   -0.44180016
H      -4.08482943   -0.22438927    0.36983408
""",
)

entry(
    index = 107,
    label = "[Li]OS[=O][=C]C",
    molecule =
"""
1  S  u0 p0 c0 {2,S} {3,D} {4,S} {5,D}
2  O  u0 p2 c0 {1,S} {6,S}
3  O  u0 p2 c0 {1,D}
4  C  u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
5  C  u0 p0 c0 {1,D} {10,S} {11,S}
6  Li u0 p0 c0 {2,S}
7  H  u0 p0 c0 {4,S}
8  H  u0 p0 c0 {4,S}
9  H  u0 p0 c0 {4,S}
10 H  u0 p0 c0 {5,S}
11 H  u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80505,0.0128278,0.000165282,-4.14033e-07,2.9967e-10,-45084.5,10.994], Tmin=(10,'K'), Tmax=(485.209,'K')),
            NASAPolynomial(coeffs=[5.6199,0.0359454,-2.3905e-05,7.64991e-09,-9.3595e-13,-45708.8,-1.06823], Tmin=(485.209,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-374.894,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (253.591,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 5, 'C=S': 1, 'O=S': 1, 'C-S': 1, 'O-S': 1, 'Li-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 2]]) broke during the scan.Significant difference observed between consecutive conformersCould not read energies
pivots: [3, 6], dihedral: [2, 3, 6, 9], rotor symmetry: 3, max scan energy: 10.99 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
Li      2.25806849    0.62481804   -0.08560287
O       0.53046080    1.22720382   -0.50702637
S      -0.06009306   -0.07343631   -0.09665021
O      -0.34529265   -1.00012280   -1.16070082
C       1.04728701   -0.70445274    1.00937130
C      -1.61954264    0.37976187    0.62486094
H       0.93252989   -1.77755448    1.12157325
H       0.98101083   -0.17194150    1.96056968
H      -2.21847959    0.84513313   -0.15673779
H      -1.44792078    1.07970039    1.44035422
H      -2.10099664   -0.52691298    0.98608412
""",
)

entry(
    index = 108,
    label = "O=CCC[CH2]",
    molecule =
"""
multiplicity 2
1  O u0 p2 c0 {5,D}
2  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  C u1 p0 c0 {3,S} {11,S} {12,S}
5  C u0 p0 c0 {1,D} {2,S} {10,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.31269,0.063611,-0.000196009,3.62718e-07,-2.38927e-10,-2505.81,12.4365], Tmin=(10,'K'), Tmax=(506.576,'K')),
            NASAPolynomial(coeffs=[2.69344,0.0362877,-1.97186e-05,5.18759e-09,-5.33409e-13,-2029.75,19.0825], Tmin=(506.576,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-20.8508,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (270.22,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 7, 'C-C': 3, 'C=O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 8.41 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 30.01 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 1 2 3 8 F
D 10 4 5 12 F
pivots: [4, 5], dihedral: [3, 4, 5, 11], rotor symmetry: 1, max scan energy: 1.02 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.93227119   -0.71778803   -0.04004807
C       1.49485126    0.39893740    0.01067195
C       0.03429381    0.74905858    0.03647934
C      -0.90202006   -0.44889987    0.00482523
C      -2.33638023   -0.07154797   -0.00557067
H       2.18460359    1.26900301    0.04275479
H      -0.13532296    1.36556578    0.92754663
H      -0.14928965    1.42113921   -0.81141098
H      -0.65913806   -1.05973969   -0.87719415
H      -0.68532144   -1.10540729    0.85345063
H      -2.65986221    0.89386132   -0.37482299
H      -3.09830329   -0.80184206    0.23109453
""",
)

entry(
    index = 109,
    label = "CCOC=C",
    molecule =
"""
1  O u0 p2 c0 {2,S} {4,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {5,D} {11,S}
5  C u0 p0 c0 {4,D} {12,S} {13,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85669,0.0104981,0.00018346,-4.93763e-07,4.0892e-10,-19061,9.53373], Tmin=(10,'K'), Tmax=(399.695,'K')),
            NASAPolynomial(coeffs=[3.24466,0.0412552,-2.4408e-05,7.13397e-09,-8.18336e-13,-19208.9,9.46379], Tmin=(399.695,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-158.477,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (295.164,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 8, 'C-O': 2, 'C-C': 1, 'C=C': 1}
1D rotors:
pivots: [1, 2], dihedral: [6, 1, 2, 3], rotor symmetry: 3, max scan energy: 12.24 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 44.29 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 2 3 4 11 F
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 24.47 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       2.23285873    0.04643928   -0.00000353
C       0.78050811    0.45883064    0.00000871
O      -0.01231769   -0.71546580    0.00001145
C      -1.34807768   -0.55387067   -0.00000757
C      -2.03849809    0.58151550   -0.00000048
H       2.46448311   -0.54794682   -0.88453361
H       2.46456227   -0.54779011    0.88461156
H       2.87177527    0.93095069   -0.00011655
H       0.53994523    1.05894879    0.88573184
H       0.53993065    1.05894163   -0.88571621
H      -1.84121613   -1.51958279   -0.00003613
H      -3.11768248    0.53085677   -0.00001180
H      -1.58105449    1.56066760    0.00001336
""",
)

entry(
    index = 110,
    label = "CCOC[=O]OCC",
    molecule =
"""
1  O u0 p2 c0 {4,S} {8,S}
2  O u0 p2 c0 {5,S} {8,S}
3  O u0 p2 c0 {8,D}
4  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
5  C u0 p0 c0 {2,S} {7,S} {11,S} {12,S}
6  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
7  C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
8  C u0 p0 c0 {1,S} {2,S} {3,D}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.98507,0.116004,-0.000565628,1.60321e-06,-1.54001e-09,-80074.7,12.4393], Tmin=(10,'K'), Tmax=(360.829,'K')),
            NASAPolynomial(coeffs=[-0.604678,0.07358,-4.74757e-05,1.43834e-08,-1.65882e-12,-79280.4,33.5153], Tmin=(360.829,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-665.838,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (407.409,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 10, 'C-O': 4, 'C-C': 2, 'C=O': 1}
1D rotors:
pivots: [1, 2], dihedral: [9, 1, 2, 3], rotor symmetry: 3, max scan energy: 12.90 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 29.19 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 38.08 kJ/mol
pivots: [4, 6], dihedral: [3, 4, 6, 7], rotor symmetry: 1, max scan energy: 38.09 kJ/mol
pivots: [6, 7], dihedral: [4, 6, 7, 8], rotor symmetry: 1, max scan energy: 29.19 kJ/mol
pivots: [7, 8], dihedral: [6, 7, 8, 16], rotor symmetry: 3, max scan energy: 12.90 kJ/mol


External symmetry: 2, optical isomers: 1

Geometry:
C       3.42389371   -0.76047227    0.00048190
C       2.33440924    0.28266322   -0.00060094
O       1.07688832   -0.40793623   -0.00013632
C       0.00023741    0.37056100    0.00004126
O       0.00031302    1.57285264    0.00006425
O      -1.07671115   -0.40779129    0.00019647
C      -2.33442204    0.28259163    0.00078611
C      -3.42433508   -0.76025599   -0.00045708
H       3.35577400   -1.39481542   -0.88391509
H       4.39919476   -0.27140901   -0.00002455
H       3.35577961   -1.39296321    0.88620682
H       2.38429481    0.92318753   -0.88332032
H       2.38411207    0.92483567    0.88091721
H      -2.38457484    0.92296684    0.88360547
H      -2.38441606    0.92490935   -0.88061488
H      -3.35690727   -1.39477537    0.88386799
H      -3.35686540   -1.39268098   -0.88628101
H      -4.39937486   -0.27060712    0.00008026
""",
)

entry(
    index = 111,
    label = "[Li]OCO[Li]",
    molecule =
"""
1 O  u0 p2 c0 {3,S} {4,S}
2 O  u0 p2 c0 {3,S} {5,S}
3 C  u0 p0 c0 {1,S} {2,S} {6,S} {7,S}
4 Li u0 p0 c0 {1,S}
5 Li u0 p0 c0 {2,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90624,0.00594272,9.20536e-05,-2.09734e-07,1.4065e-10,-55230.4,7.47724], Tmin=(10,'K'), Tmax=(509.965,'K')),
            NASAPolynomial(coeffs=[4.05519,0.0238058,-1.64671e-05,5.31267e-09,-6.46619e-13,-55493.1,4.4326], Tmin=(509.965,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-459.238,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 2, 'C-O': 2, 'Li-O': 2}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 3]]) broke during the scan.Significant difference observed between consecutive conformersCould not read energies
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Bond ([[3, 5]]) broke during the scan.Bond ([[3, 5]]) broke during the scan. But unable to propose troubleshooting methods.


External symmetry: 2, optical isomers: 1

Geometry:
Li      0.00107985    0.79281690    1.32154581
O       1.12713706    0.12203045    0.00774572
C      -0.00002945   -0.72355415   -0.04012199
O      -1.12710980    0.12217864    0.00947152
Li     -0.00085915    0.93720053   -1.22017199
H      -0.00096096   -1.35041594   -0.95978103
H       0.00066184   -1.45252493    0.80083185
""",
)

entry(
    index = 112,
    label = "[Li]OC[=O][O]",
    molecule =
"""
multiplicity 2
1 O  u0 p2 c0 {4,S} {5,S}
2 O  u1 p2 c0 {4,S}
3 O  u0 p2 c0 {4,D}
4 C  u0 p0 c0 {1,S} {2,S} {3,D}
5 Li u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88587,0.00845464,5.3769e-05,-1.45849e-07,1.07154e-10,-60584.6,8.81159], Tmin=(10,'K'), Tmax=(489.413,'K')),
            NASAPolynomial(coeffs=[4.87043,0.0150355,-1.12335e-05,3.76617e-09,-4.6711e-13,-60856.1,2.97542], Tmin=(489.413,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-503.747,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-O': 2, 'Li-O': 1, 'C=O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 4]]) broke during the scan.Bond ([[1, 2]]) broke during the scan.Bond ([[3, 5]]) broke during the scan.The rotor scan has a barrier of 677.64 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 2, optical isomers: 1

Geometry:
Li      1.96391153    0.00137053   -0.00011630
O       0.42364928    1.11045210    0.00004513
C      -0.16274234   -0.00019370    0.00000825
O       0.42511647   -1.11001816    0.00004507
O      -1.46356541   -0.00086257   -0.00003671
""",
)

entry(
    index = 113,
    label = "[Li]OC",
    molecule =
"""
1 O  u0 p2 c0 {2,S} {3,S}
2 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
3 Li u0 p0 c0 {1,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81392,0.0189919,-7.01616e-05,1.71307e-07,-1.36293e-10,-24814.9,4.91423], Tmin=(10,'K'), Tmax=(458.721,'K')),
            NASAPolynomial(coeffs=[2.03098,0.017522,-9.71089e-06,2.58372e-09,-2.67078e-13,-24472.3,14.0779], Tmin=(458.721,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-206.323,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'Li-O': 1, 'C-H': 3, 'C-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: not a torsional mode (angles = 179.97, 112.54 degrees)


External symmetry: 3, optical isomers: 1

Geometry:
Li     -2.03074713   -0.00000366    0.00011672
O      -0.44147261   -0.00013270    0.00004692
C       0.92840807    0.00003223    0.00076016
H       1.35096098    0.22197901    0.99618208
H       1.35153283    0.75118522   -0.68878838
H       1.35166500   -0.97255448   -0.30519035
""",
)

entry(
    index = 114,
    label = "[Li]NC",
    molecule =
"""
1 N  u0 p1 c0 {2,S} {3,S} {7,S}
2 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
3 Li u0 p0 c0 {1,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75569,0.0250946,-8.3018e-05,1.86333e-07,-1.4379e-10,6985.38,7.00171], Tmin=(10,'K'), Tmax=(452.751,'K')),
            NASAPolynomial(coeffs=[2.7145,0.0186738,-9.99698e-06,2.6122e-09,-2.67638e-13,7239.75,12.9677], Tmin=(452.751,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (58.0761,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (153.818,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'Li-N': 1, 'C-H': 3, 'H-N': 1, 'C-N': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 5], rotor symmetry: 1, max scan energy: 7.28 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 4 1 2 3 F
D 2 3 5 7 F
D 4 1 2 3 F
D 2 3 5 6 F


External symmetry: 1, optical isomers: 1

Geometry:
Li      1.96298665   -0.54202406    0.00417884
N       0.44856891    0.32006560   -0.00095947
C      -0.91649696   -0.16298433    0.00006451
H       0.41265082    1.33263920   -0.00544698
H      -1.50254527    0.14130195   -0.88373213
H      -1.50391306    0.14894078    0.88028419
H      -0.93480561   -1.26068913    0.00480503
""",
)

entry(
    index = 115,
    label = "CNC",
    molecule =
"""
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  N u0 p1 c0 {1,S} {2,S} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91549,0.00576178,5.23388e-05,-7.97634e-08,3.8226e-11,-3488.65,7.19048], Tmin=(10,'K'), Tmax=(542.254,'K')),
            NASAPolynomial(coeffs=[0.575718,0.030398,-1.58108e-05,4.02213e-09,-4.02405e-13,-3126.45,21.2589], Tmin=(542.254,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-29.0305,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (224.491,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 6, 'C-N': 2, 'H-N': 1}
1D rotors:
pivots: [1, 2], dihedral: [4, 1, 2, 3], rotor symmetry: 3, max scan energy: 12.64 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 8], rotor symmetry: 3, max scan energy: 12.63 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       1.20718758   -0.22106212    0.01964303
N       0.00001692    0.56243173   -0.14310428
C      -1.20716031   -0.22110365    0.01937884
H       1.27685816   -0.95606836   -0.78645595
H       2.08258492    0.42626016   -0.04870398
H       1.25523307   -0.77040771    0.97416284
H      -0.00006553    1.33350967    0.50918079
H      -1.25528135   -0.77069438    0.97375385
H      -1.27683331   -0.95591031   -0.78690879
H      -2.08255706    0.42623894   -0.04883439
""",
)

entry(
    index = 116,
    label = "CO",
    molecule =
"""
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.00439,-0.00035595,2.3513e-05,-2.48982e-08,8.41094e-12,-25475.1,5.26272], Tmin=(10,'K'), Tmax=(777.588,'K')),
            NASAPolynomial(coeffs=[0.871122,0.0157609,-7.57499e-06,1.75339e-09,-1.57172e-13,-24987.8,19.591], Tmin=(777.588,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-211.81,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (128.874,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 3, 'H-O': 1, 'C-O': 1}
1D rotors:
pivots: [1, 2], dihedral: [3, 1, 2, 6], rotor symmetry: 3, max scan energy: 4.38 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       0.66022152   -0.02031639    0.00040428
O      -0.74405171    0.12208036    0.00188428
H       1.02385563   -0.53947737   -0.89371148
H       1.08339751    0.98364096    0.00566435
H       1.02472557   -0.54923549    0.88842839
H      -1.14185094   -0.74891697   -0.00259765
""",
)

entry(
    index = 117,
    label = "CN",
    molecule =
"""
1 N u0 p1 c0 {2,S} {6,S} {7,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9975,-5.6659e-05,3.32024e-05,-4.01501e-08,1.57181e-11,-3942.74,5.22021], Tmin=(10,'K'), Tmax=(662.817,'K')),
            NASAPolynomial(coeffs=[0.928694,0.018463,-8.70876e-06,2.00432e-09,-1.81565e-13,-3535.93,18.7634], Tmin=(662.817,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-32.7839,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (153.818,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 3, 'C-N': 1, 'H-N': 2}
1D rotors:
pivots: [1, 2], dihedral: [3, 1, 2, 6], rotor symmetry: 3, max scan energy: 8.06 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C      -0.70346604   -0.00021729    0.01737458
N       0.74623417   -0.00059639   -0.12002800
H      -1.07325274    0.00309918    1.05171985
H      -1.11416624   -0.87961864   -0.48158819
H      -1.11426860    0.87588215   -0.48728824
H       1.14965153   -0.81209495    0.32698394
H       1.14970777    0.81317497    0.32278054
""",
)

entry(
    index = 118,
    label = "[Li]CC",
    molecule =
"""
1 C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C  u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 Li u0 p0 c0 {1,S}
4 H  u0 p0 c0 {1,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {2,S}
8 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91528,0.00698009,7.27614e-05,-2.12095e-07,2.06109e-10,11739.2,6.79131], Tmin=(10,'K'), Tmax=(260.286,'K')),
            NASAPolynomial(coeffs=[2.96803,0.0215372,-1.11295e-05,2.77372e-09,-2.69082e-13,11788.5,10.0863], Tmin=(260.286,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (97.5973,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 5, 'C-Li': 1, 'C-C': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 6], rotor symmetry: 3, max scan energy: 9.91 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
Li      2.03518929   -0.74871887    0.00006422
C       0.43464770    0.43791517   -0.00000873
C      -0.95199648   -0.22659637    0.00000238
H       0.49221387    1.11531261    0.86569201
H       0.49224113    1.11520975   -0.86578607
H      -1.09753223   -0.86913052    0.87582088
H      -1.09747493   -0.86932529   -0.87568607
H      -1.78974867    0.48532223   -0.00011267
""",
)

entry(
    index = 119,
    label = "[Li]OC[CH2]",
    molecule =
"""
multiplicity 2
1 O  u0 p2 c0 {2,S} {4,S}
2 C  u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3 C  u1 p0 c0 {2,S} {7,S} {8,S}
4 Li u0 p0 c0 {1,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {3,S}
8 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.66357,0.0354817,-0.000122157,2.85243e-07,-2.364e-10,-4624.46,11.4882], Tmin=(10,'K'), Tmax=(409.176,'K')),
            NASAPolynomial(coeffs=[3.08948,0.0235261,-1.39266e-05,3.97542e-09,-4.39485e-13,-4430.42,15.5419], Tmin=(409.176,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-38.4598,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (174.604,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'Li-O': 1, 'C-H': 4, 'C-C': 1, 'C-O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 0.02 kJ/mol (set as a FreeRotor)
pivots: [3, 4], dihedral: [2, 3, 4, 7], rotor symmetry: 1, max scan energy: 5.98 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 5 2 3 4 F
D 3 4 7 8 F
D 6 2 3 4 F
D 3 4 7 8 F


External symmetry: 1, optical isomers: 2

Geometry:
Li      2.41219006   -0.57927262   -0.05054602
O       0.95053602    0.05360944   -0.00980107
C      -0.31774182    0.56372735    0.00482136
C      -1.39178621   -0.46555953   -0.02688287
H      -0.48788149    1.25920662   -0.84382236
H      -0.48387609    1.20117309    0.90194466
H      -1.14445995   -1.50741690    0.13327253
H      -2.43433328   -0.18110050   -0.11565308
""",
)

entry(
    index = 120,
    label = "[Li]OC[=O]OCCOC[=O]O[Li]",
    molecule =
"""
1  O  u0 p2 c0 {7,S} {9,S}
2  O  u0 p2 c0 {8,S} {10,S}
3  O  u0 p2 c0 {9,S} {11,S}
4  O  u0 p2 c0 {10,S} {12,S}
5  O  u0 p2 c0 {9,D}
6  O  u0 p2 c0 {10,D}
7  C  u0 p0 c0 {1,S} {8,S} {13,S} {14,S}
8  C  u0 p0 c0 {2,S} {7,S} {15,S} {16,S}
9  C  u0 p0 c0 {1,S} {3,S} {5,D}
10 C  u0 p0 c0 {2,S} {4,S} {6,D}
11 Li u0 p0 c0 {3,S}
12 Li u0 p0 c0 {4,S}
13 H  u0 p0 c0 {7,S}
14 H  u0 p0 c0 {7,S}
15 H  u0 p0 c0 {8,S}
16 H  u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.31656,0.0709113,-4.40617e-05,3.80661e-09,4.13375e-12,-182652,14.6442], Tmin=(10,'K'), Tmax=(980.505,'K')),
            NASAPolynomial(coeffs=[13.8742,0.0431962,-2.51528e-05,6.92169e-09,-7.32796e-13,-185461,-39.8463], Tmin=(980.505,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-1518.67,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (382.466,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 4, 'C-C': 1, 'C-O': 8, 'C=O': 1, 'Li-O': 2}
1D rotors:
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 7], invalidation reason:
* Invalidated! pivots: [5, 8], dihedral: [4, 5, 8, 9], invalidation reason: Another conformer for O1C[=O]OC[O[Li]][O[Li]]OCC1 exists which is 1.38 kJ/mol lower.Bond ([[4, 9]]) broke during the scan.Another conformer for O1C[=O]OC[O[Li]][O[Li]]OCC1 exists which is 1.38 kJ/mol lower. But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       1.38426870   -0.69969005    0.57433648
C       1.43738856    0.50416233   -0.08843571
O       1.53832050    1.47696405    0.68223882
O       1.33120562    0.51493012   -1.33018991
C      -1.47017000    0.40713989    0.08073785
O      -1.36766615    0.44530721    1.32206458
Li      0.17650947    1.25844501    1.91315038
O      -1.64032504    1.35670272   -0.70638034
Li     -0.27525656    1.17300511   -1.94344851
O      -1.32573869   -0.79993620   -0.56376361
C      -0.68561476   -1.87076671    0.11939497
C       0.81803676   -1.82254263   -0.08926389
H      -1.08369044   -2.79041003   -0.31276677
H      -0.93312479   -1.83488077    1.18071397
H       1.27484992   -2.70600482    0.35993382
H       1.06424298   -1.79082431   -1.15108393
""",
)

entry(
    index = 121,
    label = "[Li]OCCO[C]=O",
    molecule =
"""
multiplicity 2
1  C  u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C  u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3  O  u0 p2 c0 {1,S} {5,S}
4  O  u0 p2 c0 {2,S} {10,S}
5  C  u1 p0 c0 {3,S} {11,D}
6  H  u0 p0 c0 {2,S}
7  H  u0 p0 c0 {2,S}
8  H  u0 p0 c0 {1,S}
9  H  u0 p0 c0 {1,S}
10 Li u0 p0 c0 {4,S}
11 O  u0 p2 c0 {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.3665,0.0702141,-0.000302182,8.04989e-07,-7.52676e-10,-44897.6,12.0069], Tmin=(10,'K'), Tmax=(361.225,'K')),
            NASAPolynomial(coeffs=[2.51552,0.0418517,-2.74988e-05,8.45943e-09,-9.88262e-13,-44589.6,18.6581], Tmin=(361.225,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-373.327,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (249.434,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'Li-O': 1, 'C-O': 3, 'C-H': 4, 'C=O': 1, 'C-C': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 2, max scan energy: 35.42 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 2 3 4 5 F
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: rotor scan switching back and forth between conformers or trying to switch ot a non-isomorphic conformer invalidating rotorAnother conformer for O=[C]OCCO[Li] exists which is 2.03 kJ/mol lower. But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: rotor scan switching back and forth between conformers or trying to switch ot a non-isomorphic conformer invalidating rotorAnother conformer for O=[C]OCCO[Li] exists which is 40.09 kJ/mol lower. But unable to propose troubleshooting methods.
pivots: [5, 6], dihedral: [4, 5, 6, 7], rotor symmetry: 2, max scan energy: 0.09 kJ/mol (set as a FreeRotor)


External symmetry: 1, optical isomers: 1

Geometry:
O       3.20569054    0.00188272   -0.00477460
C       2.08804990    0.38154185   -0.00477009
O       0.99075547   -0.34156497    0.00881742
C      -0.26385547    0.38307251    0.00693383
C      -1.40168784   -0.62550057   -0.00291130
O      -2.60008395    0.02914357   -0.00296442
Li     -4.04181131    0.72634917   -0.00371534
H      -0.30858626    1.01665605   -0.88081585
H      -0.31589625    1.00704723    0.90114397
H      -1.27811439   -1.28221729    0.87511954
H      -1.27231023   -1.27160587   -0.88795614
""",
)

entry(
    index = 122,
    label = "[Li][NH]",
    molecule =
"""
multiplicity 2
1 N  u1 p1 c0 {2,S} {3,S}
2 Li u0 p0 c0 {1,S}
3 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97147,0.00183955,1.79239e-05,-4.82963e-08,3.5538e-11,31076.5,-2.23953], Tmin=(10,'K'), Tmax=(506.074,'K')),
            NASAPolynomial(coeffs=[4.65678,0.00239123,-1.40148e-06,4.65515e-10,-6.23875e-14,30930.7,-5.83412], Tmin=(506.074,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (258.378,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'H-N': 1, 'Li-N': 1}

External symmetry: 1, optical isomers: 1

Geometry:
Li      1.33484506   -0.00016008    0.00000000
N      -0.37394685   -0.00029780    0.00000000
H      -1.38697520   -0.00186910    0.00000000
""",
)

entry(
    index = 123,
    label = "[Li]OCF",
    molecule =
"""
1 F  u0 p3 c0 {3,S}
2 O  u0 p2 c0 {3,S} {4,S}
3 C  u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
4 Li u0 p0 c0 {2,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89297,0.00898743,8.0458e-05,-2.86569e-07,2.94244e-10,-61932.6,8.08087], Tmin=(10,'K'), Tmax=(339.577,'K')),
            NASAPolynomial(coeffs=[4.28865,0.0170301,-1.11835e-05,3.51043e-09,-4.21134e-13,-62032.7,5.52084], Tmin=(339.577,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-514.921,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-F': 1, 'Li-O': 1, 'C-H': 2, 'C-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 4]]) broke during the scan.Bond ([[1, 2]]) broke during the scan.Bond ([[3, 5]]) broke during the scan.Significant difference observed between consecutive conformersBond ([[1, 3]]) broke during the scan.Significant difference observed between consecutive conformersCould not read energies


External symmetry: 1, optical isomers: 1

Geometry:
Li      0.47804559   -1.35607998    0.00073258
O      -1.14791351   -0.42540700   -0.00042380
C      -0.56092977    0.66385517   -0.00086146
F       1.32537088    0.11548203   -0.00091698
H      -0.42096162    1.23119723   -0.92914563
H      -0.42025673    1.23153321    0.92711191
""",
)

entry(
    index = 124,
    label = "[Li]F",
    molecule =
"""
1 F  u0 p3 c0 {2,S}
2 Li u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.51933,-0.00156062,1.33733e-05,-2.13521e-08,1.08314e-11,-42047.7,4.07628], Tmin=(10,'K'), Tmax=(653.288,'K')),
            NASAPolynomial(coeffs=[3.36888,0.00216887,-1.63791e-06,5.46605e-10,-6.68761e-14,-42087.9,4.27943], Tmin=(653.288,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-349.603,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'F-Li': 1}

External symmetry: 1, optical isomers: 1

Geometry:
Li      0.00000000    0.00000000    1.18031597
F       0.00000000    0.00000000   -0.39337832
""",
)

entry(
    index = 125,
    label = "[Li]OCCl",
    molecule =
"""
1 Cl u0 p3 c0 {3,S}
2 O  u0 p2 c0 {3,S} {4,S}
3 C  u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
4 Li u0 p0 c0 {2,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.56405,0.0310678,-5.29325e-05,4.91251e-08,-1.76392e-11,-44634,9.62982], Tmin=(10,'K'), Tmax=(820.554,'K')),
            NASAPolynomial(coeffs=[5.88572,0.0129554,-7.40138e-06,2.04123e-09,-2.19395e-13,-44786.3,0.282112], Tmin=(820.554,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-371.187,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-Cl': 1, 'Li-O': 1, 'C-H': 2, 'C-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for [Li]OCCl exists which is 6.23 kJ/mol lower.Another conformer for [Li]OCCl exists which is 6.23 kJ/mol lower. But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
Li     -0.07441528   -1.43614965   -0.00043409
O      -1.71606512   -0.45168285    0.00024799
C      -1.30342444    0.69570776   -0.00068430
Cl      1.41832368    0.07093796   -0.00076429
H      -1.14710103    1.24861831   -0.93641667
H      -1.14858930    1.25062200    0.93412146
""",
)

entry(
    index = 126,
    label = "[Li]O[CH2]",
    molecule =
"""
multiplicity 2
1 O  u0 p2 c0 {2,S} {3,S}
2 C  u1 p0 c0 {1,S} {4,S} {5,S}
3 Li u0 p0 c0 {1,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96452,0.00237604,4.82827e-05,-1.1106e-07,7.8801e-11,-6719.25,6.76033], Tmin=(10,'K'), Tmax=(458.431,'K')),
            NASAPolynomial(coeffs=[3.50795,0.0129834,-8.09741e-06,2.44732e-09,-2.86061e-13,-6746.99,7.84778], Tmin=(458.431,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-55.8723,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 2, 'Li-O': 1, 'C-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformersBond ([[1, 3]]) broke during the scan.Significant difference observed between consecutive conformersCould not read energies


External symmetry: 1, optical isomers: 1

Geometry:
Li      1.32795665   -0.84306988    0.00036599
O       0.35108104    0.56193792   -0.00018945
C      -0.70620766   -0.21349504    0.00002055
H      -1.27736114   -0.34235492    0.92751392
H      -1.27679973   -0.34359840   -0.92765357
""",
)

entry(
    index = 127,
    label = "[Li]N[CH2]",
    molecule =
"""
multiplicity 2
1 N  u0 p1 c0 {2,S} {3,S} {4,S}
2 C  u1 p0 c0 {1,S} {5,S} {6,S}
3 Li u0 p0 c0 {1,S}
4 H  u0 p0 c0 {1,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95994,0.00233926,5.32291e-05,-1.00927e-07,5.8278e-11,21339.4,7.33491], Tmin=(10,'K'), Tmax=(566.582,'K')),
            NASAPolynomial(coeffs=[3.1049,0.0175455,-1.13053e-05,3.57207e-09,-4.35494e-13,21289.1,9.67531], Tmin=(566.582,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (177.409,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'Li-N': 1, 'C-H': 2, 'H-N': 1, 'C-N': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 5], invalidation reason: Bond ([[1, 3]]) broke during the scan.Significant difference observed between consecutive conformersCould not read energies


External symmetry: 1, optical isomers: 2

Geometry:
Li      1.18326560   -1.05821125    0.20300653
N       0.41081543    0.54949778   -0.16918014
C      -0.71306433   -0.21405169    0.03866528
H       0.40267530    1.36282290    0.43476503
H      -1.52185777    0.11703093    0.68706526
H      -1.02862489   -0.86446700   -0.78021863
""",
)

entry(
    index = 128,
    label = "[Li]NC[CH2]",
    molecule =
"""
multiplicity 2
1 N  u0 p1 c0 {2,S} {4,S} {7,S}
2 C  u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3 C  u1 p0 c0 {2,S} {8,S} {9,S}
4 Li u0 p0 c0 {1,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {1,S}
8 H  u0 p0 c0 {3,S}
9 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87678,0.00792433,0.000118373,-2.76482e-07,1.90133e-10,26690.2,9.92626], Tmin=(10,'K'), Tmax=(499.449,'K')),
            NASAPolynomial(coeffs=[4.28577,0.0292508,-1.95643e-05,6.26341e-09,-7.62565e-13,26342.5,5.1652], Tmin=(499.449,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (221.883,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (203.705,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'Li-N': 1, 'C-H': 4, 'H-N': 1, 'C-C': 1, 'C-N': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 28.81 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 1 2 5 F
A 1 2 3 F
D 5 1 2 3 F
D 6 3 4 8 F
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 8], invalidation reason: Another conformer for [Li]NC[CH2] exists which is 1.79 kJ/mol lower.Another conformer for [Li]NC[CH2] exists which is 1.79 kJ/mol lower. But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
Li     -1.03242547   -1.62781129   -0.23798046
N      -1.12907580    0.09518013    0.06997806
C       0.18505219    0.68059167   -0.08287816
C       1.25424924   -0.34519186    0.05872603
H      -1.79507160    0.81616922    0.30209939
H       0.39752751    1.44732606    0.69380618
H       0.33815200    1.21170142   -1.04101935
H       2.17043786   -0.30634742   -0.51977295
H       1.25391514   -0.97464955    0.94701113
""",
)

entry(
    index = 129,
    label = "[Li]OC[=O]OC[CH2]",
    molecule =
"""
multiplicity 2
1  C  u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C  u1 p0 c0 {1,S} {8,S} {9,S}
3  C  u0 p0 c0 {4,S} {5,S} {10,D}
4  O  u0 p2 c0 {1,S} {3,S}
5  O  u0 p2 c0 {3,S} {11,S}
6  H  u0 p0 c0 {1,S}
7  H  u0 p0 c0 {1,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {2,S}
10 O  u0 p2 c0 {3,D}
11 Li u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.3461,0.0711013,-0.000275955,7.012e-07,-6.46996e-10,-65755.8,13.3802], Tmin=(10,'K'), Tmax=(356.178,'K')),
            NASAPolynomial(coeffs=[3.44896,0.0410465,-2.76762e-05,8.68871e-09,-1.03146e-12,-65579.8,15.5635], Tmin=(356.178,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-546.743,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (245.277,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-O': 3, 'Li-O': 1, 'C-H': 4, 'C=O': 1, 'C-C': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 4]]) broke during the scan.Bond ([[1, 2]]) broke during the scan.Significant difference observed between consecutive conformersBond ([[3, 5]]) broke during the scan.The rotor scan has a barrier of 844.11 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
pivots: [3, 5], dihedral: [2, 3, 5, 6], rotor symmetry: 2, max scan energy: 39.39 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 5 6 7 11 F
pivots: [5, 6], dihedral: [3, 5, 6, 7], rotor symmetry: 1, max scan energy: 31.21 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 5 6 7 11 F
pivots: [6, 7], dihedral: [5, 6, 7, 10], rotor symmetry: 1, max scan energy: 2.88 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
Li      2.88089101   -0.47395154   -0.00834993
O       1.76431223    1.00341154    0.00915533
C       0.87135515    0.12207619    0.00210305
O       1.12722678   -1.11472123   -0.01197092
O      -0.39759353    0.54674347    0.01064215
C      -1.41113323   -0.45553479   -0.00025272
C      -2.72768539    0.20900190    0.00092497
H      -1.28728059   -1.11426654    0.86829690
H      -1.27886909   -1.09658330   -0.88248228
H      -2.80025672    1.28086533   -0.10995952
H      -3.62717955   -0.38741775    0.05891925
""",
)

entry(
    index = 130,
    label = "[Li]O[C][OC]OC",
    molecule =
"""
multiplicity 2
1  O  u0 p2 c0 {4,S} {6,S}
2  O  u0 p2 c0 {5,S} {6,S}
3  O  u0 p2 c0 {6,S} {7,S}
4  C  u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
5  C  u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
6  C  u1 p0 c0 {1,S} {2,S} {3,S}
7  Li u0 p0 c0 {3,S}
8  H  u0 p0 c0 {4,S}
9  H  u0 p0 c0 {4,S}
10 H  u0 p0 c0 {4,S}
11 H  u0 p0 c0 {5,S}
12 H  u0 p0 c0 {5,S}
13 H  u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.24491,0.0787183,-0.00027618,6.15461e-07,-4.96196e-10,-53274.3,13.6202], Tmin=(10,'K'), Tmax=(407.27,'K')),
            NASAPolynomial(coeffs=[3.41676,0.0439911,-2.6591e-05,7.71514e-09,-8.63978e-13,-53014.3,16.3095], Tmin=(407.27,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-442.969,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-O': 5, 'C-H': 6, 'Li-O': 1}
1D rotors:
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Rotor scan led to non-isomorphic conformerAnother conformer for [Li]O[C][OC]OC exists which is 8.92 kJ/mol lower. But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 6], dihedral: [2, 3, 6, 7], invalidation reason: Bond ([[1, 3]]) broke during the scan.Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformersThe rotor scan has a barrier of 64.49 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
pivots: [4, 5], dihedral: [3, 4, 5, 8], rotor symmetry: 1, max scan energy: 5.10 kJ/mol
pivots: [6, 7], dihedral: [3, 6, 7, 11], rotor symmetry: 3, max scan energy: 3.49 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Could not read energies


External symmetry: 1, optical isomers: 2

Geometry:
Li     -0.49174283    2.14055826   -1.13293628
O      -0.68039665    1.40553149    0.42127211
C      -0.01637459    0.39034519   -0.00524505
O       1.32001151    0.36619105    0.32973811
C       2.07567892   -0.70098682   -0.20309581
O      -0.54680278   -0.87946138    0.11602975
C      -1.93288943   -0.96386966   -0.10218481
H       1.93469175   -0.77640552   -1.28748949
H       1.80197570   -1.65351414    0.25388711
H       3.12007004   -0.47872671    0.01221960
H      -2.20527798   -2.01046346    0.02450385
H      -2.18839470   -0.65006872   -1.12367255
H      -2.48653590   -0.34528519    0.60635158
""",
)

entry(
    index = 131,
    label = "OC[CH2]",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {8,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C u1 p0 c0 {2,S} {6,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.66375,0.0233622,-2.59184e-05,2.20743e-08,-7.99842e-12,-4719.75,8.62278], Tmin=(10,'K'), Tmax=(867.092,'K')),
            NASAPolynomial(coeffs=[3.2824,0.0196305,-9.96398e-06,2.50442e-09,-2.50352e-13,-4447.2,11.5985], Tmin=(867.092,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-39.3052,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (174.604,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-O': 1, 'C-H': 4, 'H-O': 1, 'C-C': 1}
1D rotors:
pivots: [1, 2], dihedral: [4, 1, 2, 3], rotor symmetry: 1, max scan energy: 9.49 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 1 2 3 8 F
pivots: [2, 3], dihedral: [1, 2, 3, 7], rotor symmetry: 2, max scan energy: 6.01 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.18714546   -0.25381669   -0.04533364
C       0.01016271    0.53441365   -0.02862622
C      -1.23068247   -0.27180176    0.01088457
H       1.15462063   -0.84925045    0.70612337
H       0.02596994    1.25095286    0.80453438
H       0.05562734    1.13277108   -0.94870140
H      -2.14445471    0.13382731    0.42433895
H      -1.26778259   -1.21761734   -0.51498485
""",
)
