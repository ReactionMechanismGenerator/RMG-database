#!/usr/bin/env python
# encoding: utf-8

name = "Keceli_Butane_CBS_TZMQZ"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 0,
    label = "C3H7O2_99",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  O u0 p2 c0 {1,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u1 p2 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.90614,0.0186315,2.9518e-05,-5.05607e-08,2.13224e-11,-10246.8,6.51972], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.62439,0.0295082,-1.4426e-05,3.43324e-09,-3.2256e-13,-10924.9,0.0667037], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3CH(OO)CH3
[O]OC(C)C_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -10.29 kcal/mol
deltaH(298) -15.47 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 1,
    label = "C3H4_33",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {3,S} {6,S}
3 C u1 p0 c0 {1,S} {2,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.68477,0.00150474,5.37557e-05,-7.55241e-08,3.14432e-11,32606.8,11.65], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.40765,0.0168471,-8.12187e-06,1.90862e-09,-1.7718e-13,31804.4,4.34717], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""cyc-CH2CHCH
C1[CH][CH]1_m1 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 69.32 kcal/mol
deltaH(298) 67.20 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "C3H4_32",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.69025,0.0152307,3.45169e-06,-1.46171e-08,7.00765e-12,20630.7,9.84558], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.47605,0.0164149,-7.75357e-06,1.78929e-09,-1.63521e-13,20320.5,5.15984], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3CCH
CC#C_m1 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 45.66 kcal/mol
deltaH(298) 43.95 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "C3H4_31",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 C u2 p0 c0 {1,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.58915,0.0181619,8.59871e-06,-2.80022e-08,1.38275e-11,47607.5,17.137], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.67137,0.0151924,-7.20595e-06,1.67074e-09,-1.5341e-13,46656.2,0.321897], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""3CH2CHCH
[CH]C=C_m3 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 99.06 kcal/mol
deltaH(298) 97.21 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "C2H5O_49",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {8,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C u1 p0 c0 {2,S} {6,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.03413,0.00679742,2.26162e-05,-3.212e-08,1.2791e-11,-5357.17,3.51677], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.3947,0.0168357,-7.68692e-06,1.73107e-09,-1.55813e-13,-5509.24,5.00015], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH2CH2OH
[CH2]CO_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -3.85 kcal/mol
deltaH(298) -6.78 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "C2H4O_45",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,D} {7,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.15907,-0.00666593,5.3557e-05,-6.19376e-08,2.31658e-11,-21880,2.36577], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.9968,0.0183962,-9.08471e-06,2.17486e-09,-2.04814e-13,-21722.2,14.9406], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3CHO
CC=O_m1 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -37.76 kcal/mol
deltaH(298) -40.29 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "C2H3O4_173",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {6,S}
2 C u0 p0 c0 {1,D} {4,S} {7,S}
3 O u0 p2 c0 {1,S} {5,S}
4 O u0 p2 c0 {2,S} {8,S}
5 O u0 p2 c0 {3,S} {9,S}
6 O u1 p2 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.90421,0.0357432,-1.21605e-05,-1.24884e-08,7.59972e-12,-43517.6,13.5668], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.4821,0.0194734,-1.26615e-05,3.71138e-09,-4.07078e-13,-46242.2,-32.5647], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""HOOC(O)CHOH
OO/C(=C\O)/[O]_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -78.81 kcal/mol
deltaH(298) -81.86 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "C4H9_68",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {2,S} {12,S} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.64246,0.00371093,7.81545e-05,-1.04381e-07,4.19153e-11,6991.7,3.87379], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.90623,0.0338831,-1.61501e-05,3.74577e-09,-3.43086e-13,6496.62,7.36958], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3CH2CH2CH2
CCC[CH2]_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 24.07 kcal/mol
deltaH(298) 18.57 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "C2H4O_46",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 O u0 p2 c0 {1,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.14272,0.0247906,-1.06391e-05,-8.00974e-09,6.54787e-12,-16531.3,17.7877], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.6798,0.012655,-5.62203e-06,1.22552e-09,-1.05984e-13,-17651,-5.34135], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""OHCHCH2
OC=C_m1 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -27.66 kcal/mol
deltaH(298) -30.20 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "C2H5O3_104",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  O u0 p2 c0 {1,S} {9,S}
4  O u0 p2 c0 {1,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u1 p2 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.26135,0.0314648,-2.02246e-05,4.33118e-09,6.89448e-13,-28792.8,7.94089], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.32154,0.0196888,-9.52256e-06,2.24266e-09,-2.08296e-13,-29830.7,-12.7603], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3CH(OH)OO
[O]O[C@@H](O)C_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -48.36 kcal/mol
deltaH(298) -52.25 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "CHO3_76",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {5,S}
2 O u1 p2 c0 {4,S}
3 O u0 p2 c0 {4,D}
4 C u0 p0 c0 {1,S} {2,S} {3,D}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.0681,0.017882,-1.031e-05,-2.51828e-09,3.21187e-12,-42514.6,16.8191], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.45415,0.00644528,-3.34705e-06,8.70496e-10,-8.92565e-14,-43690.3,-5.82775], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""OHC(O)O
OC(=O)[O]_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -80.37 kcal/mol
deltaH(298) -81.87 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "C4H9_67",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {3,S} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.97981,-0.0129358,0.000111886,-1.33491e-07,5.13003e-11,5337.52,-5.12799], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.71321,0.0330463,-1.50213e-05,3.2824e-09,-2.81249e-13,5038.47,9.12047], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3CHCH2CH3
C[CH]CC_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 21.06 kcal/mol
deltaH(298) 15.68 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "C4H6_54",
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
            NASAPolynomial(coeffs=[2.4621,0.0128351,5.99064e-05,-9.79492e-08,4.31699e-11,11405.3,13.7308], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.05763,0.0210224,-9.60053e-06,2.13172e-09,-1.86938e-13,9536.23,-13.9689], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH2CHCHCH2
C=CC=C_m1 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 29.45 kcal/mol
deltaH(298) 25.96 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "CH3_7",
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
            NASAPolynomial(coeffs=[3.71211,0.00284275,2.44314e-06,-3.09599e-09,1.09699e-12,16161.8,1.30806], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.52805,0.00653296,-2.47567e-06,4.43977e-10,-3.0328e-14,16480.8,7.35825], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3
[CH3]_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 35.38 kcal/mol
deltaH(298) 34.60 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "C2O_30",
    molecule = 
"""
multiplicity 3
1 O u1 p1 c+1 {2,D}
2 C u0 p1 c-1 {1,D} {3,S}
3 C u1 p1 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.6921,0.0131374,-2.09243e-05,1.64894e-08,-5.13145e-12,43882.2,9.57344], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.29159,0.00178055,-1.07695e-06,2.99588e-10,-3.16025e-14,43372.8,-2.82839], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""3CCO
[C][C][O]_m3 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 88.70 kcal/mol
deltaH(298) 89.65 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "CH_4",
    molecule = 
"""
multiplicity 2
1 C u1 p1 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.46483,0.000443729,-1.92764e-06,3.21412e-09,-1.41356e-12,69937,1.46482], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.73766,0.00148761,-5.19117e-07,7.91511e-11,-3.82597e-15,70174.5,5.4323], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH
[CH]_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 140.24 kcal/mol
deltaH(298) 141.05 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "C_3",
    molecule = 
