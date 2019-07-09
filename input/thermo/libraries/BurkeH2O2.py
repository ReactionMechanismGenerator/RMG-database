#!/usr/bin/env python
# encoding: utf-8

name = "BurkeH2O2"
shortDesc = u"Library for H2 combustion by Burke et al."
longDesc = u"""
Comprehensive H2/O2 kinetic model for high-pressure combustion
M.P. Burke, M. Chaos, Y. Ju, F.L. Dryer, S.J. Klippenstein
International Journal of Chemical Kinetics
Volume 44, Issue 7, pages 444-474, July 2012
DOI: 10.1002/kin.20603
"""
entry(
    index = 0,
    label = "H",
    molecule = 
"""
multiplicity 2
1 H u1 p0 c0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.97,4.97,4.97,4.97,4.97,4.97,4.97],'cal/(mol*K)'),
        H298 = (52.1,'kcal/mol'),
        S298 = (27.39,'cal/(mol*K)'),
    ),
    shortDesc = u"""Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.""",
    longDesc = 
u"""
H                120186 H  1                G   298.00   5000.00  1000.00      1
 0.02500000E+02 0.00000000E+00 0.00000000E+00 0.00000000E+00 0.00000000E+00    2
 0.02547163E+06-0.04601176E+01 0.02500000E+02 0.00000000E+00 0.00000000E+00    3
 0.00000000E+00 0.00000000E+00 0.02547163E+06-0.04601176E+01                   4
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.9,6.96,7,7.02,7.07,7.21,7.73],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (31.21,'cal/(mol*K)'),
    ),
    shortDesc = u"""Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.""",
    longDesc = 
u"""
H2               121286 H  2                G   298.00   5000.00  1000.00      1
 0.02991423E+02 0.07000644E-02-0.05633829E-06-0.09231578E-10 0.01582752E-13    2
-0.08350340E+04-0.01355110E+02 0.03298124E+02 0.08249442E-02-0.08143015E-05    3
-0.09475434E-09 0.04134872E-11-0.01012521E+05-0.03294094E+02                   4
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.23,5.14,5.08,5.05,5.02,5,4.98],'cal/(mol*K)'),
        H298 = (59.56,'kcal/mol'),
        S298 = (38.46,'cal/(mol*K)'),
    ),
    shortDesc = u"""Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.""",
    longDesc = 
u"""
O                120186 O  1                G   298.00   5000.00  1000.00      1
 0.02542060E+02-0.02755062E-03-0.03102803E-07 0.04551067E-10-0.04368052E-14    2
 0.02923080E+06 0.04920308E+02 0.02946429E+02-0.01638166E-01 0.02421032E-04    3
-0.01602843E-07 0.03890696E-11 0.02914764E+06 0.02963995E+02                   4
""",
)

entry(
    index = 3,
    label = "OH",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.16,7.08,7.05,7.06,7.15,7.34,7.87],'cal/(mol*K)'),
        H298 = (8.9,'kcal/mol'),
        S298 = (43.9,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
OH               S 9/01 O   1H   1          G   200.000  6000.000 1000.00      1
 2.86472886E+00 1.05650448E-03-2.59082758E-07 3.05218674E-11-1.33195876E-15    2
 3.68362875E+03 5.70164073E+00 4.12530561E+00-3.22544939E-03 6.52764691E-06    3
-5.79853643E-09 2.06237379E-12 3.34630913E+03-6.90432960E-01 4.51532273E+03    4
""",
)

entry(
    index = 4,
    label = "H2O",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8,8.23,8.45,8.67,9.22,9.87,11.26],'cal/(mol*K)'),
        H298 = (-57.8,'kcal/mol'),
        S298 = (45.1,'cal/(mol*K)'),
    ),
    shortDesc = u"""Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.""",
    longDesc = 
u"""
H2O              20387  H   2O   1          G   298.00   5000.00  1000.00      1
 0.02672146E+02 0.03056293E-01-0.08730260E-05 0.01200996E-08-0.06391618E-13    2
-0.02989921E+06 0.06862817E+02 0.03386842E+02 0.03474982E-01-0.06354696E-04    3
 0.06968581E-07-0.02506588E-10-0.03020811E+06 0.02590233E+02                   4
""",
)

entry(
    index = 5,
    label = "O2",
    molecule = 
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.01,7.22,7.44,7.66,8.07,8.35,8.72],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (49,'cal/(mol*K)'),
    ),
    shortDesc = u"""Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.""",
    longDesc = 
u"""
O2               121386 O  2                G   298.00   5000.00  1000.00      1
 0.03697578E+02 0.06135197E-02-0.01258842E-05 0.01775281E-09-0.01136435E-13    2
-0.01233930E+05 0.03189166E+02 0.03212936E+02 0.01127486E-01-0.05756150E-05    3
 0.01313877E-07-0.08768554E-11-0.01005249E+05 0.06034738E+02                   4
""",
)

