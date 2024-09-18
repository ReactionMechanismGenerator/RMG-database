#!/usr/bin/env python
# encoding: utf-8

name = "NH3"
shortDesc = "Ammonia oxidation"
longDesc = """
Written by Alon Grinberg Dana,
Based on 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ computations
with enthalpies from ATcT  v. 1.130 where available.
"""

entry(
    index=1,
    label="N",
    molecule="""
multiplicity 4
1 N u3 p1 c0
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[2.5, 4.40191e-13, -7.53247e-16, 5.07597e-19, -1.16114e-22, 56076.4, 4.17947], Tmin=(298, 'K'), Tmax=(2023.39, 'K')),
        NASAPolynomial(coeffs=[2.5, 1.12586e-09, -7.88843e-13, 2.44938e-16, -2.84351e-20, 56076.4, 4.17947], Tmin=(2023.39, 'K'), Tmax=(2500, 'K'))],
        Tmin=(298, 'K'), Tmax=(2500, 'K'), E0=(466.246, 'kJ/mol'), Cp0=(20.7862, 'J/(mol*K)'), CpInf=(20.7862, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from ATcT 1.130
S298 and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(472.440, 'kJ/mol'),
    S298=(153.171, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([20.7862, 20.7862, 20.7862, 20.7862, 20.7862, 20.7862, 20.7862, 20.7862, 20.7862], 'J/(mol*K)'),
    Cp0=(20.7862, 'J/(mol*K)'),
    CpInf=(20.7862, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=2,
    label="NH(S)",
    molecule="""
multiplicity 1
1 N u0 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.60037, -0.000534387, 6.06544e-07, 2.40431e-10, -2.16168e-13, 60210.6, 0.274904], Tmin=(298, 'K'), Tmax=(1016.57, 'K')),
        NASAPolynomial(coeffs=[3.37342, -0.000144347, 7.73144e-07, -3.55512e-10, 5.00787e-14, 60282.7, 1.50133], Tmin=(1016.57, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(500.705, 'kJ/mol'), Cp0=(29.1007, 'J/(mol*K)'), CpInf=(37.4151, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from ATcT 1.130
S298 and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(509.39, 'kJ/mol'),
    S298=(171.743, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([29.0839, 29.0587, 29.1119, 29.269, 29.8957, 30.7503, 32.8289, 34.3866, 35.288], 'J/(mol*K)'),
    Cp0=(29.1007, 'J/(mol*K)'),
    CpInf=(37.4151, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=3,
    label="NH(T)",
    molecule="""
multiplicity 3
1 N u2 p1 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.60703, -0.000582915, 7.15283e-07, 1.58499e-10, -1.95045e-13, 42096.9, 1.34837], Tmin=(298, 'K'), Tmax=(1018.46, 'K')),
        NASAPolynomial(coeffs=[3.35047, -8.48743e-05, 7.32289e-07, -3.43917e-10, 4.88775e-14, 42175.6, 2.72055], Tmin=(1018.46, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(350.104, 'kJ/mol'), Cp0=(29.1007, 'J/(mol*K)'), CpInf=(37.4151, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from ATcT 1.130
S298 and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(358.79, 'kJ/mol'),
    S298=(180.898, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([29.0824, 29.0587, 29.1169, 29.2825, 29.9315, 30.8004, 32.8894, 34.4385, 35.3262], 'J/(mol*K)'),
    Cp0=(29.1007, 'J/(mol*K)'),
    CpInf=(37.4151, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=4,
    label="NH2",
    molecule="""
multiplicity 2
1 N u1 p1 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[4.17563, -0.00169104, 5.10754e-06, -3.25458e-09, 7.05524e-13, 21166, -0.0947707], Tmin=(298, 'K'), Tmax=(1159.03, 'K')),
        NASAPolynomial(coeffs=[2.96198, 0.00249753, -3.13356e-07, -1.36462e-10, 3.29417e-14, 21447.3, 5.93948], Tmin=(1159.03, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(176.099, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(58.2013, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from ATcT 1.130
S298 and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(186.03, 'kJ/mol'),
    S298=(194.473, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([33.6462, 34.3101, 35.266, 36.4685, 39.246, 41.9191, 47.4293, 51.0909, 53.1949], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(58.2013, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=5,
    label="NH3",
    molecule="""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[4.02402, -0.00171864, 1.05396e-05, -8.56127e-09, 2.31612e-12, -6679.15, 0.316593], Tmin=(298, 'K'), Tmax=(951.008, 'K')),
        NASAPolynomial(coeffs=[2.1289, 0.00625227, -2.03265e-06, 2.51927e-10, -6.70266e-16, -6318.69, 9.36423], Tmin=(951.008, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(-55.5883, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(83.1447, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from ATcT 1.130
S298 and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(-45.556, 'kJ/mol',),
    S298=(192.286, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([35.3396, 37.6552, 40.4923, 43.6023, 49.6031, 54.8092, 64.6581, 70.8086, 74.4798], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(83.1447, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=6,
    label="N2",
    molecule="""
1 N u0 p1 c0 {2,T}
2 N u0 p1 c0 {1,T}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.57917, -0.00092269, 2.52013e-06, -1.59938e-09, 3.37289e-13, -1044.86, 2.81354], Tmin=(298, 'K'), Tmax=(1224.73, 'K')),
        NASAPolynomial(coeffs=[2.85431, 0.00144431, -3.78377e-07, -2.18841e-11, 1.53369e-14, -867.277, 6.45765], Tmin=(1224.73, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(-8.63946, 'kJ/mol'), Cp0=(29.1007, 'J/(mol*K)'), CpInf=(37.4151, 'J/(mol*K)'))
    ,
    shortDesc=u"""""",
    longDesc=u"""
H298 is exact
S298 and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(0.0, 'kJ/mol',),
    S298=(191.465, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([29.0347, 29.2669, 29.6493, 30.162, 31.3996, 32.5611, 34.6758, 35.7636, 36.2178], 'J/(mol*K)'),
    Cp0=(29.1007, 'J/(mol*K)'),
    CpInf=(37.4151, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=7,
    label="NNH",
    molecule="""
multiplicity 2
1 N u1 p1 c0 {2,D}
2 N u0 p1 c0 {1,D} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.95201, -0.00112385, 8.04654e-06, -7.44027e-09, 2.23831e-12, 28790.3, 4.48518], Tmin=(298, 'K'), Tmax=(876.559, 'K')),
        NASAPolynomial(coeffs=[2.59685, 0.00505955, -2.53369e-06, 6.05725e-10, -5.62358e-14, 29027.9, 10.8447], Tmin=(876.559, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(239.281, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(58.2013, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from ATcT 1.130
S298 and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(249.23, 'kJ/mol'),
    S298=(224.169, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([34.6139, 36.2864, 38.3125, 40.4409, 44.173, 47.1274, 51.9156, 54.2885, 55.5058], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(58.2013, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=8,
    label="N2H2",
    molecule="""
1 N u0 p1 c0 {2,D} {3,S}
2 N u0 p1 c0 {1,D} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.90363, -0.00277548, 1.71597e-05, -1.59688e-08, 4.88596e-12, 22888.6, 4.17493], Tmin=(298, 'K'), Tmax=(858.612, 'K')),
        NASAPolynomial(coeffs=[1.18583, 0.009886, -4.96016e-06, 1.20622e-09, -1.14888e-13, 23355.3, 16.8724],  Tmin=(858.612, 'K'), Tmax=(2500, 'K'))],
        Tmin=(298, 'K'), Tmax=(2500, 'K'), E0=(190.102, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(83.1447, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from ATcT 1.130
S298 and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(199.97, 'kJ/mol'),
    S298=(217.988, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([35.2366, 38.4647, 42.4773, 46.6858, 53.9989, 59.817, 69.3669, 74.2705, 76.9546], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(83.1447, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=9,
    label="N2H2(T)",
    molecule="""
multiplicity 3
1 N u1 p1 c0 {2,S} {3,S}
2 N u1 p1 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[2.80462, 0.00602849, 3.95609e-06, -8.62046e-09, 3.61111e-12, 44228.5, 10.2844], Tmin=(298, 'K'), Tmax=(866.507, 'K')),
        NASAPolynomial(coeffs=[2.53086, 0.00945813, -5.73027e-06, 1.71661e-09, -2.03545e-13, 44194.6, 11.0968], Tmin=(866.507, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(366.831, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'),
        CpInf=(78.9875, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298, S298 and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(377.074, 'kJ/mol'),
    S298=(234.184, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([39.6793, 44.7435, 49.5678, 53.7002, 59.9985, 64.6321, 71.4662, 74.7812, 76.8449], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(78.9875, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=10,
    label="H2NN(S)",
    molecule="""
1 N u0 p0 c+1 {2,D} {3,S} {4,S}
2 N u0 p2 c-1 {1,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.81477, -0.00187204, 1.62016e-05, -1.58152e-08, 5.01782e-12, 34969.2, 4.44255], Tmin=(298, 'K'), Tmax=(830.377, 'K')),
        NASAPolynomial(coeffs=[1.36937, 0.00990746, -5.07663e-06, 1.26764e-09, -1.25188e-13, 35375.3, 15.7857], Tmin=(830.377, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(290.494, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(83.1447, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from ATcT 1.130
S298 and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(300.46, 'kJ/mol'),
    S298=(217.902, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([36.0598, 39.5746, 43.755, 47.9949, 55.2547, 60.9869, 70.283, 74.9856, 77.5189], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(83.1447, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=11,
    label="H2NN(T)",
    molecule="""
multiplicity 3
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 N u2 p1 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.04506, 0.00470387, 4.86932e-06, -8.53561e-09, 3.46826e-12, 42828.9, 9.41533], Tmin=(298, 'K'), Tmax=(838.109, 'K')),
        NASAPolynomial(coeffs=[2.592, 0.00845899, -4.70219e-06, 1.34563e-09, -1.55637e-13, 42848.9, 11.1873], Tmin=(838.109, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(355.382, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(83.1447, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298, S298, and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(365.612, 'kJ/mol'),
    S298=(235.406, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([39.0515, 43.5863, 47.9629, 51.801, 57.9468, 62.6902, 70.3347, 74.5841, 77.3535], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(83.1447, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=12,
    label="N2H3",
    molecule="""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 N u1 p1 c0 {1,S} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[2.4704, 0.0102434, -2.24608e-06, -2.64426e-09, 1.46424e-12, 25803.2, 11.5301], Tmin=(298, 'K'), Tmax=(873.911, 'K')),
        NASAPolynomial(coeffs=[2.54229, 0.0110855, -5.70181e-06, 1.52552e-09, -1.67311e-13, 25745.9, 10.937],  Tmin=(873.911, 'K'), Tmax=(2500, 'K'))],
        Tmin=(298, 'K'), Tmax=(2500, 'K'), E0=(213.536, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(108.088, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from ATcT 1.130
S298 and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

Rotor scan not smooth, need to consider a strongly-coupled inversion mode

ThermoData(
    H298=(224.24, 'kJ/mol'),
    S298=(237.266, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([43.9292, 50.5402, 56.4966, 61.7058, 70.4242, 77.2517, 88.513, 94.9756, 99.1945], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(108.088, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=13,
    label="N2H4",
    molecule="""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 N u0 p1 c0 {1,S} {5,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[2.35889, 0.0117876, 7.52133e-07, -7.2024e-09, 3.25471e-12, 10513.5, 11.6062], Tmin=(298, 'K'), Tmax=(867.229, 'K')),
        NASAPolynomial(coeffs=[2.1854, 0.0146696, -7.83336e-06, 2.16554e-09, -2.43776e-13, 10465.3, 11.9671], Tmin=(867.229, 'K'), Tmax=(2500, 'K'))],
        Tmin=(298, 'K'), Tmax=(2500, 'K'), E0=(86.2821, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(128.874, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from ATcT 1.130
S298 and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(97.56, 'kJ/mol'),
    S298=(237.245, 'J/(mol*K)'), # c=1
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([48.1822, 56.75, 64.4017, 71.1699, 82.4016, 91.0855, 105.125, 113.069, 118.318], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(128.874, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=14,
    label="NH3NH",
    molecule="""
1 N u0 p0 c+1 {2,S} {3,S} {4,S} {5,S}
2 N u0 p2 c-1 {1,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.40007, 0.00605245, 7.56422e-06, -9.63729e-09, 3.18472e-12, 32468.1, 7.40385], Tmin=(298, 'K'), Tmax=(835.206, 'K')),
        NASAPolynomial(coeffs=[1.78544, 0.0137859, -6.32582e-06, 1.45068e-09, -1.34464e-13, 32737.8, 14.9026], Tmin=(835.206, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(269.545, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(128.874, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298, S298, and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(281.023, 'kJ/mol'),
    S298=(239.749, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([46.9974, 53.9847, 60.8924, 67.3473, 78.5492, 87.6979, 103.514, 112.385, 117.413], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(128.874, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=15,
    label="N3H",
    molecule="""
1 N u0 p2 c-1 {2,D}
2 N u0 p0 c+1 {1,D} {3,D}
3 N u0 p1 c0 {2,D} {4,S}
4 H u0 p0 c0 {3,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[2.74276, 0.0108092, -8.34987e-06, 3.50729e-09, -6.22863e-13, 33838.7, 10.2512], Tmin=(298, 'K'), Tmax=(1193.09, 'K')),
        NASAPolynomial(coeffs=[3.75119, 0.00742842, -4.0995e-06, 1.13236e-09, -1.25236e-13, 33598.1, 5.20806], Tmin=(1193.09, 'K'), Tmax=(2500, 'K'))],
        Tmin=(298, 'K'), Tmax=(2500, 'K'), E0=(280.682, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(83.1447, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from ATcT 1.130
S298 and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(291.58, 'kJ/mol'),
    S298=(239.1, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([44.2453, 49.4604, 53.6725, 57.2887, 63.0867, 67.3409, 73.6203, 76.8927, 79.1299], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(83.1447, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=16,
    label="N3H5",
    molecule="""
1 N u0 p1 c0 {2,S} {4,S} {5,S}
2 N u0 p1 c0 {1,S} {3,S} {6,S}
3 N u0 p1 c0 {2,S} {7,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.27949, 0.0221769, -1.43802e-05, 5.20758e-09, -8.24357e-13, 21673.1, 8.66556], Tmin=(298, 'K'), Tmax=(1224.34, 'K')),
        NASAPolynomial(coeffs=[4.54305, 0.0180488, -9.3226e-06, 2.45368e-09, -2.62032e-13, 21363.7, 2.31386], Tmin=(1224.34, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(180.079, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'),
        CpInf=(174.604, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298, S298 and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(195.541, 'kJ/mol'),
    S298=(277.401, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([72.9684, 84.4757, 94.4758, 103.263, 117.7, 128.708, 146.165, 155.963, 162.411], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(174.604, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=17,
    label="NO",
    molecule="""
multiplicity 2
1 N u1 p1 c0 {2,D}
2 O u0 p2 c0 {1,D}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.54726, -0.000976042, 3.57791e-06, -2.83595e-09, 7.41777e-13, 9921.91, 4.62453], Tmin=(298, 'K'), Tmax=(1010.73, 'K')),
        NASAPolynomial(coeffs=[2.75583, 0.00215604, -1.07029e-06, 2.29919e-10, -1.6545e-14, 10081.9, 8.45118], Tmin=(1010.73, 'K'), Tmax=(2500, 'K'))],
        Tmin=(298, 'K'), Tmax=(2500, 'K'), E0=(82.5046, 'kJ/mol'), Cp0=(29.1007, 'J/(mol*K)'), CpInf=(37.4151, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from ATcT 1.130
S298 and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(91.143, 'kJ/mol'),
    S298=(205.185, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([29.1848, 29.639, 30.2811, 31.0423, 32.5281, 33.7023, 35.5187, 36.2781, 36.5925], 'J/(mol*K)'),
    Cp0=(29.1007, 'J/(mol*K)'),
    CpInf=(37.4151, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=18,
    label="HNO(S)",
    molecule="""
1 N u0 p1 c0 {2,D} {3,S}
2 O u0 p2 c0 {1,D}
3 H u0 p0 c0 {1,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[4.04892, -0.00203371, 9.1381e-06, -7.68952e-09, 2.1349e-12, 11684, 3.72802], Tmin=(298, 'K'), Tmax=(947.955, 'K')),
        NASAPolynomial(coeffs=[2.28668, 0.00540271, -2.62961e-06, 5.86811e-10, -4.79003e-14, 12018.1, 12.1356], Tmin=(947.955, 'K'), Tmax=(2500, 'K'))],
        Tmin=(298, 'K'), Tmax=(2500, 'K'), E0=(97.1133, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(58.2013, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from ATcT 1.130
S298 and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(106.98, 'kJ/mol'),
    S298=(220.593, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([33.9253, 35.3633, 37.2635, 39.4024, 43.3578, 46.5106, 51.6233, 54.09, 55.3123], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(58.2013, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=19,
    label="HNO(T)",
    molecule="""
multiplicity 3
1 N u1 p1 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.9029, -0.000720791, 7.98867e-06, -8.20547e-09, 2.72225e-12, 21384.6, 5.26094], Tmin=(298, 'K'), Tmax=(797.947, 'K')),
        NASAPolynomial(coeffs=[2.76701, 0.00497317, -2.71477e-06, 7.36833e-10, -7.93508e-14, 21565.9, 10.4846], Tmin=(797.947, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(177.678, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(58.2013, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298, S298, and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(187.668, 'kJ/mol'),
    S298=(229.222, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([35.0004, 36.8737, 38.9327, 40.9764, 44.5361, 47.226, 51.5718, 53.8883, 55.2562], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(58.2013, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=20,
    label="HON(S)",
    molecule="""
1 N u0 p2 c-1 {2,D}
2 O u0 p1 c+1 {1,D} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.87944, -0.00103045, 8.89067e-06, -9.07581e-09, 3.0217e-12, 32654.2, 4.42294], Tmin=(298, 'K'), Tmax=(790.668, 'K')),
        NASAPolynomial(coeffs=[2.66917, 0.00509258, -2.72596e-06, 7.19359e-10, -7.55345e-14, 32845.5, 9.9775], Tmin=(790.668, 'K'), Tmax=(3000, 'K'))],
                Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(271.348, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(58.2013, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298, S298, and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(281.249, 'kJ/mol'),
    S298=(220.65, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([34.5515, 36.4022, 38.5912, 40.7405, 44.362, 47.1941, 51.7277, 54.0203, 55.3133], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(58.2013, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=21,
    label="HON(T)",
    molecule="""
multiplicity 3
1 N u2 p1 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.62076, 0.00100623, 5.86889e-06, -7.6479e-09, 2.90357e-12, 24700.4, 6.62511], Tmin=(298, 'K'), Tmax=(840.198, 'K')),
        NASAPolynomial(coeffs=[3.06606, 0.00477133, -2.86016e-06, 8.70968e-10, -1.05115e-13, 24753.9, 8.96844], Tmin=(840.198, 'K'), Tmax=(2500, 'K'))],
        Tmin=(298, 'K'), Tmax=(2500, 'K'), E0=(205.045, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(58.2013, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from ATcT 1.130
S298 and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(215.03, 'kJ/mol'),
    S298=(230.74, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([35.5185, 37.766, 40.0513, 42.1275, 45.3492, 47.7332, 51.5332, 53.647, 55.0837], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(58.2013, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=22,
    label="NH2O",
    molecule="""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[4.07928, 0.00227378, 4.54857e-06, -4.93461e-09, 1.48515e-12, 6352.15, 3.76557], Tmin=(298, 'K'), Tmax=(914.757, 'K')),
        NASAPolynomial(coeffs=[2.98935, 0.00703992, -3.26708e-06, 7.61529e-10, -7.16286e-14, 6551.55, 8.92673], Tmin=(914.757, 'K'), Tmax=(2500, 'K'))],
        Tmin=(298, 'K'), Tmax=(2500, 'K'), E0=(52.9039, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(83.1447, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from ATcT 1.130
S298 and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(64.02, 'kJ/mol'),
    S298=(231.513, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([41.9816, 45.2358, 48.4661, 51.5984, 57.2998, 61.9654, 69.8886, 74.3812, 77.0853], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(83.1447, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=23,
    label="NHOH",
    molecule="""
multiplicity 2
1 N u1 p1 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.07284, 0.00442232, 5.37198e-06, -8.99621e-09, 3.6302e-12, 10216.3, 9.07206], Tmin=(298, 'K'), Tmax=(839.264, 'K')),
        NASAPolynomial(coeffs=[2.59974, 0.00835128, -4.64222e-06, 1.33526e-09, -1.55318e-13, 10236.7, 10.9204], Tmin=(839.264, 'K'), Tmax=(2500, 'K'))],
        Tmin=(298, 'K'), Tmax=(2500, 'K'), E0=(84.2354, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(83.1447, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from ATcT 1.130
S298 and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(94.45, 'kJ/mol'),
    S298=(233.325, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([38.867, 43.3346, 47.6713, 51.4871, 57.5699, 62.2706, 69.9013, 74.2066, 77.0521], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(83.1447, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=24,
    label="NH2OH",
    molecule="""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[2.45498, 0.00912211, 5.52546e-06, -1.28325e-08, 5.37895e-12, -6389.62, 11.3877], Tmin=(298, 'K'), Tmax=(901.673, 'K')),
        NASAPolynomial(coeffs=[2.33175, 0.0137315, -8.90135e-06, 2.83138e-09, -3.49572e-13, -6532.55, 11.0537], Tmin=(901.673, 'K'), Tmax=(2500, 'K'))],
        Tmin=(298, 'K'), Tmax=(2500, 'K'), E0=(-54.3299, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(103.931, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from ATcT 1.130
S298 and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(-43.46, 'kJ/mol'),
    S298=(234.76, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([44.8708, 52.3121, 59.3393, 65.323, 74.0483, 80.2019, 88.9773, 93.3877, 96.694], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(103.931, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=25,
    label="NH3O",
    molecule="""
1 N u0 p0 c+1 {2,S} {3,S} {4,S} {5,S}
2 O u0 p3 c-1 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.72113, -0.00211582, 2.34595e-05, -2.38341e-08, 7.81597e-12, 6037.76, 5.19934], Tmin=(298, 'K'), Tmax=(807.523, 'K')),
        NASAPolynomial(coeffs=[0.301436, 0.0148247, -8.01035e-06, 2.14848e-09, -2.28548e-13, 6590.01, 20.9661], Tmin=(807.523, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(49.8408, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(108.088, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from ATcT 1.130
S298 and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(60.0, 'kJ/mol'),
    S298=(221.292, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([38.4778, 44.0343, 50.1571, 56.256, 66.9449, 75.0582, 88.1808, 95.1716, 99.2691], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(108.088, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=26,
    label="NO2",
    molecule="""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 N u0 p1 c0 {1,S} {3,D}
3 O u0 p2 c0 {2,D}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.44844, 0.00226387, 6.15116e-06, -9.07133e-09, 3.4916e-12, 2931.62, 8.34207], Tmin=(298, 'K'), Tmax=(882.308, 'K')),
        NASAPolynomial(coeffs=[2.86852, 0.00676166, -4.67235e-06, 1.50729e-09, -1.85984e-13, 2961.22, 10.6551], Tmin=(882.308, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(23.9105, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(58.2013, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from ATcT 1.130
S298 and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(34.071, 'kJ/mol'),
    S298=(239.979, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([37.1699, 40.2433, 43.2638, 45.9116, 49.7122, 52.1859, 55.2851, 56.378, 57.0702], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(58.2013, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=27,
    label="cNOO",
    molecule="""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {3,S}
3 N u1 p1 c0 {1,S} {2,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[2.2074, 0.0124306, -1.4031e-05, 7.58575e-09, -1.60229e-12, 41307.8, 13.6722], Tmin=(298, 'K'), Tmax=(1120.15, 'K')),
        NASAPolynomial(coeffs=[4.5525, 0.00405638, -2.81708e-06, 9.11697e-10, -1.12752e-13, 40782.4, 2.09241], Tmin=(1120.15, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(342.271, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(58.2013, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from ATcT 1.130
S298 and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(352.6, 'kJ/mol'),
    S298=(244.388, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([40.4759, 44.7168, 47.9996, 50.2095, 53.1141, 54.9062, 56.6267, 57.1019, 57.713], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(58.2013, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=28,
    label="NHOO(S)",
    molecule="""
1 N u0 p2 c-1 {2,S} {4,S}
2 O u0 p1 c+1 {1,S} {3,D}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[1.43236, 0.0153851, -8.68908e-06, -1.50068e-09, 2.0642e-12, 27088.3, 17.3107], Tmin=(298, 'K'), Tmax=(936.892, 'K')),
        NASAPolynomial(coeffs=[3.69261, 0.0100996, -7.21442e-06, 2.42225e-09, -3.09392e-13, 26473.2, 5.53141], Tmin=(936.892, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(223.308, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(78.9875, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from ATcT 1.130
S298 and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(233.80, 'kJ/mol'),
    S298=(246.614, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([43.6981, 51.0261, 57.4357, 62.2967, 68.431, 72.3426, 76.7918, 78.475, 80.1063], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(78.9875, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=29,
    label="NHOO(T)",
    molecule="""
multiplicity 3
1 N u1 p1 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u1 p2 c0 {2,S}
4 H u0 p0 c0 {1,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.96153, 0.0022846, 3.2891e-05, -7.09302e-08, 4.39506e-11, 41138, 8.37658], Tmin=(10, 'K'), Tmax=(566.683, 'K')),
        NASAPolynomial(coeffs=[4.36262, 0.00820607, -5.9509e-06, 2.02036e-09, -2.56656e-13, 40952, 5.42939], Tmin=(566.683, 'K'), Tmax=(3000, 'K')), ],
        Tmin=(10, 'K'), Tmax=(3000, 'K'), E0=(342.026, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(78.9875, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298, S298 and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(354.121, 'kJ/mol'),
    S298=(270.619, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([50.2858, 55.9027, 59.9243, 62.7499, 66.9165, 69.6877, 73.1807, 75.0595, 76.7195], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(78.9875, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=30,
    label="ONHO(T)",
    molecule="""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 N u0 p1 c0 {1,S} {3,S} {4,S}
3 O u1 p2 c0 {2,S}
4 H u0 p0 c0 {2,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[1.90454, 0.0151069, -1.39704e-05, 6.59807e-09, -1.25459e-12, 31530.2, 16.2771], Tmin=(298, 'K'), Tmax=(1203.84, 'K')),
        NASAPolynomial(coeffs=[4.24618, 0.00732633, -4.27568e-06, 1.22928e-09, -1.39655e-13, 30966.5, 4.54567], Tmin=(1203.84, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(260.764, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(83.1447, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298, S298, and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(271.532, 'kJ/mol'),
    S298=(258.287, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([44.4976, 50.7278, 55.889, 59.8187, 65.7008, 69.8242, 75.3579, 77.9444, 79.8667], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(83.1447, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=31,
    label="HONO(S)",
    molecule="""
1 O u0 p2 c0 {2,S} {4,S}
2 N u0 p1 c0 {1,S} {3,D}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[1.95928, 0.0165219, -1.86802e-05, 1.12647e-08, -2.76569e-12, -10688.8, 14.5546], Tmin=(298, 'K'), Tmax=(948.023, 'K')),
        NASAPolynomial(coeffs=[4.053, 0.00768787, -4.70275e-06, 1.43554e-09, -1.7367e-13, -11085.8, 4.56542], Tmin=(948.023, 'K'), Tmax=(2500, 'K'))],
        Tmin=(298, 'K'), Tmax=(2500, 'K'), E0=(-89.8571, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(83.1447, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from ATcT 1.130
S298 and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(-79.114, 'kJ/mol',),
    S298=(248.643, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([45.8098, 51.9118, 56.401, 59.8886, 65.3399, 69.1903, 74.5339, 77.3021, 79.4347], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(83.1447, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=32,
    label="HONO(T)",
    molecule="""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 N u1 p1 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {4,S}
4 H u0 p0 c0 {3,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[4.36961, 0.00784944, -6.32642e-06, 2.77539e-09, -5.16116e-13, 19098.3, 5.36276], Tmin=(298, 'K'), Tmax=(1133.99, 'K')),
        NASAPolynomial(coeffs=[5.05279, 0.00543966, -3.1389e-06, 9.01486e-10, -1.03e-13, 18943.3, 1.98093], Tmin=(1133.99, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(159.165, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(78.9875, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298, S298, and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(172.096, 'kJ/mol'),
    S298=(268.878, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([51.7719, 55.367, 58.388, 60.9663, 65.0071, 67.8768, 71.9477, 74.1705, 75.8581], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(78.9875, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=33,
    label="cNHOO",
    molecule="""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {3,S}
3 N u0 p1 c0 {1,S} {2,S} {4,S}
4 H u0 p0 c0 {3,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[2.18006, 0.0101071, -9.99705e-07, -6.10893e-09, 3.12219e-12, 31490.7, 14.2407], Tmin=(298, 'K'), Tmax=(906.597, 'K')),
        NASAPolynomial(coeffs=[2.89754, 0.0102555, -6.72828e-06, 2.13559e-09, -2.63145e-13, 31224.4, 10.0985], Tmin=(906.597, 'K'), Tmax=(2500, 'K'))],
        Tmin=(298, 'K'), Tmax=(2500, 'K'), E0=(260.456, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(83.1447, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from ATcT 1.130
S298 and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(270.80, 'kJ/mol'),
    S298=(245.946, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([41.5125, 47.7211, 53.4143, 58.0371, 64.526, 69.0285, 75.0757, 77.7832, 79.7256], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(83.1447, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=34,
    label="HNO2",
    molecule="""
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {2,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.36352, 0.00117404, 1.61593e-05, -2.00675e-08, 7.42513e-12, -6416.82, 8.58965], Tmin=(298, 'K'), Tmax=(839.373, 'K')),
        NASAPolynomial(coeffs=[1.53117, 0.0122918, -7.97211e-06, 2.485e-09, -3.00495e-13, -6193.26, 16.6082], Tmin=(839.373, 'K'), Tmax=(2500, 'K'))],
        Tmin=(298, 'K'), Tmax=(2500, 'K'), E0=(-53.9314, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(83.1447, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from ATcT 1.130
S298 and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(-43.7, 'kJ/mol',),
    S298=(238.267, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([39.0565, 44.1857, 49.4298, 54.2374, 61.6382, 66.7489, 74.0267, 77.2858, 79.2742], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(83.1447, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=35,
    label="NH2OO",
    molecule="""
multiplicity 2
1 N u0 p1 c0 {2,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u1 p2 c0 {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[5.06329, 0.00178829, 1.30223e-05, -1.60113e-08, 5.91685e-12, 17464, 3.91391], Tmin=(298, 'K'), Tmax=(781.35, 'K')),
        NASAPolynomial(coeffs=[3.41401, 0.011041, -6.29449e-06, 1.79609e-09, -2.0499e-13, 17697, 11.3057], Tmin=(781.35, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(145.771, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(103.931, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298, S298, and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(159.125, 'kJ/mol'),
    S298=(280.543, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([53.1439, 58.0059, 63.1178, 67.6716, 75.2266, 81.0401, 90.1727, 94.8317, 97.5783], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(103.931, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=36,
    label="NHOOH",
    molecule="""
multiplicity 2
1 N u1 p1 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {5,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {3,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.9686, 0.00752346, 3.26852e-06, -7.94702e-09, 3.19104e-12, 17806.5, 8.69494], Tmin=(298, 'K'), Tmax=(901.989, 'K')),
        NASAPolynomial(coeffs=[3.41474, 0.0118862, -7.15742e-06, 2.10233e-09, -2.43815e-13, 17828.8, 10.8799], Tmin=(901.989, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(147.99, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'),
        CpInf=(99.7737, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298, S298 and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(160.784, 'kJ/mol'),
    S298=(279.597, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([52.6643, 58.7966, 64.512, 69.4675, 77.4134, 83.2176, 91.5125, 95.3007, 97.5678], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(99.7737, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=37,
    label="HONOH",
    molecule="""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 N u1 p1 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {5,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {3,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[1.95838, 0.0222963, -2.49871e-05, 1.36854e-08, -2.91388e-12, -1458.84, 16.2336], Tmin=(298, 'K'), Tmax=(1121.51, 'K')),
        NASAPolynomial(coeffs=[6.28102, 0.00687946, -4.36772e-06, 1.42876e-09, -1.81778e-13, -2428.44, -5.11647], Tmin=(1121.51, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(-13.3723, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(99.7737, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298, S298, and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(-0.665543, 'kJ/mol',),
    S298=(274.714, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([56.0159, 63.9807, 69.889, 73.9757, 79.7937, 83.6851, 88.8169, 92.008, 94.9841], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(99.7737, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=38,
    label="HONHO",
    molecule="""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u1 p0 c+1 {1,S} {3,S} {4,S}
3 O u0 p2 c0 {2,S} {5,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.15375, 0.0124759, -6.22351e-06, -8.25338e-11, 7.51663e-13, -425.23, 11.4633], Tmin=(298, 'K'), Tmax=(971.537, 'K')),
        NASAPolynomial(coeffs=[3.93071, 0.0109678, -6.5057e-06, 1.90246e-09, -2.2008e-13, -655.996, 7.32673], Tmin=(971.537, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(-4.09814, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(103.931, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298, S298, and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(8.4295, 'kJ/mol'),
    S298=(273.32, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([52.7627, 59.4919, 65.484, 70.5636, 78.2241, 83.772, 91.9519, 95.8949, 98.3354], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(103.931, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=39,
    label="NH2OOH",
    molecule="""
1 N u0 p1 c0 {2,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[2.61743, 0.0236206, -2.47082e-05, 1.36895e-08, -3.07366e-12, 9.04537, 12.8721], Tmin=(298, 'K'), Tmax=(1031.66, 'K')),
        NASAPolynomial(coeffs=[5.82677, 0.0111774, -6.61631e-06, 1.99849e-09, -2.40625e-13, -653.149, -2.71116], Tmin=(1031.66, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(-0.518348, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'),
        CpInf=(124.717, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298, S298 and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(13.6809, 'kJ/mol'),
    S298=(281.365, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([64.8742, 74.4339, 81.2311, 86.6305, 95.1346, 101.229, 110.054, 114.982, 118.626], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(124.717, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=40,
    label="N2O",
    molecule="""
1 N u0 p2 c-1 {2,D}
2 N u0 p0 c+1 {1,D} {3,D}
3 O u0 p2 c0 {2,D}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[2.88536, 0.00650105, -2.19073e-06, -1.54076e-09, 9.45436e-13, 8807.07, 8.16589], Tmin=(298, 'K'), Tmax=(976.024, 'K')),
        NASAPolynomial(coeffs=[3.16776, 0.00667377, -4.5003e-06, 1.433e-09, -1.73897e-13, 8688.59, 6.48576], Tmin=(976.024, 'K'), Tmax=(2500, 'K'))],
        Tmin=(298, 'K'), Tmax=(2500, 'K'), E0=(72.8193, 'kJ/mol'), Cp0=(29.1007, 'J/(mol*K)'), CpInf=(62.3585, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from ATcT 1.130
S298 and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(82.593, 'kJ/mol'),
    S298=(219.771, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([38.2555, 42.1148, 45.4102, 48.0968, 52.1693, 54.9117, 58.3067, 59.7901, 60.9366], 'J/(mol*K)'),
    Cp0=(29.1007, 'J/(mol*K)'),
    CpInf=(62.3585, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=41,
    label="cNNO",
    molecule="""
1 N u0 p1 c0 {2,D} {3,S}
2 N u0 p1 c0 {1,D} {3,S}
3 O u0 p2 c0 {1,S} {2,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.81887, 0.00590123, -5.04223e-06, 2.16668e-09, -3.76745e-13, 40723.6, 5.75776], Tmin=(298, 'K'), Tmax=(1272.54, 'K')),
        NASAPolynomial(coeffs=[4.63318, 0.00334175, -2.02543e-06, 5.86315e-10, -6.62876e-14, 40516.3, 1.63289], Tmin=(1272.54, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(338.532, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(58.2013, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from ATcT 1.130
S298 and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(349.9, 'kJ/mol'),
    S298=(241.679, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([43.1403, 45.8127, 47.8349, 49.5288, 52.11, 53.8461, 55.9649, 56.8226, 57.4447], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(58.2013, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=42,
    label="HNNO",
    molecule="""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u1 p0 c+1 {1,S} {3,D}
3 N u0 p1 c0 {2,D} {4,S}
4 H u0 p0 c0 {3,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.22652, 0.00193049, 1.7626e-05, -2.24845e-08, 8.32227e-12, 23851.3, 10.2175], Tmin=(298, 'K'), Tmax=(856.031, 'K')),
        NASAPolynomial(coeffs=[1.17257, 0.0145893, -9.91965e-06, 3.14513e-09, -3.82762e-13, 24090.8, 19.1523], Tmin=(856.031, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(197.615, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(78.9875, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298, S298, and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

Did not use a "fine" DFT grid

ThermoData(
    H298=(207.975, 'kJ/mol'),
    S298=(247.566, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([40.4359, 46.4029, 52.4379, 57.9053, 66.1002, 71.4701, 78.3416, 80.6907, 81.9072], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(78.9875, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=43,
    label="NNHO",
    molecule="""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,D} {4,S}
3 N u1 p1 c0 {2,D}
4 H u0 p0 c0 {2,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.00442, 0.0049756, 7.77865e-06, -1.25513e-08, 4.94409e-12, 36667.9, 11.2157], Tmin=(298, 'K'), Tmax=(868.824, 'K')),
        NASAPolynomial(coeffs=[2.26136, 0.0109524, -6.95253e-06, 2.13807e-09, -2.56942e-13, 36700.5, 14.1409], Tmin=(868.824, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(304.083, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(83.1447, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298, S298, and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(314.539, 'kJ/mol'),
    S298=(249.927, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([40.7911, 46.1714, 51.3893, 55.9525, 62.8104, 67.6941, 74.5841, 77.6688, 79.5715], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(83.1447, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=44,
    label="NH2NO",
    molecule="""
1 O u0 p2 c0 {3,D}
2 N u0 p1 c0 {3,S} {4,S} {5,S}
3 N u0 p1 c0 {1,D} {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.45286, 0.0131475, -9.05272e-06, 3.31346e-09, -5.10648e-13, 7613.55, 8.05399], Tmin=(298, 'K'), Tmax=(1332.32, 'K')),
        NASAPolynomial(coeffs=[4.60865, 0.00967739, -5.14586e-06, 1.35852e-09, -1.43812e-13, 7305.58, 2.14637], Tmin=(1332.32, 'K'), Tmax=(2500, 'K'))],
        Tmin=(298, 'K'), Tmax=(2500, 'K'), E0=(63.1087, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(103.931, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from ATcT 1.130
S298 and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(76.10, 'kJ/mol'),
    S298=(259.989, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([55.486, 62.0136, 67.6695, 72.5677, 80.4224, 86.1879, 94.7048, 99.1279, 102.066], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(103.931, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=45,
    label="N2H3O",
    molecule="""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u1 p0 c+1 {1,S} {3,S} {4,S}
3 N u0 p1 c0 {2,S} {5,S} {6,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[2.61874, 0.0151368, -3.93849e-06, -4.15926e-09, 2.28086e-12, 16472.1, 14.1009], Tmin=(298, 'K'), Tmax=(962.397, 'K')),
        NASAPolynomial(coeffs=[2.931, 0.0165316, -1.03091e-05, 3.1609e-09, -3.75867e-13, 16287.3, 11.9586], Tmin=(962.397, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(136.062, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(128.874, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298, S298, and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(148.685, 'kJ/mol'),
    S298=(277.07, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([55.7533, 65.2439, 73.4606, 80.4352, 91.4434, 99.3367, 110.622, 116.589, 120.949], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(128.874, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=46,
    label="NH2NOH",
    molecule="""
multiplicity 2
1 N u0 p1 c0 {2,S} {4,S} {5,S}
2 N u1 p1 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[1.81948, 0.0227117, -1.62501e-05, 3.7015e-09, 3.93916e-13, 15285.7, 17.1085], Tmin=(298, 'K'), Tmax=(1014.83, 'K')),
        NASAPolynomial(coeffs=[4.82741, 0.0146562, -9.96086e-06, 3.2601e-09, -4.06393e-13, 14479.5, 1.58854], Tmin=(1014.83, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(125.651, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(124.717, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298, S298, and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

NH2 rotor scan not smooth, need to consider a strongly-coupled inversion mode (OH rotor is smooth)

ThermoData(
    H298=(138.856, 'kJ/mol'),
    S298=(278.986, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([60.4127, 71.2073, 80.0224, 86.7586, 96.5672, 103.071, 111.093, 115.157, 118.883], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(124.717, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=47,
    label="NH2ONH2",
    molecule="""
1 N u0 p1 c0 {2,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {3,S}
3 N u0 p1 c0 {2,S} {6,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[1.80874, 0.030058, -3.0821e-05, 1.63883e-08, -3.46868e-12, 14264.7, 14.6239], Tmin=(298, 'K'), Tmax=(1110.21, 'K')),
        NASAPolynomial(coeffs=[6.68631, 0.0124862, -7.08202e-06, 2.13462e-09, -2.59313e-13, 13181.5, -9.41792], Tmin=(1110.21, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(117.423, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(149.66, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298, S298, and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(132.176, 'kJ/mol'),
    S298=(271.509, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([70.0806, 82.3798, 91.4104, 98.1337, 108.669, 116.326, 127.924, 135.008, 140.345], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(149.66, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=48,
    label="N2O2",
    molecule="""
1 O u0 p2 c0 {2,D}
2 N u0 p1 c0 {1,D} {3,S}
3 N u0 p1 c0 {2,S} {4,D}
4 O u0 p2 c0 {3,D}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.66063, 0.0236523, -4.07459e-05, 3.20989e-08, -9.57389e-12, 18746.6, 6.81545], Tmin=(298, 'K'), Tmax=(829.986, 'K')),
        NASAPolynomial(coeffs=[8.16, 0.00196827, -1.55749e-06, 6.21844e-10, -9.27433e-14, 17999.7, -14.053], Tmin=(829.986, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(156.24, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(78.9875, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from ATcT 1.130  ###**** note trans
S298 and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

This is cis-N2O2, trans-N2O2 is higher in energy.

ThermoData(
    H298=(171.17, 'kJ/mol'),
    S298=(275.823, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([65.2315, 70.4384, 72.3074, 73.4635, 75.0276, 75.8914, 76.7608, 77.6623, 78.6564], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(78.9875, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=49,
    label="NNO2(S)",
    molecule="""
multiplicity 1
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 N u0 p2 c0 {2,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[2.50564, 0.0155584, -1.31038e-05, 4.49117e-09, -3.52952e-13, 43468.3, 13.3739], Tmin=(298, 'K'), Tmax=(1035.33, 'K')),
        NASAPolynomial(coeffs=[4.93254, 0.0084082, -5.96988e-06, 1.97431e-09, -2.46694e-13, 42846.4, 1.00507], Tmin=(1035.33, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(360.432, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(83.1447, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298, S298, and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(372.479, 'kJ/mol'),
    S298=(263.92, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([50.7842, 57.5314, 62.8916, 66.8341, 72.3365, 75.769, 79.3031, 80.6367, 82.0467], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(83.1447, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=50,
    label="NNO2(T)",
    molecule="""
multiplicity 3
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 N u2 p1 c0 {2,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[0.928089, 0.0221956, -2.64351e-05, 1.50117e-08, -3.31969e-12, 54155, 20.9565], Tmin=(298, 'K'), Tmax=(1073.88, 'K')),
        NASAPolynomial(coeffs=[5.06166, 0.0067988, -4.92872e-06, 1.66049e-09, -2.11512e-13, 53267.2, 0.719806], Tmin=(1073.88, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(448.368, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(83.1447, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298, S298, and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(459.058, 'kJ/mol'),
    S298=(264.486, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([46.4353, 53.6931, 59.0586, 62.5326, 67.1378, 69.9115, 72.4426, 73.248, 74.5276], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(83.1447, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=51,
    label="cNNOO",
    molecule="""
1 N u0 p1 c0 {2,D} {4,S}
2 N u0 p1 c0 {1,D} {3,S}
3 O u0 p2 c0 {2,S} {4,S}
4 O u0 p2 c0 {1,S} {3,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[0.879853, 0.0200966, -1.76664e-05, 6.12703e-09, -3.76974e-13, 40894.5, 19.9361], Tmin=(298, 'K'), Tmax=(974.474, 'K')),
        NASAPolynomial(coeffs=[4.18491, 0.0098391, -6.9706e-06, 2.29439e-09, -2.87694e-13, 40093.3, 3.27042], Tmin=(974.474, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(337.797, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(83.1447, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298, S298, and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(348.419, 'kJ/mol'),
    S298=(251.15, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([45.6698, 53.7324, 60.4607, 65.3245, 71.5521, 75.4741, 79.513, 80.6773, 81.9097], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(83.1447, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=52,
    label="NNOO",
    molecule="""
1 O u0 p3 c-1 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 N u0 p0 c+1 {2,S} {4,T}
4 N u0 p1 c0 {3,T}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.16972, 0.0170209, -2.04409e-05, 1.22897e-08, -2.93466e-12, 52048.4, 10.3229], Tmin=(298, 'K'), Tmax=(986.204, 'K')),
        NASAPolynomial(coeffs=[5.77709, 0.00644552, -4.35586e-06, 1.4163e-09, -1.7827e-13, 51534.1, -2.21987], Tmin=(986.204, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(432.488, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(83.1447, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298, S298, and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(445.583, 'kJ/mol'),
    S298=(271.454, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([55.9283, 61.9728, 65.8443, 68.7548, 73.0924, 75.909, 79.181, 80.6562, 81.9262], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(83.1447, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=53,
    label="ON2HO",
    molecule="""
multiplicity 2
1 N u0 p2 c-1 {2,S} {4,S}
2 N u0 p0 c+1 {1,S} {3,D} {5,S}
3 O u0 p2 c0 {2,D}
4 O u1 p2 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[2.31754, 0.0224442, -2.28344e-05, 1.16035e-08, -2.34034e-12, 20421, 14.2186], Tmin=(298, 'K'), Tmax=(1151.41, 'K')),
        NASAPolynomial(coeffs=[6.03495, 0.00953069, -6.01227e-06, 1.86404e-09, -2.25777e-13, 19564.9, -4.24011], Tmin=(1151.41, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(168.856, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(103.931, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298, S298, and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(182.324, 'kJ/mol'),
    S298=(275.991, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([60.3896, 69.4949, 76.1488, 80.9942, 88.2759, 93.1974, 99.4702, 102.51, 104.799], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(103.931, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=54,
    label="NHNO2",
    molecule="""
multiplicity 2
1 N u0 p2 c-1 {2,S} {5,S}
2 N u0 p0 c+1 {1,S} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 O u1 p2 c0 {2,S}
5 H u0 p0 c0 {1,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[2.39923, 0.0200345, -1.88548e-05, 8.79795e-09, -1.62817e-12, 26925, 15.3856], Tmin=(298, 'K'), Tmax=(1239.55, 'K')),
        NASAPolynomial(coeffs=[5.75626, 0.00920116, -5.74483e-06, 1.74683e-09, -2.06016e-13, 26092.8, -1.53095], Tmin=(1239.55, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(222.922, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(103.931, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298, S298, and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(235.963, 'kJ/mol'),
    S298=(284.868, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([57.5536, 66.0476, 72.4724, 77.3203, 84.6212, 89.5173, 95.5916, 98.4055, 100.723], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(103.931, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=55,
    label="NH2NO2",
    molecule="""
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 N u0 p1 c0 {2,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[1.67634, 0.0247611, -2.09598e-05, 8.57821e-09, -1.28769e-12, -696.412, 16.7862], Tmin=(298, 'K'), Tmax=(1058.83, 'K')),
        NASAPolynomial(coeffs=[5.14237, 0.0137643, -8.35169e-06, 2.5102e-09, -2.96596e-13, -1547.94, -0.688597], Tmin=(1058.83, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(-7.27489, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(128.874, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298, S298, and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(6.10281, 'kJ/mol'),
    S298=(273.195, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([61.8202, 72.8238, 81.6939, 88.5763, 99.063, 106.359, 116.211, 121.182, 124.806], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(128.874, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=56,
    label="NH2ONO",
    molecule="""
1 N u0 p1 c0 {2,S} {5,S} {6,S}
2 O u0 p2 c0 {1,S} {3,S}
3 N u0 p1 c0 {2,S} {4,D}
4 O u0 p2 c0 {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.69674, 0.0260916, -3.41614e-05, 2.4219e-08, -6.95122e-12, 10037.2, 6.9044], Tmin=(298, 'K'), Tmax=(828.998, 'K')),
        NASAPolynomial(coeffs=[6.8686, 0.0107868, -6.46826e-06, 1.94821e-09, -2.34931e-13, 9511.29, -7.80306], Tmin=(828.998, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(83.8728, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(124.717, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298, S298, and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(100.11, 'kJ/mol'),
    S298=(286.213, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([75.0041, 83.8873, 89.5976, 94.3951, 101.983, 107.451, 115.376, 119.564, 122.174], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(124.717, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=57,
    label="HON2HO",
    molecule="""
1 O u0 p2 c0 {2,S} {5,S}
2 N u0 p1 c0 {1,S} {3,S} {6,S}
3 N u0 p1 c0 {2,S} {4,D}
4 O u0 p2 c0 {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[4.61618, 0.0204155, -2.21054e-05, 1.38771e-08, -3.71661e-12, 4136.34, 4.0168], Tmin=(298, 'K'), Tmax=(847.47, 'K')),
        NASAPolynomial(coeffs=[6.40216, 0.0119858, -7.18519e-06, 2.14008e-09, -2.54263e-13, 3833.63, -4.30397], Tmin=(847.47, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(35.3116, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(124.717, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298, S298, and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(51.9577, 'kJ/mol'),
    S298=(295.438, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([75.5257, 83.6505, 89.6652, 94.8391, 103.05, 108.986, 117.558, 121.937, 124.669], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(124.717, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=58,
    label="NH2cNOO",
    molecule="""
1 N u0 p1 c0 {2,S} {5,S} {6,S}
2 N u0 p1 c0 {1,S} {3,S} {4,S}
3 O u0 p2 c0 {2,S} {4,S}
4 O u0 p2 c0 {2,S} {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[1.69222, 0.0259304, -2.11989e-05, 7.26543e-09, -6.1547e-13, 36689.8, 17.7734], Tmin=(298, 'K'), Tmax=(1055.81, 'K')),
        NASAPolynomial(coeffs=[5.64972, 0.0144395, -9.84922e-06, 3.2407e-09, -4.06394e-13, 35658.9, -2.45859], Tmin=(1055.81, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(303.582, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(128.874, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298, S298, and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(317.384, 'kJ/mol'),
    S298=(284.879, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([64.2108, 76.0259, 85.3891, 92.3074, 102.233, 108.783, 116.805, 120.863, 124.452], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(128.874, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=59,
    label="cNH2NOO",
    molecule="""
1 N u0 p2 c-1 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {4,S}
4 N u0 p0 c+1 {1,S} {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.48869, 0.0199535, -1.71324e-05, 8.19759e-09, -1.67381e-12, 17124.6, 8.97348], Tmin=(298, 'K'), Tmax=(1055.14, 'K')),
        NASAPolynomial(coeffs=[5.24908, 0.01328, -7.64561e-06, 2.20372e-09, -2.53682e-13, 16753.1, 0.386112], Tmin=(1055.14, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(142.395, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'),
        CpInf=(133.032, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298, S298 and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(157.264, 'kJ/mol'),
    S298=(283.551, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([67.5995, 76.7805, 83.8985, 90.0255, 99.7949, 106.91, 117.332, 122.811, 126.515], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(133.032, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=60,
    label="NH2NO2H",
    molecule="""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u1 p0 c+1 {1,S} {3,S} {4,S}
3 O u0 p2 c0 {2,S} {5,S}
4 N u0 p1 c0 {2,S} {6,S} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.84914, 0.0251024, -2.99752e-05, 2.18474e-08, -6.75647e-12, 8162.18, 9.26855], Tmin=(298, 'K'), Tmax=(756.898, 'K')),
        NASAPolynomial(coeffs=[5.98752, 0.0138016, -7.57973e-06, 2.12182e-09, -2.41199e-13, 7838.47, -0.452322], Tmin=(756.898, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(68.3432, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(149.66, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298, S298, and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(84.8018, 'kJ/mol'),
    S298=(312.012, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([76.5726, 85.8304, 93.2681, 99.4322, 109.396, 117.217, 129.571, 136.123, 140.23], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(149.66, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=61,
    label="N2H3OO",
    molecule="""
multiplicity 2
1 N u0 p1 c0 {2,S} {5,S} {6,S}
2 N u0 p1 c0 {1,S} {3,S} {7,S}
3 O u0 p2 c0 {2,S} {4,S}
4 O u1 p2 c0 {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.17919, 0.021183, -1.41801e-05, 4.69103e-09, -5.69292e-13, 26641.8, 13.584], Tmin=(298, 'K'), Tmax=(1127.37, 'K')),
        NASAPolynomial(coeffs=[4.95718, 0.0160167, -8.82585e-06, 2.42348e-09, -2.65735e-13, 26168.4, 4.47117], Tmin=(1127.37, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(221.161, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(153.818, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298, S298, and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(236.245, 'kJ/mol'),
    S298=(311.122, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([69.7485, 80.35, 89.5262, 97.4326, 110.011, 119.143, 132.462, 139.517, 144.458], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(153.818, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=62,
    label="NO3",
    molecule="""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 O u1 p2 c0 {2,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[2.4283, 0.0165038, -1.45483e-05, 5.41129e-09, -5.80254e-13, 7579.69, 12.7513], Tmin=(298, 'K'), Tmax=(1046.36, 'K')),
        NASAPolynomial(coeffs=[5.14525, 0.00833799, -6.02541e-06, 2.00922e-09, -2.51978e-13, 6889.55, -1.06038], Tmin=(1046.36, 'K'), Tmax=(2500, 'K'))],
        Tmin=(298, 'K'), Tmax=(2500, 'K'), E0=(61.9905, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(83.1447, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from ATcT 1.130
S298 and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//wB97xd/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(74.15, 'kJ/mol'),
    S298=(256.953, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([51.6024, 58.5626, 64.0258, 67.9827, 73.425, 76.7446, 79.9253, 80.9943, 82.2969], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(83.1447, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=63,
    label="HNO3",
    molecule="""
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 O u0 p2 c0 {2,S} {5,S}
5 H u0 p0 c0 {4,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[0.575295, 0.0267557, -2.74413e-05, 1.39498e-08, -2.82692e-12, -17282.9, 21.916], Tmin=(298, 'K'), Tmax=(1138.23, 'K')),
        NASAPolynomial(coeffs=[4.84502, 0.0117508, -7.66705e-06, 2.36787e-09, -2.83044e-13, -18254.9, 0.764279], Tmin=(1138.23, 'K'), Tmax=(2500, 'K'))],
        Tmin=(298, 'K'), Tmax=(2500, 'K'), E0=(-145.815, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(103.931, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from ATcT 1.130
S298 and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(-134.19, 'kJ/mol',),
    S298=(266.61, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([53.8927, 64.2395, 72.1265, 77.865, 86.3276, 91.8509, 98.0493, 100.203, 102.028], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(103.931, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=64,
    label="N2O3",
    molecule="""
1 O u0 p2 c0 {2,D}
2 N u0 p1 c0 {1,D} {3,S}
3 N u0 p0 c+1 {2,S} {4,D} {5,S}
4 O u0 p2 c0 {3,D}
5 O u0 p3 c-1 {3,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[5.00769, 0.0152729, -1.237e-05, 3.97118e-09, -2.18399e-13, 8297.22, 3.71118], Tmin=(298, 'K'), Tmax=(1009.43, 'K')),
        NASAPolynomial(coeffs=[7.15172, 0.00891867, -6.11032e-06, 1.93899e-09, -2.35681e-13, 7755.25, -7.19314], Tmin=(1009.43, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(69.3822, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(103.931, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from ATcT 1.130
S298 and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(86.19, 'kJ/mol'),
    S298=(301.625, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([71.3756, 78.1566, 83.3362, 87.5559, 93.6235, 97.2848, 100.678, 101.762, 103.133], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(103.931, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=65,
    label="ONONO2",
    molecule="""
1 O u0 p2 c0 {2,D}
2 N u0 p1 c0 {1,D} {3,S}
3 O u0 p2 c0 {2,S} {4,S}
4 N u0 p0 c+1 {3,S} {5,D} {6,S}
5 O u0 p2 c0 {4,D}
6 O u0 p3 c-1 {4,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[5.19485, 0.0183156, -1.07462e-05, -2.2203e-10, 1.56645e-12, 2592.18, 6.65451], Tmin=(298, 'K'), Tmax=(958.431, 'K')),
        NASAPolynomial(coeffs=[7.28082, 0.0134838, -9.24703e-06, 2.95239e-09, -3.61617e-13, 2014.4, -4.24875], Tmin=(958.431, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(21.8782, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(128.874, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from ATcT 1.130
S298 and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(40.4, 'kJ/mol'),
    S298=(342.823, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([80.9957, 90.0269, 97.4832, 103.57, 112.362, 117.726, 122.947, 124.886, 127.157], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(128.874, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=66,
    label="N2O4",
    molecule="""
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 N u0 p0 c+1 {2,S} {5,D} {6,S}
5 O u0 p2 c0 {4,D}
6 O u0 p3 c-1 {4,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[2.9869, 0.0298811, -3.15564e-05, 1.65055e-08, -3.46588e-12, -658.459, 11.8976], Tmin=(298, 'K'), Tmax=(1084.54, 'K')),
        NASAPolynomial(coeffs=[7.25107, 0.0141542, -9.80502e-06, 3.13503e-09, -3.8386e-13, -1583.4, -9.02068], Tmin=(1084.54, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(-5.68565, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(128.874, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298 from ATcT 1.130
S298 and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(10.90, 'kJ/mol'),
    S298=(303.947, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([79.1064, 90.4791, 98.8874, 105.076, 114.023, 119.651, 125.257, 126.617, 127.94], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(128.874, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=67,
    label="HONHOO",
    molecule="""
multiplicity 2
1 O u0 p2 c0 {2,S} {5,S}
2 N u0 p1 c0 {1,S} {3,S} {6,S}
3 O u0 p2 c0 {2,S} {4,S}
4 O u1 p2 c0 {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.61112, 0.02141, -1.84195e-05, 7.49572e-09, -1.11347e-12, 11736.3, 10.9168], Tmin=(298, 'K'), Tmax=(1059.15, 'K')),
        NASAPolynomial(coeffs=[6.59936, 0.0119468, -7.59809e-06, 2.30869e-09, -2.72541e-13, 11001.1, -4.15401], Tmin=(1059.15, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(97.1849, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(124.717, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298, S298, and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(113.2, 'kJ/mol'),
    S298=(308.599, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([71.316, 80.4555, 87.9384, 93.9811, 102.589, 107.921, 115.011, 118.13, 119.853], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(124.717, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=68,
    label="N2(T)",
    molecule="""
multiplicity 3
1 N u1 p1 c0 {2,D}
2 N u1 p1 c0 {1,D}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[3.47977, -0.000833406, 4.88592e-06, -5.03344e-09, 1.68853e-12, 85808.9, 4.68385], Tmin=(298, 'K'), Tmax=(794.109, 'K')),
        NASAPolynomial(coeffs=[2.78528, 0.00266559, -1.72486e-06, 5.17673e-10, -5.94616e-14, 85919.1, 7.87409], Tmin=(794.109, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(713.406, 'kJ/mol'), Cp0=(29.1007, 'J/(mol*K)'), CpInf=(37.4151, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298, S298, and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(722.052, 'kJ/mol'),
    S298=(203.172, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([29.5168, 30.3084, 31.2694, 32.209, 33.7077, 34.7754, 36.1697, 36.6361, 36.8816], 'J/(mol*K)'),
    Cp0=(29.1007, 'J/(mol*K)'),
    CpInf=(37.4151, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=69,
    label="ONNOH",
    molecule="""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 N u0 p1 c0 {1,D} {3,S}
3 N u1 p1 c0 {2,S} {4,S}
4 O u0 p2 c0 {3,S} {5,S}
5 H u0 p0 c0 {4,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[1.57406, 0.0271331, -3.0653e-05, 1.64652e-08, -3.42209e-12, 19803.9, 17.4663], Tmin=(298, 'K'), Tmax=(1145.48, 'K')),
        NASAPolynomial(coeffs=[7.04557, 0.00802583, -5.631e-06, 1.90185e-09, -2.43505e-13, 18550.4, -9.67349], Tmin=(1145.48, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(163.182, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(103.931, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298, S298, and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(176.584, 'kJ/mol'),
    S298=(276.847, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([61.2006, 70.7642, 77.6968, 82.3375, 88.6597, 92.5377, 96.5616, 98.5866, 100.985], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(103.931, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=70,
    label="ONOOH",
    molecule="""
1 O u0 p2 c0 {2,D}
2 N u0 p1 c0 {1,D} {3,S}
3 O u0 p2 c0 {2,S} {4,S}
4 O u0 p2 c0 {3,S} {5,S}
5 H u0 p0 c0 {4,S}
""",
    thermo=NASA(polynomials=[
        NASAPolynomial(coeffs=[4.81291, 0.0213907, -4.36423e-05, 5.23029e-08, -2.5312e-11, -3267.49, 2.58069], Tmin=(298, 'K'), Tmax=(505.037, 'K')),
        NASAPolynomial(coeffs=[6.44835, 0.00843815, -5.17384e-06, 1.52501e-09, -1.77204e-13, -3432.69, -4.19219], Tmin=(505.037, 'K'), Tmax=(3000, 'K'))],
        Tmin=(298, 'K'), Tmax=(3000, 'K'), E0=(-26.2881, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(99.7737, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298, S298, and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

ThermoData(
    H298=(-9.78789, 'kJ/mol',),
    S298=(289.746, 'J/(mol*K)'),
    Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500], 'K'),
    Cpdata=([70.7469, 75.546, 79.4249, 82.7731, 88.1058, 91.9644, 97.3891, 99.7385, 100.755], 'J/(mol*K)'),
    Cp0=(33.2579, 'J/(mol*K)'),
    CpInf=(99.7737, 'J/(mol*K)'),
    Tmin=(298, 'K'),
    Tmax=(3000, 'K'),
)
""",
)

entry(
    index=71,
    label="NH3N",
    molecule="""
multiplicity 2
1 N u0 p0 c+1 {2,S} {3,S} {4,S} {5,S}
2 N u1 p2 c-1 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo=NASA(polynomials=[
            NASAPolynomial(coeffs=[4.05422, -0.00474258, 4.75668e-05, -7.5359e-08, 4.1191e-11, 55593.2, 5.44064], Tmin=(10, 'K'), Tmax=(465.109, 'K')),
            NASAPolynomial(coeffs=[2.11876, 0.0119021, -6.11171e-06, 1.57914e-09, -1.62693e-13, 55773.3, 13.2966], Tmin=(465.109, 'K'), Tmax=(3000, 'K'))],
        Tmin=(10, 'K'), Tmax=(3000, 'K'), E0=(462.229, 'kJ/mol'), Cp0=(33.2579, 'J/(mol*K)'), CpInf=(108.088, 'J/(mol*K)')),
    shortDesc=u"""""",
    longDesc=u"""
H298, S298, and Cp from a 1DHR RRHO CCSD(T)-F12/cc-pVTZ-F12//B2PLYPD3/aug-cc-pVTZ level of theory computation

Enthalpy of formation (298 K)   =   113.035 kcal/mol
Entropy of formation (298 K)    =    56.940 cal/(mol*K)
=========== =========== =========== =========== ===========
Temperature Heat cap.   Enthalpy    Entropy     Free energy
(K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
=========== =========== =========== =========== ===========
       300      10.356     113.055      57.009      95.953
       400      11.922     114.170      60.204      90.088
       500      13.372     115.436      63.023      83.924
       600      14.665     116.839      65.577      77.492
       800      16.833     119.997      70.106      63.913
      1000      18.532     123.541      74.052      49.489
      1500      21.316     133.574      82.151      10.349
      2000      22.865     144.654      88.515     -32.375
      2400      23.673     153.970      92.759     -68.651
=========== =========== =========== =========== ===========
""",
)
