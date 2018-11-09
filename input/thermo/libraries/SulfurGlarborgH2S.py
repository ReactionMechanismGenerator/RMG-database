#!/usr/bin/env python
# encoding: utf-8

name = "SulfurGlarborgH2S"
shortDesc = u""
longDesc = u"""
H2S oxidation at high pressures

An Exploratory Flow Reactor Study of H2S Oxidation at 30-100 Bar
Y. Song, H. Hashemi, J.M. Christensen, C. Zou, B.S. Haynes, P. Marshall, P. Glarborg
International Journal of Chemical Kinetics 49(1), 2017, 37-52
DOI: 10.1002/kin.21055
"""
entry(
    index = 0,
    label = "SO",
    molecule = 
"""
multiplicity 3
1 S u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.6186,-0.00232174,1.16463e-05,-1.42093e-08,5.60765e-12,-480.622,6.36504], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.96894,0.000377297,7.67103e-09,-1.37544e-11,1.37139e-15,-728.572,3.73493], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
tpis89
GBR 1509
1.14 53.04
""",
)

entry(
    index = 1,
    label = "SO2",
    molecule = 
"""
1 S u0 p1 c0 {2,D} {3,D}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67481,0.00228302,8.46893e-06,-1.36562e-08,5.76272e-12,-36945.5,7.96866], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.38423,0.00167931,-6.32063e-07,1.08465e-10,-6.6689e-15,-37606.7,-1.83131], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
tpis89
-70.95  59.29
GBR1509
""",
)

entry(
    index = 2,
    label = "S",
    molecule = 
"""
multiplicity 3
1 S u2 p2 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.31726,0.00478018,-1.42083e-05,1.5657e-08,-5.96588e-12,32506.9,6.06242], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.87936,-0.00051105,2.53807e-07,-4.45455e-11,2.66717e-15,32501.4,3.98141], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
J 9/82
66.19/40.11
GBR 1509
""",
)

entry(
    index = 3,
    label = "O3",
    molecule = 
"""
1 O u0 p3 c-1 {2,S}
2 O u0 p1 c+1 {1,S} {3,D}
3 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.46261,0.00958278,-7.08736e-06,1.36337e-09,2.96965e-13,16061.5,12.1419], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.42937,0.00182038,-7.70561e-07,1.49929e-10,-1.07556e-14,15235.3,-3.26639], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
121286
""",
)

entry(
    index = 4,
    label = "SO(S)",
    molecule = 
"""
1 S u0 p2 c0 {2,D}
2 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.0804,0.00180311,6.70502e-07,-2.06901e-09,8.51466e-13,9825.1,8.58103], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.02108,0.000258486,8.94814e-08,-3.58014e-11,3.22843e-15,9511.76,3.45252], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Zhou: G3
21.51  53.01
""",
)

entry(
    index = 5,
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
            NASAPolynomial(coeffs=[4.13565,-0.00369243,2.0517e-05,-2.40531e-08,9.17084e-12,-3823.72,5.8877], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.34724,0.00253372,-9.51431e-07,1.58095e-10,-9.65295e-15,-4208.94,3.15888], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
T04/07
GBR 1509
-5.20  57.75
""",
)

entry(
    index = 6,
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
            NASAPolynomial(coeffs=[3.69441,0.000394328,1.10155e-05,-1.63103e-08,7.03353e-12,-1992.57,7.31636], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.37246,0.00201399,-6.50854e-07,9.74413e-11,-5.52225e-15,-2285.78,3.13657], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
T04/07
GBR 1509
-1.60/57.31
""",
)

entry(
    index = 7,
    label = "HSOH",
    molecule = 
"""
1 S u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.56764,0.0113805,-5.86673e-06,-5.947e-10,8.74383e-13,-15571.3,11.7664], Tmin=(200,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[2.56764,0.0113805,-5.86673e-06,-5.947e-10,8.74383e-13,-15571.3,11.7664], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
-28.52  58.66
GLABOZ96
Zhou - Leeds University
""",
)

