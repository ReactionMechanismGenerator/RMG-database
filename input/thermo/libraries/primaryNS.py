#!/usr/bin/env python
# encoding: utf-8

name = "primaryNS"
shortDesc = u"primaryNS"
longDesc = u"""
Thermo data for various nitrogen and sulfur species
"""
entry(
    index = 0,
    label = "N",
    molecule = 
"""
multiplicity 4
1 N u3 p1 c0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.9675,4.9675,4.9675,4.9675,4.9675,4.9674,4.9718],'cal/(mol*K)'),
        H298 = (112.96,'kcal/mol'),
        S298 = (36.6336,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Taken from the GRI-Mech3.0-N library
""",
)

entry(
    index = 1,
    label = "NH(S)",
    molecule = 
"""
1 N u0 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.98,7,7.11,7.27,7.6,7.91,8.44],'cal/(mol*K)'),
        H298 = (120.9,'kcal/mol','+|-',0.5),
        S298 = (41.7,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Anthony M. Dean, Joseph W. Bozzelli, Combustion Chemistry of Nitrogen,
in: Gas-Phase Combustion Chemistry, Editor: W.C. Gardiner, 2000, 125-341,
doi: 10.1007/978-1-4612-1310-9_2
""",
)

entry(
    index = 2,
    label = "NNOH",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {2,D}
2 N u0 p1 c0 {1,D} {3,S}
3 O u0 p2 c0 {2,S} {4,S}
4 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.44,11.42,12.25,13.1,14.32,15.15,16.68],'cal/(mol*K)'),
        H298 = (58.1,'kcal/mol','+|-',0.5),
        S298 = (61.4,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Anthony M. Dean, Joseph W. Bozzelli, Combustion Chemistry of Nitrogen,
in: Gas-Phase Combustion Chemistry, Editor: W.C. Gardiner, 2000, 125-341,
doi: 10.1007/978-1-4612-1310-9_2
""",
)

entry(
    index = 3,
    label = "CH2NN",
    molecule = 
"""
1 C u0 p1 c-1 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 N u0 p0 c+1 {1,S} {5,T}
5 N u0 p1 c0 {4,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.74,13.86,15.6,17.04,19.17,20.67,22.94],'cal/(mol*K)'),
        H298 = (68.5,'kcal/mol','+|-',0.5),
        S298 = (57.96,'cal/(mol*K)'),
    ),
    shortDesc = u"""diazomethyl""",
    longDesc = 
u"""
Anthony M. Dean, Joseph W. Bozzelli, Combustion Chemistry of Nitrogen,
in: Gas-Phase Combustion Chemistry, Editor: W.C. Gardiner, 2000, 125-341,
doi: 10.1007/978-1-4612-1310-9_2
""",
)

entry(
    index = 4,
    label = "HCNN",
    molecule = 
"""
multiplicity 2
1 C u1 p1 c-1 {2,S} {3,S}
2 N u0 p0 c+1 {1,S} {4,T}
3 H u0 p0 c0 {1,S}
4 N u0 p1 c0 {2,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.78,12.19,13.4,14.29,15.68,16.56,17.71],'cal/(mol*K)'),
        H298 = (109,'kcal/mol','+|-',0.5),
        S298 = (59.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""diazomethyl radical""",
    longDesc = 
u"""
Anthony M. Dean, Joseph W. Bozzelli, Combustion Chemistry of Nitrogen,
in: Gas-Phase Combustion Chemistry, Editor: W.C. Gardiner, 2000, 125-341,
doi: 10.1007/978-1-4612-1310-9_2
""",
)

entry(
    index = 5,
    label = "HCN2",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 N u0 p1 c0 {1,S} {3,D}
3 N u0 p1 c0 {1,S} {2,D}
4 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11,12.02,13,13.81,15.3,16.09,17.59],'cal/(mol*K)'),
        H298 = (107.1,'kcal/mol','+|-',0.5),
        S298 = (57.5,'cal/(mol*K)'),
    ),
    shortDesc = u"""diazirine radical""",
    longDesc = 
u"""
Anthony M. Dean, Joseph W. Bozzelli, Combustion Chemistry of Nitrogen,
in: Gas-Phase Combustion Chemistry, Editor: W.C. Gardiner, 2000, 125-341,
doi: 10.1007/978-1-4612-1310-9_2
""",
)

entry(
    index = 6,
    label = "CH2NNH2",
    molecule = 
"""
1 C u0 p0 c0 {3,D} {4,S} {5,S}
2 N u0 p1 c0 {3,S} {6,S} {7,S}
3 N u0 p1 c0 {1,D} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.29,17.21,18.24,19.79,25.19,29.11,32.34],'cal/(mol*K)'),
        H298 = (45.5,'kcal/mol','+|-',0.5),
        S298 = (63.1,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Anthony M. Dean, Joseph W. Bozzelli, Combustion Chemistry of Nitrogen,
in: Gas-Phase Combustion Chemistry, Editor: W.C. Gardiner, 2000, 125-341,
doi: 10.1007/978-1-4612-1310-9_2
""",
)

entry(
    index = 7,
    label = "CH3NNH",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 N u0 p1 c0 {1,S} {3,D}
3 N u0 p1 c0 {2,D} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.7,16.2,16.82,18.69,24.4,27.1,31.31],'cal/(mol*K)'),
        H298 = (42.8,'kcal/mol','+|-',0.5),
        S298 = (61.4,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Anthony M. Dean, Joseph W. Bozzelli, Combustion Chemistry of Nitrogen,
in: Gas-Phase Combustion Chemistry, Editor: W.C. Gardiner, 2000, 125-341,
doi: 10.1007/978-1-4612-1310-9_2
""",
)

entry(
    index = 8,
    label = "NCHOH",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 O u0 p2 c0 {2,S} {5,S}
5 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.5,14.24,15.8,17.16,19.17,20.46,22.39],'cal/(mol*K)'),
        H298 = (13.9,'kcal/mol','+|-',0.5),
        S298 = (62.9,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Anthony M. Dean, Joseph W. Bozzelli, Combustion Chemistry of Nitrogen,
in: Gas-Phase Combustion Chemistry, Editor: W.C. Gardiner, 2000, 125-341,
doi: 10.1007/978-1-4612-1310-9_2
""",
)

entry(
    index = 9,
    label = "NS",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {2,D}
2 S u0 p2 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.07,8.17,8.26,8.35,8.5,8.62,8.84],'cal/(mol*K)'),
        H298 = (66.4,'kcal/mol','+|-',0.5),
        S298 = (52.76,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Enthalpy is taken from Marshall2002:
L.R. Peebles, P. Marshall, Chem. Phys. Letters, 2002, 366(5-6), 520-524, doi: 10.1016/S0009-2614(02)01619-6
Entropy and Cp are taken from Burcat2005:
Alexander Burcat and Branko Ruscic
"Third Millennium Ideal Gas and Condensed Phase Thermochemical Database for
Combustion with updates from Active Thermochemical Tables" TAE # 960; ANL-50/20
Technion-IIT, Aerospace Engineering, and Argonne National Laboratory, Chemistry
Division, 2005. http://garfield.chem.elte.hu/Burcat/burcat.html
""",
)

entry(
    index = 10,
    label = "NSO",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {2,D}
2 S u0 p1 c0 {1,D} {3,D}
3 O u0 p2 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([42.7,46.11,48.85,50.92,53.56,55.04,56.7],'J/(mol*K)'),
        H298 = (175.31,'kJ/mol','+|-',2.092),
        S298 = (262.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Taken from the SulfurGlarborgNS library
H298 is updated from Table 7 in P.A. Denis, J. Sulfur Chem. 2008, 29(3-4), 327-352, doi: 10.1080/17415990802047352
""",
)

