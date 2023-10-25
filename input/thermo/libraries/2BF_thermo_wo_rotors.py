#!/usr/bin/env python
# encoding: utf-8

name = "2BF_thermo_wo_rotors"
shortDesc = ""
longDesc = """
ARC v1.1.0
ARC projects 2BF_thermo_1, 2BF_thermo_2, 2BF_thermo_3, 2BF_thermo_4

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
    label = "TB7",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {5,S}
2  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {5,D} {9,S}
4  C u0 p0 c0 {2,S} {6,D} {10,S}
5  C u0 p0 c0 {1,S} {3,D} {6,S}
6  C u0 p0 c0 {4,D} {5,S} {11,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.0945,-0.00914745,0.000179528,-3.11949e-07,1.72915e-10,7230.53,10.5421], Tmin=(10,'K'), Tmax=(575.423,'K')),
            NASAPolynomial(coeffs=[0.211161,0.0442362,-2.8421e-05,8.6726e-09,-1.00923e-12,7240.56,23.3346], Tmin=(575.423,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (60.099,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 3, 'C-H': 5, 'C-O': 1, 'C=C': 2}

External symmetry: 1, optical isomers: 1

Geometry:
O      -2.11183600    1.44157200   -0.34260300
C      -1.09179700    0.77674700   -0.18192800
C      -1.00461600   -0.65589200    0.04189600
C       0.42204500   -1.06270700    0.18675400
C       1.16236300    0.25104200    0.02907400
C       0.31953000    1.26955000   -0.17533300
H      -1.86259200   -1.31232300    0.09237900
H       0.72574600   -1.79975800   -0.57011800
H       0.62553700   -1.53589300    1.15784600
H       2.24203400    0.31669200    0.08166200
H       0.57358500    2.31097000   -0.31962800
""",
)

entry(
    index = 1,
    label = "TB11",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {3,D}
3 C u1 p0 c0 {2,D} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94764,0.00319149,5.64828e-05,-1.18956e-07,7.50654e-11,41022.3,5.4829], Tmin=(10,'K'), Tmax=(537.535,'K')),
            NASAPolynomial(coeffs=[3.91782,0.0150707,-9.19614e-06,2.84527e-09,-3.46567e-13,40857.1,4.04168], Tmin=(537.535,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (341.061,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 3, 'C=C': 2}

External symmetry: 2, optical isomers: 1

Geometry:
C       1.50226700   -0.00969800    0.11174200
C       0.28357700   -0.00183100    0.02109300
C      -1.07978000    0.00697100   -0.08031700
H       2.56148000   -0.01653600    0.19052900
H      -1.62316900    0.93822700   -0.18356100
H      -1.64437500   -0.91713300   -0.05948700
""",
)