"""
multiplicity 3
1 C u2 p1 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.55374,-0.000320299,7.33672e-07,-7.34994e-10,2.68424e-13,84607,4.51715], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.50333,-4.55225e-06,2.14221e-09,-3.91682e-13,1.7293e-17,84613.4,4.73765], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""3C
[C]_m3        torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 168.32 kcal/mol
deltaH(298) 169.63 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "C4H8_59",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {2,S} {3,D} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.92769,0.00037473,7.14086e-05,-8.86527e-08,3.39824e-11,-3883.85,-0.768535], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.23667,0.0336952,-1.642e-05,3.89283e-09,-3.64014e-13,-3843.98,13.06], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH2CHCHCH3;trans
C/C=C/C_m1 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 1.71 kcal/mol
deltaH(298) -3.24 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "C2O4_119",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {5,S}
2 O u0 p2 c0 {1,S} {6,S}
3 O u0 p2 c0 {5,D}
4 O u0 p2 c0 {6,D}
5 C u0 p0 c0 {1,S} {3,D} {6,S}
6 C u0 p0 c0 {2,S} {4,D} {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.10119,0.0348727,-3.64033e-05,1.75155e-08,-2.86236e-12,-39445.4,19.7868], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.1184,0.0108809,-6.30017e-06,1.69992e-09,-1.75396e-13,-41084.7,-15.1461], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""cyc-C(O)OOC(O)-
O=C1OOC1=O_m1 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -74.07 kcal/mol
deltaH(298) -75.23 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "CH4O_26",
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
            NASAPolynomial(coeffs=[5.66375,-0.0148826,6.30443e-05,-6.81471e-08,2.49144e-11,-25838.8,-1.26112], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.49115,0.0143348,-6.58348e-06,1.48315e-09,-1.32775e-13,-25463.7,16.2104], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3OH
CO_m1 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -45.84 kcal/mol
deltaH(298) -48.44 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "C2H3O4_135",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {6,D}
2 C u1 p0 c0 {1,S} {4,S} {7,S}
3 O u0 p2 c0 {1,S} {5,S}
4 O u0 p2 c0 {2,S} {8,S}
5 O u0 p2 c0 {3,S} {9,S}
6 O u0 p2 c0 {1,D}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.75482,0.0360279,-1.05543e-05,-1.73001e-08,1.06079e-11,-44642.7,14.1812], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.4217,0.020971,-1.3203e-05,3.74576e-09,-3.99297e-13,-46958.3,-26.6621], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""OHCHC(O)OOH
O[CH]C(=O)OO_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -81.08 kcal/mol
deltaH(298) -84.14 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "HO_10",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.13036,-0.00330779,6.80653e-06,-6.23913e-09,2.25491e-12,3273.44,-0.743345], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.35545,-7.51826e-05,5.74643e-07,-2.40416e-10,3.03818e-14,3454.57,3.04944], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""OH
[OH]_m2       torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 8.60 kcal/mol
deltaH(298) 8.76 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "C2H6_22",
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
            NASAPolynomial(coeffs=[4.51902,-0.00664399,5.93419e-05,-6.83202e-08,2.55285e-11,-11708.6,1.71075], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.480181,0.0221479,-1.03341e-05,2.34e-09,-2.08877e-13,-11358,18.5371], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3CH3
CC_m1 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -16.65 kcal/mol
deltaH(298) -20.38 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "C3H3O5_159",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {7,S}
2  O u0 p2 c0 {1,S} {8,S}
3  O u0 p2 c0 {5,S} {6,S}
4  O u0 p2 c0 {8,D}
5  O u1 p2 c0 {3,S}
6  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
7  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
8  C u0 p0 c0 {2,S} {4,D} {6,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.0885,0.00823549,7.06113e-05,-1.0469e-07,4.37706e-11,-24190,-0.0608228], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.396,0.0249839,-1.34853e-05,3.4672e-09,-3.45881e-13,-26055.5,-22.6316], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""cyc-CH2OOC(O)CH(OO)-
[O]O[C@H]1COOC1=O_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -38.60 kcal/mol
deltaH(298) -42.27 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "C4H7_56",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  C u1 p0 c0 {3,S} {10,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.56776,0.00515182,6.47766e-05,-8.84478e-08,3.57235e-11,13754.7,6.4324], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.65203,0.0293616,-1.4335e-05,3.41493e-09,-3.21651e-13,13179.4,6.49446], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3CHCHCH2;trans
C/C=C/[CH2]_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 35.49 kcal/mol
deltaH(298) 31.32 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "H2_2",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49063,8.14043e-05,-2.35648e-07,2.09347e-10,2.11875e-14,-1017.67,-4.24702], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.67879,-0.000808224,9.99232e-07,-3.42203e-10,3.93194e-14,-1038.39,-5.09533], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""[H][H]_m1 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "C4H9O4_164",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {3,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.41919,0.0619955,-4.00157e-05,4.03146e-09,4.60503e-12,-22870.7,5.74388], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.0689,0.0362547,-1.84112e-05,4.57252e-09,-4.49424e-13,-24975.9,-37.9844], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3CH(OOH)CH2CH2OO
[O]OCC[C@@H](OO)C_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -30.93 kcal/mol
deltaH(298) -37.44 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "C4H5O_79",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  C u0 p0 c0 {2,S} {5,D} {6,S}
4  C u1 p0 c0 {2,S} {7,S} {8,S}
5  C u0 p0 c0 {3,D} {9,S} {10,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.57646,0.022522,1.75492e-05,-4.18368e-08,1.92204e-11,6374.26,10.6205], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.28227,0.0223639,-1.09893e-05,2.62017e-09,-2.45842e-13,5039.32,-10.5034], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH2C(O)CHCH2
[CH2]C(=O)C=C_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 19.79 kcal/mol
deltaH(298) 16.94 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "C4H9O_96",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4  C u0 p0 c0 {5,S} {10,S} {11,S} {12,S}
5  C u1 p0 c0 {2,S} {4,S} {13,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.54242,0.0124903,4.53736e-05,-6.25706e-08,2.4349e-11,-15009.3,-3.64352], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.75224,0.0344009,-1.64822e-05,3.87606e-09,-3.62353e-13,-15225.2,1.76883], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3CHCH(OH)CH3
C[CH][C@@H](O)C_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -18.14 kcal/mol
deltaH(298) -23.68 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "C4H9O4_163",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {3,S} {7,S}
6  O u0 p2 c0 {1,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.52972,0.040454,7.83448e-05,-1.63875e-07,7.7829e-11,-22851,11.3622], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[21.3989,0.0248086,-1.11651e-05,2.45353e-09,-2.13506e-13,-28034.5,-80.6981], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3CH(OO)CH2CH2OOH
OOCC[C@@H](O[O])C_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -31.27 kcal/mol
deltaH(298) -38.35 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "C4H10_72",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
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
            NASAPolynomial(coeffs=[6.48755,-0.00310671,9.97436e-05,-1.25611e-07,4.92033e-11,-17897.1,-1.88254], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.43598,0.0392181,-1.90081e-05,4.49011e-09,-4.18997e-13,-18024.8,12.1944], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3CH2CH2CH3
CCCC_m1 ,  torsopt/wb97xd/cc-pvtz/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_tzmqz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -24.17 kcal/mol
deltaH(298) -30.69 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "C4H8_61",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.77559,0.00318949,7.61656e-05,-1.01525e-07,4.06778e-11,-2240.27,6.00691], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.29518,0.0322413,-1.5575e-05,3.66236e-09,-3.39922e-13,-2798.74,8.24388], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3CH2CHCH2
CCC=C_m1 ,  torsopt/wb97xd/cc-pvtz/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_tzmqz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 4.65 kcal/mol
deltaH(298) -0.36 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "C3H6O_71",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {10,S}
2  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
3  C u0 p0 c0 {2,S} {4,D} {8,S}
4  C u0 p0 c0 {1,S} {3,D} {9,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.47439,0.00693592,4.94936e-05,-7.02862e-08,2.88009e-11,-20427.4,7.04086], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.23783,0.0245127,-1.19002e-05,2.83685e-09,-2.6851e-13,-20981.5,4.68814], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3CHCHOH;cis
C/C=C\O_m1 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -32.72 kcal/mol
deltaH(298) -36.71 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "CH3O3_78",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {4,S} {7,S}
3 O u1 p2 c0 {1,S}
4 C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.71496,0.0215992,-7.1723e-06,-8.67852e-09,5.87773e-12,-22046.9,15.0559], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.54975,0.0128581,-6.53328e-06,1.62622e-09,-1.59706e-13,-23092.8,-4.93782], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""OOCH2OH
[O]OCO_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -37.62 kcal/mol
deltaH(298) -40.45 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    label = "C3H6O2_97",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {11,S}
3  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
4  C u0 p0 c0 {3,S} {5,D} {8,S}
5  C u0 p0 c0 {4,D} {9,S} {10,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.56567,0.0271671,-7.95643e-06,-6.46825e-09,3.99946e-12,-9084.58,1.55071], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.41614,0.0242925,-1.20497e-05,2.93056e-09,-2.81987e-13,-9626.76,-8.37329], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH2CHCH2OOH
OOCC=C_m1 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -8.74 kcal/mol
deltaH(298) -12.52 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "H2O2_28",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.4002,-0.00178517,1.90689e-05,-2.35612e-08,9.22341e-12,-17671.3,2.94776], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.09603,0.00482373,-1.91902e-06,3.74642e-10,-2.91788e-14,-17809,3.26848], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""OHOH
OO_m1 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -30.98 kcal/mol
deltaH(298) -32.42 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
    label = "C2H3_16",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 C u0 p1 c0 {1,S} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.14081,0.00233818,2.3568e-05,-3.34831e-08,1.39525e-11,34311.5,8.6984], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.94645,0.0103584,-4.76441e-06,1.07148e-09,-9.55904e-14,34110.8,8.18071], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH2CH
[CH2][CH]_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 71.55 kcal/mol
deltaH(298) 70.55 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    label = "C3H5_35",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 C u1 p0 c0 {1,S} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {7,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.79753,0.0147107,2.49158e-05,-4.60511e-08,2.05097e-11,18622.8,15.5553], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.85848,0.0192035,-9.08921e-06,2.10256e-09,-1.92622e-13,17752.5,2.95287], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH2CHCH2
[CH2]C=C_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 42.49 kcal/mol
deltaH(298) 39.65 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "C3H5O4_153",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {6,S}
2  O u0 p2 c0 {1,S} {7,S}
3  O u0 p2 c0 {4,S} {5,S}
4  O u1 p2 c0 {3,S}
5  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
6  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
7  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.695,0.0102069,8.16069e-05,-1.21447e-07,5.09922e-11,-7702.33,10.357], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.03336,0.0302547,-1.58164e-05,3.97092e-09,-3.88357e-13,-9668.49,-13.0005], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""cyc-CH2OOCH2CH(OO)
[O]OC1COOC1_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -5.37 kcal/mol
deltaH(298) -10.62 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "C4H7O_172",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {12,S}
4  C u0 p0 c0 {2,S} {3,D} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u1 p2 c0 {4,S}
12 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.42277,0.00606685,6.55059e-05,-8.83019e-08,3.51528e-11,-11046.5,5.29735], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.83242,0.0303847,-1.42961e-05,3.20223e-09,-2.76841e-13,-11804.5,3.31458], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3CHC(O)CH3;CCCO trans
C/C=C(/[O])\C_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -12.74 kcal/mol
deltaH(298) -17.37 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "C2H3O_40",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.52521,3.54321e-05,3.20893e-05,-4.03835e-08,1.56467e-11,-3231.47,5.44714], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.15923,0.0142521,-7.01695e-06,1.67625e-09,-1.57614e-13,-3292.51,10.1506], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CCHO
C[C]=O_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -1.82 kcal/mol
deltaH(298) -3.32 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    label = "C2H3O_41",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {3,S} {6,S}
3 O u0 p2 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.5318,-0.00552307,6.21826e-05,-8.09682e-08,3.27755e-11,18158.9,10.4611], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.39439,0.0140433,-6.95111e-06,1.66979e-09,-1.57831e-13,17484.9,7.09806], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""cyc-OCHCH2
O1[CH]C1_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 40.50 kcal/mol
deltaH(298) 38.49 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "C4H7O_85",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {4,S} {12,S}
4  C u0 p0 c0 {2,S} {3,S} {11,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {4,D}
12 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.13049,0.00644629,6.66501e-05,-9.10385e-08,3.66733e-11,-11760.2,6.89189], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.67934,0.0310347,-1.50708e-05,3.54629e-09,-3.27764e-13,-12609,4.00242], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3CHC(O)CH3;CCCO cis
C[CH]C(=O)C_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -14.24 kcal/mol
deltaH(298) -18.91 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    label = "C4H7O_87",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {3,D} {4,S} {9,S}
3  C u0 p0 c0 {2,D} {5,S} {10,S}
4  C u1 p0 c0 {2,S} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.80659,0.0105409,6.90184e-05,-1.03825e-07,4.39313e-11,-1307.27,6.98911], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.0661,0.0281986,-1.37826e-05,3.30518e-09,-3.14743e-13,-2728.56,-9.52469], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH2CHCHOCH3;CCCO
CO/C=C\[CH2]_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 6.58 kcal/mol
deltaH(298) 2.03 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "C4H7O_83",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {5,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  C u1 p0 c0 {3,S} {10,S} {11,S}
5  O u0 p2 c0 {2,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.73311,0.035861,-4.12294e-06,-2.26624e-08,1.27017e-11,-9352.38,13.3204], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.89483,0.0265777,-1.26365e-05,2.94764e-09,-2.73285e-13,-10842.2,-14.0885], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH2CHC(OH)CH3;
[CH2]/C=C(\O)/C_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -9.47 kcal/mol
deltaH(298) -13.95 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    label = "C4H5O3_139",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {3,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,D}
4  C u1 p0 c0 {1,S} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {2,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.66277,0.0368891,7.93323e-06,-4.30851e-08,2.18284e-11,-5714.95,16.9515], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.57549,0.0276187,-1.41195e-05,3.49303e-09,-3.3926e-13,-7852.53,-20.4872], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""cyc-CH(CH2)OOCH2C(O)-
O=C1COO[C@@H]1[CH2]_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -2.32 kcal/mol
deltaH(298) -6.53 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 46,
    label = "C4H5O3_138",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,D}
3  C u0 p0 c0 {2,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {10,S} {11,S}
5  O u0 p2 c0 {1,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {2,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.26449,0.029056,1.6273e-05,-4.64915e-08,2.18698e-11,-6525.77,7.43565], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.474,0.0236938,-1.17319e-05,2.79687e-09,-2.61056e-13,-8615.18,-26.9904], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH2CHC(O)CH2OO
[O]OCC(=O)C=C_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -3.65 kcal/mol
deltaH(298) -7.16 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
    label = "CH2_5",
    molecule = 
"""
multiplicity 3
1 C u2 p0 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97697,-0.000956038,7.34715e-06,-8.61374e-09,3.47431e-12,45500.4,0.832823], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.08735,0.00285254,-7.74608e-07,5.91402e-11,4.23083e-15,45718.8,5.20699], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""3CH2
[CH2]_m3 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 92.68 kcal/mol
deltaH(298) 92.79 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    label = "CH2_6",
    molecule = 