entry(
    index = 8,
    label = "HOSO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 S u1 p1 c0 {1,S} {3,D}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.87,13.43,14.56,15.37,16.4,17.06,18.09],'cal/(mol*K)'),
        H298 = (-57.71,'kcal/mol'),
        S298 = (67.48,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
DAGGLA03 GOUMAr99
DAG/GLA03 GOU/MAr99
-57.70  67.47
""",
)

entry(
    index = 9,
    label = "HSO2",
    molecule = 
"""
multiplicity 2
1 S u1 p0 c0 {2,S} {3,D} {4,D}
2 H u0 p0 c0 {1,S}
3 O u0 p2 c0 {1,D}
4 O u0 p2 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.94,13.68,14.99,15.98,17.28,18.05,18.98],'cal/(mol*K)'),
        H298 = (-33.8,'kcal/mol'),
        S298 = (63.01,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
ALZ/GLA01 GOU/MAr99
Zhou - Leeds University
-33.80  63.00
""",
)

entry(
    index = 10,
    label = "H2SO",
    molecule = 
"""
1 S u0 p1 c0 {2,D} {3,S} {4,S}
2 O u0 p2 c0 {1,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.52,11.17,12.65,13.92,15.85,16.99,18.44],'cal/(mol*K)'),
        H298 = (-11.26,'kcal/mol'),
        S298 = (57.27,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
ALZ/GLA01   BOZ/R
-11.26/57.26
""",
)

entry(
    index = 11,
    label = "HOSHO",
    molecule = 
"""
1 S u0 p1 c0 {2,S} {3,D} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 O u0 p2 c0 {1,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.57,15.86,17.64,19,20.84,21.95,23.54],'cal/(mol*K)'),
        H298 = (-64.51,'kcal/mol'),
        S298 = (64.49,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
ALZ/GLA01   BOZ/R
-64.50/64.48
""",
)

entry(
    index = 12,
    label = "HOSO2",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 S u1 p0 c0 {1,S} {3,D} {5,D}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([16.95,18.47,19.95,21.22,22.65,22.57,24.09],'cal/(mol*K)'),
        H298 = (-88.68,'kcal/mol'),
        S298 = (70.73,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Zhou - Leeds University
-88.67  70.73
""",
)

entry(
    index = 13,
    label = "O",
    molecule = 
"""
multiplicity 3
1 O u2 p2 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.94643,-0.00163817,2.42103e-06,-1.60284e-09,3.8907e-13,29147.6,2.96399], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.54206,-2.75506e-05,-3.1028e-09,4.55107e-12,-4.36805e-16,29230.8,4.92031], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
120186
LI/DRY04 (v6.1)
""",
)

entry(
    index = 14,
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
    shortDesc = u"""""",
    longDesc = 
u"""
tpis89
Zhou - Burcat
30.73  54.52
""",
)

entry(
    index = 15,
    label = "SH",
    molecule = 
"""
multiplicity 2
1 S u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.13333,-0.000378789,-2.77785e-06,5.37011e-09,-2.39401e-12,16027.7,0.161154], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.05381,0.00125888,-4.24917e-07,6.92959e-11,-4.28169e-15,16351.3,5.97355], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
34.23  46.73
Zhou: R.C. Shiell, X.K. Hu, Q.J. Hu, J.W. Hepburn, J. Phys. Chem. A 104 (2000) 4339-4342.
""",
)

entry(
    index = 16,
    label = "H2S",
    molecule = 
"""
1 S u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.12024,-0.00187907,8.21427e-06,-7.06426e-09,2.14235e-12,-3682.15,1.53174], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.97879,0.0035976,-1.22803e-06,1.96833e-10,-1.16716e-14,-3516.08,6.77921], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
g 4/01
GBR 1509
-4.92  49.18
""",
)

entry(
    index = 17,
    label = "HSS",
    molecule = 
"""
multiplicity 2
1 S u1 p1 c0 {2,D} {3,S}
2 S u0 p2 c0 {1,D}
3 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.62,10.3,10.8,11.19,11.8,12.26,12.98],'cal/(mol*K)'),
        H298 = (25.84,'kcal/mol'),
        S298 = (60.95,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Zhou - K. Sendt, B.S. Haynes, J. Phys. Chem. A 109 (2005) 8180 to 8186; 
K. Sendt, M. Jazbec, B.S. Haynes, Proc. Combust. Inst. 29 (2003) 2439-2446.
25.84  60.94
""",
)

entry(
    index = 18,
    label = "HSSH",
    molecule = 
"""
1 S u0 p2 c0 {2,S} {3,S}
2 S u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.63,12.9,13.84,14.57,15.73,16.62,18.02],'cal/(mol*K)'),
        H298 = (3.7,'kcal/mol'),
        S298 = (61.62,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Zhou - K. Sendt, B.S. Haynes, J. Phys. Chem. A 109 (2005) 8180 to 8186;
K. Sendt, M. Jazbec, B.S. Haynes, Proc. Combust. Inst. 29 (2003) 2439-2446.
3.70  61.61
""",
)

