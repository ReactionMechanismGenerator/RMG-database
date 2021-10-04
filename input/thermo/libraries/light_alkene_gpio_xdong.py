#!/usr/bin/env python
# encoding: utf-8

name = "light_alkene_gpio_xdong"
shortDesc = ""
longDesc = """

"""
entry(
    index = 0,
    label = "CH3CHOOH",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {9,S}
3 C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4 C u1 p0 c0 {1,S} {3,S} {8,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.54939,0.0471047,-0.000179635,3.99519e-07,-3.12454e-10,355.612,10.7597], Tmin=(10,'K'), Tmax=(426.5,'K')),
            NASAPolynomial(coeffs=[3.27752,0.0248069,-1.38256e-05,3.74319e-09,-3.95373e-13,604.796,14.489], Tmin=(426.5,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1,
    label = "P-1OM",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {4,S} {5,S}
2  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
3  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
5  C u1 p0 c0 {1,S} {2,S} {14,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.5145,0.0495058,-0.000119337,2.7371e-07,-2.24513e-10,-9904.77,11.4189], Tmin=(10,'K'), Tmax=(437.22,'K')),
            NASAPolynomial(coeffs=[1.24263,0.0463978,-2.67038e-05,7.47672e-09,-8.15454e-13,-9477.74,23.1114], Tmin=(437.22,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2,
    label = "B-1OM",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {6,S} {14,S} {15,S} {16,S}
5  C u1 p0 c0 {2,S} {6,S} {17,S}
6  O u0 p2 c0 {4,S} {5,S}
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
17 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.20578,0.082364,-0.000268195,6.03217e-07,-4.80824e-10,-13020.9,11.3134], Tmin=(10,'K'), Tmax=(427.59,'K')),
            NASAPolynomial(coeffs=[1.54022,0.0565346,-3.23196e-05,8.97402e-09,-9.70493e-13,-12499.9,22.3603], Tmin=(427.59,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 3,
    label = "iB-1OM",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {6,S} {14,S} {15,S} {16,S}
5  C u1 p0 c0 {1,S} {6,S} {17,S}
6  O u0 p2 c0 {4,S} {5,S}
7  H u0 p0 c0 {1,S}
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
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.56708,0.0503013,-2.47502e-05,4.87278e-09,-1.48089e-13,-13800.4,12.7234], Tmin=(10,'K'), Tmax=(1674.75,'K')),
            NASAPolynomial(coeffs=[20.6341,0.0188327,-4.88983e-06,2.80804e-10,4.27124e-14,-20820.5,-82.3077], Tmin=(1674.75,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 4,
    label = "iC3H7CHO",
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
            NASAPolynomial(coeffs=[2.16541,0.0328744,3.99612e-06,-2.09258e-08,8.19758e-12,-28056.3,15.6204], Tmin=(100,'K'), Tmax=(1100.75,'K')),
            NASAPolynomial(coeffs=[8.13887,0.0277302,-1.15638e-05,2.16743e-09,-1.5183e-13,-30374.8,-18.3293], Tmin=(1100.75,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 5,
    label = "[CH2]C[CH]C",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {2,S} {10,S}
4  C u1 p0 c0 {1,S} {11,S} {12,S}
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
            NASAPolynomial(coeffs=[3.43997,0.0631833,-0.000308048,7.97053e-07,-6.83185e-10,30850.8,12.672], Tmin=(10,'K'), Tmax=(408.12,'K')),
            NASAPolynomial(coeffs=[0.432032,0.0388923,-2.11343e-05,5.5345e-09,-5.63356e-13,31544.2,29.9742], Tmin=(408.12,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 6,
    label = "C=[C]CC",
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
            NASAPolynomial(coeffs=[3.83157,0.020524,8.0342e-06,-1.62748e-08,5.44753e-12,26052.3,10.0366], Tmin=(10,'K'), Tmax=(1159.29,'K')),
            NASAPolynomial(coeffs=[4.85119,0.0267954,-1.2747e-05,2.95992e-09,-2.71257e-13,25158.1,2.12956], Tmin=(1159.29,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 7,
    label = "[CH2]C([CH2])C",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u1 p0 c0 {1,S} {9,S} {10,S}
4  C u1 p0 c0 {1,S} {11,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71938,0.0231939,2.33132e-05,-5.67539e-08,3.26272e-11,31739.8,12.5302], Tmin=(10,'K'), Tmax=(469.39,'K')),
            NASAPolynomial(coeffs=[2.10634,0.0369399,-2.0615e-05,5.63768e-09,-6.03575e-13,31891.2,19.0921], Tmin=(469.39,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 8,
    label = "[CH]=C(C)C",
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
            NASAPolynomial(coeffs=[3.89993,0.00834953,0.000124504,-3.77885e-07,3.89e-10,26364.2,9.47997], Tmin=(10,'K'), Tmax=(245.13,'K')),
            NASAPolynomial(coeffs=[2.49417,0.0312891,-1.58712e-05,3.89392e-09,-3.72979e-13,26433.1,14.2855], Tmin=(245.13,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 9,
    label = "[CH2]C(CC)O[O]",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {2,S} {12,S} {13,S}
5  O u0 p2 c0 {2,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.23214,0.0753244,-0.000209123,3.90487e-07,-2.74167e-10,12238.6,12.846], Tmin=(10,'K'), Tmax=(453.46,'K')),
            NASAPolynomial(coeffs=[4.31354,0.0426765,-2.46863e-05,6.95311e-09,-7.62966e-13,12378.2,11.1039], Tmin=(453.46,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 10,
    label = "CC[CH]CO[O]",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4  C u1 p0 c0 {1,S} {2,S} {13,S}
5  O u0 p2 c0 {2,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.12002,0.0932974,-0.00038396,8.74072e-07,-6.98289e-10,12512.8,13.5203], Tmin=(10,'K'), Tmax=(414.83,'K')),
            NASAPolynomial(coeffs=[3.05806,0.0439492,-2.49214e-05,6.82966e-09,-7.27717e-13,12947.7,18.9445], Tmin=(414.83,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 11,
    label = "C[CH]C(C)O[O]",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {3,S} {13,S}
5  O u0 p2 c0 {1,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.29195,0.0640322,-0.000125628,1.83791e-07,-1.07749e-10,10071.8,13.495], Tmin=(10,'K'), Tmax=(525.15,'K')),
            NASAPolynomial(coeffs=[4.54199,0.0413888,-2.34707e-05,6.5246e-09,-7.09929e-13,10121.5,9.99219], Tmin=(525.15,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 12,
    label = "[CH2]C(C)(C)O[O]",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {1,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {14,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.6952,0.0289386,0.000250151,-1.16274e-06,1.52667e-09,9826.46,11.8783], Tmin=(10,'K'), Tmax=(272.87,'K')),
            NASAPolynomial(coeffs=[5.32256,0.0420821,-2.54927e-05,7.62871e-09,-8.89849e-13,9599.91,3.61676], Tmin=(272.87,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 13,
    label = "C[C](C)CO[O]",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {2,S} {3,S}
5  O u0 p2 c0 {1,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.2848,0.0768194,-0.000306388,7.34493e-07,-6.09393e-10,10128,13.281], Tmin=(10,'K'), Tmax=(410.83,'K')),
            NASAPolynomial(coeffs=[1.69413,0.0462341,-2.64982e-05,7.33502e-09,-7.88733e-13,10647.5,24.272], Tmin=(410.83,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 14,
    label = "CC#CC",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,T}
4  C u0 p0 c0 {2,S} {3,T}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67192,0.033081,-8.82861e-05,2.01652e-07,-1.57363e-10,15533.1,7.46601], Tmin=(10,'K'), Tmax=(465.87,'K')),
            NASAPolynomial(coeffs=[1.43402,0.0316276,-1.70608e-05,4.50099e-09,-4.66034e-13,15965.9,18.9604], Tmin=(465.87,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 15,
    label = "CC=C(C)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {4,D} {5,S}
4  C u0 p0 c0 {2,S} {3,D} {12,S}
5  O u0 p2 c0 {3,S} {13,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {4,S}
13 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76368,0.0232966,0.000118861,-4.17237e-07,4.58174e-10,784.584,11.062], Tmin=(10,'K'), Tmax=(232.06,'K')),
            NASAPolynomial(coeffs=[2.43195,0.0462519,-2.95195e-05,9.03882e-09,-1.06102e-12,846.392,15.5415], Tmin=(232.06,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 16,
    label = "CC1(C)COO1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {2,S} {5,S}
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
            NASAPolynomial(coeffs=[3.7699,0.0199181,8.69081e-05,-1.91396e-07,1.27283e-10,-13240.6,10.9798], Tmin=(10,'K'), Tmax=(390.18,'K')),
            NASAPolynomial(coeffs=[0.796775,0.0503975,-3.02658e-05,8.80774e-09,-9.92768e-13,-13008.5,22.5253], Tmin=(390.18,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 17,
    label = "CC1(C)CO1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93436,0.00478776,0.000156151,-3.63426e-07,2.82759e-10,-19254.4,9.25702], Tmin=(10,'K'), Tmax=(326.76,'K')),
            NASAPolynomial(coeffs=[0.702188,0.0443552,-2.54899e-05,7.17418e-09,-7.90555e-13,-19043.1,21.235], Tmin=(326.76,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 18,
    label = "CC=C(C)[O]",
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
            NASAPolynomial(coeffs=[3.68762,0.0335877,-8.08275e-05,2.33821e-07,-2.17991e-10,-11631.9,11.073], Tmin=(10,'K'), Tmax=(418.74,'K')),
            NASAPolynomial(coeffs=[0.319,0.0417708,-2.41838e-05,6.78868e-09,-7.40957e-13,-11139.4,26.9042], Tmin=(418.74,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 19,
    label = "[CH2]C(=CC)O[O]",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {3,S} {9,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  C u0 p0 c0 {3,D} {10,S} {11,S}
5  O u0 p2 c0 {3,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82939,0.017826,0.000177585,-7.06894e-07,9.27903e-10,19807.9,11.6763], Tmin=(10,'K'), Tmax=(192.73,'K')),
            NASAPolynomial(coeffs=[2.54773,0.044427,-2.94529e-05,9.2862e-09,-1.11535e-12,19857.3,15.7493], Tmin=(192.73,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 20,
    label = "[CH2]C(C)(C)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {2,S}
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
            NASAPolynomial(coeffs=[3.17808,0.0641795,-7.58744e-05,5.88479e-08,-1.99649e-11,-6987.36,11.5407], Tmin=(10,'K'), Tmax=(759.59,'K')),
            NASAPolynomial(coeffs=[6.94905,0.0408331,-2.28822e-05,6.29231e-09,-6.77544e-13,-7459.6,-4.95268], Tmin=(759.59,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 21,
    label = "CC(C)(C)O[O]",
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
            NASAPolynomial(coeffs=[3.81089,0.0161228,0.0002578,-8.94558e-07,9.57655e-10,-16097,10.8537], Tmin=(10,'K'), Tmax=(311.52,'K')),
            NASAPolynomial(coeffs=[3.60885,0.0470469,-2.7514e-05,7.95403e-09,-9.02501e-13,-16221.9,9.38641], Tmin=(311.52,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 22,
    label = "C[C]C",
    molecule = 
"""
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3 C u0 p1 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71711,0.0334256,-0.00017226,4.82625e-07,-4.27445e-10,34893.7,8.48269], Tmin=(10,'K'), Tmax=(411.31,'K')),
            NASAPolynomial(coeffs=[0.364891,0.0281577,-1.49499e-05,3.82238e-09,-3.79862e-13,35489.8,25.571], Tmin=(411.31,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 23,
    label = "CC1CC1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
4  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05076,-0.00441547,0.000127918,-2.01586e-07,1.03448e-10,1021.06,8.30374], Tmin=(10,'K'), Tmax=(572.48,'K')),
            NASAPolynomial(coeffs=[-1.55373,0.0445149,-2.58901e-05,7.3422e-09,-8.10287e-13,1502.64,30.8177], Tmin=(572.48,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 24,
    label = "[CH2]C1(CC)OO1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {1,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {1,S} {5,S}
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
            NASAPolynomial(coeffs=[3.91736,0.0107038,0.000445123,-2.87395e-06,6.57192e-09,5893.87,9.76436], Tmin=(10,'K'), Tmax=(109.65,'K')),
            NASAPolynomial(coeffs=[2.96719,0.0453655,-2.90454e-05,8.96573e-09,-1.0627e-12,5914.71,12.2481], Tmin=(109.65,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 25,
    label = "[CH2]C(C)CC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u1 p0 c0 {1,S} {15,S} {16,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
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
            NASAPolynomial(coeffs=[3.64694,0.0378466,-1.68245e-06,-1.33208e-08,4.94869e-12,3790.12,12.6658], Tmin=(10,'K'), Tmax=(1218.7,'K')),
            NASAPolynomial(coeffs=[7.26597,0.0385727,-1.80899e-05,4.14118e-09,-3.7431e-13,1972.01,-9.35001], Tmin=(1218.7,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 26,
    label = "CC[CH]CC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  C u1 p0 c0 {1,S} {2,S} {16,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.3348,0.0715678,-0.000274621,6.73535e-07,-5.55051e-10,3039.53,11.9506], Tmin=(10,'K'), Tmax=(428.35,'K')),
            NASAPolynomial(coeffs=[-0.315142,0.0535695,-2.92119e-05,7.73663e-09,-8.00324e-13,3830.03,32.0423], Tmin=(428.35,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 27,
    label = "[CH2]C[CH2]",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {8,S} {9,S}
3 C u1 p0 c0 {1,S} {6,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80366,0.0204295,-4.02282e-05,1.13677e-07,-1.02036e-10,35293,10.7897], Tmin=(10,'K'), Tmax=(447.71,'K')),
            NASAPolynomial(coeffs=[1.38506,0.0275188,-1.53354e-05,4.17556e-09,-4.4475e-13,35655.1,22.1396], Tmin=(447.71,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 28,
    label = "C[CH]C(C)C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
5  C u1 p0 c0 {1,S} {4,S} {16,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.56965,0.0400372,-3.04569e-05,6.19979e-08,-5.34667e-11,2253.62,12.9105], Tmin=(10,'K'), Tmax=(508.14,'K')),
            NASAPolynomial(coeffs=[0.112322,0.0535493,-2.98914e-05,8.18264e-09,-8.78047e-13,2781.89,28.9903], Tmin=(508.14,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 29,
    label = "CC[C](C)C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
5  C u1 p0 c0 {1,S} {3,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
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
            NASAPolynomial(coeffs=[3.43394,0.0635584,-0.000266453,7.15874e-07,-6.22385e-10,1267.97,15.1582], Tmin=(10,'K'), Tmax=(417.99,'K')),
            NASAPolynomial(coeffs=[-1.79488,0.0556948,-3.04488e-05,8.06299e-09,-8.3251e-13,2210.91,41.8738], Tmin=(417.99,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 30,
    label = "CCC(C)(C)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
6  O u0 p2 c0 {1,S} {18,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 O u1 p2 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73937,0.028776,0.000478029,-2.71244e-06,4.68735e-09,-19008.6,12.4472], Tmin=(10,'K'), Tmax=(199.04,'K')),
            NASAPolynomial(coeffs=[4.3525,0.0565056,-3.27744e-05,9.36876e-09,-1.04869e-12,-19112.4,8.48594], Tmin=(199.04,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 31,
    label = "C=CCCC=C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,D} {11,S}
4  C u0 p0 c0 {2,S} {6,D} {12,S}
5  C u0 p0 c0 {3,D} {13,S} {14,S}
6  C u0 p0 c0 {4,D} {15,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.38515,0.0639663,-0.000180063,4.26794e-07,-3.55771e-10,7891.25,12.0095], Tmin=(10,'K'), Tmax=(425.53,'K')),
            NASAPolynomial(coeffs=[0.675345,0.0557325,-3.22258e-05,9.04447e-09,-9.87484e-13,8427.05,26.3532], Tmin=(425.53,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 32,
    label = "C[C](C)C[O]",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {2,S} {3,S}
5  O u1 p2 c0 {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.43661,0.0647279,-0.000317877,8.66261e-07,-7.7381e-10,12492.3,13.8099], Tmin=(10,'K'), Tmax=(397.21,'K')),
            NASAPolynomial(coeffs=[-0.446334,0.0456076,-2.5801e-05,7.01472e-09,-7.39442e-13,13260.1,34.7394], Tmin=(397.21,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 33,
    label = "[CH2]O[O]",
    molecule = 
"""
multiplicity 3
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 O u1 p2 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93096,0.00558577,5.03237e-05,-1.65033e-07,1.56729e-10,26366.9,7.85935], Tmin=(10,'K'), Tmax=(365.96,'K')),
            NASAPolynomial(coeffs=[4.18118,0.011229,-7.14781e-06,2.22189e-09,-2.6597e-13,26292.4,6.1372], Tmin=(365.96,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 34,
    label = "CC(C)=CO[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {5,S} {12,S}
5  O u0 p2 c0 {4,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.60852,0.0336454,1.17111e-05,-4.50777e-08,2.37121e-11,1696.67,11.2474], Tmin=(10,'K'), Tmax=(722.39,'K')),
            NASAPolynomial(coeffs=[3.99861,0.0412516,-2.43616e-05,6.92705e-09,-7.62001e-13,1385.49,7.72855], Tmin=(722.39,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 35,
    label = "CC(=C)CO[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.43113,0.0589608,-0.000176393,3.99047e-07,-3.25896e-10,3446.5,13.1971], Tmin=(10,'K'), Tmax=(417.14,'K')),
            NASAPolynomial(coeffs=[2.33656,0.0432369,-2.55663e-05,7.30997e-09,-8.103e-13,3765.94,20.2551], Tmin=(417.14,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 36,
    label = "C[CH]C(C)[O]",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {3,S} {13,S}
5  O u1 p2 c0 {1,S}
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
            NASAPolynomial(coeffs=[3.50095,0.0489533,-0.000113476,2.31293e-07,-1.73431e-10,12704.3,13.2546], Tmin=(10,'K'), Tmax=(463.57,'K')),
            NASAPolynomial(coeffs=[1.96412,0.0416919,-2.35743e-05,6.50383e-09,-7.0112e-13,13067.3,21.8657], Tmin=(463.57,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 37,
    label = "CC1OOC1C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {2,S} {5,S}
7  H u0 p0 c0 {1,S}
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
            NASAPolynomial(coeffs=[3.71961,0.0244711,4.61639e-05,-8.54602e-08,4.07928e-11,-13226.4,10.779], Tmin=(10,'K'), Tmax=(691.37,'K')),
            NASAPolynomial(coeffs=[1.43819,0.048133,-2.78729e-05,7.82014e-09,-8.52645e-13,-13161,19.1352], Tmin=(691.37,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 38,
    label = "CC1OC1C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {7,S}
3  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8067,0.0145041,7.75757e-05,-1.52383e-07,9.23961e-11,-19091.5,9.83286], Tmin=(10,'K'), Tmax=(426.78,'K')),
            NASAPolynomial(coeffs=[0.718386,0.0434489,-2.41545e-05,6.52529e-09,-6.88145e-13,-18827.9,22.1026], Tmin=(426.78,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 39,
    label = "C=CC(C)OO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {3,D} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68116,0.0276682,0.000260108,-1.08058e-06,1.25472e-09,-14419.7,10.9688], Tmin=(10,'K'), Tmax=(312.86,'K')),
            NASAPolynomial(coeffs=[6.47077,0.0393669,-2.30656e-05,6.71854e-09,-7.69894e-13,-14826,-2.95255], Tmin=(312.86,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 40,
    label = "C=CC(C)O[O]",
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
            NASAPolynomial(coeffs=[3.43119,0.0575789,-0.000151806,3.1969e-07,-2.50561e-10,3192.2,12.5357], Tmin=(10,'K'), Tmax=(428.28,'K')),
            NASAPolynomial(coeffs=[2.76882,0.0425985,-2.52051e-05,7.22318e-09,-8.02993e-13,3443.06,17.4359], Tmin=(428.28,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 41,
    label = "CCC(C)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.46472,0.0526947,-9.49948e-05,1.93953e-07,-1.53466e-10,-13353.3,13.0355], Tmin=(10,'K'), Tmax=(449.89,'K')),
            NASAPolynomial(coeffs=[1.60638,0.0511984,-2.99266e-05,8.50272e-09,-9.39563e-13,-13003.7,22.5432], Tmin=(449.89,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 42,
    label = "CCCCO[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {3,S} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
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
            NASAPolynomial(coeffs=[3.32408,0.0676577,-0.00019658,4.18099e-07,-3.18915e-10,-11033.8,12.7824], Tmin=(10,'K'), Tmax=(447.97,'K')),
            NASAPolynomial(coeffs=[1.78201,0.049391,-2.81443e-05,7.79059e-09,-8.40554e-13,-10574.2,22.5715], Tmin=(447.97,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 43,
    label = "[CH2]C(CC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.17035,0.0752536,-0.000154955,2.2333e-07,-1.28683e-10,-4741.15,12.4909], Tmin=(10,'K'), Tmax=(520.17,'K')),
            NASAPolynomial(coeffs=[5.5157,0.0437252,-2.51274e-05,7.06833e-09,-7.76657e-13,-4802.6,4.46349], Tmin=(520.17,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 44,
    label = "CC[CH]COO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {5,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {1,S} {2,S} {14,S}
5  O u0 p2 c0 {2,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.00653,0.106846,-0.00047082,1.10107e-06,-8.96415e-10,-4191.18,13.6333], Tmin=(10,'K'), Tmax=(408.24,'K')),
            NASAPolynomial(coeffs=[2.78951,0.0475033,-2.6922e-05,7.35463e-09,-7.80077e-13,-3661.23,20.7595], Tmin=(408.24,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 45,
    label = "C[C](C)COO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
4  C u1 p0 c0 {1,S} {2,S} {3,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.16173,0.0907072,-0.000385486,9.28544e-07,-7.72883e-10,-6568.13,15.714], Tmin=(10,'K'), Tmax=(406.61,'K')),
            NASAPolynomial(coeffs=[1.75005,0.0492218,-2.81715e-05,7.77768e-09,-8.3353e-13,-5995.59,26.8829], Tmin=(406.61,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 46,
    label = "CC(C)CO[O]",
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
            NASAPolynomial(coeffs=[3.67644,0.0353128,7.18452e-06,-2.44129e-08,9.20547e-12,-11929,12.1128], Tmin=(10,'K'), Tmax=(1070.41,'K')),
            NASAPolynomial(coeffs=[5.52053,0.0420677,-2.1404e-05,5.30243e-09,-5.16372e-13,-13105.5,-0.561068], Tmin=(1070.41,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 47,
    label = "C[CH]C(C)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {3,S} {14,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
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
            NASAPolynomial(coeffs=[3.20419,0.0804678,-0.000250684,5.15195e-07,-3.86983e-10,-6491.56,14.1385], Tmin=(10,'K'), Tmax=(435.81,'K')),
            NASAPolynomial(coeffs=[3.43101,0.0469442,-2.70793e-05,7.59083e-09,-8.28428e-13,-6212.74,16.6583], Tmin=(435.81,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 48,
    label = "C[CH]C(C)OOC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {5,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {7,S} {15,S} {16,S} {17,S}
5  C u1 p0 c0 {1,S} {3,S} {18,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {4,S} {6,S}
8  H u0 p0 c0 {1,S}
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
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.00408,0.0990049,-0.000297756,5.88398e-07,-4.25959e-10,-6467.73,14.6984], Tmin=(10,'K'), Tmax=(451.21,'K')),
            NASAPolynomial(coeffs=[3.38135,0.0574557,-3.26246e-05,9.01315e-09,-9.71836e-13,-6112.87,17.4882], Tmin=(451.21,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 49,
    label = "CC(C)C(C)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {8,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
6  O u0 p2 c0 {2,S} {18,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 O u1 p2 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.47994,0.0511505,-1.41097e-05,-7.10593e-09,3.65154e-12,-16887.5,13.1734], Tmin=(10,'K'), Tmax=(1230.91,'K')),
            NASAPolynomial(coeffs=[9.22827,0.0448075,-2.14138e-05,4.9923e-09,-4.59335e-13,-19237.2,-19.5497], Tmin=(1230.91,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 50,
    label = "[CH2]CC(C)OO",
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
            NASAPolynomial(coeffs=[3.31349,0.0692303,-0.000176126,3.59864e-07,-2.79937e-10,-5281.2,13.7743], Tmin=(10,'K'), Tmax=(422.69,'K')),
            NASAPolynomial(coeffs=[3.11982,0.0495382,-2.98579e-05,8.69222e-09,-9.78786e-13,-5072.54,16.8165], Tmin=(422.69,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 51,
    label = "C[CH]CCOO",
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
            NASAPolynomial(coeffs=[3.19118,0.0875971,-0.000363477,8.84724e-07,-7.45737e-10,-4533.26,15.0483], Tmin=(10,'K'), Tmax=(402.69,'K')),
            NASAPolynomial(coeffs=[1.66821,0.0503037,-2.92963e-05,8.21549e-09,-8.92661e-13,-3985.56,26.2879], Tmin=(402.69,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 52,
    label = "CC(O[O])C(C)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {8,S}
3  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {2,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
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
            NASAPolynomial(coeffs=[2.74618,0.0964535,-0.000159392,1.55343e-07,-6.05079e-11,-25478.3,15.2415], Tmin=(10,'K'), Tmax=(728.86,'K')),
            NASAPolynomial(coeffs=[9.55192,0.0453139,-2.57669e-05,7.16205e-09,-7.77971e-13,-26104.1,-12.9272], Tmin=(728.86,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 53,
    label = "[CH2]C1CC1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
4  C u1 p0 c0 {1,S} {10,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96654,0.00208434,0.000110011,-1.99494e-07,1.17357e-10,24506.2,8.59468], Tmin=(10,'K'), Tmax=(439.01,'K')),
            NASAPolynomial(coeffs=[-0.430112,0.0421434,-2.68597e-05,8.35075e-09,-1.00145e-12,24892.2,26.1866], Tmin=(439.01,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 54,
    label = "[CH2]C(C)COO",
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
            NASAPolynomial(coeffs=[3.2375,0.0681294,-0.000115336,1.48334e-07,-8.06463e-11,-4008.93,13.176], Tmin=(10,'K'), Tmax=(533.02,'K')),
            NASAPolynomial(coeffs=[5.24632,0.0447352,-2.60899e-05,7.42796e-09,-8.23824e-13,-4104.9,5.85711], Tmin=(533.02,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 55,
    label = "[CH2]C(=C)O[O]",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 C u1 p0 c0 {1,S} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {7,S} {8,S}
4 O u0 p2 c0 {1,S} {9,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 O u1 p2 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88852,0.0067921,0.000112861,-2.41842e-07,1.53031e-10,24166,10.4668], Tmin=(10,'K'), Tmax=(539.92,'K')),
            NASAPolynomial(coeffs=[4.00996,0.0303303,-2.0425e-05,6.56406e-09,-8.0453e-13,23796.7,6.65719], Tmin=(539.92,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 56,
    label = "[CH]C(C)=O",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {7,D}
3 C u2 p0 c0 {2,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {2,D}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.00589,-0.00141213,9.69364e-05,-1.67247e-07,8.94535e-11,23183.4,10.2943], Tmin=(10,'K'), Tmax=(606.95,'K')),
            NASAPolynomial(coeffs=[1.96826,0.0288197,-1.93054e-05,6.04566e-09,-7.13578e-13,23121.2,16.5577], Tmin=(606.95,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 57,
    label = "C=CC(C)=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,D}
3  C u0 p0 c0 {2,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {10,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {2,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68292,0.0352184,-0.000109029,3.22997e-07,-3.11557e-10,-15481.8,9.85788], Tmin=(10,'K'), Tmax=(391.46,'K')),
            NASAPolynomial(coeffs=[0.757395,0.038994,-2.34179e-05,6.76437e-09,-7.54854e-13,-15052.7,23.7841], Tmin=(391.46,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 58,
    label = "[CH2]C(=O)[CH]C",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u1 p0 c0 {1,S} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {9,D}
4  C u1 p0 c0 {3,S} {10,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71822,0.0286123,-1.00226e-06,-1.5152e-08,6.79096e-12,11059,10.5344], Tmin=(10,'K'), Tmax=(990.04,'K')),
            NASAPolynomial(coeffs=[5.76529,0.0294123,-1.59572e-05,4.17234e-09,-4.25511e-13,10209.1,-1.56617], Tmin=(990.04,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 59,
    label = "[CH2]CC(C)=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,D}
4  C u1 p0 c0 {1,S} {11,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.38234,0.0658864,-0.000267641,6.25718e-07,-5.04385e-10,-6139.67,12.6702], Tmin=(10,'K'), Tmax=(421.73,'K')),
            NASAPolynomial(coeffs=[2.09199,0.0372772,-2.05949e-05,5.51354e-09,-5.75476e-13,-5667.59,22.0879], Tmin=(421.73,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 60,
    label = "C=C([O])CC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,S} {10,D}
4  C u1 p0 c0 {3,S} {11,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.64687,0.0309332,-7.60966e-06,-5.52056e-09,2.71492e-12,-9004.87,10.8549], Tmin=(10,'K'), Tmax=(1143.74,'K')),
            NASAPolynomial(coeffs=[5.64444,0.0302839,-1.50688e-05,3.67139e-09,-3.53097e-13,-9876.29,-0.862495], Tmin=(1143.74,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 61,
    label = "C=C(O)[CH]C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {3,S} {9,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  C u0 p0 c0 {3,D} {10,S} {11,S}
5  O u0 p2 c0 {3,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85645,0.0104591,0.000169242,-4.58589e-07,3.78432e-10,-7473.06,10.8563], Tmin=(10,'K'), Tmax=(405.66,'K')),
            NASAPolynomial(coeffs=[3.60519,0.0376313,-2.25441e-05,6.65702e-09,-7.69428e-13,-7655.87,9.33737], Tmin=(405.66,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 62,
    label = "[CH2]C#CC",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2 C u1 p0 c0 {4,S} {8,S} {9,S}
3 C u0 p0 c0 {1,S} {4,T}
4 C u0 p0 c0 {2,S} {3,T}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.66989,0.0310849,-5.82384e-05,1.03936e-07,-7.20268e-11,35012.8,10.7393], Tmin=(10,'K'), Tmax=(493.84,'K')),
            NASAPolynomial(coeffs=[2.91427,0.0270545,-1.51639e-05,4.16431e-09,-4.47964e-13,35211.2,15.1049], Tmin=(493.84,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 63,
    label = "C4H8Of",
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
            NASAPolynomial(coeffs=[2.28845,0.0392193,-1.98589e-05,4.6133e-09,-4.20487e-13,-30953.2,16.9251], Tmin=(100,'K'), Tmax=(2427.92,'K')),
            NASAPolynomial(coeffs=[13.9499,0.0200071,-7.98944e-06,1.35415e-09,-8.48976e-14,-36615.8,-49.6788], Tmin=(2427.92,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 64,
    label = "CC=C(C)O",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {4,D} {5,S}
4  C u0 p0 c0 {2,S} {3,D} {12,S}
5  O u0 p2 c0 {3,S} {13,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61596,0.0355786,-3.32014e-05,5.78952e-08,-4.53996e-11,-25472,9.79197], Tmin=(10,'K'), Tmax=(505.63,'K')),
            NASAPolynomial(coeffs=[1.48068,0.042472,-2.39888e-05,6.63847e-09,-7.18963e-13,-25128.2,19.9012], Tmin=(505.63,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 65,
    label = "[CH2]C([O])CC",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {2,S} {12,S} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  O u1 p2 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53185,0.0428599,-5.00577e-05,6.97763e-08,-4.60065e-11,14370.6,12.2244], Tmin=(10,'K'), Tmax=(506.5,'K')),
            NASAPolynomial(coeffs=[2.78002,0.0414325,-2.4019e-05,6.79449e-09,-7.49182e-13,14541.3,16.2727], Tmin=(506.5,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 66,
    label = "CC[CH]C[O]",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {3,S} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u1 p2 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.41913,0.0644529,-0.000277937,7.20163e-07,-6.27076e-10,14762.8,12.652], Tmin=(10,'K'), Tmax=(402.29,'K')),
            NASAPolynomial(coeffs=[0.635082,0.0444364,-2.54532e-05,7.02872e-09,-7.5319e-13,15372.8,28.3455], Tmin=(402.29,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 67,
    label = "CC(=O)C(C)O[O]",
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
            NASAPolynomial(coeffs=[3.35681,0.0622898,-0.000115498,1.88597e-07,-1.30859e-10,-24951.3,13.8927], Tmin=(10,'K'), Tmax=(438.42,'K')),
            NASAPolynomial(coeffs=[4.14518,0.0459484,-2.82885e-05,8.38987e-09,-9.59513e-13,-24932.5,11.7421], Tmin=(438.42,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 68,
    label = "C=[C]C[O]",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,D} {7,S} {8,S}
3 C u1 p0 c0 {1,S} {2,D}
4 O u1 p2 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88701,0.00844671,0.000111637,-3.342e-07,2.95496e-10,38765.8,9.42664], Tmin=(10,'K'), Tmax=(392.97,'K')),
            NASAPolynomial(coeffs=[4.55688,0.0212903,-1.24391e-05,3.61606e-09,-4.15298e-13,38561.4,4.88888], Tmin=(392.97,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 69,
    label = "[CH2]C(=C)[O]",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,S} {3,S} {4,D}
2 C u1 p0 c0 {1,S} {5,S} {6,S}
3 C u1 p0 c0 {1,S} {7,S} {8,S}
4 O u0 p2 c0 {1,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92837,0.00456343,9.28912e-05,-2.01151e-07,1.32902e-10,16421.3,8.26946], Tmin=(10,'K'), Tmax=(496.39,'K')),
            NASAPolynomial(coeffs=[3.00327,0.0264856,-1.70721e-05,5.2493e-09,-6.20142e-13,16334.9,10.2892], Tmin=(496.39,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 70,
    label = "[CH2]C(C)[O]",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u1 p0 c0 {1,S} {9,S} {10,S}
4  O u1 p2 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87745,0.0104879,8.96202e-05,-2.42557e-07,2.12584e-10,17572.7,11.4146], Tmin=(10,'K'), Tmax=(290.65,'K')),
            NASAPolynomial(coeffs=[2.35613,0.0314246,-1.84303e-05,5.27881e-09,-5.88426e-13,17661.1,16.8743], Tmin=(290.65,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 71,
    label = "C[CH]C[O]",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {2,S} {10,S}
4  O u1 p2 c0 {2,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61336,0.044829,-0.000221766,6.17329e-07,-5.58792e-10,17557.4,12.0108], Tmin=(10,'K'), Tmax=(395.11,'K')),
            NASAPolynomial(coeffs=[0.555425,0.033615,-1.90901e-05,5.21073e-09,-5.51311e-13,18128.2,28.0895], Tmin=(395.11,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 72,
    label = "[CH]1COOC1",
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
            NASAPolynomial(coeffs=[3.9655,0.00210967,0.000103851,-1.85908e-07,1.07289e-10,9593.73,9.93466], Tmin=(10,'K'), Tmax=(448.52,'K')),
            NASAPolynomial(coeffs=[-0.413415,0.0411683,-2.6796e-05,8.31294e-09,-9.8535e-13,9986.47,27.5486], Tmin=(448.52,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 73,
    label = "[CH2]C([CH2])=C",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {3,S} {4,D}
2  C u1 p0 c0 {1,S} {5,S} {6,S}
3  C u1 p0 c0 {1,S} {7,S} {8,S}
4  C u0 p0 c0 {1,D} {9,S} {10,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91729,0.00500849,0.000110185,-2.20141e-07,1.34552e-10,33363.8,6.97829], Tmin=(10,'K'), Tmax=(535.73,'K')),
            NASAPolynomial(coeffs=[2.52835,0.0335911,-2.08374e-05,6.3618e-09,-7.59395e-13,33251.2,10.373], Tmin=(535.73,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 74,
    label = "[CH2][CH]C=C",
    molecule = 
"""
multiplicity 3
1  C u1 p0 c0 {2,S} {3,S} {6,S}
2  C u0 p0 c0 {1,S} {4,D} {5,S}
3  C u1 p0 c0 {1,S} {9,S} {10,S}
4  C u0 p0 c0 {2,D} {7,S} {8,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8984,0.00643101,0.000117843,-2.5875e-07,1.71777e-10,40123.1,10.0154], Tmin=(10,'K'), Tmax=(504.83,'K')),
            NASAPolynomial(coeffs=[3.46847,0.0311743,-1.90759e-05,5.7859e-09,-6.87356e-13,39894.7,9.10288], Tmin=(504.83,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 75,
    label = "CC=CCO[O]",
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
            NASAPolynomial(coeffs=[3.49745,0.0528365,-0.000154252,3.7412e-07,-3.1969e-10,3818.19,12.4195], Tmin=(10,'K'), Tmax=(413.41,'K')),
            NASAPolynomial(coeffs=[1.45316,0.0451426,-2.66528e-05,7.60399e-09,-8.41029e-13,4221.99,23.3158], Tmin=(413.41,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 76,
    label = "C=C(C)CC",
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
            NASAPolynomial(coeffs=[3.73201,0.0304451,9.25036e-06,-2.13196e-08,7.19938e-12,-6558.05,11.0267], Tmin=(10,'K'), Tmax=(1164.78,'K')),
            NASAPolynomial(coeffs=[5.21191,0.0386303,-1.83759e-05,4.2712e-09,-3.92097e-13,-7802.8,-0.20206], Tmin=(1164.78,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 77,
    label = "C=CC(C)C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {5,D} {13,S}
5  C u0 p0 c0 {4,D} {14,S} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
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
            NASAPolynomial(coeffs=[3.61256,0.0302796,2.87173e-05,-6.95968e-08,3.95506e-11,-5775.76,9.81642], Tmin=(10,'K'), Tmax=(474.14,'K')),
            NASAPolynomial(coeffs=[1.57863,0.0474385,-2.55669e-05,6.7297e-09,-6.94066e-13,-5582.88,18.1112], Tmin=(474.14,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 78,
    label = "CC=CCC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {5,D} {15,S}
5  C u0 p0 c0 {3,S} {4,D} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.58583,0.0350492,-1.15744e-05,1.4326e-08,-1.41917e-11,-6158,11.2323], Tmin=(10,'K'), Tmax=(593.03,'K')),
            NASAPolynomial(coeffs=[0.046001,0.0501611,-2.763e-05,7.45453e-09,-7.89287e-13,-5584.04,27.7597], Tmin=(593.03,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 79,
    label = "C=CCCC(=C)C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {3,S} {6,D}
5  C u0 p0 c0 {2,S} {7,D} {15,S}
6  C u0 p0 c0 {4,D} {16,S} {17,S}
7  C u0 p0 c0 {5,D} {18,S} {19,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.30935,0.0676551,-0.000127439,2.62076e-07,-2.03721e-10,3067.69,13.6435], Tmin=(10,'K'), Tmax=(460.81,'K')),
            NASAPolynomial(coeffs=[0.516294,0.0660164,-3.78527e-05,1.05811e-08,-1.15379e-12,3599.92,27.9363], Tmin=(460.81,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 80,
    label = "C=CCC(C)C=C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {6,D} {14,S}
5  C u0 p0 c0 {2,S} {7,D} {15,S}
6  C u0 p0 c0 {4,D} {16,S} {17,S}
7  C u0 p0 c0 {5,D} {18,S} {19,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95751,0.00679816,0.000966665,-7.96634e-06,2.37952e-08,1657.58,4.0814], Tmin=(10,'K'), Tmax=(83.77,'K')),
            NASAPolynomial(coeffs=[2.78408,0.06281,-3.59494e-05,1.00447e-08,-1.09436e-12,1677.25,6.83318], Tmin=(83.77,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 81,
    label = "C=CC(C)[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u1 p2 c0 {1,S}
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
            NASAPolynomial(coeffs=[3.86237,0.0115665,0.000109146,-2.52035e-07,1.86356e-10,5590.95,11.0482], Tmin=(10,'K'), Tmax=(346.69,'K')),
            NASAPolynomial(coeffs=[1.15789,0.0427705,-2.58641e-05,7.58655e-09,-8.61475e-13,5778.47,21.2308], Tmin=(346.69,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 82,
    label = "C=CC(C)CC=CC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {7,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {2,S} {7,D} {19,S}
6  C u0 p0 c0 {1,S} {8,D} {20,S}
7  C u0 p0 c0 {4,S} {5,D} {18,S}
8  C u0 p0 c0 {6,D} {21,S} {22,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.06661,0.0874126,-0.00015056,2.51941e-07,-1.71067e-10,-563.301,14.502], Tmin=(10,'K'), Tmax=(491.61,'K')),
            NASAPolynomial(coeffs=[1.83044,0.0747863,-4.28203e-05,1.19777e-08,-1.30833e-12,-167.634,22.3761], Tmin=(491.61,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 83,
    label = "CCC1COO1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {3,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95112,0.0283874,1.51553e-05,-2.80851e-08,9.44255e-12,-10211.5,10.6721], Tmin=(10,'K'), Tmax=(1176.14,'K')),
            NASAPolynomial(coeffs=[8.7404,0.0319979,-1.48272e-05,3.29456e-09,-2.85153e-13,-12714.4,-19.0613], Tmin=(1176.14,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 84,
    label = "C=C(CC)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {5,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u0 p2 c0 {3,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.64631,0.0340985,-1.29018e-06,-1.71476e-08,7.61331e-12,2744.42,13.049], Tmin=(10,'K'), Tmax=(990.75,'K')),
            NASAPolynomial(coeffs=[5.57361,0.0361613,-1.93173e-05,5.01162e-09,-5.0887e-13,1879.4,1.33061], Tmin=(990.75,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 85,
    label = "[CH2]C(=O)C(C)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,S} {11,D}
4  C u1 p0 c0 {3,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {3,D}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.26345,0.0630387,-6.48788e-05,3.86436e-08,-9.97758e-12,-20913.6,13.0487], Tmin=(10,'K'), Tmax=(862.09,'K')),
            NASAPolynomial(coeffs=[8.35162,0.0394303,-2.38012e-05,6.8778e-09,-7.65748e-13,-21790.9,-10.7437], Tmin=(862.09,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 86,
    label = "C=C(O)C(C)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {6,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {13,S}
6  O u0 p2 c0 {3,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 O u1 p2 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75422,0.0154554,0.00021357,-4.95682e-07,3.32515e-10,-19387.6,13.1564], Tmin=(10,'K'), Tmax=(519.86,'K')),
            NASAPolynomial(coeffs=[5.58347,0.0518281,-3.69424e-05,1.22465e-08,-1.51904e-12,-20259.5,-1.02832], Tmin=(519.86,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 87,
    label = "[CH]=C(C)O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C u0 p0 c0 {1,S} {3,S} {4,D}
3 O u0 p2 c0 {2,S} {8,S}
4 C u1 p0 c0 {2,D} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92248,0.00452138,9.62635e-05,-1.85411e-07,1.07516e-10,8923.44,8.95], Tmin=(10,'K'), Tmax=(570.12,'K')),
            NASAPolynomial(coeffs=[2.6309,0.0313984,-2.13226e-05,6.89617e-09,-8.45058e-13,8781.18,11.9162], Tmin=(570.12,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 88,
    label = "C=[C]CO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,D} {7,S} {8,S}
3 C u1 p0 c0 {1,S} {2,D}
4 O u0 p2 c0 {1,S} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.56219,0.0302011,-3.14512e-05,2.25254e-08,-7.03604e-12,11518.8,10.7758], Tmin=(10,'K'), Tmax=(922.05,'K')),
            NASAPolynomial(coeffs=[4.20039,0.0228619,-1.20761e-05,3.14067e-09,-3.22495e-13,11595.4,8.80225], Tmin=(922.05,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 89,
    label = "[CH2]C[O]",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,S} {7,S}
3 O u1 p2 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97942,0.00128209,5.85417e-05,-1.07431e-07,6.44104e-11,22251.9,8.90015], Tmin=(10,'K'), Tmax=(428.8,'K')),
            NASAPolynomial(coeffs=[1.7847,0.0217498,-1.30378e-05,3.82541e-09,-4.3742e-13,22440.2,17.6306], Tmin=(428.8,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 90,
    label = "C=C(C)CO",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84599,0.0122564,0.000198626,-6.23264e-07,5.99666e-10,-22048.9,10.9485], Tmin=(10,'K'), Tmax=(349.26,'K')),
            NASAPolynomial(coeffs=[3.83494,0.0379272,-2.13351e-05,6.01353e-09,-6.7295e-13,-22203.9,8.75984], Tmin=(349.26,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 91,
    label = "CC=CCO",
    molecule = 
"""
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
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84794,0.013722,0.00024172,-9.49888e-07,1.15016e-09,-21554.4,10.6565], Tmin=(10,'K'), Tmax=(279.75,'K')),
            NASAPolynomial(coeffs=[4.08037,0.0364218,-1.95307e-05,5.22468e-09,-5.56939e-13,-21669.3,8.01126], Tmin=(279.75,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 92,
    label = "CC1[CH]COO1",
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
            NASAPolynomial(coeffs=[3.79832,0.0181285,7.27589e-05,-1.32327e-07,6.78906e-11,4254.8,11.4832], Tmin=(10,'K'), Tmax=(636.87,'K')),
            NASAPolynomial(coeffs=[1.46267,0.0469034,-2.82359e-05,8.1702e-09,-9.12575e-13,4266.25,19.4518], Tmin=(636.87,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 93,
    label = "[CH2]C1OOC1C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {2,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {2,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86005,0.0131636,0.000185853,-5.97855e-07,6.39212e-10,11733.2,12.205], Tmin=(10,'K'), Tmax=(237,'K')),
            NASAPolynomial(coeffs=[1.83976,0.0472605,-2.99439e-05,9.15376e-09,-1.07586e-12,11829,19.0432], Tmin=(237,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 94,
    label = "C[C]=CCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {5,D} {14,S}
5  C u1 p0 c0 {3,S} {4,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.5878,0.0398296,-6.05849e-05,1.31585e-07,-1.05245e-10,22392.2,12.0275], Tmin=(10,'K'), Tmax=(480.77,'K')),
            NASAPolynomial(coeffs=[0.675603,0.0463911,-2.59321e-05,7.09298e-09,-7.59723e-13,22876.4,26.0679], Tmin=(480.77,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 95,
    label = "C[CH]C1COO1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {3,S} {13,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {2,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9779,0.0259521,1.68113e-05,-3.00257e-08,1.0321e-11,12949.8,12.5138], Tmin=(10,'K'), Tmax=(1139.94,'K')),
            NASAPolynomial(coeffs=[8.38282,0.0300874,-1.44102e-05,3.31042e-09,-2.96445e-13,10672.6,-14.8978], Tmin=(1139.94,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 96,
    label = "C1=CCC1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {4,D} {9,S}
4  C u0 p0 c0 {2,S} {3,D} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.17813,-0.0132966,0.000133186,-1.86955e-07,8.52698e-11,18156.9,7.19706], Tmin=(10,'K'), Tmax=(678.86,'K')),
            NASAPolynomial(coeffs=[-1.61953,0.0392367,-2.34859e-05,6.76761e-09,-7.52062e-13,18520.7,29.8037], Tmin=(678.86,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 97,
    label = "C=C[C]C",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,D} {4,S} {8,S}
3  C u0 p0 c0 {2,D} {9,S} {10,S}
4  C u0 p1 c0 {1,S} {2,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98219,0.015909,1.50885e-05,-2.22638e-08,7.2536e-12,45420.1,9.65734], Tmin=(10,'K'), Tmax=(1156.53,'K')),
            NASAPolynomial(coeffs=[5.96274,0.0223087,-1.03963e-05,2.33239e-09,-2.0448e-13,44075.9,-4.01658], Tmin=(1156.53,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 98,
    label = "C=C[CH]CO[O]",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u1 p0 c0 {1,S} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {10,S} {11,S}
5  O u0 p2 c0 {1,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91905,0.0103728,0.000405687,-2.71709e-06,6.45975e-09,21259.8,11.8731], Tmin=(10,'K'), Tmax=(105.43,'K')),
            NASAPolynomial(coeffs=[3.12076,0.0406592,-2.52047e-05,7.52993e-09,-8.674e-13,21276.6,13.9285], Tmin=(105.43,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 99,
    label = "[CH2]C(C)C=C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  C u1 p0 c0 {1,S} {11,S} {12,S}
5  C u0 p0 c0 {3,D} {13,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
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
            NASAPolynomial(coeffs=[3.91352,0.0104634,0.000448761,-2.70773e-06,5.38114e-09,19344.4,10.3705], Tmin=(10,'K'), Tmax=(162.4,'K')),
            NASAPolynomial(coeffs=[3.52259,0.0407369,-2.15349e-05,5.56903e-09,-5.65295e-13,19329.8,10.7077], Tmin=(162.4,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 100,
    label = "[CH2]C=CCC",
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
            NASAPolynomial(coeffs=[3.69967,0.0256651,3.04816e-05,-5.64464e-08,2.48745e-11,11455.2,11.9458], Tmin=(10,'K'), Tmax=(753.32,'K')),
            NASAPolynomial(coeffs=[1.3455,0.0459895,-2.55677e-05,6.94282e-09,-7.37627e-13,11587.9,21.1629], Tmin=(753.32,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 101,
    label = "C=CCCO[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u0 p2 c0 {2,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.31284,0.0757755,-0.000332015,8.43313e-07,-7.32532e-10,5041.39,11.0166], Tmin=(10,'K'), Tmax=(395.07,'K')),
            NASAPolynomial(coeffs=[1.37487,0.0453738,-2.66541e-05,7.51821e-09,-8.20116e-13,5584.89,23.5071], Tmin=(395.07,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 102,
    label = "C=C[CH]COO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {3,S} {9,S}
3  C u0 p0 c0 {2,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.14001,0.0687639,-0.000127993,1.49697e-07,-6.89992e-11,4183.77,11.8607], Tmin=(10,'K'), Tmax=(652,'K')),
            NASAPolynomial(coeffs=[5.97461,0.0367663,-2.07735e-05,5.70499e-09,-6.12468e-13,4124.62,1.77879], Tmin=(652,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 103,
    label = "[CH2]C(=C)C[CH]C=C",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {6,D}
3  C u1 p0 c0 {1,S} {4,S} {10,S}
4  C u0 p0 c0 {3,S} {7,D} {11,S}
5  C u1 p0 c0 {2,S} {14,S} {15,S}
6  C u0 p0 c0 {2,D} {16,S} {17,S}
7  C u0 p0 c0 {4,D} {12,S} {13,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75456,0.0254672,0.000270746,-1.21948e-06,1.85313e-09,37712.2,14.2013], Tmin=(10,'K'), Tmax=(165.76,'K')),
            NASAPolynomial(coeffs=[2.35467,0.0592479,-3.49424e-05,9.95857e-09,-1.10013e-12,37758.6,18.439], Tmin=(165.76,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 104,
    label = "[CH2]CC(=C)C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {5,D}
4  C u1 p0 c0 {1,S} {11,S} {12,S}
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
            NASAPolynomial(coeffs=[3.55114,0.0426828,-6.37576e-05,1.24036e-07,-9.40931e-11,18372,12.0489], Tmin=(10,'K'), Tmax=(487.18,'K')),
            NASAPolynomial(coeffs=[1.30087,0.0457483,-2.57483e-05,7.09426e-09,-7.65019e-13,18774.2,23.1638], Tmin=(487.18,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 105,
    label = "CCC(C[O])OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u1 p2 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.46968,0.0460158,5.30944e-05,-1.69117e-07,1.11284e-10,-21796.7,13.0365], Tmin=(10,'K'), Tmax=(567.51,'K')),
            NASAPolynomial(coeffs=[5.5537,0.0555782,-3.62798e-05,1.11714e-08,-1.30804e-12,-22423.7,0.722194], Tmin=(567.51,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 106,
    label = "[CH2]C(O)C=C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,D} {7,S}
3  C u1 p0 c0 {1,S} {8,S} {9,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  O u0 p2 c0 {1,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78712,0.0200359,0.000191938,-8.05301e-07,9.96438e-10,3306.74,11.3013], Tmin=(10,'K'), Tmax=(278.44,'K')),
            NASAPolynomial(coeffs=[4.23763,0.0367085,-2.25666e-05,6.8317e-09,-8.03095e-13,3191.94,8.09276], Tmin=(278.44,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 107,
    label = "C=CCCC",
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
            NASAPolynomial(coeffs=[3.54373,0.0448382,-7.8288e-05,1.75802e-07,-1.42145e-10,-4889.05,10.756], Tmin=(10,'K'), Tmax=(468.99,'K')),
            NASAPolynomial(coeffs=[0.36628,0.0505862,-2.83806e-05,7.78376e-09,-8.35269e-13,-4356.19,26.183], Tmin=(468.99,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 108,
    label = "[C]1=CCC1",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3 C u0 p0 c0 {1,S} {4,D} {9,S}
4 C u1 p0 c0 {2,S} {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.15683,-0.0119788,0.000123799,-1.78963e-07,8.39053e-11,48096.4,8.47065], Tmin=(10,'K'), Tmax=(664.83,'K')),
            NASAPolynomial(coeffs=[-0.658353,0.0346081,-2.10566e-05,6.14852e-09,-6.90405e-13,48347.3,26.8076], Tmin=(664.83,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 109,
    label = "C=C1CC1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {9,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.10949,-0.00947443,0.000139639,-2.2667e-07,1.19786e-10,21610.1,7.38241], Tmin=(10,'K'), Tmax=(583.53,'K')),
            NASAPolynomial(coeffs=[-0.303763,0.0371622,-2.23607e-05,6.52792e-09,-7.3703e-13,21846.2,23.9064], Tmin=(583.53,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 110,
    label = "[CH2][C]1CC1",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u1 p0 c0 {1,S} {2,S} {4,S}
4  C u1 p0 c0 {3,S} {9,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93277,0.00397108,0.000103325,-1.93988e-07,1.12467e-10,52440.1,8.03838], Tmin=(10,'K'), Tmax=(551.11,'K')),
            NASAPolynomial(coeffs=[1.65178,0.0353528,-2.24429e-05,6.96784e-09,-8.37093e-13,52466.4,15.6411], Tmin=(551.11,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 111,
    label = "C=CCCO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u0 p2 c0 {2,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84453,0.0145948,0.00022226,-8.53602e-07,1.03219e-09,-20946.9,10.1399], Tmin=(10,'K'), Tmax=(268.22,'K')),
            NASAPolynomial(coeffs=[3.272,0.0409316,-2.45654e-05,7.30084e-09,-8.46793e-13,-20980.2,10.9551], Tmin=(268.22,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 112,
    label = "[CH2]C(=C)C[O]",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  C u1 p0 c0 {2,S} {8,S} {9,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  O u1 p2 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89018,0.00706394,0.000137487,-3.04017e-07,2.04934e-10,23466.9,11.1925], Tmin=(10,'K'), Tmax=(490.2,'K')),
            NASAPolynomial(coeffs=[2.8877,0.0374371,-2.33649e-05,7.09851e-09,-8.36796e-13,23298.5,12.5944], Tmin=(490.2,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 113,
    label = "[O]C[O]",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u1 p2 c0 {1,S}
3 O u1 p2 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05624,-0.0052025,4.0072e-05,2.86904e-08,-1.38473e-10,7315.17,7.25219], Tmin=(10,'K'), Tmax=(300.23,'K')),
            NASAPolynomial(coeffs=[1.36311,0.0179736,-1.22446e-05,3.91146e-09,-4.71766e-13,7534.14,17.9582], Tmin=(300.23,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 114,
    label = "C=CC[CH]C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {2,S} {11,S}
4  C u0 p0 c0 {1,S} {5,D} {12,S}
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
            NASAPolynomial(coeffs=[3.53221,0.0523044,-0.000198754,5.4954e-07,-4.93384e-10,18756,12.3449], Tmin=(10,'K'), Tmax=(409.01,'K')),
            NASAPolynomial(coeffs=[-0.754927,0.0500471,-2.84374e-05,7.81945e-09,-8.36267e-13,19476.2,33.7131], Tmin=(409.01,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 115,
    label = "[CH2]CC=CC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {12,S}
4  C u0 p0 c0 {2,S} {3,D} {11,S}
5  C u1 p0 c0 {1,S} {13,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.58666,0.0406815,-6.54421e-05,1.49813e-07,-1.24085e-10,18951.2,11.2978], Tmin=(10,'K'), Tmax=(465.65,'K')),
            NASAPolynomial(coeffs=[0.573237,0.0476484,-2.6941e-05,7.43917e-09,-8.02852e-13,19436.9,25.735], Tmin=(465.65,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 116,
    label = "C[C]1COOC1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {2,S} {3,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {2,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96293,0.0217314,3.42432e-05,-5.03327e-08,1.79981e-11,4530.59,11.2241], Tmin=(10,'K'), Tmax=(1018.4,'K')),
            NASAPolynomial(coeffs=[5.25503,0.0374421,-1.95126e-05,4.89871e-09,-4.80203e-13,3189.54,-0.325115], Tmin=(1018.4,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 117,
    label = "[CH2]C(=C)CO[O]",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  C u1 p0 c0 {2,S} {10,S} {11,S}
4  C u0 p0 c0 {2,D} {8,S} {9,S}
5  O u0 p2 c0 {1,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.59105,0.0441222,-0.000116239,3.2388e-07,-3.16758e-10,22325.1,13.3886], Tmin=(10,'K'), Tmax=(375.67,'K')),
            NASAPolynomial(coeffs=[1.4443,0.0445229,-2.81731e-05,8.47911e-09,-9.77594e-13,22644.8,23.7528], Tmin=(375.67,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 118,
    label = "[CH2]C(=C)COO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  C u1 p0 c0 {2,S} {9,S} {10,S}
4  C u0 p0 c0 {2,D} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70419,0.026691,0.000251214,-1.1064e-06,1.36665e-09,4348.08,11.7993], Tmin=(10,'K'), Tmax=(292.98,'K')),
            NASAPolynomial(coeffs=[5.93542,0.0382322,-2.29288e-05,6.75421e-09,-7.77391e-13,4037.06,0.697559], Tmin=(292.98,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 119,
    label = "[CH2][O]",
    molecule = 
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05235,-0.00398795,3.38789e-05,-4.72886e-08,2.18622e-11,22358.2,5.37998], Tmin=(10,'K'), Tmax=(652.69,'K')),
            NASAPolynomial(coeffs=[2.48161,0.00935534,-5.32885e-06,1.48404e-09,-1.61228e-13,22484.1,11.6812], Tmin=(652.69,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 120,
    label = "C1OO1",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.09984,-0.00681232,5.10768e-05,-6.43263e-08,2.62869e-11,-1687.25,5.8349], Tmin=(10,'K'), Tmax=(764.36,'K')),
            NASAPolynomial(coeffs=[1.389,0.0156992,-9.43797e-06,2.70345e-09,-2.97088e-13,-1516.04,16.5938], Tmin=(764.36,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 121,
    label = "C=C1COO1",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2 C u0 p0 c0 {1,S} {3,D} {5,S}
3 C u0 p0 c0 {2,D} {8,S} {9,S}
4 O u0 p2 c0 {1,S} {5,S}
5 O u0 p2 c0 {2,S} {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97125,0.00176676,9.33233e-05,-1.67161e-07,9.61952e-11,7904.53,8.89324], Tmin=(10,'K'), Tmax=(449.82,'K')),
            NASAPolynomial(coeffs=[-0.0373214,0.0373448,-2.50909e-05,8.00176e-09,-9.69645e-13,8265.84,25.0374], Tmin=(449.82,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 122,
    label = "C=C1CO1",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 C u0 p0 c0 {2,D} {7,S} {8,S}
4 O u0 p2 c0 {1,S} {2,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.10405,-0.00937522,0.000124496,-2.11358e-07,1.16829e-10,5907.43,7.97621], Tmin=(10,'K'), Tmax=(565.85,'K')),
            NASAPolynomial(coeffs=[0.977084,0.0284793,-1.76022e-05,5.24653e-09,-6.01779e-13,6009.16,19.0534], Tmin=(565.85,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 123,
    label = "CCC=CO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {3,D} {5,S} {12,S}
5  O u0 p2 c0 {4,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86198,0.0105805,0.000186654,-5.32486e-07,4.71545e-10,-22800.5,10.9546], Tmin=(10,'K'), Tmax=(370.76,'K')),
            NASAPolynomial(coeffs=[3.14719,0.0404382,-2.37369e-05,6.91648e-09,-7.91337e-13,-22899.8,11.6411], Tmin=(370.76,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 124,
    label = "C4H8Od",
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
            NASAPolynomial(coeffs=[3.65077,0.0316115,-4.61e-06,-4.47532e-09,1.17109e-12,-27337.9,11.3548], Tmin=(100,'K'), Tmax=(2099.1,'K')),
            NASAPolynomial(coeffs=[18.9779,0.0217536,-1.13924e-05,2.07007e-09,-1.31466e-13,-38035.3,-84.1088], Tmin=(2099.1,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 125,
    label = "C[CH][O]",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,S} {7,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u1 p2 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92342,0.00570693,3.1849e-05,-5.45843e-08,2.86974e-11,17994.8,8.04585], Tmin=(10,'K'), Tmax=(495.73,'K')),
            NASAPolynomial(coeffs=[2.17184,0.0198405,-1.09176e-05,2.92977e-09,-3.0771e-13,18168.5,15.2671], Tmin=(495.73,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 126,
    label = "CCC1COC1O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {6,S} {7,S} {11,S}
4  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
5  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
6  O u0 p2 c0 {3,S} {4,S}
7  O u0 p2 c0 {3,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73577,0.0371489,2.37426e-05,-4.79195e-08,1.84042e-11,-43825.4,12.6342], Tmin=(10,'K'), Tmax=(991.62,'K')),
            NASAPolynomial(coeffs=[5.75102,0.0496633,-2.64146e-05,6.79544e-09,-6.83071e-13,-45240,-2.18879], Tmin=(991.62,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 127,
    label = "O=COC[O]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {5,S}
2 O u1 p2 c0 {4,S}
3 O u0 p2 c0 {5,D}
4 C u0 p0 c0 {1,S} {2,S} {6,S} {7,S}
5 C u0 p0 c0 {1,S} {3,D} {8,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.02348,0.0129964,1.71514e-05,-2.65466e-08,9.48374e-12,-39305,11.4774], Tmin=(10,'K'), Tmax=(1053.25,'K')),
            NASAPolynomial(coeffs=[6.09397,0.0184451,-9.56691e-06,2.36515e-09,-2.27131e-13,-40479.6,-2.12414], Tmin=(1053.25,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 128,
    label = "C1=CCOOC1",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {2,S} {3,D} {12,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {2,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.09058,-0.00834473,0.000174347,-2.89984e-07,1.54492e-10,-3849.62,9.88401], Tmin=(10,'K'), Tmax=(588.03,'K')),
            NASAPolynomial(coeffs=[-0.945822,0.0489762,-3.06993e-05,9.17773e-09,-1.05116e-12,-3656.01,28.1173], Tmin=(588.03,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 129,
    label = "CCC(CO)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {15,S}
6  O u0 p2 c0 {3,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
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
            NASAPolynomial(coeffs=[3.03774,0.0729967,-8.78693e-05,6.55736e-08,-2.08131e-11,-31873.4,13.5676], Tmin=(10,'K'), Tmax=(822.94,'K')),
            NASAPolynomial(coeffs=[8.28486,0.0426562,-2.37516e-05,6.49047e-09,-6.94819e-13,-32573.2,-9.72926], Tmin=(822.94,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 130,
    label = "CCC([CH]O)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {6,S} {14,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {4,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.05534,0.0846289,-0.000147043,1.78287e-07,-9.24118e-11,-27210.2,13.2033], Tmin=(10,'K'), Tmax=(509.1,'K')),
            NASAPolynomial(coeffs=[6.95206,0.0496127,-3.09088e-05,9.23518e-09,-1.06092e-12,-27550,-2.40547], Tmin=(509.1,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 131,
    label = "CCC([CH]O)C[O]",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
5  C u1 p0 c0 {1,S} {6,S} {16,S}
6  O u0 p2 c0 {5,S} {17,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u1 p2 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.56282,0.0452173,4.25472e-05,-1.08656e-07,5.54139e-11,-10721.6,12.9855], Tmin=(10,'K'), Tmax=(744.11,'K')),
            NASAPolynomial(coeffs=[6.58672,0.0563321,-3.50318e-05,1.02807e-08,-1.15318e-12,-11929.3,-5.80082], Tmin=(744.11,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 132,
    label = "[O]C(O)=O",
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
            NASAPolynomial(coeffs=[4.06454,-0.00639401,9.25102e-05,-1.70342e-07,9.86693e-11,-45964.9,8.8315], Tmin=(10,'K'), Tmax=(572.97,'K')),
            NASAPolynomial(coeffs=[3.36288,0.0159265,-1.15335e-05,3.78386e-09,-4.61084e-13,-46170.5,9.33027], Tmin=(572.97,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 133,
    label = "[CH2]C[C]=O",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,S} {7,S}
3 C u1 p0 c0 {1,S} {8,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61211,0.0360583,-8.72246e-05,1.4197e-07,-8.84343e-11,19813.3,9.36617], Tmin=(10,'K'), Tmax=(502.25,'K')),
            NASAPolynomial(coeffs=[4.38628,0.0202723,-1.13473e-05,3.11706e-09,-3.35708e-13,19856.9,7.37231], Tmin=(502.25,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 134,
    label = "C=C[CH]C[CH]C",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
3  C u1 p0 c0 {1,S} {2,S} {12,S}
4  C u1 p0 c0 {1,S} {5,S} {13,S}
5  C u0 p0 c0 {4,S} {6,D} {14,S}
6  C u0 p0 c0 {5,D} {15,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.11561,0.0925872,-0.000353309,7.95513e-07,-6.23717e-10,31937.6,11.9303], Tmin=(10,'K'), Tmax=(431.05,'K')),
            NASAPolynomial(coeffs=[1.69098,0.052613,-2.90955e-05,7.79122e-09,-8.13892e-13,32554.6,23.3368], Tmin=(431.05,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 135,
    label = "C=CCC[C]C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {6,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {5,D} {14,S}
5  C u0 p0 c0 {4,D} {15,S} {16,S}
6  C u0 p1 c0 {2,S} {3,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.30346,0.0717511,-0.000207745,4.65339e-07,-3.75753e-10,41314.4,11.5671], Tmin=(10,'K'), Tmax=(424.47,'K')),
            NASAPolynomial(coeffs=[1.70554,0.0543824,-3.17791e-05,9.00176e-09,-9.90537e-13,41742.2,21.3479], Tmin=(424.47,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 136,
    label = "CC=C([O])O[O]",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u1 p0 c0 {1,S} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {9,D}
4  O u0 p2 c0 {3,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {3,D}
10 O u1 p2 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79015,0.0319073,-8.20033e-06,-1.14369e-08,6.16846e-12,-4212.01,11.4819], Tmin=(10,'K'), Tmax=(1024.91,'K')),
            NASAPolynomial(coeffs=[9.40169,0.0224967,-1.27074e-05,3.3853e-09,-3.47444e-13,-6018.27,-18.9289], Tmin=(1024.91,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 137,
    label = "CC=C([O])C[O]",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {5,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {4,S} {12,S}
4  C u0 p0 c0 {2,S} {3,S} {11,D}
5  O u1 p2 c0 {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {4,D}
12 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89472,0.0314695,2.57228e-07,-1.61332e-08,6.3478e-12,-2157.6,12.2148], Tmin=(10,'K'), Tmax=(1165.53,'K')),
            NASAPolynomial(coeffs=[10.3816,0.0252352,-1.23469e-05,2.87474e-09,-2.6004e-13,-4758.4,-24.7443], Tmin=(1165.53,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 138,
    label = "CC1OCC1=O",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {4,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
4  C u0 p0 c0 {1,S} {2,S} {12,D}
5  O u0 p2 c0 {1,S} {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83061,0.0163855,5.86414e-05,-9.99118e-08,4.73075e-11,-29839.7,10.8649], Tmin=(10,'K'), Tmax=(698.39,'K')),
            NASAPolynomial(coeffs=[1.72273,0.0418169,-2.46719e-05,7.00605e-09,-7.69872e-13,-29871.1,17.9452], Tmin=(698.39,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 139,
    label = "[CH2][C]=O",
    molecule = 
"""
multiplicity 3
1 O u0 p2 c0 {3,D}
2 C u1 p0 c0 {3,S} {4,S} {5,S}
3 C u1 p0 c0 {1,D} {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98818,0.000815919,4.41915e-05,-9.22286e-08,6.34618e-11,20468.6,7.18558], Tmin=(10,'K'), Tmax=(372.19,'K')),
            NASAPolynomial(coeffs=[2.76936,0.0139276,-8.70286e-06,2.60839e-09,-3.02414e-13,20559.3,11.8598], Tmin=(372.19,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 140,
    label = "C_CC(C)=O",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C u0 p0 c0 {1,S} {3,S} {8,D}
3 C u0 p0 c0 {2,S} {4,T}
4 C u0 p0 c0 {3,T} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 O u0 p2 c0 {2,D}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94579,0.00583251,0.000195039,-8.29523e-07,1.22102e-09,7178.31,9.30524], Tmin=(10,'K'), Tmax=(170.96,'K')),
            NASAPolynomial(coeffs=[2.90225,0.0302492,-1.91975e-05,5.92167e-09,-7.03849e-13,7213.99,12.4965], Tmin=(170.96,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 141,
    label = "C=C=CC=O",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,D} {5,S}
2 C u0 p0 c0 {1,S} {6,D} {7,S}
3 C u0 p0 c0 {4,D} {8,S} {9,S}
4 C u0 p0 c0 {1,D} {3,D}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92488,0.00469241,0.000106713,-2.2071e-07,1.40162e-10,6935.71,9.17587], Tmin=(10,'K'), Tmax=(508.4,'K')),
            NASAPolynomial(coeffs=[2.29491,0.0328332,-2.15034e-05,6.67585e-09,-7.90668e-13,6903.5,13.9901], Tmin=(508.4,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 142,
    label = "C=CCC=O",
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
            NASAPolynomial(coeffs=[3.58627,0.0452995,-0.00016945,4.41919e-07,-3.87917e-10,-11354.2,11.4187], Tmin=(10,'K'), Tmax=(405.88,'K')),
            NASAPolynomial(coeffs=[1.20481,0.0370088,-2.14307e-05,5.9927e-09,-6.50389e-13,-10899.3,23.9832], Tmin=(405.88,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 143,
    label = "C4H6Ob",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  C u0 p0 c0 {2,D} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {8,D} {9,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {4,D}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.13246,0.0359424,-1.86802e-05,3.29899e-09,1.80912e-13,-15542.9,18.2406], Tmin=(100,'K'), Tmax=(1342.81,'K')),
            NASAPolynomial(coeffs=[9.19523,0.0208502,-8.46397e-06,1.52486e-09,-1.02784e-13,-17975.8,-19.9113], Tmin=(1342.81,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 144,
    label = "C4H6Oa",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  C u0 p0 c0 {3,S} {10,D} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 O u0 p2 c0 {4,D}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.13246,0.0359424,-1.86802e-05,3.29899e-09,1.80912e-13,-14580.7,17.1099], Tmin=(100,'K'), Tmax=(1342.81,'K')),
            NASAPolynomial(coeffs=[9.19523,0.0208502,-8.46397e-06,1.52486e-09,-1.02784e-13,-17013.6,-21.042], Tmin=(1342.81,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 145,
    label = "C=C(C)C[C]=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  C u1 p0 c0 {1,S} {13,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 O u0 p2 c0 {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.4519,0.049725,-7.46347e-05,1.03627e-07,-6.25442e-11,2276.5,12.5013], Tmin=(10,'K'), Tmax=(517.3,'K')),
            NASAPolynomial(coeffs=[3.60697,0.0402677,-2.32655e-05,6.56484e-09,-7.22582e-13,2370.95,12.9234], Tmin=(517.3,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 146,
    label = "C=CC=CC=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {6,S}
2  C u0 p0 c0 {1,S} {4,D} {7,S}
3  C u0 p0 c0 {1,D} {5,S} {8,S}
4  C u0 p0 c0 {2,D} {11,S} {12,S}
5  C u0 p0 c0 {3,S} {9,D} {10,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  O u0 p2 c0 {5,D}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75932,0.0209551,6.02289e-05,-1.18379e-07,6.19186e-11,-3294.48,10.0586], Tmin=(10,'K'), Tmax=(649.64,'K')),
            NASAPolynomial(coeffs=[2.68619,0.0431341,-2.69364e-05,7.96837e-09,-9.0252e-13,-3483.64,12.2439], Tmin=(649.64,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 147,
    label = "O=CCC=O",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,D} {9,S}
3 C u0 p0 c0 {1,S} {7,D} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
7 O u0 p2 c0 {3,D}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.57131,0.0509019,-0.000291291,8.3813e-07,-7.89369e-10,-32813.5,11.7691], Tmin=(10,'K'), Tmax=(374,'K')),
            NASAPolynomial(coeffs=[0.836738,0.0315732,-1.8948e-05,5.39436e-09,-5.89931e-13,-32269.3,26.8142], Tmin=(374,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 148,
    label = "O=C=CCC=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,D} {7,S}
3  C u0 p0 c0 {1,S} {8,D} {9,S}
4  C u0 p0 c0 {2,D} {10,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  O u0 p2 c0 {3,D}
9  H u0 p0 c0 {3,S}
10 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.32508,0.0537621,-0.000108402,1.32186e-07,-6.21893e-11,-22370.5,11.0398], Tmin=(10,'K'), Tmax=(649.87,'K')),
            NASAPolynomial(coeffs=[5.42142,0.0271383,-1.52804e-05,4.16991e-09,-4.44596e-13,-22353.2,4.05884], Tmin=(649.87,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 149,
    label = "[CH2]CCCOO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u1 p0 c0 {2,S} {13,S} {14,S}
5  O u0 p2 c0 {3,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.21373,0.0797122,-0.000241321,4.97882e-07,-3.79056e-10,-3146.45,14.7199], Tmin=(10,'K'), Tmax=(428.35,'K')),
            NASAPolynomial(coeffs=[3.51888,0.0478522,-2.81659e-05,8.03199e-09,-8.8905e-13,-2906.44,16.6131], Tmin=(428.35,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 150,
    label = "C=CC[C]=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,D} {7,S}
3  C u0 p0 c0 {2,D} {8,S} {9,S}
4  C u1 p0 c0 {1,S} {10,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73942,0.0252916,-4.4878e-06,-7.06403e-09,3.19022e-12,7416.94,11.6476], Tmin=(10,'K'), Tmax=(1109.83,'K')),
            NASAPolynomial(coeffs=[5.75109,0.0246245,-1.24837e-05,3.08381e-09,-2.99639e-13,6564.99,-0.0937527], Tmin=(1109.83,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 151,
    label = "[CH2]C=CC(C)=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,D}
3  C u1 p0 c0 {2,S} {4,S} {10,S}
4  C u0 p0 c0 {3,S} {5,D} {11,S}
5  C u0 p0 c0 {4,D} {12,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u0 p2 c0 {2,D}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71778,0.0257575,6.12621e-05,-1.59011e-07,1.151e-10,-4038.84,11.57], Tmin=(10,'K'), Tmax=(361.53,'K')),
            NASAPolynomial(coeffs=[1.734,0.0477064,-2.98054e-05,8.9204e-09,-1.02671e-12,-3895.4,19.1223], Tmin=(361.53,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 152,
    label = "C[C]=CC=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {4,D} {8,S}
3  C u0 p0 c0 {2,S} {9,D} {10,S}
4  C u1 p0 c0 {1,S} {2,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.57374,0.0455005,-0.000174879,4.42022e-07,-3.79567e-10,14530.8,10.1838], Tmin=(10,'K'), Tmax=(409.94,'K')),
            NASAPolynomial(coeffs=[1.51727,0.0344448,-2.05514e-05,5.86099e-09,-6.45014e-13,14960.9,21.4608], Tmin=(409.94,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 153,
    label = "O=CC1C=CC1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {4,D} {9,S}
4  C u0 p0 c0 {2,S} {3,D} {10,S}
5  C u0 p0 c0 {1,S} {11,D} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 O u0 p2 c0 {5,D}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87506,0.0192287,3.6099e-05,-5.60703e-08,2.19297e-11,4161.11,10.4368], Tmin=(10,'K'), Tmax=(902.49,'K')),
            NASAPolynomial(coeffs=[3.39811,0.0373524,-2.06331e-05,5.49411e-09,-5.69477e-13,3595.22,9.07679], Tmin=(902.49,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 154,
    label = "O=COC=O",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {5,S}
2 O u0 p2 c0 {4,D}
3 O u0 p2 c0 {5,D}
4 C u0 p0 c0 {1,S} {2,D} {6,S}
5 C u0 p0 c0 {1,S} {3,D} {7,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91171,0.0056358,8.97648e-05,-2.0258e-07,1.3518e-10,-59310,9.72886], Tmin=(10,'K'), Tmax=(505.69,'K')),
            NASAPolynomial(coeffs=[3.61647,0.0249605,-1.79512e-05,5.86175e-09,-7.12761e-13,-59497.3,8.80408], Tmin=(505.69,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 155,
    label = "O=[C]CC=O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,D} {7,S}
3 C u1 p0 c0 {1,S} {8,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
7 H u0 p0 c0 {2,S}
8 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53738,0.0462205,-0.000159949,3.25088e-07,-2.39381e-10,-13826.3,10.8599], Tmin=(10,'K'), Tmax=(439.04,'K')),
            NASAPolynomial(coeffs=[4.10059,0.0221477,-1.29887e-05,3.66866e-09,-4.01658e-13,-13693.2,10.6854], Tmin=(439.04,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 156,
    label = "C=C([O])C=O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,D}
2 C u1 p0 c0 {1,S} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {5,D} {8,S}
4 O u0 p2 c0 {1,D}
5 O u0 p2 c0 {3,D}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81933,0.014765,3.46487e-05,-7.09547e-08,3.70116e-11,-13335.6,10.0489], Tmin=(10,'K'), Tmax=(661.26,'K')),
            NASAPolynomial(coeffs=[3.29457,0.0280308,-1.83349e-05,5.54118e-09,-6.34348e-13,-13486.8,10.6952], Tmin=(661.26,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 157,
    label = "[O]OC[C]=O",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {6,S}
3 C u1 p0 c0 {1,S} {7,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u1 p2 c0 {2,S}
7 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.54095,0.0498061,-0.000215893,5.2577e-07,-4.62401e-10,7698.74,10.7416], Tmin=(10,'K'), Tmax=(364.67,'K')),
            NASAPolynomial(coeffs=[4.3214,0.0209859,-1.40135e-05,4.36463e-09,-5.14571e-13,7776.53,9.61077], Tmin=(364.67,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 158,
    label = "C1C([O])C1",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3 C u0 p0 c0 {1,S} {2,S} {4,S} {7,S}
4 O u1 p2 c0 {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.09618,-0.00895684,0.00013887,-2.40456e-07,1.35192e-10,6198.73,8.79595], Tmin=(10,'K'), Tmax=(555.96,'K')),
            NASAPolynomial(coeffs=[0.685842,0.032796,-2.02307e-05,6.02687e-09,-6.9144e-13,6311.86,20.8539], Tmin=(555.96,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 159,
    label = "C[C]=CC(C)=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,S} {12,D}
4  C u0 p0 c0 {3,S} {5,D} {13,S}
5  C u1 p0 c0 {2,S} {4,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 O u0 p2 c0 {3,D}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.50579,0.0529009,-0.000157745,4.06007e-07,-3.68065e-10,7692.49,11.473], Tmin=(10,'K'), Tmax=(391.67,'K')),
            NASAPolynomial(coeffs=[1.48016,0.0463574,-2.84003e-05,8.34514e-09,-9.44684e-13,8060.03,22.0132], Tmin=(391.67,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 160,
    label = "C=CC(O[O])C(C)=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {11,D}
4  C u0 p0 c0 {1,S} {5,D} {12,S}
5  C u0 p0 c0 {4,D} {13,S} {14,S}
6  O u0 p2 c0 {1,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {3,D}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 O u1 p2 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.21693,0.0780175,-0.000161562,2.73828e-07,-1.97909e-10,-11283.4,13.7169], Tmin=(10,'K'), Tmax=(395.54,'K')),
            NASAPolynomial(coeffs=[5.07863,0.0517258,-3.35472e-05,1.035e-08,-1.21912e-12,-11372.3,7.20015], Tmin=(395.54,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 161,
    label = "[CH]=CC(C)=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,D}
3  C u0 p0 c0 {2,S} {4,D} {9,S}
4  C u1 p0 c0 {3,D} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {2,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85088,0.0181834,3.0141e-05,-5.6102e-08,2.51457e-11,13897.3,10.5697], Tmin=(10,'K'), Tmax=(801.61,'K')),
            NASAPolynomial(coeffs=[4.19643,0.0301232,-1.77694e-05,5.00715e-09,-5.44164e-13,13402.8,6.24075], Tmin=(801.61,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 162,
    label = "[CH2]C(=CC=O)O[O]",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {3,D} {5,S}
2  C u1 p0 c0 {1,S} {4,S} {6,S}
3  C u0 p0 c0 {1,D} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {7,D} {10,S}
5  O u0 p2 c0 {1,S} {11,S}
6  H u0 p0 c0 {2,S}
7  O u0 p2 c0 {4,D}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79417,0.0138187,0.000172816,-4.31698e-07,3.12926e-10,9065.86,12.6316], Tmin=(10,'K'), Tmax=(476.63,'K')),
            NASAPolynomial(coeffs=[4.60326,0.0427436,-3.06098e-05,1.00431e-08,-1.23078e-12,8583.05,5.07205], Tmin=(476.63,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 163,
    label = "CC(=O)C=CCO[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {5,D} {13,S}
4  C u0 p0 c0 {2,S} {5,S} {12,D}
5  C u0 p0 c0 {3,D} {4,S} {14,S}
6  O u0 p2 c0 {1,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 O u1 p2 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.19714,0.0908967,-0.000412377,1.21391e-06,-1.22405e-09,-12444.9,13.4573], Tmin=(10,'K'), Tmax=(345.37,'K')),
            NASAPolynomial(coeffs=[0.459042,0.0643235,-4.38196e-05,1.38288e-08,-1.64533e-12,-11908.1,28.7885], Tmin=(345.37,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 164,
    label = "CC(=O)[C]=O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {8,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u1 p2 c0 {2,S}
8 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67275,0.0315379,-7.11468e-05,1.34116e-07,-9.75306e-11,-16196.7,10.3023], Tmin=(10,'K'), Tmax=(455.32,'K')),
            NASAPolynomial(coeffs=[3.42617,0.0239996,-1.43422e-05,4.13495e-09,-4.61559e-13,-16073.7,12.4026], Tmin=(455.32,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 165,
    label = "CC(C)=CO",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {5,S} {12,S}
5  O u0 p2 c0 {4,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.60735,0.0348037,-2.35413e-05,2.81104e-08,-2.01805e-11,-24380.9,10.0137], Tmin=(10,'K'), Tmax=(549.44,'K')),
            NASAPolynomial(coeffs=[1.893,0.0409297,-2.2917e-05,6.30259e-09,-6.79599e-13,-24096.6,18.1306], Tmin=(549.44,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 166,
    label = "[CH2]O[CH]CC",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {5,S} {11,S}
4  C u1 p0 c0 {5,S} {12,S} {13,S}
5  O u0 p2 c0 {3,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.42356,0.0535514,-0.000110522,1.82519e-07,-1.17611e-10,14425.9,12.7412], Tmin=(10,'K'), Tmax=(503.08,'K')),
            NASAPolynomial(coeffs=[3.42577,0.0386448,-2.1684e-05,5.96666e-09,-6.43305e-13,14614.1,14.6046], Tmin=(503.08,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 167,
    label = "C1C(=O)C1",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {2,S} {8,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.10548,-0.00974415,0.000130722,-2.2727e-07,1.28621e-10,583.052,7.36496], Tmin=(10,'K'), Tmax=(554.83,'K')),
            NASAPolynomial(coeffs=[1.12074,0.0284669,-1.77125e-05,5.31157e-09,-6.12354e-13,657.328,17.6909], Tmin=(554.83,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 168,
    label = "[CH]1CCOOC1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {6,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {3,S} {13,S}
5  O u0 p2 c0 {2,S} {6,S}
6  O u0 p2 c0 {3,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95298,0.00288516,0.000141569,-2.5432e-07,1.47569e-10,4942.67,11.2459], Tmin=(10,'K'), Tmax=(444.99,'K')),
            NASAPolynomial(coeffs=[-1.91695,0.0555765,-3.57992e-05,1.10361e-08,-1.30364e-12,5465.81,34.8201], Tmin=(444.99,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 169,
    label = "[CH2]C1CCOO1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  C u1 p0 c0 {2,S} {12,S} {13,S}
5  O u0 p2 c0 {2,S} {6,S}
6  O u0 p2 c0 {3,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86558,0.0192576,5.06662e-05,-7.93196e-08,3.28689e-11,5503.09,11.527], Tmin=(10,'K'), Tmax=(833.49,'K')),
            NASAPolynomial(coeffs=[2.6872,0.0429415,-2.44025e-05,6.67557e-09,-7.08803e-13,5073.28,13.2406], Tmin=(833.49,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 170,
    label = "C=C1COC1",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {10,S} {11,S}
5  O u0 p2 c0 {1,S} {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.02727,-0.00265104,0.000119131,-1.87551e-07,9.43758e-11,722.938,8.70461], Tmin=(10,'K'), Tmax=(601.7,'K')),
            NASAPolynomial(coeffs=[-1.0621,0.0434725,-2.64902e-05,7.74002e-09,-8.70183e-13,1112.91,28.8237], Tmin=(601.7,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 171,
    label = "C=CC(=C)[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,D} {6,S}
2  C u0 p0 c0 {1,S} {3,D} {5,S}
3  C u0 p0 c0 {2,D} {9,S} {10,S}
4  C u0 p0 c0 {1,D} {7,S} {8,S}
5  O u1 p2 c0 {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82339,0.0155279,5.10319e-05,-1.00874e-07,5.46917e-11,6858.54,9.92846], Tmin=(10,'K'), Tmax=(612.45,'K')),
            NASAPolynomial(coeffs=[2.61347,0.0341784,-2.09714e-05,6.1587e-09,-6.95903e-13,6805.16,13.5267], Tmin=(612.45,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 172,
    label = "C=C=C(C)O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,D} {5,S}
3  C u0 p0 c0 {4,D} {9,S} {10,S}
4  C u0 p0 c0 {2,D} {3,D}
5  O u0 p2 c0 {2,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86489,0.00871485,0.00014012,-3.23566e-07,2.22701e-10,-2810.06,9.68155], Tmin=(10,'K'), Tmax=(494.36,'K')),
            NASAPolynomial(coeffs=[3.9871,0.0349801,-2.227e-05,6.94363e-09,-8.35233e-13,-3155.17,5.80975], Tmin=(494.36,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 173,
    label = "C=C=CO",
    molecule = 
"""
1 C u0 p0 c0 {3,D} {4,S} {5,S}
2 C u0 p0 c0 {3,D} {6,S} {7,S}
3 C u0 p0 c0 {1,D} {2,D}
4 O u0 p2 c0 {1,S} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91761,0.00479904,8.51902e-05,-1.69941e-07,1.00295e-10,3001.76,7.91698], Tmin=(10,'K'), Tmax=(577.67,'K')),
            NASAPolynomial(coeffs=[3.8452,0.0246401,-1.65479e-05,5.42559e-09,-6.79962e-13,2687.44,5.43362], Tmin=(577.67,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 174,
    label = "[CH]=C=C(C)O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  C u0 p0 c0 {2,S} {5,T}
4  O u0 p2 c0 {2,S} {9,S}
5  C u0 p0 c0 {3,T} {10,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80142,0.0156238,0.000135384,-4.27555e-07,3.87272e-10,14167.4,10.2896], Tmin=(10,'K'), Tmax=(385.85,'K')),
            NASAPolynomial(coeffs=[4.67506,0.031122,-2.03249e-05,6.41515e-09,-7.74606e-13,13917.2,4.53817], Tmin=(385.85,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 175,
    label = "C=C(CO[O])COO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {2,S} {14,S}
7  O u0 p2 c0 {5,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 O u1 p2 c0 {6,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.91987,0.113366,-0.000436734,9.65176e-07,-7.73937e-10,-6080.76,15.4618], Tmin=(10,'K'), Tmax=(398.9,'K')),
            NASAPolynomial(coeffs=[4.90779,0.0493544,-3.02833e-05,8.88663e-09,-1.00353e-12,-5888.67,12.0939], Tmin=(398.9,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 176,
    label = "CC=[C]CC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {5,D} {14,S}
5  C u1 p0 c0 {1,S} {4,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49305,0.0493423,-0.000119104,2.52999e-07,-1.89767e-10,22164.9,11.2669], Tmin=(10,'K'), Tmax=(477.86,'K')),
            NASAPolynomial(coeffs=[0.790982,0.0456768,-2.50918e-05,6.7342e-09,-7.08271e-13,22723.2,25.4474], Tmin=(477.86,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 177,
    label = "[CH2]C(C)=CC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,S} {5,D}
4  C u1 p0 c0 {2,S} {3,S} {12,S}
5  C u0 p0 c0 {3,D} {13,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78684,0.0225805,3.23476e-05,-4.96698e-08,1.8733e-11,10384.3,11.0487], Tmin=(10,'K'), Tmax=(917.82,'K')),
            NASAPolynomial(coeffs=[1.9131,0.0436626,-2.32159e-05,6.02184e-09,-6.12841e-13,10184.2,16.9641], Tmin=(917.82,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 178,
    label = "C=C(O)[C](C)O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {5,S}
3  C u0 p0 c0 {2,D} {4,S} {6,S}
4  C u1 p0 c0 {3,S} {10,S} {11,S}
5  O u0 p2 c0 {2,S} {12,S}
6  O u0 p2 c0 {3,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85097,0.0138316,0.000195652,-6.12731e-07,6.32097e-10,-30914.7,12.4349], Tmin=(10,'K'), Tmax=(246.15,'K')),
            NASAPolynomial(coeffs=[1.52562,0.0516189,-3.46178e-05,1.09224e-08,-1.30821e-12,-30800.2,20.3937], Tmin=(246.15,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 179,
    label = "[CH2][CH]C=CC=O",
    molecule = 
"""
multiplicity 3
1  C u1 p0 c0 {2,S} {3,S} {7,S}
2  C u1 p0 c0 {1,S} {5,S} {8,S}
3  C u0 p0 c0 {1,S} {4,D} {6,S}
4  C u0 p0 c0 {3,D} {10,S} {11,S}
5  C u0 p0 c0 {2,S} {9,D} {12,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {5,D}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90677,0.00976857,0.000277261,-1.2206e-06,1.85788e-09,22443.7,11.7728], Tmin=(10,'K'), Tmax=(165.28,'K')),
            NASAPolynomial(coeffs=[2.51977,0.0433369,-2.73972e-05,8.28456e-09,-9.63105e-13,22489.6,15.9675], Tmin=(165.28,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 180,
    label = "C=C1COOC1",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {2,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95724,0.00259029,0.000128247,-2.26678e-07,1.28858e-10,-2610.02,10.0116], Tmin=(10,'K'), Tmax=(456.23,'K')),
            NASAPolynomial(coeffs=[-1.66772,0.0519356,-3.40844e-05,1.06658e-08,-1.27407e-12,-2097.06,32.7313], Tmin=(456.23,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 181,
    label = "[O]OCC1CCOO1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {3,S} {5,S}
7  O u0 p2 c0 {4,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u1 p2 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65783,0.0434262,-2.28055e-06,-2.22918e-08,9.90478e-12,-12832.3,13.2306], Tmin=(10,'K'), Tmax=(1033.76,'K')),
            NASAPolynomial(coeffs=[8.73958,0.0402375,-2.15583e-05,5.55633e-09,-5.57997e-13,-14763.3,-15.7123], Tmin=(1033.76,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 182,
    label = "CC1(O[O])COOC1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {2,S} {6,S}
6  O u0 p2 c0 {3,S} {5,S}
7  O u0 p2 c0 {1,S} {15,S}
8  H u0 p0 c0 {2,S}
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
            NASAPolynomial(coeffs=[3.66217,0.0287119,9.3737e-05,-2.16068e-07,1.35398e-10,-14470.6,13.7142], Tmin=(10,'K'), Tmax=(535.51,'K')),
            NASAPolynomial(coeffs=[2.54077,0.0559782,-3.555e-05,1.07557e-08,-1.24551e-12,-14621.3,15.895], Tmin=(535.51,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 183,
    label = "CCC(C)CO[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
6  O u0 p2 c0 {3,S} {18,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 O u1 p2 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.22199,0.0810022,-0.000238362,5.52172e-07,-4.58737e-10,-14769.9,14.946], Tmin=(10,'K'), Tmax=(415.5,'K')),
            NASAPolynomial(coeffs=[1.15297,0.0631204,-3.73422e-05,1.06794e-08,-1.1839e-12,-14271.7,27.0371], Tmin=(415.5,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 184,
    label = "CCC(=CO)CO",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {6,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {2,S} {5,D}
5  C u0 p0 c0 {4,D} {7,S} {15,S}
6  O u0 p2 c0 {2,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90565,0.0386137,2.93243e-05,-5.45923e-08,1.98116e-11,-46511.1,10.8517], Tmin=(10,'K'), Tmax=(1087.61,'K')),
            NASAPolynomial(coeffs=[11.6571,0.0434572,-2.33541e-05,5.89321e-09,-5.72799e-13,-50169.8,-36.2641], Tmin=(1087.61,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 185,
    label = "CCC(C=O)CO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {15,D} {16,S}
6  O u0 p2 c0 {3,S} {17,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u0 p2 c0 {5,D}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.42337,0.0515568,6.3095e-06,-5.7106e-08,3.24141e-11,-50417.6,12.4281], Tmin=(10,'K'), Tmax=(727.76,'K')),
            NASAPolynomial(coeffs=[5.94968,0.0540388,-3.25413e-05,9.3863e-09,-1.04303e-12,-51218.8,-1.93489], Tmin=(727.76,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 186,
    label = "CCC([CH]O)C=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {6,S} {13,S}
5  C u0 p0 c0 {1,S} {14,D} {15,S}
6  O u0 p2 c0 {4,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 O u0 p2 c0 {5,D}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63608,0.0496385,-7.84559e-06,-2.03014e-08,9.56578e-12,-28657,12.463], Tmin=(10,'K'), Tmax=(1065.81,'K')),
            NASAPolynomial(coeffs=[11.4968,0.0397696,-2.1587e-05,5.57702e-09,-5.58388e-13,-31447.7,-31.1925], Tmin=(1065.81,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 187,
    label = "CC[C](C[O])CO",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {5,S} {6,S} {9,S} {13,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
5  C u1 p0 c0 {1,S} {2,S} {4,S}
6  O u0 p2 c0 {2,S} {17,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {2,S}
14 O u1 p2 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.84659,0.0881963,-0.000153292,1.656e-07,-7.02781e-11,-9065.58,14.0868], Tmin=(10,'K'), Tmax=(712.89,'K')),
            NASAPolynomial(coeffs=[6.42883,0.0479258,-2.61171e-05,6.9822e-09,-7.34512e-13,-9063.78,1.61174], Tmin=(712.89,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 188,
    label = "CCC([CH]O)[CH]O",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {7,S} {14,S}
5  C u1 p0 c0 {1,S} {6,S} {15,S}
6  O u0 p2 c0 {5,S} {17,S}
7  O u0 p2 c0 {4,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.37134,0.0552799,2.01413e-05,-1.07318e-07,6.97e-11,-16186.7,13.2285], Tmin=(10,'K'), Tmax=(620.42,'K')),
            NASAPolynomial(coeffs=[6.67375,0.056259,-3.60691e-05,1.09386e-08,-1.26465e-12,-17025.1,-4.58159], Tmin=(620.42,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 189,
    label = "C[CH]C(C[O])CO",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
5  C u1 p0 c0 {1,S} {4,S} {16,S}
6  O u0 p2 c0 {2,S} {17,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u1 p2 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.12297,0.0884724,-0.000234929,4.7054e-07,-3.61318e-10,-8220.7,14.054], Tmin=(10,'K'), Tmax=(417.31,'K')),
            NASAPolynomial(coeffs=[3.80151,0.0574213,-3.50847e-05,1.03261e-08,-1.17275e-12,-8063.59,13.9344], Tmin=(417.31,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 190,
    label = "CC[C]([CH]O)CO",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {6,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {2,S} {5,S}
5  C u1 p0 c0 {4,S} {7,S} {15,S}
6  O u0 p2 c0 {2,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.2917,0.0632928,-3.84964e-05,5.28758e-09,2.50316e-12,-13762.9,13.3996], Tmin=(10,'K'), Tmax=(954.15,'K')),
            NASAPolynomial(coeffs=[9.91272,0.0452816,-2.55022e-05,6.9132e-09,-7.27569e-13,-15470,-20.5569], Tmin=(954.15,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 191,
    label = "[CH2]CC(C[O])CO",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  C u1 p0 c0 {2,S} {15,S} {16,S}
6  O u0 p2 c0 {3,S} {17,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u1 p2 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.15244,0.0778186,-0.000121711,1.55858e-07,-8.90657e-11,-7078.68,14.0645], Tmin=(10,'K'), Tmax=(488.01,'K')),
            NASAPolynomial(coeffs=[5.15027,0.0553169,-3.37166e-05,9.92628e-09,-1.12891e-12,-7200.72,6.60686], Tmin=(488.01,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 192,
    label = "[CH2]CC([CH]O)CO",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {7,S} {13,S}
5  C u1 p0 c0 {2,S} {14,S} {15,S}
6  O u0 p2 c0 {3,S} {16,S}
7  O u0 p2 c0 {4,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95855,0.0447568,2.60937e-05,-6.16077e-08,2.4707e-11,-12940.7,12.5402], Tmin=(10,'K'), Tmax=(1016.24,'K')),
            NASAPolynomial(coeffs=[13.761,0.0424239,-2.39697e-05,6.33581e-09,-6.42511e-13,-16804.9,-44.1186], Tmin=(1016.24,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 193,
    label = "C=CCC=CC",
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
            NASAPolynomial(coeffs=[3.31044,0.0643248,-0.00014776,2.77501e-07,-1.91268e-10,6550.98,11.2662], Tmin=(10,'K'), Tmax=(500.66,'K')),
            NASAPolynomial(coeffs=[1.24954,0.0527762,-2.92277e-05,7.90165e-09,-8.36552e-13,7108.44,23.2894], Tmin=(500.66,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 194,
    label = "[O]OC1COOC1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  O u0 p2 c0 {2,S} {5,S}
5  O u0 p2 c0 {3,S} {4,S}
6  O u0 p2 c0 {1,S} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u1 p2 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93299,0.0220235,3.64297e-05,-6.01074e-08,2.38252e-11,-8511.75,12.3931], Tmin=(10,'K'), Tmax=(925.67,'K')),
            NASAPolynomial(coeffs=[5.6788,0.0357102,-2.0152e-05,5.41993e-09,-5.63792e-13,-9744.54,-0.80771], Tmin=(925.67,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 195,
    label = "CC(CCO[O])OO",
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
            NASAPolynomial(coeffs=[3.04695,0.0963156,-0.000243087,4.63909e-07,-3.54748e-10,-24128.4,14.9136], Tmin=(10,'K'), Tmax=(394.82,'K')),
            NASAPolynomial(coeffs=[5.12274,0.0587932,-3.78755e-05,1.16055e-08,-1.35897e-12,-24163.8,8.45609], Tmin=(394.82,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 196,
    label = "[CH2]C(=O)COO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,D}
3  C u1 p0 c0 {2,S} {9,S} {10,S}
4  O u0 p2 c0 {1,S} {5,S}
5  O u0 p2 c0 {4,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {2,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.51768,0.0459627,-4.29309e-05,2.23702e-08,-5.05141e-12,-15721.4,11.7462], Tmin=(10,'K'), Tmax=(950.11,'K')),
            NASAPolynomial(coeffs=[7.1304,0.0307529,-1.89182e-05,5.52105e-09,-6.17942e-13,-16407.9,-5.49823], Tmin=(950.11,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 197,
    label = "[CH2]C(=O)C(C)[O]",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,S} {10,D}
4  C u1 p0 c0 {3,S} {11,S} {12,S}
5  O u1 p2 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89332,0.0117509,0.000338891,-1.7217e-06,2.8715e-09,-1502.62,12.1921], Tmin=(10,'K'), Tmax=(188.63,'K')),
            NASAPolynomial(coeffs=[3.19322,0.0421641,-2.6751e-05,8.09772e-09,-9.41627e-13,-1503.9,13.6678], Tmin=(188.63,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 198,
    label = "C=C1OOC1C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {6,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {3,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90707,0.00604469,0.00014913,-3.19261e-07,2.13482e-10,1820.66,11.091], Tmin=(10,'K'), Tmax=(473.37,'K')),
            NASAPolynomial(coeffs=[1.44945,0.0443697,-2.79499e-05,8.48452e-09,-9.91376e-13,1856.62,19.0318], Tmin=(473.37,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 199,
    label = "[O]OC1CCOOC1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
5  O u0 p2 c0 {4,S} {6,S}
6  O u0 p2 c0 {3,S} {5,S}
7  O u0 p2 c0 {1,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 O u1 p2 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78656,0.0259082,6.63373e-05,-1.14841e-07,5.18819e-11,-14130.9,12.9716], Tmin=(10,'K'), Tmax=(770.94,'K')),
            NASAPolynomial(coeffs=[3.10532,0.0527765,-3.13399e-05,8.88487e-09,-9.71105e-13,-14719.3,11.5838], Tmin=(770.94,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 200,
    label = "CC1OOCC1O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {9,S}
3  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {3,S} {5,S}
7  O u0 p2 c0 {2,S} {15,S}
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
            NASAPolynomial(coeffs=[3.68604,0.0355461,2.83983e-05,-6.3236e-08,2.79554e-11,-14098.4,13.7111], Tmin=(10,'K'), Tmax=(849.73,'K')),
            NASAPolynomial(coeffs=[5.20312,0.0478429,-2.76227e-05,7.63738e-09,-8.16922e-13,-15057.9,2.50976], Tmin=(849.73,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 201,
    label = "CC(OO)C(=O)CO[O]",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {6,S}
2  O u0 p2 c0 {5,S} {8,S}
3  O u0 p2 c0 {1,S} {16,S}
4  O u0 p2 c0 {9,D}
5  O u1 p2 c0 {2,S}
6  C u0 p0 c0 {1,S} {7,S} {9,S} {10,S}
7  C u0 p0 c0 {6,S} {11,S} {12,S} {13,S}
8  C u0 p0 c0 {2,S} {9,S} {14,S} {15,S}
9  C u0 p0 c0 {4,D} {6,S} {8,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.28018,0.0769409,0.000112592,-1.15688e-06,1.95401e-09,-33911.1,15.2316], Tmin=(10,'K'), Tmax=(246.72,'K')),
            NASAPolynomial(coeffs=[7.45133,0.0555907,-3.89478e-05,1.28259e-08,-1.59226e-12,-34257.8,-1.90852], Tmin=(246.72,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 202,
    label = "[O]OCC(=O)COO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {6,S}
2  O u0 p2 c0 {5,S} {7,S}
3  O u0 p2 c0 {1,S} {13,S}
4  O u0 p2 c0 {8,D}
5  O u1 p2 c0 {2,S}
6  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
7  C u0 p0 c0 {2,S} {8,S} {11,S} {12,S}
8  C u0 p0 c0 {4,D} {6,S} {7,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.29318,0.0644476,7.98934e-06,-2.72384e-07,3.21896e-10,-28804,14.0264], Tmin=(10,'K'), Tmax=(386.36,'K')),
            NASAPolynomial(coeffs=[8.61511,0.0417582,-2.9748e-05,9.85144e-09,-1.22293e-12,-29457.1,-9.71806], Tmin=(386.36,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 203,
    label = "CCC(CC)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
4  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
6  O u0 p2 c0 {1,S} {18,S}
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
17 H u0 p0 c0 {5,S}
18 O u1 p2 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.20957,0.0677256,-7.1607e-05,6.61725e-08,-3.07186e-11,-16611.3,13.2841], Tmin=(10,'K'), Tmax=(588.35,'K')),
            NASAPolynomial(coeffs=[4.13047,0.0569798,-3.27761e-05,9.21627e-09,-1.01146e-12,-16642.1,9.9894], Tmin=(588.35,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 204,
    label = "C=C=CC(C)[CH]C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
4  C u1 p0 c0 {1,S} {3,S} {15,S}
5  C u0 p0 c0 {1,S} {7,D} {16,S}
6  C u0 p0 c0 {7,D} {17,S} {18,S}
7  C u0 p0 c0 {5,D} {6,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.12184,0.0777397,-0.000135905,1.92291e-07,-1.10792e-10,31451.9,13.9697], Tmin=(10,'K'), Tmax=(546.06,'K')),
            NASAPolynomial(coeffs=[3.70942,0.0566247,-3.17251e-05,8.72492e-09,-9.40828e-13,31638.3,13.7853], Tmin=(546.06,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 205,
    label = "C=C=CO[O]",
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
            NASAPolynomial(coeffs=[3.87884,0.00801202,0.000108123,-2.67672e-07,1.93224e-10,30041.5,9.84524], Tmin=(10,'K'), Tmax=(480.92,'K')),
            NASAPolynomial(coeffs=[4.62143,0.0249443,-1.67658e-05,5.36884e-09,-6.53759e-13,29702.8,4.02796], Tmin=(480.92,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 206,
    label = "C_CCO[O]",
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
            NASAPolynomial(coeffs=[3.82271,0.0231944,-1.15406e-05,1.04567e-09,5.41221e-13,30495,10.2407], Tmin=(10,'K'), Tmax=(1289.36,'K')),
            NASAPolynomial(coeffs=[8.49677,0.0137559,-6.44883e-06,1.45776e-09,-1.29041e-13,28868.9,-15.1284], Tmin=(1289.36,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 207,
    label = "C#CCC=[C]C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,D} {12,S}
4  C u1 p0 c0 {2,S} {3,D}
5  C u0 p0 c0 {1,S} {6,T}
6  C u0 p0 c0 {5,T} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.5,0.0472328,-7.61345e-05,1.28858e-07,-9.04184e-11,55905.9,12.1287], Tmin=(10,'K'), Tmax=(480.29,'K')),
            NASAPolynomial(coeffs=[2.69495,0.0423287,-2.45621e-05,6.94658e-09,-7.65456e-13,56117.2,16.8162], Tmin=(480.29,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 208,
    label = "C=C=CC[CH]C=C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u1 p0 c0 {1,S} {4,S} {10,S}
3  C u0 p0 c0 {1,S} {7,D} {11,S}
4  C u0 p0 c0 {2,S} {5,D} {12,S}
5  C u0 p0 c0 {4,D} {13,S} {14,S}
6  C u0 p0 c0 {7,D} {15,S} {16,S}
7  C u0 p0 c0 {3,D} {6,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.18132,0.0728796,-0.000136254,2.01681e-07,-1.1991e-10,41076.3,12.8257], Tmin=(10,'K'), Tmax=(533.24,'K')),
            NASAPolynomial(coeffs=[3.62715,0.0523283,-3.004e-05,8.37576e-09,-9.11018e-13,41273.4,13.249], Tmin=(533.24,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 209,
    label = "[CH2]C_CC=O",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {3,S} {6,S} {7,S}
2 C u0 p0 c0 {4,S} {5,D} {8,S}
3 C u0 p0 c0 {1,S} {4,T}
4 C u0 p0 c0 {2,S} {3,T}
5 O u0 p2 c0 {2,D}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89574,0.011329,0.000189902,-1.0167e-06,1.68471e-09,26818.9,9.54796], Tmin=(10,'K'), Tmax=(202.87,'K')),
            NASAPolynomial(coeffs=[3.93137,0.0248737,-1.55851e-05,4.71748e-09,-5.50701e-13,26788.1,8.71028], Tmin=(202.87,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 210,
    label = "C#CC[C]=O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {4,T}
3 C u1 p0 c0 {1,S} {7,D}
4 C u0 p0 c0 {2,T} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {3,D}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.60487,0.0393787,-0.000109038,2.0959e-07,-1.53345e-10,29004.4,10.2833], Tmin=(10,'K'), Tmax=(431.6,'K')),
            NASAPolynomial(coeffs=[4.21918,0.0228161,-1.36991e-05,3.97633e-09,-4.46797e-13,29052.6,9.00863], Tmin=(431.6,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 211,
    label = "C=C=CCC=C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,D} {9,S}
3  C u0 p0 c0 {1,S} {6,D} {10,S}
4  C u0 p0 c0 {2,D} {11,S} {12,S}
5  C u0 p0 c0 {6,D} {13,S} {14,S}
6  C u0 p0 c0 {3,D} {5,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.45492,0.0506806,-8.1259e-05,1.36036e-07,-9.33914e-11,27769.6,11.0968], Tmin=(10,'K'), Tmax=(495.35,'K')),
            NASAPolynomial(coeffs=[2.36859,0.0460064,-2.6387e-05,7.38756e-09,-8.07272e-13,28042.2,17.2398], Tmin=(495.35,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 212,
    label = "C_CCCC=C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {3,D} {12,S} {13,S}
5  C u0 p0 c0 {2,S} {6,T}
6  C u0 p0 c0 {5,T} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.51748,0.0402127,-1.17941e-05,-7.82411e-09,4.62841e-12,27979.7,11.8524], Tmin=(10,'K'), Tmax=(975.79,'K')),
            NASAPolynomial(coeffs=[5.24648,0.0397205,-2.11758e-05,5.51217e-09,-5.62976e-13,27328.3,1.94442], Tmin=(975.79,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 213,
    label = "[CH2]C(CO)OO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {4,S}
2  O u0 p2 c0 {5,S} {12,S}
3  O u0 p2 c0 {1,S} {13,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
6  C u1 p0 c0 {4,S} {10,S} {11,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.62957,0.0271931,0.000207382,-6.59036e-07,5.66841e-10,-20513,10.7435], Tmin=(10,'K'), Tmax=(426.74,'K')),
            NASAPolynomial(coeffs=[8.21092,0.039126,-2.74516e-05,9.16588e-09,-1.15109e-12,-21403.7,-13.3119], Tmin=(426.74,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 214,
    label = "C3H4Ob",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {4,T}
3 O u0 p2 c0 {1,S} {7,S}
4 C u0 p0 c0 {2,T} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.79887,0.0225818,-8.01311e-06,-3.43729e-09,2.32957e-12,3315.59,12.9758], Tmin=(100,'K'), Tmax=(1089.7,'K')),
            NASAPolynomial(coeffs=[7.21412,0.0135296,-5.40154e-06,9.90482e-10,-6.86284e-14,1928.52,-10.6537], Tmin=(1089.7,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 215,
    label = "CC1OCC1CO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {7,S} {10,S} {11,S}
5  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
6  O u0 p2 c0 {2,S} {3,S}
7  O u0 p2 c0 {4,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86686,0.0386966,9.35312e-06,-2.60568e-08,8.97636e-12,-40073.6,13.208], Tmin=(10,'K'), Tmax=(1208.86,'K')),
            NASAPolynomial(coeffs=[10.711,0.0381388,-1.73635e-05,3.79233e-09,-3.22565e-13,-43342.3,-27.785], Tmin=(1208.86,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 216,
    label = "C=C=CC=C=C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,D} {7,S}
2  C u0 p0 c0 {1,S} {6,D} {8,S}
3  C u0 p0 c0 {5,D} {9,S} {10,S}
4  C u0 p0 c0 {6,D} {11,S} {12,S}
5  C u0 p0 c0 {1,D} {3,D}
6  C u0 p0 c0 {2,D} {4,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85296,0.0092584,0.000159268,-3.51737e-07,2.32164e-10,46286.9,9.52492], Tmin=(10,'K'), Tmax=(511.59,'K')),
            NASAPolynomial(coeffs=[3.51375,0.0424741,-2.7735e-05,8.7305e-09,-1.05284e-12,45921.6,7.02506], Tmin=(511.59,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 217,
    label = "C_CCC=C=C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,D} {9,S}
3  C u0 p0 c0 {4,D} {10,S} {11,S}
4  C u0 p0 c0 {2,D} {3,D}
5  C u0 p0 c0 {1,S} {6,T}
6  C u0 p0 c0 {5,T} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84083,0.0142759,0.0001874,-6.43891e-07,6.92032e-10,48457.8,11.6823], Tmin=(10,'K'), Tmax=(298.71,'K')),
            NASAPolynomial(coeffs=[3.02156,0.0409737,-2.56395e-05,7.82815e-09,-9.23383e-13,48436.6,13.4704], Tmin=(298.71,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 218,
    label = "C_CCCC_C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,T}
4  C u0 p0 c0 {2,S} {6,T}
5  C u0 p0 c0 {3,T} {11,S}
6  C u0 p0 c0 {4,T} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80687,0.0143275,0.000184248,-5.38154e-07,4.64448e-10,48242.5,9.34375], Tmin=(10,'K'), Tmax=(400.39,'K')),
            NASAPolynomial(coeffs=[4.69197,0.0375597,-2.29498e-05,6.91319e-09,-8.1165e-13,47914.5,2.67319], Tmin=(400.39,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 219,
    label = "[CH2]C1(C)OO1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u1 p0 c0 {1,S} {9,S} {10,S}
4  O u0 p2 c0 {1,S} {5,S}
5  O u0 p2 c0 {1,S} {4,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87703,0.00806259,0.000129314,-3.04661e-07,2.14361e-10,9248.22,9.83681], Tmin=(10,'K'), Tmax=(481.91,'K')),
            NASAPolynomial(coeffs=[3.86976,0.032185,-2.06652e-05,6.42553e-09,-7.68689e-13,8969.51,6.96761], Tmin=(481.91,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 220,
    label = "CC=C1COO1",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,D} {6,S}
4  C u0 p0 c0 {2,S} {3,D} {12,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {3,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91131,0.023116,1.86809e-05,-3.19949e-08,1.13675e-11,3855.15,9.71252], Tmin=(10,'K'), Tmax=(1068.78,'K')),
            NASAPolynomial(coeffs=[6.04496,0.0314617,-1.59521e-05,3.90484e-09,-3.74048e-13,2466.34,-5.08657], Tmin=(1068.78,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 221,
    label = "CC=C1CO1",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {5,S}
4  C u0 p0 c0 {2,S} {3,D} {11,S}
5  O u0 p2 c0 {1,S} {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86176,0.0158161,3.32068e-05,-5.04404e-08,1.99464e-11,1977.58,9.14742], Tmin=(10,'K'), Tmax=(863.93,'K')),
            NASAPolynomial(coeffs=[2.30029,0.0344381,-1.89055e-05,5.0363e-09,-5.23984e-13,1822.23,13.9917], Tmin=(863.93,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 222,
    label = "C=C1OC1C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {5,S}
4  C u0 p0 c0 {3,D} {10,S} {11,S}
5  O u0 p2 c0 {1,S} {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9412,0.00386542,0.000125638,-2.61747e-07,1.74494e-10,80.7848,9.96683], Tmin=(10,'K'), Tmax=(454.1,'K')),
            NASAPolynomial(coeffs=[1.13855,0.0387959,-2.35808e-05,6.99524e-09,-8.06516e-13,229.713,20.1126], Tmin=(454.1,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 223,
    label = "C=CC(=C)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,D} {5,S}
2  C u0 p0 c0 {1,S} {4,D} {6,S}
3  C u0 p0 c0 {1,D} {7,S} {8,S}
4  C u0 p0 c0 {2,D} {9,S} {10,S}
5  O u0 p2 c0 {1,S} {11,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81897,0.0109882,0.000152218,-3.39991e-07,2.18367e-10,18092,11.137], Tmin=(10,'K'), Tmax=(548.57,'K')),
            NASAPolynomial(coeffs=[5.94269,0.0355941,-2.4689e-05,8.22389e-09,-1.0389e-12,17255.8,-3.33186], Tmin=(548.57,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 224,
    label = "[C]1=COOC1",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2 C u0 p0 c0 {3,D} {5,S} {8,S}
3 C u1 p0 c0 {1,S} {2,D}
4 O u0 p2 c0 {1,S} {5,S}
5 O u0 p2 c0 {2,S} {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9744,0.00158427,8.30518e-05,-1.50508e-07,8.76291e-11,35108.2,10.8501], Tmin=(10,'K'), Tmax=(443.6,'K')),
            NASAPolynomial(coeffs=[0.500384,0.0328017,-2.21416e-05,7.0324e-09,-8.46133e-13,35417.5,24.7984], Tmin=(443.6,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 225,
    label = "C=[C]C1OO1",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,D} {7,S} {8,S}
3 C u1 p0 c0 {1,S} {2,D}
4 O u0 p2 c0 {1,S} {5,S}
5 O u0 p2 c0 {1,S} {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84946,0.0157679,1.81593e-05,-3.84602e-08,1.79681e-11,34954.7,10.7253], Tmin=(10,'K'), Tmax=(781.59,'K')),
            NASAPolynomial(coeffs=[4.22022,0.0231269,-1.37286e-05,3.89163e-09,-4.25333e-13,34614,7.21925], Tmin=(781.59,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 226,
    label = "C=C=[C]O[O]",
    molecule = 
"""
multiplicity 3
1 C u1 p0 c0 {2,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {4,S}
4 O u0 p2 c0 {3,S} {7,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u1 p2 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81802,0.0146407,9.89508e-05,-3.57135e-07,3.48964e-10,56161.7,10.4229], Tmin=(10,'K'), Tmax=(373.08,'K')),
            NASAPolynomial(coeffs=[5.35269,0.0204496,-1.39155e-05,4.50114e-09,-5.52237e-13,55892.2,2.45572], Tmin=(373.08,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 227,
    label = "C=C=C(C=O)O[O]",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {4,S}
2  O u0 p2 c0 {5,D}
3  O u1 p2 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {7,D}
5  C u0 p0 c0 {2,D} {4,S} {8,S}
6  C u0 p0 c0 {7,D} {9,S} {10,S}
7  C u0 p0 c0 {4,D} {6,D}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70289,0.0276984,0.000167454,-7.97329e-07,1.01053e-09,16523.7,11.7995], Tmin=(10,'K'), Tmax=(289.14,'K')),
            NASAPolynomial(coeffs=[5.45503,0.033967,-2.33396e-05,7.5189e-09,-9.16519e-13,16294.9,3.31529], Tmin=(289.14,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 228,
    label = "[CH]=C(O)CC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,S} {5,D}
4  O u0 p2 c0 {3,S} {11,S}
5  C u1 p0 c0 {3,D} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87945,0.0080114,0.000152634,-3.47024e-07,2.41586e-10,6032.99,11.4934], Tmin=(10,'K'), Tmax=(468.56,'K')),
            NASAPolynomial(coeffs=[2.3752,0.0426006,-2.77169e-05,8.63423e-09,-1.02585e-12,5935.21,15.0627], Tmin=(468.56,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 229,
    label = "[CH2]CC(=C)O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {5,S}
3  C u1 p0 c0 {1,S} {8,S} {9,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  O u0 p2 c0 {2,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73271,0.0244124,4.89321e-05,-1.51382e-07,1.28725e-10,377.185,12.9913], Tmin=(10,'K'), Tmax=(305.54,'K')),
            NASAPolynomial(coeffs=[2.6042,0.0391868,-2.36022e-05,6.88625e-09,-7.77296e-13,446.145,17.0976], Tmin=(305.54,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 230,
    label = "[CH2]CC(CC)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  C u1 p0 c0 {3,S} {16,S} {17,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {6,S} {18,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.89802,0.0810464,-9.63448e-05,7.22065e-08,-2.30408e-11,-8043.81,14.5293], Tmin=(10,'K'), Tmax=(845,'K')),
            NASAPolynomial(coeffs=[7.92725,0.0497691,-2.75623e-05,7.47823e-09,-7.95157e-13,-8627.05,-7.30877], Tmin=(845,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 231,
    label = "CCC(=O)CO[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {2,S} {13,D}
5  O u0 p2 c0 {2,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 O u0 p2 c0 {4,D}
14 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68822,0.0356718,0.000348761,-2.35051e-06,4.40939e-09,-22868.7,12.7137], Tmin=(10,'K'), Tmax=(194.28,'K')),
            NASAPolynomial(coeffs=[5.24133,0.0440285,-2.71755e-05,8.15668e-09,-9.4751e-13,-23005.2,5.80657], Tmin=(194.28,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 232,
    label = "C=C([O])O[O]",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,S} {3,S} {4,D}
2 C u1 p0 c0 {1,S} {5,S} {6,S}
3 O u0 p2 c0 {1,S} {7,S}
4 O u0 p2 c0 {1,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 O u1 p2 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87323,0.00825152,9.99302e-05,-2.50012e-07,1.78149e-10,1776.54,10.549], Tmin=(10,'K'), Tmax=(496.22,'K')),
            NASAPolynomial(coeffs=[5.20097,0.0220722,-1.59788e-05,5.30539e-09,-6.58327e-13,1342.84,2.03151], Tmin=(496.22,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 233,
    label = "[CH2]C(=C)C(=C)[O]",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {3,S} {4,D}
2  C u0 p0 c0 {1,S} {5,S} {6,D}
3  C u1 p0 c0 {1,S} {9,S} {10,S}
4  C u0 p0 c0 {1,D} {11,S} {12,S}
5  C u1 p0 c0 {2,S} {7,S} {8,S}
6  O u0 p2 c0 {2,D}
7  H u0 p0 c0 {5,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84845,0.00977685,0.00016378,-3.75206e-07,2.57133e-10,20949.4,13.0313], Tmin=(10,'K'), Tmax=(492.91,'K')),
            NASAPolynomial(coeffs=[3.61369,0.0421199,-2.72736e-05,8.4803e-09,-1.0136e-12,20602.8,10.2471], Tmin=(492.91,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 234,
    label = "C=C([O])C[O]",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {7,D}
3 C u1 p0 c0 {2,S} {8,S} {9,S}
4 O u1 p2 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {2,D}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86179,0.0162563,3.56917e-05,-6.80234e-08,3.24234e-11,3824.33,11.2527], Tmin=(10,'K'), Tmax=(749.49,'K')),
            NASAPolynomial(coeffs=[4.30385,0.0283775,-1.75476e-05,5.11023e-09,-5.69338e-13,3351.35,6.53426], Tmin=(749.49,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 235,
    label = "O=C=CC=O",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 C u0 p0 c0 {1,S} {5,D} {6,S}
3 C u0 p0 c0 {1,D} {7,D}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {2,D}
6 H u0 p0 c0 {2,S}
7 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91089,0.00767159,7.10206e-05,-2.05369e-07,1.91808e-10,-21872.4,8.86864], Tmin=(10,'K'), Tmax=(272.75,'K')),
            NASAPolynomial(coeffs=[2.84657,0.0232804,-1.48212e-05,4.44987e-09,-5.10874e-13,-21814.3,12.6206], Tmin=(272.75,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 236,
    label = "[CH2]O[CH]C",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u1 p0 c0 {1,S} {4,S} {8,S}
3  C u1 p0 c0 {4,S} {9,S} {10,S}
4  O u0 p2 c0 {2,S} {3,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.58701,0.0366814,-6.46045e-05,9.37094e-08,-5.47566e-11,17248,10.4068], Tmin=(10,'K'), Tmax=(547.35,'K')),
            NASAPolynomial(coeffs=[3.6552,0.0274003,-1.5101e-05,4.09885e-09,-4.37451e-13,17372.1,11.3207], Tmin=(547.35,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 237,
    label = "C=C1[CH]O1",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 C u1 p0 c0 {1,S} {4,S} {5,S}
3 C u0 p0 c0 {1,D} {6,S} {7,S}
4 O u0 p2 c0 {1,S} {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96503,0.00197202,6.36755e-05,-1.09479e-07,5.81324e-11,31777.2,7.93587], Tmin=(10,'K'), Tmax=(583.96,'K')),
            NASAPolynomial(coeffs=[1.53167,0.0261929,-1.7941e-05,5.84603e-09,-7.22023e-13,31932.7,17.2638], Tmin=(583.96,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 238,
    label = "[CH2]C1(C[O])CO1",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4  C u1 p0 c0 {1,S} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  O u1 p2 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77591,0.0184878,0.000116109,-3.03754e-07,2.32385e-10,14325.9,12.6608], Tmin=(10,'K'), Tmax=(428.86,'K')),
            NASAPolynomial(coeffs=[2.80879,0.0436657,-2.84665e-05,8.8384e-09,-1.04712e-12,14260.3,14.7755], Tmin=(428.86,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 239,
    label = "OCC1CO1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
4  O u0 p2 c0 {1,S} {2,S}
5  O u0 p2 c0 {3,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91462,0.00471114,0.000116008,-2.03571e-07,1.07583e-10,-32302,10.3956], Tmin=(10,'K'), Tmax=(616.8,'K')),
            NASAPolynomial(coeffs=[0.945651,0.0447108,-3.17192e-05,1.06288e-08,-1.33844e-12,-32330.4,20.0855], Tmin=(616.8,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 240,
    label = "[CH2]CC(C)(C)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  C u1 p0 c0 {2,S} {16,S} {17,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {6,S} {18,S}
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
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.0585,0.0762617,-8.50733e-05,6.49086e-08,-2.25994e-11,-10834.9,13.1639], Tmin=(10,'K'), Tmax=(695.21,'K')),
            NASAPolynomial(coeffs=[6.83983,0.0526605,-3.01708e-05,8.44358e-09,-9.21866e-13,-11316.1,-3.38356], Tmin=(695.21,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 241,
    label = "[CH2]C(C)C(C)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {9,S}
3  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
5  C u1 p0 c0 {1,S} {16,S} {17,S}
6  O u0 p2 c0 {2,S} {7,S}
7  O u0 p2 c0 {6,S} {18,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80291,0.0271896,0.000847346,-7.06549e-06,1.81637e-08,-9417.43,10.4153], Tmin=(10,'K'), Tmax=(134.85,'K')),
            NASAPolynomial(coeffs=[4.47511,0.0567827,-3.27696e-05,9.14185e-09,-9.89072e-13,-9480.6,6.8492], Tmin=(134.85,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 242,
    label = "CC(=C=O)O[O]",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C u0 p0 c0 {1,S} {3,S} {4,D}
3 O u0 p2 c0 {2,S} {8,S}
4 C u0 p0 c0 {2,D} {9,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 O u1 p2 c0 {3,S}
9 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77769,0.0208049,0.000141296,-6.5729e-07,8.34599e-10,1678.56,11.0123], Tmin=(10,'K'), Tmax=(285.57,'K')),
            NASAPolynomial(coeffs=[5.00389,0.027375,-1.79436e-05,5.64125e-09,-6.78552e-13,1511.7,4.93806], Tmin=(285.57,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 243,
    label = "C=C[CH]OC",
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
            NASAPolynomial(coeffs=[3.77231,0.024415,1.8659e-05,-3.73296e-08,1.51358e-11,-1142.81,10.1633], Tmin=(10,'K'), Tmax=(909.08,'K')),
            NASAPolynomial(coeffs=[3.91783,0.0357137,-1.9684e-05,5.23588e-09,-5.42845e-13,-1662.6,6.76174], Tmin=(909.08,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 244,
    label = "C=CC(O)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,D} {7,S}
3  C u0 p0 c0 {2,D} {8,S} {9,S}
4  O u0 p2 c0 {1,S} {10,S}
5  O u0 p2 c0 {1,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 O u1 p2 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.62689,0.0375621,-2.26731e-05,4.44841e-09,4.39847e-13,-14633.9,13.114], Tmin=(10,'K'), Tmax=(1131.59,'K')),
            NASAPolynomial(coeffs=[9.13677,0.0240564,-1.26852e-05,3.22712e-09,-3.20533e-13,-16263.2,-15.8383], Tmin=(1131.59,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 245,
    label = "[CH2]C(O)C=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u1 p0 c0 {1,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,D} {7,S}
4  O u0 p2 c0 {1,S} {10,S}
5  H u0 p0 c0 {1,S}
6  O u0 p2 c0 {3,D}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80986,0.0156851,0.000103413,-2.96056e-07,2.46448e-10,-19585.9,10.8486], Tmin=(10,'K'), Tmax=(401.14,'K')),
            NASAPolynomial(coeffs=[3.45011,0.0343384,-2.2676e-05,7.12347e-09,-8.52142e-13,-19678.3,10.7447], Tmin=(401.14,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 246,
    label = "[CH2]OC[CH]C=O",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u1 p0 c0 {1,S} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {9,D} {10,S}
4  C u1 p0 c0 {5,S} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95466,0.0390138,-2.20425e-05,5.14681e-09,-3.0632e-13,1434.67,12.6309], Tmin=(10,'K'), Tmax=(1699.64,'K')),
            NASAPolynomial(coeffs=[24.5628,-5.3485e-05,4.11131e-06,-1.84649e-09,2.42035e-13,-6933.03,-101.73], Tmin=(1699.64,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 247,
    label = "O=CCCO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,D} {10,S}
4  O u0 p2 c0 {2,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83965,0.0091346,0.00013844,-2.80181e-07,1.63049e-10,-43885.9,9.53578], Tmin=(10,'K'), Tmax=(603.33,'K')),
            NASAPolynomial(coeffs=[5.55622,0.0366742,-2.67921e-05,9.31724e-09,-1.21362e-12,-44801.4,-3.74876], Tmin=(603.33,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 248,
    label = "O=CC=CC=O",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {3,S} {5,S}
2  C u0 p0 c0 {1,D} {4,S} {6,S}
3  C u0 p0 c0 {1,S} {7,D} {9,S}
4  C u0 p0 c0 {2,S} {8,D} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  O u0 p2 c0 {3,D}
8  O u0 p2 c0 {4,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89643,0.0104855,0.00022708,-9.74657e-07,1.35974e-09,-23215.2,9.13581], Tmin=(10,'K'), Tmax=(222.8,'K')),
            NASAPolynomial(coeffs=[3.09162,0.0363713,-2.4191e-05,7.58148e-09,-9.0438e-13,-23207.7,11.1731], Tmin=(222.8,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 249,
    label = "C=C=CC([O])C=C",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {8,S}
3  C u0 p0 c0 {2,S} {5,D} {9,S}
4  C u0 p0 c0 {2,S} {7,D} {10,S}
5  C u0 p0 c0 {3,D} {11,S} {12,S}
6  C u0 p0 c0 {7,D} {13,S} {14,S}
7  C u0 p0 c0 {4,D} {6,D}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76047,0.0274924,0.000375599,-2.32329e-06,4.28798e-09,35511.7,12.4982], Tmin=(10,'K'), Tmax=(188.61,'K')),
            NASAPolynomial(coeffs=[4.39772,0.0461313,-2.83602e-05,8.49279e-09,-9.85083e-13,35430.5,8.97072], Tmin=(188.61,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 250,
    label = "C#CC[CH2]",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C u1 p0 c0 {1,S} {7,S} {8,S}
3 C u0 p0 c0 {1,S} {4,T}
4 C u0 p0 c0 {3,T} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93047,0.00676242,0.000140468,-5.27436e-07,6.77876e-10,43712.6,9.84325], Tmin=(10,'K'), Tmax=(196.08,'K')),
            NASAPolynomial(coeffs=[2.92766,0.0272197,-1.60292e-05,4.64821e-09,-5.26067e-13,43751.9,13.0474], Tmin=(196.08,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 251,
    label = "C=C=C1OO1",
    molecule = 
"""
1 C u0 p0 c0 {3,D} {4,S} {5,S}
2 C u0 p0 c0 {3,D} {6,S} {7,S}
3 C u0 p0 c0 {1,D} {2,D}
4 O u0 p2 c0 {1,S} {5,S}
5 O u0 p2 c0 {1,S} {4,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91687,0.00542543,8.75194e-05,-2.04244e-07,1.42179e-10,32546,8.43215], Tmin=(10,'K'), Tmax=(485.71,'K')),
            NASAPolynomial(coeffs=[3.81008,0.0224412,-1.48625e-05,4.68046e-09,-5.61895e-13,32366,6.91083], Tmin=(485.71,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 252,
    label = "CC[C]CC",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  C u0 p1 c0 {1,S} {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8455,0.0151145,0.00032548,-1.42381e-06,1.96661e-09,28359.6,8.80743], Tmin=(10,'K'), Tmax=(239.94,'K')),
            NASAPolynomial(coeffs=[3.6462,0.0447817,-2.46849e-05,6.73168e-09,-7.25416e-13,28293.3,7.90418], Tmin=(239.94,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 253,
    label = "CC(CCOO)O[O]",
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
            NASAPolynomial(coeffs=[2.97935,0.0973159,-0.000214994,3.33274e-07,-2.10457e-10,-24457.1,14.4173], Tmin=(10,'K'), Tmax=(453.75,'K')),
            NASAPolynomial(coeffs=[6.56478,0.0540556,-3.34632e-05,9.96429e-09,-1.14307e-12,-24662.5,1.27486], Tmin=(453.75,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 254,
    label = "CCC(C[O])CO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {16,S} {17,S}
5  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
6  O u0 p2 c0 {3,S} {18,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u1 p2 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.66985,0.0334919,0.000320927,-1.44431e-06,1.96477e-09,-32126.2,12.3419], Tmin=(10,'K'), Tmax=(245.22,'K')),
            NASAPolynomial(coeffs=[3.51088,0.0644329,-4.17373e-05,1.30478e-08,-1.56421e-12,-32203.7,11.1475], Tmin=(245.22,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 255,
    label = "C[CH]C(O)C=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {2,S} {10,S}
4  C u0 p0 c0 {1,S} {11,D} {12,S}
5  O u0 p2 c0 {1,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 O u0 p2 c0 {4,D}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.28786,0.0719892,-0.000218806,4.4761e-07,-3.37681e-10,-24395.7,12.497], Tmin=(10,'K'), Tmax=(431.45,'K')),
            NASAPolynomial(coeffs=[3.64687,0.0424342,-2.48742e-05,7.0666e-09,-7.79751e-13,-24182.6,13.8957], Tmin=(431.45,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 256,
    label = "C=C(O)CO[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {5,S}
3  C u0 p0 c0 {2,D} {8,S} {9,S}
4  O u0 p2 c0 {1,S} {10,S}
5  O u0 p2 c0 {2,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 O u1 p2 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79926,0.0120071,0.000161079,-3.57075e-07,2.25142e-10,-14213.4,11.2843], Tmin=(10,'K'), Tmax=(562.4,'K')),
            NASAPolynomial(coeffs=[6.50901,0.0378214,-2.80238e-05,9.63243e-09,-1.23192e-12,-15231.2,-6.56832], Tmin=(562.4,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 257,
    label = "CC1OOC[C]1O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {4,S} {6,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {1,S} {2,S} {7,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {2,S} {5,S}
7  O u0 p2 c0 {4,S} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72352,0.0234361,0.000100402,-2.37006e-07,1.59746e-10,-16859.1,12.6948], Tmin=(10,'K'), Tmax=(479.65,'K')),
            NASAPolynomial(coeffs=[2.01884,0.0518539,-3.28822e-05,9.97633e-09,-1.16019e-12,-16858.9,17.9635], Tmin=(479.65,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 258,
    label = "C[CH]C(=O)COO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,S} {12,D}
4  C u1 p0 c0 {2,S} {3,S} {13,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 O u0 p2 c0 {3,D}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.34944,0.0645908,-0.000110333,1.73682e-07,-1.24968e-10,-21728.6,13.1628], Tmin=(10,'K'), Tmax=(391.93,'K')),
            NASAPolynomial(coeffs=[4.44945,0.0487171,-3.17954e-05,9.8395e-09,-1.1612e-12,-21779.1,9.34155], Tmin=(391.93,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 259,
    label = "[CH2]CC(CO)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
4  C u1 p0 c0 {2,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {3,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.10538,0.0747001,-8.16767e-05,5.17454e-08,-1.40396e-11,-23770.2,14.6539], Tmin=(10,'K'), Tmax=(837.29,'K')),
            NASAPolynomial(coeffs=[9.59448,0.0436996,-2.61393e-05,7.52531e-09,-8.36252e-13,-24856.9,-15.4999], Tmin=(837.29,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 260,
    label = "CC([O])=C(C)O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,D} {5,S}
4  C u0 p0 c0 {2,S} {3,D} {12,S}
5  O u0 p2 c0 {3,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 O u1 p2 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80681,0.0286683,6.89364e-06,-2.00505e-08,7.18873e-12,-38969.5,11.757], Tmin=(10,'K'), Tmax=(1138.4,'K')),
            NASAPolynomial(coeffs=[6.71065,0.0321309,-1.56755e-05,3.7115e-09,-3.4534e-13,-40516.1,-6.51804], Tmin=(1138.4,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 261,
    label = "[CH2]C1OO1",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,S} {7,S}
3 O u0 p2 c0 {1,S} {4,S}
4 O u0 p2 c0 {1,S} {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9454,0.00313723,6.99467e-05,-1.31224e-07,7.41755e-11,16127.7,8.53813], Tmin=(10,'K'), Tmax=(581.88,'K')),
            NASAPolynomial(coeffs=[2.77796,0.0238994,-1.64083e-05,5.33067e-09,-6.55462e-13,16047.9,11.6854], Tmin=(581.88,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 262,
    label = "[CH2]C(=O)C(C)=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,D}
3  C u0 p0 c0 {2,S} {4,S} {9,D}
4  C u1 p0 c0 {3,S} {10,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {2,D}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81958,0.0270461,9.22109e-06,-2.75528e-08,1.12874e-11,-20652.9,11.1871], Tmin=(10,'K'), Tmax=(993.75,'K')),
            NASAPolynomial(coeffs=[6.90388,0.0292372,-1.61331e-05,4.24677e-09,-4.33387e-13,-21987.1,-7.30216], Tmin=(993.75,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 263,
    label = "C=C=C[CH]CC=C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u1 p0 c0 {1,S} {4,S} {10,S}
3  C u0 p0 c0 {1,S} {5,D} {11,S}
4  C u0 p0 c0 {2,S} {7,D} {12,S}
5  C u0 p0 c0 {3,D} {13,S} {14,S}
6  C u0 p0 c0 {7,D} {15,S} {16,S}
7  C u0 p0 c0 {4,D} {6,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.17647,0.0840546,-0.000257997,5.51876e-07,-4.28659e-10,41849.5,12.0837], Tmin=(10,'K'), Tmax=(429.68,'K')),
            NASAPolynomial(coeffs=[2.50672,0.0548041,-3.20053e-05,9.03861e-09,-9.91454e-13,42234.6,18.561], Tmin=(429.68,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 264,
    label = "C_C[CH]CCC=C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,D} {12,S}
4  C u1 p0 c0 {2,S} {6,S} {13,S}
5  C u0 p0 c0 {3,D} {14,S} {15,S}
6  C u0 p0 c0 {4,S} {7,T}
7  C u0 p0 c0 {6,T} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.31977,0.0658049,-0.000116759,2.02452e-07,-1.46253e-10,43222.7,12.8066], Tmin=(10,'K'), Tmax=(449.76,'K')),
            NASAPolynomial(coeffs=[3.05533,0.05436,-3.25746e-05,9.46012e-09,-1.06452e-12,43386,15.4224], Tmin=(449.76,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 265,
    label = "[CH]=C=COC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u1 p0 c0 {3,S} {4,S} {9,S}
3  O u0 p2 c0 {1,S} {2,S}
4  C u0 p0 c0 {2,S} {5,T}
5  C u0 p0 c0 {4,T} {10,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80137,0.0186742,0.000173465,-7.81675e-07,1.00757e-09,21617.6,10.1469], Tmin=(10,'K'), Tmax=(275.46,'K')),
            NASAPolynomial(coeffs=[4.76398,0.0292622,-1.79698e-05,5.41363e-09,-6.33407e-13,21471.4,5.05229], Tmin=(275.46,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 266,
    label = "C=C(O)C=O",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 C u0 p0 c0 {1,S} {5,D} {6,S}
3 C u0 p0 c0 {1,D} {7,S} {8,S}
4 O u0 p2 c0 {1,S} {9,S}
5 O u0 p2 c0 {2,D}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92838,0.00483835,9.63017e-05,-1.97657e-07,1.31719e-10,-33228.6,9.30633], Tmin=(10,'K'), Tmax=(384.46,'K')),
            NASAPolynomial(coeffs=[1.0372,0.0349194,-2.10646e-05,5.86489e-09,-6.26979e-13,-33006.3,20.4908], Tmin=(384.46,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 267,
    label = "C=C(O)[CH][O]",
    molecule = 
"""
multiplicity 3
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 C u1 p0 c0 {1,S} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {5,D} {8,S}
4 O u0 p2 c0 {1,S} {9,S}
5 O u0 p2 c0 {3,D}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91298,0.00644168,0.00013834,-3.69637e-07,3.09337e-10,-6000.67,10.1594], Tmin=(10,'K'), Tmax=(385.37,'K')),
            NASAPolynomial(coeffs=[2.95304,0.0316536,-1.9144e-05,5.47177e-09,-6.11062e-13,-6039.91,12.4061], Tmin=(385.37,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 268,
    label = "CC(=O)C=O",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {7,D}
3 C u0 p0 c0 {2,S} {8,D} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {2,D}
8 O u0 p2 c0 {3,D}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.6915,0.0360773,-0.000161582,5.19051e-07,-5.41777e-10,-35098.4,9.69302], Tmin=(10,'K'), Tmax=(351.05,'K')),
            NASAPolynomial(coeffs=[1.20642,0.0339105,-2.20727e-05,6.75398e-09,-7.86167e-13,-34736.1,21.7559], Tmin=(351.05,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 269,
    label = "CC(=O)CC[O]",
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
            NASAPolynomial(coeffs=[3.47912,0.0579458,-0.000217584,6.08987e-07,-5.80241e-10,-22548.5,12.3203], Tmin=(10,'K'), Tmax=(373.65,'K')),
            NASAPolynomial(coeffs=[0.908384,0.0483702,-3.02239e-05,8.99543e-09,-1.02682e-12,-22097.4,25.6571], Tmin=(373.65,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 270,
    label = "[O]OCC(=O)CO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,D}
4  O u0 p2 c0 {1,S} {11,S}
5  O u0 p2 c0 {2,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 O u1 p2 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.44522,0.0520673,-4.4059e-05,1.74417e-08,-2.36069e-12,-37998.7,13.0686], Tmin=(10,'K'), Tmax=(1029.46,'K')),
            NASAPolynomial(coeffs=[11.4379,0.0266813,-1.53308e-05,4.18741e-09,-4.41082e-13,-39944.8,-27.1825], Tmin=(1029.46,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 271,
    label = "CC([O])=CO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,D}
3  C u1 p0 c0 {2,S} {4,S} {9,S}
4  O u0 p2 c0 {3,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {2,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88603,0.00865561,0.000101306,-2.64843e-07,2.31434e-10,-32675.3,10.6477], Tmin=(10,'K'), Tmax=(289.24,'K')),
            NASAPolynomial(coeffs=[2.26472,0.0310781,-1.4981e-05,3.19364e-09,-2.46609e-13,-32581.5,16.4583], Tmin=(289.24,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 272,
    label = "CC(O)=C[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  C u0 p0 c0 {2,D} {8,S} {9,S}
4  O u0 p2 c0 {2,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u1 p2 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82701,0.0139661,5.26533e-05,-1.14877e-07,7.48157e-11,-33015.9,10.166], Tmin=(10,'K'), Tmax=(398.98,'K')),
            NASAPolynomial(coeffs=[1.91599,0.0331253,-1.93779e-05,5.48281e-09,-6.02013e-13,-32863.4,17.6296], Tmin=(398.98,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 273,
    label = "CC(O)=C=O",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C u0 p0 c0 {1,S} {3,S} {4,D}
3 O u0 p2 c0 {2,S} {9,S}
4 C u0 p0 c0 {2,D} {8,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 O u0 p2 c0 {4,D}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85222,0.0123891,0.000143805,-5.29043e-07,5.68009e-10,-24740.4,10.0278], Tmin=(10,'K'), Tmax=(327.51,'K')),
            NASAPolynomial(coeffs=[4.74386,0.0241918,-1.41851e-05,4.12201e-09,-4.70833e-13,-24920.5,4.86341], Tmin=(327.51,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 274,
    label = "[CH2]C(O)=C(C)[O]",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u1 p0 c0 {3,S} {4,S} {5,S}
3  C u0 p0 c0 {1,S} {2,S} {9,D}
4  C u1 p0 c0 {2,S} {10,S} {11,S}
5  O u0 p2 c0 {2,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89781,0.00914099,0.000251093,-9.09966e-07,1.06317e-09,-12431,12.0524], Tmin=(10,'K'), Tmax=(274.18,'K')),
            NASAPolynomial(coeffs=[3.05486,0.0402905,-2.24564e-05,5.93752e-09,-6.16496e-13,-12455.6,13.7363], Tmin=(274.18,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 275,
    label = "CC(=O)C(C)=O",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,S} {11,D}
4  C u0 p0 c0 {2,S} {3,S} {12,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {3,D}
12 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.47006,0.0595373,-0.000253897,7.00802e-07,-6.54322e-10,-42445.6,10.379], Tmin=(10,'K'), Tmax=(376.58,'K')),
            NASAPolynomial(coeffs=[1.04664,0.0439498,-2.71825e-05,7.99888e-09,-9.03528e-13,-41970.1,23.5947], Tmin=(376.58,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 276,
    label = "C=C(O)C(C)=O",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {4,D} {5,S}
3  C u0 p0 c0 {1,S} {2,S} {9,D}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  O u0 p2 c0 {2,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81002,0.0169103,9.02407e-05,-2.24127e-07,1.71988e-10,-39715.2,10.6464], Tmin=(10,'K'), Tmax=(335.5,'K')),
            NASAPolynomial(coeffs=[1.61956,0.0430264,-2.65235e-05,7.89527e-09,-9.0649e-13,-39568.2,18.8218], Tmin=(335.5,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 277,
    label = "CC(=O)C(C)(O)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {3,S} {13,D}
5  O u0 p2 c0 {1,S} {15,S}
6  O u0 p2 c0 {1,S} {14,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 O u1 p2 c0 {6,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.44367,0.049924,9.46989e-05,-4.33395e-07,4.35944e-10,-49656.6,13.9614], Tmin=(10,'K'), Tmax=(376.72,'K')),
            NASAPolynomial(coeffs=[6.08288,0.0522878,-3.5708e-05,1.1506e-08,-1.40278e-12,-50071,0.943468], Tmin=(376.72,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 278,
    label = "O[C]1COOC1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {2,S} {6,S}
4  O u0 p2 c0 {1,S} {5,S}
5  O u0 p2 c0 {2,S} {4,S}
6  O u0 p2 c0 {3,S} {11,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92295,0.00459128,0.000125761,-2.37558e-07,1.38771e-10,-11277.7,11.746], Tmin=(10,'K'), Tmax=(540.92,'K')),
            NASAPolynomial(coeffs=[0.811512,0.0439816,-2.88989e-05,9.04392e-09,-1.07947e-12,-11180.7,22.6296], Tmin=(540.92,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 279,
    label = "CC=CC=CC",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {4,S} {7,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,D} {13,S}
4  C u0 p0 c0 {2,S} {6,D} {14,S}
5  C u0 p0 c0 {3,D} {6,S} {15,S}
6  C u0 p0 c0 {4,D} {5,S} {16,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.64156,0.036863,1.31777e-05,-3.50534e-08,1.394e-11,3149.64,9.44369], Tmin=(10,'K'), Tmax=(974.45,'K')),
            NASAPolynomial(coeffs=[4.67496,0.0471909,-2.51478e-05,6.51047e-09,-6.59877e-13,2256.49,0.935496], Tmin=(974.45,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 280,
    label = "C=CC=CCC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,D} {12,S}
4  C u0 p0 c0 {3,D} {5,S} {13,S}
5  C u0 p0 c0 {4,S} {6,D} {14,S}
6  C u0 p0 c0 {5,D} {15,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67676,0.0323427,3.55523e-05,-6.79923e-08,2.9301e-11,4673.55,11.8908], Tmin=(10,'K'), Tmax=(826.66,'K')),
            NASAPolynomial(coeffs=[2.99434,0.051851,-2.92526e-05,7.98525e-09,-8.48177e-13,4232.63,11.704], Tmin=(826.66,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 281,
    label = "CC1C=CC1C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {8,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {9,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {6,D} {15,S}
6  C u0 p0 c0 {2,S} {5,D} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94161,0.0040002,0.000195005,-4.06866e-07,2.80747e-10,9748.46,10.7415], Tmin=(10,'K'), Tmax=(370.39,'K')),
            NASAPolynomial(coeffs=[-1.36617,0.0613202,-3.71244e-05,1.09384e-08,-1.25138e-12,10141.7,31.0769], Tmin=(370.39,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 282,
    label = "C[CH]C(C=O)CO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {3,S} {13,S}
5  C u0 p0 c0 {1,S} {14,D} {15,S}
6  O u0 p2 c0 {2,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 O u0 p2 c0 {5,D}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75565,0.0155655,0.000234224,-5.34095e-07,3.58112e-10,-26905.5,14.9364], Tmin=(10,'K'), Tmax=(508.86,'K')),
            NASAPolynomial(coeffs=[3.86279,0.0623554,-4.41076e-05,1.44993e-08,-1.77912e-12,-27533.1,8.43234], Tmin=(508.86,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 283,
    label = "CC1=C(O)CO1",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  C u0 p0 c0 {1,S} {3,D} {6,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {4,S} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7329,0.0266517,1.04312e-05,-2.75609e-08,1.13e-11,-20738.4,11.1837], Tmin=(10,'K'), Tmax=(935.81,'K')),
            NASAPolynomial(coeffs=[4.27252,0.0345973,-1.87376e-05,4.92563e-09,-5.06171e-13,-21288.3,6.2176], Tmin=(935.81,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 284,
    label = "OOC1[CH]COOC1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {6,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {3,S} {14,S}
5  O u0 p2 c0 {2,S} {6,S}
6  O u0 p2 c0 {3,S} {5,S}
7  O u0 p2 c0 {1,S} {8,S}
8  O u0 p2 c0 {7,S} {15,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.60183,0.0399474,2.39556e-05,-6.68004e-08,3.24085e-11,-6380.3,14.0124], Tmin=(10,'K'), Tmax=(790.59,'K')),
            NASAPolynomial(coeffs=[5.5387,0.0490607,-2.92192e-05,8.29887e-09,-9.08078e-13,-7277.61,1.38516], Tmin=(790.59,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 285,
    label = "[CH2]C1OOCC1OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {10,S}
3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
4  C u1 p0 c0 {2,S} {13,S} {14,S}
5  O u0 p2 c0 {2,S} {6,S}
6  O u0 p2 c0 {3,S} {5,S}
7  O u0 p2 c0 {1,S} {8,S}
8  O u0 p2 c0 {7,S} {15,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.47556,0.0503407,-1.65683e-05,-1.34607e-08,8.65849e-12,-6233.43,14.2286], Tmin=(10,'K'), Tmax=(925.7,'K')),
            NASAPolynomial(coeffs=[8.19913,0.0424492,-2.40671e-05,6.54926e-09,-6.91025e-13,-7644.36,-11.0925], Tmin=(925.7,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 286,
    label = "OOCC1[CH]COO1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {7,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {6,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {3,S} {14,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {3,S} {5,S}
7  O u0 p2 c0 {2,S} {8,S}
8  O u0 p2 c0 {7,S} {15,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65581,0.050543,-2.30782e-05,-3.16108e-10,2.05013e-12,-5284,11.961], Tmin=(10,'K'), Tmax=(1259.63,'K')),
            NASAPolynomial(coeffs=[14.1737,0.0301716,-1.43341e-05,3.26726e-09,-2.90767e-13,-8967.32,-45.3122], Tmin=(1259.63,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 287,
    label = "OC1=COC1",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2 C u0 p0 c0 {1,S} {3,D} {5,S}
3 C u0 p0 c0 {2,D} {4,S} {8,S}
4 O u0 p2 c0 {1,S} {3,S}
5 O u0 p2 c0 {2,S} {9,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89476,0.00905661,7.49786e-05,-1.76204e-07,1.31306e-10,-13908.6,8.29901], Tmin=(10,'K'), Tmax=(344.61,'K')),
            NASAPolynomial(coeffs=[2.03367,0.0306588,-1.905e-05,5.69882e-09,-6.56421e-13,-13780.3,15.295], Tmin=(344.61,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 288,
    label = "CC=C(CO)CO",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {6,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {7,S} {10,S} {11,S}
3  C u0 p0 c0 {5,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {2,S} {5,D}
5  C u0 p0 c0 {3,S} {4,D} {15,S}
6  O u0 p2 c0 {1,S} {17,S}
7  O u0 p2 c0 {2,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75649,0.0289074,0.000523707,-3.44323e-06,6.83709e-09,-44384.5,12.6615], Tmin=(10,'K'), Tmax=(175.49,'K')),
            NASAPolynomial(coeffs=[4.55749,0.052167,-2.9992e-05,8.4673e-09,-9.34954e-13,-44476.6,8.36966], Tmin=(175.49,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 289,
    label = "C=CC(CO)CO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {5,D} {13,S}
5  C u0 p0 c0 {4,D} {14,S} {15,S}
6  O u0 p2 c0 {2,S} {17,S}
7  O u0 p2 c0 {3,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72933,0.0175642,0.000254861,-6.06049e-07,4.23095e-10,-43351.7,11.866], Tmin=(10,'K'), Tmax=(493.29,'K')),
            NASAPolynomial(coeffs=[4.82602,0.0618747,-4.16607e-05,1.33381e-08,-1.62227e-12,-44107.2,0.788945], Tmin=(493.29,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 290,
    label = "[CH2][CH]C(CO)CO",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {5,S} {13,S}
5  C u1 p0 c0 {4,S} {14,S} {15,S}
6  O u0 p2 c0 {2,S} {17,S}
7  O u0 p2 c0 {3,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53672,0.0361809,0.000262002,-8.743e-07,8.02391e-10,-10261.9,12.7569], Tmin=(10,'K'), Tmax=(393.25,'K')),
            NASAPolynomial(coeffs=[7.29666,0.0563868,-3.80205e-05,1.22776e-08,-1.50625e-12,-11009.6,-7.61995], Tmin=(393.25,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 291,
    label = "CCC(COO)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
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
            NASAPolynomial(coeffs=[2.84298,0.0934148,-0.000149209,1.45508e-07,-5.81237e-11,-23274.6,14.9696], Tmin=(10,'K'), Tmax=(678.99,'K')),
            NASAPolynomial(coeffs=[9.50541,0.0460421,-2.66088e-05,7.51236e-09,-8.26938e-13,-23992.1,-13.2145], Tmin=(678.99,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 292,
    label = "[CH]=C=CO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {5,S}
2 C u0 p0 c0 {1,D} {4,D}
3 O u0 p2 c0 {1,S} {6,S}
4 C u1 p0 c0 {2,D} {7,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88361,0.00726996,8.94548e-05,-2.1369e-07,1.44783e-10,20440.2,8.46061], Tmin=(10,'K'), Tmax=(527.57,'K')),
            NASAPolynomial(coeffs=[5.64786,0.0185775,-1.28775e-05,4.30934e-09,-5.46654e-13,19910.5,-2.17831], Tmin=(527.57,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 293,
    label = "C=CC[CH]O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u1 p0 c0 {1,S} {5,S} {9,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  O u0 p2 c0 {3,S} {12,S}
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
            NASAPolynomial(coeffs=[3.7941,0.0132031,0.000166749,-4.08902e-07,2.87616e-10,847.515,10.3529], Tmin=(10,'K'), Tmax=(505.11,'K')),
            NASAPolynomial(coeffs=[6.53358,0.0341085,-2.18405e-05,6.9822e-09,-8.66652e-13,27.3444,-6.37179], Tmin=(505.11,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 294,
    label = "C=C([CH]O)O[O]",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,D} {3,S} {4,S}
2  C u0 p0 c0 {1,D} {5,S} {6,S}
3  C u1 p0 c0 {1,S} {7,S} {8,S}
4  O u0 p2 c0 {1,S} {9,S}
5  O u0 p2 c0 {2,S} {10,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  O u1 p2 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84885,0.0101072,0.000152388,-3.73061e-07,2.70625e-10,2323.16,11.4706], Tmin=(10,'K'), Tmax=(469.12,'K')),
            NASAPolynomial(coeffs=[3.97606,0.0373312,-2.51754e-05,7.90444e-09,-9.44299e-13,1999.72,7.63305], Tmin=(469.12,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 295,
    label = "O=CC=C=CO",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,D} {6,S}
2  C u0 p0 c0 {4,D} {5,S} {8,S}
3  C u0 p0 c0 {1,S} {7,D} {9,S}
4  C u0 p0 c0 {1,D} {2,D}
5  O u0 p2 c0 {2,S} {10,S}
6  H u0 p0 c0 {1,S}
7  O u0 p2 c0 {3,D}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84392,0.00992671,0.000142375,-3.31353e-07,2.24792e-10,-11569.1,10.6153], Tmin=(10,'K'), Tmax=(509.74,'K')),
            NASAPolynomial(coeffs=[4.61925,0.0352675,-2.46692e-05,8.06137e-09,-9.90301e-13,-12056.4,3.39263], Tmin=(509.74,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 296,
    label = "O=CC=C[CH]O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,D} {7,S}
2  C u1 p0 c0 {1,S} {4,S} {6,S}
3  C u0 p0 c0 {1,D} {5,S} {8,S}
4  C u0 p0 c0 {2,S} {9,D} {10,S}
5  O u0 p2 c0 {3,S} {11,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  O u0 p2 c0 {4,D}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91898,0.00514489,0.000129789,-2.68459e-07,1.74045e-10,-24061,11.9194], Tmin=(10,'K'), Tmax=(491.26,'K')),
            NASAPolynomial(coeffs=[1.86036,0.0384403,-2.23575e-05,6.5199e-09,-7.54717e-13,-24058.3,18.3573], Tmin=(491.26,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 297,
    label = "[CH2]C(=O)[C]=O",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,S} {3,S} {4,D}
2 C u1 p0 c0 {1,S} {5,S} {6,S}
3 C u1 p0 c0 {1,S} {7,D}
4 O u0 p2 c0 {1,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84618,0.0114512,9.82138e-05,-3.04193e-07,2.62605e-10,6251.49,11.0656], Tmin=(10,'K'), Tmax=(414.86,'K')),
            NASAPolynomial(coeffs=[5.17541,0.0206311,-1.45087e-05,4.75155e-09,-5.85198e-13,5951.91,3.54097], Tmin=(414.86,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 298,
    label = "CC(=O)C(=O)CO[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,S} {12,D}
4  C u0 p0 c0 {2,S} {3,S} {11,D}
5  O u0 p2 c0 {1,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {4,D}
12 O u0 p2 c0 {3,D}
13 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.01524,0.0920317,-0.000267574,4.61942e-07,-3.0065e-10,-32585.3,13.6347], Tmin=(10,'K'), Tmax=(474.06,'K')),
            NASAPolynomial(coeffs=[6.00357,0.0411813,-2.55591e-05,7.52512e-09,-8.50494e-13,-32580.6,4.48647], Tmin=(474.06,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 299,
    label = "C=C(C=O)O[O]",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 C u0 p0 c0 {1,S} {5,D} {6,S}
3 C u0 p0 c0 {1,D} {7,S} {8,S}
4 O u0 p2 c0 {1,S} {9,S}
5 O u0 p2 c0 {2,D}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 O u1 p2 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79343,0.0174142,0.000149698,-5.60283e-07,5.92891e-10,-1902.15,10.7371], Tmin=(10,'K'), Tmax=(335.07,'K')),
            NASAPolynomial(coeffs=[4.92685,0.0295979,-1.99614e-05,6.32523e-09,-7.61464e-13,-2122.45,4.35426], Tmin=(335.07,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 300,
    label = "CC(=O)C(=O)C[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,S} {11,D}
4  C u0 p0 c0 {2,S} {3,S} {12,D}
5  O u1 p2 c0 {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {3,D}
12 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.60085,0.0387199,0.000150481,-8.26508e-07,1.10592e-09,-31244.4,12.3124], Tmin=(10,'K'), Tmax=(283.84,'K')),
            NASAPolynomial(coeffs=[6.07191,0.0379127,-2.50221e-05,7.9458e-09,-9.64496e-13,-31521.7,1.08911], Tmin=(283.84,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 301,
    label = "CC1([O])OOCC1=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {4,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {2,S} {13,D}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {2,S} {5,S}
7  O u1 p2 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77487,0.0163477,0.000198794,-5.36306e-07,4.28414e-10,-27740.8,12.928], Tmin=(10,'K'), Tmax=(424.84,'K')),
            NASAPolynomial(coeffs=[3.84956,0.0487668,-3.26142e-05,1.03316e-08,-1.24326e-12,-28046,9.11358], Tmin=(424.84,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 302,
    label = "CC[C](C=O)CO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {6,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {1,S} {2,S} {5,S}
5  C u0 p0 c0 {4,S} {14,D} {15,S}
6  O u0 p2 c0 {2,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 O u0 p2 c0 {5,D}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.23497,0.062713,-6.99131e-05,6.2985e-08,-2.71178e-11,-32205.5,14.3893], Tmin=(10,'K'), Tmax=(637.82,'K')),
            NASAPolynomial(coeffs=[4.44981,0.0501923,-2.89391e-05,8.10798e-09,-8.85182e-13,-32260.7,9.85639], Tmin=(637.82,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 303,
    label = "[CH]=[C]C=C",
    molecule = 
"""
multiplicity 3
1 C u1 p0 c0 {2,S} {3,S} {5,S}
2 C u1 p0 c0 {1,S} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {4,T}
4 C u0 p0 c0 {3,T} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88258,0.00786767,0.000105353,-2.68516e-07,1.99694e-10,62619,8.89326], Tmin=(10,'K'), Tmax=(469.71,'K')),
            NASAPolynomial(coeffs=[4.84124,0.0224933,-1.41312e-05,4.36531e-09,-5.24465e-13,62277.6,2.31658], Tmin=(469.71,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 304,
    label = "CC1OOC1=O",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {6,S}
3  O u0 p2 c0 {6,D}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
6  C u0 p0 c0 {2,S} {3,D} {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86907,0.0104808,8.93868e-05,-1.88377e-07,1.18603e-10,-29770.8,10.8123], Tmin=(10,'K'), Tmax=(511.45,'K')),
            NASAPolynomial(coeffs=[2.24897,0.0359591,-2.28997e-05,6.94844e-09,-8.06853e-13,-29772.6,15.9045], Tmin=(511.45,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 305,
    label = "C[C]C(C)C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
5  C u0 p1 c0 {1,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53674,0.0429915,-4.79917e-05,8.49642e-08,-6.40093e-11,28092.8,11.5868], Tmin=(10,'K'), Tmax=(505.65,'K')),
            NASAPolynomial(coeffs=[1.14603,0.0490059,-2.75732e-05,7.60089e-09,-8.20427e-13,28499.5,23.1208], Tmin=(505.65,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 306,
    label = "CCC1C=CC1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {6,D} {15,S}
6  C u0 p0 c0 {3,S} {5,D} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94182,0.00387201,0.000187892,-3.7671e-07,2.48591e-10,10824.2,11.9645], Tmin=(10,'K'), Tmax=(388.26,'K')),
            NASAPolynomial(coeffs=[-1.72889,0.0623135,-3.79664e-05,1.12329e-08,-1.28825e-12,11264.4,33.9556], Tmin=(388.26,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 307,
    label = "C=CC1CO1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {10,S} {11,S}
5  O u0 p2 c0 {1,S} {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94625,0.00324751,0.000115115,-2.1228e-07,1.23714e-10,-689.728,10.3457], Tmin=(10,'K'), Tmax=(517.73,'K')),
            NASAPolynomial(coeffs=[0.21161,0.0421935,-2.69603e-05,8.31577e-09,-9.86028e-13,-438.278,24.5985], Tmin=(517.73,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 308,
    label = "C=C=CCO[O]",
    molecule = 
"""
multiplicity 2
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
11 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.46963,0.0541241,-0.000148958,3.11154e-07,-2.46956e-10,25225.4,11.4061], Tmin=(10,'K'), Tmax=(408.18,'K')),
            NASAPolynomial(coeffs=[3.68226,0.0358166,-2.20621e-05,6.52906e-09,-7.44354e-13,25343.2,12.2263], Tmin=(408.18,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 309,
    label = "CC(=O)C(=O)COO",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {5,S}
2  O u0 p2 c0 {1,S} {14,S}
3  O u0 p2 c0 {8,D}
4  O u0 p2 c0 {7,D}
5  C u0 p0 c0 {1,S} {7,S} {9,S} {10,S}
6  C u0 p0 c0 {8,S} {11,S} {12,S} {13,S}
7  C u0 p0 c0 {4,D} {5,S} {8,S}
8  C u0 p0 c0 {3,D} {6,S} {7,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.45313,0.0545709,-1.39196e-05,-3.54443e-08,2.33198e-11,-51777.8,12.9475], Tmin=(10,'K'), Tmax=(787.77,'K')),
            NASAPolynomial(coeffs=[10.321,0.0402402,-2.57466e-05,7.666e-09,-8.66131e-13,-53497.3,-22.5933], Tmin=(787.77,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 310,
    label = "C=C=[C]CO[O]",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u1 p0 c0 {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,T}
4  C u0 p0 c0 {2,S} {3,T}
5  O u0 p2 c0 {1,S} {10,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.40169,0.0620882,-0.000207779,4.47797e-07,-3.59406e-10,44149.7,12.6146], Tmin=(10,'K'), Tmax=(395.37,'K')),
            NASAPolynomial(coeffs=[4.40635,0.0322965,-2.02855e-05,6.08044e-09,-6.99167e-13,44223.6,10.64], Tmin=(395.37,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 311,
    label = "[CH2]C(=C=C)O[O]",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {4,D} {5,S}
2  C u1 p0 c0 {1,S} {6,S} {7,S}
3  C u0 p0 c0 {4,D} {8,S} {9,S}
4  C u0 p0 c0 {1,D} {3,D}
5  O u0 p2 c0 {1,S} {10,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73337,0.0226227,0.000103185,-3.5021e-07,3.21551e-10,43672,12.0184], Tmin=(10,'K'), Tmax=(384.18,'K')),
            NASAPolynomial(coeffs=[4.52148,0.0347524,-2.35744e-05,7.54075e-09,-9.14035e-13,43461.4,7.01714], Tmin=(384.18,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 312,
    label = "C=CC=CC=[C]C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {7,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {3,D} {4,S} {12,S}
3  C u0 p0 c0 {2,D} {5,S} {13,S}
4  C u0 p0 c0 {2,S} {6,D} {11,S}
5  C u0 p0 c0 {3,S} {7,D} {14,S}
6  C u0 p0 c0 {4,D} {15,S} {16,S}
7  C u1 p0 c0 {1,S} {5,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71102,0.0389129,2.61919e-05,-6.05112e-08,2.59523e-11,42609.2,11.7247], Tmin=(10,'K'), Tmax=(899.1,'K')),
            NASAPolynomial(coeffs=[6.69028,0.048413,-2.76196e-05,7.53731e-09,-7.95838e-13,41153.8,-7.44629], Tmin=(899.1,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 313,
    label = "C=C([O])C=CC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {4,S} {11,S}
4  C u0 p0 c0 {3,S} {5,S} {10,D}
5  C u1 p0 c0 {4,S} {12,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {4,D}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90549,0.0119015,0.000441903,-3.00186e-06,7.24172e-09,1428.87,8.90582], Tmin=(10,'K'), Tmax=(103.89,'K')),
            NASAPolynomial(coeffs=[3.06168,0.044389,-2.71489e-05,7.97051e-09,-9.01659e-13,1446.4,11.066], Tmin=(103.89,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 314,
    label = "[O]OC(=O)[CH]CC=O",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u1 p0 c0 {1,S} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {5,S} {9,D}
4  C u0 p0 c0 {1,S} {10,D} {11,S}
5  O u0 p2 c0 {3,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {3,D}
10 O u0 p2 c0 {4,D}
11 H u0 p0 c0 {4,S}
12 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.05521,0.101383,-0.000394611,9.29801e-07,-8.22919e-10,-16073.1,13.1121], Tmin=(10,'K'), Tmax=(347.52,'K')),
            NASAPolynomial(coeffs=[5.6992,0.0440728,-3.12273e-05,1.01485e-08,-1.23488e-12,-16094.5,5.48603], Tmin=(347.52,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 315,
    label = "CC1C(O)C1CO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {6,S} {10,S}
4  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
5  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
6  O u0 p2 c0 {3,S} {17,S}
7  O u0 p2 c0 {4,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78144,0.0130561,0.000224597,-4.65791e-07,2.855e-10,-41254.7,13.9635], Tmin=(10,'K'), Tmax=(556.03,'K')),
            NASAPolynomial(coeffs=[3.66939,0.0630375,-4.2898e-05,1.39856e-08,-1.72952e-12,-42002.4,7.60259], Tmin=(556.03,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 316,
    label = "OC=CCO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {5,S} {9,S}
4  O u0 p2 c0 {1,S} {10,S}
5  O u0 p2 c0 {3,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81651,0.024196,1.97593e-05,-4.17571e-08,1.74262e-11,-39307.2,9.15442], Tmin=(10,'K'), Tmax=(919.38,'K')),
            NASAPolynomial(coeffs=[5.97108,0.0311189,-1.8125e-05,4.99464e-09,-5.2952e-13,-40392.1,-4.80478], Tmin=(919.38,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 317,
    label = "[O]C1OOCC1=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,D}
4  O u0 p2 c0 {1,S} {5,S}
5  O u0 p2 c0 {2,S} {4,S}
6  O u1 p2 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87252,0.00808628,0.000140093,-3.10973e-07,2.06261e-10,-21272.4,12.4216], Tmin=(10,'K'), Tmax=(505.95,'K')),
            NASAPolynomial(coeffs=[3.25759,0.0385776,-2.62896e-05,8.3824e-09,-1.01018e-12,-21538.2,11.7275], Tmin=(505.95,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 318,
    label = "O=C1COOC1=O",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {5,S}
2 O u0 p2 c0 {1,S} {7,S}
3 O u0 p2 c0 {6,D}
4 O u0 p2 c0 {7,D}
5 C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
6 C u0 p0 c0 {3,D} {5,S} {7,S}
7 C u0 p0 c0 {2,S} {4,D} {6,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88788,0.00737447,0.000125342,-2.87429e-07,1.98323e-10,-39679.7,11.1663], Tmin=(10,'K'), Tmax=(480.89,'K')),
            NASAPolynomial(coeffs=[3.04421,0.0347941,-2.3824e-05,7.58527e-09,-9.10334e-13,-39834.5,12.1661], Tmin=(480.89,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 319,
    label = "[CH2]C[C](CO)CO",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {4,S} {7,S} {10,S} {13,S}
4  C u1 p0 c0 {1,S} {2,S} {3,S}
5  C u1 p0 c0 {1,S} {14,S} {15,S}
6  O u0 p2 c0 {2,S} {16,S}
7  O u0 p2 c0 {3,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.48602,0.0538261,0.000333757,-2.1522e-06,3.50991e-09,-10706.5,14.6735], Tmin=(10,'K'), Tmax=(234.23,'K')),
            NASAPolynomial(coeffs=[7.42385,0.0485097,-2.87928e-05,8.46448e-09,-9.73541e-13,-11060.9,-2.23527], Tmin=(234.23,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 320,
    label = "CC([O])CC=O",
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
            NASAPolynomial(coeffs=[3.76113,0.0216785,0.000216242,-8.52121e-07,9.92904e-10,-20626.8,12.0584], Tmin=(10,'K'), Tmax=(294.43,'K')),
            NASAPolynomial(coeffs=[4.21,0.0424731,-2.67029e-05,8.17776e-09,-9.67156e-13,-20769.8,8.46219], Tmin=(294.43,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 321,
    label = "C[CH]C(CO)CO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
5  C u1 p0 c0 {1,S} {4,S} {16,S}
6  O u0 p2 c0 {2,S} {17,S}
7  O u0 p2 c0 {3,S} {18,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.54247,0.0389252,0.000162218,-4.93232e-07,4.11766e-10,-35787.8,13.1144], Tmin=(10,'K'), Tmax=(411.16,'K')),
            NASAPolynomial(coeffs=[3.744,0.0661911,-4.38768e-05,1.38167e-08,-1.65512e-12,-36051.4,9.31703], Tmin=(411.16,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 322,
    label = "C=CC(COO)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {3,D} {12,S} {13,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {1,S} {14,S}
7  O u0 p2 c0 {5,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 O u1 p2 c0 {6,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.84447,0.109039,-0.000316445,5.32487e-07,-3.38825e-10,-6028.51,14.2313], Tmin=(10,'K'), Tmax=(475.12,'K')),
            NASAPolynomial(coeffs=[7.48788,0.0434677,-2.5837e-05,7.42406e-09,-8.27131e-13,-6170.89,-1.56987], Tmin=(475.12,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 323,
    label = "OCC1(CO)CC1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {7,S} {12,S} {15,S}
6  O u0 p2 c0 {4,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76588,0.0153827,0.000245333,-5.77185e-07,4.0543e-10,-42015.9,11.4991], Tmin=(10,'K'), Tmax=(481.25,'K')),
            NASAPolynomial(coeffs=[3.48148,0.0625184,-4.11307e-05,1.29575e-08,-1.55717e-12,-42507,7.27645], Tmin=(481.25,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 324,
    label = "CC[C](CO)CO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {5,S} {6,S} {13,S} {14,S}
3  C u0 p0 c0 {5,S} {7,S} {15,S} {16,S}
4  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
5  C u1 p0 c0 {1,S} {2,S} {3,S}
6  O u0 p2 c0 {2,S} {17,S}
7  O u0 p2 c0 {3,S} {18,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.00107,0.100956,-0.000292434,5.87082e-07,-4.44852e-10,-35784.8,12.8934], Tmin=(10,'K'), Tmax=(420.35,'K')),
            NASAPolynomial(coeffs=[4.27929,0.0588803,-3.55472e-05,1.03704e-08,-1.16983e-12,-35628,10.9779], Tmin=(420.35,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 325,
    label = "[O]OCCC(CO)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {7,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {8,S}
6  O u0 p2 c0 {3,S} {17,S}
7  O u0 p2 c0 {4,S} {16,S}
8  O u0 p2 c0 {5,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {7,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.80745,0.128842,-0.000477386,1.17805e-06,-1.08645e-09,-42378.3,16.0292], Tmin=(10,'K'), Tmax=(344.63,'K')),
            NASAPolynomial(coeffs=[4.49261,0.0697779,-4.83709e-05,1.55444e-08,-1.87892e-12,-42259.9,13.0981], Tmin=(344.63,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 326,
    label = "[CH2]CC(CO)CO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {7,S} {11,S} {14,S}
5  C u1 p0 c0 {2,S} {15,S} {16,S}
6  O u0 p2 c0 {3,S} {17,S}
7  O u0 p2 c0 {4,S} {18,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.57151,0.0431946,0.000275424,-1.33161e-06,1.81435e-09,-34170.7,12.8775], Tmin=(10,'K'), Tmax=(257.32,'K')),
            NASAPolynomial(coeffs=[4.54714,0.0627604,-4.10916e-05,1.29536e-08,-1.56237e-12,-34335.9,7.26071], Tmin=(257.32,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 327,
    label = "[O][CH]CC=O",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,S} {9,S}
3 C u0 p0 c0 {1,S} {7,D} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u1 p2 c0 {2,S}
7 O u0 p2 c0 {3,D}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78933,0.0169843,0.000158301,-6.05305e-07,6.34768e-10,5690.88,10.3122], Tmin=(10,'K'), Tmax=(352.18,'K')),
            NASAPolynomial(coeffs=[6.51203,0.0215369,-1.21868e-05,3.44116e-09,-3.87838e-13,5279.09,-3.10534], Tmin=(352.18,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 328,
    label = "CCC1C(O)C1O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {6,S} {10,S}
4  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
5  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
6  O u0 p2 c0 {3,S} {17,S}
7  O u0 p2 c0 {2,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.858,0.0161138,0.000426247,-2.08112e-06,3.52366e-09,-40672.6,12.4998], Tmin=(10,'K'), Tmax=(148.47,'K')),
            NASAPolynomial(coeffs=[2.14503,0.0622633,-3.99986e-05,1.24126e-08,-1.47899e-12,-40621.7,17.4967], Tmin=(148.47,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 329,
    label = "O=C1[CH]OOC1=O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {6,S}
2 O u0 p2 c0 {1,S} {7,S}
3 O u0 p2 c0 {5,D}
4 O u0 p2 c0 {7,D}
5 C u0 p0 c0 {3,D} {6,S} {7,S}
6 C u1 p0 c0 {1,S} {5,S} {8,S}
7 C u0 p0 c0 {2,S} {4,D} {5,S}
8 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88957,0.00654536,0.00010859,-2.25801e-07,1.37221e-10,-25780.1,11.1364], Tmin=(10,'K'), Tmax=(564.09,'K')),
            NASAPolynomial(coeffs=[3.9849,0.0308349,-2.23855e-05,7.44902e-09,-9.24889e-13,-26188.1,7.21036], Tmin=(564.09,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 330,
    label = "C=C([O])CO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,D} {7,S}
3  C u0 p0 c0 {2,D} {8,S} {9,S}
4  O u0 p2 c0 {1,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  O u1 p2 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89035,0.00959552,0.000116441,-3.08302e-07,2.64674e-10,-24932,10.1914], Tmin=(10,'K'), Tmax=(297.34,'K')),
            NASAPolynomial(coeffs=[1.81449,0.0375211,-2.4435e-05,7.5535e-09,-8.91016e-13,-24808.6,17.6885], Tmin=(297.34,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 331,
    label = "CCC(CO)(CO)O[O]",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {4,S} {5,S}
2  O u0 p2 c0 {7,S} {19,S}
3  O u0 p2 c0 {8,S} {20,S}
4  O u1 p2 c0 {1,S}
5  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
6  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
7  C u0 p0 c0 {2,S} {5,S} {13,S} {14,S}
8  C u0 p0 c0 {3,S} {5,S} {12,S} {15,S}
9  C u0 p0 c0 {6,S} {16,S} {17,S} {18,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63695,0.0234094,0.000322353,-7.5965e-07,5.2098e-10,-56284.3,15.0042], Tmin=(10,'K'), Tmax=(502.53,'K')),
            NASAPolynomial(coeffs=[4.87099,0.082466,-5.95232e-05,1.97082e-08,-2.42747e-12,-57278.1,1.24641], Tmin=(502.53,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 332,
    label = "C=CC(CO[O])OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {3,D} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {2,S} {14,S}
7  O u0 p2 c0 {5,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 O u1 p2 c0 {6,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.01488,0.0949603,-0.00023032,3.6518e-07,-2.32484e-10,-6209.04,15.6197], Tmin=(10,'K'), Tmax=(440.96,'K')),
            NASAPolynomial(coeffs=[7.32635,0.0457803,-2.87708e-05,8.67903e-09,-1.00584e-12,-6491.37,-0.540291], Tmin=(440.96,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 333,
    label = "OCC1CCC1O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {9,S}
3  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {3,S} {12,S} {13,S}
5  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
6  O u0 p2 c0 {2,S} {17,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91416,0.00512154,0.000198549,-3.57882e-07,2.02961e-10,-43255.8,12.9051], Tmin=(10,'K'), Tmax=(523.7,'K')),
            NASAPolynomial(coeffs=[-3.64241,0.0778486,-5.27516e-05,1.67544e-08,-2.008e-12,-42670.1,42.5082], Tmin=(523.7,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 334,
    label = "O=CC(O)=CCO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {4,S} {6,S}
4  C u0 p0 c0 {3,S} {10,D} {11,S}
5  O u0 p2 c0 {1,S} {12,S}
6  O u0 p2 c0 {3,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {4,D}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.58121,0.0430318,-2.01705e-05,7.03251e-10,1.32449e-12,-55751.1,11.9576], Tmin=(10,'K'), Tmax=(1293.85,'K')),
            NASAPolynomial(coeffs=[11.8153,0.027432,-1.35118e-05,3.16005e-09,-2.87861e-13,-58706.8,-33.0765], Tmin=(1293.85,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 335,
    label = "[CH2]O[CH]C=C",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,D} {3,S} {6,S}
2  C u0 p0 c0 {1,D} {5,S} {7,S}
3  C u1 p0 c0 {1,S} {8,S} {9,S}
4  C u1 p0 c0 {5,S} {10,S} {11,S}
5  O u0 p2 c0 {2,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84284,0.0114204,0.000158351,-4.42085e-07,3.67636e-10,22974.3,11.7104], Tmin=(10,'K'), Tmax=(411.94,'K')),
            NASAPolynomial(coeffs=[4.32877,0.0336308,-2.05816e-05,6.18678e-09,-7.24769e-13,22705.8,7.02373], Tmin=(411.94,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 336,
    label = "[CH2]C=C[CH]C=C",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {3,D} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {10,S}
3  C u0 p0 c0 {1,D} {5,S} {9,S}
4  C u0 p0 c0 {2,D} {6,S} {8,S}
5  C u1 p0 c0 {3,S} {11,S} {12,S}
6  C u1 p0 c0 {4,S} {13,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78996,0.0264132,5.32469e-05,-9.76208e-08,4.45055e-11,41461,13.4016], Tmin=(10,'K'), Tmax=(783.07,'K')),
            NASAPolynomial(coeffs=[4.30159,0.04624,-2.77171e-05,7.90277e-09,-8.666e-13,40692.9,6.66528], Tmin=(783.07,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 337,
    label = "C=C[C]=CO[O]",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {3,S} {4,D} {6,S}
2  C u0 p0 c0 {4,D} {5,S} {9,S}
3  C u1 p0 c0 {1,S} {7,S} {8,S}
4  C u0 p0 c0 {1,D} {2,D}
5  O u0 p2 c0 {2,S} {10,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {2,S}
10 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81332,0.0130371,0.00015419,-4.19453e-07,3.29723e-10,43813.9,11.5031], Tmin=(10,'K'), Tmax=(445.37,'K')),
            NASAPolynomial(coeffs=[5.14973,0.0332385,-2.23134e-05,7.11416e-09,-8.63163e-13,43375.5,2.55103], Tmin=(445.37,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 338,
    label = "C#C[CH]CC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {4,S} {11,S}
4  C u0 p0 c0 {3,S} {5,T}
5  C u0 p0 c0 {4,T} {12,S}
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
            NASAPolynomial(coeffs=[3.76803,0.0206609,7.22957e-05,-2.22721e-07,2.08628e-10,33602.2,11.5662], Tmin=(10,'K'), Tmax=(273.13,'K')),
            NASAPolynomial(coeffs=[2.60352,0.0377155,-2.13677e-05,5.8997e-09,-6.34851e-13,33665.9,15.673], Tmin=(273.13,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 339,
    label = "C=CC[CH]C(=C)O[O]",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u1 p0 c0 {1,S} {3,S} {10,S}
3  C u0 p0 c0 {2,S} {5,D} {7,S}
4  C u0 p0 c0 {1,S} {6,D} {11,S}
5  C u0 p0 c0 {3,D} {12,S} {13,S}
6  C u0 p0 c0 {4,D} {14,S} {15,S}
7  O u0 p2 c0 {3,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 O u1 p2 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.44638,0.0579309,-3.46686e-05,7.73458e-09,5.13174e-14,29793.5,14.4779], Tmin=(10,'K'), Tmax=(1235.82,'K')),
            NASAPolynomial(coeffs=[13.1538,0.035233,-1.77054e-05,4.29477e-09,-4.08147e-13,26728.1,-37.1048], Tmin=(1235.82,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 340,
    label = "C#CC(C)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,T}
4  O u0 p2 c0 {1,S} {10,S}
5  C u0 p0 c0 {3,T} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u1 p2 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77032,0.0228073,0.000171078,-7.94894e-07,1.06287e-09,25055.7,11.6722], Tmin=(10,'K'), Tmax=(259.93,'K')),
            NASAPolynomial(coeffs=[4.25047,0.0359459,-2.32051e-05,7.24195e-09,-8.67586e-13,24961.4,8.66882], Tmin=(259.93,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 341,
    label = "CC=C=CO[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,D} {9,S}
3  C u0 p0 c0 {4,D} {5,S} {10,S}
4  C u0 p0 c0 {2,D} {3,D}
5  O u0 p2 c0 {3,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79775,0.0197184,0.000165086,-6.85934e-07,8.51749e-10,25523.6,10.9102], Tmin=(10,'K'), Tmax=(268.91,'K')),
            NASAPolynomial(coeffs=[3.68551,0.0375508,-2.4544e-05,7.71046e-09,-9.26834e-13,25471.2,10.2176], Tmin=(268.91,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 342,
    label = "C=C1[CH]C1",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 C u0 p0 c0 {1,S} {2,D} {7,S}
4 C u1 p0 c0 {2,S} {8,S} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94786,0.00302758,8.8892e-05,-1.60257e-07,8.95775e-11,44383.2,8.1558], Tmin=(10,'K'), Tmax=(561.29,'K')),
            NASAPolynomial(coeffs=[1.33216,0.0329924,-2.14496e-05,6.74527e-09,-8.15354e-13,44498.5,17.6754], Tmin=(561.29,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 343,
    label = "C=C[C]=CC=C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,D} {7,S}
2  C u0 p0 c0 {1,S} {6,D} {9,S}
3  C u0 p0 c0 {5,S} {6,D} {8,S}
4  C u0 p0 c0 {1,D} {10,S} {11,S}
5  C u1 p0 c0 {3,S} {12,S} {13,S}
6  C u0 p0 c0 {2,D} {3,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85147,0.00947154,0.000173454,-3.83788e-07,2.56377e-10,43471.8,11.2451], Tmin=(10,'K'), Tmax=(499.33,'K')),
            NASAPolynomial(coeffs=[2.9214,0.0471181,-3.03459e-05,9.4171e-09,-1.12309e-12,43188.3,11.3168], Tmin=(499.33,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 344,
    label = "C=C[C]=CC=CC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {11,S}
3  C u0 p0 c0 {2,D} {4,S} {12,S}
4  C u0 p0 c0 {3,S} {7,D} {14,S}
5  C u0 p0 c0 {6,S} {7,D} {13,S}
6  C u1 p0 c0 {5,S} {15,S} {16,S}
7  C u0 p0 c0 {4,D} {5,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78262,0.0226972,0.00027443,-1.17739e-06,1.69932e-09,38944.8,11.7027], Tmin=(10,'K'), Tmax=(174.73,'K')),
            NASAPolynomial(coeffs=[2.19729,0.0589885,-3.7111e-05,1.12367e-08,-1.30869e-12,39000.2,16.5855], Tmin=(174.73,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 345,
    label = "CO[CH]C=CC=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {6,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {4,D} {11,S}
3  C u1 p0 c0 {2,S} {5,S} {10,S}
4  C u0 p0 c0 {2,D} {6,S} {12,S}
5  C u0 p0 c0 {3,S} {13,D} {14,S}
6  O u0 p2 c0 {1,S} {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 O u0 p2 c0 {5,D}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.24088,0.061508,-8.81714e-05,9.82143e-08,-4.70746e-11,-18604.5,12.6999], Tmin=(10,'K'), Tmax=(630.14,'K')),
            NASAPolynomial(coeffs=[4.0373,0.046145,-2.7065e-05,7.60782e-09,-8.29294e-13,-18500.2,10.8493], Tmin=(630.14,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 346,
    label = "C=C[C]=CC=O",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {5,D}
2  C u0 p0 c0 {4,S} {6,D} {7,S}
3  C u0 p0 c0 {5,S} {6,D} {8,S}
4  C u1 p0 c0 {2,S} {9,S} {10,S}
5  C u0 p0 c0 {1,D} {3,S} {11,S}
6  C u0 p0 c0 {2,D} {3,D}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79681,0.0163258,0.000101346,-2.40289e-07,1.64976e-10,21500.2,10.9625], Tmin=(10,'K'), Tmax=(481.57,'K')),
            NASAPolynomial(coeffs=[2.80663,0.0410282,-2.69243e-05,8.33889e-09,-9.82972e-13,21404.5,13.0322], Tmin=(481.57,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 347,
    label = "[CH]=C1CC1",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 C u0 p0 c0 {1,S} {2,S} {4,D}
4 C u1 p0 c0 {3,D} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.0954,-0.00918468,0.000146531,-2.6145e-07,1.51049e-10,49787.3,8.67528], Tmin=(10,'K'), Tmax=(546.5,'K')),
            NASAPolynomial(coeffs=[1.04369,0.0323356,-2.00858e-05,6.03601e-09,-6.97992e-13,49834.4,18.9331], Tmin=(546.5,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 348,
    label = "C1=COCC1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {5,S} {11,S}
5  O u0 p2 c0 {2,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.08687,-0.00665286,0.00012328,-1.77117e-07,8.12555e-11,-10906.8,10.1655], Tmin=(10,'K'), Tmax=(672.14,'K')),
            NASAPolynomial(coeffs=[-1.80332,0.0445796,-2.71604e-05,7.91012e-09,-8.84295e-13,-10480.5,33.5236], Tmin=(672.14,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 349,
    label = "[CH2]CC=C[O]",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u1 p0 c0 {1,S} {4,S} {7,S}
3  C u1 p0 c0 {1,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {10,D} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 O u0 p2 c0 {4,D}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80845,0.0314857,-1.55185e-05,2.8941e-09,-3.78203e-14,16955.4,12.5771], Tmin=(10,'K'), Tmax=(1697.55,'K')),
            NASAPolynomial(coeffs=[17.3994,0.00672125,-5.13471e-08,-6.6072e-10,1.14658e-13,11295.1,-63.2646], Tmin=(1697.55,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 350,
    label = "CC1[C]=COO1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,D} {6,S} {11,S}
4  C u1 p0 c0 {1,S} {3,D}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {3,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83729,0.0159943,5.90563e-05,-1.07423e-07,5.37746e-11,29463.3,11.6823], Tmin=(10,'K'), Tmax=(673.87,'K')),
            NASAPolynomial(coeffs=[2.63491,0.0380331,-2.3172e-05,6.74287e-09,-7.54742e-13,29287,14.498], Tmin=(673.87,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 351,
    label = "C=CC=CC=C",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {3,S} {8,S}
2  C u0 p0 c0 {1,D} {4,S} {7,S}
3  C u0 p0 c0 {1,S} {5,D} {9,S}
4  C u0 p0 c0 {2,S} {6,D} {10,S}
5  C u0 p0 c0 {3,D} {11,S} {12,S}
6  C u0 p0 c0 {4,D} {13,S} {14,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88686,0.00651458,0.000164485,-3.02497e-07,1.69424e-10,18322.1,9.8631], Tmin=(10,'K'), Tmax=(574.97,'K')),
            NASAPolynomial(coeffs=[-0.0326624,0.0594728,-4.06966e-05,1.31198e-08,-1.59809e-12,18348.2,22.9105], Tmin=(574.97,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 352,
    label = "C=CC1C=CC1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {2,S} {3,D} {11,S}
5  C u0 p0 c0 {1,S} {6,D} {12,S}
6  C u0 p0 c0 {5,D} {13,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92541,0.00478506,0.000164433,-3.29214e-07,2.1052e-10,26505,10.9881], Tmin=(10,'K'), Tmax=(470.32,'K')),
            NASAPolynomial(coeffs=[-0.288274,0.0536841,-3.31823e-05,9.95305e-09,-1.15497e-12,26756.9,26.6023], Tmin=(470.32,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 353,
    label = "C1=CCCC=C1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,D} {11,S}
4  C u0 p0 c0 {2,S} {6,D} {12,S}
5  C u0 p0 c0 {3,D} {6,S} {14,S}
6  C u0 p0 c0 {4,D} {5,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.11614,-0.00983128,0.00018645,-2.92404e-07,1.47683e-10,11378.8,9.86499], Tmin=(10,'K'), Tmax=(609.91,'K')),
            NASAPolynomial(coeffs=[-2.77076,0.0578127,-3.51923e-05,1.02893e-08,-1.15868e-12,11800.8,36.2578], Tmin=(609.91,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 354,
    label = "C=C[C]=C[CH]C",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u1 p0 c0 {1,S} {3,S} {10,S}
3  C u0 p0 c0 {2,S} {6,D} {12,S}
4  C u0 p0 c0 {5,S} {6,D} {11,S}
5  C u1 p0 c0 {4,S} {13,S} {14,S}
6  C u0 p0 c0 {3,D} {4,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49376,0.05133,-0.000109476,2.49851e-07,-2.09741e-10,45855.7,11.7728], Tmin=(10,'K'), Tmax=(430.35,'K')),
            NASAPolynomial(coeffs=[1.23733,0.0504192,-3.0025e-05,8.61086e-09,-9.56606e-13,46252.6,23.1106], Tmin=(430.35,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 355,
    label = "C=C=CC=CC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {10,S}
3  C u0 p0 c0 {2,D} {4,S} {11,S}
4  C u0 p0 c0 {3,S} {6,D} {12,S}
5  C u0 p0 c0 {6,D} {13,S} {14,S}
6  C u0 p0 c0 {4,D} {5,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80795,0.0177162,0.000162049,-4.95145e-07,4.92068e-10,24639.4,10.2368], Tmin=(10,'K'), Tmax=(255.82,'K')),
            NASAPolynomial(coeffs=[1.69567,0.0507435,-3.16046e-05,9.51067e-09,-1.10289e-12,24747.5,17.5477], Tmin=(255.82,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 356,
    label = "C=C[CH]C(C=C)O[O]",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {4,S} {10,S}
3  C u0 p0 c0 {1,S} {5,D} {9,S}
4  C u0 p0 c0 {2,S} {6,D} {11,S}
5  C u0 p0 c0 {3,D} {14,S} {15,S}
6  C u0 p0 c0 {4,D} {12,S} {13,S}
7  O u0 p2 c0 {1,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 O u1 p2 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.62857,0.0413626,0.000405706,-2.60182e-06,4.65616e-09,29842.3,14.8673], Tmin=(10,'K'), Tmax=(203.29,'K')),
            NASAPolynomial(coeffs=[5.5525,0.0521018,-3.20811e-05,9.60063e-09,-1.11272e-12,29663.7,6.18073], Tmin=(203.29,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 357,
    label = "[CH2]C1(C=O)OO1",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {8,S} {9,S}
3 C u0 p0 c0 {1,S} {6,D} {7,S}
4 O u0 p2 c0 {1,S} {5,S}
5 O u0 p2 c0 {1,S} {4,S}
6 O u0 p2 c0 {3,D}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81699,0.0134981,9.84344e-05,-2.2915e-07,1.51057e-10,2384.14,10.8872], Tmin=(10,'K'), Tmax=(520.73,'K')),
            NASAPolynomial(coeffs=[3.86743,0.0346731,-2.46736e-05,7.9777e-09,-9.63084e-13,2086.55,7.86976], Tmin=(520.73,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 358,
    label = "CC=C=C[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {4,D} {9,S} {10,S}
4  C u0 p0 c0 {2,D} {3,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  O u1 p2 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65113,0.0337028,-6.41958e-05,1.30949e-07,-1.01407e-10,14498.7,10.291], Tmin=(10,'K'), Tmax=(460.99,'K')),
            NASAPolynomial(coeffs=[2.28953,0.032688,-1.91486e-05,5.43337e-09,-5.98877e-13,14760.5,17.2841], Tmin=(460.99,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 359,
    label = "CC=[C]C1OO1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {4,D} {11,S}
4  C u1 p0 c0 {1,S} {3,D}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {1,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.55616,0.0465777,-0.000132109,3.14975e-07,-2.73062e-10,30768.8,12.1689], Tmin=(10,'K'), Tmax=(398.26,'K')),
            NASAPolynomial(coeffs=[2.47417,0.0375272,-2.30052e-05,6.76849e-09,-7.67372e-13,31013,18.3759], Tmin=(398.26,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 360,
    label = "C=CC=C=CC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {6,D} {11,S}
3  C u0 p0 c0 {4,S} {5,D} {10,S}
4  C u0 p0 c0 {3,S} {6,D} {12,S}
5  C u0 p0 c0 {3,D} {13,S} {14,S}
6  C u0 p0 c0 {2,D} {4,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76161,0.0215332,0.000102829,-2.60745e-07,2.02219e-10,25070.3,10.3623], Tmin=(10,'K'), Tmax=(332.37,'K')),
            NASAPolynomial(coeffs=[1.28048,0.0513934,-3.19335e-05,9.56389e-09,-1.10321e-12,25235.2,19.5992], Tmin=(332.37,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 361,
    label = "C=CC1C=CCOO1",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {4,S}
3  C u0 p0 c0 {1,S} {5,S} {7,S} {9,S}
4  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
5  C u0 p0 c0 {3,S} {6,D} {13,S}
6  C u0 p0 c0 {4,S} {5,D} {14,S}
7  C u0 p0 c0 {3,S} {8,D} {12,S}
8  C u0 p0 c0 {7,D} {15,S} {16,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81832,0.0160494,0.000193748,-4.99064e-07,4.17108e-10,4311.38,12.1921], Tmin=(10,'K'), Tmax=(305.5,'K')),
            NASAPolynomial(coeffs=[0.172561,0.0637849,-4.06347e-05,1.24148e-08,-1.4549e-12,4534.14,25.4576], Tmin=(305.5,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 362,
    label = "[O]OC1[CH]C=CCC1",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {6,D} {14,S}
5  C u1 p0 c0 {3,S} {6,S} {13,S}
6  C u0 p0 c0 {4,D} {5,S} {15,S}
7  O u0 p2 c0 {1,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 O u1 p2 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70859,0.0279692,7.59642e-05,-1.40366e-07,6.89738e-11,17674,13.3082], Tmin=(10,'K'), Tmax=(691.21,'K')),
            NASAPolynomial(coeffs=[2.01451,0.058471,-3.51454e-05,1.01202e-08,-1.12367e-12,17413.8,17.2787], Tmin=(691.21,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 363,
    label = "CCC(=O)C=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,S} {10,D}
4  C u0 p0 c0 {3,S} {11,D} {12,S}
5  H u0 p0 c0 {1,S}
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
            NASAPolynomial(coeffs=[3.45587,0.0504014,-0.000105433,1.90331e-07,-1.3342e-10,-38286,10.8975], Tmin=(10,'K'), Tmax=(479.56,'K')),
            NASAPolynomial(coeffs=[2.6019,0.0411187,-2.50846e-05,7.30035e-09,-8.18103e-13,-38015.5,16.3567], Tmin=(479.56,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 364,
    label = "C=C1[CH]COO1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {3,S} {9,S}
3  C u0 p0 c0 {2,S} {4,D} {6,S}
4  C u0 p0 c0 {3,D} {10,S} {11,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {3,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91811,0.0047327,0.00012425,-2.27672e-07,1.27721e-10,13089.8,10.4454], Tmin=(10,'K'), Tmax=(570.19,'K')),
            NASAPolynomial(coeffs=[0.789406,0.0450889,-3.03402e-05,9.69424e-09,-1.17707e-12,13147.3,21.1579], Tmin=(570.19,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 365,
    label = "C=C=C[CH]C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {3,S} {9,S}
3  C u0 p0 c0 {2,S} {5,D} {10,S}
4  C u0 p0 c0 {5,D} {11,S} {12,S}
5  C u0 p0 c0 {3,D} {4,D}
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
            NASAPolynomial(coeffs=[3.6339,0.0386037,-9.46687e-05,2.50076e-07,-2.24131e-10,31749.8,10.3024], Tmin=(10,'K'), Tmax=(420.04,'K')),
            NASAPolynomial(coeffs=[0.78625,0.0423891,-2.48651e-05,7.0438e-09,-7.74315e-13,32194.8,24.0207], Tmin=(420.04,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 366,
    label = "C=C=C=CO[O]",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,D} {5,S} {6,S}
2 C u0 p0 c0 {4,D} {7,S} {8,S}
3 C u0 p0 c0 {1,D} {4,D}
4 C u0 p0 c0 {2,D} {3,D}
5 O u0 p2 c0 {1,S} {9,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82528,0.0122938,0.000137903,-3.79455e-07,3.00243e-10,44491.6,10.7529], Tmin=(10,'K'), Tmax=(443.08,'K')),
            NASAPolynomial(coeffs=[5.04534,0.0302214,-2.07677e-05,6.70294e-09,-8.17737e-13,44099.4,2.65401], Tmin=(443.08,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 367,
    label = "C=CC=C1[CH]C1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  C u0 p0 c0 {1,S} {2,D} {9,S}
4  C u1 p0 c0 {2,S} {5,S} {11,S}
5  C u0 p0 c0 {4,S} {6,D} {10,S}
6  C u0 p0 c0 {5,D} {12,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88194,0.0078183,0.000174851,-3.89077e-07,2.68661e-10,48063,11.2985], Tmin=(10,'K'), Tmax=(463.61,'K')),
            NASAPolynomial(coeffs=[1.5359,0.0498838,-3.18617e-05,9.70989e-09,-1.13596e-12,48046,18.2839], Tmin=(463.61,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 368,
    label = "C=CC=C=[C]C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {4,D} {10,S}
3  C u1 p0 c0 {2,S} {6,S} {11,S}
4  C u0 p0 c0 {2,D} {12,S} {13,S}
5  C u0 p0 c0 {1,S} {6,T}
6  C u0 p0 c0 {3,S} {5,T}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.54296,0.0428719,-4.22374e-05,6.17049e-08,-4.6448e-11,38478.4,12.3927], Tmin=(10,'K'), Tmax=(474.53,'K')),
            NASAPolynomial(coeffs=[2.36816,0.0454297,-2.71041e-05,7.82395e-09,-8.75671e-13,38672.6,18.0561], Tmin=(474.53,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 369,
    label = "C=C[C]=C=CC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u1 p0 c0 {1,S} {5,S} {10,S}
3  C u0 p0 c0 {4,D} {6,S} {11,S}
4  C u0 p0 c0 {3,D} {12,S} {13,S}
5  C u0 p0 c0 {2,S} {6,T}
6  C u0 p0 c0 {3,S} {5,T}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.57089,0.0420651,-5.73825e-05,1.15226e-07,-9.60314e-11,41104.4,11.3594], Tmin=(10,'K'), Tmax=(444.5,'K')),
            NASAPolynomial(coeffs=[1.86532,0.0452183,-2.687e-05,7.74191e-09,-8.6532e-13,41376.5,19.5601], Tmin=(444.5,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 370,
    label = "C=C1C=CC1C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {6,D}
4  C u0 p0 c0 {1,S} {5,D} {11,S}
5  C u0 p0 c0 {3,S} {4,D} {12,S}
6  C u0 p0 c0 {3,D} {13,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92966,0.00433689,0.000156334,-2.95123e-07,1.77069e-10,24428.5,10.7214], Tmin=(10,'K'), Tmax=(499.93,'K')),
            NASAPolynomial(coeffs=[-0.853579,0.0553202,-3.47786e-05,1.05924e-08,-1.24492e-12,24748,28.8928], Tmin=(499.93,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 371,
    label = "C=CC(CO)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {13,S}
6  O u0 p2 c0 {2,S} {14,S}
7  H u0 p0 c0 {1,S}
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
            NASAPolynomial(coeffs=[3.58526,0.0415863,0.00018323,-9.95368e-07,1.38394e-09,-15136.5,13.2607], Tmin=(10,'K'), Tmax=(266.2,'K')),
            NASAPolynomial(coeffs=[5.49272,0.0462178,-3.04735e-05,9.66332e-09,-1.17097e-12,-15356,4.36712], Tmin=(266.2,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 372,
    label = "C=C([C]=O)O[O]",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 O u0 p2 c0 {1,S} {7,S}
4 C u1 p0 c0 {1,S} {8,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 O u1 p2 c0 {3,S}
8 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78765,0.0143916,0.000132184,-3.77378e-07,2.93542e-10,18603.7,11.5902], Tmin=(10,'K'), Tmax=(472.21,'K')),
            NASAPolynomial(coeffs=[7.33775,0.0228236,-1.69108e-05,5.79227e-09,-7.38027e-13,17839.1,-7.41874], Tmin=(472.21,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 373,
    label = "[O]OC=[C]C=O",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {3,D} {4,S} {5,S}
2 C u0 p0 c0 {3,D} {6,S} {7,S}
3 C u0 p0 c0 {1,D} {2,D}
4 O u0 p2 c0 {1,S} {8,S}
5 H u0 p0 c0 {1,S}
6 O u1 p2 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 O u1 p2 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.62572,0.035299,-3.42968e-05,1.7281e-08,-3.5636e-12,28008.2,11.7823], Tmin=(10,'K'), Tmax=(1099.12,'K')),
            NASAPolynomial(coeffs=[8.33504,0.0181604,-1.09071e-05,3.09399e-09,-3.36688e-13,26973,-11.3825], Tmin=(1099.12,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 374,
    label = "[O]OCC(=O)C=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {7,D}
3  C u0 p0 c0 {2,S} {8,D} {9,S}
4  O u0 p2 c0 {1,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  O u0 p2 c0 {2,D}
8  O u0 p2 c0 {3,D}
9  H u0 p0 c0 {3,S}
10 O u1 p2 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.16518,0.0717121,-0.000185437,2.71988e-07,-1.51194e-10,-24708.3,12.542], Tmin=(10,'K'), Tmax=(549.47,'K')),
            NASAPolynomial(coeffs=[6.18163,0.0302652,-1.90908e-05,5.61484e-09,-6.30434e-13,-24745.6,2.47268], Tmin=(549.47,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 375,
    label = "O=CCC1OOC1=O",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {5,S}
2  O u0 p2 c0 {1,S} {7,S}
3  O u0 p2 c0 {7,D}
4  O u0 p2 c0 {8,D}
5  C u0 p0 c0 {1,S} {6,S} {7,S} {9,S}
6  C u0 p0 c0 {5,S} {8,S} {10,S} {11,S}
7  C u0 p0 c0 {2,S} {3,D} {5,S}
8  C u0 p0 c0 {4,D} {6,S} {12,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.59272,0.0451618,-2.71462e-05,4.05948e-09,1.20326e-12,-41683.9,12.8579], Tmin=(10,'K'), Tmax=(1104.14,'K')),
            NASAPolynomial(coeffs=[11.0036,0.0271609,-1.471e-05,3.80714e-09,-3.82605e-13,-43859.7,-26.0714], Tmin=(1104.14,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 376,
    label = "CC(=O)C(O)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,D}
4  O u0 p2 c0 {1,S} {11,S}
5  O u0 p2 c0 {1,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 O u1 p2 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.58664,0.0470844,-2.88467e-05,2.18375e-09,2.71733e-12,-42709.3,12.7702], Tmin=(10,'K'), Tmax=(1014.92,'K')),
            NASAPolynomial(coeffs=[11.5003,0.0269978,-1.55687e-05,4.24038e-09,-4.44262e-13,-44887.5,-28.3429], Tmin=(1014.92,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 377,
    label = "O=CCC(=O)C=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,D}
3  C u0 p0 c0 {1,S} {8,D} {9,S}
4  C u0 p0 c0 {2,S} {10,D} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  O u0 p2 c0 {2,D}
8  O u0 p2 c0 {3,D}
9  H u0 p0 c0 {3,S}
10 O u0 p2 c0 {4,D}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.34936,0.0727207,-0.000325113,8.89145e-07,-8.5166e-10,-46742.6,11.7371], Tmin=(10,'K'), Tmax=(352.75,'K')),
            NASAPolynomial(coeffs=[2.47233,0.042842,-2.87215e-05,8.96468e-09,-1.05835e-12,-46433,18.5664], Tmin=(352.75,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 378,
    label = "C=CC1=CC1C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {5,S}
4  C u0 p0 c0 {1,S} {3,D} {11,S}
5  C u0 p0 c0 {3,S} {6,D} {12,S}
6  C u0 p0 c0 {5,D} {13,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82149,0.0159421,0.000156933,-4.45901e-07,4.12135e-10,34209.2,11.2741], Tmin=(10,'K'), Tmax=(275.4,'K')),
            NASAPolynomial(coeffs=[1.44458,0.0504653,-3.11025e-05,9.28324e-09,-1.06978e-12,34340.1,19.6762], Tmin=(275.4,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 379,
    label = "C=C1OC1=O",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 C u0 p0 c0 {1,S} {4,S} {5,D}
3 C u0 p0 c0 {1,D} {6,S} {7,S}
4 O u0 p2 c0 {1,S} {2,S}
5 O u0 p2 c0 {2,D}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93749,0.00365826,7.5346e-05,-1.46765e-07,8.58225e-11,-8134.86,8.73031], Tmin=(10,'K'), Tmax=(568.02,'K')),
            NASAPolynomial(coeffs=[3.07903,0.024039,-1.63307e-05,5.26422e-09,-6.44437e-13,-8268.59,10.3507], Tmin=(568.02,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 380,
    label = "O=C=C1CO1",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {4,D}
3 O u0 p2 c0 {1,S} {2,S}
4 C u0 p0 c0 {2,D} {7,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88014,0.0118823,2.39989e-05,-4.72528e-08,2.32913e-11,5075.29,9.0979], Tmin=(10,'K'), Tmax=(711.79,'K')),
            NASAPolynomial(coeffs=[3.76273,0.0209247,-1.27216e-05,3.68483e-09,-4.10332e-13,4879.66,8.13276], Tmin=(711.79,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 381,
    label = "CC=C1C=CC1",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,D} {6,S}
4  C u0 p0 c0 {2,S} {3,D} {13,S}
5  C u0 p0 c0 {1,S} {6,D} {12,S}
6  C u0 p0 c0 {3,S} {5,D} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93765,0.00419505,0.000162697,-3.35687e-07,2.28565e-10,24404.8,10.4348], Tmin=(10,'K'), Tmax=(375.42,'K')),
            NASAPolynomial(coeffs=[-0.62265,0.0527841,-3.1442e-05,9.06545e-09,-1.01389e-12,24747.2,27.9678], Tmin=(375.42,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 382,
    label = "C=CC=C([CH]C)O[O]",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {3,D} {4,S} {7,S}
3  C u0 p0 c0 {1,S} {2,D} {11,S}
4  C u1 p0 c0 {2,S} {5,S} {13,S}
5  C u0 p0 c0 {4,S} {6,D} {12,S}
6  C u0 p0 c0 {5,D} {14,S} {15,S}
7  O u0 p2 c0 {2,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 O u1 p2 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.57331,0.0430178,4.21394e-05,-1.07322e-07,5.52955e-11,23706.3,13.5494], Tmin=(10,'K'), Tmax=(732.8,'K')),
            NASAPolynomial(coeffs=[6.20892,0.054431,-3.40328e-05,1.00196e-08,-1.12673e-12,22627.3,-3.07309], Tmin=(732.8,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 383,
    label = "[O]CC=CC[O]",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {2,S} {3,D} {12,S}
5  O u1 p2 c0 {1,S}
6  O u1 p2 c0 {2,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.24544,0.0530911,-6.348e-05,4.79062e-08,-1.52791e-11,14652.6,11.5369], Tmin=(10,'K'), Tmax=(881.43,'K')),
            NASAPolynomial(coeffs=[5.80292,0.0343026,-1.92832e-05,5.23339e-09,-5.53782e-13,14480.7,1.10399], Tmin=(881.43,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 384,
    label = "[O]CC(=O)C=O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {7,D}
3 C u0 p0 c0 {2,S} {8,D} {9,S}
4 O u1 p2 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {2,D}
8 O u0 p2 c0 {3,D}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71585,0.0289581,0.000218304,-1.3953e-06,2.25236e-09,-23495.5,11.0029], Tmin=(10,'K'), Tmax=(238.6,'K')),
            NASAPolynomial(coeffs=[6.61376,0.0231252,-1.37645e-05,3.96032e-09,-4.43312e-13,-23755.5,-1.37531], Tmin=(238.6,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 385,
    label = "O=[C]C(=O)COO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  O u0 p2 c0 {1,S} {5,S}
4  C u0 p0 c0 {2,D} {9,D}
5  O u0 p2 c0 {3,S} {10,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u1 p2 c0 {2,S}
9  O u0 p2 c0 {4,D}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.21909,0.0675251,-0.000153714,2.0386e-07,-1.06209e-10,-25838.5,13.4015], Tmin=(10,'K'), Tmax=(547.85,'K')),
            NASAPolynomial(coeffs=[7.34372,0.0275725,-1.73899e-05,5.19261e-09,-5.93736e-13,-26142.8,-2.66807], Tmin=(547.85,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 386,
    label = "O=CC(=O)COO",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {5,S}
2  O u0 p2 c0 {1,S} {11,S}
3  O u0 p2 c0 {6,D}
4  O u0 p2 c0 {7,D}
5  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
6  C u0 p0 c0 {3,D} {5,S} {7,S}
7  C u0 p0 c0 {4,D} {6,S} {10,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.64112,0.0392471,1.2632e-05,-6.7664e-08,3.87487e-11,-44049.5,11.4862], Tmin=(10,'K'), Tmax=(746.21,'K')),
            NASAPolynomial(coeffs=[9.46966,0.0322438,-2.20173e-05,6.82546e-09,-7.92408e-13,-45594.3,-19.4488], Tmin=(746.21,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 387,
    label = "[O]C[CH]C1CO1",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {1,S} {3,S} {12,S}
5  O u0 p2 c0 {1,S} {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u1 p2 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.46089,0.0602689,-0.000246058,6.83355e-07,-6.49362e-10,15380.9,12.8119], Tmin=(10,'K'), Tmax=(368.69,'K')),
            NASAPolynomial(coeffs=[1.33827,0.0450448,-2.84914e-05,8.54801e-09,-9.81058e-13,15797.4,24.4603], Tmin=(368.69,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 388,
    label = "[O]CC=CC=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  C u0 p0 c0 {3,S} {10,D} {11,S}
5  O u1 p2 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 O u0 p2 c0 {4,D}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.4245,0.0531658,-0.000127483,2.28569e-07,-1.55873e-10,-4718.67,11.1584], Tmin=(10,'K'), Tmax=(482.82,'K')),
            NASAPolynomial(coeffs=[3.1035,0.0377017,-2.31341e-05,6.73953e-09,-7.54727e-13,-4476.43,14.6609], Tmin=(482.82,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 389,
    label = "O=C[CH]C1CO1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3  C u1 p0 c0 {1,S} {4,S} {9,S}
4  C u0 p0 c0 {3,S} {10,D} {11,S}
5  O u0 p2 c0 {1,S} {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 O u0 p2 c0 {4,D}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8504,0.0199708,4.65286e-05,-8.44721e-08,3.88094e-11,-6854.08,11.5796], Tmin=(10,'K'), Tmax=(776.38,'K')),
            NASAPolynomial(coeffs=[4.39532,0.036358,-2.2217e-05,6.4028e-09,-7.0697e-13,-7517.19,5.36295], Tmin=(776.38,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 390,
    label = "[CH2]OC=CC=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {3,S} {6,S}
2  C u0 p0 c0 {1,D} {5,S} {7,S}
3  C u0 p0 c0 {1,S} {8,D} {9,S}
4  C u1 p0 c0 {5,S} {10,S} {11,S}
5  O u0 p2 c0 {2,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  O u0 p2 c0 {3,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67278,0.0300611,1.61696e-05,-5.57757e-08,3.07531e-11,-5851.06,12.2904], Tmin=(10,'K'), Tmax=(703.44,'K')),
            NASAPolynomial(coeffs=[5.1817,0.0345768,-2.13848e-05,6.28055e-09,-7.06969e-13,-6387.36,3.23854], Tmin=(703.44,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 391,
    label = "[CH2]OC=CC[O]",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {5,S} {10,S}
4  C u1 p0 c0 {5,S} {11,S} {12,S}
5  O u0 p2 c0 {3,S} {4,S}
6  O u1 p2 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.34131,0.0661574,-0.000180081,3.47859e-07,-2.60163e-10,14160.7,12.5363], Tmin=(10,'K'), Tmax=(415.01,'K')),
            NASAPolynomial(coeffs=[4.61811,0.0383902,-2.38371e-05,7.10058e-09,-8.13859e-13,14187.8,9.10344], Tmin=(415.01,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 392,
    label = "O=[C]C=C[CH]O",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {3,D} {6,S}
2  C u1 p0 c0 {1,S} {5,S} {8,S}
3  C u0 p0 c0 {1,D} {4,S} {7,S}
4  O u0 p2 c0 {3,S} {10,S}
5  C u1 p0 c0 {2,S} {9,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {5,D}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95072,0.00347229,0.000133577,-3.00772e-07,2.20711e-10,-2718.98,11.6268], Tmin=(10,'K'), Tmax=(396.89,'K')),
            NASAPolynomial(coeffs=[1.20931,0.0380406,-2.32969e-05,6.78743e-09,-7.69345e-13,-2556.02,21.6307], Tmin=(396.89,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 393,
    label = "[O]OC([CH]C=O)C=O",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u1 p0 c0 {1,S} {4,S} {7,S}
3  C u0 p0 c0 {1,S} {8,D} {9,S}
4  C u0 p0 c0 {2,S} {10,D} {11,S}
5  O u0 p2 c0 {1,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  O u0 p2 c0 {3,D}
9  H u0 p0 c0 {3,S}
10 O u0 p2 c0 {4,D}
11 H u0 p0 c0 {4,S}
12 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.25349,0.070215,-0.000109372,1.04092e-07,-4.21649e-11,-8770.58,14.7918], Tmin=(10,'K'), Tmax=(582.97,'K')),
            NASAPolynomial(coeffs=[8.0135,0.0375547,-2.53367e-05,7.99143e-09,-9.53578e-13,-9325.57,-5.60392], Tmin=(582.97,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 394,
    label = "[O]OC(O)C=CC=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  C u0 p0 c0 {3,S} {10,D} {11,S}
5  O u0 p2 c0 {1,S} {12,S}
6  O u0 p2 c0 {1,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 O u0 p2 c0 {4,D}
11 H u0 p0 c0 {4,S}
12 O u1 p2 c0 {5,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.2123,0.0820284,-0.000246328,5.25176e-07,-4.36906e-10,-28909.5,14.6985], Tmin=(10,'K'), Tmax=(366.85,'K')),
            NASAPolynomial(coeffs=[4.98415,0.0460262,-3.09054e-05,9.73007e-09,-1.16062e-12,-28927.3,9.45714], Tmin=(366.85,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 395,
    label = "O=C[CH]C(O)C=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u1 p0 c0 {1,S} {4,S} {7,S}
3  C u0 p0 c0 {1,S} {8,D} {9,S}
4  C u0 p0 c0 {2,S} {10,D} {11,S}
5  O u0 p2 c0 {1,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  O u0 p2 c0 {3,D}
9  H u0 p0 c0 {3,S}
10 O u0 p2 c0 {4,D}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80425,0.0201309,0.000240706,-1.03294e-06,1.4663e-09,-38019.9,12.2678], Tmin=(10,'K'), Tmax=(178.09,'K')),
            NASAPolynomial(coeffs=[2.32801,0.0532897,-3.85934e-05,1.26494e-08,-1.54635e-12,-37967.3,16.8426], Tmin=(178.09,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 396,
    label = "C=C=CC([O])C=CC=O",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {3,S}
2  O u0 p2 c0 {7,D}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {10,S}
4  C u0 p0 c0 {3,S} {6,D} {11,S}
5  C u0 p0 c0 {3,S} {9,D} {12,S}
6  C u0 p0 c0 {4,D} {7,S} {13,S}
7  C u0 p0 c0 {2,D} {6,S} {14,S}
8  C u0 p0 c0 {9,D} {15,S} {16,S}
9  C u0 p0 c0 {5,D} {8,D}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.17892,0.0808869,-0.000150356,2.40103e-07,-1.68305e-10,20448.5,15.0421], Tmin=(10,'K'), Tmax=(405.85,'K')),
            NASAPolynomial(coeffs=[4.88497,0.0571133,-3.67703e-05,1.12716e-08,-1.32113e-12,20367.3,9.05589], Tmin=(405.85,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 397,
    label = "[CH2]CC#CC=C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {9,S} {10,S}
3  C u0 p0 c0 {4,D} {6,S} {11,S}
4  C u0 p0 c0 {3,D} {12,S} {13,S}
5  C u0 p0 c0 {1,S} {6,T}
6  C u0 p0 c0 {3,S} {5,T}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.46737,0.0538131,-0.000126946,2.70115e-07,-2.16214e-10,50907.9,13.7974], Tmin=(10,'K'), Tmax=(427.54,'K')),
            NASAPolynomial(coeffs=[2.39463,0.0445101,-2.64548e-05,7.61457e-09,-8.49739e-13,51176.3,20.1283], Tmin=(427.54,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 398,
    label = "[CH]=C=C=CC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {4,D}
4  C u0 p0 c0 {3,D} {5,D}
5  C u1 p0 c0 {4,D} {10,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86397,0.0146926,0.000226208,-1.18196e-06,1.90981e-09,54007.2,10.1167], Tmin=(10,'K'), Tmax=(208.01,'K')),
            NASAPolynomial(coeffs=[3.90559,0.0312871,-1.88941e-05,5.60276e-09,-6.46593e-13,53967.9,9.07664], Tmin=(208.01,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 399,
    label = "CC=C=C1[CH]C1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,S} {6,D}
4  C u1 p0 c0 {1,S} {3,S} {12,S}
5  C u0 p0 c0 {2,S} {6,D} {13,S}
6  C u0 p0 c0 {3,D} {5,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.60371,0.0359471,-5.64233e-06,-1.27405e-08,6.07317e-12,57680.3,11.0994], Tmin=(10,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.57499,0.0366175,-1.94813e-05,5.0409e-09,-5.11049e-13,56858.3,-0.549767], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 400,
    label = "[O]C=CC(=CO)O[O]",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {3,D} {5,S}
2  C u1 p0 c0 {1,S} {4,S} {7,S}
3  C u0 p0 c0 {1,D} {6,S} {8,S}
4  C u0 p0 c0 {2,S} {9,D} {10,S}
5  O u0 p2 c0 {1,S} {11,S}
6  O u0 p2 c0 {3,S} {12,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  O u0 p2 c0 {4,D}
10 H u0 p0 c0 {4,S}
11 O u1 p2 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77342,0.0189135,0.000222805,-7.23557e-07,7.0968e-10,-13507.6,12.8796], Tmin=(10,'K'), Tmax=(335.98,'K')),
            NASAPolynomial(coeffs=[3.06888,0.0521741,-3.67326e-05,1.17658e-08,-1.41612e-12,-13600.7,13.421], Tmin=(335.98,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 401,
    label = "[O]OC(C=O)C=CO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {6,S} {10,S}
4  C u0 p0 c0 {1,S} {9,D} {11,S}
5  O u0 p2 c0 {1,S} {12,S}
6  O u0 p2 c0 {3,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {4,D}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 O u1 p2 c0 {5,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.6371,0.0543541,-4.11756e-05,1.44042e-08,-1.83261e-12,-26583.7,14.7124], Tmin=(10,'K'), Tmax=(1364.82,'K')),
            NASAPolynomial(coeffs=[17.7553,0.0191382,-9.24366e-06,2.11445e-09,-1.87367e-13,-31011.4,-59.8934], Tmin=(1364.82,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 402,
    label = "O=CC=CO",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {5,S}
2 C u0 p0 c0 {1,D} {4,S} {6,S}
3 C u0 p0 c0 {1,S} {7,D} {8,S}
4 O u0 p2 c0 {2,S} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 O u0 p2 c0 {3,D}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97244,0.00182775,9.71372e-05,-1.90559e-07,1.24051e-10,-34856,9.18745], Tmin=(10,'K'), Tmax=(392.69,'K')),
            NASAPolynomial(coeffs=[1.01871,0.0319395,-1.79781e-05,5.03101e-09,-5.70587e-13,-34624.2,20.6741], Tmin=(392.69,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 403,
    label = "O=C1C=CC1O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {1,S} {4,S} {7,D}
4  C u0 p0 c0 {2,D} {3,S} {9,S}
5  O u0 p2 c0 {1,S} {10,S}
6  H u0 p0 c0 {1,S}
7  O u0 p2 c0 {3,D}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82287,0.0161921,5.23862e-05,-1.04623e-07,5.63985e-11,-15942.9,10.7726], Tmin=(10,'K'), Tmax=(631.15,'K')),
            NASAPolynomial(coeffs=[3.13944,0.0337978,-2.1004e-05,6.22035e-09,-7.06536e-13,-16121,11.6607], Tmin=(631.15,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 404,
    label = "[CH]=CC(O)C=CC=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {5,S} {10,S}
4  C u0 p0 c0 {1,S} {7,D} {11,S}
5  C u0 p0 c0 {3,S} {12,D} {13,S}
6  O u0 p2 c0 {1,S} {14,S}
7  C u1 p0 c0 {4,D} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 O u0 p2 c0 {5,D}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.57148,0.0385831,0.000299362,-1.37566e-06,1.70615e-09,5653.82,13.7947], Tmin=(10,'K'), Tmax=(297.92,'K')),
            NASAPolynomial(coeffs=[7.30994,0.0460791,-2.8845e-05,8.76875e-09,-1.03163e-12,5175.05,-4.01094], Tmin=(297.92,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 405,
    label = "C_CC(=C)O[O]",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {5,T}
4 O u0 p2 c0 {1,S} {8,S}
5 C u0 p0 c0 {3,T} {9,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 O u1 p2 c0 {4,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81744,0.0126203,0.000137229,-3.76588e-07,2.938e-10,40999.6,11.0818], Tmin=(10,'K'), Tmax=(455.12,'K')),
            NASAPolynomial(coeffs=[5.63344,0.0284199,-1.95217e-05,6.3578e-09,-7.83059e-13,40505.3,0.136479], Tmin=(455.12,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 406,
    label = "C#C[CH]C=C[CH2]",
    molecule = 
"""
multiplicity 3
1  C u1 p0 c0 {2,S} {3,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u1 p0 c0 {1,S} {5,S} {9,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  C u0 p0 c0 {3,S} {6,T}
6  C u0 p0 c0 {5,T} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79827,0.0179101,0.000172827,-5.89136e-07,6.09179e-10,63709.5,12.6812], Tmin=(10,'K'), Tmax=(317.46,'K')),
            NASAPolynomial(coeffs=[3.27042,0.0424217,-2.73784e-05,8.50741e-09,-1.01398e-12,63653,13.2046], Tmin=(317.46,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 407,
    label = "C#CC[CH]C(=C)O[O]",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
2  C u1 p0 c0 {1,S} {3,S} {10,S}
3  C u0 p0 c0 {2,S} {4,D} {6,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  C u0 p0 c0 {1,S} {7,T}
6  O u0 p2 c0 {3,S} {13,S}
7  C u0 p0 c0 {5,T} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 O u1 p2 c0 {6,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.66566,0.0254597,0.000214634,-6.5407e-07,5.64609e-10,50655.4,14.8401], Tmin=(10,'K'), Tmax=(408.21,'K')),
            NASAPolynomial(coeffs=[5.57739,0.0499079,-3.38717e-05,1.08999e-08,-1.32948e-12,50139.5,2.92324], Tmin=(408.21,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 408,
    label = "C_CC=CC=C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {1,D} {5,S} {9,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  C u0 p0 c0 {3,S} {6,T}
6  C u0 p0 c0 {5,T} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88572,0.00688675,0.000148567,-2.97018e-07,1.80123e-10,39770.2,10.4433], Tmin=(10,'K'), Tmax=(540.54,'K')),
            NASAPolynomial(coeffs=[1.84655,0.0468415,-3.13068e-05,9.9242e-09,-1.1948e-12,39627.4,15.6665], Tmin=(540.54,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 409,
    label = "[O]OC=C=C=O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {5,S}
2 C u0 p0 c0 {1,D} {4,D}
3 O u0 p2 c0 {1,S} {6,S}
4 C u0 p0 c0 {2,D} {7,D}
5 H u0 p0 c0 {1,S}
6 O u1 p2 c0 {3,S}
7 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82708,0.0142017,8.5311e-05,-2.85229e-07,2.64265e-10,18828.9,11.1512], Tmin=(10,'K'), Tmax=(377.99,'K')),
            NASAPolynomial(coeffs=[4.34065,0.0244347,-1.74743e-05,5.72074e-09,-7.01027e-13,18678.1,7.6926], Tmin=(377.99,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 410,
    label = "C=CC1OC1[CH]C=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {9,S}
3  C u1 p0 c0 {1,S} {6,S} {11,S}
4  C u0 p0 c0 {2,S} {5,D} {10,S}
5  C u0 p0 c0 {4,D} {13,S} {14,S}
6  C u0 p0 c0 {3,S} {12,D} {15,S}
7  O u0 p2 c0 {1,S} {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {6,D}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.59947,0.0448779,9.73494e-06,-4.77936e-08,2.29615e-11,-131.68,14.3382], Tmin=(10,'K'), Tmax=(866.77,'K')),
            NASAPolynomial(coeffs=[7.80068,0.0458224,-2.7086e-05,7.58999e-09,-8.184e-13,-1623.75,-9.73536], Tmin=(866.77,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 411,
    label = "C=CC(O)[C]=CC=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,D} {9,S}
3  C u0 p0 c0 {5,S} {6,D} {10,S}
4  C u0 p0 c0 {2,D} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {11,D} {14,S}
6  C u1 p0 c0 {1,S} {3,D}
7  O u0 p2 c0 {1,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 O u0 p2 c0 {5,D}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.18936,0.0732295,-0.000144991,2.44393e-07,-1.65352e-10,4557.08,14.0799], Tmin=(10,'K'), Tmax=(487.07,'K')),
            NASAPolynomial(coeffs=[2.40803,0.0590865,-3.81204e-05,1.14538e-08,-1.30955e-12,4877.07,19.7908], Tmin=(487.07,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 412,
    label = "C=CC(=O)CO[O]",
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
            NASAPolynomial(coeffs=[3.58779,0.0449399,-3.14766e-05,1.02567e-08,-1.17127e-12,-6224.04,13.2847], Tmin=(10,'K'), Tmax=(1307.03,'K')),
            NASAPolynomial(coeffs=[12.4468,0.0225514,-1.12035e-05,2.68112e-09,-2.51113e-13,-8943.32,-33.3706], Tmin=(1307.03,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 413,
    label = "C=C[CH]OC=CC=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,D} {5,S} {8,S}
2  C u0 p0 c0 {4,D} {6,S} {9,S}
3  C u0 p0 c0 {1,D} {7,S} {11,S}
4  C u0 p0 c0 {2,D} {7,S} {10,S}
5  C u1 p0 c0 {1,S} {13,S} {14,S}
6  C u0 p0 c0 {2,S} {12,D} {15,S}
7  O u0 p2 c0 {3,S} {4,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {6,D}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.60302,0.0488204,-1.11219e-05,-1.69077e-08,8.74179e-12,-6205.59,12.6487], Tmin=(10,'K'), Tmax=(1027.73,'K')),
            NASAPolynomial(coeffs=[10.2402,0.0395686,-2.18184e-05,5.72864e-09,-5.83113e-13,-8445.5,-23.8137], Tmin=(1027.73,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 414,
    label = "O=C1[CH]COOC1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {6,S} {9,S} {10,S}
3  C u1 p0 c0 {2,S} {4,S} {12,S}
4  C u0 p0 c0 {1,S} {3,S} {11,D}
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
            NASAPolynomial(coeffs=[3.91019,0.00530551,0.000142452,-2.67339e-07,1.54479e-10,-10867.3,11.4139], Tmin=(10,'K'), Tmax=(549.35,'K')),
            NASAPolynomial(coeffs=[0.389216,0.0503538,-3.35545e-05,1.05767e-08,-1.26757e-12,-10773.4,23.6255], Tmin=(549.35,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 415,
    label = "[CH2]C1OOCC1=O",
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
            NASAPolynomial(coeffs=[3.70186,0.0257983,5.58269e-05,-1.32791e-07,7.97665e-11,-5793.19,12.4199], Tmin=(10,'K'), Tmax=(576.47,'K')),
            NASAPolynomial(coeffs=[3.44749,0.0425817,-2.69225e-05,8.09865e-09,-9.32439e-13,-6013.4,11.3425], Tmin=(576.47,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 416,
    label = "O=CC1[CH]OC=CC1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {5,D} {11,S}
4  C u1 p0 c0 {1,S} {7,S} {12,S}
5  C u0 p0 c0 {3,D} {7,S} {14,S}
6  C u0 p0 c0 {1,S} {13,D} {15,S}
7  O u0 p2 c0 {4,S} {5,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 O u0 p2 c0 {6,D}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73848,0.0233856,9.22747e-05,-1.77507e-07,9.53021e-11,-7611.17,13.6812], Tmin=(10,'K'), Tmax=(618.39,'K')),
            NASAPolynomial(coeffs=[1.6683,0.0562381,-3.46214e-05,1.01879e-08,-1.15249e-12,-7727.26,19.6649], Tmin=(618.39,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 417,
    label = "[CH]1C=COC=CCO1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,D} {11,S}
3  C u0 p0 c0 {5,D} {6,S} {12,S}
4  C u0 p0 c0 {2,D} {8,S} {14,S}
5  C u0 p0 c0 {3,D} {7,S} {15,S}
6  C u1 p0 c0 {3,S} {8,S} {13,S}
7  O u0 p2 c0 {1,S} {5,S}
8  O u0 p2 c0 {4,S} {6,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88616,0.00704061,0.000188832,-3.74877e-07,2.31539e-10,-651.617,12.6496], Tmin=(10,'K'), Tmax=(510.15,'K')),
            NASAPolynomial(coeffs=[-0.174269,0.0618515,-3.98787e-05,1.22793e-08,-1.44711e-12,-536.279,26.576], Tmin=(510.15,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 418,
    label = "O=C[CH]C1CC=CO1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {6,S} {12,S}
4  C u0 p0 c0 {2,S} {5,D} {11,S}
5  C u0 p0 c0 {4,D} {7,S} {13,S}
6  C u0 p0 c0 {3,S} {14,D} {15,S}
7  O u0 p2 c0 {1,S} {5,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 O u0 p2 c0 {6,D}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84612,0.0300007,5.07056e-05,-8.83784e-08,3.69722e-11,-8935.14,13.3682], Tmin=(10,'K'), Tmax=(873.16,'K')),
            NASAPolynomial(coeffs=[5.70494,0.0487856,-2.84641e-05,7.87679e-09,-8.39815e-13,-10300.4,-1.30676], Tmin=(873.16,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 419,
    label = "C#CC1C=CC1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {2,S} {3,D} {11,S}
5  C u0 p0 c0 {1,S} {6,T}
6  C u0 p0 c0 {5,T} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9253,0.0043958,0.000131751,-2.41057e-07,1.37152e-10,47056.2,10.5922], Tmin=(10,'K'), Tmax=(548.37,'K')),
            NASAPolynomial(coeffs=[0.0803684,0.0482414,-3.13999e-05,9.82927e-09,-1.17885e-12,47240.3,24.6658], Tmin=(548.37,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 420,
    label = "C1=CC=CCC=1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {5,S} {10,S}
4  C u0 p0 c0 {1,S} {6,D} {11,S}
5  C u0 p0 c0 {3,S} {6,D} {12,S}
6  C u0 p0 c0 {4,D} {5,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.13,-0.0121213,0.000200747,-3.45172e-07,1.91137e-10,47436.2,10.3466], Tmin=(10,'K'), Tmax=(569.69,'K')),
            NASAPolynomial(coeffs=[-0.667487,0.0486796,-3.07399e-05,9.2715e-09,-1.07068e-12,47542.8,26.9304], Tmin=(569.69,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 421,
    label = "[CH]=C=C=CC=C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,D} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {1,D} {9,S} {10,S}
4  C u0 p0 c0 {2,D} {5,D}
5  C u0 p0 c0 {4,D} {6,D}
6  C u1 p0 c0 {5,D} {11,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80417,0.0138846,0.000166163,-4.51184e-07,3.57568e-10,65278.7,11.231], Tmin=(10,'K'), Tmax=(436.77,'K')),
            NASAPolynomial(coeffs=[4.68847,0.0376838,-2.51187e-05,7.99086e-09,-9.67246e-13,64897.2,4.21432], Tmin=(436.77,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 422,
    label = "C#CC(O)C=C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {6,T}
5  O u0 p2 c0 {1,S} {11,S}
6  C u0 p0 c0 {4,T} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75548,0.0199734,0.000173079,-5.8441e-07,5.67367e-10,12839.4,11.4438], Tmin=(10,'K'), Tmax=(360.42,'K')),
            NASAPolynomial(coeffs=[4.81266,0.0377784,-2.39551e-05,7.4368e-09,-8.90171e-13,12571.4,4.76095], Tmin=(360.42,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 423,
    label = "C=CC=C[C]=CO[O]",
    molecule = 
"""
multiplicity 3
1  C u1 p0 c0 {2,S} {3,S} {9,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {1,S} {6,D} {10,S}
4  C u0 p0 c0 {2,D} {11,S} {12,S}
5  C u0 p0 c0 {6,D} {7,S} {13,S}
6  C u0 p0 c0 {3,D} {5,D}
7  O u0 p2 c0 {5,S} {14,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 O u1 p2 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68174,0.0242083,0.000223711,-6.68131e-07,5.73694e-10,47116,13.018], Tmin=(10,'K'), Tmax=(404.66,'K')),
            NASAPolynomial(coeffs=[4.89293,0.0533374,-3.66235e-05,1.17736e-08,-1.43031e-12,46681.4,4.11247], Tmin=(404.66,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 424,
    label = "C#C[C](O)C[CH2]",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {4,S} {5,S}
3  C u1 p0 c0 {1,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {6,T}
5  O u0 p2 c0 {2,S} {11,S}
6  C u0 p0 c0 {4,T} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.66127,0.0315171,0.000165506,-7.76798e-07,9.57549e-10,36535.9,13.9172], Tmin=(10,'K'), Tmax=(299.09,'K')),
            NASAPolynomial(coeffs=[5.68799,0.0368318,-2.374e-05,7.43818e-09,-8.95704e-13,36269.7,4.16162], Tmin=(299.09,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 425,
    label = "[CH2]C(C)[C]=O",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u1 p0 c0 {1,S} {9,S} {10,S}
4  C u1 p0 c0 {1,S} {11,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.5929,0.0382624,-6.18343e-05,1.01714e-07,-6.97782e-11,16161.8,13.6772], Tmin=(10,'K'), Tmax=(484.41,'K')),
            NASAPolynomial(coeffs=[3.10513,0.0334202,-1.93743e-05,5.47831e-09,-6.0371e-13,16313.2,16.751], Tmin=(484.41,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 426,
    label = "C1=C[CH][CH]CC=1",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {5,S} {10,S}
4  C u0 p0 c0 {1,S} {6,D} {11,S}
5  C u1 p0 c0 {3,S} {6,S} {12,S}
6  C u1 p0 c0 {4,D} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.12525,-0.0113951,0.000194665,-3.27371e-07,1.76311e-10,53140.8,10.8503], Tmin=(10,'K'), Tmax=(588.86,'K')),
            NASAPolynomial(coeffs=[-0.662091,0.0492186,-3.13016e-05,9.47511e-09,-1.09567e-12,53217.6,27.2754], Tmin=(588.86,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 427,
    label = "[C]1=C[CH]CC=C1",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,D} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {6,S} {11,S}
5  C u0 p0 c0 {2,D} {6,S} {12,S}
6  C u2 p0 c0 {4,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.10896,-0.00968285,0.000179511,-2.93789e-07,1.53595e-10,52619.7,10.1918], Tmin=(10,'K'), Tmax=(604.2,'K')),
            NASAPolynomial(coeffs=[-0.927111,0.0494394,-3.12732e-05,9.41133e-09,-1.0824e-12,52757.7,28.0562], Tmin=(604.2,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 428,
    label = "[CH]1[CH]C=CC=C1",
    molecule = 
"""
multiplicity 3
1  C u1 p0 c0 {2,S} {6,S} {8,S}
2  C u1 p0 c0 {1,S} {3,S} {10,S}
3  C u0 p0 c0 {2,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {5,S} {11,S}
5  C u0 p0 c0 {4,S} {6,D} {7,S}
6  C u0 p0 c0 {1,S} {5,D} {12,S}
7  H u0 p0 c0 {5,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89481,0.00616854,0.000140989,-2.6928e-07,1.56327e-10,52059,8.22353], Tmin=(10,'K'), Tmax=(562.5,'K')),
            NASAPolynomial(coeffs=[1.52573,0.0468386,-3.09939e-05,9.84817e-09,-1.19571e-12,51948.7,14.9398], Tmin=(562.5,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 429,
    label = "[CH]1CC2[CH]C=C12",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {4,S} {6,S}
4  C u1 p0 c0 {2,S} {3,S} {11,S}
5  C u0 p0 c0 {1,S} {6,D} {10,S}
6  C u0 p0 c0 {3,S} {5,D} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.13118,-0.0118683,0.000200998,-3.37334e-07,1.80216e-10,81519.7,11.4045], Tmin=(10,'K'), Tmax=(600.39,'K')),
            NASAPolynomial(coeffs=[-0.3032,0.0495407,-3.20361e-05,9.82163e-09,-1.14563e-12,81477.9,25.7526], Tmin=(600.39,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 430,
    label = "C=CC=C=O",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,D} {5,S}
2 C u0 p0 c0 {1,S} {4,D} {6,S}
3 C u0 p0 c0 {1,D} {7,S} {8,S}
4 C u0 p0 c0 {2,D} {9,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89903,0.0064048,0.000110222,-2.45773e-07,1.64133e-10,1616.57,9.01247], Tmin=(10,'K'), Tmax=(505.4,'K')),
            NASAPolynomial(coeffs=[3.68559,0.0289495,-1.8588e-05,5.79015e-09,-6.9486e-13,1371.79,7.26151], Tmin=(505.4,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 431,
    label = "C=C[CH][C]=O",
    molecule = 
"""
multiplicity 3
1 O u0 p2 c0 {5,D}
2 C u0 p0 c0 {3,S} {4,D} {6,S}
3 C u1 p0 c0 {2,S} {5,S} {7,S}
4 C u0 p0 c0 {2,D} {8,S} {9,S}
5 C u1 p0 c0 {1,D} {3,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88902,0.00760049,0.000122704,-3.07175e-07,2.31311e-10,21872.2,9.87122], Tmin=(10,'K'), Tmax=(448.44,'K')),
            NASAPolynomial(coeffs=[3.84092,0.0288388,-1.79421e-05,5.39435e-09,-6.30681e-13,21667.3,7.73177], Tmin=(448.44,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 432,
    label = "C=[C]C=C=C=C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,D} {5,S} {7,S}
2  C u0 p0 c0 {4,D} {8,S} {9,S}
3  C u1 p0 c0 {6,S} {10,S} {11,S}
4  C u0 p0 c0 {1,D} {2,D}
5  C u0 p0 c0 {1,S} {6,T}
6  C u0 p0 c0 {3,S} {5,T}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81735,0.0144739,0.000173142,-5.43048e-07,5.07584e-10,63084.1,11.0057], Tmin=(10,'K'), Tmax=(364.33,'K')),
            NASAPolynomial(coeffs=[4.0846,0.0368614,-2.32819e-05,7.13801e-09,-8.44041e-13,62896.6,7.6798], Tmin=(364.33,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 433,
    label = "[O]C1=COOC1",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2 C u0 p0 c0 {1,S} {3,D} {8,S}
3 C u0 p0 c0 {2,D} {5,S} {9,S}
4 O u0 p2 c0 {1,S} {5,S}
5 O u0 p2 c0 {3,S} {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 O u1 p2 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91917,0.00480423,0.000106844,-2.09054e-07,1.23964e-10,-9611.36,10.8228], Tmin=(10,'K'), Tmax=(551.45,'K')),
            NASAPolynomial(coeffs=[2.24271,0.0348648,-2.36148e-05,7.52548e-09,-9.0849e-13,-9698.64,15.4451], Tmin=(551.45,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 434,
    label = "CC1OO[CH]C1=O",
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
            NASAPolynomial(coeffs=[3.81145,0.0146725,0.000130699,-3.09123e-07,2.17743e-10,-15414.4,12.5303], Tmin=(10,'K'), Tmax=(464.58,'K')),
            NASAPolynomial(coeffs=[2.4803,0.0452109,-2.94946e-05,9.13707e-09,-1.07905e-12,-15496.6,15.7161], Tmin=(464.58,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 435,
    label = "CC(=O)C(=O)C=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,D}
3  C u0 p0 c0 {2,S} {4,S} {9,D}
4  C u0 p0 c0 {3,S} {10,D} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {2,D}
9  O u0 p2 c0 {3,D}
10 O u0 p2 c0 {4,D}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.16395,0.0861416,-0.000332283,6.93734e-07,-5.24655e-10,-46348.6,11.3484], Tmin=(10,'K'), Tmax=(418.49,'K')),
            NASAPolynomial(coeffs=[5.39905,0.0317094,-1.86498e-05,5.28097e-09,-5.7936e-13,-46246.1,5.97202], Tmin=(418.49,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 436,
    label = "CC(=O)C(O)=C[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u1 p0 c0 {3,S} {4,S} {5,S}
3  C u0 p0 c0 {1,S} {2,S} {9,D}
4  C u0 p0 c0 {2,S} {10,D} {11,S}
5  O u0 p2 c0 {2,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u0 p2 c0 {3,D}
10 O u0 p2 c0 {4,D}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9587,0.00508222,0.00044071,-2.47708e-06,4.80695e-09,-49534.1,11.7223], Tmin=(10,'K'), Tmax=(153.89,'K')),
            NASAPolynomial(coeffs=[2.99966,0.0412988,-2.23339e-05,5.53559e-09,-5.23069e-13,-49517.9,14.1199], Tmin=(153.89,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 437,
    label = "CCC1OC1O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {6,S} {10,S}
4  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {3,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.66599,0.0379936,-9.9461e-06,-6.32479e-09,3.11814e-12,-39718.5,11.97], Tmin=(10,'K'), Tmax=(1226.08,'K')),
            NASAPolynomial(coeffs=[8.89262,0.0315355,-1.50052e-05,3.47297e-09,-3.16522e-13,-41796.4,-17.5578], Tmin=(1226.08,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 438,
    label = "CCC(C=O)OO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,D} {14,S}
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
            NASAPolynomial(coeffs=[3.58114,0.0355887,0.000190427,-6.98061e-07,6.92796e-10,-39393.2,11.9943], Tmin=(10,'K'), Tmax=(361.33,'K')),
            NASAPolynomial(coeffs=[5.6264,0.0513538,-3.44561e-05,1.10227e-08,-1.34077e-12,-39791.8,0.73983], Tmin=(361.33,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 439,
    label = "[O]C=C(O)C=O",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 C u0 p0 c0 {1,S} {6,D} {8,S}
3 C u0 p0 c0 {1,S} {5,D} {7,S}
4 O u0 p2 c0 {1,S} {9,S}
5 O u0 p2 c0 {3,D}
6 O u0 p2 c0 {2,D}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89544,0.0075492,0.000142708,-3.81144e-07,3.1284e-10,-42185.1,10.9154], Tmin=(10,'K'), Tmax=(405.14,'K')),
            NASAPolynomial(coeffs=[3.55221,0.0309298,-1.78753e-05,4.89853e-09,-5.33558e-13,-42321.3,10.2363], Tmin=(405.14,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 440,
    label = "CC([O])C(=O)C=O",
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
            NASAPolynomial(coeffs=[3.37317,0.0651419,-0.000194505,4.2809e-07,-3.56366e-10,-27851.2,13.8748], Tmin=(10,'K'), Tmax=(387.54,'K')),
            NASAPolynomial(coeffs=[3.77143,0.0413709,-2.6402e-05,8.00638e-09,-9.28885e-13,-27734.4,14.2358], Tmin=(387.54,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 441,
    label = "C1=CC2C=CC12",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {8,S}
3  C u0 p0 c0 {1,S} {4,D} {9,S}
4  C u0 p0 c0 {2,S} {3,D} {11,S}
5  C u0 p0 c0 {1,S} {6,D} {10,S}
6  C u0 p0 c0 {2,S} {5,D} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.23341,-0.0193882,0.00021959,-3.49832e-07,1.79517e-10,47210.2,8.82197], Tmin=(10,'K'), Tmax=(621.41,'K')),
            NASAPolynomial(coeffs=[-1.26106,0.0504889,-3.23843e-05,9.85896e-09,-1.1432e-12,47226.8,27.3544], Tmin=(621.41,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 442,
    label = "C1=CC2=CC2C1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {6,S}
4  C u0 p0 c0 {1,S} {3,D} {11,S}
5  C u0 p0 c0 {2,S} {6,D} {10,S}
6  C u0 p0 c0 {3,S} {5,D} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.15984,-0.0142864,0.000208075,-3.49671e-07,1.88878e-10,53536.5,10.2754], Tmin=(10,'K'), Tmax=(588.28,'K')),
            NASAPolynomial(coeffs=[-0.705276,0.0492018,-3.13416e-05,9.51109e-09,-1.10241e-12,53582.8,26.6934], Tmin=(588.28,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 443,
    label = "O=[C]C(=O)C=O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 C u0 p0 c0 {1,S} {5,D} {6,S}
3 C u0 p0 c0 {1,D} {7,D}
4 O u1 p2 c0 {1,S}
5 O u0 p2 c0 {2,D}
6 H u0 p0 c0 {2,S}
7 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63025,0.0288957,-2.54567e-05,1.21546e-08,-2.57917e-12,-24813.6,11.2482], Tmin=(10,'K'), Tmax=(939.66,'K')),
            NASAPolynomial(coeffs=[5.26885,0.0219205,-1.43219e-05,4.25475e-09,-4.77404e-13,-25121.5,3.44487], Tmin=(939.66,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 444,
    label = "C=CC(=C)C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  C u0 p0 c0 {2,S} {5,D} {9,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  C u0 p0 c0 {3,D} {12,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89909,0.00602309,0.000143829,-2.77868e-07,1.64864e-10,7352.9,9.50171], Tmin=(10,'K'), Tmax=(545.18,'K')),
            NASAPolynomial(coeffs=[1.36093,0.0468847,-2.97849e-05,9.25553e-09,-1.11108e-12,7299.15,17.176], Tmin=(545.18,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 445,
    label = "[CH2][CH]C(=C)C",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  C u0 p0 c0 {2,S} {5,D} {9,S}
4  C u1 p0 c0 {2,S} {10,S} {11,S}
5  C u0 p0 c0 {3,D} {12,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83185,0.0145976,0.000233485,-8.5002e-07,9.49828e-10,35215.7,11.1053], Tmin=(10,'K'), Tmax=(301.38,'K')),
            NASAPolynomial(coeffs=[3.91161,0.0398245,-2.2897e-05,6.50203e-09,-7.27151e-13,35091.5,8.8357], Tmin=(301.38,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 446,
    label = "[CH2]C1CC1O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3  C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
4  C u1 p0 c0 {1,S} {10,S} {11,S}
5  O u0 p2 c0 {2,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86642,0.00848157,0.00014922,-3.31387e-07,2.21351e-10,5106.59,11.1945], Tmin=(10,'K'), Tmax=(503.91,'K')),
            NASAPolynomial(coeffs=[3.48386,0.039199,-2.46146e-05,7.6023e-09,-9.10035e-13,4793.7,9.29077], Tmin=(503.91,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 447,
    label = "[CH2]C1(O)CC1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
4  C u1 p0 c0 {1,S} {10,S} {11,S}
5  O u0 p2 c0 {1,S} {12,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87486,0.00743901,0.000139886,-2.82265e-07,1.70454e-10,4234.6,9.50241], Tmin=(10,'K'), Tmax=(557.37,'K')),
            NASAPolynomial(coeffs=[3.18118,0.0408682,-2.66471e-05,8.50536e-09,-1.04441e-12,3870,8.47914], Tmin=(557.37,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 448,
    label = "C=C(C)C(C)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {3,S} {5,D}
5  C u0 p0 c0 {4,D} {14,S} {15,S}
6  O u0 p2 c0 {1,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 O u1 p2 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.33031,0.0622968,-9.00076e-05,1.29557e-07,-8.35686e-11,-1428.79,14.8417], Tmin=(10,'K'), Tmax=(485.68,'K')),
            NASAPolynomial(coeffs=[3.36351,0.0526326,-3.1157e-05,8.96506e-09,-1.0019e-12,-1321.26,15.8458], Tmin=(485.68,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 449,
    label = "CC=C(C)CO[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {5,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {2,S} {5,D}
5  C u0 p0 c0 {3,S} {4,D} {15,S}
6  O u0 p2 c0 {1,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 O u1 p2 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.34935,0.0651242,-0.00015335,3.20954e-07,-2.50472e-10,-268.027,14.0659], Tmin=(10,'K'), Tmax=(440.8,'K')),
            NASAPolynomial(coeffs=[1.81427,0.0542035,-3.16231e-05,8.95857e-09,-9.86928e-13,108.734,22.9528], Tmin=(440.8,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 450,
    label = "C[C]1COOC1C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {8,S}
2  C u0 p0 c0 {5,S} {7,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
5  C u1 p0 c0 {1,S} {2,S} {4,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {2,S} {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80818,0.0340068,2.11162e-05,-4.0336e-08,1.46497e-11,-999.629,13.6517], Tmin=(10,'K'), Tmax=(1057.64,'K')),
            NASAPolynomial(coeffs=[6.46418,0.0444512,-2.27558e-05,5.63496e-09,-5.46447e-13,-2707.42,-4.72843], Tmin=(1057.64,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 451,
    label = "[CH2]C(=C)C(C)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,S} {5,D}
4  C u1 p0 c0 {3,S} {14,S} {15,S}
5  C u0 p0 c0 {3,D} {12,S} {13,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {6,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61961,0.0307797,0.000240647,-8.1432e-07,7.78082e-10,-1178.63,12.4796], Tmin=(10,'K'), Tmax=(370.25,'K')),
            NASAPolynomial(coeffs=[5.66896,0.0537361,-3.50525e-05,1.1052e-08,-1.33463e-12,-1639.49,0.454608], Tmin=(370.25,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 452,
    label = "C=CC=CO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {6,S}
2  C u0 p0 c0 {1,S} {4,D} {7,S}
3  C u0 p0 c0 {1,D} {5,S} {8,S}
4  C u0 p0 c0 {2,D} {9,S} {10,S}
5  O u0 p2 c0 {3,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88423,0.00676448,0.000129965,-2.56195e-07,1.50509e-10,-9148.33,9.11677], Tmin=(10,'K'), Tmax=(571.94,'K')),
            NASAPolynomial(coeffs=[2.9534,0.0400115,-2.73525e-05,8.91528e-09,-1.10116e-12,-9479.15,9.26446], Tmin=(571.94,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 453,
    label = "C=C[CH][CH]O",
    molecule = 
"""
multiplicity 3
1  C u1 p0 c0 {2,S} {3,S} {6,S}
2  C u0 p0 c0 {1,S} {4,D} {7,S}
3  C u1 p0 c0 {1,S} {5,S} {8,S}
4  C u0 p0 c0 {2,D} {9,S} {10,S}
5  O u0 p2 c0 {3,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80113,0.0172415,0.00014949,-5.1053e-07,5.16502e-10,18527.1,10.8077], Tmin=(10,'K'), Tmax=(332.87,'K')),
            NASAPolynomial(coeffs=[3.75475,0.0367423,-2.37491e-05,7.39482e-09,-8.83033e-13,18425.3,9.40402], Tmin=(332.87,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 454,
    label = "O=C1CC1=O",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,S} {6,D}
3 C u0 p0 c0 {1,S} {2,S} {7,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
7 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76157,0.021692,-9.31439e-06,-4.03591e-09,3.44809e-12,-1270.12,9.14548], Tmin=(10,'K'), Tmax=(871.61,'K')),
            NASAPolynomial(coeffs=[5.71401,0.0174564,-1.01559e-05,2.82678e-09,-3.04096e-13,-1789.93,-1.03509], Tmin=(871.61,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 455,
    label = "O=[C]CC(CO)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  O u0 p2 c0 {1,S} {7,S}
5  O u0 p2 c0 {3,S} {14,S}
6  C u1 p0 c0 {2,S} {13,D}
7  O u0 p2 c0 {4,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {6,D}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.43283,0.0675857,0.000298338,-2.85206e-06,6.0701e-09,-39886.1,13.6984], Tmin=(10,'K'), Tmax=(186.83,'K')),
            NASAPolynomial(coeffs=[6.95071,0.0506888,-3.50605e-05,1.14184e-08,-1.40496e-12,-40119.5,-0.100541], Tmin=(186.83,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 456,
    label = "[O]OCC1OOCC1OO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {8,S}
2  O u0 p2 c0 {1,S} {9,S}
3  O u0 p2 c0 {5,S} {7,S}
4  O u0 p2 c0 {6,S} {10,S}
5  O u0 p2 c0 {3,S} {17,S}
6  O u1 p2 c0 {4,S}
7  C u0 p0 c0 {3,S} {8,S} {9,S} {11,S}
8  C u0 p0 c0 {1,S} {7,S} {10,S} {12,S}
9  C u0 p0 c0 {2,S} {7,S} {13,S} {14,S}
10 C u0 p0 c0 {4,S} {8,S} {15,S} {16,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {9,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {10,S}
16 H u0 p0 c0 {10,S}
17 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.93836,0.111331,-0.000357973,7.97585e-07,-6.7427e-10,-23716.5,16.3289], Tmin=(10,'K'), Tmax=(373.06,'K')),
            NASAPolynomial(coeffs=[4.58814,0.0631339,-4.15173e-05,1.28708e-08,-1.51754e-12,-23627.3,12.8417], Tmin=(373.06,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 457,
    label = "[CH2]C(=CC)COO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {4,S} {5,D}
4  C u1 p0 c0 {2,S} {3,S} {13,S}
5  C u0 p0 c0 {3,D} {14,S} {15,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {6,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.17865,0.0771363,-0.000153824,2.39333e-07,-1.5204e-10,120.636,13.1201], Tmin=(10,'K'), Tmax=(479.07,'K')),
            NASAPolynomial(coeffs=[4.65638,0.0512739,-3.05028e-05,8.79438e-09,-9.83879e-13,134.242,8.69805], Tmin=(479.07,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 458,
    label = "C1OOCC2OC12",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {7,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {3,S} {7,S}
7  O u0 p2 c0 {4,S} {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.068,-0.00673326,0.000188165,-3.15281e-07,1.67409e-10,-18485.8,10.6073], Tmin=(10,'K'), Tmax=(596.17,'K')),
            NASAPolynomial(coeffs=[-1.08143,0.0549123,-3.5112e-05,1.06306e-08,-1.22717e-12,-18353.4,28.7485], Tmin=(596.17,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 459,
    label = "CC1=CCC1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {3,S} {5,D}
5  C u0 p0 c0 {2,S} {4,D} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9584,0.00231974,0.000119316,-2.0032e-07,1.09361e-10,12403,9.49324], Tmin=(10,'K'), Tmax=(472.17,'K')),
            NASAPolynomial(coeffs=[-1.52051,0.0487323,-2.81211e-05,7.84079e-09,-8.48545e-13,12920.4,31.8146], Tmin=(472.17,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 460,
    label = "[CH2]C1(C)CC1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
4  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
5  C u1 p0 c0 {1,S} {13,S} {14,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89979,0.00641794,0.000163589,-3.41737e-07,2.23669e-10,20020.2,9.95808], Tmin=(10,'K'), Tmax=(484.03,'K')),
            NASAPolynomial(coeffs=[1.14696,0.0489607,-2.959e-05,8.81562e-09,-1.02519e-12,20054.8,18.8462], Tmin=(484.03,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 461,
    label = "C[CH]C[C]=O",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {2,S} {10,S}
4  C u1 p0 c0 {1,S} {11,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.22348,0.075467,-0.000285097,5.59115e-07,-3.85868e-10,15117,12.2738], Tmin=(10,'K'), Tmax=(474.74,'K')),
            NASAPolynomial(coeffs=[3.88137,0.0300666,-1.57125e-05,3.96969e-09,-3.91746e-13,15503.7,14.3204], Tmin=(474.74,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 462,
    label = "C=CC[CH]OC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {6,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {5,D} {12,S}
4  C u1 p0 c0 {1,S} {6,S} {13,S}
5  C u0 p0 c0 {3,D} {14,S} {15,S}
6  O u0 p2 c0 {2,S} {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.25335,0.0633868,-9.9805e-05,1.21943e-07,-6.24004e-11,2847.9,11.6878], Tmin=(10,'K'), Tmax=(591.09,'K')),
            NASAPolynomial(coeffs=[4.43347,0.044664,-2.50463e-05,6.89587e-09,-7.44346e-13,2895.96,8.2015], Tmin=(591.09,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 463,
    label = "[O]C=CCC=CC=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,D} {10,S}
3  C u1 p0 c0 {1,S} {5,S} {9,S}
4  C u0 p0 c0 {2,D} {6,S} {11,S}
5  C u0 p0 c0 {3,S} {12,D} {14,S}
6  C u0 p0 c0 {4,S} {13,D} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 O u0 p2 c0 {5,D}
13 O u0 p2 c0 {6,D}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.29527,0.0727793,-0.000182926,4.02342e-07,-3.42725e-10,-9316.08,14.7643], Tmin=(10,'K'), Tmax=(387.64,'K')),
            NASAPolynomial(coeffs=[2.97378,0.0553767,-3.54084e-05,1.0751e-08,-1.24878e-12,-9135.48,18.0186], Tmin=(387.64,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 464,
    label = "OC1C=CC1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {4,D} {9,S}
4  C u0 p0 c0 {2,S} {3,D} {10,S}
5  O u0 p2 c0 {1,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93509,0.00402435,0.000119053,-2.32901e-07,1.4334e-10,-2284.74,9.561], Tmin=(10,'K'), Tmax=(504.19,'K')),
            NASAPolynomial(coeffs=[1.09196,0.0394248,-2.44779e-05,7.40865e-09,-8.68226e-13,-2161.3,19.7115], Tmin=(504.19,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 465,
    label = "O[CH]C(CCOO)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
4  C u1 p0 c0 {1,S} {7,S} {15,S}
5  O u0 p2 c0 {1,S} {8,S}
6  O u0 p2 c0 {3,S} {9,S}
7  O u0 p2 c0 {4,S} {16,S}
8  O u0 p2 c0 {5,S} {18,S}
9  O u0 p2 c0 {6,S} {17,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.46155,0.0362456,0.000337234,-9.21695e-07,6.92821e-10,-39232.7,14.7785], Tmin=(10,'K'), Tmax=(481.9,'K')),
            NASAPolynomial(coeffs=[10.7143,0.0688905,-5.33824e-05,1.85015e-08,-2.35122e-12,-41009.8,-26.1029], Tmin=(481.9,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 466,
    label = "O=CC=C[CH]CC=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {4,S} {10,S}
4  C u1 p0 c0 {3,S} {6,S} {11,S}
5  C u0 p0 c0 {1,S} {12,D} {13,S}
6  C u0 p0 c0 {4,S} {14,D} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 O u0 p2 c0 {5,D}
13 H u0 p0 c0 {5,S}
14 O u0 p2 c0 {6,D}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.09248,0.0957969,-0.000346593,7.98095e-07,-6.63629e-10,-14710.8,14.2258], Tmin=(10,'K'), Tmax=(396.01,'K')),
            NASAPolynomial(coeffs=[3.16061,0.0541349,-3.35905e-05,9.91062e-09,-1.12315e-12,-14394.9,18.0168], Tmin=(396.01,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 467,
    label = "CC=CC=C=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {4,S} {10,S}
4  C u0 p0 c0 {3,S} {5,D} {11,S}
5  C u0 p0 c0 {4,D} {12,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 O u0 p2 c0 {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82889,0.0149136,0.000205818,-7.40661e-07,8.14156e-10,-2600.77,10.2102], Tmin=(10,'K'), Tmax=(304.72,'K')),
            NASAPolynomial(coeffs=[3.75183,0.038732,-2.36958e-05,7.0865e-09,-8.23109e-13,-2701.96,8.75298], Tmin=(304.72,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 468,
    label = "C=C[CH]C(C=O)O[O]",
    molecule = 
"""
multiplicity 3
1  O u0 p2 c0 {3,S} {4,S}
2  O u0 p2 c0 {7,D}
3  O u1 p2 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {7,S} {9,S}
5  C u1 p0 c0 {4,S} {6,S} {10,S}
6  C u0 p0 c0 {5,S} {8,D} {11,S}
7  C u0 p0 c0 {2,D} {4,S} {12,S}
8  C u0 p0 c0 {6,D} {13,S} {14,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.48548,0.0539112,0.000223806,-1.55026e-06,2.50832e-09,9135.57,13.785], Tmin=(10,'K'), Tmax=(241.04,'K')),
            NASAPolynomial(coeffs=[7.06121,0.0445538,-2.89826e-05,9.08059e-09,-1.0913e-12,8817.99,-1.39022], Tmin=(241.04,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 469,
    label = "O=C[CH]C1OCOO1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {8,S}
2  C u0 p0 c0 {5,S} {7,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {4,S} {11,S}
4  C u0 p0 c0 {3,S} {12,D} {13,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {2,S} {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76348,0.0353066,1.6947e-05,-4.76893e-08,2.09842e-11,-26425,13.2702], Tmin=(10,'K'), Tmax=(912.82,'K')),
            NASAPolynomial(coeffs=[7.86806,0.0382756,-2.23671e-05,6.17286e-09,-6.55337e-13,-28047.4,-10.9397], Tmin=(912.82,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 470,
    label = "OCH=CHOH",
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
            NASAPolynomial(coeffs=[4.04709,-0.00456855,9.27948e-05,-1.61279e-07,9.01384e-11,-26105,8.88002], Tmin=(10,'K'), Tmax=(562.06,'K')),
            NASAPolynomial(coeffs=[1.76213,0.0237233,-1.48156e-05,4.44156e-09,-5.11169e-13,-26038.2,16.8967], Tmin=(562.06,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 471,
    label = "C#CC(O)=CC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {10,S}
3  C u0 p0 c0 {2,D} {4,S} {5,S}
4  C u0 p0 c0 {3,S} {6,T}
5  O u0 p2 c0 {3,S} {11,S}
6  C u0 p0 c0 {4,T} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78527,0.0174463,0.000169243,-5.41619e-07,5.10418e-10,7923.65,10.6126], Tmin=(10,'K'), Tmax=(362.85,'K')),
            NASAPolynomial(coeffs=[4.13529,0.0389797,-2.47444e-05,7.66029e-09,-9.13394e-13,7731.09,6.97544], Tmin=(362.85,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 472,
    label = "CC=C=C=O",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C u0 p0 c0 {1,S} {3,D} {8,S}
3 C u0 p0 c0 {2,D} {4,D}
4 C u0 p0 c0 {3,D} {9,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68654,0.0299135,-5.44526e-05,1.0369e-07,-7.69226e-11,8737.18,9.21104], Tmin=(10,'K'), Tmax=(471.72,'K')),
            NASAPolynomial(coeffs=[2.73836,0.0279222,-1.62215e-05,4.57766e-09,-5.02743e-13,8938.25,14.256], Tmin=(471.72,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 473,
    label = "C#CC(=O)O[O]",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {5,D}
2 C u0 p0 c0 {1,S} {4,T}
3 O u0 p2 c0 {1,S} {6,S}
4 C u0 p0 c0 {2,T} {7,S}
5 O u0 p2 c0 {1,D}
6 O u1 p2 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80012,0.0153775,8.16579e-05,-2.45354e-07,1.94474e-10,16789.7,10.8198], Tmin=(10,'K'), Tmax=(460.92,'K')),
            NASAPolynomial(coeffs=[5.66021,0.0223812,-1.64598e-05,5.51032e-09,-6.85401e-13,16372.4,0.619525], Tmin=(460.92,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 474,
    label = "OC=CCCOO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,D} {12,S}
4  C u0 p0 c0 {3,D} {6,S} {13,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {4,S} {14,S}
7  O u0 p2 c0 {5,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98889,0.0460447,-7.7081e-06,-1.66446e-08,7.34897e-12,-34222.4,10.2947], Tmin=(10,'K'), Tmax=(1195.35,'K')),
            NASAPolynomial(coeffs=[17.4403,0.0252113,-1.19066e-05,2.61899e-09,-2.19033e-13,-39165.6,-64.2265], Tmin=(1195.35,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 475,
    label = "O=C(CO)CCOO",
    molecule = 
"""
1  O u0 p2 c0 {3,S} {6,S}
2  O u0 p2 c0 {7,S} {15,S}
3  O u0 p2 c0 {1,S} {16,S}
4  O u0 p2 c0 {8,D}
5  C u0 p0 c0 {6,S} {8,S} {9,S} {10,S}
6  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
7  C u0 p0 c0 {2,S} {8,S} {13,S} {14,S}
8  C u0 p0 c0 {4,D} {5,S} {7,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.05936,0.0788588,-8.5543e-05,5.13989e-08,-1.29543e-11,-61071.2,13.0764], Tmin=(10,'K'), Tmax=(906.64,'K')),
            NASAPolynomial(coeffs=[11.261,0.0426745,-2.56779e-05,7.37954e-09,-8.16289e-13,-62558.4,-25.6878], Tmin=(906.64,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 476,
    label = "CC=C(C=O)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {4,S} {5,S}
4  C u0 p0 c0 {3,S} {10,D} {11,S}
5  O u0 p2 c0 {3,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {4,D}
11 H u0 p0 c0 {4,S}
12 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.47868,0.0481278,-5.72898e-05,6.85249e-08,-4.32256e-11,-6448.05,12.8667], Tmin=(10,'K'), Tmax=(450.52,'K')),
            NASAPolynomial(coeffs=[3.75486,0.0424258,-2.74844e-05,8.40792e-09,-9.80789e-13,-6439.95,12.1206], Tmin=(450.52,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 477,
    label = "C#CC(C)(O)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,T}
4  O u0 p2 c0 {1,S} {11,S}
5  O u0 p2 c0 {1,S} {10,S}
6  C u0 p0 c0 {3,T} {12,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u1 p2 c0 {5,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65932,0.0246322,0.000212345,-6.79245e-07,5.89323e-10,1581.3,12.4201], Tmin=(10,'K'), Tmax=(426.14,'K')),
            NASAPolynomial(coeffs=[8.9324,0.033184,-2.20831e-05,7.15458e-09,-8.88414e-13,604.818,-14.7058], Tmin=(426.14,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 478,
    label = "[O]CCC(=O)CO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {2,S} {13,D}
5  O u0 p2 c0 {2,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u1 p2 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74876,0.0149009,0.000210149,-4.55112e-07,2.81902e-10,-40435,13.4385], Tmin=(10,'K'), Tmax=(568.55,'K')),
            NASAPolynomial(coeffs=[6.56116,0.0521828,-3.87726e-05,1.33075e-08,-1.69586e-12,-41677.2,-6.65323], Tmin=(568.55,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 479,
    label = "O=C1[C]=COO1",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,D} {5,S} {7,S}
2 C u0 p0 c0 {3,S} {4,S} {6,D}
3 C u1 p0 c0 {1,D} {2,S}
4 O u0 p2 c0 {2,S} {5,S}
5 O u0 p2 c0 {1,S} {4,S}
6 O u0 p2 c0 {2,D}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94003,0.00334496,7.73554e-05,-1.39817e-07,7.55082e-11,12541.5,10.0204], Tmin=(10,'K'), Tmax=(608.29,'K')),
            NASAPolynomial(coeffs=[2.26026,0.0288215,-2.10533e-05,7.03656e-09,-8.76003e-13,12478.9,15.0948], Tmin=(608.29,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 480,
    label = "[O]OC1=COOC1=O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {6,S}
2 C u0 p0 c0 {1,D} {5,S} {8,S}
3 C u0 p0 c0 {1,S} {4,S} {7,D}
4 O u0 p2 c0 {3,S} {5,S}
5 O u0 p2 c0 {2,S} {4,S}
6 O u0 p2 c0 {1,S} {9,S}
7 O u0 p2 c0 {3,D}
8 H u0 p0 c0 {2,S}
9 O u1 p2 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80187,0.012482,0.000147594,-3.59672e-07,2.46545e-10,-11716.8,12.3382], Tmin=(10,'K'), Tmax=(522.2,'K')),
            NASAPolynomial(coeffs=[6.68123,0.0311907,-2.32408e-05,7.91371e-09,-1.00124e-12,-12573.3,-5.00411], Tmin=(522.2,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 481,
    label = "C1=CCOC=C1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {4,S} {11,S}
4  C u0 p0 c0 {3,S} {5,D} {10,S}
5  C u0 p0 c0 {4,D} {6,S} {12,S}
6  O u0 p2 c0 {1,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.09534,-0.00833637,0.000165696,-2.65976e-07,1.36591e-10,-1686.34,9.84151], Tmin=(10,'K'), Tmax=(609.4,'K')),
            NASAPolynomial(coeffs=[-1.21042,0.0489291,-3.04936e-05,9.07461e-09,-1.03503e-12,-1456.34,29.3923], Tmin=(609.4,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 482,
    label = "[O]OC1(C=O)OC1=O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {4,S} {6,D}
3 C u0 p0 c0 {1,S} {7,D} {8,S}
4 O u0 p2 c0 {1,S} {2,S}
5 O u0 p2 c0 {1,S} {9,S}
6 O u0 p2 c0 {2,D}
7 O u0 p2 c0 {3,D}
8 H u0 p0 c0 {3,S}
9 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.43968,0.048923,-5.57349e-05,3.20543e-08,-7.37846e-12,-26180,13.9469], Tmin=(10,'K'), Tmax=(1021.96,'K')),
            NASAPolynomial(coeffs=[11.0729,0.0190461,-1.18828e-05,3.44788e-09,-3.80577e-13,-27740.2,-23.0451], Tmin=(1021.96,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 483,
    label = "O=C([CH]O)CCO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,S} {11,D}
4  C u1 p0 c0 {3,S} {6,S} {12,S}
5  O u0 p2 c0 {2,S} {13,S}
6  O u0 p2 c0 {4,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {3,D}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8002,0.0120463,0.000202942,-4.28752e-07,2.66754e-10,-55023.2,12.2991], Tmin=(10,'K'), Tmax=(548.51,'K')),
            NASAPolynomial(coeffs=[3.81209,0.056259,-3.91123e-05,1.26877e-08,-1.55752e-12,-55690.9,6.17422], Tmin=(548.51,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 484,
    label = "O=CC(=O)CCO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,S} {10,D}
4  C u0 p0 c0 {3,S} {11,D} {12,S}
5  O u0 p2 c0 {2,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 O u0 p2 c0 {4,D}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.52438,0.0408448,5.17561e-05,-2.00073e-07,1.56582e-10,-57138.4,12.0767], Tmin=(10,'K'), Tmax=(487.33,'K')),
            NASAPolynomial(coeffs=[5.95733,0.0441216,-2.98827e-05,9.49362e-09,-1.1401e-12,-57651.5,-0.744251], Tmin=(487.33,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 485,
    label = "O=CC(=O)C=O",
    molecule = 
"""
1 O u0 p2 c0 {4,D}
2 O u0 p2 c0 {5,D}
3 O u0 p2 c0 {6,D}
4 C u0 p0 c0 {1,D} {5,S} {6,S}
5 C u0 p0 c0 {2,D} {4,S} {7,S}
6 C u0 p0 c0 {3,D} {4,S} {8,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.54133,0.0411855,-8.72287e-05,1.23323e-07,-7.04689e-11,-38452.9,11.8769], Tmin=(10,'K'), Tmax=(506.24,'K')),
            NASAPolynomial(coeffs=[5.21689,0.0221741,-1.37947e-05,4.0944e-09,-4.67007e-13,-38548.6,5.66443], Tmin=(506.24,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 486,
    label = "C=CC(=O)C=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {5,D}
3  C u0 p0 c0 {1,D} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {7,D} {10,S}
5  O u0 p2 c0 {2,D}
6  H u0 p0 c0 {1,S}
7  O u0 p2 c0 {4,D}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.69275,0.0273442,4.72796e-06,-2.4889e-08,1.13225e-11,-22004,10.4524], Tmin=(10,'K'), Tmax=(909.46,'K')),
            NASAPolynomial(coeffs=[5.49134,0.0303417,-1.82069e-05,5.11116e-09,-5.49382e-13,-22782.3,-0.534156], Tmin=(909.46,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 487,
    label = "O=C([CH]O)COO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,D}
3  C u1 p0 c0 {2,S} {5,S} {10,S}
4  O u0 p2 c0 {1,S} {6,S}
5  O u0 p2 c0 {3,S} {11,S}
6  O u0 p2 c0 {4,S} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u0 p2 c0 {2,D}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.30249,0.0581307,-8.98317e-05,1.05353e-07,-5.34125e-11,-41970.5,13.1647], Tmin=(10,'K'), Tmax=(582.83,'K')),
            NASAPolynomial(coeffs=[4.456,0.0417878,-2.60847e-05,7.63104e-09,-8.55447e-13,-41961.8,9.45025], Tmin=(582.83,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 488,
    label = "[CH2]C=C(C=O)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {3,S} {5,S}
2  C u0 p0 c0 {1,D} {4,S} {7,S}
3  C u0 p0 c0 {1,S} {8,D} {9,S}
4  C u1 p0 c0 {2,S} {10,S} {11,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {12,S}
7  H u0 p0 c0 {2,S}
8  O u0 p2 c0 {3,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.60986,0.0347503,1.04811e-05,-4.18893e-08,2.03509e-11,-11082.5,12.7027], Tmin=(10,'K'), Tmax=(821.76,'K')),
            NASAPolynomial(coeffs=[5.36734,0.0400532,-2.44934e-05,7.00513e-09,-7.66979e-13,-11839.3,1.72198], Tmin=(821.76,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 489,
    label = "C=CC1C=CO1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {9,S}
3  C u0 p0 c0 {1,S} {5,D} {8,S}
4  C u0 p0 c0 {2,D} {6,S} {10,S}
5  C u0 p0 c0 {3,D} {11,S} {12,S}
6  O u0 p2 c0 {1,S} {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89924,0.00616532,0.000141912,-2.85169e-07,1.75906e-10,12454.5,10.6411], Tmin=(10,'K'), Tmax=(525.11,'K')),
            NASAPolynomial(coeffs=[1.69752,0.0443655,-2.84206e-05,8.79537e-09,-1.04665e-12,12390.3,17.0318], Tmin=(525.11,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 490,
    label = "CC1C=CC1=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,D} {11,S}
4  C u0 p0 c0 {1,S} {5,S} {10,D}
5  C u0 p0 c0 {3,D} {4,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {4,D}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9541,0.00333523,0.000158749,-3.59601e-07,2.70453e-10,-705.954,10.8743], Tmin=(10,'K'), Tmax=(339.07,'K')),
            NASAPolynomial(coeffs=[0.365845,0.0456647,-2.85052e-05,8.56175e-09,-9.9004e-13,-462.613,24.3048], Tmin=(339.07,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 491,
    label = "C=C1C=CC1=C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,D}
2  C u0 p0 c0 {1,S} {4,S} {6,D}
3  C u0 p0 c0 {1,S} {4,D} {7,S}
4  C u0 p0 c0 {2,S} {3,D} {8,S}
5  C u0 p0 c0 {1,D} {9,S} {10,S}
6  C u0 p0 c0 {2,D} {11,S} {12,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93037,0.00405873,0.000129747,-2.32359e-07,1.2959e-10,39331.3,8.84354], Tmin=(10,'K'), Tmax=(554.2,'K')),
            NASAPolynomial(coeffs=[-0.346459,0.0494794,-3.25763e-05,1.02861e-08,-1.24127e-12,39581.8,24.9363], Tmin=(554.2,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 492,
    label = "C=C=C[CH]C(=C)O[O]",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {4,D} {7,S}
2  C u1 p0 c0 {1,S} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {6,D} {9,S}
4  C u0 p0 c0 {1,D} {10,S} {11,S}
5  C u0 p0 c0 {6,D} {12,S} {13,S}
6  C u0 p0 c0 {3,D} {5,D}
7  O u0 p2 c0 {1,S} {14,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 O u1 p2 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73046,0.0176247,0.000228795,-5.65828e-07,4.03926e-10,45234.5,13.2673], Tmin=(10,'K'), Tmax=(490.41,'K')),
            NASAPolynomial(coeffs=[5.9597,0.0517965,-3.58609e-05,1.16368e-08,-1.42735e-12,44386.3,-2.31793], Tmin=(490.41,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 493,
    label = "[CH2]C#C[C]=C=C",
    molecule = 
"""
multiplicity 3
1  C u1 p0 c0 {3,S} {7,S} {8,S}
2  C u1 p0 c0 {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,T}
4  C u0 p0 c0 {2,S} {6,T}
5  C u0 p0 c0 {3,T} {6,S}
6  C u0 p0 c0 {4,T} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78377,0.0170207,0.000162515,-5.41774e-07,5.1492e-10,78207.9,9.28362], Tmin=(10,'K'), Tmax=(372.86,'K')),
            NASAPolynomial(coeffs=[5.2696,0.0317964,-2.04962e-05,6.39174e-09,-7.66067e-13,77883.6,0.718079], Tmin=(372.86,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 494,
    label = "C=C=C1[CH]C1=C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,D}
2  C u0 p0 c0 {1,S} {3,S} {6,D}
3  C u1 p0 c0 {1,S} {2,S} {7,S}
4  C u0 p0 c0 {1,D} {8,S} {9,S}
5  C u0 p0 c0 {6,D} {10,S} {11,S}
6  C u0 p0 c0 {2,D} {5,D}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85959,0.00899913,0.00014894,-3.39173e-07,2.3056e-10,72661.5,10.81], Tmin=(10,'K'), Tmax=(498.49,'K')),
            NASAPolynomial(coeffs=[3.77249,0.0381977,-2.46797e-05,7.71176e-09,-9.26306e-13,72316.1,7.61786], Tmin=(498.49,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 495,
    label = "C=C1[C]=CC1=C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,D}
2  C u0 p0 c0 {1,S} {5,D} {6,S}
3  C u0 p0 c0 {1,S} {6,D} {7,S}
4  C u0 p0 c0 {1,D} {8,S} {9,S}
5  C u0 p0 c0 {2,D} {10,S} {11,S}
6  C u1 p0 c0 {2,S} {3,D}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91777,0.00479684,0.000123489,-2.29424e-07,1.30688e-10,70758,10.2606], Tmin=(10,'K'), Tmax=(562.73,'K')),
            NASAPolynomial(coeffs=[1.05299,0.0435545,-2.8854e-05,9.14602e-09,-1.10649e-12,70789.2,19.8466], Tmin=(562.73,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 496,
    label = "C=C1[CH]C(O[O])C1=C",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {5,D}
3  C u0 p0 c0 {2,S} {4,S} {6,D}
4  C u1 p0 c0 {1,S} {3,S} {9,S}
5  C u0 p0 c0 {2,D} {12,S} {13,S}
6  C u0 p0 c0 {3,D} {10,S} {11,S}
7  O u0 p2 c0 {1,S} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 O u1 p2 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.60194,0.0356644,4.57436e-05,-1.17102e-07,6.63973e-11,46649.3,14.0585], Tmin=(10,'K'), Tmax=(640.52,'K')),
            NASAPolynomial(coeffs=[4.46202,0.0493613,-3.09863e-05,9.23661e-09,-1.05369e-12,46148,7.23892], Tmin=(640.52,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 497,
    label = "C=C1C=C[C]1CO[O]",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  C u0 p0 c0 {2,S} {5,S} {6,D}
4  C u0 p0 c0 {2,S} {5,D} {11,S}
5  C u0 p0 c0 {3,S} {4,D} {10,S}
6  C u0 p0 c0 {3,D} {12,S} {13,S}
7  O u0 p2 c0 {1,S} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 O u1 p2 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61898,0.0439998,-9.34065e-06,-1.60795e-08,8.29954e-12,49636,14.9968], Tmin=(10,'K'), Tmax=(1004.98,'K')),
            NASAPolynomial(coeffs=[8.92412,0.0371463,-2.03981e-05,5.37657e-09,-5.50666e-13,47849.5,-14.207], Tmin=(1004.98,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 498,
    label = "O=C1C=CC1",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {4,D} {8,S}
3 C u0 p0 c0 {1,S} {4,S} {7,D}
4 C u0 p0 c0 {2,D} {3,S} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {3,D}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.07884,-0.00695692,0.000125253,-2.04365e-07,1.06674e-10,3538.79,8.99633], Tmin=(10,'K'), Tmax=(604.13,'K')),
            NASAPolynomial(coeffs=[0.508815,0.034457,-2.17108e-05,6.51778e-09,-7.48447e-13,3645.75,21.7356], Tmin=(604.13,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 499,
    label = "C=C=C[CH]C(=C)C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {5,D}
3  C u1 p0 c0 {2,S} {4,S} {11,S}
4  C u0 p0 c0 {3,S} {7,D} {12,S}
5  C u0 p0 c0 {2,D} {13,S} {14,S}
6  C u0 p0 c0 {7,D} {15,S} {16,S}
7  C u0 p0 c0 {4,D} {6,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8154,0.0162884,0.000286733,-9.49036e-07,1.00431e-09,35244.6,11.8337], Tmin=(10,'K'), Tmax=(294.4,'K')),
            NASAPolynomial(coeffs=[1.95792,0.060879,-3.90665e-05,1.20224e-08,-1.42003e-12,35270.1,17.0992], Tmin=(294.4,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 500,
    label = "O=CC=C(O)C=O",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {3,S} {5,S}
2  C u0 p0 c0 {1,D} {4,S} {6,S}
3  C u0 p0 c0 {1,S} {8,D} {9,S}
4  C u0 p0 c0 {2,S} {7,D} {10,S}
5  O u0 p2 c0 {1,S} {11,S}
6  H u0 p0 c0 {2,S}
7  O u0 p2 c0 {4,D}
8  O u0 p2 c0 {3,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79804,0.0193531,0.000106736,-3.47851e-07,3.54254e-10,-46508.9,11.0361], Tmin=(10,'K'), Tmax=(250.75,'K')),
            NASAPolynomial(coeffs=[2.39355,0.0417576,-2.7288e-05,8.47468e-09,-1.0039e-12,-46438.4,15.8691], Tmin=(250.75,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 501,
    label = "[O]OC(O)C(=O)COO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {4,S} {8,S}
2  O u0 p2 c0 {7,S} {13,S}
3  O u0 p2 c0 {6,S} {7,S}
4  O u0 p2 c0 {1,S} {14,S}
5  O u0 p2 c0 {9,D}
6  O u1 p2 c0 {3,S}
7  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
8  C u0 p0 c0 {1,S} {9,S} {11,S} {12,S}
9  C u0 p0 c0 {5,D} {7,S} {8,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {8,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.19096,0.0696963,1.03441e-05,-1.98323e-07,1.76953e-10,-51541.9,14.7139], Tmin=(10,'K'), Tmax=(506.04,'K')),
            NASAPolynomial(coeffs=[11.1121,0.0458493,-3.38763e-05,1.13147e-08,-1.40109e-12,-52840,-23.0098], Tmin=(506.04,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 502,
    label = "C=[C]C(=C)C([O])C=O",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {6,D}
3  C u0 p0 c0 {1,S} {9,D} {10,S}
4  C u1 p0 c0 {2,S} {11,S} {12,S}
5  C u0 p0 c0 {6,D} {13,S} {14,S}
6  C u0 p0 c0 {2,D} {5,D}
7  O u1 p2 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.52985,0.0416713,0.000179335,-7.69206e-07,8.44351e-10,27914,14.0691], Tmin=(10,'K'), Tmax=(337.07,'K')),
            NASAPolynomial(coeffs=[6.41823,0.0483488,-3.263e-05,1.04827e-08,-1.27999e-12,27486.6,-0.175706], Tmin=(337.07,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 503,
    label = "CCC([O])C=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,D} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  O u1 p2 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80277,0.0190958,0.000214582,-8.48752e-07,1.04073e-09,-19552.8,12.4955], Tmin=(10,'K'), Tmax=(264.28,'K')),
            NASAPolynomial(coeffs=[3.21708,0.0449742,-2.88663e-05,8.96003e-09,-1.06854e-12,-19581.3,13.4176], Tmin=(264.28,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 504,
    label = "OC1C=CO1",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {4,S} {8,S}
4 O u0 p2 c0 {1,S} {3,S}
5 O u0 p2 c0 {1,S} {9,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.12177,-0.0118503,0.000181608,-3.29117e-07,1.8841e-10,-18627.8,9.74855], Tmin=(10,'K'), Tmax=(576.21,'K')),
            NASAPolynomial(coeffs=[2.35532,0.0335603,-2.28987e-05,7.33378e-09,-8.8394e-13,-18974.5,12.5218], Tmin=(576.21,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 505,
    label = "C#CC(CC)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {6,T}
5  O u0 p2 c0 {2,S} {13,S}
6  C u0 p0 c0 {4,T} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u1 p2 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.35249,0.0546084,-4.7696e-05,2.57108e-08,-6.45778e-12,21832.1,13.5791], Tmin=(10,'K'), Tmax=(823.67,'K')),
            NASAPolynomial(coeffs=[5.97233,0.0418857,-2.45267e-05,6.95798e-09,-7.65978e-13,21400.5,1.44807], Tmin=(823.67,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 506,
    label = "C=C(C=CC)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,D} {10,S}
3  C u0 p0 c0 {4,S} {5,D} {6,S}
4  C u0 p0 c0 {2,D} {3,S} {11,S}
5  C u0 p0 c0 {3,D} {12,S} {13,S}
6  O u0 p2 c0 {3,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 O u1 p2 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74539,0.0176361,0.000216029,-5.81147e-07,4.53251e-10,13425.4,12.3984], Tmin=(10,'K'), Tmax=(449.18,'K')),
            NASAPolynomial(coeffs=[5.72327,0.0456044,-2.95867e-05,9.31575e-09,-1.12649e-12,12787.9,-0.679356], Tmin=(449.18,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 507,
    label = "C=C=CC(C)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,D} {11,S}
4  C u0 p0 c0 {5,D} {12,S} {13,S}
5  C u0 p0 c0 {3,D} {4,D}
6  O u0 p2 c0 {1,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 O u1 p2 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84926,0.0205144,0.000609644,-4.87492e-06,1.22163e-08,19332.7,11.2801], Tmin=(10,'K'), Tmax=(135.81,'K')),
            NASAPolynomial(coeffs=[4.0858,0.0458896,-2.78568e-05,8.16968e-09,-9.25869e-13,19296.5,9.51313], Tmin=(135.81,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 508,
    label = "[O]CC1OC1C[O]",
    molecule = 
"""
multiplicity 3
1  O u0 p2 c0 {4,S} {5,S}
2  O u1 p2 c0 {6,S}
3  O u1 p2 c0 {7,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {8,S}
5  C u0 p0 c0 {1,S} {4,S} {7,S} {9,S}
6  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
7  C u0 p0 c0 {3,S} {5,S} {12,S} {13,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.38387,0.0545695,-7.40169e-05,9.21195e-08,-5.36508e-11,-436.625,12.7227], Tmin=(10,'K'), Tmax=(510.07,'K')),
            NASAPolynomial(coeffs=[3.80335,0.0451078,-2.8042e-05,8.30764e-09,-9.45378e-13,-399.128,11.7684], Tmin=(510.07,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 509,
    label = "[O]CC1[CH]O1",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 C u1 p0 c0 {1,S} {4,S} {9,S}
4 O u0 p2 c0 {1,S} {3,S}
5 H u0 p0 c0 {1,S}
6 O u1 p2 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91927,0.0143823,2.98997e-05,-4.96779e-08,2.07561e-11,22665.4,11.341], Tmin=(10,'K'), Tmax=(855.29,'K')),
            NASAPolynomial(coeffs=[4.23112,0.0265579,-1.53651e-05,4.24202e-09,-4.52394e-13,22113.4,6.96996], Tmin=(855.29,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 510,
    label = "CCC([O])=CO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,S} {11,D}
4  C u1 p0 c0 {3,S} {5,S} {12,S}
5  O u0 p2 c0 {4,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {3,D}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9352,0.00690697,0.000339665,-1.72223e-06,3.11334e-09,-35676.6,13.1755], Tmin=(10,'K'), Tmax=(138.61,'K')),
            NASAPolynomial(coeffs=[2.78591,0.0400736,-1.92586e-05,4.08752e-09,-3.08712e-13,-35644.8,16.4491], Tmin=(138.61,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 511,
    label = "C=C[CH]C=CC=C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,D} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {10,S}
3  C u0 p0 c0 {2,D} {5,S} {12,S}
4  C u0 p0 c0 {1,D} {6,S} {11,S}
5  C u0 p0 c0 {3,S} {7,D} {8,S}
6  C u1 p0 c0 {4,S} {13,S} {14,S}
7  C u0 p0 c0 {5,D} {15,S} {16,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82104,0.0117437,0.000229608,-5.1706e-07,3.55726e-10,26627.7,11.147], Tmin=(10,'K'), Tmax=(475.51,'K')),
            NASAPolynomial(coeffs=[1.6318,0.0639669,-4.17761e-05,1.29383e-08,-1.53032e-12,26453.7,16.0625], Tmin=(475.51,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 512,
    label = "[CH2]C1CC1C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3  C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
4  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
5  C u1 p0 c0 {2,S} {13,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92246,0.00555032,0.000181125,-4.22164e-07,3.19653e-10,20264.2,11.5299], Tmin=(10,'K'), Tmax=(393.75,'K')),
            NASAPolynomial(coeffs=[0.743587,0.0493443,-2.95214e-05,8.66895e-09,-9.92355e-13,20425.3,22.7712], Tmin=(393.75,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 513,
    label = "C[CH]C1CC1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
4  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
5  C u1 p0 c0 {1,S} {4,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86317,0.017581,5.28138e-05,-7.64072e-08,3.01864e-11,20441.8,12.5328], Tmin=(10,'K'), Tmax=(850.89,'K')),
            NASAPolynomial(coeffs=[1.21797,0.0459362,-2.52374e-05,6.73396e-09,-7.01784e-13,20315.6,21.4807], Tmin=(850.89,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 514,
    label = "[CH2]C=CC1C=CC1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,D} {11,S}
4  C u0 p0 c0 {1,S} {6,D} {12,S}
5  C u0 p0 c0 {2,S} {3,D} {13,S}
6  C u0 p0 c0 {4,D} {7,S} {14,S}
7  C u1 p0 c0 {6,S} {15,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76119,0.0208641,0.000142692,-3.46865e-07,2.6511e-10,39478.4,13.0387], Tmin=(10,'K'), Tmax=(336.07,'K')),
            NASAPolynomial(coeffs=[0.363035,0.0613102,-3.78338e-05,1.1249e-08,-1.28983e-12,39706.8,25.7273], Tmin=(336.07,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 515,
    label = "[CH2]C1C=CC=CC1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {6,D} {12,S}
4  C u0 p0 c0 {2,S} {5,D} {11,S}
5  C u0 p0 c0 {4,D} {6,S} {13,S}
6  C u0 p0 c0 {3,D} {5,S} {14,S}
7  C u1 p0 c0 {1,S} {15,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92012,0.00513864,0.000193368,-3.84055e-07,2.44727e-10,32791.4,12.6158], Tmin=(10,'K'), Tmax=(463.88,'K')),
            NASAPolynomial(coeffs=[-1.43341,0.0643297,-4.01601e-05,1.2105e-08,-1.40702e-12,33148,32.8204], Tmin=(463.88,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 516,
    label = "C=CC=CC(C=C)O[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,D} {10,S}
3  C u0 p0 c0 {1,S} {6,D} {11,S}
4  C u0 p0 c0 {2,D} {5,S} {13,S}
5  C u0 p0 c0 {4,S} {7,D} {12,S}
6  C u0 p0 c0 {3,D} {14,S} {15,S}
7  C u0 p0 c0 {5,D} {16,S} {17,S}
8  O u0 p2 c0 {1,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 O u1 p2 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.11795,0.0913272,-0.000227257,4.92982e-07,-4.21939e-10,23304.8,16.4814], Tmin=(10,'K'), Tmax=(377.31,'K')),
            NASAPolynomial(coeffs=[3.3223,0.0671217,-4.34126e-05,1.33419e-08,-1.56541e-12,23446.3,17.7735], Tmin=(377.31,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 517,
    label = "C=CC1C=C[CH]COO1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {8,S} {10,S}
2  C u0 p0 c0 {4,S} {9,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {6,D} {15,S}
4  C u1 p0 c0 {2,S} {6,S} {14,S}
5  C u0 p0 c0 {1,S} {7,D} {13,S}
6  C u0 p0 c0 {3,D} {4,S} {16,S}
7  C u0 p0 c0 {5,D} {17,S} {18,S}
8  O u0 p2 c0 {1,S} {9,S}
9  O u0 p2 c0 {2,S} {8,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.57752,0.0416343,4.56632e-05,-9.61847e-08,4.46863e-11,17930.3,13.6264], Tmin=(10,'K'), Tmax=(776.53,'K')),
            NASAPolynomial(coeffs=[3.67579,0.0627041,-3.67145e-05,1.03196e-08,-1.12192e-12,17264.6,8.98856], Tmin=(776.53,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 518,
    label = "C#CC#CC",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {4,S}
4 C u0 p0 c0 {3,S} {5,T}
5 C u0 p0 c0 {4,T} {9,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87853,0.00928037,0.000131962,-3.95662e-07,3.56619e-10,47783.1,7.37626], Tmin=(10,'K'), Tmax=(378.15,'K')),
            NASAPolynomial(coeffs=[4.144,0.0264876,-1.56867e-05,4.60038e-09,-5.29593e-13,47619.9,4.46146], Tmin=(378.15,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 519,
    label = "[CH]1CC2C=CC1OOC2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
3  C u0 p0 c0 {5,S} {7,S} {8,S} {11,S}
4  C u0 p0 c0 {1,S} {9,S} {14,S} {15,S}
5  C u1 p0 c0 {2,S} {3,S} {16,S}
6  C u0 p0 c0 {1,S} {7,D} {18,S}
7  C u0 p0 c0 {3,S} {6,D} {17,S}
8  O u0 p2 c0 {3,S} {9,S}
9  O u0 p2 c0 {4,S} {8,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89874,0.00590599,0.000211261,-3.73205e-07,2.06184e-10,17767.7,12.1314], Tmin=(10,'K'), Tmax=(547.83,'K')),
            NASAPolynomial(coeffs=[-4.11254,0.084033,-5.64117e-05,1.79468e-08,-2.16934e-12,18350.8,43.2713], Tmin=(547.83,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 520,
    label = "[CH]1C2C=CCC1C2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {3,S} {5,S} {6,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
5  C u1 p0 c0 {1,S} {2,S} {14,S}
6  C u0 p0 c0 {2,S} {7,D} {15,S}
7  C u0 p0 c0 {4,S} {6,D} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.22359,-0.0192241,0.00027084,-4.39404e-07,2.29737e-10,38838.7,11.6717], Tmin=(10,'K'), Tmax=(602.36,'K')),
            NASAPolynomial(coeffs=[-3.32071,0.0688852,-4.32257e-05,1.29521e-08,-1.4862e-12,39058,38.5203], Tmin=(602.36,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 521,
    label = "[CH]1C=CCC2CC12",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
5  C u1 p0 c0 {2,S} {7,S} {15,S}
6  C u0 p0 c0 {4,S} {7,D} {14,S}
7  C u0 p0 c0 {5,S} {6,D} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.12669,-0.0114918,0.000239037,-3.93407e-07,2.07006e-10,26915.1,11.98], Tmin=(10,'K'), Tmax=(597.42,'K')),
            NASAPolynomial(coeffs=[-2.79476,0.0677133,-4.2343e-05,1.26638e-08,-1.45147e-12,27155.6,36.8983], Tmin=(597.42,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 522,
    label = "[CH2]C1=CC=CCC1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {7,D}
4  C u0 p0 c0 {2,S} {6,D} {12,S}
5  C u1 p0 c0 {3,S} {6,S} {13,S}
6  C u0 p0 c0 {4,D} {5,S} {14,S}
7  C u0 p0 c0 {3,D} {15,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94068,0.00357812,0.00017527,-3.07864e-07,1.74048e-10,20162.9,10.9177], Tmin=(10,'K'), Tmax=(457.82,'K')),
            NASAPolynomial(coeffs=[-3.82182,0.071311,-4.63591e-05,1.4445e-08,-1.72294e-12,20874.6,42.3127], Tmin=(457.82,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 523,
    label = "CC1=C[CH]C=CC1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {2,S} {5,D}
4  C u0 p0 c0 {1,S} {6,D} {13,S}
5  C u0 p0 c0 {3,D} {7,S} {14,S}
6  C u0 p0 c0 {4,D} {7,S} {15,S}
7  C u1 p0 c0 {5,S} {6,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94286,0.00375192,0.000191719,-3.75615e-07,2.40956e-10,17339,11.6154], Tmin=(10,'K'), Tmax=(400.07,'K')),
            NASAPolynomial(coeffs=[-2.27625,0.065909,-4.12431e-05,1.24424e-08,-1.44713e-12,17836.8,35.9239], Tmin=(400.07,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 524,
    label = "[CH]1CC=CC2CC12",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {8,S}
3  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
4  C u0 p0 c0 {5,S} {7,S} {12,S} {13,S}
5  C u1 p0 c0 {1,S} {4,S} {14,S}
6  C u0 p0 c0 {2,S} {7,D} {15,S}
7  C u0 p0 c0 {4,S} {6,D} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05107,-0.00567579,0.000220242,-3.74233e-07,2.022e-10,33660.5,12.1386], Tmin=(10,'K'), Tmax=(579.34,'K')),
            NASAPolynomial(coeffs=[-2.33303,0.0669799,-4.18644e-05,1.25242e-08,-1.43657e-12,33920.6,35.3143], Tmin=(579.34,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 525,
    label = "[CH2]C1C=CCC=C1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {5,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,D} {12,S}
4  C u0 p0 c0 {1,S} {6,D} {13,S}
5  C u0 p0 c0 {2,S} {3,D} {11,S}
6  C u0 p0 c0 {2,S} {4,D} {14,S}
7  C u1 p0 c0 {1,S} {15,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92909,0.00471145,0.000199459,-4.07448e-07,2.70005e-10,32850.6,12.3199], Tmin=(10,'K'), Tmax=(433.73,'K')),
            NASAPolynomial(coeffs=[-1.48332,0.0642921,-4.00209e-05,1.20275e-08,-1.39444e-12,33229.1,32.8624], Tmin=(433.73,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 526,
    label = "CC1=CC=CC[CH]1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {4,D} {6,S}
4  C u0 p0 c0 {1,S} {3,D} {14,S}
5  C u0 p0 c0 {1,S} {7,D} {13,S}
6  C u1 p0 c0 {3,S} {7,S} {15,S}
7  C u0 p0 c0 {5,D} {6,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94238,0.00373416,0.000189866,-3.65712e-07,2.29978e-10,16986.8,11.9908], Tmin=(10,'K'), Tmax=(408.68,'K')),
            NASAPolynomial(coeffs=[-2.52355,0.0669984,-4.2256e-05,1.28111e-08,-1.49441e-12,17515.5,37.4016], Tmin=(408.68,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 527,
    label = "[O]OCC1=CC=CCC1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {8,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {3,S} {6,D}
5  C u0 p0 c0 {2,S} {7,D} {15,S}
6  C u0 p0 c0 {4,D} {7,S} {16,S}
7  C u0 p0 c0 {5,D} {6,S} {17,S}
8  O u0 p2 c0 {3,S} {18,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 O u1 p2 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75292,0.041309,2.80358e-05,-5.68257e-08,2.20809e-11,13225.1,14.2909], Tmin=(10,'K'), Tmax=(988.07,'K')),
            NASAPolynomial(coeffs=[7.03711,0.0533638,-2.8749e-05,7.45379e-09,-7.52845e-13,11338.7,-7.77596], Tmin=(988.07,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 528,
    label = "C=C1C=CC(O[O])CC1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {11,S}
3  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {6,S} {7,D}
5  C u0 p0 c0 {2,S} {6,D} {14,S}
6  C u0 p0 c0 {4,S} {5,D} {15,S}
7  C u0 p0 c0 {4,D} {16,S} {17,S}
8  O u0 p2 c0 {2,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 O u1 p2 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72004,0.0305639,8.49166e-05,-1.47499e-07,6.80775e-11,11302,14.2678], Tmin=(10,'K'), Tmax=(743.1,'K')),
            NASAPolynomial(coeffs=[2.0304,0.0658199,-3.90572e-05,1.10987e-08,-1.21731e-12,10830.8,17.0575], Tmin=(743.1,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 529,
    label = "CC1(O[O])C=CC=CC1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {7,D} {15,S}
5  C u0 p0 c0 {2,S} {6,D} {14,S}
6  C u0 p0 c0 {5,D} {7,S} {16,S}
7  C u0 p0 c0 {4,D} {6,S} {17,S}
8  O u0 p2 c0 {1,S} {18,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 O u1 p2 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.55071,0.0402529,6.12032e-05,-1.33577e-07,6.96446e-11,10382.4,13.5551], Tmin=(10,'K'), Tmax=(669,'K')),
            NASAPolynomial(coeffs=[2.76097,0.0650284,-3.93101e-05,1.13917e-08,-1.27247e-12,10039.3,13.6938], Tmin=(669,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 530,
    label = "CC1=CC=CC(O[O])C1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {3,S} {6,D}
5  C u0 p0 c0 {1,S} {7,D} {15,S}
6  C u0 p0 c0 {4,D} {7,S} {16,S}
7  C u0 p0 c0 {5,D} {6,S} {17,S}
8  O u0 p2 c0 {1,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 O u1 p2 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49394,0.0456596,2.81739e-05,-7.43225e-08,3.57935e-11,10361.6,13.694], Tmin=(10,'K'), Tmax=(766.55,'K')),
            NASAPolynomial(coeffs=[3.70466,0.0614474,-3.57662e-05,1.00264e-08,-1.08914e-12,9833.15,9.49711], Tmin=(766.55,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 531,
    label = "C1=CC2CC[C]1COO2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {5,S} {13,S} {14,S}
4  C u0 p0 c0 {5,S} {9,S} {15,S} {16,S}
5  C u1 p0 c0 {3,S} {4,S} {7,S}
6  C u0 p0 c0 {1,S} {7,D} {17,S}
7  C u0 p0 c0 {5,S} {6,D} {18,S}
8  O u0 p2 c0 {1,S} {9,S}
9  O u0 p2 c0 {4,S} {8,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93415,0.00406793,0.000217806,-3.92577e-07,2.27272e-10,19343.2,12.0414], Tmin=(10,'K'), Tmax=(447.03,'K')),
            NASAPolynomial(coeffs=[-5.30914,0.0866051,-5.85709e-05,1.87334e-08,-2.27277e-12,20171.3,49.212], Tmin=(447.03,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 532,
    label = "C=CC=CC(=C)CO[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {6,D}
3  C u0 p0 c0 {2,S} {4,D} {13,S}
4  C u0 p0 c0 {3,D} {5,S} {12,S}
5  C u0 p0 c0 {4,S} {7,D} {11,S}
6  C u0 p0 c0 {2,D} {16,S} {17,S}
7  C u0 p0 c0 {5,D} {14,S} {15,S}
8  O u0 p2 c0 {1,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 O u1 p2 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.57601,0.0627039,-2.5233e-05,-6.9753e-09,5.40272e-12,21290.1,15.0324], Tmin=(10,'K'), Tmax=(1136.79,'K')),
            NASAPolynomial(coeffs=[15.2621,0.0405409,-2.10023e-05,5.21272e-09,-5.03616e-13,17408.3,-48.2322], Tmin=(1136.79,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 533,
    label = "C1=COCOC1",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {5,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {3,D} {6,S} {12,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {2,S} {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.07259,-0.00627049,0.000149851,-2.34388e-07,1.17133e-10,-29677.1,9.9113], Tmin=(10,'K'), Tmax=(619.08,'K')),
            NASAPolynomial(coeffs=[-1.60593,0.0492794,-3.04406e-05,8.97205e-09,-1.01463e-12,-29335.4,31.665], Tmin=(619.08,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 534,
    label = "CC=C[CH]OC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
3  C u1 p0 c0 {1,S} {4,S} {13,S}
4  C u0 p0 c0 {3,S} {5,D} {14,S}
5  C u0 p0 c0 {4,D} {6,S} {15,S}
6  O u0 p2 c0 {2,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.46409,0.0533064,-0.000102149,2.20177e-07,-1.79988e-10,-5398.25,11.2568], Tmin=(10,'K'), Tmax=(439.76,'K')),
            NASAPolynomial(coeffs=[1.34689,0.0525266,-3.11434e-05,8.92419e-09,-9.91708e-13,-5018.29,21.9347], Tmin=(439.76,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 535,
    label = "C=C[C]=C=O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {5,S}
2 C u0 p0 c0 {1,D} {6,S} {7,S}
3 C u1 p0 c0 {1,S} {4,D}
4 C u0 p0 c0 {3,D} {8,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81732,0.0158531,2.31559e-05,-5.39906e-08,2.99489e-11,23831,9.83246], Tmin=(10,'K'), Tmax=(620.77,'K')),
            NASAPolynomial(coeffs=[3.39871,0.0251609,-1.53081e-05,4.4711e-09,-5.0334e-13,23755.6,10.6265], Tmin=(620.77,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 536,
    label = "[CH2]C=CC(=C)O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,D} {6,S}
2  C u1 p0 c0 {1,S} {3,S} {7,S}
3  C u0 p0 c0 {2,S} {5,D} {8,S}
4  C u0 p0 c0 {1,D} {11,S} {12,S}
5  C u0 p0 c0 {3,D} {9,S} {10,S}
6  O u0 p2 c0 {1,S} {13,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82318,0.0107012,0.00017502,-3.73444e-07,2.34593e-10,296.538,10.7355], Tmin=(10,'K'), Tmax=(546.2,'K')),
            NASAPolynomial(coeffs=[4.29723,0.0465274,-3.12885e-05,1.00903e-08,-1.24358e-12,-341.446,3.36901], Tmin=(546.2,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 537,
    label = "[CH2]C=CC(=O)O[O]",
    molecule = 
"""
multiplicity 3
1  C u1 p0 c0 {2,S} {3,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {6,S}
3  C u0 p0 c0 {1,S} {5,S} {8,D}
4  C u0 p0 c0 {2,D} {9,S} {10,S}
5  O u0 p2 c0 {3,S} {11,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {3,D}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.62898,0.0342644,2.63242e-05,-8.86813e-08,5.23658e-11,3346.2,12.5035], Tmin=(10,'K'), Tmax=(663.97,'K')),
            NASAPolynomial(coeffs=[6.51004,0.036831,-2.44832e-05,7.52449e-09,-8.7376e-13,2524.46,-3.52316], Tmin=(663.97,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 538,
    label = "CC=CC(=O)CO[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {5,S} {12,D}
4  C u0 p0 c0 {2,S} {5,D} {13,S}
5  C u0 p0 c0 {3,S} {4,D} {14,S}
6  O u0 p2 c0 {1,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 O u0 p2 c0 {3,D}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 O u1 p2 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.22797,0.0787528,-0.000197817,4.00404e-07,-3.21344e-10,-11467.3,14.3358], Tmin=(10,'K'), Tmax=(391.01,'K')),
            NASAPolynomial(coeffs=[4.09587,0.052956,-3.39522e-05,1.03584e-08,-1.20865e-12,-11405.8,12.6174], Tmin=(391.01,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 539,
    label = "[CH2]C(=O)C(C=C)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {5,D} {10,S}
3  C u0 p0 c0 {1,S} {4,S} {9,D}
4  C u1 p0 c0 {3,S} {11,S} {12,S}
5  C u0 p0 c0 {2,D} {13,S} {14,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {6,S} {15,S}
8  H u0 p0 c0 {1,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49328,0.0418637,0.00029057,-1.19759e-06,1.29492e-09,-7056.69,12.8502], Tmin=(10,'K'), Tmax=(347.27,'K')),
            NASAPolynomial(coeffs=[9.50681,0.0441919,-2.87276e-05,9.02579e-09,-1.09081e-12,-7906.06,-16.0171], Tmin=(347.27,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 540,
    label = "C=CC(O[O])C(=C)O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {4,D} {7,S}
3  C u0 p0 c0 {1,S} {5,D} {9,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  C u0 p0 c0 {3,D} {12,S} {13,S}
6  O u0 p2 c0 {1,S} {14,S}
7  O u0 p2 c0 {2,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 O u1 p2 c0 {6,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.66577,0.0224319,0.000245976,-6.39874e-07,4.72505e-10,-5576.5,14.4976], Tmin=(10,'K'), Tmax=(479.3,'K')),
            NASAPolynomial(coeffs=[6.82256,0.0548822,-3.95818e-05,1.32464e-08,-1.65182e-12,-6554.46,-5.45559], Tmin=(479.3,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 541,
    label = "C=C(O)C=CCO[O]",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,D} {10,S}
3  C u0 p0 c0 {4,S} {5,D} {7,S}
4  C u0 p0 c0 {2,D} {3,S} {11,S}
5  C u0 p0 c0 {3,D} {12,S} {13,S}
6  O u0 p2 c0 {1,S} {14,S}
7  O u0 p2 c0 {3,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 O u1 p2 c0 {6,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.26675,0.0786416,-0.000239209,5.99906e-07,-5.66292e-10,-7208.01,14.3603], Tmin=(10,'K'), Tmax=(351.78,'K')),
            NASAPolynomial(coeffs=[2.90953,0.0570987,-3.8168e-05,1.19939e-08,-1.42884e-12,-7024.45,17.9623], Tmin=(351.78,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 542,
    label = "C=C(C[O])C[O]",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u1 p2 c0 {1,S}
6  O u1 p2 c0 {2,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7013,0.0270002,4.3949e-05,-1.03746e-07,5.78213e-11,13798.8,11.7681], Tmin=(10,'K'), Tmax=(641.23,'K')),
            NASAPolynomial(coeffs=[4.11686,0.0405282,-2.54062e-05,7.56656e-09,-8.6259e-13,13414.1,7.36372], Tmin=(641.23,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 543,
    label = "O=CC(O)=C[CH]O",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {3,D} {7,S}
3  C u0 p0 c0 {2,D} {6,S} {8,S}
4  C u0 p0 c0 {1,S} {9,D} {10,S}
5  O u0 p2 c0 {1,S} {12,S}
6  O u0 p2 c0 {3,S} {11,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  O u0 p2 c0 {4,D}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89469,0.00821253,0.000185109,-5.12086e-07,4.79456e-10,-47389.6,11.6997], Tmin=(10,'K'), Tmax=(269.74,'K')),
            NASAPolynomial(coeffs=[1.35321,0.0458988,-2.44512e-05,5.82178e-09,-5.27972e-13,-47252.5,20.6309], Tmin=(269.74,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 544,
    label = "[O]OC(O)(C=O)C=O",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {6,S} {11,S}
2  O u0 p2 c0 {5,S} {6,S}
3  O u0 p2 c0 {8,D}
4  O u0 p2 c0 {7,D}
5  O u1 p2 c0 {2,S}
6  C u0 p0 c0 {1,S} {2,S} {7,S} {8,S}
7  C u0 p0 c0 {4,D} {6,S} {10,S}
8  C u0 p0 c0 {3,D} {6,S} {9,S}
9  H u0 p0 c0 {8,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.95818,0.0749712,-0.000122941,1.05662e-07,-3.55667e-11,-47507.7,12.2418], Tmin=(10,'K'), Tmax=(832.08,'K')),
            NASAPolynomial(coeffs=[10.5941,0.0272748,-1.71486e-05,5.02905e-09,-5.62665e-13,-48398,-20.9077], Tmin=(832.08,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 545,
    label = "O=C=C1[CH]C1",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {4,D}
3 C u1 p0 c0 {1,S} {2,S} {7,S}
4 C u0 p0 c0 {2,D} {8,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
8 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92967,0.00448368,9.39743e-05,-2.02087e-07,1.33095e-10,35044.7,10.5877], Tmin=(10,'K'), Tmax=(495.11,'K')),
            NASAPolynomial(coeffs=[2.85455,0.0272289,-1.75306e-05,5.41087e-09,-6.40265e-13,34978.8,13.2785], Tmin=(495.11,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 546,
    label = "CC1CC1=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {2,S} {11,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91269,0.0070805,0.000107185,-2.3082e-07,1.61268e-10,-3467.05,10.0461], Tmin=(10,'K'), Tmax=(366.76,'K')),
            NASAPolynomial(coeffs=[0.980314,0.0390613,-2.361e-05,6.92347e-09,-7.86131e-13,-3251.95,21.2519], Tmin=(366.76,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 547,
    label = "C#CC(=O)CC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,S} {11,D}
4  C u0 p0 c0 {3,S} {5,T}
5  C u0 p0 c0 {4,T} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {3,D}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.35173,0.0461791,-4.99233e-05,3.72923e-08,-1.22702e-11,3880.61,11.0423], Tmin=(10,'K'), Tmax=(861.04,'K')),
            NASAPolynomial(coeffs=[4.59486,0.0343485,-1.87644e-05,4.99951e-09,-5.22538e-13,3891.01,6.53439], Tmin=(861.04,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 548,
    label = "O=CC(O)=C=CO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,D} {5,S}
2  C u0 p0 c0 {1,S} {7,D} {8,S}
3  C u0 p0 c0 {4,D} {6,S} {9,S}
4  C u0 p0 c0 {1,D} {3,D}
5  O u0 p2 c0 {1,S} {10,S}
6  O u0 p2 c0 {3,S} {11,S}
7  O u0 p2 c0 {2,D}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82705,0.012565,0.000173708,-4.49745e-07,3.50739e-10,-34298.5,11.3443], Tmin=(10,'K'), Tmax=(422.35,'K')),
            NASAPolynomial(coeffs=[2.76194,0.046648,-3.25624e-05,1.03685e-08,-1.2413e-12,-34422.5,13.0312], Tmin=(422.35,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 549,
    label = "O=CC(=O)C=CO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {6,D}
3  C u0 p0 c0 {1,D} {5,S} {8,S}
4  C u0 p0 c0 {2,S} {9,D} {10,S}
5  O u0 p2 c0 {3,S} {11,S}
6  O u0 p2 c0 {2,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  O u0 p2 c0 {4,D}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81799,0.0234037,3.43127e-05,-6.5814e-08,2.90799e-11,-48450.6,10.7822], Tmin=(10,'K'), Tmax=(834.91,'K')),
            NASAPolynomial(coeffs=[5.32144,0.0353143,-2.14254e-05,6.11192e-09,-6.67451e-13,-49367.9,-0.189382], Tmin=(834.91,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 550,
    label = "[O]OC(O)(C=O)C=CO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {6,S} {13,S}
2  O u0 p2 c0 {5,S} {6,S}
3  O u0 p2 c0 {9,S} {14,S}
4  O u0 p2 c0 {8,D}
5  O u1 p2 c0 {2,S}
6  C u0 p0 c0 {1,S} {2,S} {7,S} {8,S}
7  C u0 p0 c0 {6,S} {9,D} {10,S}
8  C u0 p0 c0 {4,D} {6,S} {12,S}
9  C u0 p0 c0 {3,S} {7,D} {11,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {9,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.45494,0.0444037,8.88046e-05,-2.74682e-07,1.9395e-10,-51278,15.4215], Tmin=(10,'K'), Tmax=(529.49,'K')),
            NASAPolynomial(coeffs=[6.90049,0.0538997,-3.87388e-05,1.26224e-08,-1.53276e-12,-52140.9,-3.71303], Tmin=(529.49,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 551,
    label = "O=[C]C[C](O)C=O",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u1 p0 c0 {1,S} {3,S} {5,S}
3  C u0 p0 c0 {2,S} {8,D} {9,S}
4  C u1 p0 c0 {1,S} {10,D}
5  O u0 p2 c0 {2,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {3,D}
9  H u0 p0 c0 {3,S}
10 O u0 p2 c0 {4,D}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.45463,0.0486014,-8.61357e-05,1.35083e-07,-8.70478e-11,-24699.2,13.267], Tmin=(10,'K'), Tmax=(509.18,'K')),
            NASAPolynomial(coeffs=[2.92654,0.0403311,-2.51872e-05,7.38229e-09,-8.29387e-13,-24484.5,17.0392], Tmin=(509.18,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 552,
    label = "[O]OC(=CO)[C](O)C=O",
    molecule = 
"""
multiplicity 3
1  O u0 p2 c0 {5,S} {6,S}
2  O u0 p2 c0 {7,S} {13,S}
3  O u0 p2 c0 {8,S} {12,S}
4  O u0 p2 c0 {9,D}
5  O u1 p2 c0 {1,S}
6  C u0 p0 c0 {1,S} {7,S} {8,D}
7  C u1 p0 c0 {2,S} {6,S} {9,S}
8  C u0 p0 c0 {3,S} {6,D} {10,S}
9  C u0 p0 c0 {4,D} {7,S} {11,S}
10 H u0 p0 c0 {8,S}
11 H u0 p0 c0 {9,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8405,0.0138524,0.00030989,-1.05363e-06,1.14135e-09,-38643.7,13.373], Tmin=(10,'K'), Tmax=(291.53,'K')),
            NASAPolynomial(coeffs=[2.20197,0.0590267,-3.93046e-05,1.19103e-08,-1.373e-12,-38644.6,17.6044], Tmin=(291.53,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 553,
    label = "CC(=O)CCOO",
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
            NASAPolynomial(coeffs=[3.56264,0.0402565,0.000203905,-9.22491e-07,1.09904e-09,-41698.4,12.0092], Tmin=(10,'K'), Tmax=(307.78,'K')),
            NASAPolynomial(coeffs=[5.99381,0.0486377,-3.17761e-05,1.0028e-08,-1.21217e-12,-42037.4,0.0689843], Tmin=(307.78,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 554,
    label = "C=CC1OOC1=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {1,S} {6,S} {9,D}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {3,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7183,0.0245073,4.71196e-05,-1.15374e-07,6.92059e-11,-16261.5,11.8146], Tmin=(10,'K'), Tmax=(586.1,'K')),
            NASAPolynomial(coeffs=[3.81689,0.0381051,-2.42046e-05,7.29897e-09,-8.41417e-13,-16518.2,9.3006], Tmin=(586.1,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 555,
    label = "[O]CC1OOCC1=O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {4,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {2,S} {13,D}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {2,S} {5,S}
7  H u0 p0 c0 {1,S}
8  O u1 p2 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.69206,0.0330744,3.08876e-05,-7.39144e-08,3.58111e-11,-21910.4,13.6757], Tmin=(10,'K'), Tmax=(778.04,'K')),
            NASAPolynomial(coeffs=[5.6187,0.0429035,-2.61081e-05,7.52269e-09,-8.31433e-13,-22807.5,1.0258], Tmin=(778.04,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

