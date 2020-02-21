#!/usr/bin/env python
# encoding: utf-8

name = "surfaceThermoNi"
shortDesc = u""
longDesc = u"""
A few surface species.
"""


entry(
    index = 1,
    label = "*",
    molecule = 
"""
1 X u0 p0 c0
""",
#    thermo = ThermoData(
#        Tdata = ([300,400,500,600,800,1000,1500],'K'),
#        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
#        H298 = (0,'kcal/mol'),
#        S298 = (0,'cal/(mol*K)'),
#    ),
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.0,0,0,0,0,0.0,0.0], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.0,0,0,0,0,0.0,0.0], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = u"""library value for a vacant surface site""",
    longDesc = u"""Zeros, by definition.""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 2,
    label = "H*",
    molecule =  
"""
1 H u0 p0 {2,S}
2 X u0 p0 {1,S}
""",
#    thermo = ThermoData(
#        Tdata = ([300,400,500,600,800,1000,1500],'K'),
#        Cpdata = ([1.50, 2.58, 3.40, 4.00, 4.73, 5.13, 5.57],'cal/(mol*K)'),
#        H298 = (-11.26,'kcal/mol','+|-',0.1),
#        S298 = (0.44,'cal/(mol*K)','+|-',0.1),
#    ),
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.01510910E+00, 1.27747196E-02,-1.36892852E-05, 6.67076880E-09,-1.15946694E-12,-5.53052906E+03, 8.44686890E+00], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[-1.84968995E-01, 6.05229805E-03,-4.83715532E-06, 1.81340221E-09,-2.61948776E-13,-5.91533033E+03,-5.04191778E-01], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = u"""H atom adsorbed on nickel""",
    longDesc =  u"""Estimated via CFG-TiC""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 3,
    label = "C*",
    molecule =  
"""
1 C u0 p0 {2,Q}
2 X u0 p0 {1,Q}
""", 
#    thermo = ThermoData(
#        Tdata = ([300,400,500,600,800,1000,1500],'K'),
#        Cpdata = ([4.04, 4.73, 5.12, 5.35, 5.60, 5.73, 5.85],'cal/(mol*K)'),
#        H298 = (29.89,'kcal/mol','+|-',0.1),
#        S298 = (2.62,'cal/(mol*K)','+|-',0.1),
#    ),
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.73265619E-01,  1.44803183E-02, -2.45704673E-05,  1.93668551E-08, -5.81642502E-12,  1.47661073E+04,  1.20244250E+00], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[ 2.71617577E+00,  1.99967762E-05,  3.48031630E-07, -2.47205634E-10,  5.00169813E-14,  1.41308872E+04, -1.44477318E+01], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = u"""C atom adsorbed on nickel""",
    longDesc =  u"""Estimated via CFG-TiC.
    Unsure of adjacency list: Do we want a lone pair and triple bond?!""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 4,
    label = "O*",
    molecule =  
"""
1 O u0 p2 {2,D}
2 X u0 p0 {1,D}
""",
#    thermo = ThermoData(
#        Tdata = ([300,400,500,600,800,1000,1500],'K'),
#        Cpdata = ([4.52, 5.06, 5.35, 5.52, 5.70, 5.79, 5.88],'cal/(mol*K)'),
#        H298 = (-52.58,'kcal/mol','+|-',0.1),
#        S298 = (3.61,'cal/(mol*K)','+|-',0.1),
#    ),
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[ 1.95855852E-01,  1.16923252E-02, -2.02271203E-05,  1.61601691E-08, -4.90070914E-12, -2.69189243E+04, -2.01768707E+00], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[ 2.90438370E+00, -2.74871763E-04,  5.38558858E-07, -3.03946989E-10,  5.63969783E-14, -2.74411389E+04, -1.48944150E+01], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = u"""O atom adsorbed on nickel""",
    longDesc =  u"""Estimated via CFG-TiC""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 5,
    label = "H2*",
    molecule =  
"""
1 H u0 p0 {2,S} {3,vdW}
2 H u0 p0 {1,S}
3 X u0 p0 {1,vdW}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[ 3.69073030E+00,  1.56595045E-03, -3.19654406E-06,  2.88277763E-09, -8.73556269E-13, -2.15972248E+03, -1.15931806E+01], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[ 4.49468701E+00, -1.73352628E-03,  1.97119900E-06, -7.70127035E-10,  1.07125350E-13, -2.31943201E+03, -1.54586471E+01], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = u"""H2 physisorbed on nickel""",
    longDesc =  u"""Estimated via CFG-TiC""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 6,
    label = "CH*",
    molecule =  
