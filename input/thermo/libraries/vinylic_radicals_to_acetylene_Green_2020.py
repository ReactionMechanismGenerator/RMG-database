#!/usr/bin/env python
# encoding: utf-8

name = "vinylic_radicals_to_acetylene_Green_2020"
shortDesc = "model 1"
longDesc = """
Direct Measurement of Radical-Catalyzed C6H6 Formation from Acetylene and Validation of Theoretical Rate Coefficients for C2H3 + C2H2 and C4H5 + C2H2 Reactions
Mica C. Smith, Guozhu Liu, Zachary J. Buras, Te-Chun Chu, Jeehyun Yang, and William H. Green, The Journal of Physical Chemistry A 2020 124 (14), 2871-2884, DOI: 10.1021/acs.jpca.0c00558
"""
entry(
    index = 0,
    label = "helium",
    molecule = 
"""
1 He u0 p1 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,-2.38914e-13,3.12709e-16,-1.33367e-19,1.7499e-23,-745.375,0.928724], Tmin=(100,'K'), Tmax=(4383.16,'K')),
            NASAPolynomial(coeffs=[2.50003,-3.04997e-08,1.01101e-11,-1.48797e-15,8.20356e-20,-745.406,0.928506], Tmin=(4383.16,'K'), Tmax=(5000,'K')),
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
    index = 1,
    label = "vinyl",
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
            NASAPolynomial(coeffs=[3.83068,-0.00147601,3.08992e-05,-3.80462e-08,1.43164e-11,34524.2,5.61956], Tmin=(100,'K'), Tmax=(933.67,'K')),
            NASAPolynomial(coeffs=[5.36093,0.00527333,-1.31953e-06,2.21547e-10,-1.68754e-14,33658.6,-4.76364], Tmin=(933.67,'K'), Tmax=(5000,'K')),
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
    index = 2,
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
            NASAPolynomial(coeffs=[3.08745,0.00578563,8.56365e-06,-1.72829e-08,7.83616e-12,26273.8,4.46077], Tmin=(100,'K'), Tmax=(897.94,'K')),
            NASAPolynomial(coeffs=[5.89067,0.00209058,4.88273e-08,-5.66858e-11,4.15047e-15,25415.9,-10.7351], Tmin=(897.94,'K'), Tmax=(5000,'K')),
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
    index = 3,
    label = "n-C4H5",
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
            NASAPolynomial(coeffs=[2.64258,0.0163334,3.86236e-05,-6.71392e-08,2.8361e-11,41729.6,13.2819], Tmin=(100,'K'), Tmax=(937.72,'K')),
            NASAPolynomial(coeffs=[12.9704,0.0066914,-1.00078e-06,1.6762e-10,-1.71452e-14,38279.7,-43.9471], Tmin=(937.72,'K'), Tmax=(5000,'K')),
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
    index = 4,
    label = "C4H4",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {5,S}
2 C u0 p0 c0 {1,D} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {4,T}
4 C u0 p0 c0 {3,T} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.87088,0.0182037,1.06732e-05,-2.7252e-08,1.1949e-11,33023.8,11.2933], Tmin=(100,'K'), Tmax=(955.23,'K')),
            NASAPolynomial(coeffs=[8.52637,0.0108964,-3.56581e-06,6.31282e-10,-4.51923e-14,31196.3,-19.6426], Tmin=(955.23,'K'), Tmax=(5000,'K')),
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
    label = "c-C4H5",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C u1 p0 c0 {1,S} {4,S} {8,S}
3 C u0 p0 c0 {1,S} {4,D} {7,S}
4 C u0 p0 c0 {2,S} {3,D} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.15966,-0.0134492,0.000149672,-2.40569e-07,1.25577e-10,37635.4,7.76104], Tmin=(10,'K'), Tmax=(603.98,'K')),
            NASAPolynomial(coeffs=[0.17209,0.0341869,-2.1353e-05,6.39771e-09,-7.35001e-13,37729.9,21.783], Tmin=(603.98,'K'), Tmax=(3000,'K')),
        ],
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
            NASAPolynomial(coeffs=[-0.383584,0.0239231,6.53972e-05,-1.13628e-07,5.02756e-11,8635.02,25.5128], Tmin=(100,'K'), Tmax=(846.39,'K')),
            NASAPolynomial(coeffs=[6.88982,0.0287389,-1.25906e-05,2.50538e-09,-1.8535e-13,6000.07,-16.6566], Tmin=(846.39,'K'), Tmax=(5000,'K')),
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
    index = 7,
    label = "fulvene",
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
            NASAPolynomial(coeffs=[2.27454,0.0275138,2.27962e-05,-4.29095e-08,1.61507e-11,24947.1,13.5841], Tmin=(100,'K'), Tmax=(1068.19,'K')),
            NASAPolynomial(coeffs=[11.6811,0.0209069,-8.11237e-06,1.46164e-09,-1.03914e-13,21304.8,-40.0601], Tmin=(1068.19,'K'), Tmax=(5000,'K')),
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
    index = 8,
    label = "H",
    molecule = 
"""
multiplicity 2
1 H u1 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,-2.38914e-13,3.12709e-16,-1.33367e-19,1.7499e-23,25474.2,-0.444973], Tmin=(100,'K'), Tmax=(4383.16,'K')),
            NASAPolynomial(coeffs=[2.50003,-3.04997e-08,1.01101e-11,-1.48797e-15,8.20356e-20,25474.2,-0.445191], Tmin=(4383.16,'K'), Tmax=(5000,'K')),
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
    index = 9,
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
            NASAPolynomial(coeffs=[2.80594,0.0102591,6.17238e-05,-9.01612e-08,3.59103e-11,11658.5,12.0623], Tmin=(100,'K'), Tmax=(946.05,'K')),
            NASAPolynomial(coeffs=[12.4695,0.0100551,-2.4119e-06,4.57038e-10,-3.93128e-14,8010.71,-43.6384], Tmin=(946.05,'K'), Tmax=(5000,'K')),
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
    index = 10,
    label = "C6H8",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {3,S} {8,S}