"""
1 C u0 p1 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.20198,-0.00230145,7.65456e-06,-6.0577e-09,1.73774e-12,49959.3,-0.823077], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.30511,0.00441109,-1.81047e-06,3.56904e-10,-2.74843e-14,50404.3,8.60317], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""1CH2
[CH2]_m1 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 101.58 kcal/mol
deltaH(298) 101.68 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    label = "C2O3_89",
    molecule = 
"""
multiplicity 3
1 O u0 p1 c+1 {4,D} {5,S}
2 O u1 p2 c0 {4,S}
3 O u1 p1 c+1 {5,D}
4 C u0 p1 c-1 {1,D} {2,S}
5 C u0 p1 c-1 {1,S} {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.43844,0.00345209,3.9371e-05,-6.10599e-08,2.55164e-11,-13954.6,2.66882], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.1467,0.00219424,-2.39862e-06,8.86568e-10,-1.10868e-13,-16471.9,-35.7695], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""OCOCO
[O][C]O[C][O]_m3 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -23.87 kcal/mol
deltaH(298) -23.73 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 50,
    label = "C2O3_88",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {5,S}
2 O u0 p2 c0 {4,D}
3 O u0 p2 c0 {5,D}
4 C u0 p0 c0 {1,S} {2,D} {5,S}
5 C u0 p0 c0 {1,S} {3,D} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.70888,0.0308022,-4.50361e-05,3.52331e-08,-1.11697e-11,-35289.8,16.2108], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.77724,0.00841499,-4.80779e-06,1.28577e-09,-1.31854e-13,-36294.7,-7.97087], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""cyc-C(O)OC(O)
O=C1OC1=O_m1 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -66.72 kcal/mol
deltaH(298) -67.06 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
    label = "C3H7O4_156",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {6,S}
2  O u0 p2 c0 {4,S} {7,S}
3  O u0 p2 c0 {1,S} {14,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {6,S} {7,S} {8,S} {9,S}
6  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
7  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.89494,0.0598971,-3.30087e-05,-1.4175e-08,1.47226e-11,-17647.7,15.9684], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[16.0717,0.0229191,-1.10057e-05,2.5862e-09,-2.40369e-13,-20867.5,-50.9231], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""OHOCH2CH2CH2OO
OOCCCO[O]_m2   torsopt/m062x/cc-pvtz/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -23.35 kcal/mol
deltaH(298) -28.69 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
    label = "C4H8O3_152",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,D} {14,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.86136,0.0854035,-8.58908e-05,3.58877e-08,-2.63525e-12,-39166.3,30.063], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.9022,0.0272365,-1.29876e-05,3.03347e-09,-2.80814e-13,-42404.8,-46.7496], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3CH(OOH)CH2CHO
C[C@@H](OO)CC=O_m1 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -66.33 kcal/mol
deltaH(298) -72.17 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 53,
    label = "CH2O2_50",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {5,S}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,S} {2,D} {4,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.57255,-0.00113789,3.72065e-05,-4.72874e-08,1.82605e-11,-47119.9,8.62556], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.91344,0.0138155,-8.05326e-06,2.15888e-09,-2.20369e-13,-47516.3,8.99307], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""OHCHO
OC=O_m1 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -89.40 kcal/mol
deltaH(298) -91.14 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 54,
    label = "C4H8O3_151",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {3,S} {14,D}
5  O u0 p2 c0 {2,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.86894,0.0540544,-2.84967e-06,-5.37133e-08,3.15434e-11,-41591.1,15.1624], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[15.2517,0.0264949,-1.24395e-05,2.85667e-09,-2.59907e-13,-44779.3,-48.9261], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3C(O)CH2CH2OOH
OOCCC(=O)C_m1 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -70.71 kcal/mol
deltaH(298) -76.41 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 55,
    label = "CO_17",
    molecule = 
