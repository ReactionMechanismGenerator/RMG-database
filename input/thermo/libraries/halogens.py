#!/usr/bin/env python
# encoding: utf-8

name = "halogens"
shortDesc = "halogens small molecules"
longDesc = """
This is a WIP library with small halogenated species
This libary should be used for F/Cl/Br-containing systems
"""
entry(
    index = 0,
    label = "CCHF",
    molecule = 
"""
1 C u0 p1 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), 
    Cpdata=([53.9106,58.1472,61.299,63.8388,68.1495,71.6867,76.6116],'J/(mol*K)'), 
    H298=(300.1,'kJ/mol'), S298=(246.826,'J/(mol*K)'), Cp0=(33.2579,'J/(mol*K)'), 
    CpInf=(83.1447,'J/(mol*K)')),
    shortDesc = """GA + ATcT 1.122p 70302-00-0*0 H298""",
    longDesc = 
"""
H298 = 300.1 kJ/mol
""",
)

entry(
    index = 1,
    label = "CCF2",
    molecule = 
"""
1 C u0 p1 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}
""",
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), 
    Cpdata=([62.2121,66.8883,69.8504,71.9626,75.5195,78.4131,80.7894],'J/(mol*K)'), 
    H298=(130.6,'kJ/mol'), S298=(259.54,'J/(mol*K)'), Cp0=(33.2579,'J/(mol*K)'), 
    CpInf=(83.1447,'J/(mol*K)')),
    shortDesc = """GA + ATcT 1.122p 41895-33-4*0 H298""",
    longDesc = 
"""
H298 = 130.6 kJ/mol
""",
)

entry(
    index = 2,
    label = "CCBr2",
    molecule = 
"""
1 C u0 p1 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 Br u0 p3 c0 {2,S}
4 Br u0 p3 c0 {2,S}
""",
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), 
    Cpdata=([72.2886,75.7863,76.9547,77.4615,79.7599,82.7872,82.4281],'J/(mol*K)'), 
    H298=(498.9,'kJ/mol'), S298=(304.88,'J/(mol*K)'), Cp0=(33.2579,'J/(mol*K)'), 
    CpInf=(83.1447,'J/(mol*K)')),
    shortDesc = """GA + ATcT 1.122p 261771-36-2*0 H298""",
    longDesc = 
"""
H298 = 498.9 kJ/mol
""",
)

entry(
    index = 3,
    label = "CCHBr",
    molecule = 
"""
1 C u0 p1 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 Br u0 p3 c0 {2,S}
""",
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), 
    Cpdata=([57.9599,61.9054,64.5072,66.5253,70.3786,73.8408,77.4814],'J/(mol*K)'), 
    H298=(460.1,'kJ/mol'), S298=(269.119,'J/(mol*K)'), Cp0=(33.2579,'J/(mol*K)'), 
    CpInf=(83.1447,'J/(mol*K)')),
    shortDesc = """GA + ATcT 1.122p 161957-27-3*0 H298""",
    longDesc = 
"""
H298 = 460.1 kJ/mol
""",
)

entry(
    index = 4,
    label = "CCHCl",
    molecule = 
"""
1 C u0 p1 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 Cl u0 p3 c0 {2,S}
""",
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'),
    Cpdata=([56.7425,60.9627,63.8772,66.1233,70.0187,73.3222,77.3704],'J/(mol*K)'),
    H298=(429.8,'kJ/mol'), S298=(257.32,'J/(mol*K)'), Cp0=(33.2579,'J/(mol*K)'),
    CpInf=(83.1447,'J/(mol*K)')),
    shortDesc = """GA + ATcT 1.122p 70277-82-6*0 H298""",
    longDesc = 
"""
H298 = 429.8 kJ/mol
""",
)

entry(
    index = 5,
    label = "CCCl2",
    molecule = 
"""
1 C u0 p1 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 Cl u0 p3 c0 {2,S}
4 Cl u0 p3 c0 {2,S}
""",
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'),
    Cpdata=([68.8108,73.1302,75.2712,76.546,79.2441,81.9894,82.7851],'J/(mol*K)'),
    H298=(424.8,'kJ/mol'), S298=(281.351,'J/(mol*K)'), Cp0=(33.2579,'J/(mol*K)'),
    CpInf=(83.1447,'J/(mol*K)')),
    shortDesc = """GA + ATcT 1.122p 70277-82-6*0 H298""",
    longDesc = 
"""
H298 = 424.8 kJ/mol
""",
)

entry(
    index = 6,
    label = "OOBr",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 O  u1 p2 c0 {2,S}
""",
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), 
    Cpdata=([51.8844,52.5941,51.888,50.7367,49.4281,50.2226,52.5304],'J/(mol*K)'), 
    H298=(109.2,'kJ/mol'), S298=(275.814,'J/(mol*K)'), 
    Cp0=(33.2579,'J/(mol*K)'), CpInf=(58.2013,'J/(mol*K)')),
    shortDesc = """GA + ATcT 1.122p 67177-47-3*0 H298""",
    longDesc = 