entry(
    index = 19,
    label = "SO3",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 S u0 p0 c0 {1,D} {3,D} {4,D}
3 O u0 p2 c0 {2,D}
4 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.37461,0.0159543,-1.26323e-05,2.81827e-09,6.23372e-13,-48926.9,13.1043], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.29678,0.00273576,-1.06378e-06,1.80776e-10,-1.12078e-14,-50309.7,-12.4247], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
tpis89
-94.61  61.30
GBR 1509
""",
)

entry(
    index = 20,
    label = "S2O",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 S u0 p1 c0 {1,D} {3,D}
3 S u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.89888,0.0115444,-1.46502e-05,9.19412e-09,-2.31495e-12,-8193.13,12.6536], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.69256,0.00142824,-3.95224e-07,-9.64671e-11,4.47355e-14,-8829.71,-1.14896], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Zhou - K. Sendt, B.S. Haynes, J. Phys. Chem. A 109 (2005) 8180 to 8186;
K. Sendt, M. Jazbec, B.S. Haynes, Proc. Combust. Inst. 29 (2003) 2439-2446.
-13.77  63.65
""",
)

entry(
    index = 21,
    label = "HSSO",
    molecule = 
"""
multiplicity 2
1 S u0 p2 c0 {2,S} {4,S}
2 S u0 p2 c0 {1,S} {3,S}
3 O u1 p2 c0 {2,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.93,15.2,16.04,16.63,17.45,18.02,18.85],'cal/(mol*K)'),
        H298 = (-7.89,'kcal/mol'),
        S298 = (68.61,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Zhou: PhD; L.A. Curtiss, K. RaghavachAri, P.C. Redfern, V.
Rassolov, J.A. Pople, J. Chem. Phys. 109 (1998) 7764-7776
-7.89  68.60
""",
)

entry(
    index = 22,
    label = "VDW1",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 S u0 p1 c0 {1,D} {3,D}
3 O u0 p2 c0 {2,D}
4 O u0 p2 c0 {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.13179,0.00832445,-2.04192e-06,-2.95154e-09,1.78217e-12,-68828.7,-6.98379], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.1262,0.00357133,-7.13009e-09,-5.82223e-10,1.37376e-13,-69388.2,-17.4037], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
VDW of H2O.SO2
Zhou - K. Sendt, B.S. Haynes, J. Phys. Chem. A 109 (2005) 8180 to 8186; 
K. Sendt, M. Jazbec, B.S. Haynes, Proc. Combust. Inst. 29 (2003) 2439-2446.
-131.26  82.88
""",
)

entry(
    index = 23,
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([16.99,18.76,20.07,21.04,22.39,23.27,24.46],'cal/(mol*K)'),
        H298 = (-40.9,'kcal/mol'),
        S298 = (73.62,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Zhou: PhD; L.A. Curtiss, K. RaghavachAri, P.C. Redfern, V.
Rassolov, J.A. Pople, J. Chem. Phys. 109 (1998) 7764-7776
-40.89  73.61
""",
)

entry(
    index = 24,
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
            NASAPolynomial(coeffs=[2.91749,0.0189316,-2.22226e-05,1.24562e-08,-2.69875e-12,-22883.4,12.9944], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.64652,0.0051481,-3.24616e-06,9.37856e-10,-1.0229e-13,-23685.8,-5.27911], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
1511
pw PM 1511
""",
)

entry(
    index = 25,
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
            NASAPolynomial(coeffs=[3.0464,0.0152114,-1.84763e-05,1.13862e-08,-2.72422e-12,14807.4,12.8748], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.87948,0.0045858,-2.93622e-06,1.10178e-09,-1.86219e-13,14170.6,-1.04623], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Zhou: C. Zhou, K. Sendt, B.S. Haynes, J. Phys. Chem. A 113 (2009) 2975-2981.
32.29  67.63
""",
)

entry(
    index = 26,
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
    shortDesc = u"""""",
    longDesc = 
u"""
tpis89
Zhou - Burcat
34.59  66.02
""",
)

entry(
    index = 27,
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
    shortDesc = u"""""",
    longDesc = 
u"""
tpis89
Zhou - Burcat
32.41  70.15
""",
)

entry(
    index = 28,
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
    shortDesc = u"""""",
    longDesc = 
u"""
tpis89
Zhou - Burcat
31.78  84.61
""",
)

entry(
    index = 29,
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
    shortDesc = u"""""",
    longDesc = 
u"""
tpis89
Zhou - Burcat
24.21  85.50
""",
)

entry(
    index = 30,
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
    shortDesc = u"""""",
    longDesc = 
u"""
tpis89
Zhou - Burcat
26.73  96.74
""",
)

