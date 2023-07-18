#!/usr/bin/env python
# encoding: utf-8

name = "pdep_28"
shortDesc = ""
longDesc = """
ARC v1.1.0
ARC project pdep_28

Levels of theory used:

Conformers:       wb97xd/def2svp, software: gaussian (dft)
TS guesses:       None
Composite method: cbs-qb3, software: gaussian (composite) (NOT using a fine grid)
Frequencies:      b3lyp/cbsb7, software: gaussian (dft)
Rotor scans:      None
Using p-type bond additivity corrections for thermo

Using the following ESS settings: {'gaussian': ['local']}

Considered the following species and TSs:
Species DMF[1] (run time: 0:17:25)
Species C[C]=CC=C[C][O][1230] (Failed!) (run time: None)
Species C=C[[O]][CH]C=CC[1265] (Failed!) (run time: None)
Species C[CH]C=CC[C]=O[1373] (Failed!) (run time: None)
Species [CH2]C=CC[C][C]=O[1508] (Failed!) (run time: None)
Species [CH2]C[[C]=O]C=CC[1476] (Failed!) (run time: None)
Species [CH2]C[C][CH]C=C=O[1449] (Failed!) (run time: None)
Species [CH2]C=CC[[O]]=CC[1560] (Failed!) (run time: None)
Species C=CC1=CCCO1[1792] (run time: 0:46:18)
Species [CH2]CC=C[[O]]C=C[1705] (Failed!) (run time: None)
Species CC[C]=CC=C[O][1884] (Failed!) (run time: None)
Species CC1[CH]CC=C1[O][1513] (run time: 0:45:08)
Species CC1CC=CC1=O[1669] (run time: 0:24:01)
Species [CH2]C=CC=C[C][O][1259] (Failed!) (run time: None)
Species C=C1C=CCCO1[2159] (run time: 0:18:43)
Species [CH2]CC=CC[=C][O][1363] (Failed!) (run time: None)
Species C=C[O]C=C=CC[1344] (run time: 1:20:52)
Species CC1=COC[C]=C1[1313] (run time: 1:21:37)
Species C=[C]C=CCC[O][2197] (Failed!) (run time: None)
Species [CH2]C[C]=CC[C]=O[2118] (Failed!) (run time: None)
Species C[C]1CC1=C[C][O][1320] (Failed!) (run time: None)
Species C=C[C][C]=C[C][O][2089] (Failed!) (run time: None)
Species C=[C]C[[O]]C=CC[1424] (Failed!) (run time: None)
Species C=C[C]C[[O]]=[C]C[2614] (Failed!) (run time: None)
Species C=C=CC1CCO1[2195] (run time: 1:49:14)
Species CC=CC=[C]C[O][1398] (Failed!) (run time: None)
Species [CH2]C1[CH]C1C[C]=O[1321] (Failed!) (run time: None)
Species C=CC[[O]]C=[C]C[2172] (Failed!) (run time: None)
Species C[C]=CC=CC[O][2142] (Failed!) (run time: None)
Species [CH]C=CC=C[C]O[1750] (Failed!) (run time: None)
Species CCtC[C][C]C[O][2598] (Failed!) (run time: None)
Species [CH2]C[C][[O]]CtCC[4388] (Failed!) (run time: None)
Species [CH2]C[=[C]C]C[C]=O[4100] (Failed!) (run time: None)
Species C=[C]O[CH]C=CC[1425] (Failed!) (run time: None)
Species CC=C[C]=C[C][O][1263] (Failed!) (run time: None)

Overall time since project initiation: 11:11:03
"""
entry(
    index = 0,
    label = "DMF[1]",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {5,D} {7,S}
4  C u0 p0 c0 {2,S} {6,D} {7,S}
5  C u0 p0 c0 {3,D} {6,S} {14,S}
6  C u0 p0 c0 {4,D} {5,S} {15,S}
7  O u0 p2 c0 {3,S} {4,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80382,0.0224121,6.46677e-05,-1.0333e-07,4.45398e-11,-17249.2,9.93999], Tmin=(10,'K'), Tmax=(785.336,'K')),
            NASAPolynomial(coeffs=[1.53417,0.0530933,-3.04551e-05,8.42231e-09,-9.04045e-13,-17482.3,16.5872], Tmin=(785.336,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-143.41,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (357.522,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 8, 'C-O': 2, 'C=C': 2, 'C-C': 3}

External symmetry: 2, optical isomers: 1

Geometry:
O       1.14113000    0.08997200    0.70752300
C       1.09731300    1.46408000   -1.30022000
C       0.97811100   -1.40326000    2.62189300
C       0.51615700    0.36809200   -0.48107600
C       0.46179800   -0.93933500    1.30731200
C      -0.54403200   -0.46712600   -0.64056500
C      -0.57925300   -1.31427900    0.51822500
H       2.13428400    1.24866800   -1.57725600
H       0.51787200    1.59076800   -2.21583200
H       1.09253400    2.41434600   -0.75668400
H       0.96732100   -0.59684100    3.36218400
H       2.00911400   -1.76249400    2.54163100
H       0.35947200   -2.21995500    2.99664800
H      -1.22107000   -0.48105100   -1.48037400
H      -1.28832500   -2.09865400    0.73229300
""",
)

entry(
    index = 1,
    label = "C=CC1=CCCO1[1792]",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {7,S} {10,S} {11,S}
3  C u0 p0 c0 {4,D} {5,S} {7,S}
4  C u0 p0 c0 {1,S} {3,D} {12,S}
5  C u0 p0 c0 {3,S} {6,D} {13,S}
6  C u0 p0 c0 {5,D} {14,S} {15,S}
7  O u0 p2 c0 {2,S} {3,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94589,0.00353554,0.000180523,-3.51515e-07,2.23718e-10,-5581.95,12.2471], Tmin=(10,'K'), Tmax=(403.186,'K')),
            NASAPolynomial(coeffs=[-2.03338,0.0627802,-3.96077e-05,1.20065e-08,-1.39948e-12,-5099.18,35.6699], Tmin=(403.186,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-46.4199,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (357.522,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 8, 'C-O': 2, 'C=C': 2, 'C-C': 3}

External symmetry: 1, optical isomers: 2

Geometry:
O      -0.06601800   -0.38340400    0.97180700
C      -1.92740100    0.33285100   -0.36257400
C      -1.50662200   -0.50824000    0.86340800
C       0.38526900    0.12342800   -0.22290400
C      -0.59595200    0.52342600   -1.04629600
C       1.82239400    0.17262100   -0.42096400
C       2.72115300   -0.25577600    0.46947200
H      -2.66490900   -0.19111600   -0.97736900
H      -2.37316300    1.29359400   -0.07387200
H      -1.94011600   -0.17267300    1.80546000
H      -1.73888300   -1.56839800    0.72067300
H      -0.45073800    0.97114500   -2.01765300
H       2.14231700    0.59711500   -1.36750700
H       3.78396000   -0.19044900    0.27051800
H       2.41096900   -0.67935900    1.41666000
""",
)

entry(
    index = 2,
    label = "CC1[CH]CC=C1[O][1513]",
    molecule = 
"""
multiplicity 3
1  O u1 p2 c0 {6,S}
2  C u0 p0 c0 {4,S} {5,S} {6,S} {8,S}
3  C u0 p0 c0 {5,S} {7,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
5  C u1 p0 c0 {2,S} {3,S} {14,S}
6  C u0 p0 c0 {1,S} {2,S} {7,D}
7  C u0 p0 c0 {3,S} {6,D} {15,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79009,0.0193497,9.98544e-05,-1.78638e-07,9.18228e-11,13038.1,12.7702], Tmin=(10,'K'), Tmax=(635.866,'K')),
            NASAPolynomial(coeffs=[0.859027,0.0570763,-3.46434e-05,1.00801e-08,-1.13023e-12,13021,22.5176], Tmin=(635.866,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (108.375,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (357.522,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 8, 'C-O': 1, 'C=C': 1, 'C-C': 5}

External symmetry: 1, optical isomers: 2

Geometry:
O      -0.44390300    1.51121700   -1.84021000
C      -0.66057700    0.34078700    0.31553600
C       1.74008400   -0.32317400    0.37244500
C      -1.93933900   -0.43366000   -0.05357600
C       0.39573300   -0.43592300    1.03505100
C       0.07868300    0.87316400   -0.93132200
C       1.46302700    0.48352500   -0.84787600
H      -0.97162400    1.22273600    0.90162100
H       2.18854800   -1.30199600    0.12642900
H       2.49957900    0.16227100    1.01432100
H      -2.48867200   -0.73116800    0.84297600
H      -1.69814300   -1.33576000   -0.62192500
H      -2.58580300    0.19758300   -0.66705200
H       0.22967000   -0.98025400    1.95548400
H       2.19254800    0.75102800   -1.60221900
""",
)

entry(
    index = 3,
    label = "CC1CC=CC1=O[1669]",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {6,S} {13,D}
5  C u0 p0 c0 {2,S} {6,D} {14,S}
6  C u0 p0 c0 {4,S} {5,D} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94455,0.00358874,0.000177346,-3.42023e-07,2.15501e-10,-17067.9,12.1329], Tmin=(10,'K'), Tmax=(408.258,'K')),
            NASAPolynomial(coeffs=[-2.05607,0.06244,-3.90982e-05,1.17732e-08,-1.36514e-12,-16578.4,35.7007], Tmin=(408.258,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-141.922,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (357.522,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 8, 'C=O': 1, 'C=C': 1, 'C-C': 5}

External symmetry: 1, optical isomers: 2

Geometry:
O       0.22605800    2.34426400   -0.60752600
C      -0.51323600    0.01099000   -0.48265900
C       0.25964900   -1.20412700    0.07594100
C      -1.84813100    0.32659700    0.19458300
C       0.48257500    1.18459200   -0.37289700
C       1.65414900   -0.68393700    0.32121500
C       1.77836300    0.62514000    0.07468500
H      -0.68860100   -0.12959400   -1.55579800
H       0.26795700   -2.05833100   -0.60932800
H      -0.17889000   -1.56947900    1.01254700
H      -1.72252100    0.43142800    1.27651800
H      -2.24489300    1.26833000   -0.18966600
H      -2.58281500   -0.46206100    0.01303900
H       2.45211600   -1.32770000    0.67521000
H       2.66659100    1.23142500    0.19376100
""",
)

entry(
    index = 4,
    label = "C=C1C=CCCO1[2159]",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {7,S} {10,S} {11,S}
3  C u0 p0 c0 {5,S} {6,D} {7,S}
4  C u0 p0 c0 {1,S} {5,D} {12,S}
5  C u0 p0 c0 {3,S} {4,D} {13,S}
6  C u0 p0 c0 {3,D} {14,S} {15,S}
7  O u0 p2 c0 {2,S} {3,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94415,0.00336281,0.000162332,-2.84801e-07,1.6085e-10,-7035.1,11.1092], Tmin=(10,'K'), Tmax=(457.78,'K')),
            NASAPolynomial(coeffs=[-3.25125,0.0660989,-4.27892e-05,1.32681e-08,-1.57552e-12,-6374.89,40.2162], Tmin=(457.78,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-58.5152,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (357.522,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 8, 'C-O': 2, 'C=C': 2, 'C-C': 3}

External symmetry: 1, optical isomers: 2

Geometry:
O       0.37655100   -1.27592700   -0.09872400
C      -1.66246700   -0.02259700    0.43320300
C      -1.00099900   -1.07825300   -0.44672700
C       1.16175700   -0.14899200   -0.09956700
C      -0.79984600    1.20900100    0.46263500
C       0.50573700    1.12789500    0.17999500
C       2.48253200   -0.27847900   -0.28578900
H      -1.81022300   -0.41012300    1.44952800
H      -2.65825900    0.20712800    0.03829400
H      -1.46689200   -2.05711000   -0.33366500
H      -1.06669300   -0.77895500   -1.50040800
H      -1.25201500    2.16211000    0.71602700
H       1.13785200    2.00852000    0.17834500
H       3.13063500    0.58414800   -0.21777500
H       2.92232900   -1.24836600   -0.47537300
""",
)

entry(
    index = 5,
    label = "C=C[O]C=C=CC[1344]",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {4,S} {5,D} {7,S}
3  C u0 p0 c0 {1,S} {6,D} {11,S}
4  C u0 p0 c0 {2,S} {6,D} {12,S}
5  C u0 p0 c0 {2,D} {13,S} {14,S}
6  C u0 p0 c0 {3,D} {4,D}
7  O u0 p2 c0 {2,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68816,0.0294673,0.000118213,-3.99762e-07,4.14814e-10,2262.17,12.2165], Tmin=(10,'K'), Tmax=(246.099,'K')),
            NASAPolynomial(coeffs=[2.16254,0.0542641,-3.29253e-05,9.65983e-09,-1.09508e-12,2337.26,17.4378], Tmin=(246.099,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (18.82,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (357.522,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 7, 'C-O': 1, 'C=C': 3, 'C-C': 2, 'H-O': 1}

External symmetry: 1, optical isomers: 2

Geometry:
O      -3.79961800    2.23722400    2.85988900
C      -2.14830100    4.29156900   -0.81389600
C      -5.01169500    2.30728000    2.23707000
C      -2.81707100    2.95844500   -0.58061500
C      -5.01394200    2.58599200    0.79349700
C      -6.14070800    2.12726100    2.93470400
C      -3.92141200    2.77459200    0.09119700
H      -1.11871400    4.27784300   -0.44240800
H      -2.68706700    5.09967500   -0.31834100
H      -2.10042500    4.51117100   -1.88534600
H      -2.33769300    2.08900800   -1.03216300
H      -5.98599100    2.62963300    0.31022000
H      -7.10108000    2.18509500    2.44299500
H      -6.10961500    1.92248100    3.99613100
H      -3.10742500    2.37511200    2.20098500
""",
)

entry(
    index = 6,
    label = "CC1=COC[C]=C1[1313]",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {6,D}
4  C u0 p0 c0 {2,S} {5,D} {7,S}
5  C u0 p0 c0 {3,S} {4,D} {14,S}
6  C u0 p0 c0 {3,D} {7,S} {15,S}
7  O u0 p2 c0 {4,S} {6,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7997,0.0239315,5.69427e-05,-9.08109e-08,3.80267e-11,-15999.6,10.6694], Tmin=(10,'K'), Tmax=(819.451,'K')),
            NASAPolynomial(coeffs=[1.99678,0.0519276,-2.94412e-05,8.05295e-09,-8.55991e-13,-16348.6,15.076], Tmin=(819.451,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-133.012,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (357.522,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 8, 'C-O': 2, 'C=C': 2, 'C-C': 3}

External symmetry: 1, optical isomers: 1

Geometry:
O      -0.75573100   -0.79730700   -1.10790900
C       2.49699700    0.30433900    0.27169400
C      -2.59348700   -0.50390400    0.45433700
C       1.07842800   -0.06267900   -0.03994400
C      -1.14712500   -0.37982500    0.13251200
C      -0.06722100    0.07648600    0.82211100
C       0.59549500   -0.59646300   -1.19141300
H      -2.92598500   -1.54498400    0.39398200
H      -3.20649900    0.07829300   -0.24086600
H      -2.78320100   -0.14125100    1.46545200
H       2.59118300    1.36984500    0.50388900
H       2.87122800   -0.25072500    1.13768600
H       3.15569500    0.08808800   -0.57229200
H      -0.07605000    0.46837000    1.82803700
H       1.05579400   -0.88120600   -2.12287300
""",
)

entry(
    index = 7,
    label = "C=C=CC1CCO1[2195]",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {7,D} {13,S}
5  C u0 p0 c0 {7,D} {14,S} {15,S}
6  O u0 p2 c0 {1,S} {3,S}
7  C u0 p0 c0 {4,D} {5,D}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87948,0.0252485,4.75773e-05,-7.27787e-08,2.79527e-11,12444.5,11.8376], Tmin=(10,'K'), Tmax=(927.142,'K')),
            NASAPolynomial(coeffs=[3.88991,0.0480599,-2.63075e-05,6.93851e-09,-7.1254e-13,11460.2,6.49032], Tmin=(927.142,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (103.535,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (357.522,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 8, 'C-O': 2, 'C=C': 2, 'C-C': 3}

External symmetry: 1, optical isomers: 2

Geometry:
O      -2.08176500   -0.96513900   -0.32104400
C      -0.65331700   -0.75416600   -0.51942100
C      -0.82776100    0.77263400   -0.31464000
C      -2.33330400    0.46035900   -0.26988800
C       0.17792000   -1.50457600    0.47724400
C       2.14735000   -3.08185100   -0.18240400
C       1.16494900   -2.29556600    0.15407300
H      -0.41307200    1.13989300    0.62476900
H      -0.48109000    1.40113800   -1.13475300
H      -0.35835700   -1.03070800   -1.53662100
H      -2.90379800    0.80124000   -1.14068000
H      -2.86484000    0.74474900    0.64259000
H      -0.08038100   -1.36136600    1.52509100
H       1.98581400   -4.14055300   -0.36197000
H       3.16099900   -2.70810100   -0.29168200
""",
)

