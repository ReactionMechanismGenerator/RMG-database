#!/usr/bin/env python
# encoding: utf-8

name = "SulfurHaynes"
shortDesc = u"H2S oxidation"
longDesc = u"""
Taken from:
Chenlai (Ryan) Zhou, Karina Sendt, Brian S. Haynes
Proceedings of the Combustion Institute 2013, 34(1), 625-632
doi: 10.1016/j.proci.2012.05.083

legend:
Leeds: Leeds University Sulphur Mechanism, version 5.2
Burcat: A. Burcat, B. Ruscic, Ideal Gas Thermochemical Database with Updates from Active Thermochemical Tables
Sendt: K. Sendt, B.S. Haynes, J. Phys. Chem. A 109 (2005) 8180-8186; K. Sendt, M. Jazbec, B.S. Haynes, Proc. Combust. Inst. 29 (2003) 2439-2446
G3: C. Zhou, Kinetic Study of The Oxidation of Hydrogen Sulfide, Ph.D. thesis, The University of Sydney, 2009
"""

entry(
    index = 1,
    label = "S",
    molecule = 
"""
multiplicity 3
1 S u2 p2 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.18733,-0.00159578,2.00553e-06,-1.50708e-09,4.93128e-13,32422.6,2.41444], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.90215,-0.000548455,2.76458e-07,-5.01711e-11,3.15069e-15,32494.2,3.83847], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Leeds""",
)

entry(
    index = 2,
    label = "SH",
    molecule = 
"""
multiplicity 2
1 S u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.13333,-0.000378789,-2.77785e-06,5.37011e-09,-2.39401e-12,16027.7,0.161154], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.05381,0.00125888,-4.24917e-07,6.92959e-11,-4.28169e-15,16351.3,5.97355], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
H298 is taken from R.C. Shiell, X.K. Hu, Q.J. Hu, J.W. Hepburn, J. Phys. Chem. A 104 (2000) 4339-4342
""",
)

entry(
    index = 3,
    label = "H2S",
    molecule = 
"""
1 S u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.07103,0.00557826,-1.03097e-05,1.20195e-08,-4.83837e-12,-3559.83,5.93523], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.88315,0.00382783,-1.4234e-06,2.498e-10,-1.66027e-14,-3480.74,7.25816], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Leeds""",
)

entry(
    index = 4,
    label = "SO",
    molecule = 
"""
multiplicity 3
1 S u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.0804,0.00180311,6.70502e-07,-2.06901e-09,8.51466e-13,-398.616,8.58103], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.02108,0.000258486,8.94814e-08,-3.58014e-11,3.22843e-15,-711.962,3.45252], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Leeds""",
)

entry(
    index = 5,
    label = "SO(S)",
    molecule = 
"""
1 S u0 p2 c0 {2,D}
2 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.0804,0.00180311,6.70502e-07,-2.06901e-09,8.51466e-13,9825.1,8.58103], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.02108,0.000258486,8.94814e-08,-3.58014e-11,3.22843e-15,9511.76,3.45252], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""G3""",
)

entry(
    index = 6,
    label = "SO2",
    molecule = 
"""
1 S u0 p1 c0 {2,D} {3,D}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.91144,0.00810302,-6.90671e-06,3.32902e-09,-8.77712e-13,-36878.8,11.1174], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.2545,0.00197854,-8.20423e-07,1.57638e-10,-1.12045e-14,-37568.9,-1.14606], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Leeds""",
)

entry(
    index = 7,
    label = "SO3",
    molecule = 
"""
1 S u0 p0 c0 {2,D} {3,D} {4,D}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,D}
4 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.57528,0.0151509,-1.22987e-05,4.24026e-09,-5.26681e-13,-48944.1,12.1951], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.05067,0.00324656,-1.4089e-06,2.72154e-10,-1.94236e-14,-50206.7,-11.0644], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Leeds""",
)

