#!/usr/bin/env python
# encoding: utf-8

name = "LithiumAdditionalThermo"
shortDesc = ""
longDesc = """
ARC v1.1.0
ARC project LithiumAdditionalThermo

Levels of theory used:

Conformers:       wb97x-d3/def2-tzvp, software: qchem (dft)
TS guesses:       wb97x-d3/def2-tzvp
Optimization:     wb97x-d3/def2-tzvp, software: qchem (dft) (using a fine grid)
Frequencies:      wb97x-d3/def2-tzvp, software: qchem (dft)
Single point:     ccsd(t)-f12/cc-pvdz-f12, software: molpro (wavefunction)
Rotor scans:      b3lyp/6-311++g(d,p), software: gaussian (dft)
Using p-type bond additivity corrections for thermo

Using the following ESS settings: {'gaussian': ['supercloud'], 'molpro': ['supercloud'], 'qchem': ['supercloud']}

Considered the following species and TSs:
Species [Li]OO (run time: 0:23:05)
Species [Li]O[O] (run time: 0:21:15)
Species COC[CH]OC (run time: 6:27:53)
Species COCCO[CH2] (Failed!) (run time: None)
Species [Li]OCCOC (run time: 6:07:25)
Species [O-][Np][=O]O[Li] (run time: 0:39:37)
Species O1COCC1 (Failed!) (run time: None)
Species [Li]SSSSSS[Li] (run time: 11:44:03)
Species [Li]SS[S] (run time: 0:26:01)
Species O=C1OC[CH]O1 (Failed!) (run time: None)
Species O=C1OC[F][CH]O1 (run time: 1:03:35)
Species O=C1O[C][F]CO1 (Failed!) (run time: None)
Species O=C1O[C][F]C[F]O1 (run time: 1:37:01)
Species O=C[OC]O[CH2] (run time: 5:16:48)
Species CCtN (run time: 0:20:48)
Species [CH2]CtN (run time: 0:20:11)
Species [Li]N=[C]C (run time: 0:24:16)
Species [Li]N=CC (run time: 0:30:09)
Species [Li]N=C (run time: 0:19:37)
Species [Li]N=C=C (run time: 0:20:34)
Species COCCOC (run time: 3:08:50)

Overall time since project initiation: 00:18:48
"""
entry(
    index = 0,
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
Bond corrections: {'Li-O': 1, 'H-O': 1, 'O-O': 1}
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
    index = 1,
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
Bond corrections: {'Li-O': 1, 'O-O': 1}

External symmetry: 2, optical isomers: 1

Geometry:
Li     -0.01444823   -1.37193017    0.00000000
O      -0.65913100    0.26394730    0.00000000
O       0.66445360    0.25010129    0.00000000
""",
)

entry(
    index = 2,
    label = "COC[CH]OC",
    molecule =
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {4,S}
2  O u0 p2 c0 {5,S} {6,S}
3  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
4  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
5  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
6  C u1 p0 c0 {2,S} {3,S} {15,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.2406,0.070506,-0.000171881,3.09281e-07,-2.08971e-10,-22829,13.1729], Tmin=(10,'K'), Tmax=(489.702,'K')),
            NASAPolynomial(coeffs=[2.70531,0.0493496,-2.888e-05,8.1487e-09,-8.92084e-13,-22470.5,18.4986], Tmin=(489.702,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-189.836,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (336.736,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-O': 4, 'C-H': 9, 'C-C': 1}
1D rotors:
pivots: [1, 2], dihedral: [7, 1, 2, 3], rotor symmetry: 3, max scan energy: 8.28 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 16.94 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 23.15 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 3 4 5 12 F
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 38.93 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 12 3 4 5 F
D 1 2 3 4 F
pivots: [5, 6], dihedral: [4, 5, 6, 13], rotor symmetry: 3, max scan energy: 5.44 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       1.76280445   -1.14028112    0.01535472
O       1.85942493    0.22225258   -0.31413538
C       0.84295577    1.02552508    0.27589970
C      -0.52416311    0.78009486   -0.23463114
O      -1.25775150   -0.14695975    0.42283115
C      -2.52686961   -0.41591117   -0.13591336
H       0.85826449   -1.60178204   -0.39638648
H       1.75831141   -1.28893213    1.10351439
H       2.63705044   -1.63474514   -0.40709567
H       0.84672224    0.89000675    1.36637162
H       1.13625240    2.05278481    0.05370717
H      -0.79252016    0.98513323   -1.26794064
H      -2.42920783   -0.79546964   -1.15823456
H      -2.99747553   -1.17400647    0.48667050
H      -3.14507867    0.48638583   -0.14296880
""",
)

