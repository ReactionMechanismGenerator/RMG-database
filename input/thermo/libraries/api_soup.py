# encoding: utf-8

name = "api_soup"
shortDesc = ""
longDesc = """
Thermo data for small species relevant to API oxidation
"""

entry(
    index = 0,
    label = "COCO",
    molecule = 
"""
1  O u0 p2 c0 {3,S} {4,S}
2  O u0 p2 c0 {3,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
4  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89,0.00664694,0.000111304,-2.35138e-07,1.472e-10,-47208.2,9.41851], Tmin=(10,'K'), Tmax=(546.761,'K')),
            NASAPolynomial(coeffs=[4.13549,0.0294819,-1.8915e-05,6.03134e-09,-7.44422e-13,-47603.2,5.01556], Tmin=(546.761,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-392.551,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (220.334,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
CBS-QB3

Bond corrections: {'C-O': 3, 'C-H': 5, 'H-O': 1}
1D rotors:
pivots: [1, 2], dihedral: [5, 1, 2, 3], rotor symmetry: 3, max scan energy: 6.80 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 28.18 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 10], rotor symmetry: 1, max scan energy: 20.04 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -1.28128500    0.19942300   -0.41871200
O      -0.47314300   -0.44230200    0.56182700
C       0.88368600   -0.50691400    0.21408300
O       1.51819200    0.75154800    0.19111700
H      -1.27585300   -0.36373100   -1.36210200
H      -2.29675000    0.22490600   -0.02449000
H      -0.93756300    1.21981400   -0.61259700
H       1.33456800   -1.17763100    0.95262200
H       1.01752800   -0.91386700   -0.79561800
H       1.48114000    1.10888300    1.08550500
""",
)

