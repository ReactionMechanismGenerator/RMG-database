#!/usr/bin/env python
# encoding: utf-8

name = "T3_soup"
shortDesc = ""
longDesc = """
This library contains thermo for species relevant for the H2O//CH3OH/AIBN soup
most species do not exist in the soup, but might be predicted by RMG due to bad thermo estimations.


Levels of theory used:

Conformers:       wb97xd/def2svp, software: gaussian (dft)
TS guesses:       None
Composite method: cbs-qb3, software: gaussian (composite) (using a fine grid)
Frequencies:      b3lyp/cbsb7, software: gaussian (dft)
Rotor scans:      b3lyp/cbsb7, software: gaussian (dft)
Using p-type bond additivity corrections for thermo
Species C3H6NO3_10 (Failed!) (run time: None)
Species C4H7N2O3_11 (run time: 8 days, 19:42:56)
Species C4H6N2O3_12 (run time: 9 days, 10:43:56)
Species C4H4N2O2_13 (run time: 0:51:57)
Species C4H5N2O3_14 (Failed!) (run time: None)
Species C4H5N2O3_15 (run time: 8 days, 7:08:50)
Species C4H7N2O3_0 (run time: 5 days, 7:03:10)
Species C4H6N2O3_1 (run time: 6 days, 7:14:21)
Species C4H5N2O3_2 (run time: 5 days, 3:56:21)
Species C4H7N2O3_0 (run time: 6 days, 5:23:05)
Species C4H6N2O3_1 (run time: 6 days, 5:37:10)
Species C3H8N2O3_2 (run time: 9 days, 3:39:06)
Species C3H5O2_3 (run time: 1 day, 1:15:15)
Species C3H7N2O3_4 (run time: 8 days, 15:44:21)
Species C3H6N2O3_5 (run time: 6 days, 0:43:06)
Species C3H5N2O3_6 (run time: 5 days, 0:46:05)
Species N1=NO1_7 (run time: 0:00:49)
"""
entry(
    index = 0,
    label = "CH2NO_0",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 N u1 p1 c0 {1,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.06235,-0.00469309,5.90502e-05,-8.63976e-08,3.95432e-11,5591.56,7.17223], Tmin=(10,'K'), Tmax=(713.263,'K')),
            NASAPolynomial(coeffs=[2.40211,0.0167985,-1.17632e-05,3.7327e-09,-4.3971e-13,5518.55,12.4489], Tmin=(713.263,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (46.4973,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (103.931,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C-O': 1, 'C-H': 1, 'C=N': 1}
1D rotors:
pivots: [1, 3], dihedral: [5, 1, 3, 2], rotor symmetry: 1, max scan energy: 34.38 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O       0.88308600   -0.44637800    0.14913700
N      -0.82180200    1.01851500   -0.46831900
C      -0.41021900   -0.03830400    0.06494500
H      -1.09070700   -0.75568600    0.52992500
H       1.43964200    0.22185200   -0.27569000
""",
)

entry(
    index = 1,
    label = "C3H8N2O3_2",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {6,S}
2  O u0 p2 c0 {1,S} {4,S}
3  O u0 p2 c0 {8,D}
4  N u0 p1 c0 {2,S} {5,S} {14,S}
5  N u0 p1 c0 {4,S} {15,S} {16,S}
6  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
7  C u0 p0 c0 {8,S} {11,S} {12,S} {13,S}
8  C u0 p0 c0 {3,D} {6,S} {7,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.34111,0.0641646,-9.47234e-05,1.57805e-07,-1.18637e-10,-13708.9,13.6464], Tmin=(10,'K'), Tmax=(432.111,'K')),
            NASAPolynomial(coeffs=[2.94696,0.0574252,-3.52688e-05,1.0444e-08,-1.19308e-12,-13577.9,16.3394], Tmin=(432.111,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-114.001,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (378.308,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C=O': 1, 'C-C': 2, 'O-O': 1, 'H-N': 3, 'C-O': 1, 'N-N': 1, 'N-O': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [6, 1, 2, 4], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformersThe rotor scan has a barrier of 64.35 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
* Invalidated! pivots: [1, 6], dihedral: [2, 1, 6, 8], invalidation reason: Another conformer for C3H8N2O3_2 exists which is 20.71 kJ/mol lower.
* Invalidated! pivots: [2, 4], dihedral: [1, 2, 4, 5], invalidation reason: 
* Invalidated! pivots: [4, 5], dihedral: [2, 4, 5, 15], invalidation reason: 
* Invalidated! pivots: [6, 8], dihedral: [1, 6, 8, 3], invalidation reason: 
pivots: [7, 8], dihedral: [11, 7, 8, 3], rotor symmetry: 3, max scan energy: 1.80 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       0.16681500   -2.72383200   -1.83621900
O       1.51962000   -2.71742900   -0.95151000
O      -1.12678200   -0.92770100   -0.14948600
N       2.25215300   -1.67317900   -1.29183800
N       1.76728000   -0.39737400   -0.95588500
C      -0.83398900   -3.16455100   -0.98110900
C      -2.33403200   -2.61104600    1.04260100
C      -1.40095200   -2.10052900   -0.03599200
H      -0.51920700   -4.04648900   -0.40340300
H      -1.66204900   -3.49931000   -1.62461900
H      -2.99723800   -3.39518100    0.66645800
H      -1.73822500   -3.05183200    1.84932700
H      -2.91800500   -1.78566100    1.44767100
H       2.50563500   -1.71176700   -2.27613900
H       1.89187300   -0.28354100    0.04538400
H       0.76073500   -0.37393000   -1.13667400
""",
)

entry(
    index = 2,
    label = "C4H7N2O3_0",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {2,S} {13,D}
4  N u0 p1 c0 {5,S} {7,S} {14,S}
5  C u0 p0 c0 {4,S} {15,D} {16,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {4,S} {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 O u0 p2 c0 {3,D}
14 H u0 p0 c0 {4,S}
15 N u1 p1 c0 {5,D}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73533,0.0609181,-3.66575e-05,9.47899e-09,-7.54667e-13,10136,13.5891], Tmin=(10,'K'), Tmax=(1672.77,'K')),
            NASAPolynomial(coeffs=[32.3948,0.00486304,2.41998e-06,-1.63613e-09,2.40136e-13,-1197.77,-144.639], Tmin=(1672.77,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (84.2287,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (378.308,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-N': 1, 'C=N': 1, 'C-H': 6, 'C=O': 1, 'C-C': 2, 'O-O': 1, 'H-N': 1, 'C-O': 1, 'N-O': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [6, 1, 2, 4], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformersThe rotor scan has a barrier of 57.89 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)The rotor scan has a barrier of 57.89 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
pivots: [1, 6], dihedral: [2, 1, 6, 8], rotor symmetry: 1, max scan energy: 59.51 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 10 6 8 3 F
D 13 7 8 3 F
D 6 1 2 4 F
* Invalidated! pivots: [2, 4], dihedral: [1, 2, 4, 9], invalidation reason: 
* Invalidated! pivots: [4, 9], dihedral: [2, 4, 9, 5], invalidation reason: 
* Invalidated! pivots: [6, 8], dihedral: [1, 6, 8, 3], invalidation reason: 
* Invalidated! pivots: [7, 8], dihedral: [12, 7, 8, 3], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.24301900   -0.16944300    0.88598400
O      -1.94292500    1.09978800    0.28361400
O      -0.98713700    1.61940000    3.01980400
N      -3.01626400    1.39915600    1.00953100
N      -5.08409400    0.46116100    1.65451600
C       0.01891700    0.25552200    1.31078000
C       1.37841400    1.35375700    3.20411200
C       0.02451200    1.13283700    2.56488500
C      -4.13886200    0.56852000    0.83845600
H       0.58452800   -0.66468100    1.50917500
H       0.55840900    0.78847800    0.51322700
H       1.64950200    0.46450400    3.78368100
H       1.33185700    2.20905500    3.87658800
H       2.16049200    1.50363400    2.45489400
H      -2.76600300    1.66982400    1.96239700
H      -4.14314800    0.04577400   -0.12450000
""",
)

entry(
    index = 3,
    label = "C3H5O2_3",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {4,S} {10,S}
2  O u1 p2 c0 {5,S}
3  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
4  C u0 p0 c0 {1,S} {3,S} {5,D}
5  C u0 p0 c0 {2,S} {4,D} {9,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86697,0.0102386,9.53319e-05,-2.52678e-07,2.2105e-10,-33014.3,10.1451], Tmin=(10,'K'), Tmax=(289.466,'K')),
            NASAPolynomial(coeffs=[2.31292,0.0317135,-1.5951e-05,3.61866e-09,-3.05398e-13,-32924.3,15.7159], Tmin=(289.466,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-274.525,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (220.334,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 4, 'C-C': 1, 'C=C': 1, 'H-O': 1, 'C-O': 2}
1D rotors:
pivots: [1, 4], dihedral: [10, 1, 4, 3], rotor symmetry: 1, max scan energy: 68.53 kJ/mol
pivots: [3, 4], dihedral: [6, 3, 4, 1], rotor symmetry: 3, max scan energy: 5.80 kJ/mol
pivots: [4, 5], dihedral: [1, 4, 5, 2], rotor symmetry: 1, max scan energy: 132.73 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 3 1 4 5 F
D 7 3 4 5 F
D 10 1 4 5 F


External symmetry: 1, optical isomers: 1

Geometry:
O      -0.98531600    0.49704700   -1.12557000
O       1.51518400    1.26807200   -1.30660300
C      -0.66393100   -0.76792600    0.89173400
C      -0.12642800    0.09344100   -0.18780000
C       1.21458300    0.54326300   -0.33922500
H      -1.46564000   -0.25441300    1.43350800
H       0.12193200   -1.03665400    1.59933600
H      -1.09347600   -1.68607700    0.47647600
H       1.95619400    0.23363900    0.41234700
H      -0.43920700    1.04407700   -1.73152800
""",
)

entry(
    index = 4,
    label = "C4H6N2O3_1",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {2,S} {13,D}
4  N u0 p1 c0 {6,S} {7,S} {14,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {4,S} {5,S}
7  C u0 p0 c0 {4,S} {15,T}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 O u0 p2 c0 {3,D}
14 H u0 p0 c0 {4,S}
15 N u0 p1 c0 {7,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.52547,0.0508057,0.000295869,-1.91836e-06,3.18403e-09,1866.35,14.5171], Tmin=(10,'K'), Tmax=(227.001,'K')),
            NASAPolynomial(coeffs=[6.34115,0.0508529,-3.26056e-05,1.00872e-08,-1.20017e-12,1610.57,2.28981], Tmin=(227.001,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (15.5888,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (349.208,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-N': 1, 'C-H': 5, 'C=O': 1, 'C-C': 2, 'C#N': 1, 'O-O': 1, 'H-N': 1, 'C-O': 1, 'N-O': 1}
1D rotors:
pivots: [1, 2], dihedral: [6, 1, 2, 4], rotor symmetry: 1, max scan energy: 62.31 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 1 2 4 15 F
D 2 4 9 15 F
D 11 6 8 7 F
D 14 7 8 6 F
D 2 1 6 8 F
pivots: [1, 6], dihedral: [2, 1, 6, 8], rotor symmetry: 1, max scan energy: 42.62 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 11 6 8 7 F
D 14 7 8 6 F
D 6 1 2 4 F
* Invalidated! pivots: [2, 4], dihedral: [1, 2, 4, 9], invalidation reason: 
* Invalidated! pivots: [6, 8], dihedral: [1, 6, 8, 3], invalidation reason: 
* Invalidated! pivots: [7, 8], dihedral: [12, 7, 8, 3], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.03145200   -0.57417200   -1.29625700
O       0.74126100   -1.03704900   -0.04989400
O      -2.49159300    1.20634400    0.59696200
N       1.97904900   -1.38059900   -0.45652100
N       3.56080400    0.47892700   -1.02392600
C      -1.32765600   -0.27125500   -0.82997000
C      -0.36901300    2.05441200   -0.13592200
C      -1.47849700    1.03773400   -0.03902200
C       2.81122500   -0.37031900   -0.79412000
H      -1.91794400   -0.17453000   -1.74962100
H      -1.74964100   -1.09634800   -0.24715900
H       0.52620600    1.67249800    0.36294000
H      -0.68712000    2.98102500    0.33929600
H      -0.08998000    2.23191300   -1.17796900
H       1.98590100   -2.19344000   -1.06699000
""",
)

entry(
    index = 5,
    label = "C3H7N2O3_4",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {6,S}
2  O u0 p2 c0 {1,S} {4,S}
3  O u0 p2 c0 {8,D}
4  N u0 p1 c0 {2,S} {5,S} {14,S}
5  N u1 p1 c0 {4,S} {15,S}
6  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
7  C u0 p0 c0 {8,S} {11,S} {12,S} {13,S}
8  C u0 p0 c0 {3,D} {6,S} {7,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.11113,0.0903443,-0.000250906,5.01749e-07,-3.89092e-10,-11941.5,14.7825], Tmin=(10,'K'), Tmax=(400.673,'K')),
            NASAPolynomial(coeffs=[4.73827,0.0532093,-3.3674e-05,1.01734e-08,-1.17828e-12,-11904.2,10.5133], Tmin=(400.673,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-99.3059,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (353.365,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C=O': 1, 'C-C': 2, 'O-O': 1, 'H-N': 2, 'C-O': 1, 'N-N': 1, 'N-O': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [6, 1, 2, 4], invalidation reason: Significant difference observed between consecutive conformersBond ([[4, 14]]) broke during the scan.Significant difference observed between consecutive conformersBond ([[1, 14]]) broke during the scan.Bond ([[2, 4]]) broke during the scan.Bond ([[4, 5]]) broke during the scan.Bond ([[5, 15]]) broke during the scan.Significant difference observed between consecutive conformersThe rotor scan has a barrier of 13006.96 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
* Invalidated! pivots: [1, 6], dihedral: [2, 1, 6, 8], invalidation reason: Significant difference observed between consecutive conformersCould not read energies
* Invalidated! pivots: [2, 4], dihedral: [1, 2, 4, 5], invalidation reason: Significant difference observed between consecutive conformersBond ([[4, 14]]) broke during the scan.The rotor scan has a barrier of 500.06 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
* Invalidated! pivots: [4, 5], dihedral: [2, 4, 5, 15], invalidation reason: Another conformer for C3H7N2O3_4 exists which is 22.52 kJ/mol lower.
pivots: [6, 8], dihedral: [1, 6, 8, 3], rotor symmetry: 1, max scan energy: 27.41 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 6 1 14 F
A 1 14 4 F
D 13 7 8 3 F
D 14 1 6 9 F
D 6 1 14 4 F
* Invalidated! pivots: [7, 8], dihedral: [11, 7, 8, 3], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
O       0.17007600   -3.10297200    1.45959300
O      -1.04106900   -5.67734600    3.00143200
O      -2.59860400   -1.20932600    2.31937300
N       0.11354100   -5.68915500    2.51318400
N       0.93002600   -6.64279100    2.44363300
C      -1.09003000   -2.78892900    1.23005300
C      -1.22850500   -2.46416000    3.86296700
C      -1.75530300   -2.01665800    2.53665200
H      -1.27424800   -2.10364300    0.39237600
H      -1.78360800   -3.65477600    1.21743000
H      -1.76775700   -1.96676800    4.66758500
H      -1.31551800   -3.55306800    3.92735900
H      -0.16219000   -2.22213000    3.89667300
H       0.42580600   -4.77921500    2.10107700
H       0.45998600   -7.44579100    2.88319300
""",
)

entry(
    index = 6,
    label = "C4H7N2O3_11",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {1,S} {10,D} {11,S}
4  C u0 p0 c0 {2,D} {12,S} {13,S}
5  N u0 p1 c0 {7,S} {14,S} {15,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {5,S} {6,S}
8  O u0 p2 c0 {2,S} {16,S}
9  H u0 p0 c0 {1,S}
10 N u1 p1 c0 {3,D}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.59514,0.0386182,0.000222239,-9.0291e-07,1.04631e-09,15193.9,14.2596], Tmin=(10,'K'), Tmax=(294.378,'K')),
            NASAPolynomial(coeffs=[3.82935,0.0629643,-4.20882e-05,1.33716e-08,-1.61715e-12,15060.9,11.3901], Tmin=(294.378,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (126.384,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (378.308,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 4, 'N-O': 1, 'C-C': 2, 'O-O': 1, 'C-O': 2, 'H-O': 1, 'C=N': 1, 'H-N': 2, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [6, 1, 2, 4], invalidation reason: The rotor scan has a barrier of 40.64 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
* Invalidated! pivots: [1, 6], dihedral: [2, 1, 6, 7], invalidation reason: Another conformer for C4H7N2O3_11 exists which is 15.34 kJ/mol lower.
pivots: [2, 4], dihedral: [1, 2, 4, 14], rotor symmetry: 1, max scan energy: 129.11 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 2 4 15 F
D 2 4 14 15 F
D 1 6 8 11 F
D 6 1 2 4 F
D 10 6 7 3 F
D 2 1 6 10 F
B 1 2 F
* Invalidated! pivots: [3, 7], dihedral: [16, 3, 7, 6], invalidation reason: 
* Invalidated! pivots: [6, 7], dihedral: [1, 6, 7, 3], invalidation reason: 
* Invalidated! pivots: [6, 8], dihedral: [1, 6, 8, 5], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
O       0.76855100    0.93136400   -0.08768900
O       1.79013100    0.92875600   -1.35489600
O      -0.73652800    0.09028700    1.95063300
N       2.93074700    0.38108900   -1.02793200
N       1.13006300   -1.85346900   -0.54016400
C      -0.33491400    0.15286400   -0.44114600
C      -1.30746700    0.24107500    0.72417800
C       0.00777800   -1.34888100   -0.67923800
C      -2.62220600    0.38456500    0.56683200
H      -0.82058100    0.52007600   -1.35293200
H      -0.85374300   -1.96452700   -0.98055000
H      -3.05346900    0.47848400   -0.41969100
H      -3.28009200    0.40713100    1.42575400
H       2.84825300   -0.61572500   -0.81825300
H       3.46538100    0.92572300   -0.35490100
H       0.21100300    0.25788600    1.85730400
""",
)

entry(
    index = 7,
    label = "C3H6N2O3_5",
    molecule = 
"""
1  O u0 p2 c0 {3,S} {8,S}
2  O u0 p2 c0 {7,S} {13,S}
3  O u0 p2 c0 {1,S} {4,S}
4  N u0 p1 c0 {3,S} {5,D}
5  N u0 p1 c0 {4,D} {14,S}
6  C u0 p0 c0 {7,S} {9,S} {10,S} {11,S}
7  C u0 p0 c0 {2,S} {6,S} {8,D}
8  C u0 p0 c0 {1,S} {7,D} {12,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.43986,0.0493129,-2.6815e-05,1.88753e-09,2.29874e-12,-30993.3,13.526], Tmin=(10,'K'), Tmax=(986.971,'K')),
            NASAPolynomial(coeffs=[8.10448,0.0378966,-2.08455e-05,5.54278e-09,-5.74377e-13,-32278.8,-10.7647], Tmin=(986.971,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-257.739,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (324.264,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 4, 'C-C': 1, 'C=C': 1, 'H-O': 1, 'O-O': 1, 'H-N': 1, 'C-O': 2, 'N=N': 1, 'N-O': 1}
1D rotors:
pivots: [1, 3], dihedral: [8, 1, 3, 4], rotor symmetry: 1, max scan energy: 6.56 kJ/mol
* Invalidated! pivots: [1, 8], dihedral: [3, 1, 8, 7], invalidation reason: Significant difference observed between consecutive conformers
* Invalidated! pivots: [2, 7], dihedral: [13, 2, 7, 6], invalidation reason: 
* Invalidated! pivots: [3, 4], dihedral: [1, 3, 4, 5], invalidation reason: 
pivots: [6, 7], dihedral: [9, 6, 7, 2], rotor symmetry: 3, max scan energy: 12.59 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.17590900   -1.12164000    3.54634400
O      -1.36930100   -0.35458600    1.33445300
O      -2.53204700   -2.73830400    0.04654300
N      -1.79478400   -2.67676800    1.03271700
N      -0.88846500   -3.48993000    1.38454000
C      -3.40897700   -1.22044500    2.23210200
C      -1.93208400   -1.43976400    1.96907900
C      -1.13709500   -1.78040500    3.24548700
H      -3.91185200   -1.05673300    1.27937700
H      -3.52696800   -0.33697300    2.86132200
H      -3.85947900   -2.08425400    2.72666000
H      -1.52204500   -2.60058400    3.87220600
H      -0.49917800   -0.22036700    1.74888500
H      -0.87292900   -4.23171200    0.67469200
""",
)

entry(
    index = 8,
    label = "C4H6N2O3_12",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {10,S} {11,S}
4  N u0 p1 c0 {6,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {4,S} {5,S}
7  C u0 p0 c0 {1,S} {14,T}
8  O u0 p2 c0 {2,S} {15,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 N u0 p1 c0 {7,T}
15 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.48499,0.0414367,0.000157317,-4.75306e-07,3.67637e-10,1877.94,13.8073], Tmin=(10,'K'), Tmax=(472.347,'K')),
            NASAPolynomial(coeffs=[7.12868,0.0572117,-4.08614e-05,1.34056e-08,-1.64429e-12,1013.53,-6.54499], Tmin=(472.347,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (15.5581,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (340.893,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 3, 'N-O': 1, 'C-C': 2, 'O-O': 1, 'C-O': 2, 'H-O': 1, 'C#N': 1, 'H-N': 2, 'C=C': 1}
1D rotors:
pivots: [1, 2], dihedral: [6, 1, 2, 4], rotor symmetry: 1, max scan energy: 19.34 kJ/mol
* Invalidated! pivots: [1, 6], dihedral: [2, 1, 6, 7], invalidation reason: Significant difference observed between consecutive conformers
pivots: [2, 4], dihedral: [1, 2, 4, 13], rotor symmetry: 1, max scan energy: 139.54 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 2 4 13 F
A 13 4 14 F
A 2 4 14 F
D 2 4 13 14 F
D 6 1 2 4 F
B 1 2 F
pivots: [3, 7], dihedral: [15, 3, 7, 6], rotor symmetry: 1, max scan energy: 39.66 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 10 6 7 8 F
pivots: [6, 7], dihedral: [1, 6, 7, 3], rotor symmetry: 1, max scan energy: 36.40 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 15 3 7 6 F


External symmetry: 1, optical isomers: 2

Geometry:
O       1.50813700    0.14548500   -0.20305700
O       2.98318700    0.82865700    0.22934200
O       0.62974800    2.36383700   -1.38109800
N       3.64184900    0.03662000    1.00814200
N       0.96146400    0.68614900    3.06578800
C       0.51860400    0.87155800    0.48416800
C       0.37657700    2.29775500   -0.05022100
C      -0.03435400    3.33989400    0.66583100
C       0.73061900    0.80138700    1.94235400
H      -0.40894200    0.32438100    0.25432700
H      -0.24988200    3.23930000    1.71991000
H      -0.16065400    4.30780000    0.19975300
H       3.98502300   -0.81509400    0.57083000
H       3.26653300   -0.05802000    1.95060500
H       1.13630600    1.56929500   -1.61191700
""",
)

entry(
    index = 9,
    label = "C3H5N2O3_6",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {8,S}
2  O u0 p2 c0 {7,S} {13,S}
3  O u0 p2 c0 {1,S} {4,S}
4  N u0 p1 c0 {3,S} {5,D}
5  N u1 p1 c0 {4,D}
6  C u0 p0 c0 {7,S} {9,S} {10,S} {11,S}
7  C u0 p0 c0 {2,S} {6,S} {8,D}
8  C u0 p0 c0 {1,S} {7,D} {12,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.33387,0.0826441,0.000386938,-4.67012e-06,1.12331e-08,-16142.5,14.2754], Tmin=(10,'K'), Tmax=(172.891,'K')),
            NASAPolynomial(coeffs=[9.27244,0.0376542,-2.44358e-05,7.52303e-09,-8.83705e-13,-16486,-7.94597], Tmin=(172.891,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-132.121,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (295.164,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 4, 'C-C': 1, 'C=C': 1, 'H-O': 1, 'O-O': 1, 'C-O': 2, 'N=N': 1, 'N-O': 1}
1D rotors:
* Invalidated! pivots: [1, 3], dihedral: [8, 1, 3, 4], invalidation reason: Significant difference observed between consecutive conformersBond ([[4, 12]]) broke during the scan.Significant difference observed between consecutive conformersThe rotor scan has a barrier of 228.92 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
pivots: [1, 8], dihedral: [3, 1, 8, 7], rotor symmetry: 1, max scan energy: 22.35 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 9 6 7 2 F
pivots: [2, 7], dihedral: [13, 2, 7, 6], rotor symmetry: 2, max scan energy: 19.98 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [1, 3, 4, 5], invalidation reason: Bond ([[4, 12]]) broke during the scan.Significant difference observed between consecutive conformersThe rotor scan has a barrier of 156.56 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
pivots: [6, 7], dihedral: [9, 6, 7, 2], rotor symmetry: 3, max scan energy: 5.45 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O      -0.86786600    1.55428100   -2.76916600
O       1.47839100    2.19825600   -0.09513900
O      -1.84387000    2.26982100   -3.31959900
N      -2.23750000    5.35377100   -1.94435400
N      -3.07049600    5.71248200   -2.55813600
C       1.29454200    0.22532600   -1.40315400
C       0.79517900    1.59904500   -1.10903200
C      -0.21428900    2.21339200   -1.75017500
H       1.20814800   -0.39875700   -0.50900700
H       2.35341700    0.26704500   -1.67423900
H       0.73355500   -0.23180600   -2.21573100
H      -0.58890400    3.20894000   -1.54952500
H       1.12772600    3.08244300    0.06541800
""",
)

entry(
    index = 10,
    label = "C4H5N2O3_2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {10,S}
3  C u0 p0 c0 {2,D} {12,S} {13,S}
4  N u0 p1 c0 {6,S} {7,S} {11,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {4,S} {5,S}
7  C u0 p0 c0 {4,S} {14,T}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 O u1 p2 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 N u0 p1 c0 {7,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.39607,0.0508431,5.65054e-06,-6.79497e-08,4.2754e-11,22732.1,14.2809], Tmin=(10,'K'), Tmax=(670.172,'K')),
            NASAPolynomial(coeffs=[6.53644,0.0499952,-3.25065e-05,9.85312e-09,-1.13332e-12,21909.3,-2.61104], Tmin=(670.172,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (188.928,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (328.422,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-N': 1, 'C#N': 1, 'C-C': 1, 'C-N': 1, 'C-H': 4, 'O-O': 1, 'C=C': 1, 'N-O': 1, 'C-O': 2}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [6, 1, 2, 4], invalidation reason: 
* Invalidated! pivots: [1, 6], dihedral: [2, 1, 6, 7], invalidation reason: 
* Invalidated! pivots: [2, 4], dihedral: [1, 2, 4, 9], invalidation reason: 
pivots: [6, 7], dihedral: [1, 6, 7, 3], rotor symmetry: 1, max scan energy: 54.90 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 1 2 4 12 F
D 3 7 8 13 F
D 6 1 2 4 F
D 2 1 6 7 F
* Invalidated! pivots: [7, 8], dihedral: [3, 7, 8, 13], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
O       1.28018100   -0.50263500    1.41315800
O       1.46843000    0.11943300    0.03859800
O       1.75037500    2.14740800    2.14703000
N       2.71785900    0.65562700   -0.03370800
N       4.62073400   -0.94307000   -0.34754400
C       0.26571200    0.23326300    2.04527500
C       0.68310200    1.63643500    2.50039500
C      -0.22716600    2.34931200    3.34865500
C       3.73094900   -0.22690600   -0.16804500
H      -0.62731300    0.30740100    1.40983200
H      -0.00700800   -0.37278400    2.91741800
H       2.82658900    1.38681800    0.67436100
H      -1.17641200    1.92814600    3.65875700
H       0.04745200    3.34175800    3.68208700
""",
)

entry(
    index = 11,
    label = "N1=NO1_7",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 N u0 p1 c0 {1,S} {3,D}
3 N u0 p1 c0 {1,S} {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98033,0.0012585,1.8886e-05,-4.394e-08,3.00131e-11,39639.8,5.35128], Tmin=(10,'K'), Tmax=(502.933,'K')),
            NASAPolynomial(coeffs=[4.04355,0.0047155,-3.23446e-06,1.03672e-09,-1.25873e-13,39583.4,4.5919], Tmin=(502.933,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (329.579,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'N-O': 2, 'N=N': 1}

External symmetry: 2, optical isomers: 1

Geometry:
O      -0.61700000   -0.71322700   -0.02380100
N      -0.13504700    0.74088100   -0.00554700
N       0.75204700   -0.02765400    0.02934800
""",
)

entry(
    index = 12,
    label = "C3H6O2_1",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,D}
4  O u0 p2 c0 {1,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84819,0.0182684,2.70888e-05,-3.90082e-08,1.33802e-11,-47398.1,11.8868], Tmin=(10,'K'), Tmax=(1061.72,'K')),
            NASAPolynomial(coeffs=[4.02231,0.0344055,-1.94351e-05,5.10232e-09,-5.14253e-13,-48381.6,6.57891], Tmin=(1061.72,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-394.074,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (245.277,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 2, 'C=O': 1, 'H-O': 1, 'C-O': 1}
1D rotors:
pivots: [1, 3], dihedral: [11, 1, 3, 5], rotor symmetry: 1, max scan energy: 29.88 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 10 4 5 3 F
pivots: [3, 5], dihedral: [1, 3, 5, 2], rotor symmetry: 1, max scan energy: 41.23 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 10 4 5 3 F
D 11 1 3 6 F
pivots: [4, 5], dihedral: [8, 4, 5, 2], rotor symmetry: 1, max scan energy: 0.57 kJ/mol (set as a FreeRotor)


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.73764200    1.82463200   -0.78778200
O      -0.51859800   -0.48589100   -1.19643000
C      -0.41246900    1.71757700   -0.34878500
C       1.64807300    0.13463300   -0.38658400
C       0.18622700    0.35997500   -0.68782500
H       0.21468800    2.50094100   -0.79889200
H      -0.34012500    1.84691200    0.74338600
H       2.24443200    0.53876000   -1.21169600
H       1.95841200    0.64978600    0.52571900
H       1.84965200   -0.93307700   -0.30647800
H      -1.96144600    0.94675700   -1.13584300
""",
)

entry(
    index = 13,
    label = "C4H4N2O2_13",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {5,S}
2  O u0 p2 c0 {1,S} {3,S}
3  N u0 p1 c0 {2,S} {11,S} {12,S}
4  N u0 p1 c0 {8,T}
5  C u0 p0 c0 {1,S} {7,D} {8,S}
6  C u0 p0 c0 {7,D} {9,S} {10,S}
7  C u0 p0 c0 {5,D} {6,D}
8  C u0 p0 c0 {4,T} {5,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.28185,0.0608736,-7.3558e-05,5.31708e-08,-1.65404e-11,44429.7,14.7129], Tmin=(10,'K'), Tmax=(739.9,'K')),
            NASAPolynomial(coeffs=[8.02425,0.0352354,-2.15815e-05,6.33851e-09,-7.16467e-13,43727.9,-6.73784], Tmin=(739.9,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (369.328,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 2, 'N-O': 1, 'O-O': 1, 'C#N': 1, 'H-N': 2, 'C=C': 2, 'C-O': 1, 'C-C': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [5, 1, 2, 3], invalidation reason: 
* Invalidated! pivots: [1, 5], dihedral: [2, 1, 5, 7], invalidation reason: 
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 11], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.51443000    0.57793900   -0.97191700
O      -1.58750400    0.45445200    0.45120500
N      -2.79580800    0.36381000    0.05821200
N       0.11979900   -2.76510300   -0.88987800
C       0.53006100   -0.19992000   -0.72778900
C       2.91343600    0.75927200   -0.18533900
C       1.73398100    0.27606200   -0.41880900
C       0.33234000   -1.63216300   -0.81503900
H       3.58758200    1.02989200   -0.99483800
H       3.27255200    0.91144700    0.82971700
H      -3.07304500   -0.52014300   -0.36552700
H      -3.21348400    1.20780400   -0.32922900
""",
)

entry(
    index = 14,
    label = "C2HN2O_4",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {5,S}
2 N u1 p1 c0 {4,D}
3 N u0 p1 c0 {5,T}
4 C u0 p0 c0 {1,S} {2,D} {6,S}
5 C u0 p0 c0 {1,S} {3,T}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67293,0.0308833,-6.56505e-05,8.62778e-08,-4.65142e-11,35561.7,11.4262], Tmin=(10,'K'), Tmax=(451.719,'K')),
            NASAPolynomial(coeffs=[5.59561,0.0138579,-9.11551e-06,2.84132e-09,-3.37202e-13,35388,3.67829], Tmin=(451.719,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (295.665,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (124.717,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C#N': 1, 'C-H': 1, 'C-O': 2, 'C=N': 1}
1D rotors:
pivots: [1, 4], dihedral: [5, 1, 4, 2], rotor symmetry: 1, max scan energy: 17.16 kJ/mol
pivots: [1, 5], dihedral: [4, 1, 5, 3], rotor symmetry: 1, max scan energy: 0.64 kJ/mol (set as a FreeRotor)


External symmetry: 1, optical isomers: 1

Geometry:
O       0.08987600   -0.71273300   -0.38967000
N      -0.88711600    1.22261700    0.53138900
N       2.40051600    0.08547800   -0.15407600
C      -0.98355800    0.08907900    0.02747700
C       1.30052200   -0.25121800   -0.24678900
H      -1.92024000   -0.43322300   -0.15727000
""",
)

entry(
    index = 15,
    label = "C4H5N2O3_15",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {12,D}
4  O u0 p2 c0 {1,S} {6,S}
5  C u0 p0 c0 {1,S} {13,T}
6  O u0 p2 c0 {4,S} {7,S}
7  N u1 p1 c0 {6,S} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 O u0 p2 c0 {3,D}
13 N u0 p1 c0 {5,T}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.2536,0.0717658,-0.000102124,1.0813e-07,-5.29965e-11,16781.4,15.1636], Tmin=(10,'K'), Tmax=(473.086,'K')),
            NASAPolynomial(coeffs=[5.84826,0.0498274,-3.25641e-05,1.01054e-08,-1.19555e-12,16535.9,4.58792], Tmin=(473.086,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (139.513,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 4, 'N-O': 1, 'C-C': 3, 'O-O': 1, 'C=O': 1, 'C#N': 1, 'H-N': 1, 'C-O': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [6, 1, 2, 4], invalidation reason: 
* Invalidated! pivots: [1, 6], dihedral: [2, 1, 6, 8], invalidation reason: 
* Invalidated! pivots: [2, 4], dihedral: [1, 2, 4, 14], invalidation reason: Another conformer for C4H5N2O3_15 exists which is 3.86 kJ/mol lower.
* Invalidated! pivots: [6, 8], dihedral: [1, 6, 8, 3], invalidation reason: 
* Invalidated! pivots: [7, 8], dihedral: [11, 7, 8, 3], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.66016300    2.90352100   -0.15435700
O      -1.23188900    2.95872300   -1.57061400
O      -0.55579800    1.47186700    2.82268500
N      -1.58314900    4.07700200   -2.15569000
N       1.23588800    4.04114400    1.19945600
C      -0.61359200    2.29428300    0.57837900
C      -2.60241700    1.00325400    1.65386100
C      -1.22049200    1.57208200    1.82944200
C       0.43343100    3.25635400    0.94307300
H      -0.16889500    1.49636100   -0.03210700
H      -3.32460100    1.81821500    1.55289900
H      -2.84774300    0.39264800    2.52122400
H      -2.66857600    0.41277700    0.73611100
H      -1.77398200    4.76181000   -1.41034200
""",
)

entry(
    index = 16,
    label = "CH2NO3_2",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {5,S} {7,S}
2 O u0 p2 c0 {3,S} {4,S}
3 O u1 p2 c0 {2,S}
4 N u0 p1 c0 {2,S} {5,D}
5 C u0 p0 c0 {1,S} {4,D} {6,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89646,0.00632711,8.92465e-05,-2.00518e-07,1.30179e-10,2062.74,10.2505], Tmin=(10,'K'), Tmax=(541.816,'K')),
            NASAPolynomial(coeffs=[5.11323,0.0203813,-1.34394e-05,4.30399e-09,-5.36393e-13,1592.74,2.00543], Tmin=(541.816,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (17.1148,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (149.66,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 1, 'N-O': 1, 'O-O': 1, 'H-O': 1, 'C=N': 1, 'C-O': 1}
1D rotors:
pivots: [1, 5], dihedral: [7, 1, 5, 4], rotor symmetry: 1, max scan energy: 74.29 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 2 4 5 F
D 3 2 4 5 F
pivots: [2, 4], dihedral: [3, 2, 4, 5], rotor symmetry: 1, max scan energy: 17.29 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O      -1.24991500   -0.18590400   -0.22149200
O       1.58613400   -0.05683000   -0.37264500
O       0.97860500   -0.90227900   -1.19162600
N       0.81416700    0.72801300    0.52212100
C      -0.46866700    0.58802600    0.50554100
H      -0.99551000    1.21928700    1.21574600
H      -0.65280700   -0.70005300   -0.81685300
""",
)

entry(
    index = 17,
    label = "C3H6O2_5",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  C u0 p0 c0 {2,D} {5,S} {9,S}
4  O u0 p2 c0 {2,S} {10,S}
5  O u0 p2 c0 {3,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87295,0.0106213,0.000121309,-3.09474e-07,2.54479e-10,-42071.2,10.6159], Tmin=(10,'K'), Tmax=(310.945,'K')),
            NASAPolynomial(coeffs=[1.48518,0.0413381,-2.68719e-05,8.23116e-09,-9.60815e-13,-41922.7,19.3462], Tmin=(310.945,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-349.796,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (245.277,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 4, 'C-O': 2, 'H-O': 2, 'C=C': 1, 'C-C': 1}
1D rotors:
pivots: [1, 4], dihedral: [10, 1, 4, 3], rotor symmetry: 1, max scan energy: 37.84 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 11 2 5 4 F
pivots: [2, 5], dihedral: [11, 2, 5, 4], rotor symmetry: 1, max scan energy: 23.47 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 10 1 4 5 F
pivots: [3, 4], dihedral: [6, 3, 4, 1], rotor symmetry: 3, max scan energy: 10.23 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.40173400    0.74427700   -1.62448200
O      -1.69565500   -1.34190600   -0.48104700
C       0.47928200    1.58667500    0.43209700
C      -0.31121400    0.53986300   -0.27674000
C      -0.90540500   -0.50401000    0.30830600
H       0.01913600    2.57055600    0.29717600
H       1.49169500    1.64050000    0.02023000
H       0.54443500    1.37456300    1.50021100
H      -0.88008900   -0.68494900    1.37572800
H      -0.95331900    0.02767800   -1.97067800
H      -1.43867900   -2.25553100   -0.32218700
""",
)

entry(
    index = 18,
    label = "CH2NO2_4",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {5,S}
2 O u1 p2 c0 {4,S}
3 N u0 p1 c0 {4,D} {6,S}
4 C u0 p0 c0 {1,S} {2,S} {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92123,0.0048201,6.80282e-05,-1.52791e-07,9.89708e-11,-22681.2,9.93252], Tmin=(10,'K'), Tmax=(541.126,'K')),
            NASAPolynomial(coeffs=[4.69203,0.0163037,-1.14306e-05,3.77732e-09,-4.72024e-13,-23016.2,4.36292], Tmin=(541.126,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-188.609,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (124.717,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'H-N': 1, 'C=N': 1, 'C-O': 2}
1D rotors:
pivots: [1, 4], dihedral: [5, 1, 4, 2], rotor symmetry: 1, max scan energy: 46.14 kJ/mol
pivots: [3, 4], dihedral: [6, 3, 4, 1], rotor symmetry: 1, max scan energy: 12.58 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.21368800   -0.40479700   -0.01774600
O      -0.97939000   -0.89716300    0.23506500
N      -0.35580500    1.15488100   -0.51715900
C      -0.09345300   -0.10939000   -0.03323300
H       1.29287900   -1.32732100    0.26555600
H      -1.07792000    1.58379100    0.06751700
""",
)

entry(
    index = 19,
    label = "C3H5O2_6",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  O u0 p2 c0 {3,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u1 p2 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86112,0.0124518,6.54403e-05,-1.39776e-07,9.11584e-11,-32690.9,10.3238], Tmin=(10,'K'), Tmax=(397.831,'K')),
            NASAPolynomial(coeffs=[1.55912,0.0355972,-2.18277e-05,6.46295e-09,-7.38636e-13,-32507.7,19.3078], Tmin=(397.831,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-271.814,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 4, 'C-O': 2, 'H-O': 1, 'C=C': 1, 'C-C': 1}
1D rotors:
* Invalidated! pivots: [1, 5], dihedral: [10, 1, 5, 4], invalidation reason: 
* Invalidated! pivots: [3, 4], dihedral: [6, 3, 4, 2], invalidation reason: 
* Invalidated! pivots: [4, 5], dihedral: [2, 4, 5, 1], invalidation reason: 


External symmetry: 1, optical isomers: 1

Geometry:
O      -0.02445000    0.26926300    1.65032900
O       0.46668400    1.96363800   -0.27203700
C       2.73945300    2.45326500    0.38182800
C       1.40572900    1.76292600    0.52166400
C       1.17351400    0.84022200    1.58852500
H       2.59433000    3.53598800    0.42047700
H       3.17044600    2.21732500   -0.59460400
H       3.44597500    2.16154800    1.16178000
H       1.87364300    0.55203600    2.36026100
H      -0.50547000    0.65073700    0.88176000
""",
)

entry(
    index = 20,
    label = "C3H5O2_7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  C u1 p0 c0 {2,D} {5,S}
4  O u0 p2 c0 {2,S} {9,S}
5  O u0 p2 c0 {3,S} {10,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85226,0.00977415,0.00013439,-3.29893e-07,2.37258e-10,-11555,11.0639], Tmin=(10,'K'), Tmax=(480.57,'K')),
            NASAPolynomial(coeffs=[4.58609,0.0316167,-2.10294e-05,6.73625e-09,-8.2103e-13,-11948.3,4.70327], Tmin=(480.57,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-96.1027,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (224.491,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 3, 'C-O': 2, 'H-O': 2, 'C=C': 1, 'C-C': 1}
1D rotors:
pivots: [1, 4], dihedral: [9, 1, 4, 3], rotor symmetry: 1, max scan energy: 21.89 kJ/mol
* Invalidated! pivots: [2, 5], dihedral: [10, 2, 5, 4], invalidation reason: 
pivots: [3, 4], dihedral: [6, 3, 4, 1], rotor symmetry: 3, max scan energy: 7.02 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.98138100   -1.50323100    0.08567200
O       1.57183700   -0.31283300   -2.20979900
C       0.36909400    0.42450400    0.49044700
C      -0.01069200   -0.68670800   -0.44035500
C       0.45842600   -0.84409500   -1.67627700
H       0.75642300    0.00468300    1.42435300
H       1.13376000    1.05794700    0.04225500
H      -0.50588900    1.03248700    0.73926300
H      -1.15849700   -2.20237200   -0.55564500
H       1.36255800    0.03661700   -3.08472800
""",
)

entry(
    index = 21,
    label = "C3H3O2_9",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,D}
2 O u0 p2 c0 {5,D}
3 C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
4 C u0 p0 c0 {1,D} {3,S} {5,S}
5 C u1 p0 c0 {2,D} {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67061,0.0349448,-0.000121403,2.89152e-07,-2.43217e-10,-16181.5,9.19407], Tmin=(10,'K'), Tmax=(405.822,'K')),
            NASAPolynomial(coeffs=[2.97028,0.0238966,-1.4216e-05,4.07153e-09,-4.51184e-13,-15976.8,13.7624], Tmin=(405.822,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-134.551,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (174.604,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 3, 'C-C': 2, 'C=O': 2}
1D rotors:
pivots: [3, 4], dihedral: [6, 3, 4, 1], rotor symmetry: 3, max scan energy: 3.47 kJ/mol
pivots: [4, 5], dihedral: [1, 4, 5, 2], rotor symmetry: 1, max scan energy: 0.67 kJ/mol (set as a FreeRotor)


External symmetry: 1, optical isomers: 1

Geometry:
O      -0.84012900    0.60291800   -1.37740900
O      -1.99398500    1.19176300    1.63309100
C       0.96487500   -0.09441600    0.13110500
C      -0.39606700    0.45977200   -0.21682700
C      -1.23495600    0.84677300    0.82926400
H       1.73495000    0.52688800   -0.33362700
H       1.14120800   -0.12907700    1.20929100
H       1.05529300   -1.10533300   -0.27494800
""",
)

entry(
    index = 22,
    label = "C3H4O2_8",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {9,S}
2 O u0 p2 c0 {5,D}
3 C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
4 C u0 p0 c0 {1,S} {3,S} {5,D}
5 C u0 p0 c0 {2,D} {4,D}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85221,0.0123937,0.000143843,-5.29465e-07,5.68769e-10,-24740,10.7207], Tmin=(10,'K'), Tmax=(327.333,'K')),
            NASAPolynomial(coeffs=[4.74328,0.0241919,-1.41845e-05,4.12158e-09,-4.70755e-13,-24919.8,5.56034], Tmin=(327.333,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-205.675,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (199.547,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 3, 'H-O': 1, 'C=O': 1, 'C=C': 1, 'C-C': 1, 'C-O': 1}
1D rotors:
pivots: [1, 4], dihedral: [9, 1, 4, 3], rotor symmetry: 1, max scan energy: 13.54 kJ/mol
pivots: [3, 4], dihedral: [6, 3, 4, 1], rotor symmetry: 3, max scan energy: 9.32 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.53585600    0.21783800   -0.33198000
O       0.10218100    0.88758100    2.64699300
C      -0.87422500   -0.44052400   -0.47654700
C       0.27631000    0.15919300    0.27535100
C       0.18813500    0.55334800    1.53187300
H      -0.61709600   -1.44875600   -0.81761700
H      -1.12706300    0.16005400   -1.35883800
H      -1.76954400   -0.50785200    0.14614700
H       1.54456600    0.97596400   -0.92869500
""",
)

entry(
    index = 23,
    label = "CHO3_0",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {5,S}
2 O u1 p2 c0 {4,S}
3 O u0 p2 c0 {4,D}
4 C u0 p0 c0 {1,S} {2,S} {3,D}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.06415,-0.00635065,9.21442e-05,-1.69536e-07,9.81103e-11,-45959.2,8.8365], Tmin=(10,'K'), Tmax=(573.543,'K')),
            NASAPolynomial(coeffs=[3.36423,0.0159075,-1.15137e-05,3.77655e-09,-4.6014e-13,-46164.7,9.33256], Tmin=(573.543,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-382.139,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (103.931,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'H-O': 1, 'C=O': 1}
1D rotors:
pivots: [1, 4], dihedral: [5, 1, 4, 2], rotor symmetry: 2, max scan energy: 28.91 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O       0.80139300   -0.25005100    0.57204800
O      -1.18075500   -1.08124900   -0.02648600
O      -0.65233600    0.81687000   -0.81103300
C      -0.33997100   -0.15190700   -0.09739700
H       1.32733000    0.54652000    0.40648200
""",
)

entry(
    index = 24,
    label = "CH2O3_1",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {5,S}
2 O u0 p2 c0 {4,S} {6,S}
3 O u0 p2 c0 {4,D}
4 C u0 p0 c0 {1,S} {2,S} {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94645,0.00297001,6.1104e-05,-1.12333e-07,6.09066e-11,-75283.5,6.84974], Tmin=(10,'K'), Tmax=(618.389,'K')),
            NASAPolynomial(coeffs=[3.11321,0.0215781,-1.60958e-05,5.45988e-09,-6.8874e-13,-75433.1,8.42566], Tmin=(618.389,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-625.967,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (124.717,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 2, 'C=O': 1, 'C-O': 2}
1D rotors:
pivots: [1, 4], dihedral: [5, 1, 4, 2], rotor symmetry: 1, max scan energy: 44.59 kJ/mol
pivots: [2, 4], dihedral: [6, 2, 4, 1], rotor symmetry: 1, max scan energy: 44.59 kJ/mol


External symmetry: 2, optical isomers: 1

Geometry:
O      -0.58867600    1.47571300    0.71798900
O       1.24281300    0.44057100    0.15797500
O      -0.74356600   -0.57003000   -0.23875200
C      -0.09472800    0.35609000    0.17137000
H      -1.54938900    1.37810200    0.71022700
H       1.56053100   -0.37959700   -0.24069100
""",
)

entry(
    index = 25,
    label = "C2H2NO3_2",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {5,S} {6,S}
2 O u0 p2 c0 {5,S} {8,S}
3 O u0 p2 c0 {5,D}
4 N u1 p1 c0 {6,D}
5 C u0 p0 c0 {1,S} {2,S} {3,D}
6 C u0 p0 c0 {1,S} {4,D} {7,S}
7 H u0 p0 c0 {6,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8422,0.0104997,0.000122069,-3.07184e-07,2.20917e-10,-37291.3,11.1433], Tmin=(10,'K'), Tmax=(485.954,'K')),
            NASAPolynomial(coeffs=[4.84694,0.0297553,-2.2332e-05,7.47584e-09,-9.24824e-13,-37713.9,3.67692], Tmin=(485.954,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-310.089,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (170.447,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C=O': 1, 'C-H': 1, 'C-O': 3, 'C=N': 1}
1D rotors:
pivots: [1, 5], dihedral: [6, 1, 5, 2], rotor symmetry: 1, max scan energy: 37.91 kJ/mol
pivots: [1, 6], dihedral: [5, 1, 6, 4], rotor symmetry: 1, max scan energy: 19.76 kJ/mol
pivots: [2, 5], dihedral: [8, 2, 5, 1], rotor symmetry: 1, max scan energy: 43.46 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O       0.28665500   -0.67981200   -0.29158100
O       1.35503400    0.07775100    1.43488200
O      -0.41075800    1.26923000    0.67007100
N      -0.85675300   -1.46984900   -2.12157200
C       0.33256600    0.33071700    0.61853900
C      -0.71924800   -0.59989600   -1.23911200
H      -1.36980200    0.27314500   -1.14985500
H       1.38229100    0.79870000    2.07864300
""",
)

entry(
    index = 26,
    label = "C4H8N2O2_3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  N u0 p1 c0 {7,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {7,S}
6  C u0 p0 c0 {1,S} {16,T}
7  O u0 p2 c0 {4,S} {5,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 N u0 p1 c0 {6,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.58973,0.0340895,0.00018734,-5.87472e-07,5.15095e-10,4684.49,12.5203], Tmin=(10,'K'), Tmax=(394.524,'K')),
            NASAPolynomial(coeffs=[4.26795,0.0606592,-4.08433e-05,1.29926e-08,-1.56823e-12,4370.69,6.58028], Tmin=(394.524,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (38.9604,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (365.837,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-N': 2, 'C-H': 6, 'C-C': 3, 'C-O': 1, 'N-O': 1, 'O-O': 1, 'C#N': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [5, 1, 2, 3], invalidation reason: The rotor scan has a barrier of 57.20 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
pivots: [1, 5], dihedral: [2, 1, 5, 6], rotor symmetry: 1, max scan energy: 31.89 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 5 1 2 3 F
pivots: [2, 3], dihedral: [1, 2, 3, 15], rotor symmetry: 1, max scan energy: 88.71 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 2 3 16 F
D 2 3 15 16 F
B 1 2 F
pivots: [5, 6], dihedral: [1, 5, 6, 9], rotor symmetry: 3, max scan energy: 12.41 kJ/mol
pivots: [5, 7], dihedral: [1, 5, 7, 12], rotor symmetry: 3, max scan energy: 13.26 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.14682600    0.15846600    0.58569000
O       1.76571800   -1.02651400   -0.24397800
N       2.37647200   -0.55940600   -1.33342100
N      -0.97209200    0.28665200   -2.01489300
C      -0.26884000    0.05393700    0.51928100
C      -0.77410300    1.27053600    1.31279600
C      -0.77950900   -1.26797700    1.10798300
C      -0.69189900    0.18056000   -0.90118600
H      -0.38516200    2.19418300    0.88355300
H      -0.43037300    1.18465800    2.34460300
H      -1.86538100    1.30170800    1.29865400
H      -0.45050000   -1.33636500    2.14663200
H      -0.37547800   -2.11337300    0.55296400
H      -1.87048600   -1.31030900    1.07357500
H       3.14547200    0.06232600   -1.09408700
H       1.72033200   -0.13789500   -1.98883000
""",
)

entry(
    index = 27,
    label = "C3H7NO3_4",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {12,D}
4  N u0 p1 c0 {6,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {4,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 O u0 p2 c0 {3,D}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71786,0.0374224,1.06178e-05,-3.17363e-08,1.18587e-11,-22189.3,13.3277], Tmin=(10,'K'), Tmax=(1115.13,'K')),
            NASAPolynomial(coeffs=[9.61204,0.0387621,-2.14258e-05,5.49991e-09,-5.42429e-13,-24901.7,-22.0183], Tmin=(1115.13,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-184.459,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (315.95,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-N': 2, 'C=O': 1, 'C-H': 5, 'C-C': 2, 'C-O': 1, 'N-O': 1, 'O-O': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [5, 1, 2, 4], invalidation reason: The rotor scan has a barrier of 47.77 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
pivots: [1, 5], dihedral: [2, 1, 5, 7], rotor symmetry: 1, max scan energy: 60.96 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 12 6 7 3 F
D 1 5 7 6 F
D 5 1 2 4 F
pivots: [2, 4], dihedral: [1, 2, 4, 13], rotor symmetry: 1, max scan energy: 89.85 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 2 4 13 14 F
D 12 6 7 3 F
D 2 1 5 8 F
D 5 1 2 4 F
B 1 2 F
pivots: [5, 7], dihedral: [1, 5, 7, 3], rotor symmetry: 1, max scan energy: 48.03 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 1 5 7 F
D 2 1 5 7 F
D 12 6 7 3 F
D 5 1 2 4 F
pivots: [6, 7], dihedral: [10, 6, 7, 3], rotor symmetry: 1, max scan energy: 1.03 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       0.15800400    0.57140200    2.62591900
O      -0.84782300   -0.12319400    3.59634800
O      -2.01232500    0.40586500    0.89406700
N      -1.88295800    0.69343400    3.83494900
C       0.22349200   -0.24946500    1.49975100
C      -0.95735800   -1.10224700   -0.62778700
C      -1.02518800   -0.23674700    0.61443100
H       1.07308300    0.12255600    0.91041000
H       0.45879200   -1.29148000    1.76440900
H       0.00417700   -1.00553100   -1.13919200
H      -1.06643400   -2.15321000   -0.33895400
H      -1.77087600   -0.83789700   -1.30188700
H      -1.57228400    1.53174800    4.32271200
H      -2.34807000    0.91804700    2.95477400
""",
)

entry(
    index = 28,
    label = "C4H7N2O2_5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  O u0 p2 c0 {1,S} {6,S}
5  C u0 p0 c0 {1,S} {14,T}
6  O u0 p2 c0 {4,S} {7,S}
7  N u1 p1 c0 {6,S} {15,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 N u0 p1 c0 {5,T}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.03951,0.0879832,-0.000182818,2.57382e-07,-1.46708e-10,18854.6,14.4685], Tmin=(10,'K'), Tmax=(504.186,'K')),
            NASAPolynomial(coeffs=[6.71802,0.0474098,-2.82231e-05,8.16152e-09,-9.16115e-13,18628.4,0.6765], Tmin=(504.186,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (156.717,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (357.522,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-N': 1, 'C-H': 6, 'C-C': 3, 'C-O': 1, 'N-O': 1, 'O-O': 1, 'C#N': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [5, 1, 2, 3], invalidation reason: 
* Invalidated! pivots: [1, 5], dihedral: [2, 1, 5, 6], invalidation reason: 
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 15], invalidation reason: 
* Invalidated! pivots: [5, 6], dihedral: [1, 5, 6, 9], invalidation reason: 
* Invalidated! pivots: [5, 7], dihedral: [1, 5, 7, 12], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
O       0.13012100   -1.56700700    0.95301200
O       1.80321600   -1.91362600   -0.80381600
N       2.85974900   -1.36192600   -0.66958900
N       1.25653600    1.36021200   -0.04742900
C      -0.57060100   -0.46452900    0.51433200
C      -1.43125600   -0.77005200   -0.72538100
C      -1.45178700   -0.03147200    1.71990700
C       0.41122500    0.61518800    0.20310000
H      -2.12940100   -1.57007200   -0.47389600
H      -1.98945100    0.11307400   -1.04509500
H      -0.79443700   -1.10517200   -1.54408200
H      -0.82902900    0.16926800    2.59111600
H      -2.14912600   -0.83713300    1.95053200
H      -2.00771000    0.87014800    1.45449800
H       2.70794200   -0.37780200   -0.31337000
""",
)

entry(
    index = 29,
    label = "C4H7N2O2_6",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {11,S} {12,S}
4  N u0 p1 c0 {7,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {7,S}
6  C u0 p0 c0 {1,S} {15,T}
7  O u0 p2 c0 {4,S} {5,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 N u0 p1 c0 {6,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61849,0.0496266,0.000670403,-6.16725e-06,1.51436e-08,5065.22,12.8258], Tmin=(10,'K'), Tmax=(154.088,'K')),
            NASAPolynomial(coeffs=[6.6411,0.0461846,-2.6409e-05,7.27123e-09,-7.75329e-13,4883,1.00642], Tmin=(154.088,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (46.4464,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (357.522,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-N': 2, 'C-H': 5, 'C-C': 3, 'C-O': 1, 'N-O': 1, 'O-O': 1, 'C#N': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [5, 1, 2, 3], invalidation reason: 
* Invalidated! pivots: [1, 5], dihedral: [2, 1, 5, 6], invalidation reason: Another conformer for C4H7N2O2_6 exists which is 2.62 kJ/mol lower.
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 14], invalidation reason: 
* Invalidated! pivots: [5, 6], dihedral: [1, 5, 6, 9], invalidation reason: 
* Invalidated! pivots: [5, 7], dihedral: [1, 5, 7, 12], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.47122100    1.44684800   -1.97754900
O       1.61054000   -2.01818400    0.05872600
N       2.44800400   -1.53889000    0.89760600
N       1.22416900    1.26003600    1.02316600
C      -0.71562100    0.88479600   -0.68089200
C      -1.33649500   -0.49206600   -0.63253300
C      -1.45513600    2.07365600   -1.15460400
C       0.36989200    1.10767400    0.26369000
H      -0.56350200   -1.25119600   -0.75695800
H      -2.07680100   -0.57747400   -1.42930000
H      -1.82570600   -0.65559600    0.33127300
H      -2.48708900    1.93580300   -1.46722500
H      -1.19385800    3.05965600   -0.78080600
H       3.31878500   -2.03871900    1.05808200
H       2.36175400   -0.56182800    1.18026500
""",
)

entry(
    index = 30,
    label = "C3H6NO3_7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {12,D}
4  O u0 p2 c0 {1,S} {5,S}
5  O u0 p2 c0 {4,S} {6,S}
6  N u1 p1 c0 {5,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 O u0 p2 c0 {3,D}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.23134,0.0700856,-0.000133197,1.82312e-07,-1.05369e-10,-3514.15,13.443], Tmin=(10,'K'), Tmax=(482.653,'K')),
            NASAPolynomial(coeffs=[5.81258,0.0423002,-2.69757e-05,8.14825e-09,-9.41645e-13,-3688.85,3.64176], Tmin=(482.653,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-29.2547,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (286.849,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-N': 1, 'C=O': 1, 'C-H': 5, 'C-C': 2, 'C-O': 1, 'N-O': 1, 'O-O': 1}
1D rotors:
pivots: [1, 2], dihedral: [5, 1, 2, 4], rotor symmetry: 1, max scan energy: 34.10 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 12 6 7 3 F
D 1 2 4 13 F
B 1 2 F
pivots: [1, 5], dihedral: [2, 1, 5, 7], rotor symmetry: 1, max scan energy: 40.40 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 8 5 7 6 F
D 12 6 7 3 F
D 1 2 4 13 F
D 5 1 2 4 F
B 1 2 F
pivots: [2, 4], dihedral: [1, 2, 4, 13], rotor symmetry: 1, max scan energy: 89.84 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 2 4 13 F
D 2 1 5 8 F
D 8 5 7 6 F
D 5 1 2 4 F
B 1 2 F
pivots: [5, 7], dihedral: [1, 5, 7, 3], rotor symmetry: 1, max scan energy: 24.26 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 12 6 7 3 F
D 2 1 5 8 F
D 1 2 4 13 F
D 5 1 2 4 F
B 1 2 F
pivots: [6, 7], dihedral: [10, 6, 7, 3], rotor symmetry: 3, max scan energy: 4.40 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.74088300   -0.85222600   -2.06327400
O      -1.51483800   -0.46109600   -0.78345800
O       2.24381400   -1.83874400   -0.34985400
N      -2.63231300    0.12736300   -1.07061200
C       0.27352600   -1.74159100   -1.65035500
C       1.60775700    0.39213900   -0.96794600
C       1.46424600   -1.10887900   -0.91406000
H       0.65096300   -2.16438000   -2.58980700
H      -0.12709100   -2.56484000   -1.05062600
H       1.54292500    0.75048700   -1.99905600
H       0.78283100    0.86070200   -0.42363500
H       2.55828500    0.67953100   -0.52130200
H      -2.82993100   -0.04631500   -2.06727300
""",
)

entry(
    index = 31,
    label = "C4H8N2O3_9",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  N u0 p1 c0 {7,S} {8,S} {15,S}
5  O u0 p2 c0 {1,S} {7,S}
6  C u0 p0 c0 {1,S} {16,T}
7  O u0 p2 c0 {4,S} {5,S}
8  O u0 p2 c0 {4,S} {17,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 N u0 p1 c0 {6,T}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49316,0.0474113,0.000373724,-1.81215e-06,2.38754e-09,-1800.15,13.4749], Tmin=(10,'K'), Tmax=(278.322,'K')),
            NASAPolynomial(coeffs=[7.16565,0.0593321,-3.92255e-05,1.2245e-08,-1.45889e-12,-2255.18,-4.04764], Tmin=(278.322,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-14.9098,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (382.466,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-N': 1, 'H-O': 1, 'C-H': 6, 'C-C': 3, 'C-O': 1, 'N-O': 2, 'O-O': 1, 'C#N': 1}
1D rotors:
pivots: [1, 2], dihedral: [6, 1, 2, 4], rotor symmetry: 1, max scan energy: 47.78 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 2 1 6 7 F
B 1 2 F
pivots: [1, 6], dihedral: [2, 1, 6, 7], rotor symmetry: 1, max scan energy: 19.23 kJ/mol
pivots: [2, 4], dihedral: [1, 2, 4, 3], rotor symmetry: 1, max scan energy: 67.34 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 6 1 2 4 F
D 2 1 6 9 F
pivots: [3, 4], dihedral: [17, 3, 4, 2], rotor symmetry: 1, max scan energy: 35.49 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 6 1 2 4 F
pivots: [6, 7], dihedral: [1, 6, 7, 10], rotor symmetry: 3, max scan energy: 12.43 kJ/mol
pivots: [6, 8], dihedral: [1, 6, 8, 13], rotor symmetry: 3, max scan energy: 13.37 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       2.81001900    0.24423800    2.84521700
O       2.51631700    1.75294000    3.18643600
O       1.60064400    1.23553100    5.22414900
N       1.44853300    1.84578100    3.95873800
N       4.85976400    0.56500900    5.55380500
C       4.19505800    0.00855200    3.06385900
C       4.35147700   -1.50049800    2.80725800
C       5.06698300    0.84521000    2.11510000
C       4.55578600    0.31427700    4.47080300
H       4.05537500   -1.71690400    1.77972800
H       3.71932700   -2.06874200    3.48964000
H       5.39194400   -1.79770800    2.95121200
H       4.90230100    1.90911600    2.28314000
H       4.79523400    0.60305300    1.08588200
H       6.12574700    0.62556600    2.26876700
H       0.66742200    1.33568000    3.54540400
H       2.14748500    1.85528600    5.72541500
""",
)

entry(
    index = 32,
    label = "C4H7N2O3_10",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {6,S} {8,S}
2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {12,D}
4  C u0 p0 c0 {1,S} {13,D} {14,S}
5  N u0 p1 c0 {7,S} {15,S} {16,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {5,S} {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 O u0 p2 c0 {3,D}
13 N u1 p1 c0 {4,D}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.33536,0.0648078,-4.16615e-05,1.22264e-08,-1.33717e-12,8515.43,14.2743], Tmin=(10,'K'), Tmax=(1777.75,'K')),
            NASAPolynomial(coeffs=[30.3627,0.0113001,-2.67709e-06,-8.16706e-11,6.8645e-14,-2248.43,-134.914], Tmin=(1777.75,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (70.6575,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (361.68,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-N': 2, 'C=O': 1, 'C-H': 5, 'C-C': 3, 'C-O': 1, 'C=N': 1, 'N-O': 1, 'O-O': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [6, 1, 2, 4], invalidation reason: The rotor scan has a barrier of 63.80 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
pivots: [1, 6], dihedral: [2, 1, 6, 8], rotor symmetry: 1, max scan energy: 64.30 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 9 6 8 3 F
D 11 7 8 6 F
D 1 6 9 5 F
D 6 1 2 4 F
pivots: [2, 4], dihedral: [1, 2, 4, 15], rotor symmetry: 1, max scan energy: 122.47 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 2 4 15 F
A 15 4 16 F
A 2 4 16 F
D 2 4 15 16 F
D 10 6 9 5 F
D 6 1 2 4 F
D 10 6 8 3 F
B 1 2 F
pivots: [6, 8], dihedral: [1, 6, 8, 3], rotor symmetry: 1, max scan energy: 35.54 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 13 7 8 3 F
pivots: [6, 9], dihedral: [1, 6, 9, 5], rotor symmetry: 1, max scan energy: 33.09 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 6 1 2 4 F
pivots: [7, 8], dihedral: [11, 7, 8, 3], rotor symmetry: 3, max scan energy: 5.01 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.95420200    1.28445300    0.81876100
O      -3.71860300   -0.13197800    1.05910400
O      -0.02954000   -0.32248900   -0.45931400
N      -4.96824900   -0.04346700    0.66763700
N      -3.62911400    0.53527500   -1.87149000
C      -1.96222200    1.04755400   -0.11842900
C      -0.69801100   -0.12338500    1.83582000
C      -0.80572200    0.12154400    0.35324000
C      -2.44473900    0.59420200   -1.51435700
H      -1.48805000    2.03194100   -0.27123200
H      -0.73714100    0.82083700    2.38486600
H      -1.55767700   -0.70976700    2.17037100
H       0.22852600   -0.65587900    2.04493000
H      -1.62458300    0.30460800   -2.18762900
H      -5.05083000    0.10294400   -0.34072700
H      -5.51604100    0.60029200    1.23435500
""",
)

entry(
    index = 33,
    label = "C4H7N2O3_12",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {4,D} {10,S}
3  C u0 p0 c0 {1,S} {8,D} {11,S}
4  C u0 p0 c0 {2,D} {12,S} {13,S}
5  N u0 p1 c0 {7,S} {14,S} {15,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {5,S} {6,S}
8  N u0 p1 c0 {3,D} {16,S}
9  H u0 p0 c0 {1,S}
10 O u1 p2 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.48503,0.0683977,-4.84416e-05,1.45413e-08,-1.18635e-12,12639,14.7056], Tmin=(10,'K'), Tmax=(1268.19,'K')),
            NASAPolynomial(coeffs=[19.0623,0.0298409,-1.53456e-05,3.7188e-09,-3.49138e-13,7837.53,-67.4998], Tmin=(1268.19,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (105.11,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (357.522,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'H-N': 3, 'C-H': 4, 'C-C': 2, 'C-O': 2, 'C=N': 1, 'N-O': 1, 'O-O': 1}
1D rotors:
pivots: [1, 2], dihedral: [6, 1, 2, 4], rotor symmetry: 1, max scan energy: 23.30 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 2 1 6 7 F
pivots: [1, 6], dihedral: [2, 1, 6, 7], rotor symmetry: 1, max scan energy: 39.44 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 7 6 8 5 F
D 1 6 7 3 F
D 6 1 2 4 F
pivots: [2, 4], dihedral: [1, 2, 4, 14], rotor symmetry: 1, max scan energy: 96.20 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 2 4 15 F
D 2 4 14 15 F
D 2 1 6 8 F
D 6 1 2 4 F
B 1 2 F
pivots: [6, 7], dihedral: [1, 6, 7, 3], rotor symmetry: 1, max scan energy: 26.94 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 2 1 6 7 F
D 6 1 2 4 F
pivots: [6, 8], dihedral: [1, 6, 8, 5], rotor symmetry: 1, max scan energy: 20.67 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 1 6 7 3 F
pivots: [7, 9], dihedral: [3, 7, 9, 12], rotor symmetry: 2, max scan energy: 51.21 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 7 9 12 13 F
D 6 1 2 4 F


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.70104300   -0.22271300    0.24983800
O      -1.08558300   -1.21631700   -0.93539700
O       2.75203900    0.57355800   -0.36080100
N      -2.31056300   -1.66125200   -0.73855900
N      -0.75362400    2.45704700    0.94277100
C       0.36841100    0.55330200   -0.22338200
C       1.76575300   -0.00960000    0.09915000
C       0.24103600    1.97550300    0.33232400
C       1.87659300   -1.16551000    0.93006100
H       0.31303700    0.63046300   -1.31838200
H       1.12445000    2.59327000    0.15815300
H       1.00229800   -1.65256800    1.33737800
H       2.86687500   -1.54699700    1.14403300
H      -3.00585800   -0.91769100   -0.76931600
H      -2.38863900   -2.24016500    0.09527900
H      -1.48555700    1.74380500    1.02474300
""",
)

entry(
    index = 34,
    label = "C4H6N2O3_13",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {12,D}
4  N u0 p1 c0 {6,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {4,S} {5,S}
7  C u0 p0 c0 {1,S} {15,T}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 O u0 p2 c0 {3,D}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 N u0 p1 c0 {7,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.33302,0.0640776,-5.12979e-05,2.19197e-08,-3.99611e-12,-3305.25,13.7376], Tmin=(10,'K'), Tmax=(1129.68,'K')),
            NASAPolynomial(coeffs=[8.5119,0.04574,-2.6949e-05,7.55036e-09,-8.16144e-13,-4475.34,-11.8789], Tmin=(1129.68,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-27.5526,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (345.051,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-N': 2, 'C=O': 1, 'C-H': 4, 'C-C': 3, 'C-O': 1, 'N-O': 1, 'O-O': 1, 'C#N': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [6, 1, 2, 4], invalidation reason: The rotor scan has a barrier of 44.33 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
pivots: [1, 6], dihedral: [2, 1, 6, 8], rotor symmetry: 1, max scan energy: 54.00 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 13 7 8 3 F
D 1 6 8 7 F
D 6 1 2 4 F
pivots: [2, 4], dihedral: [1, 2, 4, 14], rotor symmetry: 1, max scan energy: 126.22 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 2 4 15 F
D 2 4 14 15 F
D 2 1 6 9 F
D 1 6 8 7 F
D 6 1 2 4 F
B 1 2 F
* Invalidated! pivots: [6, 8], dihedral: [1, 6, 8, 3], invalidation reason: The rotor scan has a barrier of 46.07 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
pivots: [7, 8], dihedral: [11, 7, 8, 3], rotor symmetry: 3, max scan energy: 2.71 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.05198300   -1.29338300    1.83496900
O      -2.53221800   -0.92601800    2.36931100
O      -2.14641100   -0.48293800   -0.54106500
N      -3.41526600   -1.71495000    1.80683900
N       2.02991500   -0.22061600    1.16370500
C      -0.58794400   -0.11573000    1.24695800
C      -0.52454200    1.21092000   -1.01250300
C      -1.18042900    0.14094500   -0.17736100
C       0.87982300   -0.17212400    1.21987200
H      -0.87370600    0.75873700    1.85457100
H      -0.30859600    2.10227400   -0.41651200
H      -1.17089400    1.46436300   -1.85122700
H       0.43450700    0.84244900   -1.38947900
H      -3.43356600   -1.59510200    0.79380300
H      -3.32882800   -2.68273800    2.11047200
""",
)

entry(
    index = 35,
    label = "C4H6N2O3_14",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,D} {7,S}
3  C u0 p0 c0 {2,D} {5,S} {8,S}
4  N u0 p1 c0 {6,S} {12,S} {13,S}
5  O u0 p2 c0 {3,S} {6,S}
6  O u0 p2 c0 {4,S} {5,S}
7  O u0 p2 c0 {2,S} {15,S}
8  C u0 p0 c0 {3,S} {14,T}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 N u0 p1 c0 {8,T}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.56244,0.0499249,0.000330931,-2.34207e-06,4.35392e-09,-6328.6,13.8663], Tmin=(10,'K'), Tmax=(200.241,'K')),
            NASAPolynomial(coeffs=[5.67638,0.0532217,-3.47904e-05,1.09216e-08,-1.312e-12,-6504.53,4.78846], Tmin=(200.241,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-52.3374,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (357.522,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'H-N': 2, 'H-O': 1, 'C-H': 3, 'C-C': 2, 'C-O': 2, 'N-O': 1, 'O-O': 1, 'C#N': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [8, 1, 2, 4], invalidation reason: 
* Invalidated! pivots: [1, 8], dihedral: [2, 1, 8, 7], invalidation reason: 
* Invalidated! pivots: [2, 4], dihedral: [1, 2, 4, 13], invalidation reason: 
* Invalidated! pivots: [3, 7], dihedral: [15, 3, 7, 6], invalidation reason: 
* Invalidated! pivots: [6, 7], dihedral: [10, 6, 7, 3], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
O       0.98428300   -0.03884600   -0.81979000
O       1.22289300   -1.48788800   -2.01059000
O      -1.59915600    0.32544100   -1.04338500
N       2.43311400   -1.51316200   -2.40933300
N       1.30738600   -1.64418200    2.19045500
C      -2.17025200   -0.56965500    1.09041300
C      -1.14200900   -0.24002000    0.07250100
C       0.22610500   -0.43417700    0.16923500
C       0.80962900   -1.10466600    1.29638600
H      -2.90221900   -1.26397600    0.66585400
H      -1.72311100   -1.01828300    1.97617600
H      -2.71241900    0.33645800    1.37832800
H       3.13591700   -1.79189100   -1.72631200
H       2.71378500   -0.80458500   -3.08513300
H      -0.80593700    0.47858900   -1.59579000
""",
)

entry(
    index = 36,
    label = "C4H5N2O3_16",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,D} {5,S}
3  C u0 p0 c0 {2,D} {4,S} {6,S}
4  O u0 p2 c0 {3,S} {7,S}
5  O u0 p2 c0 {2,S} {13,S}
6  C u0 p0 c0 {3,S} {12,T}
7  O u0 p2 c0 {4,S} {8,S}
8  N u1 p1 c0 {7,S} {14,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 N u0 p1 c0 {6,T}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53002,0.0580632,0.00046572,-4.25784e-06,9.6532e-09,-7097.57,13.7782], Tmin=(10,'K'), Tmax=(171.046,'K')),
            NASAPolynomial(coeffs=[6.96997,0.0460419,-2.89015e-05,8.7065e-09,-1.00867e-12,-7315.34,0.33084], Tmin=(171.046,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-57.2537,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'H-N': 1, 'H-O': 1, 'C-H': 3, 'C-C': 2, 'C-O': 2, 'N-O': 1, 'O-O': 1, 'C#N': 1}
1D rotors:
* Invalidated! pivots: [1, 3], dihedral: [8, 1, 3, 4], invalidation reason: 
* Invalidated! pivots: [1, 8], dihedral: [3, 1, 8, 7], invalidation reason: 
* Invalidated! pivots: [2, 7], dihedral: [13, 2, 7, 6], invalidation reason: 
* Invalidated! pivots: [3, 4], dihedral: [1, 3, 4, 14], invalidation reason: 
* Invalidated! pivots: [6, 7], dihedral: [10, 6, 7, 2], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
O       1.43174900   -1.03042700    1.26501600
O      -0.27388200    0.13280600   -0.55678700
O       3.14019300   -0.34951500   -1.63880200
N       2.19562700   -0.94232300   -1.20151200
N      -0.21167800   -0.43935300    4.18228200
C      -1.82738600    0.79082700    1.10501000
C      -0.54717400    0.13365600    0.72757200
C       0.37105600   -0.47842300    1.63696200
C       0.03231500   -0.44724100    3.05318400
H      -2.65788100    0.30210900    0.58580500
H      -1.81418600    1.83532500    0.77774500
H      -2.00546900    0.75467500    2.17808600
H       0.60811400   -0.29332700   -0.76399400
H       2.48961500   -1.83956300   -0.73700600
""",
)

entry(
    index = 37,
    label = "C4H4N_17",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {5,T}
2 C u0 p0 c0 {3,S} {4,D} {5,S}
3 C u1 p0 c0 {2,S} {8,S} {9,S}
4 C u0 p0 c0 {2,D} {6,S} {7,S}
5 C u0 p0 c0 {1,T} {2,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91024,0.00545245,0.000104882,-2.1647e-07,1.34626e-10,34622.7,8.85036], Tmin=(10,'K'), Tmax=(537.624,'K')),
            NASAPolynomial(coeffs=[3.27035,0.0300547,-1.91179e-05,5.93855e-09,-7.16263e-13,34404.8,8.87356], Tmin=(537.624,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (287.838,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (203.705,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'C-H': 4, 'C-C': 2, 'C#N': 1}
1D rotors:
pivots: [2, 3], dihedral: [4, 2, 3, 8], rotor symmetry: 2, max scan energy: 66.43 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 2 3 8 9 F


External symmetry: 2, optical isomers: 1

Geometry:
N      -0.41351700    2.66649800    0.21366000
C      -0.01556300    0.10035300    0.16490200
C      -1.11359700   -0.73064700    0.35590500
C       1.28141500   -0.35151200   -0.05047700
C      -0.23671200    1.52640200    0.19199700
H       2.10194800    0.33716100   -0.19369200
H       1.48800300   -1.41382500   -0.07771400
H      -2.10328800   -0.32854100    0.51984600
H      -0.98868900   -1.80589000    0.34252700
""",
)

entry(
    index = 38,
    label = "C4H4NO2_18",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {5,S}
3  C u0 p0 c0 {2,D} {8,S} {9,S}
4  O u0 p2 c0 {1,S} {10,S}
5  C u0 p0 c0 {2,S} {11,T}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 O u1 p2 c0 {4,S}
11 N u0 p1 c0 {5,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.42613,0.0607591,-0.000200496,4.71009e-07,-4.08774e-10,24827.9,13.8199], Tmin=(10,'K'), Tmax=(378.129,'K')),
            NASAPolynomial(coeffs=[3.46915,0.0383644,-2.4626e-05,7.49467e-09,-8.71314e-13,24981.5,15.7282], Tmin=(378.129,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (206.416,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (249.434,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'C-H': 4, 'C-C': 2, 'C-O': 1, 'O-O': 1, 'C#N': 1}
1D rotors:
pivots: [1, 4], dihedral: [2, 1, 4, 5], rotor symmetry: 1, max scan energy: 26.92 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 9 4 5 7 F
pivots: [4, 5], dihedral: [1, 4, 5, 6], rotor symmetry: 1, max scan energy: 15.47 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.47267700    1.16753100    0.20344300
O       2.79106400    1.22951000    0.12195100
N      -0.10707400   -3.37769500   -0.04796400
C       0.96571900   -0.08560900   -0.30779100
C       0.98843600   -1.17325500    0.74761400
C       1.51150000   -1.03715200    1.96826700
C       0.38778500   -2.40477000    0.33010700
H       1.56394300   -0.36443700   -1.17750000
H      -0.05898800    0.13076100   -0.61849100
H       1.96660800   -0.10671600    2.27936000
H       1.49413000   -1.85665800    2.67447100
""",
)

entry(
    index = 39,
    label = "C4H5NO2_19",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {5,S}
3  C u0 p0 c0 {2,D} {9,S} {10,S}
4  O u0 p2 c0 {1,S} {6,S}
5  C u0 p0 c0 {2,S} {11,T}
6  O u0 p2 c0 {4,S} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 N u0 p1 c0 {5,T}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65709,0.0271304,0.00022238,-8.3646e-07,8.46693e-10,6425.34,11.9918], Tmin=(10,'K'), Tmax=(367.647,'K')),
            NASAPolynomial(coeffs=[8.242,0.0318269,-1.94693e-05,5.90079e-09,-7.00479e-13,5719.35,-10.5565], Tmin=(367.647,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (53.4609,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (270.22,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'H-O': 1, 'C-H': 4, 'C-C': 2, 'C-O': 1, 'O-O': 1, 'C#N': 1}
1D rotors:
pivots: [1, 2], dihedral: [4, 1, 2, 12], rotor symmetry: 1, max scan energy: 27.42 kJ/mol
pivots: [1, 4], dihedral: [2, 1, 4, 5], rotor symmetry: 1, max scan energy: 48.88 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 9 4 5 6 F
D 4 1 2 12 F
pivots: [4, 5], dihedral: [1, 4, 5, 6], rotor symmetry: 1, max scan energy: 18.29 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 4 1 2 12 F


External symmetry: 1, optical isomers: 2

Geometry:
O       0.72101700    0.09357600    0.78055600
O       0.35627300    0.61226600   -0.53395900
N       1.06545600   -4.62310200   -0.11962700
C       1.22138200   -1.21215300    0.59167600
C       0.14135400   -2.24533000    0.30920800
C      -1.16378300   -1.96758000    0.29079600
C       0.62577200   -3.57078200    0.06648600
H       1.71960000   -1.44559900    1.53935900
H       1.97439900   -1.22116300   -0.20361100
H      -1.50519100   -0.95647100    0.46766100
H      -1.89952200   -2.73539900    0.09043500
H       0.88787500    1.42030300   -0.53925300
""",
)

entry(
    index = 40,
    label = "C4H3N2O3_20",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {6,S} {9,D}
3  C u0 p0 c0 {5,S} {10,D} {11,S}
4  O u0 p2 c0 {1,S} {5,S}
5  O u0 p2 c0 {3,S} {4,S}
6  C u0 p0 c0 {2,S} {12,T}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u0 p2 c0 {2,D}
10 N u1 p1 c0 {3,D}
11 H u0 p0 c0 {3,S}
12 N u0 p1 c0 {6,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.32008,0.071041,-0.000100656,8.53133e-08,-3.13336e-11,23562.4,14.52], Tmin=(10,'K'), Tmax=(627.692,'K')),
            NASAPolynomial(coeffs=[8.00291,0.0411994,-2.9343e-05,9.57242e-09,-1.16707e-12,22974.5,-5.89106], Tmin=(627.692,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (195.91,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (270.22,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'C-H': 3, 'C-C': 2, 'C-O': 2, 'C=N': 1, 'O-O': 1, 'C#N': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [6, 1, 2, 8], invalidation reason: The rotor scan has a barrier of 64.68 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
pivots: [1, 6], dihedral: [2, 1, 6, 7], rotor symmetry: 1, max scan energy: 48.29 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 1 6 7 9 F
D 6 1 2 8 F
pivots: [2, 8], dihedral: [1, 2, 8, 4], rotor symmetry: 1, max scan energy: 30.58 kJ/mol
pivots: [6, 7], dihedral: [1, 6, 7, 3], rotor symmetry: 1, max scan energy: 19.64 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       0.69320600   -0.90241300   -0.96699100
O       1.50563100   -0.62450900    0.21962500
O      -0.49711000    1.56641700   -0.55832700
N       3.39939600    0.60973000    0.60896200
N      -3.64832900    0.69410500    0.45331800
C      -0.64445500   -0.84773800   -0.54353100
C      -1.14908100    0.57883500   -0.35420000
C       2.39798000    0.37360300   -0.10061600
C      -2.54987500    0.66165200    0.10282300
H      -1.21764100   -1.32683400   -1.34592600
H      -0.80270100   -1.42830100    0.37294900
H       2.13600300    0.94957700   -0.99028300
""",
)

entry(
    index = 41,
    label = "C3H5O3_0",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,D}
3  C u1 p0 c0 {2,S} {9,S} {10,S}
4  O u0 p2 c0 {1,S} {5,S}
5  O u0 p2 c0 {4,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {2,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87941,0.00733003,0.00015924,-3.22324e-07,1.96441e-10,-15682.6,12.266], Tmin=(10,'K'), Tmax=(533.341,'K')),
            NASAPolynomial(coeffs=[1.1137,0.0529196,-3.88605e-05,1.2648e-08,-1.52034e-12,-15741,20.5575], Tmin=(533.341,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-130.435,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (241.12,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'O-O': 1, 'H-O': 1, 'C-C': 2, 'C=O': 1, 'C-H': 4, 'C-O': 1}
1D rotors:
pivots: [1, 2], dihedral: [4, 1, 2, 11], rotor symmetry: 1, max scan energy: 50.91 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 1 4 5 6 F
pivots: [1, 4], dihedral: [2, 1, 4, 5], rotor symmetry: 1, max scan energy: 63.97 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 1 4 5 6 F
D 4 1 2 11 F
pivots: [4, 5], dihedral: [1, 4, 5, 3], rotor symmetry: 1, max scan energy: 33.52 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 3 5 6 9 F
D 2 1 4 7 F
D 4 1 2 11 F
pivots: [5, 6], dihedral: [3, 5, 6, 9], rotor symmetry: 2, max scan energy: 45.32 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 5 6 9 10 F


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.73175500   -0.46274400   -0.26995600
O      -2.07223900    0.65709100    0.58574500
O      -1.75493100   -1.55014900    2.22164100
C      -0.53409600   -1.01778200    0.21685100
C      -0.71075800   -1.69790300    1.57846900
C       0.36912900   -2.49272300    2.08361100
H       0.25420000   -0.25558900    0.28529400
H      -0.23707800   -1.75423700   -0.53764100
H       1.29324000   -2.62470800    1.53275100
H       0.24930100   -2.97838700    3.04364200
H      -2.49848800    0.17707500    1.31723800
""",
)

entry(
    index = 42,
    label = "C4H6N2O2_2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  O u0 p2 c0 {1,S} {6,S}
5  C u0 p0 c0 {1,S} {13,T}
6  N u0 p1 c0 {4,S} {14,D}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 N u0 p1 c0 {5,T}
14 O u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65597,0.0272997,0.000253987,-8.95243e-07,8.83857e-10,-1501.64,13.1278], Tmin=(10,'K'), Tmax=(365.268,'K')),
            NASAPolynomial(coeffs=[6.85997,0.0441093,-2.81577e-05,8.67787e-09,-1.03203e-12,-2081.91,-3.84186], Tmin=(365.268,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-12.4457,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (315.95,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'N-O': 1, 'N=O': 1, 'C-C': 3, 'C#N': 1, 'C-H': 6, 'C-O': 1}
1D rotors:
pivots: [1, 3], dihedral: [5, 1, 3, 2], rotor symmetry: 1, max scan energy: 49.68 kJ/mol
pivots: [1, 5], dihedral: [3, 1, 5, 6], rotor symmetry: 1, max scan energy: 9.85 kJ/mol
pivots: [5, 6], dihedral: [1, 5, 6, 9], rotor symmetry: 3, max scan energy: 13.24 kJ/mol
pivots: [5, 7], dihedral: [1, 5, 7, 12], rotor symmetry: 3, max scan energy: 14.79 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.32465900    0.42434900   -0.12391100
O       2.45733200    2.23470200   -0.43888800
N       1.36468500    1.84470200   -0.47519600
N      -1.14055100    0.30989100   -2.49260800
C      -0.02852900   -0.09411400   -0.14274600
C       0.13785300   -1.60348500    0.07075900
C      -0.87076400    0.55778300    0.96169700
C      -0.63900900    0.15064500   -1.46749400
H       0.61473300   -1.77493900    1.03709300
H      -0.83630200   -2.09537800    0.05774600
H       0.76306000   -2.03040000   -0.71356100
H      -0.95650900    1.63231100    0.79949800
H      -0.38824700    0.37897800    1.92462000
H      -1.87356000    0.12658900    0.98045800
""",
)

entry(
    index = 43,
    label = "C4H5N2O2_3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {10,S} {11,S}
4  O u0 p2 c0 {1,S} {6,S}
5  C u0 p0 c0 {1,S} {12,T}
6  N u0 p1 c0 {4,S} {13,D}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 N u0 p1 c0 {5,T}
13 O u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.07854,0.0744879,-0.000119865,1.16411e-07,-4.66421e-11,25109.3,14.0297], Tmin=(10,'K'), Tmax=(659.802,'K')),
            NASAPolynomial(coeffs=[8.55419,0.0364023,-2.21647e-05,6.46213e-09,-7.26229e-13,24493.2,-9.30371], Tmin=(659.802,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (208.66,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (291.007,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'N-O': 1, 'N=O': 1, 'C-C': 3, 'C#N': 1, 'C-H': 5, 'C-O': 1}
1D rotors:
pivots: [1, 3], dihedral: [5, 1, 3, 2], rotor symmetry: 1, max scan energy: 47.06 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 1 5 7 13 F
pivots: [1, 5], dihedral: [3, 1, 5, 6], rotor symmetry: 1, max scan energy: 11.93 kJ/mol
pivots: [5, 6], dihedral: [1, 5, 6, 9], rotor symmetry: 3, max scan energy: 14.02 kJ/mol
pivots: [5, 7], dihedral: [1, 5, 7, 12], rotor symmetry: 2, max scan energy: 3.45 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.12580500    0.57604900    0.45538400
O       3.17651600    0.68950100   -0.20763200
N       2.12513300    0.39368500   -0.59984600
N      -0.27765800   -2.34337400   -0.60957100
C      -0.21392100    0.21964100   -0.02824200
C      -1.11683400    0.49027200    1.18628600
C      -0.59373800    1.04429800   -1.21319000
C      -0.23585700   -1.21919000   -0.36039500
H      -1.06687600    1.55207300    1.43176600
H      -0.77366000   -0.08969600    2.04339000
H      -2.14799600    0.21966100    0.95562600
H      -0.52600300    0.65170500   -2.21728000
H      -0.83475100    2.08764200   -1.05533900
""",
)

entry(
    index = 44,
    label = "C3H5O2_4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {7,D}
3  C u1 p0 c0 {2,S} {8,S} {9,S}
4  O u0 p2 c0 {1,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  O u0 p2 c0 {2,D}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93619,0.00406062,0.000128961,-2.59751e-07,1.6425e-10,-24876.4,10.4288], Tmin=(10,'K'), Tmax=(479.622,'K')),
            NASAPolynomial(coeffs=[0.491143,0.0438526,-3.00781e-05,9.39368e-09,-1.10189e-12,-24673.2,23.1917], Tmin=(479.622,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-206.85,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (220.334,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C-C': 2, 'C=O': 1, 'C-H': 4, 'C-O': 1}
1D rotors:
pivots: [1, 3], dihedral: [10, 1, 3, 4], rotor symmetry: 1, max scan energy: 30.30 kJ/mol
pivots: [3, 4], dihedral: [1, 3, 4, 2], rotor symmetry: 1, max scan energy: 34.26 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 10 1 3 4 F
pivots: [4, 5], dihedral: [2, 4, 5, 8], rotor symmetry: 2, max scan energy: 44.52 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 4 5 8 9 F


External symmetry: 1, optical isomers: 1

Geometry:
O       1.92351500   -0.29956100    0.15884900
O       0.08894900    1.39547500    0.98909600
C       0.66337200   -0.84454700    0.43046500
C      -0.31129500    0.23086800    0.90211600
C      -1.65614700   -0.13752900    1.22924800
H       0.24304900   -1.32821400   -0.46445400
H       0.72999500   -1.62049500    1.20825100
H      -2.00171800   -1.16173600    1.15088500
H      -2.34097500    0.63139500    1.56296800
H       1.83672300    0.64870100    0.34981000
""",
)

entry(
    index = 45,
    label = "C4H6N2O3_5",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  O u0 p2 c0 {1,S} {7,S}
5  C u0 p0 c0 {1,S} {13,T}
6  O u0 p2 c0 {2,S} {14,S}
7  N u0 p1 c0 {4,S} {15,D}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 N u0 p1 c0 {5,T}
14 H u0 p0 c0 {6,S}
15 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.52145,0.0350929,0.000270024,-8.66315e-07,7.49559e-10,-19954.5,13.2975], Tmin=(10,'K'), Tmax=(425.13,'K')),
            NASAPolynomial(coeffs=[9.6389,0.0496327,-3.56642e-05,1.19648e-08,-1.50262e-12,-21126.2,-18.6458], Tmin=(425.13,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-165.925,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (336.736,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'N-O': 1, 'H-O': 1, 'N=O': 1, 'C-C': 3, 'C#N': 1, 'C-H': 5, 'C-O': 2}
1D rotors:
pivots: [1, 4], dihedral: [6, 1, 4, 3], rotor symmetry: 1, max scan energy: 48.34 kJ/mol
pivots: [1, 6], dihedral: [4, 1, 6, 7], rotor symmetry: 1, max scan energy: 12.23 kJ/mol
pivots: [2, 7], dihedral: [15, 2, 7, 6], rotor symmetry: 1, max scan energy: 24.94 kJ/mol
pivots: [6, 7], dihedral: [1, 6, 7, 2], rotor symmetry: 1, max scan energy: 31.71 kJ/mol
pivots: [6, 8], dihedral: [1, 6, 8, 12], rotor symmetry: 3, max scan energy: 14.36 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       2.26996000   -1.64336800   -1.24874100
O      -0.33227000   -1.40446600   -2.13713200
O       4.39449000   -1.67617100   -1.65918400
N       3.59908200   -2.24464800   -1.03874300
N       1.73296200   -2.26530600    2.07439400
C       1.23410000   -2.32866100   -0.50246100
C      -0.02009200   -1.45257300   -0.76476400
C       1.05048900   -3.76335500   -1.00401600
C       1.54194800   -2.29674000    0.93826700
H       0.16237700   -0.45611500   -0.34653300
H      -0.87490500   -1.89583000   -0.25159700
H       1.97914800   -4.32595500   -0.90924500
H       0.74355000   -3.72722800   -2.04911600
H       0.27525000   -4.26870500   -0.42445100
H       0.40433600   -0.97036500   -2.58307900
""",
)

entry(
    index = 46,
    label = "C3H2N2O2_6",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {6,S} {7,S}
3 O u0 p2 c0 {1,S} {5,S}
4 C u0 p0 c0 {1,S} {8,T}
5 N u0 p1 c0 {3,S} {9,D}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 N u0 p1 c0 {4,T}
9 O u0 p2 c0 {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.58304,0.0362305,-1.0174e-05,-4.19516e-08,3.76014e-11,19879.1,12.9787], Tmin=(10,'K'), Tmax=(558.467,'K')),
            NASAPolynomial(coeffs=[6.4365,0.0275716,-1.85543e-05,5.81933e-09,-6.89907e-13,19376.7,-0.769819], Tmin=(558.467,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (165.237,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (199.547,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'N-O': 1, 'C=C': 1, 'N=O': 1, 'C-C': 1, 'C#N': 1, 'C-H': 2, 'C-O': 1}
1D rotors:
pivots: [1, 3], dihedral: [5, 1, 3, 2], rotor symmetry: 1, max scan energy: 43.84 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 3 1 5 7 F
pivots: [1, 5], dihedral: [3, 1, 5, 6], rotor symmetry: 1, max scan energy: 7.73 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       0.99970000   -0.40998600   -0.38133300
O       3.10543100    0.25787100   -0.08874300
N       2.05725700    0.55403200    0.25285500
N      -1.68196300   -1.86198500    1.06939800
C      -0.27107400   -0.01349000   -0.07625100
C      -0.76085200    1.20255700   -0.33783000
C      -1.05580100   -1.03477000    0.56367300
H      -0.15525900    1.94352200   -0.84229300
H      -1.77001200    1.46306400   -0.05125600
""",
)

entry(
    index = 47,
    label = "C4H5N2O3_7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  O u0 p2 c0 {1,S} {6,S}
5  C u0 p0 c0 {1,S} {13,T}
6  N u0 p1 c0 {4,S} {14,D}
7  O u1 p2 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 N u0 p1 c0 {5,T}
14 O u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.48755,0.0454862,0.000205122,-9.372e-07,1.0777e-09,7767,14.7887], Tmin=(10,'K'), Tmax=(326.439,'K')),
            NASAPolynomial(coeffs=[7.26613,0.0482965,-3.34572e-05,1.08992e-08,-1.34154e-12,7258.64,-3.21853], Tmin=(326.439,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (64.6421,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (315.95,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'N-O': 1, 'N=O': 1, 'C-C': 3, 'C#N': 1, 'C-H': 5, 'C-O': 2}
1D rotors:
pivots: [1, 4], dihedral: [6, 1, 4, 3], rotor symmetry: 1, max scan energy: 49.10 kJ/mol
pivots: [1, 6], dihedral: [4, 1, 6, 7], rotor symmetry: 1, max scan energy: 12.92 kJ/mol
pivots: [6, 7], dihedral: [1, 6, 7, 2], rotor symmetry: 1, max scan energy: 18.04 kJ/mol
pivots: [6, 8], dihedral: [1, 6, 8, 12], rotor symmetry: 3, max scan energy: 13.46 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.04284700    0.87937200    0.29190500
O      -2.08015000   -0.75998900    1.30014100
O       2.91828000    0.95307500    1.37674500
N       2.00904800    0.25426300    1.21870100
N       0.62830300   -2.34811000   -0.76633900
C      -0.10198000    0.03185200    0.07128300
C      -0.90706600   -0.09370500    1.39863000
C      -0.93662000    0.72797600   -1.00583900
C       0.31923100   -1.30200900   -0.39547200
H      -1.08021400    0.92201800    1.80174200
H      -0.29344100   -0.59710200    2.16960900
H      -0.37763600    0.79223100   -1.93907300
H      -1.85555200    0.16362600   -1.17074000
H      -1.18563800    1.73638100   -0.66976700
""",
)

entry(
    index = 48,
    label = "C4H5N2O3_8",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {6,S} {11,S}
4  O u0 p2 c0 {1,S} {7,S}
5  C u0 p0 c0 {1,S} {12,T}
6  O u0 p2 c0 {3,S} {13,S}
7  N u0 p1 c0 {4,S} {14,D}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 N u0 p1 c0 {5,T}
13 H u0 p0 c0 {6,S}
14 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49511,0.0369529,0.000279288,-9.4363e-07,8.40708e-10,2467.61,13.9479], Tmin=(10,'K'), Tmax=(421.266,'K')),
            NASAPolynomial(coeffs=[11.7689,0.040975,-2.90885e-05,9.73708e-09,-1.22913e-12,1037.73,-27.5133], Tmin=(421.266,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (20.5084,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (311.793,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'N-O': 1, 'H-O': 1, 'N=O': 1, 'C-C': 3, 'C#N': 1, 'C-H': 4, 'C-O': 2}
1D rotors:
pivots: [1, 4], dihedral: [6, 1, 4, 3], rotor symmetry: 1, max scan energy: 60.27 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 4 1 6 7 F
D 14 2 8 6 F
D 1 6 8 2 F
B 1 4 F
pivots: [1, 6], dihedral: [4, 1, 6, 7], rotor symmetry: 1, max scan energy: 13.52 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 9 6 8 13 F
D 14 2 8 6 F
pivots: [2, 8], dihedral: [14, 2, 8, 6], rotor symmetry: 1, max scan energy: 32.59 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 2 8 6 13 F
D 4 1 6 7 F
D 1 6 8 2 F
pivots: [6, 7], dihedral: [1, 6, 7, 10], rotor symmetry: 3, max scan energy: 12.10 kJ/mol
pivots: [6, 8], dihedral: [1, 6, 8, 2], rotor symmetry: 1, max scan energy: 25.51 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 6 8 2 13 F
D 4 1 6 7 F
D 14 2 8 6 F


External symmetry: 1, optical isomers: 2

Geometry:
O       1.07564100    0.57297900    0.16820300
O       0.48242500   -1.65984900    2.23821100
O       3.15546800    0.06068300   -0.07803700
N       2.11872200   -0.43238900    0.11393200
N      -0.74822300   -1.96539800   -1.21506300
C      -0.23151800   -0.03758900    0.50132200
C      -1.23142000    1.11084300    0.33314000
C      -0.25527300   -0.58480200    1.88438500
C      -0.50469600   -1.11233700   -0.47853400
H      -1.15766400    1.52019400   -0.67364400
H      -0.99309400    1.89571600    1.05223500
H      -2.24710300    0.75395200    0.50643900
H      -0.54462600    0.03996300    2.71736200
H       0.79429300   -2.13275500    1.45451400
""",
)

entry(
    index = 49,
    label = "C3H6NO3_10",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,D}
3  C u1 p0 c0 {2,S} {10,S} {11,S}
4  N u0 p1 c0 {6,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {4,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u0 p2 c0 {2,D}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63673,0.0299416,7.03354e-05,-1.52345e-07,8.27101e-11,324.662,12.7349], Tmin=(10,'K'), Tmax=(647.867,'K')),
            NASAPolynomial(coeffs=[3.6262,0.0528254,-3.54789e-05,1.09044e-08,-1.26326e-12,-152.86,9.08528], Tmin=(647.867,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (2.64253,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (291.007,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'N-O': 1, 'H-N': 2, 'O-O': 1, 'C-C': 2, 'C=O': 1, 'C-H': 4, 'C-O': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [5, 1, 2, 4], invalidation reason: The rotor scan has a barrier of 51.54 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
pivots: [1, 5], dihedral: [2, 1, 5, 6], rotor symmetry: 1, max scan energy: 62.73 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 9 5 6 3 F
D 5 1 2 4 F
pivots: [2, 4], dihedral: [1, 2, 4, 12], rotor symmetry: 1, max scan energy: 98.86 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 2 4 13 F
D 2 4 12 13 F
D 9 5 6 3 F
D 5 1 2 4 F
B 1 2 F
pivots: [5, 6], dihedral: [1, 5, 6, 3], rotor symmetry: 1, max scan energy: 39.44 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 8 1 5 6 F
D 5 6 3 7 F
D 3 6 7 10 F
D 2 1 5 8 F
D 5 1 2 4 F
pivots: [6, 7], dihedral: [3, 6, 7, 10], rotor symmetry: 2, max scan energy: 43.70 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 6 7 10 11 F


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.67631400   -0.36068300   -0.08862100
O      -1.60243200   -1.51585100    0.42040200
O       0.75173600   -2.51373700   -1.12476000
N      -2.12858900   -2.16851700   -0.62183300
C       0.59350600   -0.64394600    0.41271000
C       1.31412400   -1.80294700   -0.28860100
C       2.68346900   -2.03936200    0.07632600
H       0.56505800   -0.84528700    1.49398600
H       1.17753100    0.27656400    0.27780500
H       3.19239700   -1.44246900    0.82461100
H       3.21695200   -2.84600300   -0.41011300
H      -1.37856900   -2.55945700   -1.19304700
H      -2.73880000   -1.55607700   -1.16007900
""",
)

entry(
    index = 50,
    label = "C4H4N2O3_11",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,D} {11,S}
4  O u0 p2 c0 {1,S} {6,S}
5  C u0 p0 c0 {1,S} {12,T}
6  N u0 p1 c0 {4,S} {13,D}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {3,S}
12 N u0 p1 c0 {5,T}
13 O u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.41439,0.0509409,0.000136631,-6.66618e-07,7.21089e-10,-7981.68,13.1273], Tmin=(10,'K'), Tmax=(361.821,'K')),
            NASAPolynomial(coeffs=[8.49776,0.0430091,-3.05802e-05,1.01553e-08,-1.26646e-12,-8665.47,-10.5952], Tmin=(361.821,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-66.3196,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (291.007,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'N-O': 1, 'N=O': 1, 'C-C': 3, 'C=O': 1, 'C#N': 1, 'C-H': 4, 'C-O': 1}
1D rotors:
pivots: [1, 4], dihedral: [6, 1, 4, 3], rotor symmetry: 1, max scan energy: 56.84 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 1 6 8 13 F
D 4 1 6 7 F
pivots: [1, 6], dihedral: [4, 1, 6, 7], rotor symmetry: 1, max scan energy: 30.47 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 1 6 8 13 F
pivots: [6, 7], dihedral: [1, 6, 7, 10], rotor symmetry: 3, max scan energy: 12.06 kJ/mol
pivots: [6, 8], dihedral: [1, 6, 8, 2], rotor symmetry: 1, max scan energy: 14.78 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       0.84620300    0.96447600   -0.41503300
O       0.15669600   -0.72322400   -2.46515500
O       2.93441100    1.07195100   -1.07375000
N       2.15047900    0.27918800   -0.79583000
N       0.38611400   -1.62325400    1.80152900
C      -0.17053100    0.01445300   -0.17814800
C      -1.44903200    0.80978000    0.14504100
C      -0.43927800   -0.85813500   -1.43866500
C       0.15950100   -0.89343500    0.93850900
H      -1.67485000    1.46919200   -0.69409000
H      -2.29042500    0.13700600    0.32140900
H      -1.28367200    1.41214300    1.03800300
H      -1.25315400   -1.59930700   -1.30652600
""",
)

entry(
    index = 51,
    label = "C4H3N2O3_12",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  O u0 p2 c0 {1,S} {6,S}
4  C u1 p0 c0 {1,S} {10,D}
5  C u0 p0 c0 {1,S} {11,T}
6  N u0 p1 c0 {3,S} {12,D}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {4,D}
11 N u0 p1 c0 {5,T}
12 O u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.62347,0.0319655,0.000166481,-6.36333e-07,6.47543e-10,7433.24,13.555], Tmin=(10,'K'), Tmax=(356.367,'K')),
            NASAPolynomial(coeffs=[5.77452,0.0432174,-2.98673e-05,9.6979e-09,-1.18917e-12,7055.16,2.24335], Tmin=(356.367,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (61.8408,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (278.535,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'N-O': 1, 'N=O': 1, 'C-C': 3, 'C=O': 1, 'C#N': 1, 'C-H': 3, 'C-O': 1}
1D rotors:
* Invalidated! pivots: [1, 4], dihedral: [6, 1, 4, 3], invalidation reason: Could not read energies
* Invalidated! pivots: [1, 6], dihedral: [4, 1, 6, 7], invalidation reason: Could not read energies
pivots: [6, 7], dihedral: [1, 6, 7, 10], rotor symmetry: 3, max scan energy: 11.52 kJ/mol
* Invalidated! pivots: [6, 8], dihedral: [1, 6, 8, 2], invalidation reason: The rotor scan has a barrier of 49.51 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 1, optical isomers: 2

Geometry:
O       1.02238900   -1.01463200   -0.25629000
O       0.45777900    2.22205800   -0.58535400
O       2.57337700    0.12407100   -1.68977700
N       1.63919200    0.16455000   -0.93996700
N       0.17813600   -0.01740700    2.90560800
C       0.00112200   -0.15732300    0.30057100
C      -1.40016700   -0.51551200   -0.17516800
C       0.63675900    1.06301500   -0.42419500
C       0.11496700   -0.08113600    1.75709200
H      -1.69654400   -1.48145200    0.23536200
H      -1.41170300   -0.56965900   -1.26455500
H      -2.11050400    0.24460900    0.15601900
""",
)

entry(
    index = 52,
    label = "C4H6NO2_14",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {5,S} {13,S}
2  O u0 p2 c0 {6,D}
3  N u1 p1 c0 {7,D}
4  C u0 p0 c0 {6,S} {7,S} {8,S} {9,S}
5  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
6  C u0 p0 c0 {2,D} {4,S} {5,S}
7  C u0 p0 c0 {3,D} {4,S} {12,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.50977,0.0476712,-2.79987e-05,5.73538e-09,9.64607e-14,-14962,13.1685], Tmin=(10,'K'), Tmax=(1375.88,'K')),
            NASAPolynomial(coeffs=[15.0495,0.02339,-1.16306e-05,2.69986e-09,-2.41492e-13,-19014.7,-49.374], Tmin=(1375.88,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-124.45,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (291.007,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=N': 1, 'H-O': 1, 'C-C': 3, 'C=O': 1, 'C-H': 5, 'C-O': 1}
1D rotors:
pivots: [1, 5], dihedral: [13, 1, 5, 6], rotor symmetry: 1, max scan energy: 25.68 kJ/mol
pivots: [4, 6], dihedral: [7, 4, 6, 2], rotor symmetry: 1, max scan energy: 9.88 kJ/mol
pivots: [4, 7], dihedral: [6, 4, 7, 3], rotor symmetry: 1, max scan energy: 16.18 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 8 4 6 2 F
pivots: [5, 6], dihedral: [1, 5, 6, 2], rotor symmetry: 1, max scan energy: 38.92 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 8 4 6 2 F
D 13 1 5 10 F


External symmetry: 1, optical isomers: 2

Geometry:
O       2.48542100    0.43305000   -0.52999100
O       1.46232300   -1.34464900   -2.23030700
N      -2.28537000   -2.74756700   -1.92729000
C      -0.19953000   -2.25830900   -0.76094700
C       1.35790000   -0.28301900   -0.11547800
C       0.91927300   -1.30426000   -1.14800400
C      -1.04561300   -2.66605600   -1.95810800
H       0.28364400   -3.15775700   -0.35599000
H      -0.82869200   -1.84584600    0.03007700
H       0.49588500    0.38177500    0.06272400
H       1.55447600   -0.80077000    0.83411000
H      -0.49100600   -2.88234100   -2.88262600
H       2.63269300    0.18433400   -1.45517200
""",
)

entry(
    index = 53,
    label = "C4H5NO3_15",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
2  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {2,S} {11,D}
4  O u0 p2 c0 {1,S} {6,S}
5  O u0 p2 c0 {2,S} {12,S}
6  C u0 p0 c0 {4,S} {13,T}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 O u0 p2 c0 {3,D}
12 H u0 p0 c0 {5,S}
13 N u0 p1 c0 {6,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7762,0.0490196,-3.07478e-05,8.10539e-09,-6.32478e-13,-38901.2,10.9551], Tmin=(10,'K'), Tmax=(1622.86,'K')),
            NASAPolynomial(coeffs=[26.2961,0.00400777,1.15587e-06,-1.01563e-09,1.58729e-13,-47592.5,-112.852], Tmin=(1622.86,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-323.472,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (291.007,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C-C': 2, 'C=O': 1, 'C#N': 1, 'C-H': 4, 'C-O': 3}
1D rotors:
pivots: [1, 5], dihedral: [8, 1, 5, 7], rotor symmetry: 1, max scan energy: 27.56 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 13 2 6 10 F
D 12 5 7 6 F
pivots: [2, 6], dihedral: [13, 2, 6, 7], rotor symmetry: 2, max scan energy: 22.29 kJ/mol
pivots: [5, 7], dihedral: [1, 5, 7, 3], rotor symmetry: 1, max scan energy: 15.27 kJ/mol
pivots: [6, 7], dihedral: [2, 6, 7, 3], rotor symmetry: 1, max scan energy: 40.97 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 8 1 5 11 F
D 13 2 6 10 F
D 12 5 7 6 F


External symmetry: 1, optical isomers: 1

Geometry:
O       1.83958900   -1.21376600   -1.37904200
O      -0.63996800   -4.46985500   -0.66386700
O       0.39883700   -3.98532200   -3.06718600
N       3.28460500    0.74087800   -1.65919500
C       1.61186200   -2.03475300   -2.56162100
C       0.18131800   -3.34447400   -0.78859100
C       0.69878900   -3.19386900   -2.20285100
C       2.60394200   -0.18749200   -1.54553000
H      -0.35572800   -2.42305400   -0.52012100
H       1.04600400   -3.40071400   -0.11134400
H       1.14306900   -1.43079200   -3.34197900
H       2.56541500   -2.42282800   -2.92717100
H      -0.67367700   -4.88413700   -1.53910600
""",
)

entry(
    index = 54,
    label = "C4H5NO3_16",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
2  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {2,S} {11,D}
4  N u0 p1 c0 {1,S} {6,D}
5  O u0 p2 c0 {2,S} {12,S}
6  C u0 p0 c0 {4,D} {13,D}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 O u0 p2 c0 {3,D}
12 H u0 p0 c0 {5,S}
13 O u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73284,0.0479493,-1.68293e-05,-1.32479e-08,8.1472e-12,-53324.3,12.8607], Tmin=(10,'K'), Tmax=(1034.98,'K')),
            NASAPolynomial(coeffs=[13.7782,0.028366,-1.63319e-05,4.39334e-09,-4.52702e-13,-56434.1,-40.926], Tmin=(1034.98,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-443.284,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (291.007,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=N': 1, 'H-O': 1, 'C-C': 2, 'C=O': 2, 'C-H': 4, 'C-O': 1, 'C-N': 1}
1D rotors:
pivots: [1, 6], dihedral: [13, 1, 6, 7], rotor symmetry: 1, max scan energy: 25.24 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 9 6 7 2 F
D 8 4 5 12 F
D 12 5 7 6 F
pivots: [4, 5], dihedral: [8, 4, 5, 7], rotor symmetry: 1, max scan energy: 13.92 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 13 1 6 9 F
D 12 5 7 6 F
pivots: [5, 7], dihedral: [4, 5, 7, 2], rotor symmetry: 1, max scan energy: 19.33 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 8 4 5 7 F
pivots: [6, 7], dihedral: [1, 6, 7, 2], rotor symmetry: 1, max scan energy: 33.16 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 13 1 6 7 F


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.60982600    1.07032900    0.10964700
O      -0.03430500    1.73109700    0.34886100
O       3.18764600    2.25027800    0.89755400
N       1.97594700    0.37932600    1.69914200
C       0.62848400   -0.09162300    1.75584900
C      -1.76366700    0.15979200    0.75397900
C      -0.35245200    0.70446600    0.90206600
C       2.51052300    1.37030600    1.25587200
H      -2.16310600   -0.09143600    1.74522300
H      -1.68673200   -0.78734400    0.19415600
H       0.26467100   -0.06588900    2.79167800
H       0.59187200   -1.14407100    1.45292500
H      -2.03599400    1.75880700   -0.25788900
""",
)

entry(
    index = 55,
    label = "C4H5NO3_17",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {6,S}
3  C u0 p0 c0 {2,D} {4,S} {10,S}
4  O u0 p2 c0 {3,S} {7,S}
5  O u0 p2 c0 {1,S} {11,S}
6  O u0 p2 c0 {2,S} {12,S}
7  C u0 p0 c0 {4,S} {13,T}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 N u0 p1 c0 {7,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.40985,0.0501541,-2.24939e-05,-7.67111e-09,6.52878e-12,-32541.1,13.3388], Tmin=(10,'K'), Tmax=(966.102,'K')),
            NASAPolynomial(coeffs=[9.43614,0.0379748,-2.34136e-05,6.64711e-09,-7.17299e-13,-34301.5,-18.6114], Tmin=(966.102,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-270.611,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (291.007,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'H-O': 2, 'C-O': 4, 'C-C': 1, 'C#N': 1, 'C-H': 3}
1D rotors:
pivots: [1, 7], dihedral: [8, 1, 7, 6], rotor symmetry: 1, max scan energy: 13.75 kJ/mol
pivots: [2, 5], dihedral: [12, 2, 5, 6], rotor symmetry: 1, max scan energy: 43.40 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 13 3 6 5 F
D 8 1 7 11 F
D 10 5 6 3 F
pivots: [3, 6], dihedral: [13, 3, 6, 5], rotor symmetry: 1, max scan energy: 38.12 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 8 1 7 11 F
D 10 5 6 3 F
D 12 2 5 10 F
pivots: [5, 6], dihedral: [2, 5, 6, 3], rotor symmetry: 1, max scan energy: 37.75 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 8 1 7 11 F
D 13 3 6 5 F
D 12 2 5 10 F


External symmetry: 1, optical isomers: 2

Geometry:
O       4.76638900   -0.78657300   -0.68555800
O       2.08449000    2.20969800   -1.75564100
O       4.70684300    2.70786900   -1.60438100
N       5.83550200   -2.80199200   -1.56871500
C       2.84266200    1.32896700   -0.91907700
C       4.31132000    1.45929700   -1.25075100
C       5.20435100    0.47443500   -1.17729800
C       5.34260900   -1.83252200   -1.17443700
H       2.66492000    1.67535700    0.10240500
H       2.50979400    0.29231300   -0.99210600
H       6.26063000    0.55742300   -1.38412800
H       1.98920600    1.79701900   -2.62129700
H       3.89412200    3.19282000   -1.81986600
""",
)

entry(
    index = 56,
    label = "C4H4NO3_18",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {5,S} {10,S}
4  O u0 p2 c0 {1,S} {11,S}
5  O u0 p2 c0 {3,S} {6,S}
6  C u0 p0 c0 {5,S} {12,T}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u1 p2 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 N u0 p1 c0 {6,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49119,0.0506967,-3.21298e-05,4.46804e-09,1.6695e-12,-18957.7,12.8444], Tmin=(10,'K'), Tmax=(1111.64,'K')),
            NASAPolynomial(coeffs=[13.3217,0.0270869,-1.61447e-05,4.40067e-09,-4.56145e-13,-21870.1,-38.8916], Tmin=(1111.64,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-157.636,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (261.906,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'H-O': 1, 'C-O': 4, 'C-C': 1, 'C#N': 1, 'C-H': 3}
1D rotors:
pivots: [1, 5], dihedral: [12, 1, 5, 6], rotor symmetry: 1, max scan energy: 25.49 kJ/mol
pivots: [2, 7], dihedral: [8, 2, 7, 6], rotor symmetry: 1, max scan energy: 24.74 kJ/mol
pivots: [5, 6], dihedral: [1, 5, 6, 3], rotor symmetry: 1, max scan energy: 32.31 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 12 1 5 6 F
pivots: [6, 7], dihedral: [3, 6, 7, 2], rotor symmetry: 1, max scan energy: 66.24 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 6 7 2 11 F
pivots: [2, 8], dihedral: [7, 2, 8, 4], rotor symmetry: 1, max scan energy: 0.25 kJ/mol (set as a FreeRotor)


External symmetry: 1, optical isomers: 1

Geometry:
O      -2.48956900    0.15787000    0.48930900
O       0.79589200   -1.29905300   -1.73649100
O      -0.24441100   -0.72265500    1.58073000
N       2.69640500   -2.14230800   -3.03494800
C      -1.50858400   -0.28725800   -0.40484800
C      -0.27359700   -0.76486000    0.34861300
C       0.86134900   -1.26538000   -0.35748800
C       1.81516300   -1.74984300   -2.39973500
H      -1.21248200    0.51504100   -1.09572400
H      -1.88609000   -1.11359700   -1.02397800
H       1.76599800   -1.61858800    0.11824400
H      -2.11607900    0.04249600    1.37697700
""",
)

entry(
    index = 57,
    label = "C4H3NO2_19",
    molecule = 
"""
1  C u0 p0 c0 {3,D} {4,S} {8,S}
2  C u0 p0 c0 {3,D} {5,S} {7,S}
3  C u0 p0 c0 {1,D} {2,D}
4  O u0 p2 c0 {1,S} {6,S}
5  O u0 p2 c0 {2,S} {9,S}
6  C u0 p0 c0 {4,S} {10,T}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {5,S}
10 N u0 p1 c0 {6,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71141,0.0216999,0.000152209,-4.86679e-07,4.2169e-10,8545.63,12.9371], Tmin=(10,'K'), Tmax=(420.013,'K')),
            NASAPolynomial(coeffs=[6.53231,0.0328687,-2.35082e-05,7.82458e-09,-9.75037e-13,7973.18,-2.21872], Tmin=(420.013,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (71.0477,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (224.491,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'H-O': 1, 'C#N': 1, 'C-H': 2, 'C-O': 3}
1D rotors:
pivots: [1, 4], dihedral: [7, 1, 4, 6], rotor symmetry: 1, max scan energy: 16.55 kJ/mol
pivots: [2, 5], dihedral: [10, 2, 5, 6], rotor symmetry: 1, max scan energy: 34.18 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.23646500    0.87057100    0.08506700
O      -2.23169500   -2.85662800    2.47327000
N      -2.57628500    1.81388100    1.90341900
C      -0.77580500   -0.48047600    0.19633000
C      -1.19205500   -2.01859500    2.25943000
C      -0.99421700   -1.25461800    1.21082600
C      -1.93947100    1.34640700    1.05911800
H      -0.49077000   -2.04487100    3.08725400
H      -0.22969200   -0.70662200   -0.70867700
H      -2.85475700   -2.78436100    1.73867700
""",
)

entry(
    index = 58,
    label = "C4H4NO3_20",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {5,S}
3  C u1 p0 c0 {2,D} {6,S}
4  O u0 p2 c0 {1,S} {10,S}
5  O u0 p2 c0 {2,S} {11,S}
6  O u0 p2 c0 {3,S} {7,S}
7  C u0 p0 c0 {6,S} {12,T}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 N u0 p1 c0 {7,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53117,0.0378588,9.27178e-05,-2.97245e-07,2.22554e-10,-520.28,13.6075], Tmin=(10,'K'), Tmax=(502.89,'K')),
            NASAPolynomial(coeffs=[7.32484,0.0436991,-3.21277e-05,1.06695e-08,-1.31475e-12,-1357.25,-6.61498], Tmin=(502.89,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-4.38907,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (266.063,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'H-O': 2, 'C-O': 4, 'C-C': 1, 'C#N': 1, 'C-H': 2}
1D rotors:
pivots: [1, 5], dihedral: [11, 1, 5, 6], rotor symmetry: 1, max scan energy: 38.16 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 8 3 7 6 F
D 10 5 6 7 F
D 12 2 6 7 F
pivots: [2, 6], dihedral: [12, 2, 6, 5], rotor symmetry: 1, max scan energy: 30.11 kJ/mol
pivots: [3, 7], dihedral: [8, 3, 7, 6], rotor symmetry: 1, max scan energy: 26.23 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 10 5 6 7 F
D 12 2 6 7 F
D 2 6 7 3 F
pivots: [5, 6], dihedral: [1, 5, 6, 2], rotor symmetry: 1, max scan energy: 34.57 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 11 1 5 9 F
D 8 3 7 6 F
D 12 2 6 7 F


External symmetry: 1, optical isomers: 2

Geometry:
O       0.73182200   -0.11801800   -3.14123900
O      -1.41832500   -1.54749600   -2.28177700
O      -0.83615100   -3.94591100   -0.79209600
N      -0.51693000   -6.30192700   -1.39479100
C       0.81592000   -0.72430600   -1.84748700
C      -0.20544300   -1.82707900   -1.73597000
C       0.08299300   -3.00965900   -1.19722000
C      -0.63609700   -5.18266700   -1.13620500
H       0.56547600    0.07326900   -1.14262900
H       1.81801600   -1.09282200   -1.61789900
H       1.14543300   -0.71115900   -3.77890000
H      -1.26729000   -0.82278700   -2.91073200
""",
)

entry(
    index = 59,
    label = "C4H5NO2_21",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,D}
4  O u0 p2 c0 {2,S} {12,S}
5  C u0 p0 c0 {1,S} {11,T}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 N u0 p1 c0 {5,T}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.56394,0.0419138,-2.42131e-05,5.88889e-09,-4.26035e-13,-28931.7,13.0695], Tmin=(10,'K'), Tmax=(1718.68,'K')),
            NASAPolynomial(coeffs=[21.7675,0.00757422,-1.24828e-06,-3.01618e-10,7.91649e-14,-36374.5,-88.0595], Tmin=(1718.68,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-240.658,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (270.22,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C-C': 3, 'C=O': 1, 'C#N': 1, 'C-H': 4, 'C-O': 1}
1D rotors:
pivots: [1, 5], dihedral: [12, 1, 5, 6], rotor symmetry: 1, max scan energy: 22.95 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 8 4 6 2 F
pivots: [4, 6], dihedral: [7, 4, 6, 2], rotor symmetry: 1, max scan energy: 6.37 kJ/mol
pivots: [5, 6], dihedral: [1, 5, 6, 2], rotor symmetry: 1, max scan energy: 41.92 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 8 4 6 2 F
D 12 1 5 10 F


External symmetry: 1, optical isomers: 2

Geometry:
O       2.40237600    0.38703300   -0.31080500
O       0.25975100    1.53394600   -1.40234400
N      -1.15504600    1.28663600    3.06592700
C      -1.21209900    1.42495000    0.46058100
C       1.28621700    0.57813000    0.50985200
C       0.13865700    1.21463300   -0.24378100
C      -1.18814000    1.34774500    1.91578100
H      -1.60568500    2.39282600    0.14063800
H      -1.89640200    0.66295000    0.07079800
H       0.93553200   -0.37571500    0.93231100
H       1.52344100    1.22315100    1.36964400
H       2.17183100    0.76006500   -1.17468600
""",
)

entry(
    index = 60,
    label = "C3H4NO2_22",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {5,S} {10,S}
2  O u0 p2 c0 {5,D}
3  N u1 p1 c0 {6,D}
4  C u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
5  C u0 p0 c0 {1,S} {2,D} {4,S}
6  C u0 p0 c0 {3,D} {4,S} {9,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61406,0.0380026,-8.03042e-05,1.88866e-07,-1.66753e-10,-21227.6,13.0494], Tmin=(10,'K'), Tmax=(412.582,'K')),
            NASAPolynomial(coeffs=[1.90714,0.0387677,-2.57025e-05,7.91524e-09,-9.23677e-13,-20952.4,21.4011], Tmin=(412.582,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-176.505,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (220.334,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=N': 1, 'H-O': 1, 'C-C': 2, 'C=O': 1, 'C-H': 3, 'C-O': 1}
1D rotors:
pivots: [1, 5], dihedral: [10, 1, 5, 2], rotor symmetry: 1, max scan energy: 57.15 kJ/mol
pivots: [4, 5], dihedral: [6, 4, 5, 1], rotor symmetry: 1, max scan energy: 8.92 kJ/mol
pivots: [4, 6], dihedral: [5, 4, 6, 3], rotor symmetry: 1, max scan energy: 15.89 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.98969500   -0.39677900   -0.44967900
O       0.91646500   -0.26337000    1.52186200
N      -2.32517100    1.30281300   -0.19551100
C      -0.35127700   -0.08932600   -0.53455700
C       0.89098300   -0.24639100    0.31932600
C      -1.51632000    0.47514000    0.25941300
H      -0.13887100    0.52470000   -1.40982400
H      -0.61893000   -1.08773700   -0.90188500
H      -1.61687100    0.11060800    1.29220900
H       2.74017500   -0.51871000    0.15184700
""",
)

entry(
    index = 61,
    label = "C3H3NO3_23",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,D}
3  O u0 p2 c0 {1,S} {5,S}
4  O u0 p2 c0 {2,S} {9,S}
5  C u0 p0 c0 {3,S} {10,T}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {2,D}
9  H u0 p0 c0 {4,S}
10 N u0 p1 c0 {5,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8541,0.0301092,-7.81251e-06,-7.89917e-09,3.95393e-12,-44785,14.5586], Tmin=(10,'K'), Tmax=(1155.63,'K')),
            NASAPolynomial(coeffs=[10.2273,0.0200275,-1.02737e-05,2.48958e-09,-2.33748e-13,-47057.8,-20.571], Tmin=(1155.63,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-372.315,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (220.334,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C-C': 1, 'C=O': 1, 'C#N': 1, 'C-H': 2, 'C-O': 3}
1D rotors:
pivots: [1, 5], dihedral: [7, 1, 5, 6], rotor symmetry: 1, max scan energy: 5.07 kJ/mol
pivots: [2, 6], dihedral: [10, 2, 6, 3], rotor symmetry: 1, max scan energy: 54.30 kJ/mol
pivots: [5, 6], dihedral: [1, 5, 6, 2], rotor symmetry: 1, max scan energy: 13.17 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.33145300   -0.66773700   -0.64060300
O      -2.09443200    0.15984900    0.12780200
O      -0.59611800    1.24707700   -1.16844200
N       2.90770800    0.99287400    0.22544400
C       0.05000200   -0.76928600    0.00780900
C      -0.88458000    0.34614100   -0.43654500
C       2.13903400    0.22858200   -0.17742400
H       0.16544700   -0.75300900    1.09404400
H      -0.35516100   -1.73420200   -0.29272000
H      -2.66733500    0.88540500   -0.16390800
""",
)

entry(
    index = 62,
    label = "C3H3NO3_24",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,D}
3  N u0 p1 c0 {1,S} {5,D}
4  O u0 p2 c0 {2,S} {9,S}
5  C u0 p0 c0 {3,D} {10,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {2,D}
9  H u0 p0 c0 {4,S}
10 O u0 p2 c0 {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61692,0.0368092,-1.50827e-05,-1.14771e-08,8.80685e-12,-59519.2,12.3423], Tmin=(10,'K'), Tmax=(837.443,'K')),
            NASAPolynomial(coeffs=[7.81723,0.027248,-1.67663e-05,4.83695e-09,-5.33414e-13,-60591,-9.37517], Tmin=(837.443,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-494.895,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (220.334,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=N': 1, 'H-O': 1, 'C-C': 1, 'C=O': 2, 'C-H': 2, 'C-O': 1, 'C-N': 1}
1D rotors:
pivots: [1, 6], dihedral: [10, 1, 6, 2], rotor symmetry: 1, max scan energy: 54.13 kJ/mol
pivots: [4, 5], dihedral: [7, 4, 5, 6], rotor symmetry: 1, max scan energy: 10.81 kJ/mol
pivots: [5, 6], dihedral: [4, 5, 6, 1], rotor symmetry: 1, max scan energy: 19.86 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 7 4 5 6 F


External symmetry: 1, optical isomers: 1

Geometry:
O      -0.36711800   -0.57321500   -2.88469300
O       1.77621400   -0.35154600   -2.22489700
O       3.32297100    0.01928100    0.72903700
N       0.97816600   -0.18404700    0.46753900
C       0.00756500   -0.34708000   -0.56745500
C       0.60654000   -0.41972700   -1.96464700
C       2.18187400   -0.08750600    0.50968100
H      -0.70937600    0.47988100   -0.54801600
H      -0.57513000   -1.25850700   -0.40007700
H       0.06135500   -0.61400900   -3.75287100
""",
)

entry(
    index = 63,
    label = "C3H3NO3_26",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {4,S} {5,S}
2  C u0 p0 c0 {1,D} {3,S} {7,S}
3  O u0 p2 c0 {2,S} {6,S}
4  O u0 p2 c0 {1,S} {9,S}
5  O u0 p2 c0 {1,S} {8,S}
6  C u0 p0 c0 {3,S} {10,T}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {4,S}
10 N u0 p1 c0 {6,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.674,0.0258495,0.000113194,-3.72959e-07,3.15909e-10,-32387.3,12.9205], Tmin=(10,'K'), Tmax=(435.223,'K')),
            NASAPolynomial(coeffs=[6.37977,0.0333238,-2.40335e-05,7.988e-09,-9.9134e-13,-32929.1,-1.40133], Tmin=(435.223,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-269.299,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (220.334,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'H-O': 2, 'C-O': 4, 'C#N': 1, 'C-H': 1}
1D rotors:
pivots: [1, 6], dihedral: [7, 1, 6, 5], rotor symmetry: 1, max scan energy: 8.43 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 10 2 5 3 F
D 9 3 5 6 F
pivots: [2, 5], dihedral: [10, 2, 5, 3], rotor symmetry: 1, max scan energy: 16.76 kJ/mol
pivots: [3, 5], dihedral: [9, 3, 5, 2], rotor symmetry: 1, max scan energy: 38.50 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 7 1 6 5 F
D 10 2 5 6 F


External symmetry: 1, optical isomers: 2

Geometry:
O       1.24319000    0.44672700    0.41814700
O      -2.07896500   -0.94661900    0.54907000
O      -1.30585400    0.89785600   -0.46838200
N       2.63380600    1.44347700    2.17099800
C      -1.01867100   -0.16062600    0.31687200
C       0.18857700   -0.43507500    0.82135000
C       1.95325200    0.96448300    1.36799200
H       0.45760800   -1.28345000    1.42533000
H      -0.49655000    1.40188100   -0.62862500
H      -2.84149600   -0.56076300    0.10086400
""",
)

entry(
    index = 64,
    label = "C3H2NO3_27",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {7,S} {8,D}
3 O u0 p2 c0 {1,S} {4,S}
4 C u0 p0 c0 {3,S} {9,T}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u1 p2 c0 {2,S}
8 O u0 p2 c0 {2,D}
9 N u0 p1 c0 {4,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53927,0.0489351,-0.000139611,3.21071e-07,-2.93958e-10,-14024,13.026], Tmin=(10,'K'), Tmax=(337.997,'K')),
            NASAPolynomial(coeffs=[4.18419,0.0318939,-2.22277e-05,7.18386e-09,-8.7313e-13,-14013.9,11.4093], Tmin=(337.997,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-116.602,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (199.547,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 1, 'C=O': 1, 'C#N': 1, 'C-H': 2, 'C-O': 3}
1D rotors:
pivots: [1, 5], dihedral: [7, 1, 5, 6], rotor symmetry: 2, max scan energy: 18.86 kJ/mol
pivots: [5, 6], dihedral: [1, 5, 6, 2], rotor symmetry: 2, max scan energy: 10.25 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.23518600    0.40494700   -0.01989700
O       1.65383800   -2.30697900   -0.08867200
O      -0.11498100   -2.76417900   -1.11417500
N       1.06909500    0.70000100    2.40636200
C       0.22668900   -0.40782200   -0.65660300
C       0.60409600   -1.87174800   -0.61359900
C       1.13597300    0.53862500    1.26356400
H      -0.74973500   -0.26020300   -0.18994100
H       0.18563500   -0.07707800   -1.69414100
""",
)

entry(
    index = 65,
    label = "C3H2NO3_28",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {7,S}
2 C u0 p0 c0 {1,D} {4,S} {6,S}
3 O u0 p2 c0 {1,S} {5,S}
4 O u0 p2 c0 {2,S} {8,S}
5 C u0 p0 c0 {3,S} {9,T}
6 O u1 p2 c0 {2,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {4,S}
9 N u0 p1 c0 {5,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71886,0.0397084,-3.64689e-05,1.71168e-08,-3.34718e-12,-23321.9,11.5796], Tmin=(10,'K'), Tmax=(1081.46,'K')),
            NASAPolynomial(coeffs=[7.47725,0.0258072,-1.71876e-05,5.23077e-09,-5.99489e-13,-24134.8,-6.84679], Tmin=(1081.46,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-193.913,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (191.233,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'H-O': 1, 'C-O': 4, 'C#N': 1, 'C-H': 1}
1D rotors:
pivots: [1, 5], dihedral: [7, 1, 5, 6], rotor symmetry: 1, max scan energy: 20.62 kJ/mol
pivots: [2, 6], dihedral: [9, 2, 6, 3], rotor symmetry: 1, max scan energy: 45.00 kJ/mol
pivots: [5, 6], dihedral: [1, 5, 6, 2], rotor symmetry: 2, max scan energy: 54.31 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 8 1 5 6 F
pivots: [1, 7], dihedral: [5, 1, 7, 4], rotor symmetry: 1, max scan energy: 0.26 kJ/mol (set as a FreeRotor)


External symmetry: 1, optical isomers: 1

Geometry:
O      -1.07741200   -0.32644000    0.77439500
O       1.36363000   -1.35799900    0.76614400
O       2.03968600    0.09111500   -0.84627000
N      -3.35118100    0.58578900    0.82722800
C      -0.14954100    0.20980100   -0.09037100
C       1.18144500   -0.34232500   -0.10446200
C      -2.27250600    0.17427500    0.78244400
H      -0.44824500    1.02612800   -0.72986200
H       2.28338700   -1.64420800    0.66792900
""",
)

entry(
    index = 66,
    label = "C4H3N2O3_29",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,D}
3  C u0 p0 c0 {1,S} {9,D} {10,S}
4  O u0 p2 c0 {1,S} {6,S}
5  O u0 p2 c0 {2,S} {11,S}
6  C u0 p0 c0 {4,S} {12,T}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {2,D}
9  N u1 p1 c0 {3,D}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 N u0 p1 c0 {6,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.08272,0.0899264,-0.000263084,4.8383e-07,-3.47211e-10,-11729.4,15.2751], Tmin=(10,'K'), Tmax=(410.858,'K')),
            NASAPolynomial(coeffs=[6.42725,0.0414987,-2.83539e-05,8.95952e-09,-1.0676e-12,-11870.3,3.74435], Tmin=(410.858,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-97.5421,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (266.063,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=N': 1, 'H-O': 1, 'C-C': 2, 'C=O': 1, 'C#N': 1, 'C-H': 2, 'C-O': 3}
1D rotors:
pivots: [1, 6], dihedral: [9, 1, 6, 7], rotor symmetry: 1, max scan energy: 19.18 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 1 6 7 2 F
pivots: [2, 7], dihedral: [12, 2, 7, 3], rotor symmetry: 1, max scan energy: 53.82 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 7 6 8 11 F
pivots: [6, 7], dihedral: [1, 6, 7, 2], rotor symmetry: 1, max scan energy: 7.76 kJ/mol
pivots: [6, 8], dihedral: [1, 6, 8, 4], rotor symmetry: 1, max scan energy: 12.19 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.12993800   -0.77187200   -0.74298500
O      -0.76504400   -0.65764900    2.31986400
O       1.13385500   -1.76917300    1.80771600
N      -0.68325700    2.02068400    0.13790900
N       3.49488800   -0.24370000   -0.38339900
C       0.14903400   -0.26013200    0.18678100
C       0.26159000   -1.00052200    1.52709500
C       0.27233400    1.25607700    0.35054200
C       2.37435600   -0.49738900   -0.51514900
H      -0.81063100   -0.49295100   -0.27019100
H       1.25667400    1.63757900    0.65868200
H      -0.66549200   -1.13535200    3.15798000
""",
)

entry(
    index = 67,
    label = "C4H2N2O3_30",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,D}
3  O u0 p2 c0 {1,S} {6,S}
4  C u0 p0 c0 {1,S} {9,T}
5  O u0 p2 c0 {2,S} {10,S}
6  C u0 p0 c0 {3,S} {11,T}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {2,D}
9  N u0 p1 c0 {4,T}
10 H u0 p0 c0 {5,S}
11 N u0 p1 c0 {6,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65308,0.0436167,0.000469092,-4.25853e-06,1.00394e-08,-23394.2,12.3626], Tmin=(10,'K'), Tmax=(161.459,'K')),
            NASAPolynomial(coeffs=[6.16169,0.0392662,-2.74505e-05,8.82317e-09,-1.06547e-12,-23550.6,2.50146], Tmin=(161.459,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-192.132,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (245.277,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C-C': 2, 'C=O': 1, 'C#N': 2, 'C-H': 1, 'C-O': 3}
1D rotors:
pivots: [1, 6], dihedral: [9, 1, 6, 7], rotor symmetry: 1, max scan energy: 20.18 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 1 6 7 2 F
pivots: [2, 7], dihedral: [11, 2, 7, 3], rotor symmetry: 1, max scan energy: 56.40 kJ/mol
pivots: [6, 7], dihedral: [1, 6, 7, 2], rotor symmetry: 1, max scan energy: 10.38 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.15895800    0.76076300    0.62723900
O      -1.31867500    1.28791000   -1.94487700
O       0.67521300    2.29849400   -1.59358900
N      -0.25931500   -1.99428600   -0.85277900
N       3.33862900    0.22292700   -0.36075800
C      -0.04062400    0.50777200   -0.12544100
C      -0.15242800    1.48487900   -1.31923800
C      -0.16033600   -0.89220300   -0.53490400
C       2.29590900    0.47832300    0.06541700
H      -0.84654200    0.74095100    0.57335400
H      -1.37197400    1.90558100   -2.69099800
""",
)

entry(
    index = 68,
    label = "C4H2N2O3_31",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {3,S} {6,S}
2  C u0 p0 c0 {1,D} {4,S} {5,S}
3  O u0 p2 c0 {1,S} {7,S}
4  O u0 p2 c0 {2,S} {10,S}
5  O u0 p2 c0 {2,S} {9,S}
6  C u0 p0 c0 {1,S} {8,T}
7  C u0 p0 c0 {3,S} {11,T}
8  N u0 p1 c0 {6,T}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {4,S}
11 N u0 p1 c0 {7,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.42134,0.0506523,5.75189e-05,-3.76012e-07,3.9933e-10,-15355.8,14.4155], Tmin=(10,'K'), Tmax=(392.111,'K')),
            NASAPolynomial(coeffs=[8.63045,0.0349377,-2.55313e-05,8.59924e-09,-1.07971e-12,-16052,-9.50733], Tmin=(392.111,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-127.663,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (245.277,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'H-O': 2, 'C-O': 4, 'C-C': 1, 'C#N': 2}
1D rotors:
pivots: [1, 6], dihedral: [9, 1, 6, 7], rotor symmetry: 1, max scan energy: 11.11 kJ/mol
pivots: [2, 7], dihedral: [11, 2, 7, 3], rotor symmetry: 1, max scan energy: 22.52 kJ/mol
pivots: [3, 7], dihedral: [10, 3, 7, 2], rotor symmetry: 1, max scan energy: 28.38 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 9 1 6 7 F


External symmetry: 1, optical isomers: 2

Geometry:
O       2.11961100   -1.34975000    0.42016000
O      -0.93556800   -0.67894600    2.25854900
O      -0.05791100    0.30777100    0.51591700
N       1.33107000   -3.38596500    3.18495300
N       2.36712400   -3.02191000   -1.36170900
C       1.10189600   -1.56103200    1.40227300
C       0.06588500   -0.67587600    1.39196500
C       1.26145800   -2.56957000    2.36470300
C       2.22263200   -2.25580400   -0.50945900
H       0.72194600    0.32561700   -0.05668400
H      -0.84658000   -1.41935700    2.87548800
""",
)

entry(
    index = 69,
    label = "C4HN2O3_32",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {3,S} {4,S}
2  C u0 p0 c0 {1,D} {5,S} {7,S}
3  O u0 p2 c0 {1,S} {6,S}
4  C u0 p0 c0 {1,S} {8,T}
5  O u0 p2 c0 {2,S} {9,S}
6  C u0 p0 c0 {3,S} {10,T}
7  O u1 p2 c0 {2,S}
8  N u0 p1 c0 {4,T}
9  H u0 p0 c0 {5,S}
10 N u0 p1 c0 {6,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.09952,0.0967264,-0.000403692,9.74122e-07,-8.75962e-10,-5688.37,14.7456], Tmin=(10,'K'), Tmax=(343.375,'K')),
            NASAPolynomial(coeffs=[5.66311,0.038913,-2.90433e-05,9.68334e-09,-1.19543e-12,-5699.65,7.5174], Tmin=(343.375,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-47.3098,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (216.176,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'H-O': 1, 'C-O': 4, 'C-C': 1, 'C#N': 2}
1D rotors:
pivots: [1, 6], dihedral: [9, 1, 6, 7], rotor symmetry: 1, max scan energy: 16.50 kJ/mol
pivots: [2, 7], dihedral: [10, 2, 7, 3], rotor symmetry: 1, max scan energy: 46.58 kJ/mol
pivots: [6, 7], dihedral: [1, 6, 7, 2], rotor symmetry: 1, max scan energy: 38.52 kJ/mol
pivots: [1, 9], dihedral: [6, 1, 9, 5], rotor symmetry: 1, max scan energy: 0.50 kJ/mol (set as a FreeRotor)


External symmetry: 1, optical isomers: 1

Geometry:
O       1.06415100    1.29453300   -0.45607700
O      -2.42241800    0.68258000   -0.40882500
O      -1.26130300    2.62582900   -0.55473100
N      -0.10929900   -1.97358600   -0.21102000
N       3.26290100    0.21344800   -0.37609400
C      -0.10556500    0.57198500   -0.40151700
C      -1.30461500    1.42752700   -0.46503900
C      -0.10034300   -0.81322600   -0.29785800
C       2.21010200    0.68652900   -0.41105700
H      -3.17813400    1.28714600   -0.45375100
""",
)

entry(
    index = 70,
    label = "C3H3NO2_33",
    molecule = 
"""
1 O u0 p2 c0 {5,S} {9,S}
2 O u0 p2 c0 {5,D}
3 N u0 p1 c0 {6,T}
4 C u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
5 C u0 p0 c0 {1,S} {2,D} {4,S}
6 C u0 p0 c0 {3,T} {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98804,0.0222513,1.05407e-06,-1.19039e-08,4.46576e-12,-34700.3,10.8648], Tmin=(10,'K'), Tmax=(1216.47,'K')),
            NASAPolynomial(coeffs=[9.91406,0.0159055,-7.32402e-06,1.56737e-09,-1.27681e-13,-37114.3,-22.8822], Tmin=(1216.47,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-288.451,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (199.547,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C-C': 2, 'C=O': 1, 'C#N': 1, 'C-H': 2, 'C-O': 1}
1D rotors:
pivots: [1, 5], dihedral: [9, 1, 5, 2], rotor symmetry: 1, max scan energy: 55.97 kJ/mol
pivots: [4, 5], dihedral: [6, 4, 5, 1], rotor symmetry: 1, max scan energy: 4.59 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O       1.87435900   -0.09917600    0.22276400
O       0.48983500    1.67955400    0.19949700
N      -2.84522900    0.35914200   -0.08236900
C      -0.41551200   -0.57589800    0.04655300
C       0.66352300    0.49622700    0.16373100
C      -1.76551300   -0.03521400   -0.02422700
H      -0.20829500   -1.18029500   -0.84165400
H      -0.32794800   -1.25060300    0.90343800
H       2.53478000    0.60626500    0.29646700
""",
)

entry(
    index = 71,
    label = "C3H2NO2_35",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {5,S}
2 O u0 p2 c0 {5,D}
3 N u0 p1 c0 {6,T}
4 C u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
5 C u0 p0 c0 {1,S} {2,D} {4,S}
6 C u0 p0 c0 {3,T} {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79607,0.025424,-1.43026e-05,2.21584e-09,4.1491e-13,-4673.25,11.4452], Tmin=(10,'K'), Tmax=(1233.64,'K')),
            NASAPolynomial(coeffs=[8.70722,0.0145645,-7.25635e-06,1.73591e-09,-1.6224e-13,-6270.34,-14.8414], Tmin=(1233.64,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-38.8506,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 2, 'C=O': 1, 'C#N': 1, 'C-H': 2, 'C-O': 1}
1D rotors:
pivots: [4, 5], dihedral: [6, 4, 5, 1], rotor symmetry: 2, max scan energy: 4.49 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O       1.89812800   -0.04977400    0.18741300
O       1.02151900   -1.94846700    0.22422900
N      -0.53465800    2.48681800   -0.21721100
C      -0.54085900   -0.11634500   -0.04884200
C       0.83933500   -0.71534900    0.12619200
C      -0.53186400    1.33816000   -0.14237200
H      -0.98598400   -0.55067200   -0.94967400
H      -1.15821000   -0.43734200    0.79620900
""",
)

entry(
    index = 72,
    label = "C4H3N2O3_36",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {10,D}
3  C u0 p0 c0 {1,S} {5,S} {9,D}
4  O u0 p2 c0 {2,S} {6,S}
5  O u0 p2 c0 {3,S} {11,S}
6  C u0 p0 c0 {4,S} {12,T}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u0 p2 c0 {3,D}
10 N u1 p1 c0 {2,D}
11 H u0 p0 c0 {5,S}
12 N u0 p1 c0 {6,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.25738,0.0756857,-0.000161945,2.41896e-07,-1.54358e-10,-14546.8,16.6909], Tmin=(10,'K'), Tmax=(378.784,'K')),
            NASAPolynomial(coeffs=[6.40997,0.0423938,-3.0107e-05,9.85794e-09,-1.21016e-12,-14785.6,4.54198], Tmin=(378.784,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-120.936,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (261.906,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=N': 1, 'H-O': 1, 'C-C': 2, 'C=O': 1, 'C#N': 1, 'C-H': 2, 'C-O': 3}
1D rotors:
pivots: [1, 7], dihedral: [9, 1, 7, 4], rotor symmetry: 1, max scan energy: 19.88 kJ/mol
pivots: [2, 8], dihedral: [12, 2, 8, 3], rotor symmetry: 1, max scan energy: 56.06 kJ/mol
pivots: [6, 7], dihedral: [8, 6, 7, 1], rotor symmetry: 1, max scan energy: 22.74 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 11 6 8 2 F
pivots: [6, 8], dihedral: [7, 6, 8, 2], rotor symmetry: 1, max scan energy: 6.81 kJ/mol
pivots: [1, 9], dihedral: [7, 1, 9, 5], rotor symmetry: 1, max scan energy: 0.68 kJ/mol (set as a FreeRotor)


External symmetry: 1, optical isomers: 2

Geometry:
O       1.17917400   -0.51651900   -1.39965600
O      -2.70392200    0.02322300   -0.00687900
O      -1.05368200    1.45466700   -0.56121900
N       1.83124400   -0.23922100    0.82947300
N       3.40170100   -0.00435000   -2.30553100
C      -0.50301700   -0.74880700    0.29308300
C       0.93717000   -0.46558000   -0.01006400
C      -1.41491900    0.38687800   -0.15366600
C       2.37186900   -0.23393700   -1.83762000
H      -0.62314100   -0.89497800    1.36814000
H      -0.80636500   -1.67582600   -0.20115100
H      -3.24797500    0.77696600   -0.28252400
""",
)

entry(
    index = 73,
    label = "C4H3N2O2_37",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,D}
3  C u0 p0 c0 {4,S} {9,D} {10,S}
4  O u0 p2 c0 {2,S} {3,S}
5  C u0 p0 c0 {1,S} {11,T}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {2,D}
9  N u1 p1 c0 {3,D}
10 H u0 p0 c0 {3,S}
11 N u0 p1 c0 {5,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.27324,0.0660263,-0.000148836,2.29773e-07,-1.42287e-10,3104.5,12.8527], Tmin=(10,'K'), Tmax=(483.088,'K')),
            NASAPolynomial(coeffs=[5.223,0.0379749,-2.47638e-05,7.53024e-09,-8.70794e-13,3055.06,6.30287], Tmin=(483.088,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (25.7809,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (245.277,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=N': 1, 'C-C': 2, 'C=O': 1, 'C#N': 1, 'C-H': 3, 'C-O': 2}
1D rotors:
pivots: [1, 6], dihedral: [7, 1, 6, 2], rotor symmetry: 1, max scan energy: 50.16 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 6 1 7 3 F
pivots: [1, 7], dihedral: [6, 1, 7, 3], rotor symmetry: 1, max scan energy: 19.10 kJ/mol
pivots: [5, 6], dihedral: [8, 5, 6, 1], rotor symmetry: 1, max scan energy: 5.08 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O       0.37621400    0.28978700    1.56348400
O       0.18871100    1.49338900   -0.35851400
N       2.18970300    0.63736900    2.93067200
N      -2.86230700    0.39297500   -1.91795300
C      -1.51043100   -0.14412000    0.24500800
C      -0.23267200    0.66911600    0.39188000
C       1.57176200    0.92113100    1.88702100
C      -2.25347700    0.16774300   -0.96776800
H      -2.13498400    0.03219400    1.12612500
H      -1.24767600   -1.20625000    0.26402600
H       1.90980900    1.66651900    1.16415400
""",
)

entry(
    index = 74,
    label = "C4H4N2O3_38",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {5,S}
3  C u0 p0 c0 {2,D} {10,S} {11,S}
4  O u0 p2 c0 {1,S} {6,S}
5  C u0 p0 c0 {2,S} {12,T}
6  O u0 p2 c0 {4,S} {7,S}
7  N u0 p1 c0 {6,S} {13,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 N u0 p1 c0 {5,T}
13 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.75225,0.0891165,-0.00015471,1.44497e-07,-5.22419e-11,21939.1,14.9992], Tmin=(10,'K'), Tmax=(812.131,'K')),
            NASAPolynomial(coeffs=[9.5858,0.0362427,-2.15597e-05,6.06078e-09,-6.58094e-13,21462.9,-12.6451], Tmin=(812.131,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (182.189,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (291.007,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'N-O': 1, 'C=C': 1, 'O-O': 1, 'N=O': 1, 'C-C': 2, 'C#N': 1, 'C-H': 4, 'C-O': 1}
1D rotors:
pivots: [1, 2], dihedral: [6, 1, 2, 4], rotor symmetry: 1, max scan energy: 48.74 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 1 6 7 8 F
D 2 1 6 10 F
pivots: [1, 6], dihedral: [2, 1, 6, 7], rotor symmetry: 1, max scan energy: 44.14 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 6 1 2 4 F
D 1 6 7 8 F
pivots: [2, 4], dihedral: [1, 2, 4, 3], rotor symmetry: 1, max scan energy: 58.11 kJ/mol
pivots: [6, 7], dihedral: [1, 6, 7, 8], rotor symmetry: 1, max scan energy: 16.90 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.36719000    0.27648600   -0.40599500
O       2.53737600   -0.53232200   -0.55596800
O       3.18672700    0.52194200    1.31094100
N       3.53940400   -0.23910300    0.51830300
N      -2.18042500   -2.95710400    0.01511500
C       0.31359100   -0.53073500    0.10883600
C      -0.33111700   -1.42095500   -0.93984300
C       0.00043600   -1.41594400   -2.23252800
C      -1.35840400   -2.28285100   -0.43718200
H       0.66567000   -1.12672100    0.95570100
H      -0.41225500    0.19667200    0.48646100
H      -0.49511500   -2.06663000   -2.94089000
H       0.78038900   -0.75941000   -2.59420600
""",
)

entry(
    index = 75,
    label = "C4H3N2O3_39",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,D} {5,S}
2  C u1 p0 c0 {1,S} {4,S} {8,S}
3  C u0 p0 c0 {1,D} {9,S} {10,S}
4  O u0 p2 c0 {2,S} {6,S}
5  C u0 p0 c0 {1,S} {11,T}
6  O u0 p2 c0 {4,S} {7,S}
7  N u0 p1 c0 {6,S} {12,D}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 N u0 p1 c0 {5,T}
12 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.38412,0.0561437,9.60854e-06,-2.09343e-07,2.32882e-10,39005.5,15.6812], Tmin=(10,'K'), Tmax=(397.971,'K')),
            NASAPolynomial(coeffs=[7.20156,0.0421194,-2.92898e-05,9.52737e-09,-1.16738e-12,38508.8,-1.64059], Tmin=(397.971,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (324.312,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'N-O': 1, 'C=C': 1, 'O-O': 1, 'N=O': 1, 'C-C': 2, 'C#N': 1, 'C-H': 3, 'C-O': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [7, 1, 2, 4], invalidation reason: 
* Invalidated! pivots: [1, 7], dihedral: [2, 1, 7, 6], invalidation reason: 
* Invalidated! pivots: [2, 4], dihedral: [1, 2, 4, 3], invalidation reason: Another conformer for C4H3N2O3_39 exists which is 7.21 kJ/mol lower.
* Invalidated! pivots: [6, 7], dihedral: [8, 6, 7, 1], invalidation reason: 
* Invalidated! pivots: [6, 8], dihedral: [7, 6, 8, 11], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
O       1.12278600    0.26883400    0.72592200
O       2.51085800    0.11991200    0.48285700
O       2.21172400    1.90308100   -0.87964300
N       3.00076300    1.13129700   -0.56915700
N      -2.20702300   -2.35640600   -1.38814900
C      -0.93911200   -0.43453200   -0.19841500
C       0.42127100   -0.65667500    0.01380600
C      -1.62784600    0.70845800    0.17897800
C      -1.64255000   -1.50198200   -0.85554700
H       0.95886300   -1.54299200   -0.29106800
H      -2.68540400    0.80443100   -0.01811400
H      -1.11114100    1.52067700    0.66998400
""",
)

entry(
    index = 76,
    label = "C4H4NO2_40",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {5,S} {9,S}
4  C u0 p0 c0 {1,S} {10,T}
5  O u0 p2 c0 {3,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u1 p2 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 N u0 p1 c0 {4,T}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84002,0.0136886,0.00022426,-8.04199e-07,8.81091e-10,-14978.2,12.4574], Tmin=(10,'K'), Tmax=(307.417,'K')),
            NASAPolynomial(coeffs=[3.90469,0.0386778,-2.37089e-05,6.87448e-09,-7.72824e-13,-15104.2,10.2365], Tmin=(307.417,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-124.506,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (245.277,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'H-O': 1, 'C-C': 2, 'C#N': 1, 'C-H': 3, 'C-O': 2}
1D rotors:
pivots: [1, 6], dihedral: [11, 1, 6, 5], rotor symmetry: 1, max scan energy: 67.79 kJ/mol
pivots: [4, 5], dihedral: [7, 4, 5, 2], rotor symmetry: 1, max scan energy: 10.70 kJ/mol
pivots: [5, 6], dihedral: [2, 5, 6, 1], rotor symmetry: 1, max scan energy: 126.94 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 5 6 1 10 F
D 8 4 5 6 F
D 11 1 6 5 F


External symmetry: 1, optical isomers: 1

Geometry:
O      -0.07265500   -0.93116200    0.55706400
O       1.48428000   -0.31555900    2.59019200
N       4.53028800   -1.89976100   -0.66127300
C       3.55883100   -0.93694500    1.56190600
C       2.03720300   -0.76732700    1.57430500
C       1.23514200   -1.11407600    0.45014600
C       4.11686000   -1.47390100    0.32661800
H       3.82998700   -1.58859400    2.39822300
H       4.00638400    0.03975900    1.77009500
H       1.58342200   -1.51474900   -0.49075300
H      -0.20765800   -0.56872600    1.45873200
""",
)

entry(
    index = 77,
    label = "C4H3NO2_41",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {7,D}
3  C u0 p0 c0 {2,S} {8,D} {9,S}
4  C u0 p0 c0 {1,S} {10,T}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  O u0 p2 c0 {2,D}
8  O u0 p2 c0 {3,D}
9  H u0 p0 c0 {3,S}
10 N u0 p1 c0 {4,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.424,0.051617,-0.000105715,1.62021e-07,-1.01101e-10,-16165.6,11.0713], Tmin=(10,'K'), Tmax=(493.291,'K')),
            NASAPolynomial(coeffs=[4.23508,0.0346427,-2.24833e-05,6.80748e-09,-7.83881e-13,-16119.1,9.01365], Tmin=(493.291,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-134.436,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (224.491,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 3, 'C=O': 2, 'C#N': 1, 'C-H': 3}
1D rotors:
pivots: [4, 5], dihedral: [7, 4, 5, 1], rotor symmetry: 1, max scan energy: 15.87 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 1 5 6 2 F
pivots: [5, 6], dihedral: [1, 5, 6, 2], rotor symmetry: 2, max scan energy: 31.81 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O       1.21621700   -0.21553500    0.96321300
O      -0.35862000   -2.74852800   -0.78430800
N      -1.19691300    2.40137400    0.78816400
C      -0.98474300   -0.05522000   -0.05394800
C       0.33146900   -0.72830600    0.33202800
C       0.48831400   -2.17949100   -0.14998800
C      -1.09635200    1.31550400    0.41925400
H      -1.81192300   -0.66050100    0.33276900
H      -1.08803200   -0.09176100   -1.14396500
H       1.45227200   -2.63632100    0.14660100
""",
)

entry(
    index = 78,
    label = "C4H2NO2_42",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {4,S} {7,D}
3 C u0 p0 c0 {1,S} {8,T}
4 C u1 p0 c0 {2,S} {9,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {2,D}
8 N u0 p1 c0 {3,T}
9 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.45274,0.0503072,-9.94467e-05,1.26579e-07,-6.67392e-11,2144.33,14.1195], Tmin=(10,'K'), Tmax=(487.801,'K')),
            NASAPolynomial(coeffs=[6.35468,0.024777,-1.56078e-05,4.70982e-09,-5.45733e-13,1881.84,2.41403], Tmin=(487.801,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (17.8011,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (199.547,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 3, 'C=O': 2, 'C#N': 1, 'C-H': 2}
1D rotors:
pivots: [4, 5], dihedral: [6, 4, 5, 1], rotor symmetry: 1, max scan energy: 12.63 kJ/mol
pivots: [5, 7], dihedral: [1, 5, 7, 2], rotor symmetry: 1, max scan energy: 1.62 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O      -1.67674700   -1.04787700    0.72267700
O      -1.71169600    2.11230900   -0.09556300
N       2.08630100    1.39218100   -0.74133700
C       0.64308700   -0.61269500    0.09953900
C      -0.82160500   -0.23349100    0.32206000
C       1.47243100    0.49006200   -0.37077400
C      -1.23964900    1.07333300    0.07231400
H       0.67354100   -1.43442800   -0.62291300
H       1.03955100   -0.99880900    1.04391300
""",
)

entry(
    index = 79,
    label = "C2H2NO2_44",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 O u1 p2 c0 {1,S}
3 N u0 p1 c0 {5,T}
4 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5 C u0 p0 c0 {3,T} {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81975,0.0170764,8.96042e-07,-1.38405e-08,6.97669e-12,19201.9,11.131], Tmin=(10,'K'), Tmax=(841.687,'K')),
            NASAPolynomial(coeffs=[4.82466,0.0178386,-1.03319e-05,2.86985e-09,-3.08525e-13,18836.5,5.29076], Tmin=(841.687,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (159.643,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (153.818,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'O-O': 1, 'C-C': 1, 'C#N': 1, 'C-H': 2, 'C-O': 1}
1D rotors:
pivots: [1, 4], dihedral: [2, 1, 4, 5], rotor symmetry: 1, max scan energy: 9.38 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O      -0.54639100    1.04548100   -0.38914900
O      -1.80777300    1.33279900   -0.15796400
N       2.27106500   -0.81039900   -0.37491600
C      -0.23825000   -0.29598400    0.11007600
C       1.16409500   -0.57445100   -0.16490500
H      -0.43874300   -0.31474200    1.18270200
H      -0.88728100   -1.00783800   -0.40285300
""",
)

entry(
    index = 80,
    label = "C3H3NO3_46",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,D} {9,S}
3  O u0 p2 c0 {1,S} {4,S}
4  O u0 p2 c0 {2,S} {3,S}
5  C u0 p0 c0 {1,S} {10,T}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {2,D}
9  H u0 p0 c0 {2,S}
10 N u0 p1 c0 {5,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82045,0.0381307,-2.75188e-05,9.51207e-09,-1.28377e-12,-16751.3,12.9454], Tmin=(10,'K'), Tmax=(1745.51,'K')),
            NASAPolynomial(coeffs=[14.5344,0.0135785,-6.41986e-06,1.45367e-09,-1.29608e-13,-20491.5,-44.7116], Tmin=(1745.51,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-139.286,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (220.334,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'O-O': 1, 'C-C': 1, 'C=O': 1, 'C#N': 1, 'C-H': 3, 'C-O': 2}
1D rotors:
pivots: [1, 2], dihedral: [5, 1, 2, 6], rotor symmetry: 1, max scan energy: 38.05 kJ/mol
pivots: [1, 5], dihedral: [2, 1, 5, 7], rotor symmetry: 1, max scan energy: 19.84 kJ/mol
pivots: [2, 6], dihedral: [1, 2, 6, 3], rotor symmetry: 1, max scan energy: 70.12 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 5 1 2 6 F


External symmetry: 1, optical isomers: 2

Geometry:
O       0.05341000    0.60492900    0.76625700
O      -1.26770200    0.01241200    0.83326800
O      -0.62198200   -0.95327300    2.80730800
N       0.36684700   -0.78302500   -2.37735400
C       0.93695400   -0.31570100    0.13564700
C      -1.44425100   -0.69965900    1.98703000
C       0.60976400   -0.56769900   -1.27259300
H       1.90669500    0.18442200    0.20565200
H       0.98984000   -1.25588600    0.69002800
H      -2.50314800   -1.00295600    1.98187400
""",
)

entry(
    index = 81,
    label = "C4H2NO_47",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {5,D}
2 N u0 p1 c0 {6,T}
3 C u0 p0 c0 {4,D} {5,S} {6,S}
4 C u0 p0 c0 {3,D} {7,S} {8,S}
5 C u1 p0 c0 {1,D} {3,S}
6 C u0 p0 c0 {2,T} {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81992,0.0132782,0.000131334,-4.11757e-07,3.61876e-10,27825.7,10.8104], Tmin=(10,'K'), Tmax=(410.104,'K')),
            NASAPolynomial(coeffs=[5.84251,0.0234829,-1.54707e-05,4.86123e-09,-5.86094e-13,27408.1,-0.213382], Tmin=(410.104,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (231.358,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'C-C': 2, 'C=O': 1, 'C#N': 1, 'C-H': 2}
1D rotors:
* Invalidated! pivots: [3, 5], dihedral: [4, 3, 5, 1], invalidation reason: 
pivots: [3, 4], dihedral: [5, 3, 4, 7], rotor symmetry: 2, max scan energy: 42.92 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 3 4 7 8 F
D 4 3 5 6 F


External symmetry: 1, optical isomers: 1

Geometry:
O      -1.65474700   -1.86163200   -0.76675800
N      -1.32458200    2.15732200    0.75994800
C      -0.14534400   -0.01008200   -0.00956200
C       1.27442000   -0.13211500    0.00079200
C      -0.96614900   -1.00271000   -0.41596000
C      -0.80735400    1.18384700    0.41383500
H       1.86682300    0.70329600    0.33892000
H       1.75661200   -1.04203200   -0.32277400
""",
)

entry(
    index = 82,
    label = "C4H4NO2_48",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {5,S}
3  C u0 p0 c0 {2,D} {8,S} {9,S}
4  O u0 p2 c0 {1,S} {10,S}
5  C u0 p0 c0 {2,S} {11,T}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u1 p2 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 N u0 p1 c0 {5,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79071,0.0195691,0.000260924,-1.1377e-06,1.472e-09,-9009.21,12.1918], Tmin=(10,'K'), Tmax=(267.263,'K')),
            NASAPolynomial(coeffs=[4.46211,0.0401517,-2.65116e-05,8.11969e-09,-9.47137e-13,-9154.49,7.79192], Tmin=(267.263,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-74.8812,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (245.277,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'H-O': 1, 'C-C': 2, 'C#N': 1, 'C-H': 3, 'C-O': 2}
1D rotors:
pivots: [1, 4], dihedral: [11, 1, 4, 5], rotor symmetry: 1, max scan energy: 30.06 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 8 4 5 6 F
pivots: [4, 5], dihedral: [1, 4, 5, 6], rotor symmetry: 1, max scan energy: 22.43 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 11 1 4 5 F
pivots: [5, 6], dihedral: [4, 5, 6, 2], rotor symmetry: 1, max scan energy: 66.14 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 11 1 4 5 F
D 8 4 5 6 F


External symmetry: 1, optical isomers: 2

Geometry:
O       1.34210500   -0.94667200    1.40520200
O       0.92146200   -1.65097900   -1.25740700
N      -3.04098100    0.39637500    0.16567400
C       0.40496600    0.03336300    1.03922400
C      -0.62425000   -0.44037700    0.03442300
C      -0.23470100   -1.28905800   -1.08350400
C      -1.94276900    0.01400400    0.10494400
H      -0.09808200    0.36329200    1.94992000
H       0.88906100    0.92519200    0.60107000
H      -1.03606200   -1.58140400   -1.78270700
H       1.73411400   -1.28674500    0.58921500
""",
)

entry(
    index = 83,
    label = "C4H3NO2_49",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {5,S}
3  O u0 p2 c0 {1,S} {8,S}
4  C u0 p0 c0 {2,D} {9,D}
5  C u0 p0 c0 {2,S} {10,T}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  O u0 p2 c0 {4,D}
10 N u0 p1 c0 {5,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.32017,0.0535341,-8.40211e-05,7.78109e-08,-2.93738e-11,-11391.9,12.7218], Tmin=(10,'K'), Tmax=(713.171,'K')),
            NASAPolynomial(coeffs=[7.5824,0.0251191,-1.47723e-05,4.21204e-09,-4.66136e-13,-11885.2,-5.59626], Tmin=(713.171,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-94.81,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (224.491,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'H-O': 1, 'C-C': 2, 'C=O': 1, 'C#N': 1, 'C-H': 2, 'C-O': 1}
1D rotors:
pivots: [1, 4], dihedral: [10, 1, 4, 5], rotor symmetry: 1, max scan energy: 12.84 kJ/mol
pivots: [4, 5], dihedral: [1, 4, 5, 6], rotor symmetry: 1, max scan energy: 16.97 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 10 1 4 5 F


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.70195100   -0.06036900   -0.87728100
O       0.92485600    2.06912100    1.69630600
N       2.27290700   -0.57137100   -1.59481200
C      -0.84491100   -0.50382200    0.14940700
C       0.53198100    0.17721200    0.14420500
C       0.76229300    1.19981600    0.95595200
C       1.51412500   -0.20985200   -0.79887200
H      -1.35239600   -0.28556500    1.08924600
H      -0.67033000   -1.58468900    0.09981200
H      -1.32943400   -0.32643500   -1.72503600
""",
)

entry(
    index = 84,
    label = "C3H7NO3_50",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {7,S}
3  C u0 p0 c0 {2,D} {5,S} {11,S}
4  N u0 p1 c0 {6,S} {12,S} {13,S}
5  O u0 p2 c0 {3,S} {6,S}
6  O u0 p2 c0 {4,S} {5,S}
7  O u0 p2 c0 {2,S} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84954,0.0208713,0.000669366,-5.52071e-06,1.42798e-08,-21806.1,9.4991], Tmin=(10,'K'), Tmax=(131.75,'K')),
            NASAPolynomial(coeffs=[4.11339,0.0475221,-2.86873e-05,8.36379e-09,-9.42377e-13,-21843.2,7.6193], Tmin=(131.75,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-175.118,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'N-O': 1, 'C=C': 1, 'H-N': 2, 'O-O': 1, 'H-O': 1, 'C-C': 1, 'C-H': 4, 'C-O': 2}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [7, 1, 2, 4], invalidation reason: 
* Invalidated! pivots: [1, 7], dihedral: [2, 1, 7, 6], invalidation reason: 
* Invalidated! pivots: [2, 4], dihedral: [1, 2, 4, 12], invalidation reason: 
* Invalidated! pivots: [3, 6], dihedral: [14, 3, 6, 5], invalidation reason: 
* Invalidated! pivots: [5, 6], dihedral: [8, 5, 6, 3], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
O       0.12307400   -0.03856600   -3.03543800
O       1.22883700   -1.58180500   -2.90490500
O      -0.07977000    0.43354300   -0.44799100
N       2.09666600   -1.54842900   -3.85655600
C      -2.39156400   -0.15251000   -0.31417400
C      -1.15281600   -0.00672500   -1.11998000
C      -1.02065600   -0.26407000   -2.46713000
H      -2.66581400    0.80436200    0.14212600
H      -2.23346200   -0.86510900    0.50220800
H      -3.21925500   -0.50108400   -0.93277300
H      -1.85265400   -0.68948400   -3.03202900
H       1.72133600   -1.66702000   -4.79691700
H       2.81530000   -0.82970600   -3.77715800
H       0.63132000    0.45986200   -1.11810200
""",
)

entry(
    index = 85,
    label = "C3H2N2O2_51",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 N u0 p0 c+1 {1,S} {5,S} {6,D}
3 C u0 p0 c0 {1,D} {7,S} {8,S}
4 C u0 p0 c0 {1,S} {9,T}
5 O u0 p3 c-1 {2,S}
6 O u0 p2 c0 {2,D}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 N u0 p1 c0 {4,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76746,0.019617,6.07063e-05,-1.56851e-07,1.04215e-10,21130.2,11.4567], Tmin=(10,'K'), Tmax=(537.098,'K')),
            NASAPolynomial(coeffs=[4.65721,0.0309159,-2.09103e-05,6.59276e-09,-7.84955e-13,20776.1,5.31033], Tmin=(537.098,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (175.65,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (203.705,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'N-O': 1, 'C=C': 1, 'N=O': 1, 'C-C': 1, 'C#N': 1, 'C-H': 2, 'C-N': 1}
1D rotors:
pivots: [3, 5], dihedral: [1, 3, 5, 6], rotor symmetry: 2, max scan energy: 22.66 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O      -1.55573700    1.42033300   -0.30500500
O       0.45798900    2.20097500   -0.04822100
N      -0.35849000    1.30065500   -0.12157300
N      -1.60218200   -1.98371500   -0.13250300
C       0.15180200   -0.10273500    0.02787200
C       1.45001800   -0.30713100    0.23070600
C      -0.83900300   -1.12116700   -0.06504700
H       2.12047500    0.54028100    0.28524200
H       1.83955900   -1.31014400    0.34118900
""",
)

entry(
    index = 86,
    label = "C4H2NO3_52",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {6,S}
2  O u0 p2 c0 {6,D}
3  O u1 p2 c0 {1,S}
4  N u0 p1 c0 {8,T}
5  C u0 p0 c0 {6,S} {7,D} {8,S}
6  C u0 p0 c0 {1,S} {2,D} {5,S}
7  C u0 p0 c0 {5,D} {9,S} {10,S}
8  C u0 p0 c0 {4,T} {5,S}
9  H u0 p0 c0 {7,S}
10 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.5969,0.0354225,3.19259e-05,-1.26691e-07,8.7359e-11,10395.8,13.0517], Tmin=(10,'K'), Tmax=(580.719,'K')),
            NASAPolynomial(coeffs=[7.42835,0.032915,-2.32884e-05,7.51678e-09,-9.06204e-13,9548.06,-6.81786], Tmin=(580.719,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (86.3758,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (224.491,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'O-O': 1, 'C-C': 2, 'C=O': 1, 'C#N': 1, 'C-H': 2, 'C-O': 1}
1D rotors:
pivots: [1, 6], dihedral: [3, 1, 6, 2], rotor symmetry: 1, max scan energy: 27.31 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 7 5 6 1 F
pivots: [5, 6], dihedral: [7, 5, 6, 1], rotor symmetry: 1, max scan energy: 24.73 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O       1.84474800    0.71139400    0.22172200
O       1.33044800   -1.20307200   -0.95404800
O       3.11502600    0.50145300   -0.07990200
N      -0.96056900    2.13966000    1.51399200
C      -0.43696000    0.04822900    0.08825100
C       0.96532900   -0.28023500   -0.30749100
C      -1.41629700   -0.77275100   -0.31718500
C      -0.70909500    1.21025000    0.87796200
H      -1.17225200   -1.64300200   -0.91384700
H      -2.45080700   -0.58581600   -0.06118400
""",
)

entry(
    index = 87,
    label = "C4H3NO3_53",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {6,S}
2  O u0 p2 c0 {1,S} {11,S}
3  O u0 p2 c0 {6,D}
4  N u0 p1 c0 {8,T}
5  C u0 p0 c0 {6,S} {7,D} {8,S}
6  C u0 p0 c0 {1,S} {3,D} {5,S}
7  C u0 p0 c0 {5,D} {9,S} {10,S}
8  C u0 p0 c0 {4,T} {5,S}
9  H u0 p0 c0 {7,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.69281,0.0213749,0.000197978,-5.94162e-07,4.86867e-10,-13168.6,12.3376], Tmin=(10,'K'), Tmax=(450.433,'K')),
            NASAPolynomial(coeffs=[9.02751,0.0304121,-1.99732e-05,6.45605e-09,-8.06261e-13,-14221.5,-15.4969], Tmin=(450.433,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-109.521,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (245.277,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'O-O': 1, 'H-O': 1, 'C-C': 2, 'C=O': 1, 'C#N': 1, 'C-H': 2, 'C-O': 1}
1D rotors:
pivots: [1, 2], dihedral: [6, 1, 2, 11], rotor symmetry: 1, max scan energy: 13.03 kJ/mol
pivots: [1, 6], dihedral: [2, 1, 6, 3], rotor symmetry: 1, max scan energy: 97.84 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 8 5 6 1 F
D 6 1 2 11 F
pivots: [5, 6], dihedral: [7, 5, 6, 1], rotor symmetry: 1, max scan energy: 22.85 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O       1.35534600    0.46649300    1.00315600
O       2.64355500    1.03358700    0.73027400
O       1.35971000   -0.07058000   -1.17578000
N      -1.51465200   -0.55821600    2.57580400
C      -0.53247800   -0.66541600    0.18737700
C       0.80980000   -0.07532100   -0.10021900
C      -1.20211100   -1.24404800   -0.81775700
C      -1.06535500   -0.59969300    1.51377000
H      -2.17738200   -1.68646900   -0.66403500
H      -0.76105000   -1.27137800   -1.80623100
H       2.73475700    0.84118000   -0.22880900
""",
)

entry(
    index = 88,
    label = "C4H3N2O3_54",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,D}
3  C u0 p0 c0 {2,S} {4,S} {10,D}
4  O u0 p2 c0 {3,S} {6,S}
5  O u0 p2 c0 {1,S} {11,S}
6  C u0 p0 c0 {4,S} {12,T}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u0 p2 c0 {2,D}
10 N u1 p1 c0 {3,D}
11 H u0 p0 c0 {5,S}
12 N u0 p1 c0 {6,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.22578,0.0675696,-5.73692e-05,-1.76741e-08,3.87935e-11,-1070.4,16.1809], Tmin=(10,'K'), Tmax=(565.079,'K')),
            NASAPolynomial(coeffs=[10.7458,0.0348228,-2.48193e-05,8.07636e-09,-9.80717e-13,-2247.33,-18.7003], Tmin=(565.079,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-8.98703,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (261.906,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=N': 1, 'H-O': 1, 'C-C': 2, 'C=O': 1, 'C#N': 1, 'C-H': 2, 'C-O': 3}
1D rotors:
pivots: [1, 8], dihedral: [9, 1, 8, 4], rotor symmetry: 1, max scan energy: 15.67 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 3 7 8 4 F
pivots: [2, 6], dihedral: [12, 2, 6, 7], rotor symmetry: 1, max scan energy: 20.78 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 2 6 7 3 F
pivots: [6, 7], dihedral: [2, 6, 7, 3], rotor symmetry: 1, max scan energy: 19.29 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 12 2 6 7 F
pivots: [7, 8], dihedral: [3, 7, 8, 1], rotor symmetry: 1, max scan energy: 36.92 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 2 6 7 3 F
D 12 2 6 11 F
pivots: [1, 9], dihedral: [8, 1, 9, 5], rotor symmetry: 1, max scan energy: 0.62 kJ/mol (set as a FreeRotor)


External symmetry: 1, optical isomers: 2

Geometry:
O       1.93459700   -0.54159100    0.61641100
O      -1.80604900    1.02018400   -0.66831000
O      -0.02160500   -2.01963500   -0.28887200
N       0.48099200    1.31056500    0.70643700
N       3.86789400    0.67770400    1.51173300
C      -1.75369200   -0.32644300   -0.29074700
C      -0.34038400   -0.88450700   -0.10657400
C       0.71218300    0.12353200    0.43951800
C       2.93547700    0.14152300    1.09304300
H      -2.22547900   -0.91609800   -1.07730600
H      -2.28396400   -0.53168800    0.65269000
H      -1.50160800    1.57990600    0.05941500
""",
)

entry(
    index = 89,
    label = "H2NCHO_59",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 N u0 p1 c0 {3,S} {4,S} {5,S}
3 C u0 p0 c0 {1,D} {2,S} {6,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98383,0.000990418,4.40096e-05,-7.86098e-08,4.60751e-11,-24762.6,6.55204], Tmin=(10,'K'), Tmax=(438.815,'K')),
            NASAPolynomial(coeffs=[2.273,0.0166057,-9.43745e-06,2.69448e-09,-3.05266e-13,-24612.7,13.3944], Tmin=(438.815,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-205.894,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (128.874,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-N': 1, 'C=O': 1, 'H-N': 2, 'C-H': 1}
1D rotors:
pivots: [2, 3], dihedral: [4, 2, 3, 1], rotor symmetry: 2, max scan energy: 102.31 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 5 4 2 3 F


External symmetry: 1, optical isomers: 1

Geometry:
O       1.64349900    0.10664900   -0.50943000
N      -0.52784600    0.43268500    0.11288200
C       0.57556700   -0.32346000   -0.13920500
H      -1.39178100    0.01858500    0.41957400
H      -0.47681500    1.43222400   -0.01117600
H       0.38663800   -1.40118300    0.03512000
""",
)

entry(
    index = 90,
    label = "C4H7N2O3_38",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  N u0 p1 c0 {5,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {4,S}
6  C u0 p0 c0 {1,S} {16,T}
7  O u0 p2 c0 {2,S} {15,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u1 p2 c0 {7,S}
16 N u0 p1 c0 {6,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.56733,0.0346499,0.000240356,-8.02945e-07,7.4469e-10,9492.51,13.9015], Tmin=(10,'K'), Tmax=(384.294,'K')),
            NASAPolynomial(coeffs=[6.12309,0.0570469,-3.83218e-05,1.22883e-08,-1.49771e-12,8934.27,-0.691838], Tmin=(384.294,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (78.9518,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (374.151,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'N-O': 1, 'C-C': 3, 'O-O': 1, 'C-O': 2, 'C#N': 1, 'H-N': 2}
1D rotors:
* Invalidated! pivots: [1, 4], dihedral: [6, 1, 4, 15], invalidation reason: 
pivots: [1, 6], dihedral: [4, 1, 6, 7], rotor symmetry: 1, max scan energy: 48.33 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 1 6 7 11 F
D 6 1 4 15 F
D 3 2 7 11 F
* Invalidated! pivots: [2, 7], dihedral: [3, 2, 7, 6], invalidation reason: Another conformer for C4H7N2O3_38 exists which is 7.29 kJ/mol lower.
* Invalidated! pivots: [6, 7], dihedral: [1, 6, 7, 2], invalidation reason: 
pivots: [6, 8], dihedral: [1, 6, 8, 12], rotor symmetry: 3, max scan energy: 12.35 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       0.70208400   -0.31952400    0.95216200
O       0.44823300    2.38732500   -0.05390700
O       1.74303300    2.13590600   -0.11896700
N       1.45746000   -0.87468300   -0.14667600
N      -1.73603300    1.17693300    2.60077900
C      -0.55218400    0.18339000    0.47757800
C      -0.34550400    1.29495300   -0.57324900
C      -1.43736600   -0.92682100   -0.11090000
C      -1.18952300    0.74632600    1.68341100
H       0.16200500    0.88189800   -1.44368900
H      -1.29794700    1.74817200   -0.84837500
H      -1.60894400   -1.69108800    0.64786100
H      -0.92324200   -1.37529800   -0.96069000
H      -2.40261600   -0.53093600   -0.43268200
H       2.23941700   -0.22689400   -0.24090300
H       1.82302500   -1.73856900    0.24660500
""",
)

entry(
    index = 91,
    label = "H2NCO_60",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 C u1 p0 c0 {1,S} {5,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97473,0.00159227,3.91944e-05,-8.04966e-08,5.17325e-11,-3324.73,6.89951], Tmin=(10,'K'), Tmax=(498.576,'K')),
            NASAPolynomial(coeffs=[3.39344,0.0115287,-6.56398e-06,1.90111e-09,-2.20439e-13,-3332.3,8.64207], Tmin=(498.576,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-27.6504,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (103.931,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'H-N': 2, 'C-N': 1}
1D rotors:
pivots: [2, 3], dihedral: [4, 2, 3, 1], rotor symmetry: 2, max scan energy: 88.63 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 5 4 2 3 F


External symmetry: 1, optical isomers: 1

Geometry:
O       1.66048400    0.53866100   -0.35022000
N      -0.49160500   -0.12594900    0.10040300
C       0.82306900   -0.28006700   -0.12002400
H      -1.07049900   -0.92655100    0.28249700
H      -0.92145000    0.79390700    0.08734400
""",
)

entry(
    index = 92,
    label = "C4H3N2O2_28",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {7,D}
3  C u0 p0 c0 {1,S} {8,D} {9,S}
4  C u0 p0 c0 {1,S} {10,T}
5  O u0 p2 c0 {2,S} {11,S}
6  H u0 p0 c0 {1,S}
7  O u0 p2 c0 {2,D}
8  N u1 p1 c0 {3,D}
9  H u0 p0 c0 {3,S}
10 N u0 p1 c0 {4,T}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.629,0.0484038,-4.23324e-05,1.91277e-08,-3.60358e-12,-1014.53,13.7699], Tmin=(10,'K'), Tmax=(1123.05,'K')),
            NASAPolynomial(coeffs=[8.30408,0.0317525,-2.00921e-05,5.92531e-09,-6.64624e-13,-2064.6,-9.32721], Tmin=(1123.05,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-8.45063,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (245.277,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 2, 'H-O': 1, 'C=N': 1, 'C=O': 1, 'C-C': 3, 'C#N': 1, 'C-O': 1}
1D rotors:
pivots: [1, 6], dihedral: [11, 1, 6, 2], rotor symmetry: 1, max scan energy: 56.59 kJ/mol
pivots: [5, 6], dihedral: [7, 5, 6, 1], rotor symmetry: 1, max scan energy: 6.18 kJ/mol
pivots: [5, 7], dihedral: [6, 5, 7, 3], rotor symmetry: 1, max scan energy: 18.55 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 8 5 6 2 F


External symmetry: 1, optical isomers: 2

Geometry:
O       1.99497800    0.58384900   -0.38249500
O       1.19691300   -0.40229000    1.48178400
N      -1.74282300   -2.00499000   -0.37749800
N      -1.39056000    2.30769700   -0.49832400
C      -0.28380800   -0.05964300   -0.41309800
C       1.04457000    0.00715100    0.36635800
C      -1.23255700   -1.06701000    0.25538800
C      -0.89536700    1.26762400   -0.47214700
H      -0.07237200   -0.38893900   -1.43357500
H      -1.42061700   -0.91886500    1.32571600
H       2.80350100    0.63166900    0.15141500
""",
)

entry(
    index = 93,
    label = "C2N2O2_61",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {6,S}
2 O u0 p2 c0 {5,D}
3 N u0 p1 c0 {1,S} {5,D}
4 N u0 p1 c0 {6,T}
5 C u0 p0 c0 {2,D} {3,D}
6 C u0 p0 c0 {1,S} {4,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72706,0.0239254,-1.07731e-05,-1.98071e-08,1.8762e-11,19414.7,10.2012], Tmin=(10,'K'), Tmax=(607.148,'K')),
            NASAPolynomial(coeffs=[6.34812,0.0152643,-1.06395e-05,3.39476e-09,-4.05765e-13,18937.8,-2.44251], Tmin=(607.148,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (161.389,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (128.874,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'N-O': 1, 'C-O': 1, 'C=O': 1, 'C#N': 1, 'C=N': 1}
1D rotors:
pivots: [1, 3], dihedral: [6, 1, 3, 5], rotor symmetry: 1, max scan energy: 19.01 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O      -0.33063100    0.24531600   -0.59062700
O       2.74578800   -0.26589200    0.56735400
N       0.36344200   -0.41145000    0.51145900
N      -2.76247600   -0.02084900   -0.46508000
C       1.59482400   -0.28342700    0.45837200
C      -1.61094700    0.07746400   -0.48147800
""",
)

entry(
    index = 94,
    label = "C4H7N2O3_39",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  O u0 p2 c0 {1,S} {8,S}
5  O u0 p2 c0 {2,S} {7,S}
6  C u0 p0 c0 {1,S} {14,T}
7  O u0 p2 c0 {5,S} {15,S}
8  N u1 p1 c0 {4,S} {16,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 N u0 p1 c0 {6,T}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.2692,0.0631976,-4.11262e-05,1.15822e-08,-8.29343e-13,8884.89,14.2106], Tmin=(10,'K'), Tmax=(1213.9,'K')),
            NASAPolynomial(coeffs=[12.5632,0.0396658,-2.08137e-05,5.24056e-09,-5.14703e-13,6105.85,-34.582], Tmin=(1213.9,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (73.8081,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (378.308,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C-H': 5, 'N-O': 1, 'C-C': 3, 'O-O': 1, 'C-O': 2, 'C#N': 1, 'H-N': 1}
1D rotors:
pivots: [1, 4], dihedral: [6, 1, 4, 16], rotor symmetry: 1, max scan energy: 67.17 kJ/mol
* Invalidated! pivots: [1, 6], dihedral: [4, 1, 6, 7], invalidation reason: Another conformer for C4H7N2O3_39 exists which is 4.97 kJ/mol lower.
* Invalidated! pivots: [2, 3], dihedral: [7, 2, 3, 15], invalidation reason: 
* Invalidated! pivots: [2, 7], dihedral: [3, 2, 7, 6], invalidation reason: 
* Invalidated! pivots: [6, 7], dihedral: [1, 6, 7, 2], invalidation reason: 
* Invalidated! pivots: [6, 8], dihedral: [1, 6, 8, 12], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.21374600    1.48513800   -0.80636600
O       0.19647300   -1.10535800    1.80801900
O       1.59424800   -1.49354500    1.83894500
N       1.01805100    2.07284400   -0.71479700
N       1.55540300   -1.38584100   -1.48963200
C      -0.20778000    0.13698900   -0.27667800
C       0.10394800    0.19111900    1.24217400
C      -1.60476300   -0.41826700   -0.55073000
C       0.80474500   -0.67951200   -0.97415000
H       1.02289900    0.74892600    1.41662600
H      -0.73400500    0.68397300    1.74313000
H      -1.78721400   -0.49721400   -1.62262000
H      -1.70022700   -1.40381000   -0.09406800
H      -2.34405300    0.25367300   -0.11081800
H       1.66446200   -2.04660500    1.04546500
H       0.81299900    2.99199700   -1.12626500
""",
)

entry(
    index = 95,
    label = "C4H7N2O2_62",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  N u0 p1 c0 {5,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {4,S}
6  C u0 p0 c0 {1,S} {15,T}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u1 p2 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 N u0 p1 c0 {6,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.56195,0.0476425,0.000262246,-1.70621e-06,2.86356e-09,7314.93,12.9226], Tmin=(10,'K'), Tmax=(222.392,'K')),
            NASAPolynomial(coeffs=[5.70431,0.0502527,-3.2866e-05,1.03393e-08,-1.24514e-12,7117.9,3.52008], Tmin=(222.392,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (60.9026,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (340.893,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 6, 'N-O': 2, 'C-C': 3, 'C-O': 1, 'C#N': 1, 'H-N': 1}
1D rotors:
pivots: [1, 3], dihedral: [5, 1, 3, 2], rotor symmetry: 1, max scan energy: 18.02 kJ/mol
pivots: [1, 5], dihedral: [3, 1, 5, 6], rotor symmetry: 1, max scan energy: 24.94 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 5 1 3 2 F
pivots: [5, 6], dihedral: [1, 5, 6, 9], rotor symmetry: 3, max scan energy: 13.31 kJ/mol
pivots: [5, 7], dihedral: [1, 5, 7, 12], rotor symmetry: 3, max scan energy: 13.71 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       0.13171500    1.25197200   -0.12915600
O      -1.98128500    1.42827800    0.87218700
N      -1.20288000    1.81706100   -0.01015800
N       0.00268100   -0.77583100    2.64350300
C       0.20435600   -0.17273400    0.08914300
C      -0.82636900   -0.94345000   -0.74715600
C       1.64284700   -0.51344800   -0.32895000
C       0.05101900   -0.47985100    1.53098600
H      -0.70629400   -0.66744400   -1.79669500
H      -1.84248900   -0.72086500   -0.42776500
H      -0.65433600   -2.01607500   -0.64052700
H       2.35383400    0.08735600    0.23857000
H       1.76515800   -0.30278500   -1.39240600
H       1.84419300   -1.56935300   -0.14259400
H      -1.03515400    2.82175800   -0.13011700
""",
)

entry(
    index = 96,
    label = "C4H2N2O3_7",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,D}
3  N u0 p1 c0 {1,S} {6,D}
4  C u0 p0 c0 {1,S} {9,T}
5  O u0 p2 c0 {2,S} {10,S}
6  C u0 p0 c0 {3,D} {11,D}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {2,D}
9  N u0 p1 c0 {4,T}
10 H u0 p0 c0 {5,S}
11 O u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.54784,0.0497988,-4.06961e-05,1.54084e-08,-2.09173e-12,-38920.9,13.8242], Tmin=(10,'K'), Tmax=(1186,'K')),
            NASAPolynomial(coeffs=[13.5042,0.0216445,-1.19494e-05,3.10656e-09,-3.11657e-13,-41664.1,-37.5165], Tmin=(1186,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-323.61,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (249.434,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 1, 'H-O': 1, 'C=N': 1, 'C=O': 2, 'C-N': 1, 'C-C': 2, 'C#N': 1, 'C-O': 1}
1D rotors:
pivots: [1, 7], dihedral: [11, 1, 7, 2], rotor symmetry: 1, max scan energy: 56.23 kJ/mol
pivots: [4, 6], dihedral: [9, 4, 6, 7], rotor symmetry: 1, max scan energy: 11.22 kJ/mol
* Invalidated! pivots: [6, 7], dihedral: [4, 6, 7, 1], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.84107000    1.35602700   -0.11606500
O      -0.54176700    0.21778000    1.33729400
O       1.86876400   -2.05846300    1.05115200
N       0.99370200   -0.80906600   -0.76127400
N      -1.95004500   -1.58564700   -2.32473300
C      -0.20866900   -0.09027500   -1.04937000
C      -0.87123600    0.49817400    0.22181000
C      -1.18752000   -0.92621700   -1.76836400
C       1.36408200   -1.42887000    0.21560600
H       0.03256100    0.75455800   -1.70241000
H      -2.25427800    1.68025700    0.69914800
""",
)

entry(
    index = 97,
    label = "C4H8N2O2_63",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  N u0 p1 c0 {5,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {4,S}
6  C u0 p0 c0 {1,S} {15,T}
7  O u0 p2 c0 {2,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 N u0 p1 c0 {6,T}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79655,0.0190043,0.000337442,-1.31693e-06,1.62209e-09,-18051.3,12.0974], Tmin=(10,'K'), Tmax=(263.73,'K')),
            NASAPolynomial(coeffs=[3.00562,0.0577781,-3.53926e-05,1.05363e-08,-1.21687e-12,-18102.7,13.0935], Tmin=(263.73,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-150.054,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (378.308,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C-H': 5, 'N-O': 1, 'C-C': 3, 'C-O': 2, 'C#N': 1, 'H-N': 2}
1D rotors:
pivots: [1, 3], dihedral: [5, 1, 3, 14], rotor symmetry: 1, max scan energy: 75.23 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 1 5 6 10 F
D 16 2 6 10 F
D 3 1 5 7 F
* Invalidated! pivots: [1, 5], dihedral: [3, 1, 5, 6], invalidation reason: 
* Invalidated! pivots: [2, 6], dihedral: [16, 2, 6, 5], invalidation reason: 
* Invalidated! pivots: [5, 6], dihedral: [1, 5, 6, 2], invalidation reason: 
* Invalidated! pivots: [5, 7], dihedral: [1, 5, 7, 11], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
O       0.47281800   -1.05312100    0.29874100
O      -0.69979000    1.58230500   -0.87194500
N       1.17224800   -0.51545900   -0.84709000
N       1.35489100    1.68050100    2.06349600
C      -0.30768600   -0.04003400    0.96525100
C      -1.29550000    0.65750500    0.00210000
C      -1.05275000   -0.81273000    2.05737300
C       0.61522600    0.94476000    1.57399600
H      -1.81782000   -0.15203600   -0.53076500
H      -2.03367000    1.20444200    0.59429800
H      -0.34621700   -1.39258300    2.65131800
H      -1.76547600   -1.49593600    1.59168700
H      -1.58745000   -0.12495500    2.71349800
H       1.14460500   -1.28951300   -1.50646600
H       2.14240800   -0.42443200   -0.54367500
H       0.05238600    1.11723000   -1.27002800
""",
)

entry(
    index = 98,
    label = "C4H6N2O2_40",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  N u0 p1 c0 {5,S} {6,S} {13,S}
5  O u0 p2 c0 {1,S} {4,S}
6  O u0 p2 c0 {2,S} {4,S}
7  C u0 p0 c0 {1,S} {14,T}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 N u0 p1 c0 {7,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.69627,0.0256916,9.31643e-05,-2.15295e-07,1.3758e-10,7912.42,12.7979], Tmin=(10,'K'), Tmax=(520.097,'K')),
            NASAPolynomial(coeffs=[2.44458,0.0524319,-3.33146e-05,1.00947e-08,-1.17101e-12,7811.15,15.7931], Tmin=(520.097,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (65.7474,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (328.422,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'N-O': 2, 'C-C': 3, 'C-O': 2, 'C#N': 1, 'H-N': 1}
1D rotors:
pivots: [5, 7], dihedral: [1, 5, 7, 11], rotor symmetry: 3, max scan energy: 13.27 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.61947400   -0.69285500   -1.09139800
O      -1.96978300    0.09863900    0.52537800
N      -1.67872000   -1.12173600   -0.16927800
N       0.72324000    2.32334200   -1.67117900
C       0.22358900    0.14803500   -0.28983100
C      -0.67921000    0.47093000    0.95517200
C       1.52439600   -0.56295800    0.08411800
C       0.48900000    1.36320000   -1.07856300
H      -0.70162400    1.52683900    1.21468600
H      -0.35383500   -0.13748600    1.80532100
H       2.09712500   -0.80004300   -0.81283200
H       1.28031500   -1.48965000    0.60564500
H       2.13754800    0.06653600    0.73452400
H      -2.47332600   -1.19373300   -0.81020300
""",
)

entry(
    index = 99,
    label = "C4H8N2O3_64",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  N u0 p1 c0 {5,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {4,S}
6  O u0 p2 c0 {2,S} {8,S}
7  C u0 p0 c0 {1,S} {16,T}
8  O u0 p2 c0 {6,S} {17,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 N u0 p1 c0 {7,T}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93597,0.00804412,0.000732599,-4.2358e-06,8.51599e-09,-9179.53,11.2192], Tmin=(10,'K'), Tmax=(144.648,'K')),
            NASAPolynomial(coeffs=[2.26794,0.0684162,-4.11846e-05,1.13313e-08,-1.18935e-12,-9146.18,15.5263], Tmin=(144.648,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-74.3624,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (386.623,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C-H': 5, 'N-O': 1, 'C-C': 3, 'O-O': 1, 'C-O': 2, 'C#N': 1, 'H-N': 2}
1D rotors:
pivots: [1, 4], dihedral: [6, 1, 4, 15], rotor symmetry: 1, max scan energy: 90.34 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 15 4 16 F
A 1 6 7 F
D 4 1 6 7 F
D 1 6 7 10 F
D 3 2 7 10 F
D 7 2 3 17 F
pivots: [1, 6], dihedral: [4, 1, 6, 7], rotor symmetry: 1, max scan energy: 69.87 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 1 6 7 10 F
D 6 1 4 15 F
D 3 2 7 10 F
D 7 2 3 17 F
pivots: [2, 3], dihedral: [7, 2, 3, 17], rotor symmetry: 1, max scan energy: 64.53 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 1 6 7 10 F
D 6 1 4 15 F
D 3 2 7 10 F
D 4 1 6 8 F
pivots: [2, 7], dihedral: [3, 2, 7, 6], rotor symmetry: 1, max scan energy: 77.17 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 1 6 7 10 F
D 6 1 4 15 F
D 4 1 6 8 F
D 7 2 3 17 F
* Invalidated! pivots: [6, 7], dihedral: [1, 6, 7, 2], invalidation reason: Another conformer for C4H8N2O3_64 exists which is 6.72 kJ/mol lower.
pivots: [6, 8], dihedral: [1, 6, 8, 12], rotor symmetry: 3, max scan energy: 11.14 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.95325900   -0.43920000   -0.80660800
O       1.41932200    1.59250100   -0.04618900
O       1.19184100    1.99014400   -1.41801600
N      -1.32732300    0.87432600   -1.27798100
N      -1.30468100    0.93647400    2.24328300
C      -0.07808000   -0.39532900    0.33350700
C       1.33234700    0.19018800    0.04895500
C       0.05750700   -1.87229700    0.72836700
C      -0.74447700    0.36032000    1.41730000
H       1.97137400   -0.07080800    0.89876200
H       1.72230700   -0.27727900   -0.85979000
H       0.56477900   -2.41102700   -0.07418100
H      -0.92990700   -2.30837700    0.87638900
H       0.63337700   -1.97217700    1.64900300
H      -2.15038900    1.13815000   -0.73172400
H      -1.65928000    0.66456300   -2.21681000
H       0.21409200    1.89794900   -1.46189500
""",
)

entry(
    index = 100,
    label = "C4H2N2O2_29",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {7,D}
3  C u0 p0 c0 {1,S} {8,T}
4  C u0 p0 c0 {1,S} {9,T}
5  O u0 p2 c0 {2,S} {10,S}
6  H u0 p0 c0 {1,S}
7  O u0 p2 c0 {2,D}
8  N u0 p1 c0 {3,T}
9  N u0 p1 c0 {4,T}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74684,0.0394464,-2.85234e-05,9.74984e-09,-1.28527e-12,-12418.4,13.7416], Tmin=(10,'K'), Tmax=(2083.84,'K')),
            NASAPolynomial(coeffs=[0.235942,0.0374122,-2.07437e-05,5.24053e-09,-5.01891e-13,-9050.33,37.8281], Tmin=(2083.84,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-103.257,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (224.491,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 1, 'H-O': 1, 'C=O': 1, 'C-C': 3, 'C#N': 2, 'C-O': 1}
1D rotors:
pivots: [1, 6], dihedral: [10, 1, 6, 2], rotor symmetry: 1, max scan energy: 56.96 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 8 5 6 2 F
pivots: [5, 6], dihedral: [7, 5, 6, 1], rotor symmetry: 1, max scan energy: 3.98 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.78997600    0.91429400    0.18035000
O      -1.31365700   -1.05196100   -0.82451600
N       2.12198300   -1.69601100   -0.39062900
N       1.29780500    2.55225300   -0.56470300
C       0.46279300    0.21437600    0.26752000
C      -0.98453200   -0.07881200   -0.21893800
C       1.38372000   -0.85792000   -0.11617100
C       0.93281500    1.52400900   -0.19884200
H       0.41512700    0.25332400    1.36362100
H      -2.68520500    0.71873400   -0.13714000
""",
)

entry(
    index = 101,
    label = "C4H7N2O2_65",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  O u0 p2 c0 {1,S} {7,S}
5  C u0 p0 c0 {1,S} {13,T}
6  O u0 p2 c0 {2,S} {14,S}
7  N u1 p1 c0 {4,S} {15,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 N u0 p1 c0 {5,T}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.42743,0.0481901,2.38662e-05,-9.529e-08,5.60392e-11,-253.944,13.1804], Tmin=(10,'K'), Tmax=(669.235,'K')),
            NASAPolynomial(coeffs=[6.13586,0.0532143,-3.49394e-05,1.06521e-08,-1.22938e-12,-1091.48,-2.34741], Tmin=(669.235,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-2.18711,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (340.893,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C-H': 5, 'N-O': 1, 'C-C': 3, 'C-O': 2, 'C#N': 1, 'H-N': 1}
1D rotors:
* Invalidated! pivots: [1, 3], dihedral: [5, 1, 3, 15], invalidation reason: 
pivots: [1, 5], dihedral: [3, 1, 5, 6], rotor symmetry: 1, max scan energy: 15.94 kJ/mol
pivots: [2, 6], dihedral: [14, 2, 6, 5], rotor symmetry: 1, max scan energy: 34.62 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 3 1 5 7 F
pivots: [5, 6], dihedral: [1, 5, 6, 2], rotor symmetry: 1, max scan energy: 53.70 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 14 2 6 10 F
D 3 1 5 7 F
pivots: [5, 7], dihedral: [1, 5, 7, 11], rotor symmetry: 3, max scan energy: 12.26 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.34750000    0.35071800   -0.28961700
O      -0.99758800   -1.69386300   -0.47948000
N       1.69782500   -0.95590300   -0.39698500
N      -0.56602700    3.04788100   -0.32400800
C      -0.05769100    0.51344300    0.11026400
C      -0.98671600   -0.32901700   -0.80858600
C      -0.20864400    0.17244500    1.59359600
C      -0.31418300    1.93995900   -0.13473000
H      -0.67829400   -0.14650600   -1.84645200
H      -2.00663600    0.04221800   -0.68829300
H       0.49465100    0.75824000    2.18628800
H      -0.01957000   -0.89013200    1.73400700
H      -1.22509900    0.39254300    1.92467800
H      -0.08044200   -1.99607400   -0.55780200
H       2.68407200   -0.87342500   -0.66615200
""",
)

entry(
    index = 102,
    label = "C4H5N2O2_41",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {6,S} {11,S}
4  N u0 p1 c0 {5,S} {6,S} {12,S}
5  O u0 p2 c0 {1,S} {4,S}
6  O u0 p2 c0 {3,S} {4,S}
7  C u0 p0 c0 {1,S} {13,T}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 N u0 p1 c0 {7,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75421,0.0193229,0.000156034,-4.08286e-07,3.14185e-10,31446.9,13.0188], Tmin=(10,'K'), Tmax=(432.763,'K')),
            NASAPolynomial(coeffs=[3.01338,0.0500233,-3.30531e-05,1.03626e-08,-1.23623e-12,31287.6,13.3918], Tmin=(432.763,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (261.452,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 4, 'N-O': 2, 'C-C': 3, 'C-O': 2, 'C#N': 1, 'H-N': 1}
1D rotors:
* Invalidated! pivots: [5, 6], dihedral: [1, 5, 6, 9], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
O       0.94416400   -0.33845500   -0.92148600
O       1.50622800   -0.75089100    1.22799100
N       1.38960000   -1.41412000   -0.07115700
N      -0.06555400    2.85513200   -0.70362600
C      -0.08932000    0.29366700   -0.13737900
C      -1.46705100   -0.31760000   -0.41743300
C       0.40880100    0.04599400    1.28578600
C      -0.05636600    1.72467100   -0.47882600
H      -1.42418200   -1.38633900   -0.20633900
H      -1.74217100   -0.15979600   -1.46176300
H      -2.22103600    0.14186300    0.22512500
H       0.43706000    0.79257900    2.06680500
H       2.37328600   -1.48973800   -0.34387300
""",
)

entry(
    index = 103,
    label = "C4H3NO_66",
    molecule = 
"""
1 O u0 p2 c0 {5,D}
2 N u0 p1 c0 {6,T}
3 C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
4 C u0 p0 c0 {3,S} {5,D} {6,S}
5 C u0 p0 c0 {1,D} {4,D}
6 C u0 p0 c0 {2,T} {4,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88869,0.0128288,0.000270551,-1.67937e-06,3.18616e-09,6915.75,9.99064], Tmin=(10,'K'), Tmax=(181.94,'K')),
            NASAPolynomial(coeffs=[4.22303,0.0265077,-1.56022e-05,4.44365e-09,-4.91612e-13,6868.77,7.99086], Tmin=(181.94,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (57.8403,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (203.705,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 3, 'C-C': 2, 'C=O': 1, 'C#N': 1, 'C=C': 1}
1D rotors:
pivots: [3, 4], dihedral: [7, 3, 4, 5], rotor symmetry: 3, max scan energy: 4.72 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O       2.62571900   -0.34142700   -0.51338300
N      -0.41087700    2.72236300    0.22486900
C      -0.78397100   -0.84538900    0.10198100
C       0.26430800    0.25156700   -0.03619300
C       1.53025700   -0.04899500   -0.29107500
C      -0.08389700    1.61886900    0.10348200
H      -1.23870300   -0.81060100    1.09424800
H      -0.33573500   -1.83014200   -0.03583000
H      -1.56709900   -0.71624600   -0.64809700
""",
)

entry(
    index = 104,
    label = "C3H5O3_0b",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,D}
3  C u1 p0 c0 {2,S} {4,S} {10,S}
4  O u0 p2 c0 {3,S} {5,S}
5  O u0 p2 c0 {4,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u0 p2 c0 {2,D}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.62487,0.0328672,5.32718e-05,-2.13898e-07,1.87734e-10,-20031.7,12.4056], Tmin=(10,'K'), Tmax=(424.542,'K')),
            NASAPolynomial(coeffs=[5.02953,0.0373809,-2.53849e-05,8.09157e-09,-9.76016e-13,-20310.9,4.94863], Tmin=(424.542,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-166.563,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (241.12,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'H-O': 1, 'C-H': 4, 'O-O': 1, 'C-C': 2, 'C-O': 1}
1D rotors:
pivots: [1, 2], dihedral: [6, 1, 2, 11], rotor symmetry: 1, max scan energy: 23.30 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
B 1 2 F
B 2 11 F
pivots: [1, 6], dihedral: [2, 1, 6, 5], rotor symmetry: 1, max scan energy: 28.46 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 1 6 5 10 F
D 6 1 2 11 F
B 1 2 F
pivots: [4, 5], dihedral: [7, 4, 5, 3], rotor symmetry: 3, max scan energy: 1.18 kJ/mol
pivots: [5, 6], dihedral: [3, 5, 6, 1], rotor symmetry: 1, max scan energy: 72.83 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 5 6 1 10 F
D 2 1 6 5 F
D 7 4 5 6 F
D 6 1 2 11 F
B 1 2 F


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.78579300    1.86688900   -3.52642100
O      -0.17447300    3.01118000   -4.27992400
O       0.51645800    0.30957700   -0.68201300
C      -1.78498700    0.94572500   -1.02901000
C      -0.32083600    0.84632400   -1.40553200
C       0.10853200    1.38211900   -2.67751100
H      -1.88462900    0.74956400    0.03784300
H      -2.19838800    1.92602300   -1.27581200
H      -2.36531900    0.19868400   -1.58003800
H       1.15391800    1.39466800   -2.96317300
H      -0.64035500    2.89224100   -5.12132700
""",
)

entry(
    index = 105,
    label = "C4H8N2O2_67",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  N u0 p1 c0 {5,S} {7,S} {14,S}
5  O u0 p2 c0 {1,S} {4,S}
6  C u0 p0 c0 {1,S} {15,T}
7  O u0 p2 c0 {4,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 N u0 p1 c0 {6,T}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.56731,0.0365996,0.000144937,-4.3817e-07,3.59746e-10,-6849.87,12.6814], Tmin=(10,'K'), Tmax=(420.883,'K')),
            NASAPolynomial(coeffs=[3.95793,0.0607507,-4.044e-05,1.27551e-08,-1.52879e-12,-7129.54,8.2031], Tmin=(420.883,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-56.963,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (374.151,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C-H': 6, 'N-O': 2, 'C-C': 3, 'C-O': 1, 'C#N': 1, 'H-N': 1}
1D rotors:
* Invalidated! pivots: [1, 3], dihedral: [5, 1, 3, 2], invalidation reason: 
pivots: [1, 5], dihedral: [3, 1, 5, 6], rotor symmetry: 1, max scan energy: 26.10 kJ/mol
pivots: [2, 3], dihedral: [16, 2, 3, 1], rotor symmetry: 1, max scan energy: 46.44 kJ/mol
* Invalidated! pivots: [5, 6], dihedral: [1, 5, 6, 9], invalidation reason: 
* Invalidated! pivots: [5, 7], dihedral: [1, 5, 7, 12], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
O       3.03767200   -1.21063000   -0.64113900
O       1.84110100    0.60680600   -1.40925700
N       1.72007500   -0.62434800   -0.72591300
N       3.41355800    1.39580800    1.48489300
C       3.55383700   -1.11661100    0.69898300
C       2.75773800   -2.00473200    1.66343800
C       5.01765600   -1.55098400    0.57709500
C       3.48535200    0.29582900    1.14671200
H       2.83618600   -3.04149700    1.32957200
H       3.15259500   -1.92725800    2.67876700
H       1.70927900   -1.70823300    1.66792000
H       5.54743500   -0.90275400   -0.12112100
H       5.04951100   -2.57512300    0.20131900
H       5.51050400   -1.51177000    1.54987900
H       1.30957500   -1.21644200   -1.44430400
H       1.85082300    1.25846900   -0.69656100
""",
)

entry(
    index = 106,
    label = "C4H7N2O3_42",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  N u0 p1 c0 {5,S} {7,S} {14,S}
5  O u0 p2 c0 {1,S} {4,S}
6  C u0 p0 c0 {1,S} {15,T}
7  O u0 p2 c0 {4,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 N u0 p1 c0 {6,T}
16 O u1 p2 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.66241,0.0400204,0.000452917,-3.04814e-06,5.97305e-09,18688.4,14.1751], Tmin=(10,'K'), Tmax=(180.006,'K')),
            NASAPolynomial(coeffs=[4.63263,0.0586969,-3.80073e-05,1.18272e-08,-1.41051e-12,18588.3,9.34734], Tmin=(180.006,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (156.112,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (382.466,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 6, 'N-O': 2, 'C-C': 3, 'O-O': 1, 'C-O': 1, 'C#N': 1, 'H-N': 1}
1D rotors:
* Invalidated! pivots: [1, 4], dihedral: [6, 1, 4, 2], invalidation reason: Bond ([[2, 4]]) broke during the scan.
* Invalidated! pivots: [1, 6], dihedral: [4, 1, 6, 7], invalidation reason: 
* Invalidated! pivots: [2, 4], dihedral: [3, 2, 4, 1], invalidation reason: Bond ([[2, 4]]) broke during the scan.
* Invalidated! pivots: [6, 7], dihedral: [1, 6, 7, 10], invalidation reason: 
* Invalidated! pivots: [6, 8], dihedral: [1, 6, 8, 13], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
O       0.86714100   -0.43829600    0.73378500
O       2.43822500    0.67119700   -0.61780600
O       3.68281200    0.39702800   -0.72272200
N       1.60834000   -0.64109900   -0.40400200
N      -1.64770500    0.17500600    2.77186500
C      -0.54241500   -0.15405500    0.41459500
C      -1.17884400   -1.35867400   -0.28576600
C      -0.66141400    1.14061300   -0.39549400
C      -1.13806900    0.02818900    1.74964400
H      -1.07171200   -2.25475300    0.32707100
H      -2.24104500   -1.17485900   -0.45607800
H      -0.68613700   -1.51619600   -1.24540200
H      -0.19706900    1.00212700   -1.37268500
H      -0.16614900    1.96166000    0.12340100
H      -1.71327500    1.39434300   -0.53847700
H       2.38997600   -1.22370300   -0.08552800
""",
)

entry(
    index = 107,
    label = "C4H2NO2_68",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,D}
2 C u1 p0 c0 {1,S} {5,S} {6,S}
3 C u0 p0 c0 {1,S} {8,T}
4 C u0 p0 c0 {1,D} {7,D}
5 O u0 p2 c0 {2,S} {9,S}
6 H u0 p0 c0 {2,S}
7 O u0 p2 c0 {4,D}
8 N u0 p1 c0 {3,T}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82709,0.0129011,0.000138643,-4.08232e-07,3.48869e-10,3117.11,11.5281], Tmin=(10,'K'), Tmax=(406.33,'K')),
            NASAPolynomial(coeffs=[4.5964,0.0306784,-2.05676e-05,6.52796e-09,-7.87711e-13,2845.32,5.93427], Tmin=(406.33,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (25.9204,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C-C': 2, 'C-O': 1, 'C=O': 1, 'C#N': 1, 'C=C': 1, 'C-H': 1}
1D rotors:
* Invalidated! pivots: [1, 5], dihedral: [9, 1, 5, 4], invalidation reason: Another conformer for C4H2NO2_68 exists which is 46.89 kJ/mol lower.
* Invalidated! pivots: [4, 5], dihedral: [6, 4, 5, 1], invalidation reason: 
* Invalidated! pivots: [4, 7], dihedral: [5, 4, 7, 2], invalidation reason: 


External symmetry: 1, optical isomers: 1

Geometry:
O      -1.91501000    0.44404900    0.47750500
O      -0.04752300    2.19199100    1.23953900
N       2.27576400   -1.23938300   -1.02147900
C       0.41640600    0.19728400    0.03843100
C      -0.89378800   -0.20743900   -0.02587000
C       1.44603500   -0.59240300   -0.54513500
C       0.73346600    1.44989300    0.71496600
H      -1.17683300   -1.13302100   -0.51953800
H      -1.59649500    1.26768900    0.90828300
""",
)

entry(
    index = 108,
    label = "C4HN2O2_30",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,D}
3 C u0 p0 c0 {1,S} {8,T}
4 C u0 p0 c0 {1,S} {9,T}
5 H u0 p0 c0 {1,S}
6 O u1 p2 c0 {2,S}
7 O u0 p2 c0 {2,D}
8 N u0 p1 c0 {3,T}
9 N u0 p1 c0 {4,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.50826,0.048802,-7.35795e-05,7.10519e-08,-3.00415e-11,18459.7,13.228], Tmin=(10,'K'), Tmax=(551.936,'K')),
            NASAPolynomial(coeffs=[6.22378,0.029122,-2.00949e-05,6.44928e-09,-7.79662e-13,18159.9,1.74109], Tmin=(551.936,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (153.478,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (203.705,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 1, 'C=O': 1, 'C-C': 3, 'C#N': 2, 'C-O': 1}
1D rotors:
pivots: [5, 6], dihedral: [7, 5, 6, 1], rotor symmetry: 2, max scan energy: 4.36 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O       1.89729200   -1.09432700    0.15053900
O       1.72816800    0.76497900    1.11816400
N      -1.66273600    1.75161000    1.09557900
N      -1.31103000   -2.11426800   -0.91643100
C      -0.15302900    0.15547000   -0.32439000
C       1.20897000   -0.07717100    0.36068800
C      -1.00385400    1.04318700    0.47280300
C      -0.80755100   -1.11453600   -0.65019200
H       0.08115700    0.66816600   -1.26854800
""",
)

entry(
    index = 109,
    label = "C4HNO2_69",
    molecule = 
"""
1 O u0 p2 c0 {5,D}
2 O u0 p2 c0 {7,D}
3 N u0 p1 c0 {6,T}
4 C u0 p0 c0 {5,S} {6,S} {7,D}
5 C u0 p0 c0 {1,D} {4,S} {8,S}
6 C u0 p0 c0 {3,T} {4,S}
7 C u0 p0 c0 {2,D} {4,D}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77528,0.0189552,0.000141482,-5.64866e-07,6.13096e-10,-3775.81,11.1313], Tmin=(10,'K'), Tmax=(336.163,'K')),
            NASAPolynomial(coeffs=[5.61603,0.0258444,-1.77335e-05,5.67111e-09,-6.86969e-13,-4062.26,1.83773], Tmin=(336.163,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-31.3616,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 2, 'C=O': 2, 'C#N': 1, 'C=C': 1, 'C-H': 1}
1D rotors:
pivots: [4, 5], dihedral: [6, 4, 5, 1], rotor symmetry: 1, max scan energy: 49.91 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O      -0.36716200   -2.16285500   -0.00289800
O       2.39619800   -0.24956300   -0.96802100
N      -0.72990300    2.54333900    0.46438500
C       0.13174000    0.17207000   -0.04045600
C      -0.71480600   -1.03129800    0.21279900
C      -0.31952000    1.48853700    0.22906400
C       1.35798700   -0.03043300   -0.54097600
H      -1.70668500   -0.76886200    0.62443400
""",
)

entry(
    index = 110,
    label = "C4H8N2O3_43",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  N u0 p1 c0 {5,S} {7,S} {15,S}
5  O u0 p2 c0 {1,S} {4,S}
6  C u0 p0 c0 {1,S} {16,T}
7  O u0 p2 c0 {4,S} {8,S}
8  O u0 p2 c0 {7,S} {17,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 N u0 p1 c0 {6,T}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.54034,0.0420017,0.000261769,-1.0973e-06,1.27298e-09,-1334.83,13.3754], Tmin=(10,'K'), Tmax=(307.068,'K')),
            NASAPolynomial(coeffs=[5.40374,0.0606971,-3.94557e-05,1.23855e-08,-1.49035e-12,-1651.84,3.28705], Tmin=(307.068,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-11.0361,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (403.252,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C-H': 6, 'N-O': 2, 'C-C': 3, 'O-O': 1, 'C-O': 1, 'C#N': 1, 'H-N': 1}
1D rotors:
* Invalidated! pivots: [1, 4], dihedral: [6, 1, 4, 2], invalidation reason: 
* Invalidated! pivots: [1, 6], dihedral: [4, 1, 6, 7], invalidation reason: 
pivots: [2, 3], dihedral: [4, 2, 3, 17], rotor symmetry: 1, max scan energy: 33.42 kJ/mol
* Invalidated! pivots: [2, 4], dihedral: [3, 2, 4, 1], invalidation reason: 
* Invalidated! pivots: [6, 7], dihedral: [1, 6, 7, 10], invalidation reason: 
* Invalidated! pivots: [6, 8], dihedral: [1, 6, 8, 13], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
O       2.15591100    0.97009200   -1.69772700
O       1.82758500   -1.04667600   -0.68819700
O       3.22914000   -1.13336400   -0.20538000
N       1.41961600    0.24441700   -0.70351400
N      -0.61179700    2.90700100   -2.06494100
C       1.32513800    1.29985200   -2.83778200
C       2.26960300    2.06842800   -3.76784800
C       0.74280900    0.04961900   -3.50541400
C       0.23382300    2.19512100   -2.39044300
H       3.08109900    1.40759100   -4.07775100
H       2.69098500    2.93132700   -3.25152200
H       1.73152000    2.41160100   -4.65255700
H       0.10714700   -0.50057600   -2.81309800
H       0.14742000    0.33456200   -4.37531700
H       1.55987000   -0.59734600   -3.83035600
H       1.73862400    0.67645200    0.16569000
H       3.70832600   -0.96284300   -1.03046100
""",
)

entry(
    index = 111,
    label = "C4NO2_70",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {5,D}
2 O u0 p2 c0 {7,D}
3 N u0 p1 c0 {6,T}
4 C u0 p0 c0 {5,S} {6,S} {7,D}
5 C u1 p0 c0 {1,D} {4,S}
6 C u0 p0 c0 {3,T} {4,S}
7 C u0 p0 c0 {2,D} {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75782,0.0193244,0.00011372,-4.27408e-07,4.18219e-10,16382.3,11.7705], Tmin=(10,'K'), Tmax=(379.805,'K')),
            NASAPolynomial(coeffs=[6.17571,0.023179,-1.72964e-05,5.8125e-09,-7.25572e-13,15987.2,-0.337588], Tmin=(379.805,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (136.228,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (153.818,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 2, 'C=O': 2, 'C#N': 1, 'C=C': 1}
1D rotors:
pivots: [4, 5], dihedral: [6, 4, 5, 1], rotor symmetry: 1, max scan energy: 48.68 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O      -0.63921200   -2.25373500   -0.36734200
O       2.32183200   -0.45058000    0.05842000
N      -1.23792600    2.40010900    0.28792100
C      -0.09597700    0.11087700    0.01121300
C      -0.86042100   -1.11268900   -0.21068800
C      -0.72547800    1.37286300    0.16375500
C       1.23718100   -0.06684500    0.05672100
""",
)

entry(
    index = 112,
    label = "C3NO3_8",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {5,S}
2 O u1 p2 c0 {1,S}
3 O u0 p2 c0 {6,D}
4 N u0 p1 c0 {7,T}
5 C u0 p0 c0 {1,S} {6,D} {7,S}
6 C u0 p0 c0 {3,D} {5,D}
7 C u0 p0 c0 {4,T} {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.24265,0.0507231,-9.01562e-05,7.78619e-08,-2.52877e-11,25535.2,12.5296], Tmin=(10,'K'), Tmax=(913.342,'K')),
            NASAPolynomial(coeffs=[8.37234,0.0148296,-9.15476e-06,2.6404e-09,-2.92037e-13,25158.2,-8.68715], Tmin=(913.342,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (212.159,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (153.818,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'C=O': 1, 'O-O': 1, 'C#N': 1, 'C-C': 1, 'C-O': 1}
1D rotors:
pivots: [1, 5], dihedral: [2, 1, 5, 6], rotor symmetry: 1, max scan energy: 7.82 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O      -0.18969700    1.44615900   -0.04876000
O      -1.49430100    1.64255400   -0.17685900
O      -1.63069300   -1.55968700   -0.79045000
N       2.59886900   -0.60855300   -0.07935300
C       0.14305500    0.10280200   -0.25691900
C      -0.83938900   -0.76582900   -0.54271300
C       1.49060800   -0.28581900   -0.15916600
""",
)

entry(
    index = 113,
    label = "C4H3NO2_71",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {4,S}
2  C u0 p0 c0 {1,S} {5,S} {6,D}
3  C u0 p0 c0 {1,D} {7,S} {8,S}
4  C u0 p0 c0 {1,S} {9,T}
5  O u0 p2 c0 {2,S} {10,S}
6  O u0 p2 c0 {2,D}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  N u0 p1 c0 {4,T}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78307,0.0184196,6.83003e-05,-1.47416e-07,8.53568e-11,-23649,11.1378], Tmin=(10,'K'), Tmax=(599.325,'K')),
            NASAPolynomial(coeffs=[3.80148,0.0368924,-2.44751e-05,7.55481e-09,-8.8263e-13,-23985.2,8.27218], Tmin=(599.325,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-196.668,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (228.648,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C-H': 2, 'C-C': 2, 'C-O': 1, 'C=O': 1, 'C#N': 1, 'C=C': 1}
1D rotors:
pivots: [1, 5], dihedral: [10, 1, 5, 2], rotor symmetry: 1, max scan energy: 52.86 kJ/mol
* Invalidated! pivots: [4, 5], dihedral: [6, 4, 5, 1], invalidation reason: 


External symmetry: 1, optical isomers: 1

Geometry:
O       1.56466700    0.55444600   -1.36859500
O       1.67928400   -0.80764100    0.42034600
N      -1.61366300    1.79887100   -1.78143800
C      -0.41405300    0.21615100   -0.12655700
C       1.04862100   -0.08335400   -0.30449600
C      -1.06790300   -0.34953300    0.89518400
C      -1.06948900    1.09340700   -1.04757500
H      -0.52915500   -1.00687500    1.56639100
H      -2.12032500   -0.16681900    1.06736900
H       2.50237200    0.31571900   -1.41975000
""",
)

entry(
    index = 114,
    label = "C4H2N2O3_46",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {8,D}
3  C u0 p0 c0 {1,D} {4,D}
4  N u0 p1 c0 {3,D} {6,S}
5  O u0 p2 c0 {2,S} {10,S}
6  N u0 p1 c0 {4,S} {7,D}
7  C u0 p0 c0 {6,D} {11,D}
8  O u0 p2 c0 {2,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {5,S}
11 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49132,0.0464555,-1.65103e-05,-2.90306e-08,2.24974e-11,-16477,13.6292], Tmin=(10,'K'), Tmax=(713.107,'K')),
            NASAPolynomial(coeffs=[8.5986,0.0334056,-2.18707e-05,6.65426e-09,-7.66458e-13,-17602,-12.0643], Tmin=(713.107,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-137.052,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (253.591,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C-C': 1, 'C-O': 1, 'C=O': 2, 'N-N': 1, 'C=N': 2, 'C=C': 1, 'C-H': 1}
1D rotors:
* Invalidated! pivots: [1, 7], dihedral: [11, 1, 7, 2], invalidation reason: 
pivots: [4, 5], dihedral: [8, 4, 5, 9], rotor symmetry: 1, max scan energy: 26.73 kJ/mol
* Invalidated! pivots: [6, 7], dihedral: [8, 6, 7, 1], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
O      -3.13304100   -0.33143700   -0.04926900
O      -1.81767000    1.19142100    0.96987900
O       4.71199000    0.90987100    0.54407800
N       1.52672100   -0.34836400    0.75165500
N       2.46808600    0.34483900    0.00233800
C      -0.85360500   -0.78599600    0.01830000
C      -1.93970700    0.14788900    0.37958800
C       0.39421000   -0.51558800    0.32666800
C       3.60978900    0.58919800    0.37047300
H      -1.09443400   -1.69505900   -0.51910100
H      -3.79913500    0.31943800    0.21661800
""",
)

entry(
    index = 115,
    label = "C4H2NO2_73",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 C u0 p0 c0 {1,S} {5,S} {6,D}
3 C u1 p0 c0 {1,D} {9,S}
4 C u0 p0 c0 {1,S} {7,T}
5 O u0 p2 c0 {2,S} {8,S}
6 O u0 p2 c0 {2,D}
7 N u0 p1 c0 {4,T}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79267,0.0151369,0.000136092,-3.96768e-07,3.26284e-10,8028.5,12.1354], Tmin=(10,'K'), Tmax=(431.015,'K')),
            NASAPolynomial(coeffs=[5.33598,0.0305896,-2.13085e-05,6.96706e-09,-8.57629e-13,7618.89,2.78027], Tmin=(431.015,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (66.7431,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C-C': 2, 'C-O': 1, 'C=O': 1, 'C#N': 1, 'C=C': 1, 'C-H': 1}
1D rotors:
* Invalidated! pivots: [1, 5], dihedral: [8, 1, 5, 2], invalidation reason: 
* Invalidated! pivots: [4, 5], dihedral: [6, 4, 5, 1], invalidation reason: 


External symmetry: 1, optical isomers: 1

Geometry:
O      -1.72916500   -0.21287600    0.36534700
O      -0.19677300   -1.86611200    0.38988700
N       2.96383200   -0.38426000   -0.44809200
C       0.50701600    0.36574700   -0.14219400
C      -0.48479700   -0.71348300    0.23234200
C       0.14705100    1.62493300   -0.30614900
C       1.86653800   -0.05663100   -0.31013300
H      -2.30733900   -0.95293200    0.60383100
H      -0.76636100    2.19561300   -0.24543300
""",
)

entry(
    index = 116,
    label = "C4HN2O2_31",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 C u0 p0 c0 {1,S} {5,S} {6,D}
3 C u0 p0 c0 {1,S} {7,T}
4 C u0 p0 c0 {1,S} {8,T}
5 O u0 p2 c0 {2,S} {9,S}
6 O u0 p2 c0 {2,D}
7 N u0 p1 c0 {3,T}
8 N u0 p1 c0 {4,T}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72082,0.026714,0.000120222,-5.45038e-07,6.63778e-10,2696.07,12.0076], Tmin=(10,'K'), Tmax=(287.137,'K')),
            NASAPolynomial(coeffs=[4.14971,0.0379755,-2.86509e-05,9.67097e-09,-1.20843e-12,2600.39,9.23631], Tmin=(287.137,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (22.4565,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (199.547,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C=O': 1, 'C-C': 3, 'C#N': 2, 'C-O': 1}
1D rotors:
pivots: [1, 6], dihedral: [9, 1, 6, 2], rotor symmetry: 2, max scan energy: 49.76 kJ/mol
pivots: [5, 6], dihedral: [7, 5, 6, 1], rotor symmetry: 2, max scan energy: 24.88 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O      -0.63580900   -1.72283000    0.10541300
O      -1.76255400    0.04609600    0.95511300
N       0.27046700    2.93452200    0.25782200
N       2.31942000   -0.64638500   -1.33739500
C       0.32402700    0.40122900   -0.11926500
C      -0.81565700   -0.42198900    0.38105400
C       0.28838100    1.78556300    0.09023000
C       1.41396200   -0.17193400   -0.78476700
H      -1.40223800   -2.20427100    0.45179400
""",
)

entry(
    index = 117,
    label = "C4HN2O3_74",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,D} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,D}
3  C u0 p0 c0 {1,D} {4,D}
4  N u0 p1 c0 {3,D} {5,S}
5  N u0 p1 c0 {4,S} {6,D}
6  C u0 p0 c0 {5,D} {10,D}
7  H u0 p0 c0 {1,S}
8  O u1 p2 c0 {2,S}
9  O u0 p2 c0 {2,D}
10 O u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.51653,0.048768,-3.7546e-05,6.16619e-09,3.32027e-12,13091.8,14.0668], Tmin=(10,'K'), Tmax=(879.978,'K')),
            NASAPolynomial(coeffs=[11.4596,0.0243054,-1.5694e-05,4.64688e-09,-5.197e-13,11243.1,-25.7997], Tmin=(879.978,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (108.831,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (224.491,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 1, 'C-O': 1, 'C=O': 2, 'N-N': 1, 'C=N': 2, 'C=C': 1, 'C-H': 1}
1D rotors:
pivots: [4, 5], dihedral: [8, 4, 5, 9], rotor symmetry: 1, max scan energy: 27.81 kJ/mol
pivots: [6, 7], dihedral: [8, 6, 7, 1], rotor symmetry: 2, max scan energy: 17.04 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -3.33794900    0.99984200   -0.52247200
O      -1.47820300    1.91149300   -0.79256100
O       4.33676200   -1.02909600   -0.34376000
N       1.05023700   -0.46285000    0.42337200
N       1.96866700   -0.91205600   -0.50813700
C      -1.45380600   -0.33939800    0.09109500
C      -2.09049100    0.87659700   -0.41607900
C      -0.14487300   -0.43843500    0.18460700
C       3.18187400   -0.93310900   -0.32837700
H      -2.09254600   -1.16776900    0.37637200
""",
)

entry(
    index = 118,
    label = "C4H2N2O3_48",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,D} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,D}
3  C u0 p0 c0 {4,S} {8,D} {9,S}
4  N u0 p1 c0 {1,D} {3,S}
5  C u0 p0 c0 {1,S} {10,T}
6  O u0 p2 c0 {2,S} {11,S}
7  O u0 p2 c0 {2,D}
8  O u0 p2 c0 {3,D}
9  H u0 p0 c0 {3,S}
10 N u0 p1 c0 {5,T}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79687,0.0233339,0.000422085,-2.69647e-06,5.15139e-09,-29079.7,12.7966], Tmin=(10,'K'), Tmax=(182.594,'K')),
            NASAPolynomial(coeffs=[4.50779,0.043021,-2.9307e-05,9.19007e-09,-1.08801e-12,-29164.4,8.9662], Tmin=(182.594,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-241.225,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (253.591,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C-C': 2, 'C-N': 1, 'C-O': 1, 'C=O': 2, 'C#N': 1, 'C=N': 1, 'C-H': 1}
1D rotors:
pivots: [1, 7], dihedral: [11, 1, 7, 2], rotor symmetry: 1, max scan energy: 56.32 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 9 6 7 2 F
D 6 4 8 3 F
D 4 6 7 1 F
* Invalidated! pivots: [4, 8], dihedral: [6, 4, 8, 3], invalidation reason: 
* Invalidated! pivots: [6, 7], dihedral: [4, 6, 7, 1], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
O       0.08945600   -1.36383200    0.92939600
O      -1.33093200   -0.00257600    2.04194800
O       1.98855800    0.02333800   -1.18062400
N      -0.29236000    0.23805800   -1.34052300
N      -3.17712700    1.76971000   -0.42452200
C      -1.02691000    0.31425600   -0.31479500
C      -0.78604200   -0.35584600    1.03587800
C       0.92792800   -0.44951500   -1.47454800
C      -2.21970500    1.13061700   -0.36487500
H       0.79301300   -1.41437400   -1.99456700
H       0.24293900   -1.72596300    1.81563200
""",
)

entry(
    index = 119,
    label = "C4HN2O3_49",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,D} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,D}
3  C u0 p0 c0 {1,D} {4,D}
4  N u0 p1 c0 {3,D} {5,S}
5  O u0 p2 c0 {4,S} {6,S}
6  C u0 p0 c0 {5,S} {10,T}
7  H u0 p0 c0 {1,S}
8  O u1 p2 c0 {2,S}
9  O u0 p2 c0 {2,D}
10 N u0 p1 c0 {6,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.45088,0.0574218,-7.5382e-05,5.8025e-08,-1.936e-11,33723.5,15.1468], Tmin=(10,'K'), Tmax=(682.966,'K')),
            NASAPolynomial(coeffs=[7.46164,0.0339315,-2.37897e-05,7.66372e-09,-9.25071e-13,33175.7,-2.67348], Tmin=(682.966,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (280.385,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'N-O': 1, 'C-C': 1, 'C-O': 2, 'C=O': 1, 'C#N': 1, 'C=N': 1, 'C=C': 1, 'C-H': 1}
1D rotors:
* Invalidated! pivots: [1, 4], dihedral: [9, 1, 4, 8], invalidation reason: 
* Invalidated! pivots: [6, 7], dihedral: [8, 6, 7, 2], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.85422800    0.76113500   -0.84788100
O       3.38591700   -0.11062800    0.74040400
O       1.64612900    0.35778300    1.80731700
N      -1.18626800   -0.49208800   -0.40093600
N      -4.29751900    0.59522000   -0.77574900
C       1.34225600   -0.45878900   -0.45243200
C       2.13326500   -0.06017400    0.72751200
C       0.03201200   -0.39850500   -0.45570800
C      -3.14202600    0.63264600   -0.79370700
H       1.87985800   -0.80179000   -1.33024800
""",
)

entry(
    index = 120,
    label = "C4H2N2O2_33",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {4,S}
2  C u0 p0 c0 {1,S} {5,S} {7,D}
3  C u0 p0 c0 {1,D} {6,D}
4  C u0 p0 c0 {1,S} {8,T}
5  O u0 p2 c0 {2,S} {9,S}
6  N u0 p1 c0 {3,D} {10,S}
7  O u0 p2 c0 {2,D}
8  N u0 p1 c0 {4,T}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77631,0.0188794,0.000185918,-6.65988e-07,6.93605e-10,-7371.38,12.8292], Tmin=(10,'K'), Tmax=(331.331,'K')),
            NASAPolynomial(coeffs=[4.35151,0.0389382,-2.71392e-05,8.67537e-09,-1.04502e-12,-7557.72,8.4528], Tmin=(331.331,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-61.2531,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (224.491,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'H-O': 1, 'C=N': 1, 'C=O': 1, 'C-C': 2, 'C#N': 1, 'C-O': 1, 'H-N': 1}
1D rotors:
pivots: [1, 6], dihedral: [9, 1, 6, 2], rotor symmetry: 1, max scan energy: 52.34 kJ/mol
pivots: [5, 6], dihedral: [7, 5, 6, 1], rotor symmetry: 2, max scan energy: 38.18 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       0.05807100   -1.95071500    0.44458400
O      -1.93815900   -0.95811000    0.08551300
N       2.58851500    0.24590600   -0.12197500
N      -1.12917300    2.54525200   -0.66489600
C       0.05842800    0.32473100   -0.11847800
C      -0.74047500   -0.89979700    0.13845300
C       1.39212700    0.29718900   -0.05301800
C      -0.60419800    1.54582100   -0.42134700
H      -0.52489900   -2.71055400    0.58684900
H       3.19610500    0.40557900    0.67782600
""",
)

entry(
    index = 121,
    label = "C4N2O_50",
    molecule = 
"""
1 O u0 p2 c0 {5,D}
2 N u0 p1 c0 {6,T}
3 N u0 p1 c0 {7,T}
4 C u0 p0 c0 {5,D} {6,S} {7,S}
5 C u0 p0 c0 {1,D} {4,D}
6 C u0 p0 c0 {2,T} {4,S}
7 C u0 p0 c0 {3,T} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78854,0.016559,0.000117921,-4.31442e-07,4.19695e-10,31065.9,10.4842], Tmin=(10,'K'), Tmax=(381.545,'K')),
            NASAPolynomial(coeffs=[6.28769,0.020252,-1.41196e-05,4.61366e-09,-5.69559e-13,30657.6,-2.0161], Tmin=(381.545,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (258.313,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 2, 'C=O': 1, 'C#N': 2, 'C=C': 1}

External symmetry: 2, optical isomers: 1

Geometry:
O       2.47990000   -0.14696700   -0.11346600
N      -1.09578900    2.33351300    0.05254200
N      -1.36339600   -2.18777300    0.05997600
C      -0.00033600    0.00002000    0.00001500
C       1.33835500   -0.07931600   -0.06123500
C      -0.60551500    1.28803300    0.02903200
C      -0.75322100   -1.20750900    0.03313600
""",
)

entry(
    index = 122,
    label = "C3HNO3_9",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {5,S}
2 O u0 p2 c0 {1,S} {8,S}
3 O u0 p2 c0 {6,D}
4 N u0 p1 c0 {7,T}
5 C u0 p0 c0 {1,S} {6,D} {7,S}
6 C u0 p0 c0 {3,D} {5,D}
7 C u0 p0 c0 {4,T} {5,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.62431,0.0333711,5.05364e-05,-3.05452e-07,3.38006e-10,4645.4,12.1285], Tmin=(10,'K'), Tmax=(368.609,'K')),
            NASAPolynomial(coeffs=[6.79344,0.0245438,-1.75662e-05,5.85629e-09,-7.31688e-13,4238.1,-2.3535], Tmin=(368.609,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (38.6444,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'H-O': 1, 'C=O': 1, 'O-O': 1, 'C#N': 1, 'C-C': 1, 'C-O': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [5, 1, 2, 8], invalidation reason: 
* Invalidated! pivots: [1, 5], dihedral: [2, 1, 5, 6], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.47797700   -0.71683700   -1.02045600
O      -1.48664600   -1.20786800   -0.02461600
O       2.53270700   -0.88658200    0.35588100
N      -0.21121700    2.59392600    0.05229600
C       0.38150000    0.12750100   -0.38378200
C       1.53442200   -0.41112500    0.04446900
C       0.06752200    1.48720600   -0.13692100
H      -2.29456600   -0.88575000   -0.45241100
""",
)

entry(
    index = 123,
    label = "C4H2N2O2_51",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {5,S} {6,S}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {10,S}
4  O u0 p2 c0 {2,S} {9,S}
5  C u0 p0 c0 {1,S} {7,T}
6  C u0 p0 c0 {1,S} {8,T}
7  N u0 p1 c0 {5,T}
8  N u0 p1 c0 {6,T}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72029,0.0216311,0.000148878,-4.85083e-07,4.32256e-10,-9786.26,11.2017], Tmin=(10,'K'), Tmax=(404.961,'K')),
            NASAPolynomial(coeffs=[5.94602,0.0339123,-2.35343e-05,7.6962e-09,-9.4914e-13,-10247.5,-0.993256], Tmin=(404.961,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-81.3624,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 2, 'C-C': 2, 'C-O': 2, 'C#N': 2, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [1, 6], dihedral: [10, 1, 6, 2], invalidation reason: Another conformer for C4H2N2O2_51 exists which is 4.29 kJ/mol lower.
* Invalidated! pivots: [2, 6], dihedral: [9, 2, 6, 1], invalidation reason: 


External symmetry: 2, optical isomers: 1

Geometry:
O       1.09931500    0.85283500    0.74563100
O      -0.00759600    0.34547800   -1.05526000
N       2.42155600   -2.03316400    2.21043600
N       0.07920600   -3.10679600   -1.60047200
C       1.00289700   -1.45672600    0.14346300
C       0.70559200   -0.11937100   -0.05056500
C       1.78184200   -1.82451400    1.26830100
C       0.51641500   -2.40453000   -0.79049800
H      -0.28966900   -0.38168400   -1.63171300
H       1.62265100    0.49483100    1.47951200
""",
)

entry(
    index = 124,
    label = "C3H2NO3_2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {7,S} {8,D}
3 N u0 p1 c0 {1,S} {4,D}
4 C u0 p0 c0 {3,D} {9,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u1 p2 c0 {2,S}
8 O u0 p2 c0 {2,D}
9 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87489,0.0178513,0.000436694,-4.03285e-06,1.13205e-08,-29848.9,11.1774], Tmin=(10,'K'), Tmax=(123.923,'K')),
            NASAPolynomial(coeffs=[4.19635,0.0316147,-2.20951e-05,7.19707e-09,-8.8243e-13,-29875.4,9.54989], Tmin=(123.923,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-242.152,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (199.547,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 2, 'C=N': 1, 'C-H': 2, 'C-C': 1, 'C-O': 1, 'C-N': 1}
1D rotors:
pivots: [4, 5], dihedral: [7, 4, 5, 6], rotor symmetry: 1, max scan energy: 5.19 kJ/mol
pivots: [5, 6], dihedral: [4, 5, 6, 1], rotor symmetry: 2, max scan energy: 14.66 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 7 4 5 8 F


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.52957900   -1.69293700   -0.72054700
O      -0.60296500    0.00332700   -1.53757000
O       1.92122200    2.17936100   -0.60818300
N       0.66578400    0.75658900    0.80851300
C      -0.04996300   -0.48175900    0.78649200
C      -0.75349400   -0.72285600   -0.53299700
C       1.28672900    1.43163100    0.02162700
H       0.61800300   -1.33118100    0.97072300
H      -0.79881700   -0.48958700    1.58191900
""",
)

entry(
    index = 125,
    label = "C4H2N2O3_52",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,D}
3  O u0 p2 c0 {1,S} {10,S}
4  C u0 p0 c0 {1,S} {8,T}
5  C u0 p0 c0 {1,S} {9,T}
6  O u0 p2 c0 {2,S} {11,S}
7  O u0 p2 c0 {2,D}
8  N u0 p1 c0 {4,T}
9  N u0 p1 c0 {5,T}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.4936,0.04379,3.00808e-05,-1.48798e-07,1.103e-10,-30746.5,12.4255], Tmin=(10,'K'), Tmax=(553.418,'K')),
            NASAPolynomial(coeffs=[8.13185,0.0375216,-2.68045e-05,8.72104e-09,-1.05852e-12,-31677.3,-10.9782], Tmin=(553.418,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-255.711,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (249.434,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 2, 'C-C': 3, 'C-O': 2, 'C=O': 1, 'C#N': 2}
1D rotors:
pivots: [1, 6], dihedral: [10, 1, 6, 7], rotor symmetry: 1, max scan energy: 20.47 kJ/mol
pivots: [2, 7], dihedral: [11, 2, 7, 3], rotor symmetry: 1, max scan energy: 48.88 kJ/mol
* Invalidated! pivots: [6, 7], dihedral: [1, 6, 7, 2], invalidation reason: 


External symmetry: 1, optical isomers: 1

Geometry:
O       0.28333100    0.13708700    1.49626700
O       0.86582700    1.56955300   -1.73920200
O       0.53073300    2.47813200    0.30310000
N       2.78216400   -1.17923000   -0.34975600
N      -1.49941200   -1.10222100   -1.08648500
C       0.51874900    0.07847400    0.12197300
C       0.64093800    1.53967900   -0.43540700
C       1.78297500   -0.64078000   -0.15790100
C      -0.60359900   -0.59785500   -0.56855700
H       0.26069000    1.08188400    1.72651500
H       0.93211500    2.49368100   -2.02785900
""",
)

entry(
    index = 126,
    label = "C4HN2O3_11",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,D} {4,S}
2  C u0 p0 c0 {1,S} {5,S} {7,D}
3  N u0 p1 c0 {1,D} {6,S}
4  C u0 p0 c0 {1,S} {8,T}
5  O u0 p2 c0 {2,S} {9,S}
6  C u1 p0 c0 {3,S} {10,D}
7  O u0 p2 c0 {2,D}
8  N u0 p1 c0 {4,T}
9  H u0 p0 c0 {5,S}
10 O u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.538,0.0401633,4.17676e-05,-2.28873e-07,2.15287e-10,-26063.4,13.408], Tmin=(10,'K'), Tmax=(428.86,'K')),
            NASAPolynomial(coeffs=[6.80429,0.0343729,-2.4282e-05,7.95949e-09,-9.78855e-13,-26570.4,-2.23016], Tmin=(428.86,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-216.718,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C=N': 1, 'C=O': 2, 'C-N': 1, 'C-C': 2, 'C#N': 1, 'C-O': 1}
1D rotors:
* Invalidated! pivots: [1, 7], dihedral: [10, 1, 7, 2], invalidation reason: 
* Invalidated! pivots: [4, 9], dihedral: [6, 4, 9, 3], invalidation reason: 
* Invalidated! pivots: [6, 7], dihedral: [4, 6, 7, 1], invalidation reason: 
* Invalidated! pivots: [4, 6], dihedral: [9, 4, 6, 7], invalidation reason: 
* Invalidated! pivots: [6, 8], dihedral: [4, 6, 8, 5], invalidation reason: 


External symmetry: 1, optical isomers: 1

Geometry:
O      -1.98427100   -0.51071300    0.17421200
O      -0.12985200   -1.73756900   -0.25254100
O       3.05398800   -1.12345500   -0.64304600
N       1.42914600    0.54903100   -0.19397600
N      -1.04852300    2.84510600    0.45880400
C       0.08659700    0.59044800    0.00846900
C      -0.67088000   -0.67614100   -0.03955300
C      -0.52798200    1.82822900    0.25443600
C       2.19001400   -0.38563000   -0.42331600
H      -2.40013800   -1.38413500    0.12545100
""",
)

entry(
    index = 127,
    label = "C4H2N2O3_56",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {4,S}
2  C u0 p0 c0 {1,S} {5,S} {7,D}
3  C u0 p0 c0 {1,D} {6,S} {8,S}
4  C u0 p0 c0 {1,S} {10,T}
5  O u0 p2 c0 {2,S} {11,S}
6  N u0 p1 c0 {3,S} {9,D}
7  O u0 p2 c0 {2,D}
8  H u0 p0 c0 {3,S}
9  O u0 p2 c0 {6,D}
10 N u0 p1 c0 {4,T}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.44086,0.0464204,-2.01868e-05,-1.78666e-08,1.50242e-11,-6828.86,12.7365], Tmin=(10,'K'), Tmax=(740.212,'K')),
            NASAPolynomial(coeffs=[7.56767,0.0361182,-2.36245e-05,7.12815e-09,-8.13612e-13,-7768.51,-8.15193], Tmin=(740.212,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-56.847,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (253.591,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C-H': 1, 'C-C': 2, 'C-N': 1, 'C-O': 1, 'C=O': 1, 'C#N': 1, 'C=C': 1, 'N=O': 1}
1D rotors:
pivots: [1, 7], dihedral: [11, 1, 7, 2], rotor symmetry: 1, max scan energy: 52.98 kJ/mol
* Invalidated! pivots: [4, 8], dihedral: [3, 4, 8, 6], invalidation reason: 
* Invalidated! pivots: [6, 7], dihedral: [8, 6, 7, 1], invalidation reason: 


External symmetry: 1, optical isomers: 1

Geometry:
O      -2.25297500   -0.34606100    0.41184700
O      -0.83497200   -2.03711900   -0.04691700
O       3.34858700    0.32789700   -0.76259800
N       2.27135500    0.81022200   -0.48366900
N      -0.70246200    2.66084000    0.33136600
C      -0.00356700    0.20463200   -0.03548400
C      -1.05806600   -0.86572900    0.10377800
C       1.24919500   -0.18107600   -0.34466700
C      -0.36454400    1.57013500    0.16239500
H       1.51159600   -1.22442200   -0.49290900
H      -2.88217200   -1.07980700    0.48669500
""",
)

entry(
    index = 128,
    label = "C3H2NO3_3",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {7,S}
2 C u0 p0 c0 {1,S} {4,S} {6,D}
3 N u0 p1 c0 {1,S} {5,D}
4 O u0 p2 c0 {2,S} {8,S}
5 C u0 p0 c0 {3,D} {9,D}
6 O u0 p2 c0 {2,D}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {4,S}
9 O u0 p2 c0 {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75011,0.0375837,-2.80879e-05,9.48417e-09,-1.20008e-12,-42326.2,13.3732], Tmin=(10,'K'), Tmax=(1655.81,'K')),
            NASAPolynomial(coeffs=[19.1802,0.0040555,-1.10902e-06,-1.15177e-11,2.72729e-14,-47949.7,-70.4005], Tmin=(1655.81,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-351.947,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (191.233,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 2, 'H-O': 1, 'C=N': 1, 'C-H': 1, 'C-C': 1, 'C-O': 1, 'C-N': 1}
1D rotors:
pivots: [1, 6], dihedral: [9, 1, 6, 2], rotor symmetry: 1, max scan energy: 47.60 kJ/mol
pivots: [4, 5], dihedral: [7, 4, 5, 6], rotor symmetry: 1, max scan energy: 33.52 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 5 4 7 F
B 5 8 F
pivots: [5, 6], dihedral: [4, 5, 6, 1], rotor symmetry: 1, max scan energy: 63.09 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 8 4 5 6 F
D 7 4 5 6 F
pivots: [4, 7], dihedral: [5, 4, 7, 3], rotor symmetry: 1, max scan energy: 6.04 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O      -1.25770900   -2.44379600    1.00893600
O       0.79449000   -2.73544200    0.08968200
O       3.06532600   -0.59724700   -1.24258300
N       0.95802700    0.02930700   -0.34047400
C      -0.11289100   -0.56548400    0.23486900
C      -0.11870300   -2.00488600    0.42182200
C       2.01987100   -0.39110600   -0.78163200
H      -0.93847600    0.05928400    0.53970900
H      -1.17383800   -3.40437700    1.09280700
""",
)

entry(
    index = 129,
    label = "C4HN2O3_57",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,D} {4,S}
2  C u0 p0 c0 {1,S} {5,S} {7,D}
3  C u1 p0 c0 {1,D} {6,S}
4  C u0 p0 c0 {1,S} {8,T}
5  O u0 p2 c0 {2,S} {9,S}
6  N u0 p1 c0 {3,S} {10,D}
7  O u0 p2 c0 {2,D}
8  N u0 p1 c0 {4,T}
9  H u0 p0 c0 {5,S}
10 O u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7255,0.0263207,0.00022037,-1.06453e-06,1.43558e-09,3667.59,14.4495], Tmin=(10,'K'), Tmax=(265.314,'K')),
            NASAPolynomial(coeffs=[5.03575,0.0383358,-2.71712e-05,8.79931e-09,-1.06985e-12,3486.25,7.75965], Tmin=(265.314,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (30.5273,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (224.491,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C-C': 2, 'C-N': 1, 'C-O': 1, 'C=O': 1, 'C#N': 1, 'C=C': 1, 'N=O': 1}
1D rotors:
pivots: [1, 7], dihedral: [10, 1, 7, 2], rotor symmetry: 1, max scan energy: 50.93 kJ/mol
* Invalidated! pivots: [4, 8], dihedral: [3, 4, 8, 6], invalidation reason: 
* Invalidated! pivots: [6, 7], dihedral: [8, 6, 7, 1], invalidation reason: 
pivots: [6, 8], dihedral: [7, 6, 8, 4], rotor symmetry: 1, max scan energy: 0.02 kJ/mol (set as a FreeRotor)


External symmetry: 1, optical isomers: 1

Geometry:
O      -0.28064700   -0.70834500    2.13427000
O      -2.07259800    0.48690800    1.44722800
O       3.45490800   -0.67653600   -0.11678200
N       2.32828000   -0.27819900   -0.03337100
N      -1.04194000    2.15294300   -1.59291300
C      -0.06927200    0.55329400    0.16795800
C      -0.93484600    0.12650800    1.30178200
C       1.22401400    0.11462800    0.04496000
C      -0.61392600    1.43217800   -0.79345800
H      -0.89759500   -0.94427600    2.84277100
""",
)

entry(
    index = 130,
    label = "C3H2N2O2_13",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 C u0 p0 c0 {1,S} {5,S} {6,D}
3 N u0 p1 c0 {1,D} {9,S}
4 C u0 p0 c0 {1,S} {7,T}
5 O u0 p2 c0 {2,S} {8,S}
6 O u0 p2 c0 {2,D}
7 N u0 p1 c0 {4,T}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81704,0.0126788,0.00014456,-3.97243e-07,3.11939e-10,-17211.3,10.9362], Tmin=(10,'K'), Tmax=(450.659,'K')),
            NASAPolynomial(coeffs=[5.56497,0.0296654,-2.01575e-05,6.45582e-09,-7.86e-13,-17698.9,0.234864], Tmin=(450.659,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-143.122,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (203.705,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C=N': 1, 'C=O': 1, 'C-C': 2, 'C#N': 1, 'C-O': 1, 'H-N': 1}
1D rotors:
pivots: [1, 6], dihedral: [8, 1, 6, 2], rotor symmetry: 1, max scan energy: 55.14 kJ/mol
* Invalidated! pivots: [5, 6], dihedral: [3, 5, 6, 1], invalidation reason: 


External symmetry: 1, optical isomers: 1

Geometry:
O      -1.64271700    0.20385000    0.23702400
O       0.47421100   -0.53641700    0.17620600
N      -2.52661700   -2.25619300    0.64614600
N       0.39519100   -4.12380400    0.67940100
C      -1.26680000   -2.13613200    0.53226200
C      -0.69998500   -0.73556100    0.29443300
C      -0.31698600   -3.21925800    0.60903300
H      -2.50618000   -0.23207100    0.36407700
H      -2.83648600   -3.21612800    0.80308300
""",
)

entry(
    index = 131,
    label = "C3H2N2O3_14",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {4,S}
2  C u0 p0 c0 {1,S} {5,S} {7,D}
3  N u0 p1 c0 {1,D} {6,S}
4  C u0 p0 c0 {1,S} {8,T}
5  O u0 p2 c0 {2,S} {9,S}
6  O u0 p2 c0 {3,S} {10,S}
7  O u0 p2 c0 {2,D}
8  N u0 p1 c0 {4,T}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.6939,0.0245481,0.000127861,-4.31463e-07,3.87478e-10,-24587.8,12.2588], Tmin=(10,'K'), Tmax=(403.984,'K')),
            NASAPolynomial(coeffs=[5.76267,0.034797,-2.4303e-05,7.95046e-09,-9.79024e-13,-25005.7,1.04936], Tmin=(403.984,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-204.43,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'N-O': 1, 'H-O': 2, 'C=N': 1, 'C=O': 1, 'C-C': 2, 'C#N': 1, 'C-O': 1}
1D rotors:
* Invalidated! pivots: [1, 7], dihedral: [9, 1, 7, 3], invalidation reason: 
* Invalidated! pivots: [2, 4], dihedral: [10, 2, 4, 6], invalidation reason: 
* Invalidated! pivots: [6, 7], dihedral: [4, 6, 7, 1], invalidation reason: 


External symmetry: 1, optical isomers: 1

Geometry:
O      -1.53073400   -1.45121500   -0.43904600
O       2.28524000   -0.37617200    0.11273100
O      -2.10435900    0.72297000   -0.60455600
N       1.00244700   -0.79309400   -0.07079300
N       0.86811800    2.66999500   -0.21397100
C       0.17440200    0.17831000   -0.23311000
C      -1.27628400   -0.13435000   -0.44626800
C       0.54968900    1.56168900   -0.22400800
H      -2.48424800   -1.54604800   -0.58306400
H       2.77784200   -1.19953300    0.21797000
""",
)

entry(
    index = 132,
    label = "C4H6N2O3_5b",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  O u0 p2 c0 {1,S} {6,S}
5  C u0 p0 c0 {1,S} {14,T}
6  O u0 p2 c0 {4,S} {7,S}
7  N u0 p1 c0 {6,S} {15,D}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 N u0 p1 c0 {5,T}
15 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53946,0.0403696,0.000282892,-1.22441e-06,1.42445e-09,4939.51,13.1328], Tmin=(10,'K'), Tmax=(316.54,'K')),
            NASAPolynomial(coeffs=[7.32326,0.0497262,-3.23637e-05,1.01319e-08,-1.21672e-12,4413.54,-5.29351], Tmin=(316.54,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (41.1357,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (349.208,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'N=O': 1, 'C-H': 6, 'O-O': 1, 'C-C': 3, 'C-O': 1, 'C#N': 1, 'N-O': 1}
1D rotors:
pivots: [1, 2], dihedral: [6, 1, 2, 4], rotor symmetry: 1, max scan energy: 42.29 kJ/mol
* Invalidated! pivots: [1, 6], dihedral: [2, 1, 6, 7], invalidation reason: 
* Invalidated! pivots: [2, 4], dihedral: [1, 2, 4, 3], invalidation reason: 
* Invalidated! pivots: [6, 7], dihedral: [1, 6, 7, 10], invalidation reason: 
pivots: [6, 8], dihedral: [1, 6, 8, 13], rotor symmetry: 3, max scan energy: 13.22 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       0.52848300   -0.63628800    1.01915000
O       1.74863800   -1.09866300    0.45791200
O       3.79489400   -0.33347100    0.29193400
N       2.76994600    0.02191400    0.67502700
N       0.58510100    1.69289700   -1.46053600
C      -0.40135300   -0.28723900   -0.03643500
C      -1.63732800    0.18282300    0.73827000
C      -0.68934600   -1.49186800   -0.93710600
C       0.15779100    0.82810400   -0.83015500
H      -1.38611300    1.02430000    1.38421300
H      -2.41767200    0.48989300    0.04058600
H      -2.00768600   -0.64090500    1.35035500
H      -1.10860600   -2.29567800   -0.32917100
H       0.22675300   -1.84414400   -1.40955700
H      -1.40502100   -1.21958700   -1.71527500
""",
)

entry(
    index = 133,
    label = "C4H6NO3_15",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {11,D}
4  C u0 p0 c0 {1,S} {12,D} {13,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {3,D}
12 N u1 p1 c0 {4,D}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.44777,0.0544058,-2.97697e-05,3.60829e-10,3.3893e-12,-6738.17,13.5917], Tmin=(10,'K'), Tmax=(1028.22,'K')),
            NASAPolynomial(coeffs=[11.1194,0.0363309,-2.0571e-05,5.52893e-09,-5.73963e-13,-8937.93,-26.6583], Tmin=(1028.22,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-56.042,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (324.264,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'H-O': 1, 'C=N': 1, 'C=O': 1, 'O-O': 1, 'C-C': 3, 'C-O': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [5, 1, 2, 14], invalidation reason: 
* Invalidated! pivots: [1, 5], dihedral: [2, 1, 5, 7], invalidation reason: 
pivots: [5, 7], dihedral: [1, 5, 7, 3], rotor symmetry: 1, max scan energy: 33.82 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 1 5 8 4 F
D 10 6 7 5 F
D 5 1 2 14 F
pivots: [5, 8], dihedral: [1, 5, 8, 4], rotor symmetry: 1, max scan energy: 32.82 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 1 5 7 6 F
D 5 1 2 14 F
* Invalidated! pivots: [6, 7], dihedral: [10, 6, 7, 3], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
O       0.73286700   -0.42907900   -0.85196500
O       2.11190600   -0.69173500   -1.19205500
O      -1.35361300   -0.84756800    1.93046900
N       2.21572000    0.84086700    1.17135900
C       0.53318200   -0.79900400    0.49020900
C      -1.90705400   -1.01245600   -0.39814900
C      -0.98430500   -0.87254300    0.78178500
C       1.23353000    0.15277400    1.48190200
H       0.93779500   -1.80734900    0.66360900
H      -1.80135100   -0.14332600   -1.05331100
H      -1.62754900   -1.88353000   -0.99722100
H      -2.93261600   -1.10306300   -0.04412100
H       0.79448700    0.16343800    2.49008300
H       2.54304900    0.11230900   -0.84464700
""",
)

entry(
    index = 134,
    label = "C3H3N2O3_17",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {7,D}
2  N u0 p1 c0 {1,S} {9,S} {10,S}
3  C u0 p0 c0 {5,S} {6,S} {8,D}
4  N u0 p1 c0 {1,S} {5,D}
5  C u1 p0 c0 {3,S} {4,D}
6  O u0 p2 c0 {3,S} {11,S}
7  O u0 p2 c0 {1,D}
8  O u0 p2 c0 {3,D}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.66917,0.0275503,0.000111115,-3.69881e-07,3.23985e-10,-33036.3,13.6933], Tmin=(10,'K'), Tmax=(409.327,'K')),
            NASAPolynomial(coeffs=[5.0802,0.0395008,-2.70009e-05,8.69043e-09,-1.05737e-12,-33367.5,5.51234], Tmin=(409.327,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-274.68,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'H-N': 2, 'C=N': 1, 'C=O': 2, 'C-N': 2, 'C-C': 1, 'C-O': 1}
1D rotors:
* Invalidated! pivots: [1, 7], dihedral: [11, 1, 7, 3], invalidation reason: 
* Invalidated! pivots: [4, 6], dihedral: [9, 4, 6, 2], invalidation reason: Significant difference observed between consecutive conformers
* Invalidated! pivots: [5, 6], dihedral: [8, 5, 6, 2], invalidation reason: 
* Invalidated! pivots: [7, 8], dihedral: [1, 7, 8, 5], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
O       2.26869500    0.83523800    1.34045000
O       4.35607100    2.53214600    0.92635300
O       1.99587900   -0.86821300   -0.09684900
N       6.23993900    2.34491800   -0.33888800
N       5.19437100    0.41902300    0.38793300
C       5.19342400    1.85876900    0.34713700
C       2.70699000   -0.13241600    0.52524500
C       4.20427500   -0.29747300    0.52248700
H       6.91879100    1.71857700   -0.73824800
H       6.35613500    3.34192400   -0.41776400
H       2.96689900    1.52160600    1.45044000
""",
)

entry(
    index = 135,
    label = "C4H5N2O3_6",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {11,S} {12,S}
4  O u0 p2 c0 {1,S} {6,S}
5  C u0 p0 c0 {1,S} {13,T}
6  O u0 p2 c0 {4,S} {7,S}
7  N u0 p1 c0 {6,S} {14,D}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 N u0 p1 c0 {5,T}
14 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.6528,0.0283199,0.000159116,-4.6941e-07,3.88873e-10,23830,14.0395], Tmin=(10,'K'), Tmax=(415.831,'K')),
            NASAPolynomial(coeffs=[4.08828,0.053238,-3.57653e-05,1.13569e-08,-1.3681e-12,23542.2,9.29481], Tmin=(415.831,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (198.13,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (328.422,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'N=O': 1, 'C-H': 5, 'O-O': 1, 'C-C': 3, 'C-O': 1, 'C#N': 1, 'N-O': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [6, 1, 2, 4], invalidation reason: The rotor scan has a barrier of 538.54 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
* Invalidated! pivots: [1, 6], dihedral: [2, 1, 6, 7], invalidation reason: The rotor scan has a barrier of 310.68 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
* Invalidated! pivots: [2, 4], dihedral: [1, 2, 4, 3], invalidation reason: The rotor scan has a barrier of 394.01 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
pivots: [6, 7], dihedral: [1, 6, 7, 10], rotor symmetry: 3, max scan energy: 11.84 kJ/mol
* Invalidated! pivots: [6, 8], dihedral: [1, 6, 8, 13], invalidation reason: The rotor scan has a barrier of 218.75 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 1, optical isomers: 2

Geometry:
O       0.73447800   -1.00005400   -0.82285100
O       1.40966300   -1.78116500    0.15600100
O       0.58646700   -2.80075600    2.07575500
N       0.24986100   -2.36856100    0.98709100
N       0.84081500    1.61610800    1.37626000
C      -0.25966000   -0.27950100   -0.07439700
C      -1.22284000    0.32778500   -1.08943000
C      -0.86689900   -1.38347700    0.81107100
C       0.37851600    0.76996100    0.74624800
H      -1.64986200   -0.46728500   -1.70192600
H      -0.68825500    1.02779000   -1.73223800
H      -2.02291600    0.86506500   -0.57773300
H      -1.17920800   -1.04947900    1.79855600
H      -1.68262700   -1.88374000    0.29061100
""",
)

entry(
    index = 136,
    label = "C4H6NO3_18",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {4,D} {9,S}
3  C u0 p0 c0 {1,S} {6,D} {10,S}
4  C u0 p0 c0 {2,D} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {7,S}
6  N u0 p1 c0 {3,D} {13,S}
7  O u0 p2 c0 {5,S} {14,S}
8  H u0 p0 c0 {1,S}
9  O u1 p2 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.41007,0.054708,-3.59771e-05,9.53235e-09,-2.74076e-13,-3645.22,13.951], Tmin=(10,'K'), Tmax=(1110.26,'K')),
            NASAPolynomial(coeffs=[10.7777,0.0350966,-1.88472e-05,4.87035e-09,-4.90652e-13,-5708.49,-24.2884], Tmin=(1110.26,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-30.3461,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (328.422,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 4, 'C-O': 2, 'C=C': 1, 'H-O': 1, 'C=N': 1, 'O-O': 1, 'C-C': 2, 'H-N': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [5, 1, 2, 14], invalidation reason: 
* Invalidated! pivots: [1, 5], dihedral: [2, 1, 5, 6], invalidation reason: 
* Invalidated! pivots: [5, 6], dihedral: [1, 5, 6, 3], invalidation reason: 
* Invalidated! pivots: [5, 7], dihedral: [1, 5, 7, 4], invalidation reason: 
pivots: [6, 8], dihedral: [3, 6, 8, 11], rotor symmetry: 2, max scan energy: 51.30 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 6 8 11 12 F


External symmetry: 1, optical isomers: 2

Geometry:
O       0.04605000    0.88147500    0.95042900
O       1.03772600    1.81939500    0.45096200
O       0.20284300   -1.46984600   -1.76909200
N      -2.36814700   -0.35205000    1.36639000
C      -0.45482500    0.15735400   -0.16203300
C       0.51475200   -0.90228000   -0.71892700
C      -1.75080900   -0.51606400    0.27648400
C       1.70826500   -1.20735600    0.00124500
H      -0.68232300    0.84512300   -0.98550400
H      -2.14634400   -1.20925900   -0.46913200
H       1.96687700   -0.69610200    0.91765100
H       2.36812300   -1.96141800   -0.40855100
H      -1.87676700    0.31935500    1.96314000
H       0.64489900    2.65300000    0.74621300
""",
)

entry(
    index = 137,
    label = "C4H5NO3_19",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {11,D}
4  O u0 p2 c0 {1,S} {6,S}
5  C u0 p0 c0 {1,S} {12,T}
6  O u0 p2 c0 {4,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {3,D}
12 N u0 p1 c0 {5,T}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.54412,0.0495935,-2.90811e-05,3.16106e-09,1.91962e-12,-19014,12.7047], Tmin=(10,'K'), Tmax=(1069.36,'K')),
            NASAPolynomial(coeffs=[11.2851,0.030777,-1.69091e-05,4.4391e-09,-4.51979e-13,-21249.3,-27.8707], Tmin=(1069.36,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-158.091,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 4, 'H-O': 1, 'C=O': 1, 'O-O': 1, 'C#N': 1, 'C-C': 3, 'C-O': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [5, 1, 2, 13], invalidation reason: 
* Invalidated! pivots: [1, 5], dihedral: [2, 1, 5, 7], invalidation reason: 
pivots: [5, 7], dihedral: [1, 5, 7, 3], rotor symmetry: 1, max scan energy: 41.08 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 10 6 7 3 F
D 5 1 2 13 F
D 2 1 5 7 F
pivots: [6, 7], dihedral: [10, 6, 7, 3], rotor symmetry: 3, max scan energy: 2.76 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.08052100   -2.29042100   -0.28564100
O      -1.36459800   -2.67401000    1.07816000
O      -0.57415200   -0.02031200    1.06405000
N       1.01671800   -1.64796300   -2.79894600
C       0.24688300   -1.79491800   -0.30440300
C       1.63754400    0.36374000    0.22310700
C       0.35379700   -0.40220900    0.39550000
C       0.66575100   -1.73406600   -1.70525700
H       0.90928500   -2.48769100    0.23401300
H       2.50577000   -0.28648900    0.36462500
H       1.69595800    0.75487500   -0.79728400
H       1.66508300    1.18993100    0.93155000
H      -1.66240900   -1.81819800    1.43169200
""",
)

entry(
    index = 138,
    label = "C3H8N2O3_10",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {6,S} {12,S}
4  N u0 p1 c0 {5,S} {7,S} {13,S}
5  N u0 p1 c0 {4,S} {14,S} {15,S}
6  O u0 p2 c0 {3,S} {7,S}
7  O u0 p2 c0 {4,S} {6,S}
8  O u0 p2 c0 {2,S} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.3294,0.0591996,-3.85347e-05,1.24139e-08,-1.55812e-12,-14663.2,13.1785], Tmin=(10,'K'), Tmax=(1432.17,'K')),
            NASAPolynomial(coeffs=[13.3861,0.0345652,-1.63509e-05,3.77132e-09,-3.43401e-13,-17898,-40.1881], Tmin=(1432.17,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-121.983,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (382.466,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-N': 3, 'N-N': 1, 'H-O': 1, 'C-H': 4, 'O-O': 1, 'C=C': 1, 'C-C': 1, 'C-O': 2, 'N-O': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [8, 1, 2, 4], invalidation reason: 
* Invalidated! pivots: [1, 8], dihedral: [2, 1, 8, 7], invalidation reason: 
* Invalidated! pivots: [2, 4], dihedral: [1, 2, 4, 5], invalidation reason: 
* Invalidated! pivots: [3, 7], dihedral: [16, 3, 7, 6], invalidation reason: 
* Invalidated! pivots: [4, 5], dihedral: [2, 4, 5, 14], invalidation reason: 
* Invalidated! pivots: [6, 7], dihedral: [9, 6, 7, 3], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
O       1.40876000   -3.23942800   -1.74509100
O      -0.50248800   -3.93618300   -1.76851700
O       0.89180900   -0.54851600   -1.68338900
N      -0.92152800   -3.48880800   -2.88319800
N      -1.09344000   -2.04174400   -2.89744300
C       1.98289800   -0.27893100    0.41167900
C       1.53242100   -1.16424200   -0.69717400
C       1.75967100   -2.54128800   -0.74115700
H       1.12321700    0.20902900    0.88456900
H       2.52882400   -0.84355300    1.16819300
H       2.62998200    0.51699700    0.02799400
H       2.23708700   -3.00913700    0.12904400
H      -0.31992900   -3.74229900   -3.67706000
H      -1.75310000   -1.85601800   -2.14303400
H      -1.56405700   -1.80106700   -3.76979500
H       0.42359100   -1.20712600   -2.26512400
""",
)

entry(
    index = 139,
    label = "C4H5NO3_20",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {5,S}
3  C u0 p0 c0 {2,D} {4,S} {6,S}
4  O u0 p2 c0 {3,S} {7,S}
5  O u0 p2 c0 {2,S} {12,S}
6  C u0 p0 c0 {3,S} {11,T}
7  O u0 p2 c0 {4,S} {13,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 N u0 p1 c0 {6,T}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53815,0.0421825,8.70129e-05,-3.9325e-07,4.05516e-10,-19109.3,12.7608], Tmin=(10,'K'), Tmax=(361.392,'K')),
            NASAPolynomial(coeffs=[5.31329,0.0466448,-3.15801e-05,1.01256e-08,-1.2309e-12,-19395.1,3.82523], Tmin=(361.392,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-158.858,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 3, 'C-O': 2, 'C=C': 1, 'H-O': 2, 'O-O': 1, 'C#N': 1, 'C-C': 2}
1D rotors:
pivots: [1, 3], dihedral: [7, 1, 3, 13], rotor symmetry: 1, max scan energy: 23.98 kJ/mol
* Invalidated! pivots: [1, 7], dihedral: [3, 1, 7, 6], invalidation reason: Significant difference observed between consecutive conformers
* Invalidated! pivots: [2, 6], dihedral: [12, 2, 6, 5], invalidation reason: 
* Invalidated! pivots: [5, 6], dihedral: [9, 5, 6, 2], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
O       0.41503000   -0.83274300    1.74159100
O      -1.57304000   -1.25400600    0.01945100
O       1.52074700   -1.77574400    1.35984000
N       1.86279100    2.05105100    0.56462200
C      -1.25295200    0.74277000   -1.22156400
C      -0.81947100   -0.15960700   -0.12135400
C       0.22566100    0.06660600    0.72188500
C       1.11812100    1.16785700    0.62633700
H      -2.28698400    1.05626200   -1.05354200
H      -1.22466900    0.19714800   -2.16889700
H      -0.61586100    1.62248600   -1.29382800
H      -1.21612700   -1.76297800    0.76705100
H       2.18036300   -1.51819400    2.02089900
""",
)

entry(
    index = 140,
    label = "C4H3NO2_21",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,D}
3  C u0 p0 c0 {2,S} {4,S} {9,D}
4  C u0 p0 c0 {3,S} {10,T}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {2,D}
9  O u0 p2 c0 {3,D}
10 N u0 p1 c0 {4,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65027,0.0407542,-3.39331e-05,1.48766e-08,-2.75051e-12,-15868.8,11.5521], Tmin=(10,'K'), Tmax=(1126.38,'K')),
            NASAPolynomial(coeffs=[7.19701,0.028159,-1.71602e-05,4.94931e-09,-5.47156e-13,-16667.8,-5.98099], Tmin=(1126.38,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-131.965,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (228.648,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 3, 'C=O': 2, 'C-C': 3, 'C#N': 1}
1D rotors:
* Invalidated! pivots: [4, 5], dihedral: [8, 4, 5, 1], invalidation reason: 
pivots: [5, 6], dihedral: [1, 5, 6, 2], rotor symmetry: 1, max scan energy: 21.85 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O      -0.07639600    0.13648600   -1.70044800
O       0.92698000    0.02093800    1.61309100
N       3.28100400    0.64411400   -0.75498300
C      -1.54727500   -0.28698600    0.16582200
C      -0.24102000    0.00293900   -0.51451800
C       0.98845800    0.13720600    0.41720600
C       2.25898800    0.42139600   -0.26940400
H      -1.47608700   -1.21744400    0.73612100
H      -1.77864000    0.50134200    0.88767500
H      -2.33600800   -0.36001200   -0.58056200
""",
)

entry(
    index = 141,
    label = "C3H4N2O3_11",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,D} {9,S}
2  C u0 p0 c0 {4,S} {5,S} {8,D}
3  C u0 p0 c0 {1,S} {6,S} {7,D}
4  N u0 p1 c0 {2,S} {10,S} {11,S}
5  N u0 p1 c0 {1,D} {2,S}
6  O u0 p2 c0 {3,S} {12,S}
7  O u0 p2 c0 {3,D}
8  O u0 p2 c0 {2,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.50432,0.0476548,-2.53768e-05,-2.91084e-09,4.90846e-12,-59201.2,12.4695], Tmin=(10,'K'), Tmax=(948.287,'K')),
            NASAPolynomial(coeffs=[9.70157,0.0327307,-1.95127e-05,5.4401e-09,-5.81567e-13,-60880.9,-19.7588], Tmin=(948.287,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-492.249,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (266.063,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-N': 2, 'C-N': 2, 'C=O': 2, 'H-O': 1, 'C=N': 1, 'C-H': 1, 'C-C': 1, 'C-O': 1}
1D rotors:
pivots: [1, 8], dihedral: [12, 1, 8, 2], rotor symmetry: 1, max scan energy: 55.39 kJ/mol
pivots: [4, 7], dihedral: [10, 4, 7, 3], rotor symmetry: 2, max scan energy: 111.61 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 11 10 4 7 F
D 6 5 7 4 F
pivots: [5, 7], dihedral: [6, 5, 7, 3], rotor symmetry: 1, max scan energy: 35.21 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 10 4 7 3 F
pivots: [6, 8], dihedral: [5, 6, 8, 1], rotor symmetry: 1, max scan energy: 37.13 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O      -1.17648800   -3.38553800    3.11335700
O       0.75261700   -2.70058200    4.02837300
O      -0.33950600    0.82472800    0.72791300
N      -2.29199300   -0.02877000   -0.08425300
N      -1.19909100   -1.21562400    1.55398800
C      -0.21597200   -1.32908100    2.34918700
C      -1.19734600   -0.02665000    0.70982200
C      -0.15020500   -2.53580700    3.25504200
H       0.59357900   -0.60108000    2.41991100
H      -2.95739400   -0.78072000   -0.03317900
H      -2.43255100    0.73236100   -0.72762000
H      -1.75756400   -3.01257000    2.42583100
""",
)

entry(
    index = 142,
    label = "C4H4NO3_22",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {10,S}
3  C u0 p0 c0 {2,D} {4,S} {5,S}
4  O u0 p2 c0 {3,S} {6,S}
5  C u0 p0 c0 {3,S} {11,T}
6  O u0 p2 c0 {4,S} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 O u1 p2 c0 {2,S}
11 N u0 p1 c0 {5,T}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.54056,0.0464408,-3.39266e-05,1.24694e-08,-1.84388e-12,-4202.2,13.8293], Tmin=(10,'K'), Tmax=(1519.06,'K')),
            NASAPolynomial(coeffs=[11.8147,0.024653,-1.24119e-05,3.02718e-09,-2.89904e-13,-6715.95,-29.5479], Tmin=(1519.06,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-34.9763,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (278.535,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 3, 'C-O': 2, 'C=C': 1, 'H-O': 1, 'O-O': 1, 'C#N': 1, 'C-C': 2}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [7, 1, 2, 12], invalidation reason: 
* Invalidated! pivots: [1, 7], dihedral: [2, 1, 7, 6], invalidation reason: The rotor scan has a barrier of 63.24 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
pivots: [5, 6], dihedral: [9, 5, 6, 3], rotor symmetry: 3, max scan energy: 0.57 kJ/mol (set as a FreeRotor)
* Invalidated! pivots: [6, 7], dihedral: [3, 6, 7, 1], invalidation reason: 


External symmetry: 1, optical isomers: 1

Geometry:
O      -1.00930200   -0.85730400   -2.06483900
O       0.35607700   -0.44777400   -2.12706500
O      -0.28533700    1.44567900   -0.57401500
N      -4.25906900   -0.99746500   -1.30705300
C      -2.51768700    1.76626800    0.25107400
C      -1.46300200    1.04935600   -0.55183500
C      -1.84420900   -0.12273700   -1.30721000
C      -3.16294300   -0.62216000   -1.32300800
H      -2.04942600    2.61460900    0.74684900
H      -2.96054500    1.10262900    0.99845900
H      -3.32862200    2.11837900   -0.39198800
H       0.37446800    0.36582300   -1.53755400
""",
)

entry(
    index = 143,
    label = "C4H5NO2_23",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  C u0 p0 c0 {2,D} {5,S} {6,S}
4  O u0 p2 c0 {2,S} {12,S}
5  O u0 p2 c0 {3,S} {11,S}
6  C u0 p0 c0 {3,S} {10,T}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 N u0 p1 c0 {6,T}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84543,0.0152502,0.000297658,-1.33081e-06,1.86151e-09,-27489.2,11.9688], Tmin=(10,'K'), Tmax=(236.541,'K')),
            NASAPolynomial(coeffs=[3.61565,0.0428137,-2.72837e-05,8.19256e-09,-9.4318e-13,-27544.6,11.346], Tmin=(236.541,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-228.532,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (270.22,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 3, 'C-O': 2, 'C=C': 1, 'H-O': 2, 'C-C': 2, 'C#N': 1}
1D rotors:
pivots: [1, 5], dihedral: [12, 1, 5, 4], rotor symmetry: 1, max scan energy: 46.49 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 11 2 6 7 F
pivots: [2, 6], dihedral: [11, 2, 6, 5], rotor symmetry: 1, max scan energy: 39.21 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 12 1 5 4 F
pivots: [4, 5], dihedral: [8, 4, 5, 1], rotor symmetry: 3, max scan energy: 6.82 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.19189500    0.55811300    2.68371900
O      -1.88818700    0.95168500    0.07059800
N       1.00114100   -0.80047900   -0.62938800
C      -0.19188700   -0.69641500    3.00107600
C      -1.11746300    0.01463800    2.07759200
C      -0.95130400    0.16284700    0.74352500
C       0.13922600   -0.36224400    0.00825300
H      -0.73465300   -1.48570800    3.52866800
H       0.64881200   -1.13564700    2.46612900
H       0.18810500    0.00058400    3.75365800
H      -2.20045600    0.47852200   -0.70914300
H      -2.70845300    1.01236400    1.99929200
""",
)

entry(
    index = 144,
    label = "C3H4N2O3_12",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,D} {9,S}
2  C u0 p0 c0 {4,S} {6,S} {7,D}
3  C u0 p0 c0 {1,S} {5,S} {8,D}
4  N u0 p1 c0 {1,D} {2,S}
5  O u0 p2 c0 {3,S} {12,S}
6  O u0 p2 c0 {2,S} {10,S}
7  N u0 p1 c0 {2,D} {11,S}
8  O u0 p2 c0 {3,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83349,0.0376403,6.53327e-07,-2.27581e-08,9.25348e-12,-50695.8,12.994], Tmin=(10,'K'), Tmax=(1144.46,'K')),
            NASAPolynomial(coeffs=[13.5769,0.0265138,-1.4814e-05,3.75671e-09,-3.62319e-13,-54427.5,-41.8871], Tmin=(1144.46,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-421.432,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (261.906,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-N': 1, 'H-O': 2, 'C=O': 1, 'C=N': 2, 'C-H': 1, 'C-C': 1, 'C-O': 2, 'C-N': 1}
1D rotors:
pivots: [1, 8], dihedral: [12, 1, 8, 3], rotor symmetry: 1, max scan energy: 53.12 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 6 4 7 2 F
pivots: [2, 7], dihedral: [10, 2, 7, 4], rotor symmetry: 1, max scan energy: 37.47 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 6 4 7 2 F
pivots: [4, 7], dihedral: [6, 4, 7, 2], rotor symmetry: 1, max scan energy: 26.94 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 10 2 7 4 F
pivots: [6, 8], dihedral: [4, 6, 8, 1], rotor symmetry: 1, max scan energy: 36.94 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 6 4 7 2 F
pivots: [5, 7], dihedral: [11, 5, 7, 2], rotor symmetry: 1, max scan energy: 138.65 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 6 4 7 2 F
A 7 5 11 F


External symmetry: 1, optical isomers: 2

Geometry:
O       2.49496700    0.67629700    1.03180600
O      -2.24441000    0.96316700    1.12112000
O       2.95803700   -1.11099100   -0.23908300
N      -0.11581000    0.33332800    0.53059900
N      -1.98492900   -0.51790800   -0.64489200
C       0.68071100   -0.49381600   -0.01399900
C      -1.51538100    0.20564600    0.27426500
C       2.16105100   -0.35207800    0.23951500
H       0.35771500   -1.30621300   -0.66541200
H      -1.63579100    1.43632800    1.70306600
H      -3.00134200   -0.46117200   -0.67656300
H       1.66939000    1.12936500    1.27695800
""",
)

entry(
    index = 145,
    label = "C4H4NO2_24",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  C u0 p0 c0 {2,D} {5,S} {9,S}
4  O u0 p2 c0 {2,S} {11,S}
5  C u0 p0 c0 {3,S} {10,T}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u1 p2 c0 {3,S}
10 N u0 p1 c0 {5,T}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85244,0.0162256,0.000254206,-1.26474e-06,2.01402e-09,-16106.6,11.5347], Tmin=(10,'K'), Tmax=(199.48,'K')),
            NASAPolynomial(coeffs=[3.31841,0.0402517,-2.66038e-05,8.41283e-09,-1.01558e-12,-16111.8,12.586], Tmin=(199.48,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-133.804,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 3, 'C-O': 2, 'C=C': 1, 'H-O': 1, 'C-C': 2, 'C#N': 1}
1D rotors:
* Invalidated! pivots: [1, 5], dihedral: [11, 1, 5, 4], invalidation reason: 
* Invalidated! pivots: [4, 5], dihedral: [8, 4, 5, 1], invalidation reason: 
* Invalidated! pivots: [5, 6], dihedral: [1, 5, 6, 2], invalidation reason: 


External symmetry: 1, optical isomers: 1

Geometry:
O      -1.05812600    0.84543400   -0.61170700
O       0.99795100    1.51012800    0.83429300
N       2.81621000   -1.39847600    1.00042100
C      -0.41099100   -1.43344000   -0.94833900
C      -0.15815800   -0.09359500   -0.37017500
C       0.94860300    0.32772700    0.42840400
C       1.98763000   -0.63541100    0.74575600
H      -0.49002300   -1.36145200   -2.03798000
H       0.38428300   -2.13252700   -0.69331200
H      -1.36499000   -1.82518700   -0.58068900
H      -0.72168400    1.64825800   -0.15423300
""",
)

entry(
    index = 146,
    label = "C4H4NO2_25",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {4,S} {5,S}
4  O u0 p2 c0 {3,S} {11,S}
5  C u0 p0 c0 {3,S} {10,T}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u1 p2 c0 {2,S}
10 N u0 p1 c0 {5,T}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89176,0.0130037,0.000288748,-1.6405e-06,3.23684e-09,-17568.8,11.9081], Tmin=(10,'K'), Tmax=(127.295,'K')),
            NASAPolynomial(coeffs=[3.04151,0.0397203,-2.60631e-05,8.177e-09,-9.79782e-13,-17547.2,14.2575], Tmin=(127.295,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-145.269,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (253.591,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 3, 'C-O': 2, 'C=C': 1, 'H-O': 1, 'C-C': 2, 'C#N': 1}
1D rotors:
* Invalidated! pivots: [1, 6], dihedral: [11, 1, 6, 5], invalidation reason: 
pivots: [4, 5], dihedral: [8, 4, 5, 2], rotor symmetry: 3, max scan energy: 0.16 kJ/mol (set as a FreeRotor)
* Invalidated! pivots: [5, 6], dihedral: [2, 5, 6, 1], invalidation reason: 


External symmetry: 1, optical isomers: 1

Geometry:
O       0.33349000   -2.02836800    1.18903200
O       1.29240100   -1.14511100   -1.04466400
N       2.84939500   -1.26326400    3.39808900
C       3.39042200   -0.31962200   -0.17693900
C       2.04090700   -0.97611700   -0.08263500
C       1.53878000   -1.46131900    1.20496200
C       2.22979600   -1.36854000    2.42181700
H       3.57337900   -0.03429300   -1.21132800
H       4.17673900   -1.00037400    0.16128900
H       3.43548300    0.56657500    0.46239400
H       0.06302700   -1.97464500    0.24470700
""",
)

entry(
    index = 147,
    label = "C3H3N2O3_13",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,D} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {7,D}
3  C u0 p0 c0 {4,S} {6,D} {9,S}
4  N u0 p1 c0 {1,D} {3,S}
5  O u0 p2 c0 {2,S} {10,S}
6  N u0 p1 c0 {3,D} {11,S}
7  O u0 p2 c0 {2,D}
8  H u0 p0 c0 {1,S}
9  O u1 p2 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.3509,0.0701709,-0.000236716,5.95476e-07,-5.72028e-10,-26822.4,15.1513], Tmin=(10,'K'), Tmax=(331.949,'K')),
            NASAPolynomial(coeffs=[3.96751,0.0437206,-3.12455e-05,1.02075e-08,-1.24728e-12,-26758.6,14.435], Tmin=(331.949,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-223.017,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (241.12,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-N': 1, 'C=O': 1, 'H-O': 1, 'C=N': 2, 'C-H': 1, 'C-C': 1, 'C-O': 2, 'C-N': 1}
1D rotors:
pivots: [1, 7], dihedral: [10, 1, 7, 2], rotor symmetry: 1, max scan energy: 53.37 kJ/mol
pivots: [4, 8], dihedral: [6, 4, 8, 3], rotor symmetry: 1, max scan energy: 7.19 kJ/mol
pivots: [6, 7], dihedral: [4, 6, 7, 1], rotor symmetry: 1, max scan energy: 39.73 kJ/mol
pivots: [5, 8], dihedral: [11, 5, 8, 3], rotor symmetry: 1, max scan energy: 13.31 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -3.50417400   -4.63338600    0.96221000
O      -3.97593700   -3.57932400    2.88429600
O      -1.90429200   -0.16714700   -0.24625200
N      -2.19727200   -2.45529900    0.11088300
N      -0.37106600   -1.62011000   -1.07015600
C      -2.70301200   -2.39540500    1.27305700
C      -3.46168900   -3.59206300    1.80035900
C      -1.53266000   -1.31722000   -0.41930700
H      -2.63428100   -1.53053100    1.93554900
H      -3.00807000   -4.38851400    0.16073000
H      -0.19605200   -0.93150400   -1.80811400
""",
)

entry(
    index = 148,
    label = "C3HN2O3_26",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 N u0 p1 c0 {1,S} {7,D}
4 C u0 p0 c0 {1,S} {8,T}
5 O u0 p2 c0 {2,S} {9,S}
6 O u1 p2 c0 {2,S}
7 O u0 p2 c0 {3,D}
8 N u0 p1 c0 {4,T}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67499,0.0260839,0.00013638,-4.9654e-07,4.70851e-10,-8877.34,12.6112], Tmin=(10,'K'), Tmax=(387.932,'K')),
            NASAPolynomial(coeffs=[6.25376,0.0336915,-2.52666e-05,8.49405e-09,-1.05879e-12,-9334.74,-0.70456], Tmin=(387.932,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-73.7939,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (195.39,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'N=O': 1, 'C=C': 1, 'H-O': 1, 'C-N': 1, 'C-C': 1, 'C#N': 1}
1D rotors:
pivots: [1, 7], dihedral: [9, 1, 7, 2], rotor symmetry: 1, max scan energy: 48.61 kJ/mol
pivots: [4, 6], dihedral: [3, 4, 6, 7], rotor symmetry: 1, max scan energy: 144.92 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 3 4 6 F
D 4 6 7 8 F
pivots: [6, 7], dihedral: [4, 6, 7, 1], rotor symmetry: 1, max scan energy: 32.08 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O      -0.12351900    2.01953200    0.71771900
O      -2.19468300    1.38889900    0.06160400
O      -2.46547800   -1.29430700   -0.22975500
N      -1.31373700   -1.25768800    0.11027800
N       1.91004300   -0.78029100    1.09166900
C      -0.52399900   -0.26773000    0.41969600
C      -1.06441900    1.12810300    0.37183800
C       0.81760400   -0.56303400    0.78906500
H      -0.52449300    2.90059400    0.66998900
""",
)

entry(
    index = 149,
    label = "C3H2N2O3_27",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {5,S} {6,S}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {9,S}
4  O u0 p2 c0 {2,S} {10,S}
5  N u0 p1 c0 {1,S} {7,D}
6  C u0 p0 c0 {1,S} {8,T}
7  O u0 p2 c0 {5,D}
8  N u0 p1 c0 {6,T}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76737,0.0173965,0.000143687,-4.13299e-07,3.36891e-10,-23882.4,11.8979], Tmin=(10,'K'), Tmax=(429.898,'K')),
            NASAPolynomial(coeffs=[4.90248,0.0363208,-2.5227e-05,8.19171e-09,-1.00173e-12,-24252.4,4.21087], Tmin=(429.898,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-198.579,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'N=O': 1, 'C=C': 1, 'H-O': 2, 'C-N': 1, 'C-C': 1, 'C#N': 1}
1D rotors:
* Invalidated! pivots: [1, 7], dihedral: [9, 1, 7, 2], invalidation reason: 
* Invalidated! pivots: [2, 7], dihedral: [10, 2, 7, 1], invalidation reason: 
* Invalidated! pivots: [4, 6], dihedral: [3, 4, 6, 7], invalidation reason: 


External symmetry: 1, optical isomers: 1

Geometry:
O      -0.03669400   -1.85357800   -0.29590300
O      -1.67450000   -0.33786100   -0.02502800
O      -0.95853000    2.13696300   -0.24910300
N       0.27990800    1.71205200   -0.47820000
N       2.96585000   -0.28380400   -0.93888900
C       0.52487600    0.43068100   -0.48319400
C      -0.50609100   -0.61057800   -0.24549500
C       1.87981100    0.04839900   -0.73662400
H      -0.77535600   -2.46050500   -0.13029400
H      -1.55386500    1.35681300   -0.10582100
""",
)

entry(
    index = 150,
    label = "C3H4N2O3_14",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {6,S} {8,D}
2  C u0 p0 c0 {4,D} {5,S} {7,S}
3  N u0 p1 c0 {1,S} {4,D}
4  C u0 p0 c0 {2,D} {3,D}
5  O u0 p2 c0 {2,S} {12,S}
6  O u0 p2 c0 {1,S} {10,S}
7  O u0 p2 c0 {2,S} {9,S}
8  N u0 p1 c0 {1,D} {11,S}
9  H u0 p0 c0 {7,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {8,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65075,0.0245625,0.000205156,-6.03896e-07,4.84958e-10,-28012.5,13.7987], Tmin=(10,'K'), Tmax=(453.947,'K')),
            NASAPolynomial(coeffs=[8.14853,0.0403237,-2.99651e-05,1.02154e-08,-1.29131e-12,-28991.5,-10.6347], Tmin=(453.947,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-232.946,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (261.906,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-N': 1, 'H-O': 3, 'C=N': 2, 'C=C': 1, 'C-O': 3, 'C-N': 1}
1D rotors:
pivots: [1, 7], dihedral: [12, 1, 7, 3], rotor symmetry: 1, max scan energy: 24.11 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 9 3 7 1 F
D 8 4 6 5 F
D 6 4 7 3 F
pivots: [2, 6], dihedral: [10, 2, 6, 4], rotor symmetry: 1, max scan energy: 37.05 kJ/mol
pivots: [3, 7], dihedral: [9, 3, 7, 1], rotor symmetry: 1, max scan energy: 15.73 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 12 1 7 8 F
D 8 4 6 5 F
D 6 4 7 1 F
pivots: [4, 6], dihedral: [8, 4, 6, 2], rotor symmetry: 1, max scan energy: 19.62 kJ/mol
pivots: [5, 6], dihedral: [11, 5, 6, 2], rotor symmetry: 1, max scan energy: 135.48 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 2 6 5 F
D 8 4 6 2 F
A 6 5 11 F


External symmetry: 1, optical isomers: 2

Geometry:
O       6.70748100    2.92741500   -5.53165700
O       5.39873000    0.22250400   -0.77938800
O       6.37503400    4.54524900   -3.86589000
N       5.37039200    1.44520900   -2.71558600
N       7.42817000    0.66329800   -1.82220000
C       6.17499700    0.76560100   -1.74416200
C       6.29725400    3.23573100   -4.26143800
C       5.86096400    2.30676300   -3.44715500
H       5.84688600    5.07309400   -4.48036300
H       4.47763800    0.40523400   -1.00858600
H       7.78741600    0.10002400   -1.05204700
H       7.66103700    3.07930500   -5.58689400
""",
)

entry(
    index = 151,
    label = "C3H3N2O3_15",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,D} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {7,D}
3  C u0 p0 c0 {4,S} {6,S} {9,D}
4  N u0 p1 c0 {1,D} {3,S}
5  O u0 p2 c0 {2,S} {10,S}
6  O u0 p2 c0 {3,S} {11,S}
7  O u0 p2 c0 {2,D}
8  H u0 p0 c0 {1,S}
9  N u1 p1 c0 {3,D}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.62099,0.0443785,-2.24071e-05,-5.43143e-09,5.67743e-12,-25857.1,14.5096], Tmin=(10,'K'), Tmax=(980.751,'K')),
            NASAPolynomial(coeffs=[11.3297,0.0266098,-1.61402e-05,4.52163e-09,-4.82674e-13,-28026.7,-25.8824], Tmin=(980.751,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-214.971,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (241.12,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 2, 'C=O': 1, 'C=N': 2, 'C-H': 1, 'C-C': 1, 'C-O': 2, 'C-N': 1}
1D rotors:
pivots: [1, 7], dihedral: [10, 1, 7, 3], rotor symmetry: 1, max scan energy: 53.79 kJ/mol
pivots: [2, 8], dihedral: [11, 2, 8, 4], rotor symmetry: 1, max scan energy: 28.89 kJ/mol
pivots: [4, 8], dihedral: [6, 4, 8, 2], rotor symmetry: 1, max scan energy: 10.68 kJ/mol
pivots: [6, 7], dihedral: [4, 6, 7, 1], rotor symmetry: 1, max scan energy: 42.52 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.55024200    0.12456100    0.26996100
O       1.81338700    1.89343200    0.46102400
O      -2.23183100   -2.04907000    0.71702500
N       0.09385300    0.45331000    0.07149200
N       2.24064100   -0.04217000   -0.75331700
C      -0.30633300   -0.72080100    0.34588200
C      -1.79347000   -0.96091800    0.46462900
C       1.47025100    0.71326200   -0.09922400
H       0.33882800   -1.58447000    0.51097900
H      -1.95507000    0.87215000    0.08177200
H       2.75447300    2.04520800    0.29750300
""",
)

entry(
    index = 152,
    label = "C3H3N2O3_16",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,D}
2  C u0 p0 c0 {4,D} {7,S} {8,S}
3  N u0 p1 c0 {1,S} {4,D}
4  C u0 p0 c0 {2,D} {3,D}
5  O u0 p2 c0 {1,S} {10,S}
6  N u0 p1 c0 {1,D} {11,S}
7  O u0 p2 c0 {2,S} {9,S}
8  O u1 p2 c0 {2,S}
9  H u0 p0 c0 {7,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.14084,0.0373835,-7.00215e-06,-1.50066e-08,6.8306e-12,-26199.3,14.3857], Tmin=(10,'K'), Tmax=(1190.89,'K')),
            NASAPolynomial(coeffs=[18.315,0.0133869,-6.51798e-06,1.37163e-09,-1.02772e-13,-31249.6,-63.5027], Tmin=(1190.89,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-217.657,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (236.962,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-N': 1, 'H-O': 2, 'C=N': 2, 'C=C': 1, 'C-O': 3, 'C-N': 1}
1D rotors:
pivots: [1, 6], dihedral: [10, 1, 6, 4], rotor symmetry: 1, max scan energy: 39.29 kJ/mol
pivots: [2, 7], dihedral: [9, 2, 7, 3], rotor symmetry: 1, max scan energy: 43.55 kJ/mol
pivots: [4, 6], dihedral: [8, 4, 6, 1], rotor symmetry: 1, max scan energy: 4.58 kJ/mol
pivots: [7, 8], dihedral: [2, 7, 8, 4], rotor symmetry: 1, max scan energy: 21.28 kJ/mol
pivots: [5, 6], dihedral: [11, 5, 6, 1], rotor symmetry: 1, max scan energy: 117.67 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 8 4 6 5 F
A 6 5 11 F


External symmetry: 1, optical isomers: 2

Geometry:
O       0.50604200   -1.59505900    2.57327200
O       5.20549900   -3.20772800    2.81627700
O       5.82170200   -1.20074800    3.67245800
N       2.67975500   -1.10716200    2.93623000
N       0.94042100    0.10290800    4.04475900
C       1.34092000   -0.81100500    3.27308300
C       4.97356200   -1.98227400    3.32286100
C       3.53796300   -1.74652800    3.52654700
H       6.16795400   -3.31967700    2.77893500
H      -0.38842200   -1.29972400    2.79552500
H       1.70799000    0.60748600    4.47858000
""",
)

entry(
    index = 153,
    label = "C3H3N2O3_18",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,D} {5,S} {6,S}
2  C u0 p0 c0 {4,S} {7,S} {8,D}
3  C u0 p0 c0 {1,D} {4,D}
4  N u0 p1 c0 {2,S} {3,D}
5  O u0 p2 c0 {1,S} {9,S}
6  O u0 p2 c0 {1,S} {11,S}
7  O u0 p2 c0 {2,S} {10,S}
8  N u1 p1 c0 {2,D}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.52215,0.0382613,0.000166705,-6.98431e-07,7.01561e-10,-2985.63,17.3029], Tmin=(10,'K'), Tmax=(386.607,'K')),
            NASAPolynomial(coeffs=[9.80784,0.0300809,-2.21449e-05,7.60489e-09,-9.7292e-13,-3896.53,-12.5434], Tmin=(386.607,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-24.7972,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (236.962,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 3, 'C=N': 2, 'C=C': 1, 'C-O': 3, 'C-N': 1}
1D rotors:
pivots: [1, 6], dihedral: [9, 1, 6, 2], rotor symmetry: 1, max scan energy: 18.24 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 11 2 6 1 F
pivots: [2, 6], dihedral: [11, 2, 6, 1], rotor symmetry: 1, max scan energy: 19.28 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 9 1 6 8 F
pivots: [3, 7], dihedral: [10, 3, 7, 4], rotor symmetry: 1, max scan energy: 27.62 kJ/mol
pivots: [4, 7], dihedral: [8, 4, 7, 3], rotor symmetry: 1, max scan energy: 10.79 kJ/mol
pivots: [6, 8], dihedral: [1, 6, 8, 4], rotor symmetry: 1, max scan energy: 0.94 kJ/mol (set as a FreeRotor)


External symmetry: 1, optical isomers: 2

Geometry:
O      -8.22516800    0.77107900   -1.06352800
O      -9.25367300   -0.52058300   -2.72733400
O      -3.78393200    0.24778600   -3.78457400
N      -6.05540500    0.31398700   -3.70493600
N      -4.93228100   -1.75769700   -3.49638700
C      -8.14931600    0.14975600   -2.28053800
C      -4.89334300   -0.50984800   -3.62096800
C      -7.04098300    0.17976800   -2.98481500
H      -8.93865900    1.42312800   -1.10233600
H      -3.01838200   -0.34140300   -3.74995400
H      -9.45801400   -1.22578500   -2.09736100
""",
)

entry(
    index = 154,
    label = "C3H2NO3_19",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {7,S}
2 C u0 p0 c0 {1,S} {4,S} {6,D}
3 O u0 p2 c0 {1,S} {5,S}
4 C u0 p0 c0 {2,S} {8,T}
5 O u0 p2 c0 {3,S} {9,S}
6 O u0 p2 c0 {2,D}
7 H u0 p0 c0 {1,S}
8 N u0 p1 c0 {4,T}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81089,0.014128,0.000167811,-5.24822e-07,4.72156e-10,3674.24,11.5848], Tmin=(10,'K'), Tmax=(394.71,'K')),
            NASAPolynomial(coeffs=[5.64113,0.0292886,-1.7904e-05,5.21364e-09,-5.95858e-13,3267.18,1.13011], Tmin=(394.71,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (30.56,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (195.39,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'H-O': 1, 'C-H': 1, 'O-O': 1, 'C-C': 2, 'C-O': 1, 'C#N': 1}
1D rotors:
pivots: [1, 2], dihedral: [5, 1, 2, 9], rotor symmetry: 1, max scan energy: 29.45 kJ/mol
pivots: [1, 5], dihedral: [2, 1, 5, 6], rotor symmetry: 1, max scan energy: 94.32 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 1 5 6 8 F
D 5 1 2 9 F
B 1 2 F
pivots: [5, 6], dihedral: [1, 5, 6, 3], rotor symmetry: 1, max scan energy: 143.58 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 8 1 5 6 F
D 2 1 5 6 F
D 5 1 2 9 F


External symmetry: 1, optical isomers: 1

Geometry:
O      -0.92766800    0.71639200    0.75412200
O      -1.72763100    0.80893500    1.93926100
O      -1.62474200   -1.76136600    2.02060600
N      -0.02948100   -3.86279100   -0.16760400
C      -0.57905300   -0.48504400    0.34374700
C      -0.92893700   -1.69729200    0.97656600
C      -0.42712100   -2.90471700    0.33815600
H       0.02095800   -0.43217600   -0.55633900
H      -1.84898900   -0.14876800    2.20784800
""",
)

entry(
    index = 155,
    label = "C4H3N2O3_20b",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,D}
3  C u0 p0 c0 {1,S} {9,D} {10,S}
4  O u0 p2 c0 {1,S} {6,S}
5  C u0 p0 c0 {2,S} {11,T}
6  O u0 p2 c0 {4,S} {12,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {2,D}
9  N u1 p1 c0 {3,D}
10 H u0 p0 c0 {3,S}
11 N u0 p1 c0 {5,T}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.41011,0.0502964,5.29044e-05,-2.31501e-07,1.7664e-10,19859.4,14.5612], Tmin=(10,'K'), Tmax=(532.151,'K')),
            NASAPolynomial(coeffs=[9.76961,0.0412565,-3.08757e-05,1.03371e-08,-1.27869e-12,18633.7,-17.2648], Tmin=(532.151,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (165.037,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (266.063,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'H-O': 1, 'C=N': 1, 'C-H': 2, 'O-O': 1, 'C-C': 3, 'C-O': 1, 'C#N': 1}
1D rotors:
pivots: [1, 2], dihedral: [6, 1, 2, 12], rotor symmetry: 1, max scan energy: 47.11 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 7 6 8 11 F
pivots: [1, 6], dihedral: [2, 1, 6, 7], rotor symmetry: 1, max scan energy: 55.86 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 7 6 8 11 F
D 10 6 7 9 F
D 6 1 2 12 F
pivots: [6, 7], dihedral: [1, 6, 7, 3], rotor symmetry: 1, max scan energy: 23.86 kJ/mol
pivots: [6, 8], dihedral: [1, 6, 8, 4], rotor symmetry: 1, max scan energy: 19.77 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 1 6 7 3 F
D 6 1 2 12 F


External symmetry: 1, optical isomers: 2

Geometry:
O       0.05160100    0.86004700   -0.81425200
O      -0.55807900    0.10931200   -1.89501100
O      -0.20230700   -2.03909100    1.22662300
N      -2.63737100    0.75232400   -0.03891500
N       2.42095200   -1.74593800   -0.89728600
C      -0.28861500    0.22459800    0.38596100
C       0.26465000   -1.20928400    0.49276900
C      -1.79380900    0.23121100    0.70550900
C       1.46041100   -1.48941700   -0.31322700
H       0.22700200    0.81853200    1.15409200
H      -2.08089700   -0.27790900    1.63547800
H      -1.41090500    0.57084000   -1.98062500
""",
)

entry(
    index = 156,
    label = "C4H3N2O3_21",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {4,S} {6,S}
2  C u0 p0 c0 {1,D} {5,S} {8,S}
3  C u0 p0 c0 {4,S} {9,D} {10,S}
4  O u0 p2 c0 {1,S} {3,S}
5  O u0 p2 c0 {2,S} {7,S}
6  C u0 p0 c0 {1,S} {11,T}
7  O u0 p2 c0 {5,S} {12,S}
8  H u0 p0 c0 {2,S}
9  N u1 p1 c0 {3,D}
10 H u0 p0 c0 {3,S}
11 N u0 p1 c0 {6,T}
12 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53055,0.050894,2.24255e-06,-6.26975e-08,3.65842e-11,26802,13.4833], Tmin=(10,'K'), Tmax=(784.254,'K')),
            NASAPolynomial(coeffs=[11.9968,0.0366035,-2.5682e-05,8.01244e-09,-9.29791e-13,24585.6,-30.9682], Tmin=(784.254,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (222.834,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (266.063,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C=N': 1, 'C=C': 1, 'C-H': 2, 'O-O': 1, 'C-C': 1, 'C-O': 3, 'C#N': 1}
1D rotors:
pivots: [1, 6], dihedral: [8, 1, 6, 7], rotor symmetry: 1, max scan energy: 32.23 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 6 1 8 4 F
D 7 2 3 12 F
D 1 6 7 10 F
D 3 2 7 10 F
pivots: [1, 8], dihedral: [6, 1, 8, 4], rotor symmetry: 1, max scan energy: 39.20 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 8 1 6 9 F
D 7 2 3 12 F
D 3 2 7 10 F
pivots: [2, 3], dihedral: [7, 2, 3, 12], rotor symmetry: 1, max scan energy: 43.27 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 8 1 6 9 F
D 3 2 7 6 F
pivots: [2, 7], dihedral: [3, 2, 7, 6], rotor symmetry: 1, max scan energy: 52.51 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 9 6 7 2 F
D 6 1 8 4 F
D 8 1 6 9 F
D 7 2 3 12 F


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.04754900    0.34308900   -0.41535000
O      -1.89685200   -2.10338400    0.70525700
O      -1.90651200   -3.47130300    0.18310500
N      -1.78368800   -1.33677700   -1.88828400
N       2.11127000    0.45508100    0.78928300
C      -0.23251600   -0.51292500    0.32105800
C      -0.61107000   -1.70750300    0.80537600
C      -1.72016000   -0.14859400   -1.50084000
C       1.06040500    0.02292200    0.58157500
H       0.08294000   -2.36725600    1.31395100
H      -2.22521900    0.66176500   -2.02938500
H      -2.00816300   -3.26226300   -0.76422900
""",
)

entry(
    index = 157,
    label = "C4H2N2O3_22",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,D}
3  O u0 p2 c0 {1,S} {6,S}
4  C u0 p0 c0 {1,S} {9,T}
5  C u0 p0 c0 {2,S} {10,T}
6  O u0 p2 c0 {3,S} {11,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {2,D}
9  N u0 p1 c0 {4,T}
10 N u0 p1 c0 {5,T}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.4389,0.0469809,0.000135843,-6.48968e-07,6.80378e-10,8134.27,14.0007], Tmin=(10,'K'), Tmax=(378.172,'K')),
            NASAPolynomial(coeffs=[9.68225,0.034311,-2.55806e-05,8.7588e-09,-1.1141e-12,7280.44,-15.0942], Tmin=(378.172,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (67.6652,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (245.277,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'H-O': 1, 'C-H': 1, 'O-O': 1, 'C-C': 3, 'C-O': 1, 'C#N': 2}
1D rotors:
pivots: [1, 2], dihedral: [6, 1, 2, 11], rotor symmetry: 1, max scan energy: 42.47 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 1 6 7 3 F
pivots: [1, 6], dihedral: [2, 1, 6, 7], rotor symmetry: 1, max scan energy: 45.79 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 1 6 7 3 F
D 6 1 2 11 F
pivots: [6, 7], dihedral: [1, 6, 7, 3], rotor symmetry: 1, max scan energy: 19.31 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.57514700    0.47239600    0.08074200
O      -2.25181600   -0.62947700   -0.58008000
O       0.94934600   -0.22566200   -2.27235300
N       0.81568900   -1.79332400    0.91705800
N      -1.39353600    2.10538400   -3.06891600
C      -0.20136100    0.33913800   -0.21264700
C       0.08191400    0.39921600   -1.73405900
C       0.39452700   -0.85611100    0.39837000
C      -0.76807900    1.34583100   -2.46781800
H       0.24635900    1.23663000    0.23477200
H      -2.47260800   -1.19386300    0.17704600
""",
)

entry(
    index = 158,
    label = "C4H2N2O3_23",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {3,S} {5,S}
2  C u0 p0 c0 {1,D} {4,S} {6,S}
3  O u0 p2 c0 {1,S} {7,S}
4  O u0 p2 c0 {2,S} {10,S}
5  C u0 p0 c0 {1,S} {8,T}
6  C u0 p0 c0 {2,S} {9,T}
7  O u0 p2 c0 {3,S} {11,S}
8  N u0 p1 c0 {5,T}
9  N u0 p1 c0 {6,T}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.47231,0.0463188,4.07277e-05,-1.79108e-07,1.28497e-10,7616.22,13.2613], Tmin=(10,'K'), Tmax=(573.078,'K')),
            NASAPolynomial(coeffs=[9.96927,0.0367067,-2.76496e-05,9.24735e-09,-1.13966e-12,6284.76,-19.5855], Tmin=(573.078,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (63.243,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (245.277,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 2, 'C=C': 1, 'O-O': 1, 'C-C': 2, 'C-O': 2, 'C#N': 2}
1D rotors:
pivots: [1, 3], dihedral: [6, 1, 3, 11], rotor symmetry: 1, max scan energy: 27.51 kJ/mol
pivots: [1, 6], dihedral: [3, 1, 6, 7], rotor symmetry: 1, max scan energy: 37.15 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 10 2 7 9 F
D 6 1 3 11 F
pivots: [2, 7], dihedral: [10, 2, 7, 6], rotor symmetry: 1, max scan energy: 34.13 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.29654700    0.59182700    1.43276600
O      -1.11499200   -1.96833800    1.55143500
O       1.14434100    0.77548000    1.74619100
N       0.22838100    1.10534200   -1.91649300
N      -1.34428600   -2.86537200   -1.68900700
C      -0.39993300   -0.11399500    0.26245600
C      -0.85539600   -1.39120900    0.37359200
C      -0.06550500    0.53657500   -0.95449600
C      -1.12940900   -2.20557000   -0.76757600
H      -0.90096300   -1.32343400    2.24639100
H       1.20675500    1.73975900    1.66325100
""",
)

entry(
    index = 159,
    label = "C4HN2O3_24",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {3,S} {4,S}
2  C u0 p0 c0 {1,D} {5,S} {7,S}
3  O u0 p2 c0 {1,S} {6,S}
4  C u0 p0 c0 {1,S} {8,T}
5  C u0 p0 c0 {2,S} {9,T}
6  O u0 p2 c0 {3,S} {10,S}
7  O u1 p2 c0 {2,S}
8  N u0 p1 c0 {4,T}
9  N u0 p1 c0 {5,T}
10 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65132,0.030189,0.000174961,-6.96928e-07,7.47667e-10,23217.4,13.0182], Tmin=(10,'K'), Tmax=(334.492,'K')),
            NASAPolynomial(coeffs=[5.29468,0.0434808,-3.23785e-05,1.07584e-08,-1.32821e-12,22923.2,4.13479], Tmin=(334.492,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (193.087,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (220.334,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C=C': 1, 'O-O': 1, 'C-C': 2, 'C-O': 2, 'C#N': 2}
1D rotors:
pivots: [1, 2], dihedral: [6, 1, 2, 10], rotor symmetry: 1, max scan energy: 26.39 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 2 1 6 7 F
D 8 6 7 3 F
pivots: [1, 6], dihedral: [2, 1, 6, 7], rotor symmetry: 1, max scan energy: 65.99 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 6 1 2 10 F
pivots: [6, 7], dihedral: [1, 6, 7, 3], rotor symmetry: 1, max scan energy: 106.50 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 8 1 6 7 F
D 2 1 6 7 F
D 6 1 2 10 F


External symmetry: 1, optical isomers: 1

Geometry:
O       0.07754700    1.14332900    0.48690700
O       0.37185100    2.31401300   -0.27055900
O       1.41825800    0.74179200   -1.99821400
N      -0.18944800   -2.00404600    1.52517500
N       1.71782600   -2.64189600   -1.99890900
C       0.44281400   -0.04142100   -0.00909800
C       1.11637400   -0.21410400   -1.26248900
C       0.09224900   -1.11590200    0.83928900
C       1.44229400   -1.57636600   -1.65368900
H       0.83099300    1.95993600   -1.08515800
""",
)

entry(
    index = 160,
    label = "C4H2N2O2_25",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {3,S} {5,S}
2  C u0 p0 c0 {1,D} {4,S} {6,S}
3  O u0 p2 c0 {1,S} {9,S}
4  O u0 p2 c0 {2,S} {10,S}
5  C u0 p0 c0 {1,S} {7,T}
6  C u0 p0 c0 {2,S} {8,T}
7  N u0 p1 c0 {5,T}
8  N u0 p1 c0 {6,T}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.6497,0.0265215,0.000160463,-5.44347e-07,4.83319e-10,-2466.89,12.6401], Tmin=(10,'K'), Tmax=(418.576,'K')),
            NASAPolynomial(coeffs=[7.72994,0.0327993,-2.42607e-05,8.23993e-09,-1.04004e-12,-3205.05,-8.22844], Tmin=(418.576,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-20.5151,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (224.491,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 2, 'C=C': 1, 'C-C': 2, 'C-O': 2, 'C#N': 2}
1D rotors:
pivots: [1, 5], dihedral: [9, 1, 5, 6], rotor symmetry: 1, max scan energy: 24.34 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 10 2 6 5 F
pivots: [2, 6], dihedral: [10, 2, 6, 5], rotor symmetry: 1, max scan energy: 35.77 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 9 1 5 7 F


External symmetry: 1, optical isomers: 2

Geometry:
O       0.19907900    0.10267500   -1.98251900
O       0.71609700   -1.61386300    0.00959300
N      -1.06718600    2.80108800   -0.38573800
N      -0.34913000    0.06340100    2.80944000
C      -0.08133700    0.44098600   -0.70586500
C       0.14872900   -0.40284600    0.32996900
C      -0.62414100    1.74414900   -0.52483000
C      -0.13304800   -0.10676300    1.68575500
H       0.54984500   -0.80013700   -1.98318100
H       0.64108000   -2.22869700    0.74737300
""",
)

entry(
    index = 161,
    label = "C3HN2O2_26",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {5,S} {6,S}
2 O u0 p2 c0 {5,D}
3 N u1 p1 c0 {6,D}
4 N u0 p1 c0 {7,T}
5 C u0 p0 c0 {1,S} {2,D} {7,S}
6 C u0 p0 c0 {1,S} {3,D} {8,S}
7 C u0 p0 c0 {4,T} {5,S}
8 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77175,0.0222192,0.000158431,-7.96074e-07,1.09491e-09,12219.7,11.4388], Tmin=(10,'K'), Tmax=(261.387,'K')),
            NASAPolynomial(coeffs=[4.76777,0.0303576,-2.24453e-05,7.45677e-09,-9.2139e-13,12087.7,6.44213], Tmin=(261.387,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (101.629,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (174.604,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'C=N': 1, 'C-H': 1, 'C-C': 1, 'C-O': 2, 'C#N': 1}
1D rotors:
pivots: [1, 5], dihedral: [6, 1, 5, 2], rotor symmetry: 1, max scan energy: 45.40 kJ/mol
pivots: [1, 6], dihedral: [5, 1, 6, 3], rotor symmetry: 1, max scan energy: 15.81 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O      -0.24100000   -0.33463700   -0.53501600
O       0.38080100    0.85206400    1.31203500
N      -2.45413600   -0.42479200   -1.14310600
N       3.07332600   -0.59293000   -0.19198400
C       0.63909700    0.16230700    0.37230200
C      -1.58601700   -0.00785800   -0.35389500
C       1.98799400   -0.27706100    0.02949800
H      -1.80006700    0.62291200    0.51019500
""",
)

entry(
    index = 162,
    label = "C2NO2_27",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {4,S}
2 O u0 p2 c0 {4,D}
3 N u0 p1 c0 {5,T}
4 C u0 p0 c0 {1,S} {2,D} {5,S}
5 C u0 p0 c0 {3,T} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91716,0.00549227,6.44193e-05,-1.65289e-07,1.20761e-10,4317.51,9.1499], Tmin=(10,'K'), Tmax=(483.654,'K')),
            NASAPolynomial(coeffs=[4.72506,0.0141912,-1.02605e-05,3.40008e-09,-4.20883e-13,4059.47,3.97938], Tmin=(483.654,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (35.8813,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'C-C': 1, 'C-O': 1, 'C#N': 1}

External symmetry: 2, optical isomers: 1

Geometry:
O      -1.25484400   -1.00494700    0.03306300
O      -1.16690600    1.10018700    0.11645000
N       2.05811900   -0.08093800   -0.12706300
C      -0.54488500    0.02142800    0.03364000
C       0.90851600   -0.03573000   -0.05608900
""",
)

entry(
    index = 163,
    label = "C3HN2O3_28",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {7,D}
2 C u0 p0 c0 {1,S} {4,S} {6,D}
3 O u0 p2 c0 {1,S} {5,S}
4 O u0 p2 c0 {2,S} {8,S}
5 C u0 p0 c0 {3,S} {9,T}
6 O u0 p2 c0 {2,D}
7 N u1 p1 c0 {1,D}
8 H u0 p0 c0 {4,S}
9 N u0 p1 c0 {5,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67956,0.0222443,0.000170838,-5.3021e-07,4.32808e-10,-6631.87,14.6624], Tmin=(10,'K'), Tmax=(459.449,'K')),
            NASAPolynomial(coeffs=[9.53074,0.0261073,-2.06969e-05,7.32896e-09,-9.50557e-13,-7747.97,-15.3104], Tmin=(459.449,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-55.1794,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (191.233,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'H-O': 1, 'C=N': 1, 'C-C': 1, 'C-O': 3, 'C#N': 1}
1D rotors:
pivots: [1, 6], dihedral: [8, 1, 6, 4], rotor symmetry: 1, max scan energy: 16.14 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 1 6 7 3 F
pivots: [2, 7], dihedral: [9, 2, 7, 3], rotor symmetry: 1, max scan energy: 49.45 kJ/mol
pivots: [6, 7], dihedral: [1, 6, 7, 2], rotor symmetry: 1, max scan energy: 16.88 kJ/mol
pivots: [1, 8], dihedral: [6, 1, 8, 5], rotor symmetry: 1, max scan energy: 0.65 kJ/mol (set as a FreeRotor)


External symmetry: 1, optical isomers: 1

Geometry:
O       1.27680700    0.26669600    0.27198000
O      -2.23222200   -0.12264900   -0.10731500
O      -1.00913300    1.18241400    1.27680800
N       0.05234100   -1.10774000   -1.18639900
N       3.46439300   -0.48197700   -0.55295500
C       0.10311000   -0.25811800   -0.27733200
C      -1.10475600    0.36907300    0.40706400
C       2.41637400   -0.15785000   -0.19473200
H      -2.97668100    0.29781600    0.35080200
""",
)

entry(
    index = 164,
    label = "C3H6N2O3_31",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {2,S} {13,D}
4  O u0 p2 c0 {1,S} {5,S}
5  O u0 p2 c0 {4,S} {6,S}
6  N u0 p1 c0 {5,S} {7,D}
7  N u0 p1 c0 {6,D} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 O u0 p2 c0 {3,D}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85816,0.051454,-1.75864e-05,-1.20403e-08,6.97888e-12,-5038.87,12.1051], Tmin=(10,'K'), Tmax=(1133.64,'K')),
            NASAPolynomial(coeffs=[17.4535,0.0261291,-1.40411e-05,3.49566e-09,-3.33139e-13,-9576.45,-61.6077], Tmin=(1133.64,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-41.7642,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (311.793,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-N': 1, 'N=N': 1, 'C=O': 1, 'C-H': 5, 'O-O': 1, 'C-C': 2, 'C-O': 1, 'N-O': 1}
1D rotors:
pivots: [1, 2], dihedral: [6, 1, 2, 4], rotor symmetry: 1, max scan energy: 202.12 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 2 4 5 F
A 1 2 4 F
D 13 7 8 6 F
D 2 1 6 9 F
D 1 2 4 5 F
D 1 6 8 7 F
B 2 4 F
B 5 14 F
B 1 2 F
pivots: [1, 6], dihedral: [2, 1, 6, 8], rotor symmetry: 1, max scan energy: 50.77 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 13 7 8 6 F
D 1 6 8 7 F
D 6 1 2 4 F
pivots: [2, 4], dihedral: [1, 2, 4, 5], rotor symmetry: 1, max scan energy: 53.24 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 13 7 8 6 F
pivots: [6, 8], dihedral: [1, 6, 8, 3], rotor symmetry: 1, max scan energy: 27.10 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 13 7 8 6 F
D 2 1 6 8 F
pivots: [7, 8], dihedral: [11, 7, 8, 3], rotor symmetry: 3, max scan energy: 2.04 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.26299300   -0.58130200   -2.35813400
O      -2.69812500   -0.04438700   -3.62171200
O      -4.62089400   -0.52214300   -0.91515600
N      -3.84751700   -0.84826600   -4.22201200
N      -4.30543400   -1.72188000   -3.54850500
C      -2.46482300    0.41121700   -1.36727900
C      -4.19889900    1.59151200    0.12587100
C      -3.85988100    0.39944400   -0.73825600
H      -2.21613700    1.39929400   -1.76465000
H      -1.73974900    0.17516000   -0.57852200
H      -3.34863000    1.89868900    0.74163800
H      -5.05632900    1.35906200    0.75560400
H      -4.45197400    2.43840600   -0.52123100
H      -3.89303500   -1.77819900   -2.59471500
""",
)

