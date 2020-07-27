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

"""
entry(
    index = 0,
    label = "CH2NO_0",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {5,S}
2 N u1 p1 c0 {3,D}
3 C u0 p0 c0 {1,S} {2,D} {4,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {1,S}
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
Bond corrections: {'H-O': 1, 'C-O': 1, 'C=N': 1, 'C-H': 1}
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
            NASAPolynomial(coeffs=[3.848,0.0183428,2.67545e-05,-3.85882e-08,1.32149e-11,-47398.2,11.8869], Tmin=(10,'K'), Tmax=(1064.85,'K')),
            NASAPolynomial(coeffs=[4.07829,0.0342657,-1.93236e-05,5.06519e-09,-5.09788e-13,-48399,6.29223], Tmin=(1064.85,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-394.075,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (245.277,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'H-O': 1, 'C=O': 1, 'C-C': 2, 'C-O': 1}
1D rotors:
pivots: [1, 3], dihedral: [11, 1, 3, 5], rotor symmetry: 1, max scan energy: 29.88 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 9 4 5 2 F
pivots: [3, 5], dihedral: [1, 3, 5, 2], rotor symmetry: 1, max scan energy: 40.56 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 9 4 5 2 F
D 11 1 3 5 F
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
    index = 2,
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
Bond corrections: {'C-H': 1, 'H-O': 1, 'C=N': 1, 'O-O': 1, 'N-O': 1, 'C-O': 1}
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
    index = 3,
    label = "C2HN2O_3",
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
Bond corrections: {'C-H': 1, 'C=N': 1, 'C#N': 1, 'C-O': 2}
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
    index = 4,
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
    index = 5,
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
            NASAPolynomial(coeffs=[3.87026,0.0108573,0.000119142,-3.02471e-07,2.46937e-10,-42071.1,10.6044], Tmin=(10,'K'), Tmax=(313.347,'K')),
            NASAPolynomial(coeffs=[1.48042,0.0413647,-2.68988e-05,8.24117e-09,-9.62083e-13,-41921.4,19.3607], Tmin=(313.347,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-349.795,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (245.277,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 4, 'H-O': 2, 'C=C': 1, 'C-C': 1, 'C-O': 2}
1D rotors:
pivots: [1, 4], dihedral: [10, 1, 4, 3], rotor symmetry: 1, max scan energy: 37.84 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 11 2 5 4 F
pivots: [2, 5], dihedral: [11, 2, 5, 4], rotor symmetry: 1, max scan energy: 23.52 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 10 1 4 3 F
pivots: [3, 4], dihedral: [6, 3, 4, 1], rotor symmetry: 3, max scan energy: 10.23 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.30957400    1.97126900    1.52930600
O      -1.94194100    1.03322500   -0.98440700
C      -0.48606300    0.74495900    2.47074700
C      -1.27731000    1.11693400    1.26297600
C      -1.04768900    0.67063100    0.02479200
H      -1.12302300    0.24317200    3.20590200
H      -0.08011300    1.64183600    2.94858300
H       0.33899900    0.08014100    2.21114200
H      -0.25782700   -0.02805200   -0.22164400
H      -2.76326700    2.11887900    0.68670000
H      -1.44528600    1.37122000   -1.73612200
""",
)