entry(
    index = 3,
    label = "[Li]OCCOC",
    molecule =
"""
1  O  u0 p2 c0 {3,S} {5,S}
2  O  u0 p2 c0 {4,S} {6,S}
3  C  u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
4  C  u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
5  C  u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
6  Li u0 p0 c0 {2,S}
7  H  u0 p0 c0 {4,S}
8  H  u0 p0 c0 {4,S}
9  H  u0 p0 c0 {3,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {5,S}
12 H  u0 p0 c0 {5,S}
13 H  u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89808,0.0101055,0.000301528,-1.28342e-06,1.78609e-09,-50304.1,10.3522], Tmin=(10,'K'), Tmax=(229.112,'K')),
            NASAPolynomial(coeffs=[3.16406,0.0412046,-2.1783e-05,5.66016e-09,-5.84789e-13,-50318.5,11.7646], Tmin=(229.112,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-418.231,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (291.007,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-O': 3, 'C-H': 7, 'Li-O': 1, 'C-C': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 86.08 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 2 3 4 5 F
A 1 2 3 F
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 91.57 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 1 2 3 F
D 1 2 3 7 F
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 127.62 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 11 6 12 F
D 2 3 4 5 F
A 1 2 3 F
D 1 2 3 4 F
D 4 5 6 12 F
pivots: [5, 6], dihedral: [4, 5, 6, 11], rotor symmetry: 3, max scan energy: 8.79 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
Li     -0.50221866   -1.71194050    0.01184218
O      -1.82753276   -0.65384702   -0.17741444
C      -1.42093045    0.59303321    0.20004486
C       0.03163361    0.85603371   -0.19743982
O       0.81801399   -0.27895361    0.22287199
C       2.19368369   -0.11915975   -0.02894296
H      -2.00990241    1.41202738   -0.25918492
H      -1.49411261    0.76020104    1.29573083
H       0.12355840    0.94059325   -1.28833635
H       0.43991572    1.76067685    0.27072417
H       2.59243868    0.74082965    0.51894507
H       2.70755205   -1.01964393    0.30852594
H       2.38619077    0.02755674   -1.09839934
""",
)

entry(
    index = 4,
    label = "[O-][Np][=O]O[Li]",
    molecule =
"""
1 O  u0 p2 c0 {4,S} {5,S}
2 O  u0 p3 c-1 {4,S}
3 O  u0 p2 c0 {4,D}
4 N  u0 p0 c+1 {1,S} {2,S} {3,D}
5 Li u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95668,0.00224764,6.75905e-05,-1.43287e-07,8.99133e-11,-34037.7,8.08388], Tmin=(10,'K'), Tmax=(544.829,'K')),
            NASAPolynomial(coeffs=[4.02616,0.016487,-1.22206e-05,4.0602e-09,-4.98695e-13,-34264.2,5.78186], Tmin=(544.829,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-283.026,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'Li-O': 1, 'N=O': 1, 'N-O': 2}
1D rotors:
* Invalidated! pivots: [2, 4], dihedral: [1, 2, 4, 5], invalidation reason: Bond ([[1, 5]]) broke during the scan.Bond ([[4, 5]]) broke during the scan.The rotor scan has a barrier of 838.64 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 2, optical isomers: 1

Geometry:
O       0.44869627   -1.07437932   -0.00001231
N      -0.23520208   -0.00003792   -0.00000119
O      -1.43033770   -0.00025963    0.00001016
O       0.44830940    1.07454773   -0.00001231
Li      1.97168509    0.00024782    0.00003756
""",
)