"""
1 O u0 p1 c+1 {2,T}
2 C u0 p1 c-1 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.57393,-0.000567261,8.82461e-07,1.01596e-09,-9.34359e-13,-14862.9,3.51577], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.63188,0.00224921,-1.17521e-06,2.93376e-10,-2.85153e-14,-14643.7,8.25003], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CO
[C]=O_m1 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -28.24 kcal/mol
deltaH(298) -27.45 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 56,
    label = "C3H3O_55",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,D}
2 C u0 p0 c0 {3,S} {4,D} {5,S}
3 C u1 p0 c0 {2,S} {6,S} {7,S}
4 C u0 p0 c0 {1,D} {2,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.00769,0.0279804,-2.39851e-05,9.81432e-09,-1.09265e-12,9693.61,15.4934], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.8657,0.0143482,-6.99527e-06,1.66183e-09,-1.55832e-13,8839.17,-3.53622], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH2CHCO
[CH2]C=C=O_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 23.90 kcal/mol
deltaH(298) 22.54 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 57,
    label = "C4H9O3_155",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {15,S}
6  O u0 p2 c0 {1,S} {16,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u1 p2 c0 {5,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.55591,0.0392346,1.39964e-05,-4.99823e-08,2.42087e-11,-36186,8.10675], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.1291,0.0331809,-1.5472e-05,3.48317e-09,-3.07845e-13,-38372.6,-28.2038], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3CH2C(OH)(OO)CH3
C[C@@](O[O])(CC)O_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -58.60 kcal/mol
deltaH(298) -65.08 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 58,
    label = "C4H9O3_154",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {8,S}
3  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {15,S}
6  O u0 p2 c0 {2,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u1 p2 c0 {5,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.44372,0.017594,8.55054e-05,-1.34852e-07,5.7794e-11,-33689.2,-1.79276], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.8327,0.0315378,-1.51179e-05,3.5681e-09,-3.35649e-13,-36488.1,-41.1661], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3CH(OH)CH(OO)CH3
[O]O[C@@H]([C@@H](O)C)C_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -53.21 kcal/mol
deltaH(298) -59.96 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 59,
    label = "C2H3O3_98",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {5,D}
3 O u1 p2 c0 {1,S}
4 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5 C u0 p0 c0 {2,D} {4,S} {8,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.09341,0.0206471,1.36339e-06,-1.87176e-08,9.615e-12,-12269.9,10.1021], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.0803,0.0144362,-6.94918e-06,1.56819e-09,-1.34142e-13,-13502.1,-11.3958], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""OCHCH2OO
[O]OCC=O_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -17.74 kcal/mol
deltaH(298) -20.17 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 60,
    label = "C2H2O4_134",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {5,S}
2 O u0 p2 c0 {1,S} {8,S}
3 O u0 p2 c0 {5,D}
4 O u0 p2 c0 {6,D}
5 C u0 p0 c0 {1,S} {3,D} {6,S}
6 C u0 p0 c0 {4,D} {5,S} {7,S}
7 H u0 p0 c0 {6,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.10083,0.0492143,-7.05686e-05,5.40123e-08,-1.63767e-11,-47457.1,16.3968], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.90568,0.0208624,-1.23717e-05,3.32471e-09,-3.38917e-13,-48020.6,-4.65402], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""OCHC(O)OOH
OOC(=O)C=O_m1 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -87.85 kcal/mol
deltaH(298) -89.76 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 61,
    label = "C2HO2_62",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {3,S}
2 O u0 p2 c0 {4,D}
3 C u0 p0 c0 {1,S} {4,D} {5,S}
4 C u0 p0 c0 {2,D} {3,D}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.01623,0.00964722,2.86883e-06,-1.07419e-08,5.0173e-12,-9828.99,7.99827], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.15321,0.00958612,-5.09918e-06,1.29538e-09,-1.27902e-13,-10259.7,1.46321], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""OCHCO
[O]C=C=O_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -15.91 kcal/mol
deltaH(298) -16.29 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 62,
    label = "C3H5O2_93",
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
            NASAPolynomial(coeffs=[4.26745,0.00218912,8.16989e-05,-1.13959e-07,4.69975e-11,9620.97,8.44107], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.60885,0.025796,-1.31231e-05,3.22264e-09,-3.10032e-13,8249.66,-4.2544], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""cyc-CHCH2OOCH2
[CH]1COOC1_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 26.95 kcal/mol
deltaH(298) 22.87 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 63,
    label = "C2H2_14",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u2 p0 c0 {1,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89022,-0.00242447,2.33506e-05,-2.80498e-08,1.08146e-11,71794.5,5.02162], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.68354,0.00785777,-3.7524e-06,8.72337e-10,-8.01061e-14,71842.8,9.70929], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""3CH2C
C=[C]_m3 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 145.15 kcal/mol
deltaH(298) 145.07 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 64,
    label = "C2H2_15",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {3,S}
2 C u0 p0 c0 {1,T} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.950563,0.0213444,-2.93461e-05,2.05072e-08,-5.58379e-12,26323.5,14.1334], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.59652,0.00528706,-2.56179e-06,6.07534e-10,-5.70199e-14,25647.7,-3.13524], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CHCH
C#C_m1 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 54.48 kcal/mol
deltaH(298) 54.32 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 65,
    label = "CHO2_47",
    molecule = 
"""
multiplicity 2
1 O u0 p1 c+1 {3,D} {4,S}
2 O u1 p2 c0 {3,S}
3 C u0 p1 c-1 {1,D} {2,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.90327,0.0132112,-1.46141e-05,1.0093e-08,-3.19932e-12,-23840.5,10.751], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.73829,0.00645528,-3.68047e-06,9.81186e-10,-1.00304e-13,-24284,1.62666], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""HOCO
O[C][O]_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -44.15 kcal/mol
deltaH(298) -44.71 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 66,
    label = "C3H5O5_162",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {7,S}
2  O u0 p2 c0 {1,S} {8,S}
3  O u0 p2 c0 {5,S} {6,S}
4  O u0 p2 c0 {8,D}
5  O u1 p2 c0 {3,S}
6  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
7  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
8  C u0 p0 c0 {2,S} {4,D} {6,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.21582,0.0220389,2.43302e-05,-4.71611e-08,2.07559e-11,-31451.8,-3.46787], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.1344,0.0262671,-9.40215e-06,1.20377e-09,-2.3274e-14,-32175.7,-15.0098], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3OOC(O)CH2OO
[O]OCC(=O)OOC_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -50.99 kcal/mol
deltaH(298) -55.43 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 67,
    label = "C3H3O3_112",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {4,D} {7,S}
3 O u0 p2 c0 {1,S} {8,S}
4 C u0 p0 c0 {2,D} {9,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 O u1 p2 c0 {3,S}
9 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.81552,0.00860192,3.90423e-05,-6.09602e-08,2.59272e-11,-2904.5,0.0363161], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.86856,0.0175317,-8.981e-06,2.22328e-09,-2.15897e-13,-3981.95,-13.5891], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""OCCHCH2OO
[O]OCC=C=O_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 1.41 kcal/mol
deltaH(298) -0.50 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 68,
    label = "C3H3O3_110",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {5,S}
2 C u0 p0 c0 {1,S} {4,S} {6,D}
3 C u0 p0 c0 {1,D} {7,S} {8,S}
4 O u0 p2 c0 {2,S} {9,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 O u1 p2 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.35483,0.0143888,3.33778e-05,-5.86169e-08,2.54946e-11,-8324.69,5.58127], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.32494,0.0182466,-9.86045e-06,2.54322e-09,-2.55053e-13,-9951.01,-18.0312], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH2CHC(O)OO
[O]OC(=O)C=C_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -9.55 kcal/mol
deltaH(298) -11.72 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 69,
    label = "C3H3O3_111",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2 C u1 p0 c0 {1,S} {3,S} {8,S}
3 C u0 p0 c0 {2,S} {5,S} {9,D}
4 O u0 p2 c0 {1,S} {5,S}
5 O u0 p2 c0 {3,S} {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.05427,0.0241151,2.16564e-05,-5.23185e-08,2.4517e-11,-11267.5,18.9074], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.57518,0.0210206,-1.11052e-05,2.81068e-09,-2.76963e-13,-13144.1,-11.9322], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""cyc-C(O)OOCH2CH-
[CH]1COOC1=O_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -15.81 kcal/mol
deltaH(298) -18.85 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 70,
    label = "C2H3O2_73",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 O u0 p2 c0 {1,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 O u1 p2 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.27173,0.00646657,3.61225e-05,-5.59849e-08,2.38647e-11,11183.4,7.46915], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.49854,0.0135768,-6.85503e-06,1.68291e-09,-1.62541e-13,10115.8,-6.75029], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH2CHOO
[O]OC=C_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 27.86 kcal/mol
deltaH(298) 25.76 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 71,
    label = "HO2_27",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.39975,-0.0054609,2.21673e-05,-2.47638e-08,9.31129e-12,115.608,3.28805], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.47066,0.00333127,-1.42421e-06,3.01472e-10,-2.55814e-14,113.495,6.68863], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""OOH
O[O]_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 3.36 kcal/mol
deltaH(298) 2.65 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 72,
    label = "C2H3O2_75",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 C u0 p0 c0 {1,S} {5,D} {6,S}
3 O u0 p2 c0 {1,S} {7,S}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {2,D}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80762,0.0120408,1.63168e-05,-3.05455e-08,1.31059e-11,-23078.2,8.91074], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.77725,0.014975,-7.78682e-06,1.95114e-09,-1.91039e-13,-23945.2,-3.08541], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""OCHCHOH;trans
O[CH]C=O_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -40.24 kcal/mol
deltaH(298) -42.36 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 73,
    label = "C2HO4_122",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,D}
2 C u0 p0 c0 {1,S} {5,D} {6,S}
3 O u0 p2 c0 {1,S} {7,S}
4 O u0 p2 c0 {1,D}
5 O u0 p2 c0 {2,D}
6 H u0 p0 c0 {2,S}
7 O u1 p2 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.97213,0.0510892,-8.49221e-05,7.16457e-08,-2.36621e-11,-24187.4,17.2291], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.582,0.00965317,-5.38506e-06,1.41595e-09,-1.43231e-13,-25737.9,-23.0478], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""OCHC(O)OO
[O]OC(=O)C=O_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -42.56 kcal/mol
deltaH(298) -43.62 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 74,
    label = "C2H_13",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,T} {3,S}
2 C u1 p0 c0 {1,T}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.80485,0.0139305,-2.96911e-05,3.00453e-08,-1.11596e-11,66878.3,6.52537], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.30668,0.00280259,-1.53973e-06,4.00659e-10,-4.02915e-14,66743.9,0.305006], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CHC
C#[C]_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 134.41 kcal/mol
deltaH(298) 135.38 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 75,
    label = "C2HO4_120",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {5,D}
2 O u0 p2 c0 {1,S} {4,S}
3 C u1 p0 c0 {1,S} {6,D}
4 O u0 p2 c0 {2,S} {7,S}
5 O u0 p2 c0 {1,D}
6 O u0 p2 c0 {3,D}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.5776,0.0607385,-0.000116396,1.08833e-07,-3.83867e-11,-27954.9,18.1232], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.5905,0.0120865,-6.97807e-06,1.85566e-09,-1.88223e-13,-29009.8,-17.1754], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""OCC(O)OOH
OOC(=O)[C]=O_m2 ,  torsopt/m062x/cc-pvtz/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_tzmqz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -50.05 kcal/mol
deltaH(298) -50.91 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 76,
    label = "C3H3O2_81",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {4,T}
3 O u0 p2 c0 {1,S} {7,S}
4 C u0 p0 c0 {2,T} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u1 p2 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73928,0.0202947,4.69072e-06,-2.38149e-08,1.20526e-11,30578.5,11.7159], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.85642,0.0167846,-8.63699e-06,2.17536e-09,-2.17078e-13,29615.3,-5.2386], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CHCCH2OO
[O]OCC#C_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 66.46 kcal/mol
deltaH(298) 64.77 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 77,
    label = "C3H3O2_82",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,D} {4,S} {5,S}