2  C u0 p0 c0 {1,D} {4,S} {9,S}
3  C u0 p0 c0 {1,S} {5,D} {7,S}
4  C u0 p0 c0 {2,S} {6,D} {10,S}
5  C u0 p0 c0 {3,D} {11,S} {12,S}
6  C u0 p0 c0 {4,D} {13,S} {14,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.38428,0.0414412,1.94287e-05,-6.16688e-08,2.86503e-11,17631.7,19.3258], Tmin=(100,'K'), Tmax=(941.22,'K')),
            NASAPolynomial(coeffs=[16.962,0.0157222,-4.10118e-06,6.95735e-10,-5.26521e-14,12906.2,-64.4098], Tmin=(941.22,'K'), Tmax=(5000,'K')),
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
    index = 11,
    label = "C6H7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {4,S} {10,S}
3  C u0 p0 c0 {1,S} {5,D} {9,S}
4  C u0 p0 c0 {2,S} {6,D} {11,S}
5  C u0 p0 c0 {3,D} {6,S} {13,S}
6  C u0 p0 c0 {4,D} {5,S} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.48059,0.0132581,8.26914e-05,-1.16387e-07,4.51969e-11,23633.9,16.099], Tmin=(100,'K'), Tmax=(956.69,'K')),
            NASAPolynomial(coeffs=[13.3874,0.0187092,-5.9021e-06,1.12946e-09,-8.83565e-14,19210.6,-48.2479], Tmin=(956.69,'K'), Tmax=(5000,'K')),
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
    index = 12,
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
            NASAPolynomial(coeffs=[3.59281,-0.00375065,4.40545e-05,-5.1768e-08,1.91824e-11,5113.8,5.48752], Tmin=(100,'K'), Tmax=(889.17,'K')),
            NASAPolynomial(coeffs=[2.5758,0.0132189,-5.4815e-06,1.04904e-09,-7.54583e-14,4804.7,7.51939], Tmin=(889.17,'K'), Tmax=(5000,'K')),
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
    index = 13,
    label = "C8H10",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {5,S} {10,S}
2  C u0 p0 c0 {1,D} {3,S} {11,S}
3  C u0 p0 c0 {2,S} {4,D} {12,S}
4  C u0 p0 c0 {3,D} {6,S} {13,S}
5  C u0 p0 c0 {1,S} {7,D} {9,S}
6  C u0 p0 c0 {4,S} {8,D} {14,S}
7  C u0 p0 c0 {5,D} {15,S} {16,S}
8  C u0 p0 c0 {6,D} {17,S} {18,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.0864066,0.0659513,1.48806e-06,-6.06835e-08,3.13833e-11,23908.9,26.6194], Tmin=(100,'K'), Tmax=(941.39,'K')),
            NASAPolynomial(coeffs=[22.8419,0.0196702,-5.08789e-06,8.53648e-10,-6.42354e-14,17390.9,-93.6517], Tmin=(941.39,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