entry(
    index = 5,
    label = "[Li]SSSSSS[Li]",
    molecule =
"""
1 S  u0 p2 c0 {2,S} {3,S}
2 S  u0 p2 c0 {1,S} {4,S}
3 S  u0 p2 c0 {1,S} {5,S}
4 S  u0 p2 c0 {2,S} {6,S}
5 S  u0 p2 c0 {3,S} {7,S}
6 S  u0 p2 c0 {4,S} {8,S}
7 Li u0 p0 c0 {5,S}
8 Li u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.30954,0.0560127,0.000196548,-1.05043e-06,1.17098e-09,-27522.4,14.7361], Tmin=(10,'K'), Tmax=(369.41,'K')),
            NASAPolynomial(coeffs=[15.5412,0.015747,-1.42513e-05,5.48079e-09,-7.52375e-13,-29055.1,-40.607], Tmin=(369.41,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-228.772,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'Li-S': 2, 'S-S': 5}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[3, 8]]) broke during the scan.Bond ([[1, 5]]) broke during the scan.Bond ([[1, 2]]) broke during the scan.Bond ([[7, 8]]) broke during the scan.Bond ([[4, 5]]) broke during the scan.Bond ([[1, 7]]) broke during the scan.
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Bond ([[1, 5]]) broke during the scan.Bond ([[1, 2]]) broke during the scan.Bond ([[3, 8]]) broke during the scan.Bond ([[3, 4]]) broke during the scan.Bond ([[7, 8]]) broke during the scan.Bond ([[2, 8]]) broke during the scan.Bond ([[5, 6]]) broke during the scan.Bond ([[6, 7]]) broke during the scan.Bond ([[1, 7]]) broke during the scan.Bond ([[2, 3]]) broke during the scan.Bond ([[1, 8]]) broke during the scan.Bond ([[4, 5]]) broke during the scan.Significant difference observed between consecutive conformersThe rotor scan has a barrier of 4638.47 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: Bond ([[3, 8]]) broke during the scan.Bond ([[7, 8]]) broke during the scan.Significant difference observed between consecutive conformersCould not read energies
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 7], invalidation reason: Bond ([[3, 8]]) broke during the scan.Bond ([[7, 8]]) broke during the scan.Bond ([[1, 5]]) broke during the scan.Bond ([[1, 7]]) broke during the scan.Bond ([[1, 2]]) broke during the scan.Bond ([[3, 4]]) broke during the scan.Significant difference observed between consecutive conformersCould not read energies
* Invalidated! pivots: [6, 7], dihedral: [5, 6, 7, 8], invalidation reason: Bond ([[1, 5]]) broke during the scan.Bond ([[4, 5]]) broke during the scan.Bond ([[2, 8]]) broke during the scan.Bond ([[3, 8]]) broke during the scan.Bond ([[7, 8]]) broke during the scan.Bond ([[1, 2]]) broke during the scan.Bond ([[3, 4]]) broke during the scan.Significant difference observed between consecutive conformersThe rotor scan has a barrier of 237.71 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 1, optical isomers: 2

Geometry:
Li     -0.29772235    1.05143173    1.58432106
S       1.86737597    1.47856214    0.61820790
S       1.78870604    0.04532187   -0.85142696
S       1.09821354   -1.72581236   -0.09506836
S      -0.72880491   -1.35829842    0.81752683
S      -2.02714156   -0.50336881   -0.50965304
S      -1.96695750    1.52131562   -0.08214317
Li      0.14957097    1.84195652   -1.03805980
""",
)

entry(
    index = 6,
    label = "[Li]SS[S]",
    molecule =
"""
multiplicity 2
1 S  u0 p2 c0 {2,S} {4,S}
2 S  u0 p2 c0 {1,S} {3,S}
3 S  u1 p2 c0 {2,S}
4 Li u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82825,0.0127896,6.63646e-05,-2.64399e-07,2.50127e-10,-3317.63,10.5702], Tmin=(10,'K'), Tmax=(417.251,'K')),
            NASAPolynomial(coeffs=[7.236,0.00647912,-5.70617e-06,2.15137e-09,-2.90898e-13,-3831.45,-5.64108], Tmin=(417.251,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-27.5851,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'Li-S': 1, 'S-S': 2}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: The rotor scan has a barrier of 87.47 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 2, optical isomers: 1

Geometry:
Li     -0.00029164   -1.88061351    0.00031014
S      -1.64056014   -0.25705326    0.00006949
S       0.00005708    0.86696251   -0.00008210
S       1.64043728   -0.25736778    0.00006951
""",
)

