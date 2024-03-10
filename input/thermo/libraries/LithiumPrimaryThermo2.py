#!/usr/bin/env python
# encoding: utf-8

name = "LithiumPrimaryThermo2"
shortDesc = ""
longDesc = """

"""
entry(
    index = 0,
    label = "[Li]CC",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C  u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 Li u0 p0 c0 {1,S}
4 H  u0 p0 c0 {1,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {2,S}
8 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91528,0.00697966,7.27699e-05,-2.12135e-07,2.06165e-10,11739.2,6.79126], Tmin=(10,'K'), Tmax=(260.263,'K')),
            NASAPolynomial(coeffs=[2.96811,0.0215369,-1.11292e-05,2.77359e-09,-2.69065e-13,11788.5,10.0859], Tmin=(260.263,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (97.5975,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-Li': 1, 'C-H': 5, 'C-C': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 6], rotor symmetry: 3, max scan energy: 9.91 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
Li      2.03518930   -0.74871887    0.00006422
C       0.43464770    0.43791517   -0.00000873
C      -0.95199648   -0.22659637    0.00000238
H       0.49221387    1.11531261    0.86569202
H       0.49224113    1.11520975   -0.86578607
H      -1.09753223   -0.86913052    0.87582088
H      -1.09747493   -0.86932528   -0.87568607
H      -1.78974867    0.48532223   -0.00011267
""",
)

entry(
    index = 1,
    label = "[Li]C[C]C",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C  u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C  u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  Li u0 p0 c0 {1,S}
5  H  u0 p0 c0 {1,S}
6  H  u0 p0 c0 {2,S}
7  H  u0 p0 c0 {2,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {3,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81246,0.0160469,7.63788e-05,-2.13178e-07,1.85449e-10,10095,8.29158], Tmin=(10,'K'), Tmax=(293.988,'K')),
            NASAPolynomial(coeffs=[2.42263,0.034957,-2.01058e-05,5.61856e-09,-6.10844e-13,10176.7,13.2952], Tmin=(293.988,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (83.9236,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (249.434,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-Li': 1, 'C-H': 7, 'C-C': 2}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 6], rotor symmetry: 3, max scan energy: 14.86 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 1 2 4 F
A 1 2 5 F
D 5 1 2 3 F
D 1 2 4 9 F
pivots: [2, 4], dihedral: [1, 2, 4, 9], rotor symmetry: 3, max scan energy: 14.89 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 1 2 3 F
A 1 2 5 F
D 3 1 2 4 F
D 4 2 3 7 F


External symmetry: 1, optical isomers: 1

Geometry:
Li      0.00134579    2.25719199   -0.30913837
C       0.00004247    0.34879153    0.31430228
C      -1.24958812   -0.44032209   -0.09336201
C       1.24919570   -0.44120286   -0.09314786
H      -0.00005373    0.38267220    1.41602123
H      -1.35041418   -0.51648667   -1.18357817
H      -1.24058640   -1.47844267    0.28152510
H      -2.17376673    0.01724586    0.27662530
H       2.17364480    0.01579053    0.27688035
H       1.23946359   -1.47928758    0.28181877
H       1.35003872   -0.51751959   -1.18335651
""",
)

entry(
    index = 2,
    label = "[Li]C[C][C]C",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C  u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C  u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C  u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  Li u0 p0 c0 {1,S}
6  H  u0 p0 c0 {2,S}
7  H  u0 p0 c0 {2,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {3,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {3,S}
12 H  u0 p0 c0 {4,S}
13 H  u0 p0 c0 {4,S}
14 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75399,0.0219907,0.000115131,-3.29652e-07,2.9409e-10,6385.12,8.15021], Tmin=(10,'K'), Tmax=(286.938,'K')),
            NASAPolynomial(coeffs=[1.75336,0.0498799,-3.06625e-05,9.08165e-09,-1.03722e-12,6499.93,15.3043], Tmin=(286.938,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (53.0908,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (320.107,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 9, 'C-Li': 1, 'C-C': 3}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 6], rotor symmetry: 3, max scan energy: 19.29 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 1 2 4 F
A 1 2 3 F
A 1 2 5 F
D 5 1 2 3 F
D 1 2 4 9 F
pivots: [2, 4], dihedral: [1, 2, 4, 9], rotor symmetry: 3, max scan energy: 19.26 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 1 2 4 F
A 1 2 3 F
A 1 2 5 F
D 3 1 2 4 F
D 1 2 5 12 F
pivots: [2, 5], dihedral: [1, 2, 5, 12], rotor symmetry: 3, max scan energy: 19.27 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 1 2 4 F
A 1 2 3 F
A 1 2 5 F
D 4 1 2 5 F
D 1 2 3 7 F


External symmetry: 3, optical isomers: 1

Geometry:
Li     -0.00117184    0.00312281   -2.30674664
C       0.00002867    0.00065279   -0.28823262
C      -0.26415506   -1.40146105    0.26481765
C      -1.08157280    0.92917348    0.26817070
C       1.34602672    0.47182044    0.26651255
H       0.49916621   -2.12555688   -0.04337504
H      -1.23505436   -1.80111332   -0.05083473
H      -0.26968296   -1.40820933    1.37246087
H      -2.09024039    0.63346901   -0.04357234
H      -1.08639800    0.93091853    1.37583760
H      -0.93992179    1.97156476   -0.04066053
H       1.59368068    1.49385900   -0.04349913
H       1.35257358    0.47260121    1.37415593
H       2.17688202   -0.17164625   -0.04587023
""",
)

entry(
    index = 3,
    label = "[Li]C=C",
    molecule = 
"""
1 C  u0 p0 c0 {2,D} {3,S} {4,S}
2 C  u0 p0 c0 {1,D} {5,S} {6,S}
3 Li u0 p0 c0 {1,S}
4 H  u0 p0 c0 {1,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90371,0.00845074,1.28281e-05,-2.26902e-08,9.96753e-12,24034.1,6.34678], Tmin=(10,'K'), Tmax=(762.648,'K')),
            NASAPolynomial(coeffs=[3.12482,0.0160533,-9.04293e-06,2.47568e-09,-2.64362e-13,24050.6,9.22278], Tmin=(762.648,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (199.823,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-Li': 1, 'C-H': 3, 'C=C': 1}

External symmetry: 1, optical isomers: 1

Geometry:
Li      2.02078934   -0.50340026    0.00000000
C       0.29730105    0.42362447    0.00000000
C      -0.86825847   -0.23931511    0.00000000
H       0.13780912    1.51027996    0.00000000
H      -0.92460486   -1.33065804    0.00000000
H      -1.84829458    0.24536071    0.00000000
""",
)

entry(
    index = 4,
    label = "[Li]C[C]=C",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C  u0 p0 c0 {1,S} {3,D} {7,S}
3 C  u0 p0 c0 {2,D} {8,S} {9,S}
4 H  u0 p0 c0 {1,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {1,S}
7 Li u0 p0 c0 {2,S}
8 H  u0 p0 c0 {3,S}
9 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91948,0.0084227,0.000163493,-8.11532e-07,1.40674e-09,19958.2,7.64174], Tmin=(10,'K'), Tmax=(144.791,'K')),
            NASAPolynomial(coeffs=[3.30103,0.0255078,-1.35021e-05,3.40427e-09,-3.30408e-13,19976.1,9.43027], Tmin=(144.791,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (166.15,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (203.705,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-Li': 1, 'C-H': 5, 'C=C': 1, 'C-C': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 5], rotor symmetry: 3, max scan energy: 6.89 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 4 1 2 3 F


External symmetry: 1, optical isomers: 1

Geometry:
Li      1.67166910    1.35997921    0.00292056
C       0.08129500    0.34485885    0.00003565
C      -1.38992308    0.06145104   -0.00138774
C       0.92400205   -0.69933853   -0.00137406
H      -1.63803453   -1.00986046   -0.00383839
H      -1.86612646    0.51740096    0.87148348
H      -1.86524651    0.52115055   -0.87277435
H       2.02683455   -0.59335697   -0.00048633
H       0.63423709   -1.75537551   -0.00378542
""",
)

entry(
    index = 5,
    label = "[Li]CtC",
    molecule = 
"""
1 C  u0 p0 c0 {2,T} {3,S}
2 C  u0 p0 c0 {1,T} {4,S}
3 Li u0 p0 c0 {1,S}
4 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.44518,0.00371718,3.94555e-05,-1.0954e-07,8.51928e-11,32573.4,5.76229], Tmin=(10,'K'), Tmax=(466.187,'K')),
            NASAPolynomial(coeffs=[4.3019,0.00685299,-4.37587e-06,1.39287e-09,-1.72286e-13,32379.6,1.06079], Tmin=(466.187,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (270.823,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (78.9875,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C#C': 1, 'C-H': 1, 'C-Li': 1}

External symmetry: 1, optical isomers: 1

Geometry:
Li     -0.00000415   -0.00010459    2.14727859
C       0.00001290    0.00010300    0.24222456
C      -0.00001948   -0.00001522   -0.97547300
H       0.00005191   -0.00021293   -2.04255193
""",
)

entry(
    index = 6,
    label = "[Li]OCO",
    molecule = 
"""
1 O  u0 p2 c0 {3,S} {4,S}
2 O  u0 p2 c0 {3,S} {7,S}
3 C  u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
4 Li u0 p0 c0 {1,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90799,0.00741544,7.61269e-05,-2.07885e-07,1.72674e-10,-53302.6,8.55141], Tmin=(10,'K'), Tmax=(389.343,'K')),
            NASAPolynomial(coeffs=[3.31581,0.0222007,-1.43588e-05,4.45385e-09,-5.28639e-13,-53322.4,10.0028], Tmin=(389.343,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-443.178,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'H-O': 1, 'C-H': 2, 'Li-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 4]]) broke during the scan.The rotor scan has a barrier of 203.72 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 7], invalidation reason: The rotor scan has a barrier of 54.31 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 1, optical isomers: 2

Geometry:
Li     -0.17635125   -1.55210447    0.02881330
O      -1.17256044   -0.11473417    0.00720275
C      -0.14328864    0.69757968   -0.00251405
O       1.11622510   -0.19267435   -0.05081489
H      -0.04893121    1.33911932   -0.89702753
H      -0.00456425    1.31163500    0.90942333
H       1.88194102    0.26781907    0.29074813
""",
)

entry(
    index = 7,
    label = "[Li]OCN",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 N  u0 p1 c0 {1,S} {6,S} {7,S}
3 O  u0 p2 c0 {1,S} {8,S}
4 H  u0 p0 c0 {1,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {2,S}
8 Li u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95205,0.00304831,8.52008e-05,-1.73749e-07,1.11409e-10,-28911,8.48663], Tmin=(10,'K'), Tmax=(486.29,'K')),
            NASAPolynomial(coeffs=[2.17892,0.0268667,-1.67502e-05,5.06353e-09,-5.90937e-13,-28847.7,14.6401], Tmin=(486.29,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-240.392,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'H-N': 2, 'C-H': 2, 'Li-O': 1, 'C-N': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: The rotor scan has a barrier of 65.50 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 7], invalidation reason: Bond ([[1, 4]]) broke during the scan.The rotor scan has a barrier of 100.29 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 1, optical isomers: 1

Geometry:
Li     -0.36845226   -1.56229284    0.00477104
O      -1.21307816   -0.06130424   -0.00240389
C      -0.10078536    0.68805134    0.00220051
N       1.13941843   -0.21967494   -0.00077473
H      -0.00047509    1.33422767    0.89566577
H      -0.00004944    1.34430440   -0.88374824
H       1.72488458   -0.04035429    0.80443428
H       1.71323168   -0.04938896   -0.81632012
""",
)

entry(
    index = 8,
    label = "[Li]OC=N",
    molecule = 
"""
1 O  u0 p2 c0 {3,S} {4,S}
2 N  u0 p1 c0 {3,D} {6,S}
3 C  u0 p0 c0 {1,S} {2,D} {5,S}
4 Li u0 p0 c0 {1,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95938,0.00239786,5.75123e-05,-1.09928e-07,6.4129e-11,-30837.7,7.46754], Tmin=(10,'K'), Tmax=(554.645,'K')),
            NASAPolynomial(coeffs=[2.85015,0.0194241,-1.29458e-05,4.10256e-09,-4.94812e-13,-30853.5,10.9135], Tmin=(554.645,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-256.415,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-N': 1, 'C-H': 1, 'C=N': 1, 'Li-O': 1, 'C-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 4]]) broke during the scan.Bond ([[1, 2]]) broke during the scan.Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformersCould not read energies


External symmetry: 1, optical isomers: 1

Geometry:
Li     -0.21902696   -1.56328323   -0.00000190
O      -1.14058366    0.06053324    0.00000992
C       0.01701437    0.57313850   -0.00000253
N       1.09003537   -0.17933616   -0.00000060
H       0.09814440    1.67380590   -0.00000592
H       1.94883938    0.34726104   -0.00000145
""",
)

entry(
    index = 9,
    label = "[Li]OCC",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C  u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 O  u0 p2 c0 {1,S} {9,S}
4 H  u0 p0 c0 {1,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {2,S}
8 H  u0 p0 c0 {2,S}
9 Li u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78527,0.0240446,-7.01043e-05,2.19126e-07,-2.15094e-10,-29415.9,9.52113], Tmin=(10,'K'), Tmax=(396.387,'K')),
            NASAPolynomial(coeffs=[1.22624,0.0300511,-1.78431e-05,5.10522e-09,-5.65326e-13,-29057.4,21.4627], Tmin=(396.387,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-244.588,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (199.547,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'Li-O': 1, 'C-C': 1, 'C-O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 0.02 kJ/mol (set as a FreeRotor)
pivots: [3, 4], dihedral: [2, 3, 4, 7], rotor symmetry: 3, max scan energy: 15.00 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
Li      2.43610695   -0.64117775   -0.00171087
O       1.00196542    0.05106032    0.00100417
C      -0.24728768    0.61468689    0.00329746
C      -1.35935388   -0.43034363    0.00018317
H      -0.39130442    1.26555266    0.88499490
H      -0.39195220    1.27140880   -0.87393420
H      -1.27757695   -1.07037351    0.88268601
H      -1.27812348   -1.06453984   -0.88657734
H      -2.34945561    0.03586853    0.00197986
""",
)

entry(
    index = 10,
    label = "[Li]OC[C]C",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C  u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C  u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  O  u0 p2 c0 {1,S} {12,S}
5  H  u0 p0 c0 {1,S}
6  H  u0 p0 c0 {2,S}
7  H  u0 p0 c0 {2,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {3,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {3,S}
12 Li u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73327,0.0229466,3.09263e-05,-6.51172e-08,3.28838e-11,-34510.1,10.5621], Tmin=(10,'K'), Tmax=(663.667,'K')),
            NASAPolynomial(coeffs=[2.36108,0.0389696,-2.28107e-05,6.46424e-09,-7.10939e-13,-34498.7,15.3332], Tmin=(663.667,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-286.965,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (270.22,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 7, 'C-C': 2, 'Li-O': 1, 'C-O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 0.02 kJ/mol (set as a FreeRotor)
pivots: [3, 4], dihedral: [2, 3, 4, 7], rotor symmetry: 3, max scan energy: 14.78 kJ/mol
pivots: [3, 5], dihedral: [2, 3, 5, 10], rotor symmetry: 3, max scan energy: 14.85 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
Li     -2.71154165   -0.01425702    0.33598432
O      -1.17468615   -0.00604400   -0.08722836
C       0.16374710    0.00110997   -0.39276185
C       0.85529442   -1.25210410    0.14545363
C       0.84149781    1.26237723    0.14415155
H       0.30336422    0.00129875   -1.49078010
H       0.37461763   -2.14587596   -0.25817720
H       1.91653205   -1.28157414   -0.11871183
H       0.76879355   -1.28246616    1.23600917
H       0.75430984    1.29300690    1.23463858
H       0.35134431    2.15046297   -0.26062779
H       1.90243832    1.30306468   -0.11970275
""",
)

entry(
    index = 11,
    label = "[Li]OC[C][C]C",
    molecule = 
"""
1  O  u0 p2 c0 {2,S} {6,S}
2  C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  C  u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4  C  u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
5  C  u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
6  Li u0 p0 c0 {1,S}
7  H  u0 p0 c0 {3,S}
8  H  u0 p0 c0 {3,S}
9  H  u0 p0 c0 {3,S}
10 H  u0 p0 c0 {4,S}
11 H  u0 p0 c0 {4,S}
12 H  u0 p0 c0 {4,S}
13 H  u0 p0 c0 {5,S}
14 H  u0 p0 c0 {5,S}
15 H  u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90132,0.0109021,0.000367825,-1.64377e-06,2.54824e-09,-39789.9,8.7177], Tmin=(10,'K'), Tmax=(162.25,'K')),
            NASAPolynomial(coeffs=[2.13479,0.054455,-3.48385e-05,1.08053e-08,-1.28913e-12,-39732.6,14.0275], Tmin=(162.25,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-330.61,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (345.051,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 9, 'C-C': 3, 'Li-O': 1, 'C-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: not a torsional mode (angles = 179.93, 109.71 degrees)
pivots: [3, 4], dihedral: [2, 3, 4, 7], rotor symmetry: 3, max scan energy: 15.35 kJ/mol
pivots: [3, 5], dihedral: [2, 3, 5, 10], rotor symmetry: 3, max scan energy: 15.35 kJ/mol
pivots: [3, 6], dihedral: [2, 3, 6, 13], rotor symmetry: 3, max scan energy: 15.35 kJ/mol


External symmetry: 3, optical isomers: 1

Geometry:
Li      2.86193480    0.00146544   -0.00238292
O       1.26648577    0.00148831   -0.00192426
C      -0.11092658    0.00019535   -0.00054832
C      -0.62943295   -0.56417428   -1.33040520
C      -0.62968387    1.43382917    0.17709789
C      -0.62659706   -0.87038080    1.15372616
H      -0.26019088   -1.58353894   -1.46715692
H      -1.72221245   -0.58315856   -1.37590546
H      -0.25950980    0.04505232   -2.15871115
H      -0.26479114    2.06205712   -0.63917655
H      -1.72245314    1.48189943    0.18857944
H      -0.25519190    1.84687705    1.11688292
H      -0.25569712   -0.47882422    2.10409062
H      -1.71925970   -0.90171220    1.19479269
H      -0.25551169   -1.89183175    1.03932454
""",
)

entry(
    index = 12,
    label = "[Li]OCtC",
    molecule = 
"""
1 O  u0 p2 c0 {2,S} {4,S}
2 C  u0 p0 c0 {1,S} {3,T}
3 C  u0 p0 c0 {2,T} {5,S}
4 Li u0 p0 c0 {1,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90844,0.00604744,6.35292e-05,-1.7051e-07,1.27253e-10,-1297.66,7.29513], Tmin=(10,'K'), Tmax=(486.906,'K')),
            NASAPolynomial(coeffs=[5.43676,0.0113582,-7.87145e-06,2.61136e-09,-3.28999e-13,-1658.27,-1.15301], Tmin=(486.906,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-10.8082,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'Li-O': 1, 'C-H': 1, 'C-O': 1, 'C#C': 1}

External symmetry: 1, optical isomers: 1

Geometry:
Li     -0.35884252   -1.51459863   -0.00000060
O      -1.15444060    0.26187038    0.00000082
C       0.07224523    0.35647218   -0.00000101
C       1.26365030    0.00906425   -0.00000033
H       2.30248490    0.24706598   -0.00001198
""",
)

entry(
    index = 13,
    label = "[Li]ON",
    molecule = 
"""
1 N  u0 p1 c0 {2,S} {3,S} {4,S}
2 O  u0 p2 c0 {1,S} {5,S}
3 H  u0 p0 c0 {1,S}
4 H  u0 p0 c0 {1,S}
5 Li u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.06754,-0.00674233,8.50786e-05,-1.62332e-07,1.0051e-10,-8019.64,6.2681], Tmin=(10,'K'), Tmax=(520.598,'K')),
            NASAPolynomial(coeffs=[3.00368,0.0136143,-8.67681e-06,2.67941e-09,-3.17129e-13,-8073.96,9.12058], Tmin=(520.598,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-66.6867,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'N-O': 1, 'Li-O': 1, 'H-N': 2}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 3]]) broke during the scan.Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformersCould not read energies


External symmetry: 1, optical isomers: 1

Geometry:
Li     -0.98802110   -1.07093226   -0.00034366
O      -0.52794903    0.56266134    0.00010067
N       0.67599675   -0.20341536    0.00007690
H       1.22764743    0.06777622    0.80895387
H       1.22805234    0.06840637   -0.80830535
""",
)

entry(
    index = 14,
    label = "[Li]ONC",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 N  u0 p1 c0 {1,S} {3,S} {7,S}
3 O  u0 p2 c0 {2,S} {8,S}
4 H  u0 p0 c0 {1,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {1,S}
7 H  u0 p0 c0 {2,S}
8 Li u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94426,0.00361654,8.68157e-05,-1.86241e-07,1.24574e-10,-9263.13,8.53808], Tmin=(10,'K'), Tmax=(476.292,'K')),
            NASAPolynomial(coeffs=[2.62506,0.0254458,-1.57881e-05,4.76238e-09,-5.55815e-13,-9259.41,12.6439], Tmin=(476.292,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-77.03,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-N': 1, 'C-H': 3, 'Li-O': 1, 'N-O': 1, 'C-N': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: The rotor scan has a barrier of 40.04 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
pivots: [3, 4], dihedral: [2, 3, 4, 6], rotor symmetry: 3, max scan energy: 13.50 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
Li      1.55364894   -0.93461118    0.49653840
O       0.99418127    0.60300798    0.03328543
N       0.00262445   -0.32533751   -0.37905790
C      -1.28441370    0.02722566    0.19931469
H      -0.08394086   -0.24091101   -1.38765376
H      -2.05876040   -0.63873575   -0.19298446
H      -1.23870027   -0.08988274    1.28345950
H      -1.54469616    1.06855863   -0.01782818
""",
)

entry(
    index = 15,
    label = "[Li]ON[C]C",
    molecule = 
"""
1  O  u0 p2 c0 {2,S} {5,S}
2  N  u0 p1 c0 {1,S} {3,S} {4,S}
3  C  u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
4  C  u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
5  Li u0 p0 c0 {1,S}
6  H  u0 p0 c0 {3,S}
7  H  u0 p0 c0 {3,S}
8  H  u0 p0 c0 {3,S}
9  H  u0 p0 c0 {4,S}
10 H  u0 p0 c0 {4,S}
11 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79813,0.0201331,3.05763e-05,-5.84027e-08,2.68026e-11,-7532.34,10.0697], Tmin=(10,'K'), Tmax=(766.587,'K')),
            NASAPolynomial(coeffs=[3.35818,0.0342042,-1.99983e-05,5.61797e-09,-6.1074e-13,-7810.88,9.81851], Tmin=(766.587,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-62.6365,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (245.277,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 6, 'C-N': 2, 'Li-O': 1, 'N-O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 0.18 kJ/mol (set as a FreeRotor)
pivots: [3, 4], dihedral: [2, 3, 4, 6], rotor symmetry: 3, max scan energy: 19.43 kJ/mol
pivots: [3, 5], dihedral: [2, 3, 5, 9], rotor symmetry: 3, max scan energy: 19.43 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
Li     -2.67660670   -0.00411615    0.26863706
O      -1.12881978   -0.00193126   -0.08102896
N       0.20771500    0.00041736   -0.43649438
C       0.81784732   -1.18845336    0.11230360
C       0.81354467    1.19162282    0.11198830
H       1.88116311   -1.20592873   -0.13848781
H       0.34227824   -2.06713381   -0.32491546
H       0.70327976   -1.23783452    1.21048116
H       1.87679210    1.21288130   -0.13878869
H       0.33482673    2.06847560   -0.32546243
H       0.69877246    1.24084738    1.21014755
""",
)

entry(
    index = 16,
    label = "[Li]ONO",
    molecule = 
"""
1 O  u0 p2 c0 {3,S} {4,S}
2 O  u0 p2 c0 {3,S} {6,S}
3 N  u0 p1 c0 {1,S} {2,S} {5,S}
4 Li u0 p0 c0 {1,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93143,0.00419504,6.65356e-05,-1.44751e-07,9.25028e-11,-17534.2,8.51206], Tmin=(10,'K'), Tmax=(537.987,'K')),
            NASAPolynomial(coeffs=[4.16009,0.0173973,-1.18247e-05,3.84029e-09,-4.73444e-13,-17774.5,5.54635], Tmin=(537.987,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-145.811,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'N-O': 2, 'H-N': 1, 'H-O': 1, 'Li-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for [Li]ONO exists which is 21.71 kJ/mol lower.
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 6], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
Li      0.78229900   -0.48363500   -0.98860400
O       1.26097500   -0.28792100    0.65867800
N       0.08335800    0.08383700    0.98864800
O      -0.86325700    0.10599900   -0.72282200
H       0.01380900    1.12004900    0.99443600
H      -1.70006600   -0.29064700   -0.46647500
""",
)

entry(
    index = 17,
    label = "[Li]ON=O",
    molecule = 
"""
1 O  u0 p2 c0 {3,S} {4,S}
2 O  u0 p2 c0 {3,D}
3 N  u0 p1 c0 {1,S} {2,D}
4 Li u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94597,0.00351547,4.35431e-05,-1.06826e-07,7.50278e-11,-22668.8,6.72101], Tmin=(10,'K'), Tmax=(498.207,'K')),
            NASAPolynomial(coeffs=[4.33893,0.0104673,-7.81722e-06,2.61963e-09,-3.24698e-13,-22833.4,3.84016], Tmin=(498.207,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-188.492,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'N-O': 1, 'Li-O': 1, 'N=O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 4]]) broke during the scan.The rotor scan has a barrier of 82.08 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 2, optical isomers: 1

Geometry:
Li      0.00167253   -1.56651574    0.00000000
O      -1.04905971   -0.00548014    0.00000000
N      -0.00061034    0.68174164    0.00000000
O       1.04916772   -0.00343814    0.00000000
""",
)

entry(
    index = 18,
    label = "[Li]N",
    molecule = 
"""
1 N  u0 p1 c0 {2,S} {3,S} {4,S}
2 Li u0 p0 c0 {1,S}
3 H  u0 p0 c0 {1,S}
4 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96541,0.0021667,2.85603e-05,-6.7189e-08,4.5766e-11,3299.87,2.9137], Tmin=(10,'K'), Tmax=(522.598,'K')),
            NASAPolynomial(coeffs=[4.51009,0.00558866,-3.04998e-06,9.30272e-10,-1.17229e-13,3139.28,-0.352375], Tmin=(522.598,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (27.4262,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'Li-N': 1, 'H-N': 2}

External symmetry: 2, optical isomers: 1

Geometry:
Li     -1.40647173    0.00028944    0.00007673
N       0.33083818   -0.00003900    0.00010084
H       0.95249706    0.79904741    0.00061353
H       0.95111847   -0.80020635    0.00061242
""",
)

entry(
    index = 19,
    label = "[Li]NC",
    molecule = 
"""
1 N  u0 p1 c0 {2,S} {3,S} {7,S}
2 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
3 Li u0 p0 c0 {1,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75569,0.0250946,-8.3018e-05,1.86333e-07,-1.4379e-10,6985.38,7.00171], Tmin=(10,'K'), Tmax=(452.751,'K')),
            NASAPolynomial(coeffs=[2.7145,0.0186738,-9.99698e-06,2.6122e-09,-2.67638e-13,7239.75,12.9677], Tmin=(452.751,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (58.0761,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (153.818,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-N': 1, 'C-H': 3, 'Li-N': 1, 'C-N': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 5], rotor symmetry: 1, max scan energy: 7.28 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 4 1 2 3 F
D 2 3 5 6 F
D 4 1 2 3 F
D 2 3 5 7 F


External symmetry: 1, optical isomers: 1

Geometry:
Li      1.96298665   -0.54202406    0.00417884
N       0.44856891    0.32006560   -0.00095947
C      -0.91649696   -0.16298433    0.00006451
H       0.41265082    1.33263920   -0.00544698
H      -1.50254527    0.14130195   -0.88373213
H      -1.50391306    0.14894078    0.88028419
H      -0.93480561   -1.26068913    0.00480503
""",
)

entry(
    index = 20,
    label = "[Li]NCC",
    molecule = 
"""
1  N  u0 p1 c0 {2,S} {4,S} {10,S}
2  C  u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3  C  u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4  Li u0 p0 c0 {1,S}
5  H  u0 p0 c0 {2,S}
6  H  u0 p0 c0 {2,S}
7  H  u0 p0 c0 {3,S}
8  H  u0 p0 c0 {3,S}
9  H  u0 p0 c0 {3,S}
10 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.62017,0.0399853,-0.00012608,3.01413e-07,-2.52324e-10,2425.43,8.58931], Tmin=(10,'K'), Tmax=(417.684,'K')),
            NASAPolynomial(coeffs=[2.21841,0.031708,-1.84195e-05,5.18401e-09,-5.66887e-13,2731.83,16.3943], Tmin=(417.684,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (20.1555,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (224.491,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-N': 1, 'C-H': 5, 'Li-N': 1, 'C-C': 1, 'C-N': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 10.68 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 5 1 2 3 F
pivots: [3, 4], dihedral: [2, 3, 4, 8], rotor symmetry: 3, max scan energy: 16.23 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
Li      1.61598454   -1.46502765    0.00501984
N       1.10985091    0.21136348    0.00059992
C      -0.24817169    0.70274217   -0.00063483
C      -1.23929028   -0.45268036   -0.00034931
H       1.73535955    1.00720241   -0.00148437
H      -0.47588165    1.33467780    0.87628836
H      -0.47465311    1.33316429   -0.87892590
H      -1.09890369   -1.07791260    0.88965586
H      -1.09905264   -1.07834767   -0.88999954
H      -2.27680449   -0.11034948   -0.00015054
""",
)

entry(
    index = 21,
    label = "[Li]NC[C]C",
    molecule = 
"""
1  N  u0 p1 c0 {2,S} {5,S} {13,S}
2  C  u0 p0 c0 {1,S} {3,S} {4,S} {6,S}
3  C  u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4  C  u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
5  Li u0 p0 c0 {1,S}
6  H  u0 p0 c0 {2,S}
7  H  u0 p0 c0 {3,S}
8  H  u0 p0 c0 {3,S}
9  H  u0 p0 c0 {3,S}
10 H  u0 p0 c0 {4,S}
11 H  u0 p0 c0 {4,S}
12 H  u0 p0 c0 {4,S}
13 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78448,0.01961,0.000114761,-3.48297e-07,3.34838e-10,-2456.87,10.1387], Tmin=(10,'K'), Tmax=(265.227,'K')),
            NASAPolynomial(coeffs=[2.12315,0.0446652,-2.69402e-05,7.88019e-09,-8.92296e-13,-2368.75,15.9487], Tmin=(265.227,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-20.422,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-N': 1, 'C-H': 7, 'C-C': 2, 'Li-N': 1, 'C-N': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [3, 4], dihedral: [2, 3, 4, 8], rotor symmetry: 3, max scan energy: 15.49 kJ/mol
pivots: [3, 5], dihedral: [2, 3, 5, 11], rotor symmetry: 3, max scan energy: 16.06 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
Li      2.45483180    0.27099901   -0.61232808
N       0.97169478    0.82313474    0.14077283
C      -0.19964267    0.02205479    0.41281532
C      -1.46115558    0.55306777   -0.27487919
C       0.05970171   -1.41688511   -0.02351438
H       0.77939210    1.77269387    0.43704585
H      -0.42282929   -0.01726882    1.49587795
H      -1.31919390    0.55849098   -1.35993462
H      -1.66127930    1.58114795    0.03735614
H      -2.34557719   -0.04843032   -0.03890031
H       0.93026876   -1.82796249    0.49925254
H      -0.78765735   -2.07474673    0.18318827
H       0.24749137   -1.45363215   -1.10468196
""",
)

entry(
    index = 22,
    label = "[Li]NC[C][C]C",
    molecule = 
"""
1  N  u0 p1 c0 {2,S} {6,S} {16,S}
2  C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  C  u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4  C  u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
5  C  u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
6  Li u0 p0 c0 {1,S}
7  H  u0 p0 c0 {3,S}
8  H  u0 p0 c0 {3,S}
9  H  u0 p0 c0 {3,S}
10 H  u0 p0 c0 {4,S}
11 H  u0 p0 c0 {4,S}
12 H  u0 p0 c0 {4,S}
13 H  u0 p0 c0 {5,S}
14 H  u0 p0 c0 {5,S}
15 H  u0 p0 c0 {5,S}
16 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76729,0.0193321,0.000231786,-7.11871e-07,6.70784e-10,-7276.62,10.1214], Tmin=(10,'K'), Tmax=(346.57,'K')),
            NASAPolynomial(coeffs=[2.77075,0.0559341,-3.527e-05,1.08196e-08,-1.27943e-12,-7358.29,11.6983], Tmin=(346.57,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-60.4677,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (365.837,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 9, 'H-N': 1, 'C-C': 3, 'Li-N': 1, 'C-N': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 3, max scan energy: 9.22 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 7 1 2 3 F
pivots: [3, 4], dihedral: [2, 3, 4, 8], rotor symmetry: 3, max scan energy: 17.01 kJ/mol
pivots: [3, 5], dihedral: [2, 3, 5, 11], rotor symmetry: 3, max scan energy: 16.37 kJ/mol
pivots: [3, 6], dihedral: [2, 3, 6, 14], rotor symmetry: 3, max scan energy: 16.39 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
Li     -2.73622682    0.02689338   -0.28940168
N      -1.07322095    0.10498286   -0.83590572
C       0.12105641    0.00323669   -0.02084057
C      -0.31244159   -0.18980885    1.43504264
C       0.97597497    1.27840273   -0.11191641
C       0.98725818   -1.19780420   -0.43629550
H      -0.78120309    0.23393216   -1.79865693
H      -0.90781695   -1.10461607    1.53521082
H       0.53927609   -0.27769193    2.11389534
H      -0.91282522    0.66394743    1.76965791
H       0.38940197    2.14388524    0.20470342
H       1.88013143    1.22258381    0.50352922
H       1.28473341    1.44822311   -1.14709888
H       1.30184916   -1.08922422   -1.47794981
H       1.88832702   -1.29695702    0.17821738
H       0.40759704   -2.12061238   -0.36029317
""",
)

entry(
    index = 23,
    label = "[Li]NO",
    molecule = 
"""
1 N  u0 p1 c0 {2,S} {3,S} {4,S}
2 O  u0 p2 c0 {1,S} {5,S}
3 Li u0 p0 c0 {1,S}
4 H  u0 p0 c0 {1,S}
5 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95749,0.00237177,4.62145e-05,-8.64002e-08,4.75039e-11,-656.897,6.67509], Tmin=(10,'K'), Tmax=(614.483,'K')),
            NASAPolynomial(coeffs=[3.5257,0.0156179,-1.15939e-05,3.95429e-09,-5.00369e-13,-800.846,6.94486], Tmin=(614.483,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-5.48116,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (103.931,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'N-O': 1, 'Li-N': 1, 'H-N': 1, 'H-O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 5], rotor symmetry: 1, max scan energy: 128.32 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 1 2 4 F
D 4 1 2 3 F
B 1 3 F


External symmetry: 1, optical isomers: 2

Geometry:
Li     -0.25026662   -1.43006095   -0.01355181
N      -0.75661108    0.26820749    0.12277870
O       0.73826025    0.10867040   -0.10801651
H      -0.99205942    0.96770621   -0.57414437
H       1.13381725    0.58321059    0.62267065
""",
)

entry(
    index = 24,
    label = "[Li]N=O",
    molecule = 
"""
1 O  u0 p2 c0 {2,D}
2 N  u0 p1 c0 {1,D} {3,S}
3 Li u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.4681,0.00235635,2.23974e-05,-6.83578e-08,5.87588e-11,21637.1,5.7564], Tmin=(10,'K'), Tmax=(414.146,'K')),
            NASAPolynomial(coeffs=[3.73483,0.00460715,-3.23769e-06,1.05083e-09,-1.28395e-13,21573.6,4.20496], Tmin=(414.146,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (179.901,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (54.0441,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'Li-N': 1, 'N=O': 1}

External symmetry: 1, optical isomers: 1

Geometry:
Li      0.00000000   -0.00012569    1.97167093
N       0.00000000    0.00013181    0.24282062
O       0.00000000   -0.00006820   -0.95188386
""",
)

entry(
    index = 25,
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
Bond corrections: {'C=N': 1, 'Li-N': 1, 'C-H': 2}

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
    index = 26,
    label = "[Li]S",
    molecule = 
"""
1 S  u0 p2 c0 {2,S} {3,S}
2 Li u0 p0 c0 {1,S}
3 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96923,0.0019845,1.99192e-05,-5.32821e-08,3.90783e-11,-5024.44,5.08461], Tmin=(10,'K'), Tmax=(504.914,'K')),
            NASAPolynomial(coeffs=[4.66999,0.00286084,-1.78023e-06,5.82381e-10,-7.59105e-14,-5177.14,1.37135], Tmin=(504.914,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-41.7832,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'Li-S': 1, 'H-S': 1}

External symmetry: 1, optical isomers: 1

Geometry:
Li      1.84021343   -0.04837003    0.00000000
S      -0.30984691    0.08578287    0.00000000
H      -0.56302646   -1.22984230    0.00000000
""",
)

entry(
    index = 27,
    label = "[Li]SCO",
    molecule = 
"""
1 S  u0 p2 c0 {3,S} {4,S}
2 O  u0 p2 c0 {3,S} {7,S}
3 C  u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
4 Li u0 p0 c0 {1,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8922,0.00779817,8.95013e-05,-2.45311e-07,1.97055e-10,-30224.6,8.95804], Tmin=(10,'K'), Tmax=(428.303,'K')),
            NASAPolynomial(coeffs=[4.21973,0.0210282,-1.38803e-05,4.40133e-09,-5.31966e-13,-30402.1,5.91142], Tmin=(428.303,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-251.306,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'Li-S': 1, 'H-O': 1, 'C-H': 2, 'C-S': 1, 'C-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 4]]) broke during the scan.Bond ([[1, 2]]) broke during the scan.Significant difference observed between consecutive conformersBond ([[3, 5]]) broke during the scan.Bond ([[3, 6]]) broke during the scan.Significant difference observed between consecutive conformersCould not read energies
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 7], invalidation reason: Bond ([[1, 4]]) broke during the scan.Significant difference observed between consecutive conformersCould not read energies


External symmetry: 1, optical isomers: 1

Geometry:
Li      0.27878656   -1.69162834    0.00065546
S      -1.17132577   -0.02830291    0.00050671
C       0.42940315    0.77604316    0.00079031
O       1.47927937   -0.25695500   -0.00090280
H       0.57320394    1.38909316   -0.89157228
H       0.57377620    1.38664850    0.89474598
H       2.34843195    0.14509441    0.00125362
""",
)

entry(
    index = 28,
    label = "[Li]SCC",
    molecule = 
"""
1 S  u0 p2 c0 {2,S} {4,S}
2 C  u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3 C  u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4 Li u0 p0 c0 {1,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {3,S}
8 H  u0 p0 c0 {3,S}
9 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49884,0.0535066,-0.000219761,5.11558e-07,-4.17968e-10,-7033.24,9.72394], Tmin=(10,'K'), Tmax=(407.226,'K')),
            NASAPolynomial(coeffs=[3.30783,0.0267196,-1.55122e-05,4.33894e-09,-4.70525e-13,-6780.02,13.392], Tmin=(407.226,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-58.4932,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (199.547,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'Li-S': 1, 'C-H': 5, 'C-C': 1, 'C-S': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 4.99 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 1 2 3 F
pivots: [3, 4], dihedral: [2, 3, 4, 7], rotor symmetry: 3, max scan energy: 19.24 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 1 2 3 F
D 1 2 3 6 F


External symmetry: 1, optical isomers: 1

Geometry:
Li     -0.68742196   -1.96161478   -0.00058951
S      -1.14721804    0.14470484    0.00073877
C       0.56935598    0.75882025    0.00113963
C       1.63788342   -0.32608314   -0.00030472
H       0.70613436    1.39403171    0.87867155
H       0.70582834    1.39603278   -0.87498393
H       1.55709214   -0.95561089   -0.89532704
H       2.64868479    0.09193209   -0.00012853
H       1.55759998   -0.95750393    0.89343991
""",
)

entry(
    index = 29,
    label = "[Li]SC[C]C",
    molecule = 
"""
1  S  u0 p2 c0 {2,S} {5,S}
2  C  u0 p0 c0 {1,S} {3,S} {4,S} {6,S}
3  C  u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4  C  u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
5  Li u0 p0 c0 {1,S}
6  H  u0 p0 c0 {2,S}
7  H  u0 p0 c0 {3,S}
8  H  u0 p0 c0 {3,S}
9  H  u0 p0 c0 {3,S}
10 H  u0 p0 c0 {4,S}
11 H  u0 p0 c0 {4,S}
12 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.5658,0.0385261,-2.30346e-05,6.2452e-09,-5.18716e-13,-11193.1,12.0501], Tmin=(10,'K'), Tmax=(1345.47,'K')),
            NASAPolynomial(coeffs=[9.41805,0.0248402,-1.19156e-05,2.78666e-09,-2.57144e-13,-13103.9,-19.169], Tmin=(1345.47,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-93.1063,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (270.22,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'Li-S': 1, 'C-H': 7, 'C-C': 2, 'C-S': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 7.50 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 1 2 3 F
pivots: [3, 4], dihedral: [2, 3, 4, 7], rotor symmetry: 3, max scan energy: 15.82 kJ/mol
pivots: [3, 5], dihedral: [2, 3, 5, 10], rotor symmetry: 3, max scan energy: 22.00 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 1 2 3 F
D 1 2 3 6 F


External symmetry: 1, optical isomers: 2

Geometry:
Li      1.79291558   -1.37795421   -0.71661255
S       1.22517642    0.54119316    0.08316653
C      -0.50250001    0.03234947    0.41600661
C      -1.48742786    0.93915620   -0.31105078
C      -0.76906447   -1.43050446    0.06805925
H      -0.65837890    0.14731660    1.49235103
H      -1.36026420    0.84981028   -1.39327832
H      -1.31600404    1.98209122   -0.04526828
H      -2.52260017    0.68238043   -0.06072795
H      -0.12041377   -2.10397876    0.64182724
H      -0.62799840   -1.60454468   -1.00872829
H      -1.79867568   -1.72460592    0.29254400
""",
)

entry(
    index = 30,
    label = "[Li]SC[C][C]C",
    molecule = 
"""
1  S  u0 p2 c0 {2,S} {6,S}
2  C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  C  u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4  C  u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
5  C  u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
6  Li u0 p0 c0 {1,S}
7  H  u0 p0 c0 {3,S}
8  H  u0 p0 c0 {3,S}
9  H  u0 p0 c0 {3,S}
10 H  u0 p0 c0 {4,S}
11 H  u0 p0 c0 {4,S}
12 H  u0 p0 c0 {4,S}
13 H  u0 p0 c0 {5,S}
14 H  u0 p0 c0 {5,S}
15 H  u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84433,0.0179394,0.000365074,-1.91039e-06,3.45489e-09,-15900.5,10.4383], Tmin=(10,'K'), Tmax=(138.979,'K')),
            NASAPolynomial(coeffs=[2.55488,0.0550514,-3.54726e-05,1.0981e-08,-1.30286e-12,-15864.6,14.1145], Tmin=(138.979,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-131.585,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (345.051,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 9, 'Li-S': 1, 'C-C': 3, 'C-S': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [3, 4], dihedral: [2, 3, 4, 7], rotor symmetry: 3, max scan energy: 17.64 kJ/mol
pivots: [3, 5], dihedral: [2, 3, 5, 10], rotor symmetry: 3, max scan energy: 25.07 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 1 2 3 6 F
pivots: [3, 6], dihedral: [2, 3, 6, 13], rotor symmetry: 3, max scan energy: 17.61 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
Li      2.16443688   -1.35467533   -0.00864259
S       1.32287116    0.62769299    0.00234900
C      -0.40316381   -0.01924756    0.00088266
C      -1.12724019    0.47505219    1.25338189
C      -0.42084178   -1.55199358   -0.00636865
C      -1.12968548    0.48692240   -1.24544900
H      -1.12395784    1.56502823    1.28693269
H      -0.63205552    0.11506763    2.15723878
H      -2.16812982    0.13159805    1.26548197
H       0.06099877   -1.95944294    0.89298282
H      -1.44170237   -1.94681162   -0.00820000
H       0.06081412   -1.95097535   -0.90964570
H      -0.63657046    0.13508970   -2.15364340
H      -1.12603172    1.57715255   -1.26893504
H      -2.17074730    0.14399217   -1.25855422
""",
)

entry(
    index = 31,
    label = "[Li]SC=C",
    molecule = 
"""
1 S  u0 p2 c0 {2,S} {4,S}
2 C  u0 p0 c0 {1,S} {3,D} {5,S}
3 C  u0 p0 c0 {2,D} {6,S} {7,S}
4 Li u0 p0 c0 {1,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92886,0.00430196,7.78626e-05,-1.62001e-07,1.00569e-10,2500.95,9.08026], Tmin=(10,'K'), Tmax=(543.589,'K')),
            NASAPolynomial(coeffs=[3.65195,0.0220752,-1.46027e-05,4.65231e-09,-5.67332e-13,2298.58,8.10899], Tmin=(543.589,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (20.7683,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'Li-S': 1, 'C-H': 3, 'C=C': 1, 'C-S': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 3]]) broke during the scan.Significant difference observed between consecutive conformersCould not read energies


External symmetry: 1, optical isomers: 2

Geometry:
Li      0.18764375   -1.56410673   -0.58847555
S      -1.13003828    0.04129951    0.10795744
C       0.49181862    0.56039237   -0.20932413
C       1.62663410   -0.04363065    0.21154974
H       0.60396805    1.41189094   -0.87907260
H       2.60169528    0.32167451   -0.08607324
H       1.60359184   -0.80227916    0.99431113
""",
)

entry(
    index = 32,
    label = "[Li]SN",
    molecule = 
"""
1 S  u0 p2 c0 {2,S} {3,S}
2 N  u0 p1 c0 {1,S} {4,S} {5,S}
3 Li u0 p0 c0 {1,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86795,0.0136551,5.49188e-05,-3.78791e-07,6.01432e-10,7665.68,8.66585], Tmin=(10,'K'), Tmax=(247.545,'K')),
            NASAPolynomial(coeffs=[4.86864,0.0106547,-6.70005e-06,2.06665e-09,-2.46446e-13,7575.78,4.42022], Tmin=(247.545,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (63.7445,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'Li-S': 1, 'H-N': 2, 'N-S': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for [Li]SN exists which is 83.29 kJ/mol lower.


External symmetry: 1, optical isomers: 2

Geometry:
Li      1.04076200   -0.38737400   -0.87679900
S       0.45758300   -0.24224900    1.18888400
N      -0.72130000   -0.63280300   -0.18154200
H      -1.27126800   -1.43657500    0.10637700
H      -1.41661900    0.10568800   -0.23413900
""",
)

entry(
    index = 33,
    label = "[Li]SN=C",
    molecule = 
"""
1 S  u0 p2 c0 {2,S} {4,S}
2 N  u0 p1 c0 {1,S} {3,D}
3 C  u0 p0 c0 {2,D} {5,S} {6,S}
4 Li u0 p0 c0 {1,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92621,0.00466929,6.99747e-05,-1.60834e-07,1.08471e-10,8556.62,8.48291], Tmin=(10,'K'), Tmax=(511.693,'K')),
            NASAPolynomial(coeffs=[4.29065,0.0171246,-1.1401e-05,3.63868e-09,-4.43848e-13,8318.97,5.01108], Tmin=(511.693,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (71.1229,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'Li-S': 1, 'C-H': 2, 'N-S': 1, 'C=N': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 3]]) broke during the scan.Significant difference observed between consecutive conformersThe rotor scan has a barrier of 138.52 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 1, optical isomers: 1

Geometry:
Li     -0.76054662   -1.78206555   -0.00025050
S      -0.98177750    0.37562634   -0.00027218
N       0.54999775   -0.41890920    0.00038152
C       1.64484665    0.21711815    0.00005330
H       1.68565157    1.30691733   -0.00057744
H       2.57736986   -0.34316397    0.00046950
""",
)

entry(
    index = 34,
    label = "[Li]OF",
    molecule = 
"""
1 F  u0 p3 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 Li u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97289,0.00151717,2.14505e-05,-4.36551e-08,2.49619e-11,-18961.9,6.11105], Tmin=(10,'K'), Tmax=(622.356,'K')),
            NASAPolynomial(coeffs=[4.37156,0.0056672,-4.73002e-06,1.71945e-09,-2.26496e-13,-19141.5,3.33237], Tmin=(622.356,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-157.67,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'F-O': 1, 'Li-O': 1}

External symmetry: 1, optical isomers: 1

Geometry:
Li     -0.28178101   -1.32304336    0.00000000
O      -0.73597575    0.34414156    0.00000000
F       0.74813147    0.13498904    0.00000000
""",
)

entry(
    index = 35,
    label = "[Li]SF",
    molecule = 
"""
1 S  u0 p2 c0 {2,S} {3,S}
2 F  u0 p3 c0 {1,S}
3 Li u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95384,0.00280435,2.72334e-05,-6.81514e-08,4.56486e-11,-21760.7,7.30813], Tmin=(10,'K'), Tmax=(556.768,'K')),
            NASAPolynomial(coeffs=[5.16776,0.00417422,-3.64379e-06,1.37341e-09,-1.86282e-13,-22052.3,0.757931], Tmin=(556.768,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-180.945,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'Li-S': 1, 'F-S': 1}

External symmetry: 1, optical isomers: 1

Geometry:
Li      0.96605948   -1.35611184    0.00000000
S      -0.72877559    0.00000077    0.00000000
F       0.97609576    0.45192224    0.00000000
""",
)

entry(
    index = 36,
    label = "[Li]CF",
    molecule = 
"""
1 F  u0 p3 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 Li u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96463,0.00205501,4.29664e-05,-8.25515e-08,4.77158e-11,-12858.9,6.14446], Tmin=(10,'K'), Tmax=(574.338,'K')),
            NASAPolynomial(coeffs=[3.45782,0.0138113,-9.2231e-06,2.96729e-09,-3.64951e-13,-12936.4,7.12723], Tmin=(574.338,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-106.93,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 2, 'C-Li': 1, 'C-F': 1}

External symmetry: 1, optical isomers: 1

Geometry:
Li      0.78875895   -1.26230068   -0.00000378
C      -0.81253265   -0.20611869   -0.00000032
F       0.56674405    0.50635509    0.00000123
H      -1.29297042    0.23237741    0.87951583
H      -1.29297777    0.23239105   -0.87950541
""",
)

entry(
    index = 37,
    label = "[Li]NF",
    molecule = 
"""
1 F  u0 p3 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,S} {4,S}
3 Li u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94679,0.00326668,3.8803e-05,-9.18807e-08,6.10458e-11,-1701.95,6.92076], Tmin=(10,'K'), Tmax=(542.866,'K')),
            NASAPolynomial(coeffs=[4.91158,0.00774086,-5.5649e-06,1.90934e-09,-2.46547e-13,-1977.38,1.2836], Tmin=(542.866,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-14.1689,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'F-N': 1, 'Li-N': 1, 'H-N': 1}

External symmetry: 1, optical isomers: 2

Geometry:
Li      0.23915542   -1.37812794   -0.08666808
N      -0.83473293    0.04631866    0.10553332
F       0.69695868    0.33887421    0.00779278
H      -1.14747481    0.75907386   -0.54888403
""",
)

entry(
    index = 38,
    label = "[Li]OCl",
    molecule = 
"""
1 Cl u0 p3 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 Li u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95829,0.00259676,2.61742e-05,-6.63014e-08,4.55758e-11,-14993.4,7.32524], Tmin=(10,'K'), Tmax=(535.706,'K')),
            NASAPolynomial(coeffs=[4.85891,0.00458765,-3.80467e-06,1.37637e-09,-1.80696e-13,-15215,2.37513], Tmin=(535.706,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-124.676,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'Li-O': 1, 'Cl-O': 1}

External symmetry: 1, optical isomers: 1

Geometry:
Li      1.35765610   -1.11799864    0.00000000
O       0.90479866    0.54180390    0.00000000
Cl     -0.66455821   -0.05825920    0.00000000
""",
)

entry(
    index = 39,
    label = "[Li]SCl",
    molecule = 
"""
1 Cl u0 p3 c0 {2,S}
2 S  u0 p2 c0 {1,S} {3,S}
3 Li u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9362,0.0042017,3.17685e-05,-9.58769e-08,7.41529e-11,-8677.42,8.46994], Tmin=(10,'K'), Tmax=(495.637,'K')),
            NASAPolynomial(coeffs=[5.57844,0.00330892,-2.93818e-06,1.12325e-09,-1.54172e-13,-8992.04,0.168209], Tmin=(495.637,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-72.162,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'Li-S': 1, 'Cl-S': 1}

External symmetry: 1, optical isomers: 1

Geometry:
Li     -0.18880380   -1.80425630    0.00000000
S      -1.06494774    0.19788486    0.00000000
Cl      1.03481837    0.13141394    0.00000000
""",
)

entry(
    index = 40,
    label = "[Li]CCl",
    molecule = 
"""
1 Cl u0 p3 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 Li u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94669,0.00326586,4.96105e-05,-1.09345e-07,7.04923e-11,2769.05,7.39322], Tmin=(10,'K'), Tmax=(537.868,'K')),
            NASAPolynomial(coeffs=[4.30521,0.0122857,-8.13399e-06,2.62124e-09,-3.24419e-13,2561.44,4.3145], Tmin=(537.868,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (23.005,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 2, 'C-Cl': 1, 'C-Li': 1}

External symmetry: 1, optical isomers: 1

Geometry:
Li     -0.79606620   -1.60413228    0.00000353
C      -1.17653716    0.30468298   -0.00000047
Cl      0.71209628    0.06430976   -0.00000113
H      -1.33061324    0.93520334    0.87825624
H      -1.33061347    0.93519383   -0.87826379
""",
)

entry(
    index = 41,
    label = "[Li]NCl",
    molecule = 
"""
1 Cl u0 p3 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,S} {4,S}
3 Li u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78011,0.0163735,-2.54291e-05,2.0587e-08,-6.5366e-12,8262.31,7.83001], Tmin=(10,'K'), Tmax=(857.511,'K')),
            NASAPolynomial(coeffs=[5.7345,0.0054805,-3.26705e-06,9.41391e-10,-1.0478e-13,7992.44,-0.917548], Tmin=(857.511,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (68.661,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'Li-N': 1, 'H-N': 1, 'Cl-N': 1}

External symmetry: 1, optical isomers: 1

Geometry:
Li      1.30079309   -1.27714568    0.00001663
N       1.01538898    0.44050103    0.00816985
Cl     -0.70181358   -0.04379631   -0.00045737
H       0.96968632    1.44815314    0.01792993
""",
)

entry(
    index = 42,
    label = "[Li]Cl",
    molecule = 
"""
1 Cl u0 p3 c0 {2,S}
2 Li u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49072,0.000510289,7.22654e-06,-1.44343e-08,8.06337e-12,-24640.6,5.33178], Tmin=(10,'K'), Tmax=(639.248,'K')),
            NASAPolynomial(coeffs=[3.63926,0.00194116,-1.66945e-06,6.19299e-10,-8.2738e-14,-24707.9,4.30445], Tmin=(639.248,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-204.878,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'Cl-Li': 1}

External symmetry: 1, optical isomers: 1

Geometry:
Li      0.00000000    0.00000000    1.72751370
Cl      0.00000000    0.00000000   -0.30505318
""",
)

entry(
    index = 43,
    label = "[Li][H]",
    molecule = 
"""
1 Li u0 p0 c0 {2,S}
2 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.51626,-0.00091266,5.1131e-06,-5.12269e-09,1.6301e-12,15869.3,0.594612], Tmin=(10,'K'), Tmax=(1005.64,'K')),
            NASAPolynomial(coeffs=[3.0417,0.00220199,-1.36295e-06,3.83801e-10,-4.04353e-14,15902.7,2.57825], Tmin=(1005.64,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (131.949,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-Li': 1}

External symmetry: 1, optical isomers: 1

Geometry:
Li      0.00000000    0.00000000    0.40139205
H       0.00000000    0.00000000   -1.20440546
""",
)

entry(
    index = 44,
    label = "[Li]",
    molecule = 
"""
multiplicity 2
1 Li u1 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,1.99051e-15,-1.1909e-17,2.10806e-20,-1.11018e-23,18206.2,2.43319], Tmin=(10,'K'), Tmax=(794.005,'K')),
            NASAPolynomial(coeffs=[2.5,1.52667e-14,-1.58445e-17,6.63089e-21,-9.62112e-25,18206.2,2.43319], Tmin=(794.005,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (151.375,'kJ/mol'),
        Cp0 = (20.7862,'J/(mol*K)'),
        CpInf = (20.7862,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
External symmetry: 1, optical isomers: 1

Geometry:
Li      0.00000000    0.00000000    0.00000000
""",
)

entry(
    index = 45,
    label = "[Li]OC[=O]OCCOC[=O]O[Li]",
    molecule = 
"""
1  O  u0 p2 c0 {7,S} {9,S}
2  O  u0 p2 c0 {8,S} {10,S}
3  O  u0 p2 c0 {9,S} {11,S}
4  O  u0 p2 c0 {10,S} {12,S}
5  O  u0 p2 c0 {9,D}
6  O  u0 p2 c0 {10,D}
7  C  u0 p0 c0 {1,S} {8,S} {13,S} {14,S}
8  C  u0 p0 c0 {2,S} {7,S} {15,S} {16,S}
9  C  u0 p0 c0 {1,S} {3,S} {5,D}
10 C  u0 p0 c0 {2,S} {4,S} {6,D}
11 Li u0 p0 c0 {3,S}
12 Li u0 p0 c0 {4,S}
13 H  u0 p0 c0 {7,S}
14 H  u0 p0 c0 {7,S}
15 H  u0 p0 c0 {8,S}
16 H  u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.02414,0.103814,-0.000292517,6.71916e-07,-6.19555e-10,-169644,15.8603], Tmin=(10,'K'), Tmax=(333.103,'K')),
            NASAPolynomial(coeffs=[4.47088,0.0679554,-4.77992e-05,1.55411e-08,-1.89673e-12,-169638,12.0104], Tmin=(333.103,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-1410.5,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (382.466,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 6, 'C-H': 4, 'C-C': 1, 'C=O': 2, 'Li-O': 2}
1D rotors:
* Invalidated! pivots: [1, 9], dihedral: [7, 1, 9, 3], invalidation reason: 
* Invalidated! pivots: [1, 7], dihedral: [9, 1, 7, 8], invalidation reason: 
* Invalidated! pivots: [2, 8], dihedral: [10, 2, 8, 7], invalidation reason: 
* Invalidated! pivots: [2, 10], dihedral: [8, 2, 10, 4], invalidation reason: 
* Invalidated! pivots: [3, 9], dihedral: [11, 3, 9, 1], invalidation reason: 
* Invalidated! pivots: [4, 10], dihedral: [12, 4, 10, 2], invalidation reason: 
* Invalidated! pivots: [7, 8], dihedral: [1, 7, 8, 2], invalidation reason: 


External symmetry: 2, optical isomers: 2

Geometry:
O       1.37017030    0.02453650   -0.44921343
O      -1.37018702    0.02467348    0.44919853
O       3.22259060    1.20269315   -0.70381243
O      -3.22259963    1.20290691    0.70349751
O       3.23165578   -0.49928758    0.70903761
O      -3.23168837   -0.49946086   -0.70888619
C       0.72356538   -1.06329890    0.20366887
C      -0.72359509   -1.06334590   -0.20339051
C       2.65027770    0.24357038   -0.13174025
C      -2.65029634    0.24362725    0.13167885
Li      4.64415594    0.66290389    0.35000533
Li     -4.64419102    0.66281320   -0.35013117
H       1.18960780   -2.00439462   -0.09952669
H       0.82400598   -0.96477922    1.28550026
H      -0.82403405   -0.96511718   -1.28524856
H      -1.18964718   -2.00435397    0.10006128
""",
)

entry(
    index = 46,
    label = "COC[C]=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  O u0 p2 c0 {1,S} {2,S}
4  C u1 p0 c0 {1,S} {10,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.58917,0.0393521,-7.71792e-05,1.31457e-07,-9.06867e-11,-18151.1,11.9913], Tmin=(10,'K'), Tmax=(463.323,'K')),
            NASAPolynomial(coeffs=[3.70315,0.0296502,-1.7546e-05,5.04086e-09,-5.62375e-13,-18068.1,12.5389], Tmin=(463.323,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-150.931,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (220.334,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'C-O': 2, 'C-H': 5, 'C-C': 1}
1D rotors:
pivots: [1, 2], dihedral: [6, 1, 2, 3], rotor symmetry: 3, max scan energy: 7.69 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 22.33 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 16.94 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       1.52454918   -0.70315970   -0.20576432
O       0.96687208    0.37619807    0.51318571
C      -0.07387347    1.02104926   -0.14295523
C      -1.39447419    0.25414823   -0.21448360
O      -1.62233903   -0.83983060    0.14505765
H       1.87287564   -0.37682919   -1.19368537
H       0.80629766   -1.51900371   -0.32753683
H       2.37561449   -1.06064712    0.37056812
H      -0.28712589    1.94920257    0.39010203
H       0.17739724    1.28353065   -1.18093063
""",
)

entry(
    index = 47,
    label = "COOC",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {4,S}
3  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
4  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74164,0.0247839,-2.796e-05,6.14152e-08,-5.18572e-11,-16671.9,8.82895], Tmin=(10,'K'), Tmax=(481.425,'K')),
            NASAPolynomial(coeffs=[1.77638,0.0313032,-1.77094e-05,4.89692e-09,-5.29443e-13,-16369,18.0542], Tmin=(481.425,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-138.626,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (224.491,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'O-O': 1, 'C-H': 6, 'C-O': 2}
1D rotors:
pivots: [1, 2], dihedral: [5, 1, 2, 3], rotor symmetry: 3, max scan energy: 11.61 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for COOC exists which is 2.80 kJ/mol lower.Another conformer for COOC exists which is 2.80 kJ/mol lower. But unable to propose troubleshooting methods.
pivots: [3, 4], dihedral: [2, 3, 4, 8], rotor symmetry: 3, max scan energy: 11.61 kJ/mol


External symmetry: 2, optical isomers: 2

Geometry:
C      -1.59209117    0.30222051    0.11266043
O      -0.53186277   -0.41575504   -0.47222367
O       0.53214351   -0.41445506    0.47381881
C       1.59218194    0.30207013   -0.11317734
H      -1.31556668    1.34419893    0.30311311
H      -2.39808533    0.26654816   -0.62117039
H      -1.92098953   -0.16808241    1.04301696
H       1.31560137    1.34362128   -0.30588707
H       1.92049745   -0.17038552   -1.04264632
H       2.39852656    0.26798682    0.62032549
""",
)

entry(
    index = 48,
    label = "CC=NN=C=C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,D} {10,S}
3  C u0 p0 c0 {5,D} {11,S} {12,S}
4  N u0 p1 c0 {2,D} {6,S}
5  C u0 p0 c0 {3,D} {6,D}
6  N u0 p1 c0 {4,S} {5,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94457,0.00784253,0.000529295,-3.9487e-06,1.00457e-08,39143.9,7.6517], Tmin=(10,'K'), Tmax=(121.276,'K')),
            NASAPolynomial(coeffs=[3.40906,0.0390093,-2.32193e-05,6.68639e-09,-7.46157e-13,39146.9,8.69601], Tmin=(121.276,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (330.207,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'N-N': 1, 'C=C': 1, 'C=N': 2, 'C-H': 6, 'C-C': 1}
1D rotors:
pivots: [1, 2], dihedral: [7, 1, 2, 3], rotor symmetry: 3, max scan energy: 6.86 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 38.71 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       2.83326000   -0.35873388    0.00231359
C       1.53723237    0.36875040    0.00750499
N       0.43932621   -0.26499658    0.00317261
N      -0.66469691    0.61797193    0.00968460
C      -1.77653920    0.10501364    0.00642305
C      -3.00202346   -0.33121514    0.00372653
H       3.42114023   -0.07433115   -0.87380901
H       2.66843379   -1.43456147   -0.00589485
H       3.42068452   -0.08767453    0.88296867
H       1.53794801    1.46116858    0.01520770
H      -3.51353241   -0.51253660   -0.93136338
H      -3.51288964   -0.52605713    0.93644405
""",
)

entry(
    index = 49,
    label = "[Li]C[=[N]]C",
    molecule = 
"""
multiplicity 2
1 C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C  u0 p0 c0 {1,S} {6,D} {7,S}
3 H  u0 p0 c0 {1,S}
4 H  u0 p0 c0 {1,S}
5 H  u0 p0 c0 {1,S}
6 N  u1 p1 c0 {2,D}
7 Li u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79848,0.0195546,-2.5499e-05,4.66577e-08,-3.74607e-11,22151.5,8.57555], Tmin=(10,'K'), Tmax=(447.335,'K')),
            NASAPolynomial(coeffs=[3.20837,0.020194,-1.20936e-05,3.50603e-09,-3.93814e-13,22250.7,11.4664], Tmin=(447.335,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (184.171,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (153.818,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-Li': 1, 'C=N': 1, 'C-H': 3, 'C-C': 1}
1D rotors:
pivots: [2, 4], dihedral: [1, 2, 4, 5], rotor symmetry: 3, max scan energy: 2.39 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 3 1 2 4 F


External symmetry: 1, optical isomers: 1

Geometry:
Li      1.96568996    0.94202967    0.00000943
C       0.11316808    0.17495837    0.00000359
N       1.00811240   -0.64923136   -0.00001912
C      -1.38930925    0.07841579    0.00000052
H      -1.79253160    0.58353246   -0.87866633
H      -1.71387385   -0.96619628   -0.00010567
H      -1.79251501    0.58334495    0.87878357
""",
)

entry(
    index = 50,
    label = "[Li]N=C[C[=N[Li]]C]C",
    molecule = 
"""
1  N  u0 p1 c0 {5,D} {7,S}
2  N  u0 p1 c0 {6,D} {8,S}
3  C  u0 p0 c0 {6,S} {9,S} {10,S} {11,S}
4  C  u0 p0 c0 {5,S} {12,S} {13,S} {14,S}
5  C  u0 p0 c0 {1,D} {4,S} {6,S}
6  C  u0 p0 c0 {2,D} {3,S} {5,S}
7  Li u0 p0 c0 {1,S}
8  Li u0 p0 c0 {2,S}
9  H  u0 p0 c0 {3,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {3,S}
12 H  u0 p0 c0 {4,S}
13 H  u0 p0 c0 {4,S}
14 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61411,0.0448151,0.000329152,-2.40442e-06,4.65119e-09,19630.3,11.7343], Tmin=(10,'K'), Tmax=(192.34,'K')),
            NASAPolynomial(coeffs=[5.53764,0.047917,-3.11988e-05,9.74711e-09,-1.16596e-12,19476.5,3.55261], Tmin=(192.34,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (163.615,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (324.264,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'Li-N': 2, 'C=N': 2, 'C-H': 6, 'C-C': 3}
1D rotors:
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Bond ([[2, 6]]) broke during the scan.Bond ([[2, 6]]) broke during the scan. But unable to propose troubleshooting methods.
pivots: [3, 8], dihedral: [2, 3, 8, 12], rotor symmetry: 3, max scan energy: 6.54 kJ/mol
pivots: [4, 7], dihedral: [3, 4, 7, 9], rotor symmetry: 3, max scan energy: 6.99 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
Li      3.35625317    0.25955942    0.00252948
N       1.59389128    0.51766937    0.00061826
C       0.55173688   -0.21054690   -0.00001378
C      -0.90105501    0.38205921   -0.00029014
N      -1.11442738    1.61680660   -0.00130639
Li      0.63354323    2.23782359   -0.00078634
C      -2.03134944   -0.65700367    0.00089531
C       0.65123878   -1.73320859   -0.00093392
H      -2.00472939   -1.30626604    0.88264473
H      -2.00452419   -1.30883504   -0.87893773
H      -2.97290980   -0.11096520    0.00003468
H       0.15749556   -2.16280143    0.87422009
H       0.15915749   -2.16139026   -0.87773168
H       1.69817150   -2.04709017   -0.00024671
""",
)

entry(
    index = 51,
    label = "O=C1OC[F]C[C2OC[=O]OC2F]O1",
    molecule = 
"""
1  F u0 p3 c0 {11,S}
2  F u0 p3 c0 {12,S}
3  O u0 p2 c0 {10,S} {14,S}
4  O u0 p2 c0 {9,S} {13,S}
5  O u0 p2 c0 {11,S} {13,S}
6  O u0 p2 c0 {12,S} {14,S}
7  O u0 p2 c0 {13,D}
8  O u0 p2 c0 {14,D}
9  C u0 p0 c0 {4,S} {10,S} {11,S} {15,S}
10 C u0 p0 c0 {3,S} {9,S} {12,S} {16,S}
11 C u0 p0 c0 {1,S} {5,S} {9,S} {17,S}
12 C u0 p0 c0 {2,S} {6,S} {10,S} {18,S}
13 C u0 p0 c0 {4,S} {5,S} {7,D}
14 C u0 p0 c0 {3,S} {6,S} {8,D}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {10,S}
17 H u0 p0 c0 {11,S}
18 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.59266,0.0630034,7.9642e-06,-6.06764e-08,2.90658e-11,-176238,15.7533], Tmin=(10,'K'), Tmax=(918.212,'K')),
            NASAPolynomial(coeffs=[13.6715,0.0533287,-3.21522e-05,9.05153e-09,-9.73366e-13,-179532,-39.869], Tmin=(918.212,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-1465.23,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (428.195,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 8, 'C-H': 4, 'C=O': 2, 'C-C': 3, 'C-F': 2}
1D rotors:
pivots: [6, 7], dihedral: [4, 6, 7, 8], rotor symmetry: 1, max scan energy: 47.92 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       3.47782632   -1.47126749    0.01248048
C       2.59633230   -0.69203753   -0.00534763
O       2.55022507    0.45907404    0.72086415
C       1.46571760    1.23793555    0.32825502
F       1.89598771    2.21604152   -0.51560207
C       0.57345732    0.24944153   -0.42165969
C      -0.57480248   -0.28314943    0.42587990
O      -1.44268235    0.78832938    0.75093152
C      -2.57427949    0.70548143    0.00961398
O      -3.43708527    1.50531053   -0.00852628
O      -2.54691434   -0.43795888   -0.73061533
C      -1.48542869   -1.24637234   -0.33401195
F      -1.94656991   -2.21706013    0.50210748
O       1.45783819   -0.81218932   -0.73167709
H       1.01591428    1.71070959    1.20008047
H       0.20326334    0.69496063   -1.34672860
H      -0.20758872   -0.74458360    1.34400398
H      -1.04209052   -1.72647225   -1.20530797
""",
)

entry(
    index = 52,
    label = "[Li]OC[C][OC]OC",
    molecule = 
"""
1  O  u0 p2 c0 {4,S} {6,S}
2  O  u0 p2 c0 {4,S} {7,S}
3  O  u0 p2 c0 {4,S} {8,S}
4  C  u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5  C  u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
6  C  u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
7  C  u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
8  Li u0 p0 c0 {3,S}
9  H  u0 p0 c0 {5,S}
10 H  u0 p0 c0 {5,S}
11 H  u0 p0 c0 {5,S}
12 H  u0 p0 c0 {6,S}
13 H  u0 p0 c0 {6,S}
14 H  u0 p0 c0 {6,S}
15 H  u0 p0 c0 {7,S}
16 H  u0 p0 c0 {7,S}
17 H  u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.44905,0.0604563,-3.61679e-05,1.03733e-08,-1.12735e-12,-82209.2,12.3636], Tmin=(10,'K'), Tmax=(1690.05,'K')),
            NASAPolynomial(coeffs=[21.1052,0.0240563,-8.6438e-06,1.40255e-09,-7.94197e-14,-88946.7,-84.3593], Tmin=(1690.05,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-683.601,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (407.409,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 5, 'C-H': 9, 'Li-O': 1, 'C-C': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason:
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 9], invalidation reason:
* Invalidated! pivots: [3, 5], dihedral: [2, 3, 5, 6], invalidation reason: Another conformer for [Li]OC[C][OC]OC exists which is 6.57 kJ/mol lower.
* Invalidated! pivots: [3, 7], dihedral: [2, 3, 7, 8], invalidation reason:
* Invalidated! pivots: [5, 6], dihedral: [3, 5, 6, 12], invalidation reason:
* Invalidated! pivots: [7, 8], dihedral: [3, 7, 8, 15], invalidation reason:


External symmetry: 1, optical isomers: 2

Geometry:
Li      0.40156800   -1.87080400    1.00286800
O      -0.82913100   -1.53970700   -0.23768700
C      -0.28883000   -0.38286800   -0.55196400
C       0.19937000   -0.32841500   -2.00068700
O      -1.10856900    0.77919100   -0.42352600
C      -1.86947100    0.86182200    0.77321800
O       0.88772600   -0.20298800    0.37557800
C       1.66221600    0.98815600    0.31836500
H      -0.65320500   -0.54047100   -2.64651500
H       0.60309700    0.65026400   -2.26856700
H       0.95963700   -1.09593700   -2.15924100
H      -2.49890200   -0.02207500    0.90129700
H      -1.22728500    0.97710000    1.65729400
H      -2.49308900    1.75148300    0.67525500
H       1.00886800    1.86210400    0.26201300
H       2.33547000    0.98368700   -0.54581100
H       2.26032900    1.04116100    1.23084300
""",
)

entry(
    index = 53,
    label = "CCOCOC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {5,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {6,S} {14,S} {15,S} {16,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {3,S} {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.42389,0.0501061,-4.2517e-05,4.75336e-08,-2.96342e-11,-49190.7,11.6323], Tmin=(10,'K'), Tmax=(554.594,'K')),
            NASAPolynomial(coeffs=[1.92026,0.0533454,-3.07074e-05,8.60971e-09,-9.41279e-13,-48907,19.0545], Tmin=(554.594,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-409.037,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (365.837,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 4, 'C-H': 10, 'C-C': 1}
1D rotors:
pivots: [1, 2], dihedral: [7, 1, 2, 3], rotor symmetry: 3, max scan energy: 12.52 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 22.47 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 37.86 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 2 3 4 13 F
pivots: [5, 6], dihedral: [4, 5, 6, 14], rotor symmetry: 3, max scan energy: 6.52 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -2.58109122   -0.52464820    0.09677029
C      -1.33439451    0.09980652   -0.48330070
O      -0.44061397    0.38375414    0.57960362
C       0.74534084    0.98959267    0.17334095
O       1.57735668    0.15544702   -0.57221781
C       2.09143405   -0.93097311    0.16591329
H      -3.05557124    0.15178937    0.80894065
H      -2.33776717   -1.45278309    0.61597157
H      -3.29613630   -0.75065533   -0.69608600
H      -1.57475976    1.03215619   -1.01330904
H      -0.85805032   -0.57452354   -1.20317506
H       0.54417297    1.85267348   -0.47210653
H       1.24204052    1.31078470    1.09679732
H       1.29692944   -1.60604690    0.49685895
H       2.64373154   -0.58030747    1.04674250
H       2.77206062   -1.47106564   -0.49011292
""",
)

entry(
    index = 54,
    label = "[Li]C[C]O",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C  u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 O  u0 p2 c0 {1,S} {9,S}
4 Li u0 p0 c0 {1,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {2,S}
8 H  u0 p0 c0 {2,S}
9 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89546,0.00713784,0.000114827,-2.83821e-07,2.1144e-10,-11954.9,8.73078], Tmin=(10,'K'), Tmax=(451.784,'K')),
            NASAPolynomial(coeffs=[3.74015,0.0277244,-1.73084e-05,5.28623e-09,-6.25026e-13,-12136.9,7.1868], Tmin=(451.784,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-99.4109,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (203.705,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C-Li': 1, 'C-O': 1, 'C-H': 4, 'C-C': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 6], rotor symmetry: 3, max scan energy: 14.94 kJ/mol
* Invalidated! pivots: [2, 4], dihedral: [1, 2, 4, 9], invalidation reason: Bond ([[1, 4]]) broke during the scan.The rotor scan has a barrier of 118.42 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 1, optical isomers: 2

Geometry:
Li      1.51130316    1.13974463   -0.47627180
C      -0.04710135    0.40942993    0.42232421
C      -1.35770766   -0.02307017   -0.19373844
O       1.04420800   -0.52302945   -0.05396273
H      -0.09946961    0.27058895    1.50887369
H      -1.36611369    0.08223697   -1.28359894
H      -1.63734773   -1.06785396    0.03303722
H      -2.16122966    0.60950544    0.19376770
H       0.80638236   -1.44815506    0.03473798
""",
)

entry(
    index = 55,
    label = "[CH2]OCOCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {5,S} {6,S} {12,S} {13,S}
4  C u1 p0 c0 {6,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {3,S} {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.27876,0.0577743,-5.13329e-05,2.8584e-08,-7.39031e-12,-26492.2,12.8536], Tmin=(10,'K'), Tmax=(816.594,'K')),
            NASAPolynomial(coeffs=[6.23374,0.0432997,-2.47445e-05,6.87732e-09,-7.44817e-13,-26974.8,-0.803774], Tmin=(816.594,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-220.364,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (336.736,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 4, 'C-H': 9, 'C-C': 1}
1D rotors:
pivots: [1, 2], dihedral: [7, 1, 2, 3], rotor symmetry: 1, max scan energy: 24.61 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 8 7 1 2 F
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 45.53 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 3 4 5 6 F
D 2 3 4 5 F
D 8 1 2 3 F
D 2 1 7 8 F
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 39.94 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 2 1 7 8 F
D 8 1 2 3 F
D 1 2 3 9 F
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 22.10 kJ/mol
pivots: [5, 6], dihedral: [4, 5, 6, 13], rotor symmetry: 3, max scan energy: 12.48 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       2.12232960   -0.94876508    0.20798124
O       1.64605535    0.08656019   -0.52264499
C       0.79395551    0.97309701    0.17304599
O      -0.39427676    0.39017416    0.57269748
C      -1.26272251    0.04487270   -0.49679558
C      -2.55007475   -0.48287244    0.08896946
H       2.72974500   -1.63822443   -0.35865071
H       1.57208564   -1.25616344    1.08893500
H       0.62340261    1.79948597   -0.52513706
H       1.28742407    1.32573226    1.08233450
H      -1.44760683    0.93552464   -1.11272396
H      -0.78559217   -0.70675544   -1.13425150
H      -3.02380471    0.27016640    0.72004535
H      -3.24439202   -0.75354575   -0.70813356
H      -2.35944392   -1.36895354    0.69578330
""",
)

entry(
    index = 56,
    label = "COCC[C]O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {2,S} {4,S}
6  O u0 p2 c0 {1,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.66005,0.0287875,0.000116604,-2.93079e-07,2.07059e-10,-52366.1,11.3802], Tmin=(10,'K'), Tmax=(466.726,'K')),
            NASAPolynomial(coeffs=[2.36332,0.0583107,-3.74465e-05,1.14796e-08,-1.34583e-12,-52445.5,14.5], Tmin=(466.726,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-435.425,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (361.68,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C-O': 3, 'C-H': 9, 'C-C': 2}
1D rotors:
pivots: [1, 2], dihedral: [7, 1, 2, 3], rotor symmetry: 3, max scan energy: 9.41 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 42.07 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 33.25 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 5 4 6 16 F
pivots: [4, 5], dihedral: [3, 4, 5, 13], rotor symmetry: 3, max scan energy: 11.12 kJ/mol
pivots: [4, 6], dihedral: [3, 4, 6, 16], rotor symmetry: 1, max scan energy: 21.92 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -2.59443359    0.16065639    0.13539244
O      -1.33369942   -0.25868479   -0.31607516
C      -0.28606859    0.58874772    0.09370692
C       1.01905194   -0.04852635   -0.34262897
C       2.21937992    0.76357842    0.09231822
O       1.13891886   -1.34033613    0.22038258
H      -2.85218650    1.15103971   -0.26104764
H      -3.32819158   -0.56304379   -0.21686792
H      -2.63228078    0.20339742    1.23146021
H      -0.39659897    1.58539151   -0.35734149
H      -0.29410827    0.69953341    1.18833287
H       1.00365363   -0.12419908   -1.43967755
H       2.24345563    0.85557057    1.18004967
H       2.19509208    1.76269308   -0.34685678
H       3.13701039    0.26975696   -0.22695963
H       0.30450855   -1.79146657    0.06270154
""",
)

entry(
    index = 57,
    label = "[Li]OCCO[Li]",
    molecule = 
"""
1  O  u0 p2 c0 {3,S} {5,S}
2  O  u0 p2 c0 {4,S} {6,S}
3  C  u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
4  C  u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
5  Li u0 p0 c0 {1,S}
6  Li u0 p0 c0 {2,S}
7  H  u0 p0 c0 {3,S}
8  H  u0 p0 c0 {3,S}
9  H  u0 p0 c0 {4,S}
10 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8847,0.00728096,0.000134221,-2.92948e-07,1.92445e-10,-60341.9,9.08324], Tmin=(10,'K'), Tmax=(507.154,'K')),
            NASAPolynomial(coeffs=[3.02449,0.0375956,-2.5034e-05,7.88099e-09,-9.4412e-13,-60557.2,9.66589], Tmin=(507.154,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-501.744,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C-H': 4, 'Li-O': 2, 'C-C': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[2, 6]]) broke during the scan.The rotor scan has a barrier of 157.39 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Bond ([[1, 2]]) broke during the scan.
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: Bond ([[1, 5]]) broke during the scan.The rotor scan has a barrier of 157.40 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 2, optical isomers: 2

Geometry:
Li     -0.14000369   -1.06710018    1.18366549
O       1.28319987   -0.50048631    0.16608895
C       0.76944314    0.76558840   -0.13420248
C      -0.76871516    0.76664991    0.13409197
O      -1.28416129   -0.49866931   -0.16613453
Li      0.13854606   -1.06735312   -1.18355557
H       0.93617959    1.02792696   -1.20450597
H       1.25963996    1.57288947    0.42925020
H      -0.93504382    1.02922488    1.20440705
H      -1.25748487    1.57484231   -0.42933755
""",
)

entry(
    index = 58,
    label = "[Li]COCCOC",
    molecule = 
"""
1  O  u0 p2 c0 {3,S} {5,S}
2  O  u0 p2 c0 {4,S} {6,S}
3  C  u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
4  C  u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
5  C  u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
6  C  u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
7  Li u0 p0 c0 {5,S}
8  H  u0 p0 c0 {3,S}
9  H  u0 p0 c0 {3,S}
10 H  u0 p0 c0 {4,S}
11 H  u0 p0 c0 {4,S}
12 H  u0 p0 c0 {5,S}
13 H  u0 p0 c0 {5,S}
14 H  u0 p0 c0 {6,S}
15 H  u0 p0 c0 {6,S}
16 H  u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83804,0.0136183,0.000233139,-7.27969e-07,7.72618e-10,-31325.3,11.2527], Tmin=(10,'K'), Tmax=(237.684,'K')),
            NASAPolynomial(coeffs=[1.37064,0.0551451,-2.89495e-05,7.19777e-09,-6.94022e-13,-31208.1,19.6111], Tmin=(237.684,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-260.461,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (369.994,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-Li': 1, 'C-O': 4, 'C-H': 9, 'C-C': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformers
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Bond ([[1, 3]]) broke during the scan.Significant difference observed between consecutive conformersCould not read energies
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 74.97 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 1 2 9 F
A 1 2 8 F
A 1 3 4 F
D 2 3 4 10 F
D 9 2 3 4 F
B 1 3 F
pivots: [5, 6], dihedral: [4, 5, 6, 7], rotor symmetry: 1, max scan energy: 4515.84 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 6 7 16 F
A 15 7 16 F
B 7 15 F
A 14 7 16 F
B 7 14 F
B 5 6 F
B 3 4 F
B 6 7 F
A 14 7 15 F
A 6 7 15 F
A 2 3 4 F
A 4 5 13 F
D 6 7 15 14 F
B 2 3 F
B 4 5 F
A 5 6 7 F
B 1 2 F
A 3 4 5 F
A 5 4 10 F
B 1 3 F
A 3 4 10 F
A 6 5 13 F
D 4 5 13 6 F
D 5 6 7 15 F
A 1 3 4 F
D 2 3 4 10 F
D 10 4 5 13 F
D 9 2 3 4 F
pivots: [6, 7], dihedral: [5, 6, 7, 14], rotor symmetry: 3, max scan energy: 9.38 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
Li     -0.34659823   -1.42460382    0.67336391
C      -1.81541368   -1.01310313   -0.54804457
O      -1.57828024    0.00350826    0.55019529
C      -0.87176191    1.14033664    0.16271407
C       0.48889613    0.82647074   -0.44718601
O       1.15096391   -0.12658047    0.38490683
C       2.44205489   -0.44839447   -0.08687598
H      -2.84943902   -1.32589291   -0.37316816
H      -1.82315621   -0.46243857   -1.49906233
H      -1.43752052    1.73261938   -0.57196049
H      -0.73403769    1.75051969    1.06049919
H       0.38469680    0.40341199   -1.45143645
H       1.08972408    1.74194308   -0.50754685
H       3.07576520    0.44388392   -0.11483312
H       2.39629856   -0.88628048   -1.09036266
H       2.87939124   -1.16997625    0.60225699
""",
)

entry(
    index = 59,
    label = "CCCOC",
    molecule = 
"""
1  O u0 p2 c0 {3,S} {5,S}
2  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
5  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.55752,0.0332069,1.4585e-05,-4.51385e-08,2.46957e-11,-31251.3,11.8278], Tmin=(10,'K'), Tmax=(507.68,'K')),
            NASAPolynomial(coeffs=[1.87526,0.0464614,-2.45766e-05,6.28679e-09,-6.27816e-13,-31080.5,18.8034], Tmin=(507.68,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-259.923,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (340.893,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C-H': 10, 'C-C': 2}
1D rotors:
pivots: [1, 2], dihedral: [6, 1, 2, 3], rotor symmetry: 3, max scan energy: 11.28 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 20.66 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 34.29 kJ/mol
pivots: [4, 5], dihedral: [3, 4, 5, 13], rotor symmetry: 3, max scan energy: 9.90 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       1.98613168   -0.71790760    0.13641368
C       1.32001914    0.59999581   -0.23523046
C      -0.10779466    0.70619665    0.25935353
O      -0.88820381   -0.28932273   -0.35734630
C      -2.22309146   -0.27301279    0.06614598
H       1.43726098   -1.56117713   -0.28361995
H       2.02029880   -0.84765067    1.22134830
H       3.01084855   -0.76006977   -0.23673234
H       1.88392735    1.44000744    0.18127579
H       1.31979164    0.72817903   -1.32137414
H      -0.14266547    0.58307785    1.35398237
H      -0.51966538    1.70026604    0.02887179
H      -2.70866662    0.68409883   -0.16859641
H      -2.30508082   -0.44516389    1.14800308
H      -2.74601647   -1.07183224   -0.45850366
""",
)

entry(
    index = 60,
    label = "[Li]OC[=O]O[C]1OCCO1",
    molecule = 
"""
multiplicity 2
1  O  u0 p2 c0 {6,S} {8,S}
2  O  u0 p2 c0 {7,S} {8,S}
3  O  u0 p2 c0 {8,S} {9,S}
4  O  u0 p2 c0 {9,S} {10,S}
5  O  u0 p2 c0 {9,D}
6  C  u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
7  C  u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
8  C  u1 p0 c0 {1,S} {2,S} {3,S}
9  C  u0 p0 c0 {3,S} {4,S} {5,D}
10 Li u0 p0 c0 {4,S}
11 H  u0 p0 c0 {6,S}
12 H  u0 p0 c0 {6,S}
13 H  u0 p0 c0 {7,S}
14 H  u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98617,0.0463919,-9.02618e-06,-1.58602e-08,7.20298e-12,-98528.1,13.9472], Tmin=(10,'K'), Tmax=(1192.97,'K')),
            NASAPolynomial(coeffs=[17.7219,0.0244556,-1.17712e-05,2.6214e-09,-2.21646e-13,-103522,-61.9368], Tmin=(1192.97,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-819.062,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (324.264,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 7, 'C-H': 4, 'C=O': 1, 'Li-O': 1, 'C-C': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 4]]) broke during the scan.Bond ([[1, 2]]) broke during the scan.Significant difference observed between consecutive conformersThe rotor scan has a barrier of 262.29 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
pivots: [3, 5], dihedral: [2, 3, 5, 6], rotor symmetry: 2, max scan energy: 27.61 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 3 5 6 10 F
pivots: [5, 6], dihedral: [3, 5, 6, 7], rotor symmetry: 1, max scan energy: 27.69 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 4 3 5 6 F
D 7 6 10 9 F


External symmetry: 1, optical isomers: 2

Geometry:
Li      3.73193492   -0.70189651   -0.28962567
O       2.81138998    0.67305543    0.56738257
C       1.83166020    0.10979154    0.03245337
O       1.91899203   -0.91018992   -0.69047942
O       0.61971782    0.67510776    0.28076075
C      -0.48055351    0.07937267   -0.27573721
O      -1.01090062   -0.91275036    0.50302846
C      -2.40700439   -0.91808423    0.24951052
C      -2.68562384    0.54553546   -0.06072371
O      -1.44220593    0.99510865   -0.59330774
H      -2.91798297   -1.28701262    1.13686926
H      -2.63073164   -1.56703504   -0.60270047
H      -3.46694898    0.69546989   -0.80473912
H      -2.91941690    1.12097629    0.83925110
""",
)

entry(
    index = 61,
    label = "O=C1OOC2[OCCO2]O1",
    molecule = 
"""
1  O u0 p2 c0 {7,S} {8,S}
2  O u0 p2 c0 {7,S} {9,S}
3  O u0 p2 c0 {7,S} {10,S}
4  O u0 p2 c0 {5,S} {7,S}
5  O u0 p2 c0 {4,S} {10,S}
6  O u0 p2 c0 {10,D}
7  C u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
8  C u0 p0 c0 {1,S} {9,S} {11,S} {12,S}
9  C u0 p0 c0 {2,S} {8,S} {13,S} {14,S}
10 C u0 p0 c0 {3,S} {5,S} {6,D}
11 H u0 p0 c0 {8,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {9,S}
14 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85485,0.00926513,0.000201455,-4.28829e-07,2.79706e-10,-92307.6,14.6181], Tmin=(10,'K'), Tmax=(493.839,'K')),
            NASAPolynomial(coeffs=[0.80806,0.0616493,-4.18125e-05,1.3179e-08,-1.5665e-12,-92344.5,23.7469], Tmin=(493.839,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-767.527,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 8, 'C-H': 4, 'C-C': 1, 'C=O': 1, 'O-O': 1}

External symmetry: 1, optical isomers: 2

Geometry:
O       2.98923529   -0.75457484   -0.24839323
C       1.93186898   -0.26962556   -0.05630556
O       1.71955012    1.06791545    0.05352537
O       0.37534490    1.23989889    0.46213028
C      -0.28023135    0.03412812    0.12322025
O      -1.19063909   -0.21457284    1.09961039
C      -2.45174476   -0.49646246    0.49058371
C      -2.31084468    0.19236868   -0.85393297
O      -0.91281777    0.06678846   -1.09284841
O       0.75596266   -0.90587363    0.06857320
H      -2.57528471   -1.57723943    0.39233718
H      -3.23462876   -0.08527559    1.12369866
H      -2.84213474   -0.29995248   -1.66512639
H      -2.59010415    1.24832368   -0.80888572
""",
)

entry(
    index = 62,
    label = "[Li]CCO[Li]",
    molecule = 
"""
1 O  u0 p2 c0 {2,S} {5,S}
2 C  u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 C  u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4 Li u0 p0 c0 {3,S}
5 Li u0 p0 c0 {1,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {2,S}
8 H  u0 p0 c0 {3,S}
9 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87148,0.00868139,0.000126951,-3.14882e-07,2.31672e-10,-16816.7,9.86214], Tmin=(10,'K'), Tmax=(463.26,'K')),
            NASAPolynomial(coeffs=[4.05042,0.0306313,-2.01958e-05,6.35153e-09,-7.6242e-13,-17085.3,6.41548], Tmin=(463.26,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-139.841,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-Li': 1, 'C-O': 1, 'C-H': 4, 'Li-O': 1, 'C-C': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[2, 5]]) broke during the scan.Bond ([[4, 5]]) broke during the scan.Bond ([[1, 4]]) broke during the scan.Bond ([[1, 5]]) broke during the scan.Bond ([[1, 2]]) broke during the scan.Bond ([[3, 4]]) broke during the scan.Bond ([[3, 8]]) broke during the scan.Significant difference observed between consecutive conformersCould not read energies
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Bond ([[1, 2]]) broke during the scan.Bond ([[1, 4]]) broke during the scan.Significant difference observed between consecutive conformersThe rotor scan has a barrier of 106.92 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 1, optical isomers: 2

Geometry:
Li     -0.29966404   -0.83846790    1.31145367
C       1.22568874   -0.22397863    0.02314644
C       0.02292532    0.75701017   -0.06702215
O      -1.19815536   -0.00420531   -0.01140703
Li     -0.28689020   -1.10830485   -1.09985378
H       1.91490311    0.02348935    0.83616298
H       1.84988861   -0.20364144   -0.87786322
H       0.04471997    1.36220611   -0.98703805
H       0.04387112    1.49620902    0.75103210
""",
)

entry(
    index = 63,
    label = "[Li]O[C]1OOC[=O]O1",
    molecule = 
"""
multiplicity 2
1 O  u0 p2 c0 {6,S} {7,S}
2 O  u0 p2 c0 {3,S} {6,S}
3 O  u0 p2 c0 {2,S} {7,S}
4 O  u0 p2 c0 {6,S} {8,S}
5 O  u0 p2 c0 {7,D}
6 C  u1 p0 c0 {1,S} {2,S} {4,S}
7 C  u0 p0 c0 {1,S} {3,S} {5,D}
8 Li u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81289,0.0366147,-2.98135e-05,1.06722e-08,-1.30883e-12,-63761.8,13.6004], Tmin=(10,'K'), Tmax=(1302.22,'K')),
            NASAPolynomial(coeffs=[14.4019,0.00956632,-4.96659e-06,1.18206e-09,-1.0704e-13,-66984,-42.065], Tmin=(1302.22,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-530.104,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 5, 'C=O': 1, 'Li-O': 1, 'O-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for [Li]O[C]1OOC[=O]O1 exists which is 0.01 kJ/mol lower.Another conformer for [Li]O[C]1OOC[=O]O1 exists which is 0.01 kJ/mol lower. But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
Li     -3.55242229    0.70405919    0.53594302
O      -2.07605577    0.22136256   -0.01371023
C      -0.90868553   -0.03589728   -0.43290422
O      -0.36975461   -1.26499098    0.03377812
O       1.03491149   -1.07835421    0.02671037
C       1.26287238    0.26419115    0.03871871
O       2.34726073    0.72720996    0.16649052
O       0.11445811    0.91282922   -0.12271464
""",
)

entry(
    index = 64,
    label = "[Li]C[O]",
    molecule = 
"""
multiplicity 2
1 O  u1 p2 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 Li u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96451,0.00237638,4.82825e-05,-1.11068e-07,7.88137e-11,-7563.37,6.7604], Tmin=(10,'K'), Tmax=(458.381,'K')),
            NASAPolynomial(coeffs=[3.50787,0.0129832,-8.09712e-06,2.44716e-09,-2.86035e-13,-7591.08,7.84837], Tmin=(458.381,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-62.8908,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 2, 'C-Li': 1, 'C-O': 1}

External symmetry: 1, optical isomers: 1

Geometry:
Li      1.32823772    0.84329808    0.00003266
C      -0.70613872    0.21428627    0.00000065
O       0.35097480   -0.56139120   -0.00001695
H      -1.27698487    0.34388871   -0.92758076
H      -1.27702849    0.34378938    0.92756868
""",
)

entry(
    index = 65,
    label = "[Li]OCO[Li]",
    molecule = 
"""
1 O  u0 p2 c0 {3,S} {4,S}
2 O  u0 p2 c0 {3,S} {5,S}
3 C  u0 p0 c0 {1,S} {2,S} {6,S} {7,S}
4 Li u0 p0 c0 {1,S}
5 Li u0 p0 c0 {2,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90624,0.00594272,9.20536e-05,-2.09734e-07,1.4065e-10,-55230.4,7.47724], Tmin=(10,'K'), Tmax=(509.965,'K')),
            NASAPolynomial(coeffs=[4.05519,0.0238058,-1.64671e-05,5.31267e-09,-6.46619e-13,-55493.1,4.4326], Tmin=(509.965,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-459.238,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C-H': 2, 'Li-O': 2}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 3]]) broke during the scan.Significant difference observed between consecutive conformersCould not read energies
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Bond ([[3, 5]]) broke during the scan.Bond ([[1, 2]]) broke during the scan.Bond ([[1, 4]]) broke during the scan.


External symmetry: 2, optical isomers: 1

Geometry:
Li      0.00107985    0.79281690    1.32154581
O       1.12713706    0.12203045    0.00774572
C      -0.00002945   -0.72355415   -0.04012199
O      -1.12710980    0.12217864    0.00947152
Li     -0.00085915    0.93720053   -1.22017199
H      -0.00096096   -1.35041594   -0.95978103
H       0.00066184   -1.45252493    0.80083185
""",
)

entry(
    index = 66,
    label = "[Li]OC1[[Li]]OCCO1",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C  u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C  u0 p0 c0 {4,S} {5,S} {6,S} {11,S}
4  O  u0 p2 c0 {1,S} {3,S}
5  O  u0 p2 c0 {2,S} {3,S}
6  O  u0 p2 c0 {3,S} {12,S}
7  H  u0 p0 c0 {1,S}
8  H  u0 p0 c0 {1,S}
9  H  u0 p0 c0 {2,S}
10 H  u0 p0 c0 {2,S}
11 Li u0 p0 c0 {3,S}
12 Li u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.813,0.0124988,0.000183976,-4.41209e-07,3.14155e-10,-59275,10.9223], Tmin=(10,'K'), Tmax=(474.317,'K')),
            NASAPolynomial(coeffs=[3.49148,0.0481935,-3.32143e-05,1.06658e-08,-1.28986e-12,-59615.5,8.32251], Tmin=(474.317,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-492.875,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 5, 'C-Li': 1, 'Li-O': 1, 'C-H': 4, 'C-C': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: 


External symmetry: 1, optical isomers: 1

Geometry:
Li      0.64114541    0.00093226    1.63099110
O       1.85221041   -0.00048192    0.27780774
C       0.69328400   -0.00112816   -0.41558391
Li      2.32755241   -0.00233438   -1.41419707
O      -0.15676164   -1.11253472    0.19155903
C      -1.46982490   -0.77711823   -0.17872815
C      -1.46962254    0.77587012   -0.18054676
O      -0.15646797    1.11181391    0.18893411
H      -2.16985119   -1.20857613    0.54061251
H      -1.70200302   -1.16749913   -1.17549979
H      -2.16951602    1.20920851    0.53779171
H      -1.70172542    1.16396761   -1.17823063
""",
)

entry(
    index = 67,
    label = "[Li]OC[=O]OCC[Li]",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C  u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C  u0 p0 c0 {4,S} {5,S} {11,D}
4  O  u0 p2 c0 {1,S} {3,S}
5  O  u0 p2 c0 {3,S} {12,S}
6  H  u0 p0 c0 {1,S}
7  H  u0 p0 c0 {1,S}
8  Li u0 p0 c0 {2,S}
9  H  u0 p0 c0 {2,S}
10 H  u0 p0 c0 {2,S}
11 O  u0 p2 c0 {3,D}
12 Li u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.39564,0.0630088,-0.000131753,2.61413e-07,-2.27164e-10,-70577.2,12.9484], Tmin=(10,'K'), Tmax=(339.7,'K')),
            NASAPolynomial(coeffs=[4.21068,0.0469555,-3.2359e-05,1.04042e-08,-1.26157e-12,-70595.4,10.4446], Tmin=(339.7,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-586.805,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 3, 'C-Li': 1, 'Li-O': 1, 'C-H': 4, 'C-C': 1, 'C=O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: 
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: 
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: 
* Invalidated! pivots: [5, 7], dihedral: [4, 5, 7, 8], invalidation reason: 


External symmetry: 1, optical isomers: 1

Geometry:
Li      4.18768447   -0.71344870    0.00048653
C       2.53145712    0.38650122    0.00013276
C       1.22352576   -0.33978044   -0.00050755
O       0.10098902    0.60312239   -0.00041469
C      -1.12317546    0.10203545    0.00000359
O      -1.31707076   -1.15370250    0.00020736
O      -2.08691848    0.91940325    0.00012273
Li     -3.08366665   -0.61717802    0.00026703
H       2.56728664    1.05175862   -0.87418167
H       2.56672691    1.05116054    0.87493030
H       1.09313895   -0.97503626   -0.88092879
H       1.09266132   -0.97580464    0.87926955
""",
)

entry(
    index = 68,
    label = "[Li]C[Li]",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 Li u0 p0 c0 {1,S}
3 Li u0 p0 c0 {1,S}
4 H  u0 p0 c0 {1,S}
5 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87349,0.00895393,7.22697e-05,-2.35138e-07,2.01877e-10,33512.4,5.21861], Tmin=(10,'K'), Tmax=(440.156,'K')),
            NASAPolynomial(coeffs=[6.42008,0.00883236,-5.76942e-06,1.88755e-09,-2.40037e-13,33065.2,-7.51067], Tmin=(440.156,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (278.629,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 2, 'C-Li': 2}

External symmetry: 2, optical isomers: 1

Geometry:
Li      1.69239227   -0.63637706    0.00000446
C       0.00000178    0.31138316   -0.00000055
Li     -1.69238654   -0.63638237    0.00000647
H      -0.00000336    0.97455800    0.88399316
H      -0.00002043    0.97451388   -0.88402812
""",
)

entry(
    index = 69,
    label = "[Li]C[[Li]][Li]",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 Li u0 p0 c0 {1,S}
3 Li u0 p0 c0 {1,S}
4 Li u0 p0 c0 {1,S}
5 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7617,0.0186528,9.13335e-05,-4.05496e-07,4.19469e-10,49477.8,6.03207], Tmin=(10,'K'), Tmax=(384.68,'K')),
            NASAPolynomial(coeffs=[8.1201,0.00855895,-6.6652e-06,2.38821e-09,-3.16272e-13,48881.8,-14.2186], Tmin=(384.68,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (411.398,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-Li': 3, 'C-H': 1}

External symmetry: 3, optical isomers: 1

Geometry:
Li     -1.51175395   -1.05608329    0.26627201
C      -0.00052331   -0.00008314   -0.18183020
Li     -0.15719441    1.83734610    0.26405396
Li      1.66989503   -0.78037402    0.26644246
H      -0.00190835   -0.00168746   -1.29946586
""",
)

entry(
    index = 70,
    label = "[Li]C[[Li]][[Li]][Li]",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 Li u0 p0 c0 {1,S}
3 Li u0 p0 c0 {1,S}
4 Li u0 p0 c0 {1,S}
5 Li u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70816,0.0235718,7.22621e-05,-3.64139e-07,3.85087e-10,60464.4,5.43291], Tmin=(10,'K'), Tmax=(384.957,'K')),
            NASAPolynomial(coeffs=[8.13521,0.0110665,-9.52546e-06,3.52665e-09,-4.69908e-13,59875.3,-14.9224], Tmin=(384.957,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (502.746,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-Li': 4}

External symmetry: 12, optical isomers: 1

Geometry:
Li      1.32256042    0.80505562   -1.05709191
C      -0.00005546    0.00007832   -0.00013873
Li     -0.95325698    1.32406532    0.92397660
Li      0.80593655   -1.16367246    1.22929093
Li     -1.17511714   -0.96572486   -1.09598861
""",
)

entry(
    index = 71,
    label = "[Li]CC[Li]",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C  u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3 Li u0 p0 c0 {1,S}
4 Li u0 p0 c0 {2,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {1,S}
7 H  u0 p0 c0 {2,S}
8 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88192,0.00744896,0.000105012,-2.4455e-07,1.65599e-10,27931.7,6.67966], Tmin=(10,'K'), Tmax=(515.679,'K')),
            NASAPolynomial(coeffs=[4.90711,0.0242804,-1.60373e-05,5.14062e-09,-6.32678e-13,27496.4,-0.782468], Tmin=(515.679,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (232.203,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 4, 'C-C': 1, 'C-Li': 2}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[3, 4]]) broke during the scan.Bond ([[2, 4]]) broke during the scan.Bond ([[1, 3]]) broke during the scan.Bond ([[1, 2]]) broke during the scan.Bond ([[3, 4]]) broke during the scan. But unable to propose troubleshooting methods.


External symmetry: 2, optical isomers: 1

Geometry:
Li      1.82737022    0.18176897    0.00136049
C       0.01098709    0.78301129   -0.00033902
C      -0.01098676   -0.78301371   -0.00031871
Li     -1.82736810   -0.18176473    0.00135693
H      -0.42255467    1.24154946   -0.90113037
H      -0.42399125    1.24170303    0.89978079
H       0.42256312   -1.24157177   -0.90109726
H       0.42398634   -1.24168260    0.89981364
""",
)

entry(
    index = 72,
    label = "[Li]OO[Li]",
    molecule = 
"""
1 O  u0 p2 c0 {2,S} {3,S}
2 O  u0 p2 c0 {1,S} {4,S}
3 Li u0 p0 c0 {1,S}
4 Li u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91551,0.00550928,5.2339e-05,-1.40411e-07,1.02423e-10,-31219.3,6.36234], Tmin=(10,'K'), Tmax=(501.967,'K')),
            NASAPolynomial(coeffs=[5.37641,0.00977885,-7.96535e-06,2.82608e-09,-3.64069e-13,-31566.5,-1.67548], Tmin=(501.967,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-259.592,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'Li-O': 2, 'O-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[3, 4]]) broke during the scan.Bond ([[2, 4]]) broke during the scan.The rotor scan has a barrier of 179.82 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 4, optical isomers: 1

Geometry:
Li      1.54954280    0.00150729   -0.00277754
O      -0.00076494    0.76554150    0.00096114
O       0.00076494   -0.76554150    0.00096114
Li     -1.54954280   -0.00150729   -0.00277754
""",
)

entry(
    index = 73,
    label = "[Li]OC[C][O[Li]]O[Li]",
    molecule = 
"""
1  O  u0 p2 c0 {4,S} {6,S}
2  O  u0 p2 c0 {4,S} {7,S}
3  O  u0 p2 c0 {4,S} {8,S}
4  C  u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5  C  u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
6  Li u0 p0 c0 {1,S}
7  Li u0 p0 c0 {2,S}
8  Li u0 p0 c0 {3,S}
9  H  u0 p0 c0 {5,S}
10 H  u0 p0 c0 {5,S}
11 H  u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75219,0.0157798,0.000186233,-4.59606e-07,3.19914e-10,-109208,9.31713], Tmin=(10,'K'), Tmax=(513.557,'K')),
            NASAPolynomial(coeffs=[7.209,0.0390816,-2.85281e-05,9.62034e-09,-1.21147e-12,-110225,-11.5049], Tmin=(513.557,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-908.075,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (253.591,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 3, 'C-H': 3, 'C-C': 1, 'Li-O': 3}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: The rotor scan has a barrier of 68.14 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
pivots: [3, 4], dihedral: [2, 3, 4, 9], rotor symmetry: 3, max scan energy: 14.38 kJ/mol
* Invalidated! pivots: [3, 5], dihedral: [2, 3, 5, 6], invalidation reason: Bond ([[1, 5]]) broke during the scan.Significant difference observed between consecutive conformersBond ([[2, 6]]) broke during the scan.Bond ([[3, 4]]) broke during the scan.Significant difference observed between consecutive conformersBond ([[1, 6]]) broke during the scan.Bond ([[7, 8]]) broke during the scan.Bond ([[3, 5]]) broke during the scan.Significant difference observed between consecutive conformersThe rotor scan has a barrier of 40.83 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
* Invalidated! pivots: [3, 7], dihedral: [2, 3, 7, 8], invalidation reason: Bond ([[1, 5]]) broke during the scan.Bond ([[1, 5]]) broke during the scan. But unable to propose troubleshooting methods.


External symmetry: 3, optical isomers: 1

Geometry:
Li     -0.85075259    1.77296760    0.77123352
O       0.52518802   -1.19749782    0.43665141
C       0.00774246   -0.00367277   -0.11395170
C       0.10975846   -0.05153696   -1.64301472
O      -1.34455780    0.13712715    0.27027079
Li     -1.17230256   -1.53638908    0.85332047
O       0.74764832    1.09424175    0.37951312
Li      1.84896152   -0.15449065    1.01067860
H      -0.45563481   -0.89994375   -2.03400166
H      -0.29148255    0.86606382   -2.07806276
H       1.15260455   -0.15667864   -1.94932936
""",
)

entry(
    index = 74,
    label = "[Li]N[Li]",
    molecule = 
"""
1 N  u0 p1 c0 {2,S} {3,S} {4,S}
2 Li u0 p0 c0 {1,S}
3 Li u0 p0 c0 {1,S}
4 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90065,0.00703115,5.12111e-05,-1.70111e-07,1.46039e-10,20038.7,4.93326], Tmin=(10,'K'), Tmax=(443.899,'K')),
            NASAPolynomial(coeffs=[5.91773,0.00619105,-4.53073e-06,1.58352e-09,-2.07286e-13,19688.9,-5.08363], Tmin=(443.899,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (166.604,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-N': 1, 'Li-N': 2}

External symmetry: 2, optical isomers: 1

Geometry:
Li      1.59909821   -0.47037659   -0.00013831
N      -0.00000054    0.22511536    0.00012908
Li     -1.59909955   -0.47036976   -0.00013831
H       0.00001630    1.24653648   -0.00066453
""",
)

entry(
    index = 75,
    label = "[Li]N[[Li]][Li]",
    molecule = 
"""
1 N  u0 p1 c0 {2,S} {3,S} {4,S}
2 Li u0 p0 c0 {1,S}
3 Li u0 p0 c0 {1,S}
4 Li u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81383,0.0156267,1.58498e-05,-1.09407e-07,1.10781e-10,33331.5,5.22518], Tmin=(10,'K'), Tmax=(422.639,'K')),
            NASAPolynomial(coeffs=[6.00268,0.008477,-6.92386e-06,2.46572e-09,-3.19204e-13,33025.4,-4.88304], Tmin=(422.639,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (277.13,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'Li-N': 3}

External symmetry: 6, optical isomers: 1

Geometry:
Li      1.24388269    1.20065683   -0.00020422
N       0.00046802   -0.00069642    0.00011736
Li     -1.66153404    0.47568780   -0.00020573
Li      0.41938166   -1.67812095   -0.00020233
""",
)

entry(
    index = 76,
    label = "[Li]NC[Li]",
    molecule = 
"""
1 N  u0 p1 c0 {2,S} {4,S} {7,S}
2 C  u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3 Li u0 p0 c0 {2,S}
4 Li u0 p0 c0 {1,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89845,0.00643681,8.96485e-05,-2.10392e-07,1.43352e-10,21908.7,7.34308], Tmin=(10,'K'), Tmax=(512.392,'K')),
            NASAPolynomial(coeffs=[4.74482,0.0208411,-1.40294e-05,4.53188e-09,-5.58103e-13,21546.1,1.13423], Tmin=(512.392,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (182.131,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-N': 1, 'H-N': 1, 'Li-N': 1, 'C-H': 2, 'C-Li': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 2]]) broke during the scan.Bond ([[2, 4]]) broke during the scan.Bond ([[3, 4]]) broke during the scan.Bond ([[1, 3]]) broke during the scan.Bond ([[1, 4]]) broke during the scan.Could not read energies


External symmetry: 1, optical isomers: 1

Geometry:
Li      1.32146488    0.38283908   -0.81949563
N      -0.04198811    0.68107318    0.35537058
C       0.04603486   -0.79736387    0.03309940
Li     -1.35519126    0.22828766   -0.82514251
H      -0.05146683    0.87496965    1.34966277
H       0.94506033   -1.29218983    0.44356661
H      -0.77879163   -1.39832203    0.45592429
""",
)

entry(
    index = 77,
    label = "[Li]NN[Li]",
    molecule = 
"""
1 N  u0 p1 c0 {2,S} {3,S} {5,S}
2 N  u0 p1 c0 {1,S} {4,S} {6,S}
3 Li u0 p0 c0 {1,S}
4 Li u0 p0 c0 {2,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91274,0.00510023,7.11692e-05,-1.51864e-07,9.24349e-11,19408.6,6.10284], Tmin=(10,'K'), Tmax=(581.808,'K')),
            NASAPolynomial(coeffs=[5.11215,0.0172314,-1.26429e-05,4.37082e-09,-5.65225e-13,18924.2,-1.99789], Tmin=(581.808,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (161.337,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'N-N': 1, 'H-N': 2, 'Li-N': 2}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 2]]) broke during the scan.Bond ([[1, 3]]) broke during the scan.Bond ([[3, 4]]) broke during the scan.Bond ([[1, 4]]) broke during the scan.Could not read energies


External symmetry: 2, optical isomers: 1

Geometry:
Li      1.50270362   -0.00019319   -0.58010606
N       0.00014373    0.76798461    0.09771112
N      -0.00012588   -0.76792687    0.09793743
Li     -1.50278060   -0.00000029   -0.57984305
H      -0.00017618    1.10809388    1.05530515
H       0.00038708   -1.10781361    1.05561295
""",
)

entry(
    index = 78,
    label = "[Li]NCN[Li]",
    molecule = 
"""
1 N  u0 p1 c0 {3,S} {4,S} {8,S}
2 N  u0 p1 c0 {3,S} {5,S} {9,S}
3 C  u0 p0 c0 {1,S} {2,S} {6,S} {7,S}
4 Li u0 p0 c0 {1,S}
5 Li u0 p0 c0 {2,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {3,S}
8 H  u0 p0 c0 {1,S}
9 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89569,0.00620013,0.000110387,-2.2591e-07,1.37036e-10,2483.88,7.39116], Tmin=(10,'K'), Tmax=(559.299,'K')),
            NASAPolynomial(coeffs=[3.62686,0.0317688,-2.16033e-05,7.01002e-09,-8.64416e-13,2144.1,5.22554], Tmin=(559.299,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (20.6115,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-N': 2, 'H-N': 2, 'Li-N': 2, 'C-H': 2}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[2, 5]]) broke during the scan.Bond ([[4, 5]]) broke during the scan.The rotor scan has a barrier of 165.88 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Bond ([[1, 4]]) broke during the scan.Bond ([[1, 2]]) broke during the scan.The rotor scan has a barrier of 165.74 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 2, optical isomers: 1

Geometry:
Li      0.00019339   -0.97539462    1.29111885
N       1.14361136   -0.16718463   -0.00012900
C      -0.00000743    0.77026536    0.00174399
N      -1.14362726   -0.16725375   -0.00012619
Li     -0.00015615   -0.96947783   -1.29506819
H       2.02675033    0.32304903    0.00048631
H      -0.00002778    1.45721779   -0.87371333
H      -0.00007559    1.45374159    0.87988283
H      -2.02675195    0.32300068    0.00122037
""",
)

entry(
    index = 79,
    label = "[Li]NCCN[Li]",
    molecule = 
"""
1  N  u0 p1 c0 {3,S} {5,S} {11,S}
2  N  u0 p1 c0 {4,S} {6,S} {12,S}
3  C  u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
4  C  u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
5  Li u0 p0 c0 {1,S}
6  Li u0 p0 c0 {2,S}
7  H  u0 p0 c0 {3,S}
8  H  u0 p0 c0 {3,S}
9  H  u0 p0 c0 {4,S}
10 H  u0 p0 c0 {4,S}
11 H  u0 p0 c0 {1,S}
12 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87331,0.00766158,0.000152002,-3.10143e-07,1.9073e-10,-3814.79,9.04109], Tmin=(10,'K'), Tmax=(540.506,'K')),
            NASAPolynomial(coeffs=[2.53617,0.0453812,-2.98934e-05,9.44957e-09,-1.14245e-12,-4076.68,10.9096], Tmin=(540.506,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-31.7639,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-N': 2, 'C-H': 4, 'C-C': 1, 'H-N': 2, 'Li-N': 2}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[2, 6]]) broke during the scan.Significant difference observed between consecutive conformersBond ([[1, 5]]) broke during the scan.The rotor scan has a barrier of 464.89 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Bond ([[1, 2]]) broke during the scan.Bond ([[5, 6]]) broke during the scan.Bond ([[1, 5]]) broke during the scan.Bond ([[2, 6]]) broke during the scan.Bond ([[3, 4]]) broke during the scan.The rotor scan has a barrier of 1171.95 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: Bond ([[1, 5]]) broke during the scan.Significant difference observed between consecutive conformersBond ([[2, 6]]) broke during the scan.Bond ([[5, 6]]) broke during the scan.Bond ([[2, 3]]) broke during the scan.The rotor scan has a barrier of 440.88 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 2, optical isomers: 2

Geometry:
Li      0.11143348   -1.16870289    1.21595665
N       1.31621305   -0.51034092   -0.15115957
C       0.75105076    0.80581943    0.17569589
C      -0.75133563    0.80532556   -0.17678037
N      -1.31581646   -0.51076324    0.15149726
Li     -0.11096210   -1.17162039   -1.21383801
H       2.32250636   -0.44604557   -0.18360737
H       0.83717058    1.06263348    1.25521912
H       1.24176993    1.63632911   -0.34953800
H      -0.83776273    1.06105902   -1.25647910
H      -1.24237349    1.63600098    0.34791842
H      -2.32213903   -0.44707674    0.18402267
""",
)

entry(
    index = 80,
    label = "[Li]S[Li]",
    molecule = 
"""
1 S  u0 p2 c0 {2,S} {3,S}
2 Li u0 p0 c0 {1,S}
3 Li u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86856,0.0141853,-3.65516e-05,5.18374e-08,-2.9536e-11,-4035.21,7.2714], Tmin=(10,'K'), Tmax=(428.812,'K')),
            NASAPolynomial(coeffs=[4.86051,0.00493221,-4.18398e-06,1.51581e-09,-1.98111e-13,-4120.28,3.32573], Tmin=(428.812,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-33.5416,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'Li-S': 2}

External symmetry: 1, optical isomers: 1

Geometry:
Li      1.96885897    0.00000000    0.49067031
S       0.00000000    0.00000000   -0.17847632
Li     -1.96885897    0.00000000    0.49067031
""",
)

entry(
    index = 81,
    label = "[Li]SS[Li]",
    molecule = 
"""
1 S  u0 p2 c0 {2,S} {3,S}
2 S  u0 p2 c0 {1,S} {4,S}
3 Li u0 p0 c0 {1,S}
4 Li u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87677,0.00824943,5.57642e-05,-1.78557e-07,1.42879e-10,-15382.5,8.17221], Tmin=(10,'K'), Tmax=(485.733,'K')),
            NASAPolynomial(coeffs=[7.11199,0.00467114,-4.40924e-06,1.78539e-09,-2.53328e-13,-15968.8,-7.90044], Tmin=(485.733,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-127.92,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (78.9875,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'Li-S': 2, 'S-S': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 176272.26 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
B 2 3 F
B 1 3 F
B 1 2 F
B 2 4 F
B 3 4 F


External symmetry: 2, optical isomers: 1

Geometry:
Li     -0.00053497   -1.69494027   -0.79817185
S      -1.08111212    0.00053796    0.14843873
S       1.08123077   -0.00041175    0.14872402
Li      0.00086573    1.69526994   -0.79772806
""",
)

entry(
    index = 82,
    label = "[Li]SN[Li]",
    molecule = 
"""
1 S  u0 p2 c0 {2,S} {4,S}
2 N  u0 p1 c0 {1,S} {3,S} {5,S}
3 Li u0 p0 c0 {2,S}
4 Li u0 p0 c0 {1,S}
5 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89407,0.00654843,6.8253e-05,-1.69894e-07,1.15624e-10,116.123,8.03059], Tmin=(10,'K'), Tmax=(540.316,'K')),
            NASAPolynomial(coeffs=[6.2529,0.0117582,-9.15204e-06,3.27207e-09,-4.31734e-13,-469.73,-4.95987], Tmin=(540.316,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (0.930657,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-N': 1, 'Li-N': 1, 'N-S': 1, 'Li-S': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 4]]) broke during the scan.Bond ([[1, 2]]) broke during the scan.Bond ([[2, 4]]) broke during the scan.The rotor scan has a barrier of 117.62 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 1, optical isomers: 1

Geometry:
Li      0.56878916   -1.58194699   -0.62297734
S      -0.75905876    0.00022501    0.07201615
N       1.06575990   -0.00038962    0.19756186
Li      0.56980951    1.58158833   -0.62282922
H       1.28468331   -0.00044342    1.18805124
""",
)

entry(
    index = 83,
    label = "[Li]SC[Li]",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 S  u0 p2 c0 {1,S} {6,S}
3 Li u0 p0 c0 {1,S}
4 H  u0 p0 c0 {1,S}
5 H  u0 p0 c0 {1,S}
6 Li u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86857,0.0086075,8.76115e-05,-2.35121e-07,1.7397e-10,6454.11,8.52859], Tmin=(10,'K'), Tmax=(494.166,'K')),
            NASAPolynomial(coeffs=[6.26246,0.0151245,-1.07697e-05,3.63912e-09,-4.63857e-13,5901.35,-4.53209], Tmin=(494.166,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (53.6332,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-S': 1, 'Li-S': 1, 'C-H': 2, 'C-Li': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 3]]) broke during the scan.Bond ([[2, 4]]) broke during the scan.Bond ([[1, 2]]) broke during the scan.Bond ([[3, 4]]) broke during the scan.Bond ([[2, 3]]) broke during the scan.Significant difference observed between consecutive conformersThe rotor scan has a barrier of 473.17 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 1, optical isomers: 1

Geometry:
Li      0.15405931   -1.88490425    0.00120455
S      -0.73739917    0.04930488   -0.00043100
C       1.12631217    0.00251627   -0.00025455
Li      0.47231439    1.87320032    0.00115240
H       1.58167460   -0.38445748   -0.91760818
H       1.58159986   -0.38461997    0.91711563
""",
)

entry(
    index = 84,
    label = "SC[[Li]][Li]",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 S  u0 p2 c0 {1,S} {6,S}
3 Li u0 p0 c0 {1,S}
4 Li u0 p0 c0 {1,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82768,0.0123666,9.80227e-05,-3.16088e-07,2.71448e-10,31209.5,9.48957], Tmin=(10,'K'), Tmax=(434.199,'K')),
            NASAPolynomial(coeffs=[6.64513,0.0151589,-1.09359e-05,3.68994e-09,-4.67159e-13,30693.8,-4.87307], Tmin=(434.199,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (259.481,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-Li': 2, 'C-S': 1, 'H-S': 1, 'C-H': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [5, 1, 2, 3], invalidation reason: Bond ([[3, 4]]) broke during the scan.Bond ([[1, 2]]) broke during the scan.Bond ([[1, 3]]) broke during the scan.Significant difference observed between consecutive conformersCould not read energies


External symmetry: 1, optical isomers: 2

Geometry:
S      -0.87051736   -0.13969959   -0.01063250
C       0.88876802   -0.02629742   -0.30186103
Li      0.31834905    1.74690332    0.17776530
Li      2.53488026   -0.48735153    0.50550550
H      -1.05091717   -0.81732761    1.14897329
H       1.07850670   -0.57214257   -1.23819525
""",
)

entry(
    index = 85,
    label = "S=C[[Li]][Li]",
    molecule = 
"""
1 S  u0 p2 c0 {2,D}
2 C  u0 p0 c0 {1,D} {3,S} {4,S}
3 Li u0 p0 c0 {2,S}
4 Li u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89151,0.00715677,5.85559e-05,-1.70268e-07,1.29901e-10,36390.7,7.28028], Tmin=(10,'K'), Tmax=(494.013,'K')),
            NASAPolynomial(coeffs=[6.33353,0.00802818,-6.77355e-06,2.4842e-09,-3.29756e-13,35897.5,-5.3286], Tmin=(494.013,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (302.546,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-Li': 2, 'C=S': 1}

External symmetry: 2, optical isomers: 1

Geometry:
S      -0.00026730   -0.61537280    0.00000000
C       0.00058363    1.09455487    0.00000000
Li     -1.88597711    0.54762660    0.00000000
Li      1.88665347    0.54586383    0.00000000
""",
)

entry(
    index = 86,
    label = "[Li]SCS[Li]",
    molecule = 
"""
1 S  u0 p2 c0 {3,S} {4,S}
2 S  u0 p2 c0 {3,S} {5,S}
3 C  u0 p0 c0 {1,S} {2,S} {6,S} {7,S}
4 Li u0 p0 c0 {1,S}
5 Li u0 p0 c0 {2,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81109,0.0130391,0.000117235,-3.4745e-07,2.79652e-10,-18587.4,9.29869], Tmin=(10,'K'), Tmax=(458.269,'K')),
            NASAPolynomial(coeffs=[7.00948,0.0190712,-1.3631e-05,4.58152e-09,-5.79474e-13,-19237,-7.52548], Tmin=(458.269,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-154.568,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-S': 2, 'Li-S': 2, 'C-H': 2}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[2, 5]]) broke during the scan.Bond ([[4, 5]]) broke during the scan.Bond ([[1, 4]]) broke during the scan.Bond ([[1, 5]]) broke during the scan.Bond ([[1, 2]]) broke during the scan.The rotor scan has a barrier of 487.33 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Bond ([[1, 4]]) broke during the scan.Bond ([[1, 2]]) broke during the scan.Bond ([[2, 5]]) broke during the scan.Bond ([[1, 5]]) broke during the scan.Bond ([[4, 5]]) broke during the scan.The rotor scan has a barrier of 485.94 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 2, optical isomers: 1

Geometry:
Li      0.00016703   -1.00767581    1.42646958
S       1.53982665   -0.08861015   -0.00027178
C       0.00002862    0.94494075    0.00134824
S      -1.53987510   -0.08848405    0.00006222
Li     -0.00035838   -1.00175069   -1.43064425
H      -0.00005485    1.59859685   -0.87039327
H       0.00014566    1.59631477    0.87477448
""",
)

entry(
    index = 87,
    label = "[Li]CC=C",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C  u0 p0 c0 {1,S} {3,D} {7,S}
3 C  u0 p0 c0 {2,D} {8,S} {9,S}
4 Li u0 p0 c0 {1,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {1,S}
7 H  u0 p0 c0 {2,S}
8 H  u0 p0 c0 {3,S}
9 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93657,0.00368542,9.24674e-05,-1.71331e-07,9.72994e-11,12778.3,7.07382], Tmin=(10,'K'), Tmax=(567.428,'K')),
            NASAPolynomial(coeffs=[1.93733,0.0321786,-2.09206e-05,6.6114e-09,-8.0355e-13,12773.4,13.5434], Tmin=(567.428,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (106.218,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'C-H': 5, 'C-C': 1, 'C-Li': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformersCould not read energies


External symmetry: 1, optical isomers: 1

Geometry:
Li     -0.00053281   -1.41347100    0.73652055
C      -1.24506870   -0.00265392   -0.17363087
C       0.00013487    0.53803581    0.13796797
C       1.24516672   -0.00342540   -0.17305304
H      -2.15040002    0.50161346    0.13388957
H      -1.33983051   -0.65266095   -1.04541024
H       0.00021869    1.35584492    0.85914690
H       1.33988865   -0.65347027   -1.04481537
H       2.15065213    0.50044451    0.13466794
""",
)

entry(
    index = 88,
    label = "C=CCC[CH2]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  C u1 p0 c0 {2,S} {11,S} {12,S}
5  C u0 p0 c0 {3,D} {13,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73995,0.0262781,2.92843e-05,-5.02212e-08,1.9846e-11,19835.4,11.2041], Tmin=(10,'K'), Tmax=(891.797,'K')),
            NASAPolynomial(coeffs=[2.46569,0.0451131,-2.44629e-05,6.45403e-09,-6.66329e-13,19541,14.2808], Tmin=(891.797,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (164.921,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'C-H': 9, 'C-C': 3}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: 
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Another conformer for C=CCC[CH2] exists which is 0.52 kJ/mol lower.
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 13], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
C       2.44894800    0.00616800   -0.28242900
C       1.25189700    0.58910200   -0.29406900
C       0.06205100    0.14990200    0.51089800
C      -1.15897900   -0.20353000   -0.36184700
C      -2.41850000   -0.37536200    0.41451700
H       2.65374200   -0.85939700    0.34119400
H       3.26747500    0.37386900   -0.89129300
H       1.09546000    1.45472000   -0.93741700
H      -0.20890200    1.00766500    1.13993400
H       0.28638100   -0.68135900    1.18784700
H      -1.34541200    0.59826300   -1.08991500
H      -0.89782100   -1.08300400   -0.97494400
H      -3.37888800   -0.39494900   -0.08647800
H      -2.39468600   -0.62952200    1.46817100
""",
)

entry(
    index = 89,
    label = "C=CCCC[Li]",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C  u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C  u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
4  C  u0 p0 c0 {2,S} {5,D} {13,S}
5  C  u0 p0 c0 {4,D} {14,S} {15,S}
6  Li u0 p0 c0 {3,S}
7  H  u0 p0 c0 {1,S}
8  H  u0 p0 c0 {1,S}
9  H  u0 p0 c0 {2,S}
10 H  u0 p0 c0 {2,S}
11 H  u0 p0 c0 {3,S}
12 H  u0 p0 c0 {3,S}
13 H  u0 p0 c0 {4,S}
14 H  u0 p0 c0 {5,S}
15 H  u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78117,0.0389871,-1.25283e-06,-1.53804e-08,5.76749e-12,17137.9,11.0196], Tmin=(10,'K'), Tmax=(1232.64,'K')),
            NASAPolynomial(coeffs=[10.561,0.0338385,-1.54953e-05,3.41422e-09,-2.93962e-13,14186.2,-28.3005], Tmin=(1232.64,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (142.527,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (357.522,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'C-H': 9, 'C-C': 3, 'C-Li': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 10.04 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 24.83 kJ/mol
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 13.17 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -2.66317293    0.09456538    0.43594713
C      -1.62947098    0.19398279   -0.38767988
C      -0.33251800   -0.53908746   -0.25092980
C       0.87342107    0.39129050   -0.03782098
C       2.22520608   -0.32186906    0.07412426
Li      3.84269464    0.79416765    0.39282091
H      -2.63938775   -0.57337884    1.29158935
H      -3.56893357    0.67125005    0.28860645
H      -1.70068422    0.88144185   -1.23004202
H      -0.15121892   -1.13174402   -1.15545209
H      -0.39287790   -1.24795529    0.58105533
H       0.88952892    1.11479534   -0.86460300
H       0.67276649    0.98779645    0.86174909
H       2.37099035   -0.92524529   -0.83648108
H       2.15009296   -1.07111693    0.87907053
""",
)

entry(
    index = 90,
    label = "[Li]CC=O",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C  u0 p0 c0 {1,S} {6,D} {7,S}
3 Li u0 p0 c0 {1,S}
4 H  u0 p0 c0 {1,S}
5 H  u0 p0 c0 {1,S}
6 O  u0 p2 c0 {2,D}
7 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95461,0.00264523,6.84547e-05,-1.26897e-07,7.21699e-11,-21236.1,7.95527], Tmin=(10,'K'), Tmax=(563.035,'K')),
            NASAPolynomial(coeffs=[2.34342,0.0242209,-1.6011e-05,5.06746e-09,-6.12763e-13,-21215.2,13.3771], Tmin=(563.035,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-176.586,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'C-H': 3, 'C-C': 1, 'C-Li': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 2]]) broke during the scan.Significant difference observed between consecutive conformersBond ([[1, 4]]) broke during the scan.The rotor scan has a barrier of 496.10 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 1, optical isomers: 2

Geometry:
Li      0.50206792   -1.40248738    0.48676366
C      -1.19226531   -0.12156161   -0.09069677
C      -0.01560913    0.55580020    0.09941922
O       1.14700731    0.09112043   -0.19763500
H      -2.13140475    0.29031912    0.24959882
H      -1.24425812   -0.93714260   -0.81262474
H      -0.05699558    1.51710839    0.63386112
""",
)

entry(
    index = 91,
    label = "[Li]CC=N",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C  u0 p0 c0 {1,S} {3,D} {7,S}
3 N  u0 p1 c0 {2,D} {8,S}
4 Li u0 p0 c0 {1,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {1,S}
7 H  u0 p0 c0 {2,S}
8 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94932,0.00289585,7.7778e-05,-1.39635e-07,7.69003e-11,6946.86,7.74921], Tmin=(10,'K'), Tmax=(579.834,'K')),
            NASAPolynomial(coeffs=[1.8646,0.0288196,-1.91447e-05,6.13262e-09,-7.50812e-13,6994.59,14.9975], Tmin=(579.834,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (57.737,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-N': 1, 'C-H': 3, 'C-C': 1, 'C=N': 1, 'C-Li': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 4]]) broke during the scan.Significant difference observed between consecutive conformersBond ([[1, 2]]) broke during the scan.Significant difference observed between consecutive conformersBond ([[1, 4]]) broke during the scan. But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
Li      0.23178999   -1.48321179   -0.49113613
C      -1.22576659   -0.03665132    0.09612251
C       0.00825925    0.55501184   -0.10051212
N       1.15665531   -0.05253960    0.21149503
H      -1.34266534   -0.77824112    0.88591052
H      -2.12837823    0.44934053   -0.24289373
H       0.02630632    1.51056028   -0.63591184
H       1.95853196    0.52707591    0.01526644
""",
)

entry(
    index = 92,
    label = "O=C",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.03214,-0.00195569,9.08093e-06,2.89231e-09,-8.02863e-12,-14462.6,3.46835], Tmin=(10,'K'), Tmax=(597.035,'K')),
            NASAPolynomial(coeffs=[1.41053,0.00952528,-4.48054e-06,9.69436e-10,-7.73086e-14,-14041.1,15.6719], Tmin=(597.035,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-120.237,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'C-H': 2}

External symmetry: 2, optical isomers: 1

Geometry:
O       0.00000000    0.00000000    0.67105183
C       0.00000000    0.00000000   -0.52477755
H       0.93959977    0.00000000   -1.10994430
H      -0.93959977    0.00000000   -1.10994430
""",
)

entry(
    index = 93,
    label = "N=C",
    molecule = 
"""
1 N u0 p1 c0 {2,D} {5,S}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.08222,-0.00485107,3.06854e-05,-3.08439e-08,1.00923e-11,9115.42,4.36611], Tmin=(10,'K'), Tmax=(928.945,'K')),
            NASAPolynomial(coeffs=[0.887603,0.0136926,-6.98872e-06,1.74161e-09,-1.7038e-13,9502.37,18.4309], Tmin=(928.945,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (75.812,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 2, 'C=N': 1, 'H-N': 1}

External symmetry: 1, optical isomers: 1

Geometry:
N       0.66408216    0.15430247    0.00000000
C      -0.58307890   -0.02891023    0.00000000
H       1.16405252   -0.73380180    0.00000000
H      -1.24295947    0.83934733    0.00000000
H      -1.06786980   -1.01049236    0.00000000
""",
)

entry(
    index = 94,
    label = "O=CCC[CH2]",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {5,D}
2  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  C u1 p0 c0 {3,S} {11,S} {12,S}
5  C u0 p0 c0 {1,D} {2,S} {10,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7927,0.0283819,2.22999e-06,-1.45812e-08,5.3342e-12,-2520.69,10.804], Tmin=(10,'K'), Tmax=(1175.04,'K')),
            NASAPolynomial(coeffs=[7.06548,0.0291635,-1.39876e-05,3.25501e-09,-2.97818e-13,-4112.9,-9.01553], Tmin=(1175.04,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-20.9425,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 3, 'C-H': 7, 'C=O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 8.41 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 30.01 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 1 2 3 4 F
D 3 4 5 11 F
pivots: [4, 5], dihedral: [3, 4, 5, 11], rotor symmetry: 1, max scan energy: 1.02 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.93215179   -0.71784412    0.03984750
C       1.49483145    0.39892837   -0.01074588
C       0.03429343    0.74914345   -0.03621995
C      -0.90195553   -0.44886362   -0.00457517
C      -2.33634822   -0.07162735    0.00534714
H       2.18466061    1.26893586   -0.04300079
H      -0.13546499    1.36577651   -0.92717771
H      -0.14910998    1.42110902    0.81180715
H      -0.65920987   -1.05954619    0.87759410
H      -0.68493137   -1.10549327   -0.85303807
H      -3.09817346   -0.80217306   -0.23085467
H      -2.65993508    0.89418234    0.37346169
""",
)

entry(
    index = 95,
    label = "[Li]NC=C",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {3,D} {4,S}
2 N  u0 p1 c0 {1,S} {5,S} {6,S}
3 C  u0 p0 c0 {1,D} {7,S} {8,S}
4 H  u0 p0 c0 {1,S}
5 Li u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {3,S}
8 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94943,0.00289045,7.78035e-05,-1.39697e-07,7.69516e-11,7198.08,7.74868], Tmin=(10,'K'), Tmax=(579.573,'K')),
            NASAPolynomial(coeffs=[1.86063,0.0288299,-1.91542e-05,6.13628e-09,-7.51312e-13,7246.66,15.0169], Tmin=(579.573,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (59.8257,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'Li-N': 1, 'C-H': 3, 'C=C': 1, 'C-N': 1, 'H-N': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 3]]) broke during the scan.Significant difference observed between consecutive conformersCould not read energies


External symmetry: 1, optical isomers: 2

Geometry:
Li     -0.23170979   -1.48331457    0.49114283
N      -1.15687116   -0.05258370   -0.21145052
C      -0.00844928    0.55470155    0.10096639
C       1.22559660   -0.03665110   -0.09647398
H      -1.95871795    0.52667492   -0.01392995
H      -0.02643838    1.50970216    0.63731266
H       2.12814231    0.44905344    0.24308122
H       1.34253578   -0.77748661   -0.88694979
""",
)

entry(
    index = 96,
    label = "NtCCC[CH2]",
    molecule = 
"""
multiplicity 2
1  N u0 p1 c0 {5,T}
2  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
4  C u1 p0 c0 {2,S} {10,S} {11,S}
5  C u0 p0 c0 {1,T} {3,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73583,0.0228054,2.86311e-05,-7.32776e-08,4.64076e-11,26989.4,11.0672], Tmin=(10,'K'), Tmax=(421.695,'K')),
            NASAPolynomial(coeffs=[2.24686,0.0369292,-2.16087e-05,6.14829e-09,-6.80112e-13,27114.9,16.9649], Tmin=(421.695,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (224.376,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 3, 'C-H': 6, 'C#N': 1}
1D rotors:
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Another conformer for NtCCC[CH2] exists which is 0.69 kJ/mol lower.
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 10], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
N       1.73049800    1.40197500   -1.86121100
C       1.13458500    0.94313200   -0.98656600
C       0.36253700    0.36602200    0.11134500
C      -1.06169000   -0.05686700   -0.31540800
C      -1.89964500   -0.47505700    0.84123300
H       0.90483300   -0.45981600    0.58279000
H       0.27933700    1.16016500    0.85940300
H      -0.97548900   -0.82943000   -1.09659500
H      -1.56014700    0.79022600   -0.79771200
H      -1.46147100   -0.98562200    1.69130500
H      -2.97888900   -0.41024200    0.79081700
""",
)

entry(
    index = 97,
    label = "O=COC[CH2]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u1 p0 c0 {1,S} {7,S} {8,S}
3  C u0 p0 c0 {4,S} {9,D} {10,S}
4  O u0 p2 c0 {1,S} {3,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7975,0.025542,-3.20254e-06,-8.33444e-09,3.47086e-12,-23787.3,10.8625], Tmin=(10,'K'), Tmax=(1170.54,'K')),
            NASAPolynomial(coeffs=[7.09221,0.0230641,-1.12795e-05,2.67432e-09,-2.49087e-13,-25160.2,-8.12092], Tmin=(1170.54,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-197.77,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 1, 'C-H': 5, 'C-O': 2, 'C=O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 28.40 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 3 4 5 10 F
pivots: [4, 5], dihedral: [3, 4, 5, 9], rotor symmetry: 1, max scan energy: 1.19 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.84558576   -0.63966488    0.03191043
C       1.34168439    0.44411931   -0.01444028
O       0.03519420    0.69557014   -0.03742675
C      -0.82573014   -0.45260077    0.00439661
C      -2.22569146    0.00660993   -0.00333746
H       1.89520655    1.39249502   -0.04510194
H      -0.58350856   -1.03449574    0.90459498
H      -0.60088177   -1.10334891   -0.84725555
H      -3.01758149   -0.70491105   -0.18750539
H      -2.47124308    1.01921707    0.28191976
""",
)

entry(
    index = 98,
    label = "O=CCC[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,D} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  O u1 p2 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91587,0.0211789,8.68009e-06,-1.92944e-08,6.8583e-12,-14953.3,11.0129], Tmin=(10,'K'), Tmax=(1127.8,'K')),
            NASAPolynomial(coeffs=[6.82032,0.0236549,-1.16072e-05,2.74354e-09,-2.5369e-13,-16421,-6.95129], Tmin=(1127.8,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-124.284,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 2, 'C-H': 5, 'C=O': 1, 'C-O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 12.53 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 14.76 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       2.22508857    0.15521879    0.22433934
C       1.09089148    0.36299871   -0.10605877
C       0.06439372   -0.71448914   -0.34047962
C      -1.26316175   -0.38788691    0.34187590
O      -1.89580412    0.71963795   -0.12148198
H       0.72671379    1.39986980   -0.26243884
H       0.46612327   -1.66968833    0.00144825
H      -0.10982255   -0.77564649   -1.41980825
H      -1.97833703   -1.22033977    0.20157670
H      -1.16099541   -0.31935013    1.43872418
""",
)

entry(
    index = 99,
    label = "O=CCO[CH2]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,D} {8,S}
3  C u1 p0 c0 {4,S} {9,S} {10,S}
4  O u0 p2 c0 {1,S} {3,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  O u0 p2 c0 {2,D}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75908,0.0250056,1.90461e-07,-1.33094e-08,5.61227e-12,-14149.9,11.1698], Tmin=(10,'K'), Tmax=(1029.48,'K')),
            NASAPolynomial(coeffs=[5.4591,0.0265642,-1.39755e-05,3.56707e-09,-3.566e-13,-14932.6,0.817633], Tmin=(1029.48,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-117.65,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 1, 'C-H': 5, 'C-O': 2, 'C=O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 21.87 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 29.05 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 1 2 3 4 F
D 4 5 9 10 F
D 3 4 5 10 F
pivots: [4, 5], dihedral: [3, 4, 5, 9], rotor symmetry: 1, max scan energy: 30.91 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 4 5 9 10 F


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.20488520    0.27069126    0.13432594
C      -1.08151701    0.26535930   -0.27984861
C      -0.03405011   -0.71885890    0.20382663
O       1.23409464   -0.44843924   -0.34137852
C       1.84932352    0.63865201    0.17589137
H      -0.73441881    0.97161489   -1.06175019
H      -0.32299795   -1.71942207   -0.12337037
H      -0.01210370   -0.71110535    1.30028757
H       2.81618111    0.84213552   -0.25916374
H       1.61314430    0.92243160    1.19711272
""",
)

entry(
    index = 100,
    label = "N=CCC[NH]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  N u1 p1 c0 {2,S} {11,S}
5  N u0 p1 c0 {3,D} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84092,0.0214685,2.46378e-05,-3.99772e-08,1.49441e-11,28340.6,10.9975], Tmin=(10,'K'), Tmax=(964.983,'K')),
            NASAPolynomial(coeffs=[3.67762,0.0358481,-1.90141e-05,4.89519e-09,-4.93359e-13,27734.1,8.47377], Tmin=(964.983,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (235.664,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 2, 'C-H': 5, 'H-N': 2, 'C-N': 1, 'C=N': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 21.25 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 3 4 5 12 F
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 17.05 kJ/mol
pivots: [4, 5], dihedral: [3, 4, 5, 12], rotor symmetry: 1, max scan energy: 11.74 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
N      -2.21930184   -0.10040756    0.28787278
C      -1.08250253   -0.33377384   -0.21373947
C      -0.05967070    0.74857286   -0.36827228
C       1.23769620    0.41879439    0.36466186
N       1.87774802   -0.74670209   -0.16742910
H      -2.78063317   -0.94910732    0.32047813
H      -0.77056087   -1.32891403   -0.55178515
H      -0.48411200    1.68306853    0.00173682
H       0.16896662    0.86939396   -1.43200572
H       1.92617153    1.27654164    0.30316839
H       1.04332257    0.28764909    1.44125938
H       2.71582425   -0.91894564    0.39171437
""",
)

entry(
    index = 101,
    label = "N=CCN[CH2]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  N u0 p1 c0 {1,S} {4,S} {8,S}
3  C u0 p0 c0 {1,S} {5,D} {9,S}
4  C u1 p0 c0 {2,S} {10,S} {11,S}
5  N u0 p1 c0 {3,D} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77101,0.0194155,5.94556e-05,-1.35098e-07,8.96897e-11,27711.7,11.0741], Tmin=(10,'K'), Tmax=(392.325,'K')),
            NASAPolynomial(coeffs=[1.62813,0.0412631,-2.40747e-05,6.84052e-09,-7.56107e-13,27879.9,19.4073], Tmin=(392.325,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (230.384,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 1, 'C-H': 5, 'C-N': 2, 'H-N': 2, 'C=N': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 23.34 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 3 4 5 10 F
D 9 3 4 5 F
D 3 4 5 11 F
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 42.75 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 3 4 5 10 F
D 7 2 3 9 F
D 3 4 5 11 F
pivots: [4, 5], dihedral: [3, 4, 5, 11], rotor symmetry: 1, max scan energy: 60.66 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 10 3 4 5 F
D 4 5 11 12 F
D 9 3 4 5 F
D 1 2 3 4 F


External symmetry: 1, optical isomers: 2

Geometry:
N       1.78104237   -0.78630067    0.01828883
C       1.42474920    0.42397532    0.01438359
C      -0.02104014    0.81185228   -0.00255499
N      -0.87837758   -0.32334225   -0.14952549
C      -2.22382698   -0.22153187    0.11634950
H       2.79207406   -0.88249684    0.04432206
H       2.13007052    1.26196608    0.03836031
H      -0.22233238    1.36517524    0.92963302
H      -0.17708024    1.53164706   -0.81794487
H      -0.41605501   -1.20154690    0.02915311
H      -2.69613092    0.73261361   -0.07903405
H      -2.80945203   -1.12509391    0.02703176
""",
)

entry(
    index = 102,
    label = "O=S[=O][C]CC[CH2]",
    molecule = 
"""
multiplicity 2
1  S u0 p0 c0 {2,D} {3,D} {4,S} {6,S}
2  O u0 p2 c0 {1,D}
3  O u0 p2 c0 {1,D}
4  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {4,S} {7,S} {10,S} {11,S}
6  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
7  C u1 p0 c0 {5,S} {15,S} {16,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.45669,0.0545486,-2.82219e-05,4.28915e-09,6.23838e-13,-28709.9,13.8241], Tmin=(10,'K'), Tmax=(1285.7,'K')),
            NASAPolynomial(coeffs=[12.0641,0.0365902,-1.75611e-05,4.09736e-09,-3.76466e-13,-31652.2,-32.7001], Tmin=(1285.7,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-238.741,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (382.466,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 2, 'C-H': 9, 'C-S': 2, 'O=S': 2}
1D rotors:
pivots: [2, 4], dihedral: [1, 2, 4, 8], rotor symmetry: 3, max scan energy: 8.50 kJ/mol
pivots: [2, 5], dihedral: [1, 2, 5, 6], rotor symmetry: 1, max scan energy: 16.72 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 14 6 7 16 F
pivots: [5, 6], dihedral: [2, 5, 6, 7], rotor symmetry: 1, max scan energy: 26.54 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 14 6 7 16 F
pivots: [6, 7], dihedral: [5, 6, 7, 15], rotor symmetry: 1, max scan energy: 1.05 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       0.97154173   -1.01295138    1.13640212
S       0.83316164   -0.16582519   -0.01451862
O       0.95865201   -0.72332316   -1.33186041
C       2.00881425    1.14987812    0.13339606
C      -0.74080003    0.66306644    0.09088828
C      -1.88335451   -0.34607861   -0.00319248
C      -3.21283620    0.31247262    0.02328706
H       2.98794306    0.67681418    0.06820237
H       1.89433284    1.63684622    1.09980561
H       1.87766298    1.85194178   -0.68762343
H      -0.76119710    1.19827809    1.04175661
H      -0.77784329    1.38202401   -0.73024417
H      -1.79541639   -1.07034167    0.81015430
H      -1.75998033   -0.92180984   -0.93208608
H      -3.36194192    1.27886574   -0.44212813
H      -4.08485675   -0.22431074    0.36989524
""",
)

entry(
    index = 103,
    label = "[Li]OS[=O][=C]C",
    molecule = 
"""
1  S  u0 p0 c0 {2,S} {3,D} {4,S} {5,D}
2  O  u0 p2 c0 {1,S} {6,S}
3  O  u0 p2 c0 {1,D}
4  C  u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
5  C  u0 p0 c0 {1,D} {10,S} {11,S}
6  Li u0 p0 c0 {2,S}
7  H  u0 p0 c0 {4,S}
8  H  u0 p0 c0 {4,S}
9  H  u0 p0 c0 {4,S}
10 H  u0 p0 c0 {5,S}
11 H  u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81972,0.0117873,0.000163534,-3.98089e-07,2.83019e-10,-45083.2,11.0026], Tmin=(10,'K'), Tmax=(488.251,'K')),
            NASAPolynomial(coeffs=[4.97339,0.0377532,-2.50474e-05,7.97282e-09,-9.69665e-13,-45618,1.94081], Tmin=(488.251,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-374.882,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C=S': 1, 'C-S': 1, 'O-S': 1, 'Li-O': 1, 'O=S': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 2]]) broke during the scan.Bond ([[1, 2]]) broke during the scan. But unable to propose troubleshooting methods.
pivots: [3, 6], dihedral: [2, 3, 6, 9], rotor symmetry: 3, max scan energy: 10.96 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
Li      2.25813273    0.62574404   -0.08097696
O       0.53043073    1.23018342   -0.49992352
S      -0.06000608   -0.07291001   -0.09725375
O      -0.34439027   -0.99361509   -1.16671980
C       1.04695338   -0.70989880    1.00580758
C      -1.61994556    0.37578400    0.62602140
H       0.93246474   -1.78367219    1.11182928
H       0.97975132   -0.18290747    1.96002060
H      -2.10132708   -0.53299545    0.98202295
H      -1.44893583    1.07122935    1.44549732
H      -2.21864315    0.84537908   -0.15323430
""",
)

entry(
    index = 104,
    label = "CCOC=C",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {5,D} {11,S}
5  C u0 p0 c0 {4,D} {12,S} {13,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84289,0.0171706,4.86789e-05,-7.19395e-08,2.89812e-11,-19068.9,9.40741], Tmin=(10,'K'), Tmax=(826.258,'K')),
            NASAPolynomial(coeffs=[1.067,0.0439821,-2.4273e-05,6.5103e-09,-6.82142e-13,-19066.6,19.5073], Tmin=(826.258,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-158.54,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 1, 'C-H': 8, 'C-O': 2, 'C=C': 1}
1D rotors:
pivots: [1, 2], dihedral: [6, 1, 2, 3], rotor symmetry: 3, max scan energy: 12.24 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 44.29 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 2 3 4 5 F
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 24.47 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       2.23290027    0.04643045    0.00000031
C       0.78053114    0.45879552    0.00000023
O      -0.01236128   -0.71547410   -0.00000017
C      -1.34813976   -0.55387367    0.00000026
C      -2.03851460    0.58154025   -0.00000023
H       2.46465059   -0.54784075   -0.88457907
H       2.46464960   -0.54784346    0.88457814
H       2.87175980    0.93099341    0.00000202
H       0.54001677    1.05894063    0.88572572
H       0.54001708    1.05894118   -0.88572496
H      -1.84126392   -1.51959588    0.00000112
H      -1.58098825    1.56066388   -0.00000126
H      -3.11770253    0.53096337    0.00000043
""",
)

entry(
    index = 105,
    label = "CCOC[=O]OCC",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {8,S}
2  O u0 p2 c0 {5,S} {8,S}
3  O u0 p2 c0 {8,D}
4  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
5  C u0 p0 c0 {2,S} {7,S} {11,S} {12,S}
6  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
7  C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
8  C u0 p0 c0 {1,S} {2,S} {3,D}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.21383,0.0849652,-0.000291805,7.48629e-07,-6.60823e-10,-80073.1,12.4536], Tmin=(10,'K'), Tmax=(400.54,'K')),
            NASAPolynomial(coeffs=[-0.364314,0.0693851,-4.1293e-05,1.18286e-08,-1.31071e-12,-79374.9,31.5805], Tmin=(400.54,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-665.794,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (432.353,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 2, 'C-H': 10, 'C-O': 4, 'C=O': 1}
1D rotors:
pivots: [1, 2], dihedral: [9, 1, 2, 3], rotor symmetry: 3, max scan energy: 12.90 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 29.18 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 38.08 kJ/mol
pivots: [4, 6], dihedral: [3, 4, 6, 7], rotor symmetry: 1, max scan energy: 38.09 kJ/mol
pivots: [6, 7], dihedral: [4, 6, 7, 8], rotor symmetry: 1, max scan energy: 29.18 kJ/mol
pivots: [7, 8], dihedral: [6, 7, 8, 16], rotor symmetry: 3, max scan energy: 12.90 kJ/mol


External symmetry: 2, optical isomers: 1

Geometry:
C       3.42404762   -0.76070580   -0.00022962
C       2.33446522    0.28238030   -0.00042368
O       1.07679774   -0.40807442   -0.00029739
C       0.00000000    0.37035101   -0.00046768
O      -0.00000005    1.57264299   -0.00066704
O      -1.07679771   -0.40807446   -0.00029494
C      -2.33446519    0.28238027   -0.00041798
C      -3.42404761   -0.76070581   -0.00023563
H       3.35620648   -1.39430647   -0.88518442
H       4.39927411   -0.27144559   -0.00032488
H       3.35621515   -1.39397119    0.88496578
H       2.38442587    0.92356529   -0.88266226
H       2.38442747    0.92389643    0.88157415
H      -2.38442928    0.92388815    0.88158583
H      -2.38442397    0.92357354   -0.88265057
H      -3.35621513   -1.39398109    0.88495268
H      -3.35620650   -1.39429659   -0.88519752
H      -4.39927408   -0.27144558   -0.00032557
""",
)

entry(
    index = 106,
    label = "COC[CH]OC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {6,S} {12,S} {13,S} {14,S}
4  C u1 p0 c0 {1,S} {6,S} {15,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {3,S} {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
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
    index = 107,
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
    index = 108,
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
    index = 109,
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
    index = 110,
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
    index = 111,
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
    index = 112,
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
    index = 113,
    label = "[Li]N=[C]C",
    molecule = 
"""
multiplicity 2
1 C  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C  u1 p0 c0 {1,S} {3,D}
3 N  u0 p1 c0 {2,D} {7,S}
4 H  u0 p0 c0 {1,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {1,S}
7 Li u0 p0 c0 {3,S}
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
    index = 114,
    label = "[Li]N=CC",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C  u0 p0 c0 {1,S} {3,D} {7,S}
3 N  u0 p1 c0 {2,D} {8,S}
4 H  u0 p0 c0 {1,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {1,S}
7 H  u0 p0 c0 {2,S}
8 Li u0 p0 c0 {3,S}
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
    index = 115,
    label = "[Li]OC[=O]OCCO[C]1OCCO1",
    molecule = 
"""
multiplicity 2
1  O  u0 p2 c0 {8,S} {11,S}
2  O  u0 p2 c0 {9,S} {11,S}
3  O  u0 p2 c0 {10,S} {11,S}
4  O  u0 p2 c0 {7,S} {12,S}
5  O  u0 p2 c0 {12,S} {13,S}
6  O  u0 p2 c0 {12,D}
7  C  u0 p0 c0 {4,S} {8,S} {14,S} {15,S}
8  C  u0 p0 c0 {1,S} {7,S} {16,S} {17,S}
9  C  u0 p0 c0 {2,S} {10,S} {18,S} {19,S}
10 C  u0 p0 c0 {3,S} {9,S} {20,S} {21,S}
11 C  u1 p0 c0 {1,S} {2,S} {3,S}
12 C  u0 p0 c0 {4,S} {5,S} {6,D}
13 Li u0 p0 c0 {5,S}
14 H  u0 p0 c0 {7,S}
15 H  u0 p0 c0 {7,S}
16 H  u0 p0 c0 {8,S}
17 H  u0 p0 c0 {8,S}
18 H  u0 p0 c0 {9,S}
19 H  u0 p0 c0 {9,S}
20 H  u0 p0 c0 {10,S}
21 H  u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.75158,0.138374,-0.000562608,1.53257e-06,-1.46938e-09,-121666,18.4317], Tmin=(10,'K'), Tmax=(355.521,'K')),
            NASAPolynomial(coeffs=[0.455181,0.0918228,-6.07855e-05,1.8852e-08,-2.2181e-12,-121045,33.5695], Tmin=(355.521,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-1011.64,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (507.183,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'Li-O': 1, 'C-O': 9, 'C-C': 2, 'C=O': 1, 'C-H': 8}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason:
* Invalidated! pivots: [3, 5], dihedral: [2, 3, 5, 6], invalidation reason:
* Invalidated! pivots: [5, 6], dihedral: [3, 5, 6, 7], invalidation reason:
* Invalidated! pivots: [6, 7], dihedral: [5, 6, 7, 8], invalidation reason:
* Invalidated! pivots: [7, 8], dihedral: [6, 7, 8, 9], invalidation reason:
* Invalidated! pivots: [8, 9], dihedral: [7, 8, 9, 10], invalidation reason:


External symmetry: 1, optical isomers: 2

Geometry:
Li      5.62009559    0.53270775   -0.31124866
O       3.83849498    1.08783719   -0.36393360
C       3.64651509   -0.11482735   -0.03518832
O       4.57897270   -0.93722777    0.13040618
O       2.39988517   -0.56740056    0.15442057
C       1.34327791    0.36673511   -0.02961815
C       0.06552619   -0.38583481    0.26312151
O      -0.99961577    0.53272354    0.05769874
C      -2.21059471    0.08239610    0.44428208
O      -3.15131544    1.07256915    0.44240307
C      -4.30598986    0.59712964   -0.24369464
C      -4.08795727   -0.90834530   -0.26622473
O      -2.67301295   -1.00677064   -0.26639919
H       1.34254288    0.74819764   -1.05241188
H       1.45788217    1.21429473    0.64804844
H       0.05603550   -0.74636783    1.29559775
H      -0.03725521   -1.24381169   -0.40653498
H      -4.32802149    1.02410033   -1.25038113
H      -5.19694003    0.90363788    0.30304886
H      -4.47117068   -1.39641250   -1.16043119
H      -4.49982055   -1.39251146    0.62475375
""",
)

entry(
    index = 116,
    label = "O=[C]OC[F]C[F]O[Li]",
    molecule = 
"""
multiplicity 2
1  F  u0 p3 c0 {6,S}
2  F  u0 p3 c0 {7,S}
3  O  u0 p2 c0 {6,S} {8,S}
4  O  u0 p2 c0 {7,S} {9,S}
5  O  u0 p2 c0 {8,D}
6  C  u0 p0 c0 {1,S} {3,S} {7,S} {10,S}
7  C  u0 p0 c0 {2,S} {4,S} {6,S} {11,S}
8  C  u1 p0 c0 {3,S} {5,D}
9  Li u0 p0 c0 {4,S}
10 H  u0 p0 c0 {6,S}
11 H  u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.3912,0.0628009,-8.24794e-05,6.5321e-08,-2.26929e-11,-105863,14.473], Tmin=(10,'K'), Tmax=(654.939,'K')),
            NASAPolynomial(coeffs=[7.37629,0.0384622,-2.67369e-05,8.58024e-09,-1.03413e-12,-106385,-3.06621], Tmin=(654.939,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-880.201,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'C-C': 1, 'C-H': 2, 'C-F': 2, 'C-O': 3, 'Li-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: 
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Another conformer for O=[C]OC[F]C[F]O[Li] exists which is 0.94 kJ/mol lower.
* Invalidated! pivots: [4, 6], dihedral: [3, 4, 6, 7], invalidation reason: Another conformer for O=[C]OC[F]C[F]O[Li] exists which is 6.23 kJ/mol lower. But unable to propose troubleshooting methods.
* Invalidated! pivots: [6, 8], dihedral: [4, 6, 8, 9], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.99508314   -0.71424534    0.23117819
C      -2.09633350   -0.11258515   -0.22460767
O      -0.84280654   -0.08982312    0.22765934
C       0.07552098    0.70877929   -0.48914829
F       0.13570435    1.93111131    0.09481565
C       1.43114838    0.00119668   -0.47859152
F       1.69540623   -0.10507473    1.11798345
O       1.43918985   -1.18617766   -0.92650102
Li      1.41928113   -1.87602247    0.74687257
H      -0.26847996    0.83143348   -1.51954770
H       2.24595864    0.69415361   -0.73291377
""",
)

entry(
    index = 117,
    label = "[CH3]",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9921,0.000373272,9.29867e-06,-1.0512e-08,3.94584e-12,16361.2,0.199303], Tmin=(10,'K'), Tmax=(673.422,'K')),
            NASAPolynomial(coeffs=[3.18361,0.00517559,-1.39825e-06,7.77221e-11,1.44999e-14,16470.1,3.78012], Tmin=(673.422,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (136.032,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 3}

External symmetry: 6, optical isomers: 1

Geometry:
C       0.00000000    0.00000000    0.00000000
H       1.07953380    0.00000000    0.00000000
H      -0.53976690    0.93490370    0.00000000
H      -0.53976690   -0.93490370    0.00000000
""",
)

entry(
    index = 118,
    label = "[Li]OC[=O]OC",
    molecule = 
"""
1 O  u0 p2 c0 {4,S} {5,S}
2 O  u0 p2 c0 {5,S} {6,S}
3 O  u0 p2 c0 {5,D}
4 C  u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,D}
6 Li u0 p0 c0 {2,S}
7 H  u0 p0 c0 {4,S}
8 H  u0 p0 c0 {4,S}
9 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65963,0.0337136,-6.80364e-05,1.5491e-07,-1.3672e-10,-86561.4,9.89951], Tmin=(10,'K'), Tmax=(405.141,'K')),
            NASAPolynomial(coeffs=[2.52777,0.0330551,-2.17863e-05,6.71104e-09,-7.84865e-13,-86372.5,15.536], Tmin=(405.141,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-719.719,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (199.547,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 3, 'C-O': 3, 'Li-O': 1, 'C=O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 4]]) broke during the scan.Bond ([[1, 2]]) broke during the scan.The rotor scan has a barrier of 352.57 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
pivots: [3, 5], dihedral: [2, 3, 5, 6], rotor symmetry: 2, max scan energy: 39.88 kJ/mol
pivots: [5, 6], dihedral: [3, 5, 6, 7], rotor symmetry: 3, max scan energy: 3.18 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
Li      2.32284747   -0.71573642    0.00039492
O       1.39854286    0.88820375   -0.00012639
C       0.40349369    0.12323511   -0.00002685
O       0.50524016   -1.13574728    0.00020648
O      -0.80375439    0.69941157   -0.00010632
C      -1.92343462   -0.17595307   -0.00000070
H      -1.92341418   -0.80989255    0.88723880
H      -1.92326021   -0.81030876   -0.88694064
H      -2.80117178    0.46706031   -0.00022479
""",
)

entry(
    index = 119,
    label = "CC=O",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {2,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97375,0.00138089,3.93603e-05,-5.68697e-08,2.65344e-11,-21440,7.3352], Tmin=(10,'K'), Tmax=(553.447,'K')),
            NASAPolynomial(coeffs=[1.46376,0.019522,-9.80819e-06,2.35832e-09,-2.20271e-13,-21162.2,17.9595], Tmin=(553.447,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-178.276,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (153.818,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 1, 'C-H': 4, 'C=O': 1}
1D rotors:
pivots: [1, 2], dihedral: [4, 1, 2, 3], rotor symmetry: 3, max scan energy: 4.57 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       1.16318107   -0.14751851   -0.00000730
C      -0.23352905    0.39621664   -0.00003398
O      -1.22714130   -0.27637258   -0.00053479
H       1.69804729    0.22679869   -0.87683072
H       1.69634923    0.22329875    0.87936235
H       1.15401286   -1.23577865   -0.00206977
H      -0.31081906    1.50446595    0.00052493
""",
)

entry(
    index = 120,
    label = "O=C[[Li]]O[Li]",
    molecule = 
"""
1 O  u0 p2 c0 {3,S} {5,S}
2 O  u0 p2 c0 {3,D}
3 C  u0 p0 c0 {1,S} {2,D} {4,S}
4 Li u0 p0 c0 {3,S}
5 Li u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88159,0.00771836,7.57875e-05,-2.02617e-07,1.48082e-10,-48995.3,8.1825], Tmin=(10,'K'), Tmax=(500.259,'K')),
            NASAPolynomial(coeffs=[5.95115,0.0139078,-1.09482e-05,3.82629e-09,-4.90478e-13,-49486.9,-3.21214], Tmin=(500.259,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-407.398,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'C-Li': 1, 'Li-O': 1, 'C-O': 1}
1D rotors:
* Invalidated! pivots: [2, 4], dihedral: [1, 2, 4, 5], invalidation reason: Bond ([[1, 5]]) broke during the scan.Bond ([[4, 5]]) broke during the scan.Significant difference observed between consecutive conformersBond ([[1, 3]]) broke during the scan.Bond ([[2, 3]]) broke during the scan.The rotor scan has a barrier of 2070.99 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 1, optical isomers: 1

Geometry:
O       0.75497260   -0.61072885   -0.00002187
C       0.05436362    0.56031792    0.00000135
Li      1.96480243    0.68669106    0.00004198
O      -1.19360227    0.44434888   -0.00000444
Li     -0.90443243   -1.36406578    0.00005362
""",
)

entry(
    index = 121,
    label = "CCC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9555,0.00251688,7.99058e-05,-1.28495e-07,6.74156e-11,-14245.8,6.71064], Tmin=(10,'K'), Tmax=(490.12,'K')),
            NASAPolynomial(coeffs=[0.0397609,0.0344763,-1.79115e-05,4.56543e-09,-4.60215e-13,-13862,22.8092], Tmin=(490.12,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-118.47,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (249.434,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 2, 'C-H': 8}
1D rotors:
pivots: [1, 2], dihedral: [4, 1, 2, 3], rotor symmetry: 3, max scan energy: 12.38 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 9], rotor symmetry: 3, max scan energy: 12.38 kJ/mol


External symmetry: 2, optical isomers: 1

Geometry:
C       1.26788914    0.00008019    0.25915408
C       0.00000000    0.00000000   -0.58546348
C      -1.26788914   -0.00008019    0.25915408
H       1.30983724   -0.88179406    0.90358697
H       1.30919298    0.88126682    0.90457183
H       2.16594743    0.00076862   -0.36150799
H       0.00013165   -0.87456627   -1.24300454
H      -0.00013165    0.87456627   -1.24300454
H      -1.30983724    0.88179406    0.90358697
H      -2.16594743   -0.00076862   -0.36150799
H      -1.30919298   -0.88126682    0.90457183
""",
)

entry(
    index = 122,
    label = "C[CH]C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {2,S} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70959,0.033803,-0.000160338,4.46071e-07,-3.88977e-10,8800.49,8.16573], Tmin=(10,'K'), Tmax=(422.78,'K')),
            NASAPolynomial(coeffs=[-0.140949,0.0317626,-1.66053e-05,4.19316e-09,-4.12474e-13,9469.9,27.4936], Tmin=(422.78,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (73.1627,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (224.491,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 2, 'C-H': 7}
1D rotors:
pivots: [1, 2], dihedral: [4, 1, 2, 3], rotor symmetry: 3, max scan energy: 2.70 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 1 2 3 7 F
pivots: [2, 3], dihedral: [1, 2, 3, 8], rotor symmetry: 3, max scan energy: 2.34 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 6 1 2 7 F


External symmetry: 1, optical isomers: 1

Geometry:
C      -0.00558570   -0.19802489    1.29032381
C       0.04795234    0.53462521    0.00000000
C      -0.00558570   -0.19802489   -1.29032381
H       0.71430070   -1.02392781    1.31222296
H       0.20037673    0.45369679    2.14008322
H      -0.99363379   -0.65173352    1.45969561
H      -0.06296657    1.61218397    0.00000000
H      -0.99363379   -0.65173352   -1.45969561
H       0.20037673    0.45369679   -2.14008322
H       0.71430070   -1.02392781   -1.31222296
""",
)

entry(
    index = 123,
    label = "CC",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.02909,-0.00171795,4.64246e-05,-5.51505e-08,2.12057e-11,-11481.6,3.50873], Tmin=(10,'K'), Tmax=(710.393,'K')),
            NASAPolynomial(coeffs=[-0.457388,0.0249474,-1.28427e-05,3.24976e-09,-3.25064e-13,-10879.6,23.37], Tmin=(710.393,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-95.4547,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 1, 'C-H': 6}
1D rotors:
pivots: [1, 2], dihedral: [3, 1, 2, 6], rotor symmetry: 3, max scan energy: 11.17 kJ/mol


External symmetry: 6, optical isomers: 1

Geometry:
C       0.00000000    0.00000000    0.76129868
C       0.00000000    0.00000000   -0.76129868
H       1.01673544    0.00000000    1.15914066
H      -0.50836772    0.88051872    1.15914066
H      -0.50836772   -0.88051872    1.15914066
H      -1.01673544    0.00000000   -1.15914066
H       0.50836772   -0.88051872   -1.15914066
H       0.50836772    0.88051872   -1.15914066
""",
)

entry(
    index = 124,
    label = "CC[C]C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91675,0.00580334,0.000144135,-3.12922e-07,2.26054e-10,-18240.3,7.52097], Tmin=(10,'K'), Tmax=(352.286,'K')),
            NASAPolynomial(coeffs=[0.424514,0.045456,-2.47044e-05,6.59314e-09,-6.93093e-13,-17994.3,20.7255], Tmin=(352.286,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-151.676,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (320.107,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 3, 'C-H': 10}
1D rotors:
pivots: [1, 2], dihedral: [5, 1, 2, 3], rotor symmetry: 3, max scan energy: 13.50 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 9], rotor symmetry: 3, max scan energy: 13.52 kJ/mol
pivots: [2, 4], dihedral: [1, 2, 4, 12], rotor symmetry: 3, max scan energy: 13.52 kJ/mol


External symmetry: 3, optical isomers: 1

Geometry:
C      -0.53495501    1.35032158   -0.09393970
C       0.00005941    0.00012006    0.37354017
C      -0.90164036   -1.13780240   -0.09565549
C       1.43592456   -0.21182966   -0.09693968
H      -1.55341158    1.52070355    0.26250362
H      -0.55309025    1.40105676   -1.18693903
H       0.08832358    2.17217190    0.26573290
H       0.00099078   -0.00072717    1.46999935
H      -0.93515339   -1.17825712   -1.18872455
H      -0.54028404   -2.10496858    0.26113513
H      -1.92547105   -1.00909482    0.26284618
H       2.09325063    0.58656828    0.25484933
H       1.48592497   -0.22534850   -1.19005128
H       1.83766133   -1.16083308    0.26537226
""",
)

entry(
    index = 125,
    label = "C[C][C]C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {2,S} {3,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49941,0.0531143,-0.000214213,5.24497e-07,-4.20957e-10,4342.97,9.46193], Tmin=(10,'K'), Tmax=(446.658,'K')),
            NASAPolynomial(coeffs=[-0.461951,0.0422594,-2.21688e-05,5.62877e-09,-5.57975e-13,5159,30.554], Tmin=(446.658,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (36.1048,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (295.164,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 3, 'C-H': 9}
1D rotors:
pivots: [1, 2], dihedral: [5, 1, 2, 3], rotor symmetry: 3, max scan energy: 4.15 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 8], rotor symmetry: 3, max scan energy: 4.15 kJ/mol
pivots: [2, 4], dihedral: [1, 2, 4, 11], rotor symmetry: 3, max scan energy: 4.15 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       0.84236377    1.21644497   -0.01707990
C      -0.00095504    0.00028515    0.15029730
C       0.63337324   -1.33729782   -0.01372311
C      -1.47620196    0.12069611   -0.01492324
H       1.02122818    1.44399817   -1.08029236
H       0.36895796    2.10055581    0.41679345
H       1.82526950    1.09376963    0.44488499
H       1.62268144   -1.37402473    0.44933956
H       0.77385106   -1.59328387   -1.07623058
H       0.02205705   -2.13153096    0.42160617
H      -1.76621159    0.14718553   -1.07769071
H      -2.00245016   -0.72660453    0.43151853
H      -1.86033912    1.03897366    0.43614190
""",
)

entry(
    index = 126,
    label = "[Li]CCOC",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C  u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C  u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  O  u0 p2 c0 {1,S} {3,S}
5  H  u0 p0 c0 {1,S}
6  H  u0 p0 c0 {1,S}
7  Li u0 p0 c0 {2,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {2,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {3,S}
12 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67451,0.0283481,1.19194e-05,-3.40367e-08,1.55074e-11,-15151.2,9.48544], Tmin=(10,'K'), Tmax=(811.696,'K')),
            NASAPolynomial(coeffs=[3.35157,0.0381668,-2.14291e-05,5.84051e-09,-6.20703e-13,-15369.8,9.30654], Tmin=(811.696,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-126.003,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-Li': 1, 'C-C': 1, 'C-H': 7, 'C-O': 2}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Could not read energies
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Could not read energies
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 10], invalidation reason: Could not read energies


External symmetry: 1, optical isomers: 1

Geometry:
Li     -0.78876416   -1.69187212   -0.00038797
C      -1.85872065    0.01809370    0.00120707
C      -0.52226612    0.66164337    0.00069223
O       0.54673333   -0.40951684   -0.00118316
C       1.85388131    0.09471868   -0.00018107
H      -2.44126130    0.25185673   -0.88935220
H      -2.44006597    0.25091561    0.89279329
H      -0.29778941    1.26016059   -0.89064248
H      -0.29645132    1.25845381    0.89283319
H       2.03965562    0.70789440    0.88999934
H       2.55210169   -0.74316939   -0.00208838
H       2.03951684    0.71176874   -0.88770484
""",
)

entry(
    index = 127,
    label = "O=C[[Li]]OCCO[Li]",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C  u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C  u0 p0 c0 {4,S} {10,D} {11,S}
4  O  u0 p2 c0 {1,S} {3,S}
5  O  u0 p2 c0 {2,S} {12,S}
6  H  u0 p0 c0 {1,S}
7  H  u0 p0 c0 {1,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {2,S}
10 O  u0 p2 c0 {3,D}
11 Li u0 p0 c0 {3,S}
12 Li u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71714,0.0236547,0.000213535,-7.69379e-07,7.94518e-10,-63273.5,12.3183], Tmin=(10,'K'), Tmax=(341.298,'K')),
            NASAPolynomial(coeffs=[5.1882,0.042349,-2.65602e-05,8.10123e-09,-9.57734e-13,-63583.2,3.73653], Tmin=(341.298,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-526.046,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'C-Li': 1, 'C-C': 1, 'C-H': 4, 'C-O': 3, 'Li-O': 1}
1D rotors:
* Invalidated! pivots: [2, 4], dihedral: [1, 2, 4, 5], invalidation reason: Significant difference observed between consecutive conformersThe rotor scan has a barrier of 49.03 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
* Invalidated! pivots: [4, 5], dihedral: [2, 4, 5, 6], invalidation reason: Bond ([[2, 3]]) broke during the scan.Bond ([[2, 3]]) broke during the scan. But unable to propose troubleshooting methods.
pivots: [5, 6], dihedral: [4, 5, 6, 7], rotor symmetry: 1, max scan energy: 92.30 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 2 4 5 10 F
D 5 6 7 8 F
A 6 7 8 F
D 1 2 3 4 F
pivots: [6, 7], dihedral: [5, 6, 7, 8], rotor symmetry: 1, max scan energy: 91.03 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 6 7 8 F
D 4 5 6 11 F
D 2 4 5 9 F
D 1 2 3 4 F


External symmetry: 1, optical isomers: 2

Geometry:
O       2.23319857   -0.56604853   -0.18597208
C       1.62401356    0.47478988    0.13532898
Li      3.52774211    0.66941462    0.05816733
O       0.28420697    0.39853042    0.22761639
C      -0.41916161   -0.84517184   -0.11369408
C      -1.89131030   -0.60284085    0.22169499
O      -2.33819335    0.59477528   -0.25994559
Li     -1.08316521    1.74559144   -0.08943089
H       0.03120207   -1.66894701    0.44172349
H      -0.27504159   -1.00904158   -1.18367401
H      -1.99461454   -0.69143859    1.32450737
H      -2.43582689   -1.47645220   -0.19008551
""",
)

entry(
    index = 128,
    label = "[Li]C",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 Li u0 p0 c0 {1,S}
3 H  u0 p0 c0 {1,S}
4 H  u0 p0 c0 {1,S}
5 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9801,0.00128367,3.8126e-05,-7.82619e-08,5.13076e-11,11242.2,3.06968], Tmin=(10,'K'), Tmax=(472.733,'K')),
            NASAPolynomial(coeffs=[3.24035,0.0114201,-6.33956e-06,1.79439e-09,-2.04304e-13,11268.8,5.62609], Tmin=(472.733,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (93.4689,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 3, 'C-Li': 1}

External symmetry: 3, optical isomers: 1

Geometry:
Li     -1.58833785    0.00000628   -0.00001783
C       0.38564768   -0.00008995    0.00000066
H       0.81718638   -0.83585541   -0.56734642
H       0.81704831   -0.07352483    1.00756488
H       0.81685584    0.90950728   -0.43964241
""",
)

entry(
    index = 129,
    label = "[Li]O",
    molecule = 
"""
1 O  u0 p2 c0 {2,S} {3,S}
2 Li u0 p0 c0 {1,S}
3 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.47737,0.00136998,1.54213e-05,-3.64007e-08,2.39732e-11,-28861.9,3.98038], Tmin=(10,'K'), Tmax=(555.936,'K')),
            NASAPolynomial(coeffs=[4.0159,0.00259657,-1.65256e-06,5.79721e-10,-7.91253e-14,-29000.6,0.989438], Tmin=(555.936,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-239.98,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (54.0441,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'Li-O': 1, 'H-O': 1}

External symmetry: 1, optical isomers: 1

Geometry:
Li      0.00000000   -0.00008010    1.26774229
O       0.00000000    0.00008029   -0.31732408
H       0.00000000   -0.00040212   -1.26461597
""",
)

entry(
    index = 130,
    label = "[Li]OC",
    molecule = 
"""
1 O  u0 p2 c0 {2,S} {3,S}
2 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
3 Li u0 p0 c0 {1,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81392,0.0189919,-7.01616e-05,1.71307e-07,-1.36293e-10,-24814.9,4.91423], Tmin=(10,'K'), Tmax=(458.721,'K')),
            NASAPolynomial(coeffs=[2.03098,0.017522,-9.71089e-06,2.58372e-09,-2.67078e-13,-24472.3,14.0779], Tmin=(458.721,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-206.323,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 3, 'Li-O': 1, 'C-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: not a torsional mode (angles = 179.97, 112.54 degrees)


External symmetry: 3, optical isomers: 1

Geometry:
Li     -2.03074713   -0.00000366    0.00011672
O      -0.44147261   -0.00013270    0.00004692
C       0.92840807    0.00003223    0.00076016
H       1.35096098    0.22197901    0.99618208
H       1.35153283    0.75118522   -0.68878838
H       1.35166500   -0.97255448   -0.30519035
""",
)

entry(
    index = 131,
    label = "[Li]OC=O",
    molecule = 
"""
1 O  u0 p2 c0 {3,S} {4,S}
2 O  u0 p2 c0 {3,D}
3 C  u0 p0 c0 {1,S} {2,D} {5,S}
4 Li u0 p0 c0 {1,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96476,0.00222446,4.9425e-05,-1.03857e-07,6.68737e-11,-59837.8,6.7387], Tmin=(10,'K'), Tmax=(501.15,'K')),
            NASAPolynomial(coeffs=[3.21811,0.0151586,-1.01645e-05,3.18424e-09,-3.77695e-13,-59850.5,8.95115], Tmin=(501.15,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-497.529,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'Li-O': 1, 'C-H': 1, 'C-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 4]]) broke during the scan.Bond ([[1, 2]]) broke during the scan.The rotor scan has a barrier of 505.04 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 2, optical isomers: 1

Geometry:
Li      0.00025902   -1.54247119    0.00000000
O      -1.10529344   -0.02948707    0.00000000
C      -0.00012241    0.57041887    0.00000000
O       1.10525781   -0.02909878    0.00000000
H      -0.00034105    1.67443662    0.00000000
""",
)

entry(
    index = 132,
    label = "[Li]OC=C",
    molecule = 
"""
1 C  u0 p0 c0 {2,D} {3,S} {4,S}
2 C  u0 p0 c0 {1,D} {5,S} {6,S}
3 O  u0 p2 c0 {1,S} {7,S}
4 H  u0 p0 c0 {1,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
7 Li u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98979,0.0116021,8.90767e-06,-1.54016e-08,5.39156e-12,-19251.8,8.93608], Tmin=(10,'K'), Tmax=(1105.97,'K')),
            NASAPolynomial(coeffs=[5.79537,0.014206,-7.01248e-06,1.66253e-09,-1.53777e-13,-20209.8,-2.48221], Tmin=(1105.97,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-160.027,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (153.818,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 3, 'Li-O': 1, 'C=C': 1, 'C-O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 0.09 kJ/mol (set as a FreeRotor)
Troubleshot with the following constraints and 8.0 degrees resolution:
D 1 1 2 3 F


External symmetry: 1, optical isomers: 1

Geometry:
Li      2.41820203   -0.51253326    0.00001356
O       0.92308402    0.09742846   -0.00000753
C      -0.33646448    0.45418498   -0.00007440
C      -1.40272194   -0.35593443   -0.00002042
H      -0.51409438    1.53731982   -0.00000833
H      -1.29276427   -1.43489140    0.00000876
H      -2.40046950    0.06168265    0.00002845
""",
)

entry(
    index = 133,
    label = "[Li]F",
    molecule = 
"""
1 F  u0 p3 c0 {2,S}
2 Li u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.51933,-0.00156062,1.33733e-05,-2.13521e-08,1.08314e-11,-42047.7,4.07628], Tmin=(10,'K'), Tmax=(653.288,'K')),
            NASAPolynomial(coeffs=[3.36888,0.00216887,-1.63791e-06,5.46605e-10,-6.68761e-14,-42087.9,4.27943], Tmin=(653.288,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-349.603,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'F-Li': 1}

External symmetry: 1, optical isomers: 1

Geometry:
Li      0.00000000    0.00000000    1.18031597
F       0.00000000    0.00000000   -0.39337832
""",
)

entry(
    index = 134,
    label = "O=C1OCCO1",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {6,S}
2  O u0 p2 c0 {5,S} {6,S}
3  O u0 p2 c0 {6,D}
4  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
5  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
6  C u0 p0 c0 {1,S} {2,S} {3,D}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.99055,0.000148766,0.000103635,-1.68495e-07,8.70101e-11,-63266.3,10.3612], Tmin=(10,'K'), Tmax=(573.341,'K')),
            NASAPolynomial(coeffs=[-0.753476,0.0415396,-2.63509e-05,7.8793e-09,-8.9718e-13,-62858.6,29.4206], Tmin=(573.341,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-526.038,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 4, 'C-H': 4, 'C=O': 1, 'C-C': 1}

External symmetry: 2, optical isomers: 2

Geometry:
O       0.00000000    0.00000000    2.02874124
C       0.00000000    0.00000000    0.84492828
O       0.09584228    1.10344555    0.07323799
C      -0.10549843    0.75554414   -1.29151098
C       0.10549843   -0.75554414   -1.29151098
O      -0.09584228   -1.10344555    0.07323799
H       0.61399294    1.29615784   -1.90320917
H      -1.11929351    1.03811369   -1.58265706
H      -0.61399294   -1.29615784   -1.90320917
H       1.11929351   -1.03811369   -1.58265706
""",
)

entry(
    index = 135,
    label = "[Li]OC[=O]OC[CH2]",
    molecule = 
"""
multiplicity 2
1  C  u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C  u1 p0 c0 {1,S} {8,S} {9,S}
3  C  u0 p0 c0 {4,S} {5,S} {10,D}
4  O  u0 p2 c0 {1,S} {3,S}
5  O  u0 p2 c0 {3,S} {11,S}
6  H  u0 p0 c0 {1,S}
7  H  u0 p0 c0 {1,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {2,S}
10 O  u0 p2 c0 {3,D}
11 Li u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.47881,0.0534076,-0.000102784,1.90061e-07,-1.5602e-10,-65742.6,14.0882], Tmin=(10,'K'), Tmax=(359.492,'K')),
            NASAPolynomial(coeffs=[4.14301,0.0406641,-2.72754e-05,8.61253e-09,-1.03132e-12,-65755.8,12.0444], Tmin=(359.492,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-546.614,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 1, 'C-H': 4, 'C-O': 3, 'Li-O': 1, 'C=O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 4]]) broke during the scan.Bond ([[1, 2]]) broke during the scan.Significant difference observed between consecutive conformersThe rotor scan has a barrier of 351.55 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
pivots: [3, 5], dihedral: [2, 3, 5, 6], rotor symmetry: 2, max scan energy: 39.39 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 5 6 7 11 F
pivots: [5, 6], dihedral: [3, 5, 6, 7], rotor symmetry: 1, max scan energy: 31.21 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 5 6 7 11 F
pivots: [6, 7], dihedral: [5, 6, 7, 10], rotor symmetry: 1, max scan energy: 2.88 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
Li      2.88086252   -0.47386944   -0.01026535
O       1.76427736    1.00342906    0.01131559
C       0.87133956    0.12208210    0.00246264
O       1.12723228   -1.11466837   -0.01467234
O      -0.39761093    0.54667315    0.01266280
C      -1.41113158   -0.45559307   -0.00059389
C      -2.72766869    0.20896884    0.00196430
H      -1.27879751   -1.09471859   -0.88418908
H      -1.28732738   -1.11626020    0.86651654
H      -2.80002638    1.28140722   -0.10337926
H      -3.62722312   -0.38762000    0.05708010
""",
)

entry(
    index = 136,
    label = "C=C",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.1031,-0.00685262,4.99639e-05,-5.83238e-08,2.24226e-11,5124.75,3.22268], Tmin=(10,'K'), Tmax=(779.267,'K')),
            NASAPolynomial(coeffs=[0.406086,0.0181127,-9.6186e-06,2.51082e-09,-2.57753e-13,5519.11,18.9699], Tmin=(779.267,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (42.6329,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 4, 'C=C': 1}

External symmetry: 4, optical isomers: 1

Geometry:
C       0.66096083    0.00000000    0.00000000
C      -0.66096083    0.00000000    0.00000000
H       1.22953344    0.92300818    0.00000000
H       1.22953344   -0.92300818    0.00000000
H      -1.22953344    0.92300818    0.00000000
H      -1.22953344   -0.92300818    0.00000000
""",
)

entry(
    index = 137,
    label = "CC[=N]N=C=C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {6,D}
3  C u0 p0 c0 {5,D} {10,S} {11,S}
4  N u0 p1 c0 {2,S} {5,D}
5  C u0 p0 c0 {3,D} {4,D}
6  N u0 p1 c0 {2,D} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78428,0.0201195,9.66438e-05,-3.20689e-07,3.33403e-10,27618.8,13.1382], Tmin=(10,'K'), Tmax=(245.061,'K')),
            NASAPolynomial(coeffs=[2.57905,0.0397919,-2.37694e-05,6.88433e-09,-7.72402e-13,27677.9,17.2579], Tmin=(245.061,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (229.643,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 1, 'C-H': 5, 'C=C': 1, 'C=N': 2, 'H-N': 1, 'C-N': 1}
1D rotors:
pivots: [1, 2], dihedral: [7, 1, 2, 3], rotor symmetry: 3, max scan energy: 6.36 kJ/mol
pivots: [2, 4], dihedral: [1, 2, 4, 5], rotor symmetry: 1, max scan energy: 7.15 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 10], invalidation reason: The rotor scan has a barrier of 94.80 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 1, optical isomers: 2

Geometry:
C      -1.37847127   -1.41340293    0.03378849
C      -0.93986496    0.01570330    0.03250379
N      -1.64423417    0.94199296   -0.44844645
N       0.30227369    0.24062686    0.68903495
C       1.39888576    0.15554039    0.17746204
C       2.60939331    0.08787280   -0.30328360
H      -2.36863917   -1.48722542   -0.40828490
H      -1.39541799   -1.80075686    1.05391143
H      -0.67368487   -2.02151918   -0.53809598
H      -1.19008341    1.84635588   -0.33999760
H       3.06491968    0.96157390   -0.74623564
H       3.15581166   -0.84329251   -0.26558605
""",
)

entry(
    index = 138,
    label = "[Li]N=C[C][Li]",
    molecule = 
"""
1 N  u0 p1 c0 {3,D} {5,S}
2 C  u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
3 C  u0 p0 c0 {1,D} {2,S} {4,S}
4 Li u0 p0 c0 {3,S}
5 Li u0 p0 c0 {1,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {2,S}
8 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82824,0.0193927,0.000180601,-1.19147e-06,2.18576e-09,25583.7,8.44129], Tmin=(10,'K'), Tmax=(197.937,'K')),
            NASAPolynomial(coeffs=[4.61812,0.0243762,-1.58953e-05,4.95773e-09,-5.91561e-13,25511.4,4.87352], Tmin=(197.937,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (212.862,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-Li': 1, 'C-C': 1, 'C-H': 3, 'C=N': 1, 'Li-N': 1}
1D rotors:
pivots: [3, 4], dihedral: [2, 3, 4, 6], rotor symmetry: 3, max scan energy: 4.75 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
Li      2.10726932   -1.37700481   -0.00002079
N       0.88438735   -0.15432569   -0.00001100
C      -0.21865632    0.49230067    0.00000953
C      -1.52511016   -0.26520634    0.00000534
Li      1.18385479    1.71801259    0.00000662
H      -2.11776614    0.01877747    0.87522761
H      -1.36935001   -1.35514370   -0.00002790
H      -2.11778691    0.01882583   -0.87518739
""",
)

entry(
    index = 139,
    label = "O=C1OC[F]C[F]O1",
    molecule = 
"""
1  F u0 p3 c0 {6,S}
2  F u0 p3 c0 {7,S}
3  O u0 p2 c0 {6,S} {8,S}
4  O u0 p2 c0 {7,S} {8,S}
5  O u0 p2 c0 {8,D}
6  C u0 p0 c0 {1,S} {3,S} {7,S} {9,S}
7  C u0 p0 c0 {2,S} {4,S} {6,S} {10,S}
8  C u0 p0 c0 {3,S} {4,S} {5,D}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8934,0.00672172,0.000138003,-2.92755e-07,1.88563e-10,-114957,12.1946], Tmin=(10,'K'), Tmax=(505.719,'K')),
            NASAPolynomial(coeffs=[2.04291,0.0422318,-2.92352e-05,9.3241e-09,-1.1156e-12,-115037,17.2215], Tmin=(505.719,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-955.836,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'C-C': 1, 'C-H': 2, 'C-F': 2, 'C-O': 4}

External symmetry: 2, optical isomers: 2

Geometry:
O       0.00000000    0.00000000    2.45461711
C       0.00000000    0.00000000    1.27957634
O      -0.71198850    0.85244613    0.49169691
C      -0.36680201    0.67192716   -0.84098132
F       0.48117043    1.66168311   -1.23273358
C       0.36680201   -0.67192716   -0.84098132
F      -0.48117043   -1.66168311   -1.23273358
O       0.71198850   -0.85244613    0.49169691
H      -1.25824692    0.69526148   -1.46572027
H       1.25824692   -0.69526148   -1.46572027
""",
)

entry(
    index = 140,
    label = "COC[=O]OC",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {6,S}
2  O u0 p2 c0 {5,S} {6,S}
3  O u0 p2 c0 {6,D}
4  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
5  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
6  C u0 p0 c0 {1,S} {2,S} {3,D}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.44337,0.063853,-0.000311288,9.22967e-07,-9.08041e-10,-71200,9.56899], Tmin=(10,'K'), Tmax=(361.212,'K')),
            NASAPolynomial(coeffs=[0.170896,0.0482897,-3.15411e-05,9.62579e-09,-1.11542e-12,-70625.6,26.7023], Tmin=(361.212,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-592.025,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (266.063,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 6, 'C-O': 4, 'C=O': 1}
1D rotors:
pivots: [1, 2], dihedral: [7, 1, 2, 3], rotor symmetry: 3, max scan energy: 3.12 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 39.91 kJ/mol
pivots: [3, 5], dihedral: [2, 3, 5, 6], rotor symmetry: 1, max scan energy: 39.94 kJ/mol
pivots: [5, 6], dihedral: [3, 5, 6, 10], rotor symmetry: 3, max scan energy: 3.12 kJ/mol


External symmetry: 2, optical isomers: 1

Geometry:
C       2.32090289    0.01204504    0.00086367
O       1.07661808    0.70812071   -0.00356624
C       0.00012937   -0.07073352   -0.00015784
O       0.00026658   -1.27234766    0.00586379
O      -1.07667375    0.70785679   -0.00448468
C      -2.32115353    0.01203211   -0.00118002
H       2.41143206   -0.61720003   -0.88448534
H       2.40949993   -0.60919763    0.89203265
H       3.08680621    0.78300511   -0.00183520
H      -2.41138350   -0.60835526    0.89043824
H      -2.41086360   -0.61796989   -0.88607785
H      -3.08706365    0.78306903   -0.00564580
""",
)

entry(
    index = 141,
    label = "[Li]CO[Li]",
    molecule = 
"""
1 O  u0 p2 c0 {2,S} {4,S}
2 C  u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3 Li u0 p0 c0 {2,S}
4 Li u0 p0 c0 {1,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91901,0.00497191,7.27376e-05,-1.62326e-07,1.05103e-10,-9964,7.19319], Tmin=(10,'K'), Tmax=(537.507,'K')),
            NASAPolynomial(coeffs=[4.51416,0.018052,-1.26263e-05,4.15341e-09,-5.15739e-13,-10280.9,2.33858], Tmin=(537.507,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-82.8728,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'Li-O': 1, 'C-H': 2, 'C-Li': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 2]]) broke during the scan.Bond ([[2, 4]]) broke during the scan.Significant difference observed between consecutive conformersBond ([[1, 3]]) broke during the scan.The rotor scan has a barrier of 317.06 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 1, optical isomers: 1

Geometry:
Li      1.62038376    0.41426065    0.00059896
O      -0.04564533    0.67442529   -0.00105888
C      -0.04123245   -0.79341812   -0.00032065
Li     -1.69621568    0.18733688    0.00292420
H       0.41643095   -1.22068608   -0.91211129
H       0.41863360   -1.21978630    0.91092871
""",
)

entry(
    index = 142,
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
            NASAPolynomial(coeffs=[3.96143,0.00513955,0.000499945,-3.42477e-06,8.48573e-09,-50805.2,8.45065], Tmin=(10,'K'), Tmax=(101.008,'K')),
            NASAPolynomial(coeffs=[3.07737,0.0401421,-1.97492e-05,4.59678e-09,-4.1084e-13,-50787.4,10.6892], Tmin=(101.008,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-418.235,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (295.164,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 1, 'C-H': 7, 'Li-O': 1, 'C-O': 3}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 85.02 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 1 2 3 F
D 7 3 4 5 F
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 91.63 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 1 2 3 F
D 1 2 3 4 F
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformersSignificant difference observed between consecutive conformersSignificant difference observed between consecutive conformersSignificant difference observed between consecutive conformersBond ([[3, 4]]) broke during the scan.Bond ([[4, 5]]) broke during the scan.Bond ([[5, 6]]) broke during the scan.Bond ([[2, 3]]) broke during the scan.Bond ([[6, 11]]) broke during the scan.Bond ([[6, 12]]) broke during the scan.Significant difference observed between consecutive conformersBond ([[1, 2]]) broke during the scan.The rotor scan has a barrier of 348.59 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
pivots: [5, 6], dihedral: [4, 5, 6, 11], rotor symmetry: 3, max scan energy: 8.75 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
Li     -0.50204033   -1.71201867   -0.01197927
O      -1.82725197   -0.65390924    0.17698570
C      -1.42062051    0.59302371   -0.20035201
C       0.03195809    0.85599195    0.19709190
O       0.81836014   -0.27891994   -0.22327680
C       2.19399634   -0.11908863    0.02873179
H      -1.49374024    0.76023729   -1.29602827
H      -2.00964480    1.41194334    0.25890025
H       0.12404112    0.94068322    1.28796045
H       0.44007732    1.76064838   -0.27122171
H       2.38634303    0.02764608    1.09820917
H       2.59281296    0.74087696   -0.51915049
H       2.70793547   -1.01957840   -0.30863091
""",
)

entry(
    index = 143,
    label = "O=C1OCC[F]O1",
    molecule = 
"""
1  F u0 p3 c0 {6,S}
2  O u0 p2 c0 {5,S} {7,S}
3  O u0 p2 c0 {6,S} {7,S}
4  O u0 p2 c0 {7,D}
5  C u0 p0 c0 {2,S} {6,S} {8,S} {9,S}
6  C u0 p0 c0 {1,S} {3,S} {5,S} {10,S}
7  C u0 p0 c0 {2,S} {3,S} {4,D}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93652,0.00372746,0.000114456,-2.09095e-07,1.18308e-10,-89782.7,11.9498], Tmin=(10,'K'), Tmax=(548.823,'K')),
            NASAPolynomial(coeffs=[0.33967,0.04313,-2.92795e-05,9.28495e-09,-1.11263e-12,-89586.5,25.3351], Tmin=(548.823,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-746.522,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'C-C': 1, 'C-H': 3, 'C-F': 1, 'C-O': 4}

External symmetry: 1, optical isomers: 2

Geometry:
O       2.21942094   -0.51083929    0.19672656
C       1.11852571   -0.12814852    0.01573705
O       0.66424821    1.11211148    0.26729112
C      -0.67853334    1.23412951   -0.17732499
C      -1.09649449   -0.20837896   -0.42649102
F      -1.81744135   -0.69088820    0.63180528
O       0.11116958   -0.89049482   -0.50598659
H      -1.28041675    1.69887025    0.60070456
H      -0.70652833    1.83158788   -1.08975877
H      -1.67764289   -0.38709985   -1.33001777
""",
)

entry(
    index = 144,
    label = "[Li]C[CH2]",
    molecule = 
"""
multiplicity 2
1 C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C  u1 p0 c0 {1,S} {6,S} {7,S}
3 Li u0 p0 c0 {1,S}
4 H  u0 p0 c0 {1,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95128,0.00282043,6.53372e-05,-1.22111e-07,6.95264e-11,23119.7,5.88292], Tmin=(10,'K'), Tmax=(573.877,'K')),
            NASAPolynomial(coeffs=[2.82678,0.021943,-1.41413e-05,4.48366e-09,-5.49332e-13,23062.9,9.06451], Tmin=(573.877,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (192.207,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-Li': 1, 'C-C': 1, 'C-H': 4}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 6], invalidation reason: Significant difference observed between consecutive conformersCould not read energies


External symmetry: 2, optical isomers: 1

Geometry:
Li      0.00366262   -1.66871245   -0.00002205
C      -0.71336755    0.25370452    0.00000156
C       0.71248746    0.25674866    0.00000473
H      -1.25257207    0.48358367    0.91506289
H      -1.25256202    0.48361961   -0.91505506
H       1.25064695    0.48859087    0.91516706
H       1.25066000    0.48864615   -0.91513703
""",
)

entry(
    index = 145,
    label = "[Li]CCO",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C  u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 O  u0 p2 c0 {1,S} {9,S}
4 H  u0 p0 c0 {1,S}
5 H  u0 p0 c0 {1,S}
6 Li u0 p0 c0 {2,S}
7 H  u0 p0 c0 {2,S}
8 H  u0 p0 c0 {2,S}
9 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90776,0.00587833,0.000107563,-2.37904e-07,1.59106e-10,-16923.9,7.94053], Tmin=(10,'K'), Tmax=(499.767,'K')),
            NASAPolynomial(coeffs=[3.42114,0.028742,-1.79937e-05,5.52922e-09,-6.58615e-13,-17112.2,7.58065], Tmin=(499.767,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-140.738,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-Li': 1, 'C-C': 1, 'C-H': 4, 'H-O': 1, 'C-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Could not read energies
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 9], invalidation reason: Could not read energies


External symmetry: 1, optical isomers: 1

Geometry:
Li      0.11826891   -1.65503647    0.00098611
C      -1.26331591   -0.17285088    0.00161050
C      -0.07865549    0.71593633   -0.00110983
O       1.17948562   -0.15392308   -0.00087985
H      -1.87957795   -0.06535860   -0.89033965
H      -1.87799433   -0.06229563    0.89424289
H       0.02335970    1.33698323   -0.89579065
H       0.02530497    1.33993947    0.89125063
H       1.96830926    0.38839126   -0.00909126
""",
)

entry(
    index = 146,
    label = "[Li]OC[=O]O[Li]",
    molecule = 
"""
1 O  u0 p2 c0 {4,S} {5,S}
2 O  u0 p2 c0 {4,S} {6,S}
3 O  u0 p2 c0 {4,D}
4 C  u0 p0 c0 {1,S} {2,S} {3,D}
5 Li u0 p0 c0 {1,S}
6 Li u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87545,0.00795656,9.20967e-05,-2.28079e-07,1.58749e-10,-100789,8.62044], Tmin=(10,'K'), Tmax=(512.584,'K')),
            NASAPolynomial(coeffs=[5.46104,0.0201461,-1.54538e-05,5.28752e-09,-6.66018e-13,-101274,-1.11709], Tmin=(512.584,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-838.04,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'Li-O': 2, 'C=O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 4]]) broke during the scan.Bond ([[1, 2]]) broke during the scan.The rotor scan has a barrier of 620.88 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
* Invalidated! pivots: [3, 5], dihedral: [2, 3, 5, 6], invalidation reason: Bond ([[4, 6]]) broke during the scan.Bond ([[5, 6]]) broke during the scan.The rotor scan has a barrier of 447.96 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 2, optical isomers: 1

Geometry:
Li      1.81487751   -0.88066535   -0.00002361
O       1.12980329    0.79985205    0.00000167
C      -0.00000608    0.23696256    0.00000260
O       0.00003683   -1.11673454    0.00000373
O      -1.12987508    0.79972329   -0.00000453
Li     -1.81495072   -0.88075442   -0.00001058
""",
)

entry(
    index = 147,
    label = "C[CH2]",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,S} {7,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.99459,0.000106529,3.72371e-05,-4.84586e-08,2.04315e-11,13169.6,5.69996], Tmin=(10,'K'), Tmax=(614.749,'K')),
            NASAPolynomial(coeffs=[1.04451,0.0193016,-9.59845e-06,2.33164e-09,-2.23044e-13,13532.3,18.4971], Tmin=(614.749,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (109.494,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (153.818,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 1, 'C-H': 5}
1D rotors:
pivots: [1, 2], dihedral: [3, 1, 2, 6], rotor symmetry: 6, max scan energy: 0.25 kJ/mol (set as a FreeRotor)


External symmetry: 1, optical isomers: 1

Geometry:
C      -0.69131613   -0.00212838    0.00000000
C       0.79074015   -0.01731498    0.00000000
H      -1.10233219   -0.49237476   -0.88521749
H      -1.08740975    1.02387265    0.00000000
H      -1.10233219   -0.49237476    0.88521749
H       1.34752102    0.03693598   -0.92593771
H       1.34752102    0.03693598    0.92593771
""",
)

entry(
    index = 148,
    label = "[Li]O[Li]",
    molecule = 
"""
1 O  u0 p2 c0 {2,S} {3,S}
2 Li u0 p0 c0 {1,S}
3 Li u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97457,0.00399117,0.000122677,-1.41523e-06,4.77471e-09,-18164.1,-4.08005], Tmin=(10,'K'), Tmax=(106.631,'K')),
            NASAPolynomial(coeffs=[4.10859,0.00600987,-4.83844e-06,1.70563e-09,-2.19407e-13,-18171,-4.61446], Tmin=(106.631,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-147.25,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'Li-O': 2}

External symmetry: 2, optical isomers: 1

Geometry:
Li      1.61582311    0.00000000    0.00056511
O       0.00000000    0.00000000   -0.00003394
Li     -1.61582311    0.00000000    0.00056511
""",
)

entry(
    index = 149,
    label = "[Li]N=C=C",
    molecule = 
"""
1 N  u0 p1 c0 {3,D} {4,S}
2 C  u0 p0 c0 {3,D} {5,S} {6,S}
3 C  u0 p0 c0 {1,D} {2,D}
4 Li u0 p0 c0 {1,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92788,0.00450654,6.77786e-05,-1.53421e-07,1.01786e-10,16048.8,7.216], Tmin=(10,'K'), Tmax=(521.655,'K')),
            NASAPolynomial(coeffs=[4.36408,0.0165073,-1.08544e-05,3.46214e-09,-4.24353e-13,15794.5,3.39419], Tmin=(521.655,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (133.415,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'Li-N': 1, 'C-H': 2, 'C=C': 1, 'C=N': 1}

External symmetry: 1, optical isomers: 1

Geometry:
Li     -0.29827609   -1.56389866    0.00136400
N      -1.30168683    0.25133694    0.00060114
C      -0.13234636    0.36772868   -0.00027877
C       1.21430650    0.03586485   -0.00092938
H       1.75750803    0.26012364    0.91069584
H       1.75614259    0.25843064   -0.91378741
""",
)

entry(
    index = 150,
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
            NASAPolynomial(coeffs=[3.96242,0.00211443,3.29383e-05,-6.53611e-08,3.72672e-11,-21080.7,6.65109], Tmin=(10,'K'), Tmax=(614.285,'K')),
            NASAPolynomial(coeffs=[4.30552,0.00915052,-6.87942e-06,2.4187e-09,-3.15771e-13,-21297.7,3.73941], Tmin=(614.285,'K'), Tmax=(3000,'K')),
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
Bond corrections: {'O-O': 1, 'H-O': 1, 'Li-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: The rotor scan has a barrier of 67.19 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 1, optical isomers: 2

Geometry:
Li     -0.68729161   -1.21360920    0.07695217
O      -0.62771604    0.49204238   -0.00516494
O       0.73494537   -0.08631909   -0.09704371
H       1.20180683    0.39642320    0.58672388
""",
)

entry(
    index = 151,
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
            NASAPolynomial(coeffs=[3.98529,0.000791682,1.72084e-05,-3.04004e-08,1.57297e-11,-11542,5.77242], Tmin=(10,'K'), Tmax=(645.86,'K')),
            NASAPolynomial(coeffs=[3.62608,0.00676261,-5.35955e-06,1.87544e-09,-2.39985e-13,-11573.7,6.74348], Tmin=(645.86,'K'), Tmax=(3000,'K')),
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
Bond corrections: {'O-O': 1, 'Li-O': 1}

External symmetry: 2, optical isomers: 1

Geometry:
Li     -0.01445143   -1.37193014    0.00000000
O      -0.65913039    0.26394883    0.00000000
O       0.66445417    0.25009976    0.00000000
""",
)

entry(
    index = 152,
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
            NASAPolynomial(coeffs=[3.90511,0.00562265,0.000114411,-2.27323e-07,1.35289e-10,-66351.2,12.3312], Tmin=(10,'K'), Tmax=(557.367,'K')),
            NASAPolynomial(coeffs=[2.57807,0.0363642,-2.54234e-05,8.23379e-09,-1.00179e-12,-66532.9,15.0011], Tmin=(557.367,'K'), Tmax=(3000,'K')),
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
Bond corrections: {'C=O': 1, 'C-C': 1, 'C-H': 2, 'C-F': 1, 'C-O': 4}

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
    index = 153,
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
            NASAPolynomial(coeffs=[3.99047,0.0004167,3.87572e-05,-6.00196e-08,3.03686e-11,7668.9,5.03807], Tmin=(10,'K'), Tmax=(509.148,'K')),
            NASAPolynomial(coeffs=[1.93367,0.0165754,-8.84789e-06,2.31339e-09,-2.37896e-13,7878.35,13.5726], Tmin=(509.148,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (63.7554,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 1, 'C#N': 1, 'C-H': 3}

External symmetry: 3, optical isomers: 1

Geometry:
N       0.00000000    0.00000000    1.42802996
C       0.00000000    0.00000000    0.28152438
C       0.00000000    0.00000000   -1.17445227
H       1.02399676    0.00000000   -1.54630205
H      -0.51199838   -0.88680721   -1.54630205
H      -0.51199838    0.88680721   -1.54630205
""",
)

entry(
    index = 154,
    label = "COCCOC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {6,S} {14,S} {15,S} {16,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {2,S} {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.08519,0.0735614,-0.000150283,2.07465e-07,-1.07502e-10,-44483,10.4441], Tmin=(10,'K'), Tmax=(635.241,'K')),
            NASAPolynomial(coeffs=[2.31803,0.0498085,-2.67006e-05,6.93465e-09,-7.06715e-13,-43808.8,18.3364], Tmin=(635.241,'K'), Tmax=(3000,'K')),
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
Bond corrections: {'C-C': 1, 'C-H': 10, 'C-O': 4}
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

entry(
    index = 155,
    label = "[Li]O[C]1OCCO1",
    molecule = 
"""
multiplicity 2
1  C  u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C  u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C  u1 p0 c0 {4,S} {5,S} {6,S}
4  O  u0 p2 c0 {1,S} {3,S}
5  O  u0 p2 c0 {2,S} {3,S}
6  O  u0 p2 c0 {3,S} {11,S}
7  H  u0 p0 c0 {1,S}
8  H  u0 p0 c0 {1,S}
9  H  u0 p0 c0 {2,S}
10 H  u0 p0 c0 {2,S}
11 Li u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88962,0.00731162,0.000151084,-3.37194e-07,2.31731e-10,-50946,12.2682], Tmin=(10,'K'), Tmax=(468.222,'K')),
            NASAPolynomial(coeffs=[1.91505,0.04386,-2.90491e-05,9.05049e-09,-1.07084e-12,-50976.8,17.9925], Tmin=(468.222,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-423.609,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 1, 'C-H': 4, 'C-O': 5, 'Li-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[3, 7]]) broke during the scan.Bond ([[1, 4]]) broke during the scan.Bond ([[1, 2]]) broke during the scan.Bond ([[4, 5]]) broke during the scan.The rotor scan has a barrier of 863.52 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 1, optical isomers: 2

Geometry:
Li      1.89243301   -1.29930980   -0.38833720
O       1.89406685    0.45069828   -0.02520738
C       0.69549728    0.38801156    0.36537198
O       0.13095581   -1.04268495    0.19568800
C      -1.24045446   -0.92278094   -0.11016867
C      -1.51319614    0.57637382    0.05759774
O      -0.27284477    1.17402600   -0.23999600
H      -1.84008856   -1.53352967    0.56866627
H      -1.42748461   -1.24602810   -1.13934647
H      -2.25971035    0.95746337   -0.63727419
H      -1.81496743    0.80807388    1.08461155
""",
)

entry(
    index = 156,
    label = "[Li]O[C][OC]OC",
    molecule = 
"""
multiplicity 2
1  O  u0 p2 c0 {4,S} {6,S}
2  O  u0 p2 c0 {5,S} {6,S}
3  O  u0 p2 c0 {6,S} {7,S}
4  C  u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
5  C  u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
6  C  u1 p0 c0 {1,S} {2,S} {3,S}
7  Li u0 p0 c0 {3,S}
8  H  u0 p0 c0 {4,S}
9  H  u0 p0 c0 {4,S}
10 H  u0 p0 c0 {4,S}
11 H  u0 p0 c0 {5,S}
12 H  u0 p0 c0 {5,S}
13 H  u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.28146,0.0700865,-0.000190278,3.64019e-07,-2.63169e-10,-56878.3,12.5356], Tmin=(10,'K'), Tmax=(445.071,'K')),
            NASAPolynomial(coeffs=[3.8262,0.0432879,-2.61418e-05,7.5912e-09,-8.51597e-13,-56709.9,12.7856], Tmin=(445.071,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-472.932,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 6, 'C-O': 5, 'Li-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[1, 4]]) broke during the scan.Bond ([[1, 2]]) broke during the scan.Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformersCould not read energies
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Bond ([[1, 4]]) broke during the scan.Bond ([[1, 2]]) broke during the scan.Significant difference observed between consecutive conformersCould not read energies
* Invalidated! pivots: [3, 6], dihedral: [2, 3, 6, 7], invalidation reason: Bond ([[3, 4]]) broke during the scan.Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformersThe rotor scan has a barrier of 59.02 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
pivots: [4, 5], dihedral: [3, 4, 5, 8], rotor symmetry: 3, max scan energy: 4.72 kJ/mol
pivots: [6, 7], dihedral: [3, 6, 7, 11], rotor symmetry: 3, max scan energy: 5.96 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
Li      1.18715191   -2.02051121   -0.38411947
O      -0.43617201   -1.54874557    0.15690195
C      -0.07680598   -0.32505186    0.30187805
O       1.28920412   -0.15528583   -0.17208134
C       1.89187301    1.08719368    0.12341155
O      -0.82219505    0.68947694   -0.28043782
C      -2.19958765    0.60432772    0.01505613
H       1.78917241    1.31258195    1.18852833
H       2.94845506    1.01268546   -0.13492406
H       1.42909119    1.88705549   -0.45646565
H      -2.37082769    0.65765335    1.09538395
H      -2.67700865    1.45497802   -0.46945828
H      -2.62537388   -0.32725472   -0.36363759
""",
)

