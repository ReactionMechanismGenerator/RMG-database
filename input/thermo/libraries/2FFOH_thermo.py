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