"""
1 C u0 p0 {2,S} {3,T}
2 H u0 p0 {1,S}
3 X u0 p0 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[ 4.44067538E-01,  7.15965809E-03, -6.05381899E-06,  4.41670377E-09, -1.57758787E-12,  2.48409325E+03, -2.97930741E+00], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[ 4.70984781E-01,  6.44724983E-03, -3.18677769E-06,  7.11925015E-10, -5.43593812E-14,  2.47924869E+03, -3.03223839E+00], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = u"""CH adsorbed on nickel""",
    longDesc =  u"""Estimated via CFG-TiC""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 7,
    label = "CH2*",
    molecule =  
"""
1 C u0 p0 {2,S} {3,S} {4,D}
2 H u0 p0 {1,S}
3 H u0 p0 {1,S}
4 X u0 p0 {1,D}
""",
#    thermo = ThermoData(
#        Tdata = ([300,400,500,600,800,1000,1500],'K'),
#        Cpdata = ([5.82, 7.37, 8.64, 9.69, 11.35, 12.64, 14.74],'cal/(mol*K)'),
#        H298 = (4.11,'kcal/mol','+|-',0.1),
#        S298 = (4.28,'cal/(mol*K)','+|-',0.1),
#    ),
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-7.19249342E-01, 1.65071735E-02,-1.74998510E-05, 1.09676908E-08,-2.88981251E-12, 1.68411050E+03, 2.01831094E+00  ], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.83780574E-01, 8.78623452E-03,-4.38766259E-06, 1.09400822E-09,-1.10409266E-13,1.38336061E+03,-5.98458146E+00], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = u"""CH2 adsorbed on nickel""",
    longDesc =  u"""Estimated via CFG-TiC""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 8,
    label = "CH3*",
    molecule = 
"""
1 C u0 p0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 {1,S}
3 H u0 p0 {1,S}
4 H u0 p0 {1,S}
5 X u0 p0 {1,S}
""",
#    thermo = ThermoData(
#        Tdata = ([300,400,500,600,800,1000,1500],'K'),
#        Cpdata = ([9.57,11.53,13.02,14.19,16.03,17.47,19.94],'cal/(mol*K)'),
#        H298 = (-7.32,'kcal/mol','+|-',0.1),
#        S298 = (8.06,'cal/(mol*K)','+|-',0.1),
#    ),
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.52219087E-01, 2.64420133E-02,-3.55617257E-05, 2.60043628E-08,-7.52706787E-12,-4.43346585E+03, 6.92144274E-01  ], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[ 3.62557353E+00, 7.39511955E-03,-2.43797398E-06, 1.86159414E-10, 3.64849549E-14,-5.18722188E+03,-1.89668272E+01], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = u"""Methyl adsorbed on nickle""",
    longDesc = u"""Estimated via CFG-TiC""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 9,
    label = "CH4*",
    molecule =  