entry(
    index = 8,
    label = "HSO2",
    molecule = 
"""
multiplicity 2
1 S u1 p0 c0 {2,D} {3,D} {4,S}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,D}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.56274,0.0206914,-2.31121e-05,1.26702e-08,-2.72742e-12,-18214.8,17.5568], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.56274,0.0206914,-2.31121e-05,1.26702e-08,-2.72742e-12,-18214.8,17.5568], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = u"""Leeds""",
)

entry(
    index = 9,
    label = "HOSO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 S u1 p1 c0 {1,S} {3,D}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.60147,-0.0253593,6.76829e-05,-6.34954e-08,1.95894e-11,-31254,-15.6741], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.60147,-0.0253593,6.76829e-05,-6.34954e-08,1.95894e-11,-31254,-15.6741], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = u"""Leeds""",
)

entry(
    index = 10,
    label = "HSOO",
    molecule = 
"""
multiplicity 2
1 S u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u1 p2 c0 {2,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.0464,0.0152114,-1.84763e-05,1.13862e-08,-2.72422e-12,14807.4,12.8748], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.87948,0.0045858,-2.93622e-06,1.10178e-09,-1.86219e-13,14170.6,-1.04623], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
H298 from C. Zhou, K. Sendt, B.S. Haynes, J. Phys. Chem. A 113 (2009) 2975-2981
""",
)

entry(
    index = 11,
    label = "HOSO2",
    molecule = 
"""
multiplicity 2
1 S u0 p1 c0 {2,S} {3,D} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 O u0 p2 c0 {1,D}
4 O u1 p2 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.62277,-0.00419909,3.52055e-05,-4.12715e-08,1.40007e-11,-46947.8,-7.80788], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.62277,-0.00419909,3.52055e-05,-4.12715e-08,1.40007e-11,-46947.8,-7.80788], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = u"""Leeds""",
)

entry(
    index = 12,
    label = "S2",
    molecule = 
"""
multiplicity 3
1 S u1 p2 c0 {2,S}
2 S u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.87737,0.00500301,-6.04371e-06,3.04739e-09,-3.87018e-13,14434.2,9.79874], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.8325,0.000888971,-2.59081e-07,3.63847e-11,-1.72606e-15,14283.6,5.33001], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""Burcat""",
)

entry(
    index = 13,
    label = "S3",
    molecule = 
"""
1 S u0 p1 c0 {2,D} {3,D}
2 S u0 p2 c0 {1,D}
3 S u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.67426,0.0185726,-3.39241e-05,2.89518e-08,-9.41516e-12,16032,13.727], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.53302,0.000489117,-1.9412e-07,3.34257e-11,-2.09107e-15,15318.7,-4.42378], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""Burcat""",
)

entry(
    index = 14,
    label = "S4",
    molecule = 
"""
1 S u0 p2 c0 {2,S} {4,S}
2 S u0 p2 c0 {1,S} {3,S}
3 S u0 p2 c0 {2,S} {4,S}
4 S u0 p2 c0 {1,S} {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.62124,0.0369694,-6.92244e-05,6.03241e-08,-1.99529e-11,14688,17.6312], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.12782,0.000913784,-3.62719e-07,6.24637e-11,-3.90795e-15,13330.9,-17.4976], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""Burcat""",
)

entry(
    index = 15,
    label = "S5",
    molecule = 
"""
1 S u0 p2 c0 {2,S} {5,S}
2 S u0 p2 c0 {1,S} {3,S}
3 S u0 p2 c0 {2,S} {4,S}
4 S u0 p2 c0 {3,S} {5,S}
5 S u0 p2 c0 {1,S} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.27621,0.0432968,-8.47663e-05,8.12574e-08,-2.97794e-11,13696.5,14.1197], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.3326,0.000209783,-3.36432e-07,8.53312e-11,-6.48295e-15,11378.8,-34.8612], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""Burcat""",
)

