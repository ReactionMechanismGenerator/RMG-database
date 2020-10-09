#!/usr/bin/env python
# encoding: utf-8

name = "llnl_gasoline2"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 0,
    label = "H",
    molecule = 
"""
multiplicity 2
1 H u1 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,0,0,0,0,25471.6,-0.460118], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.5,0,0,0,0,25471.6,-0.460118], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""120186""",
    longDesc = 
u"""

""",
)

entry(
    index = 1,
    label = "H2",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.29812,0.000824944,-8.14302e-07,-9.47543e-11,4.13487e-13,-1012.52,-3.29409], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.99142,0.000700064,-5.63383e-08,-9.23158e-12,1.58275e-15,-835.034,-1.35511], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""121286""",
    longDesc = 
u"""

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
            NASAPolynomial(coeffs=[2.94643,-0.00163817,2.42103e-06,-1.60284e-09,3.8907e-13,29147.6,2.964], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.54206,-2.75506e-05,-3.1028e-09,4.55107e-12,-4.36805e-16,29230.8,4.92031], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""120186""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "O2",
    molecule = 
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.21294,0.00112749,-5.75615e-07,1.31388e-09,-8.76855e-13,-1005.25,6.03474], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.69758,0.00061352,-1.25884e-07,1.77528e-11,-1.13644e-15,-1233.93,3.18917], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""121386""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "OH",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.41896,0.000319256,-3.08293e-07,3.64407e-10,-1.00195e-13,3452.64,2.54433], Tmin=(298,'K'), Tmax=(1710,'K')),
            NASAPolynomial(coeffs=[2.85376,0.00102994,-2.32666e-07,1.93751e-11,-3.1576e-16,3699.5,5.78757], Tmin=(1710,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/13/ 0 RUCIC""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "H2O",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.38684,0.00347498,-6.3547e-06,6.96858e-09,-2.50659e-12,-30208.1,2.59023], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.67215,0.00305629,-8.73026e-07,1.201e-10,-6.39162e-15,-29899.2,6.86282], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""20387""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "N2",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 N u0 p1 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.29868,0.00140824,-3.96322e-06,5.64152e-09,-2.44486e-12,-1020.9,3.95037], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.92664,0.00148798,-5.68476e-07,1.0097e-10,-6.75335e-15,-922.798,5.98053], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""121286""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
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
            NASAPolynomial(coeffs=[4.3018,-0.00474912,2.11583e-05,-2.42764e-08,9.29225e-12,294.808,3.71666], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.01721,0.00223982,-6.33658e-07,1.14246e-10,-1.07909e-14,111.857,3.7851], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""L 5/89""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
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
            NASAPolynomial(coeffs=[3.38875,0.00656923,-1.48501e-07,-4.62581e-09,2.47151e-12,-17663.2,6.78536], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.57317,0.00433614,-1.47469e-06,2.3489e-10,-1.43165e-14,-18007,0.501137], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""120186""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "CO",
    molecule = 
"""
1 O u0 p1 c+1 {2,T}
2 C u0 p1 c-1 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.19036,0.00089442,-3.24928e-08,-1.046e-10,2.41966e-14,-14286.9,5.33278], Tmin=(298,'K'), Tmax=(1429,'K')),
            NASAPolynomial(coeffs=[3.11217,0.00115948,-3.3848e-07,4.41403e-11,-2.12862e-15,-14271.9,5.71725], Tmin=(1429,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""29/11/04""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "CO2",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,D} {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5793,0.00824685,-6.42716e-06,2.54637e-09,-4.1203e-13,-48416.3,8.81141], Tmin=(298,'K'), Tmax=(1380,'K')),
            NASAPolynomial(coeffs=[5.18953,0.00206006,-7.33575e-07,1.17004e-10,-6.91729e-15,-49317.9,-5.18289], Tmin=(1380,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""29/11/04""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "CH2O",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.00754,0.00304729,5.25109e-06,-5.12019e-09,1.27134e-12,-14118.8,8.1012], Tmin=(298,'K'), Tmax=(1486,'K')),
            NASAPolynomial(coeffs=[4.02068,0.00509903,-1.7643e-06,2.76026e-10,-1.60998e-14,-14928.7,1.06526], Tmin=(1486,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""6/29/04 RUSCI""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "HCO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u1 p0 c0 {1,D} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8105,0.00081327,3.13165e-06,-2.39478e-09,5.06895e-13,4038.6,4.94843], Tmin=(298,'K'), Tmax=(1690,'K')),
            NASAPolynomial(coeffs=[3.44148,0.00352158,-1.24136e-06,1.97329e-10,-1.16539e-14,3974.1,6.24593], Tmin=(1690,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""29/11/04""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "HOCHO",
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
            NASAPolynomial(coeffs=[1.43548,0.0163363,-1.06257e-05,3.32133e-09,-4.02176e-13,-46461.7,17.2886], Tmin=(298,'K'), Tmax=(1376,'K')),
            NASAPolynomial(coeffs=[6.68733,0.00514289,-1.82239e-06,2.89719e-10,-1.70892e-14,-48399.5,-11.3105], Tmin=(1376,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""4/ 9/98 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "HOCH2O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {6,S}
3 O u1 p2 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.11183,0.00753851,3.77337e-06,-5.38746e-09,1.45616e-12,-21247.2,7.46807], Tmin=(298,'K'), Tmax=(1452,'K')),
            NASAPolynomial(coeffs=[6.39522,0.00743673,-2.50422e-06,3.8488e-10,-2.21779e-14,-22555.8,-6.63866], Tmin=(1452,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""4/ 9/98 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "CH2OH",
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
            NASAPolynomial(coeffs=[3.05674,0.0119336,-8.72501e-06,3.82781e-09,-7.22888e-13,-2831.4,8.98878], Tmin=(298,'K'), Tmax=(1399,'K')),
            NASAPolynomial(coeffs=[5.41876,0.00566185,-1.87471e-06,2.84442e-10,-1.623e-14,-3614.76,-3.49278], Tmin=(1399,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""2/25/ 4 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "CH3O",
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
            NASAPolynomial(coeffs=[2.23058,0.00853179,1.02167e-06,-3.41047e-09,9.94691e-13,945.94,12.8378], Tmin=(298,'K'), Tmax=(1509,'K')),
            NASAPolynomial(coeffs=[4.64787,0.00690831,-2.34405e-06,3.61995e-10,-2.09254e-14,-299.209,-1.5774], Tmin=(1509,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""8/ 9/ 4 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "CH3O2H",
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
            NASAPolynomial(coeffs=[2.8388,0.0186096,-8.48165e-06,1.00387e-09,1.71612e-13,-17403.4,11.6092], Tmin=(298,'K'), Tmax=(1367,'K')),
            NASAPolynomial(coeffs=[8.80409,0.00809427,-2.85843e-06,4.5337e-10,-2.66981e-14,-19851.2,-21.7001], Tmin=(1367,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""1/14/ 5 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "CH3O2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u1 p2 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80498,0.00980785,-3.90941e-07,-2.23073e-09,6.43311e-13,-455.626,7.81789], Tmin=(298,'K'), Tmax=(1365,'K')),
            NASAPolynomial(coeffs=[6.34719,0.00792089,-2.76602e-06,4.35361e-10,-2.54985e-14,-1834.36,-7.42553], Tmin=(1365,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""1/14/ 5 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
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
            NASAPolynomial(coeffs=[3.72113,-0.00250293,1.90247e-05,-1.46871e-08,3.43791e-12,-10142.4,1.22777], Tmin=(298,'K'), Tmax=(1462,'K')),
            NASAPolynomial(coeffs=[4.09618,0.00744331,-2.63872e-06,4.19578e-10,-2.47508e-14,-11383.6,-4.67561], Tmin=(1462,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""29/11/04""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
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
            NASAPolynomial(coeffs=[3.43858,0.00407753,3.19831e-07,-9.47669e-10,2.21828e-13,16316.4,2.52807], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[3.51281,0.00511413,-1.67632e-06,2.52495e-10,-1.43303e-14,16123.8,1.62436], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "CH2",
    molecule = 
"""
multiplicity 3
1 C u2 p0 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76224,0.00115982,2.48958e-07,8.80084e-10,-7.33244e-13,45367.9,1.71258], Tmin=(250,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.63641,0.00193306,-1.68702e-07,-1.0099e-10,1.80826e-14,45341.3,2.15656], Tmin=(1000,'K'), Tmax=(4000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (4000,'K'),
    ),
    shortDesc = u"""120186""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "CH2(S)",
    molecule = 
"""
1 C u0 p1 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97126,-0.000169909,1.02537e-06,2.49255e-09,-1.98127e-12,49893.7,0.0575321], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.55289,0.00206679,-1.91412e-07,-1.10467e-10,2.02135e-14,49849.8,1.68657], Tmin=(1000,'K'), Tmax=(4000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (4000,'K'),
    ),
    shortDesc = u"""31287""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "C2H6",
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
            NASAPolynomial(coeffs=[0.0478623,0.0240569,-1.15156e-05,2.48666e-09,-1.78344e-13,-11092.3,20.6544], Tmin=(298,'K'), Tmax=(1383,'K')),
            NASAPolynomial(coeffs=[6.05973,0.0130383,-4.48104e-06,6.97762e-10,-4.05606e-14,-13575.1,-12.8608], Tmin=(1383,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""8/ 4/ 4 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "C2H5",
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
            NASAPolynomial(coeffs=[1.3273,0.0176657,-6.14927e-06,-3.01143e-10,4.38618e-13,13428.4,17.1789], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[5.88784,0.0103077,-3.46844e-06,5.32499e-10,-3.06513e-14,11506.5,-8.49652], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""8/ 4/ 4 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "C2H4",
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
            NASAPolynomial(coeffs=[0.23388,0.0196335,-1.16833e-05,3.64246e-09,-4.77443e-13,5464.89,19.7084], Tmin=(298,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[5.22176,0.00896137,-3.04869e-06,4.71466e-10,-2.7274e-14,3603.9,-7.47789], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""10/ 4/ 5 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "C2H3",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u1 p0 c0 {1,D} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.2533,0.0156258,-1.07804e-05,4.18055e-09,-7.0136e-13,35073.5,17.1342], Tmin=(298,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[5.07331,0.00658316,-2.23763e-06,3.45803e-10,-1.9994e-14,33723.5,-3.39793], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""10/ 4/ 5 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "C2H2",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {3,S}
2 C u0 p0 c0 {1,T} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.06743,0.0146569,-1.52947e-05,8.30966e-09,-1.72932e-12,25957.9,8.62759], Tmin=(298,'K'), Tmax=(1407,'K')),
            NASAPolynomial(coeffs=[4.98265,0.00425993,-1.37484e-06,2.04718e-10,-1.15192e-14,25269.7,-5.81321], Tmin=(1407,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""10/ 4/ 5 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "CH3CHO",
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
            NASAPolynomial(coeffs=[1.7706,0.0184475,-7.24138e-06,2.34365e-10,3.35544e-13,-21807.9,16.5023], Tmin=(298,'K'), Tmax=(1377,'K')),
            NASAPolynomial(coeffs=[6.98519,0.00967898,-3.31842e-06,5.16026e-10,-2.99726e-14,-23980.7,-12.7485], Tmin=(1377,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""8/10/ 4 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "CH3CO",
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
            NASAPolynomial(coeffs=[2.52884,0.0137152,-4.28607e-06,-7.71684e-10,4.83836e-13,-3025.47,14.034], Tmin=(298,'K'), Tmax=(1371,'K')),
            NASAPolynomial(coeffs=[6.56682,0.00755309,-2.59967e-06,4.05335e-10,-2.35876e-14,-4766.9,-8.83302], Tmin=(1371,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""8/10/ 4 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "CH2CHO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {3,S} {6,S}
3 O u1 p2 c0 {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.47617,0.0208974,-1.50124e-05,5.62967e-09,-8.76624e-13,-482.051,16.3756], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[7.54146,0.00682297,-2.36939e-06,3.71634e-10,-2.1716e-14,-2614.37,-16.2603], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""8/10/ 4 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "CH2CO",
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
            NASAPolynomial(coeffs=[2.97497,0.0121187,-2.34505e-06,-6.46668e-09,3.90565e-12,-7632.64,8.67355], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.03882,0.00580484,-1.92095e-06,2.79448e-10,-1.45887e-14,-8583.4,-7.65758], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""121686""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "HCCO",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {3,S}
2 C u0 p0 c0 {3,T} {4,S}
3 C u0 p0 c0 {1,S} {2,T}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.04796,0.00445348,2.26828e-07,-1.48209e-09,2.25074e-13,19658.9,0.481844], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.75807,0.0020004,-2.02761e-07,-1.04113e-10,1.96516e-14,19015.1,-9.07126], Tmin=(1000,'K'), Tmax=(4000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (4000,'K'),
    ),
    shortDesc = u"""32387""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "CH3CO3H",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {5,S}
