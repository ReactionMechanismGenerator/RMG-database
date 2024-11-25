#!/usr/bin/env python
# encoding: utf-8

name = "2FFOH_coupled_cluster"
shortDesc = ""
longDesc = """
ARC v1.1.0
ARC project 2FFOH_Wang_3

Levels of theory used:

Conformers:       wb97xd/def2svp, software: gaussian
TS guesses:       wb97xd/def2svp, software: gaussian
Optimization:     wb97xd/def2tzvp, software: gaussian (using a fine grid)
Frequencies:      wb97xd/def2tzvp, software: gaussian
Single point:     ccsd(t)-f12/cc-pvtz-f12, software: molpro
Rotor scans:      wb97xd/def2tzvp, software: gaussian
Using p-type bond additivity corrections for thermo

Using the following ESS settings: {'gaussian': ['local'], 'molpro': ['local'], 'orca': ['local']}
"""
entry(
    index = 0,
    label = "benzene_rad",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {8,S}
2  C u0 p0 c0 {1,B} {4,B} {7,S}
3  C u0 p0 c0 {1,B} {5,B} {9,S}
4  C u0 p0 c0 {2,B} {6,B} {10,S}
5  C u0 p0 c0 {3,B} {6,B} {11,S}
6  C u1 p0 c0 {4,B} {5,B}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.21088,-0.0177186,0.000199919,-3.2104e-07,1.66563e-10,36427,9.54195], Tmin=(10,'K'), Tmax=(611.759,'K')),
            NASAPolynomial(coeffs=[-0.902673,0.045727,-2.92305e-05,8.86485e-09,-1.02511e-12,36491.1,27.1092], Tmin=(611.759,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (302.869,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 3, 'C-H': 5, 'C-C': 3}

External symmetry: 2, optical isomers: 1

Geometry:
C       0.15243100   -1.53967400    0.06983000
C      -1.12176800   -1.04063900    0.05161300
C      -1.24637000    0.34696300   -0.01136600
C      -0.11371900    1.14865700   -0.05209600
C       1.15422800    0.58374400   -0.03084500
C       1.30413000   -0.80136300    0.03192900
H      -1.99549800   -1.67932600    0.08395800
H      -2.23188500    0.79663700   -0.02836800
H      -0.22025500    2.22475300   -0.10090100
H       2.03250500    1.21725100   -0.06297000
H       2.28620100   -1.25700400    0.04921600
""",
)

entry(
    index = 1,
    label = "benzene",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {6,B} {7,S}
2  C u0 p0 c0 {1,B} {3,B} {8,S}
3  C u0 p0 c0 {2,B} {4,B} {9,S}
4  C u0 p0 c0 {3,B} {5,B} {10,S}
5  C u0 p0 c0 {4,B} {6,B} {11,S}
6  C u0 p0 c0 {1,B} {5,B} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.23306,-0.0190396,0.000207345,-3.2297e-07,1.62974e-10,5874.74,7.12653], Tmin=(10,'K'), Tmax=(624.488,'K')),
            NASAPolynomial(coeffs=[-1.86972,0.0502321,-3.15389e-05,9.4403e-09,-1.08111e-12,6048.44,28.9835], Tmin=(624.488,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (48.8502,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 3, 'C-H': 6, 'C-C': 3}

External symmetry: 12, optical isomers: 1

Geometry:
C      -1.23842300    0.62478800   -0.01986100
C      -0.07790700    1.38479200   -0.02983000
C       1.16052200    0.75997500   -0.00996600
C       1.23842300   -0.62478800    0.01986100
C       0.07790700   -1.38479200    0.02983000
C      -1.16052200   -0.75997500    0.00996600
H      -2.20514300    1.11243600   -0.03537600
H      -0.13874300    2.46568800   -0.05310300
H       2.06640500    1.35318900   -0.01772900
H       2.20514300   -1.11243600    0.03537600
H       0.13874300   -2.46568800    0.05310300
H      -2.06640500   -1.35318900    0.01772900
""",
)

entry(
    index = 2,
    label = "O",
    molecule = 
"""
multiplicity 3
1 O u2 p2 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,-1.5266e-15,6.3226e-18,-7.59355e-21,2.67359e-24,28974.7,4.09131], Tmin=(10,'K'), Tmax=(1363.47,'K')),
            NASAPolynomial(coeffs=[2.5,-1.01797e-13,8.3758e-17,-2.93808e-20,3.72101e-24,28974.7,4.09131], Tmin=(1363.47,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (240.909,'kJ/mol'),
        Cp0 = (20.7862,'J/(mol*K)'),
        CpInf = (20.7862,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
External symmetry: 1, optical isomers: 1

Geometry:
O       0.00000000    0.00000000    0.00000000
""",
)

entry(
    index = 3,
    label = "OH",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49687,0.000183348,-9.92782e-07,1.55941e-09,-6.05155e-13,3374.3,1.47223], Tmin=(10,'K'), Tmax=(985.623,'K')),
            NASAPolynomial(coeffs=[3.45392,-0.000299132,7.41031e-07,-2.89405e-10,3.52755e-14,3414.66,1.84064], Tmin=(985.623,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (28.0545,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1}

External symmetry: 1, optical isomers: 1

Geometry:
O       0.00000000    0.00000000    0.48548100
H       0.00000000    0.00000000   -0.48548100
""",
)

entry(
    index = 4,
    label = "HO2",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.0289,-0.00170018,1.01165e-05,-1.01025e-08,3.29436e-12,451.976,4.66131], Tmin=(10,'K'), Tmax=(938.192,'K')),
            NASAPolynomial(coeffs=[3.02249,0.00428206,-2.15221e-06,5.37047e-10,-5.27981e-14,566.381,9.05576], Tmin=(938.192,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (3.76568,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'O-O': 1, 'H-O': 1}

External symmetry: 1, optical isomers: 1

Geometry:
O       0.99430700   -0.17969800   -0.00000000
O      -0.15947500    0.43943500    0.00000000
H      -0.83483300   -0.25973700    0.00000000
""",
)

entry(
    index = 5,
    label = "H2O2",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97338,0.00194362,7.98529e-06,-1.12854e-08,4.81145e-12,-17305,5.26787], Tmin=(10,'K'), Tmax=(616.442,'K')),
            NASAPolynomial(coeffs=[3.26816,0.00651967,-3.14969e-06,7.56801e-10,-7.22924e-14,-17218,8.32896], Tmin=(616.442,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-143.887,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (78.9875,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 2, 'O-O': 1}
1D rotors:
pivots: [1, 2], dihedral: [3, 1, 2, 4], rotor symmetry: 1, max scan energy: 33.63 kJ/mol


External symmetry: 2, optical isomers: 2

Geometry:
O       0.59487700   -0.38533200    0.26580100
O      -0.59173700    0.40285500    0.24609700
H       1.18650100    0.15393200   -0.26880300
H      -1.18964000   -0.17145500   -0.24309300
""",
)

entry(
    index = 6,
    label = "CH3",
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
            NASAPolynomial(coeffs=[3.99123,0.000427466,9.38106e-06,-1.09444e-08,4.26312e-12,16164.4,0.205279], Tmin=(10,'K'), Tmax=(646.753,'K')),
            NASAPolynomial(coeffs=[3.24886,0.00501883,-1.26762e-06,3.21873e-11,2.01591e-14,16260.4,3.46326], Tmin=(646.753,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (134.395,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 3}

External symmetry: 6, optical isomers: 1

Geometry:
C      -0.00000000   -0.00000000   -0.00000000
H       1.06382500   -0.17469000    0.05400800
H      -0.68333900   -0.83511700   -0.02800500
H      -0.38048600    1.00980700   -0.02600400
""",
)

entry(
    index = 7,
    label = "CH4",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.04144,-0.00248006,1.13131e-05,3.67747e-09,-9.36777e-12,-10252.5,-0.426398], Tmin=(10,'K'), Tmax=(616.366,'K')),
            NASAPolynomial(coeffs=[0.682876,0.0116824,-4.57615e-06,7.70488e-10,-3.89508e-14,-9693.48,15.3277], Tmin=(616.366,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-85.229,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 4}

External symmetry: 12, optical isomers: 1

Geometry:
C       0.00000700    0.00000100    0.00000800
H      -0.64862500   -0.77196600   -0.41128900
H      -0.34823800    0.97866500   -0.32671900
H      -0.02227600   -0.04873700    1.08763900
H       1.01913200   -0.15796400   -0.34963800
""",
)

entry(
    index = 8,
    label = "OCH",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u1 p0 c0 {1,D} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.0141,-0.000832495,4.56529e-06,1.88212e-10,-2.65686e-12,3515.46,4.13321], Tmin=(10,'K'), Tmax=(629.048,'K')),
            NASAPolynomial(coeffs=[2.71788,0.00469624,-2.14733e-06,4.44296e-10,-3.31033e-14,3732.23,10.2126], Tmin=(629.048,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (29.2345,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'C-H': 1}

External symmetry: 1, optical isomers: 1

Geometry:
O       1.00371800   -0.23528000    0.11877000
C       0.00832200    0.25306000   -0.25071100
H      -1.01204000   -0.01778000    0.13194100
""",
)

