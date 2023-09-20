#!/usr/bin/env python
# encoding: utf-8

name = "2FFOH_thermo_1"
shortDesc = ""
longDesc = """
ARC v1.1.0
ARC project 2FFOH_thermo_1

Levels of theory used:

Conformers:       wb97xd/def2svp, software: gaussian (dft)
TS guesses:       None
Composite method: cbs-qb3, software: gaussian (composite) (using a fine grid)
Frequencies:      b3lyp/cbsb7, software: gaussian (dft)
Rotor scans:      b3lyp/cbsb7, software: gaussian (dft)
Using p-type bond additivity corrections for thermo

Using the following ESS settings: {'gaussian': ['local'], 'molpro': ['local']}

Considered the following species and TSs:
Species 2FFOH (run time: 0:51:29)
Species P1 (run time: 1:18:28)
Species P2 (run time: 1:42:17)
Species P3 (run time: 1:22:07)
Species P4 (run time: 1:46:35)
Species P5 (run time: 1:36:06)
Species P6 (run time: 2:57:03)
Species P7 (run time: 2:47:09)
Species P8 (run time: 2:42:27)
Species P9 (run time: 2:26:00)
Species P10 (run time: 0:57:09)
Species P11 (run time: 5:30:47)
Species P12 (run time: 10:01:52)
Species P13 (run time: 4:06:48)
Species P14 (run time: 5:03:14)
Species P15 (run time: 2:02:26)

Overall time since project initiation: 04:44:58
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