"""
H298 = 109.2 kJ/mol
""",
)

entry(
    index = 7,
    label = "OOCl",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 O  u1 p2 c0 {2,S}
""",
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), 
    Cpdata=([50.6312,51.4088,50.9024,49.9987,49.104,50.0514,52.3303],'J/(mol*K)'), 
    H298=(102.82,'kJ/mol'), S298=(267.489,'J/(mol*K)'), Cp0=(33.2579,'J/(mol*K)'), 
    CpInf=(58.2013,'J/(mol*K)')),
    shortDesc = """GA + ATcT 1.122p 17376-09-9*0 H298""",
    longDesc = 
"""
H298 = 102.82 kJ/mol
""",
)

entry(
    index = 8,
    label = "OOF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u1 p2 c0 {2,S}
""",
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), 
    Cpdata=([43.4949,45.0513,46.0077,46.7044,48.1531,50.0169,53.7856],'J/(mol*K)'), 
    H298=(25.10,'kJ/mol'), S298=(255.854,'J/(mol*K)'), Cp0=(33.2579,'J/(mol*K)'), 
    CpInf=(58.2013,'J/(mol*K)')),
    shortDesc = """GA + ATcT 1.122p 15499-23-7*0 H298""",
    longDesc = 
"""
H298 = 25.10 kJ/mol
""",
)

entry(
    index = 9,
    label = "CF2",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {3,S}
3 C u0 p1 c0 {1,S} {2,S}
""",
    thermo = NASA(polynomials=
    [NASAPolynomial(coeffs=[2.28591,0.0107608,-1.05382e-05,4.89881e-09,-8.86384e-13,-24340.7,13.1348], 
    Tmin=(298,'K'), Tmax=(1300,'K')), 
    NASAPolynomial(coeffs=[5.33121,0.00197748,-9.60248e-07,2.10704e-10,-1.5954e-14,-25190.9,-2.56367], 
    Tmin=(1300,'K'), Tmax=(3000,'K'))], Tmin=(298,'K'), Tmax=(3000,'K'), Cp0=(33.2579,'J/mol/K'), CpInf=(58.2013,'J/mol/K')),
    shortDesc = u"""78ROD71STUPRO + H298 from ATcT version 1.122p""",
    longDesc = 
u"""
78ROD71STUPRO
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
F[C]F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.

Base enthalpy changed from -186.62 to -193.44 kJ/mol for CF2 (2154-59-8*2) in ATcT version 1.122p
""",
)

entry(
    index = 10,
    label = "CHF",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p1 c0 {1,S} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials=[NASAPolynomial(coeffs=[3.34484,0.00235461,1.93983e-06,-2.65251e-09,7.91169e-13,16766.1,7.05286], Tmin=(298,'K'), Tmax=(1300,'K')), 
        NASAPolynomial(coeffs=[4.48366,0.00174964,-5.0479e-07,1.08953e-10,-9.87898e-15,16210.2,0.289222], Tmin=(1300,'K'), Tmax=(3000,'K'))], Tmin=(298,'K'), Tmax=(3000,'K'), 
        Cp0=(33.2579,'J/mol/K'), CpInf=(58.2013,'J/mol/K')),
    shortDesc = u"""84PRINIL71STU + H298 from ATcT version 1.122p""",
    longDesc = 
u"""
84PRINIL71STU
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH]F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.

