#!/usr/bin/env python
# encoding: utf-8

name = "2FFOH_thermo_1"
shortDesc = ""
longDesc = """
ARC v1.1.0
ARC projects 2FFOH_thermo_1, 2FFOH_thermo_2

Levels of theory used:

Conformers:       wb97xd/def2svp, software: gaussian (dft)
TS guesses:       None
Composite method: cbs-qb3, software: gaussian (composite) (using a fine grid)
Frequencies:      b3lyp/cbsb7, software: gaussian (dft)
Rotor scans:      b3lyp/cbsb7, software: gaussian (dft)
Using p-type bond additivity corrections for thermo

Using the following ESS settings: {'gaussian': ['local'], 'molpro': ['local']}
"""
entry(
    index = 0,
    label = "2FFOH",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {7,S}
2  O u0 p2 c0 {3,S} {13,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  C u0 p0 c0 {1,S} {3,S} {5,D}
5  C u0 p0 c0 {4,D} {6,S} {10,S}
6  C u0 p0 c0 {5,S} {7,D} {11,S}
7  C u0 p0 c0 {1,S} {6,D} {12,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89525,0.0262426,2.45489e-05,-4.41978e-08,1.6863e-11,-29000.2,12.0103], Tmin=(10,'K'), Tmax=(992.718,'K')),
            NASAPolynomial(coeffs=[6.3913,0.0356842,-1.91804e-05,4.95507e-09,-4.98206e-13,-30456.6,-4.85274], Tmin=(992.718,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-241.05,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'H-O': 1, 'C-C': 2, 'C-O': 3, 'C=C': 2}
1D rotors:
pivots: [1, 2], dihedral: [8, 1, 2, 3], rotor symmetry: 1, max scan energy: 11.99 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 11.89 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.42037200   -0.23374800    0.84285200
C      -1.70232700    0.31735300   -0.26210700
C      -0.22612900    0.15937300   -0.14720200
C       0.80833100    1.01197700    0.08290800
C       2.00051200    0.21593700    0.11106800
C       1.60344600   -1.06466000   -0.09752500
O       0.25076400   -1.12210400   -0.26140900
H      -2.19263100   -1.16786700    0.89193400
H      -2.04806800   -0.12666000   -1.20618300
H      -1.94246300    1.38079700   -0.28386800
H       0.73242600    2.07896800    0.22070600
H       3.01195300    0.55561500    0.26729200
H       2.12455900   -2.00497700   -0.15846300
""",
)

entry(
    index = 1,
    label = "P1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {6,S}
3  C u0 p0 c0 {2,D} {4,S} {10,S}
4  C u0 p0 c0 {3,S} {5,D} {11,S}
5  C u0 p0 c0 {4,D} {6,S} {12,S}
6  O u0 p2 c0 {2,S} {5,S}
7  O u1 p2 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79796,0.0234305,3.97656e-05,-7.43134e-08,3.36418e-11,-1420.56,11.3884], Tmin=(10,'K'), Tmax=(789.675,'K')),
            NASAPolynomial(coeffs=[4.03631,0.0394457,-2.33703e-05,6.60634e-09,-7.1996e-13,-1995.19,6.89472], Tmin=(789.675,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-11.8052,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (278.535,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 2, 'C-O': 3, 'C=C': 2}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 10.61 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O      -2.52967600   -0.68867400   -0.87817700
C      -1.87716400   -0.19365300    0.20061600
C      -0.39867400   -0.02324900    0.05146900
C       0.46539700   -0.26587500   -0.96871800
C       1.76422700    0.10764600   -0.48948500
C       1.58967000    0.54770400    0.78277000
O       0.27142500    0.47540500    1.13286300
H      -2.11073600   -0.83641600    1.07637500
H      -2.35493700    0.76746100    0.48810500
H       0.20309600   -0.66072800   -1.93638100
H       2.69865800    0.05349200   -1.02502200
H       2.25499800    0.92660800    1.53964800
""",
)

entry(
    index = 2,
    label = "P2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {5,S} {6,S}
2  C u0 p0 c0 {1,D} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {6,S} {11,S}
5  C u1 p0 c0 {1,S} {7,S} {10,S}
6  O u0 p2 c0 {1,S} {4,S}
7  O u0 p2 c0 {5,S} {12,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88768,0.00629857,0.000144742,-2.63059e-07,1.43223e-10,-14576.1,11.0928], Tmin=(10,'K'), Tmax=(603.649,'K')),
            NASAPolynomial(coeffs=[0.924919,0.0528724,-3.79352e-05,1.26243e-08,-1.57084e-12,-14709.3,19.8252], Tmin=(603.649,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-121.244,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (278.535,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 4, 'H-O': 1, 'C-C': 2, 'C-O': 3, 'C=C': 2}
1D rotors:
pivots: [1, 2], dihedral: [8, 1, 2, 3], rotor symmetry: 1, max scan energy: 27.93 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
O      -2.71344200    0.42683800   -0.13257500
C      -1.76209600   -0.53987200   -0.06354500
C      -0.40938200   -0.25906900    0.00550800
C       0.75020400   -1.03988800    0.08266000
C       1.84011400   -0.13716300    0.12640500
C       1.32449100    1.12551300    0.07600400
O      -0.04569300    1.08034400    0.00185300
H      -2.27055000    1.28565500   -0.12344900
H      -2.14963600   -1.54662500   -0.06704300
H       0.78671600   -2.11688900    0.10359200
H       2.88765400   -0.38775600    0.18810700
H       1.76161900    2.10891300    0.08262500
""",
)

entry(
    index = 3,
    label = "P3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {6,D}
3  C u0 p0 c0 {4,D} {6,S} {10,S}
4  C u0 p0 c0 {3,D} {5,S} {11,S}
5  O u0 p2 c0 {2,S} {4,S}
6  C u1 p0 c0 {2,D} {3,S}
7  O u0 p2 c0 {1,S} {12,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75625,0.0231724,4.46537e-05,-9.04577e-08,4.56333e-11,5547.04,13.8409], Tmin=(10,'K'), Tmax=(692.844,'K')),
            NASAPolynomial(coeffs=[3.41372,0.0400948,-2.43387e-05,7.06094e-09,-7.88261e-13,5235.8,12.7791], Tmin=(692.844,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (46.0967,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 4, 'H-O': 1, 'C-C': 2, 'C-O': 3, 'C=C': 2}
1D rotors:
pivots: [1, 2], dihedral: [8, 1, 2, 3], rotor symmetry: 1, max scan energy: 10.60 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 11.46 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       2.09767400    0.82053200    0.43232400
C       1.73056100   -0.44042300   -0.12553200
C       1.53662100   -0.40280400   -1.59977500
C       2.18785400   -0.87330500   -2.68413600
C       1.52048100   -0.47753000   -3.87528400
C       0.45879700    0.24654400   -3.42617700
O       0.43881300    0.30594100   -2.06286200
H       1.39563600    1.44343200    0.21804500
H       2.54610200   -1.12766400    0.09968100
H       0.81974500   -0.82537900    0.35394700
H       1.77876600   -0.69024000   -4.89932100
H      -0.34301600    0.76265100   -3.92778600
""",
)

entry(
    index = 4,
    label = "P4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {5,S}
3  C u0 p0 c0 {2,D} {6,S} {10,S}
4  C u0 p0 c0 {5,S} {6,D} {11,S}
5  O u0 p2 c0 {2,S} {4,S}
6  C u1 p0 c0 {3,S} {4,D}
7  O u0 p2 c0 {1,S} {12,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84126,0.0287423,1.00546e-05,-2.8471e-08,1.13576e-11,5417.59,12.6978], Tmin=(10,'K'), Tmax=(1019.83,'K')),
            NASAPolynomial(coeffs=[7.36955,0.0308616,-1.65343e-05,4.25383e-09,-4.25871e-13,3868.08,-8.46206], Tmin=(1019.83,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (45.0979,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 4, 'H-O': 1, 'C-C': 2, 'C-O': 3, 'C=C': 2}
1D rotors:
pivots: [1, 2], dihedral: [8, 1, 2, 3], rotor symmetry: 1, max scan energy: 11.81 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 10.95 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.58111700   -0.51044300    1.16915700
C      -1.76798700   -0.40000100   -0.24073700
C      -1.10868500   -1.49212200   -1.01171400
C      -0.01912300   -1.54385400   -1.83219900
C       0.07929100   -2.91270400   -2.20087200
C      -0.90801600   -3.61675600   -1.61414500
O      -1.66349400   -2.73947900   -0.86727000
H      -1.94938300   -1.35745700    1.44111400
H      -1.33099700    0.55465100   -0.53510500
H      -2.83824900   -0.37379200   -0.48979600
H       0.61497500   -0.72022900   -2.11603800
H      -1.21732600   -4.64626000   -1.60419900
""",
)

entry(
    index = 5,
    label = "P5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {5,S}
3  C u0 p0 c0 {2,D} {4,S} {10,S}
4  C u0 p0 c0 {3,S} {6,D} {11,S}
5  O u0 p2 c0 {2,S} {6,S}
6  C u1 p0 c0 {4,D} {5,S}
7  O u0 p2 c0 {1,S} {12,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82023,0.0270548,1.86849e-05,-4.09901e-08,1.69818e-11,5317.49,13.1478], Tmin=(10,'K'), Tmax=(930.374,'K')),
            NASAPolynomial(coeffs=[6.05921,0.03394,-1.90365e-05,5.11462e-09,-5.32665e-13,4186.26,-1.33284], Tmin=(930.374,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (44.2521,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 4, 'H-O': 1, 'C-C': 2, 'C-O': 3, 'C=C': 2}
1D rotors:
pivots: [1, 2], dihedral: [8, 1, 2, 3], rotor symmetry: 1, max scan energy: 11.75 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 13.57 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.31073600    0.71764500   -0.30679000
C      -1.49377400   -0.44695300   -0.18747700
C      -0.04203600   -0.15176200   -0.06554900
C       1.03526400   -0.24141200   -0.88975900
C       2.18551300    0.25612500   -0.17208100
C       1.67651300    0.60837800    1.03148500
O       0.37182100    0.38870000    1.15489100
H      -2.18350700    1.24141200    0.49094700
H      -1.65162300   -1.02474300   -1.09944700
H      -1.81808400   -1.06300200    0.66233000
H       1.02627200   -0.61561400   -1.90217900
H       3.20437300    0.33122800   -0.51025400
""",
)

entry(
    index = 6,
    label = "P6",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {7,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {4,S} {11,S}
4  C u0 p0 c0 {3,S} {5,D} {12,S}
5  C u0 p0 c0 {4,D} {6,S} {13,S}
6  O u0 p2 c0 {1,S} {5,S}
7  O u0 p2 c0 {2,S} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86149,0.00803354,0.000170218,-3.25786e-07,1.87572e-10,-20211.8,12.4038], Tmin=(10,'K'), Tmax=(575.314,'K')),
            NASAPolynomial(coeffs=[1.64933,0.0555709,-3.75663e-05,1.21458e-08,-1.49319e-12,-20489.4,17.2282], Tmin=(575.314,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-168.109,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (328.422,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 6, 'H-O': 1, 'C-C': 3, 'C-O': 3, 'C=C': 1}
1D rotors:
pivots: [1, 2], dihedral: [8, 1, 2, 3], rotor symmetry: 1, max scan energy: 17.89 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Inconsistent initial and final conformers But unable to propose troubleshooting methods.Inconsistent initial and final conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.91870400    0.47035200    0.95454800
C      -1.83222400    0.43421200   -0.45855900
C      -0.50140500   -0.16140200   -0.92906300
C      -0.26846300   -0.16514500   -2.40910500
C       0.82222500    0.64856700   -2.66838900
C       1.29406900    1.14438600   -1.46664200
O       0.56709300    0.69263600   -0.40382700
H      -1.15686600    0.97316900    1.26399700
H      -2.65357800   -0.19483300   -0.81088500
H      -1.94743000    1.43253400   -0.90226700
H      -0.37829900   -1.14403100   -0.45246000
H      -0.86010200   -0.72329100   -3.11806900
H       1.24996900    0.86855500   -3.63560600
H       2.11516700    1.80288900   -1.23381800
""",
)

entry(
    index = 7,
    label = "P7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {7,S} {10,S} {11,S}
3  C u1 p0 c0 {1,S} {2,S} {6,S}
4  C u0 p0 c0 {1,S} {5,D} {12,S}
5  C u0 p0 c0 {4,D} {6,S} {13,S}
6  O u0 p2 c0 {3,S} {5,S}
7  O u0 p2 c0 {2,S} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84654,0.0114731,0.000186068,-4.55771e-07,3.48229e-10,-14373,12.6962], Tmin=(10,'K'), Tmax=(413.09,'K')),
            NASAPolynomial(coeffs=[1.51491,0.0530391,-3.38163e-05,1.03662e-08,-1.21899e-12,-14342.4,19.9226], Tmin=(413.09,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-119.505,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (328.422,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 6, 'H-O': 1, 'C-C': 3, 'C-O': 3, 'C=C': 1}
1D rotors:
pivots: [1, 2], dihedral: [8, 1, 2, 3], rotor symmetry: 1, max scan energy: 11.50 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       2.57496000   -0.87153600    0.83763400
C       2.23265800   -1.36992900   -0.47488000
C       2.48686600   -0.39328000   -1.55850300
C       1.81667800    0.93889100   -1.75850300
C       2.89244300    1.69731900   -2.49849500
C       3.97357100    0.92466300   -2.57511500
O       3.81179700   -0.31212500   -1.98722800
H       3.51810900   -0.67694100    0.82231500
H       1.16674300   -1.59759700   -0.42134300
H       2.77190300   -2.30161700   -0.68530000
H       1.55493900    1.41112800   -0.79654600
H       0.87823400    0.86221500   -2.32600800
H       2.80189200    2.69868400   -2.88997900
H       4.94485300    1.09182400   -3.01468500
""",
)

entry(
    index = 8,
    label = "P8",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {7,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {4,D} {6,S}
4  C u0 p0 c0 {1,S} {3,D} {12,S}
5  C u1 p0 c0 {1,S} {6,S} {13,S}
6  O u0 p2 c0 {3,S} {5,S}
7  O u0 p2 c0 {2,S} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85495,0.0134072,0.000192087,-5.47098e-07,5.12245e-10,-13801.9,12.2834], Tmin=(10,'K'), Tmax=(271.67,'K')),
            NASAPolynomial(coeffs=[1.05777,0.0545927,-3.53183e-05,1.09532e-08,-1.30016e-12,-13649.9,22.1329], Tmin=(271.67,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-114.727,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (328.422,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 6, 'H-O': 1, 'C-C': 3, 'C-O': 3, 'C=C': 1}
1D rotors:
pivots: [1, 2], dihedral: [8, 1, 2, 3], rotor symmetry: 1, max scan energy: 15.65 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for P8 exists which is 0.67 kJ/mol lower.Another conformer for P8 exists which is 0.67 kJ/mol lower.


External symmetry: 1, optical isomers: 2

Geometry:
O       2.43365800    0.37896700    1.01364700
C       1.92216400   -0.27099000   -0.14543100
C       0.46021800   -0.03782500   -0.32918500
C      -0.26661100    0.52302100   -1.29572400
C      -1.72718000    0.46767400   -0.91156900
C      -1.62334700   -0.11205800    0.46718300
O      -0.31630000   -0.48716300    0.73140100
H       1.89250700    0.09257300    1.75738200
H       2.46447800    0.13178400   -1.00130200
H       2.11193100   -1.35360600   -0.10040300
H       0.12360100    0.94829000   -2.20751700
H      -2.20674900    1.45787300   -0.92265100
H      -2.32015500   -0.15794200   -1.60181600
H      -2.36848700   -0.65803100    1.02603500
""",
)

entry(
    index = 9,
    label = "P9",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {6,S} {10,S} {11,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {5,D} {6,S}
4  C u1 p0 c0 {1,S} {5,S} {12,S}
5  C u0 p0 c0 {3,D} {4,S} {13,S}
6  O u0 p2 c0 {1,S} {3,S}
7  O u0 p2 c0 {2,S} {14,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.69122,0.0277614,5.16508e-05,-1.05331e-07,5.38912e-11,-19951.1,12.5584], Tmin=(10,'K'), Tmax=(669.458,'K')),
            NASAPolynomial(coeffs=[2.57744,0.0492062,-2.95377e-05,8.51909e-09,-9.48382e-13,-20133.4,15.0095], Tmin=(669.458,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-165.919,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (328.422,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 6, 'H-O': 1, 'C-C': 3, 'C-O': 3, 'C=C': 1}
1D rotors:
pivots: [1, 2], dihedral: [8, 1, 2, 3], rotor symmetry: 1, max scan energy: 14.01 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       2.56866500    0.87518400    0.57851100
C       1.87063700   -0.16924500   -0.10907600
C       1.16112300    0.31040800   -1.32162300
C       1.32786200    0.07609600   -2.67819700
C       0.39352100    0.81689300   -3.37853900
C      -0.40773800    1.59152200   -2.37757700
O       0.13973400    1.19957000   -1.09250400
H       1.91974400    1.56089200    0.76884800
H       2.62068200   -0.90782700   -0.39406300
H       1.15375800   -0.65464400    0.57027000
H       2.07266800   -0.58514800   -3.09652000
H       0.24429000    0.85874100   -4.44631900
H      -1.48092700    1.35540100   -2.37601900
H      -0.30844100    2.68244900   -2.47036100
""",
)

entry(
    index = 10,
    label = "P10",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {5,S}
2  C u0 p0 c0 {1,S} {3,D} {6,S}
3  C u0 p0 c0 {2,D} {4,S} {7,S}
4  C u0 p0 c0 {3,S} {5,D} {8,S}
5  C u0 p0 c0 {1,S} {4,D} {9,S}
6  C u1 p0 c0 {2,S} {10,S} {11,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.1537,-0.0147656,0.000219245,-3.93122e-07,2.25597e-10,6062.27,10.4373], Tmin=(10,'K'), Tmax=(563.018,'K')),
            NASAPolynomial(coeffs=[0.720469,0.043979,-2.87874e-05,8.94419e-09,-1.05631e-12,5904.39,20.1931], Tmin=(563.018,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (50.3816,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-O': 2, 'C-C': 2, 'C=C': 2}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [7, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
C       2.02109400   -0.18580200    0.10117700
C       0.64839300   -0.17889700    0.04738200
C      -0.32184000   -1.19639500    0.13726200
C      -1.58221300   -0.57941500    0.01147700
C      -1.34755000    0.76121700   -0.14719100
O      -0.01480000    1.02782500   -0.12915400
H       2.55099200   -1.11709000    0.23811600
H       2.58159100    0.73312800    0.00782900
H      -0.11190800   -2.24481100    0.27651700
H      -2.55049400   -1.05429700    0.03354900
H      -1.99657600    1.61076300   -0.27849800
""",
)

entry(
    index = 11,
    label = "P11",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {4,S} {11,S}
4  C u0 p0 c0 {3,S} {5,D} {12,S}
5  C u0 p0 c0 {4,D} {6,S} {13,S}
6  O u0 p2 c0 {1,S} {5,S}
7  O u0 p2 c0 {1,S} {15,S}
8  O u0 p2 c0 {2,S} {14,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82657,0.0100583,0.00019723,-3.84298e-07,2.22887e-10,-44714.7,12.9588], Tmin=(10,'K'), Tmax=(578.073,'K')),
            NASAPolynomial(coeffs=[2.08499,0.0624946,-4.36262e-05,1.43236e-08,-1.77127e-12,-45188.1,14.57], Tmin=(578.073,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-371.852,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (353.365,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'H-O': 2, 'C-C': 3, 'C-O': 4, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [9, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [3, 4], dihedral: [2, 3, 4, 12], rotor symmetry: 1, max scan energy: 31.57 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       2.30251500   -0.49390300   -0.66861500
C       1.30216500   -0.95681400    0.23585500
C       0.15679600    0.06353800    0.30656400
O      -0.27021700    0.38734900   -0.97534000
C      -0.98086700   -0.27970200    1.21764900
C      -1.01561600    0.64392100    2.24546000
C       0.02259900    1.54365700    2.06044900
O       0.75482000    1.26593300    0.95223300
H       2.69081800    0.29529600   -0.27211600
H       1.70566000   -1.13708900    1.23702600
H       0.92373200   -1.89539600   -0.17264400
H       0.52020100    0.35641900   -1.53641700
H      -1.66657200   -1.08802500    1.01923400
H      -1.73038400    0.68675100    3.05405600
H       0.32301500    2.40866200    2.63070700
""",
)

entry(
    index = 12,
    label = "P12",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {7,S} {9,S}
2  C u0 p0 c0 {3,S} {8,S} {10,S} {11,S}
3  C u1 p0 c0 {1,S} {2,S} {6,S}
4  C u0 p0 c0 {1,S} {5,D} {12,S}
5  C u0 p0 c0 {4,D} {6,S} {13,S}
6  O u0 p2 c0 {3,S} {5,S}
7  O u0 p2 c0 {1,S} {15,S}
8  O u0 p2 c0 {2,S} {14,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84558,0.0103182,0.000210277,-4.7515e-07,3.31269e-10,-34482.3,13.703], Tmin=(10,'K'), Tmax=(462.205,'K')),
            NASAPolynomial(coeffs=[1.29253,0.0597395,-3.87945e-05,1.20172e-08,-1.42047e-12,-34538.2,20.892], Tmin=(462.205,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-286.728,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (357.522,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'H-O': 2, 'C-C': 3, 'C-O': 4, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [9, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [7, 8], dihedral: [3, 7, 8, 15], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       2.46328000   -0.08808500    0.04130500
C       1.35590200    0.00593500    0.95431200
C       1.69365200    0.75026200    2.19191700
O       1.46954900    2.10992800    2.22576200
C       2.16315600    2.60092500    3.30990200
C       2.88113200    1.67384000    3.94905600
C       2.73310000    0.37207500    3.20713800
O       3.97771500   -0.10495800    2.60078000
H       3.17727800   -0.50731700    0.53832100
H       0.99720200   -0.99738700    1.22168400
H       0.55723200    0.52131200    0.41934900
H       2.02157800    3.65466000    3.49391200
H       3.49822500    1.82453900    4.82078900
H       2.43253800   -0.47352500    3.83322300
H       4.39960300    0.66899700    2.20595300
""",
)

entry(
    index = 13,
    label = "P13",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {7,S} {9,S}
2  C u0 p0 c0 {3,S} {8,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {4,D} {6,S}
4  C u0 p0 c0 {1,S} {3,D} {12,S}
5  C u1 p0 c0 {1,S} {6,S} {13,S}
6  O u0 p2 c0 {3,S} {5,S}
7  O u0 p2 c0 {1,S} {15,S}
8  O u0 p2 c0 {2,S} {14,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70829,0.0217797,0.000226145,-6.47433e-07,5.40582e-10,-33831.3,14.1606], Tmin=(10,'K'), Tmax=(413.002,'K')),
            NASAPolynomial(coeffs=[4.61434,0.053375,-3.5231e-05,1.11598e-08,-1.34782e-12,-34250.4,6.42241], Tmin=(413.002,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-281.289,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (349.208,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'H-O': 2, 'C-C': 3, 'C-O': 4, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [9, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 12.92 kJ/mol
pivots: [5, 6], dihedral: [4, 5, 6, 14], rotor symmetry: 1, max scan energy: 14.43 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.28210700   -0.34198800    1.37055700
C      -2.05515800   -0.28676800   -0.02525700
C      -1.95692300   -1.64607600   -0.64256700
C      -2.19562400   -2.86930200   -0.16236700
C      -1.96004800   -3.88477000   -1.25705800
O      -3.12748500   -4.65851700   -1.61178900
C      -1.46078700   -2.97856700   -2.33716100
O      -1.52750100   -1.65949800   -1.96245500
H      -1.52145500   -0.77330700    1.77407000
H      -1.15180300    0.28472900   -0.28263000
H      -2.90452800    0.25295200   -0.45452600
H      -2.55676200   -3.10382600    0.82605200
H      -1.23452800   -4.65935700   -0.98283900
H      -3.82450900   -4.02677800   -1.82634500
H      -1.26247200   -3.17284500   -3.37844900
""",
)

entry(
    index = 14,
    label = "P14",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {6,S} {7,S} {9,S}
2  C u0 p0 c0 {3,S} {8,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {5,D} {6,S}
4  C u1 p0 c0 {1,S} {5,S} {12,S}
5  C u0 p0 c0 {3,D} {4,S} {13,S}
6  O u0 p2 c0 {1,S} {3,S}
7  O u0 p2 c0 {1,S} {15,S}
8  O u0 p2 c0 {2,S} {14,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80608,0.0123602,0.000213186,-4.76189e-07,3.18529e-10,-43508.2,14.0243], Tmin=(10,'K'), Tmax=(502.17,'K')),
            NASAPolynomial(coeffs=[3.0133,0.0576182,-3.83263e-05,1.2141e-08,-1.46226e-12,-43919.6,12.4139], Tmin=(502.17,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-361.8,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (353.365,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'H-O': 2, 'C-C': 3, 'C-O': 4, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [9, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [6, 7], dihedral: [5, 6, 7, 15], rotor symmetry: 1, max scan energy: 22.32 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.39903100   -0.91008000    1.00354200
C       1.74670800    0.36908000    0.46921100
C       1.98531800    0.32244000   -0.99745700
C       1.33484400    0.89723000   -2.08257200
C       1.95608400    0.47012700   -3.24093300
C       3.05303500   -0.48302800   -2.86744300
O       2.92279200   -1.78115100   -3.36567100
O       3.01081700   -0.48249500   -1.39998800
H       2.11243100   -1.51249500    0.76585900
H       2.63960800    0.76531000    0.97570200
H       0.91133800    1.03654200    0.68397500
H       0.48402500    1.55842600   -2.00584100
H       1.72566900    0.73162200   -4.26213400
H       4.06396000   -0.17227600   -3.14467200
H       1.99347200   -2.03133800   -3.28738800
""",
)

entry(
    index = 15,
    label = "P15",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {8,S}
2  O u0 p2 c0 {3,S} {4,S}
3  O u0 p2 c0 {2,S} {14,S}
4  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
5  C u0 p0 c0 {1,S} {4,S} {6,D}
6  C u0 p0 c0 {5,D} {7,S} {11,S}
7  C u0 p0 c0 {6,S} {8,D} {12,S}
8  C u0 p0 c0 {1,S} {7,D} {13,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7299,0.0211391,0.000176768,-4.83397e-07,3.87531e-10,-21069.7,12.7015], Tmin=(10,'K'), Tmax=(419.428,'K')),
            NASAPolynomial(coeffs=[3.35304,0.0525263,-3.48781e-05,1.09934e-08,-1.31772e-12,-21282.5,11.2779], Tmin=(419.428,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-175.189,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (324.264,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'H-O': 1, 'C-C': 2, 'C-O': 3, 'O-O': 1, 'C=C': 2}
1D rotors:
pivots: [1, 2], dihedral: [9, 1, 2, 3], rotor symmetry: 1, max scan energy: 29.80 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 25.05 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O      -3.35050400   -1.03952800    0.10190600
O      -1.99766800   -0.75347200   -0.32724200
C      -1.73437700   -1.56606900   -1.48051300
C      -1.58735500   -3.01213100   -1.17008900
C      -2.45929100   -4.05991600   -1.16585100
C      -1.72892400   -5.20121300   -0.70303000
C      -0.46662800   -4.76263100   -0.45734700
O      -0.35983700   -3.43553000   -0.73259300
H      -3.19272300   -1.69332000    0.79851700
H      -0.79533900   -1.15871900   -1.86361900
H      -2.52709100   -1.41229200   -2.21684300
H      -3.49569000   -4.01927200   -1.46136900
H      -2.09418400   -6.20783500   -0.57668100
H       0.43133500   -5.24353100   -0.10777800
""",
)

entry(
    index = 16,
    label = "PROO1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {6,S}
3  C u0 p0 c0 {2,D} {4,S} {11,S}
4  C u0 p0 c0 {3,S} {5,D} {12,S}
5  C u0 p0 c0 {4,D} {6,S} {13,S}
6  O u0 p2 c0 {2,S} {5,S}
7  O u0 p2 c0 {1,S} {8,S}
8  O u0 p2 c0 {7,S} {14,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 O u1 p2 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75239,0.0441119,-4.78448e-06,-2.04444e-08,9.25977e-12,-1828.09,14.4039], Tmin=(10,'K'), Tmax=(1073.8,'K')),
            NASAPolynomial(coeffs=[11.3866,0.0348252,-1.85641e-05,4.7196e-09,-4.65711e-13,-4571.73,-28.1113], Tmin=(1073.8,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-15.1288,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 2, 'C-O': 3, 'C=C': 2, 'O-O': 2}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for PROO1 exists which is 5.83 kJ/mol lower.Another conformer for PROO1 exists which is 5.83 kJ/mol lower.
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: Bond ([[2, 3]]) broke during the scan. But unable to propose troubleshooting methods.Bond ([[2, 3]]) broke during the scan. But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       3.78436700    0.80395700   -0.74701200
O       3.02176800    0.62036000   -1.68100400
O       1.43572500    0.23190300   -1.23181100
C       1.42245600   -0.03285900    0.13743100
C       1.51167700   -1.47787700    0.48738300
C       2.49714000   -2.25235000    1.02003700
C       1.97806900   -3.58535100    1.08624000
C       0.71629500   -3.52064800    0.58766500
O       0.41304400   -2.24669800    0.21931400
H       0.50305200    0.42758200    0.52278800
H       2.25888600    0.50453200    0.61923600
H       3.47578000   -1.91560300    1.32382400
H       2.47813800   -4.46664100    1.45472300
H      -0.06098600   -4.25034100    0.43617000
""",
)

entry(
    index = 17,
    label = "PROO2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {6,S}
3  C u0 p0 c0 {2,D} {4,S} {10,S}
4  C u0 p0 c0 {3,S} {5,D} {11,S}
5  C u0 p0 c0 {4,D} {6,S} {12,S}
6  O u0 p2 c0 {2,S} {5,S}
7  O u0 p2 c0 {1,S} {13,S}
8  O u0 p2 c0 {1,S} {14,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 O u1 p2 c0 {7,S}
14 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61645,0.0378065,3.73332e-05,-9.67064e-08,5.07771e-11,-25552.6,14.7008], Tmin=(10,'K'), Tmax=(717.741,'K')),
            NASAPolynomial(coeffs=[5.81753,0.0477489,-2.986e-05,8.81711e-09,-9.94836e-13,-26440.6,0.826698], Tmin=(717.741,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-212.488,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (328.422,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 4, 'C-C': 2, 'C-O': 4, 'C=C': 2, 'H-O': 1, 'O-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 11], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [3, 5], dihedral: [2, 3, 5, 6], rotor symmetry: 1, max scan energy: 19.97 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -3.04267600   -1.62259200    0.63179500
O      -1.78002800   -1.51018700    0.30847600
C      -1.45327500   -0.04044200   -0.03817600
O      -2.15561300    0.77440000    0.80420300
C       0.00007800    0.13183700    0.12688800
C       0.76926900    0.57352900    1.15875800
C       2.12371400    0.48005600    0.71109100
C       2.07208500   -0.01259800   -0.55530700
O       0.78379400   -0.22948600   -0.93122000
H      -1.75985000    0.01416200   -1.08947000
H      -3.04231700    0.38094000    0.87195000
H       0.40626000    0.92526900    2.11021000
H       3.01324100    0.74676600    1.25875400
H       2.82093200   -0.25240800   -1.29086500
""",
)

entry(
    index = 18,
    label = "PROO3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {6,S}
3  C u0 p0 c0 {2,D} {4,S} {8,S}
4  C u0 p0 c0 {3,S} {5,D} {11,S}
5  C u0 p0 c0 {4,D} {6,S} {12,S}
6  O u0 p2 c0 {2,S} {5,S}
7  O u0 p2 c0 {1,S} {13,S}
8  O u0 p2 c0 {3,S} {14,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {7,S}
14 O u1 p2 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.69324,0.0293249,7.41076e-05,-1.55461e-07,8.34591e-11,-20772.3,13.7085], Tmin=(10,'K'), Tmax=(656.083,'K')),
            NASAPolynomial(coeffs=[4.0388,0.0516298,-3.27003e-05,9.78219e-09,-1.11706e-12,-21343,8.18299], Tmin=(656.083,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-172.75,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 4, 'C-C': 2, 'C-O': 4, 'C=C': 2, 'H-O': 1, 'O-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for PROO3 exists which is 6.66 kJ/mol lower.Another conformer for PROO3 exists which is 6.66 kJ/mol lower.
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 12], invalidation reason: Inconsistent initial and final conformers But unable to propose troubleshooting methods.Inconsistent initial and final conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       0.36014000    2.30345400    1.27426100
O      -0.78759700    1.95715500    0.69238800
C      -0.85663200    0.66165000    0.26008700
C       0.13000000   -0.29432900    0.20946400
C       1.56855700   -0.32571600    0.61840100
O       1.75142200   -0.12602700    2.00853300
O      -0.42376200   -1.42475300   -0.30687500
C      -1.73752600   -1.17397200   -0.58593200
C      -2.06375200    0.09849900   -0.25724800
H       1.96309500   -1.31407100    0.37763900
H       2.12641800    0.41710900    0.03284900
H       1.46108200    0.78005900    2.18213400
H      -2.29191400   -1.99439700   -1.00760200
H      -3.01986300    0.58509700   -0.35475600
""",
)

entry(
    index = 19,
    label = "PROO4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,D} {6,S}
3  C u0 p0 c0 {4,S} {5,D} {8,S}
4  C u0 p0 c0 {2,D} {3,S} {11,S}
5  C u0 p0 c0 {3,D} {6,S} {12,S}
6  O u0 p2 c0 {2,S} {5,S}
7  O u0 p2 c0 {1,S} {13,S}
8  O u0 p2 c0 {3,S} {14,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {7,S}
14 O u1 p2 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.6226,0.0525941,-3.3794e-05,8.97464e-09,-5.25932e-13,-20465.3,14.7943], Tmin=(10,'K'), Tmax=(1332.44,'K')),
            NASAPolynomial(coeffs=[15.9515,0.0241228,-1.13566e-05,2.55876e-09,-2.24689e-13,-24508.9,-51.0692], Tmin=(1332.44,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-170.144,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (320.107,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 4, 'C-C': 2, 'C-O': 4, 'C=C': 2, 'H-O': 1, 'O-O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 18.43 kJ/mol
pivots: [6, 7], dihedral: [5, 6, 7, 8], rotor symmetry: 1, max scan energy: 10.33 kJ/mol
pivots: [7, 8], dihedral: [6, 7, 8, 13], rotor symmetry: 1, max scan energy: 10.28 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -3.23353700   -1.67930700   -0.16966800
O      -3.08122600   -0.36736000   -0.02217200
C      -1.77398400    0.02359900    0.12708800
C      -1.40399700    1.32551700    0.28922500
O      -0.05030900    1.38135600    0.40214000
C       0.43056400    0.09610400    0.31623700
C       1.90733100   -0.05251600    0.45231500
O       2.38246300    0.25196600    1.76062000
C      -0.59463800   -0.77953200    0.14725500
H      -1.94880500    2.25134700    0.33817800
H       2.40831600    0.57023900   -0.30165000
H       2.17345600   -1.09213000    0.26025300
H       2.17833800    1.17631800    1.93625600
H      -0.54423200   -1.85007900    0.05359500
""",
)

entry(
    index = 20,
    label = "PROO5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {6,S}
3  C u0 p0 c0 {2,D} {5,S} {12,S}
4  C u0 p0 c0 {5,D} {6,S} {8,S}
5  C u0 p0 c0 {3,S} {4,D} {11,S}
6  O u0 p2 c0 {2,S} {4,S}
7  O u0 p2 c0 {1,S} {13,S}
8  O u0 p2 c0 {4,S} {14,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {7,S}
14 O u1 p2 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67546,0.0504661,-2.86654e-05,5.09299e-09,4.67249e-13,-20961.2,14.0589], Tmin=(10,'K'), Tmax=(1316.21,'K')),
            NASAPolynomial(coeffs=[15.7247,0.0245555,-1.13392e-05,2.49778e-09,-2.13748e-13,-25060.6,-50.9055], Tmin=(1316.21,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-174.257,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (324.264,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 4, 'C-C': 2, 'C-O': 4, 'C=C': 2, 'H-O': 1, 'O-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for PROO5 exists which is 2.66 kJ/mol lower.Another conformer for PROO5 exists which is 2.66 kJ/mol lower.
pivots: [6, 7], dihedral: [5, 6, 7, 8], rotor symmetry: 1, max scan energy: 12.26 kJ/mol
pivots: [7, 8], dihedral: [6, 7, 8, 14], rotor symmetry: 1, max scan energy: 11.25 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       3.69830600    1.25998900    0.57930100
O       2.41357400    1.62059000    0.60125000
C       1.56774200    0.62641200    0.24877700
C       1.72256600   -0.67450300   -0.12660700
C       0.39231500   -1.14278500   -0.34925100
C      -0.45638800   -0.10388900   -0.10233700
C      -1.93498100    0.06565600   -0.11213400
O      -2.49822000    0.18857600    1.19184000
O       0.27475300    1.00557000    0.27126100
H       2.65597500   -1.20052400   -0.22124400
H       0.10015100   -2.13544700   -0.65325600
H      -2.20250800    0.92819200   -0.73758800
H      -2.38197700   -0.82366100   -0.55754200
H      -2.15000000    0.99519200    1.58583400
""",
)

entry(
    index = 21,
    label = "PROO6",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {10,S}
3  C u0 p0 c0 {1,S} {8,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {5,D} {13,S}
5  C u0 p0 c0 {4,D} {6,S} {14,S}
6  O u0 p2 c0 {1,S} {5,S}
7  O u0 p2 c0 {2,S} {15,S}
8  O u0 p2 c0 {3,S} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 O u1 p2 c0 {7,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.47759,0.0502758,-1.66504e-06,-3.59321e-08,1.8808e-11,-30803.5,14.8504], Tmin=(10,'K'), Tmax=(845.939,'K')),
            NASAPolynomial(coeffs=[7.10084,0.0493343,-2.87051e-05,8.00286e-09,-8.62546e-13,-31995.8,-5.44762], Tmin=(845.939,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-256.142,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (374.151,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 6, 'C-C': 3, 'C-O': 4, 'C=C': 1, 'H-O': 1, 'O-O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 11.39 kJ/mol
* Invalidated! pivots: [7, 8], dihedral: [3, 7, 8, 9], invalidation reason: Inconsistent initial and final conformers But unable to propose troubleshooting methods.Inconsistent initial and final conformers But unable to propose troubleshooting methods.
pivots: [8, 9], dihedral: [7, 8, 9, 16], rotor symmetry: 1, max scan energy: 15.15 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.63198500   -2.58133900    0.60088600
O      -1.76041700   -1.32199500    0.96567600
C      -1.00807600   -0.42345300    0.05343400
C      -1.20002700    0.98761800    0.48855600
C      -0.01248600    1.47573300    0.85098400
O       1.04057500    0.62589600    0.72622400
C       0.51229300   -0.64002200    0.21697900
C       1.24817200   -0.98046000   -1.06856400
O       0.99813100   -0.03796100   -2.09748300
H      -1.36920700   -0.66362700   -0.94738100
H      -2.13990200    1.51542800    0.49265400
H       0.24563200    2.45811900    1.22210300
H       0.70058300   -1.40409800    0.97448300
H       0.88774400   -1.94646600   -1.42885100
H       2.32082400   -1.07060500   -0.85383200
H       1.35186600    0.80768800   -1.80136900
""",
)

entry(
    index = 22,
    label = "PROO7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {8,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {5,D} {13,S}
5  C u0 p0 c0 {4,D} {6,S} {14,S}
6  O u0 p2 c0 {1,S} {5,S}
7  O u0 p2 c0 {1,S} {15,S}
8  O u0 p2 c0 {3,S} {16,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 O u1 p2 c0 {7,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76706,0.0154498,0.000242062,-5.75234e-07,4.08093e-10,-33260,14.1814], Tmin=(10,'K'), Tmax=(475.507,'K')),
            NASAPolynomial(coeffs=[3.3406,0.0621866,-4.14868e-05,1.31409e-08,-1.58093e-12,-33707.2,10.7923], Tmin=(475.507,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-276.583,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (378.308,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 6, 'C-C': 3, 'C-O': 4, 'C=C': 1, 'H-O': 1, 'O-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for PROO7 exists which is 1.18 kJ/mol lower.Another conformer for PROO7 exists which is 1.18 kJ/mol lower.
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [4, 5], dihedral: [3, 4, 5, 12], rotor symmetry: 1, max scan energy: 21.44 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.04767400    1.57008100    1.62037500
O       0.40917500    1.71750200    0.47910900
C       0.16639400    0.40655600   -0.19684100
C       1.51092700   -0.10304900   -0.70166700
O       1.36128900   -1.31397500   -1.41525200
C      -0.66633600   -0.51381600    0.70203700
C      -2.05550300   -0.27650900    0.16217200
C      -1.95375400    0.43113200   -0.95495700
O      -0.64560000    0.75920700   -1.29464600
H       2.15477300   -0.30347200    0.15483500
H       1.96907600    0.68625800   -1.30980800
H       0.82332500   -1.12249300   -2.19176900
H      -0.52423800   -0.23967500    1.74877200
H      -0.34818500   -1.55313000    0.57352200
H      -2.97036000   -0.65018500    0.59450400
H      -2.69568000    0.78431900   -1.65411800
""",
)

entry(
    index = 23,
    label = "PROO8",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {8,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {5,D} {6,S}
5  C u0 p0 c0 {2,S} {4,D} {14,S}
6  O u0 p2 c0 {1,S} {4,S}
7  O u0 p2 c0 {1,S} {15,S}
8  O u0 p2 c0 {3,S} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 O u1 p2 c0 {7,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.43009,0.0544469,-1.86739e-05,-1.27607e-08,8.41517e-12,-32180.4,14.1082], Tmin=(10,'K'), Tmax=(940.776,'K')),
            NASAPolynomial(coeffs=[8.50118,0.0458906,-2.57668e-05,6.95939e-09,-7.29926e-13,-33710,-13.106], Tmin=(940.776,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-267.59,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (374.151,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 6, 'C-C': 3, 'C-O': 4, 'C=C': 1, 'H-O': 1, 'O-O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 9.47 kJ/mol
* Invalidated! pivots: [6, 7], dihedral: [5, 6, 7, 8], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [7, 8], dihedral: [6, 7, 8, 16], rotor symmetry: 1, max scan energy: 17.01 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.28952100    2.48923300    0.38539000
O      -1.93163400    1.30715900    0.84995900
C      -1.50288800    0.41851200   -0.23354200
C      -1.40536100   -0.99287700    0.35787900
C       0.08778100   -1.14254600    0.52182300
C       0.68979100   -0.11223100   -0.06355600
C       2.11735000    0.28225400   -0.24031400
O       2.40265100    1.54462300    0.34776800
O      -0.20554600    0.78964600   -0.64155100
H      -2.19557500    0.58507400   -1.05489500
H      -1.83433100   -1.73725300   -0.32069500
H      -1.95929700   -1.04114700    1.29910300
H       0.58015200   -1.95798400    1.02772300
H       2.76028400   -0.45069400    0.24764800
H       2.35592900    0.28521800   -1.31431900
H       1.77105800    2.17623700   -0.01390600
""",
)

entry(
    index = 24,
    label = "PROO9",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {8,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {5,D} {6,S}
5  C u0 p0 c0 {1,S} {4,D} {14,S}
6  O u0 p2 c0 {2,S} {4,S}
7  O u0 p2 c0 {1,S} {15,S}
8  O u0 p2 c0 {3,S} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 O u1 p2 c0 {7,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.37327,0.0596336,-3.69599e-05,8.25284e-09,3.17802e-13,-30785.9,14.5938], Tmin=(10,'K'), Tmax=(1117.01,'K')),
            NASAPolynomial(coeffs=[11.4328,0.0391724,-2.07627e-05,5.31781e-09,-5.31994e-13,-33110.4,-27.526], Tmin=(1117.01,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-256.003,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (369.994,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 6, 'C-C': 3, 'C-O': 4, 'C=C': 1, 'H-O': 1, 'O-O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 11.39 kJ/mol
pivots: [5, 6], dihedral: [4, 5, 6, 7], rotor symmetry: 1, max scan energy: 13.87 kJ/mol
pivots: [6, 7], dihedral: [5, 6, 7, 14], rotor symmetry: 1, max scan energy: 15.31 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -3.35467000    0.27679100   -1.52731500
O      -2.04045000    0.30678300   -1.47463300
C      -1.55983300    0.48170900   -0.06711400
C      -0.07145900    0.48468100   -0.08156800
C       0.35277400   -0.69831500    0.38295100
C       1.72234900   -1.28698400    0.50483200
O       2.00361900   -1.72328100    1.82673500
O      -0.64147500   -1.52434400    0.82152100
C      -1.87084200   -0.75799500    0.77344200
H      -2.06066300    1.38368300    0.28327100
H       0.54708500    1.27531600   -0.47412500
H       2.46867700   -0.53507300    0.24863800
H       1.81070200   -2.11417900   -0.21505700
H       1.30219200   -2.33404900    2.07794700
H      -2.13306700   -0.48207900    1.79742100
H      -2.65840900   -1.37170600    0.33988400
""",
)

entry(
    index = 25,
    label = "PROO10",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {5,S} {8,S}
2  O u0 p2 c0 {3,S} {4,S}
3  O u1 p2 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
5  C u0 p0 c0 {1,S} {4,S} {6,D}
6  C u0 p0 c0 {5,D} {7,S} {11,S}
7  C u0 p0 c0 {6,S} {8,D} {12,S}
8  C u0 p0 c0 {1,S} {7,D} {13,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95233,0.0266522,3.22401e-05,-5.5974e-08,2.16969e-11,-3237.89,13.7542], Tmin=(10,'K'), Tmax=(974.505,'K')),
            NASAPolynomial(coeffs=[7.38045,0.0366825,-2.0297e-05,5.34622e-09,-5.44941e-13,-5050.44,-8.56773], Tmin=(974.505,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-26.8196,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 2, 'C-O': 3, 'C=C': 2, 'O-O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 10.23 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       3.34266300   -0.49581500    1.18714400
O       2.03381900   -0.48860600    1.06965000
C       1.60163400    0.31430900   -0.10060000
C       1.71120300    1.76466800    0.13793200
C       2.70241100    2.67298600   -0.08304000
C       2.22861500    3.92339400    0.42284300
C       0.98476100    3.68210400    0.91581200
O       0.65058200    2.37580500    0.75336900
H       0.56597800    0.00752500   -0.24668000
H       2.22412400   -0.00338900   -0.93558200
H       3.65657900    2.46877900   -0.54157200
H       2.74363300    4.87051800    0.41734100
H       0.24000600    4.30216500    1.38546900
""",
)

entry(
    index = 26,
    label = "PROO11",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {10,S}
3  C u0 p0 c0 {1,S} {9,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {5,D} {13,S}
5  C u0 p0 c0 {4,D} {6,S} {14,S}
6  O u0 p2 c0 {1,S} {5,S}
7  O u0 p2 c0 {1,S} {16,S}
8  O u0 p2 c0 {2,S} {15,S}
9  O u0 p2 c0 {3,S} {17,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 O u1 p2 c0 {8,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74691,0.016419,0.000261795,-6.00516e-07,4.10049e-10,-54880.8,14.8232], Tmin=(10,'K'), Tmax=(492.997,'K')),
            NASAPolynomial(coeffs=[2.90751,0.0708885,-4.89423e-05,1.57768e-08,-1.9119e-12,-55377.2,12.4052], Tmin=(492.997,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-456.366,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (403.252,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 3, 'C-O': 5, 'C=C': 1, 'H-O': 2, 'O-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for PROO11 exists which is 3.34 kJ/mol lower.Another conformer for PROO11 exists which is 3.34 kJ/mol lower.
* Invalidated! pivots: [7, 8], dihedral: [3, 7, 8, 14], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [7, 9], dihedral: [3, 7, 9, 10], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [9, 10], dihedral: [7, 9, 10, 17], rotor symmetry: 1, max scan energy: 25.67 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.34549900   -2.49140700    0.70331300
O      -1.18194800   -1.58352300    1.16331100
C      -0.92918000   -0.22512200    0.61754000
C      -1.16867900   -0.14489400   -0.84880700
C      -0.00834500    0.14154400   -1.44424800
O       1.05462900    0.32168200   -0.62177900
C       0.56431400    0.23793200    0.75178000
O       1.38241600   -0.57804600    1.50281900
C       0.66008900    1.63987700    1.35765900
O       0.16386500    1.65477600    2.68077000
H      -1.57987500    0.36907200    1.25845600
H      -2.11309800   -0.33000300   -1.33450900
H       0.21083900    0.25974100   -2.49652000
H       1.23632700   -1.49449100    1.21957400
H       1.71007900    1.94915800    1.29793200
H       0.05506200    2.33685600    0.77585000
H       0.67986800    1.00909200    3.17812000
""",
)

entry(
    index = 27,
    label = "PROO12",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {10,S}
3  C u0 p0 c0 {1,S} {9,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {5,D} {13,S}
5  C u0 p0 c0 {4,D} {6,S} {14,S}
6  O u0 p2 c0 {1,S} {5,S}
7  O u0 p2 c0 {1,S} {15,S}
8  O u0 p2 c0 {2,S} {17,S}
9  O u0 p2 c0 {3,S} {16,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 O u1 p2 c0 {7,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.55627,0.0379992,0.000108905,-2.61394e-07,1.64095e-10,-51575.2,14.5875], Tmin=(10,'K'), Tmax=(552.823,'K')),
            NASAPolynomial(coeffs=[3.59979,0.0657433,-4.25085e-05,1.30125e-08,-1.51819e-12,-52008.8,10.5254], Tmin=(552.823,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-428.887,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (407.409,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 3, 'C-O': 5, 'C=C': 1, 'H-O': 2, 'O-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 13], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [9, 10], dihedral: [3, 9, 10, 17], invalidation reason: Another conformer for PROO12 exists which is 5.39 kJ/mol lower.Another conformer for PROO12 exists which is 5.39 kJ/mol lower.


External symmetry: 1, optical isomers: 2

Geometry:
O       0.89111800    0.67432900    2.27442000
O      -0.02235600   -0.13650200    1.77477900
C       0.12761600   -0.36181400    0.31873300
C       1.59658200   -0.52702700   -0.06321100
O       2.27142400    0.70148600   -0.20102400
O      -0.57004100   -1.57188900    0.12836800
C      -1.74617800   -1.27829700   -0.53694000
C      -1.88118300   -0.00779500   -0.89482700
C      -0.66189100    0.76360300   -0.45247500
O      -0.91222900    1.92514100    0.30623600
H       2.07320300   -1.19588600    0.66510400
H       1.61701200   -1.01901900   -1.03781900
H       2.21287500    1.14187600    0.65655600
H      -2.38734500   -2.13401100   -0.68606500
H      -2.71060800    0.42520200   -1.43170400
H      -0.05034300    1.10777300   -1.28845200
H      -1.47372400    1.68215500    1.05175500
""",
)

entry(
    index = 28,
    label = "PROO13",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {7,S} {10,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {11,S}
3  C u0 p0 c0 {4,S} {9,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {5,D} {6,S}
5  C u0 p0 c0 {1,S} {4,D} {14,S}
6  O u0 p2 c0 {2,S} {4,S}
7  O u0 p2 c0 {1,S} {17,S}
8  O u0 p2 c0 {2,S} {15,S}
9  O u0 p2 c0 {3,S} {16,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 O u1 p2 c0 {8,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.26057,0.0658094,-3.57415e-05,-2.01271e-09,6.28746e-12,-51581.4,15.5031], Tmin=(10,'K'), Tmax=(883.061,'K')),
            NASAPolynomial(coeffs=[9.408,0.0498447,-2.88052e-05,7.98707e-09,-8.57045e-13,-53130.4,-16.0131], Tmin=(883.061,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-428.936,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (399.095,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 3, 'C-O': 5, 'C=C': 1, 'H-O': 2, 'O-O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 10.81 kJ/mol
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 7], invalidation reason: Another conformer for PROO13 exists which is 0.80 kJ/mol lower.Another conformer for PROO13 exists which is 0.80 kJ/mol lower.
* Invalidated! pivots: [6, 7], dihedral: [5, 6, 7, 14], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [9, 10], dihedral: [3, 9, 10, 17], rotor symmetry: 1, max scan energy: 21.07 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.38959400    2.58800400    0.37112000
O      -1.85180100    1.57316700    1.02501100
C      -1.55379200    0.46549700    0.13474500
O      -0.36406600    0.76403400   -0.56988900
C       0.64766800    0.02646600    0.01706800
C       2.01885900    0.34182000   -0.49229900
O       3.03390600   -0.34858300    0.20890600
C       0.22760100   -0.84323500    0.93754000
C      -1.27247200   -0.77505100    1.01686400
O      -1.93734200   -1.94433600    0.55384200
H      -2.38303200    0.36707300   -0.56176000
H       2.15663200    1.43193900   -0.47353800
H       2.09186200    0.03261900   -1.53908200
H       3.06556900    0.00158400    1.10524600
H       0.84709900   -1.53031700    1.49068000
H      -1.66101700   -0.59382100    2.02102700
H      -1.42984500   -2.28923700   -0.18966900
""",
)

entry(
    index = 29,
    label = "PROO14",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {7,S} {10,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {11,S}
3  C u0 p0 c0 {4,S} {9,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {5,D} {6,S}
5  C u0 p0 c0 {1,S} {4,D} {14,S}
6  O u0 p2 c0 {2,S} {4,S}
7  O u0 p2 c0 {1,S} {15,S}
8  O u0 p2 c0 {2,S} {17,S}
9  O u0 p2 c0 {3,S} {16,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 O u1 p2 c0 {7,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.18623,0.0761469,-7.40456e-05,4.40357e-08,-1.20084e-11,-53756.4,14.7375], Tmin=(10,'K'), Tmax=(778.624,'K')),
            NASAPolynomial(coeffs=[7.16855,0.0556887,-3.46333e-05,1.02904e-08,-1.17349e-12,-54376.5,-3.47837], Tmin=(778.624,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-447.02,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (394.937,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 3, 'C-O': 5, 'C=C': 1, 'H-O': 2, 'O-O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 10.04 kJ/mol
pivots: [5, 6], dihedral: [4, 5, 6, 7], rotor symmetry: 1, max scan energy: 15.91 kJ/mol
* Invalidated! pivots: [6, 7], dihedral: [5, 6, 7, 15], invalidation reason: Another conformer for PROO14 exists which is 1.36 kJ/mol lower.Another conformer for PROO14 exists which is 1.36 kJ/mol lower.
pivots: [9, 10], dihedral: [3, 9, 10, 17], rotor symmetry: 1, max scan energy: 16.78 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -3.30844000   -0.62300400    1.22780200
O      -2.02819800   -0.90670400    1.35327800
C      -1.29293300   -0.67243500    0.08341400
C       0.13796100   -1.01379400    0.29030000
C       0.83471400    0.12817300    0.32783800
C       2.29507100    0.36217400    0.55493800
O       2.98178800   -0.80201600    0.96933100
O       0.09033700    1.25990500    0.13905500
C      -1.24429300    0.83085900   -0.23745300
O      -1.43549300    0.99165100   -1.60454400
H      -1.83621900   -1.22002100   -0.68558800
H       0.54249800   -2.00709500    0.38772600
H       2.40483600    1.19515500    1.26402200
H       2.75769200    0.68124100   -0.38346000
H       2.63002800   -1.06296600    1.82704800
H      -1.94426300    1.41582600    0.36236500
H      -1.38966800    1.93170900   -1.80996400
""",
)

entry(
    index = 30,
    label = "P16",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {6,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {5,D} {6,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {2,S} {3,D} {11,S}
5  C u0 p0 c0 {2,D} {7,S} {12,S}
6  O u0 p2 c0 {1,S} {2,S}
7  O u0 p2 c0 {5,S} {13,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90017,0.00623232,0.000161377,-3.25921e-07,2.04603e-10,-21118.8,11.8402], Tmin=(10,'K'), Tmax=(503.902,'K')),
            NASAPolynomial(coeffs=[0.697663,0.0516316,-3.32346e-05,1.023e-08,-1.20502e-12,-21049.6,22.5789], Tmin=(503.902,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-175.621,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 2, 'C=C': 2, 'C-O': 3, 'C-H': 5, 'H-O': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [8, 1, 2, 3], invalidation reason: Another conformer for P1 exists which is 3.57 kJ/mol lower.


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.64257100   -0.89922600    2.61404900
C      -1.20134400   -0.40427800    1.45115900
C      -0.41480900   -0.05254600    0.42549900
C       1.02478100   -0.18164000    0.28009200
C       1.38113800    0.31623400   -0.90873100
C       0.15500500    0.81303000   -1.61908800
O      -0.92777900    0.54553700   -0.71043500
H      -1.23438200   -1.56353200    2.97843800
H      -2.27363900   -0.24313500    1.42584400
H       1.66102500   -0.61704800    1.03546700
H       2.37730800    0.36742100   -1.32574700
H       0.18462500    1.89021200   -1.83036800
H      -0.03525700    0.29033000   -2.56595100
""",
)

entry(
    index = 31,
    label = "P17",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,D} {11,S}
4  C u0 p0 c0 {2,S} {5,S} {10,D}
5  C u0 p0 c0 {3,D} {4,S} {12,S}
6  O u0 p2 c0 {1,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {4,D}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78956,0.0238102,4.40555e-05,-7.86424e-08,3.49389e-11,-32408.5,11.7659], Tmin=(10,'K'), Tmax=(792.037,'K')),
            NASAPolynomial(coeffs=[3.36698,0.0431489,-2.51519e-05,7.03565e-09,-7.61258e-13,-32881.2,10.2994], Tmin=(792.037,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-269.455,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 4, 'C=C': 1, 'H-O': 1, 'C-O': 1, 'C=O': 1}
1D rotors:
pivots: [5, 6], dihedral: [4, 5, 6, 11], rotor symmetry: 1, max scan energy: 10.18 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.69188500    2.11840100   -0.38860400
C       0.83667000    1.27602500   -0.25158800
C      -0.63447600    1.47986500   -0.31849600
C      -1.27156700    0.31106500   -0.19571500
C      -0.33265500   -0.86741800   -0.03284500
O      -0.67047600   -1.68347300    1.08524100
C       1.06633900   -0.21717700    0.02092200
H      -1.07644300    2.45895400   -0.45127500
H      -2.34561400    0.16260500   -0.19773900
H      -0.42306500   -1.53816800   -0.89170800
H      -0.67301000   -1.12253600    1.86912000
H       1.51037200   -0.34207200    1.01244400
H       1.77518100   -0.62635500   -0.70136200
""",
)

entry(
    index = 32,
    label = "P18",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  C u0 p0 c0 {2,S} {5,D} {6,S}
4  C u0 p0 c0 {2,D} {9,S} {10,S}
5  C u0 p0 c0 {3,D} {7,S} {8,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {5,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87319,0.00738066,0.000130378,-2.60397e-07,1.5354e-10,-10260.3,9.08241], Tmin=(10,'K'), Tmax=(578.483,'K')),
            NASAPolynomial(coeffs=[3.75418,0.0379279,-2.59055e-05,8.53444e-09,-1.06895e-12,-10743.8,5.29269], Tmin=(578.483,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-85.3615,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (249.434,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'H-O': 1, 'C=C': 2, 'C-O': 1, 'C-C': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 30.55 kJ/mol
pivots: [3, 5], dihedral: [2, 3, 5, 11], rotor symmetry: 1, max scan energy: 18.29 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C      -1.75214300    0.70902000    0.54969500
C      -0.82668400    0.32810100   -0.33262100
C       0.45326700   -0.28610800    0.02102700
C       1.36047500   -0.65662800   -0.89589500
O       0.62647300   -0.44136400    1.36829300
H      -1.60007100    0.57929800    1.61386600
H      -2.68271300    1.15927200    0.22591900
H      -0.99209900    0.46399700   -1.39636400
H       2.30561800   -1.11099300   -0.61998000
H       1.16623200   -0.50795900   -1.94847700
H       1.48425500   -0.84865600    1.52728300
""",
)

entry(
    index = 33,
    label = "P19",
    molecule = 
"""
1  O u0 p2 c0 {3,S} {6,S}
2  O u0 p2 c0 {7,D}
3  C u0 p0 c0 {1,S} {4,D} {7,S}
4  C u0 p0 c0 {3,D} {5,S} {8,S}
5  C u0 p0 c0 {4,S} {6,D} {9,S}
6  C u0 p0 c0 {1,S} {5,D} {10,S}
7  C u0 p0 c0 {2,D} {3,S} {11,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9351,0.00379574,0.000123666,-2.22527e-07,1.24516e-10,-20888,10.7077], Tmin=(10,'K'), Tmax=(549.81,'K')),
            NASAPolynomial(coeffs=[-0.272837,0.0476545,-3.21255e-05,1.01922e-08,-1.22536e-12,-20625.5,26.6709], Tmin=(549.81,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-173.7,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 4, 'C-C': 2, 'C=C': 2, 'C-O': 2, 'C=O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for P19 exists which is 4.85 kJ/mol lower.


External symmetry: 1, optical isomers: 1

Geometry:
O       2.59778200   -1.36004800    0.23278500
C       2.03303600   -0.34913500   -0.12515900
C       0.59189600   -0.15694100   -0.04584200
C      -0.43261100   -0.95077100    0.39743700
C      -1.62815000   -0.20333000    0.21872900
C      -1.24900700    0.99272200   -0.32049700
O       0.09021700    1.04186100   -0.48889500
H       2.58274600    0.51735000   -0.54617300
H      -0.32028800   -1.94508600    0.79847500
H      -2.63525000   -0.50650600    0.45606300
H      -1.79535900    1.87001000   -0.62492000
""",
)

entry(
    index = 34,
    label = "P20",
    molecule = 
"""
1  O u0 p2 c0 {3,S} {12,S}
2  O u0 p2 c0 {4,D}
3  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
4  C u0 p0 c0 {2,D} {3,S} {5,S}
5  C u0 p0 c0 {4,S} {6,D} {9,S}
6  C u0 p0 c0 {5,D} {10,S} {11,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.62897,0.0319006,5.7872e-06,-2.8866e-08,1.33319e-11,-34553.2,10.4487], Tmin=(10,'K'), Tmax=(871.264,'K')),
            NASAPolynomial(coeffs=[4.70926,0.0374256,-2.17755e-05,6.03618e-09,-6.46057e-13,-35139.4,3.10201], Tmin=(871.264,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-287.322,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 2, 'C=C': 1, 'H-O': 1, 'C-O': 1, 'C=O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 25.52 kJ/mol
* Invalidated! pivots: [3, 5], dihedral: [2, 3, 5, 6], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [5, 6], dihedral: [3, 5, 6, 12], rotor symmetry: 1, max scan energy: 29.71 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C      -1.88642500    0.11800000   -0.28303500
C      -0.96923100    0.96560500    0.18211400
C       0.44129000    0.54786900    0.38405500
O       0.84996200   -0.57374700    0.14411900
C       1.40856400    1.59063100    0.91900800
O       2.70043800    1.07479800    1.06422100
H      -2.91763100    0.41450500   -0.43332300
H      -1.60901800   -0.90261700   -0.52323400
H      -1.22501800    1.99210600    0.42907400
H       1.01549900    1.95691400    1.88073700
H       1.39782600    2.44951200    0.22923100
H       2.63947500    0.15043500    0.77439700
""",
)

entry(
    index = 35,
    label = "P21",
    molecule = 
"""
multiplicity 3
1  O u0 p2 c0 {3,S} {4,S}
2  O u0 p2 c0 {7,S} {13,S}
3  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
4  C u0 p0 c0 {1,S} {6,D} {7,S}
5  C u1 p0 c0 {3,S} {6,S} {10,S}
6  C u0 p0 c0 {4,D} {5,S} {11,S}
7  C u1 p0 c0 {2,S} {4,S} {12,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87354,0.0081291,0.00017381,-3.75284e-07,2.48921e-10,2173.12,13.3409], Tmin=(10,'K'), Tmax=(488.22,'K')),
            NASAPolynomial(coeffs=[1.6369,0.050982,-3.32108e-05,1.03081e-08,-1.22041e-12,2099.19,19.534], Tmin=(488.22,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (18.0376,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 3, 'H-O': 1, 'C=C': 1, 'C-O': 3}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [8, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.77741200    0.02833300   -0.79726700
C      -1.99317800    0.33215900    0.28759000
C      -0.55980300    0.11840900    0.25298400
C       0.23675900   -0.86375400    0.84967600
C       1.55973900   -0.60883700    0.57302800
C       1.61411400    0.62592500   -0.27249100
O       0.23392800    1.03109700   -0.42525700
H      -2.27032400   -0.54494100   -1.38528500
H      -2.46016400    1.07237000    0.92586300
H      -0.15700600   -1.67855500    1.43939300
H       2.42420300   -1.17070400    0.89264800
H       2.16868600    1.45754900    0.18473000
H       2.03455700    0.46231000   -1.27538300
""",
)

entry(
    index = 36,
    label = "P22",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {4,S} {6,S} {7,S} {9,S}
2  C u0 p0 c0 {3,S} {8,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {5,D} {6,S}
4  C u1 p0 c0 {1,S} {5,S} {12,S}
5  C u0 p0 c0 {3,D} {4,S} {13,S}
6  O u0 p2 c0 {1,S} {3,S}
7  O u0 p2 c0 {1,S} {14,S}
8  O u0 p2 c0 {2,S} {15,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 O u1 p2 c0 {7,S}
15 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.58494,0.0487897,-7.40106e-06,-2.32306e-08,1.17245e-11,-16187.7,15.4515], Tmin=(10,'K'), Tmax=(969.485,'K')),
            NASAPolynomial(coeffs=[9.47722,0.0418385,-2.35051e-05,6.31307e-09,-6.56683e-13,-18146,-17.0002], Tmin=(969.485,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-134.57,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (353.365,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 3, 'C-O': 4, 'C=C': 1, 'H-O': 1, 'O-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[2, 3]]) broke during the scan.Bond ([[2, 3]]) broke during the scan. But unable to propose troubleshooting methods.
pivots: [6, 7], dihedral: [5, 6, 7, 8], rotor symmetry: 1, max scan energy: 12.84 kJ/mol
* Invalidated! pivots: [7, 8], dihedral: [6, 7, 8, 15], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       3.15383400    1.82502900    0.02666200
O       2.15878600    1.33554400    0.73628000
C       1.70769000    0.00844700    0.20359900
C       1.01829900   -0.74399600    1.27800300
C      -0.32536000   -0.78694300    0.95046700
C      -0.49217800   -0.18066800   -0.28600300
C      -1.67417400    0.12391000   -1.13330800
O      -1.95128100    1.52190700   -1.20365300
O       0.71701700    0.25194900   -0.78009400
H       2.60125700   -0.40413000   -0.26495200
H       1.50830600   -1.11692800    2.16279100
H      -1.12388900   -1.21489900    1.53749600
H      -1.51861800   -0.29353300   -2.13871800
H      -2.55840800   -0.34697200   -0.70286800
H      -1.16496400    1.95335600   -1.55557000
""",
)

entry(
    index = 37,
    label = "P23",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {4,D} {5,S} {6,S}
4  C u0 p0 c0 {1,S} {3,D} {11,S}
5  C u0 p0 c0 {3,S} {12,D} {13,S}
6  O u0 p2 c0 {2,S} {3,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 O u0 p2 c0 {5,D}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94624,0.0194866,4.91754e-05,-7.2826e-08,2.8148e-11,-25457.4,11.1162], Tmin=(10,'K'), Tmax=(914.307,'K')),
            NASAPolynomial(coeffs=[3.9343,0.041525,-2.30509e-05,6.13847e-09,-6.34791e-13,-26374.2,6.14717], Tmin=(914.307,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-211.594,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 6, 'C-C': 3, 'C=C': 1, 'C-O': 2, 'C=O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Inconsistent initial and final conformersInconsistent initial and final conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       3.05191800   -0.74919700   -0.38695100
C       2.32213800    0.19083100   -0.17411500
C       0.85533400    0.07787100   -0.04875100
C       0.08874500   -1.01561300   -0.12678200
C      -1.34338000   -0.62027100    0.13088100
C      -1.23992500    0.92471400    0.11437300
O       0.17685700    1.24373800    0.19661800
H       2.70932300    1.22276900   -0.05631000
H       0.45747300   -2.01549400   -0.29416900
H      -2.03649500   -0.99101300   -0.62918500
H      -1.69086600   -1.00646200    1.09710900
H      -1.73814600    1.41290200    0.95132200
H      -1.61809200    1.34525400   -0.82190700
""",
)

entry(
    index = 38,
    label = "P24",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {4,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {7,S} {9,S} {10,S}
3  C u0 p0 c0 {5,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {5,D} {14,S}
5  C u0 p0 c0 {3,S} {4,D} {13,S}
6  O u0 p2 c0 {1,S} {3,S}
7  O u0 p2 c0 {2,S} {15,S}
8  O u1 p2 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u1 p2 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.22428,0.0802485,-0.000180674,3.68015e-07,-3.13587e-10,-33575.6,15.8368], Tmin=(10,'K'), Tmax=(359.29,'K')),
            NASAPolynomial(coeffs=[4.1197,0.0582958,-3.89917e-05,1.22875e-08,-1.46893e-12,-33562.5,13.5099], Tmin=(359.29,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-279.166,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (357.522,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 3, 'C=C': 1, 'C-O': 5, 'H-O': 1}
1D rotors:
* Invalidated! pivots: [5, 7], dihedral: [4, 5, 7, 8], invalidation reason: Internal coordinate error; 
* Invalidated! pivots: [7, 8], dihedral: [5, 7, 8, 15], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformersSignificant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.02034500    1.40973900    1.08733600
C      -1.53026400    0.66289700    0.10101200
C      -1.38842300   -0.81548900    0.50270500
C      -0.67950200   -1.42706300   -0.43751600
C      -0.32523900   -0.46156400   -1.51337200
O       0.25050800   -0.63924900   -2.54199000
C       2.27542100    0.40775600    0.30079200
O       1.74441900    0.78551200    1.49480300
O      -0.83671700    0.77177700   -1.14198700
H      -2.58432800    0.93986900   -0.07266700
H      -1.79565500   -1.18934200    1.42921800
H      -0.39007100   -2.46620000   -0.48622200
H       2.07883800    1.00776600   -0.58076300
H       3.18713700   -0.16591600    0.39099600
H       0.96737200    1.34062800    1.33803400
""",
)

entry(
    index = 39,
    label = "P25",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
2  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {5,D} {6,S}
4  C u0 p0 c0 {1,S} {2,S} {11,D}
5  C u0 p0 c0 {2,S} {3,D} {12,S}
6  O u0 p2 c0 {3,S} {13,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 O u0 p2 c0 {4,D}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87647,0.0072779,0.00015815,-3.07004e-07,1.80271e-10,-33515.8,10.6484], Tmin=(10,'K'), Tmax=(560.199,'K')),
            NASAPolynomial(coeffs=[1.63948,0.0511828,-3.42023e-05,1.09113e-08,-1.32609e-12,-33703.5,16.2324], Tmin=(560.199,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-278.716,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 4, 'C=C': 1, 'H-O': 1, 'C-O': 1, 'C=O': 1}
1D rotors:
pivots: [5, 6], dihedral: [4, 5, 6, 11], rotor symmetry: 1, max scan energy: 22.70 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O      -1.82754200   -1.87569100   -0.23493500
C      -1.02484900   -0.98638400   -0.13532200
C      -1.32375400    0.51557600   -0.27252100
C       0.02051200    1.16154400   -0.05964400
C       0.97561400    0.25110100    0.16638700
O       2.30008200    0.42968100    0.40113300
C       0.47370200   -1.16071700    0.15083200
H      -2.08271100    0.80272300    0.46572700
H      -1.76442800    0.70856700   -1.25844300
H       0.17990100    2.23320400   -0.08874400
H       2.49956600    1.37328900    0.38642800
H       0.62746300   -1.67926600    1.10352500
H       0.94644300   -1.77362800   -0.62442000
""",
)

entry(
    index = 40,
    label = "P26",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {5,D} {6,S}
3  C u0 p0 c0 {1,S} {4,D} {9,S}
4  C u0 p0 c0 {2,S} {3,D} {10,S}
5  C u0 p0 c0 {2,D} {11,S} {12,S}
6  O u0 p2 c0 {1,S} {2,S}
7  O u0 p2 c0 {1,S} {13,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8764,0.00733916,0.000158964,-3.11739e-07,1.85152e-10,-26759,11.3808], Tmin=(10,'K'), Tmax=(553.354,'K')),
            NASAPolynomial(coeffs=[1.67863,0.0508469,-3.38477e-05,1.07598e-08,-1.30318e-12,-26938.6,16.8622], Tmin=(553.354,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-222.535,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 2, 'C=C': 2, 'H-O': 1, 'C-O': 3}
1D rotors:
pivots: [5, 6], dihedral: [4, 5, 6, 13], rotor symmetry: 1, max scan energy: 22.43 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       1.98688100   -0.89926500    0.72837000
C       0.87428000   -0.29566300    0.30123700
C      -0.06818800    0.53069500    1.05371400
C      -1.02579900    0.95369500    0.22582900
C      -0.78376800    0.38691900   -1.15088100
O      -1.82017900   -0.41039400   -1.64302000
O       0.43716000   -0.36835300   -1.00008000
H       2.59568200   -1.49017100    0.05811400
H       2.29500500   -0.79575700    1.75921300
H       0.03302600    0.73638200    2.10997500
H      -1.87718300    1.58000300    0.45105600
H      -0.61759800    1.14202200   -1.92340700
H      -2.02931600   -1.07011200   -0.97011800
""",
)

entry(
    index = 41,
    label = "P27",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {12,S}
2  O u0 p2 c0 {4,S} {13,S}
3  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
4  C u0 p0 c0 {2,S} {3,S} {5,D}
5  C u0 p0 c0 {4,D} {6,S} {9,S}
6  C u1 p0 c0 {5,S} {10,S} {11,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85658,0.009157,0.000173908,-3.8112e-07,2.53113e-10,-27446.8,12.2303], Tmin=(10,'K'), Tmax=(497.714,'K')),
            NASAPolynomial(coeffs=[2.43748,0.0490671,-3.22805e-05,1.01316e-08,-1.2109e-12,-27658.6,14.5396], Tmin=(497.714,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-228.243,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 2, 'H-O': 2, 'C=C': 1, 'C-O': 2}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [7, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [3, 4], dihedral: [2, 3, 4, 10], rotor symmetry: 1, max scan energy: 35.64 kJ/mol
* Invalidated! pivots: [3, 5], dihedral: [2, 3, 5, 6], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [5, 6], dihedral: [3, 5, 6, 13], invalidation reason: Another conformer for P27 exists which is 4.91 kJ/mol lower.
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
C       2.32419200   -0.59505800   -0.30538000
C       0.99908500   -0.44324200   -0.64932300
C       0.04375300    0.24564100    0.08805100
O       0.38989500    0.84654400    1.25900800
C      -1.36778000    0.48875800   -0.34966700
O      -2.26458100    0.43967900    0.77441500
H       3.00286900   -1.15247100   -0.93716300
H       2.71765600   -0.16141200    0.60464400
H       0.64317300   -0.88656200   -1.57552200
H      -0.43809500    1.10923800    1.68868900
H      -1.65715600   -0.21088100   -1.14046000
H      -1.48784300    1.50697700   -0.73866100
H      -2.29576200   -0.47366700    1.08244600
""",
)

entry(
    index = 42,
    label = "P28",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {6,D}
3  C u0 p0 c0 {4,D} {6,S} {10,S}
4  C u0 p0 c0 {3,D} {5,S} {11,S}
5  O u0 p2 c0 {2,S} {4,S}
6  C u1 p0 c0 {2,D} {3,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96242,0.00234372,0.000117341,-2.15214e-07,1.27739e-10,23048.4,10.9314], Tmin=(10,'K'), Tmax=(434.258,'K')),
            NASAPolynomial(coeffs=[-0.652308,0.0447709,-2.89348e-05,8.92355e-09,-1.05268e-12,23449.9,29.3542], Tmin=(434.258,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (191.624,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (253.591,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 2, 'C=C': 2, 'C-O': 2}
1D rotors:
pivots: [1, 2], dihedral: [7, 1, 2, 3], rotor symmetry: 3, max scan energy: 3.61 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       1.89903200    0.04919800    0.18452900
C       0.42732400    0.15825000    0.02707300
C      -0.65195700   -0.28796800    0.70570700
C      -1.85091700    0.13815500    0.06842300
C      -1.41099400    0.84817100   -1.00523200
O      -0.04557700    0.87667300   -1.05485100
H       2.36075800    1.03522200    0.29430000
H       2.35603300   -0.43827800   -0.68207300
H       2.12944800   -0.54000600    1.07261500
H      -2.87275800   -0.04808500    0.35443200
H      -1.91678700    1.37467500   -1.79736100
""",
)

entry(
    index = 43,
    label = "P29",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {5,S}
3  C u0 p0 c0 {2,D} {4,S} {10,S}
4  C u0 p0 c0 {3,S} {6,D} {11,S}
5  O u0 p2 c0 {2,S} {6,S}
6  C u1 p0 c0 {4,D} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96404,0.00233194,0.000124241,-2.38552e-07,1.49067e-10,22920.4,10.8135], Tmin=(10,'K'), Tmax=(412.011,'K')),
            NASAPolynomial(coeffs=[-0.362213,0.0443317,-2.86612e-05,8.84689e-09,-1.04474e-12,23276.9,27.8492], Tmin=(412.011,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (190.564,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (253.591,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 2, 'C=C': 2, 'C-O': 2}
1D rotors:
pivots: [1, 2], dihedral: [7, 1, 2, 3], rotor symmetry: 3, max scan energy: 4.48 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C      -1.73326600   -0.03756000    0.04691200
C      -0.25388200   -0.14844100   -0.00214100
C       0.77335100    0.74146600    0.02476400
C       2.00984000   -0.00565300   -0.05749900
C       1.59469700   -1.29028000   -0.12669500
O       0.27163500   -1.43456500   -0.09817600
H      -2.01776300    1.01337500    0.12126500
H      -2.19652300   -0.45553300   -0.85217300
H      -2.14638700   -0.56671800    0.91119500
H       0.67976500    1.81454600    0.09508600
H       3.01853100    0.36936200   -0.06253300
""",
)

entry(
    index = 44,
    label = "P30",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {3,S} {6,S}
2  C u0 p0 c0 {1,D} {5,S} {7,S}
3  C u0 p0 c0 {1,S} {8,D} {9,S}
4  C u0 p0 c0 {5,D} {10,S} {11,S}
5  C u1 p0 c0 {2,S} {4,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  O u0 p2 c0 {3,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8243,0.0142624,9.58273e-05,-2.05043e-07,1.28307e-10,19333.6,10.8506], Tmin=(10,'K'), Tmax=(522.258,'K')),
            NASAPolynomial(coeffs=[2.3081,0.0413833,-2.66096e-05,8.1072e-09,-9.43177e-13,19280.5,15.1556], Tmin=(522.258,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (160.719,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (253.591,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 2, 'C=C': 2, 'C=O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: not a torsional mode (angles = 179.89, 124.51 degrees)
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 66.36 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       2.14199600    0.31608800   -0.47675700
C       1.02488700   -0.33862300   -0.39999600
C      -0.12402700   -1.01458600   -0.32196600
C      -1.32721500   -0.48865000    0.19264200
C      -2.52877700   -1.29126800    0.24067800
O      -2.59513900   -2.45123900   -0.14809400
H       2.86495200    0.30565000    0.33592300
H       2.40037300    0.89979800   -1.35752200
H      -0.15670700   -2.04407800   -0.67419900
H      -1.36273500    0.53114600    0.56018300
H      -3.42121400   -0.78849600    0.66190800
""",
)

entry(
    index = 45,
    label = "P31",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,D} {5,S} {6,S}
2  C u0 p0 c0 {4,S} {5,D} {7,S}
3  C u0 p0 c0 {1,D} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {8,D} {11,S}
5  C u1 p0 c0 {1,S} {2,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  O u0 p2 c0 {4,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78789,0.0200424,5.2441e-05,-1.06687e-07,5.63814e-11,21506,13.219], Tmin=(10,'K'), Tmax=(657.778,'K')),
            NASAPolynomial(coeffs=[3.56331,0.0373359,-2.33171e-05,6.908e-09,-7.83573e-13,21190.9,11.5892], Tmin=(657.778,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (178.784,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (249.434,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 2, 'C=C': 2, 'C=O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 2, max scan energy: 0.03 kJ/mol (set as a FreeRotor)
Troubleshot with the following constraints and 8.0 degrees resolution:
D 1 1 2 3 F
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 36.46 kJ/mol
* Invalidated! pivots: [1, 2], dihedral: [7, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
C       2.04679600    0.23615500   -0.65266200
C       1.15883100   -0.83168600   -0.54398800
C       1.14852500   -1.93038300   -1.32181800
C       1.15174000   -3.01552600   -2.05201500
C       1.93742800   -4.22039400   -1.67711800
O       1.95673100   -5.23238400   -2.33477300
H       2.82337100    0.24606500   -1.40609500
H       1.97256400    1.07967200    0.01971100
H       0.39416900   -0.78919100    0.23122900
H       0.57883300   -3.09581000   -2.97601000
H       2.51383500   -4.12262800   -0.73454600
""",
)

entry(
    index = 46,
    label = "P114",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,D}
4  C u0 p0 c0 {2,S} {5,D} {11,S}
5  C u0 p0 c0 {3,S} {4,D} {12,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.0333,-0.00342451,0.000143804,-2.32286e-07,1.19202e-10,-13088.7,10.3095], Tmin=(10,'K'), Tmax=(603.029,'K')),
            NASAPolynomial(coeffs=[-1.18993,0.0489257,-3.04503e-05,9.04182e-09,-1.02879e-12,-12780.6,30.1978], Tmin=(603.029,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-108.84,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 6, 'C=C': 1, 'C-C': 4, 'C=O': 1}

External symmetry: 1, optical isomers: 1

Geometry:
O       0.36011700    2.22618700    1.15953300
C      -1.00383800    0.30941200    0.46803700
C      -0.59265100   -0.92699800   -0.35393100
C       0.26817700    1.16631200    0.58433400
C       0.87029600   -0.69986900   -0.65091600
C       1.34131300    0.44247500   -0.13925900
H      -0.73537500   -1.86491900    0.19348300
H      -1.78881100    0.90046600   -0.00927800
H      -1.35780400    0.05977600    1.47090500
H      -1.16512900   -1.02667000   -1.28240300
H       1.45344600   -1.41162100   -1.22497000
H       2.35025900    0.82544800   -0.21553400
""",
)

entry(
    index = 47,
    label = "P100",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {5,D} {15,S}
5  C u0 p0 c0 {3,S} {4,D} {14,S}
6  C u0 p0 c0 {2,S} {7,D} {13,S}
7  C u0 p0 c0 {6,D} {16,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78368,0.0310949,4.55411e-05,-7.43691e-08,2.92003e-11,23396,12.3095], Tmin=(10,'K'), Tmax=(911.285,'K')),
            NASAPolynomial(coeffs=[3.62098,0.0543468,-2.98302e-05,7.90975e-09,-8.17319e-13,22489.9,7.94474], Tmin=(911.285,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (194.572,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (399.095,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 10, 'C=C': 2, 'C-C': 5}
1D rotors:
pivots: [1, 2], dihedral: [3, 1, 2, 6], rotor symmetry: 1, max scan energy: 19.19 kJ/mol
pivots: [2, 6], dihedral: [1, 2, 6, 7], rotor symmetry: 1, max scan energy: 12.35 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -0.56654300   -0.68562400   -0.11437700
C       0.62355400   -0.30989100    0.77973400
C      -1.27286100    0.48723600   -0.89472200
C      -1.91592100   -0.88261800    0.56326600
C      -2.51399000    0.10724300   -0.10708300
C       1.86411300    0.01842200   -0.00247200
C       2.49900000    1.18688100    0.01545200
H      -0.28478600   -1.51489500   -0.77470800
H       0.34633800    0.53599300    1.41833600
H       0.83091900   -1.15692500    1.44809500
H      -1.33183200    0.35729400   -1.97973900
H      -0.85745000    1.47727500   -0.68493500
H       2.24886000   -0.77975100   -0.63670900
H      -3.52439900    0.50051600   -0.10959500
H      -2.25254300   -1.58689200    1.31661500
H       2.15338200    2.01187300    0.63157900
H       3.38914000    1.36136500   -0.57865600
""",
)

entry(
    index = 48,
    label = "P94",
    molecule = 
"""
multiplicity 3
1  O u0 p2 c0 {4,S} {11,S}
2  C u0 p0 c0 {3,D} {4,S} {6,S}
3  C u0 p0 c0 {2,D} {5,S} {7,S}
4  C u1 p0 c0 {1,S} {2,S} {8,S}
5  C u1 p0 c0 {3,S} {9,S} {10,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90375,0.00568644,0.000130956,-2.52647e-07,1.4805e-10,17684.2,9.61141], Tmin=(10,'K'), Tmax=(555.423,'K')),
            NASAPolynomial(coeffs=[1.58864,0.0437543,-2.96331e-05,9.45876e-09,-1.14291e-12,17611.4,16.4483], Tmin=(555.423,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (146.996,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (253.591,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-O': 1, 'C=C': 1, 'C-C': 2, 'H-O': 1}
1D rotors:
pivots: [1, 4], dihedral: [11, 1, 4, 2], rotor symmetry: 2, max scan energy: 34.95 kJ/mol
* Invalidated! pivots: [2, 4], dihedral: [3, 2, 4, 1], invalidation reason: Another conformer for C4H6O[125] exists which is 9.40 kJ/mol lower.Another conformer for C4H6O[125] exists which is 9.40 kJ/mol lower.
* Invalidated! pivots: [3, 5], dihedral: [2, 3, 5, 9], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 3], dihedral: [4, 2, 3, 5], invalidation reason: 


External symmetry: 1, optical isomers: 1

Geometry:
O      -1.92151100    0.94766400    0.83942200
C       0.08723700    1.21041500   -0.51152800
C       1.03937100    0.68668200    0.35570400
C      -1.27425700    1.32881000   -0.28535600
C       0.78311000    0.15141100    1.69488200
H       0.42896400    1.57114700   -1.47628500
H       2.07408100    0.67045300    0.01231200
H      -1.94645200    1.75134100   -1.02034300
H       0.69310400   -0.92109700    1.86171500
H       0.95884500    0.75663200    2.58315600
H      -1.26804500    0.57736700    1.45983500
""",
)

entry(
    index = 49,
    label = "P93",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  C u1 p0 c0 {3,S} {5,S} {10,S}
5  O u0 p2 c0 {1,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.09242,-0.00858824,0.000113279,-4.51083e-08,-1.69923e-10,4120.61,9.64582], Tmin=(10,'K'), Tmax=(303.456,'K')),
            NASAPolynomial(coeffs=[-1.72413,0.0441981,-2.95842e-05,9.37692e-09,-1.12688e-12,4583.59,32.583], Tmin=(303.456,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (34.2688,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-O': 2, 'C=C': 1, 'C-C': 2}

External symmetry: 1, optical isomers: 1

Geometry:
O      -1.01495900   -0.92420200    0.09282600
C      -1.04662400    0.51074900   -0.12701000
C       0.39221400    0.92758100   -0.12267000
C       1.15148300   -0.21187900    0.08647200
C       0.29328800   -1.28987400    0.21008200
H      -1.56775000    0.69505400   -1.07733700
H      -1.65022000    0.96149600    0.67371600
H       0.73823400    1.94007400   -0.26043500
H       2.22831000   -0.27024800    0.14606900
H       0.47602400   -2.33875300    0.37828700
""",
)

entry(
    index = 50,
    label = "P108",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {7,S} {14,D}
5  C u0 p0 c0 {2,S} {7,D} {15,S}
6  C u0 p0 c0 {3,S} {8,D} {16,S}
7  C u0 p0 c0 {4,S} {5,D} {17,S}
8  C u0 p0 c0 {6,D} {18,S} {19,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.57382,0.0405722,6.43997e-05,-1.29447e-07,6.28159e-11,-7857.05,13.6233], Tmin=(10,'K'), Tmax=(722.711,'K')),
            NASAPolynomial(coeffs=[2.80165,0.0679701,-4.04597e-05,1.15537e-08,-1.27376e-12,-8349.34,12.9198], Tmin=(722.711,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-65.3622,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (448.981,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 10, 'C-C': 6, 'C=O': 1, 'C=C': 2}
1D rotors:
pivots: [2, 4], dihedral: [3, 2, 4, 7], rotor symmetry: 1, max scan energy: 23.34 kJ/mol
pivots: [4, 7], dihedral: [2, 4, 7, 9], rotor symmetry: 1, max scan energy: 21.38 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.83521700   -2.30614300   -0.36618700
C      -0.34965100   -0.48147500    0.32079400
C      -0.69238700    1.01358100    0.48774000
C       0.76685200   -0.83296700   -0.68491200
C      -1.69560300   -1.15113000   -0.02866700
C      -2.19679200    1.06316300    0.40034700
C       0.50788100   -0.34385500   -2.08255200
C      -2.74906000   -0.12301200    0.11835400
C       1.27324400    0.51950200   -2.74491800
H      -0.05945400   -0.89799100    1.29250800
H      -0.24936700    1.62180100   -0.30936900
H      -0.33325200    1.43045300    1.43443800
H       1.72173400   -0.43892800   -0.32310200
H       0.84654800   -1.92582700   -0.69802800
H      -2.74866000    1.98625900    0.54110500
H      -0.37597100   -0.75015800   -2.57074300
H      -3.80033700   -0.33917900   -0.01850200
H       1.04029100    0.82578800   -3.75864600
H       2.17057800    0.94177800   -2.30137300
""",
)

entry(
    index = 51,
    label = "P112",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,D} {6,S}
3  C u0 p0 c0 {1,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {6,S} {10,S}
5  C u0 p0 c0 {2,D} {11,S} {12,S}
6  O u0 p2 c0 {2,S} {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.08026,-0.00766857,0.000176305,-2.97627e-07,1.60017e-10,-2006.16,10.0412], Tmin=(10,'K'), Tmax=(589.291,'K')),
            NASAPolynomial(coeffs=[-0.43621,0.0482877,-3.05256e-05,9.21423e-09,-1.06379e-12,-1913.13,25.7149], Tmin=(589.291,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-16.6978,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 6, 'C-O': 2, 'C=C': 2, 'C-C': 2}

External symmetry: 1, optical isomers: 1

Geometry:
O      -0.23594000   -1.34686100   -0.22230900
C      -0.08575700    0.98950500    0.14287800
C       0.67693700   -0.31929700    0.00513500
C      -1.51223600    0.52710600   -0.03962700
C      -1.49606900   -0.78626200   -0.23697600
C       1.98028700   -0.56628100    0.07064000
H       0.22439400    1.71669100   -0.61571800
H       0.08742500    1.45421300    1.11987100
H      -2.38763700    1.15642500   -0.01353900
H      -2.29427800   -1.49252400   -0.40677900
H       2.36221100   -1.57083300   -0.05114000
H       2.68066400    0.23811800    0.24756400
""",
)

entry(
    index = 52,
    label = "P92",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {4,S} {9,D} {10,S}
4  C u1 p0 c0 {2,D} {3,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65113,0.0336998,-6.41604e-05,1.30842e-07,-1.01309e-10,14498.6,10.9842], Tmin=(10,'K'), Tmax=(461.058,'K')),
            NASAPolynomial(coeffs=[2.28975,0.0326875,-1.91481e-05,5.43319e-09,-5.98853e-13,14760.4,17.9761], Tmin=(461.058,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (120.538,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (228.648,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C=C': 1, 'C-C': 2, 'C=O': 1}
1D rotors:
pivots: [2, 3], dihedral: [6, 2, 3, 5], rotor symmetry: 3, max scan energy: 6.30 kJ/mol
* Invalidated! pivots: [4, 5], dihedral: [1, 4, 5, 3], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.35518400    0.09169200    3.92290200
C      -1.58322800    0.12747600   -0.46134600
C      -0.33873200    0.04372800    0.39464400
C      -0.23857100   -0.70375500    2.97843600
C      -0.29377900   -0.32436100    1.63702100
H      -1.72187000    1.15127700   -0.82087200
H      -2.47206200   -0.16991500    0.09475400
H      -1.48327500   -0.51895700   -1.33829300
H       0.59934700    0.32769500   -0.08971700
H      -0.08115300   -1.78171300    3.16247800
""",
)

entry(
    index = 53,
    label = "P113",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {5,D} {6,S}
3  C u0 p0 c0 {1,S} {4,D} {9,S}
4  C u0 p0 c0 {2,S} {3,D} {10,S}
5  C u0 p0 c0 {2,D} {11,S} {12,S}
6  O u0 p2 c0 {1,S} {2,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.07992,-0.00756631,0.000173546,-2.91314e-07,1.55979e-10,-3269.15,9.91461], Tmin=(10,'K'), Tmax=(589.306,'K')),
            NASAPolynomial(coeffs=[-0.596111,0.0483757,-3.04515e-05,9.15534e-09,-1.0537e-12,-3138.28,26.4353], Tmin=(589.306,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-27.1977,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 6, 'C-O': 2, 'C=C': 2, 'C-C': 2}

External symmetry: 1, optical isomers: 1

Geometry:
O      -0.08560200   -1.18896400    0.25329400
C      -1.42403100   -0.66811500    0.26335500
C       0.79910000   -0.17423600   -0.03427000
C      -1.26539000    0.78998800   -0.05199600
C       0.03197600    1.05536200   -0.22096100
C       2.12033100   -0.36725200   -0.11058300
H      -2.02276800   -1.20671100   -0.48209500
H      -1.87047200   -0.84879900    1.24941400
H      -2.09316700    1.48199200   -0.12222900
H       0.48235700    2.00855500   -0.45760500
H       2.77396900    0.46223600   -0.33953400
H       2.55369600   -1.34405700    0.05321100
""",
)

entry(
    index = 54,
    label = "P102",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {3,S} {6,D}
5  C u0 p0 c0 {2,S} {7,D} {15,S}
6  C u0 p0 c0 {4,D} {7,S} {17,S}
7  C u0 p0 c0 {5,D} {6,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93376,0.00419401,0.000189876,-3.57431e-07,2.19922e-10,6084.04,11.6125], Tmin=(10,'K'), Tmax=(417.491,'K')),
            NASAPolynomial(coeffs=[-2.79698,0.0686647,-4.16994e-05,1.22614e-08,-1.39705e-12,6646.2,38.2069], Tmin=(417.491,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (50.5662,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (403.252,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 10, 'C=C': 2, 'C-C': 5}
1D rotors:
pivots: [3, 4], dihedral: [12, 3, 4, 1], rotor symmetry: 3, max scan energy: 9.27 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -0.12887300    1.33233700   -0.73521300
C      -1.60982400    0.92386700   -0.71491000
C       2.20327700    0.22349800   -0.72695100
C       0.78861300    0.23584800   -0.22777500
C      -1.97238600    0.20252500    0.56020800
C       0.32394100   -0.61559000    0.70157900
C      -1.05061900   -0.52966100    1.19930700
H      -2.24217800    1.80453600   -0.85942900
H      -1.81914300    0.25608000   -1.56535600
H       0.01970400    2.21835400   -0.09793000
H       0.16136900    1.63569900   -1.74605900
H       2.69133600    1.18895200   -0.54181900
H       2.79658500   -0.55569400   -0.24377900
H       2.24055300    0.06044600   -1.81063100
H      -2.99866700    0.23832800    0.91062500
H      -1.31259100   -1.09152400    2.09018500
H       0.97853100   -1.37390500    1.12125700
""",
)

entry(
    index = 55,
    label = "P99",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {6,D}
4  C u1 p0 c0 {1,S} {3,S} {14,S}
5  C u0 p0 c0 {1,S} {7,D} {13,S}
6  C u0 p0 c0 {3,D} {7,S} {15,S}
7  C u0 p0 c0 {5,D} {6,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94121,0.00375098,0.000183746,-3.47632e-07,2.14469e-10,17938.7,11.9931], Tmin=(10,'K'), Tmax=(417.157,'K')),
            NASAPolynomial(coeffs=[-2.5863,0.0663683,-4.15083e-05,1.25056e-08,-1.45196e-12,18483.1,37.7748], Tmin=(417.157,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (149.136,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (378.308,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 9, 'C=C': 2, 'C-C': 5}
1D rotors:
pivots: [2, 3], dihedral: [10, 2, 3, 4], rotor symmetry: 3, max scan energy: 3.42 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       1.34536000   -0.84796500   -0.80285600
C      -2.33891900    0.14622900    0.06131800
C      -0.82947500    0.09405400    0.05214700
C      -0.15254200   -0.76474000   -0.76321700
C       2.02467300    0.10112800    0.13747400
C      -0.10277700    0.96487300    0.91777600
C       1.31116600    0.94444400    0.93680300
H       1.70404900   -0.67754900   -1.83428600
H       1.66991100   -1.88334100   -0.59259300
H      -2.73347600   -0.08179500    1.05675600
H      -2.69874900    1.14491800   -0.20647200
H      -2.76814000   -0.56791700   -0.64398400
H       3.10902100    0.10039200    0.16656500
H      -0.70426600   -1.42816000   -1.42263000
H      -0.64159000    1.64711200    1.56548800
H       1.83651000    1.61879000    1.60609900
""",
)

entry(
    index = 56,
    label = "P103",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {5,D} {7,S}
5  C u0 p0 c0 {2,S} {4,D} {16,S}
6  C u0 p0 c0 {1,S} {7,D} {15,S}
7  C u0 p0 c0 {4,S} {6,D} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.932,0.00431831,0.000189824,-3.59602e-07,2.22938e-10,6411.5,11.6768], Tmin=(10,'K'), Tmax=(414.173,'K')),
            NASAPolynomial(coeffs=[-2.66672,0.0680504,-4.1004e-05,1.19628e-08,-1.35342e-12,6958.07,37.6949], Tmin=(414.173,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (53.2883,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (403.252,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 10, 'C=C': 2, 'C-C': 5}
1D rotors:
pivots: [3, 4], dihedral: [12, 3, 4, 5], rotor symmetry: 3, max scan energy: 7.78 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -1.88307700   -0.46460200    0.23561600
C      -1.32376000    0.91457600    0.61638300
C       2.44423800    0.01331000    0.17085100
C       0.94164500    0.04095700    0.07660400
C       0.17659500    0.88406900    0.78752500
C      -1.02404100   -1.13530600   -0.80822200
C       0.29173000   -0.89401800   -0.85947400
H      -1.91663700   -1.11018400    1.12715500
H      -2.91592500   -0.37145100   -0.11178500
H      -1.57415600    1.64150600   -0.17232000
H      -1.80860500    1.27697900    1.52734200
H       2.80340000   -0.97364600    0.48331100
H       2.90215600    0.22298700   -0.80272900
H       2.81384800    0.75140100    0.88536700
H      -1.48103700   -1.85617200   -1.47888500
H       0.63538100    1.60565300    1.45750200
H       0.91696600   -1.40810600   -1.58403500
""",
)

entry(
    index = 57,
    label = "P105",
    molecule = 
"""
multiplicity 3
1  O u1 p2 c0 {8,S}
2  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {5,S} {7,S} {8,D}
4  C u0 p0 c0 {2,S} {6,D} {13,S}
5  C u1 p0 c0 {3,S} {6,S} {14,S}
6  C u0 p0 c0 {4,D} {5,S} {16,S}
7  C u0 p0 c0 {3,S} {9,D} {15,S}
8  C u0 p0 c0 {1,S} {3,D} {17,S}
9  C u0 p0 c0 {7,D} {18,S} {19,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.21668,0.0801803,-0.000158581,3.49405e-07,-3.06406e-10,19424.2,15.7697], Tmin=(10,'K'), Tmax=(394.567,'K')),
            NASAPolynomial(coeffs=[1.66447,0.0732588,-4.61332e-05,1.38767e-08,-1.60185e-12,19723,24.0497], Tmin=(394.567,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (161.485,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (444.824,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 10, 'C-O': 1, 'C=C': 3, 'C-C': 4}
1D rotors:
pivots: [2, 4], dihedral: [10, 2, 4, 6], rotor symmetry: 3, max scan energy: 4.83 kJ/mol
pivots: [3, 5], dihedral: [7, 3, 5, 6], rotor symmetry: 1, max scan energy: 22.60 kJ/mol
pivots: [3, 7], dihedral: [5, 3, 7, 9], rotor symmetry: 1, max scan energy: 61.00 kJ/mol
* Invalidated! pivots: [5, 6], dihedral: [3, 5, 6, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 8], dihedral: [5, 3, 8, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 6], dihedral: [2, 4, 6, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [7, 9], dihedral: [3, 7, 9, 18], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       3.88122200    0.14425400   -0.07187200
C      -2.76095800   -1.84168000    0.72535000
C       1.55831000    0.63839100   -0.24697600
C      -1.82982100   -0.69108900    0.92045400
C       0.25777000    0.52132500    0.43960400
C      -0.61758200   -0.54318900    0.26873800
C       1.71398700    1.28154900   -1.49660400
C       2.75535100    0.08870600    0.39869300
C       0.70632800    1.84213200   -2.22541000
H      -3.74485200   -1.50524000    0.37477500
H      -2.93892300   -2.37564700    1.66734000
H      -2.37154700   -2.55939200   -0.00046700
H      -2.13224400    0.07934900    1.62660200
H      -0.01330600    1.31235500    1.13828000
H       2.73174600    1.31270800   -1.87520200
H      -0.32586600   -1.32189500   -0.43498900
H       2.57526300   -0.40333700    1.37445600
H      -0.32086900    1.82505700   -1.88021800
H       0.90657600    2.31999800   -3.17656000
""",
)

entry(
    index = 58,
    label = "P106",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {6,D} {7,S} {8,S}
5  C u0 p0 c0 {1,S} {7,D} {16,S}
6  C u0 p0 c0 {2,S} {4,D} {15,S}
7  C u0 p0 c0 {4,S} {5,D} {17,S}
8  C u0 p0 c0 {4,S} {18,D} {19,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 O u0 p2 c0 {8,D}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73809,0.0251912,0.00013137,-2.33566e-07,1.18645e-10,-9032.78,12.7028], Tmin=(10,'K'), Tmax=(650.568,'K')),
            NASAPolynomial(coeffs=[0.352641,0.0738784,-4.51504e-05,1.31765e-08,-1.4791e-12,-9182.11,23.0471], Tmin=(650.568,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-75.1385,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (448.981,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 10, 'C-C': 6, 'C=O': 1, 'C=C': 2}
1D rotors:
pivots: [2, 4], dihedral: [3, 2, 4, 13], rotor symmetry: 3, max scan energy: 14.55 kJ/mol
pivots: [5, 9], dihedral: [7, 5, 9, 1], rotor symmetry: 1, max scan energy: 46.29 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       3.52297500   -0.13817500    1.05898800
C      -1.25375000    0.57275800   -0.63991400
C      -0.56197800   -0.47406100   -1.54281800
C      -2.12083600   -0.08443200    0.45371400
C       1.46469500   -0.24440800   -0.13618200
C      -0.23527400    1.49573400   -0.00220900
C       0.71642400   -1.00336100   -0.96037700
C       1.01658800    1.09813500    0.25040300
C       2.75793100   -0.75787000    0.35463300
H      -1.91928100    1.16814400   -1.27371900
H      -1.25343000   -1.29151200   -1.77054900
H      -0.31255600   -0.01392000   -2.51153200
H      -1.51352200   -0.71786600    1.10562800
H      -2.90678600   -0.70172000    0.00744400
H      -2.60139900    0.67326400    1.07823900
H       1.06558800   -1.98894200   -1.25782200
H      -0.57565600    2.47493000    0.32125000
H       1.72870600    1.72936400    0.76835100
H       2.99831800   -1.79032800    0.01832000
""",
)

entry(
    index = 59,
    label = "P101",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,D} {10,S}
3  C u0 p0 c0 {1,S} {6,D} {11,S}
4  C u0 p0 c0 {2,D} {5,S} {13,S}
5  C u0 p0 c0 {4,S} {7,D} {12,S}
6  C u0 p0 c0 {3,D} {16,S} {17,S}
7  C u0 p0 c0 {5,D} {14,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72565,0.0437831,4.79212e-06,-2.69005e-08,1.03969e-11,17434.6,11.6035], Tmin=(10,'K'), Tmax=(1110.02,'K')),
            NASAPolynomial(coeffs=[9.30956,0.0436054,-2.1919e-05,5.32865e-09,-5.07409e-13,14966.2,-21.453], Tmin=(1110.02,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (145.014,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (399.095,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 10, 'C=C': 3, 'C-C': 3}
1D rotors:
pivots: [1, 2], dihedral: [3, 1, 2, 4], rotor symmetry: 1, max scan energy: 12.03 kJ/mol
* Invalidated! pivots: [1, 3], dihedral: [2, 1, 3, 6], invalidation reason: Another conformer for C7H10[276] exists which is 2.48 kJ/mol lower.Another conformer for C7H10[276] exists which is 2.48 kJ/mol lower.
pivots: [4, 5], dihedral: [2, 4, 5, 7], rotor symmetry: 1, max scan energy: 30.48 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       0.98926000    0.46481200    0.16140800
C      -0.34703500   -0.04555400    0.63198600
C       2.12361500   -0.44543400    0.56724700
C      -1.15977700    0.59202800    1.48497700
C      -2.44419700    0.07803900    1.93445200
C       2.92340500   -1.09129300   -0.27565700
C      -3.26151200    0.71375400    2.78099000
H       1.15661800    1.46730100    0.57293600
H       0.98557000    0.56181100   -0.93125700
H      -0.64552600   -1.01869100    0.24502500
H       2.26046500   -0.57301100    1.63938900
H      -2.73848300   -0.89297500    1.54083300
H      -0.86040400    1.56302100    1.87776900
H      -4.20936700    0.28656600    3.08516300
H      -3.00506800    1.68358900    3.19586600
H       2.81383900   -0.99364900   -1.35186000
H       3.71904200   -1.73777800    0.07723200
""",
)

entry(
    index = 60,
    label = "P104",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,D} {14,S}
4  C u0 p0 c0 {2,S} {8,D} {13,S}
5  C u0 p0 c0 {3,D} {6,S} {15,S}
6  C u0 p0 c0 {5,S} {7,D} {16,S}
7  C u0 p0 c0 {6,D} {9,S} {17,S}
8  C u0 p0 c0 {4,D} {18,S} {19,S}
9  O u0 p2 c0 {1,S} {7,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61559,0.0428786,4.13559e-05,-8.29853e-08,3.56288e-11,2525.52,12.8759], Tmin=(10,'K'), Tmax=(854.532,'K')),
            NASAPolynomial(coeffs=[4.37142,0.0631072,-3.5871e-05,9.81064e-09,-1.04121e-12,1528.59,4.27093], Tmin=(854.532,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (21.0115,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (448.981,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 4, 'C-H': 10, 'C=C': 3, 'C-O': 2}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 5], rotor symmetry: 1, max scan energy: 24.22 kJ/mol
pivots: [3, 5], dihedral: [2, 3, 5, 9], rotor symmetry: 1, max scan energy: 12.61 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       0.74576700    1.23368000   -0.46508600
C       0.04617900    0.00539300   -0.82198800
C      -0.94277400   -0.36900000    0.30481600
C       1.01161300   -1.11290800   -1.12522300
C      -1.98713900    0.68001300    0.55874100
C       2.21062700   -1.13412800   -0.52953100
C       2.62221700   -0.01164300    0.30066600
C       1.88976400    1.11229600    0.25085500
C      -3.29997800    0.48033400    0.48530200
H      -0.52290400    0.28130700   -1.71254000
H      -1.41707100   -1.31879800    0.03522900
H      -0.35401000   -0.55191000    1.21192800
H      -1.61125700    1.66917100    0.80819800
H       0.68648600   -1.89422800   -1.80264600
H       2.90573200   -1.94836600   -0.70301000
H       3.54039300   -0.03371300    0.87086200
H       2.16924900    2.04726700    0.72177300
H      -3.71679100   -0.49189900    0.23793600
H      -4.00807200    1.27919800    0.67533000
""",
)

entry(
    index = 61,
    label = "P97",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {4,S} {15,S}
2  O u0 p2 c0 {5,S} {14,S}
3  O u0 p2 c0 {8,D}
4  C u0 p0 c0 {1,S} {6,S} {7,S} {9,S}
5  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
6  C u1 p0 c0 {4,S} {5,S} {12,S}
7  C u0 p0 c0 {4,S} {8,D} {13,S}
8  C u0 p0 c0 {3,D} {7,D}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9403,0.00935302,0.000820853,-6.76941e-06,2.00766e-08,-32912,6.87234], Tmin=(10,'K'), Tmax=(84.4861,'K')),
            NASAPolynomial(coeffs=[2.91966,0.0577032,-3.80632e-05,1.20205e-08,-1.44921e-12,-32894.8,9.27361], Tmin=(84.4861,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-258.794,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (357.522,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-O': 2, 'C=C': 1, 'C=O': 1, 'C-C': 3, 'H-O': 2}
1D rotors:
* Invalidated! pivots: [1, 4], dihedral: [15, 1, 4, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 5], dihedral: [14, 2, 5, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 6], dihedral: [1, 4, 6, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 7], dihedral: [1, 4, 7, 8], invalidation reason: Another conformer for C5H7O3[59] exists which is 3.61 kJ/mol lower.Another conformer for C5H7O3[59] exists which is 3.61 kJ/mol lower.
* Invalidated! pivots: [5, 6], dihedral: [2, 5, 6, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       1.95156500   -0.05628700   -1.37584500
O       0.09441200    2.02947900   -1.91185200
O      -1.44050900    0.64887200    1.30021200
C       0.76458300   -0.76811000   -1.06175900
C      -0.33829600    0.90277900   -2.71257400
C      -0.40431800   -0.34864500   -1.91105000
C       0.44102100   -0.70711400    0.43433100
C      -0.54791700    0.01246900    0.90608500
H       1.00469000   -1.81577700   -1.28302400
H      -1.29805700    1.11472800   -3.19539500
H       0.42242100    0.83183300   -3.49747600
H      -1.27480500   -0.99393600   -1.95711200
H       1.10826800   -1.18396400    1.14152800
H      -0.57915100    2.18722200   -1.24017000
H       1.73976500    0.88560700   -1.29205700
""",
)

entry(
    index = 62,
    label = "P111",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {8,S}
3  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
4  C u1 p0 c0 {1,S} {2,S} {11,S}
5  O u0 p2 c0 {2,S} {12,S}
6  O u0 p2 c0 {3,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88907,0.00676092,0.000156566,-3.1264e-07,1.91633e-10,-7739.66,11.7133], Tmin=(10,'K'), Tmax=(528.258,'K')),
            NASAPolynomial(coeffs=[1.3972,0.0493341,-3.16317e-05,9.81243e-09,-1.16975e-12,-7807.13,19.0143], Tmin=(528.258,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-64.3898,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-O': 2, 'C-C': 4, 'H-O': 2}
1D rotors:
* Invalidated! pivots: [1, 4], dihedral: [12, 1, 4, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 5], dihedral: [13, 2, 5, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 5], dihedral: [4, 3, 5, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       1.15891800    1.43308200    0.29098600
O       2.12419700    0.37726700   -2.12841200
C       0.98135200   -1.01188800   -0.43986400
C       1.06285800    0.08030900    0.63892700
C       1.09856100   -0.59730200   -1.90410400
C       2.14854700   -0.89625400    0.46296500
H       0.29372500   -1.84622600   -0.29141400
H       0.43095500   -0.02072600    1.51793300
H       0.17155800   -0.12481100   -2.23603800
H       1.26900700   -1.48311500   -2.52880000
H       2.68418300   -1.58500000    1.10278100
H       1.64080700    1.47743200   -0.54943400
H       2.96289300   -0.02521400   -1.87309300
""",
)

entry(
    index = 63,
    label = "P91",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
3 C u0 p0 c0 {1,D} {5,S} {9,S}
4 C u0 p0 c0 {2,S} {5,T}
5 C u0 p0 c0 {3,S} {4,T}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70471,0.029885,-6.79648e-05,1.53189e-07,-1.25108e-10,7842.64,10.3034], Tmin=(10,'K'), Tmax=(439.29,'K')),
            NASAPolynomial(coeffs=[2.37799,0.0283827,-1.64549e-05,4.63111e-09,-5.07183e-13,8090.26,17.1044], Tmin=(439.29,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (65.2,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (203.705,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 4, 'C#C': 1, 'C-C': 2, 'C=O': 1}
1D rotors:
* Invalidated! pivots: [2, 4], dihedral: [6, 2, 4, 5], invalidation reason: 
pivots: [3, 5], dihedral: [1, 3, 5, 4], rotor symmetry: 2, max scan energy: 0.05 kJ/mol (set as a FreeRotor)


External symmetry: 1, optical isomers: 1

Geometry:
O       2.90104600   -1.04348300    0.52431400
C      -1.78198500   -0.01689900   -0.48709600
C       2.23172900   -0.04878800    0.36351900
C      -0.36038000   -0.02812000   -0.18582100
C       0.82008100   -0.05540400    0.06469400
H      -2.16104600    1.00342000   -0.58694600
H      -2.34549300   -0.51697400    0.30591700
H      -1.97967300   -0.55011400   -1.42148800
H       2.67708000    0.96262200    0.43846200
""",
)

entry(
    index = 64,
    label = "P98",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {14,S}
2  O u0 p2 c0 {5,S} {15,S}
3  O u0 p2 c0 {8,S} {16,S}
4  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
5  C u0 p0 c0 {2,S} {4,S} {6,D}
6  C u0 p0 c0 {5,D} {7,S} {11,S}
7  C u0 p0 c0 {6,S} {8,D} {12,S}
8  C u0 p0 c0 {3,S} {7,D} {13,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72408,0.018506,0.000247428,-6.09945e-07,4.41e-10,-54708.1,13.2132], Tmin=(10,'K'), Tmax=(474.391,'K')),
            NASAPolynomial(coeffs=[4.39693,0.0615112,-4.24722e-05,1.37593e-08,-1.67797e-12,-55319.6,4.69564], Tmin=(474.391,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-454.918,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (369.994,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-O': 3, 'C=C': 2, 'C-C': 2, 'H-O': 3}
1D rotors:
* Invalidated! pivots: [1, 4], dihedral: [14, 1, 4, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [2, 5], dihedral: [15, 2, 5, 4], rotor symmetry: 1, max scan energy: 31.03 kJ/mol
pivots: [3, 8], dihedral: [16, 3, 8, 7], rotor symmetry: 1, max scan energy: 22.49 kJ/mol
* Invalidated! pivots: [4, 5], dihedral: [1, 4, 5, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [6, 7], dihedral: [5, 6, 7, 8], rotor symmetry: 1, max scan energy: 31.44 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -3.39006200    0.59979500   -0.50681400
O      -1.15849400    2.03081000   -1.19751600
O       2.35777000    4.20703400    1.90084400
C      -2.13253400    0.25067800    0.09736000
C      -1.17268100    1.40262600    0.02080600
C      -0.35051100    1.78166100    1.01346800
C       0.61260500    2.85877200    0.92007500
C       1.43468900    3.20683000    1.92076600
H      -1.77088000   -0.59017900   -0.50305900
H      -2.25306500   -0.09037800    1.13019000
H      -0.40717000    1.22493600    1.94352900
H       0.65462400    3.40193100   -0.02108700
H       1.43955400    2.69940500    2.87933900
H      -3.80645100    1.26535400    0.05291900
H      -1.98514300    1.78786900   -1.63858000
H       2.33470500    4.63748500    1.03796100
""",
)

entry(
    index = 65,
    label = "P96",
    molecule = 
"""
multiplicity 3
1  O u0 p2 c0 {6,S} {13,S}
2  O u1 p2 c0 {4,S}
3  C u0 p0 c0 {4,S} {5,D} {8,S}
4  C u0 p0 c0 {2,S} {3,S} {6,D}
5  C u0 p0 c0 {3,D} {7,S} {9,S}
6  C u0 p0 c0 {1,S} {4,D} {10,S}
7  C u1 p0 c0 {5,S} {11,S} {12,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85574,0.0110415,0.000214118,-5.94082e-07,5.16299e-10,-7391.88,12.2981], Tmin=(10,'K'), Tmax=(369.204,'K')),
            NASAPolynomial(coeffs=[2.32949,0.0494809,-3.10442e-05,9.29341e-09,-1.0737e-12,-7428.47,16.1188], Tmin=(369.204,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-61.4411,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-O': 2, 'C=C': 2, 'C-C': 2, 'H-O': 1}
1D rotors:
pivots: [1, 6], dihedral: [13, 1, 6, 4], rotor symmetry: 1, max scan energy: 63.05 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [5, 3, 4, 2], invalidation reason: Another conformer for C5H6O2[120] exists which is 8.12 kJ/mol lower.Another conformer for C5H6O2[120] exists which is 8.12 kJ/mol lower.
* Invalidated! pivots: [5, 7], dihedral: [3, 5, 7, 11], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 6], dihedral: [2, 4, 6, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 5], dihedral: [4, 3, 5, 7], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
O       3.26055000   -0.67229100    0.19842500
O       1.26027500    0.27039300   -1.21942600
C      -0.36411700    0.10000500    0.51415800
C       0.98446300   -0.04746100   -0.03445800
C      -1.41703700    0.59954800   -0.24246400
C       2.05750900   -0.56536800    0.76375300
C      -2.70475000    0.76041400    0.21957700
H      -0.53165300   -0.19451700    1.54667400
H      -1.18375000    0.87558500   -1.26691100
H       1.99438800   -0.88452100    1.79448100
H      -2.97696100    0.49644400    1.23578300
H      -3.48557500    1.15549200   -0.41742800
H       3.13177900   -0.34453500   -0.71606900
""",
)

entry(
    index = 66,
    label = "P110",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {5,D} {15,S}
4  C u0 p0 c0 {1,S} {8,D} {14,S}
5  C u0 p0 c0 {3,D} {6,S} {17,S}
6  C u0 p0 c0 {5,S} {7,D} {16,S}
7  C u0 p0 c0 {6,D} {9,S} {18,S}
8  C u0 p0 c0 {4,D} {19,S} {20,S}
9  O u0 p2 c0 {7,S} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {3,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.37668,0.0758383,-4.36613e-05,1.09147e-08,-7.81473e-13,-18721.5,15.1625], Tmin=(10,'K'), Tmax=(1533.26,'K')),
            NASAPolynomial(coeffs=[23.6165,0.0340419,-1.35385e-05,2.49869e-09,-1.72564e-13,-26221.7,-95.3518], Tmin=(1533.26,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-155.717,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (490.554,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 4, 'C-H': 10, 'C=C': 3, 'H-O': 1, 'C-O': 2}
1D rotors:
pivots: [1, 9], dihedral: [21, 1, 9, 8], rotor symmetry: 1, max scan energy: 72.90 kJ/mol
pivots: [3, 4], dihedral: [6, 3, 4, 5], rotor symmetry: 1, max scan energy: 19.80 kJ/mol
pivots: [3, 6], dihedral: [4, 3, 6, 10], rotor symmetry: 1, max scan energy: 10.06 kJ/mol
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 7], invalidation reason: Another conformer for C8H11O2[132] exists which is 0.51 kJ/mol lower.Another conformer for C8H11O2[132] exists which is 0.51 kJ/mol lower.
pivots: [7, 8], dihedral: [5, 7, 8, 2], rotor symmetry: 1, max scan energy: 31.61 kJ/mol
* Invalidated! pivots: [8, 9], dihedral: [2, 8, 9, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       5.33633100    0.24820500   -0.96286800
O       2.99399200    1.29954800   -1.35191800
C      -1.27124200    1.04336900    1.55343500
C      -0.60942000   -0.08734800    0.72818700
C       0.63207700    0.36555600    0.02731100
C      -2.56375000    0.61239700    2.18641800
C       1.85603400   -0.14767200    0.20173700
C       3.02857300    0.36091000   -0.52477200
C       4.30726300   -0.24115700   -0.28749400
C      -2.80395900    0.58164500    3.49369800
H      -1.45666200    1.89619200    0.88784000
H      -0.57398000    1.38863200    2.32273700
H      -1.33350200   -0.43684400   -0.02028200
H      -0.39343600   -0.93792000    1.38160300
H      -3.34693900    0.29678400    1.49783000
H       0.53511500    1.18952400   -0.67737500
H       2.01798400   -0.97042600    0.89442400
H       4.52633200   -1.05728200    0.38732000
H      -2.05317600    0.88624000    4.21699000
H      -3.75966700    0.25727700    3.88975700
H       4.93370200    0.96499400   -1.50678200
""",
)

entry(
    index = 67,
    label = "P107",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {6,D} {14,S}
4  C u0 p0 c0 {6,S} {8,D} {9,S}
5  C u0 p0 c0 {2,S} {7,D} {13,S}
6  C u0 p0 c0 {3,D} {4,S} {15,S}
7  C u0 p0 c0 {5,D} {16,S} {17,S}
8  C u0 p0 c0 {4,D} {18,S} {19,S}
9  O u0 p2 c0 {1,S} {4,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68057,0.0327192,9.47032e-05,-1.69602e-07,8.11912e-11,880.911,13.8574], Tmin=(10,'K'), Tmax=(712.946,'K')),
            NASAPolynomial(coeffs=[1.79172,0.0705763,-4.2299e-05,1.21374e-08,-1.34276e-12,457.448,17.4723], Tmin=(712.946,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (7.30338,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (453.139,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 4, 'C-H': 10, 'C=C': 3, 'C-O': 2}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 6], rotor symmetry: 1, max scan energy: 21.42 kJ/mol
* Invalidated! pivots: [3, 6], dihedral: [2, 3, 6, 8], invalidation reason: Another conformer for C8H10O[213] exists which is 1.55 kJ/mol lower.Another conformer for C8H10O[213] exists which is 1.55 kJ/mol lower.


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.89723900    0.37100400    0.90656300
C      -0.35310000    0.63472100   -0.40456000
C       0.87764300   -0.26103900   -0.63592300
C      -1.51030200    0.39109400   -1.33270400
C      -2.22503400    0.02570500    0.79949400
C       1.62894000    0.09720600   -1.88637700
C      -2.58073900    0.03856400   -0.61718600
C       1.81581100   -0.71039300   -2.92637000
C      -2.98739700   -0.25612900    1.86147100
H      -0.03708300    1.68748800   -0.42626100
H       1.52726500   -0.13737300    0.23819900
H       0.55631200   -1.30597800   -0.66062500
H       2.04417000    1.10382800   -1.92048400
H      -1.43772900    0.49205400   -2.40617100
H      -3.56597100   -0.20901200   -0.98595300
H       1.42455900   -1.72326500   -2.93731800
H       2.37472400   -0.39298200   -3.79948900
H      -4.02621500   -0.52046500    1.72410000
H      -2.58460100   -0.22583000    2.86433900
""",
)

entry(
    index = 68,
    label = "P109",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {9,S} {11,S}
2  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
3  C u0 p0 c0 {4,S} {10,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {7,D} {9,S}
5  C u1 p0 c0 {1,S} {7,S} {17,S}
6  C u0 p0 c0 {2,S} {8,D} {16,S}
7  C u0 p0 c0 {4,D} {5,S} {18,S}
8  C u0 p0 c0 {6,D} {19,S} {20,S}
9  O u0 p2 c0 {1,S} {4,S}
10 O u0 p2 c0 {3,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.39949,0.0656185,-1.20982e-05,-2.27089e-08,1.10149e-11,-15810.8,15.4518], Tmin=(10,'K'), Tmax=(1039.08,'K')),
            NASAPolynomial(coeffs=[10.1959,0.0592669,-3.15291e-05,8.10749e-09,-8.14311e-13,-18292.8,-22.7441], Tmin=(1039.08,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-131.451,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (498.868,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 5, 'C-H': 10, 'C=C': 2, 'H-O': 1, 'C-O': 3}
1D rotors:
pivots: [2, 5], dihedral: [21, 2, 5, 6], rotor symmetry: 1, max scan energy: 13.56 kJ/mol
pivots: [3, 4], dihedral: [1, 3, 4, 8], rotor symmetry: 1, max scan energy: 21.54 kJ/mol
* Invalidated! pivots: [4, 8], dihedral: [3, 4, 8, 10], invalidation reason: Another conformer for C8H11O2[105] exists which is 0.61 kJ/mol lower.Another conformer for C8H11O2[105] exists which is 0.61 kJ/mol lower.
* Invalidated! pivots: [5, 6], dihedral: [2, 5, 6, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.66895900   -0.34896100   -0.61293700
O      -3.50208500   -2.39056500    0.51340300
C      -0.30363800    0.16139400   -0.67263400
C       0.56166100   -0.82895100   -1.48012300
C      -3.37689300   -1.03342500    0.95407000
C      -2.02633600   -0.46865600    0.70663400
C       0.07435400    0.34115900    0.76814900
C       1.93191000   -0.28736100   -1.76972000
C      -0.99558200   -0.06609400    1.54268800
C       3.07208800   -0.81746200   -1.33670500
H      -0.35024000    1.11433600   -1.22116600
H       0.03257600   -1.02533500   -2.42031500
H       0.62455200   -1.77150800   -0.92975800
H      -3.58012300   -1.03567800    2.02552000
H      -4.13612400   -0.40588100    0.46349300
H       1.96809000    0.61357400   -2.38110100
H       1.03193900    0.71140400    1.09852100
H      -1.04285100   -0.08378900    2.62198600
H       3.08575500   -1.71488400   -0.72577900
H       4.03251200   -0.37894300   -1.58332200
H      -3.25992100   -2.40055500   -0.41864800
""",
)

entry(
    index = 69,
    label = "P115",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {13,S}
2  O u0 p2 c0 {7,D}
3  C u0 p0 c0 {4,S} {5,S} {6,S} {8,S}
4  C u0 p0 c0 {1,S} {3,S} {5,S} {9,S}
5  C u0 p0 c0 {3,S} {4,S} {10,S} {11,S}
6  C u0 p0 c0 {3,S} {7,D} {12,S}
7  C u0 p0 c0 {2,D} {6,D}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79113,0.0180678,0.000154074,-4.43001e-07,3.89403e-10,-16410.9,12.7131], Tmin=(10,'K'), Tmax=(359.378,'K')),
            NASAPolynomial(coeffs=[2.32087,0.048469,-3.14044e-05,9.75418e-09,-1.15908e-12,-16395.8,17.0405], Tmin=(359.378,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-136.429,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'C-O': 1, 'C-C': 4, 'C-H': 5, 'H-O': 1, 'C=O': 1}
1D rotors:
pivots: [1, 4], dihedral: [13, 1, 4, 3], rotor symmetry: 1, max scan energy: 10.13 kJ/mol
* Invalidated! pivots: [3, 6], dihedral: [4, 3, 6, 7], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.38791600    1.75917500   -0.41281500
O       1.40241100   -3.26880300    0.48447800
C       0.04009300   -0.03444500    0.62777700
C      -0.72045400    0.53581300   -0.55582200
C      -1.30121900   -0.60928700    0.20342700
C       1.31022900   -0.79405500    0.43050400
C       1.36644500   -2.10602700    0.46902700
H      -0.00172100    0.58913000    1.51710200
H      -0.31342300    0.33092800   -1.54445200
H      -2.14872200   -0.38065000    0.83713000
H      -1.32994500   -1.58365200   -0.26944100
H       2.25030500   -0.27586200    0.27335100
H      -0.73931000    2.46422900   -0.51063600
""",
)

entry(
    index = 70,
    label = "P116",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {5,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {2,S} {6,D}
5  C u0 p0 c0 {3,S} {7,D} {15,S}
6  C u0 p0 c0 {4,D} {7,S} {17,S}
7  C u0 p0 c0 {5,D} {6,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7106,0.0324932,5.30781e-05,-9.40695e-08,4.07368e-11,23657.4,10.2863], Tmin=(10,'K'), Tmax=(814.601,'K')),
            NASAPolynomial(coeffs=[3.03483,0.0575303,-3.30178e-05,9.12096e-09,-9.7704e-13,23046.9,8.98494], Tmin=(814.601,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (196.708,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (399.095,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-C': 5, 'C-H': 10}
1D rotors:
pivots: [3, 5], dihedral: [12, 3, 5, 7], rotor symmetry: 3, max scan energy: 7.50 kJ/mol
pivots: [6, 7], dihedral: [4, 6, 7, 5], rotor symmetry: 2, max scan energy: 31.43 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       0.52596400   -3.86197800   -2.21936400
C      -0.59033400   -3.12836900   -2.98866600
C       3.18821800    0.14097500    1.08125500
C       0.28945600   -2.42404500   -2.05553500
C       2.07576500   -0.01099300    0.08957600
C       0.63804000   -1.28490500   -1.46664300
C       1.72235700   -1.15829400   -0.50552800
H       1.39372600   -4.19316800   -2.78329500
H       0.22897200   -4.53966100   -1.42359100
H      -0.45354100   -2.98058800   -4.05653700
H      -1.61813500   -3.32703400   -2.69701900
H       3.69137800   -0.81037500    1.26984100
H       3.93880600    0.85841100    0.72928700
H       2.81702300    0.52470100    2.03882800
H       1.52058500    0.89372300   -0.15545500
H       2.26846800   -2.07003300   -0.27005500
H       0.08463000   -0.37944800   -1.70996900
""",
)

entry(
    index = 71,
    label = "P117",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {5,S} {6,D}
4  C u0 p0 c0 {2,S} {7,D} {14,S}
5  C u0 p0 c0 {3,S} {7,D} {15,S}
6  C u0 p0 c0 {3,D} {16,S} {17,S}
7  C u0 p0 c0 {4,D} {5,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.46174,0.0457317,7.87764e-06,-4.39545e-08,2.23362e-11,19980.6,12.4839], Tmin=(10,'K'), Tmax=(760.514,'K')),
            NASAPolynomial(coeffs=[3.63367,0.0552954,-3.16317e-05,8.77803e-09,-9.4783e-13,19651.8,9.71131], Tmin=(760.514,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (166.07,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (394.937,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 3, 'C-C': 3, 'C-H': 10}
1D rotors:
pivots: [1, 3], dihedral: [8, 1, 3, 5], rotor symmetry: 3, max scan energy: 7.21 kJ/mol
pivots: [2, 4], dihedral: [11, 2, 4, 7], rotor symmetry: 3, max scan energy: 6.50 kJ/mol
pivots: [3, 5], dihedral: [1, 3, 5, 7], rotor symmetry: 1, max scan energy: 26.72 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -1.82404600    0.25862500   -2.31829300
C      -4.93691600    2.10093000    0.61085400
C      -0.91794400    0.44797000   -1.12956800
C      -3.65038100    2.62742100    0.02130000
C      -1.37787200    1.33107300   -0.04616600
C       0.27426000   -0.15732600   -1.03862500
C      -2.52015000    1.97895200   -0.02030600
H      -1.37410100   -0.40990400   -3.05364400
H      -2.03693600    1.21661900   -2.80261300
H      -2.78760500   -0.16002600   -2.01124800
H      -5.28423500    2.75018500    1.42134600
H      -5.72861600    2.07777200   -0.14525900
H      -4.80843900    1.09308800    1.00747700
H      -3.68424500    3.63338200   -0.39802400
H      -0.70011400    1.44863600    0.79840200
H       0.91848200   -0.01314000   -0.17805300
H       0.63869300   -0.81252800   -1.82117100
""",
)

entry(
    index = 72,
    label = "P118",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {5,S} {14,S}
5  C u0 p0 c0 {4,S} {7,D} {15,S}
6  C u0 p0 c0 {7,D} {16,S} {17,S}
7  C u0 p0 c0 {5,D} {6,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53237,0.0476096,-1.33922e-05,-5.93433e-09,3.07615e-12,20223.3,11.4033], Tmin=(10,'K'), Tmax=(1270.69,'K')),
            NASAPolynomial(coeffs=[9.67705,0.0401938,-1.87174e-05,4.24628e-09,-3.8012e-13,17698.8,-23.5021], Tmin=(1270.69,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (168.114,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (399.095,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 3, 'C-C': 3, 'C-H': 10}
1D rotors:
pivots: [1, 3], dihedral: [8, 1, 3, 2], rotor symmetry: 3, max scan energy: 8.57 kJ/mol
pivots: [2, 3], dihedral: [11, 2, 3, 1], rotor symmetry: 3, max scan energy: 3.92 kJ/mol
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 7], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
C      -1.85654700    1.56814700    0.60841300
C      -0.23933900   -0.26810700    1.27754000
C      -1.10252500    0.32969300    0.19820200
C      -1.22507900   -0.16364600   -1.04731900
C      -0.56608000   -1.34596100   -1.59461100
C      -0.89162500   -2.20182500   -4.04435600
C      -0.72953900   -1.77587100   -2.82497700
H      -1.16780300    2.35765000    0.93304900
H      -2.51630100    1.36206400    1.46007500
H      -2.46617700    1.96246600   -0.20654900
H      -0.84665600   -0.53306800    2.15109600
H       0.50136300    0.46216000    1.62425000
H       0.29695200   -1.16207100    0.96100200
H      -1.88052300    0.35749300   -1.73992800
H       0.10371900   -1.91381800   -0.95352100
H      -1.67294100   -2.91316400   -4.29996700
H      -0.25159800   -1.86379600   -4.85546400
""",
)

entry(
    index = 73,
    label = "P119",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {6,S} {7,D}
4  C u0 p0 c0 {2,S} {5,D} {14,S}
5  C u0 p0 c0 {4,D} {7,S} {15,S}
6  C u1 p0 c0 {3,S} {16,S} {17,S}
7  C u1 p0 c0 {3,D} {5,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.42475,0.0602213,-0.00014717,3.7105e-07,-3.27521e-10,42055.6,17.8108], Tmin=(10,'K'), Tmax=(416.362,'K')),
            NASAPolynomial(coeffs=[0.0381491,0.0610646,-3.60346e-05,1.02914e-08,-1.14005e-12,42612.3,34.4807], Tmin=(416.362,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (349.653,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (390.78,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-C': 4, 'C-H': 10}
1D rotors:
pivots: [1, 3], dihedral: [8, 1, 3, 6], rotor symmetry: 3, max scan energy: 0.10 kJ/mol (set as a FreeRotor)
pivots: [2, 4], dihedral: [11, 2, 4, 5], rotor symmetry: 3, max scan energy: 4.32 kJ/mol
* Invalidated! pivots: [3, 6], dihedral: [1, 3, 6, 16], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [5, 7], dihedral: [4, 5, 7, 3], rotor symmetry: 2, max scan energy: 0.02 kJ/mol (set as a FreeRotor)
pivots: [3, 7], dihedral: [1, 3, 7, 5], rotor symmetry: 2, max scan energy: 0.02 kJ/mol (set as a FreeRotor)
* Invalidated! pivots: [4, 5], dihedral: [2, 4, 5, 7], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
C       2.04160300    2.30936200   -0.18185800
C      -3.39080200   -0.25243400   -0.10420400
C       1.63125900    0.84223200   -0.30113400
C      -1.96418500    0.04194800    0.22632500
C      -0.97869200    0.28143300   -0.73380200
C       2.61001400   -0.14771700   -0.22306800
C       0.32290400    0.54581100   -0.49981700
H       2.18723200    2.74710100   -1.17371300
H       1.27668000    2.89383300    0.33148600
H       2.97881100    2.40380100    0.37077400
H      -3.56305400   -0.25158800   -1.18354700
H      -3.70095100   -1.23085100    0.28487900
H      -4.06905200    0.48430600    0.34519600
H      -1.68019300    0.06730000    1.27420900
H      -1.29676600    0.24549600   -1.78085200
H       2.35643400   -1.19439800   -0.32939200
H       3.64787000    0.11103300   -0.05160200
""",
)

entry(
    index = 74,
    label = "P120",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {6,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {2,S} {5,D}
5  C u0 p0 c0 {1,S} {4,D} {7,S}
6  C u0 p0 c0 {3,S} {7,D} {16,S}
7  C u0 p0 c0 {5,S} {6,D} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.39961,0.0582923,-0.000107927,2.31635e-07,-1.83876e-10,27860.4,11.7132], Tmin=(10,'K'), Tmax=(463.639,'K')),
            NASAPolynomial(coeffs=[0.159062,0.0610422,-3.52706e-05,9.89631e-09,-1.08096e-12,28431.8,27.7779], Tmin=(463.639,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (231.628,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (399.095,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-C': 5, 'C-H': 10}
1D rotors:
pivots: [2, 4], dihedral: [10, 2, 4, 1], rotor symmetry: 2, max scan energy: 4.89 kJ/mol
pivots: [3, 6], dihedral: [13, 3, 6, 7], rotor symmetry: 3, max scan energy: 7.46 kJ/mol
* Invalidated! pivots: [5, 7], dihedral: [1, 5, 7, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
C       2.52031800   -0.56515400    3.63236400
C       1.20972000   -2.02952200    1.59207600
C      -0.67876700    2.58191200    5.58933900
C       1.46340100   -1.06974600    2.68503100
C       1.07955900   -0.13025400    3.49976100
C       0.32693200    1.63339100    5.01625800
C       0.08887000    0.76402300    4.02291600
H       3.31759000    0.08491300    3.26113200
H       2.82349000   -1.17867300    4.48543100
H       0.17856700   -1.97192500    1.23537100
H       1.40514300   -3.05507600    1.92478900
H       1.88054500   -1.83930400    0.74681800
H      -1.65036300    2.48672900    5.09898700
H      -0.81912500    2.40690100    6.66236000
H      -0.34445300    3.62080500    5.48620000
H       1.32641400    1.65836900    5.44540700
H      -0.90216000    0.71728600    3.57472100
""",
)

entry(
    index = 75,
    label = "P121",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {5,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {5,S} {6,D}
5  C u0 p0 c0 {3,S} {4,S} {7,D}
6  C u0 p0 c0 {1,S} {4,D} {15,S}
7  C u0 p0 c0 {5,D} {16,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.59168,0.0365001,6.65554e-05,-1.78149e-07,1.27731e-10,29129.4,12.459], Tmin=(10,'K'), Tmax=(366.539,'K')),
            NASAPolynomial(coeffs=[1.2638,0.061904,-3.7406e-05,1.09378e-08,-1.23712e-12,29300,21.3533], Tmin=(366.539,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (242.171,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (399.095,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-C': 5, 'C-H': 10}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [4, 1, 2, 9], invalidation reason: 
pivots: [3, 5], dihedral: [12, 3, 5, 4], rotor symmetry: 3, max scan energy: 6.45 kJ/mol
pivots: [4, 5], dihedral: [1, 4, 5, 3], rotor symmetry: 1, max scan energy: 23.10 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -1.51219800    2.87133400   -1.88416000
C      -2.91082500    3.00985000   -2.46728300
C      -0.02708200   -0.70305700   -0.78543600
C      -0.93120900    1.53482200   -1.49434900
C      -0.96282600    0.45435400   -0.53576200
C      -0.43726200    2.07015000   -2.57330800
C      -1.79221500    0.51066000    0.51632000
H      -1.19800000    3.74543900   -1.30526600
H      -3.19977600    2.10442600   -3.00823700
H      -2.96409500    3.85201200   -3.16585200
H      -3.65506500    3.18783200   -1.68371600
H       1.01203200   -0.36057900   -0.81500200
H      -0.11854600   -1.46371500   -0.00825100
H      -0.23784600   -1.16869800   -1.75320700
H       0.24461100    2.02853600   -3.40620200
H      -1.82976800   -0.28555000    1.25110000
H      -2.45151600    1.35760500    0.66373100
""",
)

entry(
    index = 75,
    label = "P122",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u1 p0 c0 {1,S} {3,S} {7,S}
3 C u0 p0 c0 {2,S} {4,D} {8,S}
4 C u1 p0 c0 {1,S} {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.15781,-0.0127374,0.000129377,-1.99947e-07,1.0009e-10,67551.7,8.73817], Tmin=(10,'K'), Tmax=(632.91,'K')),
            NASAPolynomial(coeffs=[0.516074,0.0300666,-1.89673e-05,5.70849e-09,-6.56523e-13,67616.3,21.5106], Tmin=(632.91,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (561.662,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 4, 'C-C': 3, 'C=C': 1}

External symmetry: 1, optical isomers: 1

Geometry:
C       0.98124500   -0.12556000    0.09069700
C      -0.32074900    0.69295700    0.04949400
C      -1.13260600   -0.41945800   -0.17320300
C      -0.01771900   -1.25689900   -0.15449900
H       1.50136600   -0.14760700    1.05129700
H       1.69220000    0.06697900   -0.71629400
H      -0.50901500    1.75492500    0.15809100
H      -2.19472200   -0.56533700   -0.30558200
""",
)

entry(
    index = 76,
    label = "P123",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {2,S} {4,D}
4 C u0 p0 c0 {1,S} {3,D} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.16701,-0.013271,0.000127163,-1.92589e-07,9.48192e-11,55850.3,8.26985], Tmin=(10,'K'), Tmax=(639.921,'K')),
            NASAPolynomial(coeffs=[0.254881,0.0300839,-1.8768e-05,5.59741e-09,-6.39291e-13,55964,22.3734], Tmin=(639.921,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (464.375,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 4, 'C-C': 4, 'C=C': 1}

External symmetry: 1, optical isomers: 2

Geometry:
C       0.17519100    0.38658000   -0.60835100
C      -0.98490500   -0.15725500    0.12032600
C       0.25131900   -0.24922800    1.08910500
C       1.18572400   -0.31532700    0.09105400
H       0.24569200    1.43120900   -0.91903800
H      -1.81085400    0.50151000    0.38627400
H      -1.31426200   -1.14855900   -0.16973200
H       2.25209500   -0.44893000    0.01036100
""",
)

entry(
    index = 77,
    label = "P124",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {6,S}
3 C u0 p0 c0 {1,S} {2,S} {7,S} {8,S}
4 C u0 p1 c0 {1,S} {2,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.17754,-0.0136667,0.000124586,-1.82559e-07,8.67989e-11,59659.4,7.56236], Tmin=(10,'K'), Tmax=(663.816,'K')),
            NASAPolynomial(coeffs=[0.0513423,0.0305606,-1.91083e-05,5.69539e-09,-6.49045e-13,59780.6,22.5647], Tmin=(663.816,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (496.052,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 4, 'C-C': 5}

External symmetry: 1, optical isomers: 1

Geometry:
C       0.42806400   -0.80903000   -0.09590100
C       0.46973800    0.76342900    0.20853900
C      -0.81886400   -0.00277500    0.12642600
C       1.42362000   -0.17469800    0.70745800
H       0.62028200   -1.44502200   -0.95596100
H       0.70266700    1.66360100   -0.35410800
H      -1.32478600   -0.17218800    1.07071000
H      -1.50072000    0.17668400   -0.70716100
""",
)

entry(
    index = 78,
    label = "P125",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {4,S}
2  O u0 p2 c0 {3,S} {7,S}
3  C u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
5  C u1 p0 c0 {3,S} {6,S} {10,S}
6  C u0 p0 c0 {5,S} {7,D} {11,S}
7  C u0 p0 c0 {2,S} {6,D} {12,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91728,0.00466509,0.00013541,-2.37304e-07,1.27327e-10,-2169.14,11.3201], Tmin=(10,'K'), Tmax=(588.417,'K')),
            NASAPolynomial(coeffs=[-0.582139,0.0538508,-3.73875e-05,1.21911e-08,-1.49924e-12,-1961.61,27.9051], Tmin=(588.417,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-18.0733,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 3, 'C=C': 1, 'C-O': 4}

External symmetry: 1, optical isomers: 2

Geometry:
O       1.55326100   -0.18104600    1.28093900
O      -0.23179000   -1.27409600    0.11884300
C       0.54080200   -0.08890500    0.28925800
C       1.95597100   -0.14690800   -0.10369600
C      -0.41278200    1.03168000    0.25143500
C      -1.67706800    0.48460200    0.09843800
C      -1.53633700   -0.89078700    0.02256400
H       2.33871100   -1.08574700   -0.49561500
H       2.47235500    0.75616400   -0.42098100
H      -0.13214600    2.06585200    0.36687600
H      -2.61629900    1.01466200    0.05256200
H      -2.25468000   -1.68547200   -0.09289700
""",
)

entry(
    index = 79,
    label = "P126",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {2,S} {6,S}
4  C u0 p0 c0 {1,S} {5,D} {10,S}
5  C u0 p0 c0 {4,D} {6,S} {11,S}
6  O u0 p2 c0 {3,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.21664,-0.0185638,0.000214987,-3.54004e-07,1.87292e-10,30796,10.962], Tmin=(10,'K'), Tmax=(607.503,'K')),
            NASAPolynomial(coeffs=[-0.248493,0.0457203,-2.98717e-05,9.22336e-09,-1.08094e-12,30694.8,24.9803], Tmin=(607.503,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (256.045,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 4, 'C=C': 1, 'C-O': 2}

External symmetry: 1, optical isomers: 2

Geometry:
O       0.70647500   -1.44366300    0.06490900
C      -0.40655800    0.54032000    0.58267200
C      -1.44346200   -0.33071400   -0.25094700
C      -0.46224400   -0.94878100    0.65227100
C       0.91349300    0.81256300   -0.01493900
C       1.49457300   -0.37066200   -0.26694600
H      -0.85156000    1.21046900    1.30792500
H      -2.46414600   -0.21188100    0.09190300
H      -1.30875800   -0.41887400   -1.32505300
H       1.36495700    1.78255600   -0.15551400
H       2.45723200   -0.62133400   -0.68628000
""",
)

entry(
    index = 80,
    label = "P127",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {6,D} {9,S}
3  C u0 p0 c0 {4,D} {5,S} {11,S}
4  C u0 p0 c0 {3,D} {6,S} {10,S}
5  O u0 p2 c0 {1,S} {3,S}
6  C u1 p0 c0 {2,D} {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.08331,-0.00790824,0.000166426,-2.82578e-07,1.53059e-10,27975.5,11.1061], Tmin=(10,'K'), Tmax=(584.919,'K')),
            NASAPolynomial(coeffs=[-0.0773494,0.0442586,-2.8167e-05,8.52359e-09,-9.85178e-13,28056.6,25.4798], Tmin=(584.919,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (232.586,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 2, 'C=C': 2, 'C-O': 2}

External symmetry: 1, optical isomers: 2

Geometry:
O       0.02925000   -0.90524200   -0.94153000
C      -1.15525200   -0.43589300   -0.23630800
C      -0.97094600    0.99965000    0.22233200
C       1.20796300   -0.62490400   -0.35083500
C       1.37000000    0.37725900    0.54850000
C       0.24644000    1.24841200    0.67696600
H      -1.32106000   -1.12394400    0.60492500
H      -1.97216500   -0.54021400   -0.94921000
H      -1.76158600    1.72926800    0.09637700
H       2.31787600    0.53354000    1.04385900
H       2.00947900   -1.25793200   -0.71507600
""",
)

entry(
    index = 81,
    label = "P128",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3 C u1 p0 c0 {1,S} {8,S} {9,S}
4 C u0 p1 c0 {1,S} {2,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.17506,-0.0138337,0.000138623,-2.08369e-07,1.01775e-10,56629.7,8.36368], Tmin=(10,'K'), Tmax=(642.458,'K')),
            NASAPolynomial(coeffs=[-0.369384,0.0345652,-2.13185e-05,6.30822e-09,-7.16529e-13,56798.7,25.0482], Tmin=(642.458,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (470.856,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 4}
1D rotors:
* Invalidated! pivots: [1, 3], dihedral: [2, 1, 3, 8], invalidation reason: Bond ([[1, 4]]) broke during the scan. But unable to propose troubleshooting methods.Bond ([[1, 4]]) broke during the scan. But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
C      -0.03384700   -0.59267100   -0.42942200
C       1.15694800    0.27568300   -0.04288300
C      -1.14194100    0.16419500    0.29219100
C       0.14725800   -0.18390900    0.94911900
H      -0.06930300   -1.52063700   -0.98138800
H       1.19933200    1.32213900   -0.35289800
H       2.11716400   -0.23120200   -0.02861900
H      -1.36981500    1.19755000    0.02158000
H      -2.00579800   -0.43114700    0.57232000
""",
)

entry(
    index = 82,
    label = "P129",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3 C u1 p0 c0 {1,S} {4,S} {9,S}
4 C u0 p1 c0 {2,S} {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.15683,-0.0119789,0.0001238,-1.78964e-07,8.39058e-11,47945.4,8.47065], Tmin=(10,'K'), Tmax=(664.828,'K')),
            NASAPolynomial(coeffs=[-0.658366,0.0346081,-2.10567e-05,6.14853e-09,-6.90406e-13,48196.3,26.8076], Tmin=(664.828,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (398.655,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 4}

External symmetry: 1, optical isomers: 1

Geometry:
C       0.25255900    0.66993200   -0.14118100
C      -1.01083000   -0.26135500   -0.00886600
C       1.12135200   -0.54560800    0.20799900
C       0.03823300   -1.30591200    0.31240900
H       0.27812900    1.47971600    0.59359000
H       0.40032900    1.06623100   -1.14984500
H      -1.57297900   -0.41709000   -0.93131400
H      -1.69453700   -0.00585400    0.80257700
H       2.18774400   -0.68005900    0.31463000
""",
)

entry(
    index = 83,
    label = "P130",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {6,S}
2  O u0 p2 c0 {3,S} {13,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
4  C u0 p0 c0 {1,S} {3,S} {7,D}
5  C u0 p0 c0 {3,S} {6,D} {9,S}
6  C u0 p0 c0 {1,S} {5,D} {10,S}
7  C u0 p0 c0 {4,D} {11,S} {12,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86052,0.00814642,0.000159818,-3.13306e-07,1.83608e-10,-21854.4,11.2395], Tmin=(10,'K'), Tmax=(571.716,'K')),
            NASAPolynomial(coeffs=[2.56725,0.0494929,-3.34018e-05,1.08177e-08,-1.33417e-12,-22234.4,12.1394], Tmin=(571.716,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-181.766,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'H-O': 1, 'C-C': 2, 'C=C': 2, 'C-O': 3}
1D rotors:
pivots: [2, 3], dihedral: [13, 2, 3, 4], rotor symmetry: 1, max scan energy: 14.22 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.21202400   -0.48954000   -1.44530900
O       0.18611900    1.22023200    1.54217400
C      -0.11538700   -0.01113100    0.88973100
C       0.67288100   -0.23631700   -0.40207800
C      -1.53054000   -0.15007400    0.38223300
C      -1.48448000   -0.41129900   -0.92147200
C       1.98312700   -0.17050400   -0.59883100
H       0.13071400   -0.77098000    1.63694000
H      -2.41517700   -0.05810000    0.99206700
H      -2.26911400   -0.57817500   -1.64426200
H       2.41291700   -0.31150200   -1.58169600
H       2.63778200    0.03806400    0.23592700
H       0.00319300    1.92932400    0.91457900
""",
)

entry(
    index = 84,
    label = "P131",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,S} {4,D} {5,S}
3 C u0 p0 c0 {1,D} {2,S} {6,S}
4 C u0 p1 c0 {2,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92365,0.00484562,6.9454e-05,-1.61724e-07,1.09776e-10,36835.4,7.93315], Tmin=(10,'K'), Tmax=(510.91,'K')),
            NASAPolynomial(coeffs=[4.39195,0.0167968,-1.1486e-05,3.72214e-09,-4.56955e-13,36583.7,3.9936], Tmin=(510.91,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (306.245,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (128.874,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'C=O': 1, 'C-H': 2, 'C-C': 1}
1D rotors:
pivots: [2, 3], dihedral: [4, 2, 3, 1], rotor symmetry: 1, max scan energy: 23.27 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O      -1.54295500    0.24419400    0.79266800
C       0.71044500   -0.08382200    0.12031800
C      -0.76303200    0.09126100   -0.10829600
C       1.61727600   -0.25399000   -0.79750200
H       1.05738200   -0.06716700    1.15575700
H      -1.07911600    0.06952400   -1.16294500
""",
)

entry(
    index = 85,
    label = "P132",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {12,S}
2  O u0 p2 c0 {3,S} {13,S}
3  C u0 p0 c0 {1,S} {2,S} {6,S} {7,S}
4  C u0 p0 c0 {5,S} {8,S} {9,S} {10,S}
5  C u0 p0 c0 {4,S} {6,D} {11,S}
6  C u1 p0 c0 {3,S} {5,D}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.42711,0.0563459,-0.000127749,2.43254e-07,-1.79225e-10,-15872,12.3745], Tmin=(10,'K'), Tmax=(446.235,'K')),
            NASAPolynomial(coeffs=[3.18631,0.0421093,-2.47818e-05,7.08909e-09,-7.87965e-13,-15687.3,15.171], Tmin=(446.235,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-131.983,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C=C': 1, 'C-H': 5, 'C-C': 2, 'H-O': 2}
1D rotors:
* Invalidated! pivots: [1, 3], dihedral: [12, 1, 3, 2], invalidation reason: Another conformer for C4H7O2[262] exists which is 1.40 kJ/mol lower.Another conformer for C4H7O2[262] exists which is 1.40 kJ/mol lower.
* Invalidated! pivots: [2, 3], dihedral: [13, 2, 3, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [3, 6], dihedral: [1, 3, 6, 5], rotor symmetry: 1, max scan energy: 12.75 kJ/mol
pivots: [4, 5], dihedral: [8, 4, 5, 6], rotor symmetry: 3, max scan energy: 6.65 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.48430000   -2.28419300    2.26398000
O       0.53202400   -2.57945000    1.11397400
C      -0.88028400   -2.71557600    1.06501100
C      -1.89954500   -0.63135300   -2.15285900
C      -1.04956300   -1.37693900   -1.15827600
C      -1.47174500   -1.93672100   -0.05109200
H      -1.03891400   -3.78865200    0.90521500
H      -1.54036100    0.39563900   -2.27594200
H      -1.84895200   -1.10852600   -3.13712500
H      -2.94264800   -0.59795900   -1.83651400
H       0.01644600   -1.46096100   -1.39980300
H      -1.15179900   -2.85492500    2.96621700
H       0.71137400   -1.63881200    1.24249000
""",
)

entry(
    index = 86,
    label = "P133",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {4,S} {6,S}
2  C u0 p0 c0 {1,D} {7,S} {8,S}
3  C u1 p0 c0 {5,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {5,T}
5  C u0 p0 c0 {3,S} {4,T}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85317,0.0135748,9.69758e-05,-3.1111e-07,3.22041e-10,45453.7,11.597], Tmin=(10,'K'), Tmax=(245.496,'K')),
            NASAPolynomial(coeffs=[2.68102,0.0326732,-1.97158e-05,5.77447e-09,-6.54855e-13,45511.2,15.6057], Tmin=(245.496,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (377.932,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (228.648,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'C#C': 1, 'C-H': 5, 'C-C': 2}
1D rotors:
pivots: [1, 4], dihedral: [2, 1, 4, 5], rotor symmetry: 1, max scan energy: 0.05 kJ/mol (set as a FreeRotor)
* Invalidated! pivots: [3, 5], dihedral: [9, 3, 5, 4], invalidation reason: 
* Invalidated! pivots: [1, 2], dihedral: [4, 1, 2, 7], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
C      -1.22510600   -0.63553800   -0.42779700
C      -1.84164800   -0.94366000   -1.59628800
C       2.60398500    0.35907300   -0.01521500
C       0.11757400   -0.28937600   -0.30249400
C       1.30648000    0.02125800   -0.16087900
H      -1.80747500   -0.65493700    0.49158700
H      -2.89239800   -1.20413100   -1.61669300
H      -1.30423200   -0.93810900   -2.53668600
H       3.26961500    0.40763500   -0.86941500
H       3.01595800    0.59111800    0.96028800
""",
)

entry(
    index = 87,
    label = "P134",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {6,D}
2  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
4  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
5  C u1 p0 c0 {3,S} {6,S} {11,S}
6  C u0 p0 c0 {1,D} {2,S} {5,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.10779,-0.0105613,0.000194732,-3.44657e-07,1.93976e-10,23901.3,11.1888], Tmin=(10,'K'), Tmax=(573.307,'K')),
            NASAPolynomial(coeffs=[0.692757,0.0440576,-2.87375e-05,8.88694e-09,-1.04487e-12,23786.9,21.3511], Tmin=(573.307,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (198.704,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C=O': 1, 'C-C': 6}

External symmetry: 1, optical isomers: 2

Geometry:
O       2.04487600    0.65763200   -1.40592800
C       0.11462000   -0.72745200   -0.55371300
C      -0.26926300   -0.17163800    0.86241600
C      -1.23443300   -0.12021300   -0.31071200
C       0.77976300    0.86132100    0.71504500
C       1.17688100    0.38294000   -0.61203800
H       0.25284200   -1.76166700   -0.83944500
H      -0.49460700   -0.74083600    1.75381900
H      -2.05762600   -0.82621800   -0.25697000
H      -1.48753900    0.84030400   -0.74653600
H       1.17448500    1.60582600    1.39406400
""",
)

entry(
    index = 88,
    label = "P135",
    molecule = 
"""
multiplicity 3
1  O u1 p2 c0 {3,S}
2  C u0 p0 c0 {3,S} {4,D} {7,S}
3  C u0 p0 c0 {1,S} {2,S} {6,D}
4  C u0 p0 c0 {2,D} {5,S} {8,S}
5  C u1 p0 c0 {4,S} {9,S} {12,S}
6  C u0 p0 c0 {3,D} {10,S} {11,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84083,0.010054,0.000166409,-3.72734e-07,2.48227e-10,18302.8,11.4456], Tmin=(10,'K'), Tmax=(510.074,'K')),
            NASAPolynomial(coeffs=[3.8132,0.0433021,-2.85021e-05,8.97314e-09,-1.08226e-12,17875.9,7.34824], Tmin=(510.074,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (152.133,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'C=C': 2, 'C-H': 6, 'C-C': 2}
1D rotors:
pivots: [2, 3], dihedral: [4, 2, 3, 1], rotor symmetry: 1, max scan energy: 41.71 kJ/mol
* Invalidated! pivots: [4, 5], dihedral: [2, 4, 5, 9], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 6], dihedral: [1, 3, 6, 10], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [2, 4], dihedral: [3, 2, 4, 5], rotor symmetry: 1, max scan energy: 67.45 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O      -1.43796900    1.45015500    0.45855900
C       0.05492900   -0.29292600   -0.10402300
C      -1.27060400    0.32097900   -0.06389700
C       1.18197500    0.33808300    0.42909900
C       2.44525300   -0.19260800    0.41761200
C      -2.40009700   -0.36632200   -0.62519600
H       0.15802400   -1.27127000   -0.56497100
H       1.01679000    1.31399900    0.87658500
H       2.64635300   -1.16438200   -0.02074100
H      -2.31365800   -1.34210600   -1.08817700
H      -3.36686100    0.11676900   -0.57854100
H       3.28438400    0.34088500    0.84587100
""",
)

entry(
    index = 89,
    label = "P136",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {6,S}
3  C u0 p0 c0 {1,S} {5,D} {8,S}
4  C u0 p0 c0 {2,D} {11,S} {12,S}
5  C u0 p0 c0 {3,D} {9,S} {10,S}
6  O u0 p2 c0 {1,S} {2,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86404,0.00840835,0.000151321,-3.23799e-07,2.07783e-10,12834.8,10.7303], Tmin=(10,'K'), Tmax=(524.721,'K')),
            NASAPolynomial(coeffs=[3.36675,0.0414153,-2.65533e-05,8.30482e-09,-1.0024e-12,12484.8,8.97614], Tmin=(524.721,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (106.671,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (278.535,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C=C': 2, 'C-H': 6, 'C-C': 2}
1D rotors:
pivots: [2, 4], dihedral: [1, 2, 4, 6], rotor symmetry: 1, max scan energy: 18.63 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.00637400   -1.09249900    0.93115800
C      -0.03786200   -0.04653000    0.62566000
C       1.35387100    0.01704100    0.24747700
C      -1.09459400   -0.45604300   -0.31454500
C       2.40850700    0.56510600   -0.32493000
C      -2.37100300   -0.10635000   -0.17205500
H      -0.35596500    0.48896000    1.51638500
H      -0.76919000   -1.05484900   -1.16013400
H      -2.70699500    0.49148500    0.66936100
H      -3.12278200   -0.39933900   -0.89479800
H       2.31754000    1.52010300   -0.82272200
H       3.37210300    0.07291800   -0.30086200
""",
)

entry(
    index = 90,
    label = "P137",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {6,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  C u0 p0 c0 {3,S} {5,D} {10,S}
5  C u0 p0 c0 {4,D} {11,S} {12,S}
6  O u0 p2 c0 {1,S} {2,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89774,0.00617732,0.000143731,-2.83981e-07,1.71708e-10,12965.1,10.2806], Tmin=(10,'K'), Tmax=(535.615,'K')),
            NASAPolynomial(coeffs=[1.47913,0.046283,-3.03187e-05,9.49136e-09,-1.13506e-12,12908,17.4873], Tmin=(535.615,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (107.761,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (278.535,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C=C': 2, 'C-H': 6, 'C-C': 2}
1D rotors:
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 30.55 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O       2.07810300    0.31537300    0.60141500
C       1.76294100    0.33472100    2.05466000
C       0.79827400    0.14907000    1.00916000
C      -0.40728100   -0.04800700    0.48630000
C      -0.65541200   -0.14743900   -0.94201500
C      -1.85766900   -0.34533600   -1.49394400
H       2.15215500   -0.51844700    2.60205300
H       1.88898300    1.30733100    2.52067100
H      -1.24072400   -0.13746300    1.17455600
H       0.21527000   -0.05062600   -1.58564200
H      -1.98215100   -0.41114100   -2.56769600
H      -2.75259100   -0.44732900   -0.88812600
""",
)

entry(
    index = 91,
    label = "P138",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {2,S} {9,D}
4  C u0 p0 c0 {1,S} {5,D} {10,S}
5  C u0 p0 c0 {4,D} {11,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91647,0.00570858,0.000156257,-3.47458e-07,2.45593e-10,9112.74,11.4719], Tmin=(10,'K'), Tmax=(433.91,'K')),
            NASAPolynomial(coeffs=[1.04291,0.045723,-2.88235e-05,8.73515e-09,-1.01703e-12,9234.79,21.4688], Tmin=(433.91,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (75.7605,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'C=O': 1, 'C-H': 6, 'C-C': 4}
1D rotors:
* Invalidated! pivots: [2, 5], dihedral: [3, 2, 5, 6], invalidation reason: Another conformer for C5H6O[264] exists which is 2.60 kJ/mol lower.Another conformer for C5H6O[264] exists which is 2.60 kJ/mol lower.


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.95939100    1.68538100   -0.95523500
C      -0.29146000   -0.18640600   -0.38987700
C      -1.62210700   -0.42949000    0.44052300
C      -1.48474200    0.69474100   -0.48664100
C       0.94084900    0.26534200    0.28880600
C       2.17502000   -0.09408600   -0.05884700
H      -0.14780500   -0.88222400   -1.21315500
H      -1.59071800   -0.22679600    1.50751000
H      -2.22255600   -1.28837500    0.15849900
H       0.80014300    0.95057000    1.12261100
H       2.36167100   -0.77054200   -0.88658700
H       3.04109900    0.28188400    0.47238600
""",
)

entry(
    index = 91,
    label = "P139",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,D}
4  C u0 p0 c0 {1,S} {5,D} {11,S}
5  C u0 p0 c0 {2,S} {4,D} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.04079,-0.0041817,0.000152327,-2.51279e-07,1.31782e-10,-11179.3,9.64373], Tmin=(10,'K'), Tmax=(594.125,'K')),
            NASAPolynomial(coeffs=[-0.911159,0.0486771,-3.04073e-05,9.06542e-09,-1.03555e-12,-10935.4,28.0565], Tmin=(594.125,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-92.966,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'C=O': 1, 'C-H': 6, 'C-C': 4}

External symmetry: 2, optical isomers: 1

Geometry:
O       0.12354100    2.36963900    0.30940500
C       1.25743400    0.21656800    0.06064200
C      -1.22777800    0.35227200    0.01363200
C       0.06144800    1.17863900    0.15389500
C       0.60918500   -1.12828800   -0.12997200
C      -0.72303800   -1.05554200   -0.15517200
H       1.90969100    0.51475700   -0.76866700
H       1.86451700    0.29000600    0.97067900
H      -1.81196600    0.71797700   -0.83906600
H      -1.85714000    0.49322500    0.90028000
H       1.17777800   -2.04456000   -0.23360100
H      -1.38367200   -1.90469300   -0.28205400
""",
)

entry(
    index = 92,
    label = "P140",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {3,S} {12,D}
5  C u0 p1 c0 {2,S} {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9373,0.00375041,0.000133569,-2.43474e-07,1.39709e-10,23376.5,10.8518], Tmin=(10,'K'), Tmax=(525.976,'K')),
            NASAPolynomial(coeffs=[-0.622598,0.0502654,-3.28426e-05,1.02382e-08,-1.21967e-12,23692.4,28.3644], Tmin=(525.976,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (194.339,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 6, 'C=O': 1, 'C-C': 5}

External symmetry: 1, optical isomers: 2

Geometry:
O       0.18354600    2.13014200   -1.01021500
C      -1.07973600    0.26667500   -0.02396800
C      -0.50531400   -1.15413300    0.13284300
C       1.36170200    0.27285500    0.08164500
C       0.15266200    1.08965000   -0.41043400
C       0.98794000   -1.14710500    0.26626700
H      -1.46484300    0.65592300    0.92561800
H      -1.87220100    0.37369900   -0.76516000
H      -0.99175700   -1.79962900    0.86917700
H      -0.59670300   -1.72373300   -0.81223300
H       1.50808500    0.54800300    1.14877300
H       2.31661800    0.48765400   -0.40231500
""",
)

entry(
    index = 93,
    label = "P141",
    molecule = 
"""
multiplicity 3
1  O u0 p2 c0 {3,S} {4,S}
2  O u0 p2 c0 {5,S} {13,S}
3  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
4  C u0 p0 c0 {1,S} {5,D} {7,S}
5  C u0 p0 c0 {2,S} {4,D} {6,S}
6  C u1 p0 c0 {3,S} {5,S} {10,S}
7  C u1 p0 c0 {4,S} {11,S} {12,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80157,0.0145218,0.000184953,-4.83691e-07,3.79891e-10,4299.29,12.1249], Tmin=(10,'K'), Tmax=(424.485,'K')),
            NASAPolynomial(coeffs=[3.1643,0.0481732,-3.16533e-05,9.92637e-09,-1.18676e-12,4104.32,11.7195], Tmin=(424.485,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (35.7395,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 3, 'C=C': 1, 'C-H': 5, 'C-C': 3, 'H-O': 1}
1D rotors:
pivots: [2, 5], dihedral: [13, 2, 5, 4], rotor symmetry: 1, max scan energy: 13.74 kJ/mol
* Invalidated! pivots: [4, 7], dihedral: [1, 4, 7, 11], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
O      -0.84664300    0.04124000   -1.11753000
O       1.30561700    0.03114800    1.75997000
C      -0.49177400   -1.36744300   -1.07085000
C      -0.20600600    0.66693900   -0.06988400
C       0.55270200   -0.25875300    0.66413900
C       0.41894200   -1.50677900    0.10569600
C      -0.38903200    2.09564600    0.11947300
H      -0.02810300   -1.62411700   -2.03365600
H      -1.42542100   -1.94153400   -0.98963500
H       0.87736300   -2.42342100    0.44060600
H       0.22372200    2.81988200   -0.41299400
H      -1.23614200    2.48829200    0.67780700
H       1.22795700    0.97439000    1.94280500
""",
)

entry(
    index = 94,
    label = "P142",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {9,S}
3  C u0 p0 c0 {1,S} {8,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {5,D} {12,S}
5  C u0 p0 c0 {2,S} {4,D} {13,S}
6  O u0 p2 c0 {1,S} {15,S}
7  O u0 p2 c0 {2,S} {16,S}
8  O u0 p2 c0 {3,S} {14,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81445,0.0113457,0.000218239,-4.54138e-07,2.83992e-10,-48975.9,12.6983], Tmin=(10,'K'), Tmax=(532.334,'K')),
            NASAPolynomial(coeffs=[2.03402,0.0644737,-4.34705e-05,1.3883e-08,-1.6793e-12,-49349.6,14.8752], Tmin=(532.334,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-407.273,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (378.308,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 3, 'C-O': 3, 'C=C': 1, 'C-H': 5, 'C-C': 4}
1D rotors:
* Invalidated! pivots: [1, 4], dihedral: [15, 1, 4, 5], invalidation reason: Another conformer for C5H8O3[248] exists which is 9.04 kJ/mol lower.Another conformer for C5H8O3[248] exists which is 9.04 kJ/mol lower.
* Invalidated! pivots: [2, 5], dihedral: [16, 2, 5, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [3, 6], dihedral: [14, 3, 6, 4], rotor symmetry: 1, max scan energy: 25.90 kJ/mol
* Invalidated! pivots: [4, 6], dihedral: [1, 4, 6, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.18542000    0.64315300   -1.42261000
O       2.18230400    0.77927700   -0.15131000
O      -0.19374200   -2.07603200   -1.20476200
C      -0.23494500    0.08185500   -0.12085800
C       1.17324500    0.12490300    0.61275200
C      -0.89535500   -1.28098800   -0.26118600
C      -0.69923300    0.99813900    1.00573700
C       0.49301300    1.03154100    1.61266100
H       1.53210200   -0.83894100    0.98904100
H      -0.87418000   -1.81256600    0.69294700
H      -1.94728800   -1.14565200   -0.55384500
H      -1.66554400    1.43292300    1.23557100
H       0.86429100    1.50767500    2.51233600
H      -0.10514000   -1.51246800   -1.98403800
H       0.61600600    1.18844300   -1.44191600
H       2.69102800    0.10238700   -0.61038200
""",
)

entry(
    index = 93,
    label = "P143",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {6,S} {9,S} {10,S}
2  C u0 p0 c0 {4,S} {5,D} {7,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {2,S} {3,D} {12,S}
5  C u0 p0 c0 {2,D} {8,S} {13,S}
6  O u0 p2 c0 {1,S} {14,S}
7  O u0 p2 c0 {2,S} {15,S}
8  O u0 p2 c0 {5,S} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.64641,0.0304294,8.32296e-05,-1.64823e-07,8.62856e-11,-54316.2,12.7475], Tmin=(10,'K'), Tmax=(649.675,'K')),
            NASAPolynomial(coeffs=[2.13626,0.0614167,-3.83931e-05,1.13681e-08,-1.28836e-12,-54577.7,15.859], Tmin=(649.675,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-451.66,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (378.308,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 3, 'C-O': 3, 'C=C': 2, 'C-H': 5, 'C-C': 2}
1D rotors:
* Invalidated! pivots: [1, 4], dihedral: [14, 1, 4, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 5], dihedral: [15, 2, 5, 7], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [3, 8], dihedral: [16, 3, 8, 5], rotor symmetry: 1, max scan energy: 40.28 kJ/mol
* Invalidated! pivots: [4, 6], dihedral: [1, 4, 6, 7], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [5, 7], dihedral: [2, 5, 7, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       2.27810700   -0.40451800    1.44367300
O       0.00726600   -1.81620300    1.68886000
O      -1.34364300   -4.11875400    1.88088600
C       1.96621500   -0.20689000    0.03970800
C       0.21085000   -2.76549300    0.70845300
C       1.85579500   -1.49299200   -0.73396100
C       1.09256400   -2.56003500   -0.41655000
C      -0.51189900   -3.90060100    0.83924300
H       1.02422300    0.34629700    0.05437600
H       2.72366900    0.44103400   -0.41131300
H       2.44960700   -1.55503500   -1.64004000
H       1.13968500   -3.41545100   -1.08575200
H      -0.49689000   -4.70139800    0.11366100
H       3.06096200   -0.96662500    1.48679400
H       0.83283600   -1.30708600    1.83212900
H      -1.27123400   -3.33943900    2.45393900
""",
)

entry(
    index = 94,
    label = "P144",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {10,S}
3  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {5,D} {8,S}
5  C u0 p0 c0 {1,S} {4,D} {13,S}
6  O u0 p2 c0 {2,S} {15,S}
7  O u0 p2 c0 {3,S} {14,S}
8  O u0 p2 c0 {4,S} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82289,0.0118421,0.000225807,-5.16399e-07,3.62039e-10,-50444.1,12.3846], Tmin=(10,'K'), Tmax=(464.261,'K')),
            NASAPolynomial(coeffs=[1.53921,0.0629785,-4.1059e-05,1.27764e-08,-1.51593e-12,-50571.1,17.9983], Tmin=(464.261,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-419.445,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (378.308,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 3, 'C-O': 3, 'C=C': 1, 'C-H': 5, 'C-C': 4}
1D rotors:
* Invalidated! pivots: [1, 5], dihedral: [15, 1, 5, 4], invalidation reason: The rotor scan has a barrier of 47.16 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)The rotor scan has a barrier of 47.16 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
* Invalidated! pivots: [2, 6], dihedral: [14, 2, 6, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [3, 7], dihedral: [16, 3, 7, 5], rotor symmetry: 1, max scan energy: 27.45 kJ/mol
* Invalidated! pivots: [4, 6], dihedral: [5, 4, 6, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       0.48782400    3.68724500   -0.87367500
O       0.43207400    2.92358500   -3.55337900
O       2.43184800    1.11913300   -0.29831100
C      -0.62490500    1.54347100   -1.81352700
C       0.16463900    2.33071000   -0.68580700
C      -0.79873800    2.33688500   -3.10895900
C       1.23316400    1.27392400   -0.88872900
C       0.53131500    0.54698800   -1.77469200
H      -1.60186000    1.15947900   -1.49543900
H      -0.32064000    2.25909400    0.29225100
H      -1.22391000    1.69798700   -3.89342000
H      -1.48100800    3.17486800   -2.95009500
H       0.68337100   -0.41988900   -2.23623200
H       1.08059900    2.20942800   -3.60080500
H       0.74421300    3.78031100   -1.80633600
H       2.62040100    1.91727200    0.20997200
""",
)

entry(
    index = 95,
    label = "P145",
    molecule = 
"""
multiplicity 3
1  O u0 p2 c0 {4,S} {14,S}
2  O u0 p2 c0 {6,S} {15,S}
3  O u0 p2 c0 {8,S} {16,S}
4  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
5  C u1 p0 c0 {4,S} {7,S} {11,S}
6  C u0 p0 c0 {2,S} {7,D} {8,S}
7  C u0 p0 c0 {5,S} {6,D} {12,S}
8  C u1 p0 c0 {3,S} {6,S} {13,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71095,0.0253144,0.000212892,-6.62886e-07,6.25527e-10,-28451.5,14.035], Tmin=(10,'K'), Tmax=(341.91,'K')),
            NASAPolynomial(coeffs=[2.42278,0.0616792,-4.00661e-05,1.24946e-08,-1.49078e-12,-28487.9,17.047], Tmin=(341.91,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-236.524,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (382.466,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 3, 'C-O': 3, 'C=C': 1, 'C-H': 5, 'C-C': 3}
1D rotors:
* Invalidated! pivots: [1, 4], dihedral: [14, 1, 4, 5], invalidation reason: Another conformer for C5H8O3[261] exists which is 5.15 kJ/mol lower.Another conformer for C5H8O3[261] exists which is 5.15 kJ/mol lower.
* Invalidated! pivots: [2, 6], dihedral: [15, 2, 6, 7], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 8], dihedral: [16, 3, 8, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 5], dihedral: [1, 4, 5, 7], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [5, 7], dihedral: [4, 5, 7, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [6, 8], dihedral: [2, 6, 8, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [6, 7], dihedral: [2, 6, 7, 5], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.84922200    1.28824200    0.76659200
O       0.58768000    1.24216900   -0.24674700
O       3.22372200    0.98716600   -0.31579300
C      -2.09786000   -0.08649000    0.30524200
C      -1.12083300   -1.06165500    0.85044900
C       1.03718700    0.00792000    0.07982700
C       0.29213000   -0.99397900    0.65494600
C       2.45490200   -0.12807700   -0.27410600
H      -3.12245700   -0.36459800    0.56330600
H      -2.03857600    0.01160300   -0.78504700
H      -1.51462300   -1.94403200    1.33986900
H       0.86505000   -1.86175300    0.96616300
H       2.99982000   -1.05280000   -0.15820300
H      -1.81298300    1.25445200    1.73122400
H      -0.30495000    1.41438700    0.15045400
H       2.61605000    1.74190500   -0.35406500
""",
)

entry(
    index = 96,
    label = "P146",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {6,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {5,D} {14,S}
5  C u0 p0 c0 {4,D} {15,S} {16,S}
6  C u0 p1 c0 {2,S} {3,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49763,0.0517038,-9.90804e-05,2.51404e-07,-2.25307e-10,41305.5,11.7234], Tmin=(10,'K'), Tmax=(426.317,'K')),
            NASAPolynomial(coeffs=[-0.00760905,0.0589978,-3.46899e-05,9.88541e-09,-1.09375e-12,41836.9,28.3735], Tmin=(426.317,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (343.419,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (378.308,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'C-H': 10, 'C-C': 4}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [4, 1, 2, 6], invalidation reason: Another conformer for C6H10[255] exists which is 0.74 kJ/mol lower.Another conformer for C6H10[255] exists which is 0.74 kJ/mol lower.
pivots: [1, 4], dihedral: [2, 1, 4, 5], rotor symmetry: 1, max scan energy: 10.22 kJ/mol
* Invalidated! pivots: [2, 6], dihedral: [1, 2, 6, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 6], dihedral: [11, 3, 6, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
C       1.34334200    1.62916100   -0.63732000
C       0.83075000    1.92777200    0.78386900
C      -1.07719900    2.59481200    2.16414200
C       2.83395000    1.45459800   -0.70134400
C       3.67003500    2.21712700   -1.39959200
C      -0.61580600    1.80633000    1.00773100
H       1.03610000    2.44166500   -1.30310800
H       0.83605200    0.72411600   -0.98871100
H       1.31794200    2.82275400    1.21399000
H       1.13475300    1.09418500    1.45903000
H      -0.32315300    2.95304000    2.88634400
H      -1.94360600    2.16451700    2.67258100
H      -1.47225400    3.48818400    1.64110100
H       3.24022800    0.63134100   -0.11344100
H       3.31282900    3.04915700   -1.99949900
H       4.73912700    2.03642700   -1.40376100
""",
)

entry(
    index = 97,
    label = "P147",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {6,D} {7,S}
4  C u1 p0 c0 {1,S} {6,S} {13,S}
5  C u0 p0 c0 {1,S} {7,D} {14,S}
6  C u0 p0 c0 {3,D} {4,S} {15,S}
7  C u0 p0 c0 {3,S} {5,D} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93931,0.00368693,0.00017161,-3.05222e-07,1.75589e-10,17932.2,11.8009], Tmin=(10,'K'), Tmax=(449.057,'K')),
            NASAPolynomial(coeffs=[-3.26757,0.0678706,-4.27448e-05,1.29473e-08,-1.50929e-12,18579.6,40.8015], Tmin=(449.057,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (149.074,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (378.308,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-H': 9, 'C-C': 5}
1D rotors:
pivots: [2, 3], dihedral: [10, 2, 3, 6], rotor symmetry: 12, max scan energy: 0.00 kJ/mol (set as a FreeRotor)


External symmetry: 1, optical isomers: 2

Geometry:
C      -1.94673800   -0.64125800   -0.14971800
C       2.35818200    0.34962600    0.15644600
C       0.89604100    0.01202100    0.07983000
C      -1.43659200    0.70333300    0.27883700
C      -0.84580900   -1.61900700   -0.44013700
C      -0.10494300    0.97660700    0.37450300
C       0.46763200   -1.28562500   -0.32557800
H      -2.60225000   -0.53520900   -1.03325600
H      -2.62479600   -1.05266900    0.61959100
H       2.52968100    1.25454600    0.74427600
H       2.78659800    0.52252800   -0.84003800
H       2.93515100   -0.46206600    0.61139100
H      -2.16746400    1.46873500    0.51786500
H      -1.12823700   -2.62039000   -0.74820300
H       0.20959200    1.96778400    0.69000100
H       1.22429900   -2.03348600   -0.54799100
""",
)

entry(
    index = 98,
    label = "P148",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {7,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {4,D} {13,S}
4  C u0 p0 c0 {3,D} {5,S} {15,S}
5  C u0 p0 c0 {4,S} {6,D} {14,S}
6  C u0 p0 c0 {5,D} {16,S} {17,S}
7  C u0 p1 c0 {1,S} {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.48217,0.0457526,2.23523e-05,-7.17202e-08,3.72674e-11,50826.5,12.166], Tmin=(10,'K'), Tmax=(722.13,'K')),
            NASAPolynomial(coeffs=[4.09152,0.0576578,-3.41174e-05,9.71498e-09,-1.06977e-12,50340.1,6.66598], Tmin=(722.13,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (422.541,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (399.095,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-H': 10, 'C-C': 4}
1D rotors:
pivots: [1, 3], dihedral: [7, 1, 3, 4], rotor symmetry: 1, max scan energy: 14.60 kJ/mol
* Invalidated! pivots: [1, 7], dihedral: [3, 1, 7, 2], invalidation reason: Bond ([[1, 3]]) broke during the scan. But unable to propose troubleshooting methods.Bond ([[1, 3]]) broke during the scan. But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 7], dihedral: [10, 2, 7, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 30.73 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -1.18235800   -0.30344500   -0.19457400
C      -3.39386400    0.18995900    0.72830400
C       0.25193300   -0.63948300    0.08063300
C       1.29156900    0.10437400   -0.31718400
C       2.68205800   -0.21699300   -0.03618600
C       3.72554200    0.52022800   -0.43152500
C      -2.16487500   -0.61473800    0.85258400
H      -1.29529200    0.66078200   -0.72323000
H      -1.59824400   -1.06684600   -0.90374100
H      -3.57643400    0.72147400   -0.22158500
H      -3.19822000    0.96184900    1.49819900
H      -4.29304200   -0.32629600    1.07374700
H       0.41569400   -1.54280700    0.66269200
H       2.85932000   -1.12513300    0.53645300
H       1.10891100    1.01536200   -0.88596600
H       4.74401700    0.23596200   -0.19640200
H       3.59084800    1.43264900   -1.00412200
""",
)

entry(
    index = 99,
    label = "P149",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {11,S}
3  C u0 p0 c0 {2,D} {5,S} {15,S}
4  C u0 p0 c0 {5,D} {6,S} {13,S}
5  C u0 p0 c0 {3,S} {4,D} {14,S}
6  C u0 p0 c0 {4,S} {7,D} {12,S}
7  C u0 p0 c0 {6,D} {16,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72485,0.0345324,5.40331e-05,-9.97846e-08,4.3927e-11,13749.1,10.6721], Tmin=(10,'K'), Tmax=(818.869,'K')),
            NASAPolynomial(coeffs=[4.45478,0.0565267,-3.30765e-05,9.252e-09,-9.99158e-13,12772.6,2.06395], Tmin=(818.869,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (114.34,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (394.937,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 3, 'C-H': 10, 'C-C': 3}
1D rotors:
pivots: [1, 2], dihedral: [8, 1, 2, 3], rotor symmetry: 3, max scan energy: 7.38 kJ/mol
pivots: [3, 5], dihedral: [2, 3, 5, 4], rotor symmetry: 1, max scan energy: 34.60 kJ/mol
pivots: [4, 6], dihedral: [5, 4, 6, 7], rotor symmetry: 1, max scan energy: 34.35 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       1.66811700    2.73889900    1.67525300
C       1.09050100    1.90440000    0.57495000
C       0.48395500    0.71852500    0.73930100
C      -0.67947100   -1.26730000   -0.17672900
C      -0.06892200   -0.07474200   -0.33728800
C      -1.22992100   -2.05424200   -1.26071000
C      -1.83771600   -3.23889200   -1.11165100
H       2.73952500    2.91212400    1.52019600
H       1.19641200    3.72790900    1.71155800
H       1.53863200    2.26507200    2.65105900
H       1.17812100    2.30667900   -0.43343700
H      -1.13143300   -1.63357600   -2.25983300
H      -0.77374900   -1.68086800    0.82609400
H       0.02272600    0.33439800   -1.34243400
H       0.39190000    0.30863300    1.74437100
H      -2.23204600   -3.78597800   -1.95922000
H      -1.95762600   -3.69503800   -0.13401300
""",
)

entry(
    index = 100,
    label = "P150",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {7,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {5,D} {12,S}
4  C u0 p0 c0 {2,S} {6,D} {13,S}
5  C u0 p0 c0 {3,D} {16,S} {17,S}
6  C u0 p0 c0 {4,D} {14,S} {15,S}
7  C u0 p1 c0 {1,S} {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85483,0.024925,6.62554e-05,-9.86035e-08,3.89918e-11,30465.2,12.4341], Tmin=(10,'K'), Tmax=(873.966,'K')),
            NASAPolynomial(coeffs=[2.12713,0.0574808,-3.1925e-05,8.55907e-09,-8.9321e-13,29825.8,15.1511], Tmin=(873.966,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (253.355,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (403.252,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-H': 10, 'C-C': 4}
1D rotors:
* Invalidated! pivots: [1, 3], dihedral: [7, 1, 3, 5], invalidation reason: Another conformer for C7H10[280] exists which is 1.52 kJ/mol lower.Another conformer for C7H10[280] exists which is 1.52 kJ/mol lower.
pivots: [1, 7], dihedral: [3, 1, 7, 2], rotor symmetry: 1, max scan energy: 13.28 kJ/mol
* Invalidated! pivots: [2, 4], dihedral: [7, 2, 4, 6], invalidation reason: Bond ([[2, 4]]) broke during the scan. But unable to propose troubleshooting methods.Bond ([[2, 4]]) broke during the scan. But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 7], dihedral: [4, 2, 7, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
C       0.68366600    0.15173900   -0.29943600
C      -1.45902300    0.56223700    1.34254200
C       1.94950100   -0.63105500   -0.07298000
C      -0.59921800   -0.43394700    2.06349800
C       2.55314000   -1.38872700   -0.98338500
C      -0.82908100   -1.60806700    1.15539400
C      -0.45331500   -0.26649800    0.59478400
H       0.38161200    0.06597100   -1.34952400
H       0.88039400    1.21723700   -0.11887500
H      -2.52629100    0.36449900    1.22564400
H      -1.21273400    1.61325800    1.47674400
H       2.37909700   -0.55582900    0.92475200
H       0.10550800   -0.29712300    2.86895200
H      -1.84342700   -1.98940500    1.02278800
H      -0.05606500   -2.37138300    1.13160800
H       2.15563500   -1.49444600   -1.98850400
H       3.46748300   -1.92732900   -0.76078700
""",
)

entry(
    index = 101,
    label = "P151",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {5,D} {15,S}
5  C u0 p0 c0 {2,S} {4,D} {14,S}
6  C u0 p0 c0 {2,S} {7,D} {13,S}
7  C u0 p0 c0 {6,D} {16,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75825,0.020838,0.000147275,-3.45517e-07,2.55302e-10,22161.9,11.6857], Tmin=(10,'K'), Tmax=(347.808,'K')),
            NASAPolynomial(coeffs=[0.00314081,0.0640243,-3.89764e-05,1.14858e-08,-1.30849e-12,22423.1,25.8362], Tmin=(347.808,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (184.255,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (399.095,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-H': 10, 'C-C': 5}
1D rotors:
pivots: [1, 3], dihedral: [2, 1, 3, 10], rotor symmetry: 3, max scan energy: 13.81 kJ/mol
pivots: [2, 6], dihedral: [1, 2, 6, 7], rotor symmetry: 1, max scan energy: 13.41 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -0.60560200    0.36301500    0.58650100
C       0.71703100   -0.31588300    0.02022600
C      -1.83952800   -0.52655800    0.69731700
C       0.20871200    0.62125200    1.84485900
C       1.32549400    0.06450300    1.36886300
C       1.32060000    0.29692000   -1.20322900
C       1.66286700   -0.36686500   -2.30494400
H      -0.85308200    1.27814600    0.03626300
H       0.59424700   -1.39564800   -0.11899100
H      -1.60751200   -1.45471300    1.22817600
H      -2.22609200   -0.78615900   -0.29284100
H      -2.64003300   -0.01930500    1.24496300
H       1.48462100    1.37316100   -1.15709200
H       2.32523800   -0.07299600    1.76587700
H      -0.04753300    1.08997100    2.78902100
H       1.52170100   -1.44052100   -2.38764300
H       2.09639400    0.13593000   -3.16216900
""",
)

entry(
    index = 102,
    label = "P152",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {7,D} {15,S}
5  C u0 p0 c0 {2,S} {6,D} {14,S}
6  C u0 p0 c0 {5,D} {7,S} {16,S}
7  C u0 p0 c0 {4,D} {6,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93668,0.00385629,0.000183615,-3.26827e-07,1.88193e-10,7338.2,11.2824], Tmin=(10,'K'), Tmax=(448.533,'K')),
            NASAPolynomial(coeffs=[-3.76446,0.0724948,-4.5795e-05,1.39519e-08,-1.6367e-12,8029.45,42.2658], Tmin=(448.533,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (60.9897,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (403.252,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-H': 10, 'C-C': 5}
1D rotors:
pivots: [1, 3], dihedral: [2, 1, 3, 11], rotor symmetry: 3, max scan energy: 14.65 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -0.84786900   -0.11225400    0.53203700
C       0.10351200   -1.30844200    0.30725900
C      -1.76325600    0.14352400   -0.68342400
C      -0.06383800    1.14328000    0.85611800
C       1.33479100   -0.94144300   -0.48384900
C       1.83791300    0.29812800   -0.41954800
C       1.17572900    1.32974800    0.38273000
H      -1.49275200   -0.35409500    1.38382500
H       0.42965900   -1.70181100    1.28212100
H      -0.44005600   -2.12528500   -0.17901100
H      -2.38741900   -0.73185400   -0.88984100
H      -1.17147900    0.36221200   -1.57595300
H      -2.42550800    0.99470300   -0.50238200
H       1.83456400   -1.71445900   -1.05886800
H      -0.56428600    1.92608300    1.41846300
H       2.75020800    0.55475200   -0.94802100
H       1.70337600    2.25937300    0.57059800
""",
)

entry(
    index = 103,
    label = "P153",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {6,S}
3  C u0 p0 c0 {2,D} {4,S} {13,S}
4  C u0 p0 c0 {3,S} {5,D} {12,S}
5  C u0 p0 c0 {4,D} {7,S} {11,S}
6  C u1 p0 c0 {2,S} {16,S} {17,S}
7  C u1 p0 c0 {5,S} {14,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.62814,0.0439078,4.10081e-06,-2.70014e-08,1.08278e-11,36904.4,14.3446], Tmin=(10,'K'), Tmax=(1055.67,'K')),
            NASAPolynomial(coeffs=[7.24472,0.0470789,-2.4382e-05,6.12775e-09,-6.03589e-13,35200.5,-7.75268], Tmin=(1055.67,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (306.86,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (399.095,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-H': 10, 'C-C': 4}
1D rotors:
pivots: [1, 2], dihedral: [8, 1, 2, 3], rotor symmetry: 3, max scan energy: 1.66 kJ/mol
* Invalidated! pivots: [2, 6], dihedral: [1, 2, 6, 16], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 18.22 kJ/mol
* Invalidated! pivots: [5, 7], dihedral: [4, 5, 7, 14], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 7], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
C      -2.40599200   -1.00261100   -0.34365900
C      -1.36042400    0.07868000   -0.15398300
C      -0.02274400   -0.28145500    0.05119600
C       0.48829200   -1.65755100    0.12740300
C       0.98797900   -2.37559100   -0.95421500
C      -1.73618300    1.40896400   -0.18501600
C       1.49407200   -3.65838300   -0.88765500
H      -2.17896000   -1.62354400   -1.21418800
H      -2.44209000   -1.67045900    0.52204000
H      -3.39839300   -0.57051100   -0.48129100
H       0.97595400   -1.88274800   -1.92455000
H       0.50744100   -2.14006000    1.10675700
H       0.69375500    0.52647500    0.20159000
H       1.86712600   -4.16406500   -1.76884600
H       1.53271600   -4.19813900    0.05233100
H      -2.76603300    1.70308600   -0.34453900
H      -1.00608700    2.19895000   -0.05103800
""",
)

entry(
    index = 104,
    label = "P154",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  C u0 p0 c0 {2,S} {5,D} {13,S}
4  C u0 p0 c0 {2,D} {7,S} {12,S}
5  C u0 p0 c0 {3,D} {6,S} {11,S}
6  C u1 p0 c0 {5,S} {14,S} {15,S}
7  C u1 p0 c0 {4,S} {16,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49208,0.0473388,-4.28274e-06,-2.04123e-08,9.25267e-12,36033.5,14.3398], Tmin=(10,'K'), Tmax=(998.613,'K')),
            NASAPolynomial(coeffs=[6.04251,0.0495783,-2.63557e-05,6.81343e-09,-6.90046e-13,34903,-1.07049], Tmin=(998.613,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (299.574,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (399.095,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-H': 10, 'C-C': 4}
1D rotors:
pivots: [1, 2], dihedral: [8, 1, 2, 3], rotor symmetry: 3, max scan energy: 6.07 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 5], rotor symmetry: 1, max scan energy: 22.60 kJ/mol
* Invalidated! pivots: [4, 7], dihedral: [2, 4, 7, 16], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [5, 6], dihedral: [3, 5, 6, 14], invalidation reason: The rotor scan has a barrier of 53.24 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)The rotor scan has a barrier of 53.24 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
* Invalidated! pivots: [3, 5], dihedral: [2, 3, 5, 6], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
* Invalidated! pivots: [2, 4], dihedral: [1, 2, 4, 7], invalidation reason: Another conformer for C7H10[286] exists which is 3.42 kJ/mol lower.Another conformer for C7H10[286] exists which is 3.42 kJ/mol lower.


External symmetry: 1, optical isomers: 2

Geometry:
C      -0.48157600   -1.99203200    0.58765300
C      -0.61503600   -0.51855000    0.31181700
C       0.31526700    0.37868500    1.02796200
C      -1.60067600   -0.02882700   -0.54673600
C       1.48233700    0.89916100    0.48360700
C       2.37379800    1.71773300    1.15075900
C      -1.83182900    1.29511000   -0.86165700
H       0.51357200   -2.35855700    0.30673900
H      -0.59496100   -2.20691800    1.65810200
H      -1.22890700   -2.57359900    0.04260700
H       1.70239500    0.64471100   -0.55151000
H      -2.24891400   -0.77236600   -1.00785100
H       0.08071600    0.61886600    2.06638800
H       2.20528300    2.00763100    2.18221600
H       3.26301500    2.09756400    0.66454600
H      -2.62940000    1.57307400   -1.53867800
H      -1.22579400    2.09062200   -0.44568800
""",
)

entry(
    index = 105,
    label = "P155",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {3,S} {5,D}
5  C u0 p0 c0 {1,S} {4,D} {15,S}
6  C u0 p0 c0 {1,S} {7,D} {14,S}
7  C u0 p0 c0 {6,D} {16,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63976,0.0316863,6.53397e-05,-1.4127e-07,8.33832e-11,20569.6,11.7287], Tmin=(10,'K'), Tmax=(449.123,'K')),
            NASAPolynomial(coeffs=[0.19873,0.0623334,-3.70179e-05,1.06694e-08,-1.19315e-12,20878.7,25.5753], Tmin=(449.123,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (170.994,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (399.095,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-H': 10, 'C-C': 5}
1D rotors:
pivots: [1, 6], dihedral: [2, 1, 6, 7], rotor symmetry: 1, max scan energy: 13.84 kJ/mol
pivots: [3, 4], dihedral: [11, 3, 4, 2], rotor symmetry: 3, max scan energy: 6.38 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -0.74068600    0.57180500   -0.00931500
C       0.24396300   -0.47044900   -0.67696500
C       2.81558700   -0.02121500    0.14941100
C       1.34851800    0.22938000    0.09953200
C       0.51659300    1.11034000    0.67050500
C      -1.80361100    0.00600100    0.87827500
C      -3.09750200    0.31142500    0.81853600
H      -1.18494800    1.25889400   -0.73772200
H       0.30365700   -0.40197700   -1.76830200
H       0.05358000   -1.51288900   -0.40195300
H       3.26452900    0.07716300   -0.84557000
H       3.31746000    0.67896400    0.82153400
H       3.02965400   -1.03969600    0.49263800
H      -1.45679000   -0.70321600    1.62957500
H       0.65896500    1.92560200    1.37231000
H      -3.82005400   -0.13100000    1.49511200
H      -3.48048400    1.01807200    0.08808100
""",
)

entry(
    index = 106,
    label = "P156",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {3,S} {7,D}
5  C u0 p0 c0 {1,S} {6,D} {15,S}
6  C u0 p0 c0 {2,S} {5,D} {14,S}
7  C u0 p0 c0 {4,D} {16,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68739,0.0331785,3.8943e-05,-6.88505e-08,2.80805e-11,21523.6,11.8457], Tmin=(10,'K'), Tmax=(870.974,'K')),
            NASAPolynomial(coeffs=[2.71811,0.055639,-3.07541e-05,8.23749e-09,-8.60643e-13,21009.3,12.4666], Tmin=(870.974,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (178.964,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (399.095,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-H': 10, 'C-C': 5}
1D rotors:
pivots: [1, 4], dihedral: [2, 1, 4, 3], rotor symmetry: 1, max scan energy: 15.39 kJ/mol
pivots: [3, 4], dihedral: [11, 3, 4, 1], rotor symmetry: 3, max scan energy: 7.73 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -0.49843100   -0.67911600   -0.24201400
C      -1.33399300    0.46735200   -0.95816200
C       1.83911900   -0.60224600   -1.24365300
C       0.96872400   -0.41252700   -0.02651400
C      -1.48815000   -0.50860900    0.89940900
C      -2.20461800    0.43547900    0.28268700
C       1.46474000   -0.02738200    1.15004400
H      -0.61762800   -1.63401900   -0.77063100
H      -1.81509000    0.17841700   -1.89785900
H      -0.77062100    1.39170700   -1.11316500
H       1.49188200    0.01927400   -2.07687000
H       1.80314100   -1.64113400   -1.59130700
H       2.88032900   -0.34664600   -1.03911000
H      -3.10028800    0.98440800    0.55045900
H      -1.57688600   -1.00689300    1.85812900
H       0.83117100    0.10798900    2.01892900
H       2.52353700    0.17049000    1.27938000
""",
)

entry(
    index = 107,
    label = "P157",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {3,S} {5,D}
5  C u0 p0 c0 {2,S} {4,D} {15,S}
6  C u0 p0 c0 {1,S} {7,D} {14,S}
7  C u0 p0 c0 {6,D} {16,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73166,0.0229036,0.000142824,-3.5889e-07,2.84094e-10,20409.5,11.7435], Tmin=(10,'K'), Tmax=(323.771,'K')),
            NASAPolynomial(coeffs=[0.596716,0.0616338,-3.66082e-05,1.05715e-08,-1.18489e-12,20612.5,23.3325], Tmin=(323.771,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (169.681,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (399.095,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-H': 10, 'C-C': 5}
1D rotors:
pivots: [1, 6], dihedral: [2, 1, 6, 7], rotor symmetry: 1, max scan energy: 14.34 kJ/mol
pivots: [3, 4], dihedral: [11, 3, 4, 1], rotor symmetry: 3, max scan energy: 5.89 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       0.33129400   -0.83152200    0.04214900
C      -0.68708600   -1.89938800   -0.52422300
C      -1.05033400    1.33248000    1.00911200
C      -0.92119600   -0.00681400    0.37165000
C      -1.77004300   -0.92245400   -0.11256500
C       1.28566000   -0.23411000   -0.94210200
C       2.59466700   -0.08458800   -0.75287200
H       0.87173000   -1.18440800    0.92788200
H      -0.67031500   -2.85830200    0.00351500
H      -0.58925900   -2.09041800   -1.59740600
H      -0.49035500    2.08947400    0.44939300
H      -2.09515100    1.64768000    1.06492200
H      -0.64011700    1.32471000    2.02550400
H       0.84039400    0.10663500   -1.87677000
H      -2.85202200   -0.96433000   -0.18056800
H       3.07600500   -0.40873500    0.16513700
H       3.23251300    0.36311900   -1.50677100
""",
)

entry(
    index = 108,
    label = "P158",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {6,D} {15,S}
5  C u0 p0 c0 {1,S} {7,D} {14,S}
6  C u0 p0 c0 {2,S} {4,D} {13,S}
7  C u0 p0 c0 {5,D} {16,S} {17,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89737,0.00641297,0.000204103,-3.99346e-07,2.47042e-10,21905.6,11.8217], Tmin=(10,'K'), Tmax=(494.593,'K')),
            NASAPolynomial(coeffs=[-1.37106,0.0684424,-4.29198e-05,1.30116e-08,-1.52117e-12,22189.2,31.1284], Tmin=(494.593,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (182.104,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (403.252,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-H': 10, 'C-C': 5}
1D rotors:
pivots: [1, 3], dihedral: [2, 1, 3, 10], rotor symmetry: 3, max scan energy: 18.26 kJ/mol
* Invalidated! pivots: [1, 5], dihedral: [2, 1, 5, 7], invalidation reason: Another conformer for C7H10[290] exists which is 0.81 kJ/mol lower.Another conformer for C7H10[290] exists which is 0.81 kJ/mol lower.


External symmetry: 1, optical isomers: 2

Geometry:
C      -0.33641600    0.11077700    0.21700700
C      -0.37126000    1.00637600   -1.09965900
C      -0.43687800   -1.39141500   -0.04040100
C      -1.67025600    0.80293600    0.53697400
C       0.76715500    0.51094600    1.15955400
C      -1.68081200    1.55193900   -0.56792400
C       1.60900400   -0.29335400    1.80459500
H       0.45071100    1.72274200   -1.19066500
H      -0.43374000    0.42484400   -2.02457700
H       0.49239800   -1.78469300   -0.46305300
H      -1.24747500   -1.60125600   -0.74247700
H      -0.64554500   -1.93724600    0.88435100
H      -2.36989700    2.29173600   -0.95922100
H       0.84829400    1.58585500    1.31700300
H      -2.33766500    0.69974100    1.38594300
H       1.58074800   -1.37205400    1.69945700
H       2.36623600    0.10755900    2.46902200
""",
)

entry(
    index = 109,
    label = "P159",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {5,D} {12,S}
4  C u0 p0 c0 {1,S} {7,D} {13,S}
5  C u0 p0 c0 {3,D} {14,S} {15,S}
6  C u0 p0 c0 {7,D} {16,S} {17,S}
7  C u0 p0 c0 {4,D} {6,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89378,0.0142178,0.00068471,-4.80518e-06,1.12764e-08,23266.1,10.0994], Tmin=(10,'K'), Tmax=(134.981,'K')),
            NASAPolynomial(coeffs=[3.28511,0.0554803,-3.19224e-05,8.98214e-09,-9.86274e-13,23261.4,11.0332], Tmin=(134.981,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (197.472,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (394.937,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 3, 'C-H': 10, 'C-C': 3}
1D rotors:
pivots: [1, 2], dihedral: [3, 1, 2, 9], rotor symmetry: 3, max scan energy: 13.33 kJ/mol
pivots: [1, 3], dihedral: [2, 1, 3, 5], rotor symmetry: 1, max scan energy: 13.63 kJ/mol
pivots: [1, 4], dihedral: [2, 1, 4, 7], rotor symmetry: 1, max scan energy: 8.00 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -0.28601400   -0.05589500    0.31032900
C      -1.00200800   -1.41291400    0.34683500
C      -1.27131500    1.07787400    0.13584200
C       0.77836000    0.03053600   -0.77791600
C      -1.44493300    2.08075300    0.99109900
C       1.28255400   -1.77336400   -2.59359100
C       1.02521600   -0.87250700   -1.68659900
H       0.22517800    0.09509600    1.26994600
H      -1.54056900   -1.59811300   -0.58656300
H      -1.72255600   -1.43847200    1.16720000
H      -0.28727400   -2.22771400    0.48526500
H      -1.86497800    1.03901900   -0.77645700
H       1.36247400    0.94926500   -0.79050500
H      -0.86740600    2.15284300    1.90819700
H      -2.17079200    2.86534200    0.80894000
H       2.01536100   -2.55671800   -2.42298400
H       0.77603400   -1.77224500   -3.55437200
""",
)

entry(
    index = 110,
    label = "P160",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {4,S} {5,S} {6,D}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {2,S} {3,D} {13,S}
5  C u0 p0 c0 {2,S} {7,D} {12,S}
6  C u0 p0 c0 {2,D} {14,S} {15,S}
7  C u0 p0 c0 {5,D} {16,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77374,0.0211816,0.000225731,-7.40909e-07,8.02371e-10,15635.8,12.1077], Tmin=(10,'K'), Tmax=(234.034,'K')),
            NASAPolynomial(coeffs=[1.36271,0.0623898,-3.83857e-05,1.14539e-08,-1.3204e-12,15748.7,20.238], Tmin=(234.034,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (130.031,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (399.095,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 3, 'C-H': 10, 'C-C': 3}
1D rotors:
pivots: [1, 3], dihedral: [8, 1, 3, 4], rotor symmetry: 3, max scan energy: 7.97 kJ/mol
* Invalidated! pivots: [2, 4], dihedral: [5, 2, 4, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [2, 5], dihedral: [4, 2, 5, 7], rotor symmetry: 1, max scan energy: 23.68 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       3.17787400    2.00215400    0.86291400
C      -0.06732000    0.71572300    2.60614500
C       1.82667100    1.92064900    1.50710100
C       1.27965300    0.80761600    2.00240600
C      -0.23972100   -0.08285800    3.82950800
C      -1.13299400    1.32108600    2.05160400
C       0.73645800   -0.63838700    4.55314200
H       3.09894000    2.35906700   -0.17044100
H       3.67755300    1.03075900    0.84809800
H       3.82474400    2.71285600    1.38937000
H       1.26774700    2.85204100    1.57603900
H      -1.26948900   -0.21032600    4.15544100
H       1.85770400   -0.11466600    1.97892500
H      -1.05279800    1.87706000    1.12576800
H      -2.11330200    1.26335800    2.51211000
H       0.51391000   -1.21235900    5.44481800
H       1.78277600   -0.53208700    4.29049400
""",
)

entry(
    index = 111,
    label = "P161",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {4,S} {7,D}
4  C u0 p0 c0 {3,S} {6,D} {15,S}
5  C u0 p0 c0 {2,S} {7,D} {14,S}
6  C u0 p0 c0 {4,D} {16,S} {17,S}
7  C u0 p0 c0 {3,D} {5,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83462,0.0182099,0.000383545,-1.88177e-06,3.19848e-09,20482.4,11.4718], Tmin=(10,'K'), Tmax=(147.866,'K')),
            NASAPolynomial(coeffs=[2.30513,0.0595857,-3.61938e-05,1.07003e-08,-1.22553e-12,20527.6,15.9271], Tmin=(147.866,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (170.738,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (394.937,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 3, 'C-H': 10, 'C-C': 3}
1D rotors:
pivots: [1, 3], dihedral: [8, 1, 3, 4], rotor symmetry: 3, max scan energy: 9.35 kJ/mol
pivots: [2, 5], dihedral: [11, 2, 5, 7], rotor symmetry: 3, max scan energy: 6.54 kJ/mol
pivots: [3, 4], dihedral: [1, 3, 4, 6], rotor symmetry: 1, max scan energy: 26.60 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -1.94559700    1.83366000    0.19608400
C      -2.39861100   -2.37906200    2.07624900
C      -1.12380900    0.56088400    0.21552200
C       0.32032700    0.63127400   -0.05021900
C      -2.23966400   -1.75918500    0.70792700
C       1.01041600    1.74553600   -0.31392100
C      -1.68607800   -0.60468300    0.46314100
H      -1.88064900    2.32121200   -0.78188000
H      -1.57708200    2.54478700    0.94225300
H      -2.99366400    1.62359900    0.40775200
H      -3.45572800   -2.55575700    2.30079600
H      -1.89278400   -3.34911200    2.12248400
H      -1.98348300   -1.73638600    2.85360200
H      -2.62477300   -2.33709100   -0.13314100
H       0.84264800   -0.32092100   -0.02345300
H       2.07709000    1.70830100   -0.49985500
H       0.54448700    2.72330200   -0.35396700
""",
)

entry(
    index = 112,
    label = "P162",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  C u0 p0 c0 {2,D} {5,S} {13,S}
4  C u0 p0 c0 {2,S} {7,D} {12,S}
5  C u0 p0 c0 {3,S} {6,D} {11,S}
6  C u0 p0 c0 {5,D} {14,S} {15,S}
7  C u0 p0 c0 {4,D} {16,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.64386,0.0309318,7.85032e-05,-1.58857e-07,8.59837e-11,14142.5,11.2484], Tmin=(10,'K'), Tmax=(609.549,'K')),
            NASAPolynomial(coeffs=[1.31164,0.0621611,-3.75356e-05,1.0916e-08,-1.22564e-12,14131,18.9187], Tmin=(609.549,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (117.54,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (399.095,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 3, 'C-H': 10, 'C-C': 3}
1D rotors:
pivots: [1, 2], dihedral: [8, 1, 2, 3], rotor symmetry: 3, max scan energy: 5.13 kJ/mol
pivots: [2, 4], dihedral: [1, 2, 4, 7], rotor symmetry: 1, max scan energy: 29.94 kJ/mol
* Invalidated! pivots: [3, 5], dihedral: [2, 3, 5, 6], invalidation reason: Inconsistent initial and final conformers But unable to propose troubleshooting methods.Inconsistent initial and final conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
C       0.71007500    1.47645600    0.19606700
C       0.46566600    0.02078100   -0.10754400
C       1.37298600   -0.96243600    0.11634200
C      -0.82902500   -0.34935400   -0.67775600
C       2.70656200   -0.83718000    0.66747900
C       3.53439800   -1.87544800    0.85178800
C      -1.84000800    0.48069800   -0.96476600
H      -0.03231300    1.85179300    0.90785900
H       0.61559300    2.08084800   -0.71192400
H       1.69724200    1.65849800    0.61667300
H       3.05341700    0.15314800    0.94626300
H      -0.95932700   -1.41033100   -0.87991000
H       1.07770100   -1.97703300   -0.14524600
H       4.52619300   -1.74426000    1.26705300
H       3.24134900   -2.88771100    0.59142400
H      -2.76466600    0.10663700   -1.38752100
H      -1.78497500    1.54910800   -0.79166800
""",
)

entry(
    index = 113,
    label = "P163",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {6,D}
3  C u0 p0 c0 {2,S} {4,D} {13,S}
4  C u0 p0 c0 {3,D} {5,S} {12,S}
5  C u0 p0 c0 {4,S} {7,D} {11,S}
6  C u0 p0 c0 {2,D} {16,S} {17,S}
7  C u0 p0 c0 {5,D} {14,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82023,0.0118512,0.000233818,-5.23822e-07,3.59824e-10,13638.6,12.0935], Tmin=(10,'K'), Tmax=(473.121,'K')),
            NASAPolynomial(coeffs=[1.2382,0.0665013,-4.35019e-05,1.3566e-08,-1.611e-12,13515.6,18.7359], Tmin=(473.121,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (113.363,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (394.937,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 3, 'C-H': 10, 'C-C': 3}
1D rotors:
pivots: [1, 2], dihedral: [8, 1, 2, 3], rotor symmetry: 3, max scan energy: 9.63 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 29.00 kJ/mol
pivots: [4, 5], dihedral: [3, 4, 5, 7], rotor symmetry: 1, max scan energy: 33.41 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C      -2.01099000    0.95443700   -0.10610700
C      -1.50021600   -0.45729400   -0.26241900
C      -2.40555200   -1.57137800    0.00356700
C      -3.69473900   -1.47922800    0.38746900
C      -4.54577400   -2.62648000    0.63719500
C      -0.23429800   -0.70161300   -0.63986200
C      -5.82740400   -2.55358900    1.01878900
H      -2.85900900    1.14361200   -0.77199400
H      -2.35668000    1.13844300    0.91613000
H      -1.22974300    1.67996300   -0.33635900
H      -4.08992900   -3.60502400    0.49855500
H      -4.15019600   -0.50192000    0.52599000
H      -1.97838900   -2.56400200   -0.12658100
H      -6.32073400   -1.59833800    1.16851200
H      -6.42020400   -3.44333600    1.19246200
H       0.13546400   -1.71496500   -0.75299400
H       0.46420200    0.10122900   -0.84525400
""",
)

entry(
    index = 114,
    label = "P164",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {5,D} {7,S}
4  C u0 p0 c0 {1,S} {6,D} {13,S}
5  C u0 p0 c0 {3,D} {16,S} {17,S}
6  C u0 p0 c0 {4,D} {14,S} {15,S}
7  C u0 p1 c0 {1,S} {3,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.69924,0.0424352,5.44342e-06,-2.5469e-08,9.5273e-12,50003.1,12.1596], Tmin=(10,'K'), Tmax=(1129.02,'K')),
            NASAPolynomial(coeffs=[8.29969,0.0446392,-2.20676e-05,5.29155e-09,-4.98268e-13,47785,-15.8157], Tmin=(1129.02,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (415.784,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (403.252,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-H': 10, 'C-C': 4}
1D rotors:
* Invalidated! pivots: [1, 4], dihedral: [7, 1, 4, 6], invalidation reason: Another conformer for C7H10[300] exists which is 11.14 kJ/mol lower.Another conformer for C7H10[300] exists which is 11.14 kJ/mol lower.
* Invalidated! pivots: [1, 7], dihedral: [4, 1, 7, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [2, 3], dihedral: [10, 2, 3, 5], rotor symmetry: 3, max scan energy: 2.96 kJ/mol
* Invalidated! pivots: [3, 7], dihedral: [2, 3, 7, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
C      -0.37740500   -2.05625700    0.43638300
C      -0.98337400    1.66166700    0.48419100
C      -1.25038500    0.23760400    0.05436000
C      -0.71405400   -3.32754300    1.16912200
C      -2.01692600   -0.06219800   -1.03186800
C      -0.99023500   -4.48218600    0.57308700
C      -0.98868500   -0.82487200    0.95839900
H       0.68523100   -1.79940500    0.65153500
H      -0.41250500   -2.18843000   -0.66065500
H       0.09420300    1.84005500    0.55683900
H      -1.39465600    2.37604100   -0.23233000
H      -1.40828900    1.84775300    1.47294600
H      -0.74022200   -3.24444400    2.25215200
H      -1.23419900   -5.37058700    1.14413800
H      -0.98579300   -4.58256700   -0.50841900
H      -2.19804700   -1.08589300   -1.33514100
H      -2.60662300    0.70247800   -1.52818000
""",
)

entry(
    index = 115,
    label = "P165",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {7,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {4,S} {5,D}
4  C u0 p0 c0 {3,S} {6,D} {13,S}
5  C u0 p0 c0 {3,D} {14,S} {15,S}
6  C u0 p0 c0 {4,D} {16,S} {17,S}
7  C u0 p1 c0 {1,S} {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75231,0.0222366,0.00010114,-1.78661e-07,9.04984e-11,27168.8,12.3133], Tmin=(10,'K'), Tmax=(636.828,'K')),
            NASAPolynomial(coeffs=[0.050889,0.0633586,-3.78181e-05,1.08786e-08,-1.21002e-12,27277.9,25.6548], Tmin=(636.828,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (225.861,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (399.095,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-H': 10, 'C-C': 4}
1D rotors:
* Invalidated! pivots: [1, 3], dihedral: [7, 1, 3, 4], invalidation reason: The rotor scan has a barrier of 125.19 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)The rotor scan has a barrier of 125.19 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
* Invalidated! pivots: [1, 7], dihedral: [3, 1, 7, 2], invalidation reason: The rotor scan has a barrier of 50.63 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)The rotor scan has a barrier of 50.63 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
pivots: [2, 7], dihedral: [10, 2, 7, 1], rotor symmetry: 3, max scan energy: 7.91 kJ/mol
pivots: [3, 4], dihedral: [1, 3, 4, 6], rotor symmetry: 1, max scan energy: 19.51 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       0.28048200   -0.83931600   -1.05992600
C       2.01995900    1.08634200   -0.26213400
C      -0.58017300    0.34212500   -0.71520300
C      -1.34266500    0.65378900    0.48443300
C      -0.16942900    1.23049800   -1.86354400
C      -1.80446100   -0.23940600    1.36375600
C       0.87756000    0.53694200   -1.05411100
H       0.12289900   -1.36234200   -2.00499000
H       0.56538000   -1.48819700   -0.23440500
H       2.95800600    1.02590500   -0.82356200
H       2.15335900    0.52855700    0.66975600
H       1.85364600    2.13774100   -0.00921900
H      -1.53530200    1.71205200    0.65369600
H      -0.27166400    2.30300600   -1.70802500
H      -0.37956600    0.90770300   -2.88519000
H      -2.34156200    0.07153400    2.25170500
H      -1.66627800   -1.30523100    1.21780100
""",
)

entry(
    index = 116,
    label = "P166",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {5,D}
3  C u0 p0 c0 {1,S} {6,D} {10,S}
4  C u0 p0 c0 {2,S} {7,D} {11,S}
5  C u0 p0 c0 {2,D} {14,S} {15,S}
6  C u0 p0 c0 {3,D} {16,S} {17,S}
7  C u0 p0 c0 {4,D} {12,S} {13,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.5821,0.0401733,2.8635e-05,-6.68179e-08,3.03118e-11,17422,12.5003], Tmin=(10,'K'), Tmax=(812.108,'K')),
            NASAPolynomial(coeffs=[3.85711,0.0558989,-3.19588e-05,8.82195e-09,-9.45643e-13,16814.1,7.763], Tmin=(812.108,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (144.835,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (399.095,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 3, 'C-H': 10, 'C-C': 3}
1D rotors:
pivots: [1, 2], dihedral: [3, 1, 2, 4], rotor symmetry: 1, max scan energy: 27.64 kJ/mol
* Invalidated! pivots: [1, 3], dihedral: [2, 1, 3, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [2, 4], dihedral: [1, 2, 4, 7], rotor symmetry: 1, max scan energy: 24.17 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       0.54329900    0.68561800   -0.67917600
C      -0.88181200    0.27760000   -0.34080500
C       1.58203400    0.32066600    0.34272900
C      -1.89812200    0.38211700   -1.39566300
C      -1.23919800   -0.14702600    0.87953900
C       2.33981800    1.18916400    1.00515200
C      -1.71162500    0.81467100   -2.64671700
H       0.81274500    0.21234100   -1.63267900
H       0.56806800    1.76612900   -0.86424200
H       1.71260300   -0.74429500    0.52584500
H      -2.89895800    0.07810100   -1.09676300
H      -0.74574300    1.13946500   -3.01594700
H      -2.53562700    0.85952400   -3.34885400
H      -0.52923900   -0.21993700    1.69365200
H      -2.26603000   -0.42229400    1.09441600
H       3.08927400    0.86295400    1.71754500
H       2.24003900    2.26038700    0.85684200
""",
)

entry(
    index = 117,
    label = "P167",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {4,D} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {5,D} {11,S}
4  C u0 p0 c0 {2,D} {5,S} {13,S}
5  C u0 p0 c0 {3,D} {4,S} {12,S}
6  C u1 p0 c0 {2,S} {14,S} {15,S}
7  C u1 p0 c0 {2,S} {16,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63501,0.0328924,0.000102935,-2.83668e-07,2.29475e-10,32402.4,12.5649], Tmin=(10,'K'), Tmax=(319.61,'K')),
            NASAPolynomial(coeffs=[1.227,0.0630292,-3.85039e-05,1.13547e-08,-1.29288e-12,32556.3,21.4354], Tmin=(319.61,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (269.399,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (399.095,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-H': 10, 'C-C': 4}
1D rotors:
pivots: [1, 3], dihedral: [8, 1, 3, 5], rotor symmetry: 3, max scan energy: 5.79 kJ/mol
* Invalidated! pivots: [2, 6], dihedral: [4, 2, 6, 14], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 7], dihedral: [4, 2, 7, 16], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 5], dihedral: [2, 4, 5, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [2, 4], dihedral: [6, 2, 4, 5], rotor symmetry: 2, max scan energy: 37.51 kJ/mol
* Invalidated! pivots: [3, 5], dihedral: [1, 3, 5, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
C       2.73582900    1.06115400   -0.39949500
C      -1.22868400   -2.01595900    0.43143200
C       2.09689900   -0.19848400    0.08984700
C       0.16812100   -1.66493600    0.47986200
C       0.75968400   -0.47633000    0.01639600
C      -1.61984900   -3.26082400    0.95146100
C      -2.20301500   -1.16048000   -0.11442500
H       3.49386100    0.85343700   -1.16492500
H       2.00127500    1.74621400   -0.82969300
H       3.25483400    1.58707800    0.41147900
H       2.75576100   -0.94147600    0.53552700
H       0.11801900    0.27889200   -0.43236700
H       0.83095300   -2.40326400    0.92397100
H      -0.89595900   -3.94339400    1.37887600
H      -2.65727900   -3.57026400    0.93816900
H      -1.96121900   -0.19169600   -0.52861700
H      -3.24289400   -1.46102700   -0.13222700
""",
)

entry(
    index = 118,
    label = "P168",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {6,S} {7,D}
5  C u0 p0 c0 {1,S} {6,D} {14,S}
6  C u0 p0 c0 {4,S} {5,D} {15,S}
7  C u0 p0 c0 {4,D} {16,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94177,0.00380563,0.000203255,-3.93495e-07,2.49008e-10,7622.7,12.2586], Tmin=(10,'K'), Tmax=(406.291,'K')),
            NASAPolynomial(coeffs=[-2.87905,0.0709779,-4.48153e-05,1.36755e-08,-1.60818e-12,8176.79,39.0196], Tmin=(406.291,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (63.37,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (403.252,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-H': 10, 'C-C': 5}
1D rotors:
pivots: [1, 3], dihedral: [2, 1, 3, 11], rotor symmetry: 3, max scan energy: 14.03 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -0.97850200   -0.03222500    0.49639500
C       0.39314100    0.70248500    0.56095200
C      -2.13357900    0.84234800   -0.00990100
C       1.39372600   -0.22784300   -0.11580300
C      -0.68118100   -1.22225200   -0.38927900
C       0.61591900   -1.31588600   -0.70908800
C       2.72236600   -0.08364800   -0.15841500
H      -1.25025200   -0.39824200    1.49631400
H       0.33755800    1.64764800    0.01037200
H       0.68913400    0.94543400    1.58393800
H      -1.91767300    1.22876600   -1.01056800
H      -3.06776800    0.27527100   -0.06208200
H      -2.29898100    1.69549800    0.65459500
H      -1.45267800   -1.91886600   -0.69893100
H       1.06139500   -2.09741300   -1.31349700
H       3.35013400   -0.80140100   -0.67484300
H       3.22211800    0.75144400    0.31963800
""",
)

entry(
    index = 119,
    label = "P169",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {6,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {2,S} {7,D}
5  C u0 p0 c0 {1,S} {6,D} {15,S}
6  C u0 p0 c0 {3,S} {5,D} {14,S}
7  C u0 p0 c0 {4,D} {16,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71324,0.0270508,0.000181322,-6.43564e-07,7.41793e-10,25340.5,11.8464], Tmin=(10,'K'), Tmax=(219.826,'K')),
            NASAPolynomial(coeffs=[1.97853,0.0586158,-3.40635e-05,9.63173e-09,-1.05889e-12,25416.7,17.5874], Tmin=(219.826,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (210.712,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (399.095,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-H': 10, 'C-C': 5}
1D rotors:
pivots: [1, 5], dihedral: [2, 1, 5, 6], rotor symmetry: 1, max scan energy: 13.71 kJ/mol
pivots: [3, 6], dihedral: [11, 3, 6, 5], rotor symmetry: 3, max scan energy: 7.88 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -1.37416300   -0.27191900   -0.23109900
C      -1.78384000    0.82228200    0.79351200
C       1.65514600   -0.63514900   -2.66370400
C      -2.66856700    0.43461300   -0.30343200
C      -0.30862400   -0.00307100   -1.22338300
C       0.57672400   -0.90188300   -1.65513000
C      -3.79465100    0.61907500   -0.96380100
H      -1.39813800   -1.28933100    0.15325300
H      -1.26920400    1.77771700    0.73825800
H      -2.01119600    0.49252100    1.80294500
H       1.63350600    0.40135400   -3.00911100
H       2.64862400   -0.83209100   -2.24481100
H       1.55017700   -1.28586200   -3.53939400
H       0.52906600   -1.91511900   -1.25786400
H      -0.27581700    1.01154300   -1.61920200
H      -4.52932100    1.34846200   -0.63707100
H      -4.02595200    0.04402800   -1.85463500
""",
)

entry(
    index = 120,
    label = "P170",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {8,S}
2  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {9,S} {12,S} {13,S}
4  C u0 p0 c0 {9,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {2,S} {6,D}
6  C u0 p0 c0 {5,D} {7,S} {17,S}
7  C u0 p0 c0 {6,S} {8,D} {18,S}
8  C u0 p0 c0 {1,S} {7,D} {19,S}
9  C u0 p1 c0 {3,S} {4,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.2953,0.0766526,-0.000219896,6.17105e-07,-5.96957e-10,28635.9,13.3989], Tmin=(10,'K'), Tmax=(379.06,'K')),
            NASAPolynomial(coeffs=[-0.737539,0.0761441,-4.74706e-05,1.41398e-08,-1.61754e-12,29251.1,33.0239], Tmin=(379.06,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (238.066,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (448.981,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 10, 'C-O': 2, 'C=C': 2, 'C-C': 5}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [5, 2, 3, 9], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [2, 5], dihedral: [3, 2, 5, 1], rotor symmetry: 1, max scan energy: 8.70 kJ/mol
* Invalidated! pivots: [3, 9], dihedral: [2, 3, 9, 4], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
pivots: [4, 9], dihedral: [14, 4, 9, 3], rotor symmetry: 3, max scan energy: 7.58 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.74195100   -1.24207300    0.79822700
C       0.10994300   -0.58041400   -0.88066400
C      -1.12556300   -0.60114400    0.04037800
C      -3.56687500   -0.65712400    0.17525300
C       1.38794300   -0.32749000   -0.15884700
C       2.33361300    0.64943100   -0.22388100
C       3.33760100    0.32016100    0.74719700
C       2.92813700   -0.83079900    1.33553000
C      -2.36579800   -1.12931800   -0.53653100
H       0.14986800   -1.53487500   -1.41501600
H      -0.01512700    0.19912300   -1.63635900
H      -0.97650900   -1.39862400    0.80274200
H      -1.21436700    0.33149300    0.62777100
H      -4.39525000   -1.36974600    0.15841200
H      -3.43879500   -0.21301000    1.17753500
H      -3.88484500    0.16002200   -0.50192100
H       2.32115900    1.50061100   -0.88631600
H       4.23804000    0.86964600    0.97135700
H       3.33585800   -1.45935600    2.10879000
""",
)

entry(
    index = 121,
    label = "P171",
    molecule = 
"""
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {6,S}
3  C u0 p0 c0 {1,S} {4,S} {7,S} {11,S}
4  C u0 p0 c0 {2,S} {3,S} {8,S} {12,S}
5  C u0 p0 c0 {1,S} {9,S} {13,S} {14,S}
6  C u0 p0 c0 {2,S} {10,S} {15,S} {16,S}
7  C u0 p0 c0 {3,S} {9,D} {18,S}
8  C u0 p0 c0 {4,S} {10,D} {20,S}
9  C u0 p0 c0 {5,S} {7,D} {17,S}
10 C u0 p0 c0 {6,S} {8,D} {19,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87786,0.00824387,0.00027916,-5.97273e-07,4.1007e-10,-18069,14.9974], Tmin=(10,'K'), Tmax=(432.832,'K')),
            NASAPolynomial(coeffs=[-2.52571,0.086037,-5.49453e-05,1.66917e-08,-1.94026e-12,-17689,38.5143], Tmin=(432.832,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-150.245,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (478.082,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 10, 'C-O': 4, 'C=C': 2, 'C-C': 5}
1D rotors:
pivots: [3, 4], dihedral: [1, 3, 4, 2], rotor symmetry: 1, max scan energy: 29.28 kJ/mol


External symmetry: 2, optical isomers: 2

Geometry:
O      -1.82790300    1.03961600    0.02670400
O       1.67657400    0.68007700   -0.98099800
C      -0.73111800    0.57827000   -0.77686000
C       0.58666400    1.01459300   -0.10825000
C      -2.75356700   -0.02973300    0.25575000
C       2.69776000   -0.00979600   -0.25019100
C      -0.94383900   -0.90539800   -0.89930400
C       0.91669500    0.33725400    1.19321200
C      -2.08770800   -1.24794500   -0.31952800
C       2.11039900   -0.23783800    1.11412300
H      -0.76306900    1.06260700   -1.76448900
H       0.53304800    2.10629600    0.01951400
H      -2.94849400   -0.11555200    1.33265100
H      -3.71205400    0.19121200   -0.23704100
H       3.61099000    0.60250100   -0.21197200
H       2.94806200   -0.94315000   -0.77103400
H      -2.51385800   -2.24142700   -0.26195400
H      -0.25117400   -1.55706900   -1.41313300
H       2.62017800   -0.78478500    1.89700200
H       0.25815500    0.36007000    2.05011500
""",
)

entry(
    index = 122,
    label = "P172",
    molecule = 
"""
multiplicity 3
1  O u1 p2 c0 {9,S}
2  O u1 p2 c0 {10,S}
3  C u0 p0 c0 {4,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {3,S} {8,S} {13,S} {14,S}
5  C u0 p0 c0 {6,S} {7,S} {15,S} {16,S}
6  C u0 p0 c0 {5,S} {8,S} {17,S} {18,S}
7  C u0 p0 c0 {3,S} {5,S} {9,D}
8  C u0 p0 c0 {4,S} {6,S} {10,D}
9  C u0 p0 c0 {1,S} {7,D} {19,S}
10 C u0 p0 c0 {2,S} {8,D} {20,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71418,0.0436905,4.71329e-05,-8.46179e-08,3.36071e-11,-9787.5,13.9306], Tmin=(10,'K'), Tmax=(929.975,'K')),
            NASAPolynomial(coeffs=[5.54569,0.0656137,-3.62956e-05,9.64688e-09,-9.96683e-13,-11416.8,-1.7009], Tmin=(929.975,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-81.3072,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (482.239,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 10, 'C-O': 2, 'C=C': 2, 'C-C': 6}
1D rotors:
* Invalidated! pivots: [7, 9], dihedral: [3, 7, 9, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [8, 10], dihedral: [4, 8, 10, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
O      -3.43119400    1.15474200    0.29147200
O       3.43215100   -1.13545200   -0.39122400
C      -0.64601000    1.28751000   -0.48444900
C       0.70738200    1.28498200    0.27606700
C      -0.70642500   -1.26569200   -0.37582000
C       0.64696800   -1.26821900    0.38469700
C      -1.42193100    0.03733200   -0.22122500
C       1.42288800   -0.01804100    0.12147300
C      -2.80287400    0.10296400    0.15338800
C       2.80383100   -0.08367300   -0.25314100
H      -1.24655400    2.15779400   -0.21772800
H      -0.43752600    1.35080800   -1.56272500
H       1.33142400    2.11900400   -0.05685100
H       0.49835500    1.45069200    1.34364800
H      -0.49739700   -1.43140100   -1.44340000
H      -1.33046700   -2.09971300   -0.04290200
H       1.24751100   -2.13850300    0.11797600
H       0.43848300   -1.33151800    1.46297200
H      -3.30147900   -0.87224400    0.32101200
H       3.30243600    0.89153500   -0.42076400
""",
)

entry(
    index = 123,
    label = "P173",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C u1 p0 c0 {1,S} {7,S} {8,S}
3 C u0 p0 c0 {1,S} {4,T}
4 C u0 p0 c0 {3,T} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93222,0.00658403,0.000141423,-5.2827e-07,6.75665e-10,43711.9,10.5497], Tmin=(10,'K'), Tmax=(197.04,'K')),
            NASAPolynomial(coeffs=[2.91296,0.0272754,-1.60948e-05,4.67772e-09,-5.30527e-13,43752,13.8114], Tmin=(197.04,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (363.465,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (203.705,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C#C': 1, 'C-H': 5, 'C-C': 2}
1D rotors:
pivots: [1, 2], dihedral: [3, 1, 2, 7], rotor symmetry: 1, max scan energy: 1.98 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -0.56588500   -0.40366100   -0.00253800
C      -1.06672100    0.96109200    0.35362100
C       0.88041000   -0.48133800   -0.20010200
C       2.06893000   -0.53734500   -0.36317800
H      -1.06612600   -0.76421800   -0.91693400
H      -0.86016200   -1.12660100    0.77326800
H      -0.41838900    1.82415400    0.30552000
H      -2.11019300    1.09573600    0.60844700
H       3.12007200   -0.58937100   -0.50653900
""",
)

entry(
    index = 124,
    label = "P174",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {11,S}
2  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {5,S} {6,S} {9,S}
4  C u0 p0 c0 {1,S} {2,S} {5,D}
5  C u0 p0 c0 {3,S} {4,D} {10,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94676,0.00313904,0.00011224,-2.00406e-07,1.12499e-10,-5225.75,8.69431], Tmin=(10,'K'), Tmax=(538.613,'K')),
            NASAPolynomial(coeffs=[-0.0794394,0.0433094,-2.82329e-05,8.86352e-09,-1.06579e-12,-4941,24.2443], Tmin=(538.613,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-43.4709,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (253.591,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-O': 1, 'H-O': 1, 'C-C': 3, 'C=C': 1}
1D rotors:
pivots: [1, 4], dihedral: [11, 1, 4, 2], rotor symmetry: 1, max scan energy: 20.37 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O       2.11963700    0.46777100    0.14752700
C      -0.19605900   -0.11066000    1.03821900
C      -1.20941600   -0.26227800   -0.15630700
C       0.81232300    0.18532100   -0.03795000
C      -0.03459000    0.06084500   -1.07122500
H      -2.02408500    0.46803900   -0.14593200
H      -0.40771300    0.71286800    1.72556300
H      -0.01701000   -1.02248200    1.61438000
H      -1.63373200   -1.26575700   -0.25701600
H       0.05740700    0.15042200   -2.14606500
H       2.53324100    0.61590900   -0.71119200
""",
)

entry(
    index = 125,
    label = "P175",
    molecule = 
"""
multiplicity 3
1  O u0 p2 c0 {2,S} {11,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  C u0 p0 c0 {2,D} {5,S} {6,S}
4  C u1 p0 c0 {2,S} {8,S} {9,S}
5  C u1 p0 c0 {3,S} {7,S} {10,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {5,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86001,0.00914788,0.000146706,-3.44838e-07,2.42118e-10,17723.4,10.3307], Tmin=(10,'K'), Tmax=(484.161,'K')),
            NASAPolynomial(coeffs=[3.98268,0.0359609,-2.25752e-05,6.96235e-09,-8.32067e-13,17385.4,6.45969], Tmin=(484.161,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (147.331,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-O': 1, 'H-O': 1, 'C-C': 2, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [11, 1, 2, 3], invalidation reason: Another conformer for C4H6O[212] exists which is 0.80 kJ/mol lower.Another conformer for C4H6O[212] exists which is 0.80 kJ/mol lower.
* Invalidated! pivots: [2, 4], dihedral: [1, 2, 4, 8], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 5], dihedral: [2, 3, 5, 7], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
O       1.27896800    0.82166800    1.48239000
C       0.76116500    0.38660200    0.28200100
C       1.50845500    0.61851600   -0.86990200
C      -0.53818800   -0.28695700    0.31564700
C       2.73134700    1.25004000   -0.91915100
H       1.06422300    0.25988100   -1.79334700
H       3.24508900    1.38886000   -1.86122100
H      -1.46734600    0.27038800    0.22665900
H      -0.61486000   -1.36292900    0.45089700
H       3.20740000    1.62174700   -0.02147200
H       0.65901800    0.59433900    2.18365500
""",
)

entry(
    index = 126,
    label = "P176",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {12,S}
2  O u0 p2 c0 {5,S} {13,S}
3  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
4  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
5  C u0 p0 c0 {2,S} {6,D} {11,S}
6  C u1 p0 c0 {3,S} {5,D}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89422,0.0103192,0.00023246,-8.15779e-07,9.70741e-10,-13732.2,11.9004], Tmin=(10,'K'), Tmax=(212.249,'K')),
            NASAPolynomial(coeffs=[1.92185,0.0474898,-3.02295e-05,9.31751e-09,-1.10454e-12,-13648.5,18.3587], Tmin=(212.249,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-114.139,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-O': 2, 'H-O': 2, 'C-C': 2, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [1, 3], dihedral: [12, 1, 3, 4], invalidation reason: Another conformer for C4H7O2[219] exists which is 1.55 kJ/mol lower.Another conformer for C4H7O2[219] exists which is 1.55 kJ/mol lower.
* Invalidated! pivots: [2, 5], dihedral: [13, 2, 5, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [3, 4], dihedral: [1, 3, 4, 8], rotor symmetry: 3, max scan energy: 15.15 kJ/mol
* Invalidated! pivots: [3, 6], dihedral: [1, 3, 6, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.35715600   -0.27945000   -1.41633800
O      -2.42664000    2.25881800   -0.50524000
C      -0.92904900   -0.50391700   -0.04241500
C      -1.07628200   -1.97223600    0.34582900
C      -2.30672900    1.57184000    0.67845400
C      -1.66600100    0.43043800    0.84321200
H       0.13425900   -0.24263200   -0.06035700
H      -0.53322200   -2.60266900   -0.36155300
H      -2.13114800   -2.26434000    0.34858300
H      -0.68058000   -2.14467000    1.34944700
H      -2.80697700    2.08894900    1.49027500
H      -2.23835400   -0.66511700   -1.50075800
H      -1.98980100    1.72179200   -1.18531600
""",
)

entry(
    index = 127,
    label = "P177",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {6,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  C u0 p0 c0 {3,S} {5,D} {10,S}
5  C u0 p0 c0 {4,D} {11,S} {12,S}
6  O u0 p2 c0 {1,S} {2,S}
7  O u0 p2 c0 {1,S} {13,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80653,0.012245,0.00018675,-4.26451e-07,2.86345e-10,-10532.4,11.9823], Tmin=(10,'K'), Tmax=(511.416,'K')),
            NASAPolynomial(coeffs=[4.40728,0.0471906,-3.20249e-05,1.03136e-08,-1.25922e-12,-11112.3,4.41821], Tmin=(511.416,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-87.6265,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-O': 3, 'H-O': 1, 'C-C': 2, 'C=C': 2}
1D rotors:
pivots: [2, 3], dihedral: [13, 2, 3, 1], rotor symmetry: 1, max scan energy: 23.26 kJ/mol
pivots: [5, 6], dihedral: [4, 5, 6, 7], rotor symmetry: 1, max scan energy: 31.40 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.22307900   -0.77587900   -0.38621100
O       3.08270700    0.75167800    0.08447600
C       2.24250500   -0.20898100    0.55735300
C       0.82733500   -0.05107600    0.69773400
C      -0.30014400    0.41360900    1.23295900
C      -1.61505600    0.17377400    0.66485100
C      -2.76143700    0.62829000    1.18358400
H       2.79577300   -0.97677600    1.08466600
H      -0.21661900    0.99754400    2.14353400
H      -1.64048100   -0.42058800   -0.24484200
H      -2.77930500    1.22450300    2.09049900
H      -3.71551600    0.41627100    0.71720300
H       2.56113300    1.49481500   -0.24218700
""",
)

entry(
    index = 128,
    label = "P178",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {8,S}
3  C u0 p0 c0 {1,S} {2,S} {9,D}
4  C u0 p0 c0 {1,S} {5,D} {10,S}
5  C u0 p0 c0 {4,D} {11,S} {12,S}
6  O u0 p2 c0 {2,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75561,0.0199049,0.000183247,-5.69776e-07,5.23033e-10,-8251.71,11.8924], Tmin=(10,'K'), Tmax=(368.779,'K')),
            NASAPolynomial(coeffs=[3.79763,0.0458503,-2.96716e-05,9.26147e-09,-1.10767e-12,-8434.34,9.29756], Tmin=(368.779,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-68.5855,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-O': 1, 'C=O': 1, 'H-O': 1, 'C-C': 4, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [1, 4], dihedral: [13, 1, 4, 3], invalidation reason: Bond ([[3, 4]]) broke during the scan. But unable to propose troubleshooting methods.Bond ([[3, 4]]) broke during the scan. But unable to propose troubleshooting methods.
pivots: [3, 6], dihedral: [4, 3, 6, 7], rotor symmetry: 1, max scan energy: 14.03 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.64874600   -1.06051000   -0.29559600
O      -0.18977400   -1.23324700    2.63875600
C      -2.30256600    0.06335000    1.97322200
C      -1.37371900   -0.10391400    0.67649100
C      -0.95632800   -0.57623400    2.00165600
C      -3.50448500   -0.77261100    2.16612100
C      -4.61868100   -0.36726800    2.77416800
H      -2.37811300    1.09776700    2.30072200
H      -0.97375900    0.84927100    0.32853800
H      -3.44229400   -1.78568300    1.77805200
H      -5.46587200   -1.03203100    2.89341500
H      -4.71934700    0.63439000    3.17954100
H      -2.35177900   -0.71977800   -0.86077200
""",
)

entry(
    index = 129,
    label = "P179",
    molecule = 
"""
1  O u0 p2 c0 {7,D}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {4,D} {11,S}
4  C u0 p0 c0 {3,D} {5,D}
5  C u0 p0 c0 {4,D} {6,D}
6  C u0 p0 c0 {5,D} {7,D}
7  C u0 p0 c0 {1,D} {6,D}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.43734,0.0533135,-0.000107102,1.6613e-07,-1.06232e-10,37476.5,11.6014], Tmin=(10,'K'), Tmax=(465.567,'K')),
            NASAPolynomial(coeffs=[4.71147,0.0344528,-2.08378e-05,6.09313e-09,-6.89349e-13,37443.6,7.34962], Tmin=(465.567,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (311.576,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (253.591,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 4, 'C=O': 1, 'C=C': 4, 'C-C': 1}
1D rotors:
pivots: [2, 3], dihedral: [8, 2, 3, 4], rotor symmetry: 3, max scan energy: 5.46 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O       5.00968700   -0.45355100   -0.16777700
C      -2.21743700    0.73429800    0.13558300
C      -1.30250300   -0.44238100   -0.02077900
C       0.01792900   -0.38868600   -0.04508900
C       1.28379900   -0.36986700   -0.07214800
C       2.56929200   -0.32687600   -0.09688200
C       3.83927900   -0.41128800   -0.13590100
H      -2.89315700    0.80274500   -0.72495700
H      -1.66429300    1.66797200    0.23012600
H      -2.85289600    0.60229300    1.01908600
H      -1.78970000   -1.41465700   -0.12128200
""",
)

entry(
    index = 130,
    label = "P180",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u1 p0 c0 {1,S} {4,D}
4  C u0 p0 c0 {3,D} {5,D}
5  C u0 p0 c0 {4,D} {6,D}
6  C u0 p0 c0 {5,D} {12,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 O u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.44413,0.0461391,-4.02719e-05,2.24448e-08,-5.96958e-12,34856.3,12.7666], Tmin=(10,'K'), Tmax=(775.12,'K')),
            NASAPolynomial(coeffs=[5.36234,0.0362403,-2.1116e-05,5.96926e-09,-6.55765e-13,34558.9,4.00097], Tmin=(775.12,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (289.746,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (278.535,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C=O': 1, 'C=C': 3, 'C-C': 2}
1D rotors:
pivots: [2, 3], dihedral: [4, 2, 3, 10], rotor symmetry: 3, max scan energy: 11.77 kJ/mol
* Invalidated! pivots: [2, 4], dihedral: [3, 2, 4, 5], invalidation reason: 
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 7], invalidation reason: 


External symmetry: 1, optical isomers: 1

Geometry:
O       5.09474100    0.34820400   -0.27132500
C      -1.27342600   -0.40995300    0.35915800
C      -2.07533700    0.31765100   -0.73538000
C       0.16723800   -0.26610800    0.25528800
C       1.38740600   -0.13356500    0.15243600
C       2.69834000   -0.00385900    0.06026200
C       3.93686900    0.18779700   -0.12499100
H      -1.51271900   -1.48184100    0.35240300
H      -1.58287600   -0.05604500    1.35174400
H      -1.80637600   -0.05488200   -1.72559600
H      -3.14637800    0.15995300   -0.58664500
H      -1.87837800    1.39110100   -0.71159400
""",
)

entry(
    index = 131,
    label = "P181",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {9,S} {10,S}
3  C u0 p0 c0 {5,S} {6,D} {11,S}
4  C u0 p0 c0 {1,S} {5,T}
5  C u0 p0 c0 {3,S} {4,T}
6  C u0 p0 c0 {3,D} {12,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83797,0.0211779,0.000457496,-3.53295e-06,8.33198e-09,39990.8,14.7673], Tmin=(10,'K'), Tmax=(146.76,'K')),
            NASAPolynomial(coeffs=[4.24429,0.0392123,-2.43416e-05,7.28805e-09,-8.41121e-13,39947.5,12.5188], Tmin=(146.76,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (335.065,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C#C': 1, 'C=O': 1, 'C-C': 3, 'C=C': 1}
1D rotors:
pivots: [2, 3], dihedral: [5, 2, 3, 10], rotor symmetry: 1, max scan energy: 1.71 kJ/mol
* Invalidated! pivots: [2, 5], dihedral: [3, 2, 5, 6], invalidation reason: 
pivots: [4, 6], dihedral: [7, 4, 6, 5], rotor symmetry: 1, max scan energy: 0.05 kJ/mol (set as a FreeRotor)


External symmetry: 1, optical isomers: 2

Geometry:
O       4.16260100   -0.07082200    0.56617600
C      -1.53114600   -0.74160000   -0.52589500
C      -2.46723500    0.09488800    0.29027500
C       2.26470700    0.73920500   -0.81177400
C      -0.17011200   -0.21898700   -0.62476300
C       0.95434800    0.21240000   -0.69817300
C       3.27131200    0.30129100   -0.07272300
H      -1.48079400   -1.76468300   -0.11421700
H      -1.93956100   -0.87920700   -1.53822400
H      -3.52673100   -0.12904200    0.28623400
H      -2.09266400    0.86412300    0.95072200
H       2.49962200    1.53170500   -1.51583000
""",
)

entry(
    index = 132,
    label = "P182",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {3,S} {5,S} {7,D}
3  C u0 p0 c0 {2,S} {6,D} {12,S}
4  C u0 p0 c0 {1,S} {8,D} {13,S}
5  C u0 p0 c0 {2,S} {14,D} {15,S}
6  C u0 p0 c0 {3,D} {16,S} {17,S}
7  C u0 p0 c0 {2,D} {8,D}
8  C u0 p0 c0 {4,D} {7,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 O u0 p2 c0 {5,D}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74189,0.0601226,-3.43663e-05,8.2337e-09,-5.11169e-13,24576.3,12.101], Tmin=(10,'K'), Tmax=(1615.81,'K')),
            NASAPolynomial(coeffs=[27.3431,0.0136505,-2.32188e-06,-4.09029e-10,1.17654e-13,15388.8,-117.915], Tmin=(1615.81,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (204.321,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (394.937,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 8, 'C=O': 1, 'C=C': 4, 'C-C': 3}
1D rotors:
pivots: [2, 5], dihedral: [10, 2, 5, 9], rotor symmetry: 3, max scan energy: 5.44 kJ/mol
pivots: [3, 4], dihedral: [6, 3, 4, 7], rotor symmetry: 1, max scan energy: 27.23 kJ/mol
pivots: [3, 6], dihedral: [4, 3, 6, 1], rotor symmetry: 1, max scan energy: 47.55 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O       0.85366500   -4.68824700    1.80352900
C       2.24323000    1.50900200   -1.53077000
C       0.81130000   -2.39821900    1.13511400
C      -0.24104800   -2.06596000    2.09909300
C       2.54604100    0.04741400   -1.38381800
C       1.28470300   -3.80870000    1.09318800
C      -0.79047200   -0.86231800    2.28237400
C       1.38569100   -1.54043200    0.28615500
C       1.95312600   -0.76870500   -0.52901600
H       1.46384100    1.83101900   -0.84041500
H       1.92069600    1.73139800   -2.55415600
H       3.14376900    2.10605300   -1.34810300
H      -0.56709500   -2.91360100    2.69304500
H       3.31487100   -0.36447300   -2.03554300
H       2.08008300   -4.00279000    0.34688200
H      -0.48568600    0.00369000    1.70427800
H      -1.56661500   -0.71251100    3.02292800
""",
)

entry(
    index = 133,
    label = "P183",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {4,S} {7,S} {8,D}
4  C u0 p0 c0 {3,S} {5,D} {14,S}
5  C u0 p0 c0 {4,D} {15,S} {16,S}
6  C u0 p0 c0 {1,S} {7,T}
7  C u0 p0 c0 {3,S} {6,T}
8  C u0 p0 c0 {3,D} {17,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 O u0 p2 c0 {8,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67077,0.0347481,0.000348241,-1.76895e-06,2.6793e-09,22157.4,16.307], Tmin=(10,'K'), Tmax=(225.406,'K')),
            NASAPolynomial(coeffs=[4.03427,0.0606109,-3.8902e-05,1.20731e-08,-1.43995e-12,22058.9,13.274], Tmin=(225.406,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (184.298,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (394.937,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 8, 'C#C': 1, 'C=O': 1, 'C=C': 2, 'C-C': 4}
1D rotors:
pivots: [2, 3], dihedral: [7, 2, 3, 12], rotor symmetry: 3, max scan energy: 12.57 kJ/mol
* Invalidated! pivots: [2, 7], dihedral: [3, 2, 7, 8], invalidation reason: 
pivots: [4, 5], dihedral: [8, 4, 5, 6], rotor symmetry: 1, max scan energy: 24.84 kJ/mol
pivots: [4, 8], dihedral: [5, 4, 8, 7], rotor symmetry: 1, max scan energy: 0.03 kJ/mol (set as a FreeRotor)


External symmetry: 1, optical isomers: 2

Geometry:
O       1.44376000   -3.39426700   -1.28461200
C      -2.16584400    0.92364900   -0.46469700
C      -2.31724100    1.21839300    1.03883600
C       1.36964400   -0.90704000   -1.40835700
C       2.57872600   -0.16770500   -1.80654500
C       2.65533500    1.16034800   -1.90665100
C      -0.91028000    0.26368100   -0.81155300
C       0.13169700   -0.28387400   -1.08053700
C       1.40768100   -2.23822500   -1.34175200
H      -2.99953200    0.29806300   -0.80425000
H      -2.24159700    1.85758600   -1.03346200
H      -3.27290700    1.71105800    1.23574800
H      -1.51475100    1.87080800    1.38914500
H      -2.27978800    0.29535400    1.62109600
H       3.44998700   -0.77775000   -2.02674400
H       3.57948800    1.63800000   -2.20576000
H       1.80483200    1.79710800   -1.69427600
""",
)

entry(
    index = 134,
    label = "P184",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {7,D}
2  C u0 p0 c0 {5,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {4,D} {6,S} {7,S}
4  C u0 p0 c0 {3,D} {8,S} {13,S}
5  C u0 p0 c0 {2,S} {9,D} {14,S}
6  C u0 p0 c0 {3,S} {9,D} {15,S}
7  C u0 p0 c0 {1,D} {3,S} {18,S}
8  C u1 p0 c0 {4,S} {16,S} {17,S}
9  C u0 p0 c0 {5,D} {6,D}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.13653,0.0764133,-0.000108756,1.50304e-07,-9.28953e-11,19754,14.3728], Tmin=(10,'K'), Tmax=(515.458,'K')),
            NASAPolynomial(coeffs=[2.70251,0.0664001,-4.06776e-05,1.18923e-08,-1.33868e-12,19976.6,17.9034], Tmin=(515.458,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (164.194,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (419.881,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 9, 'C=O': 1, 'C=C': 3, 'C-C': 4}
1D rotors:
pivots: [2, 5], dihedral: [10, 2, 5, 9], rotor symmetry: 3, max scan energy: 6.40 kJ/mol
pivots: [3, 6], dihedral: [4, 3, 6, 9], rotor symmetry: 1, max scan energy: 43.01 kJ/mol
* Invalidated! pivots: [3, 7], dihedral: [4, 3, 7, 1], invalidation reason: Another conformer for C8H9O[201] exists which is 1.21 kJ/mol lower.Another conformer for C8H9O[201] exists which is 1.21 kJ/mol lower.
* Invalidated! pivots: [4, 8], dihedral: [3, 4, 8, 16], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [3, 4], dihedral: [6, 3, 4, 8], rotor symmetry: 1, max scan energy: 37.81 kJ/mol
* Invalidated! pivots: [6, 9], dihedral: [3, 6, 9, 5], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
O      -3.26261400    0.23289200    2.30315000
C       2.62294800   -1.43803500   -1.16383400
C      -1.10603700    0.03961600    1.26845700
C      -1.31442500    0.87916000    0.12310400
C       2.29717500   -0.49653100   -0.02751000
C       0.15217800   -0.61766300    1.49071400
C      -2.12906300   -0.21408000    2.28519800
C      -2.44406400    1.54927200   -0.19925300
C       1.23244300   -0.55182900    0.71766000
H       3.56776500   -1.95580900   -0.97089400
H       2.74223600   -0.88266100   -2.09930200
H       1.83982800   -2.18422600   -1.30022900
H      -0.45787100    0.97106200   -0.54038600
H       3.02676200    0.28942200    0.17576600
H       0.22174500   -1.23165900    2.38872400
H      -2.47492500    2.15494200   -1.09774500
H      -3.32892600    1.50023900    0.41825900
H      -1.78784500   -0.88795700    3.10087200
""",
)

entry(
    index = 135,
    label = "P185",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {11,S}
3  C u0 p0 c0 {2,D} {5,S} {15,S}
4  C u0 p0 c0 {5,D} {6,S} {12,S}
5  C u0 p0 c0 {3,S} {4,D} {13,S}
6  C u0 p0 c0 {4,S} {8,D} {14,S}
7  C u0 p0 c0 {1,S} {16,D} {17,S}
8  C u0 p0 c0 {6,D} {18,S} {19,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {3,S}
16 O u0 p2 c0 {7,D}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.16176,0.0925894,-0.000312417,8.97246e-07,-9.07264e-10,1333.66,15.2639], Tmin=(10,'K'), Tmax=(349.553,'K')),
            NASAPolynomial(coeffs=[0.238761,0.0790077,-5.23202e-05,1.62905e-08,-1.92556e-12,1825.33,30.4032], Tmin=(349.553,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (11.0628,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (440.667,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 10, 'C=O': 1, 'C=C': 3, 'C-C': 4}
1D rotors:
pivots: [2, 3], dihedral: [8, 2, 3, 4], rotor symmetry: 1, max scan energy: 8.54 kJ/mol
pivots: [2, 8], dihedral: [3, 2, 8, 1], rotor symmetry: 1, max scan energy: 10.63 kJ/mol
pivots: [4, 6], dihedral: [3, 4, 6, 5], rotor symmetry: 1, max scan energy: 34.81 kJ/mol
pivots: [5, 7], dihedral: [6, 5, 7, 9], rotor symmetry: 1, max scan energy: 34.23 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -4.09370200    1.50818100   -1.32807800
C      -2.98444300    0.18647500    0.36679900
C      -1.68050400    0.31455800   -0.35517800
C      -0.50391600    0.56264200    0.23904900
C       1.94214100    0.91806100    0.13626700
C       0.75729000    0.67503900   -0.46142300
C       3.20310300    1.03094100   -0.56706900
C      -4.14042700    0.93426100   -0.27188100
C       4.38251400    1.27117400    0.02097800
H      -2.90668100    0.50351500    1.41396800
H      -3.31244400   -0.86618200    0.41252800
H      -1.72144400    0.20288900   -1.43501400
H       1.97222900    1.04048900    1.21782700
H       0.72867800    0.55342900   -1.54279700
H       3.16569000    0.90905000   -1.64786600
H      -0.47175800    0.69223700    1.32030300
H      -5.08533400    0.89885000    0.31557500
H       5.29830700    1.34702100   -0.55231400
H       4.46404200    1.39957200    1.09571700
""",
)

entry(
    index = 136,
    label = "P186",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {4,D} {10,S}
3  C u0 p0 c0 {1,S} {7,D} {11,S}
4  C u0 p0 c0 {2,D} {5,S} {13,S}
5  C u0 p0 c0 {4,S} {8,D} {12,S}
6  C u0 p0 c0 {1,S} {14,D} {15,S}
7  C u0 p0 c0 {3,D} {18,S} {19,S}
8  C u0 p0 c0 {5,D} {16,S} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {4,S}
14 O u0 p2 c0 {6,D}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.46501,0.0687977,-4.36408e-05,1.34322e-08,-1.60418e-12,4476.82,14.7137], Tmin=(10,'K'), Tmax=(1710.45,'K')),
            NASAPolynomial(coeffs=[24.6134,0.0240319,-8.49692e-06,1.33792e-09,-7.08383e-14,-3444.09,-100.673], Tmin=(1710.45,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (37.1647,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (440.667,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 10, 'C=O': 1, 'C=C': 3, 'C-C': 4}
1D rotors:
pivots: [2, 3], dihedral: [4, 2, 3, 5], rotor symmetry: 1, max scan energy: 14.05 kJ/mol
pivots: [2, 4], dihedral: [3, 2, 4, 8], rotor symmetry: 1, max scan energy: 11.68 kJ/mol
pivots: [2, 7], dihedral: [3, 2, 7, 1], rotor symmetry: 1, max scan energy: 10.11 kJ/mol
pivots: [5, 6], dihedral: [3, 5, 6, 9], rotor symmetry: 1, max scan energy: 30.47 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.91632600   -2.72438700   -0.49302700
C      -1.12384400   -0.53010900    0.19617400
C       0.25537300   -0.22377100   -0.34704200
C      -2.21646300    0.09646700   -0.63111200
C       1.28469800    0.22707800    0.38379200
C       2.60950900    0.49956900   -0.14989800
C      -1.24017200   -2.06021400    0.24640600
C      -2.96330400    1.11984100   -0.23259000
C       3.63522000    0.95475400    0.57765000
H      -1.17390600   -0.17234100    1.23152700
H       0.39498500   -0.41323900   -1.40957300
H      -2.37699100   -0.34900600   -1.60849000
H       2.75077500    0.31303000   -1.21231600
H       1.14010300    0.41889900    1.44592500
H      -0.59446800   -2.53141400    1.01904100
H       3.53357700    1.15209300    1.64019200
H       4.60588700    1.14324200    0.13557200
H      -3.73511800    1.53792300   -0.86861800
H      -2.83360000    1.57886700    0.74306300
""",
)

entry(
    index = 137,
    label = "P187",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {9,S}
3  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {5,D} {13,S}
5  C u0 p0 c0 {2,S} {4,D} {15,S}
6  C u0 p0 c0 {1,S} {8,D} {14,S}
7  C u0 p0 c0 {1,S} {16,D} {17,S}
8  C u0 p0 c0 {6,D} {18,S} {19,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {5,S}
16 O u0 p2 c0 {7,D}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91231,0.0121502,0.000804576,-5.48778e-06,1.33641e-08,7612.28,9.55089], Tmin=(10,'K'), Tmax=(102.899,'K')),
            NASAPolynomial(coeffs=[2.4137,0.0704043,-4.4591e-05,1.36714e-08,-1.61414e-12,7643.12,13.373], Tmin=(102.899,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (69.59,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (444.824,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 6, 'C=O': 1, 'C=C': 2, 'C-H': 10}
1D rotors:
pivots: [2, 7], dihedral: [3, 2, 7, 9], rotor symmetry: 1, max scan energy: 14.07 kJ/mol
pivots: [2, 8], dihedral: [3, 2, 8, 1], rotor symmetry: 1, max scan energy: 15.67 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 11], rotor symmetry: 3, max scan energy: 12.27 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.93175000    0.07738000    2.56339500
C      -0.56610900    0.53364000    0.21219100
C       0.76338100   -0.04386500   -0.53665000
C       1.92771300   -0.62546900    0.26046500
C      -0.24154200    1.81227900   -0.55147500
C       0.87791500    1.35244800   -1.11391700
C      -1.84719900   -0.18716100   -0.08299300
C      -0.31334000    0.65626700    1.70636500
C      -2.65143400    0.07483300   -1.10969200
H       0.42470000   -0.77314200   -1.27811600
H       1.62528400   -1.52481100    0.80414400
H       2.73509100   -0.90797000   -0.42216700
H       2.33962100    0.08648000    0.97907000
H      -0.77068000    2.75720300   -0.59362800
H      -2.10438300   -0.97314300    0.62104900
H       1.62019400    1.79733000   -1.76755400
H       0.52525300    1.33512200    1.97023700
H      -3.55875000   -0.49604700   -1.27082500
H      -2.43620900    0.86314100   -1.82398100
""",
)

# entry(
#     index = 138,
#     label = "P188",
#     molecule = 
# """
# multiplicity 3
# 1  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
# 2  C u0 p0 c0 {4,S} {6,S} {7,D}
# 3  C u0 p0 c0 {1,S} {5,D} {12,S}
# 4  C u1 p0 c0 {2,S} {5,S} {13,S}
# 5  C u0 p0 c0 {3,D} {4,S} {15,S}
# 6  C u0 p0 c0 {2,S} {8,D} {14,S}
# 7  C u0 p0 c0 {2,D} {16,S} {17,S}
# 8  C u0 p0 c0 {6,D} {18,S} {19,S}
# 9  H u0 p0 c0 {1,S}
# 10 H u0 p0 c0 {1,S}
# 11 H u0 p0 c0 {1,S}
# 12 H u0 p0 c0 {3,S}
# 13 H u0 p0 c0 {4,S}
# 14 H u0 p0 c0 {6,S}
# 15 H u0 p0 c0 {5,S}
# 16 O u1 p2 c0 {7,S}
# 17 H u0 p0 c0 {7,S}
# 18 H u0 p0 c0 {8,S}
# 19 H u0 p0 c0 {8,S}
# """,
#     thermo = NASA(
#         polynomials = [
#             NASAPolynomial(coeffs=[3.21664,0.0801848,-0.000158618,3.49505e-07,-3.06497e-10,19424.2,15.7696], Tmin=(10,'K'), Tmax=(394.561,'K')),
#             NASAPolynomial(coeffs=[1.66441,0.0732588,-4.61331e-05,1.38767e-08,-1.60184e-12,19723,24.0501], Tmin=(394.561,'K'), Tmax=(3000,'K')),
#         ],
#         Tmin = (10,'K'),
#         Tmax = (3000,'K'),
#         E0 = (161.485,'kJ/mol'),
#         Cp0 = (33.2579,'J/(mol*K)'),
#         CpInf = (444.824,'J/(mol*K)'),
#     ),
#     shortDesc = """""",
#     longDesc = 
# """
# Bond corrections: {'C-H': 10, 'C-O': 1, 'C=C': 3, 'C-C': 4}
# 1D rotors:
# pivots: [2, 4], dihedral: [10, 2, 4, 6], rotor symmetry: 3, max scan energy: 4.83 kJ/mol
# pivots: [3, 5], dihedral: [7, 3, 5, 6], rotor symmetry: 1, max scan energy: 22.60 kJ/mol
# pivots: [3, 7], dihedral: [5, 3, 7, 9], rotor symmetry: 1, max scan energy: 61.00 kJ/mol
# * Invalidated! pivots: [5, 6], dihedral: [3, 5, 6, 4], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
# * Invalidated! pivots: [3, 8], dihedral: [5, 3, 8, 1], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
# * Invalidated! pivots: [4, 6], dihedral: [2, 4, 6, 5], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
# * Invalidated! pivots: [7, 9], dihedral: [3, 7, 9, 18], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers


# External symmetry: 1, optical isomers: 2

# Geometry:
# O       3.88122200    0.14425400   -0.07187200
# C      -2.76095800   -1.84168000    0.72535000
# C       1.55831000    0.63839100   -0.24697600
# C      -1.82982100   -0.69108900    0.92045400
# C       0.25777000    0.52132500    0.43960400
# C      -0.61758200   -0.54318900    0.26873800
# C       1.71398700    1.28154900   -1.49660400
# C       2.75535100    0.08870600    0.39869300
# C       0.70632800    1.84213200   -2.22541000
# H      -3.74485200   -1.50524000    0.37477500
# H      -2.93892300   -2.37564700    1.66734000
# H      -2.37154700   -2.55939200   -0.00046700
# H      -2.13224400    0.07934900    1.62660200
# H      -0.01330600    1.31235500    1.13828000
# H       2.73174600    1.31270800   -1.87520200
# H      -0.32586600   -1.32189500   -0.43498900
# H       2.57526300   -0.40333700    1.37445600
# H      -0.32086900    1.82505700   -1.88021800
# H       0.90657600    2.31999800   -3.17656000
# """,
# )

entry(
    index = 139,
    label = "P189",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {5,S} {6,S} {7,D}
4  C u0 p0 c0 {1,S} {5,D} {14,S}
5  C u0 p0 c0 {3,S} {4,D} {15,S}
6  C u0 p0 c0 {3,S} {8,D} {16,S}
7  C u0 p0 c0 {3,D} {9,S} {17,S}
8  C u0 p0 c0 {6,D} {18,S} {19,S}
9  O u0 p2 c0 {1,S} {7,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80973,0.0120008,0.000256043,-5.41698e-07,3.50953e-10,-609.766,13.3691], Tmin=(10,'K'), Tmax=(502.957,'K')),
            NASAPolynomial(coeffs=[0.693016,0.07547,-4.86088e-05,1.50307e-08,-1.78173e-12,-785.514,21.3996], Tmin=(502.957,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-5.12366,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (448.981,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C-C': 4, 'C=C': 3, 'C-H': 10}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 11], rotor symmetry: 3, max scan energy: 14.37 kJ/mol
pivots: [4, 7], dihedral: [6, 4, 7, 9], rotor symmetry: 1, max scan energy: 27.02 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.95194400    1.60694400   -0.47184700
C      -1.82505800    0.62059800    0.15672500
C      -2.47977700   -0.23443100   -0.93069500
C       0.98676800    0.27814000   -0.01692200
C      -1.07630500   -0.19885100    1.17546400
C       0.23946900   -0.39510000    1.04734600
C       2.38313600   -0.00672500   -0.32257000
C       0.33635800    1.26666800   -0.67454900
C       3.14245100   -0.97442800    0.20432000
H      -2.58898300    1.23020300    0.64513000
H      -1.72812900   -0.83002100   -1.45365000
H      -2.99920000    0.39956000   -1.65336800
H      -3.20496800   -0.91806700   -0.48003900
H      -1.64576900   -0.63538500    1.98850000
H       0.77940400   -1.00039400    1.76592400
H       2.83147100    0.64923900   -1.06667300
H       0.81766700    1.92026600   -1.39386400
H       2.76628300   -1.67822400    0.93807600
H       4.17667700   -1.09406200   -0.09355400
""",
)

entry(
    index = 140,
    label = "P190",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
2  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {6,S} {7,D}
4  C u0 p0 c0 {1,S} {5,D} {15,S}
5  C u0 p0 c0 {2,S} {4,D} {14,S}
6  C u0 p0 c0 {3,S} {8,D} {16,S}
7  C u0 p0 c0 {3,D} {9,S} {17,S}
8  C u0 p0 c0 {6,D} {18,S} {19,S}
9  O u0 p2 c0 {1,S} {7,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83376,0.0199637,0.00056668,-3.1685e-06,6.19106e-09,13066.1,12.2376], Tmin=(10,'K'), Tmax=(128.504,'K')),
            NASAPolynomial(coeffs=[2.14537,0.0725216,-4.68444e-05,1.45563e-08,-1.73391e-12,13109.5,16.9188], Tmin=(128.504,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (110.117,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (444.824,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C-C': 4, 'C=C': 3, 'C-H': 10}
1D rotors:
pivots: [2, 5], dihedral: [1, 2, 5, 6], rotor symmetry: 1, max scan energy: 17.82 kJ/mol
pivots: [3, 6], dihedral: [11, 3, 6, 5], rotor symmetry: 3, max scan energy: 7.55 kJ/mol
pivots: [4, 7], dihedral: [2, 4, 7, 9], rotor symmetry: 1, max scan energy: 29.20 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.29484700    1.87006700   -3.15532300
C       1.34793500    2.39769000   -1.74653500
C       3.60309500    0.72134400    0.95049700
C       1.41919000    3.79220500   -2.36783400
C       2.52290900    1.87025100   -1.01025000
C       2.43975400    1.24282300    0.16310200
C       1.50438300    5.13414400   -1.86607800
C       1.36060500    3.18270700   -3.56714600
C       1.54223700    5.48440500   -0.57255800
H       0.40201300    2.15662300   -1.25807300
H       3.64951700    1.18914400    1.94012600
H       4.55058600    0.90718300    0.44037600
H       3.50865500   -0.35719700    1.11779000
H       1.45462400    1.08886100    0.60211400
H       3.48885400    2.04130600   -1.47986900
H       1.53860500    5.91460100   -2.62381000
H       1.34499400    3.43802300   -4.61868200
H       1.51661700    4.74478000    0.22001700
H       1.60608000    6.52320000   -0.27406500
""",
)

entry(
    index = 141,
    label = "P191",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
2  C u0 p0 c0 {5,S} {10,S} {14,S} {15,S}
3  C u0 p0 c0 {5,D} {6,S} {8,S}
4  C u0 p0 c0 {1,S} {7,D} {9,S}
5  C u0 p0 c0 {2,S} {3,D} {16,S}
6  C u1 p0 c0 {3,S} {7,S} {18,S}
7  C u0 p0 c0 {4,D} {6,S} {17,S}
8  C u1 p0 c0 {3,S} {9,S} {19,S}
9  O u0 p2 c0 {4,S} {8,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.50133,0.0442954,4.69259e-05,-1.05781e-07,5.26028e-11,11278.4,13.9744], Tmin=(10,'K'), Tmax=(708.515,'K')),
            NASAPolynomial(coeffs=[2.57075,0.067386,-3.97219e-05,1.12813e-08,-1.24024e-12,10962.6,14.9838], Tmin=(708.515,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (93.7221,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (448.981,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C-C': 5, 'C=C': 2, 'C-H': 10}
1D rotors:
pivots: [2, 5], dihedral: [11, 2, 5, 1], rotor symmetry: 3, max scan energy: 7.67 kJ/mol
pivots: [3, 6], dihedral: [10, 3, 6, 4], rotor symmetry: 3, max scan energy: 1.04 kJ/mol
* Invalidated! pivots: [4, 6], dihedral: [7, 4, 6, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
O      -2.02144100   -2.13687000    3.77322400
C      -1.41132100   -1.17744200    5.85966200
C      -2.93496900   -2.12944600   -0.50695800
C      -2.26430600   -0.92530100    1.66679800
C      -1.68258600   -0.95632400    4.41341500
C      -2.55804200   -0.92043000    0.28855500
C      -1.91142200    0.28528600    2.34857600
C      -1.62762600    0.22033300    3.72841900
C      -2.30389000   -2.09994300    2.42213000
H      -3.11476400   -1.87479800   -1.55241800
H      -0.59073700   -1.89052400    5.99745700
H      -1.14616400   -0.24013600    6.34979300
H      -2.28970000   -1.59977900    6.36057400
H      -3.84584900   -2.60585300   -0.12101300
H      -2.14941100   -2.89623600   -0.48349000
H      -2.50390400    0.03448900   -0.22269900
H      -1.35722100    1.11411800    4.27795100
H      -1.86688400    1.22088500    1.80783000
H      -2.55168500   -3.08005300    2.04752100
""",
)

entry(
    index = 142,
    label = "P192",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {7,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {2,S} {7,D} {8,S}
6  C u0 p0 c0 {1,S} {8,D} {18,S}
7  C u0 p0 c0 {4,S} {5,D} {17,S}
8  C u0 p0 c0 {5,S} {6,D} {19,S}
9  O u0 p2 c0 {1,S} {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.60666,0.0348354,8.45295e-05,-1.63109e-07,8.34043e-11,2477.24,12.7624], Tmin=(10,'K'), Tmax=(651.245,'K')),
            NASAPolynomial(coeffs=[0.937274,0.0705419,-4.21914e-05,1.21446e-08,-1.35092e-12,2415.41,21.3518], Tmin=(651.245,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (20.5483,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (448.981,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C-C': 6, 'C=C': 2, 'C-H': 10}
1D rotors:
pivots: [2, 4], dihedral: [1, 2, 4, 11], rotor symmetry: 3, max scan energy: 9.01 kJ/mol
pivots: [5, 8], dihedral: [14, 5, 8, 6], rotor symmetry: 3, max scan energy: 5.23 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       4.09656300    3.17470500   -0.15067500
C       2.95469400    3.60019500   -0.94167700
C       3.30502200    2.16937100   -0.82583800
C       3.25599600    4.49110500   -2.11334500
C       3.04985000   -0.88766100   -0.04938500
C       2.26162800    1.52331700    0.03836300
C       1.72339600    3.78032700   -0.09988500
C       2.13902700    0.22810100    0.36078600
C       1.36363600    2.61150500    0.45422600
H       3.82310500    1.62341300   -1.60663000
H       2.42332400    4.49779000   -2.82246500
H       4.15603600    4.15130200   -2.62831000
H       3.42504200    5.51900500   -1.77772600
H       2.49212800   -1.68171700   -0.55866500
H       3.85137100   -0.55319200   -0.70945000
H       3.51444900   -1.34882400    0.82983200
H       1.29982800   -0.05419000    0.99442700
H       1.23564900    4.73539400    0.04819300
H       0.54713300    2.46615900    1.15158100
""",
)

entry(
    index = 143,
    label = "P193",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {5,D} {7,S}
4  C u0 p0 c0 {2,S} {6,D} {9,S}
5  C u0 p0 c0 {3,D} {6,S} {16,S}
6  C u0 p0 c0 {4,D} {5,S} {15,S}
7  C u0 p0 c0 {3,S} {8,D} {17,S}
8  C u0 p0 c0 {7,D} {18,S} {19,S}
9  O u0 p2 c0 {1,S} {4,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.66571,0.0325532,0.000101629,-1.88054e-07,9.38694e-11,-2481.44,12.7363], Tmin=(10,'K'), Tmax=(680.554,'K')),
            NASAPolynomial(coeffs=[1.75152,0.0710202,-4.31427e-05,1.25254e-08,-1.39942e-12,-2851.16,16.604], Tmin=(680.554,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-20.6663,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (448.981,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C-C': 4, 'C=C': 3, 'C-H': 10}
1D rotors:
pivots: [3, 5], dihedral: [12, 3, 5, 1], rotor symmetry: 3, max scan energy: 7.39 kJ/mol
pivots: [4, 8], dihedral: [2, 4, 8, 9], rotor symmetry: 1, max scan energy: 32.94 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.93243600    1.10373000   -0.62718900
C       0.45790900    0.75236800   -0.79977700
C      -3.18769200    0.43666600   -0.36462400
C       1.01627300   -0.02736100    0.36785700
C      -1.74773800    0.16159800   -0.08429200
C       0.14807800   -0.83313800    1.02173800
C      -1.25690400   -0.83333400    0.68647900
C       2.42547200    0.04015700    0.69953200
C       3.36681200    0.77150300    0.08348600
H       0.96751700    1.70537100   -0.93743000
H       0.55205100    0.17509800   -1.73316100
H      -3.44657200    1.44337800   -0.02098100
H      -3.38688000    0.40334000   -1.44021900
H      -3.82991100   -0.28496100    0.14040200
H      -1.93348200   -1.55188500    1.12809500
H       0.49531800   -1.45760700    1.83899800
H       2.72746000   -0.59117600    1.53303700
H       4.39822600    0.74132800    0.41223400
H       3.14948700    1.42071200   -0.75695700
""",
)

entry(
    index = 144,
    label = "P194",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {4,D} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {5,D} {12,S}
4  C u0 p0 c0 {2,D} {5,S} {14,S}
5  C u0 p0 c0 {3,D} {4,S} {13,S}
6  C u0 p0 c0 {2,S} {8,D} {15,S}
7  C u1 p0 c0 {2,S} {16,S} {17,S}
8  C u0 p0 c0 {6,D} {18,S} {19,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 O u1 p2 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77285,0.030563,0.000850025,-6.60085e-06,1.61867e-08,21375.8,10.6497], Tmin=(10,'K'), Tmax=(137.242,'K')),
            NASAPolynomial(coeffs=[3.90493,0.0695227,-4.36764e-05,1.31965e-08,-1.53364e-12,21331.9,8.80596], Tmin=(137.242,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (183.778,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (448.981,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 10, 'C-O': 1, 'C=C': 3, 'C-C': 4}
1D rotors:
* Invalidated! pivots: [2, 4], dihedral: [10, 2, 4, 1], invalidation reason: 
* Invalidated! pivots: [3, 7], dihedral: [5, 3, 7, 9], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [3, 8], dihedral: [5, 3, 8, 16], rotor symmetry: 2, max scan energy: 11.41 kJ/mol
* Invalidated! pivots: [5, 6], dihedral: [3, 5, 6, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [4, 6], dihedral: [1, 4, 6, 5], rotor symmetry: 1, max scan energy: 42.06 kJ/mol
* Invalidated! pivots: [3, 5], dihedral: [7, 3, 5, 6], invalidation reason: 
* Invalidated! pivots: [7, 9], dihedral: [3, 7, 9, 18], invalidation reason: 


External symmetry: 1, optical isomers: 1

Geometry:
O       1.25194000   -0.02556200    2.06308800
C       3.47358500   -0.28110100    1.20936800
C      -0.33435700   -3.38380200    0.01573200
C       2.01165300   -0.66884100    1.35400900
C       0.25978800   -2.28076000    0.66641900
C       1.56718400   -1.85227800    0.59839600
C       0.40145800   -4.25653300   -0.85840800
C      -1.76817100   -3.63660800    0.25325200
C      -0.11664300   -5.32444700   -1.50539300
H       4.12197500   -1.10204500    1.53242800
H       3.67720900    0.60272400    1.81190900
H       3.71349800   -0.07332500    0.16151400
H       2.30564800   -2.36616600   -0.00725900
H      -0.38324400   -1.68267000    1.30682400
H       1.45400000   -4.03458900   -1.00548100
H      -2.52770500   -3.18106200   -0.37312000
H      -2.09677200   -4.26632600    1.07315000
H      -1.15982100   -5.60060100   -1.40178800
H       0.49830300   -5.93986100   -2.15042900
""",
)

entry(
    index = 145,
    label = "P195",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
2  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {6,S} {7,D}
4  C u0 p0 c0 {2,S} {5,D} {9,S}
5  C u0 p0 c0 {1,S} {4,D} {14,S}
6  C u0 p0 c0 {3,S} {8,D} {15,S}
7  C u0 p0 c0 {3,D} {16,S} {17,S}
8  C u0 p0 c0 {6,D} {18,S} {19,S}
9  O u0 p2 c0 {1,S} {4,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77349,0.024657,0.000393954,-1.70776e-06,2.50643e-09,12007.4,12.9814], Tmin=(10,'K'), Tmax=(171.798,'K')),
            NASAPolynomial(coeffs=[1.58849,0.0755311,-5.02401e-05,1.59573e-08,-1.93102e-12,12082.5,19.674], Tmin=(171.798,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (100.022,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (444.824,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C-C': 4, 'C=C': 3, 'C-H': 10}
1D rotors:
pivots: [2, 4], dihedral: [1, 2, 4, 7], rotor symmetry: 1, max scan energy: 24.16 kJ/mol
pivots: [3, 5], dihedral: [11, 3, 5, 1], rotor symmetry: 3, max scan energy: 5.69 kJ/mol
pivots: [4, 7], dihedral: [2, 4, 7, 9], rotor symmetry: 1, max scan energy: 22.34 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.61546800   -0.26390300   -0.13242400
C      -0.31629400    0.33552200   -0.50923800
C      -2.33069700   -0.06060900    2.25469400
C       0.64995500   -0.64624800   -1.11105800
C      -1.35450000    0.17354700    1.16784400
C      -0.16301600    0.74001500    0.94898100
C       1.97273400   -0.14518500   -1.49601800
C       0.31259000   -1.92762200   -1.30637800
C       2.41576000    1.11055200   -1.37334900
H      -0.51373800    1.16569300   -1.19428600
H      -2.51157800   -1.13198600    2.38496800
H      -3.28936800    0.40949900    2.01450100
H      -1.96097300    0.35179500    3.19446300
H       0.58682900    1.24805600    1.52962000
H       2.63606800   -0.89299300   -1.92430400
H      -0.66738500   -2.29618900   -1.03682700
H       1.01836000   -2.62625800   -1.74238500
H       1.81025700    1.90724300   -0.95623500
H       3.41406800    1.38290600   -1.69414500
""",
)

entry(
    index = 146,
    label = "P196",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {6,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {5,D} {7,S}
5  C u0 p0 c0 {2,S} {4,D} {17,S}
6  C u0 p0 c0 {3,S} {8,S} {16,D}
7  C u0 p0 c0 {4,S} {8,D} {19,S}
8  C u0 p0 c0 {6,S} {7,D} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 O u0 p2 c0 {6,D}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87166,0.0529406,-1.98146e-06,-2.25476e-08,8.68349e-12,1917.74,11.937], Tmin=(10,'K'), Tmax=(1227.18,'K')),
            NASAPolynomial(coeffs=[16.4227,0.0388823,-1.76189e-05,3.77749e-09,-3.11709e-13,-3184.64,-59.4217], Tmin=(1227.18,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (16.0557,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (444.824,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 6, 'C=O': 1, 'C=C': 2, 'C-H': 10}
1D rotors:
pivots: [4, 7], dihedral: [14, 4, 7, 1], rotor symmetry: 3, max scan energy: 3.11 kJ/mol
pivots: [5, 8], dihedral: [2, 5, 8, 9], rotor symmetry: 1, max scan energy: 31.54 kJ/mol
pivots: [7, 9], dihedral: [1, 7, 9, 8], rotor symmetry: 1, max scan energy: 33.56 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O      -2.69186700    1.61811000    0.52799700
C       2.61530800    0.49533500    1.00065100
C       3.18000500   -0.87993100    0.49241600
C      -2.00050700    3.65982100    1.56268500
C       1.25871600   -0.01454500    0.52541500
C       1.75504200   -1.19358800    0.09193100
C      -1.77508100    2.27369100    0.98748100
C      -0.06258300    0.55183600    0.53532000
C      -0.37839200    1.76801300    1.01838200
H       3.00034700    1.37243500    0.47366000
H       2.70655300    0.65899700    2.07776200
H       3.89921200   -0.80865800   -0.32933400
H       3.60614300   -1.52033500    1.27081200
H      -1.39616400    4.39752800    1.02454000
H      -3.05436200    3.92276800    1.48660900
H      -1.68679700    3.69179800    2.61130600
H       1.29927200   -2.05911000   -0.37649200
H       0.38748800    2.41017100    1.44425800
H      -0.87110000   -0.04683400    0.12097700
""",
)

entry(
    index = 147,
    label = "P197",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {5,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {6,D} {7,S}
5  C u0 p0 c0 {1,S} {3,S} {15,D}
6  C u0 p0 c0 {1,S} {4,D} {16,S}
7  C u0 p0 c0 {4,S} {8,D} {17,S}
8  C u0 p0 c0 {7,D} {18,S} {19,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 O u0 p2 c0 {5,D}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63875,0.0472894,2.61119e-05,-6.19691e-08,2.56952e-11,2779.64,13.493], Tmin=(10,'K'), Tmax=(935.254,'K')),
            NASAPolynomial(coeffs=[6.88377,0.0586376,-3.25486e-05,8.68563e-09,-9.00568e-13,1069.37,-7.84343], Tmin=(935.254,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (23.1583,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (448.981,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 6, 'C=O': 1, 'C=C': 2, 'C-H': 10}
1D rotors:
* Invalidated! pivots: [2, 6], dihedral: [3, 2, 6, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [4, 6], dihedral: [13, 4, 6, 1], rotor symmetry: 3, max scan energy: 2.19 kJ/mol
pivots: [5, 8], dihedral: [3, 5, 8, 9], rotor symmetry: 1, max scan energy: 27.08 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.77915300    0.97940100    0.91136400
C      -1.89299600   -1.21708200    1.30300400
C      -1.44230800   -0.82384200    2.74838900
C      -3.01572600   -0.53881700   -0.91672400
C      -0.01769200   -1.05395400    2.25617300
C      -2.58855700   -0.13574300    0.48295000
C      -0.40277200   -1.38951000    1.01017400
C       1.26549900   -0.96040200    2.91611600
C       1.42513200   -0.61373300    4.19826000
H      -2.46876700   -2.14886600    1.24017000
H      -1.69282900    0.20374600    3.01343200
H      -1.78564700   -1.50686800    3.53036000
H      -3.82816400   -1.27071500   -0.85593300
H      -3.36078300    0.33750800   -1.46390900
H      -2.19332400   -1.01764100   -1.45628700
H       0.13181700   -1.68105800    0.11288700
H       2.13770200   -1.19187600    2.30845500
H       0.57595200   -0.37418600    4.82955000
H       2.40658300   -0.55588200    4.65309700
""",
)

entry(
    index = 148,
    label = "P198",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {12,S}
3  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {3,S} {6,D}
5  C u0 p0 c0 {2,S} {7,D} {8,S}
6  C u0 p0 c0 {4,D} {7,S} {16,S}
7  C u0 p0 c0 {5,D} {6,S} {17,S}
8  C u0 p0 c0 {5,S} {18,D} {19,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 O u0 p2 c0 {8,D}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.64149,0.0300882,0.000105168,-1.90674e-07,9.62788e-11,-11238.4,12.7415], Tmin=(10,'K'), Tmax=(642.73,'K')),
            NASAPolynomial(coeffs=[-0.469436,0.0752353,-4.58522e-05,1.33271e-08,-1.49054e-12,-11114.1,27.6137], Tmin=(642.73,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-93.4921,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (448.981,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 6, 'C=O': 1, 'C=C': 2, 'C-H': 10}
1D rotors:
pivots: [4, 5], dihedral: [14, 4, 5, 2], rotor symmetry: 3, max scan energy: 8.62 kJ/mol
pivots: [6, 9], dihedral: [3, 6, 9, 1], rotor symmetry: 1, max scan energy: 53.61 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       3.61371600    1.44425900   -0.61136300
C      -0.72320300    1.29253000   -0.62501700
C       0.73682100    1.14219300   -1.07308800
C      -2.76984600   -0.17477300   -0.07037200
C      -1.28658300    0.02699100   -0.01121000
C       1.55695400    0.39795000   -0.04951600
C      -0.45537500   -0.81725300    0.63285900
C       0.96707200   -0.54228800    0.72185600
C       2.99663500    0.63790300    0.05536200
H       1.19063800    2.11385600   -1.27651800
H      -1.34357200    1.61201600   -1.46770700
H      -0.80679800    2.09071400    0.12879900
H       0.77899600    0.58258600   -2.01832000
H      -3.11044600   -0.26072800   -1.10871500
H      -3.08321900   -1.06959900    0.47039800
H      -3.29460900    0.68882400    0.35642800
H      -0.84936400   -1.69518300    1.13465600
H       1.56722000   -1.11612700    1.42349000
H       3.51419700    0.01095800    0.81470000
""",
)

entry(
    index = 149,
    label = "P199",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {5,D} {7,S}
5  C u0 p0 c0 {2,S} {4,D} {15,S}
6  C u0 p0 c0 {1,S} {7,D} {16,S}
7  C u0 p0 c0 {4,S} {6,D} {17,S}
8  C u0 p0 c0 {1,S} {18,D} {19,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 O u0 p2 c0 {8,D}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.45058,0.0487412,1.27618e-05,-4.30176e-08,1.80309e-11,-7400.85,13.0179], Tmin=(10,'K'), Tmax=(931.46,'K')),
            NASAPolynomial(coeffs=[4.2206,0.0615896,-3.39449e-05,9.03155e-09,-9.36449e-13,-8245.12,5.59572], Tmin=(931.46,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-61.5681,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (448.981,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 6, 'C=O': 1, 'C=C': 2, 'C-H': 10}
1D rotors:
pivots: [2, 9], dihedral: [3, 2, 9, 1], rotor symmetry: 1, max scan energy: 18.94 kJ/mol
pivots: [4, 5], dihedral: [13, 4, 5, 6], rotor symmetry: 3, max scan energy: 7.52 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.41486100    0.58189200    1.73994400
C      -1.48143700   -0.77151500   -0.04822200
C      -0.40384900   -1.26229800    0.93137100
C       2.43538100    1.17871600   -0.18117600
C       1.18818500    0.33586400   -0.13997700
C       0.83013900   -0.39598300    0.92529300
C      -0.89313500   -0.22043300   -1.33129300
C       0.33735300    0.30616900   -1.34097000
C      -2.39341700    0.29028200    0.57290800
H      -2.15684800   -1.60192100   -0.29901500
H      -0.11782700   -2.29292000    0.67935500
H      -0.83351900   -1.29083300    1.93582700
H       3.09664200    0.86333900   -0.99633500
H       2.19470200    2.23304800   -0.35673900
H       2.99353500    1.11025600    0.75425600
H       1.45642500   -0.40871100    1.81231900
H      -1.50705600   -0.21774400   -2.22597300
H       0.73634800    0.73049600   -2.25805100
H      -3.06867900    0.79506900   -0.15309100
""",
)

entry(
    index = 150,
    label = "P200",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {6,S} {8,D}
5  C u0 p0 c0 {1,S} {6,D} {14,S}
6  C u0 p0 c0 {4,S} {5,D} {15,S}
7  C u0 p0 c0 {1,S} {16,D} {17,S}
8  C u0 p0 c0 {4,D} {18,S} {19,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 O u0 p2 c0 {7,D}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.66309,0.0283111,0.000143985,-3.3184e-07,2.34382e-10,-7373.91,12.9794], Tmin=(10,'K'), Tmax=(365.803,'K')),
            NASAPolynomial(coeffs=[-0.560574,0.0744963,-4.54016e-05,1.33138e-08,-1.50661e-12,-7064.9,29.1085], Tmin=(365.803,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-61.3373,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (453.139,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 6, 'C=O': 1, 'C=C': 2, 'C-H': 10}
1D rotors:
pivots: [2, 8], dihedral: [3, 2, 8, 1], rotor symmetry: 1, max scan energy: 11.14 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.38056000   -0.49859000    1.79421800
C      -1.46999800    0.21777200   -0.33869800
C      -0.74575800   -1.12931000   -0.46021700
C       0.56323500   -1.14146600    0.34493900
C       1.47202200    0.00711600   -0.03662000
C      -0.52499400    1.39326200   -0.46793200
C       0.80465700    1.27226100   -0.34564600
C      -2.27057300    0.35683600    0.95439000
C       2.80712100   -0.09925900   -0.06801100
H      -2.22230800    0.30789300   -1.13824800
H      -0.52623500   -1.31331900   -1.51647100
H      -1.40211500   -1.92893700   -0.11127600
H       0.31617900   -1.05830300    1.40938300
H       1.08291000   -2.09378900    0.21417200
H      -0.96076900    2.36504100   -0.68059900
H       1.43524600    2.14520900   -0.48939200
H      -2.77097500    1.34271500    1.08017800
H       3.30837500   -1.03535400    0.15139300
H       3.43645000    0.75066800   -0.30984300
""",
)

entry(
    index = 151,
    label = "P201",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,D} {11,S}
3  C u0 p0 c0 {1,S} {7,D} {12,S}
4  C u0 p0 c0 {2,D} {5,S} {14,S}
5  C u1 p0 c0 {4,S} {6,S} {15,S}
6  C u0 p0 c0 {5,S} {8,D} {13,S}
7  C u0 p0 c0 {3,D} {18,S} {19,S}
8  C u0 p0 c0 {6,D} {16,S} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 O u1 p2 c0 {6,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.11774,0.0850615,-0.000136581,2.11488e-07,-1.46424e-10,23383.7,14.8399], Tmin=(10,'K'), Tmax=(438.424,'K')),
            NASAPolynomial(coeffs=[3.81396,0.068079,-4.21075e-05,1.25277e-08,-1.43604e-12,23424.8,13.2202], Tmin=(438.424,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (194.396,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (444.824,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 10, 'C-O': 1, 'C=C': 3, 'C-C': 4}
1D rotors:
pivots: [2, 3], dihedral: [4, 2, 3, 5], rotor symmetry: 1, max scan energy: 9.92 kJ/mol
pivots: [2, 4], dihedral: [3, 2, 4, 8], rotor symmetry: 1, max scan energy: 11.98 kJ/mol
* Invalidated! pivots: [5, 6], dihedral: [3, 5, 6, 7], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [6, 7], dihedral: [5, 6, 7, 1], rotor symmetry: 1, max scan energy: 43.60 kJ/mol
* Invalidated! pivots: [7, 9], dihedral: [1, 7, 9, 16], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
* Invalidated! pivots: [3, 5], dihedral: [2, 3, 5, 6], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers


External symmetry: 1, optical isomers: 2

Geometry:
O      -3.31347500    0.53201500   -1.73805700
C       1.44976600    0.34159400    0.37196000
C       0.82780700    0.68678300   -0.95018900
C       2.40441200   -0.82553700    0.26365900
C      -0.51849800    0.63633700   -1.21611200
C      -1.09775200    0.94826500   -2.44754200
C      -2.54011100    0.87918100   -2.66412100
C       3.71131100   -0.76434800    0.49900700
C      -3.09285800    1.21018900   -3.94947400
H       1.99719300    1.20976400    0.76138200
H       0.65943700    0.10772900    1.09432900
H       1.51287200    0.97873400   -1.74368900
H       1.95839200   -1.76826600   -0.04644700
H      -1.20352200    0.33799600   -0.42591100
H      -0.46457000    1.25263700   -3.27602100
H      -4.16546600    1.14812700   -4.07534100
H      -2.47490100    1.51609900   -4.78531200
H       4.34795600   -1.63618100    0.39934600
H       4.19207000    0.15982400    0.80618400
""",
)

entry(
    index = 152,
    label = "P202",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
2  C u0 p0 c0 {5,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {7,D} {9,S}
4  C u0 p0 c0 {1,S} {5,D} {15,S}
5  C u0 p0 c0 {2,S} {4,D} {13,S}
6  C u0 p0 c0 {2,S} {8,D} {14,S}
7  C u0 p0 c0 {3,D} {18,S} {19,S}
8  C u0 p0 c0 {6,D} {16,S} {17,S}
9  O u0 p2 c0 {1,S} {3,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.1593,0.0789729,-0.000103319,1.34142e-07,-8.44105e-11,18077.1,14.198], Tmin=(10,'K'), Tmax=(464.181,'K')),
            NASAPolynomial(coeffs=[3.81451,0.066432,-4.05121e-05,1.19386e-08,-1.35921e-12,18090.5,12.34], Tmin=(464.181,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (150.267,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (444.824,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C-C': 4, 'C=C': 3, 'C-H': 10}
1D rotors:
pivots: [2, 5], dihedral: [1, 2, 5, 6], rotor symmetry: 1, max scan energy: 17.96 kJ/mol
pivots: [3, 6], dihedral: [7, 3, 6, 5], rotor symmetry: 1, max scan energy: 11.51 kJ/mol
pivots: [3, 7], dihedral: [6, 3, 7, 9], rotor symmetry: 1, max scan energy: 11.86 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       2.74022900   -1.26208900    1.11342300
C       1.97947600   -0.20300200    0.34446300
C      -1.01802000   -0.65527400   -2.08530700
C       3.41118900   -0.38421200    0.34024200
C       1.11265000   -0.69578400   -0.73681500
C      -0.11078200   -0.21567600   -0.96628400
C      -1.31543600    0.46661400   -3.05113200
C       4.64526400   -0.10376100   -0.03372900
C      -2.52167600    0.97637300   -3.27892600
H       1.55869700    0.55326900    1.00184400
H      -1.96108600   -1.02550400   -1.66625600
H      -0.55113300   -1.49012800   -2.62048500
H      -0.50110100    0.57145300   -0.32280300
H      -0.45332500    0.87463100   -3.57514900
H       1.53025500   -1.47837300   -1.36510300
H      -3.40473700    0.59816700   -2.77224400
H      -2.67259000    1.78640000   -3.98347300
H       5.48256500   -0.68175100    0.33543400
H       4.83068300    0.71544700   -0.71393900
""",
)

entry(
    index = 153,
    label = "P203",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {5,S} {10,S} {11,S}
2  C u0 p0 c0 {3,S} {9,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {6,D} {9,S}
4  C u0 p0 c0 {1,S} {7,D} {14,S}
5  C u0 p0 c0 {1,S} {8,D} {15,S}
6  C u0 p0 c0 {3,D} {7,S} {17,S}
7  C u0 p0 c0 {4,D} {6,S} {16,S}
8  C u0 p0 c0 {5,D} {18,S} {19,S}
9  O u0 p2 c0 {2,S} {3,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.62463,0.0602641,-1.95624e-05,-7.77267e-09,4.51767e-12,18514.8,13.2069], Tmin=(10,'K'), Tmax=(1246.06,'K')),
            NASAPolynomial(coeffs=[15.7054,0.0406443,-1.90104e-05,4.27289e-09,-3.75066e-13,14016.6,-53.7026], Tmin=(1246.06,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (153.984,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (448.981,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C-C': 4, 'C=C': 3, 'C-H': 10}
1D rotors:
pivots: [2, 5], dihedral: [6, 2, 5, 8], rotor symmetry: 1, max scan energy: 12.55 kJ/mol
* Invalidated! pivots: [2, 6], dihedral: [5, 2, 6, 9], invalidation reason: Another conformer for C8H10O[216] exists which is 2.39 kJ/mol lower.Another conformer for C8H10O[216] exists which is 2.39 kJ/mol lower.
pivots: [7, 8], dihedral: [4, 7, 8, 5], rotor symmetry: 1, max scan energy: 29.52 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -4.62064700   -0.03717600    0.31277800
C       1.63532300   -0.14709600   -0.46334400
C      -4.19554600    0.81983600   -0.82499600
C      -3.30747900    0.05440000    0.00534100
C       0.32486800   -0.51826700    0.18049800
C       2.56205200    0.56734000    0.49065400
C      -2.13644000   -0.41413100    0.42177200
C      -0.87471400   -0.06209700   -0.20493500
C       3.75352100    0.12164200    0.87712200
H       2.13805400   -1.04765300   -0.83749500
H       1.43936500    0.49368800   -1.33185000
H      -4.33118600    1.88311900   -0.65181600
H      -4.49909300    0.44507500   -1.79781000
H       0.38755800   -1.19711900    1.02922500
H       2.18842300    1.50927700    0.88810100
H      -0.92848900    0.62109300   -1.05132300
H      -2.13249500   -1.09105300    1.27064200
H       4.15652100   -0.81707000    0.50797000
H       4.37141600    0.67780600    1.57319000
""",
)

entry(
    index = 154,
    label = "P204",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {7,D} {9,S}
4  C u0 p0 c0 {1,S} {6,D} {14,S}
5  C u0 p0 c0 {2,S} {8,D} {13,S}
6  C u0 p0 c0 {4,D} {9,S} {15,S}
7  C u0 p0 c0 {3,D} {18,S} {19,S}
8  C u0 p0 c0 {5,D} {16,S} {17,S}
9  O u0 p2 c0 {3,S} {6,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.48057,0.0476765,3.60118e-05,-8.95824e-08,4.36521e-11,3246.87,13.413], Tmin=(10,'K'), Tmax=(751.74,'K')),
            NASAPolynomial(coeffs=[3.76684,0.0655827,-3.84864e-05,1.08663e-08,-1.18727e-12,2654.84,8.46212], Tmin=(751.74,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (26.9521,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (448.981,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C-C': 4, 'C=C': 3, 'C-H': 10}
1D rotors:
pivots: [2, 3], dihedral: [4, 2, 3, 6], rotor symmetry: 1, max scan energy: 22.48 kJ/mol
pivots: [3, 6], dihedral: [2, 3, 6, 9], rotor symmetry: 1, max scan energy: 16.08 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.24004800    0.09144100   -1.38181300
C      -0.51509500   -0.35617800    0.19304300
C       0.70544500    0.55557000    0.49152600
C      -1.78939000    0.42603400   -0.10944300
C      -0.37917000   -1.17884900   -1.06903800
C       1.93609300   -0.22154800    0.86215700
C      -1.37291000   -0.85532900   -1.88832800
C      -2.44700500    1.30674200    0.63736000
C       3.08457300   -0.20667600    0.19187000
H      -0.67616600   -1.00003000    1.06722400
H       0.90103600    1.18875600   -0.37843000
H       0.43125200    1.22090600    1.31916300
H       1.85411200   -0.84247800    1.75391900
H       0.40885200   -1.88750600   -1.26742900
H      -1.62479600   -1.20122900   -2.87923600
H       3.94008500   -0.78908400    0.51526300
H       3.21240100    0.39565400   -0.70254500
H      -2.09481800    1.55534500    1.62890100
H      -3.34438600    1.78711300    0.27134000
""",
)

entry(
    index = 155,
    label = "P205",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {6,S} {10,S} {11,S}
2  C u0 p0 c0 {5,S} {9,S} {12,S} {13,S}
3  C u0 p0 c0 {4,D} {7,S} {9,S}
4  C u0 p0 c0 {1,S} {3,D} {14,S}
5  C u0 p0 c0 {2,S} {7,D} {16,S}
6  C u0 p0 c0 {1,S} {8,D} {15,S}
7  C u0 p0 c0 {3,S} {5,D} {17,S}
8  C u0 p0 c0 {6,D} {18,S} {19,S}
9  O u0 p2 c0 {2,S} {3,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73209,0.0447863,2.36313e-05,-5.08791e-08,1.92668e-11,2268.03,13.117], Tmin=(10,'K'), Tmax=(1030.13,'K')),
            NASAPolynomial(coeffs=[7.63512,0.0552739,-2.89791e-05,7.33323e-09,-7.24981e-13,103.31,-12.4327], Tmin=(1030.13,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (18.9326,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (453.139,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C-C': 4, 'C=C': 3, 'C-H': 10}
1D rotors:
* Invalidated! pivots: [2, 5], dihedral: [7, 2, 5, 4], invalidation reason: Another conformer for C8H10O[224] exists which is 2.28 kJ/mol lower.Another conformer for C8H10O[224] exists which is 2.28 kJ/mol lower.
pivots: [2, 7], dihedral: [5, 2, 7, 9], rotor symmetry: 1, max scan energy: 13.04 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       0.67973000    1.59836500   -2.51331400
C       2.57980700    1.12935900   -0.30276900
C      -0.44104700    1.88075900   -3.36789600
C       0.29169700    1.71960400   -1.19406600
C       1.13174700    1.51929700   -0.16833800
C      -1.56699400    2.18944300   -2.42510700
C       2.87216200   -0.21221200    0.32362800
C      -1.11903300    2.08938500   -1.17079000
C       3.70739400   -0.41860100    1.33758800
H       2.83983700    1.10204600   -1.36539100
H       3.21938200    1.88771500    0.16587000
H      -0.63602100    1.00562400   -4.00088000
H      -0.18556800    2.72192000   -4.02495400
H       0.72768100    1.63124800    0.83172700
H       2.32873300   -1.05420400   -0.10130900
H      -2.56601500    2.44694200   -2.74829700
H      -1.67784800    2.24871600   -0.25981600
H       4.26211400    0.39753400    1.79179000
H       3.87172100   -1.40849200    1.74864600
""",
)

entry(
    index = 156,
    label = "P206",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,D} {9,S}
4  C u0 p0 c0 {2,S} {7,D} {13,S}
5  C u0 p0 c0 {3,D} {6,S} {15,S}
6  C u0 p0 c0 {5,S} {8,D} {14,S}
7  C u0 p0 c0 {4,D} {18,S} {19,S}
8  C u0 p0 c0 {6,D} {16,S} {17,S}
9  O u0 p2 c0 {1,S} {3,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.41838,0.060863,-1.51872e-05,-1.7992e-08,9.63627e-12,16900.8,13.6638], Tmin=(10,'K'), Tmax=(1011.26,'K')),
            NASAPolynomial(coeffs=[9.67757,0.053052,-2.87384e-05,7.51301e-09,-7.65677e-13,14768.3,-20.8877], Tmin=(1011.26,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (140.518,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (444.824,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C-C': 4, 'C=C': 3, 'C-H': 10}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 5], rotor symmetry: 1, max scan energy: 13.11 kJ/mol
pivots: [3, 5], dihedral: [2, 3, 5, 8], rotor symmetry: 1, max scan energy: 10.58 kJ/mol
pivots: [6, 7], dihedral: [4, 6, 7, 9], rotor symmetry: 1, max scan energy: 30.99 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.15533600   -2.53112600   -0.27023600
C       0.65177200   -1.30233900   -0.54439300
C       1.78927500   -1.02899200    0.41587800
C      -0.72902300   -1.31402400   -0.14285400
C       2.18436000    0.42475700    0.40355000
C      -1.90315900   -0.78671100    0.19098300
C      -2.15170900    0.64396800    0.20333900
C       3.35423800    0.88905800   -0.02380200
C      -3.31204100    1.21699200    0.54322100
H       0.88017200   -1.18737800   -1.60154200
H       1.46505700   -1.32599200    1.41849700
H       2.64502700   -1.65458200    0.14282200
H       1.43496200    1.12222500    0.77216400
H      -1.31928900    1.27813700   -0.09449200
H      -2.70853200   -1.46316600    0.46129100
H      -3.43606900    2.29264200    0.52908700
H      -4.17137000    0.62641500    0.84400200
H       4.12905300    0.22535900   -0.39587500
H       3.58413300    1.94830100   -0.00948700
""",
)

entry(
    index = 157,
    label = "P207",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
2  C u0 p0 c0 {4,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {4,D} {9,S}
4  C u0 p0 c0 {2,S} {3,D} {13,S}
5  C u0 p0 c0 {1,S} {7,D} {15,S}
6  C u0 p0 c0 {2,S} {8,D} {14,S}
7  C u0 p0 c0 {5,D} {16,S} {17,S}
8  C u0 p0 c0 {6,D} {18,S} {19,S}
9  O u0 p2 c0 {1,S} {3,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.11112,0.0716934,-5.0584e-05,1.89353e-08,-2.97854e-12,18598.9,14.1846], Tmin=(10,'K'), Tmax=(1327.37,'K')),
            NASAPolynomial(coeffs=[10.2928,0.0500518,-2.6128e-05,6.65243e-09,-6.65174e-13,16692.3,-22.4965], Tmin=(1327.37,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (154.529,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (444.824,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C-C': 4, 'C=C': 3, 'C-H': 10}
1D rotors:
pivots: [2, 6], dihedral: [1, 2, 6, 8], rotor symmetry: 1, max scan energy: 18.59 kJ/mol
pivots: [3, 5], dihedral: [7, 3, 5, 4], rotor symmetry: 1, max scan energy: 9.16 kJ/mol
pivots: [3, 7], dihedral: [5, 3, 7, 9], rotor symmetry: 1, max scan energy: 12.58 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.30766900    1.22778500   -1.38377600
C      -0.60998600    0.91968100   -2.68517100
C      -0.15260600   -0.78752700    0.83246000
C      -0.37536200    0.24554300   -1.43200900
C       0.18862200   -0.64195600   -0.63213700
C      -1.46004100    0.34824600   -3.74345200
C      -0.71874700   -2.14719100    1.15765000
C      -1.34333000    0.67688300   -5.02806200
C      -0.16705100   -3.02444600    1.99047500
H       0.07266600    1.71153700   -2.98294900
H       0.74086100   -0.61454600    1.44368300
H      -0.87901700   -0.01328900    1.10311500
H       0.92876500   -1.30885600   -1.05993100
H      -1.64312300   -2.40475800    0.64396200
H      -2.19024700   -0.38667600   -3.41759900
H      -1.96418400    0.21953700   -5.78884100
H      -0.61693700    1.41015300   -5.36416100
H      -0.61941600   -3.99112100    2.18147100
H       0.75772400   -2.80505800    2.51637300
""",
)

entry(
    index = 158,
    label = "P208",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {10,S}
3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {2,S} {13,D}
5  C u0 p0 c0 {2,S} {8,D} {15,S}
6  C u0 p0 c0 {3,S} {7,D} {14,S}
7  C u0 p0 c0 {6,D} {18,S} {19,S}
8  C u0 p0 c0 {5,D} {16,S} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61007,0.0631071,-3.31229e-05,7.04939e-09,-2.88233e-13,14566.1,13.6764], Tmin=(10,'K'), Tmax=(1642.24,'K')),
            NASAPolynomial(coeffs=[26.9422,0.0187695,-4.03599e-06,-1.2636e-10,9.89889e-14,5218.17,-115.591], Tmin=(1642.24,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (121.05,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (448.981,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 6, 'C=O': 1, 'C=C': 2, 'C-H': 10}
1D rotors:
* Invalidated! pivots: [2, 4], dihedral: [3, 2, 4, 7], invalidation reason: Another conformer for C8H10O[228] exists which is 1.02 kJ/mol lower.Another conformer for C8H10O[228] exists which is 1.02 kJ/mol lower.
pivots: [3, 6], dihedral: [2, 3, 6, 9], rotor symmetry: 1, max scan energy: 12.65 kJ/mol
pivots: [4, 7], dihedral: [2, 4, 7, 8], rotor symmetry: 1, max scan energy: 11.15 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       2.86789800    1.52372800   -1.68136600
C       0.71443800    0.30889400   -1.02239100
C       1.71198900    0.22567400    0.21443300
C      -0.55640200    1.14611400   -0.92920300
C       2.05016700    0.90668700   -1.06573800
C       2.32138500   -1.06208500    0.60541900
C      -1.67523400    0.41554700   -0.23751600
C      -2.86010100    0.15380900   -0.78018700
C       2.60444900   -1.42190300    1.85619300
H       0.60306200   -0.63263500   -1.55847000
H       1.46200400    0.89535200    1.03605100
H      -0.86617800    1.44230500   -1.93643400
H      -0.32686500    2.07330200   -0.38866500
H      -1.46701600    0.08017900    0.77680500
H       2.55518900   -1.74387300   -0.20994800
H       2.39549200   -0.77182300    2.69965400
H       3.06108900   -2.37935000    2.07629100
H      -3.10598100    0.46849300   -1.79017200
H      -3.62953400   -0.38083300   -0.23491600
""",
)

entry(
    index = 159,
    label = "P209",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {9,S} {12,S} {13,S}
3  C u0 p0 c0 {4,D} {5,S} {9,S}
4  C u0 p0 c0 {1,S} {3,D} {14,S}
5  C u0 p0 c0 {3,S} {6,D} {16,S}
6  C u0 p0 c0 {5,D} {7,S} {15,S}
7  C u0 p0 c0 {6,S} {8,D} {17,S}
8  C u0 p0 c0 {7,D} {18,S} {19,S}
9  O u0 p2 c0 {2,S} {3,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85492,0.00957377,0.00026232,-5.60203e-07,3.77164e-10,593.607,14.504], Tmin=(10,'K'), Tmax=(458.901,'K')),
            NASAPolynomial(coeffs=[-1.39191,0.0805028,-5.18791e-05,1.58901e-08,-1.85828e-12,809.869,32.8395], Tmin=(458.901,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (4.91079,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (453.139,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C-C': 4, 'C=C': 3, 'C-H': 10}
1D rotors:
* Invalidated! pivots: [4, 6], dihedral: [1, 4, 6, 7], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [7, 8], dihedral: [6, 7, 8, 9], rotor symmetry: 1, max scan energy: 33.90 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.18061200   -0.79739700   -0.09002800
C       2.89856000    0.68327500    0.69275700
C       2.50725600   -0.79819500    0.49551500
C       0.66176000    0.46424600    0.08490600
C       1.55533300    1.35394100    0.55077600
C      -0.72650900    0.66161200   -0.26068800
C      -1.54170600   -0.30923800   -0.71822400
C      -2.93150500   -0.09938300   -1.06725200
C      -3.74913300   -1.05724400   -1.52367900
H       3.60605900    1.03114500   -0.07139100
H       3.37076300    0.84965200    1.66541500
H       2.44898300   -1.32797200    1.45163500
H       3.16555600   -1.34831800   -0.17674300
H       1.35644800    2.39909200    0.73267600
H      -1.14065300   -1.31166200   -0.83604800
H      -1.10100000    1.67316100   -0.13377000
H      -3.31694300    0.91094100   -0.94282500
H      -3.40334600   -2.07664400   -1.66208500
H      -4.78339200   -0.85164800   -1.77147400
""",
)

entry(
    index = 160,
    label = "P210",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {3,S} {9,S} {12,S}
5  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
6  C u0 p0 c0 {1,S} {7,D} {16,S}
7  C u0 p0 c0 {2,S} {6,D} {17,S}
8  C u0 p0 c0 {2,S} {18,D} {19,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 O u0 p2 c0 {8,D}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79704,0.0183939,0.000253174,-6.77894e-07,5.93314e-10,8385.53,12.5556], Tmin=(10,'K'), Tmax=(291.19,'K')),
            NASAPolynomial(coeffs=[-0.481879,0.0771714,-4.96012e-05,1.52866e-08,-1.80497e-12,8634.73,27.9197], Tmin=(291.19,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (69.7532,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (448.981,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 8, 'C=O': 1, 'C=C': 1, 'C-H': 10}
1D rotors:
pivots: [2, 6], dihedral: [3, 2, 6, 14], rotor symmetry: 3, max scan energy: 13.19 kJ/mol
pivots: [3, 9], dihedral: [2, 3, 9, 1], rotor symmetry: 1, max scan energy: 16.68 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.49091300   -1.24964800    2.19229800
C      -0.64893700    0.19629900   -0.24153000
C       0.79503400   -0.49467600    0.02731700
C       0.05230100    1.59186100   -0.10292800
C       1.41932400    0.91958600    0.18907600
C      -1.88983800   -0.06058100    0.58602900
C      -0.52437100   -0.40269600   -1.62692300
C       0.66199900   -0.97966500   -1.40372200
C       0.94476000   -1.47840100    1.13798000
H       1.76685400    1.07571900    1.21038900
H      -0.00073300    2.21497400   -0.99740700
H      -0.33119400    2.16549900    0.74350800
H       2.23206400    1.14407200   -0.50267400
H      -1.73302800    0.21267800    1.63335300
H      -2.19478500   -1.10959900    0.54497200
H      -2.72197700    0.54331400    0.20641900
H      -1.15145400   -0.30429300   -2.50776400
H       1.35997000   -1.51672100   -2.03700600
H       0.47309700   -2.46772200    0.94861100
""",
)

entry(
    index = 161,
    label = "P211",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {7,S} {8,D}
6  C u0 p0 c0 {1,S} {7,D} {17,S}
7  C u0 p0 c0 {5,S} {6,D} {18,S}
8  C u0 p0 c0 {5,D} {19,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 O u0 p2 c0 {8,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67476,0.0299889,0.000100073,-1.78628e-07,8.80135e-11,-7202.55,13.152], Tmin=(10,'K'), Tmax=(670.503,'K')),
            NASAPolynomial(coeffs=[0.318147,0.0719482,-4.28659e-05,1.22831e-08,-1.36039e-12,-7245.49,24.3271], Tmin=(670.503,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-59.9223,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (453.139,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 6, 'C=O': 1, 'C=C': 2, 'C-H': 10}
1D rotors:
pivots: [2, 5], dihedral: [3, 2, 5, 15], rotor symmetry: 3, max scan energy: 13.77 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       4.24070100    0.25688400    0.65243100
C      -1.08463500    0.07119800   -0.38737200
C      -0.26947100   -1.14605300    0.08541200
C       1.18441000   -1.09751600   -0.40501400
C      -2.47111200    0.10562900    0.27298100
C       1.83302100    0.20768700    0.04876900
C      -0.32470700    1.35410200   -0.13567500
C       0.99595100    1.40578900    0.08918000
C       3.10955000    0.24230400    0.37302800
H      -1.24303500   -0.02735300   -1.47233900
H      -0.74301000   -2.06905000   -0.26414800
H      -0.27660500   -1.17438400    1.18089100
H       1.74122700   -1.96163400   -0.03505300
H       1.20227500   -1.14721600   -1.50058400
H      -2.38243300    0.21126900    1.35858400
H      -3.06283100    0.94739700   -0.09807600
H      -3.02880300   -0.81231400    0.06543600
H      -0.89638600    2.27752300   -0.12543000
H       1.47586900    2.35628800    0.29690400
""",
)

entry(
    index = 162,
    label = "P212",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {11,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {12,S}
3  C u0 p0 c0 {1,S} {10,S} {13,S} {14,S}
4  C u0 p0 c0 {7,S} {9,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {8,D} {17,S}
6  C u0 p0 c0 {2,S} {7,D} {19,S}
7  C u0 p0 c0 {4,S} {6,D} {18,S}
8  C u0 p0 c0 {5,D} {10,S} {20,S}
9  O u0 p2 c0 {2,S} {4,S}
10 O u0 p2 c0 {3,S} {8,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89646,0.00647867,0.000252847,-4.8285e-07,2.93983e-10,-19100,15.275], Tmin=(10,'K'), Tmax=(483.794,'K')),
            NASAPolynomial(coeffs=[-4.14001,0.0898392,-5.80568e-05,1.78448e-08,-2.09538e-12,-18520.4,46.1652], Tmin=(483.794,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-158.835,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (482.239,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 4, 'C-C': 5, 'C=C': 2, 'C-H': 10}
1D rotors:
* Invalidated! pivots: [3, 4], dihedral: [5, 3, 4, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       0.88291000   -1.41160300   -0.32780100
O      -3.05647600    0.18454900   -0.11689300
C      -0.71559600    0.23992900    0.45132900
C       0.33240800   -0.11651300   -0.62572100
C      -1.98313900   -0.64311800    0.41861300
C       0.94524100   -2.20624300   -1.51672300
C      -1.32133800    1.61560600    0.25665000
C      -0.17132000   -0.24319500   -2.03955600
C       0.17380100   -1.42305400   -2.54165000
C      -2.60135900    1.46865500   -0.08276000
H      -0.20617400    0.13883600    1.41428700
H       1.13274000    0.63972600   -0.57051700
H      -2.28244700   -0.95626400    1.42200400
H      -1.88594600   -1.52044500   -0.21959700
H       1.99266900   -2.35868100   -1.81973400
H       0.51421400   -3.19401900   -1.31154200
H      -0.78847600    2.55155400    0.32896000
H      -0.03295200   -1.78790000   -3.53965300
H      -0.71457800    0.54394600   -2.54380600
H      -3.33975400    2.21406300   -0.34472700
""",
)

entry(
    index = 163,
    label = "P213",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,D} {6,S}
4  C u0 p0 c0 {2,S} {7,D} {8,S}
5  C u0 p0 c0 {3,D} {15,S} {16,S}
6  C u0 p0 c0 {3,S} {13,D} {17,S}
7  C u0 p0 c0 {4,D} {18,S} {19,S}
8  C u0 p0 c0 {4,S} {14,D} {20,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 O u0 p2 c0 {6,D}
14 O u0 p2 c0 {8,D}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74649,0.0736516,-4.25612e-05,9.9552e-09,-5.00118e-13,-24417.6,13.4413], Tmin=(10,'K'), Tmax=(1575.15,'K')),
            NASAPolynomial(coeffs=[32.5752,0.0162621,-2.97426e-06,-4.23656e-10,1.35208e-13,-35462,-144.968], Tmin=(1575.15,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-203.013,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (465.61,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 5, 'C=O': 2, 'C=C': 2, 'C-H': 10}
1D rotors:
* Invalidated! pivots: [3, 4], dihedral: [5, 3, 4, 6], invalidation reason: Another conformer for C8H10O2[220] exists which is 1.85 kJ/mol lower.Another conformer for C8H10O2[220] exists which is 1.85 kJ/mol lower.
pivots: [3, 5], dihedral: [4, 3, 5, 7], rotor symmetry: 1, max scan energy: 21.77 kJ/mol
pivots: [4, 6], dihedral: [3, 4, 6, 9], rotor symmetry: 1, max scan energy: 21.77 kJ/mol
pivots: [5, 8], dihedral: [3, 5, 8, 1], rotor symmetry: 1, max scan energy: 44.64 kJ/mol
pivots: [6, 10], dihedral: [4, 6, 10, 2], rotor symmetry: 1, max scan energy: 44.64 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O      -0.62396100    1.55460900   -1.04793000
O      -0.11051700   -3.25895700    2.50514000
C      -0.68631700   -1.11039200    0.07164000
C      -0.04815100   -0.59396600    1.38554800
C      -1.90790300   -0.32151500   -0.32115700
C       1.17343200   -1.38284600    1.77834800
C      -3.16592900   -0.76068300   -0.19573900
C      -1.70534700    1.03581000   -0.88439900
C       2.43146000   -0.94368600    1.65292400
C       0.97087000   -2.74016600    2.34160200
H       0.05631700   -1.03114800   -0.72784700
H      -0.95128400   -2.16219400    0.18988500
H      -0.79078700   -0.67320900    2.18503400
H       0.21681800    0.45783600    1.26730400
H      -3.39648300   -1.74285300    0.20129400
H      -4.00643400   -0.13977100   -0.49118600
H      -2.64145400    1.56659300   -1.16267400
H       2.66201800    0.03848100    1.25588300
H       3.27196200   -1.56459900    1.94837400
H       1.90697600   -3.27095000    2.61987900
""",
)

entry(
    index = 164,
    label = "P214",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {12,S}
3  C u0 p0 c0 {1,S} {9,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {10,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {7,D} {17,S}
6  C u0 p0 c0 {2,S} {8,D} {18,S}
7  C u0 p0 c0 {5,D} {9,S} {19,S}
8  C u0 p0 c0 {6,D} {10,S} {20,S}
9  O u0 p2 c0 {3,S} {7,S}
10 O u0 p2 c0 {4,S} {8,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89117,0.00670168,0.000248759,-4.68293e-07,2.79587e-10,-19382.3,14.4353], Tmin=(10,'K'), Tmax=(499.279,'K')),
            NASAPolynomial(coeffs=[-4.11286,0.089856,-5.82358e-05,1.79631e-08,-2.11644e-12,-18820.2,45.1153], Tmin=(499.279,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-161.188,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (482.239,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 4, 'C-C': 5, 'C=C': 2, 'C-H': 10}
1D rotors:
* Invalidated! pivots: [3, 4], dihedral: [5, 3, 4, 6], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers


External symmetry: 2, optical isomers: 2

Geometry:
O      -2.72229000   -0.88927000   -0.04122900
O       0.82943400   -2.17799100   -1.64707300
C      -0.61252400    0.18851300    0.43167300
C       0.61150200   -0.06499000   -0.49638000
C      -1.48603700   -1.06185000    0.71074400
C       0.28755700   -0.83426900   -1.80312400
C      -1.64391200    1.11323900   -0.18467100
C       1.64258800   -0.99022400    0.11970600
C      -2.75171800    0.41714400   -0.43290000
C       1.66120800   -2.13116100   -0.56681900
H      -0.22234900    0.58838500    1.37354600
H       1.03899000    0.91421600   -0.73652400
H      -1.03183500   -1.99954600    0.39202100
H      -1.75712000   -1.13619900    1.76705300
H       0.78131600   -0.38435500   -2.66833000
H      -0.77821400   -0.92805300   -2.00925800
H      -1.47850000    2.15019100   -0.43586700
H       2.21880400   -0.77634000    1.00737600
H      -3.67245800    0.72189300   -0.91116500
H       2.22518400   -3.03763200   -0.39473300
""",
)

entry(
    index = 165,
    label = "P215",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {7,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {11,S}
3  C u0 p0 c0 {2,D} {5,S} {12,S}
4  C u0 p0 c0 {5,D} {6,S} {13,S}
5  C u0 p0 c0 {3,S} {4,D} {14,S}
6  C u0 p0 c0 {4,S} {8,D} {15,S}
7  C u1 p0 c0 {1,S} {16,S} {17,S}
8  C u0 p0 c0 {6,D} {18,S} {19,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 O u1 p2 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.56013,0.0625848,-2.02325e-05,-1.03232e-08,5.99083e-12,29277.3,15.4141], Tmin=(10,'K'), Tmax=(1161.24,'K')),
            NASAPolynomial(coeffs=[14.3403,0.044925,-2.25755e-05,5.46302e-09,-5.16682e-13,25460.6,-43.8591], Tmin=(1161.24,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (243.472,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (448.981,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 10, 'C-C': 4, 'C=C': 3, 'C-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [8, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [2, 8], dihedral: [3, 2, 8, 16], rotor symmetry: 1, max scan energy: 1.79 kJ/mol
* Invalidated! pivots: [4, 6], dihedral: [1, 4, 6, 5], invalidation reason: Another conformer for C8H10O[230] exists which is 8.86 kJ/mol lower.Another conformer for C8H10O[230] exists which is 8.86 kJ/mol lower.
pivots: [5, 7], dihedral: [6, 5, 7, 9], rotor symmetry: 1, max scan energy: 33.22 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.03321300   -0.82209700   -1.12602300
C       0.81319900    0.56469200   -2.84267600
C       0.75592700    0.66349700   -1.36049800
C      -0.21330100   -0.06739500   -0.57999100
C      -1.04999500   -0.50094700    1.70489100
C      -0.18539700    0.12908400    0.88981300
C      -1.07995900   -0.35823800    3.14550000
C       2.19807300    0.51476000   -3.39845900
C      -1.95110700   -0.99749600    3.93685000
H       0.27934400    1.44713500   -3.26062800
H       0.21172500   -0.29174600   -3.16290100
H       1.45312600    1.32451000   -0.85264400
H      -1.77770500   -1.16545400    1.24468000
H       0.56237400    0.80427800    1.29740300
H      -0.34554100    0.31008700    3.58985400
H       3.02820700    0.97812900   -2.87938200
H       2.37332400    0.11227000   -4.38771200
H      -2.69627100   -1.67111700    3.52632300
H      -1.94514000   -0.86730300    5.01230100
""",
)

entry(
    index = 166,
    label = "P216",
    molecule = 
"""
1  O u0 p2 c0 {8,D}
2  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {5,D} {7,S} {8,S}
4  C u0 p0 c0 {2,S} {6,D} {13,S}
5  C u0 p0 c0 {3,D} {6,S} {14,S}
6  C u0 p0 c0 {4,D} {5,S} {16,S}
7  C u0 p0 c0 {3,S} {9,D} {15,S}
8  C u0 p0 c0 {1,D} {3,S} {17,S}
9  C u0 p0 c0 {7,D} {18,S} {19,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.20815,0.0657782,-3.7873e-05,1.00169e-08,-8.82473e-13,-578.666,13.0765], Tmin=(10,'K'), Tmax=(1480.7,'K')),
            NASAPolynomial(coeffs=[14.8973,0.0403883,-1.84202e-05,4.08058e-09,-3.56667e-13,-4718.58,-50.1954], Tmin=(1480.7,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-4.9142,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (448.981,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 10, 'C-C': 4, 'C=C': 3, 'C=O': 1}
1D rotors:
pivots: [2, 4], dihedral: [10, 2, 4, 6], rotor symmetry: 3, max scan energy: 7.28 kJ/mol
pivots: [3, 7], dihedral: [5, 3, 7, 9], rotor symmetry: 1, max scan energy: 18.65 kJ/mol
* Invalidated! pivots: [3, 8], dihedral: [5, 3, 8, 1], invalidation reason: Another conformer for C8H10O[186] exists which is 8.22 kJ/mol lower.Another conformer for C8H10O[186] exists which is 8.22 kJ/mol lower.
* Invalidated! pivots: [5, 6], dihedral: [3, 5, 6, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
O       1.76683600   -0.38565900   -4.13569700
C       0.79542100   -0.90193300    3.17070800
C       1.47224100   -0.06279200   -1.76125800
C       0.96588800   -1.27671700    1.73452000
C       1.29459300   -0.83357700   -0.64895200
C       1.13496300   -0.41027400    0.71987100
C       1.53115000    1.39914200   -1.73083400
C       1.60297100   -0.83177800   -3.02203300
C       1.70200300    2.22019600   -2.77418500
H       1.58144600   -1.35208000    3.78794500
H       0.82321400    0.18002100    3.31487900
H      -0.15713500   -1.27732200    3.56207700
H       0.94949100   -2.34194700    1.50816300
H       1.26825500   -1.91139300   -0.80295100
H       1.42286000    1.84924600   -0.74834200
H       1.15176900    0.65251300    0.94226800
H       1.53567300   -1.93206000   -2.86818600
H       1.72797000    3.29301200   -2.61898800
H       1.81692800    1.84856800   -3.78177800
""",
)

entry(
    index = 167,
    label = "P217",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,D} {11,S}
3  C u0 p0 c0 {1,S} {7,D} {12,S}
4  C u0 p0 c0 {2,D} {5,S} {13,S}
5  C u0 p0 c0 {4,S} {6,D} {15,S}
6  C u0 p0 c0 {5,D} {8,S} {14,S}
7  C u0 p0 c0 {3,D} {18,S} {19,S}
8  C u1 p0 c0 {6,S} {16,S} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 O u1 p2 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.50736,0.0672063,-3.83602e-05,9.3175e-09,-5.90533e-13,22772.8,14.3806], Tmin=(10,'K'), Tmax=(1534.38,'K')),
            NASAPolynomial(coeffs=[22.627,0.0280847,-1.05966e-05,1.80863e-09,-1.09088e-13,15643.4,-90.1589], Tmin=(1534.38,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (189.307,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (444.824,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 10, 'C-C': 4, 'C=C': 3, 'C-O': 1}
1D rotors:
pivots: [2, 3], dihedral: [4, 2, 3, 5], rotor symmetry: 1, max scan energy: 15.92 kJ/mol
pivots: [2, 4], dihedral: [3, 2, 4, 8], rotor symmetry: 1, max scan energy: 11.32 kJ/mol
* Invalidated! pivots: [5, 6], dihedral: [1, 5, 6, 7], invalidation reason: Another conformer for C8H10O[225] exists which is 7.88 kJ/mol lower.Another conformer for C8H10O[225] exists which is 7.88 kJ/mol lower.
* Invalidated! pivots: [7, 9], dihedral: [6, 7, 9, 16], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 5], dihedral: [2, 3, 5, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [6, 7], dihedral: [5, 6, 7, 9], rotor symmetry: 1, max scan energy: 68.80 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.59139000   -0.63591800   -1.43268000
C       1.93989200   -0.54143800   -0.05625900
C       0.59625600   -0.33896400    0.56093600
C       2.82415500    0.67508500    0.10194200
C      -0.62835800   -0.40641000   -0.20112600
C      -1.91010400   -0.20491300    0.47765100
C      -3.12740200   -0.25634600   -0.20298400
C       3.95512300    0.71018500    0.80000300
C      -4.35395200   -0.07504800    0.38431300
H       1.79883500   -0.77462600   -1.11535400
H       2.43433500   -1.40199700    0.41461300
H       0.54471900   -0.11628500    1.62298400
H       2.47542200    1.57455200   -0.40077600
H      -3.07148100   -0.45521300   -1.26943300
H      -1.90223800   -0.00949900    1.54638900
H      -4.44799700    0.12519800    1.44636000
H      -5.26822900   -0.12606400   -0.19328100
H       4.33419300   -0.16725000    1.31568800
H       4.54845300    1.61451300    0.87392500
""",
)