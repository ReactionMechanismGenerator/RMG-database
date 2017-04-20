#!/usr/bin/env python
# encoding: utf-8

name = ""
shortDesc = u"SOxNOx"
longDesc = u"""
"""

entry(
    index = 1,
    label = "HOSH",
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
        H298 = (-236.3,'kJ/mol'),
        S298 = (270.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
UMP2=full/6-31G+
A. Goumri, J-D.R. Rocha, D. Laakso, C.E. Smith, P. Marshall
The Journal of Chemical Physics 101, 9405 (1994); doi: http://dx.doi.org/10.1063/1.467971
As reported by: M.U. Alzueta, R. Bilbao, P. Glarborg, Comb. Flame, 2001, 127(4) 2234-2251, doi: 10.1016/S0010-2180(01)00325-X 
""",
)

entry(
    index = 2,
    label = "SO",
    molecule = 
"""
multiplicity 3
1 S u2 p1 c0 {2,D}
2 O u0 p2 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.22,7.55,7.84,8.08,8.43,8.62,8.95],'cal/(mol*K)'),
        H298 = (1.2,'kcal/mol'),
        S298 = (53.01,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
R.J. Kee, F.M. Rupley, J.A. Miller, The Chemkin Thermodynamic Data Base, Sandia Report SAND87-8215, Sandia National Laboratories, Livermore, California, 1991
As reported by: P. Glarborg, D. Kubel, K Dam-Johansen, H-M. Chiang, J.W. Bozzelli, Int. J. Chem. Kin., 1996, 28(10), 773-790, doi: 10.1002/(SICI)1097-4601(1996)28:10<773::AID-KIN8>3.0.CO;2-K
""",
)

entry(
    index = 3,
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
        H298 = (-71.0,'kcal/mol'),
        S298 = (59.29,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
R.J. Kee, F.M. Rupley, J.A. Miller, The Chemkin Thermodynamic Data Base, Sandia Report SAND87-8215, Sandia National Laboratories, Livermore, California, 1991
As reported by: P. Glarborg, D. Kubel, K Dam-Johansen, H-M. Chiang, J.W. Bozzelli, Int. J. Chem. Kin., 1996, 28(10), 773-790, doi: 10.1002/(SICI)1097-4601(1996)28:10<773::AID-KIN8>3.0.CO;2-K
""",
)

entry(
    index = 4,
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
    index = 5,
    label = "HSO",
    molecule = 
"""
multiplicity 2
1 S u1 p1 c0 {2,S} {3,D}
2 H u0 p0 c0 {1,S}
3 O u0 p2 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.02,9.93,10.73,11.36,12.22,12.73,13.34],'cal/(mol*K)'),
        H298 = (-5.4,'kcal/mol'),
        S298 = (57.80,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
H.M. Chiang, J.W. Bozzelli, Quantum Rice–Ramsberger–Kassel (QRRK) Analysis on Reaction of HSO + O, H + SO2, and OH + SO; HO2 and HOSO Formation and Dissociation
As reported by: P. Glarborg, D. Kubel, K Dam-Johansen, H-M. Chiang, J.W. Bozzelli, Int. J. Chem. Kin., 1996, 28(10), 773-790, doi: 10.1002/(SICI)1097-4601(1996)28:10<773::AID-KIN8>3.0.CO;2-K
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.71,9.42,10.00,10.45,11.08,11.53,12.33],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (57.15,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
H.M. Chiang, J.W. Bozzelli, Quantum Rice–Ramsberger–Kassel (QRRK) Analysis on Reaction of HSO + O, H + SO2, and OH + SO; HO2 and HOSO Formation and Dissociation
As reported by: P. Glarborg, D. Kubel, K Dam-Johansen, H-M. Chiang, J.W. Bozzelli, Int. J. Chem. Kin., 1996, 28(10), 773-790, doi: 10.1002/(SICI)1097-4601(1996)28:10<773::AID-KIN8>3.0.CO;2-K
""",
)