Base enthalpy changed from 163.19 to 148.66 kJ/mol for CHF (13453-52-6*2) in ATcT version 1.122p
""",
)

entry(
    index = 11,
    label = "CF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p1 c0 {1,S}
""",
    thermo = NASA(
        polynomials=[NASAPolynomial(coeffs=[3.35384,0.000209097,3.20774e-06,-3.66875e-09,1.19863e-12,28645.6,6.33463], Tmin=(298,'K'), Tmax=(1100,'K')), 
        NASAPolynomial(coeffs=[3.66497,0.000973681,-4.10982e-07,8.00629e-11,-5.64981e-15,28462.1,4.28163], Tmin=(1100,'K'), Tmax=(3000,'K'))], 
        Tmin=(298,'K'), Tmax=(3000,'K'), Cp0=(29.1007,'J/mol/K'), CpInf=(37.4151,'J/mol/K')),
    shortDesc = u"""91GURVEY71STU + H298 from ATcT version 1.122p""",
    longDesc = 
u"""
91GURVEY71STU
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.

Base enthalpy changed from 240.60 to 246.74 kJ/mol for CF (3889-75-6*0) in ATcT version 1.122p
""",
)

entry(
    index = 12,
    label = "CF2(T)",
    molecule = 
"""
multiplicity 3
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {3,S}
3 C u2 p0 c0 {1,S} {2,S}
""",
    thermo = NASA(
        polynomials=[NASAPolynomial(coeffs=[2.28591,0.0107608,-1.05382e-05,4.89881e-09,-8.86384e-13,4216.69,13.1348], Tmin=(298,'K'), Tmax=(1300,'K')), 
        NASAPolynomial(coeffs=[5.33121,0.00197748,-9.60248e-07,2.10704e-10,-1.5954e-14,3366.49,-2.56367], Tmin=(1300,'K'), Tmax=(3000,'K'))], Tmin=(298,'K'), 
        Tmax=(3000,'K'), Cp0=(33.2579,'J/mol/K'), CpInf=(58.2013,'J/mol/K')),
    shortDesc = u"""CF2 + H298 from ATcT version 1.122p""",
    longDesc = 
u"""
Thermo from CF2(S) + Base enthalpy set to 44.00 kJ/mol for CF2(T) (2154-59-8*1) in ATcT version 1.122p
""",
)

entry(
    index = 13,
    label = "CCl2",
    molecule = 
"""
1 Cl u0 p3 c0 {3,S}
2 Cl u0 p3 c0 {3,S}
3 C  u0 p1 c0 {1,S} {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96424,0.00210486,2.42565e-05,-5.53641e-08,3.47438e-11,25957.4,8.03065], Tmin=(10,'K'), Tmax=(580.713,'K')),
            NASAPolynomial(coeffs=[4.74855,0.00489616,-4.118e-06,1.50748e-09,-1.99821e-13,25728.1,3.48355], Tmin=(580.713,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: 54.36 kcal/mol
S298: 63.39 cal/mol/K

Coordinates (Angstoms):
Cl 1.41553 -0.15151 0.00000
Cl -1.41553 -0.15153 0.00000
C 0.00000 0.85863 0.00000

Frequencies (cm^-1) = 328.2,719.4,727.7
"""
)

entry(
    index = 14,
    label = "CHCl",
    molecule = 
"""
1 Cl u0 p3 c0 {3,S}
2 H  u0 p0 c0 {3,S}
3 C  u0 p1 c0 {1,S} {2,S}
""",
    thermo = NASA(
        polynomials=[
            NASAPolynomial(coeffs=[0.680737,0.0175179,-1.87718e-05,8.94803e-09,-1.59474e-12,37731.7,19.9258], Tmin=(298,'K'), Tmax=(1410,'K')), 
            NASAPolynomial(coeffs=[7.02528,-0.000480796,3.75706e-07,-1.05187e-10,1.04423e-14,35942.6,-12.8629], Tmin=(1410,'K'), Tmax=(3500,'K'))], 
            Tmin=(298,'K'), Tmax=(3500,'K')),
    shortDesc = """CHCl(S)""",
    longDesc = 
"""
H298: 76.63 kcal/mol
S298: 56.17 cal/mol/k

Pelucchi M, Cavallotti C, Frassoldati A, Ranzi E, Glarborg P, Faravelli T.
Theoretical and kinetic modeling study of chloromethane (CH3Cl) pyrolysis and oxidation. Int J Chem Kinet. 2021;53:403–418. 
https://doi.org/10.1002/kin.21452

Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
"""
)