entry(
    index = 16,
    label = "S6",
    molecule = 
"""
1 S u0 p2 c0 {2,S} {6,S}
2 S u0 p2 c0 {1,S} {3,S}
3 S u0 p2 c0 {2,S} {4,S}
4 S u0 p2 c0 {3,S} {5,S}
5 S u0 p2 c0 {4,S} {6,S}
6 S u0 p2 c0 {1,S} {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.69716,0.0686819,-0.000143788,1.35427e-07,-4.71806e-11,9353.5,12.4775], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.4044,0.00342127,-1.12816e-06,1.4642e-10,-6.61286e-15,8108.61,-34.2546], Tmin=(1000,'K'), Tmax=(2500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (2500,'K'),
    ),
    shortDesc = u"""Burcat""",
)

entry(
    index = 17,
    label = "S7",
    molecule = 
"""
1 S u0 p2 c0 {2,S} {7,S}
2 S u0 p2 c0 {1,S} {3,S}
3 S u0 p2 c0 {2,S} {4,S}
4 S u0 p2 c0 {3,S} {5,S}
5 S u0 p2 c0 {4,S} {6,S}
6 S u0 p2 c0 {5,S} {7,S}
7 S u0 p2 c0 {1,S} {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.91733,0.082965,-0.000173743,1.63959e-07,-5.74388e-11,10138,13.7222], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[17.8534,0.00121114,-4.83082e-07,8.34577e-11,-5.23295e-15,7807.77,-54.0619], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""Burcat""",
)

entry(
    index = 18,
    label = "S8",
    molecule = 
"""
1 S u0 p2 c0 {2,S} {8,S}
2 S u0 p2 c0 {1,S} {3,S}
3 S u0 p2 c0 {2,S} {4,S}
4 S u0 p2 c0 {3,S} {5,S}
5 S u0 p2 c0 {4,S} {6,S}
6 S u0 p2 c0 {5,S} {7,S}
7 S u0 p2 c0 {6,S} {8,S}
8 S u0 p2 c0 {1,S} {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.13158,0.0943299,-0.000205776,2.05748e-07,-7.51844e-11,8203.19,7.83537], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[20.4308,0.00518093,-2.91895e-06,5.97575e-10,-4.13758e-14,5118.43,-67.4373], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""Burcat""",
)

entry(
    index = 19,
    label = "HSO",
    molecule = 
"""
multiplicity 2
1 S u1 p1 c0 {2,S} {3,D}
2 H u0 p0 c0 {1,S}
3 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.69499,0.00852437,-9.6799e-06,6.24322e-09,-1.68282e-12,-3724.66,11.6328], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.27129,0.00544982,-3.73779e-06,1.30021e-09,-1.83114e-13,-3808.55,9.02815], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
H298 taken from P.A. Denis, Chem. Phys. Lett. 402 (2005)289-293
""",
)

entry(
    index = 20,
    label = "HOS",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 S u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.63737,0.00789119,-8.11726e-06,4.24834e-09,-8.57901e-13,-1890.59,11.7097], Tmin=(298,'K'), Tmax=(1442,'K')),
            NASAPolynomial(coeffs=[2.63737,0.00789119,-8.11726e-06,4.24834e-09,-8.57901e-13,-1890.59,11.7097], Tmin=(1442,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
H298 taken from P.A. Denis, Chem. Phys. Lett. 402 (2005)289-293
""",
)

entry(
    index = 21,
    label = "HSOH",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 S u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.56764,0.0113805,-5.86673e-06,-5.947e-10,8.74383e-13,-15571.3,11.7664], Tmin=(298,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[2.56764,0.0113805,-5.86673e-06,-5.947e-10,8.74383e-13,-15571.3,11.7664], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Leeds""",
)

entry(
    index = 22,
    label = "HSS",
    molecule = 
"""
multiplicity 2
1 S u1 p1 c0 {2,D} {3,S}
2 S u0 p2 c0 {1,D}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.81672,0.010397,-1.55535e-05,1.24198e-08,-3.90835e-12,11815.7,12.1144], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.59076,0.00498507,-3.43046e-06,1.19342e-09,-1.67403e-13,11765,8.92476], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = u"""Sendt""",
)

entry(
    index = 23,
    label = "HSSO",
    molecule = 
"""
multiplicity 2
1 S u0 p2 c0 {2,S} {4,S}
2 S u0 p2 c0 {1,S} {3,S}
3 O u1 p2 c0 {2,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.70485,0.0232127,-3.77895e-05,3.04179e-08,-9.47692e-12,-5528.11,13.6259], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.11859,0.00559523,-3.70627e-06,1.22525e-09,-1.6279e-13,-6058.87,-1.97721], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = u"""G3""",
)

entry(
    index = 24,
    label = "HSSH",
    molecule = 
"""
1 S u0 p2 c0 {2,S} {3,S}
2 S u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.07852,0.0194743,-2.93966e-05,2.37296e-08,-7.52058e-12,596.292,14.4742], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.69311,0.00601994,-3.01832e-06,7.52298e-10,-7.91533e-14,172.18,2.47729], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = u"""Sendt""",
)

