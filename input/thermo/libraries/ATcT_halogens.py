#!/usr/bin/env python
# encoding: utf-8

name = "ATcT_halogens"
shortDesc = ""
longDesc = """

"""
entry(
    index = 0,
    label = "Hydrogen bromide",
    molecule = 
"""
1 Br u0 p3 c0 {2,S}
2 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49627,0.000333234,-2.46357e-06,5.30348e-09,-2.90077e-12,-5348.59,3.90886], Tmin=(10,'K'), Tmax=(730.648,'K')),
            NASAPolynomial(coeffs=[3.12191,0.000728821,1.19691e-07,-1.5163e-10,2.57981e-14,-5059.79,5.89955], Tmin=(730.648,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-26.3978,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: Br
H298 = -8.554015296000001 kcal/mol
""",
    rank = 5,
)

entry(
    index = 1,
    label = "trans-1,2-Dibromoethene",
    molecule = 
"""
1 Br u0 p3 c0 {3,S}
2 Br u0 p3 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,D} {5,S}
4 C  u0 p0 c0 {2,S} {3,D} {6,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92162,0.00500791,7.17347e-05,-1.68479e-07,1.15549e-10,10449.7,11.8074], Tmin=(10,'K'), Tmax=(505.415,'K')),
            NASAPolynomial(coeffs=[4.39816,0.0171561,-1.15666e-05,3.72048e-09,-4.55243e-13,9941.57,7.82204], Tmin=(505.415,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (119.779,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: BrC=CBr
H298 = 24.23518164 kcal/mol
""",
    rank = 5,
)

entry(
    index = 2,
    label = "F",
    molecule =
"""
multiplicity 2
1 F u1 p3 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.90371,-0.000635296,2.64735e-07,7.69063e-11,-5.45254e-14,7771.93,2.70828], Tmin=(298,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[2.65117,-0.00014013,5.19236e-08,-8.84954e-12,5.9028e-16,8758.29,4.07857], Tmin=(1400,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (72.8916,'kJ/mol'),
        Cp0 = (20.7862,'J/mol/K'),
        CpInf = (20.7862,'J/mol/K'),
    ),
    shortDesc = """71STUPRO, H298 from ATcT_1.122p""",
    longDesc = 
"""
71STUPRO
********************************
*** Hydrogen/Oxygen/Fluorine ***
********************************
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[F]
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 3,
    label = "Dibromine",
    molecule = 
"""
1 Br u0 p3 c0 {2,S}
2 Br u0 p3 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.4667,0.00246908,1.28374e-05,-5.33465e-08,5.1445e-11,2539.05,8.84154], Tmin=(10,'K'), Tmax=(415.716,'K')),
            NASAPolynomial(coeffs=[4.22894,0.00066701,-6.21319e-07,2.47432e-10,-3.51494e-14,2901.72,5.25831], Tmin=(415.716,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (49.5943,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: BrBr
H298 = 7.380497132 kcal/mol
""",
    rank = 5,
)

entry(
    index = 4,
    label = "1,2-Dibromoacetylene",
    molecule = 
"""
1 Br u0 p3 c0 {3,S}
2 Br u0 p3 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,T}
4 C  u0 p0 c0 {2,S} {3,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87803,0.00912595,5.8146e-05,-2.20542e-07,2.09235e-10,36930.2,7.78084], Tmin=(10,'K'), Tmax=(407.805,'K')),
            NASAPolynomial(coeffs=[6.19103,0.00631473,-4.62223e-06,1.58531e-09,-2.04469e-13,36451.5,-3.32972], Tmin=(407.805,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (332.701,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: BrC#CBr
H298 = 76.84034417 kcal/mol
""",
    rank = 5,
)

entry(
    index = 5,
    label = "Tetrabromomethane",
    molecule = 
"""
1 Br u0 p3 c0 {5,S}
2 Br u0 p3 c0 {5,S}
3 Br u0 p3 c0 {5,S}
4 Br u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.35251,0.0510211,-0.000114048,1.17212e-07,-4.53808e-11,9943.89,12.8928], Tmin=(10,'K'), Tmax=(711.164,'K')),
            NASAPolynomial(coeffs=[10.3147,0.00539189,-4.16086e-06,1.40851e-09,-1.74727e-13,9101.78,-17.1726], Tmin=(711.164,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (132.643,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: BrC(Br)(Br)Br
H298 = 24.66539197 kcal/mol
""",
    rank = 5,
)

entry(
    index = 6,
    label = "Bromoform",
    molecule = 
"""
1 Br u0 p3 c0 {4,S}
2 Br u0 p3 c0 {4,S}
3 Br u0 p3 c0 {4,S}
4 C  u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80226,0.0166818,4.23654e-05,-2.08783e-07,2.18867e-10,3942.57,12.7714], Tmin=(10,'K'), Tmax=(380.603,'K')),
            NASAPolynomial(coeffs=[5.9251,0.0120374,-8.95407e-06,3.06158e-09,-3.88931e-13,3663.39,2.89961], Tmin=(380.603,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (74.9802,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: BrC(Br)Br
H298 = 11.6873805 kcal/mol
""",
    rank = 5,
)

entry(
    index = 7,
    label = "Dibromomethane",
    molecule = 
"""
1 Br u0 p3 c0 {3,S}
2 Br u0 p3 c0 {3,S}
3 C  u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H  u0 p0 c0 {3,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96226,0.0023424,4.54658e-05,-9.61203e-08,6.14948e-11,-1032.11,10.7653], Tmin=(10,'K'), Tmax=(519.267,'K')),
            NASAPolynomial(coeffs=[3.62234,0.0129598,-8.31107e-06,2.58709e-09,-3.09986e-13,-1061.58,11.144], Tmin=(519.267,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (25.7822,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: BrCBr
H298 = 0.979923518 kcal/mol
""",
    rank = 5,
)

entry(
    index = 8,
    label = "1,2-Dibromoethane",
    molecule = 
"""
1 Br u0 p3 c0 {3,S}
2 Br u0 p3 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C  u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {4,S}
8 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88814,0.00758208,0.00010489,-2.66133e-07,1.98794e-10,-6631.83,11.5758], Tmin=(10,'K'), Tmax=(461.56,'K')),
            NASAPolynomial(coeffs=[4.389,0.0239314,-1.54817e-05,4.84762e-09,-5.82915e-13,-7095.05,7.15932], Tmin=(461.56,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-13.2659,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: BrCCBr
H298 = -9.225621415 kcal/mol
""",
    rank = 5,
)

entry(
    index = 9,
    label = "Bromo hypobromite",
    molecule = 
"""
1 Br u0 p3 c0 {3,S}
2 Br u0 p3 c0 {3,S}
3 O  u0 p2 c0 {1,S} {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93196,0.00474092,3.18149e-05,-1.06005e-07,8.91351e-11,10988.5,10.4786], Tmin=(10,'K'), Tmax=(457.576,'K')),
            NASAPolynomial(coeffs=[5.40778,0.00361953,-3.12509e-06,1.16296e-09,-1.5586e-13,10573.8,3.16487], Tmin=(457.576,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (118.956,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: BrOBr
H298 = 24.80879541 kcal/mol
""",
    rank = 5,
)

entry(
    index = 10,
    label = "Bromoacetylene",
    molecule = 
"""
1 Br u0 p3 c0 {3,S}
2 C  u0 p0 c0 {3,T} {4,S}
3 C  u0 p0 c0 {1,S} {2,T}
4 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.45405,0.00278681,3.45866e-05,-7.96287e-08,5.18898e-11,31773.4,8.14143], Tmin=(10,'K'), Tmax=(551.933,'K')),
            NASAPolynomial(coeffs=[4.30574,0.00691611,-4.63282e-06,1.56068e-09,-2.02811e-13,31144.1,3.11724], Tmin=(551.933,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (279.865,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (78.9875,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: C#CBr
H298 = 65.77437859 kcal/mol
""",
    rank = 5,
)

entry(
    index = 11,
    label = "Chloroacetylene",
    molecule = 
"""
1 Cl u0 p3 c0 {3,S}
2 C  u0 p0 c0 {3,T} {4,S}
3 C  u0 p0 c0 {1,S} {2,T}
4 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.45246,0.00292688,3.51795e-05,-8.33148e-08,5.56911e-11,26212.5,6.99438], Tmin=(10,'K'), Tmax=(539.818,'K')),
            NASAPolynomial(coeffs=[4.34987,0.00673012,-4.4345e-06,1.47923e-09,-1.91311e-13,25355.7,1.80748], Tmin=(539.818,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (224.033,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (78.9875,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: C#CCl
H298 = 54.73470363 kcal/mol
""",
    rank = 5,
)