entry(
    index = 7,
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
        Cpdata = ([9.53,11.13,12.66,13.95,15.82,17.00,18.44],'cal/(mol*K)'),
        H298 = (-11.3,'kcal/mol'),
        S298 = (57.26,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
H.M. Chiang, J.W. Bozzelli, Quantum Rice–Ramsberger–Kassel (QRRK) Analysis on Reaction of HSO + O, H + SO2, and OH + SO; HO2 and HOSO Formation and Dissociation
As reported by: P. Glarborg, D. Kubel, K Dam-Johansen, H-M. Chiang, J.W. Bozzelli, Int. J. Chem. Kin., 1996, 28(10), 773-790, doi: 10.1002/(SICI)1097-4601(1996)28:10<773::AID-KIN8>3.0.CO;2-K
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
        Cpdata = ([11.87,13.43,14.56,15.36,16.40,17.06,18.09],'cal/(mol*K)'),
        H298 = (-57.7,'kcal/mol'),
        S298 = (64.62,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
H.M. Chiang, J.W. Bozzelli, Quantum Rice–Ramsberger–Kassel (QRRK) Analysis on Reaction of HSO + O, H + SO2, and OH + SO; HO2 and HOSO Formation and Dissociation
As reported by: P. Glarborg, D. Kubel, K Dam-Johansen, H-M. Chiang, J.W. Bozzelli, Int. J. Chem. Kin., 1996, 28(10), 773-790, doi: 10.1002/(SICI)1097-4601(1996)28:10<773::AID-KIN8>3.0.CO;2-K
""",
)

entry(
    index = 9,
    label = "HSO2",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 S u1 p0 c0 {1,D} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {2,S}
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
H.M. Chiang, J.W. Bozzelli, Quantum Rice–Ramsberger–Kassel (QRRK) Analysis on Reaction of HSO + O, H + SO2, and OH + SO; HO2 and HOSO Formation and Dissociation
As reported by: P. Glarborg, D. Kubel, K Dam-Johansen, H-M. Chiang, J.W. Bozzelli, Int. J. Chem. Kin., 1996, 28(10), 773-790, doi: 10.1002/(SICI)1097-4601(1996)28:10<773::AID-KIN8>3.0.CO;2-K
""",
)

entry(
    index = 10,
    label = "HOSHO",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {4,S}
2 S u0 p1 c0 {1,S} {3,D} {5,S}
3 O u0 p2 c0 {2,D}
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
H.M. Chiang, J.W. Bozzelli, Quantum Rice–Ramsberger–Kassel (QRRK) Analysis on Reaction of HSO + O, H + SO2, and OH + SO; HO2 and HOSO Formation and Dissociation
As reported by: P. Glarborg, D. Kubel, K Dam-Johansen, H-M. Chiang, J.W. Bozzelli, Int. J. Chem. Kin., 1996, 28(10), 773-790, doi: 10.1002/(SICI)1097-4601(1996)28:10<773::AID-KIN8>3.0.CO;2-K
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([16.74,18.76,20.13,21.07,22.22,22.94,24.02],'cal/(mol*K)'),
        H298 = (-93.5,'kcal/mol'),
        S298 = (70.72,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
H.M. Chiang, J.W. Bozzelli, Quantum Rice–Ramsberger–Kassel (QRRK) Analysis on Reaction of HSO + O, H + SO2, and OH + SO; HO2 and HOSO Formation and Dissociation
As reported by: P. Glarborg, D. Kubel, K Dam-Johansen, H-M. Chiang, J.W. Bozzelli, Int. J. Chem. Kin., 1996, 28(10), 773-790, doi: 10.1002/(SICI)1097-4601(1996)28:10<773::AID-KIN8>3.0.CO;2-K
""",
)

entry(
    index = 12,
    label = "HSOO",
    molecule = 
"""
multiplicity 2
1 S u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u1 p2 c0 {2,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,700,1000,1300,2500],'K'),
        Cpdata = ([51.7,56.8,60.5,65.6,70.2,72.9,76.0],'J/(mol*K)'),
        H298 = (111.5,'kJ/mol'),
        S298 = (283.0,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Table 5
MP2=FULL/6-31G(d)
A. Goumri, J-D.R. Rocha, D. Laakso, C.E. Smith, P. Marshall
J. Phys. Chem. A, 1999, 103, 11328-11335, doi: 10.1021/jp9924070
""",
)

entry(
    index = 13,
    label = "NS",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {2,D}
2 S u0 p2 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.07,8.17,8.26,8.35,8.50,8.62,8.84],'cal/(mol*K)'),
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
    index = 14,
    label = "NH(S)",
    molecule = 
"""
1 N u0 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.98,7.00,7.11,7.27,7.60,7.91,8.44],'cal/(mol*K)'),
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
    index = 15,
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
        Cpdata = ([10.44,11.42,12.25,13.10,14.32,15.15,16.68],'cal/(mol*K)'),
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
    index = 16,
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
        Cpdata = ([11.74,13.86,15.60,17.04,19.17,20.67,22.94],'cal/(mol*K)'),
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
    index = 17,
    label = "HCNN",
    molecule = 
"""
multiplicity 2
1 C u1 p1 c-1 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 N u0 p0 c+1 {1,S} {4,T}
4 N u0 p1 c0 {3,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.78,12.19,13.40,14.29,15.68,16.56,17.71],'cal/(mol*K)'),
        H298 = (109.0,'kcal/mol','+|-',0.5),
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
    index = 18,
    label = "HCN2",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,D} {3,S}
2 N u0 p1 c0 {1,D} {3,S}
3 C u1 p0 c0 {1,S} {2,S} {4,S}
4 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.00,12.02,13.00,13.81,15.30,16.09,17.59],'cal/(mol*K)'),
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
    index = 19,
    label = "CH2NNH2",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 N u0 p1 c0 {1,D} {3,S}
3 N u0 p1 c0 {2,S} {6,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
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
    index = 20,
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
        Cpdata = ([13.70,16.20,16.82,18.69,24.40,27.10,31.31],'cal/(mol*K)'),
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
    index = 21,
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
        Cpdata = ([12.50,14.24,15.80,17.16,19.17,20.46,22.39],'cal/(mol*K)'),
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



















"""
check Burcat?
check GlarborgNS?
Add:
HOSO2
N2H3NO
HNNO2 - bad
H2NONO
NH2NHNO
NH2NHNO2
NH2NHONO
CH2N2 - radical, but no data for non-rad
CHN2 - same
cN2CH2 - same
CNNH - same
CNN - same
CH2NC - same
CH2NCN
NCCHN
NCNCN
cNCN
OHNHCN - bad
HONCNH
NCOHNH
HN(O)CN - bad
HNC(O)N
HOOS
SNO
H298 for NCN from Lin2013b: http://pubs.acs.org/doi/abs/10.1021/jp402903t
I can derive thermo for S, SNO, NSO, SON, SNO excited, NOS excited, SON excited in Cantherm with assistance from Table II in http://aip.scitation.org/doi/abs/10.1063/1.1806419
"""