entry(
    index = 1,
    label = "OCOCO",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
3  O u0 p2 c0 {1,S} {2,S}
4  O u0 p2 c0 {1,S} {10,S}
5  O u0 p2 c0 {2,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91912,0.00461168,0.000124224,-2.24038e-07,1.22985e-10,-69810.9,10.7156], Tmin=(10,'K'), Tmax=(581.199,'K')),
            NASAPolynomial(coeffs=[0.342174,0.0474822,-3.35271e-05,1.09465e-08,-1.33595e-12,-69703.4,23.3791], Tmin=(581.199,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-580.477,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (249.434,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
CBS-QB3

Bond corrections: {'C-O': 4, 'C-H': 4, 'H-O': 2}
1D rotors:
pivots: [1, 2], dihedral: [6, 1, 2, 3], rotor symmetry: 1, max scan energy: 24.42 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: 
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 32.29 kJ/mol
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 11], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
O       1.87706300   -0.64202500   -0.30415700
C       1.06356600    0.49468300   -0.29680000
O       1.79104000    1.71765600   -0.32520400
C       2.27472600    2.05939600   -1.59440900
O       3.26328400    1.16254500   -2.07661500
H       2.35777400   -0.63486600   -1.14148600
H       0.52175300    0.49168600    0.64717600
H       0.35567200    0.49228100   -1.14162200
H       2.66545000    3.07608100   -1.50039900
H       1.47718800    2.02821000   -2.34595400
H       4.01920400    1.21829400   -1.47975900
""",
)

entry(
    index = 2,
    label = "COCOO",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  O u0 p2 c0 {1,S} {2,S}
4  O u0 p2 c0 {1,S} {5,S}
5  O u0 p2 c0 {4,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49034,0.0386092,-3.72171e-05,2.63704e-08,-8.98832e-12,-38900.6,9.5211], Tmin=(10,'K'), Tmax=(770.093,'K')),
            NASAPolynomial(coeffs=[4.40275,0.0311833,-1.75196e-05,4.78795e-09,-5.11141e-13,-38961.4,5.87489], Tmin=(770.093,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-323.514,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (245.277,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
CBS-QB3

Bond corrections: {'C-O': 3, 'C-H': 5, 'H-O': 1, 'O-O': 1}
1D rotors:
pivots: [1, 2], dihedral: [6, 1, 2, 3], rotor symmetry: 3, max scan energy: 6.46 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: 
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 3, max scan energy: 45.39 kJ/mol
pivots: [4, 5], dihedral: [3, 4, 5, 11], rotor symmetry: 1, max scan energy: 23.73 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -1.50943000    0.27446900    0.04859500
O      -0.34631300    0.16332500   -0.76962800
C       0.34163100    1.36903800   -0.93935600
O       1.03126800    1.77571400    0.22208000
O       2.16459000    0.88704400    0.38810000
H      -2.25162300    0.93671700   -0.41539400
H      -1.26550400    0.65525200    1.04550700
H      -1.92976700   -0.72670200    0.13535200
H       1.04560700    1.21443900   -1.75780200
H      -0.33717700    2.20963000   -1.13766200
H       1.73462500    0.09331600    0.74068500
""",
)

entry(
    index = 3,
    label = "COCOCO",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
4  O u0 p2 c0 {1,S} {2,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {2,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.69112,0.0312862,1.71415e-05,-3.98153e-08,1.65731e-11,-68377.5,10.4913], Tmin=(10,'K'), Tmax=(902.095,'K')),
            NASAPolynomial(coeffs=[4.10315,0.0425573,-2.33794e-05,6.22589e-09,-6.47008e-13,-68984.8,5.59202], Tmin=(902.095,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-568.525,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (324.264,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
CBS-QB3

Bond corrections: {'C-O': 5, 'C-H': 7, 'H-O': 1}
1D rotors:
pivots: [1, 2], dihedral: [7, 1, 2, 3], rotor symmetry: 3, max scan energy: 6.98 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: 
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: 
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: 
pivots: [5, 6], dihedral: [4, 5, 6, 14], rotor symmetry: 2, max scan energy: 25.00 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -2.19006100    0.01142900   -0.18610800
O      -1.05621000   -0.24998100   -1.01558200
C      -0.00678700   -0.90866800   -0.34032900
O      -0.31277500   -2.22929200    0.02580900
C      -0.47167000   -3.10692300   -1.07970600
O      -1.70244600   -2.97073900   -1.73240100
H      -1.90373300    0.62164700    0.67951900
H      -2.64681700   -0.91943900    0.15985100
H      -2.90170300    0.56730600   -0.79573200
H       0.84028700   -0.88052700   -1.03614900
H       0.24317300   -0.39132800    0.59230400
H       0.37094400   -2.95176000   -1.77322800
H      -0.43985300   -4.11492600   -0.67022900
H      -1.72778200   -2.07659100   -2.09619400
""",
)

entry(
    index = 4,
    label = "COOCO",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  O u0 p2 c0 {1,S} {4,S}
4  O u0 p2 c0 {2,S} {3,S}
5  O u0 p2 c0 {1,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.62507,0.0347464,-1.93193e-05,3.17404e-09,5.33831e-13,-40471.3,10.9392], Tmin=(10,'K'), Tmax=(1142.31,'K')),
            NASAPolynomial(coeffs=[7.90603,0.0247718,-1.28077e-05,3.21783e-09,-3.17035e-13,-41776.6,-11.7159], Tmin=(1142.31,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-336.523,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (245.277,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
CBS-QB3

Bond corrections: {'C-O': 3, 'C-H': 5, 'H-O': 1, 'O-O': 1}
1D rotors:
pivots: [1, 2], dihedral: [6, 1, 2, 3], rotor symmetry: 3, max scan energy: 11.87 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: The rotor scan has a barrier of 59.44264792178095 kJ/mol, which is higher than the maximal barrier for rotation (40 kJ/mol)
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 33.17 kJ/mol
pivots: [4, 5], dihedral: [3, 4, 5, 11], rotor symmetry: 1, max scan energy: 18.07 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -1.79012300   -0.06210600    0.06840400
O      -0.60490500   -0.83289100    0.18497600
O      -1.01243300   -2.22478100   -0.02388300
C      -0.38907400   -2.95476600    1.01020900
O      -0.92064500   -2.70529500    2.27735200
H      -2.51585600   -0.32863400    0.84240400
H      -1.45917600    0.97110100    0.19863200
H      -2.24031800   -0.18035000   -0.92173000
H       0.69091900   -2.76499100    0.97653700
H      -0.60783000   -3.99267100    0.75394600
H      -0.61150300   -1.83422700    2.54765800
""",
)

entry(
    index = 5,
    label = "COCOC",
    molecule = 
"""
1  O u0 p2 c0 {3,S} {4,S}
2  O u0 p2 c0 {3,S} {5,S}
3  C u0 p0 c0 {1,S} {2,S} {6,S} {7,S}
4  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
5  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.55288,0.0423009,-0.00010446,2.28105e-07,-1.68738e-10,-45535.6,9.73037], Tmin=(10,'K'), Tmax=(500.486,'K')),
            NASAPolynomial(coeffs=[-0.291258,0.0442729,-2.41998e-05,6.4133e-09,-6.64286e-13,-44790.7,29.2127], Tmin=(500.486,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-378.61,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
CBS-QB3

Bond corrections: {'C-O': 4, 'C-H': 8}
1D rotors:
pivots: [1, 2], dihedral: [6, 1, 2, 3], rotor symmetry: 3, max scan energy: 6.55 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: 
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: 
pivots: [4, 5], dihedral: [3, 4, 5, 11], rotor symmetry: 3, max scan energy: 6.55 kJ/mol


External symmetry: 2, optical isomers: 2

Geometry:
C      -1.78258900    0.62575900    0.25024700
O      -0.87896100   -0.28224000    0.86973100
C      -0.09286400   -0.99842300   -0.04677100
O      -0.81618900   -1.92809700   -0.81054500
C      -1.29576700   -3.03173600   -0.05110300
H      -2.47559900    0.10830400   -0.42044500
H      -1.23992900    1.39100600   -0.32177600
H      -2.34277900    1.10949500    1.05003500
H       0.67355800   -1.49729600    0.55883700
H       0.37262500   -0.32530900   -0.77702900
H      -1.95842800   -2.70602600    0.75676000
H      -0.46248900   -3.60237100    0.38169800
H      -1.84734600   -3.67272000   -0.73839900
""",
)

entry(
    index = 6,
    label = "COCOOC",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {6,S} {12,S} {13,S} {14,S}
4  O u0 p2 c0 {1,S} {2,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {3,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.16433,0.087485,-0.000333735,7.42742e-07,-5.86648e-10,-38575.2,8.79099], Tmin=(10,'K'), Tmax=(418.118,'K')),
            NASAPolynomial(coeffs=[3.21751,0.0442776,-2.55473e-05,7.11381e-09,-7.69313e-13,-38206.4,13.044], Tmin=(418.118,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-320.754,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (311.793,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
CBS-QB3

Bond corrections: {'C-O': 4, 'C-H': 8, 'O-O': 1}
1D rotors:
pivots: [1, 2], dihedral: [7, 1, 2, 3], rotor symmetry: 3, max scan energy: 6.61 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 4, max scan energy: 23.22 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 5, max scan energy: 40.20 kJ/mol
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 41.29 kJ/mol
pivots: [5, 6], dihedral: [4, 5, 6, 12], rotor symmetry: 3, max scan energy: 11.92 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -2.36600700    0.10922300   -0.08365300
O      -1.45654800    1.18271300   -0.30009600
C      -1.97920800    2.43813200    0.01484300
O      -2.14654600    2.67280600    1.39654800
O      -0.83286100    2.98845300    1.94617300
C      -0.47042800    1.92977800    2.81909400
H      -3.27213700    0.23318500   -0.69182100
H      -2.65321200    0.02922000    0.96983900
H      -1.85501500   -0.80324800   -0.38904000
H      -1.29520800    3.17655400   -0.40420600
H      -2.99739800    2.56532000   -0.38015600
H      -0.31553700    0.99533000    2.27268300
H      -1.21756200    1.79415200    3.60718900
H       0.47142700    2.25909100    3.26505400
""",
)

entry(
    index = 7,
    label = "COCOCOC",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {5,S}
2  O u0 p2 c0 {4,S} {6,S}
3  O u0 p2 c0 {5,S} {7,S}
4  C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
5  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
6  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
7  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.25878,0.0766112,-0.000256483,6.05734e-07,-4.89917e-10,-66573.2,11.7906], Tmin=(10,'K'), Tmax=(436.529,'K')),
            NASAPolynomial(coeffs=[-0.40443,0.0611175,-3.46628e-05,9.51292e-09,-1.0162e-12,-65786,31.7811], Tmin=(436.529,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-553.537,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (399.095,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
CBS-QB3

Bond corrections: {'C-O': 6, 'C-H': 10}
1D rotors:
pivots: [1, 2], dihedral: [8, 1, 2, 3], rotor symmetry: 3, max scan energy: 6.70 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: 
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: 
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: 
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 7], invalidation reason: 
pivots: [6, 7], dihedral: [5, 6, 7, 15], rotor symmetry: 3, max scan energy: 6.70 kJ/mol


External symmetry: 2, optical isomers: 2

Geometry:
C      -2.88825600    0.32918900   -0.33923800
O      -2.06198100   -0.19318100    0.69523300
C      -0.89540900   -0.80767800    0.22645400
O      -1.14805100   -2.01383800   -0.47519300
C      -1.49366200   -3.09628700    0.37322600
O      -0.39690300   -3.61788700    1.06842700
C       0.54140000   -4.28932800    0.23507000
H      -3.22330500   -0.45782100   -1.02174900
H      -3.75217500    0.78248400    0.14592300
H      -2.35544500    1.09770000   -0.91580900
H      -0.27984700   -0.99810400    1.10814000
H      -0.36542500   -0.16691500   -0.48774100
H      -1.94111900   -3.84686700   -0.28855100
H      -2.20775400   -2.77475300    1.13430200
H       0.96258600   -3.61693700   -0.51855900
H       0.07358000   -5.14432000   -0.27194500
H       1.33724400   -4.65203900    0.88490500
""",
)

entry(
    index = 8,
    label = "OOCOCCtN",
    molecule =
"""
1  O u0 p2 c0 {5,S} {6,S}
2  O u0 p2 c0 {3,S} {5,S}
3  O u0 p2 c0 {2,S} {12,S}
4  N u0 p1 c0 {7,T}
5  C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
6  C u0 p0 c0 {1,S} {7,S} {10,S} {11,S}
7  C u0 p0 c0 {4,T} {6,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73332,0.0248128,0.00020995,-9.08554e-07,1.12499e-09,-21628.9,11.885], Tmin=(10,'K'), Tmax=(284.356,'K')),
            NASAPolynomial(coeffs=[4.74522,0.0400254,-2.56319e-05,7.93867e-09,-9.4553e-13,-21805.5,6.18234], Tmin=(284.356,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-179.796,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (278.535,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
CBS-QB3

Bond corrections: {'H-O': 1, 'C-O': 3, 'C#N': 1, 'C-H': 4, 'O-O': 1, 'C-C': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [8, 1, 2, 3], invalidation reason: Inconsistent by 10.4 kJ/mol between initial and final position
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Inconsistent by 28.8 kJ/mol between initial and final position
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Inconsistent by more than 15 kJ/mol between consecutive points
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 22.46 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.90039900    0.10544300    0.98167600
O       1.39694400   -0.64536700   -0.15482500
C       2.46031100   -1.35044000   -0.72606300
O       3.39388600   -0.54888200   -1.42292500
C       2.82789000    0.30555900   -2.39729600
C       2.32696600    1.55133400   -1.78922200
N       1.96604400    2.50558100   -1.25268300
H       1.82057000    1.01336700    0.64418200
H       1.94947100   -2.04383100   -1.40772100
H       3.04389400   -1.87946500    0.02718700
H       3.62273800    0.55576100   -3.10205800
H       2.01054200   -0.17579400   -2.94912100
""",
)

entry(
    index = 9,
    label = "OCCtN",
    molecule =
"""
1 O u0 p2 c0 {3,S} {7,S}
2 N u0 p1 c0 {4,T}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C u0 p0 c0 {2,T} {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93803,0.00457318,8.23755e-05,-2.22981e-07,1.8667e-10,-8455.37,9.4495], Tmin=(10,'K'), Tmax=(393.898,'K')),
            NASAPolynomial(coeffs=[3.62871,0.018359,-1.06581e-05,3.08323e-09,-3.51677e-13,-8513.58,9.60538], Tmin=(393.898,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-70.2982,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (153.818,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
CBS-QB3

Bond corrections: {'H-O': 1, 'C-O': 1, 'C-H': 2, 'C-C': 1, 'C#N': 1}
1D rotors:
pivots: [1, 2], dihedral: [5, 1, 2, 3], rotor symmetry: 1, max scan energy: 9.81 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.02462400    0.81189000   -0.43095500
C      -0.33431800   -0.34311900    0.00137900
C       1.12996700   -0.18250400   -0.03115200
N       2.27113200   -0.02229000   -0.03791000
H      -0.80877000    1.53693400    0.16518100
H      -0.62115700   -0.65278200    1.01472100
H      -0.61223000   -1.14812900   -0.68126500
""",
)

entry(
    index = 10,
    label = "COCOCCtN",
    molecule =
"""
1  O u0 p2 c0 {4,S} {5,S}
2  O u0 p2 c0 {4,S} {6,S}
3  N u0 p1 c0 {7,T}
4  C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
5  C u0 p0 c0 {1,S} {7,S} {10,S} {11,S}
6  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
7  C u0 p0 c0 {3,T} {5,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.26668,0.0652089,-0.000149087,2.48542e-07,-1.5545e-10,-28318.2,12.3454], Tmin=(10,'K'), Tmax=(530.925,'K')),
            NASAPolynomial(coeffs=[2.50867,0.0463439,-2.63552e-05,7.24607e-09,-7.76057e-13,-27891.4,18.7845], Tmin=(530.925,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-235.484,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (324.264,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
CBS-QB3

Bond corrections: {'C-O': 4, 'C#N': 1, 'C-H': 7, 'C-C': 1}
1D rotors:
pivots: [1, 2], dihedral: [8, 1, 2, 3], rotor symmetry: 3, max scan energy: 6.17 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Inconsistent by 13.6 kJ/mol between initial and final position
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Inconsistent by 10.9 kJ/mol between initial and final position
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 20.07 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -2.24775100   -0.15198300    0.61013900
O      -1.05200600    0.61966300    0.70928700
C      -0.12356200    0.10849000    1.61604400
O       0.49535400   -1.08898400    1.16261800
C       1.33262000   -0.90605800    0.03406800
C       2.61067400   -0.26030700    0.38380300
N       3.60258600    0.25217800    0.66888600
H      -2.76879300   -0.18696700    1.57534100
H      -2.88225400    0.34636600   -0.12144800
H      -2.03996300   -1.17398300    0.27900800
H       0.61998500    0.89651400    1.76760000
H      -0.58940300   -0.17070200    2.56666900
H       1.53851300   -1.89763100   -0.37150900
H       0.83550100   -0.30921000   -0.73808500
""",
)

entry(
    index = 11,
    label = "COOCOCCtN",
    molecule =
"""
1  O u0 p2 c0 {5,S} {6,S}
2  O u0 p2 c0 {3,S} {5,S}
3  O u0 p2 c0 {2,S} {7,S}
4  N u0 p1 c0 {8,T}
5  C u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
6  C u0 p0 c0 {1,S} {8,S} {11,S} {12,S}
7  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
8  C u0 p0 c0 {4,T} {6,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.16627,0.0865864,-0.000265751,5.82606e-07,-4.79674e-10,-21143.1,13.8402], Tmin=(10,'K'), Tmax=(391.806,'K')),
            NASAPolynomial(coeffs=[3.7713,0.0531731,-3.35575e-05,1.00995e-08,-1.16526e-12,-20981.5,14.1561], Tmin=(391.806,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-175.814,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (345.051,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
CBS-QB3

Bond corrections: {'C-O': 4, 'C#N': 1, 'C-H': 7, 'O-O': 1, 'C-C': 1}
1D rotors:
pivots: [1, 2], dihedral: [9, 1, 2, 3], rotor symmetry: 3, max scan energy: 11.55 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Inconsistent by more than 17.7 kJ/mol between consecutive points
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 35.85 kJ/mol
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 19.82 kJ/mol
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 7], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
C      -2.28106600    0.06677800   -0.33317000
O      -1.64345800   -1.12950200   -0.75227000
O      -2.52094500   -1.72187900   -1.76724800
C      -1.71081800   -2.13309000   -2.83873300
O      -1.13211500   -3.40482900   -2.67233300
C      -0.06420300   -3.48487100   -1.73936600
C       1.12808000   -2.73558200   -2.17327100
N       2.05140800   -2.14106700   -2.52243100
H      -3.27263200   -0.14164300    0.07847000
H      -2.35578300    0.78719100   -1.15341200
H      -1.63104100    0.46044600    0.45112100
H      -2.40227300   -2.23997100   -3.67511300
H      -0.95051900   -1.36998700   -3.03862800
H       0.19425600   -4.54216000   -1.66687800
H      -0.36464700   -3.12569700   -0.75138900
""",
)

entry(
    index = 12,
    label = "C3H6NO3_0",
    molecule =
"""
multiplicity 2
1  O u0 p2 c0 {5,S} {6,S}
2  O u0 p2 c0 {3,S} {6,S}
3  O u0 p2 c0 {2,S} {13,S}
4  N u1 p1 c0 {7,D}
5  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
6  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
7  C u0 p0 c0 {4,D} {5,S} {12,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63226,0.0344711,1.37784e-05,-4.50031e-08,2.16909e-11,-8508.59,12.5572], Tmin=(10,'K'), Tmax=(800.845,'K')),
            NASAPolynomial(coeffs=[4.6896,0.0420305,-2.4431e-05,6.82531e-09,-7.38314e-13,-9089.71,5.12011], Tmin=(800.845,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-70.7688,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
CBS-QB3

Bond corrections: {'C-O': 3, 'C-H': 5, 'C=N': 1, 'H-O': 1, 'O-O': 1, 'C-C': 1}

External symmetry: 1, optical isomers: 2

Geometry:
O      -0.13343300   -0.77774100    0.78331300
O       1.56391600   -0.17237300   -0.74856400
O       2.21208300    0.78886900    0.12273300
N      -0.39756000    1.98458000    0.13703400
C      -1.22968700   -0.33869900    0.02352500
C       1.00469900   -1.17546000    0.04845500
C      -1.26333600    1.17251300   -0.22394900
H      -2.13723500   -0.59146600    0.58099400
H      -1.28405800   -0.83840000   -0.95462500
H       0.75112400   -1.95858700   -0.67919600
H       1.71669100   -1.52937400    0.79393700
H      -2.15966600    1.53443400   -0.75473900
H       1.50117300    1.45358800    0.21774300
""",
)

entry(
    index = 13,
    label = "C3H7NO3_0",
    molecule =
"""
1  O u0 p2 c0 {5,S} {6,S}
2  O u0 p2 c0 {3,S} {6,S}
3  O u0 p2 c0 {2,S} {14,S}
4  N u0 p1 c0 {7,D} {13,S}
5  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
6  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
7  C u0 p0 c0 {4,D} {5,S} {12,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7639,0.0293353,3.54571e-05,-6.47282e-08,2.66575e-11,-29221.4,11.5573], Tmin=(10,'K'), Tmax=(891.124,'K')),
            NASAPolynomial(coeffs=[4.77276,0.0453365,-2.60345e-05,7.12763e-09,-7.54131e-13,-30216.4,2.23281], Tmin=(891.124,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-242.931,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (328.422,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
CBS-QB3

Bond corrections: {'C-O': 3, 'C-H': 5, 'C=N': 1, 'H-O': 1, 'O-O': 1, 'H-N': 1, 'C-C': 1}
1D rotors:
* Invalidated! pivots: [1, 5], dihedral: [6, 1, 5, 7], invalidation reason: 
* Invalidated! pivots: [1, 6], dihedral: [5, 1, 6, 2], invalidation reason: 
* Invalidated! pivots: [2, 3], dihedral: [6, 2, 3, 14], invalidation reason: 
* Invalidated! pivots: [2, 6], dihedral: [3, 2, 6, 1], invalidation reason: 
pivots: [5, 7], dihedral: [1, 5, 7, 4], rotor symmetry: 1, max scan energy: 32.03 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       2.80295300   -0.91927400   -0.06523800
O       1.09467800    0.28342700    1.03108000
O       1.22559900    1.44595100    0.17391500
N       3.91464700    1.45309100    0.97401200
C       3.70740300   -0.98594800    1.01101100
C       1.43639900   -0.84172300    0.27821900
C       4.29416000    0.33710700    1.43739000
H       3.25914000   -1.46335300    1.89690100
H       4.54064000   -1.62640600    0.69598200
H       1.14079700   -1.68004300    0.92500500
H       0.90371600   -0.85639800   -0.67342800
H       5.10043900    0.24150300    2.17803500
H       4.43538300    2.22949200    1.38066000
H       2.18972300    1.62146400    0.28768100
""",
)

entry(
    index = 14,
    label = "C3H5NO2_0",
    molecule =
"""
1  O u0 p2 c0 {4,S} {5,S}
2  O u0 p2 c0 {4,S} {11,S}
3  N u0 p1 c0 {6,T}
4  C u0 p0 c0 {1,S} {2,S} {7,S} {8,S}
5  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
6  C u0 p0 c0 {3,T} {5,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75836,0.0175427,0.000162749,-4.77741e-07,3.9539e-10,-29934.3,11.5583], Tmin=(10,'K'), Tmax=(430.373,'K')),
            NASAPolynomial(coeffs=[5.85719,0.0345054,-2.34822e-05,7.63935e-09,-9.41102e-13,-30452.7,-0.721742], Tmin=(430.373,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-248.899,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (245.277,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
CBS-QB3

Bond corrections: {'C-O': 3, 'C-H': 4, 'H-O': 1, 'C#N': 1, 'C-C': 1}
1D rotors:
pivots: [1, 4], dihedral: [5, 1, 4, 2], rotor symmetry: 1, max scan energy: 30.31 kJ/mol
pivots: [1, 5], dihedral: [4, 1, 5, 6], rotor symmetry: 1, max scan energy: 21.17 kJ/mol
pivots: [2, 4], dihedral: [11, 2, 4, 1], rotor symmetry: 1, max scan energy: 25.83 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       0.08640400    0.35081300   -1.04285700
O       1.85802600    0.13786700    0.48439700
N      -2.69670200   -0.76938100    0.59676900
C       1.00592300   -0.52538500   -0.40902500
C      -0.84989400    0.93896200   -0.15551900
C      -1.89273000   -0.01218700    0.26804300
H       1.54404800   -0.99331800   -1.23702500
H       0.48272900   -1.28378300    0.18048800
H      -0.35313200    1.33989600    0.73410300
H      -1.32063600    1.76293400   -0.69333100
H       2.43008000    0.72227500   -0.02580000
""",
)

entry(
    index = 15,
    label = "C2H5NO_0",
    molecule =
"""
1 O u0 p2 c0 {3,S} {8,S}
2 N u0 p1 c0 {4,D} {9,S}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C u0 p0 c0 {2,D} {3,S} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96492,0.00207641,8.07381e-05,-1.40089e-07,7.85788e-11,-15771.1,8.42744], Tmin=(10,'K'), Tmax=(460.297,'K')),
            NASAPolynomial(coeffs=[0.409745,0.0329731,-1.99539e-05,5.75743e-09,-6.39704e-13,-15443.8,22.8205], Tmin=(460.297,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-131.144,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (203.705,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
CBS-QB3

Bond corrections: {'C-O': 1, 'C-H': 3, 'C=N': 1, 'H-O': 1, 'H-N': 1, 'C-C': 1}
1D rotors:
pivots: [1, 3], dihedral: [8, 1, 3, 4], rotor symmetry: 1, max scan energy: 33.18 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [1, 3, 4, 2], invalidation reason: 


External symmetry: 1, optical isomers: 1

Geometry:
O      -1.37739600   -0.82005800    0.13772400
N      -0.02456300   -0.41824200   -2.11023900
C      -0.98950600    0.50096200   -0.12967200
C      -0.23015500    0.62610200   -1.42286700
H      -0.35433700    0.89377500    0.68014700
H      -1.86795200    1.16359900   -0.18252300
H       0.10738500    1.63227100   -1.70039800
H      -1.04355600   -1.34080900   -0.61090200
H       0.49637000   -0.23062300   -2.96556900
""",
)

entry(
    index = 16,
    label = "C3H8O3_0",
    molecule =
"""
1  O u0 p2 c0 {4,S} {6,S}
2  O u0 p2 c0 {4,S} {13,S}
3  O u0 p2 c0 {5,S} {14,S}
4  C u0 p0 c0 {1,S} {2,S} {5,S} {7,S}
5  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
6  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78157,0.0277119,3.75481e-05,-6.5224e-08,2.61666e-11,-72625.2,10.8514], Tmin=(10,'K'), Tmax=(913.89,'K')),
            NASAPolynomial(coeffs=[4.90989,0.0445528,-2.5841e-05,7.09441e-09,-7.50111e-13,-73740.9,0.533445], Tmin=(913.89,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-603.805,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (320.107,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
CBS-QB3

Bond corrections: {'C-O': 4, 'C-H': 6, 'H-O': 2, 'C-C': 1}
1D rotors:
pivots: [1, 4], dihedral: [6, 1, 4, 2], rotor symmetry: 1, max scan energy: 47.04 kJ/mol
pivots: [1, 6], dihedral: [4, 1, 6, 10], rotor symmetry: 3, max scan energy: 6.88 kJ/mol
pivots: [2, 4], dihedral: [13, 2, 4, 1], rotor symmetry: 1, max scan energy: 33.25 kJ/mol
* Invalidated! pivots: [3, 5], dihedral: [14, 3, 5, 4], invalidation reason: 
* Invalidated! pivots: [4, 5], dihedral: [1, 4, 5, 3], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.68072100   -0.17109400    2.99708900
O       0.65138600   -0.00610700    1.07609600
O      -2.04784400   -0.52496600    0.59982100
C      -0.33893900    0.60516900    1.86081300
C      -1.63795600    0.75467300    1.07689700
C       0.39940900   -0.39097400    3.89701200
H       0.07203500    1.57344800    2.17383800
H      -1.46939800    1.37775300    0.19785700
H      -2.40535900    1.21801400    1.70724600
H       0.75211500    0.55761800    4.32385300
H       1.23426500   -0.89008700    3.39814300
H       0.01829600   -1.02219300    4.69941900
H       0.19672200   -0.69994200    0.57650400
H      -2.19069600   -1.06660100    1.38579500
""",
)

entry(
    index = 17,
    label = "C2H6O3_0",
    molecule =
"""
1  O u0 p2 c0 {4,S} {10,S}
2  O u0 p2 c0 {4,S} {9,S}
3  O u0 p2 c0 {5,S} {11,S}
4  C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
5  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {5,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92854,0.00428844,0.0001256,-2.3727e-07,1.39138e-10,-74379.1,10.3838], Tmin=(10,'K'), Tmax=(531.752,'K')),
            NASAPolynomial(coeffs=[0.477765,0.044846,-2.99919e-05,9.43134e-09,-1.12184e-12,-74218.5,22.9115], Tmin=(531.752,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-618.45,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (253.591,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
CBS-QB3

Bond corrections: {'C-O': 3, 'C-H': 3, 'H-O': 3, 'C-C': 1}
1D rotors:
pivots: [1, 4], dihedral: [10, 1, 4, 2], rotor symmetry: 1, max scan energy: 32.03 kJ/mol
* Invalidated! pivots: [2, 4], dihedral: [9, 2, 4, 1], invalidation reason: 
* Invalidated! pivots: [3, 5], dihedral: [11, 3, 5, 4], invalidation reason: 
* Invalidated! pivots: [4, 5], dihedral: [1, 4, 5, 3], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.17547900    0.80976900    2.54764800
O      -2.73397300   -0.13229500    0.48750800
O      -0.38666900   -1.11135400    1.60859100
C      -1.85330200    0.74367500    1.18510700
C      -0.46024500    0.16265200    0.97396200
H      -1.93547400    1.76597700    0.79989200
H      -0.23767200    0.09745800   -0.09735600
H       0.28292500    0.79849700    1.45634800
H      -3.62566400    0.06843700    0.79190900
H      -1.82288000   -0.00280300    2.93975000
H      -1.05824700   -1.65681400    1.18024700
""",
)

entry(
    index = 18,
    label = "C4H10O3_0",
    molecule =
"""
1  O u0 p2 c0 {4,S} {6,S}
2  O u0 p2 c0 {4,S} {7,S}
3  O u0 p2 c0 {5,S} {17,S}
4  C u0 p0 c0 {1,S} {2,S} {5,S} {8,S}
5  C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
6  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
7  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.41606,0.0548953,-2.75455e-05,3.31357e-09,1.00172e-12,-69178.6,12.1176], Tmin=(10,'K'), Tmax=(1226.08,'K')),
            NASAPolynomial(coeffs=[10.6165,0.0399523,-1.97218e-05,4.74579e-09,-4.49747e-13,-71586.8,-26.7083], Tmin=(1226.08,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-575.225,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (390.78,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
CBS-QB3

Bond corrections: {'C-O': 5, 'C-H': 9, 'H-O': 1, 'C-C': 1}
1D rotors:
* Invalidated! pivots: [1, 4], dihedral: [6, 1, 4, 2], invalidation reason: 
pivots: [1, 6], dihedral: [4, 1, 6, 11], rotor symmetry: 3, max scan energy: 5.76 kJ/mol
pivots: [2, 4], dihedral: [7, 2, 4, 1], rotor symmetry: 1, max scan energy: 26.50 kJ/mol
pivots: [2, 7], dihedral: [4, 2, 7, 14], rotor symmetry: 3, max scan energy: 6.23 kJ/mol
pivots: [3, 5], dihedral: [17, 3, 5, 4], rotor symmetry: 1, max scan energy: 21.96 kJ/mol
* Invalidated! pivots: [4, 5], dihedral: [1, 4, 5, 3], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
O       0.22595300    1.02562700   -1.11335800
O      -1.06648800   -0.60626900   -0.02613600
O       0.98992800   -1.24543700   -2.32950600
C       0.22756900   -0.11630500   -0.27739000
C       1.20003700   -1.10125100   -0.93504200
C      -0.41003900    2.16644500   -0.54723400
C      -1.80956000   -1.07765000   -1.15407400
H       0.59939600    0.14721400    0.72172300
H       2.22138600   -0.75365100   -0.72360900
H       1.07412800   -2.08601900   -0.48039100
H       0.12880500    2.51036800    0.34509300
H      -0.38528500    2.95018000   -1.30392700
H      -1.44657400    1.94883700   -0.27542300
H      -1.35302000   -1.96378300   -1.60110100
H      -1.89892900   -0.30463900   -1.92330800
H      -2.80048900   -1.32462900   -0.77306200
H       0.90742400   -0.34909100   -2.67735000
""",
)

entry(
    index = 19,
    label = "iC3H5CN",
    molecule =
"""
1  N u0 p1 c0 {5,T}
2  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  C u0 p0 c0 {3,D} {9,S} {10,S}
5  C u0 p0 c0 {1,T} {3,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94101,0.00527146,0.000158165,-5.22611e-07,5.91992e-10,15957.4,9.25408], Tmin=(10,'K'), Tmax=(222.636,'K')),
            NASAPolynomial(coeffs=[2.48514,0.0314282,-1.80636e-05,5.08687e-09,-5.60944e-13,16022.2,14.0908], Tmin=(222.636,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (132.689,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (228.648,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
CBS-QB3

Bond corrections: {'C-C': 2, 'C#N': 1, 'C-H': 5, 'C=C': 1}
1D rotors:
pivots: [1, 2], dihedral: [6, 1, 2, 3], rotor symmetry: 3, max scan energy: 7.34 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C      -0.79359100   -0.96590100   -0.09628200
C       0.21539900    0.15121800    0.01172000
C      -0.09891400    1.43850700    0.19051500
C       1.59554700   -0.23337100   -0.08902000
N       2.69500400   -0.57769800   -0.17420300
H      -0.69871400   -1.48271200   -1.05536000
H      -0.63450900   -1.70941400    0.68972500
H      -1.80762800   -0.57423700   -0.00809300
H       0.66180400    2.20529200    0.26213900
H      -1.13439900    1.74831600    0.26885900
""",
)

entry(
    index = 20,
    label = "CH3OCH2OCH2j",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u1 p0 c0 {5,S} {11,S} {12,S}
4  O u0 p2 c0 {1,S} {2,S}
5  O u0 p2 c0 {1,S} {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85629,0.0168586,0.000320925,-1.89714e-06,3.55103e-09,-22502,10.5836], Tmin=(10,'K'), Tmax=(176.045,'K')),
            NASAPolynomial(coeffs=[3.69964,0.038907,-2.44788e-05,7.45997e-09,-8.76611e-13,-22525.1,10.2535], Tmin=(176.045,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-186.656,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (266.063,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
CBS-QB3

Bond corrections: {'C-O': 4, 'C-H': 7}
1D rotors:
pivots: [1, 4], dihedral: [2, 1, 4, 5], rotor symmetry: 1, max scan energy: 25.21 kJ/mol
pivots: [4, 5], dihedral: [1, 4, 5, 6], rotor symmetry: 1, max scan energy: 40.19 kJ/mol
pivots: [5, 6], dihedral: [4, 5, 6, 7], rotor symmetry: 1, max scan energy: 47.23 kJ/mol
pivots: [6, 7], dihedral: [5, 6, 7, 10], rotor symmetry: 3, max scan energy: 6.33 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       1.95278900    0.33986700    0.10545600
H       2.93458300    0.30458100    0.56317100
H       1.80427400    0.70960900   -0.89888300
O       1.03534500   -0.59923300    0.47618400
C       1.22381100   -1.14682700    1.77717300
O       2.37851700   -1.91702500    1.89095500
C       2.33099400   -3.13861000    1.15804900
H       1.32237100   -0.34057700    2.50874200
H       0.31953300   -1.73764900    1.95937100
H       2.22451100   -2.95793600    0.08430900
H       1.49852900   -3.76746800    1.50040700
H       3.27149400   -3.65390500    1.34858500
""",
)

entry(
    index = 21,
    label = "CH3OCHjOCH3",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
3  C u1 p0 c0 {4,S} {5,S} {12,S}
4  O u0 p2 c0 {1,S} {3,S}
5  O u0 p2 c0 {2,S} {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.37927,0.0474269,-7.13908e-05,7.77306e-08,-3.42788e-11,-22485.1,11.5549], Tmin=(10,'K'), Tmax=(710.759,'K')),
            NASAPolynomial(coeffs=[3.69004,0.0339878,-1.83576e-05,4.84681e-09,-5.03486e-13,-22234,12.2389], Tmin=(710.759,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-187.038,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (266.063,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
CBS-QB3

Bond corrections: {'C-O': 4, 'C-H': 7}
1D rotors:
pivots: [1, 2], dihedral: [7, 1, 2, 3], rotor symmetry: 3, max scan energy: 5.26 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 5], rotor symmetry: 1, max scan energy: 13.92 kJ/mol
pivots: [3, 5], dihedral: [2, 3, 5, 6], rotor symmetry: 1, max scan energy: 39.69 kJ/mol
pivots: [5, 6], dihedral: [3, 5, 6, 10], rotor symmetry: 3, max scan energy: 6.55 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -1.97603700   -0.16053700   -0.51205100
O      -0.54810500   -0.09821200   -0.45853000
C       0.01805600   -0.46982200    0.71439900
H       1.10379900   -0.34582000    0.68969700
O      -0.43942100   -1.67203900    1.19893000
C       0.13283700   -2.04290700    2.44554000
H      -2.41719200    0.43088800    0.29749600
H      -2.25965400    0.26289700   -1.47448300
H      -2.32859500   -1.19145500   -0.44141500
H      -0.11140300   -1.31279100    3.22454600
H      -0.28551300   -3.01354600    2.70787100
H       1.22426800   -2.13105800    2.36833800
""",
)

entry(
    index = 22,
    label = "OHCH2OCHO",
    molecule =
"""
1 O u0 p2 c0 {4,S} {5,S}
2 O u0 p2 c0 {4,S} {9,S}
3 O u0 p2 c0 {5,D}
4 C u0 p0 c0 {1,S} {2,S} {6,S} {7,S}
5 C u0 p0 c0 {1,S} {3,D} {8,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9184,0.00494055,0.000111554,-2.23143e-07,1.35665e-10,-67593.6,10.2609], Tmin=(10,'K'), Tmax=(534.61,'K')),
            NASAPolynomial(coeffs=[2.1192,0.035906,-2.44393e-05,7.68505e-09,-9.16266e-13,-67651.3,15.475], Tmin=(534.61,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-562.034,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (195.39,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
CBS-QB3

Bond corrections: {'C-H': 3, 'H-O': 1, 'C=O': 1, 'C-O': 3}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 66.83 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 40.44 kJ/mol
pivots: [4, 5], dihedral: [3, 4, 5, 9], rotor symmetry: 1, max scan energy: 34.26 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.84540500    0.77741000    0.63529000
C       1.58720000   -0.19362800   -0.03109600
O       0.36272300   -0.58049000   -0.39721500
C      -0.71597600    0.31176700    0.03403300
O      -0.84089100    0.37666000    1.40520400
H       2.33434300   -0.89529500   -0.42641300
H      -0.52201900    1.28557100   -0.42578300
H      -1.61159700   -0.14836600   -0.37350700
H      -0.08969200    0.88966300    1.73128800
""",
)

entry(
    index = 23,
    label = "CH3OCH2OCHO",
    molecule =
"""
1  O u0 p2 c0 {4,S} {5,S}
2  O u0 p2 c0 {4,S} {6,S}
3  O u0 p2 c0 {6,D}
4  C u0 p0 c0 {1,S} {2,S} {7,S} {8,S}
5  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
6  C u0 p0 c0 {2,S} {3,D} {12,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.33938,0.0754359,-0.000384785,1.05227e-06,-9.63698e-10,-64698.4,11.183], Tmin=(10,'K'), Tmax=(379.209,'K')),
            NASAPolynomial(coeffs=[0.559139,0.0449282,-2.74281e-05,7.92507e-09,-8.78563e-13,-64057.3,27.5726], Tmin=(379.209,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-537.972,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (270.22,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
CBS-QB3

Bond corrections: {'C-O': 4, 'C-H': 6, 'C=O': 1}
1D rotors:
pivots: [1, 2], dihedral: [7, 1, 2, 3], rotor symmetry: 3, max scan energy: 6.88 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for s241 exists which is 2.05 kJ/mol lower.
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 27.82 kJ/mol
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 50.94 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       1.85523000   -0.00112600   -0.30407700
O       1.07367700    0.71671100    0.64791700
C       0.18433000   -0.06424400    1.35765700
O      -0.89200800   -0.55474000    0.51276500
C      -2.02962400    0.17320900    0.48050700
O      -2.26914000    1.15221300    1.12573700
H       1.22988800   -0.42516200   -1.09519600
H       2.41991900   -0.80802900    0.18121400
H       2.55199900    0.71508000   -0.73684800
H      -0.23692900    0.55459700    2.14577600
H       0.64841100   -0.97645300    1.74665400
H      -2.72026200   -0.29492900   -0.23590400
""",
)

entry(
    index = 24,
    label = "CH3NCH2",
    molecule =
"""
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,D} {7,S} {8,S}
3 N u0 p1 c0 {1,S} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.12431,0.0161642,4.57771e-06,-1.2116e-08,4.53506e-12,7335.42,14.5092], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.74096,0.0220935,-1.09102e-05,2.60524e-09,-2.44225e-13,7192.29,15.2596], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
from NOx2018
CN=C
""",
)

entry(
    index = 25,
    label = "cyanoisopropyl_polymer",
    molecule =
"""
1  O u0 p2 c0 {3,S} {8,S}
2  O u0 p2 c0 {4,S} {7,S}
3  O u0 p2 c0 {1,S} {13,S}
4  O u0 p2 c0 {2,S} {28,S}
5  N u0 p1 c0 {13,D} {27,S}
6  N u0 p1 c0 {14,T}
7  C u0 p0 c0 {2,S} {9,S} {10,S} {13,S}
8  C u0 p0 c0 {1,S} {11,S} {12,S} {14,S}
9  C u0 p0 c0 {7,S} {21,S} {22,S} {23,S}
10 C u0 p0 c0 {7,S} {24,S} {25,S} {26,S}
11 C u0 p0 c0 {8,S} {15,S} {16,S} {17,S}
12 C u0 p0 c0 {8,S} {18,S} {19,S} {20,S}
13 C u0 p0 c0 {3,S} {5,D} {7,S}
14 C u0 p0 c0 {6,T} {8,S}
15 H u0 p0 c0 {11,S}
16 H u0 p0 c0 {11,S}
17 H u0 p0 c0 {11,S}
18 H u0 p0 c0 {12,S}
19 H u0 p0 c0 {12,S}
20 H u0 p0 c0 {12,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {10,S}
25 H u0 p0 c0 {10,S}
26 H u0 p0 c0 {10,S}
27 H u0 p0 c0 {5,S}
28 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.64346,0.125262,-0.00010256,4.75026e-08,-9.79338e-12,-21092.5,17.6434], Tmin=(10,'K'), Tmax=(980.332,'K')),
            NASAPolynomial(coeffs=[10.0646,0.0949817,-5.62282e-05,1.59953e-08,-1.75852e-12,-22547.6,-18.0119], Tmin=(980.332,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-175.516,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (681.787,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
b3lyp/6-311+g(3df,2p), no rotors

Bond corrections: {'C-H': 12, 'C-O': 3, 'C#N': 1, 'H-O': 1, 'C=N': 1, 'H-N': 1, 'C-C': 6, 'O-O': 2}

External symmetry: 1, optical isomers: 1

Geometry:
N      -3.07028300   -1.70085700    1.52767300
C      -1.95716000   -1.47811800    1.70485200
C      -0.51833000   -1.23897300    1.95115100
C       0.32922000   -2.21872400    1.13851300
C      -0.22921300   -1.32712700    3.45404600
O      -0.20114100    0.13136900    1.64713500
O      -0.52658200    0.37447300    0.25637700
C       0.47060500    1.07720200   -0.36810300
N       1.55987500    1.46491400    0.12700400
C       0.05607600    1.34373100   -1.82591100
C      -1.21704300    2.19561300   -1.86264100
C      -0.11105200    0.03395100   -2.60129900
O       1.02664800    2.19228300   -2.43151000
O       2.30589300    1.53169300   -2.51846700
H       0.13971700   -2.11074300    0.07388700
H       0.09111400   -3.24159200    1.42679700
H       1.38374000   -2.03247000    1.33685900
H      -0.47559100   -2.32465200    3.81263600
H      -0.82199900   -0.59926300    4.00331700
H       0.82841900   -1.13893100    3.63077400
H       1.65413700    1.21258400    1.10659900
H      -1.07186500    3.12631400   -1.31620700
H      -1.45297700    2.43292200   -2.89868000
H      -2.05172600    1.65356200   -1.42365300
H      -0.90030100   -0.57542300   -2.16359900
H       0.81787900   -0.53150400   -2.60953400
H      -0.37983500    0.26775200   -3.63052200
H       2.60703400    1.64693000   -1.59679900
""",
)

entry(
    index = 26,
    label = "cyanoisopropyl_polymer_rad",
    molecule =
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {8,S}
2  O u0 p2 c0 {4,S} {7,S}
3  O u0 p2 c0 {1,S} {13,S}
4  O u0 p2 c0 {2,S} {27,S}
5  N u1 p1 c0 {13,D}
6  N u0 p1 c0 {14,T}
7  C u0 p0 c0 {2,S} {9,S} {10,S} {13,S}
8  C u0 p0 c0 {1,S} {11,S} {12,S} {14,S}
9  C u0 p0 c0 {7,S} {21,S} {22,S} {23,S}
10 C u0 p0 c0 {7,S} {24,S} {25,S} {26,S}
11 C u0 p0 c0 {8,S} {15,S} {16,S} {17,S}
12 C u0 p0 c0 {8,S} {18,S} {19,S} {20,S}
13 C u0 p0 c0 {3,S} {5,D} {7,S}
14 C u0 p0 c0 {6,T} {8,S}
15 H u0 p0 c0 {11,S}
16 H u0 p0 c0 {11,S}
17 H u0 p0 c0 {11,S}
18 H u0 p0 c0 {12,S}
19 H u0 p0 c0 {12,S}
20 H u0 p0 c0 {12,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {10,S}
25 H u0 p0 c0 {10,S}
26 H u0 p0 c0 {10,S}
27 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.54803,0.129561,-0.000124392,7.33251e-08,-1.9804e-11,435.615,17.1024], Tmin=(10,'K'), Tmax=(788.646,'K')),
            NASAPolynomial(coeffs=[9.47534,0.0944261,-5.75657e-05,1.68346e-08,-1.89657e-12,-657.026,-14.6731], Tmin=(788.646,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (3.48117,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (656.843,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
b3lyp/6-311+g(3df,2p), no rotors

Bond corrections: {'C-H': 12, 'C-O': 3, 'C#N': 1, 'H-O': 1, 'C=N': 1, 'C-C': 6, 'O-O': 2}

External symmetry: 1, optical isomers: 1

Geometry:
N       0.98186500    1.38843500   -2.08385300
C       1.58427400    0.76677600   -1.32852400
C       2.30936000   -0.07654600   -0.35284600
C       2.65989400   -1.42499900   -0.98700600
C       3.53971500    0.65796500    0.18666600
O       1.48340100   -0.23771200    0.81130500
O       0.21826000   -0.79923900    0.37210000
C      -0.81693500   -0.01990900    0.82512300
N      -0.71274500    0.92656700    1.63014400
C      -2.15127500   -0.48312500    0.18600300
C      -3.31924000    0.33376000    0.72518800
C      -2.35261900   -1.98289100    0.42067100
O      -2.03141700   -0.38151500   -1.23502500
O      -2.01615100    1.00482000   -1.63418200
H       3.31131600   -1.27761800   -1.84764000
H       3.17774400   -2.03610300   -0.24932400
H       1.76304100   -1.94369000   -1.31562000
H       3.25558800    1.60617600    0.63693900
H       4.02399500    0.03542800    0.93691600
H       4.24095300    0.84343900   -0.62494900
H      -3.17448600    1.39386800    0.54406600
H      -4.23061200    0.01026600    0.22351300
H      -3.42801100    0.17342200    1.79668900
H      -2.36476500   -2.19236200    1.48942800
H      -3.30764200   -2.28283300   -0.00754700
H      -1.56063500   -2.56673900   -0.04235500
H      -1.09035500    1.12172300   -1.91258200
""",
)

entry(
    index = 27,
    label = "CH3NCH2OOj",
    molecule =
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {4,S}
2  O u1 p2 c0 {1,S}
3  N u0 p1 c0 {4,S} {5,S} {11,S}
4  C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
5  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77982,0.0251633,1.0407e-06,-1.19808e-08,4.48165e-12,-1237.13,11.0948], Tmin=(10,'K'), Tmax=(1153.5,'K')),
            NASAPolynomial(coeffs=[5.97643,0.0267741,-1.30541e-05,3.10073e-09,-2.90139e-13,-2357.82,-2.47743], Tmin=(1153.5,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-10.2842,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (253.591,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
CBS-QB3 with rotors

Bond corrections: {'O-O': 1, 'C-H': 5, 'C-O': 1, 'C-N': 2, 'H-N': 1}
1D rotors:
pivots: [1, 2], dihedral: [6, 1, 2, 3], rotor symmetry: 3, max scan energy: 8.54 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: 
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: 


External symmetry: 1, optical isomers: 1

Geometry:
C      -1.29587500   -0.43082500   -0.38325700
N      -0.33407300   -0.32467600    0.71439500
C       0.40124400   -1.47433700    1.02572100
O      -0.43028900   -2.65087500    1.50418800
O      -1.12285300   -2.31489800    2.57020600
H      -2.11142100   -1.13839100   -0.18858800
H      -1.72524300    0.55352000   -0.57688300
H      -0.77287400   -0.75006600   -1.28861300
H      -0.74882600    0.07473900    1.54771600
H       1.10512200   -1.28849900    1.83654100
H       0.89606700   -1.89839000    0.15100400
""",
)

entry(
    index = 28,
    label = "NH2CH2OOj",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 O u1 p2 c0 {1,S}
3 N u0 p1 c0 {4,S} {7,S} {8,S}
4 C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94753,0.0139079,1.31767e-05,-2.18939e-08,7.71369e-12,-1444.75,10.344], Tmin=(10,'K'), Tmax=(1090.04,'K')),
            NASAPolynomial(coeffs=[6.10063,0.0182803,-9.72947e-06,2.44489e-09,-2.3741e-13,-2643.3,-3.57369], Tmin=(1090.04,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-11.9744,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (174.604,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
CBS-QB3 with rotors

Bond corrections: {'H-N': 2, 'C-N': 1, 'C-H': 2, 'O-O': 1, 'C-O': 1}
1D rotors:
pivots: [1, 2], dihedral: [5, 1, 2, 3], rotor symmetry: 1, max scan energy: 44.49 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 6 5 1 2 F
D 7 2 3 4 F
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 6.61 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
N      -1.06615100   -0.07964000    0.01857600
C       0.15881100    0.61247900    0.00890000
O       1.32369900   -0.17443400   -0.52994300
O       1.10383800   -0.51774600   -1.78076900
H      -1.04682600   -0.90457800    0.60658600
H      -1.35847700   -0.33422700   -0.91758500
H       0.10506600    1.49965200   -0.62169000
H       0.49779000    0.86027400    1.01430400
""",
)

entry(
    index = 29,
    label = "CH2jNHCH2OOH",
    molecule =
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {11,S}
3  N u0 p1 c0 {4,S} {5,S} {8,S}
4  C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
5  C u1 p0 c0 {3,S} {9,S} {10,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86487,0.0104873,0.000150215,-4.09168e-07,3.44723e-10,1583.38,11.0603], Tmin=(10,'K'), Tmax=(382.897,'K')),
            NASAPolynomial(coeffs=[2.7623,0.038527,-2.4353e-05,7.46515e-09,-8.80777e-13,1546.7,13.7396], Tmin=(382.897,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (13.1753,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
B3LYP/6-311+G(3df,2p) no rotors

Bond corrections: {'H-O': 1, 'C-N': 2, 'O-O': 1, 'C-H': 4, 'C-O': 1, 'H-N': 1}

External symmetry: 1, optical isomers: 1

Geometry:
C       0.77571600   -1.09059300    0.48147000
H       1.30167700   -1.59330300    1.27838500
H       0.78199800   -1.52239300   -0.50842100
N       0.69797800    0.29164400    0.55754400
C      -0.08053900    1.03798000   -0.38361000
O      -1.48731300    0.97978700   -0.16117100
O      -1.96830900   -0.29864100   -0.62893300
H       0.70360000    0.67752700    1.49022100
H       0.14516000    2.10029000   -0.28942300
H       0.13567800    0.68855900   -1.39374400
H      -1.69643900   -0.89474000    0.08888900
""",
)

entry(
    index = 30,
    label = "CH2dNCH2OH",
    molecule =
"""
1 O u0 p2 c0 {3,S} {9,S}
2 N u0 p1 c0 {3,S} {4,D}
3 C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
4 C u0 p0 c0 {2,D} {7,S} {8,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90546,0.0128189,2.46438e-05,-3.69882e-08,1.41923e-11,-13418.1,8.30539], Tmin=(10,'K'), Tmax=(905.746,'K')),
            NASAPolynomial(coeffs=[3.05617,0.0264654,-1.43446e-05,3.7714e-09,-3.87494e-13,-13670.1,10.0779], Tmin=(905.746,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-111.546,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
B3LYP/6-311+G(3df,2p) no rotors

Bond corrections: {'C-H': 4, 'H-O': 1, 'C=N': 1, 'C-O': 1, 'C-N': 1}

External symmetry: 1, optical isomers: 1

Geometry:
O      -0.66089000    0.61232700    0.77861300
C      -0.73096200   -0.34044300   -0.27641600
N      -0.33326500   -1.65693500    0.11826100
C       0.03398800   -1.88474700    1.30448300
H      -0.93968200    1.46939600    0.44719900
H      -0.08025800   -0.04331700   -1.10671400
H      -1.75499700   -0.41520600   -0.65963900
H       0.07285600   -1.12386100    2.08300800
H       0.32889600   -2.89762400    1.56666800
""",
)

entry(
    index = 31,
    label = "NH2CH2OOH",
    molecule =
"""
1 O u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {9,S}
3 N u0 p1 c0 {4,S} {7,S} {8,S}
4 C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92792,0.0054829,0.000114382,-2.94342e-07,2.41464e-10,-18023.6,9.31269], Tmin=(10,'K'), Tmax=(377.65,'K')),
            NASAPolynomial(coeffs=[2.55436,0.0294338,-1.80951e-05,5.44607e-09,-6.34716e-13,-17986.9,13.7141], Tmin=(377.65,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-149.849,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
B3LYP/6-311+G(3df,2p) no rotors

Bond corrections: {'H-O': 1, 'C-H': 2, 'H-N': 2, 'C-N': 1, 'O-O': 1, 'C-O': 1}

External symmetry: 1, optical isomers: 1

Geometry:
N      -0.78742800    0.64601100    0.30751800
C      -0.17817600   -0.58751400   -0.06252500
O      -0.91141400   -1.78795100    0.22282700
O      -0.87962600   -1.97662000    1.66059400
H      -0.84007400    0.76765800    1.30939400
H      -1.70349900    0.77196300   -0.10245700
H      -0.07113700   -0.64753200   -1.14688100
H       0.80231000   -0.66429900    0.40808700
H      -1.81775500   -1.90371400    1.87641800
""",
)

entry(
    index = 32,
    label = "NH2CH2OH",
    molecule =
"""
1 O u0 p2 c0 {3,S} {8,S}
2 N u0 p1 c0 {3,S} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9765,0.00143989,6.80532e-05,-1.21403e-07,7.06725e-11,-26506.9,7.64776], Tmin=(10,'K'), Tmax=(442.756,'K')),
            NASAPolynomial(coeffs=[1.2472,0.0261136,-1.55937e-05,4.62933e-09,-5.38242e-13,-26265.4,18.5896], Tmin=(442.756,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-220.399,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
B3LYP/6-311+G(3df,2p) no rotors

Bond corrections: {'C-N': 1, 'H-N': 2, 'C-H': 2, 'C-O': 1, 'H-O': 1}

External symmetry: 1, optical isomers: 1

Geometry:
N      -0.81687700   -0.22524400    0.48623900
C       0.23747700    0.35405300   -0.29764600
O      -0.05102900    0.58065200   -1.68133800
H      -1.00881700   -1.18715500    0.23687700
H      -1.67501800    0.30692800    0.41290700
H       0.46687100    1.34314800    0.09449300
H       1.12537600   -0.27521300   -0.19626800
H      -0.12287500   -0.26587500   -2.13161400
""",
)

entry(
    index = 33,
    label = "OOCNCOOj",
    molecule =
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {6,S}
2  O u0 p2 c0 {4,S} {7,S}
3  O u0 p2 c0 {1,S} {13,S}
4  O u1 p2 c0 {2,S}
5  N u0 p1 c0 {6,S} {7,S} {12,S}
6  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
7  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
8  H u0 p0 c0 {6,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.56925,0.0380171,4.3939e-06,-3.73281e-08,2.00377e-11,-15382.9,12.9224], Tmin=(10,'K'), Tmax=(758.106,'K')),
            NASAPolynomial(coeffs=[4.88457,0.0418742,-2.46011e-05,6.95617e-09,-7.61095e-13,-15892.6,4.89465], Tmin=(758.106,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-127.944,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
CBS-QB3

Bond corrections: {'O-O': 2, 'C-O': 2, 'H-O': 1, 'C-N': 2, 'C-H': 4, 'H-N': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [8, 1, 2, 3], invalidation reason: The rotor scan has a barrier of 48.81 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: 
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: 
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: 
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 7], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
O       1.95785300   -0.53224000   -0.92600100
O       1.63344600   -0.02712300    0.39135300
C       0.79368100    1.10681800    0.20961100
N      -0.50779800    0.83850500   -0.34682400
C      -1.38329100   -0.01257900    0.33702800
O      -0.97596400   -1.48065200    0.36797300
O      -0.61128800   -1.89784600   -0.81973600
H       1.31806700   -1.26230100   -1.00355100
H       1.29458800    1.83774200   -0.42884500
H       0.69344400    1.49989900    1.22526900
H      -0.48431000    0.66637100   -1.34310300
H      -2.36993700   -0.02517200   -0.12568000
H      -1.44254500    0.21728300    1.40040000
""",
)