2 O u0 p2 c0 {1,S} {9,S}
3 O u0 p2 c0 {5,D}
4 C u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
5 C u0 p0 c0 {1,S} {3,D} {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.24136,0.0337964,-2.53887e-05,9.67584e-09,-1.49266e-12,-42467.8,17.0668], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[12.506,0.0094779,-3.30402e-06,5.19631e-10,-3.04234e-14,-45985.7,-37.9196], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""6/26/95 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    label = "CH3CO3",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {5,S}
2 O u0 p2 c0 {5,D}
3 O u1 p2 c0 {1,S}
4 C u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
5 C u0 p0 c0 {1,S} {2,D} {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.60373,0.027008,-2.08293e-05,8.50541e-09,-1.43846e-12,-23420.5,11.2015], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[11.2522,0.00833653,-2.89015e-06,4.52782e-10,-2.64354e-14,-26023.9,-29.637], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""4/ 3/ 0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "CH3CO2",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {4,S}
2 O u0 p2 c0 {4,D}
3 C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4 C u0 p0 c0 {1,S} {2,D} {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.37441,0.0249116,-1.74309e-05,6.248e-09,-9.09517e-13,-27233,18.1405], Tmin=(298,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[8.5406,0.00832951,-2.84722e-06,4.41927e-10,-2.56373e-14,-29729.1,-20.3884], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""2/14/95 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
    label = "C2H5OH",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {9,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.179106,0.030906,-1.93597e-05,6.31831e-09,-8.53167e-13,-29567.1,24.4716], Tmin=(298,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[8.31742,0.0129603,-4.39286e-06,6.77735e-10,-3.91448e-14,-32522,-19.6503], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""8/ 9/ 4 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    label = "PC2H4OH",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,S} {7,S}
3 O u0 p2 c0 {1,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.990023,0.0261564,-1.65928e-05,5.50525e-09,-7.57521e-13,-4960.32,22.8676], Tmin=(298,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[7.8851,0.0108288,-3.6683e-06,5.65734e-10,-3.26673e-14,-7449.75,-14.4674], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""8/ 9/ 4 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "SC2H4OH",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u1 p0 c0 {1,S} {3,S} {7,S}
3 O u0 p2 c0 {2,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.61104,0.0263512,-1.82941e-05,6.91243e-09,-1.10384e-12,-8714.95,18.0115], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[8.34981,0.0103718,-3.49683e-06,5.37525e-10,-3.09661e-14,-11055.6,-18.1354], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""8/ 9/ 4 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "C2H3O1-2",
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
            NASAPolynomial(coeffs=[-1.62965,0.0293455,-2.43738e-05,1.00522e-08,-1.61259e-12,15245.9,32.2783], Tmin=(298,'K'), Tmax=(1492,'K')),
            NASAPolynomial(coeffs=[6.88486,0.00694721,-2.23215e-06,3.32191e-10,-1.87125e-14,12644.2,-12.3843], Tmin=(1492,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""4/ 3/ 0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "CH3COCH3",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,D}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.24527,0.029976,-1.40027e-05,2.16454e-09,1.27637e-13,-27834.9,20.3683], Tmin=(298,'K'), Tmax=(1382,'K')),
            NASAPolynomial(coeffs=[9.62674,0.0145519,-4.97749e-06,7.72795e-10,-4.48367e-14,-31186.2,-26.1613], Tmin=(1382,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""8/30/ 4 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    label = "CH3COCH2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u1 p2 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.22337,0.0324547,-2.13543e-05,6.96778e-09,-8.9916e-13,-6594.19,20.5537], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[10.8892,0.0111541,-3.85517e-06,6.02834e-10,-3.51533e-14,-10074.1,-31.8043], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""8/30/ 4 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "CH3COCH2O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {4,S}
2  O u0 p2 c0 {6,D}
3  O u1 p2 c0 {1,S}
4  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
5  C u0 p0 c0 {6,S} {9,S} {10,S} {11,S}
6  C u0 p0 c0 {2,D} {4,S} {5,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.95535,0.0270255,-1.37385e-05,3.53736e-09,-4.03923e-13,-20667.9,5.21436], Tmin=(298,'K'), Tmax=(1379,'K')),
            NASAPolynomial(coeffs=[12.769,0.0142555,-4.92821e-06,7.70449e-10,-4.49111e-14,-23479.9,-32.7156], Tmin=(1379,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""2/14/95""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    label = "CH3COCH2O2H",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {12,S}
3  O u0 p2 c0 {6,D}
4  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
5  C u0 p0 c0 {6,S} {9,S} {10,S} {11,S}
6  C u0 p0 c0 {3,D} {4,S} {5,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.9479,0.0360474,-2.2172e-05,6.98297e-09,-9.21269e-13,-38868.7,8.49926], Tmin=(298,'K'), Tmax=(1381,'K')),
            NASAPolynomial(coeffs=[15.2373,0.0144115,-5.0129e-06,7.87071e-10,-4.60226e-14,-42756.4,-47.7384], Tmin=(1381,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""2/14/95""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "CH3COCH2O",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {4,S}
2  O u0 p2 c0 {5,D}
3  C u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
4  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
5  C u0 p0 c0 {2,D} {3,S} {4,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72928,0.0263944,-1.09796e-05,8.58185e-10,3.39475e-13,-19155.2,11.8505], Tmin=(298,'K'), Tmax=(1370,'K')),
            NASAPolynomial(coeffs=[11.4638,0.0132124,-4.5658e-06,7.13898e-10,-4.16281e-14,-22383.3,-31.5128], Tmin=(1370,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""4/ 3/ 0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    label = "C2H3CO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,D}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u0 p0 c0 {2,D} {6,S} {7,S}
4 C u1 p0 c0 {1,D} {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.36242,0.0315274,-3.00219e-05,1.48167e-08,-2.87972e-12,4257.7,17.2627], Tmin=(298,'K'), Tmax=(1402,'K')),
            NASAPolynomial(coeffs=[9.37468,0.00791297,-2.67198e-06,4.11115e-10,-2.36979e-14,1929.7,-24.0893], Tmin=(1402,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""4/ 3/ 0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 46,
    label = "C2H5CHO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,D} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.93108,0.00887944,2.03764e-05,-1.80149e-08,4.14086e-12,-25137.8,-0.58702], Tmin=(298,'K'), Tmax=(1375,'K')),
            NASAPolynomial(coeffs=[8.87216,0.0201711,-8.06488e-06,1.37618e-09,-8.48922e-14,-28384.9,-23.5069], Tmin=(1375,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""8/10/ 4 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
    label = "C2H5CO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 C u1 p0 c0 {1,S} {9,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.35352,-0.0040874,3.64218e-05,-2.72458e-08,6.0644e-12,-6585.77,-10.5948], Tmin=(298,'K'), Tmax=(1362,'K')),
            NASAPolynomial(coeffs=[10.0147,0.0161528,-6.62976e-06,1.15291e-09,-7.21263e-14,-10043,-28.8571], Tmin=(1362,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""8/10/ 4 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    label = "IC3H7",
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
            NASAPolynomial(coeffs=[1.63418,0.0240171,-4.72808e-06,-3.24355e-09,1.23539e-12,9207.53,18.3848], Tmin=(298,'K'), Tmax=(1373,'K')),
            NASAPolynomial(coeffs=[8.14705,0.0158727,-5.44612e-06,8.47208e-10,-4.92179e-14,6180.73,-19.1981], Tmin=(1373,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""8/ 4/ 4 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    label = "NC3H7",
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
            NASAPolynomial(coeffs=[0.474365,0.031919,-1.7191e-05,4.45928e-09,-4.36675e-13,10631.5,23.2671], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[8.88635,0.0152273,-5.21906e-06,8.11259e-10,-4.71028e-14,7346.72,-23.0728], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""8/ 4/ 4 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 50,
    label = "C3H6",
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
            NASAPolynomial(coeffs=[0.394615,0.0289108,-1.54887e-05,3.88814e-09,-3.3789e-13,1177.6,21.9004], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[8.01596,0.0137024,-4.6625e-06,7.21254e-10,-4.1737e-14,-1767.49,-20.0161], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""10/23/ 5 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
    label = "C3H5-A",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 C u1 p0 c0 {1,S} {7,S} {8,S}
3 C u0 p0 c0 {1,D} {5,S} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.529132,0.0334559,-2.53401e-05,1.02866e-08,-1.73258e-12,19494.1,24.6172], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[8.45884,0.0112695,-3.83793e-06,5.94059e-10,-3.43918e-14,16468.3,-23.2704], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""10/23/ 5 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
    label = "C3H5-S",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u1 p0 c0 {2,D} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.32807,0.0253108,-1.5153e-05,4.74346e-09,-6.24666e-13,30798.1,18.3329], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[7.88766,0.0113013,-3.84213e-06,5.93983e-10,-3.43567e-14,28348.5,-17.4292], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""10/23/ 5 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 53,
    label = "C3H5-T",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,D} {7,S} {8,S}
3 C u1 p0 c0 {1,S} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.17917,0.0203827,-7.91414e-06,4.76906e-10,2.70399e-13,29600.3,14.8786], Tmin=(298,'K'), Tmax=(1382,'K')),
            NASAPolynomial(coeffs=[7.37492,0.011751,-4.00021e-06,6.18947e-10,-3.58215e-14,27398.2,-14.3479], Tmin=(1382,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""10/23/ 5 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 54,
    label = "C3H4-P",
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
            NASAPolynomial(coeffs=[3.02973,0.0149896,-1.3985e-06,-3.96962e-09,1.38822e-12,21484.1,8.00459], Tmin=(298,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[9.7681,0.00521915,-3.75314e-07,-2.99219e-10,5.10788e-14,18602.8,-30.2068], Tmin=(1400,'K'), Tmax=(4000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (4000,'K'),
    ),
    shortDesc = u"""101993""",
    longDesc = 
u"""

""",
)

entry(
    index = 55,
    label = "C3H4-A",
    molecule = 
"""
1 C u0 p0 c0 {3,D} {4,S} {5,S}
2 C u0 p0 c0 {3,D} {6,S} {7,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.53983,0.0163344,-1.76495e-06,-4.64736e-09,1.72913e-12,22512.4,9.9357], Tmin=(298,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[9.77626,0.00530214,-3.70112e-07,-3.02639e-10,5.08958e-14,19549.7,-30.7706], Tmin=(1400,'K'), Tmax=(4000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (4000,'K'),
    ),
    shortDesc = u"""101993""",
    longDesc = 
u"""

""",
)

entry(
    index = 56,
    label = "C3H3",
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
            NASAPolynomial(coeffs=[4.7542,0.0110803,2.79332e-07,-5.47921e-09,1.94963e-12,39888.8,0.585455], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.83105,0.0043572,-4.10907e-07,-2.36872e-10,4.37652e-14,38474.2,-21.7792], Tmin=(1000,'K'), Tmax=(4000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (4000,'K'),
    ),
    shortDesc = u"""82489""",
    longDesc = 
u"""

""",
)

entry(
    index = 57,
    label = "C3H2",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {3,D}
3 C u2 p0 c0 {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.16671,0.0248257,-4.59164e-05,4.26802e-08,-1.48215e-11,63504.2,8.86945], Tmin=(150,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.67098,0.00274875,-4.37094e-07,-6.4556e-11,1.66389e-14,62597.2,-12.3689], Tmin=(1000,'K'), Tmax=(4000,'K')),
        ],
        Tmin = (150,'K'),
        Tmax = (4000,'K'),
    ),
    shortDesc = u"""102193""",
    longDesc = 
u"""

""",
)

entry(
    index = 58,
    label = "C3H5O",
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
            NASAPolynomial(coeffs=[1.19823,0.030558,-1.8063e-05,4.8615e-09,-4.19855e-13,9582.18,21.5566], Tmin=(298,'K'), Tmax=(1380,'K')),
            NASAPolynomial(coeffs=[10.2552,0.0114984,-3.84646e-06,5.8891e-10,-3.38558e-14,6265.61,-27.7655], Tmin=(1380,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/20/95 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 59,
    label = "NC3H7O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {4,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.10731,0.0396165,-2.49492e-05,8.5945e-09,-1.3124e-12,-7937.46,18.9083], Tmin=(298,'K'), Tmax=(1384,'K')),
            NASAPolynomial(coeffs=[12.6327,0.0169911,-5.88867e-06,9.22195e-10,-5.38231e-14,-11919.5,-38.5349], Tmin=(1384,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 60,
    label = "C4H8-1",
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
            NASAPolynomial(coeffs=[-0.833377,0.0454141,-2.97609e-05,1.03518e-08,-1.51976e-12,-1491.62,29.4328], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[11.3457,0.0180843,-6.17277e-06,9.56926e-10,-5.54586e-14,-5886.59,-36.4627], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""6/29/ 4 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 61,
    label = "C4H71-2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {4,D} {10,S} {11,S}
4  C u1 p0 c0 {1,S} {3,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.964124,0.0366781,-2.17105e-05,6.5588e-09,-8.11791e-13,26842.3,22.4366], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[10.7092,0.0161103,-5.49846e-06,8.52304e-10,-4.93905e-14,23187.4,-30.7648], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""4/ 2/97 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 62,
    label = "C4H6",
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
            NASAPolynomial(coeffs=[-1.43095,0.0478706,-4.15447e-05,1.9155e-08,-3.57159e-12,11755.1,29.0826], Tmin=(298,'K'), Tmax=(1398,'K')),
            NASAPolynomial(coeffs=[11.1634,0.0137164,-4.69716e-06,7.29694e-10,-4.23486e-14,7790.4,-36.9848], Tmin=(1398,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""4/ 4/ 0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 63,
    label = "C2H5COCH2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u1 p2 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.54014,0.0439486,-2.97002e-05,1.05495e-08,-1.58599e-12,-9507.97,19.9707], Tmin=(298,'K'), Tmax=(1383,'K')),
            NASAPolynomial(coeffs=[14.2099,0.0157866,-5.50529e-06,8.65871e-10,-5.06913e-14,-14128.5,-48.7133], Tmin=(1383,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""4/ 3/ 0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 64,
    label = "NC3H7CHO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,D} {13,S}
5  H u0 p0 c0 {1,S}
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
            NASAPolynomial(coeffs=[1.87416,0.041924,-2.35149e-05,6.26914e-09,-6.09444e-13,-27103.2,19.1569], Tmin=(298,'K'), Tmax=(1378,'K')),
            NASAPolynomial(coeffs=[13.5988,0.0181652,-6.17844e-06,9.5598e-10,-5.53443e-14,-31584.5,-45.179], Tmin=(1378,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""9/27/95 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 65,
    label = "IC4H9",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {1,S} {12,S} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
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
            NASAPolynomial(coeffs=[-0.221458,0.0463756,-2.88283e-05,9.60201e-09,-1.39021e-12,6761.54,26.4801], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[12.1277,0.0198689,-6.85937e-06,1.07142e-09,-6.24185e-14,2119.52,-40.8727], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""8/ 4/ 4 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 66,
    label = "TC4H9",
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
            NASAPolynomial(coeffs=[3.043,0.0291276,-4.01387e-06,-4.90274e-09,1.64015e-12,4047.81,12.1127], Tmin=(298,'K'), Tmax=(1372,'K')),
            NASAPolynomial(coeffs=[10.5855,0.0211892,-7.31668e-06,1.14296e-09,-6.65899e-14,318.311,-32.0671], Tmin=(1372,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""8/ 4/ 4 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 67,
    label = "IC4H8",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.938433,0.0390547,-2.16437e-05,5.87267e-09,-6.14435e-13,-3954.52,19.8338], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[11.2258,0.0181796,-6.20349e-06,9.61444e-10,-5.57088e-14,-7906.18,-36.6412], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""10/23/ 5 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 68,
    label = "IC4H7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  C u1 p0 c0 {2,S} {10,S} {11,S}
4  C u0 p0 c0 {2,D} {8,S} {9,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.000720882,0.0436496,-3.16386e-05,1.23985e-08,-2.04378e-12,14365.4,23.3234], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[11.6383,0.0157681,-5.38539e-06,8.35173e-10,-4.84141e-14,10340.8,-39.026], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""10/23/ 5 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 69,
    label = "TC4H9O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {15,S}
6  H u0 p0 c0 {2,S}
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
            NASAPolynomial(coeffs=[1.08743,0.0582781,-4.33293e-05,1.76893e-08,-3.0677e-12,-14945.7,20.1872], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[16.7062,0.0207328,-7.17596e-06,1.12282e-09,-6.54941e-14,-20404.7,-63.5559], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 70,
    label = "IC4H9O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {2,S} {15,S}
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
            NASAPolynomial(coeffs=[1.21434,0.0545388,-3.67002e-05,1.34131e-08,-2.11742e-12,-11848.2,23.4153], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[15.9741,0.0213535,-7.39001e-06,1.15624e-09,-6.74408e-14,-17232.9,-56.5302], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 71,
    label = "IC4H8O2H-I",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {13,S} {14,S}
5  O u0 p2 c0 {2,S} {6,S}
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
            NASAPolynomial(coeffs=[0.994785,0.0589212,-4.25202e-05,1.61371e-08,-2.55905e-12,-4080.29,25.8951], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[18.0246,0.0193668,-6.74676e-06,1.0604e-09,-6.20506e-14,-10085.9,-65.763], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 72,
    label = "TC4H9O",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
4  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
5  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.532084,0.0571613,-4.20177e-05,1.63745e-08,-2.64125e-12,-13496.3,26.2777], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[15.0819,0.0194454,-6.61334e-06,1.02279e-09,-5.91797e-14,-18811.1,-57.1659], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""8/ 9/ 4 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 73,
    label = "IC4H7O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u1 p2 c0 {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.74701,0.0407783,-2.4475e-05,7.06503e-09,-7.51571e-13,4869.79,19.4536], Tmin=(298,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[13.3458,0.0161219,-5.44376e-06,8.38199e-10,-4.83608e-14,611.444,-43.6819], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""4/ 3/ 0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 74,
    label = "IC3H7CHO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,D} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
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
            NASAPolynomial(coeffs=[-0.273021,0.0489696,-3.1277e-05,1.00053e-08,-1.27512e-12,-27605.5,28.3451], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[13.7502,0.0183127,-6.28573e-06,9.78251e-10,-5.68539e-14,-32693.7,-47.7271], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""2/22/96 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 75,
    label = "TC3H6CHO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {2,S} {4,S}
4  C u0 p0 c0 {3,S} {11,D} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {4,D}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.87053,0.041487,-2.66816e-05,9.01532e-09,-1.27871e-12,-8977.31,16.6174], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[13.1013,0.0166392,-5.68458e-06,8.81808e-10,-5.1129e-14,-13063.9,-44.2706], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""2/22/96 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 76,
    label = "IC4H8OOH-IO2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {6,S}
2  O u0 p2 c0 {4,S} {7,S}
3  O u0 p2 c0 {1,S} {17,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {6,S} {7,S} {8,S} {9,S}
6  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
7  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
8  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.39424,0.0676573,-5.17084e-05,2.10796e-08,-3.5996e-12,-22478.7,22.503], Tmin=(298,'K'), Tmax=(1385,'K')),
            NASAPolynomial(coeffs=[21.897,0.0209638,-7.34665e-06,1.15927e-09,-6.80225e-14,-29266.5,-82.0541], Tmin=(1385,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 TRM""",
    longDesc = 
u"""

""",
)

entry(
    index = 77,
    label = "IC4KETII",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {5,S}
2  O u0 p2 c0 {1,S} {15,S}
3  O u0 p2 c0 {7,D}
4  C u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
5  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
6  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
7  C u0 p0 c0 {3,D} {4,S} {14,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.15502,0.0610622,-4.49711e-05,1.70515e-08,-2.65949e-12,-38274.8,26.9612], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[19.5143,0.0182377,-6.38909e-06,1.00802e-09,-5.9144e-14,-44688.5,-71.7168], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 78,
    label = "IC3H5CHO",
    molecule = 
"""
1  O u0 p2 c0 {5,D}
2  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  C u0 p0 c0 {3,D} {9,S} {10,S}
5  C u0 p0 c0 {1,D} {3,S} {11,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.627184,0.046678,-3.74431e-05,1.58331e-08,-2.73952e-12,-15720.3,21.6034], Tmin=(298,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[13.6204,0.0137917,-4.7337e-06,7.36655e-10,-4.20098e-14,-20002.5,-47.3185], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/95 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 79,
    label = "IC3H5CO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {5,D}
2  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  C u0 p0 c0 {3,D} {9,S} {10,S}
5  C u1 p0 c0 {1,D} {3,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.85097,0.0418856,-3.62554e-05,1.65691e-08,-3.05851e-12,170.381,15.3014], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[13.0667,0.0116704,-3.99107e-06,6.19498e-10,-3.59348e-14,-3365.19,-43.5803], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""4/ 3/ 0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 80,
    label = "TC3H6OCHO",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {3,S}
2  O u0 p2 c0 {6,D}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
6  C u0 p0 c0 {2,D} {3,S} {13,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.37083,0.0538476,-3.82478e-05,1.32882e-08,-1.79229e-12,-21839.1,25.8142], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[17.0371,0.0154401,-5.28333e-06,8.21085e-10,-4.76898e-14,-27587.2,-63.7271], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""8/25/95 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 81,
    label = "C5H11-1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u1 p0 c0 {3,S} {15,S} {16,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.994216,0.0599861,-3.78319e-05,1.21311e-08,-1.57043e-12,4976.98,33.5998], Tmin=(298,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[15.4992,0.0238273,-8.13845e-06,1.26221e-09,-7.3173e-14,-1009.89,-55.8564], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""8/ 4/ 4 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 82,
    label = "C5H10-1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {5,D} {13,S}
5  C u0 p0 c0 {4,D} {14,S} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.06223,0.0574218,-3.74487e-05,1.27365e-08,-1.7961e-12,-4465.47,32.274], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[14.5852,0.0224072,-7.63348e-06,1.18189e-09,-6.84385e-14,-10089.8,-52.3684], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""4/ 7/97 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 83,
    label = "C5H91-3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {4,S} {11,S}
4  C u0 p0 c0 {3,S} {5,D} {12,S}
5  C u0 p0 c0 {4,D} {13,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.38014,0.0557608,-3.70144e-05,1.26884e-08,-1.78539e-12,12559,32.6441], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[14.186,0.0207129,-7.06961e-06,1.09607e-09,-6.35322e-14,7004.96,-51.4502], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""4/ 7/97 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 84,
    label = "NC4H9CHO",
    molecule = 
"""
1  O u0 p2 c0 {6,D}
2  C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
5  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
6  C u0 p0 c0 {1,D} {4,S} {16,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.59663,0.0543541,-3.21021e-05,9.35774e-09,-1.06689e-12,-29984.1,22.1281], Tmin=(298,'K'), Tmax=(1381,'K')),
            NASAPolynomial(coeffs=[16.7965,0.0225685,-7.67632e-06,1.18769e-09,-6.87546e-14,-35682.6,-60.9063], Tmin=(1381,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""2/29/96 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 85,
    label = "NC3H7COCH2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {5,S} {13,D}
5  C u1 p0 c0 {4,S} {14,S} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.958299,0.0568163,-3.99113e-05,1.52672e-08,-2.49221e-12,-12306.2,23.4113], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[16.1502,0.0214093,-7.3606e-06,1.14657e-09,-6.66713e-14,-17696.9,-58.3865], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""2/22/96 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 86,
    label = "NC7H16",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {7,S} {16,S} {17,S}
6  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
7  C u0 p0 c0 {5,S} {21,S} {22,S} {23,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.26836,0.0854356,-5.25347e-05,1.62946e-08,-2.02395e-12,-25658.7,35.3733], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[22.2149,0.0347676,-1.18407e-05,1.83298e-09,-1.0613e-13,-34276,-92.304], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 87,
    label = "C7H15-1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {7,S} {16,S} {17,S}
6  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
7  C u1 p0 c0 {5,S} {21,S} {22,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.49957,0.0808826,-5.00533e-05,1.56549e-08,-1.96616e-12,-1045.9,34.6564], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[21.7941,0.032628,-1.11138e-05,1.72067e-09,-9.96367e-14,-9209.38,-86.4954], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 88,
    label = "C7H15-2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {7,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {7,S} {19,S} {20,S} {21,S}
7  C u1 p0 c0 {4,S} {6,S} {22,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.0379156,0.0756727,-4.07474e-05,9.32679e-09,-4.92361e-13,-2356.05,33.7322], Tmin=(298,'K'), Tmax=(1382,'K')),
            NASAPolynomial(coeffs=[21.6369,0.0323325,-1.09274e-05,1.68357e-09,-9.71774e-14,-10587.4,-85.221], Tmin=(1382,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 89,
    label = "C7H15-3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
4  C u0 p0 c0 {6,S} {7,S} {12,S} {13,S}
5  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {4,S} {16,S} {17,S} {18,S}
7  C u1 p0 c0 {3,S} {4,S} {22,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.0379156,0.0756727,-4.07474e-05,9.32679e-09,-4.92361e-13,-2356.05,33.7322], Tmin=(298,'K'), Tmax=(1382,'K')),
            NASAPolynomial(coeffs=[21.6369,0.0323325,-1.09274e-05,1.68357e-09,-9.71774e-14,-10587.4,-85.221], Tmin=(1382,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 90,
    label = "C7H15-4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {7,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
7  C u1 p0 c0 {3,S} {4,S} {22,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.0379156,0.0756727,-4.07474e-05,9.32679e-09,-4.92361e-13,-2356.05,33.0427], Tmin=(298,'K'), Tmax=(1382,'K')),
            NASAPolynomial(coeffs=[21.6369,0.0323325,-1.09274e-05,1.68357e-09,-9.71774e-14,-10587.4,-85.9104], Tmin=(1382,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 91,
    label = "C7H14-1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {7,D} {19,S}
7  C u0 p0 c0 {6,D} {20,S} {21,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.67721,0.0824612,-5.46504e-05,1.87862e-08,-2.65738e-12,-10216.9,38.5068], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[21.0898,0.0310608,-1.05645e-05,1.63406e-09,-9.45598e-14,-18326,-84.4391], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 92,
    label = "C7H14-2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {7,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {3,S} {7,D} {21,S}
7  C u0 p0 c0 {5,S} {6,D} {20,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.16533,0.079044,-4.96102e-05,1.58569e-08,-2.05346e-12,-11736.2,35.9871], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[20.6192,0.0314853,-1.07162e-05,1.65828e-09,-9.59912e-14,-19671.3,-82.2519], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 93,
    label = "C7H14-3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
3  C u0 p0 c0 {5,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
6  C u0 p0 c0 {3,S} {7,D} {20,S}
7  C u0 p0 c0 {2,S} {6,D} {21,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.03027,0.0826324,-5.45514e-05,1.87706e-08,-2.67571e-12,-11514.1,40.2316], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[20.6823,0.0315389,-1.07571e-05,1.6669e-09,-9.6581e-14,-19645.1,-82.5235], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 94,
    label = "C7H131-3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  C u1 p0 c0 {3,S} {6,S} {17,S}
6  C u0 p0 c0 {5,S} {7,D} {18,S}
7  C u0 p0 c0 {6,D} {19,S} {20,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.01708,0.0808916,-5.43384e-05,1.88066e-08,-2.66059e-12,6665.08,38.9797], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[20.6978,0.0293585,-9.99754e-06,1.54773e-09,-8.96231e-14,-1380.5,-83.5627], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""6/24/99 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 95,
    label = "C7H15O2-1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {5,S} {15,S} {16,S}
4  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
5  C u0 p0 c0 {3,S} {7,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {8,S} {19,S} {20,S}
7  C u0 p0 c0 {5,S} {21,S} {22,S} {23,S}
8  O u0 p2 c0 {6,S} {24,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 O u1 p2 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.20889,0.0884062,-5.79861e-05,2.03575e-08,-3.0646e-12,-19291.9,29.8117], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[25.2657,0.0350804,-1.21179e-05,1.89361e-09,-1.10354e-13,-28111.3,-100.705], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 96,
    label = "C7H15O2-2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {5,S} {14,S} {15,S}
5  C u0 p0 c0 {4,S} {7,S} {16,S} {17,S}
6  C u0 p0 c0 {1,S} {18,S} {19,S} {20,S}
7  C u0 p0 c0 {5,S} {21,S} {22,S} {23,S}
8  O u0 p2 c0 {1,S} {24,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 O u1 p2 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.355253,0.0942381,-6.66955e-05,2.54796e-08,-4.13211e-12,-21579.5,32.9433], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[26.0536,0.0343832,-1.18713e-05,1.8545e-09,-1.08052e-13,-30684.2,-105.408], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 97,
    label = "C7H15O2-3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
5  C u0 p0 c0 {3,S} {7,S} {16,S} {17,S}
6  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
7  C u0 p0 c0 {5,S} {21,S} {22,S} {23,S}
8  O u0 p2 c0 {1,S} {24,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 O u1 p2 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.355253,0.0942381,-6.66955e-05,2.54796e-08,-4.13211e-12,-21579.5,32.9433], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[26.0536,0.0343832,-1.18713e-05,1.8545e-09,-1.08052e-13,-30684.2,-105.408], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 98,
    label = "C7H15O2-4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
5  C u0 p0 c0 {3,S} {7,S} {16,S} {17,S}
6  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
7  C u0 p0 c0 {5,S} {21,S} {22,S} {23,S}
8  O u0 p2 c0 {1,S} {24,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 O u1 p2 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.355253,0.0942381,-6.66955e-05,2.54796e-08,-4.13211e-12,-21579.5,32.2539], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[26.0536,0.0343832,-1.18713e-05,1.8545e-09,-1.08052e-13,-30684.2,-106.097], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 99,
    label = "C7H14OOH1-2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {6,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {7,S} {16,S} {17,S}
5  C u0 p0 c0 {7,S} {8,S} {18,S} {19,S}
6  C u0 p0 c0 {3,S} {20,S} {21,S} {22,S}
7  C u1 p0 c0 {4,S} {5,S} {23,S}
8  O u0 p2 c0 {5,S} {9,S}
9  O u0 p2 c0 {8,S} {24,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.11146,0.0891595,-5.67352e-05,1.7889e-08,-2.2226e-12,-12986.8,32.92], Tmin=(298,'K'), Tmax=(1383,'K')),
            NASAPolynomial(coeffs=[27.229,0.0324922,-1.1126e-05,1.72929e-09,-1.00428e-13,-22497.7,-108.902], Tmin=(1383,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 100,
    label = "C7H14OOH1-3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {7,S} {16,S} {17,S}
4  C u0 p0 c0 {5,S} {7,S} {14,S} {15,S}
5  C u0 p0 c0 {4,S} {8,S} {18,S} {19,S}
6  C u0 p0 c0 {2,S} {20,S} {21,S} {22,S}
7  C u1 p0 c0 {3,S} {4,S} {23,S}
8  O u0 p2 c0 {5,S} {9,S}
9  O u0 p2 c0 {8,S} {24,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.11146,0.0891595,-5.67352e-05,1.7889e-08,-2.2226e-12,-12986.8,32.92], Tmin=(298,'K'), Tmax=(1383,'K')),
            NASAPolynomial(coeffs=[27.229,0.0324922,-1.1126e-05,1.72929e-09,-1.00428e-13,-22497.7,-108.902], Tmin=(1383,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 101,
    label = "C7H14OOH2-4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {8,S} {10,S}
2  C u0 p0 c0 {4,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {7,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {2,S} {20,S} {21,S} {22,S}
7  C u1 p0 c0 {3,S} {4,S} {23,S}
8  O u0 p2 c0 {1,S} {9,S}
9  O u0 p2 c0 {8,S} {24,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.849786,0.0925107,-6.2536e-05,2.1788e-08,-3.1272e-12,-15364.1,33.2997], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[27.4035,0.0327528,-1.12992e-05,1.76445e-09,-1.02787e-13,-24863.7,-110.202], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 102,
    label = "C7H14OOH2-5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {7,S} {13,S} {14,S}
4  C u0 p0 c0 {6,S} {7,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {4,S} {20,S} {21,S} {22,S}
7  C u1 p0 c0 {3,S} {4,S} {23,S}
8  O u0 p2 c0 {1,S} {9,S}
9  O u0 p2 c0 {8,S} {24,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.849786,0.0925107,-6.2536e-05,2.1788e-08,-3.1272e-12,-15364.1,33.2997], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[27.4035,0.0327528,-1.12992e-05,1.76445e-09,-1.02787e-13,-24863.7,-110.202], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 103,
    label = "C7H14OOH3-5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
4  C u0 p0 c0 {6,S} {7,S} {15,S} {16,S}
5  C u0 p0 c0 {2,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {4,S} {20,S} {21,S} {22,S}
7  C u1 p0 c0 {3,S} {4,S} {23,S}
8  O u0 p2 c0 {1,S} {9,S}
9  O u0 p2 c0 {8,S} {24,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.849786,0.0925107,-6.2536e-05,2.1788e-08,-3.1272e-12,-15364.1,33.2997], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[27.4035,0.0327528,-1.12992e-05,1.76445e-09,-1.02787e-13,-24863.7,-110.202], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 104,
    label = "C7H14OOH4-2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {7,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {7,S} {20,S} {21,S} {22,S}
7  C u1 p0 c0 {4,S} {6,S} {23,S}
8  O u0 p2 c0 {1,S} {9,S}
9  O u0 p2 c0 {8,S} {24,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.849786,0.0925107,-6.2536e-05,2.1788e-08,-3.1272e-12,-15364.1,32.6103], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[27.4035,0.0327528,-1.12992e-05,1.76445e-09,-1.02787e-13,-24863.7,-110.891], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 105,
    label = "C7H14OOH1-3O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {9,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {5,S} {16,S} {17,S}
4  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {7,S} {18,S} {19,S}
6  C u0 p0 c0 {4,S} {8,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {22,S} {23,S} {24,S}
8  O u0 p2 c0 {6,S} {10,S}
9  O u0 p2 c0 {1,S} {25,S}
10 O u0 p2 c0 {8,S} {26,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 O u1 p2 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.89718,0.10623,-8.0277e-05,3.23649e-08,-5.4585e-12,-32279,30.2475], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[32.0144,0.0340056,-1.18416e-05,1.8606e-09,-1.08851e-13,-42717.2,-131.118], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/0 TRM""",
    longDesc = 
u"""

""",
)

entry(
    index = 106,
    label = "C7H14OOH2-4O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {9,S} {12,S}
2  C u0 p0 c0 {3,S} {6,S} {8,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {5,S} {15,S} {16,S}
5  C u0 p0 c0 {4,S} {7,S} {17,S} {18,S}
6  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {22,S} {23,S} {24,S}
8  O u0 p2 c0 {2,S} {10,S}
9  O u0 p2 c0 {1,S} {25,S}
10 O u0 p2 c0 {8,S} {26,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 O u1 p2 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.40912,0.110721,-8.71178e-05,3.63663e-08,-6.28351e-12,-34630.5,31.6223], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[32.8358,0.0332767,-1.15833e-05,1.81959e-09,-1.06434e-13,-45287.3,-135.976], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/0 TRM""",
    longDesc = 
u"""

""",
)

entry(
    index = 107,
    label = "C7H14OOH3-5O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {8,S} {11,S}
2  C u0 p0 c0 {3,S} {5,S} {9,S} {12,S}
3  C u0 p0 c0 {1,S} {2,S} {15,S} {16,S}
4  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {2,S} {7,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {22,S} {23,S} {24,S}
8  O u0 p2 c0 {1,S} {10,S}
9  O u0 p2 c0 {2,S} {25,S}
10 O u0 p2 c0 {8,S} {26,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 O u1 p2 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.40912,0.110721,-8.71178e-05,3.63663e-08,-6.28351e-12,-34630.5,31.6223], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[32.8358,0.0332767,-1.15833e-05,1.81959e-09,-1.06434e-13,-45287.3,-135.976], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/0 TRM""",
    longDesc = 
u"""

""",
)

entry(
    index = 108,
    label = "C7H14OOH4-2O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {8,S} {11,S}
2  C u0 p0 c0 {3,S} {6,S} {9,S} {12,S}
3  C u0 p0 c0 {1,S} {2,S} {17,S} {18,S}
4  C u0 p0 c0 {1,S} {5,S} {15,S} {16,S}
5  C u0 p0 c0 {4,S} {7,S} {13,S} {14,S}
6  C u0 p0 c0 {2,S} {22,S} {23,S} {24,S}
7  C u0 p0 c0 {5,S} {19,S} {20,S} {21,S}
8  O u0 p2 c0 {1,S} {10,S}
9  O u0 p2 c0 {2,S} {25,S}
10 O u0 p2 c0 {8,S} {26,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 O u1 p2 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.40912,0.110721,-8.71178e-05,3.63663e-08,-6.28351e-12,-34630.5,31.6223], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[32.8358,0.0332767,-1.15833e-05,1.81959e-09,-1.06434e-13,-45287.3,-135.976], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/0 TRM""",
    longDesc = 
u"""

""",
)

entry(
    index = 109,
    label = "C7H14O2-4",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {8,S} {10,S}
2  C u0 p0 c0 {3,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {5,S} {13,S} {14,S}
5  C u0 p0 c0 {4,S} {7,S} {15,S} {16,S}
6  C u0 p0 c0 {2,S} {17,S} {18,S} {19,S}
7  C u0 p0 c0 {5,S} {20,S} {21,S} {22,S}
8  O u0 p2 c0 {1,S} {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.39477,0.101847,-7.60046e-05,2.96538e-08,-4.74854e-12,-26711.8,55.1731], Tmin=(298,'K'), Tmax=(1399,'K')),
            NASAPolynomial(coeffs=[23.2693,0.0325585,-1.11625e-05,1.73574e-09,-1.00813e-13,-36435,-97.9457], Tmin=(1399,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 110,
    label = "C7H14O2-5",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {5,S} {8,S} {10,S}
2  C u0 p0 c0 {3,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {7,S} {15,S} {16,S}
6  C u0 p0 c0 {2,S} {17,S} {18,S} {19,S}
7  C u0 p0 c0 {5,S} {20,S} {21,S} {22,S}
8  O u0 p2 c0 {1,S} {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-7.24295,0.105687,-7.87952e-05,3.059e-08,-4.86103e-12,-36389.2,63.6526], Tmin=(298,'K'), Tmax=(1399,'K')),
            NASAPolynomial(coeffs=[22.6707,0.0334803,-1.14785e-05,1.78491e-09,-1.03672e-13,-46530.8,-96.1517], Tmin=(1399,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 111,
    label = "C7H14O3-5",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {5,S} {8,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
5  C u0 p0 c0 {2,S} {7,S} {15,S} {16,S}
6  C u0 p0 c0 {4,S} {17,S} {18,S} {19,S}
7  C u0 p0 c0 {5,S} {20,S} {21,S} {22,S}
8  O u0 p2 c0 {1,S} {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.39477,0.101847,-7.60046e-05,2.96538e-08,-4.74854e-12,-26711.8,55.1731], Tmin=(298,'K'), Tmax=(1399,'K')),
            NASAPolynomial(coeffs=[23.2693,0.0325585,-1.11625e-05,1.73574e-09,-1.00813e-13,-36435,-97.9457], Tmin=(1399,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 112,
    label = "NC7KET13",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {24,S}
3  O u0 p2 c0 {10,D}
4  C u0 p0 c0 {1,S} {5,S} {8,S} {11,S}
5  C u0 p0 c0 {4,S} {6,S} {12,S} {13,S}
6  C u0 p0 c0 {5,S} {7,S} {14,S} {15,S}
7  C u0 p0 c0 {6,S} {9,S} {16,S} {17,S}
8  C u0 p0 c0 {4,S} {10,S} {18,S} {19,S}
9  C u0 p0 c0 {7,S} {20,S} {21,S} {22,S}
10 C u0 p0 c0 {3,D} {8,S} {23,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {10,S}
24 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.21629,0.0947374,-6.90474e-05,2.6782e-08,-4.36392e-12,-48796.6,26.3157], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[29.0745,0.0317177,-1.10263e-05,1.73054e-09,-1.01162e-13,-58234.5,-118.064], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 113,
    label = "AC5H10",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {3,S} {5,D}
5  C u0 p0 c0 {4,D} {14,S} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.276631,0.0553539,-3.545e-05,1.19627e-08,-1.69878e-12,-6395.47,27.3912], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[14.5614,0.0225371,-7.701e-06,1.19468e-09,-6.92705e-14,-11800.5,-53.0652], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""2/14/95""",
    longDesc = 
u"""

""",
)

entry(
    index = 114,
    label = "AC5H9-A2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,S} {5,D}
4  C u1 p0 c0 {3,S} {11,S} {12,S}
5  C u0 p0 c0 {3,D} {13,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.21034,0.059927,-4.54162e-05,1.84721e-08,-3.12472e-12,11923.6,30.8551], Tmin=(298,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[14.975,0.0201226,-6.88146e-06,1.06814e-09,-6.19591e-14,6446.27,-55.4559], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""4/ 7/97 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 115,
    label = "AC5H9O-A2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {3,S} {5,D}
5  C u0 p0 c0 {4,D} {14,S} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u1 p2 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.517939,0.0570752,-3.82548e-05,1.31239e-08,-1.82693e-12,2226.6,27.0905], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[16.7123,0.02041,-6.90864e-06,1.0655e-09,-6.15447e-14,-3502.86,-60.2788], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/14/ 3 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 116,
    label = "IC4H7-I1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u1 p0 c0 {3,D} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.87632,0.0354486,-2.13105e-05,6.734e-09,-9.03166e-13,25871.3,16.2429], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[11.0958,0.015781,-5.3842e-06,8.3436e-10,-4.83401e-14,22417.6,-34.0427], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""4/ 2/97 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 117,
    label = "YC7H15",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {7,S} {19,S} {20,S} {21,S}
7  C u1 p0 c0 {2,S} {6,S} {22,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.30897,0.0696136,-3.3115e-05,5.82888e-09,3.54427e-14,-5785.13,24.5658], Tmin=(298,'K'), Tmax=(1384,'K')),
            NASAPolynomial(coeffs=[20.4581,0.0343076,-1.18103e-05,1.8413e-09,-1.07134e-13,-13497.9,-81.8212], Tmin=(1384,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 118,
    label = "XC7H14",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {2,S} {7,D} {19,S}
7  C u0 p0 c0 {6,D} {20,S} {21,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.33081,0.0821082,-5.49123e-05,1.94285e-08,-2.88887e-12,-13202.1,34.355], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[21.0164,0.0315215,-1.08074e-05,1.6804e-09,-9.75892e-14,-21211.7,-86.3819], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 119,
    label = "YC7H14",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {7,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {1,S} {7,D} {20,S}
7  C u0 p0 c0 {5,S} {6,D} {21,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.842233,0.0789798,-5.04574e-05,1.68934e-08,-2.37202e-12,-14597.2,31.9096], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[20.5074,0.0319644,-1.09619e-05,1.70464e-09,-9.90036e-14,-22394.6,-83.9267], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/19/ 0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 120,
    label = "XC7H13-X1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
5  C u1 p0 c0 {1,S} {6,S} {17,S}
6  C u0 p0 c0 {5,S} {7,D} {18,S}
7  C u0 p0 c0 {6,D} {19,S} {20,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.29007,0.0867902,-6.50308e-05,2.60294e-08,-4.3349e-12,5100.76,37.9381], Tmin=(298,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[21.4418,0.0290952,-9.98351e-06,1.55317e-09,-9.0237e-14,-2991.53,-88.8433], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""6/25/99 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 121,
    label = "XC7H13-Z",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {7,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {1,S} {7,D} {20,S}
7  C u1 p0 c0 {5,S} {6,D}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.64635,0.080451,-5.44891e-05,1.93901e-08,-2.88082e-12,3801.39,34.7109], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[20.6194,0.029828,-1.02444e-05,1.59477e-09,-9.26958e-14,-4137.8,-85.4759], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""6/25/99 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 122,
    label = "YC7H13-Y2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {6,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {6,D} {18,S}
6  C u0 p0 c0 {4,S} {5,D} {17,S}
7  C u1 p0 c0 {1,S} {19,S} {20,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.306783,0.0720691,-4.20234e-05,1.2005e-08,-1.32605e-12,1217.27,28.0339], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[19.6153,0.0307074,-1.0553e-05,1.64346e-09,-9.555e-14,-6296.51,-80.9255], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""6/25/99 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 123,
    label = "YC7H13-X2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {6,D} {17,S}
6  C u0 p0 c0 {5,D} {7,S} {18,S}
7  C u1 p0 c0 {6,S} {19,S} {20,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.0791769,0.0744508,-4.80064e-05,1.62688e-08,-2.31692e-12,9996.36,30.525], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[20.0933,0.0298145,-1.02305e-05,1.59153e-09,-9.246e-14,2649.33,-78.8504], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""6/25/99 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 124,
    label = "YC7H13O-Y2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {6,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {6,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {4,S} {5,S} {7,D}
7  C u0 p0 c0 {1,S} {6,D} {21,S}
8  O u1 p2 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.727102,0.0887136,-6.66484e-05,2.60146e-08,-4.12941e-12,-10333.3,32.3861], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[24.4896,0.0272499,-9.0688e-06,1.38348e-09,-7.93299e-14,-18769.1,-102.028], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/14/ 3 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 125,
    label = "ACC6H10",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,D} {13,S}
4  C u0 p0 c0 {2,S} {3,D} {12,S}
5  C u0 p0 c0 {1,S} {6,D} {14,S}
6  C u0 p0 c0 {5,D} {15,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.762524,0.0676164,-5.21692e-05,2.17987e-08,-3.79062e-12,2729.7,28.4975], Tmin=(298,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[17.118,0.0228898,-7.8169e-06,1.21213e-09,-7.02599e-14,-3268.88,-66.624], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/14/ 3 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 126,
    label = "ACC6H9-A",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,D} {13,S}
4  C u0 p0 c0 {2,S} {3,D} {12,S}
5  C u0 p0 c0 {6,D} {14,S} {15,S}
6  C u1 p0 c0 {1,S} {5,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.7085,0.0722433,-6.22151e-05,2.83599e-08,-5.2287e-12,21050.7,32.0185], Tmin=(298,'K'), Tmax=(1398,'K')),
            NASAPolynomial(coeffs=[17.534,0.0204762,-6.99836e-06,1.08583e-09,-6.29648e-14,14975.5,-69.0317], Tmin=(1398,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/14/ 3 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 127,
    label = "IC8H18",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {18,S} {19,S} {20,S}
5  C u0 p0 c0 {1,S} {21,S} {22,S} {23,S}
6  C u0 p0 c0 {1,S} {24,S} {25,S} {26,S}
7  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
8  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.20869,0.111441,-7.91347e-05,2.92406e-08,-4.43743e-12,-29944.7,44.9522], Tmin=(298,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[27.1374,0.0379005,-1.29437e-05,2.0076e-09,-1.16401e-13,-40795.8,-123.277], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/20/ 0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 128,
    label = "AC8H17",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {3,S} {6,S} {7,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {2,S} {18,S} {19,S} {20,S}
7  C u0 p0 c0 {2,S} {21,S} {22,S} {23,S}
8  C u1 p0 c0 {1,S} {24,S} {25,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.41945,0.106803,-7.65412e-05,2.85342e-08,-4.36479e-12,-5335.14,44.5472], Tmin=(298,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[26.707,0.0357661,-1.22179e-05,1.89537e-09,-1.09908e-13,-15723,-117.001], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/20/ 0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 129,
    label = "BC8H17",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {6,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {2,S} {22,S} {23,S} {24,S}
8  C u1 p0 c0 {1,S} {2,S} {25,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.09104,0.102319,-6.84859e-05,2.30184e-08,-3.07013e-12,-6628.29,43.1174], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[26.4569,0.0355421,-1.20521e-05,1.86089e-09,-1.07572e-13,-17039.3,-116.246], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/20/ 0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 130,
    label = "CC8H17",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {8,S} {20,S} {21,S} {22,S}
7  C u0 p0 c0 {8,S} {23,S} {24,S} {25,S}
8  C u1 p0 c0 {2,S} {6,S} {7,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.097316,0.0892654,-5.12874e-05,1.37641e-08,-1.27788e-12,-8811.47,28.9792], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[25.1497,0.0371097,-1.26854e-05,1.96873e-09,-1.14194e-13,-18276.2,-109.057], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/20/ 0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 131,
    label = "DC8H17",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {1,S} {18,S} {19,S} {20,S}
7  C u0 p0 c0 {2,S} {21,S} {22,S} {23,S}
8  C u1 p0 c0 {2,S} {24,S} {25,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.41945,0.106803,-7.65412e-05,2.85342e-08,-4.36479e-12,-5737.76,43.45], Tmin=(298,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[26.707,0.0357661,-1.22179e-05,1.89537e-09,-1.09908e-13,-16125.6,-118.098], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/20/ 0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 132,
    label = "JC8H16",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {7,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {7,S} {20,S} {21,S} {22,S}
7  C u0 p0 c0 {2,S} {6,S} {8,D}
8  C u0 p0 c0 {7,D} {23,S} {24,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.31862,0.104315,-7.64763e-05,2.92169e-08,-4.56914e-12,-16544.8,41.4548], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[26.0102,0.0339703,-1.15422e-05,1.78423e-09,-1.03212e-13,-26517.5,-115.359], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/20/ 0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 133,
    label = "IC8H15",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {2,S} {5,S} {8,D}
7  C u1 p0 c0 {1,S} {20,S} {21,S}
8  C u0 p0 c0 {6,D} {22,S} {23,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.74988,0.105476,-8.12782e-05,3.26272e-08,-5.33784e-12,1922.5,43.1416], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[26.0931,0.031763,-1.078e-05,1.66534e-09,-9.62986e-14,-8003.12,-115.651], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/20/ 0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 134,
    label = "AC8H17O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {9,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {1,S} {18,S} {19,S} {20,S}
7  C u0 p0 c0 {2,S} {21,S} {22,S} {23,S}
8  C u0 p0 c0 {2,S} {24,S} {25,S} {26,S}
9  O u0 p2 c0 {4,S} {27,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 O u1 p2 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.78614,0.114755,-8.50605e-05,3.34041e-08,-5.45173e-12,-23774.2,40.0276], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[30.2816,0.0378729,-1.30468e-05,2.03524e-09,-1.18471e-13,-34803.2,-131.647], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/20/ 0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 135,
    label = "BC8H17O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {9,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {1,S} {18,S} {19,S} {20,S}
7  C u0 p0 c0 {2,S} {21,S} {22,S} {23,S}
8  C u0 p0 c0 {2,S} {24,S} {25,S} {26,S}
9  O u0 p2 c0 {3,S} {27,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 O u1 p2 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.07002,0.12264,-9.72203e-05,4.09128e-08,-7.09103e-12,-26401.4,44.0346], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[30.9352,0.0374103,-1.29071e-05,2.01545e-09,-1.17399e-13,-37745.8,-136.731], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/20/ 0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 136,
    label = "AC8H16OOH-B",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {3,S} {6,S} {7,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {9,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {2,S} {22,S} {23,S} {24,S}
8  C u1 p0 c0 {1,S} {25,S} {26,S}
9  O u0 p2 c0 {4,S} {10,S}
10 O u0 p2 c0 {9,S} {27,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.06913,0.116142,-8.44027e-05,3.10689e-08,-4.5988e-12,-17638.3,44.0293], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[32.5511,0.0347987,-1.18445e-05,1.83416e-09,-1.06263e-13,-29512,-141.568], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/20/ 0 THRM""",
    longDesc = 
u"""

""",
)

entry(
    index = 137,
    label = "BC8H16OOH-A",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {3,S} {6,S} {7,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {9,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {2,S} {22,S} {23,S} {24,S}
8  C u1 p0 c0 {1,S} {25,S} {26,S}
9  O u0 p2 c0 {3,S} {10,S}
10 O u0 p2 c0 {9,S} {27,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.22208,0.126636,-0.000102427,4.32558e-08,-7.4499e-12,-18641.1,47.3182], Tmin=(298,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[32.965,0.0354522,-1.22761e-05,1.92176e-09,-1.12144e-13,-30596.6,-144.76], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/20/ 0 THRM""",
    longDesc = 
u"""

""",
)

entry(
    index = 138,
    label = "IC8ETERAB",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {6,S}
2  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
3  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
5  C u0 p0 c0 {1,S} {2,S} {13,S} {14,S}
6  C u0 p0 c0 {1,S} {2,S} {15,S} {16,S}
7  C u0 p0 c0 {2,S} {17,S} {18,S} {19,S}
8  C u0 p0 c0 {3,S} {20,S} {21,S} {22,S}
9  C u0 p0 c0 {3,S} {23,S} {24,S} {25,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {9,S}
25 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-7.80049,0.123581,-9.58622e-05,3.83545e-08,-6.21761e-12,-28819.8,63.44], Tmin=(298,'K'), Tmax=(1403,'K')),
            NASAPolynomial(coeffs=[27.6798,0.0359323,-1.23073e-05,1.91269e-09,-1.11054e-13,-40591.2,-125.296], Tmin=(1403,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""8/11/98 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 139,
    label = "AC8H16OOH-BO2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {12,S}
3  C u0 p0 c0 {1,S} {2,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {9,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {10,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {2,S} {22,S} {23,S} {24,S}
8  C u0 p0 c0 {2,S} {25,S} {26,S} {27,S}
9  O u0 p2 c0 {4,S} {11,S}
10 O u0 p2 c0 {5,S} {28,S}
11 O u0 p2 c0 {9,S} {29,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 O u1 p2 c0 {10,S}
29 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.29317,0.132763,-0.000107404,4.54645e-08,-7.86977e-12,-36710.9,41.5232], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[36.8372,0.0370742,-1.28898e-05,2.0233e-09,-1.18291e-13,-49384.6,-161.072], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/20/ 0 TM""",
    longDesc = 
u"""

""",
)

entry(
    index = 140,
    label = "BC8H16OOH-AO2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {12,S}
3  C u0 p0 c0 {1,S} {2,S} {9,S} {13,S}
4  C u0 p0 c0 {1,S} {10,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {2,S} {22,S} {23,S} {24,S}
8  C u0 p0 c0 {2,S} {25,S} {26,S} {27,S}
9  O u0 p2 c0 {3,S} {11,S}
10 O u0 p2 c0 {4,S} {28,S}
11 O u0 p2 c0 {9,S} {29,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 O u1 p2 c0 {10,S}
29 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.29317,0.132763,-0.000107404,4.54645e-08,-7.86977e-12,-36710.9,41.5232], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[36.8372,0.0370742,-1.28898e-05,2.0233e-09,-1.18291e-13,-49384.6,-161.072], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/20/ 0 TM""",
    longDesc = 
u"""

""",
)

entry(
    index = 141,
    label = "IC8KETAB",
    molecule = 
"""
multiplicity 3
1  O u0 p2 c0 {3,S} {7,S}
2  O u1 p2 c0 {8,S}
3  O u1 p2 c0 {1,S}
4  C u0 p0 c0 {6,S} {7,S} {8,S} {9,S}
5  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
6  C u0 p0 c0 {4,S} {5,S} {13,S} {14,S}
7  C u0 p0 c0 {1,S} {4,S} {15,S} {16,S}
8  C u0 p0 c0 {2,S} {4,S} {17,S} {18,S}
9  C u0 p0 c0 {4,S} {19,S} {20,S} {21,S}
10 C u0 p0 c0 {5,S} {22,S} {23,S} {24,S}
11 C u0 p0 c0 {5,S} {25,S} {26,S} {27,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {10,S}
24 H u0 p0 c0 {10,S}
25 H u0 p0 c0 {11,S}
26 H u0 p0 c0 {11,S}
27 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.37787,0.124999,-9.81048e-05,3.95573e-08,-6.48097e-12,-53325.5,44.6667], Tmin=(298,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[34.7134,0.0341945,-1.18953e-05,1.86805e-09,-1.09256e-13,-65774.6,-153.036], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/20/ 0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 142,
    label = "IC8KETBA",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {6,S}
2  O u0 p2 c0 {1,S} {27,S}
3  O u0 p2 c0 {11,D}
4  C u0 p0 c0 {6,S} {7,S} {8,S} {11,S}
5  C u0 p0 c0 {9,S} {10,S} {11,S} {12,S}
6  C u0 p0 c0 {1,S} {4,S} {13,S} {14,S}
7  C u0 p0 c0 {4,S} {15,S} {16,S} {17,S}
8  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
9  C u0 p0 c0 {5,S} {21,S} {22,S} {23,S}
10 C u0 p0 c0 {5,S} {24,S} {25,S} {26,S}
11 C u0 p0 c0 {3,D} {4,S} {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {10,S}
25 H u0 p0 c0 {10,S}
26 H u0 p0 c0 {10,S}
27 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.65723,0.12716,-0.000100733,4.13368e-08,-6.92387e-12,-53221.5,51.3887], Tmin=(298,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[33.688,0.0351531,-1.2245e-05,1.92459e-09,-1.12626e-13,-65750.1,-147.55], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""7/20/ 0 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 143,
    label = "IC3H7COC3H6-T",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {8,S}
3  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
4  C u0 p0 c0 {1,S} {18,S} {19,S} {20,S}
5  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
6  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
7  C u1 p0 c0 {1,S} {21,D}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.660479,0.083843,-5.79349e-05,2.10237e-08,-3.1896e-12,-22131.8,32.2077], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[23.0232,0.0297794,-1.02937e-05,1.60942e-09,-9.38331e-14,-30566.9,-95.5768], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""3/4/96 TRM""",
    longDesc = 
u"""

""",
)

entry(
    index = 144,
    label = "NC4H3",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {5,S}
2 C u0 p0 c0 {1,S} {4,T}
3 C u1 p0 c0 {1,D} {6,S}
4 C u0 p0 c0 {2,T} {7,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.39888,0.0325281,-3.44239e-05,1.99648e-08,-4.82595e-12,63906.8,17.8182], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.13818,0.00848296,-2.27319e-06,3.05662e-10,-1.67391e-14,62426.1,-15.4147], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 145,
    label = "C6H5CH3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {5,B} {11,S}
4  C u0 p0 c0 {2,B} {7,B} {15,S}
5  C u0 p0 c0 {3,B} {6,B} {12,S}
6  C u0 p0 c0 {5,B} {7,B} {13,S}
7  C u0 p0 c0 {4,B} {6,B} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.08982,0.0686477,-4.74717e-05,1.67001e-08,-2.39578e-12,4499.38,43.4583], Tmin=(298,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[16.3092,0.0225332,-7.84282e-06,1.23201e-09,-7.20675e-14,-2758.04,-66.676], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/19/93 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 146,
    label = "C6H5CH2J",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {7,S}
2  C u0 p0 c0 {1,B} {4,B} {8,S}
3  C u0 p0 c0 {1,B} {6,B} {12,S}
4  C u0 p0 c0 {2,B} {5,B} {9,S}
5  C u0 p0 c0 {4,B} {6,B} {10,S}
6  C u0 p0 c0 {3,B} {5,B} {11,S}
7  C u1 p0 c0 {1,S} {13,S} {14,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.481115,0.0385128,3.28615e-05,-7.69727e-08,3.54231e-11,23307,23.5488], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.044,0.0234939,-8.53754e-06,1.38908e-09,-8.36144e-14,18564.2,-51.6656], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T08/90""",
    longDesc = 
u"""

""",
)

entry(
    index = 147,
    label = "OC6H4CH3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {7,B} {15,S}
4  C u0 p0 c0 {2,B} {5,B} {12,S}
5  C u0 p0 c0 {4,B} {6,B} {11,S}
6  C u0 p0 c0 {5,B} {7,B} {13,S}
7  C u0 p0 c0 {3,B} {6,B} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 O u1 p2 c0 {5,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.03964,0.0739909,-5.15945e-05,1.20373e-08,1.4321e-12,225.708,45.3169], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.32623,0.0370921,-1.3737e-05,2.32847e-09,-1.49702e-13,-1566.36,-4.68621], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""THERGAS""",
    longDesc = 
u"""

""",
)

entry(
    index = 148,
    label = "HOC6H4CH3",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {16,S}
2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {4,B} {5,B}
4  C u0 p0 c0 {1,S} {3,B} {6,B}
5  C u0 p0 c0 {3,B} {7,B} {12,S}
6  C u0 p0 c0 {4,B} {8,B} {15,S}
7  C u0 p0 c0 {5,B} {8,B} {13,S}
8  C u0 p0 c0 {6,B} {7,B} {14,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.8386,0.07713,-5.33551e-05,1.2949e-08,1.09766e-12,-17273.9,43.5757], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.93692,0.0457992,-1.89178e-05,3.46244e-09,-2.34982e-13,-18225,7.47181], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""THERGAS""",
    longDesc = 
u"""

""",
)

entry(
    index = 149,
    label = "OC6H4O",
    molecule = 
"""
1  O u0 p2 c0 {3,D}
2  O u0 p2 c0 {8,D}
3  C u0 p0 c0 {1,D} {4,S} {8,S}
4  C u0 p0 c0 {3,S} {5,D} {9,S}
5  C u0 p0 c0 {4,D} {6,S} {10,S}
6  C u0 p0 c0 {5,S} {7,D} {11,S}
7  C u0 p0 c0 {6,D} {8,S} {12,S}
8  C u0 p0 c0 {2,D} {3,S} {7,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.40668,0.069641,-5.94147e-05,2.51064e-08,-4.21954e-12,-16635,38.6279], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[18.9273,0.0134964,-4.81966e-06,7.7024e-10,-4.56004e-14,-23934.4,-79.8144], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""4/ 1/94 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 150,
    label = "RODC6JDO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {5,D}
2  O u0 p2 c0 {8,D}
3  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
4  C u1 p0 c0 {3,S} {6,S} {10,S}
5  C u0 p0 c0 {1,D} {3,S} {7,S}
6  C u0 p0 c0 {4,S} {7,D} {11,S}
7  C u0 p0 c0 {5,S} {6,D} {12,S}
8  C u0 p0 c0 {2,D} {3,S} {13,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.337183,0.0611552,-5.11124e-05,2.19527e-08,-3.78092e-12,6.99212,22.5447], Tmin=(298,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[17.8078,0.0157342,-5.31173e-06,8.1782e-10,-4.71852e-14,-5549.92,-69.566], Tmin=(1400,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""4/26/ 0HADAD""",
    longDesc = 
u"""

""",
)

entry(
    index = 151,
    label = "C6H5OH",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {13,S}
2  C u0 p0 c0 {1,S} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {5,B} {8,S}
4  C u0 p0 c0 {2,B} {7,B} {12,S}
5  C u0 p0 c0 {3,B} {6,B} {9,S}
6  C u0 p0 c0 {5,B} {7,B} {10,S}
7  C u0 p0 c0 {4,B} {6,B} {11,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.48631,0.0722846,-6.19804e-05,2.67795e-08,-4.60013e-12,-12601.3,44.3728], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[17.1525,0.0160439,-5.46326e-06,8.46545e-10,-4.9076e-14,-19463.3,-69.6842], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/ 2/91 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 152,
    label = "CYPDONE",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {6,S}
3  C u0 p0 c0 {2,S} {4,D} {7,S}
4  C u0 p0 c0 {3,D} {5,S} {8,S}
5  C u0 p0 c0 {4,S} {6,D} {9,S}
6  C u0 p0 c0 {2,S} {5,D} {10,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.15439,0.0611975,-5.52982e-05,2.4974e-08,-4.46439e-12,2684.11,41.2432], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[14.3779,0.0119184,-4.19444e-06,6.63874e-10,-3.90411e-14,-3123.21,-56.1146], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""3/27/95 XIAN""",
    longDesc = 
u"""

""",
)

entry(
    index = 153,
    label = "C6H5CH2OJ",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {6,B} {14,S}
4  C u0 p0 c0 {2,B} {7,B} {15,S}
5  C u0 p0 c0 {6,B} {7,B} {11,S}
6  C u0 p0 c0 {3,B} {5,B} {12,S}
7  C u0 p0 c0 {4,B} {5,B} {13,S}
8  O u1 p2 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.77737,0.0751049,-5.68533e-05,2.1829e-08,-3.38134e-12,12623.4,51.0429], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[17.8843,0.0209012,-7.21833e-06,1.1284e-09,-6.57955e-14,4931.83,-70.1305], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""4/14/94 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 154,
    label = "C6H5CHO",
    molecule = 
"""
1  O u0 p2 c0 {8,D}
2  C u0 p0 c0 {3,B} {4,B} {8,S}
3  C u0 p0 c0 {2,B} {5,B} {9,S}
4  C u0 p0 c0 {2,B} {7,B} {13,S}
5  C u0 p0 c0 {3,B} {6,B} {10,S}
6  C u0 p0 c0 {5,B} {7,B} {11,S}
7  C u0 p0 c0 {4,B} {6,B} {12,S}
8  C u0 p0 c0 {1,D} {2,S} {14,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.70518,0.0646822,-4.57286e-05,1.60322e-08,-2.23734e-12,-6073.45,40.0414], Tmin=(298,'K'), Tmax=(1382,'K')),
            NASAPolynomial(coeffs=[17.5038,0.0187911,-6.51898e-06,1.02244e-09,-5.9763e-14,-13183.6,-68.8976], Tmin=(1382,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""2/25/94 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 155,
    label = "C6H6",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {7,S}
2  C u0 p0 c0 {1,B} {4,B} {8,S}
3  C u0 p0 c0 {1,B} {5,B} {9,S}
4  C u0 p0 c0 {2,B} {6,B} {10,S}
5  C u0 p0 c0 {3,B} {6,B} {11,S}
6  C u0 p0 c0 {4,B} {5,B} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.18689,0.0630511,-4.82875e-05,1.89015e-08,-3.01017e-12,9099.5,45.0745], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[13.8673,0.0174152,-6.08384e-06,9.58141e-10,-5.61503e-14,2599.89,-56.8525], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""5/2/91  THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 156,
    label = "C6H5OJ",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {7,S}
2  C u0 p0 c0 {3,B} {4,B} {8,S}
3  C u0 p0 c0 {2,B} {5,B} {9,S}
4  C u0 p0 c0 {2,B} {6,B} {10,S}
5  C u0 p0 c0 {3,B} {7,B} {11,S}
6  C u0 p0 c0 {4,B} {7,B} {12,S}
7  C u0 p0 c0 {1,S} {5,B} {6,B}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.56102,0.0698936,-6.18066e-05,2.76045e-08,-4.8941e-12,4836.71,45.507], Tmin=(298,'K'), Tmax=(1401,'K')),
            NASAPolynomial(coeffs=[15.9513,0.0152837,-5.26839e-06,8.22485e-10,-4.79123e-14,-1567.83,-62.2003], Tmin=(1401,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""4/26/ 0HADAD""",
    longDesc = 
u"""

""",
)

entry(
    index = 157,
    label = "FULVENE",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,D}
2  C u0 p0 c0 {1,S} {4,D} {7,S}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  C u0 p0 c0 {2,D} {5,S} {8,S}
5  C u0 p0 c0 {3,D} {4,S} {9,S}
6  C u0 p0 c0 {1,D} {11,S} {12,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.60963,0.0730648,-7.03269e-05,3.65804e-08,-8.02019e-12,27468.9,48.3392], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.50994,0.0338799,-1.77371e-05,4.47693e-09,-4.41274e-13,24921.9,-6.77575], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""98 MARINOVC&F""",
    longDesc = 
u"""

""",
)

entry(
    index = 158,
    label = "C14H14",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {5,B} {6,B}
4  C u0 p0 c0 {1,S} {7,B} {8,B}
5  C u0 p0 c0 {3,B} {9,B} {19,S}
6  C u0 p0 c0 {3,B} {11,B} {23,S}
7  C u0 p0 c0 {4,B} {12,B} {24,S}
8  C u0 p0 c0 {4,B} {14,B} {28,S}
9  C u0 p0 c0 {5,B} {10,B} {20,S}
10 C u0 p0 c0 {9,B} {11,B} {21,S}
11 C u0 p0 c0 {6,B} {10,B} {22,S}
12 C u0 p0 c0 {7,B} {13,B} {25,S}
13 C u0 p0 c0 {12,B} {14,B} {26,S}
14 C u0 p0 c0 {8,B} {13,B} {27,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {11,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {12,S}
26 H u0 p0 c0 {13,S}
27 H u0 p0 c0 {14,S}
28 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-8.14782,0.130621,-8.19368e-05,1.94757e-08,0,12614.2,71.8459], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[18.3725,0.0606471,-2.15506e-05,2.54284e-09,0,5185.16,-65.9251], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 159,
    label = "C6H5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {7,S}
2  C u0 p0 c0 {1,B} {4,B} {8,S}
3  C u0 p0 c0 {1,B} {5,B} {9,S}
4  C u0 p0 c0 {2,B} {6,B} {10,S}
5  C u0 p0 c0 {3,B} {6,B} {11,S}
6  C u1 p0 c0 {4,B} {5,B}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.210307,0.0204746,5.89743e-05,-1.01534e-07,4.47106e-11,39546.9,25.291], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.8445,0.0173212,-6.29233e-06,1.0237e-09,-6.16217e-14,35559.8,-35.3735], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""PHENYL RAD  T04/02""",
    longDesc = 
u"""

""",
)

entry(
    index = 160,
    label = "C6H4CH3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,B} {7,B}
3  C u0 p0 c0 {2,B} {4,B} {13,S}
4  C u0 p0 c0 {3,B} {5,B} {12,S}
5  C u0 p0 c0 {4,B} {6,B} {11,S}
6  C u0 p0 c0 {5,B} {7,B} {14,S}
7  C u1 p0 c0 {2,B} {6,B}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.53984,0.0611194,-3.16055e-05,1.04281e-09,2.86557e-12,34181.7,43.0769], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.5915,0.0224187,-7.13697e-06,1.08735e-09,-6.49369e-14,28819.5,-48.0783], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""THERGAS""",
    longDesc = 
u"""

""",
)

entry(
    index = 161,
    label = "C6H5CJO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {8,D}
2  C u0 p0 c0 {3,B} {4,B} {8,S}
3  C u0 p0 c0 {2,B} {5,B} {9,S}
4  C u0 p0 c0 {2,B} {7,B} {13,S}
5  C u0 p0 c0 {3,B} {6,B} {10,S}
6  C u0 p0 c0 {5,B} {7,B} {11,S}
7  C u0 p0 c0 {4,B} {6,B} {12,S}
8  C u1 p0 c0 {1,D} {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.93002,0.06188,-4.60917e-05,1.70134e-08,-2.4987e-12,11335.2,37.1779], Tmin=(298,'K'), Tmax=(1382,'K')),
            NASAPolynomial(coeffs=[17.7196,0.015999,-5.54532e-06,8.69583e-10,-5.08335e-14,4574.08,-68.2553], Tmin=(1382,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""2/25/94 THERM""",
    longDesc = 
u"""

""",
)

entry(
    index = 162,
    label = "RODC6J(C)DO",
    molecule = 
"""
multiplicity 4
1  O u0 p2 c0 {2,S} {8,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {6,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {5,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {4,S} {6,S} {7,D}
6  C u1 p0 c0 {3,S} {5,S} {15,S}
7  C u0 p0 c0 {5,D} {8,S} {16,S}
8  C u0 p0 c0 {1,S} {7,S} {9,D}
9  C u1 p0 c0 {3,S} {8,D}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-6.06739,0.0892808,-7.08112e-05,2.37918e-08,-1.50768e-12,-9402.73,57.1452], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.85605,0.0392559,-1.47595e-05,2.52937e-09,-1.63917e-13,-11950.8,-10.2841], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 163,
    label = "OCCXCCXCJC",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {5,S} {14,S}
2  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {7,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {6,D} {12,S}
5  C u0 p0 c0 {1,S} {6,S} {7,D}
6  C u0 p0 c0 {4,D} {5,S} {13,S}
7  C u1 p0 c0 {3,S} {5,D}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.296032,0.0558238,-3.63319e-05,1.32264e-08,-1.97858e-12,20733.7,31.0297], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.0497,0.0387919,-1.53207e-05,2.71713e-09,-1.80337e-13,19759.8,7.77228], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 164,
    label = "iso001",
    molecule = 
"""
multiplicity 3
1  O u0 p2 c0 {3,S} {4,S}
2  O u1 p2 c0 {6,S}
3  O u1 p2 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {9,S} {11,S}
5  C u0 p0 c0 {4,S} {6,S} {17,S} {18,S}
6  C u0 p0 c0 {2,S} {5,S} {7,S} {12,S}
7  C u0 p0 c0 {6,S} {8,S} {15,S} {16,S}
8  C u0 p0 c0 {7,S} {10,S} {13,S} {14,S}
9  C u0 p0 c0 {4,S} {22,S} {23,S} {24,S}
10 C u0 p0 c0 {8,S} {19,S} {20,S} {21,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.52937,0.0958173,-6.96689e-05,2.6954e-08,-4.38728e-12,-52384,29.3851], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[28.833,0.0320168,-1.11508e-05,1.75226e-09,-1.0252e-13,-62014.2,-117.5], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