entry(
    index = 31,
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
    shortDesc = u"""""",
    longDesc = 
u"""
tpis89
Zhou - Burcat
24.20 103.35
""",
)

entry(
    index = 32,
    label = "OSSO",
    molecule = 
"""
1 S u0 p1 c0 {2,D} {3,D}
2 S u0 p1 c0 {1,D} {4,D}
3 O u0 p2 c0 {1,D}
4 O u0 p2 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.37,16.56,17.4,17.98,18.7,19.08,19.5],'cal/(mol*K)'),
        H298 = (-28.15,'kcal/mol'),
        S298 = (71.34,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Zhou: PhD; L.A. Curtiss, K. RaghavachAri, P.C. Redfern, V.
Rassolov, J.A. Pople, J. Chem. Phys. 109 (1998) 7764-7776
-28.15  71.33
""",
)

entry(
    index = 33,
    label = "H2S3O",
    molecule = 
"""
1 S u0 p1 c+1 {2,S} {3,S} {4,S}
2 S u0 p2 c0 {1,S} {5,S}
3 S u0 p2 c0 {1,S} {6,S}
4 O u0 p3 c-1 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67805,0.0407191,-6.6799e-05,5.28547e-08,-1.60811e-11,-11398,9.98571], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.8514,0.00333851,-6.86563e-07,-2.026e-10,7.4778e-14,-12885.3,-28.5027], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Zhou - K. Sendt, B.S. Haynes, J. Phys. Chem. A 109 (2005) 8180 to 8186; 
! K. Sendt, M. Jazbec, B.S. Haynes, Proc. Combust. Inst. 29 (2003) 2439-2446.
-17.86  80.56
""",
)

entry(
    index = 34,
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
            NASAPolynomial(coeffs=[2.93988,0.0405696,-6.59919e-05,5.33283e-08,-1.67311e-11,-16302.9,14.9845], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.0809,0.00373388,-2.44411e-07,-6.13454e-10,1.6465e-13,-17835.6,-23.5332], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Zhou - K. Sendt, B.S. Haynes, J. Phys. Chem. A 109 (2005) 8180 to 8186;
K. Sendt, M. Jazbec, B.S. Haynes, Proc. Combust. Inst. 29 (2003) 2439-2446.
-28.04  82.12
""",
)

entry(
    index = 35,
    label = "H2S2O2",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {5,S}
2 S u0 p1 c0 {1,S} {3,S} {4,D}
3 S u0 p2 c0 {2,S} {6,S}
4 O u0 p2 c0 {2,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.828112,0.0474478,-6.95648e-05,4.87812e-08,-1.32222e-11,-36928.8,22.9903], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.6213,0.00343806,-5.74448e-07,-3.13293e-10,1.00662e-13,-39104.8,-29.0177], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Zhou - K. Sendt, B.S. Haynes, J. Phys. Chem. A 109 (2005) 8180 to 8186; 
K. Sendt, M. Jazbec, B.S. Haynes, Proc. Combust. Inst. 29 (2003) 2439-2446.
-69.74  77.82
""",
)

entry(
    index = 36,
    label = "HOCO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 C u1 p0 c0 {1,S} {3,D}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.35681,0.00898413,-7.12206e-06,2.4573e-09,-1.42885e-13,-23787.2,14.3851], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.63651,0.00274146,-9.95898e-07,1.60387e-10,-9.16199e-15,-24440.1,2.54925], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
CLR est L 7/88
CLR est based on CO2 data and SANDIA
H298=-45.19 kcal/mol
S298= 60.00 cal/mol/K
""",
)

entry(
    index = 37,
    label = "HOSOH",
    molecule = 
"""
1 S u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 O u0 p2 c0 {1,S} {5,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.92,15.88,17.33,18.4,19.85,20.85,22.57],'cal/(mol*K)'),
        H298 = (-75.31,'kcal/mol'),
        S298 = (64.94,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
ALZ/GLA01  BOZ/R
""",
)

entry(
    index = 38,
    label = "H2SO4",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 S u0 p0 c0 {1,D} {3,D} {4,S} {5,S}
3 O u0 p2 c0 {2,D}
4 O u0 p2 c0 {2,S} {6,S}
5 O u0 p2 c0 {2,S} {7,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.53388,0.0310348,-4.10422e-05,2.95752e-08,-8.81459e-12,-90545.9,3.93961], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.3355,0.00560829,-1.94574e-06,3.07136e-10,-1.8111e-14,-92108.7,-29.6094], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Burcat
""",
)