2 C u0 p0 c0 {3,D} {6,S} {7,S}
3 C u0 p0 c0 {1,D} {2,D}
4 O u0 p2 c0 {1,S} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 O u1 p2 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49444,0.0246156,-2.66042e-06,-1.92224e-08,1.11162e-11,30194.2,11.0034], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.44271,0.0145009,-7.14948e-06,1.71047e-09,-1.61262e-13,28821.9,-14.9771], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH2CCHOO
[O]OC=C=C_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 65.83 kcal/mol
deltaH(298) 64.14 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 78,
    label = "C3H4O_58",
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
            NASAPolynomial(coeffs=[2.64096,0.0181327,1.17319e-05,-2.93385e-08,1.33827e-11,-9909.92,13.0255], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.91768,0.0193529,-9.94351e-06,2.46112e-09,-2.38276e-13,-10797.3,-0.278525], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH2CHCHO
C=CC=O_m1 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -14.03 kcal/mol
deltaH(298) -16.42 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 79,
    label = "C3H5O2_95",
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
            NASAPolynomial(coeffs=[3.0835,0.029404,-6.90088e-06,-1.25666e-08,7.64351e-12,-15951.6,14.3927], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.9822,0.0243941,-1.25161e-05,3.10562e-09,-3.02249e-13,-16802.5,-1.0509], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""OCH2CH2CHO
[O]CCC=O_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -24.07 kcal/mol
deltaH(298) -27.44 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 80,
    label = "C2H2O2_69",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 O u0 p2 c0 {4,D}
3 C u0 p0 c0 {1,D} {4,S} {5,S}
4 C u0 p0 c0 {2,D} {3,S} {6,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.88797,-0.000825386,4.26168e-05,-5.4509e-08,2.09061e-11,-27959.7,3.61715], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.0162,0.0123235,-6.89767e-06,1.81869e-09,-1.84239e-13,-29021.4,-6.07129], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""OCHCHO
O=CC=O_m1 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -50.83 kcal/mol
deltaH(298) -52.19 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 81,
    label = "C3H5O2_94",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,D} {7,S}
3  C u0 p0 c0 {2,D} {8,S} {9,S}
4  O u0 p2 c0 {1,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 O u1 p2 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.55023,-0.00159596,7.20893e-05,-9.50402e-08,3.8283e-11,8391.81,1.87285], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.87311,0.0236323,-1.18351e-05,2.89632e-09,-2.80226e-13,7658.12,0.279468], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH2CHCH2OO
[O]OCC=C_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 24.68 kcal/mol
deltaH(298) 21.34 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 82,
    label = "C3H4O2_90",
    molecule = 
"""
1 O u0 p2 c0 {4,D}
2 O u0 p2 c0 {5,D}
3 C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4 C u0 p0 c0 {1,D} {3,S} {8,S}
5 C u0 p0 c0 {2,D} {3,S} {9,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.44024,0.000380252,5.81331e-05,-7.55645e-08,2.97813e-11,-33167.7,7.26242], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.07322,0.0236589,-1.23707e-05,3.11586e-09,-3.06905e-13,-33591.2,9.974], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""OCHCH2CHO
O=CCC=O_m1 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -59.14 kcal/mol
deltaH(298) -61.90 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 83,
    label = "C2H3O4_136",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,D} {7,S}
3 O u0 p2 c0 {1,S} {9,S}
4 O u0 p2 c0 {1,S} {8,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
7 H u0 p0 c0 {2,S}
8 O u1 p2 c0 {4,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.47048,0.0408259,-2.21093e-05,-1.30179e-08,1.20645e-11,-34750,17.1569], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.1676,0.0116675,-5.91274e-06,1.45027e-09,-1.38937e-13,-37443.1,-37.4482], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""OCHCH(OH)OO
O[C@@H](C=O)O[O]_m2 ,  torsopt/m062x/cc-pvtz/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_tzmqz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -61.57 kcal/mol
deltaH(298) -64.41 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 84,
    label = "H2O_12",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.20684,-0.00213778,6.58301e-06,-5.54453e-09,1.76478e-12,-30291,-0.898855], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.20912,0.0017402,8.77983e-08,-1.96083e-10,3.1284e-14,-30057.6,4.01333], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""H2O
O_m1 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -57.11 kcal/mol
deltaH(298) -57.80 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 85,
    label = "C3H3_29",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.3672,0.0294685,-3.81005e-05,2.74084e-08,-7.92464e-12,40673.6,15.385], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.33498,0.0107899,-4.90376e-06,1.09518e-09,-9.73877e-14,39992.4,-3.12906], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH2CCH
[CH2]C#C_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 84.33 kcal/mol
deltaH(298) 83.67 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 86,
    label = "C2HO_34",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {4,S}
4 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.05638,0.0203688,-3.28683e-05,2.81574e-08,-9.40968e-12,19815.6,13.0066], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.78559,0.00571088,-2.79702e-06,6.68163e-10,-6.30167e-14,19394.5,0.602647], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""HCCO
[O]C#C_m2      torsopt/b2plypd3/cc-pvtz/gaussian,torsscan/b2plypd3/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 41.71 kcal/mol
deltaH(298) 41.92 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 87,
    label = "C4H6O_80",
    molecule = 
"""
1  O u0 p2 c0 {3,D}
2  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,D} {2,S} {4,S}
4  C u0 p0 c0 {3,S} {5,D} {9,S}
5  C u0 p0 c0 {4,D} {10,S} {11,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.26268,0.00790197,5.61347e-05,-7.9011e-08,3.19841e-11,-16141.2,4.37877], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.47714,0.0274795,-1.3672e-05,3.30149e-09,-3.13768e-13,-16994.1,-1.13988], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3C(O)CHCH2
CC(=O)C=C_m1 ,  torsopt/wb97xd/cc-pvtz/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_tzmqz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -23.84 kcal/mol
deltaH(298) -27.55 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 88,
    label = "CH4_9",
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
            NASAPolynomial(coeffs=[5.17724,-0.0136285,4.77937e-05,-4.69975e-08,1.61098e-11,-10238.8,-4.81134], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.0305499,0.0131885,-5.96649e-06,1.31758e-09,-1.15369e-13,-9414.28,18.7551], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH4
C_m1 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -15.91 kcal/mol
deltaH(298) -17.81 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 89,
    label = "C4H7O3_145",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {3,S} {13,D}
5  O u0 p2 c0 {1,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.63665,0.0167563,5.29523e-05,-8.32297e-08,3.49799e-11,-25046.3,-2.26772], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.3208,0.0302197,-1.44801e-05,3.33495e-09,-2.99939e-13,-26569.9,-20.5914], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3C(O)CH(OO)CH3
C[C@@H](C(=O)C)O[O]_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -38.09 kcal/mol
deltaH(298) -43.13 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 90,
    label = "C4H7O3_148",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {13,S}
6  O u0 p2 c0 {1,S} {14,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 O u1 p2 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.18902,0.0491944,-3.58471e-05,1.12411e-08,-3.52071e-13,-21339.6,4.30377], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.3983,0.0294853,-1.46963e-05,3.58303e-09,-3.44943e-13,-22831.5,-26.9038], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH2CHC(OH)(OO)CH3
C[C@@](C=C)(O[O])O_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -30.76 kcal/mol
deltaH(298) -35.57 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 91,
    label = "C4H7O3_149",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {6,S} {12,D}
4  C u1 p0 c0 {3,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {3,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 O u0 p2 c0 {3,D}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.12001,0.0476725,-2.17295e-05,-7.76223e-09,7.53823e-12,-23155.4,10.7581], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.61296,0.0338616,-1.7593e-05,4.38382e-09,-4.2629e-13,-24565.3,-17.5007], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3CH2OOC(O)CH2
CCOOC(=O)[CH2]_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -34.79 kcal/mol
deltaH(298) -39.77 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 92,
    label = "CH3O_23",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.13404,-0.00610793,4.19368e-05,-4.93971e-08,1.89116e-11,924.511,4.86121], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.02403,0.01208,-5.89041e-06,1.39361e-09,-1.29861e-13,993.565,12.9925], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3O
C[O]_m2       torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 6.11 kcal/mol
deltaH(298) 4.31 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 93,
    label = "C4H7O3_146",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {4,D} {6,S}
4  C u0 p0 c0 {1,S} {3,D} {12,S}
5  O u0 p2 c0 {1,S} {13,S}
6  O u0 p2 c0 {3,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 O u1 p2 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.67533,0.00302398,0.000137536,-1.98194e-07,8.23412e-11,-20725.7,0.919492], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[17.2198,0.023544,-1.21391e-05,3.06118e-09,-3.0387e-13,-25423.5,-64.0258], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3C(OH)CHCH2OO;CCCO cis
[O]OC/C=C(\O)/C_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -29.67 kcal/mol
deltaH(298) -35.25 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 94,
    label = "CH3O_24",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.90272,0.0102798,3.1623e-07,-9.41404e-09,5.216e-12,-3541.01,9.50626], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.50239,0.00716075,-2.90597e-06,5.93816e-10,-5.02499e-14,-3955.79,1.16688], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH2OH
[CH2]O_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -2.87 kcal/mol
deltaH(298) -4.44 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 95,
    label = "C5H7O2_137",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {4,S}
2  O u0 p2 c0 {5,D}
3  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
4  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
5  C u0 p0 c0 {2,D} {3,S} {6,S}
6  C u0 p0 c0 {5,S} {7,D} {12,S}
7  C u0 p0 c0 {6,D} {13,S} {14,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.67291,0.0262722,3.48545e-05,-6.52614e-08,2.81209e-11,-10653.8,5.87312], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.92858,0.0345723,-1.78861e-05,4.48731e-09,-4.43033e-13,-12203.8,-14.6547], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH2CHC(O)CH2CH2O
[O]CCC(=O)C=C_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -10.68 kcal/mol
deltaH(298) -15.11 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 96,
    label = "C3H3O4_143",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u1 p0 c0 {1,S} {5,S} {8,S}