entry(
    index = 25,
    label = "SSO2",
    molecule = 
"""
1 S u0 p0 c0 {2,D} {3,D} {4,D}
2 S u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,D}
4 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.80169,0.0199919,-2.56401e-05,1.6556e-08,-4.3362e-12,-22022.6,13.4189], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.34281,0.00605028,-4.24572e-06,1.40853e-09,-1.81318e-13,-22768.5,-3.78738], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = u"""G3""",
)

entry(
    index = 26,
    label = "HSSO2",
    molecule = 
"""
multiplicity 2
1 S u0 p0 c0 {2,D} {3,D} {4,D}
2 S u1 p1 c0 {1,D} {5,S}
3 O u0 p2 c0 {1,D}
4 O u0 p2 c0 {1,D}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49857,0.0250749,-3.40614e-05,2.40531e-08,-6.85627e-12,-22479.4,10.9552], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.76282,0.00702637,-4.08429e-06,1.1246e-09,-1.18489e-13,-23327.2,-9.48284], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = u"""G3""",
)

entry(
    index = 27,
    label = "OSSO",
    molecule = 
"""
1 S u0 p1 c0 {2,D} {3,D}
2 S u0 p1 c0 {1,D} {4,D}
3 O u0 p2 c0 {1,D}
4 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.27684,0.0171764,-2.30032e-05,1.50851e-08,-3.93336e-12,-16027.6,7.31095], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.06933,0.00278601,-1.65788e-06,4.55717e-10,-4.76688e-14,-16859.8,-11.2638], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = u"""G3""",
)

entry(
    index = 28,
    label = "VDW1",
    molecule = 
"""
1 S u0 p1 c0 {3,D} {4,D}
2 O u0 p2 c0 {5,S} {6,S}
3 O u0 p2 c0 {1,D}
4 O u0 p2 c0 {1,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.13179,0.00832445,-2.04192e-06,-2.95154e-09,1.78217e-12,-68828.7,-6.98379], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.1262,0.00357133,-7.13009e-09,-5.82223e-10,1.37376e-13,-69388.2,-17.4037], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Sendt""",
)

entry(
    index = 29,
    label = "H2S2O2",
    molecule = 
"""
1 S u0 p1 c0 {2,S} {3,S} {4,D}
2 O u0 p2 c0 {1,S} {5,S}
3 S u0 p2 c0 {1,S} {6,S}
4 O u0 p2 c0 {1,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.828112,0.0474478,-6.95648e-05,4.87812e-08,-1.32222e-11,-36928.8,22.9903], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.6213,0.00343806,-5.74448e-07,-3.13293e-10,1.00662e-13,-39104.8,-29.0177], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Sendt""",
)

entry(
    index = 30,
    label = "S2O",
    molecule = 
"""
1 S u0 p1 c0 {2,D} {3,D}
2 O u0 p2 c0 {1,D}
3 S u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.89888,0.0115444,-1.46502e-05,9.19412e-09,-2.31495e-12,-8193.13,12.6536], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.69256,0.00142824,-3.95224e-07,-9.64671e-11,4.47355e-14,-8829.71,-1.14896], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Sendt""",
)

entry(
    index = 31,
    label = "H2S3O",
    molecule = 
"""
1 S u0 p1 c0 {2,S} {3,S} {4,D}
2 S u0 p2 c0 {1,S} {5,S}
3 S u0 p2 c0 {1,S} {6,S}
4 O u0 p2 c0 {1,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67805,0.0407191,-6.6799e-05,5.28547e-08,-1.60811e-11,-11398,9.98571], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.8514,0.00333851,-6.86563e-07,-2.026e-10,7.4778e-14,-12885.3,-28.5027], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Sendt""",
)

entry(
    index = 32,
    label = "HSSSOH",
    molecule = 
"""
1 S u0 p2 c0 {2,S} {3,S}
2 S u0 p2 c0 {1,S} {4,S}
3 O u0 p2 c0 {1,S} {5,S}
4 S u0 p2 c0 {2,S} {6,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.93988,0.0405696,-6.59919e-05,5.33283e-08,-1.67311e-11,-16302.9,14.9845], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.0809,0.00373388,-2.44411e-07,-6.13454e-10,1.6465e-13,-17835.6,-23.5332], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Sendt""",
)

entry(
    index = 33,
    label = "O3",
    molecule =
"""
1 O u0 p1 c+1 {2,S} {3,D}
2 O u0 p3 c-1 {1,S}
3 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.40738,0.00205379,1.38486e-05,-2.23312e-08,9.76073e-12,15864.5,8.28248], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.3303,-0.0119325,7.98741e-06,-1.77195e-09,1.26076e-13,12675.6,-40.8823], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""Burcat""",
)