entry(
    index = 9,
    label = "OCH2",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.03209,-0.00195558,9.15987e-06,2.76127e-09,-7.98321e-12,-14682.7,3.46609], Tmin=(10,'K'), Tmax=(595.86,'K')),
            NASAPolynomial(coeffs=[1.42096,0.00951833,-4.48259e-06,9.72091e-10,-7.78374e-14,-14264.1,15.6133], Tmin=(595.86,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-122.068,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 2, 'C=O': 1}

External symmetry: 2, optical isomers: 1

Geometry:
O       1.18411900   -0.06026900    0.09333700
C      -0.00572500    0.00029100   -0.00045100
H      -0.54249300    0.96798100   -0.03328800
H      -0.63590200   -0.90800300   -0.05959800
""",
)

entry(
    index = 10,
    label = "methanol_rad",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.07153,-0.00478852,3.76459e-05,-4.45701e-08,1.73251e-11,978.605,5.39816], Tmin=(10,'K'), Tmax=(768.066,'K')),
            NASAPolynomial(coeffs=[1.27139,0.0140925,-7.62199e-06,2.00757e-09,-2.07148e-13,1281.96,17.343], Tmin=(768.066,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (8.15242,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'C-H': 3}

External symmetry: 1, optical isomers: 1

Geometry:
O       1.29943100    0.08269700   -0.20332900
C      -0.03482600   -0.04031800    0.01015100
H      -0.28115800   -0.40525600    1.01661800
H      -0.43727800    0.98816600   -0.05694700
H      -0.54616900   -0.62528800   -0.76649300
""",
)

