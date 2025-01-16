#!/usr/bin/env python
# encoding: utf-8

name = "thermo_xmr_2081_1"
shortDesc = ""
longDesc = """
ARC v1.1.0
ARC project thermo_xmr_2081_1

Levels of theory used:

Conformer optimization:       wb97xd/def2svp, software: gaussian
Conformer single point:       None
TS guesses:       None
Optimization:     wb97xd/def2tzvp, software: gaussian (using a fine grid)
Frequencies:      wb97xd/def2tzvp, software: gaussian
Single point:     ccsd(t)-f12/cc-pvtz-f12, software: molpro
Rotor scans:      wb97xd/def2tzvp, software: gaussian
Using p-type bond additivity corrections for thermo

Using the following ESS settings: {'gaussian': ['local'], 'molpro': ['local'], 'orca': ['local']}

Considered the following species and TSs:
Species W5 (run time: 19:11:09)
Species W8 (Failed!) (run time: None)
Species W18 (run time: 22:15:25)
Species W20 (run time: 18:32:04)
Species W15 (run time: 1 day, 12:57:35)
Species CH2CHOH (run time: 1:17:45)
Species P22 (run time: 4:47:15)
Species P24 (run time: 4:18:08)
Species P18 (run time: 9:23:50)
Species P49 (run time: 1:41:18)
Species P51 (run time: 1:57:00)
Species INT19 (run time: 2 days, 6:25:30)
Species O1C[C]C=C1CO (run time: 1 day, 10:43:21)
Species OCC1=CC[C]O1 (run time: 9:01:43)
Species OCC1[C]C=CO1 (run time: 8:24:59)
Species OCC1[C]OC=C1 (run time: 8:39:26)
Species [O]C=CC=[C]CO (run time: 1 day, 3:58:28)

Overall time since project initiation: 1.0 days, 06:38:54
"""
entry(
    index = 0,
    label = "W5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {3,S} {9,S}
3  C u0 p0 c0 {2,S} {4,D} {11,S}
4  C u0 p0 c0 {3,D} {5,S} {10,S}
5  C u0 p0 c0 {4,S} {12,D} {13,S}
6  O u0 p2 c0 {1,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {5,D}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.37454,0.0613003,-0.000117544,2.20883e-07,-1.71113e-10,-21436.4,12.8243], Tmin=(10,'K'), Tmax=(423.363,'K')),
            NASAPolynomial(coeffs=[3.02217,0.0508966,-3.20264e-05,9.59995e-09,-1.10411e-12,-21283.5,15.675], Tmin=(423.363,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-178.248,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (320.107,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 6, 'C=O': 1, 'C-C': 3, 'C-O': 1, 'H-O': 1, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [1, 3], dihedral: [14, 1, 3, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [3, 4], dihedral: [1, 3, 4, 5], rotor symmetry: 1, max scan energy: 14.03 kJ/mol
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [6, 7], dihedral: [5, 6, 7, 2], rotor symmetry: 1, max scan energy: 51.78 kJ/mol
pivots: [5, 6], dihedral: [4, 5, 6, 7], rotor symmetry: 1, max scan energy: 60.14 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.44207200   -1.83994700   -0.61429400
O      -0.05914800    3.41769300   -3.25384100
C      -1.09777000   -1.79614900   -0.20838000
C      -0.34228700   -0.59064400   -0.66227700
C      -0.81871800    0.34672300   -1.53238400
C      -0.10093400    1.46789400   -1.94360900
C      -0.64805700    2.42657700   -2.87137500
H      -1.00460000   -1.88602100    0.88326600
H      -0.62431700   -2.69175200   -0.62463600
H       0.66280800   -0.48363200   -0.26435000
H       0.90167200    1.65426400   -1.57384700
H      -1.81744700    0.20588800   -1.93761300
H      -1.67343300    2.20703400   -3.23341500
H      -2.92707600   -1.15103900   -0.15633800
""",
)

entry(
    index = 1,
    label = "W18",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,D} {9,S}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  C u0 p0 c0 {2,D} {6,S} {11,S}
5  C u0 p0 c0 {3,D} {12,S} {13,S}
6  O u0 p2 c0 {4,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u1 p2 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.58033,0.0339343,1.79593e-05,-4.52666e-08,2.01173e-11,-23993.4,14.419], Tmin=(10,'K'), Tmax=(812.674,'K')),
            NASAPolynomial(coeffs=[2.44944,0.0493658,-2.87321e-05,7.9733e-09,-8.55782e-13,-24135.3,17.636], Tmin=(812.674,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-199.54,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (324.264,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 6, 'C-C': 2, 'C-O': 2, 'H-O': 1, 'C=C': 2}
1D rotors:
pivots: [1, 6], dihedral: [14, 1, 6, 4], rotor symmetry: 1, max scan energy: 65.75 kJ/mol
pivots: [3, 4], dihedral: [5, 3, 4, 2], rotor symmetry: 1, max scan energy: 5.27 kJ/mol
* Invalidated! pivots: [3, 5], dihedral: [4, 3, 5, 7], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 6], dihedral: [2, 4, 6, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       3.22151000   -0.78259200    1.06420700
O       1.00588500   -1.99454200    1.74265100
C      -0.20749000   -1.43362000   -0.26084300
C       1.00711900   -1.43637600    0.63876000
C      -1.32577100   -0.63819200    0.34886700
C       2.19569500   -0.76500500    0.23482800
C      -1.93186200    0.37775400   -0.24298500
H      -0.52051800   -2.47550600   -0.37661200
H       0.04367200   -1.04238700   -1.24886700
H      -1.62102900   -0.94297000    1.34791300
H       2.34205600   -0.23288800   -0.69362400
H      -1.65335000    0.70533600   -1.23893900
H      -2.73309600    0.91719600    0.24573400
H       2.90744900   -1.29331800    1.83689100
""",
)

entry(
    index = 2,
    label = "W20",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {9,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  C u0 p0 c0 {2,D} {6,S} {11,S}
5  C u0 p0 c0 {3,D} {7,S} {12,S}
6  O u0 p2 c0 {4,S} {13,S}
7  O u0 p2 c0 {5,S} {14,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.66031,0.0278753,0.000187679,-6.19526e-07,5.75788e-10,-21310.9,11.2359], Tmin=(10,'K'), Tmax=(376.89,'K')),
            NASAPolynomial(coeffs=[4.86474,0.049181,-3.27865e-05,1.04308e-08,-1.26302e-12,-21643.7,3.38863], Tmin=(376.89,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-177.165,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (320.107,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 2, 'C-O': 2, 'H-O': 2, 'C=C': 2}
1D rotors:
pivots: [1, 6], dihedral: [13, 1, 6, 4], rotor symmetry: 1, max scan energy: 19.27 kJ/mol
pivots: [2, 7], dihedral: [14, 2, 7, 5], rotor symmetry: 1, max scan energy: 17.14 kJ/mol
pivots: [3, 4], dihedral: [5, 3, 4, 6], rotor symmetry: 2, max scan energy: 43.32 kJ/mol
* Invalidated! pivots: [3, 5], dihedral: [4, 3, 5, 7], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 6], dihedral: [3, 4, 6, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
O      -0.27267100   -5.43932200   -0.55868900
O      -2.98307800    0.59968700    0.20634700
C      -1.59990600   -2.06710100    0.23407300
C      -0.91683000   -3.29762000    0.33488700
C      -1.59061400   -1.08576500    1.24100300
C      -0.91573000   -4.25250900   -0.62500200
C      -2.22269800    0.11755800    1.21286900
H      -0.35486900   -3.48541600    1.24854900
H      -2.15571400   -1.89659000   -0.68492700
H      -1.02501800   -1.29244200    2.14277400
H      -1.44984200   -4.14012400   -1.55998800
H      -2.16222100    0.81599100    2.03522600
H       0.19124100   -5.51135300    0.27918300
H      -3.02216700   -0.03656300   -0.51138700
""",
)

entry(
    index = 3,
    label = "W15",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,D} {10,S}
3  C u0 p0 c0 {1,S} {5,D} {9,S}
4  C u0 p0 c0 {2,D} {6,S} {11,S}
5  C u0 p0 c0 {3,D} {12,S} {13,S}
6  O u0 p2 c0 {4,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 O u1 p2 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74431,0.0233324,7.02719e-05,-1.31838e-07,6.711e-11,-20179.8,12.5308], Tmin=(10,'K'), Tmax=(656.357,'K')),
            NASAPolynomial(coeffs=[1.86009,0.0512026,-3.08717e-05,8.93337e-09,-9.97111e-13,-20285.5,18.1387], Tmin=(656.357,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-167.816,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 6, 'C-C': 2, 'C-O': 2, 'H-O': 1, 'C=C': 2}
1D rotors:
* Invalidated! pivots: [1, 6], dihedral: [14, 1, 6, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 4], dihedral: [5, 3, 4, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 5], dihedral: [4, 3, 5, 7], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [5, 7], dihedral: [3, 5, 7, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.31870800    1.53213400   -1.02732600
O       1.15253900    1.72147400    0.12895600
C       0.41626800   -0.91870900   -0.80650600
C      -1.08420200   -0.82314200   -0.64001500
C       1.05181600   -0.58701800    0.49539900
C      -1.78409800    0.30863300   -0.76971900
C       1.39653400    0.74494000    0.84312300
H       0.68693500   -1.92738400   -1.11699600
H       0.75743700   -0.22481200   -1.57781100
H       1.20476600   -1.36541300    1.23386100
H      -1.62882400   -1.72353300   -0.39158700
H      -2.86596200    0.29289900   -0.69430200
H       1.91824800    0.89484400    1.80053800
H      -0.36482700    1.60528800   -0.82246500
""",
)

entry(
    index = 4,
    label = "CH2CHOH",
    molecule = 
"""
multiplicity 3
1 O u0 p2 c0 {2,S} {7,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 C u1 p0 c0 {2,S} {5,S} {6,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94642,0.003205,6.71384e-05,-1.33204e-07,8.0346e-11,16693.5,8.32737], Tmin=(10,'K'), Tmax=(548.201,'K')),
            NASAPolynomial(coeffs=[3.25067,0.020328,-1.26754e-05,3.94136e-09,-4.77512e-13,16588.8,9.61482], Tmin=(548.201,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (138.778,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 3, 'C-C': 1, 'C-O': 1, 'H-O': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [7, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       0.93218500   -0.95348900    0.21412200
C       0.47897600    0.29918700   -0.10798900
C       0.95215900    1.45184400    0.63702200
H      -0.51072600    0.26460900   -0.54721400
H       0.54015800    1.71071900    1.61129700
H       1.71977500    2.10903800    0.24079200
H       1.75847800   -0.86883600    0.69660300
""",
)

entry(
    index = 5,
    label = "P22",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {4,S} {11,S}
4  C u0 p0 c0 {3,S} {5,S} {10,D}
5  C u0 p0 c0 {4,S} {12,D} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {4,D}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {5,D}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.40269,0.0585893,-0.000134242,2.77575e-07,-2.22302e-10,-28882.3,11.6086], Tmin=(10,'K'), Tmax=(421.417,'K')),
            NASAPolynomial(coeffs=[2.54638,0.0481288,-3.08442e-05,9.33558e-09,-1.07883e-12,-28645.1,16.9582], Tmin=(421.417,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-240.156,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (295.164,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 6, 'C=O': 2, 'C-C': 3, 'C=C': 1}
1D rotors:
pivots: [3, 4], dihedral: [8, 3, 4, 5], rotor symmetry: 3, max scan energy: 7.35 kJ/mol
pivots: [5, 6], dihedral: [4, 5, 6, 1], rotor symmetry: 1, max scan energy: 33.41 kJ/mol
pivots: [6, 7], dihedral: [1, 6, 7, 2], rotor symmetry: 1, max scan energy: 24.88 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O       1.70523700   -0.04714700   -1.54057400
O       1.97942600   -3.16778300   -0.11032300
C      -2.26460800   -0.10070300    0.24515800
C      -0.90603500   -0.09879300   -0.35779500
C      -0.01958600   -1.08769900   -0.25885800
C       1.30057500   -0.98588100   -0.89447100
C       2.25275900   -2.17754200   -0.72384300
H      -2.37682600    0.74749200    0.92547900
H      -2.46815100   -1.02035100    0.79264300
H      -3.02286800    0.02252600   -0.53248000
H      -0.61612400    0.78255500   -0.92451000
H      -0.23398100   -1.99768100    0.28863300
H       3.22603300   -2.02769100   -1.22963100
""",
)

entry(
    index = 6,
    label = "P24",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,D} {9,S}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  C u0 p0 c0 {2,D} {6,S} {11,S}
5  C u0 p0 c0 {3,D} {12,D}
6  O u0 p2 c0 {4,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 O u0 p2 c0 {5,D}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67084,0.0333225,0.000216162,-1.15033e-06,1.66399e-09,-22416.3,12.3839], Tmin=(10,'K'), Tmax=(251.295,'K')),
            NASAPolynomial(coeffs=[5.20555,0.0414222,-2.63512e-05,8.15056e-09,-9.71371e-13,-22596.2,5.05588], Tmin=(251.295,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-186.349,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (295.164,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C=O': 1, 'C-C': 2, 'C-O': 1, 'H-O': 1, 'C=C': 2}
1D rotors:
pivots: [1, 6], dihedral: [13, 1, 6, 4], rotor symmetry: 1, max scan energy: 19.96 kJ/mol
pivots: [3, 4], dihedral: [5, 3, 4, 6], rotor symmetry: 1, max scan energy: 13.37 kJ/mol
pivots: [3, 5], dihedral: [4, 3, 5, 7], rotor symmetry: 1, max scan energy: 8.68 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       3.20932100    1.17573100   -1.80775800
O      -3.04616800   -0.47244800    0.53876900
C      -0.28234900   -0.23967400   -1.63843800
C       1.08628100    0.22166400   -1.23190500
C      -1.38532600    0.55297300   -0.96824200
C       1.96196400    0.73154900   -2.08778300
C      -2.26760500    0.01406000   -0.16804500
H      -0.38614900   -0.15775400   -2.72381300
H      -0.40783900   -1.29853200   -1.39852500
H       1.34085800    0.14013600   -0.17794000
H      -1.45793900    1.62190100   -1.11868200
H       1.74020300    0.83988400   -3.14355700
H       3.38618200    1.06840500   -0.86990900
""",
)

entry(
    index = 7,
    label = "P18",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,D}
3  C u0 p0 c0 {1,S} {5,D} {9,S}
4  C u0 p0 c0 {2,S} {10,D} {11,S}
5  C u0 p0 c0 {3,D} {12,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {2,D}
9  H u0 p0 c0 {3,S}
10 O u0 p2 c0 {4,D}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81616,0.0397159,-1.34687e-05,-4.67889e-09,2.82799e-12,-26510.8,12.5482], Tmin=(10,'K'), Tmax=(1275.93,'K')),
            NASAPolynomial(coeffs=[13.3737,0.0235032,-1.05733e-05,2.25411e-09,-1.85265e-13,-30069,-40.2764], Tmin=(1275.93,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-220.379,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 6, 'C=O': 2, 'C-C': 3, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [3, 4], dihedral: [5, 3, 4, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [3, 5], dihedral: [4, 3, 5, 7], rotor symmetry: 1, max scan energy: 9.86 kJ/mol
pivots: [4, 6], dihedral: [1, 4, 6, 2], rotor symmetry: 1, max scan energy: 23.61 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.09187500    2.05015100    0.42446400
O      -2.63288000    0.44143200    2.09297800
C      -0.18494300   -0.33662300    0.75522400
C      -0.65543400    1.08850200    0.87433600
C       1.16981600   -0.47466700    0.14042400
C      -1.98002900    1.32282500    1.61621300
C       2.15763300   -1.17107500    0.67701300
H      -0.23738600   -0.80257700    1.74261400
H      -0.94446300   -0.85783900    0.15781600
H       1.32227600    0.03978300   -0.80225200
H      -2.27049100    2.39001700    1.66353600
H       2.04199100   -1.68756600    1.62384000
H       3.12042300   -1.24985500    0.18884100
""",
)

entry(
    index = 8,
    label = "P49",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {4,S} {6,S}
2  O u0 p2 c0 {4,S} {11,S}
3  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
4  C u1 p0 c0 {1,S} {2,S} {3,S}
5  C u0 p0 c0 {3,S} {6,D} {9,S}
6  C u0 p0 c0 {1,S} {5,D} {10,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90425,0.00561141,0.000125881,-2.41218e-07,1.4017e-10,-13999.3,11.1444], Tmin=(10,'K'), Tmax=(563.667,'K')),
            NASAPolynomial(coeffs=[1.89696,0.04159,-2.77004e-05,8.83358e-09,-1.07421e-12,-14118.3,16.615], Tmin=(563.667,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-116.436,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (253.591,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 4, 'C-C': 2, 'C-O': 3, 'H-O': 1, 'C=C': 1}
1D rotors:
pivots: [2, 4], dihedral: [11, 2, 4, 1], rotor symmetry: 1, max scan energy: 13.00 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       0.71868700    1.18004300    0.19269700
O       2.07899500   -0.68394000    0.15532100
C      -0.35719700   -0.92660500    0.15251100
C       0.88444800   -0.16268900    0.52213400
C      -1.27886000    0.20440800   -0.21325400
C      -0.59192000    1.33604500   -0.16886900
H      -0.72895400   -1.53688400    0.97946200
H      -0.16235700   -1.60674000   -0.68784500
H      -2.31838500    0.10998400   -0.47976200
H      -0.89467600    2.35330200   -0.36159800
H       2.77793800   -0.07838700    0.41469900
""",
)

entry(
    index = 9,
    label = "P51",
    molecule = 
"""
1  O u0 p2 c0 {5,D}
2  O u0 p2 c0 {6,D}
3  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {3,S} {6,D} {9,S}
5  C u0 p0 c0 {1,D} {3,S} {10,S}
6  C u0 p0 c0 {2,D} {4,D}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.5675,0.0451057,-0.000128888,2.9681e-07,-2.52212e-10,-23085.9,12.0327], Tmin=(10,'K'), Tmax=(397.929,'K')),
            NASAPolynomial(coeffs=[2.96136,0.0338277,-2.08955e-05,6.1837e-09,-7.04278e-13,-22900.1,16.1266], Tmin=(397.929,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-191.959,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (228.648,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 4, 'C=O': 2, 'C-C': 2, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [3, 4], dihedral: [5, 3, 4, 6], invalidation reason: Another conformer for P51 exists which is 4.23 kJ/mol lower.Another conformer for P51 exists which is 4.23 kJ/mol lower.
pivots: [3, 5], dihedral: [4, 3, 5, 1], rotor symmetry: 1, max scan energy: 10.85 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.31746100    1.70376900    0.63500700
O       2.93973100   -0.66103900   -1.03385800
C      -0.43001500   -0.42429800   -0.04768600
C       0.95159800    0.10145100    0.20563800
C      -1.50448200    0.60428400    0.19991800
C       2.00605400   -0.30278700   -0.45160000
H      -0.68138200   -1.27493600    0.60131500
H      -0.55671100   -0.79287500   -1.06982600
H       1.10285500    0.87642200    0.94564100
H      -2.53035000    0.25199500   -0.03223300
""",
)

entry(
    index = 10,
    label = "INT19",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {4,S} {14,S}
2  O u0 p2 c0 {5,S} {15,S}
3  O u1 p2 c0 {8,S}
4  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
5  C u0 p0 c0 {2,S} {4,S} {6,D}
6  C u0 p0 c0 {5,D} {7,S} {12,S}
7  C u0 p0 c0 {6,S} {8,D} {11,S}
8  C u0 p0 c0 {3,S} {7,D} {13,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.66903,0.0372387,2.1442e-05,-5.18877e-08,2.22998e-11,-49269.8,13.4011], Tmin=(10,'K'), Tmax=(890.346,'K')),
            NASAPolynomial(coeffs=[5.37843,0.0477609,-2.69507e-05,7.30895e-09,-7.69375e-13,-50295.7,1.30122], Tmin=(890.346,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-409.639,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (357.522,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 2, 'C-O': 3, 'H-O': 2, 'C=C': 2}
1D rotors:
* Invalidated! pivots: [1, 4], dihedral: [14, 1, 4, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 5], dihedral: [15, 2, 5, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 5], dihedral: [1, 4, 5, 2], invalidation reason: Inconsistent initial and final conformers But unable to propose troubleshooting methods.Inconsistent initial and final conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [6, 7], dihedral: [5, 6, 7, 8], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [7, 8], dihedral: [6, 7, 8, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [5, 6], dihedral: [2, 5, 6, 7], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.75712900   -0.38696800   -0.68282200
O      -1.49632900   -0.81488700    1.65425400
O      -0.84568000   -1.89434100    3.80322300
C      -1.68610100   -1.28842700   -0.63117000
C      -1.39221700   -1.76496700    0.76671300
C      -1.00878700   -3.07063000    1.02014300
C      -0.63602300   -3.66551500    2.23039200
C      -0.57435200   -3.07385600    3.51622300
H      -1.93425300   -2.13291500   -1.27297300
H      -0.76322300   -0.83223700   -1.02229900
H      -0.36586100   -4.71384700    2.19476300
H      -1.00000300   -3.71392500    0.14867700
H      -0.25508800   -3.73594800    4.33208700
H      -2.65129100    0.23667700    0.04067500
H      -1.25573300   -1.16326600    2.59223300
""",
)

entry(
    index = 11,
    label = "O1C[C]C=C1CO",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {5,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,D} {5,S}
4  C u0 p0 c0 {3,D} {6,S} {12,S}
5  O u0 p2 c0 {2,S} {3,S}
6  C u2 p0 c0 {2,S} {4,S}
7  O u0 p2 c0 {1,S} {13,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72838,0.0311642,1.71004e-05,-4.21573e-08,1.80754e-11,11389.8,12.5975], Tmin=(10,'K'), Tmax=(897.442,'K')),
            NASAPolynomial(coeffs=[5.32509,0.0393467,-2.21474e-05,5.99378e-09,-6.29728e-13,10487.2,1.63456], Tmin=(897.442,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (94.7145,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 3, 'C-O': 3, 'H-O': 1, 'C=C': 1}
1D rotors:
pivots: [2, 3], dihedral: [13, 2, 3, 5], rotor symmetry: 1, max scan energy: 12.32 kJ/mol
* Invalidated! pivots: [3, 5], dihedral: [2, 3, 5, 1], invalidation reason: Inconsistent initial and final conformers But unable to propose troubleshooting methods.Inconsistent initial and final conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.48986200    1.09016800    0.45784300
O       2.14329200    0.63473200   -0.83357800
C       1.67959300    0.04285800    0.36777600
C      -1.90110600    0.79498400    0.47141700
C       0.20446200   -0.08945600    0.42040000
C      -0.63205300   -1.18641800    0.41640500
C      -1.91251900   -0.69156200    0.46119000
H       2.02556100    0.62039400    1.23567200
H       2.12873400   -0.94807500    0.42131100
H      -2.34308000    1.24271900    1.36761600
H      -2.36334300    1.25180100   -0.41048700
H      -0.30938200   -2.21442500    0.38407400
H       1.72026300    1.49104800   -0.92277500
""",
)

entry(
    index = 12,
    label = "OCC1=CC[C]O1",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,D} {6,S}
4  C u0 p0 c0 {2,S} {3,D} {12,S}
5  C u2 p0 c0 {2,S} {6,S}
6  O u0 p2 c0 {3,S} {5,S}
7  O u0 p2 c0 {1,S} {13,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80995,0.0215832,5.96276e-05,-1.04063e-07,4.8025e-11,16951.7,12.5485], Tmin=(10,'K'), Tmax=(748.114,'K')),
            NASAPolynomial(coeffs=[2.92436,0.0455988,-2.71832e-05,7.74581e-09,-8.50911e-13,16544.6,12.9579], Tmin=(748.114,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (140.944,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 3, 'C-O': 3, 'H-O': 1, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [13, 2, 3, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 5], dihedral: [2, 3, 5, 1], invalidation reason: Another conformer for OCC1=CC[C]O1 exists which is 1.03 kJ/mol lower.Another conformer for OCC1=CC[C]O1 exists which is 1.03 kJ/mol lower.


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.45831100   -1.18475800   -0.06465700
O       2.41443200    1.05430200   -0.10608000
C       1.73832300   -0.17130500   -0.00324100
C      -1.88251000    0.52741200   -0.94060200
C       0.28565000   -0.05292800   -0.32490100
C      -0.43522000    0.95053200   -0.81413700
C      -1.72777900   -0.86891600   -0.42962600
H       2.21351700   -0.85275500   -0.71205200
H       1.84181400   -0.62055600    0.99254400
H      -2.56356500    1.13863200   -0.33469600
H      -2.24873500    0.57102300   -1.97404400
H      -0.04420900    1.91139800   -1.10642100
H       2.04001100    1.66277600    0.53393500
""",
)

entry(
    index = 13,
    label = "OCC1[C]C=CO1",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {5,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {7,S} {9,S} {10,S}
3  C u1 p0 c0 {4,S} {5,S} {12,S}
4  C u0 p0 c0 {3,S} {6,D} {11,S}
5  O u0 p2 c0 {1,S} {3,S}
6  C u1 p0 c0 {1,S} {4,D}
7  O u0 p2 c0 {2,S} {13,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85619,0.00876272,0.000167463,-3.47496e-07,2.16724e-10,11062.3,12.9407], Tmin=(10,'K'), Tmax=(535.369,'K')),
            NASAPolynomial(coeffs=[2.68512,0.0487701,-3.22079e-05,1.01995e-08,-1.23374e-12,10739.8,13.6751], Tmin=(535.369,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (91.927,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 3, 'C-O': 3, 'H-O': 1, 'C=C': 1}
1D rotors:
pivots: [2, 4], dihedral: [13, 2, 4, 3], rotor symmetry: 1, max scan energy: 14.16 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [1, 3, 4, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       0.31035300   -0.88064500    0.86598300
O      -2.44782600   -0.57083600    0.12584300
C      -0.31181200    0.42447600    0.71082600
C      -1.43784600    0.30365500   -0.30792200
C       1.62160600   -0.77531900    0.51757300
C       1.98322300    0.50479400    0.16333400
C       0.84234200    1.26312200    0.28775700
H      -0.73446100    0.69975200    1.68341300
H      -1.01016300   -0.01026500   -1.26804500
H      -1.89735700    1.28387200   -0.44282600
H       2.96895000    0.81799600   -0.13945500
H       2.19829400   -1.68394300    0.56996600
H      -2.04933900   -1.43196700    0.27027300
""",
)

entry(
    index = 14,
    label = "OCC1[C]OC=C1",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {7,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {3,D} {6,S} {12,S}
5  C u2 p0 c0 {1,S} {6,S}
6  O u0 p2 c0 {4,S} {5,S}
7  O u0 p2 c0 {2,S} {13,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78958,0.0242108,4.89027e-05,-8.92406e-08,4.08297e-11,17711.4,12.6321], Tmin=(10,'K'), Tmax=(771.915,'K')),
            NASAPolynomial(coeffs=[3.69937,0.0437122,-2.598e-05,7.3761e-09,-8.07263e-13,17158.3,9.37087], Tmin=(771.915,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (147.265,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 3, 'C-O': 3, 'H-O': 1, 'C=C': 1}
1D rotors:
pivots: [2, 4], dihedral: [13, 2, 4, 3], rotor symmetry: 1, max scan energy: 12.69 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [5, 3, 4, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.06545300   -2.72105100    2.61363300
O      -1.81623400   -1.57158500   -0.36683100
C      -0.82803600   -0.64304700    1.68480600
C      -1.33944300   -0.40815400    0.25395000
C      -1.82494500   -1.29685800    2.61919600
C      -1.33288000   -2.43733200    3.08063600
C       0.24372100   -1.69021800    1.79780900
H      -0.49047400    0.33136900    2.06730100
H      -0.53554500    0.05748100   -0.32981100
H      -2.17567800    0.29290700    0.28714100
H      -2.79938300   -0.89480200    2.84573200
H      -1.74446100   -3.17626600    3.74874800
H      -1.12963900   -2.24171400   -0.30790400
""",
)

entry(
    index = 15,
    label = "C5H6O2[635]",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {3,S} {12,D}
5  C u0 p1 c0 {2,S} {3,S}
6  O u0 p2 c0 {1,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86485,0.00826361,0.000170471,-3.49922e-07,2.17396e-10,2083.05,11.8101], Tmin=(10,'K'), Tmax=(529.807,'K')),
            NASAPolynomial(coeffs=[1.88155,0.0520216,-3.49123e-05,1.10615e-08,-1.32902e-12,1889.22,16.306], Tmin=(529.807,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (17.273,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'H-O': 1, 'C=O': 1, 'C-H': 5, 'C-C': 5}
1D rotors:
pivots: [1, 3], dihedral: [13, 1, 3, 4], rotor symmetry: 1, max scan energy: 23.84 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.72974400    1.03644300    0.65592500
O       0.95306700    1.81253400    0.73614400
C      -0.80119800    0.43881500   -0.19516700
C      -0.72627200   -1.08290400   -0.09788900
C       1.49832800   -0.34487000   -0.30183400
C       0.63647600    0.82360700    0.13821500
C       0.66487100   -1.57239000   -0.29171800
H      -0.98136300    0.73204200   -1.24212000
H      -0.86916400   -1.37704000    0.96025700
H      -1.48012300   -1.64933200   -0.64414700
H       2.48847300   -0.41530500    0.14654600
H       1.66958100   -0.24166500   -1.39085600
H      -1.32295100    1.84003700    1.00140100
""",
)

entry(
    index = 16,
    label = "C5H5O[1522]",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {4,D}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u1 p0 c0 {2,S} {5,S} {10,S}
4  C u0 p0 c0 {1,D} {6,S} {11,S}
5  C u0 p0 c0 {3,S} {6,T}
6  C u0 p0 c0 {4,S} {5,T}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.48716,0.0547211,-0.000196419,4.73316e-07,-4.01422e-10,21130.3,15.9091], Tmin=(10,'K'), Tmax=(402.32,'K')),
            NASAPolynomial(coeffs=[2.40417,0.0367014,-2.19057e-05,6.28824e-09,-6.97901e-13,21450.5,23.0432], Tmin=(402.32,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (175.671,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (249.434,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C=O': 1, 'C-C': 3, 'C#C': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [7, 2, 3, 5], invalidation reason: 
pivots: [3, 5], dihedral: [2, 3, 5, 6], rotor symmetry: 1, max scan energy: 0.06 kJ/mol (set as a FreeRotor)
pivots: [4, 6], dihedral: [1, 4, 6, 5], rotor symmetry: 1, max scan energy: 0.07 kJ/mol (set as a FreeRotor)


External symmetry: 1, optical isomers: 1

Geometry:
O      -1.06196700   -2.68684400    4.57110100
C      -2.24107100   -0.03661200   -0.12823100
C      -0.88631800   -0.19081300    0.47132200
C      -0.20623200   -2.15276900    3.90133100
C      -0.64852400   -0.85313300    1.63131200
C      -0.46434900   -1.45770300    2.68181900
H      -2.49209100    1.02274900   -0.23537200
H      -2.26441800   -0.46805000   -1.13324600
H      -3.00486600   -0.51871800    0.47856600
H      -0.04130800    0.25022100   -0.04668700
H       0.85473700   -2.17435100    4.20619300
""",
)

entry(
    index = 17,
    label = "C5H4O[1515]",
    molecule = 
"""
1  O u0 p2 c0 {4,D}
2  C u0 p0 c0 {3,D} {5,S} {7,S}
3  C u0 p0 c0 {2,D} {8,S} {9,S}
4  C u0 p0 c0 {1,D} {6,S} {10,S}
5  C u0 p0 c0 {2,S} {6,T}
6  C u0 p0 c0 {4,S} {5,T}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78797,0.0270859,-7.35095e-06,-4.77176e-09,2.40882e-12,18494.8,12.39], Tmin=(10,'K'), Tmax=(1210.91,'K')),
            NASAPolynomial(coeffs=[8.0179,0.0212722,-1.02563e-05,2.39208e-09,-2.18977e-13,16872.2,-11.2965], Tmin=(1210.91,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (153.781,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (228.648,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'C-H': 4, 'C=O': 1, 'C-C': 2, 'C#C': 1}
1D rotors:
* Invalidated! pivots: [2, 5], dihedral: [3, 2, 5, 6], invalidation reason: not a torsional mode (angles = 122.89, 179.85 degrees)
pivots: [4, 6], dihedral: [1, 4, 6, 5], rotor symmetry: 1, max scan energy: 0.06 kJ/mol (set as a FreeRotor)


External symmetry: 1, optical isomers: 1

Geometry:
O       3.11881800   -0.64400100    1.19159400
C      -1.30672600    0.28675800   -0.59089000
C      -2.23575700   -0.48133100   -0.02869300
C       2.64056900    0.09864000    0.37503800
C       0.07022700    0.21170900   -0.24477800
C       1.23572400    0.14590600    0.05039500
H      -1.57813300    1.01230400   -1.34988900
H      -1.98124900   -1.21009200    0.73008000
H      -3.27468800   -0.39519100   -0.31852000
H       3.26655800    0.81032500   -0.19236600
""",
)

entry(
    index = 18,
    label = "C5H6O2[601]",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {5,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,D} {6,S}
4  C u0 p0 c0 {3,D} {7,S} {12,S}
5  C u0 p1 c0 {1,S} {2,S}
6  O u0 p2 c0 {2,S} {3,S}
7  O u0 p2 c0 {4,S} {13,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87836,0.00807839,0.000177081,-3.92994e-07,2.70481e-10,9743.25,12.0006], Tmin=(10,'K'), Tmax=(463.7,'K')),
            NASAPolynomial(coeffs=[1.34798,0.0515387,-3.34848e-05,1.03479e-08,-1.21973e-12,9745.35,19.7558], Tmin=(463.7,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (80.9891,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 3, 'H-O': 1, 'C=C': 1, 'C-H': 5, 'C-C': 3}
1D rotors:
* Invalidated! pivots: [2, 6], dihedral: [13, 2, 6, 5], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.08192600   -0.83110600   -0.71581100
O       2.44926300   -1.18511400    0.45773000
C      -0.50949200    1.21617400    0.30079900
C      -1.49179400   -0.56414200   -0.75507800
C       0.47305700    0.09605400    0.13757100
C       1.66956000   -0.09357300    0.67360600
C      -1.82448400    0.72562000   -0.14871700
H      -0.37306200    1.98859400   -0.48822000
H      -0.50313400    1.76827300    1.23904000
H      -1.86771800   -0.68354000   -1.77354100
H      -2.03734800   -1.29155400   -0.12691500
H       2.12186800    0.63792400    1.32651900
H       1.97520200   -1.78362200   -0.12695100
""",
)