entry(
    index = 7,
    label = "O=C1OC[F][CH]O1",
    molecule =
"""
multiplicity 2
1 F u0 p3 c0 {5,S}
2 O u0 p2 c0 {5,S} {7,S}
3 O u0 p2 c0 {6,S} {7,S}
4 O u0 p2 c0 {7,D}
5 C u0 p0 c0 {1,S} {2,S} {6,S} {8,S}
6 C u1 p0 c0 {3,S} {5,S} {9,S}
7 C u0 p0 c0 {2,S} {3,S} {4,D}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90506,0.0056248,0.000114392,-2.27269e-07,1.35244e-10,-66351.2,12.3313], Tmin=(10,'K'), Tmax=(557.443,'K')),
            NASAPolynomial(coeffs=[2.57916,0.036361,-2.54202e-05,8.23252e-09,-1.00162e-12,-66533.1,14.9956], Tmin=(557.443,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-551.713,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-F': 1, 'C-O': 4, 'C=O': 1, 'C-H': 2, 'C-C': 1}

External symmetry: 1, optical isomers: 2

Geometry:
O       2.20596130   -0.52514743    0.21113867
C       1.10925817   -0.14631236    0.01369757
O       0.07290657   -0.89928884   -0.42275247
C      -1.11024906   -0.14865163   -0.43237742
F      -1.91517090   -0.57304395    0.60190907
C      -0.61054024    1.22928300   -0.21720114
O       0.68732297    1.14640616    0.17311135
H      -1.65817222   -0.33855369   -1.35526327
H      -1.16697667    2.10577654    0.06835142
""",
)

entry(
    index = 8,
    label = "O=C1O[C][F]C[F]O1",
    molecule =
"""
multiplicity 2
1 F u0 p3 c0 {6,S}
2 F u0 p3 c0 {7,S}
3 O u0 p2 c0 {6,S} {8,S}
4 O u0 p2 c0 {7,S} {8,S}
5 O u0 p2 c0 {8,D}
6 C u0 p0 c0 {1,S} {3,S} {7,S} {9,S}
7 C u1 p0 c0 {2,S} {4,S} {6,S}
8 C u0 p0 c0 {3,S} {4,S} {5,D}
9 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86634,0.00863828,0.000134234,-3.08225e-07,2.09389e-10,-88378,13.6803], Tmin=(10,'K'), Tmax=(497.078,'K')),
            NASAPolynomial(coeffs=[3.50637,0.0366549,-2.61131e-05,8.49208e-09,-1.03119e-12,-88652.6,12.0437], Tmin=(497.078,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-734.85,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-F': 2, 'C-O': 4, 'C=O': 1, 'C-H': 1, 'C-C': 1}

External symmetry: 1, optical isomers: 2

Geometry:
O      -2.49813862   -0.09477813    0.04675173
C      -1.32598681   -0.05460666   -0.00860489
O      -0.48792523   -1.05338479    0.42866284
C       0.79766886   -0.65668318    0.27258337
F       1.57580340   -1.57799760   -0.26438298
C       0.78160522    0.71883545   -0.34111839
F       1.28515396    1.65541154    0.50098883
O      -0.58731034    0.95595871   -0.52236837
H       1.30790394    0.79265665   -1.29432730
""",
)