entry(
    index = 15,
    label = "CHCl(T)",
    molecule = 
"""
multiplicity 3
1 Cl u0 p3 c0 {3,S}
2 H  u0 p0 c0 {3,S}
3 C  u2 p0 c0 {1,S} {2,S}
""",
    thermo = NASA(
        polynomials=[
            NASAPolynomial(coeffs=[0.680737,0.0175179,-1.87718e-05,8.94803e-09,-1.59474e-12,40835.1,19.9258], Tmin=(298,'K'), Tmax=(1410,'K')), 
            NASAPolynomial(coeffs=[7.02528,-0.000480796,3.75706e-07,-1.05187e-10,1.04423e-14,39046,-12.8629], Tmin=(1410,'K'), Tmax=(3500,'K'))], 
            Tmin=(298,'K'), Tmax=(3500,'K')),
    shortDesc = """CHCl(T)""",
    longDesc = 
"""
Thermo from CHCl(S) + Base enthalpy set to 346.44 kJ/mol for CHCl(T) (2108-20-5*1) in ATcT version 1.122p
"""
)

entry(
    index = 16,
    label = "CClBr",
    molecule = 
"""
1 Br u0 p3 c0 {3,S}
2 Cl u0 p3 c0 {3,S}
3 C  u0 p1 c0 {1,S} {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95362,0.00292047,2.74172e-05,-7.21448e-08,5.08621e-11,32647.3,9.94238], Tmin=(10,'K'), Tmax=(527.687,'K')),
            NASAPolynomial(coeffs=[5.02979,0.00430161,-3.62373e-06,1.32778e-09,-1.76138e-13,32401,4.18006], Tmin=(527.687,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: 67.72 kcal/mol
S298: 67.60 cal/mol/K

Coordinates (Angstoms):
Br 0.00000 1.04521 0.00000
Cl -0.30924 -1.91853 0.00000
C 0.87618 -0.66121 0.00000

Frequencies (cm^-1) = 256.3,606.9,735.2
""",
    rank = 5,
)

entry(
    index = 17,
    label = "CFBr",
    molecule = 
"""
1 Br u0 p3 c0 {3,S}
2 F  u0 p3 c0 {3,S}
3 C  u0 p1 c0 {1,S} {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97246,0.00166288,2.18036e-05,-4.92192e-08,3.14417e-11,9629.51,8.94364], Tmin=(10,'K'), Tmax=(555.179,'K')),
            NASAPolynomial(coeffs=[4.32472,0.00516967,-4.00323e-06,1.38181e-09,-1.75468e-13,9497.24,6.61249], Tmin=(555.179,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: 21.85 kcal/mol
S298: 64.92 cal/mol/K

Coordinates (Angstoms):
Br 0.00000 0.69104 0.00000
F -0.42009 -1.90537 0.00000
C 0.63014 -1.17302 0.00000

Frequencies (cm^-1) = 334.7,639.9,1244.2
""",
    rank = 5,
)

entry(
    index = 18,
    label = "CCl",
    molecule = 
"""
multiplicity 2
1 C  u1 p1 c0 {2,S}
2 Cl u0 p3 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.51949,-0.00165133,1.48927e-05,-2.50303e-08,1.33468e-11,50774.4,6.33642], Tmin=(10,'K'), Tmax=(624.891,'K')),
            NASAPolynomial(coeffs=[3.41316,0.00213272,-1.64002e-06,5.55234e-10,-6.87304e-14,50727.1,6.3146], Tmin=(624.891,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: 103.01 kcal/mol
S298: 52.39 cal/mol/K

Coordinates (Angstoms):
Cl 0.00000 0.00000 0.43678
C 0.00000 0.00000 -1.23753

Frequencies (cm^-1) = 844.1
""",
    rank = 5,
)

