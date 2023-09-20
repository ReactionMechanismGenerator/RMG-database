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
    index = 0,
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
    index = 1,
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
    index = 2,
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
    index = 3,
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
    index = 4,
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
    index = 5,
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
    index = 6,
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
    index = 7,
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
    index = 8,
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
    index = 9,
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
    index = 10,
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
    index = 11,
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
    index = 12,
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
    index = 13,
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