entry(
    index = 9,
    label = "O=C[OC]O[CH2]",
    molecule =
"""
multiplicity 2
1  O u0 p2 c0 {4,S} {5,S}
2  O u0 p2 c0 {5,S} {6,S}
3  O u0 p2 c0 {5,D}
4  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
5  C u0 p0 c0 {1,S} {2,S} {3,D}
6  C u1 p0 c0 {2,S} {10,S} {11,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74465,0.0341353,-5.70048e-06,-1.50671e-08,7.28235e-12,-47095.4,11.2649], Tmin=(10,'K'), Tmax=(1049.4,'K')),
            NASAPolynomial(coeffs=[9.75904,0.0258208,-1.46996e-05,3.91691e-09,-4.0085e-13,-49162.2,-21.8741], Tmin=(1049.4,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-391.539,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (241.12,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-O': 4, 'C=O': 1, 'C-H': 5}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 40.92 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 5 6 10 11 F
pivots: [2, 5], dihedral: [1, 2, 5, 6], rotor symmetry: 1, max scan energy: 38.03 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 2 5 6 11 F
D 5 6 10 11 F
pivots: [3, 4], dihedral: [2, 3, 4, 7], rotor symmetry: 3, max scan energy: 3.20 kJ/mol
pivots: [5, 6], dihedral: [2, 5, 6, 10], rotor symmetry: 2, max scan energy: 22.75 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 5 6 10 11 F


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.02738340   -1.29667643    0.01701349
C      -0.04654373   -0.09957343    0.01792455
O       1.00178444    0.70918265    0.00892019
C       2.26790493    0.04964347   -0.00536109
O      -1.14963582    0.66996278    0.02591696
C      -2.35646901    0.03677362    0.06548275
H       2.36545828   -0.56802926   -0.89785256
H       2.38171168   -0.57579049    0.87971871
H       3.00945441    0.84359598   -0.00887538
H      -3.19164285    0.70619022   -0.04866512
H      -2.38023833   -1.03409239   -0.05711663
""",
)

entry(
    index = 10,
    label = "CCtN",
    molecule =
"""
1 N u0 p1 c0 {3,T}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {1,T} {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.99047,0.000417087,3.8756e-05,-6.00184e-08,3.03682e-11,7668.92,5.03807], Tmin=(10,'K'), Tmax=(509.148,'K')),
            NASAPolynomial(coeffs=[1.93377,0.0165752,-8.84765e-06,2.31329e-09,-2.37884e-13,7878.35,13.5721], Tmin=(509.148,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (63.7555,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C#N': 1, 'C-H': 3, 'C-C': 1}

External symmetry: 3, optical isomers: 1

Geometry:
C       0.00000000    0.00000000    1.17445126
C       0.00000000    0.00000000   -0.28152283
N       0.00000000    0.00000000   -1.42802759
H       1.02399836    0.00000000    1.54629535
H      -0.51199918    0.88680859    1.54629535
H      -0.51199918   -0.88680859    1.54629535
""",
)

entry(
    index = 11,
    label = "[CH2]CtN",
    molecule =
"""
multiplicity 2
1 N u0 p1 c0 {3,T}
2 C u1 p0 c0 {3,S} {4,S} {5,S}
3 C u0 p0 c0 {1,T} {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97566,0.00147517,3.87512e-05,-7.48941e-08,4.50762e-11,30070.6,5.57726], Tmin=(10,'K'), Tmax=(528.34,'K')),
            NASAPolynomial(coeffs=[3.189,0.0126304,-7.68159e-06,2.3224e-09,-2.74994e-13,30081.2,8.18373], Tmin=(528.34,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (250.013,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C#N': 1, 'C-H': 2, 'C-C': 1}

External symmetry: 2, optical isomers: 1

Geometry:
C       0.00000000    0.00000000    1.19081292
C       0.00000000    0.00000000   -0.19034534
N       0.00000000    0.00000000   -1.35151389
H       0.93626596    0.00000000    1.72908334
H      -0.93626596    0.00000000    1.72908334
""",
)

