#!/usr/bin/env python
# encoding: utf-8

name = "unimolecular_decomp_Xing_Vermie"
shortDesc = ""
longDesc = """
ARC v1.1.0
ARC project unimolecular_decomp_Xing_Vermie

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
Species INT1 (run time: 9:14:30)
Species INT2 (run time: 3:20:57)
Species INT3 (run time: 5:02:56)
Species INT4 (run time: 4:49:14)
Species INT5 (run time: 1 day, 0:45:58)
Species INT1a (run time: 13:25:22)
Species O=C=CO (run time: 0:08:50)
Species P1c (run time: 2:20:54)
Species P1b (run time: 0:51:38)
Species P1g (run time: 0:15:21)
Species INT3a (run time: 5:55:39)
Species P3d (run time: 2:51:42)
Species P3f (run time: 0:32:34)
Species P4a (run time: 1 day, 5:37:45)
Species P5 (run time: 1:19:12)
Species rxn_2_product_0 (run time: 0:33:25)
Species rxn_3_product_0 (run time: 5:01:14)
Species rxn_5_product_0 (run time: 1:40:38)
Species rxn_6_product_0 (run time: 1:48:23)
Species rxn_8_product_0 (run time: 0:33:22)
Species rxn_13_product_0 (run time: 5:27:43)
Species rxn_15_reactant_0 (run time: 6:38:26)
Species rxn_15_product_0 (run time: 1 day, 17:15:18)
Species rxn_16_product_0 (run time: 1 day, 1:35:05)
Species rxn_17_product_0 (run time: 2:06:49)
Species rxn_19_product_0 (run time: 1 day, 9:40:29)
Species rxn_20_product_0 (run time: 5:38:10)
Species rxn_21_product_0 (run time: 1 day, 17:09:43)
Species rxn_22_product_0 (run time: 4:38:15)
Species rxn_24_reactant_0 (run time: 1 day, 8:25:54)
Species rxn_24_product_0 (run time: 1 day, 4:43:56)
Species rxn_25_product_0 (run time: 1:04:42)

Overall time since project initiation: 1.0 days, 02:17:16
"""
entry(
    index = 0,
    label = "INT1",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {5,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,S} {5,D}
4  C u0 p0 c0 {3,S} {6,D} {12,S}
5  O u0 p1 c+1 {2,S} {3,D}
6  C u0 p1 c-1 {2,S} {4,D}
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
            NASAPolynomial(coeffs=[3.90091,0.0066275,0.000173135,-3.7782e-07,2.59823e-10,-1146.09,12.4436], Tmin=(10,'K'), Tmax=(451.233,'K')),
            NASAPolynomial(coeffs=[0.71908,0.0517622,-3.31788e-05,1.0139e-08,-1.18519e-12,-1031.29,23.3524], Tmin=(451.233,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-9.54319,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 3, 'C-O': 2, 'H-O': 1, 'C=C': 1, 'C=O': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [8, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for INT1 exists which is 1.42 kJ/mol lower.Another conformer for INT1 exists which is 1.42 kJ/mol lower.


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.24540100    0.77269500   -0.43239100
C      -1.70089900   -0.42410400    0.04214200
C      -0.39837600   -0.27246000    0.76058100
C       0.18820800   -1.10612400    1.70751900
C       1.43853400   -0.61413400    2.07611000
C       1.57090200    0.59121000    1.27069600
O       0.32820700    0.75006600    0.43158400
H      -1.55007800    1.28534400   -0.85095500
H      -2.42738500   -0.87410300    0.71926200
H      -1.52636400   -1.14873300   -0.76815800
H      -0.29702400   -1.99479100    2.08780300
H       1.64215100    1.50610400    1.86067000
H       2.39698600    0.55053100    0.55883000
""",
)

entry(
    index = 1,
    label = "INT2",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,D} {6,S}
4  C u0 p0 c0 {2,S} {3,D} {12,S}
5  C u0 p1 c-1 {2,S} {6,D}
6  O u0 p1 c+1 {3,S} {5,D}
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
            NASAPolynomial(coeffs=[3.77959,0.0251622,4.14414e-05,-7.62478e-08,3.39979e-11,-2426.27,12.1257], Tmin=(10,'K'), Tmax=(798.247,'K')),
            NASAPolynomial(coeffs=[3.75827,0.0429225,-2.51051e-05,7.03424e-09,-7.61681e-13,-2985.31,8.70079], Tmin=(798.247,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-20.1669,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 3, 'C-O': 2, 'H-O': 1, 'C=C': 1, 'C=O': 1}
1D rotors:
pivots: [1, 2], dihedral: [8, 1, 2, 3], rotor symmetry: 1, max scan energy: 10.61 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for INT2 exists which is 1.74 kJ/mol lower.Another conformer for INT2 exists which is 1.74 kJ/mol lower.


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.61282200    0.53430200    0.26692400
C      -1.66539600   -0.27347000   -0.38120100
C      -0.26571100    0.15597000   -0.10798800
C       0.29469900    1.04649100    0.68817300
C       1.76863000    0.95907900    0.45022900
C       1.94326000   -0.10834300   -0.59657100
O       0.72519200   -0.51949000   -0.86337400
H      -2.55817900    1.42110700   -0.09414200
H      -1.81262300   -1.29049600   -0.01095500
H      -1.81937300   -0.30590100   -1.46730700
H      -0.22039700    1.68701800    1.38409100
H       2.35245300    0.67050200    1.33177200
H       2.23136100    1.88241600    0.08459800
""",
)

entry(
    index = 2,
    label = "INT3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {7,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {6,D} {11,S}
4  C u0 p0 c0 {3,S} {5,D} {12,S}
5  O u0 p1 c+1 {1,S} {4,D}
6  C u0 p1 c-1 {1,S} {3,D}
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
            NASAPolynomial(coeffs=[3.84924,0.0111448,0.000167898,-4.03579e-07,2.99744e-10,-502.174,11.5291], Tmin=(10,'K'), Tmax=(429.526,'K')),
            NASAPolynomial(coeffs=[1.82132,0.0491526,-3.16139e-05,9.73417e-09,-1.14712e-12,-504.365,17.5455], Tmin=(429.526,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-4.18326,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 3, 'C-O': 2, 'H-O': 1, 'C=C': 1, 'C=O': 1}
1D rotors:
pivots: [1, 2], dihedral: [8, 1, 2, 3], rotor symmetry: 1, max scan energy: 12.55 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for INT3 exists which is 5.80 kJ/mol lower.Another conformer for INT3 exists which is 5.80 kJ/mol lower.


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.42271900    0.40818000    0.37603000
C      -1.48072800   -0.24435100   -0.43447000
C      -0.19639600   -0.58213600    0.30969200
C       0.83359300   -1.25659500   -0.46907800
C       1.91915500   -0.37734200   -0.40971000
C       1.57414400    0.74171400    0.32700600
O       0.37035800    0.74081800    0.79954600
H      -2.05901300    1.25247300    0.64885100
H      -1.22971100    0.34317100   -1.32569200
H      -1.92704000   -1.18062800   -0.76331100
H      -0.42420600   -1.12441100    1.23155900
H       2.89022600   -0.51266100   -0.86428700
H       2.16971500    1.61793200    0.56240400
""",
)

entry(
    index = 3,
    label = "INT4",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {7,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {3,D} {6,S} {12,S}
5  C u0 p1 c-1 {1,S} {6,D}
6  O u0 p1 c+1 {4,S} {5,D}
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
            NASAPolynomial(coeffs=[3.81082,0.0150074,0.000135428,-3.12974e-07,2.18177e-10,-1031.59,11.7312], Tmin=(10,'K'), Tmax=(459.198,'K')),
            NASAPolynomial(coeffs=[1.82266,0.0492318,-3.15918e-05,9.68094e-09,-1.13489e-12,-1027.24,17.8349], Tmin=(459.198,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-8.59637,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 3, 'C-O': 2, 'H-O': 1, 'C=C': 1, 'C=O': 1}
1D rotors:
pivots: [1, 2], dihedral: [8, 1, 2, 3], rotor symmetry: 1, max scan energy: 11.67 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for INT4 exists which is 4.25 kJ/mol lower.Another conformer for INT4 exists which is 4.25 kJ/mol lower.


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.10224100    0.64197000   -0.60485500
C      -1.34052800   -0.40743700   -0.06070700
C      -2.20777800   -1.52532100    0.53209100
C      -3.08493500   -2.16209300   -0.51844400
O      -4.29152500   -2.15852400   -0.01658900
C      -4.34390900   -1.55792300    1.26608600
C      -3.14761700   -1.15501200    1.63749800
H      -2.52463500    0.32519000   -1.40644500
H      -0.72625700    0.03263300    0.72543400
H      -0.67359500   -0.84899200   -0.80774600
H      -1.52323300   -2.32783200    0.84756100
H      -5.32283300   -1.52318300    1.71391900
H      -2.89763800   -0.65868700    2.56066400
""",
)

entry(
    index = 4,
    label = "INT5",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {8,S}
2  C u0 p0 c0 {1,S} {4,D} {9,S}
3  C u0 p0 c0 {1,D} {5,S} {7,S}
4  C u0 p0 c0 {2,D} {6,S} {10,S}
5  C u0 p0 c0 {3,S} {11,D} {12,S}
6  O u0 p2 c0 {4,S} {13,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 O u0 p2 c0 {5,D}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74536,0.0198179,0.000171979,-4.79954e-07,3.928e-10,-27058.8,10.9173], Tmin=(10,'K'), Tmax=(410.813,'K')),
            NASAPolynomial(coeffs=[3.39991,0.0496637,-3.3691e-05,1.07234e-08,-1.29172e-12,-27253.9,9.55675], Tmin=(410.813,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-224.98,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (295.164,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-H': 5, 'C-C': 2, 'H-O': 1, 'C=O': 1, 'C-O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 43.73 kJ/mol
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 37.19 kJ/mol
pivots: [6, 7], dihedral: [5, 6, 7, 13], rotor symmetry: 1, max scan energy: 27.05 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O      -3.74252700   -0.05508200    0.93359100
C      -2.66330600    0.41448300    0.67047900
C      -1.46071300   -0.36271000    0.39017800
C      -0.30245400    0.24844400    0.10673900
C       0.94417400   -0.40909100   -0.18529200
C       2.05570400    0.28304100   -0.45834000
O       3.26315100   -0.22029800   -0.74251500
H      -2.52271900    1.51675500    0.62588500
H      -1.54932900   -1.44314600    0.42210600
H      -0.29081500    1.33722000    0.09316300
H       0.96653200   -1.49526300   -0.17988500
H       2.06719500    1.36693900   -0.47183100
H       3.23597800   -1.18121500   -0.72648800
""",
)

entry(
    index = 5,
    label = "INT1a",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,D}
3  C u0 p0 c0 {2,S} {5,D} {10,S}
4  C u0 p0 c0 {5,D} {11,S} {12,S}
5  C u0 p0 c0 {3,D} {4,D}
6  O u0 p2 c0 {1,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u0 p2 c0 {2,D}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.57401,0.0409233,-1.96656e-06,-3.01276e-08,1.62615e-11,-20232.8,11.6717], Tmin=(10,'K'), Tmax=(829.063,'K')),
            NASAPolynomial(coeffs=[6.74052,0.0391361,-2.31407e-05,6.52567e-09,-7.09421e-13,-21221.5,-5.80734], Tmin=(829.063,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-168.25,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-H': 5, 'C-C': 2, 'H-O': 1, 'C=O': 1, 'C-O': 1}
1D rotors:
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 26.80 kJ/mol
* Invalidated! pivots: [4, 6], dihedral: [3, 4, 6, 7], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [6, 7], dihedral: [4, 6, 7, 13], rotor symmetry: 1, max scan energy: 28.04 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       1.53762900   -0.23180200    2.01423600
C       0.85107300    0.50739700    1.20291500
C       0.15419700    1.24096500    0.37691900
C      -0.62170400    0.67666000   -0.74731000
O      -1.25448000    1.39236300   -1.48998600
C      -0.62374400   -0.82351700   -0.97224500
O      -1.40516100   -1.16503700   -2.07087600
H       2.57558100   -0.46664600    1.81000400
H       1.09062100   -0.63064400    2.91718600
H       0.11693700    2.31910000    0.48664000
H      -0.99365800   -1.30910200   -0.06048900
H       0.41356500   -1.15370000   -1.10970400
H      -1.75578900   -0.33342500   -2.41796900
""",
)

entry(
    index = 6,
    label = "O=C=CO",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {6,S}
2 O u0 p2 c0 {4,D}
3 C u0 p0 c0 {1,S} {4,D} {5,S}
4 C u0 p0 c0 {2,D} {3,D}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92645,0.00478658,6.60071e-05,-1.60581e-07,1.13999e-10,-20409.5,8.61119], Tmin=(10,'K'), Tmax=(491.447,'K')),
            NASAPolynomial(coeffs=[4.52892,0.0146825,-9.36863e-06,2.94535e-09,-3.58344e-13,-20647.4,4.31433], Tmin=(491.447,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-169.711,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (128.874,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'C-H': 1, 'H-O': 1, 'C=C': 1, 'C-O': 1}
1D rotors:
pivots: [3, 4], dihedral: [2, 3, 4, 6], rotor symmetry: 2, max scan energy: 11.55 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.82088100   -0.69587800   -0.41647800
C       0.87865700   -0.12716500   -0.05850200
C      -0.17835300    0.53615400    0.36317900
O      -1.43166300   -0.04581500    0.32311200
H      -0.03068100    1.49719400    0.83866700
H      -1.92387600    0.33462000   -0.40744400
""",
)

entry(
    index = 7,
    label = "P1c",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,T}
4  O u0 p2 c0 {2,S} {10,S}
5  C u0 p0 c0 {3,T} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86859,0.00856465,0.000139688,-3.26711e-07,2.28839e-10,-1992.18,10.2766], Tmin=(10,'K'), Tmax=(485.352,'K')),
            NASAPolynomial(coeffs=[4.01716,0.0338956,-2.06684e-05,6.27951e-09,-7.46824e-13,-2319.38,6.44506], Tmin=(485.352,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-16.5927,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (253.591,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 2, 'C#C': 1, 'H-O': 1, 'C-O': 1}
1D rotors:
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [4, 5], dihedral: [3, 4, 5, 11], rotor symmetry: 1, max scan energy: 15.35 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       2.03111400   -1.00613600   -0.41257700
C       0.88868500   -0.87186200   -0.07729500
C      -0.50723600   -0.64812200    0.28250900
C      -1.00802500    0.70596300   -0.23005400
O      -0.94804400    0.80862900   -1.62996200
H       3.04746000   -1.14497200   -0.69383600
H      -1.12250400   -1.44413500   -0.14338000
H      -0.61802500   -0.68955400    1.36919800
H      -2.05699700    0.82422100    0.04291400
H      -0.43850200    1.50907800    0.25312200
H      -0.03450700    0.68376900   -1.90016300
""",
)

entry(
    index = 8,
    label = "P1b",
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
            NASAPolynomial(coeffs=[3.8149,0.0156561,0.000189519,-7.17533e-07,7.91762e-10,-1848.28,10.069], Tmin=(10,'K'), Tmax=(320.706,'K')),
            NASAPolynomial(coeffs=[5.141,0.0293842,-1.62584e-05,4.5123e-09,-4.98943e-13,-2089,2.75268], Tmin=(320.706,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-15.3372,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (249.434,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-H': 5, 'C-C': 1, 'H-O': 1, 'C-O': 1}
1D rotors:
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 11.95 kJ/mol
pivots: [4, 5], dihedral: [3, 4, 5, 11], rotor symmetry: 1, max scan energy: 10.01 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       2.13543500   -0.59616200   -0.13317000
C       1.03913400    0.07206100   -0.33250500
C      -0.06791200    0.72326100   -0.53832200
C      -1.43338700    0.10092200   -0.41772800
O      -2.22994800    0.75128800    0.55190600
H       2.58234400   -0.65884500    0.85205500
H       2.63649900   -1.10460100   -0.94850400
H      -0.02938400    1.77848500   -0.79265400
H      -1.97415800    0.20886700   -1.35957300
H      -1.33404800   -0.96916400   -0.20647100
H      -1.76871000    0.71014900    1.39171100
""",
)

entry(
    index = 9,
    label = "P1g",
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
            NASAPolynomial(coeffs=[3.92522,0.00500573,9.03789e-05,-2.13565e-07,1.53902e-10,3229.96,9.55183], Tmin=(10,'K'), Tmax=(462.036,'K')),
            NASAPolynomial(coeffs=[3.56875,0.0225467,-1.34959e-05,4.02629e-09,-4.70971e-13,3108.61,9.32668], Tmin=(462.036,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (26.8438,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 3, 'C-C': 1, 'C#C': 1, 'H-O': 1, 'C-O': 1}
1D rotors:
pivots: [3, 4], dihedral: [2, 3, 4, 8], rotor symmetry: 1, max scan energy: 9.57 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       1.87545900    0.00866700   -0.31253000
C       0.69420100   -0.17683400   -0.25149600
C      -0.75572900   -0.36357200   -0.16294600
O      -1.48857000    0.60563100   -0.87869800
H       2.92599500    0.16404100   -0.37415300
H      -1.02510400   -1.32998800   -0.59118700
H      -1.04441900   -0.38256300    0.89502200
H      -1.18183500    1.47461700   -0.61372400
""",
)

entry(
    index = 10,
    label = "INT3a",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,D} {9,S}
3  C u0 p0 c0 {4,S} {5,D} {10,S}
4  C u0 p0 c0 {3,S} {11,D} {12,S}
5  C u0 p0 c0 {2,D} {3,D}
6  O u0 p2 c0 {1,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 O u0 p2 c0 {4,D}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.60146,0.0413124,-1.29189e-05,-9.4421e-09,5.60273e-12,-16724.5,12.4608], Tmin=(10,'K'), Tmax=(1021.83,'K')),
            NASAPolynomial(coeffs=[8.27838,0.0340895,-1.85887e-05,4.8738e-09,-4.97288e-13,-18259.1,-13.0354], Tmin=(1021.83,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-139.06,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C=O': 1, 'C-H': 5, 'C-C': 2, 'H-O': 1, 'C-O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 36.38 kJ/mol
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 7], invalidation reason: Another conformer for INT3a exists which is 1.51 kJ/mol lower.Another conformer for INT3a exists which is 1.51 kJ/mol lower.
pivots: [6, 7], dihedral: [5, 6, 7, 13], rotor symmetry: 1, max scan energy: 7.37 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       3.56056900    0.47496800   -1.71642600
C       2.44897500    0.08084000   -1.48544900
C       1.85562000    0.05809100   -0.13345200
C       0.63866800   -0.38336200    0.05132000
C      -0.57794500   -0.80870800    0.19034800
C      -1.79980700    0.07240200    0.10884700
O      -1.53391800    1.40626300   -0.21854000
H       1.78637800   -0.29516200   -2.28915800
H       2.46825000    0.41631700    0.68706100
H      -0.74594200   -1.86170900    0.39913400
H      -2.45737400   -0.31240500   -0.67362300
H      -2.34806800   -0.01234900    1.05722300
H      -0.91890700    1.77172100    0.42093700
""",
)

entry(
    index = 11,
    label = "P3f",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,D} {6,S}
2  C u0 p0 c0 {1,S} {7,D} {8,S}
3  C u0 p0 c0 {5,D} {9,S} {10,S}
4  C u0 p0 c0 {1,D} {5,D}
5  C u0 p0 c0 {3,D} {4,D}
6  H u0 p0 c0 {1,S}
7  O u0 p2 c0 {2,D}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82103,0.0139825,0.000104655,-2.59368e-07,1.87534e-10,20493.1,10.1456], Tmin=(10,'K'), Tmax=(461.292,'K')),
            NASAPolynomial(coeffs=[3.21517,0.0364192,-2.41786e-05,7.57563e-09,-9.01548e-13,20366.1,10.6182], Tmin=(461.292,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (170.37,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (228.648,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 3, 'C=O': 1, 'C-H': 4, 'C-C': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 36.19 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O      -3.39828700    0.19820900    0.37637200
C      -2.21371700    0.38738000    0.29216800
C      -1.20421700   -0.66064900    0.52984100
C       0.07987000   -0.39474500    0.42300900
C       1.30205800   -0.09755300    0.31004000
C       2.57104100    0.19565200    0.19668200
H      -1.80081500    1.37978300    0.02574800
H      -1.56368700   -1.64946500    0.79374300
H       3.33491500   -0.55435100    0.36553900
H       2.89284200    1.19574100   -0.06897400
""",
)

entry(
    index = 12,
    label = "P4a",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  C u0 p0 c0 {2,S} {5,D} {10,S}
4  C u0 p0 c0 {2,D} {6,S} {12,S}
5  C u0 p0 c0 {3,D} {6,S} {11,S}
6  O u0 p2 c0 {4,S} {5,S}
7  O u0 p2 c0 {1,S} {13,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76878,0.0207312,6.88618e-05,-1.32236e-07,6.97131e-11,-29542.5,11.6962], Tmin=(10,'K'), Tmax=(631.103,'K')),
            NASAPolynomial(coeffs=[2.06908,0.0465681,-2.83511e-05,8.27659e-09,-9.30714e-13,-29628,16.7372], Tmin=(631.103,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-245.662,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-H': 5, 'C-C': 2, 'C-O': 3, 'H-O': 1}
1D rotors:
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [5, 6], dihedral: [4, 5, 6, 12], rotor symmetry: 1, max scan energy: 10.77 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.60764200    1.35873800    0.57722300
C      -2.04484400    0.09865000    0.35440800
C      -1.04053300   -0.68116500   -0.09627700
C       0.11933900    0.16002500   -0.16014600
C       1.48990300   -0.22166500   -0.61182100
O       1.51086300   -0.72939200   -1.93310300
C      -0.29640500    1.37876800    0.25574200
H      -3.08488100   -0.08411200    0.56246900
H      -1.10000100   -1.72338000   -0.36199700
H       2.16193900    0.63896900   -0.50767700
H       1.88759800   -1.02318800    0.01286900
H       1.05635300   -0.10274700   -2.49919300
H       0.21121900    2.32071800    0.37895100
""",
)

entry(
    index = 13,
    label = "P5",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {4,S} {11,S}
4  C u0 p0 c0 {3,S} {5,D} {10,S}
5  C u0 p0 c0 {4,D} {6,S} {12,S}
6  O u0 p2 c0 {1,S} {5,S}
7  O u0 p2 c0 {1,S} {13,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89414,0.00611073,0.000150421,-2.783e-07,1.56813e-10,-27997.9,11.0701], Tmin=(10,'K'), Tmax=(573.972,'K')),
            NASAPolynomial(coeffs=[0.608813,0.0531995,-3.58658e-05,1.1509e-08,-1.40331e-12,-28019.3,21.6244], Tmin=(573.972,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-232.834,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-H': 5, 'C-C': 2, 'C-O': 3, 'H-O': 1}
1D rotors:
pivots: [6, 7], dihedral: [1, 6, 7, 13], rotor symmetry: 1, max scan energy: 20.06 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.14905400   -1.22242800   -0.87387000
C       1.10243200   -1.02854700   -0.43363100
C       1.51687400    0.11073200    0.13175500
C       0.57867200    1.20887400    0.20565700
C      -0.70558800    1.00452800   -0.09912700
C      -1.18924600   -0.38856800   -0.35398900
O      -1.74067000   -0.96144200    0.79336200
H       1.74340800   -1.87707500   -0.63414300
H       2.54458800    0.21760000    0.44304500
H       0.93522100    2.19705200    0.46874500
H      -1.44017300    1.79810000   -0.10154600
H      -1.97017800   -0.43648600   -1.11011400
H      -1.20623900   -0.69947200    1.54827500
""",
)

entry(
    index = 14,
    label = "rxn_2_product_0",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {3,S} {6,S}
2  C u0 p0 c0 {1,D} {4,S} {7,S}
3  C u0 p0 c0 {1,S} {8,D} {9,S}
4  C u0 p0 c0 {2,S} {5,T}
5  C u0 p0 c0 {4,T} {10,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  O u0 p2 c0 {3,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84389,0.0122959,0.000151789,-4.59377e-07,4.17767e-10,16627.5,9.93918], Tmin=(10,'K'), Tmax=(369.081,'K')),
            NASAPolynomial(coeffs=[3.70019,0.0345093,-2.24393e-05,6.96681e-09,-8.27826e-13,16497.4,8.58327], Tmin=(369.081,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (138.266,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (228.648,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 4, 'C-C': 2, 'C#C': 1, 'C=C': 1, 'C=O': 1}
1D rotors:
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 34.81 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       2.74819900   -0.67732300    0.17509900
C       1.55401300   -0.58731700    0.23512300
C       0.13943500   -0.50914600    0.30830000
C      -0.55960600    0.62805400    0.26432000
C      -2.02621400    0.59644300    0.34840800
O      -2.72446000    1.57485300    0.31596900
H       3.80836600   -0.74951700    0.12124800
H      -0.39025200   -1.45365500    0.40674000
H      -0.08285700    1.59577200    0.16714000
H      -2.46662300   -0.41816200    0.44698200
""",
)

entry(
    index = 15,
    label = "rxn_3_product_0",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {5,S} {9,S}
4  C u0 p0 c0 {1,S} {10,D} {11,S}
5  C u0 p0 c0 {3,S} {12,D} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 O u0 p2 c0 {4,D}
11 H u0 p0 c0 {4,S}
12 O u0 p2 c0 {5,D}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73087,0.0367184,-1.99435e-06,-1.75197e-08,7.48362e-12,-28096.6,11.6937], Tmin=(10,'K'), Tmax=(1084.29,'K')),
            NASAPolynomial(coeffs=[8.63936,0.033223,-1.7373e-05,4.36426e-09,-4.27629e-13,-30020,-16.3452], Tmin=(1084.29,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-233.576,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 2, 'C-H': 6, 'C-C': 3, 'C=C': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 36.83 kJ/mol
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: 
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 7], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
O       0.49669700   -3.09618000   -1.90346500
C       0.64182200   -1.94396800   -1.58964000
C      -0.14194900   -1.26683300   -0.54645400
C       0.06519600    0.01512700   -0.26454800
C      -0.68360700    0.79270000    0.76225700
C       0.19227100    1.63617200    1.65897500
O       1.37531700    1.76754900    1.52904400
H       1.40224900   -1.30710500   -2.08830900
H      -0.88535400   -1.86429800   -0.02882200
H       0.83481700    0.55704300   -0.80754800
H      -1.37842200    1.49249900    0.27758800
H      -1.30616500    0.14878900    1.38991100
H      -0.35225800    2.15928300    2.47106500
""",
)

entry(
    index = 16,
    label = "rxn_5_product_0",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,D} {7,S}
3  C u0 p0 c0 {1,S} {8,D} {9,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  O u0 p2 c0 {3,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65263,0.0377385,-0.000117658,3.18672e-07,-2.88336e-10,-12711.3,11.9246], Tmin=(10,'K'), Tmax=(406.902,'K')),
            NASAPolynomial(coeffs=[1.04544,0.0375815,-2.20194e-05,6.23309e-09,-6.84352e-13,-12285.7,24.7816], Tmin=(406.902,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-105.7,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (249.434,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 6, 'C-C': 2, 'C=C': 1, 'C=O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 9.62 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 9.73 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -1.84922700   -0.45339700   -0.22512700
C      -0.68976800    0.15159000   -0.42164000
C       0.44845700    0.12148200    0.54575300
C       1.77585300   -0.26804000   -0.05544500
O       1.97249000   -0.47443500   -1.21914000
H      -2.64587000   -0.39549700   -0.95563700
H      -2.04552800   -1.03199200    0.67133000
H      -0.52118800    0.70982100   -1.33626400
H       0.60593500    1.11098400    0.99710300
H       0.24847800   -0.55171800    1.38573000
H       2.60569900   -0.34298800    0.67868500
""",
)

entry(
    index = 17,
    label = "rxn_8_product_0",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {3,S} {8,S}
2  C u0 p0 c0 {1,D} {4,S} {7,S}
3  C u0 p0 c0 {1,S} {5,D} {9,S}
4  C u0 p0 c0 {2,S} {6,S} {10,D}
5  C u0 p0 c0 {3,D} {6,S} {11,S}
6  O u0 p2 c0 {4,S} {5,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 O u0 p2 c0 {4,D}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05967,-0.00646758,0.000175657,-3.10704e-07,1.7356e-10,-27801.2,10.6244], Tmin=(10,'K'), Tmax=(575.559,'K')),
            NASAPolynomial(coeffs=[0.57935,0.0449671,-2.94012e-05,9.06411e-09,-1.06137e-12,-27851.9,21.5718], Tmin=(575.559,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-231.177,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C=O': 1, 'C-H': 4, 'C-C': 2, 'C-O': 2}

External symmetry: 1, optical isomers: 1

Geometry:
O       2.62553500   -0.70370900   -0.01805100
C       1.46592600   -0.41335000   -0.01083700
C       0.89494700    0.91862200    0.03682000
C      -0.43778900    1.10752100    0.03973900
C      -1.32452400   -0.01227500   -0.00451800
C      -0.78050800   -1.23597100   -0.04824000
O       0.53830100   -1.45219800   -0.05221700
H       1.60144900    1.73499000    0.06926900
H      -0.84445200    2.11079400    0.07570700
H      -2.39700800    0.10517400   -0.00345000
H      -1.34187800   -2.15959700   -0.08422300
""",
)

entry(
    index = 18,
    label = "rxn_13_product_0",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {3,S} {6,S}
2  C u0 p0 c0 {1,D} {4,S} {7,S}
3  C u0 p0 c0 {1,S} {5,D} {8,S}
4  C u0 p0 c0 {2,S} {9,D} {10,S}
5  C u0 p0 c0 {3,D} {11,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  O u0 p2 c0 {4,D}
10 H u0 p0 c0 {4,S}
11 O u0 p2 c0 {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7092,0.0320205,4.07396e-06,-2.92945e-08,1.41191e-11,-15887.9,11.1839], Tmin=(10,'K'), Tmax=(881.785,'K')),
            NASAPolynomial(coeffs=[6.67799,0.0319824,-1.87054e-05,5.19873e-09,-5.56967e-13,-16933.5,-5.72575], Tmin=(881.785,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-132.094,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (253.591,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C=O': 2, 'C-H': 4, 'C-C': 2}
1D rotors:
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Bond ([[6, 7]]) broke during the scan. But unable to propose troubleshooting methods.Bond ([[6, 7]]) broke during the scan. But unable to propose troubleshooting methods.
pivots: [5, 6], dihedral: [4, 5, 6, 7], rotor symmetry: 1, max scan energy: 41.67 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O       3.60153400    0.23541700    0.37396600
C       2.45937200    0.35948900    0.37142900
C       1.14743300    0.51451600    0.38236900
C       0.29534100   -0.20679700   -0.52070200
C      -1.04720400   -0.11399000   -0.58240600
C      -1.86851800    0.74284900    0.26573300
O      -1.46220500    1.48361700    1.13573700
H       0.73371100    1.21033500    1.10214600
H       0.78522100   -0.88512200   -1.21177900
H      -1.57469200   -0.71488600   -1.31237900
H      -2.95623800    0.68218600    0.06531300
""",
)

entry(
    index = 19,
    label = "rxn_15_reactant_0",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,D} {7,S}
3  C u0 p0 c0 {5,D} {6,S} {7,S}
4  C u0 p0 c0 {2,D} {5,S} {11,S}
5  C u0 p0 c0 {3,D} {4,S} {12,S}
6  C u0 p0 c0 {3,S} {13,D} {14,S}
7  O u0 p2 c0 {2,S} {3,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 O u0 p2 c0 {6,D}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81109,0.0293513,3.06383e-05,-5.61779e-08,2.2499e-11,-28729,11.056], Tmin=(10,'K'), Tmax=(927.125,'K')),
            NASAPolynomial(coeffs=[5.29225,0.0430153,-2.39148e-05,6.38049e-09,-6.6111e-13,-29865.6,-0.625976], Tmin=(927.125,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-238.818,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (328.422,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-H': 6, 'C-C': 3, 'C-O': 2, 'C=O': 1}
1D rotors:
pivots: [1, 2], dihedral: [9, 1, 2, 3], rotor symmetry: 3, max scan energy: 3.83 kJ/mol
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 7], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
C      -2.27803500    0.53165300   -0.05412500
C      -0.91828200   -0.05006700   -0.13677500
C      -0.23614700   -0.67109800   -1.13874500
C       1.03505100   -1.00767500   -0.61131100
C       1.04053600   -0.56878600    0.67573000
C       2.03534200   -0.61114800    1.73338800
O       3.13044500   -1.10013100    1.60705800
O      -0.15497100    0.01761800    0.96708200
H      -2.78930500    0.41293300   -1.00754400
H      -2.86631100    0.03732000    0.72121100
H      -2.23226600    1.59525200    0.18720900
H      -0.60690400   -0.86067900   -2.13212200
H       1.85246100   -1.50856100   -1.10211100
H       1.70950300   -0.15166700    2.68708400
""",
)

entry(
    index = 20,
    label = "rxn_15_product_0",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,D}
3  C u0 p0 c0 {2,S} {4,D} {11,S}
4  C u0 p0 c0 {3,D} {5,S} {12,S}
5  C u0 p0 c0 {4,S} {6,D} {13,S}
6  C u0 p0 c0 {5,D} {14,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 O u0 p2 c0 {2,D}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 O u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.45511,0.0564293,-0.000116208,2.70794e-07,-2.4601e-10,-22788.2,12.4582], Tmin=(10,'K'), Tmax=(386.324,'K')),
            NASAPolynomial(coeffs=[2.12805,0.0526173,-3.32557e-05,1.00389e-08,-1.16209e-12,-22554.7,19.2935], Tmin=(386.324,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-189.483,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (328.422,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-H': 6, 'C-C': 3, 'C=O': 2}
1D rotors:
pivots: [1, 2], dihedral: [9, 1, 2, 3], rotor symmetry: 3, max scan energy: 2.74 kJ/mol
* Invalidated! pivots: [2, 4], dihedral: [1, 2, 4, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 7], invalidation reason: Bond ([[2, 3]]) broke during the scan. But unable to propose troubleshooting methods.Bond ([[2, 3]]) broke during the scan. But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
C      -2.55857200   -0.08043500   -0.06261200
C      -1.09359900   -0.24959100    0.26511800
O      -0.70150900   -0.20539500    1.41558200
C      -0.20306000   -0.46604700   -0.88535200
C       1.12863200   -0.63904700   -0.81592600
C       1.92419600   -0.64501000    0.38236700
C       3.23117800   -0.82348000    0.34735800
O       4.37077400   -0.97768300    0.33356900
H      -2.69643900    0.77174700   -0.73237600
H      -2.92965600   -0.96475000   -0.58614800
H      -3.12819300    0.07296800    0.85062500
H      -0.66684200   -0.48614000   -1.86386800
H       1.66232900   -0.78926900   -1.74892000
H       1.46454700   -0.50160300    1.35256600
""",
)

entry(
    index = 21,
    label = "rxn_16_product_0",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {3,S} {9,S}
2  C u0 p0 c0 {1,D} {4,S} {10,S}
3  C u0 p0 c0 {1,S} {5,D} {8,S}
4  C u0 p0 c0 {2,S} {6,S} {7,D}
5  C u0 p0 c0 {3,D} {12,S} {13,S}
6  C u0 p0 c0 {4,S} {11,D} {14,S}
7  O u0 p2 c0 {4,D}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {6,D}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68098,0.0425233,5.7632e-06,-3.86103e-08,1.80422e-11,-18548.8,11.716], Tmin=(10,'K'), Tmax=(922.721,'K')),
            NASAPolynomial(coeffs=[9.04101,0.0398034,-2.31662e-05,6.38739e-09,-6.77954e-13,-20411.3,-18.4446], Tmin=(922.721,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-154.183,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (324.264,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-H': 6, 'C=O': 2, 'C-C': 3}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 29.68 kJ/mol
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: 
pivots: [5, 7], dihedral: [4, 5, 7, 8], rotor symmetry: 1, max scan energy: 25.39 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C      -3.00644800    0.45503300    0.37391200
C      -1.76941500    0.15385000    0.76024300
C      -0.65658900    0.07277500   -0.16380100
C       0.59791600   -0.22702800    0.19025500
C       1.66837600   -0.28845600   -0.80951700
O       1.53938600   -0.08598500   -1.99547500
C       3.07473600   -0.64026500   -0.30735600
O       3.33689900   -0.86298900    0.83867600
H      -3.82362200    0.51029600    1.08107200
H      -3.23731200    0.65577700   -0.66617200
H      -1.55926300   -0.04377000    1.80671200
H      -0.86151000    0.26978300   -1.21306600
H       0.86814800   -0.43377400    1.21863900
H       3.82833300   -0.66761800   -1.11762600
""",
)

entry(
    index = 22,
    label = "rxn_17_product_0",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {7,S}
3  C u0 p0 c0 {2,D} {4,S} {11,S}
4  C u0 p0 c0 {3,S} {5,D} {12,S}
5  C u0 p0 c0 {4,D} {6,S} {13,S}
6  C u0 p0 c0 {5,S} {7,S} {14,D}
7  O u0 p2 c0 {2,S} {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 O u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81265,0.0167653,0.000107467,-2.00839e-07,1.09155e-10,-34508.3,11.3588], Tmin=(10,'K'), Tmax=(602.818,'K')),
            NASAPolynomial(coeffs=[1.35727,0.0531398,-3.30144e-05,9.78407e-09,-1.11289e-12,-34577.1,18.9354], Tmin=(602.818,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-286.952,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (328.422,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-H': 6, 'C-C': 3, 'C-O': 2, 'C=O': 1}
1D rotors:
pivots: [1, 2], dihedral: [9, 1, 2, 3], rotor symmetry: 3, max scan energy: 6.25 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       2.21702700   -0.13497900   -0.02465400
C       0.73396300   -0.02815300   -0.04467400
C      -0.02908000    0.28051200   -1.10940000
C      -1.44390300    0.33676200   -0.93875600
C      -2.00269900    0.08661900    0.26059600
C      -1.18185900   -0.24509000    1.40459400
O      -1.54724300   -0.48776400    2.51765300
O       0.18891000   -0.27968700    1.15653400
H       2.63396300    0.57021600    0.69651400
H       2.63068800    0.07347600   -1.00909900
H       2.51649100   -1.13764600    0.28551100
H       0.43230600    0.47860700   -2.06458900
H      -2.07070700    0.58398700   -1.78707900
H      -3.06861500    0.11907700    0.43039200
""",
)

entry(
    index = 23,
    label = "rxn_19_product_0",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {4,D} {5,S} {6,S}
4  C u0 p0 c0 {3,D} {7,S} {12,S}
5  C u0 p0 c0 {3,S} {13,D} {14,S}
6  O u0 p2 c0 {1,S} {3,S}
7  C u2 p0 c0 {1,S} {4,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 O u0 p2 c0 {5,D}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72975,0.0256162,7.25088e-05,-1.4226e-07,7.38042e-11,11623,13.2459], Tmin=(10,'K'), Tmax=(662.65,'K')),
            NASAPolynomial(coeffs=[2.93469,0.050995,-3.15245e-05,9.27116e-09,-1.04602e-12,11276.5,13.3451], Tmin=(662.65,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (96.6064,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (328.422,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 6, 'C-C': 4, 'C-O': 2, 'C=C': 1, 'C=O': 1}
1D rotors:
pivots: [1, 2], dihedral: [9, 1, 2, 3], rotor symmetry: 3, max scan energy: 13.77 kJ/mol
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 7], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
C       2.10247900   -0.61410200    0.00349200
C       1.05450100    0.34300300   -0.52964700
C       0.53580000    1.34659200    0.44271400
C      -0.77966600    1.22156400    0.66131800
C      -1.19024600    0.14187300   -0.16331500
C      -2.49649200   -0.41983300   -0.32297700
O      -3.47881600   -0.00532900    0.27024600
O      -0.15572700   -0.38207500   -0.86207200
H       1.74511200   -1.10121900    0.91065600
H       3.01627300   -0.06575100    0.23460300
H       2.32910500   -1.37341300   -0.74434600
H       1.40627100    0.81693800   -1.45189800
H      -1.44035300    1.77894900    1.30494200
H      -2.55607100   -1.26685300   -1.03036300
""",
)

entry(
    index = 24,
    label = "rxn_20_product_0",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {4,D} {6,S}
4  C u0 p0 c0 {3,D} {7,S} {13,S}
5  C u0 p0 c0 {1,S} {12,D} {14,S}
6  O u0 p2 c0 {1,S} {3,S}
7  C u2 p0 c0 {1,S} {4,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 O u0 p2 c0 {5,D}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.58374,0.0393025,9.72966e-06,-4.36955e-08,2.15558e-11,15441.3,13.3931], Tmin=(10,'K'), Tmax=(813.66,'K')),
            NASAPolynomial(coeffs=[5.50792,0.0442443,-2.59297e-05,7.27452e-09,-7.88544e-13,14651.5,1.57744], Tmin=(813.66,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (128.361,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (324.264,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 6, 'C-C': 4, 'C-O': 2, 'C=C': 1, 'C=O': 1}
1D rotors:
pivots: [1, 2], dihedral: [9, 1, 2, 3], rotor symmetry: 3, max scan energy: 5.99 kJ/mol
pivots: [5, 6], dihedral: [4, 5, 6, 7], rotor symmetry: 1, max scan energy: 19.43 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       2.10437800   -0.77685400    0.24743500
C       0.83664700   -0.02492200    0.15753800
C      -0.04038800    0.42476700    1.11589000
C      -1.07318400    1.04505100    0.44194800
C      -0.81391500    1.02878100   -1.02578100
C      -0.58827600    2.44407200   -1.55084600
O      -1.43380100    3.08403900   -2.10123500
O       0.41588200    0.29112500   -1.10844700
H       2.02975400   -1.72684800   -0.28848400
H       2.92538000   -0.21126000   -0.20130400
H       2.34855300   -0.98104800    1.28850600
H       0.07312100    0.28685200    2.17881100
H      -1.58297400    0.53805600   -1.62959700
H       0.42445800    2.84432800   -1.34099300
""",
)

entry(
    index = 25,
    label = "rxn_21_product_0",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {4,S} {5,S} {6,S} {8,S}
2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {4,D} {7,S}
4  C u0 p0 c0 {1,S} {3,D} {12,S}
5  C u0 p0 c0 {1,S} {13,D} {14,S}
6  C u2 p0 c0 {1,S} {7,S}
7  O u0 p2 c0 {3,S} {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 O u0 p2 c0 {5,D}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70503,0.0382096,4.91167e-06,-2.83074e-08,1.19845e-11,20925.3,13.3406], Tmin=(10,'K'), Tmax=(1001.97,'K')),
            NASAPolynomial(coeffs=[7.59439,0.0391853,-2.12541e-05,5.53985e-09,-5.6203e-13,19317.5,-9.56478], Tmin=(1001.97,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (174.016,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (328.422,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 6, 'C-C': 4, 'C-O': 2, 'C=C': 1, 'C=O': 1}
1D rotors:
pivots: [1, 2], dihedral: [9, 1, 2, 3], rotor symmetry: 3, max scan energy: 6.99 kJ/mol
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: Another conformer for rxn_21_product_0 exists which is 5.37 kJ/mol lower.Another conformer for rxn_21_product_0 exists which is 5.37 kJ/mol lower.


External symmetry: 1, optical isomers: 2

Geometry:
C       2.38286500   -0.01737100    0.16302300
C       0.92458700   -0.26421000    0.14029500
C      -0.09200300    0.31136900    0.77427500
C      -1.39319300   -0.31761500    0.34367500
C      -2.33565900    0.61295700   -0.41881900
O      -2.18843300    1.79575800   -0.51476000
C      -0.81916900   -1.37599700   -0.55148800
O       0.51564600   -1.28604300   -0.70644400
H       2.91855600   -0.91160000    0.48646600
H       2.73982100    0.24492200   -0.83443900
H       2.61016800    0.79929400    0.84557200
H      -0.01541400    1.13865500    1.45982900
H      -1.97614100   -0.74549700    1.17373900
H      -3.19096700    0.09619400   -0.89980000
""",
)

entry(
    index = 26,
    label = "rxn_22_product_0",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,D} {7,S}
3  C u0 p0 c0 {4,S} {5,D} {6,S}
4  C u0 p0 c0 {2,D} {3,S} {11,S}
5  C u0 p0 c0 {3,D} {7,S} {12,S}
6  C u0 p0 c0 {3,S} {13,D} {14,S}
7  O u0 p2 c0 {2,S} {5,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 O u0 p2 c0 {6,D}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.6254,0.035032,1.56289e-05,-4.18809e-08,1.78554e-11,-28408.6,10.7596], Tmin=(10,'K'), Tmax=(905.737,'K')),
            NASAPolynomial(coeffs=[4.82574,0.0448767,-2.57581e-05,7.04423e-09,-7.44746e-13,-29247.3,1.65797], Tmin=(905.737,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-236.215,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (324.264,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-H': 6, 'C-C': 3, 'C-O': 2, 'C=O': 1}
1D rotors:
pivots: [1, 2], dihedral: [9, 1, 2, 3], rotor symmetry: 3, max scan energy: 4.66 kJ/mol
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 2, max scan energy: 36.68 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C      -2.45722900    0.06665000   -0.02852700
C      -0.97899800    0.15230000   -0.01231700
C      -0.09741800    1.12771400   -0.31210800
C       1.20742300    0.57664400   -0.08799500
C       2.50774600    1.21378400   -0.26182100
O       2.66681300    2.34769600   -0.63661300
C       1.00291000   -0.69813200    0.33257800
O      -0.30747400   -0.97137600    0.38426900
H      -2.87415900    1.01616900   -0.35907800
H      -2.79722900   -0.71744700   -0.70770800
H      -2.84804600   -0.15713900    0.96589400
H      -0.32101000    2.12433200   -0.65255600
H       3.37784100    0.57003800   -0.01988100
H       1.67470200   -1.49055000    0.61827100
""",
)

entry(
    index = 27,
    label = "rxn_24_reactant_0",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,D}
3  C u0 p0 c0 {2,S} {6,D} {11,S}
4  C u0 p0 c0 {5,S} {6,D} {12,S}
5  C u0 p0 c0 {4,S} {13,D} {14,S}
6  C u0 p0 c0 {3,D} {4,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 O u0 p2 c0 {2,D}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 O u0 p2 c0 {5,D}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.50741,0.048949,-1.93147e-05,-9.71166e-09,7.22263e-12,-15911,13.2998], Tmin=(10,'K'), Tmax=(941.307,'K')),
            NASAPolynomial(coeffs=[8.93754,0.0381904,-2.1797e-05,5.9465e-09,-6.27696e-13,-17478.9,-15.4673], Tmin=(941.307,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-132.308,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (320.107,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-H': 6, 'C=O': 2, 'C-C': 3}
1D rotors:
pivots: [1, 2], dihedral: [9, 1, 2, 3], rotor symmetry: 3, max scan energy: 2.45 kJ/mol
pivots: [2, 4], dihedral: [1, 2, 4, 5], rotor symmetry: 1, max scan energy: 24.35 kJ/mol
pivots: [6, 7], dihedral: [5, 6, 7, 8], rotor symmetry: 1, max scan energy: 33.52 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -2.39718000    1.99861400   -0.68128100
C      -1.18489600    1.14104300   -0.43453600
O      -0.51225100    0.68845300   -1.32524300
C      -0.81067700    0.84270400    0.98436800
C      -1.46721500    1.28829800    2.01476900
C      -2.16418900    1.70869200    3.03405600
C      -3.28458600    0.90110500    3.56512800
O      -3.96506000    1.24782300    4.49090100
H      -3.28536600    1.52723300   -0.25598400
H      -2.52946700    2.13505500   -1.75134000
H      -2.28102100    2.96853500   -0.19404800
H       0.06820000    0.22123700    1.11825100
H      -1.94884100    2.65398300    3.52009900
H      -3.45725700   -0.05908400    3.04180700
""",
)

entry(
    index = 28,
    label = "rxn_24_product_0",
    molecule = 
"""
1  O u0 p2 c0 {4,D}
2  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,D} {2,S} {3,S}
5  C u0 p0 c0 {2,S} {6,T}
6  C u0 p0 c0 {5,T} {12,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92471,0.00827037,0.000286448,-1.26854e-06,1.9497e-09,804.127,12.4442], Tmin=(10,'K'), Tmax=(163.642,'K')),
            NASAPolynomial(coeffs=[2.52586,0.0424633,-2.69753e-05,8.3263e-09,-9.90151e-13,849.909,16.6608], Tmin=(163.642,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (6.84778,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (278.535,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 6, 'C-C': 3, 'C#C': 1, 'C=O': 1}
1D rotors:
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 9.76 kJ/mol
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 10], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
C       2.14083700   -0.25390600    1.35752300
C       1.48421000   -0.26501400    0.35681300
C       0.67283700   -0.28082500   -0.85128100
C      -0.70410800    0.38525200   -0.73502100
C      -0.83939700    1.54838100    0.20703300
O      -1.61045000   -0.01375000   -1.41571200
H       2.72873000   -0.24855400    2.24389300
H       0.51629400   -1.30043200   -1.20439900
H       1.20123400    0.25327700   -1.64914100
H      -0.02607400    2.26106400    0.05508200
H      -1.80325900    2.02948100    0.06164500
H      -0.75204500    1.19147400    1.23547200
""",
)

entry(
    index = 29,
    label = "rxn_25_product_0",
    molecule = 
"""
1 O u0 p2 c0 {4,D}
2 O u0 p2 c0 {5,D}
3 C u0 p0 c0 {4,S} {5,D} {6,S}
4 C u0 p0 c0 {1,D} {3,S} {7,S}
5 C u0 p0 c0 {2,D} {3,D}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93092,0.00639976,8.54959e-05,-2.55699e-07,2.51046e-10,-22920.7,9.27635], Tmin=(10,'K'), Tmax=(258.932,'K')),
            NASAPolynomial(coeffs=[2.79981,0.0238733,-1.57291e-05,4.9245e-09,-5.87636e-13,-22862.2,13.205], Tmin=(258.932,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-190.56,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 2, 'C-H': 2, 'C-C': 1, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
O       2.38578800    0.06596400    0.60550100
C       1.33490100    0.25321500    0.19599800
C       0.11246900    0.45848500   -0.27206700
C      -0.94954900   -0.48525600    0.06201500
O      -0.81831400   -1.46888100    0.74704600
H      -0.05798200    1.32652000   -0.89146200
H      -1.92806500   -0.22002500   -0.37927600
""",
)