3  C u0 p0 c0 {4,S} {5,S} {9,D}
4  O u0 p2 c0 {1,S} {3,S}
5  O u0 p2 c0 {2,S} {3,S}
6  O u0 p2 c0 {1,S} {10,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.61434,0.0402628,-1.0974e-05,-2.32469e-08,1.48101e-11,-64451.8,20.2399], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.6914,0.0197423,-1.03174e-05,2.60818e-09,-2.58121e-13,-66937.6,-27.1212], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""cyc-CHOC(O)OCH(OH)-
O[C@H]1[CH]OC(=O)O1_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -120.40 kcal/mol
deltaH(298) -123.84 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 97,
    label = "C3H3O4_144",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {7,D} {8,S}
3  O u0 p1 c+1 {1,S} {5,D}
4  O u0 p2 c0 {1,S} {9,S}
5  C u0 p1 c-1 {3,D} {10,S}
6  H u0 p0 c0 {1,S}
7  O u0 p2 c0 {2,D}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.58606,0.0515691,-5.4341e-05,2.99928e-08,-6.87566e-12,-56022.9,18.3509], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.7067,0.0201944,-1.18752e-05,3.24402e-09,-3.38492e-13,-58231.7,-27.2281], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""OCHCH(OH)OCO
O[C@H](C=O)O[C][O]_m2 ,  torsopt/m062x/cc-pvtz/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_tzmqz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -103.65 kcal/mol
deltaH(298) -106.09 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 98,
    label = "C3H5O3_125",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {5,S} {9,D}
3  C u1 p0 c0 {2,S} {10,S} {11,S}
4  O u0 p2 c0 {1,S} {5,S}
5  O u0 p2 c0 {2,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u0 p2 c0 {2,D}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.76962,0.0478451,-4.51971e-05,2.3306e-08,-4.96309e-12,-18344.1,14.5792], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.14413,0.0244771,-1.27127e-05,3.15841e-09,-3.06351e-13,-19757.2,-16.7768], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3OOC(O)CH2
COOC(=O)[CH2]_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -27.58 kcal/mol
deltaH(298) -31.29 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 99,
    label = "C3H5O3_127",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,D} {7,S}
3  C u0 p0 c0 {2,D} {8,S} {9,S}
4  O u0 p2 c0 {1,S} {11,S}
5  O u0 p2 c0 {1,S} {10,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 O u1 p2 c0 {5,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.18934,0.0261819,8.88676e-06,-3.28898e-08,1.5821e-11,-14551.2,6.93806], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.73304,0.021872,-1.07141e-05,2.53194e-09,-2.33731e-13,-16050.9,-18.132], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH2CHCH(OH)OO
O[C@@H](C=C)O[O]_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -19.77 kcal/mol
deltaH(298) -23.49 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 100,
    label = "C3H5O3_126",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,D}
4  O u0 p2 c0 {1,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 O u1 p2 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.06544,0.0180918,2.6888e-05,-4.97486e-08,2.16678e-11,-19548.9,3.04668], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.07616,0.0222808,-1.05635e-05,2.37666e-09,-2.05631e-13,-20826.9,-15.1207], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3C(O)CH2OO
CC(=O)CO[O]_m2 ,  torsopt/b2plypd3/cc-pvtz/gaussian,torsscan/b2plypd3/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_tzmqz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -29.69 kcal/mol
deltaH(298) -33.36 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 101,
    label = "C3H5O3_129",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {5,S} {9,S}
4  O u0 p2 c0 {1,S} {10,S}
5  O u0 p2 c0 {3,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 O u1 p2 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.54569,-0.00320037,0.000144558,-2.11465e-07,8.98521e-11,-14370.1,5.30827], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[18.2465,0.0109073,-4.81371e-06,1.03905e-09,-8.81461e-14,-19472,-70.1973], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""OHCHCHCH2OO;CCCO cis
[O]OC/C=C\O_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -19.52 kcal/mol
deltaH(298) -23.76 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 102,
    label = "C4H7O4_161",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {5,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {6,S} {15,D}
5  O u0 p2 c0 {3,S} {6,S}
6  O u0 p2 c0 {4,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u1 p2 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.54666,0.0400347,-1.87391e-06,-2.61111e-08,1.35904e-11,-36651.5,2.52889], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.96184,0.0374535,-1.96743e-05,4.92727e-09,-4.81642e-13,-37787.9,-16.4091], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""OCH2CH2C(O)OOCH3
COOC(=O)CC[O]_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -60.32 kcal/mol
deltaH(298) -65.54 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 103,
    label = "C4H7O4_160",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {2,S} {6,S}
6  O u0 p2 c0 {3,S} {5,S}
7  O u0 p2 c0 {1,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u1 p2 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.77792,0.0140953,9.14429e-05,-1.36135e-07,5.68939e-11,-13038.5,7.62147], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.17446,0.0380591,-1.95462e-05,4.86311e-09,-4.75734e-13,-15196.3,-16.9673], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""cyc-CH2OOCH(CH3)CH(OO)-
[O]O[C@H]1COO[C@@H]1C_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -13.54 kcal/mol
deltaH(298) -20.12 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 104,
    label = "C3H7O2_100",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  O u0 p2 c0 {2,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u1 p2 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.42438,-0.0042892,9.14246e-05,-1.1758e-07,4.68455e-11,-8002.46,-1.7384], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.5485,0.0296543,-1.45103e-05,3.45908e-09,-3.26376e-13,-8612.11,1.69027], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3CH2CH2OO
CCCO[O]_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -5.78 kcal/mol
deltaH(298) -10.70 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 105,
    label = "C3H7O2_101",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {10,S} {11,S}
4  O u0 p2 c0 {2,S} {5,S}
5  O u0 p2 c0 {4,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.5957,0.013679,3.57987e-05,-5.72389e-08,2.42166e-11,-251.598,-4.38974], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.47845,0.0248453,-1.17407e-05,2.71834e-09,-2.50337e-13,-966.971,-11.7532], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH2CH2CH2OOH
[CH2]CCOO_m2 ,  torsopt/wb97xd/cc-pvtz/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_tzmqz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 9.85 kcal/mol
deltaH(298) 5.64 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 106,
    label = "C3H7O2_102",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {2,S} {11,S}
4  O u0 p2 c0 {1,S} {5,S}
5  O u0 p2 c0 {4,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.91298,-0.00454103,8.37289e-05,-1.06532e-07,4.21519e-11,-1350.35,-7.00094], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.35655,0.0261057,-1.23208e-05,2.83809e-09,-2.59052e-13,-1961.12,-4.72544], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3CHCH2OOH
C[CH]COO_m2 ,  torsopt/wb97xd/cc-pvtz/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_tzmqz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 7.62 kcal/mol
deltaH(298) 3.29 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 107,
    label = "C4H8O_91",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.68393,-0.002637,0.000112182,-1.46799e-07,5.86911e-11,-17656.3,8.52824], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.47864,0.0370269,-1.83908e-05,4.42513e-09,-4.18512e-13,-18742.7,6.84619], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""cyc-CH(CH3)CH2CH2O
C[C@H]1CCO1_m1 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -24.96 kcal/mol
deltaH(298) -31.10 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 108,
    label = "C4H8O_92",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {3,S} {13,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.56625,0.00051097,7.09873e-05,-8.6316e-08,3.24875e-11,-31938.2,-4.66312], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.09857,0.0339514,-1.62302e-05,3.75895e-09,-3.42727e-13,-32070.9,7.64163], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3CH2C(O)CH3
CCC(=O)C_m1 ,  torsopt/b2plypd3/cc-pvtz/gaussian,torsscan/b2plypd3/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_tzmqz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -52.83 kcal/mol
deltaH(298) -58.00 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 109,
    label = "C5H7O3_158",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {4,S} {6,S}
2  O u0 p2 c0 {4,S} {15,S}
3  O u0 p2 c0 {7,D}
4  C u0 p0 c0 {1,S} {2,S} {7,S} {9,S}
5  C u0 p0 c0 {6,D} {8,S} {10,S}
6  C u0 p0 c0 {1,S} {5,D} {11,S}
7  C u0 p0 c0 {3,D} {4,S} {12,S}
8  C u1 p0 c0 {5,S} {13,S} {14,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83746,0.042722,3.84883e-05,-1.00963e-07,4.91678e-11,-37390.7,13.9005], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[16.9701,0.0267579,-1.34932e-05,3.34825e-09,-3.30375e-13,-41392.3,-57.2576], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH2CHCHOCH(OH)CHO;CCCO cis
[CH2]/C=C\O[C@@H](C=O)O_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -62.99 kcal/mol
deltaH(298) -67.93 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 110,
    label = "C3H2O3_106",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {4,S} {6,S}
2 C u0 p0 c0 {1,D} {5,S} {7,S}
3 C u0 p0 c0 {4,S} {5,S} {8,D}
4 O u0 p2 c0 {1,S} {3,S}
5 O u0 p2 c0 {2,S} {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.843977,0.0240974,1.92467e-05,-5.05849e-08,2.42112e-11,-49995,21.6135], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.13061,0.0181456,-9.69233e-06,2.47642e-09,-2.45946e-13,-52033.3,-12.9645], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""cyc-C(O)OCHCHO-
O=c1occo1_m1 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -93.95 kcal/mol
deltaH(298) -96.56 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 111,
    label = "C3H2O3_107",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,D} {6,S}
2 C u0 p0 c0 {1,S} {5,S} {7,D}
3 C u0 p0 c0 {1,D} {4,S} {8,S}
4 O u0 p2 c0 {3,S} {5,S}
5 O u0 p2 c0 {2,S} {4,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {2,D}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.687148,0.0281395,7.84077e-06,-3.83594e-08,1.96274e-11,-23798.5,22.7303], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.50031,0.0177407,-9.49244e-06,2.42824e-09,-2.41368e-13,-25857.7,-13.8966], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""cyc-C(O)OOCHCH-
O=c1ccoo1_m1 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -41.88 kcal/mol
deltaH(298) -44.39 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 112,
    label = "H_1",
    molecule = 