entry(
    index = 19,
    label = "CBr2",
    molecule = 
"""
1 Br u0 p3 c0 {3,S}
2 Br u0 p3 c0 {3,S}
3 C  u0 p1 c0 {1,S} {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93995,0.00407964,3.03373e-05,-9.41351e-08,7.54238e-11,39243.8,10.4044], Tmin=(10,'K'), Tmax=(474.229,'K')),
            NASAPolynomial(coeffs=[5.238,0.00392956,-3.34425e-06,1.23081e-09,-1.63525e-13,38999.3,3.83026], Tmin=(474.229,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: 80.91 kcal/mol
S298: 69.02 cal/mol/K

Coordinates (Angstoms):
Br 1.56138 -0.08629 0.00000
Br -1.56138 -0.08628 0.00000
C 0.00000 1.00663 0.00000

Frequencies (cm^-1) = 192.1,594.3,627.1
""",
    rank = 5,
)

entry(
    index = 20,
    label = "CHBr",
    molecule = 
"""
1 Br u0 p3 c0 {2,S}
2 C  u0 p1 c0 {1,S} {3,S}
3 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.02658,-0.00248701,2.57606e-05,-4.62229e-08,2.75632e-11,43642.3,6.65622], Tmin=(10,'K'), Tmax=(519.797,'K')),
            NASAPolynomial(coeffs=[3.47763,0.00456534,-2.75177e-06,8.12651e-10,-9.30817e-14,43661.2,8.57786], Tmin=(519.797,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: 89.19 kcal/mol
S298: 58.91 cal/mol/K

Coordinates (Angstoms):
Br 0.02612 -0.31729 0.00000
C 0.02612 1.55838 0.00000
H -1.07081 1.75493 0.00000

Frequencies (cm^-1) = 664.5,1163.9,2916.4
""",
    rank = 5,
)

entry(
    index = 21,
    label = "CBr",
    molecule = 
"""
multiplicity 2
1 C  u1 p1 c0 {2,S}
2 Br u0 p3 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49353,0.000343339,6.34351e-06,-1.14479e-08,5.91793e-12,58330,7.55902], Tmin=(10,'K'), Tmax=(666.154,'K')),
            NASAPolynomial(coeffs=[3.45107,0.00231157,-1.94617e-06,7.08864e-10,-9.32622e-14,58297.6,7.46132], Tmin=(666.154,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: 118.08 kcal/mol
S298: 55.16 cal/mol/K

Coordinates (Angstoms):
Br 0.00000 0.00000 0.26927
C 0.00000 0.00000 -1.57075

Frequencies (cm^-1) = 707.7
""",
    rank = 5,
)

entry(
    index = 22,
    label = "CFCl",
    molecule = 
"""
1 Cl u0 p3 c0 {3,S}
2 F  u0 p3 c0 {3,S}
3 C  u0 p1 c0 {1,S} {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98114,0.00104581,1.86129e-05,-3.54182e-08,1.94951e-11,2463.99,7.66105], Tmin=(10,'K'), Tmax=(623.692,'K')),
            NASAPolynomial(coeffs=[3.9304,0.00607124,-4.77719e-06,1.66617e-09,-2.12976e-13,2378.91,7.14903], Tmin=(623.692,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: 7.55 kcal/mol
S298: 62.01 cal/mol/K

Coordinates (Angstoms):
Cl -0.67700 -0.73424 0.00000
F 1.27877 0.77567 0.00000
C 0.00000 0.91683 0.00000

Frequencies (cm^-1) = 432.9,724.3,1235.0
""",
    rank = 5,
)

entry(
    index = 23,
    label = "C6H5F",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {7,D}
3 C u0 p0 c0 {2,S} {4,D} {8,S}
4 C u0 p0 c0 {3,D} {5,S} {9,S}
5 C u0 p0 c0 {4,S} {6,D} {10,S}
6 C u0 p0 c0 {5,D} {7,S} {11,S}
7 C u0 p0 c0 {2,D} {6,S} {12,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials=[
            NASAPolynomial(coeffs=[4.144,-0.013576,0.00021967,-3.82379e-07,2.12897e-10,-15718.5,9.89288], Tmin=(10,'K'), Tmax=(575.024,'K')), 
            NASAPolynomial(coeffs=[-0.246923,0.0500332,-3.25125e-05,9.9937e-09,-1.16863e-12,-15760.2,23.8936], Tmin=(575.024,'K'), Tmax=(3000,'K'))
            ], 
        Tmin=(10,'K'), 
        Tmax=(3000,'K'), 
        Cp0=(33.2579,'J/(mol*K)'), 
        CpInf=(282.692,'J/(mol*K)')
    ),
    shortDesc = """ATct v1.122r + G4""",
    longDesc = 
"""
H298 from ATcT version 1.122r ATcT ID 462-06-6*0 
S and Cp from G4 calculation

H298: -114.76 kJ/mol
S298: 301.453 J/mol/K
""",
)