"""
1 C u0 p0 {2,S} {3,S} {4,S} {5,S} {6,vdW}
2 H u0 p0 {1,S}
3 H u0 p0 {1,S}
4 H u0 p0 {1,S}
5 H u0 p0 {1,S}
6 X u0 p0 {1,vdW}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[ 3.32887778E+00, -5.00781929E-03,  2.79052442E-05, -2.68118150E-08,  8.62124183E-12, -9.68331332E+03, -5.81051526E+00], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[-1.60598709E+00,  1.64084653E-02, -9.05813323E-06,  2.60602815E-09, -3.14643586E-13, -8.70274862E+03,  1.77717514E+01], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = u"""CH4 physisorbed on nickel""",
    longDesc =  u"""Estimated via CFG-TiC""",
    metal = "Ni",
    facet = "111",
)


entry(
    index = 10,
    label = "OH*",
    molecule =  
"""
1 O u0 p2 {2,S} {3,S}
2 H u0 p0 {1,S}
3 X u0 p0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[ 1.58477686E+00,  3.87867982E-03,  1.34107764E-06, -3.93949585E-09,  1.68540254E-12, -2.90977259E+04, -7.42452379E+00], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[ 1.42377797E+00,  5.57119676E-03, -3.39293380E-06,  1.09513419E-09, -1.46734126E-13, -2.90972119E+04, -6.85806991E+00], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = u"""OH adsorbed on nickel""",
    longDesc =  u"""Estimated via CFG-TiC""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 11,
    label = "H2O*",
    molecule =  
"""
1 O u0 p2 {2,S} {3,S} {4,vdW}
2 H u0 p0 {1,S}
3 H u0 p0 {1,S}
4 X u0 p0 {1,vdW}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[ 4.57850728E+00,  5.24431866E-03, -6.83196649E-06,  5.61222436E-09, -1.73417281E-12, -3.35165877E+04, -1.70841839E+01], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[ 5.76070198E+00,  3.01863620E-05,  1.95429732E-06, -1.04677380E-09,  1.70499154E-13, -3.37366557E+04, -2.26859971E+01], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = u"""H2O physisorbed on nickel""",
    longDesc =  u"""Estimated via CFG-TiC""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 12,
    label = "CO*",
    molecule =  
"""
1 C u0 p0 {2,D} {3,D}
2 O u0 p2 {1,D} 
3 X u0 p0 {1,D} 
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[ 3.13851368E+00,  7.37719433E-03, -1.21673211E-05,  1.06231734E-08, -3.55085256E-12, -3.01011015E+04, -1.40684039E+01], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[ 4.39015575E+00,  1.21423223E-03,  2.26543548E-08, -2.74772156E-10,  6.84375847E-14, -3.03339593E+04, -1.99186406E+01], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = u"""CO adsorbed on nickel (?)""",
    longDesc =  u"""Estimated via CFG-TiC
    Unsure of adjacency list.""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 13,
    label = "HCO*",
    molecule =  
"""
1 C u0 p0 {2,D} {3,S} {4,S}
2 O u0 p2 {1,D}
3 H u0 p0 {1,S}
4 X u0 p0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[ 1.67902911E+00,  1.39424587E-02, -1.51013698E-05,  9.67718274E-09, -2.69733533E-12, -2.16030349E+04, -8.23427981E+00], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[ 3.03186697E+00,  8.02892147E-03, -4.79702422E-06,  1.39761897E-09, -1.61417712E-13, -2.18711786E+04, -1.46921130E+01], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = u"""HCO di-sigma adsorbed on nickel. PREVIOUSLY WAS DI-SIGMA. I'VE CHANGED IT.""",
    longDesc =  u"""Estimated via CFG-TiC
H--C--O
   || |
***********
""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 14,
    label = "COH*",
    molecule =  
"""
1 C u0 p0 {2,S} {4,T}
2 O u0 p2 {1,S} {3,S}
3 H u0 p0 {2,S}
4 X u0 p0 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[ 1.57671035E+00,  1.40109542E-02, -1.49135569E-05,  9.39835302E-09, -2.59115734E-12, -2.39932633E+04, -7.86764175E+00], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[ 2.90364615E+00,  8.26442693E-03, -4.98148751E-06,  1.46592732E-09, -1.71209513E-13, -2.42585084E+04, -1.42141420E+01], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = u"""COH adsorbed on nickel""",
    longDesc =  u"""Estimated via CFG-TiC""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 15,
    label = "CH2O*",
    molecule =  
"""
1 C u0 p0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 {1,S} {6,S}
3 H u0 p0 {1,S}
4 H u0 p0 {1,S}
5 X u0 p0 {1,S}
6 X u0 p0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.25242157E-01,  1.54111015E-02, -5.43318168E-06, -2.53324638E-09,  1.74558573E-12, -2.15271737E+04, -2.17550678E-01], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[-4.92586490E-01,  1.77560911E-02, -1.15522673E-05,  3.73955554E-09, -4.85775848E-13, -2.15145571E+04,  8.10658192E-01], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = u"""CH2O di-sigma adsorbed on nickel.""",
    longDesc =  u"""Estimated via CFG-TiC. Adjacency list changed by Richard to use two surface sites.""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 16,
    label = "CHOH*",
    molecule =  
"""
1 C u0 p0 {2,S} {3,S} {5,D}
2 O u0 p2 {1,S} {4,S}
3 H u0 p0 {1,S}
4 H u0 p0 {2,S}
5 X u0 p0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[ 4.61466774E+00,  1.97736658E-03,  1.13520606E-05, -1.28686112E-08,  4.28854240E-12, -2.08405084E+04, -1.83405542E+01], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[ 2.12897595E+00,  1.31031973E-02, -8.04327296E-06,  2.48752777E-09, -3.12401921E-13, -2.03714667E+04, -6.56664446E+00], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = u"""CHOH adsorbed on nickel""",
    longDesc =  u"""Estimated via CFG-TiC""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 17,
    label = "CH3O*",
    molecule =  
"""
1 O u0 p2 {2,S} {6,S}
2 C u0 p0 {1,S} {3,S} {4,S} {5,S}
3 H u0 p0 {2,S}
4 H u0 p0 {2,S}
5 H u0 p0 {2,S}
6 X u0 p0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[ 7.53085334E-01,  2.34767303E-02, -2.14198542E-05,  1.12397159E-08, -2.54634600E-12, -2.90522738E+04, -4.44446697E+00], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[ 2.56333702E+00,  1.57779773E-02, -9.23295028E-06,  2.72123962E-09, -3.26272331E-13, -2.93898460E+04, -1.30594679E+01], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = u"""CH3O adsorbed on nickel""",
    longDesc =  u"""Estimated via CFG-TiC""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 18,
    label = "CH2OH*",
    molecule =  
"""
1 C u0 p0 {2,S} {3,S} {4,S} {6,S}
2 H u0 p0 {1,S}
3 H u0 p0 {1,S}
4 O u0 p2 {1,S} {5,S}
5 H u0 p0 {4,S}
6 X u0 p0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[ 1.72324170E+00,  2.46490814E-02, -2.80859624E-05,  1.72678472E-08, -4.26645223E-12, -2.48262518E+04, -8.86801544E+00], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[ 5.35800551E+00,  9.63360342E-03, -4.83501645E-06,  1.27341188E-09, -1.42248592E-13, -2.55298238E+04, -2.62856418E+01], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = u"""CH2OH adsorbed on nickel""",
    longDesc =  u"""Estimated via CFG-TiC""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 19,
    label = "CH3OH*",
    molecule =  
"""
1 O u0 p2 {2,S} {3,S} {7,vdW}
2 C u0 p0 {1,S} {4,S} {5,S} {6,S}
3 H u0 p0 {1,S}
4 H u0 p0 {2,S}
5 H u0 p0 {2,S}
6 H u0 p0 {2,S}
7 X u0 p0 {1,vdW}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[ 5.13156551E+00,  2.38019419E-03,  2.17569785E-05, -2.56954742E-08,  9.11028845E-12, -3.25405443E+04, -1.86648447E+01], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[ 1.37902838E+00,  2.02943524E-02, -1.24520299E-05,  3.99094219E-09, -5.28740583E-13, -3.18358817E+04, -1.03860539E+00], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = u"""CH3OH physisorbed on nickel""",
    longDesc =  u"""Estimated via CFG-TiC""",
    metal = "Ni",
    facet = "111",
)


