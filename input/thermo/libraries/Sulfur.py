#!/usr/bin/env python
# encoding: utf-8

name = "Sulfur"
shortDesc = "H2S oxidation"
longDesc = """
Written by Esty Ritov,
Based on CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/Def2TZVP computations
with enthalpies from ATcT  v. 1.220 where available.
"""

entry(
    index=1,
    label="S",
    molecule="""
multiplicity 3
1 S u2 p2 c0
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[2.5, -1.5266e-15, 6.3226e-18, -7.59355e-21, 2.67359e-24, 32729.9, 5.13449], Tmin=(10, 'K'), Tmax=(1363.47, 'K')),
        NASAPolynomial(coeffs=[2.5, -1.01797e-13, 8.3758e-17, -2.93808e-20, 3.72101e-24, 32729.9, 5.13449], Tmin=(1363.47, 'K'), Tmax=(3000, 'K'))],
        Tmin=(10, 'K'), Tmax=(3000, 'K'), E0=(272.132, 'kJ/mol'), Cp0=(20.7862, 'J/(mol*K)'), CpInf=(20.7862, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from ATcT: 279.07 kJ/mol
H298 from CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/Def2TZVP:(278.326,'kJ/mol')
S298 and Cp from CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/Def2TZVP computations

ThermoData(
    H298=(279.07,'kJ/mol'),
    S298=(161.111,'J/(mol*K)'),
    Tdata=([300,400,500,600,800,1000,1500,2000,2500,3000],'K'),
    Cpdata=([20.7862,20.7862,20.7862,20.7862,20.7862,20.7862,20.7862,20.7862,20.7862,20.7862],'J/(mol*K)'),
    Cp0=(20.7862,'J/(mol*K)'),
    CpInf=(20.7862,'J/(mol*K)'),
    Tmin=(298,'K'),
    Tmax=(3000,'K'),
)
""",
)

entry(
    index=2,
    label="H2S",
    molecule="""
1 S u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[4.00977, -0.000524204, 2.80302e-06, 6.28655e-10, -1.59871e-12, -3173.84, 1.89989], Tmin=(10, 'K'), Tmax=(724.68, 'K')),
        NASAPolynomial(coeffs=[2.88871, 0.00350411, -1.06503e-06, 7.4813e-11, 1.09913e-14, -2954.65, 7.3386], Tmin=(724.68, 'K'), Tmax=(3000, 'K'))],
        Tmin=(10, 'K'), Tmax=(3000, 'K'), E0=(-26.3849, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(58.2013, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from ATcT: -20.3 kJ/mol
H298 from CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/Def2TZVP:(-16.4376,'kJ/mol')
S298 and Cp from CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/Def2TZVP computations

ThermoData(
    H298=(-20.3 kJ/mol,'kJ/mol'),
    S298=(205.489,'J/(mol*K)'),
    Tdata=([300,400,500,600,800,1000,1500,2000,2500,3000],'K'),
    Cpdata=([34.1625,35.3189,36.8089,38.5204,42.0146,45.0112,50.3582,53.3055,54.7994,55.9233],'J/(mol*K)'),
    Cp0=(33.2579,'J/(mol*K)'),
    CpInf=(58.2013,'J/(mol*K)'),
    Tmin=(298,'K'),
    Tmax=(3000,'K'),
)
""",
)

entry(
    index=3,
    label="S2",
    molecule="""
multiplicity 3
1 S u1 p2 c0 {2,S}
2 S u1 p2 c0 {1,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.49354, 0.000342919, 6.3422e-06, -1.14434e-08, 5.9149e-12, 14475.1, 7.23942], Tmin=(10, 'K'), Tmax=(666.147, 'K')),
        NASAPolynomial(coeffs=[3.45053, 0.00231267, -1.94702e-06, 7.09148e-10, -9.32965e-14, 14442.8, 7.14443], Tmin=(666.147, 'K'), Tmax=(3000, 'K'))],
        Tmin=(10, 'K'), Tmax=(3000, 'K'), E0=(120.35, 'kJ/mol'), Cp0=(29.1007, 'J/(mol*K)'), CpInf=(37.4151, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from high-level computations: 129.436 kJ/mol
S298 and Cp from CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/Def2TZVP computations

ThermoData(
    H298=(129.436,'kJ/mol'),
    S298=(228.124,'J/(mol*K)'),
    Tdata=([300,400,500,600,800,1000,1500,2000,2500,3000],'K'),
    Cpdata=([32.4776,33.7942,34.836,35.5633,36.4128,36.85,37.0809,37.151,37.4099,37.0438],'J/(mol*K)'),
    Cp0=(29.1007,'J/(mol*K)'),
    CpInf=(37.4151,'J/(mol*K)'),
    Tmin=(298,'K'),
    Tmax=(3000,'K'),
)
""",
)

entry(
    index=4,
    label="S3",
    molecule="""
1 S u0 p1 c0 {2,D} {3,D}
2 S u0 p2 c0 {1,D}
3 S u0 p2 c0 {1,D}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.95028, 0.00314874, 2.82863e-05, -7.61637e-08, 5.44601e-11, 16232.4, 8.91127], Tmin=(10, 'K'), Tmax=(523.795, 'K')),
        NASAPolynomial(coeffs=[5.15633, 0.00409251, -3.49397e-06, 1.29394e-09, -1.73115e-13, 15966.7, 2.54307], Tmin=(523.795, 'K'), Tmax=(3000, 'K'))],
        Tmin=(10, 'K'), Tmax=(3000, 'K'), E0=(134.949, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(58.2013, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from high-level computations: 146.953 kJ/mol
S298 and Cp from CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/Def2TZVP computations

ThermoData(
    H298=(146.953,'kJ/mol'),
    S298=(274.762,'J/(mol*K)'),
    Tdata=([300,400,500,600,800,1000,1500,2000,2500,3000],'K'),
    Cpdata=([48.4349,52.0094,53.8738,54.9675,56.4202,57.1678,57.572,57.7619,58.2495,57.3881],'J/(mol*K)'),
    Cp0=(33.2579,'J/(mol*K)'),
    CpInf=(58.2013,'J/(mol*K)'),
    Tmin=(298,'K'),
    Tmax=(3000,'K'),
)
""",
)

entry(
    index=5,
    label="S4",
    molecule="""
1 S u0 p2 c0 {2,S} {4,S}
2 S u0 p2 c0 {1,S} {3,S}
3 S u0 p2 c0 {2,S} {4,S}
4 S u0 p2 c0 {1,S} {3,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.84981, 0.010348, 6.82134e-05, -2.29992e-07, 1.9285e-10, 25456.5, 9.50638], Tmin=(10, 'K'), Tmax=(464.092, 'K')),
        NASAPolynomial(coeffs=[7.53646, 0.00582118, -5.22499e-06, 2.01411e-09, -2.78288e-13, 24820.9, -8.61086], Tmin=(464.092, 'K'), Tmax=(3000, 'K'))],
        Tmin=(10, 'K'), Tmax=(3000, 'K'), E0=(211.638, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(83.1447, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from high-level computations: 227.003 kJ/mol
S298 and Cp from CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/Def2TZVP computations

ThermoData(
    H298=(227.003,'kJ/mol'),
    S298=(298.515,'J/(mol*K)'),
    Tdata=([300,400,500,600,800,1000,1500,2000,2500,3000],'K'),
    Cpdata=([70.2217,75.8332,77.9496,79.3795,81.2045,82.0511,82.3198,82.6386,83.4196,81.6043],'J/(mol*K)'),
    Cp0=(33.2579,'J/(mol*K)'),
    CpInf=(83.1447,'J/(mol*K)'),
    Tmin=(298,'K'),
    Tmax=(3000,'K'),
)
""",
)