entry(
    index = 11,
    label = "NNS",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 N u0 p0 c+1 {1,T} {3,S}
3 S u0 p3 c-1 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.48496,0.00087841,1.61418e-05,-3.21583e-08,1.89692e-11,23801.9,6.98879], Tmin=(10,'K'), Tmax=(573.927,'K')),
            NASAPolynomial(coeffs=[3.41668,0.00484707,-3.35932e-06,1.09773e-09,-1.35956e-13,23752.2,6.77912], Tmin=(573.927,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (197.894,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (54.0441,'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12a/cc-pVTZ-f12//M06-2x/cc-pVTZ""",
    longDesc = 
u"""
SMILES: N#[N+][S-]

calculated by alongd (xq1161, xc1074) at the CCSD(T)-F12a/cc-pVTZ-f12//M06-2x/cc-pVTZ level of theory
frequencies calculated at M06-2x/cc-pVTZ

Thermodynamics for NNS:
    Enthalpy of formation (298 K)   =    49.615 kcal/mol
    Entropy of formation (298 K)    =    54.798 cal/(mol*K)
    =========== =========== =========== =========== ===========
    Temperature Heat cap.   Enthalpy    Entropy     Free energy
    (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
    =========== =========== =========== =========== ===========
            300       8.916      49.633      54.857      33.176
            400       9.631      50.562      57.523      27.552
            500      10.185      51.554      59.735      21.686
            600      10.602      52.594      61.630      15.616
            800      11.229      54.781      64.772       2.963
           1000      11.657      57.072      67.327     -10.254
           1500      12.212      63.062      72.176     -45.202
           2000      12.480      69.239      75.728     -82.218
           2400      12.647      74.266      78.019    -112.980
    =========== =========== =========== =========== ===========
""",
)

entry(
    index = 12,
    label = "SO",
    molecule = 
"""
multiplicity 3
1 S u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.22,7.55,7.84,8.08,8.43,8.62,8.95],'cal/(mol*K)'),
        H298 = (1.2,'kcal/mol','+|-',0.3),
        S298 = (53.01,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
R.J. Kee, F.M. Rupley, J.A. Miller, The Chemkin Thermodynamic Data Base, Sandia Report SAND87-8215, Sandia National Laboratories, Livermore, California, 1991
As reported by: P. Glarborg, D. Kubel, K Dam-Johansen, H-M. Chiang, J.W. Bozzelli, Int. J. Chem. Kin., 1996, 28(10), 773-790, doi: 10.1002/(SICI)1097-4601(1996)28:10<773::AID-KIN8>3.0.CO;2-K
H298 is taken from Table 7 in P.A. Denis, J. Sulfur Chem. 2008, 29(3-4), 327-352, doi: 10.1080/17415990802047352
""",
)

entry(
    index = 13,
    label = "SO2",
    molecule = 
"""
1 S u0 p1 c0 {2,D} {3,D}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.54,10.41,11.12,11.71,12.55,13.03,13.61],'cal/(mol*K)'),
        H298 = (-70.94,'kcal/mol','+|-',0.05),
        S298 = (59.29,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
R.J. Kee, F.M. Rupley, J.A. Miller, The Chemkin Thermodynamic Data Base, Sandia Report SAND87-8215, Sandia National Laboratories, Livermore, California, 1991
As reported by: P. Glarborg, D. Kubel, K Dam-Johansen, H-M. Chiang, J.W. Bozzelli, Int. J. Chem. Kin., 1996, 28(10), 773-790, doi: 10.1002/(SICI)1097-4601(1996)28:10<773::AID-KIN8>3.0.CO;2-K
H298 is taken from Table 7 in P.A. Denis, J. Sulfur Chem. 2008, 29(3-4), 327-352, doi: 10.1080/17415990802047352
""",
)

entry(
    index = 14,
    label = "OSO(T)",
    molecule = 
"""
multiplicity 3
1 S u1 p1 c0 {2,S} {3,D}
2 O u1 p2 c0 {1,S}
3 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9676,0.00189329,2.31571e-05,-5.14929e-08,3.17715e-11,46018.7,8.61359], Tmin=(10,'K'), Tmax=(585.659,'K')),
            NASAPolynomial(coeffs=[4.60402,0.00505536,-4.17317e-06,1.50935e-09,-1.98437e-13,45815.4,4.78435], Tmin=(585.659,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (382.608,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12a//cc-pVTZ-F12//B3LYP/6-311+G(2d,p)""",
    longDesc = 
u"""
SMILES: [O][S]=O, [O]S[O]

calculated by alongd (xq1287, xc1112) at the CCSD(T)-F12a//cc-pVTZ-F12//B3LYP/6-311+G(2d,p) level of theory
(no rotors)

Thermodynamics for OSO(T):
    Enthalpy of formation (298 K)   =    94.199 kcal/mol
    Entropy of formation (298 K)    =    64.422 cal/(mol*K)
    =========== =========== =========== =========== ===========
    Temperature Heat cap.   Enthalpy    Entropy     Free energy
    (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
    =========== =========== =========== =========== ===========
           300      10.903      94.221      64.495      74.873
           400      11.820      95.360      67.764      68.254
           500      12.425      96.574      70.472      61.338
           600      12.788      97.836      72.772      54.173
           800      13.253     100.445      76.521      39.228
          1000      13.507     103.123      79.508      23.615
          1500      13.686     109.938      85.032     -17.610
          2000      13.755     116.794      88.976     -61.159
          2400      13.873     122.319      91.494     -97.267
    =========== =========== =========== =========== ===========
""",
)

entry(
    index = 15,
    label = "OOS(T)",
    molecule = 
"""
multiplicity 3
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 S u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96011,0.0025733,2.55356e-05,-6.72978e-08,4.84507e-11,33434.7,8.77386], Tmin=(10,'K'), Tmax=(508.046,'K')),
            NASAPolynomial(coeffs=[4.67958,0.00470058,-3.75057e-06,1.32005e-09,-1.69845e-13,33261,4.80039], Tmin=(508.046,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (277.982,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12a//cc-pVTZ-F12//B3LYP/6-311+G(2d,p)""",
    longDesc = 
u"""
SMILES: [O]O[S]

calculated by alongd (xq1286, xc1111) at the CCSD(T)-F12a//cc-pVTZ-F12//B3LYP/6-311+G(2d,p) level of theory
(no rotors)

Thermodynamics for OOS(T):
    Enthalpy of formation (298 K)   =    69.243 kcal/mol
    Entropy of formation (298 K)    =    65.056 cal/(mol*K)
    =========== =========== =========== =========== ===========
    Temperature Heat cap.   Enthalpy    Entropy     Free energy
    (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
    =========== =========== =========== =========== ===========
           300      11.140      69.265      65.131      49.726
           400      11.940      70.422      68.454      43.041
           500      12.413      71.642      71.174      36.055
           600      12.744      72.901      73.467      28.820
           800      13.207      75.500      77.202      13.738
          1000      13.473      78.170      80.181      -2.011
          1500      13.686      84.977      85.698     -43.570
          2000      13.754      91.835      89.643     -87.452
          2400      13.853      97.356      92.159    -123.827
    =========== =========== =========== =========== ===========
""",
)

entry(
    index = 16,
    label = "SO3",
    molecule = 
"""
1 S u0 p0 c0 {2,D} {3,D} {4,D}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,D}
4 O u0 p2 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.17,13.76,15.05,16.07,17.45,18.16,19.02],'cal/(mol*K)'),
        H298 = (-94.6,'kcal/mol'),
        S298 = (61.34,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
R.J. Kee, F.M. Rupley, J.A. Miller, The Chemkin Thermodynamic Data Base, Sandia Report SAND87-8215, Sandia National Laboratories, Livermore, California, 1991
As reported by: P. Glarborg, D. Kubel, K Dam-Johansen, H-M. Chiang, J.W. Bozzelli, Int. J. Chem. Kin., 1996, 28(10), 773-790, doi: 10.1002/(SICI)1097-4601(1996)28:10<773::AID-KIN8>3.0.CO;2-K
""",
)

entry(
    index = 17,
    label = "HSO",
    molecule = 
"""
multiplicity 2
1 S u1 p1 c0 {2,S} {3,D}
2 H u0 p0 c0 {1,S}
3 O u0 p2 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,700,1000,1300,2000],'K'),
        Cpdata = ([36.15,38.6,41.4,45.8,50.1,52.7,55.6],'J/(mol*K)'),
        H298 = (-5.2,'kcal/mol','+|-',0.5),
        S298 = (57.65,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
A. Goumri, D. Laakso, J-D R. Rocha, C.E. Smith, P. Marshall
The Journal of Chemical Physics 102, 161 (1995)
doi: 10.1063/1.469387
Table V.
Cp(200K) = 33.7; Cp(300K) interpolated
H298 is taken from Table 7 in P.A. Denis, J. Sulfur Chem. 2008, 29(3-4), 327-352, doi: 10.1080/17415990802047352
""",
)

entry(
    index = 18,
    label = "HOS",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 S u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,700,1000,1300,2000],'K'),
        Cpdata = ([36.85,39.6,42,45.3,48.6,50.9,54.2],'J/(mol*K)'),
        H298 = (-1.6,'kcal/mol','+|-',0.5),
        S298 = (57.48,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
A. Goumri, D. Laakso, J-D R. Rocha, C.E. Smith, P. Marshall
The Journal of Chemical Physics 102, 161 (1995)
doi: 10.1063/1.469387
Table VI.
Cp(200K) = 34.1; Cp(300K) interpolated
H298 is taken from Table 7 in P.A. Denis, J. Sulfur Chem. 2008, 29(3-4), 327-352, doi: 10.1080/17415990802047352
""",
)

entry(
    index = 19,
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
        H298 = (25,'kcal/mol','+|-',0.5),
        S298 = (60.95,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Taken from the SulfurGlarborgH2S library with comment:
Zhou - K. Sendt, B.S. Haynes, J. Phys. Chem. A 109 (2005) 8180 to 8186;
K. Sendt, M. Jazbec, B.S. Haynes, Proc. Combust. Inst. 29 (2003) 2439-2446.
25.84  60.94
H298 is taken from Table 7 in P.A. Denis, J. Sulfur Chem. 2008, 29(3-4), 327-352, doi: 10.1080/17415990802047352
""",
)

entry(
    index = 20,
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
        H298 = (3.7,'kcal/mol','+|-',0.5),
        S298 = (61.62,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Taken from the SulfurGlarborgH2S library with comment:
Zhou - K. Sendt, B.S. Haynes, J. Phys. Chem. A 109 (2005) 8180 to 8186;
K. Sendt, M. Jazbec, B.S. Haynes, Proc. Combust. Inst. 29 (2003) 2439-2446.
3.70  61.61
H298 (updated uncertainty) is taken from Table 7 in P.A. Denis, J. Sulfur Chem. 2008, 29(3-4), 327-352, doi: 10.1080/17415990802047352
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([49.66,56.19,60.09,64.27,68.62,71.38,75.68],'J/(mol*K)'),
        H298 = (-118.83,'kJ/mol','+|-',4.2),
        S298 = (270.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
UMP2=full/6-31G+
A. Goumri, J-D.R. Rocha, D. Laakso, C.E. Smith, P. Marshall
The Journal of Chemical Physics 101, 9405 (1994); doi: http://dx.doi.org/10.1063/1.467971
As reported by: M.U. Alzueta, R. Bilbao, P. Glarborg, Comb. Flame, 2001, 127(4) 2234-2251, doi: 10.1016/S0010-2180(01)00325-X
H298 is taken from Table 7 in P.A. Denis, J. Sulfur Chem. 2008, 29(3-4), 327-352, doi: 10.1080/17415990802047352
This is significantly different that the value reported  by Marshall 1994 (-236.3 kJ/mol),
but in agreement with SulfurGlargotgBozzelli library that took it from a currently untraceable source.
Also in agreement with Table 8 in P.A. Denis, Molecular Physics 2008, 106(21-23), 2557-2567, doi: 10.1080/00268970802603523
""",
)

entry(
    index = 22,
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
        Cpdata = ([9.53,11.13,12.66,13.95,15.82,17,18.44],'cal/(mol*K)'),
        H298 = (-12.5,'kcal/mol','+|-',1),
        S298 = (57.26,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
H.M. Chiang, J.W. Bozzelli, Quantum Rice-Ramsberger-Kassel (QRRK) Analysis on Reaction of HSO + O, H + SO2, and OH + SO; HO2 and HOSO Formation and Dissociation
As reported by: P. Glarborg, D. Kubel, K Dam-Johansen, H-M. Chiang, J.W. Bozzelli, Int. J. Chem. Kin., 1996, 28(10), 773-790, doi: 10.1002/(SICI)1097-4601(1996)28:10<773::AID-KIN8>3.0.CO;2-K
H298 is taken from Table 7 in P.A. Denis, J. Sulfur Chem. 2008, 29(3-4), 327-352, doi: 10.1080/17415990802047352
""",
)

entry(
    index = 23,
    label = "HSO2",
    molecule = 
"""
multiplicity 2
1 S u1 p0 c0 {2,D} {3,D} {4,S}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,D}
4 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.94,13.68,14.99,15.97,17.28,18.05,18.98],'cal/(mol*K)'),
        H298 = (-33.8,'kcal/mol'),
        S298 = (63.68,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
H.M. Chiang, J.W. Bozzelli, Quantum Rice-Ramsberger-Kassel (QRRK) Analysis on Reaction of HSO + O, H + SO2, and OH + SO; HO2 and HOSO Formation and Dissociation
As reported by: P. Glarborg, D. Kubel, K Dam-Johansen, H-M. Chiang, J.W. Bozzelli, Int. J. Chem. Kin., 1996, 28(10), 773-790, doi: 10.1002/(SICI)1097-4601(1996)28:10<773::AID-KIN8>3.0.CO;2-K
Also available from:
A. Goumri, J-D.R. Rocha, D. Laakso, C.E. Smith, P. Marshall, J. Phys. Chem. A, 1999, 103, 11328-11335, doi: 10.1021/jp9924070; Table 3; MP2=FULL/6-31G(d)
""",
)

entry(
    index = 24,
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
        Cpdata = ([13.58,15.84,17.65,19.01,20.82,21.95,23.54],'cal/(mol*K)'),
        H298 = (-64.5,'kcal/mol'),
        S298 = (64.48,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
H.M. Chiang, J.W. Bozzelli, Quantum Rice-Ramsberger-Kassel (QRRK) Analysis on Reaction of HSO + O, H + SO2, and OH + SO; HO2 and HOSO Formation and Dissociation
As reported by: P. Glarborg, D. Kubel, K Dam-Johansen, H-M. Chiang, J.W. Bozzelli, Int. J. Chem. Kin., 1996, 28(10), 773-790, doi: 10.1002/(SICI)1097-4601(1996)28:10<773::AID-KIN8>3.0.CO;2-K
""",
)

entry(
    index = 25,
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([16.74,18.76,20.13,21.07,22.22,22.94,24.02],'cal/(mol*K)'),
        H298 = (-89.4,'kcal/mol','+|-',0.72),
        S298 = (70.72,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
H.M. Chiang, J.W. Bozzelli, Quantum Rice-Ramsberger-Kassel (QRRK) Analysis on Reaction of HSO + O, H + SO2, and OH + SO; HO2 and HOSO Formation and Dissociation
As reported by: P. Glarborg, D. Kubel, K Dam-Johansen, H-M. Chiang, J.W. Bozzelli, Int. J. Chem. Kin., 1996, 28(10), 773-790, doi: 10.1002/(SICI)1097-4601(1996)28:10<773::AID-KIN8>3.0.CO;2-K
H298 is calculated at fc-CCSD(T)/cc-pV(T+d)Z and taken from W. Klopper, D.P. Tew, N. Gonzalez-Garcia, M. Olzmann, J. Chem. Phys. 2008, 129, 114308, doi: 10.1063/1.2973637
""",
)

entry(
    index = 26,
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
            NASAPolynomial(coeffs=[3.86474,0.0135584,-2.40972e-05,2.93163e-08,-1.55426e-11,14275.4,9.88043], Tmin=(10,'K'), Tmax=(448.899,'K')),
            NASAPolynomial(coeffs=[4.48696,0.00801407,-5.57065e-06,1.8022e-09,-2.19497e-13,14219.5,7.37697], Tmin=(448.899,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (118.694,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (78.9875,'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12a/cc-pVTZ-f12//B3LYP/6-311G(2d,d,p)""",
    longDesc = 
u"""
SMILES: SO[O]

calculated by alongd (xq1174, xc1086) at the CCSD(T)-F12a/cc-pVTZ-f12//B3LYP/6-311G(2d,d,p) level of theory
frequencies calculated at B3LYP/6-311G(2d,d,p)
rotor calculated at B3LYP/6-311G(2d,pd)

Thermodynamics for HSOO:
    Enthalpy of formation (298 K)   =    31.531 kcal/mol
    Entropy of formation (298 K)    =    69.744 cal/(mol*K)
    =========== =========== =========== =========== ===========
    Temperature Heat cap.   Enthalpy    Entropy     Free energy
    (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
    =========== =========== =========== =========== ===========
           300      12.776      31.557      69.830      10.608
           400      13.733      32.884      73.641       3.427
           500      14.532      34.298      76.794      -4.099
           600      15.204      35.786      79.504     -11.917
           800      16.227      38.935      84.028     -28.287
          1000      16.917      42.255      87.728     -45.473
          1500      17.776      50.965      94.780     -91.205
          2000      18.159      59.955      99.950    -139.944
          2400      18.412      67.271     103.283    -180.610
    =========== =========== =========== =========== ===========
""",
)

entry(
    index = 27,
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
        Tdata = ([300,400,500,700,1000,1300,2500],'K'),
        Cpdata = ([53.4,57.1,60.1,64.3,68.3,71.1,74.7],'J/(mol*K)'),
        H298 = (-241.4,'kJ/mol'),
        S298 = (282.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Table 4
MP2=FULL/6-31G(d)
A. Goumri, J-D.R. Rocha, D. Laakso, C.E. Smith, P. Marshall
J. Phys. Chem. A, 1999, 103, 11328-11335, doi: 10.1021/jp9924070
also available from:
H.M. Chiang, J.W. Bozzelli, Quantum Rice-Ramsberger-Kassel (QRRK) Analysis on Reaction of HSO + O, H + SO2, and OH + SO; HO2 and HOSO Formation and Dissociation
As reported by: P. Glarborg, D. Kubel, K Dam-Johansen, H-M. Chiang, J.W. Bozzelli, Int. J. Chem. Kin., 1996, 28(10), 773-790, doi: 10.1002/(SICI)1097-4601(1996)28:10<773::AID-KIN8>3.0.CO;2-K
""",
)

entry(
    index = 28,
    label = "HSOS",
    molecule = 
"""
multiplicity 2
1 S u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {3,S}
3 S u1 p2 c0 {2,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76439,0.0252802,-0.000110467,2.55957e-07,-2.17671e-10,13066.9,9.29384], Tmin=(10,'K'), Tmax=(362.811,'K')),
            NASAPolynomial(coeffs=[4.59981,0.00798713,-5.55392e-06,1.77626e-09,-2.13294e-13,13059.5,6.84355], Tmin=(362.811,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (108.638,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (78.9875,'J/(mol*K)'),
    ),
    shortDesc = u"""UCCSD(T)-F12a/cc-pVTZ-f12//UM06-2x/cc-pVTZ""",
    longDesc = 
u"""
SMILES: SO[S]

calculated by alongd (xq1112, xc1063) at the UCCSD(T)-F12a/cc-pVTZ-f12//UM06-2x/cc-pVTZ level of theory
frequencies calculated at UM06-2x/cc-pVTZ
rotor calculated at ub3lyp/6-311++g(df,pd)

Thermodynamics for HSOS:
    Enthalpy of formation (298 K)   =    29.290 kcal/mol
    Entropy of formation (298 K)    =    69.944 cal/(mol*K)
    =========== =========== =========== =========== ===========
    Temperature Heat cap.   Enthalpy    Entropy     Free energy
    (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
    =========== =========== =========== =========== ===========
           300      13.024      29.316      70.031       8.306
           400      13.939      30.664      73.905       1.102
           500      14.732      32.099      77.103      -6.452
           600      15.398      33.606      79.849     -14.303
           800      16.409      36.794      84.427     -30.748
          1000      17.082      40.147      88.166     -48.019
          1500      17.883      48.926      95.274     -93.985
          2000      18.194      57.953     100.466    -142.979
          2400      18.395      65.271     103.801    -183.851
    =========== =========== =========== =========== ===========
""",
)

entry(
    index = 29,
    label = "O2ScycOO",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 S u0 p0 c0 {1,D} {3,D} {4,S} {5,S}
3 O u0 p2 c0 {2,D}
4 O u0 p2 c0 {2,S} {5,S}
5 O u0 p2 c0 {2,S} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93153,0.00394097,6.00801e-05,-1.23616e-07,7.28108e-11,-35195.9,8.63709], Tmin=(10,'K'), Tmax=(593.33,'K')),
            NASAPolynomial(coeffs=[4.45657,0.0166144,-1.29477e-05,4.4926e-09,-5.7278e-13,-35543.6,3.97325], Tmin=(593.33,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-292.664,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12a/cc-pVTZ-f12//M06-2x/cc-pVTZ""",
    longDesc = 
u"""
SMILES: O=S1(=O)OO1

calculated by alongd (xq1112, xc1063) at the CCSD(T)-F12a/cc-pVTZ-f12//M06-2x/cc-pVTZ level of theory
frequencies calculated at M06-2x/cc-pVTZ
(no rotors)

Thermodynamics for O2ScycOO:
    Enthalpy of formation (298 K)   =   -66.629 kcal/mol
    Entropy of formation (298 K)    =    67.427 cal/(mol*K)
    =========== =========== =========== =========== ===========
    Temperature Heat cap.   Enthalpy    Entropy     Free energy
    (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
    =========== =========== =========== =========== ===========
           300      15.447     -66.598      67.530     -86.857
           400      18.030     -64.919      72.343     -93.856
           500      19.913     -63.016      76.582    -101.307
           600      21.184     -60.957      80.332    -109.156
           800      22.907     -56.534      86.682    -125.880
          1000      23.932     -51.841      91.914    -143.755
          1500      24.857     -39.581     101.844    -192.346
          2000      25.179     -27.074     109.037    -245.149
          2400      25.544     -16.931     113.660    -289.714
    =========== =========== =========== =========== ===========
""",
)

entry(
    index = 30,
    label = "cycOOS",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {3,S}
3 S u0 p2 c0 {1,S} {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05319,-0.00458038,4.32509e-05,-7.36568e-08,3.97671e-11,19631.5,7.5508], Tmin=(10,'K'), Tmax=(616.814,'K')),
            NASAPolynomial(coeffs=[3.74301,0.00630752,-4.81298e-06,1.62255e-09,-2.00437e-13,19500.9,7.52857], Tmin=(616.814,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (163.223,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12a/cc-pVTZ-f12//M06-2x/cc-pVTZ""",
    longDesc = 
u"""
SMILES: O1OS1

calculated by alongd (xq1119, xc1070) at the CCSD(T)-F12a/cc-pVTZ-f12//M06-2x/cc-pVTZ level of theory
frequencies calculated at M06-2x/cc-pVTZ

Thermodynamics for cycOOS:
    Enthalpy of formation (298 K)   =    41.515 kcal/mol
    Entropy of formation (298 K)    =    60.861 cal/(mol*K)
    =========== =========== =========== =========== ===========
    Temperature Heat cap.   Enthalpy    Entropy     Free energy
    (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
    =========== =========== =========== =========== ===========
           300       9.747      41.534      60.926      23.256
           400      10.821      42.564      63.882      17.011
           500      11.633      43.689      66.389      10.495
           600      12.160      44.881      68.560       3.745
           800      12.832      47.385      72.158     -10.341
          1000      13.234      49.996      75.069     -25.073
          1500      13.585      56.727      80.522     -64.057
          2000      13.671      63.540      84.442    -105.344
          2400      13.788      69.031      86.945    -139.636
    =========== =========== =========== =========== ===========
""",
)

entry(
    index = 31,
    label = "cycOOSS",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {3,S}
3 S u0 p2 c0 {2,S} {4,S}
4 S u0 p2 c0 {1,S} {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93391,0.00383934,4.67573e-05,-1.03421e-07,6.33246e-11,27935.9,9.35695], Tmin=(10,'K'), Tmax=(591.303,'K')),
            NASAPolynomial(coeffs=[5.28612,0.0101553,-8.49195e-06,3.09661e-09,-4.09322e-13,27505.6,1.2579], Tmin=(591.303,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (232.245,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12a/cc-pVTZ-f12//M06-2x/cc-pVTZ""",
    longDesc = 
u"""
SMILES: O1OSS1

calculated by alongd (xq1118, xc1069) at the CCSD(T)-F12a/cc-pVTZ-f12//M06-2x/cc-pVTZ level of theory
frequencies calculated at M06-2x/cc-pVTZ

Thermodynamics for cycOOSS:
    Enthalpy of formation (298 K)   =    58.656 kcal/mol
    Entropy of formation (298 K)    =    67.966 cal/(mol*K)
    =========== =========== =========== =========== ===========
    Temperature Heat cap.   Enthalpy    Entropy     Free energy
    (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
    =========== =========== =========== =========== ===========
           300      13.939      58.684      68.059      38.267
           400      15.804      60.176      72.338      31.241
           500      17.036      61.824      76.009      23.819
           600      17.762      63.566      79.185      16.056
           800      18.667      67.218      84.430      -0.327
          1000      19.150      71.005      88.654     -17.649
          1500      19.457      80.688      96.502     -64.065
          2000      19.579      90.438     102.111    -113.784
          2400      19.817      98.317     105.702    -155.367
    =========== =========== =========== =========== ===========
""",
)

entry(
    index = 32,
    label = "H2SO4",
    molecule = 
"""
1 S u0 p0 c0 {2,D} {3,D} {4,S} {5,S}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,D}
4 O u0 p2 c0 {1,S} {6,S}
5 O u0 p2 c0 {1,S} {7,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82425,0.0119047,0.000109424,-3.15925e-07,2.47803e-10,-91732.6,8.87386], Tmin=(10,'K'), Tmax=(471.056,'K')),
            NASAPolynomial(coeffs=[7.04982,0.0173189,-1.22766e-05,4.15079e-09,-5.29527e-13,-92400.4,-8.12269], Tmin=(471.056,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-762.735,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (153.818,'J/(mol*K)'),
    ),
    shortDesc = u"""UCCSD(T)-F12a/cc-pVTZ-f12//B3LYP/6-311G(2d,d,p)""",
    longDesc = 
u"""
SMILES: OS(=O)(=O)O

calculated by alongd (xq1173, xc1085) at the UCCSD(T)-F12a/cc-pVTZ-f12//B3LYP/6-311G(2d,d,p) level of theory
frequencies calculated at B3LYP/6-311G(2d,d,p)
rotors calculated at B3LYP/6-311G(2d,pd)

Thermodynamics for H2SO4:
    Enthalpy of formation (298 K)   =  -178.065 kcal/mol
    Entropy of formation (298 K)    =    73.067 cal/(mol*K)
    =========== =========== =========== =========== ===========
    Temperature Heat cap.   Enthalpy    Entropy     Free energy
    (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
    =========== =========== =========== =========== ===========
           300      21.305    -178.022      73.210    -199.985
           400      24.281    -175.730      79.784    -207.643
           500      26.084    -173.206      85.408    -215.910
           600      27.522    -170.524      90.294    -224.700
           800      29.721    -164.786      98.533    -243.612
          1000      31.226    -158.681     105.337    -264.018
          1500      33.254    -142.490     118.439    -320.149
          2000      34.409    -125.564     128.170    -381.904
          2400      35.202    -111.636     134.517    -434.476
    =========== =========== =========== =========== ===========
""",
)

entry(
    index = 33,
    label = "HSO2OO",
    molecule = 
"""
multiplicity 2
1 S u0 p0 c0 {2,S} {3,D} {4,S} {5,D}
2 O u0 p2 c0 {1,S} {6,S}
3 O u0 p2 c0 {1,D}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {1,D}
6 O u1 p2 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79167,0.0166396,5.60531e-05,-1.97213e-07,1.66845e-10,-28503.7,11.2581], Tmin=(10,'K'), Tmax=(449.043,'K')),
            NASAPolynomial(coeffs=[5.95215,0.0173632,-1.30682e-05,4.43954e-09,-5.57766e-13,-28899,0.323081], Tmin=(449.043,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-237.008,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (128.874,'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12a/cc-pVTZ-f12//B3LYP/6-311G(2d,d,p)""",
    longDesc = 
u"""
SMILES: [O]O[SH](=O)=O

calculated by alongd (xq1167, xc1079) at the CCSD(T)-F12a/cc-pVTZ-f12//B3LYP/6-311G(2d,d,p) level of theory
frequencies calculated at B3LYP/6-311G(2d,d,p)
rotor calculated at B3LYP/6-311G(2d,pd)

Thermodynamics for HSO2OO:
    Enthalpy of formation (298 K)   =   -52.563 kcal/mol
    Entropy of formation (298 K)    =    77.295 cal/(mol*K)
    =========== =========== =========== =========== ===========
    Temperature Heat cap.   Enthalpy    Entropy     Free energy
    (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
    =========== =========== =========== =========== ===========
           300      19.584     -52.524      77.426     -75.752
           400      21.990     -50.436      83.416     -83.803
           500      23.621     -48.152      88.506     -92.405
           600      24.944     -45.722      92.933    -101.482
           800      26.874     -40.526     100.394    -120.841
          1000      28.077     -35.021     106.531    -141.552
          1500      29.318     -20.602     118.207    -197.912
          2000      29.803      -5.820     126.709    -259.237
          2400      30.240       6.189     132.181    -311.046
    =========== =========== =========== =========== ===========
""",
)

entry(
    index = 34,
    label = "HSO3",
    molecule = 
"""
multiplicity 2
1 S u0 p0 c0 {2,S} {3,D} {4,D} {5,S}
2 H u0 p0 c0 {1,S}
3 O u0 p2 c0 {1,D}
4 O u0 p2 c0 {1,D}
5 O u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92255,0.0129065,-8.44739e-07,-8.83705e-09,4.38872e-12,-16579,8.38917], Tmin=(10,'K'), Tmax=(957.734,'K')),
            NASAPolynomial(coeffs=[6.26213,0.00958261,-5.73674e-06,1.59724e-09,-1.69777e-13,-17322.8,-4.34062], Tmin=(957.734,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-137.825,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12a/cc-pVTZ-f12//B3LYP/6-311G(2d,d,p)""",
    longDesc = 
u"""
SMILES: [O][SH](=O)=O

calculated by alongd (xq1168, xc1080) at the CCSD(T)-F12a/cc-pVTZ-f12//B3LYP/6-311G(2d,d,p) level of theory
frequencies calculated at B3LYP/6-311G(2d,d,p)

Thermodynamics for HSO3:
    Enthalpy of formation (298 K)   =   -29.530 kcal/mol
    Entropy of formation (298 K)    =    68.510 cal/(mol*K)
    =========== =========== =========== =========== ===========
    Temperature Heat cap.   Enthalpy    Entropy     Free energy
    (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
    =========== =========== =========== =========== ===========
           300      14.935     -29.500      68.610     -50.083
           400      16.885     -27.906      73.180     -57.178
           500      18.549     -26.132      77.132     -64.698
           600      19.916     -24.207      80.639     -72.590
           800      21.820     -20.016      86.654     -89.339
          1000      22.923     -15.533      91.652    -107.184
          1500      24.362      -3.655     101.264    -155.551
          2000      24.923       8.686     108.361    -208.035
          2400      25.166      18.707     112.927    -252.319
    =========== =========== =========== =========== ===========
""",
)

entry(
    index = 35,
    label = "HOSO3",
    molecule = 
"""
multiplicity 2
1 S u0 p0 c0 {2,S} {3,S} {4,D} {5,D}
2 O u0 p2 c0 {1,S} {6,S}
3 O u1 p2 c0 {1,S}
4 O u0 p2 c0 {1,D}
5 O u0 p2 c0 {1,D}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85754,0.0099495,8.51696e-05,-2.46189e-07,1.94906e-10,-63517.7,11.0751], Tmin=(10,'K'), Tmax=(458.746,'K')),
            NASAPolynomial(coeffs=[5.63474,0.0171977,-1.28996e-05,4.40463e-09,-5.5626e-13,-63920.1,1.27755], Tmin=(458.746,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-528.134,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (128.874,'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12a/cc-pVTZ-f12//B3LYP/6-311G(2d,d,p)""",
    longDesc = 
u"""
SMILES: [O]S(=O)(=O)O

calculated by alongd (xq1170, xc1082) at the CCSD(T)-F12a/cc-pVTZ-f12//B3LYP/6-311G(2d,d,p) level of theory
frequencies calculated at B3LYP/6-311G(2d,d,p)
rotor calculated at B3LYP/6-311G(2d,pd)

Thermodynamics for HOSO3:
    Enthalpy of formation (298 K)   =  -122.350 kcal/mol
    Entropy of formation (298 K)    =    75.536 cal/(mol*K)
    =========== =========== =========== =========== ===========
    Temperature Heat cap.   Enthalpy    Entropy     Free energy
    (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
    =========== =========== =========== =========== ===========
           300      18.758    -122.313      75.661    -145.011
           400      21.259    -120.302      81.428    -152.873
           500      22.902    -118.090      86.357    -161.269
           600      24.222    -115.732      90.653    -170.124
           800      26.161    -110.679      97.907    -189.005
          1000      27.386    -105.315     103.887    -209.202
          1500      28.729     -91.218     115.300    -264.169
          2000      29.349     -76.697     123.651    -324.000
          2400      29.892     -64.849     129.050    -374.569
    =========== =========== =========== =========== ===========
""",
)

entry(
    index = 36,
    label = "SO4(T)",
    molecule = 
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3 O u0 p2 c0 {2,D}
4 O u0 p2 c0 {2,D}
5 O u1 p2 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87898,0.00756363,7.69807e-05,-1.95254e-07,1.34821e-10,-32083.1,9.11986], Tmin=(10,'K'), Tmax=(532.188,'K')),
            NASAPolynomial(coeffs=[6.41676,0.0136579,-1.11352e-05,3.99257e-09,-5.21782e-13,-32709.7,-4.87131], Tmin=(532.188,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-266.792,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12a/cc-pVTZ-f12//B3LYP/6-311G(2d,d,p)""",
    longDesc = 
u"""
SMILES: [O]S(=O)(=O)[O]

calculated by alongd (xq1171, xc1083) at the CCSD(T)-F12a/cc-pVTZ-f12//B3LYP/6-311G(2d,d,p) level of theory
frequencies calculated at B3LYP/6-311G(2d,d,p)

Thermodynamics for SO4(T):
    Enthalpy of formation (298 K)   =   -60.081 kcal/mol
    Entropy of formation (298 K)    =    70.415 cal/(mol*K)
    =========== =========== =========== =========== ===========
    Temperature Heat cap.   Enthalpy    Entropy     Free energy
    (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
    =========== =========== =========== =========== ===========
           300      17.679     -60.046      70.533     -81.206
           400      20.223     -58.141      75.995     -88.539
           500      21.711     -56.037      80.684     -96.379
           600      22.649     -53.817      84.729    -104.654
           800      23.940     -49.147      91.438    -122.297
          1000      24.662     -44.279      96.866    -141.145
          1500      25.203     -31.767     107.005    -192.274
          2000      25.404     -19.124     114.278    -247.680
          2400      25.712      -8.902     118.937    -294.349
    =========== =========== =========== =========== ===========
""",
)

entry(
    index = 37,
    label = "HSOOH",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 S u0 p2 c0 {1,S} {4,S}
3 O u0 p2 c0 {1,S} {5,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84407,0.0150566,5.35225e-05,-3.37418e-07,4.77338e-10,-5883.48,7.95668], Tmin=(10,'K'), Tmax=(278.49,'K')),
            NASAPolynomial(coeffs=[5.11563,0.0116763,-8.43568e-06,2.80455e-09,-3.4898e-13,-6012.02,2.41143], Tmin=(278.49,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-48.9027,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (99.7737,'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12a/cc-pVTZ-f12//B3LYP/6-311G(2d,d,p)""",
    longDesc = 
u"""
SMILES: [O]S(=O)(=O)[O]

calculated by alongd (xq1175, xc1087) at the CCSD(T)-F12a/cc-pVTZ-f12//B3LYP/6-311G(2d,d,p) level of theory
frequencies calculated at B3LYP/6-311G(2d,d,p)
rotors calculated at B3LYP/6-311G(2d,pd)

Thermodynamics for HSOOH:
    Enthalpy of formation (298 K)   =    -8.025 kcal/mol
    Entropy of formation (298 K)    =    68.926 cal/(mol*K)
    =========== =========== =========== =========== ===========
    Temperature Heat cap.   Enthalpy    Entropy     Free energy
    (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
    =========== =========== =========== =========== ===========
           300      15.763      -7.993      69.031     -28.702
           400      17.104      -6.348      73.755     -35.850
           500      18.230      -4.580      77.696     -43.428
           600      19.167      -2.708      81.105     -51.371
           800      20.569       1.275      86.825     -68.185
          1000      21.485       5.487      91.521     -86.034
          1500      22.552      16.547     100.475    -134.166
          2000      23.008      27.943     107.029    -186.115
          2400      23.332      37.213     111.253    -229.795
    =========== =========== =========== =========== ===========
""",
)

entry(
    index = 38,
    label = "OOSHO",
    molecule = 
"""
multiplicity 2
1 S u0 p1 c0 {2,S} {3,D} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 O u0 p2 c0 {1,D}
4 H u0 p0 c0 {1,S}
5 O u1 p2 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49301,0.057111,-0.000324634,8.35612e-07,-7.49669e-10,-4565.4,10.0383], Tmin=(10,'K'), Tmax=(362.268,'K')),
            NASAPolynomial(coeffs=[4.35851,0.0143188,-9.83395e-06,3.05114e-09,-3.54701e-13,-4410.02,9.75165], Tmin=(362.268,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-37.9856,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (103.931,'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12a/cc-pVTZ-f12//B3LYP/6-311G(2d,d,p)""",
    longDesc = 
u"""
SMILES: [O]O[SH]=O

calculated by alongd (xq1194, xc1090) at the CCSD(T)-F12a/cc-pVTZ-f12//B3LYP/6-311G(2d,d,p) level of theory
frequencies calculated at B3LYP/6-311G(2d,d,p)
rotors calculated at B3LYP/6-311G(2d,pd)

Thermodynamics for OOSHO:
    Enthalpy of formation (298 K)   =    -5.082 kcal/mol
    Entropy of formation (298 K)    =    76.381 cal/(mol*K)
    =========== =========== =========== =========== ===========
    Temperature Heat cap.   Enthalpy    Entropy     Free energy
    (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
    =========== =========== =========== =========== ===========
           300      15.696      -5.050      76.485     -27.996
           400      17.286      -3.402      81.215     -35.888
           500      18.717      -1.600      85.231     -44.216
           600      19.917       0.333      88.753     -52.918
           800      21.734       4.510      94.748     -71.288
          1000      22.932       8.986      99.737     -90.751
          1500      24.268      20.858     109.346    -143.161
          2000      24.630      33.097     116.386    -199.674
          2400      24.822      42.988     120.894    -247.156
    =========== =========== =========== =========== ===========
""",
)

entry(
    index = 39,
    label = "OSOOH",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {5,S}
3 S u1 p1 c0 {1,S} {4,D}
4 O u0 p2 c0 {3,D}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75941,0.01881,7.03236e-05,-3.28577e-07,3.35762e-10,-20685.7,10.7497], Tmin=(10,'K'), Tmax=(396.765,'K')),
            NASAPolynomial(coeffs=[8.07624,0.00716155,-6.13257e-06,2.34914e-09,-3.22926e-13,-21279.1,-9.24738], Tmin=(396.765,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-171.981,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (99.7737,'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12a/cc-pVTZ-f12//B3LYP/6-311G(2d,d,p)""",
    longDesc = 
u"""
SMILES: O=[S]OO

calculated by alongd (xq1195, xc1091) at the CCSD(T)-F12a/cc-pVTZ-f12//B3LYP/6-311G(2d,d,p) level of theory
frequencies calculated at B3LYP/6-311G(2d,d,p)
rotors calculated at B3LYP/6-311G(2d,pd)

Thermodynamics for OSOOH:
    Enthalpy of formation (298 K)   =   -36.962 kcal/mol
    Entropy of formation (298 K)    =    76.823 cal/(mol*K)
    =========== =========== =========== =========== ===========
    Temperature Heat cap.   Enthalpy    Entropy     Free energy
    (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
    =========== =========== =========== =========== ===========
           300      19.037     -36.924      76.950     -60.009
           400      20.074     -34.959      82.595     -67.997
           500      20.662     -32.921      87.140     -76.491
           600      21.126     -30.831      90.949     -85.401
           800      21.762     -26.537      97.122    -104.234
          1000      22.120     -22.145     102.021    -124.166
          1500      22.483     -10.978     111.071    -177.585
          2000      22.844       0.343     117.583    -234.822
          2400      23.252       9.563     121.784    -282.719
    =========== =========== =========== =========== ===========
""",
)

entry(
    index = 40,
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
Taken from the SulfurGlarborgH2S library
""",
)

entry(
    index = 41,
    label = "HOOS",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {3,S}
3 S u1 p2 c0 {2,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73157,0.0188787,-3.67753e-05,3.44399e-08,-1.20186e-11,6226.5,8.96936], Tmin=(10,'K'), Tmax=(846.872,'K')),
            NASAPolynomial(coeffs=[5.81757,0.00423321,-2.34567e-06,6.53755e-10,-7.20093e-14,6045.05,0.267052], Tmin=(846.872,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (51.72,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (78.9875,'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12/cc-pVTZ-f12//B3LYP/6-311G(2d,d,p)""",
    longDesc = 
u"""
SMILES: OO[S]

calculated by alongd (xq1228, xc1102) at the CCSD(T)-F12/cc-pVTZ//B3LYP/6-311G(2d,d,p) level of theory
frequencies calculated at B3LYP/6-311G(2d,d,p)
rotor calculated at B3LYP/6-311G(2d,pd)

Thermodynamics for HOOS:
    Enthalpy of formation (298 K)   =    15.728 kcal/mol
    Entropy of formation (298 K)    =    68.562 cal/(mol*K)
    =========== =========== =========== =========== ===========
    Temperature Heat cap.   Enthalpy    Entropy     Free energy
    (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
    =========== =========== =========== =========== ===========
           300      13.747      15.755      68.654      -4.841
           400      14.498      17.171      72.720     -11.917
           500      14.966      18.646      76.009     -19.359
           600      15.304      20.160      78.769     -27.102
           800      15.915      23.281      83.255     -43.322
          1000      16.468      26.522      86.868     -60.346
          1500      17.351      35.001      93.732    -105.597
          2000      17.844      43.809      98.796    -153.784
          2400      18.113      51.003     102.075    -193.976
    =========== =========== =========== =========== ===========
""",
)

entry(
    index = 42,
    label = "H2NN(S)",
    molecule =
"""
1 N u0 p0 c+1 {2,S} {3,S} {4,D}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 N u0 p2 c-1 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [4.03102, -0.0019749, 1.08994e-05, -2.27362e-10, -7.02557e-12, 35633.4, 4.05454],
                Tmin = (10, 'K'),
                Tmax = (562.69, 'K'),
            ),
            NASAPolynomial(
                coeffs = [1.7302, 0.00905511, -4.30653e-06, 9.67276e-10, -8.28241e-14, 35976.6, 14.5808],
                Tmin = (562.69, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (296.282, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (83.1447, 'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12a/aug-cc-pVTZ//wB97x-D3/6-311++G(3df,3pd)""",
    longDesc =
    u"""
    SMILES: [NH2+]=[N-]

    calculated by alongd (xq1334, xc1120)
    opt, freq: wB97x-D3/6-311++G(3df,3pd)
    sp: CCSD(T)-F12a/aug-cc-pVTZ

    Thermodynamics for H2NN(S):
        Enthalpy of formation (298 K)   =    73.207 kcal/mol
        Entropy of formation (298 K)    =    53.454 cal/(mol*K)
        =========== =========== =========== =========== ===========
        Temperature Heat cap.   Enthalpy    Entropy     Free energy
        (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
        =========== =========== =========== =========== ===========
               300       8.657      73.225      53.512      57.171
               400       9.520      74.132      56.116      51.685
               500      10.534      75.134      58.347      45.960
               600      11.548      76.238      60.359      40.023
               800      13.273      78.727      63.927      27.586
              1000      14.632      81.523      67.041      14.483
              1500      16.829      89.449      73.438     -20.708
              2000      17.939      98.172      78.449     -58.726
              2400      18.442     105.456      81.768     -90.787
        =========== =========== =========== =========== ===========
    """,
)

entry(
    index = 43,
    label = "H2NN(T)",
    molecule =
"""
multiplicity 3
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 N u2 p1 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [4.04705, -0.00354577, 3.01414e-05, -4.15281e-08, 1.90485e-11, 43380.7, 5.31138],
                Tmin = (10, 'K'),
                Tmax = (653.103, 'K'),
            ),
            NASAPolynomial(
                coeffs = [2.60416, 0.00842517, -4.55014e-06, 1.23097e-09, -1.31549e-13, 43502.3, 11.1461],
                Tmin = (653.103, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (360.693, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (83.1447, 'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12a/aug-cc-pVTZ//wB97x-D3/6-311++G(3df,3pd)""",
    longDesc =
    u"""
    SMILES: N[N]

    calculated by alongd (xq1448, xc1120)
    opt, freq: wB97x-D3/6-311++G(3df,3pd)
    sp: CCSD(T)-F12a/aug-cc-pVTZ

    Thermodynamics for H2NN(T):
        Enthalpy of formation (298 K)   =    88.674 kcal/mol
        Entropy of formation (298 K)    =    56.279 cal/(mol*K)
        =========== =========== =========== =========== ===========
        Temperature Heat cap.   Enthalpy    Entropy     Free energy
        (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
        =========== =========== =========== =========== ===========
               300       9.398      88.692      56.342      71.790
               400      10.495      89.687      59.195      66.009
               500      11.544      90.790      61.652      59.964
               600      12.458      91.991      63.839      53.687
               800      13.927      94.636      67.634      40.529
              1000      15.060      97.540      70.869      26.671
              1500      16.877     105.573      77.358     -10.465
              2000      17.879     114.283      82.363     -50.443
              2400      18.418     121.547      85.673     -84.067
        =========== =========== =========== =========== ===========
    """,
)

entry(
    index = 44,
    label = "N2H2(T)",
    molecule =
"""
multiplicity 3
1 N u1 p1 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 N u1 p1 c0 {1,S} {4,S}
4 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [4.05595, -0.00430189, 3.68637e-05, -5.32232e-08, 2.52157e-11, 44827.2, 5.88046],
                Tmin = (10, 'K'),
                Tmax = (654.983, 'K'),
            ),
            NASAPolynomial(
                coeffs = [2.6776, 0.00914612, -5.45436e-06, 1.57544e-09, -1.75989e-13, 44899.8, 11.1233],
                Tmin = (654.983, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (372.719, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (78.9875, 'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12a/aug-cc-pVTZ//wB97x-D3/6-311++G(3df,3pd)""",
    longDesc =
    u"""
    SMILES: [NH][NH]

    calculated by alongd (xq1448, xc1120)
    opt, freq: wB97x-D3/6-311++G(3df,3pd)
    sp: CCSD(T)-F12a/aug-cc-pVTZ
    rotor: B3LYP/6-311++G(3df,3pd)

    Thermodynamics for N2H2(T):
        Enthalpy of formation (298 K)   =    91.564 kcal/mol
        Entropy of formation (298 K)    =    57.475 cal/(mol*K)
        =========== =========== =========== =========== ===========
        Temperature Heat cap.   Enthalpy    Entropy     Free energy
        (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
        =========== =========== =========== =========== ===========
               300       9.639      91.584      57.540      74.322
               400      10.875      92.609      60.482      68.417
               500      12.011      93.755      63.034      62.238
               600      12.952      95.005      65.310      55.819
               800      14.384      97.746      69.243      42.352
              1000      15.438     100.734      72.572      28.162
              1500      16.992     108.891      79.166      -9.858
              2000      17.766     117.598      84.170     -50.742
              2400      18.185     124.792      87.448     -85.083
        =========== =========== =========== =========== ===========
    """,
)

entry(
    index = 45,
    label = "NH3NH",
    molecule =
"""
1 N u0 p0 c+1 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 N u0 p2 c-1 {1,S} {6,S}
6 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.98502, 0.000725295, 2.40756e-05, -3.03906e-08, 1.24561e-11, 32805, 5.0309],
                Tmin = (10, 'K'),
                Tmax = (628.906, 'K'),
            ),
            NASAPolynomial(
                coeffs = [2.02176, 0.0132122, -5.70704e-06, 1.18047e-09, -9.40542e-14, 33051.9, 13.592],
                Tmin = (628.906, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (272.75, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (128.874, 'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12a/aug-cc-pVTZ//wB97x-D3/6-311++G(3df,3pd)""",
    longDesc =
    u"""
    SMILES: [NH3+][NH-]

    calculated by alongd (xq1484, xc1120)
    opt, freq: wB97x-D3/6-311++G(3df,3pd)
    sp: CCSD(T)-F12a/aug-cc-pVTZ
    rotor: B3LYP/6-311++G(3df,3pd)

    Thermodynamics for NH3NH:
        Enthalpy of formation (298 K)   =    67.929 kcal/mol
        Entropy of formation (298 K)    =    57.183 cal/(mol*K)
        =========== =========== =========== =========== ===========
        Temperature Heat cap.   Enthalpy    Entropy     Free energy
        (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
        =========== =========== =========== =========== ===========
               300      11.227      67.951      57.258      50.774
               400      12.919      69.158      60.718      44.871
               500      14.599      70.535      63.783      38.643
               600      16.171      72.074      66.585      32.123
               800      18.888      75.589      71.623      18.291
              1000      21.091      79.595      76.083       3.512
              1500      24.854      91.171      85.419     -36.957
              2000      26.940     104.171      92.884     -81.597
              2400      27.934     115.160      97.890    -119.777
        =========== =========== =========== =========== ===========

    In agreement with the values reported in doi 10.1021/jp101640p
    """,
)

entry(
    index = 46,
    label = "N3H5",
    molecule =
"""
1 N u0 p1 c0 {2,S} {4,S} {5,S}
2 N u0 p1 c0 {1,S} {3,S} {6,S}
3 N u0 p1 c0 {2,S} {7,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.90787, 0.00658287, 9.4825e-05, -2.61963e-07, 2.15681e-10, 22396.1, 6.78292],
                Tmin = (10, 'K'),
                Tmax = (420.43, 'K'),
            ),
            NASAPolynomial(
                coeffs = [4.47752, 0.0185703, -1.0048e-05, 2.81007e-09, -3.18669e-13, 22194.4, 2.69867],
                Tmin = (420.43, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (186.21, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (174.604, 'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12a/aug-cc-pVTZ//wB97x-D3/6-311++G(3df,3pd)""",
    longDesc =
    u"""
    SMILES: NNN

    calculated by alongd (xq1449, xc1120)
    opt, freq: wB97x-D3/6-311++G(3df,3pd)
    sp: CCSD(T)-F12a/aug-cc-pVTZ
    rotors: B3LYP/6-311++G(3df,3pd)

    Thermodynamics for N3H5:
        Enthalpy of formation (298 K)   =    48.238 kcal/mol
        Entropy of formation (298 K)    =    66.239 cal/(mol*K)
        =========== =========== =========== =========== ===========
        Temperature Heat cap.   Enthalpy    Entropy     Free energy
        (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
        =========== =========== =========== =========== ===========
               300      18.066      48.274      66.360      28.366
               400      20.804      50.225      71.952      21.444
               500      23.016      52.418      76.837      13.999
               600      24.975      54.819      81.210       6.093
               800      28.241      60.155      88.862     -10.935
              1000      30.784      66.068      95.449     -29.381
              1500      34.966      82.610     108.806     -80.599
              2000      37.375     100.744     119.223    -137.702
              2400      38.638     115.963     126.156    -186.813
        =========== =========== =========== =========== ===========
    """,
)

entry(
    index = 47,
    label = "NH2NH2NH",
    molecule =
"""
1 N u0 p1 c0 {2,S} {7,S} {8,S}
2 N u0 p0 c+1 {1,S} {3,S} {4,S} {5,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 N u0 p2 c-1 {2,S} {6,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.96096, 0.00228708, 7.02891e-05, -1.26989e-07, 7.16093e-11, 40957.5, 7.58571],
                Tmin = (10, 'K'),
                Tmax = (551.473, 'K'),
            ),
            NASAPolynomial(
                coeffs = [1.83955, 0.0259417, -1.65382e-05, 5.15915e-09, -6.21174e-13, 41065.7, 15.4179],
                Tmin = (551.473, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (340.524, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (174.604, 'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12a/aug-cc-pVTZ//wB97x-D3/6-311++G(3df,3pd)""",
    longDesc =
    u"""
    SMILES: N[NH2+][NH-]

    calculated by alongd (xq1462, xc1120)
    opt, freq: wB97x-D3/6-311++G(3df,3pd)
    sp: CCSD(T)-F12a/aug-cc-pVTZ
    rotors: B3LYP/6-311++G(3df,3pd)

    Thermodynamics for NH2NH2NH:
        Enthalpy of formation (298 K)   =    84.740 kcal/mol
        Entropy of formation (298 K)    =    65.528 cal/(mol*K)
        =========== =========== =========== =========== ===========
        Temperature Heat cap.   Enthalpy    Entropy     Free energy
        (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
        =========== =========== =========== =========== ===========
               300      16.145      84.772      65.636      65.081
               400      19.530      86.559      70.754      58.258
               500      22.413      88.661      75.432      50.945
               600      24.810      91.025      79.736      43.184
               800      28.607      96.387      87.422      26.449
              1000      31.360     102.399      94.118       8.281
              1500      35.389     119.213     107.698     -42.335
              2000      37.567     137.490     118.199     -98.909
              2400      38.851     152.785     125.168    -147.617
        =========== =========== =========== =========== ===========
    """,
)

entry(
    index = 48,
    label = "nN3H4",
    molecule =
"""
multiplicity 2
1 N u1 p1 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 N u0 p1 c0 {1,S} {4,S} {5,S}
4 N u0 p1 c0 {3,S} {6,S} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.67804, 0.0335268, -0.000125195, 2.77593e-07, -2.16472e-10, 36762.7, 5.56865],
                Tmin = (10, 'K'),
                Tmax = (429.285, 'K'),
            ),
            NASAPolynomial(
                coeffs = [3.39183, 0.0184252, -1.03403e-05, 2.80841e-09, -2.9725e-13, 36951, 8.61436],
                Tmin = (429.285, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (305.655, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (149.66, 'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12a/aug-cc-pVTZ//wB97x-D3/6-311++G(3df,3pd)""",
    longDesc =
    u"""
    SMILES: [NH]NN

    calculated by alongd (xq1455, xc1120)
    opt, freq: wB97x-D3/6-311++G(3df,3pd)
    sp: CCSD(T)-F12a/aug-cc-pVTZ
    rotors: B3LYP/6-311++G(3df,3pd)

    Thermodynamics for nN3H4:
        Enthalpy of formation (298 K)   =    76.882 kcal/mol
        Entropy of formation (298 K)    =    65.532 cal/(mol*K)
        =========== =========== =========== =========== ===========
        Temperature Heat cap.   Enthalpy    Entropy     Free energy
        (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
        =========== =========== =========== =========== ===========
               300      16.315      76.915      65.641      57.223
               400      18.445      78.651      70.620      50.403
               500      20.571      80.604      74.969      43.119
               600      22.441      82.756      78.888      35.423
               800      25.497      87.564      85.783      18.938
              1000      27.797      92.904      91.732       1.173
              1500      31.274     107.781     103.748     -47.841
              2000      32.973     123.887     113.003    -102.119
              2400      33.810     137.253     119.093    -148.570
        =========== =========== =========== =========== ===========
    """,
)

entry(
    index = 49,
    label = "iN3H4",
    molecule =
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {4,S} {5,S}
2 N u1 p1 c0 {1,S} {3,S}
3 N u0 p1 c0 {2,S} {6,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.9149, 0.00466504, 7.13855e-05, -1.37682e-07, 7.59162e-11, 32993.8, 6.51512],
                Tmin = (10, 'K'),
                Tmax = (640.546, 'K'),
            ),
            NASAPolynomial(
                coeffs = [5.01244, 0.0196699, -1.49395e-05, 5.4379e-09, -7.35158e-13, 32404.8, -1.79135],
                Tmin = (640.546, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (274.287, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (149.66, 'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12a/aug-cc-pVTZ//wB97x-D3/6-311++G(3df,3pd)""",
    longDesc =
    u"""
    SMILES: N[N]N

    calculated by alongd (xq1455, xc1120)
    opt, freq: wB97x-D3/6-311++G(3df,3pd)
    sp: CCSD(T)-F12a/aug-cc-pVTZ
    rotors: B3LYP/6-311++G(3df,3pd)

    Thermodynamics for iN3H4:
        Enthalpy of formation (298 K)   =    69.078 kcal/mol
        Entropy of formation (298 K)    =    64.214 cal/(mol*K)
        =========== =========== =========== =========== ===========
        Temperature Heat cap.   Enthalpy    Entropy     Free energy
        (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
        =========== =========== =========== =========== ===========
               300      17.163      69.113      64.328      49.814
               400      20.537      71.003      69.744      43.106
               500      23.108      73.193      74.619      35.883
               600      24.864      75.597      78.998      28.198
               800      27.165      80.816      86.489      11.625
              1000      28.706      86.413      92.728      -6.314
              1500      30.870     101.369     104.827     -55.871
              2000      32.461     117.200     113.924    -110.648
              2400      33.686     130.439     119.955    -157.453
        =========== =========== =========== =========== ===========
    """,
)

entry(
    index = 50,
    label = "NH2NHN",
    molecule =
"""
1 N u0 p1 c0 {2,S} {5,S} {6,S}
2 N u0 p0 c+1 {1,S} {3,S} {4,D}
3 H u0 p0 c0 {2,S}
4 N u0 p2 c-1 {2,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.98425, 0.000945858, 4.48683e-05, -7.82227e-08, 4.41117e-11, 41335.6, 7.16058],
                Tmin = (10, 'K'),
                Tmax = (459.105, 'K'),
            ),
            NASAPolynomial(
                coeffs = [2.01419, 0.0181272, -1.13225e-05, 3.45266e-09, -4.07496e-13, 41516.3, 15.1294],
                Tmin = (459.105, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (343.677, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (128.874, 'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12a/aug-cc-pVTZ//wB97x-D3/6-311++G(3df,3pd)""",
    longDesc =
    u"""
    SMILES: N[NH+]=[N-]

    calculated by alongd (xq1338, xc1120)
    opt, freq: wB97x-D3/6-311++G(3df,3pd)
    sp: CCSD(T)-F12a/aug-cc-pVTZ
    rotors: B3LYP/6-311++G(3df,3pd)

    Thermodynamics for NH2NHN:
        Enthalpy of formation (298 K)   =    85.106 kcal/mol
        Entropy of formation (298 K)    =    62.657 cal/(mol*K)
        =========== =========== =========== =========== ===========
        Temperature Heat cap.   Enthalpy    Entropy     Free energy
        (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
        =========== =========== =========== =========== ===========
               300      13.019      85.132      62.744      66.309
               400      15.231      86.546      66.797      59.828
               500      17.196      88.170      70.412      52.964
               600      18.893      89.977      73.701      45.756
               800      21.602      94.040      79.527      30.418
              1000      23.576      98.568      84.571      13.997
              1500      26.468     111.172      94.752     -30.956
              2000      27.979     124.813     102.590     -80.368
              2400      28.837     136.184     107.771    -122.466
        =========== =========== =========== =========== ===========
    """,
)

entry(
    index = 51,
    label = "NH2NNH",
    molecule =
"""
1 N u0 p1 c0 {2,S} {4,S} {5,S}
2 N u0 p1 c0 {1,S} {3,D}
3 N u0 p1 c0 {2,D} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.8649, 0.0137824, -2.63045e-05, 6.74328e-08, -5.91398e-11, 26119.9, 5.29321],
                Tmin = (10, 'K'),
                Tmax = (443.414, 'K'),
            ),
            NASAPolynomial(
                coeffs = [2.68549, 0.0166314, -9.5884e-06, 2.67796e-09, -2.9115e-13, 26301, 10.8876],
                Tmin = (443.414, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (217.17, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (128.874, 'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12a/aug-cc-pVTZ//wB97x-D3/6-311++G(3df,3pd)""",
    longDesc =
    u"""
    SMILES: NN=N

    calculated by alongd (xq1339, xc1120)
    opt, freq: wB97x-D3/6-311++G(3df,3pd)
    sp: CCSD(T)-F12a/aug-cc-pVTZ
    rotors: B3LYP/6-311++G(3df,3pd)

    Thermodynamics for NH2NNH:
    Enthalpy of formation (298 K)   =    55.158 kcal/mol
    Entropy of formation (298 K)    =    61.065 cal/(mol*K)
    =========== =========== =========== =========== ===========
    Temperature Heat cap.   Enthalpy    Entropy     Free energy
    (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
    =========== =========== =========== =========== ===========
           300      13.859      55.186      61.158      36.839
           400      15.840      56.671      65.415      30.504
           500      17.727      58.351      69.157      23.772
           600      19.382      60.208      72.539      16.685
           800      22.070      64.366      78.501       1.565
          1000      24.076      68.991      83.652     -14.662
          1500      27.071      81.872      94.057     -59.214
          2000      28.536      95.812     102.068    -108.324
          2400      29.276     107.382     107.339    -150.232
    =========== =========== =========== =========== ===========
    """,
)

entry(
    index = 52,
    label = "NHNHNH(S)",
    molecule =
"""
1 N u0 p1 c0 {2,S} {3,D}
2 H u0 p0 c0 {1,S}
3 N u0 p0 c+1 {1,D} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 N u0 p2 c-1 {3,S} {6,S}
6 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [4.02119, -0.00153801, 4.38047e-05, -5.90251e-08, 2.54386e-11, 36471.9, 6.58307],
                Tmin = (10, 'K'),
                Tmax = (679.56, 'K'),
            ),
            NASAPolynomial(
                coeffs = [0.955284, 0.0200944, -1.18604e-05, 3.34919e-09, -3.64709e-13, 36805.8, 19.5807],
                Tmin = (679.56, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (303.247, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (124.717, 'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12a/aug-cc-pVTZ//wB97x-D3/6-311++G(3df,3pd)""",
    longDesc =
    u"""
    SMILES: [NH]=[NH+][NH-]

    calculated by alongd (xq1467, xc1120)
    opt, freq: wB97x-D3/6-311++G(3df,3pd)
    sp: CCSD(T)-F12a/aug-cc-pVTZ
    rotors: B3LYP/6-311++G(3df,3pd)

    Thermodynamics for NHNHNH(S):
        Enthalpy of formation (298 K)   =    75.283 kcal/mol
        Entropy of formation (298 K)    =    60.626 cal/(mol*K)
        =========== =========== =========== =========== ===========
        Temperature Heat cap.   Enthalpy    Entropy     Free energy
        (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
        =========== =========== =========== =========== ===========
               300      12.151      75.307      60.707      57.095
               400      14.483      76.639      64.522      50.830
               500      16.723      78.201      67.998      44.202
               600      18.711      79.975      71.227      37.239
               800      21.870      84.049      77.066      22.397
              1000      24.192      88.668      82.209       6.459
              1500      27.559     101.719      92.747     -37.401
              2000      29.134     115.934     100.915     -85.895
              2400      29.937     127.756     106.301    -127.366
        =========== =========== =========== =========== ===========
    """,
)

entry(
    index = 53,
    label = "cN3H3",
    molecule =
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 N u0 p1 c0 {1,S} {3,S} {5,S}
3 N u0 p1 c0 {1,S} {2,S} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [4.1305, -0.00878148, 6.34349e-05, -7.80965e-08, 3.12888e-11, 48604, 6.52817],
                Tmin = (10, 'K'),
                Tmax = (777.26, 'K'),
            ),
            NASAPolynomial(
                coeffs = [0.570347, 0.0198195, -1.15986e-05, 3.27587e-09, -3.56856e-13, 48847, 20.8093],
                Tmin = (777.26, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (404.145, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (133.032, 'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12a/aug-cc-pVTZ//wB97x-D3/6-311++G(3df,3pd)""",
    longDesc =
    u"""
    SMILES: N1NN1

    calculated by alongd (xq1467, xc1120)
    opt, freq: wB97x-D3/6-311++G(3df,3pd)
    sp: CCSD(T)-F12a/aug-cc-pVTZ

    Thermodynamics for cN3H3:
        Enthalpy of formation (298 K)   =    99.093 kcal/mol
        Entropy of formation (298 K)    =    58.886 cal/(mol*K)
        =========== =========== =========== =========== ===========
        Temperature Heat cap.   Enthalpy    Entropy     Free energy
        (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
        =========== =========== =========== =========== ===========
               300      10.632      99.114      58.957      81.427
               400      13.057     100.297      62.343      75.360
               500      15.484     101.725      65.520      68.965
               600      17.655     103.385      68.541      62.261
               800      20.933     107.266      74.100      47.986
              1000      23.271     111.698      79.035      32.662
              1500      26.732     124.310      89.215      -9.513
              2000      28.441     138.144      97.163     -56.183
              2400      29.361     149.712     102.434     -96.129
        =========== =========== =========== =========== ===========
    """,
)

entry(
    index = 54,
    label = "NH2NH2N",
    molecule =
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {6,S} {7,S}
2 N u0 p0 c+1 {1,S} {3,S} {4,S} {5,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 N u1 p2 c-1 {2,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.98018, 0.00120723, 5.63907e-05, -9.9883e-08, 5.76657e-11, 63636.7, 7.66343],
                Tmin = (10, 'K'),
                Tmax = (446.623, 'K'),
            ),
            NASAPolynomial(
                coeffs = [1.67274, 0.0218841, -1.30907e-05, 3.88693e-09, -4.51603e-13, 63842.7, 16.9343],
                Tmin = (446.623, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (529.098, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (157.975, 'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12a/aug-cc-pVTZ//wB97x-D3/6-311++G(3df,3pd)""",
    longDesc =
    u"""
    SMILES: N[NH2+][N-]

    calculated by alongd (xq1456, xc1120)
    opt, freq: wB97x-D3/6-311++G(3df,3pd)
    sp: CCSD(T)-F12a/aug-cc-pVTZ

    Thermodynamics for NH2NH2N:
        Enthalpy of formation (298 K)   =   129.574 kcal/mol
        Entropy of formation (298 K)    =    64.455 cal/(mol*K)
        =========== =========== =========== =========== ===========
        Temperature Heat cap.   Enthalpy    Entropy     Free energy
        (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
        =========== =========== =========== =========== ===========
               300      14.284     129.602      64.551     110.237
               400      17.029     131.170      69.041     103.553
               500      19.474     132.998      73.110      96.443
               600      21.604     135.054      76.853      88.942
               800      25.053     139.737      83.565      72.885
              1000      27.625     145.017      89.445      55.572
              1500      31.550     159.926     101.482       7.703
              2000      33.678     176.275     110.874     -45.473
              2400      34.859     189.995     117.124     -91.104
        =========== =========== =========== =========== ===========
    """,
)

entry(
    index = 55,
    label = "N4H6",
    molecule =
"""
1  N u0 p1 c0 {2,S} {5,S} {6,S}
2  N u0 p1 c0 {1,S} {3,S} {7,S}
3  N u0 p1 c0 {2,S} {4,S} {8,S}
4  N u0 p1 c0 {3,S} {9,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.92525, 0.00488384, 9.02053e-05, -1.64564e-07, 9.61822e-11, 33964.7, 9.36706],
                Tmin = (10, 'K'),
                Tmax = (441.326, 'K'),
            ),
            NASAPolynomial(
                coeffs = [0.249974, 0.0381945, -2.30108e-05, 6.45746e-09, -6.95769e-13, 34289.1, 24.0919],
                Tmin = (441.326, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (282.372, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (220.334, 'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12a/aug-cc-pVTZ//wB97x-D3/6-311++G(3df,3pd)""",
    longDesc =
    u"""
    SMILES: NNNN

    calculated by alongd (xq1335, xc1120)
    opt, freq: wB97x-D3/6-311++G(3df,3pd)
    sp: CCSD(T)-F12a/aug-cc-pVTZ
    rotors: B3LYP/6-311++G(3df,3pd)

    Thermodynamics for N4H6:
        Enthalpy of formation (298 K)   =    71.277 kcal/mol
        Entropy of formation (298 K)    =    71.397 cal/(mol*K)
        =========== =========== =========== =========== ===========
        Temperature Heat cap.   Enthalpy    Entropy     Free energy
        (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
        =========== =========== =========== =========== ===========
               300      19.563      71.316      71.527      49.857
               400      24.327      73.514      77.819      42.386
               500      28.533      76.162      83.710      34.307
               600      32.168      79.201      89.242      25.656
               800      37.955      86.244      99.332       6.778
              1000      42.119      94.275     108.276     -14.000
              1500      47.770     116.970     126.602     -72.933
              2000      49.925     141.475     140.686    -139.898
              2400      50.790     161.631     149.871    -198.060
        =========== =========== =========== =========== ===========
    """,
)

entry(
    index = 56,
    label = "NH2NH2NNH2",
    molecule =
"""
1  N u0 p1 c0 {2,S} {7,S} {8,S}
2  N u0 p2 c-1 {1,S} {3,S}
3  N u0 p0 c+1 {2,S} {4,S} {5,S} {6,S}
4  H u0 p0 c0 {3,S}
5  H u0 p0 c0 {3,S}
6  N u0 p1 c0 {3,S} {9,S} {10,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.93231, 0.0039948, 0.000103213, -1.94027e-07, 1.12396e-10, 49902.3, 8.70296],
                Tmin = (10, 'K'),
                Tmax = (551.915, 'K'),
            ),
            NASAPolynomial(
                coeffs = [1.62997, 0.035551, -2.29642e-05, 7.20107e-09, -8.66502e-13, 49930, 16.3903],
                Tmin = (551.915, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (414.884, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (228.648, 'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12a/aug-cc-pVTZ//wB97x-D3/6-311++G(3df,3pd)""",
    longDesc =
    u"""
    SMILES: N[N-][NH2+]N

    calculated by alongd (xq1336, xc1120)
    opt, freq: wB97x-D3/6-311++G(3df,3pd)
    sp: CCSD(T)-F12a/aug-cc-pVTZ
    rotors: B3LYP/6-311++G(3df,3pd)

    Thermodynamics for NH2NH2NNH2:
        Enthalpy of formation (298 K)   =   103.001 kcal/mol
        Entropy of formation (298 K)    =    70.325 cal/(mol*K)
        =========== =========== =========== =========== ===========
        Temperature Heat cap.   Enthalpy    Entropy     Free energy
        (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
        =========== =========== =========== =========== ===========
               300      20.054     103.041      70.459      81.904
               400      24.848     105.292      76.902      74.532
               500      28.823     107.983      82.889      66.538
               600      32.067     111.032      88.440      57.968
               800      37.172     117.984      98.403      39.261
              1000      40.840     125.805     107.115      18.690
              1500      46.111     147.715     124.810     -39.501
              2000      48.925     171.521     138.488    -105.456
              2400      50.630     191.446     147.565    -162.711
        =========== =========== =========== =========== ===========
    """,
)

entry(
    index = 57,
    label = "NH2NHNH2NH",
    molecule =
"""
1  N u0 p1 c0 {2,S} {8,S} {9,S}
2  N u0 p1 c0 {1,S} {3,S} {10,S}
3  N u0 p0 c+1 {2,S} {4,S} {5,S} {6,S}
4  H u0 p0 c0 {3,S}
5  H u0 p0 c0 {3,S}
6  N u0 p2 c-1 {3,S} {7,S}
7  H u0 p0 c0 {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.94926, 0.00321392, 0.000103215, -2.04626e-07, 1.29246e-10, 52132.6, 8.68186],
                Tmin = (10, 'K'),
                Tmax = (483.527, 'K'),
            ),
            NASAPolynomial(
                coeffs = [1.45658, 0.033368, -1.99027e-05, 5.89899e-09, -6.84601e-13, 52262.2, 17.7439],
                Tmin = (483.527, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (433.442, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (232.805, 'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12a/aug-cc-pVTZ//wB97x-D3/6-311++G(3df,3pd)""",
    longDesc =
    u"""
    SMILES: NN[NH2+][NH-]

    calculated by alongd (xq1475, xc1120)
    opt, freq: wB97x-D3/6-311++G(3df,3pd)
    sp: CCSD(T)-F12a/aug-cc-pVTZ

    Thermodynamics for NH2NHNH2NH:
        Enthalpy of formation (298 K)   =   107.349 kcal/mol
        Entropy of formation (298 K)    =    69.893 cal/(mol*K)
        =========== =========== =========== =========== ===========
        Temperature Heat cap.   Enthalpy    Entropy     Free energy
        (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
        =========== =========== =========== =========== ===========
               300      19.325     107.387      70.022      86.381
               400      23.771     109.548      76.206      79.065
               500      27.542     112.118      81.927      71.155
               600      30.797     115.039      87.243      62.693
               800      36.074     121.752      96.862      44.262
              1000      40.015     129.380     105.357      24.023
              1500      46.045     151.071     122.864     -33.225
              2000      49.322     174.977     136.597     -98.216
              2400      51.139     195.089     145.758    -154.731
        =========== =========== =========== =========== ===========
    """,
)

entry(
    index = 58,
    label = "1_N4(T)",
    molecule =
"""
multiplicity 3
1 N u0 p1 c0 {2,S} {3,D}
2 N u0 p1 c0 {1,S} {4,D}
3 N u1 p1 c0 {1,D}
4 N u1 p1 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.87765, 0.0127008, 4.12966e-05, -3.26349e-07, 5.40082e-10, 77213.1, 8.16284],
                Tmin = (10, 'K'),
                Tmax = (243.876, 'K'),
            ),
            NASAPolynomial(
                coeffs = [4.84868, 0.00859309, -6.13284e-06, 2.02652e-09, -2.51366e-13, 77130.6, 4.12779],
                Tmin = (243.876, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (641.996, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (83.1447, 'J/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3""",
    longDesc =
    u"""
    SMILES: [N]=NN=[N]

    calculated by alongd (xq1486, xc1121)
    CBS-QB3, no rotors
    """,
)

entry(
    index = 59,
    label = "2_N4H2",
    molecule =
"""
1 N u0 p1 c0 {2,S} {3,S} {5,S}
2 N u0 p1 c0 {1,S} {3,S} {6,S}
3 N u0 p0 c+1 {1,S} {2,S} {4,D}
4 N u0 p2 c-1 {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.96213, 0.00218253, 5.48648e-05, -1.00893e-07, 5.66069e-11, 79968.7, 7.03098],
                Tmin = (10, 'K'),
                Tmax = (574.563, 'K'),
            ),
            NASAPolynomial(
                coeffs = [2.69923, 0.0196113, -1.31839e-05, 4.22616e-09, -5.15252e-13, 79971.3, 11.1833],
                Tmin = (574.563, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (664.881, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (133.032, 'J/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3""",
    longDesc =
    u"""
    SMILES: [N-]=[N+]1NN1

    calculated by alongd (xq1486, xc1121)
    CBS-QB3, no rotors
    """,
)

entry(
    index = 60,
    label = "3_N4H3",
    molecule =
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 N u0 p1 c0 {1,S} {3,S} {5,S}
3 N u0 p1 c0 {1,S} {2,S} {6,S}
4 N u1 p1 c0 {1,S} {7,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.96213, 0.00218253, 5.48648e-05, -1.00893e-07, 5.66069e-11, 79968.7, 7.03098],
                Tmin = (10, 'K'),
                Tmax = (574.563, 'K'),
            ),
            NASAPolynomial(
                coeffs = [2.69923, 0.0196113, -1.31839e-05, 4.22616e-09, -5.15252e-13, 79971.3, 11.1833],
                Tmin = (574.563, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (664.881, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (133.032, 'J/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3""",
    longDesc =
    u"""
    SMILES: [NH]N1NN1

    calculated by alongd (xq1486, xc1121)
    CBS-QB3, no rotors
    """,
)

entry(
    index = 61,
    label = "6_N4H2",
    molecule =
"""
1 N u0 p0 c+1 {2,S} {3,S} {4,D}
2 N u0 p1 c0 {1,S} {3,S} {5,S}
3 N u0 p2 c-1 {1,S} {2,S}
4 N u0 p1 c0 {1,D} {6,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [4.0794, -0.00809309, 0.000110362, -2.09319e-07, 1.28628e-10, 76642.8, 7.89803],
                Tmin = (10, 'K'),
                Tmax = (521.1, 'K'),
            ),
            NASAPolynomial(
                coeffs = [2.4603, 0.019495, -1.26886e-05, 3.93358e-09, -4.64754e-13, 76605.7, 12.679],
                Tmin = (521.1, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (637.234, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (133.032, 'J/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3""",
    longDesc =
    u"""
    SMILES: [N-]1N[N+]1=N

    calculated by alongd (xq1486, xc1121)
    CBS-QB3, no rotors
    """,
)

entry(
    index = 62,
    label = "7_N4H",
    molecule =
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,D}
2 N u1 p1 c0 {1,S} {5,S}
3 N u0 p0 c+1 {1,D} {4,D}
4 N u0 p2 c-1 {3,D}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.9535, 0.00290272, 4.99533e-05, -1.09209e-07, 7.11534e-11, 64187.6, 8.18369],
                Tmin = (10, 'K'),
                Tmax = (518.727, 'K'),
            ),
            NASAPolynomial(
                coeffs = [3.84141, 0.0135306, -9.01275e-06, 2.8596e-09, -3.45858e-13, 64067.9, 7.38468],
                Tmin = (518.727, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (533.672, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (108.088, 'J/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3""",
    longDesc =
    u"""
    SMILES: [N-]=[N+]=N[NH]

    calculated by alongd (xq1486, xc1121)
    CBS-QB3, no rotors
    """,
)

entry(
    index = 63,
    label = "8_N4H2",
    molecule =
"""
multiplicity 3
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 N u0 p1 c0 {1,S} {3,S} {5,S}
3 N u1 p1 c0 {1,S} {2,S}
4 N u1 p1 c0 {1,S} {6,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.95142, 0.00273515, 5.84249e-05, -1.07974e-07, 5.95586e-11, 93095.5, 8.58962],
                Tmin = (10, 'K'),
                Tmax = (602.615, 'K'),
            ),
            NASAPolynomial(
                coeffs = [3.08061, 0.020234, -1.43016e-05, 4.75252e-09, -5.94121e-13, 92987.6, 10.5843],
                Tmin = (602.615, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (774.018, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (133.032, 'J/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3""",
    longDesc =
    u"""
    SMILES: [NH]N1[N]N1

    calculated by alongd (xq1486, xc1121)
    CBS-QB3, no rotors
    """,
)

entry(
    index = 64,
    label = "9_N4H2",
    molecule =
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 N u0 p1 c0 {1,S} {3,S} {4,S}
3 N u0 p1 c0 {1,S} {2,S} {5,S}
4 N u0 p1 c0 {1,S} {2,S} {6,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [4.13283, -0.0106176, 9.89851e-05, -1.5268e-07, 7.59726e-11, 79196.3, 6.92906],
                Tmin = (10, 'K'),
                Tmax = (644.77, 'K'),
            ),
            NASAPolynomial(
                coeffs = [1.7117, 0.0211454, -1.38598e-05, 4.27146e-09, -4.98478e-13, 79160.5, 14.8482],
                Tmin = (644.77, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (658.482, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (133.032, 'J/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3""",
    longDesc =
    u"""
    SMILES: N1N2N1N2

    calculated by alongd (xq1486, xc1121)
    CBS-QB3, no rotors
    """,
)

entry(
    index = 65,
    label = "11_N4",
    molecule =
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 N u0 p1 c0 {1,S} {3,S} {4,S}
3 N u0 p1 c0 {1,S} {2,S} {4,S}
4 N u0 p1 c0 {1,S} {2,S} {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [4.13283, -0.0106176, 9.89851e-05, -1.5268e-07, 7.59726e-11, 79196.3, 6.92906],
                Tmin = (10, 'K'),
                Tmax = (644.77, 'K'),
            ),
            NASAPolynomial(
                coeffs = [1.7117, 0.0211454, -1.38598e-05, 4.27146e-09, -4.98478e-13, 79160.5, 14.8482],
                Tmin = (644.77, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (658.482, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (133.032, 'J/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3""",
    longDesc =
    u"""
    SMILES: N12N3N1N23

    calculated by alongd (xq1486, xc1121)
    CBS-QB3, no rotors
    """,
)

entry(
    index = 66,
    label = "NH3NNH2",
    molecule =
"""
1 N u0 p0 c+1 {3,S} {4,S} {5,S} {6,S}
2 N u0 p1 c0 {3,S} {7,S} {8,S}
3 N u0 p2 c-1 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.90745, 0.00682728, 3.70177e-05, -6.71939e-08, 3.79399e-11, 41571.8, 7.25965],
                Tmin = (10, 'K'),
                Tmax = (457.914, 'K'),
            ),
            NASAPolynomial(
                coeffs = [2.22687, 0.0215076, -1.10709e-05, 2.81732e-09, -2.83072e-13, 41725.7, 14.0548],
                Tmin = (457.914, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (345.625, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (178.761, 'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12a/aug-cc-pVTZ//wB97x-D3/6-311++G(3df,3pd)""",
    longDesc =
    u"""
    SMILES: [NH3+][N-]N

    calculated by alongd (xq1487, xc1120)
    opt, freq: wB97x-D3/6-311++G(3df,3pd)
    sp: CCSD(T)-F12a/aug-cc-pVTZ
    rotor: B3LYP/6-311++G(3df,3pd)

    Thermodynamics for NH3NNH2:
        Enthalpy of formation (298 K)   =    85.949 kcal/mol
        Entropy of formation (298 K)    =    64.944 cal/(mol*K)
        =========== =========== =========== =========== ===========
        Temperature Heat cap.   Enthalpy    Entropy     Free energy
        (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
        =========== =========== =========== =========== ===========
               300      15.461      85.980      65.047      66.466
               400      18.346      87.672      69.895      59.714
               500      20.960      89.640      74.275      52.502
               600      23.286      91.854      78.307      44.870
               800      27.173      96.916      85.561      28.468
              1000      30.201     102.667      91.964      10.703
              1500      35.082     119.119     105.239     -38.739
              2000      37.693     137.375     115.725     -94.075
              2400      39.012     152.731     122.721    -141.798
        =========== =========== =========== =========== ===========
    """,
)

entry(
    index = 67,
    label = "NH2NNH(T)",
    molecule =
"""
multiplicity 3
1 N u0 p1 c0 {2,S} {4,S} {5,S}
2 N u1 p1 c0 {1,S} {3,S}
3 N u1 p1 c0 {2,S} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.92579, 0.0045666, 6.65762e-05, -1.4919e-07, 9.70639e-11, 53380.5, 6.75656],
                Tmin = (10, 'K'),
                Tmax = (535.446, 'K'),
            ),
            NASAPolynomial(
                coeffs = [4.50916, 0.0162684, -1.11949e-05, 3.65571e-09, -4.53348e-13, 53087.8, 2.15678],
                Tmin = (535.446, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (443.806, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (124.717, 'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12a/aug-cc-pVTZ//wB97x-D3/6-311++G(3df,3pd)""",
    longDesc =
    u"""
    SMILES: N[N][NH]

    calculated by alongd (xq1487, xc1120)
    opt, freq: wB97x-D3/6-311++G(3df,3pd)
    sp: CCSD(T)-F12a/aug-cc-pVTZ
    rotors: B3LYP/6-311++G(3df,3pd)

    Thermodynamics for NH2NNH(T):
        Enthalpy of formation (298 K)   =   109.479 kcal/mol
        Entropy of formation (298 K)    =    64.215 cal/(mol*K)
        =========== =========== =========== =========== ===========
        Temperature Heat cap.   Enthalpy    Entropy     Free energy
        (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
        =========== =========== =========== =========== ===========
               300      15.988     109.511      64.322      90.214
               400      18.563     111.245      69.292      83.528
               500      20.410     113.199      73.645      76.376
               600      21.801     115.312      77.493      68.816
               800      23.936     119.898      84.076      52.638
              1000      25.406     124.842      89.585      35.257
              1500      27.356     138.106     100.315     -12.367
              2000      28.334     152.043     108.327     -64.612
              2400      28.945     163.505     113.550    -109.015
        =========== =========== =========== =========== ===========
    """,
)

entry(
    index = 68,
    label = "N2(T)",
    molecule =
"""
multiplicity 3
1 N u1 p1 c0 {2,D}
2 N u1 p1 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.50659, -0.000372835, 1.04511e-06, 1.55261e-09, -1.81005e-12, 85626.6, 4.37685],
                Tmin = (10, 'K'),
                Tmax = (658.073, 'K'),
            ),
            NASAPolynomial(
                coeffs = [2.88333, 0.00195625, -9.3733e-07, 1.91057e-10, -1.25972e-14, 85740.2, 7.36305],
                Tmin = (658.073, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (711.942, 'kJ/mol'),
        Cp0 = (29.1007, 'J/(mol*K)'),
        CpInf = (37.4151, 'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12a/aug-cc-pVTZ//wB97x-D3/6-311++G(3df,3pd)""",
    longDesc =
    u"""
    SMILES: [N]=[N]

    calculated by alongd (xq1487, xc1120)
    opt, freq: wB97x-D3/6-311++G(3df,3pd)
    sp: CCSD(T)-F12a/aug-cc-pVTZ

    Thermodynamics for N2(T):
        Enthalpy of formation (298 K)   =   172.224 kcal/mol
        Entropy of formation (298 K)    =    48.288 cal/(mol*K)
        =========== =========== =========== =========== ===========
        Temperature Heat cap.   Enthalpy    Entropy     Free energy
        (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
        =========== =========== =========== =========== ===========
               300       6.987     172.238      48.335     157.737
               400       7.110     172.942      50.361     152.798
               500       7.278     173.661      51.965     147.679
               600       7.472     174.399      53.308     142.414
               800       7.832     175.931      55.509     131.523
              1000       8.109     177.526      57.288     120.238
              1500       8.525     181.699      60.666      90.699
              2000       8.691     186.009      63.145      59.719
              2400       8.749     189.498      64.735      34.133
        =========== =========== =========== =========== ===========
    """,
)

entry(
    index = 69,
    label = "NHNNHN",
    molecule =
"""
1 N u0 p0 c+1 {2,S} {4,D} {5,S}
2 N u0 p1 c0 {1,S} {3,D}
3 N u0 p1 c0 {2,D} {6,S}
4 N u0 p2 c-1 {1,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.94185, 0.00538891, 7.3383e-05, -2.62541e-07, 3.15541e-10, 62811.5, 7.81883],
                Tmin = (10, 'K'),
                Tmax = (210.149, 'K'),
            ),
            NASAPolynomial(
                coeffs = [3.32577, 0.0171153, -1.03169e-05, 2.98356e-09, -3.33183e-13, 62837.3, 9.82999],
                Tmin = (210.149, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (522.252, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (133.032, 'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12a/aug-cc-pVTZ//wB97x-D3/6-311++G(3df,3pd)""",
    longDesc =
    u"""
    SMILES: [N-]=[NH+]N=N

    calculated by alongd (xq1487, xc1120)
    opt, freq: wB97x-D3/6-311++G(3df,3pd)
    sp: CCSD(T)-F12a/aug-cc-pVTZ
    species has no hindered rotors (scan at B3LYP of the two potential rotors broke the molecule)

    Thermodynamics for NHNNHN:
        Enthalpy of formation (298 K)   =   128.181 kcal/mol
        Entropy of formation (298 K)    =    66.462 cal/(mol*K)
        =========== =========== =========== =========== ===========
        Temperature Heat cap.   Enthalpy    Entropy     Free energy
        (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
        =========== =========== =========== =========== ===========
               300      15.122     128.211      66.563     108.242
               400      17.296     129.835      71.219     101.347
               500      19.189     131.661      75.286      94.018
               600      20.830     133.664      78.934      86.304
               800      23.462     138.106      85.306      69.862
              1000      25.386     143.001      90.759      52.242
              1500      28.156     156.481     101.652       4.003
              2000      29.463     170.919     109.950     -48.982
              2400      30.141     182.846     115.385     -94.078
        =========== =========== =========== =========== ===========
    """,
)

entry(
    index = 70,
    label = "NH2NNN",
    molecule =
"""
1 N u0 p1 c0 {2,S} {5,S} {6,S}
2 N u0 p1 c0 {1,S} {3,D}
3 N u0 p0 c+1 {2,D} {4,D}
4 N u0 p2 c-1 {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.94242, 0.00380542, 6.38745e-05, -1.47842e-07, 1.0313e-10, 50916.6, 8.08248],
                Tmin = (10, 'K'),
                Tmax = (477.246, 'K'),
            ),
            NASAPolynomial(
                coeffs = [3.59595, 0.0172408, -1.14538e-05, 3.62347e-09, -4.35076e-13, 50829.8, 8.24117],
                Tmin = (477.246, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (423.334, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (128.874, 'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12a/aug-cc-pVTZ//wB97x-D3/6-311++G(3df,3pd)""",
    longDesc =
    u"""
    SMILES: [N-]=[N+]=NN

    calculated by alongd (xq1487, xc1120)
    opt, freq: wB97x-D3/6-311++G(3df,3pd)
    sp: CCSD(T)-F12a/aug-cc-pVTZ
    rotor: B3LYP/6-311++G(3df,3pd)

    Thermodynamics for NH2NNN:
        Enthalpy of formation (298 K)   =   104.489 kcal/mol
        Entropy of formation (298 K)    =    66.397 cal/(mol*K)
        =========== =========== =========== =========== ===========
        Temperature Heat cap.   Enthalpy    Entropy     Free energy
        (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
        =========== =========== =========== =========== ===========
               300      15.255     104.520      66.499      84.570
               400      17.612     106.168      71.225      77.678
               500      19.432     108.024      75.358      70.345
               600      20.952     110.045      79.039      62.622
               800      23.320     114.486      85.410      46.158
              1000      24.982     119.326      90.803      28.522
              1500      27.250     132.466     101.428     -19.676
              2000      28.394     146.396     109.435     -72.474
              2400      29.124     157.903     114.678    -117.324
        =========== =========== =========== =========== ===========
    """,
)