entry(
    index = 12,
    label = "[Li]N=[C]C",
    molecule =
"""
multiplicity 2
1 N  u0 p1 c0 {3,D} {4,S}
2 C  u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
3 C  u1 p0 c0 {1,D} {2,S}
4 Li u0 p0 c0 {1,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65421,0.0327694,-8.43234e-05,1.44345e-07,-9.36987e-11,20975.3,7.48533], Tmin=(10,'K'), Tmax=(485.128,'K')),
            NASAPolynomial(coeffs=[4.29295,0.0181564,-1.02414e-05,2.82773e-09,-3.05595e-13,21023.3,5.99936], Tmin=(485.128,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (174.387,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'Li-N': 1, 'C-H': 3, 'C-C': 1, 'C=N': 1}
1D rotors:
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: not a torsional mode (angles = 179.96, 109.61 degrees)


External symmetry: 3, optical isomers: 1

Geometry:
Li     -3.06419338   -0.00016070    0.00336616
N      -1.00552464    0.00008324   -0.00204369
C       0.13792585    0.00002801   -0.00106716
C       1.58957226   -0.00008390    0.00115542
H       1.95579451   -0.89431229   -0.50167921
H       1.95287018    0.01039226    1.02812201
H       1.95588321    0.88363931   -0.51986697
""",
)

entry(
    index = 13,
    label = "[Li]N=CC",
    molecule =
"""
1 N  u0 p1 c0 {3,D} {4,S}
2 C  u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
3 C  u0 p0 c0 {1,D} {2,S} {8,S}
4 Li u0 p0 c0 {1,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {2,S}
8 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71148,0.028102,-6.80134e-05,1.41494e-07,-1.0724e-10,11587,7.8912], Tmin=(10,'K'), Tmax=(461.055,'K')),
            NASAPolynomial(coeffs=[2.71649,0.0241076,-1.39382e-05,3.90358e-09,-4.2523e-13,11813,13.3765], Tmin=(461.055,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (96.333,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'Li-N': 1, 'C-H': 4, 'C-C': 1, 'C=N': 1}
1D rotors:
pivots: [3, 4], dihedral: [2, 3, 4, 6], rotor symmetry: 3, max scan energy: 5.14 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
Li      2.61674894   -0.54234889    0.00002700
N       1.01717182    0.07357765    0.00001383
C      -0.14889597    0.50859545    0.00000437
C      -1.41462347   -0.32673923    0.00000301
H      -0.37138717    1.60123753   -0.00004874
H      -2.02582212   -0.09645732    0.87881869
H      -2.02579297   -0.09649924   -0.87884411
H      -1.16649739   -1.38892503    0.00003147
""",
)

entry(
    index = 14,
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
Bond corrections: {'Li-N': 1, 'C-H': 2, 'C=N': 1}

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
    index = 16,
    label = "COCCOC",
    molecule =
"""
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {6,S}
3  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
4  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
5  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
6  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.08519,0.0735618,-0.000150286,2.07472e-07,-1.07508e-10,-44483,10.4439], Tmin=(10,'K'), Tmax=(635.231,'K')),
            NASAPolynomial(coeffs=[2.31805,0.0498087,-2.67009e-05,6.9348e-09,-7.06738e-13,-43808.8,18.3362], Tmin=(635.231,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-369.942,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (361.68,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-O': 4, 'C-H': 10, 'C-C': 1}
1D rotors:
pivots: [1, 2], dihedral: [7, 1, 2, 3], rotor symmetry: 3, max scan energy: 9.82 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 30.67 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 36.95 kJ/mol
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 30.67 kJ/mol
pivots: [5, 6], dihedral: [4, 5, 6, 14], rotor symmetry: 3, max scan energy: 9.82 kJ/mol


External symmetry: 2, optical isomers: 1

Geometry:
C       2.96325442   -0.11316643   -0.00014617
O       1.71092399    0.51732109    0.00002989
C       0.64449209   -0.39543599    0.00010228
C      -0.64451233    0.39566066    0.00016940
O      -1.71081578   -0.51726373    0.00008900
C      -2.96328151    0.11294278   -0.00017957
H       3.09597981   -0.74168676   -0.89068847
H       3.09630665   -0.74156541    0.89043343
H       3.72402393    0.66633092   -0.00035031
H       0.68127235   -1.04265254   -0.88750718
H       0.68139594   -1.04267326    0.88769072
H      -0.68148177    1.04292878   -0.88739206
H      -0.68150380    1.04280842    0.88781704
H      -3.09620762    0.74127058   -0.89083041
H      -3.72388316   -0.66672927   -0.00023577
H      -3.09651417    0.74145409    0.89029278
""",
)