entry(
    index=6,
    label="S5",
    molecule="""
1 S u0 p2 c0 {2,S} {5,S}
2 S u0 p2 c0 {1,S} {3,S}
3 S u0 p2 c0 {2,S} {4,S}
4 S u0 p2 c0 {3,S} {5,S}
5 S u0 p2 c0 {1,S} {4,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.71401, 0.0215315, 0.000107387, -4.52447e-07, 4.42395e-10, 13732.7, 12.2961], Tmin=(10, 'K'), Tmax=(408.473, 'K')),
        NASAPolynomial(coeffs=[9.66945, 0.00796889, -7.16333e-06, 2.75341e-09, -3.78861e-13, 12872.8, -15.6738], Tmin=(408.473, 'K'), Tmax=(3000, 'K'))],
        Tmin=(10, 'K'), Tmax=(3000, 'K'), E0=(114.185, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(108.088, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from high-level computations: 133.52 kJ/mol
S298 and Cp from CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/Def2TZVP computations

ThermoData(
    H298=(133.52,'kJ/mol'),
    S298=(345.224,'J/(mol*K)'),
    Tdata=([300,400,500,600,800,1000,1500,2000,2500,3000],'K'),
    Cpdata=([93.1688,98.7529,101.3,103.246,105.715,106.837,107.091,107.418,108.451,106.097],'J/(mol*K)'),
    Cp0=(33.2579,'J/(mol*K)'),
    CpInf=(108.088,'J/(mol*K)'),
    Tmin=(298,'K'),
    Tmax=(3000,'K'),
)
""",
)

entry(
    index=7,
    label="S6",
    molecule="""
1 S u0 p2 c0 {2,S} {6,S}
2 S u0 p2 c0 {1,S} {3,S}
3 S u0 p2 c0 {2,S} {4,S}
4 S u0 p2 c0 {3,S} {5,S}
5 S u0 p2 c0 {4,S} {6,S}
6 S u0 p2 c0 {1,S} {5,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.60842, 0.029716, 0.000144124, -6.22102e-07, 6.1756e-10, 9959.76, 11.1936], Tmin=(10, 'K'), Tmax=(403.677, 'K')),
        NASAPolynomial(coeffs=[11.686, 0.0103424, -9.31284e-06, 3.58537e-09, -4.94071e-13, 8813.32, -26.5708], Tmin=(403.677, 'K'), Tmax=(3000, 'K'))],
        Tmin=(10, 'K'), Tmax=(3000, 'K'), E0=(82.8215, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(133.032, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from high-level computations: 105.508 kJ/mol
S298 and Cp from CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/Def2TZVP computations

ThermoData(
    H298=(105.508,'kJ/mol'),
    S298=(355.325,'J/(mol*K)'),
    Tdata=([300,400,500,600,800,1000,1500,2000,2500,3000],'K'),
    Cpdata=([113.907,120.973,124.27,126.789,129.98,131.426,131.744,132.177,133.518,130.395],'J/(mol*K)'),
    Cp0=(33.2579,'J/(mol*K)'),
    CpInf=(133.032,'J/(mol*K)'),
    Tmin=(298,'K'),
    Tmax=(3000,'K'),
)
""",
)

entry(
    index=8,
    label="S7",
    molecule="""
multiplicity 1
1 S u0 p2 c0 {2,S} {7,S}
2 S u0 p2 c0 {1,S} {3,S}
3 S u0 p2 c0 {2,S} {4,S}
4 S u0 p2 c0 {3,S} {5,S}
5 S u0 p2 c0 {4,S} {6,S}
6 S u0 p2 c0 {5,S} {7,S}
7 S u0 p2 c0 {1,S} {6,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[2.78267, 0.0789636, -0.000148843, 1.23042e-07, -3.73104e-11, 11090.2, 15.7797], Tmin=(10, 'K'), Tmax=(978.549, 'K')),
        NASAPolynomial(coeffs=[13.9263, 0.0101247, -7.62441e-06, 2.51352e-09, -3.04481e-13, 10024.2, -32.0432], Tmin=(978.549, 'K'), Tmax=(3000, 'K'))],
        Tmin=(10, 'K'), Tmax=(3000, 'K'), E0=(91.96, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(157.975, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from high-level computations: 119.21 kJ/mol
S298 and Cp from CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/Def2TZVP computations

ThermoData(
    H298=(119.21,'kJ/mol'),
    S298=(412.122,'J/(mol*K)'),
    Tdata=([300,400,500,600,800,1000,1500,2000,2500,3000],'K'),
    Cpdata=([133.828,145.277,150.509,152.313,153.063,154.945,157.145,157.264,157.688,157],'J/(mol*K)'),
    Cp0=(33.2579,'J/(mol*K)'),
    CpInf=(157.975,'J/(mol*K)'),
    Tmin=(298,'K'),
    Tmax=(3000,'K'),
)
""",
)

entry(
    index=9,
    label="S8",
    molecule="""
multiplicity 1
1 S u0 p2 c0 {2,S} {8,S}
2 S u0 p2 c0 {1,S} {3,S}
3 S u0 p2 c0 {2,S} {4,S}
4 S u0 p2 c0 {3,S} {5,S}
5 S u0 p2 c0 {4,S} {6,S}
6 S u0 p2 c0 {5,S} {7,S}
7 S u0 p2 c0 {6,S} {8,S}
8 S u0 p2 c0 {1,S} {7,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[2.54293, 0.0986015, -0.000195053, 1.7017e-07, -5.46629e-11, 9076.55, 14.8102], Tmin=(10, 'K'), Tmax=(912.998, 'K')),
        NASAPolynomial(coeffs=[16.7335, 0.0106249, -8.11649e-06, 2.71144e-09, -3.32064e-13, 7560.88, -46.4694], Tmin=(912.998, 'K'), Tmax=(3000, 'K'))],
        Tmin=(10, 'K'), Tmax=(3000, 'K'), E0=(75.1785, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(182.918, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from high-level computations: 106.439 kJ/mol
S298 and Cp from CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/Def2TZVP computations

ThermoData(
    H298=(106.439,'kJ/mol'),
    S298=(427.475,'J/(mol*K)'),
    Tdata=([300,400,500,600,800,1000,1500,2000,2500,3000],'K'),
    Cpdata=([155.65,168.506,174.066,175.911,177.325,179.77,181.911,182.052,182.608,181.85],'J/(mol*K)'),
    Cp0=(33.2579,'J/(mol*K)'),
    CpInf=(182.918,'J/(mol*K)'),
    Tmin=(298,'K'),
    Tmax=(3000,'K'),
)
""",
)