entry(
    index = 6,
    label = "HO2",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.35,8.89,9.47,10,10.77,11.38,12.48],'cal/(mol*K)'),
        H298 = (3,'kcal/mol'),
        S298 = (54.75,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
HO2              L 5/89 H   1O   2          G   200.000  3500.000  1000.000    1
 4.01721090E+00 2.23982013E-03-6.33658150E-07 1.14246370E-10-1.07908535E-14    2
 1.11856713E+02 3.78510215E+00 4.30179801E+00-4.74912051E-03 2.11582891E-05    3
-2.42763894E-08 9.29225124E-12 2.94808040E+02 3.71666245E+00 1.00021620E+04    4
""",
)

entry(
    index = 7,
    label = "H2O2",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.42,11.45,12.35,13.11,14.29,15.21,16.85],'cal/(mol*K)'),
        H298 = (-32.53,'kcal/mol'),
        S298 = (55.65,'cal/(mol*K)'),
    ),
    shortDesc = u"""Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.""",
    longDesc = 
u"""
H2O2             120186 H   2O   2          G   298.00   5000.00  1000.00      1
 0.04573167E+02 0.04336136E-01-0.01474689E-04 0.02348904E-08-0.01431654E-12    2
-0.01800696E+06 0.05011370E+01 0.03388754E+02 0.06569226E-01-0.01485013E-05    3
-0.04625806E-07 0.02471515E-10-0.01766315E+06 0.06785363E+02                   4
""",
)

entry(
    index = 8,
    label = "CO",
    molecule = 
"""
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.95,7.03,7.14,7.27,7.61,7.95,8.41],'cal/(mol*K)'),
        H298 = (-26.42,'kcal/mol'),
        S298 = (47.21,'cal/(mol*K)'),
    ),
    shortDesc = u"""Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.""",
    longDesc = 
u"""
CO               121286 C   1O   1          G   298.00   5000.00  1000.00      1
 0.03025078E+02 0.01442689E-01-0.05630828E-05 0.01018581E-08-0.06910952E-13    2
-0.01426835E+06 0.06108218E+02 0.03262452E+02 0.01511941E-01-0.03881755E-04    3
 0.05581944E-07-0.02474951E-10-0.01431054E+06 0.04848897E+02                   4
""",
)

entry(
    index = 9,
    label = "CO2",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,D}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.91,9.87,10.65,11.31,12.32,12.99,13.93],'cal/(mol*K)'),
        H298 = (-94.06,'kcal/mol'),
        S298 = (51.08,'cal/(mol*K)'),
    ),
    shortDesc = u"""Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.""",
    longDesc = 
u"""
CO2              121286 C   1O   2          G   298.00   5000.00  1000.00      1
 0.04453623E+02 0.03140169E-01-0.01278411E-04 0.02393997E-08-0.01669033E-12    2
-0.04896696E+06-0.09553959E+01 0.02275725E+02 0.09922072E-01-0.01040911E-03    3
 0.06866687E-07-0.02117280E-10-0.04837314E+06 0.01018849E+03                   4
""",
)

entry(
    index = 10,
    label = "N2",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 N u0 p1 c0 {1,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.95,7.01,7.08,7.19,7.5,7.83,8.32],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (45.77,'cal/(mol*K)'),
    ),
    shortDesc = u"""Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.""",
    longDesc = 
u"""
N2               121286 N  2                G   298.00   5000.00  1000.00      1
 0.02926640E+02 0.01487977E-01-0.05684761E-05 0.01009704E-08-0.06753351E-13    2
-0.09227977E+04 0.05980528E+02 0.03298677E+02 0.01408240E-01-0.03963222E-04    3
 0.05641515E-07-0.02444855E-10-0.01020900E+05 0.03950372E+02                   4
""",
)

entry(
    index = 11,
    label = "Ar",
    molecule = 
"""
1 Ar u0 p4 c0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.97,4.97,4.97,4.97,4.97,4.97,4.97],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (36.98,'cal/(mol*K)'),
    ),
    shortDesc = u"""Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.""",
    longDesc = 
u"""
Ar               120186 Ar  1               G   298.00   5000.00  1000.00      1
 0.02500000E+02 0.00000000E+00 0.00000000E+00 0.00000000E+00 0.00000000E+00    2
-0.07453750E+04 0.04366001E+02 0.02500000E+02 0.00000000E+00 0.00000000E+00    3
 0.00000000E+00 0.00000000E+00-0.07453750E+04 0.04366001E+02                   4
""",
)

entry(
    index = 12,
    label = "He",
    molecule = 
"""
1 He u0 p1 c0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.97,4.97,4.97,4.97,4.97,4.97,4.97],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (30.12,'cal/(mol*K)'),
    ),
    shortDesc = u"""Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.""",
    longDesc = 
u"""
He               120186 He  1               G   298.00   5000.00  1000.00      1
 0.02500000E+02 0.00000000E+00 0.00000000E+00 0.00000000E+00 0.00000000E+00    2
-0.07453750E+04 0.09153489E+01 0.02500000E+02 0.00000000E+00 0.00000000E+00    3
 0.00000000E+00 0.00000000E+00-0.07453750E+04 0.09153488E+01                   4
""",
)