entry(
    index = 12,
    label = "Fluoroacetylene",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 C u0 p0 c0 {3,T} {4,S}
3 C u0 p0 c0 {1,S} {2,T}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.4498,0.0030263,3.99146e-05,-8.9615e-08,5.74336e-11,11343.1,5.90915], Tmin=(10,'K'), Tmax=(555.749,'K')),
            NASAPolynomial(coeffs=[4.23833,0.0086714,-5.87678e-06,1.96876e-09,-2.53031e-13,11206.2,0.995297], Tmin=(555.749,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (106.353,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (87.302,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: C#CF
H298 = 25.25334608 kcal/mol
""",
    rank = 5,
)

entry(
    index = 13,
    label = "1,1-Dibromoethene",
    molecule = 
"""
1 Br u0 p3 c0 {4,S}
2 Br u0 p3 c0 {4,S}
3 C  u0 p0 c0 {4,D} {5,S} {6,S}
4 C  u0 p0 c0 {1,S} {2,S} {3,D}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90854,0.00597005,7.54938e-05,-1.88443e-07,1.35229e-10,10816.7,11.426], Tmin=(10,'K'), Tmax=(491.774,'K')),
            NASAPolynomial(coeffs=[4.88513,0.0161465,-1.0815e-05,3.48439e-09,-4.28773e-13,10370.2,5.17995], Tmin=(491.774,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (124.003,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: C=C(Br)Br
H298 = 25.04780115 kcal/mol
""",
    rank = 5,
)

entry(
    index = 14,
    label = "1,1-Dichloroethene",
    molecule = 
"""
1 Cl u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {4,S}
3 C  u0 p0 c0 {4,D} {5,S} {6,S}
4 C  u0 p0 c0 {1,S} {2,S} {3,D}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93466,0.00386022,6.46244e-05,-1.33198e-07,8.06415e-11,-1335.69,9.18792], Tmin=(10,'K'), Tmax=(566.676,'K')),
            NASAPolynomial(coeffs=[4.06002,0.0179634,-1.23804e-05,4.0686e-09,-5.07239e-13,-1718.39,6.53096], Tmin=(566.676,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (7.90688,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: C=C(Cl)Cl
H298 = 0.7026768640000001 kcal/mol
""",
    rank = 5,
)

entry(
    index = 15,
    label = "1,1-Difluoroethene",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 C u0 p0 c0 {4,D} {5,S} {6,S}
4 C u0 p0 c0 {1,S} {2,S} {3,D}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.10281,-0.0101072,0.000121983,-2.28108e-07,1.37933e-10,-43637.3,7.77929], Tmin=(10,'K'), Tmax=(534.293,'K')),
            NASAPolynomial(coeffs=[2.52167,0.0198841,-1.31824e-05,4.13929e-09,-4.93215e-13,-43580.8,11.9914], Tmin=(534.293,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-342.289,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: C=C(F)F
H298 = -83.80497132 kcal/mol
""",
    rank = 5,
)

entry(
    index = 16,
    label = "Vinyl bromide",
    molecule = 
"""
1 Br u0 p3 c0 {3,S}
2 C  u0 p0 c0 {3,D} {4,S} {5,S}
3 C  u0 p0 c0 {1,S} {2,D} {6,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05982,-0.00612034,9.18701e-05,-1.7485e-07,1.09328e-10,7416.14,9.04847], Tmin=(10,'K'), Tmax=(498.103,'K')),
            NASAPolynomial(coeffs=[2.30606,0.018,-1.09915e-05,3.27477e-09,-3.77446e-13,7399.63,15.0372], Tmin=(498.103,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (88.133,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: C=CBr
H298 = 17.629063100000003 kcal/mol
""",
    rank = 5,
)

entry(
    index = 17,
    label = "Vinyl chloride",
    molecule = 
"""
1 Cl u0 p3 c0 {3,S}
2 C  u0 p0 c0 {3,D} {4,S} {5,S}
3 C  u0 p0 c0 {1,S} {2,D} {6,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.07717,-0.00712033,8.8157e-05,-1.54161e-07,8.84765e-11,1193.36,7.86424], Tmin=(10,'K'), Tmax=(542.854,'K')),
            NASAPolynomial(coeffs=[2.0337,0.0183873,-1.12017e-05,3.32144e-09,-3.80635e-13,1294.71,15.0561], Tmin=(542.854,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (29.5694,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: C=CCl
H298 = 5.181644359 kcal/mol
""",
    rank = 5,
)

entry(
    index = 18,
    label = "Vinyl fluoride",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u0 p0 c0 {1,S} {2,D} {6,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.09164,-0.0073724,7.45741e-05,-1.12982e-07,5.61696e-11,-18476.6,6.78145], Tmin=(10,'K'), Tmax=(619.705,'K')),
            NASAPolynomial(coeffs=[1.44203,0.0189088,-1.12569e-05,3.25441e-09,-3.64262e-13,-18255.1,16.8744], Tmin=(619.705,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-133.886,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: C=CF
H298 = -34.02724665 kcal/mol
""",
    rank = 5,
)

entry(
    index = 19,
    label = "Bromomethane",
    molecule = 
"""
1 Br u0 p3 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.04874,-0.00393866,3.59732e-05,-3.73373e-08,5.41592e-12,-5638.97,6.3985], Tmin=(10,'K'), Tmax=(415.147,'K')),
            NASAPolynomial(coeffs=[1.74292,0.0131256,-7.06575e-06,1.88031e-09,-1.97095e-13,-5287.92,16.0304], Tmin=(415.147,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-19.9462,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: CBr
H298 = -8.666347992 kcal/mol
""",
    rank = 5,
)

entry(
    index = 20,
    label = "Acetyl chloride",
    molecule = 
"""
1 Cl u0 p3 c0 {4,S}
2 O  u0 p2 c0 {4,D}
3 C  u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4 C  u0 p0 c0 {1,S} {2,D} {3,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96579,0.00359411,0.000137138,-6.18662e-07,9.77253e-10,-30755.8,9.3122], Tmin=(10,'K'), Tmax=(159.009,'K')),
            NASAPolynomial(coeffs=[3.34074,0.0193171,-1.11783e-05,3.15059e-09,-3.46486e-13,-30817.3,11.1784], Tmin=(159.009,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-231.917,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (153.818,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: CC(=O)Cl
H298 = -57.74139579 kcal/mol
""",
    rank = 5,
)

entry(
    index = 21,
    label = "1,1-Dibromoethane",
    molecule = 
"""
1 Br u0 p3 c0 {4,S}
2 Br u0 p3 c0 {4,S}
3 C  u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4 C  u0 p0 c0 {1,S} {2,S} {3,S} {8,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {3,S}
8 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89063,0.00861207,0.000103108,-3.02235e-07,2.67669e-10,-5878.1,12.2711], Tmin=(10,'K'), Tmax=(375.451,'K')),
            NASAPolynomial(coeffs=[3.62373,0.0249424,-1.60162e-05,4.96252e-09,-5.90024e-13,-6261.41,12.0314], Tmin=(375.451,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-7.90111,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: CC(Br)Br
H298 = -7.743785851 kcal/mol
""",
    rank = 5,
)

entry(
    index = 22,
    label = "1,1,1-Trichloroethane",
    molecule = 
"""
1 Cl u0 p3 c0 {5,S}
2 Cl u0 p3 c0 {5,S}
3 Cl u0 p3 c0 {5,S}
4 C  u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
6 H  u0 p0 c0 {4,S}
7 H  u0 p0 c0 {4,S}
8 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83119,0.0117235,0.000122583,-3.44451e-07,2.72791e-10,-19621.3,10.3112], Tmin=(10,'K'), Tmax=(451.905,'K')),
            NASAPolynomial(coeffs=[5.75468,0.0241914,-1.66989e-05,5.44403e-09,-6.7139e-13,-20369.8,-0.772752], Tmin=(451.905,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-136.725,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: CC(Cl)(Cl)Cl
H298 = -34.63432122 kcal/mol
""",
    rank = 5,
)

entry(
    index = 23,
    label = "1,1-Dichloroethane",
    molecule = 
"""
1 Cl u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {4,S}
3 C  u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4 C  u0 p0 c0 {1,S} {2,S} {3,S} {8,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {3,S}
8 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92514,0.00482565,9.20261e-05,-2.04473e-07,1.38186e-10,-17862.2,10.2704], Tmin=(10,'K'), Tmax=(489.482,'K')),
            NASAPolynomial(coeffs=[3.2678,0.0251286,-1.59476e-05,4.9045e-09,-5.81296e-13,-18074.7,11.1449], Tmin=(489.482,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-121.059,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: CC(Cl)Cl
H298 = -31.80449331 kcal/mol
""",
    rank = 5,
)

entry(
    index = 24,
    label = "1,1-Difluoroethane",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4 C u0 p0 c0 {1,S} {2,S} {3,S} {8,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97687,0.00152092,7.98382e-05,-1.56075e-07,9.99812e-11,-62159.4,8.51335], Tmin=(10,'K'), Tmax=(400.397,'K')),
            NASAPolynomial(coeffs=[1.38252,0.0274158,-1.70856e-05,5.16176e-09,-6.0281e-13,-61920.3,18.6573], Tmin=(400.397,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-488.663,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: CC(F)F
H298 = -120.15296370000002 kcal/mol
""",
    rank = 5,
)

entry(
    index = 25,
    label = "Ethyl bromide",
    molecule = 
"""
1 Br u0 p3 c0 {3,S}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C  u0 p0 c0 {1,S} {2,S} {7,S} {8,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {3,S}
8 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97523,0.00153972,6.79116e-05,-1.24249e-07,7.45156e-11,-9258.95,9.3778], Tmin=(10,'K'), Tmax=(428.211,'K')),
            NASAPolynomial(coeffs=[1.45409,0.0250906,-1.45874e-05,4.19288e-09,-4.7342e-13,-9029.21,19.4025], Tmin=(428.211,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-41.3056,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: CCBr
H298 = -15.13623327 kcal/mol
""",
    rank = 5,
)

entry(
    index = 26,
    label = "Chloroethane",
    molecule = 
"""
1 Cl u0 p3 c0 {3,S}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C  u0 p0 c0 {1,S} {2,S} {7,S} {8,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {3,S}
8 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97391,0.00149727,6.00407e-05,-9.89218e-08,5.27772e-11,-15019.3,8.16871], Tmin=(10,'K'), Tmax=(484.301,'K')),
            NASAPolynomial(coeffs=[1.03942,0.0257249,-1.49693e-05,4.294e-09,-4.83116e-13,-14611.4,20.1994], Tmin=(484.301,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-95.8699,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: CCCl
H298 = -26.64674952 kcal/mol
""",
    rank = 5,
)

entry(
    index = 27,
    label = "Fluoroethane",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {1,S} {2,S} {7,S} {8,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.01083,-0.00102926,6.16557e-05,-9.19329e-08,4.49175e-11,-34255.7,7.2642], Tmin=(10,'K'), Tmax=(528.36,'K')),
            NASAPolynomial(coeffs=[0.478247,0.0257143,-1.4268e-05,3.8642e-09,-4.09773e-13,-33817.5,22.0532], Tmin=(528.36,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-256.677,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: CCF
H298 = -65.02629063 kcal/mol
""",
    rank = 5,
)

entry(
    index = 28,
    label = "Chloromethane",
    molecule = 
"""
1 Cl u0 p3 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.06993,-0.00479947,3.79157e-05,-4.59844e-08,1.84177e-11,-11181.9,5.10056], Tmin=(10,'K'), Tmax=(740.83,'K')),
            NASAPolynomial(coeffs=[1.42627,0.0134735,-7.17954e-06,1.88274e-09,-1.94328e-13,-10784.2,16.321], Tmin=(740.83,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-73.684,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: CCl
H298 = -19.73231358 kcal/mol
""",
    rank = 5,
)

entry(
    index = 29,
    label = "Fluoromethane",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05191,-0.00340134,1.7341e-05,2.49456e-09,-1.5179e-11,-29530.1,3.91759], Tmin=(10,'K'), Tmax=(534.708,'K')),
            NASAPolynomial(coeffs=[0.487074,0.0143029,-7.17972e-06,1.7168e-09,-1.57925e-13,-29095.7,20.0824], Tmin=(534.708,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-228.098,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: CF
H298 = -56.2834608 kcal/mol
""",
    rank = 5,
)

entry(
    index = 30,
    label = "Methyl hypochlorite",
    molecule = 
"""
1 Cl u0 p3 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 C  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 H  u0 p0 c0 {3,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98144,0.0013949,6.02531e-05,-1.45263e-07,1.17802e-10,-9138.06,8.00191], Tmin=(10,'K'), Tmax=(313.045,'K')),
            NASAPolynomial(coeffs=[2.84717,0.0158878,-9.18922e-06,2.61769e-09,-2.92785e-13,-9098.74,12.1568], Tmin=(313.045,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-53.5484,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (128.874,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: COCl
H298 = -15.08126195 kcal/mol
""",
    rank = 5,
)

entry(
    index = 31,
    label = "Hydrogen chloride",
    molecule = 
"""
1 Cl u0 p3 c0 {2,S}
2 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49635,0.000276377,-1.82806e-06,3.52201e-09,-1.71444e-12,-12130,2.49152], Tmin=(10,'K'), Tmax=(811.161,'K')),
            NASAPolynomial(coeffs=[3.22712,0.000339652,3.92943e-07,-2.249e-10,3.25754e-14,-11837.6,3.99044], Tmin=(811.161,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-90.2944,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: Cl
H298 = -22.02987572 kcal/mol
""",
    rank = 5,
)

entry(
    index = 32,
    label = "Bromochlorane",
    molecule = 
"""
1 Br u0 p3 c0 {2,S}
2 Cl u0 p3 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.47949,0.00131363,1.04268e-05,-2.99366e-08,2.21693e-11,597.538,8.4027], Tmin=(10,'K'), Tmax=(516.485,'K')),
            NASAPolynomial(coeffs=[4.04623,0.00108345,-9.83504e-07,3.82583e-10,-5.32184e-14,764.298,5.50595], Tmin=(516.485,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (24.2142,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: ClBr
H298 = 3.450047801 kcal/mol
""",
    rank = 5,
)

entry(
    index = 33,
    label = "Dichloroacetylene",
    molecule = 
"""
1 Cl u0 p3 c0 {3,S}
2 Cl u0 p3 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,T}
4 C  u0 p0 c0 {2,S} {3,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89059,0.00810976,5.5448e-05,-2.01138e-07,1.86335e-10,26369.5,4.8004], Tmin=(10,'K'), Tmax=(413.134,'K')),
            NASAPolynomial(coeffs=[5.89501,0.00670832,-4.83817e-06,1.63828e-09,-2.09144e-13,25534.4,-4.95759], Tmin=(413.134,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (226.324,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: ClC#CCl
H298 = 55.7791587 kcal/mol
""",
    rank = 5,
)

entry(
    index = 34,
    label = "Tribromochloromethane",
    molecule = 
"""
1 Br u0 p3 c0 {5,S}
2 Br u0 p3 c0 {5,S}
3 Br u0 p3 c0 {5,S}
4 Cl u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.35936,0.0444148,-8.3903e-05,7.15978e-08,-2.27614e-11,4179.28,13.8244], Tmin=(10,'K'), Tmax=(904.481,'K')),
            NASAPolynomial(coeffs=[9.9145,0.00596021,-4.43286e-06,1.45311e-09,-1.75408e-13,3218.1,-15.0021], Tmin=(904.481,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (75.791,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: ClC(Br)(Br)Br
H298 = 13.00191205 kcal/mol
""",
    rank = 5,
)

entry(
    index = 35,
    label = "Chlorodibromomethane",
    molecule = 
"""
1 Br u0 p3 c0 {4,S}
2 Br u0 p3 c0 {4,S}
3 Cl u0 p3 c0 {4,S}
4 C  u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85166,0.0114037,6.26742e-05,-2.24197e-07,2.05418e-10,-1909.65,13.02], Tmin=(10,'K'), Tmax=(410.406,'K')),
            NASAPolynomial(coeffs=[5.65285,0.0124645,-9.24357e-06,3.15281e-09,-3.99542e-13,-2217.18,4.0244], Tmin=(410.406,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (18.5366,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: ClC(Br)Br
H298 = -0.095602294 kcal/mol
""",
    rank = 5,
)

entry(
    index = 36,
    label = "Bromotrichloromethane",
    molecule = 
"""
1 Br u0 p3 c0 {5,S}
2 Cl u0 p3 c0 {5,S}
3 Cl u0 p3 c0 {5,S}
4 Cl u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75766,0.0181211,9.50665e-05,-3.7488e-07,3.54286e-10,-7208.18,11.7761], Tmin=(10,'K'), Tmax=(415.384,'K')),
            NASAPolynomial(coeffs=[8.33271,0.0105033,-9.00799e-06,3.3366e-09,-4.45685e-13,-8635.6,-10.0604], Tmin=(415.384,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-38.8145,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: ClC(Cl)(Cl)Br
H298 = -9.971319312 kcal/mol
""",
    rank = 5,
)

entry(
    index = 37,
    label = "Hexachloroethane",
    molecule = 
"""
1 Cl u0 p3 c0 {7,S}
2 Cl u0 p3 c0 {7,S}
3 Cl u0 p3 c0 {7,S}
4 Cl u0 p3 c0 {8,S}
5 Cl u0 p3 c0 {8,S}
6 Cl u0 p3 c0 {8,S}
7 C  u0 p0 c0 {1,S} {2,S} {3,S} {8,S}
8 C  u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.47895,0.0415869,0.000171516,-7.87604e-07,8.22584e-10,-21198.8,12.5716], Tmin=(10,'K'), Tmax=(380.999,'K')),
            NASAPolynomial(coeffs=[11.5866,0.0232918,-1.95472e-05,7.06843e-09,-9.26957e-13,-23928.8,-25.0847], Tmin=(380.999,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-159.947,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: ClC(Cl)(Cl)C(Cl)(Cl)Cl
H298 = -35.70745698 kcal/mol
""",
    rank = 5,
)

entry(
    index = 38,
    label = "Tetrachloromethane",
    molecule = 
"""
1 Cl u0 p3 c0 {5,S}
2 Cl u0 p3 c0 {5,S}
3 Cl u0 p3 c0 {5,S}
4 Cl u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79581,0.0143838,9.4746e-05,-3.21927e-07,2.75344e-10,-13595.9,9.50938], Tmin=(10,'K'), Tmax=(450.236,'K')),
            NASAPolynomial(coeffs=[8.10227,0.0108611,-9.24588e-06,3.41341e-09,-4.55427e-13,-14738.7,-11.7402], Tmin=(450.236,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-96.8169,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: ClC(Cl)(Cl)Cl
H298 = -22.84416826 kcal/mol
""",
    rank = 5,
)

entry(
    index = 39,
    label = "Tetrachloroethene",
    molecule = 
"""
1 Cl u0 p3 c0 {5,S}
2 Cl u0 p3 c0 {5,S}
3 Cl u0 p3 c0 {6,S}
4 Cl u0 p3 c0 {6,S}
5 C  u0 p0 c0 {1,S} {2,S} {6,D}
6 C  u0 p0 c0 {3,S} {4,S} {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7113,0.0226586,9.84757e-05,-4.10148e-07,4.04113e-10,-5152.36,11.576], Tmin=(10,'K'), Tmax=(396.376,'K')),
            NASAPolynomial(coeffs=[7.84504,0.0165771,-1.33592e-05,4.75008e-09,-6.1662e-13,-6065.45,-8.07274], Tmin=(396.376,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-24.8233,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: ClC(Cl)=C(Cl)Cl
H298 = -5.544933078 kcal/mol
""",
    rank = 5,
)

entry(
    index = 40,
    label = "Bromodichloromethane",
    molecule = 
"""
1 Br u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {4,S}
3 Cl u0 p3 c0 {4,S}
4 C  u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88839,0.00780002,6.92536e-05,-2.04939e-07,1.6572e-10,-7719.24,12.0868], Tmin=(10,'K'), Tmax=(452.18,'K')),
            NASAPolynomial(coeffs=[5.48765,0.0125475,-9.17365e-06,3.09864e-09,-3.90378e-13,-8184.15,3.50464], Tmin=(452.18,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-38.4612,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: ClC(Cl)Br
H298 = -11.78298279 kcal/mol
""",
    rank = 5,
)

entry(
    index = 41,
    label = "Pentachloroethane",
    molecule = 
"""
1 Cl u0 p3 c0 {6,S}
2 Cl u0 p3 c0 {6,S}
3 Cl u0 p3 c0 {7,S}
4 Cl u0 p3 c0 {7,S}
5 Cl u0 p3 c0 {7,S}
6 C  u0 p0 c0 {1,S} {2,S} {7,S} {8,S}
7 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
8 H  u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.58154,0.0347805,0.000122803,-5.7358e-07,6.11388e-10,-21758.2,13.8049], Tmin=(10,'K'), Tmax=(367.957,'K')),
            NASAPolynomial(coeffs=[8.31617,0.0266835,-2.09986e-05,7.30603e-09,-9.33245e-13,-23079.4,-8.29313], Tmin=(367.957,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-157.175,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: ClC(Cl)C(Cl)(Cl)Cl
H298 = -37.57170172 kcal/mol
""",
    rank = 5,
)

entry(
    index = 42,
    label = "1,1,2,2-Tetrachloroethane",
    molecule = 
"""
1 Cl u0 p3 c0 {5,S}
2 Cl u0 p3 c0 {5,S}
3 Cl u0 p3 c0 {6,S}
4 Cl u0 p3 c0 {6,S}
5 C  u0 p0 c0 {1,S} {2,S} {6,S} {7,S}
6 C  u0 p0 c0 {3,S} {4,S} {5,S} {8,S}
7 H  u0 p0 c0 {5,S}
8 H  u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63678,0.0407624,-4.67153e-05,2.90481e-08,-7.64752e-12,-21333.8,12.7584], Tmin=(10,'K'), Tmax=(849.089,'K')),
            NASAPolynomial(coeffs=[7.29474,0.02353,-1.62725e-05,5.1458e-09,-6.09881e-13,-22122.2,-4.29076], Tmin=(849.089,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-149.81,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: ClC(Cl)C(Cl)Cl
H298 = -37.35659656 kcal/mol
""",
    rank = 5,
)

entry(
    index = 43,
    label = "Chloroform",
    molecule = 
"""
1 Cl u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {4,S}
3 Cl u0 p3 c0 {4,S}
4 C  u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91005,0.00582391,6.47481e-05,-1.65754e-07,1.18837e-10,-14014.6,9.95099], Tmin=(10,'K'), Tmax=(501.859,'K')),
            NASAPolynomial(coeffs=[5.24941,0.0128889,-9.39195e-06,3.16968e-09,-3.99731e-13,-14241,2.18699], Tmin=(501.859,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-96.2688,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: ClC(Cl)Cl
H298 = -24.42399618 kcal/mol
""",
    rank = 5,
)

entry(
    index = 44,
    label = "Trichloroethene",
    molecule = 
"""
1 Cl u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {5,S}
3 Cl u0 p3 c0 {5,S}
4 C  u0 p0 c0 {1,S} {5,D} {6,S}
5 C  u0 p0 c0 {2,S} {3,S} {4,D}
6 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84749,0.0108789,9.18615e-05,-2.79009e-07,2.31131e-10,-3766.49,11.8132], Tmin=(10,'K'), Tmax=(440.81,'K')),
            NASAPolynomial(coeffs=[5.82532,0.0172619,-1.26505e-05,4.2635e-09,-5.3538e-13,-4223.37,1.21019], Tmin=(440.81,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-11.5272,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: ClC=C(Cl)Cl
H298 = -3.513384321 kcal/mol
""",
    rank = 5,
)

entry(
    index = 45,
    label = "1,2-Dichloroethene",
    molecule = 
"""
1 Cl u0 p3 c0 {3,S}
2 Cl u0 p3 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,D} {5,S}
4 C  u0 p0 c0 {2,S} {3,D} {6,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94337,0.00335425,6.25373e-05,-1.2619e-07,7.58027e-11,-1886.26,9.53327], Tmin=(10,'K'), Tmax=(560.755,'K')),
            NASAPolynomial(coeffs=[3.60306,0.01863,-1.26933e-05,4.10928e-09,-5.04849e-13,-1872.47,9.17704], Tmin=(560.755,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (5.65926,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: ClC=CCl
H298 = -0.444550669 kcal/mol
""",
    rank = 5,
)

entry(
    index = 46,
    label = "Bromochloromethane",
    molecule = 
"""
1 Br u0 p3 c0 {3,S}
2 Cl u0 p3 c0 {3,S}
3 C  u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H  u0 p0 c0 {3,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97166,0.00167217,4.09963e-05,-7.78031e-08,4.52688e-11,-6586.87,10.2809], Tmin=(10,'K'), Tmax=(554.333,'K')),
            NASAPolynomial(coeffs=[3.15721,0.0138489,-9.00034e-06,2.82679e-09,-3.4071e-13,-6763.1,12.8565], Tmin=(554.333,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-29.7346,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: ClCBr
H298 = -10.13384321 kcal/mol
""",
    rank = 5,
)

entry(
    index = 47,
    label = "1,1,1,2-Tetrachloroethane",
    molecule = 
"""
1 Cl u0 p3 c0 {5,S}
2 Cl u0 p3 c0 {6,S}
3 Cl u0 p3 c0 {6,S}
4 Cl u0 p3 c0 {6,S}
5 C  u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
6 C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
7 H  u0 p0 c0 {5,S}
8 H  u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72284,0.0217258,0.00011988,-4.27921e-07,3.97154e-10,-20888.2,12.7556], Tmin=(10,'K'), Tmax=(399.542,'K')),
            NASAPolynomial(coeffs=[6.42852,0.026794,-1.98718e-05,6.70221e-09,-8.39908e-13,-21786.9,-1.02733], Tmin=(399.542,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-148.202,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: ClCC(Cl)(Cl)Cl
H298 = -36.5917782 kcal/mol
""",
    rank = 5,
)

entry(
    index = 48,
    label = "1,1,2-Trichloroethane",
    molecule = 
"""
1 Cl u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {5,S}
3 Cl u0 p3 c0 {5,S}
4 C  u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5 C  u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
6 H  u0 p0 c0 {4,S}
7 H  u0 p0 c0 {4,S}
8 H  u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80131,0.0159196,7.78841e-05,-2.3064e-07,1.85386e-10,-19995.5,12.6451], Tmin=(10,'K'), Tmax=(439.357,'K')),
            NASAPolynomial(coeffs=[4.54255,0.026642,-1.83698e-05,5.91876e-09,-7.1897e-13,-20190.1,7.75972], Tmin=(439.357,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-137.355,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: ClCC(Cl)Cl
H298 = -35.44455067 kcal/mol
""",
    rank = 5,
)

entry(
    index = 49,
    label = "1,2-Dichloroethane",
    molecule = 
"""
1 Cl u0 p3 c0 {3,S}
2 Cl u0 p3 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C  u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {4,S}
8 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91255,0.00698049,0.000107676,-3.1493e-07,2.86291e-10,-17637.3,9.42648], Tmin=(10,'K'), Tmax=(355.366,'K')),
            NASAPolynomial(coeffs=[3.28614,0.0251423,-1.58839e-05,4.85063e-09,-5.70474e-13,-17797.9,10.8134], Tmin=(355.366,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-119.507,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: ClCCCl
H298 = -31.19502868 kcal/mol
""",
    rank = 5,
)

entry(
    index = 50,
    label = "Dichloromethane",
    molecule = 
"""
1 Cl u0 p3 c0 {3,S}
2 Cl u0 p3 c0 {3,S}
3 C  u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H  u0 p0 c0 {3,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98196,0.00104838,3.79516e-05,-6.64824e-08,3.64924e-11,-12706.7,8.34609], Tmin=(10,'K'), Tmax=(550.53,'K')),
            NASAPolynomial(coeffs=[2.51796,0.01518,-1.00739e-05,3.20457e-09,-3.89005e-13,-12539.3,14.0542], Tmin=(550.53,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-86.2465,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: ClCCl
H298 = -22.36137667 kcal/mol
""",
    rank = 5,
)

entry(
    index = 51,
    label = "Dichlorine",
    molecule = 
"""
1 Cl u0 p3 c0 {2,S}
2 Cl u0 p3 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.48726,0.000735498,8.28887e-06,-1.86476e-08,1.14343e-11,-1113.59,6.49117], Tmin=(10,'K'), Tmax=(599.093,'K')),
            NASAPolynomial(coeffs=[3.81066,0.00159007,-1.39685e-06,5.27833e-10,-7.16245e-14,-922.533,4.64523], Tmin=(599.093,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (2.39357,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: ClCl
H298 = 0.0 kcal/mol
""",
    rank = 5,
)

entry(
    index = 52,
    label = "Chloro hypochlorite",
    molecule = 
"""
1 Cl u0 p3 c0 {3,S}
2 Cl u0 p3 c0 {3,S}
3 O  u0 p2 c0 {1,S} {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95615,0.00268221,2.66649e-05,-6.6664e-08,4.49033e-11,7954.71,8.19901], Tmin=(10,'K'), Tmax=(550.487,'K')),
            NASAPolynomial(coeffs=[5.02666,0.00436966,-3.72694e-06,1.37949e-09,-1.84483e-13,7663.98,2.37072], Tmin=(550.487,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (79.5641,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: ClOCl
H298 = 18.63527725 kcal/mol
""",
    rank = 5,
)

entry(
    index = 53,
    label = "Chlorooxy hypochlorite",
    molecule = 
"""
1 Cl u0 p3 c0 {3,S}
2 Cl u0 p3 c0 {4,S}
3 O  u0 p2 c0 {1,S} {4,S}
4 O  u0 p2 c0 {2,S} {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8869,0.00744392,6.06431e-05,-1.73787e-07,1.30791e-10,14051.5,10.3332], Tmin=(10,'K'), Tmax=(497.855,'K')),
            NASAPolynomial(coeffs=[6.23731,0.00947088,-8.46814e-06,3.12614e-09,-4.11601e-13,13910.5,-1.96964], Tmin=(497.855,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (137.687,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (78.9875,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: ClOOCl
H298 = 31.38623327 kcal/mol
""",
    rank = 5,
)

entry(
    index = 54,
    label = "Dichloromethyl",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {3,S}
2 Cl u0 p3 c0 {3,S}
3 C  u1 p0 c0 {1,S} {2,S} {4,S}
4 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95837,0.00247158,3.55196e-05,-7.65764e-08,4.74581e-11,9380.57,9.50715], Tmin=(10,'K'), Tmax=(566.995,'K')),
            NASAPolynomial(coeffs=[4.41086,0.00877734,-6.28956e-06,2.12659e-09,-2.70363e-13,8871.67,6.23456], Tmin=(566.995,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (90.0943,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: Cl[CH]Cl
H298 = 21.57026769 kcal/mol
""",
    rank = 5,
)

entry(
    index = 55,
    label = "Pentachloroethyl",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {6,S}
2 Cl u0 p3 c0 {6,S}
3 Cl u0 p3 c0 {6,S}
4 Cl u0 p3 c0 {7,S}
5 Cl u0 p3 c0 {7,S}
6 C  u0 p0 c0 {1,S} {2,S} {3,S} {7,S}
7 C  u1 p0 c0 {4,S} {5,S} {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.17282,0.0622122,-0.000111008,9.35242e-08,-3.0131e-11,119.985,17.0943], Tmin=(10,'K'), Tmax=(837.73,'K')),
            NASAPolynomial(coeffs=[12.555,0.011084,-8.12636e-06,2.63088e-09,-3.14373e-13,-2891.31,-25.1823], Tmin=(837.73,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (12.0497,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (153.818,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: Cl[C](Cl)C(Cl)(Cl)Cl
H298 = 5.999043977 kcal/mol
""",
    rank = 5,
)

entry(
    index = 56,
    label = "Trichloromethyl",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {4,S}
3 Cl u0 p3 c0 {4,S}
4 C  u1 p0 c0 {1,S} {2,S} {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88786,0.00760386,5.87506e-05,-1.79361e-07,1.4272e-10,6877.55,10.5664], Tmin=(10,'K'), Tmax=(474.922,'K')),
            NASAPolynomial(coeffs=[6.24618,0.00802903,-6.67e-06,2.42071e-09,-3.18995e-13,5965.91,-1.46395], Tmin=(474.922,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (68.3114,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: Cl[C](Cl)Cl
H298 = 17.10086042 kcal/mol
""",
    rank = 5,
)

entry(
    index = 57,
    label = "Dichloromethylene",
    molecule = 
"""
1 Cl u0 p3 c0 {3,S}
2 Cl u0 p3 c0 {3,S}
3 C  u0 p1 c0 {1,S} {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96424,0.00210486,2.42565e-05,-5.53641e-08,3.47438e-11,26349.6,8.03065], Tmin=(10,'K'), Tmax=(580.713,'K')),
            NASAPolynomial(coeffs=[4.74855,0.00489616,-4.118e-06,1.50748e-09,-1.99821e-13,25728.1,3.48355], Tmin=(580.713,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (226.213,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: Cl[C]Cl
H298 = 55.13623327 kcal/mol
""",
    rank = 5,
)

entry(
    index = 58,
    label = "Hydrogen fluoride",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49719,0.000149335,-7.43426e-07,1.0692e-09,-3.73263e-13,-33844.9,0.924583], Tmin=(10,'K'), Tmax=(1079.95,'K')),
            NASAPolynomial(coeffs=[3.54618,-0.000497644,8.01791e-07,-2.83828e-10,3.2354e-14,-33937.2,0.810149], Tmin=(1079.95,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-273.679,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: F
H298 = -65.18188337 kcal/mol
""",
    rank = 5,
)

entry(
    index = 59,
    label = "1,2-Difluoroacetylene",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {4,S}
3 C u0 p0 c0 {1,S} {4,T}
4 C u0 p0 c0 {2,S} {3,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.37365,0.00967198,6.42941e-05,-2.48371e-07,2.43362e-10,-942.316,6.86461], Tmin=(10,'K'), Tmax=(392.056,'K')),
            NASAPolynomial(coeffs=[5.56744,0.00756355,-5.20729e-06,1.71201e-09,-2.14827e-13,-1118.95,-3.65215], Tmin=(392.056,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (4.39627,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (87.302,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: FC#CF
H298 = 1.359942639 kcal/mol
""",
    rank = 5,
)

entry(
    index = 60,
    label = "Tribromofluoromethane",
    molecule = 
"""
1 Br u0 p3 c0 {5,S}
2 Br u0 p3 c0 {5,S}
3 Br u0 p3 c0 {5,S}
4 F  u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7183,0.0229288,7.41394e-05,-3.75034e-07,4.03523e-10,-17853.8,12.9488], Tmin=(10,'K'), Tmax=(377.061,'K')),
            NASAPolynomial(coeffs=[7.9274,0.0110966,-9.35127e-06,3.42209e-09,-4.53051e-13,-18254.9,-6.34611], Tmin=(377.061,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-104.897,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: FC(Br)(Br)Br
H298 = -31.04684512 kcal/mol
""",
    rank = 5,
)

entry(
    index = 61,
    label = "Fluorodibromomethane",
    molecule = 
"""
1 Br u0 p3 c0 {4,S}
2 Br u0 p3 c0 {4,S}
3 F  u0 p3 c0 {4,S}
4 C  u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89909,0.0073113,6.37296e-05,-1.90572e-07,1.58276e-10,-23312.2,12.3582], Tmin=(10,'K'), Tmax=(432.651,'K')),
            NASAPolynomial(coeffs=[4.8884,0.0133013,-9.51612e-06,3.15436e-09,-3.91451e-13,-22998.2,6.77703], Tmin=(432.651,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-155.117,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: FC(Br)Br
H298 = -42.85372849 kcal/mol
""",
    rank = 5,
)

entry(
    index = 62,
    label = "Dibromofluorochloromethane",
    molecule = 
"""
1 Br u0 p3 c0 {5,S}
2 Br u0 p3 c0 {5,S}
3 Cl u0 p3 c0 {5,S}
4 F  u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77138,0.0173875,8.69863e-05,-3.47419e-07,3.3287e-10,-24601.6,13.2645], Tmin=(10,'K'), Tmax=(408.002,'K')),
            NASAPolynomial(coeffs=[7.64904,0.0115147,-9.59526e-06,3.48499e-09,-4.58989e-13,-24602.5,-5.2453], Tmin=(408.002,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-165.063,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: FC(Cl)(Br)Br
H298 = -44.64627151 kcal/mol
""",
    rank = 5,
)

entry(
    index = 63,
    label = "Dichlorofluorobromomethane",
    molecule = 
"""
1 Br u0 p3 c0 {5,S}
2 Cl u0 p3 c0 {5,S}
3 Cl u0 p3 c0 {5,S}
4 F  u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81169,0.0134121,8.92065e-05,-3.01676e-07,2.59582e-10,-30706.4,12.3967], Tmin=(10,'K'), Tmax=(443.891,'K')),
            NASAPolynomial(coeffs=[7.40445,0.0118755,-9.81102e-06,3.54504e-09,-4.65466e-13,-30974.9,-5.44052], Tmin=(443.891,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-225.369,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: FC(Cl)(Cl)Br
H298 = -56.95506692 kcal/mol
""",
    rank = 5,
)

entry(
    index = 64,
    label = "Fluorotrichloromethane",
    molecule = 
"""
1 Cl u0 p3 c0 {5,S}
2 Cl u0 p3 c0 {5,S}
3 Cl u0 p3 c0 {5,S}
4 F  u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84275,0.0105289,8.57599e-05,-2.53277e-07,1.9694e-10,-36652.5,10.3387], Tmin=(10,'K'), Tmax=(483.16,'K')),
            NASAPolynomial(coeffs=[7.13826,0.0123339,-1.01492e-05,3.66215e-09,-4.8081e-13,-37418.1,-6.67656], Tmin=(483.16,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-286.258,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: FC(Cl)(Cl)Cl
H298 = -68.93642447 kcal/mol
""",
    rank = 5,
)

entry(
    index = 65,
    label = "Fluorochlorobromomethane",
    molecule = 
"""
1 Br u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {4,S}
3 F  u0 p3 c0 {4,S}
4 C  u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92384,0.00500026,6.11537e-05,-1.53829e-07,1.10736e-10,-29450.4,11.346], Tmin=(10,'K'), Tmax=(489.522,'K')),
            NASAPolynomial(coeffs=[4.6505,0.0135829,-9.63873e-06,3.17618e-09,-3.92713e-13,-29416.7,6.58233], Tmin=(489.522,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-215.972,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: FC(Cl)Br
H298 = -55.18642447 kcal/mol
""",
    rank = 5,
)

entry(
    index = 66,
    label = "Fluorodichloromethane",
    molecule = 
"""
1 Cl u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {4,S}
3 F  u0 p3 c0 {4,S}
4 C  u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93978,0.00365806,5.51865e-05,-1.20708e-07,7.66817e-11,-35737.8,10.2291], Tmin=(10,'K'), Tmax=(545.704,'K')),
            NASAPolynomial(coeffs=[4.28695,0.014279,-1.0197e-05,3.37927e-09,-4.19949e-13,-35904.9,6.96837], Tmin=(545.704,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-277.583,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: FC(Cl)Cl
H298 = -67.79636711 kcal/mol
""",
    rank = 5,
)

entry(
    index = 67,
    label = "Difluorodibromomethane",
    molecule = 
"""
1 Br u0 p3 c0 {5,S}
2 Br u0 p3 c0 {5,S}
3 F  u0 p3 c0 {5,S}
4 F  u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82735,0.0125013,8.23795e-05,-2.78055e-07,2.41426e-10,-47967.7,12.0662], Tmin=(10,'K'), Tmax=(435.614,'K')),
            NASAPolynomial(coeffs=[6.67065,0.012916,-1.03789e-05,3.67513e-09,-4.75262e-13,-48297.6,-2.17679], Tmin=(435.614,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-363.004,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: FC(F)(Br)Br
H298 = -91.37189293 kcal/mol
""",
    rank = 5,
)

entry(
    index = 68,
    label = "Difluorochlorobromomethane",
    molecule = 
"""
1 Br u0 p3 c0 {5,S}
2 Cl u0 p3 c0 {5,S}
3 F  u0 p3 c0 {5,S}
4 F  u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86096,0.00935621,8.05761e-05,-2.32662e-07,1.79948e-10,-54810.4,11.8129], Tmin=(10,'K'), Tmax=(479.341,'K')),
            NASAPolynomial(coeffs=[6.39889,0.0133447,-1.06601e-05,3.76125e-09,-4.85342e-13,-54980.2,-1.58078], Tmin=(479.341,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-425.915,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: FC(F)(Cl)Br
H298 = -105.1386233 kcal/mol
""",
    rank = 5,
)

entry(
    index = 69,
    label = "Dichlorodifluoromethane",
    molecule = 
"""
1 Cl u0 p3 c0 {5,S}
2 Cl u0 p3 c0 {5,S}
3 F  u0 p3 c0 {5,S}
4 F  u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88556,0.00721063,7.5069e-05,-1.90454e-07,1.32448e-10,-61199.4,10.0779], Tmin=(10,'K'), Tmax=(525.254,'K')),
            NASAPolynomial(coeffs=[6.075,0.0139731,-1.11701e-05,3.94846e-09,-5.10602e-13,-61730.8,-2.15264], Tmin=(525.254,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-489.439,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: FC(F)(Cl)Cl
H298 = -117.98518159999999 kcal/mol
""",
    rank = 5,
)

entry(
    index = 70,
    label = "Bromotrifluoromethane",
    molecule = 
"""
1 Br u0 p3 c0 {5,S}
2 F  u0 p3 c0 {5,S}
3 F  u0 p3 c0 {5,S}
4 F  u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90433,0.00597792,6.97616e-05,-1.68948e-07,1.14438e-10,-80067,10.0172], Tmin=(10,'K'), Tmax=(529.57,'K')),
            NASAPolynomial(coeffs=[5.33838,0.0149255,-1.16073e-05,4.01542e-09,-5.10481e-13,-80391.9,1.39166], Tmin=(529.57,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-638.225,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: FC(F)(F)Br
H298 = -155.6022945 kcal/mol
""",
    rank = 5,
)

entry(
    index = 71,
    label = "Hexafluoroethane",
    molecule = 
"""
1 F u0 p3 c0 {7,S}
2 F u0 p3 c0 {7,S}
3 F u0 p3 c0 {7,S}
4 F u0 p3 c0 {8,S}
5 F u0 p3 c0 {8,S}
6 F u0 p3 c0 {8,S}
7 C u0 p0 c0 {1,S} {2,S} {3,S} {8,S}
8 C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75983,0.0167661,0.000138559,-3.99529e-07,3.13901e-10,-163911,10.5821], Tmin=(10,'K'), Tmax=(462.306,'K')),
            NASAPolynomial(coeffs=[6.6683,0.029005,-2.25109e-05,7.74883e-09,-9.79342e-13,-164824,-5.52865], Tmin=(462.306,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-1336.53,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: FC(F)(F)C(F)(F)F
H298 = -320.8628107 kcal/mol
""",
    rank = 5,
)

entry(
    index = 72,
    label = "Chlorotrifluoromethane",
    molecule = 
"""
1 Cl u0 p3 c0 {5,S}
2 F  u0 p3 c0 {5,S}
3 F  u0 p3 c0 {5,S}
4 F  u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92199,0.00457507,6.3518e-05,-1.36744e-07,8.34884e-11,-87048.2,8.87918], Tmin=(10,'K'), Tmax=(579.018,'K')),
            NASAPolynomial(coeffs=[4.86932,0.0159823,-1.25388e-05,4.37059e-09,-5.59088e-13,-87387.8,2.22791], Tmin=(579.018,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-704.048,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: FC(F)(F)Cl
H298 = -169.60086040000002 kcal/mol
""",
    rank = 5,
)

entry(
    index = 73,
    label = "Tetrafluoromethane",
    molecule = 
"""
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 F u0 p3 c0 {5,S}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95115,0.00268145,5.30836e-05,-9.75807e-08,5.23699e-11,-113868,6.54777], Tmin=(10,'K'), Tmax=(629.919,'K')),
            NASAPolynomial(coeffs=[3.32674,0.0189076,-1.47521e-05,5.11268e-09,-6.50321e-13,-114015,7.34073], Tmin=(629.919,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-927.471,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: FC(F)(F)F
H298 = -223.10468450000002 kcal/mol
""",
    rank = 5,
)

entry(
    index = 74,
    label = "Tetrafluoroethylene",
    molecule = 
"""
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {6,S}
4 F u0 p3 c0 {6,S}
5 C u0 p0 c0 {1,S} {2,S} {6,D}
6 C u0 p0 c0 {3,S} {4,S} {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86796,0.00896674,9.20781e-05,-2.50451e-07,1.90637e-10,-83074.1,9.05323], Tmin=(10,'K'), Tmax=(470.327,'K')),
            NASAPolynomial(coeffs=[5.38595,0.0191802,-1.42425e-05,4.78608e-09,-5.97116e-13,-83205.3,0.155967], Tmin=(470.327,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-668.76,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: FC(F)=C(F)F
H298 = -161.19263859999998 kcal/mol
""",
    rank = 5,
)

entry(
    index = 75,
    label = "Difluorobromomethane",
    molecule = 
"""
1 Br u0 p3 c0 {4,S}
2 F  u0 p3 c0 {4,S}
3 F  u0 p3 c0 {4,S}
4 C  u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95451,0.00275528,5.08692e-05,-1.05772e-07,6.55172e-11,-52561.2,10.5127], Tmin=(10,'K'), Tmax=(541.714,'K')),
            NASAPolynomial(coeffs=[3.63702,0.0149937,-1.04157e-05,3.36503e-09,-4.09279e-13,-52590.1,10.5098], Tmin=(541.714,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-409.943,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: FC(F)Br
H298 = -101.3264818 kcal/mol
""",
    rank = 5,
)

entry(
    index = 76,
    label = "Chlorodifluoromethane",
    molecule = 
"""
1 Cl u0 p3 c0 {4,S}
2 F  u0 p3 c0 {4,S}
3 F  u0 p3 c0 {4,S}
4 C  u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96593,0.00193259,4.53655e-05,-8.32534e-08,4.59619e-11,-59523,9.29198], Tmin=(10,'K'), Tmax=(591.873,'K')),
            NASAPolynomial(coeffs=[3.00434,0.0164342,-1.16687e-05,3.83344e-09,-4.72139e-13,-59468,12.2425], Tmin=(591.873,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-475.325,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: FC(F)Cl
H298 = -115.25334609999999 kcal/mol
""",
    rank = 5,
)

entry(
    index = 77,
    label = "Fluoroform",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 F u0 p3 c0 {4,S}
4 C u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.06655,-0.00569699,7.11567e-05,-1.16193e-07,6.06504e-11,-85093,7.48265], Tmin=(10,'K'), Tmax=(615.111,'K')),
            NASAPolynomial(coeffs=[2.45498,0.0163704,-1.09138e-05,3.38161e-09,-3.95687e-13,-85171.3,12.6925], Tmin=(615.111,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-689.544,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: FC(F)F
H298 = -166.3432122 kcal/mol
""",
    rank = 5,
)

entry(
    index = 78,
    label = "Trifluoroethene",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 C u0 p0 c0 {1,S} {5,D} {6,S}
5 C u0 p0 c0 {2,S} {3,S} {4,D}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93201,0.00413887,7.03233e-05,-1.49827e-07,9.42397e-11,-61644.4,9.50863], Tmin=(10,'K'), Tmax=(540.182,'K')),
            NASAPolynomial(coeffs=[3.82032,0.0197002,-1.38027e-05,4.49179e-09,-5.49698e-13,-61712.1,7.9889], Tmin=(540.182,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-491.796,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: FC=C(F)F
H298 = -119.07265770000001 kcal/mol
""",
    rank = 5,
)

entry(
    index = 79,
    label = "Bromofluoromethane",
    molecule = 
"""
1 Br u0 p3 c0 {3,S}
2 F  u0 p3 c0 {3,S}
3 C  u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H  u0 p0 c0 {3,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.01248,-0.00124952,4.41315e-05,-7.34434e-08,3.93234e-11,-26888.9,9.37564], Tmin=(10,'K'), Tmax=(568.359,'K')),
            NASAPolynomial(coeffs=[2.46389,0.0141966,-8.63485e-06,2.52719e-09,-2.85246e-13,-26503.6,15.3256], Tmin=(568.359,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-195.066,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: FCBr
H298 = -50.64531549 kcal/mol
""",
    rank = 5,
)

entry(
    index = 80,
    label = "1,2-Difluoroethane",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {4,S}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92422,0.00937296,2.43709e-05,-3.4286e-08,1.28696e-11,-55598.1,8.62109], Tmin=(10,'K'), Tmax=(910.507,'K')),
            NASAPolynomial(coeffs=[2.74666,0.0232304,-1.27649e-05,3.37977e-09,-3.48575e-13,-55707.5,12.215], Tmin=(910.507,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-434.144,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: FCCF
H298 = -107.02915870000001 kcal/mol
""",
    rank = 5,
)

entry(
    index = 81,
    label = "Chlorofluoromethane",
    molecule = 
"""
1 Cl u0 p3 c0 {3,S}
2 F  u0 p3 c0 {3,S}
3 C  u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H  u0 p0 c0 {3,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.03933,-0.00316189,4.7235e-05,-7.136e-08,3.4853e-11,-33023.4,8.19834], Tmin=(10,'K'), Tmax=(629.218,'K')),
            NASAPolynomial(coeffs=[2.14796,0.0146098,-8.83376e-06,2.56409e-09,-2.86848e-13,-32859.2,15.5427], Tmin=(629.218,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-255.75,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: FCCl
H298 = -62.93021033 kcal/mol
""",
    rank = 5,
)

entry(
    index = 82,
    label = "Difluoromethane",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {3,S}
3 C u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.06909,-0.00454455,4.03365e-05,-4.87809e-08,1.9023e-11,-55486.1,6.40435], Tmin=(10,'K'), Tmax=(788.976,'K')),
            NASAPolynomial(coeffs=[1.30655,0.0154345,-9.00408e-06,2.50681e-09,-2.68973e-13,-55305.1,17.899], Tmin=(788.976,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-443.646,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: FCF
H298 = -107.71988529999999 kcal/mol
""",
    rank = 5,
)

entry(
    index = 83,
    label = "Chlorine fluoride",
    molecule = 
"""
1 Cl u0 p3 c0 {2,S}
2 F  u0 p3 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.51957,-0.00177045,1.70581e-05,-3.05891e-08,1.73665e-11,-7769.15,6.13565], Tmin=(10,'K'), Tmax=(590.895,'K')),
            NASAPolynomial(coeffs=[3.46968,0.00208041,-1.63558e-06,5.63433e-10,-7.07257e-14,-7878.69,5.83113], Tmin=(590.895,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-56.0527,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: FCl
H298 = -13.31548757 kcal/mol
""",
    rank = 5,
)

entry(
    index = 84,
    label = "Difluorine",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 F u0 p3 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.51828,-0.00125712,8.98951e-06,-1.18664e-08,4.9918e-12,-1050.88,4.31705], Tmin=(10,'K'), Tmax=(772.592,'K')),
            NASAPolynomial(coeffs=[3.2138,0.00225397,-1.58351e-06,4.98172e-10,-5.80159e-14,-672.508,5.33378], Tmin=(772.592,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (3.27766,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: FF
H298 = 0.0 kcal/mol
""",
    rank = 5,
)

entry(
    index = 85,
    label = "Oxygen difluoride",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {3,S}
3 O u0 p2 c0 {1,S} {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.03449,-0.00336126,4.20188e-05,-7.82672e-08,4.57369e-11,1663.01,6.37844], Tmin=(10,'K'), Tmax=(574.663,'K')),
            NASAPolynomial(coeffs=[3.91346,0.00598694,-4.58407e-06,1.5533e-09,-1.93094e-13,1801.75,5.67331], Tmin=(574.663,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (29.1615,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: FOF
H298 = 5.86998088 kcal/mol
""",
    rank = 5,
)

entry(
    index = 86,
    label = "Difluorodioxidane",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {4,S}
3 O u0 p2 c0 {1,S} {4,S}
4 O u0 p2 c0 {2,S} {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94266,0.00327275,4.37043e-05,-9.21323e-08,5.45215e-11,2244.85,8.29295], Tmin=(10,'K'), Tmax=(605.111,'K')),
            NASAPolynomial(coeffs=[4.9562,0.0104152,-8.31467e-06,2.98258e-09,-3.93685e-13,2274.79,1.81831], Tmin=(605.111,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (39.7382,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (78.9875,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: FOOF
H298 = 7.540630975 kcal/mol
""",
    rank = 5,
)

entry(
    index = 87,
    label = "Trifluoromethyl",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 F u0 p3 c0 {4,S}
4 C u1 p0 c0 {1,S} {2,S} {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05587,-0.0054938,7.30062e-05,-1.34908e-07,7.857e-11,-57638.2,8.13986], Tmin=(10,'K'), Tmax=(570.231,'K')),
            NASAPolynomial(coeffs=[3.53924,0.0118582,-8.75006e-06,2.89362e-09,-3.54041e-13,-58277.3,8.38507], Tmin=(570.231,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-468.975,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: F[C](F)F
H298 = -111.79732309999999 kcal/mol
""",
    rank = 5,
)

entry(
    index = 88,
    label = "Dibromophosgene",
    molecule = 
"""
1 Br u0 p3 c0 {4,S}
2 Br u0 p3 c0 {4,S}
3 O  u0 p2 c0 {4,D}
4 C  u0 p0 c0 {1,S} {2,S} {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89242,0.00765783,5.59627e-05,-1.86029e-07,1.60268e-10,-15403.6,11.471], Tmin=(10,'K'), Tmax=(440.312,'K')),
            NASAPolynomial(coeffs=[5.94519,0.00737458,-5.63603e-06,1.96274e-09,-2.53638e-13,-16325.2,1.2299], Tmin=(440.312,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-102.769,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: O=C(Br)Br
H298 = -27.22753346 kcal/mol
""",
    rank = 5,
)

entry(
    index = 89,
    label = "Phosgene",
    molecule = 
"""
1 Cl u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {4,S}
3 O  u0 p2 c0 {4,D}
4 C  u0 p0 c0 {1,S} {2,S} {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93491,0.00401054,4.55748e-05,-1.09905e-07,7.35764e-11,-27927.1,9.28615], Tmin=(10,'K'), Tmax=(541.21,'K')),
            NASAPolynomial(coeffs=[5.14547,0.00901362,-6.95538e-06,2.42857e-09,-3.13456e-13,-28590.4,2.3016], Tmin=(541.21,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-220.12,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: O=C(Cl)Cl
H298 = -52.37571702 kcal/mol
""",
    rank = 5,
)

entry(
    index = 90,
    label = "Difluorophosgene",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 O u0 p2 c0 {4,D}
4 C u0 p0 c0 {1,S} {2,S} {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.06775,-0.00614966,6.73615e-05,-1.17623e-07,6.56735e-11,-74271.4,7.68563], Tmin=(10,'K'), Tmax=(584.627,'K')),
            NASAPolynomial(coeffs=[3.15981,0.0116963,-8.27581e-06,2.66621e-09,-3.20585e-13,-74493.3,9.87819], Tmin=(584.627,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-604.43,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: O=C(F)F
H298 = -144.94502869999997 kcal/mol
""",
    rank = 5,
)

entry(
    index = 91,
    label = "Formyl chloride",
    molecule = 
"""
1 Cl u0 p3 c0 {3,S}
2 O  u0 p2 c0 {3,D}
3 C  u0 p0 c0 {1,S} {2,D} {4,S}
4 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.03409,-0.00372951,5.17846e-05,-1.0006e-07,6.39443e-11,-23360,7.75699], Tmin=(10,'K'), Tmax=(480.467,'K')),
            NASAPolynomial(coeffs=[2.98088,0.00996395,-6.34232e-06,1.92887e-09,-2.24693e-13,-23518,11.4745], Tmin=(480.467,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-181.688,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: O=CCl
H298 = -43.78585086 kcal/mol
""",
    rank = 5,
)

entry(
    index = 92,
    label = "Formyl fluoride",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,S} {2,D} {4,S}
4 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05425,-0.00375329,3.18277e-05,-4.07297e-08,1.68956e-11,-47221.6,6.56837], Tmin=(10,'K'), Tmax=(745.315,'K')),
            NASAPolynomial(coeffs=[2.27714,0.0104751,-6.24845e-06,1.77292e-09,-1.93455e-13,-47288.4,13.7455], Tmin=(745.315,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-380.284,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: O=CF
H298 = -91.35516252 kcal/mol
""",
    rank = 5,
)

entry(
    index = 93,
    label = "Chloroformyl",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {3,S}
2 O  u0 p2 c0 {3,D}
3 C  u1 p0 c0 {1,S} {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96971,0.00204294,2.18869e-05,-6.00548e-08,4.61322e-11,-3839.22,7.99725], Tmin=(10,'K'), Tmax=(470.281,'K')),
            NASAPolynomial(coeffs=[4.41731,0.00399715,-2.72231e-06,8.8066e-10,-1.08824e-13,-4199.59,5.49819], Tmin=(470.281,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-23.9716,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: O=[C]Cl
H298 = -4.9067877630000005 kcal/mol
""",
    rank = 5,
)

entry(
    index = 94,
    label = "Fluoroformyl",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {3,S}
2 O u0 p2 c0 {3,D}
3 C u1 p0 c0 {1,S} {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.02994,-0.00208576,2.20825e-05,-3.30628e-08,1.5841e-11,-22418.1,6.85532], Tmin=(10,'K'), Tmax=(668.186,'K')),
            NASAPolynomial(coeffs=[3.39014,0.00554951,-3.6e-06,1.08417e-09,-1.23809e-13,-22894.5,9.04838], Tmin=(668.186,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-180.567,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: O=[C]F
H298 = -42.07456979 kcal/mol
""",
    rank = 5,
)

entry(
    index = 95,
    label = "Hypobromous acid",
    molecule = 
"""
1 Br u0 p3 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.02867,-0.00270475,2.86486e-05,-5.37779e-08,3.27903e-11,-8709.05,6.76736], Tmin=(10,'K'), Tmax=(537.04,'K')),
            NASAPolynomial(coeffs=[3.79726,0.00367933,-2.19982e-06,6.75608e-10,-8.09052e-14,-8702.02,7.11421], Tmin=(537.04,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-51.1695,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: OBr
H298 = -14.8374761 kcal/mol
""",
    rank = 5,
)

entry(
    index = 96,
    label = "2-Bromoethanol",
    molecule = 
"""
1 Br u0 p3 c0 {4,S}
2 O  u0 p2 c0 {3,S} {9,S}
3 C  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 C  u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {4,S}
8 H  u0 p0 c0 {4,S}
9 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87686,0.00731498,0.000107783,-2.30555e-07,1.42777e-10,-28562.3,10.407], Tmin=(10,'K'), Tmax=(565.609,'K')),
            NASAPolynomial(coeffs=[5.13626,0.0266093,-1.81741e-05,6.05837e-09,-7.69876e-13,-28577.5,1.06117], Tmin=(565.609,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-192.494,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (199.547,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: OCCBr
H298 = -52.69837476 kcal/mol
""",
    rank = 5,
)

entry(
    index = 97,
    label = "2-Chloroethanol",
    molecule = 
"""
1 Cl u0 p3 c0 {4,S}
2 O  u0 p2 c0 {3,S} {9,S}
3 C  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 C  u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {4,S}
8 H  u0 p0 c0 {4,S}
9 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8856,0.00664489,0.000103911,-2.13097e-07,1.27002e-10,-34068.9,9.24449], Tmin=(10,'K'), Tmax=(584.173,'K')),
            NASAPolynomial(coeffs=[4.78104,0.0275285,-1.90798e-05,6.42443e-09,-8.21383e-13,-34135.8,1.46052], Tmin=(584.173,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-246.489,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (199.547,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: OCCCl
H298 = -63.70936902 kcal/mol
""",
    rank = 5,
)

entry(
    index = 98,
    label = "2-Fluoroethanol",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 O u0 p2 c0 {3,S} {9,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90619,0.00529487,9.61873e-05,-1.83947e-07,1.03574e-10,-52807.6,8.28151], Tmin=(10,'K'), Tmax=(606.252,'K')),
            NASAPolynomial(coeffs=[3.69936,0.0295955,-2.06865e-05,6.9776e-09,-8.90908e-13,-52858.4,5.69957], Tmin=(606.252,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-403.659,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (199.547,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: OCCF
H298 = -101.0970363 kcal/mol
""",
    rank = 5,
)

entry(
    index = 99,
    label = "Chloromethanol",
    molecule = 
"""
1 Cl u0 p3 c0 {3,S}
2 O  u0 p2 c0 {3,S} {6,S}
3 C  u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H  u0 p0 c0 {3,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97204,0.00163864,4.80133e-05,-8.74742e-08,4.9564e-11,-30708.8,8.7193], Tmin=(10,'K'), Tmax=(553.368,'K')),
            NASAPolynomial(coeffs=[2.61936,0.0174417,-1.11565e-05,3.48717e-09,-4.2002e-13,-30489.3,13.6112], Tmin=(553.368,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-231.132,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (128.874,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: OCCl
H298 = -57.98279159 kcal/mol
""",
    rank = 5,
)

entry(
    index = 100,
    label = "Hypochlorous acid",
    molecule = 
"""
1 Cl u0 p3 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.02901,-0.00244123,2.23322e-05,-3.66129e-08,1.9704e-11,-10464.3,5.49775], Tmin=(10,'K'), Tmax=(592.963,'K')),
            NASAPolynomial(coeffs=[3.59317,0.00388795,-2.25187e-06,6.65748e-10,-7.70517e-14,-10170.6,6.87023], Tmin=(592.963,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-71.3219,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: OCl
H298 = -18.35779159 kcal/mol
""",
    rank = 5,
)

entry(
    index = 101,
    label = "Hypofluorous acid",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.02848,-0.00192233,1.33972e-05,-1.61993e-08,6.45714e-12,-11703,4.36077], Tmin=(10,'K'), Tmax=(768.674,'K')),
            NASAPolynomial(coeffs=[3.2293,0.00415811,-2.21832e-06,5.96331e-10,-6.32051e-14,-11391.9,7.63678], Tmin=(768.674,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-82.3063,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: OF
H298 = -20.86281071 kcal/mol
""",
    rank = 5,
)

entry(
    index = 102,
    label = "Peroxyhypochlorous acid",
    molecule = 
"""
1 Cl u0 p3 c0 {3,S}
2 O  u0 p2 c0 {3,S} {4,S}
3 O  u0 p2 c0 {1,S} {2,S}
4 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94694,0.00314254,3.74897e-05,-8.5074e-08,5.36851e-11,-1663.9,8.54355], Tmin=(10,'K'), Tmax=(574.198,'K')),
            NASAPolynomial(coeffs=[5.03333,0.00768376,-6.00698e-06,2.1552e-09,-2.8452e-13,-1635.09,2.16679], Tmin=(574.198,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (6.8112,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (78.9875,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: OOCl
H298 = -0.317877629 kcal/mol
""",
    rank = 5,
)

entry(
    index = 103,
    label = "Chlorohydroxymethyl",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {3,S}
2 O  u0 p2 c0 {3,S} {5,S}
3 C  u1 p0 c0 {1,S} {2,S} {4,S}
4 H  u0 p0 c0 {3,S}
5 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93666,0.00360101,4.80544e-05,-1.00369e-07,5.91332e-11,-8875.32,8.30606], Tmin=(10,'K'), Tmax=(608.981,'K')),
            NASAPolynomial(coeffs=[5.15344,0.0110534,-8.34398e-06,3.01698e-09,-4.05617e-13,-9407.68,0.687908], Tmin=(608.981,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-55.7238,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (103.931,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: O[CH]Cl
H298 = -14.48374761 kcal/mol
""",
    rank = 5,
)

entry(
    index = 104,
    label = "Chloromethyl",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {2,S}
2 C  u1 p0 c0 {1,S} {3,S} {4,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86219,0.0142634,-5.7405e-05,1.24395e-07,-9.29955e-11,12386.8,6.84207], Tmin=(10,'K'), Tmax=(449.622,'K')),
            NASAPolynomial(coeffs=[3.70085,0.00689427,-3.4478e-06,8.39322e-10,-7.99379e-14,12352.1,8.48115], Tmin=(449.622,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (115.956,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: [CH2]Cl
H298 = 27.55497132 kcal/mol
""",
    rank = 5,
)

entry(
    index = 105,
    label = "Bromovinylidene",
    molecule = 
"""
multiplicity 3
1 Br u0 p3 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,D} {4,S}
3 C  u2 p0 c0 {2,D}
4 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95831,0.00250161,3.57495e-05,-7.81591e-08,4.9196e-11,53862.2,9.75622], Tmin=(10,'K'), Tmax=(557.736,'K')),
            NASAPolynomial(coeffs=[4.39566,0.00872987,-6.18736e-06,2.07376e-09,-2.62048e-13,73921,6.59582], Tmin=(557.736,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (634.962,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: [C]=CBr
H298 = 109.9665392 kcal/mol
""",
    rank = 5,
)

entry(
    index = 106,
    label = "Chlorovinylidene",
    molecule = 
"""
1 Cl u0 p3 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,D} {4,S}
3 C  u0 p1 c0 {2,D}
4 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89899,0.0107072,-2.59181e-05,6.43747e-08,-6.17789e-11,50186.4,7.77545], Tmin=(10,'K'), Tmax=(357.143,'K')),
            NASAPolynomial(coeffs=[3.74091,0.00923104,-6.08218e-06,1.89357e-09,-2.24222e-13,49917.6,8.66523], Tmin=(357.143,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (425.719,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: [C]=CCl
H298 = 102.7246654 kcal/mol
""",
    rank = 5,
)

entry(
    index = 107,
    label = "Bromooxidanyl",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {2,S}
2 O  u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.51947,-0.00191589,1.99991e-05,-3.87037e-08,2.3647e-11,13791.9,7.86441], Tmin=(10,'K'), Tmax=(553.304,'K')),
            NASAPolynomial(coeffs=[3.5363,0.00201074,-1.62087e-06,5.69301e-10,-7.25704e-14,14847.7,7.23319], Tmin=(553.304,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (140.589,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: [O]Br
H298 = 29.54349904 kcal/mol
""",
    rank = 5,
)

entry(
    index = 108,
    label = "Chloromethoxy",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {3,S}
2 O  u1 p2 c0 {3,S}
3 C  u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H  u0 p0 c0 {3,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05317,-0.00535402,7.64236e-05,-1.41945e-07,8.54719e-11,-3677.73,8.7587], Tmin=(10,'K'), Tmax=(527.733,'K')),
            NASAPolynomial(coeffs=[2.72786,0.0147928,-9.55276e-06,2.93626e-09,-3.4441e-13,-4014.34,12.9728], Tmin=(527.733,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-14.9254,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: [O]CCl
H298 = -4.5172084130000005 kcal/mol
""",
    rank = 5,
)

entry(
    index = 109,
    label = "Fluorooxidanyl",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 O u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.51779,-0.00115859,7.7708e-06,-9.55983e-09,3.74809e-12,12288.7,5.42233], Tmin=(10,'K'), Tmax=(823.913,'K')),
            NASAPolynomial(coeffs=[3.16214,0.00226288,-1.54389e-06,4.73852e-10,-5.4015e-14,12351.2,6.72012], Tmin=(823.913,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (111.42,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: [O]F
H298 = 26.50334608 kcal/mol
""",
    rank = 5,
)

entry(
    index = 110,
    label = "Fluorodioxidanyl",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u1 p2 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98216,0.00101488,1.81021e-05,-3.53706e-08,2.01549e-11,1687.67,7.38172], Tmin=(10,'K'), Tmax=(599.238,'K')),
            NASAPolynomial(coeffs=[3.92533,0.00567567,-4.28187e-06,1.45535e-09,-1.83029e-13,1814.04,6.9854], Tmin=(599.238,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (28.8945,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """ATcT_1.122p""",
    longDesc = 
"""
ATcT_1.122p H298 with b3lyp/6-31g(2df,p) freq and 1D HR
SMILES: [O]OF
H298 = 5.999043977 kcal/mol
""",
    rank = 5,
)

entry(
    index = 111,
    label = "Br",
    molecule = 
"""
multiplicity 2
1 Br u1 p3 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.48422,0.000161406,-5.63461e-07,7.46724e-10,-2.58956e-13,7867.65,6.86657], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.08902,0.000711612,-2.69887e-07,4.15012e-11,-2.3138e-15,12855.6,9.07043], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (105.654,'kJ/mol'),
        Cp0 = (20.7862,'J/mol/K'),
        CpInf = (20.7862,'J/mol/K'),
    ),
    shortDesc = """J 6/74 H298 from ATcT_1.122p""",
    longDesc = 
"""
J 6/74
BR                J 6/74BR  1    0    0    0G   300.00   5000.00  1000.00      1
0.20843207E+01 0.71949483E-03-0.27419924E-06 0.42422650E-10-0.23791570E-14    2
0.12858837E+05 0.90838003E+01 0.24611551E+01 0.33319275E-03-0.10080655E-05    3
0.12262126E-08-0.44283510E-12 0.12711920E 05 0.69494733E+01                   4.
[Br]
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

