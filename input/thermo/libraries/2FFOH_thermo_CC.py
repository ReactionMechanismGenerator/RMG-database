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