entry(
    index = 6,
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
            NASAPolynomial(coeffs=[3.91659,0.00631637,0.000116499,-3.02796e-07,2.65896e-10,-32674.8,10.5986], Tmin=(10,'K'), Tmax=(287.738,'K')),
            NASAPolynomial(coeffs=[2.09263,0.0316749,-1.57114e-05,3.55846e-09,-3.06576e-13,-32569.9,17.1258], Tmin=(287.738,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-271.69,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (220.334,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 4, 'H-O': 1, 'C=C': 1, 'C-C': 1, 'C-O': 2}
1D rotors:
pivots: [1, 5], dihedral: [10, 1, 5, 4], rotor symmetry: 1, max scan energy: 70.29 kJ/mol
pivots: [3, 4], dihedral: [6, 3, 4, 2], rotor symmetry: 3, max scan energy: 2.37 kJ/mol
pivots: [4, 5], dihedral: [2, 4, 5, 1], rotor symmetry: 1, max scan energy: 123.51 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 4 5 1 9 F
D 7 3 4 2 F
D 10 1 5 4 F


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
    index = 7,
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
            NASAPolynomial(coeffs=[3.84244,0.00965457,0.000132949,-3.00509e-07,1.95405e-10,-11563.9,10.9928], Tmin=(10,'K'), Tmax=(540.848,'K')),
            NASAPolynomial(coeffs=[5.53665,0.0313174,-2.19619e-05,7.33184e-09,-9.22353e-13,-12247.2,-0.762751], Tmin=(540.848,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-96.2013,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (220.334,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 3, 'H-O': 2, 'C=C': 1, 'C-C': 1, 'C-O': 2}
1D rotors:
pivots: [1, 4], dihedral: [9, 1, 4, 3], rotor symmetry: 1, max scan energy: 21.89 kJ/mol
pivots: [2, 5], dihedral: [10, 2, 5, 4], rotor symmetry: 1, max scan energy: 35.45 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 1 4 5 2 F
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
    index = 8,
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
    index = 9,
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
            NASAPolynomial(coeffs=[3.67061,0.0349437,-0.000121392,2.89118e-07,-2.43185e-10,-16181.5,9.19403], Tmin=(10,'K'), Tmax=(405.826,'K')),
            NASAPolynomial(coeffs=[2.97037,0.0238964,-1.42159e-05,4.07152e-09,-4.51183e-13,-15976.8,13.7619], Tmin=(405.826,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-134.55,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (174.604,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 3, 'C=O': 2, 'C-C': 2}
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
    index = 10,
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
    index = 11,
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
    index = 12,
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
    index = 13,
    label = "C4H8N2O2_3",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {5,S}
2  O u0 p2 c0 {1,S} {3,S}
3  N u0 p1 c0 {2,S} {15,S} {16,S}
4  N u0 p1 c0 {8,T}
5  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
6  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
7  C u0 p0 c0 {5,S} {12,S} {13,S} {14,S}
8  C u0 p0 c0 {4,T} {5,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
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
    index = 14,
    label = "C3H7NO3_4",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {5,S}
2  O u0 p2 c0 {1,S} {4,S}
3  O u0 p2 c0 {7,D}
4  N u0 p1 c0 {2,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
6  C u0 p0 c0 {7,S} {10,S} {11,S} {12,S}
7  C u0 p0 c0 {3,D} {5,S} {6,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
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
    index = 15,
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
    index = 16,
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
    index = 17,
    label = "C3H6NO3_7",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {5,S}
2  O u0 p2 c0 {1,S} {4,S}
3  O u0 p2 c0 {7,D}
4  N u1 p1 c0 {2,S} {13,S}
5  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
6  C u0 p0 c0 {7,S} {10,S} {11,S} {12,S}
7  C u0 p0 c0 {3,D} {5,S} {6,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {4,S}
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
    index = 18,
    label = "C4H8N2O3_9",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {6,S}
2  O u0 p2 c0 {1,S} {4,S}
3  O u0 p2 c0 {4,S} {17,S}
4  N u0 p1 c0 {2,S} {3,S} {16,S}
5  N u0 p1 c0 {9,T}
6  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
7  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
8  C u0 p0 c0 {6,S} {13,S} {14,S} {15,S}
9  C u0 p0 c0 {5,T} {6,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {3,S}
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
    index = 19,
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
    index = 20,
    label = "C4H7N2O3_11",
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
            NASAPolynomial(coeffs=[3.24131,0.0709654,-0.000123801,2.534e-07,-2.07935e-10,10135,14.685], Tmin=(10,'K'), Tmax=(442.963,'K')),
            NASAPolynomial(coeffs=[0.0979409,0.0743402,-5.05373e-05,1.56759e-08,-1.83145e-12,10658.8,30.06], Tmin=(442.963,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (84.2442,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (361.68,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-N': 1, 'C-N': 1, 'C=O': 1, 'C-H': 6, 'C-C': 2, 'C-O': 1, 'C=N': 1, 'N-O': 1, 'O-O': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [6, 1, 2, 4], invalidation reason: The rotor scan has a barrier of 52.16 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
pivots: [1, 6], dihedral: [2, 1, 6, 8], rotor symmetry: 1, max scan energy: 59.50 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 12 7 8 6 F
D 11 6 8 7 F
D 6 1 2 4 F
pivots: [2, 4], dihedral: [1, 2, 4, 9], rotor symmetry: 1, max scan energy: 101.59 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 2 4 9 15 F
D 14 7 8 3 F
D 2 4 9 16 F
D 1 6 8 3 F
D 2 1 6 11 F
D 6 1 2 4 F
pivots: [4, 9], dihedral: [2, 4, 9, 5], rotor symmetry: 1, max scan energy: 38.22 kJ/mol
pivots: [6, 8], dihedral: [1, 6, 8, 3], rotor symmetry: 1, max scan energy: 48.56 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 2 1 6 8 F
D 12 7 8 6 F
D 6 1 2 4 F
pivots: [7, 8], dihedral: [12, 7, 8, 3], rotor symmetry: 3, max scan energy: 1.18 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.11542800    0.85181600    0.70342100
O      -0.95499400    2.08597700   -0.25302600
O       0.93298200   -0.05726300   -0.96877200
N      -1.24923300    1.72183000   -1.49779400
N      -3.05788500    0.87500500   -2.75613500
C       0.16000300    0.59642600    1.21486500
C       2.42559200   -0.56680800    0.82367000
C       1.15131000   -0.01496300    0.22188800
C      -2.61316600    1.53842500   -1.79019300
H       0.61467000    1.50181000    1.64468200
H       0.00501200   -0.10107200    2.04884800
H       2.80933600    0.07671300    1.61994600
H       3.17619000   -0.69048200    0.04441600
H       2.21597900   -1.54546400    1.26915300
H      -0.58894200    1.02950600   -1.85633000
H      -3.27523100    2.08617600   -1.11033600
""",
)

entry(
    index = 21,
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
    index = 22,
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
    index = 23,
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
    index = 24,
    label = "C4H5N2O3_16",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {8,S}
2  O u0 p2 c0 {7,S} {13,S}
3  O u0 p2 c0 {1,S} {4,S}
4  N u1 p1 c0 {3,S} {14,S}
5  N u0 p1 c0 {9,T}
6  C u0 p0 c0 {7,S} {10,S} {11,S} {12,S}
7  C u0 p0 c0 {2,S} {6,S} {8,D}
8  C u0 p0 c0 {1,S} {7,D} {9,S}
9  C u0 p0 c0 {5,T} {8,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
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
    index = 25,
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
    index = 26,
    label = "C4H4NO2_18",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {4,S}
2  O u1 p2 c0 {1,S}
3  N u0 p1 c0 {7,T}
4  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {4,S} {6,D} {7,S}
6  C u0 p0 c0 {5,D} {10,S} {11,S}
7  C u0 p0 c0 {3,T} {5,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
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
    index = 27,
    label = "C4H5NO2_19",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {12,S}
3  N u0 p1 c0 {7,T}
4  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {4,S} {6,D} {7,S}
6  C u0 p0 c0 {5,D} {10,S} {11,S}
7  C u0 p0 c0 {3,T} {5,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {2,S}
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
    index = 28,
    label = "C4H3N2O3_20",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {6,S}
2  O u0 p2 c0 {1,S} {8,S}
3  O u0 p2 c0 {7,D}
4  N u1 p1 c0 {8,D}
5  N u0 p1 c0 {9,T}
6  C u0 p0 c0 {1,S} {7,S} {10,S} {11,S}
7  C u0 p0 c0 {3,D} {6,S} {9,S}
8  C u0 p0 c0 {2,S} {4,D} {12,S}
9  C u0 p0 c0 {5,T} {7,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {8,S}
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
    index = 29,
    label = "C3H5O3_0",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {11,S}
3  O u0 p2 c0 {5,D}
4  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
5  C u0 p0 c0 {3,D} {4,S} {6,S}
6  C u1 p0 c0 {5,S} {9,S} {10,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {2,S}
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
    index = 30,
    label = "C4H6N2O2_2",
    molecule = 
"""
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {3,D}
3  N u0 p1 c0 {1,S} {2,D}
4  N u0 p1 c0 {8,T}
5  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
6  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
7  C u0 p0 c0 {5,S} {12,S} {13,S} {14,S}
8  C u0 p0 c0 {4,T} {5,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
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
    index = 31,
    label = "C4H5N2O2_3",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {3,D}
3  N u0 p1 c0 {1,S} {2,D}
4  N u0 p1 c0 {8,T}
5  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
6  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
7  C u1 p0 c0 {5,S} {12,S} {13,S}
8  C u0 p0 c0 {4,T} {5,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
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
    index = 32,
    label = "C3H5O2_4",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {10,S}
2  O u0 p2 c0 {4,D}
3  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
4  C u0 p0 c0 {2,D} {3,S} {5,S}
5  C u1 p0 c0 {4,S} {8,S} {9,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {1,S}
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
    index = 33,
    label = "C4H6N2O3_5",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {6,S}
2  O u0 p2 c0 {7,S} {15,S}
3  O u0 p2 c0 {4,D}
4  N u0 p1 c0 {1,S} {3,D}
5  N u0 p1 c0 {9,T}
6  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
7  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
8  C u0 p0 c0 {6,S} {12,S} {13,S} {14,S}
9  C u0 p0 c0 {5,T} {6,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {2,S}
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
    index = 34,
    label = "C3H2N2O2_6",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {5,S}
2 O u0 p2 c0 {3,D}
3 N u0 p1 c0 {1,S} {2,D}
4 N u0 p1 c0 {7,T}
5 C u0 p0 c0 {1,S} {6,D} {7,S}
6 C u0 p0 c0 {5,D} {8,S} {9,S}
7 C u0 p0 c0 {4,T} {5,S}
8 H u0 p0 c0 {6,S}
9 H u0 p0 c0 {6,S}
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
    index = 35,
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
    index = 36,
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
    index = 37,
    label = "C3H6NO3_10",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {5,S}
2  O u0 p2 c0 {1,S} {4,S}
3  O u0 p2 c0 {6,D}
4  N u0 p1 c0 {2,S} {12,S} {13,S}
5  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
6  C u0 p0 c0 {3,D} {5,S} {7,S}
7  C u1 p0 c0 {6,S} {10,S} {11,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {7,S}
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
    index = 38,
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
    index = 39,
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
    index = 40,
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
    index = 41,
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
    index = 42,
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
    index = 43,
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
    index = 44,
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
    index = 45,
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
    index = 46,
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
    index = 47,
    label = "C4H5NO2_21",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {12,S}
2  O u0 p2 c0 {6,D}
3  N u0 p1 c0 {7,T}
4  C u0 p0 c0 {6,S} {7,S} {8,S} {9,S}
5  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
6  C u0 p0 c0 {2,D} {4,S} {5,S}
7  C u0 p0 c0 {3,T} {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {1,S}
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
    index = 48,
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
    index = 49,
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
    index = 50,
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
    index = 51,
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
    index = 52,
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
    index = 53,
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
    index = 54,
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
    index = 55,
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
    index = 56,
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
    index = 57,
    label = "C4HN2O3_32",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {6,S} {9,S}
2  O u0 p2 c0 {7,S} {10,S}
3  O u1 p2 c0 {7,S}
4  N u0 p1 c0 {8,T}
5  N u0 p1 c0 {9,T}
6  C u0 p0 c0 {1,S} {7,D} {8,S}
7  C u0 p0 c0 {2,S} {3,S} {6,D}
8  C u0 p0 c0 {4,T} {6,S}
9  C u0 p0 c0 {1,S} {5,T}
10 H u0 p0 c0 {2,S}
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
    index = 58,
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
    index = 59,
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
    index = 60,
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
    index = 61,
    label = "C4H3N2O2_37",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {6,S} {7,S}
2  O u0 p2 c0 {6,D}
3  N u1 p1 c0 {7,D}
4  N u0 p1 c0 {8,T}
5  C u0 p0 c0 {6,S} {8,S} {9,S} {10,S}
6  C u0 p0 c0 {1,S} {2,D} {5,S}
7  C u0 p0 c0 {1,S} {3,D} {11,S}
8  C u0 p0 c0 {4,T} {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {7,S}
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
    index = 62,
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
    index = 63,
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
    index = 64,
    label = "C4H4NO2_40",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {6,S} {11,S}
2  O u1 p2 c0 {5,S}
3  N u0 p1 c0 {7,T}
4  C u0 p0 c0 {5,S} {7,S} {8,S} {9,S}
5  C u0 p0 c0 {2,S} {4,S} {6,D}
6  C u0 p0 c0 {1,S} {5,D} {10,S}
7  C u0 p0 c0 {3,T} {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {1,S}
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
    index = 65,
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
    index = 66,
    label = "C4H2NO2_42",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {5,D}
2 O u0 p2 c0 {7,D}
3 N u0 p1 c0 {6,T}
4 C u0 p0 c0 {5,S} {6,S} {8,S} {9,S}
5 C u0 p0 c0 {1,D} {4,S} {7,S}
6 C u0 p0 c0 {3,T} {4,S}
7 C u1 p0 c0 {2,D} {5,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
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
    index = 67,
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
    index = 68,
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
    index = 69,
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
    index = 70,
    label = "C4H4NO2_48",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {4,S} {11,S}
2  O u1 p2 c0 {6,S}
3  N u0 p1 c0 {7,T}
4  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {4,S} {6,D} {7,S}
6  C u0 p0 c0 {2,S} {5,D} {10,S}
7  C u0 p0 c0 {3,T} {5,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {1,S}
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
    index = 71,
    label = "C4H3NO2_49",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {10,S}
2  O u0 p2 c0 {6,D}
3  N u0 p1 c0 {7,T}
4  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {4,S} {6,D} {7,S}
6  C u0 p0 c0 {2,D} {5,D}
7  C u0 p0 c0 {3,T} {5,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {1,S}
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
    index = 72,
    label = "C3H7NO3_50",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {7,S}
2  O u0 p2 c0 {1,S} {4,S}
3  O u0 p2 c0 {6,S} {14,S}
4  N u0 p1 c0 {2,S} {12,S} {13,S}
5  C u0 p0 c0 {6,S} {8,S} {9,S} {10,S}
6  C u0 p0 c0 {3,S} {5,S} {7,D}
7  C u0 p0 c0 {1,S} {6,D} {11,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
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
    index = 73,
    label = "C3H2N2O2_51",
    molecule = 
"""
1 O u0 p3 c-1 {3,S}
2 O u0 p2 c0 {3,D}
3 N u0 p0 c+1 {1,S} {2,D} {5,S}
4 N u0 p1 c0 {7,T}
5 C u0 p0 c0 {3,S} {6,D} {7,S}
6 C u0 p0 c0 {5,D} {8,S} {9,S}
7 C u0 p0 c0 {4,T} {5,S}
8 H u0 p0 c0 {6,S}
9 H u0 p0 c0 {6,S}
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
    index = 74,
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
    index = 75,
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
    index = 76,
    label = "C4H3N2O3_54",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {8,S} {9,S}
2  O u0 p2 c0 {6,S} {12,S}
3  O u0 p2 c0 {7,D}
4  N u1 p1 c0 {8,D}
5  N u0 p1 c0 {9,T}
6  C u0 p0 c0 {2,S} {7,S} {10,S} {11,S}
7  C u0 p0 c0 {3,D} {6,S} {8,S}
8  C u0 p0 c0 {1,S} {4,D} {7,S}
9  C u0 p0 c0 {1,S} {5,T}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {2,S}
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
