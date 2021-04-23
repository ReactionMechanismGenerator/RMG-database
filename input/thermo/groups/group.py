#!/usr/bin/env python
# encoding: utf-8

name = "Functional Group Additivity Values"
shortDesc = ""
longDesc = """

"""
entry(
    index = 0,
    label = "R",
    group = 
"""
1 * R ux
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1,
    label = "C",
    group = 
"""
1 * C u0
""",
    thermo = 'Cs-CsCsCsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2,
    label = "CJ2_singlet",
    group = 
"""
1 * C u0 p1
""",
    thermo = 'CsJ2_singlet-CsH',
    shortDesc = """Branch for singlet carbenes""",
    longDesc = 
"""

""",
)

entry(
    index = 3,
    label = "CsJ2_singlet-HH",
    group = 
"""
1 * C2s u0 p1 {2,S} {3,S}
2   H   u0 {1,S}
3   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.069,8.313,8.631,8.994,9.768,10.497,11.825],'cal/(mol*K)'),
        H298 = (102.462,'kcal/mol'),
        S298 = (45.144,'cal/(mol*K)'),
    ),
    shortDesc = """Fitted to DFT_QCI_thermo library""",
    longDesc = 
"""
Fitted to RQCISD(T)/cc-PV(infinity)(Q)Z calculations of:

Goldsmith, C. F.; Magoon, G. R.; Green, W. H., Database of Small Molecule Thermochemistry for Combustion.
J. Phys. Chem. A 2012, 116, 9033-9057.
""",
)

entry(
    index = 4,
    label = "CsJ2_singlet-OsH",
    group = 
"""
1 * C2s u0 p1 {2,S} {3,S}
2   O2s u0 {1,S}
3   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.075,5.312,6.211,6.926,8.355,9.557,10.212],'cal/(mol*K)'),
        H298 = (65.592,'kcal/mol'),
        S298 = (23.749,'cal/(mol*K)'),
    ),
    shortDesc = """Fitted to DFT_QCI_thermo library""",
    longDesc = 
"""
Fitted to RQCISD(T)/cc-PV(infinity)(Q)Z calculations of:

Goldsmith, C. F.; Magoon, G. R.; Green, W. H., Database of Small Molecule Thermochemistry for Combustion.
J. Phys. Chem. A 2012, 116, 9033-9057.
""",
)

entry(
    index = 5,
    label = "CdJ2_singlet-Od",
    group = 
"""
1 * C2d u0 p1 {2,D}
2   O2d u0 p2 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.5,-2.38,-3.32,-4.24,-5.75,-6.88,-8.59],'cal/(mol*K)'),
        H298 = (103.73,'kcal/mol'),
        S298 = (-6.47,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated in relation to formaldehyde from NIST values""",
    longDesc = 
"""

""",
)

entry(
    index = 6,
    label = "CdJ2_singlet-Sd",
    group = 
"""
1 * C2d u0 p1 {2,D}
2   S2d u0 p2 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.97,-2.97,-3.85,-4.6,-5.82,-6.79,-8.44],'cal/(mol*K)'),
        H298 = (143.53,'kcal/mol'),
        S298 = (-6.23,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 7,
    label = "CdJ2_singlet-(Cdd-Od)",
    group = 
"""
1   Cdd u0 {2,D} {3,D}
2 * C2d u0 p1 {1,D}
3   O2d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.135,11.201,11.749,12.051,12.813,13.581,14.122],'cal/(mol*K)'),
        H298 = (110.367,'kcal/mol'),
        S298 = (53.61,'cal/(mol*K)'),
    ),
    shortDesc = """Fitted to DFT_QCI_thermo library""",
    longDesc = 
"""
Fitted to RQCISD(T)/cc-PV(infinity)(Q)Z calculations of:

Goldsmith, C. F.; Magoon, G. R.; Green, W. H., Database of Small Molecule Thermochemistry for Combustion.
J. Phys. Chem. A 2012, 116, 9033-9057.
""",
)

entry(
    index = 8,
    label = "CsJ2_singlet-CH",
    group = 
"""
1   C   u0 {2,S}
2 * C2s u0 p1 {1,S} {3,S}
3   H   u0 {2,S}
""",
    thermo = 'CsJ2_singlet-CsH',
    shortDesc = """Branch for singlet carbenes single-bonded to one carbon and one hydrogen""",
    longDesc = 
"""

""",
)

entry(
    index = 9,
    label = "CsJ2_singlet-CsH",
    group = 
"""
1   Cs  u0 {2,S}
2 * C2s u0 p1 {1,S} {3,S}
3   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.255,5.932,6.136,6.192,6.77,7.73,8.134],'cal/(mol*K)'),
        H298 = (97.669,'kcal/mol'),
        S298 = (29.684,'cal/(mol*K)'),
    ),
    shortDesc = """Fitted to DFT_QCI_thermo library""",
    longDesc = 
"""
Fitted to RQCISD(T)/cc-PV(infinity)(Q)Z calculations of:

Goldsmith, C. F.; Magoon, G. R.; Green, W. H., Database of Small Molecule Thermochemistry for Combustion.
J. Phys. Chem. A 2012, 116, 9033-9057.
""",
)

entry(
    index = 10,
    label = "CsJ2_singlet-CtH",
    group = 
"""
1   Ct  u0 {2,S}
2 * C2s u0 p1 {1,S} {3,S}
3   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.675,6.472,6.776,6.9,7.469,8.156,7.58],'cal/(mol*K)'),
        H298 = (88.247,'kcal/mol'),
        S298 = (28.407,'cal/(mol*K)'),
    ),
    shortDesc = """Fitted to DFT_QCI_thermo library""",
    longDesc = 
"""
Fitted to RQCISD(T)/cc-PV(infinity)(Q)Z calculations of:

Goldsmith, C. F.; Magoon, G. R.; Green, W. H., Database of Small Molecule Thermochemistry for Combustion.
J. Phys. Chem. A 2012, 116, 9033-9057.
""",
)

entry(
    index = 11,
    label = "CdJ2_singlet-Cd",
    group = 
"""
1   C   u0 {2,D}
2 * C2d u0 p1 {1,D}
""",
    thermo = 'CdJ2_singlet-Cds',
    shortDesc = """Branch for singlet carbenes double-bonded to one carbon""",
    longDesc = 
"""

""",
)

entry(
    index = 12,
    label = "CdJ2_singlet-Cds",
    group = 
"""
1   Cd  u0 {2,D}
2 * C2d u0 p1 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.372,5.272,4.916,4.506,4.219,4.263,3.97],'cal/(mol*K)'),
        H298 = (92.157,'kcal/mol'),
        S298 = (26.864,'cal/(mol*K)'),
    ),
    shortDesc = """Fitted to DFT_QCI_thermo library""",
    longDesc = 
"""
Fitted to RQCISD(T)/cc-PV(infinity)(Q)Z calculations of:

Goldsmith, C. F.; Magoon, G. R.; Green, W. H., Database of Small Molecule Thermochemistry for Combustion.
J. Phys. Chem. A 2012, 116, 9033-9057.
""",
)

entry(
    index = 13,
    label = "CdJ2_singlet-(Cdd-Cds)",
    group = 
"""
1   Cdd u0 {2,D} {3,D}
2 * C2d u0 p1 {1,D}
3   C   u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.406,3.333,3.175,3.019,3.156,3.468,3.593],'cal/(mol*K)'),
        H298 = (91.676,'kcal/mol'),
        S298 = (26.434,'cal/(mol*K)'),
    ),
    shortDesc = """Fitted to DFT_QCI_thermo library""",
    longDesc = 
"""
Fitted to RQCISD(T)/cc-PV(infinity)(Q)Z calculations of:

Goldsmith, C. F.; Magoon, G. R.; Green, W. H., Database of Small Molecule Thermochemistry for Combustion.
J. Phys. Chem. A 2012, 116, 9033-9057.
""",
)

entry(
    index = 14,
    label = "CsJ2_singlet-(Cds-Cds-Cds-C)C",
    group = 
"""
1   C   u0 {2,D}
2   Cd  u0 {1,D} {6,S}
3   C   u0 {4,S}
4 * C2s u0 p1 {3,S} {5,S}
5   Cd  u0 {4,S} {6,D}
6   Cd  u0 {2,S} {5,D}
""",
    thermo = 'CsJ2_singlet-(Cds-Cds-Cds-Cds)Cs_6_ring',
    shortDesc = """Branch for singlet carbenes delocalized over two conjugated carbon double bonds""",
    longDesc = 
"""

""",
)

entry(
    index = 15,
    label = "CsJ2_singlet-(Cds-Cds-Cds-Cds)Cs_5_ring",
    group = 
"""
1   Cd  u0 {2,D}
2   Cd  u0 {1,D} {3,S} {6,S}
3   Cs  u0 {2,S} {4,S}
4 * C2s u0 p1 {3,S} {5,S}
5   Cd  u0 {4,S} {6,D}
6   Cd  u0 {2,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.025,5.12,5.268,4.917,4.799,5.731,5.087],'cal/(mol*K)'),
        H298 = (82.041,'kcal/mol'),
        S298 = (10.325,'cal/(mol*K)'),
    ),
    shortDesc = """Fitted to DFT_QCI_thermo library""",
    longDesc = 
"""
Fitted to RQCISD(T)/cc-PV(infinity)(Q)Z calculations of:

    Goldsmith, C. F.; Magoon, G. R.; Green, W. H., Database of Small Molecule Thermochemistry for Combustion.
    J. Phys. Chem. A 2012, 116, 9033-9057.
""",
)

entry(
    index = 16,
    label = "CsJ2_singlet-(Cds-Cds-Cds-Cds)Cs_6_ring",
    group = 
"""
1   Cd  u0 {2,D} {3,S}
2   Cd  u0 {1,D} {6,S}
3   Cs  u0 {1,S} {4,S}
4 * C2s u0 p1 {3,S} {5,S}
5   Cd  u0 {4,S} {6,D}
6   Cd  u0 {2,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.322,5.406,5.554,5.182,5.008,5.927,5.232],'cal/(mol*K)'),
        H298 = (80.263,'kcal/mol'),
        S298 = (12.963,'cal/(mol*K)'),
    ),
    shortDesc = """Fitted to DFT_QCI_thermo library""",
    longDesc = 
"""
Fitted to RQCISD(T)/cc-PV(infinity)(Q)Z calculations of:

    Goldsmith, C. F.; Magoon, G. R.; Green, W. H., Database of Small Molecule Thermochemistry for Combustion.
    J. Phys. Chem. A 2012, 116, 9033-9057.
""",
)

entry(
    index = 17,
    label = "Cbf",
    group = 
"""
1 * Cbf u0
""",
    thermo = 'Cbf-CbCbCbf',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 18,
    label = "Cbf-CbCbCbf",
    group = 
"""
1 * Cbf u0 {2,B} {3,B} {4,B}
2   Cb  u0 {1,B}
3   Cb  u0 {1,B}
4   Cbf u0 {1,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.01,3.68,4.2,4.61,5.2,5.7,6.2],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (4.8,'kcal/mol','+|-',0.17),
        S298 = (-5,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = """Cbf-CbfCbCb STEIN and FAHR; J. PHYS. CHEM. 1985, 89, 17, 3714""",
    longDesc = 
"""

""",
)

entry(
    index = 19,
    label = "Cbf-CbCbfCbf",
    group = 
"""
1 * Cbf u0 {2,B} {3,B} {4,B}
2   Cb  u0 {1,B}
3   Cbf u0 {1,B}
4   Cbf u0 {1,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.01,3.68,4.2,4.61,5.2,5.7,6.2],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (3.7,'kcal/mol','+|-',0.3),
        S298 = (-5,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = """Cbf-CbfCbfCb STEIN and FAHR; J. PHYS. CHEM. 1985, 89, 17, 3714""",
    longDesc = 
"""

""",
)

entry(
    index = 20,
    label = "Cbf-CbfCbfCbf",
    group = 
"""
1  * Cbf u0 p0 c0 {2,B} {3,B} {6,B}
2    Cbf u0 p0 c0 {1,B} {4,B} {5,B}
3    Cbf u0 p0 c0 {1,B} {8,B} {9,B}
4    Cbf u0 p0 c0 {2,B} {10,B} {11,B}
5    Cbf u0 p0 c0 {2,B} {13,B} {14,B}
6    Cbf u0 p0 c0 {1,B} {15,B} {16,B}
7    C   u0 p0 c0 {8,B} {16,B}
8    C   u0 p0 c0 {3,B} {7,B}
9    C   u0 p0 c0 {3,B} {10,B}
10   C   u0 p0 c0 {4,B} {9,B}
11   C   u0 p0 c0 {4,B} {12,B}
12   C   u0 p0 c0 {11,B} {13,B}
13   C   u0 p0 c0 {5,B} {12,B}
14   C   u0 p0 c0 {5,B} {15,B}
15   C   u0 p0 c0 {6,B} {14,B}
16   C   u0 p0 c0 {6,B} {7,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2,3.11,3.9,4.42,5,5.3,5.7],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (1.5,'kcal/mol','+|-',0.3),
        S298 = (1.8,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = """Cbf-CbfCbfCbf STEIN and FAHR; J. PHYS. CHEM. 1985, 89, 17, 3714""",
    longDesc = 
"""
The smallest PAH that can have Cbf-CbfCbfCbf is pyrene. Currently the database is restricted
that any group with more three Cbf atoms must have all benzene rings explicitly written out.
Previously, this node would also match one carbon on Benzo[c]phenanthrene and does not now.
Examples from the original source do not include Benzo[c]phenanthrene.
""",
)

entry(
    index = 21,
    label = "Cb",
    group = 
"""
1 * Cb u0
""",
    thermo = 'Cb-Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 22,
    label = "Cb-H",
    group = 
"""
1 * Cb u0 {2,S}
2   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.24,4.44,5.46,6.3,7.54,8.41,9.73],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (3.3,'kcal/mol','+|-',0.11),
        S298 = (11.53,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = """Cb-H BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 23,
    label = "Cb-O2s",
    group = 
"""
1 * Cb  u0 {2,S}
2   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.9,5.3,6.2,6.6,6.9,6.9,7.07],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-0.9,'kcal/mol','+|-',0.16),
        S298 = (-10.2,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = """Cb-O BENSON Cp1500=3D Cp1000*(Cp1500/Cp1000: Cb/Cd)""",
    longDesc = 
"""

""",
)

entry(
    index = 24,
    label = "Cb-S",
    group = 
"""
1 * Cb u0 {2,S}
2   S  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.75,3.75,3.47,3.5,5.18,6.15,4.65],'cal/(mol*K)'),
        H298 = (18.76,'kcal/mol'),
        S298 = (-0.62,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 25,
    label = "Cb-N3s",
    group = 
"""
1 * Cb  u0 {2,S}
2   N3s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.95,5.21,5.94,6.32,6.53,6.56,6.635],'cal/(mol*K)'),
        H298 = (-0.5,'kcal/mol'),
        S298 = (-9.69,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 26,
    label = "Cb-C",
    group = 
"""
1 * Cb u0 {2,S}
2   C  u0 {1,S}
""",
    thermo = 'Cb-Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 27,
    label = "Cb-Cs",
    group = 
"""
1 * Cb u0 {2,S}
2   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.67,3.14,3.68,4.15,4.96,5.44,5.98],'cal/(mol*K)','+|-',[0.07,0.07,0.07,0.07,0.07,0.07,0.07]),
        H298 = (5.51,'kcal/mol','+|-',0.13),
        S298 = (-7.69,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = """Cb-Cs BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 28,
    label = "Cb-Cds",
    group = 
"""
1 * Cb         u0 {2,S}
2   [Cd,CO,CS] u0 {1,S}
""",
    thermo = 'Cb-(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 29,
    label = "Cb-(Cds-O2d)",
    group = 
"""
1 * Cb  u0 {2,S}
2   CO  u0 {1,S} {3,D}
3   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.59,3.97,4.38,4.72,5.28,5.61,5.75],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (3.69,'kcal/mol','+|-',0.2),
        S298 = (-7.8,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = """Enthalpy from Cb-CO, entropies and heat capacities assigned value of Cb-Cd""",
    longDesc = 
"""

""",
)

entry(
    index = 30,
    label = "Cb-(Cds-Cd)",
    group = 
"""
1 * Cb u0 {2,S}
2   Cd u0 {1,S} {3,D}
3   C  u0 {2,D}
""",
    thermo = 'Cb-(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 31,
    label = "Cb-(Cds-Cds)",
    group = 
"""
1 * Cb u0 {2,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.59,3.97,4.38,4.72,5.28,5.61,5.75],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (5.69,'kcal/mol','+|-',0.2),
        S298 = (-7.8,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = """Cb-Cd STEIN and FAHR; J. PHYS. CHEM. 1985, 89, 17, 3714""",
    longDesc = 
"""

""",
)

entry(
    index = 32,
    label = "Cb-(Cds-Cdd)",
    group = 
"""
1 * Cb  u0 {2,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D}
""",
    thermo = 'Cb-(Cds-Cdd-Cd)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 33,
    label = "Cb-(Cds-Cdd-O2d)",
    group = 
"""
1 * Cb  u0 {2,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {4,D}
4   O2d u0 {3,D}
""",
    thermo = 'Cb-(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 34,
    label = "Cb-(Cds-Cdd-S2d)",
    group = 
"""
1 * Cb  u0 {2,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {4,D}
4   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 35,
    label = "Cb-(Cds-Cdd-Cd)",
    group = 
"""
1 * Cb  u0 {2,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {4,D}
4   C   u0 {3,D}
""",
    thermo = 'Cb-(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 36,
    label = "Cb-Ct",
    group = 
"""
1 * Cb u0 {2,S}
2   Ct u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.59,3.97,4.38,4.72,5.28,5.61,5.75],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (5.69,'kcal/mol','+|-',0.3),
        S298 = (-7.8,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = """Cb-Ct STEIN and FAHR; J. PHYS. CHEM. 1985, 89, 17, 3714""",
    longDesc = 
"""

""",
)

entry(
    index = 37,
    label = "Cb-(CtN3t)",
    group = 
"""
1 * Cb  u0 {2,S}
2   Ct  u0 {1,S} {3,T}
3   N3t u0 {2,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.8,11.2,12.3,13.1,14.2,14.9,16.65],'cal/(mol*K)'),
        H298 = (35.8,'kcal/mol'),
        S298 = (20.5,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 38,
    label = "Cb-Cb",
    group = 
"""
1 * Cb u0 {2,S}
2   Cb u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.33,4.22,4.89,5.27,5.76,5.95,6.05],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (4.96,'kcal/mol','+|-',0.3),
        S298 = (-8.64,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = """Cb-Cb BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 39,
    label = "Cb-Cl",
    group = 
"""
1 * Cb   u0 {2,S}
2   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.4,8.4,9.2,9.7,10.2,10.4,10.4],'cal/(mol*K)'),
        H298 = (-3.8,'kcal/mol'),
        S298 = (18.9,'cal/(mol*K)'),
    ),
    shortDesc = """Cb-Cl BENSON""",
    longDesc = 
"""
Thermochemical Kinetics 2nd Ed., by Sidney Benson
""",
)

entry(
    index = 40,
    label = "Cb-I",
    group = 
"""
1 * Cb  u0 {2,S}
2   I1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8,8.9,9.6,9.9,10.3,10.5,10.7],'cal/(mol*K)'),
        H298 = (24,'kcal/mol'),
        S298 = (23.7,'cal/(mol*K)'),
    ),
    shortDesc = """Cb-I BENSON""",
    longDesc = 
"""
Thermochemical Kinetics 2nd Ed., by Sidney Benson (Table A4, p.281)
Cpdata at 1500K was not in the book, Cpdata at 1500K = Cpdata at 1000K + 0.2
""",
)

entry(
    index = 41,
    label = "Ct",
    group = 
"""
1 * Ct u0
""",
    thermo = 'Ct-CtCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 42,
    label = "Ct-CtN3s",
    group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   Ct  u0 {1,T}
3   N3s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 43,
    label = "Ct-N3tN3s",
    group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   N3t u0 {1,T}
3   N3s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 44,
    label = "Ct-CtH",
    group = 
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T}
3   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.28,5.99,6.49,6.87,7.47,7.96,8.85],'cal/(mol*K)','+|-',[0.07,0.07,0.07,0.07,0.07,0.07,0.07]),
        H298 = (26.93,'kcal/mol','+|-',0.05),
        S298 = (24.7,'cal/(mol*K)','+|-',0.07),
    ),
    shortDesc = """Ct-H STEIN and FAHR; J. PHYS. CHEM. 1985, 89, 17, 3714""",
    longDesc = 
"""

""",
)

entry(
    index = 45,
    label = "Ct-StH",
    group = 
"""
1 * Ct             u0 {2,T} {3,S}
2   [S4t,S6t,S6td] u0 {1,T}
3   H              u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.3,1.12,1.92,2.33,1.71,1.44,2.24],'cal/(mol*K)'),
        H298 = (98.15,'kcal/mol'),
        S298 = (-9.54,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""

""",
)

entry(
    index = 46,
    label = "Ct-CtOs",
    group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   Ct  u0 {1,T}
3   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.64,4.39,4.85,5.63,5.66,5.73,5.73],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (31.4,'kcal/mol','+|-',0.27),
        S298 = (4.91,'cal/(mol*K)','+|-',0.09),
    ),
    shortDesc = """Ct-O MELIUS / hc#coh !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
"""

""",
)

entry(
    index = 47,
    label = "Ct-N3tOs",
    group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   N3t u0 {1,T}
3   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 48,
    label = "Ct-CtS",
    group = 
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T}
3   S  u0 {1,S}
""",
    thermo = 'Ct-CtS2',
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 49,
    label = "Ct-CtS2",
    group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   Ct  u0 {1,T}
3   S2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.7,3.47,2.94,2.87,4.56,5.68,4.73],'cal/(mol*K)'),
        H298 = (45.23,'kcal/mol'),
        S298 = (14.57,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""

""",
)

entry(
    index = 50,
    label = "Ct-CtS4",
    group = 
"""
1 * Ct                u0 {2,T} {3,S}
2   Ct                u0 {1,T}
3   [S4s,S4d,S4b,S4t] u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.19,2.04,1.74,1.81,3.72,4.89,4.48],'cal/(mol*K)'),
        H298 = (56.56,'kcal/mol'),
        S298 = (12.4,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""

""",
)

entry(
    index = 51,
    label = "Ct-CtS6",
    group = 
"""
1 * Ct                      u0 {2,T} {3,S}
2   Ct                      u0 {1,T}
3   [S6s,S6d,S6dd,S6t,S6td] u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.29,3.67,4,4.29,4.74,5.05,5.49],'cal/(mol*K)'),
        H298 = (27.63,'kcal/mol'),
        S298 = (6.32,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 52,
    label = "Ct-N3tC",
    group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   N3t u0 {1,T}
3   C   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 53,
    label = "Ct-N3tCs",
    group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   N3t u0 {1,T}
3   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 54,
    label = "Ct-N3tCd",
    group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   N3t u0 {1,T}
3   Cd  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 55,
    label = "Ct-CtC",
    group = 
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T}
3   C  u0 {1,S}
""",
    thermo = 'Ct-CtCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 56,
    label = "Ct-CtCs",
    group = 
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T}
3   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.13,3.48,3.81,4.09,4.6,4.92,6.35],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (27.55,'kcal/mol','+|-',0.27),
        S298 = (6.35,'cal/(mol*K)','+|-',0.09),
    ),
    shortDesc = """Ct-Cs STEIN and FAHR; J. PHYS. CHEM. 1985, 89, 17, 3714""",
    longDesc = 
"""

""",
)

entry(
    index = 57,
    label = "Ct-CtCds",
    group = 
"""
1 * Ct         u0 {2,T} {3,S}
2   Ct         u0 {1,T}
3   [Cd,CO,CS] u0 {1,S}
""",
    thermo = 'Ct-Ct(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 58,
    label = "Ct-Ct(Cds-O2d)",
    group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   Ct  u0 {1,T}
3   CO  u0 {1,S} {4,D}
4   O2d u0 {3,D}
""",
    thermo = 'Ct-CtCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 59,
    label = "Ct-Ct(Cds-Cd)",
    group = 
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T}
3   Cd u0 {1,S} {4,D}
4   C  u0 {3,D}
""",
    thermo = 'Ct-Ct(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 60,
    label = "Ct-Ct(Cds-Cds)",
    group = 
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T}
3   Cd u0 {1,S} {4,D}
4   Cd u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.57,3.54,3.5,4.92,5.34,5.5,5.8],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (28.2,'kcal/mol','+|-',0.27),
        S298 = (6.43,'cal/(mol*K)','+|-',0.09),
    ),
    shortDesc = """Ct-Cd STEIN and FAHR; J. PHYS. CHEM. 1985, 89, 17, 3714""",
    longDesc = 
"""

""",
)

entry(
    index = 61,
    label = "Ct-Ct(Cds-Cdd)",
    group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   Ct  u0 {1,T}
3   Cd  u0 {1,S} {4,D}
4   Cdd u0 {3,D}
""",
    thermo = 'Ct-Ct(Cds-Cdd-Cd)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 62,
    label = "Ct-Ct(Cds-Cdd-O2d)",
    group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   Ct  u0 {1,T}
3   Cd  u0 {1,S} {4,D}
4   Cdd u0 {3,D} {5,D}
5   O2d u0 {4,D}
""",
    thermo = 'Ct-Ct(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 63,
    label = "Ct-Ct(Cds-Cdd-S2d)",
    group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   Ct  u0 {1,T}
3   Cd  u0 {1,S} {4,D}
4   Cdd u0 {3,D} {5,D}
5   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 64,
    label = "Ct-Ct(Cds-Cdd-Cd)",
    group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   Ct  u0 {1,T}
3   Cd  u0 {1,S} {4,D}
4   Cdd u0 {3,D} {5,D}
5   C   u0 {4,D}
""",
    thermo = 'Ct-Ct(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 65,
    label = "Ct-CtCt",
    group = 
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T}
3   Ct u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.54,4.06,4.4,4.64,5,5.23,5.57],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (25.6,'kcal/mol','+|-',0.27),
        S298 = (5.88,'cal/(mol*K)','+|-',0.09),
    ),
    shortDesc = """Ct-Ct STEIN and FAHR; J. PHYS. CHEM. 1985, 89, 17, 3714""",
    longDesc = 
"""

""",
)

entry(
    index = 66,
    label = "Ct-Ct(CtN3t)",
    group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   Ct  u0 {1,T}
3   Ct  u0 {1,S} {4,T}
4   N3t u0 {3,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.3,11.3,12.1,12.7,13.6,14.3,15.3],'cal/(mol*K)'),
        H298 = (63.8,'kcal/mol'),
        S298 = (35.4,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 67,
    label = "Ct-CtCb",
    group = 
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T}
3   Cb u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.57,3.54,4.5,4.92,5.34,5.5,5.8],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (24.67,'kcal/mol','+|-',0.27),
        S298 = (6.43,'cal/(mol*K)','+|-',0.09),
    ),
    shortDesc = """Ct-Cb STEIN and FAHR; J. PHYS. CHEM. 1985, 89, 17, 3714""",
    longDesc = 
"""

""",
)

entry(
    index = 68,
    label = "Cdd",
    group = 
"""
1 * Cdd u0
""",
    thermo = 'Cdd-CdsCds',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 69,
    label = "Cdd-N3dCd",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   N3d u0 {1,D}
3   Cd  u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.5,5.1,5.6,6,6.5,6.9,7.4],'cal/(mol*K)','+|-',[1.1,1.1,1.1,1.1,1.1,1.1,1.1]),
        H298 = (25.9,'kcal/mol','+|-',1.5),
        S298 = (19.7,'cal/(mol*K)','+|-',1.4),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 70,
    label = "Cdd-OdOd",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   O2d u0 {1,D}
3   O2d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.91,9.86,10.65,11.31,12.32,12.99,13.93],'cal/(mol*K)'),
        H298 = (-94.05,'kcal/mol','+|-',0.03),
        S298 = (52.46,'cal/(mol*K)','+|-',0.002),
    ),
    shortDesc = """CHEMKIN DATABASE: S(group) = S(CO2) + Rln(2)""",
    longDesc = 
"""

""",
)

entry(
    index = 71,
    label = "Cdd-OdSd",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   O2d u0 {1,D}
3   S2d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.81,10.84,11.62,12.18,12.99,13.52,14.14],'cal/(mol*K)'),
        H298 = (-34.78,'kcal/mol'),
        S298 = (55.34,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""

""",
)

entry(
    index = 72,
    label = "Cdd-SdSd",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   S   u0 {1,D}
3   S   u0 {1,D}
""",
    thermo = 'Cdd-S2dS2d',
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 73,
    label = "Cdd-S2dS2d",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   S2d u0 {1,D}
3   S2d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.91,11.83,12.49,12.98,13.63,14.01,14.47],'cal/(mol*K)'),
        H298 = (24.5,'kcal/mol'),
        S298 = (58.24,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 74,
    label = "Cdd-S4S4",
    group = 
"""
1 * Cdd        u0 {2,D} {3,D}
2   [S4d,S4dd] u0 {1,D}
3   [S4d,S4dd] u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.44,10.6,10.48,10.8,11.92,12.75,12.7],'cal/(mol*K)'),
        H298 = (54.12,'kcal/mol'),
        S298 = (66.19,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""

""",
)

entry(
    index = 75,
    label = "Cdd-S2S4",
    group = 
"""
1 * Cdd        u0 {2,D} {3,D}
2   S2d        u0 {1,D}
3   [S4d,S4dd] u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.88,11.09,11.15,11.47,12.26,12.78,13.01],'cal/(mol*K)'),
        H298 = (60.89,'kcal/mol'),
        S298 = (65.93,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""

""",
)

entry(
    index = 76,
    label = "Cdd-CdOd",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   C   u0 {1,D}
3   O2d u0 {1,D}
""",
    thermo = 'Cdd-CdsOd',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 77,
    label = "Cdd-CdsOd",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cd  u0 {1,D}
3   O2d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """O=C*=C< currently treat the adjacent C as Ck""",
    longDesc = 
"""

""",
)

entry(
    index = 78,
    label = "Cdd-CddOd",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cdd u0 {1,D}
3   O2d u0 {1,D}
""",
    thermo = 'Cdd-(Cdd-Cd)O2d',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 79,
    label = "Cdd-(Cdd-O2d)O2d",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cdd u0 {1,D} {4,D}
3   O2d u0 {1,D}
4   O2d u0 {2,D}
""",
    thermo = 'Cdd-CdsOd',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 80,
    label = "Cdd-(Cdd-Cd)O2d",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cdd u0 {1,D} {4,D}
3   O2d u0 {1,D}
4   C   u0 {2,D}
""",
    thermo = 'Cdd-CdsOd',
    shortDesc = """O=C*=C= currently not defined. Assigned same value as Ca""",
    longDesc = 
"""

""",
)

entry(
    index = 81,
    label = "Cdd-CdSd",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   C   u0 {1,D}
3   S   u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.88,8.48,8.8,8.99,9.23,9.37,9.58],'cal/(mol*K)'),
        H298 = (40.33,'kcal/mol'),
        S298 = (34.24,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 82,
    label = "Cdd-CdsSd",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cd  u0 {1,D}
3   S   u0 {1,D}
""",
    thermo = 'Cdd-CdsS6d',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 83,
    label = "Cdd-CdsS2d",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cd  u0 {1,D}
3   S2d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.88,8.48,8.8,8.99,9.23,9.37,9.58],'cal/(mol*K)'),
        H298 = (40.33,'kcal/mol'),
        S298 = (34.24,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 84,
    label = "Cdd-CdsS4d",
    group = 
"""
1 * Cdd        u0 {2,D} {3,D}
2   Cd         u0 {1,D}
3   [S4d,S4dd] u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.88,8.48,8.8,8.99,9.23,9.37,9.58],'cal/(mol*K)'),
        H298 = (40.33,'kcal/mol'),
        S298 = (34.24,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 85,
    label = "Cdd-CdsS6d",
    group = 
"""
1 * Cdd                   u0 {2,D} {3,D}
2   Cd                    u0 {1,D}
3   [S6d,S6dd,S6ddd,S6td] u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.18,7.47,7.69,7.97,8.76,9.31,9.81],'cal/(mol*K)'),
        H298 = (45.67,'kcal/mol'),
        S298 = (34.13,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""

""",
)

entry(
    index = 86,
    label = "Cdd-CddSd",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cdd u0 {1,D}
3   S2d u0 {1,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 87,
    label = "Cdd-(Cdd-S2d)S2d",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cdd u0 {1,D} {4,D}
3   S2d u0 {1,D}
4   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 88,
    label = "Cdd-(Cdd-Cd)S2d",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cdd u0 {1,D} {4,D}
3   S2d u0 {1,D}
4   C   u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 89,
    label = "Cdd-CdCd",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   C   u0 {1,D}
3   C   u0 {1,D}
""",
    thermo = 'Cdd-CdsCds',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 90,
    label = "Cdd-CddCdd",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cdd u0 {1,D}
3   Cdd u0 {1,D}
""",
    thermo = 'Cdd-(Cdd-Cd)(Cdd-Cd)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 91,
    label = "Cdd-(Cdd-O2d)(Cdd-O2d)",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cdd u0 {1,D} {4,D}
3   Cdd u0 {1,D} {5,D}
4   O2d u0 {2,D}
5   O2d u0 {3,D}
""",
    thermo = 'Cdd-CdsCds',
    shortDesc = """O=C=C*=C=O, currently not defined. Assigned same value as Ca""",
    longDesc = 
"""

""",
)

entry(
    index = 92,
    label = "Cdd-(Cdd-S2d)(Cdd-S2d)",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cdd u0 {1,D} {4,D}
3   Cdd u0 {1,D} {5,D}
4   S2d u0 {2,D}
5   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 93,
    label = "Cdd-(Cdd-O2d)(Cdd-Cd)",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cdd u0 {1,D} {4,D}
3   Cdd u0 {1,D} {5,D}
4   O2d u0 {2,D}
5   C   u0 {3,D}
""",
    thermo = 'Cdd-(Cdd-O2d)Cds',
    shortDesc = """O=C=C*=C=C, currently not defined. Assigned same value as Ca""",
    longDesc = 
"""

""",
)

entry(
    index = 94,
    label = "Cdd-(Cdd-S2d)(Cdd-Cd)",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cdd u0 {1,D} {4,D}
3   Cdd u0 {1,D} {5,D}
4   S2d u0 {2,D}
5   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 95,
    label = "Cdd-(Cdd-Cd)(Cdd-Cd)",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cdd u0 {1,D} {4,D}
3   Cdd u0 {1,D} {5,D}
4   C   u0 {2,D}
5   C   u0 {3,D}
""",
    thermo = 'Cdd-CdsCds',
    shortDesc = """C=C=C*=C=C, currently not defined. Assigned same value as Ca""",
    longDesc = 
"""

""",
)

entry(
    index = 96,
    label = "Cdd-CddCds",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cdd u0 {1,D}
3   Cd  u0 {1,D}
""",
    thermo = 'Cdd-(Cdd-Cd)(Cdd-Cd)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 97,
    label = "Cdd-(Cdd-O2d)Cds",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cdd u0 {1,D} {4,D}
3   Cd  u0 {1,D}
4   O2d u0 {2,D}
""",
    thermo = 'Cdd-CdsCds',
    shortDesc = """O=C=C*=C<, currently not defined. Assigned same value as Ca""",
    longDesc = 
"""

""",
)

entry(
    index = 98,
    label = "Cdd-(Cdd-S2d)Cds",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cdd u0 {1,D} {4,D}
3   Cd  u0 {1,D}
4   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 99,
    label = "Cdd-(Cdd-Cd)Cds",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cdd u0 {1,D} {4,D}
3   Cd  u0 {1,D}
4   C   u0 {2,D}
""",
    thermo = 'Cdd-CdsCds',
    shortDesc = """C=C=C*=C<, currently not defined. Assigned same value as Ca""",
    longDesc = 
"""

""",
)

entry(
    index = 100,
    label = "Cdd-CdsCds",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cd  u0 {1,D}
3   Cd  u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.9,4.4,4.7,5,5.3,5.5,5.7],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (34.2,'kcal/mol','+|-',0.2),
        S298 = (6,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = """Benson's Ca""",
    longDesc = 
"""

""",
)

entry(
    index = 101,
    label = "Cds",
    group = 
"""
1 * [Cd,CO,CS] u0
""",
    thermo = 'Cds-CdsCsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 102,
    label = "Cds-OdN3sH",
    group = 
"""
1 * CO  u0 {2,S} {3,S} {4,D}
2   N3s u0 {1,S}
3   H   u0 {1,S}
4   O2d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.03,7.87,8.82,9.68,11.16,12.2,14.8],'cal/(mol*K)'),
        H298 = (-29.6,'kcal/mol'),
        S298 = (34.93,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 103,
    label = "Cds-OdN3sCs",
    group = 
"""
1 * CO  u0 {2,S} {3,S} {4,D}
2   N3s u0 {1,S}
3   Cs  u0 {1,S}
4   O2d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.37,6.17,7.07,7.66,9.62,11.19,15.115],'cal/(mol*K)'),
        H298 = (-32.8,'kcal/mol'),
        S298 = (16.2,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 104,
    label = "Cd-N3dCsCs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   N3d u0 {1,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.5,4.2,5,5.6,6.6,7.2,7.9],'cal/(mol*K)','+|-',[0.9,0.9,0.9,0.9,0.9,0.9,0.9]),
        H298 = (5.7,'kcal/mol','+|-',1.2),
        S298 = (2,'cal/(mol*K)','+|-',1.1),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 105,
    label = "Cd-N3dCsH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   N3d u0 {1,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.5,6.3,7.2,8,9.3,10.2,11.6],'cal/(mol*K)','+|-',[0.9,0.9,0.9,0.9,0.9,0.9,0.9]),
        H298 = (3.3,'kcal/mol','+|-',1.3),
        S298 = (21.2,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 106,
    label = "Cd-N3dHH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   N3d u0 {1,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.2,7.4,8.7,9.8,11.5,12.9,15],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (4.4,'kcal/mol','+|-',1.4),
        S298 = (40.8,'cal/(mol*K)','+|-',1.3),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 107,
    label = "Cds-OdHH",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.47,9.38,10.46,11.52,13.37,14.81,14.81],'cal/(mol*K)','+|-',[0.06,0.06,0.06,0.06,0.06,0.06,0.06]),
        H298 = (-25.95,'kcal/mol','+|-',0.11),
        S298 = (53.68,'cal/(mol*K)','+|-',0.06),
    ),
    shortDesc = """CO-HH BENSON !!!WARNING! Cp1500 value taken as Cp1000, S(group) = S(CH2O) + Rln(2)""",
    longDesc = 
"""

""",
)

entry(
    index = 108,
    label = "Cds-OdOsH",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   O2s u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.88,34.56,42.08,48.16,56.57,61.38,65.84],'J/(mol*K)','+|-',[4.01,4.01,4.01,4.01,4.01,4.01,4.01]),
        H298 = (-211.8,'kJ/mol','+|-',3.42),
        S298 = (124.04,'J/(mol*K)','+|-',4.68),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 109,
    label = "CO-SH",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   S   u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = 'CO-S2H',
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc = 
"""
"
""",
)

entry(
    index = 110,
    label = "CO-S2H",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   S2s u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.27,9.88,10.36,10.77,12.65,14.02,14.06],'cal/(mol*K)'),
        H298 = (-15.2,'kcal/mol'),
        S298 = (41.26,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 111,
    label = "CO-S4H",
    group = 
"""
1 * CO                u0 {2,D} {3,S} {4,S}
2   O2d               u0 {1,D}
3   [S4s,S4d,S4b,S4t] u0 {1,S}
4   H                 u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.51,9.3,9.66,10.35,13.15,14.94,15.19],'cal/(mol*K)'),
        H298 = (-8.53,'kcal/mol'),
        S298 = (39.05,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 112,
    label = "CO-S6H",
    group = 
"""
1 * CO                      u0 {2,D} {3,S} {4,S}
2   O2d                     u0 {1,D}
3   [S6s,S6d,S6dd,S6t,S6td] u0 {1,S}
4   H                       u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.08,7.22,8.24,9.21,11.83,13.5,14.27],'cal/(mol*K)'),
        H298 = (-8.01,'kcal/mol'),
        S298 = (48.01,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 113,
    label = "Cds-OdOsOs",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.17,39.3,48.25,53.88,58.97,59.63,56.09],'J/(mol*K)','+|-',[6,6,6,6,6,6,6]),
        H298 = (-281.4,'kJ/mol','+|-',5.11),
        S298 = (22.66,'J/(mol*K)','+|-',7),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 114,
    label = "CO-CsSs",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   S2s u0 {1,S}
4   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.12,8.65,9.04,9.38,11.01,11.97,10.97],'cal/(mol*K)'),
        H298 = (-19.07,'kcal/mol'),
        S298 = (20.3,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 115,
    label = "CO-OsSs",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   O2s u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.87,9.51,10.75,11.62,13.62,14.53,12.86],'cal/(mol*K)'),
        H298 = (-35.59,'kcal/mol'),
        S298 = (16.37,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""

""",
)

entry(
    index = 116,
    label = "Cds-OdCH",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   C   u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = 'Cds-OdCsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 117,
    label = "Cds-OdCsH",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.24,31.22,35.94,40.13,46.74,51.39,57.73],'J/(mol*K)','+|-',[2.08,2.08,2.08,2.08,2.08,2.08,2.08]),
        H298 = (-123.4,'kJ/mol','+|-',1.77),
        S298 = (145.46,'J/(mol*K)','+|-',2.42),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 118,
    label = "Cds-OdCdsH",
    group = 
"""
1 * CO      u0 {2,D} {3,S} {4,S}
2   O2d     u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   H       u0 {1,S}
""",
    thermo = 'Cds-O2d(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 119,
    label = "Cds-O2d(Cds-O2d)H",
    group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   CO  u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   H   u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.76,34.63,39.25,43.32,49.57,53.77,59.32],'J/(mol*K)','+|-',[1.7,1.7,1.7,1.7,1.7,1.7,1.7]),
        H298 = (-104.8,'kJ/mol','+|-',1.45),
        S298 = (140.49,'J/(mol*K)','+|-',1.98),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 120,
    label = "Cds-O2d(Cds-Cd)H",
    group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   H   u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.31,34,39.42,43.77,50.16,54.55,60.77],'J/(mol*K)','+|-',[4.9,4.9,4.9,4.9,4.9,4.9,4.9]),
        H298 = (-128.3,'kJ/mol','+|-',5.9),
        S298 = (129.26,'J/(mol*K)','+|-',5.71),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 121,
    label = "Cds-O2d(Cds-Cds)H",
    group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   H   u0 {1,S}
5   Cd  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.45,8.77,9.82,10.7,12.14,12.9,12.9],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (-30.9,'kcal/mol','+|-',0.3),
        S298 = (33.4,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = """CO-CdH Hf BOZZELLI S,Cp =3D CO/C/H-del(cd syst) !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
"""

""",
)

entry(
    index = 122,
    label = "Cds-O2d(Cds-Cdd)H",
    group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   H   u0 {1,S}
5   Cdd u0 {2,D}
""",
    thermo = 'Cds-O2d(Cds-Cdd-Cd)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 123,
    label = "Cds-O2d(Cds-Cdd-O2d)H",
    group = 
"""
1 * CO  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   O2d u0 {1,D}
5   H   u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = 'Cds-O2d(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 124,
    label = "Cds-O2d(Cds-Cdd-Cd)H",
    group = 
"""
1 * CO  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   O2d u0 {1,D}
5   H   u0 {1,S}
6   C   u0 {3,D}
""",
    thermo = 'Cds-O2d(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 125,
    label = "Cds-OdCtH",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Ct  u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = 'Cds-O2d(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 126,
    label = "Cds-OdCbH",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = 'Cds-O2d(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 127,
    label = "Cds-OdCOs",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   C   u0 {1,S}
4   O2s u0 {1,S}
""",
    thermo = 'Cds-OdCsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 128,
    label = "Cds-OdCsOs",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cs  u0 {1,S}
4   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.67,28.39,34.6,39.48,46.23,50.09,52.68],'J/(mol*K)','+|-',[2.85,2.85,2.85,2.85,2.85,2.85,2.85]),
        H298 = (-222,'kJ/mol','+|-',2.43),
        S298 = (43.52,'J/(mol*K)','+|-',3.33),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 129,
    label = "Cds-OdCdsOs",
    group = 
"""
1 * CO      u0 {2,D} {3,S} {4,S}
2   O2d     u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   O2s     u0 {1,S}
""",
    thermo = 'Cds-O2d(Cds-Cds)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 130,
    label = "Cds-O2d(Cds-O2d)O2s",
    group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   CO  u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   O2s u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.18,34.34,39.85,44.13,49.81,52.4,52.33],'J/(mol*K)','+|-',[3.36,3.36,3.36,3.36,3.36,3.36,3.36]),
        H298 = (-196.2,'kJ/mol','+|-',2.86),
        S298 = (39.37,'J/(mol*K)','+|-',3.92),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 131,
    label = "Cds-O2d(Cds-Cd)O2s",
    group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   O2s u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.33,37.84,44.54,49.34,55.45,58.73,60.61],'J/(mol*K)','+|-',[7.46,7.46,7.46,7.46,7.46,7.46,7.46]),
        H298 = (-218.6,'kJ/mol','+|-',6.36),
        S298 = (33.44,'J/(mol*K)','+|-',8.7),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 132,
    label = "Cds-O2d(Cds-Cds)O2s",
    group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   O2s u0 {1,S}
5   Cd  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.97,6.7,7.4,8.02,8.87,9.36,9.36],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (-32.1,'kcal/mol','+|-',0.3),
        S298 = (14.78,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = """CO-OCd RPS + S Coreected !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
"""

""",
)

entry(
    index = 133,
    label = "Cds-O2d(Cds-Cdd)O2s",
    group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   O2s u0 {1,S}
5   Cdd u0 {2,D}
""",
    thermo = 'Cds-O2d(Cds-Cdd-Cd)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 134,
    label = "Cds-O2d(Cds-Cdd-O2d)O2s",
    group = 
"""
1 * CO  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   O2d u0 {1,D}
5   O2s u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = 'Cds-O2d(Cds-Cds)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 135,
    label = "Cds-O2d(Cds-Cdd-Cd)O2s",
    group = 
"""
1 * CO  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   O2d u0 {1,D}
5   O2s u0 {1,S}
6   C   u0 {3,D}
""",
    thermo = 'Cds-O2d(Cds-Cds)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 136,
    label = "Cds-OdCtOs",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Ct  u0 {1,S}
4   O2s u0 {1,S}
""",
    thermo = 'Cds-O2d(Cds-Cds)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 137,
    label = "Cds-OdCbOs",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cb  u0 {1,S}
4   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.97,6.7,7.4,8.02,8.87,9.36,9.36],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (-36.6,'kcal/mol','+|-',0.3),
        S298 = (14.78,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = """CO-OCb RPS + S Coreected !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
"""

""",
)

entry(
    index = 138,
    label = "Cds-OdCC",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   C   u0 {1,S}
4   C   u0 {1,S}
""",
    thermo = 'Cds-OdCsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 139,
    label = "Cds-OdCsCs",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.82,27.7,31.22,34.19,38.37,40.85,43.26],'J/(mol*K)','+|-',[2.08,2.08,2.08,2.08,2.08,2.08,2.08]),
        H298 = (-132.2,'kJ/mol','+|-',1.77),
        S298 = (61.78,'J/(mol*K)','+|-',2.42),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 140,
    label = "Cds-OdCdsCs",
    group = 
"""
1 * CO      u0 {2,D} {3,S} {4,S}
2   O2d     u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
""",
    thermo = 'Cds-O2d(Cds-Cds)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 141,
    label = "Cds-O2d(Cds-O2d)Cs",
    group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   CO  u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   Cs  u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.77,30.83,34.36,37.27,41.27,43.45,45.25],'J/(mol*K)','+|-',[1.28,1.28,1.28,1.28,1.28,1.28,1.28]),
        H298 = (-122,'kJ/mol','+|-',1.09),
        S298 = (57.8,'J/(mol*K)','+|-',1.5),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 142,
    label = "Cds-O2d(Cds-Cd)Cs",
    group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   Cs  u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.26,30.66,34.68,37.69,41.62,43.93,46.69],'J/(mol*K)','+|-',[4.9,4.9,4.9,4.9,4.9,4.9,4.9]),
        H298 = (-130.4,'kJ/mol','+|-',4.17),
        S298 = (47.38,'J/(mol*K)','+|-',5.71),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 143,
    label = "Cds-O2d(Cds-Cds)Cs",
    group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   Cs  u0 {1,S}
5   Cd  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.46,6.32,7.17,7.88,9,9.77,9.77],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (-30.9,'kcal/mol','+|-',0.3),
        S298 = (14.6,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = """CO-CdCs Hf BENSON =3D CO/Cb/C S,Cp !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
"""

""",
)

entry(
    index = 144,
    label = "Cds-O2d(Cds-Cdd)Cs",
    group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   Cs  u0 {1,S}
5   Cdd u0 {2,D}
""",
    thermo = 'Cds-O2d(Cds-Cdd-Cd)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 145,
    label = "Cds-O2d(Cds-Cdd-O2d)Cs",
    group = 
"""
1 * CO  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   O2d u0 {1,D}
5   Cs  u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = 'Cds-O2d(Cds-Cds)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 146,
    label = "Cds-O2d(Cds-Cdd-Cd)Cs",
    group = 
"""
1 * CO  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   O2d u0 {1,D}
5   Cs  u0 {1,S}
6   C   u0 {3,D}
""",
    thermo = 'Cds-O2d(Cds-Cds)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 147,
    label = "Cds-OdCdsCds",
    group = 
"""
1 * CO      u0 {2,D} {3,S} {4,S}
2   O2d     u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
""",
    thermo = 'Cds-O2d(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 148,
    label = "Cds-O2d(Cds-O2d)(Cds-O2d)",
    group = 
"""
1 * CO  u0 {2,S} {3,S} {4,D}
2   CO  u0 {1,S} {5,D}
3   CO  u0 {1,S} {6,D}
4   O2d u0 {1,D}
5   O2d u0 {2,D}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([31.75,33.35,34.1,34.51,35.19,36.06,38.14],'J/(mol*K)','+|-',[2.41,2.41,2.41,2.41,2.41,2.41,2.41]),
        H298 = (-89.3,'kJ/mol','+|-',2.05),
        S298 = (64.51,'J/(mol*K)','+|-',2.81),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 149,
    label = "Cds-O2d(Cds-Cd)(Cds-O2d)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   CO  u0 {1,S} {6,D}
5   C   u0 {3,D}
6   O2d u0 {4,D}
""",
    thermo = 'Cds-O2d(Cds-Cds)(Cds-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 150,
    label = "Cds-O2d(Cds-Cds)(Cds-O2d)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   CO  u0 {1,S} {6,D}
5   Cd  u0 {3,D}
6   O2d u0 {4,D}
""",
    thermo = 'Cds-O2d(Cds-O2d)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 151,
    label = "Cds-O2d(Cds-Cdd)(Cds-O2d)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   CO  u0 {1,S} {6,D}
5   Cdd u0 {3,D}
6   O2d u0 {4,D}
""",
    thermo = 'Cds-O2d(Cds-Cdd-Cd)(Cds-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 152,
    label = "Cds-O2d(Cds-Cdd-O2d)(Cds-O2d)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   CO  u0 {1,S} {7,D}
5   Cdd u0 {3,D} {6,D}
6   O2d u0 {5,D}
7   O2d u0 {4,D}
""",
    thermo = 'Cds-O2d(Cds-Cdd-O2d)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 153,
    label = "Cds-O2d(Cds-Cdd-Cd)(Cds-O2d)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   CO  u0 {1,S} {7,D}
5   Cdd u0 {3,D} {6,D}
6   C   u0 {5,D}
7   O2d u0 {4,D}
""",
    thermo = 'Cds-O2d(Cds-Cds)(Cds-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 154,
    label = "Cds-O2d(Cds-Cd)(Cds-Cd)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   Cd  u0 {1,S} {6,D}
5   C   u0 {3,D}
6   C   u0 {4,D}
""",
    thermo = 'Cds-O2d(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 155,
    label = "Cds-O2d(Cds-Cds)(Cds-Cds)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   Cd  u0 {1,S} {6,D}
5   Cd  u0 {3,D}
6   Cd  u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.46,6.32,7.17,7.88,9,9.77,9.77],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (-30.9,'kcal/mol','+|-',0.3),
        S298 = (14.6,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = """CO-CdCd Estimate BOZZELLI !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
"""

""",
)

entry(
    index = 156,
    label = "Cds-O2d(Cds-Cdd)(Cds-Cds)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   Cd  u0 {1,S} {6,D}
5   Cdd u0 {3,D}
6   Cd  u0 {4,D}
""",
    thermo = 'Cds-O2d(Cds-Cdd-Cd)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 157,
    label = "Cds-O2d(Cds-Cdd-O2d)(Cds-Cds)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   Cd  u0 {1,S} {6,D}
5   Cdd u0 {3,D} {7,D}
6   Cd  u0 {4,D}
7   O2d u0 {5,D}
""",
    thermo = 'Cds-O2d(Cds-Cdd-O2d)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 158,
    label = "Cds-O2d(Cds-Cdd-Cd)(Cds-Cds)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   Cd  u0 {1,S} {6,D}
5   Cdd u0 {3,D} {7,D}
6   Cd  u0 {4,D}
7   C   u0 {5,D}
""",
    thermo = 'Cds-O2d(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 159,
    label = "Cds-O2d(Cds-Cdd)(Cds-Cdd)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   Cd  u0 {1,S} {6,D}
5   Cdd u0 {3,D}
6   Cdd u0 {4,D}
""",
    thermo = 'Cds-O2d(Cds-Cdd-Cd)(Cds-Cdd-Cd)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 160,
    label = "Cds-O2d(Cds-Cdd-O2d)(Cds-Cdd-O2d)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   Cd  u0 {1,S} {6,D}
5   Cdd u0 {3,D} {7,D}
6   Cdd u0 {4,D} {8,D}
7   O2d u0 {5,D}
8   O2d u0 {6,D}
""",
    thermo = 'Cds-O2d(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 161,
    label = "Cds-O2d(Cds-Cdd-Cd)(Cds-Cdd-O2d)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   Cd  u0 {1,S} {6,D}
5   Cdd u0 {3,D} {7,D}
6   Cdd u0 {4,D} {8,D}
7   C   u0 {5,D}
8   O2d u0 {6,D}
""",
    thermo = 'Cds-O2d(Cds-Cdd-O2d)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 162,
    label = "Cds-O2d(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   Cd  u0 {1,S} {6,D}
5   Cdd u0 {3,D} {7,D}
6   Cdd u0 {4,D} {8,D}
7   C   u0 {5,D}
8   C   u0 {6,D}
""",
    thermo = 'Cds-O2d(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 163,
    label = "Cds-OdCtCs",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Ct  u0 {1,S}
4   Cs  u0 {1,S}
""",
    thermo = 'Cds-O2d(Cds-Cds)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 164,
    label = "Cds-OdCtCds",
    group = 
"""
1 * CO      u0 {2,D} {3,S} {4,S}
2   O2d     u0 {1,D}
3   Ct      u0 {1,S}
4   [Cd,CO] u0 {1,S}
""",
    thermo = 'Cds-OdCt(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 165,
    label = "Cds-OdCt(Cds-O2d)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Ct  u0 {1,S}
4   CO  u0 {1,S} {5,D}
5   O2d u0 {4,D}
""",
    thermo = 'Cds-O2d(Cds-Cds)(Cds-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 166,
    label = "Cds-OdCt(Cds-Cd)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Ct  u0 {1,S}
4   Cd  u0 {1,S} {5,D}
5   C   u0 {4,D}
""",
    thermo = 'Cds-OdCt(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 167,
    label = "Cds-OdCt(Cds-Cds)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Ct  u0 {1,S}
4   Cd  u0 {1,S} {5,D}
5   Cd  u0 {4,D}
""",
    thermo = 'Cds-O2d(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 168,
    label = "Cds-OdCt(Cds-Cdd)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Ct  u0 {1,S}
4   Cd  u0 {1,S} {5,D}
5   Cdd u0 {4,D}
""",
    thermo = 'Cds-OdCt(Cds-Cdd-Cd)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 169,
    label = "Cds-OdCt(Cds-Cdd-O2d)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Ct  u0 {1,S}
4   Cd  u0 {1,S} {5,D}
5   Cdd u0 {4,D} {6,D}
6   O2d u0 {5,D}
""",
    thermo = 'Cds-O2d(Cds-Cdd-O2d)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 170,
    label = "Cds-OdCt(Cds-Cdd-Cd)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Ct  u0 {1,S}
4   Cd  u0 {1,S} {5,D}
5   Cdd u0 {4,D} {6,D}
6   C   u0 {5,D}
""",
    thermo = 'Cds-OdCt(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 171,
    label = "Cds-OdCtCt",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Ct  u0 {1,S}
4   Ct  u0 {1,S}
""",
    thermo = 'Cds-O2d(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 172,
    label = "Cds-OdCbCs",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cb  u0 {1,S}
4   Cs  u0 {1,S}
""",
    thermo = 'Cds-O2d(Cds-Cds)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 173,
    label = "Cds-OdCbCds",
    group = 
"""
1 * CO      u0 {2,D} {3,S} {4,S}
2   O2d     u0 {1,D}
3   Cb      u0 {1,S}
4   [Cd,CO] u0 {1,S}
""",
    thermo = 'Cds-OdCb(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 174,
    label = "Cds-OdCb(Cds-O2d)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cb  u0 {1,S}
4   CO  u0 {1,S} {5,D}
5   O2d u0 {4,D}
""",
    thermo = 'Cds-O2d(Cds-Cds)(Cds-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 175,
    label = "Cds-OdCb(Cds-Cd)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cb  u0 {1,S}
4   Cd  u0 {1,S} {5,D}
5   C   u0 {4,D}
""",
    thermo = 'Cds-OdCb(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 176,
    label = "Cds-OdCb(Cds-Cds)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cb  u0 {1,S}
4   Cd  u0 {1,S} {5,D}
5   Cd  u0 {4,D}
""",
    thermo = 'Cds-O2d(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 177,
    label = "Cds-OdCb(Cds-Cdd)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cb  u0 {1,S}
4   Cd  u0 {1,S} {5,D}
5   Cdd u0 {4,D}
""",
    thermo = 'Cds-OdCb(Cds-Cdd-Cd)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 178,
    label = "Cds-OdCb(Cds-Cdd-O2d)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cb  u0 {1,S}
4   Cd  u0 {1,S} {5,D}
5   Cdd u0 {4,D} {6,D}
6   O2d u0 {5,D}
""",
    thermo = 'Cds-O2d(Cds-Cdd-O2d)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 179,
    label = "Cds-OdCb(Cds-Cdd-Cd)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cb  u0 {1,S}
4   Cd  u0 {1,S} {5,D}
5   Cdd u0 {4,D} {6,D}
6   C   u0 {5,D}
""",
    thermo = 'Cds-OdCb(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 180,
    label = "Cds-OdCbCt",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cb  u0 {1,S}
4   Ct  u0 {1,S}
""",
    thermo = 'Cds-OdCt(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 181,
    label = "Cds-OdCbCb",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
""",
    thermo = 'Cds-O2d(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 182,
    label = "Cds-CdHH",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = 'Cds-CdsHH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 183,
    label = "Cds-CdsHH",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.1,6.36,7.51,8.5,10.07,11.27,13.19],'cal/(mol*K)','+|-',[0.07,0.07,0.07,0.07,0.07,0.07,0.07]),
        H298 = (6.26,'kcal/mol','+|-',0.19),
        S298 = (27.61,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = """Cd-HH BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 184,
    label = "Cds-CddHH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = 'Cds-(Cdd-Cd)HH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 185,
    label = "Cds-(Cdd-O2d)HH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.08,13.91,15.4,16.64,18.61,20.1,22.47],'cal/(mol*K)','+|-',[0.07,0.07,0.07,0.07,0.07,0.07,0.07]),
        H298 = (-11.34,'kcal/mol','+|-',0.19),
        S298 = (57.47,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = """{CCO/H2} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
"""

""",
)

entry(
    index = 186,
    label = "Cds-(Cdd-S2d)HH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 187,
    label = "Cds-(Cdd-Cd)HH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = 'Cds-CdsHH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 188,
    label = "Cds-CdOsH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   C   u0 {1,D}
3   O2s u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.08,21.17,24.43,27.41,32.22,35.73,40.97],'J/(mol*K)'),
        H298 = (36.4,'kJ/mol'),
        S298 = (33.51,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 189,
    label = "Cds-CdsOsH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cd  u0 {1,D}
3   O2s u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.75,6.46,7.64,8.35,9.1,9.56,10.46],'cal/(mol*K)','+|-',[0.07,0.07,0.07,0.07,0.07,0.07,0.07]),
        H298 = (2.03,'kcal/mol','+|-',0.19),
        S298 = (6.2,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = """Cd-OH BOZZELLI Hf vin-oh RADOM + C/Cd/H, S&Cp LAY""",
    longDesc = 
"""

""",
)

entry(
    index = 190,
    label = "Cds-CddOsH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   O2s u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = 'Cds-(Cdd-Cd)OsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 191,
    label = "Cds-(Cdd-O2d)OsH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   O2s u0 {1,S}
4   H   u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.29,13.67,15.1,16.1,17.36,18.25,19.75],'cal/(mol*K)','+|-',[0.07,0.07,0.07,0.07,0.07,0.07,0.07]),
        H298 = (2.11,'kcal/mol','+|-',0.19),
        S298 = (38.17,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = """{CCO/O/H} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
"""

""",
)

entry(
    index = 192,
    label = "Cds-(Cdd-Cd)OsH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   O2s u0 {1,S}
4   H   u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = 'Cds-CdsOsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 193,
    label = "Cds-CdSH",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   S  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = 'Cds-CdsSH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 194,
    label = "Cds-CdsSH",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   S  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = 'Cds-CdsS4H',
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc = 
"""
"
""",
)

entry(
    index = 195,
    label = "Cds-CdsS2H",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cd  u0 {1,D}
3   S2s u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.72,6.61,6.84,7.2,9.2,10.44,9.73],'cal/(mol*K)'),
        H298 = (18.92,'kcal/mol'),
        S298 = (12.2,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 196,
    label = "Cds-CdsS4H",
    group = 
"""
1 * Cd                u0 {2,D} {3,S} {4,S}
2   Cd                u0 {1,D}
3   [S4s,S4d,S4b,S4t] u0 {1,S}
4   H                 u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.22,7.89,7.54,8.28,10.6,11.9,10.95],'cal/(mol*K)'),
        H298 = (27.56,'kcal/mol'),
        S298 = (5.06,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 197,
    label = "Cds-CdsS6H",
    group = 
"""
1 * Cd                      u0 {2,D} {3,S} {4,S}
2   Cd                      u0 {1,D}
3   [S6s,S6d,S6dd,S6t,S6td] u0 {1,S}
4   H                       u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.03,5.53,6.45,7.26,9.65,11,10.77],'cal/(mol*K)'),
        H298 = (19.86,'kcal/mol'),
        S298 = (13.58,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 198,
    label = "Cds-CddSsH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   S2s u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 199,
    label = "Cds-(Cdd-S2d)SsH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   S2s u0 {1,S}
4   H   u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 200,
    label = "Cds-(Cdd-Cd)SsH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   S2s u0 {1,S}
4   H   u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 201,
    label = "Cds-CdOsOs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   C   u0 {1,D}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.34,11.93,14.86,17.95,22.31,24.6,26.92],'J/(mol*K)','+|-',[7.4,7.4,7.4,7.4,7.4,7.4,7.4]),
        H298 = (28.3,'kJ/mol','+|-',6.3),
        S298 = (-42.69,'J/(mol*K)','+|-',8.63),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 202,
    label = "Cds-CdsOsOs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cd  u0 {1,D}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
""",
    thermo = 'Cds-CdsCsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 203,
    label = "Cds-CddOsOs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
""",
    thermo = 'Cds-(Cdd-Cd)OsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 204,
    label = "Cds-(Cdd-O2d)OsOs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.56,15.58,17.69,18.67,18.78,18.4,18.01],'cal/(mol*K)','+|-',[0.07,0.07,0.07,0.07,0.07,0.07,0.07]),
        H298 = (2.403,'kcal/mol','+|-',0.19),
        S298 = (13.42,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = """{CCO/O2} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
"""

""",
)

entry(
    index = 205,
    label = "Cds-(Cdd-Cd)OsOs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = 'Cds-CdsOsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 206,
    label = "Cds-CdSsSs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   C   u0 {1,D}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 207,
    label = "Cds-CdsSsSs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cd  u0 {1,D}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 208,
    label = "Cds-CddSsSs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 209,
    label = "Cds-(Cdd-S2d)SsSs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 210,
    label = "Cds-(Cdd-Cd)SsSs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 211,
    label = "Cds-CdCH",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   C  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = 'Cds-CdsCsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 212,
    label = "Cds-CdsCsH",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cs u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.16,5.03,5.81,6.5,7.65,8.45,9.62],'cal/(mol*K)','+|-',[0.06,0.06,0.06,0.06,0.06,0.06,0.06]),
        H298 = (8.59,'kcal/mol','+|-',0.17),
        S298 = (7.97,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = """Cd-CsH BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 213,
    label = "Cds-CdsCdsH",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cd      u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   H       u0 {1,S}
""",
    thermo = 'Cds-Cds(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 214,
    label = "Cd-Cd(CO)H",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   CO  u0 {1,S} {5,D}
3   H   u0 {1,S}
4   Cd  u0 {1,D}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.08,21.17,24.43,27.41,32.22,35.73,40.97],'J/(mol*K)'),
        H298 = (36.4,'kJ/mol'),
        S298 = (33.51,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 215,
    label = "Cds-Cds(Cds-Cd)H",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   H  u0 {1,S}
5   C  u0 {2,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 216,
    label = "Cds-Cds(Cds-Cds)H",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   H  u0 {1,S}
5   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.46,5.79,6.75,7.42,8.35,8.99,9.98],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (6.78,'kcal/mol','+|-',0.2),
        S298 = (6.38,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = """Cd-CdH BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 217,
    label = "Cds-Cds(Cds-Cdd)H",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,D}
4   H   u0 {1,S}
5   Cdd u0 {2,D}
""",
    thermo = 'Cds-Cds(Cds-Cdd-Cd)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 218,
    label = "Cd-Cd(CCO)H",
    group = 
"""
1 * Cd  u0 {2,S} {4,S} {5,D}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   H   u0 {1,S}
5   Cd  u0 {1,D}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.08,21.17,24.43,27.41,32.22,35.73,40.97],'J/(mol*K)'),
        H298 = (36.4,'kJ/mol'),
        S298 = (33.51,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 219,
    label = "Cds-Cds(Cds-Cdd-S2d)H",
    group = 
"""
1 * Cd  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   Cd  u0 {1,D}
5   H   u0 {1,S}
6   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 220,
    label = "Cds-Cds(Cds-Cdd-Cd)H",
    group = 
"""
1 * Cd  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   Cd  u0 {1,D}
5   H   u0 {1,S}
6   C   u0 {3,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 221,
    label = "Cds-CdsCtH",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Ct u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.46,5.79,6.75,7.42,8.35,8.99,9.98],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (6.78,'kcal/mol','+|-',0.2),
        S298 = (6.38,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = """Cd-CtH BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 222,
    label = "Cds-CdsH(CtN3t)",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Ct  u0 {1,S} {5,T}
3   Cd  u0 {1,D}
4   H   u0 {1,S}
5   N3t u0 {2,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.3,12,13.4,14.6,16.3,17.5,19.4],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (38.5,'kcal/mol','+|-',1.3),
        S298 = (37.6,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 223,
    label = "Cds-CdsCbH",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cb u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.46,5.79,6.75,7.42,8.35,8.99,9.98],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (6.78,'kcal/mol','+|-',0.2),
        S298 = (6.38,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = """Cd-CbH BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 224,
    label = "Cds-(Cds-Os)CbH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cd  u0 {1,D} {5,S}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
5   O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.28,6.83,7.245,7.264,8.226,9.901,10.176],'cal/(mol*K)'),
        H298 = (10.329,'kcal/mol'),
        S298 = (2.958,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3""",
    longDesc = 
"""
Fitted to CBS-QB3 calculations for OC=Cc1ccccc1
""",
)

entry(
    index = 225,
    label = "Cds-CddCsH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = 'Cds-(Cdd-Cd)CsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 226,
    label = "Cds-(Cdd-O2d)CsH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([43.83,50.1,55.5,60.05,67.09,72.13,79.55],'J/(mol*K)','+|-',[4,4,4,4,4,4,4]),
        H298 = (-17.6,'kJ/mol','+|-',3.41),
        S298 = (169.15,'J/(mol*K)','+|-',4.67),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 227,
    label = "Cds-(Cdd-S2d)CsH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 228,
    label = "Cds-(Cdd-Cd)CsH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = 'Cds-CdsCsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 229,
    label = "Cds-CddCdsH",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cdd     u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   H       u0 {1,S}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 230,
    label = "Cds-(Cdd-O2d)(Cds-O2d)H",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CO  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   O2d u0 {2,D}
6   O2d u0 {3,D}
""",
    thermo = 'Cds-(Cdd-O2d)CsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 231,
    label = "Cds-(Cdd-O2d)(Cds-Cd)H",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   O2d u0 {2,D}
6   C   u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([43.67,52.95,59.65,64.67,71.81,76.72,83.92],'J/(mol*K)','+|-',[5.66,5.66,5.66,5.66,5.66,5.66,5.66]),
        H298 = (-36,'kJ/mol','+|-',4.82),
        S298 = (152.19,'J/(mol*K)','+|-',6.6),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 232,
    label = "Cds-(Cdd-O2d)(Cds-Cds)H",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   O2d u0 {2,D}
6   Cd  u0 {3,D}
""",
    thermo = 'Cds-(Cdd-O2d)CsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 233,
    label = "Cds-(Cdd-O2d)(Cds-Cdd)H",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   O2d u0 {2,D}
6   Cdd u0 {3,D}
""",
    thermo = 'Cds-(Cdd-O2d)(Cds-Cdd-Cd)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 234,
    label = "Cds-(Cdd-O2d)(Cds-Cdd-O2d)H",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   H   u0 {1,S}
6   O2d u0 {3,D}
7   O2d u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.55,12.41,13.82,14.91,16.51,17.62,19.24],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-4.998,'kcal/mol','+|-',0.2),
        S298 = (39.06,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = """{CCO/H/CCO} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
"""

""",
)

entry(
    index = 235,
    label = "Cds-(Cdd-O2d)(Cds-Cdd-Cd)H",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   H   u0 {1,S}
6   O2d u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = 'Cds-(Cdd-O2d)(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 236,
    label = "Cds-(Cdd-S2d)(Cds-Cd)H",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   S2d u0 {2,D}
6   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 237,
    label = "Cds-(Cdd-S2d)(Cds-Cds)H",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   S2d u0 {2,D}
6   Cd  u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 238,
    label = "Cds-(Cdd-S2d)(Cds-Cdd)H",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   S2d u0 {2,D}
6   Cdd u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 239,
    label = "Cds-(Cdd-S2d)(Cds-Cdd-S2d)H",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   H   u0 {1,S}
6   S2d u0 {3,D}
7   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 240,
    label = "Cds-(Cdd-S2d)(Cds-Cdd-Cd)H",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   H   u0 {1,S}
6   S2d u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 241,
    label = "Cds-(Cdd-Cd)(Cds-O2d)H",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CO  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   C   u0 {2,D}
6   O2d u0 {3,D}
""",
    thermo = 'Cd-Cd(CO)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 242,
    label = "Cds-(Cdd-Cd)(Cds-Cd)H",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   C   u0 {2,D}
6   C   u0 {3,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 243,
    label = "Cds-(Cdd-Cd)(Cds-Cds)H",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   C   u0 {2,D}
6   Cd  u0 {3,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 244,
    label = "Cds-(Cdd-Cd)(Cds-Cdd)H",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   C   u0 {2,D}
6   Cdd u0 {3,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cdd-Cd)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 245,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-O2d)H",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   H   u0 {1,S}
6   C   u0 {3,D}
7   O2d u0 {4,D}
""",
    thermo = 'Cd-Cd(CCO)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 246,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-S2d)H",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   H   u0 {1,S}
6   C   u0 {3,D}
7   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 247,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-Cd)H",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   H   u0 {1,S}
6   C   u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 248,
    label = "Cds-CddCtH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   Ct  u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = 'Cds-(Cdd-Cd)CtH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 249,
    label = "Cds-(Cdd-O2d)CtH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Ct  u0 {1,S}
4   H   u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = 'Cds-(Cdd-O2d)(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 250,
    label = "Cds-(Cdd-S2d)CtH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Ct  u0 {1,S}
4   H   u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 251,
    label = "Cds-(Cdd-Cd)CtH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Ct  u0 {1,S}
4   H   u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = 'Cds-CdsCtH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 252,
    label = "Cds-CddCbH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = 'Cds-(Cdd-Cd)CbH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 253,
    label = "Cds-(Cdd-O2d)CbH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = 'Cds-(Cdd-O2d)(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 254,
    label = "Cds-(Cdd-S2d)CbH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 255,
    label = "Cds-(Cdd-Cd)CbH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = 'Cds-CdsCbH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 256,
    label = "Cds-(Cdd-Cd)C=SH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CS  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   C   u0 {2,D}
6   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 257,
    label = "Cds-(Cdd-S2d)C=SH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CS  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   S2d u0 {2,D}
6   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 258,
    label = "Cds-CdsC=SH",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   CS  u0 {1,S} {5,D}
3   Cd  u0 {1,D}
4   H   u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.4,5.23,6.07,6.84,8.03,8.83,9.89],'cal/(mol*K)'),
        H298 = (7.8,'kcal/mol'),
        S298 = (8.3,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 259,
    label = "Cds-CdCO",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   C   u0 {1,D}
3   C   u0 {1,S}
4   O2s u0 {1,S}
""",
    thermo = 'Cds-CdsCsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 260,
    label = "Cds-CdsCdsOs",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cd      u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   O2s     u0 {1,S}
""",
    thermo = 'Cds-Cds(Cds-Cds)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 261,
    label = "Cds-Cds(Cds-O2d)O2s",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   CO  u0 {1,S} {5,D}
3   Cd  u0 {1,D}
4   O2s u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.4,5.37,5.93,6.18,6.5,6.62,6.72],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (5.13,'kcal/mol','+|-',0.2),
        S298 = (-14.6,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = """Cd-OCO adj BENSON for RADOM c*coh""",
    longDesc = 
"""

""",
)

entry(
    index = 262,
    label = "Cds-Cds(Cds-Cd)O2s",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,D}
4   O2s u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 263,
    label = "Cds-Cds(Cds-Cds)O2s",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,D}
4   O2s u0 {1,S}
5   Cd  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.4,5.37,5.93,6.18,6.5,6.62,6.72],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (1.5,'kcal/mol','+|-',0.2),
        S298 = (-14.4,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = """Cd-OCd jwb need calc""",
    longDesc = 
"""

""",
)

entry(
    index = 264,
    label = "Cds-Cds(Cds-Cdd)O2s",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,D}
4   O2s u0 {1,S}
5   Cdd u0 {2,D}
""",
    thermo = 'Cds-Cds(Cds-Cdd-Cd)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 265,
    label = "Cds-Cds(Cds-Cdd-O2d)O2s",
    group = 
"""
1 * Cd  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   Cd  u0 {1,D}
5   O2s u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 266,
    label = "Cds-Cds(Cds-Cdd-Cd)O2s",
    group = 
"""
1 * Cd  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   Cd  u0 {1,D}
5   O2s u0 {1,S}
6   C   u0 {3,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 267,
    label = "Cds-CdsCtOs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cd  u0 {1,D}
3   Ct  u0 {1,S}
4   O2s u0 {1,S}
""",
    thermo = 'Cds-Cds(Cds-Cds)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 268,
    label = "Cds-CdsCbOs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cd  u0 {1,D}
3   Cb  u0 {1,S}
4   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.4,5.37,5.93,6.18,6.5,6.62,6.72],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (1.5,'kcal/mol','+|-',0.2),
        S298 = (-14.4,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = """Cd-OCb jwb need calc""",
    longDesc = 
"""

""",
)

entry(
    index = 269,
    label = "Cds-CddCdsOs",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cdd     u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   O2s     u0 {1,S}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cds)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 270,
    label = "Cds-(Cdd-O2d)(Cds-O2d)O2s",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CO  u0 {1,S} {6,D}
4   O2s u0 {1,S}
5   O2d u0 {2,D}
6   O2d u0 {3,D}
""",
    thermo = 'Cds-(Cdd-O2d)CsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 271,
    label = "Cds-(Cdd-O2d)(Cds-Cd)O2s",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   O2s u0 {1,S}
5   O2d u0 {2,D}
6   C   u0 {3,D}
""",
    thermo = 'Cds-(Cdd-O2d)(Cds-Cds)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 272,
    label = "Cds-(Cdd-O2d)(Cds-Cds)O2s",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   O2s u0 {1,S}
5   O2d u0 {2,D}
6   Cd  u0 {3,D}
""",
    thermo = 'Cds-(Cdd-O2d)CsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 273,
    label = "Cds-(Cdd-O2d)(Cds-Cdd)O2s",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   O2s u0 {1,S}
5   O2d u0 {2,D}
6   Cdd u0 {3,D}
""",
    thermo = 'Cds-(Cdd-O2d)(Cds-Cdd-Cd)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 274,
    label = "Cds-(Cdd-O2d)(Cds-Cdd-O2d)O2s",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   O2s u0 {1,S}
6   O2d u0 {3,D}
7   O2d u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.01,12.97,14.17,14.97,15.8,16.26,16.88],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (1.607,'kcal/mol','+|-',0.2),
        S298 = (17.73,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = """{CCO/O/CCO} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
"""

""",
)

entry(
    index = 275,
    label = "Cds-(Cdd-O2d)(Cds-Cdd-Cd)O2s",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   O2s u0 {1,S}
6   O2d u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = 'Cds-(Cdd-O2d)(Cds-Cds)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 276,
    label = "Cds-(Cdd-Cd)(Cds-Cd)O2s",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   O2s u0 {1,S}
5   C   u0 {2,D}
6   C   u0 {3,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cds)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 277,
    label = "Cds-(Cdd-Cd)(Cds-Cds)O2s",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   O2s u0 {1,S}
5   C   u0 {2,D}
6   Cd  u0 {3,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 278,
    label = "Cds-(Cdd-Cd)(Cds-Cdd)O2s",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   O2s u0 {1,S}
5   C   u0 {2,D}
6   Cdd u0 {3,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cdd-Cd)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 279,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-O2d)O2s",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   O2s u0 {1,S}
6   C   u0 {3,D}
7   O2d u0 {4,D}
""",
    thermo = 'Cds-Cds(Cds-Cdd-O2d)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 280,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-Cd)O2s",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   O2s u0 {1,S}
6   C   u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cds)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 281,
    label = "Cds-CddCtOs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   Ct  u0 {1,S}
4   O2s u0 {1,S}
""",
    thermo = 'Cds-(Cdd-Cd)CtOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 282,
    label = "Cds-(Cdd-O2d)CtOs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Ct  u0 {1,S}
4   O2s u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = 'Cds-(Cdd-O2d)(Cds-Cds)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 283,
    label = "Cds-(Cdd-Cd)CtOs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Ct  u0 {1,S}
4   O2s u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = 'Cds-CdsCtOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 284,
    label = "Cds-CddCbOs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   Cb  u0 {1,S}
4   O2s u0 {1,S}
""",
    thermo = 'Cds-(Cdd-Cd)CbOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 285,
    label = "Cds-(Cdd-O2d)CbOs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cb  u0 {1,S}
4   O2s u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = 'Cds-(Cdd-O2d)(Cds-Cds)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 286,
    label = "Cds-(Cdd-Cd)CbOs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cb  u0 {1,S}
4   O2s u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = 'Cds-CdsCbOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 287,
    label = "Cd-CdCsOs",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   Cs  u0 {1,S}
3   O2s u0 {1,S}
4   C   u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.79,15.86,19.67,22.91,26.55,27.85,28.45],'J/(mol*K)','+|-',[5.1,5.1,5.1,5.1,5.1,5.1,5.1]),
        H298 = (33,'kJ/mol','+|-',4.34),
        S298 = (-50.89,'J/(mol*K)','+|-',5.94),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 288,
    label = "Cds-CdsCsOs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cd  u0 {1,D}
3   Cs  u0 {1,S}
4   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.59,4.56,5.04,5.3,5.84,6.07,6.16],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (3.03,'kcal/mol','+|-',0.2),
        S298 = (-12.32,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = """Cd-OCs BOZZELLI-RADOM vin-oh and del (ccoh-ccohc)""",
    longDesc = 
"""

""",
)

entry(
    index = 289,
    label = "Cds-CddCsOs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   Cs  u0 {1,S}
4   O2s u0 {1,S}
""",
    thermo = 'Cds-(Cdd-Cd)CsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 290,
    label = "Cds-(Cdd-O2d)CsOs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cs  u0 {1,S}
4   O2s u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.91,12.65,13.59,14.22,15,15.48,16.28],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (3.273,'kcal/mol','+|-',0.2),
        S298 = (18.58,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = """{CCO/O/C} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
"""

""",
)

entry(
    index = 291,
    label = "Cds-(Cdd-Cd)CsOs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cs  u0 {1,S}
4   O2s u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = 'Cds-CdsCsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 292,
    label = "Cds-CdCS",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   C  u0 {1,S}
4   S  u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 293,
    label = "Cds-CdsCsSs",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cs u0 {1,S}
4   S  u0 {1,S}
""",
    thermo = 'Cds-CdsCsS2',
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc = 
"""
"
""",
)

entry(
    index = 294,
    label = "Cds-CdsCsS2",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cd  u0 {1,D}
3   Cs  u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.3,5.84,5.62,5.57,6.97,7.7,6.11],'cal/(mol*K)'),
        H298 = (20.57,'kcal/mol'),
        S298 = (-8.4,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 295,
    label = "Cds-CdsCsS4",
    group = 
"""
1 * Cd                u0 {2,D} {3,S} {4,S}
2   Cd                u0 {1,D}
3   Cs                u0 {1,S}
4   [S4s,S4d,S4b,S4t] u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.74,5.6,4.93,5.57,7.72,8.79,7.32],'cal/(mol*K)'),
        H298 = (27.53,'kcal/mol'),
        S298 = (-12.89,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 296,
    label = "Cds-CdsCsS6",
    group = 
"""
1 * Cd                      u0 {2,D} {3,S} {4,S}
2   Cd                      u0 {1,D}
3   Cs                      u0 {1,S}
4   [S6s,S6d,S6dd,S6t,S6td] u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.01,5.41,5.84,6.2,7.7,8.36,7.24],'cal/(mol*K)'),
        H298 = (21.44,'kcal/mol'),
        S298 = (-2.61,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 297,
    label = "Cds-CdsCdsSs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cd  u0 {1,D}
3   Cd  u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 298,
    label = "Cds-Cds(Cds-Cd)S2s",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,D}
4   S2s u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 299,
    label = "Cds-Cds(Cds-Cds)S2s",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,D}
4   S2s u0 {1,S}
5   Cd  u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 300,
    label = "Cds-Cds(Cds-Cdd)S2s",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,D}
4   S2s u0 {1,S}
5   Cdd u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 301,
    label = "Cds-Cds(Cds-Cdd-S2d)S2s",
    group = 
"""
1 * Cd  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   Cd  u0 {1,D}
5   S2s u0 {1,S}
6   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 302,
    label = "Cds-Cds(Cds-Cdd-Cd)S2s",
    group = 
"""
1 * Cd  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   Cd  u0 {1,D}
5   S2s u0 {1,S}
6   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 303,
    label = "Cds-CdsCtSs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cd  u0 {1,D}
3   Ct  u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 304,
    label = "Cds-CdsCbSs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cd  u0 {1,D}
3   Cb  u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 305,
    label = "Cds-CddCsSs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   Cs  u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 306,
    label = "Cds-(Cdd-S2d)CsSs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cs  u0 {1,S}
4   S2s u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 307,
    label = "Cds-(Cdd-Cd)CsSs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cs  u0 {1,S}
4   S2s u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 308,
    label = "Cds-CddCdsSs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   Cd  u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 309,
    label = "Cds-(Cdd-S2d)(Cds-Cd)S2s",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   S2s u0 {1,S}
5   S2d u0 {2,D}
6   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 310,
    label = "Cds-(Cdd-S2d)(Cds-Cds)S2s",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   S2s u0 {1,S}
5   S2d u0 {2,D}
6   Cd  u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 311,
    label = "Cds-(Cdd-S2d)(Cds-Cdd)S2s",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   S2s u0 {1,S}
5   S2d u0 {2,D}
6   Cdd u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 312,
    label = "Cds-(Cdd-S2d)(Cds-Cdd-S2d)S2s",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   S2s u0 {1,S}
6   S2d u0 {3,D}
7   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 313,
    label = "Cds-(Cdd-S2d)(Cds-Cdd-Cd)S2s",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   S2s u0 {1,S}
6   S2d u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 314,
    label = "Cds-(Cdd-Cd)(Cds-Cd)S2s",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   S2s u0 {1,S}
5   C   u0 {2,D}
6   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 315,
    label = "Cds-(Cdd-Cd)(Cds-Cds)S2s",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   S2s u0 {1,S}
5   C   u0 {2,D}
6   Cd  u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 316,
    label = "Cds-(Cdd-Cd)(Cds-Cdd)S2s",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   S2s u0 {1,S}
5   C   u0 {2,D}
6   Cdd u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 317,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-S2d)S2s",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   S2s u0 {1,S}
6   C   u0 {3,D}
7   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 318,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-Cd)S2s",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   S2s u0 {1,S}
6   C   u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 319,
    label = "Cds-CddCtSs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   Ct  u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 320,
    label = "Cds-(Cdd-S2d)CtSs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Ct  u0 {1,S}
4   S2s u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 321,
    label = "Cds-(Cdd-Cd)CtSs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Ct  u0 {1,S}
4   S2s u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 322,
    label = "Cds-CddCbSs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   Cb  u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 323,
    label = "Cds-(Cdd-S2d)CbSs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cb  u0 {1,S}
4   S2s u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 324,
    label = "Cds-(Cdd-Cd)CbSs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cb  u0 {1,S}
4   S2s u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 325,
    label = "Cds-(Cdd-S2d)C=SSs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CS  u0 {1,S} {6,D}
4   S2s u0 {1,S}
5   S2d u0 {2,D}
6   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 326,
    label = "Cds-CdsC=SSs",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   CS  u0 {1,S} {5,D}
3   Cd  u0 {1,D}
4   S2s u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 327,
    label = "Cds-CdCC",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   C  u0 {1,S}
4   C  u0 {1,S}
""",
    thermo = 'Cds-CdsCsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 328,
    label = "Cds-CdsCsCs",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.1,4.61,4.99,5.26,5.8,6.08,6.36],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (10.34,'kcal/mol','+|-',0.24),
        S298 = (-12.7,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = """Cd-CsCs BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 329,
    label = "Cds-CdsCdsCs",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cd      u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
""",
    thermo = 'Cds-Cds(Cds-Cds)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 330,
    label = "Cd-CdCs(CO)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   CO  u0 {1,S} {5,D}
3   Cs  u0 {1,S}
4   Cd  u0 {1,D}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.33,16.82,18.64,20.42,23.2,25,27.1],'J/(mol*K)','+|-',[5.66,5.66,5.66,5.66,5.66,5.66,5.66]),
        H298 = (39,'kJ/mol','+|-',4.82),
        S298 = (-51.26,'J/(mol*K)','+|-',6.6),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 331,
    label = "Cds-Cds(Cds-Cd)Cs",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   Cs u0 {1,S}
5   C  u0 {2,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 332,
    label = "Cds-Cds(Cds-Cds)Cs",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   Cs u0 {1,S}
5   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.4,5.37,5.93,6.18,6.5,6.62,6.72],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (8.88,'kcal/mol','+|-',0.24),
        S298 = (-14.6,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = """Cd-CdCs BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 333,
    label = "Cds-Cds(Cds-Cdd)Cs",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,D}
4   Cs  u0 {1,S}
5   Cdd u0 {2,D}
""",
    thermo = 'Cds-Cds(Cds-Cdd-Cd)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 334,
    label = "Cd-CdCs(CCO)",
    group = 
"""
1 * Cd  u0 {2,S} {4,S} {5,D}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   Cs  u0 {1,S}
5   Cd  u0 {1,D}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([22.68,24.05,24.63,25.07,25.64,25.84,25.7],'J/(mol*K)','+|-',[8,8,8,8,8,8,8]),
        H298 = (41.6,'kJ/mol','+|-',6.82),
        S298 = (-48.01,'J/(mol*K)','+|-',9.33),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 335,
    label = "Cds-Cds(Cds-Cdd-S2d)Cs",
    group = 
"""
1 * Cd  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   Cd  u0 {1,D}
5   Cs  u0 {1,S}
6   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 336,
    label = "Cds-Cds(Cds-Cdd-Cd)Cs",
    group = 
"""
1 * Cd  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   Cd  u0 {1,D}
5   Cs  u0 {1,S}
6   C   u0 {3,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 337,
    label = "Cds-CdsCdsCds",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cd      u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
""",
    thermo = 'Cds-Cds(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 338,
    label = "Cds-Cds(Cds-O2d)(Cds-O2d)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   CO  u0 {1,S} {5,D}
3   CO  u0 {1,S} {6,D}
4   Cd  u0 {1,D}
5   O2d u0 {2,D}
6   O2d u0 {3,D}
""",
    thermo = 'Cds-CdsCsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 339,
    label = "Cds-Cds(Cds-O2d)(Cds-Cd)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   CO  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {5,D}
4   Cd  u0 {1,D}
5   C   u0 {3,D}
6   O2d u0 {2,D}
""",
    thermo = 'Cds-Cds(Cds-O2d)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 340,
    label = "Cds-Cds(Cds-O2d)(Cds-Cds)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   CO  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {5,D}
4   Cd  u0 {1,D}
5   Cd  u0 {3,D}
6   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.7,6.13,6.87,7.1,7.2,7.16,7.06],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (11.6,'kcal/mol','+|-',0.24),
        S298 = (-16.5,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = """Cd-COCd from CD/CD2/ jwb est 6/97""",
    longDesc = 
"""
AG Vandeputte, added 7 kcal/mol to the following value (see phd M Sabbe)
""",
)

entry(
    index = 341,
    label = "Cds-Cds(Cds-O2d)(Cds-Cdd)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   CO  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {5,D}
4   Cd  u0 {1,D}
5   Cdd u0 {3,D}
6   O2d u0 {2,D}
""",
    thermo = 'Cds-Cds(Cds-O2d)(Cds-Cdd-Cd)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 342,
    label = "Cds-Cds(Cds-O2d)(Cds-Cdd-O2d)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {5,D}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Cd  u0 {1,D}
6   O2d u0 {3,D}
7   O2d u0 {4,D}
""",
    thermo = 'Cd-CdCs(CCO)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 343,
    label = "Cds-Cds(Cds-O2d)(Cds-Cdd-Cd)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {5,D}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Cd  u0 {1,D}
6   O2d u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = 'Cds-Cds(Cds-O2d)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 344,
    label = "Cds-Cds(Cds-Cd)(Cds-Cd)",
    group = 
"""
1 * Cd u0 {2,S} {3,S} {4,D}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,S} {6,D}
4   Cd u0 {1,D}
5   C  u0 {2,D}
6   C  u0 {3,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 345,
    label = "Cds-Cds(Cds-Cds)(Cds-Cds)",
    group = 
"""
1 * Cd u0 {2,S} {3,S} {4,D}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,S} {6,D}
4   Cd u0 {1,D}
5   Cd u0 {2,D}
6   Cd u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.9,2.69,3.5,4.28,5.57,6.21,7.37],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (11.6,'kcal/mol','+|-',0.24),
        S298 = (-15.67,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = """Cd-CdCd Hf=3D est S,Cp mopac nov99""",
    longDesc = 
"""
AG Vandeputte, added 7 kcal/mol to the following value (see phd M Sabbe)
""",
)

entry(
    index = 346,
    label = "Cds-Cds(Cds-Cds)(Cds-Cdd)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,D}
5   Cd  u0 {2,D}
6   Cdd u0 {3,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)(Cds-Cdd-Cd)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 347,
    label = "Cds-Cds(Cds-Cds)(Cds-Cdd-O2d)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {5,D}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Cd  u0 {1,D}
6   Cd  u0 {3,D}
7   O2d u0 {4,D}
""",
    thermo = 'Cd-CdCs(CCO)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 348,
    label = "Cds-Cds(Cds-Cds)(Cds-Cdd-S2d)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {5,D}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Cd  u0 {1,D}
6   Cd  u0 {3,D}
7   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 349,
    label = "Cds-Cds(Cds-Cds)(Cds-Cdd-Cd)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {5,D}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Cd  u0 {1,D}
6   Cd  u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 350,
    label = "Cds-Cds(Cds-Cdd)(Cds-Cdd)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,D}
5   Cdd u0 {2,D}
6   Cdd u0 {3,D}
""",
    thermo = 'Cds-Cds(Cds-Cdd-Cd)(Cds-Cdd-Cd)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 351,
    label = "Cds-Cds(Cds-Cdd-O2d)(Cds-Cdd-O2d)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {6,D}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {7,D}
5   Cdd u0 {3,D} {8,D}
6   Cd  u0 {1,D}
7   O2d u0 {4,D}
8   O2d u0 {5,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 352,
    label = "Cds-Cds(Cds-Cdd-O2d)(Cds-Cdd-Cd)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {6,D}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {7,D}
5   Cdd u0 {3,D} {8,D}
6   Cd  u0 {1,D}
7   O2d u0 {4,D}
8   C   u0 {5,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)(Cds-Cdd-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 353,
    label = "Cds-Cds(Cds-Cdd-S2d)(Cds-Cdd-S2d)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {6,D}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {7,D}
5   Cdd u0 {3,D} {8,D}
6   Cd  u0 {1,D}
7   S2d u0 {4,D}
8   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 354,
    label = "Cds-Cds(Cds-Cdd-S2d)(Cds-Cdd-Cd)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {6,D}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {7,D}
5   Cdd u0 {3,D} {8,D}
6   Cd  u0 {1,D}
7   S2d u0 {4,D}
8   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 355,
    label = "Cds-Cds(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {6,D}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {7,D}
5   Cdd u0 {3,D} {8,D}
6   Cd  u0 {1,D}
7   C   u0 {4,D}
8   C   u0 {5,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)(Cds-Cdd-Cd)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 356,
    label = "Cds-CdsCtCs",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.5,3.88,4.88,4.18,4.86,5.4,6.01],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (8.11,'kcal/mol','+|-',0.24),
        S298 = (-13.02,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = """Cd-CtCs RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
"""

""",
)

entry(
    index = 357,
    label = "Cd-CdCs(CtN3t)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cd  u0 {1,D} {5,S} {6,S}
3   Ct  u0 {1,S} {7,T}
4   Cs  u0 {1,S}
5   R   u0 {2,S}
6   R   u0 {2,S}
7   N3t u0 {3,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.2,10.6,11.7,12.5,13.8,14.7,15.9],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (40.2,'kcal/mol','+|-',1.3),
        S298 = (17.9,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 358,
    label = "Cds-CdsCtCds",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cd      u0 {1,D}
3   Ct      u0 {1,S}
4   [Cd,CO] u0 {1,S}
""",
    thermo = 'Cds-Cds(Cds-Cds)Ct',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 359,
    label = "Cds-CdsCt(Cds-O2d)",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   CO  u0 {1,S} {5,D}
3   Cd  u0 {1,D}
4   Ct  u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = 'Cds-Cds(Cds-O2d)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 360,
    label = "Cds-CdsCt(Cds-Cd)",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   Ct u0 {1,S}
5   C  u0 {2,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)Ct',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 361,
    label = "Cds-Cds(Cds-Cds)Ct",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   Ct u0 {1,S}
5   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.89,5.26,5.98,6.37,6.67,6.78,6.89],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (7.54,'kcal/mol','+|-',0.24),
        S298 = (-14.65,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = """Cd-CtCd RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
"""

""",
)

entry(
    index = 362,
    label = "Cds-Cds(Cds-Cdd)Ct",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,D}
4   Ct  u0 {1,S}
5   Cdd u0 {2,D}
""",
    thermo = 'Cds-Cds(Cds-Cdd-Cd)Ct',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 363,
    label = "Cds-Cds(Cds-Cdd-O2d)Ct",
    group = 
"""
1 * Cd  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   Cd  u0 {1,D}
5   Ct  u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)(Cds-Cdd-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 364,
    label = "Cds-Cds(Cds-Cdd-S2d)Ct",
    group = 
"""
1 * Cd  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   Cd  u0 {1,D}
5   Ct  u0 {1,S}
6   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 365,
    label = "Cds-Cds(Cds-Cdd-Cd)Ct",
    group = 
"""
1 * Cd  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   Cd  u0 {1,D}
5   Ct  u0 {1,S}
6   C   u0 {3,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)Ct',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 366,
    label = "Cds-CdsCtCt",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.23,4.59,5.41,5.93,6.48,6.74,7.02],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (8.81,'kcal/mol','+|-',0.24),
        S298 = (-13.51,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = """Cd-CtCt RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
"""

""",
)

entry(
    index = 367,
    label = "Cds-Cd(CtN3t)(CtN3t)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   Ct  u0 {1,S} {5,T}
3   Ct  u0 {1,S} {6,T}
4   Cd  u0 {1,D}
5   N3t u0 {2,T}
6   N3t u0 {3,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (84.1,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 368,
    label = "Cds-CdsCbCs",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.4,5.37,5.93,6.18,6.5,6.62,6.72],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (8.64,'kcal/mol','+|-',0.24),
        S298 = (-14.6,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = """Cd-CbCs BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 369,
    label = "Cds-CdsCbCds",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cd      u0 {1,D}
3   Cb      u0 {1,S}
4   [Cd,CO] u0 {1,S}
""",
    thermo = 'Cds-Cds(Cds-Cds)Cb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 370,
    label = "Cds-CdsCb(Cds-O2d)",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   CO  u0 {1,S} {5,D}
3   Cd  u0 {1,D}
4   Cb  u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = 'Cds-Cds(Cds-O2d)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 371,
    label = "Cds-Cds(Cds-Cd)Cb",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   Cb u0 {1,S}
5   C  u0 {2,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)Cb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 372,
    label = "Cds-Cds(Cds-Cds)Cb",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   Cb u0 {1,S}
5   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.7,6.13,6.87,7.1,7.2,7.16,7.06],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (7.18,'kcal/mol','+|-',0.24),
        S298 = (-16.5,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = """Cd-CbCd BOZZELLI =3D Cd/Cs/Cb + (Cd/Cs/Cd - Cd/Cs/Cs)""",
    longDesc = 
"""

""",
)

entry(
    index = 373,
    label = "Cds-Cds(Cds-Cdd)Cb",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,D}
4   Cb  u0 {1,S}
5   Cdd u0 {2,D}
""",
    thermo = 'Cds-Cds(Cds-Cdd-Cd)Cb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 374,
    label = "Cds-Cds(Cds-Cdd-O2d)Cb",
    group = 
"""
1 * Cd  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   Cd  u0 {1,D}
5   Cb  u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)(Cds-Cdd-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 375,
    label = "Cds-Cds(Cds-Cdd-S2d)Cb",
    group = 
"""
1 * Cd  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   Cd  u0 {1,D}
5   Cb  u0 {1,S}
6   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 376,
    label = "Cds-Cds(Cds-Cdd-Cd)Cb",
    group = 
"""
1 * Cd  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   Cd  u0 {1,D}
5   Cb  u0 {1,S}
6   C   u0 {3,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)Cb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 377,
    label = "Cds-CdsCbCt",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cb u0 {1,S}
4   Ct u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.22,3.14,4.54,4.11,5.06,5.79,6.71],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (6.7,'kcal/mol','+|-',0.24),
        S298 = (-17.04,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = """Cd-CbCt Hf=3D est S,Cp mopac nov99""",
    longDesc = 
"""

""",
)

entry(
    index = 378,
    label = "Cds-CdsCbCb",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.7,6.13,6.87,7.1,7.2,7.16,7.06],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (8,'kcal/mol','+|-',0.24),
        S298 = (-16.5,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = """Cd-CbCb BOZZELLI =3D Cd/Cs/Cb + (Cd/Cs/Cb - Cd/Cs/Cs)""",
    longDesc = 
"""

""",
)

entry(
    index = 379,
    label = "Cds-CddCsCs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
""",
    thermo = 'Cds-(Cdd-Cd)CsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 380,
    label = "Cds-(Cdd-O2d)CsCs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([42.55,46.42,50,53.24,58.3,61.71,66.01],'J/(mol*K)','+|-',[4.76,4.76,4.76,4.76,4.76,4.76,4.76]),
        H298 = (0.5,'kJ/mol','+|-',4.06),
        S298 = (84.72,'J/(mol*K)','+|-',5.55),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 381,
    label = "Cds-(Cdd-S2d)CsCs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 382,
    label = "Cds-(Cdd-Cd)CsCs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = 'Cds-CdsCsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 383,
    label = "Cds-CddCdsCs",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cdd     u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cds)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 384,
    label = "Cds-(Cdd-O2d)(Cds-O2d)Cs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CO  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   O2d u0 {2,D}
6   O2d u0 {3,D}
""",
    thermo = 'Cds-(Cdd-O2d)CsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 385,
    label = "Cds-(Cdd-O2d)(Cds-Cd)Cs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   O2d u0 {2,D}
6   C   u0 {3,D}
""",
    thermo = 'Cds-(Cdd-O2d)(Cds-Cds)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 386,
    label = "Cds-(Cdd-O2d)(Cds-Cds)Cs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   O2d u0 {2,D}
6   Cd  u0 {3,D}
""",
    thermo = 'Cds-(Cdd-O2d)CsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 387,
    label = "Cds-(Cdd-O2d)(Cds-Cdd)Cs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   O2d u0 {2,D}
6   Cdd u0 {3,D}
""",
    thermo = 'Cds-(Cdd-O2d)(Cds-Cdd-Cd)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 388,
    label = "Cds-(Cdd-O2d)(Cds-Cdd-O2d)Cs",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Cs  u0 {1,S}
6   O2d u0 {3,D}
7   O2d u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.1,11.24,12.12,12.84,14,14.75,15.72],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-2.07,'kcal/mol','+|-',0.24),
        S298 = (19.65,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = """{CCO/C/CCO} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
"""

""",
)

entry(
    index = 389,
    label = "Cds-(Cdd-O2d)(Cds-Cdd-Cd)Cs",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Cs  u0 {1,S}
6   O2d u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = 'Cds-(Cdd-O2d)(Cds-Cds)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 390,
    label = "Cds-(Cdd-S2d)(Cds-Cd)Cs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   S2d u0 {2,D}
6   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 391,
    label = "Cds-(Cdd-S2d)(Cds-Cds)Cs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   S2d u0 {2,D}
6   Cd  u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 392,
    label = "Cds-(Cdd-S2d)(Cds-Cdd)Cs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   S2d u0 {2,D}
6   Cdd u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 393,
    label = "Cds-(Cdd-S2d)(Cds-Cdd-S2d)Cs",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Cs  u0 {1,S}
6   S2d u0 {3,D}
7   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 394,
    label = "Cds-(Cdd-S2d)(Cds-Cdd-Cd)Cs",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Cs  u0 {1,S}
6   S2d u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 395,
    label = "Cds-(Cdd-Cd)(Cds-Cd)Cs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   C   u0 {2,D}
6   C   u0 {3,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cds)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 396,
    label = "Cds-(Cdd-Cd)(Cds-Cds)Cs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   C   u0 {2,D}
6   Cd  u0 {3,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 397,
    label = "Cds-(Cdd-Cd)(Cds-Cdd)Cs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   C   u0 {2,D}
6   Cdd u0 {3,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cdd-Cd)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 398,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-O2d)Cs",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Cs  u0 {1,S}
6   C   u0 {3,D}
7   O2d u0 {4,D}
""",
    thermo = 'Cd-CdCs(CCO)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 399,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-S2d)Cs",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Cs  u0 {1,S}
6   C   u0 {3,D}
7   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 400,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-Cd)Cs",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Cs  u0 {1,S}
6   C   u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cds)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 401,
    label = "Cds-CddCdsCds",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cdd     u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 402,
    label = "Cds-(Cdd-O2d)(Cds-O2d)(Cds-O2d)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CO  u0 {1,S} {6,D}
4   CO  u0 {1,S} {7,D}
5   O2d u0 {2,D}
6   O2d u0 {3,D}
7   O2d u0 {4,D}
""",
    thermo = 'Cds-(Cdd-O2d)CsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 403,
    label = "Cds-(Cdd-O2d)(Cds-Cd)(Cds-O2d)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   CO  u0 {1,S} {7,D}
5   O2d u0 {2,D}
6   C   u0 {3,D}
7   O2d u0 {4,D}
""",
    thermo = 'Cds-(Cdd-O2d)(Cds-Cds)(Cds-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 404,
    label = "Cds-(Cdd-O2d)(Cds-Cds)(Cds-O2d)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   CO  u0 {1,S} {7,D}
5   O2d u0 {2,D}
6   Cd  u0 {3,D}
7   O2d u0 {4,D}
""",
    thermo = 'Cds-(Cdd-O2d)(Cds-O2d)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 405,
    label = "Cds-(Cdd-O2d)(Cds-Cdd)(Cds-O2d)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   CO  u0 {1,S} {7,D}
5   O2d u0 {2,D}
6   Cdd u0 {3,D}
7   O2d u0 {4,D}
""",
    thermo = 'Cds-(Cdd-O2d)(Cds-Cdd-Cd)(Cds-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 406,
    label = "Cds-(Cdd-O2d)(Cds-Cdd-O2d)(Cds-O2d)",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cdd u0 {1,D} {6,D}
4   CO  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {8,D}
6   O2d u0 {3,D}
7   O2d u0 {4,D}
8   O2d u0 {5,D}
""",
    thermo = 'Cds-(Cdd-O2d)(Cds-Cdd-O2d)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 407,
    label = "Cds-(Cdd-O2d)(Cds-Cdd-Cd)(Cds-O2d)",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cdd u0 {1,D} {6,D}
4   CO  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {8,D}
6   O2d u0 {3,D}
7   O2d u0 {4,D}
8   C   u0 {5,D}
""",
    thermo = 'Cds-(Cdd-O2d)(Cds-Cds)(Cds-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 408,
    label = "Cds-(Cdd-O2d)(Cds-Cd)(Cds-Cd)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   O2d u0 {2,D}
6   C   u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = 'Cds-(Cdd-O2d)(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 409,
    label = "Cds-(Cdd-O2d)(Cds-Cds)(Cds-Cds)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   O2d u0 {2,D}
6   Cd  u0 {3,D}
7   Cd  u0 {4,D}
""",
    thermo = 'Cds-(Cdd-O2d)CsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 410,
    label = "Cds-(Cdd-O2d)(Cds-Cdd)(Cds-Cds)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   O2d u0 {2,D}
6   Cdd u0 {3,D}
7   Cd  u0 {4,D}
""",
    thermo = 'Cds-(Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 411,
    label = "Cds-(Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cds)",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cdd u0 {1,D} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {8,D}
6   O2d u0 {3,D}
7   Cd  u0 {4,D}
8   O2d u0 {5,D}
""",
    thermo = 'Cds-(Cdd-O2d)(Cds-Cdd-O2d)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 412,
    label = "Cds-(Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cds)",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cdd u0 {1,D} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {8,D}
6   O2d u0 {3,D}
7   Cd  u0 {4,D}
8   C   u0 {5,D}
""",
    thermo = 'Cds-(Cdd-O2d)(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 413,
    label = "Cds-(Cdd-O2d)(Cds-Cdd)(Cds-Cdd)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   O2d u0 {2,D}
6   Cdd u0 {3,D}
7   Cdd u0 {4,D}
""",
    thermo = 'Cds-(Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 414,
    label = "Cds-(Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cdd u0 {1,D} {7,D}
5   Cdd u0 {2,D} {8,D}
6   Cdd u0 {3,D} {9,D}
7   O2d u0 {4,D}
8   O2d u0 {5,D}
9   O2d u0 {6,D}
""",
    thermo = 'Cds-(Cdd-O2d)(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 415,
    label = "Cds-(Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cdd u0 {1,D} {7,D}
5   Cdd u0 {2,D} {8,D}
6   Cdd u0 {3,D} {9,D}
7   O2d u0 {4,D}
8   O2d u0 {5,D}
9   C   u0 {6,D}
""",
    thermo = 'Cds-(Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 416,
    label = "Cds-(Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cdd u0 {1,D} {7,D}
5   Cdd u0 {2,D} {8,D}
6   Cdd u0 {3,D} {9,D}
7   O2d u0 {4,D}
8   C   u0 {5,D}
9   C   u0 {6,D}
""",
    thermo = 'Cds-(Cdd-O2d)(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 417,
    label = "Cds-(Cdd-Cd)(Cds-O2d)(Cds-O2d)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CO  u0 {1,S} {6,D}
4   CO  u0 {1,S} {7,D}
5   C   u0 {2,D}
6   O2d u0 {3,D}
7   O2d u0 {4,D}
""",
    thermo = 'Cds-Cds(Cds-O2d)(Cds-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 418,
    label = "Cds-(Cdd-Cd)(Cds-O2d)(Cds-Cd)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CO  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {6,D}
5   C   u0 {2,D}
6   C   u0 {4,D}
7   O2d u0 {3,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-O2d)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 419,
    label = "Cds-(Cdd-Cd)(Cds-O2d)(Cds-Cds)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CO  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {6,D}
5   C   u0 {2,D}
6   Cd  u0 {4,D}
7   O2d u0 {3,D}
""",
    thermo = 'Cds-Cds(Cds-O2d)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 420,
    label = "Cds-(Cdd-Cd)(Cds-O2d)(Cds-Cdd)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CO  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {6,D}
5   C   u0 {2,D}
6   Cdd u0 {4,D}
7   O2d u0 {3,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-O2d)(Cds-Cdd-Cd)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 421,
    label = "Cds-(Cdd-Cd)(Cds-O2d)(Cds-Cdd-O2d)",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cdd u0 {1,D} {6,D}
4   CO  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {8,D}
6   C   u0 {3,D}
7   O2d u0 {4,D}
8   O2d u0 {5,D}
""",
    thermo = 'Cds-Cds(Cds-O2d)(Cds-Cdd-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 422,
    label = "Cds-(Cdd-Cd)(Cds-O2d)(Cds-Cdd-Cd)",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cdd u0 {1,D} {6,D}
4   CO  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {8,D}
6   C   u0 {3,D}
7   O2d u0 {4,D}
8   C   u0 {5,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-O2d)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 423,
    label = "Cds-(Cdd-S2d)(Cds-Cd)(Cds-Cd)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   S2d u0 {2,D}
6   C   u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 424,
    label = "Cds-(Cdd-S2d)(Cds-Cds)(Cds-Cds)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   S2d u0 {2,D}
6   Cd  u0 {3,D}
7   Cd  u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 425,
    label = "Cds-(Cdd-S2d)(Cds-Cdd)(Cds-Cds)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   S2d u0 {2,D}
6   Cdd u0 {3,D}
7   Cd  u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 426,
    label = "Cds-(Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cds)",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cdd u0 {1,D} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {8,D}
6   S2d u0 {3,D}
7   Cd  u0 {4,D}
8   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 427,
    label = "Cds-(Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cds)",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cdd u0 {1,D} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {8,D}
6   S2d u0 {3,D}
7   Cd  u0 {4,D}
8   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 428,
    label = "Cds-(Cdd-S2d)(Cds-Cdd)(Cds-Cdd)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   S2d u0 {2,D}
6   Cdd u0 {3,D}
7   Cdd u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 429,
    label = "Cds-(Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cdd u0 {1,D} {7,D}
5   Cdd u0 {2,D} {8,D}
6   Cdd u0 {3,D} {9,D}
7   S2d u0 {4,D}
8   S2d u0 {5,D}
9   S2d u0 {6,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 430,
    label = "Cds-(Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-Cd)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cdd u0 {1,D} {7,D}
5   Cdd u0 {2,D} {8,D}
6   Cdd u0 {3,D} {9,D}
7   S2d u0 {4,D}
8   S2d u0 {5,D}
9   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 431,
    label = "Cds-(Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cdd u0 {1,D} {7,D}
5   Cdd u0 {2,D} {8,D}
6   Cdd u0 {3,D} {9,D}
7   S2d u0 {4,D}
8   C   u0 {5,D}
9   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 432,
    label = "Cds-(Cdd-Cd)(Cds-Cd)(Cds-Cd)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   C   u0 {2,D}
6   C   u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 433,
    label = "Cds-(Cdd-Cd)(Cds-Cds)(Cds-Cds)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   C   u0 {2,D}
6   Cd  u0 {3,D}
7   Cd  u0 {4,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 434,
    label = "Cds-(Cdd-Cd)(Cds-Cdd)(Cds-Cds)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   C   u0 {2,D}
6   Cdd u0 {3,D}
7   Cd  u0 {4,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 435,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-O2d)(Cds-Cds)",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cdd u0 {1,D} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {8,D}
6   C   u0 {3,D}
7   Cd  u0 {4,D}
8   O2d u0 {5,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)(Cds-Cdd-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 436,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-S2d)(Cds-Cds)",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cdd u0 {1,D} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {8,D}
6   C   u0 {3,D}
7   Cd  u0 {4,D}
8   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 437,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cds)",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cdd u0 {1,D} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {8,D}
6   C   u0 {3,D}
7   Cd  u0 {4,D}
8   C   u0 {5,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 438,
    label = "Cds-(Cdd-Cd)(Cds-Cdd)(Cds-Cdd)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   C   u0 {2,D}
6   Cdd u0 {3,D}
7   Cdd u0 {4,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 439,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-O2d)(Cds-Cdd-O2d)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cdd u0 {1,D} {7,D}
5   Cdd u0 {2,D} {8,D}
6   Cdd u0 {3,D} {9,D}
7   C   u0 {4,D}
8   O2d u0 {5,D}
9   O2d u0 {6,D}
""",
    thermo = 'Cds-Cds(Cds-Cdd-O2d)(Cds-Cdd-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 440,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-O2d)(Cds-Cdd-Cd)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cdd u0 {1,D} {7,D}
5   Cdd u0 {2,D} {8,D}
6   Cdd u0 {3,D} {9,D}
7   C   u0 {4,D}
8   O2d u0 {5,D}
9   C   u0 {6,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cdd-O2d)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 441,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-S2d)(Cds-Cdd-S2d)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cdd u0 {1,D} {7,D}
5   Cdd u0 {2,D} {8,D}
6   Cdd u0 {3,D} {9,D}
7   C   u0 {4,D}
8   S2d u0 {5,D}
9   S2d u0 {6,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 442,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-S2d)(Cds-Cdd-Cd)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cdd u0 {1,D} {7,D}
5   Cdd u0 {2,D} {8,D}
6   Cdd u0 {3,D} {9,D}
7   C   u0 {4,D}
8   S2d u0 {5,D}
9   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 443,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cdd u0 {1,D} {7,D}
5   Cdd u0 {2,D} {8,D}
6   Cdd u0 {3,D} {9,D}
7   C   u0 {4,D}
8   C   u0 {5,D}
9   C   u0 {6,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 444,
    label = "Cds-CddCtCs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   Ct  u0 {1,S}
4   Cs  u0 {1,S}
""",
    thermo = 'Cds-(Cdd-Cd)CtCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 445,
    label = "Cds-(Cdd-O2d)CtCs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Ct  u0 {1,S}
4   Cs  u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = 'Cds-(Cdd-O2d)(Cds-Cds)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 446,
    label = "Cds-(Cdd-S2d)CtCs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Ct  u0 {1,S}
4   Cs  u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 447,
    label = "Cds-(Cdd-Cd)CtCs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Ct  u0 {1,S}
4   Cs  u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = 'Cds-CdsCtCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 448,
    label = "Cds-CddCtCds",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cdd     u0 {1,D}
3   Ct      u0 {1,S}
4   [Cd,CO] u0 {1,S}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cds)Ct',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 449,
    label = "Cds-(Cdd-O2d)(Cds-O2d)Ct",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CO  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   O2d u0 {2,D}
6   O2d u0 {3,D}
""",
    thermo = 'Cds-(Cdd-O2d)(Cds-Cds)(Cds-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 450,
    label = "Cds-(Cdd-O2d)(Cds-Cd)Ct",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   O2d u0 {2,D}
6   C   u0 {3,D}
""",
    thermo = 'Cds-(Cdd-O2d)(Cds-Cds)Ct',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 451,
    label = "Cds-(Cdd-O2d)(Cds-Cds)Ct",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   O2d u0 {2,D}
6   Cd  u0 {3,D}
""",
    thermo = 'Cds-(Cdd-O2d)(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 452,
    label = "Cds-(Cdd-O2d)(Cds-Cdd)Ct",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   O2d u0 {2,D}
6   Cdd u0 {3,D}
""",
    thermo = 'Cds-(Cdd-O2d)(Cds-Cdd-Cd)Ct',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 453,
    label = "Cds-(Cdd-O2d)(Cds-Cdd-O2d)Ct",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Ct  u0 {1,S}
6   O2d u0 {3,D}
7   O2d u0 {4,D}
""",
    thermo = 'Cds-(Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 454,
    label = "Cds-(Cdd-O2d)(Cds-Cdd-Cd)Ct",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Ct  u0 {1,S}
6   O2d u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = 'Cds-(Cdd-O2d)(Cds-Cds)Ct',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 455,
    label = "Cds-(Cdd-S2d)(Cds-Cd)Ct",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   S2d u0 {2,D}
6   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 456,
    label = "Cds-(Cdd-S2d)(Cds-Cds)Ct",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   S2d u0 {2,D}
6   Cd  u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 457,
    label = "Cds-(Cdd-S2d)(Cds-Cdd)Ct",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   S2d u0 {2,D}
6   Cdd u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 458,
    label = "Cds-(Cdd-S2d)(Cds-Cdd-S2d)Ct",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Ct  u0 {1,S}
6   S2d u0 {3,D}
7   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 459,
    label = "Cds-(Cdd-S2d)(Cds-Cdd-Cd)Ct",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Ct  u0 {1,S}
6   S2d u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 460,
    label = "Cds-(Cdd-Cd)(Cds-Cd)Ct",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   C   u0 {2,D}
6   C   u0 {3,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cds)Ct',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 461,
    label = "Cds-(Cdd-Cd)(Cds-Cds)Ct",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   C   u0 {2,D}
6   Cd  u0 {3,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)Ct',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 462,
    label = "Cds-(Cdd-Cd)(Cds-Cdd)Ct",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   C   u0 {2,D}
6   Cdd u0 {3,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cdd-Cd)Ct',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 463,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-O2d)Ct",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Ct  u0 {1,S}
6   C   u0 {3,D}
7   O2d u0 {4,D}
""",
    thermo = 'Cds-Cds(Cds-Cdd-O2d)Ct',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 464,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-S2d)Ct",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Ct  u0 {1,S}
6   C   u0 {3,D}
7   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 465,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-Cd)Ct",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Ct  u0 {1,S}
6   C   u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cds)Ct',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 466,
    label = "Cds-CddCtCt",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   Ct  u0 {1,S}
4   Ct  u0 {1,S}
""",
    thermo = 'Cds-(Cdd-Cd)CtCt',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 467,
    label = "Cds-(Cdd-O2d)CtCt",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Ct  u0 {1,S}
4   Ct  u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = 'Cds-(Cdd-O2d)(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 468,
    label = "Cds-(Cdd-S2d)CtCt",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Ct  u0 {1,S}
4   Ct  u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 469,
    label = "Cds-(Cdd-Cd)CtCt",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Ct  u0 {1,S}
4   Ct  u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = 'Cds-CdsCtCt',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 470,
    label = "Cds-CddCbCs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   Cb  u0 {1,S}
4   Cs  u0 {1,S}
""",
    thermo = 'Cds-(Cdd-Cd)CbCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 471,
    label = "Cds-(Cdd-O2d)CbCs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cb  u0 {1,S}
4   Cs  u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = 'Cds-(Cdd-O2d)(Cds-Cds)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 472,
    label = "Cds-(Cdd-S2d)CbCs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cb  u0 {1,S}
4   Cs  u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 473,
    label = "Cds-(Cdd-Cd)CbCs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cb  u0 {1,S}
4   Cs  u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = 'Cds-CdsCbCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 474,
    label = "Cds-CddCbCds",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cdd     u0 {1,D}
3   Cb      u0 {1,S}
4   [Cd,CO] u0 {1,S}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cds)Cb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 475,
    label = "Cds-(Cdd-O2d)(Cds-O2d)Cb",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CO  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   O2d u0 {2,D}
6   O2d u0 {3,D}
""",
    thermo = 'Cds-(Cdd-O2d)(Cds-Cds)(Cds-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 476,
    label = "Cds-(Cdd-O2d)(Cds-Cd)Cb",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   O2d u0 {2,D}
6   C   u0 {3,D}
""",
    thermo = 'Cds-(Cdd-O2d)(Cds-Cds)Cb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 477,
    label = "Cds-(Cdd-O2d)(Cds-Cds)Cb",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   O2d u0 {2,D}
6   Cd  u0 {3,D}
""",
    thermo = 'Cds-(Cdd-O2d)(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 478,
    label = "Cds-(Cdd-O2d)(Cds-Cdd)Cb",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   O2d u0 {2,D}
6   Cdd u0 {3,D}
""",
    thermo = 'Cds-(Cdd-O2d)(Cds-Cdd-Cd)Cb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 479,
    label = "Cds-(Cdd-O2d)(Cds-Cdd-O2d)Cb",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Cb  u0 {1,S}
6   O2d u0 {3,D}
7   O2d u0 {4,D}
""",
    thermo = 'Cds-(Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 480,
    label = "Cds-(Cdd-O2d)(Cds-Cdd-Cd)Cb",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Cb  u0 {1,S}
6   O2d u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = 'Cds-(Cdd-O2d)(Cds-Cds)Cb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 481,
    label = "Cds-(Cdd-S2d)(Cds-Cd)Cb",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   S2d u0 {2,D}
6   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 482,
    label = "Cds-(Cdd-S2d)(Cds-Cds)Cb",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   S2d u0 {2,D}
6   Cd  u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 483,
    label = "Cds-(Cdd-S2d)(Cds-Cdd)Cb",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   S2d u0 {2,D}
6   Cdd u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 484,
    label = "Cds-(Cdd-S2d)(Cds-Cdd-S2d)Cb",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Cb  u0 {1,S}
6   S2d u0 {3,D}
7   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 485,
    label = "Cds-(Cdd-S2d)(Cds-Cdd-Cd)Cb",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Cb  u0 {1,S}
6   S2d u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 486,
    label = "Cds-(Cdd-Cd)(Cds-Cd)Cb",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   C   u0 {2,D}
6   C   u0 {3,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cds)Cb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 487,
    label = "Cds-(Cdd-Cd)(Cds-Cds)Cb",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   C   u0 {2,D}
6   Cd  u0 {3,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)Cb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 488,
    label = "Cds-(Cdd-Cd)(Cds-Cdd)Cb",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   C   u0 {2,D}
6   Cdd u0 {3,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cdd-Cd)Cb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 489,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-O2d)Cb",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Cb  u0 {1,S}
6   C   u0 {3,D}
7   O2d u0 {4,D}
""",
    thermo = 'Cds-Cds(Cds-Cdd-O2d)Cb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 490,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-S2d)Cb",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Cb  u0 {1,S}
6   C   u0 {3,D}
7   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 491,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-Cd)Cb",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Cb  u0 {1,S}
6   C   u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cds)Cb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 492,
    label = "Cds-CddCbCt",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   Cb  u0 {1,S}
4   Ct  u0 {1,S}
""",
    thermo = 'Cds-(Cdd-Cd)CbCt',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 493,
    label = "Cds-(Cdd-O2d)CbCt",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cb  u0 {1,S}
4   Ct  u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = 'Cds-(Cdd-O2d)(Cds-Cds)Ct',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 494,
    label = "Cds-(Cdd-S2d)CbCt",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cb  u0 {1,S}
4   Ct  u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 495,
    label = "Cds-(Cdd-Cd)CbCt",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cb  u0 {1,S}
4   Ct  u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = 'Cds-CdsCbCt',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 496,
    label = "Cds-CddCbCb",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
""",
    thermo = 'Cds-(Cdd-Cd)CbCb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 497,
    label = "Cds-(Cdd-O2d)CbCb",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = 'Cds-(Cdd-O2d)(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 498,
    label = "Cds-(Cdd-S2d)CbCb",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 499,
    label = "Cds-(Cdd-Cd)CbCb",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = 'Cds-CdsCbCb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 500,
    label = "Cds-CdsC=SC=S",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   CS  u0 {1,S} {5,D}
3   CS  u0 {1,S} {6,D}
4   Cd  u0 {1,D}
5   S2d u0 {2,D}
6   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 501,
    label = "Cds-(Cdd-Cd)C=S(Cds-Cd)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CS  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {6,D}
5   C   u0 {2,D}
6   C   u0 {4,D}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 502,
    label = "Cds-(Cdd-Cd)C=S(Cds-Cds)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CS  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {6,D}
5   C   u0 {2,D}
6   Cd  u0 {4,D}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 503,
    label = "Cds-(Cdd-Cd)C=S(Cds-Cdd)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CS  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {6,D}
5   C   u0 {2,D}
6   Cdd u0 {4,D}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 504,
    label = "Cds-(Cdd-Cd)C=S(Cds-Cdd-Cd)",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cdd u0 {1,D} {6,D}
4   CS  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {8,D}
6   C   u0 {3,D}
7   S2d u0 {4,D}
8   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 505,
    label = "Cds-(Cdd-Cd)C=S(Cds-Cdd-S2d)",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cdd u0 {1,D} {6,D}
4   CS  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {8,D}
6   C   u0 {3,D}
7   S2d u0 {4,D}
8   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 506,
    label = "Cds-(Cdd-S2d)C=SCs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CS  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   S2d u0 {2,D}
6   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 507,
    label = "Cds-(Cdd-S2d)C=SCt",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CS  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   S2d u0 {2,D}
6   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 508,
    label = "Cds-(Cdd-S2d)C=SCb",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CS  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   S2d u0 {2,D}
6   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 509,
    label = "Cds-(Cdd-Cd)C=SC=S",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CS  u0 {1,S} {6,D}
4   CS  u0 {1,S} {7,D}
5   C   u0 {2,D}
6   S2d u0 {3,D}
7   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 510,
    label = "Cds-(Cdd-S2d)(Cds-Cd)C=S",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   CS  u0 {1,S} {7,D}
5   S2d u0 {2,D}
6   C   u0 {3,D}
7   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 511,
    label = "Cds-(Cdd-S2d)(Cds-Cds)C=S",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   CS  u0 {1,S} {7,D}
5   S2d u0 {2,D}
6   Cd  u0 {3,D}
7   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 512,
    label = "Cds-(Cdd-S2d)(Cds-Cdd)C=S",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   CS  u0 {1,S} {7,D}
5   S2d u0 {2,D}
6   Cdd u0 {3,D}
7   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 513,
    label = "Cds-(Cdd-S2d)(Cds-Cdd-S2d)C=S",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cdd u0 {1,D} {6,D}
4   CS  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {8,D}
6   S2d u0 {3,D}
7   S2d u0 {4,D}
8   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 514,
    label = "Cds-(Cdd-S2d)(Cds-Cdd-Cd)C=S",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cdd u0 {1,D} {6,D}
4   CS  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {8,D}
6   S2d u0 {3,D}
7   S2d u0 {4,D}
8   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 515,
    label = "Cds-CdsCbC=S",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   CS  u0 {1,S} {5,D}
3   Cd  u0 {1,D}
4   Cb  u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 516,
    label = "Cds-CdsCtC=S",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   CS  u0 {1,S} {5,D}
3   Cd  u0 {1,D}
4   Ct  u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 517,
    label = "Cds-CdsC=SCs",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   CS  u0 {1,S} {5,D}
3   Cd  u0 {1,D}
4   Cs  u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.21,4.51,4.77,4.99,5.4,5.66,5.98],'cal/(mol*K)'),
        H298 = (9.24,'kcal/mol'),
        S298 = (-11.25,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 518,
    label = "Cds-CdsC=S(Cds-Cd)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   CS  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {5,D}
4   Cd  u0 {1,D}
5   C   u0 {3,D}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 519,
    label = "Cds-CdsC=S(Cds-Cds)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   CS  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {5,D}
4   Cd  u0 {1,D}
5   Cd  u0 {3,D}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 520,
    label = "Cds-CdsC=S(Cds-Cdd)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   CS  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {5,D}
4   Cd  u0 {1,D}
5   Cdd u0 {3,D}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 521,
    label = "Cds-CdsC=S(Cds-Cdd-Cd)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {5,D}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Cd  u0 {1,D}
6   S2d u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 522,
    label = "Cds-CdsC=S(Cds-Cdd-S2d)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {5,D}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Cd  u0 {1,D}
6   S2d u0 {3,D}
7   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 523,
    label = "Cds-(Cdd-S2d)C=SC=S",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CS  u0 {1,S} {6,D}
4   CS  u0 {1,S} {7,D}
5   S2d u0 {2,D}
6   S2d u0 {3,D}
7   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 524,
    label = "Cds-CNH",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   N  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 525,
    label = "Cd-CdHN3s",
    group = 
"""
1 * Cd  u0 {2,D} {5,S} {6,S}
2   Cd  u0 {1,D} {3,S} {4,S}
3   R   u0 {2,S}
4   R   u0 {2,S}
5   H   u0 {1,S}
6   N3s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.7,6,7,7.7,8.8,9.5,10.6],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (2.2,'kcal/mol','+|-',1.4),
        S298 = (7.1,'cal/(mol*K)','+|-',1.3),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 526,
    label = "Cd-CdH(N5dcOdOs)",
    group = 
"""
1 * Cd   u0 {2,D} {3,S} {4,S}
2   Cd   u0 {1,D} {5,S} {6,S}
3   N5dc u0 {1,S} {7,D} {8,S}
4   H    u0 {1,S}
5   R    u0 {2,S}
6   R    u0 {2,S}
7   O2d  u0 {3,D}
8   O2s  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.7,15.4,17.6,19.3,21.7,23.1,25],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (2,'kcal/mol','+|-',1.3),
        S298 = (44.3,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 527,
    label = "Cds-CCN",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   C  u0 {1,S}
4   N  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 528,
    label = "Cd-CdCsN3s",
    group = 
"""
1 * Cd  u0 {2,D} {5,S} {6,S}
2   Cd  u0 {1,D} {3,S} {4,S}
3   R   u0 {2,S}
4   R   u0 {2,S}
5   Cs  u0 {1,S}
6   N3s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.8,5,5.9,6.4,6.9,7.1,7.2],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (3.5,'kcal/mol','+|-',1.4),
        S298 = (-14.1,'cal/(mol*K)','+|-',1.3),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 529,
    label = "Cd-CdCs(N5dcOdOs)",
    group = 
"""
1 * Cd   u0 {2,D} {3,S} {4,S}
2   Cd   u0 {1,D} {5,S} {6,S}
3   N5dc u0 {1,S} {7,D} {8,S}
4   Cs   u0 {1,S}
5   R    u0 {2,S}
6   R    u0 {2,S}
7   O2d  u0 {3,D}
8   O2s  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.1,14.3,16.1,17.5,19.3,20.3,21.4],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (2.3,'kcal/mol','+|-',1.3),
        S298 = (24,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 530,
    label = "C=S-SsSs",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 531,
    label = "C=S-CH",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S  u0 {1,D}
3   C  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = 'C=S-CsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 532,
    label = "C=S-CsH",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S  u0 {1,D}
3   Cs u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = 'C=S2-CsH',
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc = 
"""
"
""",
)

entry(
    index = 533,
    label = "C=S2-CsH",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.09,9.4,9.55,10.13,11.37,12.36,13.87],'cal/(mol*K)'),
        H298 = (24.14,'kcal/mol'),
        S298 = (36.84,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 534,
    label = "C=S4-CsH",
    group = 
"""
1 * CS         u0 {2,D} {3,S} {4,S}
2   [S4d,S4dd] u0 {1,D}
3   Cs         u0 {1,S}
4   H          u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.55,7.96,8.45,9.22,10.82,11.81,12.94],'cal/(mol*K)'),
        H298 = (16.51,'kcal/mol'),
        S298 = (38.28,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 535,
    label = "C=S-CdsH",
    group = 
"""
1 * CS      u0 {2,D} {3,S} {4,S}
2   S2d     u0 {1,D}
3   [Cd,Cb] u0 {1,S}
4   H       u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.41,9.18,10.55,11.53,12.8,13.57,14.62],'cal/(mol*K)'),
        H298 = (24.85,'kcal/mol'),
        S298 = (33.97,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 536,
    label = "C=S-(Cds-Cd)H",
    group = 
"""
1 * CS          u0 {2,S} {3,D} {4,S}
2   Cd          u0 {1,S} {5,D}
3   S2d         u0 {1,D}
4   H           u0 {1,S}
5   [Cd,Cdd,CO] u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 537,
    label = "C=S-(Cds-Cdd)H",
    group = 
"""
1 * CS  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   S2d u0 {1,D}
4   H   u0 {1,S}
5   Cdd u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 538,
    label = "C=S-(Cds-Cdd-Cd)H",
    group = 
"""
1 * CS  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   S2d u0 {1,D}
5   H   u0 {1,S}
6   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 539,
    label = "C=S-(Cds-Cdd-S2d)H",
    group = 
"""
1 * CS  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   S2d u0 {1,D}
5   H   u0 {1,S}
6   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 540,
    label = "C=S-(Cds-Cds)H",
    group = 
"""
1 * CS  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   S2d u0 {1,D}
4   H   u0 {1,S}
5   Cd  u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 541,
    label = "C=S-CtH",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   Ct  u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.07,8.97,10.47,10.17,11.38,12.33,13.6],'cal/(mol*K)'),
        H298 = (30.53,'kcal/mol'),
        S298 = (36.94,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 542,
    label = "C=S-C=SH",
    group = 
"""
1 * CS  u0 {2,S} {3,D} {4,S}
2   CS  u0 {1,S} {5,D}
3   S2d u0 {1,D}
4   H   u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.79,9.18,10.41,11.42,12.82,13.64,14.54],'cal/(mol*K)'),
        H298 = (26.96,'kcal/mol'),
        S298 = (35.65,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 543,
    label = "C=S-CC",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   C   u0 {1,S}
4   C   u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 544,
    label = "C=S-CbCds",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   Cb  u0 {1,S}
4   Cd  u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 545,
    label = "C=S-Cb(Cds-Cd)",
    group = 
"""
1 * CS          u0 {2,S} {3,D} {4,S}
2   Cd          u0 {1,S} {5,D}
3   S2d         u0 {1,D}
4   Cb          u0 {1,S}
5   [Cd,Cdd,CO] u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 546,
    label = "C=S-Cb(Cds-Cds)",
    group = 
"""
1 * CS  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   S2d u0 {1,D}
4   Cb  u0 {1,S}
5   Cd  u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 547,
    label = "C=S-Cb(Cds-Cdd)",
    group = 
"""
1 * CS  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   S2d u0 {1,D}
4   Cb  u0 {1,S}
5   Cdd u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 548,
    label = "C=S-Cb(Cds-Cdd-S2d)",
    group = 
"""
1 * CS  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   S2d u0 {1,D}
5   Cb  u0 {1,S}
6   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 549,
    label = "C=S-Cb(Cds-Cdd-Cd)",
    group = 
"""
1 * CS  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   S2d u0 {1,D}
5   Cb  u0 {1,S}
6   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 550,
    label = "C=S-CtCt",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   Ct  u0 {1,S}
4   Ct  u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 551,
    label = "C=S-CbCb",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 552,
    label = "C=S-CdsCds",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   Cd  u0 {1,S}
4   Cd  u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 553,
    label = "C=S-(Cds-Cd)(Cds-Cd)",
    group = 
"""
1 * CS          u0 {2,S} {3,S} {4,D}
2   Cd          u0 {1,S} {5,D}
3   Cd          u0 {1,S} {6,D}
4   S2d         u0 {1,D}
5   [Cd,Cdd,CO] u0 {2,D}
6   [Cd,Cdd,CO] u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 554,
    label = "C=S-(Cds-Cdd)(Cds-Cds)",
    group = 
"""
1 * CS  u0 {2,S} {3,S} {4,D}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   S2d u0 {1,D}
5   Cdd u0 {2,D}
6   Cd  u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 555,
    label = "C=S-(Cds-Cdd-Cd)(Cds-Cds)",
    group = 
"""
1 * CS  u0 {2,S} {3,S} {5,D}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {6,D}
4   Cdd u0 {2,D} {7,D}
5   S2d u0 {1,D}
6   Cd  u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 556,
    label = "C=S-(Cds-Cdd-S2d)(Cds-Cds)",
    group = 
"""
1 * CS  u0 {2,S} {3,S} {5,D}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {6,D}
4   Cdd u0 {2,D} {7,D}
5   S2d u0 {1,D}
6   Cd  u0 {3,D}
7   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 557,
    label = "C=S-(Cds-Cds)(Cds-Cds)",
    group = 
"""
1 * CS  u0 {2,S} {3,S} {4,D}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   S2d u0 {1,D}
5   Cd  u0 {2,D}
6   Cd  u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 558,
    label = "C=S-(Cds-Cdd)(Cds-Cdd)",
    group = 
"""
1 * CS  u0 {2,S} {3,S} {4,D}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   S2d u0 {1,D}
5   Cdd u0 {2,D}
6   Cdd u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 559,
    label = "C=S-(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1 * CS  u0 {2,S} {3,S} {6,D}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {7,D}
5   Cdd u0 {3,D} {8,D}
6   S2d u0 {1,D}
7   C   u0 {4,D}
8   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 560,
    label = "C=S-(Cds-Cdd-S2d)(Cds-Cdd-S2d)",
    group = 
"""
1 * CS  u0 {2,S} {3,S} {6,D}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {7,D}
5   Cdd u0 {3,D} {8,D}
6   S2d u0 {1,D}
7   S2d u0 {4,D}
8   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 561,
    label = "C=S-(Cds-Cdd-Cd)(Cds-Cdd-S2d)",
    group = 
"""
1 * CS  u0 {2,S} {3,S} {6,D}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {7,D}
5   Cdd u0 {3,D} {8,D}
6   S2d u0 {1,D}
7   C   u0 {4,D}
8   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 562,
    label = "C=S-CtCds",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   Ct  u0 {1,S}
4   Cd  u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 563,
    label = "C=S-Ct(Cds-Cd)",
    group = 
"""
1 * CS          u0 {2,S} {3,D} {4,S}
2   Cd          u0 {1,S} {5,D}
3   S2d         u0 {1,D}
4   Ct          u0 {1,S}
5   [Cd,Cdd,CO] u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 564,
    label = "C=S-Ct(Cds-Cds)",
    group = 
"""
1 * CS  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   S2d u0 {1,D}
4   Ct  u0 {1,S}
5   Cd  u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 565,
    label = "C=S-Ct(Cds-Cdd)",
    group = 
"""
1 * CS  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   S2d u0 {1,D}
4   Ct  u0 {1,S}
5   Cdd u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 566,
    label = "C=S-Ct(Cds-Cdd-Cd)",
    group = 
"""
1 * CS  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   S2d u0 {1,D}
5   Ct  u0 {1,S}
6   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 567,
    label = "C=S-Ct(Cds-Cdd-S2d)",
    group = 
"""
1 * CS  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   S2d u0 {1,D}
5   Ct  u0 {1,S}
6   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 568,
    label = "C=S-CbCt",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   Cb  u0 {1,S}
4   Ct  u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 569,
    label = "C=S-CsCs",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.64,8.16,7.45,7.69,8.72,9.5,10.5],'cal/(mol*K)'),
        H298 = (20.9,'kcal/mol'),
        S298 = (16.55,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 570,
    label = "C=S-CdsCs",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   Cd  u0 {1,S}
4   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.58,9.38,9.53,9.87,10.47,10.79,11.17],'cal/(mol*K)'),
        H298 = (23.84,'kcal/mol'),
        S298 = (12.34,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""

""",
)

entry(
    index = 571,
    label = "C=S-(Cds-Cd)Cs",
    group = 
"""
1 * CS          u0 {2,S} {3,D} {4,S}
2   Cd          u0 {1,S} {5,D}
3   S2d         u0 {1,D}
4   Cs          u0 {1,S}
5   [Cd,Cdd,CO] u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 572,
    label = "C=S-(Cds-Cds)Cs",
    group = 
"""
1 * CS  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   S2d u0 {1,D}
4   Cs  u0 {1,S}
5   Cd  u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 573,
    label = "C=S-(Cds-Cdd)Cs",
    group = 
"""
1 * CS  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   S2d u0 {1,D}
4   Cs  u0 {1,S}
5   Cdd u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 574,
    label = "C=S-(Cds-Cdd-S2d)Cs",
    group = 
"""
1 * CS  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   S2d u0 {1,D}
5   Cs  u0 {1,S}
6   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 575,
    label = "C=S-(Cds-Cdd-Cd)Cs",
    group = 
"""
1 * CS  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   S2d u0 {1,D}
5   Cs  u0 {1,S}
6   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 576,
    label = "C=S-CtCs",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   Ct  u0 {1,S}
4   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.44,8.3,8.72,7.99,8.85,9.55,10.38],'cal/(mol*K)'),
        H298 = (26.63,'kcal/mol'),
        S298 = (16.54,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""

""",
)

entry(
    index = 577,
    label = "C=S-CbCs",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   Cb  u0 {1,S}
4   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.94,8.73,9,9.46,10.17,10.53,10.9],'cal/(mol*K)'),
        H298 = (23.58,'kcal/mol'),
        S298 = (13.65,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 578,
    label = "C=S-C=SCs",
    group = 
"""
1 * CS  u0 {2,S} {3,D} {4,S}
2   CS  u0 {1,S} {5,D}
3   S2d u0 {1,D}
4   Cs  u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.9,8.29,8.4,8.85,9.71,10.22,10.71],'cal/(mol*K)'),
        H298 = (24.34,'kcal/mol'),
        S298 = (15.85,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 579,
    label = "C=S-CtC=S",
    group = 
"""
1 * CS  u0 {2,S} {3,D} {4,S}
2   CS  u0 {1,S} {5,D}
3   S2d u0 {1,D}
4   Ct  u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 580,
    label = "C=S-(Cds-Cd)C=S",
    group = 
"""
1 * CS  u0 {2,S} {3,D} {4,S}
2   CS  u0 {1,S} {5,D}
3   S2d u0 {1,D}
4   Cd  u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 581,
    label = "C=S-(Cds-Cdd)C=S",
    group = 
"""
1 * CS  u0 {2,S} {3,S} {4,D}
2   Cd  u0 {1,S} {5,D}
3   CS  u0 {1,S} {6,D}
4   S2d u0 {1,D}
5   Cdd u0 {2,D}
6   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 582,
    label = "C=S-(Cds-Cdd-Cd)C=S",
    group = 
"""
1 * CS  u0 {2,S} {3,S} {5,D}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {6,D}
5   S2d u0 {1,D}
6   C   u0 {4,D}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 583,
    label = "C=S-(Cds-Cdd-S2d)C=S",
    group = 
"""
1 * CS  u0 {2,S} {3,S} {5,D}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {6,D}
5   S2d u0 {1,D}
6   S2d u0 {4,D}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 584,
    label = "C=S-(Cds-Cds)C=S",
    group = 
"""
1 * CS  u0 {2,S} {3,S} {4,D}
2   Cd  u0 {1,S} {5,D}
3   CS  u0 {1,S} {6,D}
4   S2d u0 {1,D}
5   Cd  u0 {2,D}
6   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 585,
    label = "C=S-C=SC=S",
    group = 
"""
1 * CS  u0 {2,S} {3,S} {4,D}
2   CS  u0 {1,S} {5,D}
3   CS  u0 {1,S} {6,D}
4   S2d u0 {1,D}
5   S2d u0 {2,D}
6   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 586,
    label = "C=S-CbC=S",
    group = 
"""
1 * CS  u0 {2,S} {3,D} {4,S}
2   CS  u0 {1,S} {5,D}
3   S2d u0 {1,D}
4   Cb  u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 587,
    label = "C=S-HH",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S  u0 {1,D}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = 'C=S2d-HH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 588,
    label = "C=S2d-HH",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.08,10.35,11.52,12.5,14.08,15.25,17.14],'cal/(mol*K)'),
        H298 = (27.7,'kcal/mol'),
        S298 = (56.5,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 589,
    label = "C=S4d-HH",
    group = 
"""
1 * CS         u0 {2,D} {3,S} {4,S}
2   [S4d,S4dd] u0 {1,D}
3   H          u0 {1,S}
4   H          u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.82,9.96,10.83,11.76,13.57,14.92,16.57],'cal/(mol*K)'),
        H298 = (16.47,'kcal/mol'),
        S298 = (57.73,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 590,
    label = "C=S6dd-HH",
    group = 
"""
1 * CS   u0 {2,D} {3,S} {4,S}
2   S6dd u0 {1,D}
3   H    u0 {1,S}
4   H    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.79,11.27,12.37,13.22,14.74,15.89,17.4],'cal/(mol*K)'),
        H298 = (14.2,'kcal/mol'),
        S298 = (54.75,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 591,
    label = "C=S6ddd-HH",
    group = 
"""
1 * CS           u0 {2,D} {3,S} {4,S}
2   [S6ddd,S6td] u0 {1,D}
3   H            u0 {1,S}
4   H            u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.85,10.47,11.15,12.02,14.01,15.34,17.31],'cal/(mol*K)'),
        H298 = (10.97,'kcal/mol'),
        S298 = (52.97,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 592,
    label = "C=S-SH",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S  u0 {1,D}
3   S  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = 'C=S-S2H',
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc = 
"""
"
""",
)

entry(
    index = 593,
    label = "C=S-S2H",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   S2s u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.85,10.7,11.13,11.7,14.22,15.76,15.35],'cal/(mol*K)'),
        H298 = (30.11,'kcal/mol'),
        S298 = (39.21,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 594,
    label = "C=S-S4H",
    group = 
"""
1 * CS                u0 {2,D} {3,S} {4,S}
2   S2d               u0 {1,D}
3   [S4s,S4d,S4b,S4t] u0 {1,S}
4   H                 u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.98,9.29,9.55,10.22,13.01,14.82,15.15],'cal/(mol*K)'),
        H298 = (45.35,'kcal/mol'),
        S298 = (42.42,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 595,
    label = "C=S-S6H",
    group = 
"""
1 * CS                      u0 {2,D} {3,S} {4,S}
2   S2d                     u0 {1,D}
3   [S6s,S6d,S6dd,S6t,S6td] u0 {1,S}
4   H                       u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.5,9.98,11.08,11.93,13.14,13.95,15.08],'cal/(mol*K)'),
        H298 = (21.69,'kcal/mol'),
        S298 = (34.23,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc = 
"""
"
""",
)

entry(
    index = 596,
    label = "C=S6-S2H",
    group = 
"""
1 * CS                    u0 {2,D} {3,S} {4,S}
2   [S6d,S6dd,S6ddd,S6td] u0 {1,D}
3   S2s                   u0 {1,S}
4   H                     u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.67,15.3,16,16.78,20.51,22.83,21.04],'cal/(mol*K)'),
        H298 = (32.31,'kcal/mol'),
        S298 = (64.82,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 597,
    label = "C=S-CSs",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S  u0 {1,D}
3   C  u0 {1,S}
4   S  u0 {1,S}
""",
    thermo = 'C=S-CsSs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 598,
    label = "C=S-CbSs",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   Cb  u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 599,
    label = "C=S-CdsSs",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   Cd  u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 600,
    label = "C=S-(Cds-Cd)S2s",
    group = 
"""
1 * CS          u0 {2,S} {3,D} {4,S}
2   Cd          u0 {1,S} {5,D}
3   S2d         u0 {1,D}
4   S2s         u0 {1,S}
5   [Cd,Cdd,CO] u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 601,
    label = "C=S-(Cds-Cds)S2s",
    group = 
"""
1 * CS  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   S2d u0 {1,D}
4   S2s u0 {1,S}
5   Cd  u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 602,
    label = "C=S-(Cds-Cdd)S2s",
    group = 
"""
1 * CS  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   S2d u0 {1,D}
4   S2s u0 {1,S}
5   Cdd u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 603,
    label = "C=S-(Cds-Cdd-Cd)S2s",
    group = 
"""
1 * CS  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   S2d u0 {1,D}
5   S2s u0 {1,S}
6   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 604,
    label = "C=S-(Cds-Cdd-S2d)S2s",
    group = 
"""
1 * CS  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   S2d u0 {1,D}
5   S2s u0 {1,S}
6   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 605,
    label = "C=S-S(CO)",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   CO  u0 {1,S}
4   S   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.4,8.38,9.16,9.8,10.72,11.25,11.66],'cal/(mol*K)'),
        H298 = (21.35,'kcal/mol'),
        S298 = (14.52,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 606,
    label = "C=S-CtSs",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   Ct  u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 607,
    label = "C=S-CsSs",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   Cs  u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.76,9.54,8.97,9.22,11.6,13.02,12.13],'cal/(mol*K)'),
        H298 = (26.79,'kcal/mol'),
        S298 = (18.82,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""

""",
)

entry(
    index = 608,
    label = "C=S-C=SSs",
    group = 
"""
1 * CS  u0 {2,S} {3,D} {4,S}
2   CS  u0 {1,S} {5,D}
3   S2d u0 {1,D}
4   S2s u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 609,
    label = "Cds-CdClH",
    group = 
"""
1 * Cd   u0 {2,D} {3,S} {4,S}
2   C    u0 {1,D}
3   Cl1s u0 {1,S}
4   H    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.9,9.2,10.3,11.2,12.3,13.1,14.25],'cal/(mol*K)'),
        H298 = (-1.2,'kcal/mol'),
        S298 = (35.4,'cal/(mol*K)'),
    ),
    shortDesc = """CD/Cl/H CHEN AND BOZZELLI""",
    longDesc = 
"""
Chinugh-Ju Chen, D. Wong, Joseph W. Bozzelli,
Standard Chemical Thermodynamic Properties of Multichloro Alkanes and Alkenes: A Modified Group Additivity Scheme
JPCA, 1998, 102, 4551-4558
""",
)

entry(
    index = 610,
    label = "Cds-CdIH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   C   u0 {1,D}
3   I1s u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.8,10,10.9,11.6,12.6,13.3,14],'cal/(mol*K)'),
        H298 = (24.5,'kcal/mol'),
        S298 = (40.5,'cal/(mol*K)'),
    ),
    shortDesc = """Cd-(I)(H) BENSON""",
    longDesc = 
"""
Thermochemical Kinetics 2nd Ed., by Sidney Benson (Table A4, p.280)
Cpdata at 1500K was not in the book, Cpdata at 1500K = Cpdata at 1000K + 0.7
""",
)

entry(
    index = 611,
    label = "Cds-CdClCl",
    group = 
"""
1 * Cd   u0 {2,D} {3,S} {4,S}
2   C    u0 {1,D}
3   Cl1s u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.97,12.42,13.33,13.92,14.63,15.01,15.44],'cal/(mol*K)'),
        H298 = (-5.76,'kcal/mol'),
        S298 = (40.77,'cal/(mol*K)'),
    ),
    shortDesc = """CD/Cl2 CHEN AND BOZZELLI""",
    longDesc = 
"""
Chinugh-Ju Chen, D. Wong, Joseph W. Bozzelli,
Standard Chemical Thermodynamic Properties of Multichloro Alkanes and Alkenes: A Modified Group Additivity Scheme
JPCA, 1998, 102, 4551-4558
""",
)

entry(
    index = 612,
    label = "Cds-CdClC",
    group = 
"""
1 * Cd   u0 {2,D} {3,S} {4,S}
2   Cd   u0 {1,D}
3   Cl1s u0 {1,S}
4   C    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8,8.4,8.5,9,9.2,9.4,9.57],'cal/(mol*K)'),
        H298 = (-2.1,'kcal/mol'),
        S298 = (15,'cal/(mol*K)'),
    ),
    shortDesc = """CD/C/Cl CHEN AND BOZZELLI""",
    longDesc = 
"""
Chinugh-Ju Chen, D. Wong, Joseph W. Bozzelli,
Standard Chemical Thermodynamic Properties of Multichloro Alkanes and Alkenes: A Modified Group Additivity Scheme
JPCA, 1998, 102, 4551-4558
""",
)

entry(
    index = 613,
    label = "Cds-CdClCd",
    group = 
"""
1 * Cd   u0 {2,D} {3,S} {4,S}
2   Cd   u0 {1,D}
3   Cl1s u0 {1,S}
4   Cd   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.23,8.86,9.66,10.26,10.96,11.28,11.52],'cal/(mol*K)'),
        H298 = (-13.76,'kcal/mol'),
        S298 = (14.47,'cal/(mol*K)'),
    ),
    shortDesc = """CD/CD/Cl CHEN AND BOZZELLI""",
    longDesc = 
"""
Chinugh-Ju Chen, D. Wong, Joseph W. Bozzelli,
Standard Chemical Thermodynamic Properties of Multichloro Alkanes and Alkenes: A Modified Group Additivity Scheme
JPCA, 1998, 102, 4551-4558
""",
)

entry(
    index = 614,
    label = "C=S-OsH",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   S   u0 {1,D}
3   O2s u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = 'C=S2-OsH',
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc = 
"""
"
""",
)

entry(
    index = 615,
    label = "C=S2-OsH",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   O2s u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.1,10.53,11.43,12.21,13.48,14.27,15.01],'cal/(mol*K)'),
        H298 = (19.05,'kcal/mol'),
        S298 = (34.45,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 616,
    label = "C=S4-OsH",
    group = 
"""
1 * CS         u0 {2,D} {3,S} {4,S}
2   [S4d,S4dd] u0 {1,D}
3   O2s        u0 {1,S}
4   H          u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.67,8.18,9.52,10.9,13.34,14.97,16.45],'cal/(mol*K)'),
        H298 = (9.61,'kcal/mol'),
        S298 = (32.61,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 617,
    label = "C=S-CsOs",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   O2s u0 {1,S}
4   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.55,9.84,9.67,10.07,11.21,11.91,12.2],'cal/(mol*K)'),
        H298 = (11.72,'kcal/mol'),
        S298 = (12.22,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""

""",
)

entry(
    index = 618,
    label = "C=S-OsOs",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.25,13.98,14.47,14.69,14.74,14.19,12.39],'cal/(mol*K)'),
        H298 = (9.69,'kcal/mol'),
        S298 = (11.28,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""

""",
)

entry(
    index = 619,
    label = "C=S-OsS",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   O2s u0 {1,S}
4   S   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.39,10.42,10.78,11.43,14.16,15.66,14.34],'cal/(mol*K)'),
        H298 = (36.94,'kcal/mol'),
        S298 = (16.85,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""

""",
)

entry(
    index = 620,
    label = "Cs",
    group = 
"""
1 * Cs u0
""",
    thermo = 'Cs-CsCsCsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 621,
    label = "Cs-NHHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   N  u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 622,
    label = "Cs-N3sHHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3s u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.19,7.84,9.4,10.79,13.02,14.77,17.58],'cal/(mol*K)'),
        H298 = (-10.08,'kcal/mol'),
        S298 = (30.41,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 623,
    label = "Cs-N3dHHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3d u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 624,
    label = "Cs-(N3dCd)HHH",
    group = 
"""
1 * Cs       u0 {2,S} {3,S} {4,S} {5,S}
2   N3d      u0 {1,S} {6,D}
3   H        u0 {1,S}
4   H        u0 {1,S}
5   H        u0 {1,S}
6   [Cd,Cdd] u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6,7.7,9.3,10.7,13.1,14.8,17.7],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-5.7,'kcal/mol','+|-',1.3),
        S298 = (30.4,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 625,
    label = "Cs-(N3dN3d)HHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3d u0 {1,S} {6,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   N3d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6,7.8,9.4,10.8,13.1,14.8,17.6],'cal/(mol*K)','+|-',[0.6,0.6,0.6,0.6,0.6,0.6,0.6]),
        H298 = (-9,'kcal/mol','+|-',0.8),
        S298 = (30.2,'cal/(mol*K)','+|-',0.8),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 626,
    label = "Cs-NCsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   N  u0 {1,S}
3   Cs u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 627,
    label = "Cs-N3sCsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3s u0 {1,S}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.25,6.9,8.28,9.39,11.09,12.34,14.8],'cal/(mol*K)'),
        H298 = (-6.6,'kcal/mol'),
        S298 = (9.8,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 628,
    label = "Cs-N3dCHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3d u0 {1,S}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 629,
    label = "Cs-(N3dN3d)CsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3d u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   N3d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.3,6.9,8.3,9.4,11.1,12.3,14.2],'cal/(mol*K)','+|-',[0.6,0.6,0.6,0.6,0.6,0.6,0.6]),
        H298 = (-5.5,'kcal/mol','+|-',0.8),
        S298 = (9.4,'cal/(mol*K)','+|-',0.8),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 630,
    label = "Cs-(N3dOd)CHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3d u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.8,13.6,15.2,16.7,18.9,20.5,23],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (21.4,'kcal/mol','+|-',1.3),
        S298 = (44.3,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 631,
    label = "Cs-(N3dCd)CsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3d u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   Cd  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.3,7.2,8.7,9.8,11.6,12.8,14.7],'cal/(mol*K)','+|-',[1.2,1.2,1.2,1.2,1.2,1.2,1.2]),
        H298 = (-2.9,'kcal/mol','+|-',1.7),
        S298 = (8.6,'cal/(mol*K)','+|-',1.6),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 632,
    label = "Cs-N5dcCsHH",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   N5dc u0 {1,S}
3   Cs   u0 {1,S}
4   H    u0 {1,S}
5   H    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 633,
    label = "Cs-(N5dcOdOs)CsHH",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   N5dc u0 {1,S} {6,D} {7,S}
3   Cs   u0 {1,S}
4   H    u0 {1,S}
5   H    u0 {1,S}
6   O2d  u0 {2,D}
7   O2s  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.9,15.8,18.3,20.3,23.3,25.4,28.3],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-14.8,'kcal/mol','+|-',1.3),
        S298 = (48.9,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 634,
    label = "Cs-NCsCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   N  u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 635,
    label = "Cs-N3sCsCsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3s u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.67,6.32,7.64,8.39,9.56,10.23,11.905],'cal/(mol*K)'),
        H298 = (-5.2,'kcal/mol'),
        S298 = (-11.7,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 636,
    label = "Cs-N3dCsCsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3d u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 637,
    label = "Cs-(N3dOd)CsCsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3d u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.2,12.7,14,15.1,16.8,17.9,19.5],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (23.4,'kcal/mol','+|-',1.3),
        S298 = (23.1,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 638,
    label = "Cs-(N3dN3d)CsCsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   N3d u0 {1,S} {3,D}
3   N3d u0 {2,D}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (-3.3,'kcal/mol'),
        S298 = (-11.7,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 639,
    label = "Cs-N5dcCsCsH",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   N5dc u0 {1,S}
3   Cs   u0 {1,S}
4   Cs   u0 {1,S}
5   H    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 640,
    label = "Cs-(N5dcOdOs)CsCsH",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   N5dc u0 {1,S} {6,D} {7,S}
3   Cs   u0 {1,S}
4   Cs   u0 {1,S}
5   H    u0 {1,S}
6   O2d  u0 {2,D}
7   O2s  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.6,16.1,18.1,19.6,21.8,23.2,25.1],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-13.9,'kcal/mol','+|-',1.3),
        S298 = (27.5,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 641,
    label = "Cs-NCsCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   N  u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 642,
    label = "Cs-N3sCsCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3s u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.35,6.16,7.31,7.91,8.49,8.5,8.525],'cal/(mol*K)'),
        H298 = (-3.2,'kcal/mol'),
        S298 = (-34.1,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 643,
    label = "Cs-N3dCsCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3d u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 644,
    label = "Cs-(N3dOd)CsCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3d u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.2,13.3,14,14.5,15.3,15.7,16.2],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (24.1,'kcal/mol','+|-',1.3),
        S298 = (1.2,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 645,
    label = "Cs-(N3dN3d)CsCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   N3d u0 {1,S} {3,D}
3   N3d u0 {2,D}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (-1.9,'kcal/mol'),
        S298 = (-34.7,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 646,
    label = "Cs-N5dcCsCsCs",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   N5dc u0 {1,S}
3   Cs   u0 {1,S}
4   Cs   u0 {1,S}
5   Cs   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 647,
    label = "Cs-(N5dcOdOs)CsCsCs",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   N5dc u0 {1,S} {6,D} {7,S}
3   Cs   u0 {1,S}
4   Cs   u0 {1,S}
5   Cs   u0 {1,S}
6   O2d  u0 {2,D}
7   O2s  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.5,16,17.8,18.9,20.3,21.1,21.9],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-12.7,'kcal/mol','+|-',1.3),
        S298 = (5.2,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 648,
    label = "Cs-NNCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   N  u0 {1,S}
3   N  u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 649,
    label = "Cs-N5dcN5dcCsCs",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   N5dc u0 {1,S}
3   N5dc u0 {1,S}
4   Cs   u0 {1,S}
5   Cs   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 650,
    label = "Cs-NNCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   N  u0 {1,S}
3   N  u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 651,
    label = "Cs-(N5dcOdOs)(N5dcOdOs)CsH",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   N5dc u0 {1,S} {6,D} {7,S}
3   N5dc u0 {1,S} {8,D} {9,S}
4   Cs   u0 {1,S}
5   H    u0 {1,S}
6   O2d  u0 {2,D}
7   O2s  u0 {2,S}
8   O2d  u0 {3,D}
9   O2s  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (-14.9,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 652,
    label = "Cs-HHHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   H  u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.43,9.84,11.14,12.41,15,17.25,20.63],'cal/(mol*K)','+|-',[0.06,0.06,0.06,0.06,0.06,0.06,0.06]),
        H298 = (-17.9,'kcal/mol','+|-',0.1),
        S298 = (49.41,'cal/(mol*K)','+|-',0.05),
    ),
    shortDesc = """CHEMKIN DATABASE S(group) = S(CH4) + Rln(12)""",
    longDesc = 
"""

""",
)

entry(
    index = 653,
    label = "Cs-CHHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = 'Cs-CsHHH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 654,
    label = "Cs-CsHHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.19,7.84,9.4,10.79,13.02,14.77,17.58],'cal/(mol*K)','+|-',[0.08,0.08,0.08,0.08,0.08,0.08,0.08]),
        H298 = (-10.2,'kcal/mol','+|-',0.12),
        S298 = (30.41,'cal/(mol*K)','+|-',0.08),
    ),
    shortDesc = """Cs-CsHHH BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 655,
    label = "Cs-CdsHHH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   H       u0 {1,S}
4   H       u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)HHH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 656,
    label = "Cs-(Cds-O2d)HHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.31,32.07,38.44,44.06,53.36,60.63,72.47],'J/(mol*K)'),
        H298 = (-42.9,'kJ/mol'),
        S298 = (127.12,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 657,
    label = "Cs-(Cds-Cd)HHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)HHH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 658,
    label = "Cs-(Cds-Cds)HHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.19,7.84,9.4,10.79,13.02,14.77,17.58],'cal/(mol*K)','+|-',[0.04,0.04,0.04,0.04,0.04,0.04,0.04]),
        H298 = (-10.2,'kcal/mol','+|-',0.08),
        S298 = (30.41,'cal/(mol*K)','+|-',0.04),
    ),
    shortDesc = """Cs-CdHHH BENSON (Assigned Cs-CsHHH)""",
    longDesc = 
"""

""",
)

entry(
    index = 659,
    label = "Cs-(Cds-Cdd)HHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)HHH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 660,
    label = "Cs-(Cds-Cdd-O2d)HHH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.31,32.07,38.44,44.06,53.36,60.63,72.47],'J/(mol*K)'),
        H298 = (-42.9,'kJ/mol'),
        S298 = (127.12,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 661,
    label = "Cs-(Cds-Cdd-S2d)HHH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 662,
    label = "Cs-(Cds-Cdd-Cd)HHH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)HHH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 663,
    label = "Cs-(CdN3d)HHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   N3d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.2,7.8,9.4,10.8,13,14.8,17.6],'cal/(mol*K)'),
        H298 = (-10.2,'kcal/mol'),
        S298 = (30.4,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 664,
    label = "Cs-CtHHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.19,7.84,9.4,10.79,13.02,14.77,17.58],'cal/(mol*K)','+|-',[0.08,0.08,0.08,0.08,0.08,0.08,0.08]),
        H298 = (-10.2,'kcal/mol','+|-',0.15),
        S298 = (30.41,'cal/(mol*K)','+|-',0.08),
    ),
    shortDesc = """Cs-CtHHH BENSON (Assigned Cs-CsHHH)""",
    longDesc = 
"""

""",
)

entry(
    index = 665,
    label = "Cs-(CtN3t)HHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S} {6,T}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   N3t u0 {2,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.5,14.6,16.6,18.3,21.1,23.4,26.9],'cal/(mol*K)','+|-',[1.3,1.3,1.3,1.3,1.3,1.3,1.3]),
        H298 = (17.7,'kcal/mol','+|-',1.9),
        S298 = (60.2,'cal/(mol*K)','+|-',1.7),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 666,
    label = "Cs-CbHHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.19,7.84,9.4,10.79,13.02,14.77,17.58],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-10.2,'kcal/mol','+|-',0.18),
        S298 = (30.41,'cal/(mol*K)','+|-',0.14),
    ),
    shortDesc = """Cs-CbHHH BENSON (Assigned Cs-CsHHH)""",
    longDesc = 
"""

""",
)

entry(
    index = 667,
    label = "Cs-C=SHHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.99,7.23,9.48,11.01,13.13,14.7,17.27],'cal/(mol*K)'),
        H298 = (-7.1,'kcal/mol'),
        S298 = (31.12,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 668,
    label = "Cs-OsHHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.31,32.07,38.44,44.06,53.36,60.63,72.47],'J/(mol*K)'),
        H298 = (-42.9,'kJ/mol'),
        S298 = (127.12,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 669,
    label = "Cs-OsOsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S}
3   O2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.35,43.68,53.55,58.15,60.86,61.66,63.53],'J/(mol*K)','+|-',[5.77,5.77,5.77,5.77,5.77,5.77,5.77]),
        H298 = (-67.5,'kJ/mol','+|-',4.92),
        S298 = (17.89,'J/(mol*K)','+|-',6.74),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 670,
    label = "Cs-OsOsOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.54,6,7.17,8.05,9.31,10.05,10.05],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-21.23,'kcal/mol','+|-',0.2),
        S298 = (-12.07,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = """Cs-OOOH BOZZELLI del C/C2/O - C/C3/O, series !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
"""

""",
)

entry(
    index = 671,
    label = "Cs-OsSHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S}
3   S   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = 'Cs-OsS2HH',
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc = 
"""
"
""",
)

entry(
    index = 672,
    label = "Cs-OsS2HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S}
3   S2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.61,10.2,11.36,12.27,14.72,16.15,15.88],'cal/(mol*K)'),
        H298 = (3.32,'kcal/mol'),
        S298 = (11.26,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 673,
    label = "Cs-OsS4HH",
    group = 
"""
1 * Cs                u0 {2,S} {3,S} {4,S} {5,S}
2   O2s               u0 {1,S}
3   [S4s,S4d,S4b,S4t] u0 {1,S}
4   H                 u0 {1,S}
5   H                 u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.97,7.92,9.33,10.67,14.39,16.61,16.95],'cal/(mol*K)'),
        H298 = (5.62,'kcal/mol'),
        S298 = (8.3,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 674,
    label = "Cs-OsSSH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S}
3   S   u0 {1,S}
4   S   u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = 'Cs-OsS2S2H',
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc = 
"""
"
""",
)

entry(
    index = 675,
    label = "Cs-OsS2S2H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.48,8.15,9.41,10.4,11.71,12.83,14.46],'cal/(mol*K)'),
        H298 = (-10.34,'kcal/mol'),
        S298 = (6.83,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc = 
"""
"
""",
)

entry(
    index = 676,
    label = "Cs-OsS4S2H",
    group = 
"""
1 * Cs                u0 {2,S} {3,S} {4,S} {5,S}
2   O2s               u0 {1,S}
3   S2s               u0 {1,S}
4   [S4s,S4d,S4b,S4t] u0 {1,S}
5   H                 u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.61,9,10.51,11.92,16.57,18.75,16.38],'cal/(mol*K)'),
        H298 = (19.45,'kcal/mol'),
        S298 = (-12.67,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 677,
    label = "Cs-OsOsSH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S}
3   O2s u0 {1,S}
4   S   u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = 'Cs-OsOsS2H',
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc = 
"""
"
""",
)

entry(
    index = 678,
    label = "Cs-OsOsS2H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S}
3   O2s u0 {1,S}
4   S2s u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.28,9.26,10.65,11.64,14.06,15.03,13.66],'cal/(mol*K)'),
        H298 = (-3.58,'kcal/mol'),
        S298 = (-10.1,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 679,
    label = "Cs-OsOsS4H",
    group = 
"""
1 * Cs                u0 {2,S} {3,S} {4,S} {5,S}
2   O2s               u0 {1,S}
3   O2s               u0 {1,S}
4   [S4s,S4d,S4b,S4t] u0 {1,S}
5   H                 u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.65,7.55,8.69,9.85,13.15,14.98,14.49],'cal/(mol*K)'),
        H298 = (-3.81,'kcal/mol'),
        S298 = (-12.44,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 680,
    label = "Cs-SsHHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   S  u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = 'Cs-S2sHHH',
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 681,
    label = "Cs-S2sHHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   S2s u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.68,8.89,10.23,11.52,14.91,17.19,18.48],'cal/(mol*K)'),
        H298 = (1.96,'kcal/mol'),
        S298 = (35.84,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 682,
    label = "Cs-S4HHH",
    group = 
"""
1 * Cs                u0 {2,S} {3,S} {4,S} {5,S}
2   [S4s,S4d,S4b,S4t] u0 {1,S}
3   H                 u0 {1,S}
4   H                 u0 {1,S}
5   H                 u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.48,6.85,8.1,9.45,13.61,16.46,18.29],'cal/(mol*K)'),
        H298 = (5.53,'kcal/mol'),
        S298 = (33.83,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 683,
    label = "Cs-S6HHH",
    group = 
"""
1 * Cs                      u0 {2,S} {3,S} {4,S} {5,S}
2   [S6s,S6d,S6dd,S6t,S6td] u0 {1,S}
3   H                       u0 {1,S}
4   H                       u0 {1,S}
5   H                       u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.93,7.19,8.82,10.34,13.83,16.2,18.09],'cal/(mol*K)'),
        H298 = (-0.84,'kcal/mol'),
        S298 = (41.29,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 684,
    label = "Cs-SsSsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   S  u0 {1,S}
3   S  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.04,11.14,12.08,12.95,16.92,19,17.34],'cal/(mol*K)'),
        H298 = (19.1,'kcal/mol'),
        S298 = (16.46,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 685,
    label = "Cs-SsSsSsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   S  u0 {1,S}
3   S  u0 {1,S}
4   S  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.14,12.16,12.79,13.27,17.74,19.66,15.75],'cal/(mol*K)'),
        H298 = (36.14,'kcal/mol'),
        S298 = (-0.63,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 686,
    label = "Cs-CCHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = 'Cs-CsCsHH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 687,
    label = "Cs-CsCsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.5,6.95,8.25,9.35,11.07,12.34,14.25],'cal/(mol*K)','+|-',[0.04,0.04,0.04,0.04,0.04,0.04,0.04]),
        H298 = (-4.93,'kcal/mol','+|-',0.05),
        S298 = (9.42,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = """Cs-CsCsHH BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 688,
    label = "Cs-CdsCsHH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   Cs      u0 {1,S}
4   H       u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CsHH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 689,
    label = "Cs-(Cds-O2d)CsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.91,30.8,34.98,38.91,45.56,50.73,58.93],'J/(mol*K)','+|-',[1.53,1.53,1.53,1.53,1.53,1.53,1.53]),
        H298 = (-21.5,'kJ/mol','+|-',1.3),
        S298 = (40.32,'J/(mol*K)','+|-',1.78),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 690,
    label = "Cs-(Cds-Cd)CsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)CsHH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 691,
    label = "Cs-(Cds-Cds)CsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.12,6.86,8.32,9.49,11.22,12.48,14.36],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-4.76,'kcal/mol','+|-',0.16),
        S298 = (9.8,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = """Cs-CdCsHH BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 692,
    label = "Cs-(Cds-Cdd)CsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CsHH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 693,
    label = "Cs-(Cds-Cdd-O2d)CsHH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.35,6.83,8.25,9.45,11.19,12.46,14.34],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-5.723,'kcal/mol','+|-',0.16),
        S298 = (9.37,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = """{C/C/H2/CCO} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
"""

""",
)

entry(
    index = 694,
    label = "Cs-(Cds-Cdd-S2d)CsHH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 695,
    label = "Cs-(Cds-Cdd-Cd)CsHH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)CsHH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 696,
    label = "Cs-(CdN3d)CsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D} {7,S}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   N3d u0 {2,D}
7   R   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.5,6.9,8.1,9.2,10.9,12.2,14.1],'cal/(mol*K)','+|-',[1.2,1.2,1.2,1.2,1.2,1.2,1.2]),
        H298 = (-5.1,'kcal/mol','+|-',1.7),
        S298 = (10.1,'cal/(mol*K)','+|-',1.6),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 697,
    label = "Cs-CdsCdsHH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   H       u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)HH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 698,
    label = "Cs-(Cds-O2d)(Cds-O2d)HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   CO  u0 {1,S} {7,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.77,32.81,37.1,40.67,46.39,50.85,58.25],'J/(mol*K)','+|-',[4.19,4.19,4.19,4.19,4.19,4.19,4.19]),
        H298 = (-10,'kJ/mol','+|-',3.57),
        S298 = (40.1,'J/(mol*K)','+|-',4.88),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 699,
    label = "Cs-(Cds-O2d)(Cds-Cd)HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   C   u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([24.94,31.41,36.47,40.49,46.72,51.49,59.29],'J/(mol*K)','+|-',[3.34,3.34,3.34,3.34,3.34,3.34,3.34]),
        H298 = (-16.9,'kJ/mol','+|-',2.85),
        S298 = (40.18,'J/(mol*K)','+|-',3.9),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 700,
    label = "Cs-(Cds-O2d)(Cds-Cds)HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   Cd  u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.75,7.11,8.92,10.32,12.16,13.61,13.61],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-3.8,'kcal/mol','+|-',0.16),
        S298 = (6.31,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = """Cs-COCdHH BENSON Hf, Mopac =3D S,Cp nov99 !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
"""

""",
)

entry(
    index = 701,
    label = "Cs-(Cds-O2d)(Cds-Cdd)HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cdd-Cd)HH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 702,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   O2d u0 {3,D}
8   O2d u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)CsHH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 703,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   O2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)HH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 704,
    label = "Cs-(Cds-Cd)(Cds-Cd)HH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)HH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 705,
    label = "Cs-(Cds-Cds)(Cds-Cds)HH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.7,6.8,8.4,9.6,11.3,12.6,14.4],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-4.29,'kcal/mol','+|-',0.16),
        S298 = (10.2,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = """Cs-CdCdHH BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 706,
    label = "Cs-(Cds-Cdd)(Cds-Cds)HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cds)HH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 707,
    label = "Cs-Cd(CCO)HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   Cd  u0 {3,D}
8   O2d u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.85,31.99,37.06,41.14,47.42,52.15,59.73],'J/(mol*K)','+|-',[6.93,6.93,6.93,6.93,6.93,6.93,6.93]),
        H298 = (-22.2,'kJ/mol','+|-',5.9),
        S298 = (37.92,'J/(mol*K)','+|-',8.08),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 708,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cds)HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   Cd  u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 709,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   Cd  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)HH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 710,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)HH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 711,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   H   u0 {1,S}
7   H   u0 {1,S}
8   O2d u0 {4,D}
9   O2d u0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.68,8.28,9.58,10.61,12.04,13.13,14.87],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-5.301,'kcal/mol','+|-',0.16),
        S298 = (7.18,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = """{C/H2/CCO2} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
"""

""",
)

entry(
    index = 712,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   H   u0 {1,S}
7   H   u0 {1,S}
8   O2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-Cd(CCO)HH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 713,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   H   u0 {1,S}
7   H   u0 {1,S}
8   S2d u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 714,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   H   u0 {1,S}
7   H   u0 {1,S}
8   S2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 715,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   H   u0 {1,S}
7   H   u0 {1,S}
8   C   u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)HH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 716,
    label = "Cs-CtCsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Cs u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.95,6.56,7.93,9.08,10.86,12.19,14.2],'cal/(mol*K)','+|-',[0.08,0.08,0.08,0.08,0.08,0.08,0.08]),
        H298 = (-4.73,'kcal/mol','+|-',0.28),
        S298 = (10.3,'cal/(mol*K)','+|-',0.07),
    ),
    shortDesc = """Cs-CtCsHH BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 717,
    label = "Cs-(CtN3t)CsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S} {6,T}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   N3t u0 {2,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.3,13.5,15.3,16.8,19.2,20.9,23.5],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (22.9,'kcal/mol','+|-',1.3),
        S298 = (39.8,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 718,
    label = "Cs-CtCdsHH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Ct      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   H       u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CtHH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 719,
    label = "Cs-(Cds-O2d)CtHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.85,6.22,8.01,9.43,11.29,12.76,12.76],'cal/(mol*K)','+|-',[0.08,0.08,0.08,0.08,0.08,0.08,0.08]),
        H298 = (-5.4,'kcal/mol','+|-',0.28),
        S298 = (7.68,'cal/(mol*K)','+|-',0.07),
    ),
    shortDesc = """Cs-COCtHH BENSON Hf, Mopac =3D S,Cp nov99 !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
"""

""",
)

entry(
    index = 720,
    label = "Cs-(Cds-Cd)CtHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)CtHH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 721,
    label = "Cs-(Cds-Cds)CtHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.4,6.33,7.9,9.16,10.93,12.29,13.43],'cal/(mol*K)','+|-',[0.08,0.08,0.08,0.08,0.08,0.08,0.08]),
        H298 = (-3.49,'kcal/mol','+|-',0.28),
        S298 = (9.31,'cal/(mol*K)','+|-',0.07),
    ),
    shortDesc = """Cs-CtCdHH RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
"""

""",
)

entry(
    index = 722,
    label = "Cs-(Cds-Cdd)CtHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CtHH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 723,
    label = "Cs-(Cds-Cdd-O2d)CtHH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = 'Cs-Cd(CCO)HH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 724,
    label = "Cs-(Cds-Cdd-S2d)CtHH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 725,
    label = "Cs-(Cds-Cdd-Cd)CtHH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)CtHH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 726,
    label = "Cs-CtCtHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Ct u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4,6.07,7.71,9.03,10.88,12.3,12.48],'cal/(mol*K)','+|-',[0.08,0.08,0.08,0.08,0.08,0.08,0.08]),
        H298 = (-0.82,'kcal/mol','+|-',0.28),
        S298 = (10.04,'cal/(mol*K)','+|-',0.07),
    ),
    shortDesc = """Cs-CtCtHH RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
"""

""",
)

entry(
    index = 727,
    label = "Cs-CbCsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cs u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.84,7.61,8.98,10.01,11.49,12.54,13.76],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-4.86,'kcal/mol','+|-',0.2),
        S298 = (9.34,'cal/(mol*K)','+|-',0.19),
    ),
    shortDesc = """Cs-CbCsHH BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 728,
    label = "Cs-CbCdsHH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   H       u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CbHH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 729,
    label = "Cs-(Cds-O2d)CbHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.38,7.59,9.25,10.51,12.19,13.52,13.52],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-5.4,'kcal/mol','+|-',0.2),
        S298 = (5.89,'cal/(mol*K)','+|-',0.19),
    ),
    shortDesc = """Cs-COCbHH BENSON Hf, Mopac =3D S,Cp nov99 !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
"""

""",
)

entry(
    index = 730,
    label = "Cs-(Cds-Cd)CbHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)CbHH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 731,
    label = "Cs-(Cds-Cds)CbHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.51,6.76,8.61,10.01,11.97,13.4,15.47],'cal/(mol*K)','+|-',[0.2,0.2,0.2,0.2,0.2,0.2,0.2]),
        H298 = (-4.29,'kcal/mol','+|-',0.2),
        S298 = (2,'cal/(mol*K)','+|-',0.19),
    ),
    shortDesc = """Cs-CbCdHH Hf=Stein S,Cp=3D mopac nov99""",
    longDesc = 
"""

""",
)

entry(
    index = 732,
    label = "Cs-(Cds-Cdd)CbHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CbHH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 733,
    label = "Cs-(Cds-Cdd-O2d)CbHH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = 'Cs-Cd(CCO)HH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 734,
    label = "Cs-(Cds-Cdd-S2d)CbHH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 735,
    label = "Cs-(Cds-Cdd-Cd)CbHH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)CbHH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 736,
    label = "Cs-CbCtHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Ct u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.28,6.43,8.16,9.5,11.36,12.74,13.7],'cal/(mol*K)','+|-',[0.08,0.08,0.08,0.08,0.08,0.08,0.08]),
        H298 = (-4.29,'kcal/mol','+|-',0.28),
        S298 = (9.84,'cal/(mol*K)','+|-',0.07),
    ),
    shortDesc = """Cs-CbCtHH Hf=Stein S,Cp=3D mopac nov99""",
    longDesc = 
"""

""",
)

entry(
    index = 737,
    label = "Cs-CbCbHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.67,7.7,9.31,10.52,12.21,13.47,15.11],'cal/(mol*K)','+|-',[0.2,0.2,0.2,0.2,0.2,0.2,0.2]),
        H298 = (-4.29,'kcal/mol','+|-',0.2),
        S298 = (8.07,'cal/(mol*K)','+|-',0.19),
    ),
    shortDesc = """Cs-CbCbHH Hf=3Dbsn/Cs/Cd2/H2 S,Cp=3D mopac nov99""",
    longDesc = 
"""

""",
)

entry(
    index = 738,
    label = "Cs-C=SCtHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 739,
    label = "Cs-C=SCsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.04,6.19,8.2,9.42,10.99,12.05,13.72],'cal/(mol*K)'),
        H298 = (-1.72,'kcal/mol'),
        S298 = (10.53,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 740,
    label = "Cs-C=S(Cds-Cd)HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   C   u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 741,
    label = "Cs-C=S(Cds-Cdd)HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 742,
    label = "Cs-C=S(Cds-Cdd-Cd)HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 743,
    label = "Cs-C=S(Cds-Cdd-S2d)HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 744,
    label = "Cs-C=S(Cds-Cds)HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   Cd  u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 745,
    label = "Cs-C=SC=SHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   CS  u0 {1,S} {7,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   S2d u0 {2,D}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 746,
    label = "Cs-C=SCbHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 747,
    label = "Cs-CCCH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = 'Cs-CsCsCsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 748,
    label = "Cs-CsCsCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.54,6,7.17,8.05,9.31,10.05,11.17],'cal/(mol*K)','+|-',[0.07,0.07,0.07,0.07,0.07,0.07,0.07]),
        H298 = (-1.9,'kcal/mol','+|-',0.15),
        S298 = (-12.07,'cal/(mol*K)','+|-',0.07),
    ),
    shortDesc = """Cs-CsCsCsH BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 749,
    label = "Cs-CdsCsCsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   Cs      u0 {1,S}
4   Cs      u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CsCsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 750,
    label = "Cs-(Cds-O2d)CsCsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.68,27.86,31.26,34,38.07,41,45.46],'J/(mol*K)','+|-',[3.34,3.34,3.34,3.34,3.34,3.34,3.34]),
        H298 = (-5.4,'kJ/mol','+|-',2.85),
        S298 = (-47.41,'J/(mol*K)','+|-',3.9),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 751,
    label = "Cs-(Cds-Cd)CsCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)CsCsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 752,
    label = "Cs-(Cds-Cds)CsCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.16,5.91,7.34,8.19,9.46,10.19,11.28],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (-1.48,'kcal/mol','+|-',0.27),
        S298 = (-11.69,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = """Cs-CdCsCsH BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 753,
    label = "Cs-(Cds-Cdd)CsCsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CsCsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 754,
    label = "Cs-(Cds-Cdd-O2d)CsCsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   H   u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.23,27.55,32.36,35.85,40.37,43.16,46.94],'J/(mol*K)','+|-',[6.93,6.93,6.93,6.93,6.93,6.93,6.93]),
        H298 = (-11.1,'kJ/mol','+|-',5.9),
        S298 = (-47.59,'J/(mol*K)','+|-',8.08),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 755,
    label = "Cs-(Cds-Cdd-S2d)CsCsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 756,
    label = "Cs-(Cds-Cdd-Cd)CsCsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   H   u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.16,5.91,7.34,8.19,9.46,10.19,11.28],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (-1.48,'kcal/mol','+|-',0.27),
        S298 = (-11.69,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = """Cs-CdCsCsH BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 757,
    label = "Cs-(CdN3d)CsCsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D} {7,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   N3d u0 {2,D}
7   R   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5,6.5,7.5,8.2,9.3,9.9,10.9],'cal/(mol*K)','+|-',[1.2,1.2,1.2,1.2,1.2,1.2,1.2]),
        H298 = (-1.6,'kcal/mol','+|-',1.7),
        S298 = (-11.2,'cal/(mol*K)','+|-',1.6),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 758,
    label = "Cs-CtCsCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.99,5.61,6.85,7.78,9.1,9.9,11.12],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (-1.72,'kcal/mol','+|-',0.27),
        S298 = (-11.19,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = """Cs-CtCsCsH BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 759,
    label = "Cs-(CtN3t)CsCsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S} {6,T}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   N3t u0 {2,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11,12.7,14.1,15.4,17.3,18.6,21.85],'cal/(mol*K)'),
        H298 = (25.8,'kcal/mol'),
        S298 = (19.8,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 760,
    label = "Cs-CbCsCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.88,6.66,7.9,8.75,9.73,10.25,10.68],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (-0.98,'kcal/mol','+|-',0.27),
        S298 = (-12.15,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = """Cs-CbCsCsH BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 761,
    label = "Cs-CdsCdsCsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 762,
    label = "Cs-(Cds-O2d)(Cds-O2d)CsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   CO  u0 {1,S} {7,D}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
""",
    thermo = 'Cs-CsCsCsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 763,
    label = "Cs-(Cds-O2d)(Cds-Cd)CsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   C   u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.32,32.99,35.49,37.28,39.75,41.6,44.96],'J/(mol*K)','+|-',[3.34,3.34,3.34,3.34,3.34,3.34,3.34]),
        H298 = (-2.2,'kJ/mol','+|-',2.85),
        S298 = (-50.47,'J/(mol*K)','+|-',3.9),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 764,
    label = "Cs-(Cds-O2d)(Cds-Cds)CsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   Cd  u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)CsCsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 765,
    label = "Cs-(Cds-O2d)(Cds-Cdd)CsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cdd-Cd)CsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 766,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)CsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   H   u0 {1,S}
7   O2d u0 {3,D}
8   O2d u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)CsCsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 767,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)CsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   H   u0 {1,S}
7   O2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)CsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 768,
    label = "Cs-(Cds-Cd)(Cds-Cd)CsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 769,
    label = "Cs-(Cds-Cds)(Cds-Cds)CsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.28,6.54,7.67,8.48,9.45,10.18,11.24],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (-1.1,'kcal/mol','+|-',0.27),
        S298 = (-13.03,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = """Cs-CdCdCsH RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
"""

""",
)

entry(
    index = 770,
    label = "Cs-(Cds-Cdd)(Cds-Cds)CsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cds)CsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 771,
    label = "Cs-CsCd(CCO)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   H   u0 {1,S}
7   Cd  u0 {3,D}
8   O2d u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([24.45,31.59,36.01,38.8,42.13,44.21,47.25],'J/(mol*K)','+|-',[6.93,6.93,6.93,6.93,6.93,6.93,6.93]),
        H298 = (-10.4,'kJ/mol','+|-',5.9),
        S298 = (-54.03,'J/(mol*K)','+|-',8.08),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 772,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cds)CsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   H   u0 {1,S}
7   Cd  u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 773,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   H   u0 {1,S}
7   Cd  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 774,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)CsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 775,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cs  u0 {1,S}
7   H   u0 {1,S}
8   O2d u0 {4,D}
9   O2d u0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.19,28,33.91,38.75,46.07,51.36,59.45],'J/(mol*K)','+|-',[3.46,3.46,3.46,3.46,3.46,3.46,3.46]),
        H298 = (-21.1,'kJ/mol','+|-',2.95),
        S298 = (40.95,'J/(mol*K)','+|-',4.04),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 776,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cs  u0 {1,S}
7   H   u0 {1,S}
8   O2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-CsCd(CCO)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 777,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cs  u0 {1,S}
7   H   u0 {1,S}
8   S2d u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 778,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cs  u0 {1,S}
7   H   u0 {1,S}
8   S2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 779,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cs  u0 {1,S}
7   H   u0 {1,S}
8   C   u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 780,
    label = "Cs-CtCdsCsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Ct      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CtCsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 781,
    label = "Cs-(Cds-O2d)CtCsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)CsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 782,
    label = "Cs-(Cds-Cd)CtCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)CtCsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 783,
    label = "Cs-(Cds-Cds)CtCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.55,7.21,8.39,9.17,10,10.61,10.51],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (-6.9,'kcal/mol','+|-',0.27),
        S298 = (-13.48,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = """Cs-CtCdCsH RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
"""

""",
)

entry(
    index = 784,
    label = "Cs-(Cds-Cdd)CtCsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CtCsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 785,
    label = "Cs-(Cds-Cdd-O2d)CtCsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Cs  u0 {1,S}
6   H   u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = 'Cs-CsCd(CCO)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 786,
    label = "Cs-(Cds-Cdd-S2d)CtCsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Cs  u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 787,
    label = "Cs-(Cds-Cdd-Cd)CtCsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Cs  u0 {1,S}
6   H   u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)CtCsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 788,
    label = "Cs-CbCdsCsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CbCsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 789,
    label = "Cs-(Cds-O2d)CbCsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)CsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 790,
    label = "Cs-(Cds-Cd)CbCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)CbCsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 791,
    label = "Cs-(Cds-Cds)CbCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.5,6.57,8.07,8.89,9.88,10.39,10.79],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (-1.56,'kcal/mol','+|-',0.27),
        S298 = (-11.77,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = """Cs-CbCdCsH BOZZELLI =3D Cs/Cs2/Cd/H + (Cs/Cs2/Cb/H - Cs/Cs3/H)""",
    longDesc = 
"""

""",
)

entry(
    index = 792,
    label = "Cs-(Cds-Cdd)CbCsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CbCsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 793,
    label = "Cs-(Cds-Cdd-O2d)CbCsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cs  u0 {1,S}
6   H   u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = 'Cs-CsCd(CCO)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 794,
    label = "Cs-(Cds-Cdd-Cd)CbCsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cs  u0 {1,S}
6   H   u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)CbCsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 795,
    label = "Cs-CtCtCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.27,5.32,6.9,8.03,9.33,10.21,9.38],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (1.72,'kcal/mol','+|-',0.27),
        S298 = (-11.61,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = """Cs-CtCtCsH RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
"""

""",
)

entry(
    index = 796,
    label = "Cs-CbCtCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.33,6.27,7.58,8.48,9.52,10.1,10.63],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (-1.55,'kcal/mol','+|-',0.27),
        S298 = (-11.65,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = """Cs-CbCtCsH BOZZELLI =3D Cs/Cs2/Cb/H + (Cs/Cs2/Ct/H - Cs/Cs3/H)""",
    longDesc = 
"""

""",
)

entry(
    index = 797,
    label = "Cs-CbCbCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.22,7.32,8.63,8.45,10.15,10.45,10.89],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (-1.06,'kcal/mol','+|-',0.27),
        S298 = (-12.23,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = """Cs-CbCbCsCs BOZZELLI =3D Cs/Cs2/Cb/H + (Cs/Cs2/Cb/H - Cs/Cs3/H)""",
    longDesc = 
"""

""",
)

entry(
    index = 798,
    label = "Cs-CdsCdsCdsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 799,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   CO  u0 {1,S} {7,D}
4   CO  u0 {1,S} {8,D}
5   H   u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
8   O2d u0 {4,D}
""",
    thermo = 'Cs-CsCsCsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 800,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cd)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   H   u0 {1,S}
6   C   u0 {4,D}
7   O2d u0 {2,D}
8   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 801,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   H   u0 {1,S}
6   Cd  u0 {4,D}
7   O2d u0 {2,D}
8   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-O2d)CsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 802,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   H   u0 {1,S}
6   Cdd u0 {4,D}
7   O2d u0 {2,D}
8   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 803,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {7,D}
4   CO  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   H   u0 {1,S}
7   O2d u0 {3,D}
8   O2d u0 {4,D}
9   O2d u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)CsCsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 804,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {7,D}
4   CO  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   H   u0 {1,S}
7   O2d u0 {3,D}
8   O2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 805,
    label = "Cs-(Cds-O2d)(Cds-Cd)(Cds-Cd)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   H   u0 {1,S}
6   C   u0 {3,D}
7   C   u0 {4,D}
8   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.26,34.41,37.4,39.22,41.43,43.04,46.12],'J/(mol*K)','+|-',[3.34,3.34,3.34,3.34,3.34,3.34,3.34]),
        H298 = (2.9,'kJ/mol','+|-',2.85),
        S298 = (-53.2,'J/(mol*K)','+|-',3.9),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 806,
    label = "Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   H   u0 {1,S}
6   Cd  u0 {3,D}
7   Cd  u0 {4,D}
8   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)CsCsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 807,
    label = "Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cds)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   H   u0 {1,S}
6   Cdd u0 {3,D}
7   Cd  u0 {4,D}
8   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 808,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {9,D}
6   H   u0 {1,S}
7   Cd  u0 {4,D}
8   O2d u0 {3,D}
9   O2d u0 {5,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cdd-O2d)CsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 809,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cds)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {9,D}
6   H   u0 {1,S}
7   Cd  u0 {4,D}
8   O2d u0 {3,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 810,
    label = "Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cdd)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   H   u0 {1,S}
6   Cdd u0 {3,D}
7   Cdd u0 {4,D}
8   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 811,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)H",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CO  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    H   u0 {1,S}
8    O2d u0 {4,D}
9    O2d u0 {5,D}
10   O2d u0 {6,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 812,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)H",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CO  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    H   u0 {1,S}
8    O2d u0 {4,D}
9    O2d u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 813,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CO  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    H   u0 {1,S}
8    O2d u0 {4,D}
9    C   u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 814,
    label = "Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)H",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cd u0 {1,S} {8,D}
5   H  u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
8   C  u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 815,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)H",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cd u0 {1,S} {8,D}
5   H  u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
8   Cd u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.51,5.96,7.13,7.98,9.06,9.9,11.23],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (0.41,'kcal/mol','+|-',0.27),
        S298 = (-11.82,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = """Cs-CdCdCdH RAMAN & GREEN JPC 2002""",
    longDesc = 
"""

""",
)

entry(
    index = 816,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   H   u0 {1,S}
6   Cd  u0 {2,D}
7   Cd  u0 {3,D}
8   Cdd u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 817,
    label = "Cs-CdCd(CCO)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   H   u0 {1,S}
7   Cd  u0 {3,D}
8   Cd  u0 {4,D}
9   O2d u0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.62,35.4,39.24,41.25,43.4,44.87,47.43],'J/(mol*K)','+|-',[6.93,6.93,6.93,6.93,6.93,6.93,6.93]),
        H298 = (-6.8,'kJ/mol','+|-',5.9),
        S298 = (-55.37,'J/(mol*K)','+|-',8.08),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 818,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-S2d)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   H   u0 {1,S}
7   Cd  u0 {3,D}
8   Cd  u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 819,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   H   u0 {1,S}
7   Cd  u0 {3,D}
8   Cd  u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 820,
    label = "Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   H   u0 {1,S}
6   Cd  u0 {2,D}
7   Cdd u0 {3,D}
8   Cdd u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 821,
    label = "Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)H",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    H   u0 {1,S}
8    Cd  u0 {4,D}
9    O2d u0 {5,D}
10   O2d u0 {6,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 822,
    label = "Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-Cd)H",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    H   u0 {1,S}
8    Cd  u0 {4,D}
9    O2d u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = 'Cs-CdCd(CCO)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 823,
    label = "Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-S2d)H",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    H   u0 {1,S}
8    Cd  u0 {4,D}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 824,
    label = "Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-Cd)H",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    H   u0 {1,S}
8    Cd  u0 {4,D}
9    S2d u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 825,
    label = "Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    H   u0 {1,S}
8    Cd  u0 {4,D}
9    C   u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 826,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
8   Cdd u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 827,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)H",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    H   u0 {1,S}
9    O2d u0 {5,D}
10   O2d u0 {6,D}
11   O2d u0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 828,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)H",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    H   u0 {1,S}
9    O2d u0 {5,D}
10   O2d u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 829,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    H   u0 {1,S}
9    O2d u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = 'Cs-CdCd(CCO)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 830,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)H",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    H   u0 {1,S}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
11   S2d u0 {7,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 831,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-Cd)H",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    H   u0 {1,S}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 832,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    H   u0 {1,S}
9    S2d u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 833,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    H   u0 {1,S}
9    C   u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 834,
    label = "Cs-CtCdsCdsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Ct      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 835,
    label = "Cs-(Cds-O2d)(Cds-O2d)CtH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   CO  u0 {1,S} {7,D}
4   Ct  u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 836,
    label = "Cs-(Cds-O2d)(Cds-Cd)CtH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   H   u0 {1,S}
6   C   u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)CtH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 837,
    label = "Cs-(Cds-O2d)(Cds-Cds)CtH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   H   u0 {1,S}
6   Cd  u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 838,
    label = "Cs-(Cds-O2d)(Cds-Cdd)CtH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cdd-Cd)CtH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 839,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)CtH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   H   u0 {1,S}
7   O2d u0 {3,D}
8   O2d u0 {4,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 840,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)CtH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   H   u0 {1,S}
7   O2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)CtH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 841,
    label = "Cs-(Cds-Cd)(Cds-Cd)CtH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Ct u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 842,
    label = "Cs-(Cds-Cds)(Cds-Cds)CtH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Ct u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.68,7.85,8.62,9.16,9.81,10.42,10.49],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (1.88,'kcal/mol','+|-',0.27),
        S298 = (-13.75,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = """Cs-CtCdCdH RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
"""

""",
)

entry(
    index = 843,
    label = "Cs-(Cds-Cdd)(Cds-Cds)CtH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Ct  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cds)CtH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 844,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cds)CtH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   H   u0 {1,S}
7   Cd  u0 {3,D}
8   O2d u0 {4,D}
""",
    thermo = 'Cs-CdCd(CCO)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 845,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cds)CtH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   H   u0 {1,S}
7   Cd  u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 846,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CtH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   H   u0 {1,S}
7   Cd  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 847,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)CtH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Ct  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 848,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CtH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Ct  u0 {1,S}
7   H   u0 {1,S}
8   O2d u0 {4,D}
9   O2d u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 849,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CtH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Ct  u0 {1,S}
7   H   u0 {1,S}
8   O2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)(Cds-Cds)CtH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 850,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CtH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Ct  u0 {1,S}
7   H   u0 {1,S}
8   S2d u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 851,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CtH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Ct  u0 {1,S}
7   H   u0 {1,S}
8   S2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 852,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Ct  u0 {1,S}
7   H   u0 {1,S}
8   C   u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 853,
    label = "Cs-CbCdsCdsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CbH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 854,
    label = "Cs-(Cds-O2d)(Cds-O2d)CbH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   CO  u0 {1,S} {7,D}
4   Cb  u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 855,
    label = "Cs-(Cds-O2d)(Cds-Cd)CbH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   H   u0 {1,S}
6   C   u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)CbH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 856,
    label = "Cs-(Cds-O2d)(Cds-Cds)CbH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   H   u0 {1,S}
6   Cd  u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 857,
    label = "Cs-(Cds-O2d)(Cds-Cdd)CbH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cdd-Cd)CbH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 858,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)CbH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   H   u0 {1,S}
7   O2d u0 {3,D}
8   O2d u0 {4,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 859,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)CbH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   H   u0 {1,S}
7   O2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)CbH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 860,
    label = "Cs-(Cds-Cd)(Cds-Cd)CbH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cb u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CbH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 861,
    label = "Cs-(Cds-Cds)(Cds-Cds)CbH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cb u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.12,6.51,8.24,9,10.03,10.53,10.89],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (-1.39,'kcal/mol','+|-',0.27),
        S298 = (-11.39,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = """Cs-CbCdCdH BOZZELLI =3D Cs/Cs/Cd2/H + (Cs/Cs2/Cb/H - Cs/Cs3/H)""",
    longDesc = 
"""

""",
)

entry(
    index = 862,
    label = "Cs-(Cds-Cdd)(Cds-Cds)CbH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cb  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cds)CbH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 863,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cds)CbH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   H   u0 {1,S}
7   Cd  u0 {3,D}
8   O2d u0 {4,D}
""",
    thermo = 'Cs-CdCd(CCO)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 864,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cds)CbH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   H   u0 {1,S}
7   Cd  u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 865,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CbH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   H   u0 {1,S}
7   Cd  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CbH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 866,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)CbH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cb  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 867,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CbH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   H   u0 {1,S}
8   O2d u0 {4,D}
9   O2d u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 868,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CbH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   H   u0 {1,S}
8   O2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)(Cds-Cds)CbH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 869,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CbH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   H   u0 {1,S}
8   S2d u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 870,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CbH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   H   u0 {1,S}
8   S2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 871,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   H   u0 {1,S}
8   C   u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CbH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 872,
    label = "Cs-CtCtCdsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Ct      u0 {1,S}
3   Ct      u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = 'Cs-CtCt(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 873,
    label = "Cs-CtCt(Cds-O2d)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   Ct  u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 874,
    label = "Cs-CtCt(Cds-Cd)H",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = 'Cs-CtCt(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 875,
    label = "Cs-CtCt(Cds-Cds)H",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.58,5.68,7.11,8.12,9.27,10.13,9.44],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (4.73,'kcal/mol','+|-',0.27),
        S298 = (-11.46,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = """Cs-CtCtCdH RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
"""

""",
)

entry(
    index = 876,
    label = "Cs-CtCt(Cds-Cdd)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   Ct  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = 'Cs-CtCt(Cds-Cdd-Cd)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 877,
    label = "Cs-CtCt(Cds-Cdd-O2d)H",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   H   u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = 'Cs-CdCd(CCO)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 878,
    label = "Cs-CtCt(Cds-Cdd-S2d)H",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 879,
    label = "Cs-CtCt(Cds-Cdd-Cd)H",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   H   u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = 'Cs-CtCt(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 880,
    label = "Cs-CbCtCdsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   Ct      u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = 'Cs-CbCt(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 881,
    label = "Cs-CbCt(Cds-O2d)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Ct  u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)CtH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 882,
    label = "Cs-CbCt(Cds-Cd)H",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Ct u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = 'Cs-CbCt(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 883,
    label = "Cs-CbCt(Cds-Cds)H",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Ct u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 884,
    label = "Cs-CbCt(Cds-Cdd)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Ct  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = 'Cs-CbCt(Cds-Cdd-Cd)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 885,
    label = "Cs-CbCt(Cds-Cdd-O2d)H",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   H   u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)(Cds-Cds)CtH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 886,
    label = "Cs-CbCt(Cds-Cdd-S2d)H",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 887,
    label = "Cs-CbCt(Cds-Cdd-Cd)H",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   H   u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = 'Cs-CbCt(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 888,
    label = "Cs-CbCbCdsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   Cb      u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = 'Cs-CbCb(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 889,
    label = "Cs-CbCb(Cds-O2d)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 890,
    label = "Cs-CbCb(Cds-Cd)H",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 891,
    label = "Cs-CbCb(Cds-Cds)H",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 892,
    label = "Cs-CbCb(Cds-Cdd)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = 'Cs-CbCb(Cds-Cdd-Cd)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 893,
    label = "Cs-CbCb(Cds-Cdd-O2d)H",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   H   u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = 'Cs-CdCd(CCO)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 894,
    label = "Cs-CbCb(Cds-Cdd-S2d)H",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 895,
    label = "Cs-CbCb(Cds-Cdd-Cd)H",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   H   u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = 'Cs-CbCb(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 896,
    label = "Cs-CtCtCtH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.03,5.27,6.78,7.88,9.14,10.08,8.47],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (10.11,'kcal/mol','+|-',0.27),
        S298 = (-10.46,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = """Cs-CtCtCtH RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
"""

""",
)

entry(
    index = 897,
    label = "Cs-CbCtCtH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = 'Cs-CtCt(Cds-Cds)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 898,
    label = "Cs-CbCbCtH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   Ct u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 899,
    label = "Cs-CbCbCbH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.56,7.98,9.36,10.15,10.57,10.65,9.7],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (-0.34,'kcal/mol','+|-',0.27),
        S298 = (-12.31,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = """Cs-CbCbCbH BOZZELLI =3D Cs/Cs/Cb2/H + (Cs/Cs2/Cb/H - Cs/Cs3/H)""",
    longDesc = 
"""

""",
)

entry(
    index = 900,
    label = "Cs-C=SC=SCbH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   CS  u0 {1,S} {7,D}
4   Cb  u0 {1,S}
5   H   u0 {1,S}
6   S2d u0 {2,D}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 901,
    label = "Cs-C=S(Cds-Cd)(Cds-Cd)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   H   u0 {1,S}
6   C   u0 {3,D}
7   C   u0 {4,D}
8   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 902,
    label = "Cs-C=S(Cds-Cdd)(Cds-Cds)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   H   u0 {1,S}
6   Cdd u0 {3,D}
7   Cd  u0 {4,D}
8   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 903,
    label = "Cs-C=S(Cds-Cdd-Cd)(Cds-Cds)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CS  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {9,D}
6   H   u0 {1,S}
7   Cd  u0 {4,D}
8   S2d u0 {3,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 904,
    label = "Cs-C=S(Cds-Cdd-S2d)(Cds-Cds)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CS  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {9,D}
6   H   u0 {1,S}
7   Cd  u0 {4,D}
8   S2d u0 {3,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 905,
    label = "Cs-C=S(Cds-Cds)(Cds-Cds)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   H   u0 {1,S}
6   Cd  u0 {3,D}
7   Cd  u0 {4,D}
8   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 906,
    label = "Cs-C=S(Cds-Cdd)(Cds-Cdd)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   H   u0 {1,S}
6   Cdd u0 {3,D}
7   Cdd u0 {4,D}
8   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 907,
    label = "Cs-C=S(Cds-Cdd-Cd)(Cds-Cdd-Cd)H",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CS  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    H   u0 {1,S}
8    S2d u0 {4,D}
9    C   u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 908,
    label = "Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-S2d)H",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CS  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    H   u0 {1,S}
8    S2d u0 {4,D}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 909,
    label = "Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-Cd)H",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CS  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    H   u0 {1,S}
8    S2d u0 {4,D}
9    S2d u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 910,
    label = "Cs-C=S(Cds-Cd)CtH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   H   u0 {1,S}
6   C   u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 911,
    label = "Cs-C=S(Cds-Cdd)CtH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 912,
    label = "Cs-C=S(Cds-Cdd-S2d)CtH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 913,
    label = "Cs-C=S(Cds-Cdd-Cd)CtH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 914,
    label = "Cs-C=S(Cds-Cds)CtH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   H   u0 {1,S}
6   Cd  u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 915,
    label = "Cs-C=SC=SCtH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   CS  u0 {1,S} {7,D}
4   Ct  u0 {1,S}
5   H   u0 {1,S}
6   S2d u0 {2,D}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 916,
    label = "Cs-C=SCtCsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 917,
    label = "Cs-C=SC=SCsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   CS  u0 {1,S} {7,D}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   S2d u0 {2,D}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 918,
    label = "Cs-C=S(Cds-Cd)CbH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   H   u0 {1,S}
6   C   u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 919,
    label = "Cs-C=S(Cds-Cds)CbH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   H   u0 {1,S}
6   Cd  u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 920,
    label = "Cs-C=S(Cds-Cdd)CbH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 921,
    label = "Cs-C=S(Cds-Cdd-S2d)CbH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 922,
    label = "Cs-C=S(Cds-Cdd-Cd)CbH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 923,
    label = "Cs-C=S(Cds-Cd)CsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   C   u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 924,
    label = "Cs-C=S(Cds-Cds)CsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   Cd  u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 925,
    label = "Cs-C=S(Cds-Cdd)CsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 926,
    label = "Cs-C=S(Cds-Cdd-Cd)CsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 927,
    label = "Cs-C=S(Cds-Cdd-S2d)CsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 928,
    label = "Cs-CbCtC=SH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Ct  u0 {1,S}
5   H   u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 929,
    label = "Cs-C=SC=SC=SH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   CS  u0 {1,S} {7,D}
4   CS  u0 {1,S} {8,D}
5   H   u0 {1,S}
6   S2d u0 {2,D}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 930,
    label = "Cs-C=SCsCsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.36,5.4,7.24,8.24,9.35,9.91,10.56],'cal/(mol*K)'),
        H298 = (2.29,'kcal/mol'),
        S298 = (-10.76,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 931,
    label = "Cs-CtCtC=SH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   Ct  u0 {1,S}
5   H   u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 932,
    label = "Cs-CbCbC=SH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
5   H   u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 933,
    label = "Cs-C=SC=S(Cds-Cd)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   CS  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   H   u0 {1,S}
6   C   u0 {4,D}
7   S2d u0 {2,D}
8   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 934,
    label = "Cs-C=SC=S(Cds-Cds)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   CS  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   H   u0 {1,S}
6   Cd  u0 {4,D}
7   S2d u0 {2,D}
8   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 935,
    label = "Cs-C=SC=S(Cds-Cdd)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   CS  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   H   u0 {1,S}
6   Cdd u0 {4,D}
7   S2d u0 {2,D}
8   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 936,
    label = "Cs-C=SC=S(Cds-Cdd-S2d)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CS  u0 {1,S} {7,D}
4   CS  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   H   u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 937,
    label = "Cs-C=SC=S(Cds-Cdd-Cd)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CS  u0 {1,S} {7,D}
4   CS  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   H   u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 938,
    label = "Cs-CCCC",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   C  u0 {1,S}
""",
    thermo = 'Cs-CsCsCsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 939,
    label = "Cs-CsCsCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.37,6.13,7.36,8.12,8.77,8.76,8.12],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (0.5,'kcal/mol','+|-',0.27),
        S298 = (-35.1,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = """Cs-CsCsCsCs BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 940,
    label = "Cs-CdsCsCsCs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   Cs      u0 {1,S}
4   Cs      u0 {1,S}
5   Cs      u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CsCsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 941,
    label = "Cs-(Cds-O2d)CsCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([22.68,27.48,30.12,31.51,32.36,32.39,32.42],'J/(mol*K)','+|-',[3.34,3.34,3.34,3.34,3.34,3.34,3.34]),
        H298 = (4.6,'kJ/mol','+|-',2.85),
        S298 = (-140.94,'J/(mol*K)','+|-',3.9),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 942,
    label = "Cs-(Cds-Cd)CsCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)CsCsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 943,
    label = "Cs-(Cds-Cds)CsCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.99,6.04,7.43,8.26,8.92,8.96,8.23],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (1.68,'kcal/mol','+|-',0.27),
        S298 = (-34.72,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = """Cs-CdCsCsCs BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 944,
    label = "Cs-(Cds-Cdd)CsCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CsCsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 945,
    label = "Cs-(Cds-Cdd-O2d)CsCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   Cs  u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.63,27.65,31.98,34.41,36.16,36.25,35.2],'J/(mol*K)','+|-',[6.93,6.93,6.93,6.93,6.93,6.93,6.93]),
        H298 = (-4.5,'kJ/mol','+|-',5.9),
        S298 = (-144.08,'J/(mol*K)','+|-',8.08),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 946,
    label = "Cs-(Cds-Cdd-S2d)CsCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   Cs  u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 947,
    label = "Cs-(Cds-Cdd-Cd)CsCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   Cs  u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)CsCsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 948,
    label = "Cs-(CdN3d)CsCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D} {7,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   N3d u0 {2,D}
7   R   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.3,6.6,7.3,7.5,7.8,7.8,7.7],'cal/(mol*K)','+|-',[1.2,1.2,1.2,1.2,1.2,1.2,1.2]),
        H298 = (0.6,'kcal/mol','+|-',1.7),
        S298 = (-33.5,'cal/(mol*K)','+|-',1.6),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 949,
    label = "Cs-CtCsCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.37,6.79,8.09,8.78,9.19,8.96,7.63],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (2.81,'kcal/mol','+|-',0.27),
        S298 = (-35.18,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = """Cs-CtCsCsCs BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 950,
    label = "Cs-(CtN3t)CsCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S} {6,T}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   N3t u0 {2,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.4,13.4,14.6,15.3,16.3,16.7,17.2],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (28.3,'kcal/mol','+|-',1.3),
        S298 = (-3,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 951,
    label = "Cs-CbCsCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.37,6.79,8.09,8.78,9.19,8.96,7.63],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (2.81,'kcal/mol','+|-',0.26),
        S298 = (-35.18,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = """Cs-CbCsCsCs BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 952,
    label = "Cs-CdsCdsCsCs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
5   Cs      u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 953,
    label = "Cs-(Cds-O2d)(Cds-O2d)CsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   CO  u0 {1,S} {7,D}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([33.76,33.42,32.6,31.91,31.01,30.55,30.35],'J/(mol*K)','+|-',[5.08,5.08,5.08,5.08,5.08,5.08,5.08]),
        H298 = (14.9,'kJ/mol','+|-',4.33),
        S298 = (-146.69,'J/(mol*K)','+|-',5.92),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 954,
    label = "Cs-(Cds-O2d)(Cds-Cd)CsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   C   u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.01,30.13,32.44,33.51,33.75,33.26,32.55],'J/(mol*K)','+|-',[3.34,3.34,3.34,3.34,3.34,3.34,3.34]),
        H298 = (9.8,'kJ/mol','+|-',2.85),
        S298 = (-146.74,'J/(mol*K)','+|-',3.9),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 955,
    label = "Cs-(Cds-O2d)(Cds-Cds)CsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   Cd  u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)CsCsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 956,
    label = "Cs-(Cds-O2d)(Cds-Cdd)CsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   Cdd u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cdd-Cd)CsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 957,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)CsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   Cs  u0 {1,S}
7   O2d u0 {3,D}
8   O2d u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)CsCsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 958,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)CsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   Cs  u0 {1,S}
7   O2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)CsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 959,
    label = "Cs-(Cds-Cd)(Cds-Cd)CsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 960,
    label = "Cs-(Cds-Cds)(Cds-Cds)CsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.99,6.04,7.43,8.26,8.92,8.96,8.23],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (1.68,'kcal/mol','+|-',0.26),
        S298 = (-34.72,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = """Cs-CdCdCsCs BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 961,
    label = "Cs-(Cds-Cdd)(Cds-Cds)CsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   Cdd u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cds)CsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 962,
    label = "Cs-CsCsCd(CCO)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   Cs  u0 {1,S}
7   Cd  u0 {3,D}
8   O2d u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.48,31.89,35.19,36.68,37.19,36.66,34.96],'J/(mol*K)','+|-',[6.93,6.93,6.93,6.93,6.93,6.93,6.93]),
        H298 = (2.9,'kJ/mol','+|-',5.9),
        S298 = (-144.6,'J/(mol*K)','+|-',8.08),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 963,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cds)CsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   Cs  u0 {1,S}
7   Cd  u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 964,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   Cs  u0 {1,S}
7   Cd  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 965,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)CsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 966,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cs  u0 {1,S}
7   Cs  u0 {1,S}
8   O2d u0 {4,D}
9   O2d u0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.73,8.1,9.02,9.53,9.66,9.52,8.93],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (-2.987,'kcal/mol','+|-',0.26),
        S298 = (-36.46,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = """{C/C2/CCO2} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
"""

""",
)

entry(
    index = 967,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cs  u0 {1,S}
7   Cs  u0 {1,S}
8   O2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-CsCsCd(CCO)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 968,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cs  u0 {1,S}
7   Cs  u0 {1,S}
8   S2d u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 969,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cs  u0 {1,S}
7   Cs  u0 {1,S}
8   S2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 970,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cs  u0 {1,S}
7   Cs  u0 {1,S}
8   C   u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 971,
    label = "Cs-CtCdsCsCs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Ct      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
5   Cs      u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CtCsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 972,
    label = "Cs-(Cds-O2d)CtCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)CsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 973,
    label = "Cs-(Cds-Cd)CtCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)CtCsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 974,
    label = "Cs-(Cds-Cds)CtCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.99,6.7,8.16,8.92,9.34,9.16,7.14],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (2.99,'kcal/mol','+|-',0.26),
        S298 = (-34.8,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = """Cs-CtCdCsCs BOZZELLI =3D Cs/Cs3/Cd + (Cs/Cs3/Ct - Cs/Cs4)""",
    longDesc = 
"""

""",
)

entry(
    index = 975,
    label = "Cs-(Cds-Cdd)CtCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CtCsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 976,
    label = "Cs-(Cds-Cdd-O2d)CtCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Cs  u0 {1,S}
6   Cs  u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = 'Cs-CsCsCd(CCO)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 977,
    label = "Cs-(Cds-Cdd-S2d)CtCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Cs  u0 {1,S}
6   Cs  u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 978,
    label = "Cs-(Cds-Cdd-Cd)CtCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Cs  u0 {1,S}
6   Cs  u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)CtCsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 979,
    label = "Cs-CbCdsCsCs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
5   Cs      u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CbCsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 980,
    label = "Cs-(Cds-O2d)CbCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)CsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 981,
    label = "Cs-(Cds-Cd)CbCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)CbCsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 982,
    label = "Cs-(Cds-Cds)CbCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.99,6.7,8.16,8.92,9.34,9.16,7.14],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (2.99,'kcal/mol','+|-',0.26),
        S298 = (-34.8,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = """Cs-CbCdCsCs BOZZELLI =3D Cs/Cs3/Cb + (Cs/Cs3/Cd - Cs/Cs4)""",
    longDesc = 
"""

""",
)

entry(
    index = 983,
    label = "Cs-(Cds-Cdd)CbCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CbCsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 984,
    label = "Cs-(Cds-Cdd-O2d)CbCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cs  u0 {1,S}
6   Cs  u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = 'Cs-CsCsCd(CCO)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 985,
    label = "Cs-(Cds-Cdd-S2d)CbCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cs  u0 {1,S}
6   Cs  u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 986,
    label = "Cs-(Cds-Cdd-Cd)CbCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cs  u0 {1,S}
6   Cs  u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)CbCsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 987,
    label = "Cs-CtCtCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.57,5.98,7.51,8.37,9,9.02,8.34],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (1.16,'kcal/mol','+|-',0.26),
        S298 = (-35.26,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = """Cs-CtCtCsCs BOZZELLI =3D Cs/Cs3/Ct + (Cs/Cs3/Ct - Cs/Cs4)""",
    longDesc = 
"""

""",
)

entry(
    index = 988,
    label = "Cs-(CtN3t)(CtN3t)CsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S} {6,T}
3   Ct  u0 {1,S} {7,T}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   N3t u0 {2,T}
7   N3t u0 {3,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (28.4,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 989,
    label = "Cs-CbCtCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.57,5.98,7.51,8.37,9,9.02,8.34],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (1.16,'kcal/mol','+|-',0.26),
        S298 = (-35.26,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = """Cs-CbCtCsCs BOZZELLI =3D Cs/Cs3/Cb + (Cs/Cs3/Ct - Cs/Cs4)""",
    longDesc = 
"""

""",
)

entry(
    index = 990,
    label = "Cs-CbCbCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.57,5.98,7.51,8.37,9,9.02,8.34],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (1.16,'kcal/mol','+|-',0.26),
        S298 = (-35.26,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = """Cs-CbCbCsCs BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 991,
    label = "Cs-CdsCdsCdsCs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   Cs      u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 992,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   CO  u0 {1,S} {7,D}
4   CO  u0 {1,S} {8,D}
5   Cs  u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
8   O2d u0 {4,D}
""",
    thermo = 'Cs-CsCsCsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 993,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cd)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   Cs  u0 {1,S}
6   C   u0 {4,D}
7   O2d u0 {2,D}
8   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([35.99,39.53,39.94,39.09,36.71,34.8,32.51],'J/(mol*K)','+|-',[5.08,5.08,5.08,5.08,5.08,5.08,5.08]),
        H298 = (19.9,'kJ/mol','+|-',4.33),
        S298 = (-150.69,'J/(mol*K)','+|-',5.92),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 994,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   Cs  u0 {1,S}
6   Cd  u0 {4,D}
7   O2d u0 {2,D}
8   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-O2d)CsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 995,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   Cs  u0 {1,S}
6   Cdd u0 {4,D}
7   O2d u0 {2,D}
8   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 996,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {7,D}
4   CO  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   Cs  u0 {1,S}
7   O2d u0 {3,D}
8   O2d u0 {4,D}
9   O2d u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)CsCsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 997,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {7,D}
4   CO  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   Cs  u0 {1,S}
7   O2d u0 {3,D}
8   O2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 998,
    label = "Cs-(Cds-O2d)(Cds-Cd)(Cds-Cd)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cs  u0 {1,S}
6   C   u0 {3,D}
7   C   u0 {4,D}
8   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 999,
    label = "Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cs  u0 {1,S}
6   Cd  u0 {3,D}
7   Cd  u0 {4,D}
8   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)CsCsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1000,
    label = "Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cds)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cs  u0 {1,S}
6   Cdd u0 {3,D}
7   Cd  u0 {4,D}
8   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cds)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1001,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {9,D}
6   Cs  u0 {1,S}
7   Cd  u0 {4,D}
8   O2d u0 {3,D}
9   O2d u0 {5,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cdd-O2d)CsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1002,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cds)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {9,D}
6   Cs  u0 {1,S}
7   Cd  u0 {4,D}
8   O2d u0 {3,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1003,
    label = "Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cdd)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cs  u0 {1,S}
6   Cdd u0 {3,D}
7   Cdd u0 {4,D}
8   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1004,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Cs",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CO  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cs  u0 {1,S}
8    O2d u0 {4,D}
9    O2d u0 {5,D}
10   O2d u0 {6,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1005,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)Cs",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CO  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cs  u0 {1,S}
8    O2d u0 {4,D}
9    O2d u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1006,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CO  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cs  u0 {1,S}
8    O2d u0 {4,D}
9    C   u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1007,
    label = "Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)Cs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cd u0 {1,S} {8,D}
5   Cs u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
8   C  u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1008,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cd u0 {1,S} {8,D}
5   Cs u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
8   Cd u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.32,5.86,7.57,8.54,9.22,9.36,8.45],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (2.54,'kcal/mol','+|-',0.26),
        S298 = (-33.96,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = """Cs-CdCdCdCs BOZZELLI =3D Cs/Cs2/Cd2 + (Cs/Cs3/Cd - Cs/Cs4)""",
    longDesc = 
"""

""",
)

entry(
    index = 1009,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cs  u0 {1,S}
6   Cd  u0 {2,D}
7   Cd  u0 {3,D}
8   Cdd u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1010,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   Cs  u0 {1,S}
7   Cd  u0 {3,D}
8   Cd  u0 {4,D}
9   O2d u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)CsCsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1011,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-S2d)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   Cs  u0 {1,S}
7   Cd  u0 {3,D}
8   Cd  u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1012,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   Cs  u0 {1,S}
7   Cd  u0 {3,D}
8   Cd  u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1013,
    label = "Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cs  u0 {1,S}
6   Cd  u0 {2,D}
7   Cdd u0 {3,D}
8   Cdd u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1014,
    label = "Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Cs",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cs  u0 {1,S}
8    Cd  u0 {4,D}
9    O2d u0 {5,D}
10   O2d u0 {6,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1015,
    label = "Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-Cd)Cs",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cs  u0 {1,S}
8    Cd  u0 {4,D}
9    O2d u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1016,
    label = "Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-S2d)Cs",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cs  u0 {1,S}
8    Cd  u0 {4,D}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1017,
    label = "Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-Cd)Cs",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cs  u0 {1,S}
8    Cd  u0 {4,D}
9    S2d u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1018,
    label = "Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cs  u0 {1,S}
8    Cd  u0 {4,D}
9    C   u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1019,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cs  u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
8   Cdd u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1020,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Cs",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    Cs  u0 {1,S}
9    O2d u0 {5,D}
10   O2d u0 {6,D}
11   O2d u0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1021,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)Cs",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    Cs  u0 {1,S}
9    O2d u0 {5,D}
10   O2d u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1022,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    Cs  u0 {1,S}
9    O2d u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1023,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)Cs",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    Cs  u0 {1,S}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
11   S2d u0 {7,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1024,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-Cd)Cs",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    Cs  u0 {1,S}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1025,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    Cs  u0 {1,S}
9    S2d u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1026,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    Cs  u0 {1,S}
9    C   u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1027,
    label = "Cs-CtCdsCdsCs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Ct      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   Cs      u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1028,
    label = "Cs-(Cds-O2d)(Cds-O2d)CtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   CO  u0 {1,S} {7,D}
4   Ct  u0 {1,S}
5   Cs  u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1029,
    label = "Cs-(Cds-O2d)(Cds-Cd)CtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   Cs  u0 {1,S}
6   C   u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)CtCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1030,
    label = "Cs-(Cds-O2d)(Cds-Cds)CtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   Cs  u0 {1,S}
6   Cd  u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1031,
    label = "Cs-(Cds-O2d)(Cds-Cdd)CtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   Cs  u0 {1,S}
6   Cdd u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cdd-Cd)CtCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1032,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)CtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   Cs  u0 {1,S}
7   O2d u0 {3,D}
8   O2d u0 {4,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1033,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)CtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   Cs  u0 {1,S}
7   O2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)CtCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1034,
    label = "Cs-(Cds-Cd)(Cds-Cd)CtCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Ct u0 {1,S}
5   Cs u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1035,
    label = "Cs-(Cds-Cds)(Cds-Cds)CtCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Ct u0 {1,S}
5   Cs u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1036,
    label = "Cs-(Cds-Cdd)(Cds-Cds)CtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Ct  u0 {1,S}
5   Cs  u0 {1,S}
6   Cdd u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cds)CtCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1037,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cds)CtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   Cs  u0 {1,S}
7   Cd  u0 {3,D}
8   O2d u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1038,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cds)CtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   Cs  u0 {1,S}
7   Cd  u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1039,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   Cs  u0 {1,S}
7   Cd  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1040,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)CtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Ct  u0 {1,S}
5   Cs  u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1041,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Ct  u0 {1,S}
7   Cs  u0 {1,S}
8   O2d u0 {4,D}
9   O2d u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1042,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Ct  u0 {1,S}
7   Cs  u0 {1,S}
8   O2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)(Cds-Cds)CtCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1043,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Ct  u0 {1,S}
7   Cs  u0 {1,S}
8   S2d u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1044,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Ct  u0 {1,S}
7   Cs  u0 {1,S}
8   S2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1045,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Ct  u0 {1,S}
7   Cs  u0 {1,S}
8   C   u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1046,
    label = "Cs-CbCdsCdsCs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   Cs      u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CbCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1047,
    label = "Cs-(Cds-O2d)(Cds-O2d)CbCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   CO  u0 {1,S} {7,D}
4   Cb  u0 {1,S}
5   Cs  u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1048,
    label = "Cs-(Cds-O2d)(Cds-Cd)CbCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   Cs  u0 {1,S}
6   C   u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)CbCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1049,
    label = "Cs-(Cds-O2d)(Cds-Cds)CbCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   Cs  u0 {1,S}
6   Cd  u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1050,
    label = "Cs-(Cds-O2d)(Cds-Cdd)CbCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   Cs  u0 {1,S}
6   Cdd u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cdd-Cd)CbCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1051,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)CbCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   Cs  u0 {1,S}
7   O2d u0 {3,D}
8   O2d u0 {4,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1052,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)CbCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   Cs  u0 {1,S}
7   O2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)CbCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1053,
    label = "Cs-(Cds-Cd)(Cds-Cd)CbCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cb u0 {1,S}
5   Cs u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CbCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1054,
    label = "Cs-(Cds-Cds)(Cds-Cds)CbCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cb u0 {1,S}
5   Cs u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1055,
    label = "Cs-(Cds-Cdd)(Cds-Cds)CbCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cb  u0 {1,S}
5   Cs  u0 {1,S}
6   Cdd u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cds)CbCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1056,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cds)CbCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   Cs  u0 {1,S}
7   Cd  u0 {3,D}
8   O2d u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1057,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cds)CbCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   Cs  u0 {1,S}
7   Cd  u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1058,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CbCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   Cs  u0 {1,S}
7   Cd  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CbCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1059,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)CbCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cb  u0 {1,S}
5   Cs  u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1060,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CbCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   Cs  u0 {1,S}
8   O2d u0 {4,D}
9   O2d u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1061,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CbCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   Cs  u0 {1,S}
8   O2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)(Cds-Cds)CbCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1062,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CbCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   Cs  u0 {1,S}
8   S2d u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1063,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CbCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   Cs  u0 {1,S}
8   S2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1064,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   Cs  u0 {1,S}
8   C   u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CbCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1065,
    label = "Cs-CtCtCdsCs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Ct      u0 {1,S}
3   Ct      u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   Cs      u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CtCtCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1066,
    label = "Cs-(Cds-O2d)CtCtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   Ct  u0 {1,S}
5   Cs  u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1067,
    label = "Cs-(Cds-Cd)CtCtCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
5   Cs u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)CtCtCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1068,
    label = "Cs-(Cds-Cds)CtCtCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
5   Cs u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.99,7.36,8.89,9.58,9.76,9.16,7.25],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (5.1,'kcal/mol','+|-',0.26),
        S298 = (-34.88,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = """Cs-CtCtCdCs BOZZELLI =3D Cs/Cd2/Cs2 + (Cs/Cs3/Ct - Cs/Cs4)""",
    longDesc = 
"""

""",
)

entry(
    index = 1069,
    label = "Cs-(Cds-Cdd)CtCtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   Ct  u0 {1,S}
5   Cs  u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CtCtCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1070,
    label = "Cs-(Cds-Cdd-O2d)CtCtCs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   Cs  u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1071,
    label = "Cs-(Cds-Cdd-S2d)CtCtCs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   Cs  u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1072,
    label = "Cs-(Cds-Cdd-Cd)CtCtCs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   Cs  u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)CtCtCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1073,
    label = "Cs-CbCtCdsCs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   Ct      u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   Cs      u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CbCtCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1074,
    label = "Cs-(Cds-O2d)CbCtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Ct  u0 {1,S}
5   Cs  u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)CtCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1075,
    label = "Cs-(Cds-Cd)CbCtCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Ct u0 {1,S}
5   Cs u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)CbCtCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1076,
    label = "Cs-(Cds-Cds)CbCtCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Ct u0 {1,S}
5   Cs u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.99,7.36,8.89,9.58,9.76,9.16,7.25],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (5.1,'kcal/mol','+|-',0.26),
        S298 = (-34.88,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = """Cs-CbCtCdCs BOZZELLI =3D Cs/Cb/Cd/Cs2 + (Cs/Cs3/Ct - Cs/Cs4)""",
    longDesc = 
"""

""",
)

entry(
    index = 1077,
    label = "Cs-(Cds-Cdd)CbCtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Ct  u0 {1,S}
5   Cs  u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CbCtCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1078,
    label = "Cs-(Cds-Cdd-O2d)CbCtCs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   Cs  u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)(Cds-Cds)CtCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1079,
    label = "Cs-(Cds-Cdd-S2d)CbCtCs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   Cs  u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1080,
    label = "Cs-(Cds-Cdd-Cd)CbCtCs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   Cs  u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.99,7.36,8.89,9.58,9.76,9.16,7.25],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (5.1,'kcal/mol','+|-',0.26),
        S298 = (-34.88,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = """Cs-CbCtCdCs BOZZELLI =3D Cs/Cb/Cd/Cs2 + (Cs/Cs3/Ct - Cs/Cs4)""",
    longDesc = 
"""

""",
)

entry(
    index = 1081,
    label = "Cs-CbCbCdsCs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   Cb      u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   Cs      u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CbCbCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1082,
    label = "Cs-(Cds-O2d)CbCbCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
5   Cs  u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1083,
    label = "Cs-(Cds-Cd)CbCbCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   Cs u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)CbCbCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1084,
    label = "Cs-(Cds-Cds)CbCbCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   Cs u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.99,7.36,8.89,9.58,9.76,9.16,7.25],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (5.1,'kcal/mol','+|-',0.26),
        S298 = (-34.88,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = """Cs-CbCbCdCs BOZZELLI =3D Cs/Cs2/Cb2 + (Cs/Cs3/Cd - Cs/Cs4)""",
    longDesc = 
"""

""",
)

entry(
    index = 1085,
    label = "Cs-(Cds-Cdd)CbCbCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
5   Cs  u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CbCbCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1086,
    label = "Cs-(Cds-Cdd-O2d)CbCbCs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   Cs  u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1087,
    label = "Cs-(Cds-Cdd-S2d)CbCbCs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   Cs  u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1088,
    label = "Cs-(Cds-Cdd-Cd)CbCbCs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   Cs  u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)CbCbCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1089,
    label = "Cs-CtCtCtCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
5   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.37,8.11,9.55,10.1,10.03,9.36,6.65],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (6.23,'kcal/mol','+|-',0.26),
        S298 = (-35.34,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = """Cs-CtCtCtCs BOZZELLI =3D Cs/Cs2/Ct2 + (Cs/Cs3/Ct - Cs/Cs4)""",
    longDesc = 
"""

""",
)

entry(
    index = 1090,
    label = "Cs-CbCtCtCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
5   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.37,8.11,9.55,10.1,10.03,9.36,6.65],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (6.23,'kcal/mol','+|-',0.26),
        S298 = (-35.34,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = """Cs-CbCtCtCs BOZZELLI =3D Cs/Cs2/Cb/Ct + (Cs/Cs3/Ct - Cs/Cs4)""",
    longDesc = 
"""

""",
)

entry(
    index = 1091,
    label = "Cs-CbCbCtCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   Ct u0 {1,S}
5   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.37,8.11,9.55,10.1,10.03,9.36,6.65],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (6.43,'kcal/mol','+|-',0.26),
        S298 = (-35.34,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = """Cs-CbCbCtCs BOZZELLI =3D Cs/Cs2/Cb2 + (Cs/Cs3/Ct - Cs/Cs4)""",
    longDesc = 
"""

""",
)

entry(
    index = 1092,
    label = "Cs-CbCbCbCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.37,8.11,9.55,10.1,10.03,9.36,6.65],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (6.23,'kcal/mol','+|-',0.26),
        S298 = (-35.34,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = """Cs-CbCbCbCs BOZZELLI =3D Cs/Cs2/Cb2 + (Cs/Cs3/Cb - Cs/Cs4)""",
    longDesc = 
"""

""",
)

entry(
    index = 1093,
    label = "Cs-CdsCdsCdsCds",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   [Cd,CO] u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1094,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)(Cds-O2d)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   CO  u0 {1,S} {7,D}
4   CO  u0 {1,S} {8,D}
5   CO  u0 {1,S} {9,D}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
8   O2d u0 {4,D}
9   O2d u0 {5,D}
""",
    thermo = 'Cs-CsCsCsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1095,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)(Cds-Cd)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   CO  u0 {1,S} {8,D}
4   CO  u0 {1,S} {9,D}
5   Cd  u0 {1,S} {6,D}
6   C   u0 {5,D}
7   O2d u0 {2,D}
8   O2d u0 {3,D}
9   O2d u0 {4,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1096,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)(Cds-Cds)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   CO  u0 {1,S} {8,D}
4   CO  u0 {1,S} {9,D}
5   Cd  u0 {1,S} {6,D}
6   Cd  u0 {5,D}
7   O2d u0 {2,D}
8   O2d u0 {3,D}
9   O2d u0 {4,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1097,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)(Cds-Cdd)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   CO  u0 {1,S} {8,D}
4   CO  u0 {1,S} {9,D}
5   Cd  u0 {1,S} {6,D}
6   Cdd u0 {5,D}
7   O2d u0 {2,D}
8   O2d u0 {3,D}
9   O2d u0 {4,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1098,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    CO  u0 {1,S} {7,D}
4    CO  u0 {1,S} {8,D}
5    CO  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    O2d u0 {3,D}
8    O2d u0 {4,D}
9    O2d u0 {5,D}
10   O2d u0 {6,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)CsCsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1099,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    CO  u0 {1,S} {7,D}
4    CO  u0 {1,S} {8,D}
5    CO  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    O2d u0 {3,D}
8    O2d u0 {4,D}
9    O2d u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1100,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cd)(Cds-Cd)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {8,D}
3   CO  u0 {1,S} {9,D}
4   Cd  u0 {1,S} {6,D}
5   Cd  u0 {1,S} {7,D}
6   C   u0 {4,D}
7   C   u0 {5,D}
8   O2d u0 {2,D}
9   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([42.49,50.96,52.27,50.54,45.33,41.1,35.7],'J/(mol*K)','+|-',[5.08,5.08,5.08,5.08,5.08,5.08,5.08]),
        H298 = (25.2,'kJ/mol','+|-',4.33),
        S298 = (-168.67,'J/(mol*K)','+|-',5.92),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 1101,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)(Cds-Cds)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {8,D}
3   CO  u0 {1,S} {9,D}
4   Cd  u0 {1,S} {6,D}
5   Cd  u0 {1,S} {7,D}
6   Cd  u0 {4,D}
7   Cd  u0 {5,D}
8   O2d u0 {2,D}
9   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-O2d)CsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1102,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd)(Cds-Cds)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {8,D}
3   CO  u0 {1,S} {9,D}
4   Cd  u0 {1,S} {6,D}
5   Cd  u0 {1,S} {7,D}
6   Cdd u0 {4,D}
7   Cd  u0 {5,D}
8   O2d u0 {2,D}
9   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1103,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    CO  u0 {1,S} {8,D}
4    CO  u0 {1,S} {9,D}
5    Cd  u0 {1,S} {7,D}
6    Cdd u0 {2,D} {10,D}
7    Cd  u0 {5,D}
8    O2d u0 {3,D}
9    O2d u0 {4,D}
10   O2d u0 {6,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1104,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cds)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    CO  u0 {1,S} {8,D}
4    CO  u0 {1,S} {9,D}
5    Cd  u0 {1,S} {7,D}
6    Cdd u0 {2,D} {10,D}
7    Cd  u0 {5,D}
8    O2d u0 {3,D}
9    O2d u0 {4,D}
10   C   u0 {6,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1105,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd)(Cds-Cdd)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {8,D}
3   CO  u0 {1,S} {9,D}
4   Cd  u0 {1,S} {6,D}
5   Cd  u0 {1,S} {7,D}
6   Cdd u0 {4,D}
7   Cdd u0 {5,D}
8   O2d u0 {2,D}
9   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1106,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    CO  u0 {1,S} {8,D}
5    CO  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    O2d u0 {4,D}
9    O2d u0 {5,D}
10   O2d u0 {6,D}
11   O2d u0 {7,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1107,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    CO  u0 {1,S} {8,D}
5    CO  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    O2d u0 {4,D}
9    O2d u0 {5,D}
10   O2d u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1108,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    CO  u0 {1,S} {8,D}
5    CO  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    O2d u0 {4,D}
9    O2d u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1109,
    label = "Cs-(Cds-O2d)(Cds-Cd)(Cds-Cd)(Cds-Cd)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {9,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cd  u0 {1,S} {8,D}
6   C   u0 {3,D}
7   C   u0 {4,D}
8   C   u0 {5,D}
9   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1110,
    label = "Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cds)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {9,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cd  u0 {1,S} {8,D}
6   Cd  u0 {3,D}
7   Cd  u0 {4,D}
8   Cd  u0 {5,D}
9   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)CsCsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1111,
    label = "Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cdd)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {9,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cd  u0 {1,S} {8,D}
6   Cd  u0 {3,D}
7   Cd  u0 {4,D}
8   Cdd u0 {5,D}
9   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1112,
    label = "Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    CO  u0 {1,S} {9,D}
4    Cd  u0 {1,S} {7,D}
5    Cd  u0 {1,S} {8,D}
6    Cdd u0 {2,D} {10,D}
7    Cd  u0 {4,D}
8    Cd  u0 {5,D}
9    O2d u0 {3,D}
10   O2d u0 {6,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cdd-O2d)CsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1113,
    label = "Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    CO  u0 {1,S} {9,D}
4    Cd  u0 {1,S} {7,D}
5    Cd  u0 {1,S} {8,D}
6    Cdd u0 {2,D} {10,D}
7    Cd  u0 {4,D}
8    Cd  u0 {5,D}
9    O2d u0 {3,D}
10   C   u0 {6,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1114,
    label = "Cs-(Cds-O2d)(Cds-Cds)(Cds-Cdd)(Cds-Cdd)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {9,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cd  u0 {1,S} {8,D}
6   Cd  u0 {3,D}
7   Cdd u0 {4,D}
8   Cdd u0 {5,D}
9   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1115,
    label = "Cs-(Cds-O2d)(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    CO  u0 {1,S} {9,D}
5    Cd  u0 {1,S} {8,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cd  u0 {5,D}
9    O2d u0 {4,D}
10   O2d u0 {6,D}
11   O2d u0 {7,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1116,
    label = "Cs-(Cds-O2d)(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    CO  u0 {1,S} {9,D}
5    Cd  u0 {1,S} {8,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cd  u0 {5,D}
9    O2d u0 {4,D}
10   O2d u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1117,
    label = "Cs-(Cds-O2d)(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    CO  u0 {1,S} {9,D}
5    Cd  u0 {1,S} {8,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cd  u0 {5,D}
9    O2d u0 {4,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1118,
    label = "Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {9,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cd  u0 {1,S} {8,D}
6   Cdd u0 {3,D}
7   Cdd u0 {4,D}
8   Cdd u0 {5,D}
9   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1119,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    CO  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    O2d u0 {5,D}
10   O2d u0 {6,D}
11   O2d u0 {7,D}
12   O2d u0 {8,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1120,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    CO  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    O2d u0 {5,D}
10   O2d u0 {6,D}
11   O2d u0 {7,D}
12   C   u0 {8,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1121,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    CO  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    O2d u0 {5,D}
10   O2d u0 {6,D}
11   C   u0 {7,D}
12   C   u0 {8,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1122,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    CO  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    O2d u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
12   C   u0 {8,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1123,
    label = "Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)(Cds-Cd)",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cd u0 {1,S} {8,D}
5   Cd u0 {1,S} {9,D}
6   C  u0 {2,D}
7   C  u0 {3,D}
8   C  u0 {4,D}
9   C  u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1124,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cd u0 {1,S} {8,D}
5   Cd u0 {1,S} {9,D}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
8   Cd u0 {4,D}
9   Cd u0 {5,D}
""",
    thermo = 'Cs-CsCsCsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1125,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cd  u0 {1,S} {9,D}
6   Cd  u0 {2,D}
7   Cd  u0 {3,D}
8   Cd  u0 {4,D}
9   Cdd u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1126,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cd  u0 {3,D}
8    Cd  u0 {4,D}
9    Cd  u0 {5,D}
10   O2d u0 {6,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)CsCsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1127,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-S2d)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cd  u0 {3,D}
8    Cd  u0 {4,D}
9    Cd  u0 {5,D}
10   S2d u0 {6,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1128,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cd  u0 {3,D}
8    Cd  u0 {4,D}
9    Cd  u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1129,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)(Cds-Cdd)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cd  u0 {1,S} {9,D}
6   Cd  u0 {2,D}
7   Cd  u0 {3,D}
8   Cdd u0 {4,D}
9   Cdd u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1130,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cd  u0 {4,D}
9    Cd  u0 {5,D}
10   O2d u0 {6,D}
11   O2d u0 {7,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1131,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cd  u0 {4,D}
9    Cd  u0 {5,D}
10   O2d u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1132,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-S2d)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cd  u0 {4,D}
9    Cd  u0 {5,D}
10   S2d u0 {6,D}
11   S2d u0 {7,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1133,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cd  u0 {4,D}
9    Cd  u0 {5,D}
10   S2d u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1134,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cd  u0 {4,D}
9    Cd  u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1135,
    label = "Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cd  u0 {1,S} {9,D}
6   Cd  u0 {2,D}
7   Cdd u0 {3,D}
8   Cdd u0 {4,D}
9   Cdd u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1136,
    label = "Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    Cd  u0 {5,D}
10   O2d u0 {6,D}
11   O2d u0 {7,D}
12   O2d u0 {8,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1137,
    label = "Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    Cd  u0 {5,D}
10   O2d u0 {6,D}
11   O2d u0 {7,D}
12   C   u0 {8,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1138,
    label = "Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    Cd  u0 {5,D}
10   O2d u0 {6,D}
11   C   u0 {7,D}
12   C   u0 {8,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1139,
    label = "Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    Cd  u0 {5,D}
10   S2d u0 {6,D}
11   S2d u0 {7,D}
12   S2d u0 {8,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1140,
    label = "Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    Cd  u0 {5,D}
10   S2d u0 {6,D}
11   S2d u0 {7,D}
12   C   u0 {8,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1141,
    label = "Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    Cd  u0 {5,D}
10   S2d u0 {6,D}
11   C   u0 {7,D}
12   C   u0 {8,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1142,
    label = "Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    Cd  u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
12   C   u0 {8,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1143,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cd  u0 {1,S} {9,D}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
8   Cdd u0 {4,D}
9   Cdd u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1144,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    Cdd u0 {5,D} {13,D}
10   O2d u0 {6,D}
11   O2d u0 {7,D}
12   O2d u0 {8,D}
13   O2d u0 {9,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1145,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    Cdd u0 {5,D} {13,D}
10   O2d u0 {6,D}
11   O2d u0 {7,D}
12   O2d u0 {8,D}
13   C   u0 {9,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1146,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    Cdd u0 {5,D} {13,D}
10   O2d u0 {6,D}
11   O2d u0 {7,D}
12   C   u0 {8,D}
13   C   u0 {9,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1147,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    Cdd u0 {5,D} {13,D}
10   O2d u0 {6,D}
11   C   u0 {7,D}
12   C   u0 {8,D}
13   C   u0 {9,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1148,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    Cdd u0 {5,D} {13,D}
10   S2d u0 {6,D}
11   S2d u0 {7,D}
12   S2d u0 {8,D}
13   S2d u0 {9,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1149,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    Cdd u0 {5,D} {13,D}
10   S2d u0 {6,D}
11   S2d u0 {7,D}
12   S2d u0 {8,D}
13   C   u0 {9,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1150,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    Cdd u0 {5,D} {13,D}
10   S2d u0 {6,D}
11   S2d u0 {7,D}
12   C   u0 {8,D}
13   C   u0 {9,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1151,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    Cdd u0 {5,D} {13,D}
10   S2d u0 {6,D}
11   C   u0 {7,D}
12   C   u0 {8,D}
13   C   u0 {9,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1152,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    Cdd u0 {5,D} {13,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
12   C   u0 {8,D}
13   C   u0 {9,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1153,
    label = "Cs-CtCdsCdsCds",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Ct      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   [Cd,CO] u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1154,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   CO  u0 {1,S} {7,D}
4   CO  u0 {1,S} {8,D}
5   Ct  u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
8   O2d u0 {4,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1155,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cd)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   Ct  u0 {1,S}
6   C   u0 {4,D}
7   O2d u0 {2,D}
8   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)Ct',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1156,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   Ct  u0 {1,S}
6   Cd  u0 {4,D}
7   O2d u0 {2,D}
8   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1157,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   Ct  u0 {1,S}
6   Cdd u0 {4,D}
7   O2d u0 {2,D}
8   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)Ct',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1158,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {7,D}
4   CO  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   Ct  u0 {1,S}
7   O2d u0 {3,D}
8   O2d u0 {4,D}
9   O2d u0 {5,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1159,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {7,D}
4   CO  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   Ct  u0 {1,S}
7   O2d u0 {3,D}
8   O2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)Ct',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1160,
    label = "Cs-(Cds-O2d)(Cds-Cd)(Cds-Cd)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Ct  u0 {1,S}
6   C   u0 {3,D}
7   C   u0 {4,D}
8   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1161,
    label = "Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Ct  u0 {1,S}
6   Cd  u0 {3,D}
7   Cd  u0 {4,D}
8   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1162,
    label = "Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cds)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Ct  u0 {1,S}
6   Cdd u0 {3,D}
7   Cd  u0 {4,D}
8   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cds)Ct',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1163,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {9,D}
6   Ct  u0 {1,S}
7   Cd  u0 {4,D}
8   O2d u0 {3,D}
9   O2d u0 {5,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1164,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cds)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {9,D}
6   Ct  u0 {1,S}
7   Cd  u0 {4,D}
8   O2d u0 {3,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1165,
    label = "Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cdd)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Ct  u0 {1,S}
6   Cdd u0 {3,D}
7   Cdd u0 {4,D}
8   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1166,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Ct",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CO  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Ct  u0 {1,S}
8    O2d u0 {4,D}
9    O2d u0 {5,D}
10   O2d u0 {6,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1167,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)Ct",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CO  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Ct  u0 {1,S}
8    O2d u0 {4,D}
9    O2d u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)Ct',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1168,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CO  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Ct  u0 {1,S}
8    O2d u0 {4,D}
9    C   u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1169,
    label = "Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)Ct",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cd u0 {1,S} {8,D}
5   Ct u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
8   C  u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1170,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Ct",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cd u0 {1,S} {8,D}
5   Ct u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
8   Cd u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1171,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Ct  u0 {1,S}
6   Cd  u0 {2,D}
7   Cd  u0 {3,D}
8   Cdd u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)Ct',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1172,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   Ct  u0 {1,S}
7   Cd  u0 {3,D}
8   Cd  u0 {4,D}
9   O2d u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1173,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-S2d)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   Ct  u0 {1,S}
7   Cd  u0 {3,D}
8   Cd  u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1174,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   Ct  u0 {1,S}
7   Cd  u0 {3,D}
8   Cd  u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1175,
    label = "Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Ct  u0 {1,S}
6   Cd  u0 {2,D}
7   Cdd u0 {3,D}
8   Cdd u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1176,
    label = "Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Ct",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Ct  u0 {1,S}
8    Cd  u0 {4,D}
9    O2d u0 {5,D}
10   O2d u0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1177,
    label = "Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-Cd)Ct",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Ct  u0 {1,S}
8    Cd  u0 {4,D}
9    O2d u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)Ct',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1178,
    label = "Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-S2d)Ct",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Ct  u0 {1,S}
8    Cd  u0 {4,D}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1179,
    label = "Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-Cd)Ct",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Ct  u0 {1,S}
8    Cd  u0 {4,D}
9    S2d u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1180,
    label = "Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Ct  u0 {1,S}
8    Cd  u0 {4,D}
9    C   u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1181,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Ct  u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
8   Cdd u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1182,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Ct",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    Ct  u0 {1,S}
9    O2d u0 {5,D}
10   O2d u0 {6,D}
11   O2d u0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1183,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)Ct",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    Ct  u0 {1,S}
9    O2d u0 {5,D}
10   O2d u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Ct',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1184,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    Ct  u0 {1,S}
9    O2d u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)Ct',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1185,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)Ct",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    Ct  u0 {1,S}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
11   S2d u0 {7,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1186,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-Cd)Ct",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    Ct  u0 {1,S}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1187,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    Ct  u0 {1,S}
9    S2d u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1188,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    Ct  u0 {1,S}
9    C   u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1189,
    label = "Cs-CbCdsCdsCds",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   [Cd,CO] u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1190,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   CO  u0 {1,S} {7,D}
4   CO  u0 {1,S} {8,D}
5   Cb  u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
8   O2d u0 {4,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1191,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cd)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   Cb  u0 {1,S}
6   C   u0 {4,D}
7   O2d u0 {2,D}
8   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)Cb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1192,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   Cb  u0 {1,S}
6   Cd  u0 {4,D}
7   O2d u0 {2,D}
8   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1193,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   Cb  u0 {1,S}
6   Cdd u0 {4,D}
7   O2d u0 {2,D}
8   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)Cb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1194,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {7,D}
4   CO  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   Cb  u0 {1,S}
7   O2d u0 {3,D}
8   O2d u0 {4,D}
9   O2d u0 {5,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1195,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {7,D}
4   CO  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   Cb  u0 {1,S}
7   O2d u0 {3,D}
8   O2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)Cb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1196,
    label = "Cs-(Cds-O2d)(Cds-Cd)(Cds-Cd)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cb  u0 {1,S}
6   C   u0 {3,D}
7   C   u0 {4,D}
8   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)Cb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1197,
    label = "Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cb  u0 {1,S}
6   Cd  u0 {3,D}
7   Cd  u0 {4,D}
8   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1198,
    label = "Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cds)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cb  u0 {1,S}
6   Cdd u0 {3,D}
7   Cd  u0 {4,D}
8   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cds)Cb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1199,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {9,D}
6   Cb  u0 {1,S}
7   Cd  u0 {4,D}
8   O2d u0 {3,D}
9   O2d u0 {5,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1200,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cds)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {9,D}
6   Cb  u0 {1,S}
7   Cd  u0 {4,D}
8   O2d u0 {3,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)Cb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1201,
    label = "Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cdd)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cb  u0 {1,S}
6   Cdd u0 {3,D}
7   Cdd u0 {4,D}
8   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1202,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Cb",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CO  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cb  u0 {1,S}
8    O2d u0 {4,D}
9    O2d u0 {5,D}
10   O2d u0 {6,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1203,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)Cb",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CO  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cb  u0 {1,S}
8    O2d u0 {4,D}
9    O2d u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)Cb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1204,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CO  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cb  u0 {1,S}
8    O2d u0 {4,D}
9    C   u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)Cb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1205,
    label = "Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)Cb",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cd u0 {1,S} {8,D}
5   Cb u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
8   C  u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1206,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cb",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cd u0 {1,S} {8,D}
5   Cb u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
8   Cd u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1207,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cb  u0 {1,S}
6   Cd  u0 {2,D}
7   Cd  u0 {3,D}
8   Cdd u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)Cb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1208,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   Cb  u0 {1,S}
7   Cd  u0 {3,D}
8   Cd  u0 {4,D}
9   O2d u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1209,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-S2d)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   Cb  u0 {1,S}
7   Cd  u0 {3,D}
8   Cd  u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1210,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   Cb  u0 {1,S}
7   Cd  u0 {3,D}
8   Cd  u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1211,
    label = "Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cb  u0 {1,S}
6   Cd  u0 {2,D}
7   Cdd u0 {3,D}
8   Cdd u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1212,
    label = "Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Cb",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cb  u0 {1,S}
8    Cd  u0 {4,D}
9    O2d u0 {5,D}
10   O2d u0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1213,
    label = "Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-Cd)Cb",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cb  u0 {1,S}
8    Cd  u0 {4,D}
9    O2d u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)Cb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1214,
    label = "Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-S2d)Cb",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cb  u0 {1,S}
8    Cd  u0 {4,D}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1215,
    label = "Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-Cd)Cb",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cb  u0 {1,S}
8    Cd  u0 {4,D}
9    S2d u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1216,
    label = "Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cb  u0 {1,S}
8    Cd  u0 {4,D}
9    C   u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1217,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cb  u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
8   Cdd u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1218,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Cb",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    Cb  u0 {1,S}
9    O2d u0 {5,D}
10   O2d u0 {6,D}
11   O2d u0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1219,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)Cb",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    Cb  u0 {1,S}
9    O2d u0 {5,D}
10   O2d u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Cb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1220,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    Cb  u0 {1,S}
9    O2d u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)Cb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1221,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)Cb",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    Cb  u0 {1,S}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
11   S2d u0 {7,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1222,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-Cd)Cb",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    Cb  u0 {1,S}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1223,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    Cb  u0 {1,S}
9    S2d u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1224,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    Cb  u0 {1,S}
9    C   u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1225,
    label = "Cs-CtCtCdsCds",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Ct      u0 {1,S}
3   Ct      u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   [Cd,CO] u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtCt',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1226,
    label = "Cs-(Cds-O2d)(Cds-O2d)CtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   CO  u0 {1,S} {7,D}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1227,
    label = "Cs-(Cds-O2d)(Cds-Cd)CtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   C   u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)CtCt',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1228,
    label = "Cs-(Cds-O2d)(Cds-Cds)CtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   Cd  u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1229,
    label = "Cs-(Cds-O2d)(Cds-Cdd)CtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   Cdd u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cdd-Cd)CtCt',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1230,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)CtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   Ct  u0 {1,S}
7   O2d u0 {3,D}
8   O2d u0 {4,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1231,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)CtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   Ct  u0 {1,S}
7   O2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)CtCt',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1232,
    label = "Cs-(Cds-Cd)(Cds-Cd)CtCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Ct u0 {1,S}
5   Ct u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtCt',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1233,
    label = "Cs-(Cds-Cds)(Cds-Cds)CtCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Ct u0 {1,S}
5   Ct u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.61,7.3,8.97,9.69,9.84,9.42,7.36],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (5.48,'kcal/mol','+|-',0.26),
        S298 = (-34.5,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = """Cs-CtCtCdCd BOZZELLI =3D Cs/Cs/Cd/Ct2 + (Cs/Cs3/Cd - Cs/Cs4)""",
    longDesc = 
"""

""",
)

entry(
    index = 1234,
    label = "Cs-(Cds-Cdd)(Cds-Cds)CtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   Cdd u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cds)CtCt',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1235,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cds)CtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   Ct  u0 {1,S}
7   Cd  u0 {3,D}
8   O2d u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1236,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cds)CtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   Ct  u0 {1,S}
7   Cd  u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1237,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   Ct  u0 {1,S}
7   Cd  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtCt',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1238,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)CtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtCt',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1239,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Ct  u0 {1,S}
7   Ct  u0 {1,S}
8   O2d u0 {4,D}
9   O2d u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1240,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Ct  u0 {1,S}
7   Ct  u0 {1,S}
8   O2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)(Cds-Cds)CtCt',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1241,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Ct  u0 {1,S}
7   Ct  u0 {1,S}
8   S2d u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1242,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Ct  u0 {1,S}
7   Ct  u0 {1,S}
8   S2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1243,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Ct  u0 {1,S}
7   Ct  u0 {1,S}
8   C   u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtCt',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1244,
    label = "Cs-CbCtCdsCds",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   Ct      u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   [Cd,CO] u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CbCt',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1245,
    label = "Cs-(Cds-O2d)(Cds-O2d)CbCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   CO  u0 {1,S} {7,D}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)Ct',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1246,
    label = "Cs-(Cds-O2d)(Cds-Cd)CbCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   C   u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)CbCt',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1247,
    label = "Cs-(Cds-O2d)(Cds-Cds)CbCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   Cd  u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1248,
    label = "Cs-(Cds-O2d)(Cds-Cdd)CbCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   Cdd u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cdd-Cd)CbCt',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1249,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)CbCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   Ct  u0 {1,S}
7   O2d u0 {3,D}
8   O2d u0 {4,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)Ct',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1250,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)CbCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   Ct  u0 {1,S}
7   O2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)CbCt',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1251,
    label = "Cs-(Cds-Cd)(Cds-Cd)CbCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cb u0 {1,S}
5   Ct u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CbCt',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1252,
    label = "Cs-(Cds-Cds)(Cds-Cds)CbCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cb u0 {1,S}
5   Ct u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.61,7.3,8.97,9.69,9.84,9.42,7.36],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (5.48,'kcal/mol','+|-',0.26),
        S298 = (-34.5,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = """Cs-CbCtCdCd BOZZELLI =3D Cs/Cs/Cb/Cd2 + (Cs/Cs3/Ct - Cs/Cs4)""",
    longDesc = 
"""

""",
)

entry(
    index = 1253,
    label = "Cs-(Cds-Cdd)(Cds-Cds)CbCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   Cdd u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cds)CbCt',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1254,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cds)CbCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   Ct  u0 {1,S}
7   Cd  u0 {3,D}
8   O2d u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)Ct',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1255,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cds)CbCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   Ct  u0 {1,S}
7   Cd  u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1256,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CbCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   Ct  u0 {1,S}
7   Cd  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CbCt',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1257,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)CbCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbCt',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1258,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CbCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   Ct  u0 {1,S}
8   O2d u0 {4,D}
9   O2d u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Ct',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1259,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CbCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   Ct  u0 {1,S}
8   O2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)(Cds-Cds)CbCt',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1260,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CbCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   Ct  u0 {1,S}
8   S2d u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1261,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CbCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   Ct  u0 {1,S}
8   S2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1262,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   Ct  u0 {1,S}
8   C   u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CbCt',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1263,
    label = "Cs-CbCbCdsCds",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   Cb      u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   [Cd,CO] u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CbCb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1264,
    label = "Cs-(Cds-O2d)(Cds-O2d)CbCb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   CO  u0 {1,S} {7,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1265,
    label = "Cs-(Cds-O2d)(Cds-Cd)CbCb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   C   u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)CbCb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1266,
    label = "Cs-(Cds-O2d)(Cds-Cds)CbCb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   Cd  u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1267,
    label = "Cs-(Cds-O2d)(Cds-Cdd)CbCb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   Cdd u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cdd-Cd)CbCb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1268,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)CbCb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   Cb  u0 {1,S}
7   O2d u0 {3,D}
8   O2d u0 {4,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1269,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)CbCb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   Cb  u0 {1,S}
7   O2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)CbCb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1270,
    label = "Cs-(Cds-Cd)(Cds-Cd)CbCb",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cb u0 {1,S}
5   Cb u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CbCb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1271,
    label = "Cs-(Cds-Cds)(Cds-Cds)CbCb",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cb u0 {1,S}
5   Cb u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.61,7.3,8.97,9.69,9.84,9.42,7.36],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (5.48,'kcal/mol','+|-',0.26),
        S298 = (-34.5,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = """Cs-CbCbCdCd BOZZELLI =3D Cs/Cs/Cb2/Cd + (Cs/Cs3/Cd - Cs/Cs4)""",
    longDesc = 
"""

""",
)

entry(
    index = 1272,
    label = "Cs-(Cds-Cdd)(Cds-Cds)CbCb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   Cdd u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cds)CbCb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1273,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cds)CbCb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   Cb  u0 {1,S}
7   Cd  u0 {3,D}
8   O2d u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1274,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cds)CbCb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   Cb  u0 {1,S}
7   Cd  u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1275,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CbCb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   Cb  u0 {1,S}
7   Cd  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CbCb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1276,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)CbCb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbCb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1277,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CbCb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   Cb  u0 {1,S}
8   O2d u0 {4,D}
9   O2d u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1278,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CbCb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   Cb  u0 {1,S}
8   O2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)(Cds-Cds)CbCb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1279,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CbCb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   Cb  u0 {1,S}
8   S2d u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1280,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CbCb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   Cb  u0 {1,S}
8   S2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1281,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbCb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   Cb  u0 {1,S}
8   C   u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CbCb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1282,
    label = "Cs-CtCtCtCds",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Ct      u0 {1,S}
3   Ct      u0 {1,S}
4   Ct      u0 {1,S}
5   [Cd,CO] u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CtCtCt',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1283,
    label = "Cs-(Cds-O2d)CtCtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1284,
    label = "Cs-(Cds-Cd)CtCtCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
5   Ct u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1285,
    label = "Cs-(Cds-Cds)CtCtCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
5   Ct u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1286,
    label = "Cs-(Cds-Cdd)CtCtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CtCtCt',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1287,
    label = "Cs-(Cds-Cdd-O2d)CtCtCt",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   Ct  u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1288,
    label = "Cs-(Cds-Cdd-S2d)CtCtCt",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   Ct  u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1289,
    label = "Cs-(Cds-Cdd-Cd)CtCtCt",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   Ct  u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)CtCtCt',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1290,
    label = "Cs-CbCtCtCds",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   Ct      u0 {1,S}
4   Ct      u0 {1,S}
5   [Cd,CO] u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CbCtCt',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1291,
    label = "Cs-(Cds-O2d)CbCtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)CtCt',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1292,
    label = "Cs-(Cds-Cd)CbCtCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Ct u0 {1,S}
5   Ct u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)CbCtCt',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1293,
    label = "Cs-(Cds-Cds)CbCtCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Ct u0 {1,S}
5   Ct u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtCt',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1294,
    label = "Cs-(Cds-Cdd)CbCtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CbCtCt',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1295,
    label = "Cs-(Cds-Cdd-O2d)CbCtCt",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   Ct  u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)(Cds-Cds)CtCt',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1296,
    label = "Cs-(Cds-Cdd-S2d)CbCtCt",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   Ct  u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1297,
    label = "Cs-(Cds-Cdd-Cd)CbCtCt",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   Ct  u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)CbCtCt',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1298,
    label = "Cs-CbCbCtCds",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   Cb      u0 {1,S}
4   Ct      u0 {1,S}
5   [Cd,CO] u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CbCbCt',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1299,
    label = "Cs-(Cds-O2d)CbCbCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1300,
    label = "Cs-(Cds-Cd)CbCbCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   Ct u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)CbCbCt',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1301,
    label = "Cs-(Cds-Cds)CbCbCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   Ct u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1302,
    label = "Cs-(Cds-Cdd)CbCbCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CbCbCt',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1303,
    label = "Cs-(Cds-Cdd-O2d)CbCbCt",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   Ct  u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)Ct',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1304,
    label = "Cs-(Cds-Cdd-S2d)CbCbCt",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   Ct  u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1305,
    label = "Cs-(Cds-Cdd-Cd)CbCbCt",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   Ct  u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)CbCbCt',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1306,
    label = "Cs-CbCbCbCds",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   Cb      u0 {1,S}
4   Cb      u0 {1,S}
5   [Cd,CO] u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CbCbCb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1307,
    label = "Cs-(Cds-O2d)CbCbCb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1308,
    label = "Cs-(Cds-Cd)CbCbCb",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   Cb u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)CbCbCb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1309,
    label = "Cs-(Cds-Cds)CbCbCb",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   Cb u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1310,
    label = "Cs-(Cds-Cdd)CbCbCb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CbCbCb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1311,
    label = "Cs-(Cds-Cdd-O2d)CbCbCb",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   Cb  u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1312,
    label = "Cs-(Cds-Cdd-S2d)CbCbCb",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   Cb  u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1313,
    label = "Cs-(Cds-Cdd-Cd)CbCbCb",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   Cb  u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)CbCbCb',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1314,
    label = "Cs-CtCtCtCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
5   Ct u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1315,
    label = "Cs-CbCtCtCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
5   Ct u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CtCtCt',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1316,
    label = "Cs-CbCbCtCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   Ct u0 {1,S}
5   Ct u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtCt',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1317,
    label = "Cs-CbCbCbCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   Ct u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1318,
    label = "Cs-CbCbCbCb",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   Cb u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1319,
    label = "Cs-C=SCbCtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1320,
    label = "Cs-C=S(Cds-Cd)(Cds-Cd)(Cds-Cd)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {9,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cd  u0 {1,S} {8,D}
6   C   u0 {3,D}
7   C   u0 {4,D}
8   C   u0 {5,D}
9   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1321,
    label = "Cs-C=S(Cds-Cds)(Cds-Cds)(Cds-Cdd)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {9,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cd  u0 {1,S} {8,D}
6   Cd  u0 {3,D}
7   Cd  u0 {4,D}
8   Cdd u0 {5,D}
9   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1322,
    label = "Cs-C=S(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    CS  u0 {1,S} {9,D}
4    Cd  u0 {1,S} {7,D}
5    Cd  u0 {1,S} {8,D}
6    Cdd u0 {2,D} {10,D}
7    Cd  u0 {4,D}
8    Cd  u0 {5,D}
9    S2d u0 {3,D}
10   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1323,
    label = "Cs-C=S(Cds-Cds)(Cds-Cds)(Cds-Cdd-S2d)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    CS  u0 {1,S} {9,D}
4    Cd  u0 {1,S} {7,D}
5    Cd  u0 {1,S} {8,D}
6    Cdd u0 {2,D} {10,D}
7    Cd  u0 {4,D}
8    Cd  u0 {5,D}
9    S2d u0 {3,D}
10   S2d u0 {6,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1324,
    label = "Cs-C=S(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {9,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cd  u0 {1,S} {8,D}
6   Cdd u0 {3,D}
7   Cdd u0 {4,D}
8   Cdd u0 {5,D}
9   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1325,
    label = "Cs-C=S(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    CS  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    S2d u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
12   C   u0 {8,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1326,
    label = "Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    CS  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
11   C   u0 {7,D}
12   C   u0 {8,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1327,
    label = "Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    CS  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
11   S2d u0 {7,D}
12   S2d u0 {8,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1328,
    label = "Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    CS  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
11   S2d u0 {7,D}
12   C   u0 {8,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1329,
    label = "Cs-C=S(Cds-Cds)(Cds-Cds)(Cds-Cds)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {9,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cd  u0 {1,S} {8,D}
6   Cd  u0 {3,D}
7   Cd  u0 {4,D}
8   Cd  u0 {5,D}
9   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1330,
    label = "Cs-C=S(Cds-Cds)(Cds-Cdd)(Cds-Cdd)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {9,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cd  u0 {1,S} {8,D}
6   Cd  u0 {3,D}
7   Cdd u0 {4,D}
8   Cdd u0 {5,D}
9   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1331,
    label = "Cs-C=S(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-S2d)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    CS  u0 {1,S} {9,D}
5    Cd  u0 {1,S} {8,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cd  u0 {5,D}
9    S2d u0 {4,D}
10   S2d u0 {6,D}
11   S2d u0 {7,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1332,
    label = "Cs-C=S(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    CS  u0 {1,S} {9,D}
5    Cd  u0 {1,S} {8,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cd  u0 {5,D}
9    S2d u0 {4,D}
10   S2d u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1333,
    label = "Cs-C=S(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    CS  u0 {1,S} {9,D}
5    Cd  u0 {1,S} {8,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cd  u0 {5,D}
9    S2d u0 {4,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1334,
    label = "Cs-C=S(Cds-Cd)CtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   C   u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1335,
    label = "Cs-C=S(Cds-Cds)CtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   Cd  u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1336,
    label = "Cs-C=S(Cds-Cdd)CtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   Cdd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1337,
    label = "Cs-C=S(Cds-Cdd-S2d)CtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   Ct  u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1338,
    label = "Cs-C=S(Cds-Cdd-Cd)CtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   Ct  u0 {1,S}
7   S2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1339,
    label = "Cs-C=S(Cds-Cd)CtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   Cs  u0 {1,S}
6   C   u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1340,
    label = "Cs-C=S(Cds-Cds)CtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   Cs  u0 {1,S}
6   Cd  u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1341,
    label = "Cs-C=S(Cds-Cdd)CtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   Cs  u0 {1,S}
6   Cdd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1342,
    label = "Cs-C=S(Cds-Cdd-S2d)CtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   Cs  u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1343,
    label = "Cs-C=S(Cds-Cdd-Cd)CtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   Cs  u0 {1,S}
7   S2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1344,
    label = "Cs-C=SCbCbCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1345,
    label = "Cs-C=SCbCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1346,
    label = "Cs-C=SCbCbCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
5   Cs  u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1347,
    label = "Cs-C=SCtCtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1348,
    label = "Cs-C=S(Cds-Cd)(Cds-Cd)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cs  u0 {1,S}
6   C   u0 {3,D}
7   C   u0 {4,D}
8   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1349,
    label = "Cs-C=S(Cds-Cdd)(Cds-Cdd)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cs  u0 {1,S}
6   Cdd u0 {3,D}
7   Cdd u0 {4,D}
8   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1350,
    label = "Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-Cd)Cs",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CS  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cs  u0 {1,S}
8    S2d u0 {4,D}
9    S2d u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1351,
    label = "Cs-C=S(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CS  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cs  u0 {1,S}
8    S2d u0 {4,D}
9    C   u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1352,
    label = "Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-S2d)Cs",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CS  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cs  u0 {1,S}
8    S2d u0 {4,D}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1353,
    label = "Cs-C=S(Cds-Cds)(Cds-Cds)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cs  u0 {1,S}
6   Cd  u0 {3,D}
7   Cd  u0 {4,D}
8   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1354,
    label = "Cs-C=S(Cds-Cdd)(Cds-Cds)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cs  u0 {1,S}
6   Cdd u0 {3,D}
7   Cd  u0 {4,D}
8   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1355,
    label = "Cs-C=S(Cds-Cdd-S2d)(Cds-Cds)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CS  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {9,D}
6   Cs  u0 {1,S}
7   Cd  u0 {4,D}
8   S2d u0 {3,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1356,
    label = "Cs-C=S(Cds-Cdd-Cd)(Cds-Cds)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CS  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {9,D}
6   Cs  u0 {1,S}
7   Cd  u0 {4,D}
8   S2d u0 {3,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1357,
    label = "Cs-C=SC=SCtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   CS  u0 {1,S} {7,D}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   S2d u0 {2,D}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1358,
    label = "Cs-C=SCsCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.49,5.54,7.04,7.55,7.81,7.65,7.27],'cal/(mol*K)'),
        H298 = (4.38,'kcal/mol'),
        S298 = (-33.21,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 1359,
    label = "Cs-C=SCtCtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   Ct  u0 {1,S}
5   Cs  u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1360,
    label = "Cs-C=SC=SC=SCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   CS  u0 {1,S} {7,D}
4   CS  u0 {1,S} {8,D}
5   Ct  u0 {1,S}
6   S2d u0 {2,D}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1361,
    label = "Cs-C=SC=SC=SCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   CS  u0 {1,S} {7,D}
4   CS  u0 {1,S} {8,D}
5   Cs  u0 {1,S}
6   S2d u0 {2,D}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1362,
    label = "Cs-C=SC=SC=SC=S",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   CS  u0 {1,S} {7,D}
4   CS  u0 {1,S} {8,D}
5   CS  u0 {1,S} {9,D}
6   S2d u0 {2,D}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1363,
    label = "Cs-C=SCtCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1364,
    label = "Cs-C=SC=SC=SCb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   CS  u0 {1,S} {7,D}
4   CS  u0 {1,S} {8,D}
5   Cb  u0 {1,S}
6   S2d u0 {2,D}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1365,
    label = "Cs-C=SC=SC=S(Cds-Cd)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   CS  u0 {1,S} {8,D}
4   CS  u0 {1,S} {9,D}
5   Cd  u0 {1,S} {6,D}
6   C   u0 {5,D}
7   S2d u0 {2,D}
8   S2d u0 {3,D}
9   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1366,
    label = "Cs-C=SC=SC=S(Cds-Cdd)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   CS  u0 {1,S} {8,D}
4   CS  u0 {1,S} {9,D}
5   Cd  u0 {1,S} {6,D}
6   Cdd u0 {5,D}
7   S2d u0 {2,D}
8   S2d u0 {3,D}
9   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1367,
    label = "Cs-C=SC=SC=S(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    CS  u0 {1,S} {7,D}
4    CS  u0 {1,S} {8,D}
5    CS  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    S2d u0 {3,D}
8    S2d u0 {4,D}
9    S2d u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1368,
    label = "Cs-C=SC=SC=S(Cds-Cdd-S2d)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    CS  u0 {1,S} {7,D}
4    CS  u0 {1,S} {8,D}
5    CS  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    S2d u0 {3,D}
8    S2d u0 {4,D}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1369,
    label = "Cs-C=SC=SC=S(Cds-Cds)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   CS  u0 {1,S} {8,D}
4   CS  u0 {1,S} {9,D}
5   Cd  u0 {1,S} {6,D}
6   Cd  u0 {5,D}
7   S2d u0 {2,D}
8   S2d u0 {3,D}
9   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1370,
    label = "Cs-C=S(Cds-Cd)(Cds-Cd)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Ct  u0 {1,S}
6   C   u0 {3,D}
7   C   u0 {4,D}
8   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1371,
    label = "Cs-C=S(Cds-Cdd)(Cds-Cdd)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Ct  u0 {1,S}
6   Cdd u0 {3,D}
7   Cdd u0 {4,D}
8   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1372,
    label = "Cs-C=S(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CS  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Ct  u0 {1,S}
8    S2d u0 {4,D}
9    C   u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1373,
    label = "Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-S2d)Ct",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CS  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Ct  u0 {1,S}
8    S2d u0 {4,D}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1374,
    label = "Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-Cd)Ct",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CS  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Ct  u0 {1,S}
8    S2d u0 {4,D}
9    S2d u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1375,
    label = "Cs-C=S(Cds-Cds)(Cds-Cds)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Ct  u0 {1,S}
6   Cd  u0 {3,D}
7   Cd  u0 {4,D}
8   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1376,
    label = "Cs-C=S(Cds-Cdd)(Cds-Cds)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Ct  u0 {1,S}
6   Cdd u0 {3,D}
7   Cd  u0 {4,D}
8   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1377,
    label = "Cs-C=S(Cds-Cdd-Cd)(Cds-Cds)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CS  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {9,D}
6   Ct  u0 {1,S}
7   Cd  u0 {4,D}
8   S2d u0 {3,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1378,
    label = "Cs-C=S(Cds-Cdd-S2d)(Cds-Cds)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CS  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {9,D}
6   Ct  u0 {1,S}
7   Cd  u0 {4,D}
8   S2d u0 {3,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1379,
    label = "Cs-C=SC=SCtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   CS  u0 {1,S} {7,D}
4   Ct  u0 {1,S}
5   Cs  u0 {1,S}
6   S2d u0 {2,D}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1380,
    label = "Cs-C=SC=SCbCb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   CS  u0 {1,S} {7,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   S2d u0 {2,D}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1381,
    label = "Cs-C=S(Cds-Cd)CsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   C   u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1382,
    label = "Cs-C=S(Cds-Cds)CsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   Cd  u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1383,
    label = "Cs-C=S(Cds-Cdd)CsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   Cdd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1384,
    label = "Cs-C=S(Cds-Cdd-Cd)CsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   Cs  u0 {1,S}
7   S2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1385,
    label = "Cs-C=S(Cds-Cdd-S2d)CsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   Cs  u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1386,
    label = "Cs-C=SC=SCbCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   CS  u0 {1,S} {7,D}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   S2d u0 {2,D}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1387,
    label = "Cs-C=S(Cds-Cd)CbCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   C   u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1388,
    label = "Cs-C=S(Cds-Cds)CbCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   Cd  u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1389,
    label = "Cs-C=S(Cds-Cdd)CbCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   Cdd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1390,
    label = "Cs-C=S(Cds-Cdd-S2d)CbCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   Ct  u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1391,
    label = "Cs-C=S(Cds-Cdd-Cd)CbCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   Ct  u0 {1,S}
7   S2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1392,
    label = "Cs-C=SC=SCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   CS  u0 {1,S} {7,D}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   S2d u0 {2,D}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1393,
    label = "Cs-C=S(Cds-Cd)CbCb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   C   u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1394,
    label = "Cs-C=S(Cds-Cds)CbCb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   Cd  u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1395,
    label = "Cs-C=S(Cds-Cdd)CbCb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   Cdd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1396,
    label = "Cs-C=S(Cds-Cdd-S2d)CbCb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   Cb  u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1397,
    label = "Cs-C=S(Cds-Cdd-Cd)CbCb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   Cb  u0 {1,S}
7   S2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1398,
    label = "Cs-C=SC=S(Cds-Cd)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   CS  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   Ct  u0 {1,S}
6   C   u0 {4,D}
7   S2d u0 {2,D}
8   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1399,
    label = "Cs-C=SC=S(Cds-Cds)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   CS  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   Ct  u0 {1,S}
6   Cd  u0 {4,D}
7   S2d u0 {2,D}
8   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1400,
    label = "Cs-C=SC=S(Cds-Cdd)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   CS  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   Ct  u0 {1,S}
6   Cdd u0 {4,D}
7   S2d u0 {2,D}
8   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1401,
    label = "Cs-C=SC=S(Cds-Cdd-Cd)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CS  u0 {1,S} {7,D}
4   CS  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   Ct  u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1402,
    label = "Cs-C=SC=S(Cds-Cdd-S2d)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CS  u0 {1,S} {7,D}
4   CS  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   Ct  u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1403,
    label = "Cs-C=SC=S(Cds-Cd)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   CS  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   Cs  u0 {1,S}
6   C   u0 {4,D}
7   S2d u0 {2,D}
8   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1404,
    label = "Cs-C=SC=S(Cds-Cds)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   CS  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   Cs  u0 {1,S}
6   Cd  u0 {4,D}
7   S2d u0 {2,D}
8   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1405,
    label = "Cs-C=SC=S(Cds-Cdd)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   CS  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   Cs  u0 {1,S}
6   Cdd u0 {4,D}
7   S2d u0 {2,D}
8   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1406,
    label = "Cs-C=SC=S(Cds-Cdd-S2d)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CS  u0 {1,S} {7,D}
4   CS  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   Cs  u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1407,
    label = "Cs-C=SC=S(Cds-Cdd-Cd)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CS  u0 {1,S} {7,D}
4   CS  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   Cs  u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1408,
    label = "Cs-C=SC=S(Cds-Cd)(Cds-Cd)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {8,D}
3   CS  u0 {1,S} {9,D}
4   Cd  u0 {1,S} {6,D}
5   Cd  u0 {1,S} {7,D}
6   C   u0 {4,D}
7   C   u0 {5,D}
8   S2d u0 {2,D}
9   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1409,
    label = "Cs-C=SC=S(Cds-Cdd)(Cds-Cds)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {8,D}
3   CS  u0 {1,S} {9,D}
4   Cd  u0 {1,S} {6,D}
5   Cd  u0 {1,S} {7,D}
6   Cdd u0 {4,D}
7   Cd  u0 {5,D}
8   S2d u0 {2,D}
9   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1410,
    label = "Cs-C=SC=S(Cds-Cdd-S2d)(Cds-Cds)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    CS  u0 {1,S} {8,D}
4    CS  u0 {1,S} {9,D}
5    Cd  u0 {1,S} {7,D}
6    Cdd u0 {2,D} {10,D}
7    Cd  u0 {5,D}
8    S2d u0 {3,D}
9    S2d u0 {4,D}
10   S2d u0 {6,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1411,
    label = "Cs-C=SC=S(Cds-Cdd-Cd)(Cds-Cds)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    CS  u0 {1,S} {8,D}
4    CS  u0 {1,S} {9,D}
5    Cd  u0 {1,S} {7,D}
6    Cdd u0 {2,D} {10,D}
7    Cd  u0 {5,D}
8    S2d u0 {3,D}
9    S2d u0 {4,D}
10   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1412,
    label = "Cs-C=SC=S(Cds-Cdd)(Cds-Cdd)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {8,D}
3   CS  u0 {1,S} {9,D}
4   Cd  u0 {1,S} {6,D}
5   Cd  u0 {1,S} {7,D}
6   Cdd u0 {4,D}
7   Cdd u0 {5,D}
8   S2d u0 {2,D}
9   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1413,
    label = "Cs-C=SC=S(Cds-Cdd-S2d)(Cds-Cdd-S2d)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    CS  u0 {1,S} {8,D}
5    CS  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    S2d u0 {4,D}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
11   S2d u0 {7,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1414,
    label = "Cs-C=SC=S(Cds-Cdd-S2d)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    CS  u0 {1,S} {8,D}
5    CS  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    S2d u0 {4,D}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1415,
    label = "Cs-C=SC=S(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    CS  u0 {1,S} {8,D}
5    CS  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    S2d u0 {4,D}
9    S2d u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1416,
    label = "Cs-C=SC=S(Cds-Cds)(Cds-Cds)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {8,D}
3   CS  u0 {1,S} {9,D}
4   Cd  u0 {1,S} {6,D}
5   Cd  u0 {1,S} {7,D}
6   Cd  u0 {4,D}
7   Cd  u0 {5,D}
8   S2d u0 {2,D}
9   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1417,
    label = "Cs-C=SC=S(Cds-Cd)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   CS  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   Cb  u0 {1,S}
6   C   u0 {4,D}
7   S2d u0 {2,D}
8   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1418,
    label = "Cs-C=SC=S(Cds-Cdd)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   CS  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   Cb  u0 {1,S}
6   Cdd u0 {4,D}
7   S2d u0 {2,D}
8   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1419,
    label = "Cs-C=SC=S(Cds-Cdd-S2d)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CS  u0 {1,S} {7,D}
4   CS  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   Cb  u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1420,
    label = "Cs-C=SC=S(Cds-Cdd-Cd)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CS  u0 {1,S} {7,D}
4   CS  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   Cb  u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1421,
    label = "Cs-C=SC=S(Cds-Cds)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   CS  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   Cb  u0 {1,S}
6   Cd  u0 {4,D}
7   S2d u0 {2,D}
8   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1422,
    label = "Cs-C=SCbCtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Ct  u0 {1,S}
5   Cs  u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1423,
    label = "Cs-C=S(Cds-Cd)CbCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   Cs  u0 {1,S}
6   C   u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1424,
    label = "Cs-C=S(Cds-Cds)CbCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   Cs  u0 {1,S}
6   Cd  u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1425,
    label = "Cs-C=S(Cds-Cdd)CbCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   Cs  u0 {1,S}
6   Cdd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1426,
    label = "Cs-C=S(Cds-Cdd-S2d)CbCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   Cs  u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1427,
    label = "Cs-C=S(Cds-Cdd-Cd)CbCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   Cs  u0 {1,S}
7   S2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1428,
    label = "Cs-C=S(Cds-Cd)(Cds-Cd)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cb  u0 {1,S}
6   C   u0 {3,D}
7   C   u0 {4,D}
8   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1429,
    label = "Cs-C=S(Cds-Cdd)(Cds-Cdd)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cb  u0 {1,S}
6   Cdd u0 {3,D}
7   Cdd u0 {4,D}
8   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1430,
    label = "Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-Cd)Cb",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CS  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cb  u0 {1,S}
8    S2d u0 {4,D}
9    S2d u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1431,
    label = "Cs-C=S(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CS  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cb  u0 {1,S}
8    S2d u0 {4,D}
9    C   u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1432,
    label = "Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-S2d)Cb",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CS  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cb  u0 {1,S}
8    S2d u0 {4,D}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1433,
    label = "Cs-C=S(Cds-Cds)(Cds-Cds)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cb  u0 {1,S}
6   Cd  u0 {3,D}
7   Cd  u0 {4,D}
8   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1434,
    label = "Cs-C=S(Cds-Cdd)(Cds-Cds)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cb  u0 {1,S}
6   Cdd u0 {3,D}
7   Cd  u0 {4,D}
8   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1435,
    label = "Cs-C=S(Cds-Cdd-S2d)(Cds-Cds)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CS  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {9,D}
6   Cb  u0 {1,S}
7   Cd  u0 {4,D}
8   S2d u0 {3,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1436,
    label = "Cs-C=S(Cds-Cdd-Cd)(Cds-Cds)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CS  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {9,D}
6   Cb  u0 {1,S}
7   Cd  u0 {4,D}
8   S2d u0 {3,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1437,
    label = "Cs-C=SCbCbCb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1438,
    label = "Cs-C=SC=SCbCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   CS  u0 {1,S} {7,D}
4   Cb  u0 {1,S}
5   Cs  u0 {1,S}
6   S2d u0 {2,D}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1439,
    label = "Cs-CCCOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = 'Cs-CsCsCsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1440,
    label = "Cs-CsCsCsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.99,31.2,34.89,36.47,36.78,36.05,34.4],'J/(mol*K)','+|-',[3.81,3.81,3.81,3.81,3.81,3.81,3.81]),
        H298 = (-20.3,'kJ/mol','+|-',3.24),
        S298 = (-144.38,'J/(mol*K)','+|-',4.44),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 1441,
    label = "Cs-CdsCsCsOs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   Cs      u0 {1,S}
4   Cs      u0 {1,S}
5   O2s     u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CsCsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1442,
    label = "Cs-(Cds-O2d)CsCsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   O2s u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.15,35.17,38.11,38.72,37.49,35.88,33.45],'J/(mol*K)','+|-',[5.16,5.16,5.16,5.16,5.16,5.16,5.16]),
        H298 = (-10.9,'kJ/mol','+|-',4.39),
        S298 = (-148.7,'J/(mol*K)','+|-',6.02),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 1443,
    label = "Cs-(Cds-Cd)CsCsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   O2s u0 {1,S}
6   C   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.24,37.61,40.84,41.46,40.06,38.2,35.08],'J/(mol*K)','+|-',[3.81,3.81,3.81,3.81,3.81,3.81,3.81]),
        H298 = (-14.6,'kJ/mol','+|-',3.24),
        S298 = (-153.23,'J/(mol*K)','+|-',4.44),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 1444,
    label = "Cs-(Cds-Cds)CsCsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   O2s u0 {1,S}
6   Cd  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.63,6.79,7.95,8.4,8.8,8.44,8.44],'cal/(mol*K)','+|-',[0.2,0.2,0.2,0.2,0.2,0.2,0.2]),
        H298 = (-6.6,'kcal/mol','+|-',0.4),
        S298 = (-32.56,'cal/(mol*K)','+|-',0.2),
    ),
    shortDesc = """Cs-OCdCsCs BOZZELLI C/C3/O - (C/C3/H - C/Cb/C2/H), Hf-1 !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
"""

""",
)

entry(
    index = 1445,
    label = "Cs-(Cds-Cdd)CsCsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   O2s u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CsCsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1446,
    label = "Cs-(Cds-Cdd-O2d)CsCsOs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   O2s u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.39,9.66,10.03,10.07,9.64,9.26,8.74],'cal/(mol*K)','+|-',[0.2,0.2,0.2,0.2,0.2,0.2,0.2]),
        H298 = (-9.725,'kcal/mol','+|-',0.4),
        S298 = (-36.5,'cal/(mol*K)','+|-',0.2),
    ),
    shortDesc = """{C/CCO/O/C2} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
"""

""",
)

entry(
    index = 1447,
    label = "Cs-(Cds-Cdd-Cd)CsCsOs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   O2s u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)CsCsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1448,
    label = "Cs-OsCtCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S}
3   Ct  u0 {1,S}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CsCsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1449,
    label = "Cs-CbCsCsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.63,6.79,7.95,8.4,8.8,8.44,8.44],'cal/(mol*K)','+|-',[0.2,0.2,0.2,0.2,0.2,0.2,0.2]),
        H298 = (-6.6,'kcal/mol','+|-',0.4),
        S298 = (-32.56,'cal/(mol*K)','+|-',0.2),
    ),
    shortDesc = """Cs-OCbCsCs BOZZELLI C/C3/O - (C/C3/H - C/Cb/C2/H), Hf-1 !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
"""

""",
)

entry(
    index = 1450,
    label = "Cs-CdsCdsCsOs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
5   O2s     u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1451,
    label = "Cs-(Cds-O2d)(Cds-O2d)CsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   CO  u0 {1,S} {7,D}
4   Cs  u0 {1,S}
5   O2s u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
""",
    thermo = 'Cs-CsCsCsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1452,
    label = "Cs-(Cds-O2d)(Cds-Cd)CsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   O2s u0 {1,S}
6   C   u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([33.75,42.15,45.09,44.95,41.74,38.55,34.46],'J/(mol*K)','+|-',[4.3,4.3,4.3,4.3,4.3,4.3,4.3]),
        H298 = (-3.9,'kJ/mol','+|-',3.66),
        S298 = (-158.3,'J/(mol*K)','+|-',5.02),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 1453,
    label = "Cs-(Cds-O2d)(Cds-Cds)CsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   O2s u0 {1,S}
6   Cd  u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)CsCsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1454,
    label = "Cs-(Cds-O2d)(Cds-Cdd)CsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   O2s u0 {1,S}
6   Cdd u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cdd-Cd)CsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1455,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)CsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   O2s u0 {1,S}
7   O2d u0 {3,D}
8   O2d u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)CsCsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1456,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)CsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   O2s u0 {1,S}
7   O2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)CsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1457,
    label = "Cs-(Cds-Cd)(Cds-Cd)CsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cs  u0 {1,S}
5   O2s u0 {1,S}
6   C   u0 {2,D}
7   C   u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1458,
    label = "Cs-(Cds-Cds)(Cds-Cds)CsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cs  u0 {1,S}
5   O2s u0 {1,S}
6   Cd  u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.61,5.98,7.51,8.37,9,9.02,8.34],'cal/(mol*K)','+|-',[0.2,0.2,0.2,0.2,0.2,0.2,0.2]),
        H298 = (-8.01,'kcal/mol','+|-',0.4),
        S298 = (-34.34,'cal/(mol*K)','+|-',0.2),
    ),
    shortDesc = """Cs-OCdCdCs Hf jwb 697 S,Cp from C/Cd2/C2""",
    longDesc = 
"""

""",
)

entry(
    index = 1459,
    label = "Cs-(Cds-Cdd)(Cds-Cds)CsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cs  u0 {1,S}
5   O2s u0 {1,S}
6   Cdd u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cds)CsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1460,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cds)CsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   O2s u0 {1,S}
7   Cd  u0 {3,D}
8   O2d u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)CsCsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1461,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   O2s u0 {1,S}
7   Cd  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1462,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)CsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cs  u0 {1,S}
5   O2s u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1463,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cs  u0 {1,S}
7   O2s u0 {1,S}
8   O2d u0 {4,D}
9   O2d u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1464,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cs  u0 {1,S}
7   O2s u0 {1,S}
8   O2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)(Cds-Cds)CsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1465,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cs  u0 {1,S}
7   O2s u0 {1,S}
8   C   u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1466,
    label = "Cs-CtCdsCsOs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Ct      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
5   O2s     u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CtCsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1467,
    label = "Cs-(Cds-O2d)CtCsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   Cs  u0 {1,S}
5   O2s u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)CsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1468,
    label = "Cs-(Cds-Cd)CtCsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   Cs  u0 {1,S}
5   O2s u0 {1,S}
6   C   u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)CtCsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1469,
    label = "Cs-(Cds-Cds)CtCsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   Cs  u0 {1,S}
5   O2s u0 {1,S}
6   Cd  u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1470,
    label = "Cs-(Cds-Cdd)CtCsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   Cs  u0 {1,S}
5   O2s u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CtCsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1471,
    label = "Cs-(Cds-Cdd-O2d)CtCsOs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Cs  u0 {1,S}
6   O2s u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)(Cds-Cds)CsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1472,
    label = "Cs-(Cds-Cdd-Cd)CtCsOs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Cs  u0 {1,S}
6   O2s u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)CtCsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1473,
    label = "Cs-CbCdsCsOs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
5   O2s     u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CbCsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1474,
    label = "Cs-(Cds-O2d)CbCsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Cs  u0 {1,S}
5   O2s u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)CsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1475,
    label = "Cs-(Cds-Cd)CbCsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Cs  u0 {1,S}
5   O2s u0 {1,S}
6   C   u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)CbCsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1476,
    label = "Cs-(Cds-Cds)CbCsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Cs  u0 {1,S}
5   O2s u0 {1,S}
6   Cd  u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1477,
    label = "Cs-(Cds-Cdd)CbCsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Cs  u0 {1,S}
5   O2s u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CbCsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1478,
    label = "Cs-(Cds-Cdd-O2d)CbCsOs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cs  u0 {1,S}
6   O2s u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)(Cds-Cds)CsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1479,
    label = "Cs-(Cds-Cdd-Cd)CbCsOs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cs  u0 {1,S}
6   O2s u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)CbCsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1480,
    label = "Cs-CtCtCsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S}
3   Ct  u0 {1,S}
4   Cs  u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1481,
    label = "Cs-CbCtCsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   Ct  u0 {1,S}
4   Cs  u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CtCsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1482,
    label = "Cs-CbCbCsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   Cb  u0 {1,S}
4   Cs  u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1483,
    label = "Cs-CdsCdsCdsOs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   O2s     u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1484,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)O2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   CO  u0 {1,S} {7,D}
4   CO  u0 {1,S} {8,D}
5   O2s u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
8   O2d u0 {4,D}
""",
    thermo = 'Cs-CsCsCsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1485,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cd)O2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   O2s u0 {1,S}
6   C   u0 {4,D}
7   O2d u0 {2,D}
8   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1486,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)O2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   O2s u0 {1,S}
6   Cd  u0 {4,D}
7   O2d u0 {2,D}
8   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-O2d)CsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1487,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd)O2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   O2s u0 {1,S}
6   Cdd u0 {4,D}
7   O2d u0 {2,D}
8   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1488,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)O2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {7,D}
4   CO  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   O2s u0 {1,S}
7   O2d u0 {3,D}
8   O2d u0 {4,D}
9   O2d u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)CsCsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1489,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)O2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {7,D}
4   CO  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   O2s u0 {1,S}
7   O2d u0 {3,D}
8   O2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1490,
    label = "Cs-(Cds-O2d)(Cds-Cd)(Cds-Cd)O2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   O2s u0 {1,S}
6   C   u0 {3,D}
7   C   u0 {4,D}
8   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([36.85,46.04,49,48.85,45.61,42.23,37.25],'J/(mol*K)','+|-',[4.09,4.09,4.09,4.09,4.09,4.09,4.09]),
        H298 = (3,'kJ/mol','+|-',3.49),
        S298 = (-160.69,'J/(mol*K)','+|-',4.77),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 1491,
    label = "Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)O2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   O2s u0 {1,S}
6   Cd  u0 {3,D}
7   Cd  u0 {4,D}
8   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)CsCsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1492,
    label = "Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cds)O2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   O2s u0 {1,S}
6   Cdd u0 {3,D}
7   Cd  u0 {4,D}
8   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cds)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1493,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)O2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {9,D}
6   O2s u0 {1,S}
7   Cd  u0 {4,D}
8   O2d u0 {3,D}
9   O2d u0 {5,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cdd-O2d)CsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1494,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cds)O2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {9,D}
6   O2s u0 {1,S}
7   Cd  u0 {4,D}
8   O2d u0 {3,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1495,
    label = "Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cdd)O2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   O2s u0 {1,S}
6   Cdd u0 {3,D}
7   Cdd u0 {4,D}
8   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1496,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)O2s",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CO  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    O2s u0 {1,S}
8    O2d u0 {4,D}
9    O2d u0 {5,D}
10   O2d u0 {6,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1497,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)O2s",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CO  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    O2s u0 {1,S}
8    O2d u0 {4,D}
9    O2d u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1498,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)O2s",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CO  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    O2s u0 {1,S}
8    O2d u0 {4,D}
9    C   u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1499,
    label = "Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)O2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   O2s u0 {1,S}
6   C   u0 {2,D}
7   C   u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1500,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)O2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   O2s u0 {1,S}
6   Cd  u0 {2,D}
7   Cd  u0 {3,D}
8   Cd  u0 {4,D}
""",
    thermo = 'Cs-CsCsCsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1501,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)O2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   O2s u0 {1,S}
6   Cd  u0 {2,D}
7   Cd  u0 {3,D}
8   Cdd u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1502,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)O2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   O2s u0 {1,S}
7   Cd  u0 {3,D}
8   Cd  u0 {4,D}
9   O2d u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)CsCsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1503,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)O2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   O2s u0 {1,S}
7   Cd  u0 {3,D}
8   Cd  u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1504,
    label = "Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)O2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   O2s u0 {1,S}
6   Cd  u0 {2,D}
7   Cdd u0 {3,D}
8   Cdd u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1505,
    label = "Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)O2s",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    O2s u0 {1,S}
8    Cd  u0 {4,D}
9    O2d u0 {5,D}
10   O2d u0 {6,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1506,
    label = "Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-Cd)O2s",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    O2s u0 {1,S}
8    Cd  u0 {4,D}
9    O2d u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1507,
    label = "Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)O2s",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    O2s u0 {1,S}
8    Cd  u0 {4,D}
9    C   u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1508,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)O2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   O2s u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
8   Cdd u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1509,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)O2s",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    O2s u0 {1,S}
9    O2d u0 {5,D}
10   O2d u0 {6,D}
11   O2d u0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1510,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)O2s",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    O2s u0 {1,S}
9    O2d u0 {5,D}
10   O2d u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1511,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)O2s",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    O2s u0 {1,S}
9    O2d u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1512,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)O2s",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    O2s u0 {1,S}
9    C   u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1513,
    label = "Cs-CtCdsCdsOs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Ct      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   O2s     u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1514,
    label = "Cs-(Cds-O2d)(Cds-O2d)CtOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   CO  u0 {1,S} {7,D}
4   Ct  u0 {1,S}
5   O2s u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1515,
    label = "Cs-(Cds-O2d)(Cds-Cd)CtOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   O2s u0 {1,S}
6   C   u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)CtOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1516,
    label = "Cs-(Cds-O2d)(Cds-Cds)CtOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   O2s u0 {1,S}
6   Cd  u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1517,
    label = "Cs-(Cds-O2d)(Cds-Cdd)CtOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   O2s u0 {1,S}
6   Cdd u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cdd-Cd)CtOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1518,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)CtOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   O2s u0 {1,S}
7   O2d u0 {3,D}
8   O2d u0 {4,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1519,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)CtOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   O2s u0 {1,S}
7   O2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)CtOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1520,
    label = "Cs-(Cds-Cd)(Cds-Cd)CtOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Ct  u0 {1,S}
5   O2s u0 {1,S}
6   C   u0 {2,D}
7   C   u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1521,
    label = "Cs-(Cds-Cds)(Cds-Cds)CtOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Ct  u0 {1,S}
5   O2s u0 {1,S}
6   Cd  u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1522,
    label = "Cs-(Cds-Cdd)(Cds-Cds)CtOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Ct  u0 {1,S}
5   O2s u0 {1,S}
6   Cdd u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cds)CtOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1523,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cds)CtOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   O2s u0 {1,S}
7   Cd  u0 {3,D}
8   O2d u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1524,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CtOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   O2s u0 {1,S}
7   Cd  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1525,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)CtOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Ct  u0 {1,S}
5   O2s u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1526,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CtOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Ct  u0 {1,S}
7   O2s u0 {1,S}
8   O2d u0 {4,D}
9   O2d u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1527,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CtOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Ct  u0 {1,S}
7   O2s u0 {1,S}
8   O2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)(Cds-Cds)CtOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1528,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Ct  u0 {1,S}
7   O2s u0 {1,S}
8   C   u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1529,
    label = "Cs-CbCdsCdsOs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   O2s     u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CbOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1530,
    label = "Cs-(Cds-O2d)(Cds-O2d)CbOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   CO  u0 {1,S} {7,D}
4   Cb  u0 {1,S}
5   O2s u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1531,
    label = "Cs-(Cds-O2d)(Cds-Cd)CbOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   O2s u0 {1,S}
6   C   u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)CbOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1532,
    label = "Cs-(Cds-O2d)(Cds-Cds)CbOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   O2s u0 {1,S}
6   Cd  u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1533,
    label = "Cs-(Cds-O2d)(Cds-Cdd)CbOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   O2s u0 {1,S}
6   Cdd u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cdd-Cd)CbOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1534,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)CbOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   O2s u0 {1,S}
7   O2d u0 {3,D}
8   O2d u0 {4,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1535,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)CbOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   O2s u0 {1,S}
7   O2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)CbOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1536,
    label = "Cs-(Cds-Cd)(Cds-Cd)CbOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cb  u0 {1,S}
5   O2s u0 {1,S}
6   C   u0 {2,D}
7   C   u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CbOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1537,
    label = "Cs-(Cds-Cds)(Cds-Cds)CbOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cb  u0 {1,S}
5   O2s u0 {1,S}
6   Cd  u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1538,
    label = "Cs-(Cds-Cdd)(Cds-Cds)CbOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cb  u0 {1,S}
5   O2s u0 {1,S}
6   Cdd u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cds)CbOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1539,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cds)CbOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   O2s u0 {1,S}
7   Cd  u0 {3,D}
8   O2d u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1540,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CbOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   O2s u0 {1,S}
7   Cd  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CbOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1541,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)CbOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cb  u0 {1,S}
5   O2s u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1542,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CbOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   O2s u0 {1,S}
8   O2d u0 {4,D}
9   O2d u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1543,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CbOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   O2s u0 {1,S}
8   O2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)(Cds-Cds)CbOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1544,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   O2s u0 {1,S}
8   C   u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CbOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1545,
    label = "Cs-CtCtCdsOs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Ct      u0 {1,S}
3   Ct      u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   O2s     u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CtCtOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1546,
    label = "Cs-(Cds-O2d)CtCtOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   Ct  u0 {1,S}
5   O2s u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1547,
    label = "Cs-(Cds-Cd)CtCtOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   Ct  u0 {1,S}
5   O2s u0 {1,S}
6   C   u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)CtCtOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1548,
    label = "Cs-(Cds-Cds)CtCtOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   Ct  u0 {1,S}
5   O2s u0 {1,S}
6   Cd  u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1549,
    label = "Cs-(Cds-Cdd)CtCtOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   Ct  u0 {1,S}
5   O2s u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CtCtOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1550,
    label = "Cs-(Cds-Cdd-O2d)CtCtOs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   O2s u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1551,
    label = "Cs-(Cds-Cdd-Cd)CtCtOs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   O2s u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)CtCtOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1552,
    label = "Cs-CbCtCdsOs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   Ct      u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   O2s     u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CbCtOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1553,
    label = "Cs-(Cds-O2d)CbCtOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Ct  u0 {1,S}
5   O2s u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)CtOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1554,
    label = "Cs-(Cds-Cd)CbCtOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Ct  u0 {1,S}
5   O2s u0 {1,S}
6   C   u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)CbCtOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1555,
    label = "Cs-(Cds-Cds)CbCtOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Ct  u0 {1,S}
5   O2s u0 {1,S}
6   Cd  u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1556,
    label = "Cs-(Cds-Cdd)CbCtOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Ct  u0 {1,S}
5   O2s u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CbCtOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1557,
    label = "Cs-(Cds-Cdd-O2d)CbCtOs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   O2s u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)(Cds-Cds)CtOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1558,
    label = "Cs-(Cds-Cdd-Cd)CbCtOs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   O2s u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)CbCtOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1559,
    label = "Cs-CbCbCdsOs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   Cb      u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   O2s     u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CbCbOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1560,
    label = "Cs-(Cds-O2d)CbCbOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
5   O2s u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1561,
    label = "Cs-(Cds-Cd)CbCbOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
5   O2s u0 {1,S}
6   C   u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)CbCbOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1562,
    label = "Cs-(Cds-Cds)CbCbOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
5   O2s u0 {1,S}
6   Cd  u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1563,
    label = "Cs-(Cds-Cdd)CbCbOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
5   O2s u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CbCbOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1564,
    label = "Cs-(Cds-Cdd-O2d)CbCbOs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   O2s u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1565,
    label = "Cs-(Cds-Cdd-Cd)CbCbOs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   O2s u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)CbCbOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1566,
    label = "Cs-CtCtCtOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S}
3   Ct  u0 {1,S}
4   Ct  u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1567,
    label = "Cs-CbCtCtOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   Ct  u0 {1,S}
4   Ct  u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CtCtOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1568,
    label = "Cs-CbCbCtOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   Cb  u0 {1,S}
4   Ct  u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1569,
    label = "Cs-CbCbCbOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)O2s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1570,
    label = "Cs-CCOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = 'Cs-CsCsOsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1571,
    label = "Cs-CsCsOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.88,43.75,51.85,54,50.77,45.94,38.31],'J/(mol*K)','+|-',[5.77,5.77,5.77,5.77,5.77,5.77,5.77]),
        H298 = (-69.2,'kJ/mol','+|-',4.92),
        S298 = (-163.77,'J/(mol*K)','+|-',6.74),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 1572,
    label = "Cs-CdsCsOsOs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   Cs      u0 {1,S}
4   O2s     u0 {1,S}
5   O2s     u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CsOsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1573,
    label = "Cs-(Cds-O2d)CsOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = 'Cs-CsCsOsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1574,
    label = "Cs-(Cds-Cd)CsOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   C   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.95,42.92,51.33,54.81,53.92,49.73,41.11],'J/(mol*K)','+|-',[5.77,5.77,5.77,5.77,5.77,5.77,5.77]),
        H298 = (-62.8,'kJ/mol','+|-',4.92),
        S298 = (-170.44,'J/(mol*K)','+|-',6.74),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 1575,
    label = "Cs-(Cds-Cds)CsOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   Cd  u0 {2,D}
""",
    thermo = 'Cs-CsCsOsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1576,
    label = "Cs-(Cds-Cdd)CsOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CsOsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1577,
    label = "Cs-(Cds-Cdd-O2d)CsOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cs  u0 {1,S}
5   O2s u0 {1,S}
6   O2s u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)CsOsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1578,
    label = "Cs-(Cds-Cdd-Cd)CsOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cs  u0 {1,S}
5   O2s u0 {1,S}
6   O2s u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)CsOsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1579,
    label = "Cs-CdsCdsOsOs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   O2s     u0 {1,S}
5   O2s     u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)OsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1580,
    label = "Cs-(Cds-O2d)(Cds-O2d)OsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   CO  u0 {1,S} {7,D}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
""",
    thermo = 'Cs-CsCsOsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1581,
    label = "Cs-(Cds-O2d)(Cds-Cd)OsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   C   u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)OsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1582,
    label = "Cs-(Cds-O2d)(Cds-Cds)OsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   Cd  u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)CsOsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1583,
    label = "Cs-(Cds-O2d)(Cds-Cdd)OsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   Cdd u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cdd-Cd)OsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1584,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)OsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   O2s u0 {1,S}
6   O2s u0 {1,S}
7   O2d u0 {3,D}
8   O2d u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)CsOsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1585,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)OsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   O2s u0 {1,S}
6   O2s u0 {1,S}
7   O2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)OsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1586,
    label = "Cs-(Cds-Cd)(Cds-Cd)OsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   C   u0 {2,D}
7   C   u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([30.08,45.85,54.7,58.39,57.78,53.65,44.31],'J/(mol*K)','+|-',[5.77,5.77,5.77,5.77,5.77,5.77,5.77]),
        H298 = (-55.7,'kJ/mol','+|-',4.92),
        S298 = (-179.76,'J/(mol*K)','+|-',6.74),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 1587,
    label = "Cs-(Cds-Cds)(Cds-Cds)OsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   Cd  u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = 'Cs-CsCsOsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1588,
    label = "Cs-(Cds-Cdd)(Cds-Cds)OsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   Cdd u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cds)OsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1589,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cds)OsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   O2s u0 {1,S}
6   O2s u0 {1,S}
7   Cd  u0 {3,D}
8   O2d u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)CsOsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1590,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)OsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   O2s u0 {1,S}
6   O2s u0 {1,S}
7   Cd  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)OsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1591,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)OsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)OsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1592,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)OsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   O2s u0 {1,S}
7   O2s u0 {1,S}
8   O2d u0 {4,D}
9   O2d u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)OsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1593,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)OsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   O2s u0 {1,S}
7   O2s u0 {1,S}
8   O2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)(Cds-Cds)OsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1594,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)OsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   O2s u0 {1,S}
7   O2s u0 {1,S}
8   C   u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)OsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1595,
    label = "Cs-CtCsOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S}
3   Cs  u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CsOsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1596,
    label = "Cs-CtCdsOsOs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Ct      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   O2s     u0 {1,S}
5   O2s     u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CtOsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1597,
    label = "Cs-(Cds-O2d)CtOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)OsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1598,
    label = "Cs-(Cds-Cd)CtOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   C   u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)CtOsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1599,
    label = "Cs-(Cds-Cds)CtOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   Cd  u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)OsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1600,
    label = "Cs-(Cds-Cdd)CtOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CtOsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1601,
    label = "Cs-(Cds-Cdd-O2d)CtOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   O2s u0 {1,S}
6   O2s u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)(Cds-Cds)OsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1602,
    label = "Cs-(Cds-Cdd-Cd)CtOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   O2s u0 {1,S}
6   O2s u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)CtOsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1603,
    label = "Cs-CtCtOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S}
3   Ct  u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)OsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1604,
    label = "Cs-CbCsOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   Cs  u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CsOsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1605,
    label = "Cs-CbCdsOsOs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   O2s     u0 {1,S}
5   O2s     u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CbOsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1606,
    label = "Cs-(Cds-O2d)CbOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)OsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1607,
    label = "Cs-(Cds-Cd)CbOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   C   u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)CbOsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1608,
    label = "Cs-(Cds-Cds)CbOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   Cd  u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)OsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1609,
    label = "Cs-(Cds-Cdd)CbOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CbOsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1610,
    label = "Cs-(Cds-Cdd-O2d)CbOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   O2s u0 {1,S}
6   O2s u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)(Cds-Cds)OsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1611,
    label = "Cs-(Cds-Cdd-Cd)CbOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   O2s u0 {1,S}
6   O2s u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)CbOsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1612,
    label = "Cs-CbCtOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   Ct  u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CtOsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1613,
    label = "Cs-CbCbOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   Cb  u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)OsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1614,
    label = "Cs-COsOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   C   u0 {1,S}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = 'Cs-CsOsOsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1615,
    label = "Cs-CsOsOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 {1,S}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.33,6.19,7.25,7.7,8.2,8.24,8.24],'cal/(mol*K)','+|-',[0.2,0.2,0.2,0.2,0.2,0.2,0.2]),
        H298 = (-19,'kcal/mol','+|-',0.4),
        S298 = (-33.56,'cal/(mol*K)','+|-',0.2),
    ),
    shortDesc = """Cs-OOOCs BOZZELLI est !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
"""

""",
)

entry(
    index = 1616,
    label = "Cs-CdsOsOsOs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   O2s     u0 {1,S}
4   O2s     u0 {1,S}
5   O2s     u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)OsOsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1617,
    label = "Cs-(Cds-O2d)OsOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = 'Cs-CsOsOsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1618,
    label = "Cs-(Cds-Cd)OsOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   C   u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)OsOsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1619,
    label = "Cs-(Cds-Cds)OsOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   Cd  u0 {2,D}
""",
    thermo = 'Cs-CsOsOsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1620,
    label = "Cs-(Cds-Cdd)OsOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)OsOsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1621,
    label = "Cs-(Cds-Cdd-O2d)OsOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   O2s u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)OsOsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1622,
    label = "Cs-(Cds-Cdd-Cd)OsOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   O2s u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)OsOsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1623,
    label = "Cs-CtOsOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)OsOsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1624,
    label = "Cs-CbOsOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)OsOsOs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1625,
    label = "Cs-OsOsOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.33,6.13,7.25,7.7,8.2,8.24,8.24],'cal/(mol*K)','+|-',[0.2,0.2,0.2,0.2,0.2,0.2,0.2]),
        H298 = (-23,'kcal/mol','+|-',0.4),
        S298 = (-35.56,'cal/(mol*K)','+|-',0.2),
    ),
    shortDesc = """Cs-OOOO BOZZELLI est !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
"""

""",
)

entry(
    index = 1626,
    label = "Cs-COsOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   C   u0 {1,S}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = 'Cs-CsOsOsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1627,
    label = "Cs-CsOsOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 {1,S}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.25,7.1,8.81,9.55,10.31,11.05,11.05],'cal/(mol*K)','+|-',[0.12,0.12,0.12,0.12,0.12,0.12,0.12]),
        H298 = (-16,'kcal/mol','+|-',0.24),
        S298 = (-12.07,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = """Cs-OOCsH BENSON Hf, BOZZELLI C/C3/H - C/C2/O/H !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
"""

""",
)

entry(
    index = 1628,
    label = "Cs-CdsOsOsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   O2s     u0 {1,S}
4   O2s     u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)OsOsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1629,
    label = "Cs-(Cds-O2d)OsOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = 'Cs-CsOsOsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1630,
    label = "Cs-(Cds-Cd)OsOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
6   C   u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)OsOsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1631,
    label = "Cs-(Cds-Cds)OsOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
6   Cd  u0 {2,D}
""",
    thermo = 'Cs-CsOsOsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1632,
    label = "Cs-(Cds-Cdd)OsOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)OsOsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1633,
    label = "Cs-(Cds-Cdd-O2d)OsOsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   H   u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)OsOsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1634,
    label = "Cs-(Cds-Cdd-Cd)OsOsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   H   u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)OsOsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1635,
    label = "Cs-CtOsOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)OsOsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1636,
    label = "Cs-CbOsOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)OsOsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1637,
    label = "Cs-COsSH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   C   u0 {1,S}
3   O2s u0 {1,S}
4   S   u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = 'Cs-CsOsSH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1638,
    label = "Cs-CsOsSH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 {1,S}
3   O2s u0 {1,S}
4   S   u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = 'Cs-CsOsS2H',
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc = 
"""
"
""",
)

entry(
    index = 1639,
    label = "Cs-CsOsS2H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 {1,S}
3   O2s u0 {1,S}
4   S2s u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.76,10.63,11.62,12.1,13.03,14.22,12.83],'cal/(mol*K)'),
        H298 = (4.17,'kcal/mol'),
        S298 = (-13.3,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 1640,
    label = "Cs-CsOsS4H",
    group = 
"""
1 * Cs                u0 {2,S} {3,S} {4,S} {5,S}
2   Cs                u0 {1,S}
3   O2s               u0 {1,S}
4   [S4s,S4d,S4b,S4t] u0 {1,S}
5   H                 u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.67,8.88,10.44,11.92,15.43,17.07,15.18],'cal/(mol*K)'),
        H298 = (5.25,'kcal/mol'),
        S298 = (-20.4,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 1641,
    label = "Cs-CdsOsSsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S}
3   O2s u0 {1,S}
4   S2s u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.88,11.94,12.92,13.33,14.67,15.02,13.48],'cal/(mol*K)'),
        H298 = (5.37,'kcal/mol'),
        S298 = (-11.83,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 1642,
    label = "Cs-CtOsSsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S}
3   O2s u0 {1,S}
4   S2s u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1643,
    label = "Cs-CbOsSsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   O2s u0 {1,S}
4   S2s u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.94,11.75,12.59,12.98,14.4,14.78,12.9],'cal/(mol*K)'),
        H298 = (4.61,'kcal/mol'),
        S298 = (-13.38,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 1644,
    label = "Cs-CCOsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
4   O2s u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1645,
    label = "Cs-CsCsOsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   O2s u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.94,10.89,11.45,11.37,11.9,11.9,9.51],'cal/(mol*K)'),
        H298 = (6.54,'kcal/mol'),
        S298 = (-38.36,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 1646,
    label = "Cs-COsOsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   C   u0 {1,S}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = 'Cs-CsOsOsSs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1647,
    label = "Cs-CsOsOsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 {1,S}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.58,8.97,9.76,10.23,11.93,12.31,10.02],'cal/(mol*K)'),
        H298 = (-5.27,'kcal/mol'),
        S298 = (-33.54,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 1648,
    label = "Cs-CCOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = 'Cs-CsCsOsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1649,
    label = "Cs-CsCsOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.99,29.03,34.22,37.78,41.96,44.27,47.11],'J/(mol*K)','+|-',[3.32,3.32,3.32,3.32,3.32,3.32,3.32]),
        H298 = (-25.1,'kJ/mol','+|-',2.83),
        S298 = (-52.05,'J/(mol*K)','+|-',3.88),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 1650,
    label = "Cs-CdsCsOsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   Cs      u0 {1,S}
4   O2s     u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CsOsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1651,
    label = "Cs-(Cds-O2d)CsOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.47,6.82,8.45,9.17,10.24,10.8,11.02],'cal/(mol*K)','+|-',[0.12,0.12,0.12,0.12,0.12,0.12,0.12]),
        H298 = (-6,'kcal/mol','+|-',0.24),
        S298 = (-11.1,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = """Cs-OCOCsH BOZZELLI""",
    longDesc = 
"""

""",
)

entry(
    index = 1652,
    label = "Cs-(Cds-Cd)CsOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
6   C   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.84,38.86,43.83,46.37,48.34,49.06,49.94],'J/(mol*K)','+|-',[3.74,3.74,3.74,3.74,3.74,3.74,3.74]),
        H298 = (-24,'kJ/mol','+|-',3.19),
        S298 = (-61.06,'J/(mol*K)','+|-',4.36),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 1653,
    label = "Cs-(Cds-Cds)CsOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
6   Cd  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.47,6.82,8.45,9.17,10.24,10.8,11.02],'cal/(mol*K)','+|-',[0.12,0.12,0.12,0.12,0.12,0.12,0.12]),
        H298 = (-6,'kcal/mol','+|-',0.24),
        S298 = (-11.1,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = """Cs-OCdCsH BOZZELLI""",
    longDesc = 
"""

""",
)

entry(
    index = 1654,
    label = "Cs-(Cds-Cdd)CsOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CsOsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1655,
    label = "Cs-(Cds-Cdd-O2d)CsOsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cs  u0 {1,S}
5   O2s u0 {1,S}
6   H   u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.2,8.49,9.33,9.92,10.5,10.92,11.71],'cal/(mol*K)','+|-',[0.12,0.12,0.12,0.12,0.12,0.12,0.12]),
        H298 = (-8.37,'kcal/mol','+|-',0.24),
        S298 = (-13.04,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = """{C/CCO/O/C/H} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
"""

""",
)

entry(
    index = 1656,
    label = "Cs-(Cds-Cdd-Cd)CsOsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cs  u0 {1,S}
5   O2s u0 {1,S}
6   H   u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)CsOsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1657,
    label = "Cs-CdsCdsOsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   O2s     u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)OsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1658,
    label = "Cs-(Cds-O2d)(Cds-O2d)OsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   CO  u0 {1,S} {7,D}
4   O2s u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
""",
    thermo = 'Cs-CsCsOsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1659,
    label = "Cs-(Cds-O2d)(Cds-Cd)OsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   O2s u0 {1,S}
5   H   u0 {1,S}
6   C   u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)OsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1660,
    label = "Cs-(Cds-O2d)(Cds-Cds)OsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   O2s u0 {1,S}
5   H   u0 {1,S}
6   Cd  u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)CsOsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1661,
    label = "Cs-(Cds-O2d)(Cds-Cdd)OsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   O2s u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cdd-Cd)OsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1662,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)OsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   O2s u0 {1,S}
6   H   u0 {1,S}
7   O2d u0 {3,D}
8   O2d u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)CsOsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1663,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)OsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   O2s u0 {1,S}
6   H   u0 {1,S}
7   O2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)OsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1664,
    label = "Cs-(Cds-Cd)(Cds-Cd)OsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   O2s u0 {1,S}
5   H   u0 {1,S}
6   C   u0 {2,D}
7   C   u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.82,38.47,43.27,45.7,47.5,48.09,48.78],'J/(mol*K)','+|-',[3.64,3.64,3.64,3.64,3.64,3.64,3.64]),
        H298 = (-17.4,'kJ/mol','+|-',3.1),
        S298 = (-64.14,'J/(mol*K)','+|-',4.24),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 1665,
    label = "Cs-(Cds-Cds)(Cds-Cds)OsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   O2s u0 {1,S}
5   H   u0 {1,S}
6   Cd  u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.21,6.6,8.26,9.05,10.23,10.86,11.04],'cal/(mol*K)','+|-',[0.12,0.12,0.12,0.12,0.12,0.12,0.12]),
        H298 = (-6.67,'kcal/mol','+|-',0.24),
        S298 = (-10.42,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = """Cs-OCdCdH BOZZELLI""",
    longDesc = 
"""

""",
)

entry(
    index = 1666,
    label = "Cs-(Cds-Cdd)(Cds-Cds)OsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   O2s u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cds)OsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1667,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cds)OsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   O2s u0 {1,S}
6   H   u0 {1,S}
7   Cd  u0 {3,D}
8   O2d u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)CsOsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1668,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)OsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   O2s u0 {1,S}
6   H   u0 {1,S}
7   Cd  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)OsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1669,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)OsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   O2s u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)OsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1670,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)OsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   O2s u0 {1,S}
7   H   u0 {1,S}
8   O2d u0 {4,D}
9   O2d u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)OsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1671,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)OsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   O2s u0 {1,S}
7   H   u0 {1,S}
8   O2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)(Cds-Cds)OsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1672,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)OsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   O2s u0 {1,S}
7   H   u0 {1,S}
8   C   u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)OsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1673,
    label = "Cs-CtCsOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S}
3   Cs  u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CsOsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1674,
    label = "Cs-CtCdsOsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Ct      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   O2s     u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CtOsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1675,
    label = "Cs-(Cds-O2d)CtOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)OsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1676,
    label = "Cs-(Cds-Cd)CtOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
6   C   u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)CtOsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1677,
    label = "Cs-(Cds-Cds)CtOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
6   Cd  u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)OsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1678,
    label = "Cs-(Cds-Cdd)CtOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CtOsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1679,
    label = "Cs-(Cds-Cdd-O2d)CtOsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   O2s u0 {1,S}
6   H   u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)(Cds-Cds)OsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1680,
    label = "Cs-(Cds-Cdd-Cd)CtOsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   O2s u0 {1,S}
6   H   u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)CtOsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1681,
    label = "Cs-CtCtOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S}
3   Ct  u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)OsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1682,
    label = "Cs-CbCsOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   Cs  u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.47,6.82,8.45,9.17,10.24,10.8,11.02],'cal/(mol*K)','+|-',[0.12,0.12,0.12,0.12,0.12,0.12,0.12]),
        H298 = (-6,'kcal/mol','+|-',0.24),
        S298 = (-11.1,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = """Cs-OCbCsH BOZZELLI =3D C/Cd/C/H/O Jul 91""",
    longDesc = 
"""

""",
)

entry(
    index = 1683,
    label = "Cs-CbCdsOsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   O2s     u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CbOsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1684,
    label = "Cs-(Cds-O2d)CbOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = 'Cs-(Cds-O2d)(Cds-Cds)OsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1685,
    label = "Cs-(Cds-Cd)CbOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
6   C   u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)CbOsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1686,
    label = "Cs-(Cds-Cds)CbOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
6   Cd  u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)OsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1687,
    label = "Cs-(Cds-Cdd)CbOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CbOsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1688,
    label = "Cs-(Cds-Cdd-O2d)CbOsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   O2s u0 {1,S}
6   H   u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-O2d)(Cds-Cds)OsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1689,
    label = "Cs-(Cds-Cdd-Cd)CbOsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   O2s u0 {1,S}
6   H   u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)CbOsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1690,
    label = "Cs-CbCtOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   Ct  u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CtOsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1691,
    label = "Cs-CbCbOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   Cb  u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)OsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1692,
    label = "Cs-COsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   C   u0 {1,S}
3   O2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = 'Cs-CsOsHH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1693,
    label = "Cs-CsOsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 {1,S}
3   O2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.01,31.9,37.45,41.88,48.53,53.31,60.53],'J/(mol*K)','+|-',[1.43,1.43,1.43,1.43,1.43,1.43,1.43]),
        H298 = (-34.3,'kJ/mol','+|-',1.22),
        S298 = (37.65,'J/(mol*K)','+|-',1.67),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 1694,
    label = "Cs-CdsOsHH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   O2s     u0 {1,S}
4   H       u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)OsHH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1695,
    label = "Cs-(Cds-O2d)OsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   O2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.75,34.37,40.77,45.37,51.2,54.96,60.79],'J/(mol*K)','+|-',[4.34,4.34,4.34,4.34,4.34,4.34,4.34]),
        H298 = (-19.8,'kJ/mol','+|-',3.7),
        S298 = (31.54,'J/(mol*K)','+|-',5.06),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 1696,
    label = "Cs-(Cds-Cd)OsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   O2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   C   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.42,35.65,40.62,44.31,49.79,53.92,60.6],'J/(mol*K)','+|-',[3.38,3.38,3.38,3.38,3.38,3.38,3.38]),
        H298 = (-26.6,'kJ/mol','+|-',2.88),
        S298 = (34.59,'J/(mol*K)','+|-',3.95),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 1697,
    label = "Cs-(Cds-Cds)OsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   O2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   Cd  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.12,6.86,8.32,9.49,11.22,12.48,14.4],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-6.76,'kcal/mol','+|-',0.2),
        S298 = (9.8,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = """Cs-OCdHH BOZZELLI Hf PEDLEY c*ccoh C/C/Cd/H2""",
    longDesc = 
"""

""",
)

entry(
    index = 1698,
    label = "Cs-(Cds-Cdd)OsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   O2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)OsHH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1699,
    label = "Cs-(Cds-Cdd-O2d)OsHH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   O2s u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.15,8.67,9.75,10.65,11.93,12.97,14.86],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-8.68,'kcal/mol','+|-',0.2),
        S298 = (8.43,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = """{C/CCO/O/H2} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
"""

""",
)

entry(
    index = 1700,
    label = "Cs-(Cds-Cdd-Cd)OsHH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   O2s u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)OsHH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1701,
    label = "Cs-CtOsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S}
3   O2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.12,6.86,8.32,9.49,11.22,12.48,14.4],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-6.76,'kcal/mol','+|-',0.2),
        S298 = (9.8,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = """Cs-OCtHH BOZZELLI assigned C/Cd/H2/O""",
    longDesc = 
"""

""",
)

entry(
    index = 1702,
    label = "Cs-CbOsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   O2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)OsHH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1703,
    label = "Cs-CCCS",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   S  u0 {1,S}
""",
    thermo = 'Cs-CsCsCsS',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1704,
    label = "Cs-CsCsCsS",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   S  u0 {1,S}
""",
    thermo = 'Cs-CsCsCsS2',
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc = 
"""
"
""",
)

entry(
    index = 1705,
    label = "Cs-CsCsCsS2",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.97,6.93,7.58,8.09,10.09,10.99,9.6],'cal/(mol*K)'),
        H298 = (10.75,'kcal/mol'),
        S298 = (-31.6,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 1706,
    label = "Cs-CsCsCsS4",
    group = 
"""
1 * Cs                u0 {2,S} {3,S} {4,S} {5,S}
2   Cs                u0 {1,S}
3   Cs                u0 {1,S}
4   Cs                u0 {1,S}
5   [S4s,S4d,S4b,S4t] u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.57,5.49,5.72,6.11,8.54,9.77,8.79],'cal/(mol*K)'),
        H298 = (14.82,'kcal/mol'),
        S298 = (-29.47,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 1707,
    label = "Cs-CdsCsCsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1708,
    label = "Cs-(Cds-Cd)CsCsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   S2s u0 {1,S}
6   C   u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1709,
    label = "Cs-(Cds-Cds)CsCsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   S2s u0 {1,S}
6   Cd  u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1710,
    label = "Cs-(Cds-Cdd)CsCsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   S2s u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1711,
    label = "Cs-(Cds-Cdd-S2d)CsCsSs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   S2s u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1712,
    label = "Cs-(Cds-Cdd-Cd)CsCsSs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   S2s u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1713,
    label = "Cs-SsCtCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   S2s u0 {1,S}
3   Ct  u0 {1,S}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1714,
    label = "Cs-CbCsCsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1715,
    label = "Cs-CdsCdsCsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S}
3   Cd  u0 {1,S}
4   Cs  u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1716,
    label = "Cs-(Cds-Cd)(Cds-Cd)CsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cs  u0 {1,S}
5   S2s u0 {1,S}
6   C   u0 {2,D}
7   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1717,
    label = "Cs-(Cds-Cds)(Cds-Cds)CsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cs  u0 {1,S}
5   S2s u0 {1,S}
6   Cd  u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1718,
    label = "Cs-(Cds-Cdd)(Cds-Cds)CsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cs  u0 {1,S}
5   S2s u0 {1,S}
6   Cdd u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1719,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cds)CsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   S2s u0 {1,S}
7   Cd  u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1720,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   S2s u0 {1,S}
7   Cd  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1721,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)CsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cs  u0 {1,S}
5   S2s u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1722,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cs  u0 {1,S}
7   S2s u0 {1,S}
8   S2d u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1723,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cs  u0 {1,S}
7   S2s u0 {1,S}
8   S2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1724,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cs  u0 {1,S}
7   S2s u0 {1,S}
8   C   u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1725,
    label = "Cs-CtCdsCsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S}
3   Cd  u0 {1,S}
4   Cs  u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1726,
    label = "Cs-(Cds-Cd)CtCsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   Cs  u0 {1,S}
5   S2s u0 {1,S}
6   C   u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1727,
    label = "Cs-(Cds-Cds)CtCsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   Cs  u0 {1,S}
5   S2s u0 {1,S}
6   Cd  u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1728,
    label = "Cs-(Cds-Cdd)CtCsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   Cs  u0 {1,S}
5   S2s u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1729,
    label = "Cs-(Cds-Cdd-S2d)CtCsSs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Cs  u0 {1,S}
6   S2s u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1730,
    label = "Cs-(Cds-Cdd-Cd)CtCsSs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Cs  u0 {1,S}
6   S2s u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1731,
    label = "Cs-CbCdsCsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   Cd  u0 {1,S}
4   Cs  u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1732,
    label = "Cs-(Cds-Cd)CbCsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Cs  u0 {1,S}
5   S2s u0 {1,S}
6   C   u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1733,
    label = "Cs-(Cds-Cds)CbCsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Cs  u0 {1,S}
5   S2s u0 {1,S}
6   Cd  u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1734,
    label = "Cs-(Cds-Cdd)CbCsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Cs  u0 {1,S}
5   S2s u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1735,
    label = "Cs-(Cds-Cdd-S2d)CbCsSs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cs  u0 {1,S}
6   S2s u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1736,
    label = "Cs-(Cds-Cdd-Cd)CbCsSs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cs  u0 {1,S}
6   S2s u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1737,
    label = "Cs-CtCtCsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S}
3   Ct  u0 {1,S}
4   Cs  u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1738,
    label = "Cs-CbCtCsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   Ct  u0 {1,S}
4   Cs  u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1739,
    label = "Cs-CbCbCsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   Cb  u0 {1,S}
4   Cs  u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1740,
    label = "Cs-CdsCdsCdsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S}
3   Cd  u0 {1,S}
4   Cd  u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1741,
    label = "Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)S2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   S2s u0 {1,S}
6   C   u0 {2,D}
7   C   u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1742,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)S2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   S2s u0 {1,S}
6   Cd  u0 {2,D}
7   Cd  u0 {3,D}
8   Cd  u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1743,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)S2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   S2s u0 {1,S}
6   Cd  u0 {2,D}
7   Cd  u0 {3,D}
8   Cdd u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1744,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-S2d)S2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   S2s u0 {1,S}
7   Cd  u0 {3,D}
8   Cd  u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1745,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)S2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   S2s u0 {1,S}
7   Cd  u0 {3,D}
8   Cd  u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1746,
    label = "Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)S2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   S2s u0 {1,S}
6   Cd  u0 {2,D}
7   Cdd u0 {3,D}
8   Cdd u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1747,
    label = "Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-S2d)S2s",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    S2s u0 {1,S}
8    Cd  u0 {4,D}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1748,
    label = "Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-Cd)S2s",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    S2s u0 {1,S}
8    Cd  u0 {4,D}
9    S2d u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1749,
    label = "Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)S2s",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    S2s u0 {1,S}
8    Cd  u0 {4,D}
9    C   u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1750,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)S2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   S2s u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
8   Cdd u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1751,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)S2s",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    S2s u0 {1,S}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
11   S2d u0 {7,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1752,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-Cd)S2s",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    S2s u0 {1,S}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1753,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)S2s",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    S2s u0 {1,S}
9    S2d u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1754,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)S2s",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    S2s u0 {1,S}
9    C   u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1755,
    label = "Cs-CtCdsCdsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S}
3   Cd  u0 {1,S}
4   Cd  u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1756,
    label = "Cs-(Cds-Cd)(Cds-Cd)CtSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Ct  u0 {1,S}
5   S2s u0 {1,S}
6   C   u0 {2,D}
7   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1757,
    label = "Cs-(Cds-Cds)(Cds-Cds)CtSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Ct  u0 {1,S}
5   S2s u0 {1,S}
6   Cd  u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1758,
    label = "Cs-(Cds-Cdd)(Cds-Cds)CtSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Ct  u0 {1,S}
5   S2s u0 {1,S}
6   Cdd u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1759,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cds)CtSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   S2s u0 {1,S}
7   Cd  u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1760,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CtSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   S2s u0 {1,S}
7   Cd  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1761,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)CtSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Ct  u0 {1,S}
5   S2s u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1762,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CtSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Ct  u0 {1,S}
7   S2s u0 {1,S}
8   S2d u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1763,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CtSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Ct  u0 {1,S}
7   S2s u0 {1,S}
8   S2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1764,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Ct  u0 {1,S}
7   S2s u0 {1,S}
8   C   u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1765,
    label = "Cs-CbCdsCdsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   Cd  u0 {1,S}
4   Cd  u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1766,
    label = "Cs-(Cds-Cd)(Cds-Cd)CbSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cb  u0 {1,S}
5   S2s u0 {1,S}
6   C   u0 {2,D}
7   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1767,
    label = "Cs-(Cds-Cds)(Cds-Cds)CbSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cb  u0 {1,S}
5   S2s u0 {1,S}
6   Cd  u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1768,
    label = "Cs-(Cds-Cdd)(Cds-Cds)CbSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cb  u0 {1,S}
5   S2s u0 {1,S}
6   Cdd u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1769,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cds)CbSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   S2s u0 {1,S}
7   Cd  u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1770,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CbSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   S2s u0 {1,S}
7   Cd  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1771,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)CbSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cb  u0 {1,S}
5   S2s u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1772,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CbSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   S2s u0 {1,S}
8   S2d u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1773,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CbSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   S2s u0 {1,S}
8   S2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1774,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   S2s u0 {1,S}
8   C   u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1775,
    label = "Cs-CtCtCdsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S}
3   Ct  u0 {1,S}
4   Cd  u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1776,
    label = "Cs-(Cds-Cd)CtCtSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   Ct  u0 {1,S}
5   S2s u0 {1,S}
6   C   u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1777,
    label = "Cs-(Cds-Cds)CtCtSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   Ct  u0 {1,S}
5   S2s u0 {1,S}
6   Cd  u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1778,
    label = "Cs-(Cds-Cdd)CtCtSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   Ct  u0 {1,S}
5   S2s u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1779,
    label = "Cs-(Cds-Cdd-S2d)CtCtSs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   S2s u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1780,
    label = "Cs-(Cds-Cdd-Cd)CtCtSs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   S2s u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1781,
    label = "Cs-CbCtCdsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   Ct  u0 {1,S}
4   Cd  u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1782,
    label = "Cs-(Cds-Cd)CbCtSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Ct  u0 {1,S}
5   S2s u0 {1,S}
6   C   u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1783,
    label = "Cs-(Cds-Cds)CbCtSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Ct  u0 {1,S}
5   S2s u0 {1,S}
6   Cd  u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1784,
    label = "Cs-(Cds-Cdd)CbCtSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Ct  u0 {1,S}
5   S2s u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1785,
    label = "Cs-(Cds-Cdd-S2d)CbCtSs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   S2s u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1786,
    label = "Cs-(Cds-Cdd-Cd)CbCtSs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   S2s u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1787,
    label = "Cs-CbCbCdsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   Cb  u0 {1,S}
4   Cd  u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1788,
    label = "Cs-(Cds-Cd)CbCbSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
5   S2s u0 {1,S}
6   C   u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1789,
    label = "Cs-(Cds-Cds)CbCbSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
5   S2s u0 {1,S}
6   Cd  u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1790,
    label = "Cs-(Cds-Cdd)CbCbSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
5   S2s u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1791,
    label = "Cs-(Cds-Cdd-S2d)CbCbSs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   S2s u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1792,
    label = "Cs-(Cds-Cdd-Cd)CbCbSs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   S2s u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1793,
    label = "Cs-CtCtCtSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S}
3   Ct  u0 {1,S}
4   Ct  u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1794,
    label = "Cs-CbCtCtSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   Ct  u0 {1,S}
4   Ct  u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1795,
    label = "Cs-CbCbCtSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   Cb  u0 {1,S}
4   Ct  u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1796,
    label = "Cs-CbCbCbSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1797,
    label = "Cs-C=SCbCsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Cs  u0 {1,S}
5   S2s u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1798,
    label = "Cs-C=SCsCsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   S2s u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1799,
    label = "Cs-C=S(Cds-Cd)(Cds-Cd)S2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   S2s u0 {1,S}
6   C   u0 {3,D}
7   C   u0 {4,D}
8   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1800,
    label = "Cs-C=S(Cds-Cdd)(Cds-Cdd)S2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   S2s u0 {1,S}
6   Cdd u0 {3,D}
7   Cdd u0 {4,D}
8   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1801,
    label = "Cs-C=S(Cds-Cdd-Cd)(Cds-Cdd-Cd)S2s",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CS  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    S2s u0 {1,S}
8    S2d u0 {4,D}
9    C   u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1802,
    label = "Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-Cd)S2s",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CS  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    S2s u0 {1,S}
8    S2d u0 {4,D}
9    S2d u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1803,
    label = "Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-S2d)S2s",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CS  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    S2s u0 {1,S}
8    S2d u0 {4,D}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1804,
    label = "Cs-C=S(Cds-Cdd)(Cds-Cds)S2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   S2s u0 {1,S}
6   Cdd u0 {3,D}
7   Cd  u0 {4,D}
8   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1805,
    label = "Cs-C=S(Cds-Cdd-Cd)(Cds-Cds)S2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CS  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {9,D}
6   S2s u0 {1,S}
7   Cd  u0 {4,D}
8   S2d u0 {3,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1806,
    label = "Cs-C=S(Cds-Cdd-S2d)(Cds-Cds)S2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CS  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {9,D}
6   S2s u0 {1,S}
7   Cd  u0 {4,D}
8   S2d u0 {3,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1807,
    label = "Cs-C=S(Cds-Cds)(Cds-Cds)S2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   S2s u0 {1,S}
6   Cd  u0 {3,D}
7   Cd  u0 {4,D}
8   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1808,
    label = "Cs-C=S(Cds-Cd)CtSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   S2s u0 {1,S}
6   C   u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1809,
    label = "Cs-C=S(Cds-Cds)CtSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   S2s u0 {1,S}
6   Cd  u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1810,
    label = "Cs-C=S(Cds-Cdd)CtSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   S2s u0 {1,S}
6   Cdd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1811,
    label = "Cs-C=S(Cds-Cdd-S2d)CtSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   S2s u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1812,
    label = "Cs-C=S(Cds-Cdd-Cd)CtSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   S2s u0 {1,S}
7   S2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1813,
    label = "Cs-C=SCtCsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   Cs  u0 {1,S}
5   S2s u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1814,
    label = "Cs-C=SC=SC=SSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   CS  u0 {1,S} {7,D}
4   CS  u0 {1,S} {8,D}
5   S2s u0 {1,S}
6   S2d u0 {2,D}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1815,
    label = "Cs-C=SC=S(Cds-Cd)S2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   CS  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   S2s u0 {1,S}
6   C   u0 {4,D}
7   S2d u0 {2,D}
8   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1816,
    label = "Cs-C=SC=S(Cds-Cds)S2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   CS  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   S2s u0 {1,S}
6   Cd  u0 {4,D}
7   S2d u0 {2,D}
8   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1817,
    label = "Cs-C=SC=S(Cds-Cdd)S2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   CS  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   S2s u0 {1,S}
6   Cdd u0 {4,D}
7   S2d u0 {2,D}
8   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1818,
    label = "Cs-C=SC=S(Cds-Cdd-S2d)S2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CS  u0 {1,S} {7,D}
4   CS  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   S2s u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1819,
    label = "Cs-C=SC=S(Cds-Cdd-Cd)S2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CS  u0 {1,S} {7,D}
4   CS  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   S2s u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1820,
    label = "Cs-C=SCbCbSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
5   S2s u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1821,
    label = "Cs-C=SC=SCbSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   CS  u0 {1,S} {7,D}
4   Cb  u0 {1,S}
5   S2s u0 {1,S}
6   S2d u0 {2,D}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1822,
    label = "Cs-C=SC=SCsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   CS  u0 {1,S} {7,D}
4   Cs  u0 {1,S}
5   S2s u0 {1,S}
6   S2d u0 {2,D}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1823,
    label = "Cs-C=SCtCtSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   Ct  u0 {1,S}
5   S2s u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1824,
    label = "Cs-C=S(Cds-Cd)CbSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   S2s u0 {1,S}
6   C   u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1825,
    label = "Cs-C=S(Cds-Cdd)CbSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   S2s u0 {1,S}
6   Cdd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1826,
    label = "Cs-C=S(Cds-Cdd-Cd)CbSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   S2s u0 {1,S}
7   S2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1827,
    label = "Cs-C=S(Cds-Cdd-S2d)CbSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   S2s u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1828,
    label = "Cs-C=S(Cds-Cds)CbSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   S2s u0 {1,S}
6   Cd  u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1829,
    label = "Cs-C=SCbCtSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Ct  u0 {1,S}
5   S2s u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1830,
    label = "Cs-C=SC=SCtSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   CS  u0 {1,S} {7,D}
4   Ct  u0 {1,S}
5   S2s u0 {1,S}
6   S2d u0 {2,D}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1831,
    label = "Cs-C=S(Cds-Cd)CsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   S2s u0 {1,S}
6   C   u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1832,
    label = "Cs-C=S(Cds-Cds)CsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   S2s u0 {1,S}
6   Cd  u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1833,
    label = "Cs-C=S(Cds-Cdd)CsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   S2s u0 {1,S}
6   Cdd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1834,
    label = "Cs-C=S(Cds-Cdd-S2d)CsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   S2s u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1835,
    label = "Cs-C=S(Cds-Cdd-Cd)CsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   S2s u0 {1,S}
7   S2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1836,
    label = "Cs-CCSS",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   S  u0 {1,S}
5   S  u0 {1,S}
""",
    thermo = 'Cs-CsCsSS',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1837,
    label = "Cs-CsCsSS",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   S  u0 {1,S}
5   S  u0 {1,S}
""",
    thermo = 'Cs-CsCsS2S2',
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc = 
"""
"
""",
)

entry(
    index = 1838,
    label = "Cs-CsCsS2S2",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.83,10.39,10.63,10.76,13.38,14.21,10.84],'cal/(mol*K)'),
        H298 = (24.52,'kcal/mol'),
        S298 = (-26.78,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 1839,
    label = "Cs-CsCsS6S2",
    group = 
"""
1 * Cs                      u0 {2,S} {3,S} {4,S} {5,S}
2   Cs                      u0 {1,S}
3   Cs                      u0 {1,S}
4   [S6s,S6d,S6dd,S6t,S6td] u0 {1,S}
5   S2s                     u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.61,8.47,9.47,10.23,13.38,14.44,10.88],'cal/(mol*K)'),
        H298 = (20.26,'kcal/mol'),
        S298 = (-21.75,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 1840,
    label = "Cs-CdsCsSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S}
3   Cs  u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1841,
    label = "Cs-(Cds-Cd)CsSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   C   u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1842,
    label = "Cs-(Cds-Cds)CsSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   Cd  u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1843,
    label = "Cs-(Cds-Cdd)CsSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1844,
    label = "Cs-(Cds-Cdd-S2d)CsSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cs  u0 {1,S}
5   S2s u0 {1,S}
6   S2s u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1845,
    label = "Cs-(Cds-Cdd-Cd)CsSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cs  u0 {1,S}
5   S2s u0 {1,S}
6   S2s u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1846,
    label = "Cs-CdsCdsSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S}
3   Cd  u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1847,
    label = "Cs-(Cds-Cd)(Cds-Cd)SsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   C   u0 {2,D}
7   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1848,
    label = "Cs-(Cds-Cds)(Cds-Cds)SsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   Cd  u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1849,
    label = "Cs-(Cds-Cdd)(Cds-Cds)SsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   Cdd u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1850,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cds)SsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   S2s u0 {1,S}
6   S2s u0 {1,S}
7   Cd  u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1851,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)SsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   S2s u0 {1,S}
6   S2s u0 {1,S}
7   Cd  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1852,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)SsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1853,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)SsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   S2s u0 {1,S}
7   S2s u0 {1,S}
8   S2d u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1854,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)SsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   S2s u0 {1,S}
7   S2s u0 {1,S}
8   S2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1855,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)SsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   S2s u0 {1,S}
7   S2s u0 {1,S}
8   C   u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1856,
    label = "Cs-CtCsSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S}
3   Cs  u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1857,
    label = "Cs-CtCdsSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S}
3   Cd  u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1858,
    label = "Cs-(Cds-Cd)CtSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   C   u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1859,
    label = "Cs-(Cds-Cds)CtSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   Cd  u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1860,
    label = "Cs-(Cds-Cdd)CtSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1861,
    label = "Cs-(Cds-Cdd-S2d)CtSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   S2s u0 {1,S}
6   S2s u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1862,
    label = "Cs-(Cds-Cdd-Cd)CtSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   S2s u0 {1,S}
6   S2s u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1863,
    label = "Cs-CtCtSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S}
3   Ct  u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1864,
    label = "Cs-CbCsSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   Cs  u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1865,
    label = "Cs-CbCdsSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   Cd  u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1866,
    label = "Cs-(Cds-Cd)CbSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   C   u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1867,
    label = "Cs-(Cds-Cds)CbSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   Cd  u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1868,
    label = "Cs-(Cds-Cdd)CbSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1869,
    label = "Cs-(Cds-Cdd-S2d)CbSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   S2s u0 {1,S}
6   S2s u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1870,
    label = "Cs-(Cds-Cdd-Cd)CbSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   S2s u0 {1,S}
6   S2s u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1871,
    label = "Cs-CbCtSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   Ct  u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1872,
    label = "Cs-CbCbSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   Cb  u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1873,
    label = "Cs-C=SCsSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1874,
    label = "Cs-C=S(Cds-Cd)SsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   C   u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1875,
    label = "Cs-C=S(Cds-Cdd)SsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   Cdd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1876,
    label = "Cs-C=S(Cds-Cdd-Cd)SsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   S2s u0 {1,S}
6   S2s u0 {1,S}
7   S2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1877,
    label = "Cs-C=S(Cds-Cdd-S2d)SsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   S2s u0 {1,S}
6   S2s u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1878,
    label = "Cs-C=S(Cds-Cds)SsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   Cd  u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1879,
    label = "Cs-C=SC=SSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   CS  u0 {1,S} {7,D}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   S2d u0 {2,D}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1880,
    label = "Cs-C=SCbSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1881,
    label = "Cs-C=SCtSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1882,
    label = "Cs-CSsSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   C   u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1883,
    label = "Cs-CsSsSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.76,12.55,12.86,12.95,16.67,17.86,12.77],'cal/(mol*K)'),
        H298 = (37.76,'kcal/mol'),
        S298 = (-23.39,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 1884,
    label = "Cs-CdsSsSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1885,
    label = "Cs-(Cds-Cd)SsSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   C   u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1886,
    label = "Cs-(Cds-Cds)SsSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   Cd  u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1887,
    label = "Cs-(Cds-Cdd)SsSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1888,
    label = "Cs-(Cds-Cdd-S2d)SsSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   S2s u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1889,
    label = "Cs-(Cds-Cdd-Cd)SsSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   S2s u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1890,
    label = "Cs-CtSsSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1891,
    label = "Cs-CbSsSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1892,
    label = "Cs-C=SSsSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1893,
    label = "Cs-SsSsSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   S2s u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.33,15.09,16.62,17.94,24.67,27.95,23.34],'cal/(mol*K)'),
        H298 = (33.21,'kcal/mol'),
        S298 = (-20.45,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 1894,
    label = "Cs-CSSH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   S  u0 {1,S}
4   S  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = 'Cs-CsSSH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1895,
    label = "Cs-CsSSH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   S  u0 {1,S}
4   S  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = 'Cs-CsS2S2H',
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc = 
"""
"
""",
)

entry(
    index = 1896,
    label = "Cs-CsS2S2H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.47,10.83,11.17,11.54,14.74,16.21,13.93],'cal/(mol*K)'),
        H298 = (22.59,'kcal/mol'),
        S298 = (-4.77,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 1897,
    label = "Cs-CsS4S2H",
    group = 
"""
1 * Cs                u0 {2,S} {3,S} {4,S} {5,S}
2   Cs                u0 {1,S}
3   [S4s,S4d,S4b,S4t] u0 {1,S}
4   S2s               u0 {1,S}
5   H                 u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.81,11.54,12.42,13.49,17.89,19.74,16.4],'cal/(mol*K)'),
        H298 = (18.39,'kcal/mol'),
        S298 = (-14.28,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 1898,
    label = "Cs-CsS6S2H",
    group = 
"""
1 * Cs                      u0 {2,S} {3,S} {4,S} {5,S}
2   Cs                      u0 {1,S}
3   [S6s,S6d,S6dd,S6t,S6td] u0 {1,S}
4   S2s                     u0 {1,S}
5   H                       u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.79,9.79,12.04,13.48,17.54,19.23,16.19],'cal/(mol*K)'),
        H298 = (18.74,'kcal/mol'),
        S298 = (-6.26,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 1899,
    label = "Cs-CdsSsSsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1900,
    label = "Cs-(Cds-Cd)SsSsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   H   u0 {1,S}
6   C   u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1901,
    label = "Cs-(Cds-Cds)SsSsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   H   u0 {1,S}
6   Cd  u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1902,
    label = "Cs-(Cds-Cdd)SsSsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1903,
    label = "Cs-(Cds-Cdd-S2d)SsSsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1904,
    label = "Cs-(Cds-Cdd-Cd)SsSsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   H   u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1905,
    label = "Cs-CtSsSsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1906,
    label = "Cs-CbSsSsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1907,
    label = "Cs-C=SSsSsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   H   u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1908,
    label = "Cs-CCSH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   S  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = 'Cs-CsCsSH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1909,
    label = "Cs-CsCsSH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   S  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = 'Cs-CsCsS2H',
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc = 
"""
"
""",
)

entry(
    index = 1910,
    label = "Cs-CsCsS2H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   S2s u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.41,7.56,8.52,9.25,11.57,12.8,12.07],'cal/(mol*K)'),
        H298 = (11.07,'kcal/mol'),
        S298 = (-7.17,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 1911,
    label = "Cs-CsCsS4H",
    group = 
"""
1 * Cs                u0 {2,S} {3,S} {4,S} {5,S}
2   Cs                u0 {1,S}
3   Cs                u0 {1,S}
4   [S4s,S4d,S4b,S4t] u0 {1,S}
5   H                 u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.45,5.07,5.65,6.45,9.65,11.6,12.52],'cal/(mol*K)'),
        H298 = (12.82,'kcal/mol'),
        S298 = (-7.24,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 1912,
    label = "Cs-CsCsS6H",
    group = 
"""
1 * Cs                      u0 {2,S} {3,S} {4,S} {5,S}
2   Cs                      u0 {1,S}
3   Cs                      u0 {1,S}
4   [S6s,S6d,S6dd,S6t,S6td] u0 {1,S}
5   H                       u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.72,5.38,6.37,7.25,9.88,11.39,11.46],'cal/(mol*K)'),
        H298 = (5.98,'kcal/mol'),
        S298 = (-5.67,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 1913,
    label = "Cs-CdsCsSH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   Cs      u0 {1,S}
4   S       u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = 'Cs-(Cds-Cd)CsSsH',
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc = 
"""
"
""",
)

entry(
    index = 1914,
    label = "Cs-CdsCsS4H",
    group = 
"""
1 * Cs                u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO]           u0 {1,S}
3   Cs                u0 {1,S}
4   [S4s,S4d,S4b,S4t] u0 {1,S}
5   H                 u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.04343,9.7511,9.94209,10.4998,13.2832,14.9311,14.2721],'cal/(mol*K)'),
        H298 = (5.13823,'kcal/mol'),
        S298 = (-1.82552,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 1915,
    label = "Cs-(Cds-Cd)CsSsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   S2s u0 {1,S}
5   H   u0 {1,S}
6   C   u0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)CsSsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1916,
    label = "Cs-(Cds-Cds)CsSsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   S2s u0 {1,S}
5   H   u0 {1,S}
6   Cd  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.97,10.76,11.55,11.83,13.17,13.89,12.78],'cal/(mol*K)'),
        H298 = (10.35,'kcal/mol'),
        S298 = (-9.71,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""

""",
)

entry(
    index = 1917,
    label = "Cs-(Cds-Cdd)CsSsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   S2s u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1918,
    label = "Cs-(Cds-Cdd-S2d)CsSsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cs  u0 {1,S}
5   S2s u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1919,
    label = "Cs-(Cds-Cdd-Cd)CsSsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cs  u0 {1,S}
5   S2s u0 {1,S}
6   H   u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1920,
    label = "Cs-CdsCdsSsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S}
3   Cd  u0 {1,S}
4   S2s u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1921,
    label = "Cs-(Cds-Cd)(Cds-Cd)SsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   S2s u0 {1,S}
5   H   u0 {1,S}
6   C   u0 {2,D}
7   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1922,
    label = "Cs-(Cds-Cds)(Cds-Cds)SsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   S2s u0 {1,S}
5   H   u0 {1,S}
6   Cd  u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1923,
    label = "Cs-(Cds-Cdd)(Cds-Cds)SsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   S2s u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1924,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cds)SsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   S2s u0 {1,S}
6   H   u0 {1,S}
7   Cd  u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1925,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)SsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   S2s u0 {1,S}
6   H   u0 {1,S}
7   Cd  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1926,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)SsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   S2s u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1927,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)SsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   S2s u0 {1,S}
7   H   u0 {1,S}
8   S2d u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1928,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)SsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   S2s u0 {1,S}
7   H   u0 {1,S}
8   S2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1929,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)SsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   S2s u0 {1,S}
7   H   u0 {1,S}
8   C   u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1930,
    label = "Cs-CtCsSsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S}
3   Cs  u0 {1,S}
4   S2s u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.62,7.79,8.7,9.44,11.69,12.98,11.46],'cal/(mol*K)'),
        H298 = (13.55,'kcal/mol'),
        S298 = (-6.16,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 1931,
    label = "Cs-CtCdsSsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S}
3   Cd  u0 {1,S}
4   S2s u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1932,
    label = "Cs-(Cds-Cd)CtSsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   S2s u0 {1,S}
5   H   u0 {1,S}
6   C   u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1933,
    label = "Cs-(Cds-Cds)CtSsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   S2s u0 {1,S}
5   H   u0 {1,S}
6   Cd  u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1934,
    label = "Cs-(Cds-Cdd)CtSsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   S2s u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1935,
    label = "Cs-(Cds-Cdd-S2d)CtSsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   S2s u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1936,
    label = "Cs-(Cds-Cdd-Cd)CtSsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   S2s u0 {1,S}
6   H   u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1937,
    label = "Cs-CtCtSsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S}
3   Ct  u0 {1,S}
4   S2s u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1938,
    label = "Cs-CbCsSsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   Cs  u0 {1,S}
4   S2s u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.44,8.88,9.92,10.57,12.5,13.34,12.17],'cal/(mol*K)'),
        H298 = (11.58,'kcal/mol'),
        S298 = (-9,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 1939,
    label = "Cs-CbCdsSsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   Cd  u0 {1,S}
4   S2s u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1940,
    label = "Cs-(Cds-Cd)CbSsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   S2s u0 {1,S}
5   H   u0 {1,S}
6   C   u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1941,
    label = "Cs-(Cds-Cds)CbSsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   S2s u0 {1,S}
5   H   u0 {1,S}
6   Cd  u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1942,
    label = "Cs-(Cds-Cdd)CbSsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   S2s u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1943,
    label = "Cs-(Cds-Cdd-S2d)CbSsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   S2s u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1944,
    label = "Cs-(Cds-Cdd-Cd)CbSsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   S2s u0 {1,S}
6   H   u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1945,
    label = "Cs-CbCtSsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   Ct  u0 {1,S}
4   S2s u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1946,
    label = "Cs-CbCbSsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   Cb  u0 {1,S}
4   S2s u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1947,
    label = "Cs-C=SCbSsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   S2s u0 {1,S}
5   H   u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1948,
    label = "Cs-C=SC=SSsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   CS  u0 {1,S} {7,D}
4   S2s u0 {1,S}
5   H   u0 {1,S}
6   S2d u0 {2,D}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1949,
    label = "Cs-C=SCsSsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   S2s u0 {1,S}
5   H   u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.76,10.49,12.16,12.69,14.03,14.39,12.81],'cal/(mol*K)'),
        H298 = (12.61,'kcal/mol'),
        S298 = (-10.23,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 1950,
    label = "Cs-C=SCtSsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   S2s u0 {1,S}
5   H   u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1951,
    label = "Cs-C=S(Cds-Cd)SsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   S2s u0 {1,S}
5   H   u0 {1,S}
6   C   u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1952,
    label = "Cs-C=S(Cds-Cdd)SsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   S2s u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1953,
    label = "Cs-C=S(Cds-Cdd-Cd)SsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   S2s u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1954,
    label = "Cs-C=S(Cds-Cdd-S2d)SsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   S2s u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1955,
    label = "Cs-C=S(Cds-Cds)SsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   S2s u0 {1,S}
5   H   u0 {1,S}
6   Cd  u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1956,
    label = "Cs-CSHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   S  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = 'Cs-CsSHH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1957,
    label = "Cs-CsSHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   S  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = 'Cs-CsS2HH',
    shortDesc = """""",
    longDesc = 
"""
"
""",
)

entry(
    index = 1958,
    label = "Cs-CsS2HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 {1,S}
3   S2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.96,8.17,9.34,10.35,13.25,15.03,15.38],'cal/(mol*K)'),
        H298 = (6.95,'kcal/mol'),
        S298 = (14.5,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 1959,
    label = "Cs-CsS4HH",
    group = 
"""
1 * Cs                u0 {2,S} {3,S} {4,S} {5,S}
2   Cs                u0 {1,S}
3   [S4s,S4d,S4b,S4t] u0 {1,S}
4   H                 u0 {1,S}
5   H                 u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.12,6.09,6.9,7.99,11.61,14.01,15.09],'cal/(mol*K)'),
        H298 = (9.13,'kcal/mol'),
        S298 = (12.35,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 1960,
    label = "Cs-CsS6HH",
    group = 
"""
1 * Cs                      u0 {2,S} {3,S} {4,S} {5,S}
2   Cs                      u0 {1,S}
3   [S6s,S6d,S6dd,S6t,S6td] u0 {1,S}
4   H                       u0 {1,S}
5   H                       u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.91,5.81,7.26,8.55,11.77,13.8,14.82],'cal/(mol*K)'),
        H298 = (3.84,'kcal/mol'),
        S298 = (19.66,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 1961,
    label = "Cs-CdsSsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S}
3   S2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.96,10.86,11.45,12.01,14.21,15.74,15.89],'cal/(mol*K)'),
        H298 = (7.47,'kcal/mol'),
        S298 = (12.31,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 1962,
    label = "Cs-(Cds-Cd)SsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   S2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   C   u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1963,
    label = "Cs-(Cds-Cds)SsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   S2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   Cd  u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1964,
    label = "Cs-(Cds-Cdd)SsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   S2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1965,
    label = "Cs-(Cds-Cdd-S2d)SsHH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   S2s u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1966,
    label = "Cs-(Cds-Cdd-Cd)SsHH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   S2s u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1967,
    label = "Cs-CtSsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S}
3   S2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.95,8.29,9.45,10.53,13.39,15.28,14.76],'cal/(mol*K)'),
        H298 = (10.19,'kcal/mol'),
        S298 = (15.23,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 1968,
    label = "Cs-CbSsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   S2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.54,8.82,10.03,11.08,13.8,15.37,15.33],'cal/(mol*K)'),
        H298 = (6.16,'kcal/mol'),
        S298 = (12.86,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 1969,
    label = "Cs-C=SSsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   S2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.7,11.06,12.6,13.3,15.32,16.4,15.98],'cal/(mol*K)'),
        H298 = (10.03,'kcal/mol'),
        S298 = (11.36,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 1970,
    label = "Cs-ClClHH",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   H    u0 {1,S}
5   H    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.2,14.3,16,17.4,19.4,20.8,22.9],'cal/(mol*K)'),
        H298 = (-22.8,'kcal/mol'),
        S298 = (65.8,'cal/(mol*K)'),
    ),
    shortDesc = """CH2Cl2 BENSON""",
    longDesc = 
"""
Thermochemical Kinetics 2nd Ed., by Sidney Benson
""",
)

entry(
    index = 1971,
    label = "Cs-ClClClH",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cl1s u0 {1,S}
5   H    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.7,17.9,19.4,20.5,21.9,22.9,24.2],'cal/(mol*K)'),
        H298 = (-24.6,'kcal/mol'),
        S298 = (72.9,'cal/(mol*K)'),
    ),
    shortDesc = """CHCl3 BENSON""",
    longDesc = 
"""
Thermochemical Kinetics 2nd Ed., by Sidney Benson
""",
)

entry(
    index = 1972,
    label = "Cs-ClClClCl",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cl1s u0 {1,S}
5   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19.9,21.8,23,23.8,24.6,25,25.5],'cal/(mol*K)'),
        H298 = (-22.9,'kcal/mol'),
        S298 = (79.1,'cal/(mol*K)'),
    ),
    shortDesc = """CCl4 BENSON""",
    longDesc = 
"""
Thermochemical Kinetics 2nd Ed., by Sidney Benson
""",
)

entry(
    index = 1973,
    label = "Cs-CClHH",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   C    u0 {1,S}
3   Cl1s u0 {1,S}
4   H    u0 {1,S}
5   H    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.74,10.54,12.08,13.31,15.15,16.47,18.46],'cal/(mol*K)'),
        H298 = (-16.8,'kcal/mol'),
        S298 = (38.17,'cal/(mol*K)'),
    ),
    shortDesc = """C/C/Cl/H2 CHEN AND BOZZELLI""",
    longDesc = 
"""
Chinugh-Ju Chen, D. Wong, Joseph W. Bozzelli,
Standard Chemical Thermodynamic Properties of Multichloro Alkanes and Alkenes: A Modified Group Additivity Scheme
JPCA, 1998, 102, 4551-4558
""",
)

entry(
    index = 1974,
    label = "Cs-CIHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   C   u0 {1,S}
3   I1s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.2,11,12.9,13.9,15.8,17.2,18.6],'cal/(mol*K)'),
        H298 = (8,'kcal/mol'),
        S298 = (43,'cal/(mol*K)'),
    ),
    shortDesc = """C-(I)(H)2(C) BENSON""",
    longDesc = 
"""
Thermochemical Kinetics 2nd Ed., by Sidney Benson (Table A4, p.280)
Cpdata at 1500K = Cpdata at 1000K + 1.4
""",
)

entry(
    index = 1975,
    label = "Cs-CClClH",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   C    u0 {1,S}
3   Cl1s u0 {1,S}
4   Cl1s u0 {1,S}
5   H    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.99,13.98,15.53,16.62,18.09,18.8,19.43],'cal/(mol*K)'),
        H298 = (-21.04,'kcal/mol'),
        S298 = (44.91,'cal/(mol*K)'),
    ),
    shortDesc = """C/C/Cl2/H CHEN AND BOZZELLI""",
    longDesc = 
"""
Chinugh-Ju Chen, D. Wong, Joseph W. Bozzelli,
Standard Chemical Thermodynamic Properties of Multichloro Alkanes and Alkenes: A Modified Group Additivity Scheme
JPCA, 1998, 102, 4551-4558
""",
)

entry(
    index = 1976,
    label = "Cs-CIIH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   C   u0 {1,S}
3   I1s u0 {1,S}
4   I1s u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.2,13.4,16.4,17,17.7,18.4,19.1],'cal/(mol*K)'),
        H298 = (26,'kcal/mol'),
        S298 = (54.6,'cal/(mol*K)'),
    ),
    shortDesc = """C-(I)2(C)(H) BENSON""",
    longDesc = 
"""
Thermochemical Kinetics 2nd Ed., by Sidney Benson (Table A4, p.280)
Cpdata from 600 to 1500K estimated (base on entry 2088)
""",
)

entry(
    index = 1977,
    label = "Cs-CClClCl",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   C    u0 {1,S}
3   Cl1s u0 {1,S}
4   Cl1s u0 {1,S}
5   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.83,17.86,19.25,20.1,21.06,21.21,21.42],'cal/(mol*K)'),
        H298 = (-23.84,'kcal/mol'),
        S298 = (50.69,'cal/(mol*K)'),
    ),
    shortDesc = """C/C/Cl3 CHEN AND BOZZELLI""",
    longDesc = 
"""
Chinugh-Ju Chen, D. Wong, Joseph W. Bozzelli,
Standard Chemical Thermodynamic Properties of Multichloro Alkanes and Alkenes: A Modified Group Additivity Scheme
JPCA, 1998, 102, 4551-4558
""",
)

entry(
    index = 1978,
    label = "Cs-CCClH",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   C    u0 {1,S}
3   C    u0 {1,S}
4   Cl1s u0 {1,S}
5   H    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.47,10.2,11.68,12.76,14.29,15.38,16.21],'cal/(mol*K)'),
        H298 = (-14.47,'kcal/mol'),
        S298 = (17.33,'cal/(mol*K)'),
    ),
    shortDesc = """C/C2/Cl/H CHEN AND BOZZELLI""",
    longDesc = 
"""
Chinugh-Ju Chen, D. Wong, Joseph W. Bozzelli,
Standard Chemical Thermodynamic Properties of Multichloro Alkanes and Alkenes: A Modified Group Additivity Scheme
JPCA, 1998, 102, 4551-4558
""",
)

entry(
    index = 1979,
    label = "Cs-CCIH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
4   I1s u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.2,10.9,12.2,13,14.2,14.8,15.4],'cal/(mol*K)'),
        H298 = (10.5,'kcal/mol'),
        S298 = (21.3,'cal/(mol*K)'),
    ),
    shortDesc = """C-(I)(H)(C)2 BENSON""",
    longDesc = 
"""
Thermochemical Kinetics 2nd Ed., by Sidney Benson (Table A4, p.280)
Cpdata at 1500K = Cpdata at 1000K + 0.6
""",
)

entry(
    index = 1980,
    label = "Cs-CCClCl",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   C    u0 {1,S}
3   C    u0 {1,S}
4   Cl1s u0 {1,S}
5   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.12,14.88,15.95,16.48,16.96,17.02,16.82],'cal/(mol*K)'),
        H298 = (-22,'kcal/mol'),
        S298 = (23.06,'cal/(mol*K)'),
    ),
    shortDesc = """C/C2/Cl2 CHEN AND BOZZELLI""",
    longDesc = 
"""
Chinugh-Ju Chen, D. Wong, Joseph W. Bozzelli,
Standard Chemical Thermodynamic Properties of Multichloro Alkanes and Alkenes: A Modified Group Additivity Scheme
JPCA, 1998, 102, 4551-4558
""",
)

entry(
    index = 1981,
    label = "Cs-CCCCl",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   C    u0 {1,S}
3   C    u0 {1,S}
4   Cl1s u0 {1,S}
5   C    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.09,10.15,11.69,12.65,13.47,13.53,13.32],'cal/(mol*K)'),
        H298 = (-14.03,'kcal/mol'),
        S298 = (-6.45,'cal/(mol*K)'),
    ),
    shortDesc = """C/C3/Cl CHEN AND BOZZELLI""",
    longDesc = 
"""
Chinugh-Ju Chen, D. Wong, Joseph W. Bozzelli,
Standard Chemical Thermodynamic Properties of Multichloro Alkanes and Alkenes: A Modified Group Additivity Scheme
JPCA, 1998, 102, 4551-4558
""",
)

entry(
    index = 1982,
    label = "Cs-CCCI",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   I1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.7,11.4,12.7,13.9,14.7,15.3,15.9],'cal/(mol*K)'),
        H298 = (13,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """C-(I)(C)3  BENSON""",
    longDesc = 
"""
Thermochemical Kinetics 2nd Ed., by Sidney Benson (Table A4, p.280)
Cpdata from 400 to 1500K estimated (base on entry 2092)
""",
)

entry(
    index = 1983,
    label = "O",
    group = 
"""
1 * O u0
""",
    thermo = 'O2s-CsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1984,
    label = "Oa(S)",
    group = 
"""
1 * O u0 p3 c0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.968,4.968,4.968,4.968,4.968,4.968,4.968],'cal/(mol*K)'),
        H298 = (104.81,'kcal/mol'),
        S298 = (34.25,'cal/(mol*K)'),
    ),
    shortDesc = """PrimaryTHermoLibrary""",
    longDesc = 
"""
H298: ATcT version 1.110
level of theory energy: CCSD(T)F12A/cc-pVQZ-F12//CCSD(T)/cc-pVQZ
level of theory frequency: B3LYP/6-311++g(d,p)//B3LYP/6-311++g(d,p)
""",
)

entry(
    index = 1985,
    label = "O2d",
    group = 
"""
1 * O2d u0
""",
    thermo = 'O2d-Cd',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1986,
    label = "O2d-Cd",
    group = 
"""
1 * O2d u0 {2,D}
2   CO  u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """In this case the C is treated as the central atom""",
    longDesc = 
"""

""",
)

entry(
    index = 1987,
    label = "O2d-O2d",
    group = 
"""
1 * O2d u0 {2,D}
2   O2d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.5,3.575,3.685,3.8,3.99,4.12,4.29],'cal/(mol*K)'),
        H298 = (14.01,'kcal/mol'),
        S298 = (24.085,'cal/(mol*K)'),
    ),
    shortDesc = """A. Vandeputte""",
    longDesc = 
"""

""",
)

entry(
    index = 1988,
    label = "O2d-N3d",
    group = 
"""
1 * O2d u0 {2,D}
2   N3d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1989,
    label = "O2d-N5dc",
    group = 
"""
1 * O2d  u0 {2,D}
2   N5dc u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1990,
    label = "O2d-Sd",
    group = 
"""
1 * O2d u0 {2,D}
2   S   ux {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
Inferred from a least squares fit from 40 species mostly calculated at cbsqb3, 4/2017, Ryan Gillis
""",
)

entry(
    index = 1991,
    label = "O2s",
    group = 
"""
1 * O2s u0
""",
    thermo = 'O2s-(Cds-Cd)(Cds-Cd)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1992,
    label = "O2s-N",
    group = 
"""
1 * O2s u0 {2,S}
2   N   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1993,
    label = "O2s-CN",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   C   u0 {1,S}
3   N   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1994,
    label = "O2s-CsN3s",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   N3s u0 {1,S}
3   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.5,3.6,4,4.3,4.7,4.8,4.2],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-9.2,'kcal/mol','+|-',1.3),
        S298 = (7.2,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1995,
    label = "O2s-CsN3d",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cs  u0 {1,S}
3   N3d u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1996,
    label = "O2s-Cs(N3dOd)",
    group = 
"""
1 * O2s u0 {2,S} {4,S}
2   N3d u0 {1,S} {3,D}
3   O2d u0 {2,D}
4   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.6,11.3,11.9,12.6,13.6,14.3,14.8],'cal/(mol*K)','+|-',[0.8,0.8,0.8,0.8,0.8,0.8,0.8]),
        H298 = (-4.8,'kcal/mol','+|-',1.1),
        S298 = (40,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1997,
    label = "O2s-CdN3d",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cd  u0 {1,S}
3   N3d u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1998,
    label = "O2s-(Cd-Cd)(N3dOd)",
    group = 
"""
1   Cd  u0 {2,S} {4,D} {5,S}
2 * O2s u0 {1,S} {3,S}
3   N3d u0 {2,S} {6,D}
4   Cd  u0 {1,D}
5   R   u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.1,11.7,12.2,12.7,13.5,14.1,14.9],'cal/(mol*K)','+|-',[0.7,0.7,0.7,0.7,0.7,0.7,0.7]),
        H298 = (-5.3,'kcal/mol','+|-',0.9),
        S298 = (39.5,'cal/(mol*K)','+|-',0.9),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1999,
    label = "O2s-CsN5dc",
    group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   Cs   u0 {1,S}
3   N5dc u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2000,
    label = "O2s-Cs(N5dcOdOs)",
    group = 
"""
1   N5dc u0 {2,S} {3,D} {4,S}
2 * O2s  u0 {1,S} {5,S}
3   O2d  u0 {1,D}
4   O2s  u0 {1,S}
5   Cs   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.2,13.9,15.4,16.6,18.4,19.3,19.9],'cal/(mol*K)','+|-',[0.8,0.8,0.8,0.8,0.8,0.8,0.8]),
        H298 = (-19.1,'kcal/mol','+|-',1.1),
        S298 = (45.3,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2001,
    label = "O2s-CdN5dc",
    group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   Cd   u0 {1,S}
3   N5dc u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2002,
    label = "O2s-(Cd-CdHH)(N5dcOdOs)",
    group = 
"""
1   N5dc u0 {3,S} {4,D} {5,S}
2   Cd   u0 {3,S} {6,D} {7,S}
3 * O2s  u0 {1,S} {2,S}
4   O2d  u0 {1,D}
5   O2s  u0 {1,S}
6   Cd   u0 {2,D}
7   R    u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.4,14.2,15.7,16.9,18.5,19.3,20.1],'cal/(mol*K)','+|-',[0.8,0.8,0.8,0.8,0.8,0.8,0.8]),
        H298 = (-18.4,'kcal/mol','+|-',1.1),
        S298 = (45.4,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2003,
    label = "O2s-ON",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   O2s u0 {1,S}
3   N   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2004,
    label = "O2s-OsN3s",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   N3s u0 {1,S}
3   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.3,4.9,5.6,6.3,7,7.1,6.5],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (5.3,'kcal/mol','+|-',1.3),
        S298 = (6.9,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2005,
    label = "O2s-OsN3d",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   O2s u0 {1,S}
3   N3d u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2006,
    label = "O2s-O2s(N3dOd)",
    group = 
"""
1 * O2s u0 {2,S} {4,S}
2   N3d u0 {1,S} {3,D}
3   O2d u0 {2,D}
4   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.7,12.9,13.6,14.2,15,15.5,16],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (15.2,'kcal/mol','+|-',1.3),
        S298 = (40.7,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2007,
    label = "O2s-NN",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   N   u0 {1,S}
3   N   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2008,
    label = "O2s-N3sN3s",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   N3s u0 {1,S}
3   N3s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.8,4.6,5.1,5.2,5.2,4.9,4.3],'cal/(mol*K)','+|-',[1.6,1.6,1.6,1.6,1.6,1.6,1.6]),
        H298 = (5.7,'kcal/mol','+|-',2.2),
        S298 = (6.8,'cal/(mol*K)','+|-',2.1),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2009,
    label = "O2s-N3sN3d",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   N3s u0 {1,S}
3   N3d u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2010,
    label = "O2s-N3s(N3dOd)",
    group = 
"""
1 * O2s u0 {2,S} {4,S}
2   N3d u0 {1,S} {3,D}
3   O2d u0 {2,D}
4   N3s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.2,11.5,12.4,13,13.9,14.3,14.8],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (10.8,'kcal/mol','+|-',1.3),
        S298 = (40.8,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2011,
    label = "O2s-HH",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   H   u0 {1,S}
3   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.03,8.19,8.42,8.68,9.26,9.86,11.26],'cal/(mol*K)'),
        H298 = (-57.8,'kcal/mol','+|-',0.01),
        S298 = (46.51,'cal/(mol*K)','+|-',0.002),
    ),
    shortDesc = """O-HH WATER. !!!Using NIST value for H2O, S(group) = S(H2O) + Rln(2)""",
    longDesc = 
"""

""",
)

entry(
    index = 2012,
    label = "O2s-OsH",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   O2s u0 {1,S}
3   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.21,5.72,6.17,6.66,7.15,7.61,8.43],'cal/(mol*K)','+|-',[0.07,0.07,0.07,0.07,0.07,0.07,0.07]),
        H298 = (-16.3,'kcal/mol','+|-',0.14),
        S298 = (27.83,'cal/(mol*K)','+|-',0.07),
    ),
    shortDesc = """O-OH SANDIA 1/2*H2O2""",
    longDesc = 
"""

""",
)

entry(
    index = 2013,
    label = "O2s-OsOs",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   O2s u0 {1,S}
3   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.2,3.64,4.2,4.34,4.62,4.9,4.9],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (8.85,'kcal/mol','+|-',0.16),
        S298 = (9.4,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = """O-OO LAY 1997=20 !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
"""

""",
)

entry(
    index = 2014,
    label = "O2s-SsOs",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   S   u0 {1,S}
3   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.22,3.81,4.08,4.22,4.78,4.9,4.88],'cal/(mol*K)'),
        H298 = (-3.35,'kcal/mol'),
        S298 = (8.69,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""

""",
)

entry(
    index = 2015,
    label = "O2s-CH",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   C   u0 {1,S}
3   H   u0 {1,S}
""",
    thermo = 'O2s-CsH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2016,
    label = "O2s-CtH",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Ct  u0 {1,S}
3   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.3,4.5,4.82,5.23,6.02,6.61,7.44],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-37.9,'kcal/mol','+|-',0.16),
        S298 = (29.1,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = """O-CtH BENSON (Assigned O-CsH)""",
    longDesc = 
"""

""",
)

entry(
    index = 2017,
    label = "O2s-CdsH",
    group = 
"""
1 * O2s     u0 {2,S} {3,S}
2   [Cd,CO] u0 {1,S}
3   H       u0 {1,S}
""",
    thermo = 'O2s-(Cds-Cd)H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2018,
    label = "O2s-(Cds-O2d)H",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   CO  u0 {1,S} {4,D}
3   H   u0 {1,S}
4   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19.07,19.8,20.85,22.07,24.57,26.95,31.66],'J/(mol*K)','+|-',[2.54,2.54,2.54,2.54,2.54,2.54,2.54]),
        H298 = (-165.2,'kJ/mol','+|-',2.16),
        S298 = (125.32,'J/(mol*K)','+|-',2.96),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 2019,
    label = "O2s-(Cds-Cd)H",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cd  u0 {1,S} {4,D}
3   H   u0 {1,S}
4   C   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([24.6,30.3,32.52,33.15,33.29,33.55,34.97],'J/(mol*K)','+|-',[4.18,4.18,4.18,4.18,4.18,4.18,4.18]),
        H298 = (-188.1,'kJ/mol','+|-',3.56),
        S298 = (106.3,'J/(mol*K)','+|-',4.87),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 2020,
    label = "O2s-CsH",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cs  u0 {1,S}
3   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19.07,19.8,20.85,22.07,24.57,26.95,31.66],'J/(mol*K)','+|-',[2.54,2.54,2.54,2.54,2.54,2.54,2.54]),
        H298 = (-165.2,'kJ/mol','+|-',2.16),
        S298 = (125.32,'J/(mol*K)','+|-',2.96),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 2021,
    label = "O2s-CbH",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cb  u0 {1,S}
3   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.3,4.5,4.82,5.23,6.02,6.61,7.44],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-37.9,'kcal/mol','+|-',0.16),
        S298 = (29.1,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = """O-CbH BENSON (Assigned O-CsH)""",
    longDesc = 
"""

""",
)

entry(
    index = 2022,
    label = "O2s-CSH",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   CS  u0 {1,S} {4,D}
3   H   u0 {1,S}
4   S2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.4,3.15,4.19,5.05,6.21,7.04,8.41],'cal/(mol*K)'),
        H298 = (-47.58,'kcal/mol'),
        S298 = (27.77,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2023,
    label = "O2s-OsC",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   O2s u0 {1,S}
3   C   u0 {1,S}
""",
    thermo = 'O2s-OsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2024,
    label = "O2s-OsCt",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   O2s u0 {1,S}
3   Ct  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.9,4.31,4.6,4.84,5.32,5.8,5.8],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (7,'kcal/mol','+|-',0.3),
        S298 = (10.8,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = """O-OCb Hf JWB plot S,Cp assigned O/O/Cd !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
"""

""",
)

entry(
    index = 2025,
    label = "O2s-OsCds",
    group = 
"""
1 * O2s     u0 {2,S} {3,S}
2   O2s     u0 {1,S}
3   [Cd,CO] u0 {1,S}
""",
    thermo = 'O2s-O2s(Cds-Cd)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2026,
    label = "O2s-O2s(Cds-O2d)",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   CO  u0 {1,S} {4,D}
3   O2s u0 {1,S}
4   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.53,5.02,5.79,6.08,6.54,6.49,6.49],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (-23.22,'kcal/mol','+|-',0.3),
        S298 = (9.11,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = """O-OCO jwl cbsQ 99 cqcho=20 !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
"""

""",
)

entry(
    index = 2027,
    label = "O2s-O2s(Cds-Cd)",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cd  u0 {1,S} {4,D}
3   O2s u0 {1,S}
4   C   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.5,3.87,3.95,4.15,4.73,4.89,4.89],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (1.64,'kcal/mol','+|-',0.3),
        S298 = (10.12,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = """O-OCd WESTMORELAND S,Cp LAY'9405 !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
"""

""",
)

entry(
    index = 2028,
    label = "O2s-OsCs",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   O2s u0 {1,S}
3   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.9,4.31,4.6,4.84,5.32,5.8,5.8],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (-5.4,'kcal/mol','+|-',0.3),
        S298 = (8.54,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = """O-OCs LAY 1997 !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
"""

""",
)

entry(
    index = 2029,
    label = "O2s-OsCb",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   O2s u0 {1,S}
3   Cb  u0 {1,S}
""",
    thermo = 'O2s-O2s(Cds-Cd)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2030,
    label = "O2s-CC",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
""",
    thermo = 'O2s-(Cds-Cd)(Cds-Cd)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2031,
    label = "O2s-CtCt",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Ct  u0 {1,S}
3   Ct  u0 {1,S}
""",
    thermo = 'O2s-(Cds-Cd)(Cds-Cd)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2032,
    label = "O2s-CtCds",
    group = 
"""
1 * O2s     u0 {2,S} {3,S}
2   Ct      u0 {1,S}
3   [Cd,CO] u0 {1,S}
""",
    thermo = 'O2s-(Cds-Cd)(Cds-Cd)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2033,
    label = "O2s-Ct(Cds-O2d)",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   CO  u0 {1,S} {4,D}
3   Ct  u0 {1,S}
4   O2d u0 {2,D}
""",
    thermo = 'O2s-(Cds-Cd)(Cds-Cd)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2034,
    label = "O2s-Ct(Cds-Cd)",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cd  u0 {1,S} {4,D}
3   Ct  u0 {1,S}
4   C   u0 {2,D}
""",
    thermo = 'O2s-(Cds-Cd)(Cds-Cd)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2035,
    label = "O2s-CtCs",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Ct  u0 {1,S}
3   Cs  u0 {1,S}
""",
    thermo = 'O2s-Cs(Cds-Cd)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2036,
    label = "O2s-Cs(CtN3t)",
    group = 
"""
1 * O2s u0 {2,S} {4,S}
2   Ct  u0 {1,S} {3,T}
3   N3t u0 {2,T}
4   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.1,9.8,10.6,11.2,12.3,13,13.8],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (10,'kcal/mol','+|-',1.3),
        S298 = (39.1,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2037,
    label = "O2s-CtCb",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Ct  u0 {1,S}
3   Cb  u0 {1,S}
""",
    thermo = 'O2s-(Cds-Cd)(Cds-Cd)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2038,
    label = "O2s-CdsCds",
    group = 
"""
1 * O2s     u0 {2,S} {3,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
""",
    thermo = 'O2s-(Cds-Cd)(Cds-Cd)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2039,
    label = "O2s-(Cds-O2d)(Cds-O2d)",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   CO  u0 {1,S} {4,D}
3   CO  u0 {1,S} {5,D}
4   O2d u0 {2,D}
5   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.4,11.55,6.97,3.72,-0.53,-2.57,-1.41],'J/(mol*K)','+|-',[6.51,6.51,6.51,6.51,6.51,6.51,6.51]),
        H298 = (-46.4,'kJ/mol','+|-',5.54),
        S298 = (80.8,'J/(mol*K)','+|-',7.59),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 2040,
    label = "O2s-(Cds-O2d)(Cds-Cd)",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   CO  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {4,D}
4   C   u0 {3,D}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.02,19.61,18.5,17.71,17.02,16.49,15.33],'J/(mol*K)','+|-',[8.17,8.17,8.17,8.17,8.17,8.17,8.17]),
        H298 = (-100.6,'kJ/mol','+|-',6.96),
        S298 = (38.43,'J/(mol*K)','+|-',9.53),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 2041,
    label = "O2s-(Cds-Cd)(Cds-Cd)",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cd  u0 {1,S}
3   Cd  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.4,3.7,3.7,3.8,4.4,4.6,4.8],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-19.61,'kcal/mol','+|-',0.19),
        S298 = (10,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = """O-CdCd BOZZELLI""",
    longDesc = 
"""

""",
)

entry(
    index = 2042,
    label = "O2s-CdsCs",
    group = 
"""
1 * O2s     u0 {2,S} {3,S}
2   [Cd,CO] u0 {1,S}
3   Cs      u0 {1,S}
""",
    thermo = 'O2s-Cs(Cds-Cd)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2043,
    label = "O2s-Cs(Cds-O2d)",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   CO  u0 {1,S} {4,D}
3   Cs  u0 {1,S}
4   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.49,9.94,9.96,10.7,12.71,14.71,18],'J/(mol*K)','+|-',[3.15,3.15,3.15,3.15,3.15,3.15,3.15]),
        H298 = (-102.2,'kJ/mol','+|-',2.69),
        S298 = (45.71,'J/(mol*K)','+|-',3.68),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 2044,
    label = "O2s-Cs(Cds-Cd)",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cd  u0 {1,S} {4,D}
3   Cs  u0 {1,S}
4   C   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19.07,23.32,25.26,25.92,25.5,24.52,22.72],'J/(mol*K)','+|-',[3.47,3.47,3.47,3.47,3.47,3.47,3.47]),
        H298 = (-123.9,'kJ/mol','+|-',2.96),
        S298 = (18.91,'J/(mol*K)','+|-',4.05),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 2045,
    label = "O2s-CdsCb",
    group = 
"""
1 * O2s     u0 {2,S} {3,S}
2   [Cd,CO] u0 {1,S}
3   Cb      u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2046,
    label = "O2s-Cb(Cds-O2d)",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   CO  u0 {1,S} {4,D}
3   Cb  u0 {1,S}
4   O2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2047,
    label = "O2s-Cb(Cds-Cd)",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cd  u0 {1,S} {4,D}
3   Cb  u0 {1,S}
4   C   u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2048,
    label = "O2s-CsCs",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.7,13.4,13.58,14.54,16.71,18.29,20.17],'J/(mol*K)','+|-',[2.44,2.44,2.44,2.44,2.44,2.44,2.44]),
        H298 = (-98.6,'kJ/mol','+|-',2.08),
        S298 = (38.61,'J/(mol*K)','+|-',2.85),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 2049,
    label = "O2s-CsCb",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cs  u0 {1,S}
3   Cb  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.4,3.7,3.7,3.8,4.4,4.6,4.6],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-22.6,'kcal/mol','+|-',0.19),
        S298 = (9.7,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = """O-CbCs REID, PRAUSNITZ and SHERWOOD !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
"""

""",
)

entry(
    index = 2050,
    label = "O2s-CbCb",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cb  u0 {1,S}
3   Cb  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.19,-0.24,-0.72,-0.51,0.43,1.36,1.75],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-18.77,'kcal/mol','+|-',0.19),
        S298 = (13.59,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = """O-CbCb CHERN 1/97 Hf PEDLEY, Mopac""",
    longDesc = 
"""

""",
)

entry(
    index = 2051,
    label = "O2s-Cs(Cds-S2d)",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cs  u0 {1,S}
3   CS  u0 {1,S} {4,D}
4   S2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.05,1.22,1.84,2.44,3.31,3.94,4.86],'cal/(mol*K)'),
        H298 = (-30.58,'kcal/mol'),
        S298 = (5.73,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""

""",
)

entry(
    index = 2052,
    label = "O2s-CS",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   S   ux {1,S}
3   C   ux {1,S}
""",
    thermo = 'O2s-CS4',
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2053,
    label = "O2s-CS2",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   S2s ux {1,S}
3   Cs  ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.78,3.48,3.83,4.16,5.02,5.4,5.86],'cal/(mol*K)'),
        H298 = (-22.57,'kcal/mol'),
        S298 = (7.17,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2054,
    label = "O2s-CS4",
    group = 
"""
1 * O2s               u0 {2,S} {3,S}
2   [S4s,S4d,S4b,S4t] ux {1,S}
3   C                 ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.73,1.7,1.94,2.26,3.23,3.84,4.43],'cal/(mol*K)'),
        H298 = (-22.17,'kcal/mol'),
        S298 = (10.56,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2055,
    label = "O2s-CS6",
    group = 
"""
1 * O2s                     u0 {2,S} {3,S}
2   [S6s,S6d,S6dd,S6t,S6td] ux {1,S}
3   C                       ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.4,2.24,2.31,2.47,3.22,3.56,3.99],'cal/(mol*K)'),
        H298 = (-23.77,'kcal/mol'),
        S298 = (10.68,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2056,
    label = "O2s-SH",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   S   ux {1,S}
3   H   ux {1,S}
""",
    thermo = 'O2s-S_nonDeH',
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2057,
    label = "O2s-S_nonDeH",
    group = 
"""
1 * O2s           u0 {2,S} {3,S}
2   [S2s,S4s,S6s] ux {1,S}
3   H             ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.88,4.91,5.45,5.86,6.66,7.13,7.81],'cal/(mol*K)'),
        H298 = (-36.34,'kcal/mol'),
        S298 = (29.09,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2058,
    label = "O2s-S_DeH",
    group = 
"""
1 * O2s            u0 {2,S} {3,S}
2   [S4d,S6d,S6dd] ux {1,S}
3   H              ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.89,4.41,4.73,4.97,5.74,6.3,7.25],'cal/(mol*K)'),
        H298 = (-37.92,'kcal/mol'),
        S298 = (30,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2059,
    label = "Si",
    group = 
"""
1 * Si u0
""",
    thermo = 'Cs-HHHH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2060,
    label = "SiJ2(S)",
    group = 
"""
1 * Si u0 p1
""",
    thermo = 'CJ2_singlet',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2061,
    label = "S",
    group = 
"""
1 * S ux
""",
    thermo = 'S2s-CsCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2062,
    label = "Sc",
    group = 
"""
1 * S ux c+1
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5,5,5,5,5,5,5],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (200,'kcal/mol','+|-',1),
        S298 = (20,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = """Knocks out charged thermo""",
    longDesc = 
"""

""",
)

entry(
    index = 2063,
    label = "Sa(S)",
    group = 
"""
1 * S u0 p3 c0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.97,4.97,4.97,4.97,4.97,5.13,5.06],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (66.2,'kcal/mol','+|-',1),
        S298 = (40.11,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = """SulfurLibrary""",
    longDesc = 
"""
H298, S298, Cp1000, Cp1500 from [10], rest from AGV
Singlet sulfur, thermo data copied from triplet sulfur, likely very incorrect (taken from SulfurLibrary).
""",
)

entry(
    index = 2064,
    label = "S2d",
    group = 
"""
1 * S2d u0
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2065,
    label = "S2d-C",
    group = 
"""
1 * S2d u0 {2,D}
2   C   u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 2066,
    label = "S2d-S",
    group = 
"""
1 * S2d u0 {2,D}
2   S   u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.99,7.45,7,6.93,7.48,7.75,8.1],'cal/(mol*K)'),
        H298 = (4.59,'kcal/mol'),
        S298 = (54.27,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""

""",
)

entry(
    index = 2067,
    label = "S2d-O",
    group = 
"""
1 * S2d u0 {2,D}
2   O   u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.27,7.55,7.84,8.08,8.39,8.57,8.77],'cal/(mol*K)'),
        H298 = (0.26,'kcal/mol'),
        S298 = (50.87,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""

""",
)

entry(
    index = 2068,
    label = "S2s",
    group = 
"""
1 * S2s u0
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2069,
    label = "S2s-HH",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   H   u0 {1,S}
3   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.15,8.48,8.84,9.25,10.09,10.83,12.09],'cal/(mol*K)'),
        H298 = (-5.38,'kcal/mol'),
        S298 = (50.53,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2070,
    label = "S2s-CH",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   C   u0 {1,S}
3   H   u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2071,
    label = "S2s-CsH",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cs  u0 {1,S}
3   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.73,5.21,5.55,5.8,4.98,4.87,7.06],'cal/(mol*K)'),
        H298 = (-7.93,'kcal/mol'),
        S298 = (28.75,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2072,
    label = "S2s-CdH",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cd  u0 {1,S}
3   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.59,5.16,6.11,6.73,6.25,6.14,8.62],'cal/(mol*K)'),
        H298 = (-6.3,'kcal/mol'),
        S298 = (27.69,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2073,
    label = "S2s-CtH",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Ct  u0 {1,S}
3   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.77,7.04,8.31,8.95,8.11,7.62,9.5],'cal/(mol*K)'),
        H298 = (-11.24,'kcal/mol'),
        S298 = (23.31,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2074,
    label = "S2s-CbH",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cb  u0 {1,S}
3   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.15,6.51,7.79,8.49,7.74,7.43,9.83],'cal/(mol*K)'),
        H298 = (-8.34,'kcal/mol'),
        S298 = (24.34,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2075,
    label = "S2s-(C=O)H",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   CO  u0 {1,S} {4,D}
3   H   u0 {1,S}
4   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.37,5.5,6.36,7.04,6.91,6.85,8.81],'cal/(mol*K)'),
        H298 = (-15.61,'kcal/mol'),
        S298 = (23.19,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2076,
    label = "S2s-(C=S2d)H",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   CS  u0 {1,S} {4,D}
3   H   u0 {1,S}
4   S2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.59,5.99,7.09,7.59,6.62,6.19,8.26],'cal/(mol*K)'),
        H298 = (-4.41,'kcal/mol'),
        S298 = (27.28,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2077,
    label = "S2s-SH",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   S   ux {1,S}
3   H   u0 {1,S}
""",
    thermo = 'S2s-S2sH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2078,
    label = "S2s-S2sH",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   S2s u0 {1,S}
3   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.8,6.58,7.13,7.49,8,8.38,8.96],'cal/(mol*K)'),
        H298 = (2.4,'kcal/mol'),
        S298 = (32.51,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2079,
    label = "S2s-S_DeH",
    group = 
"""
1 * S2s            u0 {2,S} {3,S}
2   [S4d,S6d,S6dd] u0 {1,S}
3   H              u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.29,6.86,6.95,7.35,7.78,8.09,8.5],'cal/(mol*K)'),
        H298 = (1.99,'kcal/mol'),
        S298 = (28.52,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2080,
    label = "S2s-SS",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   S   ux {1,S}
3   S   ux {1,S}
""",
    thermo = 'S2s-SsSs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2081,
    label = "S2s-SsSs",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   S2s u0 {1,S}
3   S2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.26,6.39,6.35,6.52,6.64,6.58,6.03],'cal/(mol*K)'),
        H298 = (1.76,'kcal/mol'),
        S298 = (9.13,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2082,
    label = "S2s-SO",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   S   ux {1,S}
3   O   ux {1,S}
""",
    thermo = 'S2s-S2O',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2083,
    label = "S2s-S2O",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   S2s ux {1,S}
3   O   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.98,6.87,6.93,6.96,6.69,6.54,5.98],'cal/(mol*K)'),
        H298 = (5,'kcal/mol'),
        S298 = (10.55,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""

""",
)

entry(
    index = 2084,
    label = "S2s-S4O",
    group = 
"""
1 * S2s               u0 {2,S} {3,S}
2   [S4s,S4d,S4b,S4t] ux {1,S}
3   O                 ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.61,7.25,7.18,7.84,7.92,7.81,7.13],'cal/(mol*K)'),
        H298 = (6.05,'kcal/mol'),
        S298 = (5.79,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""

""",
)

entry(
    index = 2085,
    label = "S2s-S6O",
    group = 
"""
1 * S2s                     u0 {2,S} {3,S}
2   [S6s,S6d,S6dd,S6t,S6td] ux {1,S}
3   O                       ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.91,8.77,9.05,9.21,9.05,8.65,6.9],'cal/(mol*K)'),
        H298 = (4.43,'kcal/mol'),
        S298 = (0.9,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""

""",
)

entry(
    index = 2086,
    label = "S2s-SC",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   S   ux {1,S}
3   C   ux {1,S}
""",
    thermo = 'S2s-S2sC',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2087,
    label = "S2s-S2sC",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   S2s u0 {1,S}
3   C   u0 {1,S}
""",
    thermo = 'S2s-S2sCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2088,
    label = "S2s-S2sCs",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   S2s u0 {1,S}
3   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.97,4.54,4.79,4.86,3.65,3.01,4.31],'cal/(mol*K)'),
        H298 = (-5.11,'kcal/mol'),
        S298 = (6.93,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2089,
    label = "S2s-S2sCd",
    group = 
"""
1 * S2s        u0 {2,S} {3,S}
2   S2s        u0 {1,S}
3   [Cd,CO,CS] u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.7,4.33,5.07,5.44,4.22,3.51,4.92],'cal/(mol*K)'),
        H298 = (-1.95,'kcal/mol'),
        S298 = (7.45,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2090,
    label = "S2s-S2sCt",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   S2s u0 {1,S}
3   Ct  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.79,5.99,7.05,7.43,6.04,5.03,6.05],'cal/(mol*K)'),
        H298 = (-4.98,'kcal/mol'),
        S298 = (4.54,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2091,
    label = "S2s-S2sCb",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   S2s u0 {1,S}
3   Cb  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.16,5.6,6.38,6.83,5.95,5.19,6.4],'cal/(mol*K)'),
        H298 = (-8.28,'kcal/mol'),
        S298 = (4.18,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2092,
    label = "S2s-S46C",
    group = 
"""
1 * S2s                                 u0 {2,S} {3,S}
2   [S4s,S4d,S4b,S4t,S6d,S6dd,S6t,S6td] u0 {1,S}
3   C                                   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.13,4.53,4.39,4.58,3.29,2.61,4.05],'cal/(mol*K)'),
        H298 = (-6.87,'kcal/mol'),
        S298 = (5.39,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""

""",
)

entry(
    index = 2093,
    label = "S2s-CC",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2094,
    label = "S2s-CsCs",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.08,3.18,3.6,3.63,1.11,-0.35,2.47],'cal/(mol*K)'),
        H298 = (-12.89,'kcal/mol'),
        S298 = (1.98,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2095,
    label = "S2s-CsCd",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cs  u0 {1,S}
3   Cd  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.39,4.01,4.68,4.86,2.31,0.98,4.01],'cal/(mol*K)'),
        H298 = (-12.92,'kcal/mol'),
        S298 = (1.68,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2096,
    label = "S2s-Cs(C=O)",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cs  u0 {1,S}
3   CO  u0 {1,S} {4,D}
4   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.59,1.97,3.07,3.92,2.65,1.84,4.64],'cal/(mol*K)'),
        H298 = (-23.07,'kcal/mol'),
        S298 = (-5.22,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2097,
    label = "S2s-CsCt",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cs  u0 {1,S}
3   Ct  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.28,4.58,5.7,6.11,3.57,2.07,4.79],'cal/(mol*K)'),
        H298 = (-17.69,'kcal/mol'),
        S298 = (-0.51,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2098,
    label = "S2s-CsCb",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cs  u0 {1,S}
3   Cb  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.39,3.88,5.06,5.54,3.13,1.85,5.1],'cal/(mol*K)'),
        H298 = (-13.96,'kcal/mol'),
        S298 = (-0.49,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2099,
    label = "S2s-CdCd",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cd  u0 {1,S}
3   Cd  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.84,3.28,4.52,5.08,2.91,1.76,5.17],'cal/(mol*K)'),
        H298 = (-10,'kcal/mol'),
        S298 = (3.65,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2100,
    label = "S2s-CdCt",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cd  u0 {1,S}
3   Ct  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.35,4.54,6.16,6.8,4.41,2.93,5.43],'cal/(mol*K)'),
        H298 = (-14.92,'kcal/mol'),
        S298 = (-0.53,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2101,
    label = "S2s-CdCb",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cd  u0 {1,S}
3   Cb  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.19,4.37,5.99,6.68,4.42,3.05,6.26],'cal/(mol*K)'),
        H298 = (-13,'kcal/mol'),
        S298 = (0.31,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2102,
    label = "S2s-CtCt",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Ct  u0 {1,S}
3   Ct  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.62,8.35,10.97,12.26,10.43,9.14,12.23],'cal/(mol*K)'),
        H298 = (1.21,'kcal/mol'),
        S298 = (0.47,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2103,
    label = "S2s-CtCb",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Ct  u0 {1,S}
3   Cb  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.83,5.58,7.44,8.2,5.74,4.15,7.1],'cal/(mol*K)'),
        H298 = (-16.99,'kcal/mol'),
        S298 = (-3.81,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2104,
    label = "S2s-CbCb",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cb  u0 {1,S}
3   Cb  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.85,4.81,6.83,7.67,5.37,3.9,6.97],'cal/(mol*K)'),
        H298 = (-15.35,'kcal/mol'),
        S298 = (-2.38,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2105,
    label = "S2s-(C=S2d)Cs",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cs  u0 {1,S}
3   CS  u0 {1,S} {4,D}
4   S2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.04,2.62,3.94,4.57,2.28,1,3.93],'cal/(mol*K)'),
        H298 = (-13.74,'kcal/mol'),
        S298 = (2.06,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2106,
    label = "S2s-(C=S2d)(C=S2d)",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   CS  u0 {1,S} {4,D}
3   CS  u0 {1,S} {5,D}
4   S2d u0 {2,D}
5   S2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.02,3.44,5.09,5.96,3.79,2.41,4.8],'cal/(mol*K)'),
        H298 = (-4.19,'kcal/mol'),
        S298 = (3.36,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2107,
    label = "S2s-(C=S2d)Cmb",
    group = 
"""
1 * S2s           u0 {2,S} {3,S}
2   [Cd,Cb,Ct,CO] u0 {1,S}
3   CS            u0 {1,S} {4,D}
4   S2d           u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.39,4.13,5.9,6.62,4.15,2.64,5.52],'cal/(mol*K)'),
        H298 = (-10.72,'kcal/mol'),
        S298 = (0.91,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2108,
    label = "S2s-OH",
    group = 
"""
1 * S2s u0 p2 {2,S} {3,S}
2   O   ux {1,S}
3   H   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.22,7.55,7.83,8.08,8.24,8.46,8.72],'cal/(mol*K)'),
        H298 = (9.67,'kcal/mol'),
        S298 = (30.8,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2109,
    label = "S2s-OO",
    group = 
"""
1 * S2s u0 p2 {2,S} {3,S}
2   O   ux {1,S}
3   O   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.28,7.69,8.3,8.61,8.32,8.04,7.13],'cal/(mol*K)'),
        H298 = (6.03,'kcal/mol'),
        S298 = (8.53,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2110,
    label = "S2s-OC",
    group = 
"""
1 * S2s u0 p2 {2,S} {3,S}
2   O   ux {1,S}
3   C   ux {1,S}
""",
    thermo = 'S2s-OCs',
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2111,
    label = "S2s-OCs",
    group = 
"""
1 * S2s u0 p2 {2,S} {3,S}
2   O   ux {1,S}
3   Cs  ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.26,5.46,5.62,5.65,4.15,3.34,4.29],'cal/(mol*K)'),
        H298 = (-0.85,'kcal/mol'),
        S298 = (6.38,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2112,
    label = "S4dd",
    group = 
"""
1 * S4dd u0
""",
    thermo = 'S4dd-OdOd',
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2113,
    label = "S4dd-OdOd",
    group = 
"""
1 * S4dd u0 p1 {2,D} {3,D}
2   O2d  ux p2 {1,D}
3   O2d  ux p2 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.57,10.44,11.16,11.7,12.44,12.92,13.45],'cal/(mol*K)'),
        H298 = (-71.22,'kcal/mol'),
        S298 = (60.73,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2114,
    label = "S4dd-CdOd",
    group = 
"""
1 * S4dd u0 p1 {2,D} {3,D}
2   C    ux {1,D}
3   O2d  ux {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.64,4.67,5.46,5.81,5.99,6.04,6.34],'cal/(mol*K)'),
        H298 = (-24.69,'kcal/mol'),
        S298 = (4.78,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2115,
    label = "S4dd-CdCd",
    group = 
"""
1 * S4dd u0 p1 {2,D} {3,D}
2   C    ux {1,D}
3   C    ux {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.54,-0.74,0.01,0.11,-0.46,-0.94,-0.92],'cal/(mol*K)'),
        H298 = (21.12,'kcal/mol'),
        S298 = (-51.68,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2116,
    label = "S4dd-OdSd",
    group = 
"""
1 * S4dd u0 p1 {2,D} {3,D}
2   O    ux {1,D}
3   S    ux {1,D}
""",
    thermo = 'S4dd-OdS4d',
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2117,
    label = "S4dd-OdS4d",
    group = 
"""
1 * S4dd       u0 p1 {2,D} {3,D}
2   O          ux {1,D}
3   [S4d,S4dd] ux {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.65,7.66,9.29,10.12,10.39,10.88,10.49],'cal/(mol*K)'),
        H298 = (-4.33,'kcal/mol'),
        S298 = (24.93,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2118,
    label = "S4dd-OdS6d",
    group = 
"""
1 * S4dd                  u0 p1 {2,D} {3,D}
2   O                     ux {1,D}
3   [S6d,S6dd,S6ddd,S6td] ux {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.95,12.32,11.99,12.11,12.88,13.34,13.96],'cal/(mol*K)'),
        H298 = (-14.29,'kcal/mol'),
        S298 = (63.4,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2119,
    label = "S4dd-SdCd",
    group = 
"""
1 * S4dd u0 p1 {2,D} {3,D}
2   C    ux {1,D}
3   S    ux {1,D}
""",
    thermo = 'S4dd-S46dCd',
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2120,
    label = "S4dd-S2dCd",
    group = 
"""
1 * S4dd u0 p1 {2,D} {3,D}
2   C    ux {1,D}
3   S2d  ux {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.07,-1.49,-1.34,-1.37,-1.46,-1.6,-2.06],'cal/(mol*K)'),
        H298 = (-1.36,'kcal/mol'),
        S298 = (-49.24,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2121,
    label = "S4dd-S46dCd",
    group = 
"""
1 * S4dd                           u0 p1 {2,D} {3,D}
2   C                              ux {1,D}
3   [S4d,S4dd,S6d,S6dd,S6ddd,S6td] ux {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.65,7.45,7.16,7.17,7.22,6.89,6.86],'cal/(mol*K)'),
        H298 = (0.95,'kcal/mol'),
        S298 = (13.93,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2122,
    label = "S4d",
    group = 
"""
1 * S4d u0
""",
    thermo = 'S4d-Od',
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2123,
    label = "S4d-Od",
    group = 
"""
1 * S4d u0 p1 {2,D}
2   O2d ux {1,D}
""",
    thermo = 'S4d-OdCC',
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2124,
    label = "S4d-OdHH",
    group = 
"""
1 * S4d u0 p1 {2,D} {3,S} {4,S}
2   O2d ux {1,D}
3   H   ux {1,S}
4   H   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.94,4.77,5.73,6.51,7.67,8.38,9.3],'cal/(mol*K)'),
        H298 = (21.19,'kcal/mol'),
        S298 = (39.44,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2125,
    label = "S4d-OdCC",
    group = 
"""
1 * S4d u0 p1 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   C   ux {1,S}
4   C   ux {1,S}
""",
    thermo = 'S4d-OdCsCs',
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
Inferred from a least squares fit from 40 species mostly calculated at cbsqb3, 4/2017, Ryan Gillis
""",
)

entry(
    index = 2126,
    label = "S4d-OdCsCs",
    group = 
"""
1 * S4d u0 p1 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cs  ux {1,S}
4   Cs  ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.65,11.72,12.66,12.81,9.35,7.25,8.64],'cal/(mol*K)'),
        H298 = (-47.94,'kcal/mol'),
        S298 = (9.7,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2127,
    label = "S4d-OdCdCd",
    group = 
"""
1 * S4d u0 p1 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cd  ux {1,S}
4   Cd  ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.82,7.03,9.56,9.62,7.29,6.09,9.27],'cal/(mol*K)'),
        H298 = (-53.32,'kcal/mol'),
        S298 = (17.34,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2128,
    label = "S4d-OdCH",
    group = 
"""
1 * S4d u0 p1 {2,D} {3,S} {4,S}
2   O2d ux {1,D}
3   C   ux {1,S}
4   H   ux {1,S}
""",
    thermo = 'S4d-OdCsH',
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
Inferred from a least squares fit from 40 species mostly calculated at cbsqb3, 4/2017, Ryan Gillis
""",
)

entry(
    index = 2129,
    label = "S4d-OdCsH",
    group = 
"""
1 * S4d u0 p1 {2,D} {3,S} {4,S}
2   O2d ux {1,D}
3   Cs  ux {1,S}
4   H   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.79,10.53,12.04,12.87,12.36,12.08,13.59],'cal/(mol*K)'),
        H298 = (-27.22,'kcal/mol'),
        S298 = (31.86,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2130,
    label = "S4d-OdCdH",
    group = 
"""
1 * S4d u0 p1 {2,D} {3,S} {4,S}
2   O2d ux {1,D}
3   Cd  ux {1,S}
4   H   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.55,9.7,11.89,12.33,11.69,11.45,13.54],'cal/(mol*K)'),
        H298 = (-31.31,'kcal/mol'),
        S298 = (37.66,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2131,
    label = "S4d-OdCS",
    group = 
"""
1 * S4d u0 p1 {2,D} {3,S} {4,S}
2   O2d ux {1,D}
3   C   ux {1,S}
4   S   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.59,10.13,11.04,11.14,9.76,8.95,10.26],'cal/(mol*K)'),
        H298 = (-33.31,'kcal/mol'),
        S298 = (16.13,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2132,
    label = "S4d-OdCO",
    group = 
"""
1 * S4d u0 p1 {2,D} {3,S} {4,S}
2   O2d ux {1,D}
3   C   ux {1,S}
4   O   ux {1,S}
""",
    thermo = 'S4d-OdOsCs',
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2133,
    label = "S4d-OdOsCs",
    group = 
"""
1 * S4d u0 p1 {2,D} {3,S} {4,S}
2   O2d ux {1,D}
3   Cs  ux {1,S}
4   O   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.03,12.12,12.87,13.15,11.23,10.02,10.49],'cal/(mol*K)'),
        H298 = (-46.79,'kcal/mol'),
        S298 = (12.6,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2134,
    label = "S4d-OdOsCd",
    group = 
"""
1 * S4d u0 p1 {2,D} {3,S} {4,S}
2   O2d ux {1,D}
3   Cd  ux {1,S}
4   O   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.15,9.65,11.36,11.59,10.33,9.63,10.88],'cal/(mol*K)'),
        H298 = (-48.07,'kcal/mol'),
        S298 = (15.92,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2135,
    label = "S4d-OdOO",
    group = 
"""
1 * S4d u0 p1 {2,D} {3,S} {4,S}
2   O2d ux {1,D}
3   O   ux {1,S}
4   O   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.02,13.07,13.64,13.98,13.71,13.43,12.62],'cal/(mol*K)'),
        H298 = (-50.32,'kcal/mol'),
        S298 = (10.96,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2136,
    label = "S4d-OdOH",
    group = 
"""
1 * S4d u0 p1 {2,D} {3,S} {4,S}
2   O2d ux {1,D}
3   O   ux {1,S}
4   H   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.93,12.17,12.99,13.57,14.11,14.5,14.89],'cal/(mol*K)'),
        H298 = (-25.38,'kcal/mol'),
        S298 = (35.22,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2137,
    label = "S4d-OdOS",
    group = 
"""
1 * S4d u0 p1 {2,D} {3,S} {4,S}
2   O2d ux {1,D}
3   O   ux {1,S}
4   S   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.86,12.2,13.01,13.23,13.15,12.93,12.03],'cal/(mol*K)'),
        H298 = (-29.87,'kcal/mol'),
        S298 = (17.5,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2138,
    label = "S4d-OdSS",
    group = 
"""
1 * S4d u0 p1 {2,D} {3,S} {4,S}
2   O2d ux {1,D}
3   S   ux {1,S}
4   S   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.82,10.07,10.6,10.43,10.54,10.66,10.61],'cal/(mol*K)'),
        H298 = (-17.88,'kcal/mol'),
        S298 = (23.27,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2139,
    label = "S4d-OdSH",
    group = 
"""
1 * S4d u0 p1 {2,D} {3,S} {4,S}
2   O2d ux {1,D}
3   S   ux {1,S}
4   H   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.11,10.24,11.59,11.97,13.17,13.96,14.81],'cal/(mol*K)'),
        H298 = (-13.85,'kcal/mol'),
        S298 = (39.74,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2140,
    label = "S4d-Cd",
    group = 
"""
1 * S4d u0 p1 {2,D}
2   C   ux {1,D}
""",
    thermo = 'S4d-CdCC',
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2141,
    label = "S4d-CdCC",
    group = 
"""
1 * S4d u0 p1 {2,D} {3,S} {4,S}
2   C   ux {1,D}
3   C   ux {1,S}
4   C   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.87,5.65,6.38,6.77,6.73,6.63,6.95],'cal/(mol*K)'),
        H298 = (27.48,'kcal/mol'),
        S298 = (-29.43,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2142,
    label = "S4d-CdCH",
    group = 
"""
1 * S4d u0 p1 {2,D} {3,S} {4,S}
2   C   ux {1,D}
3   C   ux {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.64,5.68,6.69,7.14,5.62,4.77,6.37],'cal/(mol*K)'),
        H298 = (25.84,'kcal/mol'),
        S298 = (-20.06,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2143,
    label = "S4d-CdHH",
    group = 
"""
1 * S4d u0 p1 {2,D} {3,S} {4,S}
2   C   ux {1,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.33,3.4,4.62,5.47,6.49,7.25,8.78],'cal/(mol*K)'),
        H298 = (42.16,'kcal/mol'),
        S298 = (1.02,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2144,
    label = "S4d-CdOC",
    group = 
"""
1 * S4d u0 p1 {2,D} {3,S} {4,S}
2   C   ux {1,D}
3   O   ux {1,S}
4   C   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.83,6.25,6.67,6.58,3.83,2.18,2.8],'cal/(mol*K)'),
        H298 = (8.84,'kcal/mol'),
        S298 = (-41.43,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2145,
    label = "S4d-CdOH",
    group = 
"""
1 * S4d u0 p1 {2,D} {3,S} {4,S}
2   C   ux {1,D}
3   O   ux {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.49,5.71,6.73,7.26,7.26,7.27,7.72],'cal/(mol*K)'),
        H298 = (22.11,'kcal/mol'),
        S298 = (-18.81,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2146,
    label = "S4d-Sd",
    group = 
"""
1 * S4d u0 p1 {2,D}
2   S   ux {1,D}
""",
    thermo = 'S4d-SdOC',
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2147,
    label = "S4d-SdOC",
    group = 
"""
1 * S4d u0 p1 {2,D} {3,S} {4,S}
2   S   ux {1,D}
3   O   ux {1,S}
4   C   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.73,5.08,6.27,6.72,4.37,2.93,3.02],'cal/(mol*K)'),
        H298 = (-0.53,'kcal/mol'),
        S298 = (-38.29,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2148,
    label = "S4d-SdOH",
    group = 
"""
1 * S4d u0 p1 {2,D} {3,S} {4,S}
2   S   ux {1,D}
3   O   ux {1,S}
4   H   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.25,7.29,8.38,8.82,8.27,7.9,7.26],'cal/(mol*K)'),
        H298 = (18.23,'kcal/mol'),
        S298 = (-16.74,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2149,
    label = "S4d-SdCH",
    group = 
"""
1 * S4d u0 p1 {2,D} {3,S} {4,S}
2   S   ux {1,D}
3   H   ux {1,S}
4   C   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.75,8.55,8.19,7.43,6.36,5.7,8.6],'cal/(mol*K)'),
        H298 = (-2.01,'kcal/mol'),
        S298 = (24.87,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2150,
    label = "S4d-SdSC",
    group = 
"""
1 * S4d u0 p1 {2,D} {3,S} {4,S}
2   S   ux {1,D}
3   S   ux {1,S}
4   C   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.2,5.12,5.01,4.82,1.87,0.29,1.16],'cal/(mol*K)'),
        H298 = (1.85,'kcal/mol'),
        S298 = (-36.46,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2151,
    label = "S4s",
    group = 
"""
1 * S4s u0
""",
    thermo = 'S4s-CCCH',
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
Couldn't converge these geometries to calculate values and so I copied the S6s values that seem similarly unfavorable
""",
)

entry(
    index = 2152,
    label = "S4s-OCCH",
    group = 
"""
1 * S4s u0 p1 {2,S} {3,S} {4,S} {5,S}
2   O   ux {1,S}
3   C   ux {1,S}
4   C   ux {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.58,11.43,12.51,13.49,14.96,15.33,16.12],'cal/(mol*K)'),
        H298 = (45.75,'kcal/mol'),
        S298 = (-21.17,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2153,
    label = "S4s-CCCH",
    group = 
"""
1 * S4s u0 p1 {2,S} {3,S} {4,S} {5,S}
2   C   ux {1,S}
3   C   ux {1,S}
4   C   ux {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.51,12.57,13.68,14.04,14.27,14.27,13.38],'cal/(mol*K)'),
        H298 = (29.21,'kcal/mol'),
        S298 = (-10.57,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2154,
    label = "S4s-OOCC",
    group = 
"""
1 * S4s u0 p1 {2,S} {3,S} {4,S} {5,S}
2   O   ux {1,S}
3   O   ux {1,S}
4   C   ux {1,S}
5   C   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.68,10.98,11.54,12.28,13.55,13.51,13.81],'cal/(mol*K)'),
        H298 = (7.83,'kcal/mol'),
        S298 = (-46.41,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2155,
    label = "S4s-SOCH",
    group = 
"""
1 * S4s u0 p1 {2,S} {3,S} {4,S} {5,S}
2   S   ux {1,S}
3   O   ux {1,S}
4   C   ux {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.55,13.48,13.14,13.2,11.78,10.9,11.16],'cal/(mol*K)'),
        H298 = (12.88,'kcal/mol'),
        S298 = (-10.63,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2156,
    label = "S4s-SOOH",
    group = 
"""
1 * S4s u0 p1 {2,S} {3,S} {4,S} {5,S}
2   S   ux {1,S}
3   O   ux {1,S}
4   O   ux {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.68,10.98,11.54,12.28,13.55,13.51,13.81],'cal/(mol*K)'),
        H298 = (7.83,'kcal/mol'),
        S298 = (-46.41,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2157,
    label = "S4t",
    group = 
"""
1 * S4t u0
""",
    thermo = 'S4t-CtC',
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2158,
    label = "S4t-CtC",
    group = 
"""
1 * S4t u0 p1 {2,T} {3,S}
2   C   ux {1,T}
3   C   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.54,9.51,9.84,10.13,9.9,9.77,10.77],'cal/(mol*K)'),
        H298 = (-38.28,'kcal/mol'),
        S298 = (45.08,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2159,
    label = "S4t-CtH",
    group = 
"""
1 * S4t u0 p1 {2,T} {3,S}
2   C   ux {1,T}
3   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.17,10.15,10.6,11.21,13.36,14.74,15.51],'cal/(mol*K)'),
        H298 = (-24.12,'kcal/mol'),
        S298 = (66.64,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2160,
    label = "S4t-CtO",
    group = 
"""
1 * S4t u0 p1 {2,T} {3,S}
2   C   ux {1,T}
3   O   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.38,11.65,11.4,11.31,12.16,12.69,12.2],'cal/(mol*K)'),
        H298 = (-40.3,'kcal/mol'),
        S298 = (46.32,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2161,
    label = "S6s",
    group = 
"""
1 * S6s u0
""",
    thermo = 'S6s-CCCCCH',
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2162,
    label = "S6s-CCCCCH",
    group = 
"""
1 * S6s u0 p0 {2,S} {3,S} {4,S} {5,S} {6,S} {7,S}
2   C   ux {1,S}
3   C   ux {1,S}
4   C   ux {1,S}
5   C   ux {1,S}
6   C   ux {1,S}
7   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.46,12.07,12.63,12.69,7.76,5.42,10.58],'cal/(mol*K)'),
        H298 = (76.13,'kcal/mol'),
        S298 = (-111.16,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
Calculated at CBS-QB3, June 2017
""",
)

entry(
    index = 2163,
    label = "S6s-OCCCCH",
    group = 
"""
1 * S6s u0 p0 {2,S} {3,S} {4,S} {5,S} {6,S} {7,S}
2   O   ux {1,S}
3   C   ux {1,S}
4   C   ux {1,S}
5   C   ux {1,S}
6   C   ux {1,S}
7   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.12,12.36,12.67,12.71,8.75,7.04,11.45],'cal/(mol*K)'),
        H298 = (54.74,'kcal/mol'),
        S298 = (-90.21,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2164,
    label = "S6s-SOOCCH",
    group = 
"""
1 * S6s u0 p0 {2,S} {3,S} {4,S} {5,S} {6,S} {7,S}
2   S   ux {1,S}
3   O   ux {1,S}
4   O   ux {1,S}
5   C   ux {1,S}
6   C   ux {1,S}
7   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.67,11.03,11.69,12.23,10.78,10.53,14.25],'cal/(mol*K)'),
        H298 = (40.9,'kcal/mol'),
        S298 = (-66.41,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
Calculated at CBS-QB3, June 2017
""",
)

entry(
    index = 2165,
    label = "S6d",
    group = 
"""
1 * S6d u0
""",
    thermo = 'S6d-OdCCCH',
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2166,
    label = "S6d-OdOCCH",
    group = 
"""
1 * S6d u0 p0 {2,S} {3,S} {4,S} {5,D} {6,S}
2   O   ux {1,S}
3   C   ux {1,S}
4   C   ux {1,S}
5   O   ux {1,D}
6   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.7,13.05,14.45,15.56,14.84,14.71,17.5],'cal/(mol*K)'),
        H298 = (-5.1,'kcal/mol'),
        S298 = (-25.46,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2167,
    label = "S6d-OdCCCH",
    group = 
"""
1 * S6d u0 p0 {2,S} {3,S} {4,S} {5,D} {6,S}
2   C   ux {1,S}
3   C   ux {1,S}
4   C   ux {1,S}
5   O   ux {1,D}
6   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.79,8.88,10.35,11.48,13.31,14.04,14.47],'cal/(mol*K)'),
        H298 = (79.31,'kcal/mol'),
        S298 = (-37.87,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2168,
    label = "S6dd",
    group = 
"""
1 * S6dd u0
""",
    thermo = 'S6dd-OdOd',
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2169,
    label = "S6dd-OdOd",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
""",
    thermo = 'S6dd-OdOdCC',
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2170,
    label = "S6dd-OdOdHH",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
4   H    ux {1,S}
5   H    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.03,13.12,15.11,16.81,19.28,21,23.29],'cal/(mol*K)'),
        H298 = (-55.94,'kcal/mol'),
        S298 = (61.76,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2171,
    label = "S6dd-OdOdCC",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
4   C    ux {1,S}
5   C    ux {1,S}
""",
    thermo = 'S6dd-OdOdCsCs',
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
Inferred from a least squares fit from 40 species mostly calculated at cbsqb3, 4/2017, Ryan Gillis
""",
)

entry(
    index = 2172,
    label = "S6dd-OdOdCsCs",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
4   Cs   ux {1,S}
5   Cs   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.64,14.54,15,15.25,13.44,12.58,14.73],'cal/(mol*K)'),
        H298 = (-90,'kcal/mol'),
        S298 = (1.03,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2173,
    label = "S6dd-OdOdCdCd",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
4   Cd   ux {1,S}
5   Cd   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.34,14.68,15.09,15.34,13.41,12.49,14.85],'cal/(mol*K)'),
        H298 = (-87.32,'kcal/mol'),
        S298 = (5.39,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2174,
    label = "S6dd-OdOdCH",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
4   C    ux {1,S}
5   H    ux {1,S}
""",
    thermo = 'S6dd-OdOdCsH',
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
Inferred from a least squares fit from 40 species mostly calculated at cbsqb3, 4/2017, Ryan Gillis
""",
)

entry(
    index = 2175,
    label = "S6dd-OdOdCsH",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
4   Cs   ux {1,S}
5   H    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.64,13.86,15.05,15.97,16.14,16.47,18.79],'cal/(mol*K)'),
        H298 = (-74.06,'kcal/mol'),
        S298 = (32.2,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2176,
    label = "S6dd-OdOdCdH",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
4   Cd   ux {1,S}
5   H    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.09,13.45,14.58,15.49,15.79,16.26,18.8],'cal/(mol*K)'),
        H298 = (-69.95,'kcal/mol'),
        S298 = (34.66,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2177,
    label = "S6dd-OdOdCS",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
4   C    ux {1,S}
5   S    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.6,14.32,15.26,15.6,15.14,14.88,15.86],'cal/(mol*K)'),
        H298 = (-75.54,'kcal/mol'),
        S298 = (12.81,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2178,
    label = "S6dd-OdOdCO",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
4   C    ux {1,S}
5   O    ux {1,S}
""",
    thermo = 'S6dd-OdOdCsOs',
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
Inferred from a least squares fit from 40 species mostly calculated at cbsqb3, 4/2017, Ryan Gillis
""",
)

entry(
    index = 2179,
    label = "S6dd-OdOdCsOs",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
4   Cs   ux {1,S}
5   O    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.56,14.36,15.29,15.97,15.5,15.29,16.42],'cal/(mol*K)'),
        H298 = (-95.47,'kcal/mol'),
        S298 = (9.6,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2180,
    label = "S6dd-OdOdCdOs",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
4   Cd   ux {1,S}
5   O    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.37,14.34,15.19,15.88,15.36,15.15,16.38],'cal/(mol*K)'),
        H298 = (-94.3,'kcal/mol'),
        S298 = (11.82,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2181,
    label = "S6dd-OdOdOO",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
4   O    ux {1,S}
5   O    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.64,16.22,17.16,17.82,17.92,18.06,17.79],'cal/(mol*K)'),
        H298 = (-98.03,'kcal/mol'),
        S298 = (15.1,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2182,
    label = "S6dd-OdOdOH",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
4   O    ux {1,S}
5   H    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.97,13.8,15.36,16.73,18.83,19.72,20.78],'cal/(mol*K)'),
        H298 = (-79.78,'kcal/mol'),
        S298 = (40.9,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2183,
    label = "S6dd-OdOdOS",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
4   O    ux {1,S}
5   S    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.13,15.31,16.33,16.74,17.12,17.44,17.58],'cal/(mol*K)'),
        H298 = (-77.13,'kcal/mol'),
        S298 = (21.78,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2184,
    label = "S6dd-OdOdSS",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
4   S    ux {1,S}
5   S    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.66,14.99,15.99,15.76,15.89,16.31,16.71],'cal/(mol*K)'),
        H298 = (-60.04,'kcal/mol'),
        S298 = (24.66,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2185,
    label = "S6dd-OdOdSH",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
4   S    ux {1,S}
5   H    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.86,12.82,14.59,15.68,17.55,18.77,20.03],'cal/(mol*K)'),
        H298 = (-58.11,'kcal/mol'),
        S298 = (44.42,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2186,
    label = "S6dd-OdCd",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D}
2   O2d  u0 {1,D}
3   C    ux {1,D}
""",
    thermo = 'S6dd-OdCdCC',
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2187,
    label = "S6dd-OdCdCC",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  u0 {1,D}
3   C    ux {1,D}
4   C    ux {1,S}
5   C    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.65,7.93,8.24,8.33,6.87,6.07,7.56],'cal/(mol*K)'),
        H298 = (-3.53,'kcal/mol'),
        S298 = (-29.64,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2188,
    label = "S6dd-OdCdCH",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  u0 {1,D}
3   C    ux {1,D}
4   C    ux {1,S}
5   H    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.54,6.96,7.76,8.52,8.63,8.91,11.16],'cal/(mol*K)'),
        H298 = (0.76,'kcal/mol'),
        S298 = (-21.89,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2189,
    label = "S6dd-OdCdOC",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  u0 {1,D}
3   C    ux {1,D}
4   C    ux {1,S}
5   O    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.93,8.96,9.5,9.97,8.89,8.13,8.68],'cal/(mol*K)'),
        H298 = (-18.83,'kcal/mol'),
        S298 = (-44.17,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2190,
    label = "S6dd-OdCdOO",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  u0 {1,D}
3   C    ux {1,D}
4   O    ux {1,S}
5   O    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.83,11.13,11.78,12.17,11.47,11.11,10.34],'cal/(mol*K)'),
        H298 = (-23.6,'kcal/mol'),
        S298 = (-37.31,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2191,
    label = "S6dd-OdCdOH",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  u0 {1,D}
3   C    ux {1,D}
4   H    ux {1,S}
5   O    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.06,9.02,10.52,11.62,12.49,12.94,13.19],'cal/(mol*K)'),
        H298 = (-1.99,'kcal/mol'),
        S298 = (-13.94,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2192,
    label = "S6dd-OdCdSH",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  u0 {1,D}
3   C    ux {1,D}
4   H    ux {1,S}
5   S    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.1,7.25,8.55,9.3,10.38,11.06,12.03],'cal/(mol*K)'),
        H298 = (12.06,'kcal/mol'),
        S298 = (-5.77,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2193,
    label = "S6dd-OdCdOS",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  u0 {1,D}
3   C    ux {1,D}
4   S    ux {1,S}
5   O    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.12,8.63,9.14,9.39,9.28,9.17,9.38],'cal/(mol*K)'),
        H298 = (-4.86,'kcal/mol'),
        S298 = (-28.94,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2194,
    label = "S6dd-CdCd",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D}
2   C    ux {1,D}
3   C    ux {1,D}
""",
    thermo = 'S6dd-CdCdCC',
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2195,
    label = "S6dd-CdCdCC",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   C    ux {1,D}
3   C    ux {1,D}
4   C    ux {1,S}
5   C    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.87,1.85,1.58,1.37,-1.28,-2.78,-0.97],'cal/(mol*K)'),
        H298 = (57.75,'kcal/mol'),
        S298 = (-104.28,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2196,
    label = "S6dd-CdCdCH",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   C    ux {1,D}
3   C    ux {1,D}
4   C    ux {1,S}
5   H    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.08,0.58,1.26,1.83,1.41,1.26,3.2],'cal/(mol*K)'),
        H298 = (69.6,'kcal/mol'),
        S298 = (-73.49,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2197,
    label = "S6dd-CdCdOC",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   C    ux {1,D}
3   C    ux {1,D}
4   O    ux {1,S}
5   C    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.46,2.57,3.31,3.63,2.23,1.2,1.36],'cal/(mol*K)'),
        H298 = (46.88,'kcal/mol'),
        S298 = (-98.33,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2198,
    label = "S6dd-OdSd",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D}
2   O2d  u0 {1,D}
3   S    ux {1,D}
""",
    thermo = 'S6dd-OdSdOC',
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2199,
    label = "S6dd-OdSdOC",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  u0 {1,D}
3   S    ux {1,D}
4   C    ux {1,S}
5   O    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.38,10.01,11.28,11.7,10.06,9.15,9.07],'cal/(mol*K)'),
        H298 = (-36.41,'kcal/mol'),
        S298 = (-43.9,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2200,
    label = "S6dd-OdSdOH",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  u0 {1,D}
3   S    ux {1,D}
4   H    ux {1,S}
5   O    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.42,8.8,10.42,11.4,11.87,12.37,12.86],'cal/(mol*K)'),
        H298 = (-19.76,'kcal/mol'),
        S298 = (-11.85,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2201,
    label = "S6dd-OdSdCH",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  u0 {1,D}
3   S    ux {1,D}
4   C    ux {1,S}
5   H    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.14,7.72,9.25,10.1,9.72,9.71,11.2],'cal/(mol*K)'),
        H298 = (-16.02,'kcal/mol'),
        S298 = (-20.03,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2202,
    label = "S6ddd",
    group = 
"""
1 * S6ddd u0
""",
    thermo = 'S6ddd-XdXdXd',
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2203,
    label = "S6ddd-OdOdOd",
    group = 
"""
1 * S6ddd u0 p0 {2,D} {3,D} {4,D}
2   O2d   ux {1,D}
3   O2d   ux {1,D}
4   O2d   ux {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.21,13.87,15.2,16.17,17.5,18.31,19.08],'cal/(mol*K)'),
        H298 = (-94.93,'kcal/mol'),
        S298 = (61.47,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2204,
    label = "S6ddd-OdOdXd",
    group = 
"""
1 * S6ddd                                u0 p0 {2,D} {3,D} {4,D}
2   O2d                                  ux {1,D}
3   O2d                                  ux {1,D}
4   [C,S2d,S4d,S4dd,S6ddd,S6td,S6dd,S6d] ux {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.61,7.82,9.36,10.15,10.64,10.98,11.18],'cal/(mol*K)'),
        H298 = (-46.89,'kcal/mol'),
        S298 = (14.06,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2205,
    label = "S6ddd-OdXdXd",
    group = 
"""
1 * S6ddd                                u0 p0 {2,D} {3,D} {4,D}
2   O2d                                  ux {1,D}
3   [C,S2d,S4d,S4dd,S6ddd,S6td,S6dd,S6d] ux {1,D}
4   [C,S2d,S4d,S4dd,S6ddd,S6td,S6dd,S6d] ux {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.96,1.79,3.54,4.16,3.79,3.66,3.3],'cal/(mol*K)'),
        H298 = (2.27,'kcal/mol'),
        S298 = (-36.84,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2206,
    label = "S6t",
    group = 
"""
1 * S6t u0
""",
    thermo = 'S6t-CtCCC',
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2207,
    label = "S6t-CtCCC",
    group = 
"""
1 * S6t u0 p0 {2,T} {3,S} {4,S} {5,S}
2   C   ux {1,T}
3   C   ux {1,S}
4   C   ux {1,S}
5   C   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19,15.96,14.89,14.22,11.57,10.28,12.58],'cal/(mol*K)'),
        H298 = (11.59,'kcal/mol'),
        S298 = (41.24,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2208,
    label = "S6t-CtHHH",
    group = 
"""
1 * S6t u0 p0 {2,T} {3,S} {4,S} {5,S}
2   C   ux {1,T}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.26,10.74,11.95,13.44,17.14,19.55,21.82],'cal/(mol*K)'),
        H298 = (50.77,'kcal/mol'),
        S298 = (67.32,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2209,
    label = "S6t-CtOCC",
    group = 
"""
1 * S6t u0 p0 {2,T} {3,S} {4,S} {5,S}
2   C   ux {1,T}
3   C   ux {1,S}
4   C   ux {1,S}
5   O   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([16.27,14.42,14.26,14.24,13.24,12.82,14.25],'cal/(mol*K)'),
        H298 = (-12.08,'kcal/mol'),
        S298 = (-13.95,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2210,
    label = "S6t-CtOCH",
    group = 
"""
1 * S6t u0 p0 {2,T} {3,S} {4,S} {5,S}
2   C   ux {1,T}
3   C   ux {1,S}
4   O   ux {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.27,13.66,14.24,14.95,16.09,16.97,18.46],'cal/(mol*K)'),
        H298 = (-0.66,'kcal/mol'),
        S298 = (17.2,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2211,
    label = "S6td",
    group = 
"""
1 * S6td u0
""",
    thermo = 'S6td-CtCdC',
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2212,
    label = "S6td-CtCdC",
    group = 
"""
1 * S6td u0 p0 {2,T} {3,D} {4,S}
2   C    ux {1,T}
3   C    ux {1,D}
4   C    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.12,7.84,8.16,8.32,8.21,8.26,8.78],'cal/(mol*K)'),
        H298 = (12.45,'kcal/mol'),
        S298 = (-7.14,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2213,
    label = "S6td-CtOdC",
    group = 
"""
1 * S6td u0 p0 {2,T} {3,D} {4,S}
2   C    ux {1,T}
3   O    u0 {1,D}
4   C    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.72,13.21,13.52,13.94,14.8,15.4,16.57],'cal/(mol*K)'),
        H298 = (-54.95,'kcal/mol'),
        S298 = (42.23,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2214,
    label = "S6td-CtOdH",
    group = 
"""
1 * S6td u0 p0 {2,T} {3,D} {4,S}
2   C    ux {1,T}
3   O    u0 {1,D}
4   H    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.25,13.84,14.72,15.64,18.27,19.93,20.96],'cal/(mol*K)'),
        H298 = (-43.98,'kcal/mol'),
        S298 = (72.22,'cal/(mol*K)'),
    ),
    shortDesc = """RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
"""
"
""",
)

entry(
    index = 2215,
    label = "N",
    group = 
"""
1 * N u0
""",
    thermo = 'N3s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2216,
    label = "N0sc",
    group = 
"""
1 * N0sc u0 p3 c-2 {2,S}
2   R    ux {1,S}
""",
    thermo = 'N1s',
    shortDesc = """""",
    longDesc = 
"""
Nitrogen with three lone pairs and a single bond (e.g., [NH+]#[N+][N-2])
""",
)

entry(
    index = 2217,
    label = "N1s",
    group = 
"""
1 * N1s u0 p2
""",
    thermo = 'N1s-H',
    shortDesc = """""",
    longDesc = 
"""
Nitrogen with two lone pairs and a single bond
""",
)

entry(
    index = 2218,
    label = "N1s-H",
    group = 
"""
1 * N1s u0 p2 {2,S}
2   H   u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.9764,6.9777,6.9982,7.0454,7.2242,7.4742,8.0656],'cal/(mol*K)'),
        H298 = (85.2952,'kcal/mol'),
        S298 = (43.3053,'cal/(mol*K)'),
    ),
    shortDesc = """NH(S)""",
    longDesc = 
"""
Data base on species NH(S), source: GRIMech3.0-N
""",
)

entry(
    index = 2219,
    label = "N1s-N1s",
    group = 
"""
1 * N1s u0 p2 {2,S}
2   N1s u0 p2 {1,S}
""",
    thermo = 'N1s-H',
    shortDesc = """[N][N](S)""",
    longDesc = 
"""
Pointing to NH(S), so far no better alternative
""",
)

entry(
    index = 2220,
    label = "N1s-Cs",
    group = 
"""
1 * N1s u0 p2 {2,S}
2   C   u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3,2.65,2.5,2.49,2.65,2.65,2.57],'cal/(mol*K)'),
        H298 = (120.94,'kcal/mol'),
        S298 = (24.25,'cal/(mol*K)'),
    ),
    shortDesc = """[N]-CH3(S)""",
    longDesc = 
"""
Data base on species CH3N(S), source: thermo_DFT_CCSDTF12_BAC
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
subtracting the Cs-N2sHHH group
[N1s-CH3 (N-CH3 species) from thermo_DFT_CCSDTF12_BAC] - [Cs-N2sHHH from group.py]
""",
)

entry(
    index = 2221,
    label = "N1s-N3s",
    group = 
"""
1 * N1s u0 p2 {2,S}
2   N   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.97,2.07,2.25,2.5,3.05,3.48,5.5],'cal/(mol*K)'),
        H298 = (61,'kcal/mol'),
        S298 = (23,'cal/(mol*K)'),
    ),
    shortDesc = """[N]-NH2(S)""",
    longDesc = 
"""
Data base on species H2NN(S), source: Curran thermo library
subtracting the N3s-N3sFF group
[N1s-NH2 (N-NH2 species) from Curran] - [N3s-N3sHH from group.py]
""",
)

entry(
    index = 2222,
    label = "N1s-O2s",
    group = 
"""
1 * N1s u0 p2 {2,S}
2   O   u0 {1,S}
""",
    thermo = 'N1s-H',
    shortDesc = """[N]-OH(S)""",
    longDesc = 
"""
Pointing to NH(S), so far no better alternative
""",
)

entry(
    index = 2223,
    label = "N1dc",
    group = 
"""
1 * N1dc u0 p2 {2,D}
2   R!H  ux {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2224,
    label = "N1sc",
    group = 
"""
1 * N1sc u0 p2 {2,S} {3,S}
2   R    ux {1,S}
3   R    ux {1,S}
""",
    thermo = 'N1s',
    shortDesc = """""",
    longDesc = 
"""
Nitrogen with two lone pairs and two single bonds
""",
)

entry(
    index = 2225,
    label = "N3s",
    group = 
"""
1 * N3s u0
""",
    thermo = 'N3s-CsHH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2226,
    label = "N3s-CHH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2227,
    label = "N3s-CsHH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.72,6.51,7.32,8.07,9.41,10.47,12.28],'cal/(mol*K)'),
        H298 = (4.8,'kcal/mol'),
        S298 = (29.71,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2228,
    label = "N3s-CbHH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cb  u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.72,6.51,7.32,8.07,9.41,10.47,12.28],'cal/(mol*K)'),
        H298 = (4.8,'kcal/mol'),
        S298 = (29.71,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2229,
    label = "N3s-(CO)HH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.07,5.74,7.13,8.29,9.96,11.22,14.37],'cal/(mol*K)'),
        H298 = (-14.9,'kcal/mol'),
        S298 = (-24.69,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2230,
    label = "N3s-CdHH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.7,6.5,7.3,8.1,9.4,10.5,12.3],'cal/(mol*K)'),
        H298 = (4.8,'kcal/mol'),
        S298 = (29.7,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2231,
    label = "N3s-CCH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2232,
    label = "N3s-CsCsH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.2,5.21,6.13,6.83,7.9,8.65,9.55],'cal/(mol*K)'),
        H298 = (15.4,'kcal/mol'),
        S298 = (8.94,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2233,
    label = "N3s-CbCsH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cb  u0 {1,S}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (14.9,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2234,
    label = "N3s-CbCbH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cb  u0 {1,S}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (16.3,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2235,
    label = "N3s-(CO)CsH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (-4.4,'kcal/mol'),
        S298 = (3.9,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2236,
    label = "N3s-(CO)CbH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0.4,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2237,
    label = "N3s-(CO)(CO)H",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   CO  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   O2d u0 {2,D}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (-18.5,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2238,
    label = "N3s-(CtN3t)CsH",
    group = 
"""
1 * N3s u0 {2,S} {4,S} {5,S}
2   Ct  u0 {1,S} {3,T}
3   N3t u0 {2,T}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.3,11.6,12.8,13.9,15.5,16.7,18.3],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (44.1,'kcal/mol','+|-',1.3),
        S298 = (40.7,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2239,
    label = "N3s-(CdCd)CsH",
    group = 
"""
1 * N3s u0 {2,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D} {4,S}
3   Cd  u0 {2,D}
4   R   u0 {2,S}
5   Cs  u0 {1,S}
6   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.8,6.1,6.4,6.7,7.5,8.1,9.1],'cal/(mol*K)','+|-',[1.3,1.3,1.3,1.3,1.3,1.3,1.3]),
        H298 = (15.3,'kcal/mol','+|-',1.9),
        S298 = (8.7,'cal/(mol*K)','+|-',1.7),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2240,
    label = "N3s-CCC",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2241,
    label = "N3s-CsCsCs",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.48,4.56,5.43,5.97,6.56,6.67,6.5],'cal/(mol*K)'),
        H298 = (24.4,'kcal/mol'),
        S298 = (-13.46,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2242,
    label = "N3s-CbCsCs",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cb  u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (26.2,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2243,
    label = "N3s-(CO)CsCs",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2244,
    label = "N3s-(CO)(CO)Cs",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   CO  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   O2d u0 {2,D}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (-5.9,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2245,
    label = "N3s-(CO)(CO)Cb",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   CO  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   O2d u0 {2,D}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (-0.5,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2246,
    label = "N3s-(CtN3t)CsCs",
    group = 
"""
1 * N3s u0 {2,S} {4,S} {5,S}
2   Ct  u0 {1,S} {3,T}
3   N3t u0 {2,T}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.6,9.6,10.5,11.4,12.9,13.8,14.8],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (53.3,'kcal/mol','+|-',1.3),
        S298 = (21,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2247,
    label = "N3s-(CdCd)CsCs",
    group = 
"""
1 * N3s u0 {2,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D} {4,S}
3   Cd  u0 {2,D}
4   R   u0 {2,S}
5   Cs  u0 {1,S}
6   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.8,2.9,3.3,3.7,4.6,5,5.5],'cal/(mol*K)','+|-',[1.3,1.3,1.3,1.3,1.3,1.3,1.3]),
        H298 = (25.9,'kcal/mol','+|-',1.9),
        S298 = (-11,'cal/(mol*K)','+|-',1.7),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2248,
    label = "N3s-N3sHH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   H   u0 {1,S}
3   H   u0 {1,S}
4   N3s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.1,7.38,8.43,9.27,10.54,11.52,13.19],'cal/(mol*K)'),
        H298 = (11.4,'kcal/mol'),
        S298 = (29.13,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2249,
    label = "N3s-N3dHH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   H   u0 {1,S}
3   H   u0 {1,S}
4   N3d u0 {1,S}
""",
    thermo = 'N3s-N3sHH',
    shortDesc = """""",
    longDesc = 
"""
Currently points to N3s-N3sHH with no better estimate available
""",
)

entry(
    index = 2250,
    label = "N3s-NCH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   N   u0 {1,S}
3   C   u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2251,
    label = "N3s-N3sCsH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   H   u0 {1,S}
4   N3s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.82,5.8,6.5,7,7.8,8.3,9],'cal/(mol*K)'),
        H298 = (20.9,'kcal/mol'),
        S298 = (9.61,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2252,
    label = "N3s-N3sCbH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   N3s u0 {1,S}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (22.1,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2253,
    label = "N3s-CsH(N3dOd)",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   H   u0 {1,S}
4   N3d u0 {1,S} {5,D}
5   O2d u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.4,11.9,13.4,14.7,16.6,17.9,19.2],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (25.2,'kcal/mol','+|-',1.3),
        S298 = (41.7,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2254,
    label = "N3s-CsH(N5dcOdOs)",
    group = 
"""
1 * N3s  u0 {2,S} {3,S} {4,S}
2   Cs   u0 {1,S}
3   H    u0 {1,S}
4   N5dc u0 {1,S} {5,D} {6,S}
5   O2d  u0 {4,D}
6   O2s  u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.1,15.5,17.6,19.2,21.4,22.8,24.4],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (8.4,'kcal/mol','+|-',1.3),
        S298 = (45.3,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2255,
    label = "N3s-(CdCd)HN3s",
    group = 
"""
1 * N3s u0 {2,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D} {4,S}
3   Cd  u0 {2,D}
4   R   u0 {2,S}
5   H   u0 {1,S}
6   N3s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.5,5.4,6.5,7.3,8.5,9.1,9.9],'cal/(mol*K)','+|-',[1.1,1.1,1.1,1.1,1.1,1.1,1.1]),
        H298 = (20.5,'kcal/mol','+|-',1.5),
        S298 = (6.6,'cal/(mol*K)','+|-',1.4),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2256,
    label = "N3s-NCC",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   N   u0 {1,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2257,
    label = "N3s-NCsCs",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   N   u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (29.2,'kcal/mol'),
        S298 = (-13.8,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2258,
    label = "N3s-CsCsN3s",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   N3s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.7,4.9,5.8,6.3,6.8,6.8,6.7],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (26.8,'kcal/mol','+|-',1.3),
        S298 = (-14.5,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2259,
    label = "N3s-CsCs(N3dOd)",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   N3d u0 {1,S} {5,D}
5   O2d u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.4,10.5,11.5,12.4,13.8,14.6,15.3],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (32.6,'kcal/mol','+|-',1.3),
        S298 = (19.3,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2260,
    label = "N3s-CsCs(N5dcOdOs)",
    group = 
"""
1 * N3s  u0 {2,S} {3,S} {4,S}
2   Cs   u0 {1,S}
3   Cs   u0 {1,S}
4   N5dc u0 {1,S} {5,D} {6,S}
5   O2d  u0 {4,D}
6   O2s  u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.5,13.4,15.2,16.7,18.8,20,21.1],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (16.7,'kcal/mol','+|-',1.3),
        S298 = (25.8,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2261,
    label = "N3s-NCdCs",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   N   u0 {1,S}
3   Cd  u0 {1,S}
4   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2262,
    label = "N3s-(CdCd)CsN3s",
    group = 
"""
1 * N3s u0 {2,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D} {4,S}
3   Cd  u0 {2,D}
4   R   u0 {2,S}
5   Cs  u0 {1,S}
6   N3s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.2,4.2,4.4,4.8,5.4,5.7,6],'cal/(mol*K)','+|-',[1.1,1.1,1.1,1.1,1.1,1.1,1.1]),
        H298 = (30.3,'kcal/mol','+|-',1.5),
        S298 = (-13.2,'cal/(mol*K)','+|-',1.4),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2263,
    label = "N3s-CsHOs",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   H   u0 {1,S}
4   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.2,6.2,7,7.7,8.7,9.4,10.5],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (20.4,'kcal/mol','+|-',1.4),
        S298 = (8.1,'cal/(mol*K)','+|-',1.3),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2264,
    label = "N3s-CsCsOs",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.3,5.1,5.7,6.2,7,7.3,7.5],'cal/(mol*K)','+|-',[0.8,0.8,0.8,0.8,0.8,0.8,0.8]),
        H298 = (26.6,'kcal/mol','+|-',1.2),
        S298 = (-12.7,'cal/(mol*K)','+|-',1.1),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2265,
    label = "N3s-OsHH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   O2s u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.1,7.4,8.4,9.3,10.5,11.5,13.2],'cal/(mol*K)'),
        H298 = (11.4,'kcal/mol'),
        S298 = (29.1,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2266,
    label = "N3d",
    group = 
"""
1 * N3d u0
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2267,
    label = "N3d-CdH",
    group = 
"""
1 * N3d      u0 {2,D} {3,S}
2   [Cd,Cdd] u0 {1,D}
3   H        u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3,3.5,3.9,4.3,5,5.5,6.4],'cal/(mol*K)'),
        H298 = (16.3,'kcal/mol'),
        S298 = (13.3,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2268,
    label = "N3d-CdN3s",
    group = 
"""
1 * N3d u0 {2,D} {3,S}
2   Cd  u0 {1,D}
3   N3s u0 {1,S}
""",
    thermo = 'N3d-CdH',
    shortDesc = """""",
    longDesc = 
"""
Currently references to N3d-CdH with no better data
""",
)

entry(
    index = 2269,
    label = "N3d-N3dH",
    group = 
"""
1 * N3d u0 {2,S} {3,D}
2   H   u0 {1,S}
3   N3d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.38,4.89,5.44,5.94,6.77,7.42,8.44],'cal/(mol*K)'),
        H298 = (25.1,'kcal/mol'),
        S298 = (26.8,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2270,
    label = "N3d-N3dN3s",
    group = 
"""
1 * N3d u0 {2,D} {3,S}
2   N3d u0 {1,D}
3   N3s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (23,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2271,
    label = "N3d-OdOs",
    group = 
"""
1 * N3d u0 {2,D} {3,S}
2   O2d u0 {1,D}
3   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2272,
    label = "N3d-OdN3s",
    group = 
"""
1 * N3d u0 {2,D} {3,S}
2   O2d u0 {1,D}
3   N3s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2273,
    label = "N3d-CsR",
    group = 
"""
1 * N3d u0 {2,S} {3,D}
2   Cs  u0 {1,S}
3   R!H u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (21.3,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2274,
    label = "N3d-OdC",
    group = 
"""
1 * N3d u0 {2,D} {3,S}
2   O2d u0 {1,D}
3   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2275,
    label = "N3d-CdCs",
    group = 
"""
1 * N3d      u0 {2,D} {3,S}
2   [Cd,Cdd] u0 {1,D}
3   Cs       u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2,2.2,2.2,2.3,2.5,2.7,2.9],'cal/(mol*K)'),
        H298 = (21.3,'kcal/mol'),
        S298 = (-6.3,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2276,
    label = "N3d-N3dCs",
    group = 
"""
1 * N3d u0 {2,D} {3,S}
2   N3d u0 {1,D}
3   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.4,3.6,3.7,3.9,4.3,4.6,4.9],'cal/(mol*K)'),
        H298 = (27,'kcal/mol'),
        S298 = (7.2,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2277,
    label = "N3d-CbR",
    group = 
"""
1 * N3d u0 {2,S} {3,D}
2   Cb  u0 {1,S}
3   R!H u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (16.7,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2278,
    label = "N3t",
    group = 
"""
1 * N3t u0 p1 {2,T}
2   R!H u0 {1,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2279,
    label = "N3t-CtH",
    group = 
"""
1 * N3t u0 p1 {2,T}
2   Ct  u0 {1,T} {3,S}
3   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.28,5.68,5.97,6.22,6.6,6.97,6.66],'cal/(mol*K)'),
        H298 = (3.17,'kcal/mol'),
        S298 = (41.74,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Calculated by subtracting the data for the Ct-CtCs group (Ct-Cs STEIN and FAHR; J. PHYS. CHEM. 1985, 89, 17, 3714) from respective values from thermo_DFT_CCSDTF12_BAC data for the HCN species.
""",
)

entry(
    index = 2280,
    label = "N5dc",
    group = 
"""
1 * N5dc u0
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2281,
    label = "N5dc-OdOsCs",
    group = 
"""
1 * N5dc u0 {2,D} {3,S} {4,S}
2   O2d  u0 {1,D}
3   O2s  u0 {1,S}
4   Cs   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2282,
    label = "N5dc-OdOsCd",
    group = 
"""
1 * N5dc u0 {2,D} {3,S} {4,S}
2   O2d  u0 {1,D}
3   O2s  u0 {1,S}
4   Cd   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2283,
    label = "N5dc-OdOsOs",
    group = 
"""
1 * N5dc u0 {2,D} {3,S} {4,S}
2   O2d  u0 {1,D}
3   O2s  u0 {1,S}
4   O2s  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2284,
    label = "N5dc-OdOsN3s",
    group = 
"""
1 * N5dc u0 {2,D} {3,S} {4,S}
2   O2d  u0 {1,D}
3   O2s  u0 {1,S}
4   N3s  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2285,
    label = "N5ddc",
    group = 
"""
1 * N5ddc u0 p0 c+1
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2286,
    label = "Cl1s",
    group = 
"""
1 * Cl1s u0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """Dummy Chlorine group""",
    longDesc = 
"""
Dummy group for singly-bonded chlorine. Benson groups for chloroalkanes already account for Cl in the Carbon-centered groups.
""",
)

entry(
    index = 2287,
    label = "I1s",
    group = 
"""
1 * I1s u0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """Dummy Iodine group""",
    longDesc = 
"""
Dummy group for singly-bonded iodine.
Benson groups for iodoalkanes already account for I in the Carbon-centered groups.
""",
)

tree(
"""
L1: R
    L2: C
        L3: CJ2_singlet
            L4: CsJ2_singlet-HH
            L4: CsJ2_singlet-OsH
            L4: CdJ2_singlet-Od
            L4: CdJ2_singlet-Sd
            L4: CdJ2_singlet-(Cdd-Od)
            L4: CsJ2_singlet-CH
                L5: CsJ2_singlet-CsH
                L5: CsJ2_singlet-CtH
            L4: CdJ2_singlet-Cd
                L5: CdJ2_singlet-Cds
                L5: CdJ2_singlet-(Cdd-Cds)
            L4: CsJ2_singlet-(Cds-Cds-Cds-C)C
                L5: CsJ2_singlet-(Cds-Cds-Cds-Cds)Cs_5_ring
                L5: CsJ2_singlet-(Cds-Cds-Cds-Cds)Cs_6_ring
        L3: Cbf
            L4: Cbf-CbCbCbf
            L4: Cbf-CbCbfCbf
            L4: Cbf-CbfCbfCbf
        L3: Cb
            L4: Cb-H
            L4: Cb-O2s
            L4: Cb-S
            L4: Cb-N3s
            L4: Cb-C
                L5: Cb-Cs
                L5: Cb-Cds
                    L6: Cb-(Cds-O2d)
                    L6: Cb-(Cds-Cd)
                        L7: Cb-(Cds-Cds)
                        L7: Cb-(Cds-Cdd)
                            L8: Cb-(Cds-Cdd-O2d)
                            L8: Cb-(Cds-Cdd-S2d)
                            L8: Cb-(Cds-Cdd-Cd)
                L5: Cb-Ct
                    L6: Cb-(CtN3t)
                L5: Cb-Cb
            L4: Cb-Cl
            L4: Cb-I
        L3: Ct
            L4: Ct-CtN3s
            L4: Ct-N3tN3s
            L4: Ct-CtH
            L4: Ct-StH
            L4: Ct-CtOs
            L4: Ct-N3tOs
            L4: Ct-CtS
                L5: Ct-CtS2
                L5: Ct-CtS4
                L5: Ct-CtS6
            L4: Ct-N3tC
                L5: Ct-N3tCs
                L5: Ct-N3tCd
            L4: Ct-CtC
                L5: Ct-CtCs
                L5: Ct-CtCds
                    L6: Ct-Ct(Cds-O2d)
                    L6: Ct-Ct(Cds-Cd)
                        L7: Ct-Ct(Cds-Cds)
                        L7: Ct-Ct(Cds-Cdd)
                            L8: Ct-Ct(Cds-Cdd-O2d)
                            L8: Ct-Ct(Cds-Cdd-S2d)
                            L8: Ct-Ct(Cds-Cdd-Cd)
                L5: Ct-CtCt
                    L6: Ct-Ct(CtN3t)
                L5: Ct-CtCb
        L3: Cdd
            L4: Cdd-N3dCd
            L4: Cdd-OdOd
            L4: Cdd-OdSd
            L4: Cdd-SdSd
                L5: Cdd-S2dS2d
                L5: Cdd-S4S4
                L5: Cdd-S2S4
            L4: Cdd-CdOd
                L5: Cdd-CdsOd
                L5: Cdd-CddOd
                    L6: Cdd-(Cdd-O2d)O2d
                    L6: Cdd-(Cdd-Cd)O2d
            L4: Cdd-CdSd
                L5: Cdd-CdsSd
                    L6: Cdd-CdsS2d
                    L6: Cdd-CdsS4d
                    L6: Cdd-CdsS6d
                L5: Cdd-CddSd
                    L6: Cdd-(Cdd-S2d)S2d
                    L6: Cdd-(Cdd-Cd)S2d
            L4: Cdd-CdCd
                L5: Cdd-CddCdd
                    L6: Cdd-(Cdd-O2d)(Cdd-O2d)
                    L6: Cdd-(Cdd-S2d)(Cdd-S2d)
                    L6: Cdd-(Cdd-O2d)(Cdd-Cd)
                    L6: Cdd-(Cdd-S2d)(Cdd-Cd)
                    L6: Cdd-(Cdd-Cd)(Cdd-Cd)
                L5: Cdd-CddCds
                    L6: Cdd-(Cdd-O2d)Cds
                    L6: Cdd-(Cdd-S2d)Cds
                    L6: Cdd-(Cdd-Cd)Cds
                L5: Cdd-CdsCds
        L3: Cds
            L4: Cds-OdN3sH
            L4: Cds-OdN3sCs
            L4: Cd-N3dCsCs
            L4: Cd-N3dCsH
            L4: Cd-N3dHH
            L4: Cds-OdHH
            L4: Cds-OdOsH
            L4: CO-SH
                L5: CO-S2H
                L5: CO-S4H
                L5: CO-S6H
            L4: Cds-OdOsOs
            L4: CO-CsSs
            L4: CO-OsSs
            L4: Cds-OdCH
                L5: Cds-OdCsH
                L5: Cds-OdCdsH
                    L6: Cds-O2d(Cds-O2d)H
                    L6: Cds-O2d(Cds-Cd)H
                        L7: Cds-O2d(Cds-Cds)H
                        L7: Cds-O2d(Cds-Cdd)H
                            L8: Cds-O2d(Cds-Cdd-O2d)H
                            L8: Cds-O2d(Cds-Cdd-Cd)H
                L5: Cds-OdCtH
                L5: Cds-OdCbH
            L4: Cds-OdCOs
                L5: Cds-OdCsOs
                L5: Cds-OdCdsOs
                    L6: Cds-O2d(Cds-O2d)O2s
                    L6: Cds-O2d(Cds-Cd)O2s
                        L7: Cds-O2d(Cds-Cds)O2s
                        L7: Cds-O2d(Cds-Cdd)O2s
                            L8: Cds-O2d(Cds-Cdd-O2d)O2s
                            L8: Cds-O2d(Cds-Cdd-Cd)O2s
                L5: Cds-OdCtOs
                L5: Cds-OdCbOs
            L4: Cds-OdCC
                L5: Cds-OdCsCs
                L5: Cds-OdCdsCs
                    L6: Cds-O2d(Cds-O2d)Cs
                    L6: Cds-O2d(Cds-Cd)Cs
                        L7: Cds-O2d(Cds-Cds)Cs
                        L7: Cds-O2d(Cds-Cdd)Cs
                            L8: Cds-O2d(Cds-Cdd-O2d)Cs
                            L8: Cds-O2d(Cds-Cdd-Cd)Cs
                L5: Cds-OdCdsCds
                    L6: Cds-O2d(Cds-O2d)(Cds-O2d)
                    L6: Cds-O2d(Cds-Cd)(Cds-O2d)
                        L7: Cds-O2d(Cds-Cds)(Cds-O2d)
                        L7: Cds-O2d(Cds-Cdd)(Cds-O2d)
                            L8: Cds-O2d(Cds-Cdd-O2d)(Cds-O2d)
                            L8: Cds-O2d(Cds-Cdd-Cd)(Cds-O2d)
                    L6: Cds-O2d(Cds-Cd)(Cds-Cd)
                        L7: Cds-O2d(Cds-Cds)(Cds-Cds)
                        L7: Cds-O2d(Cds-Cdd)(Cds-Cds)
                            L8: Cds-O2d(Cds-Cdd-O2d)(Cds-Cds)
                            L8: Cds-O2d(Cds-Cdd-Cd)(Cds-Cds)
                        L7: Cds-O2d(Cds-Cdd)(Cds-Cdd)
                            L8: Cds-O2d(Cds-Cdd-O2d)(Cds-Cdd-O2d)
                            L8: Cds-O2d(Cds-Cdd-Cd)(Cds-Cdd-O2d)
                            L8: Cds-O2d(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                L5: Cds-OdCtCs
                L5: Cds-OdCtCds
                    L6: Cds-OdCt(Cds-O2d)
                    L6: Cds-OdCt(Cds-Cd)
                        L7: Cds-OdCt(Cds-Cds)
                        L7: Cds-OdCt(Cds-Cdd)
                            L8: Cds-OdCt(Cds-Cdd-O2d)
                            L8: Cds-OdCt(Cds-Cdd-Cd)
                L5: Cds-OdCtCt
                L5: Cds-OdCbCs
                L5: Cds-OdCbCds
                    L6: Cds-OdCb(Cds-O2d)
                    L6: Cds-OdCb(Cds-Cd)
                        L7: Cds-OdCb(Cds-Cds)
                        L7: Cds-OdCb(Cds-Cdd)
                            L8: Cds-OdCb(Cds-Cdd-O2d)
                            L8: Cds-OdCb(Cds-Cdd-Cd)
                L5: Cds-OdCbCt
                L5: Cds-OdCbCb
            L4: Cds-CdHH
                L5: Cds-CdsHH
                L5: Cds-CddHH
                    L6: Cds-(Cdd-O2d)HH
                    L6: Cds-(Cdd-S2d)HH
                    L6: Cds-(Cdd-Cd)HH
            L4: Cds-CdOsH
                L5: Cds-CdsOsH
                L5: Cds-CddOsH
                    L6: Cds-(Cdd-O2d)OsH
                    L6: Cds-(Cdd-Cd)OsH
            L4: Cds-CdSH
                L5: Cds-CdsSH
                    L6: Cds-CdsS2H
                    L6: Cds-CdsS4H
                    L6: Cds-CdsS6H
                L5: Cds-CddSsH
                    L6: Cds-(Cdd-S2d)SsH
                    L6: Cds-(Cdd-Cd)SsH
            L4: Cds-CdOsOs
                L5: Cds-CdsOsOs
                L5: Cds-CddOsOs
                    L6: Cds-(Cdd-O2d)OsOs
                    L6: Cds-(Cdd-Cd)OsOs
            L4: Cds-CdSsSs
                L5: Cds-CdsSsSs
                L5: Cds-CddSsSs
                    L6: Cds-(Cdd-S2d)SsSs
                    L6: Cds-(Cdd-Cd)SsSs
            L4: Cds-CdCH
                L5: Cds-CdsCsH
                L5: Cds-CdsCdsH
                    L6: Cd-Cd(CO)H
                    L6: Cds-Cds(Cds-Cd)H
                        L7: Cds-Cds(Cds-Cds)H
                        L7: Cds-Cds(Cds-Cdd)H
                            L8: Cd-Cd(CCO)H
                            L8: Cds-Cds(Cds-Cdd-S2d)H
                            L8: Cds-Cds(Cds-Cdd-Cd)H
                L5: Cds-CdsCtH
                    L6: Cds-CdsH(CtN3t)
                L5: Cds-CdsCbH
                    L6: Cds-(Cds-Os)CbH
                L5: Cds-CddCsH
                    L6: Cds-(Cdd-O2d)CsH
                    L6: Cds-(Cdd-S2d)CsH
                    L6: Cds-(Cdd-Cd)CsH
                L5: Cds-CddCdsH
                    L6: Cds-(Cdd-O2d)(Cds-O2d)H
                    L6: Cds-(Cdd-O2d)(Cds-Cd)H
                        L7: Cds-(Cdd-O2d)(Cds-Cds)H
                        L7: Cds-(Cdd-O2d)(Cds-Cdd)H
                            L8: Cds-(Cdd-O2d)(Cds-Cdd-O2d)H
                            L8: Cds-(Cdd-O2d)(Cds-Cdd-Cd)H
                    L6: Cds-(Cdd-S2d)(Cds-Cd)H
                        L7: Cds-(Cdd-S2d)(Cds-Cds)H
                        L7: Cds-(Cdd-S2d)(Cds-Cdd)H
                            L8: Cds-(Cdd-S2d)(Cds-Cdd-S2d)H
                            L8: Cds-(Cdd-S2d)(Cds-Cdd-Cd)H
                    L6: Cds-(Cdd-Cd)(Cds-O2d)H
                    L6: Cds-(Cdd-Cd)(Cds-Cd)H
                        L7: Cds-(Cdd-Cd)(Cds-Cds)H
                        L7: Cds-(Cdd-Cd)(Cds-Cdd)H
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-O2d)H
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-S2d)H
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Cd)H
                L5: Cds-CddCtH
                    L6: Cds-(Cdd-O2d)CtH
                    L6: Cds-(Cdd-S2d)CtH
                    L6: Cds-(Cdd-Cd)CtH
                L5: Cds-CddCbH
                    L6: Cds-(Cdd-O2d)CbH
                    L6: Cds-(Cdd-S2d)CbH
                    L6: Cds-(Cdd-Cd)CbH
                L5: Cds-(Cdd-Cd)C=SH
                L5: Cds-(Cdd-S2d)C=SH
                L5: Cds-CdsC=SH
            L4: Cds-CdCO
                L5: Cds-CdsCdsOs
                    L6: Cds-Cds(Cds-O2d)O2s
                    L6: Cds-Cds(Cds-Cd)O2s
                        L7: Cds-Cds(Cds-Cds)O2s
                        L7: Cds-Cds(Cds-Cdd)O2s
                            L8: Cds-Cds(Cds-Cdd-O2d)O2s
                            L8: Cds-Cds(Cds-Cdd-Cd)O2s
                L5: Cds-CdsCtOs
                L5: Cds-CdsCbOs
                L5: Cds-CddCdsOs
                    L6: Cds-(Cdd-O2d)(Cds-O2d)O2s
                    L6: Cds-(Cdd-O2d)(Cds-Cd)O2s
                        L7: Cds-(Cdd-O2d)(Cds-Cds)O2s
                        L7: Cds-(Cdd-O2d)(Cds-Cdd)O2s
                            L8: Cds-(Cdd-O2d)(Cds-Cdd-O2d)O2s
                            L8: Cds-(Cdd-O2d)(Cds-Cdd-Cd)O2s
                    L6: Cds-(Cdd-Cd)(Cds-Cd)O2s
                        L7: Cds-(Cdd-Cd)(Cds-Cds)O2s
                        L7: Cds-(Cdd-Cd)(Cds-Cdd)O2s
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-O2d)O2s
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Cd)O2s
                L5: Cds-CddCtOs
                    L6: Cds-(Cdd-O2d)CtOs
                    L6: Cds-(Cdd-Cd)CtOs
                L5: Cds-CddCbOs
                    L6: Cds-(Cdd-O2d)CbOs
                    L6: Cds-(Cdd-Cd)CbOs
                L5: Cd-CdCsOs
                    L6: Cds-CdsCsOs
                    L6: Cds-CddCsOs
                        L7: Cds-(Cdd-O2d)CsOs
                        L7: Cds-(Cdd-Cd)CsOs
            L4: Cds-CdCS
                L5: Cds-CdsCsSs
                    L6: Cds-CdsCsS2
                    L6: Cds-CdsCsS4
                    L6: Cds-CdsCsS6
                L5: Cds-CdsCdsSs
                    L6: Cds-Cds(Cds-Cd)S2s
                        L7: Cds-Cds(Cds-Cds)S2s
                        L7: Cds-Cds(Cds-Cdd)S2s
                            L8: Cds-Cds(Cds-Cdd-S2d)S2s
                            L8: Cds-Cds(Cds-Cdd-Cd)S2s
                L5: Cds-CdsCtSs
                L5: Cds-CdsCbSs
                L5: Cds-CddCsSs
                    L6: Cds-(Cdd-S2d)CsSs
                    L6: Cds-(Cdd-Cd)CsSs
                L5: Cds-CddCdsSs
                    L6: Cds-(Cdd-S2d)(Cds-Cd)S2s
                        L7: Cds-(Cdd-S2d)(Cds-Cds)S2s
                        L7: Cds-(Cdd-S2d)(Cds-Cdd)S2s
                            L8: Cds-(Cdd-S2d)(Cds-Cdd-S2d)S2s
                            L8: Cds-(Cdd-S2d)(Cds-Cdd-Cd)S2s
                    L6: Cds-(Cdd-Cd)(Cds-Cd)S2s
                        L7: Cds-(Cdd-Cd)(Cds-Cds)S2s
                        L7: Cds-(Cdd-Cd)(Cds-Cdd)S2s
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-S2d)S2s
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Cd)S2s
                L5: Cds-CddCtSs
                    L6: Cds-(Cdd-S2d)CtSs
                    L6: Cds-(Cdd-Cd)CtSs
                L5: Cds-CddCbSs
                    L6: Cds-(Cdd-S2d)CbSs
                    L6: Cds-(Cdd-Cd)CbSs
                L5: Cds-(Cdd-S2d)C=SSs
                L5: Cds-CdsC=SSs
            L4: Cds-CdCC
                L5: Cds-CdsCsCs
                L5: Cds-CdsCdsCs
                    L6: Cd-CdCs(CO)
                    L6: Cds-Cds(Cds-Cd)Cs
                        L7: Cds-Cds(Cds-Cds)Cs
                        L7: Cds-Cds(Cds-Cdd)Cs
                            L8: Cd-CdCs(CCO)
                            L8: Cds-Cds(Cds-Cdd-S2d)Cs
                            L8: Cds-Cds(Cds-Cdd-Cd)Cs
                L5: Cds-CdsCdsCds
                    L6: Cds-Cds(Cds-O2d)(Cds-O2d)
                    L6: Cds-Cds(Cds-O2d)(Cds-Cd)
                        L7: Cds-Cds(Cds-O2d)(Cds-Cds)
                        L7: Cds-Cds(Cds-O2d)(Cds-Cdd)
                            L8: Cds-Cds(Cds-O2d)(Cds-Cdd-O2d)
                            L8: Cds-Cds(Cds-O2d)(Cds-Cdd-Cd)
                    L6: Cds-Cds(Cds-Cd)(Cds-Cd)
                        L7: Cds-Cds(Cds-Cds)(Cds-Cds)
                        L7: Cds-Cds(Cds-Cds)(Cds-Cdd)
                            L8: Cds-Cds(Cds-Cds)(Cds-Cdd-O2d)
                            L8: Cds-Cds(Cds-Cds)(Cds-Cdd-S2d)
                            L8: Cds-Cds(Cds-Cds)(Cds-Cdd-Cd)
                        L7: Cds-Cds(Cds-Cdd)(Cds-Cdd)
                            L8: Cds-Cds(Cds-Cdd-O2d)(Cds-Cdd-O2d)
                            L8: Cds-Cds(Cds-Cdd-O2d)(Cds-Cdd-Cd)
                            L8: Cds-Cds(Cds-Cdd-S2d)(Cds-Cdd-S2d)
                            L8: Cds-Cds(Cds-Cdd-S2d)(Cds-Cdd-Cd)
                            L8: Cds-Cds(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                L5: Cds-CdsCtCs
                    L6: Cd-CdCs(CtN3t)
                L5: Cds-CdsCtCds
                    L6: Cds-CdsCt(Cds-O2d)
                    L6: Cds-CdsCt(Cds-Cd)
                        L7: Cds-Cds(Cds-Cds)Ct
                        L7: Cds-Cds(Cds-Cdd)Ct
                            L8: Cds-Cds(Cds-Cdd-O2d)Ct
                            L8: Cds-Cds(Cds-Cdd-S2d)Ct
                            L8: Cds-Cds(Cds-Cdd-Cd)Ct
                L5: Cds-CdsCtCt
                    L6: Cds-Cd(CtN3t)(CtN3t)
                L5: Cds-CdsCbCs
                L5: Cds-CdsCbCds
                    L6: Cds-CdsCb(Cds-O2d)
                    L6: Cds-Cds(Cds-Cd)Cb
                        L7: Cds-Cds(Cds-Cds)Cb
                        L7: Cds-Cds(Cds-Cdd)Cb
                            L8: Cds-Cds(Cds-Cdd-O2d)Cb
                            L8: Cds-Cds(Cds-Cdd-S2d)Cb
                            L8: Cds-Cds(Cds-Cdd-Cd)Cb
                L5: Cds-CdsCbCt
                L5: Cds-CdsCbCb
                L5: Cds-CddCsCs
                    L6: Cds-(Cdd-O2d)CsCs
                    L6: Cds-(Cdd-S2d)CsCs
                    L6: Cds-(Cdd-Cd)CsCs
                L5: Cds-CddCdsCs
                    L6: Cds-(Cdd-O2d)(Cds-O2d)Cs
                    L6: Cds-(Cdd-O2d)(Cds-Cd)Cs
                        L7: Cds-(Cdd-O2d)(Cds-Cds)Cs
                        L7: Cds-(Cdd-O2d)(Cds-Cdd)Cs
                            L8: Cds-(Cdd-O2d)(Cds-Cdd-O2d)Cs
                            L8: Cds-(Cdd-O2d)(Cds-Cdd-Cd)Cs
                    L6: Cds-(Cdd-S2d)(Cds-Cd)Cs
                        L7: Cds-(Cdd-S2d)(Cds-Cds)Cs
                        L7: Cds-(Cdd-S2d)(Cds-Cdd)Cs
                            L8: Cds-(Cdd-S2d)(Cds-Cdd-S2d)Cs
                            L8: Cds-(Cdd-S2d)(Cds-Cdd-Cd)Cs
                    L6: Cds-(Cdd-Cd)(Cds-Cd)Cs
                        L7: Cds-(Cdd-Cd)(Cds-Cds)Cs
                        L7: Cds-(Cdd-Cd)(Cds-Cdd)Cs
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-O2d)Cs
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-S2d)Cs
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Cd)Cs
                L5: Cds-CddCdsCds
                    L6: Cds-(Cdd-O2d)(Cds-O2d)(Cds-O2d)
                    L6: Cds-(Cdd-O2d)(Cds-Cd)(Cds-O2d)
                        L7: Cds-(Cdd-O2d)(Cds-Cds)(Cds-O2d)
                        L7: Cds-(Cdd-O2d)(Cds-Cdd)(Cds-O2d)
                            L8: Cds-(Cdd-O2d)(Cds-Cdd-O2d)(Cds-O2d)
                            L8: Cds-(Cdd-O2d)(Cds-Cdd-Cd)(Cds-O2d)
                    L6: Cds-(Cdd-O2d)(Cds-Cd)(Cds-Cd)
                        L7: Cds-(Cdd-O2d)(Cds-Cds)(Cds-Cds)
                        L7: Cds-(Cdd-O2d)(Cds-Cdd)(Cds-Cds)
                            L8: Cds-(Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cds)
                            L8: Cds-(Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cds)
                        L7: Cds-(Cdd-O2d)(Cds-Cdd)(Cds-Cdd)
                            L8: Cds-(Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)
                            L8: Cds-(Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)
                            L8: Cds-(Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                    L6: Cds-(Cdd-Cd)(Cds-O2d)(Cds-O2d)
                    L6: Cds-(Cdd-Cd)(Cds-O2d)(Cds-Cd)
                        L7: Cds-(Cdd-Cd)(Cds-O2d)(Cds-Cds)
                        L7: Cds-(Cdd-Cd)(Cds-O2d)(Cds-Cdd)
                            L8: Cds-(Cdd-Cd)(Cds-O2d)(Cds-Cdd-O2d)
                            L8: Cds-(Cdd-Cd)(Cds-O2d)(Cds-Cdd-Cd)
                    L6: Cds-(Cdd-S2d)(Cds-Cd)(Cds-Cd)
                        L7: Cds-(Cdd-S2d)(Cds-Cds)(Cds-Cds)
                        L7: Cds-(Cdd-S2d)(Cds-Cdd)(Cds-Cds)
                            L8: Cds-(Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cds)
                            L8: Cds-(Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cds)
                        L7: Cds-(Cdd-S2d)(Cds-Cdd)(Cds-Cdd)
                            L8: Cds-(Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)
                            L8: Cds-(Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-Cd)
                            L8: Cds-(Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                    L6: Cds-(Cdd-Cd)(Cds-Cd)(Cds-Cd)
                        L7: Cds-(Cdd-Cd)(Cds-Cds)(Cds-Cds)
                        L7: Cds-(Cdd-Cd)(Cds-Cdd)(Cds-Cds)
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-O2d)(Cds-Cds)
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-S2d)(Cds-Cds)
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cds)
                        L7: Cds-(Cdd-Cd)(Cds-Cdd)(Cds-Cdd)
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-O2d)(Cds-Cdd-O2d)
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-O2d)(Cds-Cdd-Cd)
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-S2d)(Cds-Cdd-S2d)
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-S2d)(Cds-Cdd-Cd)
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                L5: Cds-CddCtCs
                    L6: Cds-(Cdd-O2d)CtCs
                    L6: Cds-(Cdd-S2d)CtCs
                    L6: Cds-(Cdd-Cd)CtCs
                L5: Cds-CddCtCds
                    L6: Cds-(Cdd-O2d)(Cds-O2d)Ct
                    L6: Cds-(Cdd-O2d)(Cds-Cd)Ct
                        L7: Cds-(Cdd-O2d)(Cds-Cds)Ct
                        L7: Cds-(Cdd-O2d)(Cds-Cdd)Ct
                            L8: Cds-(Cdd-O2d)(Cds-Cdd-O2d)Ct
                            L8: Cds-(Cdd-O2d)(Cds-Cdd-Cd)Ct
                    L6: Cds-(Cdd-S2d)(Cds-Cd)Ct
                        L7: Cds-(Cdd-S2d)(Cds-Cds)Ct
                        L7: Cds-(Cdd-S2d)(Cds-Cdd)Ct
                            L8: Cds-(Cdd-S2d)(Cds-Cdd-S2d)Ct
                            L8: Cds-(Cdd-S2d)(Cds-Cdd-Cd)Ct
                    L6: Cds-(Cdd-Cd)(Cds-Cd)Ct
                        L7: Cds-(Cdd-Cd)(Cds-Cds)Ct
                        L7: Cds-(Cdd-Cd)(Cds-Cdd)Ct
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-O2d)Ct
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-S2d)Ct
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Cd)Ct
                L5: Cds-CddCtCt
                    L6: Cds-(Cdd-O2d)CtCt
                    L6: Cds-(Cdd-S2d)CtCt
                    L6: Cds-(Cdd-Cd)CtCt
                L5: Cds-CddCbCs
                    L6: Cds-(Cdd-O2d)CbCs
                    L6: Cds-(Cdd-S2d)CbCs
                    L6: Cds-(Cdd-Cd)CbCs
                L5: Cds-CddCbCds
                    L6: Cds-(Cdd-O2d)(Cds-O2d)Cb
                    L6: Cds-(Cdd-O2d)(Cds-Cd)Cb
                        L7: Cds-(Cdd-O2d)(Cds-Cds)Cb
                        L7: Cds-(Cdd-O2d)(Cds-Cdd)Cb
                            L8: Cds-(Cdd-O2d)(Cds-Cdd-O2d)Cb
                            L8: Cds-(Cdd-O2d)(Cds-Cdd-Cd)Cb
                    L6: Cds-(Cdd-S2d)(Cds-Cd)Cb
                        L7: Cds-(Cdd-S2d)(Cds-Cds)Cb
                        L7: Cds-(Cdd-S2d)(Cds-Cdd)Cb
                            L8: Cds-(Cdd-S2d)(Cds-Cdd-S2d)Cb
                            L8: Cds-(Cdd-S2d)(Cds-Cdd-Cd)Cb
                    L6: Cds-(Cdd-Cd)(Cds-Cd)Cb
                        L7: Cds-(Cdd-Cd)(Cds-Cds)Cb
                        L7: Cds-(Cdd-Cd)(Cds-Cdd)Cb
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-O2d)Cb
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-S2d)Cb
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Cd)Cb
                L5: Cds-CddCbCt
                    L6: Cds-(Cdd-O2d)CbCt
                    L6: Cds-(Cdd-S2d)CbCt
                    L6: Cds-(Cdd-Cd)CbCt
                L5: Cds-CddCbCb
                    L6: Cds-(Cdd-O2d)CbCb
                    L6: Cds-(Cdd-S2d)CbCb
                    L6: Cds-(Cdd-Cd)CbCb
                L5: Cds-CdsC=SC=S
                L5: Cds-(Cdd-Cd)C=S(Cds-Cd)
                    L6: Cds-(Cdd-Cd)C=S(Cds-Cds)
                    L6: Cds-(Cdd-Cd)C=S(Cds-Cdd)
                        L7: Cds-(Cdd-Cd)C=S(Cds-Cdd-Cd)
                        L7: Cds-(Cdd-Cd)C=S(Cds-Cdd-S2d)
                L5: Cds-(Cdd-S2d)C=SCs
                L5: Cds-(Cdd-S2d)C=SCt
                L5: Cds-(Cdd-S2d)C=SCb
                L5: Cds-(Cdd-Cd)C=SC=S
                L5: Cds-(Cdd-S2d)(Cds-Cd)C=S
                    L6: Cds-(Cdd-S2d)(Cds-Cds)C=S
                    L6: Cds-(Cdd-S2d)(Cds-Cdd)C=S
                        L7: Cds-(Cdd-S2d)(Cds-Cdd-S2d)C=S
                        L7: Cds-(Cdd-S2d)(Cds-Cdd-Cd)C=S
                L5: Cds-CdsCbC=S
                L5: Cds-CdsCtC=S
                L5: Cds-CdsC=SCs
                L5: Cds-CdsC=S(Cds-Cd)
                    L6: Cds-CdsC=S(Cds-Cds)
                    L6: Cds-CdsC=S(Cds-Cdd)
                        L7: Cds-CdsC=S(Cds-Cdd-Cd)
                        L7: Cds-CdsC=S(Cds-Cdd-S2d)
                L5: Cds-(Cdd-S2d)C=SC=S
            L4: Cds-CNH
                L5: Cd-CdHN3s
                L5: Cd-CdH(N5dcOdOs)
            L4: Cds-CCN
                L5: Cd-CdCsN3s
                L5: Cd-CdCs(N5dcOdOs)
            L4: C=S-SsSs
            L4: C=S-CH
                L5: C=S-CsH
                    L6: C=S2-CsH
                    L6: C=S4-CsH
                L5: C=S-CdsH
                    L6: C=S-(Cds-Cd)H
                        L7: C=S-(Cds-Cdd)H
                            L8: C=S-(Cds-Cdd-Cd)H
                            L8: C=S-(Cds-Cdd-S2d)H
                        L7: C=S-(Cds-Cds)H
                L5: C=S-CtH
                L5: C=S-C=SH
            L4: C=S-CC
                L5: C=S-CbCds
                    L6: C=S-Cb(Cds-Cd)
                        L7: C=S-Cb(Cds-Cds)
                        L7: C=S-Cb(Cds-Cdd)
                            L8: C=S-Cb(Cds-Cdd-S2d)
                            L8: C=S-Cb(Cds-Cdd-Cd)
                L5: C=S-CtCt
                L5: C=S-CbCb
                L5: C=S-CdsCds
                    L6: C=S-(Cds-Cd)(Cds-Cd)
                        L7: C=S-(Cds-Cdd)(Cds-Cds)
                            L8: C=S-(Cds-Cdd-Cd)(Cds-Cds)
                            L8: C=S-(Cds-Cdd-S2d)(Cds-Cds)
                        L7: C=S-(Cds-Cds)(Cds-Cds)
                        L7: C=S-(Cds-Cdd)(Cds-Cdd)
                            L8: C=S-(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                            L8: C=S-(Cds-Cdd-S2d)(Cds-Cdd-S2d)
                            L8: C=S-(Cds-Cdd-Cd)(Cds-Cdd-S2d)
                L5: C=S-CtCds
                    L6: C=S-Ct(Cds-Cd)
                        L7: C=S-Ct(Cds-Cds)
                        L7: C=S-Ct(Cds-Cdd)
                            L8: C=S-Ct(Cds-Cdd-Cd)
                            L8: C=S-Ct(Cds-Cdd-S2d)
                L5: C=S-CbCt
                L5: C=S-CsCs
                L5: C=S-CdsCs
                    L6: C=S-(Cds-Cd)Cs
                        L7: C=S-(Cds-Cds)Cs
                        L7: C=S-(Cds-Cdd)Cs
                            L8: C=S-(Cds-Cdd-S2d)Cs
                            L8: C=S-(Cds-Cdd-Cd)Cs
                L5: C=S-CtCs
                L5: C=S-CbCs
                L5: C=S-C=SCs
                L5: C=S-CtC=S
                L5: C=S-(Cds-Cd)C=S
                    L6: C=S-(Cds-Cdd)C=S
                        L7: C=S-(Cds-Cdd-Cd)C=S
                        L7: C=S-(Cds-Cdd-S2d)C=S
                    L6: C=S-(Cds-Cds)C=S
                L5: C=S-C=SC=S
                L5: C=S-CbC=S
            L4: C=S-HH
                L5: C=S2d-HH
                L5: C=S4d-HH
                L5: C=S6dd-HH
                L5: C=S6ddd-HH
            L4: C=S-SH
                L5: C=S-S2H
                L5: C=S-S4H
                L5: C=S-S6H
                L5: C=S6-S2H
            L4: C=S-CSs
                L5: C=S-CbSs
                L5: C=S-CdsSs
                    L6: C=S-(Cds-Cd)S2s
                        L7: C=S-(Cds-Cds)S2s
                        L7: C=S-(Cds-Cdd)S2s
                            L8: C=S-(Cds-Cdd-Cd)S2s
                            L8: C=S-(Cds-Cdd-S2d)S2s
                L5: C=S-S(CO)
                L5: C=S-CtSs
                L5: C=S-CsSs
                L5: C=S-C=SSs
            L4: Cds-CdClH
            L4: Cds-CdIH
            L4: Cds-CdClCl
            L4: Cds-CdClC
                L5: Cds-CdClCd
            L4: C=S-OsH
                L5: C=S2-OsH
                L5: C=S4-OsH
            L4: C=S-CsOs
            L4: C=S-OsOs
            L4: C=S-OsS
        L3: Cs
            L4: Cs-NHHH
                L5: Cs-N3sHHH
                L5: Cs-N3dHHH
                    L6: Cs-(N3dCd)HHH
                    L6: Cs-(N3dN3d)HHH
            L4: Cs-NCsHH
                L5: Cs-N3sCsHH
                L5: Cs-N3dCHH
                    L6: Cs-(N3dN3d)CsHH
                    L6: Cs-(N3dOd)CHH
                    L6: Cs-(N3dCd)CsHH
                L5: Cs-N5dcCsHH
                    L6: Cs-(N5dcOdOs)CsHH
            L4: Cs-NCsCsH
                L5: Cs-N3sCsCsH
                L5: Cs-N3dCsCsH
                    L6: Cs-(N3dOd)CsCsH
                    L6: Cs-(N3dN3d)CsCsH
                L5: Cs-N5dcCsCsH
                    L6: Cs-(N5dcOdOs)CsCsH
            L4: Cs-NCsCsCs
                L5: Cs-N3sCsCsCs
                L5: Cs-N3dCsCsCs
                    L6: Cs-(N3dOd)CsCsCs
                    L6: Cs-(N3dN3d)CsCsCs
                L5: Cs-N5dcCsCsCs
                    L6: Cs-(N5dcOdOs)CsCsCs
            L4: Cs-NNCsCs
                L5: Cs-N5dcN5dcCsCs
            L4: Cs-NNCsH
                L5: Cs-(N5dcOdOs)(N5dcOdOs)CsH
            L4: Cs-HHHH
            L4: Cs-CHHH
                L5: Cs-CsHHH
                L5: Cs-CdsHHH
                    L6: Cs-(Cds-O2d)HHH
                    L6: Cs-(Cds-Cd)HHH
                        L7: Cs-(Cds-Cds)HHH
                        L7: Cs-(Cds-Cdd)HHH
                            L8: Cs-(Cds-Cdd-O2d)HHH
                            L8: Cs-(Cds-Cdd-S2d)HHH
                            L8: Cs-(Cds-Cdd-Cd)HHH
                    L6: Cs-(CdN3d)HHH
                L5: Cs-CtHHH
                    L6: Cs-(CtN3t)HHH
                L5: Cs-CbHHH
                L5: Cs-C=SHHH
            L4: Cs-OsHHH
            L4: Cs-OsOsHH
            L4: Cs-OsOsOsH
            L4: Cs-OsSHH
                L5: Cs-OsS2HH
                L5: Cs-OsS4HH
            L4: Cs-OsSSH
                L5: Cs-OsS2S2H
                L5: Cs-OsS4S2H
            L4: Cs-OsOsSH
                L5: Cs-OsOsS2H
                L5: Cs-OsOsS4H
            L4: Cs-SsHHH
                L5: Cs-S2sHHH
                L5: Cs-S4HHH
                L5: Cs-S6HHH
            L4: Cs-SsSsHH
            L4: Cs-SsSsSsH
            L4: Cs-CCHH
                L5: Cs-CsCsHH
                L5: Cs-CdsCsHH
                    L6: Cs-(Cds-O2d)CsHH
                    L6: Cs-(Cds-Cd)CsHH
                        L7: Cs-(Cds-Cds)CsHH
                        L7: Cs-(Cds-Cdd)CsHH
                            L8: Cs-(Cds-Cdd-O2d)CsHH
                            L8: Cs-(Cds-Cdd-S2d)CsHH
                            L8: Cs-(Cds-Cdd-Cd)CsHH
                    L6: Cs-(CdN3d)CsHH
                L5: Cs-CdsCdsHH
                    L6: Cs-(Cds-O2d)(Cds-O2d)HH
                    L6: Cs-(Cds-O2d)(Cds-Cd)HH
                        L7: Cs-(Cds-O2d)(Cds-Cds)HH
                        L7: Cs-(Cds-O2d)(Cds-Cdd)HH
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)HH
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)HH
                    L6: Cs-(Cds-Cd)(Cds-Cd)HH
                        L7: Cs-(Cds-Cds)(Cds-Cds)HH
                        L7: Cs-(Cds-Cdd)(Cds-Cds)HH
                            L8: Cs-Cd(CCO)HH
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cds)HH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)HH
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)HH
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)HH
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)HH
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)HH
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)HH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)HH
                L5: Cs-CtCsHH
                    L6: Cs-(CtN3t)CsHH
                L5: Cs-CtCdsHH
                    L6: Cs-(Cds-O2d)CtHH
                    L6: Cs-(Cds-Cd)CtHH
                        L7: Cs-(Cds-Cds)CtHH
                        L7: Cs-(Cds-Cdd)CtHH
                            L8: Cs-(Cds-Cdd-O2d)CtHH
                            L8: Cs-(Cds-Cdd-S2d)CtHH
                            L8: Cs-(Cds-Cdd-Cd)CtHH
                L5: Cs-CtCtHH
                L5: Cs-CbCsHH
                L5: Cs-CbCdsHH
                    L6: Cs-(Cds-O2d)CbHH
                    L6: Cs-(Cds-Cd)CbHH
                        L7: Cs-(Cds-Cds)CbHH
                        L7: Cs-(Cds-Cdd)CbHH
                            L8: Cs-(Cds-Cdd-O2d)CbHH
                            L8: Cs-(Cds-Cdd-S2d)CbHH
                            L8: Cs-(Cds-Cdd-Cd)CbHH
                L5: Cs-CbCtHH
                L5: Cs-CbCbHH
                L5: Cs-C=SCtHH
                L5: Cs-C=SCsHH
                L5: Cs-C=S(Cds-Cd)HH
                    L6: Cs-C=S(Cds-Cdd)HH
                        L7: Cs-C=S(Cds-Cdd-Cd)HH
                        L7: Cs-C=S(Cds-Cdd-S2d)HH
                    L6: Cs-C=S(Cds-Cds)HH
                L5: Cs-C=SC=SHH
                L5: Cs-C=SCbHH
            L4: Cs-CCCH
                L5: Cs-CsCsCsH
                L5: Cs-CdsCsCsH
                    L6: Cs-(Cds-O2d)CsCsH
                    L6: Cs-(Cds-Cd)CsCsH
                        L7: Cs-(Cds-Cds)CsCsH
                        L7: Cs-(Cds-Cdd)CsCsH
                            L8: Cs-(Cds-Cdd-O2d)CsCsH
                            L8: Cs-(Cds-Cdd-S2d)CsCsH
                            L8: Cs-(Cds-Cdd-Cd)CsCsH
                    L6: Cs-(CdN3d)CsCsH
                L5: Cs-CtCsCsH
                    L6: Cs-(CtN3t)CsCsH
                L5: Cs-CbCsCsH
                L5: Cs-CdsCdsCsH
                    L6: Cs-(Cds-O2d)(Cds-O2d)CsH
                    L6: Cs-(Cds-O2d)(Cds-Cd)CsH
                        L7: Cs-(Cds-O2d)(Cds-Cds)CsH
                        L7: Cs-(Cds-O2d)(Cds-Cdd)CsH
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)CsH
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)CsH
                    L6: Cs-(Cds-Cd)(Cds-Cd)CsH
                        L7: Cs-(Cds-Cds)(Cds-Cds)CsH
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CsH
                            L8: Cs-CsCd(CCO)H
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cds)CsH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CsH
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CsH
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CsH
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CsH
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CsH
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CsH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CsH
                L5: Cs-CtCdsCsH
                    L6: Cs-(Cds-O2d)CtCsH
                    L6: Cs-(Cds-Cd)CtCsH
                        L7: Cs-(Cds-Cds)CtCsH
                        L7: Cs-(Cds-Cdd)CtCsH
                            L8: Cs-(Cds-Cdd-O2d)CtCsH
                            L8: Cs-(Cds-Cdd-S2d)CtCsH
                            L8: Cs-(Cds-Cdd-Cd)CtCsH
                L5: Cs-CbCdsCsH
                    L6: Cs-(Cds-O2d)CbCsH
                    L6: Cs-(Cds-Cd)CbCsH
                        L7: Cs-(Cds-Cds)CbCsH
                        L7: Cs-(Cds-Cdd)CbCsH
                            L8: Cs-(Cds-Cdd-O2d)CbCsH
                            L8: Cs-(Cds-Cdd-Cd)CbCsH
                L5: Cs-CtCtCsH
                L5: Cs-CbCtCsH
                L5: Cs-CbCbCsH
                L5: Cs-CdsCdsCdsH
                    L6: Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)H
                    L6: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cd)H
                        L7: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)H
                        L7: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd)H
                            L8: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)H
                            L8: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)H
                    L6: Cs-(Cds-O2d)(Cds-Cd)(Cds-Cd)H
                        L7: Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)H
                        L7: Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cds)H
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)H
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cds)H
                        L7: Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cdd)H
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)H
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)H
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H
                    L6: Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)H
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)H
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)H
                            L8: Cs-CdCd(CCO)H
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-S2d)H
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)H
                        L7: Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)H
                            L8: Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)H
                            L8: Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-Cd)H
                            L8: Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-S2d)H
                            L8: Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-Cd)H
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)H
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)H
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)H
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)H
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-Cd)H
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H
                L5: Cs-CtCdsCdsH
                    L6: Cs-(Cds-O2d)(Cds-O2d)CtH
                    L6: Cs-(Cds-O2d)(Cds-Cd)CtH
                        L7: Cs-(Cds-O2d)(Cds-Cds)CtH
                        L7: Cs-(Cds-O2d)(Cds-Cdd)CtH
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)CtH
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)CtH
                    L6: Cs-(Cds-Cd)(Cds-Cd)CtH
                        L7: Cs-(Cds-Cds)(Cds-Cds)CtH
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CtH
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cds)CtH
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cds)CtH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CtH
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CtH
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CtH
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CtH
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CtH
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CtH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtH
                L5: Cs-CbCdsCdsH
                    L6: Cs-(Cds-O2d)(Cds-O2d)CbH
                    L6: Cs-(Cds-O2d)(Cds-Cd)CbH
                        L7: Cs-(Cds-O2d)(Cds-Cds)CbH
                        L7: Cs-(Cds-O2d)(Cds-Cdd)CbH
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)CbH
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)CbH
                    L6: Cs-(Cds-Cd)(Cds-Cd)CbH
                        L7: Cs-(Cds-Cds)(Cds-Cds)CbH
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CbH
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cds)CbH
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cds)CbH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CbH
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CbH
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CbH
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CbH
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CbH
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CbH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbH
                L5: Cs-CtCtCdsH
                    L6: Cs-CtCt(Cds-O2d)H
                    L6: Cs-CtCt(Cds-Cd)H
                        L7: Cs-CtCt(Cds-Cds)H
                        L7: Cs-CtCt(Cds-Cdd)H
                            L8: Cs-CtCt(Cds-Cdd-O2d)H
                            L8: Cs-CtCt(Cds-Cdd-S2d)H
                            L8: Cs-CtCt(Cds-Cdd-Cd)H
                L5: Cs-CbCtCdsH
                    L6: Cs-CbCt(Cds-O2d)H
                    L6: Cs-CbCt(Cds-Cd)H
                        L7: Cs-CbCt(Cds-Cds)H
                        L7: Cs-CbCt(Cds-Cdd)H
                            L8: Cs-CbCt(Cds-Cdd-O2d)H
                            L8: Cs-CbCt(Cds-Cdd-S2d)H
                            L8: Cs-CbCt(Cds-Cdd-Cd)H
                L5: Cs-CbCbCdsH
                    L6: Cs-CbCb(Cds-O2d)H
                    L6: Cs-CbCb(Cds-Cd)H
                        L7: Cs-CbCb(Cds-Cds)H
                        L7: Cs-CbCb(Cds-Cdd)H
                            L8: Cs-CbCb(Cds-Cdd-O2d)H
                            L8: Cs-CbCb(Cds-Cdd-S2d)H
                            L8: Cs-CbCb(Cds-Cdd-Cd)H
                L5: Cs-CtCtCtH
                L5: Cs-CbCtCtH
                L5: Cs-CbCbCtH
                L5: Cs-CbCbCbH
                L5: Cs-C=SC=SCbH
                L5: Cs-C=S(Cds-Cd)(Cds-Cd)H
                    L6: Cs-C=S(Cds-Cdd)(Cds-Cds)H
                        L7: Cs-C=S(Cds-Cdd-Cd)(Cds-Cds)H
                        L7: Cs-C=S(Cds-Cdd-S2d)(Cds-Cds)H
                    L6: Cs-C=S(Cds-Cds)(Cds-Cds)H
                    L6: Cs-C=S(Cds-Cdd)(Cds-Cdd)H
                        L7: Cs-C=S(Cds-Cdd-Cd)(Cds-Cdd-Cd)H
                        L7: Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-S2d)H
                        L7: Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-Cd)H
                L5: Cs-C=S(Cds-Cd)CtH
                    L6: Cs-C=S(Cds-Cdd)CtH
                        L7: Cs-C=S(Cds-Cdd-S2d)CtH
                        L7: Cs-C=S(Cds-Cdd-Cd)CtH
                    L6: Cs-C=S(Cds-Cds)CtH
                L5: Cs-C=SC=SCtH
                L5: Cs-C=SCtCsH
                L5: Cs-C=SC=SCsH
                L5: Cs-C=S(Cds-Cd)CbH
                    L6: Cs-C=S(Cds-Cds)CbH
                    L6: Cs-C=S(Cds-Cdd)CbH
                        L7: Cs-C=S(Cds-Cdd-S2d)CbH
                        L7: Cs-C=S(Cds-Cdd-Cd)CbH
                L5: Cs-C=S(Cds-Cd)CsH
                    L6: Cs-C=S(Cds-Cds)CsH
                    L6: Cs-C=S(Cds-Cdd)CsH
                        L7: Cs-C=S(Cds-Cdd-Cd)CsH
                        L7: Cs-C=S(Cds-Cdd-S2d)CsH
                L5: Cs-CbCtC=SH
                L5: Cs-C=SC=SC=SH
                L5: Cs-C=SCsCsH
                L5: Cs-CtCtC=SH
                L5: Cs-CbCbC=SH
                L5: Cs-C=SC=S(Cds-Cd)H
                    L6: Cs-C=SC=S(Cds-Cds)H
                    L6: Cs-C=SC=S(Cds-Cdd)H
                        L7: Cs-C=SC=S(Cds-Cdd-S2d)H
                        L7: Cs-C=SC=S(Cds-Cdd-Cd)H
            L4: Cs-CCCC
                L5: Cs-CsCsCsCs
                L5: Cs-CdsCsCsCs
                    L6: Cs-(Cds-O2d)CsCsCs
                    L6: Cs-(Cds-Cd)CsCsCs
                        L7: Cs-(Cds-Cds)CsCsCs
                        L7: Cs-(Cds-Cdd)CsCsCs
                            L8: Cs-(Cds-Cdd-O2d)CsCsCs
                            L8: Cs-(Cds-Cdd-S2d)CsCsCs
                            L8: Cs-(Cds-Cdd-Cd)CsCsCs
                    L6: Cs-(CdN3d)CsCsCs
                L5: Cs-CtCsCsCs
                    L6: Cs-(CtN3t)CsCsCs
                L5: Cs-CbCsCsCs
                L5: Cs-CdsCdsCsCs
                    L6: Cs-(Cds-O2d)(Cds-O2d)CsCs
                    L6: Cs-(Cds-O2d)(Cds-Cd)CsCs
                        L7: Cs-(Cds-O2d)(Cds-Cds)CsCs
                        L7: Cs-(Cds-O2d)(Cds-Cdd)CsCs
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)CsCs
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)CsCs
                    L6: Cs-(Cds-Cd)(Cds-Cd)CsCs
                        L7: Cs-(Cds-Cds)(Cds-Cds)CsCs
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CsCs
                            L8: Cs-CsCsCd(CCO)
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cds)CsCs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CsCs
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CsCs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CsCs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CsCs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CsCs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CsCs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CsCs
                L5: Cs-CtCdsCsCs
                    L6: Cs-(Cds-O2d)CtCsCs
                    L6: Cs-(Cds-Cd)CtCsCs
                        L7: Cs-(Cds-Cds)CtCsCs
                        L7: Cs-(Cds-Cdd)CtCsCs
                            L8: Cs-(Cds-Cdd-O2d)CtCsCs
                            L8: Cs-(Cds-Cdd-S2d)CtCsCs
                            L8: Cs-(Cds-Cdd-Cd)CtCsCs
                L5: Cs-CbCdsCsCs
                    L6: Cs-(Cds-O2d)CbCsCs
                    L6: Cs-(Cds-Cd)CbCsCs
                        L7: Cs-(Cds-Cds)CbCsCs
                        L7: Cs-(Cds-Cdd)CbCsCs
                            L8: Cs-(Cds-Cdd-O2d)CbCsCs
                            L8: Cs-(Cds-Cdd-S2d)CbCsCs
                            L8: Cs-(Cds-Cdd-Cd)CbCsCs
                L5: Cs-CtCtCsCs
                    L6: Cs-(CtN3t)(CtN3t)CsCs
                L5: Cs-CbCtCsCs
                L5: Cs-CbCbCsCs
                L5: Cs-CdsCdsCdsCs
                    L6: Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)Cs
                    L6: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cd)Cs
                        L7: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)Cs
                        L7: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd)Cs
                            L8: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)Cs
                            L8: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)Cs
                    L6: Cs-(Cds-O2d)(Cds-Cd)(Cds-Cd)Cs
                        L7: Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)Cs
                        L7: Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cds)Cs
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)Cs
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cds)Cs
                        L7: Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cdd)Cs
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Cs
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)Cs
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs
                    L6: Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)Cs
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cs
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)Cs
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)Cs
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-S2d)Cs
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)Cs
                        L7: Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)Cs
                            L8: Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Cs
                            L8: Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-Cd)Cs
                            L8: Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-S2d)Cs
                            L8: Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-Cd)Cs
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)Cs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Cs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)Cs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)Cs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-Cd)Cs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs
                L5: Cs-CtCdsCdsCs
                    L6: Cs-(Cds-O2d)(Cds-O2d)CtCs
                    L6: Cs-(Cds-O2d)(Cds-Cd)CtCs
                        L7: Cs-(Cds-O2d)(Cds-Cds)CtCs
                        L7: Cs-(Cds-O2d)(Cds-Cdd)CtCs
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)CtCs
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)CtCs
                    L6: Cs-(Cds-Cd)(Cds-Cd)CtCs
                        L7: Cs-(Cds-Cds)(Cds-Cds)CtCs
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CtCs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cds)CtCs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cds)CtCs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CtCs
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CtCs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CtCs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CtCs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CtCs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CtCs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtCs
                L5: Cs-CbCdsCdsCs
                    L6: Cs-(Cds-O2d)(Cds-O2d)CbCs
                    L6: Cs-(Cds-O2d)(Cds-Cd)CbCs
                        L7: Cs-(Cds-O2d)(Cds-Cds)CbCs
                        L7: Cs-(Cds-O2d)(Cds-Cdd)CbCs
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)CbCs
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)CbCs
                    L6: Cs-(Cds-Cd)(Cds-Cd)CbCs
                        L7: Cs-(Cds-Cds)(Cds-Cds)CbCs
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CbCs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cds)CbCs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cds)CbCs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CbCs
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CbCs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CbCs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CbCs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CbCs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CbCs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbCs
                L5: Cs-CtCtCdsCs
                    L6: Cs-(Cds-O2d)CtCtCs
                    L6: Cs-(Cds-Cd)CtCtCs
                        L7: Cs-(Cds-Cds)CtCtCs
                        L7: Cs-(Cds-Cdd)CtCtCs
                            L8: Cs-(Cds-Cdd-O2d)CtCtCs
                            L8: Cs-(Cds-Cdd-S2d)CtCtCs
                            L8: Cs-(Cds-Cdd-Cd)CtCtCs
                L5: Cs-CbCtCdsCs
                    L6: Cs-(Cds-O2d)CbCtCs
                    L6: Cs-(Cds-Cd)CbCtCs
                        L7: Cs-(Cds-Cds)CbCtCs
                        L7: Cs-(Cds-Cdd)CbCtCs
                            L8: Cs-(Cds-Cdd-O2d)CbCtCs
                            L8: Cs-(Cds-Cdd-S2d)CbCtCs
                            L8: Cs-(Cds-Cdd-Cd)CbCtCs
                L5: Cs-CbCbCdsCs
                    L6: Cs-(Cds-O2d)CbCbCs
                    L6: Cs-(Cds-Cd)CbCbCs
                        L7: Cs-(Cds-Cds)CbCbCs
                        L7: Cs-(Cds-Cdd)CbCbCs
                            L8: Cs-(Cds-Cdd-O2d)CbCbCs
                            L8: Cs-(Cds-Cdd-S2d)CbCbCs
                            L8: Cs-(Cds-Cdd-Cd)CbCbCs
                L5: Cs-CtCtCtCs
                L5: Cs-CbCtCtCs
                L5: Cs-CbCbCtCs
                L5: Cs-CbCbCbCs
                L5: Cs-CdsCdsCdsCds
                    L6: Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)(Cds-O2d)
                    L6: Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)(Cds-Cd)
                        L7: Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)(Cds-Cds)
                        L7: Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)(Cds-Cdd)
                            L8: Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)
                            L8: Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)
                    L6: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cd)(Cds-Cd)
                        L7: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)(Cds-Cds)
                        L7: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd)(Cds-Cds)
                            L8: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)
                            L8: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cds)
                        L7: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd)(Cds-Cdd)
                            L8: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)
                            L8: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                    L6: Cs-(Cds-O2d)(Cds-Cd)(Cds-Cd)(Cds-Cd)
                        L7: Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cds)
                        L7: Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cdd)
                            L8: Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)
                            L8: Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)
                        L7: Cs-(Cds-O2d)(Cds-Cds)(Cds-Cdd)(Cds-Cdd)
                            L8: Cs-(Cds-O2d)(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)
                            L8: Cs-(Cds-O2d)(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-O2d)(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                        L7: Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                    L6: Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)(Cds-Cd)
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd)
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-S2d)
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)(Cds-Cdd)
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-S2d)
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                        L7: Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)
                            L8: Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)
                            L8: Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)
                            L8: Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                L5: Cs-CtCdsCdsCds
                    L6: Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)Ct
                    L6: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cd)Ct
                        L7: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)Ct
                        L7: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd)Ct
                            L8: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)Ct
                            L8: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)Ct
                    L6: Cs-(Cds-O2d)(Cds-Cd)(Cds-Cd)Ct
                        L7: Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)Ct
                        L7: Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cds)Ct
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)Ct
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cds)Ct
                        L7: Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cdd)Ct
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Ct
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)Ct
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct
                    L6: Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)Ct
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Ct
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)Ct
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)Ct
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-S2d)Ct
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)Ct
                        L7: Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)Ct
                            L8: Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Ct
                            L8: Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-Cd)Ct
                            L8: Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-S2d)Ct
                            L8: Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-Cd)Ct
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)Ct
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Ct
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)Ct
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)Ct
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-Cd)Ct
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct
                L5: Cs-CbCdsCdsCds
                    L6: Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)Cb
                    L6: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cd)Cb
                        L7: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)Cb
                        L7: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd)Cb
                            L8: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)Cb
                            L8: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)Cb
                    L6: Cs-(Cds-O2d)(Cds-Cd)(Cds-Cd)Cb
                        L7: Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)Cb
                        L7: Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cds)Cb
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)Cb
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cds)Cb
                        L7: Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cdd)Cb
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Cb
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)Cb
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb
                    L6: Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)Cb
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cb
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)Cb
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)Cb
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-S2d)Cb
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)Cb
                        L7: Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)Cb
                            L8: Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Cb
                            L8: Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-Cd)Cb
                            L8: Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-S2d)Cb
                            L8: Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-Cd)Cb
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)Cb
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Cb
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)Cb
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)Cb
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-Cd)Cb
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb
                L5: Cs-CtCtCdsCds
                    L6: Cs-(Cds-O2d)(Cds-O2d)CtCt
                    L6: Cs-(Cds-O2d)(Cds-Cd)CtCt
                        L7: Cs-(Cds-O2d)(Cds-Cds)CtCt
                        L7: Cs-(Cds-O2d)(Cds-Cdd)CtCt
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)CtCt
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)CtCt
                    L6: Cs-(Cds-Cd)(Cds-Cd)CtCt
                        L7: Cs-(Cds-Cds)(Cds-Cds)CtCt
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CtCt
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cds)CtCt
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cds)CtCt
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CtCt
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CtCt
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CtCt
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CtCt
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CtCt
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CtCt
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtCt
                L5: Cs-CbCtCdsCds
                    L6: Cs-(Cds-O2d)(Cds-O2d)CbCt
                    L6: Cs-(Cds-O2d)(Cds-Cd)CbCt
                        L7: Cs-(Cds-O2d)(Cds-Cds)CbCt
                        L7: Cs-(Cds-O2d)(Cds-Cdd)CbCt
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)CbCt
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)CbCt
                    L6: Cs-(Cds-Cd)(Cds-Cd)CbCt
                        L7: Cs-(Cds-Cds)(Cds-Cds)CbCt
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CbCt
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cds)CbCt
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cds)CbCt
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CbCt
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CbCt
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CbCt
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CbCt
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CbCt
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CbCt
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbCt
                L5: Cs-CbCbCdsCds
                    L6: Cs-(Cds-O2d)(Cds-O2d)CbCb
                    L6: Cs-(Cds-O2d)(Cds-Cd)CbCb
                        L7: Cs-(Cds-O2d)(Cds-Cds)CbCb
                        L7: Cs-(Cds-O2d)(Cds-Cdd)CbCb
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)CbCb
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)CbCb
                    L6: Cs-(Cds-Cd)(Cds-Cd)CbCb
                        L7: Cs-(Cds-Cds)(Cds-Cds)CbCb
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CbCb
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cds)CbCb
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cds)CbCb
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CbCb
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CbCb
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CbCb
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CbCb
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CbCb
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CbCb
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbCb
                L5: Cs-CtCtCtCds
                    L6: Cs-(Cds-O2d)CtCtCt
                    L6: Cs-(Cds-Cd)CtCtCt
                        L7: Cs-(Cds-Cds)CtCtCt
                        L7: Cs-(Cds-Cdd)CtCtCt
                            L8: Cs-(Cds-Cdd-O2d)CtCtCt
                            L8: Cs-(Cds-Cdd-S2d)CtCtCt
                            L8: Cs-(Cds-Cdd-Cd)CtCtCt
                L5: Cs-CbCtCtCds
                    L6: Cs-(Cds-O2d)CbCtCt
                    L6: Cs-(Cds-Cd)CbCtCt
                        L7: Cs-(Cds-Cds)CbCtCt
                        L7: Cs-(Cds-Cdd)CbCtCt
                            L8: Cs-(Cds-Cdd-O2d)CbCtCt
                            L8: Cs-(Cds-Cdd-S2d)CbCtCt
                            L8: Cs-(Cds-Cdd-Cd)CbCtCt
                L5: Cs-CbCbCtCds
                    L6: Cs-(Cds-O2d)CbCbCt
                    L6: Cs-(Cds-Cd)CbCbCt
                        L7: Cs-(Cds-Cds)CbCbCt
                        L7: Cs-(Cds-Cdd)CbCbCt
                            L8: Cs-(Cds-Cdd-O2d)CbCbCt
                            L8: Cs-(Cds-Cdd-S2d)CbCbCt
                            L8: Cs-(Cds-Cdd-Cd)CbCbCt
                L5: Cs-CbCbCbCds
                    L6: Cs-(Cds-O2d)CbCbCb
                    L6: Cs-(Cds-Cd)CbCbCb
                        L7: Cs-(Cds-Cds)CbCbCb
                        L7: Cs-(Cds-Cdd)CbCbCb
                            L8: Cs-(Cds-Cdd-O2d)CbCbCb
                            L8: Cs-(Cds-Cdd-S2d)CbCbCb
                            L8: Cs-(Cds-Cdd-Cd)CbCbCb
                L5: Cs-CtCtCtCt
                L5: Cs-CbCtCtCt
                L5: Cs-CbCbCtCt
                L5: Cs-CbCbCbCt
                L5: Cs-CbCbCbCb
                L5: Cs-C=SCbCtCt
                L5: Cs-C=S(Cds-Cd)(Cds-Cd)(Cds-Cd)
                    L6: Cs-C=S(Cds-Cds)(Cds-Cds)(Cds-Cdd)
                        L7: Cs-C=S(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)
                        L7: Cs-C=S(Cds-Cds)(Cds-Cds)(Cds-Cdd-S2d)
                    L6: Cs-C=S(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)
                        L7: Cs-C=S(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                        L7: Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                        L7: Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)
                        L7: Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-Cd)
                    L6: Cs-C=S(Cds-Cds)(Cds-Cds)(Cds-Cds)
                    L6: Cs-C=S(Cds-Cds)(Cds-Cdd)(Cds-Cdd)
                        L7: Cs-C=S(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-S2d)
                        L7: Cs-C=S(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-Cd)
                        L7: Cs-C=S(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                L5: Cs-C=S(Cds-Cd)CtCt
                    L6: Cs-C=S(Cds-Cds)CtCt
                    L6: Cs-C=S(Cds-Cdd)CtCt
                        L7: Cs-C=S(Cds-Cdd-S2d)CtCt
                        L7: Cs-C=S(Cds-Cdd-Cd)CtCt
                L5: Cs-C=S(Cds-Cd)CtCs
                    L6: Cs-C=S(Cds-Cds)CtCs
                    L6: Cs-C=S(Cds-Cdd)CtCs
                        L7: Cs-C=S(Cds-Cdd-S2d)CtCs
                        L7: Cs-C=S(Cds-Cdd-Cd)CtCs
                L5: Cs-C=SCbCbCt
                L5: Cs-C=SCbCsCs
                L5: Cs-C=SCbCbCs
                L5: Cs-C=SCtCtCt
                L5: Cs-C=S(Cds-Cd)(Cds-Cd)Cs
                    L6: Cs-C=S(Cds-Cdd)(Cds-Cdd)Cs
                        L7: Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-Cd)Cs
                        L7: Cs-C=S(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs
                        L7: Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-S2d)Cs
                    L6: Cs-C=S(Cds-Cds)(Cds-Cds)Cs
                    L6: Cs-C=S(Cds-Cdd)(Cds-Cds)Cs
                        L7: Cs-C=S(Cds-Cdd-S2d)(Cds-Cds)Cs
                        L7: Cs-C=S(Cds-Cdd-Cd)(Cds-Cds)Cs
                L5: Cs-C=SC=SCtCt
                L5: Cs-C=SCsCsCs
                L5: Cs-C=SCtCtCs
                L5: Cs-C=SC=SC=SCt
                L5: Cs-C=SC=SC=SCs
                L5: Cs-C=SC=SC=SC=S
                L5: Cs-C=SCtCsCs
                L5: Cs-C=SC=SC=SCb
                L5: Cs-C=SC=SC=S(Cds-Cd)
                    L6: Cs-C=SC=SC=S(Cds-Cdd)
                        L7: Cs-C=SC=SC=S(Cds-Cdd-Cd)
                        L7: Cs-C=SC=SC=S(Cds-Cdd-S2d)
                    L6: Cs-C=SC=SC=S(Cds-Cds)
                L5: Cs-C=S(Cds-Cd)(Cds-Cd)Ct
                    L6: Cs-C=S(Cds-Cdd)(Cds-Cdd)Ct
                        L7: Cs-C=S(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct
                        L7: Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-S2d)Ct
                        L7: Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-Cd)Ct
                    L6: Cs-C=S(Cds-Cds)(Cds-Cds)Ct
                    L6: Cs-C=S(Cds-Cdd)(Cds-Cds)Ct
                        L7: Cs-C=S(Cds-Cdd-Cd)(Cds-Cds)Ct
                        L7: Cs-C=S(Cds-Cdd-S2d)(Cds-Cds)Ct
                L5: Cs-C=SC=SCtCs
                L5: Cs-C=SC=SCbCb
                L5: Cs-C=S(Cds-Cd)CsCs
                    L6: Cs-C=S(Cds-Cds)CsCs
                    L6: Cs-C=S(Cds-Cdd)CsCs
                        L7: Cs-C=S(Cds-Cdd-Cd)CsCs
                        L7: Cs-C=S(Cds-Cdd-S2d)CsCs
                L5: Cs-C=SC=SCbCt
                L5: Cs-C=S(Cds-Cd)CbCt
                    L6: Cs-C=S(Cds-Cds)CbCt
                    L6: Cs-C=S(Cds-Cdd)CbCt
                        L7: Cs-C=S(Cds-Cdd-S2d)CbCt
                        L7: Cs-C=S(Cds-Cdd-Cd)CbCt
                L5: Cs-C=SC=SCsCs
                L5: Cs-C=S(Cds-Cd)CbCb
                    L6: Cs-C=S(Cds-Cds)CbCb
                    L6: Cs-C=S(Cds-Cdd)CbCb
                        L7: Cs-C=S(Cds-Cdd-S2d)CbCb
                        L7: Cs-C=S(Cds-Cdd-Cd)CbCb
                L5: Cs-C=SC=S(Cds-Cd)Ct
                    L6: Cs-C=SC=S(Cds-Cds)Ct
                    L6: Cs-C=SC=S(Cds-Cdd)Ct
                        L7: Cs-C=SC=S(Cds-Cdd-Cd)Ct
                        L7: Cs-C=SC=S(Cds-Cdd-S2d)Ct
                L5: Cs-C=SC=S(Cds-Cd)Cs
                    L6: Cs-C=SC=S(Cds-Cds)Cs
                    L6: Cs-C=SC=S(Cds-Cdd)Cs
                        L7: Cs-C=SC=S(Cds-Cdd-S2d)Cs
                        L7: Cs-C=SC=S(Cds-Cdd-Cd)Cs
                L5: Cs-C=SC=S(Cds-Cd)(Cds-Cd)
                    L6: Cs-C=SC=S(Cds-Cdd)(Cds-Cds)
                        L7: Cs-C=SC=S(Cds-Cdd-S2d)(Cds-Cds)
                        L7: Cs-C=SC=S(Cds-Cdd-Cd)(Cds-Cds)
                    L6: Cs-C=SC=S(Cds-Cdd)(Cds-Cdd)
                        L7: Cs-C=SC=S(Cds-Cdd-S2d)(Cds-Cdd-S2d)
                        L7: Cs-C=SC=S(Cds-Cdd-S2d)(Cds-Cdd-Cd)
                        L7: Cs-C=SC=S(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                    L6: Cs-C=SC=S(Cds-Cds)(Cds-Cds)
                L5: Cs-C=SC=S(Cds-Cd)Cb
                    L6: Cs-C=SC=S(Cds-Cdd)Cb
                        L7: Cs-C=SC=S(Cds-Cdd-S2d)Cb
                        L7: Cs-C=SC=S(Cds-Cdd-Cd)Cb
                    L6: Cs-C=SC=S(Cds-Cds)Cb
                L5: Cs-C=SCbCtCs
                L5: Cs-C=S(Cds-Cd)CbCs
                    L6: Cs-C=S(Cds-Cds)CbCs
                    L6: Cs-C=S(Cds-Cdd)CbCs
                        L7: Cs-C=S(Cds-Cdd-S2d)CbCs
                        L7: Cs-C=S(Cds-Cdd-Cd)CbCs
                L5: Cs-C=S(Cds-Cd)(Cds-Cd)Cb
                    L6: Cs-C=S(Cds-Cdd)(Cds-Cdd)Cb
                        L7: Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-Cd)Cb
                        L7: Cs-C=S(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb
                        L7: Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-S2d)Cb
                    L6: Cs-C=S(Cds-Cds)(Cds-Cds)Cb
                    L6: Cs-C=S(Cds-Cdd)(Cds-Cds)Cb
                        L7: Cs-C=S(Cds-Cdd-S2d)(Cds-Cds)Cb
                        L7: Cs-C=S(Cds-Cdd-Cd)(Cds-Cds)Cb
                L5: Cs-C=SCbCbCb
                L5: Cs-C=SC=SCbCs
            L4: Cs-CCCOs
                L5: Cs-CsCsCsOs
                L5: Cs-CdsCsCsOs
                    L6: Cs-(Cds-O2d)CsCsOs
                    L6: Cs-(Cds-Cd)CsCsOs
                        L7: Cs-(Cds-Cds)CsCsOs
                        L7: Cs-(Cds-Cdd)CsCsOs
                            L8: Cs-(Cds-Cdd-O2d)CsCsOs
                            L8: Cs-(Cds-Cdd-Cd)CsCsOs
                L5: Cs-OsCtCsCs
                L5: Cs-CbCsCsOs
                L5: Cs-CdsCdsCsOs
                    L6: Cs-(Cds-O2d)(Cds-O2d)CsOs
                    L6: Cs-(Cds-O2d)(Cds-Cd)CsOs
                        L7: Cs-(Cds-O2d)(Cds-Cds)CsOs
                        L7: Cs-(Cds-O2d)(Cds-Cdd)CsOs
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)CsOs
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)CsOs
                    L6: Cs-(Cds-Cd)(Cds-Cd)CsOs
                        L7: Cs-(Cds-Cds)(Cds-Cds)CsOs
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CsOs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cds)CsOs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CsOs
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CsOs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CsOs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CsOs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CsOs
                L5: Cs-CtCdsCsOs
                    L6: Cs-(Cds-O2d)CtCsOs
                    L6: Cs-(Cds-Cd)CtCsOs
                        L7: Cs-(Cds-Cds)CtCsOs
                        L7: Cs-(Cds-Cdd)CtCsOs
                            L8: Cs-(Cds-Cdd-O2d)CtCsOs
                            L8: Cs-(Cds-Cdd-Cd)CtCsOs
                L5: Cs-CbCdsCsOs
                    L6: Cs-(Cds-O2d)CbCsOs
                    L6: Cs-(Cds-Cd)CbCsOs
                        L7: Cs-(Cds-Cds)CbCsOs
                        L7: Cs-(Cds-Cdd)CbCsOs
                            L8: Cs-(Cds-Cdd-O2d)CbCsOs
                            L8: Cs-(Cds-Cdd-Cd)CbCsOs
                L5: Cs-CtCtCsOs
                L5: Cs-CbCtCsOs
                L5: Cs-CbCbCsOs
                L5: Cs-CdsCdsCdsOs
                    L6: Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)O2s
                    L6: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cd)O2s
                        L7: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)O2s
                        L7: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd)O2s
                            L8: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)O2s
                            L8: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)O2s
                    L6: Cs-(Cds-O2d)(Cds-Cd)(Cds-Cd)O2s
                        L7: Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)O2s
                        L7: Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cds)O2s
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)O2s
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cds)O2s
                        L7: Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cdd)O2s
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)O2s
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)O2s
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)O2s
                    L6: Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)O2s
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)O2s
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)O2s
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)O2s
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)O2s
                        L7: Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)O2s
                            L8: Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)O2s
                            L8: Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-Cd)O2s
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)O2s
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)O2s
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)O2s
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)O2s
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)O2s
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)O2s
                L5: Cs-CtCdsCdsOs
                    L6: Cs-(Cds-O2d)(Cds-O2d)CtOs
                    L6: Cs-(Cds-O2d)(Cds-Cd)CtOs
                        L7: Cs-(Cds-O2d)(Cds-Cds)CtOs
                        L7: Cs-(Cds-O2d)(Cds-Cdd)CtOs
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)CtOs
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)CtOs
                    L6: Cs-(Cds-Cd)(Cds-Cd)CtOs
                        L7: Cs-(Cds-Cds)(Cds-Cds)CtOs
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CtOs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cds)CtOs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CtOs
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CtOs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CtOs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CtOs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtOs
                L5: Cs-CbCdsCdsOs
                    L6: Cs-(Cds-O2d)(Cds-O2d)CbOs
                    L6: Cs-(Cds-O2d)(Cds-Cd)CbOs
                        L7: Cs-(Cds-O2d)(Cds-Cds)CbOs
                        L7: Cs-(Cds-O2d)(Cds-Cdd)CbOs
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)CbOs
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)CbOs
                    L6: Cs-(Cds-Cd)(Cds-Cd)CbOs
                        L7: Cs-(Cds-Cds)(Cds-Cds)CbOs
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CbOs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cds)CbOs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CbOs
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CbOs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CbOs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CbOs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbOs
                L5: Cs-CtCtCdsOs
                    L6: Cs-(Cds-O2d)CtCtOs
                    L6: Cs-(Cds-Cd)CtCtOs
                        L7: Cs-(Cds-Cds)CtCtOs
                        L7: Cs-(Cds-Cdd)CtCtOs
                            L8: Cs-(Cds-Cdd-O2d)CtCtOs
                            L8: Cs-(Cds-Cdd-Cd)CtCtOs
                L5: Cs-CbCtCdsOs
                    L6: Cs-(Cds-O2d)CbCtOs
                    L6: Cs-(Cds-Cd)CbCtOs
                        L7: Cs-(Cds-Cds)CbCtOs
                        L7: Cs-(Cds-Cdd)CbCtOs
                            L8: Cs-(Cds-Cdd-O2d)CbCtOs
                            L8: Cs-(Cds-Cdd-Cd)CbCtOs
                L5: Cs-CbCbCdsOs
                    L6: Cs-(Cds-O2d)CbCbOs
                    L6: Cs-(Cds-Cd)CbCbOs
                        L7: Cs-(Cds-Cds)CbCbOs
                        L7: Cs-(Cds-Cdd)CbCbOs
                            L8: Cs-(Cds-Cdd-O2d)CbCbOs
                            L8: Cs-(Cds-Cdd-Cd)CbCbOs
                L5: Cs-CtCtCtOs
                L5: Cs-CbCtCtOs
                L5: Cs-CbCbCtOs
                L5: Cs-CbCbCbOs
            L4: Cs-CCOsOs
                L5: Cs-CsCsOsOs
                L5: Cs-CdsCsOsOs
                    L6: Cs-(Cds-O2d)CsOsOs
                    L6: Cs-(Cds-Cd)CsOsOs
                        L7: Cs-(Cds-Cds)CsOsOs
                        L7: Cs-(Cds-Cdd)CsOsOs
                            L8: Cs-(Cds-Cdd-O2d)CsOsOs
                            L8: Cs-(Cds-Cdd-Cd)CsOsOs
                L5: Cs-CdsCdsOsOs
                    L6: Cs-(Cds-O2d)(Cds-O2d)OsOs
                    L6: Cs-(Cds-O2d)(Cds-Cd)OsOs
                        L7: Cs-(Cds-O2d)(Cds-Cds)OsOs
                        L7: Cs-(Cds-O2d)(Cds-Cdd)OsOs
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)OsOs
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)OsOs
                    L6: Cs-(Cds-Cd)(Cds-Cd)OsOs
                        L7: Cs-(Cds-Cds)(Cds-Cds)OsOs
                        L7: Cs-(Cds-Cdd)(Cds-Cds)OsOs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cds)OsOs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)OsOs
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)OsOs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)OsOs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)OsOs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)OsOs
                L5: Cs-CtCsOsOs
                L5: Cs-CtCdsOsOs
                    L6: Cs-(Cds-O2d)CtOsOs
                    L6: Cs-(Cds-Cd)CtOsOs
                        L7: Cs-(Cds-Cds)CtOsOs
                        L7: Cs-(Cds-Cdd)CtOsOs
                            L8: Cs-(Cds-Cdd-O2d)CtOsOs
                            L8: Cs-(Cds-Cdd-Cd)CtOsOs
                L5: Cs-CtCtOsOs
                L5: Cs-CbCsOsOs
                L5: Cs-CbCdsOsOs
                    L6: Cs-(Cds-O2d)CbOsOs
                    L6: Cs-(Cds-Cd)CbOsOs
                        L7: Cs-(Cds-Cds)CbOsOs
                        L7: Cs-(Cds-Cdd)CbOsOs
                            L8: Cs-(Cds-Cdd-O2d)CbOsOs
                            L8: Cs-(Cds-Cdd-Cd)CbOsOs
                L5: Cs-CbCtOsOs
                L5: Cs-CbCbOsOs
            L4: Cs-COsOsOs
                L5: Cs-CsOsOsOs
                L5: Cs-CdsOsOsOs
                    L6: Cs-(Cds-O2d)OsOsOs
                    L6: Cs-(Cds-Cd)OsOsOs
                        L7: Cs-(Cds-Cds)OsOsOs
                        L7: Cs-(Cds-Cdd)OsOsOs
                            L8: Cs-(Cds-Cdd-O2d)OsOsOs
                            L8: Cs-(Cds-Cdd-Cd)OsOsOs
                L5: Cs-CtOsOsOs
                L5: Cs-CbOsOsOs
            L4: Cs-OsOsOsOs
            L4: Cs-COsOsH
                L5: Cs-CsOsOsH
                L5: Cs-CdsOsOsH
                    L6: Cs-(Cds-O2d)OsOsH
                    L6: Cs-(Cds-Cd)OsOsH
                        L7: Cs-(Cds-Cds)OsOsH
                        L7: Cs-(Cds-Cdd)OsOsH
                            L8: Cs-(Cds-Cdd-O2d)OsOsH
                            L8: Cs-(Cds-Cdd-Cd)OsOsH
                L5: Cs-CtOsOsH
                L5: Cs-CbOsOsH
            L4: Cs-COsSH
                L5: Cs-CsOsSH
                    L6: Cs-CsOsS2H
                    L6: Cs-CsOsS4H
                L5: Cs-CdsOsSsH
                L5: Cs-CtOsSsH
                L5: Cs-CbOsSsH
            L4: Cs-CCOsSs
                L5: Cs-CsCsOsSs
            L4: Cs-COsOsSs
                L5: Cs-CsOsOsSs
            L4: Cs-CCOsH
                L5: Cs-CsCsOsH
                L5: Cs-CdsCsOsH
                    L6: Cs-(Cds-O2d)CsOsH
                    L6: Cs-(Cds-Cd)CsOsH
                        L7: Cs-(Cds-Cds)CsOsH
                        L7: Cs-(Cds-Cdd)CsOsH
                            L8: Cs-(Cds-Cdd-O2d)CsOsH
                            L8: Cs-(Cds-Cdd-Cd)CsOsH
                L5: Cs-CdsCdsOsH
                    L6: Cs-(Cds-O2d)(Cds-O2d)OsH
                    L6: Cs-(Cds-O2d)(Cds-Cd)OsH
                        L7: Cs-(Cds-O2d)(Cds-Cds)OsH
                        L7: Cs-(Cds-O2d)(Cds-Cdd)OsH
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)OsH
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)OsH
                    L6: Cs-(Cds-Cd)(Cds-Cd)OsH
                        L7: Cs-(Cds-Cds)(Cds-Cds)OsH
                        L7: Cs-(Cds-Cdd)(Cds-Cds)OsH
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cds)OsH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)OsH
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)OsH
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)OsH
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)OsH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)OsH
                L5: Cs-CtCsOsH
                L5: Cs-CtCdsOsH
                    L6: Cs-(Cds-O2d)CtOsH
                    L6: Cs-(Cds-Cd)CtOsH
                        L7: Cs-(Cds-Cds)CtOsH
                        L7: Cs-(Cds-Cdd)CtOsH
                            L8: Cs-(Cds-Cdd-O2d)CtOsH
                            L8: Cs-(Cds-Cdd-Cd)CtOsH
                L5: Cs-CtCtOsH
                L5: Cs-CbCsOsH
                L5: Cs-CbCdsOsH
                    L6: Cs-(Cds-O2d)CbOsH
                    L6: Cs-(Cds-Cd)CbOsH
                        L7: Cs-(Cds-Cds)CbOsH
                        L7: Cs-(Cds-Cdd)CbOsH
                            L8: Cs-(Cds-Cdd-O2d)CbOsH
                            L8: Cs-(Cds-Cdd-Cd)CbOsH
                L5: Cs-CbCtOsH
                L5: Cs-CbCbOsH
            L4: Cs-COsHH
                L5: Cs-CsOsHH
                L5: Cs-CdsOsHH
                    L6: Cs-(Cds-O2d)OsHH
                    L6: Cs-(Cds-Cd)OsHH
                        L7: Cs-(Cds-Cds)OsHH
                        L7: Cs-(Cds-Cdd)OsHH
                            L8: Cs-(Cds-Cdd-O2d)OsHH
                            L8: Cs-(Cds-Cdd-Cd)OsHH
                L5: Cs-CtOsHH
                L5: Cs-CbOsHH
            L4: Cs-CCCS
                L5: Cs-CsCsCsS
                    L6: Cs-CsCsCsS2
                    L6: Cs-CsCsCsS4
                L5: Cs-CdsCsCsSs
                    L6: Cs-(Cds-Cd)CsCsSs
                        L7: Cs-(Cds-Cds)CsCsSs
                        L7: Cs-(Cds-Cdd)CsCsSs
                            L8: Cs-(Cds-Cdd-S2d)CsCsSs
                            L8: Cs-(Cds-Cdd-Cd)CsCsSs
                L5: Cs-SsCtCsCs
                L5: Cs-CbCsCsSs
                L5: Cs-CdsCdsCsSs
                    L6: Cs-(Cds-Cd)(Cds-Cd)CsSs
                        L7: Cs-(Cds-Cds)(Cds-Cds)CsSs
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CsSs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cds)CsSs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CsSs
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CsSs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CsSs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CsSs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CsSs
                L5: Cs-CtCdsCsSs
                    L6: Cs-(Cds-Cd)CtCsSs
                        L7: Cs-(Cds-Cds)CtCsSs
                        L7: Cs-(Cds-Cdd)CtCsSs
                            L8: Cs-(Cds-Cdd-S2d)CtCsSs
                            L8: Cs-(Cds-Cdd-Cd)CtCsSs
                L5: Cs-CbCdsCsSs
                    L6: Cs-(Cds-Cd)CbCsSs
                        L7: Cs-(Cds-Cds)CbCsSs
                        L7: Cs-(Cds-Cdd)CbCsSs
                            L8: Cs-(Cds-Cdd-S2d)CbCsSs
                            L8: Cs-(Cds-Cdd-Cd)CbCsSs
                L5: Cs-CtCtCsSs
                L5: Cs-CbCtCsSs
                L5: Cs-CbCbCsSs
                L5: Cs-CdsCdsCdsSs
                    L6: Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)S2s
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)S2s
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)S2s
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-S2d)S2s
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)S2s
                        L7: Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)S2s
                            L8: Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-S2d)S2s
                            L8: Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-Cd)S2s
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)S2s
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)S2s
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)S2s
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-Cd)S2s
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)S2s
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)S2s
                L5: Cs-CtCdsCdsSs
                    L6: Cs-(Cds-Cd)(Cds-Cd)CtSs
                        L7: Cs-(Cds-Cds)(Cds-Cds)CtSs
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CtSs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cds)CtSs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CtSs
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CtSs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CtSs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CtSs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtSs
                L5: Cs-CbCdsCdsSs
                    L6: Cs-(Cds-Cd)(Cds-Cd)CbSs
                        L7: Cs-(Cds-Cds)(Cds-Cds)CbSs
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CbSs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cds)CbSs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CbSs
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CbSs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CbSs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CbSs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbSs
                L5: Cs-CtCtCdsSs
                    L6: Cs-(Cds-Cd)CtCtSs
                        L7: Cs-(Cds-Cds)CtCtSs
                        L7: Cs-(Cds-Cdd)CtCtSs
                            L8: Cs-(Cds-Cdd-S2d)CtCtSs
                            L8: Cs-(Cds-Cdd-Cd)CtCtSs
                L5: Cs-CbCtCdsSs
                    L6: Cs-(Cds-Cd)CbCtSs
                        L7: Cs-(Cds-Cds)CbCtSs
                        L7: Cs-(Cds-Cdd)CbCtSs
                            L8: Cs-(Cds-Cdd-S2d)CbCtSs
                            L8: Cs-(Cds-Cdd-Cd)CbCtSs
                L5: Cs-CbCbCdsSs
                    L6: Cs-(Cds-Cd)CbCbSs
                        L7: Cs-(Cds-Cds)CbCbSs
                        L7: Cs-(Cds-Cdd)CbCbSs
                            L8: Cs-(Cds-Cdd-S2d)CbCbSs
                            L8: Cs-(Cds-Cdd-Cd)CbCbSs
                L5: Cs-CtCtCtSs
                L5: Cs-CbCtCtSs
                L5: Cs-CbCbCtSs
                L5: Cs-CbCbCbSs
                L5: Cs-C=SCbCsSs
                L5: Cs-C=SCsCsSs
                L5: Cs-C=S(Cds-Cd)(Cds-Cd)S2s
                    L6: Cs-C=S(Cds-Cdd)(Cds-Cdd)S2s
                        L7: Cs-C=S(Cds-Cdd-Cd)(Cds-Cdd-Cd)S2s
                        L7: Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-Cd)S2s
                        L7: Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-S2d)S2s
                    L6: Cs-C=S(Cds-Cdd)(Cds-Cds)S2s
                        L7: Cs-C=S(Cds-Cdd-Cd)(Cds-Cds)S2s
                        L7: Cs-C=S(Cds-Cdd-S2d)(Cds-Cds)S2s
                    L6: Cs-C=S(Cds-Cds)(Cds-Cds)S2s
                L5: Cs-C=S(Cds-Cd)CtSs
                    L6: Cs-C=S(Cds-Cds)CtSs
                    L6: Cs-C=S(Cds-Cdd)CtSs
                        L7: Cs-C=S(Cds-Cdd-S2d)CtSs
                        L7: Cs-C=S(Cds-Cdd-Cd)CtSs
                L5: Cs-C=SCtCsSs
                L5: Cs-C=SC=SC=SSs
                L5: Cs-C=SC=S(Cds-Cd)S2s
                    L6: Cs-C=SC=S(Cds-Cds)S2s
                    L6: Cs-C=SC=S(Cds-Cdd)S2s
                        L7: Cs-C=SC=S(Cds-Cdd-S2d)S2s
                        L7: Cs-C=SC=S(Cds-Cdd-Cd)S2s
                L5: Cs-C=SCbCbSs
                L5: Cs-C=SC=SCbSs
                L5: Cs-C=SC=SCsSs
                L5: Cs-C=SCtCtSs
                L5: Cs-C=S(Cds-Cd)CbSs
                    L6: Cs-C=S(Cds-Cdd)CbSs
                        L7: Cs-C=S(Cds-Cdd-Cd)CbSs
                        L7: Cs-C=S(Cds-Cdd-S2d)CbSs
                    L6: Cs-C=S(Cds-Cds)CbSs
                L5: Cs-C=SCbCtSs
                L5: Cs-C=SC=SCtSs
                L5: Cs-C=S(Cds-Cd)CsSs
                    L6: Cs-C=S(Cds-Cds)CsSs
                    L6: Cs-C=S(Cds-Cdd)CsSs
                        L7: Cs-C=S(Cds-Cdd-S2d)CsSs
                        L7: Cs-C=S(Cds-Cdd-Cd)CsSs
            L4: Cs-CCSS
                L5: Cs-CsCsSS
                    L6: Cs-CsCsS2S2
                    L6: Cs-CsCsS6S2
                L5: Cs-CdsCsSsSs
                    L6: Cs-(Cds-Cd)CsSsSs
                        L7: Cs-(Cds-Cds)CsSsSs
                        L7: Cs-(Cds-Cdd)CsSsSs
                            L8: Cs-(Cds-Cdd-S2d)CsSsSs
                            L8: Cs-(Cds-Cdd-Cd)CsSsSs
                L5: Cs-CdsCdsSsSs
                    L6: Cs-(Cds-Cd)(Cds-Cd)SsSs
                        L7: Cs-(Cds-Cds)(Cds-Cds)SsSs
                        L7: Cs-(Cds-Cdd)(Cds-Cds)SsSs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cds)SsSs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)SsSs
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)SsSs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)SsSs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)SsSs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)SsSs
                L5: Cs-CtCsSsSs
                L5: Cs-CtCdsSsSs
                    L6: Cs-(Cds-Cd)CtSsSs
                        L7: Cs-(Cds-Cds)CtSsSs
                        L7: Cs-(Cds-Cdd)CtSsSs
                            L8: Cs-(Cds-Cdd-S2d)CtSsSs
                            L8: Cs-(Cds-Cdd-Cd)CtSsSs
                L5: Cs-CtCtSsSs
                L5: Cs-CbCsSsSs
                L5: Cs-CbCdsSsSs
                    L6: Cs-(Cds-Cd)CbSsSs
                        L7: Cs-(Cds-Cds)CbSsSs
                        L7: Cs-(Cds-Cdd)CbSsSs
                            L8: Cs-(Cds-Cdd-S2d)CbSsSs
                            L8: Cs-(Cds-Cdd-Cd)CbSsSs
                L5: Cs-CbCtSsSs
                L5: Cs-CbCbSsSs
                L5: Cs-C=SCsSsSs
                L5: Cs-C=S(Cds-Cd)SsSs
                    L6: Cs-C=S(Cds-Cdd)SsSs
                        L7: Cs-C=S(Cds-Cdd-Cd)SsSs
                        L7: Cs-C=S(Cds-Cdd-S2d)SsSs
                    L6: Cs-C=S(Cds-Cds)SsSs
                L5: Cs-C=SC=SSsSs
                L5: Cs-C=SCbSsSs
                L5: Cs-C=SCtSsSs
            L4: Cs-CSsSsSs
                L5: Cs-CsSsSsSs
                L5: Cs-CdsSsSsSs
                    L6: Cs-(Cds-Cd)SsSsSs
                        L7: Cs-(Cds-Cds)SsSsSs
                        L7: Cs-(Cds-Cdd)SsSsSs
                            L8: Cs-(Cds-Cdd-S2d)SsSsSs
                            L8: Cs-(Cds-Cdd-Cd)SsSsSs
                L5: Cs-CtSsSsSs
                L5: Cs-CbSsSsSs
                L5: Cs-C=SSsSsSs
            L4: Cs-SsSsSsSs
            L4: Cs-CSSH
                L5: Cs-CsSSH
                    L6: Cs-CsS2S2H
                    L6: Cs-CsS4S2H
                    L6: Cs-CsS6S2H
                L5: Cs-CdsSsSsH
                    L6: Cs-(Cds-Cd)SsSsH
                        L7: Cs-(Cds-Cds)SsSsH
                        L7: Cs-(Cds-Cdd)SsSsH
                            L8: Cs-(Cds-Cdd-S2d)SsSsH
                            L8: Cs-(Cds-Cdd-Cd)SsSsH
                L5: Cs-CtSsSsH
                L5: Cs-CbSsSsH
                L5: Cs-C=SSsSsH
            L4: Cs-CCSH
                L5: Cs-CsCsSH
                    L6: Cs-CsCsS2H
                    L6: Cs-CsCsS4H
                    L6: Cs-CsCsS6H
                L5: Cs-CdsCsSH
                    L6: Cs-CdsCsS4H
                    L6: Cs-(Cds-Cd)CsSsH
                        L7: Cs-(Cds-Cds)CsSsH
                        L7: Cs-(Cds-Cdd)CsSsH
                            L8: Cs-(Cds-Cdd-S2d)CsSsH
                            L8: Cs-(Cds-Cdd-Cd)CsSsH
                L5: Cs-CdsCdsSsH
                    L6: Cs-(Cds-Cd)(Cds-Cd)SsH
                        L7: Cs-(Cds-Cds)(Cds-Cds)SsH
                        L7: Cs-(Cds-Cdd)(Cds-Cds)SsH
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cds)SsH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)SsH
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)SsH
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)SsH
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)SsH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)SsH
                L5: Cs-CtCsSsH
                L5: Cs-CtCdsSsH
                    L6: Cs-(Cds-Cd)CtSsH
                        L7: Cs-(Cds-Cds)CtSsH
                        L7: Cs-(Cds-Cdd)CtSsH
                            L8: Cs-(Cds-Cdd-S2d)CtSsH
                            L8: Cs-(Cds-Cdd-Cd)CtSsH
                L5: Cs-CtCtSsH
                L5: Cs-CbCsSsH
                L5: Cs-CbCdsSsH
                    L6: Cs-(Cds-Cd)CbSsH
                        L7: Cs-(Cds-Cds)CbSsH
                        L7: Cs-(Cds-Cdd)CbSsH
                            L8: Cs-(Cds-Cdd-S2d)CbSsH
                            L8: Cs-(Cds-Cdd-Cd)CbSsH
                L5: Cs-CbCtSsH
                L5: Cs-CbCbSsH
                L5: Cs-C=SCbSsH
                L5: Cs-C=SC=SSsH
                L5: Cs-C=SCsSsH
                L5: Cs-C=SCtSsH
                L5: Cs-C=S(Cds-Cd)SsH
                    L6: Cs-C=S(Cds-Cdd)SsH
                        L7: Cs-C=S(Cds-Cdd-Cd)SsH
                        L7: Cs-C=S(Cds-Cdd-S2d)SsH
                    L6: Cs-C=S(Cds-Cds)SsH
            L4: Cs-CSHH
                L5: Cs-CsSHH
                    L6: Cs-CsS2HH
                    L6: Cs-CsS4HH
                    L6: Cs-CsS6HH
                L5: Cs-CdsSsHH
                    L6: Cs-(Cds-Cd)SsHH
                        L7: Cs-(Cds-Cds)SsHH
                        L7: Cs-(Cds-Cdd)SsHH
                            L8: Cs-(Cds-Cdd-S2d)SsHH
                            L8: Cs-(Cds-Cdd-Cd)SsHH
                L5: Cs-CtSsHH
                L5: Cs-CbSsHH
                L5: Cs-C=SSsHH
            L4: Cs-ClClHH
            L4: Cs-ClClClH
            L4: Cs-ClClClCl
            L4: Cs-CClHH
            L4: Cs-CIHH
            L4: Cs-CClClH
            L4: Cs-CIIH
            L4: Cs-CClClCl
            L4: Cs-CCClH
            L4: Cs-CCIH
            L4: Cs-CCClCl
            L4: Cs-CCCCl
            L4: Cs-CCCI
    L2: O
        L3: Oa(S)
        L3: O2d
            L4: O2d-Cd
            L4: O2d-O2d
            L4: O2d-N3d
            L4: O2d-N5dc
            L4: O2d-Sd
        L3: O2s
            L4: O2s-N
                L5: O2s-CN
                    L6: O2s-CsN3s
                    L6: O2s-CsN3d
                        L7: O2s-Cs(N3dOd)
                    L6: O2s-CdN3d
                        L7: O2s-(Cd-Cd)(N3dOd)
                    L6: O2s-CsN5dc
                        L7: O2s-Cs(N5dcOdOs)
                    L6: O2s-CdN5dc
                        L7: O2s-(Cd-CdHH)(N5dcOdOs)
                L5: O2s-ON
                    L6: O2s-OsN3s
                    L6: O2s-OsN3d
                        L7: O2s-O2s(N3dOd)
                L5: O2s-NN
                    L6: O2s-N3sN3s
                    L6: O2s-N3sN3d
                        L7: O2s-N3s(N3dOd)
            L4: O2s-HH
            L4: O2s-OsH
            L4: O2s-OsOs
            L4: O2s-SsOs
            L4: O2s-CH
                L5: O2s-CtH
                L5: O2s-CdsH
                    L6: O2s-(Cds-O2d)H
                    L6: O2s-(Cds-Cd)H
                L5: O2s-CsH
                L5: O2s-CbH
                L5: O2s-CSH
            L4: O2s-OsC
                L5: O2s-OsCt
                L5: O2s-OsCds
                    L6: O2s-O2s(Cds-O2d)
                    L6: O2s-O2s(Cds-Cd)
                L5: O2s-OsCs
                L5: O2s-OsCb
            L4: O2s-CC
                L5: O2s-CtCt
                L5: O2s-CtCds
                    L6: O2s-Ct(Cds-O2d)
                    L6: O2s-Ct(Cds-Cd)
                L5: O2s-CtCs
                    L6: O2s-Cs(CtN3t)
                L5: O2s-CtCb
                L5: O2s-CdsCds
                    L6: O2s-(Cds-O2d)(Cds-O2d)
                    L6: O2s-(Cds-O2d)(Cds-Cd)
                    L6: O2s-(Cds-Cd)(Cds-Cd)
                L5: O2s-CdsCs
                    L6: O2s-Cs(Cds-O2d)
                    L6: O2s-Cs(Cds-Cd)
                L5: O2s-CdsCb
                    L6: O2s-Cb(Cds-O2d)
                    L6: O2s-Cb(Cds-Cd)
                L5: O2s-CsCs
                L5: O2s-CsCb
                L5: O2s-CbCb
                L5: O2s-Cs(Cds-S2d)
            L4: O2s-CS
                L5: O2s-CS2
                L5: O2s-CS4
                L5: O2s-CS6
            L4: O2s-SH
                L5: O2s-S_nonDeH
                L5: O2s-S_DeH
    L2: Si
        L3: SiJ2(S)
    L2: S
        L3: Sc
        L3: Sa(S)
        L3: S2d
            L4: S2d-C
            L4: S2d-S
            L4: S2d-O
        L3: S2s
            L4: S2s-HH
            L4: S2s-CH
                L5: S2s-CsH
                L5: S2s-CdH
                L5: S2s-CtH
                L5: S2s-CbH
                L5: S2s-(C=O)H
                L5: S2s-(C=S2d)H
            L4: S2s-SH
                L5: S2s-S2sH
                L5: S2s-S_DeH
            L4: S2s-SS
                L5: S2s-SsSs
            L4: S2s-SO
                L5: S2s-S2O
                L5: S2s-S4O
                L5: S2s-S6O
            L4: S2s-SC
                L5: S2s-S2sC
                    L6: S2s-S2sCs
                    L6: S2s-S2sCd
                    L6: S2s-S2sCt
                    L6: S2s-S2sCb
                L5: S2s-S46C
            L4: S2s-CC
                L5: S2s-CsCs
                L5: S2s-CsCd
                L5: S2s-Cs(C=O)
                L5: S2s-CsCt
                L5: S2s-CsCb
                L5: S2s-CdCd
                L5: S2s-CdCt
                L5: S2s-CdCb
                L5: S2s-CtCt
                L5: S2s-CtCb
                L5: S2s-CbCb
                L5: S2s-(C=S2d)Cs
                L5: S2s-(C=S2d)(C=S2d)
                L5: S2s-(C=S2d)Cmb
            L4: S2s-OH
            L4: S2s-OO
            L4: S2s-OC
                L5: S2s-OCs
        L3: S4dd
            L4: S4dd-OdOd
            L4: S4dd-CdOd
            L4: S4dd-CdCd
            L4: S4dd-OdSd
                L5: S4dd-OdS4d
                L5: S4dd-OdS6d
            L4: S4dd-SdCd
                L5: S4dd-S2dCd
                L5: S4dd-S46dCd
        L3: S4d
            L4: S4d-Od
                L5: S4d-OdHH
                L5: S4d-OdCC
                    L6: S4d-OdCsCs
                    L6: S4d-OdCdCd
                L5: S4d-OdCH
                    L6: S4d-OdCsH
                    L6: S4d-OdCdH
                L5: S4d-OdCS
                L5: S4d-OdCO
                    L6: S4d-OdOsCs
                    L6: S4d-OdOsCd
                L5: S4d-OdOO
                L5: S4d-OdOH
                L5: S4d-OdOS
                L5: S4d-OdSS
                L5: S4d-OdSH
            L4: S4d-Cd
                L5: S4d-CdCC
                L5: S4d-CdCH
                L5: S4d-CdHH
                L5: S4d-CdOC
                L5: S4d-CdOH
            L4: S4d-Sd
                L5: S4d-SdOC
                L5: S4d-SdOH
                L5: S4d-SdCH
                L5: S4d-SdSC
        L3: S4s
            L4: S4s-OCCH
            L4: S4s-CCCH
            L4: S4s-OOCC
            L4: S4s-SOCH
            L4: S4s-SOOH
        L3: S4t
            L4: S4t-CtC
            L4: S4t-CtH
            L4: S4t-CtO
        L3: S6s
            L4: S6s-CCCCCH
            L4: S6s-OCCCCH
            L4: S6s-SOOCCH
        L3: S6d
            L4: S6d-OdOCCH
            L4: S6d-OdCCCH
        L3: S6dd
            L4: S6dd-OdOd
                L5: S6dd-OdOdHH
                L5: S6dd-OdOdCC
                    L6: S6dd-OdOdCsCs
                    L6: S6dd-OdOdCdCd
                L5: S6dd-OdOdCH
                    L6: S6dd-OdOdCsH
                    L6: S6dd-OdOdCdH
                L5: S6dd-OdOdCS
                L5: S6dd-OdOdCO
                    L6: S6dd-OdOdCsOs
                    L6: S6dd-OdOdCdOs
                L5: S6dd-OdOdOO
                L5: S6dd-OdOdOH
                L5: S6dd-OdOdOS
                L5: S6dd-OdOdSS
                L5: S6dd-OdOdSH
            L4: S6dd-OdCd
                L5: S6dd-OdCdCC
                L5: S6dd-OdCdCH
                L5: S6dd-OdCdOC
                L5: S6dd-OdCdOO
                L5: S6dd-OdCdOH
                L5: S6dd-OdCdSH
                L5: S6dd-OdCdOS
            L4: S6dd-CdCd
                L5: S6dd-CdCdCC
                L5: S6dd-CdCdCH
                L5: S6dd-CdCdOC
            L4: S6dd-OdSd
                L5: S6dd-OdSdOC
                L5: S6dd-OdSdOH
                L5: S6dd-OdSdCH
        L3: S6ddd
            L4: S6ddd-OdOdOd
            L4: S6ddd-OdOdXd
            L4: S6ddd-OdXdXd
        L3: S6t
            L4: S6t-CtCCC
            L4: S6t-CtHHH
            L4: S6t-CtOCC
            L4: S6t-CtOCH
        L3: S6td
            L4: S6td-CtCdC
            L4: S6td-CtOdC
            L4: S6td-CtOdH
    L2: N
        L3: N0sc
        L3: N1s
            L4: N1s-H
            L4: N1s-N1s
            L4: N1s-Cs
            L4: N1s-N3s
            L4: N1s-O2s
        L3: N1dc
        L3: N1sc
        L3: N3s
            L4: N3s-CHH
                L5: N3s-CsHH
                L5: N3s-CbHH
                L5: N3s-(CO)HH
                L5: N3s-CdHH
            L4: N3s-CCH
                L5: N3s-CsCsH
                L5: N3s-CbCsH
                L5: N3s-CbCbH
                L5: N3s-(CO)CsH
                L5: N3s-(CO)CbH
                L5: N3s-(CO)(CO)H
                L5: N3s-(CtN3t)CsH
                L5: N3s-(CdCd)CsH
            L4: N3s-CCC
                L5: N3s-CsCsCs
                L5: N3s-CbCsCs
                L5: N3s-(CO)CsCs
                L5: N3s-(CO)(CO)Cs
                L5: N3s-(CO)(CO)Cb
                L5: N3s-(CtN3t)CsCs
                L5: N3s-(CdCd)CsCs
            L4: N3s-N3sHH
            L4: N3s-N3dHH
            L4: N3s-NCH
                L5: N3s-N3sCsH
                L5: N3s-N3sCbH
                L5: N3s-CsH(N3dOd)
                L5: N3s-CsH(N5dcOdOs)
                L5: N3s-(CdCd)HN3s
            L4: N3s-NCC
                L5: N3s-NCsCs
                    L6: N3s-CsCsN3s
                    L6: N3s-CsCs(N3dOd)
                    L6: N3s-CsCs(N5dcOdOs)
                L5: N3s-NCdCs
                    L6: N3s-(CdCd)CsN3s
            L4: N3s-CsHOs
            L4: N3s-CsCsOs
            L4: N3s-OsHH
        L3: N3d
            L4: N3d-CdH
            L4: N3d-CdN3s
            L4: N3d-N3dH
            L4: N3d-N3dN3s
            L4: N3d-OdOs
            L4: N3d-OdN3s
            L4: N3d-CsR
                L5: N3d-OdC
                L5: N3d-CdCs
                L5: N3d-N3dCs
            L4: N3d-CbR
        L3: N3t
            L4: N3t-CtH
        L3: N5dc
            L4: N5dc-OdOsCs
            L4: N5dc-OdOsCd
            L4: N5dc-OdOsOs
            L4: N5dc-OdOsN3s
        L3: N5ddc
    L2: Cl1s
    L2: I1s
"""
)