entry(
    index = 20,
    label = "CO2*",
    molecule =  
"""
1 C u0 p0 {2,D} {3,D} {4,vdW}
2 O u0 p2 {1,D}
3 O u0 p2 {1,D}
4 X u0 p0 {1,vdW}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[ 2.24139903E+00,  1.23292022E-02, -1.44097226E-05,  9.43642793E-09, -2.60737252E-12, -4.96482688E+04,  1.76120609E+00], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[ 3.71448250E+00,  6.02066374E-03, -3.73960975E-06,  1.12938233E-09, -1.34984787E-13, -4.99415034E+04, -5.29009370E+00], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = u"""CO2 physisorbed on nickel""",
    longDesc =  u"""Estimated via CFG-TiC""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 21,
    label = "HOCO*",
    molecule =  
"""
1 C u0 p0 {2,D} {3,S} {5,S}
2 O u0 p2 {1,D}
3 O u0 p2 {1,S} {4,S}
4 H u0 p0 {3,S}
5 X u0 p0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[ 7.00750147E-01,  3.22756606E-02, -4.70618414E-05,  3.45557357E-08, -1.00331658E-11, -5.18553737E+04, -4.52637913E+00], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[ 6.47849692E+00,  7.14986800E-03, -4.22981914E-06,  1.15767979E-09, -1.19086295E-13, -5.29808669E+04, -3.20736929E+01], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = u"""HOCO adsorbed on nickel""",
    longDesc =  u"""Estimated via CFG-TiC""",
    metal = "Ni",
    facet = "111",
)