entry(
    index = 24,
    label = "C6H5Cl",
    molecule = 
"""
1 Cl u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {7,D}
3 C u0 p0 c0 {2,S} {4,D} {8,S}
4 C u0 p0 c0 {3,D} {5,S} {9,S}
5 C u0 p0 c0 {4,S} {6,D} {10,S}
6 C u0 p0 c0 {5,D} {7,S} {11,S}
7 C u0 p0 c0 {2,D} {6,S} {12,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials=[
            NASAPolynomial(coeffs=[3.93394,0.00379949,0.000132529,-2.31181e-07,1.25418e-10,4164.96,10.0304], Tmin=(10,'K'), Tmax=(561.624,'K')), 
            NASAPolynomial(coeffs=[-1.25831,0.0540087,-3.69033e-05,1.18818e-08,-1.44743e-12,4539.54,30.227], Tmin=(561.624,'K'), Tmax=(3000,'K'))
            ], 
        Tmin=(10,'K'), 
        Tmax=(3000,'K'),
        Cp0=(33.2579,'J/(mol*K)'), 
        CpInf=(282.692,'J/(mol*K)')
    ),
    shortDesc = """ATct v1.122r + G4""",
    longDesc = 
"""
H298 from ATcT version 1.122r ATcT ID 108-90-7*0 
S and Cp from G4 calculation

H298: 52.2 kJ/mol
S298: 313.183 J/mol/K
""",
)

entry(
    index = 25,
    label = "C6H5Br",
    molecule = 
"""
1 Br u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {7,D}
3 C u0 p0 c0 {2,S} {4,D} {8,S}
4 C u0 p0 c0 {3,D} {5,S} {9,S}
5 C u0 p0 c0 {4,S} {6,D} {10,S}
6 C u0 p0 c0 {5,D} {7,S} {11,S}
7 C u0 p0 c0 {2,D} {6,S} {12,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials=[
            NASAPolynomial(coeffs=[3.92273,0.00446979,0.000135475,-2.42908e-07,1.3465e-10,10433.6,11.2665], Tmin=(10,'K'), Tmax=(563,'K')), 
            NASAPolynomial(coeffs=[-0.424236,0.0519026,-3.49897e-05,1.11533e-08,-1.34899e-12,10660.8,27.4117], Tmin=(563,'K'), Tmax=(3000,'K'))
            ], 
        Tmin=(10,'K'), 
        Tmax=(3000,'K'),
        Cp0=(33.2579,'J/(mol*K)'), 
        CpInf=(282.692,'J/(mol*K)')
    ),
    shortDesc = """ATct v1.122r + G4""",
    longDesc = 
"""
H298 from ATcT version 1.122r ATcT ID 108-86-1*0
S and Cp from G4 calculation

H298: 104.6 kJ/mol
S298: 324.969 J/mol/K
""",
)

entry(
    index = 26,
    label = "C2F",
    molecule = 
"""
multiplicity 2
1 C  u1 p0 c0 {2,T}
2 C  u0 p0 c0 {1,T} {3,S}
3 Br u0 p3 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.81236, 0.0213694, -0.000129618, 3.30825e-07, -2.89499e-10, 52803.9, 5.3484],
                Tmin = (10, 'K'),
                Tmax = (375.518, 'K'),
            ),
            NASAPolynomial(
                coeffs = [4.02651, 0.00433281, -2.62518e-06, 7.31474e-10, -7.71719e-14, 52891.9, 5.91025],
                Tmin = (375.518, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (58.2013, 'J/(mol*K)'),
    ),
    shortDesc = """G4""",
    longDesc = 
"""
#   Enthalpy of formation (0 K)     =   106.475 kcal/mol
#   Enthalpy of formation (298 K)   =   107.829 kcal/mol
#   Entropy of formation (298 K)    =    59.672 cal/(mol*K)
""",
)


