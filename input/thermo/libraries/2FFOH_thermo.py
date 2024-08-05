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

entry(
    index = 168,
    label = "P218",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3  C u1 p0 c0 {5,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {5,T}
5  C u0 p0 c0 {3,S} {4,T}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.6336,0.0296985,-1.5274e-05,2.10128e-09,5.40964e-13,18099.7,12.3544], Tmin=(10,'K'), Tmax=(1096.69,'K')),
            NASAPolynomial(coeffs=[5.88755,0.0246708,-1.27649e-05,3.2309e-09,-3.21752e-13,17413.2,0.396909], Tmin=(1096.69,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (150.449,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (228.648,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C-H': 4, 'C#C': 1, 'C-C': 2, 'C-O': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [10, 1, 2, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [2, 4], dihedral: [1, 2, 4, 5], rotor symmetry: 2, max scan energy: 0.03 kJ/mol (set as a FreeRotor)
* Invalidated! pivots: [3, 5], dihedral: [8, 3, 5, 4], invalidation reason: not a torsional mode (angles = 120.92, 179.73 degrees)


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.17053200   -0.63509500   -0.32698000
C      -1.50007900   -0.16928700   -0.53724500
C      -1.73281100    3.83711500   -1.09503800
C      -1.59928300    1.27526400   -0.72448300
C      -1.66038600    2.48640200   -0.90198500
H      -1.97056000   -0.67602200   -1.39361100
H      -2.06234100   -0.46847900    0.35325200
H      -2.60905500    4.28901600   -1.54378000
H      -0.91679200    4.48568200   -0.80036100
H       0.36979800   -0.30338900   -1.05151100
""",
)

entry(
    index = 169,
    label = "P219",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 C u0 p0 c0 {1,S} {3,D} {5,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.10265,-0.00760795,6.11929e-05,-8.55215e-08,3.89121e-11,58934.1,5.28581], Tmin=(10,'K'), Tmax=(692.069,'K')),
            NASAPolynomial(coeffs=[1.8301,0.0152454,-9.40407e-06,2.77534e-09,-3.13708e-13,59015.9,13.7316], Tmin=(692.069,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (490.019,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 1, 'C=C': 2, 'C-H': 2}

External symmetry: 2, optical isomers: 1

Geometry:
C      -0.64439600    0.12455500   -0.08900700
C       0.63365900   -0.18546500    0.05255500
C       0.18305000    1.03839300    0.62143000
H      -1.62833000   -0.11465800   -0.46330100
H       1.45601700   -0.86282500   -0.12167600
""",
)

entry(
    index = 170,
    label = "P220",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 C u0 p0 c0 {2,D} {7,S} {8,S}
4 C u0 p1 c0 {1,S} {2,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95084,0.00315427,8.64579e-05,-1.78995e-07,1.16564e-10,69327,8.08759], Tmin=(10,'K'), Tmax=(479.685,'K')),
            NASAPolynomial(coeffs=[2.24995,0.0267217,-1.65827e-05,4.99367e-09,-5.81425e-13,69382.2,13.9186], Tmin=(479.685,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (576.406,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 4, 'C-C': 3, 'C=C': 1}

External symmetry: 1, optical isomers: 1

Geometry:
C      -1.13083500   -0.02352700    0.58237600
C       0.09116000   -0.15806500   -0.18655100
C       1.32740000    0.20794100   -0.52617300
C      -0.92612000   -1.12204500   -0.48580800
H      -1.18495200   -0.35679200    1.62001300
H      -1.86211900    0.75223300    0.34977400
H       1.86112100   -0.34576000   -1.29417100
H       1.83970800    1.04818300   -0.06575900
""",
)

entry(
    index = 171,
    label = "P221",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,D} {9,S}
3  C u0 p0 c0 {4,D} {5,S} {10,S}
4  C u0 p0 c0 {2,D} {3,D}
5  O u0 p2 c0 {3,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86506,0.0101952,0.00014541,-3.94171e-07,3.2714e-10,-1240.32,10.3953], Tmin=(10,'K'), Tmax=(395.541,'K')),
            NASAPolynomial(coeffs=[3.12418,0.0361099,-2.27286e-05,6.96973e-09,-8.23668e-13,-1325.82,11.4607], Tmin=(395.541,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-10.3064,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (249.434,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C-H': 5, 'C-C': 1, 'C=C': 2, 'C-O': 1}
1D rotors:
pivots: [1, 4], dihedral: [11, 1, 4, 5], rotor symmetry: 1, max scan energy: 21.33 kJ/mol
pivots: [2, 3], dihedral: [6, 2, 3, 5], rotor symmetry: 3, max scan energy: 6.61 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       0.10212400   -0.15659500    4.23207500
C      -1.62815000    0.77597600    0.04215600
C      -0.66625500   -0.18167000    0.70023900
C       0.54761800    0.20897700    2.98337700
C      -0.06475200    0.01286500    1.84481900
H      -1.25586300    1.07748200   -0.94294300
H      -1.77459700    1.67146800    0.64712500
H      -2.60088100    0.29847900   -0.11832500
H      -0.46733400   -1.10455100    0.15180500
H       1.51166300    0.70146200    3.04666300
H      -0.75112700   -0.59416400    4.12999100
""",
)

entry(
    index = 172,
    label = "P222",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {4,D} {9,S} {10,S}
4  C u0 p0 c0 {2,D} {3,D}
5  O u0 p2 c0 {1,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80736,0.0144187,0.000167796,-5.26439e-07,4.75778e-10,-379.439,10.0201], Tmin=(10,'K'), Tmax=(394.417,'K')),
            NASAPolynomial(coeffs=[5.808,0.0284257,-1.59072e-05,4.53179e-09,-5.18054e-13,-804.023,-1.15229], Tmin=(394.417,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-3.14389,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (249.434,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C-H': 5, 'C-C': 1, 'C=C': 2, 'C-O': 1}
1D rotors:
pivots: [1, 2], dihedral: [11, 1, 2, 3], rotor symmetry: 1, max scan energy: 11.86 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 5], rotor symmetry: 1, max scan energy: 12.36 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.10868300    0.74063600    1.25745500
C      -1.43837800   -0.50620700    1.09019100
C      -0.36616400   -0.43338300    0.02771500
C      -0.28365300   -1.99039900   -2.06308200
C      -0.32083000   -1.20616300   -1.02293100
H      -0.98511600   -0.71935200    2.06180500
H      -2.13821200   -1.31821900    0.85816900
H       0.39216400    0.33514900    0.16487400
H      -0.78413900   -1.72658600   -2.98990700
H       0.25370200   -2.93368800   -2.04109500
H      -2.49828100    0.97176200    0.40777000
""",
)

entry(
    index = 173,
    label = "P223",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,D}
4  C u0 p0 c0 {2,S} {5,D} {11,S}
5  C u0 p0 c0 {3,S} {4,D} {12,S}
6  O u0 p2 c0 {1,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90365,0.0056138,0.000151898,-2.79977e-07,1.58459e-10,-32734.3,11.7133], Tmin=(10,'K'), Tmax=(561.447,'K')),
            NASAPolynomial(coeffs=[-0.0834711,0.055216,-3.7252e-05,1.18628e-08,-1.43177e-12,-32620.7,25.6722], Tmin=(561.447,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-272.209,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C-H': 5, 'C-C': 4, 'C=C': 1, 'C-O': 1, 'C=O': 1}
1D rotors:
pivots: [1, 3], dihedral: [13, 1, 3, 4], rotor symmetry: 1, max scan energy: 28.61 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       2.11358700   -0.32493100    0.12197600
O       0.85306400    2.22033600    0.04584600
C       0.83282300   -0.15611400   -0.44139800
C      -0.19536600   -1.19064900    0.03885900
C       0.21122000    1.19705700   -0.05351100
C      -1.43859300   -0.36498200    0.27100100
C      -1.21880500    0.95689800    0.21421100
H       0.88221900   -0.17639000   -1.54261300
H      -0.36375800   -2.00827000   -0.66689800
H       0.15447600   -1.63729500    0.97574600
H      -2.39887500   -0.82141700    0.48411800
H      -1.93641500    1.74612600    0.39389700
H       2.50441900    0.55959700    0.15876400
""",
)

entry(
    index = 174,
    label = "P224",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {4,D} {6,S}
3  C u0 p0 c0 {1,S} {5,D} {9,S}
4  C u0 p0 c0 {2,D} {7,S} {10,S}
5  C u0 p0 c0 {3,D} {11,S} {12,S}
6  O u0 p2 c0 {1,S} {2,S}
7  O u0 p2 c0 {4,S} {13,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75981,0.0154403,0.000194436,-4.77889e-07,3.3659e-10,-5575.93,11.8067], Tmin=(10,'K'), Tmax=(503.552,'K')),
            NASAPolynomial(coeffs=[6.76257,0.0406654,-2.68998e-05,8.69557e-09,-1.0791e-12,-6500.56,-6.79804], Tmin=(503.552,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-46.4222,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 3, 'H-O': 1, 'C-H': 5, 'C-C': 2, 'C=C': 2}
1D rotors:
pivots: [2, 6], dihedral: [13, 2, 6, 4], rotor symmetry: 1, max scan energy: 14.55 kJ/mol
pivots: [3, 5], dihedral: [1, 3, 5, 7], rotor symmetry: 1, max scan energy: 18.89 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       0.74857200   -1.03865100   -0.88888900
O       3.29076600   -0.11239200    0.73567500
C      -0.26079400    0.05495800   -0.68671000
C       1.06456300    0.06128500   -0.13113200
C      -1.44630300   -0.31605800    0.10719600
C       2.08133400    0.51646300    0.57786100
C      -2.67559300    0.10452000   -0.18131800
H      -0.44496300    0.61957200   -1.59771400
H      -1.25626000   -0.94866800    0.96916900
H       2.02535700    1.46040300    1.10036100
H      -2.87331200    0.73762500   -1.04066200
H      -3.52583400   -0.16342200    0.43411600
H       3.27250400   -0.94393600    0.24806200
""",
)

entry(
    index = 175,
    label = "P226",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {5,S} {15,S} {16,S}
5  C u1 p0 c0 {3,S} {4,S} {6,S}
6  C u0 p0 c0 {5,S} {7,D} {17,S}
7  C u0 p0 c0 {6,D} {8,S} {18,S}
8  O u0 p2 c0 {7,S} {19,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71623,0.0283015,9.81264e-05,-1.66263e-07,7.78408e-11,-9510.99,13.119], Tmin=(10,'K'), Tmax=(710.878,'K')),
            NASAPolynomial(coeffs=[0.370527,0.0708501,-4.17109e-05,1.18211e-08,-1.29649e-12,-9634.73,23.9023], Tmin=(710.878,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-79.0985,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (453.139,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 10, 'H-O': 1, 'C-C': 6, 'C-O': 1, 'C=C': 1}
1D rotors:
pivots: [1, 8], dihedral: [19, 1, 8, 7], rotor symmetry: 1, max scan energy: 20.18 kJ/mol
* Invalidated! pivots: [6, 7], dihedral: [4, 6, 7, 8], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [7, 8], dihedral: [6, 7, 8, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       1.19625700   -3.45539700    0.48364800
C      -1.54439500    0.98472300   -0.40792900
C      -2.09353400   -0.14165500    0.48389900
C      -0.02644800    0.94165900   -0.14972700
C      -1.02766500   -1.25604000    0.37693200
C       0.27044600   -0.52252100    0.09254700
C       1.55108700   -1.06506100    0.03472700
C       1.97078100   -2.36823300    0.21336000
H      -1.99101400    1.95710600   -0.18783800
H      -1.74776700    0.75798700   -1.46010100
H      -2.15625600    0.20624000    1.52016100
H      -3.09033100   -0.47820500    0.19064800
H       0.21627000    1.54062100    0.74181700
H       0.56023400    1.36002000   -0.97358700
H      -1.28397700   -1.94043700   -0.44732200
H      -0.99216100   -1.85693500    1.29567100
H       2.36217200   -0.37549400   -0.18662900
H       3.01515000   -2.64112200    0.14461100
H       0.27011400   -3.19351100    0.51574200
""",
)

entry(
    index = 176,
    label = "P227",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {5,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
5  C u0 p0 c0 {3,S} {4,S} {11,S} {12,S}
6  C u0 p0 c0 {1,S} {7,D} {17,S}
7  C u0 p0 c0 {6,D} {18,S} {19,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {6,S}
18 O u1 p2 c0 {7,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89283,0.0326634,5.57592e-05,-8.29125e-08,3.04787e-11,-9563.68,13.9732], Tmin=(10,'K'), Tmax=(979.123,'K')),
            NASAPolynomial(coeffs=[4.72271,0.0594932,-3.16402e-05,8.11868e-09,-8.13043e-13,-11174.8,2.58978], Tmin=(979.123,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-79.4105,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (453.139,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 11, 'C-C': 6, 'C-O': 1, 'C=C': 1}
1D rotors:
pivots: [2, 7], dihedral: [3, 2, 7, 8], rotor symmetry: 1, max scan energy: 12.02 kJ/mol
* Invalidated! pivots: [7, 8], dihedral: [2, 7, 8, 1], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers


External symmetry: 1, optical isomers: 1

Geometry:
O       3.02212800   -1.56939800    0.35180500
C       0.44494000   -0.23827700   -0.12307500
C      -0.52478300   -0.38559500   -1.32460200
C      -0.34545900    0.72116400    0.80454300
C      -1.92410800   -0.48135700   -0.67673400
C      -1.80811600    0.23452900    0.70045900
C       1.79260100    0.24995500   -0.49037100
C       2.99413100   -0.47376000   -0.21536900
H       0.55463000   -1.20792300    0.37172200
H      -2.20347100   -1.52858600   -0.53758900
H      -2.68928800   -0.03258700   -1.31397000
H      -2.51152200    1.06454800    0.79665100
H      -2.03093900   -0.46372800    1.51094100
H      -0.28097300   -1.24684300   -1.94991000
H      -0.45511600    0.50789400   -1.95537000
H      -0.25463100    1.74525000    0.42501100
H       0.03714700    0.71654300    1.82718200
H       1.88057600    1.20958400   -0.99661300
H       3.93649200    0.00521300   -0.54371900
""",
)

entry(
    index = 177,
    label = "P228",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {5,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {4,S} {6,D}
6  C u0 p0 c0 {5,D} {7,S} {17,S}
7  C u0 p0 c0 {6,S} {8,D} {18,S}
8  C u0 p0 c0 {7,D} {19,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 O u0 p2 c0 {8,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.60859,0.0358829,8.07502e-05,-1.52827e-07,7.53279e-11,-4923.02,13.2948], Tmin=(10,'K'), Tmax=(686.355,'K')),
            NASAPolynomial(coeffs=[1.34198,0.0705759,-4.20213e-05,1.2027e-08,-1.33023e-12,-5117.9,19.6906], Tmin=(686.355,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-40.9736,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (453.139,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 10, 'C-C': 6, 'C=C': 2, 'C=O': 1}
1D rotors:
pivots: [7, 8], dihedral: [6, 7, 8, 9], rotor symmetry: 1, max scan energy: 21.12 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       4.96168900   -0.40788400    0.74773200
C      -1.83993100    0.91875900   -0.27572000
C      -2.17575000   -0.54377600    0.06577300
C      -0.30055300    0.92932400   -0.40360800
C      -1.03947800   -0.95329400    1.02168400
C       0.17243300   -0.20319600    0.49524900
C       1.44564200   -0.52073600    0.76330400
C       2.60782900    0.20143900    0.25200800
C       3.85720100   -0.12601900    0.51765400
H      -2.14806600    1.56767400    0.55106800
H      -2.34355600    1.27756500   -1.17604100
H      -2.13638200   -1.15613800   -0.84182900
H      -3.16955500   -0.66519000    0.50286700
H       0.13296400    1.89626500   -0.12827400
H      -0.00242500    0.73518900   -1.44218600
H      -1.27971500   -0.61544900    2.03904200
H      -0.88104600   -2.03344400    1.07217900
H       1.65166800   -1.37375400    1.40368200
H       2.48746200    1.06610800   -0.39120400
""",
)

entry(
    index = 178,
    label = "P229",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
2  C u0 p0 c0 {4,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {4,D} {15,S}
4  C u0 p0 c0 {2,S} {3,D} {13,S}
5  C u0 p0 c0 {1,S} {7,D} {16,S}
6  C u0 p0 c0 {2,S} {8,D} {14,S}
7  C u0 p0 c0 {5,D} {9,S} {17,S}
8  C u0 p0 c0 {6,D} {18,S} {19,S}
9  O u0 p2 c0 {1,S} {7,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49831,0.0608212,-2.34944e-05,-3.4311e-09,3.15551e-12,17727.6,13.5661], Tmin=(10,'K'), Tmax=(1249.02,'K')),
            NASAPolynomial(coeffs=[13.7595,0.0431577,-2.05335e-05,4.73053e-09,-4.28023e-13,13978.8,-42.9657], Tmin=(1249.02,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (147.396,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (448.981,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 10, 'C-C': 4, 'C-O': 2, 'C=C': 3}
1D rotors:
pivots: [2, 4], dihedral: [1, 2, 4, 5], rotor symmetry: 1, max scan energy: 16.53 kJ/mol
pivots: [3, 5], dihedral: [7, 3, 5, 4], rotor symmetry: 1, max scan energy: 11.48 kJ/mol
* Invalidated! pivots: [3, 7], dihedral: [5, 3, 7, 9], invalidation reason: Another conformer for C8H10O[181] exists which is 2.50 kJ/mol lower.Another conformer for C8H10O[181] exists which is 2.50 kJ/mol lower.


External symmetry: 1, optical isomers: 2

Geometry:
O      -3.11039800   -0.33803600   -1.52375600
C      -2.22309700   -0.71481300   -0.37171300
C       1.45253300    0.57134500   -0.09497500
C      -1.02865600    0.16367800   -0.29462500
C       0.22224900   -0.29051000   -0.21951200
C      -3.41334700   -0.41943500    0.52820100
C       2.18756700    0.33269800    1.20169500
C      -4.09501900   -0.11465300   -0.57886300
C       3.42640100   -0.13889800    1.30154000
H      -1.96060000   -1.76986200   -0.47214900
H       1.16094700    1.62569800   -0.16540900
H       2.12959100    0.36598200   -0.93254500
H       0.39809400   -1.36526000   -0.22824000
H       1.62759300    0.56179300    2.10643200
H      -1.23310300    1.23199000   -0.28315400
H      -3.59306900   -0.44895100    1.58874100
H      -5.08378700    0.20722700   -0.87763900
H       3.90013600   -0.29392300    2.26434700
H       4.01497200   -0.38329300    0.42205500
""",
)

entry(
    index = 179,
    label = "P230",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {10,S}
3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {5,D} {14,S}
5  C u0 p0 c0 {2,S} {4,D} {15,S}
6  C u0 p0 c0 {3,S} {8,D} {13,S}
7  C u0 p0 c0 {2,S} {16,D} {17,S}
8  C u0 p0 c0 {6,D} {18,S} {19,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 O u0 p2 c0 {7,D}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.5745,0.052426,3.41404e-06,-3.22999e-08,1.33978e-11,9330.16,14.7607], Tmin=(10,'K'), Tmax=(1038.84,'K')),
            NASAPolynomial(coeffs=[8.58852,0.0537729,-2.83524e-05,7.22393e-09,-7.1933e-13,7173.98,-14.9839], Tmin=(1038.84,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (77.6082,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (448.981,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 10, 'C-C': 6, 'C=C': 2, 'C=O': 1}
1D rotors:
pivots: [2, 4], dihedral: [3, 2, 4, 7], rotor symmetry: 1, max scan energy: 18.54 kJ/mol
* Invalidated! pivots: [3, 8], dihedral: [2, 3, 8, 1], invalidation reason: Another conformer for C8H10O[182] exists which is 0.81 kJ/mol lower.Another conformer for C8H10O[182] exists which is 0.81 kJ/mol lower.
pivots: [4, 7], dihedral: [2, 4, 7, 9], rotor symmetry: 1, max scan energy: 10.36 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.69547400    2.53593100    1.10976700
C      -0.43273100   -0.38471500   -0.66795700
C      -1.13122400    0.24582500    0.60926400
C       1.02883600   -0.81940500   -0.48695600
C      -1.50068100   -1.46136800   -0.57992200
C      -2.08302600   -0.94399300    0.50526700
C       1.98230300    0.34062300   -0.42073700
C      -1.78025000    1.58634900    0.37353900
C       2.77016400    0.62551400    0.61157900
H      -0.51939000    0.25306600   -1.55687500
H      -0.50233300    0.29761500    1.50050300
H       1.29442100   -1.46182800   -1.33756500
H       1.11801600   -1.43490900    0.41416600
H       2.00351500    0.98867400   -1.29607200
H      -1.69889100   -2.33612900   -1.18939100
H      -2.93869500   -1.22527700    1.10753700
H      -2.38178400    1.63948400   -0.56392400
H       2.78207900    0.00882200    1.50542700
H       3.43364900    1.48269100    0.60173300
""",
)

entry(
    index = 180,
    label = "P231",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,D} {11,S}
3  C u0 p0 c0 {1,S} {7,D} {12,S}
4  C u0 p0 c0 {2,D} {5,S} {13,S}
5  C u0 p0 c0 {4,S} {6,D} {14,S}
6  C u0 p0 c0 {5,D} {8,S} {15,S}
7  C u0 p0 c0 {3,D} {18,S} {19,S}
8  C u0 p0 c0 {6,S} {16,D} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 O u0 p2 c0 {8,D}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.22071,0.0787465,-0.000156468,3.52061e-07,-3.09559e-10,1791.38,13.1661], Tmin=(10,'K'), Tmax=(401.398,'K')),
            NASAPolynomial(coeffs=[1.08574,0.0747895,-4.73889e-05,1.42903e-08,-1.65072e-12,2166.04,24.0494], Tmin=(401.398,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (14.8765,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (444.824,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 10, 'C-C': 4, 'C=C': 3, 'C=O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [4, 2, 3, 5], invalidation reason: Another conformer for C8H10O[183] exists which is 1.91 kJ/mol lower.Another conformer for C8H10O[183] exists which is 1.91 kJ/mol lower.
pivots: [2, 4], dihedral: [3, 2, 4, 8], rotor symmetry: 1, max scan energy: 11.76 kJ/mol
pivots: [5, 6], dihedral: [3, 5, 6, 7], rotor symmetry: 1, max scan energy: 35.74 kJ/mol
pivots: [7, 9], dihedral: [6, 7, 9, 1], rotor symmetry: 1, max scan energy: 45.17 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       4.57842200    2.04233100    2.32818900
C      -2.33263000   -0.25169900    1.16840600
C      -1.18073300    0.71425400    1.17541600
C      -2.84270200   -0.51458800   -0.22943000
C       0.06001500    0.43708500    1.60681500
C       1.14433300    1.39325800    1.58846100
C       2.39938700    1.15594000    2.01827200
C      -4.06066600   -0.20815100   -0.66439400
C       3.43331400    2.19032100    1.95948800
H      -3.15154500    0.15307900    1.77543300
H      -2.01941700   -1.19358200    1.63309600
H      -1.39142400    1.70637900    0.77934600
H      -2.13102300   -0.97924300   -0.90870700
H       0.28125700   -0.55365300    1.99863400
H       0.91385700    2.38210200    1.19251200
H       2.69522600    0.19272000    2.42396100
H       3.08986200    3.16224600    1.53786200
H      -4.79638300    0.25943700   -0.01667700
H      -4.36964700   -0.41845200   -1.68196400
""",
)

entry(
    index = 181,
    label = "P232",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {9,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {6,D} {15,S}
4  C u0 p0 c0 {2,S} {7,D} {14,S}
5  C u0 p0 c0 {1,S} {8,D} {16,S}
6  C u0 p0 c0 {3,D} {7,S} {17,S}
7  C u0 p0 c0 {4,D} {6,S} {18,S}
8  C u0 p0 c0 {5,D} {19,S} {20,S}
9  O u0 p2 c0 {2,S} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 O u1 p2 c0 {4,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.8538,0.117635,-0.000348544,7.68892e-07,-6.30066e-10,-18376.1,15.0269], Tmin=(10,'K'), Tmax=(403.822,'K')),
            NASAPolynomial(coeffs=[2.37843,0.0797869,-4.9882e-05,1.48669e-08,-1.70082e-12,-17990.7,21.1855], Tmin=(403.822,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-152.816,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (490.554,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 10, 'H-O': 1, 'C-C': 4, 'C-O': 2, 'C=C': 3}
1D rotors:
pivots: [1, 4], dihedral: [21, 1, 4, 6], rotor symmetry: 1, max scan energy: 31.95 kJ/mol
pivots: [3, 5], dihedral: [7, 3, 5, 8], rotor symmetry: 1, max scan energy: 9.66 kJ/mol
pivots: [3, 7], dihedral: [5, 3, 7, 10], rotor symmetry: 1, max scan energy: 11.57 kJ/mol
* Invalidated! pivots: [4, 6], dihedral: [1, 4, 6, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [8, 9], dihedral: [5, 8, 9, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [6, 9], dihedral: [2, 6, 9, 8], rotor symmetry: 1, max scan energy: 47.69 kJ/mol
* Invalidated! pivots: [5, 8], dihedral: [3, 5, 8, 9], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O      -4.23249600   -0.93911100    0.43939200
O      -3.08487400   -1.32650000   -1.89439600
C      -1.35794900    1.44251300   -6.00726800
C      -3.97196500    0.20903000   -0.31836100
C      -2.02156200    1.68671500   -4.68438900
C      -3.30735700   -0.14301000   -1.64532100
C      -0.00757400    2.11785200   -6.09519900
C      -2.35954300    0.70548700   -3.78599200
C      -2.96927800    0.93983100   -2.55079000
C       0.29931100    3.09391100   -6.94356400
H      -1.99716600    1.82526400   -6.81323100
H      -1.24642200    0.36413200   -6.16584200
H      -3.31177700    0.90035900    0.22791200
H      -4.90107300    0.76017400   -0.53108500
H      -2.22512200    2.72536200   -4.43141200
H       0.74083500    1.76337000   -5.38976100
H      -2.15192500   -0.33354300   -4.03055500
H      -3.20284700    1.95634700   -2.24632900
H      -0.42268400    3.47508300   -7.65967200
H       1.28570600    3.54326100   -6.95840100
H      -3.90843800   -1.67547600   -0.10515400
""",
)

entry(
    index = 182,
    label = "P233",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {6,D} {13,S}
3  C u0 p0 c0 {1,S} {5,D} {14,S}
4  C u0 p0 c0 {5,S} {7,D} {9,S}
5  C u0 p0 c0 {3,D} {4,S} {16,S}
6  C u0 p0 c0 {2,D} {8,S} {15,S}
7  C u0 p0 c0 {4,D} {10,S} {17,S}
8  C u1 p0 c0 {6,S} {18,S} {19,S}
9  O u0 p2 c0 {4,S} {20,S}
10 O u0 p2 c0 {7,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76902,0.0313602,0.0010815,-8.60945e-06,2.15696e-08,-13196.3,10.2631], Tmin=(10,'K'), Tmax=(135.449,'K')),
            NASAPolynomial(coeffs=[4.12089,0.0771719,-4.82353e-05,1.43816e-08,-1.64511e-12,-13257.4,7.36581], Tmin=(135.449,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-101.2,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (494.711,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 9, 'H-O': 2, 'C-C': 4, 'C-O': 2, 'C=C': 3}
1D rotors:
* Invalidated! pivots: [1, 6], dihedral: [20, 1, 6, 7], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [2, 9], dihedral: [21, 2, 9, 6], rotor symmetry: 1, max scan energy: 34.71 kJ/mol
pivots: [3, 4], dihedral: [5, 3, 4, 8], rotor symmetry: 1, max scan energy: 10.78 kJ/mol
pivots: [3, 5], dihedral: [4, 3, 5, 7], rotor symmetry: 1, max scan energy: 12.74 kJ/mol
* Invalidated! pivots: [6, 7], dihedral: [1, 6, 7, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [8, 10], dihedral: [4, 8, 10, 18], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 8], dihedral: [3, 4, 8, 10], invalidation reason: The rotor scan has a barrier of 69.78 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)The rotor scan has a barrier of 69.78 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 1, optical isomers: 2

Geometry:
O       3.45557700   -1.16716600   -1.79092800
O       4.85173600   -0.13556200    0.28897600
C      -0.27890100    0.79005300   -3.13225200
C      -1.40160700   -0.20702100   -3.07623700
C       1.03551400    0.18901300   -2.69784800
C       2.96053000   -0.03267300   -1.15253800
C       1.72764500    0.56796000   -1.61211900
C      -2.11640100   -0.65088000   -4.17770200
C       3.71006400    0.44957000   -0.14406500
C      -3.13887200   -1.58050900   -4.14745100
H      -0.19033500    1.17649000   -4.15495800
H      -0.50732800    1.64866100   -2.48706200
H      -1.63909800   -0.61774700   -2.09720700
H       1.41891500   -0.60931200   -3.32907000
H      -1.85050400   -0.22602800   -5.14519000
H       1.35292200    1.38602000   -1.00090100
H       3.46242200    1.36063400    0.38264900
H      -3.65989800   -1.87561000   -5.04903700
H      -3.45194300   -2.04052900   -3.21659600
H       2.72244700   -1.77599500   -1.93962600
H       4.98060500   -0.92812800   -0.25250600
""",
)

entry(
    index = 183,
    label = "P234",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {12,S}
3  C u0 p0 c0 {1,S} {2,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {6,D} {16,S}
5  C u0 p0 c0 {1,S} {8,D} {15,S}
6  C u0 p0 c0 {4,D} {7,S} {9,S}
7  C u1 p0 c0 {6,S} {10,S} {17,S}
8  C u0 p0 c0 {5,D} {18,S} {19,S}
9  O u0 p2 c0 {6,S} {20,S}
10 O u0 p2 c0 {7,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.45282,0.0578599,3.56038e-05,-9.4563e-08,4.44148e-11,-9873.26,15.1785], Tmin=(10,'K'), Tmax=(817.714,'K')),
            NASAPolynomial(coeffs=[6.57388,0.0713965,-4.20647e-05,1.1836e-08,-1.28462e-12,-11346.7,-5.13908], Tmin=(817.714,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-82.0972,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (503.026,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 9, 'H-O': 2, 'C-C': 6, 'C-O': 2, 'C=C': 2}
1D rotors:
* Invalidated! pivots: [1, 8], dihedral: [20, 1, 8, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [2, 9], dihedral: [21, 2, 9, 8], rotor symmetry: 1, max scan energy: 37.03 kJ/mol
* Invalidated! pivots: [3, 7], dihedral: [4, 3, 7, 10], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 6], dihedral: [3, 4, 6, 8], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [8, 9], dihedral: [1, 8, 9, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [6, 8], dihedral: [4, 6, 8, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       1.61266600    1.28153200    0.07469600
O       3.55002900    1.04871400    1.86977900
C      -1.16309900   -0.36366500   -0.77680600
C       0.22700100   -0.94992200   -1.13242700
C      -0.99283800   -1.81969200   -1.15611600
C       1.26644200   -1.10100600   -0.08880200
C      -1.81586300    0.59021700   -1.69231000
C       1.93502200   -0.01410000    0.44180700
C       2.97159200   -0.06933900    1.37023900
C      -2.53101200    1.65046700   -1.31355900
H      -1.32073900   -0.17565500    0.28057700
H       0.57970400   -0.63815900   -2.11645000
H      -1.37829900   -2.13648600   -2.11834000
H      -1.10652400   -2.54829700   -0.36171200
H      -1.67858100    0.39758000   -2.75573100
H       1.54572100   -2.09219000    0.24935400
H       3.37952500   -0.99463900    1.74663600
H      -2.70023100    1.87845500   -0.26566300
H      -2.97850600    2.31978100   -2.03845500
H       0.78223200    1.27495000   -0.41540800
H       3.09890500    1.80617300    1.46923000
""",
)

entry(
    index = 184,
    label = "P235",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {11,S}
2  C u0 p0 c0 {1,S} {5,D} {13,S}
3  C u0 p0 c0 {1,S} {8,D} {12,S}
4  C u0 p0 c0 {5,S} {7,D} {9,S}
5  C u0 p0 c0 {2,D} {4,S} {14,S}
6  C u1 p0 c0 {1,S} {16,S} {17,S}
7  C u0 p0 c0 {4,D} {10,S} {15,S}
8  C u0 p0 c0 {3,D} {18,S} {19,S}
9  O u0 p2 c0 {4,S} {20,S}
10 O u0 p2 c0 {7,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.37736,0.0722968,-2.36904e-05,-1.44779e-08,8.73649e-12,-3854.01,16.5371], Tmin=(10,'K'), Tmax=(1062.51,'K')),
            NASAPolynomial(coeffs=[13.1041,0.0562419,-3.00551e-05,7.7306e-09,-7.74851e-13,-7081.66,-36.4406], Tmin=(1062.51,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-32.0221,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (498.868,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 9, 'H-O': 2, 'C-C': 4, 'C-O': 2, 'C=C': 3}
1D rotors:
* Invalidated! pivots: [1, 6], dihedral: [20, 1, 6, 7], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [2, 9], dihedral: [21, 2, 9, 6], rotor symmetry: 1, max scan energy: 34.81 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [5, 3, 4, 7], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 5], dihedral: [4, 3, 5, 10], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [3, 8], dihedral: [4, 3, 8, 16], rotor symmetry: 1, max scan energy: 1.40 kJ/mol
* Invalidated! pivots: [6, 7], dihedral: [1, 6, 7, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       2.75796600    0.05391800   -1.72457900
O       4.61576100    0.16136100    0.24542400
C      -1.29454300   -1.50296500   -0.85526400
C       0.11585900   -1.03039800   -1.13504200
C      -2.29922700   -0.43603200   -1.24648900
C       2.39916200   -0.36290500   -0.44463300
C       1.05775900   -0.84472800   -0.19827900
C      -1.58514800   -2.79845600   -1.55625900
C       3.37037200   -0.31208100    0.48551900
C      -3.15337400    0.15070400   -0.41445700
H      -1.38636500   -1.65745300    0.23329900
H      -2.29692400   -0.15965900   -2.29962500
H       0.35527700   -0.86234100   -2.18302100
H       0.82181000   -1.05079500    0.84317900
H       3.22948300   -0.67020300    1.49584100
H      -2.60352600   -3.07035100   -1.80690200
H      -0.79712200   -3.52604500   -1.70826400
H      -3.85154700    0.90652900   -0.75625700
H      -3.18559800   -0.10280600    0.64099900
H       2.05212200    0.61341500   -2.06969400
H       4.63228500    0.44244300   -0.68127200
""",
)

entry(
    index = 185,
    label = "P236",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {6,D} {13,S}
3  C u0 p0 c0 {5,S} {7,D} {9,S}
4  C u0 p0 c0 {1,S} {8,D} {14,S}
5  C u1 p0 c0 {3,S} {6,S} {16,S}
6  C u0 p0 c0 {2,D} {5,S} {15,S}
7  C u0 p0 c0 {3,D} {10,S} {17,S}
8  C u0 p0 c0 {4,D} {18,S} {19,S}
9  O u0 p2 c0 {3,S} {20,S}
10 O u0 p2 c0 {7,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.99719,0.0942828,-0.000138613,1.88545e-07,-1.1794e-10,-15304.8,15.1622], Tmin=(10,'K'), Tmax=(465.211,'K')),
            NASAPolynomial(coeffs=[4.27946,0.0742921,-4.52489e-05,1.33244e-08,-1.51623e-12,-15327.1,10.9999], Tmin=(465.211,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-127.292,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (498.868,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 9, 'H-O': 2, 'C-C': 4, 'C-O': 2, 'C=C': 3}
1D rotors:
* Invalidated! pivots: [1, 5], dihedral: [20, 1, 5, 7], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 9], dihedral: [21, 2, 9, 5], invalidation reason: Another conformer for C8H11O2[139] exists which is 5.40 kJ/mol lower.Another conformer for C8H11O2[139] exists which is 5.40 kJ/mol lower.
pivots: [3, 4], dihedral: [6, 3, 4, 8], rotor symmetry: 1, max scan energy: 11.91 kJ/mol
pivots: [3, 6], dihedral: [4, 3, 6, 10], rotor symmetry: 1, max scan energy: 13.10 kJ/mol
* Invalidated! pivots: [5, 7], dihedral: [1, 5, 7, 8], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [7, 8], dihedral: [5, 7, 8, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [5, 9], dihedral: [1, 5, 9, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 8], dihedral: [3, 4, 8, 7], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       3.12669200   -1.06527500   -0.48662100
O       4.47389000    1.23017500   -0.67792500
C      -0.72301500   -2.90801400    2.64724200
C      -0.02672800   -1.59961700    2.39370400
C       2.75667500   -0.04537700    0.38934800
C      -0.59073300   -3.35893600    4.08315500
C       1.71819100   -0.22206600    1.31877300
C       1.02642800   -1.43354600    1.54181900
C       3.51254000    1.09351700    0.26181000
C      -1.60353200   -3.51821900    4.92979400
H      -1.78989300   -2.82327600    2.40243100
H      -0.30324400   -3.67450300    1.98402800
H      -0.38907200   -0.74407400    2.95984500
H       0.42676700   -3.53950000    4.42447700
H       1.37363400   -2.31491300    1.00268400
H       1.44236800    0.64863800    1.90534000
H       3.40314300    1.94851500    0.91267800
H      -2.63132700   -3.34009300    4.62684900
H      -1.44468900   -3.83491400    5.95451200
H       2.33117700   -1.50822600   -0.79992900
H       4.48090100    0.40790700   -1.19094500
""",
)

entry(
    index = 186,
    label = "P237",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {12,S}
3  C u0 p0 c0 {1,S} {2,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {6,D} {15,S}
5  C u0 p0 c0 {6,S} {8,D} {9,S}
6  C u0 p0 c0 {4,D} {5,S} {16,S}
7  C u1 p0 c0 {2,S} {18,S} {19,S}
8  C u0 p0 c0 {5,D} {10,S} {17,S}
9  O u0 p2 c0 {5,S} {20,S}
10 O u0 p2 c0 {8,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.33912,0.0599509,5.1187e-05,-1.45545e-07,8.06586e-11,-3997.87,15.0752], Tmin=(10,'K'), Tmax=(674.125,'K')),
            NASAPolynomial(coeffs=[5.44707,0.0757606,-4.70007e-05,1.3869e-08,-1.56874e-12,-4925.51,0.964429], Tmin=(674.125,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-33.3163,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (498.868,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 9, 'H-O': 2, 'C-C': 6, 'C-O': 2, 'C=C': 2}
1D rotors:
* Invalidated! pivots: [1, 7], dihedral: [20, 1, 7, 8], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [2, 10], dihedral: [21, 2, 10, 7], rotor symmetry: 1, max scan energy: 34.71 kJ/mol
* Invalidated! pivots: [3, 6], dihedral: [4, 3, 6, 8], invalidation reason: Another conformer for C8H11O2[140] exists which is 5.02 kJ/mol lower.Another conformer for C8H11O2[140] exists which is 5.02 kJ/mol lower.
pivots: [4, 9], dihedral: [3, 4, 9, 18], rotor symmetry: 2, max scan energy: 17.24 kJ/mol
* Invalidated! pivots: [7, 8], dihedral: [1, 7, 8, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       2.83217400    0.69591600   -0.17271700
O       2.96774700    0.03098600    2.44812900
C       0.78800300   -1.92975200   -3.01054100
C      -0.03443500   -1.20106300   -4.17281400
C       1.19988900   -2.02317200   -4.44892600
C       1.52287400   -1.10991200   -2.04726500
C       2.21160800   -0.48039600    0.24866500
C       1.52553800   -1.30869600   -0.71394400
C      -1.36117000   -1.65820600   -4.50392700
C       2.33769000   -0.77215600    1.55758500
H       0.27178100   -2.79160800   -2.60194300
H       0.11160000   -0.12607200   -4.16019800
H       2.09795400   -1.49376800   -4.74856900
H       1.05596400   -2.97292000   -4.95208600
H       2.11094600   -0.29241800   -2.46060300
H       0.97246100   -2.14782800   -0.29953000
H       1.95929900   -1.68764000    1.99050000
H      -2.20377200   -0.98038700   -4.47560200
H      -1.55883900   -2.70988700   -4.67465200
H       2.21506200    1.17686400   -0.73678700
H       3.27507900    0.80485300    1.95350000
""",
)

entry(
    index = 187,
    label = "P238",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {12,S}
3  C u0 p0 c0 {5,S} {6,S} {7,S} {13,S}
4  C u0 p0 c0 {1,S} {2,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
6  C u1 p0 c0 {2,S} {3,S} {18,S}
7  C u0 p0 c0 {3,S} {8,D} {9,S}
8  C u0 p0 c0 {7,D} {10,S} {19,S}
9  O u0 p2 c0 {7,S} {20,S}
10 O u0 p2 c0 {8,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79208,0.0127766,0.000288204,-5.84976e-07,3.62911e-10,-10349.2,15.4206], Tmin=(10,'K'), Tmax=(522.353,'K')),
            NASAPolynomial(coeffs=[-0.73098,0.0908013,-6.04492e-05,1.90195e-08,-2.26989e-12,-10468.6,28.6383], Tmin=(522.353,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-86.1173,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (503.026,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 9, 'H-O': 2, 'C-C': 8, 'C-O': 2, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [1, 9], dihedral: [20, 1, 9, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [2, 10], dihedral: [21, 2, 10, 9], rotor symmetry: 1, max scan energy: 27.13 kJ/mol
* Invalidated! pivots: [5, 9], dihedral: [7, 5, 9, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       1.68312900   -1.22017700    0.03055100
O       0.31293100    0.45657400    1.70355000
C       4.26294400    0.01043300   -2.90648900
C       2.99648800   -0.36017200   -3.67528400
C       2.29673200    0.59405600   -1.52613800
C       3.82569800    0.89407100   -4.03064800
C       3.84886700    0.38842600   -1.49022400
C       1.86978700   -0.15942800   -2.76793900
C       1.59760300    0.13520300   -0.27953700
C       0.93974200    0.91510700    0.58135000
H       5.16505300   -0.57541700   -3.04050100
H       2.98018000   -1.15673200   -4.41006000
H       2.06810600    1.66428000   -1.64212100
H       3.39714100    1.86616400   -3.81364800
H       4.38625500    0.84490100   -4.95707800
H       4.08219600   -0.43739300   -0.81311100
H       4.36075300    1.27827200   -1.11463200
H       0.83002100   -0.29060800   -3.04505600
H       0.86928200    1.98678900    0.45842200
H       1.67327700   -1.71160200   -0.80111100
H       0.42849200   -0.50333100    1.71332600
""",
)

entry(
    index = 188,
    label = "P239",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {6,S} {12,S}
2  C u0 p0 c0 {3,S} {5,S} {7,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {8,D} {9,S}
5  C u0 p0 c0 {2,S} {6,D} {15,S}
6  C u0 p0 c0 {1,S} {5,D} {16,S}
7  C u1 p0 c0 {2,S} {18,S} {19,S}
8  C u0 p0 c0 {4,D} {10,S} {17,S}
9  O u0 p2 c0 {4,S} {20,S}
10 O u0 p2 c0 {8,S} {21,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.5376,0.0448059,0.000102407,-2.08873e-07,1.08192e-10,-11454.8,14.524], Tmin=(10,'K'), Tmax=(677.522,'K')),
            NASAPolynomial(coeffs=[3.51012,0.079083,-4.90093e-05,1.44367e-08,-1.62987e-12,-12234.1,8.86747], Tmin=(677.522,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-95.2905,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (503.026,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 9, 'H-O': 2, 'C-C': 6, 'C-O': 2, 'C=C': 2}
1D rotors:
* Invalidated! pivots: [1, 6], dihedral: [20, 1, 6, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [2, 10], dihedral: [21, 2, 10, 6], rotor symmetry: 1, max scan energy: 28.04 kJ/mol
* Invalidated! pivots: [3, 6], dihedral: [5, 3, 6, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 9], dihedral: [5, 4, 9, 18], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       1.38696400   -1.18581400    0.34185900
O       3.50230300   -1.01457300   -1.38120400
C       0.28072900    0.82526900   -0.59046700
C      -1.87731300    0.08821900    0.46888400
C      -1.11265900    0.17885000   -0.88773800
C       1.42959000   -0.14509300   -0.58488900
C      -1.06356600    1.02556600    1.36045000
C       0.06921400    1.43109600    0.78773400
C      -1.95191400   -1.28906700    1.04799600
C       2.47259200   -0.12105100   -1.41853500
H      -2.89565000    0.48149700    0.36475700
H       0.51510800    1.59887300   -1.32829600
H      -1.66633700    0.82555400   -1.57167200
H      -1.01318700   -0.79592800   -1.36605100
H      -1.39530800    1.29646200    2.35659700
H       0.80655800    2.08015000    1.24803200
H       2.56718600    0.60840200   -2.21079000
H      -1.14269400   -1.99002000    0.87985000
H      -2.74044700   -1.56525200    1.73760800
H       1.00104000   -0.84627700    1.15994600
H       3.32443900   -1.61196000   -0.64183400
""",
)

entry(
    index = 189,
    label = "P240",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {6,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {7,D} {18,S}
5  C u0 p0 c0 {2,S} {6,D} {16,S}
6  C u0 p0 c0 {3,S} {5,D} {17,S}
7  C u0 p0 c0 {4,D} {8,S} {9,S}
8  C u1 p0 c0 {7,S} {10,S} {19,S}
9  O u0 p2 c0 {7,S} {20,S}
10 O u0 p2 c0 {8,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68647,0.0397638,9.77498e-05,-1.72632e-07,7.85865e-11,-19625.1,13.0369], Tmin=(10,'K'), Tmax=(773.002,'K')),
            NASAPolynomial(coeffs=[3.58483,0.0771253,-4.62286e-05,1.31866e-08,-1.44713e-12,-20709.9,6.3826], Tmin=(773.002,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-163.152,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (503.026,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 9, 'H-O': 2, 'C-C': 6, 'C-O': 2, 'C=C': 2}
1D rotors:
* Invalidated! pivots: [1, 9], dihedral: [20, 1, 9, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [2, 10], dihedral: [21, 2, 10, 9], rotor symmetry: 2, max scan energy: 37.54 kJ/mol
* Invalidated! pivots: [3, 6], dihedral: [4, 3, 6, 9], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [9, 10], dihedral: [1, 9, 10, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [6, 9], dihedral: [3, 6, 9, 1], invalidation reason: Another conformer for C8H11O2[143] exists which is 6.48 kJ/mol lower.Another conformer for C8H11O2[143] exists which is 6.48 kJ/mol lower.


External symmetry: 1, optical isomers: 1

Geometry:
O       2.27649700    0.13894300    1.22242800
O       2.41151700   -2.07921100   -0.18237900
C       1.51973800    2.83148500   -0.04078400
C       0.45990600    2.87685600    1.12035800
C       2.84734100    3.32416300    0.64353400
C       1.63726400    1.48772900   -0.71290900
C       1.29108800    2.93259700    2.37789200
C       2.57997000    3.17408000    2.12047400
C       1.98052700    0.28691000   -0.12068100
C       2.07053700   -0.92607200   -0.80790200
H       1.23174400    3.54554000   -0.81290400
H      -0.17011500    3.77148500    1.04281500
H      -0.21500200    2.01675400    1.09030800
H       3.71673000    2.75339700    0.30505400
H       3.04880100    4.37457600    0.39992600
H       0.86735800    2.81892000    3.36971400
H       3.35274500    3.28457800    2.87332700
H       1.43315000    1.44338200   -1.77651100
H       1.87819200   -1.02606300   -1.86477800
H       2.21323100    0.98163900    1.69618200
H       2.55640300   -1.85893600    0.74970200
""",
)

entry(
    index = 190,
    label = "P241",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {6,S} {12,S}
2  C u0 p0 c0 {3,S} {5,S} {8,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {7,S} {9,S} {15,S}
5  C u0 p0 c0 {2,S} {6,S} {16,S} {17,S}
6  C u1 p0 c0 {1,S} {5,S} {18,S}
7  C u0 p0 c0 {4,S} {8,D} {10,S}
8  C u0 p0 c0 {2,S} {7,D} {19,S}
9  O u0 p2 c0 {4,S} {20,S}
10 O u0 p2 c0 {7,S} {21,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83406,0.00960842,0.000260811,-4.76669e-07,2.67298e-10,-21812.5,13.3387], Tmin=(10,'K'), Tmax=(567.008,'K')),
            NASAPolynomial(coeffs=[-3.16806,0.0958392,-6.47519e-05,2.06853e-08,-2.50542e-12,-21610.5,37.9257], Tmin=(567.008,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-181.431,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (503.026,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 9, 'H-O': 2, 'C-C': 8, 'C-O': 2, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [1, 6], dihedral: [20, 1, 6, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [2, 9], dihedral: [21, 2, 9, 6], rotor symmetry: 1, max scan energy: 34.03 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.43629100    2.17144800    0.05310900
O       2.61670300    2.08498700   -2.43159600
C       1.06989800   -0.29577600    0.03677900
C       2.56737800   -1.50955000   -1.34222700
C       1.06764900   -1.46343500   -0.97919100
C       1.20968300    1.01822300   -0.77108300
C       3.22661300   -1.50244900    0.06991300
C       2.30950800   -0.59379100    0.83893000
C       2.31440500    0.90847400   -1.80574500
C       2.93120500   -0.24232700   -2.09130800
H       2.84006200   -2.39446600   -1.92045600
H       0.16750800   -0.22840500    0.65086700
H       0.42891300   -1.28132800   -1.84647800
H       0.74424800   -2.39013600   -0.49598000
H       0.26268200    1.24072400   -1.27661500
H       3.24145500   -2.51656700    0.50151000
H       4.26583800   -1.15615500    0.04911900
H       2.45640100   -0.30828700    1.87320700
H       3.72836400   -0.25632200   -2.82664000
H       2.20397500    1.97018600    0.60487400
H       2.27902100    2.79018300   -1.86113500
""",
)

entry(
    index = 191,
    label = "P242",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {11,S}
2  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
3  C u0 p0 c0 {4,S} {9,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {5,D} {10,S}
5  C u0 p0 c0 {1,S} {4,D} {18,S}
6  C u1 p0 c0 {1,S} {8,S} {16,S}
7  C u0 p0 c0 {2,S} {8,D} {17,S}
8  C u0 p0 c0 {6,S} {7,D} {19,S}
9  O u0 p2 c0 {3,S} {20,S}
10 O u0 p2 c0 {4,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.56563,0.0473088,6.07678e-05,-1.18926e-07,5.33755e-11,-17103.9,15.6329], Tmin=(10,'K'), Tmax=(803.736,'K')),
            NASAPolynomial(coeffs=[4.01679,0.0740136,-4.31e-05,1.20434e-08,-1.30165e-12,-18111.5,7.73784], Tmin=(803.736,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-142.208,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (507.183,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 9, 'H-O': 2, 'C-C': 6, 'C-O': 2, 'C=C': 2}
1D rotors:
* Invalidated! pivots: [1, 5], dihedral: [20, 1, 5, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 6], dihedral: [21, 2, 6, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 7], dihedral: [4, 3, 7, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [5, 6], dihedral: [1, 5, 6, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O      -3.57383900    1.08627900   -0.87201700
O      -3.12747300   -1.31472400    0.25434400
C       0.17824000    0.22319400    1.26646900
C       1.50193600   -0.55941600    0.93809300
C      -2.20883300    0.64618300   -0.77289500
C      -2.07935200   -0.43119000    0.27708700
C      -1.06979200   -0.60970000    1.13563900
C       0.42115800    0.71666100    2.68040300
C       2.38398500   -0.32862200    2.13560600
C       1.69693300    0.38368100    3.10756600
H       0.11001600    1.08995700    0.59725900
H       1.95840100   -0.21248400    0.00385600
H       1.29380200   -1.62724500    0.79448400
H      -1.53301000    1.48348100   -0.58776100
H      -1.98096200    0.23437600   -1.76020700
H      -0.31995000    1.26357500    3.24823900
H       3.39652000   -0.70030300    2.22144800
H      -1.14510700   -1.46513300    1.80262300
H       2.10594700    0.64707700    4.07610000
H      -3.78044400    1.58482800   -0.07335900
H      -3.84038900   -0.87928000   -0.23544000
""",
)

entry(
    index = 191,
    label = "P243",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {11,S}
3  C u0 p0 c0 {4,S} {6,S} {8,S} {12,S}
4  C u0 p0 c0 {2,S} {3,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {10,S} {15,S} {16,S}
6  C u1 p0 c0 {1,S} {3,S} {17,S}
7  C u0 p0 c0 {2,S} {8,D} {19,S}
8  C u0 p0 c0 {3,S} {7,D} {18,S}
9  O u0 p2 c0 {1,S} {21,S}
10 O u0 p2 c0 {5,S} {20,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81197,0.0107861,0.000265154,-4.87625e-07,2.72338e-10,-14742.8,13.5689], Tmin=(10,'K'), Tmax=(579.652,'K')),
            NASAPolynomial(coeffs=[-2.16396,0.0952589,-6.53223e-05,2.11378e-08,-2.58512e-12,-14776.4,32.8752], Tmin=(579.652,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-122.662,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (503.026,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 9, 'H-O': 2, 'C-C': 8, 'C-O': 2, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [1, 3], dihedral: [21, 1, 3, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [2, 7], dihedral: [20, 2, 7, 3], rotor symmetry: 1, max scan energy: 24.75 kJ/mol
* Invalidated! pivots: [3, 7], dihedral: [1, 3, 7, 2], invalidation reason: Inconsistent initial and final conformers But unable to propose troubleshooting methods.Inconsistent initial and final conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.62941400   -0.36533700    2.82316000
O      -1.99862300   -1.91473000    0.70600400
C      -1.50701700    0.07324000    2.03123400
C      -0.11819600   -0.42111300    2.60490100
C       0.07400400    1.83340200    2.61968900
C       0.83886600    0.63249700    1.99677000
C      -1.81865200   -0.50945500    0.64432500
C      -1.31005200    1.56667900    2.06615900
C      -0.09399500    0.01887900    4.06548800
C       0.00001600    1.35542000    4.08153600
H       0.07389900   -1.47155700    2.39958600
H       0.47439000    2.83379800    2.46362300
H       0.85125300    0.65059700    0.90472800
H       1.85869200    0.53918300    2.37546900
H      -2.71704100   -0.00908500    0.25749400
H      -0.99800500   -0.32209400   -0.04887300
H      -2.12411400    2.27921800    2.02597900
H      -0.05591300    2.01444400    4.93892800
H      -0.22066100   -0.63865800    4.91596300
H      -2.62535900   -2.06330700    1.42496800
H      -2.49992700   -0.02906900    3.71687600
""",
)

entry(
    index = 192,
    label = "P244",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {6,S} {11,S} {14,S}
3  C u0 p0 c0 {5,S} {9,S} {15,S} {16,S}
4  C u0 p0 c0 {1,S} {7,S} {8,D}
5  C u0 p0 c0 {3,S} {7,D} {10,S}
6  C u1 p0 c0 {2,S} {8,S} {17,S}
7  C u0 p0 c0 {4,S} {5,D} {19,S}
8  C u0 p0 c0 {4,D} {6,S} {18,S}
9  O u0 p2 c0 {3,S} {20,S}
10 O u0 p2 c0 {5,S} {21,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74363,0.0490804,4.66247e-05,-8.93002e-08,3.59232e-11,-24587.7,14.1134], Tmin=(10,'K'), Tmax=(941.651,'K')),
            NASAPolynomial(coeffs=[8.06305,0.0661705,-3.70506e-05,9.9063e-09,-1.02593e-12,-26972.4,-14.8083], Tmin=(941.651,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-204.326,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (498.868,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 9, 'H-O': 2, 'C-C': 6, 'C-O': 2, 'C=C': 2}
1D rotors:
* Invalidated! pivots: [1, 5], dihedral: [20, 1, 5, 7], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [2, 7], dihedral: [21, 2, 7, 5], rotor symmetry: 1, max scan energy: 34.64 kJ/mol
* Invalidated! pivots: [5, 7], dihedral: [1, 5, 7, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [6, 9], dihedral: [3, 6, 9, 7], rotor symmetry: 1, max scan energy: 51.46 kJ/mol
* Invalidated! pivots: [7, 9], dihedral: [2, 7, 9, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O      -4.16147600    0.00442100    0.69871200
O      -2.38652300   -2.01166800    0.25003400
C      -0.84907100   -3.44837600   -1.82562200
C      -0.04478800   -4.21821100   -2.91239700
C      -2.93610500    0.31589100    0.01071800
C      -1.03191700   -2.05156500   -2.39387800
C      -2.32873400   -0.92419900   -0.57606700
C       0.16030200   -3.20011600   -4.00451900
C      -1.69805500   -0.96833700   -1.79052300
C      -0.40690600   -2.00708300   -3.67043900
H      -0.58740100   -5.09869000   -3.27773200
H      -0.32264400   -3.41765600   -0.86767000
H      -1.81471300   -3.91747200   -1.61728500
H       0.91085500   -4.59318200   -2.52602800
H      -2.29204400    0.73085800    0.79436100
H      -3.07807900    1.08356700   -0.75607400
H       0.69161800   -3.40783900   -4.92458900
H      -0.39059100   -1.11965300   -4.29385400
H      -1.71392600   -0.03647900   -2.34981500
H      -4.81060800   -0.25334300    0.03368200
H      -3.05017000   -1.80300300    0.92470300
""",
)

entry(
    index = 193,
    label = "P245",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {13,S}
3  C u0 p0 c0 {1,S} {2,S} {6,S} {12,S}
4  C u0 p0 c0 {1,S} {5,S} {14,S} {15,S}
5  C u0 p0 c0 {4,S} {6,S} {16,S} {17,S}
6  C u1 p0 c0 {3,S} {5,S} {18,S}
7  C u0 p0 c0 {2,S} {8,D} {9,S}
8  C u0 p0 c0 {7,D} {10,S} {19,S}
9  O u0 p2 c0 {7,S} {20,S}
10 O u0 p2 c0 {8,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7953,0.0132143,0.000299987,-6.41747e-07,4.24121e-10,-10601.3,15.4137], Tmin=(10,'K'), Tmax=(483.382,'K')),
            NASAPolynomial(coeffs=[-0.975951,0.0909794,-6.01259e-05,1.87511e-08,-2.21887e-12,-10587.3,30.3375], Tmin=(483.382,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-88.1922,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (503.026,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 9, 'H-O': 2, 'C-C': 8, 'C-O': 2, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [1, 9], dihedral: [20, 1, 9, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [2, 10], dihedral: [21, 2, 10, 9], rotor symmetry: 1, max scan energy: 29.87 kJ/mol
* Invalidated! pivots: [4, 9], dihedral: [3, 4, 9, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.36769900    1.55284400    1.15712400
O      -2.69190000   -0.64594600    2.05643300
C       0.30568800   -0.45811900   -1.45152800
C      -0.76088200    0.49072800   -0.97624600
C       0.71183300    0.97757500   -1.11970500
C       1.00205100   -1.37636400   -0.44945700
C       1.58621700   -0.45418800    0.66082100
C       1.56676800    0.92463400    0.06550800
C      -1.40529200    0.41236700    0.35565500
C      -2.09075400   -0.63155900    0.83253200
H       0.25880300   -0.77786400   -2.48620800
H       0.89058800    1.71731100   -1.89099100
H      -1.38911500    0.89255200   -1.76876500
H       0.33491900   -2.13670700   -0.03750200
H       1.81161700   -1.89751300   -0.96849200
H       0.97135100   -0.51166700    1.56970300
H       2.59534400   -0.76127900    0.95825300
H       2.21499900    1.73330200    0.37627100
H      -2.23999600   -1.54062200    0.26757400
H      -0.49093300    1.94626100    1.05526800
H      -2.50369500    0.21104100    2.46416200
""",
)

entry(
    index = 194,
    label = "P246",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {4,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {5,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {5,D} {7,S}
5  C u0 p0 c0 {3,S} {4,D} {17,S}
6  C u0 p0 c0 {7,S} {8,D} {9,S}
7  C u1 p0 c0 {4,S} {6,S} {18,S}
8  C u0 p0 c0 {6,D} {10,S} {19,S}
9  O u0 p2 c0 {6,S} {21,S}
10 O u0 p2 c0 {8,S} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68017,0.0405573,9.31117e-05,-1.64941e-07,7.45644e-11,-24259.8,14.0325], Tmin=(10,'K'), Tmax=(780.855,'K')),
            NASAPolynomial(coeffs=[3.71011,0.0766208,-4.5737e-05,1.30012e-08,-1.42273e-12,-25368.7,6.82542], Tmin=(780.855,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-201.685,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (503.026,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 9, 'H-O': 2, 'C-C': 6, 'C-O': 2, 'C=C': 2}
1D rotors:
* Invalidated! pivots: [1, 8], dihedral: [21, 1, 8, 9], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [2, 10], dihedral: [20, 2, 10, 8], rotor symmetry: 1, max scan energy: 37.92 kJ/mol
* Invalidated! pivots: [6, 9], dihedral: [4, 6, 9, 8], invalidation reason: Another conformer for C8H11O2[155] exists which is 2.41 kJ/mol lower.Another conformer for C8H11O2[155] exists which is 2.41 kJ/mol lower.
* Invalidated! pivots: [8, 9], dihedral: [1, 8, 9, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [8, 10], dihedral: [1, 8, 10, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       1.23289600    1.18118600   -1.17978600
O       3.82270000    1.56039200   -1.66703000
C      -1.53157200   -1.83011000    1.92106100
C      -0.00223200   -1.67361300    2.05511600
C      -2.02810200   -0.44248700    1.45298100
C       0.33652400   -0.53047400    1.10157100
C      -0.81201100    0.15032200    0.79067600
C       2.12129400    0.55150700   -0.32259900
C       1.68120800   -0.28164600    0.71728700
C       3.44248600    0.80388500   -0.61321100
H      -1.75358300   -2.57254400    1.14900500
H      -2.00841100   -2.16455100    2.84466800
H       0.53935900   -2.59334500    1.81836000
H       0.28110200   -1.38972600    3.07696400
H      -2.89501900   -0.50828400    0.78668400
H      -2.34457700    0.17833000    2.30447700
H      -0.85336400    1.09232900    0.25735800
H       2.46020800   -0.82487200    1.24198100
H       4.25966300    0.43089300   -0.01410300
H       3.01413200    1.82564700   -2.13041500
H       0.41728200    0.66474600   -1.20521400
""",
)

entry(
    index = 195,
    label = "P247",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {5,S} {16,S} {17,S}
5  C u0 p0 c0 {3,S} {4,S} {6,D}
6  C u0 p0 c0 {5,D} {7,S} {19,S}
7  C u0 p0 c0 {6,S} {8,D} {18,S}
8  C u0 p0 c0 {7,D} {9,S} {20,S}
9  O u0 p2 c0 {8,S} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 O u1 p2 c0 {7,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7741,0.0364587,9.50751e-05,-1.53381e-07,6.46447e-11,-28262.5,13.9525], Tmin=(10,'K'), Tmax=(831.518,'K')),
            NASAPolynomial(coeffs=[3.0446,0.0770266,-4.49579e-05,1.24878e-08,-1.33894e-12,-29422.4,9.63353], Tmin=(831.518,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-234.925,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (498.868,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 10, 'H-O': 1, 'C-C': 6, 'C-O': 2, 'C=C': 2}
1D rotors:
pivots: [1, 10], dihedral: [21, 1, 10, 9], rotor symmetry: 1, max scan energy: 73.27 kJ/mol
pivots: [8, 9], dihedral: [7, 8, 9, 2], rotor symmetry: 1, max scan energy: 34.24 kJ/mol
* Invalidated! pivots: [9, 10], dihedral: [2, 9, 10, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       3.12942600   -2.99565300    2.33517200
O       2.14923100   -0.73588800    1.55060100
C      -1.33381900    0.80572000   -1.87462100
C      -0.23446800    1.72032900   -1.30682800
C      -0.64322900   -0.56894700   -1.94689700
C       0.48353200    0.83809500   -0.26472000
C       0.30188100   -0.58225000   -0.76038400
C       0.85641100   -1.69666400   -0.24933900
C       1.77361400   -1.73295800    0.88713900
C       2.30121600   -3.00327100    1.29985200
H      -1.71978800    1.13982700   -2.83999300
H      -2.17852400    0.76080200   -1.17865500
H       0.46243000    1.99803300   -2.10518500
H      -0.62477900    2.64643000   -0.87998900
H      -1.33320200   -1.41620200   -1.94609600
H      -0.05426300   -0.63674200   -2.87167800
H       0.01473300    0.93123700    0.72210100
H       1.53385500    1.08605400   -0.10682900
H       0.61816100   -2.65675800   -0.70147500
H       2.09752900   -3.96917000    0.85880700
H       3.17489100   -2.04002600    2.57747900
""",
)

entry(
    index = 196,
    label = "P248",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {5,S} {11,S} {14,S}
3  C u0 p0 c0 {4,S} {5,S} {15,S} {16,S}
4  C u0 p0 c0 {1,S} {3,S} {7,D}
5  C u1 p0 c0 {2,S} {3,S} {17,S}
6  C u0 p0 c0 {7,S} {8,D} {9,S}
7  C u0 p0 c0 {4,D} {6,S} {18,S}
8  C u0 p0 c0 {6,D} {10,S} {19,S}
9  O u0 p2 c0 {6,S} {21,S}
10 O u0 p2 c0 {8,S} {20,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.60175,0.0494801,5.93146e-05,-1.18231e-07,5.24377e-11,-13169.3,14.2894], Tmin=(10,'K'), Tmax=(830.974,'K')),
            NASAPolynomial(coeffs=[5.77974,0.0724429,-4.25112e-05,1.18985e-08,-1.28451e-12,-14686,-2.76327], Tmin=(830.974,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-109.463,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (503.026,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 9, 'H-O': 2, 'C-C': 6, 'C-O': 2, 'C=C': 2}
1D rotors:
* Invalidated! pivots: [1, 8], dihedral: [21, 1, 8, 9], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [2, 10], dihedral: [20, 2, 10, 8], rotor symmetry: 1, max scan energy: 33.56 kJ/mol
* Invalidated! pivots: [8, 9], dihedral: [1, 8, 9, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       2.02197300    0.85525800    1.55879200
O       4.29029300   -0.21862200    0.57289400
C      -0.68630200    2.06538500    0.84378000
C      -1.66586500    3.11888400    0.26791500
C      -1.47091600    1.24432600   -1.33709500
C      -0.30631500    1.21190300   -0.35520100
C      -2.26493200    2.44321200   -0.92399200
C       2.02834900    0.44157700    0.22372600
C       0.85105200    0.57918100   -0.61040400
C       3.19755300   -0.06144900   -0.21471500
H      -2.41138500    3.44752800    1.00089200
H      -1.22242500    1.45702500    1.58631600
H       0.17568200    2.51157800    1.33842800
H      -1.10934000    4.02452000   -0.02516300
H      -2.07214600    0.32043400   -1.26919800
H      -1.12594400    1.28897300   -2.38000100
H      -3.12252300    2.81689500   -1.46815600
H       0.94242500    0.07630700   -1.57110700
H       3.35686000   -0.35996100   -1.24131500
H       4.03855100    0.08478700    1.45738100
H       1.20449700    0.55307700    1.96853500
""",
)

entry(
    index = 197,
    label = "P249",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {7,S} {9,S} {13,S}
3  C u0 p0 c0 {1,S} {5,S} {12,S} {14,S}
4  C u0 p0 c0 {1,S} {6,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {6,S} {17,S} {18,S}
6  C u1 p0 c0 {4,S} {5,S} {8,S}
7  C u0 p0 c0 {2,S} {8,D} {10,S}
8  C u0 p0 c0 {6,S} {7,D} {19,S}
9  O u0 p2 c0 {2,S} {20,S}
10 O u0 p2 c0 {7,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85793,0.00836806,0.000254464,-4.65606e-07,2.64897e-10,-18646.8,13.543], Tmin=(10,'K'), Tmax=(546.899,'K')),
            NASAPolynomial(coeffs=[-3.75581,0.0938436,-6.16761e-05,1.9362e-08,-2.32042e-12,-18259.6,41.6072], Tmin=(546.899,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-155.096,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (507.183,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 9, 'H-O': 2, 'C-C': 8, 'C-O': 2, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [1, 4], dihedral: [20, 1, 4, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 9], dihedral: [21, 2, 9, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       2.00796900   -0.90226700   -1.15905400
O       0.00405600    0.94754400   -0.98635700
C       1.49538300   -1.78531900    1.13177800
C       1.50061900   -0.59560600    0.15102700
C       0.61261200   -2.99788600    0.67906300
C       0.74751500   -1.28183400    2.39519800
C      -0.79371900   -2.79024500    1.36372600
C      -0.65230200   -1.35368800    1.82816300
C       0.12050500    0.03320300    0.01614100
C      -0.91149400   -0.33826600    0.79604900
H       2.52933100   -2.08861400    1.31461100
H       0.50898300   -3.05739500   -0.40874500
H       2.20580600    0.15759800    0.52083800
H       1.07239900   -3.93689900    0.99485000
H       1.04849100   -0.27952900    2.70467500
H       0.89073700   -1.96855800    3.23538000
H      -0.91596100   -3.48579100    2.19981800
H      -1.62004900   -2.94245700    0.66836400
H      -1.91417400    0.01670300    0.57695700
H       1.49442100   -1.64048800   -1.50825100
H       0.76041400    0.80610000   -1.57466100
""",
)

entry(
    index = 198,
    label = "P250",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {12,S} {13,S}
2  C u0 p0 c0 {5,S} {7,S} {11,S} {14,S}
3  C u0 p0 c0 {6,S} {9,S} {15,S} {16,S}
4  C u0 p0 c0 {1,S} {7,D} {8,S}
5  C u1 p0 c0 {1,S} {2,S} {17,S}
6  C u0 p0 c0 {3,S} {8,D} {10,S}
7  C u0 p0 c0 {2,S} {4,D} {18,S}
8  C u0 p0 c0 {4,S} {6,D} {19,S}
9  O u0 p2 c0 {3,S} {20,S}
10 O u0 p2 c0 {6,S} {21,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.59702,0.0512591,5.14243e-05,-1.07429e-07,4.74108e-11,-14361.9,14.4239], Tmin=(10,'K'), Tmax=(848.082,'K')),
            NASAPolynomial(coeffs=[6.56059,0.070448,-4.11766e-05,1.14766e-08,-1.23396e-12,-16057.3,-6.41728], Tmin=(848.082,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-119.372,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (498.868,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 9, 'H-O': 2, 'C-C': 6, 'C-O': 2, 'C=C': 2}
1D rotors:
* Invalidated! pivots: [1, 5], dihedral: [20, 1, 5, 8], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [2, 8], dihedral: [21, 2, 8, 5], rotor symmetry: 1, max scan energy: 34.65 kJ/mol
* Invalidated! pivots: [5, 8], dihedral: [1, 5, 8, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [6, 10], dihedral: [3, 6, 10, 8], rotor symmetry: 1, max scan energy: 25.03 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -4.22629700    0.06195600    0.64321500
O      -2.40539600    2.05062600    0.40368300
C      -0.72534900    3.54706200   -1.49421600
C       0.53246000    3.44771900   -3.61875700
C      -2.96006100   -0.25573000    0.04389300
C      -0.83343200    2.17260800   -2.14186300
C       0.13443200    4.30557800   -2.45632100
C      -2.28118100    0.99453700   -0.45286300
C      -0.14198100    2.13766200   -3.29653400
C      -1.57782700    1.05180800   -1.59731100
H       1.62632500    3.33852800   -3.71756900
H      -1.71622700    4.00058400   -1.34397300
H      -0.29571500    3.48287300   -0.48355800
H       0.20215200    3.85791100   -4.58872700
H      -2.37973200   -0.70270400    0.85707900
H      -3.05719900   -0.99449600   -0.75663100
H       0.43260800    5.33749600   -2.32675000
H      -0.06643900    1.26616800   -3.93773600
H      -1.55380700    0.13627100   -2.18081100
H      -4.82659600    0.32935500   -0.06225900
H      -3.13096400    1.82661600    1.00582300
""",
)

entry(
    index = 199,
    label = "P251",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {6,S} {14,S} {15,S}
4  C u0 p0 c0 {7,S} {9,S} {16,S} {17,S}
5  C u0 p0 c0 {2,S} {6,D} {8,S}
6  C u0 p0 c0 {3,S} {5,D} {19,S}
7  C u0 p0 c0 {4,S} {8,D} {18,S}
8  C u0 p0 c0 {5,S} {7,D} {20,S}
9  O u0 p2 c0 {4,S} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 O u1 p2 c0 {7,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94825,0.0508606,2.96591e-05,-5.98528e-08,2.17515e-11,-27768.2,13.2644], Tmin=(10,'K'), Tmax=(1096.51,'K')),
            NASAPolynomial(coeffs=[13.1887,0.0550982,-2.80473e-05,6.79228e-09,-6.38953e-13,-32075.9,-42.569], Tmin=(1096.51,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-230.697,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (494.711,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 10, 'H-O': 1, 'C-C': 6, 'C-O': 2, 'C=C': 2}
1D rotors:
pivots: [1, 6], dihedral: [21, 1, 6, 9], rotor symmetry: 1, max scan energy: 33.05 kJ/mol
* Invalidated! pivots: [6, 9], dihedral: [1, 6, 9, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [7, 10], dihedral: [4, 7, 10, 9], rotor symmetry: 1, max scan energy: 66.20 kJ/mol
pivots: [9, 10], dihedral: [2, 9, 10, 7], rotor symmetry: 1, max scan energy: 47.08 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       4.04524100    0.51367400    0.79761800
O       5.10868400   -1.68462400   -0.15065000
C       4.93618800   -5.75820900   -1.98603600
C       5.04995200   -4.27874500   -1.54885300
C       3.65687000   -5.82928800   -2.85546300
C       3.17654800   -0.33381400    0.09915500
C       3.62842300   -3.75092800   -1.66607700
C       2.86702400   -4.64073000   -2.40276000
C       3.90802300   -1.57796800   -0.40469100
C       3.13759900   -2.54820900   -1.15097700
H       4.80669600   -6.39032500   -1.10328800
H       5.82413600   -6.11204600   -2.51234000
H       5.45884400   -4.14802100   -0.54782700
H       5.70206900   -3.70424300   -2.21629600
H       3.88984300   -5.73843600   -3.92743800
H       3.11014000   -6.77154400   -2.74610000
H       2.73258200    0.18308700   -0.76546800
H       2.34132600   -0.65611800    0.73979200
H       1.82640000   -4.47718000   -2.66020700
H       2.08941300   -2.31510800   -1.31946300
H       4.90516000    0.06141800    0.76951400
""",
)

entry(
    index = 200,
    label = "P252",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {11,S} {13,S}
2  C u0 p0 c0 {1,S} {7,S} {12,S} {14,S}
3  C u0 p0 c0 {5,S} {9,S} {15,S} {16,S}
4  C u0 p0 c0 {6,S} {7,D} {8,S}
5  C u0 p0 c0 {3,S} {8,D} {10,S}
6  C u1 p0 c0 {1,S} {4,S} {17,S}
7  C u0 p0 c0 {2,S} {4,D} {18,S}
8  C u0 p0 c0 {4,S} {5,D} {19,S}
9  O u0 p2 c0 {3,S} {20,S}
10 O u0 p2 c0 {5,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.41577,0.0533672,4.45343e-05,-1.08834e-07,5.38241e-11,-19427.4,15.872], Tmin=(10,'K'), Tmax=(735.65,'K')),
            NASAPolynomial(coeffs=[3.61081,0.0745461,-4.39959e-05,1.24884e-08,-1.37081e-12,-20057.9,10.9008], Tmin=(735.65,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-161.582,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (503.026,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 9, 'H-O': 2, 'C-C': 6, 'C-O': 2, 'C=C': 2}
1D rotors:
* Invalidated! pivots: [1, 5], dihedral: [20, 1, 5, 7], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 7], dihedral: [21, 2, 7, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [5, 7], dihedral: [1, 5, 7, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [6, 10], dihedral: [8, 6, 10, 7], rotor symmetry: 1, max scan energy: 9.80 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -3.71792100    0.02033700   -0.24208700
O      -2.29050800   -1.94331400   -1.30195800
C       1.86541000    2.02323200    0.27620200
C       2.52500400    1.81765900   -1.11887800
C      -2.32094500    0.00866800    0.09614900
C       0.65211600    0.33324700   -0.91474100
C      -1.55975400   -0.87738600   -0.86415300
C       0.73196800    1.03375700    0.29362900
C       1.68372300    0.75290900   -1.76209300
C      -0.29780600   -0.71464600   -1.29322100
H       2.57294400    1.84112500    1.09436600
H       3.57491500    1.50970700   -1.03028200
H       1.51344200    3.05429100    0.40997200
H       2.53466600    2.74309600   -1.70806300
H      -1.90101700    1.01611500    0.11891700
H      -2.28194500   -0.40336300    1.10871500
H       0.13710000    0.83687500    1.17491500
H       1.85747500    0.36606500   -2.75821700
H       0.05082900   -1.44135500   -2.02092600
H      -3.82691500    0.57404300   -1.02326800
H      -3.20947800   -1.76495200   -1.04897000
""",
)

entry(
    index = 201,
    label = "P253",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {9,S} {11,S}
2  C u0 p0 c0 {6,S} {7,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {10,S} {14,S} {15,S}
4  C u0 p0 c0 {5,S} {6,D} {8,S}
5  C u1 p0 c0 {1,S} {4,S} {18,S}
6  C u0 p0 c0 {2,S} {4,D} {16,S}
7  C u0 p0 c0 {2,S} {8,D} {17,S}
8  C u0 p0 c0 {4,S} {7,D} {19,S}
9  O u0 p2 c0 {1,S} {21,S}
10 O u0 p2 c0 {3,S} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75706,0.0161527,0.000309714,-7.0323e-07,4.8895e-10,-19514.1,16.6897], Tmin=(10,'K'), Tmax=(468.178,'K')),
            NASAPolynomial(coeffs=[0.537542,0.0871767,-5.72654e-05,1.787e-08,-2.12215e-12,-19689.5,24.6852], Tmin=(468.178,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-162.292,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (503.026,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 9, 'H-O': 2, 'C-C': 6, 'C-O': 2, 'C=C': 2}
1D rotors:
* Invalidated! pivots: [1, 3], dihedral: [21, 1, 3, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [2, 5], dihedral: [20, 2, 5, 3], rotor symmetry: 1, max scan energy: 24.05 kJ/mol
* Invalidated! pivots: [3, 5], dihedral: [1, 3, 5, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 7], dihedral: [1, 3, 7, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [6, 7], dihedral: [8, 6, 7, 3], invalidation reason: Another conformer for C8H11O2[163] exists which is 0.86 kJ/mol lower.Another conformer for C8H11O2[163] exists which is 0.86 kJ/mol lower.


External symmetry: 1, optical isomers: 2

Geometry:
O       2.50548300    0.60307900    1.27450400
O       4.15986300    0.42353700   -0.88153300
C       2.15834600   -0.35985400    0.25554000
C      -0.52899900   -4.07727500   -0.08701000
C       2.76517600    0.22278900   -1.02558100
C       0.02783700   -1.77154600    0.07301800
C       0.68025100   -0.55034100    0.18017300
C       0.57056100   -3.06477300    0.03665300
C      -1.77107700   -3.22208500   -0.11355500
C      -1.44147200   -1.92665800   -0.02445000
H       2.67033600   -1.30743300    0.46369800
H      -0.53632100   -4.79159300    0.74948600
H      -0.43011100   -4.68944100   -0.99557500
H       2.61919900   -0.47329600   -1.85354200
H       2.24509500    1.16181600   -1.26464500
H       1.61978200   -3.31908400    0.08475100
H      -2.77233300   -3.62443400   -0.19310600
H       0.09044800    0.36219900    0.18595000
H      -2.12870900   -1.08970300   -0.02118600
H       4.26765000    0.90773900   -0.05381500
H       2.20358500    0.26119900    2.12167400
""",
)

entry(
    index = 202,
    label = "P254",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {5,S} {16,S} {17,S}
5  C u0 p0 c0 {3,S} {4,S} {7,D}
6  C u0 p0 c0 {7,S} {8,D} {9,S}
7  C u0 p0 c0 {5,D} {6,S} {18,S}
8  C u0 p0 c0 {6,D} {19,S} {20,S}
9  O u0 p2 c0 {6,S} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {7,S}
19 O u1 p2 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73988,0.039531,6.82074e-05,-1.04663e-07,3.94141e-11,-31424.1,13.8844], Tmin=(10,'K'), Tmax=(955.244,'K')),
            NASAPolynomial(coeffs=[4.20989,0.0733994,-4.12489e-05,1.10002e-08,-1.13472e-12,-33148.9,3.08024], Tmin=(955.244,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-261.196,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (498.868,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 10, 'H-O': 1, 'C-C': 6, 'C-O': 2, 'C=C': 2}
1D rotors:
pivots: [1, 8], dihedral: [21, 1, 8, 9], rotor symmetry: 1, max scan energy: 58.30 kJ/mol
pivots: [8, 9], dihedral: [1, 8, 9, 7], rotor symmetry: 1, max scan energy: 52.04 kJ/mol
* Invalidated! pivots: [8, 10], dihedral: [1, 8, 10, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [7, 9], dihedral: [5, 7, 9, 8], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers


External symmetry: 1, optical isomers: 2

Geometry:
O       2.42553200   -0.80060800    0.51259000
O       4.32627600    0.93395300   -0.00470200
C      -1.68454900   -2.33428500   -0.34509300
C      -1.97986900   -2.01940100   -1.82188200
C      -0.22028600   -1.88750900   -0.15432700
C      -1.23988200   -0.68864800   -2.05460100
C      -0.02318800   -0.76990500   -1.15645200
C       2.23600400    0.05984700   -0.50366300
C       1.06237100    0.04940900   -1.28260000
C       3.32273000    0.97784500   -0.72459900
H      -2.34166100   -1.73860000    0.29765000
H      -1.84350400   -3.38385500   -0.08959100
H      -3.04697300   -1.95869000   -2.04540100
H      -1.55210100   -2.79834300   -2.46213000
H       0.01897400   -1.58006800    0.86507900
H       0.47048000   -2.70809600   -0.38714200
H      -1.87440800    0.14976100   -1.73320000
H      -0.98074800   -0.50340900   -3.10059400
H       1.04922800    0.79487100   -2.07411000
H       3.22152600    1.70532800   -1.54581500
H       3.30955900   -0.56372200    0.86218600
""",
)

entry(
    index = 203,
    label = "P255",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,D}
2 C u0 p0 c0 {1,S} {3,D} {5,S}
3 C u0 p0 c0 {1,S} {2,D} {6,S}
4 C u0 p0 c0 {1,D} {7,S} {8,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.1221,-0.0118785,0.000153342,-2.82714e-07,1.69597e-10,45557.9,7.1146], Tmin=(10,'K'), Tmax=(530.769,'K')),
            NASAPolynomial(coeffs=[1.57326,0.0279815,-1.76676e-05,5.38652e-09,-6.30206e-13,45537.5,15.0565], Tmin=(530.769,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (378.777,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 4, 'C-C': 2, 'C=C': 2}

External symmetry: 2, optical isomers: 1

Geometry:
C       0.14807900   -0.00448100   -0.00145000
C      -1.11880100    0.63909200   -0.24906300
C      -1.15030800   -0.57042300    0.27128600
C       1.47468200   -0.04462700   -0.01444300
H      -1.67076100    1.49437400   -0.60392500
H      -1.74592100   -1.39097700    0.63738700
H       2.05372100    0.79102100   -0.38665200
H       2.00930800   -0.91397800    0.34686000
""",
)

entry(
    index = 204,
    label = "P256",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {7,S} {13,S} {14,S}
4  C u0 p0 c0 {8,S} {9,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {8,D} {19,S}
6  C u0 p0 c0 {1,S} {7,D} {18,S}
7  C u0 p0 c0 {3,S} {6,D} {20,S}
8  C u0 p0 c0 {4,S} {5,D} {17,S}
9  O u0 p2 c0 {4,S} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 O u1 p2 c0 {8,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82548,0.051192,2.76125e-05,-5.8587e-08,2.18118e-11,-20820.1,14.0395], Tmin=(10,'K'), Tmax=(1064.41,'K')),
            NASAPolynomial(coeffs=[10.9116,0.0583999,-3.02298e-05,7.50723e-09,-7.26595e-13,-24245.4,-29.5936], Tmin=(1064.41,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-172.97,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (503.026,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'H-O': 1, 'C-H': 10, 'C-C': 6, 'C=C': 2}
1D rotors:
pivots: [1, 6], dihedral: [21, 1, 6, 10], rotor symmetry: 1, max scan energy: 31.22 kJ/mol
* Invalidated! pivots: [3, 7], dihedral: [4, 3, 7, 10], invalidation reason: Another conformer for C8H11O2[154] exists which is 1.03 kJ/mol lower.Another conformer for C8H11O2[154] exists which is 1.03 kJ/mol lower.
* Invalidated! pivots: [6, 10], dihedral: [1, 6, 10, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [7, 10], dihedral: [3, 7, 10, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       4.33060500   -0.42608600   -0.35875900
O       4.40052900    0.55839100    2.07752400
C       2.13798100    1.42394900    3.71863700
C       1.58664600    2.89016700    3.78961000
C       0.85719700    2.99388700    5.15087400
C       3.09070700   -0.10000700    0.20531700
C       2.08673400    0.85195700    2.34885400
C       1.24770800    0.70527000    4.72550300
C       0.56598000    1.55325000    5.49228600
C       3.25757600    0.46035400    1.61612800
H       3.18103400    1.39081300    4.05240000
H       2.38368500    3.62425100    3.66423600
H       0.86728100    3.04324300    2.98006900
H       1.49461500    3.44676300    5.92112300
H      -0.04428600    3.61141900    5.09149600
H       2.43809900   -0.98488700    0.25564900
H       2.56550400    0.64734400   -0.40868200
H       1.23907200   -0.37439400    4.81743900
H       1.11465500    0.73442600    1.87431200
H      -0.08556500    1.26110000    6.30805100
H       4.98352500   -0.19978400    0.32386500
""",
)

entry(
    index = 205,
    label = "P257",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {6,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {6,D} {16,S}
5  C u0 p0 c0 {1,S} {7,D} {18,S}
6  C u0 p0 c0 {3,S} {4,D} {17,S}
7  C u0 p0 c0 {5,D} {8,S} {9,S}
8  C u1 p0 c0 {7,S} {10,S} {19,S}
9  O u0 p2 c0 {7,S} {20,S}
10 O u0 p2 c0 {8,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68636,0.0396259,9.85939e-05,-1.74197e-07,7.94746e-11,-19760.7,14.2699], Tmin=(10,'K'), Tmax=(770.754,'K')),
            NASAPolynomial(coeffs=[3.55049,0.077209,-4.63186e-05,1.32231e-08,-1.45218e-12,-20835.2,7.78396], Tmin=(770.754,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-164.281,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (503.026,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'H-O': 2, 'C-H': 9, 'C-C': 6, 'C=C': 2}
1D rotors:
* Invalidated! pivots: [1, 9], dihedral: [20, 1, 9, 7], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [2, 10], dihedral: [21, 2, 10, 9], rotor symmetry: 1, max scan energy: 37.62 kJ/mol
* Invalidated! pivots: [3, 7], dihedral: [4, 3, 7, 9], invalidation reason: Another conformer for C8H11O2[148] exists which is 6.94 kJ/mol lower.Another conformer for C8H11O2[148] exists which is 6.94 kJ/mol lower.
* Invalidated! pivots: [9, 10], dihedral: [1, 9, 10, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [7, 9], dihedral: [3, 7, 9, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       1.53296800   -1.03424500    0.29895700
O       3.99846700   -0.27274200    0.86202700
C      -0.68995700    0.86829000   -0.27462300
C      -1.48528700    0.26265600    0.93534000
C      -2.43096800   -0.80575000    0.33333100
C      -0.87568600   -0.20779800   -1.34068200
C       0.73617800    1.24453300    0.02510500
C      -1.79838700   -1.11136500   -1.00418000
C       1.74191100    0.33822200    0.30479500
C       3.05415900    0.67223400    0.63594600
H      -1.20116100    1.77425500   -0.62457500
H      -0.77732900   -0.21562000    1.61544100
H      -2.01274100    1.03207000    1.50118700
H      -3.44566600   -0.41461100    0.18196800
H      -2.53322500   -1.68878400    0.97179700
H      -0.33650800   -0.18161100   -2.28160500
H      -2.11689000   -1.93639600   -1.63207600
H       1.00247900    2.29424000    0.05230800
H       3.39969500    1.68916300    0.74028800
H       0.72749500   -1.23819800   -0.19690100
H       3.57140400   -1.13181200    0.72701300
""",
)


entry(
    index = 206,
    label = "P259",
    molecule = 
"""
multiplicity 3
1  O u1 p2 c0 {9,S}
2  C u0 p0 c0 {3,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {5,D} {12,S}
4  C u0 p0 c0 {2,S} {8,D} {13,S}
5  C u0 p0 c0 {3,D} {6,S} {14,S}
6  C u1 p0 c0 {5,S} {7,S} {15,S}
7  C u0 p0 c0 {6,S} {9,D} {16,S}
8  C u0 p0 c0 {4,D} {18,S} {19,S}
9  C u0 p0 c0 {1,S} {7,D} {17,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.97983,0.105569,-0.000324429,7.15602e-07,-5.79873e-10,27734.6,15.1258], Tmin=(10,'K'), Tmax=(408.835,'K')),
            NASAPolynomial(coeffs=[2.56062,0.0691136,-4.18718e-05,1.22054e-08,-1.37381e-12,28107.8,20.9185], Tmin=(408.835,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (230.571,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (448.981,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 10, 'C-O': 1, 'C-C': 4, 'C=C': 3}
1D rotors:
pivots: [2, 3], dihedral: [4, 2, 3, 5], rotor symmetry: 1, max scan energy: 10.24 kJ/mol
pivots: [2, 4], dihedral: [3, 2, 4, 8], rotor symmetry: 1, max scan energy: 12.22 kJ/mol
* Invalidated! pivots: [5, 6], dihedral: [3, 5, 6, 7], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [6, 7], dihedral: [5, 6, 7, 9], invalidation reason: Another conformer for C8H10O[179] exists which is 7.33 kJ/mol lower.Another conformer for C8H10O[179] exists which is 7.33 kJ/mol lower.
* Invalidated! pivots: [7, 9], dihedral: [6, 7, 9, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 5], dihedral: [2, 3, 5, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O      -5.03726600   -1.68689000    0.12783200
C       1.75059300   -0.18186500    0.94713600
C       0.82147100   -1.27186300    0.49795400
C       2.39749700    0.53387000   -0.21687900
C      -0.53647300   -1.30388100    0.76225200
C      -1.40640200   -2.30062700    0.33752000
C      -2.83896800   -2.32963000    0.63320900
C       3.70185400    0.54535000   -0.47308900
C      -3.83744900   -1.65274700   -0.14441800
H       1.19688200    0.53867800    1.56074500
H       2.54006900   -0.60343100    1.58315700
H       1.25942300   -2.07313500   -0.09293400
H       1.71484400    1.05521200   -0.88483500
H      -0.95572200   -0.48814500    1.34944500
H      -1.00129800   -3.13152900   -0.24124900
H      -3.21565000   -2.90473800    1.47931100
H      -3.46895400   -1.07627000   -1.01465800
H       4.41258400    0.03219200    0.16809600
H       4.10828500    1.07152600   -1.32938300
""",
)

entry(
    index = 207,
    label = "P82",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,D}
2  C u0 p0 c0 {1,S} {5,D} {6,S}
3  C u1 p0 c0 {1,S} {7,S} {8,S}
4  C u0 p0 c0 {1,D} {9,S} {10,S}
5  C u0 p0 c0 {2,D} {11,D}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 O u0 p2 c0 {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85615,0.0091295,0.000146229,-3.31738e-07,2.23273e-10,15637,11.7326], Tmin=(10,'K'), Tmax=(507.238,'K')),
            NASAPolynomial(coeffs=[4.09943,0.0369484,-2.39762e-05,7.54319e-09,-9.12254e-13,15229.8,6.95308], Tmin=(507.238,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (129.974,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (253.591,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-H': 5, 'C-C': 2, 'C=O': 1}
1D rotors:
pivots: [2, 3], dihedral: [4, 2, 3, 6], rotor symmetry: 2, max scan energy: 13.41 kJ/mol
* Invalidated! pivots: [2, 4], dihedral: [3, 2, 4, 8], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
O      -0.61735900    0.88088500   -3.24143100
C      -0.34388000   -0.05925400    0.15922300
C       0.40275000    0.37102000   -1.04192300
C       0.37759000   -0.30688800    1.31960400
C      -1.73003800   -0.21261800    0.13095400
C      -0.14211500    0.64119700   -2.20919900
H       1.47956000    0.48348300   -0.99662000
H       1.45314800   -0.19304900    1.35959400
H      -0.12986100   -0.62374300    2.22139700
H      -2.31697500   -0.02633600   -0.75995900
H      -2.25976700   -0.52836600    1.01979700
""",
)

entry(
    index = 208,
    label = "P81",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {4,S} {14,S}
2  O u0 p2 c0 {8,S} {15,S}
3  O u1 p2 c0 {7,S}
4  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
5  C u0 p0 c0 {4,S} {6,D} {11,S}
6  C u0 p0 c0 {5,D} {7,S} {12,S}
7  C u0 p0 c0 {3,S} {6,S} {8,D}
8  C u0 p0 c0 {2,S} {7,D} {13,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.62004,0.0347448,3.91317e-05,-8.35572e-08,3.98299e-11,-43310.2,13.7875], Tmin=(10,'K'), Tmax=(744.26,'K')),
            NASAPolynomial(coeffs=[3.01636,0.0540063,-3.19696e-05,9.04702e-09,-9.89171e-13,-43663.9,13.5414], Tmin=(744.26,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-360.134,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (353.365,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 2, 'C=C': 2, 'C-H': 5, 'C-O': 3, 'C-C': 2}
1D rotors:
* Invalidated! pivots: [1, 4], dihedral: [14, 1, 4, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [2, 8], dihedral: [15, 2, 8, 7], rotor symmetry: 1, max scan energy: 73.85 kJ/mol
* Invalidated! pivots: [4, 5], dihedral: [1, 4, 5, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [6, 7], dihedral: [5, 6, 7, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [7, 8], dihedral: [3, 7, 8, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.57179300   -2.17796300    0.95952600
O       2.84033800    1.58306700    1.88438100
O       1.59238000   -0.59784300    1.27245200
C      -0.60821800   -1.98583600   -0.43195000
C      -0.51295200   -0.55829200   -0.91829700
C       0.25073700    0.45272100   -0.46330300
C       1.24452400    0.41619100    0.60939400
C       1.92862500    1.63229100    0.93030700
H       0.17915300   -2.56335400   -0.95158500
H      -1.56151900   -2.39606300   -0.77674600
H      -1.14140600   -0.33258800   -1.77765300
H       0.15594100    1.41666600   -0.95649200
H       1.77752200    2.59795200    0.46805600
H       0.27543100   -1.81367100    1.27109200
H       2.83294500    0.64156600    2.17431700
""",
)

entry(
    index = 209,
    label = "P75",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {5,D} {6,S}
3  C u0 p0 c0 {1,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {7,S} {10,S}
5  C u0 p0 c0 {2,D} {11,S} {12,S}
6  O u0 p2 c0 {1,S} {2,S}
7  O u0 p2 c0 {4,S} {13,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86503,0.00861592,0.000172931,-3.74857e-07,2.47659e-10,-9020.13,12.8376], Tmin=(10,'K'), Tmax=(495.9,'K')),
            NASAPolynomial(coeffs=[2.05573,0.0499121,-3.27506e-05,1.02336e-08,-1.21814e-12,-9169.01,16.9871], Tmin=(495.9,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-75.0327,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C=C': 2, 'C-H': 5, 'C-O': 3, 'C-C': 2}
1D rotors:
* Invalidated! pivots: [2, 6], dihedral: [13, 2, 6, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [3, 5], dihedral: [1, 3, 5, 6], rotor symmetry: 1, max scan energy: 24.22 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       0.07186900    1.37587900    0.29289000
O      -2.13446100    0.03930500   -0.71322200
C       0.27995000    0.12141500    1.12414100
C       1.11947200    0.54153900    0.02620900
C      -0.76272700   -0.92070400    1.02512200
C      -1.80584300   -0.91252600    0.18228700
C       2.11975200    0.45712800   -0.82504300
H       0.62567300    0.36372400    2.12657200
H      -0.67423600   -1.74867200    1.71787300
H      -2.51797100   -1.73018200    0.17387200
H       2.26439000    1.20928800   -1.59006300
H       2.80802000   -0.37452300   -0.76908900
H      -1.49814800    0.76985900   -0.63178800
""",
)

entry(
    index = 210,
    label = "P85",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {5,D} {6,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {6,S} {12,S}
5  C u0 p0 c0 {2,D} {7,S} {11,S}
6  O u0 p2 c0 {2,S} {4,S}
7  O u0 p2 c0 {5,S} {13,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89468,0.00597554,0.000152008,-2.74471e-07,1.50415e-10,-21765.7,11.1414], Tmin=(10,'K'), Tmax=(588.489,'K')),
            NASAPolynomial(coeffs=[0.0215222,0.0566979,-3.94616e-05,1.28796e-08,-1.58259e-12,-21732.3,24.1844], Tmin=(588.489,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-181.018,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C=C': 2, 'C-H': 5, 'C-O': 3, 'C-C': 2}
1D rotors:
pivots: [2, 7], dihedral: [13, 2, 7, 4], rotor symmetry: 1, max scan energy: 23.15 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O       0.18022800    1.19717100    0.05400200
O       2.79970000    0.44563300    0.60002400
C      -0.75179000   -0.99907300    0.25013500
C       0.50196100   -0.15062200    0.32002100
C      -1.78367200    0.05863100   -0.08565600
C      -1.17731600    1.23763600   -0.17366600
C       1.77248000   -0.45503200    0.57533200
H      -0.69050200   -1.77728100   -0.52018700
H      -0.97058000   -1.50495900    1.19827500
H      -2.83735400   -0.12272400   -0.22864800
H       2.08996500   -1.46630800    0.78733200
H      -1.56484400    2.22098000   -0.39265500
H       2.43172300    1.31594500    0.40213300
""",
)

entry(
    index = 211,
    label = "P77",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {6,S}
3  C u0 p0 c0 {2,D} {4,S} {10,S}
4  C u0 p0 c0 {3,S} {5,D} {11,S}
5  C u0 p0 c0 {4,D} {7,S} {12,S}
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
            NASAPolynomial(coeffs=[3.87162,0.00795912,0.000167411,-3.47847e-07,2.20043e-10,-8599.71,13.3699], Tmin=(10,'K'), Tmax=(517.505,'K')),
            NASAPolynomial(coeffs=[1.83313,0.0504453,-3.32137e-05,1.0412e-08,-1.24344e-12,-8746.65,18.4034], Tmin=(517.505,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-71.5428,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C=C': 2, 'C-H': 5, 'C-O': 3, 'C-C': 2}
1D rotors:
* Invalidated! pivots: [2, 7], dihedral: [13, 2, 7, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [5, 6], dihedral: [4, 5, 6, 7], rotor symmetry: 1, max scan energy: 22.26 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       0.21988000   -3.68756900   -0.18264500
O       0.96305300   -1.29374500   -1.49729200
C      -0.41642900   -4.24609900    1.04087500
C      -0.86610800   -3.05779300    0.37872300
C      -1.57909800   -1.95897000    0.17507100
C      -1.36513700   -0.95232400   -0.86021500
C      -0.24567200   -0.69570200   -1.56233900
H      -0.91246600   -5.19691400    0.87061400
H       0.20220000   -4.17919700    1.93117900
H      -2.40901100   -1.80320500    0.85586400
H      -2.20497800   -0.30039100   -1.06988400
H      -0.23462500    0.10895700   -2.28893900
H       0.93933700   -2.08935600   -0.94425100
""",
)

entry(
    index = 212,
    label = "P38",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {8,S}
3  C u0 p0 c0 {1,S} {7,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {5,D} {11,S}
5  C u0 p0 c0 {2,S} {4,D} {12,S}
6  O u0 p2 c0 {1,S} {2,S}
7  O u0 p2 c0 {3,S} {13,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87948,0.00683699,0.000155652,-2.86613e-07,1.58743e-10,2027.59,11.3398], Tmin=(10,'K'), Tmax=(593.022,'K')),
            NASAPolynomial(coeffs=[0.948023,0.0550988,-3.84818e-05,1.2638e-08,-1.56328e-12,1874.33,19.727], Tmin=(593.022,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (16.8043,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C=C': 1, 'C-H': 5, 'C-O': 3, 'C-C': 4}
1D rotors:
pivots: [2, 5], dihedral: [13, 2, 5, 3], rotor symmetry: 1, max scan energy: 22.08 kJ/mol
* Invalidated! pivots: [3, 5], dihedral: [1, 3, 5, 2], invalidation reason: Inconsistent initial and final conformers But unable to propose troubleshooting methods.Inconsistent initial and final conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.52136000    2.03472700    1.92964900
O      -2.33364900   -0.18343600    0.40876900
C      -0.76870000    1.61076000    0.75567100
C      -0.26703200    1.29740200    2.08851600
C      -1.49897400    0.75861300   -0.23731200
C       0.42046900    2.57936400    0.60423700
C       0.87901400    2.28211500    1.82786500
H      -0.29947500    0.36773800    2.63868200
H      -2.07408100    1.40925100   -0.91488300
H      -0.78051700    0.20161200   -0.84480900
H       0.67585500    3.32337900   -0.13878600
H       1.65867400    2.68683100    2.45918600
H      -2.78675400    0.30198900    1.11032000
""",
)

entry(
    index = 213,
    label = "MF",
    molecule = 
"""
1  O u0 p2 c0 {3,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {5,S} {10,S}
5  C u0 p0 c0 {4,S} {6,D} {11,S}
6  C u0 p0 c0 {1,S} {5,D} {12,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98619,0.00025583,0.000129024,-2.17556e-07,1.16796e-10,-11338.6,10.2611], Tmin=(10,'K'), Tmax=(558.837,'K')),
            NASAPolynomial(coeffs=[-1.06192,0.0479158,-2.98427e-05,8.87542e-09,-1.01136e-12,-10954.3,30.0674], Tmin=(558.837,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-94.2911,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (278.535,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-H': 6, 'C-O': 2, 'C-C': 2}
1D rotors:
pivots: [2, 3], dihedral: [7, 2, 3, 1], rotor symmetry: 3, max scan energy: 4.00 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O      -0.13092200    0.83234500    0.89594700
C       1.89887600   -0.23679900    0.09180200
C       0.42436300   -0.06022200    0.02019100
C      -0.55252100   -0.60764800   -0.75330600
C      -1.79153100   -0.01869300   -0.33200900
C      -1.47711700    0.84326700    0.66634400
H       2.20963400   -0.58853600    1.08055200
H       2.42196500    0.70470000   -0.10280600
H       2.22256400   -0.96841700   -0.64966100
H      -0.41045400   -1.34207600   -1.53039000
H      -2.77701600   -0.21509300   -0.72345300
H      -2.05332000    1.50691700    1.28818800
""",
)

entry(
    index = 214,
    label = "P260",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {6,S} {11,S} {14,S}
3  C u0 p0 c0 {5,S} {8,S} {9,S} {15,S}
4  C u0 p0 c0 {1,S} {5,D} {7,S}
5  C u0 p0 c0 {3,S} {4,D} {17,S}
6  C u0 p0 c0 {2,S} {7,D} {16,S}
7  C u0 p0 c0 {4,S} {6,D} {19,S}
8  C u1 p0 c0 {3,S} {10,S} {18,S}
9  O u0 p2 c0 {3,S} {20,S}
10 O u0 p2 c0 {8,S} {21,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.42829,0.0544187,4.004e-05,-9.98575e-08,4.80166e-11,-13640.4,15.4611], Tmin=(10,'K'), Tmax=(771.357,'K')),
            NASAPolynomial(coeffs=[4.4423,0.0731179,-4.29112e-05,1.21006e-08,-1.31957e-12,-14509.6,6.21241], Tmin=(771.357,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-113.451,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (503.026,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 9, 'C-C': 6, 'C=C': 2, 'H-O': 2, 'C-O': 2}
1D rotors:
* Invalidated! pivots: [1, 5], dihedral: [20, 1, 5, 7], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 10], dihedral: [21, 2, 10, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [5, 7], dihedral: [1, 5, 7, 6], rotor symmetry: 1, max scan energy: 14.81 kJ/mol
* Invalidated! pivots: [5, 10], dihedral: [1, 5, 10, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.32365400    1.48031500    0.59439900
O      -2.32353900   -1.23938200    0.52651700
C      -0.44526200    3.59920900   -1.17786500
C       0.34283700    4.91967200   -1.39464100
C      -1.15992600    0.82620600   -0.00537200
C       0.42563300    2.75921200   -0.25135800
C       0.12985300    1.55010000    0.25432200
C       1.61950400    4.70873600   -0.62144800
C       1.64431200    3.52240700    0.00200700
C      -1.13048100   -0.58725000    0.47835400
H      -0.20620000    5.79154100   -1.02054600
H      -0.61303200    3.07506100   -2.12367100
H      -1.42932000    3.76387100   -0.73607300
H       0.54238900    5.11806800   -2.45352800
H      -1.41372000    0.86728500   -1.07743800
H       2.41104600    5.44800400   -0.58414500
H       0.83820500    1.06556500    0.92153900
H      -0.27982700   -1.23658700    0.31056100
H       2.45284700    3.15416700    0.62217300
H      -2.08620900    1.66270800    1.51280900
H      -2.99592200   -0.54261700    0.60151300
""",
)

entry(
    index = 215,
    label = "P261",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {12,S}
3  C u0 p0 c0 {1,S} {2,S} {10,S} {13,S}
4  C u0 p0 c0 {5,S} {6,S} {15,S} {16,S}
5  C u0 p0 c0 {4,S} {7,S} {14,S} {17,S}
6  C u0 p0 c0 {1,S} {4,S} {8,D}
7  C u1 p0 c0 {5,S} {8,S} {18,S}
8  C u0 p0 c0 {6,D} {7,S} {19,S}
9  O u0 p2 c0 {2,S} {20,S}
10 O u0 p2 c0 {3,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.55492,0.0452534,8.46075e-05,-1.68768e-07,8.27995e-11,-13443.7,16.1386], Tmin=(10,'K'), Tmax=(722.132,'K')),
            NASAPolynomial(coeffs=[3.71802,0.0763176,-4.63215e-05,1.34072e-08,-1.49185e-12,-14300.8,9.63361], Tmin=(722.132,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-111.807,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (498.868,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 9, 'C-C': 8, 'C=C': 1, 'H-O': 2, 'C-O': 2}
1D rotors:
pivots: [1, 4], dihedral: [20, 1, 4, 3], rotor symmetry: 1, max scan energy: 24.59 kJ/mol
* Invalidated! pivots: [2, 5], dihedral: [21, 2, 5, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [3, 8], dihedral: [4, 3, 8, 6], rotor symmetry: 1, max scan energy: 9.95 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.42240400    1.93705500    1.25685400
O      -0.19776100    2.26828700   -1.41525300
C       1.23088700    0.61698200   -0.15942700
C      -0.16035400    0.79956600    0.50479100
C      -0.01522800    0.94493500   -0.97174000
C       3.26547500   -0.92025000    0.38935400
C       3.56887100   -2.42148900    0.11138900
C       1.90289900   -0.68150000   -0.22987200
C       2.33516200   -2.91375600   -0.60169700
C       1.43065400   -1.88042700   -0.76795300
H       1.86970300    1.47700200    0.02770100
H      -0.62519000   -0.09369800    0.90737700
H      -0.41566500    0.18133100   -1.63463700
H       3.75671700   -2.97840700    1.03711300
H       4.02486400   -0.25892800   -0.04588100
H       3.25190200   -0.69953200    1.46389000
H       4.46876900   -2.54762200   -0.50342500
H       2.19861400   -3.93189500   -0.94059600
H       0.47170700   -1.99563600   -1.26089200
H      -0.49488600    2.66662100    0.62529300
H       0.49888200    2.48107800   -2.04427300
""",
)

entry(
    index = 216,
    label = "P262",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {12,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {11,S}
3  C u0 p0 c0 {1,S} {5,S} {9,S} {13,S}
4  C u0 p0 c0 {2,S} {7,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {10,S} {16,S} {17,S}
6  C u1 p0 c0 {1,S} {2,S} {8,S}
7  C u0 p0 c0 {4,S} {8,D} {18,S}
8  C u0 p0 c0 {6,S} {7,D} {19,S}
9  O u0 p2 c0 {3,S} {21,S}
10 O u0 p2 c0 {5,S} {20,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79585,0.0125045,0.000283993,-5.73375e-07,3.54028e-10,-2967.64,15.8492], Tmin=(10,'K'), Tmax=(524.775,'K')),
            NASAPolynomial(coeffs=[-0.709489,0.0897454,-5.94131e-05,1.86624e-08,-2.22775e-12,-3085.49,29.0517], Tmin=(524.775,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-24.7437,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (503.026,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 9, 'C-C': 8, 'C=C': 1, 'H-O': 2, 'C-O': 2}
1D rotors:
* Invalidated! pivots: [1, 5], dihedral: [21, 1, 5, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [2, 7], dihedral: [20, 2, 7, 5], rotor symmetry: 1, max scan energy: 23.77 kJ/mol
* Invalidated! pivots: [3, 5], dihedral: [4, 3, 5, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [5, 7], dihedral: [1, 5, 7, 2], invalidation reason: Inconsistent initial and final conformers But unable to propose troubleshooting methods.Inconsistent initial and final conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       4.15743000   -0.33263100    0.91441200
O       2.77310000    1.29058200   -0.82529200
C       1.90859200    0.03050000    1.73527200
C       0.66782200   -0.74994000    2.22746300
C       2.77310100   -0.62572200    0.67682300
C      -0.51997200   -0.04704900    2.88682100
C       2.49382700   -0.09711900   -0.72876700
C       1.83899800   -0.52767700    3.11429100
C       0.07628900    0.53176300    4.15429700
C       1.39139600    0.25909100    4.25973000
H       0.50512500   -1.70114100    1.73036300
H       1.85076300    1.11239200    1.63461600
H       2.61255900   -1.71302200    0.69280400
H      -1.33558000   -0.74882300    3.09724900
H      -0.94813200    0.74153300    2.25397800
H       3.09633800   -0.67251900   -1.44499800
H       1.43927300   -0.23302500   -0.97876600
H      -0.48738700    1.15744800    4.83725000
H       2.04564200    0.62534200    5.04134300
H       3.66292400    1.39832000   -0.46683100
H       4.31602000   -0.45093000    1.85695600
""",
)

entry(
    index = 217,
    label = "P263",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {12,S} {13,S}
2  C u0 p0 c0 {4,S} {6,S} {11,S} {16,S}
3  C u0 p0 c0 {5,S} {7,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {2,S} {7,D}
5  C u1 p0 c0 {1,S} {3,S} {17,S}
6  C u0 p0 c0 {2,S} {8,D} {9,S}
7  C u0 p0 c0 {3,S} {4,D} {18,S}
8  C u0 p0 c0 {6,D} {10,S} {19,S}
9  O u0 p2 c0 {6,S} {21,S}
10 O u0 p2 c0 {8,S} {20,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.5638,0.0491087,6.63515e-05,-1.3431e-07,6.21906e-11,-14173.2,14.8021], Tmin=(10,'K'), Tmax=(786.882,'K')),
            NASAPolynomial(coeffs=[5.11086,0.0741818,-4.42314e-05,1.25731e-08,-1.37621e-12,-15436.3,1.22977], Tmin=(786.882,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-117.838,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (503.026,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 9, 'C-C': 6, 'C=C': 2, 'H-O': 2, 'C-O': 2}
1D rotors:
* Invalidated! pivots: [1, 8], dihedral: [21, 1, 8, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [2, 10], dihedral: [20, 2, 10, 8], rotor symmetry: 1, max scan energy: 26.81 kJ/mol
* Invalidated! pivots: [4, 6], dihedral: [8, 4, 6, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 8], dihedral: [6, 4, 8, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       1.90804000   -1.14316000   -0.81041300
O      -0.14221000    0.64052700   -1.14255400
C       4.53552900    1.22504000    0.73855400
C       3.61729900    0.43515000   -1.61990300
C       6.05809300   -0.67998100    1.12657300
C       4.51341900    0.24472200   -0.42193300
C       5.50832400    0.59736100    1.68870800
C       2.18183600    0.13169700   -1.29129300
C       5.33534600   -0.78764000   -0.19758200
C       1.14757600    0.95987100   -1.45524000
H       3.95417000   -0.22518800   -2.42887300
H       3.53317100    1.37043900    1.17128300
H       4.84732200    2.22874600    0.40253400
H       7.15241000   -0.65428500    0.99316700
H       5.87196800   -1.55128700    1.77550000
H       3.68676300    1.46465300   -1.98563500
H       5.79598500    1.02135400    2.64118600
H       5.50038400   -1.60394800   -0.89310500
H       1.25411000    1.94956400   -1.87653100
H      -0.12559000   -0.25167500   -0.77038200
H       2.66779200   -1.43552900   -0.29014800
""",
)

entry(
    index = 218,
    label = "P264",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {7,S} {9,S} {12,S}
3  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {8,S} {15,S} {16,S}
5  C u0 p0 c0 {6,S} {7,S} {17,S} {18,S}
6  C u0 p0 c0 {3,S} {5,S} {8,D}
7  C u1 p0 c0 {2,S} {5,S} {10,S}
8  C u0 p0 c0 {4,S} {6,D} {19,S}
9  O u0 p2 c0 {2,S} {20,S}
10 O u0 p2 c0 {7,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86619,0.00765872,0.000251922,-4.40926e-07,2.38824e-10,-14869.3,12.8005], Tmin=(10,'K'), Tmax=(569.227,'K')),
            NASAPolynomial(coeffs=[-5.54016,0.101791,-7.00021e-05,2.26218e-08,-2.75985e-12,-14252.6,48.8912], Tmin=(569.227,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-123.69,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (503.026,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 9, 'C-C': 8, 'C=C': 1, 'H-O': 2, 'C-O': 2}
1D rotors:
* Invalidated! pivots: [1, 4], dihedral: [20, 1, 4, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [2, 9], dihedral: [21, 2, 9, 4], rotor symmetry: 1, max scan energy: 28.22 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       0.79542900   -1.82997000    0.29923000
O       1.20813400   -2.61713500   -2.16820800
C       1.53271300    0.47225900   -0.24024200
C       0.66493700   -0.74709600   -0.63039800
C       1.43077700    1.49509800   -1.41380900
C       2.95896200   -0.08902000   -0.44328500
C       0.91569500   -0.33215800   -3.14307300
C       1.93462600    0.63737500   -2.56137400
C       1.32199800   -1.23941000   -1.96056200
C       2.73120400   -0.50617800   -1.89463900
H       1.29936300    0.88315900    0.74528300
H      -0.39410300   -0.49927700   -0.76689300
H       2.08788700    2.34735300   -1.21093100
H       0.42022400    1.87943100   -1.57818700
H       3.73243900    0.67486400   -0.32510400
H       3.17880300   -0.92791100    0.21867700
H       1.24312300   -0.79126700   -4.08003900
H      -0.12740000   -0.01571100   -3.22830100
H       3.52546500   -0.98818900   -2.46122000
H       0.23080500   -1.65988700    1.05783100
H       1.15683500   -3.01876000   -1.28913000
""",
)

entry(
    index = 219,
    label = "P265",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {6,S} {14,S} {15,S}
4  C u0 p0 c0 {5,S} {7,S} {16,S} {17,S}
5  C u0 p0 c0 {2,S} {4,S} {6,D}
6  C u0 p0 c0 {3,S} {5,D} {19,S}
7  C u0 p0 c0 {4,S} {8,D} {18,S}
8  C u0 p0 c0 {7,D} {9,S} {20,S}
9  O u0 p2 c0 {8,S} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 O u1 p2 c0 {7,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61208,0.0571564,4.64023e-06,-3.34269e-08,1.30631e-11,-26775.5,14.9142], Tmin=(10,'K'), Tmax=(1105.94,'K')),
            NASAPolynomial(coeffs=[10.5171,0.0570086,-2.88319e-05,7.04852e-09,-6.74902e-13,-29821.1,-25.9578], Tmin=(1105.94,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-222.565,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (503.026,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 10, 'C-C': 6, 'C=C': 2, 'H-O': 1, 'C-O': 2}
1D rotors:
* Invalidated! pivots: [1, 10], dihedral: [21, 1, 10, 9], invalidation reason: Another conformer for C8H11O2[147] exists which is 1.47 kJ/mol lower.Another conformer for C8H11O2[147] exists which is 1.47 kJ/mol lower.
pivots: [6, 7], dihedral: [9, 6, 7, 4], rotor symmetry: 1, max scan energy: 13.59 kJ/mol
* Invalidated! pivots: [6, 9], dihedral: [7, 6, 9, 2], invalidation reason: 
* Invalidated! pivots: [9, 10], dihedral: [2, 9, 10, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       4.43652000   -2.06290500    2.12060000
O       3.13240800   -0.36036400    0.62328800
C       2.47231800   -1.62150400   -3.73032700
C       2.01753400   -0.92721900   -2.42359400
C       1.85447900   -3.04341700   -3.67634500
C       1.38090700   -1.90245800   -0.04955200
C       1.64810400   -2.08772900   -1.52108000
C       1.56324100   -3.23047100   -2.20661400
C       2.64108800   -1.50324500    0.69965800
C       3.32689800   -2.46094200    1.50777700
H       2.18395200   -1.06894700   -4.62666600
H       3.56269000   -1.70219500   -3.73506600
H       1.13678000   -0.28908200   -2.58126800
H       2.78602700   -0.28610900   -1.98521900
H       2.52782600   -3.80703900   -4.07867700
H       0.92816600   -3.10920100   -4.26328500
H       0.65052900   -1.09866200    0.09911900
H       0.96509500   -2.82089100    0.37451200
H       1.27248900   -4.18531600   -1.78064500
H       3.03774100   -3.48865600    1.67653500
H       4.53520200   -1.12411500    1.84650500
""",
)

entry(
    index = 220,
    label = "P266",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
3  C u0 p0 c0 {4,S} {5,S} {15,S} {16,S}
4  C u0 p0 c0 {3,S} {6,S} {7,D}
5  C u0 p0 c0 {3,S} {8,D} {9,S}
6  C u1 p0 c0 {1,S} {4,S} {17,S}
7  C u0 p0 c0 {2,S} {4,D} {18,S}
8  C u0 p0 c0 {5,D} {10,S} {19,S}
9  O u0 p2 c0 {5,S} {21,S}
10 O u0 p2 c0 {8,S} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63748,0.0473174,6.68806e-05,-1.27911e-07,5.66246e-11,-20059.6,14.734], Tmin=(10,'K'), Tmax=(825.57,'K')),
            NASAPolynomial(coeffs=[5.62841,0.0726756,-4.27939e-05,1.20126e-08,-1.29978e-12,-21581.2,-1.71416], Tmin=(825.57,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-166.745,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (503.026,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 9, 'C-C': 6, 'C=C': 2, 'H-O': 2, 'C-O': 2}
1D rotors:
* Invalidated! pivots: [1, 7], dihedral: [21, 1, 7, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [2, 10], dihedral: [20, 2, 10, 7], rotor symmetry: 1, max scan energy: 27.51 kJ/mol
* Invalidated! pivots: [5, 6], dihedral: [7, 5, 6, 8], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [5, 7], dihedral: [6, 5, 7, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       1.79599200   -1.38790400   -0.71203500
O      -0.28320100   -0.25111000    0.65330200
C       6.22178100   -1.66306200    0.08378000
C       6.08432500   -0.93805900    1.45656400
C       3.19994700    0.63599400   -0.55263900
C       4.40436000   -0.11800800   -0.02785200
C       1.91674400   -0.08296800   -0.24662900
C       5.10166400   -1.08711200   -0.74245700
C       4.93364800    0.00926400    1.25436000
C       0.86680800    0.43636400    0.39391200
H       6.14617800   -2.75203500    0.18468600
H       7.19739500   -1.47212700   -0.37996700
H       7.00478900   -0.41271500    1.73794400
H       5.88283600   -1.64538300    2.27101800
H       3.30160600    0.75802400   -1.63840900
H       3.16184600    1.63586800   -0.11392300
H       4.92881700   -1.33763100   -1.78240100
H       4.56185200    0.68149500    2.01704800
H       0.84068400    1.46056800    0.73857800
H      -0.15210400   -1.14616200    0.31127500
H       2.65200100   -1.82556200   -0.60876100
""",
)

entry(
    index = 221,
    label = "P267",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {8,S} {9,S} {15,S}
4  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
5  C u0 p0 c0 {4,S} {7,S} {16,S} {17,S}
6  C u0 p0 c0 {7,S} {8,S} {18,S} {19,S}
7  C u1 p0 c0 {1,S} {5,S} {6,S}
8  C u0 p0 c0 {3,S} {6,S} {20,D}
9  O u0 p2 c0 {3,S} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 O u0 p2 c0 {8,D}
21 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86265,0.00903747,0.000289908,-6.04908e-07,4.01632e-10,-26258.3,15.0487], Tmin=(10,'K'), Tmax=(453.935,'K')),
            NASAPolynomial(coeffs=[-2.99042,0.0920944,-5.94565e-05,1.81937e-08,-2.12284e-12,-25869.6,40.1257], Tmin=(453.935,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-218.346,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (503.026,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 10, 'C-C': 9, 'H-O': 1, 'C=O': 1, 'C-O': 1}
1D rotors:
pivots: [1, 5], dihedral: [21, 1, 5, 3], rotor symmetry: 1, max scan energy: 25.92 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       2.38989200    1.04830900    1.45341900
O       3.82087100    1.21321100   -0.90345400
C       1.32830100   -0.90645500    0.32400900
C      -0.14175900   -1.21499800    0.67423900
C       1.82035600    0.55034200    0.27107500
C      -0.48101400   -2.43800400   -0.20667500
C       0.27957500   -2.19081400   -1.53467400
C       2.39165700   -0.52322700   -1.90931100
C       1.45489200   -1.37098800   -1.10962900
C       2.82472800    0.53402700   -0.89036800
H       2.00597200   -1.45045900    1.00114500
H      -0.10273200   -3.34969100    0.26651100
H      -1.55538900   -2.56960800   -0.35222600
H      -0.76935500   -0.36358300    0.38630700
H      -0.30415000   -1.39771300    1.73816400
H       0.97890900    1.18822600   -0.05752500
H      -0.34719600   -1.63186500   -2.25000100
H       0.55108200   -3.12415200   -2.04314300
H       1.91185400   -0.03920400   -2.77491200
H       3.27838500   -1.03537700   -2.30606000
H       3.17529100    1.54589000    1.18065900
""",
)

entry(
    index = 222,
    label = "P268",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {9,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
4  C u0 p0 c0 {3,S} {6,S} {16,S} {17,S}
5  C u0 p0 c0 {6,S} {7,S} {18,S} {19,S}
6  C u1 p0 c0 {1,S} {4,S} {5,S}
7  C u0 p0 c0 {5,S} {8,D} {9,S}
8  C u0 p0 c0 {7,D} {10,S} {20,S}
9  O u0 p2 c0 {1,S} {7,S}
10 O u0 p2 c0 {8,S} {21,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8447,0.00937251,0.000268613,-5.12265e-07,3.03533e-10,-15938.5,15.8072], Tmin=(10,'K'), Tmax=(527.903,'K')),
            NASAPolynomial(coeffs=[-3.10456,0.093856,-6.18778e-05,1.9308e-08,-2.29095e-12,-15648.2,40.6933], Tmin=(527.903,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-132.577,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (503.026,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 10, 'C-C': 7, 'C=C': 1, 'H-O': 1, 'C-O': 3}
1D rotors:
pivots: [2, 10], dihedral: [21, 2, 10, 9], rotor symmetry: 1, max scan energy: 23.19 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.97426200   -0.14227600   -1.22481500
O      -3.56533900   -1.08527500   -1.55658100
C       0.07590000    0.71788400   -0.73406500
C       1.45733600    0.45374400   -1.35273500
C       2.42562400    0.76794500   -0.19173400
C       1.69636900    0.24316300    1.07352900
C      -0.90490700   -0.49922200    1.14774300
C       0.24568400    0.35728000    0.71446100
C      -1.70755600   -0.61179300   -0.13409500
C      -2.94551900   -1.06024100   -0.33561400
H       2.57145500    1.84991600   -0.11162000
H       3.41119800    0.31927900   -0.33054300
H       1.50670800   -0.60656200   -1.61899400
H       1.65425800    1.03987000   -2.25264900
H      -0.24051400    1.76010600   -0.89491000
H       1.97688500    0.79552500    1.97801500
H       1.95707900   -0.80895300    1.26880800
H      -0.55024100   -1.47752500    1.50520200
H      -1.49438800   -0.06476800    1.96511200
H      -3.55426200   -1.46362600    0.46128600
H      -2.95086900   -0.69483800   -2.19151400
""",
)

entry(
    index = 223,
    label = "P269",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {13,S} {14,S}
2  C u0 p0 c0 {6,S} {7,S} {9,S} {12,S}
3  C u0 p0 c0 {1,S} {8,S} {10,S} {11,S}
4  C u0 p0 c0 {5,S} {6,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {4,S} {7,D}
6  C u0 p0 c0 {2,S} {4,S} {17,D}
7  C u0 p0 c0 {2,S} {5,D} {18,S}
8  C u1 p0 c0 {3,S} {19,S} {20,S}
9  O u0 p2 c0 {2,S} {21,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 O u0 p2 c0 {6,D}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.4957,0.0651689,-1.45415e-05,-1.69653e-08,8.10843e-12,-17245.5,14.9074], Tmin=(10,'K'), Tmax=(1138.67,'K')),
            NASAPolynomial(coeffs=[12.7812,0.0536059,-2.70468e-05,6.59598e-09,-6.30016e-13,-20725.2,-37.0899], Tmin=(1138.67,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-143.353,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (498.868,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 10, 'C-C': 7, 'C=C': 1, 'H-O': 1, 'C=O': 1, 'C-O': 1}
1D rotors:
pivots: [1, 4], dihedral: [21, 1, 4, 8], rotor symmetry: 1, max scan energy: 17.98 kJ/mol
* Invalidated! pivots: [3, 5], dihedral: [7, 3, 5, 10], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 7], dihedral: [5, 3, 7, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [5, 10], dihedral: [3, 5, 10, 19], rotor symmetry: 2, max scan energy: 2.11 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.84546700    1.81630300   -1.15119000
O      -3.27045700    0.14849600    1.09850200
C       1.06728700   -1.04008900   -0.85871600
C      -1.77966800    1.45411500   -0.29420900
C       2.18791200   -1.13011800    0.20161300
C      -0.96753600   -0.63956500    0.76835800
C      -0.12233900   -0.23612600   -0.42613200
C      -2.16449800    0.29745600    0.64577200
C      -0.58781100    0.87850900   -1.00522900
C       2.79519500    0.18020200    0.56177900
H       2.96440900   -1.81484900   -0.16523600
H       1.78875800   -1.62740300    1.10231800
H      -1.48356600    2.31839900    0.32806200
H       0.73675600   -2.05934900   -1.09605400
H       1.47490500   -0.61456400   -1.78059100
H      -0.45862400   -0.46606400    1.72552300
H      -1.28547900   -1.68724400    0.76336500
H      -0.15558200    1.35170500   -1.87874100
H       2.29692500    1.11266400    0.32754500
H       3.71319800    0.22198500    1.13482600
H      -3.65584800    1.68824900   -0.63991000
""",
)

entry(
    index = 224,
    label = "P270",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
3  C u0 p0 c0 {4,S} {5,S} {15,S} {16,S}
4  C u0 p0 c0 {1,S} {3,S} {7,D}
5  C u0 p0 c0 {3,S} {8,D} {9,S}
6  C u1 p0 c0 {2,S} {7,S} {17,S}
7  C u0 p0 c0 {4,D} {6,S} {18,S}
8  C u0 p0 c0 {5,D} {10,S} {19,S}
9  O u0 p2 c0 {5,S} {20,S}
10 O u0 p2 c0 {8,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.64521,0.049732,5.37012e-05,-1.06627e-07,4.58379e-11,-20666.3,14.9675], Tmin=(10,'K'), Tmax=(867.849,'K')),
            NASAPolynomial(coeffs=[6.67462,0.0700011,-4.04989e-05,1.1187e-08,-1.19349e-12,-22481.2,-6.64527], Tmin=(867.849,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-171.77,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (503.026,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 9, 'C-C': 6, 'C=C': 2, 'H-O': 2, 'C-O': 2}
1D rotors:
* Invalidated! pivots: [1, 7], dihedral: [20, 1, 7, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [2, 10], dihedral: [21, 2, 10, 7], rotor symmetry: 1, max scan energy: 26.64 kJ/mol
* Invalidated! pivots: [5, 6], dihedral: [7, 5, 6, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [5, 7], dihedral: [6, 5, 7, 1], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers


External symmetry: 1, optical isomers: 2

Geometry:
O       2.25197200   -0.17103600   -1.48813200
O      -0.07414400    0.92079400   -0.54752800
C       4.24818300   -0.31695400    1.82095100
C       5.79869500   -0.19797600    1.74359100
C       2.47864300   -1.71780700    0.42193900
C       3.89053000   -1.32171600    0.74789400
C       1.72317800   -0.62308700   -0.28342700
C       6.18544500   -1.16958600    0.65795600
C       5.05231100   -1.77090500    0.12839000
C       0.57610500   -0.07474700    0.12329600
H       3.91433200   -0.66626900    2.80660500
H       3.74765600    0.64447800    1.66005000
H       6.27798900   -0.44350700    2.69857800
H       6.11737100    0.82392400    1.50293000
H       1.93453900   -1.97653000    1.33839600
H       2.49304300   -2.61409500   -0.21166400
H       7.20471400   -1.35852000    0.34877000
H       5.06492400   -2.51192200   -0.66402700
H       0.05809700   -0.40034200    1.01442100
H       3.21462800   -0.20732800   -1.42662900
H       0.46984400    1.13834800   -1.31668900
""",
)

entry(
    index = 225,
    label = "P271",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {7,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {8,D} {9,S}
6  C u0 p0 c0 {1,S} {7,D} {17,S}
7  C u0 p0 c0 {4,S} {6,D} {18,S}
8  C u0 p0 c0 {5,D} {19,S} {20,S}
9  O u0 p2 c0 {5,S} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 O u1 p2 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73082,0.0562252,6.2076e-06,-3.29447e-08,1.22289e-11,-26352.4,14.2576], Tmin=(10,'K'), Tmax=(1167.29,'K')),
            NASAPolynomial(coeffs=[12.9658,0.0528046,-2.56672e-05,5.97446e-09,-5.42909e-13,-30431.3,-39.9613], Tmin=(1167.29,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-219.018,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (494.711,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 10, 'C-C': 6, 'C=C': 2, 'H-O': 1, 'C-O': 2}
1D rotors:
pivots: [1, 7], dihedral: [21, 1, 7, 5], rotor symmetry: 1, max scan energy: 68.23 kJ/mol
pivots: [3, 5], dihedral: [4, 3, 5, 7], rotor symmetry: 1, max scan energy: 20.04 kJ/mol
pivots: [5, 7], dihedral: [3, 5, 7, 1], rotor symmetry: 1, max scan energy: 12.52 kJ/mol
* Invalidated! pivots: [7, 10], dihedral: [1, 7, 10, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       2.54182900    1.18670500    0.19450600
O       3.96931700   -1.00972600    0.13427700
C      -0.42514600    0.57227000    0.00948200
C      -0.68003300   -0.57215600    1.02849400
C       0.68434900    0.26311300   -1.02732600
C      -2.21155100   -0.59061300    1.26525500
C       2.03483800    0.11915900   -0.42750500
C      -1.79010700    0.77301400   -0.61302500
C      -2.75083900    0.14425100    0.06072100
C       2.85667600   -1.04303100   -0.42481600
H      -0.12511200    1.48940100    0.53293900
H      -0.37267500   -1.52353600    0.58236400
H      -0.10856300   -0.44849100    1.94999400
H      -2.48637600   -0.06286600    2.18780300
H      -2.60920800   -1.60562500    1.36092100
H       0.71306600    1.07839500   -1.76205100
H       0.43600200   -0.65515700   -1.56873400
H      -1.94514800    1.39917700   -1.48518700
H      -3.80688800    0.18133100   -0.18194200
H       2.48037400   -1.94746900   -0.92550700
H       3.41593800    0.88071000    0.52217100
""",
)

entry(
    index = 226,
    label = "P272",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {6,D} {16,S}
6  C u0 p0 c0 {4,S} {5,D} {17,S}
7  C u0 p0 c0 {3,S} {8,D} {18,S}
8  C u0 p0 c0 {7,D} {19,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 O u0 p2 c0 {8,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81312,0.0430296,2.45957e-05,-4.86371e-08,1.76056e-11,-2672.98,13.3167], Tmin=(10,'K'), Tmax=(1078.17,'K')),
            NASAPolynomial(coeffs=[8.57303,0.0526341,-2.66972e-05,6.53278e-09,-6.25269e-13,-5284,-17.3541], Tmin=(1078.17,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-22.1281,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (453.139,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 10, 'C-C': 6, 'C=C': 2, 'C=O': 1}
1D rotors:
* Invalidated! pivots: [2, 4], dihedral: [3, 2, 4, 8], invalidation reason: Another conformer for C8H10O[155] exists which is 0.97 kJ/mol lower.Another conformer for C8H10O[155] exists which is 0.97 kJ/mol lower.
pivots: [4, 8], dihedral: [2, 4, 8, 9], rotor symmetry: 1, max scan energy: 8.52 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.03483600    4.38102000    0.43893500
C      -0.24103500   -0.01721100   -0.02437300
C      -1.08904800   -0.95487200   -0.92790200
C       0.45305800    1.11201000   -0.81269000
C      -2.33278900   -1.34036500   -0.08814200
C      -1.24880200    0.44943600    1.00427100
C      -2.37619100   -0.25819100    0.96543300
C       1.38135900    1.96395000    0.03140300
C       1.19857800    3.24289400    0.25107500
H       0.54659900   -0.59449500    0.48306200
H      -1.41046700   -0.39728900   -1.81393600
H      -0.52496900   -1.82186400   -1.27811700
H       1.02950700    0.66615300   -1.63218800
H      -0.31062100    1.74223300   -1.27874400
H      -2.21673400   -2.32664000    0.38048100
H      -3.24648200   -1.39049400   -0.68870200
H      -1.03425200    1.24809700    1.70475800
H      -3.22189900   -0.11810300    1.62948100
H       2.25603900    1.51988000    0.49399700
""",
)

entry(
    index = 227,
    label = "P273",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {6,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {6,S} {16,S} {17,S}
5  C u0 p0 c0 {7,S} {8,S} {9,S} {18,S}
6  C u0 p0 c0 {3,S} {4,S} {7,D}
7  C u0 p0 c0 {5,S} {6,D} {19,S}
8  O u0 p2 c0 {5,S} {21,S}
9  C u1 p0 c0 {5,S} {20,D}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {7,S}
20 O u0 p2 c0 {9,D}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.46529,0.0659162,-1.97107e-05,-1.03578e-08,5.65246e-12,-18811.8,14.9598], Tmin=(10,'K'), Tmax=(1191.93,'K')),
            NASAPolynomial(coeffs=[13.4038,0.0514153,-2.51861e-05,5.97399e-09,-5.56158e-13,-22520.1,-40.3503], Tmin=(1191.93,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-156.396,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (498.868,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 10, 'C-C': 7, 'C=C': 1, 'H-O': 1, 'C=O': 1, 'C-O': 1}
1D rotors:
pivots: [1, 7], dihedral: [21, 1, 7, 9], rotor symmetry: 1, max scan energy: 10.23 kJ/mol
* Invalidated! pivots: [7, 9], dihedral: [1, 7, 9, 8], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [7, 10], dihedral: [1, 7, 10, 2], rotor symmetry: 1, max scan energy: 14.35 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       3.26192600    0.65326400   -1.38281500
O       2.44044600   -0.71864300    1.82142200
C      -1.97134200    0.88950100    1.12480900
C      -2.51968100    0.54597700   -0.27157100
C      -0.44732000    1.02859100    0.91029800
C      -1.44215600   -0.38811200   -0.85185200
C       2.34758100    0.51074400   -0.31986500
C      -0.13998600    0.17002200   -0.30914100
C       1.06293300   -0.03771700   -0.84991900
C       2.94704100   -0.41128200    0.80502500
H      -2.42138100    1.78650400    1.55503000
H      -2.17377300    0.06180900    1.81237400
H      -3.51145800    0.08962700   -0.24285400
H      -2.59074000    1.45416400   -0.88002900
H       0.13008100    0.72261800    1.78533200
H      -0.17992700    2.07255700    0.70003900
H      -1.45042800   -0.45392100   -1.94197600
H      -1.59201600   -1.40450600   -0.46413700
H       2.18797400    1.46312400    0.21142300
H       1.17877500   -0.66131100   -1.73134100
H       4.15014000    0.67893800   -1.00906600
""",
)

entry(
    index = 228,
    label = "P274",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {6,S} {9,S}
4  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
5  O u0 p2 c0 {2,S} {15,S}
6  C u1 p0 c0 {3,S} {13,D}
7  O u0 p2 c0 {4,S} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 O u0 p2 c0 {6,D}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.58224,0.0362705,7.11644e-05,-1.99655e-07,1.39867e-10,-33212.9,13.1445], Tmin=(10,'K'), Tmax=(487.199,'K')),
            NASAPolynomial(coeffs=[3.09832,0.0555705,-3.54462e-05,1.07997e-08,-1.25963e-12,-33347.7,13.2643], Tmin=(487.199,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-276.185,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (353.365,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C-C': 5, 'H-O': 2, 'C=O': 1, 'C-H': 5}
1D rotors:
* Invalidated! pivots: [1, 5], dihedral: [15, 1, 5, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 7], dihedral: [14, 2, 7, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 7], dihedral: [5, 4, 7, 2], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
pivots: [6, 8], dihedral: [4, 6, 8, 3], rotor symmetry: 1, max scan energy: 22.81 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       0.45160100    1.83357300   -0.10566500
O      -1.33746400    1.86344200    2.05021600
O      -2.50109300   -0.20868800   -2.57061900
C      -1.35797000    0.20105900    0.22407200
C      -0.42948100    0.90892900   -0.68490700
C      -1.93094500    1.24122600   -0.74975800
C      -1.38962900    0.48794600    1.71983900
C      -2.67969500    0.77646800   -1.93007500
H      -1.56720300   -0.83181600   -0.03918700
H      -2.23374200    2.17532000   -0.29597700
H      -0.03451100    0.36595600   -1.53986800
H      -0.56816600   -0.06977600    2.19330700
H      -2.32561900    0.10669900    2.13473100
H      -0.52323800    2.20908200    1.66245800
H       0.67776500    2.49957100   -0.76403100
""",
)

entry(
    index = 229,
    label = "P275",
    molecule = 
"""
multiplicity 3
1  O u0 p2 c0 {6,S} {13,S}
2  O u1 p2 c0 {5,S}
3  C u1 p0 c0 {4,S} {5,S} {8,S}
4  C u0 p0 c0 {3,S} {6,D} {9,S}
5  C u0 p0 c0 {2,S} {3,S} {7,D}
6  C u0 p0 c0 {1,S} {4,D} {10,S}
7  C u0 p0 c0 {5,D} {11,S} {12,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84684,0.0111887,0.000167053,-3.88513e-07,2.78003e-10,-6963.62,12.2235], Tmin=(10,'K'), Tmax=(447.306,'K')),
            NASAPolynomial(coeffs=[1.70597,0.0505338,-3.26278e-05,1.00534e-08,-1.184e-12,-6974.19,18.5706], Tmin=(447.306,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-57.9142,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C-C': 2, 'H-O': 1, 'C-H': 5, 'C=C': 2}
1D rotors:
* Invalidated! pivots: [1, 6], dihedral: [13, 1, 6, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 4], dihedral: [5, 3, 4, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 5], dihedral: [4, 3, 5, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [5, 7], dihedral: [2, 5, 7, 11], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 6], dihedral: [3, 4, 6, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
O      -1.54255800    0.36053800   -1.78241500
O      -0.54881300    2.62186600   -1.13458300
C      -1.39871900    1.84013500    0.95611300
C      -1.94492500    0.59809000    0.60205800
C      -0.73270200    2.79642900    0.10664200
C      -2.00564900   -0.05529400   -0.62003900
C      -0.23380800    4.03466200    0.66821300
H      -1.48560800    2.12174100    1.99963800
H      -2.40260000    0.03982300    1.41275600
H      -2.48221600   -1.02870200   -0.67583000
H      -0.34127700    4.27782200    1.71756700
H       0.26066600    4.73009600    0.00413600
H      -1.11513000    1.26539900   -1.65933700
""",
)

entry(
    index = 230,
    label = "P276",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {4,S} {11,S}
4  C u0 p0 c0 {3,S} {5,D} {10,S}
5  C u0 p0 c0 {4,D} {12,S} {13,S}
6  O u0 p2 c0 {1,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u1 p2 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86802,0.0137811,0.000331968,-1.43499e-06,2.12638e-09,-23299.7,10.8509], Tmin=(10,'K'), Tmax=(169.963,'K')),
            NASAPolynomial(coeffs=[2.0928,0.055562,-3.6786e-05,1.14908e-08,-1.36672e-12,-23239.3,16.2692], Tmin=(169.963,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-193.57,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (320.107,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C-C': 2, 'H-O': 1, 'C-H': 6, 'C=C': 2}
1D rotors:
pivots: [1, 3], dihedral: [14, 1, 3, 4], rotor symmetry: 1, max scan energy: 31.16 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [1, 3, 4, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [5, 6], dihedral: [4, 5, 6, 7], rotor symmetry: 2, max scan energy: 67.32 kJ/mol
pivots: [4, 5], dihedral: [2, 4, 5, 6], rotor symmetry: 1, max scan energy: 44.79 kJ/mol
* Invalidated! pivots: [6, 7], dihedral: [5, 6, 7, 12], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
O      -2.76695000    0.08917700    1.22262000
O      -0.81753800   -1.41158300    0.28568400
C      -2.10471200    0.57156100    0.08789800
C      -1.00133300   -0.38113600   -0.35744800
C      -0.21647500   -0.02208500   -1.52729600
C       0.81455900   -0.83725500   -2.00520700
C       1.58228500   -0.54507600   -3.10094300
H      -2.80551100    0.70575200   -0.75071300
H      -1.65338500    1.55668500    0.28342400
H       0.99624400   -1.75466500   -1.45273600
H      -0.44825900    0.90980800   -2.03586900
H       1.42621000    0.36267500   -3.67399800
H       2.36998800   -1.21052400   -3.43095700
H      -2.33019800   -0.75334100    1.42929800
""",
)

entry(
    index = 231,
    label = "P277",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {5,D}
2  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
4  C u1 p0 c0 {2,S} {3,S} {9,S}
5  C u0 p0 c0 {1,D} {2,S} {10,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93179,0.00432602,0.000116474,-2.38381e-07,1.52556e-10,19112.7,10.722], Tmin=(10,'K'), Tmax=(489.676,'K')),
            NASAPolynomial(coeffs=[1.55297,0.0369119,-2.36388e-05,7.23415e-09,-8.47862e-13,19188,18.8896], Tmin=(489.676,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (158.894,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (228.648,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 4, 'C-H': 5, 'C=O': 1}
1D rotors:
pivots: [2, 5], dihedral: [3, 2, 5, 1], rotor symmetry: 1, max scan energy: 25.56 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       2.58831200    0.18854800   -0.07791200
C       0.22228800    0.48910200    0.00265100
C      -0.98631700   -0.32274900    0.54739100
C      -0.97330700    0.18262400   -0.81274800
C       1.48408000   -0.26937100   -0.22651100
H       0.38015200    1.50523400    0.35455700
H      -0.80442600   -1.38200800    0.72190800
H      -1.61549200    0.14568900    1.30011400
H      -1.62912900    0.83068700   -1.37426500
H       1.33138500   -1.32349700   -0.54930600
""",
)

entry(
    index = 232,
    label = "P278",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u1 p0 c0 {1,S} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {5,D} {9,S}
4  C u0 p0 c0 {1,S} {10,D} {11,S}
5  C u0 p0 c0 {3,D} {12,S} {13,S}
6  O u0 p2 c0 {1,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 O u0 p2 c0 {4,D}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.6383,0.0311762,5.33846e-05,-1.28261e-07,7.61659e-11,-18549.5,13.112], Tmin=(10,'K'), Tmax=(569.213,'K')),
            NASAPolynomial(coeffs=[2.59485,0.0509169,-3.13348e-05,9.25932e-09,-1.05334e-12,-18631.8,15.7923], Tmin=(569.213,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-154.274,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 3, 'C-O': 1, 'C=O': 1, 'H-O': 1, 'C-H': 6, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [1, 3], dihedral: [14, 1, 3, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 4], dihedral: [1, 3, 4, 5], invalidation reason: Another conformer for C5H7O2[4790] exists which is 1.39 kJ/mol lower.Another conformer for C5H7O2[4790] exists which is 1.39 kJ/mol lower.
* Invalidated! pivots: [3, 6], dihedral: [1, 3, 6, 2], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 7], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [5, 7], dihedral: [4, 5, 7, 12], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.07911200   -1.29861900   -0.11025900
O      -3.11114400    0.34575200    0.32910200
C      -0.81734900   -0.20165300    0.72340300
C       0.27789300    0.69316800    0.20585400
C       0.79712000    0.60285600   -1.07448700
C      -2.08421700    0.64039600    0.88867600
C       1.79049200    1.41799200   -1.57965300
H      -0.54262200   -0.55034100    1.73615700
H       0.65313200    1.44765700    0.89293500
H       0.39358900   -0.18371700   -1.70487000
H      -2.00269800    1.53757400    1.53073100
H       2.23122800    2.20929300   -0.98297200
H       2.16290700    1.28897600   -2.58761600
H      -2.01552400   -1.22651100   -0.35550200
""",
)

entry(
    index = 233,
    label = "P279",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u1 p0 c0 {1,S} {4,S} {12,S}
4  C u0 p0 c0 {3,S} {5,D} {7,S}
5  C u0 p0 c0 {4,D} {6,S} {13,S}
6  O u0 p2 c0 {1,S} {5,S}
7  O u0 p2 c0 {4,S} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82341,0.012269,0.000199727,-4.96145e-07,3.73928e-10,-21313.1,12.2585], Tmin=(10,'K'), Tmax=(440.857,'K')),
            NASAPolynomial(coeffs=[2.96778,0.0502317,-3.21923e-05,9.94652e-09,-1.17926e-12,-21531.1,12.3573], Tmin=(440.857,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-177.222,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (324.264,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 3, 'C-C': 3, 'H-O': 1, 'C-H': 6, 'C=C': 1}
1D rotors:
pivots: [2, 6], dihedral: [14, 2, 6, 5], rotor symmetry: 1, max scan energy: 13.02 kJ/mol
pivots: [3, 4], dihedral: [1, 3, 4, 9], rotor symmetry: 3, max scan energy: 13.71 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.62060800   -0.27530300    0.55160000
O       2.54109500   -0.16649200   -1.08092700
C       0.01881500    0.70607800    1.42915000
C      -0.06648700    0.20545000    2.86882000
C       1.40058000    0.86047800    0.86364300
C       1.49238500    0.04171200   -0.23843500
C       0.27551600   -0.62410000   -0.41156900
H      -0.57616200    1.62694800    1.33394000
H       0.48680700   -0.72960200    2.97775100
H       0.36260000    0.94723800    3.54843500
H      -1.10824900    0.03746300    3.15209300
H       2.15620700    1.51531600    1.27167500
H      -0.03547600   -1.34602400   -1.14760100
H       3.27525600    0.38929600   -0.80274200
""",
)

entry(
    index = 234,
    label = "P280",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {3,D} {7,S} {12,S}
5  C u1 p0 c0 {1,S} {13,D}
6  O u0 p2 c0 {2,S} {14,S}
7  O u0 p2 c0 {4,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 O u0 p2 c0 {5,D}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.4992,0.0470814,-9.11118e-06,-1.86867e-08,9.91859e-12,-36605.8,14.1216], Tmin=(10,'K'), Tmax=(927.993,'K')),
            NASAPolynomial(coeffs=[6.84831,0.044739,-2.48729e-05,6.67959e-09,-6.98281e-13,-37748.1,-4.5914], Tmin=(927.993,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-304.384,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (357.522,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C-C': 3, 'H-O': 2, 'C=O': 1, 'C-H': 5, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [1, 5], dihedral: [14, 1, 5, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 7], dihedral: [15, 2, 7, 6], invalidation reason: 
* Invalidated! pivots: [4, 5], dihedral: [6, 4, 5, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 6], dihedral: [5, 4, 6, 7], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 8], dihedral: [5, 4, 8, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.10532500   -0.87047900   -1.69527500
O       2.34551600   -0.37191100   -0.59025200
O      -1.57926100    2.19943300    1.64620500
C      -0.45090700    0.82156200   -0.03235700
C      -1.02998200   -0.44230200   -0.68240300
C       0.72444000    0.63346500    0.90489400
C       1.92618200    0.13463000    0.58750000
C      -1.59541000    1.59097200    0.63741800
H      -0.17870800    1.48054300   -0.87400400
H      -1.99707700   -0.20702400   -1.13935900
H      -1.16702000   -1.22260000    0.07357200
H       0.59332700    0.99858400    1.91559800
H       2.71832700    0.11658200    1.32951600
H      -0.32903400   -1.76476300   -1.97080200
H       1.57343800   -0.51617500   -1.17041400
""",
)

entry(
    index = 235,
    label = "P281",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {6,S}
2  O u0 p2 c0 {3,S} {7,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {5,S} {8,S}
5  C u0 p0 c0 {4,S} {6,D} {9,S}
6  C u0 p0 c0 {1,S} {5,D} {10,S}
7  C u1 p0 c0 {2,S} {11,S} {12,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88251,0.00710424,0.000151473,-3.04713e-07,1.8594e-10,-1029.05,12.4835], Tmin=(10,'K'), Tmax=(538.05,'K')),
            NASAPolynomial(coeffs=[1.92865,0.0471462,-3.12937e-05,9.88356e-09,-1.18869e-12,-1188.14,17.2664], Tmin=(538.05,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-8.59861,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 4, 'C-C': 1, 'C=C': 2, 'C-H': 5}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [7, 2, 3, 1], invalidation reason: Another conformer for C5H5O2[2729] exists which is 1.22 kJ/mol lower.Another conformer for C5H5O2[2729] exists which is 1.22 kJ/mol lower.
* Invalidated! pivots: [2, 7], dihedral: [3, 2, 7, 11], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.17423200   -0.47966200    0.63670000
O       1.59295800    0.15912900   -0.71552900
C       0.28026100    0.18131200   -0.45051700
C      -0.73103400    0.78394100   -1.13419600
C      -1.92102800    0.46277500   -0.39940700
C      -1.54290800   -0.29692400    0.65691800
C       2.47549600   -0.45074000    0.13513600
H      -0.63344100    1.37050500   -2.03150300
H      -2.92846700    0.76622600   -0.63597800
H      -2.05925300   -0.76595400    1.47521900
H       3.47146400   -0.49465000   -0.27440000
H       2.09169200   -1.14075300    0.87038700
""",
)

entry(
    index = 236,
    label = "P282",
    molecule = 
"""
1  O u0 p2 c0 {6,D}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {5,S} {11,S}
5  C u0 p0 c0 {4,S} {6,D} {12,S}
6  C u0 p0 c0 {1,D} {5,D}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82882,0.0149203,0.000205833,-7.40829e-07,8.14426e-10,-2603.14,10.2101], Tmin=(10,'K'), Tmax=(304.707,'K')),
            NASAPolynomial(coeffs=[3.753,0.0387309,-2.36956e-05,7.08654e-09,-8.23125e-13,-2704.44,8.74778], Tmin=(304.707,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-21.6127,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 2, 'C-H': 6, 'C=O': 1, 'C=C': 2}
1D rotors:
pivots: [2, 3], dihedral: [7, 2, 3, 4], rotor symmetry: 3, max scan energy: 7.77 kJ/mol
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 22.49 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O       1.35501500   -4.34334200    1.52078900
C      -2.07602800    0.41491900    0.21867900
C      -0.80656200   -0.34688900   -0.01733200
C      -0.47866000   -1.48788200    0.60032000
C       0.75744900   -2.22856200    0.36971200
C       1.07114100   -3.35230300    0.98373600
H      -1.87144800    1.43242200    0.57163500
H      -2.65895100    0.51542100   -0.70427500
H      -2.70717700   -0.07791400    0.96243000
H      -0.11564200    0.07364700   -0.74601500
H      -1.16669500   -1.91038300    1.32863300
H       1.49129800   -1.86699900   -0.34308300
""",
)

entry(
    index = 237,
    label = "P283",
    molecule = 
"""
1  O u0 p2 c0 {3,S} {13,S}
2  O u0 p2 c0 {5,D}
3  C u0 p0 c0 {1,S} {5,S} {6,S} {8,S}
4  C u0 p0 c0 {5,S} {7,S} {9,S} {10,S}
5  C u0 p0 c0 {2,D} {3,S} {4,S}
6  C u0 p0 c0 {3,S} {7,D} {11,S}
7  C u0 p0 c0 {4,S} {6,D} {12,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8879,0.00701235,0.00016391,-3.37668e-07,2.14354e-10,-30367.5,12.0398], Tmin=(10,'K'), Tmax=(506.271,'K')),
            NASAPolynomial(coeffs=[1.23102,0.0507279,-3.29392e-05,1.02035e-08,-1.20736e-12,-30389.7,20.1732], Tmin=(506.271,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-252.523,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 4, 'C-O': 1, 'C=O': 1, 'H-O': 1, 'C-H': 5, 'C=C': 1}
1D rotors:
pivots: [1, 3], dihedral: [13, 1, 3, 5], rotor symmetry: 1, max scan energy: 18.46 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       2.03851200    0.97415500   -0.09615400
O       1.32021700   -1.74745700   -0.46279900
C       0.86558000    0.43699900    0.48115600
C      -1.01538600   -0.99634800   -0.29816700
C       0.50100800   -0.93492700   -0.11926600
C      -0.37906700    1.23488700    0.20281600
C      -1.39605300    0.46080200   -0.18269900
H       1.00043900    0.30692000    1.57057300
H      -1.45816400   -1.61803100    0.49113500
H      -1.27851400   -1.46307200   -1.25205700
H      -0.41886700    2.30738800    0.34320200
H      -2.39612000    0.81733100   -0.39757000
H       2.61641700    0.22134600   -0.28017100
""",
)

entry(
    index = 238,
    label = "P284",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {3,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {1,S} {3,D} {10,S}
5  C u0 p0 c0 {1,S} {11,D} {12,S}
6  O u0 p2 c0 {2,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 O u0 p2 c0 {5,D}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67963,0.03207,1.81929e-05,-4.69625e-08,2.1311e-11,-6434.65,11.8093], Tmin=(10,'K'), Tmax=(835.13,'K')),
            NASAPolynomial(coeffs=[4.6243,0.0414986,-2.38037e-05,6.56879e-09,-7.02855e-13,-7079.01,4.50883], Tmin=(835.13,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-53.5098,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 4, 'H-O': 1, 'C=O': 1, 'C-H': 5, 'C-O': 1, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [1, 4], dihedral: [13, 1, 4, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 7], dihedral: [5, 3, 7, 2], invalidation reason: Inconsistent initial and final conformers But unable to propose troubleshooting methods.Inconsistent initial and final conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 5], dihedral: [1, 4, 5, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       1.44044800    1.49585100   -0.41232100
O      -1.01547900    1.65764600    1.37284500
C      -1.00076200   -0.49256600    0.32983400
C       1.69641800    0.11918900   -0.19986900
C       0.51695900   -0.56646000    0.38160600
C      -0.08916200   -1.28230200    1.25985800
C      -1.62779600    0.76510500    0.82506600
H      -1.57081100   -1.02113800   -0.43571800
H       1.93614300   -0.31078000   -1.17751400
H       2.56084600   -0.04738300    0.45838000
H      -0.10626000   -1.94369500    2.10769000
H      -2.72151000    0.85995400    0.65735100
H       0.94835500    1.82190200    0.35442900
""",
)

entry(
    index = 239,
    label = "P285",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {3,S} {8,S}
2  C u0 p0 c0 {1,D} {4,S} {7,S}
3  C u0 p0 c0 {1,S} {5,D} {9,S}
4  C u0 p0 c0 {2,S} {10,D} {11,S}
5  C u1 p0 c0 {3,D} {6,S}
6  O u0 p2 c0 {5,S} {12,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 O u0 p2 c0 {4,D}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.69061,0.0264242,0.000130295,-4.33342e-07,3.99458e-10,3985.4,12.3243], Tmin=(10,'K'), Tmax=(374.286,'K')),
            NASAPolynomial(coeffs=[4.04381,0.0446005,-3.05206e-05,9.79009e-09,-1.18714e-12,3805.2,8.91348], Tmin=(374.286,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (33.155,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (270.22,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 2, 'H-O': 1, 'C=O': 1, 'C-H': 4, 'C=C': 2, 'C-O': 1}
1D rotors:
pivots: [1, 7], dihedral: [12, 1, 7, 5], rotor symmetry: 1, max scan energy: 12.63 kJ/mol
pivots: [3, 5], dihedral: [4, 3, 5, 7], rotor symmetry: 1, max scan energy: 40.88 kJ/mol
pivots: [4, 6], dihedral: [3, 4, 6, 2], rotor symmetry: 1, max scan energy: 48.37 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       3.15753700   -0.87419600    0.09329200
O      -3.13112100    2.40775800   -1.29822200
C       0.05929900    0.83155100   -0.99727300
C      -1.09268400    1.41181700   -0.60204800
C       1.08824300    0.33722700   -0.11827900
C      -2.07705100    1.87613200   -1.57650100
C       2.21501700   -0.22094800   -0.56459900
H      -1.33417600    1.55697600    0.44681700
H       0.24033900    0.71591800   -2.06440000
H       0.96017800    0.44353400    0.96027500
H      -1.78765800    1.70514700   -2.63886400
H       4.01871200   -0.73457600   -0.32127700
""",
)

entry(
    index = 240,
    label = "P286",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
2  C u0 p0 c0 {3,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {12,D}
4  C u0 p0 c0 {5,D} {7,S} {13,S}
5  C u1 p0 c0 {1,S} {4,D}
6  O u0 p2 c0 {2,S} {14,S}
7  O u0 p2 c0 {4,S} {15,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 O u0 p2 c0 {3,D}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.56985,0.0499894,-2.23871e-05,-3.11771e-10,1.99139e-12,-29666.1,13.7785], Tmin=(10,'K'), Tmax=(1230.3,'K')),
            NASAPolynomial(coeffs=[11.8644,0.0341493,-1.66413e-05,3.92615e-09,-3.63603e-13,-32549.2,-31.3795], Tmin=(1230.3,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-246.66,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (357.522,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 3, 'H-O': 2, 'C=O': 1, 'C-O': 2, 'C-H': 5, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [1, 5], dihedral: [14, 1, 5, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 7], dihedral: [15, 2, 7, 8], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 6], dihedral: [8, 4, 6, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 8], dihedral: [6, 4, 8, 7], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [5, 6], dihedral: [1, 5, 6, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O      -3.86524800    0.00893100    2.24446700
O       0.13805500   -2.84929400   -0.12880300
O      -2.01565000   -1.45400900    1.01860500
C      -1.05464000   -2.44522300    3.01452400
C      -2.90349600   -0.62254400    3.04101800
C      -1.97878300   -1.51623600    2.23262300
C       0.62968400   -3.20013700    1.09660300
C       0.09616500   -2.99172900    2.28227300
H      -3.39210400   -1.21768700    3.82253600
H      -2.25716100    0.10803900    3.55730200
H      -1.70552600   -3.25097300    3.39142600
H      -0.72992300   -1.90349200    3.91349800
H       1.58323400   -3.71200200    1.00101400
H      -3.56784700   -0.09602200    1.32880700
H      -0.69631400   -2.36863500    0.01515100
""",
)

entry(
    index = 241,
    label = "P287",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {6,S} {12,S}
4  C u0 p0 c0 {1,S} {7,D} {11,S}
5  O u0 p2 c0 {2,S} {13,S}
6  O u0 p2 c0 {3,S} {15,S}
7  C u0 p0 c0 {4,D} {14,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 O u0 p2 c0 {7,D}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68894,0.028864,0.000219013,-8.31552e-07,9.31448e-10,-32883.8,13.3393], Tmin=(10,'K'), Tmax=(300.035,'K')),
            NASAPolynomial(coeffs=[3.60431,0.0549042,-3.57189e-05,1.11893e-08,-1.34225e-12,-32990.9,11.7771], Tmin=(300.035,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-273.366,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (353.365,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 3, 'H-O': 2, 'C=O': 1, 'C-O': 2, 'C-H': 5, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [1, 5], dihedral: [14, 1, 5, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 6], dihedral: [15, 2, 6, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 5], dihedral: [6, 4, 5, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 6], dihedral: [5, 4, 6, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [4, 7], dihedral: [5, 4, 7, 8], rotor symmetry: 1, max scan energy: 18.14 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.51280900   -0.92461700    0.78544000
O       0.84569900   -1.52273800    2.12862800
O      -0.42846700   -5.17065800   -1.76726800
C       0.40959300   -2.08955200   -0.22418900
C      -0.68874800   -1.01961700   -0.38759300
C       1.35462600   -1.75134800    0.88608500
C      -0.22760300   -3.47923500    0.02851900
C      -0.34352800   -4.38804800   -0.90751600
H       0.98002600   -2.12464800   -1.15720900
H      -1.30311400   -1.23617700   -1.26789500
H      -0.23455000   -0.03464400   -0.50998400
H      -0.49819600   -3.75089000    1.04110300
H       2.34878600   -2.18253200    0.91203900
H      -2.06988300   -1.71150200    0.80740100
H      -0.06165400   -1.18577500    2.01841800
""",
)

entry(
    index = 242,
    label = "P288",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {8,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {6,S} {9,S} {16,S} {17,S}
6  C u0 p0 c0 {5,S} {7,D} {8,S}
7  C u0 p0 c0 {2,S} {6,D} {18,S}
8  O u0 p2 c0 {3,S} {6,S}
9  O u0 p2 c0 {5,S} {19,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.6956,0.0310058,9.40688e-05,-1.63967e-07,7.72634e-11,-24495.4,12.9021], Tmin=(10,'K'), Tmax=(717.55,'K')),
            NASAPolynomial(coeffs=[1.21084,0.070423,-4.17748e-05,1.18979e-08,-1.3091e-12,-24796.9,19.4787], Tmin=(717.55,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-203.685,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (453.139,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'H-O': 1, 'C-C': 6, 'C-H': 9, 'C-O': 3}
1D rotors:
* Invalidated! pivots: [2, 7], dihedral: [19, 2, 7, 8], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [3, 6], dihedral: [4, 3, 6, 13], rotor symmetry: 3, max scan energy: 6.89 kJ/mol
* Invalidated! pivots: [7, 8], dihedral: [2, 7, 8, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O      -4.10646900   -0.13229100    0.76140600
O      -2.24760400    2.09795700    0.60423100
C      -3.24833000   -2.05536100    2.13032000
C      -3.16675300   -2.31461100    0.61946300
C      -4.28653800   -1.46944300    1.21841500
C      -2.25728700   -1.22034300    2.90787500
C      -2.58778300    1.24837400   -0.49310400
C      -2.97559300   -0.11614300   -0.03526600
C      -2.41329500   -1.31991100   -0.18790200
H      -3.62779200   -2.91713700    2.67287300
H      -3.31963500   -3.32303900    0.25253200
H      -5.33197300   -1.74449600    1.27399600
H      -1.91196500   -0.35563400    2.34073900
H      -2.71441100   -0.85213800    3.83134100
H      -1.38039100   -1.81489400    3.18024700
H      -3.40722800    1.68649400   -1.08056800
H      -1.70450000    1.18608000   -1.12855000
H      -1.53505800   -1.52800900   -0.77972300
H      -3.00763600    2.10096500    1.19646200
""",
)

entry(
    index = 242,
    label = "P289",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {4,D} {6,S} {11,S}
4  C u1 p0 c0 {1,S} {3,D}
5  O u0 p2 c0 {2,S} {12,S}
6  O u0 p2 c0 {3,S} {13,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78236,0.0195797,7.96588e-05,-1.75627e-07,1.1567e-10,-13279.5,11.9198], Tmin=(10,'K'), Tmax=(395.118,'K')),
            NASAPolynomial(coeffs=[0.938888,0.0483662,-2.96257e-05,8.76674e-09,-1.0015e-12,-13054.8,22.9975], Tmin=(395.118,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-110.423,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 2, 'H-O': 2, 'C-O': 2, 'C-H': 5, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [1, 4], dihedral: [12, 1, 4, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 5], dihedral: [13, 2, 5, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 4], dihedral: [6, 3, 4, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 6], dihedral: [4, 3, 6, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.28138000   -1.12704900   -0.78320300
O      -4.69372800    0.09108100   -0.04602600
C      -1.66300600   -0.06980700    1.37350300
C      -1.34910800   -0.25930400   -0.12253900
C      -4.21803600    0.59460200    1.13874200
C      -3.00326600    0.48544400    1.63692800
H      -0.32917400   -0.64306700   -0.24324400
H      -1.42252500    0.69421400   -0.64640200
H      -0.89153100    0.59581100    1.78405700
H      -1.52954900   -1.03124800    1.89215800
H      -4.99782600    1.13239200    1.67039500
H      -2.20736600   -2.00618400   -0.39572900
H      -3.96897500   -0.39817200   -0.47846900
""",
)

entry(
    index = 243,
    label = "P290",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,D} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {4,D} {10,S}
3  C u0 p0 c0 {1,D} {2,S} {8,S}
4  C u0 p0 c0 {2,D} {5,S} {9,S}
5  C u1 p0 c0 {4,S} {6,S} {11,S}
6  O u0 p2 c0 {1,S} {5,S}
7  O u0 p2 c0 {1,S} {12,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86818,0.00759807,0.000148383,-2.87001e-07,1.65124e-10,-15352.2,10.8885], Tmin=(10,'K'), Tmax=(583.874,'K')),
            NASAPolynomial(coeffs=[2.63973,0.0470431,-3.26684e-05,1.0742e-08,-1.33448e-12,-15737.6,11.6248], Tmin=(583.874,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-127.702,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (278.535,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 2, 'H-O': 1, 'C-O': 3, 'C-H': 4, 'C=C': 2}
1D rotors:
pivots: [2, 3], dihedral: [12, 2, 3, 1], rotor symmetry: 1, max scan energy: 17.88 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O       0.57507900   -1.18933700    0.54621100
O       2.47738400   -0.00792800    0.65348200
C       1.16099900    0.03293000    0.38047200
C      -0.91213200    1.05504200   -0.27127500
C       0.49063700    1.14127700   -0.01040200
C      -1.52311900   -0.19905800   -0.10318300
C      -0.80027900   -1.28281700    0.29250300
H       1.04554500    2.06340800   -0.11284600
H      -2.58251900   -0.33732800   -0.28326300
H      -1.47338400    1.92276700   -0.58458300
H      -1.15694500   -2.28656100    0.45353600
H       2.69873400   -0.91239800    0.90724800
""",
)

entry(
    index = 244,
    label = "P291",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {5,S} {9,S}
4  C u0 p0 c0 {1,S} {6,D} {10,S}
5  O u0 p2 c0 {3,S} {12,S}
6  C u0 p0 c0 {4,D} {11,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 O u0 p2 c0 {6,D}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.47965,0.0441433,-2.74146e-05,4.1392e-09,1.7603e-12,-8325.87,11.2906], Tmin=(10,'K'), Tmax=(904.415,'K')),
            NASAPolynomial(coeffs=[7.33607,0.0330638,-1.8951e-05,5.20694e-09,-5.54512e-13,-9267.86,-8.27824], Tmin=(904.415,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-69.2784,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (270.22,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 2, 'H-O': 1, 'C=O': 1, 'C-H': 4, 'C=C': 2, 'C-O': 1}
1D rotors:
pivots: [1, 5], dihedral: [12, 1, 5, 4], rotor symmetry: 2, max scan energy: 14.65 kJ/mol
pivots: [3, 4], dihedral: [6, 3, 4, 5], rotor symmetry: 2, max scan energy: 61.50 kJ/mol
pivots: [3, 6], dihedral: [4, 3, 6, 7], rotor symmetry: 1, max scan energy: 34.57 kJ/mol
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [6, 7], dihedral: [3, 6, 7, 2], invalidation reason: 


External symmetry: 1, optical isomers: 1

Geometry:
O       2.44566700    0.94863900   -0.69152300
O       1.13721300   -3.68770600   -4.50090300
C       1.67816600   -1.64266500   -1.67601900
C       1.74260900   -1.29476900   -0.32310100
C       2.10614800   -0.06538600    0.16239300
C       1.29021500   -2.94764700   -2.12635700
C       1.21122700   -3.33401400   -3.39421300
H       1.93194300   -0.89532300   -2.41762500
H       1.48861300   -2.04239000    0.42269900
H       2.13875300    0.14933500    1.22415500
H       1.02909400   -3.72136100   -1.40951800
H       2.67101400    1.73191500   -0.18374600
""",
)

entry(
    index = 245,
    label = "P292",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,D} {7,S}
3  C u0 p0 c0 {2,D} {8,S} {9,S}
4  C u1 p0 c0 {1,S} {10,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.55076,0.0455292,-0.000139113,2.93868e-07,-2.23663e-10,7414.5,11.8333], Tmin=(10,'K'), Tmax=(441.259,'K')),
            NASAPolynomial(coeffs=[3.01464,0.0300012,-1.7021e-05,4.69895e-09,-5.06116e-13,7660.3,16.2303], Tmin=(441.259,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (61.6375,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (224.491,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 2, 'C=O': 1, 'C-H': 5, 'C=C': 1}
1D rotors:
pivots: [2, 3], dihedral: [5, 2, 3, 4], rotor symmetry: 1, max scan energy: 8.15 kJ/mol
pivots: [2, 5], dihedral: [3, 2, 5, 1], rotor symmetry: 1, max scan energy: 7.33 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       2.16054300    1.28902700    0.50493100
C       0.73899600   -0.61640000   -0.07178500
C      -0.52267400    0.16364600    0.16148000
C      -1.52904400    0.23169400   -0.70397500
C       2.01767600    0.22945700    0.00707600
H       0.88844700   -1.38767700    0.69625900
H       0.73299700   -1.13635600   -1.03228300
H      -0.57086300    0.71571400    1.09595900
H      -2.41722900    0.81614100   -0.49321400
H      -1.50463500   -0.29599700   -1.65270300
""",
)

entry(
    index = 246,
    label = "P293",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {7,S} {11,S}
2  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
3  C u0 p0 c0 {4,S} {10,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {5,D} {9,S}
5  C u0 p0 c0 {1,S} {4,D} {17,S}
6  C u0 p0 c0 {2,S} {8,D} {16,S}
7  C u1 p0 c0 {1,S} {9,S} {18,S}
8  C u0 p0 c0 {6,D} {19,S} {20,S}
9  O u0 p2 c0 {4,S} {7,S}
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
            NASAPolynomial(coeffs=[3.27156,0.0713001,-3.01573e-05,-3.64388e-09,4.34742e-12,-8349.45,14.9594], Tmin=(10,'K'), Tmax=(1112.17,'K')),
            NASAPolynomial(coeffs=[11.4468,0.0562223,-2.9142e-05,7.32872e-09,-7.22343e-13,-11053.9,-29.3336], Tmin=(1112.17,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-69.453,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (498.868,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'H-O': 1, 'C-C': 5, 'C-H': 10, 'C-O': 3}
1D rotors:
pivots: [2, 5], dihedral: [21, 2, 5, 6], rotor symmetry: 1, max scan energy: 15.20 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [7, 3, 4, 8], invalidation reason: 
pivots: [4, 8], dihedral: [3, 4, 8, 10], rotor symmetry: 1, max scan energy: 15.88 kJ/mol
* Invalidated! pivots: [5, 6], dihedral: [2, 5, 6, 1], invalidation reason: Another conformer for C8H11O2[92] exists which is 0.65 kJ/mol lower.Another conformer for C8H11O2[92] exists which is 0.65 kJ/mol lower.


External symmetry: 1, optical isomers: 2

Geometry:
O       1.36001400    1.31160300    0.20743600
O       3.94275700    0.36074700    1.10457300
C       0.05726500    0.03182800   -1.30952800
C       0.21357500   -0.18827700   -2.84451300
C       2.71306200   -0.29461700    1.39888100
C       1.66987100   -0.03563600    0.36459900
C       0.97273400   -0.81967400   -0.45729700
C      -0.27100200   -1.53673000   -3.29353400
C       0.46785900    1.39832600   -0.84357500
C       0.47813100   -2.46472400   -3.88234200
H      -1.00264000   -0.17119300   -1.06764800
H       1.26217100   -0.04555100   -3.11884700
H      -0.36410300    0.59427200   -3.35237300
H       2.92418400   -1.36343300    1.44094300
H       2.33209000    0.01661800    2.38281400
H      -1.32277000   -1.75058400   -3.10487100
H       1.05343100   -1.89356000   -0.52430400
H      -0.09113000    2.32130100   -0.88828500
H       0.06639100   -3.42118800   -4.18473400
H       1.53079600   -2.29747800   -4.08993300
H       3.74006300    1.29420100    0.97990600
""",
)

entry(
    index = 247,
    label = "P294",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {6,S} {11,S}
4  C u0 p0 c0 {1,S} {9,S} {12,S} {13,S}
5  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
6  C u0 p0 c0 {3,S} {7,D} {17,S}
7  C u0 p0 c0 {6,D} {8,S} {18,S}
8  O u0 p2 c0 {1,S} {7,S}
9  O u0 p2 c0 {4,S} {19,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68256,0.0270828,0.00016828,-3.91577e-07,2.73766e-10,-25276.1,12.8921], Tmin=(10,'K'), Tmax=(441.259,'K')),
            NASAPolynomial(coeffs=[0.135427,0.0748631,-4.72603e-05,1.43181e-08,-1.66534e-12,-25115.2,25.3792], Tmin=(441.259,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-210.176,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (448.981,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'H-O': 1, 'C-C': 6, 'C-H': 9, 'C-O': 3}
1D rotors:
pivots: [2, 6], dihedral: [19, 2, 6, 3], rotor symmetry: 1, max scan energy: 17.04 kJ/mol
* Invalidated! pivots: [3, 6], dihedral: [1, 3, 6, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [4, 7], dihedral: [3, 4, 7, 14], rotor symmetry: 3, max scan energy: 4.45 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -3.76148200   -1.96964900   -0.10141300
O      -0.91850000   -2.44295500    0.07260400
C      -2.79068400   -0.91535600   -0.20747800
C      -3.30924200    0.48091500   -0.39930600
C      -2.89984300   -0.35590700   -1.62213500
C      -1.54198100   -1.26077900    0.55235100
C      -4.72543000    0.90137000   -0.08524500
C      -3.94453800   -1.21327300   -2.24147500
C      -4.38800800   -2.07286000   -1.32165100
H      -2.56084400    1.22931700   -0.15139600
H      -2.03030900   -0.05283300   -2.19402100
H      -0.81558500   -0.45311400    0.44326200
H      -1.78726400   -1.35056800    1.62119300
H      -4.85778000    1.03483700    0.99241500
H      -5.45379200    0.16258000   -0.42068400
H      -4.96092600    1.85094300   -0.57469300
H      -4.28332700   -1.15533700   -3.26445000
H      -5.15654600   -2.83014800   -1.37030500
H      -1.59209600   -3.13167200    0.08898200
""",
)

entry(
    index = 248,
    label = "P295",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {4,D} {5,S} {6,S}
3  C u1 p0 c0 {1,S} {4,S} {9,S}
4  C u0 p0 c0 {2,D} {3,S} {10,S}
5  C u0 p0 c0 {2,S} {11,D} {12,S}
6  O u0 p2 c0 {1,S} {2,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 O u0 p2 c0 {5,D}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90927,0.005385,0.000143185,-2.70673e-07,1.57631e-10,-14304.8,11.4752], Tmin=(10,'K'), Tmax=(545.608,'K')),
            NASAPolynomial(coeffs=[0.497656,0.0499477,-3.30792e-05,1.03765e-08,-1.24066e-12,-14223.5,23.2006], Tmin=(545.608,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-118.973,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (278.535,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 3, 'C=O': 1, 'C-O': 2, 'C-H': 5, 'C=C': 1}
1D rotors:
pivots: [4, 7], dihedral: [1, 4, 7, 2], rotor symmetry: 1, max scan energy: 77.32 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O       0.54620900   -1.06794000    0.12014300
O       1.99884900    1.76774600   -1.44446500
C      -0.75661100   -1.21972800    0.72953600
C       0.64765800    0.20484200   -0.34589100
C      -1.40681700    0.11871700    0.56422000
C      -0.54025100    0.93739400   -0.07936400
C       1.84843500    0.63092600   -1.00255400
H      -0.61241200   -1.51731200    1.77573500
H      -1.28159100   -2.03502500    0.21614600
H      -2.40186400    0.35254500    0.91354900
H      -0.67794800    1.96934100   -0.36284100
H       2.63634200   -0.14150600   -1.08421200
""",
)

entry(
    index = 249,
    label = "P296",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {2,S} {3,D} {10,S}
5  O u0 p2 c0 {1,S} {2,S}
6  C u1 p0 c0 {1,S} {12,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91318,0.00579966,0.000158587,-3.436e-07,2.35209e-10,-4435.89,13.0724], Tmin=(10,'K'), Tmax=(450.126,'K')),
            NASAPolynomial(coeffs=[0.819675,0.0479691,-3.08557e-05,9.42747e-09,-1.10077e-12,-4306.1,23.8756], Tmin=(450.126,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-36.8943,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 3, 'C=O': 1, 'C-O': 2, 'C-H': 5, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [3, 7], dihedral: [1, 3, 7, 2], invalidation reason: Another conformer for C5H5O2[95] exists which is 2.25 kJ/mol lower.Another conformer for C5H5O2[95] exists which is 2.25 kJ/mol lower.


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.21683900   -1.17188900    0.63972000
O       3.07356500    0.12871200    0.05871800
C       0.73287400   -0.13299300    0.70448400
C      -1.25770400   -0.81818100   -0.28305800
C       0.11326400    1.03237900   -0.01679600
C      -1.01154600    0.62964800   -0.59843100
C       2.08943900   -0.51745700    0.00920900
H       0.99767800    0.06358100    1.75113900
H      -2.22600200   -0.99722800    0.19777900
H      -1.20273200   -1.45103900   -1.17975400
H      -1.66906800    1.22746700   -1.21559100
H       0.57687300    2.00729700   -0.06802400
""",
)

entry(
    index = 250,
    label = "P297",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {11,S}
2  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
3  C u0 p0 c0 {4,S} {10,S} {14,S} {15,S}
4  C u1 p0 c0 {1,S} {3,S} {9,S}
5  C u0 p0 c0 {1,S} {7,D} {17,S}
6  C u0 p0 c0 {2,S} {8,D} {16,S}
7  C u0 p0 c0 {5,D} {9,S} {18,S}
8  C u0 p0 c0 {6,D} {19,S} {20,S}
9  O u0 p2 c0 {4,S} {7,S}
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
            NASAPolynomial(coeffs=[3.62552,0.0565281,1.31406e-05,-4.56784e-08,1.80702e-11,-8865.52,14.6852], Tmin=(10,'K'), Tmax=(1043.83,'K')),
            NASAPolynomial(coeffs=[9.72201,0.0604618,-3.1737e-05,8.0357e-09,-7.94496e-13,-11625.3,-22.1114], Tmin=(1043.83,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-73.6384,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (507.183,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'H-O': 1, 'C-C': 5, 'C-H': 10, 'C-O': 3}
1D rotors:
* Invalidated! pivots: [2, 5], dihedral: [21, 2, 5, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 4], dihedral: [6, 3, 4, 8], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 8], dihedral: [3, 4, 8, 10], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [5, 6], dihedral: [2, 5, 6, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.01709600    0.70923200   -0.13779300
O      -3.15010300   -0.54966100   -0.76179000
C      -1.61777000    2.40523200   -0.59244300
C      -2.52063300    2.51662700   -1.86990400
C      -2.30332600   -0.06228800    0.30106500
C      -1.36989800    1.00699500   -0.10535400
C      -0.19083000    2.87332100   -0.78694800
C      -1.97563000    1.81560400   -3.08056300
C       0.63318400    1.85937900   -0.52704500
C      -2.61761400    0.87633500   -3.77223200
H      -2.13081900    3.00352100    0.18003100
H      -3.51192100    2.12687400   -1.62801000
H      -2.63450600    3.58608300   -2.09161600
H      -1.72116800   -0.87852100    0.74621600
H      -3.00774100    0.30011900    1.05732700
H      -0.98030700    2.11759200   -3.40002800
H       0.10396900    3.86280400   -1.10277800
H       1.70863400    1.77884400   -0.56128600
H      -3.61269600    0.54488900   -3.49150100
H      -2.17751400    0.42002100   -4.65232000
H      -2.58620600   -0.68513900   -1.53238600
""",
)

entry(
    index = 251,
    label = "P298",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {10,S} {13,S} {14,S}
4  C u1 p0 c0 {1,S} {6,S} {16,S}
5  C u0 p0 c0 {2,S} {8,D} {15,S}
6  C u0 p0 c0 {4,S} {7,D} {17,S}
7  C u0 p0 c0 {6,D} {9,S} {18,S}
8  C u0 p0 c0 {5,D} {19,S} {20,S}
9  O u0 p2 c0 {1,S} {7,S}
10 O u0 p2 c0 {3,S} {21,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68735,0.0210309,0.000318955,-7.6729e-07,5.51704e-10,-16438.3,16.2974], Tmin=(10,'K'), Tmax=(468.028,'K')),
            NASAPolynomial(coeffs=[2.95197,0.0825219,-5.50518e-05,1.74778e-08,-2.10567e-12,-16974.1,12.8273], Tmin=(468.028,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-136.728,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (494.711,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'H-O': 1, 'C-C': 5, 'C-H': 10, 'C-O': 3}
1D rotors:
pivots: [2, 5], dihedral: [21, 2, 5, 3], rotor symmetry: 1, max scan energy: 20.00 kJ/mol
pivots: [3, 4], dihedral: [1, 3, 4, 7], rotor symmetry: 1, max scan energy: 19.12 kJ/mol
* Invalidated! pivots: [3, 5], dihedral: [1, 3, 5, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [4, 7], dihedral: [3, 4, 7, 10], rotor symmetry: 1, max scan energy: 17.33 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       0.31344500   -1.50253400   -2.98660400
O       0.19280000   -2.48250500   -0.31166000
C       0.26857600   -0.56182000   -1.84892300
C       1.74088700   -0.25447100   -1.47676400
C      -0.48420500   -1.30921000   -0.73105500
C      -0.50238600    0.60578200   -2.39632300
C       1.89086100    0.64770100   -0.28496000
C      -0.86478600    0.31289500   -3.69996600
C      -0.37338800   -0.93962700   -4.02119400
C       2.31735100    1.90707200   -0.33330400
H       2.22368000   -1.21448000   -1.27279300
H       2.21914800    0.18662400   -2.35448400
H      -1.49458600   -1.53382300   -1.09468300
H      -0.57567000   -0.66587400    0.14640100
H       1.63592700    0.21306200    0.67920900
H      -0.69368200    1.51110200   -1.84239500
H      -1.42463800    0.94548800   -4.37356600
H      -0.42878600   -1.52140600   -4.92737000
H       2.59425900    2.37811400   -1.27174200
H       2.41439100    2.50925900    0.56321600
H       0.28018200   -3.04296400   -1.09122100
""",
)

entry(
    index = 252,
    label = "P299",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {3,S} {6,S}
3 C u0 p0 c0 {1,S} {2,S} {4,D}
4 C u0 p0 c0 {1,S} {3,D} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94464,0.00310318,6.27025e-05,-1.17085e-07,6.45388e-11,1949.53,8.39242], Tmin=(10,'K'), Tmax=(608.826,'K')),
            NASAPolynomial(coeffs=[3.18733,0.0215519,-1.59453e-05,5.38231e-09,-6.75307e-13,1792.04,9.6195], Tmin=(608.826,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (16.1841,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (128.874,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C-O': 3, 'C-H': 1, 'C=C': 1}
1D rotors:
pivots: [2, 3], dihedral: [6, 2, 3, 1], rotor symmetry: 1, max scan energy: 44.16 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.31686200   -0.48046100    1.33877200
O       1.26136200    0.30113200   -0.12089200
C       0.06146200   -0.15266100    0.21199400
C      -0.99360600   -0.51955300   -0.64239400
H      -1.77569100    0.24917800   -0.67031700
H       1.80695700    0.31494900    0.68202600
""",
)

entry(
    index = 253,
    label = "P300",
    molecule = 
"""
multiplicity 3
1 O u0 p2 c0 {4,S} {6,S}
2 O u1 p2 c0 {3,S}
3 C u0 p0 c0 {2,S} {4,D} {5,S}
4 C u1 p0 c0 {1,S} {3,D}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93636,0.00354142,6.16892e-05,-1.17767e-07,6.53007e-11,4420.5,8.22025], Tmin=(10,'K'), Tmax=(621.267,'K')),
            NASAPolynomial(coeffs=[3.96663,0.0192092,-1.44384e-05,5.02101e-09,-6.47663e-13,4110.61,5.62488], Tmin=(621.267,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (36.7251,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (128.874,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C-O': 2, 'C-H': 1, 'C=C': 1}
1D rotors:
pivots: [1, 4], dihedral: [6, 1, 4, 3], rotor symmetry: 2, max scan energy: 20.55 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
O      -1.51054900   -0.48935500    0.26138900
O       0.60664700    1.12744900   -0.39270100
C       0.84605600    0.05068000    0.17812800
C      -0.26324200   -0.78021100    0.51252900
H       1.85459400   -0.28964500    0.43501800
H      -1.53350500    0.38108200   -0.18607300
""",
)

entry(
    index = 254,
    label = "P301",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {3,S} {4,S}
2  C u0 p0 c0 {1,D} {5,S} {7,S}
3  C u0 p0 c0 {1,S} {6,D} {8,S}
4  C u1 p0 c0 {1,S} {9,S} {10,S}
5  O u0 p2 c0 {2,S} {12,S}
6  C u0 p0 c0 {3,D} {11,D}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 O u0 p2 c0 {6,D}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67935,0.0266531,0.000163415,-5.78689e-07,5.6306e-10,-6264.25,12.1592], Tmin=(10,'K'), Tmax=(367.283,'K')),
            NASAPolynomial(coeffs=[5.3736,0.0407636,-2.71983e-05,8.68485e-09,-1.05587e-12,-6608.33,2.69256], Tmin=(367.283,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-52.056,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (278.535,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 2, 'H-O': 1, 'C=O': 1, 'C-H': 4, 'C=C': 2, 'C-O': 1}
1D rotors:
* Invalidated! pivots: [1, 4], dihedral: [12, 1, 4, 3], invalidation reason: Another conformer for C5H5O2[105] exists which is 3.13 kJ/mol lower.Another conformer for C5H5O2[105] exists which is 3.13 kJ/mol lower.
pivots: [3, 5], dihedral: [4, 3, 5, 7], rotor symmetry: 1, max scan energy: 20.17 kJ/mol
* Invalidated! pivots: [3, 6], dihedral: [4, 3, 6, 10], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 4], dihedral: [5, 3, 4, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
O      -1.77820100   -0.53970200    1.41977200
O       0.60805800   -0.85309800    3.39187100
C      -0.00868000   -0.65961300   -0.16212600
C      -1.36816400   -0.53292500    0.11776500
C       0.95646800   -0.79757400    0.93884700
C       0.44575300   -0.65701400   -1.47212800
C       0.71606500   -0.82129200    2.23648600
H      -2.11709700   -0.42881600   -0.65683200
H       2.00828300   -0.89449500    0.69271400
H       1.49723000   -0.75441800   -1.70431600
H      -0.24529500   -0.55680800   -2.29897900
H      -2.73269500   -0.44551100    1.47432000
""",
)

entry(
    index = 255,
    label = "P302",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {4,D}
3 C u1 p0 c0 {1,S} {2,S} {7,S}
4 C u0 p0 c0 {2,D} {8,S} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96614,0.00201987,8.75233e-05,-1.54455e-07,8.66287e-11,44365.2,8.08782], Tmin=(10,'K'), Tmax=(517.918,'K')),
            NASAPolynomial(coeffs=[0.391141,0.0348847,-2.28778e-05,7.2419e-09,-8.78009e-13,44665.1,22.3027], Tmin=(517.918,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (368.861,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 3, 'C-H': 5, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [2, 4], dihedral: [1, 2, 4, 8], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
C      -0.99771600   -0.72693000    0.00696400
C       0.22420000    0.16078400   -0.00138600
C      -0.97948500    0.76135400   -0.09030400
C       1.58240900    0.20825400    0.05116200
H      -1.30655400   -1.20069000    0.94077200
H      -1.23191800   -1.32051600   -0.87882900
H      -1.57009900    1.65712700   -0.17350200
H       2.10666800    1.15627900    0.01020800
H       2.17249700   -0.69570800    0.13489800
""",
)

entry(
    index = 256,
    label = "P303",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {4,S} {13,S}
2  O u0 p2 c0 {5,D}
3  C u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
4  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
5  C u0 p0 c0 {2,D} {3,S} {4,S}
6  C u1 p0 c0 {3,S} {11,S} {12,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.56243,0.0385496,-9.41846e-06,-1.08109e-08,5.87242e-12,-25176.3,12.4948], Tmin=(10,'K'), Tmax=(964.513,'K')),
            NASAPolynomial(coeffs=[5.74248,0.0375309,-2.03104e-05,5.34109e-09,-5.49339e-13,-25970,0.121708], Tmin=(964.513,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-209.361,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C-C': 3, 'C-H': 6, 'C=O': 1, 'C-O': 1}
1D rotors:
* Invalidated! pivots: [1, 4], dihedral: [13, 1, 4, 5], invalidation reason: 
* Invalidated! pivots: [3, 5], dihedral: [6, 3, 5, 2], invalidation reason: Inconsistent initial and final conformers But unable to propose troubleshooting methods.Inconsistent initial and final conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 6], dihedral: [5, 3, 6, 11], invalidation reason: 
* Invalidated! pivots: [4, 5], dihedral: [1, 4, 5, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.29983700    0.77505500    1.30189300
O      -0.39379900   -1.06484600    1.30744600
C       1.10558300    0.01885100   -0.23116600
C      -1.12124400    1.07181500    0.60533400
C      -0.14366900   -0.09452400    0.62578500
C       2.17848600   -0.94663400    0.11841700
H       0.76333700   -0.12419900   -1.27340700
H       1.46218300    1.05839400   -0.21185900
H      -1.34398100    1.33429800   -0.43812100
H      -0.60280600    1.93962100    1.04552100
H       1.95773200   -1.78545000    0.76293500
H       3.15961100   -0.85586900   -0.32754300
H      -2.13447900   -0.07705800    1.73481200
""",
)

entry(
    index = 257,
    label = "P304",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {7,S}
2 O u0 p2 c0 {4,D}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C u1 p0 c0 {2,D} {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74529,0.02179,-1.88808e-05,1.0206e-08,-2.60102e-12,-20039.7,10.3866], Tmin=(10,'K'), Tmax=(804.278,'K')),
            NASAPolynomial(coeffs=[4.70163,0.0170337,-1.00102e-05,2.85318e-09,-3.15491e-13,-20193.5,5.98113], Tmin=(804.278,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-166.648,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (149.66,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C-C': 1, 'C-H': 2, 'C=O': 1, 'C-O': 1}
1D rotors:
pivots: [1, 3], dihedral: [7, 1, 3, 4], rotor symmetry: 1, max scan energy: 13.67 kJ/mol
pivots: [3, 4], dihedral: [1, 3, 4, 2], rotor symmetry: 1, max scan energy: 18.34 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.22749300    0.48015000   -0.17916600
O      -0.36892400   -0.54408700    2.32790200
C      -0.19829100   -0.47457700   -0.08618700
C       0.04886900   -1.00944000    1.32636600
H      -0.45974500   -1.31677100   -0.72894500
H       0.78132600   -0.09781400   -0.42098900
H      -1.11731000    1.11163300    0.54043900
""",
)

entry(
    index = 258,
    label = "P305",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {10,S}
3  C u0 p0 c0 {2,D} {4,S} {12,S}
4  C u0 p0 c0 {3,S} {5,D} {11,S}
5  C u0 p0 c0 {4,D} {6,S} {13,S}
6  O u0 p2 c0 {5,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 O u1 p2 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95664,0.00515943,0.000440759,-2.23757e-06,4.0332e-09,-25545.2,11.2283], Tmin=(10,'K'), Tmax=(139.232,'K')),
            NASAPolynomial(coeffs=[2.4445,0.0486294,-2.78566e-05,7.67061e-09,-8.24097e-13,-25503.2,15.5412], Tmin=(139.232,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-211.723,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (324.264,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 2, 'H-O': 1, 'C=C': 2, 'C-O': 2, 'C-H': 6}
1D rotors:
pivots: [1, 7], dihedral: [14, 1, 7, 6], rotor symmetry: 1, max scan energy: 72.90 kJ/mol
pivots: [3, 4], dihedral: [8, 3, 4, 5], rotor symmetry: 3, max scan energy: 7.65 kJ/mol
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 2], invalidation reason: Another conformer for W19[66] exists which is 10.28 kJ/mol lower.Another conformer for W19[66] exists which is 10.28 kJ/mol lower.
* Invalidated! pivots: [6, 7], dihedral: [2, 6, 7, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
O      -3.11467000   -1.05100200   -1.19347300
O      -1.55471000    0.67788700   -0.04585200
C       2.78458100    0.13702700    0.24808100
C       1.30392200    0.29971900    0.13594800
C       0.46793100   -0.56772300   -0.44706900
C      -0.98120500   -0.33082900   -0.51474900
C      -1.81494200   -1.30502600   -1.15528500
H       3.09713200    0.14402800    1.29851700
H       3.30425200    0.97361200   -0.23277100
H       3.13197100   -0.79233300   -0.20841700
H       0.86454300    1.19824400    0.56329900
H       0.84362800   -1.48561400   -0.89352700
H      -1.49787900   -2.23141900   -1.61426800
H      -3.19156200   -0.18252600   -0.73337800
""",
)

entry(
    index = 259,
    label = "P306",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {6,S}
3  C u0 p0 c0 {1,D} {5,S} {8,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  C u0 p0 c0 {3,S} {9,D} {12,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  O u0 p2 c0 {5,D}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75934,0.0209526,6.02478e-05,-1.18419e-07,6.19455e-11,-3294.48,10.0586], Tmin=(10,'K'), Tmax=(649.563,'K')),
            NASAPolynomial(coeffs=[2.68586,0.0431353,-2.69376e-05,7.9689e-09,-9.02596e-13,-3483.55,12.2455], Tmin=(649.563,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-27.4253,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 2, 'C=C': 2, 'C-H': 6, 'C=O': 1}
1D rotors:
pivots: [2, 3], dihedral: [4, 2, 3, 5], rotor symmetry: 1, max scan energy: 33.10 kJ/mol
pivots: [4, 6], dihedral: [2, 4, 6, 1], rotor symmetry: 1, max scan energy: 43.18 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O      -3.52270900   -0.46869600    0.02837100
C      -0.02769700    0.17624300   -0.32380700
C       1.30938700   -0.38108500   -0.35251300
C      -1.15761200   -0.53333900   -0.14387600
C       2.41351700    0.35381300   -0.53381100
C      -2.47251100    0.11415500   -0.12875600
H       1.39486800   -1.45631200   -0.21726400
H      -0.10829900    1.25444600   -0.45982200
H      -1.14328300   -1.61030100   -0.00296000
H       2.36167700    1.42910300   -0.67164000
H       3.39899200   -0.09537500   -0.54990200
H      -2.44633300    1.21734100   -0.27622600
""",
)

entry(
    index = 260,
    label = "P307",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {4,S} {8,S}
2  C u0 p0 c0 {1,D} {3,S} {7,S}
3  C u0 p0 c0 {2,S} {5,S} {9,D}
4  C u0 p0 c0 {1,S} {6,D} {10,S}
5  O u0 p2 c0 {3,S} {12,S}
6  C u1 p0 c0 {4,D} {11,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70458,0.0325884,2.30376e-05,-5.94262e-08,2.76624e-11,-4307.96,11.6877], Tmin=(10,'K'), Tmax=(838.82,'K')),
            NASAPolynomial(coeffs=[6.76438,0.0384217,-2.39169e-05,6.91905e-09,-7.62291e-13,-5539.83,-6.81941], Tmin=(838.82,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-35.8097,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (270.22,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 2, 'H-O': 1, 'C=C': 2, 'C-O': 1, 'C-H': 4, 'C=O': 1}
1D rotors:
pivots: [1, 5], dihedral: [12, 1, 5, 2], rotor symmetry: 1, max scan energy: 55.49 kJ/mol
pivots: [3, 6], dihedral: [4, 3, 6, 7], rotor symmetry: 1, max scan energy: 31.57 kJ/mol
pivots: [4, 5], dihedral: [3, 4, 5, 1], rotor symmetry: 1, max scan energy: 34.11 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O       2.84854000    0.67772600    0.31958200
O       2.19397500   -1.31124100   -0.50693800
C      -0.51592500   -0.34158600   -0.40465400
C       0.55564100    0.37183600   -0.02513100
C       1.91049600   -0.20471200   -0.11140100
C      -1.88228700    0.15231800   -0.35116900
C      -2.94155000   -0.53899800   -0.72100600
H       0.46979200    1.38378300    0.35380900
H      -0.35920900   -1.35003200   -0.77521900
H      -2.02178500    1.17192200    0.02537700
H      -4.01073100   -0.40045000   -0.77408400
H       3.70269000    0.22973300    0.23283400
""",
)

entry(
    index = 261,
    label = "P308",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  C u1 p0 c0 {1,S} {2,S} {8,S}
4  C u0 p0 c0 {2,D} {5,S} {9,S}
5  O u0 p2 c0 {4,S} {10,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89481,0.00621157,0.00011939,-2.38386e-07,1.4212e-10,22706.2,9.81965], Tmin=(10,'K'), Tmax=(562.548,'K')),
            NASAPolynomial(coeffs=[3.02683,0.036316,-2.46966e-05,7.99462e-09,-9.81548e-13,22425.2,10.142], Tmin=(562.548,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (188.748,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (228.648,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 3, 'H-O': 1, 'C-O': 1, 'C-H': 4, 'C=C': 1}
1D rotors:
pivots: [1, 5], dihedral: [10, 1, 5, 3], rotor symmetry: 1, max scan energy: 29.65 kJ/mol
* Invalidated! pivots: [3, 5], dihedral: [2, 3, 5, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
O       2.12293500    0.60571100    0.59581300
C      -1.09446700    0.56771700   -0.31605900
C       0.00863200   -0.40127400    0.06775400
C      -1.18800100   -0.92059900   -0.23477900
C       1.31677700   -0.47866800    0.44523600
H      -1.06080200    1.05340500   -1.29378900
H      -1.55922000    1.18048000    0.45951100
H      -1.82438900   -1.77796400   -0.35354600
H       1.82709900   -1.40822600    0.65768000
H       1.60571200    1.39550700    0.39153700
""",
)

entry(
    index = 262,
    label = "P309",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {9,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {5,S} {14,S}
5  C u0 p0 c0 {4,S} {6,D} {15,S}
6  C u0 p0 c0 {5,D} {7,S} {16,S}
7  O u0 p2 c0 {1,S} {6,S}
8  O u0 p2 c0 {2,S} {17,S}
9  O u0 p2 c0 {3,S} {18,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81003,0.0128814,0.000259645,-5.96546e-07,4.23965e-10,-44272.8,14.0828], Tmin=(10,'K'), Tmax=(452.374,'K')),
            NASAPolynomial(coeffs=[0.72379,0.0727551,-4.69305e-05,1.44824e-08,-1.70867e-12,-44327,22.8389], Tmin=(452.374,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-368.13,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (432.353,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 4, 'H-O': 2, 'C-O': 4, 'C-H': 7, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [2, 5], dihedral: [17, 2, 5, 4], invalidation reason: 
* Invalidated! pivots: [3, 6], dihedral: [18, 3, 6, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 5], dihedral: [1, 4, 5, 2], invalidation reason: Another conformer for C6H9O3[2410] exists which is 1.53 kJ/mol lower.Another conformer for C6H9O3[2410] exists which is 1.53 kJ/mol lower.
* Invalidated! pivots: [4, 6], dihedral: [1, 4, 6, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.79105400   -1.30947700   -1.87948000
O      -1.56421500   -0.79615000    0.90451600
O      -2.90198800    0.45000000   -1.19109500
C      -0.47900200   -0.03645500   -1.21124700
C      -0.39186300   -0.28173600    0.31136600
C      -1.61877000    0.92701200   -1.59775500
C       0.84305400    0.36063300   -1.80812300
C       1.20896600   -0.61398600   -2.72199400
C       0.22534000   -1.58518200   -2.74470300
H      -0.08530100    0.67309100    0.76992200
H       0.40345700   -1.00681000    0.49546900
H      -1.47421300    1.88914300   -1.10126100
H      -1.58975500    1.08958800   -2.68084000
H       1.39038100    1.24950500   -1.53459600
H       2.10822100   -0.63399800   -3.32028900
H       0.13604700   -2.50240600   -3.30434500
H      -2.30852300   -0.28188600    0.56344700
H      -3.01764000   -0.41274000   -1.60868300
""",
)

entry(
    index = 263,
    label = "P310",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u1 p0 c0 {1,S} {2,S} {4,S}
4  C u0 p0 c0 {3,S} {9,D} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {4,D}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96125,0.00267913,0.000120262,-2.55944e-07,1.79725e-10,16154.3,10.5574], Tmin=(10,'K'), Tmax=(364.081,'K')),
            NASAPolynomial(coeffs=[0.789962,0.0375223,-2.32976e-05,6.93963e-09,-7.95297e-13,16385.2,22.6527], Tmin=(364.081,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (134.313,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 4, 'C-H': 5, 'C=O': 1}
1D rotors:
* Invalidated! pivots: [4, 5], dihedral: [2, 4, 5, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
O       2.36722000    1.00936700    0.48827400
C      -0.89326300   -0.74806600   -0.30629100
C      -0.93152900    0.70941600    0.20172700
C       0.31899800   -0.00727500    0.01971400
C       1.73093200    0.02373300    0.10827900
H      -1.13324400   -0.93247000   -1.35089000
H      -1.22780700   -1.53378700    0.36713900
H      -1.28523200    0.89227700    1.21324300
H      -1.19065600    1.49367600   -0.50502600
H       2.24858100   -0.90737500   -0.18911800
""",
)

entry(
    index = 264,
    label = "P311",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,D} {6,S}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {5,S} {8,S}
4  C u0 p0 c0 {1,D} {7,S} {10,S}
5  C u1 p0 c0 {3,S} {11,S} {12,S}
6  O u0 p2 c0 {1,S} {13,S}
7  O u0 p2 c0 {4,S} {14,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79414,0.0153599,0.000202382,-5.40853e-07,4.37802e-10,-20681.7,12.7052], Tmin=(10,'K'), Tmax=(408.962,'K')),
            NASAPolynomial(coeffs=[2.93565,0.0516867,-3.33008e-05,1.03395e-08,-1.22996e-12,-20845,13.2237], Tmin=(408.962,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-171.956,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 2, 'H-O': 2, 'C=C': 2, 'C-O': 2, 'C-H': 5}
1D rotors:
* Invalidated! pivots: [1, 3], dihedral: [13, 1, 3, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 6], dihedral: [14, 2, 6, 3], invalidation reason: Another conformer for C5H7O2[4650] exists which is 6.10 kJ/mol lower.Another conformer for C5H7O2[4650] exists which is 6.10 kJ/mol lower.
* Invalidated! pivots: [3, 4], dihedral: [1, 3, 4, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [5, 7], dihedral: [4, 5, 7, 11], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 7], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 6], dihedral: [1, 3, 6, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.11173900   -1.27820000   -0.55523100
O      -3.27143800    0.27277900   -0.35583700
C      -0.92519400   -0.01398200   -0.00074300
C       0.33688000    0.41573700    0.43960700
C       1.54196000   -0.30669900    0.28490700
C      -2.06971800    0.74449700    0.04002300
C       2.75882000    0.07687600    0.76151100
H       1.49641900   -1.23594500   -0.28089600
H       0.37294400    1.38334600    0.93038500
H      -2.08332700    1.77168600    0.37357500
H       2.88173400    0.99571700    1.32470700
H       3.64521200   -0.51907200    0.58704000
H      -0.56659500   -1.91165100   -0.07714700
H      -3.13415100   -0.64598100   -0.63249900
""",
)

entry(
    index = 265,
    label = "P312",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,D} {10,S}
3  C u0 p0 c0 {4,S} {5,D} {6,S}
4  C u0 p0 c0 {2,D} {3,S} {11,S}
5  C u0 p0 c0 {3,D} {12,S} {13,S}
6  O u0 p2 c0 {3,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 O u1 p2 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68273,0.0268857,0.000107438,-3.38028e-07,3.26795e-10,-28769.7,11.8852], Tmin=(10,'K'), Tmax=(264.05,'K')),
            NASAPolynomial(coeffs=[2.09022,0.0510105,-2.96118e-05,7.99768e-09,-8.253e-13,-28685.6,17.4475], Tmin=(264.05,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-239.232,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (320.107,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 2, 'H-O': 1, 'C=C': 2, 'C-O': 2, 'C-H': 6}
1D rotors:
pivots: [1, 5], dihedral: [14, 1, 5, 6], rotor symmetry: 1, max scan energy: 56.20 kJ/mol
pivots: [3, 4], dihedral: [8, 3, 4, 6], rotor symmetry: 3, max scan energy: 6.34 kJ/mol
pivots: [5, 6], dihedral: [1, 5, 6, 4], rotor symmetry: 1, max scan energy: 50.99 kJ/mol
* Invalidated! pivots: [5, 7], dihedral: [1, 5, 7, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 6], dihedral: [3, 4, 6, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
O       1.29437700   -1.63045100    0.06288500
O       1.62675000   -3.55902000   -1.70248900
C      -2.48140400    0.54625500    0.27780700
C      -1.19387300   -0.20473900    0.19572800
C       0.27870700   -1.92316500   -0.76234300
C      -0.94006500   -1.21025400   -0.68261300
C       0.53258700   -2.98609900   -1.69837900
H      -2.92762500    0.45183700    1.27498500
H      -2.32102700    1.61864100    0.11452600
H      -3.20878300    0.19378800   -0.45680500
H      -0.40772400    0.07726000    0.89020600
H      -1.70724200   -1.51491200   -1.38995800
H      -0.27564400   -3.25934000   -2.39559400
H       2.00449700   -2.25361900   -0.19249400
""",
)

entry(
    index = 266,
    label = "P313",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {12,S}
4  C u0 p0 c0 {2,S} {3,D} {11,S}
5  O u0 p2 c0 {1,S} {14,S}
6  C u1 p0 c0 {1,S} {13,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {6,D}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79963,0.0241164,0.000431932,-2.82554e-06,5.67492e-09,-16501.5,12.0983], Tmin=(10,'K'), Tmax=(170.22,'K')),
            NASAPolynomial(coeffs=[4.11721,0.0465135,-2.85628e-05,8.52791e-09,-9.85514e-13,-16555.5,9.85775], Tmin=(170.22,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-136.315,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (324.264,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 3, 'H-O': 1, 'C-O': 1, 'C-H': 6, 'C=O': 1, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [1, 3], dihedral: [14, 1, 3, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 5], dihedral: [1, 3, 5, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [3, 7], dihedral: [1, 3, 7, 2], rotor symmetry: 1, max scan energy: 14.60 kJ/mol
pivots: [4, 6], dihedral: [9, 4, 6, 5], rotor symmetry: 3, max scan energy: 7.72 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.26367400   -0.37630100    1.76431800
O       0.26756300    2.55284700    3.53750000
C       0.76750900    0.93728700    1.76038000
C      -2.34840300    0.37549500   -0.54739300
C      -0.48807100    1.14948000    0.95094900
C      -1.10161200    0.18918400    0.26342500
C       0.48455700    1.44313900    3.21014400
H       1.57642000    1.57647000    1.38695000
H      -2.17209900    0.11970100   -1.59779200
H      -3.14687600   -0.28644500   -0.19441900
H      -2.71283600    1.40395200   -0.50199700
H      -0.66049300   -0.80457000    0.26084200
H      -0.88125000    2.16317600    0.96997800
H       0.67176700   -0.91190100    2.30586300
""",
)

entry(
    index = 267,
    label = "P314",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,D} {11,S}
4  C u0 p0 c0 {1,S} {5,S} {10,D}
5  C u0 p0 c0 {3,D} {4,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {4,D}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9541,0.00333555,0.000158758,-3.59641e-07,2.705e-10,-705.632,10.8741], Tmin=(10,'K'), Tmax=(339.056,'K')),
            NASAPolynomial(coeffs=[0.366176,0.0456639,-2.85045e-05,8.56152e-09,-9.90012e-13,-462.33,24.3031], Tmin=(339.056,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-5.86014,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (278.535,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 4, 'C-H': 6, 'C=O': 1, 'C=C': 1}
1D rotors:
pivots: [2, 3], dihedral: [4, 2, 3, 8], rotor symmetry: 3, max scan energy: 10.16 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       0.58603400   -2.31968400    0.13426600
C      -0.16948200    0.02029500   -0.55121000
C      -1.57167100    0.18344500    0.02638600
C       0.96218000    0.89381200   -0.00494600
C       0.71563000   -1.13163000    0.05008200
C       1.71304700   -0.10853400    0.48943100
H      -0.20474800   -0.01341700   -1.64629700
H      -2.04404100    1.10356000   -0.32963200
H      -2.20298500   -0.65644400   -0.27422900
H      -1.54768700    0.21367200    1.11941800
H       1.09858800    1.96850600   -0.01666700
H       2.66513400   -0.15358100    1.00339700
""",
)

entry(
    index = 268,
    label = "P315",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {7,S} {9,S} {10,S}
2  C u0 p0 c0 {3,S} {8,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {5,S} {13,S}
5  C u0 p0 c0 {4,S} {6,D} {14,S}
6  C u0 p0 c0 {5,D} {15,S} {16,S}
7  O u0 p2 c0 {1,S} {17,S}
8  O u0 p2 c0 {2,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 O u1 p2 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.39224,0.0629723,-3.5795e-05,8.82864e-09,-5.98028e-13,-42631.3,13.9483], Tmin=(10,'K'), Tmax=(1496.32,'K')),
            NASAPolynomial(coeffs=[17.9328,0.0325555,-1.37778e-05,2.79483e-09,-2.20749e-13,-47929.1,-65.2239], Tmin=(1496.32,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-354.52,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (428.195,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 3, 'H-O': 2, 'C-O': 3, 'C-H': 7, 'C=C': 2}
1D rotors:
* Invalidated! pivots: [1, 4], dihedral: [17, 1, 4, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [2, 5], dihedral: [18, 2, 5, 6], rotor symmetry: 1, max scan energy: 20.11 kJ/mol
* Invalidated! pivots: [4, 6], dihedral: [1, 4, 6, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [5, 6], dihedral: [2, 5, 6, 4], invalidation reason: Another conformer for C6H9O3[7630] exists which is 1.05 kJ/mol lower.Another conformer for C6H9O3[7630] exists which is 1.05 kJ/mol lower.
* Invalidated! pivots: [7, 8], dihedral: [6, 7, 8, 9], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
* Invalidated! pivots: [8, 9], dihedral: [7, 8, 9, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [6, 7], dihedral: [4, 6, 7, 8], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.04781200    2.16861200    0.28251200
O      -2.85791800   -0.99995700    1.35479400
O       1.29260100    0.86986300   -1.75557200
C       0.35234600    1.01403600    1.00781900
C      -1.81628500   -0.09577500    1.67527200
C      -0.61673400   -0.11875200    0.76297000
C      -0.49455000   -1.11600400   -0.17946900
C       0.41964800   -1.30348500   -1.23202800
C       1.25426500   -0.34923100   -1.92057300
H       1.37464100    0.71628200    0.76102100
H       0.32691000    1.28370100    2.06827900
H      -1.49736600   -0.35079800    2.69371000
H      -2.17669800    0.94303900    1.71511600
H      -1.22717800   -1.91382000   -0.07249600
H       0.43192400   -2.29438900   -1.67824000
H       1.89210900   -0.79798900   -2.70559300
H       0.25904700    1.99530500   -0.62251500
H      -3.27266900   -0.69743700    0.53992200
""",
)

entry(
    index = 269,
    label = "P316",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {15,S}
2  O u0 p2 c0 {4,S} {16,S}
3  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
5  C u0 p0 c0 {3,S} {4,S} {6,D}
6  C u0 p0 c0 {5,D} {7,S} {12,S}
7  C u1 p0 c0 {6,S} {13,S} {14,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70699,0.0263251,0.000127274,-3.42534e-07,2.84036e-10,-27151.1,13.0203], Tmin=(10,'K'), Tmax=(309.783,'K')),
            NASAPolynomial(coeffs=[1.07971,0.0602495,-3.69932e-05,1.09796e-08,-1.25776e-12,-26988.3,22.6165], Tmin=(309.783,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-225.748,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (382.466,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 3, 'H-O': 2, 'C-O': 2, 'C-H': 7, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [1, 3], dihedral: [15, 1, 3, 5], invalidation reason: Another conformer for C5H9O2[7825] exists which is 2.33 kJ/mol lower.Another conformer for C5H9O2[7825] exists which is 2.33 kJ/mol lower.
* Invalidated! pivots: [2, 4], dihedral: [16, 2, 4, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 5], dihedral: [1, 3, 5, 4], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
* Invalidated! pivots: [4, 5], dihedral: [2, 4, 5, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [6, 7], dihedral: [5, 6, 7, 13], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [5, 6], dihedral: [3, 5, 6, 7], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.97710700    0.77381300   -3.03982500
O      -2.35310300   -0.45982500   -0.92731600
C      -0.14470400    1.27693600   -2.00991200
C      -0.95815300   -0.81789900   -0.77354100
C      -0.07877200    0.39414200   -0.78190700
C       0.74095100    0.69459300    0.30720600
C       1.59459300    1.77114000    0.41851300
H      -0.44974400    2.29407300   -1.71101000
H       0.85544300    1.37604900   -2.44753900
H      -0.75079300   -1.45801600   -1.63395800
H      -0.81015200   -1.40498100    0.13918400
H       0.70283800    0.00249300    1.14693800
H       1.70206600    2.50856500   -0.36765700
H       2.19474900    1.91380600    1.30791700
H      -1.82294900    0.54071900   -2.63164500
H      -2.58829900    0.10055400   -0.17908000
""",
)

entry(
    index = 270,
    label = "P317",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {5,D}
4  C u0 p0 c0 {3,S} {6,D} {9,S}
5  C u0 p0 c0 {3,D} {10,S} {11,S}
6  C u0 p0 c0 {4,D} {12,S} {13,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85126,0.00957176,0.000181515,-4.031e-07,2.7231e-10,-10359.2,11.5369], Tmin=(10,'K'), Tmax=(490.906,'K')),
            NASAPolynomial(coeffs=[2.69517,0.0489827,-3.05479e-05,9.33728e-09,-1.10601e-12,-10607.1,12.6111], Tmin=(490.906,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-86.1674,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (328.422,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 2, 'H-O': 1, 'C=C': 2, 'C-O': 1, 'C-H': 7}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [14, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [3, 4], dihedral: [2, 3, 4, 6], rotor symmetry: 1, max scan energy: 21.26 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.04176300   -0.96807900   -1.69756800
C       0.76528700    0.06747400   -1.16025600
C       0.25995600    1.47032300   -1.44067500
C       0.94355100    2.59783900   -0.79875000
C      -0.77320500    1.68046800   -2.26684000
C       2.00531800    2.52986600    0.01152200
H       0.89582000   -0.05944300   -0.07630900
H       1.75283700   -0.05936800   -1.61382900
H       0.52984700    3.57662200   -1.03080300
H      -1.26328700    0.85824900   -2.77193600
H      -1.13584800    2.68194000   -2.46902700
H       2.44431600    3.42780900    0.42963100
H       2.47751100    1.59328500    0.28491000
H      -0.89430900   -0.93301200   -1.25153000
""",
)

entry(
    index = 271,
    label = "P318",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {5,S} {12,S}
2  O u0 p2 c0 {7,D}
3  C u0 p0 c0 {4,S} {6,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {5,D} {10,S}
5  C u0 p0 c0 {1,S} {4,D} {11,S}
6  C u1 p0 c0 {3,S} {7,D}
7  C u0 p0 c0 {2,D} {6,D}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.64577,0.0317938,1.69139e-05,-5.31222e-08,2.77383e-11,3286.26,12.3344], Tmin=(10,'K'), Tmax=(722.927,'K')),
            NASAPolynomial(coeffs=[4.35461,0.0396159,-2.36842e-05,6.788e-09,-7.50665e-13,2876.89,7.02215], Tmin=(722.927,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (27.2878,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 4, 'C-O': 1, 'C=C': 2, 'C=O': 1, 'C-C': 2, 'H-O': 1}
1D rotors:
* Invalidated! pivots: [1, 5], dihedral: [12, 1, 5, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 4], dihedral: [6, 3, 4, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 6], dihedral: [4, 3, 6, 7], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
O      -0.61933500   -1.55653700   -2.03152100
O      -1.08545400    3.10931500   -1.22287500
C      -0.66939700   -0.12610700    0.67612100
C      -0.52474100   -1.59025200    0.37937200
C      -0.50947700   -2.16367800   -0.83335500
C      -0.81006000    0.79220700   -0.46102100
C      -0.95362200    2.02911200   -0.77630000
H       0.18690100    0.21685700    1.28363700
H      -1.53095800    0.03399600    1.34845100
H      -0.42281100   -2.24340200    1.23777100
H      -0.39917600   -3.23761100   -0.93980000
H      -0.71604600   -0.59420100   -1.87973000
""",
)

entry(
    index = 272,
    label = "P319",
    molecule = 
"""
multiplicity 3
1  O u1 p2 c0 {5,S}
2  O u0 p2 c0 {6,D}
3  C u0 p0 c0 {4,D} {5,S} {9,S}
4  C u0 p0 c0 {3,D} {6,S} {8,S}
5  C u0 p0 c0 {1,S} {3,S} {7,D}
6  C u0 p0 c0 {2,D} {4,S} {10,S}
7  C u1 p0 c0 {5,D} {11,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87237,0.0358333,-5.76959e-06,-1.6812e-08,8.09167e-12,21781.5,11.6144], Tmin=(10,'K'), Tmax=(1064.75,'K')),
            NASAPolynomial(coeffs=[12.0285,0.0230244,-1.28456e-05,3.34726e-09,-3.34754e-13,19033.9,-32.9925], Tmin=(1064.75,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (181.192,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (245.277,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 4, 'C-O': 1, 'C=C': 2, 'C=O': 1, 'C-C': 2}
1D rotors:
pivots: [3, 5], dihedral: [4, 3, 5, 1], rotor symmetry: 1, max scan energy: 24.15 kJ/mol
pivots: [4, 6], dihedral: [3, 4, 6, 2], rotor symmetry: 1, max scan energy: 31.47 kJ/mol
pivots: [5, 7], dihedral: [1, 5, 7, 11], rotor symmetry: 1, max scan energy: 32.38 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O      -1.33205500    0.49170400    1.67643600
O       3.10046000   -0.21493800   -0.86604000
C      -0.43839100   -0.14536000   -0.45463600
C       0.85538400   -0.02619200   -0.13021600
C      -1.53250100    0.13127300    0.50625200
C       1.92090900   -0.30883000   -1.11027900
C      -2.88576600   -0.01717300    0.08861100
H       1.15725700    0.28279300    0.86541100
H      -0.73473600   -0.45526700   -1.45390500
H       1.56216600   -0.62189600   -2.11470300
H      -3.78997000    0.14528500    0.66624200
""",
)

entry(
    index = 273,
    label = "P320",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
2  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {5,S} {11,S}
5  O u0 p2 c0 {1,S} {4,S}
6  O u0 p2 c0 {2,S} {12,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82755,0.012467,0.000175246,-4.85827e-07,4.01454e-10,-17996,10.9778], Tmin=(10,'K'), Tmax=(414.724,'K')),
            NASAPolynomial(coeffs=[4.39192,0.0370766,-2.24607e-05,6.71611e-09,-7.84899e-13,-18301.3,5.63586], Tmin=(414.724,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-149.628,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-O': 3, 'C=C': 1, 'C-C': 2, 'H-O': 1}
1D rotors:
pivots: [2, 4], dihedral: [12, 2, 4, 5], rotor symmetry: 1, max scan energy: 11.81 kJ/mol
pivots: [4, 5], dihedral: [2, 4, 5, 3], rotor symmetry: 1, max scan energy: 16.00 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.11130600    3.31862900   -1.46974800
O      -1.38905800   -0.09254300    1.06622900
C      -2.89370200    2.33975000   -0.67945800
C      -1.43257400    0.00495400   -0.36331700
C      -1.73447600    1.37533800   -0.83999300
C      -1.12802600    2.34697200   -1.53791900
H      -0.49207800   -0.33750600   -0.81726400
H      -2.21405200   -0.69837900   -0.66441800
H      -3.08851800    2.72924800    0.32043900
H      -3.82293100    2.09555500   -1.19721500
H      -0.20334300    2.52803600   -2.07093200
H      -0.74885800    0.55876500    1.37195700
""",
)

entry(
    index = 274,
    label = "P321",
    molecule = 
"""
multiplicity 3
1  O u0 p2 c0 {3,S} {12,S}
2  O u1 p2 c0 {6,S}
3  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
4  C u0 p0 c0 {3,S} {5,S} {6,D}
5  C u1 p0 c0 {4,S} {9,S} {10,S}
6  C u0 p0 c0 {2,S} {4,D} {11,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83192,0.0145021,0.000165221,-4.96352e-07,4.64679e-10,-3025.67,12.3087], Tmin=(10,'K'), Tmax=(336.255,'K')),
            NASAPolynomial(coeffs=[2.48842,0.0441951,-2.84003e-05,8.78971e-09,-1.0434e-12,-3012.83,16.1735], Tmin=(336.255,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-25.1316,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-O': 2, 'C=C': 1, 'C-C': 2, 'H-O': 1}
1D rotors:
* Invalidated! pivots: [1, 3], dihedral: [12, 1, 3, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 4], dihedral: [1, 3, 4, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 9], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 6], dihedral: [3, 4, 6, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       1.06324200   -1.32597600    0.41900300
O       2.04688800    0.58835300    2.07046100
C       1.15235500   -0.31133500   -0.54640500
C       1.10748600    1.11242700   -0.03452700
C       0.69609900    2.16780300   -0.94980000
C       1.57481400    1.42503500    1.28917800
H       0.33594500   -0.45921000   -1.26092500
H       2.08667500   -0.38991300   -1.13979700
H      -0.34615700    2.46308800   -1.02534200
H       1.39726200    2.62652300   -1.64049900
H       1.51351900    2.48476600    1.58984000
H       1.57789300   -1.02954600    1.18611800
""",
)

entry(
    index = 275,
    label = "P322",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {5,D}
4  O u0 p2 c0 {1,S} {11,S}
5  C u0 p0 c0 {3,D} {12,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 O u0 p2 c0 {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72697,0.0209799,0.000202698,-7.01095e-07,6.73109e-10,-31853.5,11.2117], Tmin=(10,'K'), Tmax=(381.497,'K')),
            NASAPolynomial(coeffs=[7.33557,0.0300074,-1.70599e-05,4.9316e-09,-5.7041e-13,-32469.8,-7.18986], Tmin=(381.497,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-264.821,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (270.22,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-O': 1, 'C=C': 1, 'C=O': 1, 'C-C': 2, 'H-O': 1}
1D rotors:
pivots: [1, 3], dihedral: [12, 1, 3, 5], rotor symmetry: 1, max scan energy: 12.04 kJ/mol
pivots: [3, 5], dihedral: [1, 3, 5, 4], rotor symmetry: 1, max scan energy: 22.56 kJ/mol
pivots: [4, 5], dihedral: [9, 4, 5, 3], rotor symmetry: 3, max scan energy: 6.21 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.56240900   -0.74310400   -0.96844600
O       2.90083200    1.45975200    2.64780100
C       1.12312300    0.30373400   -0.10574600
C       0.70226900   -1.21158000    1.97790200
C       1.37155100   -0.00271000    1.35689400
C       2.18424000    0.76483900    2.04467200
H       0.04665600    0.37866000   -0.28365700
H       1.57314400    1.26594200   -0.37961900
H       0.91304900   -2.09744400    1.37360200
H       1.04925000   -1.39941600    2.99503800
H      -0.38451900   -1.07738300    2.00949900
H       2.51137000   -0.84485100   -0.83746800
""",
)

entry(
    index = 276,
    label = "P323",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,D} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {6,D}
3  C u0 p0 c0 {1,D} {4,S} {7,S}
4  C u1 p0 c0 {3,S} {10,S} {11,S}
5  C u0 p0 c0 {2,S} {9,D} {12,S}
6  O u0 p2 c0 {2,D}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {1,S}
9  O u0 p2 c0 {5,D}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.62168,0.0355828,4.2923e-06,-3.14178e-08,1.49442e-11,-11577,12.0199], Tmin=(10,'K'), Tmax=(886.095,'K')),
            NASAPolynomial(coeffs=[6.30874,0.0373489,-2.22209e-05,6.22806e-09,-6.70447e-13,-12598.7,-3.69694], Tmin=(886.095,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-96.2718,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 3, 'C-H': 5, 'C=O': 2, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [3, 4], dihedral: [5, 3, 4, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [4, 7], dihedral: [1, 4, 7, 2], rotor symmetry: 1, max scan energy: 33.68 kJ/mol
* Invalidated! pivots: [5, 6], dihedral: [3, 5, 6, 10], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [3, 5], dihedral: [4, 3, 5, 6], rotor symmetry: 1, max scan energy: 65.60 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O       0.54379500    0.58310300    1.37822000
O       2.77467600    0.47774700   -1.28488200
C       0.04151100   -0.26673000   -0.78151300
C       0.88746100    0.33126400    0.22374200
C      -1.28831800   -0.62185600   -0.51416700
C      -2.12042500   -1.18918000   -1.43700300
C       2.32020700    0.67490000   -0.18740100
H      -1.65206200   -0.42418000    0.49019500
H       0.47501100   -0.43365700   -1.76161400
H      -3.14251800   -1.44940500   -1.19134200
H      -1.78291400   -1.39720300   -2.44664900
H       2.90394000    1.12946000    0.63868900
""",
)

entry(
    index = 277,
    label = "P324",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {4,S} {11,S}
4  C u0 p0 c0 {3,S} {5,D} {10,S}
5  C u0 p0 c0 {4,D} {6,S} {12,S}
6  O u0 p2 c0 {1,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 O u1 p2 c0 {4,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92205,0.00471627,0.000141163,-2.68113e-07,1.58888e-10,-10838.3,12.9564], Tmin=(10,'K'), Tmax=(523.941,'K')),
            NASAPolynomial(coeffs=[0.103534,0.0496043,-3.23977e-05,1.00499e-08,-1.18948e-12,-10654.2,26.8491], Tmin=(523.941,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-90.1429,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 3, 'C=C': 2, 'C-C': 2, 'C-H': 5}

External symmetry: 1, optical isomers: 1

Geometry:
O      -0.44300600   -1.47406900   -0.17414400
O       2.71958000    0.16054100    0.11906800
C      -1.37829400   -0.37746700   -0.09196500
C      -0.76611100    0.97582000    0.07556100
C       0.55109400    1.17009700    0.14567100
C       1.48889700    0.02551200    0.05851500
C       0.87806100   -1.25224900   -0.10091700
H      -1.98221500   -0.42086300   -1.00610400
H      -2.04776900   -0.60800700    0.74524000
H      -1.46923800    1.80147800    0.13743600
H       0.98843600    2.15424500    0.26720900
H       1.46829700   -2.15590900   -0.17537300
""",
)

entry(
    index = 278,
    label = "P325",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {6,S}
3  C u0 p0 c0 {2,D} {5,S} {12,S}
4  C u0 p0 c0 {5,D} {6,S} {7,S}
5  C u0 p0 c0 {3,S} {4,D} {11,S}
6  O u0 p2 c0 {2,S} {4,S}
7  O u0 p2 c0 {4,S} {13,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78006,0.0204374,0.000119099,-3.63939e-07,3.50308e-10,-32639.5,9.97836], Tmin=(10,'K'), Tmax=(265.229,'K')),
            NASAPolynomial(coeffs=[2.04141,0.0466583,-2.91918e-05,8.79243e-09,-1.01881e-12,-32547.3,16.0589], Tmin=(265.229,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-271.368,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 3, 'C=C': 2, 'H-O': 1, 'C-C': 2, 'C-H': 5}
1D rotors:
pivots: [2, 6], dihedral: [13, 2, 6, 1], rotor symmetry: 2, max scan energy: 8.42 kJ/mol
pivots: [3, 4], dihedral: [8, 3, 4, 1], rotor symmetry: 3, max scan energy: 5.41 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O      -0.15896000    0.22879500   -1.01946900
O      -2.31999900   -0.12334800   -1.71771500
C       2.03577700    0.43935600    0.03854100
C       0.62318200   -0.01174700    0.10616300
C      -0.13862600   -0.63303300    1.03930500
C      -1.39670700   -0.25530200   -0.74949700
C      -1.46127800   -0.79762100    0.49111500
H       2.54109700    0.19595700    0.97451000
H       2.57874600   -0.04870100   -0.77788700
H       2.10910500    1.52115000   -0.11609300
H      -2.32476300   -1.24889000    0.94880600
H       0.19503100   -0.94527600    2.01675400
H      -1.90730900    0.31711900   -2.46968000
""",
)

entry(
    index = 279,
    label = "P326",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 C u0 p0 c0 {1,S} {2,S} {4,D}
4 C u1 p0 c0 {3,D} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.09539,-0.00918414,0.000146529,-2.61446e-07,1.51047e-10,49787.3,8.67528], Tmin=(10,'K'), Tmax=(546.498,'K')),
            NASAPolynomial(coeffs=[1.0437,0.0323355,-2.00857e-05,6.03597e-09,-6.97988e-13,49834.4,18.9331], Tmin=(546.498,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (413.942,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 3, 'C-H': 5, 'C=C': 1}

External symmetry: 1, optical isomers: 1

Geometry:
C      -0.58206500    0.89342000   -0.10114300
C      -0.75544500   -0.60468400    0.08828200
C       0.60709200    0.01487300   -0.01232800
C       1.88535000   -0.11419800   -0.01831500
H      -0.82419200    1.31699500   -1.07092400
H      -0.79289900    1.54272600    0.74293600
H      -1.10080500   -1.19393000   -0.75491800
H      -1.06945700   -0.96789800    1.06139100
H       2.63242000   -0.88730400    0.06501900
""",
)

entry(
    index = 280,
    label = "327",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
3  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
4  C u0 p1 c0 {2,S} {3,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90282,0.00769253,0.000106006,-2.71058e-07,2.28859e-10,14694.2,8.96154], Tmin=(10,'K'), Tmax=(301.077,'K')),
            NASAPolynomial(coeffs=[2.01772,0.0327377,-1.87731e-05,5.24184e-09,-5.7071e-13,14807.7,15.7932], Tmin=(301.077,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (122.169,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C-C': 2, 'C-H': 5, 'C-O': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [10, 1, 2, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 4], dihedral: [1, 2, 4, 3], invalidation reason: Another conformer for C[C]CO[71] exists which is 9.09 kJ/mol lower.Another conformer for C[C]CO[71] exists which is 9.09 kJ/mol lower.
* Invalidated! pivots: [3, 4], dihedral: [7, 3, 4, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       0.10003000   -0.62038000   -0.31210600
C       1.15225500    0.17314400    0.17124600
C       2.02526800    1.78388100    1.78621300
C       0.84004600    1.22743000    1.10155000
H       1.51595800    0.90580000   -0.61183200
H       2.01939800   -0.47643600    0.37032200
H       1.96322700    2.86607400    1.92813200
H       3.02382300    1.49589300    1.41826700
H       1.91352800    1.36687600    2.80289200
H      -0.70781600   -0.14927600   -0.06869300
""",
)

entry(
    index = 281,
    label = "P328",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 C u0 p0 c0 {1,S} {4,D} {5,S}
3 C u0 p0 c0 {1,D} {6,S} {7,S}
4 C u1 p0 c0 {1,S} {2,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9549,0.00253449,6.64609e-05,-1.17689e-07,6.34326e-11,73667.7,8.5191], Tmin=(10,'K'), Tmax=(596.445,'K')),
            NASAPolynomial(coeffs=[2.12772,0.0253335,-1.73967e-05,5.68436e-09,-7.03866e-13,73698.1,14.8176], Tmin=(596.445,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (612.488,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-C': 2, 'C-H': 3}
1D rotors:
* Invalidated! pivots: [1, 3], dihedral: [2, 1, 3, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
C       0.16855000    0.18538200   -0.10578800
C       1.29835900   -0.34504600    0.45921900
C      -1.19004300    0.18865500   -0.29639700
C       1.49325400    0.75087900   -0.34685700
H       1.70591200   -1.15546000    1.04545100
H      -1.86488200   -0.15757500    0.47730000
H      -1.61087900    0.53316800   -1.23340400
""",
)

entry(
    index = 282,
    label = "P329",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {3,S} {6,S} {13,S} {14,S}
5  C u1 p0 c0 {1,S} {3,S} {15,S}
6  C u1 p0 c0 {2,S} {4,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9365,0.00380345,0.000165425,-2.89418e-07,1.63986e-10,30495.9,10.5415], Tmin=(10,'K'), Tmax=(455.366,'K')),
            NASAPolynomial(coeffs=[-3.19628,0.0664091,-4.06378e-05,1.20232e-08,-1.37645e-12,31146,39.3477], Tmin=(455.366,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (253.531,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (382.466,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 6, 'C-H': 10}

External symmetry: 2, optical isomers: 1

Geometry:
C       1.21571800   -0.84063300    0.25587700
C       1.34430800    0.64010000   -0.18224400
C      -1.34430800   -0.64010000    0.18224400
C      -1.21571800    0.84063300   -0.25587700
C      -0.10784900   -1.42205700   -0.12321600
C       0.10784900    1.42205700    0.12321600
H       1.33139300   -0.87857300    1.35468500
H       2.03868800   -1.43072700   -0.15812800
H       2.22405400    1.09681700    0.28073500
H       1.52705800    0.65466300   -1.27246900
H      -2.22405400   -1.09681700   -0.28073500
H      -1.52705800   -0.65466300    1.27246900
H      -2.03868800    1.43072700    0.15812800
H      -1.33139300    0.87857300   -1.35468500
H      -0.18442500   -2.48100400   -0.34482600
H       0.18442500    2.48100400    0.34482600
""",
)

entry(
    index = 283,
    label = "P330",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {4,D} {6,S}
4  C u0 p0 c0 {1,S} {3,D} {12,S}
5  C u0 p0 c0 {1,S} {6,S} {13,D}
6  O u0 p2 c0 {3,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 O u0 p2 c0 {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85652,0.0116885,0.000117134,-2.26774e-07,1.32963e-10,-38755.6,10.7621], Tmin=(10,'K'), Tmax=(539.127,'K')),
            NASAPolynomial(coeffs=[0.849281,0.0494224,-3.07599e-05,9.1662e-09,-1.04955e-12,-38655.5,21.3338], Tmin=(539.127,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-322.261,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C-C': 3, 'C-H': 6, 'C=O': 1, 'C=C': 1}
1D rotors:
pivots: [4, 5], dihedral: [10, 4, 5, 1], rotor symmetry: 3, max scan energy: 8.31 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O       0.16901700    1.21671100   -0.35894700
O       2.36460600    1.61522000   -0.71009500
C       1.59510200   -0.62108000   -0.00027600
C      -2.04636700    0.35838100    0.12304500
C      -0.58640700    0.10804200    0.03376400
C       0.16041400   -0.97330800    0.25487700
C       1.50608500    0.84846000   -0.40181700
H       2.06479000   -1.18807800   -0.81078200
H       2.24856900   -0.71683100    0.87312200
H      -2.43998900    0.68216800   -0.84494400
H      -2.56980300   -0.54646500    0.43339700
H      -2.25572600    1.15465400    0.84339000
H      -0.21028900   -1.93787300    0.56527200
""",
)

entry(
    index = 284,
    label = "P331",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {12,S}
4  C u0 p0 c0 {2,S} {3,D} {11,S}
5  C u1 p0 c0 {1,S} {13,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u1 p2 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.29838,0.0731756,-0.000244003,5.45772e-07,-4.44081e-10,-4608.7,13.643], Tmin=(10,'K'), Tmax=(405.427,'K')),
            NASAPolynomial(coeffs=[3.22603,0.0441757,-2.67745e-05,7.79739e-09,-8.76427e-13,-4358.63,16.9384], Tmin=(405.427,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-38.3382,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 3, 'C-H': 6, 'C=O': 1, 'C-O': 1, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [3, 5], dihedral: [7, 3, 5, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [3, 7], dihedral: [5, 3, 7, 2], rotor symmetry: 1, max scan energy: 9.10 kJ/mol
pivots: [4, 6], dihedral: [10, 4, 6, 1], rotor symmetry: 2, max scan energy: 0.49 kJ/mol (set as a FreeRotor)
* Invalidated! pivots: [5, 6], dihedral: [3, 5, 6, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
O      -0.45937200    0.70216000    1.91354600
O       2.75845500   -0.75685500   -1.70447500
C       1.73155500    0.46291600    0.13244000
C      -1.69869800   -1.18782100    1.08853800
C       0.54635700   -0.44372900    0.15850700
C      -0.51950200   -0.23146200    1.11174300
C       2.77338500    0.12384200   -0.91832000
H       1.43321000    1.50839100   -0.02132700
H       2.23836800    0.48827900    1.10617900
H      -2.41109500   -0.89799800    1.85953300
H      -2.19245800   -1.17050900    0.11218400
H      -1.36772900   -2.21542400    1.26702100
H       0.50159900   -1.26308800   -0.55089100
""",
)

entry(
    index = 285,
    label = "P332",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {4,S}
2  O u0 p2 c0 {7,S} {21,S}
3  C u0 p0 c0 {1,S} {5,S} {7,S} {9,S}
4  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
5  C u0 p0 c0 {3,S} {8,S} {12,S} {13,S}
6  C u0 p0 c0 {4,S} {8,S} {14,S} {15,S}
7  C u0 p0 c0 {2,S} {3,S} {16,S} {17,S}
8  C u1 p0 c0 {5,S} {6,S} {18,S}
9  C u0 p0 c0 {3,S} {10,D} {19,S}
10 C u0 p0 c0 {4,S} {9,D} {20,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81982,0.010542,0.000265228,-4.9706e-07,2.8497e-10,-15805.9,13.8868], Tmin=(10,'K'), Tmax=(560.543,'K')),
            NASAPolynomial(coeffs=[-2.09211,0.092793,-6.20844e-05,1.97264e-08,-2.38248e-12,-15772.6,33.3719], Tmin=(560.543,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-131.493,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (503.026,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 10, 'C=C': 1, 'C-C': 7, 'H-O': 1, 'C-O': 3}
1D rotors:
pivots: [2, 7], dihedral: [21, 2, 7, 3], rotor symmetry: 1, max scan energy: 23.11 kJ/mol
* Invalidated! pivots: [3, 7], dihedral: [1, 3, 7, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       2.94047700    1.06985300   -2.30917100
O       2.97847300    0.76932500    0.48600900
C       1.98461700    0.19731900   -1.65740700
C       2.13249700    1.86886200   -3.19145600
C       1.64867000   -0.92215600   -2.67096900
C       1.83835800    0.99953100   -4.43451000
C       2.63667900   -0.30036000   -0.37501200
C       1.30370900   -0.33825700   -4.01177900
C       0.78628400    1.12252800   -1.47648000
C       0.87257300    2.09776000   -2.37321500
H       2.68901300    2.77296900   -3.44450300
H       2.53059700   -1.58024800   -2.74653400
H       0.82828300   -1.54874700   -2.30033600
H       1.13727800    1.50559700   -5.10915400
H       2.78133200    0.88914700   -4.99481900
H       1.94248700   -0.94638100    0.16956900
H       3.51987300   -0.89897500   -0.64148500
H       0.77492200   -0.95103600   -4.73263000
H      -0.01373600    0.93891600   -0.77197500
H       0.15275800    2.88162300   -2.56930600
H       3.41188600    1.42480400   -0.07473700
""",
)

entry(
    index = 286,
    label = "P333",
    molecule = 
"""
multiplicity 3
1  O u0 p2 c0 {3,S} {10,S}
2  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3  C u1 p0 c0 {1,S} {2,S} {7,S}
4  C u1 p0 c0 {2,S} {8,S} {9,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91596,0.00718164,0.000144165,-4.38414e-07,4.31724e-10,13545.9,10.2495], Tmin=(10,'K'), Tmax=(310.349,'K')),
            NASAPolynomial(coeffs=[2.66934,0.0321577,-1.9609e-05,5.88503e-09,-6.86124e-13,13580.4,14.114], Tmin=(310.349,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (112.647,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (228.648,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C-C': 2, 'C-H': 5, 'C-O': 1}
1D rotors:
* Invalidated! pivots: [1, 3], dihedral: [10, 1, 3, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 3], dihedral: [4, 2, 3, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [2, 4], dihedral: [3, 2, 4, 8], rotor symmetry: 2, max scan energy: 9.76 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.73949600   -0.14903900   -1.31574100
C      -0.31617500   -0.44397100    0.01819900
C       1.14970400   -0.14605700   -0.07882900
C      -1.15710600    0.43535700   -0.85189200
H      -0.60874100   -0.32807600    1.07516300
H      -0.52783600   -1.50047500   -0.22846500
H       1.83730500   -0.45682200    0.69840100
H      -2.06651300    0.06471200   -1.30881900
H      -0.96974000    1.50344800   -0.87987400
H       1.06024200    0.06322900   -1.96925800
""",
)

entry(
    index = 287,
    label = "P334",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {1,S} {3,D} {11,S}
5  C u0 p0 c0 {1,S} {6,S} {12,D}
6  O u0 p2 c0 {5,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 O u0 p2 c0 {5,D}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76615,0.0363906,-1.13977e-06,-1.79883e-08,7.39445e-12,-20843.4,11.5549], Tmin=(10,'K'), Tmax=(1128.89,'K')),
            NASAPolynomial(coeffs=[10.0704,0.0308211,-1.60205e-05,3.95771e-09,-3.79638e-13,-23335.2,-24.3563], Tmin=(1128.89,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-173.258,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (295.164,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C-C': 4, 'C-H': 5, 'C=O': 1, 'C-O': 1, 'C=C': 1}
1D rotors:
pivots: [1, 7], dihedral: [13, 1, 7, 2], rotor symmetry: 1, max scan energy: 56.32 kJ/mol
pivots: [3, 7], dihedral: [5, 3, 7, 1], rotor symmetry: 1, max scan energy: 23.53 kJ/mol
pivots: [4, 5], dihedral: [9, 4, 5, 3], rotor symmetry: 3, max scan energy: 5.39 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.22746900    1.25844300    0.50552100
O      -0.94031200    0.32479800    2.09593700
C      -0.73475400   -0.43310900   -0.18328900
C       2.08911400   -0.49793200   -0.11682100
C       0.68765500   -0.95219900   -0.06527600
C      -0.23343500   -1.82958300    0.11519600
C      -1.27875500    0.38849100    0.93864000
H      -1.15776800   -0.19435800   -1.15792300
H       2.77920900   -1.32793100    0.04756000
H       2.26184600    0.26012700    0.65282700
H       2.31125300   -0.03851500   -1.08472900
H      -0.56767100   -2.82434500    0.34874700
H      -2.51980600    1.74893200    1.28794000
""",
)

entry(
    index = 288,
    label = "P335",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  C u0 p0 c0 {1,S} {3,D} {12,S}
5  C u0 p0 c0 {3,S} {6,S} {13,D}
6  O u0 p2 c0 {1,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 O u0 p2 c0 {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89243,0.0180067,5.56647e-05,-8.50813e-08,3.50393e-11,-39136.4,10.5255], Tmin=(10,'K'), Tmax=(836.004,'K')),
            NASAPolynomial(coeffs=[2.61719,0.043477,-2.47876e-05,6.78796e-09,-7.20817e-13,-39600,12.4013], Tmin=(836.004,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-325.363,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C-C': 3, 'C-H': 6, 'C=O': 1, 'C=C': 1}
1D rotors:
pivots: [4, 5], dihedral: [10, 4, 5, 6], rotor symmetry: 3, max scan energy: 3.40 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O      -1.74899000   -0.23748000    0.73094300
O      -0.16742000   -1.30874500    1.94116000
C      -1.76317100    0.59611000   -0.43229400
C       1.91168100   -0.21036800    0.02642300
C       0.43721100    0.00834800   -0.01096400
C      -0.32838600    0.70796300   -0.84999800
C      -0.45630400   -0.60743300    1.01294500
H      -2.39331400    0.12618200   -1.19488900
H      -2.20634200    1.56217200   -0.16812100
H       2.32535700    0.13943200    0.97658200
H       2.14080200   -1.27797500   -0.03690700
H       2.41661100    0.30774800   -0.79013100
H      -0.00706100    1.28119300   -1.71020300
""",
)

entry(
    index = 289,
    label = "P336",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  C u0 p0 c0 {2,S} {5,D} {9,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  C u0 p0 c0 {3,D} {12,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 O u1 p2 c0 {4,S}
11 O u1 p2 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67304,0.0360018,1.85027e-07,-2.14761e-08,9.57812e-12,-5158.07,12.478], Tmin=(10,'K'), Tmax=(984.691,'K')),
            NASAPolynomial(coeffs=[6.72677,0.0363493,-1.97703e-05,5.18626e-09,-5.30212e-13,-6377.71,-5.34668], Tmin=(984.691,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-42.8785,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C=C': 2, 'C-C': 2, 'C-H': 6}
1D rotors:
pivots: [3, 4], dihedral: [8, 3, 4, 5], rotor symmetry: 3, max scan energy: 1.87 kJ/mol
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 7], invalidation reason: Inconsistent initial and final conformers But unable to propose troubleshooting methods.Inconsistent initial and final conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 6], dihedral: [3, 4, 6, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [5, 7], dihedral: [4, 5, 7, 12], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
O       0.14721300    2.38379300    1.01756500
O      -0.11525900    2.32474400   -1.04985100
C      -0.64047100   -0.50161700   -1.20522500
C      -0.35606200    0.21239700    0.07932500
C      -0.31332500   -0.40649700    1.33998700
C      -0.10625100    1.64757300    0.01965500
C      -0.52303200   -1.73780500    1.57609500
H       0.09867200   -1.28737500   -1.39369200
H      -1.62608500   -0.97844300   -1.18353800
H      -0.61851200    0.19280700   -2.04582500
H      -0.09446700    0.24031300    2.18532500
H      -0.47245800   -2.13856600    2.58038200
H      -0.74531800   -2.43577500    0.77784100
""",
)

entry(
    index = 290,
    label = "P337",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  C u0 p0 c0 {1,S} {6,S} {11,D}
5  C u0 p0 c0 {3,D} {12,S} {13,S}
6  O u0 p2 c0 {1,S} {4,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 O u0 p2 c0 {4,D}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83329,0.016738,0.000210137,-8.32354e-07,1.10626e-09,-21684.3,11.5239], Tmin=(10,'K'), Tmax=(189.942,'K')),
            NASAPolynomial(coeffs=[2.39201,0.04709,-2.95569e-05,8.93551e-09,-1.03933e-12,-21629.6,16.0832], Tmin=(189.942,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-180.239,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C-C': 3, 'C-H': 6, 'C=O': 1, 'C=C': 1}
1D rotors:
pivots: [3, 4], dihedral: [1, 3, 4, 8], rotor symmetry: 3, max scan energy: 8.26 kJ/mol
* Invalidated! pivots: [3, 5], dihedral: [1, 3, 5, 7], invalidation reason: Another conformer for C5H6O2[113] exists which is 1.75 kJ/mol lower.Another conformer for C5H6O2[113] exists which is 1.75 kJ/mol lower.


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.61618400   -0.47143300   -1.83134100
O       0.13988800    1.72339500   -2.18537300
C      -0.33879300   -0.01038800   -0.33961800
C      -1.59881200    0.16321100    0.46228900
C       0.82062500   -0.71777800    0.23664000
C      -0.16166000    0.74374200   -1.58422700
C       0.94645700   -1.05083100    1.52020300
H      -1.95023900   -0.79824400    0.84451500
H      -1.40684200    0.82571600    1.31072200
H      -2.38395300    0.61143400   -0.14613200
H       1.61848600   -0.94206600   -0.46485900
H       1.84121400   -1.54393200    1.88002100
H       0.18019300   -0.83677900    2.25611700
""",
)

entry(
    index = 291,
    label = "P338",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {2,S} {12,D}
5  C u0 p0 c0 {1,S} {3,S} {13,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {4,D}
13 O u0 p2 c0 {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79206,0.0307014,2.43145e-05,-5.35908e-08,2.305e-11,-20833.3,11.8666], Tmin=(10,'K'), Tmax=(893.032,'K')),
            NASAPolynomial(coeffs=[6.48385,0.0385381,-2.22629e-05,6.12488e-09,-6.50271e-13,-22107.3,-5.25658], Tmin=(893.032,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-173.175,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 5, 'C-H': 6, 'C=O': 2}
1D rotors:
pivots: [3, 7], dihedral: [4, 3, 7, 2], rotor symmetry: 1, max scan energy: 30.29 kJ/mol
pivots: [5, 7], dihedral: [11, 5, 7, 2], rotor symmetry: 3, max scan energy: 3.06 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.41172200   -1.24260900   -3.86218900
O      -0.37345200   -0.75698700    0.04147100
C       0.59902200    0.12660300   -1.93132800
C      -0.76335600    0.78243100   -2.34182700
C       1.98166400   -1.13006400   -0.18707000
C      -0.29029500   -0.40672100   -3.02375300
C       0.63222500   -0.59548000   -0.61544400
H       1.52243400    0.59265800   -2.26186000
H      -1.53693000    0.64490600   -1.58937000
H      -0.75119400    1.73980200   -2.85231100
H       2.39994900   -1.77034100   -0.96967400
H       2.68317700   -0.30336600   -0.03555200
H       1.87598800   -1.69413600    0.73833300
""",
)

entry(
    index = 292,
    label = "P339",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {7,S}
2  C u0 p0 c0 {1,S} {9,S} {13,S} {14,S}
3  C u0 p0 c0 {5,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {6,S} {7,D} {16,S}
5  C u0 p0 c0 {3,S} {9,D} {17,S}
6  C u0 p0 c0 {4,S} {8,D} {15,S}
7  C u0 p0 c0 {1,S} {4,D} {18,S}
8  C u0 p0 c0 {6,D} {19,S} {20,S}
9  C u1 p0 c0 {2,S} {5,D}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.01261,0.105759,-0.000345755,8.61518e-07,-7.75559e-10,25997.6,16.3104], Tmin=(10,'K'), Tmax=(377.849,'K')),
            NASAPolynomial(coeffs=[1.37381,0.0770243,-4.87372e-05,1.46853e-08,-1.6947e-12,26450.4,26.9748], Tmin=(377.849,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (216.126,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (465.61,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 11, 'C=C': 3, 'C-C': 3, 'C-O': 2}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [7, 1, 2, 9], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [1, 7], dihedral: [2, 1, 7, 4], rotor symmetry: 1, max scan energy: 21.79 kJ/mol
pivots: [2, 9], dihedral: [1, 2, 9, 5], rotor symmetry: 1, max scan energy: 9.17 kJ/mol
pivots: [3, 5], dihedral: [10, 3, 5, 9], rotor symmetry: 3, max scan energy: 6.87 kJ/mol
pivots: [4, 6], dihedral: [7, 4, 6, 8], rotor symmetry: 1, max scan energy: 31.85 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       0.01303000    0.98603400   -0.44857600
C      -0.72097900   -0.24374300   -0.25699200
C      -1.62885000   -0.48849000    3.60078100
C       2.10782000    0.03412300    0.35187800
C      -1.11430700    0.10273200    2.31321700
C       3.53589500    0.20899000    0.54443400
C       1.34242600    1.00027900   -0.18141100
C       4.35952700   -0.70334200    1.07437600
C      -1.10874900   -0.48274300    1.14383300
H      -2.42821700    0.13225600    4.01864800
H      -2.01810900   -1.49584400    3.44735900
H      -0.83220100   -0.53420800    4.35041000
H      -0.13601500   -1.08097400   -0.65586500
H      -1.60980700   -0.12819600   -0.88124500
H       3.94976100    1.16437000    0.22582900
H       1.67169500   -0.90477700    0.67522700
H      -0.70345000    1.11685700    2.37941200
H       1.76038300    1.95981200   -0.46942300
H       5.41845800   -0.50900500    1.19138100
H       3.99814500   -1.67155400    1.40603800
""",
)

entry(
    index = 293,
    label = "P340",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {5,D} {6,S}
4  C u0 p0 c0 {1,S} {5,S} {12,D}
5  C u0 p0 c0 {3,D} {4,S} {13,S}
6  O u0 p2 c0 {1,S} {3,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84807,0.0186371,5.98553e-05,-9.72405e-08,4.28529e-11,-34262.5,10.644], Tmin=(10,'K'), Tmax=(772.948,'K')),
            NASAPolynomial(coeffs=[2.29627,0.0448163,-2.61684e-05,7.33183e-09,-7.94667e-13,-34564.8,14.2239], Tmin=(772.948,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-284.865,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C-C': 3, 'C-H': 6, 'C=O': 1, 'C=C': 1}
1D rotors:
pivots: [4, 5], dihedral: [10, 4, 5, 1], rotor symmetry: 3, max scan energy: 4.33 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O      -0.01063500    0.40299800   -1.12258500
O      -2.69296600    0.08067900    1.17196200
C      -1.42105500    0.55924100   -0.85991200
C       2.02802700   -0.30924600   -0.09282500
C       0.56205100   -0.08644200    0.00515900
C      -1.62812700    0.09443600    0.59197400
C      -0.29501000   -0.29079700    1.03204000
H      -1.69042800    1.60864400   -0.99226600
H      -1.98170700   -0.05533800   -1.56651400
H       2.53297600    0.63026500   -0.33498400
H       2.24543100   -1.01241800   -0.90188600
H       2.42761200   -0.70159900    0.84139900
H      -0.04415300   -0.67184700    2.00894900
""",
)

entry(
    index = 294,
    label = "P341",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {4,S} {11,S}
4  C u0 p0 c0 {3,S} {5,D} {10,S}
5  C u0 p0 c0 {4,D} {12,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u1 p2 c0 {2,S}
10 O u1 p2 c0 {4,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77484,0.0389366,1.60715e-06,-2.83059e-08,1.28336e-11,-5396.96,12.527], Tmin=(10,'K'), Tmax=(992.788,'K')),
            NASAPolynomial(coeffs=[10.1074,0.0328613,-1.85839e-05,4.97501e-09,-5.13506e-13,-7612.31,-22.8027], Tmin=(992.788,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-44.8061,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (295.164,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C=C': 2, 'C-C': 2, 'C-H': 6}
1D rotors:
pivots: [3, 4], dihedral: [8, 3, 4, 1], rotor symmetry: 3, max scan energy: 3.78 kJ/mol
pivots: [5, 6], dihedral: [4, 5, 6, 2], rotor symmetry: 1, max scan energy: 30.28 kJ/mol
pivots: [4, 5], dihedral: [1, 4, 5, 6], rotor symmetry: 1, max scan energy: 30.81 kJ/mol
* Invalidated! pivots: [6, 7], dihedral: [2, 6, 7, 12], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
O      -1.77419400    0.72559600   -1.74847400
O       0.65435800    0.42331400    1.68928400
C      -1.98565500    0.05192800    0.53645700
C      -1.22295000    0.57349900   -0.65996500
C       0.19644300    0.91922500   -0.57939800
C       1.07816600    0.83482600    0.57516200
C       2.45092900    1.22436900    0.44938100
H      -1.95581200    0.76832100    1.36011400
H      -3.01489700   -0.13177700    0.23070600
H      -1.53266900   -0.86574700    0.91750400
H       0.60557300    1.27942100   -1.51808500
H       2.86748500    1.58478400   -0.48302200
H       3.08434700    1.15165700    1.32340200
""",
)

entry(
    index = 295,
    label = "P342",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {5,D} {6,S}
4  C u0 p0 c0 {2,S} {5,S} {12,D}
5  C u0 p0 c0 {3,D} {4,S} {13,S}
6  O u0 p2 c0 {1,S} {3,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7503,0.0357918,-3.15524e-06,-1.48552e-08,6.30873e-12,-15805.2,11.0534], Tmin=(10,'K'), Tmax=(1117.1,'K')),
            NASAPolynomial(coeffs=[8.77319,0.0316267,-1.61199e-05,3.95656e-09,-3.79663e-13,-17789.7,-17.5951], Tmin=(1117.1,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-131.379,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C-C': 3, 'C-H': 6, 'C=O': 1, 'C=C': 1}
1D rotors:
pivots: [4, 6], dihedral: [10, 4, 6, 2], rotor symmetry: 3, max scan energy: 2.74 kJ/mol
pivots: [6, 7], dihedral: [2, 6, 7, 5], rotor symmetry: 1, max scan energy: 40.81 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O       2.35969100    0.68821300   -1.16074900
O      -0.29458600   -0.94247200    1.48276300
C       2.54713700   -0.12056300    0.09226800
C      -2.32646400   -0.22472600    0.44283900
C       1.29393600    0.27292600   -0.47246800
C      -0.81743000   -0.33918500    0.56290000
C      -0.03547100    0.32494200   -0.50216900
H       2.96971500    0.43913000    0.91880600
H       2.93108200   -1.11928500   -0.08131300
H      -2.63051500    0.82697500    0.44695100
H      -2.79784100   -0.74651800    1.27411700
H      -2.66726100   -0.65525800   -0.50428200
H      -0.53427200    0.85315700   -1.30598100
""",
)

entry(
    index = 296,
    label = "P343",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {5,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u0 p2 c0 {3,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u1 p2 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93572,0.00681332,0.000337206,-1.54469e-06,2.38708e-09,-35940.4,12.4973], Tmin=(10,'K'), Tmax=(198.51,'K')),
            NASAPolynomial(coeffs=[2.93326,0.0406401,-2.13694e-05,5.34738e-09,-5.22453e-13,-35927.4,15.0364], Tmin=(198.51,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-298.729,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (295.164,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'H-O': 1, 'C-C': 2, 'C-H': 6, 'C=C': 1}
1D rotors:
pivots: [1, 5], dihedral: [13, 1, 5, 3], rotor symmetry: 1, max scan energy: 68.19 kJ/mol
pivots: [3, 4], dihedral: [5, 3, 4, 9], rotor symmetry: 3, max scan energy: 11.86 kJ/mol
pivots: [3, 5], dihedral: [4, 3, 5, 1], rotor symmetry: 1, max scan energy: 7.59 kJ/mol
* Invalidated! pivots: [5, 6], dihedral: [1, 5, 6, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       0.67803000    1.50811200   -0.52796000
O       2.76588200    0.65281400    0.80703200
C      -0.49199600   -0.59593800   -0.45541200
C      -1.80123500   -0.06799000    0.16261000
C       0.69344100    0.23644600   -0.12212300
C       1.85239800   -0.16785400    0.59789600
H      -0.29997500   -1.62020800   -0.12311900
H      -0.59933300   -0.62786500   -1.54714800
H      -1.99600100    0.95471500   -0.16427500
H      -2.64381500   -0.69312500   -0.14121400
H      -1.74826700   -0.07259200    1.25396700
H       1.90824300   -1.20788800    0.95272200
H       1.53022500    1.87406000   -0.20450000
""",
)

entry(
    index = 297,
    label = "P344",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  O u0 p2 c0 {2,S} {13,S}
5  C u1 p0 c0 {2,S} {12,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {5,D}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.62135,0.0411045,-2.25708e-05,4.88852e-09,-1.1307e-13,-28431.9,12.6124], Tmin=(10,'K'), Tmax=(1413.62,'K')),
            NASAPolynomial(coeffs=[12.0351,0.0234576,-1.03829e-05,2.2236e-09,-1.87e-13,-31426.2,-33.0687], Tmin=(1413.62,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-236.424,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (295.164,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C-C': 3, 'C-H': 6, 'C=O': 1, 'C-O': 1}
1D rotors:
pivots: [1, 4], dihedral: [13, 1, 4, 3], rotor symmetry: 1, max scan energy: 16.64 kJ/mol
pivots: [3, 4], dihedral: [5, 3, 4, 1], rotor symmetry: 1, max scan energy: 19.45 kJ/mol
pivots: [3, 5], dihedral: [4, 3, 5, 10], rotor symmetry: 3, max scan energy: 11.41 kJ/mol
* Invalidated! pivots: [4, 6], dihedral: [1, 4, 6, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.73315500    1.10871100   -0.75881100
O      -1.46427800   -1.09420500   -2.31714100
C       0.35700100   -0.45453900    0.69947000
C      -0.87535500   -0.16128900   -0.15489100
C       1.65891900   -0.49863300   -0.10360900
C      -1.13537000   -1.27077200   -1.19673900
H       0.18980100   -1.40400000    1.21686400
H       0.41243800    0.32537600    1.46446600
H      -1.77477000   -0.20372700    0.48234000
H       1.81205600    0.43924000   -0.63938300
H       2.51437600   -0.66116800    0.55597500
H       1.64477300   -1.31120100   -0.83661700
H      -1.32773300    1.15324800   -1.51649600
""",
)

entry(
    index = 298,
    label = "P35",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 C u0 p0 c0 {1,S} {2,D} {7,S}
4 C u1 p0 c0 {1,S} {8,S} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93577,0.00369923,9.14314e-05,-1.68227e-07,9.44546e-11,51559.3,8.20572], Tmin=(10,'K'), Tmax=(575.97,'K')),
            NASAPolynomial(coeffs=[1.9458,0.0322717,-2.13998e-05,6.84138e-09,-8.36136e-13,51543.8,14.5841], Tmin=(575.97,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (428.66,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (203.705,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'C-H': 5, 'C-C': 3}
1D rotors:
pivots: [1, 4], dihedral: [2, 1, 4, 8], rotor symmetry: 2, max scan energy: 24.33 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       0.07859400   -0.50930100   -0.09104800
C       0.85315700    0.62153500   -0.77677800
C       1.13637600    0.44932000    0.46672000
C      -1.32506600   -0.35138800    0.25051900
H       0.39317000   -1.53093000   -0.30418400
H       0.94119500    1.18484900   -1.69116600
H       1.63795600    0.76117500    1.36802100
H      -1.72671100    0.62914500    0.47779500
H      -1.99178900   -1.20393100    0.28430200
""",
)

entry(
    index = 299,
    label = "P60",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {3,S} {8,S}
2  C u0 p0 c0 {1,D} {5,S} {7,S}
3  C u0 p0 c0 {1,S} {4,D} {6,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  C u0 p0 c0 {2,S} {9,D} {10,S}
6  O u1 p2 c0 {3,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  O u0 p2 c0 {5,D}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49069,0.0463923,-3.57004e-05,1.5058e-08,-2.83807e-12,-7618.34,11.986], Tmin=(10,'K'), Tmax=(995.807,'K')),
            NASAPolynomial(coeffs=[5.54609,0.038136,-2.3264e-05,6.73222e-09,-7.47857e-13,-8027.7,2.07846], Tmin=(995.807,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-63.4012,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-H': 5, 'C=O': 1, 'C-O': 1, 'C-C': 2}
1D rotors:
pivots: [3, 5], dihedral: [4, 3, 5, 1], rotor symmetry: 1, max scan energy: 21.73 kJ/mol
pivots: [4, 7], dihedral: [3, 4, 7, 2], rotor symmetry: 1, max scan energy: 31.39 kJ/mol
* Invalidated! pivots: [5, 6], dihedral: [1, 5, 6, 11], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
O      -1.46472800   -0.54833400   -1.28131300
O       3.21934700   -0.70443800    0.78949500
C      -0.02645800    0.64476600    0.19914500
C       1.00583700   -0.20181100    0.10277900
C      -1.30679400    0.43285800   -0.54014200
C      -2.34924600    1.39798300   -0.36781600
C       2.25977300    0.02846000    0.84229400
H       0.94277700   -1.08368500   -0.52670300
H       0.05154200    1.52459100    0.83417800
H       2.26999200    0.94569200    1.47128100
H      -2.23635800    2.26371800    0.27384200
H      -3.27994700    1.25086400   -0.90050900
""",
)

entry(
    index = 300,
    label = "P69",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,D}
3  C u1 p0 c0 {2,S} {4,S} {10,S}
4  C u0 p0 c0 {3,S} {5,D} {11,S}
5  C u0 p0 c0 {4,D} {12,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u0 p2 c0 {2,D}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 O u0 p2 c0 {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91551,0.00557026,0.000153295,-3.26813e-07,2.19679e-10,-26332.1,11.7791], Tmin=(10,'K'), Tmax=(459.423,'K')),
            NASAPolynomial(coeffs=[0.827585,0.047142,-3.03865e-05,9.30791e-09,-1.08852e-12,-26203.3,22.588], Tmin=(459.423,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-218.952,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (278.535,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'C-H': 5, 'C=O': 2, 'C-C': 3}
1D rotors:
pivots: [3, 4], dihedral: [8, 3, 4, 1], rotor symmetry: 3, max scan energy: 4.29 kJ/mol
* Invalidated! pivots: [4, 5], dihedral: [1, 4, 5, 6], invalidation reason: Bond ([[1, 7]]) broke during the scan. But unable to propose troubleshooting methods.Bond ([[1, 7]]) broke during the scan. But unable to propose troubleshooting methods.
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 7], invalidation reason: The rotor scan has a barrier of 133.50 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)The rotor scan has a barrier of 133.50 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
* Invalidated! pivots: [6, 7], dihedral: [5, 6, 7, 2], invalidation reason: Bond ([[1, 7]]) broke during the scan. But unable to propose troubleshooting methods.Bond ([[1, 7]]) broke during the scan. But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
O       0.38953000   -0.03144400    0.84332400
O       2.39776200   -0.01421300    1.95106400
C      -1.85341500   -0.41490800    0.02412700
C      -0.76356900   -0.71546900    0.98096700
C      -0.69279800   -1.60986600    2.04719100
C       0.56690200   -1.48541400    2.61161400
C       1.29401100   -0.48283000    1.86919300
H      -1.52622600   -0.60429100   -1.00350600
H      -2.73100900   -1.02704700    0.23395100
H      -2.13565100    0.64147700    0.08194900
H      -1.49133300   -2.26797900    2.35416500
H       0.98810400   -2.01205600    3.45251800
""",
)

entry(
    index = 301,
    label = "P345",
    molecule = 
"""
multiplicity 1
1  O u0 p2 c0 {4,S} {6,S}
2  O u0 p2 c0 {7,S} {13,S}
3  C u0 p0 c0 {5,S} {6,S} {8,S} {9,S}
4  C u0 p0 c0 {1,S} {5,D} {7,S}
5  C u0 p0 c0 {3,S} {4,D} {10,S}
6  C u1 p0 c0 {1,S} {3,S} {11,S}
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
            NASAPolynomial(coeffs=[3.88277,0.00656314,0.000152847,-2.75977e-07,1.49709e-10,-4515.9,11.2942], Tmin=(10,'K'), Tmax=(604.817,'K')),
            NASAPolynomial(coeffs=[0.67847,0.0559413,-3.95195e-05,1.31147e-08,-1.63574e-12,-4643.83,20.88], Tmin=(604.817,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-37.6012,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C=C': 1, 'H-O': 1, 'C-O': 3, 'C-C': 3}
1D rotors:
pivots: [2, 7], dihedral: [13, 2, 7, 4], rotor symmetry: 1, max scan energy: 19.25 kJ/mol
* Invalidated! pivots: [4, 7], dihedral: [1, 4, 7, 2], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
O       0.07763200    1.15979200    0.77039300
O       2.90196200    0.61424900    0.28618100
C      -1.69346700   -0.07305200   -0.32213700
C       0.63061100   -0.10071700    0.44644500
C      -0.66457500   -0.82464700    0.52615100
C      -1.21284000    0.52487200    0.95385000
C       1.91948900   -0.33849300    0.23478400
H      -2.69231800   -0.49547300   -0.28971400
H      -1.40114300    0.37092400   -1.26783300
H      -0.83842600   -1.81281700    0.92710300
H      -1.80614800    0.84232600    1.80032500
H       2.29136100   -1.32991500    0.01846000
H       2.48711800    1.46001200    0.49654900
""",
)

entry(
    index = 302,
    label = "P346",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {9,S}
2  C u0 p0 c0 {6,D} {10,S} {11,S}
3  O u0 p2 c0 {1,S} {6,S}
4  O u0 p2 c0 {1,S} {7,S}
5  C u0 p0 c0 {1,S} {8,T}
6  C u1 p0 c0 {2,D} {3,S}
7  O u0 p2 c0 {4,S} {13,S}
8  C u0 p0 c0 {5,T} {12,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.56304,0.0394254,0.000124724,-5.34907e-07,5.68579e-10,32087.4,14.9848], Tmin=(10,'K'), Tmax=(346.687,'K')),
            NASAPolynomial(coeffs=[5.55177,0.0459592,-3.10931e-05,9.99154e-09,-1.21827e-12,31772.3,4.94197], Tmin=(346.687,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (266.827,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 1, 'H-O': 1, 'C-H': 4, 'C-O': 3, 'C=C': 1, 'O-O': 1, 'C#C': 1}
1D rotors:
pivots: [1, 4], dihedral: [7, 1, 4, 2], rotor symmetry: 1, max scan energy: 10.57 kJ/mol
* Invalidated! pivots: [1, 7], dihedral: [4, 1, 7, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 3], dihedral: [4, 2, 3, 13], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 4], dihedral: [3, 2, 4, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       0.62339500   -0.51245600   -0.40417700
O      -0.05160900   -2.34913000    0.80256300
O      -0.60148400   -1.54995400    1.87658100
C      -0.28024900   -1.65435900   -0.38440000
C       0.75789600    1.40219700   -1.85830800
C       0.01589200   -2.55837900   -1.48810600
C       0.17789400    0.59363800   -0.99541000
C       0.24803000   -3.28381100   -2.41402100
H      -1.30360900   -1.27098100   -0.41992400
H       1.70529600    1.13506900   -2.32426600
H       0.29623000    2.34169900   -2.13081200
H       0.45506900   -3.92928700   -3.23294600
H       0.16128500   -0.99427900    2.09921500
""",
)

entry(
    index = 303,
    label = "P347",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {10,S}
3  C u1 p0 c0 {1,S} {4,S} {11,S}
4  C u0 p0 c0 {3,S} {5,D} {6,S}
5  C u0 p0 c0 {4,D} {12,S} {13,S}
6  O u0 p2 c0 {2,S} {4,S}
7  O u0 p2 c0 {1,S} {8,S}
8  O u0 p2 c0 {2,S} {7,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88524,0.00653432,0.000158992,-2.90697e-07,1.60813e-10,3625.13,12.7077], Tmin=(10,'K'), Tmax=(586.93,'K')),
            NASAPolynomial(coeffs=[0.281866,0.0577928,-4.02463e-05,1.31188e-08,-1.61106e-12,3588.21,24.2539], Tmin=(586.93,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (30.0898,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 3, 'C-H': 5, 'C-O': 4, 'C=C': 1, 'O-O': 1}
1D rotors:
* Invalidated! pivots: [7, 8], dihedral: [1, 7, 8, 12], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       0.02589600   -0.69479200   -1.25843700
O      -1.91014800   -0.20615000    1.09879200
O      -1.92997900   -1.21022700   -0.00214000
C      -1.16692100    0.72533700    0.23507800
C      -1.27371300   -0.30169500   -0.89332200
C       0.29060600    0.75763000    0.50317100
C       0.92629000   -0.14150700   -0.35018800
C       2.25001700   -0.49565900   -0.42312300
H      -1.68599700    1.68293400    0.18406300
H      -1.85170300   -0.14511100   -1.80284000
H       0.77894100    1.33301800    1.27378500
H       2.96367500   -0.05620500    0.25871900
H       2.58990600   -1.21432000   -1.15515400
""",
)

entry(
    index = 304,
    label = "P348",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {6,S}
2  O u0 p2 c0 {4,S} {14,S}
3  O u0 p2 c0 {8,D}
4  C u0 p0 c0 {1,S} {2,S} {5,S} {9,S}
5  C u0 p0 c0 {4,S} {7,S} {10,S} {11,S}
6  C u0 p0 c0 {1,S} {7,D} {8,S}
7  C u0 p0 c0 {5,S} {6,D} {12,S}
8  C u0 p0 c0 {3,D} {6,S} {13,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70548,0.029128,5.80158e-05,-1.17543e-07,5.89516e-11,-49759.8,11.7209], Tmin=(10,'K'), Tmax=(706.348,'K')),
            NASAPolynomial(coeffs=[3.90577,0.049406,-3.05175e-05,8.93283e-09,-1.00202e-12,-50322.3,7.04313], Tmin=(706.348,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-413.751,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (324.264,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'C-C': 3, 'H-O': 1, 'C-H': 5, 'C-O': 3, 'C=C': 1}
1D rotors:
pivots: [2, 4], dihedral: [14, 2, 4, 1], rotor symmetry: 1, max scan energy: 20.13 kJ/mol
pivots: [6, 8], dihedral: [1, 6, 8, 3], rotor symmetry: 2, max scan energy: 39.14 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.10233700   -0.85998100   -0.99258600
O      -1.88155100   -1.03823200    0.51261200
O       3.32716400   -0.40229900   -0.17473500
C      -1.29858600   -0.23082300   -0.46715200
C      -0.82744700    1.07495900    0.20075600
C       0.97355700   -0.23860500   -0.39455200
C       0.65705100    0.85995600    0.29829500
C       2.29450600   -0.85719500   -0.60898200
H      -1.96221400   -0.09477900   -1.32515900
H      -1.32043700    1.18644500    1.16949500
H      -1.07153600    1.95526400   -0.40419000
H       1.36278400    1.48196100    0.82602800
H       2.26769700   -1.78840700   -1.20997600
H      -2.11851900   -1.88006200    0.10745800
""",
)

entry(
    index = 305,
    label = "P349",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {6,S}
3  O u0 p2 c0 {6,D}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {9,S}
5  C u0 p0 c0 {4,S} {7,S} {10,S} {11,S}
6  C u0 p0 c0 {2,S} {3,D} {4,S}
7  C u0 p0 c0 {5,S} {8,T}
8  C u0 p0 c0 {7,T} {12,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.62386,0.0326072,4.31507e-05,-1.26982e-07,8.15096e-11,1366.42,13.3725], Tmin=(10,'K'), Tmax=(571.215,'K')),
            NASAPolynomial(coeffs=[4.74436,0.0420956,-2.72864e-05,8.35262e-09,-9.73646e-13,955.603,6.11872], Tmin=(571.215,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (11.3102,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (278.535,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'C-C': 3, 'C-H': 4, 'C-O': 2, 'O-O': 1, 'C#C': 1}
1D rotors:
pivots: [4, 5], dihedral: [1, 4, 5, 7], rotor symmetry: 1, max scan energy: 18.71 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.08386600   -0.79702800   -0.35181100
O      -2.61371600    0.52330600    0.08673000
O      -1.06843700    2.22352400    0.14543900
C      -0.76775900   -0.21280200   -0.52997700
C       0.28785600   -0.87133100    0.35998100
C      -1.36919700    1.10069400   -0.06617100
C       1.60659800   -0.27989100    0.16632700
C       2.68470500    0.21676300   -0.01022000
H      -0.47634700   -0.21197300   -1.58257300
H      -0.02200600   -0.79426000    1.40643900
H       0.31447900   -1.93797500    0.11177500
H       3.63932200    0.65970500   -0.15785500
""",
)

entry(
    index = 306,
    label = "P350",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {7,S}
2 C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3 C u0 p0 c0 {2,S} {4,T}
4 C u0 p0 c0 {3,T} {8,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92132,0.00521975,9.04867e-05,-2.13319e-07,1.52359e-10,4251.67,9.53751], Tmin=(10,'K'), Tmax=(470.013,'K')),
            NASAPolynomial(coeffs=[3.73077,0.0223047,-1.3388e-05,4.01406e-09,-4.72068e-13,4098.78,8.49593], Tmin=(470.013,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (35.3364,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 1, 'H-O': 1, 'C-H': 3, 'C-O': 1, 'C#C': 1}
1D rotors:
pivots: [1, 2], dihedral: [7, 1, 2, 3], rotor symmetry: 1, max scan energy: 10.66 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.58094200    0.60133200    0.31600500
C      -0.70569500   -0.46273200   -0.04094700
C       0.71274800   -0.10816000    0.05491500
C       1.86766500    0.21768500    0.11612900
H      -0.91360100   -0.83098300   -1.05567300
H      -0.92865300   -1.27898000    0.65030600
H      -1.34260700    1.36531900   -0.21916400
H       2.89108400    0.49651700    0.17843000
""",
)

entry(
    index = 307,
    label = "P351",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {7,S} {9,S}
2  C u0 p0 c0 {4,D} {5,S} {6,S}
3  C u0 p0 c0 {1,S} {6,D} {10,S}
4  C u0 p0 c0 {2,D} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {2,S}
6  C u1 p0 c0 {2,S} {3,D}
7  O u0 p2 c0 {1,S} {8,S}
8  O u0 p2 c0 {7,S} {13,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78121,0.0134495,0.000195063,-4.36647e-07,2.83212e-10,14522.4,13.1242], Tmin=(10,'K'), Tmax=(536.754,'K')),
            NASAPolynomial(coeffs=[5.37555,0.0485534,-3.43416e-05,1.1365e-08,-1.41317e-12,13674.4,0.119572], Tmin=(536.754,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (120.673,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 2, 'H-O': 1, 'C-H': 4, 'C-O': 3, 'C=C': 2, 'O-O': 1}
1D rotors:
pivots: [2, 3], dihedral: [4, 2, 3, 13], rotor symmetry: 1, max scan energy: 25.65 kJ/mol
pivots: [2, 4], dihedral: [3, 2, 4, 1], rotor symmetry: 1, max scan energy: 42.42 kJ/mol
* Invalidated! pivots: [5, 7], dihedral: [1, 5, 7, 11], invalidation reason: The rotor scan has a barrier of 174.35 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)The rotor scan has a barrier of 174.35 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.58842500   -0.47493400    1.37046600
O      -1.96768300    0.49474700   -0.71709800
O      -2.34405000    1.76485000   -0.12932600
C      -1.01421000   -0.12728200    0.09940400
C      -0.80868600    0.04837600    2.39577200
C       0.22894200    0.68376000    0.42892900
C      -1.09828200   -0.11867300    3.68518400
C       0.29041900    0.73537800    1.74555000
H      -0.80416000   -1.04460600   -0.46217900
H       0.87393500    1.10253500   -0.32788100
H      -0.44578400    0.29744700    4.43870300
H      -1.97687400   -0.66844400    3.99288600
H      -3.06879700    1.48454700    0.44931800
""",
)

entry(
    index = 308,
    label = "P352",
    molecule = 
"""
multiplicity 2
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
13 O u1 p2 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86419,0.00845137,0.000175657,-3.67548e-07,2.33759e-10,776.539,14.1196], Tmin=(10,'K'), Tmax=(514.977,'K')),
            NASAPolynomial(coeffs=[1.75295,0.0528565,-3.52599e-05,1.11007e-08,-1.32622e-12,622.62,19.2984], Tmin=(514.977,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (6.41429,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 2, 'C-H': 5, 'C-O': 3, 'C=C': 2, 'O-O': 1}
1D rotors:
* Invalidated! pivots: [2, 4], dihedral: [3, 2, 4, 1], invalidation reason: Another conformer for s44_C5H5O3 exists which is 2.56 kJ/mol lower.Another conformer for s44_C5H5O3 exists which is 2.56 kJ/mol lower.


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.28677900   -0.03552200   -1.02497000
O      -2.08303300   -1.43503300    0.84923300
O      -2.37215900   -0.76235500    1.94669400
C      -1.36230000   -0.59394300   -0.12828400
C      -2.11019700   -0.60160500   -2.27776300
C      -0.48536500   -1.48319100   -0.95316200
C      -0.95669200   -1.49111700   -2.20302900
C      -2.89881100   -0.30471400   -3.31044800
H      -0.89409900    0.18911400    0.46908600
H       0.34778600   -2.03478100   -0.54467200
H      -0.57955300   -2.05118000   -3.04623800
H      -2.70838400   -0.74565600   -4.27856100
H      -3.73198200    0.37532000   -3.20008800
""",
)

entry(
    index = 309,
    label = "P353",
    molecule = 
"""
1 O u0 p2 c0 {4,D}
2 C u0 p0 c0 {3,D} {5,S} {6,S}
3 C u0 p0 c0 {2,D} {7,S} {8,S}
4 C u0 p0 c0 {1,D} {5,S} {9,S}
5 C u0 p1 c0 {2,S} {4,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8128,0.0209662,4.637e-06,-1.72883e-08,7.1259e-12,34615.9,9.83902], Tmin=(10,'K'), Tmax=(984.675,'K')),
            NASAPolynomial(coeffs=[5.1547,0.0240078,-1.29337e-05,3.36695e-09,-3.42143e-13,33939.9,1.29518], Tmin=(984.675,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (287.82,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 2, 'C=O': 1, 'C-H': 4, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [2, 5], dihedral: [3, 2, 5, 4], invalidation reason: 
* Invalidated! pivots: [4, 5], dihedral: [1, 4, 5, 2], invalidation reason: Internal coordinate error; Internal coordinate error; 


External symmetry: 1, optical isomers: 2

Geometry:
O       2.50948000    0.48577300   -0.59483400
C      -0.45551300   -0.28416700   -0.41903900
C      -1.77397400   -0.13569400   -0.12416500
C       1.80085000    0.39060600    0.40948300
C       0.42930300    0.62796500    0.16823900
H      -0.10041300   -1.17025800   -0.94893700
H      -2.48928500   -0.93434400   -0.29151300
H      -2.11871400    0.76510700    0.36895700
H       2.19826300    0.25505500    1.43177800
""",
)

entry(
    index = 310,
    label = "P354",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {5,D}
3 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
4 C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
5 C u0 p0 c0 {2,D} {3,S} {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.01925,-0.00209955,0.000100711,-1.63494e-07,8.42716e-11,-24029.8,8.57476], Tmin=(10,'K'), Tmax=(599.06,'K')),
            NASAPolynomial(coeffs=[0.33034,0.0346486,-2.1643e-05,6.43186e-09,-7.31851e-13,-23805.3,22.6668], Tmin=(599.06,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-199.806,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 2, 'C=O': 1, 'C-H': 4, 'C-O': 2}

External symmetry: 2, optical isomers: 1

Geometry:
O       0.00650200   -1.21467000   -0.23595600
O      -0.01078200    2.01428100    0.39128500
C      -1.02807800   -0.20327700   -0.28675900
C       1.03069300   -0.28523200    0.19186300
C      -0.00452100    0.84464400    0.16407700
H      -1.84434200   -0.39114800    0.41917700
H      -1.43272700   -0.05615000   -1.29400300
H       1.84743500   -0.18672600   -0.53143200
H       1.43582000   -0.52172300    1.18174800
""",
)

entry(
    index = 311,
    label = "P355",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,D} {6,S}
2  C u1 p0 c0 {1,S} {5,S} {8,S}
3  C u0 p0 c0 {1,D} {4,S} {7,S}
4  O u0 p2 c0 {3,S} {9,S}
5  O u0 p2 c0 {2,S} {10,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89061,0.00724622,0.000128133,-2.98027e-07,2.10272e-10,-25103.1,11.1037], Tmin=(10,'K'), Tmax=(471.499,'K')),
            NASAPolynomial(coeffs=[3.25979,0.0333817,-2.11327e-05,6.51386e-09,-7.73221e-13,-25274.6,11.2229], Tmin=(471.499,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-208.739,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 1, 'H-O': 2, 'C-H': 3, 'C-O': 2, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [1, 5], dihedral: [9, 1, 5, 3], invalidation reason: Inconsistent initial and final conformers But unable to propose troubleshooting methods.Inconsistent initial and final conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 4], dihedral: [10, 2, 4, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 4], dihedral: [5, 3, 4, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.76710700   -0.11339500   -0.70944700
O       0.76279500   -1.19546100   -0.74950700
C       0.15679100    0.73413400    0.52132200
C       1.12378700   -0.15737800    0.09768400
C      -1.17598800    0.75484100    0.14855400
H       0.47737300    1.49973000    1.21822800
H      -1.86665400    1.49535500    0.52804700
H       2.15248500   -0.13043400    0.43061000
H      -1.09771700   -0.74786400   -1.00748500
H       1.54590600   -1.60634700   -1.12379300
""",
)

entry(
    index = 312,
    label = "P356",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {4,S} {7,S}
2  O u0 p2 c0 {4,S} {15,S}
3  O u1 p2 c0 {6,S}
4  C u0 p0 c0 {1,S} {2,S} {5,S} {9,S}
5  C u0 p0 c0 {4,S} {8,S} {10,S} {11,S}
6  C u0 p0 c0 {3,S} {7,S} {12,S} {13,S}
7  C u0 p0 c0 {1,S} {6,S} {8,D}
8  C u0 p0 c0 {5,S} {7,D} {14,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78141,0.0197112,0.000222755,-7.08427e-07,7.08466e-10,-31880.1,13.0018], Tmin=(10,'K'), Tmax=(309.268,'K')),
            NASAPolynomial(coeffs=[1.95482,0.0584289,-3.8235e-05,1.19688e-08,-1.43139e-12,-31839.3,18.5035], Tmin=(309.268,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-265.027,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (353.365,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 3, 'H-O': 1, 'C-H': 6, 'C-O': 4, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [2, 4], dihedral: [15, 2, 4, 1], invalidation reason: Another conformer for s50_C5H7O3 exists which is 2.06 kJ/mol lower.Another conformer for s50_C5H7O3 exists which is 2.06 kJ/mol lower.
pivots: [6, 7], dihedral: [3, 6, 7, 1], rotor symmetry: 1, max scan energy: 11.67 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       0.30764100   -0.99940600    1.02002900
O      -1.43418600   -0.09608500    2.28988100
O       2.95841000    0.84474100   -0.65954200
C      -1.11521300   -0.72065300    1.07975200
C      -1.40190000    0.26086500   -0.07065100
C       2.36589900   -0.04515200    0.17857800
C       0.86807900   -0.04687000    0.19297500
C      -0.01329000    0.70403700   -0.45955300
H      -1.60950100   -1.69200200    0.98926600
H      -2.03532800    1.07003300    0.30104900
H      -1.92935200   -0.22787000   -0.89711000
H       2.75883300    0.11979400    1.20347200
H       2.74873000   -1.06030300   -0.05568500
H       0.23127200    1.49135800   -1.15417300
H      -1.19465100   -0.69412800    3.00657700
""",
)

entry(
    index = 312,
    label = "P357",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {5,D}
3  C u0 p0 c0 {2,S} {4,D} {11,S}
4  C u0 p0 c0 {3,D} {6,S} {7,S}
5  C u0 p0 c0 {2,D} {6,S} {12,S}
6  O u0 p2 c0 {4,S} {5,S}
7  O u0 p2 c0 {4,S} {13,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89387,0.0103464,0.000231197,-8.02851e-07,9.43229e-10,-31608.2,10.5532], Tmin=(10,'K'), Tmax=(215.08,'K')),
            NASAPolynomial(coeffs=[1.873,0.0479301,-3.09189e-05,9.60999e-09,-1.14544e-12,-31521.3,17.1972], Tmin=(215.08,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-262.768,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 2, 'H-O': 1, 'C-H': 5, 'C-O': 3, 'C=C': 2}
1D rotors:
pivots: [2, 6], dihedral: [13, 2, 6, 1], rotor symmetry: 1, max scan energy: 9.99 kJ/mol
pivots: [3, 4], dihedral: [8, 3, 4, 5], rotor symmetry: 3, max scan energy: 5.08 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O       1.56393100   -0.43345700   -0.58438800
O       2.64961000    1.54287600   -0.16049700
C      -2.04564400   -0.09932300    0.17797700
C      -0.57148600    0.02758100   -0.05054200
C       0.23438200    1.20546600    0.17317700
C       1.49879300    0.85067000   -0.16865100
C       0.27084200   -0.93173400   -0.50564200
H      -2.60404500    0.61685500   -0.43280900
H      -2.30238600    0.09582300    1.22381800
H      -2.39984900   -1.10148900   -0.07272100
H      -0.08420900    2.16902900    0.53424400
H       0.14928300   -1.95745500   -0.80611100
H       3.35362300    0.96159600   -0.47151300
""",
)

entry(
    index = 314,
    label = "P358",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {6,S}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,S} {2,D} {4,S}
4 C u0 p0 c0 {3,S} {5,T}
5 C u0 p0 c0 {4,T} {7,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91944,0.00472532,8.39897e-05,-1.69799e-07,1.01029e-10,-16428.5,9.07222], Tmin=(10,'K'), Tmax=(571.066,'K')),
            NASAPolynomial(coeffs=[3.66028,0.0250387,-1.79552e-05,5.93475e-09,-7.34802e-13,-16700.5,7.53645], Tmin=(571.066,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-136.627,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (153.818,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 1, 'C=O': 1, 'H-O': 1, 'C-O': 1, 'C-H': 1, 'C#C': 1}
1D rotors:
pivots: [1, 3], dihedral: [6, 1, 3, 2], rotor symmetry: 1, max scan energy: 50.05 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O      -1.44183100   -0.45688600    0.71761900
O      -0.77917400    1.65351000    0.27553600
C      -0.56318000    0.46924700    0.28144100
C       0.66795400   -0.13822400   -0.17706900
C       1.71218200   -0.57983000   -0.57187000
H      -2.23179000    0.02684900    1.00429500
H       2.63583900   -0.97466700   -0.92074800
""",
)

entry(
    index = 315,
    label = "P359",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {2,S} {10,S}
4  O u0 p2 c0 {1,S} {5,S}
5  O u0 p2 c0 {2,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96552,0.00210873,0.000103822,-1.85827e-07,1.07223e-10,9594.2,9.93462], Tmin=(10,'K'), Tmax=(447.774,'K')),
            NASAPolynomial(coeffs=[-0.413825,0.0411644,-2.67911e-05,8.31088e-09,-9.85057e-13,9987.05,27.5511], Tmin=(447.774,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (79.7584,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 2, 'C-H': 5, 'C-O': 2, 'O-O': 1}

External symmetry: 2, optical isomers: 2

Geometry:
O       0.60166800   -0.32195700   -1.38262900
O      -0.78199900    0.15535100   -1.31972200
C       1.17461400    0.14968800   -0.15725500
C      -1.18383300   -0.15820500    0.01910900
C       0.05474000    0.05057300    0.82030100
H       2.02266100   -0.50952300    0.05733200
H       1.54554400    1.18183600   -0.27384300
H      -2.00136400    0.52920000    0.26182100
H      -1.55849600   -1.19380100    0.07975600
H       0.12646400    0.11683800    1.89513000
""",
)