entry(
    index=10,
    label="S2O",
    molecule="""
multiplicity 1
1 S u0 p1 c0 {2,D} {3,D}
2 S u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,D}
""",
    thermo=NASA(polynomials=[
        # NASA polynomials are not provided, so only ThermoData is included in longDesc
    ],
        Tmin=(298,'K'), Tmax=(3000,'K'), E0=(-74.2163,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(58.2013,'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from ATcT: -52.64 kJ/mol  
H298 from high-level computations:-62.926,kJ/mol
S298 and Cp from CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/Def2TZVP computations

ThermoData(
    H298=(-52.64,'kJ/mol'),
    S298=(267.212,'J/(mol*K)'),
    Tdata=([300,400,500,600,800,1000,1500,2000,2500,3000],'K'),
    Cpdata=([44.1001,47.7948,50.4541,52.2054,54.5229,55.8681,56.9928,57.3749,57.9809,57.3043],'J/(mol*K)'),
    Cp0=(33.2579,'J/(mol*K)'),
    CpInf=(58.2013,'J/(mol*K)'),
    Tmin=(298,'K'),
    Tmax=(3000,'K'),
)
""",
)

entry(
    index=11,
    label="SH",
    molecule="""
multiplicity 2
1 S u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.49628, 0.000318284, -2.28661e-06, 4.78457e-09, -2.54063e-12, 16476.8, 3.14048], Tmin=(10, 'K'), Tmax=(750.577, 'K')),
        NASAPolynomial(coeffs=[3.14677, 0.000629139, 1.93224e-07, -1.72406e-10, 2.78442e-14, 16573, 5.01752], Tmin=(750.577, 'K'), Tmax=(3000, 'K'))],
        Tmin=(10, 'K'), Tmax=(3000, 'K'), E0=(136.996, 'kJ/mol'), Cp0=(29.1007, 'J/(mol*K)'), CpInf=(37.4151, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from ATcT: 143.26 kJ/mol  
H298 from high-level computations:145.677,kJ/mol
S298 and Cp from CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/Def2TZVP computations

ThermoData(
    H298=(143.26,'kJ/mol'),
    S298=(191.978,'J/(mol*K)'),
    Tdata=([300,400,500,600,800,1000,1500,2000,2500,3000],'K'),
    Cpdata=([29.0555,29.0916,29.2923,29.6683,30.7376,31.7993,33.959,35.2883,35.9276,36.3644],'J/(mol*K)'),
    Cp0=(29.1007,'J/(mol*K)'),
    CpInf=(37.4151,'J/(mol*K)'),
    Tmin=(298,'K'),
    Tmax=(3000,'K'),
)
""",
)

entry(
    index=12,
    label="SO",
    molecule="""
multiplicity 3
1 S u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.51797, -0.00119342, 8.19114e-06, -1.03376e-08, 4.15804e-12, -431.889, 6.72121], Tmin=(10, 'K'), Tmax=(804.784, 'K')),
        NASAPolynomial(coeffs=[3.18041, 0.00226117, -1.55948e-06, 4.83043e-10, -5.55048e-14, -435.097, 7.91894], Tmin=(804.784, 'K'), Tmax=(3000, 'K'))],
        Tmin=(10, 'K'), Tmax=(3000, 'K'), E0=(-3.58678, 'kJ/mol'), Cp0=(29.1007, 'J/(mol*K)'), CpInf=(37.4151, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from high-level computations:5.13256,kJ/mol
S298 and Cp from CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/Def2TZVP computations

ThermoData(
    H298=(5.13256,'kJ/mol'),
    S298=(221.901,'J/(mol*K)'),
    Tdata=([300,400,500,600,800,1000,1500,2000,2500,3000],'K'),
    Cpdata=([30.3621,31.5619,32.7318,33.7292,35.0525,35.8324,36.6885,36.9254,37.1322,37.2062],'J/(mol*K)'),
    Cp0=(29.1007,'J/(mol*K)'),
    CpInf=(37.4151,'J/(mol*K)'),
    Tmin=(298,'K'),
    Tmax=(3000,'K'),
)
""",
)

entry(
    index=13,
    label="SO2",
    molecule="""
multiplicity 1
1 S u0 p1 c0 {2,D} {3,D}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,D}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[4.02204, -0.0018645, 2.55227e-05, -4.13087e-08, 2.10141e-11, -39716.6, 6.70374], Tmin=(10, 'K'), Tmax=(642.851, 'K')),
        NASAPolynomial(coeffs=[3.53625, 0.00602806, -4.25658e-06, 1.35793e-09, -1.61323e-13, -39754.8, 8.05008], Tmin=(642.851, 'K'), Tmax=(3000, 'K'))],
        Tmin=(10, 'K'), Tmax=(3000, 'K'), E0=(-330.224, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(58.2013, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from ATcT: -296.75 kJ/mol  
H298 from high-level computations:-319.669,kJ/mol
S298 and Cp from CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/Def2TZVP computations

ThermoData(
    H298=(-296.75,'kJ/mol'),
    S298=(248.373,'J/(mol*K)'),
    Tdata=([300,400,500,600,800,1000,1500,2000,2500,3000],'K'),
    Cpdata=([40.031,43.6849,46.7295,48.991,52.0791,54.0801,56.267,56.9402,57.5258,57.4377],'J/(mol*K)'),
    Cp0=(33.2579,'J/(mol*K)'),
    CpInf=(58.2013,'J/(mol*K)'),
    Tmin=(298,'K'),
    Tmax=(3000,'K'),
)
""",
)

entry(
    index=14,
    label="SO3",
    molecule="""
1 S u0 p0 c0 {2,D} {3,D} {4,D}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,D}
4 O u0 p2 c0 {1,D}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.84473, 0.0173417, -2.20167e-05, 1.40402e-08, -3.61545e-12, 1553.21, 7.90665], Tmin=(10, 'K'), Tmax=(902.737, 'K')),
        NASAPolynomial(coeffs=[6.10764, 0.00731479, -5.35592e-06, 1.73631e-09, -2.08067e-13, 1144.64, -2.77904], Tmin=(902.737, 'K'), Tmax=(3000, 'K'))],
        Tmin=(10, 'K'), Tmax=(3000, 'K'), E0=(12.9076, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(83.1447, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from high-level computations:27.4437,kJ/mol
S298 and Cp from CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/Def2TZVP computations

ThermoData(
    H298=(27.4437,'kJ/mol'),
    S298=(283.668,'J/(mol*K)'),
    Tdata=([300,400,500,600,800,1000,1500,2000,2500,3000],'K'),
    Cpdata=([61.6563,67.0542,71.0095,73.8979,77.6164,79.7753,81.7788,82.105,82.499,82.111],'J/(mol*K)'),
    Cp0=(33.2579,'J/(mol*K)'),
    CpInf=(83.1447,'J/(mol*K)'),
    Tmin=(298,'K'),
    Tmax=(3000,'K'),
)
""",
)

entry(
    index=15,
    label="HOS",
    molecule="""
multiplicity 2
1 S u1 p2 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[4.01763, -0.00166465, 7.90219e-06, 3.10339e-08, -7.64019e-11, -1993.93, 5.99597], Tmin=(10, 'K'), Tmax=(282.688, 'K')),
        NASAPolynomial(coeffs=[3.23378, 0.00493084, -3.23886e-06, 1.04823e-09, -1.29241e-13, -1931.65, 9.10499], Tmin=(282.688, 'K'), Tmax=(3000, 'K'))],
        Tmin=(10, 'K'), Tmax=(3000, 'K'), E0=(-16.5764, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(58.2013, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
ATcT H298: -5.18 kJ/mol
H298 from high-level computations:-6.44878,kJ/mol
S298 and Cp from CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/Def2TZVP computations

ThermoData(
    H298=(-5.18,'kJ/mol'),
    S298=(239.978,'J/(mol*K)'),
    Tdata=([300,400,500,600,800,1000,1500,2000,2500,3000],'K'),
    Cpdata=([36.9893,39.5077,41.6758,43.5343,46.4724,48.596,51.7667,53.6949,55.2756,55.7922],'J/(mol*K)'),
    Cp0=(33.2579,'J/(mol*K)'),
    CpInf=(58.2013,'J/(mol*K)'),
    Tmin=(298,'K'),
    Tmax=(3000,'K'),
)
""",
)

entry(
    index=16,
    label="HOSO",
    molecule="""
multiplicity 2
1 S u1 p1 c0 {2,S} {3,D}
2 O u0 p2 c0 {1,S} {4,S}
3 O u0 p2 c0 {1,D}
4 H u0 p0 c0 {2,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.93742, 0.00434614, 3.82082e-05, -1.10023e-07, 8.69686e-11, -32276.7, 9.72327], Tmin=(10, 'K'), Tmax=(460.348, 'K')),
        NASAPolynomial(coeffs=[4.77328, 0.00740614, -5.39854e-06, 1.83832e-09, -2.32868e-13, -32463, 5.15113], Tmin=(460.348, 'K'), Tmax=(3000, 'K'))],
        Tmin=(10, 'K'), Tmax=(3000, 'K'), E0=(-268.371, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(78.9875, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from high-level computations:-255.665,kJ/mol
S298 and Cp from CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/Def2TZVP computations

ThermoData(
    H298=(-255.665,'kJ/mol'),
    S298=(285.583,'J/(mol*K)'),
    Tdata=([300,400,500,600,800,1000,1500,2000,2500,3000],'K'),
    Cpdata=([53.3276,57.9861,61.0444,63.5258,67.2555,69.7279,72.8448,74.598,76.2861,76.3033],'J/(mol*K)'),
    Cp0=(33.2579,'J/(mol*K)'),
    CpInf=(78.9875,'J/(mol*K)'),
    Tmin=(298,'K'),
    Tmax=(3000,'K'),
)
""",
)

entry(
    index=17,
    label="HOSO2",
    molecule="""
multiplicity 2
1 S u0 p1 c0 {2,S} {3,S} {4,D}
2 O u0 p2 c0 {1,S} {5,S}
3 O u1 p2 c0 {1,S}
4 O u0 p2 c0 {1,D}
5 H u0 p0 c0 {2,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.92124, 0.00468662, 5.77936e-05, -1.30561e-07, 8.25557e-11, -48365.5, 10.8032], Tmin=(10, 'K'), Tmax=(569.269, 'K')),
        NASAPolynomial(coeffs=[5.35987, 0.0124165, -9.57803e-06, 3.38374e-09, -4.41201e-13, -48818.4, 2.13441], Tmin=(569.269, 'K'), Tmax=(3000, 'K'))],
        Tmin=(10, 'K'), Tmax=(3000, 'K'), E0=(-402.164, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(103.931, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
ATcT H298: -374.7 kJ/mol
H298 from high-level computations:-388.266,kJ/mol
S298 and Cp from CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/Def2TZVP computations


ThermoData(
    H298=(-374.7,'kJ/mol'),
    S298=(300.291,'J/(mol*K)'),
    Tdata=([300,400,500,600,800,1000,1500,2000,2500,3000],'K'),
    Cpdata=([63.7903,73.1706,79.4245,83.4389,89.0887,92.6305,96.6191,98.8712,101.228,100.03],'J/(mol*K)'),
    Cp0=(33.2579,'J/(mol*K)'),
    CpInf=(103.931,'J/(mol*K)'),
    Tmin=(298,'K'),
    Tmax=(3000,'K'),
)
""",
)

entry(
    index=18,
    label="HSO",
    molecule="""
multiplicity 2
1 S u1 p1 c0 {2,D} {3,S}
2 O u0 p2 c0 {1,D}
3 H u0 p0 c0 {1,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[4.03423, -0.00221791, 1.57025e-05, -1.8484e-08, 7.03836e-12, -4976.46, 6.14699], Tmin=(10, 'K'), Tmax=(817.045, 'K')),
        NASAPolynomial(coeffs=[2.99512, 0.00548997, -3.25966e-06, 9.14016e-10, -9.82777e-14, -4894.13, 10.4148], Tmin=(817.045, 'K'), Tmax=(3000, 'K'))],
        Tmin=(10, 'K'), Tmax=(3000, 'K'), E0=(-41.3683, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(58.2013, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from high-level computations:-31.3236,kJ/mol
S298 and Cp from CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/Def2TZVP computations

ThermoData(
    H298=(-31.3236,'kJ/mol'),
    S298=(241.265,'J/(mol*K)'),
    Tdata=([300,400,500,600,800,1000,1500,2000,2500,3000],'K'),
    Cpdata=([36.085,38.7178,41.4085,43.8672,47.6303,50.2291,53.9037,55.5083,56.4527,56.9211],'J/(mol*K)'),
    Cp0=(33.2579,'J/(mol*K)'),
    CpInf=(58.2013,'J/(mol*K)'),
    Tmin=(298,'K'),
    Tmax=(3000,'K'),
)
""",
)

entry(
    index=19,
    label="HSO2",
    molecule="""
multiplicity 2
1 S u1 p0 c0 {2,D} {3,D} {4,S}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,D}
4 H u0 p0 c0 {1,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[4.04863, -0.00405815, 4.85026e-05, -7.75806e-08, 3.95777e-11, -22571, 8.2568], Tmin=(10, 'K'), Tmax=(630.724, 'K')),
        NASAPolynomial(coeffs=[2.90654, 0.0113747, -7.67739e-06, 2.38808e-09, -2.79578e-13, -22589.8, 11.949], Tmin=(630.724, 'K'), Tmax=(3000, 'K'))],
        Tmin=(10, 'K'), Tmax=(3000, 'K'), E0=(-187.667, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(83.1447, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from high-level computations:-176.692,kJ/mol
S298 and Cp from CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/Def2TZVP computations

ThermoData(
    H298=(-176.692,'kJ/mol'),
    S298=(263.238,'J/(mol*K)'),
    Tdata=([300,400,500,600,800,1000,1500,2000,2500,3000],'K'),
    Cpdata=([45.0837,51.8309,57.5464,61.914,68.1866,72.4386,77.6478,79.6341,81.0855,81.2031],'J/(mol*K)'),
    Cp0=(33.2579,'J/(mol*K)'),
    CpInf=(83.1447,'J/(mol*K)'),
    Tmin=(298,'K'),
    Tmax=(3000,'K'),
)
""",
)

entry(
    index=20,
    label="HSOH",
    molecule="""
multiplicity 1
1 S u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {3,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {1,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[4.04799, -0.00465286, 5.70956e-05, -1.06871e-07, 6.39088e-11, -14961.2, 7.34863], Tmin=(10, 'K'), Tmax=(551.897, 'K')),
        NASAPolynomial(coeffs=[3.62636, 0.00841934, -5.65664e-06, 1.81566e-09, -2.20403e-13, -15067.2, 7.75017], Tmin=(551.897, 'K'), Tmax=(3000, 'K'))],
        Tmin=(10, 'K'), Tmax=(3000, 'K'), E0=(-124.401, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(78.9875, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
ATcT H298: -114.32 kJ/mol
H298 from high-level computations:-113.397,kJ/mol
S298 and Cp from CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/Def2TZVP computations

ThermoData(
    H298=(-114.32,'kJ/mol'),
    S298=(255.606,'J/(mol*K)'),
    Tdata=([300,400,500,600,800,1000,1500,2000,2500,3000],'K'),
    Cpdata=([45.0884,50.8718,55.1323,58.2445,63.0314,66.3854,71.0055,73.4776,75.5029,76.0342],'J/(mol*K)'),
    Cp0=(33.2579,'J/(mol*K)'),
    CpInf=(78.9875,'J/(mol*K)'),
    Tmin=(298,'K'),
    Tmax=(3000,'K'),
)
""",
)

entry(
    index=21,
    label="HSOO",
    molecule="""
multiplicity 2
1 S u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u1 p2 c0 {2,S}
4 H u0 p0 c0 {1,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.87436, 0.0109931, -5.77421e-07, -2.31699e-08, 2.16573e-11, 13259.3, 9.48723], Tmin=(10, 'K'), Tmax=(491.441, 'K')),
        NASAPolynomial(coeffs=[4.7341, 0.00834179, -5.75119e-06, 1.84505e-09, -2.22907e-13, 13122.3, 5.41626], Tmin=(491.441, 'K'), Tmax=(3000, 'K'))],
        Tmin=(10, 'K'), Tmax=(3000, 'K'), E0=(110.233, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(83.1447, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
    H298 from high-level computations:123.565,kJ/mol
S298 and Cp from CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/Def2TZVP computations


ThermoData(
    H298=(123.565,'kJ/mol'),
    S298=(288.083,'J/(mol*K)'),
    Tdata=([300,400,500,600,800,1000,1500,2000,2500,3000],'K'),
    Cpdata=([55.4588,60.2863,63.8875,66.8349,71.3393,74.3883,78.1991,79.8755,81.1928,81.1463],'J/(mol*K)'),
    Cp0=(33.2579,'J/(mol*K)'),
    CpInf=(83.1447,'J/(mol*K)'),
    Tmin=(298,'K'),
    Tmax=(3000,'K'),
)
""",
)

entry(
    index=22,
    label="HSS",
    molecule="""
multiplicity 2
1 S u1 p1 c0 {2,D} {3,S}
2 S u0 p2 c0 {1,D}
3 H u0 p0 c0 {1,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.99324, 0.000384408, 1.26992e-05, -2.19379e-08, 1.17605e-11, 11869.7, 7.33301], Tmin=(10, 'K'), Tmax=(574.972, 'K')),
        NASAPolynomial(coeffs=[3.51194, 0.00515713, -3.46809e-06, 1.11635e-09, -1.3704e-13, 11901.5, 9.18386], Tmin=(574.972, 'K'), Tmax=(3000, 'K'))],
        Tmin=(10, 'K'), Tmax=(3000, 'K'), E0=(98.687, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(58.2013, 'J/(mol*K)')),
    shortDesc=u"""""""",
    longDesc=u"""
H298 from high-level computations:109.344,kJ/mol
S298 and Cp from CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/Def2TZVP computations

ThermoData(
    H298=(109.344,'kJ/mol'),
    S298=(254.348,'J/(mol*K)'),
    Tdata=([300,400,500,600,800,1000,1500,2000,2500,3000],'K'),
    Cpdata=([39.5306,42.2036,44.5077,46.4037,49.334,51.3858,54.1966,55.6404,56.6968,56.6359],'J/(mol*K)'),
    Cp0=(33.2579,'J/(mol*K)'),
    CpInf=(58.2013,'J/(mol*K)'),
    Tmin=(298,'K'),
    Tmax=(3000,'K'),
)
""",
)

entry(
    index=23,
    label="HSSH",
    molecule="""
multiplicity 1
1 S u0 p2 c0 {2,S} {3,S}
2 S u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.97462, 0.00146078, 2.98054e-05, -5.7177e-08, 3.26695e-11, 1249.13, 7.72678], Tmin=(10, 'K'), Tmax=(583.795, 'K')),
        NASAPolynomial(coeffs=[3.62753, 0.00980046, -6.94005e-06, 2.27642e-09, -2.80914e-13, 1188.06, 8.34439], Tmin=(583.795, 'K'), Tmax=(3000, 'K'))],
        Tmin=(10, 'K'), Tmax=(3000, 'K'), E0=(10.3749, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(78.9875, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from high-level computations:22.1496,kJ/mol
S298 and Cp from CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/Def2TZVP computations

ThermoData(
    H298=(22.1496,'kJ/mol'),
    S298=(263.48,'J/(mol*K)'),
    Tdata=([300,400,500,600,800,1000,1500,2000,2500,3000],'K'),
    Cpdata=([48.3585,54.084,58.626,62.0649,67.1538,70.5354,74.6132,76.3683,77.7339,77.1397],'J/(mol*K)'),
    Cp0=(33.2579,'J/(mol*K)'),
    CpInf=(78.9875,'J/(mol*K)'),
    Tmin=(298,'K'),
    Tmax=(3000,'K'),
)
""",
)

entry(
    index=24,
    label="OSO",
    molecule="""
multiplicity 1
1 S u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 O u0 p2 c0 {1,S} {5,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.9213, 0.00456317, 5.81253e-05, -1.26535e-07, 7.69001e-11, -35757.5, 7.53899], Tmin=(10, 'K'), Tmax=(591.767, 'K')),
        NASAPolynomial(coeffs=[5.37847, 0.0132169, -1.07119e-05, 3.85334e-09, -5.06255e-13, -36253.9, -1.46393], Tmin=(591.767, 'K'), Tmax=(3000, 'K'))],
        Tmin=(10, 'K'), Tmax=(3000, 'K'), E0=(-297.337, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(99.7737, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from high-level computations:-283.415,kJ/mol
S298 and Cp from CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/Def2TZVP computations

ThermoData(
    H298=(-283.415,'kJ/mol'),
    S298=(273.173,'J/(mol*K)'),
    Tdata=([300,400,500,600,800,1000,1500,2000,2500,3000],'K'),
    Cpdata=([64.254,74.1403,80.8465,84.9659,90.3111,93.3761,95.9835,97.2071,98.9771,96.9101],'J/(mol*K)'),
    Cp0=(33.2579,'J/(mol*K)'),
    CpInf=(99.7737,'J/(mol*K)'),
    Tmin=(298,'K'),
    Tmax=(3000,'K'),
)
""",
)

entry(
    index=25,
    label="H2SS",
    molecule="""
multiplicity 1
1 S u0 p1 c0 {2,D} {3,S} {4,S}
2 S u0 p2 c0 {1,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[4.04822, -0.00452745, 4.95227e-05, -8.5973e-08, 4.93245e-11, 14902.5, 7.20488], Tmin=(10, 'K'), Tmax=(536.147, 'K')),
        NASAPolynomial(coeffs=[2.78458, 0.0101789, -6.39074e-06, 1.91614e-09, -2.2037e-13, 14962.1, 11.806], Tmin=(536.147, 'K'), Tmax=(3000, 'K'))],
        Tmin=(10, 'K'), Tmax=(3000, 'K'), E0=(123.904, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(83.1447, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from high-level computations:134.681,kJ/mol
S298 and Cp from CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/Def2TZVP computations

ThermoData(
    H298=(134.681,'kJ/mol'),
    S298=(253.23,'J/(mol*K)'),
    Tdata=([300,400,500,600,800,1000,1500,2000,2500,3000],'K'),
    Cpdata=([43.4455,49.2325,54.0551,58.0066,64.2578,68.7483,75.0391,78.0115,79.9951,80.5708],'J/(mol*K)'),
    Cp0=(33.2579,'J/(mol*K)'),
    CpInf=(83.1447,'J/(mol*K)'),
    Tmin=(298,'K'),
    Tmax=(3000,'K'),
)
""",
)

entry(
    index=26,
    label="HSSO",
    molecule="""
multiplicity 2
1 S u0 p2 c0 {2,S} {3,S}
2 S u0 p2 c0 {1,S} {4,S}
3 O u1 p2 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.90136, 0.00777643, 4.77408e-05, -1.8524e-07, 1.84285e-10, -5601.55, 10.3593], Tmin=(10, 'K'), Tmax=(380.699, 'K')),
        NASAPolynomial(coeffs=[5.20789, 0.0076612, -5.43972e-06, 1.81062e-09, -2.2679e-13, -5799.67, 4.0223], Tmin=(380.699, 'K'), Tmax=(3000, 'K'))],
        Tmin=(10, 'K'), Tmax=(3000, 'K'), E0=(-46.5664, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(83.1447, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from high-level computations:-32.8514,kJ/mol
S298 and Cp from CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/Def2TZVP computations

ThermoData(
    H298=(-32.8514,'kJ/mol'),
    S298=(297.26,'J/(mol*K)'),
    Tdata=([300,400,500,600,800,1000,1500,2000,2500,3000],'K'),
    Cpdata=([58.3858,62.4591,65.6071,68.2453,72.2492,74.94,78.3476,80.0495,81.4369,81.0724],'J/(mol*K)'),
    Cp0=(33.2579,'J/(mol*K)'),
    CpInf=(83.1447,'J/(mol*K)'),
    Tmin=(298,'K'),
    Tmax=(3000,'K'),
)
""",
)

entry(
    index=27,
    label="HSSSOH",
    molecule="""
multiplicity 1
1 S u0 p2 c0 {2,S} {4,S}
2 S u0 p2 c0 {1,S} {3,S}
3 S u0 p2 c0 {2,S} {6,S}
4 O u0 p2 c0 {1,S} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {3,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.57575, 0.0378121, -5.83003e-05, 4.45814e-08, -1.34858e-11, -14903, 12.5171], Tmin=(10, 'K'), Tmax=(795.232, 'K')),
        NASAPolynomial(coeffs=[8.83775, 0.0113444, -8.37594e-06, 2.7283e-09, -3.28312e-13, -15739.9, -11.6633], Tmin=(795.232, 'K'), Tmax=(3000, 'K'))],
        Tmin=(10, 'K'), Tmax=(3000, 'K'), E0=(-123.956, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(120.56, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from high-level computations:-104.689,kJ/mol
S298 and Cp from CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/Def2TZVP computations

ThermoData(
    H298=(-104.689,'kJ/mol'),
    S298=(348.663,'J/(mol*K)'),
    Tdata=([300,400,500,600,800,1000,1500,2000,2500,3000],'K'),
    Cpdata=([89.5204,98.7802,105.066,109.391,114.865,118.117,121.012,121.36,121.841,121.045],'J/(mol*K)'),
    Cp0=(33.2579,'J/(mol*K)'),
    CpInf=(120.56,'J/(mol*K)'),
    Tmin=(298,'K'),
    Tmax=(3000,'K'),
)
""",
)

entry(
    index=28,
    label="SSO2",
    molecule="""
multiplicity 1
1 S u0 p0 c0 {2,D} {3,D} {4,D}
2 S u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,D}
4 O u0 p2 c0 {1,D}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.94225, 0.00349759, 4.42648e-05, -1.01299e-07, 6.52805e-11, -25467.7, 8.89942], Tmin=(10, 'K'), Tmax=(553.375, 'K')),
        NASAPolynomial(coeffs=[4.7783, 0.010086, -7.83408e-06, 2.71577e-09, -3.46408e-13, -25753.7, 3.61313], Tmin=(553.375, 'K'), Tmax=(3000, 'K'))],
        Tmin=(10, 'K'), Tmax=(3000, 'K'), E0=(-211.772, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(83.1447, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from high-level computations:-198.85,kJ/mol
S298 and Cp from CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/Def2TZVP computations

ThermoData(
    H298=(-198.85,'kJ/mol'),
    S298=(279.38,'J/(mol*K)'),
    Tdata=([300,400,500,600,800,1000,1500,2000,2500,3000],'K'),
    Cpdata=([56.2811,63.2873,67.97,71.0999,75.511,78.1526,80.5893,81.462,82.5847,81.4512],'J/(mol*K)'),
    Cp0=(33.2579,'J/(mol*K)'),
    CpInf=(83.1447,'J/(mol*K)'),
    Tmin=(298,'K'),
    Tmax=(3000,'K'),
)
""",
)

entry(
    index=29,
    label="OSSO",
    molecule="""
multiplicity 1
1 S u0 p1 c0 {2,D} {3,D}
2 S u0 p1 c0 {1,D} {4,D}
3 O u0 p2 c0 {1,D}
4 O u0 p2 c0 {2,D}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.85797, 0.0114385, 3.46169e-05, -1.49048e-07, 1.43964e-10, -20415.2, 9.32464], Tmin=(10, 'K'), Tmax=(406.404, 'K')),
        NASAPolynomial(coeffs=[5.49236, 0.00905884, -7.19019e-06, 2.52087e-09, -3.23424e-13, -20661.2, 1.51869], Tmin=(406.404, 'K'), Tmax=(3000, 'K'))],
        Tmin=(10, 'K'), Tmax=(3000, 'K'), E0=(-169.74, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(83.1447, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from high-level computations:-155.302,kJ/mol
S298 and Cp from CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/Def2TZVP computations

ThermoData(
    H298=(-155.302,'kJ/mol'),
    S298=(292.824,'J/(mol*K)'),
    Tdata=([300,400,500,600,800,1000,1500,2000,2500,3000],'K'),
    Cpdata=([62.7481,67.5009,70.832,73.5148,77.2907,79.4735,81.2598,81.8265,82.7757,81.6757],'J/(mol*K)'),
    Cp0=(33.2579,'J/(mol*K)'),
    CpInf=(83.1447,'J/(mol*K)'),
    Tmin=(298,'K'),
    Tmax=(3000,'K'),
)
""",
)

entry(
    index=30,
    label="OS2",
    molecule="""
multiplicity 3
1 S u1 p1 c0 {2,D} {3,S}
2 S u0 p2 c0 {1,D}
3 O u1 p2 c0 {1,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.95315, 0.00313718, 2.70831e-05, -7.79437e-08, 5.99896e-11, 13548.1, 9.90002], Tmin=(10, 'K'), Tmax=(482.556, 'K')),
        NASAPolynomial(coeffs=[4.8398, 0.00438397, -3.51404e-06, 1.24382e-09, -1.60967e-13, 13362.4, 5.23142], Tmin=(482.556, 'K'), Tmax=(3000, 'K'))],
        Tmin=(10, 'K'), Tmax=(3000, 'K'), E0=(112.637, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(58.2013, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from high-level computations:124.541,kJ/mol
S298 and Cp from CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/Def2TZVP computations

ThermoData(
    H298=(124.541,'kJ/mol'),
    S298=(282.606,'J/(mol*K)'),
    Tdata=([300,400,500,600,800,1000,1500,2000,2500,3000],'K'),
    Cpdata=([47.5024,50.624,52.3703,53.6527,55.4483,56.4767,57.3047,57.5916,58.0674,57.4544],'J/(mol*K)'),
    Cp0=(33.2579,'J/(mol*K)'),
    CpInf=(58.2013,'J/(mol*K)'),
    Tmin=(298,'K'),
    Tmax=(3000,'K'),
)
""",
)

entry(
    index=31,
    label="S1OO1",
    molecule="""
1 S u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {1,S} {2,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[4.05351, -0.00500335, 5.1175e-05, -9.42627e-08, 5.48819e-11, 18657, 6.90488], Tmin=(10, 'K'), Tmax=(577.027, 'K')),
        NASAPolynomial(coeffs=[3.94672, 0.00613619, -4.81588e-06, 1.65915e-09, -2.08506e-13, 18496.2, 5.86117], Tmin=(577.027, 'K'), Tmax=(3000, 'K'))],
        Tmin=(10, 'K'), Tmax=(3000, 'K'), E0=(155.117, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(58.2013, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
ATcT H298: 163.7 kJ/mol
H298 from high-level computations:165.742,kJ/mol
S298 and Cp from CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/Def2TZVP computations

ThermoData(
    H298=(163.7,'kJ/mol'),
    S298=(249.9,'J/(mol*K)'),
    Tdata=([300,400,500,600,800,1000,1500,2000,2500,3000],'K'),
    Cpdata=([42.0522,46.6636,49.8275,51.7665,54.3566,55.8539,57.0318,57.309,57.9302,57.5398],'J/(mol*K)'),
    Cp0=(33.2579,'J/(mol*K)'),
    CpInf=(58.2013,'J/(mol*K)'),
    Tmin=(298,'K'),
    Tmax=(3000,'K'),
)
""",
)

entry(
    index=32,
    label="S1SO1",
    molecule="""
1 S u0 p2 c0 {2,S} {3,S}
2 S u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {1,S} {2,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.97275, 0.00150379, 2.14705e-05, -4.2946e-08, 2.4081e-11, 15156.8, 7.66941], Tmin=(10, 'K'), Tmax=(635.458, 'K')),
        NASAPolynomial(coeffs=[4.38428, 0.00580228, -4.93736e-06, 1.81872e-09, -2.41807e-13, 14965.4, 4.77621], Tmin=(635.458, 'K'), Tmax=(3000, 'K'))],
        Tmin=(10, 'K'), Tmax=(3000, 'K'), E0=(126.009, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(58.2013, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
ATcT H298: 134.3 kJ/mol
H298 from high-level computations:137.384,kJ/mol
S298 and Cp from CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/Def2TZVP computations

ThermoData(
    H298=(134.3,'kJ/mol'),
    S298=(260.847,'J/(mol*K)'),
    Tdata=([300,400,500,600,800,1000,1500,2000,2500,3000],'K'),
    Cpdata=([44.8295,48.8681,51.7915,53.6197,55.6931,56.7555,57.3089,57.5382,58.2295,57.1533],'J/(mol*K)'),
    Cp0=(33.2579,'J/(mol*K)'),
    CpInf=(58.2013,'J/(mol*K)'),
    Tmin=(298,'K'),
    Tmax=(3000,'K'),
)
""",
)

entry(
    index=33,
    label="HOS2",
    molecule="""
multiplicity 2
1 S u1 p1 c0 {2,D} {3,S}
2 S u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,S} {4,S}
4 H u0 p0 c0 {3,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.90203, 0.00731664, 4.19141e-05, -1.52061e-07, 1.3867e-10, -9078.44, 10.0199], Tmin=(10, 'K'), Tmax=(420.132, 'K')),
        NASAPolynomial(coeffs=[5.48278, 0.00632885, -4.76558e-06, 1.67736e-09, -2.18369e-13, -9335.37, 2.28752], Tmin=(420.132, 'K'), Tmax=(3000, 'K'))],
        Tmin=(10, 'K'), Tmax=(3000, 'K'), E0=(-75.4837, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(78.9875, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from high-level computations:-61.9898,kJ/mol
S298 and Cp from CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/Def2TZVP computations

ThermoData(
    H298=(-61.9898,'kJ/mol'),
    S298=(292.866,'J/(mol*K)'),
    Tdata=([300,400,500,600,800,1000,1500,2000,2500,3000],'K'),
    Cpdata=([57.2607,61.1362,63.6209,65.6718,68.7212,70.7149,73.243,74.8563,76.4827,76.3264],'J/(mol*K)'),
    Cp0=(33.2579,'J/(mol*K)'),
    CpInf=(78.9875,'J/(mol*K)'),
    Tmin=(298,'K'),
    Tmax=(3000,'K'),
)
""",
)

entry(
    index=34,
    label="S1OSO1",
    molecule="""
multiplicity 1
1 S u0 p2 c0 {3,S} {4,S}
2 S u0 p2 c0 {3,S} {4,S}
3 O u0 p2 c0 {1,S} {2,S}
4 O u0 p2 c0 {1,S} {2,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.93088, 0.00401177, 4.77258e-05, -1.06242e-07, 6.5176e-11, 9014.82, 8.54971], Tmin=(10, 'K'), Tmax=(592.68, 'K')),
        NASAPolynomial(coeffs=[5.44172, 0.0100199, -8.49225e-06, 3.12545e-09, -4.15852e-13, 8551.12, -0.349939], Tmin=(592.68, 'K'), Tmax=(3000, 'K'))],
        Tmin=(10, 'K'), Tmax=(3000, 'K'), E0=(74.9248, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(83.1447, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from high-level computations:88.1877,kJ/mol
S298 and Cp from CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/Def2TZVP computations

ThermoData(
    H298=(88.1877,'kJ/mol'),
    S298=(278.121,'J/(mol*K)'),
    Tdata=([300,400,500,600,800,1000,1500,2000,2500,3000],'K'),
    Cpdata=([58.9423,66.8545,72.0155,74.977,78.5925,80.4755,81.5413,82.0014,83.1933,81.2682],'J/(mol*K)'),
    Cp0=(33.2579,'J/(mol*K)'),
    CpInf=(83.1447,'J/(mol*K)'),
    Tmin=(298,'K'),
    Tmax=(3000,'K'),
)
""",
)

entry(
    index=35,
    label="O2S2",
    molecule="""
multiplicity 3
1 S u0 p1 c0 {2,S} {3,S} {4,D}
2 S u1 p2 c0 {1,S}
3 O u1 p2 c0 {1,S}
4 O u0 p2 c0 {1,D}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.8675, 0.0105887, 4.27101e-05, -1.77157e-07, 1.74656e-10, -5831.95, 11.0892], Tmin=(10, 'K'), Tmax=(392.565, 'K')),
        NASAPolynomial(coeffs=[5.46766, 0.00894532, -7.03172e-06, 2.4537e-09, -3.14201e-13, -6070.55, 3.42669], Tmin=(392.565, 'K'), Tmax=(3000, 'K'))],
        Tmin=(10, 'K'), Tmax=(3000, 'K'), E0=(-48.484, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(83.1447, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from high-level computations:-34.0869,kJ/mol
S298 and Cp from CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/Def2TZVP computations

ThermoData(
    H298=(-34.0869,'kJ/mol'),
    S298=(307.271,'J/(mol*K)'),
    Tdata=([300,400,500,600,800,1000,1500,2000,2500,3000],'K'),
    Cpdata=([62.5206,67.0953,70.4191,73.1068,76.919,79.1601,81.1066,81.7629,82.7148,81.6295],'J/(mol*K)'),
    Cp0=(33.2579,'J/(mol*K)'),
    CpInf=(83.1447,'J/(mol*K)'),
    Tmin=(298,'K'),
    Tmax=(3000,'K'),
)
""",
)

entry(
    index=36,
    label="O2S2",
    molecule="""
multiplicity 1
1 S u0 p1 c0 {2,S} {3,S} {4,D}
2 S u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {1,S} {2,S}
4 O u0 p2 c0 {1,D}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.92095, 0.00494244, 5.07013e-05, -1.2833e-07, 8.85939e-11, -14861.8, 10.1685], Tmin=(10, 'K'), Tmax=(531.608, 'K')),
        NASAPolynomial(coeffs=[5.55636, 0.00907486, -7.33997e-06, 2.62126e-09, -3.4189e-13, -15267.9, 1.12738], Tmin=(531.608, 'K'), Tmax=(3000, 'K'))],
        Tmin=(10, 'K'), Tmax=(3000, 'K'), E0=(-123.592, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(83.1447, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
ATcT H298: -114.32 kJ/mol
H298 from high-level computations:-110.067,kJ/mol
S298 and Cp from CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/Def2TZVP computations

ThermoData(
    H298=(-114.32,'kJ/mol'),
    S298=(293.278,'J/(mol*K)'),
    Tdata=([300,400,500,600,800,1000,1500,2000,2500,3000],'K'),
    Cpdata=([60.0263,67.0564,71.1998,73.8389,77.4968,79.5747,81.2295,81.8646,82.902,81.4996],'J/(mol*K)'),
    Cp0=(33.2579,'J/(mol*K)'),
    CpInf=(83.1447,'J/(mol*K)'),
    Tmin=(298,'K'),
    Tmax=(3000,'K'),
)
""",
)

entry(
    index=37,
    label="O2S2",
    molecule="""
multiplicity 1
1 S u0 p1 c0 {2,D} {3,S} {4,S}
2 S u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,S} {4,S}
4 O u0 p2 c0 {1,S} {3,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.91714, 0.00510009, 5.20188e-05, -1.2973e-07, 8.77711e-11, 11781.8, 9.52554], Tmin=(10, 'K'), Tmax=(544.812, 'K')),
        NASAPolynomial(coeffs=[5.78837, 0.00904851, -7.54855e-06, 2.74868e-09, -3.63095e-13, 11315.4, -0.774643], Tmin=(544.812, 'K'), Tmax=(3000, 'K'))],
        Tmin=(10, 'K'), Tmax=(3000, 'K'), E0=(97.9313, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(83.1447, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from high-level computations:111.58,kJ/mol
S298 and Cp from CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/Def2TZVP computations

ThermoData(
    H298=(111.58, 'kJ/mol'),
    S298=(288.513, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000], 'K'),
    Cpdata=([61.0041, 68.3816, 72.6795, 75.2182, 78.6109, 80.4335, 81.6109, 82.0731, 83.1109, 81.4869], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(83.1447, 'J/(mol*K)'),
    Tmin=(298,'K'),
    Tmax=(3000,'K'),
)
""",
)

entry(
    index=38,
    label="O2S2_T",
    molecule="""
multiplicity 3
1 S u1 p2 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 S u1 p1 c0 {2,S} {4,D}
4 O u0 p2 c0 {3,D}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.77926, 0.0218244, -3.89469e-05, 3.65264e-08, -1.38071e-11, -3719.55, 11.1723], Tmin=(10, 'K'), Tmax=(635.774, 'K')),
        NASAPolynomial(coeffs=[5.99281, 0.00789774, -6.08936e-06, 2.07228e-09, -2.58969e-13, -4001.02, 1.49577], Tmin=(635.774, 'K'), Tmax=(3000, 'K'))],
        Tmin=(10, 'K'), Tmax=(3000, 'K'), E0=(-30.9336, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(83.1447, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from high-level computations:-15.8168,kJ/mol
S298 and Cp from CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/Def2TZVP computations

ThermoData(
    H298=(-15.8168, 'kJ/mol'),
    S298=(314.058, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000], 'K'),
    Cpdata=([63.986, 68.692, 71.9833, 74.4421, 77.8962, 79.9395, 81.6587, 82.0271, 82.663, 81.9546], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(83.1447, 'J/(mol*K)'),
    Tmin=(298,'K'),
    Tmax=(3000,'K'),
)
""",
)