"""
multiplicity 2
1 H u1 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.49915,1.99587e-06,1.70484e-09,-7.66268e-12,4.56937e-15,25389.7,-1.15046], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.49784,4.16161e-06,-3.12902e-09,1.00364e-12,-1.17796e-16,25390.3,-1.14287], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""[H]_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]""",
    longDesc = 
u"""

""",
)

entry(
    index = 113,
    label = "CO2_44",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,D} {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.32732,0.00916198,-6.78826e-06,2.18473e-10,1.17611e-12,-48737.7,10.0097], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.5438,0.00281212,-1.67132e-06,4.58981e-10,-4.79515e-14,-49300.2,-1.28399], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""OCO
O=C=O_m1 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -94.70 kcal/mol
deltaH(298) -94.78 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 114,
    label = "O2_25",
    molecule = 
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77606,-0.00300055,1.00127e-05,-1.00144e-08,3.40261e-12,-1203.46,3.67976], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.08649,0.00193281,-1.10967e-06,2.97266e-10,-3.04873e-14,-1164.42,6.49203], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""3O2
[O][O]_m3 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -0.28 kcal/mol
deltaH(298) -0.28 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 115,
    label = "CHO_19",
    molecule = 
"""
multiplicity 2
1 O u1 p1 c+1 {2,D}
2 C u0 p1 c-1 {1,D} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.23234,-0.00328038,1.34789e-05,-1.30351e-08,4.29711e-12,3392.7,3.3353], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.5326,0.00526533,-2.70934e-06,6.68689e-10,-6.44301e-14,3662.01,11.1475], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CHO
[CH][O]_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 9.06 kcal/mol
deltaH(298) 9.15 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 116,
    label = "H3N_11",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.41884,-0.00550541,2.16206e-05,-2.15213e-08,7.53235e-12,-6709.33,-1.20266], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.02563,0.00633868,-2.11813e-06,3.13984e-10,-1.50711e-14,-6274.59,9.96274], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""NH3
N_m1 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -9.22 kcal/mol
deltaH(298) -10.90 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 117,
    label = "CH2O_21",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.81463,-0.00986529,3.61664e-05,-3.6267e-08,1.24905e-11,-14721.8,0.471094], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.36845,0.00980407,-4.90685e-06,1.18599e-09,-1.12466e-13,-14261.9,15.8101], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH2O
C=O_m1 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -25.85 kcal/mol
deltaH(298) -26.77 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 118,
    label = "C4H5O5_169",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {7,S}
2  O u0 p2 c0 {1,S} {8,S}
3  O u0 p2 c0 {5,S} {6,S}
4  O u0 p2 c0 {9,D}
5  O u1 p2 c0 {3,S}
6  C u0 p0 c0 {3,S} {7,S} {9,S} {10,S}
7  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
8  C u0 p0 c0 {2,S} {9,S} {13,S} {14,S}
9  C u0 p0 c0 {4,D} {6,S} {8,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.3613,0.0198,7.1728e-05,-1.14383e-07,4.85574e-11,-21071.1,9.54983], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.80156,0.0359999,-1.91247e-05,4.86935e-09,-4.82798e-13,-23332.2,-19.3868], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""cyc-CH2OOCH2C(O)CHOO-
[O]O[C@H]1COOCC1=O_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -30.63 kcal/mol
deltaH(298) -36.09 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 119,
    label = "C2H2O_36",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.19982,0.017427,-1.60461e-05,8.04739e-09,-1.53979e-12,-7381.79,11.9549], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.26567,0.00934114,-4.46399e-06,1.04176e-09,-9.61961e-14,-7802.7,1.95373], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH2CO
C=C=O_m1 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -11.32 kcal/mol
deltaH(298) -12.08 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 120,
    label = "C3H2O3_108",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {4,S} {6,D}
3 C u0 p0 c0 {1,S} {7,D} {8,S}
4 O u0 p2 c0 {1,S} {2,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
7 O u0 p2 c0 {3,D}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.35917,0.0326318,-1.79947e-05,-4.45154e-09,5.51266e-12,-35393.3,16.2681], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.82601,0.0158448,-8.63024e-06,2.24323e-09,-2.26319e-13,-37114,-17.0952], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""cyc-CH(CHO)OC(O)-
O=C[C@H]1OC1=O_m1 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -64.61 kcal/mol
deltaH(298) -66.38 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 121,
    label = "C2HO4_121",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {4,S} {7,D}
3 O u0 p2 c0 {1,S} {4,S}
4 O u0 p2 c0 {2,S} {3,S}
5 O u1 p2 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.11396,0.0362364,-2.71245e-05,2.41857e-09,3.83418e-12,-18924.5,21.9485], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.91732,0.013199,-7.38941e-06,1.94981e-09,-1.98099e-13,-20863.9,-17.621], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""cyc-CH(O)OOC(O)-
O=C1OO[C@@H]1[O]_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -32.30 kcal/mol
deltaH(298) -34.21 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 122,
    label = "C3H6_37",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.12586,0.00065541,5.5129e-05,-7.0418e-08,2.75828e-11,533.885,6.40764], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.01278,0.024206,-1.16034e-05,2.70979e-09,-2.50011e-13,400.456,13.4023], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3CHCH2
CC=C_m1 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 7.89 kcal/mol
deltaH(298) 4.28 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 123,
    label = "C2H5O3_105",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  O u0 p2 c0 {1,S} {10,S}
4  O u0 p2 c0 {2,S} {9,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u1 p2 c0 {4,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.28063,0.0273089,4.92127e-06,-3.42055e-08,1.8446e-11,-23220.4,8.18925], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.4845,0.0158785,-6.96684e-06,1.47771e-09,-1.2253e-13,-24953.5,-24.5432], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""OHCH2CH2OO
OCCO[O]_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -37.41 kcal/mol
deltaH(298) -41.23 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 124,
    label = "CH3O2_51",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.56628,-0.010941,5.95222e-05,-6.8664e-08,2.60029e-11,-263.708,1.88208], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.91758,0.0139491,-6.86678e-06,1.64092e-09,-1.54373e-13,-275.153,11.5874], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3OO
CO[O]_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 4.98 kcal/mol
deltaH(298) 2.61 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 125,
    label = "C3H5O_66",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {8,S} {9,S}
4 O u1 p2 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.65161,0.00621075,4.70627e-05,-6.75484e-08,2.78812e-11,9404.75,6.51187], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.94683,0.0216656,-1.06634e-05,2.54868e-09,-2.39899e-13,8724.09,1.54535], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH2CHCH2O
[O]CC=C_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 25.57 kcal/mol
deltaH(298) 22.58 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 126,
    label = "C3H5O_65",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {5,S}
2 C u0 p0 c0 {1,D} {4,S} {6,S}
3 C u1 p0 c0 {1,S} {7,S} {8,S}
4 O u0 p2 c0 {2,S} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.74986,0.0301188,-7.30699e-06,-1.63433e-08,1.02615e-11,-3382.56,16.6743], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.17503,0.0179283,-8.36973e-06,1.92178e-09,-1.75481e-13,-4837.1,-11.5586], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH2CHCHOH;cis
[CH2]/C=C\O_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -0.06 kcal/mol
deltaH(298) -3.21 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 127,
    label = "C3H5O_63",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {7,D}
3 C u1 p0 c0 {2,S} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {2,D}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.66029,0.0185295,1.59776e-05,-3.48024e-08,1.56446e-11,-5908.91,14.6584], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.09065,0.0228426,-1.14576e-05,2.80459e-09,-2.70696e-13,-6569.44,5.62552], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3C(O)CH2
CC(=O)[CH2]_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -5.12 kcal/mol
deltaH(298) -8.37 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 128,
    label = "C2H3O2_171",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 O u0 p2 c0 {1,S} {7,S}
4 H u0 p0 c0 {1,S}
5 O u1 p2 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.31524,0.0156156,1.28713e-05,-2.87728e-08,1.305e-11,-26127.6,15.3422], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.23227,0.0219411,-1.16794e-05,2.85214e-09,-2.66674e-13,-26266.7,14.6527], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""OCHCHOH;cis
O/C=C\[O]_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -46.55 kcal/mol
deltaH(298) -49.04 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 129,
    label = "C2H3O_39",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {4,S} {5,S}
2 C u0 p1 c-1 {1,S} {3,D}
3 O u0 p1 c+1 {2,D} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.73045,0.0177313,-1.20754e-05,2.86682e-09,4.64769e-13,12133.9,12.1652], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.89033,0.0107364,-4.92325e-06,1.11543e-09,-1.00951e-13,11638.5,1.3894], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH2COH
[CH2][C]O_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 28.51 kcal/mol
deltaH(298) 27.10 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 130,
    label = "C2H3O_38",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.73135,0.00961834,1.53448e-05,-2.75984e-08,1.19759e-11,237.274,12.2485], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.71964,0.0135965,-6.69496e-06,1.60174e-09,-1.50932e-13,-268.183,5.76174], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH2CHO
[CH2]C=O_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 4.87 kcal/mol
deltaH(298) 3.11 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 131,
    label = "C3H7_43",
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
            NASAPolynomial(coeffs=[6.17178,-0.0119965,8.86231e-05,-1.03219e-07,3.90215e-11,8364.83,0.0450997], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.1127,0.028322,-1.38119e-05,3.28737e-09,-3.09844e-13,8649.18,20.2215], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3CHCH3
C[CH]C_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 24.60 kcal/mol
deltaH(298) 20.41 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 132,
    label = "C3H7_42",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u1 p0 c0 {1,S} {9,S} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.26509,0.00465336,5.11559e-05,-6.87554e-08,2.75332e-11,9981.48,7.48869], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.45767,0.0263795,-1.27087e-05,3.00746e-09,-2.83748e-13,9836.72,13.2134], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3CH2CH2
CC[CH2]_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 27.63 kcal/mol
deltaH(298) 23.43 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 133,
    label = "C4H9O2_130",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.20958,0.0111979,7.28663e-05,-1.03472e-07,4.22126e-11,-13382.4,-0.595049], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.04711,0.0372012,-1.81311e-05,4.29852e-09,-4.01813e-13,-14308.9,-5.24738], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3CH(OO)CH2CH3
C[C@@H](O[O])CC_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -14.03 kcal/mol
deltaH(298) -20.42 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 134,
    label = "C4H9O2_131",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {2,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.15683,0.0230527,4.26968e-05,-7.57447e-08,3.31438e-11,-5232.51,-0.730139], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.0628,0.0324612,-1.55117e-05,3.62985e-09,-3.36802e-13,-6587.44,-19.1962], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3CH(OOH)CH2CH2
C[C@@H](OO)C[CH2]_m2 ,  torsopt/wb97xd/cc-pvtz/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_tzmqz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 2.12 kcal/mol
deltaH(298) -3.64 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 135,
    label = "C4H9O2_132",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {3,S} {14,S}
5  O u0 p2 c0 {2,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.83955,0.0134354,5.47442e-05,-7.90792e-08,3.20088e-11,-4624.3,-6.67476], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.65426,0.0341752,-1.63342e-05,3.80347e-09,-3.5001e-13,-5365.03,-10.1333], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3CHCH2CH2OOH
C[CH]CCOO_m2 ,  torsopt/wb97xd/cc-pvtz/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_tzmqz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 3.57 kcal/mol
deltaH(298) -2.08 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 136,
    label = "C4H9O2_133",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {3,S} {15,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.57316,-0.00921392,0.000123978,-1.56017e-07,6.15723e-11,-11191,-8.61668], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.74809,0.0374358,-1.82009e-05,4.31514e-09,-4.04943e-13,-11985.3,-2.61154], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3CH2CH2CH2OO
CCCCO[O]_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -9.65 kcal/mol
deltaH(298) -15.76 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 137,
    label = "C2H5_20",
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
            NASAPolynomial(coeffs=[4.38536,-0.00399643,4.75498e-05,-5.71648e-08,2.19878e-11,12788.9,4.30501], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.70885,0.0175106,-8.13838e-06,1.84663e-09,-1.65994e-13,12952.6,14.9987], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3CH2
C[CH2]_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 30.92 kcal/mol
deltaH(298) 28.29 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 138,
    label = "C4H5O3_140",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,S} {11,D}
4  C u1 p0 c0 {3,S} {6,S} {12,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {4,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {3,D}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.15094,0.0387343,2.07042e-06,-3.52883e-08,1.84288e-11,-14724.5,18.6273], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.88285,0.0285877,-1.46353e-05,3.60872e-09,-3.47869e-13,-16783.5,-17.6472], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""cyc-CH(CH3)OOCHC(O)-
O=C1[CH]OO[C@H]1C_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -20.31 kcal/mol
deltaH(298) -24.65 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 139,
    label = "C4H5O3_141",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {4,S} {12,S}
4  C u0 p0 c0 {2,S} {3,S} {11,D}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {2,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {4,D}
12 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.67399,0.0313109,3.05807e-05,-6.84756e-08,3.12633e-11,-10233.5,20.5392], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.8172,0.0310847,-1.6215e-05,4.06384e-09,-3.97414e-13,-12467.8,-14.5373], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""cyc-CH2OOCH2CHC(O)-
O=C1[CH]COOC1_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -11.45 kcal/mol
deltaH(298) -16.28 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 140,
    label = "C4H5O3_142",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,S} {10,D}
4  C u0 p0 c0 {3,S} {11,D} {12,S}
5  O u1 p2 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 O u0 p2 c0 {4,D}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.06529,0.0268077,1.18666e-05,-4.11129e-08,2.05755e-11,-29754.3,-4.09265], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.7989,0.0216886,-1.05214e-05,2.46115e-09,-2.25186e-13,-31199.1,-29.8028], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3CH(O)C(O)CHO
C[C@@H](C(=O)C=O)[O]_m2 ,  torsopt/wb97xd/cc-pvtz/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_tzmqz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -49.46 kcal/mol
deltaH(298) -51.92 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 141,
    label = "CHO4_103",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {5,S}
2 O u0 p2 c0 {5,S} {6,S}
3 O u0 p2 c0 {5,D}
4 O u1 p2 c0 {1,S}
5 C u0 p0 c0 {1,S} {2,S} {3,D}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.66664,0.0269612,-6.65547e-06,-1.81886e-08,1.10463e-11,-42938.2,18.6588], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.06591,0.0113478,-7.52027e-06,2.16847e-09,-2.31775e-13,-45076.1,-20.3739], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""OHC(O)OO
[O]OC(=O)O_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -80.22 kcal/mol
deltaH(298) -82.14 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 142,
    label = "C2H5O2_77",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.88556,-0.00223132,6.08994e-05,-7.72468e-08,3.03375e-11,-4983.21,2.40672], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.35534,0.0214867,-1.04277e-05,2.45848e-09,-2.28495e-13,-5349.42,5.99573], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3CH2OO
CCO[O]_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -2.06 kcal/mol
deltaH(298) -5.82 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 143,
    label = "C2H4_18",
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
            NASAPolynomial(coeffs=[4.20788,-0.00957557,6.06232e-05,-7.20532e-08,2.79003e-11,4894.89,3.07603], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.66753,0.0149648,-6.97447e-06,1.58805e-09,-1.43279e-13,4896.02,12.3464], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH2CH2
C=C_m1 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 14.23 kcal/mol
deltaH(298) 12.18 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 144,
    label = "C4H7O2_113",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {4,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4  C u1 p0 c0 {1,S} {2,S} {13,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {2,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.24665,0.0158152,6.73064e-05,-1.04028e-07,4.39623e-11,4368.58,10.6803], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.85368,0.0336216,-1.68864e-05,4.10499e-09,-3.91793e-13,2760.07,-7.99442], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""cyc-C(CH3)OOCH2CH-
C[C@H]1[CH]COO1_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 18.86 kcal/mol
deltaH(298) 13.41 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 145,
    label = "C4H7O2_114",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.83621,0.0109717,5.99423e-05,-8.73024e-08,3.60019e-11,3202.29,1.25398], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.35781,0.0311285,-1.54115e-05,3.7332e-09,-3.5838e-13,2233.37,-6.08416], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3CH(OO)CHCH2
C[C@@H](C=C)O[O]_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 16.81 kcal/mol
deltaH(298) 12.13 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 146,
    label = "C4H7O2_115",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {3,S} {13,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  O u1 p2 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.13214,0.0121068,6.19852e-05,-9.16627e-08,3.79973e-11,-23035.4,4.2221], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.60989,0.0327018,-1.62802e-05,3.88846e-09,-3.61127e-13,-23938.2,-2.80114], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3C(O)CH2CH2O
CC(=O)CC[O]_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -35.57 kcal/mol
deltaH(298) -40.31 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 147,
    label = "C4H7O2_116",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {12,S}
4  C u0 p0 c0 {2,S} {3,D} {11,S}
5  O u0 p2 c0 {1,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.86298,0.00186226,7.88439e-05,-1.0312e-07,4.08021e-11,3579.91,-2.591], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.01226,0.0308367,-1.46315e-05,3.32816e-09,-2.94692e-13,2709.1,-4.15982], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3CHCHCH2OO;CCCC
C/C=C/CO[O]_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 17.59 kcal/mol
deltaH(298) 12.95 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 148,
    label = "C4H7O2_118",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,D} {13,S}
5  O u1 p2 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.57786,0.0449448,-2.91117e-05,6.5264e-09,1.05599e-12,-20935.3,11.6275], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.49358,0.0302039,-1.49609e-05,3.59787e-09,-3.4104e-13,-22186,-13.3382], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3CH(O)CH2CHO
C[C@@H](CC=O)[O]_m2 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -31.39 kcal/mol
deltaH(298) -36.00 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 149,
    label = "O_8",
    molecule = 
"""
multiplicity 3
1 O u2 p2 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.16831,-0.00328278,6.65718e-06,-6.14779e-09,2.12143e-12,28813,2.03645], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.59385,-0.000144816,9.01992e-08,-2.56181e-11,2.74255e-15,28900.6,4.63913], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""3O
[O]_m3        torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) 58.37 kcal/mol
deltaH(298) 58.94 kcal/mol""",
    longDesc = 
u"""

""",
)

entry(
    index = 150,
    label = "CH4O2_53",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {7,S}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.7291,0.00196204,3.33745e-05,-4.43549e-08,1.76244e-11,-17288.6,4.63428], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.95859,0.0151183,-7.30968e-06,1.72993e-09,-1.62001e-13,-17498.8,6.22763], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CH3OOH
COO_m1 ,  torsopt/wb97xd/6-31g*/gaussian,torsscan/m062x/cc-pvtz/gaussian,opt/b2plypd3/cc-pvtz/gaussian,freq/b2plypd3/cc-pvtz/gaussian,energy/ccsd(t)-f12/cc-pvdz-f12/molpro,energy/ccsd(t)-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvdz-f12/molpro,energy/mp2-f12/cc-pvtz-f12/molpro,energy/mp2-f12/cc-pvqz-f12/molpro,composite/cbs_dzmtz/energy=e[4]+e[7]-e[6],composite/cbs_tzmqz/energy=e[5]+e[8]-e[7]
deltaH(0) -27.89 kcal/mol
deltaH(298) -30.95 kcal/mol""",
    longDesc = 
u"""

""",
)