entry(
    index = 11,
    label = "methanol",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.0039,-0.000328902,2.33168e-05,-2.46409e-08,8.30671e-12,-25677.4,5.24955], Tmin=(10,'K'), Tmax=(779.147,'K')),
            NASAPolynomial(coeffs=[0.886376,0.0156765,-7.49748e-06,1.72588e-09,-1.53735e-13,-25191.6,19.5117], Tmin=(779.147,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-213.491,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (128.874,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C-H': 3, 'C-O': 1}
1D rotors:
pivots: [1, 2], dihedral: [3, 1, 2, 4], rotor symmetry: 3, max scan energy: 4.59 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O       0.97475300    0.48506700   -0.01381500
C      -0.35614000    0.01841800   -0.00338100
H       1.56443600   -0.26692100    0.03806000
H      -0.59842000   -0.52357600    0.91786100
H      -0.57562900   -0.62834000   -0.86051100
H      -1.00171900    0.89366600   -0.06321500
""",
)

entry(
    index = 12,
    label = "ethane_rad",
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
            NASAPolynomial(coeffs=[3.99168,0.00028158,3.67653e-05,-4.80927e-08,2.03733e-11,12610,5.70396], Tmin=(10,'K'), Tmax=(611.562,'K')),
            NASAPolynomial(coeffs=[1.11148,0.0191195,-9.43847e-06,2.27336e-09,-2.15489e-13,12962.3,18.183], Tmin=(611.562,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (104.84,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (153.818,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 1}
1D rotors:
pivots: [1, 2], dihedral: [3, 1, 2, 5], rotor symmetry: 6, max scan energy: 0.24 kJ/mol (set as a FreeRotor)


External symmetry: 1, optical isomers: 1

Geometry:
C       0.85647800    0.05623900    0.08142200
C      -0.61908500   -0.03586400   -0.01797600
H       1.46191900   -0.83293500    0.19233400
H       1.36642000    0.99541600   -0.08409600
H      -1.01415000   -0.86332800    0.57513800
H      -0.94594000   -0.20959600   -1.05362400
H      -1.10547000    0.88498900    0.31067600
""",
)

entry(
    index = 13,
    label = "ethane",
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
            NASAPolynomial(coeffs=[4.02899,-0.00167052,4.58784e-05,-5.41207e-08,2.0626e-11,-11978.3,3.50591], Tmin=(10,'K'), Tmax=(725.197,'K')),
            NASAPolynomial(coeffs=[-0.462921,0.0249014,-1.27973e-05,3.23384e-09,-3.23097e-13,-11374,23.4079], Tmin=(725.197,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-99.5843,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 6, 'C-C': 1}
1D rotors:
pivots: [1, 2], dihedral: [3, 1, 2, 6], rotor symmetry: 3, max scan energy: 11.20 kJ/mol


External symmetry: 6, optical isomers: 1

Geometry:
C       0.76096700    0.02500300    0.00508800
C      -0.76096700   -0.02500300   -0.00508800
H       1.19039600   -0.92370600   -0.32165200
H       1.13589400    0.80414700   -0.66093000
H       1.14349700    0.23356300    1.00578300
H      -1.13589400   -0.80414700    0.66093000
H      -1.14349700   -0.23356300   -1.00578300
H      -1.19039600    0.92370600    0.32165200
""",
)

entry(
    index = 14,
    label = "furfuryl",
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
            NASAPolynomial(coeffs=[3.85691,0.0249605,3.1236e-05,-5.4466e-08,2.17206e-11,-30328.5,12.447], Tmin=(10,'K'), Tmax=(922.182,'K')),
            NASAPolynomial(coeffs=[5.07028,0.0385125,-2.14116e-05,5.71862e-09,-5.9312e-13,-31352.3,2.35377], Tmin=(922.182,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-252.115,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 2, 'H-O': 1, 'C-O': 3, 'C-H': 5, 'C=C': 2}
1D rotors:
pivots: [1, 2], dihedral: [8, 1, 2, 3], rotor symmetry: 1, max scan energy: 10.43 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 11.99 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.41135500   -0.22549500    0.83384100
C      -1.69351100    0.31298300   -0.26028200
C      -0.22132300    0.14948000   -0.14160700
C       0.80133500    1.00474600    0.08577400
C       1.99256000    0.21529200    0.10937400
C       1.59688100   -1.05812200   -0.10055800
O       0.25573500   -1.11718700   -0.25978300
H      -2.20363000   -1.15935300    0.89901700
H      -2.03782800   -0.12928200   -1.20340300
H      -1.92299900    1.37737800   -0.28713100
H       0.71683300    2.06948500    0.22571700
H       3.00299600    0.55409400    0.26383700
H       2.12430700   -1.99401400   -0.16479700
""",
)

entry(
    index = 15,
    label = "P368",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {5,S}
2 C u0 p0 c0 {1,S} {4,D} {6,S}
3 C u0 p0 c0 {1,D} {7,S} {8,S}
4 C u1 p0 c0 {2,D} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93144,0.00387247,9.08264e-05,-1.64809e-07,9.04653e-11,40261.6,8.14011], Tmin=(10,'K'), Tmax=(596.182,'K')),
            NASAPolynomial(coeffs=[2.11621,0.0323648,-2.19051e-05,7.14721e-09,-8.88305e-13,40188.2,13.5273], Tmin=(596.182,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (334.723,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (203.705,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 1, 'C-H': 5, 'C=C': 2}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 24.76 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C      -1.62246200    0.05671300   -0.10871000
C      -0.38238300    0.30969200    0.29525200
C       0.80731600   -0.19096900   -0.39014400
C       2.04408600    0.03608600   -0.02369400
H      -2.47975300    0.44505000    0.42496800
H      -1.81891200   -0.54773600   -0.98730500
H      -0.21104700    0.91714400    1.17739600
H       0.62944800   -0.80326300   -1.27948300
H       3.03370500   -0.22284200   -0.36644000
""",
)

entry(
    index = 16,
    label = "P367",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {5,S}
2  C u0 p0 c0 {1,S} {4,D} {6,S}
3  C u0 p0 c0 {1,D} {7,S} {8,S}
4  C u0 p0 c0 {2,D} {9,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95298,0.00269446,9.57653e-05,-1.65103e-07,8.89066e-11,10182.8,6.91126], Tmin=(10,'K'), Tmax=(564.567,'K')),
            NASAPolynomial(coeffs=[0.144869,0.0391137,-2.60744e-05,8.38334e-09,-1.02891e-12,10462.4,21.774], Tmin=(564.567,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (84.6437,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (228.648,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 1, 'C-H': 6, 'C=C': 2}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 25.77 kJ/mol


External symmetry: 2, optical isomers: 1

Geometry:
C       1.83343600    0.08472500   -0.10624700
C       0.59933300   -0.40715600   -0.07494500
C      -0.59932200    0.40713900    0.07512300
C      -1.83342400   -0.08474200    0.10642500
H       2.01785200    1.14984300   -0.01908400
H       2.69717100   -0.55720300   -0.21949300
H       0.44654600   -1.47927700   -0.16472700
H      -0.44653500    1.47926100    0.16490500
H      -2.01784000   -1.14986000    0.01926200
H      -2.69715900    0.55718700    0.21967100
""",
)

entry(
    index = 17,
    label = "P2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {6,S}
2  O u0 p2 c0 {7,S} {12,S}
3  C u0 p0 c0 {1,S} {4,S} {7,D}
4  C u0 p0 c0 {3,S} {5,D} {8,S}
5  C u0 p0 c0 {4,D} {6,S} {9,S}
6  C u1 p0 c0 {1,S} {5,S} {11,S}
7  C u0 p0 c0 {2,S} {3,D} {10,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87972,0.00675384,0.00014583,-2.6845e-07,1.47339e-10,-15392.8,11.0414], Tmin=(10,'K'), Tmax=(604.87,'K')),
            NASAPolynomial(coeffs=[1.53809,0.051314,-3.67763e-05,1.22802e-08,-1.53519e-12,-15641.4,16.7645], Tmin=(604.87,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-128.038,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (278.535,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 2, 'H-O': 1, 'C-O': 3, 'C-H': 4, 'C=C': 2}
1D rotors:
pivots: [1, 2], dihedral: [8, 1, 2, 3], rotor symmetry: 1, max scan energy: 25.05 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
O       2.49593500   -0.47869800   -0.49470300
C       1.68460800    0.55711400   -0.19649500
C       2.13805300    1.85408100   -0.07032600
C       1.51632500    3.06485800    0.22329300
C       2.53235500    4.04550600    0.20542400
C       3.69427900    3.40910800   -0.08942400
O       3.47908300    2.07711500   -0.26114700
H       3.39549200   -0.15182100   -0.59503200
H       0.64800700    0.29389300   -0.06317000
H       0.46747200    3.20457900    0.42158100
H       2.42123200    5.10123900    0.38892700
H       4.70958700    3.74401600   -0.20797500
""",
)

entry(
    index = 18,
    label = "furfural",
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
            NASAPolynomial(coeffs=[3.93657,0.00416324,0.000140944,-2.91582e-07,1.92129e-10,-22355.6,11.0446], Tmin=(10,'K'), Tmax=(453.221,'K')),
            NASAPolynomial(coeffs=[0.392182,0.0456107,-2.98772e-05,9.17689e-09,-1.07094e-12,-22138.7,24.1874], Tmin=(453.221,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-185.886,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (253.591,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-H': 4, 'C=O': 1, 'C-C': 2, 'C-O': 2}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 46.40 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O       2.85119400    0.51010200   -0.07350700
C       2.02441100   -0.36590900   -0.08947200
C       0.59014700   -0.12164700   -0.02685000
C      -0.15047800    1.01622700    0.05729000
C      -1.50740400    0.60467800    0.08363200
C      -1.48615900   -0.75085600    0.01348300
O      -0.22795100   -1.20754000   -0.05386400
H       2.30650400   -1.43442100   -0.15403800
H       0.24536800    2.01705800    0.09470300
H      -2.38260000    1.22885500    0.14617100
H      -2.26303200   -1.49654600    0.00244800
""",
)

entry(
    index = 19,
    label = "P415",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {4,S} {7,S}
2  O u0 p2 c0 {4,S} {13,S}
3  O u0 p2 c0 {8,D}
4  C u0 p0 c0 {1,S} {2,S} {5,S} {8,S}
5  C u0 p0 c0 {4,S} {6,D} {9,S}
6  C u0 p0 c0 {5,D} {7,S} {10,S}
7  C u1 p0 c0 {1,S} {6,S} {12,S}
8  C u0 p0 c0 {3,D} {4,S} {11,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {8,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82011,0.0107892,0.000182631,-3.82572e-07,2.3598e-10,-34282,13.2554], Tmin=(10,'K'), Tmax=(553.047,'K')),
            NASAPolynomial(coeffs=[3.75003,0.0513325,-3.59206e-05,1.17778e-08,-1.45333e-12,-34886.6,8.01653], Tmin=(553.047,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-285.105,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 3, 'C=C': 1, 'H-O': 1, 'C-H': 4, 'C-C': 3, 'C=O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [3, 4], dihedral: [2, 3, 4, 10], rotor symmetry: 1, max scan energy: 25.41 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       2.75241800   -0.07996100    0.47140600
C       1.62328500    0.30149200    0.58053600
C       0.47689600   -0.30175100   -0.25163200
O       0.96150100   -1.27221600   -1.08573500
C      -0.68793400   -0.73542800    0.58154300
C      -1.74615000    0.10047300    0.30596900
C      -1.32965800    1.02261800   -0.63072100
O      -0.04132500    0.83681800   -0.99225200
H       1.32918100    1.11454400    1.26626200
H       1.92516100   -1.18748300   -1.10276600
H      -0.66034700   -1.60149400    1.22144500
H      -2.74241100    0.04285400    0.71443200
H      -1.85473700    1.82421900   -1.12296500
""",
)

entry(
    index = 20,
    label = "P416",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {6,S}
2  O u0 p2 c0 {7,D}
3  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
4  C u0 p0 c0 {3,S} {5,D} {9,S}
5  C u0 p0 c0 {4,D} {6,S} {10,S}
6  C u1 p0 c0 {1,S} {5,S} {12,S}
7  C u0 p0 c0 {2,D} {3,S} {11,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88227,0.00705555,0.000150823,-3.00197e-07,1.80791e-10,-10571.4,12.6579], Tmin=(10,'K'), Tmax=(545.641,'K')),
            NASAPolynomial(coeffs=[1.85691,0.0477614,-3.21659e-05,1.02323e-08,-1.23473e-12,-10735.3,17.6748], Tmin=(545.641,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-87.9403,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (278.535,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'C-H': 5, 'C-C': 3, 'C=O': 1, 'C-O': 2}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 21.67 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       2.98634300    0.02724300   -0.38343800
C       1.86526800    0.14761400    0.01449900
C       0.63996200   -0.15700300   -0.84230500
C       0.20770000    1.08212700   -1.56360500
C      -1.04465500    1.41326900   -1.08799100
C      -1.41945500    0.46487800   -0.16489800
O      -0.46616400   -0.48572000    0.00241900
H       1.62806200    0.53864300    1.02447600
H       0.86986400   -1.00854900   -1.49195400
H       0.80996000    1.59332500   -2.29545400
H      -1.64581900    2.25707100   -1.38693700
H      -2.31373800    0.34967700    0.42387000
""",
)

entry(
    index = 21,
    label = "P417",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {6,S}
2  O u0 p2 c0 {7,D}
3  C u0 p0 c0 {1,S} {4,S} {7,D}
4  C u0 p0 c0 {3,S} {5,D} {8,S}
5  C u0 p0 c0 {4,D} {6,S} {9,S}
6  C u1 p0 c0 {1,S} {5,S} {10,S}
7  C u0 p0 c0 {2,D} {3,D}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92372,0.00441864,0.000116368,-2.14497e-07,1.20687e-10,-2569.8,11.317], Tmin=(10,'K'), Tmax=(567.62,'K')),
            NASAPolynomial(coeffs=[0.903622,0.0426618,-2.95144e-05,9.48278e-09,-1.14712e-12,-2500.18,21.7701], Tmin=(567.62,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-21.3992,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (228.648,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-H': 3, 'C=O': 1, 'C-C': 2, 'C-O': 2}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 2, max scan energy: 32.49 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O       3.00546800   -0.97439300    0.41924400
C       2.28015100   -0.07378500    0.18156400
C       0.84403700   -0.02986400    0.07406200
C       0.02495500    1.02298600   -0.20181400
C      -1.29842800    0.51870300   -0.18715600
C      -1.18165200   -0.80463100    0.09709700
O       0.09684600   -1.15872800    0.25856000
H       0.35018700    2.03251700   -0.39029300
H      -2.21295800    1.05879200   -0.36252400
H      -1.90860600   -1.59159700    0.21160600
""",
)

entry(
    index = 22,
    label = "P418",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {6,S}
2 C u0 p0 c0 {1,S} {5,D} {7,S}
3 C u0 p0 c0 {1,D} {4,S} {8,S}
4 O u0 p2 c0 {3,S} {5,S}
5 C u1 p0 c0 {2,D} {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.19453,-0.0156243,0.000147665,-2.287e-07,1.14296e-10,27216.3,9.31552], Tmin=(10,'K'), Tmax=(641.341,'K')),
            NASAPolynomial(coeffs=[0.570207,0.031676,-2.07225e-05,6.37725e-09,-7.43589e-13,27173.3,21.2313], Tmin=(641.341,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (226.297,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-H': 3, 'C-C': 1, 'C-O': 2}

External symmetry: 1, optical isomers: 1

Geometry:
C      -0.62960900   -1.18245200    0.56144000
C      -1.14242000   -0.15893100   -0.14976000
C       0.01476900    0.63905100   -0.46081500
C       1.08179300    0.02022900    0.08752600
O       0.67831900   -1.12208200    0.72870800
H      -2.16863000    0.01530100   -0.41762000
H       0.03022100    1.55727900   -1.02450900
H       2.13555900    0.23160500    0.12195800
""",
)

entry(
    index = 23,
    label = "P419",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {4,S} {6,S}
2 C u0 p0 c0 {1,D} {3,S} {7,S}
3 C u1 p0 c0 {2,S} {5,S} {9,S}
4 C u0 p0 c0 {1,S} {5,S} {8,D}
5 O u0 p2 c0 {3,S} {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 O u0 p2 c0 {4,D}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.1344,-0.0125163,0.000176635,-3.09649e-07,1.73067e-10,-20086.4,10.4242], Tmin=(10,'K'), Tmax=(580.426,'K')),
            NASAPolynomial(coeffs=[1.34282,0.035929,-2.40436e-05,7.54191e-09,-8.9407e-13,-20254.4,18.1352], Tmin=(580.426,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-167.025,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 3, 'C=O': 1, 'C-C': 2, 'C=C': 1, 'C-O': 2}

External symmetry: 1, optical isomers: 1

Geometry:
O       2.29936000   -0.89631200   -0.04983500
C       1.17224600   -0.49432100   -0.06646100
C       0.58572300    0.82344200    0.01496000
C      -0.78435400    0.68017000   -0.05659400
C      -1.03439300   -0.67454500   -0.17759800
O       0.08824500   -1.39534000   -0.18707100
H       1.16991100    1.72240100    0.11354600
H      -1.53510100    1.45234500   -0.02668400
H      -1.96163700   -1.21783900   -0.26228900
""",
)

entry(
    index = 24,
    label = "P422",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 C u1 p0 c0 {1,S} {7,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93354,0.00420424,7.67561e-05,-1.68417e-07,1.11571e-10,9073.31,8.45248], Tmin=(10,'K'), Tmax=(505.613,'K')),
            NASAPolynomial(coeffs=[3.62284,0.0205296,-1.28168e-05,3.93256e-09,-4.68893e-13,8927.47,7.98663], Tmin=(505.613,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (75.4212,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 3, 'C=O': 1, 'C-C': 1, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: 
* Invalidated! pivots: [1, 2], dihedral: [5, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
C      -1.05852100   -0.25197800   -0.07123800
C       0.17609500    0.40120000   -0.22262100
C       0.38219100    1.52623200   -0.91094600
O       0.57402000    2.50115800   -1.50448600
H      -1.10862200   -1.15892000    0.50949100
H      -1.96183700    0.13010300   -0.52171500
H       1.07717300    0.00729600    0.23507400
""",
)

entry(
    index = 25,
    label = "P423",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {5,S}
2 C u0 p0 c0 {1,S} {4,D} {6,S}
3 C u1 p0 c0 {1,D} {8,S}
4 C u0 p0 c0 {2,D} {7,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 O u0 p2 c0 {4,D}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87356,0.00880238,0.000110868,-2.96689e-07,2.31587e-10,30227.2,9.60845], Tmin=(10,'K'), Tmax=(445.367,'K')),
            NASAPolynomial(coeffs=[4.62759,0.0242347,-1.58932e-05,5.00486e-09,-6.03177e-13,29939.8,4.1083], Tmin=(445.367,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (251.312,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-H': 3, 'C=O': 1, 'C-C': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 22.02 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C      -1.76472800    0.56415100   -0.10744100
C      -0.62995300   -0.07504800   -0.24838100
C       0.62912100    0.27664300    0.40130000
C       1.73662600   -0.40818400    0.21740400
O       2.71169500   -1.00537200    0.05986500
H      -2.76977000    0.46929200   -0.48481800
H      -0.60905400   -0.94789400   -0.90520700
H       0.69606400    1.12641100    1.06728000
""",
)

entry(
    index = 26,
    label = "P424",
    molecule = 
"""
1 O u0 p2 c0 {5,D}
2 C u0 p0 c0 {3,S} {4,D} {6,S}
3 C u0 p0 c0 {2,S} {5,D} {7,S}
4 C u0 p0 c0 {2,D} {8,S} {9,S}
5 C u0 p0 c0 {1,D} {3,D}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89655,0.00705046,0.00011648,-2.85613e-07,2.11612e-10,-122.694,9.04072], Tmin=(10,'K'), Tmax=(452.272,'K')),
            NASAPolynomial(coeffs=[3.60858,0.0285974,-1.79976e-05,5.49919e-09,-6.4913e-13,-290.968,8.05324], Tmin=(452.272,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-1.03282,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (203.705,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-H': 4, 'C=O': 1, 'C-C': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 23.75 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C      -1.37833100   -0.15684400    0.88169200
C      -0.28760600    0.36826700    0.33264600
C       0.61805300   -0.35137400   -0.55175000
C       1.69029700    0.19847900   -1.07902100
O       2.63231700    0.67675400   -1.54403400
H      -1.67110900   -1.18428700    0.70036700
H      -2.00948000    0.43362900    1.53100900
H      -0.03472400    1.40216200    0.54356900
H       0.44050500   -1.38674700   -0.81459100
""",
)

entry(
    index = 27,
    label = "P427",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {5,S}
2 C u0 p0 c0 {1,D} {4,S} {6,S}
3 C u0 p0 c0 {1,S} {7,D} {8,S}
4 C u1 p0 c0 {2,S} {9,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 O u0 p2 c0 {3,D}
8 H u0 p0 c0 {3,S}
9 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76273,0.0206804,2.79673e-05,-7.2264e-08,4.24242e-11,-9799.15,10.9899], Tmin=(10,'K'), Tmax=(606.082,'K')),
            NASAPolynomial(coeffs=[3.86928,0.0297392,-1.86127e-05,5.5473e-09,-6.33742e-13,-9991.37,9.05005], Tmin=(606.082,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-81.5061,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 3, 'C=O': 2, 'C-C': 2, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: 
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Another conformer for P427 exists which is 7.09 kJ/mol lower.Another conformer for P427 exists which is 7.09 kJ/mol lower.


External symmetry: 1, optical isomers: 1

Geometry:
O       3.06543500   -0.01118700   -0.51215800
C       1.99132700    0.25749900   -0.20324100
C       0.74553100    0.55950500    0.15034700
C       0.37625900    1.75603800    0.79654700
C      -0.99941400    1.97869700    1.13279400
O      -1.89563300    1.18444600    0.89247700
H      -0.01867300   -0.17577600   -0.08294800
H       1.11385300    2.50823700    1.04251300
H      -1.21828200    2.93616700    1.63722100
""",
)

entry(
    index = 28,
    label = "P428",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3 C u0 p0 c0 {2,S} {4,D} {7,S}
4 C u0 p0 c0 {3,D} {8,S} {9,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89363,0.0117636,3.0783e-05,-4.81914e-08,2.02112e-11,8997.88,9.9982], Tmin=(10,'K'), Tmax=(804.792,'K')),
            NASAPolynomial(coeffs=[2.57208,0.027459,-1.54819e-05,4.22487e-09,-4.48802e-13,8915.02,14.2506], Tmin=(804.792,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (74.8165,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (203.705,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 1, 'C=C': 1, 'C-O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 11.49 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C      -1.39904000    0.03277900   -0.13335000
C      -0.20723900    0.51160400    0.17821100
C       1.07724200   -0.25365700    0.02158200
O       0.99736200   -1.51034700   -0.46992500
H      -1.50789600   -0.96942100   -0.53015400
H      -2.29478600    0.62543800   -0.00144800
H      -0.10333100    1.51740800    0.57587200
H       1.62022600   -0.30745100    0.98568000
H       1.79131600    0.30699100   -0.61322900
""",
)

entry(
    index = 29,
    label = "P429",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 C u0 p0 c0 {1,S} {5,D} {6,S}
3 C u1 p0 c0 {1,D} {7,S}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {2,D}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95119,0.00275168,6.94605e-05,-1.24807e-07,6.78385e-11,19509,8.45954], Tmin=(10,'K'), Tmax=(594.65,'K')),
            NASAPolynomial(coeffs=[2.15637,0.026229,-1.85276e-05,6.08771e-09,-7.50495e-13,19520.9,14.4902], Tmin=(594.65,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (162.185,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (153.818,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 3, 'C=O': 1, 'C-C': 1, 'C=C': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 29.50 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       1.29664800    0.15838500    0.49437800
C       0.29601300   -0.16123600   -0.28275200
C      -1.11355500    0.11762900    0.08379100
O      -2.04487800   -0.16937800   -0.61851700
H       2.37345500    0.09160800    0.50749100
H       0.44840800   -0.65208600   -1.24571100
H      -1.25609000    0.61507900    1.06132200
""",
)

entry(
    index = 30,
    label = "P430",
    molecule = 
"""
1 O u0 p2 c0 {4,D}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u0 p0 c0 {2,D} {6,S} {7,S}
4 C u0 p0 c0 {1,D} {2,S} {8,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9656,0.00210796,7.87204e-05,-1.46916e-07,8.70318e-11,-10602.5,7.89155], Tmin=(10,'K'), Tmax=(503.203,'K')),
            NASAPolynomial(coeffs=[1.39621,0.0286003,-1.83389e-05,5.63645e-09,-6.64885e-13,-10420.7,17.7595], Tmin=(503.203,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-88.1653,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 4, 'C=O': 1, 'C-C': 1, 'C=C': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 32.52 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C      -1.08266000   -0.42654900   -0.35202800
C      -0.19048600    0.08140300    0.48840400
C       1.18462000    0.36975000    0.04407600
O       2.04196800    0.82908400    0.75042900
H      -0.81821600   -0.63984400   -1.38283700
H      -2.09835100   -0.64700000   -0.05011000
H      -0.42552600    0.30459000    1.52282100
H       1.38865200    0.12856600   -1.02075500
""",
)



