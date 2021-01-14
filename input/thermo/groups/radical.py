#!/usr/bin/env python
# encoding: utf-8

name = "Radical Corrections"
shortDesc = ""
longDesc = """

"""
entry(
    index = 0,
    label = "Radical",
    group = "OR{RJ, RJ2_triplet, RJ3}",
    thermo = 'RJ',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1,
    label = "RJ",
    group = 
"""
1 * R u1
""",
    thermo = 'CJ',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2,
    label = "CJ",
    group = 
"""
1 * C u1
""",
    thermo = 'CsJ',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 3,
    label = "CsJ",
    group = 
"""
1 * Cs u1
""",
    thermo = 'Cs_P',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 4,
    label = "CsBr1sBr1sCO",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   CO   u0 {1,S}
3   Br1s u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.56192,-1.80318,-2.03486,-2.2846,-2.75088,-3.13763,-3.75706],'cal/(mol*K)','+|-',[0.494212,0.507429,0.475777,0.444387,0.392181,0.343187,0.251358]),
        H298 = (87.3053,'kcal/mol','+|-',0.789499),
        S298 = (-1.30281,'cal/(mol*K)','+|-',1.34172),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:ODC(O)[C](Br)Br smiles:O=C(O)[C](Br)Br H298:-46.23 kcal/mol
library:CHOBr_G4 label:CC(DO)[C](Br)Br smiles:CC(=O)[C](Br)Br H298:-0.84 kcal/mol
library:CHOBr_G4 label:ODC(Br)[C](Br)Br smiles:O=C(Br)[C](Br)Br H298:10.93 kcal/mol
library:CHOBr_G4 label:ODC[C](Br)Br smiles:O=C[C](Br)Br H298:10.93 kcal/mol
""",
)

entry(
    index = 5,
    label = "CsBr1sCOCl1s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   CO   u0 {1,S}
3   Cl1s u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.40061,-1.82476,-2.06306,-2.25352,-2.63207,-3.03295,-3.79357],'cal/(mol*K)','+|-',[0.494212,0.507429,0.475777,0.444387,0.392181,0.343187,0.251358]),
        H298 = (86.4805,'kcal/mol','+|-',0.789499),
        S298 = (-0.100724,'cal/(mol*K)','+|-',1.34172),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOClBr_G4 label:ODC(Br)[C](Cl)Br smiles:O=C(Br)[C](Cl)Br H298:-1.01 kcal/mol
library:CHOClBr_G4 label:CC(DO)[C](Cl)Br smiles:CC(=O)[C](Cl)Br H298:-12.83 kcal/mol
library:CHOClBr_G4 label:ODC(O)[C](Cl)Br smiles:O=C(O)[C](Cl)Br H298:-58.18 kcal/mol
library:CHOClBr_G4 label:ODC[C](Cl)Br smiles:O=C[C](Cl)Br H298:-1.11 kcal/mol
""",
)

entry(
    index = 6,
    label = "CsCOCl1sCl1s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   CO   u0 {1,S}
3   Cl1s u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.46732,-1.86748,-2.15651,-2.38254,-2.80851,-3.16653,-3.85184],'cal/(mol*K)','+|-',[0.329475,0.338286,0.317185,0.296258,0.261454,0.228792,0.167572]),
        H298 = (85.8392,'kcal/mol','+|-',0.526333),
        S298 = (0.341121,'cal/(mol*K)','+|-',0.894479),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOCl_G4 label:ODC[C](Cl)Cl smiles:O=C[C](Cl)Cl H298:-13.07 kcal/mol
library:CHOCl_G4 label:ODC(Cl)[C](Cl)Cl smiles:O=C(Cl)[C](Cl)Cl H298:-25.54 kcal/mol
library:CHOCl_G4 label:ODC(OCl)[C](Cl)Cl smiles:O=C(OCl)[C](Cl)Cl H298:-30.41 kcal/mol
library:CHOCl_G4 label:ODC(O)[C](Cl)Cl smiles:O=C(O)[C](Cl)Cl H298:-70.30 kcal/mol
library:CHOCl_G4 label:ODC([C](Cl)Cl)C(Cl)(Cl)Cl smiles:O=C([C](Cl)Cl)C(Cl)(Cl)Cl H298:-28.71 kcal/mol
library:CHOCl_G4 label:ODC(CCl)[C](Cl)Cl smiles:O=C(CCl)[C](Cl)Cl H298:-26.52 kcal/mol
library:CHOCl_G4 label:CC(DO)[C](Cl)Cl smiles:CC(=O)[C](Cl)Cl H298:-24.94 kcal/mol
library:CHOCl_G4 label:ODC([C](Cl)Cl)C(Cl)Cl smiles:O=C([C](Cl)Cl)C(Cl)Cl H298:-28.79 kcal/mol
library:CHOClBr_G4 label:ODC(Br)[C](Cl)Cl smiles:O=C(Br)[C](Cl)Cl H298:-13.00 kcal/mol
""",
)

entry(
    index = 7,
    label = "CsBr1sCOF1s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   CO   u0 {1,S}
3   F1s  u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.10664,-1.54639,-1.9071,-2.24279,-2.81012,-3.2478,-3.93362],'cal/(mol*K)','+|-',[0.373589,0.38358,0.359654,0.335925,0.296461,0.259425,0.190009]),
        H298 = (88.9206,'kcal/mol','+|-',0.596805),
        S298 = (-0.290312,'cal/(mol*K)','+|-',1.01424),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFBr_G4 label:ODC(Br)[C](F)Br smiles:O=C(Br)[C](F)Br H298:-37.75 kcal/mol
library:CHOFBr_G4 label:ODC(O)[C](F)Br smiles:O=C(O)[C](F)Br H298:-94.39 kcal/mol
library:CHOFBr_G4 label:CC(DO)[C](F)Br smiles:CC(=O)[C](F)Br H298:-50.51 kcal/mol
library:CHOFBr_G4 label:ODC([C](F)Br)C(Br)Br smiles:O=C([C](F)Br)C(Br)Br H298:-31.95 kcal/mol
library:CHOFBr_G4 label:ODC(OBr)[C](F)Br smiles:O=C(OBr)[C](F)Br H298:-52.65 kcal/mol
library:CHOFBr_G4 label:ODC[C](F)Br smiles:O=C[C](F)Br H298:-37.42 kcal/mol
library:CHOFBr_G4 label:ODC(CBr)[C](F)Br smiles:O=C(CBr)[C](F)Br H298:-41.10 kcal/mol
""",
)

entry(
    index = 8,
    label = "CsCOCl1sF1s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   CO   u0 {1,S}
3   F1s  u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.27325,-1.57656,-1.86086,-2.11983,-2.55326,-2.9453,-3.75862],'cal/(mol*K)','+|-',[0.442037,0.453859,0.425548,0.397472,0.350777,0.306956,0.224821]),
        H298 = (88.5716,'kcal/mol','+|-',0.706149),
        S298 = (-1.41946,'cal/(mol*K)','+|-',1.20007),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFCl_G4 label:ODC(Cl)[C](F)Cl smiles:O=C(Cl)[C](F)Cl H298:-62.70 kcal/mol
library:CHOFCl_G4 label:ODC[C](F)Cl smiles:O=C[C](F)Cl H298:-50.20 kcal/mol
library:CHOFCl_G4 label:CC(DO)[C](F)Cl smiles:CC(=O)[C](F)Cl H298:-63.75 kcal/mol
library:CHOFCl_G4 label:ODC(O)[C](F)Cl smiles:O=C(O)[C](F)Cl H298:-107.14 kcal/mol
library:CHOFClBr_G4 label:ODC(Br)[C](F)Cl smiles:O=C(Br)[C](F)Cl H298:-50.27 kcal/mol
""",
)

entry(
    index = 9,
    label = "CsCOF1sF1s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CO  u0 {1,S}
3   F1s u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0230327,-0.342649,-0.866132,-1.38589,-2.2862,-2.94061,-3.8375],'cal/(mol*K)','+|-',[0.264167,0.271232,0.254314,0.237535,0.20963,0.183441,0.134356]),
        H298 = (93.0546,'kcal/mol','+|-',0.422005),
        S298 = (-0.504836,'cal/(mol*K)','+|-',0.717179),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:ODC[C](F)F smiles:O=C[C](F)F H298:-89.99 kcal/mol
library:CHOF_G4 label:CC(DO)[C](F)F smiles:CC(=O)[C](F)F H298:-102.19 kcal/mol
library:CHOF_G4 label:ODC([C](F)F)C(F)F smiles:O=C([C](F)F)C(F)F H298:-191.21 kcal/mol
library:CHOF_G4 label:ODC(CF)[C](F)F smiles:O=C(CF)[C](F)F H298:-140.16 kcal/mol
library:CHOF_G4 label:ODC(O)[C](F)F smiles:O=C(O)[C](F)F H298:-146.09 kcal/mol
library:CHOF_G4 label:ODC(F)[C](F)F smiles:O=C(F)[C](F)F H298:-146.91 kcal/mol
library:CHOF_G4 label:ODC(OF)[C](F)F smiles:O=C(OF)[C](F)F H298:-104.74 kcal/mol
library:CHOF_G4 label:ODC([C](F)F)C(F)(F)F smiles:O=C([C](F)F)C(F)(F)F H298:-246.97 kcal/mol
library:CHOFCl_G4 label:ODC(Cl)[C](F)F smiles:O=C(Cl)[C](F)F H298:-101.63 kcal/mol
library:CHOFBr_G4 label:ODC(CBr)[C](F)F smiles:O=C(CBr)[C](F)F H298:-93.04 kcal/mol
library:CHOFBr_G4 label:ODC(Br)[C](F)F smiles:O=C(Br)[C](F)F H298:-89.06 kcal/mol
library:CHOFBr_G4 label:ODC(OBr)[C](F)F smiles:O=C(OBr)[C](F)F H298:-104.11 kcal/mol
library:CHOFBr_G4 label:ODC([C](F)F)C(Br)Br smiles:O=C([C](F)F)C(Br)Br H298:-83.86 kcal/mol
library:CHOFBr_G4 label:ODC([C](F)F)C(F)Br smiles:O=C([C](F)F)C(F)Br H298:-134.62 kcal/mol
""",
)

entry(
    index = 10,
    label = "CsBr1sCOH",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   CO   u0 {1,S}
3   H    u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.486218,-0.830888,-1.18514,-1.50547,-2.11525,-2.68783,-3.77601],'cal/(mol*K)','+|-',[0.403522,0.414314,0.38847,0.362841,0.320214,0.280211,0.205233]),
        H298 = (90.3947,'kcal/mol','+|-',0.644623),
        S298 = (-2.0357,'cal/(mol*K)','+|-',1.09551),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:ODC(Br)[CH]Br smiles:O=C(Br)[CH]Br H298:3.59 kcal/mol
library:CHOBr_G4 label:ODC([CH]Br)OBr smiles:O=C([CH]Br)OBr H298:-11.57 kcal/mol
library:CHOBr_G4 label:ODC([CH]Br)CBr smiles:O=C([CH]Br)CBr H298:2.47 kcal/mol
library:CHOBr_G4 label:ODC[CH]Br smiles:O=C[CH]Br H298:6.00 kcal/mol
library:CHOBr_G4 label:CC(DO)[CH]Br smiles:CC(=O)[CH]Br H298:-6.15 kcal/mol
library:CHOBr_G4 label:ODC(O)[CH]Br smiles:O=C(O)[CH]Br H298:-52.74 kcal/mol
""",
)

entry(
    index = 11,
    label = "CsCOCl1sH",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   CO   u0 {1,S}
3   H    u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.57003,-0.738929,-1.06503,-1.39581,-2.03941,-2.63124,-3.69337],'cal/(mol*K)','+|-',[0.298021,0.305991,0.286904,0.267976,0.236494,0.20695,0.151574]),
        H298 = (88.5012,'kcal/mol','+|-',0.476086),
        S298 = (-1.95718,'cal/(mol*K)','+|-',0.809087),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOCl_G4 label:ODC([CH]Cl)C(Cl)Cl smiles:O=C([CH]Cl)C(Cl)Cl H298:-24.61 kcal/mol
library:CHOCl_G4 label:ODC([CH]Cl)CCl smiles:O=C([CH]Cl)CCl H298:-20.61 kcal/mol
library:CHOCl_G4 label:ODC(Cl)[CH]Cl smiles:O=C(Cl)[CH]Cl H298:-20.81 kcal/mol
library:CHOCl_G4 label:ODC(O)[CH]Cl smiles:O=C(O)[CH]Cl H298:-65.01 kcal/mol
library:CHOCl_G4 label:CC(DO)[CH]Cl smiles:CC(=O)[CH]Cl H298:-18.50 kcal/mol
library:CHOCl_G4 label:ODC[CH]Cl smiles:O=C[CH]Cl H298:-6.29 kcal/mol
library:CHOCl_G4 label:ODC([CH]Cl)OCl smiles:O=C([CH]Cl)OCl H298:-25.50 kcal/mol
library:CHOCl_G4 label:ODC([CH]Cl)C(Cl)(Cl)Cl smiles:O=C([CH]Cl)C(Cl)(Cl)Cl H298:-25.31 kcal/mol
library:CHOClBr_G4 label:ODC([CH]Cl)OBr smiles:O=C([CH]Cl)OBr H298:-23.74 kcal/mol
library:CHOClBr_G4 label:ODC(Br)[CH]Cl smiles:O=C(Br)[CH]Cl H298:-8.44 kcal/mol
library:CHOClBr_G4 label:ODC([CH]Cl)CBr smiles:O=C([CH]Cl)CBr H298:-9.69 kcal/mol
""",
)

entry(
    index = 12,
    label = "CsCOF1sH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CO  u0 {1,S}
3   H   u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.11204,-1.34335,-1.69224,-2.07284,-2.75347,-3.23588,-4.03263],'cal/(mol*K)','+|-',[0.22676,0.232825,0.218301,0.203899,0.179945,0.157465,0.115331]),
        H298 = (89.9852,'kcal/mol','+|-',0.362247),
        S298 = (-1.6464,'cal/(mol*K)','+|-',0.615623),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:ODC([CH]F)OF smiles:O=C([CH]F)OF H298:-60.66 kcal/mol
library:CHOF_G4 label:ODC([CH]F)CF smiles:O=C([CH]F)CF H298:-94.68 kcal/mol
library:CHOF_G4 label:ODC([CH]F)C(F)F smiles:O=C([CH]F)C(F)F H298:-144.39 kcal/mol
library:CHOF_G4 label:ODC(O)[CH]F smiles:O=C(O)[CH]F H298:-100.88 kcal/mol
library:CHOF_G4 label:ODC([CH]F)C(F)(F)F smiles:O=C([CH]F)C(F)(F)F H298:-200.45 kcal/mol
library:CHOF_G4 label:ODC[CH]F smiles:O=C[CH]F H298:-42.56 kcal/mol
library:CHOF_G4 label:ODC(F)[CH]F smiles:O=C(F)[CH]F H298:-102.15 kcal/mol
library:CHOF_G4 label:CC(DO)[CH]F smiles:CC(=O)[CH]F H298:-55.22 kcal/mol
library:CHOFCl_G4 label:ODC([CH]F)OCl smiles:O=C([CH]F)OCl H298:-61.76 kcal/mol
library:CHOFCl_G4 label:ODC(Cl)[CH]F smiles:O=C(Cl)[CH]F H298:-56.57 kcal/mol
library:CHOFCl_G4 label:ODC([CH]F)CCl smiles:O=C([CH]F)CCl H298:-56.34 kcal/mol
library:CHOFBr_G4 label:ODC([CH]F)C(F)(Br)Br smiles:O=C([CH]F)C(F)(Br)Br H298:-79.11 kcal/mol
library:CHOFBr_G4 label:ODC([CH]F)CBr smiles:O=C([CH]F)CBr H298:-45.90 kcal/mol
library:CHOFBr_G4 label:ODC([CH]F)C(Br)Br smiles:O=C([CH]F)C(Br)Br H298:-37.33 kcal/mol
library:CHOFBr_G4 label:ODC([CH]F)C(Br)(Br)Br smiles:O=C([CH]F)C(Br)(Br)Br H298:-25.35 kcal/mol
library:CHOFBr_G4 label:ODC(Br)[CH]F smiles:O=C(Br)[CH]F H298:-43.97 kcal/mol
library:CHOFBr_G4 label:ODC([CH]F)C(F)(F)Br smiles:O=C([CH]F)C(F)(F)Br H298:-137.28 kcal/mol
library:CHOFBr_G4 label:ODC([CH]F)C(F)Br smiles:O=C([CH]F)C(F)Br H298:-88.05 kcal/mol
library:CHOFBr_G4 label:ODC([CH]F)OBr smiles:O=C([CH]F)OBr H298:-58.94 kcal/mol
""",
)

entry(
    index = 13,
    label = "CsBr1sCOO2s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   CO   u0 {1,S}
3   O2s  u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.12412,-2.99811,-3.45358,-3.64604,-3.81702,-3.87261,-4.00097],'cal/(mol*K)','+|-',[0.494212,0.507429,0.475777,0.444387,0.392181,0.343187,0.251358]),
        H298 = (83.101,'kcal/mol','+|-',0.789499),
        S298 = (-2.60285e-05,'cal/(mol*K)','+|-',1.34172),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:ODC[C](O)Br smiles:O=C[C](O)Br H298:-43.84 kcal/mol
library:CHOBr_G4 label:ODC(Br)[C](O)Br smiles:O=C(Br)[C](O)Br H298:-43.14 kcal/mol
library:CHOFBr_G4 label:ODC(F)[C](O)Br smiles:O=C(F)[C](O)Br H298:-100.26 kcal/mol
library:CHOClBr_G4 label:ODC(Cl)[C](O)Br smiles:O=C(Cl)[C](O)Br H298:-55.71 kcal/mol
""",
)

entry(
    index = 14,
    label = "CsCOCl1sO2s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   CO   u0 {1,S}
3   O2s  u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.30789,-3.14343,-3.54971,-3.65949,-3.72569,-3.71624,-3.64574],'cal/(mol*K)','+|-',[0.570667,0.585929,0.54938,0.513134,0.452851,0.396279,0.290243]),
        H298 = (81.7661,'kcal/mol','+|-',0.911635),
        S298 = (0.125636,'cal/(mol*K)','+|-',1.54928),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOCl_G4 label:ODC[C](O)Cl smiles:O=C[C](O)Cl H298:-56.50 kcal/mol
library:CHOCl_G4 label:ODC(Cl)[C](O)Cl smiles:O=C(Cl)[C](O)Cl H298:-68.33 kcal/mol
library:CHOFCl_G4 label:ODC(F)[C](O)Cl smiles:O=C(F)[C](O)Cl H298:-112.84 kcal/mol
""",
)

entry(
    index = 15,
    label = "CsCOF1sO2s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CO  u0 {1,S}
3   O2s u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.00005,-2.77291,-3.25129,-3.46512,-3.63633,-3.66557,-3.58204],'cal/(mol*K)','+|-',[0.698921,0.717613,0.67285,0.628458,0.554627,0.48534,0.355473]),
        H298 = (85.1381,'kcal/mol','+|-',1.11652),
        S298 = (0.447461,'cal/(mol*K)','+|-',1.89748),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:ODC(F)[C](O)F smiles:O=C(F)[C](O)F H298:-151.47 kcal/mol
library:CHOF_G4 label:ODC[C](O)F smiles:O=C[C](O)F H298:-96.07 kcal/mol
""",
)

entry(
    index = 16,
    label = "CsBr1sCOCO",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   CO   u0 {1,S}
3   CO   u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 17,
    label = "CsCOCOCl1s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   CO   u0 {1,S}
3   CO   u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 18,
    label = "CsCOCOF1s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CO  u0 {1,S}
3   CO  u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 19,
    label = "CsBr1sCOCt",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Ct   u0 {1,S}
3   CO   u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 20,
    label = "CsCOCl1sCt",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Ct   u0 {1,S}
3   CO   u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 21,
    label = "CsCOCtF1s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Ct  u0 {1,S}
3   CO  u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 22,
    label = "CsBr1sCOCd",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cd   u0 {1,S}
3   CO   u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 23,
    label = "CsCOCdCl1s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cd   u0 {1,S}
3   CO   u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 24,
    label = "CsCOCdF1s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S}
3   CO  u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 25,
    label = "CsBr1sCOCs",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cs   u0 {1,S}
3   CO   u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.95105,-2.22409,-2.42576,-2.61947,-3.01655,-3.40045,-4.11254],'cal/(mol*K)','+|-',[0.274139,0.281471,0.263914,0.246502,0.217543,0.190366,0.139428]),
        H298 = (88.1056,'kcal/mol','+|-',0.437935),
        S298 = (1.90413,'cal/(mol*K)','+|-',0.744252),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:C[C](Br)C(DO)Br smiles:C[C](Br)C(=O)Br H298:-7.05 kcal/mol
library:CHOBr_G4 label:C[C](Br)CDO smiles:C[C](Br)C=O H298:-6.54 kcal/mol
library:CHOBr_G4 label:ODC[C](Br)CBr smiles:O=C[C](Br)CBr H298:0.60 kcal/mol
library:CHOFBr_G4 label:ODC[C](Br)C(F)(F)F smiles:O=C[C](Br)C(F)(F)F H298:-151.73 kcal/mol
library:CHOFBr_G4 label:ODC(Br)[C](Br)C(F)F smiles:O=C(Br)[C](Br)C(F)F H298:-97.86 kcal/mol
library:CHOFBr_G4 label:ODC[C](Br)C(F)(Br)Br smiles:O=C[C](Br)C(F)(Br)Br H298:-30.44 kcal/mol
library:CHOFBr_G4 label:ODC[C](Br)C(F)Br smiles:O=C[C](Br)C(F)Br H298:-39.55 kcal/mol
library:CHOFBr_G4 label:ODC(Br)[C](Br)CF smiles:O=C(Br)[C](Br)CF H298:-45.78 kcal/mol
library:CHOFBr_G4 label:ODC(Br)[C](Br)C(F)Br smiles:O=C(Br)[C](Br)C(F)Br H298:-42.04 kcal/mol
library:CHOFBr_G4 label:ODC[C](Br)C(F)(F)Br smiles:O=C[C](Br)C(F)(F)Br H298:-88.97 kcal/mol
library:CHOFBr_G4 label:ODC[C](Br)CF smiles:O=C[C](Br)CF H298:-45.86 kcal/mol
library:CHOFBr_G4 label:ODC[C](Br)C(F)F smiles:O=C[C](Br)C(F)F H298:-97.16 kcal/mol
library:CHOClBr_G4 label:ODC[C](Br)CCl smiles:O=C[C](Br)CCl H298:-9.41 kcal/mol
""",
)

entry(
    index = 26,
    label = "CsCOCl1sCs",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cs   u0 {1,S}
3   CO   u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.16691,-1.63574,-2.09046,-2.48493,-3.10168,-3.53478,-4.18937],'cal/(mol*K)','+|-',[0.312567,0.320926,0.300908,0.281055,0.248037,0.217051,0.158973]),
        H298 = (86.6,'kcal/mol','+|-',0.499323),
        S298 = (0.928022,'cal/(mol*K)','+|-',0.848578),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOCl_G4 label:C[C](Cl)CDO smiles:C[C](Cl)C=O H298:-18.93 kcal/mol
library:CHOCl_G4 label:ODC(Cl)[C](Cl)C(Cl)Cl smiles:O=C(Cl)[C](Cl)C(Cl)Cl H298:-37.80 kcal/mol
library:CHOCl_G4 label:C[C](Cl)C(DO)Cl smiles:C[C](Cl)C(=O)Cl H298:-32.21 kcal/mol
library:CHOCl_G4 label:ODC[C](Cl)CCl smiles:O=C[C](Cl)CCl H298:-21.57 kcal/mol
library:CHOCl_G4 label:ODC(Cl)[C](Cl)C(Cl)(Cl)Cl smiles:O=C(Cl)[C](Cl)C(Cl)(Cl)Cl H298:-33.86 kcal/mol
library:CHOCl_G4 label:ODC[C](Cl)C(Cl)(Cl)Cl smiles:O=C[C](Cl)C(Cl)(Cl)Cl H298:-22.26 kcal/mol
library:CHOCl_G4 label:ODC(Cl)[C](Cl)CCl smiles:O=C(Cl)[C](Cl)CCl H298:-34.79 kcal/mol
library:CHOCl_G4 label:ODC[C](Cl)C(Cl)Cl smiles:O=C[C](Cl)C(Cl)Cl H298:-24.94 kcal/mol
library:CHOFCl_G4 label:ODC[C](Cl)CF smiles:O=C[C](Cl)CF H298:-58.06 kcal/mol
library:CHOClBr_G4 label:C[C](Cl)C(DO)Br smiles:C[C](Cl)C(=O)Br H298:-19.78 kcal/mol
""",
)

entry(
    index = 27,
    label = "CsCOCsF1s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   CO  u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.31427,-1.63375,-2.02315,-2.4112,-3.05102,-3.49285,-4.01448],'cal/(mol*K)','+|-',[0.285333,0.292964,0.27469,0.256567,0.226426,0.198139,0.145122]),
        H298 = (89.2948,'kcal/mol','+|-',0.455817),
        S298 = (0.254838,'cal/(mol*K)','+|-',0.774642),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:C[C](F)C(DO)F smiles:C[C](F)C(=O)F H298:-115.81 kcal/mol
library:CHOF_G4 label:C[C](F)CDO smiles:C[C](F)C=O H298:-56.65 kcal/mol
library:CHOF_G4 label:ODC(F)[C](F)C(F)(F)F smiles:O=C(F)[C](F)C(F)(F)F H298:-256.53 kcal/mol
library:CHOF_G4 label:ODC[C](F)C(F)(F)F smiles:O=C[C](F)C(F)(F)F H298:-198.75 kcal/mol
library:CHOF_G4 label:ODC(F)[C](F)C(F)F smiles:O=C(F)[C](F)C(F)F H298:-202.93 kcal/mol
library:CHOF_G4 label:ODC[C](F)CF smiles:O=C[C](F)CF H298:-94.75 kcal/mol
library:CHOF_G4 label:ODC[C](F)C(F)F smiles:O=C[C](F)C(F)F H298:-144.44 kcal/mol
library:CHOF_G4 label:ODC(F)[C](F)CF smiles:O=C(F)[C](F)CF H298:-153.74 kcal/mol
library:CHOFCl_G4 label:C[C](F)C(DO)Cl smiles:C[C](F)C(=O)Cl H298:-70.22 kcal/mol
library:CHOFBr_G4 label:ODC(Br)[C](F)CF smiles:O=C(Br)[C](F)CF H298:-95.23 kcal/mol
library:CHOFBr_G4 label:C[C](F)C(DO)Br smiles:C[C](F)C(=O)Br H298:-57.86 kcal/mol
library:CHOFBr_G4 label:ODC(Br)[C](F)C(F)F smiles:O=C(Br)[C](F)C(F)F H298:-144.67 kcal/mol
""",
)

entry(
    index = 28,
    label = "CsBr1sBr1sO2s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   O2s  u0 {1,S}
3   Br1s u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.06482,-2.14079,-2.92763,-3.53967,-4.33677,-4.7435,-5.02543],'cal/(mol*K)','+|-',[0.22676,0.232825,0.218301,0.203899,0.179945,0.157465,0.115331]),
        H298 = (94.6857,'kcal/mol','+|-',0.362247),
        S298 = (2.65274,'cal/(mol*K)','+|-',0.615623),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:OCO[C](Br)Br smiles:OCO[C](Br)Br H298:-35.95 kcal/mol
library:CHOBr_G4 label:OC(Br)O[C](Br)Br smiles:OC(Br)O[C](Br)Br H298:-31.61 kcal/mol
library:CHOBr_G4 label:CDCO[C](Br)Br smiles:C=CO[C](Br)Br H298:29.69 kcal/mol
library:CHOBr_G4 label:BrOCO[C](Br)Br smiles:BrOCO[C](Br)Br H298:2.18 kcal/mol
library:CHOBr_G4 label:BrOC(Br)O[C](Br)Br smiles:BrOC(Br)O[C](Br)Br H298:6.96 kcal/mol
library:CHOBr_G4 label:CO[C](Br)Br smiles:CO[C](Br)Br H298:6.36 kcal/mol
library:CHOBr_G4 label:CCO[C](Br)Br smiles:CCO[C](Br)Br H298:-2.19 kcal/mol
library:CHOBr_G4 label:BrC#CO[C](Br)Br smiles:BrC#CO[C](Br)Br H298:97.02 kcal/mol
library:CHOBr_G4 label:BrCO[C](Br)Br smiles:BrCO[C](Br)Br H298:11.93 kcal/mol
library:CHOBr_G4 label:BrCCO[C](Br)Br smiles:BrCCO[C](Br)Br H298:4.48 kcal/mol
library:CHOBr_G4 label:C#CO[C](Br)Br smiles:C#CO[C](Br)Br H298:85.37 kcal/mol
library:CHOBr_G4 label:ODCO[C](Br)Br smiles:O=CO[C](Br)Br H298:-25.67 kcal/mol
library:CHOBr_G4 label:Br[C](Br)OC(Br)Br smiles:Br[C](Br)OC(Br)Br H298:21.12 kcal/mol
library:CHOBr_G4 label:BrCDCO[C](Br)Br smiles:BrC=CO[C](Br)Br H298:35.72 kcal/mol
library:CHOBr_G4 label:BrCC(Br)O[C](Br)Br smiles:BrCC(Br)O[C](Br)Br H298:6.57 kcal/mol
library:CHOBr_G4 label:O[C](Br)Br smiles:O[C](Br)Br H298:3.39 kcal/mol
library:CHOBr_G4 label:CC(Br)O[C](Br)Br smiles:CC(Br)O[C](Br)Br H298:0.24 kcal/mol
library:CHOFBr_G4 label:FC#CO[C](Br)Br smiles:FC#CO[C](Br)Br H298:60.28 kcal/mol
library:CHOClBr_G4 label:ClC#CO[C](Br)Br smiles:ClC#CO[C](Br)Br H298:86.40 kcal/mol
""",
)

entry(
    index = 29,
    label = "CsBr1sCl1sO2s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   O2s  u0 {1,S}
3   Cl1s u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.378665,-1.44155,-2.27914,-2.93104,-3.82506,-4.38583,-5.03853],'cal/(mol*K)','+|-',[0.264167,0.271232,0.254314,0.237535,0.20963,0.183441,0.134356]),
        H298 = (95.1183,'kcal/mol','+|-',0.422005),
        S298 = (5.33713,'cal/(mol*K)','+|-',0.717179),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFClBr_G4 label:FC#CO[C](Cl)Br smiles:FC#CO[C](Cl)Br H298:48.00 kcal/mol
library:CHOClBr_G4 label:Cl[C](Br)OCBr smiles:Cl[C](Br)OCBr H298:-0.52 kcal/mol
library:CHOClBr_G4 label:Cl[C](Br)OCOBr smiles:Cl[C](Br)OCOBr H298:-9.77 kcal/mol
library:CHOClBr_G4 label:CO[C](Cl)Br smiles:CO[C](Cl)Br H298:-5.82 kcal/mol
library:CHOClBr_G4 label:CCO[C](Cl)Br smiles:CCO[C](Cl)Br H298:-14.28 kcal/mol
library:CHOClBr_G4 label:ClC#CO[C](Cl)Br smiles:ClC#CO[C](Cl)Br H298:74.16 kcal/mol
library:CHOClBr_G4 label:OCO[C](Cl)Br smiles:OCO[C](Cl)Br H298:-48.14 kcal/mol
library:CHOClBr_G4 label:OC(Br)O[C](Cl)Br smiles:OC(Br)O[C](Cl)Br H298:-43.71 kcal/mol
library:CHOClBr_G4 label:CDCO[C](Cl)Br smiles:C=CO[C](Cl)Br H298:16.98 kcal/mol
library:CHOClBr_G4 label:OO[C](Cl)Br smiles:OO[C](Cl)Br H298:12.36 kcal/mol
library:CHOClBr_G4 label:O[C](Cl)Br smiles:O[C](Cl)Br H298:-8.92 kcal/mol
library:CHOClBr_G4 label:ODC(Br)O[C](Cl)Br smiles:O=C(Br)O[C](Cl)Br H298:-34.29 kcal/mol
library:CHOClBr_G4 label:ODCO[C](Cl)Br smiles:O=CO[C](Cl)Br H298:-37.93 kcal/mol
library:CHOClBr_G4 label:C#CO[C](Cl)Br smiles:C#CO[C](Cl)Br H298:73.09 kcal/mol
""",
)

entry(
    index = 30,
    label = "CsCl1sCl1sO2s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   O2s  u0 {1,S}
3   Cl1s u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.20448,-1.29445,-2.25688,-3.01312,-4.03158,-4.61682,-5.20422],'cal/(mol*K)','+|-',[0.160344,0.164632,0.154362,0.144178,0.12724,0.111345,0.0815512]),
        H298 = (94.8744,'kcal/mol','+|-',0.256147),
        S298 = (4.16931,'cal/(mol*K)','+|-',0.435311),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOCl_G4 label:C#CO[C](Cl)Cl smiles:C#CO[C](Cl)Cl H298:60.87 kcal/mol
library:CHOCl_G4 label:ClCO[C](Cl)Cl smiles:ClCO[C](Cl)Cl H298:-24.00 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)OC(Cl)(Cl)C(Cl)Cl smiles:Cl[C](Cl)OC(Cl)(Cl)C(Cl)Cl H298:-43.94 kcal/mol
library:CHOCl_G4 label:ClCCO[C](Cl)Cl smiles:ClCCO[C](Cl)Cl H298:-30.14 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)(Cl)O[C](Cl)Cl smiles:ClOC(Cl)(Cl)O[C](Cl)Cl H298:-33.20 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)OC(Cl)(Cl)C(Cl)(Cl)Cl smiles:Cl[C](Cl)OC(Cl)(Cl)C(Cl)(Cl)Cl H298:-44.49 kcal/mol
library:CHOCl_G4 label:ClCDCO[C](Cl)Cl smiles:ClC=CO[C](Cl)Cl H298:-0.06 kcal/mol
library:CHOCl_G4 label:ODCO[C](Cl)Cl smiles:O=CO[C](Cl)Cl H298:-50.19 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)OC(Cl)Cl smiles:Cl[C](Cl)OC(Cl)Cl H298:-27.38 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(Cl)O[C](Cl)Cl smiles:ClCC(Cl)(Cl)O[C](Cl)Cl H298:-41.71 kcal/mol
library:CHOCl_G4 label:OC(Cl)O[C](Cl)Cl smiles:OC(Cl)O[C](Cl)Cl H298:-69.34 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)OCC(Cl)(Cl)Cl smiles:Cl[C](Cl)OCC(Cl)(Cl)Cl H298:-38.00 kcal/mol
library:CHOCl_G4 label:O[C](Cl)Cl smiles:O[C](Cl)Cl H298:-21.31 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)O[C](Cl)Cl smiles:ClOC(Cl)O[C](Cl)Cl H298:-31.19 kcal/mol
library:CHOCl_G4 label:ClOCO[C](Cl)Cl smiles:ClOCO[C](Cl)Cl H298:-25.05 kcal/mol
library:CHOCl_G4 label:CDCO[C](Cl)Cl smiles:C=CO[C](Cl)Cl H298:5.13 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)OC(Cl)(Cl)Cl smiles:Cl[C](Cl)OC(Cl)(Cl)Cl H298:-28.05 kcal/mol
library:CHOCl_G4 label:CC(Cl)O[C](Cl)Cl smiles:CC(Cl)O[C](Cl)Cl H298:-35.59 kcal/mol
library:CHOCl_G4 label:OCO[C](Cl)Cl smiles:OCO[C](Cl)Cl H298:-60.32 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)O[C](Cl)Cl smiles:ClCC(Cl)O[C](Cl)Cl H298:-39.02 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)OCC(Cl)Cl smiles:Cl[C](Cl)OCC(Cl)Cl H298:-35.07 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)OC(Cl)DC(Cl)Cl smiles:Cl[C](Cl)OC(Cl)=C(Cl)Cl H298:-8.08 kcal/mol
library:CHOCl_G4 label:ODC(Cl)O[C](Cl)Cl smiles:O=C(Cl)O[C](Cl)Cl H298:-58.93 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)OC(Cl)C(Cl)Cl smiles:Cl[C](Cl)OC(Cl)C(Cl)Cl H298:-41.32 kcal/mol
library:CHOCl_G4 label:CC(Cl)(Cl)O[C](Cl)Cl smiles:CC(Cl)(Cl)O[C](Cl)Cl H298:-39.53 kcal/mol
library:CHOCl_G4 label:ClC#CO[C](Cl)Cl smiles:ClC#CO[C](Cl)Cl H298:62.02 kcal/mol
library:CHOCl_G4 label:CCO[C](Cl)Cl smiles:CCO[C](Cl)Cl H298:-26.12 kcal/mol
library:CHOCl_G4 label:CDC(Cl)O[C](Cl)Cl smiles:C=C(Cl)O[C](Cl)Cl H298:-1.68 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)OC(Cl)C(Cl)(Cl)Cl smiles:Cl[C](Cl)OC(Cl)C(Cl)(Cl)Cl H298:-43.65 kcal/mol
library:CHOCl_G4 label:OC(Cl)(Cl)O[C](Cl)Cl smiles:OC(Cl)(Cl)O[C](Cl)Cl H298:-71.39 kcal/mol
library:CHOCl_G4 label:CO[C](Cl)Cl smiles:CO[C](Cl)Cl H298:-17.79 kcal/mol
library:CHOFCl_G4 label:FC#CO[C](Cl)Cl smiles:FC#CO[C](Cl)Cl H298:35.82 kcal/mol
library:CHOClBr_G4 label:ODC(Br)O[C](Cl)Cl smiles:O=C(Br)O[C](Cl)Cl H298:-46.49 kcal/mol
library:CHOClBr_G4 label:Cl[C](Cl)OCBr smiles:Cl[C](Cl)OCBr H298:-12.28 kcal/mol
library:CHOClBr_G4 label:OC(Br)O[C](Cl)Cl smiles:OC(Br)O[C](Cl)Cl H298:-55.75 kcal/mol
library:CHOClBr_G4 label:Cl[C](Cl)OC(Cl)Br smiles:Cl[C](Cl)OC(Cl)Br H298:-15.02 kcal/mol
library:CHOClBr_G4 label:Cl[C](Cl)OCOBr smiles:Cl[C](Cl)OCOBr H298:-22.02 kcal/mol
library:CHOClBr_G4 label:Cl[C](Cl)OC(Br)Br smiles:Cl[C](Cl)OC(Br)Br H298:-3.09 kcal/mol
""",
)

entry(
    index = 31,
    label = "CsBr1sF1sO2s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   O2s  u0 {1,S}
3   F1s  u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.11512,-0.669275,-1.53088,-2.23454,-3.31301,-4.04657,-4.93776],'cal/(mol*K)','+|-',[0.22676,0.232825,0.218301,0.203899,0.179945,0.157465,0.115331]),
        H298 = (97.8983,'kcal/mol','+|-',0.362247),
        S298 = (2.91126,'cal/(mol*K)','+|-',0.615623),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFBr_G4 label:F[C](Br)OOCBr smiles:F[C](Br)OOCBr H298:-22.14 kcal/mol
library:CHOFBr_G4 label:OO[C](F)Br smiles:OO[C](F)Br H298:-27.51 kcal/mol
library:CHOFBr_G4 label:CDCO[C](F)Br smiles:C=CO[C](F)Br H298:-25.18 kcal/mol
library:CHOFBr_G4 label:CO[C](F)Br smiles:CO[C](F)Br H298:-48.15 kcal/mol
library:CHOFBr_G4 label:OC(Br)O[C](F)Br smiles:OC(Br)O[C](F)Br H298:-86.35 kcal/mol
library:CHOFBr_G4 label:OCO[C](F)Br smiles:OCO[C](F)Br H298:-90.57 kcal/mol
library:CHOFBr_G4 label:O[C](F)Br smiles:O[C](F)Br H298:-51.11 kcal/mol
library:CHOFBr_G4 label:F[C](Br)OC(Br)Br smiles:F[C](Br)OC(Br)Br H298:-32.10 kcal/mol
library:CHOFBr_G4 label:ODCO[C](F)Br smiles:O=CO[C](F)Br H298:-78.85 kcal/mol
library:CHOFBr_G4 label:F[C](Br)OC(Br)(Br)Br smiles:F[C](Br)OC(Br)(Br)Br H298:-18.63 kcal/mol
library:CHOFBr_G4 label:ODC(Br)O[C](F)Br smiles:O=C(Br)O[C](F)Br H298:-74.57 kcal/mol
library:CHOFBr_G4 label:FC#CO[C](F)Br smiles:FC#CO[C](F)Br H298:6.45 kcal/mol
library:CHOFBr_G4 label:COO[C](F)Br smiles:COO[C](F)Br H298:-27.99 kcal/mol
library:CHOFBr_G4 label:C#CO[C](F)Br smiles:C#CO[C](F)Br H298:31.55 kcal/mol
library:CHOFBr_G4 label:F[C](Br)OCBr smiles:F[C](Br)OCBr H298:-41.95 kcal/mol
library:CHOFBr_G4 label:F[C](Br)OC(Br)OBr smiles:F[C](Br)OC(Br)OBr H298:-45.97 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)O[C](F)Br smiles:OC(Br)(Br)O[C](F)Br H298:-73.80 kcal/mol
library:CHOFBr_G4 label:F[C](Br)OCOBr smiles:F[C](Br)OCOBr H298:-52.02 kcal/mol
library:CHOFBr_G4 label:CCO[C](F)Br smiles:CCO[C](F)Br H298:-56.46 kcal/mol
""",
)

entry(
    index = 32,
    label = "CsCl1sF1sO2s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   O2s  u0 {1,S}
3   F1s  u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.169644,-0.665331,-1.55482,-2.28307,-3.36341,-4.09089,-4.93424],'cal/(mol*K)','+|-',[0.210733,0.216369,0.202872,0.189487,0.167226,0.146336,0.107179]),
        H298 = (98.6011,'kcal/mol','+|-',0.336643),
        S298 = (3.29366,'cal/(mol*K)','+|-',0.572111),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFCl_G4 label:OC(Cl)O[C](F)Cl smiles:OC(Cl)O[C](F)Cl H298:-111.08 kcal/mol
library:CHOFCl_G4 label:CCO[C](F)Cl smiles:CCO[C](F)Cl H298:-68.24 kcal/mol
library:CHOFCl_G4 label:F[C](Cl)OC(Cl)Cl smiles:F[C](Cl)OC(Cl)Cl H298:-68.74 kcal/mol
library:CHOFCl_G4 label:F[C](Cl)OCCl smiles:F[C](Cl)OCCl H298:-65.88 kcal/mol
library:CHOFCl_G4 label:COO[C](F)Cl smiles:COO[C](F)Cl H298:-40.62 kcal/mol
library:CHOFCl_G4 label:F[C](Cl)OOCCl smiles:F[C](Cl)OOCCl H298:-46.39 kcal/mol
library:CHOFCl_G4 label:FC#CO[C](F)Cl smiles:FC#CO[C](F)Cl H298:-5.85 kcal/mol
library:CHOFCl_G4 label:ODCO[C](F)Cl smiles:O=CO[C](F)Cl H298:-91.60 kcal/mol
library:CHOFCl_G4 label:F[C](Cl)OCOCl smiles:F[C](Cl)OCOCl H298:-67.00 kcal/mol
library:CHOFCl_G4 label:O[C](F)Cl smiles:O[C](F)Cl H298:-63.53 kcal/mol
library:CHOFCl_G4 label:OCO[C](F)Cl smiles:OCO[C](F)Cl H298:-102.35 kcal/mol
library:CHOFCl_G4 label:CO[C](F)Cl smiles:CO[C](F)Cl H298:-60.03 kcal/mol
library:CHOFCl_G4 label:ODC(Cl)O[C](F)Cl smiles:O=C(Cl)O[C](F)Cl H298:-100.00 kcal/mol
library:CHOFCl_G4 label:CDCO[C](F)Cl smiles:C=CO[C](F)Cl H298:-36.49 kcal/mol
library:CHOFCl_G4 label:OO[C](F)Cl smiles:OO[C](F)Cl H298:-40.44 kcal/mol
library:CHOFClBr_G4 label:F[C](Cl)OCOBr smiles:F[C](Cl)OCOBr H298:-64.06 kcal/mol
library:CHOFClBr_G4 label:ODC(Br)O[C](F)Cl smiles:O=C(Br)O[C](F)Cl H298:-87.18 kcal/mol
library:CHOFClBr_G4 label:F[C](Cl)OOCBr smiles:F[C](Cl)OOCBr H298:-34.38 kcal/mol
library:CHOFClBr_G4 label:OC(Br)O[C](F)Cl smiles:OC(Br)O[C](F)Cl H298:-98.45 kcal/mol
library:CHOFClBr_G4 label:F[C](Cl)OC(Br)Br smiles:F[C](Cl)OC(Br)Br H298:-44.26 kcal/mol
library:CHOFClBr_G4 label:F[C](Cl)OCBr smiles:F[C](Cl)OCBr H298:-54.06 kcal/mol
library:CHOFClBr_G4 label:F[C](Cl)OC(Cl)Br smiles:F[C](Cl)OC(Cl)Br H298:-55.56 kcal/mol
""",
)

entry(
    index = 33,
    label = "CsF1sF1sO2s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S}
3   F1s u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.774318,-1.52929,-2.08276,-2.54232,-3.29647,-3.85651,-4.6867],'cal/(mol*K)','+|-',[0.127605,0.131018,0.122845,0.11474,0.101261,0.0886106,0.0649003]),
        H298 = (103.114,'kcal/mol','+|-',0.203848),
        S298 = (2.18532,'cal/(mol*K)','+|-',0.34643),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:F[C](F)OC(F)DC(F)F smiles:F[C](F)OC(F)=C(F)F H298:-208.49 kcal/mol
library:CHOF_G4 label:F[C](F)OC(F)F smiles:F[C](F)OC(F)F H298:-207.87 kcal/mol
library:CHOF_G4 label:ODC(F)O[C](F)F smiles:O=C(F)O[C](F)F H298:-191.15 kcal/mol
library:CHOF_G4 label:FCC(F)O[C](F)F smiles:FCC(F)O[C](F)F H298:-205.33 kcal/mol
library:CHOF_G4 label:F[C](F)OCC(F)F smiles:F[C](F)OCC(F)F H298:-206.99 kcal/mol
library:CHOF_G4 label:O[C](F)F smiles:O[C](F)F H298:-109.25 kcal/mol
library:CHOF_G4 label:F[C](F)OCC(F)(F)F smiles:F[C](F)OCC(F)(F)F H298:-264.99 kcal/mol
library:CHOF_G4 label:CC(F)(F)O[C](F)F smiles:CC(F)(F)O[C](F)F H298:-222.01 kcal/mol
library:CHOF_G4 label:F[C](F)OC(F)C(F)(F)F smiles:F[C](F)OC(F)C(F)(F)F H298:-312.50 kcal/mol
library:CHOF_G4 label:FCO[C](F)F smiles:FCO[C](F)F H298:-153.12 kcal/mol
library:CHOF_G4 label:FCDC(F)O[C](F)F smiles:FC=C(F)O[C](F)F H298:-165.14 kcal/mol
library:CHOF_G4 label:F[C](F)OCDC(F)F smiles:F[C](F)OC=C(F)F H298:-168.01 kcal/mol
library:CHOF_G4 label:CC(F)O[C](F)F smiles:CC(F)O[C](F)F H298:-166.56 kcal/mol
library:CHOF_G4 label:FOC(F)(F)O[C](F)F smiles:FOC(F)(F)O[C](F)F H298:-219.32 kcal/mol
library:CHOF_G4 label:ODCO[C](F)F smiles:O=CO[C](F)F H298:-136.37 kcal/mol
library:CHOF_G4 label:FCC(F)(F)O[C](F)F smiles:FCC(F)(F)O[C](F)F H298:-259.59 kcal/mol
library:CHOF_G4 label:FC#CO[C](F)F smiles:FC#CO[C](F)F H298:-50.30 kcal/mol
library:CHOF_G4 label:FOC(F)O[C](F)F smiles:FOC(F)O[C](F)F H298:-166.15 kcal/mol
library:CHOF_G4 label:FOCO[C](F)F smiles:FOCO[C](F)F H298:-116.38 kcal/mol
library:CHOF_G4 label:FCDCO[C](F)F smiles:FC=CO[C](F)F H298:-122.27 kcal/mol
library:CHOF_G4 label:OC(F)(F)O[C](F)F smiles:OC(F)(F)O[C](F)F H298:-258.84 kcal/mol
library:CHOF_G4 label:CCO[C](F)F smiles:CCO[C](F)F H298:-113.04 kcal/mol
library:CHOF_G4 label:CO[C](F)F smiles:CO[C](F)F H298:-104.66 kcal/mol
library:CHOF_G4 label:F[C](F)OC(F)(F)C(F)F smiles:F[C](F)OC(F)(F)C(F)F H298:-308.94 kcal/mol
library:CHOF_G4 label:F[C](F)OC(F)C(F)F smiles:F[C](F)OC(F)C(F)F H298:-256.50 kcal/mol
library:CHOF_G4 label:F[C](F)OC(F)(F)C(F)(F)F smiles:F[C](F)OC(F)(F)C(F)(F)F H298:-364.46 kcal/mol
library:CHOF_G4 label:OC(F)O[C](F)F smiles:OC(F)O[C](F)F H298:-203.48 kcal/mol
library:CHOF_G4 label:CDCO[C](F)F smiles:C=CO[C](F)F H298:-81.10 kcal/mol
library:CHOF_G4 label:F[C](F)OC(F)(F)F smiles:F[C](F)OC(F)(F)F H298:-263.91 kcal/mol
library:CHOF_G4 label:C#CO[C](F)F smiles:C#CO[C](F)F H298:-25.22 kcal/mol
library:CHOF_G4 label:CDC(F)O[C](F)F smiles:C=C(F)O[C](F)F H298:-128.40 kcal/mol
library:CHOF_G4 label:FCCO[C](F)F smiles:FCCO[C](F)F H298:-154.12 kcal/mol
library:CHOF_G4 label:OCO[C](F)F smiles:OCO[C](F)F H298:-146.90 kcal/mol
library:CHOFCl_G4 label:F[C](F)OC(F)Cl smiles:F[C](F)OC(F)Cl H298:-158.68 kcal/mol
library:CHOFCl_G4 label:ODC(Cl)O[C](F)F smiles:O=C(Cl)O[C](F)F H298:-144.49 kcal/mol
library:CHOFCl_G4 label:OC(Cl)O[C](F)F smiles:OC(Cl)O[C](F)F H298:-154.16 kcal/mol
library:CHOFCl_G4 label:F[C](F)OOCl smiles:F[C](F)OOCl H298:-50.69 kcal/mol
library:CHOFCl_G4 label:F[C](F)OOCCl smiles:F[C](F)OOCCl H298:-90.43 kcal/mol
library:CHOFCl_G4 label:F[C](F)OCl smiles:F[C](F)OCl H298:-67.70 kcal/mol
library:CHOFCl_G4 label:F[C](F)OCOCl smiles:F[C](F)OCOCl H298:-111.50 kcal/mol
library:CHOFCl_G4 label:F[C](F)OC(Cl)Cl smiles:F[C](F)OC(Cl)Cl H298:-112.42 kcal/mol
library:CHOFCl_G4 label:F[C](F)OCCl smiles:F[C](F)OCCl H298:-109.87 kcal/mol
library:CHOFClBr_G4 label:F[C](F)OC(Cl)Br smiles:F[C](F)OC(Cl)Br H298:-100.10 kcal/mol
library:CHOFBr_G4 label:F[C](F)OC(Br)Br smiles:F[C](F)OC(Br)Br H298:-87.68 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)O[C](F)F smiles:OC(Br)(Br)O[C](F)F H298:-130.91 kcal/mol
library:CHOFBr_G4 label:F[C](F)OC(F)OBr smiles:F[C](F)OC(F)OBr H298:-161.51 kcal/mol
library:CHOFBr_G4 label:F[C](F)OCBr smiles:F[C](F)OCBr H298:-97.93 kcal/mol
library:CHOFBr_G4 label:F[C](F)OC(F)(Br)Br smiles:F[C](F)OC(F)(Br)Br H298:-134.38 kcal/mol
library:CHOFBr_G4 label:F[C](F)OC(F)(F)Br smiles:F[C](F)OC(F)(F)Br H298:-197.95 kcal/mol
library:CHOFBr_G4 label:F[C](F)OCOBr smiles:F[C](F)OCOBr H298:-108.51 kcal/mol
library:CHOFBr_G4 label:F[C](F)OOCBr smiles:F[C](F)OOCBr H298:-78.34 kcal/mol
library:CHOFBr_G4 label:OC(F)(Br)O[C](F)F smiles:OC(F)(Br)O[C](F)F H298:-193.78 kcal/mol
library:CHOFBr_G4 label:OC(Br)O[C](F)F smiles:OC(Br)O[C](F)F H298:-141.74 kcal/mol
library:CHOFBr_G4 label:F[C](F)OOBr smiles:F[C](F)OOBr H298:-46.86 kcal/mol
library:CHOFBr_G4 label:F[C](F)OC(Br)(Br)Br smiles:F[C](F)OC(Br)(Br)Br H298:-75.72 kcal/mol
library:CHOFBr_G4 label:F[C](F)OOC(F)Br smiles:F[C](F)OOC(F)Br H298:-125.89 kcal/mol
library:CHOFBr_G4 label:ODC(Br)O[C](F)F smiles:O=C(Br)O[C](F)F H298:-131.58 kcal/mol
library:CHOFBr_G4 label:F[C](F)OC(Br)OBr smiles:F[C](F)OC(Br)OBr H298:-101.64 kcal/mol
library:CHOFBr_G4 label:F[C](F)OOC(Br)Br smiles:F[C](F)OOC(Br)Br H298:-69.42 kcal/mol
library:CHOFBr_G4 label:F[C](F)OC(F)Br smiles:F[C](F)OC(F)Br H298:-145.57 kcal/mol
""",
)

entry(
    index = 34,
    label = "CsBr1sHO2s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   O2s  u0 {1,S}
3   H    u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.629793,-0.122125,-1.03566,-1.77356,-2.89316,-3.67298,-4.81233],'cal/(mol*K)','+|-',[0.201761,0.207157,0.194235,0.18142,0.160107,0.140106,0.102616]),
        H298 = (96.8602,'kcal/mol','+|-',0.322312),
        S298 = (0.903069,'cal/(mol*K)','+|-',0.547755),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:Br[CH]OCC(Br)Br smiles:Br[CH]OCC(Br)Br H298:6.86 kcal/mol
library:CHOBr_G4 label:Br[CH]OCCBr smiles:Br[CH]OCCBr H298:-0.43 kcal/mol
library:CHOBr_G4 label:C#CO[CH]Br smiles:C#CO[CH]Br H298:79.18 kcal/mol
library:CHOBr_G4 label:O[CH]Br smiles:O[CH]Br H298:-2.09 kcal/mol
library:CHOBr_G4 label:CC(Br)(Br)O[CH]Br smiles:CC(Br)(Br)O[CH]Br H298:2.29 kcal/mol
library:CHOBr_G4 label:Br[CH]OC(Br)CBr smiles:Br[CH]OC(Br)CBr H298:4.78 kcal/mol
library:CHOBr_G4 label:OC(Br)O[CH]Br smiles:OC(Br)O[CH]Br H298:-38.35 kcal/mol
library:CHOBr_G4 label:CDC(Br)O[CH]Br smiles:C=C(Br)O[CH]Br H298:29.18 kcal/mol
library:CHOBr_G4 label:CO[CH]Br smiles:CO[CH]Br H298:1.50 kcal/mol
library:CHOBr_G4 label:Br[CH]OCDC(Br)Br smiles:Br[CH]OC=C(Br)Br H298:38.34 kcal/mol
library:CHOBr_G4 label:Br[CH]OCDCBr smiles:Br[CH]OC=CBr H298:30.02 kcal/mol
library:CHOBr_G4 label:BrC#CO[CH]Br smiles:BrC#CO[CH]Br H298:90.90 kcal/mol
library:CHOBr_G4 label:Br[CH]OC(Br)Br smiles:Br[CH]OC(Br)Br H298:15.21 kcal/mol
library:CHOBr_G4 label:ODC(Br)O[CH]Br smiles:O=C(Br)O[CH]Br H298:-29.01 kcal/mol
library:CHOBr_G4 label:Br[CH]OC(Br)OBr smiles:Br[CH]OC(Br)OBr H298:2.40 kcal/mol
library:CHOBr_G4 label:CDCO[CH]Br smiles:C=CO[CH]Br H298:23.34 kcal/mol
library:CHOBr_G4 label:OCO[CH]Br smiles:OCO[CH]Br H298:-41.49 kcal/mol
library:CHOBr_G4 label:Br[CH]OCBr smiles:Br[CH]OCBr H298:6.53 kcal/mol
library:CHOBr_G4 label:CCO[CH]Br smiles:CCO[CH]Br H298:-6.70 kcal/mol
library:CHOBr_G4 label:ODCO[CH]Br smiles:O=CO[CH]Br H298:-32.90 kcal/mol
library:CHOBr_G4 label:CC(Br)O[CH]Br smiles:CC(Br)O[CH]Br H298:-4.82 kcal/mol
library:CHOBr_G4 label:Br[CH]OCOBr smiles:Br[CH]OCOBr H298:-3.35 kcal/mol
library:CHOFBr_G4 label:FC#CO[CH]Br smiles:FC#CO[CH]Br H298:54.11 kcal/mol
library:CHOClBr_G4 label:ClC#CO[CH]Br smiles:ClC#CO[CH]Br H298:80.28 kcal/mol
""",
)

entry(
    index = 35,
    label = "CsCl1sHO2s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   O2s  u0 {1,S}
3   H    u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.524045,-0.359509,-1.27024,-1.9772,-3.02444,-3.7292,-4.68416],'cal/(mol*K)','+|-',[0.147346,0.151286,0.141849,0.132491,0.116926,0.102319,0.0749404]),
        H298 = (96.3059,'kcal/mol','+|-',0.235383),
        S298 = (1.09883,'cal/(mol*K)','+|-',0.400023),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:ATcT_halogens label:Chlorohydroxymethyl smiles:O[CH]Cl H298:-14.48 kcal/mol
library:CHOCl_G4 label:CDC(Cl)O[CH]Cl smiles:C=C(Cl)O[CH]Cl H298:4.88 kcal/mol
library:CHOCl_G4 label:Cl[CH]OCC(Cl)(Cl)Cl smiles:Cl[CH]OCC(Cl)(Cl)Cl H298:-30.84 kcal/mol
library:CHOCl_G4 label:Cl[CH]OC(Cl)DC(Cl)Cl smiles:Cl[CH]OC(Cl)=C(Cl)Cl H298:-1.52 kcal/mol
library:CHOCl_G4 label:ODCO[CH]Cl smiles:O=CO[CH]Cl H298:-45.80 kcal/mol
library:CHOCl_G4 label:CCO[CH]Cl smiles:CCO[CH]Cl H298:-18.71 kcal/mol
library:CHOCl_G4 label:Cl[CH]OCCCl smiles:Cl[CH]OCCCl H298:-23.41 kcal/mol
library:CHOCl_G4 label:Cl[CH]OC(Cl)(Cl)Cl smiles:Cl[CH]OC(Cl)(Cl)Cl H298:-22.85 kcal/mol
library:CHOCl_G4 label:Cl[CH]OCDCCl smiles:Cl[CH]OC=CCl H298:6.26 kcal/mol
library:CHOCl_G4 label:OC(Cl)O[CH]Cl smiles:OC(Cl)O[CH]Cl H298:-63.04 kcal/mol
library:CHOCl_G4 label:OCO[CH]Cl smiles:OCO[CH]Cl H298:-53.24 kcal/mol
library:CHOCl_G4 label:CDCO[CH]Cl smiles:C=CO[CH]Cl H298:11.15 kcal/mol
library:CHOCl_G4 label:Cl[CH]OC(Cl)C(Cl)(Cl)Cl smiles:Cl[CH]OC(Cl)C(Cl)(Cl)Cl H298:-35.87 kcal/mol
library:CHOCl_G4 label:Cl[CH]OC(Cl)OCl smiles:Cl[CH]OC(Cl)OCl H298:-23.71 kcal/mol
library:CHOCl_G4 label:Cl[CH]OC(Cl)(Cl)C(Cl)(Cl)Cl smiles:Cl[CH]OC(Cl)(Cl)C(Cl)(Cl)Cl H298:-38.85 kcal/mol
library:CHOCl_G4 label:Cl[CH]OC(Cl)(Cl)OCl smiles:Cl[CH]OC(Cl)(Cl)OCl H298:-28.03 kcal/mol
library:CHOCl_G4 label:Cl[CH]OC(Cl)(Cl)CCl smiles:Cl[CH]OC(Cl)(Cl)CCl H298:-36.45 kcal/mol
library:CHOCl_G4 label:CC(Cl)O[CH]Cl smiles:CC(Cl)O[CH]Cl H298:-28.79 kcal/mol
library:CHOCl_G4 label:OC(Cl)(Cl)O[CH]Cl smiles:OC(Cl)(Cl)O[CH]Cl H298:-65.93 kcal/mol
library:CHOCl_G4 label:CO[CH]Cl smiles:CO[CH]Cl H298:-10.57 kcal/mol
library:CHOCl_G4 label:Cl[CH]OC(Cl)(Cl)C(Cl)Cl smiles:Cl[CH]OC(Cl)(Cl)C(Cl)Cl H298:-38.44 kcal/mol
library:CHOCl_G4 label:Cl[CH]OC(Cl)CCl smiles:Cl[CH]OC(Cl)CCl H298:-32.55 kcal/mol
library:CHOCl_G4 label:Cl[CH]OCCl smiles:Cl[CH]OCCl H298:-17.42 kcal/mol
library:CHOCl_G4 label:ClC#CO[CH]Cl smiles:ClC#CO[CH]Cl H298:67.88 kcal/mol
library:CHOCl_G4 label:Cl[CH]OC(Cl)Cl smiles:Cl[CH]OC(Cl)Cl H298:-21.61 kcal/mol
library:CHOCl_G4 label:Cl[CH]OCOCl smiles:Cl[CH]OCOCl H298:-18.46 kcal/mol
library:CHOCl_G4 label:Cl[CH]OC(Cl)C(Cl)Cl smiles:Cl[CH]OC(Cl)C(Cl)Cl H298:-34.93 kcal/mol
library:CHOCl_G4 label:CC(Cl)(Cl)O[CH]Cl smiles:CC(Cl)(Cl)O[CH]Cl H298:-34.46 kcal/mol
library:CHOCl_G4 label:Cl[CH]OCC(Cl)Cl smiles:Cl[CH]OCC(Cl)Cl H298:-28.51 kcal/mol
library:CHOCl_G4 label:C#CO[CH]Cl smiles:C#CO[CH]Cl H298:66.70 kcal/mol
library:CHOCl_G4 label:ODC(Cl)O[CH]Cl smiles:O=C(Cl)O[CH]Cl H298:-54.47 kcal/mol
library:CHOFCl_G4 label:FC#CO[CH]Cl smiles:FC#CO[CH]Cl H298:41.69 kcal/mol
library:CHOClBr_G4 label:OC(Cl)(Br)O[CH]Cl smiles:OC(Cl)(Br)O[CH]Cl H298:-53.38 kcal/mol
library:CHOClBr_G4 label:Cl[CH]OC(Br)(Br)Br smiles:Cl[CH]OC(Br)(Br)Br H298:13.88 kcal/mol
library:CHOClBr_G4 label:Cl[CH]OCOBr smiles:Cl[CH]OCOBr H298:-15.33 kcal/mol
library:CHOClBr_G4 label:Cl[CH]OC(Cl)Br smiles:Cl[CH]OC(Cl)Br H298:-9.51 kcal/mol
library:CHOClBr_G4 label:Cl[CH]OCBr smiles:Cl[CH]OCBr H298:-5.67 kcal/mol
library:CHOClBr_G4 label:Cl[CH]OC(Br)Br smiles:Cl[CH]OC(Br)Br H298:2.51 kcal/mol
library:CHOClBr_G4 label:ODC(Br)O[CH]Cl smiles:O=C(Br)O[CH]Cl H298:-41.73 kcal/mol
library:CHOClBr_G4 label:OC(Br)O[CH]Cl smiles:OC(Br)O[CH]Cl H298:-48.99 kcal/mol
library:CHOClBr_G4 label:Cl[CH]OC(Cl)(Br)Br smiles:Cl[CH]OC(Cl)(Br)Br H298:1.66 kcal/mol
library:CHOClBr_G4 label:Cl[CH]OC(Cl)OBr smiles:Cl[CH]OC(Cl)OBr H298:-22.74 kcal/mol
library:CHOClBr_G4 label:OC(Br)(Br)O[CH]Cl smiles:OC(Br)(Br)O[CH]Cl H298:-40.93 kcal/mol
library:CHOClBr_G4 label:Cl[CH]OC(Cl)(Cl)Br smiles:Cl[CH]OC(Cl)(Cl)Br H298:-10.52 kcal/mol
library:CHOClBr_G4 label:Cl[CH]OC(Br)OBr smiles:Cl[CH]OC(Br)OBr H298:-10.07 kcal/mol
""",
)

entry(
    index = 36,
    label = "CsF1sHO2s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S}
3   H   u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.039582,-0.708448,-1.40904,-2.00234,-2.94186,-3.62167,-4.60136],'cal/(mol*K)','+|-',[0.119864,0.12307,0.115393,0.10778,0.0951178,0.0832352,0.0609632]),
        H298 = (99.775,'kcal/mol','+|-',0.191482),
        S298 = (1.67663,'cal/(mol*K)','+|-',0.325415),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:CC(F)O[CH]F smiles:CC(F)O[CH]F H298:-112.62 kcal/mol
library:CHOF_G4 label:F[CH]OC(F)(F)OF smiles:F[CH]OC(F)(F)OF H298:-167.66 kcal/mol
library:CHOF_G4 label:F[CH]OC(F)CF smiles:F[CH]OC(F)CF H298:-152.33 kcal/mol
library:CHOF_G4 label:F[CH]OCC(F)(F)F smiles:F[CH]OCC(F)(F)F H298:-212.22 kcal/mol
library:CHOF_G4 label:F[CH]OCOF smiles:F[CH]OCOF H298:-63.51 kcal/mol
library:CHOF_G4 label:F[CH]OC(F)(F)CF smiles:F[CH]OC(F)(F)CF H298:-206.71 kcal/mol
library:CHOF_G4 label:F[CH]OC(F)OF smiles:F[CH]OC(F)OF H298:-113.99 kcal/mol
library:CHOF_G4 label:F[CH]OCCF smiles:F[CH]OCCF H298:-101.64 kcal/mol
library:CHOF_G4 label:F[CH]OC(F)(F)F smiles:F[CH]OC(F)(F)F H298:-211.72 kcal/mol
library:CHOF_G4 label:F[CH]OC(F)DCF smiles:F[CH]OC(F)=CF H298:-112.92 kcal/mol
library:CHOF_G4 label:OC(F)(F)O[CH]F smiles:OC(F)(F)O[CH]F H298:-206.05 kcal/mol
library:CHOF_G4 label:OCO[CH]F smiles:OCO[CH]F H298:-93.91 kcal/mol
library:CHOF_G4 label:ODCO[CH]F smiles:O=CO[CH]F H298:-85.16 kcal/mol
library:CHOF_G4 label:F[CH]OC(F)C(F)(F)F smiles:F[CH]OC(F)C(F)(F)F H298:-260.28 kcal/mol
library:CHOF_G4 label:F[CH]OCDCF smiles:F[CH]OC=CF H298:-69.53 kcal/mol
library:CHOF_G4 label:C#CO[CH]F smiles:C#CO[CH]F H298:26.91 kcal/mol
library:CHOF_G4 label:CDCO[CH]F smiles:C=CO[CH]F H298:-28.45 kcal/mol
library:CHOF_G4 label:ODC(F)O[CH]F smiles:O=C(F)O[CH]F H298:-140.25 kcal/mol
library:CHOF_G4 label:FC#CO[CH]F smiles:FC#CO[CH]F H298:2.19 kcal/mol
library:CHOF_G4 label:F[CH]OC(F)(F)C(F)F smiles:F[CH]OC(F)(F)C(F)F H298:-256.57 kcal/mol
library:CHOF_G4 label:O[CH]F smiles:O[CH]F H298:-55.34 kcal/mol
library:CHOF_G4 label:OC(F)O[CH]F smiles:OC(F)O[CH]F H298:-149.95 kcal/mol
library:CHOF_G4 label:CC(F)(F)O[CH]F smiles:CC(F)(F)O[CH]F H298:-169.37 kcal/mol
library:CHOF_G4 label:F[CH]OC(F)(F)C(F)(F)F smiles:F[CH]OC(F)(F)C(F)(F)F H298:-312.34 kcal/mol
library:CHOF_G4 label:F[CH]OCDC(F)F smiles:F[CH]OC=C(F)F H298:-114.87 kcal/mol
library:CHOF_G4 label:CDC(F)O[CH]F smiles:C=C(F)O[CH]F H298:-75.81 kcal/mol
library:CHOF_G4 label:CO[CH]F smiles:CO[CH]F H298:-50.61 kcal/mol
library:CHOF_G4 label:F[CH]OC(F)F smiles:F[CH]OC(F)F H298:-155.64 kcal/mol
library:CHOF_G4 label:F[CH]OCC(F)F smiles:F[CH]OCC(F)F H298:-154.41 kcal/mol
library:CHOF_G4 label:F[CH]OCF smiles:F[CH]OCF H298:-99.81 kcal/mol
library:CHOF_G4 label:F[CH]OC(F)C(F)F smiles:F[CH]OC(F)C(F)F H298:-203.78 kcal/mol
library:CHOF_G4 label:F[CH]OC(F)DC(F)F smiles:F[CH]OC(F)=C(F)F H298:-156.22 kcal/mol
library:CHOF_G4 label:CCO[CH]F smiles:CCO[CH]F H298:-58.89 kcal/mol
library:CHOFCl_G4 label:ODC(Cl)O[CH]F smiles:O=C(Cl)O[CH]F H298:-93.60 kcal/mol
library:CHOFCl_G4 label:F[CH]OC(Cl)Cl smiles:F[CH]OC(Cl)Cl H298:-60.69 kcal/mol
library:CHOFCl_G4 label:F[CH]OCOCl smiles:F[CH]OCOCl H298:-58.27 kcal/mol
library:CHOFCl_G4 label:F[CH]OC(F)(Cl)Cl smiles:F[CH]OC(F)(Cl)Cl H298:-108.95 kcal/mol
library:CHOFCl_G4 label:F[CH]OC(F)OCl smiles:F[CH]OC(F)OCl H298:-111.52 kcal/mol
library:CHOFCl_G4 label:OC(Cl)(Cl)O[CH]F smiles:OC(Cl)(Cl)O[CH]F H298:-104.94 kcal/mol
library:CHOFCl_G4 label:OC(F)(Cl)O[CH]F smiles:OC(F)(Cl)O[CH]F H298:-154.35 kcal/mol
library:CHOFCl_G4 label:OC(Cl)O[CH]F smiles:OC(Cl)O[CH]F H298:-102.58 kcal/mol
library:CHOFCl_G4 label:F[CH]OC(Cl)OCl smiles:F[CH]OC(Cl)OCl H298:-63.84 kcal/mol
library:CHOFCl_G4 label:F[CH]OC(F)(F)Cl smiles:F[CH]OC(F)(F)Cl H298:-159.33 kcal/mol
library:CHOFCl_G4 label:F[CH]OCCl smiles:F[CH]OCCl H298:-57.00 kcal/mol
library:CHOFCl_G4 label:F[CH]OC(F)Cl smiles:F[CH]OC(F)Cl H298:-106.23 kcal/mol
library:CHOFCl_G4 label:F[CH]OC(Cl)(Cl)Cl smiles:F[CH]OC(Cl)(Cl)Cl H298:-61.72 kcal/mol
library:CHOFClBr_G4 label:F[CH]OC(Cl)(Cl)Br smiles:F[CH]OC(Cl)(Cl)Br H298:-49.23 kcal/mol
library:CHOFClBr_G4 label:F[CH]OC(Cl)OBr smiles:F[CH]OC(Cl)OBr H298:-62.08 kcal/mol
library:CHOFClBr_G4 label:F[CH]OC(Cl)(Br)Br smiles:F[CH]OC(Cl)(Br)Br H298:-36.96 kcal/mol
library:CHOFClBr_G4 label:F[CH]OC(F)(Cl)Br smiles:F[CH]OC(F)(Cl)Br H298:-95.92 kcal/mol
library:CHOFClBr_G4 label:OC(Cl)(Br)O[CH]F smiles:OC(Cl)(Br)O[CH]F H298:-92.36 kcal/mol
library:CHOFClBr_G4 label:F[CH]OC(Cl)Br smiles:F[CH]OC(Cl)Br H298:-48.47 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)O[CH]F smiles:OC(Br)(Br)O[CH]F H298:-79.77 kcal/mol
library:CHOFBr_G4 label:F[CH]OC(F)(Br)OBr smiles:F[CH]OC(F)(Br)OBr H298:-100.53 kcal/mol
library:CHOFBr_G4 label:OC(F)(Br)O[CH]F smiles:OC(F)(Br)O[CH]F H298:-141.46 kcal/mol
library:CHOFBr_G4 label:OC(Br)O[CH]F smiles:OC(Br)O[CH]F H298:-89.99 kcal/mol
library:CHOFBr_G4 label:F[CH]OC(F)Br smiles:F[CH]OC(F)Br H298:-93.19 kcal/mol
library:CHOFBr_G4 label:F[CH]OCBr smiles:F[CH]OCBr H298:-45.14 kcal/mol
library:CHOFBr_G4 label:F[CH]OC(F)(F)Br smiles:F[CH]OC(F)(F)Br H298:-146.09 kcal/mol
library:CHOFBr_G4 label:F[CH]OC(Br)OBr smiles:F[CH]OC(Br)OBr H298:-49.92 kcal/mol
library:CHOFBr_G4 label:F[CH]OC(Br)Br smiles:F[CH]OC(Br)Br H298:-36.37 kcal/mol
library:CHOFBr_G4 label:F[CH]OC(F)(F)OBr smiles:F[CH]OC(F)(F)OBr H298:-163.20 kcal/mol
library:CHOFBr_G4 label:F[CH]OC(Br)(Br)OBr smiles:F[CH]OC(Br)(Br)OBr H298:-40.30 kcal/mol
library:CHOFBr_G4 label:F[CH]OC(F)(Br)Br smiles:F[CH]OC(F)(Br)Br H298:-83.05 kcal/mol
library:CHOFBr_G4 label:F[CH]OC(F)OBr smiles:F[CH]OC(F)OBr H298:-109.27 kcal/mol
library:CHOFBr_G4 label:ODC(Br)O[CH]F smiles:O=C(Br)O[CH]F H298:-80.74 kcal/mol
library:CHOFBr_G4 label:F[CH]OC(Br)(Br)Br smiles:F[CH]OC(Br)(Br)Br H298:-24.69 kcal/mol
library:CHOFBr_G4 label:F[CH]OCOBr smiles:F[CH]OCOBr H298:-55.12 kcal/mol
""",
)

entry(
    index = 37,
    label = "CsBr1sO2sO2s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   O2s  u0 {1,S}
3   O2s  u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.275161,-0.975235,-1.93766,-2.58804,-3.58001,-4.29315,-5.22963],'cal/(mol*K)','+|-',[0.298021,0.305991,0.286904,0.267976,0.236494,0.20695,0.151574]),
        H298 = (94.906,'kcal/mol','+|-',0.476086),
        S298 = (3.74502,'cal/(mol*K)','+|-',0.809087),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:O[C](Br)OCBr smiles:O[C](Br)OCBr H298:-40.29 kcal/mol
library:CHOBr_G4 label:O[C](O)Br smiles:O[C](O)Br H298:-48.69 kcal/mol
library:CHOBr_G4 label:CO[C](O)Br smiles:CO[C](O)Br H298:-45.71 kcal/mol
library:CHOBr_G4 label:O[C](Br)OC(Br)Br smiles:O[C](Br)OC(Br)Br H298:-31.05 kcal/mol
library:CHOFBr_G4 label:O[C](Br)OC(F)(F)Br smiles:O[C](Br)OC(F)(F)Br H298:-139.54 kcal/mol
library:CHOFBr_G4 label:O[C](Br)OC(F)Br smiles:O[C](Br)OC(F)Br H298:-87.52 kcal/mol
library:CHOFBr_G4 label:O[C](Br)OCF smiles:O[C](Br)OCF H298:-94.16 kcal/mol
library:CHOFBr_G4 label:O[C](Br)OC(F)(Br)Br smiles:O[C](Br)OC(F)(Br)Br H298:-76.72 kcal/mol
library:CHOFBr_G4 label:O[C](Br)OC(F)(F)F smiles:O[C](Br)OC(F)(F)F H298:-204.72 kcal/mol
library:CHOFBr_G4 label:O[C](Br)OC(F)F smiles:O[C](Br)OC(F)F H298:-149.37 kcal/mol
library:CHOClBr_G4 label:O[C](Br)OCCl smiles:O[C](Br)OCCl H298:-52.05 kcal/mol
""",
)

entry(
    index = 38,
    label = "CsCl1sO2sO2s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   O2s  u0 {1,S}
3   O2s  u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.492434,-2.3146,-3.29062,-3.80665,-4.50572,-4.90385,-5.24337],'cal/(mol*K)','+|-',[0.403522,0.414314,0.38847,0.362841,0.320214,0.280211,0.205233]),
        H298 = (96.2474,'kcal/mol','+|-',0.644623),
        S298 = (4.22306,'cal/(mol*K)','+|-',1.09551),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOCl_G4 label:O[C](Cl)OCCl smiles:O[C](Cl)OCCl H298:-63.45 kcal/mol
library:CHOCl_G4 label:O[C](Cl)OC(Cl)(Cl)Cl smiles:O[C](Cl)OC(Cl)(Cl)Cl H298:-67.57 kcal/mol
library:CHOCl_G4 label:CO[C](O)Cl smiles:CO[C](O)Cl H298:-56.64 kcal/mol
library:CHOCl_G4 label:O[C](O)Cl smiles:O[C](O)Cl H298:-60.22 kcal/mol
library:CHOCl_G4 label:O[C](Cl)OC(Cl)Cl smiles:O[C](Cl)OC(Cl)Cl H298:-66.96 kcal/mol
library:CHOFCl_G4 label:O[C](Cl)OCF smiles:O[C](Cl)OCF H298:-105.67 kcal/mol
""",
)

entry(
    index = 39,
    label = "CsF1sO2sO2s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S}
3   O2s u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.00139,-2.69591,-2.86385,-3.05773,-3.46676,-3.76913,-4.21476],'cal/(mol*K)','+|-',[0.349461,0.358807,0.336425,0.314229,0.277314,0.24267,0.177737]),
        H298 = (101.088,'kcal/mol','+|-',0.55826),
        S298 = (2.94024,'cal/(mol*K)','+|-',0.948739),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:CO[C](O)F smiles:CO[C](O)F H298:-100.56 kcal/mol
library:CHOF_G4 label:O[C](F)OC(F)(F)F smiles:O[C](F)OC(F)(F)F H298:-261.49 kcal/mol
library:CHOF_G4 label:O[C](F)OC(F)F smiles:O[C](F)OC(F)F H298:-204.64 kcal/mol
library:CHOF_G4 label:O[C](O)F smiles:O[C](O)F H298:-105.00 kcal/mol
library:CHOF_G4 label:O[C](F)OCF smiles:O[C](F)OCF H298:-149.59 kcal/mol
library:CHOFCl_G4 label:O[C](F)OCl smiles:O[C](F)OCl H298:-65.16 kcal/mol
library:CHOFCl_G4 label:FCO[C](F)OCl smiles:FCO[C](F)OCl H298:-109.57 kcal/mol
library:CHOFBr_G4 label:O[C](F)OBr smiles:O[C](F)OBr H298:-62.92 kcal/mol
""",
)

entry(
    index = 40,
    label = "CsBr1sBr1sCt",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Ct   u0 {1,S}
3   Br1s u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.21489,-0.93447,-1.57481,-2.12517,-2.97707,-3.60224,-4.53857],'cal/(mol*K)','+|-',[0.373589,0.38358,0.359654,0.335925,0.296461,0.259425,0.190009]),
        H298 = (84.717,'kcal/mol','+|-',0.596805),
        S298 = (-0.10693,'cal/(mol*K)','+|-',1.01424),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:OC#C[C](Br)Br smiles:OC#C[C](Br)Br H298:64.17 kcal/mol
library:CHOBr_G4 label:BrCC#C[C](Br)Br smiles:BrCC#C[C](Br)Br H298:94.26 kcal/mol
library:CHOBr_G4 label:C#C[C](Br)Br smiles:C#C[C](Br)Br H298:96.44 kcal/mol
library:CHOBr_G4 label:BrC#C[C](Br)Br smiles:BrC#C[C](Br)Br H298:106.50 kcal/mol
library:CHOBr_G4 label:CC#C[C](Br)Br smiles:CC#C[C](Br)Br H298:84.96 kcal/mol
library:CHOFBr_G4 label:FC#C[C](Br)Br smiles:FC#C[C](Br)Br H298:69.51 kcal/mol
library:CHOClBr_G4 label:ClC#C[C](Br)Br smiles:ClC#C[C](Br)Br H298:95.68 kcal/mol
""",
)

entry(
    index = 41,
    label = "CsBr1sCl1sCt",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Ct   u0 {1,S}
3   Cl1s u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.165006,-0.817023,-1.4403,-2.0269,-2.96678,-3.60706,-4.49955],'cal/(mol*K)','+|-',[0.494212,0.507429,0.475777,0.444387,0.392181,0.343187,0.251358]),
        H298 = (84.5995,'kcal/mol','+|-',0.789499),
        S298 = (1.89344,'cal/(mol*K)','+|-',1.34172),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFClBr_G4 label:FC#C[C](Cl)Br smiles:FC#C[C](Cl)Br H298:57.97 kcal/mol
library:CHOClBr_G4 label:C#C[C](Cl)Br smiles:C#C[C](Cl)Br H298:84.90 kcal/mol
library:CHOClBr_G4 label:OC#C[C](Cl)Br smiles:OC#C[C](Cl)Br H298:52.70 kcal/mol
library:CHOClBr_G4 label:CC#C[C](Cl)Br smiles:CC#C[C](Cl)Br H298:73.43 kcal/mol
""",
)

entry(
    index = 42,
    label = "CsCl1sCl1sCt",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Ct   u0 {1,S}
3   Cl1s u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.133831,-0.661626,-1.32915,-1.88401,-2.76851,-3.4241,-4.40174],'cal/(mol*K)','+|-',[0.329475,0.338286,0.317185,0.296258,0.261454,0.228792,0.167572]),
        H298 = (83.5772,'kcal/mol','+|-',0.526333),
        S298 = (1.08754,'cal/(mol*K)','+|-',0.894479),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOCl_G4 label:Cl[C](Cl)C#CC(Cl)Cl smiles:Cl[C](Cl)C#CC(Cl)Cl H298:58.82 kcal/mol
library:CHOCl_G4 label:CC#C[C](Cl)Cl smiles:CC#C[C](Cl)Cl H298:61.75 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)C#CC(Cl)(Cl)Cl smiles:Cl[C](Cl)C#CC(Cl)(Cl)Cl H298:58.20 kcal/mol
library:CHOCl_G4 label:ClC#C[C](Cl)Cl smiles:ClC#C[C](Cl)Cl H298:72.61 kcal/mol
library:CHOCl_G4 label:ClCC#C[C](Cl)Cl smiles:ClCC#C[C](Cl)Cl H298:60.65 kcal/mol
library:CHOCl_G4 label:OC#C[C](Cl)Cl smiles:OC#C[C](Cl)Cl H298:40.93 kcal/mol
library:CHOCl_G4 label:C#C[C](Cl)Cl smiles:C#C[C](Cl)Cl H298:73.15 kcal/mol
library:CHOFCl_G4 label:FC#C[C](Cl)Cl smiles:FC#C[C](Cl)Cl H298:46.20 kcal/mol
library:CHOClBr_G4 label:Cl[C](Cl)C#CCBr smiles:Cl[C](Cl)C#CCBr H298:71.18 kcal/mol
""",
)

entry(
    index = 43,
    label = "CsBr1sCtF1s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Ct   u0 {1,S}
3   F1s  u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.539106,-0.448781,-1.16805,-1.75893,-2.71247,-3.41714,-4.45553],'cal/(mol*K)','+|-',[0.988423,1.01486,0.951553,0.888774,0.784361,0.686374,0.502715]),
        H298 = (88.5852,'kcal/mol','+|-',1.579),
        S298 = (4.01696,'cal/(mol*K)','+|-',2.68344),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFBr_G4 label:C#C[C](F)Br smiles:C#C[C](F)Br H298:49.16 kcal/mol
""",
)

entry(
    index = 44,
    label = "CsCl1sCtF1s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Ct   u0 {1,S}
3   F1s  u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.255028,-0.587165,-1.32361,-1.94622,-2.93492,-3.64566,-4.67423],'cal/(mol*K)','+|-',[0.442037,0.453859,0.425548,0.397472,0.350777,0.306956,0.224821]),
        H298 = (88.4593,'kcal/mol','+|-',0.706149),
        S298 = (1.85933,'cal/(mol*K)','+|-',1.20007),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFCl_G4 label:OC#C[C](F)Cl smiles:OC#C[C](F)Cl H298:3.93 kcal/mol
library:CHOFCl_G4 label:FC#C[C](F)Cl smiles:FC#C[C](F)Cl H298:9.13 kcal/mol
library:CHOFCl_G4 label:CC#C[C](F)Cl smiles:CC#C[C](F)Cl H298:25.24 kcal/mol
library:CHOFCl_G4 label:C#C[C](F)Cl smiles:C#C[C](F)Cl H298:36.61 kcal/mol
library:CHOFClBr_G4 label:F[C](Cl)C#CCBr smiles:F[C](Cl)C#CCBr H298:34.76 kcal/mol
""",
)

entry(
    index = 45,
    label = "CsCtF1sF1s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Ct  u0 {1,S}
3   F1s u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.905589,0.0858261,-0.690337,-1.35881,-2.42239,-3.19995,-4.33111],'cal/(mol*K)','+|-',[0.349461,0.358807,0.336425,0.314229,0.277314,0.24267,0.177737]),
        H298 = (93.9781,'kcal/mol','+|-',0.55826),
        S298 = (0.54969,'cal/(mol*K)','+|-',0.948739),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:FCC#C[C](F)F smiles:FCC#C[C](F)F H298:-52.89 kcal/mol
library:CHOF_G4 label:F[C](F)C#CC(F)F smiles:F[C](F)C#CC(F)F H298:-101.85 kcal/mol
library:CHOF_G4 label:CC#C[C](F)F smiles:CC#C[C](F)F H298:-13.55 kcal/mol
library:CHOF_G4 label:F[C](F)C#CC(F)(F)F smiles:F[C](F)C#CC(F)(F)F H298:-157.63 kcal/mol
library:CHOF_G4 label:C#C[C](F)F smiles:C#C[C](F)F H298:-2.28 kcal/mol
library:CHOF_G4 label:OC#C[C](F)F smiles:OC#C[C](F)F H298:-36.18 kcal/mol
library:CHOFCl_G4 label:F[C](F)C#CCCl smiles:F[C](F)C#CCCl H298:-14.68 kcal/mol
library:CHOFBr_G4 label:F[C](F)C#CC(F)Br smiles:F[C](F)C#CC(F)Br H298:-44.59 kcal/mol
""",
)

entry(
    index = 46,
    label = "CsBr1sCtH",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Ct   u0 {1,S}
3   H    u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.170266,-0.456527,-1.08903,-1.65478,-2.59458,-3.31711,-4.43644],'cal/(mol*K)','+|-',[0.349461,0.358807,0.336425,0.314229,0.277314,0.24267,0.177737]),
        H298 = (87.4241,'kcal/mol','+|-',0.55826),
        S298 = (1.04323,'cal/(mol*K)','+|-',0.948739),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:BrC#C[CH]Br smiles:BrC#C[CH]Br H298:99.70 kcal/mol
library:CHOBr_G4 label:CC#C[CH]Br smiles:CC#C[CH]Br H298:78.32 kcal/mol
library:CHOBr_G4 label:C#C[CH]Br smiles:C#C[CH]Br H298:89.37 kcal/mol
library:CHOBr_G4 label:Br[CH]C#CC(Br)Br smiles:Br[CH]C#CC(Br)Br H298:96.94 kcal/mol
library:CHOBr_G4 label:Br[CH]C#CCBr smiles:Br[CH]C#CCBr H298:87.61 kcal/mol
library:CHOBr_G4 label:OC#C[CH]Br smiles:OC#C[CH]Br H298:57.80 kcal/mol
library:CHOFBr_G4 label:FC#C[CH]Br smiles:FC#C[CH]Br H298:62.46 kcal/mol
library:CHOClBr_G4 label:ClC#C[CH]Br smiles:ClC#C[CH]Br H298:88.83 kcal/mol
""",
)

entry(
    index = 47,
    label = "CsCl1sCtH",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Ct   u0 {1,S}
3   H    u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.333212,-0.276249,-0.893023,-1.4563,-2.41933,-3.17148,-4.33331],'cal/(mol*K)','+|-',[0.312567,0.320926,0.300908,0.281055,0.248037,0.217051,0.158973]),
        H298 = (86.3701,'kcal/mol','+|-',0.499323),
        S298 = (1.70185,'cal/(mol*K)','+|-',0.848578),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOCl_G4 label:OC#C[CH]Cl smiles:OC#C[CH]Cl H298:46.06 kcal/mol
library:CHOCl_G4 label:C#C[CH]Cl smiles:C#C[CH]Cl H298:77.65 kcal/mol
library:CHOCl_G4 label:CC#C[CH]Cl smiles:CC#C[CH]Cl H298:66.78 kcal/mol
library:CHOCl_G4 label:ClC#C[CH]Cl smiles:ClC#C[CH]Cl H298:77.21 kcal/mol
library:CHOCl_G4 label:Cl[CH]C#CCCl smiles:Cl[CH]C#CCCl H298:65.28 kcal/mol
library:CHOCl_G4 label:Cl[CH]C#CC(Cl)(Cl)Cl smiles:Cl[CH]C#CC(Cl)(Cl)Cl H298:62.69 kcal/mol
library:CHOFCl_G4 label:FC#C[CH]Cl smiles:FC#C[CH]Cl H298:50.71 kcal/mol
library:CHOClBr_G4 label:Cl[CH]C#CC(Br)Br smiles:Cl[CH]C#CC(Br)Br H298:85.33 kcal/mol
library:CHOClBr_G4 label:Cl[CH]C#CC(Cl)Br smiles:Cl[CH]C#CC(Cl)Br H298:74.51 kcal/mol
library:CHOClBr_G4 label:Cl[CH]C#CCBr smiles:Cl[CH]C#CCBr H298:75.99 kcal/mol
""",
)

entry(
    index = 48,
    label = "CsCtF1sH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Ct  u0 {1,S}
3   H   u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.441043,-0.132531,-0.790446,-1.40697,-2.44071,-3.22514,-4.43454],'cal/(mol*K)','+|-',[0.239728,0.246139,0.230786,0.21556,0.190236,0.16647,0.121926]),
        H298 = (88.3515,'kcal/mol','+|-',0.382963),
        S298 = (0.858039,'cal/(mol*K)','+|-',0.650829),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:C#C[CH]F smiles:C#C[CH]F H298:42.02 kcal/mol
library:CHOF_G4 label:F[CH]C#CC(F)(F)F smiles:F[CH]C#CC(F)(F)F H298:-113.95 kcal/mol
library:CHOF_G4 label:FC#C[CH]F smiles:FC#C[CH]F H298:14.35 kcal/mol
library:CHOF_G4 label:F[CH]C#CCF smiles:F[CH]C#CCF H298:-8.11 kcal/mol
library:CHOF_G4 label:OC#C[CH]F smiles:OC#C[CH]F H298:9.84 kcal/mol
library:CHOF_G4 label:CC#C[CH]F smiles:CC#C[CH]F H298:31.12 kcal/mol
library:CHOF_G4 label:F[CH]C#CC(F)F smiles:F[CH]C#CC(F)F H298:-57.87 kcal/mol
library:CHOFCl_G4 label:F[CH]C#CC(Cl)Cl smiles:F[CH]C#CC(Cl)Cl H298:28.01 kcal/mol
library:CHOFCl_G4 label:F[CH]C#CCCl smiles:F[CH]C#CCCl H298:29.81 kcal/mol
library:CHOFCl_G4 label:F[CH]C#CC(F)Cl smiles:F[CH]C#CC(F)Cl H298:-12.74 kcal/mol
library:CHOFClBr_G4 label:F[CH]C#CC(Cl)Br smiles:F[CH]C#CC(Cl)Br H298:39.23 kcal/mol
library:CHOFBr_G4 label:F[CH]C#CC(Br)Br smiles:F[CH]C#CC(Br)Br H298:49.98 kcal/mol
library:CHOFBr_G4 label:F[CH]C#CC(Br)(Br)Br smiles:F[CH]C#CC(Br)(Br)Br H298:61.49 kcal/mol
library:CHOFBr_G4 label:F[CH]C#CC(F)Br smiles:F[CH]C#CC(F)Br H298:-0.85 kcal/mol
library:CHOFBr_G4 label:F[CH]C#CCBr smiles:F[CH]C#CCBr H298:40.57 kcal/mol
library:CHOFBr_G4 label:F[CH]C#CC(F)(Br)Br smiles:F[CH]C#CC(F)(Br)Br H298:8.52 kcal/mol
library:CHOFBr_G4 label:F[CH]C#CC(F)(F)Br smiles:F[CH]C#CC(F)(F)Br H298:-49.88 kcal/mol
""",
)

entry(
    index = 49,
    label = "CsBr1sCtO2s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Ct   u0 {1,S}
3   O2s  u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 50,
    label = "CsCl1sCtO2s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Ct   u0 {1,S}
3   O2s  u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 51,
    label = "CsCtF1sO2s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Ct  u0 {1,S}
3   O2s u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 52,
    label = "CsBr1sCtCt",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Ct   u0 {1,S}
3   Ct   u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 53,
    label = "CsCl1sCtCt",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Ct   u0 {1,S}
3   Ct   u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 54,
    label = "CsCtCtF1s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Ct  u0 {1,S}
3   Ct  u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 55,
    label = "CsBr1sBr1sCd",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cd   u0 {1,S}
3   Br1s u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.03647,-1.57316,-2.06415,-2.4767,-3.09717,-3.5218,-4.11549],'cal/(mol*K)','+|-',[0.177526,0.182274,0.170904,0.159629,0.140876,0.123277,0.0902904]),
        H298 = (85.7057,'kcal/mol','+|-',0.283596),
        S298 = (-0.680298,'cal/(mol*K)','+|-',0.48196),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:CCDC[C](Br)Br smiles:CC=C[C](Br)Br H298:41.15 kcal/mol
library:CHOBr_G4 label:CDC(OBr)[C](Br)Br smiles:C=C(OBr)[C](Br)Br H298:50.32 kcal/mol
library:CHOBr_G4 label:CDC(C)[C](Br)Br smiles:C=C(C)[C](Br)Br H298:41.42 kcal/mol
library:CHOBr_G4 label:CCDC(Br)[C](Br)Br smiles:CC=C(Br)[C](Br)Br H298:48.33 kcal/mol
library:CHOBr_G4 label:CDCDC[C](Br)Br smiles:C=C=C[C](Br)Br H298:85.15 kcal/mol
library:CHOBr_G4 label:CDC(Br)[C](Br)Br smiles:C=C(Br)[C](Br)Br H298:57.13 kcal/mol
library:CHOBr_G4 label:CDC(CBr)[C](Br)Br smiles:C=C(CBr)[C](Br)Br H298:47.96 kcal/mol
library:CHOBr_G4 label:BrCDC(Br)[C](Br)Br smiles:BrC=C(Br)[C](Br)Br H298:63.09 kcal/mol
library:CHOBr_G4 label:CC(DCBr)[C](Br)Br smiles:CC(=CBr)[C](Br)Br H298:45.87 kcal/mol
library:CHOBr_G4 label:Br[C](Br)CDC(Br)Br smiles:Br[C](Br)C=C(Br)Br H298:64.91 kcal/mol
library:CHOBr_G4 label:CC(Br)DC[C](Br)Br smiles:CC(Br)=C[C](Br)Br H298:47.50 kcal/mol
library:CHOBr_G4 label:OCDC[C](Br)Br smiles:OC=C[C](Br)Br H298:7.44 kcal/mol
library:CHOBr_G4 label:CDC[C](Br)Br smiles:C=C[C](Br)Br H298:49.38 kcal/mol
library:CHOBr_G4 label:BrCCDC[C](Br)Br smiles:BrCC=C[C](Br)Br H298:46.45 kcal/mol
library:CHOBr_G4 label:BrCDC[C](Br)Br smiles:BrC=C[C](Br)Br H298:54.28 kcal/mol
library:CHOBr_G4 label:CDC(O)[C](Br)Br smiles:C=C(O)[C](Br)Br H298:8.63 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)DC[C](Br)Br smiles:FC(Cl)=C[C](Br)Br H298:1.10 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)[C](Br)Br smiles:FC=C(Br)[C](Br)Br H298:15.02 kcal/mol
library:CHOFBr_G4 label:OC(DCF)[C](Br)Br smiles:OC(=CF)[C](Br)Br H298:-33.07 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(F)[C](Br)Br smiles:FC(F)=C(F)[C](Br)Br H298:-76.34 kcal/mol
library:CHOFBr_G4 label:FC(Br)DC[C](Br)Br smiles:FC(Br)=C[C](Br)Br H298:13.84 kcal/mol
library:CHOFBr_G4 label:FC(Br)DC(Br)[C](Br)Br smiles:FC(Br)=C(Br)[C](Br)Br H298:26.08 kcal/mol
library:CHOFBr_G4 label:CDC(F)[C](Br)Br smiles:C=C(F)[C](Br)Br H298:5.62 kcal/mol
library:CHOFBr_G4 label:CC([C](Br)Br)DC(F)Br smiles:CC([C](Br)Br)=C(F)Br H298:7.67 kcal/mol
library:CHOFBr_G4 label:CC(DCF)[C](Br)Br smiles:CC(=CF)[C](Br)Br H298:-0.11 kcal/mol
library:CHOFBr_G4 label:CC([C](Br)Br)DC(F)F smiles:CC([C](Br)Br)=C(F)F H298:-46.77 kcal/mol
library:CHOClBr_G4 label:CC(DCCl)[C](Br)Br smiles:CC(=CCl)[C](Br)Br H298:34.20 kcal/mol
library:CHOClBr_G4 label:ClCDC(Cl)[C](Br)Br smiles:ClC=C(Cl)[C](Br)Br H298:39.41 kcal/mol
library:CHOClBr_G4 label:ClCDC[C](Br)Br smiles:ClC=C[C](Br)Br H298:42.36 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)[C](Br)Br smiles:C=C(Cl)[C](Br)Br H298:45.13 kcal/mol
library:CHOClBr_G4 label:OC(DCCl)[C](Br)Br smiles:OC(=CCl)[C](Br)Br H298:1.74 kcal/mol
""",
)

entry(
    index = 56,
    label = "CsBr1sCdCl1s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cd   u0 {1,S}
3   Cl1s u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.875682,-1.5291,-2.05385,-2.45199,-3.05453,-3.50097,-4.23207],'cal/(mol*K)','+|-',[0.210733,0.216369,0.202872,0.189487,0.167226,0.146336,0.107179]),
        H298 = (84.6628,'kcal/mol','+|-',0.336643),
        S298 = (0.921809,'cal/(mol*K)','+|-',0.572111),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFClBr_G4 label:FC(F)DC[C](Cl)Br smiles:FC(F)=C[C](Cl)Br H298:-51.91 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)DC[C](Cl)Br smiles:FC(Cl)=C[C](Cl)Br H298:-10.94 kcal/mol
library:CHOFClBr_G4 label:FCDC(F)[C](Cl)Br smiles:FC=C(F)[C](Cl)Br H298:-45.72 kcal/mol
library:CHOFClBr_G4 label:OC(DCF)[C](Cl)Br smiles:OC(=CF)[C](Cl)Br H298:-44.87 kcal/mol
library:CHOFClBr_G4 label:FCDC(Cl)[C](Cl)Br smiles:FC=C(Cl)[C](Cl)Br H298:-8.29 kcal/mol
library:CHOFClBr_G4 label:FCDC[C](Cl)Br smiles:FC=C[C](Cl)Br H298:-6.16 kcal/mol
library:CHOFClBr_G4 label:CDC(F)[C](Cl)Br smiles:C=C(F)[C](Cl)Br H298:-6.32 kcal/mol
library:CHOFClBr_G4 label:CC(DCF)[C](Cl)Br smiles:CC(=CF)[C](Cl)Br H298:-12.27 kcal/mol
library:CHOClBr_G4 label:OC(DCCl)[C](Cl)Br smiles:OC(=CCl)[C](Cl)Br H298:-10.10 kcal/mol
library:CHOClBr_G4 label:CCDC(Br)[C](Cl)Br smiles:CC=C(Br)[C](Cl)Br H298:41.09 kcal/mol
library:CHOClBr_G4 label:CDC(C)[C](Cl)Br smiles:C=C(C)[C](Cl)Br H298:29.34 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)[C](Cl)Br smiles:C=C(Cl)[C](Cl)Br H298:33.16 kcal/mol
library:CHOClBr_G4 label:CDC(OBr)[C](Cl)Br smiles:C=C(OBr)[C](Cl)Br H298:38.56 kcal/mol
library:CHOClBr_G4 label:CCDC[C](Cl)Br smiles:CC=C[C](Cl)Br H298:29.24 kcal/mol
library:CHOClBr_G4 label:OCDC(Br)[C](Cl)Br smiles:OC=C(Br)[C](Cl)Br H298:1.98 kcal/mol
library:CHOClBr_G4 label:CC(DCCl)[C](Cl)Br smiles:CC(=CCl)[C](Cl)Br H298:22.27 kcal/mol
library:CHOClBr_G4 label:CDC(O)[C](Cl)Br smiles:C=C(O)[C](Cl)Br H298:-3.29 kcal/mol
library:CHOClBr_G4 label:CDC[C](Cl)Br smiles:C=C[C](Cl)Br H298:37.37 kcal/mol
library:CHOClBr_G4 label:OC(Br)DC[C](Cl)Br smiles:OC(Br)=C[C](Cl)Br H298:1.76 kcal/mol
library:CHOClBr_G4 label:OCDC[C](Cl)Br smiles:OC=C[C](Cl)Br H298:-4.48 kcal/mol
library:CHOClBr_G4 label:CDCDC[C](Cl)Br smiles:C=C=C[C](Cl)Br H298:73.27 kcal/mol
library:CHOClBr_G4 label:CDC(CBr)[C](Cl)Br smiles:C=C(CBr)[C](Cl)Br H298:35.93 kcal/mol
""",
)

entry(
    index = 57,
    label = "CsCdCl1sCl1s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cd   u0 {1,S}
3   Cl1s u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.909736,-1.39438,-1.84154,-2.23597,-2.87253,-3.33311,-4.01397],'cal/(mol*K)','+|-',[0.128682,0.132123,0.123882,0.115709,0.102115,0.0893584,0.065448]),
        H298 = (84.3344,'kcal/mol','+|-',0.205568),
        S298 = (-0.923097,'cal/(mol*K)','+|-',0.349354),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOCl_G4 label:ClCDC([C](Cl)Cl)C(Cl)Cl smiles:ClC=C([C](Cl)Cl)C(Cl)Cl H298:4.98 kcal/mol
library:CHOCl_G4 label:CDC(OCl)[C](Cl)Cl smiles:C=C(OCl)[C](Cl)Cl H298:23.93 kcal/mol
library:CHOCl_G4 label:CC(Cl)DC(Cl)[C](Cl)Cl smiles:CC(Cl)=C(Cl)[C](Cl)Cl H298:10.86 kcal/mol
library:CHOCl_G4 label:CDCDC[C](Cl)Cl smiles:C=C=C[C](Cl)Cl H298:61.25 kcal/mol
library:CHOCl_G4 label:OCDC[C](Cl)Cl smiles:OC=C[C](Cl)Cl H298:-16.44 kcal/mol
library:CHOCl_G4 label:ClCCDC[C](Cl)Cl smiles:ClCC=C[C](Cl)Cl H298:11.69 kcal/mol
library:CHOCl_G4 label:ClCCDC(Cl)[C](Cl)Cl smiles:ClCC=C(Cl)[C](Cl)Cl H298:8.01 kcal/mol
library:CHOCl_G4 label:CC([C](Cl)Cl)DC(Cl)Cl smiles:CC([C](Cl)Cl)=C(Cl)Cl H298:11.35 kcal/mol
library:CHOCl_G4 label:OCDC(Cl)[C](Cl)Cl smiles:OC=C(Cl)[C](Cl)Cl H298:-21.30 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)CDC(Cl)C(Cl)(Cl)Cl smiles:Cl[C](Cl)C=C(Cl)C(Cl)(Cl)Cl H298:3.06 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)CDC(Cl)C(Cl)Cl smiles:Cl[C](Cl)C=C(Cl)C(Cl)Cl H298:3.27 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)C(Cl)DCC(Cl)(Cl)Cl smiles:Cl[C](Cl)C(Cl)=CC(Cl)(Cl)Cl H298:4.43 kcal/mol
library:CHOCl_G4 label:CCDC(Cl)[C](Cl)Cl smiles:CC=C(Cl)[C](Cl)Cl H298:12.31 kcal/mol
library:CHOCl_G4 label:OC([C](Cl)Cl)DC(Cl)Cl smiles:OC([C](Cl)Cl)=C(Cl)Cl H298:-20.38 kcal/mol
library:CHOCl_G4 label:CDC[C](Cl)Cl smiles:C=C[C](Cl)Cl H298:25.19 kcal/mol
library:CHOCl_G4 label:CDC(O)[C](Cl)Cl smiles:C=C(O)[C](Cl)Cl H298:-15.11 kcal/mol
library:CHOCl_G4 label:OC(Cl)DC(Cl)[C](Cl)Cl smiles:OC(Cl)=C(Cl)[C](Cl)Cl H298:-22.28 kcal/mol
library:CHOCl_G4 label:ClCDC(OCl)[C](Cl)Cl smiles:ClC=C(OCl)[C](Cl)Cl H298:18.48 kcal/mol
library:CHOCl_G4 label:CDC([C](Cl)Cl)C(Cl)(Cl)Cl smiles:C=C([C](Cl)Cl)C(Cl)(Cl)Cl H298:12.12 kcal/mol
library:CHOCl_G4 label:CDCDC(Cl)[C](Cl)Cl smiles:C=C=C(Cl)[C](Cl)Cl H298:59.11 kcal/mol
library:CHOCl_G4 label:ClCDCDC[C](Cl)Cl smiles:ClC=C=C[C](Cl)Cl H298:56.70 kcal/mol
library:CHOCl_G4 label:OC(Cl)DC[C](Cl)Cl smiles:OC(Cl)=C[C](Cl)Cl H298:-22.87 kcal/mol
library:CHOCl_G4 label:CC(DCCl)[C](Cl)Cl smiles:CC(=CCl)[C](Cl)Cl H298:9.61 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)C(Cl)DC(Cl)C(Cl)Cl smiles:Cl[C](Cl)C(Cl)=C(Cl)C(Cl)Cl H298:3.79 kcal/mol
library:CHOCl_G4 label:CDC([C](Cl)Cl)C(Cl)Cl smiles:C=C([C](Cl)Cl)C(Cl)Cl H298:10.03 kcal/mol
library:CHOCl_G4 label:CCDC[C](Cl)Cl smiles:CC=C[C](Cl)Cl H298:17.21 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)CDCC(Cl)(Cl)Cl smiles:Cl[C](Cl)C=CC(Cl)(Cl)Cl H298:4.73 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)DC[C](Cl)Cl smiles:ClCC(Cl)=C[C](Cl)Cl H298:7.18 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)CDCC(Cl)Cl smiles:Cl[C](Cl)C=CC(Cl)Cl H298:7.11 kcal/mol
library:CHOCl_G4 label:CDC(CCl)[C](Cl)Cl smiles:C=C(CCl)[C](Cl)Cl H298:13.18 kcal/mol
library:CHOCl_G4 label:CDC(Cl)[C](Cl)Cl smiles:C=C(Cl)[C](Cl)Cl H298:21.11 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)C(Cl)DC(Cl)Cl smiles:Cl[C](Cl)C(Cl)=C(Cl)Cl H298:17.36 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)C(DC(Cl)Cl)C(Cl)Cl smiles:Cl[C](Cl)C(=C(Cl)Cl)C(Cl)Cl H298:6.96 kcal/mol
library:CHOCl_G4 label:ClCDC[C](Cl)Cl smiles:ClC=C[C](Cl)Cl H298:18.41 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)CDC(Cl)Cl smiles:Cl[C](Cl)C=C(Cl)Cl H298:16.36 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)[C](Cl)Cl smiles:ClC=C(Cl)[C](Cl)Cl H298:15.61 kcal/mol
library:CHOCl_G4 label:ClOC([C](Cl)Cl)DC(Cl)Cl smiles:ClOC([C](Cl)Cl)=C(Cl)Cl H298:18.32 kcal/mol
library:CHOCl_G4 label:ClCDC(CCl)[C](Cl)Cl smiles:ClC=C(CCl)[C](Cl)Cl H298:6.29 kcal/mol
library:CHOCl_G4 label:ClCDCDC(Cl)[C](Cl)Cl smiles:ClC=C=C(Cl)[C](Cl)Cl H298:54.41 kcal/mol
library:CHOCl_G4 label:CDC(C)[C](Cl)Cl smiles:C=C(C)[C](Cl)Cl H298:17.12 kcal/mol
library:CHOCl_G4 label:ClCDC([C](Cl)Cl)C(Cl)(Cl)Cl smiles:ClC=C([C](Cl)Cl)C(Cl)(Cl)Cl H298:11.58 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)C(Cl)DCC(Cl)Cl smiles:Cl[C](Cl)C(Cl)=CC(Cl)Cl H298:3.35 kcal/mol
library:CHOCl_G4 label:OC(DCCl)[C](Cl)Cl smiles:OC(=CCl)[C](Cl)Cl H298:-21.81 kcal/mol
library:CHOCl_G4 label:CC(Cl)DC[C](Cl)Cl smiles:CC(Cl)=C[C](Cl)Cl H298:11.29 kcal/mol
library:CHOFCl_G4 label:CC(DCF)[C](Cl)Cl smiles:CC(=CF)[C](Cl)Cl H298:-24.43 kcal/mol
library:CHOFCl_G4 label:CDC(F)[C](Cl)Cl smiles:C=C(F)[C](Cl)Cl H298:-18.22 kcal/mol
library:CHOFCl_G4 label:FCDC[C](Cl)Cl smiles:FC=C[C](Cl)Cl H298:-18.24 kcal/mol
library:CHOFCl_G4 label:FCDC(Cl)[C](Cl)Cl smiles:FC=C(Cl)[C](Cl)Cl H298:-20.22 kcal/mol
library:CHOFCl_G4 label:OC(DCF)[C](Cl)Cl smiles:OC(=CF)[C](Cl)Cl H298:-56.54 kcal/mol
library:CHOFCl_G4 label:FCDC(F)[C](Cl)Cl smiles:FC=C(F)[C](Cl)Cl H298:-57.45 kcal/mol
library:CHOFCl_G4 label:FC(Cl)DC[C](Cl)Cl smiles:FC(Cl)=C[C](Cl)Cl H298:-22.97 kcal/mol
library:CHOFCl_G4 label:FC(F)DC[C](Cl)Cl smiles:FC(F)=C[C](Cl)Cl H298:-63.96 kcal/mol
library:CHOClBr_G4 label:CDC(CBr)[C](Cl)Cl smiles:C=C(CBr)[C](Cl)Cl H298:23.78 kcal/mol
library:CHOClBr_G4 label:CC(Br)DC[C](Cl)Cl smiles:CC(Br)=C[C](Cl)Cl H298:23.19 kcal/mol
library:CHOClBr_G4 label:OC(Br)DC[C](Cl)Cl smiles:OC(Br)=C[C](Cl)Cl H298:-10.10 kcal/mol
library:CHOClBr_G4 label:OCDC(Br)[C](Cl)Cl smiles:OC=C(Br)[C](Cl)Cl H298:-9.90 kcal/mol
library:CHOClBr_G4 label:Cl[C](Cl)CDCCBr smiles:Cl[C](Cl)C=CCBr H298:22.50 kcal/mol
library:CHOClBr_G4 label:CDC(OBr)[C](Cl)Cl smiles:C=C(OBr)[C](Cl)Cl H298:26.58 kcal/mol
library:CHOClBr_G4 label:CCDC(Br)[C](Cl)Cl smiles:CC=C(Br)[C](Cl)Cl H298:24.41 kcal/mol
""",
)

entry(
    index = 58,
    label = "CsBr1sCdF1s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cd   u0 {1,S}
3   F1s  u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.06597,-1.56595,-2.00286,-2.38727,-2.97525,-3.38486,-3.95318],'cal/(mol*K)','+|-',[0.197685,0.202972,0.190311,0.177755,0.156872,0.137275,0.100543]),
        H298 = (87.5955,'kcal/mol','+|-',0.3158),
        S298 = (1.02806,'cal/(mol*K)','+|-',0.536688),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFBr_G4 label:CCDC[C](F)Br smiles:CC=C[C](F)Br H298:-8.44 kcal/mol
library:CHOFBr_G4 label:CDC[C](F)Br smiles:C=C[C](F)Br H298:-0.17 kcal/mol
library:CHOFBr_G4 label:CDC(F)[C](F)Br smiles:C=C(F)[C](F)Br H298:-42.82 kcal/mol
library:CHOFBr_G4 label:F[C](Br)CDCC(Br)Br smiles:F[C](Br)C=CC(Br)Br H298:4.36 kcal/mol
library:CHOFBr_G4 label:CDC(CBr)[C](F)Br smiles:C=C(CBr)[C](F)Br H298:-1.73 kcal/mol
library:CHOFBr_G4 label:F[C](Br)CDC(F)F smiles:F[C](Br)C=C(F)F H298:-89.19 kcal/mol
library:CHOFBr_G4 label:CDCDC[C](F)Br smiles:C=C=C[C](F)Br H298:36.50 kcal/mol
library:CHOFBr_G4 label:OC(Br)DC[C](F)Br smiles:OC(Br)=C[C](F)Br H298:-35.55 kcal/mol
library:CHOFBr_G4 label:OCDC[C](F)Br smiles:OC=C[C](F)Br H298:-42.07 kcal/mol
library:CHOFBr_G4 label:CC([C](F)Br)DC(F)F smiles:CC([C](F)Br)=C(F)F H298:-96.91 kcal/mol
library:CHOFBr_G4 label:FCDC[C](F)Br smiles:FC=C[C](F)Br H298:-43.31 kcal/mol
library:CHOFBr_G4 label:CDC(OBr)[C](F)Br smiles:C=C(OBr)[C](F)Br H298:1.76 kcal/mol
library:CHOFBr_G4 label:F[C](Br)CDC(Br)CBr smiles:F[C](Br)C=C(Br)CBr H298:2.32 kcal/mol
library:CHOFBr_G4 label:CCDC(Br)[C](F)Br smiles:CC=C(Br)[C](F)Br H298:-0.53 kcal/mol
library:CHOFBr_G4 label:OC(Br)DC(Br)[C](F)Br smiles:OC(Br)=C(Br)[C](F)Br H298:-23.55 kcal/mol
library:CHOFBr_G4 label:CDC(O)[C](F)Br smiles:C=C(O)[C](F)Br H298:-39.46 kcal/mol
library:CHOFBr_G4 label:FCDC(F)[C](F)Br smiles:FC=C(F)[C](F)Br H298:-81.64 kcal/mol
library:CHOFBr_G4 label:OCDC(Br)[C](F)Br smiles:OC=C(Br)[C](F)Br H298:-34.21 kcal/mol
library:CHOFBr_G4 label:CC(Br)DC[C](F)Br smiles:CC(Br)=C[C](F)Br H298:-2.93 kcal/mol
library:CHOFBr_G4 label:FCDC(OBr)[C](F)Br smiles:FC=C(OBr)[C](F)Br H298:-38.78 kcal/mol
library:CHOFBr_G4 label:CDC(C)[C](F)Br smiles:C=C(C)[C](F)Br H298:-8.36 kcal/mol
library:CHOFBr_G4 label:F[C](Br)CDCCBr smiles:F[C](Br)C=CCBr H298:-2.78 kcal/mol
library:CHOFBr_G4 label:F[C](Br)C(F)DC(F)F smiles:F[C](Br)C(F)=C(F)F H298:-124.45 kcal/mol
library:CHOFBr_G4 label:CDC([C](F)Br)C(Br)Br smiles:C=C([C](F)Br)C(Br)Br H298:6.86 kcal/mol
library:CHOFBr_G4 label:CC(Br)DC(Br)[C](F)Br smiles:CC(Br)=C(Br)[C](F)Br H298:7.82 kcal/mol
""",
)

entry(
    index = 59,
    label = "CsCdCl1sF1s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cd   u0 {1,S}
3   F1s  u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.835817,-1.28143,-1.73699,-2.12478,-2.72965,-3.16783,-3.86437],'cal/(mol*K)','+|-',[0.197685,0.202972,0.190311,0.177755,0.156872,0.137275,0.100543]),
        H298 = (87.022,'kcal/mol','+|-',0.3158),
        S298 = (1.14697,'cal/(mol*K)','+|-',0.536688),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFCl_G4 label:CDC(CCl)[C](F)Cl smiles:C=C(CCl)[C](F)Cl H298:-25.08 kcal/mol
library:CHOFCl_G4 label:CDC(C)[C](F)Cl smiles:C=C(C)[C](F)Cl H298:-21.13 kcal/mol
library:CHOFCl_G4 label:CDC(OCl)[C](F)Cl smiles:C=C(OCl)[C](F)Cl H298:-13.66 kcal/mol
library:CHOFCl_G4 label:CCDC(Cl)[C](F)Cl smiles:CC=C(Cl)[C](F)Cl H298:-24.97 kcal/mol
library:CHOFCl_G4 label:OC(Cl)DC[C](F)Cl smiles:OC(Cl)=C[C](F)Cl H298:-60.84 kcal/mol
library:CHOFCl_G4 label:FCDC(F)[C](F)Cl smiles:FC=C(F)[C](F)Cl H298:-94.14 kcal/mol
library:CHOFCl_G4 label:CDC(O)[C](F)Cl smiles:C=C(O)[C](F)Cl H298:-51.97 kcal/mol
library:CHOFCl_G4 label:F[C](Cl)CDCCCl smiles:F[C](Cl)C=CCCl H298:-26.02 kcal/mol
library:CHOFCl_G4 label:FCDC[C](F)Cl smiles:FC=C[C](F)Cl H298:-56.11 kcal/mol
library:CHOFCl_G4 label:F[C](Cl)CDC(F)F smiles:F[C](Cl)C=C(F)F H298:-101.92 kcal/mol
library:CHOFCl_G4 label:OCDC[C](F)Cl smiles:OC=C[C](F)Cl H298:-54.75 kcal/mol
library:CHOFCl_G4 label:CDCDC[C](F)Cl smiles:C=C=C[C](F)Cl H298:23.81 kcal/mol
library:CHOFCl_G4 label:CC(Cl)DC[C](F)Cl smiles:CC(Cl)=C[C](F)Cl H298:-27.92 kcal/mol
library:CHOFCl_G4 label:OCDC(Cl)[C](F)Cl smiles:OC=C(Cl)[C](F)Cl H298:-58.13 kcal/mol
library:CHOFCl_G4 label:OC(DCF)[C](F)Cl smiles:OC(=CF)[C](F)Cl H298:-93.33 kcal/mol
library:CHOFCl_G4 label:CDC(F)[C](F)Cl smiles:C=C(F)[C](F)Cl H298:-55.47 kcal/mol
library:CHOFCl_G4 label:CDC[C](F)Cl smiles:C=C[C](F)Cl H298:-13.04 kcal/mol
library:CHOFCl_G4 label:CCDC[C](F)Cl smiles:CC=C[C](F)Cl H298:-20.83 kcal/mol
library:CHOFClBr_G4 label:CC(Br)DC[C](F)Cl smiles:CC(Br)=C[C](F)Cl H298:-15.68 kcal/mol
library:CHOFClBr_G4 label:OCDC(Br)[C](F)Cl smiles:OC=C(Br)[C](F)Cl H298:-46.65 kcal/mol
library:CHOFClBr_G4 label:F[C](Cl)CDCCBr smiles:F[C](Cl)C=CCBr H298:-15.66 kcal/mol
library:CHOFClBr_G4 label:CCDC(Br)[C](F)Cl smiles:CC=C(Br)[C](F)Cl H298:-12.90 kcal/mol
library:CHOFClBr_G4 label:CDC(OBr)[C](F)Cl smiles:C=C(OBr)[C](F)Cl H298:-10.78 kcal/mol
library:CHOFClBr_G4 label:OC(Br)DC[C](F)Cl smiles:OC(Br)=C[C](F)Cl H298:-48.12 kcal/mol
library:CHOFClBr_G4 label:CDC(CBr)[C](F)Cl smiles:C=C(CBr)[C](F)Cl H298:-14.45 kcal/mol
""",
)

entry(
    index = 60,
    label = "CsCdF1sF1s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S}
3   F1s u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.426557,-0.842816,-1.28458,-1.69885,-2.41286,-2.95515,-3.77227],'cal/(mol*K)','+|-',[0.122599,0.125878,0.118026,0.110239,0.0972881,0.0851343,0.0623542]),
        H298 = (92.9055,'kcal/mol','+|-',0.195851),
        S298 = (-0.110351,'cal/(mol*K)','+|-',0.33284),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:FCC([C](F)F)DC(F)F smiles:FCC([C](F)F)=C(F)F H298:-190.32 kcal/mol
library:CHOF_G4 label:CDC(F)[C](F)F smiles:C=C(F)[C](F)F H298:-94.53 kcal/mol
library:CHOF_G4 label:F[C](F)C(DC(F)F)C(F)F smiles:F[C](F)C(=C(F)F)C(F)F H298:-240.66 kcal/mol
library:CHOF_G4 label:CDC(O)[C](F)F smiles:C=C(O)[C](F)F H298:-90.71 kcal/mol
library:CHOF_G4 label:F[C](F)C(F)DCC(F)F smiles:F[C](F)C(F)=CC(F)F H298:-196.82 kcal/mol
library:CHOF_G4 label:CDC(OF)[C](F)F smiles:C=C(OF)[C](F)F H298:-56.85 kcal/mol
library:CHOF_G4 label:CCDC(F)[C](F)F smiles:CC=C(F)[C](F)F H298:-101.97 kcal/mol
library:CHOF_G4 label:FCC(F)DC(F)[C](F)F smiles:FCC(F)=C(F)[C](F)F H298:-184.64 kcal/mol
library:CHOF_G4 label:F[C](F)C(F)DC(F)C(F)F smiles:F[C](F)C(F)=C(F)C(F)F H298:-234.19 kcal/mol
library:CHOF_G4 label:CDC(C)[C](F)F smiles:C=C(C)[C](F)F H298:-61.58 kcal/mol
library:CHOF_G4 label:F[C](F)C(F)DC(F)F smiles:F[C](F)C(F)=C(F)F H298:-175.27 kcal/mol
library:CHOF_G4 label:FCDC(F)[C](F)F smiles:FC=C(F)[C](F)F H298:-132.54 kcal/mol
library:CHOF_G4 label:OCDC[C](F)F smiles:OC=C[C](F)F H298:-94.52 kcal/mol
library:CHOF_G4 label:F[C](F)CDCC(F)(F)F smiles:F[C](F)C=CC(F)(F)F H298:-216.73 kcal/mol
library:CHOF_G4 label:CDCDC(F)[C](F)F smiles:C=C=C(F)[C](F)F H298:-52.78 kcal/mol
library:CHOF_G4 label:F[C](F)C(F)DC(F)C(F)(F)F smiles:F[C](F)C(F)=C(F)C(F)(F)F H298:-289.13 kcal/mol
library:CHOF_G4 label:OC(DCF)[C](F)F smiles:OC(=CF)[C](F)F H298:-131.67 kcal/mol
library:CHOF_G4 label:CDC(CF)[C](F)F smiles:C=C(CF)[C](F)F H298:-103.16 kcal/mol
library:CHOF_G4 label:F[C](F)CDC(F)F smiles:F[C](F)C=C(F)F H298:-141.81 kcal/mol
library:CHOF_G4 label:F[C](F)CDCC(F)F smiles:F[C](F)C=CC(F)F H298:-158.13 kcal/mol
library:CHOF_G4 label:F[C](F)C(DC(F)F)C(F)(F)F smiles:F[C](F)C(=C(F)F)C(F)(F)F H298:-295.56 kcal/mol
library:CHOF_G4 label:FOC([C](F)F)DC(F)F smiles:FOC([C](F)F)=C(F)F H298:-139.96 kcal/mol
library:CHOF_G4 label:FCDC([C](F)F)C(F)F smiles:FC=C([C](F)F)C(F)F H298:-196.75 kcal/mol
library:CHOF_G4 label:FCCDC(F)[C](F)F smiles:FCC=C(F)[C](F)F H298:-144.87 kcal/mol
library:CHOF_G4 label:CC(DCF)[C](F)F smiles:CC(=CF)[C](F)F H298:-104.48 kcal/mol
library:CHOF_G4 label:FCCDC[C](F)F smiles:FCC=C[C](F)F H298:-104.71 kcal/mol
library:CHOF_G4 label:CC([C](F)F)DC(F)F smiles:CC([C](F)F)=C(F)F H298:-149.68 kcal/mol
library:CHOF_G4 label:FCDC(OF)[C](F)F smiles:FC=C(OF)[C](F)F H298:-97.07 kcal/mol
library:CHOF_G4 label:FCC(F)DC[C](F)F smiles:FCC(F)=C[C](F)F H298:-148.69 kcal/mol
library:CHOF_G4 label:CC(F)DC(F)[C](F)F smiles:CC(F)=C(F)[C](F)F H298:-143.80 kcal/mol
library:CHOF_G4 label:FCDC([C](F)F)C(F)(F)F smiles:FC=C([C](F)F)C(F)(F)F H298:-253.53 kcal/mol
library:CHOF_G4 label:F[C](F)CDC(F)C(F)F smiles:F[C](F)C=C(F)C(F)F H298:-199.77 kcal/mol
library:CHOF_G4 label:ODCDC(F)[C](F)F smiles:O=C=C(F)[C](F)F H298:-106.47 kcal/mol
library:CHOF_G4 label:F[C](F)C(F)DCC(F)(F)F smiles:F[C](F)C(F)=CC(F)(F)F H298:-253.82 kcal/mol
library:CHOF_G4 label:OCDC(F)[C](F)F smiles:OC=C(F)[C](F)F H298:-132.39 kcal/mol
library:CHOF_G4 label:OC(F)DC(F)[C](F)F smiles:OC(F)=C(F)[C](F)F H298:-175.32 kcal/mol
library:CHOF_G4 label:OC(F)DC[C](F)F smiles:OC(F)=C[C](F)F H298:-141.59 kcal/mol
library:CHOF_G4 label:CCDC[C](F)F smiles:CC=C[C](F)F H298:-61.31 kcal/mol
library:CHOF_G4 label:OC([C](F)F)DC(F)F smiles:OC([C](F)F)=C(F)F H298:-173.98 kcal/mol
library:CHOF_G4 label:F[C](F)CDC(F)C(F)(F)F smiles:F[C](F)C=C(F)C(F)(F)F H298:-256.67 kcal/mol
library:CHOFCl_G4 label:OCDC(Cl)[C](F)F smiles:OC=C(Cl)[C](F)F H298:-96.67 kcal/mol
library:CHOFCl_G4 label:F[C](F)CDCCCl smiles:F[C](F)C=CCCl H298:-66.71 kcal/mol
library:CHOFCl_G4 label:CDC(CCl)[C](F)F smiles:C=C(CCl)[C](F)F H298:-65.42 kcal/mol
library:CHOFCl_G4 label:ODCDC(Cl)[C](F)F smiles:O=C=C(Cl)[C](F)F H298:-64.18 kcal/mol
library:CHOFCl_G4 label:CCDC(Cl)[C](F)F smiles:CC=C(Cl)[C](F)F H298:-64.38 kcal/mol
library:CHOFCl_G4 label:OC(Cl)DC[C](F)F smiles:OC(Cl)=C[C](F)F H298:-100.25 kcal/mol
library:CHOFCl_G4 label:CDC(OCl)[C](F)F smiles:C=C(OCl)[C](F)F H298:-52.83 kcal/mol
library:CHOFBr_G4 label:ODCDC(Br)[C](F)F smiles:O=C=C(Br)[C](F)F H298:-54.19 kcal/mol
library:CHOFBr_G4 label:CC(Br)DC(Br)[C](F)F smiles:CC(Br)=C(Br)[C](F)F H298:-45.42 kcal/mol
library:CHOFBr_G4 label:CCDC(Br)[C](F)F smiles:CC=C(Br)[C](F)F H298:-53.14 kcal/mol
library:CHOFBr_G4 label:F[C](F)C(Br)DCCBr smiles:F[C](F)C(Br)=CCBr H298:-47.69 kcal/mol
library:CHOFBr_G4 label:OC(Br)DC(F)[C](F)F smiles:OC(Br)=C(F)[C](F)F H298:-123.35 kcal/mol
library:CHOFBr_G4 label:OC(Br)DC[C](F)F smiles:OC(Br)=C[C](F)F H298:-87.69 kcal/mol
library:CHOFBr_G4 label:OC(Br)DC(Br)[C](F)F smiles:OC(Br)=C(Br)[C](F)F H298:-75.84 kcal/mol
library:CHOFBr_G4 label:CDC(OBr)[C](F)F smiles:C=C(OBr)[C](F)F H298:-49.71 kcal/mol
library:CHOFBr_G4 label:FCDC(OBr)[C](F)F smiles:FC=C(OBr)[C](F)F H298:-88.76 kcal/mol
library:CHOFBr_G4 label:F[C](F)CDCCBr smiles:F[C](F)C=CCBr H298:-56.32 kcal/mol
library:CHOFBr_G4 label:CC(Br)DC(F)[C](F)F smiles:CC(Br)=C(F)[C](F)F H298:-94.46 kcal/mol
library:CHOFBr_G4 label:CC(Br)DC[C](F)F smiles:CC(Br)=C[C](F)F H298:-57.68 kcal/mol
library:CHOFBr_G4 label:F[C](F)CDC(Br)CBr smiles:F[C](F)C=C(Br)CBr H298:-51.34 kcal/mol
library:CHOFBr_G4 label:CDC(CBr)[C](F)F smiles:C=C(CBr)[C](F)F H298:-54.66 kcal/mol
library:CHOFBr_G4 label:OCDC(Br)[C](F)F smiles:OC=C(Br)[C](F)F H298:-85.46 kcal/mol
library:CHOFBr_G4 label:F[C](F)C(F)DCCBr smiles:F[C](F)C(F)=CCBr H298:-96.10 kcal/mol
library:CHOFBr_G4 label:F[C](F)CDCC(F)Br smiles:F[C](F)C=CC(F)Br H298:-99.54 kcal/mol
library:CHOFBr_G4 label:F[C](F)CDCC(Br)Br smiles:F[C](F)C=CC(Br)Br H298:-49.42 kcal/mol
""",
)

entry(
    index = 61,
    label = "CsBr1sCdH",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cd   u0 {1,S}
3   H    u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.229934,-0.64201,-1.12114,-1.53874,-2.20809,-2.74947,-3.70053],'cal/(mol*K)','+|-',[0.164737,0.169143,0.158592,0.148129,0.130727,0.114396,0.0837859]),
        H298 = (85.8747,'kcal/mol','+|-',0.263166),
        S298 = (-1.0617,'cal/(mol*K)','+|-',0.44724),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:OCDC(Br)[CH]Br smiles:OC=C(Br)[CH]Br H298:5.54 kcal/mol
library:CHOBr_G4 label:Br[CH]C(DCBr)OBr smiles:Br[CH]C(=CBr)OBr H298:49.04 kcal/mol
library:CHOBr_G4 label:CDC(C)[CH]Br smiles:C=C(C)[CH]Br H298:33.88 kcal/mol
library:CHOBr_G4 label:CC([CH]Br)DCBr smiles:CC([CH]Br)=CBr H298:39.32 kcal/mol
library:CHOBr_G4 label:Br[CH]CDC(Br)CBr smiles:Br[CH]C=C(Br)CBr H298:43.49 kcal/mol
library:CHOBr_G4 label:CC(Br)DC[CH]Br smiles:CC(Br)=C[CH]Br H298:38.96 kcal/mol
library:CHOBr_G4 label:CDC([CH]Br)CBr smiles:C=C([CH]Br)CBr H298:41.65 kcal/mol
library:CHOBr_G4 label:Br[CH]CDCC(Br)Br smiles:Br[CH]C=CC(Br)Br H298:47.49 kcal/mol
library:CHOBr_G4 label:CDC([CH]Br)OBr smiles:C=C([CH]Br)OBr H298:43.33 kcal/mol
library:CHOBr_G4 label:OC(Br)DC[CH]Br smiles:OC(Br)=C[CH]Br H298:6.09 kcal/mol
library:CHOBr_G4 label:CDC(O)[CH]Br smiles:C=C(O)[CH]Br H298:0.44 kcal/mol
library:CHOBr_G4 label:Br[CH]CDCCBr smiles:Br[CH]C=CCBr H298:40.46 kcal/mol
library:CHOBr_G4 label:CCDC[CH]Br smiles:CC=C[CH]Br H298:35.33 kcal/mol
library:CHOBr_G4 label:CDC[CH]Br smiles:C=C[CH]Br H298:43.59 kcal/mol
library:CHOBr_G4 label:Br[CH]C(Br)DCCBr smiles:Br[CH]C(Br)=CCBr H298:45.81 kcal/mol
library:CHOBr_G4 label:Br[CH]CDCDCBr smiles:Br[CH]C=C=CBr H298:84.98 kcal/mol
library:CHOBr_G4 label:CDC(Br)[CH]Br smiles:C=C(Br)[CH]Br H298:48.84 kcal/mol
library:CHOBr_G4 label:OC([CH]Br)DCBr smiles:OC([CH]Br)=CBr H298:6.14 kcal/mol
library:CHOBr_G4 label:Br[CH]C(DCBr)CBr smiles:Br[CH]C(=CBr)CBr H298:45.96 kcal/mol
library:CHOBr_G4 label:Br[CH]C(Br)DCBr smiles:Br[CH]C(Br)=CBr H298:54.68 kcal/mol
library:CHOBr_G4 label:Br[CH]CDCBr smiles:Br[CH]C=CBr H298:48.05 kcal/mol
library:CHOBr_G4 label:CCDC(Br)[CH]Br smiles:CC=C(Br)[CH]Br H298:40.22 kcal/mol
library:CHOBr_G4 label:OCDC[CH]Br smiles:OC=C[CH]Br H298:0.42 kcal/mol
library:CHOFClBr_G4 label:FCDC(Cl)[CH]Br smiles:FC=C(Cl)[CH]Br H298:-4.68 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)DC(Cl)[CH]Br smiles:FC(Cl)=C(Cl)[CH]Br H298:-10.19 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)DC[CH]Br smiles:FC(Cl)=C[CH]Br H298:-7.61 kcal/mol
library:CHOFClBr_G4 label:FC(F)DC(Cl)[CH]Br smiles:FC(F)=C(Cl)[CH]Br H298:-49.55 kcal/mol
library:CHOFBr_G4 label:CDC(F)[CH]Br smiles:C=C(F)[CH]Br H298:-2.10 kcal/mol
library:CHOFBr_G4 label:FC(Br)DC[CH]Br smiles:FC(Br)=C[CH]Br H298:5.17 kcal/mol
library:CHOFBr_G4 label:CC([CH]Br)DC(F)F smiles:CC([CH]Br)=C(F)F H298:-56.60 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(Br)[CH]Br smiles:FC(F)=C(Br)[CH]Br H298:-38.11 kcal/mol
library:CHOFBr_G4 label:FCDC[CH]Br smiles:FC=C[CH]Br H298:-1.19 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)[CH]Br smiles:FC=C(Br)[CH]Br H298:6.65 kcal/mol
library:CHOFBr_G4 label:FC(F)DC[CH]Br smiles:FC(F)=C[CH]Br H298:-48.19 kcal/mol
library:CHOFBr_G4 label:FC(F)DC([CH]Br)CBr smiles:FC(F)=C([CH]Br)CBr H298:-49.48 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)[CH]Br smiles:C=C(Cl)[CH]Br H298:37.11 kcal/mol
""",
)

entry(
    index = 62,
    label = "CsCdCl1sH",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cd   u0 {1,S}
3   H    u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.297037,-0.586456,-0.97946,-1.36131,-2.02864,-2.58063,-3.55367],'cal/(mol*K)','+|-',[0.116487,0.119602,0.112142,0.104743,0.0924379,0.0808901,0.0592456]),
        H298 = (84.2982,'kcal/mol','+|-',0.186087),
        S298 = (-1.17227,'cal/(mol*K)','+|-',0.316246),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOCl_G4 label:Cl[CH]CDCC(Cl)Cl smiles:Cl[CH]C=CC(Cl)Cl H298:12.99 kcal/mol
library:CHOCl_G4 label:OCDC[CH]Cl smiles:OC=C[CH]Cl H298:-11.61 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(CCl)DC(Cl)Cl smiles:Cl[CH]C(CCl)=C(Cl)Cl H298:6.21 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)DC(Cl)CCl smiles:Cl[CH]C(Cl)=C(Cl)CCl H298:5.31 kcal/mol
library:CHOCl_G4 label:CDC([CH]Cl)OCl smiles:C=C([CH]Cl)OCl H298:28.42 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)DCCl smiles:Cl[CH]C(Cl)=CCl H298:19.50 kcal/mol
library:CHOCl_G4 label:CDCDC[CH]Cl smiles:C=C=C[CH]Cl H298:67.15 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)DCCCl smiles:Cl[CH]C(Cl)=CCCl H298:12.30 kcal/mol
library:CHOCl_G4 label:Cl[CH]CDCC(Cl)(Cl)Cl smiles:Cl[CH]C=CC(Cl)(Cl)Cl H298:10.63 kcal/mol
library:CHOCl_G4 label:OCDC(Cl)[CH]Cl smiles:OC=C(Cl)[CH]Cl H298:-17.45 kcal/mol
library:CHOCl_G4 label:CC(Cl)DC[CH]Cl smiles:CC(Cl)=C[CH]Cl H298:14.84 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)DC(Cl)C(Cl)(Cl)Cl smiles:Cl[CH]C(Cl)=C(Cl)C(Cl)(Cl)Cl H298:7.38 kcal/mol
library:CHOCl_G4 label:CDC[CH]Cl smiles:C=C[CH]Cl H298:31.43 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(DCCl)OCl smiles:Cl[CH]C(=CCl)OCl H298:23.05 kcal/mol
library:CHOCl_G4 label:CCDC[CH]Cl smiles:CC=C[CH]Cl H298:23.32 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)DCC(Cl)Cl smiles:Cl[CH]C(Cl)=CC(Cl)Cl H298:7.38 kcal/mol
library:CHOCl_G4 label:OC([CH]Cl)DCCl smiles:OC([CH]Cl)=CCl H298:-17.21 kcal/mol
library:CHOCl_G4 label:Cl[CH]CDC(Cl)CCl smiles:Cl[CH]C=C(Cl)CCl H298:9.32 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)DC(Cl)C(Cl)Cl smiles:Cl[CH]C(Cl)=C(Cl)C(Cl)Cl H298:2.02 kcal/mol
library:CHOCl_G4 label:CC(Cl)DC(Cl)[CH]Cl smiles:CC(Cl)=C(Cl)[CH]Cl H298:9.32 kcal/mol
library:CHOCl_G4 label:CDC(O)[CH]Cl smiles:C=C(O)[CH]Cl H298:-11.36 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)DCDCCl smiles:Cl[CH]C(Cl)=C=CCl H298:58.75 kcal/mol
library:CHOCl_G4 label:CDC(Cl)[CH]Cl smiles:C=C(Cl)[CH]Cl H298:25.09 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)DCC(Cl)(Cl)Cl smiles:Cl[CH]C(Cl)=CC(Cl)(Cl)Cl H298:8.49 kcal/mol
library:CHOCl_G4 label:CC([CH]Cl)DCCl smiles:CC([CH]Cl)=CCl H298:15.34 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(DCCl)C(Cl)(Cl)Cl smiles:Cl[CH]C(=CCl)C(Cl)(Cl)Cl H298:9.98 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(DCCl)CCl smiles:Cl[CH]C(=CCl)CCl H298:11.54 kcal/mol
library:CHOCl_G4 label:OC(Cl)DC[CH]Cl smiles:OC(Cl)=C[CH]Cl H298:-18.72 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(DCCl)C(Cl)Cl smiles:Cl[CH]C(=CCl)C(Cl)Cl H298:7.76 kcal/mol
library:CHOCl_G4 label:OC(Cl)DC(Cl)[CH]Cl smiles:OC(Cl)=C(Cl)[CH]Cl H298:-22.53 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)DCDC(Cl)Cl smiles:Cl[CH]C(Cl)=C=C(Cl)Cl H298:54.93 kcal/mol
library:CHOCl_G4 label:CCDC(Cl)[CH]Cl smiles:CC=C(Cl)[CH]Cl H298:16.73 kcal/mol
library:CHOCl_G4 label:Cl[CH]CDCCCl smiles:Cl[CH]C=CCCl H298:17.71 kcal/mol
library:CHOCl_G4 label:CDC(C)[CH]Cl smiles:C=C(C)[CH]Cl H298:23.16 kcal/mol
library:CHOCl_G4 label:Cl[CH]CDCCl smiles:Cl[CH]C=CCl H298:23.93 kcal/mol
library:CHOCl_G4 label:Cl[CH]CDC(Cl)C(Cl)Cl smiles:Cl[CH]C=C(Cl)C(Cl)Cl H298:5.54 kcal/mol
library:CHOCl_G4 label:CDC([CH]Cl)C(Cl)Cl smiles:C=C([CH]Cl)C(Cl)Cl H298:14.37 kcal/mol
library:CHOCl_G4 label:CDC([CH]Cl)C(Cl)(Cl)Cl smiles:C=C([CH]Cl)C(Cl)(Cl)Cl H298:13.73 kcal/mol
library:CHOCl_G4 label:CDC([CH]Cl)CCl smiles:C=C([CH]Cl)CCl H298:18.80 kcal/mol
library:CHOCl_G4 label:Cl[CH]CDC(Cl)C(Cl)(Cl)Cl smiles:Cl[CH]C=C(Cl)C(Cl)(Cl)Cl H298:4.85 kcal/mol
library:CHOFCl_G4 label:FC(F)DC(Cl)[CH]Cl smiles:FC(F)=C(Cl)[CH]Cl H298:-61.32 kcal/mol
library:CHOFCl_G4 label:FCDC([CH]Cl)CCl smiles:FC=C([CH]Cl)CCl H298:-25.36 kcal/mol
library:CHOFCl_G4 label:FC(Cl)DC(Cl)[CH]Cl smiles:FC(Cl)=C(Cl)[CH]Cl H298:-21.97 kcal/mol
library:CHOFCl_G4 label:FC(F)DC[CH]Cl smiles:FC(F)=C[CH]Cl H298:-60.20 kcal/mol
library:CHOFCl_G4 label:CC([CH]Cl)DC(F)F smiles:CC([CH]Cl)=C(F)F H298:-68.49 kcal/mol
library:CHOFCl_G4 label:FCDC[CH]Cl smiles:FC=C[CH]Cl H298:-13.29 kcal/mol
library:CHOFCl_G4 label:CC([CH]Cl)DC(F)Cl smiles:CC([CH]Cl)=C(F)Cl H298:-27.98 kcal/mol
library:CHOFCl_G4 label:FCDC(Cl)[CH]Cl smiles:FC=C(Cl)[CH]Cl H298:-16.55 kcal/mol
library:CHOFCl_G4 label:CDC(F)[CH]Cl smiles:C=C(F)[CH]Cl H298:-14.11 kcal/mol
library:CHOFCl_G4 label:CC([CH]Cl)DCF smiles:CC([CH]Cl)=CF H298:-21.83 kcal/mol
library:CHOFClBr_G4 label:FCDC([CH]Cl)CBr smiles:FC=C([CH]Cl)CBr H298:-14.66 kcal/mol
library:CHOClBr_G4 label:CCDC(Br)[CH]Cl smiles:CC=C(Br)[CH]Cl H298:28.40 kcal/mol
library:CHOClBr_G4 label:CDC([CH]Cl)CBr smiles:C=C([CH]Cl)CBr H298:29.54 kcal/mol
library:CHOClBr_G4 label:CDC([CH]Cl)C(Cl)Br smiles:C=C([CH]Cl)C(Cl)Br H298:25.81 kcal/mol
library:CHOClBr_G4 label:CC(Br)DC(Cl)[CH]Cl smiles:CC(Br)=C(Cl)[CH]Cl H298:21.33 kcal/mol
library:CHOClBr_G4 label:Cl[CH]CDCCBr smiles:Cl[CH]C=CCBr H298:28.41 kcal/mol
library:CHOClBr_G4 label:Cl[CH]C(DCCl)CBr smiles:Cl[CH]C(=CCl)CBr H298:22.08 kcal/mol
library:CHOClBr_G4 label:Cl[CH]C(Br)DCCBr smiles:Cl[CH]C(Br)=CCBr H298:33.99 kcal/mol
library:CHOClBr_G4 label:OC(Br)DC[CH]Cl smiles:OC(Br)=C[CH]Cl H298:-5.91 kcal/mol
library:CHOClBr_G4 label:OC(Br)DC(Br)[CH]Cl smiles:OC(Br)=C(Br)[CH]Cl H298:1.28 kcal/mol
library:CHOClBr_G4 label:CDC([CH]Cl)C(Br)Br smiles:C=C([CH]Cl)C(Br)Br H298:37.09 kcal/mol
library:CHOClBr_G4 label:CC(Br)DC(Br)[CH]Cl smiles:CC(Br)=C(Br)[CH]Cl H298:33.20 kcal/mol
library:CHOClBr_G4 label:CC(Br)DC[CH]Cl smiles:CC(Br)=C[CH]Cl H298:27.06 kcal/mol
library:CHOClBr_G4 label:Cl[CH]CDCC(Br)Br smiles:Cl[CH]C=CC(Br)Br H298:35.42 kcal/mol
library:CHOClBr_G4 label:Cl[CH]CDC(Cl)CBr smiles:Cl[CH]C=C(Cl)CBr H298:19.61 kcal/mol
library:CHOClBr_G4 label:Cl[CH]C(DCCl)OBr smiles:Cl[CH]C(=CCl)OBr H298:25.55 kcal/mol
library:CHOClBr_G4 label:OC(Br)DC(Cl)[CH]Cl smiles:OC(Br)=C(Cl)[CH]Cl H298:-10.13 kcal/mol
library:CHOClBr_G4 label:Cl[CH]C(Cl)DCCBr smiles:Cl[CH]C(Cl)=CCBr H298:22.43 kcal/mol
library:CHOClBr_G4 label:Cl[CH]CDC(Br)CBr smiles:Cl[CH]C=C(Br)CBr H298:31.51 kcal/mol
library:CHOClBr_G4 label:CDC([CH]Cl)OBr smiles:C=C([CH]Cl)OBr H298:31.44 kcal/mol
library:CHOClBr_G4 label:OCDC(Br)[CH]Cl smiles:OC=C(Br)[CH]Cl H298:-6.12 kcal/mol
library:CHOClBr_G4 label:Cl[CH]CDCC(Cl)Br smiles:Cl[CH]C=CC(Cl)Br H298:25.98 kcal/mol
""",
)

entry(
    index = 63,
    label = "CsCdF1sH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S}
3   H   u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.417423,-0.566041,-0.91178,-1.2927,-1.99663,-2.57088,-3.52809],'cal/(mol*K)','+|-',[0.0983519,0.100982,0.0946832,0.0884364,0.0780469,0.0682969,0.0500221]),
        H298 = (85.6558,'kcal/mol','+|-',0.157116),
        S298 = (-0.912551,'cal/(mol*K)','+|-',0.267012),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:F[CH]CDC(F)C(F)(F)F smiles:F[CH]C=C(F)C(F)(F)F H298:-210.53 kcal/mol
library:CHOF_G4 label:F[CH]C(F)DC(F)CF smiles:F[CH]C(F)=C(F)CF H298:-141.64 kcal/mol
library:CHOF_G4 label:CDC[CH]F smiles:C=C[CH]F H298:-5.90 kcal/mol
library:CHOF_G4 label:F[CH]CDC(F)CF smiles:F[CH]C=C(F)CF H298:-102.56 kcal/mol
library:CHOF_G4 label:CDCDC(F)[CH]F smiles:C=C=C(F)[CH]F H298:-8.82 kcal/mol
library:CHOF_G4 label:F[CH]C(F)DCC(F)(F)F smiles:F[CH]C(F)=CC(F)(F)F H298:-208.79 kcal/mol
library:CHOF_G4 label:OCDC(F)[CH]F smiles:OC=C(F)[CH]F H298:-89.31 kcal/mol
library:CHOF_G4 label:OC(F)DC(F)[CH]F smiles:OC(F)=C(F)[CH]F H298:-132.71 kcal/mol
library:CHOF_G4 label:F[CH]C(F)DCF smiles:F[CH]C(F)=CF H298:-89.21 kcal/mol
library:CHOF_G4 label:CC([CH]F)DC(F)F smiles:CC([CH]F)=C(F)F H298:-104.48 kcal/mol
library:CHOF_G4 label:F[CH]CDCF smiles:F[CH]C=CF H298:-50.14 kcal/mol
library:CHOF_G4 label:F[CH]CDC(F)C(F)F smiles:F[CH]C=C(F)C(F)F H298:-153.47 kcal/mol
library:CHOF_G4 label:F[CH]C(DCF)C(F)(F)F smiles:F[CH]C(=CF)C(F)(F)F H298:-208.68 kcal/mol
library:CHOF_G4 label:CCDC(F)[CH]F smiles:CC=C(F)[CH]F H298:-57.64 kcal/mol
library:CHOF_G4 label:CDC([CH]F)CF smiles:C=C([CH]F)CF H298:-55.24 kcal/mol
library:CHOF_G4 label:CDC(F)[CH]F smiles:C=C(F)[CH]F H298:-49.95 kcal/mol
library:CHOF_G4 label:F[CH]C(F)DC(F)F smiles:F[CH]C(F)=C(F)F H298:-132.20 kcal/mol
library:CHOF_G4 label:CDC([CH]F)OF smiles:C=C([CH]F)OF H298:-12.00 kcal/mol
library:CHOF_G4 label:CC([CH]F)DCF smiles:CC([CH]F)=CF H298:-58.21 kcal/mol
library:CHOF_G4 label:CCDC[CH]F smiles:CC=C[CH]F H298:-13.85 kcal/mol
library:CHOF_G4 label:F[CH]C(DCF)CF smiles:F[CH]C(=CF)CF H298:-99.24 kcal/mol
library:CHOF_G4 label:CDC(C)[CH]F smiles:C=C(C)[CH]F H298:-13.64 kcal/mol
library:CHOF_G4 label:OC(F)DC[CH]F smiles:OC(F)=C[CH]F H298:-96.62 kcal/mol
library:CHOF_G4 label:F[CH]C(DCF)OF smiles:F[CH]C(=CF)OF H298:-52.35 kcal/mol
library:CHOF_G4 label:F[CH]C(F)DC(F)C(F)(F)F smiles:F[CH]C(F)=C(F)C(F)(F)F H298:-246.25 kcal/mol
library:CHOF_G4 label:F[CH]CDC(F)F smiles:F[CH]C=C(F)F H298:-96.46 kcal/mol
library:CHOF_G4 label:OC([CH]F)DC(F)F smiles:OC([CH]F)=C(F)F H298:-131.66 kcal/mol
library:CHOF_G4 label:F[CH]C(DCF)C(F)F smiles:F[CH]C(=CF)C(F)F H298:-151.63 kcal/mol
library:CHOF_G4 label:OCDC[CH]F smiles:OC=C[CH]F H298:-48.97 kcal/mol
library:CHOF_G4 label:F[CH]CDCC(F)(F)F smiles:F[CH]C=CC(F)(F)F H298:-169.40 kcal/mol
library:CHOF_G4 label:F[CH]C(DC(F)F)C(F)(F)F smiles:F[CH]C(=C(F)F)C(F)(F)F H298:-253.53 kcal/mol
library:CHOF_G4 label:CDC(O)[CH]F smiles:C=C(O)[CH]F H298:-46.50 kcal/mol
library:CHOF_G4 label:CC(F)DC[CH]F smiles:CC(F)=C[CH]F H298:-60.87 kcal/mol
library:CHOF_G4 label:F[CH]CDCCF smiles:F[CH]C=CCF H298:-56.76 kcal/mol
library:CHOF_G4 label:F[CH]C(F)DC(F)C(F)F smiles:F[CH]C(F)=C(F)C(F)F H298:-191.32 kcal/mol
library:CHOF_G4 label:F[CH]C(CF)DC(F)F smiles:F[CH]C(CF)=C(F)F H298:-145.30 kcal/mol
library:CHOF_G4 label:OC([CH]F)DCF smiles:OC([CH]F)=CF H298:-87.66 kcal/mol
library:CHOF_G4 label:CC(F)DC(F)[CH]F smiles:CC(F)=C(F)[CH]F H298:-101.30 kcal/mol
library:CHOF_G4 label:CDC([CH]F)C(F)F smiles:C=C([CH]F)C(F)F H298:-108.69 kcal/mol
library:CHOF_G4 label:F[CH]C(F)DCC(F)F smiles:F[CH]C(F)=CC(F)F H298:-152.55 kcal/mol
library:CHOF_G4 label:F[CH]C(DC(F)F)C(F)F smiles:F[CH]C(=C(F)F)C(F)F H298:-196.74 kcal/mol
library:CHOF_G4 label:F[CH]CDCC(F)F smiles:F[CH]C=CC(F)F H298:-110.44 kcal/mol
library:CHOF_G4 label:F[CH]C(F)DCCF smiles:F[CH]C(F)=CCF H298:-99.63 kcal/mol
library:CHOFCl_G4 label:CC(Cl)DC[CH]F smiles:CC(Cl)=C[CH]F H298:-23.28 kcal/mol
library:CHOFCl_G4 label:F[CH]C(DCF)OCl smiles:F[CH]C(=CF)OCl H298:-47.95 kcal/mol
library:CHOFCl_G4 label:F[CH]C(Cl)DCCCl smiles:F[CH]C(Cl)=CCCl H298:-23.93 kcal/mol
library:CHOFCl_G4 label:F[CH]CDCC(Cl)Cl smiles:F[CH]C=CC(Cl)Cl H298:-24.10 kcal/mol
library:CHOFCl_G4 label:CC(Cl)DC(F)[CH]F smiles:CC(Cl)=C(F)[CH]F H298:-64.29 kcal/mol
library:CHOFCl_G4 label:OC(Cl)DC(Cl)[CH]F smiles:OC(Cl)=C(Cl)[CH]F H298:-57.57 kcal/mol
library:CHOFCl_G4 label:CCDC(Cl)[CH]F smiles:CC=C(Cl)[CH]F H298:-19.43 kcal/mol
library:CHOFCl_G4 label:F[CH]CDC(Cl)CCl smiles:F[CH]C=C(Cl)CCl H298:-27.37 kcal/mol
library:CHOFCl_G4 label:OCDC(Cl)[CH]F smiles:OC=C(Cl)[CH]F H298:-52.92 kcal/mol
library:CHOFCl_G4 label:CDC([CH]F)C(F)Cl smiles:C=C([CH]F)C(F)Cl H298:-63.57 kcal/mol
library:CHOFCl_G4 label:OC(Cl)DC[CH]F smiles:OC(Cl)=C[CH]F H298:-55.64 kcal/mol
library:CHOFCl_G4 label:CDC([CH]F)OCl smiles:C=C([CH]F)OCl H298:-7.74 kcal/mol
library:CHOFCl_G4 label:F[CH]CDCCCl smiles:F[CH]C=CCCl H298:-19.07 kcal/mol
library:CHOFCl_G4 label:OC(Cl)DC(F)[CH]F smiles:OC(Cl)=C(F)[CH]F H298:-93.49 kcal/mol
library:CHOFCl_G4 label:F[CH]C(F)DCCCl smiles:F[CH]C(F)=CCCl H298:-61.91 kcal/mol
library:CHOFCl_G4 label:F[CH]CDCC(F)Cl smiles:F[CH]C=CC(F)Cl H298:-65.09 kcal/mol
library:CHOFCl_G4 label:F[CH]C(DCF)CCl smiles:F[CH]C(=CF)CCl H298:-61.46 kcal/mol
library:CHOFClBr_G4 label:F[CH]CDC(Cl)CBr smiles:F[CH]C=C(Cl)CBr H298:-17.08 kcal/mol
library:CHOFClBr_G4 label:CC(Br)DC(Cl)[CH]F smiles:CC(Br)=C(Cl)[CH]F H298:-14.53 kcal/mol
library:CHOFClBr_G4 label:F[CH]CDCC(Cl)Br smiles:F[CH]C=CC(Cl)Br H298:-12.84 kcal/mol
library:CHOFClBr_G4 label:F[CH]C(Cl)DCCBr smiles:F[CH]C(Cl)=CCBr H298:-13.75 kcal/mol
library:CHOFClBr_G4 label:OC(Br)DC(Cl)[CH]F smiles:OC(Br)=C(Cl)[CH]F H298:-45.18 kcal/mol
library:CHOFBr_G4 label:CC(Br)DC(Br)[CH]F smiles:CC(Br)=C(Br)[CH]F H298:-3.00 kcal/mol
library:CHOFBr_G4 label:OCDC(Br)[CH]F smiles:OC=C(Br)[CH]F H298:-41.63 kcal/mol
library:CHOFBr_G4 label:F[CH]C(DCF)CBr smiles:F[CH]C(=CF)CBr H298:-50.79 kcal/mol
library:CHOFBr_G4 label:F[CH]CDCC(F)Br smiles:F[CH]C=CC(F)Br H298:-53.04 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)DCCBr smiles:F[CH]C(F)=CCBr H298:-51.48 kcal/mol
library:CHOFBr_G4 label:OC(Br)DC(F)[CH]F smiles:OC(Br)=C(F)[CH]F H298:-81.09 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)DCC(F)Br smiles:F[CH]C(F)=CC(F)Br H298:-95.16 kcal/mol
library:CHOFBr_G4 label:F[CH]C(DCF)C(Br)Br smiles:F[CH]C(=CF)C(Br)Br H298:-41.87 kcal/mol
library:CHOFBr_G4 label:F[CH]CDCCBr smiles:F[CH]C=CCBr H298:-8.63 kcal/mol
library:CHOFBr_G4 label:CDC([CH]F)OBr smiles:C=C([CH]F)OBr H298:-4.67 kcal/mol
library:CHOFBr_G4 label:F[CH]CDCC(F)(F)Br smiles:F[CH]C=CC(F)(F)Br H298:-105.24 kcal/mol
library:CHOFBr_G4 label:CDC([CH]F)C(Br)(Br)Br smiles:C=C([CH]F)C(Br)(Br)Br H298:12.99 kcal/mol
library:CHOFBr_G4 label:CDC([CH]F)C(F)Br smiles:C=C([CH]F)C(F)Br H298:-51.12 kcal/mol
library:CHOFBr_G4 label:F[CH]CDC(F)CBr smiles:F[CH]C=C(F)CBr H298:-54.42 kcal/mol
library:CHOFBr_G4 label:F[CH]CDC(Br)C(Br)Br smiles:F[CH]C=C(Br)C(Br)Br H298:2.69 kcal/mol
library:CHOFBr_G4 label:F[CH]C(DCF)C(F)Br smiles:F[CH]C(=CF)C(F)Br H298:-93.99 kcal/mol
library:CHOFBr_G4 label:OC(Br)DC(Br)[CH]F smiles:OC(Br)=C(Br)[CH]F H298:-34.01 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)DC(F)CBr smiles:F[CH]C(F)=C(F)CBr H298:-93.89 kcal/mol
library:CHOFBr_G4 label:F[CH]C(Br)DCCBr smiles:F[CH]C(Br)=CCBr H298:-2.23 kcal/mol
library:CHOFBr_G4 label:CC(Br)DC[CH]F smiles:CC(Br)=C[CH]F H298:-9.65 kcal/mol
library:CHOFBr_G4 label:F[CH]CDC(F)C(F)Br smiles:F[CH]C=C(F)C(F)Br H298:-95.56 kcal/mol
library:CHOFBr_G4 label:F[CH]CDCC(Br)(Br)Br smiles:F[CH]C=CC(Br)(Br)Br H298:8.46 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)DCC(Br)Br smiles:F[CH]C(F)=CC(Br)Br H298:-44.19 kcal/mol
library:CHOFBr_G4 label:F[CH]CDC(F)C(Br)Br smiles:F[CH]C=C(F)C(Br)Br H298:-45.67 kcal/mol
library:CHOFBr_G4 label:F[CH]C(Br)DC(Br)CBr smiles:F[CH]C(Br)=C(Br)CBr H298:2.49 kcal/mol
library:CHOFBr_G4 label:CCDC(Br)[CH]F smiles:CC=C(Br)[CH]F H298:-7.84 kcal/mol
library:CHOFBr_G4 label:F[CH]C(CBr)DC(F)F smiles:F[CH]C(CBr)=C(F)F H298:-96.91 kcal/mol
library:CHOFBr_G4 label:F[CH]CDCC(Br)Br smiles:F[CH]C=CC(Br)Br H298:-1.65 kcal/mol
library:CHOFBr_G4 label:CDC([CH]F)CBr smiles:C=C([CH]F)CBr H298:-7.28 kcal/mol
library:CHOFBr_G4 label:F[CH]CDCC(F)(Br)Br smiles:F[CH]C=CC(F)(Br)Br H298:-46.38 kcal/mol
library:CHOFBr_G4 label:CC(Br)DC(F)[CH]F smiles:CC(Br)=C(F)[CH]F H298:-52.38 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)DC(Br)CBr smiles:F[CH]C(F)=C(Br)CBr H298:-46.01 kcal/mol
library:CHOFBr_G4 label:CDC([CH]F)C(F)(F)Br smiles:C=C([CH]F)C(F)(F)Br H298:-102.84 kcal/mol
library:CHOFBr_G4 label:F[CH]C(DCF)OBr smiles:F[CH]C(=CF)OBr H298:-45.18 kcal/mol
library:CHOFBr_G4 label:F[CH]C(Br)DCC(Br)Br smiles:F[CH]C(Br)=CC(Br)Br H298:4.86 kcal/mol
library:CHOFBr_G4 label:F[CH]CDC(Br)CBr smiles:F[CH]C=C(Br)CBr H298:-5.13 kcal/mol
""",
)

entry(
    index = 64,
    label = "CsBr1sCdO2s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cd   u0 {1,S}
3   O2s  u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 65,
    label = "CsCdCl1sO2s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cd   u0 {1,S}
3   O2s  u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 66,
    label = "CsCdF1sO2s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S}
3   O2s u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 67,
    label = "CsBr1sCdCt",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cd   u0 {1,S}
3   Ct   u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 68,
    label = "CsCdCl1sCt",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cd   u0 {1,S}
3   Ct   u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 69,
    label = "CsCdCtF1s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S}
3   Ct  u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 70,
    label = "CsBr1sCdCd",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cd   u0 {1,S}
3   Cd   u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 71,
    label = "CsCdCdCl1s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cd   u0 {1,S}
3   Cd   u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 72,
    label = "CsCdCdF1s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S}
3   Cd  u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 73,
    label = "CsBr1sBr1sCs",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cs   u0 {1,S}
3   Br1s u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.19197,-2.14962,-2.87797,-3.44523,-4.21784,-4.66526,-5.11791],'cal/(mol*K)','+|-',[0.134507,0.138105,0.12949,0.120947,0.106738,0.0934038,0.0684109]),
        H298 = (93.8619,'kcal/mol','+|-',0.214874),
        S298 = (3.18111,'cal/(mol*K)','+|-',0.36517),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:Br[C](Br)CC(Br)Br smiles:Br[C](Br)CC(Br)Br H298:40.12 kcal/mol
library:CHOBr_G4 label:CCC[C](Br)Br smiles:CCC[C](Br)Br H298:23.14 kcal/mol
library:CHOBr_G4 label:BrC#CC[C](Br)Br smiles:BrC#CC[C](Br)Br H298:106.46 kcal/mol
library:CHOBr_G4 label:COC(Br)[C](Br)Br smiles:COC(Br)[C](Br)Br H298:4.23 kcal/mol
library:CHOBr_G4 label:CC[C](Br)Br smiles:CC[C](Br)Br H298:28.49 kcal/mol
library:CHOBr_G4 label:OCC(Br)[C](Br)Br smiles:OCC(Br)[C](Br)Br H298:-5.68 kcal/mol
library:CHOBr_G4 label:C#CC(Br)[C](Br)Br smiles:C#CC(Br)[C](Br)Br H298:101.84 kcal/mol
library:CHOBr_G4 label:BrC[C](Br)Br smiles:BrC[C](Br)Br H298:39.54 kcal/mol
library:CHOBr_G4 label:OC(CBr)[C](Br)Br smiles:OC(CBr)[C](Br)Br H298:-4.46 kcal/mol
library:CHOBr_G4 label:BrCCC[C](Br)Br smiles:BrCCC[C](Br)Br H298:27.38 kcal/mol
library:CHOBr_G4 label:BrCC[C](Br)Br smiles:BrCC[C](Br)Br H298:33.79 kcal/mol
library:CHOBr_G4 label:CC(C)[C](Br)Br smiles:CC(C)[C](Br)Br H298:20.83 kcal/mol
library:CHOBr_G4 label:CDCC[C](Br)Br smiles:C=CC[C](Br)Br H298:52.84 kcal/mol
library:CHOBr_G4 label:OC(Br)C[C](Br)Br smiles:OC(Br)C[C](Br)Br H298:-6.67 kcal/mol
library:CHOBr_G4 label:CC(Br)[C](Br)Br smiles:CC(Br)[C](Br)Br H298:30.61 kcal/mol
library:CHOBr_G4 label:OCC[C](Br)Br smiles:OCC[C](Br)Br H298:-7.24 kcal/mol
library:CHOBr_G4 label:BrOC(Br)C[C](Br)Br smiles:BrOC(Br)C[C](Br)Br H298:30.82 kcal/mol
library:CHOBr_G4 label:BrCC(Br)[C](Br)Br smiles:BrCC(Br)[C](Br)Br H298:35.79 kcal/mol
library:CHOBr_G4 label:CC(OBr)[C](Br)Br smiles:CC(OBr)[C](Br)Br H298:24.78 kcal/mol
library:CHOBr_G4 label:BrOCC[C](Br)Br smiles:BrOCC[C](Br)Br H298:28.26 kcal/mol
library:CHOBr_G4 label:BrCDCC[C](Br)Br smiles:BrC=CC[C](Br)Br H298:57.81 kcal/mol
library:CHOBr_G4 label:BrCOC[C](Br)Br smiles:BrCOC[C](Br)Br H298:5.46 kcal/mol
library:CHOBr_G4 label:BrOC(Br)[C](Br)Br smiles:BrOC(Br)[C](Br)Br H298:39.80 kcal/mol
library:CHOBr_G4 label:BrCC(Br)C[C](Br)Br smiles:BrCC(Br)C[C](Br)Br H298:31.11 kcal/mol
library:CHOBr_G4 label:CC(O)[C](Br)Br smiles:CC(O)[C](Br)Br H298:-10.92 kcal/mol
library:CHOBr_G4 label:BrOC[C](Br)Br smiles:BrOC[C](Br)Br H298:36.05 kcal/mol
library:CHOBr_G4 label:OC(OBr)[C](Br)Br smiles:OC(OBr)[C](Br)Br H298:-9.83 kcal/mol
library:CHOBr_G4 label:COC[C](Br)Br smiles:COC[C](Br)Br H298:3.12 kcal/mol
library:CHOBr_G4 label:C[C](Br)Br smiles:C[C](Br)Br H298:34.51 kcal/mol
library:CHOBr_G4 label:CC(Br)C[C](Br)Br smiles:CC(Br)C[C](Br)Br H298:24.81 kcal/mol
library:CHOBr_G4 label:Br[C](Br)C(Br)Br smiles:Br[C](Br)C(Br)Br H298:48.37 kcal/mol
library:CHOBr_G4 label:OC(Br)[C](Br)Br smiles:OC(Br)[C](Br)Br H298:0.23 kcal/mol
library:CHOBr_G4 label:OC[C](Br)Br smiles:OC[C](Br)Br H298:-0.63 kcal/mol
library:CHOBr_G4 label:BrOC(OBr)[C](Br)Br smiles:BrOC(OBr)[C](Br)Br H298:29.63 kcal/mol
library:CHOBr_G4 label:CDCC(Br)[C](Br)Br smiles:C=CC(Br)[C](Br)Br H298:56.46 kcal/mol
library:CHOBr_G4 label:CC(CBr)[C](Br)Br smiles:CC(CBr)[C](Br)Br H298:25.78 kcal/mol
library:CHOBr_G4 label:C#CC[C](Br)Br smiles:C#CC[C](Br)Br H298:96.04 kcal/mol
library:CHOBr_G4 label:BrCCC(Br)[C](Br)Br smiles:BrCCC(Br)[C](Br)Br H298:32.56 kcal/mol
library:CHOBr_G4 label:BrOOC[C](Br)Br smiles:BrOOC[C](Br)Br H298:51.88 kcal/mol
library:CHOBr_G4 label:BrOOC(Br)[C](Br)Br smiles:BrOOC(Br)[C](Br)Br H298:56.80 kcal/mol
library:CHOBr_G4 label:CDC(Br)C[C](Br)Br smiles:C=C(Br)C[C](Br)Br H298:56.28 kcal/mol
library:CHOBr_G4 label:BrCC(CBr)[C](Br)Br smiles:BrCC(CBr)[C](Br)Br H298:31.50 kcal/mol
library:CHOBr_G4 label:OOC[C](Br)Br smiles:OOC[C](Br)Br H298:17.58 kcal/mol
library:CHOBr_G4 label:CCC(Br)[C](Br)Br smiles:CCC(Br)[C](Br)Br H298:23.96 kcal/mol
library:CHOBr_G4 label:ODCC[C](Br)Br smiles:O=CC[C](Br)Br H298:11.48 kcal/mol
library:CHOBr_G4 label:OOC(Br)[C](Br)Br smiles:OOC(Br)[C](Br)Br H298:20.99 kcal/mol
library:CHOFBr_G4 label:C#CC(F)(Br)[C](Br)Br smiles:C#CC(F)(Br)[C](Br)Br H298:60.63 kcal/mol
library:CHOFBr_G4 label:C#CC(F)(F)[C](Br)Br smiles:C#CC(F)(F)[C](Br)Br H298:4.71 kcal/mol
library:CHOFBr_G4 label:FC#CC(F)[C](Br)Br smiles:FC#CC(F)[C](Br)Br H298:25.53 kcal/mol
library:CHOFBr_G4 label:FC#CC[C](Br)Br smiles:FC#CC[C](Br)Br H298:67.65 kcal/mol
library:CHOFBr_G4 label:FC#CC(Br)[C](Br)Br smiles:FC#CC(Br)[C](Br)Br H298:73.55 kcal/mol
library:CHOFBr_G4 label:C#CC(F)[C](Br)Br smiles:C#CC(F)[C](Br)Br H298:54.43 kcal/mol
library:CHOClBr_G4 label:ClC#CC[C](Br)Br smiles:ClC#CC[C](Br)Br H298:95.40 kcal/mol
library:CHOClBr_G4 label:C#CC(Cl)[C](Br)Br smiles:C#CC(Cl)[C](Br)Br H298:91.95 kcal/mol
""",
)

entry(
    index = 74,
    label = "CsBr1sCl1sCs",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cs   u0 {1,S}
3   Cl1s u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.858948,-1.74583,-2.4483,-3.02148,-3.84165,-4.36667,-5.01023],'cal/(mol*K)','+|-',[0.164737,0.169143,0.158592,0.148129,0.130727,0.114396,0.0837859]),
        H298 = (93.5587,'kcal/mol','+|-',0.263166),
        S298 = (4.1303,'cal/(mol*K)','+|-',0.44724),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFClBr_G4 label:C#CC(F)[C](Cl)Br smiles:C#CC(F)[C](Cl)Br H298:42.56 kcal/mol
library:CHOFClBr_G4 label:FC#CC[C](Cl)Br smiles:FC#CC[C](Cl)Br H298:55.75 kcal/mol
library:CHOClBr_G4 label:Cl[C](Br)CCBr smiles:Cl[C](Br)CCBr H298:21.58 kcal/mol
library:CHOClBr_G4 label:OC(O)[C](Cl)Br smiles:OC(O)[C](Cl)Br H298:-58.30 kcal/mol
library:CHOClBr_G4 label:CC(OBr)[C](Cl)Br smiles:CC(OBr)[C](Cl)Br H298:12.81 kcal/mol
library:CHOClBr_G4 label:ClC#CC[C](Cl)Br smiles:ClC#CC[C](Cl)Br H298:83.54 kcal/mol
library:CHOClBr_G4 label:CC(Br)(Br)[C](Cl)Br smiles:CC(Br)(Br)[C](Cl)Br H298:26.99 kcal/mol
library:CHOClBr_G4 label:CDCC[C](Cl)Br smiles:C=CC[C](Cl)Br H298:41.82 kcal/mol
library:CHOClBr_G4 label:OC(Br)C[C](Cl)Br smiles:OC(Br)C[C](Cl)Br H298:-18.77 kcal/mol
library:CHOClBr_G4 label:CC(Br)[C](Cl)Br smiles:CC(Br)[C](Cl)Br H298:18.71 kcal/mol
library:CHOClBr_G4 label:OCC[C](Cl)Br smiles:OCC[C](Cl)Br H298:-19.03 kcal/mol
library:CHOClBr_G4 label:OC(CBr)[C](Cl)Br smiles:OC(CBr)[C](Cl)Br H298:-16.22 kcal/mol
library:CHOClBr_G4 label:Cl[C](Br)C(Br)Br smiles:Cl[C](Br)C(Br)Br H298:36.65 kcal/mol
library:CHOClBr_G4 label:CC(C)(Br)[C](Cl)Br smiles:CC(C)(Br)[C](Cl)Br H298:10.00 kcal/mol
library:CHOClBr_G4 label:CC(C)[C](Cl)Br smiles:CC(C)[C](Cl)Br H298:8.81 kcal/mol
library:CHOClBr_G4 label:OC(Br)(Br)[C](Cl)Br smiles:OC(Br)(Br)[C](Cl)Br H298:-3.02 kcal/mol
library:CHOClBr_G4 label:CCC[C](Cl)Br smiles:CCC[C](Cl)Br H298:11.30 kcal/mol
library:CHOClBr_G4 label:COC(Br)[C](Cl)Br smiles:COC(Br)[C](Cl)Br H298:-7.46 kcal/mol
library:CHOClBr_G4 label:CC[C](Cl)Br smiles:CC[C](Cl)Br H298:16.52 kcal/mol
library:CHOClBr_G4 label:OCC(Br)[C](Cl)Br smiles:OCC(Br)[C](Cl)Br H298:-17.43 kcal/mol
library:CHOClBr_G4 label:Cl[C](Br)CBr smiles:Cl[C](Br)CBr H298:27.66 kcal/mol
library:CHOClBr_G4 label:OOC[C](Cl)Br smiles:OOC[C](Cl)Br H298:5.86 kcal/mol
library:CHOClBr_G4 label:CCC(Br)[C](Cl)Br smiles:CCC(Br)[C](Cl)Br H298:12.36 kcal/mol
library:CHOClBr_G4 label:ODCC[C](Cl)Br smiles:O=CC[C](Cl)Br H298:-1.27 kcal/mol
library:CHOClBr_G4 label:CC(CBr)[C](Cl)Br smiles:CC(CBr)[C](Cl)Br H298:14.04 kcal/mol
library:CHOClBr_G4 label:C#CC[C](Cl)Br smiles:C#CC[C](Cl)Br H298:84.08 kcal/mol
library:CHOClBr_G4 label:ODCC(Br)[C](Cl)Br smiles:O=CC(Br)[C](Cl)Br H298:4.27 kcal/mol
library:CHOClBr_G4 label:C[C](Cl)Br smiles:C[C](Cl)Br H298:22.29 kcal/mol
library:CHOClBr_G4 label:OC(Br)[C](Cl)Br smiles:OC(Br)[C](Cl)Br H298:-11.37 kcal/mol
library:CHOClBr_G4 label:C#CC(Cl)[C](Cl)Br smiles:C#CC(Cl)[C](Cl)Br H298:80.12 kcal/mol
library:CHOClBr_G4 label:CC(Br)C[C](Cl)Br smiles:CC(Br)C[C](Cl)Br H298:13.08 kcal/mol
library:CHOClBr_G4 label:OC[C](Cl)Br smiles:OC[C](Cl)Br H298:-12.55 kcal/mol
library:CHOClBr_G4 label:ODC(Br)C[C](Cl)Br smiles:O=C(Br)C[C](Cl)Br H298:-5.79 kcal/mol
library:CHOClBr_G4 label:CC(O)[C](Cl)Br smiles:CC(O)[C](Cl)Br H298:-22.57 kcal/mol
library:CHOClBr_G4 label:Cl[C](Br)COBr smiles:Cl[C](Br)COBr H298:24.29 kcal/mol
library:CHOClBr_G4 label:OC(OBr)[C](Cl)Br smiles:OC(OBr)[C](Cl)Br H298:-21.52 kcal/mol
""",
)

entry(
    index = 75,
    label = "CsCl1sCl1sCs",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cs   u0 {1,S}
3   Cl1s u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.450315,-1.47843,-2.32038,-2.99802,-3.92933,-4.48895,-5.1497],'cal/(mol*K)','+|-',[0.0698921,0.0717613,0.067285,0.0628459,0.0554628,0.048534,0.0355474]),
        H298 = (92.1198,'kcal/mol','+|-',0.111652),
        S298 = (3.72281,'cal/(mol*K)','+|-',0.189748),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:ATcT_halogens label:Pentachloroethyl smiles:Cl[C](Cl)C(Cl)(Cl)Cl H298:6.00 kcal/mol
library:CHOCl_G4 label:OC(Cl)(OCl)[C](Cl)Cl smiles:OC(Cl)(OCl)[C](Cl)Cl H298:-42.67 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)C(Cl)C(Cl)Cl smiles:Cl[C](Cl)C(Cl)C(Cl)Cl H298:-11.60 kcal/mol
library:CHOCl_G4 label:CC(Cl)([C](Cl)Cl)C(Cl)Cl smiles:CC(Cl)([C](Cl)Cl)C(Cl)Cl H298:-21.28 kcal/mol
library:CHOCl_G4 label:OC(CCl)[C](Cl)Cl smiles:OC(CCl)[C](Cl)Cl H298:-38.99 kcal/mol
library:CHOCl_G4 label:OC(Cl)([C](Cl)Cl)C(Cl)Cl smiles:OC(Cl)([C](Cl)Cl)C(Cl)Cl H298:-52.76 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(Cl)C[C](Cl)Cl smiles:ClCC(Cl)(Cl)C[C](Cl)Cl H298:-20.56 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)[C](Cl)Cl smiles:ClOC(Cl)[C](Cl)Cl H298:2.78 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)CC(Cl)C(Cl)Cl smiles:Cl[C](Cl)CC(Cl)C(Cl)Cl H298:-19.42 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)C(Cl)[C](Cl)Cl smiles:ClCC(Cl)C(Cl)[C](Cl)Cl H298:-22.16 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)COC(Cl)Cl smiles:Cl[C](Cl)COC(Cl)Cl H298:-36.29 kcal/mol
library:CHOCl_G4 label:ClC[C](Cl)Cl smiles:ClC[C](Cl)Cl H298:5.60 kcal/mol
library:CHOCl_G4 label:CC(O)[C](Cl)Cl smiles:CC(O)[C](Cl)Cl H298:-34.16 kcal/mol
library:CHOCl_G4 label:OOC(Cl)(Cl)[C](Cl)Cl smiles:OOC(Cl)(Cl)[C](Cl)Cl H298:-17.20 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)C(C(Cl)Cl)C(Cl)(Cl)Cl smiles:Cl[C](Cl)C(C(Cl)Cl)C(Cl)(Cl)Cl H298:-21.01 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)C(Cl)(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:Cl[C](Cl)C(Cl)(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-12.04 kcal/mol
library:CHOCl_G4 label:CC(C)(Cl)[C](Cl)Cl smiles:CC(C)(Cl)[C](Cl)Cl H298:-12.72 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)C(Cl)OC(Cl)Cl smiles:Cl[C](Cl)C(Cl)OC(Cl)Cl H298:-42.91 kcal/mol
library:CHOCl_G4 label:OC(O)(Cl)[C](Cl)Cl smiles:OC(O)(Cl)[C](Cl)Cl H298:-79.50 kcal/mol
library:CHOCl_G4 label:CCC(Cl)(Cl)[C](Cl)Cl smiles:CCC(Cl)(Cl)[C](Cl)Cl H298:-13.55 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)C[C](Cl)Cl smiles:ClOC(Cl)C[C](Cl)Cl H298:-7.08 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)C(Cl)(C(Cl)Cl)C(Cl)Cl smiles:Cl[C](Cl)C(Cl)(C(Cl)Cl)C(Cl)Cl H298:-24.02 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)C(Cl)(Cl)OC(Cl)(Cl)Cl smiles:Cl[C](Cl)C(Cl)(Cl)OC(Cl)(Cl)Cl H298:-42.48 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)(Cl)C(Cl)[C](Cl)Cl smiles:ClOC(Cl)(Cl)C(Cl)[C](Cl)Cl H298:-15.26 kcal/mol
library:CHOCl_G4 label:ClOCC(Cl)[C](Cl)Cl smiles:ClOCC(Cl)[C](Cl)Cl H298:-4.18 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(Cl)C(Cl)[C](Cl)Cl smiles:ClCC(Cl)(Cl)C(Cl)[C](Cl)Cl H298:-22.68 kcal/mol
library:CHOCl_G4 label:ClOCC[C](Cl)Cl smiles:ClOCC[C](Cl)Cl H298:1.65 kcal/mol
library:CHOCl_G4 label:ClCOC(Cl)[C](Cl)Cl smiles:ClCOC(Cl)[C](Cl)Cl H298:-39.07 kcal/mol
library:CHOCl_G4 label:OC[C](Cl)Cl smiles:OC[C](Cl)Cl H298:-24.28 kcal/mol
library:CHOCl_G4 label:CDC(Cl)C(Cl)[C](Cl)Cl smiles:C=C(Cl)C(Cl)[C](Cl)Cl H298:14.72 kcal/mol
library:CHOCl_G4 label:OCC(Cl)[C](Cl)Cl smiles:OCC(Cl)[C](Cl)Cl H298:-39.50 kcal/mol
library:CHOCl_G4 label:C#CC(Cl)[C](Cl)Cl smiles:C#CC(Cl)[C](Cl)Cl H298:68.28 kcal/mol
library:CHOCl_G4 label:OC(Cl)C[C](Cl)Cl smiles:OC(Cl)C[C](Cl)Cl H298:-42.24 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)C(Cl)(C(Cl)Cl)C(Cl)(Cl)Cl smiles:Cl[C](Cl)C(Cl)(C(Cl)Cl)C(Cl)(Cl)Cl H298:-20.31 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(CCl)[C](Cl)Cl smiles:ClCC(Cl)(CCl)[C](Cl)Cl H298:-22.38 kcal/mol
library:CHOCl_G4 label:OC([C](Cl)Cl)C(Cl)(Cl)Cl smiles:OC([C](Cl)Cl)C(Cl)(Cl)Cl H298:-46.06 kcal/mol
library:CHOCl_G4 label:OC([C](Cl)Cl)C(Cl)Cl smiles:OC([C](Cl)Cl)C(Cl)Cl H298:-43.31 kcal/mol
library:CHOCl_G4 label:COC(Cl)[C](Cl)Cl smiles:COC(Cl)[C](Cl)Cl H298:-30.42 kcal/mol
library:CHOCl_G4 label:COC[C](Cl)Cl smiles:COC[C](Cl)Cl H298:-20.35 kcal/mol
library:CHOCl_G4 label:C[C](Cl)Cl smiles:C[C](Cl)Cl H298:10.12 kcal/mol
library:CHOCl_G4 label:CC([C](Cl)Cl)C(Cl)(Cl)Cl smiles:CC([C](Cl)Cl)C(Cl)(Cl)Cl H298:-15.83 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)C(Cl)C(Cl)C(Cl)Cl smiles:Cl[C](Cl)C(Cl)C(Cl)C(Cl)Cl H298:-24.93 kcal/mol
library:CHOCl_G4 label:ClCC[C](Cl)Cl smiles:ClCC[C](Cl)Cl H298:-1.39 kcal/mol
library:CHOCl_G4 label:OCC(Cl)(Cl)[C](Cl)Cl smiles:OCC(Cl)(Cl)[C](Cl)Cl H298:-43.49 kcal/mol
library:CHOCl_G4 label:ClCC(OCl)[C](Cl)Cl smiles:ClCC(OCl)[C](Cl)Cl H298:-5.10 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)CC(Cl)(Cl)C(Cl)(Cl)Cl smiles:Cl[C](Cl)CC(Cl)(Cl)C(Cl)(Cl)Cl H298:-22.91 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)C(Cl)Cl smiles:Cl[C](Cl)C(Cl)Cl H298:2.84 kcal/mol
library:CHOCl_G4 label:ClC#CC(Cl)[C](Cl)Cl smiles:ClC#CC(Cl)[C](Cl)Cl H298:67.49 kcal/mol
library:CHOCl_G4 label:ODC(Cl)C(Cl)[C](Cl)Cl smiles:O=C(Cl)C(Cl)[C](Cl)Cl H298:-32.62 kcal/mol
library:CHOCl_G4 label:C#CC[C](Cl)Cl smiles:C#CC[C](Cl)Cl H298:72.01 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)CC(Cl)DC(Cl)Cl smiles:Cl[C](Cl)CC(Cl)=C(Cl)Cl H298:11.38 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)C(Cl)(Cl)OC(Cl)Cl smiles:Cl[C](Cl)C(Cl)(Cl)OC(Cl)Cl H298:-45.21 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)C(Cl)(Cl)C(Cl)DC(Cl)Cl smiles:Cl[C](Cl)C(Cl)(Cl)C(Cl)=C(Cl)Cl H298:12.32 kcal/mol
library:CHOCl_G4 label:CC([C](Cl)Cl)C(Cl)Cl smiles:CC([C](Cl)Cl)C(Cl)Cl H298:-14.08 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:Cl[C](Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-10.20 kcal/mol
library:CHOCl_G4 label:CC(OCl)[C](Cl)Cl smiles:CC(OCl)[C](Cl)Cl H298:-1.33 kcal/mol
library:CHOCl_G4 label:C#CC(Cl)(Cl)[C](Cl)Cl smiles:C#CC(Cl)(Cl)[C](Cl)Cl H298:67.47 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)C(Cl)C(Cl)C(Cl)(Cl)Cl smiles:Cl[C](Cl)C(Cl)C(Cl)C(Cl)(Cl)Cl H298:-23.23 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)(Cl)C[C](Cl)Cl smiles:ClOC(Cl)(Cl)C[C](Cl)Cl H298:-12.32 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)C(Cl)(Cl)CDC(Cl)Cl smiles:Cl[C](Cl)C(Cl)(Cl)C=C(Cl)Cl H298:10.21 kcal/mol
library:CHOCl_G4 label:COC(Cl)(Cl)[C](Cl)Cl smiles:COC(Cl)(Cl)[C](Cl)Cl H298:-35.59 kcal/mol
library:CHOCl_G4 label:ClCDCC[C](Cl)Cl smiles:ClC=CC[C](Cl)Cl H298:22.08 kcal/mol
library:CHOCl_G4 label:CC(Cl)[C](Cl)Cl smiles:CC(Cl)[C](Cl)Cl H298:-3.47 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)C(Cl)(Cl)C(Cl)C(Cl)(Cl)Cl smiles:Cl[C](Cl)C(Cl)(Cl)C(Cl)C(Cl)(Cl)Cl H298:-19.84 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)C(Cl)[C](Cl)Cl smiles:ClOC(Cl)C(Cl)[C](Cl)Cl H298:-14.52 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)CC(Cl)(Cl)C(Cl)Cl smiles:Cl[C](Cl)CC(Cl)(Cl)C(Cl)Cl H298:-22.95 kcal/mol
library:CHOCl_G4 label:CC(Cl)(OCl)[C](Cl)Cl smiles:CC(Cl)(OCl)[C](Cl)Cl H298:-7.66 kcal/mol
library:CHOCl_G4 label:ODCC[C](Cl)Cl smiles:O=CC[C](Cl)Cl H298:-12.41 kcal/mol
library:CHOCl_G4 label:OOC[C](Cl)Cl smiles:OOC[C](Cl)Cl H298:-5.94 kcal/mol
library:CHOCl_G4 label:OC(Cl)C(Cl)(Cl)[C](Cl)Cl smiles:OC(Cl)C(Cl)(Cl)[C](Cl)Cl H298:-51.06 kcal/mol
library:CHOCl_G4 label:CC(Cl)C(Cl)(Cl)[C](Cl)Cl smiles:CC(Cl)C(Cl)(Cl)[C](Cl)Cl H298:-19.96 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)C(Cl)(Cl)CC(Cl)(Cl)Cl smiles:Cl[C](Cl)C(Cl)(Cl)CC(Cl)(Cl)Cl H298:-21.80 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)C(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:Cl[C](Cl)C(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-22.62 kcal/mol
library:CHOCl_G4 label:ClCDCC(Cl)(Cl)[C](Cl)Cl smiles:ClC=CC(Cl)(Cl)[C](Cl)Cl H298:13.92 kcal/mol
library:CHOCl_G4 label:ClCCC[C](Cl)Cl smiles:ClCCC[C](Cl)Cl H298:-7.53 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)C(Cl)C(Cl)(Cl)Cl smiles:Cl[C](Cl)C(Cl)C(Cl)(Cl)Cl H298:-11.31 kcal/mol
library:CHOCl_G4 label:ClCOC(Cl)(Cl)[C](Cl)Cl smiles:ClCOC(Cl)(Cl)[C](Cl)Cl H298:-40.09 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)COC(Cl)(Cl)Cl smiles:Cl[C](Cl)COC(Cl)(Cl)Cl H298:-38.28 kcal/mol
library:CHOCl_G4 label:OC(Cl)[C](Cl)Cl smiles:OC(Cl)[C](Cl)Cl H298:-34.57 kcal/mol
library:CHOCl_G4 label:OC(Cl)C(Cl)[C](Cl)Cl smiles:OC(Cl)C(Cl)[C](Cl)Cl H298:-47.62 kcal/mol
library:CHOCl_G4 label:ClOOC[C](Cl)Cl smiles:ClOOC[C](Cl)Cl H298:24.72 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)C(Cl)C(Cl)(Cl)C(Cl)Cl smiles:Cl[C](Cl)C(Cl)C(Cl)(Cl)C(Cl)Cl H298:-26.41 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)C(Cl)C(Cl)DC(Cl)Cl smiles:Cl[C](Cl)C(Cl)C(Cl)=C(Cl)Cl H298:8.46 kcal/mol
library:CHOCl_G4 label:CC(Cl)([C](Cl)Cl)C(Cl)(Cl)Cl smiles:CC(Cl)([C](Cl)Cl)C(Cl)(Cl)Cl H298:-18.62 kcal/mol
library:CHOCl_G4 label:CC[C](Cl)Cl smiles:CC[C](Cl)Cl H298:4.50 kcal/mol
library:CHOCl_G4 label:OC(Cl)(Cl)C[C](Cl)Cl smiles:OC(Cl)(Cl)C[C](Cl)Cl H298:-49.35 kcal/mol
library:CHOCl_G4 label:CC(Cl)(Cl)[C](Cl)Cl smiles:CC(Cl)(Cl)[C](Cl)Cl H298:-7.40 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(OCl)[C](Cl)Cl smiles:ClCC(Cl)(OCl)[C](Cl)Cl H298:-10.30 kcal/mol
library:CHOCl_G4 label:CDCC(Cl)[C](Cl)Cl smiles:C=CC(Cl)[C](Cl)Cl H298:22.54 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)C(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:Cl[C](Cl)C(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-17.34 kcal/mol
library:CHOCl_G4 label:CCC[C](Cl)Cl smiles:CCC[C](Cl)Cl H298:-0.74 kcal/mol
library:CHOCl_G4 label:OC(Cl)([C](Cl)Cl)C(Cl)(Cl)Cl smiles:OC(Cl)([C](Cl)Cl)C(Cl)(Cl)Cl H298:-50.43 kcal/mol
library:CHOCl_G4 label:CDC(Cl)C[C](Cl)Cl smiles:C=C(Cl)C[C](Cl)Cl H298:20.47 kcal/mol
library:CHOCl_G4 label:ODCC(Cl)(Cl)[C](Cl)Cl smiles:O=CC(Cl)(Cl)[C](Cl)Cl H298:-19.19 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)([C](Cl)Cl)C(Cl)Cl smiles:ClCC(Cl)([C](Cl)Cl)C(Cl)Cl H298:-21.60 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)C(Cl)CC(Cl)(Cl)Cl smiles:Cl[C](Cl)C(Cl)CC(Cl)(Cl)Cl H298:-23.21 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)([C](Cl)Cl)C(Cl)Cl smiles:ClOC(Cl)([C](Cl)Cl)C(Cl)Cl H298:-13.93 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)(Cl)[C](Cl)Cl smiles:ClOC(Cl)(Cl)[C](Cl)Cl H298:-0.75 kcal/mol
library:CHOCl_G4 label:ClOC([C](Cl)Cl)C(Cl)(Cl)Cl smiles:ClOC([C](Cl)Cl)C(Cl)(Cl)Cl H298:-9.76 kcal/mol
library:CHOCl_G4 label:ClCC([C](Cl)Cl)C(Cl)(Cl)Cl smiles:ClCC([C](Cl)Cl)C(Cl)(Cl)Cl H298:-20.72 kcal/mol
library:CHOCl_G4 label:CC(C)[C](Cl)Cl smiles:CC(C)[C](Cl)Cl H298:-3.16 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)C(Cl)(Cl)C(Cl)Cl smiles:Cl[C](Cl)C(Cl)(Cl)C(Cl)Cl H298:-12.97 kcal/mol
library:CHOCl_G4 label:ClOC(OCl)[C](Cl)Cl smiles:ClOC(OCl)[C](Cl)Cl H298:1.85 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)([C](Cl)Cl)C(Cl)(Cl)Cl smiles:ClCC(Cl)([C](Cl)Cl)C(Cl)(Cl)Cl H298:-21.40 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)C(Cl)CC(Cl)Cl smiles:Cl[C](Cl)C(Cl)CC(Cl)Cl H298:-21.29 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)C(Cl)(Cl)C(Cl)C(Cl)Cl smiles:Cl[C](Cl)C(Cl)(Cl)C(Cl)C(Cl)Cl H298:-24.06 kcal/mol
library:CHOCl_G4 label:ClOCC(Cl)(Cl)[C](Cl)Cl smiles:ClOCC(Cl)(Cl)[C](Cl)Cl H298:-7.31 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)CC(Cl)C(Cl)(Cl)Cl smiles:Cl[C](Cl)CC(Cl)C(Cl)(Cl)Cl H298:-21.59 kcal/mol
library:CHOCl_G4 label:OC(OCl)[C](Cl)Cl smiles:OC(OCl)[C](Cl)Cl H298:-35.91 kcal/mol
library:CHOCl_G4 label:ClCC([C](Cl)Cl)C(Cl)Cl smiles:ClCC([C](Cl)Cl)C(Cl)Cl H298:-18.49 kcal/mol
library:CHOCl_G4 label:OC(Cl)(CCl)[C](Cl)Cl smiles:OC(Cl)(CCl)[C](Cl)Cl H298:-48.72 kcal/mol
library:CHOCl_G4 label:OC(Cl)(Cl)C(Cl)[C](Cl)Cl smiles:OC(Cl)(Cl)C(Cl)[C](Cl)Cl H298:-52.79 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)([C](Cl)Cl)C(Cl)(Cl)Cl smiles:ClOC(Cl)([C](Cl)Cl)C(Cl)(Cl)Cl H298:-12.45 kcal/mol
library:CHOCl_G4 label:CC(Cl)(Cl)C(Cl)[C](Cl)Cl smiles:CC(Cl)(Cl)C(Cl)[C](Cl)Cl H298:-20.60 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)C(Cl)(Cl)C(Cl)(Cl)C(Cl)Cl smiles:Cl[C](Cl)C(Cl)(Cl)C(Cl)(Cl)C(Cl)Cl H298:-21.44 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)C(Cl)[C](Cl)Cl smiles:ClC=C(Cl)C(Cl)[C](Cl)Cl H298:12.34 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)CCC(Cl)Cl smiles:Cl[C](Cl)CCC(Cl)Cl H298:-13.46 kcal/mol
library:CHOCl_G4 label:ClOOC(Cl)[C](Cl)Cl smiles:ClOOC(Cl)[C](Cl)Cl H298:18.96 kcal/mol
library:CHOCl_G4 label:OCC[C](Cl)Cl smiles:OCC[C](Cl)Cl H298:-31.03 kcal/mol
library:CHOCl_G4 label:ClCCC(Cl)(Cl)[C](Cl)Cl smiles:ClCCC(Cl)(Cl)[C](Cl)Cl H298:-18.69 kcal/mol
library:CHOCl_G4 label:OC(Cl)(Cl)[C](Cl)Cl smiles:OC(Cl)(Cl)[C](Cl)Cl H298:-38.34 kcal/mol
library:CHOCl_G4 label:CC(Cl)(Cl)C(Cl)(Cl)[C](Cl)Cl smiles:CC(Cl)(Cl)C(Cl)(Cl)[C](Cl)Cl H298:-19.55 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)C[C](Cl)Cl smiles:ClCC(Cl)C[C](Cl)Cl H298:-15.14 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)C(Cl)OC(Cl)(Cl)Cl smiles:Cl[C](Cl)C(Cl)OC(Cl)(Cl)Cl H298:-44.18 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)C(C(Cl)Cl)C(Cl)Cl smiles:Cl[C](Cl)C(C(Cl)Cl)C(Cl)Cl H298:-18.04 kcal/mol
library:CHOCl_G4 label:ClCCC(Cl)[C](Cl)Cl smiles:ClCCC(Cl)[C](Cl)Cl H298:-15.80 kcal/mol
library:CHOCl_G4 label:ClC#CC(Cl)(Cl)[C](Cl)Cl smiles:ClC#CC(Cl)(Cl)[C](Cl)Cl H298:66.15 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)CCC(Cl)(Cl)Cl smiles:Cl[C](Cl)CCC(Cl)(Cl)Cl H298:-17.63 kcal/mol
library:CHOCl_G4 label:ClCOC[C](Cl)Cl smiles:ClCOC[C](Cl)Cl H298:-29.99 kcal/mol
library:CHOCl_G4 label:OOC(Cl)[C](Cl)Cl smiles:OOC(Cl)[C](Cl)Cl H298:-14.28 kcal/mol
library:CHOCl_G4 label:ClOC([C](Cl)Cl)C(Cl)Cl smiles:ClOC([C](Cl)Cl)C(Cl)Cl H298:-8.83 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)CC(Cl)(Cl)Cl smiles:Cl[C](Cl)CC(Cl)(Cl)Cl H298:-8.27 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(Cl)[C](Cl)Cl smiles:ClCC(Cl)(Cl)[C](Cl)Cl H298:-10.94 kcal/mol
library:CHOCl_G4 label:CDCC[C](Cl)Cl smiles:C=CC[C](Cl)Cl H298:29.82 kcal/mol
library:CHOCl_G4 label:CCC(Cl)[C](Cl)Cl smiles:CCC(Cl)[C](Cl)Cl H298:-9.48 kcal/mol
library:CHOCl_G4 label:CC(Cl)(CCl)[C](Cl)Cl smiles:CC(Cl)(CCl)[C](Cl)Cl H298:-18.03 kcal/mol
library:CHOCl_G4 label:CC(Cl)C[C](Cl)Cl smiles:CC(Cl)C[C](Cl)Cl H298:-10.11 kcal/mol
library:CHOCl_G4 label:OC(Cl)(Cl)C(Cl)(Cl)[C](Cl)Cl smiles:OC(Cl)(Cl)C(Cl)(Cl)[C](Cl)Cl H298:-51.52 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(Cl)C(Cl)(Cl)[C](Cl)Cl smiles:ClCC(Cl)(Cl)C(Cl)(Cl)[C](Cl)Cl H298:-21.45 kcal/mol
library:CHOCl_G4 label:ODC(Cl)C[C](Cl)Cl smiles:O=C(Cl)C[C](Cl)Cl H298:-30.09 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)CC(Cl)Cl smiles:Cl[C](Cl)CC(Cl)Cl H298:-6.23 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)(OCl)[C](Cl)Cl smiles:ClOC(Cl)(OCl)[C](Cl)Cl H298:-5.28 kcal/mol
library:CHOCl_G4 label:CDCC(Cl)(Cl)[C](Cl)Cl smiles:C=CC(Cl)(Cl)[C](Cl)Cl H298:19.97 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)C(Cl)(Cl)CC(Cl)Cl smiles:Cl[C](Cl)C(Cl)(Cl)CC(Cl)Cl H298:-22.70 kcal/mol
library:CHOCl_G4 label:ODCC(Cl)[C](Cl)Cl smiles:O=CC(Cl)[C](Cl)Cl H298:-17.19 kcal/mol
library:CHOCl_G4 label:ClOC[C](Cl)Cl smiles:ClOC[C](Cl)Cl H298:9.27 kcal/mol
library:CHOCl_G4 label:CC(Cl)C(Cl)[C](Cl)Cl smiles:CC(Cl)C(Cl)[C](Cl)Cl H298:-16.23 kcal/mol
library:CHOCl_G4 label:Cl[C](Cl)C(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:Cl[C](Cl)C(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-17.35 kcal/mol
library:CHOCl_G4 label:ClOOC(Cl)(Cl)[C](Cl)Cl smiles:ClOOC(Cl)(Cl)[C](Cl)Cl H298:16.20 kcal/mol
library:CHOCl_G4 label:CC(Cl)(Cl)C[C](Cl)Cl smiles:CC(Cl)(Cl)C[C](Cl)Cl H298:-16.16 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)C(Cl)(Cl)[C](Cl)Cl smiles:ClOC(Cl)C(Cl)(Cl)[C](Cl)Cl H298:-13.60 kcal/mol
library:CHOCl_G4 label:ClC#CC[C](Cl)Cl smiles:ClC#CC[C](Cl)Cl H298:71.58 kcal/mol
library:CHOCl_G4 label:CC(CCl)[C](Cl)Cl smiles:CC(CCl)[C](Cl)Cl H298:-8.66 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)[C](Cl)Cl smiles:ClCC(Cl)[C](Cl)Cl H298:-8.53 kcal/mol
library:CHOCl_G4 label:OC(O)[C](Cl)Cl smiles:OC(O)[C](Cl)Cl H298:-70.36 kcal/mol
library:CHOCl_G4 label:ClCDCC(Cl)[C](Cl)Cl smiles:ClC=CC(Cl)[C](Cl)Cl H298:16.06 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)(Cl)C(Cl)(Cl)[C](Cl)Cl smiles:ClOC(Cl)(Cl)C(Cl)(Cl)[C](Cl)Cl H298:-13.94 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)C[C](Cl)Cl smiles:ClC=C(Cl)C[C](Cl)Cl H298:15.24 kcal/mol
library:CHOCl_G4 label:ClCC(CCl)[C](Cl)Cl smiles:ClCC(CCl)[C](Cl)Cl H298:-14.08 kcal/mol
library:CHOCl_G4 label:CC(O)(Cl)[C](Cl)Cl smiles:CC(O)(Cl)[C](Cl)Cl H298:-46.17 kcal/mol
library:CHOCl_G4 label:ODC(Cl)C(Cl)(Cl)[C](Cl)Cl smiles:O=C(Cl)C(Cl)(Cl)[C](Cl)Cl H298:-33.80 kcal/mol
library:CHOFCl_G4 label:FC#CC[C](Cl)Cl smiles:FC#CC[C](Cl)Cl H298:43.87 kcal/mol
library:CHOFCl_G4 label:C#CC(F)[C](Cl)Cl smiles:C#CC(F)[C](Cl)Cl H298:30.64 kcal/mol
library:CHOClBr_G4 label:OC(OBr)[C](Cl)Cl smiles:OC(OBr)[C](Cl)Cl H298:-33.10 kcal/mol
library:CHOClBr_G4 label:Cl[C](Cl)C(Cl)(Br)Br smiles:Cl[C](Cl)C(Cl)(Br)Br H298:25.77 kcal/mol
library:CHOClBr_G4 label:ODC(Br)C[C](Cl)Cl smiles:O=C(Br)C[C](Cl)Cl H298:-17.77 kcal/mol
library:CHOClBr_G4 label:Cl[C](Cl)CC(Cl)Br smiles:Cl[C](Cl)CC(Cl)Br H298:5.39 kcal/mol
library:CHOClBr_G4 label:Cl[C](Cl)C(Br)CBr smiles:Cl[C](Cl)C(Br)CBr H298:12.15 kcal/mol
library:CHOClBr_G4 label:CC(Br)C[C](Cl)Cl smiles:CC(Br)C[C](Cl)Cl H298:1.21 kcal/mol
library:CHOClBr_G4 label:OC(Br)[C](Cl)Cl smiles:OC(Br)[C](Cl)Cl H298:-23.42 kcal/mol
library:CHOClBr_G4 label:CC(Cl)(Br)[C](Cl)Cl smiles:CC(Cl)(Br)[C](Cl)Cl H298:3.71 kcal/mol
library:CHOClBr_G4 label:Cl[C](Cl)C(Cl)CBr smiles:Cl[C](Cl)C(Cl)CBr H298:2.21 kcal/mol
library:CHOClBr_G4 label:CC(O)(Br)[C](Cl)Cl smiles:CC(O)(Br)[C](Cl)Cl H298:-33.94 kcal/mol
library:CHOClBr_G4 label:ODCC(Br)[C](Cl)Cl smiles:O=CC(Br)[C](Cl)Cl H298:-7.65 kcal/mol
library:CHOClBr_G4 label:CC(CBr)[C](Cl)Cl smiles:CC(CBr)[C](Cl)Cl H298:2.22 kcal/mol
library:CHOClBr_G4 label:Cl[C](Cl)CCOBr smiles:Cl[C](Cl)CCOBr H298:5.62 kcal/mol
library:CHOClBr_G4 label:Cl[C](Cl)COOBr smiles:Cl[C](Cl)COOBr H298:28.18 kcal/mol
library:CHOClBr_G4 label:Cl[C](Cl)C(Cl)(Cl)Br smiles:Cl[C](Cl)C(Cl)(Cl)Br H298:13.98 kcal/mol
library:CHOClBr_G4 label:CCC(Br)[C](Cl)Cl smiles:CCC(Br)[C](Cl)Cl H298:0.56 kcal/mol
library:CHOClBr_G4 label:Cl[C](Cl)CCBr smiles:Cl[C](Cl)CCBr H298:10.01 kcal/mol
library:CHOClBr_G4 label:Cl[C](Cl)CC(Br)Br smiles:Cl[C](Cl)CC(Br)Br H298:16.90 kcal/mol
library:CHOClBr_G4 label:OC(Cl)(Br)[C](Cl)Cl smiles:OC(Cl)(Br)[C](Cl)Cl H298:-26.64 kcal/mol
library:CHOClBr_G4 label:OCC(Br)[C](Cl)Cl smiles:OCC(Br)[C](Cl)Cl H298:-29.41 kcal/mol
library:CHOClBr_G4 label:Cl[C](Cl)COBr smiles:Cl[C](Cl)COBr H298:12.38 kcal/mol
library:CHOClBr_G4 label:COC(Br)[C](Cl)Cl smiles:COC(Br)[C](Cl)Cl H298:-19.13 kcal/mol
library:CHOClBr_G4 label:OC(Br)(Br)[C](Cl)Cl smiles:OC(Br)(Br)[C](Cl)Cl H298:-14.66 kcal/mol
library:CHOClBr_G4 label:Cl[C](Cl)COCBr smiles:Cl[C](Cl)COCBr H298:-18.03 kcal/mol
library:CHOClBr_G4 label:Cl[C](Cl)CCCBr smiles:Cl[C](Cl)CCCBr H298:3.62 kcal/mol
library:CHOClBr_G4 label:CC(C)(Br)[C](Cl)Cl smiles:CC(C)(Br)[C](Cl)Cl H298:-2.10 kcal/mol
library:CHOClBr_G4 label:Cl[C](Cl)C(Cl)Br smiles:Cl[C](Cl)C(Cl)Br H298:13.77 kcal/mol
library:CHOClBr_G4 label:OC(CBr)[C](Cl)Cl smiles:OC(CBr)[C](Cl)Cl H298:-28.09 kcal/mol
library:CHOClBr_G4 label:Cl[C](Cl)C(Cl)OBr smiles:Cl[C](Cl)C(Cl)OBr H298:5.40 kcal/mol
library:CHOClBr_G4 label:Cl[C](Cl)C(Br)(Br)Br smiles:Cl[C](Cl)C(Br)(Br)Br H298:37.30 kcal/mol
library:CHOClBr_G4 label:Cl[C](Cl)C(Br)OBr smiles:Cl[C](Cl)C(Br)OBr H298:16.40 kcal/mol
library:CHOClBr_G4 label:CC(Br)[C](Cl)Cl smiles:CC(Br)[C](Cl)Cl H298:6.71 kcal/mol
library:CHOClBr_G4 label:Cl[C](Cl)C(Br)Br smiles:Cl[C](Cl)C(Br)Br H298:24.89 kcal/mol
library:CHOClBr_G4 label:OC(Br)C[C](Cl)Cl smiles:OC(Br)C[C](Cl)Cl H298:-30.22 kcal/mol
library:CHOClBr_G4 label:CC(Br)(Br)[C](Cl)Cl smiles:CC(Br)(Br)[C](Cl)Cl H298:15.23 kcal/mol
library:CHOClBr_G4 label:CC(OBr)[C](Cl)Cl smiles:CC(OBr)[C](Cl)Cl H298:1.29 kcal/mol
library:CHOClBr_G4 label:Cl[C](Cl)CBr smiles:Cl[C](Cl)CBr H298:15.56 kcal/mol
""",
)

entry(
    index = 76,
    label = "CsBr1sCsF1s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cs   u0 {1,S}
3   F1s  u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.432718,-1.42741,-2.23202,-2.8819,-3.76889,-4.29275,-4.92154],'cal/(mol*K)','+|-',[0.119864,0.12307,0.115393,0.10778,0.0951178,0.0832352,0.0609632]),
        H298 = (96.6802,'kcal/mol','+|-',0.191482),
        S298 = (4.587,'cal/(mol*K)','+|-',0.325415),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFBr_G4 label:CC(Br)C(Br)[C](F)Br smiles:CC(Br)C(Br)[C](F)Br H298:-19.63 kcal/mol
library:CHOFBr_G4 label:CDCC[C](F)Br smiles:C=CC[C](F)Br H298:4.49 kcal/mol
library:CHOFBr_G4 label:F[C](Br)CC(Br)CBr smiles:F[C](Br)CC(Br)CBr H298:-18.57 kcal/mol
library:CHOFBr_G4 label:CCC(Br)[C](F)Br smiles:CCC(Br)[C](F)Br H298:-24.37 kcal/mol
library:CHOFBr_G4 label:CC(O)[C](F)Br smiles:CC(O)[C](F)Br H298:-59.96 kcal/mol
library:CHOFBr_G4 label:F[C](Br)CCOBr smiles:F[C](Br)CCOBr H298:-19.71 kcal/mol
library:CHOFBr_G4 label:OC(CBr)[C](F)Br smiles:OC(CBr)[C](F)Br H298:-53.08 kcal/mol
library:CHOFBr_G4 label:F[C](Br)COOBr smiles:F[C](Br)COOBr H298:3.61 kcal/mol
library:CHOFBr_G4 label:OOC[C](F)Br smiles:OOC[C](F)Br H298:-30.64 kcal/mol
library:CHOFBr_G4 label:F[C](Br)CC(Br)(Br)Br smiles:F[C](Br)CC(Br)(Br)Br H298:2.88 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)[C](F)Br smiles:O=CC(Br)[C](F)Br H298:-30.78 kcal/mol
library:CHOFBr_G4 label:OC[C](F)Br smiles:OC[C](F)Br H298:-49.57 kcal/mol
library:CHOFBr_G4 label:C#CC(F)(F)[C](F)Br smiles:C#CC(F)(F)[C](F)Br H298:-43.48 kcal/mol
library:CHOFBr_G4 label:CC(Br)(Br)[C](F)Br smiles:CC(Br)(Br)[C](F)Br H298:-10.13 kcal/mol
library:CHOFBr_G4 label:COC(Br)(Br)[C](F)Br smiles:COC(Br)(Br)[C](F)Br H298:-37.65 kcal/mol
library:CHOFBr_G4 label:F[C](Br)C(CBr)CBr smiles:F[C](Br)C(CBr)CBr H298:-17.59 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(Br)[C](F)Br smiles:OC(Br)C(Br)[C](F)Br H298:-49.56 kcal/mol
library:CHOFBr_G4 label:CC(C)(Br)[C](F)Br smiles:CC(C)(Br)[C](F)Br H298:-27.12 kcal/mol
library:CHOFBr_G4 label:F[C](Br)CCC(Br)Br smiles:F[C](Br)CCC(Br)Br H298:-15.87 kcal/mol
library:CHOFBr_G4 label:CC(C)[C](F)Br smiles:CC(C)[C](F)Br H298:-28.74 kcal/mol
library:CHOFBr_G4 label:OC(OBr)[C](F)Br smiles:OC(OBr)[C](F)Br H298:-57.56 kcal/mol
library:CHOFBr_G4 label:FC#CC(F)[C](F)Br smiles:FC#CC(F)[C](F)Br H298:-23.17 kcal/mol
library:CHOFBr_G4 label:ODCC[C](F)Br smiles:O=CC[C](F)Br H298:-38.15 kcal/mol
library:CHOFBr_G4 label:OC(Br)[C](F)Br smiles:OC(Br)[C](F)Br H298:-47.88 kcal/mol
library:CHOFBr_G4 label:F[C](Br)C(Br)OBr smiles:F[C](Br)C(Br)OBr H298:-7.73 kcal/mol
library:CHOFBr_G4 label:F[C](Br)C(Br)Br smiles:F[C](Br)C(Br)Br H298:0.25 kcal/mol
library:CHOFBr_G4 label:CC[C](F)Br smiles:CC[C](F)Br H298:-21.30 kcal/mol
library:CHOFBr_G4 label:F[C](Br)C(Br)(Br)OBr smiles:F[C](Br)C(Br)(Br)OBr H298:-0.09 kcal/mol
library:CHOFBr_G4 label:OC(Br)C[C](F)Br smiles:OC(Br)C[C](F)Br H298:-55.31 kcal/mol
library:CHOFBr_G4 label:OCC[C](F)Br smiles:OCC[C](F)Br H298:-56.83 kcal/mol
library:CHOFBr_G4 label:OOC(Br)(Br)[C](F)Br smiles:OOC(Br)(Br)[C](F)Br H298:-19.06 kcal/mol
library:CHOFBr_G4 label:C[C](F)Br smiles:C[C](F)Br H298:-15.87 kcal/mol
library:CHOFBr_G4 label:CC(Br)(Br)C[C](F)Br smiles:CC(Br)(Br)C[C](F)Br H298:-17.69 kcal/mol
library:CHOFBr_G4 label:CC(Br)C[C](F)Br smiles:CC(Br)C[C](F)Br H298:-23.79 kcal/mol
library:CHOFBr_G4 label:C#CC[C](F)Br smiles:C#CC[C](F)Br H298:46.74 kcal/mol
library:CHOFBr_G4 label:COC[C](F)Br smiles:COC[C](F)Br H298:-45.21 kcal/mol
library:CHOFBr_G4 label:OC([C](F)Br)C(Br)Br smiles:OC([C](F)Br)C(Br)Br H298:-45.64 kcal/mol
library:CHOFBr_G4 label:F[C](Br)C(Br)(Br)CBr smiles:F[C](Br)C(Br)(Br)CBr H298:-2.77 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)(Br)[C](F)Br smiles:O=CC(Br)(Br)[C](F)Br H298:-22.18 kcal/mol
library:CHOFBr_G4 label:F[C](Br)C(Br)OCBr smiles:F[C](Br)C(Br)OCBr H298:-40.65 kcal/mol
library:CHOFBr_G4 label:F[C](Br)C(Br)CBr smiles:F[C](Br)C(Br)CBr H298:-12.14 kcal/mol
library:CHOFBr_G4 label:OCC(Br)(Br)[C](F)Br smiles:OCC(Br)(Br)[C](F)Br H298:-46.42 kcal/mol
library:CHOFBr_G4 label:CC(Br)[C](F)Br smiles:CC(Br)[C](F)Br H298:-18.27 kcal/mol
library:CHOFBr_G4 label:CC(Br)(OBr)[C](F)Br smiles:CC(Br)(OBr)[C](F)Br H298:-18.61 kcal/mol
library:CHOFBr_G4 label:C#CC(F)[C](F)Br smiles:C#CC(F)[C](F)Br H298:6.28 kcal/mol
library:CHOFBr_G4 label:CC(OBr)[C](F)Br smiles:CC(OBr)[C](F)Br H298:-22.62 kcal/mol
library:CHOFBr_G4 label:OC(O)[C](F)Br smiles:OC(O)[C](F)Br H298:-94.98 kcal/mol
library:CHOFBr_G4 label:FC#CC[C](F)Br smiles:FC#CC[C](F)Br H298:18.31 kcal/mol
library:CHOFBr_G4 label:CC(O)(Br)[C](F)Br smiles:CC(O)(Br)[C](F)Br H298:-59.04 kcal/mol
library:CHOFBr_G4 label:F[C](Br)CCBr smiles:F[C](Br)CCBr H298:-15.41 kcal/mol
library:CHOFBr_G4 label:F[C](Br)C(CBr)OBr smiles:F[C](Br)C(CBr)OBr H298:-15.91 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)C[C](F)Br smiles:OC(Br)(Br)C[C](F)Br H298:-49.63 kcal/mol
library:CHOFBr_G4 label:CC([C](F)Br)C(Br)Br smiles:CC([C](F)Br)C(Br)Br H298:-15.92 kcal/mol
library:CHOFBr_G4 label:F[C](Br)CC(Br)Br smiles:F[C](Br)CC(Br)Br H298:-8.15 kcal/mol
library:CHOFBr_G4 label:CCC(Br)(Br)[C](F)Br smiles:CCC(Br)(Br)[C](F)Br H298:-16.37 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)[C](F)Br smiles:OC(Br)(Br)[C](F)Br H298:-39.82 kcal/mol
library:CHOFBr_G4 label:F[C](Br)C(Br)C(Br)Br smiles:F[C](Br)C(Br)C(Br)Br H298:-2.55 kcal/mol
library:CHOFBr_G4 label:CCC[C](F)Br smiles:CCC[C](F)Br H298:-26.64 kcal/mol
library:CHOFBr_G4 label:F[C](Br)C(Br)(Br)Br smiles:F[C](Br)C(Br)(Br)Br H298:12.26 kcal/mol
library:CHOFBr_G4 label:OC(Br)(OBr)[C](F)Br smiles:OC(Br)(OBr)[C](F)Br H298:-52.94 kcal/mol
library:CHOFBr_G4 label:F[C](Br)CBr smiles:F[C](Br)CBr H298:-9.38 kcal/mol
library:CHOFBr_G4 label:F[C](Br)COCBr smiles:F[C](Br)COCBr H298:-45.07 kcal/mol
library:CHOFBr_G4 label:F[C](Br)CCCBr smiles:F[C](Br)CCCBr H298:-22.03 kcal/mol
library:CHOFBr_G4 label:F[C](Br)C(OBr)OBr smiles:F[C](Br)C(OBr)OBr H298:-17.75 kcal/mol
library:CHOFBr_G4 label:OCC(Br)[C](F)Br smiles:OCC(Br)[C](F)Br H298:-53.89 kcal/mol
library:CHOFBr_G4 label:F[C](Br)CC(Br)OBr smiles:F[C](Br)CC(Br)OBr H298:-17.41 kcal/mol
library:CHOFBr_G4 label:F[C](Br)COC(Br)Br smiles:F[C](Br)COC(Br)Br H298:-37.08 kcal/mol
library:CHOFBr_G4 label:CC(CBr)[C](F)Br smiles:CC(CBr)[C](F)Br H298:-22.98 kcal/mol
""",
)

entry(
    index = 77,
    label = "CsCl1sCsF1s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cs   u0 {1,S}
3   F1s  u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.232562,-1.19868,-1.97511,-2.58465,-3.46656,-4.05647,-4.82175],'cal/(mol*K)','+|-',[0.110509,0.113465,0.106387,0.099368,0.0876943,0.076739,0.0562053]),
        H298 = (96.6428,'kcal/mol','+|-',0.176537),
        S298 = (3.97979,'cal/(mol*K)','+|-',0.300018),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFCl_G4 label:ODCC(Cl)[C](F)Cl smiles:O=CC(Cl)[C](F)Cl H298:-54.70 kcal/mol
library:CHOFCl_G4 label:F[C](Cl)C(Cl)(Cl)Cl smiles:F[C](Cl)C(Cl)(Cl)Cl H298:-34.80 kcal/mol
library:CHOFCl_G4 label:CCC[C](F)Cl smiles:CCC[C](F)Cl H298:-39.40 kcal/mol
library:CHOFCl_G4 label:OC(Cl)C[C](F)Cl smiles:OC(Cl)C[C](F)Cl H298:-80.24 kcal/mol
library:CHOFCl_G4 label:CCC(Cl)[C](F)Cl smiles:CCC(Cl)[C](F)Cl H298:-47.23 kcal/mol
library:CHOFCl_G4 label:OC(CCl)[C](F)Cl smiles:OC(CCl)[C](F)Cl H298:-76.74 kcal/mol
library:CHOFCl_G4 label:F[C](Cl)CCCl smiles:F[C](Cl)CCCl H298:-39.18 kcal/mol
library:CHOFCl_G4 label:F[C](Cl)C(Cl)OCl smiles:F[C](Cl)C(Cl)OCl H298:-34.03 kcal/mol
library:CHOFCl_G4 label:FC#CC[C](F)Cl smiles:FC#CC[C](F)Cl H298:5.49 kcal/mol
library:CHOFCl_G4 label:OC(O)[C](F)Cl smiles:OC(O)[C](F)Cl H298:-107.54 kcal/mol
library:CHOFCl_G4 label:C#CC(F)[C](F)Cl smiles:C#CC(F)[C](F)Cl H298:-7.11 kcal/mol
library:CHOFCl_G4 label:OC(OCl)[C](F)Cl smiles:OC(OCl)[C](F)Cl H298:-72.95 kcal/mol
library:CHOFCl_G4 label:F[C](Cl)C(Cl)Cl smiles:F[C](Cl)C(Cl)Cl H298:-34.03 kcal/mol
library:CHOFCl_G4 label:CC(C)(Cl)[C](F)Cl smiles:CC(C)(Cl)[C](F)Cl H298:-50.89 kcal/mol
library:CHOFCl_G4 label:F[C](Cl)CCl smiles:F[C](Cl)CCl H298:-32.37 kcal/mol
library:CHOFCl_G4 label:CC(Cl)(Cl)[C](F)Cl smiles:CC(Cl)(Cl)[C](F)Cl H298:-44.87 kcal/mol
library:CHOFCl_G4 label:OC(Cl)[C](F)Cl smiles:OC(Cl)[C](F)Cl H298:-71.84 kcal/mol
library:CHOFCl_G4 label:COC[C](F)Cl smiles:COC[C](F)Cl H298:-57.93 kcal/mol
library:CHOFCl_G4 label:F[C](Cl)CCOCl smiles:F[C](Cl)CCOCl H298:-36.06 kcal/mol
library:CHOFCl_G4 label:C#CC[C](F)Cl smiles:C#CC[C](F)Cl H298:33.91 kcal/mol
library:CHOFCl_G4 label:F[C](Cl)COOCl smiles:F[C](Cl)COOCl H298:-12.59 kcal/mol
library:CHOFCl_G4 label:C[C](F)Cl smiles:C[C](F)Cl H298:-28.87 kcal/mol
library:CHOFCl_G4 label:CC(OCl)[C](F)Cl smiles:CC(OCl)[C](F)Cl H298:-38.44 kcal/mol
library:CHOFCl_G4 label:OC(Cl)(Cl)[C](F)Cl smiles:OC(Cl)(Cl)[C](F)Cl H298:-75.91 kcal/mol
library:CHOFCl_G4 label:F[C](Cl)COCCl smiles:F[C](Cl)COCCl H298:-67.39 kcal/mol
library:CHOFCl_G4 label:OCC[C](F)Cl smiles:OCC[C](F)Cl H298:-69.51 kcal/mol
library:CHOFCl_G4 label:CC(Cl)[C](F)Cl smiles:CC(Cl)[C](F)Cl H298:-41.36 kcal/mol
library:CHOFCl_G4 label:F[C](Cl)CCCCl smiles:F[C](Cl)CCCCl H298:-45.70 kcal/mol
library:CHOFCl_G4 label:CC(O)(Cl)[C](F)Cl smiles:CC(O)(Cl)[C](F)Cl H298:-83.50 kcal/mol
library:CHOFCl_G4 label:CC[C](F)Cl smiles:CC[C](F)Cl H298:-35.60 kcal/mol
library:CHOFCl_G4 label:F[C](Cl)CC(Cl)Cl smiles:F[C](Cl)CC(Cl)Cl H298:-43.77 kcal/mol
library:CHOFCl_G4 label:ODCC[C](F)Cl smiles:O=CC[C](F)Cl H298:-50.66 kcal/mol
library:CHOFCl_G4 label:CC(C)[C](F)Cl smiles:CC(C)[C](F)Cl H298:-41.31 kcal/mol
library:CHOFCl_G4 label:OCC(Cl)[C](F)Cl smiles:OCC(Cl)[C](F)Cl H298:-77.02 kcal/mol
library:CHOFCl_G4 label:CC(Cl)C[C](F)Cl smiles:CC(Cl)C[C](F)Cl H298:-47.77 kcal/mol
library:CHOFCl_G4 label:F[C](Cl)C(Cl)CCl smiles:F[C](Cl)C(Cl)CCl H298:-45.69 kcal/mol
library:CHOFCl_G4 label:F[C](Cl)COCl smiles:F[C](Cl)COCl H298:-28.03 kcal/mol
library:CHOFCl_G4 label:OC[C](F)Cl smiles:OC[C](F)Cl H298:-62.34 kcal/mol
library:CHOFCl_G4 label:CC(CCl)[C](F)Cl smiles:CC(CCl)[C](F)Cl H298:-46.76 kcal/mol
library:CHOFCl_G4 label:COC(Cl)[C](F)Cl smiles:COC(Cl)[C](F)Cl H298:-67.02 kcal/mol
library:CHOFCl_G4 label:OOC[C](F)Cl smiles:OOC[C](F)Cl H298:-43.53 kcal/mol
library:CHOFCl_G4 label:OC(O)(Cl)[C](F)Cl smiles:OC(O)(Cl)[C](F)Cl H298:-117.06 kcal/mol
library:CHOFCl_G4 label:ODC(Cl)C[C](F)Cl smiles:O=C(Cl)C[C](F)Cl H298:-67.63 kcal/mol
library:CHOFCl_G4 label:CC(O)[C](F)Cl smiles:CC(O)[C](F)Cl H298:-72.08 kcal/mol
library:CHOFCl_G4 label:CDCC[C](F)Cl smiles:C=CC[C](F)Cl H298:-8.32 kcal/mol
library:CHOFClBr_G4 label:CC(CBr)[C](F)Cl smiles:CC(CBr)[C](F)Cl H298:-35.80 kcal/mol
library:CHOFClBr_G4 label:F[C](Cl)CC(Br)Br smiles:F[C](Cl)CC(Br)Br H298:-20.62 kcal/mol
library:CHOFClBr_G4 label:OCC(Br)[C](F)Cl smiles:OCC(Br)[C](F)Cl H298:-66.23 kcal/mol
library:CHOFClBr_G4 label:OC(Br)(Br)[C](F)Cl smiles:OC(Br)(Br)[C](F)Cl H298:-52.13 kcal/mol
library:CHOFClBr_G4 label:F[C](Cl)C(Br)(Br)Br smiles:F[C](Cl)C(Br)(Br)Br H298:-0.14 kcal/mol
library:CHOFClBr_G4 label:F[C](Cl)COBr smiles:F[C](Cl)COBr H298:-24.86 kcal/mol
library:CHOFClBr_G4 label:F[C](Cl)C(Cl)CBr smiles:F[C](Cl)C(Cl)CBr H298:-35.13 kcal/mol
library:CHOFClBr_G4 label:CC(O)(Br)[C](F)Cl smiles:CC(O)(Br)[C](F)Cl H298:-71.11 kcal/mol
library:CHOFClBr_G4 label:F[C](Cl)C(Br)CBr smiles:F[C](Cl)C(Br)CBr H298:-24.47 kcal/mol
library:CHOFClBr_G4 label:ODC(Br)C[C](F)Cl smiles:O=C(Br)C[C](F)Cl H298:-55.28 kcal/mol
library:CHOFClBr_G4 label:CC(OBr)[C](F)Cl smiles:CC(OBr)[C](F)Cl H298:-35.51 kcal/mol
library:CHOFClBr_G4 label:OC(Cl)(Br)[C](F)Cl smiles:OC(Cl)(Br)[C](F)Cl H298:-64.15 kcal/mol
library:CHOFClBr_G4 label:CC(Br)[C](F)Cl smiles:CC(Br)[C](F)Cl H298:-30.81 kcal/mol
library:CHOFClBr_G4 label:F[C](Cl)CC(Cl)Br smiles:F[C](Cl)CC(Cl)Br H298:-32.15 kcal/mol
library:CHOFClBr_G4 label:F[C](Cl)CCCBr smiles:F[C](Cl)CCCBr H298:-34.71 kcal/mol
library:CHOFClBr_G4 label:F[C](Cl)COCBr smiles:F[C](Cl)COCBr H298:-60.76 kcal/mol
library:CHOFClBr_G4 label:CC(Br)C[C](F)Cl smiles:CC(Br)C[C](F)Cl H298:-36.55 kcal/mol
library:CHOFClBr_G4 label:F[C](Cl)COOBr smiles:F[C](Cl)COOBr H298:-9.12 kcal/mol
library:CHOFClBr_G4 label:F[C](Cl)CCOBr smiles:F[C](Cl)CCOBr H298:-32.55 kcal/mol
library:CHOFClBr_G4 label:OC(Br)C[C](F)Cl smiles:OC(Br)C[C](F)Cl H298:-67.67 kcal/mol
library:CHOFClBr_G4 label:F[C](Cl)CBr smiles:F[C](Cl)CBr H298:-22.11 kcal/mol
library:CHOFClBr_G4 label:F[C](Cl)C(Cl)Br smiles:F[C](Cl)C(Cl)Br H298:-23.39 kcal/mol
library:CHOFClBr_G4 label:F[C](Cl)C(Cl)(Br)Br smiles:F[C](Cl)C(Cl)(Br)Br H298:-11.92 kcal/mol
library:CHOFClBr_G4 label:OC(Br)[C](F)Cl smiles:OC(Br)[C](F)Cl H298:-60.23 kcal/mol
library:CHOFClBr_G4 label:OC(OBr)[C](F)Cl smiles:OC(OBr)[C](F)Cl H298:-68.72 kcal/mol
library:CHOFClBr_G4 label:F[C](Cl)C(Br)OBr smiles:F[C](Cl)C(Br)OBr H298:-20.15 kcal/mol
library:CHOFClBr_G4 label:CC(C)(Br)[C](F)Cl smiles:CC(C)(Br)[C](F)Cl H298:-39.30 kcal/mol
library:CHOFClBr_G4 label:CC(Cl)(Br)[C](F)Cl smiles:CC(Cl)(Br)[C](F)Cl H298:-33.98 kcal/mol
library:CHOFClBr_G4 label:CC(Br)(Br)[C](F)Cl smiles:CC(Br)(Br)[C](F)Cl H298:-22.56 kcal/mol
library:CHOFClBr_G4 label:F[C](Cl)C(Cl)OBr smiles:F[C](Cl)C(Cl)OBr H298:-31.41 kcal/mol
library:CHOFClBr_G4 label:F[C](Cl)CCBr smiles:F[C](Cl)CCBr H298:-27.98 kcal/mol
library:CHOFClBr_G4 label:OC(CBr)[C](F)Cl smiles:OC(CBr)[C](F)Cl H298:-65.87 kcal/mol
library:CHOFClBr_G4 label:CCC(Br)[C](F)Cl smiles:CCC(Br)[C](F)Cl H298:-36.81 kcal/mol
library:CHOFClBr_G4 label:F[C](Cl)C(Cl)(Cl)Br smiles:F[C](Cl)C(Cl)(Cl)Br H298:-23.53 kcal/mol
library:CHOFClBr_G4 label:F[C](Cl)C(Br)Br smiles:F[C](Cl)C(Br)Br H298:-12.17 kcal/mol
""",
)

entry(
    index = 78,
    label = "CsCsF1sF1s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   F1s u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.318184,-1.16131,-1.85832,-2.41649,-3.26427,-3.87628,-4.79145],'cal/(mol*K)','+|-',[0.05669,0.0582061,0.0545754,0.0509747,0.0449862,0.0393663,0.0288327]),
        H298 = (100.526,'kcal/mol','+|-',0.0905617),
        S298 = (2.83935,'cal/(mol*K)','+|-',0.153906),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:F[C](F)C(F)(F)C(F)(F)C(F)(F)F smiles:F[C](F)C(F)(F)C(F)(F)C(F)(F)F H298:-416.31 kcal/mol
library:CHOF_G4 label:CDCC(F)[C](F)F smiles:C=CC(F)[C](F)F H298:-93.79 kcal/mol
library:CHOF_G4 label:F[C](F)C(F)(F)CDC(F)F smiles:F[C](F)C(F)(F)C=C(F)F H298:-237.07 kcal/mol
library:CHOF_G4 label:OC(O)[C](F)F smiles:OC(O)[C](F)F H298:-149.12 kcal/mol
library:CHOF_G4 label:CC[C](F)F smiles:CC[C](F)F H298:-76.88 kcal/mol
library:CHOF_G4 label:FCC(F)C(F)(F)[C](F)F smiles:FCC(F)C(F)(F)[C](F)F H298:-262.89 kcal/mol
library:CHOF_G4 label:FCC(F)(F)[C](F)F smiles:FCC(F)(F)[C](F)F H298:-212.09 kcal/mol
library:CHOF_G4 label:FOC([C](F)F)C(F)(F)F smiles:FOC([C](F)F)C(F)(F)F H298:-230.19 kcal/mol
library:CHOF_G4 label:CDCC(F)(F)[C](F)F smiles:C=CC(F)(F)[C](F)F H298:-145.89 kcal/mol
library:CHOF_G4 label:F[C](F)CC(F)(F)C(F)F smiles:F[C](F)CC(F)(F)C(F)F H298:-275.94 kcal/mol
library:CHOF_G4 label:F[C](F)CCC(F)(F)F smiles:F[C](F)CCC(F)(F)F H298:-240.86 kcal/mol
library:CHOF_G4 label:F[C](F)COC(F)F smiles:F[C](F)COC(F)F H298:-209.38 kcal/mol
library:CHOF_G4 label:FOCC[C](F)F smiles:FOCC[C](F)F H298:-84.16 kcal/mol
library:CHOF_G4 label:F[C](F)C(F)(F)F smiles:F[C](F)C(F)(F)F H298:-216.37 kcal/mol
library:CHOF_G4 label:OC(F)[C](F)F smiles:OC(F)[C](F)F H298:-155.98 kcal/mol
library:CHOF_G4 label:FCDCC[C](F)F smiles:FC=CC[C](F)F H298:-96.76 kcal/mol
library:CHOF_G4 label:OC(F)(F)C[C](F)F smiles:OC(F)(F)C[C](F)F H298:-226.05 kcal/mol
library:CHOF_G4 label:CCC[C](F)F smiles:CCC[C](F)F H298:-82.00 kcal/mol
library:CHOF_G4 label:FCC(F)(CF)[C](F)F smiles:FCC(F)(CF)[C](F)F H298:-212.69 kcal/mol
library:CHOF_G4 label:OC(F)(F)[C](F)F smiles:OC(F)(F)[C](F)F H298:-211.75 kcal/mol
library:CHOF_G4 label:CC(F)(F)C(F)[C](F)F smiles:CC(F)(F)C(F)[C](F)F H298:-226.23 kcal/mol
library:CHOF_G4 label:FCC(F)([C](F)F)C(F)F smiles:FCC(F)([C](F)F)C(F)F H298:-263.28 kcal/mol
library:CHOF_G4 label:OC(OF)[C](F)F smiles:OC(OF)[C](F)F H298:-116.40 kcal/mol
library:CHOF_G4 label:OC[C](F)F smiles:OC[C](F)F H298:-104.59 kcal/mol
library:CHOF_G4 label:F[C](F)C(F)(F)C(F)C(F)(F)F smiles:F[C](F)C(F)(F)C(F)C(F)(F)F H298:-368.44 kcal/mol
library:CHOF_G4 label:FOOC(F)[C](F)F smiles:FOOC(F)[C](F)F H298:-110.18 kcal/mol
library:CHOF_G4 label:F[C](F)C(F)(C(F)(F)F)C(F)(F)F smiles:F[C](F)C(F)(C(F)(F)F)C(F)(F)F H298:-422.76 kcal/mol
library:CHOF_G4 label:F[C](F)C(F)CC(F)F smiles:F[C](F)C(F)CC(F)F H298:-224.53 kcal/mol
library:CHOF_G4 label:FC#CC[C](F)F smiles:FC#CC[C](F)F H298:-37.07 kcal/mol
library:CHOF_G4 label:OC(O)(F)[C](F)F smiles:OC(O)(F)[C](F)F H298:-206.58 kcal/mol
library:CHOF_G4 label:FOC(F)[C](F)F smiles:FOC(F)[C](F)F H298:-120.83 kcal/mol
library:CHOF_G4 label:F[C](F)CC(F)(F)C(F)(F)F smiles:F[C](F)CC(F)(F)C(F)(F)F H298:-331.74 kcal/mol
library:CHOF_G4 label:FOC(F)C[C](F)F smiles:FOC(F)C[C](F)F H298:-135.64 kcal/mol
library:CHOF_G4 label:F[C](F)C(F)C(F)DC(F)F smiles:F[C](F)C(F)C(F)=C(F)F H298:-223.46 kcal/mol
library:CHOF_G4 label:FC[C](F)F smiles:FC[C](F)F H298:-110.75 kcal/mol
library:CHOF_G4 label:FCC(F)(F)C[C](F)F smiles:FCC(F)(F)C[C](F)F H298:-225.52 kcal/mol
library:CHOF_G4 label:F[C](F)C(F)(F)C(F)C(F)F smiles:F[C](F)C(F)(F)C(F)C(F)F H298:-313.21 kcal/mol
library:CHOF_G4 label:OC(F)(CF)[C](F)F smiles:OC(F)(CF)[C](F)F H298:-208.19 kcal/mol
library:CHOF_G4 label:FOOC[C](F)F smiles:FOOC[C](F)F H298:-64.33 kcal/mol
library:CHOF_G4 label:F[C](F)COC(F)(F)F smiles:F[C](F)COC(F)(F)F H298:-265.66 kcal/mol
library:CHOF_G4 label:F[C](F)C(F)F smiles:F[C](F)C(F)F H298:-160.11 kcal/mol
library:CHOF_G4 label:COC[C](F)F smiles:COC[C](F)F H298:-99.55 kcal/mol
library:CHOF_G4 label:F[C](F)C(F)(F)OC(F)F smiles:F[C](F)C(F)(F)OC(F)F H298:-308.96 kcal/mol
library:CHOF_G4 label:OCC(F)[C](F)F smiles:OCC(F)[C](F)F H298:-155.24 kcal/mol
library:CHOF_G4 label:F[C](F)C(F)C(F)F smiles:F[C](F)C(F)C(F)F H298:-213.10 kcal/mol
library:CHOF_G4 label:FC#CC(F)(F)[C](F)F smiles:FC#CC(F)(F)[C](F)F H298:-126.43 kcal/mol
library:CHOF_G4 label:FC#CC(F)[C](F)F smiles:FC#CC(F)[C](F)F H298:-76.98 kcal/mol
library:CHOF_G4 label:FCCC[C](F)F smiles:FCCC[C](F)F H298:-126.46 kcal/mol
library:CHOF_G4 label:FOC(F)C(F)(F)[C](F)F smiles:FOC(F)C(F)(F)[C](F)F H298:-222.07 kcal/mol
library:CHOF_G4 label:OC(F)C(F)[C](F)F smiles:OC(F)C(F)[C](F)F H298:-207.77 kcal/mol
library:CHOF_G4 label:F[C](F)C(F)C(F)C(F)(F)F smiles:F[C](F)C(F)C(F)C(F)(F)F H298:-320.93 kcal/mol
library:CHOF_G4 label:CCC(F)(F)[C](F)F smiles:CCC(F)(F)[C](F)F H298:-179.21 kcal/mol
library:CHOF_G4 label:CC(F)[C](F)F smiles:CC(F)[C](F)F H298:-121.07 kcal/mol
library:CHOF_G4 label:F[C](F)C(F)C(F)(F)C(F)(F)F smiles:F[C](F)C(F)C(F)(F)C(F)(F)F H298:-368.54 kcal/mol
library:CHOF_G4 label:OOC(F)(F)[C](F)F smiles:OOC(F)(F)[C](F)F H298:-187.75 kcal/mol
library:CHOF_G4 label:OC(CF)[C](F)F smiles:OC(CF)[C](F)F H298:-156.48 kcal/mol
library:CHOF_G4 label:F[C](F)C(F)(F)CC(F)F smiles:F[C](F)C(F)(F)CC(F)F H298:-274.67 kcal/mol
library:CHOF_G4 label:FCC([C](F)F)C(F)(F)F smiles:FCC([C](F)F)C(F)(F)F H298:-279.14 kcal/mol
library:CHOF_G4 label:FCC(F)(OF)[C](F)F smiles:FCC(F)(OF)[C](F)F H298:-172.01 kcal/mol
library:CHOF_G4 label:OCC[C](F)F smiles:OCC[C](F)F H298:-111.70 kcal/mol
library:CHOF_G4 label:F[C](F)C(F)OC(F)F smiles:F[C](F)C(F)OC(F)F H298:-256.91 kcal/mol
library:CHOF_G4 label:FOC(OF)[C](F)F smiles:FOC(OF)[C](F)F H298:-82.33 kcal/mol
library:CHOF_G4 label:CC(O)[C](F)F smiles:CC(O)[C](F)F H298:-114.16 kcal/mol
library:CHOF_G4 label:C#CC[C](F)F smiles:C#CC[C](F)F H298:-8.64 kcal/mol
library:CHOF_G4 label:CDC(F)C[C](F)F smiles:C=C(F)C[C](F)F H298:-98.50 kcal/mol
library:CHOF_G4 label:OC(F)(F)C(F)[C](F)F smiles:OC(F)(F)C(F)[C](F)F H298:-264.74 kcal/mol
library:CHOF_G4 label:FOC(F)([C](F)F)C(F)F smiles:FOC(F)([C](F)F)C(F)F H298:-220.22 kcal/mol
library:CHOF_G4 label:F[C](F)C(F)OC(F)(F)F smiles:F[C](F)C(F)OC(F)(F)F H298:-313.50 kcal/mol
library:CHOF_G4 label:CC([C](F)F)C(F)F smiles:CC([C](F)F)C(F)F H298:-180.49 kcal/mol
library:CHOF_G4 label:OC(F)C[C](F)F smiles:OC(F)C[C](F)F H298:-167.81 kcal/mol
library:CHOF_G4 label:FCOC(F)(F)[C](F)F smiles:FCOC(F)(F)[C](F)F H298:-254.45 kcal/mol
library:CHOF_G4 label:FCOC[C](F)F smiles:FCOC[C](F)F H298:-151.66 kcal/mol
library:CHOF_G4 label:F[C](F)CCC(F)F smiles:F[C](F)CCC(F)F H298:-181.15 kcal/mol
library:CHOF_G4 label:CDCC[C](F)F smiles:C=CC[C](F)F H298:-51.13 kcal/mol
library:CHOF_G4 label:FCC(F)C(F)[C](F)F smiles:FCC(F)C(F)[C](F)F H298:-212.06 kcal/mol
library:CHOF_G4 label:OOC(F)[C](F)F smiles:OOC(F)[C](F)F H298:-134.80 kcal/mol
library:CHOF_G4 label:OOC[C](F)F smiles:OOC[C](F)F H298:-85.06 kcal/mol
library:CHOF_G4 label:F[C](F)C(C(F)(F)F)C(F)(F)F smiles:F[C](F)C(C(F)(F)F)C(F)(F)F H298:-386.18 kcal/mol
library:CHOF_G4 label:F[C](F)C(F)C(F)(F)F smiles:F[C](F)C(F)C(F)(F)F H298:-269.18 kcal/mol
library:CHOF_G4 label:F[C](F)C(F)(C(F)F)C(F)F smiles:F[C](F)C(F)(C(F)F)C(F)F H298:-312.65 kcal/mol
library:CHOF_G4 label:FOCC(F)(F)[C](F)F smiles:FOCC(F)(F)[C](F)F H298:-175.89 kcal/mol
library:CHOF_G4 label:CC(C)[C](F)F smiles:CC(C)[C](F)F H298:-84.04 kcal/mol
library:CHOF_G4 label:FCDC(F)C(F)[C](F)F smiles:FC=C(F)C(F)[C](F)F H298:-178.62 kcal/mol
library:CHOF_G4 label:FOCC(F)[C](F)F smiles:FOCC(F)[C](F)F H298:-126.13 kcal/mol
library:CHOF_G4 label:FOC([C](F)F)C(F)F smiles:FOC([C](F)F)C(F)F H298:-175.30 kcal/mol
library:CHOF_G4 label:F[C](F)C(F)CC(F)(F)F smiles:F[C](F)C(F)CC(F)(F)F H298:-281.92 kcal/mol
library:CHOF_G4 label:F[C](F)CC(F)F smiles:F[C](F)CC(F)F H298:-173.26 kcal/mol
library:CHOF_G4 label:ODCC(F)(F)[C](F)F smiles:O=CC(F)(F)[C](F)F H298:-181.19 kcal/mol
library:CHOF_G4 label:FCC(F)[C](F)F smiles:FCC(F)[C](F)F H298:-161.27 kcal/mol
library:CHOF_G4 label:FOC(F)C(F)[C](F)F smiles:FOC(F)C(F)[C](F)F H298:-175.18 kcal/mol
library:CHOF_G4 label:C[C](F)F smiles:C[C](F)F H298:-71.99 kcal/mol
library:CHOF_G4 label:FCCC(F)(F)[C](F)F smiles:FCCC(F)(F)[C](F)F H298:-221.63 kcal/mol
library:CHOF_G4 label:F[C](F)C(F)CDC(F)F smiles:F[C](F)C(F)C=C(F)F H298:-187.75 kcal/mol
library:CHOF_G4 label:F[C](F)C(F)C(F)C(F)F smiles:F[C](F)C(F)C(F)C(F)F H298:-263.24 kcal/mol
library:CHOF_G4 label:C#CC(F)[C](F)F smiles:C#CC(F)[C](F)F H298:-47.97 kcal/mol
library:CHOF_G4 label:FOOC(F)(F)[C](F)F smiles:FOOC(F)(F)[C](F)F H298:-161.21 kcal/mol
library:CHOF_G4 label:CCC(F)[C](F)F smiles:CCC(F)[C](F)F H298:-126.16 kcal/mol
library:CHOF_G4 label:F[C](F)C(F)(F)C(F)DC(F)F smiles:F[C](F)C(F)(F)C(F)=C(F)F H298:-271.14 kcal/mol
library:CHOF_G4 label:F[C](F)C(F)(F)C(F)F smiles:F[C](F)C(F)(F)C(F)F H298:-261.28 kcal/mol
library:CHOF_G4 label:FCOC(F)[C](F)F smiles:FCOC(F)[C](F)F H298:-201.72 kcal/mol
library:CHOF_G4 label:ODC(F)C(F)[C](F)F smiles:O=C(F)C(F)[C](F)F H298:-194.13 kcal/mol
library:CHOF_G4 label:FCC(F)C[C](F)F smiles:FCC(F)C[C](F)F H298:-172.00 kcal/mol
library:CHOF_G4 label:FCDCC(F)(F)[C](F)F smiles:FC=CC(F)(F)[C](F)F H298:-190.01 kcal/mol
library:CHOF_G4 label:FCC([C](F)F)C(F)F smiles:FCC([C](F)F)C(F)F H298:-221.98 kcal/mol
library:CHOF_G4 label:CC(C)(F)[C](F)F smiles:CC(C)(F)[C](F)F H298:-132.05 kcal/mol
library:CHOF_G4 label:COC(F)(F)[C](F)F smiles:COC(F)(F)[C](F)F H298:-207.64 kcal/mol
library:CHOF_G4 label:OC(F)(F)C(F)(F)[C](F)F smiles:OC(F)(F)C(F)(F)[C](F)F H298:-313.02 kcal/mol
library:CHOF_G4 label:ODC(F)C[C](F)F smiles:O=C(F)C[C](F)F H298:-156.63 kcal/mol
library:CHOF_G4 label:FOC(F)(OF)[C](F)F smiles:FOC(F)(OF)[C](F)F H298:-129.19 kcal/mol
library:CHOF_G4 label:F[C](F)CC(F)DC(F)F smiles:F[C](F)CC(F)=C(F)F H298:-184.35 kcal/mol
library:CHOF_G4 label:CC(OF)[C](F)F smiles:CC(OF)[C](F)F H298:-84.42 kcal/mol
library:CHOF_G4 label:CC(F)C(F)[C](F)F smiles:CC(F)C(F)[C](F)F H298:-171.95 kcal/mol
library:CHOF_G4 label:FOC(F)(F)C(F)(F)[C](F)F smiles:FOC(F)(F)C(F)(F)[C](F)F H298:-272.97 kcal/mol
library:CHOF_G4 label:FOC(F)(F)C(F)[C](F)F smiles:FOC(F)(F)C(F)[C](F)F H298:-225.01 kcal/mol
library:CHOF_G4 label:OC(F)([C](F)F)C(F)F smiles:OC(F)([C](F)F)C(F)F H298:-259.06 kcal/mol
library:CHOF_G4 label:OCC(F)(F)[C](F)F smiles:OCC(F)(F)[C](F)F H298:-206.83 kcal/mol
library:CHOF_G4 label:C#CC(F)(F)[C](F)F smiles:C#CC(F)(F)[C](F)F H298:-97.25 kcal/mol
library:CHOF_G4 label:FCC(F)(F)C(F)(F)[C](F)F smiles:FCC(F)(F)C(F)(F)[C](F)F H298:-312.06 kcal/mol
library:CHOF_G4 label:OC([C](F)F)C(F)F smiles:OC([C](F)F)C(F)F H298:-208.10 kcal/mol
library:CHOF_G4 label:OC(F)C(F)(F)[C](F)F smiles:OC(F)C(F)(F)[C](F)F H298:-258.26 kcal/mol
library:CHOF_G4 label:FCC(CF)[C](F)F smiles:FCC(CF)[C](F)F H298:-169.42 kcal/mol
library:CHOF_G4 label:CC([C](F)F)C(F)(F)F smiles:CC([C](F)F)C(F)(F)F H298:-238.67 kcal/mol
library:CHOF_G4 label:F[C](F)C(F)(C(F)F)C(F)(F)F smiles:F[C](F)C(F)(C(F)F)C(F)(F)F H298:-367.41 kcal/mol
library:CHOF_G4 label:ODC(F)C(F)(F)[C](F)F smiles:O=C(F)C(F)(F)[C](F)F H298:-240.56 kcal/mol
library:CHOF_G4 label:FCDCC(F)[C](F)F smiles:FC=CC(F)[C](F)F H298:-137.99 kcal/mol
library:CHOF_G4 label:F[C](F)C(F)(F)C(F)(F)F smiles:F[C](F)C(F)(F)C(F)(F)F H298:-316.98 kcal/mol
library:CHOF_G4 label:F[C](F)C(F)C(F)(F)C(F)F smiles:F[C](F)C(F)C(F)(F)C(F)F H298:-313.72 kcal/mol
library:CHOF_G4 label:CC(F)(F)C(F)(F)[C](F)F smiles:CC(F)(F)C(F)(F)[C](F)F H298:-275.58 kcal/mol
library:CHOF_G4 label:F[C](F)CC(F)(F)F smiles:F[C](F)CC(F)(F)F H298:-232.99 kcal/mol
library:CHOF_G4 label:FCCC(F)[C](F)F smiles:FCCC(F)[C](F)F H298:-170.73 kcal/mol
library:CHOF_G4 label:ODCC[C](F)F smiles:O=CC[C](F)F H298:-93.49 kcal/mol
library:CHOF_G4 label:F[C](F)C(F)(F)CC(F)(F)F smiles:F[C](F)C(F)(F)CC(F)(F)F H298:-332.08 kcal/mol
library:CHOF_G4 label:CC(O)(F)[C](F)F smiles:CC(O)(F)[C](F)F H298:-169.05 kcal/mol
library:CHOF_G4 label:CDC(F)C(F)(F)[C](F)F smiles:C=C(F)C(F)(F)[C](F)F H298:-188.98 kcal/mol
library:CHOF_G4 label:CC(F)C[C](F)F smiles:CC(F)C[C](F)F H298:-129.45 kcal/mol
library:CHOF_G4 label:FOC(F)(F)C[C](F)F smiles:FOC(F)(F)C[C](F)F H298:-188.11 kcal/mol
library:CHOF_G4 label:F[C](F)C(C(F)F)C(F)F smiles:F[C](F)C(C(F)F)C(F)F H298:-273.48 kcal/mol
library:CHOF_G4 label:FOC[C](F)F smiles:FOC[C](F)F H298:-74.25 kcal/mol
library:CHOF_G4 label:F[C](F)C(F)(F)C(F)(F)C(F)F smiles:F[C](F)C(F)(F)C(F)(F)C(F)F H298:-360.70 kcal/mol
library:CHOF_G4 label:COC(F)[C](F)F smiles:COC(F)[C](F)F H298:-151.34 kcal/mol
library:CHOF_G4 label:CC(F)(CF)[C](F)F smiles:CC(F)(CF)[C](F)F H298:-172.97 kcal/mol
library:CHOF_G4 label:FCDC(F)C[C](F)F smiles:FC=C(F)C[C](F)F H298:-138.76 kcal/mol
library:CHOF_G4 label:FCDC(F)C(F)(F)[C](F)F smiles:FC=C(F)C(F)(F)[C](F)F H298:-228.21 kcal/mol
library:CHOF_G4 label:CDC(F)C(F)[C](F)F smiles:C=C(F)C(F)[C](F)F H298:-138.61 kcal/mol
library:CHOF_G4 label:F[C](F)CCDC(F)F smiles:F[C](F)CC=C(F)F H298:-145.53 kcal/mol
library:CHOF_G4 label:FCC(OF)[C](F)F smiles:FCC(OF)[C](F)F H298:-124.48 kcal/mol
library:CHOF_G4 label:F[C](F)C(F)(F)OC(F)(F)F smiles:F[C](F)C(F)(F)OC(F)(F)F H298:-365.13 kcal/mol
library:CHOF_G4 label:FCC(F)(F)C(F)[C](F)F smiles:FCC(F)(F)C(F)[C](F)F H298:-265.60 kcal/mol
library:CHOF_G4 label:OC(F)([C](F)F)C(F)(F)F smiles:OC(F)([C](F)F)C(F)(F)F H298:-314.17 kcal/mol
library:CHOF_G4 label:CC(F)([C](F)F)C(F)F smiles:CC(F)([C](F)F)C(F)F H298:-225.25 kcal/mol
library:CHOF_G4 label:F[C](F)CC(F)C(F)F smiles:F[C](F)CC(F)C(F)F H298:-224.69 kcal/mol
library:CHOF_G4 label:FOC(F)(F)[C](F)F smiles:FOC(F)(F)[C](F)F H298:-172.20 kcal/mol
library:CHOF_G4 label:CC(F)C(F)(F)[C](F)F smiles:CC(F)C(F)(F)[C](F)F H298:-223.11 kcal/mol
library:CHOF_G4 label:CC(F)(F)C[C](F)F smiles:CC(F)(F)C[C](F)F H298:-185.38 kcal/mol
library:CHOF_G4 label:CC(F)([C](F)F)C(F)(F)F smiles:CC(F)([C](F)F)C(F)(F)F H298:-281.15 kcal/mol
library:CHOF_G4 label:F[C](F)CC(F)C(F)(F)F smiles:F[C](F)CC(F)C(F)(F)F H298:-282.10 kcal/mol
library:CHOF_G4 label:FCC[C](F)F smiles:FCC[C](F)F H298:-119.66 kcal/mol
library:CHOF_G4 label:CC(F)(F)[C](F)F smiles:CC(F)(F)[C](F)F H298:-174.07 kcal/mol
library:CHOF_G4 label:CC(CF)[C](F)F smiles:CC(CF)[C](F)F H298:-126.71 kcal/mol
library:CHOF_G4 label:OC([C](F)F)C(F)(F)F smiles:OC([C](F)F)C(F)(F)F H298:-264.04 kcal/mol
library:CHOF_G4 label:ODCC(F)[C](F)F smiles:O=CC(F)[C](F)F H298:-133.10 kcal/mol
library:CHOFCl_G4 label:CC(Cl)C[C](F)F smiles:CC(Cl)C[C](F)F H298:-90.13 kcal/mol
library:CHOFCl_G4 label:F[C](F)C(F)(F)Cl smiles:F[C](F)C(F)(F)Cl H298:-166.68 kcal/mol
library:CHOFCl_G4 label:COC(Cl)[C](F)F smiles:COC(Cl)[C](F)F H298:-108.52 kcal/mol
library:CHOFCl_G4 label:OC(O)(Cl)[C](F)F smiles:OC(O)(Cl)[C](F)F H298:-158.18 kcal/mol
library:CHOFCl_G4 label:F[C](F)C(F)CCl smiles:F[C](F)C(F)CCl H298:-124.03 kcal/mol
library:CHOFCl_G4 label:OC(Cl)[C](F)F smiles:OC(Cl)[C](F)F H298:-112.57 kcal/mol
library:CHOFCl_G4 label:ODCC(Cl)[C](F)F smiles:O=CC(Cl)[C](F)F H298:-95.56 kcal/mol
library:CHOFCl_G4 label:F[C](F)CC(Cl)Cl smiles:F[C](F)CC(Cl)Cl H298:-85.82 kcal/mol
library:CHOFCl_G4 label:CC(CCl)[C](F)F smiles:CC(CCl)[C](F)F H298:-88.66 kcal/mol
library:CHOFCl_G4 label:CC(C)(Cl)[C](F)F smiles:CC(C)(Cl)[C](F)F H298:-92.51 kcal/mol
library:CHOFCl_G4 label:F[C](F)C(F)Cl smiles:F[C](F)C(F)Cl H298:-115.95 kcal/mol
library:CHOFCl_G4 label:OCC(Cl)[C](F)F smiles:OCC(Cl)[C](F)F H298:-117.70 kcal/mol
library:CHOFCl_G4 label:F[C](F)CC(F)Cl smiles:F[C](F)CC(F)Cl H298:-127.40 kcal/mol
library:CHOFCl_G4 label:F[C](F)COCl smiles:F[C](F)COCl H298:-69.24 kcal/mol
library:CHOFCl_G4 label:OC(F)(Cl)[C](F)F smiles:OC(F)(Cl)[C](F)F H298:-163.41 kcal/mol
library:CHOFCl_G4 label:F[C](F)COOCl smiles:F[C](F)COOCl H298:-53.95 kcal/mol
library:CHOFCl_G4 label:OC(OCl)[C](F)F smiles:OC(OCl)[C](F)F H298:-113.13 kcal/mol
library:CHOFCl_G4 label:F[C](F)CCOCl smiles:F[C](F)CCOCl H298:-78.26 kcal/mol
library:CHOFCl_G4 label:F[C](F)C(Cl)CCl smiles:F[C](F)C(Cl)CCl H298:-86.78 kcal/mol
library:CHOFCl_G4 label:F[C](F)CCl smiles:F[C](F)CCl H298:-74.02 kcal/mol
library:CHOFCl_G4 label:ODC(Cl)C[C](F)F smiles:O=C(Cl)C[C](F)F H298:-109.44 kcal/mol
library:CHOFCl_G4 label:F[C](F)C(Cl)OCl smiles:F[C](F)C(Cl)OCl H298:-74.35 kcal/mol
library:CHOFCl_G4 label:F[C](F)C(Cl)(Cl)Cl smiles:F[C](F)C(Cl)(Cl)Cl H298:-75.90 kcal/mol
library:CHOFCl_G4 label:OC(Cl)(Cl)[C](F)F smiles:OC(Cl)(Cl)[C](F)F H298:-116.85 kcal/mol
library:CHOFCl_G4 label:CC(Cl)[C](F)F smiles:CC(Cl)[C](F)F H298:-82.81 kcal/mol
library:CHOFCl_G4 label:F[C](F)CCCCl smiles:F[C](F)CCCCl H298:-88.16 kcal/mol
library:CHOFCl_G4 label:F[C](F)COCCl smiles:F[C](F)COCCl H298:-108.90 kcal/mol
library:CHOFCl_G4 label:CC(OCl)[C](F)F smiles:CC(OCl)[C](F)F H298:-79.72 kcal/mol
library:CHOFCl_G4 label:F[C](F)CCCl smiles:F[C](F)CCCl H298:-81.27 kcal/mol
library:CHOFCl_G4 label:CCC(Cl)[C](F)F smiles:CCC(Cl)[C](F)F H298:-88.25 kcal/mol
library:CHOFCl_G4 label:CC(F)(Cl)[C](F)F smiles:CC(F)(Cl)[C](F)F H298:-128.60 kcal/mol
library:CHOFCl_G4 label:F[C](F)C(Cl)Cl smiles:F[C](F)C(Cl)Cl H298:-75.25 kcal/mol
library:CHOFCl_G4 label:OC(CCl)[C](F)F smiles:OC(CCl)[C](F)F H298:-118.91 kcal/mol
library:CHOFCl_G4 label:F[C](F)C(F)OCl smiles:F[C](F)C(F)OCl H298:-118.02 kcal/mol
library:CHOFCl_G4 label:CC(O)(Cl)[C](F)F smiles:CC(O)(Cl)[C](F)F H298:-124.71 kcal/mol
library:CHOFCl_G4 label:OC(Cl)C[C](F)F smiles:OC(Cl)C[C](F)F H298:-122.52 kcal/mol
library:CHOFCl_G4 label:F[C](F)C(F)(Cl)Cl smiles:F[C](F)C(F)(Cl)Cl H298:-119.53 kcal/mol
library:CHOFCl_G4 label:CC(Cl)(Cl)[C](F)F smiles:CC(Cl)(Cl)[C](F)F H298:-86.45 kcal/mol
library:CHOFClBr_G4 label:F[C](F)C(F)(Cl)Br smiles:F[C](F)C(F)(Cl)Br H298:-107.18 kcal/mol
library:CHOFClBr_G4 label:OC(Cl)(Br)[C](F)F smiles:OC(Cl)(Br)[C](F)F H298:-104.75 kcal/mol
library:CHOFClBr_G4 label:F[C](F)C(Cl)(Br)Br smiles:F[C](F)C(Cl)(Br)Br H298:-52.60 kcal/mol
library:CHOFClBr_G4 label:F[C](F)C(Cl)Br smiles:F[C](F)C(Cl)Br H298:-64.01 kcal/mol
library:CHOFClBr_G4 label:CC(Cl)(Br)[C](F)F smiles:CC(Cl)(Br)[C](F)F H298:-74.94 kcal/mol
library:CHOFClBr_G4 label:F[C](F)C(Cl)(Cl)Br smiles:F[C](F)C(Cl)(Cl)Br H298:-64.22 kcal/mol
library:CHOFClBr_G4 label:F[C](F)C(Cl)OBr smiles:F[C](F)C(Cl)OBr H298:-72.15 kcal/mol
library:CHOFClBr_G4 label:F[C](F)C(Cl)CBr smiles:F[C](F)C(Cl)CBr H298:-75.92 kcal/mol
library:CHOFClBr_G4 label:F[C](F)CC(Cl)Br smiles:F[C](F)CC(Cl)Br H298:-74.16 kcal/mol
library:CHOFBr_G4 label:CC(OBr)[C](F)F smiles:CC(OBr)[C](F)F H298:-76.70 kcal/mol
library:CHOFBr_G4 label:CC(Br)[C](F)F smiles:CC(Br)[C](F)F H298:-71.51 kcal/mol
library:CHOFBr_G4 label:F[C](F)C(Br)OBr smiles:F[C](F)C(Br)OBr H298:-60.78 kcal/mol
library:CHOFBr_G4 label:FCC(CBr)[C](F)F smiles:FCC(CBr)[C](F)F H298:-120.39 kcal/mol
library:CHOFBr_G4 label:F[C](F)C(F)OBr smiles:F[C](F)C(F)OBr H298:-115.76 kcal/mol
library:CHOFBr_G4 label:ODCC(F)(Br)[C](F)F smiles:O=CC(F)(Br)[C](F)F H298:-125.77 kcal/mol
library:CHOFBr_G4 label:F[C](F)C(Br)C(Br)Br smiles:F[C](F)C(Br)C(Br)Br H298:-56.55 kcal/mol
library:CHOFBr_G4 label:F[C](F)CC(F)(F)Br smiles:F[C](F)CC(F)(F)Br H298:-166.38 kcal/mol
library:CHOFBr_G4 label:F[C](F)C(Br)Br smiles:F[C](F)C(Br)Br H298:-52.85 kcal/mol
library:CHOFBr_G4 label:F[C](F)CC(Br)CBr smiles:F[C](F)CC(Br)CBr H298:-73.46 kcal/mol
library:CHOFBr_G4 label:OC(Br)C[C](F)F smiles:OC(Br)C[C](F)F H298:-109.81 kcal/mol
library:CHOFBr_G4 label:COC(F)(Br)[C](F)F smiles:COC(F)(Br)[C](F)F H298:-147.26 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)[C](F)F smiles:CC(F)(Br)[C](F)F H298:-116.50 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(F)[C](F)F smiles:CC(Br)C(F)[C](F)F H298:-121.04 kcal/mol
library:CHOFBr_G4 label:CCC(Br)(Br)[C](F)F smiles:CCC(Br)(Br)[C](F)F H298:-69.26 kcal/mol
library:CHOFBr_G4 label:F[C](F)CCC(F)Br smiles:F[C](F)CCC(F)Br H298:-122.64 kcal/mol
library:CHOFBr_G4 label:CCC(Br)[C](F)F smiles:CCC(Br)[C](F)F H298:-77.24 kcal/mol
library:CHOFBr_G4 label:CC(F)(CBr)[C](F)F smiles:CC(F)(CBr)[C](F)F H298:-123.43 kcal/mol
library:CHOFBr_G4 label:OC([C](F)F)C(F)Br smiles:OC([C](F)F)C(F)Br H298:-150.90 kcal/mol
library:CHOFBr_G4 label:OC(F)(Br)C[C](F)F smiles:OC(F)(Br)C[C](F)F H298:-163.12 kcal/mol
library:CHOFBr_G4 label:COC(Br)(Br)[C](F)F smiles:COC(Br)(Br)[C](F)F H298:-90.44 kcal/mol
library:CHOFBr_G4 label:FOC(OBr)[C](F)F smiles:FOC(OBr)[C](F)F H298:-76.67 kcal/mol
library:CHOFBr_G4 label:CC(Br)(Br)C[C](F)F smiles:CC(Br)(Br)C[C](F)F H298:-72.20 kcal/mol
library:CHOFBr_G4 label:F[C](F)C(Br)OOBr smiles:F[C](F)C(Br)OOBr H298:-43.76 kcal/mol
library:CHOFBr_G4 label:F[C](F)C(F)CCBr smiles:F[C](F)C(F)CCBr H298:-119.56 kcal/mol
library:CHOFBr_G4 label:CC([C](F)F)C(F)Br smiles:CC([C](F)F)C(F)Br H298:-122.24 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)C[C](F)F smiles:CC(F)(Br)C[C](F)F H298:-126.29 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(Br)[C](F)F smiles:OC(Br)C(Br)[C](F)F H298:-103.62 kcal/mol
library:CHOFBr_G4 label:OC(F)(CBr)[C](F)F smiles:OC(F)(CBr)[C](F)F H298:-160.59 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(Br)[C](F)F smiles:O=C(Br)C(Br)[C](F)F H298:-87.38 kcal/mol
library:CHOFBr_G4 label:OOC(F)(Br)[C](F)F smiles:OOC(F)(Br)[C](F)F H298:-128.53 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C[C](F)F smiles:O=C(Br)C[C](F)F H298:-97.00 kcal/mol
library:CHOFBr_G4 label:F[C](F)C(Br)(Br)CBr smiles:F[C](F)C(Br)(Br)CBr H298:-54.88 kcal/mol
library:CHOFBr_G4 label:OC(CBr)[C](F)F smiles:OC(CBr)[C](F)F H298:-108.00 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(F)[C](F)F smiles:OC(Br)C(F)[C](F)F H298:-151.49 kcal/mol
library:CHOFBr_G4 label:F[C](F)C(F)(F)OBr smiles:F[C](F)C(F)(F)OBr H298:-169.63 kcal/mol
library:CHOFBr_G4 label:F[C](F)CCBr smiles:F[C](F)CCBr H298:-70.18 kcal/mol
library:CHOFBr_G4 label:F[C](F)C(F)(Br)Br smiles:F[C](F)C(F)(Br)Br H298:-94.70 kcal/mol
library:CHOFBr_G4 label:F[C](F)COC(F)Br smiles:F[C](F)COC(F)Br H298:-147.98 kcal/mol
library:CHOFBr_G4 label:F[C](F)COCBr smiles:F[C](F)COCBr H298:-97.16 kcal/mol
library:CHOFBr_G4 label:F[C](F)CCCBr smiles:F[C](F)CCCBr H298:-76.97 kcal/mol
library:CHOFBr_G4 label:F[C](F)CCC(Br)Br smiles:F[C](F)CCC(Br)Br H298:-70.50 kcal/mol
library:CHOFBr_G4 label:CC(O)(Br)[C](F)F smiles:CC(O)(Br)[C](F)F H298:-112.49 kcal/mol
library:CHOFBr_G4 label:F[C](F)C(F)(Br)OBr smiles:F[C](F)C(F)(Br)OBr H298:-109.73 kcal/mol
library:CHOFBr_G4 label:F[C](F)C(CBr)CBr smiles:F[C](F)C(CBr)CBr H298:-71.98 kcal/mol
library:CHOFBr_G4 label:CC([C](F)F)C(Br)Br smiles:CC([C](F)F)C(Br)Br H298:-69.84 kcal/mol
library:CHOFBr_G4 label:F[C](F)CC(F)CBr smiles:F[C](F)CC(F)CBr H298:-122.72 kcal/mol
library:CHOFBr_G4 label:OC(Br)(OBr)[C](F)F smiles:OC(Br)(OBr)[C](F)F H298:-106.15 kcal/mol
library:CHOFBr_G4 label:OOC(Br)[C](F)F smiles:OOC(Br)[C](F)F H298:-80.23 kcal/mol
library:CHOFBr_G4 label:COC(Br)[C](F)F smiles:COC(Br)[C](F)F H298:-96.50 kcal/mol
library:CHOFBr_G4 label:OC(O)(Br)[C](F)F smiles:OC(O)(Br)[C](F)F H298:-145.15 kcal/mol
library:CHOFBr_G4 label:F[C](F)CBr smiles:F[C](F)CBr H298:-63.22 kcal/mol
library:CHOFBr_G4 label:F[C](F)CC(F)OBr smiles:F[C](F)CC(F)OBr H298:-128.74 kcal/mol
library:CHOFBr_G4 label:F[C](F)C(CBr)OBr smiles:F[C](F)C(CBr)OBr H298:-68.97 kcal/mol
library:CHOFBr_G4 label:F[C](F)C(F)(Br)CBr smiles:F[C](F)C(F)(Br)CBr H298:-108.03 kcal/mol
library:CHOFBr_G4 label:OC([C](F)F)C(Br)Br smiles:OC([C](F)F)C(Br)Br H298:-99.14 kcal/mol
library:CHOFBr_G4 label:CC(F)(OBr)[C](F)F smiles:CC(F)(OBr)[C](F)F H298:-129.64 kcal/mol
library:CHOFBr_G4 label:CC(Br)(OBr)[C](F)F smiles:CC(Br)(OBr)[C](F)F H298:-72.56 kcal/mol
library:CHOFBr_G4 label:F[C](F)CCOBr smiles:F[C](F)CCOBr H298:-74.80 kcal/mol
library:CHOFBr_G4 label:F[C](F)COOBr smiles:F[C](F)COOBr H298:-50.53 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)C[C](F)F smiles:OC(Br)(Br)C[C](F)F H298:-104.36 kcal/mol
library:CHOFBr_G4 label:F[C](F)COBr smiles:F[C](F)COBr H298:-66.04 kcal/mol
library:CHOFBr_G4 label:F[C](F)C(F)(F)CBr smiles:F[C](F)C(F)(F)CBr H298:-163.76 kcal/mol
library:CHOFBr_G4 label:OOC(Br)(Br)[C](F)F smiles:OOC(Br)(Br)[C](F)F H298:-71.59 kcal/mol
library:CHOFBr_G4 label:F[C](F)C(Br)(Br)Br smiles:F[C](F)C(Br)(Br)Br H298:-41.00 kcal/mol
library:CHOFBr_G4 label:F[C](F)CC(F)Br smiles:F[C](F)CC(F)Br H298:-114.77 kcal/mol
library:CHOFBr_G4 label:CC(CBr)[C](F)F smiles:CC(CBr)[C](F)F H298:-77.71 kcal/mol
library:CHOFBr_G4 label:F[C](F)C(Br)(Br)OBr smiles:F[C](F)C(Br)(Br)OBr H298:-52.61 kcal/mol
library:CHOFBr_G4 label:CC(Br)(Br)[C](F)F smiles:CC(Br)(Br)[C](F)F H298:-63.49 kcal/mol
library:CHOFBr_G4 label:F[C](F)C(F)OOBr smiles:F[C](F)C(F)OOBr H298:-97.83 kcal/mol
library:CHOFBr_G4 label:F[C](F)C(F)Br smiles:F[C](F)C(F)Br H298:-104.03 kcal/mol
library:CHOFBr_G4 label:F[C](F)C(F)COBr smiles:F[C](F)C(F)COBr H298:-116.84 kcal/mol
library:CHOFBr_G4 label:OCC(F)(Br)[C](F)F smiles:OCC(F)(Br)[C](F)F H298:-151.25 kcal/mol
library:CHOFBr_G4 label:OC(Br)[C](F)F smiles:OC(Br)[C](F)F H298:-100.96 kcal/mol
library:CHOFBr_G4 label:F[C](F)C(Br)OCBr smiles:F[C](F)C(Br)OCBr H298:-93.84 kcal/mol
library:CHOFBr_G4 label:F[C](F)C(Br)CCBr smiles:F[C](F)C(Br)CCBr H298:-72.29 kcal/mol
library:CHOFBr_G4 label:F[C](F)CC(Br)Br smiles:F[C](F)CC(Br)Br H298:-62.57 kcal/mol
library:CHOFBr_G4 label:FCC(OBr)[C](F)F smiles:FCC(OBr)[C](F)F H298:-117.05 kcal/mol
library:CHOFBr_G4 label:OC(F)(Br)[C](F)F smiles:OC(F)(Br)[C](F)F H298:-150.78 kcal/mol
library:CHOFBr_G4 label:F[C](F)C(OBr)OBr smiles:F[C](F)C(OBr)OBr H298:-71.63 kcal/mol
library:CHOFBr_G4 label:CCC(F)(Br)[C](F)F smiles:CCC(F)(Br)[C](F)F H298:-122.14 kcal/mol
library:CHOFBr_G4 label:OC(Br)(CBr)[C](F)F smiles:OC(Br)(CBr)[C](F)F H298:-104.42 kcal/mol
library:CHOFBr_G4 label:OCC(Br)(Br)[C](F)F smiles:OCC(Br)(Br)[C](F)F H298:-99.38 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)[C](F)F smiles:OC(Br)(Br)[C](F)F H298:-92.64 kcal/mol
library:CHOFBr_G4 label:F[C](F)COC(Br)Br smiles:F[C](F)COC(Br)Br H298:-91.30 kcal/mol
library:CHOFBr_G4 label:F[C](F)CC(Br)OBr smiles:F[C](F)CC(Br)OBr H298:-72.64 kcal/mol
library:CHOFBr_G4 label:CC(Br)C[C](F)F smiles:CC(Br)C[C](F)F H298:-78.92 kcal/mol
library:CHOFBr_G4 label:F[C](F)C(F)C(Br)Br smiles:F[C](F)C(F)C(Br)Br H298:-103.90 kcal/mol
library:CHOFBr_G4 label:OC(F)(OBr)[C](F)F smiles:OC(F)(OBr)[C](F)F H298:-164.55 kcal/mol
library:CHOFBr_G4 label:F[C](F)C(F)CBr smiles:F[C](F)C(F)CBr H298:-113.21 kcal/mol
library:CHOFBr_G4 label:F[C](F)C(F)C(F)Br smiles:F[C](F)C(F)C(F)Br H298:-155.11 kcal/mol
library:CHOFBr_G4 label:F[C](F)CC(Br)(Br)Br smiles:F[C](F)CC(Br)(Br)Br H298:-51.60 kcal/mol
library:CHOFBr_G4 label:F[C](F)CC(F)(Br)Br smiles:F[C](F)CC(F)(Br)Br H298:-106.66 kcal/mol
library:CHOFBr_G4 label:F[C](F)C(F)(F)Br smiles:F[C](F)C(F)(F)Br H298:-153.76 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(F)[C](F)F smiles:O=C(Br)C(F)[C](F)F H298:-135.19 kcal/mol
library:CHOFBr_G4 label:OC(OBr)[C](F)F smiles:OC(OBr)[C](F)F H298:-110.31 kcal/mol
""",
)

entry(
    index = 79,
    label = "CsBr1sCsH",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cs   u0 {1,S}
3   H    u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.133567,-1.16766,-1.99677,-2.662,-3.61533,-4.22481,-5.00004],'cal/(mol*K)','+|-',[0.111917,0.11491,0.107742,0.100634,0.0888115,0.0777166,0.0569213]),
        H298 = (97.5558,'kcal/mol','+|-',0.178786),
        S298 = (3.7069,'cal/(mol*K)','+|-',0.30384),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:COC[CH]Br smiles:COC[CH]Br H298:0.08 kcal/mol
library:CHOBr_G4 label:Br[CH]CCDCBr smiles:Br[CH]CC=CBr H298:54.42 kcal/mol
library:CHOBr_G4 label:CC([CH]Br)OBr smiles:CC([CH]Br)OBr H298:21.83 kcal/mol
library:CHOBr_G4 label:Br[CH]C(Br)OOBr smiles:Br[CH]C(Br)OOBr H298:52.45 kcal/mol
library:CHOBr_G4 label:OC(Br)C[CH]Br smiles:OC(Br)C[CH]Br H298:-10.66 kcal/mol
library:CHOBr_G4 label:Br[CH]C(Br)COBr smiles:Br[CH]C(Br)COBr H298:27.92 kcal/mol
library:CHOBr_G4 label:Br[CH]COOBr smiles:Br[CH]COOBr H298:47.60 kcal/mol
library:CHOBr_G4 label:C[CH]Br smiles:C[CH]Br H298:30.64 kcal/mol
library:CHOBr_G4 label:Br[CH]CCOBr smiles:Br[CH]CCOBr H298:25.61 kcal/mol
library:CHOBr_G4 label:CC(Br)(Br)C[CH]Br smiles:CC(Br)(Br)C[CH]Br H298:26.42 kcal/mol
library:CHOBr_G4 label:Br[CH]C(CBr)CBr smiles:Br[CH]C(CBr)CBr H298:27.15 kcal/mol
library:CHOBr_G4 label:Br[CH]COBr smiles:Br[CH]COBr H298:32.14 kcal/mol
library:CHOBr_G4 label:Br[CH]CCC(Br)Br smiles:Br[CH]CCC(Br)Br H298:29.72 kcal/mol
library:CHOBr_G4 label:CC(Br)(Br)[CH]Br smiles:CC(Br)(Br)[CH]Br H298:33.14 kcal/mol
library:CHOBr_G4 label:Br[CH]CC(Br)Br smiles:Br[CH]CC(Br)Br H298:36.34 kcal/mol
library:CHOBr_G4 label:OOC[CH]Br smiles:OOC[CH]Br H298:13.77 kcal/mol
library:CHOBr_G4 label:COC(Br)(Br)[CH]Br smiles:COC(Br)(Br)[CH]Br H298:4.80 kcal/mol
library:CHOBr_G4 label:CC[CH]Br smiles:CC[CH]Br H298:25.37 kcal/mol
library:CHOBr_G4 label:CDC(Br)C[CH]Br smiles:C=C(Br)C[CH]Br H298:52.37 kcal/mol
library:CHOBr_G4 label:ODCC(Br)[CH]Br smiles:O=CC(Br)[CH]Br H298:11.74 kcal/mol
library:CHOBr_G4 label:Br[CH]C(Br)(Br)OBr smiles:Br[CH]C(Br)(Br)OBr H298:41.64 kcal/mol
library:CHOBr_G4 label:OC([CH]Br)CBr smiles:OC([CH]Br)CBr H298:-8.21 kcal/mol
library:CHOBr_G4 label:C#CC(Br)[CH]Br smiles:C#CC(Br)[CH]Br H298:97.63 kcal/mol
library:CHOBr_G4 label:CC(O)[CH]Br smiles:CC(O)[CH]Br H298:-14.06 kcal/mol
library:CHOBr_G4 label:CCC(Br)[CH]Br smiles:CCC(Br)[CH]Br H298:21.17 kcal/mol
library:CHOBr_G4 label:C#CC[CH]Br smiles:C#CC[CH]Br H298:91.96 kcal/mol
library:CHOBr_G4 label:CC(C)(Br)[CH]Br smiles:CC(C)(Br)[CH]Br H298:17.99 kcal/mol
library:CHOBr_G4 label:Br[CH]CBr smiles:Br[CH]CBr H298:35.29 kcal/mol
library:CHOBr_G4 label:Br[CH]C(Br)CBr smiles:Br[CH]C(Br)CBr H298:32.27 kcal/mol
library:CHOBr_G4 label:Br[CH]CC(Br)CBr smiles:Br[CH]CC(Br)CBr H298:26.33 kcal/mol
library:CHOBr_G4 label:Br[CH]CC(Br)(Br)Br smiles:Br[CH]CC(Br)(Br)Br H298:45.81 kcal/mol
library:CHOBr_G4 label:OC[CH]Br smiles:OC[CH]Br H298:-4.09 kcal/mol
library:CHOBr_G4 label:CC(Br)[CH]Br smiles:CC(Br)[CH]Br H298:26.99 kcal/mol
library:CHOBr_G4 label:Br[CH]C(Br)(Br)Br smiles:Br[CH]C(Br)(Br)Br H298:54.10 kcal/mol
library:CHOBr_G4 label:Br[CH]C(OBr)OBr smiles:Br[CH]C(OBr)OBr H298:24.14 kcal/mol
library:CHOBr_G4 label:Br[CH]C(Br)C(Br)Br smiles:Br[CH]C(Br)C(Br)Br H298:40.44 kcal/mol
library:CHOBr_G4 label:Br[CH]C(Br)OBr smiles:Br[CH]C(Br)OBr H298:35.25 kcal/mol
library:CHOBr_G4 label:OCC[CH]Br smiles:OCC[CH]Br H298:-10.76 kcal/mol
library:CHOBr_G4 label:Br[CH]COC(Br)Br smiles:Br[CH]COC(Br)Br H298:7.79 kcal/mol
library:CHOBr_G4 label:Br[CH]CC(Br)OBr smiles:Br[CH]CC(Br)OBr H298:26.60 kcal/mol
library:CHOBr_G4 label:Br[CH]C(Br)Br smiles:Br[CH]C(Br)Br H298:43.28 kcal/mol
library:CHOBr_G4 label:CC(Br)([CH]Br)OBr smiles:CC(Br)([CH]Br)OBr H298:24.94 kcal/mol
library:CHOBr_G4 label:CCC[CH]Br smiles:CCC[CH]Br H298:19.81 kcal/mol
library:CHOBr_G4 label:ODCC[CH]Br smiles:O=CC[CH]Br H298:7.13 kcal/mol
library:CHOBr_G4 label:CC(Br)C[CH]Br smiles:CC(Br)C[CH]Br H298:22.04 kcal/mol
library:CHOBr_G4 label:OC([CH]Br)OBr smiles:OC([CH]Br)OBr H298:-13.62 kcal/mol
library:CHOBr_G4 label:CCC(Br)(Br)[CH]Br smiles:CCC(Br)(Br)[CH]Br H298:26.87 kcal/mol
library:CHOBr_G4 label:Br[CH]C(Br)(Br)CBr smiles:Br[CH]C(Br)(Br)CBr H298:39.79 kcal/mol
library:CHOBr_G4 label:ODC(Br)C[CH]Br smiles:O=C(Br)C[CH]Br H298:1.84 kcal/mol
library:CHOBr_G4 label:OC(Br)(Br)[CH]Br smiles:OC(Br)(Br)[CH]Br H298:2.66 kcal/mol
library:CHOBr_G4 label:CC([CH]Br)C(Br)Br smiles:CC([CH]Br)C(Br)Br H298:29.50 kcal/mol
library:CHOBr_G4 label:Br[CH]C(CBr)OBr smiles:Br[CH]C(CBr)OBr H298:28.43 kcal/mol
library:CHOBr_G4 label:BrC#CC[CH]Br smiles:BrC#CC[CH]Br H298:102.28 kcal/mol
library:CHOBr_G4 label:Br[CH]CCBr smiles:Br[CH]CCBr H298:30.25 kcal/mol
library:CHOBr_G4 label:OC(O)[CH]Br smiles:OC(O)[CH]Br H298:-50.78 kcal/mol
library:CHOBr_G4 label:Br[CH]CCCBr smiles:Br[CH]CCCBr H298:24.26 kcal/mol
library:CHOBr_G4 label:CDCC[CH]Br smiles:C=CC[CH]Br H298:50.65 kcal/mol
library:CHOBr_G4 label:CC(Br)C(Br)[CH]Br smiles:CC(Br)C(Br)[CH]Br H298:24.02 kcal/mol
library:CHOBr_G4 label:Br[CH]COCBr smiles:Br[CH]COCBr H298:1.44 kcal/mol
library:CHOBr_G4 label:Br[CH]C(Br)CCBr smiles:Br[CH]C(Br)CCBr H298:25.17 kcal/mol
library:CHOBr_G4 label:CC([CH]Br)CBr smiles:CC([CH]Br)CBr H298:22.83 kcal/mol
library:CHOBr_G4 label:Br[CH]C(Br)OCBr smiles:Br[CH]C(Br)OCBr H298:2.65 kcal/mol
library:CHOBr_G4 label:OCC(Br)[CH]Br smiles:OCC(Br)[CH]Br H298:-9.75 kcal/mol
library:CHOBr_G4 label:CC(C)[CH]Br smiles:CC(C)[CH]Br H298:18.19 kcal/mol
library:CHOFClBr_G4 label:FC#CC(Cl)[CH]Br smiles:FC#CC(Cl)[CH]Br H298:58.97 kcal/mol
library:CHOFClBr_G4 label:C#CC(F)(Cl)[CH]Br smiles:C#CC(F)(Cl)[CH]Br H298:44.13 kcal/mol
library:CHOFBr_G4 label:FC#CC[CH]Br smiles:FC#CC[CH]Br H298:63.48 kcal/mol
library:CHOFBr_G4 label:C#CC(F)[CH]Br smiles:C#CC(F)[CH]Br H298:49.33 kcal/mol
library:CHOFBr_G4 label:FC#CC(F)[CH]Br smiles:FC#CC(F)[CH]Br H298:20.51 kcal/mol
library:CHOFBr_G4 label:C#CC(F)(F)[CH]Br smiles:C#CC(F)(F)[CH]Br H298:-1.25 kcal/mol
library:CHOFBr_G4 label:C#CC(F)(Br)[CH]Br smiles:C#CC(F)(Br)[CH]Br H298:55.95 kcal/mol
library:CHOFBr_G4 label:FC#CC(F)(F)[CH]Br smiles:FC#CC(F)(F)[CH]Br H298:-30.39 kcal/mol
library:CHOFBr_G4 label:FC#CC(Br)(Br)[CH]Br smiles:FC#CC(Br)(Br)[CH]Br H298:78.11 kcal/mol
library:CHOFBr_G4 label:FC#CC(F)(Br)[CH]Br smiles:FC#CC(F)(Br)[CH]Br H298:27.70 kcal/mol
library:CHOClBr_G4 label:ClC#CC[CH]Br smiles:ClC#CC[CH]Br H298:91.24 kcal/mol
library:CHOClBr_G4 label:C#CC(Cl)(Br)[CH]Br smiles:C#CC(Cl)(Br)[CH]Br H298:95.84 kcal/mol
library:CHOClBr_G4 label:C#CC(Cl)(Cl)[CH]Br smiles:C#CC(Cl)(Cl)[CH]Br H298:85.09 kcal/mol
library:CHOClBr_G4 label:C#CC(Cl)[CH]Br smiles:C#CC(Cl)[CH]Br H298:87.43 kcal/mol
""",
)

entry(
    index = 80,
    label = "CsCl1sCsH",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cs   u0 {1,S}
3   H    u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.197528,-0.86367,-1.76193,-2.47312,-3.48282,-4.13051,-4.95992],'cal/(mol*K)','+|-',[0.0620192,0.0636779,0.0597058,0.0557667,0.0492152,0.043067,0.0315432]),
        H298 = (95.973,'kcal/mol','+|-',0.0990751),
        S298 = (3.6424,'cal/(mol*K)','+|-',0.168374),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOCl_G4 label:Cl[CH]C(Cl)(Cl)CCCl smiles:Cl[CH]C(Cl)(Cl)CCCl H298:-12.36 kcal/mol
library:CHOCl_G4 label:CC(C)[CH]Cl smiles:CC(C)[CH]Cl H298:5.59 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)(Cl)Cl smiles:Cl[CH]C(Cl)(Cl)Cl H298:7.59 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)(Cl)OCCl smiles:Cl[CH]C(Cl)(Cl)OCCl H298:-35.18 kcal/mol
library:CHOCl_G4 label:CCC(Cl)[CH]Cl smiles:CCC(Cl)[CH]Cl H298:-1.11 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)(Cl)C(Cl)(Cl)Cl smiles:Cl[CH]C(Cl)(Cl)C(Cl)(Cl)Cl H298:-7.54 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)OCCl smiles:Cl[CH]C(Cl)OCCl H298:-28.98 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)CCCl smiles:Cl[CH]C(Cl)CCCl H298:-7.99 kcal/mol
library:CHOCl_G4 label:C#CC(Cl)[CH]Cl smiles:C#CC(Cl)[CH]Cl H298:75.28 kcal/mol
library:CHOCl_G4 label:OC([CH]Cl)C(Cl)(Cl)Cl smiles:OC([CH]Cl)C(Cl)(Cl)Cl H298:-39.22 kcal/mol
library:CHOCl_G4 label:OCC(Cl)(Cl)[CH]Cl smiles:OCC(Cl)(Cl)[CH]Cl H298:-37.80 kcal/mol
library:CHOCl_G4 label:CC(C)(Cl)[CH]Cl smiles:CC(C)(Cl)[CH]Cl H298:-5.07 kcal/mol
library:CHOCl_G4 label:CC(Cl)([CH]Cl)CCl smiles:CC(Cl)([CH]Cl)CCl H298:-10.73 kcal/mol
library:CHOCl_G4 label:CDCC[CH]Cl smiles:C=CC[CH]Cl H298:38.11 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)CC(Cl)(Cl)Cl smiles:Cl[CH]C(Cl)CC(Cl)(Cl)Cl H298:-12.72 kcal/mol
library:CHOCl_G4 label:OC(Cl)C(Cl)[CH]Cl smiles:OC(Cl)C(Cl)[CH]Cl H298:-42.21 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)(Cl)OCl smiles:Cl[CH]C(Cl)(Cl)OCl H298:4.68 kcal/mol
library:CHOCl_G4 label:OC(O)[CH]Cl smiles:OC(O)[CH]Cl H298:-62.87 kcal/mol
library:CHOCl_G4 label:CC(Cl)([CH]Cl)C(Cl)(Cl)Cl smiles:CC(Cl)([CH]Cl)C(Cl)(Cl)Cl H298:-15.04 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)(Cl)C(Cl)Cl smiles:Cl[CH]C(Cl)(Cl)C(Cl)Cl H298:-7.16 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)(Cl)C(Cl)C(Cl)(Cl)Cl smiles:Cl[CH]C(Cl)(Cl)C(Cl)C(Cl)(Cl)Cl H298:-13.20 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)(CCl)OCl smiles:Cl[CH]C(Cl)(CCl)OCl H298:-5.91 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(CCl)OCl smiles:Cl[CH]C(CCl)OCl H298:2.83 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)CCl smiles:Cl[CH]C(Cl)CCl H298:-0.68 kcal/mol
library:CHOCl_G4 label:Cl[CH]CCl smiles:Cl[CH]CCl H298:13.10 kcal/mol
library:CHOCl_G4 label:C#CC(Cl)(Cl)[CH]Cl smiles:C#CC(Cl)(Cl)[CH]Cl H298:73.03 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:Cl[CH]C(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-17.08 kcal/mol
library:CHOCl_G4 label:Cl[CH]CC(Cl)C(Cl)(Cl)Cl smiles:Cl[CH]CC(Cl)C(Cl)(Cl)Cl H298:-13.10 kcal/mol
library:CHOCl_G4 label:Cl[CH]CC(Cl)(Cl)CCl smiles:Cl[CH]CC(Cl)(Cl)CCl H298:-13.47 kcal/mol
library:CHOCl_G4 label:CC(Cl)(Cl)C(Cl)[CH]Cl smiles:CC(Cl)(Cl)C(Cl)[CH]Cl H298:-15.09 kcal/mol
library:CHOCl_G4 label:OC([CH]Cl)OCl smiles:OC([CH]Cl)OCl H298:-28.53 kcal/mol
library:CHOCl_G4 label:Cl[CH]CCOCl smiles:Cl[CH]CCOCl H298:10.04 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)(Cl)C(Cl)CCl smiles:Cl[CH]C(Cl)(Cl)C(Cl)CCl H298:-17.79 kcal/mol
library:CHOCl_G4 label:Cl[CH]COOCl smiles:Cl[CH]COOCl H298:31.95 kcal/mol
library:CHOCl_G4 label:CC(Cl)C(Cl)(Cl)[CH]Cl smiles:CC(Cl)C(Cl)(Cl)[CH]Cl H298:-13.83 kcal/mol
library:CHOCl_G4 label:OC(Cl)C(Cl)(Cl)[CH]Cl smiles:OC(Cl)C(Cl)(Cl)[CH]Cl H298:-44.76 kcal/mol
library:CHOCl_G4 label:CC(O)(Cl)[CH]Cl smiles:CC(O)(Cl)[CH]Cl H298:-38.48 kcal/mol
library:CHOCl_G4 label:Cl[CH]COCl smiles:Cl[CH]COCl H298:16.65 kcal/mol
library:CHOCl_G4 label:ODCC[CH]Cl smiles:O=CC[CH]Cl H298:-5.06 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)OC(Cl)(Cl)Cl smiles:Cl[CH]C(Cl)OC(Cl)(Cl)Cl H298:-37.32 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)C(Cl)DC(Cl)Cl smiles:Cl[CH]C(Cl)C(Cl)=C(Cl)Cl H298:13.77 kcal/mol
library:CHOCl_G4 label:OC(Cl)(Cl)C(Cl)[CH]Cl smiles:OC(Cl)(Cl)C(Cl)[CH]Cl H298:-47.09 kcal/mol
library:CHOCl_G4 label:Cl[CH]CCDCCl smiles:Cl[CH]CC=CCl H298:30.48 kcal/mol
library:CHOCl_G4 label:CC(Cl)(Cl)C(Cl)(Cl)[CH]Cl smiles:CC(Cl)(Cl)C(Cl)(Cl)[CH]Cl H298:-17.75 kcal/mol
library:CHOCl_G4 label:CCC[CH]Cl smiles:CCC[CH]Cl H298:8.09 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(C(Cl)Cl)C(Cl)Cl smiles:Cl[CH]C(C(Cl)Cl)C(Cl)Cl H298:-15.89 kcal/mol
library:CHOCl_G4 label:CDC(Cl)C[CH]Cl smiles:C=C(Cl)C[CH]Cl H298:28.51 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(C(Cl)Cl)C(Cl)(Cl)Cl smiles:Cl[CH]C(C(Cl)Cl)C(Cl)(Cl)Cl H298:-15.75 kcal/mol
library:CHOCl_G4 label:COC(Cl)[CH]Cl smiles:COC(Cl)[CH]Cl H298:-23.44 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)(Cl)C(Cl)(Cl)OCl smiles:Cl[CH]C(Cl)(Cl)C(Cl)(Cl)OCl H298:-10.58 kcal/mol
library:CHOCl_G4 label:CDCC(Cl)(Cl)[CH]Cl smiles:C=CC(Cl)(Cl)[CH]Cl H298:26.02 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(OCl)C(Cl)Cl smiles:Cl[CH]C(OCl)C(Cl)Cl H298:-2.16 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)(CCl)C(Cl)Cl smiles:Cl[CH]C(Cl)(CCl)C(Cl)Cl H298:-14.94 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)C(Cl)(Cl)OCl smiles:Cl[CH]C(Cl)C(Cl)(Cl)OCl H298:-8.92 kcal/mol
library:CHOCl_G4 label:OC(Cl)([CH]Cl)CCl smiles:OC(Cl)([CH]Cl)CCl H298:-42.47 kcal/mol
library:CHOCl_G4 label:Cl[CH]CC(Cl)OCl smiles:Cl[CH]CC(Cl)OCl H298:-0.22 kcal/mol
library:CHOCl_G4 label:Cl[CH]CC(Cl)(Cl)Cl smiles:Cl[CH]CC(Cl)(Cl)Cl H298:-1.86 kcal/mol
library:CHOCl_G4 label:CCC(Cl)(Cl)[CH]Cl smiles:CCC(Cl)(Cl)[CH]Cl H298:-7.29 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(OCl)C(Cl)(Cl)Cl smiles:Cl[CH]C(OCl)C(Cl)(Cl)Cl H298:-2.72 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)(Cl)CC(Cl)Cl smiles:Cl[CH]C(Cl)(Cl)CC(Cl)Cl H298:-16.86 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:Cl[CH]C(Cl)(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-10.84 kcal/mol
library:CHOCl_G4 label:OCC[CH]Cl smiles:OCC[CH]Cl H298:-22.81 kcal/mol
library:CHOCl_G4 label:OC(Cl)C[CH]Cl smiles:OC(Cl)C[CH]Cl H298:-34.61 kcal/mol
library:CHOCl_G4 label:Cl[CH]CC(Cl)C(Cl)Cl smiles:Cl[CH]CC(Cl)C(Cl)Cl H298:-11.93 kcal/mol
library:CHOCl_G4 label:OC(Cl)(Cl)[CH]Cl smiles:OC(Cl)(Cl)[CH]Cl H298:-33.39 kcal/mol
library:CHOCl_G4 label:CC(Cl)C(Cl)[CH]Cl smiles:CC(Cl)C(Cl)[CH]Cl H298:-9.05 kcal/mol
library:CHOCl_G4 label:CC([CH]Cl)C(Cl)(Cl)Cl smiles:CC([CH]Cl)C(Cl)(Cl)Cl H298:-8.96 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)C(Cl)OCl smiles:Cl[CH]C(Cl)C(Cl)OCl H298:-7.27 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)(OCl)OCl smiles:Cl[CH]C(Cl)(OCl)OCl H298:0.44 kcal/mol
library:CHOCl_G4 label:Cl[CH]COC(Cl)Cl smiles:Cl[CH]COC(Cl)Cl H298:-28.84 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)(C(Cl)Cl)C(Cl)(Cl)Cl smiles:Cl[CH]C(Cl)(C(Cl)Cl)C(Cl)(Cl)Cl H298:-15.38 kcal/mol
library:CHOCl_G4 label:Cl[CH]CC(Cl)Cl smiles:Cl[CH]CC(Cl)Cl H298:1.17 kcal/mol
library:CHOCl_G4 label:ODCC(Cl)[CH]Cl smiles:O=CC(Cl)[CH]Cl H298:-10.34 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)(C(Cl)Cl)C(Cl)Cl smiles:Cl[CH]C(Cl)(C(Cl)Cl)C(Cl)Cl H298:-19.46 kcal/mol
library:CHOCl_G4 label:OC[CH]Cl smiles:OC[CH]Cl H298:-16.26 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(OCl)OCl smiles:Cl[CH]C(OCl)OCl H298:7.29 kcal/mol
library:CHOCl_G4 label:CC([CH]Cl)CCl smiles:CC([CH]Cl)CCl H298:-0.50 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)OC(Cl)Cl smiles:Cl[CH]C(Cl)OC(Cl)Cl H298:-36.18 kcal/mol
library:CHOCl_G4 label:CC(Cl)(Cl)[CH]Cl smiles:CC(Cl)(Cl)[CH]Cl H298:-1.25 kcal/mol
library:CHOCl_G4 label:ClC#CC(Cl)(Cl)[CH]Cl smiles:ClC#CC(Cl)(Cl)[CH]Cl H298:72.14 kcal/mol
library:CHOCl_G4 label:CC([CH]Cl)OCl smiles:CC([CH]Cl)OCl H298:6.69 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(CCl)C(Cl)(Cl)Cl smiles:Cl[CH]C(CCl)C(Cl)(Cl)Cl H298:-13.56 kcal/mol
library:CHOCl_G4 label:OC(Cl)(Cl)C(Cl)(Cl)[CH]Cl smiles:OC(Cl)(Cl)C(Cl)(Cl)[CH]Cl H298:-48.80 kcal/mol
library:CHOCl_G4 label:CDCC(Cl)[CH]Cl smiles:C=CC(Cl)[CH]Cl H298:29.97 kcal/mol
library:CHOCl_G4 label:CC(Cl)([CH]Cl)C(Cl)Cl smiles:CC(Cl)([CH]Cl)C(Cl)Cl H298:-14.08 kcal/mol
library:CHOCl_G4 label:COC(Cl)(Cl)[CH]Cl smiles:COC(Cl)(Cl)[CH]Cl H298:-30.36 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)C(Cl)CCl smiles:Cl[CH]C(Cl)C(Cl)CCl H298:-14.41 kcal/mol
library:CHOCl_G4 label:Cl[CH]CC(Cl)DCCl smiles:Cl[CH]CC(Cl)=CCl H298:22.91 kcal/mol
library:CHOCl_G4 label:ClC#CC[CH]Cl smiles:ClC#CC[CH]Cl H298:79.04 kcal/mol
library:CHOCl_G4 label:OC(Cl)([CH]Cl)OCl smiles:OC(Cl)([CH]Cl)OCl H298:-36.13 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)C(Cl)(Cl)CCl smiles:Cl[CH]C(Cl)C(Cl)(Cl)CCl H298:-17.55 kcal/mol
library:CHOCl_G4 label:OC(Cl)[CH]Cl smiles:OC(Cl)[CH]Cl H298:-26.98 kcal/mol
library:CHOCl_G4 label:ClC#CC(Cl)[CH]Cl smiles:ClC#CC(Cl)[CH]Cl H298:74.53 kcal/mol
library:CHOCl_G4 label:Cl[CH]CC(Cl)CCl smiles:Cl[CH]CC(Cl)CCl H298:-7.39 kcal/mol
library:CHOCl_G4 label:OC(O)(Cl)[CH]Cl smiles:OC(O)(Cl)[CH]Cl H298:-72.77 kcal/mol
library:CHOCl_G4 label:C#CC[CH]Cl smiles:C#CC[CH]Cl H298:79.50 kcal/mol
library:CHOCl_G4 label:OC([CH]Cl)C(Cl)Cl smiles:OC([CH]Cl)C(Cl)Cl H298:-36.92 kcal/mol
library:CHOCl_G4 label:ODC(Cl)C(Cl)(Cl)[CH]Cl smiles:O=C(Cl)C(Cl)(Cl)[CH]Cl H298:-28.01 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)(Cl)C(Cl)(Cl)CCl smiles:Cl[CH]C(Cl)(Cl)C(Cl)(Cl)CCl H298:-18.78 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)(Cl)CDC(Cl)Cl smiles:Cl[CH]C(Cl)(Cl)C=C(Cl)Cl H298:16.54 kcal/mol
library:CHOCl_G4 label:ODC(Cl)C[CH]Cl smiles:O=C(Cl)C[CH]Cl H298:-22.68 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:Cl[CH]C(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-12.59 kcal/mol
library:CHOCl_G4 label:Cl[CH]CCC(Cl)(Cl)Cl smiles:Cl[CH]CCC(Cl)(Cl)Cl H298:-8.51 kcal/mol
library:CHOCl_G4 label:OCC(Cl)[CH]Cl smiles:OCC(Cl)[CH]Cl H298:-32.02 kcal/mol
library:CHOCl_G4 label:ODCC(Cl)(Cl)[CH]Cl smiles:O=CC(Cl)(Cl)[CH]Cl H298:-15.43 kcal/mol
library:CHOCl_G4 label:CC(O)[CH]Cl smiles:CC(O)[CH]Cl H298:-26.04 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)(CCl)C(Cl)(Cl)Cl smiles:Cl[CH]C(Cl)(CCl)C(Cl)(Cl)Cl H298:-16.87 kcal/mol
library:CHOCl_G4 label:CC(Cl)(Cl)C[CH]Cl smiles:CC(Cl)(Cl)C[CH]Cl H298:-9.26 kcal/mol
library:CHOCl_G4 label:Cl[CH]CCCl smiles:Cl[CH]CCCl H298:6.51 kcal/mol
library:CHOCl_G4 label:ODC(Cl)C(Cl)[CH]Cl smiles:O=C(Cl)C(Cl)[CH]Cl H298:-25.61 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)C(Cl)Cl smiles:Cl[CH]C(Cl)C(Cl)Cl H298:-4.21 kcal/mol
library:CHOCl_G4 label:Cl[CH]CCC(Cl)Cl smiles:Cl[CH]CCC(Cl)Cl H298:-5.21 kcal/mol
library:CHOCl_G4 label:OC(Cl)(Cl)C[CH]Cl smiles:OC(Cl)(Cl)C[CH]Cl H298:-42.78 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)C(Cl)C(Cl)Cl smiles:Cl[CH]C(Cl)C(Cl)C(Cl)Cl H298:-16.78 kcal/mol
library:CHOCl_G4 label:Cl[CH]COCCl smiles:Cl[CH]COCCl H298:-22.13 kcal/mol
library:CHOCl_G4 label:Cl[CH]CCCCl smiles:Cl[CH]CCCCl H298:0.80 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)(Cl)C(Cl)OCl smiles:Cl[CH]C(Cl)(Cl)C(Cl)OCl H298:-8.09 kcal/mol
library:CHOCl_G4 label:CC[CH]Cl smiles:CC[CH]Cl H298:13.23 kcal/mol
library:CHOCl_G4 label:Cl[CH]CC(Cl)(Cl)OCl smiles:Cl[CH]CC(Cl)(Cl)OCl H298:-5.70 kcal/mol
library:CHOCl_G4 label:OC([CH]Cl)CCl smiles:OC([CH]Cl)CCl H298:-32.04 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)CC(Cl)Cl smiles:Cl[CH]C(Cl)CC(Cl)Cl H298:-13.51 kcal/mol
library:CHOCl_G4 label:CC(Cl)[CH]Cl smiles:CC(Cl)[CH]Cl H298:4.37 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)Cl smiles:Cl[CH]C(Cl)Cl H298:9.37 kcal/mol
library:CHOCl_G4 label:CC([CH]Cl)C(Cl)Cl smiles:CC([CH]Cl)C(Cl)Cl H298:-5.51 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(CCl)CCl smiles:Cl[CH]C(CCl)CCl H298:-6.66 kcal/mol
library:CHOCl_G4 label:OC(Cl)([CH]Cl)C(Cl)(Cl)Cl smiles:OC(Cl)([CH]Cl)C(Cl)(Cl)Cl H298:-46.81 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)(Cl)OC(Cl)Cl smiles:Cl[CH]C(Cl)(Cl)OC(Cl)Cl H298:-40.18 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)OCl smiles:Cl[CH]C(Cl)OCl H298:8.78 kcal/mol
library:CHOCl_G4 label:OOC[CH]Cl smiles:OOC[CH]Cl H298:1.65 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)(CCl)CCl smiles:Cl[CH]C(Cl)(CCl)CCl H298:-14.87 kcal/mol
library:CHOCl_G4 label:CC(Cl)C[CH]Cl smiles:CC(Cl)C[CH]Cl H298:-2.04 kcal/mol
library:CHOCl_G4 label:Cl[CH]COC(Cl)(Cl)Cl smiles:Cl[CH]COC(Cl)(Cl)Cl H298:-30.86 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)(Cl)CCl smiles:Cl[CH]C(Cl)(Cl)CCl H298:-5.01 kcal/mol
library:CHOCl_G4 label:OOC(Cl)[CH]Cl smiles:OOC(Cl)[CH]Cl H298:-7.54 kcal/mol
library:CHOCl_G4 label:Cl[CH]CC(Cl)(Cl)C(Cl)Cl smiles:Cl[CH]CC(Cl)(Cl)C(Cl)Cl H298:-16.18 kcal/mol
library:CHOCl_G4 label:CC(Cl)([CH]Cl)OCl smiles:CC(Cl)([CH]Cl)OCl H298:-2.98 kcal/mol
library:CHOCl_G4 label:C[CH]Cl smiles:C[CH]Cl H298:18.28 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)COCl smiles:Cl[CH]C(Cl)COCl H298:2.81 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)(OCl)C(Cl)Cl smiles:Cl[CH]C(Cl)(OCl)C(Cl)Cl H298:-8.33 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)(Cl)C(Cl)C(Cl)Cl smiles:Cl[CH]C(Cl)(Cl)C(Cl)C(Cl)Cl H298:-19.51 kcal/mol
library:CHOCl_G4 label:Cl[CH]CC(Cl)DC(Cl)Cl smiles:Cl[CH]CC(Cl)=C(Cl)Cl H298:20.03 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(CCl)C(Cl)Cl smiles:Cl[CH]C(CCl)C(Cl)Cl H298:-12.07 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)OOCl smiles:Cl[CH]C(Cl)OOCl H298:25.30 kcal/mol
library:CHOCl_G4 label:OC(Cl)([CH]Cl)C(Cl)Cl smiles:OC(Cl)([CH]Cl)C(Cl)Cl H298:-46.43 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:Cl[CH]C(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-14.19 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)(Cl)C(Cl)(Cl)C(Cl)Cl smiles:Cl[CH]C(Cl)(Cl)C(Cl)(Cl)C(Cl)Cl H298:-19.84 kcal/mol
library:CHOCl_G4 label:OOC(Cl)(Cl)[CH]Cl smiles:OOC(Cl)(Cl)[CH]Cl H298:-11.51 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)C(Cl)(Cl)Cl smiles:Cl[CH]C(Cl)C(Cl)(Cl)Cl H298:-6.26 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)(Cl)C(Cl)DC(Cl)Cl smiles:Cl[CH]C(Cl)(Cl)C(Cl)=C(Cl)Cl H298:15.14 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)(Cl)CDCCl smiles:Cl[CH]C(Cl)(Cl)C=CCl H298:19.81 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)(Cl)OOCl smiles:Cl[CH]C(Cl)(Cl)OOCl H298:21.50 kcal/mol
library:CHOCl_G4 label:COC[CH]Cl smiles:COC[CH]Cl H298:-13.66 kcal/mol
library:CHOCl_G4 label:Cl[CH]C(Cl)(Cl)COCl smiles:Cl[CH]C(Cl)(Cl)COCl H298:-1.03 kcal/mol
library:CHOFCl_G4 label:C#CC(F)(Cl)[CH]Cl smiles:C#CC(F)(Cl)[CH]Cl H298:32.15 kcal/mol
library:CHOFCl_G4 label:C#CC(F)(F)[CH]Cl smiles:C#CC(F)(F)[CH]Cl H298:-13.34 kcal/mol
library:CHOFCl_G4 label:FC#CC(F)[CH]Cl smiles:FC#CC(F)[CH]Cl H298:8.27 kcal/mol
library:CHOFCl_G4 label:FC#CC(Cl)[CH]Cl smiles:FC#CC(Cl)[CH]Cl H298:46.86 kcal/mol
library:CHOFCl_G4 label:C#CC(F)[CH]Cl smiles:C#CC(F)[CH]Cl H298:37.12 kcal/mol
library:CHOFCl_G4 label:FC#CC[CH]Cl smiles:FC#CC[CH]Cl H298:51.25 kcal/mol
library:CHOClBr_G4 label:ODCC(Cl)(Br)[CH]Cl smiles:O=CC(Cl)(Br)[CH]Cl H298:-4.37 kcal/mol
library:CHOClBr_G4 label:OCC(Br)[CH]Cl smiles:OCC(Br)[CH]Cl H298:-21.36 kcal/mol
library:CHOClBr_G4 label:Cl[CH]C(Cl)OOBr smiles:Cl[CH]C(Cl)OOBr H298:28.98 kcal/mol
library:CHOClBr_G4 label:Cl[CH]C(Br)(Br)OBr smiles:Cl[CH]C(Br)(Br)OBr H298:30.11 kcal/mol
library:CHOClBr_G4 label:Cl[CH]C(Cl)COBr smiles:Cl[CH]C(Cl)COBr H298:6.06 kcal/mol
library:CHOClBr_G4 label:CC(Br)C(Br)[CH]Cl smiles:CC(Br)C(Br)[CH]Cl H298:12.12 kcal/mol
library:CHOClBr_G4 label:Cl[CH]CC(Br)CBr smiles:Cl[CH]CC(Br)CBr H298:14.40 kcal/mol
library:CHOClBr_G4 label:CC(Cl)([CH]Cl)OBr smiles:CC(Cl)([CH]Cl)OBr H298:1.31 kcal/mol
library:CHOClBr_G4 label:Cl[CH]C(Cl)(Cl)CBr smiles:Cl[CH]C(Cl)(Cl)CBr H298:5.89 kcal/mol
library:CHOClBr_G4 label:Cl[CH]C(Cl)C(Br)Br smiles:Cl[CH]C(Cl)C(Br)Br H298:18.58 kcal/mol
library:CHOClBr_G4 label:Cl[CH]C(Cl)OBr smiles:Cl[CH]C(Cl)OBr H298:11.63 kcal/mol
library:CHOClBr_G4 label:Cl[CH]C(CCl)CBr smiles:Cl[CH]C(CCl)CBr H298:5.52 kcal/mol
library:CHOClBr_G4 label:Cl[CH]C(Br)(Br)Br smiles:Cl[CH]C(Br)(Br)Br H298:42.05 kcal/mol
library:CHOClBr_G4 label:CC([CH]Cl)C(Cl)Br smiles:CC([CH]Cl)C(Cl)Br H298:6.04 kcal/mol
library:CHOClBr_G4 label:CC(Cl)(Br)C[CH]Cl smiles:CC(Cl)(Br)C[CH]Cl H298:2.58 kcal/mol
library:CHOClBr_G4 label:Cl[CH]C(Cl)Br smiles:Cl[CH]C(Cl)Br H298:20.34 kcal/mol
library:CHOClBr_G4 label:OC(Br)(Br)[CH]Cl smiles:OC(Br)(Br)[CH]Cl H298:-9.15 kcal/mol
library:CHOClBr_G4 label:OC([CH]Cl)CBr smiles:OC([CH]Cl)CBr H298:-20.41 kcal/mol
library:CHOClBr_G4 label:ODC(Br)C[CH]Cl smiles:O=C(Br)C[CH]Cl H298:-10.46 kcal/mol
library:CHOClBr_G4 label:CC(Cl)(Br)[CH]Cl smiles:CC(Cl)(Br)[CH]Cl H298:9.95 kcal/mol
library:CHOClBr_G4 label:COC(Cl)(Br)[CH]Cl smiles:COC(Cl)(Br)[CH]Cl H298:-18.16 kcal/mol
library:CHOClBr_G4 label:Cl[CH]CCCBr smiles:Cl[CH]CCCBr H298:11.81 kcal/mol
library:CHOClBr_G4 label:OC([CH]Cl)C(Br)Br smiles:OC([CH]Cl)C(Br)Br H298:-13.37 kcal/mol
library:CHOClBr_G4 label:Cl[CH]COCBr smiles:Cl[CH]COCBr H298:-10.64 kcal/mol
library:CHOClBr_G4 label:CCC(Br)(Br)[CH]Cl smiles:CCC(Br)(Br)[CH]Cl H298:15.10 kcal/mol
library:CHOClBr_G4 label:Cl[CH]CCC(Cl)Br smiles:Cl[CH]CCC(Cl)Br H298:6.48 kcal/mol
library:CHOClBr_G4 label:Cl[CH]C(Cl)C(Cl)Br smiles:Cl[CH]C(Cl)C(Cl)Br H298:7.39 kcal/mol
library:CHOClBr_G4 label:CC(Br)C[CH]Cl smiles:CC(Br)C[CH]Cl H298:9.21 kcal/mol
library:CHOClBr_G4 label:Cl[CH]CCBr smiles:Cl[CH]CCBr H298:17.92 kcal/mol
library:CHOClBr_G4 label:OCC(Br)(Br)[CH]Cl smiles:OCC(Br)(Br)[CH]Cl H298:-15.53 kcal/mol
library:CHOClBr_G4 label:Cl[CH]CC(Br)(Br)Br smiles:Cl[CH]CC(Br)(Br)Br H298:33.78 kcal/mol
library:CHOClBr_G4 label:CC([CH]Cl)C(Br)Br smiles:CC([CH]Cl)C(Br)Br H298:17.64 kcal/mol
library:CHOClBr_G4 label:Cl[CH]C(Br)Br smiles:Cl[CH]C(Br)Br H298:31.39 kcal/mol
library:CHOClBr_G4 label:OOC(Br)[CH]Cl smiles:OOC(Br)[CH]Cl H298:4.29 kcal/mol
library:CHOClBr_G4 label:OC(Cl)(Br)C[CH]Cl smiles:OC(Cl)(Br)C[CH]Cl H298:-30.35 kcal/mol
library:CHOClBr_G4 label:OC([CH]Cl)C(Cl)Br smiles:OC([CH]Cl)C(Cl)Br H298:-25.41 kcal/mol
library:CHOClBr_G4 label:Cl[CH]CCC(Br)Br smiles:Cl[CH]CCC(Br)Br H298:17.96 kcal/mol
library:CHOClBr_G4 label:Cl[CH]C(Br)OBr smiles:Cl[CH]C(Br)OBr H298:23.34 kcal/mol
library:CHOClBr_G4 label:Cl[CH]C(CBr)CBr smiles:Cl[CH]C(CBr)CBr H298:15.14 kcal/mol
library:CHOClBr_G4 label:Cl[CH]CC(Cl)CBr smiles:Cl[CH]CC(Cl)CBr H298:3.97 kcal/mol
library:CHOClBr_G4 label:OC(Cl)([CH]Cl)OBr smiles:OC(Cl)([CH]Cl)OBr H298:-34.58 kcal/mol
library:CHOClBr_G4 label:OC(Br)C(Br)[CH]Cl smiles:OC(Br)C(Br)[CH]Cl H298:-19.97 kcal/mol
library:CHOClBr_G4 label:Cl[CH]C(Cl)(Br)CBr smiles:Cl[CH]C(Cl)(Br)CBr H298:16.70 kcal/mol
library:CHOClBr_G4 label:Cl[CH]C(Br)COBr smiles:Cl[CH]C(Br)COBr H298:15.91 kcal/mol
library:CHOClBr_G4 label:ODC(Br)C(Cl)[CH]Cl smiles:O=C(Br)C(Cl)[CH]Cl H298:-13.41 kcal/mol
library:CHOClBr_G4 label:Cl[CH]C(Br)OOBr smiles:Cl[CH]C(Br)OOBr H298:40.19 kcal/mol
library:CHOClBr_G4 label:CC(Br)[CH]Cl smiles:CC(Br)[CH]Cl H298:14.90 kcal/mol
library:CHOClBr_G4 label:CC([CH]Cl)OBr smiles:CC([CH]Cl)OBr H298:9.87 kcal/mol
library:CHOClBr_G4 label:CC([CH]Cl)CBr smiles:CC([CH]Cl)CBr H298:10.64 kcal/mol
library:CHOClBr_G4 label:Cl[CH]C(OCl)OBr smiles:Cl[CH]C(OCl)OBr H298:10.32 kcal/mol
library:CHOClBr_G4 label:Cl[CH]C(Br)OCBr smiles:Cl[CH]C(Br)OCBr H298:-9.42 kcal/mol
library:CHOClBr_G4 label:Cl[CH]CC(Cl)Br smiles:Cl[CH]CC(Cl)Br H298:12.79 kcal/mol
library:CHOClBr_G4 label:Cl[CH]COC(Cl)Br smiles:Cl[CH]COC(Cl)Br H298:-16.26 kcal/mol
library:CHOClBr_G4 label:Cl[CH]C(Br)CCBr smiles:Cl[CH]C(Br)CCBr H298:13.20 kcal/mol
library:CHOClBr_G4 label:OC(Br)(Br)C[CH]Cl smiles:OC(Br)(Br)C[CH]Cl H298:-18.13 kcal/mol
library:CHOClBr_G4 label:Cl[CH]C(Cl)(Br)OBr smiles:Cl[CH]C(Cl)(Br)OBr H298:18.45 kcal/mol
library:CHOClBr_G4 label:Cl[CH]C(Cl)(Br)Br smiles:Cl[CH]C(Cl)(Br)Br H298:30.49 kcal/mol
library:CHOClBr_G4 label:Cl[CH]CC(Cl)(Cl)Br smiles:Cl[CH]CC(Cl)(Cl)Br H298:10.14 kcal/mol
library:CHOClBr_G4 label:Cl[CH]CC(Cl)OBr smiles:Cl[CH]CC(Cl)OBr H298:2.94 kcal/mol
library:CHOClBr_G4 label:OC(Cl)([CH]Cl)CBr smiles:OC(Cl)([CH]Cl)CBr H298:-31.48 kcal/mol
library:CHOClBr_G4 label:Cl[CH]C(Br)CBr smiles:Cl[CH]C(Br)CBr H298:20.28 kcal/mol
library:CHOClBr_G4 label:Cl[CH]C(CBr)OBr smiles:Cl[CH]C(CBr)OBr H298:16.48 kcal/mol
library:CHOClBr_G4 label:CC(C)(Br)[CH]Cl smiles:CC(C)(Br)[CH]Cl H298:6.09 kcal/mol
library:CHOClBr_G4 label:CC(Br)C(Cl)[CH]Cl smiles:CC(Br)C(Cl)[CH]Cl H298:1.69 kcal/mol
library:CHOClBr_G4 label:OCC(Cl)(Br)[CH]Cl smiles:OCC(Cl)(Br)[CH]Cl H298:-26.55 kcal/mol
library:CHOClBr_G4 label:CCC(Br)[CH]Cl smiles:CCC(Br)[CH]Cl H298:8.86 kcal/mol
library:CHOClBr_G4 label:Cl[CH]COBr smiles:Cl[CH]COBr H298:19.95 kcal/mol
library:CHOClBr_G4 label:Cl[CH]C(Br)C(Br)Br smiles:Cl[CH]C(Br)C(Br)Br H298:28.68 kcal/mol
library:CHOClBr_G4 label:ODCC(Br)[CH]Cl smiles:O=CC(Br)[CH]Cl H298:-0.83 kcal/mol
library:CHOClBr_G4 label:Cl[CH]COOBr smiles:Cl[CH]COOBr H298:35.42 kcal/mol
library:CHOClBr_G4 label:ODC(Br)C(Br)[CH]Cl smiles:O=C(Br)C(Br)[CH]Cl H298:-3.78 kcal/mol
library:CHOClBr_G4 label:Cl[CH]CCOBr smiles:Cl[CH]CCOBr H298:13.55 kcal/mol
library:CHOClBr_G4 label:OC([CH]Cl)OBr smiles:OC([CH]Cl)OBr H298:-25.58 kcal/mol
library:CHOClBr_G4 label:Cl[CH]CBr smiles:Cl[CH]CBr H298:23.07 kcal/mol
library:CHOClBr_G4 label:CCC(Cl)(Br)[CH]Cl smiles:CCC(Cl)(Br)[CH]Cl H298:3.63 kcal/mol
library:CHOClBr_G4 label:OC(Br)C(Cl)[CH]Cl smiles:OC(Br)C(Cl)[CH]Cl H298:-30.15 kcal/mol
library:CHOClBr_G4 label:Cl[CH]C(Cl)CBr smiles:Cl[CH]C(Cl)CBr H298:10.15 kcal/mol
library:CHOClBr_G4 label:COC(Br)(Br)[CH]Cl smiles:COC(Br)(Br)[CH]Cl H298:-6.82 kcal/mol
library:CHOClBr_G4 label:Cl[CH]C(CCl)OBr smiles:Cl[CH]C(CCl)OBr H298:5.60 kcal/mol
library:CHOClBr_G4 label:CC(Br)(Br)[CH]Cl smiles:CC(Br)(Br)[CH]Cl H298:21.24 kcal/mol
library:CHOClBr_G4 label:OC(Cl)(Br)[CH]Cl smiles:OC(Cl)(Br)[CH]Cl H298:-20.90 kcal/mol
library:CHOClBr_G4 label:Cl[CH]C(Cl)(Cl)OBr smiles:Cl[CH]C(Cl)(Cl)OBr H298:6.89 kcal/mol
library:CHOClBr_G4 label:CC(Br)(Br)C[CH]Cl smiles:CC(Br)(Br)C[CH]Cl H298:14.38 kcal/mol
library:CHOClBr_G4 label:ODCC(Br)(Br)[CH]Cl smiles:O=CC(Br)(Br)[CH]Cl H298:5.55 kcal/mol
library:CHOClBr_G4 label:CC(Cl)([CH]Cl)CBr smiles:CC(Cl)([CH]Cl)CBr H298:0.18 kcal/mol
library:CHOClBr_G4 label:Cl[CH]COC(Br)Br smiles:Cl[CH]COC(Br)Br H298:-4.42 kcal/mol
library:CHOClBr_G4 label:Cl[CH]CC(Br)OBr smiles:Cl[CH]CC(Br)OBr H298:14.57 kcal/mol
library:CHOClBr_G4 label:Cl[CH]CC(Br)Br smiles:Cl[CH]CC(Br)Br H298:24.32 kcal/mol
library:CHOClBr_G4 label:Cl[CH]C(Cl)CCBr smiles:Cl[CH]C(Cl)CCBr H298:3.06 kcal/mol
library:CHOClBr_G4 label:OC(Br)C[CH]Cl smiles:OC(Br)C[CH]Cl H298:-22.72 kcal/mol
library:CHOClBr_G4 label:Cl[CH]C(Br)(Br)CBr smiles:Cl[CH]C(Br)(Br)CBr H298:28.11 kcal/mol
library:CHOClBr_G4 label:Cl[CH]C(Cl)OCBr smiles:Cl[CH]C(Cl)OCBr H298:-20.46 kcal/mol
library:CHOClBr_G4 label:Cl[CH]C(OBr)OBr smiles:Cl[CH]C(OBr)OBr H298:12.13 kcal/mol
library:CHOClBr_G4 label:Cl[CH]C(Cl)(Cl)Br smiles:Cl[CH]C(Cl)(Cl)Br H298:19.03 kcal/mol
library:CHOClBr_G4 label:Cl[CH]CC(Cl)(Br)Br smiles:Cl[CH]CC(Cl)(Br)Br H298:22.01 kcal/mol
""",
)

entry(
    index = 81,
    label = "CsCsF1sH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   H   u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.207512,-0.677416,-1.44112,-2.06484,-3.02331,-3.7022,-4.68962],'cal/(mol*K)','+|-',[0.045352,0.0465649,0.0436603,0.0407798,0.035989,0.031493,0.0230662]),
        H298 = (98.9178,'kcal/mol','+|-',0.0724494),
        S298 = (3.50882,'cal/(mol*K)','+|-',0.123125),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:F[CH]COF smiles:F[CH]COF H298:-24.66 kcal/mol
library:CHOF_G4 label:F[CH]CC(F)(F)F smiles:F[CH]CC(F)(F)F H298:-180.60 kcal/mol
library:CHOF_G4 label:OC([CH]F)OF smiles:OC([CH]F)OF H298:-67.42 kcal/mol
library:CHOF_G4 label:F[CH]C(F)COF smiles:F[CH]C(F)COF H298:-74.97 kcal/mol
library:CHOF_G4 label:F[CH]C(F)(F)C(F)(F)C(F)F smiles:F[CH]C(F)(F)C(F)(F)C(F)F H298:-314.34 kcal/mol
library:CHOF_G4 label:C#CC[CH]F smiles:C#CC[CH]F H298:43.67 kcal/mol
library:CHOF_G4 label:CC(F)[CH]F smiles:CC(F)[CH]F H298:-70.30 kcal/mol
library:CHOF_G4 label:OCC(F)(F)[CH]F smiles:OCC(F)(F)[CH]F H298:-158.03 kcal/mol
library:CHOF_G4 label:CDCC[CH]F smiles:C=CC[CH]F H298:1.82 kcal/mol
library:CHOF_G4 label:F[CH]CCOF smiles:F[CH]CCOF H298:-32.51 kcal/mol
library:CHOF_G4 label:F[CH]C(F)(F)OF smiles:F[CH]C(F)(F)OF H298:-125.74 kcal/mol
library:CHOF_G4 label:F[CH]CCF smiles:F[CH]CCF H298:-67.41 kcal/mol
library:CHOF_G4 label:OC([CH]F)CF smiles:OC([CH]F)CF H298:-104.87 kcal/mol
library:CHOF_G4 label:OC(F)C(F)(F)[CH]F smiles:OC(F)C(F)(F)[CH]F H298:-210.08 kcal/mol
library:CHOF_G4 label:CDC(F)C(F)[CH]F smiles:C=C(F)C(F)[CH]F H298:-89.54 kcal/mol
library:CHOF_G4 label:F[CH]C(F)CCF smiles:F[CH]C(F)CCF H298:-119.94 kcal/mol
library:CHOF_G4 label:F[CH]C(OF)OF smiles:F[CH]C(OF)OF H298:-34.64 kcal/mol
library:CHOF_G4 label:OCC(F)[CH]F smiles:OCC(F)[CH]F H298:-105.66 kcal/mol
library:CHOF_G4 label:F[CH]CC(F)(F)C(F)F smiles:F[CH]CC(F)(F)C(F)F H298:-225.81 kcal/mol
library:CHOF_G4 label:F[CH]C(F)C(F)(F)F smiles:F[CH]C(F)C(F)(F)F H298:-220.98 kcal/mol
library:CHOF_G4 label:F[CH]C(F)(F)C(F)DCF smiles:F[CH]C(F)(F)C(F)=CF H298:-179.83 kcal/mol
library:CHOF_G4 label:F[CH]C(F)OC(F)F smiles:F[CH]C(F)OC(F)F H298:-208.35 kcal/mol
library:CHOF_G4 label:F[CH]CCCF smiles:F[CH]CCCF H298:-73.38 kcal/mol
library:CHOF_G4 label:F[CH]C(F)(F)CF smiles:F[CH]C(F)(F)CF H298:-163.69 kcal/mol
library:CHOF_G4 label:F[CH]C(F)(F)OC(F)F smiles:F[CH]C(F)(F)OC(F)F H298:-262.70 kcal/mol
library:CHOF_G4 label:CC(F)([CH]F)C(F)F smiles:CC(F)([CH]F)C(F)F H298:-175.26 kcal/mol
library:CHOF_G4 label:CC(C)(F)[CH]F smiles:CC(C)(F)[CH]F H298:-80.64 kcal/mol
library:CHOF_G4 label:ODCC[CH]F smiles:O=CC[CH]F H298:-40.95 kcal/mol
library:CHOF_G4 label:F[CH]CC(F)(F)C(F)(F)F smiles:F[CH]CC(F)(F)C(F)(F)F H298:-281.82 kcal/mol
library:CHOF_G4 label:F[CH]C(F)(F)OOF smiles:F[CH]C(F)(F)OOF H298:-114.08 kcal/mol
library:CHOF_G4 label:F[CH]C(F)(F)C(F)C(F)F smiles:F[CH]C(F)(F)C(F)C(F)F H298:-264.82 kcal/mol
library:CHOF_G4 label:FC#CC(F)(F)[CH]F smiles:FC#CC(F)(F)[CH]F H298:-77.40 kcal/mol
library:CHOF_G4 label:ODCC(F)[CH]F smiles:O=CC(F)[CH]F H298:-83.51 kcal/mol
library:CHOF_G4 label:OCC[CH]F smiles:OCC[CH]F H298:-58.47 kcal/mol
library:CHOF_G4 label:CC(F)(F)C(F)(F)[CH]F smiles:CC(F)(F)C(F)(F)[CH]F H298:-228.05 kcal/mol
library:CHOF_G4 label:F[CH]C(F)(F)OCF smiles:F[CH]C(F)(F)OCF H298:-207.07 kcal/mol
library:CHOF_G4 label:F[CH]C(F)(CF)CF smiles:F[CH]C(F)(CF)CF H298:-163.55 kcal/mol
library:CHOF_G4 label:OOC(F)[CH]F smiles:OOC(F)[CH]F H298:-85.45 kcal/mol
library:CHOF_G4 label:COC(F)(F)[CH]F smiles:COC(F)(F)[CH]F H298:-159.18 kcal/mol
library:CHOF_G4 label:F[CH]C(F)OC(F)(F)F smiles:F[CH]C(F)OC(F)(F)F H298:-264.72 kcal/mol
library:CHOF_G4 label:F[CH]CC(F)(F)CF smiles:F[CH]CC(F)(F)CF H298:-174.48 kcal/mol
library:CHOF_G4 label:F[CH]C(CF)C(F)F smiles:F[CH]C(CF)C(F)F H298:-169.70 kcal/mol
library:CHOF_G4 label:F[CH]C(F)C(F)C(F)(F)F smiles:F[CH]C(F)C(F)C(F)(F)F H298:-271.62 kcal/mol
library:CHOF_G4 label:OC([CH]F)C(F)F smiles:OC([CH]F)C(F)F H298:-157.76 kcal/mol
library:CHOF_G4 label:F[CH]C(F)(F)C(F)DC(F)F smiles:F[CH]C(F)(F)C(F)=C(F)F H298:-222.77 kcal/mol
library:CHOF_G4 label:OC(F)(F)C[CH]F smiles:OC(F)(F)C[CH]F H298:-175.15 kcal/mol
library:CHOF_G4 label:F[CH]CC(F)OF smiles:F[CH]CC(F)OF H298:-84.05 kcal/mol
library:CHOF_G4 label:OC(F)([CH]F)C(F)F smiles:OC(F)([CH]F)C(F)F H298:-211.05 kcal/mol
library:CHOF_G4 label:OC(F)[CH]F smiles:OC(F)[CH]F H298:-105.51 kcal/mol
library:CHOF_G4 label:F[CH]CC(F)(F)OF smiles:F[CH]CC(F)(F)OF H298:-138.09 kcal/mol
library:CHOF_G4 label:OC(F)(F)C(F)(F)[CH]F smiles:OC(F)(F)C(F)(F)[CH]F H298:-265.31 kcal/mol
library:CHOF_G4 label:F[CH]CC(F)DC(F)F smiles:F[CH]CC(F)=C(F)F H298:-132.22 kcal/mol
library:CHOF_G4 label:F[CH]C(F)(F)CC(F)F smiles:F[CH]C(F)(F)CC(F)F H298:-225.63 kcal/mol
library:CHOF_G4 label:CDC(F)C(F)(F)[CH]F smiles:C=C(F)C(F)(F)[CH]F H298:-140.49 kcal/mol
library:CHOF_G4 label:F[CH]CCC(F)(F)F smiles:F[CH]CCC(F)(F)F H298:-187.82 kcal/mol
library:CHOF_G4 label:F[CH]CC(F)CF smiles:F[CH]CC(F)CF H298:-119.81 kcal/mol
library:CHOF_G4 label:F[CH]C(F)CC(F)(F)F smiles:F[CH]C(F)CC(F)(F)F H298:-232.55 kcal/mol
library:CHOF_G4 label:F[CH]CCDC(F)F smiles:F[CH]CC=C(F)F H298:-92.15 kcal/mol
library:CHOF_G4 label:F[CH]C(F)(C(F)F)C(F)(F)F smiles:F[CH]C(F)(C(F)F)C(F)(F)F H298:-321.14 kcal/mol
library:CHOF_G4 label:CC(F)C(F)(F)[CH]F smiles:CC(F)C(F)(F)[CH]F H298:-173.66 kcal/mol
library:CHOF_G4 label:CDCC(F)[CH]F smiles:C=CC(F)[CH]F H298:-43.73 kcal/mol
library:CHOF_G4 label:OOC[CH]F smiles:OOC[CH]F H298:-34.42 kcal/mol
library:CHOF_G4 label:F[CH]C(F)C(F)(F)OF smiles:F[CH]C(F)C(F)(F)OF H298:-177.20 kcal/mol
library:CHOF_G4 label:F[CH]C(F)CC(F)F smiles:F[CH]C(F)CC(F)F H298:-174.28 kcal/mol
library:CHOF_G4 label:F[CH]C(F)OF smiles:F[CH]C(F)OF H298:-73.51 kcal/mol
library:CHOF_G4 label:F[CH]C(F)(C(F)F)C(F)F smiles:F[CH]C(F)(C(F)F)C(F)F H298:-265.41 kcal/mol
library:CHOF_G4 label:CC(F)([CH]F)OF smiles:CC(F)([CH]F)OF H298:-85.62 kcal/mol
library:CHOF_G4 label:F[CH]C(CF)C(F)(F)F smiles:F[CH]C(CF)C(F)(F)F H298:-228.04 kcal/mol
library:CHOF_G4 label:CC(F)C[CH]F smiles:CC(F)C[CH]F H298:-77.59 kcal/mol
library:CHOF_G4 label:CC(O)(F)[CH]F smiles:CC(O)(F)[CH]F H298:-118.02 kcal/mol
library:CHOF_G4 label:F[CH]C(F)CDC(F)F smiles:F[CH]C(F)C=C(F)F H298:-137.39 kcal/mol
library:CHOF_G4 label:OC(F)(F)[CH]F smiles:OC(F)(F)[CH]F H298:-163.58 kcal/mol
library:CHOF_G4 label:F[CH]COC(F)(F)F smiles:F[CH]COC(F)(F)F H298:-216.43 kcal/mol
library:CHOF_G4 label:F[CH]C(F)C(F)(F)CF smiles:F[CH]C(F)C(F)(F)CF H298:-217.23 kcal/mol
library:CHOF_G4 label:F[CH]C(F)(CF)C(F)F smiles:F[CH]C(F)(CF)C(F)F H298:-215.81 kcal/mol
library:CHOF_G4 label:CC(F)([CH]F)CF smiles:CC(F)([CH]F)CF H298:-122.62 kcal/mol
library:CHOF_G4 label:ODCC(F)(F)[CH]F smiles:O=CC(F)(F)[CH]F H298:-132.34 kcal/mol
library:CHOF_G4 label:F[CH]C(F)CF smiles:F[CH]C(F)CF H298:-111.27 kcal/mol
library:CHOF_G4 label:CC(F)C(F)[CH]F smiles:CC(F)C(F)[CH]F H298:-122.55 kcal/mol
library:CHOF_G4 label:OC(F)([CH]F)CF smiles:OC(F)([CH]F)CF H298:-159.33 kcal/mol
library:CHOF_G4 label:F[CH]CC(F)DCF smiles:F[CH]CC(F)=CF H298:-86.81 kcal/mol
library:CHOF_G4 label:OC(F)C(F)[CH]F smiles:OC(F)C(F)[CH]F H298:-160.00 kcal/mol
library:CHOF_G4 label:F[CH]CCDCF smiles:F[CH]CC=CF H298:-43.31 kcal/mol
library:CHOF_G4 label:CCC[CH]F smiles:CCC[CH]F H298:-28.13 kcal/mol
library:CHOF_G4 label:F[CH]C(F)C(F)CF smiles:F[CH]C(F)C(F)CF H298:-163.38 kcal/mol
library:CHOF_G4 label:F[CH]C(F)C(F)(F)C(F)(F)F smiles:F[CH]C(F)C(F)(F)C(F)(F)F H298:-321.45 kcal/mol
library:CHOF_G4 label:OC(F)([CH]F)C(F)(F)F smiles:OC(F)([CH]F)C(F)(F)F H298:-266.55 kcal/mol
library:CHOF_G4 label:F[CH]C(F)(F)F smiles:F[CH]C(F)(F)F H298:-168.39 kcal/mol
library:CHOF_G4 label:OC(F)([CH]F)OF smiles:OC(F)([CH]F)OF H298:-120.67 kcal/mol
library:CHOF_G4 label:OC(F)(F)C(F)[CH]F smiles:OC(F)(F)C(F)[CH]F H298:-216.21 kcal/mol
library:CHOF_G4 label:CDCC(F)(F)[CH]F smiles:C=CC(F)(F)[CH]F H298:-95.75 kcal/mol
library:CHOF_G4 label:F[CH]C(F)C(F)DCF smiles:F[CH]C(F)C(F)=CF H298:-128.61 kcal/mol
library:CHOF_G4 label:F[CH]C(F)C(F)OF smiles:F[CH]C(F)C(F)OF H298:-125.40 kcal/mol
library:CHOF_G4 label:F[CH]CC(F)F smiles:F[CH]CC(F)F H298:-121.62 kcal/mol
library:CHOF_G4 label:F[CH]C(F)C(F)C(F)F smiles:F[CH]C(F)C(F)C(F)F H298:-214.31 kcal/mol
library:CHOF_G4 label:CC([CH]F)C(F)(F)F smiles:CC([CH]F)C(F)(F)F H298:-187.16 kcal/mol
library:CHOF_G4 label:F[CH]C(F)(F)C(F)OF smiles:F[CH]C(F)(F)C(F)OF H298:-174.03 kcal/mol
library:CHOF_G4 label:F[CH]C(F)F smiles:F[CH]C(F)F H298:-111.16 kcal/mol
library:CHOF_G4 label:F[CH]CC(F)C(F)F smiles:F[CH]CC(F)C(F)F H298:-172.13 kcal/mol
library:CHOF_G4 label:F[CH]C(F)(F)CDCF smiles:F[CH]C(F)(F)C=CF H298:-140.31 kcal/mol
library:CHOF_G4 label:CC([CH]F)OF smiles:CC([CH]F)OF H298:-33.28 kcal/mol
library:CHOF_G4 label:CDC(F)C[CH]F smiles:C=C(F)C[CH]F H298:-46.13 kcal/mol
library:CHOF_G4 label:CC[CH]F smiles:CC[CH]F H298:-22.83 kcal/mol
library:CHOF_G4 label:ODC(F)C(F)(F)[CH]F smiles:O=C(F)C(F)(F)[CH]F H298:-192.64 kcal/mol
library:CHOF_G4 label:F[CH]C(F)CDCF smiles:F[CH]C(F)C=CF H298:-88.00 kcal/mol
library:CHOF_G4 label:CC([CH]F)C(F)F smiles:CC([CH]F)C(F)F H298:-128.23 kcal/mol
library:CHOF_G4 label:F[CH]C(C(F)(F)F)C(F)(F)F smiles:F[CH]C(C(F)(F)F)C(F)(F)F H298:-337.43 kcal/mol
library:CHOF_G4 label:F[CH]C(F)(F)C(F)CF smiles:F[CH]C(F)(F)C(F)CF H298:-215.07 kcal/mol
library:CHOF_G4 label:CC(O)[CH]F smiles:CC(O)[CH]F H298:-61.85 kcal/mol
library:CHOF_G4 label:CC(F)(F)C[CH]F smiles:CC(F)(F)C[CH]F H298:-134.31 kcal/mol
library:CHOF_G4 label:F[CH]C(F)C(F)(F)C(F)F smiles:F[CH]C(F)C(F)(F)C(F)F H298:-266.91 kcal/mol
library:CHOF_G4 label:OOC(F)(F)[CH]F smiles:OOC(F)(F)[CH]F H298:-139.90 kcal/mol
library:CHOF_G4 label:CCC(F)[CH]F smiles:CCC(F)[CH]F H298:-74.93 kcal/mol
library:CHOF_G4 label:F[CH]CCC(F)F smiles:F[CH]CCC(F)F H298:-128.30 kcal/mol
library:CHOF_G4 label:CC([CH]F)CF smiles:CC([CH]F)CF H298:-73.78 kcal/mol
library:CHOF_G4 label:F[CH]C(F)(F)C(F)(F)OF smiles:F[CH]C(F)(F)C(F)(F)OF H298:-225.13 kcal/mol
library:CHOF_G4 label:F[CH]C(C(F)F)C(F)F smiles:F[CH]C(C(F)F)C(F)F H298:-223.35 kcal/mol
library:CHOF_G4 label:F[CH]C(F)(F)CCF smiles:F[CH]C(F)(F)CCF H298:-172.29 kcal/mol
library:CHOF_G4 label:F[CH]C(F)(OF)OF smiles:F[CH]C(F)(OF)OF H298:-82.80 kcal/mol
library:CHOF_G4 label:C#CC(F)(F)[CH]F smiles:C#CC(F)(F)[CH]F H298:-48.27 kcal/mol
library:CHOF_G4 label:F[CH]COC(F)F smiles:F[CH]COC(F)F H298:-159.25 kcal/mol
library:CHOF_G4 label:F[CH]C(F)(F)CC(F)(F)F smiles:F[CH]C(F)(F)CC(F)(F)F H298:-283.32 kcal/mol
library:CHOF_G4 label:F[CH]C(F)(C(F)(F)F)C(F)(F)F smiles:F[CH]C(F)(C(F)(F)F)C(F)(F)F H298:-375.89 kcal/mol
library:CHOF_G4 label:OC(O)(F)[CH]F smiles:OC(O)(F)[CH]F H298:-156.80 kcal/mol
library:CHOF_G4 label:CC(F)(F)[CH]F smiles:CC(F)(F)[CH]F H298:-124.31 kcal/mol
library:CHOF_G4 label:F[CH]C(F)(F)C(F)(F)CF smiles:F[CH]C(F)(F)C(F)(F)CF H298:-265.21 kcal/mol
library:CHOF_G4 label:F[CH]C(F)(F)COF smiles:F[CH]C(F)(F)COF H298:-127.56 kcal/mol
library:CHOF_G4 label:OC([CH]F)C(F)(F)F smiles:OC([CH]F)C(F)(F)F H298:-215.40 kcal/mol
library:CHOF_G4 label:F[CH]C(F)C(F)DC(F)F smiles:F[CH]C(F)C(F)=C(F)F H298:-174.42 kcal/mol
library:CHOF_G4 label:FC#CC(F)[CH]F smiles:FC#CC(F)[CH]F H298:-27.63 kcal/mol
library:CHOF_G4 label:OC(F)C[CH]F smiles:OC(F)C[CH]F H298:-115.32 kcal/mol
library:CHOF_G4 label:F[CH]CF smiles:F[CH]CF H298:-60.44 kcal/mol
library:CHOF_G4 label:F[CH]C(F)(CF)C(F)(F)F smiles:F[CH]C(F)(CF)C(F)(F)F H298:-271.00 kcal/mol
library:CHOF_G4 label:F[CH]C(OF)C(F)(F)F smiles:F[CH]C(OF)C(F)(F)F H298:-182.95 kcal/mol
library:CHOF_G4 label:F[CH]C(C(F)F)C(F)(F)F smiles:F[CH]C(C(F)F)C(F)(F)F H298:-280.56 kcal/mol
library:CHOF_G4 label:C[CH]F smiles:C[CH]F H298:-18.29 kcal/mol
library:CHOF_G4 label:COC[CH]F smiles:COC[CH]F H298:-48.06 kcal/mol
library:CHOF_G4 label:CC(C)[CH]F smiles:CC(C)[CH]F H298:-29.44 kcal/mol
library:CHOF_G4 label:F[CH]COCF smiles:F[CH]COCF H298:-100.52 kcal/mol
library:CHOF_G4 label:F[CH]C(F)(F)C(F)F smiles:F[CH]C(F)(F)C(F)F H298:-213.84 kcal/mol
library:CHOF_G4 label:OC(O)[CH]F smiles:OC(O)[CH]F H298:-98.31 kcal/mol
library:CHOF_G4 label:F[CH]C(F)(F)OC(F)(F)F smiles:F[CH]C(F)(F)OC(F)(F)F H298:-316.68 kcal/mol
library:CHOF_G4 label:F[CH]C(F)(F)C(F)(F)C(F)(F)F smiles:F[CH]C(F)(F)C(F)(F)C(F)(F)F H298:-368.86 kcal/mol
library:CHOF_G4 label:F[CH]C(F)(F)C(F)(F)F smiles:F[CH]C(F)(F)C(F)(F)F H298:-269.69 kcal/mol
library:CHOF_G4 label:F[CH]CC(F)C(F)(F)F smiles:F[CH]CC(F)C(F)(F)F H298:-230.69 kcal/mol
library:CHOF_G4 label:C#CC(F)[CH]F smiles:C#CC(F)[CH]F H298:1.18 kcal/mol
library:CHOF_G4 label:COC(F)[CH]F smiles:COC(F)[CH]F H298:-102.10 kcal/mol
library:CHOF_G4 label:F[CH]C(F)OCF smiles:F[CH]C(F)OCF H298:-152.52 kcal/mol
library:CHOF_G4 label:F[CH]C(CF)CF smiles:F[CH]C(CF)CF H298:-117.90 kcal/mol
library:CHOF_G4 label:CC(F)(F)C(F)[CH]F smiles:CC(F)(F)C(F)[CH]F H298:-176.52 kcal/mol
library:CHOF_G4 label:F[CH]COOF smiles:F[CH]COOF H298:-14.74 kcal/mol
library:CHOF_G4 label:CCC(F)(F)[CH]F smiles:CCC(F)(F)[CH]F H298:-129.52 kcal/mol
library:CHOF_G4 label:ODC(F)C(F)[CH]F smiles:O=C(F)C(F)[CH]F H298:-144.49 kcal/mol
library:CHOF_G4 label:F[CH]C(OF)C(F)F smiles:F[CH]C(OF)C(F)F H298:-127.07 kcal/mol
library:CHOF_G4 label:F[CH]C(F)(F)CDC(F)F smiles:F[CH]C(F)(F)C=C(F)F H298:-188.24 kcal/mol
library:CHOF_G4 label:F[CH]C(F)(F)C(F)C(F)(F)F smiles:F[CH]C(F)(F)C(F)C(F)(F)F H298:-320.46 kcal/mol
library:CHOF_G4 label:CC(F)([CH]F)C(F)(F)F smiles:CC(F)([CH]F)C(F)(F)F H298:-232.45 kcal/mol
library:CHOF_G4 label:FC#CC[CH]F smiles:FC#CC[CH]F H298:15.36 kcal/mol
library:CHOF_G4 label:OC[CH]F smiles:OC[CH]F H298:-52.44 kcal/mol
library:CHOF_G4 label:F[CH]C(F)C(F)F smiles:F[CH]C(F)C(F)F H298:-163.58 kcal/mol
library:CHOF_G4 label:F[CH]C(CF)OF smiles:F[CH]C(CF)OF H298:-74.85 kcal/mol
library:CHOF_G4 label:ODC(F)C[CH]F smiles:O=C(F)C[CH]F H298:-105.47 kcal/mol
library:CHOF_G4 label:F[CH]C(F)OOF smiles:F[CH]C(F)OOF H298:-62.15 kcal/mol
library:CHOFCl_G4 label:F[CH]COCCl smiles:F[CH]COCCl H298:-57.66 kcal/mol
library:CHOFCl_G4 label:F[CH]C(Cl)COCl smiles:F[CH]C(Cl)COCl H298:-32.90 kcal/mol
library:CHOFCl_G4 label:F[CH]C(Cl)OCl smiles:F[CH]C(Cl)OCl H298:-26.11 kcal/mol
library:CHOFCl_G4 label:CC([CH]F)CCl smiles:CC([CH]F)CCl H298:-35.72 kcal/mol
library:CHOFCl_G4 label:F[CH]CC(F)CCl smiles:F[CH]CC(F)CCl H298:-83.67 kcal/mol
library:CHOFCl_G4 label:F[CH]C(Cl)OOCl smiles:F[CH]C(Cl)OOCl H298:-10.35 kcal/mol
library:CHOFCl_G4 label:F[CH]CCCCl smiles:F[CH]CCCCl H298:-35.06 kcal/mol
library:CHOFCl_G4 label:CC(C)(Cl)[CH]F smiles:CC(C)(Cl)[CH]F H298:-40.81 kcal/mol
library:CHOFCl_G4 label:F[CH]C(F)(F)CCl smiles:F[CH]C(F)(F)CCl H298:-125.94 kcal/mol
library:CHOFCl_G4 label:F[CH]C(F)(Cl)OCl smiles:F[CH]C(F)(Cl)OCl H298:-75.21 kcal/mol
library:CHOFCl_G4 label:F[CH]COC(F)Cl smiles:F[CH]COC(F)Cl H298:-110.26 kcal/mol
library:CHOFCl_G4 label:OC(F)(Cl)[CH]F smiles:OC(F)(Cl)[CH]F H298:-114.28 kcal/mol
library:CHOFCl_G4 label:CC(Cl)[CH]F smiles:CC(Cl)[CH]F H298:-31.53 kcal/mol
library:CHOFCl_G4 label:F[CH]C(CCl)CCl smiles:F[CH]C(CCl)CCl H298:-41.98 kcal/mol
library:CHOFCl_G4 label:OC(Cl)(Cl)[CH]F smiles:OC(Cl)(Cl)[CH]F H298:-68.07 kcal/mol
library:CHOFCl_G4 label:OC(Cl)(Cl)C[CH]F smiles:OC(Cl)(Cl)C[CH]F H298:-78.33 kcal/mol
library:CHOFCl_G4 label:F[CH]CCC(Cl)Cl smiles:F[CH]CCC(Cl)Cl H298:-41.08 kcal/mol
library:CHOFCl_G4 label:F[CH]COCl smiles:F[CH]COCl H298:-19.44 kcal/mol
library:CHOFCl_G4 label:F[CH]C(F)CCCl smiles:F[CH]C(F)CCCl H298:-81.88 kcal/mol
library:CHOFCl_G4 label:CC(F)(Cl)C[CH]F smiles:CC(F)(Cl)C[CH]F H298:-87.80 kcal/mol
library:CHOFCl_G4 label:F[CH]C(F)OCCl smiles:F[CH]C(F)OCCl H298:-109.45 kcal/mol
library:CHOFCl_G4 label:CCC(Cl)[CH]F smiles:CCC(Cl)[CH]F H298:-36.88 kcal/mol
library:CHOFCl_G4 label:F[CH]C(Cl)(Cl)CCl smiles:F[CH]C(Cl)(Cl)CCl H298:-39.95 kcal/mol
library:CHOFCl_G4 label:F[CH]C(OF)OCl smiles:F[CH]C(OF)OCl H298:-30.81 kcal/mol
library:CHOFCl_G4 label:F[CH]C(F)OCl smiles:F[CH]C(F)OCl H298:-69.10 kcal/mol
library:CHOFCl_G4 label:F[CH]C(CF)OCl smiles:F[CH]C(CF)OCl H298:-69.45 kcal/mol
library:CHOFCl_G4 label:ODCC(Cl)(Cl)[CH]F smiles:O=CC(Cl)(Cl)[CH]F H298:-49.85 kcal/mol
library:CHOFCl_G4 label:CC(F)([CH]F)OCl smiles:CC(F)([CH]F)OCl H298:-80.61 kcal/mol
library:CHOFCl_G4 label:ODC(Cl)C(Cl)[CH]F smiles:O=C(Cl)C(Cl)[CH]F H298:-60.61 kcal/mol
library:CHOFCl_G4 label:CCC(F)(Cl)[CH]F smiles:CCC(F)(Cl)[CH]F H298:-84.04 kcal/mol
library:CHOFCl_G4 label:F[CH]CCC(F)Cl smiles:F[CH]CCC(F)Cl H298:-82.50 kcal/mol
library:CHOFCl_G4 label:CC(Cl)([CH]F)CCl smiles:CC(Cl)([CH]F)CCl H298:-45.91 kcal/mol
library:CHOFCl_G4 label:OC([CH]F)CCl smiles:OC([CH]F)CCl H298:-66.21 kcal/mol
library:CHOFCl_G4 label:OC(O)(Cl)[CH]F smiles:OC(O)(Cl)[CH]F H298:-107.67 kcal/mol
library:CHOFCl_G4 label:OC(F)([CH]F)CCl smiles:OC(F)([CH]F)CCl H298:-122.14 kcal/mol
library:CHOFCl_G4 label:OC(Cl)([CH]F)OCl smiles:OC(Cl)([CH]F)OCl H298:-71.40 kcal/mol
library:CHOFCl_G4 label:F[CH]C(F)C(F)Cl smiles:F[CH]C(F)C(F)Cl H298:-118.23 kcal/mol
library:CHOFCl_G4 label:CC(Cl)C(F)[CH]F smiles:CC(Cl)C(F)[CH]F H298:-82.98 kcal/mol
library:CHOFCl_G4 label:OC([CH]F)C(Cl)Cl smiles:OC([CH]F)C(Cl)Cl H298:-71.84 kcal/mol
library:CHOFCl_G4 label:F[CH]C(Cl)Cl smiles:F[CH]C(Cl)Cl H298:-25.88 kcal/mol
library:CHOFCl_G4 label:OCC(Cl)[CH]F smiles:OCC(Cl)[CH]F H298:-66.64 kcal/mol
library:CHOFCl_G4 label:F[CH]C(Cl)C(Cl)Cl smiles:F[CH]C(Cl)C(Cl)Cl H298:-39.21 kcal/mol
library:CHOFCl_G4 label:ODCC(F)(Cl)[CH]F smiles:O=CC(F)(Cl)[CH]F H298:-89.78 kcal/mol
library:CHOFCl_G4 label:CC([CH]F)C(F)Cl smiles:CC([CH]F)C(F)Cl H298:-82.59 kcal/mol
library:CHOFCl_G4 label:F[CH]CC(Cl)CCl smiles:F[CH]CC(Cl)CCl H298:-42.94 kcal/mol
library:CHOFCl_G4 label:ODC(Cl)C[CH]F smiles:O=C(Cl)C[CH]F H298:-58.37 kcal/mol
library:CHOFCl_G4 label:F[CH]C(Cl)(Cl)Cl smiles:F[CH]C(Cl)(Cl)Cl H298:-27.58 kcal/mol
library:CHOFCl_G4 label:ODC(Cl)C(F)[CH]F smiles:O=C(Cl)C(F)[CH]F H298:-98.74 kcal/mol
library:CHOFCl_G4 label:CC(Cl)C(Cl)[CH]F smiles:CC(Cl)C(Cl)[CH]F H298:-43.95 kcal/mol
library:CHOFCl_G4 label:CCC(Cl)(Cl)[CH]F smiles:CCC(Cl)(Cl)[CH]F H298:-42.43 kcal/mol
library:CHOFCl_G4 label:F[CH]COC(Cl)Cl smiles:F[CH]COC(Cl)Cl H298:-64.80 kcal/mol
library:CHOFCl_G4 label:OC([CH]F)C(F)Cl smiles:OC([CH]F)C(F)Cl H298:-112.34 kcal/mol
library:CHOFCl_G4 label:CC([CH]F)C(Cl)Cl smiles:CC([CH]F)C(Cl)Cl H298:-41.19 kcal/mol
library:CHOFCl_G4 label:F[CH]C(OCl)OCl smiles:F[CH]C(OCl)OCl H298:-26.87 kcal/mol
library:CHOFCl_G4 label:F[CH]CC(F)Cl smiles:F[CH]CC(F)Cl H298:-75.99 kcal/mol
library:CHOFCl_G4 label:CC(Cl)C[CH]F smiles:CC(Cl)C[CH]F H298:-37.66 kcal/mol
library:CHOFCl_G4 label:OC(Cl)[CH]F smiles:OC(Cl)[CH]F H298:-61.77 kcal/mol
library:CHOFCl_G4 label:OC(Cl)C(Cl)[CH]F smiles:OC(Cl)C(Cl)[CH]F H298:-77.08 kcal/mol
library:CHOFCl_G4 label:F[CH]CC(Cl)OCl smiles:F[CH]CC(Cl)OCl H298:-35.59 kcal/mol
library:CHOFCl_G4 label:F[CH]CC(F)(F)Cl smiles:F[CH]CC(F)(F)Cl H298:-129.26 kcal/mol
library:CHOFCl_G4 label:OCC(Cl)(Cl)[CH]F smiles:OCC(Cl)(Cl)[CH]F H298:-72.76 kcal/mol
library:CHOFCl_G4 label:F[CH]CC(F)(Cl)Cl smiles:F[CH]CC(F)(Cl)Cl H298:-81.46 kcal/mol
library:CHOFCl_G4 label:COC(Cl)(Cl)[CH]F smiles:COC(Cl)(Cl)[CH]F H298:-64.95 kcal/mol
library:CHOFCl_G4 label:COC(Cl)[CH]F smiles:COC(Cl)[CH]F H298:-58.40 kcal/mol
library:CHOFCl_G4 label:F[CH]CC(Cl)Cl smiles:F[CH]CC(Cl)Cl H298:-34.54 kcal/mol
library:CHOFCl_G4 label:OC(Cl)([CH]F)CCl smiles:OC(Cl)([CH]F)CCl H298:-76.30 kcal/mol
library:CHOFCl_G4 label:OC(F)([CH]F)OCl smiles:OC(F)([CH]F)OCl H298:-118.22 kcal/mol
library:CHOFCl_G4 label:CC(O)(Cl)[CH]F smiles:CC(O)(Cl)[CH]F H298:-73.35 kcal/mol
library:CHOFCl_G4 label:OC([CH]F)OCl smiles:OC([CH]F)OCl H298:-63.28 kcal/mol
library:CHOFCl_G4 label:F[CH]C(F)Cl smiles:F[CH]C(F)Cl H298:-66.35 kcal/mol
library:CHOFCl_G4 label:OCC(F)(Cl)[CH]F smiles:OCC(F)(Cl)[CH]F H298:-113.27 kcal/mol
library:CHOFCl_G4 label:F[CH]CC(Cl)(Cl)Cl smiles:F[CH]CC(Cl)(Cl)Cl H298:-37.28 kcal/mol
library:CHOFCl_G4 label:F[CH]C(F)(Cl)Cl smiles:F[CH]C(F)(Cl)Cl H298:-70.93 kcal/mol
library:CHOFCl_G4 label:CC(Cl)([CH]F)OCl smiles:CC(Cl)([CH]F)OCl H298:-36.41 kcal/mol
library:CHOFCl_G4 label:COC(F)(Cl)[CH]F smiles:COC(F)(Cl)[CH]F H298:-110.23 kcal/mol
library:CHOFCl_G4 label:OC(Cl)C(F)[CH]F smiles:OC(Cl)C(F)[CH]F H298:-114.58 kcal/mol
library:CHOFCl_G4 label:F[CH]C(F)C(Cl)Cl smiles:F[CH]C(F)C(Cl)Cl H298:-77.45 kcal/mol
library:CHOFCl_G4 label:F[CH]C(CF)CCl smiles:F[CH]C(CF)CCl H298:-79.16 kcal/mol
library:CHOFCl_G4 label:CC(F)([CH]F)CCl smiles:CC(F)([CH]F)CCl H298:-85.14 kcal/mol
library:CHOFCl_G4 label:F[CH]CCl smiles:F[CH]CCl H298:-23.07 kcal/mol
library:CHOFCl_G4 label:CC(Cl)(Cl)[CH]F smiles:CC(Cl)(Cl)[CH]F H298:-36.72 kcal/mol
library:CHOFCl_G4 label:F[CH]C(F)CCl smiles:F[CH]C(F)CCl H298:-74.03 kcal/mol
library:CHOFCl_G4 label:CC(Cl)(Cl)C[CH]F smiles:CC(Cl)(Cl)C[CH]F H298:-44.97 kcal/mol
library:CHOFCl_G4 label:ODCC(Cl)[CH]F smiles:O=CC(Cl)[CH]F H298:-45.32 kcal/mol
library:CHOFCl_G4 label:F[CH]C(F)OOCl smiles:F[CH]C(F)OOCl H298:-53.30 kcal/mol
library:CHOFCl_G4 label:OOC(Cl)[CH]F smiles:OOC(Cl)[CH]F H298:-42.31 kcal/mol
library:CHOFCl_G4 label:F[CH]C(Cl)(Cl)OCl smiles:F[CH]C(Cl)(Cl)OCl H298:-29.95 kcal/mol
library:CHOFCl_G4 label:F[CH]CCCl smiles:F[CH]CCCl H298:-28.84 kcal/mol
library:CHOFCl_G4 label:F[CH]C(F)(F)Cl smiles:F[CH]C(F)(F)Cl H298:-118.02 kcal/mol
library:CHOFCl_G4 label:F[CH]C(F)COCl smiles:F[CH]C(F)COCl H298:-70.13 kcal/mol
library:CHOFCl_G4 label:OC(F)(Cl)C[CH]F smiles:OC(F)(Cl)C[CH]F H298:-125.12 kcal/mol
library:CHOFCl_G4 label:F[CH]C(CCl)OCl smiles:F[CH]C(CCl)OCl H298:-32.49 kcal/mol
library:CHOFCl_G4 label:OC(Cl)C[CH]F smiles:OC(Cl)C[CH]F H298:-70.48 kcal/mol
library:CHOFCl_G4 label:CC(F)(Cl)[CH]F smiles:CC(F)(Cl)[CH]F H298:-78.47 kcal/mol
library:CHOFCl_G4 label:F[CH]C(F)(Cl)CCl smiles:F[CH]C(F)(Cl)CCl H298:-81.24 kcal/mol
library:CHOFCl_G4 label:F[CH]C(F)(F)OCl smiles:F[CH]C(F)(F)OCl H298:-123.67 kcal/mol
library:CHOFCl_G4 label:F[CH]CCOCl smiles:F[CH]CCOCl H298:-25.63 kcal/mol
library:CHOFCl_G4 label:F[CH]C(Cl)OCCl smiles:F[CH]C(Cl)OCCl H298:-67.13 kcal/mol
library:CHOFCl_G4 label:F[CH]C(Cl)CCCl smiles:F[CH]C(Cl)CCCl H298:-43.29 kcal/mol
library:CHOFCl_G4 label:F[CH]COOCl smiles:F[CH]COOCl H298:-2.89 kcal/mol
library:CHOFCl_G4 label:F[CH]C(Cl)CCl smiles:F[CH]C(Cl)CCl H298:-36.03 kcal/mol
library:CHOFCl_G4 label:CC([CH]F)OCl smiles:CC([CH]F)OCl H298:-28.76 kcal/mol
library:CHOFCl_G4 label:F[CH]CC(F)OCl smiles:F[CH]CC(F)OCl H298:-79.94 kcal/mol
library:CHOFClBr_G4 label:OCC(Cl)(Br)[CH]F smiles:OCC(Cl)(Br)[CH]F H298:-61.32 kcal/mol
library:CHOFClBr_G4 label:F[CH]C(Cl)CBr smiles:F[CH]C(Cl)CBr H298:-25.11 kcal/mol
library:CHOFClBr_G4 label:F[CH]C(Cl)CCBr smiles:F[CH]C(Cl)CCBr H298:-32.21 kcal/mol
library:CHOFClBr_G4 label:F[CH]C(Cl)OCBr smiles:F[CH]C(Cl)OCBr H298:-55.30 kcal/mol
library:CHOFClBr_G4 label:F[CH]C(F)(Cl)CBr smiles:F[CH]C(F)(Cl)CBr H298:-70.29 kcal/mol
library:CHOFClBr_G4 label:F[CH]C(CCl)OBr smiles:F[CH]C(CCl)OBr H298:-29.26 kcal/mol
library:CHOFClBr_G4 label:F[CH]CC(Cl)(Br)Br smiles:F[CH]CC(Cl)(Br)Br H298:-13.30 kcal/mol
library:CHOFClBr_G4 label:F[CH]C(Cl)(Cl)OBr smiles:F[CH]C(Cl)(Cl)OBr H298:-27.25 kcal/mol
library:CHOFClBr_G4 label:F[CH]C(Cl)(Br)OBr smiles:F[CH]C(Cl)(Br)OBr H298:-16.06 kcal/mol
library:CHOFClBr_G4 label:F[CH]C(F)C(Cl)Br smiles:F[CH]C(F)C(Cl)Br H298:-65.92 kcal/mol
library:CHOFClBr_G4 label:CC(Cl)([CH]F)OBr smiles:CC(Cl)([CH]F)OBr H298:-33.04 kcal/mol
library:CHOFClBr_G4 label:F[CH]CC(Cl)(Cl)Br smiles:F[CH]CC(Cl)(Cl)Br H298:-25.23 kcal/mol
library:CHOFClBr_G4 label:F[CH]C(F)(Cl)Br smiles:F[CH]C(F)(Cl)Br H298:-58.58 kcal/mol
library:CHOFClBr_G4 label:CC(Cl)(Br)[CH]F smiles:CC(Cl)(Br)[CH]F H298:-24.87 kcal/mol
library:CHOFClBr_G4 label:OC(Cl)([CH]F)CBr smiles:OC(Cl)([CH]F)CBr H298:-65.36 kcal/mol
library:CHOFClBr_G4 label:F[CH]CC(Cl)Br smiles:F[CH]CC(Cl)Br H298:-22.83 kcal/mol
library:CHOFClBr_G4 label:F[CH]CC(F)(Cl)Br smiles:F[CH]CC(F)(Cl)Br H298:-68.60 kcal/mol
library:CHOFClBr_G4 label:F[CH]CC(Cl)OBr smiles:F[CH]CC(Cl)OBr H298:-32.51 kcal/mol
library:CHOFClBr_G4 label:F[CH]C(OCl)OBr smiles:F[CH]C(OCl)OBr H298:-23.90 kcal/mol
library:CHOFClBr_G4 label:CC([CH]F)C(Cl)Br smiles:CC([CH]F)C(Cl)Br H298:-29.24 kcal/mol
library:CHOFClBr_G4 label:CC(Cl)(Br)C[CH]F smiles:CC(Cl)(Br)C[CH]F H298:-33.17 kcal/mol
library:CHOFClBr_G4 label:OC(Br)C(Cl)[CH]F smiles:OC(Br)C(Cl)[CH]F H298:-64.85 kcal/mol
library:CHOFClBr_G4 label:F[CH]COC(Cl)Br smiles:F[CH]COC(Cl)Br H298:-52.62 kcal/mol
library:CHOFClBr_G4 label:F[CH]C(Cl)(Cl)Br smiles:F[CH]C(Cl)(Cl)Br H298:-16.08 kcal/mol
library:CHOFClBr_G4 label:F[CH]CC(Cl)CBr smiles:F[CH]CC(Cl)CBr H298:-32.04 kcal/mol
library:CHOFClBr_G4 label:F[CH]C(Cl)C(Cl)Br smiles:F[CH]C(Cl)C(Cl)Br H298:-27.57 kcal/mol
library:CHOFClBr_G4 label:CC(Br)C(Cl)[CH]F smiles:CC(Br)C(Cl)[CH]F H298:-33.36 kcal/mol
library:CHOFClBr_G4 label:F[CH]C(Cl)Br smiles:F[CH]C(Cl)Br H298:-14.64 kcal/mol
library:CHOFClBr_G4 label:OC([CH]F)C(Cl)Br smiles:OC([CH]F)C(Cl)Br H298:-60.52 kcal/mol
library:CHOFClBr_G4 label:OC(Cl)(Br)C[CH]F smiles:OC(Cl)(Br)C[CH]F H298:-65.92 kcal/mol
library:CHOFClBr_G4 label:OC(Cl)([CH]F)OBr smiles:OC(Cl)([CH]F)OBr H298:-69.15 kcal/mol
library:CHOFClBr_G4 label:ODC(Br)C(Cl)[CH]F smiles:O=C(Br)C(Cl)[CH]F H298:-48.34 kcal/mol
library:CHOFClBr_G4 label:OC(Cl)(Br)[CH]F smiles:OC(Cl)(Br)[CH]F H298:-55.88 kcal/mol
library:CHOFClBr_G4 label:CC(Cl)([CH]F)CBr smiles:CC(Cl)([CH]F)CBr H298:-34.82 kcal/mol
library:CHOFClBr_G4 label:F[CH]C(Cl)(Cl)CBr smiles:F[CH]C(Cl)(Cl)CBr H298:-28.92 kcal/mol
library:CHOFClBr_G4 label:F[CH]CCC(Cl)Br smiles:F[CH]CCC(Cl)Br H298:-28.78 kcal/mol
library:CHOFClBr_G4 label:F[CH]C(CCl)CBr smiles:F[CH]C(CCl)CBr H298:-31.76 kcal/mol
library:CHOFClBr_G4 label:F[CH]C(Cl)(Br)Br smiles:F[CH]C(Cl)(Br)Br H298:-4.53 kcal/mol
library:CHOFClBr_G4 label:F[CH]C(F)(Cl)OBr smiles:F[CH]C(F)(Cl)OBr H298:-72.54 kcal/mol
library:CHOFClBr_G4 label:CCC(Cl)(Br)[CH]F smiles:CCC(Cl)(Br)[CH]F H298:-30.65 kcal/mol
library:CHOFClBr_G4 label:F[CH]C(Cl)C(Br)Br smiles:F[CH]C(Cl)C(Br)Br H298:-16.32 kcal/mol
library:CHOFClBr_G4 label:F[CH]C(Cl)OBr smiles:F[CH]C(Cl)OBr H298:-22.91 kcal/mol
library:CHOFClBr_G4 label:F[CH]C(Cl)COBr smiles:F[CH]C(Cl)COBr H298:-29.28 kcal/mol
library:CHOFBr_G4 label:F[CH]CC(F)OBr smiles:F[CH]CC(F)OBr H298:-76.36 kcal/mol
library:CHOFBr_G4 label:CC([CH]F)OBr smiles:CC([CH]F)OBr H298:-25.72 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)C(Br)OBr smiles:F[CH]C(F)C(Br)OBr H298:-62.95 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)OC(Br)Br smiles:F[CH]C(F)OC(Br)Br H298:-88.43 kcal/mol
library:CHOFBr_G4 label:F[CH]COOBr smiles:F[CH]COOBr H298:0.25 kcal/mol
library:CHOFBr_G4 label:F[CH]C(CF)C(F)Br smiles:F[CH]C(CF)C(F)Br H298:-112.20 kcal/mol
library:CHOFBr_G4 label:F[CH]CCOBr smiles:F[CH]CCOBr H298:-22.37 kcal/mol
library:CHOFBr_G4 label:F[CH]C(OBr)OBr smiles:F[CH]C(OBr)OBr H298:-21.80 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)[CH]F smiles:OC(Br)(Br)[CH]F H298:-44.22 kcal/mol
library:CHOFBr_G4 label:F[CH]C(CBr)C(Br)Br smiles:F[CH]C(CBr)C(Br)Br H298:-15.88 kcal/mol
library:CHOFBr_G4 label:F[CH]C(CBr)C(F)F smiles:F[CH]C(CBr)C(F)F H298:-121.84 kcal/mol
library:CHOFBr_G4 label:F[CH]CC(F)(Br)Br smiles:F[CH]CC(F)(Br)Br H298:-55.99 kcal/mol
library:CHOFBr_G4 label:OC([CH]F)C(F)(Br)Br smiles:OC([CH]F)C(F)(Br)Br H298:-92.29 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(F)[CH]F smiles:OC(Br)C(F)[CH]F H298:-103.23 kcal/mol
library:CHOFBr_G4 label:CC([CH]F)C(Br)Br smiles:CC([CH]F)C(Br)Br H298:-17.81 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)(F)OBr smiles:F[CH]C(F)(F)OBr H298:-121.62 kcal/mol
library:CHOFBr_G4 label:F[CH]COC(Br)Br smiles:F[CH]COC(Br)Br H298:-40.66 kcal/mol
library:CHOFBr_G4 label:F[CH]CC(Br)OBr smiles:F[CH]CC(Br)OBr H298:-20.62 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)C(F)OBr smiles:F[CH]C(F)C(F)OBr H298:-119.18 kcal/mol
library:CHOFBr_G4 label:OC(F)([CH]F)C(F)Br smiles:OC(F)([CH]F)C(F)Br H298:-152.49 kcal/mol
library:CHOFBr_G4 label:F[CH]COC(F)(F)Br smiles:F[CH]COC(F)(F)Br H298:-150.40 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)(OBr)OBr smiles:F[CH]C(F)(OBr)OBr H298:-74.82 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)C(Br)Br smiles:F[CH]C(F)C(Br)Br H298:-54.35 kcal/mol
library:CHOFBr_G4 label:COC(F)(Br)[CH]F smiles:COC(F)(Br)[CH]F H298:-97.53 kcal/mol
library:CHOFBr_G4 label:F[CH]CC(Br)(Br)OBr smiles:F[CH]CC(Br)(Br)OBr H298:-14.40 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)(Br)Br smiles:F[CH]C(F)(Br)Br H298:-46.26 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)(F)COBr smiles:F[CH]C(F)(F)COBr H298:-118.71 kcal/mol
library:CHOFBr_G4 label:F[CH]C(OBr)C(F)F smiles:F[CH]C(OBr)C(F)F H298:-118.30 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)(F)OOBr smiles:F[CH]C(F)(F)OOBr H298:-102.82 kcal/mol
library:CHOFBr_G4 label:F[CH]C(OBr)C(F)Br smiles:F[CH]C(OBr)C(F)Br H298:-61.51 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)COBr smiles:F[CH]C(F)COBr H298:-66.63 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)(F)Br smiles:F[CH]C(F)(F)Br H298:-104.87 kcal/mol
library:CHOFBr_G4 label:F[CH]CCBr smiles:F[CH]CCBr H298:-17.73 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)OOBr smiles:F[CH]C(F)OOBr H298:-49.69 kcal/mol
library:CHOFBr_G4 label:F[CH]CC(F)(F)OBr smiles:F[CH]CC(F)(F)OBr H298:-133.56 kcal/mol
library:CHOFBr_G4 label:F[CH]CC(Br)Br smiles:F[CH]CC(Br)Br H298:-11.28 kcal/mol
library:CHOFBr_G4 label:F[CH]C(Br)C(Br)CBr smiles:F[CH]C(Br)C(Br)CBr H298:-17.67 kcal/mol
library:CHOFBr_G4 label:CC(Br)C[CH]F smiles:CC(Br)C[CH]F H298:-26.64 kcal/mol
library:CHOFBr_G4 label:OCC(F)(Br)[CH]F smiles:OCC(F)(Br)[CH]F H298:-101.02 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)CBr smiles:F[CH]C(F)CBr H298:-63.08 kcal/mol
library:CHOFBr_G4 label:F[CH]CBr smiles:F[CH]CBr H298:-12.68 kcal/mol
library:CHOFBr_G4 label:F[CH]COC(Br)(Br)Br smiles:F[CH]COC(Br)(Br)Br H298:-29.47 kcal/mol
library:CHOFBr_G4 label:F[CH]C(Br)(Br)C(Br)Br smiles:F[CH]C(Br)(Br)C(Br)Br H298:3.27 kcal/mol
library:CHOFBr_G4 label:CC(F)([CH]F)CBr smiles:CC(F)([CH]F)CBr H298:-74.11 kcal/mol
library:CHOFBr_G4 label:F[CH]C(CF)CBr smiles:F[CH]C(CF)CBr H298:-68.82 kcal/mol
library:CHOFBr_G4 label:CC([CH]F)C(F)(Br)Br smiles:CC([CH]F)C(F)(Br)Br H298:-62.83 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)(CBr)OBr smiles:F[CH]C(F)(CBr)OBr H298:-69.79 kcal/mol
library:CHOFBr_G4 label:OC(Br)([CH]F)OBr smiles:OC(Br)([CH]F)OBr H298:-55.79 kcal/mol
library:CHOFBr_G4 label:F[CH]CCC(F)(F)Br smiles:F[CH]CCC(F)(F)Br H298:-123.29 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)Br smiles:F[CH]C(F)Br H298:-54.24 kcal/mol
library:CHOFBr_G4 label:OC([CH]F)OBr smiles:OC([CH]F)OBr H298:-60.19 kcal/mol
library:CHOFBr_G4 label:F[CH]C(CBr)OBr smiles:F[CH]C(CBr)OBr H298:-18.39 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)C(F)(F)Br smiles:F[CH]C(F)C(F)(F)Br H298:-156.94 kcal/mol
library:CHOFBr_G4 label:F[CH]C(Br)(Br)Br smiles:F[CH]C(Br)(Br)Br H298:6.90 kcal/mol
library:CHOFBr_G4 label:F[CH]C(Br)(Br)OOBr smiles:F[CH]C(Br)(Br)OOBr H298:13.12 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)(CF)CBr smiles:F[CH]C(F)(CF)CBr H298:-114.59 kcal/mol
library:CHOFBr_G4 label:F[CH]CC(F)(Br)OBr smiles:F[CH]CC(F)(Br)OBr H298:-71.61 kcal/mol
library:CHOFBr_G4 label:OC(F)([CH]F)OBr smiles:OC(F)([CH]F)OBr H298:-115.16 kcal/mol
library:CHOFBr_G4 label:CCC(Br)(Br)[CH]F smiles:CCC(Br)(Br)[CH]F H298:-19.41 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)(Br)OCBr smiles:F[CH]C(F)(Br)OCBr H298:-90.52 kcal/mol
library:CHOFBr_G4 label:F[CH]C(CBr)C(F)Br smiles:F[CH]C(CBr)C(F)Br H298:-64.45 kcal/mol
library:CHOFBr_G4 label:OC(F)(Br)C[CH]F smiles:OC(F)(Br)C[CH]F H298:-111.97 kcal/mol
library:CHOFBr_G4 label:OC(F)(Br)C(F)[CH]F smiles:OC(F)(Br)C(F)[CH]F H298:-153.73 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)(Br)CCBr smiles:F[CH]C(F)(Br)CCBr H298:-65.97 kcal/mol
library:CHOFBr_G4 label:OC(Br)C[CH]F smiles:OC(Br)C[CH]F H298:-58.46 kcal/mol
library:CHOFBr_G4 label:F[CH]COC(F)(Br)Br smiles:F[CH]COC(F)(Br)Br H298:-88.34 kcal/mol
library:CHOFBr_G4 label:CC([CH]F)C(F)(F)Br smiles:CC([CH]F)C(F)(F)Br H298:-122.57 kcal/mol
library:CHOFBr_G4 label:F[CH]CC(F)(F)Br smiles:F[CH]CC(F)(F)Br H298:-115.73 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(F)(F)[CH]F smiles:CC(Br)C(F)(F)[CH]F H298:-123.72 kcal/mol
library:CHOFBr_G4 label:F[CH]C(Br)C(Br)Br smiles:F[CH]C(Br)C(Br)Br H298:-4.94 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)C(Br)(Br)Br smiles:F[CH]C(F)C(Br)(Br)Br H298:-44.07 kcal/mol
library:CHOFBr_G4 label:F[CH]CCC(Br)(Br)Br smiles:F[CH]CCC(Br)(Br)Br H298:-8.53 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)(Br)CBr smiles:F[CH]C(F)(Br)CBr H298:-58.09 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)C[CH]F smiles:OC(Br)(Br)C[CH]F H298:-53.44 kcal/mol
library:CHOFBr_G4 label:F[CH]CC(F)Br smiles:F[CH]CC(F)Br H298:-63.35 kcal/mol
library:CHOFBr_G4 label:OC([CH]F)C(F)Br smiles:OC([CH]F)C(F)Br H298:-100.18 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)[CH]F smiles:CC(F)(Br)[CH]F H298:-66.04 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)C(F)[CH]F smiles:CC(F)(Br)C(F)[CH]F H298:-118.16 kcal/mol
library:CHOFBr_G4 label:F[CH]C(Br)COBr smiles:F[CH]C(Br)COBr H298:-18.98 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)C[CH]F smiles:CC(F)(Br)C[CH]F H298:-75.17 kcal/mol
library:CHOFBr_G4 label:F[CH]C(Br)OOBr smiles:F[CH]C(Br)OOBr H298:5.86 kcal/mol
library:CHOFBr_G4 label:F[CH]CC(F)C(F)Br smiles:F[CH]CC(F)C(F)Br H298:-114.43 kcal/mol
library:CHOFBr_G4 label:F[CH]C(Br)OBr smiles:F[CH]C(Br)OBr H298:-10.60 kcal/mol
library:CHOFBr_G4 label:OC(F)(Br)[CH]F smiles:OC(F)(Br)[CH]F H298:-101.34 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(F)(F)[CH]F smiles:O=C(Br)C(F)(F)[CH]F H298:-134.56 kcal/mol
library:CHOFBr_G4 label:OC([CH]F)C(F)(F)Br smiles:OC([CH]F)C(F)(F)Br H298:-151.64 kcal/mol
library:CHOFBr_G4 label:F[CH]C(Br)(CBr)OBr smiles:F[CH]C(Br)(CBr)OBr H298:-13.18 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(F)(F)[CH]F smiles:OC(Br)C(F)(F)[CH]F H298:-153.45 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)C(F)(Br)Br smiles:F[CH]C(F)C(F)(Br)Br H298:-97.96 kcal/mol
library:CHOFBr_G4 label:CC([CH]F)C(F)Br smiles:CC([CH]F)C(F)Br H298:-70.13 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)(Br)OBr smiles:F[CH]C(F)(Br)OBr H298:-60.74 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(F)(Br)[CH]F smiles:OC(Br)C(F)(Br)[CH]F H298:-96.35 kcal/mol
library:CHOFBr_G4 label:CC([CH]F)C(Br)(Br)Br smiles:CC([CH]F)C(Br)(Br)Br H298:-8.39 kcal/mol
library:CHOFBr_G4 label:CC(Br)(Br)C[CH]F smiles:CC(Br)(Br)C[CH]F H298:-21.32 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)(Br)COBr smiles:F[CH]C(F)(Br)COBr H298:-62.07 kcal/mol
library:CHOFBr_G4 label:F[CH]CC(Br)C(Br)Br smiles:F[CH]CC(Br)C(Br)Br H298:-13.46 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)(F)C(F)Br smiles:F[CH]C(F)(F)C(F)Br H298:-156.13 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(F)(Br)[CH]F smiles:O=C(Br)C(F)(Br)[CH]F H298:-79.19 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)(Br)C(Br)Br smiles:F[CH]C(F)(Br)C(Br)Br H298:-47.57 kcal/mol
library:CHOFBr_G4 label:F[CH]C(CF)C(Br)Br smiles:F[CH]C(CF)C(Br)Br H298:-60.73 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)(Br)OOBr smiles:F[CH]C(F)(Br)OOBr H298:-43.19 kcal/mol
library:CHOFBr_G4 label:F[CH]CC(Br)(Br)Br smiles:F[CH]CC(Br)(Br)Br H298:-1.43 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)(F)C(Br)Br smiles:F[CH]C(F)(F)C(Br)Br H298:-104.61 kcal/mol
library:CHOFBr_G4 label:F[CH]C(Br)(Br)CCBr smiles:F[CH]C(Br)(Br)CCBr H298:-13.77 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)C(F)Br smiles:F[CH]C(F)C(F)Br H298:-105.64 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)C(F)[CH]F smiles:OC(Br)(Br)C(F)[CH]F H298:-95.84 kcal/mol
library:CHOFBr_G4 label:CCC(Br)[CH]F smiles:CCC(Br)[CH]F H298:-25.42 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)(CF)OBr smiles:F[CH]C(F)(CF)OBr H298:-118.36 kcal/mol
library:CHOFBr_G4 label:F[CH]C(Br)(Br)OCBr smiles:F[CH]C(Br)(Br)OCBr H298:-34.47 kcal/mol
library:CHOFBr_G4 label:F[CH]CC(F)(Br)CBr smiles:F[CH]CC(F)(Br)CBr H298:-68.13 kcal/mol
library:CHOFBr_G4 label:CC(F)([CH]F)C(Br)Br smiles:CC(F)([CH]F)C(Br)Br H298:-64.97 kcal/mol
library:CHOFBr_G4 label:OC(F)([CH]F)CBr smiles:OC(F)([CH]F)CBr H298:-111.12 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)CC(F)Br smiles:F[CH]C(F)CC(F)Br H298:-116.31 kcal/mol
library:CHOFBr_G4 label:F[CH]C(OBr)C(Br)Br smiles:F[CH]C(OBr)C(Br)Br H298:-10.96 kcal/mol
library:CHOFBr_G4 label:F[CH]CCC(Br)Br smiles:F[CH]CCC(Br)Br H298:-17.26 kcal/mol
library:CHOFBr_G4 label:OC([CH]F)CBr smiles:OC([CH]F)CBr H298:-55.24 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(Br)(Br)[CH]F smiles:OC(Br)C(Br)(Br)[CH]F H298:-45.87 kcal/mol
library:CHOFBr_G4 label:F[CH]C(CBr)CBr smiles:F[CH]C(CBr)CBr H298:-19.62 kcal/mol
library:CHOFBr_G4 label:F[CH]CCC(F)Br smiles:F[CH]CCC(F)Br H298:-69.85 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)CC(Br)Br smiles:F[CH]C(F)CC(Br)Br H298:-63.15 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)(CBr)CBr smiles:F[CH]C(F)(CBr)CBr H298:-66.48 kcal/mol
library:CHOFBr_G4 label:COC(Br)(Br)[CH]F smiles:COC(Br)(Br)[CH]F H298:-41.74 kcal/mol
library:CHOFBr_G4 label:CC(F)([CH]F)OBr smiles:CC(F)([CH]F)OBr H298:-78.48 kcal/mol
library:CHOFBr_G4 label:F[CH]C(CF)OBr smiles:F[CH]C(CF)OBr H298:-66.08 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)OBr smiles:F[CH]C(F)OBr H298:-66.20 kcal/mol
library:CHOFBr_G4 label:F[CH]CCC(F)(Br)Br smiles:F[CH]CCC(F)(Br)Br H298:-63.74 kcal/mol
library:CHOFBr_G4 label:F[CH]C(Br)C(Br)OBr smiles:F[CH]C(Br)C(Br)OBr H298:-14.70 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C[CH]F smiles:O=C(Br)C[CH]F H298:-45.94 kcal/mol
library:CHOFBr_G4 label:OOC(F)(Br)[CH]F smiles:OOC(F)(Br)[CH]F H298:-77.44 kcal/mol
library:CHOFBr_G4 label:F[CH]C(OF)OBr smiles:F[CH]C(OF)OBr H298:-27.88 kcal/mol
library:CHOFBr_G4 label:F[CH]CC(F)(F)CBr smiles:F[CH]CC(F)(F)CBr H298:-125.62 kcal/mol
library:CHOFBr_G4 label:F[CH]C(Br)C(Br)(Br)Br smiles:F[CH]C(Br)C(Br)(Br)Br H298:5.06 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)OCBr smiles:F[CH]C(F)OCBr H298:-97.53 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)CCBr smiles:F[CH]C(F)CCBr H298:-70.47 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(F)[CH]F smiles:O=C(Br)C(F)[CH]F H298:-86.34 kcal/mol
library:CHOFBr_G4 label:F[CH]COBr smiles:F[CH]COBr H298:-15.88 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)(OF)OBr smiles:F[CH]C(F)(OF)OBr H298:-79.25 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(F)(Br)[CH]F smiles:CC(Br)C(F)(Br)[CH]F H298:-66.16 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)(F)OCBr smiles:F[CH]C(F)(F)OCBr H298:-150.52 kcal/mol
library:CHOFBr_G4 label:F[CH]CC(Br)(Br)CBr smiles:F[CH]CC(Br)(Br)CBr H298:-15.17 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)(F)CCBr smiles:F[CH]C(F)(F)CCBr H298:-122.63 kcal/mol
library:CHOFBr_G4 label:F[CH]C(Br)(Br)OBr smiles:F[CH]C(Br)(Br)OBr H298:-4.36 kcal/mol
library:CHOFBr_G4 label:F[CH]C(Br)(OBr)OBr smiles:F[CH]C(Br)(OBr)OBr H298:-17.34 kcal/mol
library:CHOFBr_G4 label:CCC(F)(Br)[CH]F smiles:CCC(F)(Br)[CH]F H298:-71.81 kcal/mol
library:CHOFBr_G4 label:CC(Br)(Br)[CH]F smiles:CC(Br)(Br)[CH]F H298:-13.66 kcal/mol
library:CHOFBr_G4 label:OC(F)([CH]F)C(Br)Br smiles:OC(F)([CH]F)C(Br)Br H298:-100.20 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)C(F)CBr smiles:F[CH]C(F)C(F)CBr H298:-114.42 kcal/mol
library:CHOFBr_G4 label:F[CH]CC(Br)CBr smiles:F[CH]CC(Br)CBr H298:-21.02 kcal/mol
library:CHOFBr_G4 label:F[CH]COC(F)Br smiles:F[CH]COC(F)Br H298:-94.99 kcal/mol
library:CHOFBr_G4 label:CC(Br)(Br)C(F)[CH]F smiles:CC(Br)(Br)C(F)[CH]F H298:-65.22 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(F)[CH]F smiles:CC(Br)C(F)[CH]F H298:-71.89 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(Br)[CH]F smiles:OC(Br)C(Br)[CH]F H298:-53.98 kcal/mol
library:CHOFBr_G4 label:F[CH]CC(F)C(Br)Br smiles:F[CH]CC(F)C(Br)Br H298:-62.90 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)(F)CBr smiles:F[CH]C(F)(F)CBr H298:-114.88 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)C(Br)[CH]F smiles:OC(Br)(Br)C(Br)[CH]F H298:-46.89 kcal/mol
library:CHOFBr_G4 label:ODCC(F)(Br)[CH]F smiles:O=CC(F)(Br)[CH]F H298:-75.96 kcal/mol
library:CHOFBr_G4 label:CC(F)([CH]F)C(F)Br smiles:CC(F)([CH]F)C(F)Br H298:-116.97 kcal/mol
library:CHOFBr_G4 label:F[CH]C(Br)Br smiles:F[CH]C(Br)Br H298:-3.60 kcal/mol
library:CHOFBr_G4 label:F[CH]CCCBr smiles:F[CH]CCCBr H298:-24.03 kcal/mol
library:CHOFBr_G4 label:OC([CH]F)C(Br)Br smiles:OC([CH]F)C(Br)Br H298:-49.05 kcal/mol
library:CHOFBr_G4 label:OC([CH]F)C(Br)(Br)Br smiles:OC([CH]F)C(Br)(Br)Br H298:-38.39 kcal/mol
library:CHOFBr_G4 label:F[CH]CC(F)CBr smiles:F[CH]CC(F)CBr H298:-70.77 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)C(Br)CBr smiles:F[CH]C(F)C(Br)CBr H298:-65.56 kcal/mol
library:CHOFBr_G4 label:CC([CH]F)CBr smiles:CC([CH]F)CBr H298:-24.65 kcal/mol
library:CHOFBr_G4 label:F[CH]COCBr smiles:F[CH]COCBr H298:-46.00 kcal/mol
library:CHOFBr_G4 label:F[CH]C(F)OC(F)Br smiles:F[CH]C(F)OC(F)Br H298:-145.06 kcal/mol
""",
)

entry(
    index = 82,
    label = "CsBr1sCsO2s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cs   u0 {1,S}
3   O2s  u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.366681,-1.46456,-2.2701,-2.92239,-3.86779,-4.44122,-5.05783],'cal/(mol*K)','+|-',[0.127605,0.131018,0.122845,0.11474,0.101261,0.0886106,0.0649003]),
        H298 = (94.1527,'kcal/mol','+|-',0.203848),
        S298 = (4.19277,'cal/(mol*K)','+|-',0.34643),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:BrCO[C](Br)C(Br)Br smiles:BrCO[C](Br)C(Br)Br H298:7.61 kcal/mol
library:CHOBr_G4 label:BrC[C](Br)OC(Br)Br smiles:BrC[C](Br)OC(Br)Br H298:7.68 kcal/mol
library:CHOBr_G4 label:C[C](Br)OC(Br)Br smiles:C[C](Br)OC(Br)Br H298:2.36 kcal/mol
library:CHOBr_G4 label:CO[C](Br)C(Br)Br smiles:CO[C](Br)C(Br)Br H298:3.27 kcal/mol
library:CHOBr_G4 label:O[C](Br)CC(Br)Br smiles:O[C](Br)CC(Br)Br H298:-7.44 kcal/mol
library:CHOBr_G4 label:O[C](Br)COBr smiles:O[C](Br)COBr H298:-11.59 kcal/mol
library:CHOBr_G4 label:C[C](O)Br smiles:C[C](O)Br H298:-14.03 kcal/mol
library:CHOBr_G4 label:O[C](Br)CCBr smiles:O[C](Br)CCBr H298:-14.44 kcal/mol
library:CHOBr_G4 label:CC[C](O)Br smiles:CC[C](O)Br H298:-19.47 kcal/mol
library:CHOBr_G4 label:BrCO[C](Br)CBr smiles:BrCO[C](Br)CBr H298:-1.00 kcal/mol
library:CHOBr_G4 label:O[C](Br)CBr smiles:O[C](Br)CBr H298:-8.48 kcal/mol
library:CHOBr_G4 label:CO[C](C)Br smiles:CO[C](C)Br H298:-10.50 kcal/mol
library:CHOBr_G4 label:CO[C](Br)CBr smiles:CO[C](Br)CBr H298:-5.03 kcal/mol
library:CHOBr_G4 label:O[C](Br)C(Br)OBr smiles:O[C](Br)C(Br)OBr H298:-7.39 kcal/mol
library:CHOBr_G4 label:OC[C](O)Br smiles:OC[C](O)Br H298:-48.09 kcal/mol
library:CHOBr_G4 label:C[C](Br)OCBr smiles:C[C](Br)OCBr H298:-6.22 kcal/mol
library:CHOFClBr_G4 label:CO[C](Br)C(F)Cl smiles:CO[C](Br)C(F)Cl H298:-59.39 kcal/mol
library:CHOFClBr_G4 label:CC(F)(Cl)[C](O)Br smiles:CC(F)(Cl)[C](O)Br H298:-74.49 kcal/mol
library:CHOFClBr_G4 label:O[C](Br)C(F)Cl smiles:O[C](Br)C(F)Cl H298:-62.32 kcal/mol
library:CHOFBr_G4 label:O[C](Br)CC(F)(F)Br smiles:O[C](Br)CC(F)(F)Br H298:-110.74 kcal/mol
library:CHOFBr_G4 label:CO[C](Br)C(F)(F)Br smiles:CO[C](Br)C(F)(F)Br H298:-97.71 kcal/mol
library:CHOFBr_G4 label:O[C](Br)CC(F)Br smiles:O[C](Br)CC(F)Br H298:-59.20 kcal/mol
library:CHOFBr_G4 label:O[C](Br)CC(F)(Br)Br smiles:O[C](Br)CC(F)(Br)Br H298:-51.28 kcal/mol
library:CHOFBr_G4 label:CO[C](Br)C(F)(F)F smiles:CO[C](Br)C(F)(F)F H298:-160.16 kcal/mol
library:CHOFBr_G4 label:O[C](Br)C(F)C(F)F smiles:O[C](Br)C(F)C(F)F H298:-159.34 kcal/mol
library:CHOFBr_G4 label:O[C](Br)C(F)(Br)Br smiles:O[C](Br)C(F)(Br)Br H298:-41.92 kcal/mol
library:CHOFBr_G4 label:O[C](Br)C(F)Br smiles:O[C](Br)C(F)Br H298:-49.86 kcal/mol
library:CHOFBr_G4 label:CC(F)[C](O)Br smiles:CC(F)[C](O)Br H298:-65.88 kcal/mol
library:CHOFBr_G4 label:CO[C](Br)CF smiles:CO[C](Br)CF H298:-51.80 kcal/mol
library:CHOFBr_G4 label:O[C](Br)C(F)CF smiles:O[C](Br)C(F)CF H298:-106.61 kcal/mol
library:CHOFBr_G4 label:FC(F)[C](Br)OCBr smiles:FC(F)[C](Br)OCBr H298:-98.18 kcal/mol
library:CHOFBr_G4 label:CC(F)(F)[C](O)Br smiles:CC(F)(F)[C](O)Br H298:-119.74 kcal/mol
library:CHOFBr_G4 label:O[C](Br)C(F)(Br)CF smiles:O[C](Br)C(F)(Br)CF H298:-100.40 kcal/mol
library:CHOFBr_G4 label:O[C](Br)CCF smiles:O[C](Br)CCF H298:-62.82 kcal/mol
library:CHOFBr_G4 label:FC(Br)[C](Br)OCBr smiles:FC(Br)[C](Br)OCBr H298:-42.23 kcal/mol
library:CHOFBr_G4 label:O[C](Br)CC(F)F smiles:O[C](Br)CC(F)F H298:-116.66 kcal/mol
library:CHOFBr_G4 label:O[C](Br)C(F)(F)CF smiles:O[C](Br)C(F)(F)CF H298:-159.33 kcal/mol
library:CHOFBr_G4 label:CO[C](Br)C(F)(Br)Br smiles:CO[C](Br)C(F)(Br)Br H298:-39.30 kcal/mol
library:CHOFBr_G4 label:O[C](Br)CC(F)(F)F smiles:O[C](Br)CC(F)(F)F H298:-175.26 kcal/mol
library:CHOFBr_G4 label:O[C](Br)C(Br)CF smiles:O[C](Br)C(Br)CF H298:-58.88 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)[C](O)Br smiles:CC(F)(Br)[C](O)Br H298:-62.71 kcal/mol
library:CHOFBr_G4 label:CO[C](Br)C(F)F smiles:CO[C](Br)C(F)F H298:-103.45 kcal/mol
library:CHOFBr_G4 label:O[C](Br)C(Br)C(F)F smiles:O[C](Br)C(Br)C(F)F H298:-111.75 kcal/mol
library:CHOFBr_G4 label:O[C](Br)CF smiles:O[C](Br)CF H298:-55.24 kcal/mol
library:CHOFBr_G4 label:O[C](Br)C(F)(F)F smiles:O[C](Br)C(F)(F)F H298:-162.90 kcal/mol
library:CHOFBr_G4 label:FC[C](Br)OCBr smiles:FC[C](Br)OCBr H298:-47.32 kcal/mol
library:CHOFBr_G4 label:O[C](Br)C(Br)C(F)Br smiles:O[C](Br)C(Br)C(F)Br H298:-51.73 kcal/mol
library:CHOFBr_G4 label:FC[C](Br)OC(Br)Br smiles:FC[C](Br)OC(Br)Br H298:-38.13 kcal/mol
library:CHOFBr_G4 label:O[C](Br)C(F)F smiles:O[C](Br)C(F)F H298:-106.53 kcal/mol
library:CHOFBr_G4 label:CO[C](Br)C(F)Br smiles:CO[C](Br)C(F)Br H298:-47.35 kcal/mol
library:CHOClBr_G4 label:O[C](Br)C(Cl)Cl smiles:O[C](Br)C(Cl)Cl H298:-21.67 kcal/mol
library:CHOClBr_G4 label:ClC[C](Br)OCBr smiles:ClC[C](Br)OCBr H298:-11.00 kcal/mol
library:CHOClBr_G4 label:CO[C](Br)CCl smiles:CO[C](Br)CCl H298:-15.27 kcal/mol
library:CHOClBr_G4 label:CO[C](Br)C(Cl)Br smiles:CO[C](Br)C(Cl)Br H298:-7.76 kcal/mol
library:CHOClBr_G4 label:O[C](Br)CCl smiles:O[C](Br)CCl H298:-18.76 kcal/mol
library:CHOClBr_G4 label:CC(Cl)(Cl)[C](O)Br smiles:CC(Cl)(Cl)[C](O)Br H298:-32.62 kcal/mol
library:CHOClBr_G4 label:O[C](Br)CCCl smiles:O[C](Br)CCCl H298:-25.02 kcal/mol
library:CHOClBr_G4 label:CC(Cl)[C](O)Br smiles:CC(Cl)[C](O)Br H298:-27.70 kcal/mol
library:CHOClBr_G4 label:CC(Cl)(Br)[C](O)Br smiles:CC(Cl)(Br)[C](O)Br H298:-20.86 kcal/mol
library:CHOClBr_G4 label:CO[C](Br)C(Cl)Cl smiles:CO[C](Br)C(Cl)Cl H298:-18.56 kcal/mol
""",
)

entry(
    index = 83,
    label = "CsCl1sCsO2s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cs   u0 {1,S}
3   O2s  u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.10357,-1.13143,-2.01657,-2.71765,-3.69589,-4.29486,-5.00487],'cal/(mol*K)','+|-',[0.133279,0.136844,0.128308,0.119842,0.105763,0.0925508,0.0677862]),
        H298 = (94.4051,'kcal/mol','+|-',0.212912),
        S298 = (3.43196,'cal/(mol*K)','+|-',0.361835),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOCl_G4 label:O[C](Cl)CCCl smiles:O[C](Cl)CCCl H298:-37.25 kcal/mol
library:CHOCl_G4 label:O[C](Cl)CCl smiles:O[C](Cl)CCl H298:-31.03 kcal/mol
library:CHOCl_G4 label:CO[C](Cl)C(Cl)(Cl)Cl smiles:CO[C](Cl)C(Cl)(Cl)Cl H298:-31.11 kcal/mol
library:CHOCl_G4 label:CO[C](Cl)C(Cl)Cl smiles:CO[C](Cl)C(Cl)Cl H298:-30.17 kcal/mol
library:CHOCl_G4 label:O[C](Cl)C(Cl)(Cl)OCl smiles:O[C](Cl)C(Cl)(Cl)OCl H298:-38.00 kcal/mol
library:CHOCl_G4 label:CO[C](Cl)CCl smiles:CO[C](Cl)CCl H298:-27.29 kcal/mol
library:CHOCl_G4 label:ClCO[C](Cl)C(Cl)Cl smiles:ClCO[C](Cl)C(Cl)Cl H298:-37.07 kcal/mol
library:CHOCl_G4 label:OC[C](O)Cl smiles:OC[C](O)Cl H298:-60.88 kcal/mol
library:CHOCl_G4 label:O[C](Cl)CC(Cl)Cl smiles:O[C](Cl)CC(Cl)Cl H298:-42.90 kcal/mol
library:CHOCl_G4 label:O[C](Cl)CC(Cl)(Cl)Cl smiles:O[C](Cl)CC(Cl)(Cl)Cl H298:-44.43 kcal/mol
library:CHOCl_G4 label:Cl[C](OC(Cl)(Cl)Cl)C(Cl)Cl smiles:Cl[C](OC(Cl)(Cl)Cl)C(Cl)Cl H298:-40.90 kcal/mol
library:CHOCl_G4 label:CO[C](C)Cl smiles:CO[C](C)Cl H298:-22.48 kcal/mol
library:CHOCl_G4 label:O[C](Cl)C(Cl)(Cl)C(Cl)Cl smiles:O[C](Cl)C(Cl)(Cl)C(Cl)Cl H298:-50.44 kcal/mol
library:CHOCl_G4 label:C[C](Cl)OCCl smiles:C[C](Cl)OCCl H298:-29.96 kcal/mol
library:CHOCl_G4 label:C[C](Cl)OC(Cl)Cl smiles:C[C](Cl)OC(Cl)Cl H298:-34.09 kcal/mol
library:CHOCl_G4 label:O[C](Cl)C(Cl)CCl smiles:O[C](Cl)C(Cl)CCl H298:-44.76 kcal/mol
library:CHOCl_G4 label:OO[C](Cl)CCl smiles:OO[C](Cl)CCl H298:-8.25 kcal/mol
library:CHOCl_G4 label:CC[C](O)Cl smiles:CC[C](O)Cl H298:-31.73 kcal/mol
library:CHOCl_G4 label:C[C](Cl)OC(Cl)(Cl)Cl smiles:C[C](Cl)OC(Cl)(Cl)Cl H298:-33.75 kcal/mol
library:CHOCl_G4 label:C[C](O)Cl smiles:C[C](O)Cl H298:-26.44 kcal/mol
library:CHOCl_G4 label:ClC[C](Cl)OC(Cl)Cl smiles:ClC[C](Cl)OC(Cl)Cl H298:-38.11 kcal/mol
library:CHOCl_G4 label:CC(Cl)[C](O)Cl smiles:CC(Cl)[C](O)Cl H298:-39.95 kcal/mol
library:CHOCl_G4 label:Cl[C](OC(Cl)Cl)C(Cl)(Cl)Cl smiles:Cl[C](OC(Cl)Cl)C(Cl)(Cl)Cl H298:-41.42 kcal/mol
library:CHOCl_G4 label:O[C](Cl)C(Cl)(Cl)Cl smiles:O[C](Cl)C(Cl)(Cl)Cl H298:-34.71 kcal/mol
library:CHOCl_G4 label:O[C](Cl)C(Cl)C(Cl)(Cl)Cl smiles:O[C](Cl)C(Cl)C(Cl)(Cl)Cl H298:-48.21 kcal/mol
library:CHOCl_G4 label:O[C](Cl)C(Cl)Cl smiles:O[C](Cl)C(Cl)Cl H298:-33.62 kcal/mol
library:CHOCl_G4 label:O[C](Cl)C(Cl)C(Cl)Cl smiles:O[C](Cl)C(Cl)C(Cl)Cl H298:-48.07 kcal/mol
library:CHOCl_G4 label:ClC[C](Cl)OC(Cl)(Cl)Cl smiles:ClC[C](Cl)OC(Cl)(Cl)Cl H298:-37.51 kcal/mol
library:CHOCl_G4 label:CC(Cl)(Cl)[C](O)Cl smiles:CC(Cl)(Cl)[C](O)Cl H298:-44.34 kcal/mol
library:CHOCl_G4 label:O[C](Cl)C(O)(Cl)Cl smiles:O[C](Cl)C(O)(Cl)Cl H298:-76.06 kcal/mol
library:CHOCl_G4 label:O[C](Cl)C(Cl)(Cl)CCl smiles:O[C](Cl)C(Cl)(Cl)CCl H298:-47.73 kcal/mol
library:CHOCl_G4 label:ClCO[C](Cl)C(Cl)(Cl)Cl smiles:ClCO[C](Cl)C(Cl)(Cl)Cl H298:-37.78 kcal/mol
library:CHOCl_G4 label:Cl[C](OC(Cl)Cl)C(Cl)Cl smiles:Cl[C](OC(Cl)Cl)C(Cl)Cl H298:-40.27 kcal/mol
library:CHOCl_G4 label:ClCO[C](Cl)CCl smiles:ClCO[C](Cl)CCl H298:-34.58 kcal/mol
library:CHOCl_G4 label:Cl[C](OC(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:Cl[C](OC(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-41.65 kcal/mol
library:CHOCl_G4 label:O[C](Cl)C(O)Cl smiles:O[C](Cl)C(O)Cl H298:-70.09 kcal/mol
library:CHOCl_G4 label:O[C](Cl)COCl smiles:O[C](Cl)COCl H298:-26.79 kcal/mol
library:CHOCl_G4 label:O[C](Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:O[C](Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-46.86 kcal/mol
library:CHOFCl_G4 label:CO[C](Cl)CF smiles:CO[C](Cl)CF H298:-63.76 kcal/mol
library:CHOFCl_G4 label:O[C](Cl)C(F)Cl smiles:O[C](Cl)C(F)Cl H298:-74.54 kcal/mol
library:CHOFCl_G4 label:CO[C](Cl)C(F)F smiles:CO[C](Cl)C(F)F H298:-115.26 kcal/mol
library:CHOFCl_G4 label:FC[C](Cl)OCCl smiles:FC[C](Cl)OCCl H298:-71.10 kcal/mol
library:CHOFCl_G4 label:O[C](Cl)C(F)F smiles:O[C](Cl)C(F)F H298:-118.78 kcal/mol
library:CHOFCl_G4 label:CC(F)(F)[C](O)Cl smiles:CC(F)(F)[C](O)Cl H298:-131.75 kcal/mol
library:CHOFCl_G4 label:CC(F)[C](O)Cl smiles:CC(F)[C](O)Cl H298:-77.17 kcal/mol
library:CHOFCl_G4 label:CO[C](Cl)C(F)Cl smiles:CO[C](Cl)C(F)Cl H298:-71.01 kcal/mol
library:CHOFCl_G4 label:O[C](Cl)CF smiles:O[C](Cl)CF H298:-68.00 kcal/mol
library:CHOFCl_G4 label:CC(F)(Cl)[C](O)Cl smiles:CC(F)(Cl)[C](O)Cl H298:-86.86 kcal/mol
library:CHOFCl_G4 label:O[C](Cl)CCF smiles:O[C](Cl)CCF H298:-75.27 kcal/mol
library:CHOFClBr_G4 label:FC[C](Cl)OCBr smiles:FC[C](Cl)OCBr H298:-59.40 kcal/mol
library:CHOClBr_G4 label:O[C](Cl)COBr smiles:O[C](Cl)COBr H298:-23.29 kcal/mol
library:CHOClBr_G4 label:ClC[C](Cl)OCBr smiles:ClC[C](Cl)OCBr H298:-22.95 kcal/mol
library:CHOClBr_G4 label:C[C](Cl)OC(Cl)Br smiles:C[C](Cl)OC(Cl)Br H298:-22.02 kcal/mol
library:CHOClBr_G4 label:C[C](Cl)OCBr smiles:C[C](Cl)OCBr H298:-18.31 kcal/mol
library:CHOClBr_G4 label:C[C](Cl)OC(Br)Br smiles:C[C](Cl)OC(Br)Br H298:-9.63 kcal/mol
""",
)

entry(
    index = 84,
    label = "CsCsF1sO2s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   O2s u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0614432,-1.27015,-2.21882,-2.91799,-3.86605,-4.454,-5.16472],'cal/(mol*K)','+|-',[0.13577,0.139402,0.130706,0.122083,0.10774,0.0942808,0.0690533]),
        H298 = (98.7355,'kcal/mol','+|-',0.216892),
        S298 = (3.48611,'cal/(mol*K)','+|-',0.368599),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:O[C](F)C(F)F smiles:O[C](F)C(F)F H298:-158.14 kcal/mol
library:CHOF_G4 label:O[C](F)COF smiles:O[C](F)COF H298:-71.84 kcal/mol
library:CHOF_G4 label:C[C](O)F smiles:C[C](O)F H298:-68.01 kcal/mol
library:CHOF_G4 label:O[C](F)C(F)(F)C(F)F smiles:O[C](F)C(F)(F)C(F)F H298:-260.00 kcal/mol
library:CHOF_G4 label:O[C](F)CCF smiles:O[C](F)CCF H298:-116.73 kcal/mol
library:CHOF_G4 label:FCO[C](F)CF smiles:FCO[C](F)CF H298:-152.79 kcal/mol
library:CHOF_G4 label:O[C](F)CC(F)F smiles:O[C](F)CC(F)F H298:-170.85 kcal/mol
library:CHOF_G4 label:F[C](OC(F)(F)F)C(F)F smiles:F[C](OC(F)(F)F)C(F)F H298:-313.25 kcal/mol
library:CHOF_G4 label:O[C](F)C(O)(F)F smiles:O[C](F)C(O)(F)F H298:-210.53 kcal/mol
library:CHOF_G4 label:CO[C](F)C(F)(F)F smiles:CO[C](F)C(F)(F)F H298:-211.45 kcal/mol
library:CHOF_G4 label:O[C](F)CC(F)(F)F smiles:O[C](F)CC(F)(F)F H298:-228.99 kcal/mol
library:CHOF_G4 label:FC[C](F)OC(F)(F)F smiles:FC[C](F)OC(F)(F)F H298:-264.09 kcal/mol
library:CHOF_G4 label:CC(F)(F)[C](O)F smiles:CC(F)(F)[C](O)F H298:-172.05 kcal/mol
library:CHOF_G4 label:CO[C](F)CF smiles:CO[C](F)CF H298:-103.71 kcal/mol
library:CHOF_G4 label:O[C](F)CF smiles:O[C](F)CF H298:-108.15 kcal/mol
library:CHOF_G4 label:O[C](F)C(F)(F)CF smiles:O[C](F)C(F)(F)CF H298:-210.47 kcal/mol
library:CHOF_G4 label:FCO[C](F)C(F)F smiles:FCO[C](F)C(F)F H298:-202.77 kcal/mol
library:CHOF_G4 label:CC[C](O)F smiles:CC[C](O)F H298:-72.83 kcal/mol
library:CHOF_G4 label:O[C](F)C(F)C(F)F smiles:O[C](F)C(F)C(F)F H298:-209.53 kcal/mol
library:CHOF_G4 label:O[C](F)C(O)F smiles:O[C](F)C(O)F H298:-154.59 kcal/mol
library:CHOF_G4 label:FCO[C](F)C(F)(F)F smiles:FCO[C](F)C(F)(F)F H298:-259.35 kcal/mol
library:CHOF_G4 label:C[C](F)OC(F)(F)F smiles:C[C](F)OC(F)(F)F H298:-225.46 kcal/mol
library:CHOF_G4 label:C[C](F)OCF smiles:C[C](F)OCF H298:-113.06 kcal/mol
library:CHOF_G4 label:OC[C](O)F smiles:OC[C](O)F H298:-101.33 kcal/mol
library:CHOF_G4 label:FC[C](F)OC(F)F smiles:FC[C](F)OC(F)F H298:-208.23 kcal/mol
library:CHOF_G4 label:O[C](F)C(F)(F)C(F)(F)F smiles:O[C](F)C(F)(F)C(F)(F)F H298:-315.76 kcal/mol
library:CHOF_G4 label:CO[C](F)C(F)F smiles:CO[C](F)C(F)F H298:-154.47 kcal/mol
library:CHOF_G4 label:F[C](OC(F)(F)F)C(F)(F)F smiles:F[C](OC(F)(F)F)C(F)(F)F H298:-369.50 kcal/mol
library:CHOF_G4 label:F[C](OC(F)F)C(F)F smiles:F[C](OC(F)F)C(F)F H298:-257.18 kcal/mol
library:CHOF_G4 label:CC(F)[C](O)F smiles:CC(F)[C](O)F H298:-118.30 kcal/mol
library:CHOF_G4 label:CO[C](C)F smiles:CO[C](C)F H298:-63.43 kcal/mol
library:CHOF_G4 label:O[C](F)C(F)CF smiles:O[C](F)C(F)CF H298:-159.13 kcal/mol
library:CHOF_G4 label:O[C](F)C(F)(F)F smiles:O[C](F)C(F)(F)F H298:-215.39 kcal/mol
library:CHOF_G4 label:O[C](F)C(F)C(F)(F)F smiles:O[C](F)C(F)C(F)(F)F H298:-267.84 kcal/mol
library:CHOF_G4 label:F[C](OC(F)F)C(F)(F)F smiles:F[C](OC(F)F)C(F)(F)F H298:-313.59 kcal/mol
library:CHOF_G4 label:C[C](F)OC(F)F smiles:C[C](F)OC(F)F H298:-171.06 kcal/mol
library:CHOFCl_G4 label:O[C](F)COCl smiles:O[C](F)COCl H298:-66.30 kcal/mol
library:CHOFCl_G4 label:FC[C](F)OCCl smiles:FC[C](F)OCCl H298:-110.50 kcal/mol
library:CHOFCl_G4 label:C[C](F)OCCl smiles:C[C](F)OCCl H298:-70.48 kcal/mol
library:CHOFCl_G4 label:C[C](F)OC(F)Cl smiles:C[C](F)OC(F)Cl H298:-119.89 kcal/mol
library:CHOFCl_G4 label:C[C](F)OC(Cl)Cl smiles:C[C](F)OC(Cl)Cl H298:-74.85 kcal/mol
library:CHOFClBr_G4 label:C[C](F)OC(Cl)Br smiles:C[C](F)OC(Cl)Br H298:-62.29 kcal/mol
library:CHOFBr_G4 label:C[C](F)OC(Br)Br smiles:C[C](F)OC(Br)Br H298:-49.90 kcal/mol
library:CHOFBr_G4 label:FC[C](F)OC(F)Br smiles:FC[C](F)OC(F)Br H298:-146.03 kcal/mol
library:CHOFBr_G4 label:C[C](F)OC(F)(F)Br smiles:C[C](F)OC(F)(F)Br H298:-160.03 kcal/mol
library:CHOFBr_G4 label:C[C](F)OC(F)(Br)Br smiles:C[C](F)OC(F)(Br)Br H298:-96.79 kcal/mol
library:CHOFBr_G4 label:C[C](F)OC(Br)(Br)Br smiles:C[C](F)OC(Br)(Br)Br H298:-37.98 kcal/mol
library:CHOFBr_G4 label:O[C](F)C(F)(Br)OBr smiles:O[C](F)C(F)(Br)OBr H298:-108.23 kcal/mol
library:CHOFBr_G4 label:C[C](F)OC(F)Br smiles:C[C](F)OC(F)Br H298:-106.79 kcal/mol
library:CHOFBr_G4 label:C[C](F)OCBr smiles:C[C](F)OCBr H298:-58.71 kcal/mol
library:CHOFBr_G4 label:FC[C](F)OCBr smiles:FC[C](F)OCBr H298:-98.70 kcal/mol
library:CHOFBr_G4 label:O[C](F)COBr smiles:O[C](F)COBr H298:-63.38 kcal/mol
library:CHOFBr_G4 label:FC[C](F)OC(Br)Br smiles:FC[C](F)OC(Br)Br H298:-89.16 kcal/mol
""",
)

entry(
    index = 85,
    label = "CsBr1sCsCt",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cs   u0 {1,S}
3   Ct   u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.855573,-1.68274,-2.30135,-2.78438,-3.52715,-4.06092,-4.83049],'cal/(mol*K)','+|-',[0.349461,0.358807,0.336425,0.314229,0.277314,0.24267,0.177737]),
        H298 = (85.5773,'kcal/mol','+|-',0.55826),
        S298 = (3.92811,'cal/(mol*K)','+|-',0.948739),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:BrC#C[C](Br)CBr smiles:BrC#C[C](Br)CBr H298:95.31 kcal/mol
library:CHOBr_G4 label:C[C](Br)C#CBr smiles:C[C](Br)C#CBr H298:89.46 kcal/mol
library:CHOBr_G4 label:C#C[C](Br)CBr smiles:C#C[C](Br)CBr H298:85.33 kcal/mol
library:CHOBr_G4 label:C#C[C](C)Br smiles:C#C[C](C)Br H298:79.20 kcal/mol
library:CHOFBr_G4 label:FC#C[C](Br)CBr smiles:FC#C[C](Br)CBr H298:58.24 kcal/mol
library:CHOFBr_G4 label:FC#C[C](Br)C(Br)Br smiles:FC#C[C](Br)C(Br)Br H298:66.36 kcal/mol
library:CHOFBr_G4 label:C[C](Br)C#CF smiles:C[C](Br)C#CF H298:52.54 kcal/mol
library:CHOClBr_G4 label:C[C](Br)C#CCl smiles:C[C](Br)C#CCl H298:78.67 kcal/mol
""",
)

entry(
    index = 86,
    label = "CsCl1sCsCt",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cs   u0 {1,S}
3   Ct   u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.350307,-1.14379,-1.85988,-2.46117,-3.38361,-4.01596,-4.82728],'cal/(mol*K)','+|-',[0.285333,0.292964,0.27469,0.256567,0.226426,0.198139,0.145122]),
        H298 = (85.0272,'kcal/mol','+|-',0.455817),
        S298 = (4.01523,'cal/(mol*K)','+|-',0.774642),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOCl_G4 label:C#C[C](Cl)C(Cl)(Cl)Cl smiles:C#C[C](Cl)C(Cl)(Cl)Cl H298:59.45 kcal/mol
library:CHOCl_G4 label:C#C[C](Cl)C(Cl)Cl smiles:C#C[C](Cl)C(Cl)Cl H298:60.14 kcal/mol
library:CHOCl_G4 label:C#C[C](C)Cl smiles:C#C[C](C)Cl H298:67.45 kcal/mol
library:CHOCl_G4 label:C[C](Cl)C#CCl smiles:C[C](Cl)C#CCl H298:67.00 kcal/mol
library:CHOCl_G4 label:ClC#C[C](Cl)C(Cl)Cl smiles:ClC#C[C](Cl)C(Cl)Cl H298:59.34 kcal/mol
library:CHOCl_G4 label:C#C[C](Cl)CCl smiles:C#C[C](Cl)CCl H298:63.57 kcal/mol
library:CHOCl_G4 label:ClC#C[C](Cl)C(Cl)(Cl)Cl smiles:ClC#C[C](Cl)C(Cl)(Cl)Cl H298:58.32 kcal/mol
library:CHOCl_G4 label:ClC#C[C](Cl)CCl smiles:ClC#C[C](Cl)CCl H298:62.87 kcal/mol
library:CHOFCl_G4 label:FC#C[C](Cl)CCl smiles:FC#C[C](Cl)CCl H298:36.53 kcal/mol
library:CHOFCl_G4 label:C[C](Cl)C#CF smiles:C[C](Cl)C#CF H298:40.76 kcal/mol
library:CHOFClBr_G4 label:FC#C[C](Cl)CBr smiles:FC#C[C](Cl)CBr H298:46.61 kcal/mol
library:CHOClBr_G4 label:C#C[C](Cl)CBr smiles:C#C[C](Cl)CBr H298:73.72 kcal/mol
""",
)

entry(
    index = 87,
    label = "CsCsCtF1s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   Ct  u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0421806,-0.803368,-1.58195,-2.23561,-3.19758,-3.85864,-4.81732],'cal/(mol*K)','+|-',[0.239728,0.246139,0.230786,0.21556,0.190236,0.16647,0.121926]),
        H298 = (88.1641,'kcal/mol','+|-',0.382963),
        S298 = (4.67363,'cal/(mol*K)','+|-',0.650829),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:C#C[C](F)CF smiles:C#C[C](F)CF H298:-10.04 kcal/mol
library:CHOF_G4 label:FC#C[C](F)C(F)F smiles:FC#C[C](F)C(F)F H298:-87.90 kcal/mol
library:CHOF_G4 label:C#C[C](F)C(F)(F)F smiles:C#C[C](F)C(F)(F)F H298:-117.00 kcal/mol
library:CHOF_G4 label:FC#C[C](F)CF smiles:FC#C[C](F)CF H298:-37.31 kcal/mol
library:CHOF_G4 label:C#C[C](C)F smiles:C#C[C](C)F H298:30.49 kcal/mol
library:CHOF_G4 label:C#C[C](F)C(F)F smiles:C#C[C](F)C(F)F H298:-60.55 kcal/mol
library:CHOF_G4 label:FC#C[C](F)C(F)(F)F smiles:FC#C[C](F)C(F)(F)F H298:-144.47 kcal/mol
library:CHOFCl_G4 label:FC#C[C](F)CCl smiles:FC#C[C](F)CCl H298:0.01 kcal/mol
library:CHOFCl_G4 label:C#C[C](F)CCl smiles:C#C[C](F)CCl H298:27.19 kcal/mol
library:CHOFBr_G4 label:C#C[C](F)C(F)(F)Br smiles:C#C[C](F)C(F)(F)Br H298:-53.60 kcal/mol
library:CHOFBr_G4 label:C#C[C](F)C(Br)Br smiles:C#C[C](F)C(Br)Br H298:46.59 kcal/mol
library:CHOFBr_G4 label:C#C[C](F)C(F)Br smiles:C#C[C](F)C(F)Br H298:-3.85 kcal/mol
library:CHOFBr_G4 label:C#C[C](F)CBr smiles:C#C[C](F)CBr H298:37.39 kcal/mol
library:CHOFBr_G4 label:C#C[C](F)C(Br)(Br)Br smiles:C#C[C](F)C(Br)(Br)Br H298:58.30 kcal/mol
library:CHOFBr_G4 label:FC#C[C](F)CBr smiles:FC#C[C](F)CBr H298:10.14 kcal/mol
library:CHOFBr_G4 label:FC#C[C](F)C(F)Br smiles:FC#C[C](F)C(F)Br H298:-31.15 kcal/mol
library:CHOFBr_G4 label:FC#C[C](F)C(Br)Br smiles:FC#C[C](F)C(Br)Br H298:19.40 kcal/mol
""",
)

entry(
    index = 88,
    label = "CsBr1sCdCs",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cs   u0 {1,S}
3   Cd   u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.508658,-1.28308,-1.85049,-2.32013,-3.01906,-3.47614,-4.05416],'cal/(mol*K)','+|-',[0.988423,1.01486,0.951553,0.888774,0.784361,0.686374,0.502715]),
        H298 = (84.5326,'kcal/mol','+|-',1.579),
        S298 = (0.463834,'cal/(mol*K)','+|-',2.68344),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFBr_G4 label:CDC(F)[C](C)Br smiles:C=C(F)[C](C)Br H298:-12.03 kcal/mol
""",
)

entry(
    index = 89,
    label = "CsCdCl1sCs",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cs   u0 {1,S}
3   Cd   u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.06079,-1.4982,-1.89189,-2.24122,-2.85895,-3.30708,-3.98505],'cal/(mol*K)','+|-',[0.570667,0.585929,0.54938,0.513134,0.452851,0.396279,0.290243]),
        H298 = (86.2725,'kcal/mol','+|-',0.911635),
        S298 = (-0.0146229,'cal/(mol*K)','+|-',1.54928),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOCl_G4 label:CDC(Cl)[C](Cl)C(Cl)(Cl)Cl smiles:C=C(Cl)[C](Cl)C(Cl)(Cl)Cl H298:13.21 kcal/mol
library:CHOFCl_G4 label:C[C](Cl)C(Cl)DCF smiles:C[C](Cl)C(Cl)=CF H298:-26.42 kcal/mol
library:CHOFCl_G4 label:C[C](Cl)CDC(F)F smiles:C[C](Cl)C=C(F)F H298:-68.89 kcal/mol
""",
)

entry(
    index = 90,
    label = "CsCdCsF1s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   Cd  u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.660954,-0.778589,-1.0872,-1.44258,-2.11558,-2.64316,-3.5592],'cal/(mol*K)','+|-',[0.285333,0.292964,0.27469,0.256567,0.226426,0.198139,0.145122]),
        H298 = (85.1266,'kcal/mol','+|-',0.455817),
        S298 = (0.936419,'cal/(mol*K)','+|-',0.774642),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:C[C](F)CDC(F)F smiles:C[C](F)C=C(F)F H298:-107.41 kcal/mol
library:CHOF_G4 label:CDC(F)[C](F)C(F)(F)F smiles:C=C(F)[C](F)C(F)(F)F H298:-206.94 kcal/mol
library:CHOF_G4 label:CDC(F)[C](C)F smiles:C=C(F)[C](C)F H298:-62.00 kcal/mol
library:CHOF_G4 label:CDC(F)[C](F)C(F)F smiles:C=C(F)[C](F)C(F)F H298:-152.17 kcal/mol
library:CHOFCl_G4 label:FCDC[C](F)CCl smiles:FC=C[C](F)CCl H298:-64.87 kcal/mol
library:CHOFCl_G4 label:CDC[C](F)CCl smiles:C=C[C](F)CCl H298:-21.01 kcal/mol
library:CHOFBr_G4 label:CDC[C](F)CBr smiles:C=C[C](F)CBr H298:-10.64 kcal/mol
library:CHOFBr_G4 label:CDC[C](F)C(F)Br smiles:C=C[C](F)C(F)Br H298:-52.63 kcal/mol
library:CHOFBr_G4 label:F[C](CDC(F)F)CBr smiles:F[C](C=C(F)F)CBr H298:-100.61 kcal/mol
library:CHOFBr_G4 label:CDC(F)[C](F)C(Br)Br smiles:C=C(F)[C](F)C(Br)Br H298:-45.72 kcal/mol
library:CHOFBr_G4 label:CDC[C](F)C(Br)(Br)Br smiles:C=C[C](F)C(Br)(Br)Br H298:9.44 kcal/mol
library:CHOFBr_G4 label:CDC(F)[C](F)C(F)Br smiles:C=C(F)[C](F)C(F)Br H298:-95.77 kcal/mol
""",
)

entry(
    index = 91,
    label = "CsBr1sCsCs",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cs   u0 {1,S}
3   Cs   u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.12453,-2.24419,-3.04822,-3.63799,-4.41618,-4.88254,-5.43646],'cal/(mol*K)','+|-',[0.108494,0.111395,0.104447,0.0975557,0.0860949,0.0753394,0.0551802]),
        H298 = (94.6479,'kcal/mol','+|-',0.173318),
        S298 = (5.7896,'cal/(mol*K)','+|-',0.294546),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:BrC[C](Br)COBr smiles:BrC[C](Br)COBr H298:24.77 kcal/mol
library:CHOBr_G4 label:C[C](Br)CBr smiles:C[C](Br)CBr H298:24.01 kcal/mol
library:CHOBr_G4 label:BrC[C](Br)C(Br)OBr smiles:BrC[C](Br)C(Br)OBr H298:28.95 kcal/mol
library:CHOBr_G4 label:CC[C](Br)CBr smiles:CC[C](Br)CBr H298:18.81 kcal/mol
library:CHOBr_G4 label:OC[C](Br)C(Br)Br smiles:OC[C](Br)C(Br)Br H298:-2.59 kcal/mol
library:CHOBr_G4 label:C[C](Br)COBr smiles:C[C](Br)COBr H298:20.98 kcal/mol
library:CHOBr_G4 label:BrC[C](Br)CBr smiles:BrC[C](Br)CBr H298:29.56 kcal/mol
library:CHOBr_G4 label:C[C](Br)C(Br)OBr smiles:C[C](Br)C(Br)OBr H298:22.93 kcal/mol
library:CHOBr_G4 label:BrCC[C](Br)CBr smiles:BrCC[C](Br)CBr H298:23.01 kcal/mol
library:CHOBr_G4 label:OC[C](Br)CBr smiles:OC[C](Br)CBr H298:-11.18 kcal/mol
library:CHOBr_G4 label:C[C](Br)CO smiles:C[C](Br)CO H298:-14.83 kcal/mol
library:CHOBr_G4 label:BrC[C](Br)C(Br)Br smiles:BrC[C](Br)C(Br)Br H298:37.69 kcal/mol
library:CHOBr_G4 label:C[C](Br)C(C)Br smiles:C[C](Br)C(C)Br H298:15.80 kcal/mol
library:CHOBr_G4 label:C[C](Br)C(Br)Br smiles:C[C](Br)C(Br)Br H298:31.48 kcal/mol
library:CHOBr_G4 label:C[C](C)Br smiles:C[C](C)Br H298:20.79 kcal/mol
library:CHOBr_G4 label:CC[C](C)Br smiles:CC[C](C)Br H298:15.49 kcal/mol
library:CHOBr_G4 label:C[C](Br)CC(Br)Br smiles:C[C](Br)CC(Br)Br H298:25.42 kcal/mol
library:CHOBr_G4 label:CC(Br)[C](Br)CBr smiles:CC(Br)[C](Br)CBr H298:20.58 kcal/mol
library:CHOBr_G4 label:BrC[C](Br)CC(Br)Br smiles:BrC[C](Br)CC(Br)Br H298:29.79 kcal/mol
library:CHOBr_G4 label:CC[C](Br)C(Br)Br smiles:CC[C](Br)C(Br)Br H298:25.74 kcal/mol
library:CHOBr_G4 label:C[C](Br)C(Br)CBr smiles:C[C](Br)C(Br)CBr H298:20.77 kcal/mol
library:CHOBr_G4 label:C[C](Br)CCBr smiles:C[C](Br)CCBr H298:19.87 kcal/mol
library:CHOBr_G4 label:BrCC[C](Br)C(Br)Br smiles:BrCC[C](Br)C(Br)Br H298:30.20 kcal/mol
library:CHOFClBr_G4 label:C[C](Br)C(F)(F)Cl smiles:C[C](Br)C(F)(F)Cl H298:-82.51 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)[C](Br)CBr smiles:FC(Cl)[C](Br)CBr H298:-24.53 kcal/mol
library:CHOFClBr_G4 label:C[C](Br)C(F)(Cl)Cl smiles:C[C](Br)C(F)(Cl)Cl H298:-35.04 kcal/mol
library:CHOFClBr_G4 label:C[C](Br)C(F)Cl smiles:C[C](Br)C(F)Cl H298:-31.22 kcal/mol
library:CHOFClBr_G4 label:C[C](Br)C(F)(Cl)Br smiles:C[C](Br)C(F)(Cl)Br H298:-23.23 kcal/mol
library:CHOFClBr_G4 label:CC[C](Br)C(F)Cl smiles:CC[C](Br)C(F)Cl H298:-36.77 kcal/mol
library:CHOFBr_G4 label:CC[C](Br)C(F)Br smiles:CC[C](Br)C(F)Br H298:-25.48 kcal/mol
library:CHOFBr_G4 label:FC(Br)[C](Br)C(Br)Br smiles:FC(Br)[C](Br)C(Br)Br H298:-4.62 kcal/mol
library:CHOFBr_G4 label:CC(Br)[C](Br)C(F)Br smiles:CC(Br)[C](Br)C(F)Br H298:-21.95 kcal/mol
library:CHOFBr_G4 label:FC[C](Br)COBr smiles:FC[C](Br)COBr H298:-20.65 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)[C](Br)CF smiles:OC(Br)(Br)[C](Br)CF H298:-49.19 kcal/mol
library:CHOFBr_G4 label:C[C](Br)C(F)(F)F smiles:C[C](Br)C(F)(F)F H298:-132.33 kcal/mol
library:CHOFBr_G4 label:CC[C](Br)CF smiles:CC[C](Br)CF H298:-27.34 kcal/mol
library:CHOFBr_G4 label:C[C](Br)C(F)F smiles:C[C](Br)C(F)F H298:-75.21 kcal/mol
library:CHOFBr_G4 label:CC[C](Br)C(F)(Br)Br smiles:CC[C](Br)C(F)(Br)Br H298:-16.89 kcal/mol
library:CHOFBr_G4 label:FC[C](Br)CC(Br)Br smiles:FC[C](Br)CC(Br)Br H298:-16.58 kcal/mol
library:CHOFBr_G4 label:CC[C](Br)C(F)(F)Br smiles:CC[C](Br)C(F)(F)Br H298:-75.42 kcal/mol
library:CHOFBr_G4 label:CC(Br)[C](Br)CF smiles:CC(Br)[C](Br)CF H298:-26.22 kcal/mol
library:CHOFBr_G4 label:CC(Br)(Br)[C](Br)CF smiles:CC(Br)(Br)[C](Br)CF H298:-18.80 kcal/mol
library:CHOFBr_G4 label:FC(Br)[C](Br)COBr smiles:FC(Br)[C](Br)COBr H298:-17.28 kcal/mol
library:CHOFBr_G4 label:FC(Br)(Br)[C](Br)CBr smiles:FC(Br)(Br)[C](Br)CBr H298:-4.77 kcal/mol
library:CHOFBr_G4 label:FC[C](Br)CBr smiles:FC[C](Br)CBr H298:-17.44 kcal/mol
library:CHOFBr_G4 label:CC[C](Br)C(F)F smiles:CC[C](Br)C(F)F H298:-80.45 kcal/mol
library:CHOFBr_G4 label:FC(F)[C](Br)CCBr smiles:FC(F)[C](Br)CCBr H298:-75.36 kcal/mol
library:CHOFBr_G4 label:FC(F)[C](Br)COBr smiles:FC(F)[C](Br)COBr H298:-72.40 kcal/mol
library:CHOFBr_G4 label:OC[C](Br)C(F)(F)Br smiles:OC[C](Br)C(F)(F)Br H298:-103.47 kcal/mol
library:CHOFBr_G4 label:OC[C](Br)C(F)F smiles:OC[C](Br)C(F)F H298:-108.72 kcal/mol
library:CHOFBr_G4 label:C[C](Br)CF smiles:C[C](Br)CF H298:-22.29 kcal/mol
library:CHOFBr_G4 label:FC(Br)[C](Br)CCBr smiles:FC(Br)[C](Br)CCBr H298:-19.77 kcal/mol
library:CHOFBr_G4 label:OC[C](Br)CF smiles:OC[C](Br)CF H298:-56.62 kcal/mol
library:CHOFBr_G4 label:OC[C](Br)C(F)(F)F smiles:OC[C](Br)C(F)(F)F H298:-165.95 kcal/mol
library:CHOFBr_G4 label:C[C](Br)C(F)Br smiles:C[C](Br)C(F)Br H298:-19.47 kcal/mol
library:CHOFBr_G4 label:C[C](Br)C(F)(Br)Br smiles:C[C](Br)C(F)(Br)Br H298:-11.09 kcal/mol
library:CHOFBr_G4 label:FC(F)[C](Br)C(Br)Br smiles:FC(F)[C](Br)C(Br)Br H298:-60.46 kcal/mol
library:CHOFBr_G4 label:FC(F)[C](Br)CBr smiles:FC(F)[C](Br)CBr H298:-68.74 kcal/mol
library:CHOFBr_G4 label:FC(F)(Br)[C](Br)CBr smiles:FC(F)(Br)[C](Br)CBr H298:-63.19 kcal/mol
library:CHOFBr_G4 label:FC(F)(F)[C](Br)CBr smiles:FC(F)(F)[C](Br)CBr H298:-126.04 kcal/mol
library:CHOFBr_G4 label:FC[C](Br)C(Br)(Br)Br smiles:FC[C](Br)C(Br)(Br)Br H298:3.64 kcal/mol
library:CHOFBr_G4 label:CC[C](Br)C(F)(F)F smiles:CC[C](Br)C(F)(F)F H298:-137.78 kcal/mol
library:CHOFBr_G4 label:FC[C](Br)CCBr smiles:FC[C](Br)CCBr H298:-22.64 kcal/mol
library:CHOFBr_G4 label:FC[C](Br)C(Br)OBr smiles:FC[C](Br)C(Br)OBr H298:-17.44 kcal/mol
library:CHOFBr_G4 label:CC(Br)[C](Br)C(F)F smiles:CC(Br)[C](Br)C(F)F H298:-77.75 kcal/mol
library:CHOFBr_G4 label:C[C](Br)C(F)(F)Br smiles:C[C](Br)C(F)(F)Br H298:-69.97 kcal/mol
library:CHOFBr_G4 label:FC(Br)[C](Br)CBr smiles:FC(Br)[C](Br)CBr H298:-13.34 kcal/mol
library:CHOClBr_G4 label:C[C](Br)C(Cl)(Cl)Cl smiles:C[C](Br)C(Cl)(Cl)Cl H298:9.29 kcal/mol
library:CHOClBr_G4 label:C[C](Br)C(Cl)Br smiles:C[C](Br)C(Cl)Br H298:20.57 kcal/mol
library:CHOClBr_G4 label:ClC[C](Br)CCBr smiles:ClC[C](Br)CCBr H298:13.16 kcal/mol
library:CHOClBr_G4 label:CC(Br)[C](Br)CCl smiles:CC(Br)[C](Br)CCl H298:10.75 kcal/mol
library:CHOClBr_G4 label:CC[C](Br)C(Cl)Cl smiles:CC[C](Br)C(Cl)Cl H298:3.91 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)[C](Br)CBr smiles:ClC(Cl)[C](Br)CBr H298:16.03 kcal/mol
library:CHOClBr_G4 label:C[C](Br)C(Cl)(Br)Br smiles:C[C](Br)C(Cl)(Br)Br H298:32.18 kcal/mol
library:CHOClBr_G4 label:CC[C](Br)C(Cl)Br smiles:CC[C](Br)C(Cl)Br H298:14.55 kcal/mol
library:CHOClBr_G4 label:OC[C](Br)CCl smiles:OC[C](Br)CCl H298:-20.79 kcal/mol
library:CHOClBr_G4 label:ClC[C](Br)CBr smiles:ClC[C](Br)CBr H298:19.75 kcal/mol
library:CHOClBr_G4 label:ClC[C](Br)COBr smiles:ClC[C](Br)COBr H298:15.23 kcal/mol
library:CHOClBr_G4 label:C[C](Br)C(Cl)Cl smiles:C[C](Br)C(Cl)Cl H298:9.66 kcal/mol
library:CHOClBr_G4 label:CC[C](Br)CCl smiles:CC[C](Br)CCl H298:9.02 kcal/mol
library:CHOClBr_G4 label:C[C](Br)C(Cl)(Cl)Br smiles:C[C](Br)C(Cl)(Cl)Br H298:20.53 kcal/mol
library:CHOClBr_G4 label:C[C](Br)CCl smiles:C[C](Br)CCl H298:14.16 kcal/mol
library:CHOClBr_G4 label:ClC[C](Br)C(Br)Br smiles:ClC[C](Br)C(Br)Br H298:27.64 kcal/mol
""",
)

entry(
    index = 92,
    label = "CsCl1sCsCs",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cs   u0 {1,S}
3   Cs   u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.660649,-1.76914,-2.62677,-3.28641,-4.18142,-4.71444,-5.36404],'cal/(mol*K)','+|-',[0.0873652,0.0897017,0.0841063,0.0785573,0.0693284,0.0606675,0.0444342]),
        H298 = (93.4595,'kcal/mol','+|-',0.139565),
        S298 = (5.53628,'cal/(mol*K)','+|-',0.237185),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOCl_G4 label:OC[C](Cl)C(Cl)(Cl)Cl smiles:OC[C](Cl)C(Cl)(Cl)Cl H298:-36.40 kcal/mol
library:CHOCl_G4 label:C[C](Cl)C(O)Cl smiles:C[C](Cl)C(O)Cl H298:-39.00 kcal/mol
library:CHOCl_G4 label:C[C](Cl)C(C)Cl smiles:C[C](Cl)C(C)Cl H298:-6.60 kcal/mol
library:CHOCl_G4 label:Cl[C](C(Cl)(Cl)Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:Cl[C](C(Cl)(Cl)Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-16.72 kcal/mol
library:CHOCl_G4 label:ClC[C](Cl)C(Cl)C(Cl)Cl smiles:ClC[C](Cl)C(Cl)C(Cl)Cl H298:-19.73 kcal/mol
library:CHOCl_G4 label:Cl[C](C(Cl)Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:Cl[C](C(Cl)Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-24.58 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)[C](Cl)C(Cl)Cl smiles:ClCC(Cl)[C](Cl)C(Cl)Cl H298:-20.34 kcal/mol
library:CHOCl_G4 label:Cl[C](CC(Cl)(Cl)Cl)C(Cl)Cl smiles:Cl[C](CC(Cl)(Cl)Cl)C(Cl)Cl H298:-21.34 kcal/mol
library:CHOCl_G4 label:OC[C](Cl)C(Cl)Cl smiles:OC[C](Cl)C(Cl)Cl H298:-35.87 kcal/mol
library:CHOCl_G4 label:C[C](Cl)CC(Cl)(Cl)Cl smiles:C[C](Cl)CC(Cl)(Cl)Cl H298:-11.86 kcal/mol
library:CHOCl_G4 label:C[C](Cl)CO smiles:C[C](Cl)CO H298:-26.84 kcal/mol
library:CHOCl_G4 label:Cl[C](C(Cl)Cl)C(Cl)(Cl)Cl smiles:Cl[C](C(Cl)Cl)C(Cl)(Cl)Cl H298:-9.40 kcal/mol
library:CHOCl_G4 label:Cl[C](CC(Cl)Cl)C(Cl)Cl smiles:Cl[C](CC(Cl)Cl)C(Cl)Cl H298:-19.06 kcal/mol
library:CHOCl_G4 label:Cl[C](C(Cl)C(Cl)Cl)C(Cl)(Cl)Cl smiles:Cl[C](C(Cl)C(Cl)Cl)C(Cl)(Cl)Cl H298:-21.79 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(Cl)[C](Cl)C(Cl)Cl smiles:ClCC(Cl)(Cl)[C](Cl)C(Cl)Cl H298:-23.48 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)(Cl)[C](Cl)C(Cl)Cl smiles:ClOC(Cl)(Cl)[C](Cl)C(Cl)Cl H298:-13.34 kcal/mol
library:CHOCl_G4 label:ClOC[C](Cl)C(Cl)Cl smiles:ClOC[C](Cl)C(Cl)Cl H298:-2.32 kcal/mol
library:CHOCl_G4 label:OC(Cl)[C](Cl)CCl smiles:OC(Cl)[C](Cl)CCl H298:-42.21 kcal/mol
library:CHOCl_G4 label:CC(Cl)[C](Cl)C(Cl)(Cl)Cl smiles:CC(Cl)[C](Cl)C(Cl)(Cl)Cl H298:-15.74 kcal/mol
library:CHOCl_G4 label:OC(Cl)[C](Cl)C(Cl)(Cl)Cl smiles:OC(Cl)[C](Cl)C(Cl)(Cl)Cl H298:-46.92 kcal/mol
library:CHOCl_G4 label:ClC[C](Cl)C(Cl)(Cl)CCl smiles:ClC[C](Cl)C(Cl)(Cl)CCl H298:-20.16 kcal/mol
library:CHOCl_G4 label:C[C](Cl)C(O)(Cl)Cl smiles:C[C](Cl)C(O)(Cl)Cl H298:-44.31 kcal/mol
library:CHOCl_G4 label:ClC[C](Cl)COCl smiles:ClC[C](Cl)COCl H298:0.30 kcal/mol
library:CHOCl_G4 label:ClC[C](Cl)CCl smiles:ClC[C](Cl)CCl H298:-2.08 kcal/mol
library:CHOCl_G4 label:C[C](Cl)C(Cl)(Cl)C(Cl)Cl smiles:C[C](Cl)C(Cl)(Cl)C(Cl)Cl H298:-18.38 kcal/mol
library:CHOCl_G4 label:C[C](Cl)C(Cl)(Cl)OCl smiles:C[C](Cl)C(Cl)(Cl)OCl H298:-6.39 kcal/mol
library:CHOCl_G4 label:C[C](Cl)CCCl smiles:C[C](Cl)CCCl H298:-4.19 kcal/mol
library:CHOCl_G4 label:Cl[C](C(Cl)Cl)C(Cl)C(Cl)(Cl)Cl smiles:Cl[C](C(Cl)Cl)C(Cl)C(Cl)(Cl)Cl H298:-24.00 kcal/mol
library:CHOCl_G4 label:ClC[C](Cl)C(Cl)OCl smiles:ClC[C](Cl)C(Cl)OCl H298:-6.23 kcal/mol
library:CHOCl_G4 label:CC[C](Cl)C(Cl)(Cl)Cl smiles:CC[C](Cl)C(Cl)(Cl)Cl H298:-8.43 kcal/mol
library:CHOCl_G4 label:CC[C](C)Cl smiles:CC[C](C)Cl H298:3.30 kcal/mol
library:CHOCl_G4 label:ClCC[C](Cl)CCl smiles:ClCC[C](Cl)CCl H298:-9.44 kcal/mol
library:CHOCl_G4 label:C[C](Cl)C(Cl)OCl smiles:C[C](Cl)C(Cl)OCl H298:-2.41 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)[C](Cl)C(Cl)Cl smiles:ClOC(Cl)[C](Cl)C(Cl)Cl H298:-10.11 kcal/mol
library:CHOCl_G4 label:C[C](C)Cl smiles:C[C](C)Cl H298:8.52 kcal/mol
library:CHOCl_G4 label:C[C](Cl)C(Cl)Cl smiles:C[C](Cl)C(Cl)Cl H298:-2.39 kcal/mol
library:CHOCl_G4 label:Cl[C](C(Cl)C(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:Cl[C](C(Cl)C(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-24.34 kcal/mol
library:CHOCl_G4 label:Cl[C](C(Cl)Cl)C(Cl)C(Cl)Cl smiles:Cl[C](C(Cl)Cl)C(Cl)C(Cl)Cl H298:-23.93 kcal/mol
library:CHOCl_G4 label:CC(Cl)(Cl)[C](Cl)C(Cl)(Cl)Cl smiles:CC(Cl)(Cl)[C](Cl)C(Cl)(Cl)Cl H298:-15.87 kcal/mol
library:CHOCl_G4 label:ClCC[C](Cl)C(Cl)(Cl)Cl smiles:ClCC[C](Cl)C(Cl)(Cl)Cl H298:-14.07 kcal/mol
library:CHOCl_G4 label:C[C](Cl)C(Cl)C(Cl)(Cl)Cl smiles:C[C](Cl)C(Cl)C(Cl)(Cl)Cl H298:-16.38 kcal/mol
library:CHOCl_G4 label:OC(Cl)(Cl)[C](Cl)CCl smiles:OC(Cl)(Cl)[C](Cl)CCl H298:-48.34 kcal/mol
library:CHOCl_G4 label:C[C](Cl)CCl smiles:C[C](Cl)CCl H298:1.64 kcal/mol
library:CHOCl_G4 label:Cl[C](C(Cl)Cl)C(Cl)Cl smiles:Cl[C](C(Cl)Cl)C(Cl)Cl H298:-9.43 kcal/mol
library:CHOCl_G4 label:C[C](Cl)C(Cl)CCl smiles:C[C](Cl)C(Cl)CCl H298:-12.17 kcal/mol
library:CHOCl_G4 label:OC(Cl)[C](Cl)C(Cl)Cl smiles:OC(Cl)[C](Cl)C(Cl)Cl H298:-45.33 kcal/mol
library:CHOCl_G4 label:OC(Cl)(Cl)[C](Cl)C(Cl)(Cl)Cl smiles:OC(Cl)(Cl)[C](Cl)C(Cl)(Cl)Cl H298:-47.82 kcal/mol
library:CHOCl_G4 label:ClC[C](Cl)C(Cl)(Cl)Cl smiles:ClC[C](Cl)C(Cl)(Cl)Cl H298:-6.57 kcal/mol
library:CHOCl_G4 label:CC[C](Cl)CCl smiles:CC[C](Cl)CCl H298:-2.97 kcal/mol
library:CHOCl_G4 label:ClC[C](Cl)C(Cl)CCl smiles:ClC[C](Cl)C(Cl)CCl H298:-16.07 kcal/mol
library:CHOCl_G4 label:C[C](Cl)COCl smiles:C[C](Cl)COCl H298:5.72 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)[C](Cl)C(Cl)(Cl)Cl smiles:ClOC(Cl)[C](Cl)C(Cl)(Cl)Cl H298:-9.56 kcal/mol
library:CHOCl_G4 label:C[C](Cl)C(Cl)(Cl)CCl smiles:C[C](Cl)C(Cl)(Cl)CCl H298:-16.05 kcal/mol
library:CHOCl_G4 label:CC(Cl)(Cl)[C](Cl)C(Cl)Cl smiles:CC(Cl)(Cl)[C](Cl)C(Cl)Cl H298:-17.08 kcal/mol
library:CHOCl_G4 label:OC(Cl)(Cl)[C](Cl)C(Cl)Cl smiles:OC(Cl)(Cl)[C](Cl)C(Cl)Cl H298:-51.56 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(Cl)[C](Cl)C(Cl)(Cl)Cl smiles:ClCC(Cl)(Cl)[C](Cl)C(Cl)(Cl)Cl H298:-18.78 kcal/mol
library:CHOCl_G4 label:ClC[C](Cl)C(Cl)(Cl)OCl smiles:ClC[C](Cl)C(Cl)(Cl)OCl H298:-9.96 kcal/mol
library:CHOCl_G4 label:Cl[C](C(Cl)Cl)C(Cl)(Cl)C(Cl)Cl smiles:Cl[C](C(Cl)Cl)C(Cl)(Cl)C(Cl)Cl H298:-23.49 kcal/mol
library:CHOCl_G4 label:C[C](Cl)C(Cl)(Cl)Cl smiles:C[C](Cl)C(Cl)(Cl)Cl H298:-2.88 kcal/mol
library:CHOCl_G4 label:ClC[C](Cl)CC(Cl)Cl smiles:ClC[C](Cl)CC(Cl)Cl H298:-15.23 kcal/mol
library:CHOCl_G4 label:ClC[C](Cl)CC(Cl)(Cl)Cl smiles:ClC[C](Cl)CC(Cl)(Cl)Cl H298:-17.54 kcal/mol
library:CHOCl_G4 label:Cl[C](C(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:Cl[C](C(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-4.50 kcal/mol
library:CHOCl_G4 label:CC[C](Cl)C(Cl)Cl smiles:CC[C](Cl)C(Cl)Cl H298:-7.55 kcal/mol
library:CHOCl_G4 label:OC[C](Cl)CCl smiles:OC[C](Cl)CCl H298:-32.73 kcal/mol
library:CHOCl_G4 label:C[C](Cl)CC(Cl)Cl smiles:C[C](Cl)CC(Cl)Cl H298:-9.56 kcal/mol
library:CHOCl_G4 label:CC(Cl)[C](Cl)CCl smiles:CC(Cl)[C](Cl)CCl H298:-11.06 kcal/mol
library:CHOCl_G4 label:Cl[C](C(Cl)(Cl)Cl)C(Cl)(Cl)C(Cl)Cl smiles:Cl[C](C(Cl)(Cl)Cl)C(Cl)(Cl)C(Cl)Cl H298:-20.81 kcal/mol
library:CHOCl_G4 label:ClCC[C](Cl)C(Cl)Cl smiles:ClCC[C](Cl)C(Cl)Cl H298:-13.36 kcal/mol
library:CHOCl_G4 label:ClOC[C](Cl)C(Cl)(Cl)Cl smiles:ClOC[C](Cl)C(Cl)(Cl)Cl H298:-2.49 kcal/mol
library:CHOCl_G4 label:CC(Cl)(Cl)[C](Cl)CCl smiles:CC(Cl)(Cl)[C](Cl)CCl H298:-16.13 kcal/mol
library:CHOCl_G4 label:C[C](Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:C[C](Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-16.20 kcal/mol
library:CHOCl_G4 label:Cl[C](CC(Cl)Cl)C(Cl)(Cl)Cl smiles:Cl[C](CC(Cl)Cl)C(Cl)(Cl)Cl H298:-19.62 kcal/mol
library:CHOCl_G4 label:C[C](Cl)C(C)(Cl)Cl smiles:C[C](Cl)C(C)(Cl)Cl H298:-12.17 kcal/mol
library:CHOCl_G4 label:C[C](Cl)C(Cl)C(Cl)Cl smiles:C[C](Cl)C(Cl)C(Cl)Cl H298:-15.61 kcal/mol
library:CHOCl_G4 label:CC(Cl)[C](Cl)C(Cl)Cl smiles:CC(Cl)[C](Cl)C(Cl)Cl H298:-15.02 kcal/mol
library:CHOCl_G4 label:ClC[C](Cl)C(Cl)Cl smiles:ClC[C](Cl)C(Cl)Cl H298:-5.75 kcal/mol
library:CHOFCl_G4 label:FC(F)[C](Cl)CCl smiles:FC(F)[C](Cl)CCl H298:-90.78 kcal/mol
library:CHOFCl_G4 label:CC[C](Cl)C(F)Cl smiles:CC[C](Cl)C(F)Cl H298:-48.62 kcal/mol
library:CHOFCl_G4 label:OC(Cl)[C](Cl)CF smiles:OC(Cl)[C](Cl)CF H298:-79.35 kcal/mol
library:CHOFCl_G4 label:CC[C](Cl)CF smiles:CC[C](Cl)CF H298:-39.51 kcal/mol
library:CHOFCl_G4 label:FC[C](Cl)CCCl smiles:FC[C](Cl)CCCl H298:-45.29 kcal/mol
library:CHOFCl_G4 label:FC[C](Cl)C(Cl)Cl smiles:FC[C](Cl)C(Cl)Cl H298:-42.16 kcal/mol
library:CHOFCl_G4 label:FC(Cl)[C](Cl)CCl smiles:FC(Cl)[C](Cl)CCl H298:-46.39 kcal/mol
library:CHOFCl_G4 label:FC[C](Cl)COCl smiles:FC[C](Cl)COCl H298:-35.98 kcal/mol
library:CHOFCl_G4 label:C[C](Cl)C(F)(F)Cl smiles:C[C](Cl)C(F)(F)Cl H298:-94.63 kcal/mol
library:CHOFCl_G4 label:CC(Cl)[C](Cl)CF smiles:CC(Cl)[C](Cl)CF H298:-48.23 kcal/mol
library:CHOFCl_G4 label:C[C](Cl)C(F)(Cl)Cl smiles:C[C](Cl)C(F)(Cl)Cl H298:-47.18 kcal/mol
library:CHOFCl_G4 label:C[C](Cl)C(F)F smiles:C[C](Cl)C(F)F H298:-87.42 kcal/mol
library:CHOFCl_G4 label:CC[C](Cl)C(F)F smiles:CC[C](Cl)C(F)F H298:-92.56 kcal/mol
library:CHOFCl_G4 label:C[C](Cl)C(F)Cl smiles:C[C](Cl)C(F)Cl H298:-43.06 kcal/mol
library:CHOFCl_G4 label:C[C](Cl)C(F)(F)F smiles:C[C](Cl)C(F)(F)F H298:-144.47 kcal/mol
library:CHOFCl_G4 label:C[C](Cl)CF smiles:C[C](Cl)CF H298:-34.58 kcal/mol
library:CHOFCl_G4 label:OC[C](Cl)CF smiles:OC[C](Cl)CF H298:-68.62 kcal/mol
library:CHOFCl_G4 label:FC[C](Cl)CCl smiles:FC[C](Cl)CCl H298:-39.14 kcal/mol
library:CHOFClBr_G4 label:CC(Br)[C](Cl)CF smiles:CC(Br)[C](Cl)CF H298:-38.00 kcal/mol
library:CHOFClBr_G4 label:FC[C](Cl)CBr smiles:FC[C](Cl)CBr H298:-29.40 kcal/mol
library:CHOFClBr_G4 label:FC[C](Cl)C(Br)Br smiles:FC[C](Cl)C(Br)Br H298:-20.38 kcal/mol
library:CHOFClBr_G4 label:FC[C](Cl)COBr smiles:FC[C](Cl)COBr H298:-32.26 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)[C](Cl)CBr smiles:FC(Cl)[C](Cl)CBr H298:-36.80 kcal/mol
library:CHOFClBr_G4 label:FC[C](Cl)C(Cl)Br smiles:FC[C](Cl)C(Cl)Br H298:-31.68 kcal/mol
library:CHOFClBr_G4 label:FC[C](Cl)CCBr smiles:FC[C](Cl)CCBr H298:-34.28 kcal/mol
library:CHOFClBr_G4 label:FC(F)[C](Cl)CBr smiles:FC(F)[C](Cl)CBr H298:-80.76 kcal/mol
library:CHOClBr_G4 label:ClC[C](Cl)C(Cl)Br smiles:ClC[C](Cl)C(Cl)Br H298:5.13 kcal/mol
library:CHOClBr_G4 label:C[C](Cl)C(Br)CBr smiles:C[C](Cl)C(Br)CBr H298:8.85 kcal/mol
library:CHOClBr_G4 label:C[C](Cl)C(C)(Cl)Br smiles:C[C](Cl)C(C)(Cl)Br H298:-1.19 kcal/mol
library:CHOClBr_G4 label:C[C](Cl)CC(Cl)Br smiles:C[C](Cl)CC(Cl)Br H298:2.04 kcal/mol
library:CHOClBr_G4 label:CC(Br)[C](Cl)CCl smiles:CC(Br)[C](Cl)CCl H298:-1.12 kcal/mol
library:CHOClBr_G4 label:C[C](Cl)C(Cl)(Cl)Br smiles:C[C](Cl)C(Cl)(Cl)Br H298:8.47 kcal/mol
library:CHOClBr_G4 label:Cl[C](CBr)C(Cl)Cl smiles:Cl[C](CBr)C(Cl)Cl H298:4.24 kcal/mol
library:CHOClBr_G4 label:ClC[C](Cl)CCBr smiles:ClC[C](Cl)CCBr H298:1.49 kcal/mol
library:CHOClBr_G4 label:C[C](Cl)CC(Br)Br smiles:C[C](Cl)CC(Br)Br H298:13.45 kcal/mol
library:CHOClBr_G4 label:C[C](Cl)C(Cl)(Br)Br smiles:C[C](Cl)C(Cl)(Br)Br H298:19.95 kcal/mol
library:CHOClBr_G4 label:C[C](Cl)COBr smiles:C[C](Cl)COBr H298:9.00 kcal/mol
library:CHOClBr_G4 label:ClC[C](Cl)C(Br)Br smiles:ClC[C](Cl)C(Br)Br H298:15.85 kcal/mol
library:CHOClBr_G4 label:C[C](Cl)C(C)(Br)Br smiles:C[C](Cl)C(C)(Br)Br H298:9.75 kcal/mol
library:CHOClBr_G4 label:C[C](Cl)C(Cl)CBr smiles:C[C](Cl)C(Cl)CBr H298:-1.49 kcal/mol
library:CHOClBr_G4 label:C[C](Cl)CBr smiles:C[C](Cl)CBr H298:11.83 kcal/mol
library:CHOClBr_G4 label:C[C](Cl)C(Cl)Br smiles:C[C](Cl)C(Cl)Br H298:8.62 kcal/mol
library:CHOClBr_G4 label:C[C](Cl)C(Cl)OBr smiles:C[C](Cl)C(Cl)OBr H298:0.32 kcal/mol
library:CHOClBr_G4 label:C[C](Cl)CCBr smiles:C[C](Cl)CCBr H298:7.77 kcal/mol
library:CHOClBr_G4 label:ClC[C](Cl)CBr smiles:ClC[C](Cl)CBr H298:7.80 kcal/mol
library:CHOClBr_G4 label:ClC[C](Cl)COBr smiles:ClC[C](Cl)COBr H298:3.31 kcal/mol
library:CHOClBr_G4 label:C[C](Cl)C(O)(Cl)Br smiles:C[C](Cl)C(O)(Cl)Br H298:-32.05 kcal/mol
library:CHOClBr_G4 label:C[C](Cl)C(O)(Br)Br smiles:C[C](Cl)C(O)(Br)Br H298:-20.48 kcal/mol
library:CHOClBr_G4 label:C[C](Cl)C(C)Br smiles:C[C](Cl)C(C)Br H298:3.78 kcal/mol
library:CHOClBr_G4 label:C[C](Cl)C(Br)(Br)Br smiles:C[C](Cl)C(Br)(Br)Br H298:31.60 kcal/mol
library:CHOClBr_G4 label:C[C](Cl)C(Br)Br smiles:C[C](Cl)C(Br)Br H298:19.24 kcal/mol
library:CHOClBr_G4 label:C[C](Cl)C(Br)OBr smiles:C[C](Cl)C(Br)OBr H298:11.03 kcal/mol
""",
)

entry(
    index = 93,
    label = "CsCsCsF1s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.728544,-1.92787,-2.68421,-3.20251,-3.90566,-4.37599,-5.03676],'cal/(mol*K)','+|-',[0.0796495,0.0817796,0.0766784,0.0716195,0.0632057,0.0553097,0.04051]),
        H298 = (97.6148,'kcal/mol','+|-',0.127239),
        S298 = (4.76327,'cal/(mol*K)','+|-',0.216238),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:FC[C](F)COF smiles:FC[C](F)COF H298:-77.20 kcal/mol
library:CHOF_G4 label:CC(F)(F)[C](F)C(F)F smiles:CC(F)(F)[C](F)C(F)F H298:-225.82 kcal/mol
library:CHOF_G4 label:C[C](F)C(F)(F)F smiles:C[C](F)C(F)(F)F H298:-181.00 kcal/mol
library:CHOF_G4 label:CC(F)[C](F)C(F)(F)F smiles:CC(F)[C](F)C(F)(F)F H298:-229.23 kcal/mol
library:CHOF_G4 label:F[C](CC(F)F)C(F)(F)F smiles:F[C](CC(F)F)C(F)(F)F H298:-282.94 kcal/mol
library:CHOF_G4 label:FCC[C](F)CF smiles:FCC[C](F)CF H298:-120.69 kcal/mol
library:CHOF_G4 label:F[C](C(F)C(F)(F)F)C(F)(F)F smiles:F[C](C(F)C(F)(F)F)C(F)(F)F H298:-377.54 kcal/mol
library:CHOF_G4 label:F[C](C(F)F)C(F)C(F)F smiles:F[C](C(F)F)C(F)C(F)F H298:-265.03 kcal/mol
library:CHOF_G4 label:OC[C](F)CF smiles:OC[C](F)CF H298:-105.83 kcal/mol
library:CHOF_G4 label:OC[C](F)C(F)F smiles:OC[C](F)C(F)F H298:-156.69 kcal/mol
library:CHOF_G4 label:FC[C](F)C(F)CF smiles:FC[C](F)C(F)CF H298:-164.41 kcal/mol
library:CHOF_G4 label:F[C](C(F)F)C(F)C(F)(F)F smiles:F[C](C(F)F)C(F)C(F)(F)F H298:-322.08 kcal/mol
library:CHOF_G4 label:F[C](C(F)F)C(F)(F)C(F)(F)F smiles:F[C](C(F)F)C(F)(F)C(F)(F)F H298:-370.23 kcal/mol
library:CHOF_G4 label:C[C](F)C(C)F smiles:C[C](F)C(C)F H298:-81.96 kcal/mol
library:CHOF_G4 label:F[C](CC(F)(F)F)C(F)(F)F smiles:F[C](CC(F)(F)F)C(F)(F)F H298:-340.74 kcal/mol
library:CHOF_G4 label:OC(F)[C](F)CF smiles:OC(F)[C](F)CF H298:-159.85 kcal/mol
library:CHOF_G4 label:FC[C](F)C(F)(F)OF smiles:FC[C](F)C(F)(F)OF H298:-177.88 kcal/mol
library:CHOF_G4 label:OC(F)(F)[C](F)C(F)F smiles:OC(F)(F)[C](F)C(F)F H298:-264.35 kcal/mol
library:CHOF_G4 label:CC(F)(F)[C](F)C(F)(F)F smiles:CC(F)(F)[C](F)C(F)(F)F H298:-281.67 kcal/mol
library:CHOF_G4 label:CC[C](F)CF smiles:CC[C](F)CF H298:-76.98 kcal/mol
library:CHOF_G4 label:OC(F)[C](F)C(F)(F)F smiles:OC(F)[C](F)C(F)(F)F H298:-264.03 kcal/mol
library:CHOF_G4 label:FC[C](F)CC(F)(F)F smiles:FC[C](F)CC(F)(F)F H298:-233.87 kcal/mol
library:CHOF_G4 label:C[C](F)CCF smiles:C[C](F)CCF H298:-78.82 kcal/mol
library:CHOF_G4 label:OC(F)(F)[C](F)CF smiles:OC(F)(F)[C](F)CF H298:-215.76 kcal/mol
library:CHOF_G4 label:FC[C](F)C(F)(F)CF smiles:FC[C](F)C(F)(F)CF H298:-216.35 kcal/mol
library:CHOF_G4 label:OC[C](F)C(F)(F)F smiles:OC[C](F)C(F)(F)F H298:-213.59 kcal/mol
library:CHOF_G4 label:C[C](F)CF smiles:C[C](F)CF H298:-72.41 kcal/mol
library:CHOF_G4 label:FOC(F)(F)[C](F)C(F)(F)F smiles:FOC(F)(F)[C](F)C(F)(F)F H298:-281.16 kcal/mol
library:CHOF_G4 label:C[C](F)C(F)(F)C(F)F smiles:C[C](F)C(F)(F)C(F)F H298:-226.32 kcal/mol
library:CHOF_G4 label:OC(F)[C](F)C(F)F smiles:OC(F)[C](F)C(F)F H298:-208.27 kcal/mol
library:CHOF_G4 label:C[C](F)C(F)F smiles:C[C](F)C(F)F H298:-123.81 kcal/mol
library:CHOF_G4 label:FC[C](F)C(F)C(F)(F)F smiles:FC[C](F)C(F)C(F)(F)F H298:-272.55 kcal/mol
library:CHOF_G4 label:OC(F)(F)[C](F)C(F)(F)F smiles:OC(F)(F)[C](F)C(F)(F)F H298:-319.90 kcal/mol
library:CHOF_G4 label:C[C](F)COF smiles:C[C](F)COF H298:-36.67 kcal/mol
library:CHOF_G4 label:FC[C](F)C(F)F smiles:FC[C](F)C(F)F H298:-163.54 kcal/mol
library:CHOF_G4 label:F[C](C(F)F)C(F)F smiles:F[C](C(F)F)C(F)F H298:-212.85 kcal/mol
library:CHOF_G4 label:CC[C](C)F smiles:CC[C](C)F H298:-34.12 kcal/mol
library:CHOF_G4 label:C[C](F)C(F)CF smiles:C[C](F)C(F)CF H298:-123.71 kcal/mol
library:CHOF_G4 label:FOC[C](F)C(F)F smiles:FOC[C](F)C(F)F H298:-128.29 kcal/mol
library:CHOF_G4 label:C[C](F)C(F)C(F)F smiles:C[C](F)C(F)C(F)F H298:-175.27 kcal/mol
library:CHOF_G4 label:FCC(F)[C](F)C(F)F smiles:FCC(F)[C](F)C(F)F H298:-213.67 kcal/mol
library:CHOF_G4 label:FCC[C](F)C(F)(F)F smiles:FCC[C](F)C(F)(F)F H298:-228.53 kcal/mol
library:CHOF_G4 label:CC(F)[C](F)CF smiles:CC(F)[C](F)CF H298:-122.61 kcal/mol
library:CHOF_G4 label:F[C](CC(F)F)C(F)F smiles:F[C](CC(F)F)C(F)F H298:-226.13 kcal/mol
library:CHOF_G4 label:C[C](F)C(F)(F)OF smiles:C[C](F)C(F)(F)OF H298:-141.17 kcal/mol
library:CHOF_G4 label:C[C](F)CC(F)(F)F smiles:C[C](F)CC(F)(F)F H298:-192.25 kcal/mol
library:CHOF_G4 label:C[C](F)CC(F)F smiles:C[C](F)CC(F)F H298:-133.50 kcal/mol
library:CHOF_G4 label:C[C](F)C(F)(F)CF smiles:C[C](F)C(F)(F)CF H298:-176.60 kcal/mol
library:CHOF_G4 label:C[C](F)CO smiles:C[C](F)CO H298:-64.24 kcal/mol
library:CHOF_G4 label:FOC[C](F)C(F)(F)F smiles:FOC[C](F)C(F)(F)F H298:-184.13 kcal/mol
library:CHOF_G4 label:CC[C](F)C(F)F smiles:CC[C](F)C(F)F H298:-129.32 kcal/mol
library:CHOF_G4 label:FOC(F)[C](F)C(F)F smiles:FOC(F)[C](F)C(F)F H298:-174.88 kcal/mol
library:CHOF_G4 label:F[C](C(F)(F)F)C(F)(F)F smiles:F[C](C(F)(F)F)C(F)(F)F H298:-324.37 kcal/mol
library:CHOF_G4 label:C[C](F)C(O)(F)F smiles:C[C](F)C(O)(F)F H298:-175.76 kcal/mol
library:CHOF_G4 label:FC[C](F)C(F)(F)C(F)F smiles:FC[C](F)C(F)(F)C(F)F H298:-265.63 kcal/mol
library:CHOF_G4 label:F[C](CC(F)(F)F)C(F)F smiles:F[C](CC(F)(F)F)C(F)F H298:-284.65 kcal/mol
library:CHOF_G4 label:CC(F)(F)[C](F)CF smiles:CC(F)(F)[C](F)CF H298:-177.61 kcal/mol
library:CHOF_G4 label:C[C](F)C(F)C(F)(F)F smiles:C[C](F)C(F)C(F)(F)F H298:-233.05 kcal/mol
library:CHOF_G4 label:FC[C](F)CF smiles:FC[C](F)CF H298:-112.54 kcal/mol
library:CHOF_G4 label:F[C](C(F)C(F)F)C(F)(F)F smiles:F[C](C(F)C(F)F)C(F)(F)F H298:-323.18 kcal/mol
library:CHOF_G4 label:CC(F)[C](F)C(F)F smiles:CC(F)[C](F)C(F)F H298:-173.42 kcal/mol
library:CHOF_G4 label:FC[C](F)C(F)C(F)F smiles:FC[C](F)C(F)C(F)F H298:-215.26 kcal/mol
library:CHOF_G4 label:FOC(F)(F)[C](F)C(F)F smiles:FOC(F)(F)[C](F)C(F)F H298:-226.30 kcal/mol
library:CHOF_G4 label:CC[C](F)C(F)(F)F smiles:CC[C](F)C(F)(F)F H298:-186.89 kcal/mol
library:CHOF_G4 label:FOC(F)[C](F)C(F)(F)F smiles:FOC(F)[C](F)C(F)(F)F H298:-230.57 kcal/mol
library:CHOF_G4 label:FC[C](F)CC(F)F smiles:FC[C](F)CC(F)F H298:-174.52 kcal/mol
library:CHOF_G4 label:C[C](F)C(O)F smiles:C[C](F)C(O)F H298:-118.43 kcal/mol
library:CHOF_G4 label:C[C](F)C(C)(F)F smiles:C[C](F)C(C)(F)F H298:-139.18 kcal/mol
library:CHOF_G4 label:FCC[C](F)C(F)F smiles:FCC[C](F)C(F)F H298:-172.15 kcal/mol
library:CHOF_G4 label:C[C](F)C(F)(F)C(F)(F)F smiles:C[C](F)C(F)(F)C(F)(F)F H298:-282.55 kcal/mol
library:CHOF_G4 label:C[C](C)F smiles:C[C](C)F H298:-29.49 kcal/mol
library:CHOF_G4 label:FCC(F)(F)[C](F)C(F)F smiles:FCC(F)(F)[C](F)C(F)F H298:-265.12 kcal/mol
library:CHOF_G4 label:FC[C](F)C(F)(F)F smiles:FC[C](F)C(F)(F)F H298:-220.17 kcal/mol
library:CHOF_G4 label:F[C](C(F)F)C(F)(F)F smiles:F[C](C(F)F)C(F)(F)F H298:-269.03 kcal/mol
library:CHOF_G4 label:F[C](C(F)(F)F)C(F)(F)C(F)F smiles:F[C](C(F)(F)F)C(F)(F)C(F)F H298:-369.87 kcal/mol
library:CHOF_G4 label:FCC(F)[C](F)C(F)(F)F smiles:FCC(F)[C](F)C(F)(F)F H298:-270.94 kcal/mol
library:CHOF_G4 label:F[C](C(F)(F)F)C(F)(F)C(F)(F)F smiles:F[C](C(F)(F)F)C(F)(F)C(F)(F)F H298:-425.34 kcal/mol
library:CHOFCl_G4 label:C[C](F)CC(F)Cl smiles:C[C](F)CC(F)Cl H298:-87.60 kcal/mol
library:CHOFCl_G4 label:FC[C](F)CCCl smiles:FC[C](F)CCCl H298:-82.72 kcal/mol
library:CHOFCl_G4 label:C[C](F)CC(Cl)Cl smiles:C[C](F)CC(Cl)Cl H298:-46.43 kcal/mol
library:CHOFCl_G4 label:C[C](F)CCCl smiles:C[C](F)CCCl H298:-41.37 kcal/mol
library:CHOFCl_G4 label:C[C](F)C(F)(F)Cl smiles:C[C](F)C(F)(F)Cl H298:-131.02 kcal/mol
library:CHOFCl_G4 label:C[C](F)C(C)Cl smiles:C[C](F)C(C)Cl H298:-43.56 kcal/mol
library:CHOFCl_G4 label:C[C](F)C(O)Cl smiles:C[C](F)C(O)Cl H298:-75.09 kcal/mol
library:CHOFCl_G4 label:C[C](F)C(O)(Cl)Cl smiles:C[C](F)C(O)(Cl)Cl H298:-81.14 kcal/mol
library:CHOFCl_G4 label:CC(Cl)[C](F)CF smiles:CC(Cl)[C](F)CF H298:-83.32 kcal/mol
library:CHOFCl_G4 label:C[C](F)C(Cl)CCl smiles:C[C](F)C(Cl)CCl H298:-48.64 kcal/mol
library:CHOFCl_G4 label:C[C](F)C(F)CCl smiles:C[C](F)C(F)CCl H298:-86.27 kcal/mol
library:CHOFCl_G4 label:FC[C](F)C(Cl)Cl smiles:FC[C](F)C(Cl)Cl H298:-78.10 kcal/mol
library:CHOFCl_G4 label:C[C](F)C(Cl)(Cl)Cl smiles:C[C](F)C(Cl)(Cl)Cl H298:-39.91 kcal/mol
library:CHOFCl_G4 label:C[C](F)C(F)OCl smiles:C[C](F)C(F)OCl H298:-81.67 kcal/mol
library:CHOFCl_G4 label:C[C](F)C(Cl)OCl smiles:C[C](F)C(Cl)OCl H298:-37.99 kcal/mol
library:CHOFCl_G4 label:F[C](CCl)C(F)F smiles:F[C](CCl)C(F)F H298:-126.69 kcal/mol
library:CHOFCl_G4 label:C[C](F)CCl smiles:C[C](F)CCl H298:-35.38 kcal/mol
library:CHOFCl_G4 label:OC(Cl)[C](F)CF smiles:OC(Cl)[C](F)CF H298:-114.67 kcal/mol
library:CHOFCl_G4 label:C[C](F)C(C)(F)Cl smiles:C[C](F)C(C)(F)Cl H298:-91.54 kcal/mol
library:CHOFCl_G4 label:C[C](F)COCl smiles:C[C](F)COCl H298:-31.96 kcal/mol
library:CHOFCl_G4 label:C[C](F)C(F)Cl smiles:C[C](F)C(F)Cl H298:-79.35 kcal/mol
library:CHOFCl_G4 label:FC[C](F)CCl smiles:FC[C](F)CCl H298:-75.55 kcal/mol
library:CHOFCl_G4 label:FC[C](F)COCl smiles:FC[C](F)COCl H298:-72.18 kcal/mol
library:CHOFCl_G4 label:C[C](F)C(Cl)Cl smiles:C[C](F)C(Cl)Cl H298:-38.78 kcal/mol
library:CHOFCl_G4 label:C[C](F)C(F)(Cl)Cl smiles:C[C](F)C(F)(Cl)Cl H298:-83.66 kcal/mol
library:CHOFCl_G4 label:C[C](F)C(C)(Cl)Cl smiles:C[C](F)C(C)(Cl)Cl H298:-49.18 kcal/mol
library:CHOFCl_G4 label:FC[C](F)C(F)Cl smiles:FC[C](F)C(F)Cl H298:-118.86 kcal/mol
library:CHOFClBr_G4 label:C[C](F)C(Cl)(Br)Br smiles:C[C](F)C(Cl)(Br)Br H298:-16.59 kcal/mol
library:CHOFClBr_G4 label:C[C](F)C(F)(Cl)Br smiles:C[C](F)C(F)(Cl)Br H298:-71.73 kcal/mol
library:CHOFClBr_G4 label:C[C](F)C(Cl)OBr smiles:C[C](F)C(Cl)OBr H298:-34.29 kcal/mol
library:CHOFClBr_G4 label:C[C](F)C(Cl)(Cl)Br smiles:C[C](F)C(Cl)(Cl)Br H298:-28.13 kcal/mol
library:CHOFClBr_G4 label:FC[C](F)C(Cl)Br smiles:FC[C](F)C(Cl)Br H298:-67.01 kcal/mol
library:CHOFClBr_G4 label:C[C](F)C(Cl)CBr smiles:C[C](F)C(Cl)CBr H298:-37.86 kcal/mol
library:CHOFClBr_G4 label:C[C](F)CC(Cl)Br smiles:C[C](F)CC(Cl)Br H298:-35.01 kcal/mol
library:CHOFBr_G4 label:C[C](F)CC(F)(F)Br smiles:C[C](F)CC(F)(F)Br H298:-127.12 kcal/mol
library:CHOFBr_G4 label:FC[C](F)C(F)Br smiles:FC[C](F)C(F)Br H298:-106.76 kcal/mol
library:CHOFBr_G4 label:F[C](CBr)C(F)F smiles:F[C](CBr)C(F)F H298:-116.95 kcal/mol
library:CHOFBr_G4 label:C[C](F)C(O)(F)Br smiles:C[C](F)C(O)(F)Br H298:-113.75 kcal/mol
library:CHOFBr_G4 label:CC(Br)(Br)[C](F)CF smiles:CC(Br)(Br)[C](F)CF H298:-66.02 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)[C](F)CF smiles:CC(F)(Br)[C](F)CF H298:-118.93 kcal/mol
library:CHOFBr_G4 label:FC[C](F)C(F)CBr smiles:FC[C](F)C(F)CBr H298:-114.60 kcal/mol
library:CHOFBr_G4 label:C[C](F)CC(Br)(Br)Br smiles:C[C](F)CC(Br)(Br)Br H298:-13.14 kcal/mol
library:CHOFBr_G4 label:FC[C](F)COBr smiles:FC[C](F)COBr H298:-69.01 kcal/mol
library:CHOFBr_G4 label:CC(Br)[C](F)C(F)F smiles:CC(Br)[C](F)C(F)F H298:-125.23 kcal/mol
library:CHOFBr_G4 label:F[C](C(F)F)C(F)Br smiles:F[C](C(F)F)C(F)Br H298:-157.12 kcal/mol
library:CHOFBr_G4 label:FC[C](F)CBr smiles:FC[C](F)CBr H298:-64.97 kcal/mol
library:CHOFBr_G4 label:C[C](F)COBr smiles:C[C](F)COBr H298:-27.48 kcal/mol
library:CHOFBr_G4 label:C[C](F)C(F)Br smiles:C[C](F)C(F)Br H298:-67.24 kcal/mol
library:CHOFBr_G4 label:C[C](F)C(F)(Br)Br smiles:C[C](F)C(F)(Br)Br H298:-59.22 kcal/mol
library:CHOFBr_G4 label:FC[C](F)CC(Br)Br smiles:FC[C](F)CC(Br)Br H298:-65.05 kcal/mol
library:CHOFBr_G4 label:C[C](F)C(F)(Br)OBr smiles:C[C](F)C(F)(Br)OBr H298:-74.35 kcal/mol
library:CHOFBr_G4 label:FC[C](F)CC(F)Br smiles:FC[C](F)CC(F)Br H298:-117.18 kcal/mol
library:CHOFBr_G4 label:OC(F)(Br)[C](F)CF smiles:OC(F)(Br)[C](F)CF H298:-154.35 kcal/mol
library:CHOFBr_G4 label:C[C](F)C(F)OBr smiles:C[C](F)C(F)OBr H298:-77.97 kcal/mol
library:CHOFBr_G4 label:C[C](F)C(F)(F)OBr smiles:C[C](F)C(F)(F)OBr H298:-133.63 kcal/mol
library:CHOFBr_G4 label:FC[C](F)C(F)(F)Br smiles:FC[C](F)C(F)(F)Br H298:-157.20 kcal/mol
library:CHOFBr_G4 label:C[C](F)C(F)(F)CBr smiles:C[C](F)C(F)(F)CBr H298:-128.15 kcal/mol
library:CHOFBr_G4 label:FC[C](F)C(Br)(Br)Br smiles:FC[C](F)C(Br)(Br)Br H298:-44.44 kcal/mol
library:CHOFBr_G4 label:C[C](F)C(F)CBr smiles:C[C](F)C(F)CBr H298:-75.48 kcal/mol
library:CHOFBr_G4 label:F[C](COBr)C(F)F smiles:F[C](COBr)C(F)F H298:-119.65 kcal/mol
library:CHOFBr_G4 label:F[C](CBr)C(F)(F)F smiles:F[C](CBr)C(F)(F)F H298:-173.46 kcal/mol
library:CHOFBr_G4 label:C[C](F)C(Br)(Br)Br smiles:C[C](F)C(Br)(Br)Br H298:-5.17 kcal/mol
library:CHOFBr_G4 label:C[C](F)CC(Br)Br smiles:C[C](F)CC(Br)Br H298:-23.22 kcal/mol
library:CHOFBr_G4 label:C[C](F)C(F)(F)Br smiles:C[C](F)C(F)(F)Br H298:-118.50 kcal/mol
library:CHOFBr_G4 label:F[C](CCBr)C(F)F smiles:F[C](CCBr)C(F)F H298:-122.97 kcal/mol
library:CHOFBr_G4 label:C[C](F)CCBr smiles:C[C](F)CCBr H298:-30.31 kcal/mol
library:CHOFBr_G4 label:C[C](F)C(F)C(F)Br smiles:C[C](F)C(F)C(F)Br H298:-117.89 kcal/mol
library:CHOFBr_G4 label:FC[C](F)CCBr smiles:FC[C](F)CCBr H298:-71.68 kcal/mol
library:CHOFBr_G4 label:FC[C](F)C(F)(Br)Br smiles:FC[C](F)C(F)(Br)Br H298:-98.66 kcal/mol
library:CHOFBr_G4 label:FC[C](F)C(F)OBr smiles:FC[C](F)C(F)OBr H298:-119.75 kcal/mol
library:CHOFBr_G4 label:C[C](F)C(F)C(Br)Br smiles:C[C](F)C(F)C(Br)Br H298:-66.76 kcal/mol
library:CHOFBr_G4 label:F[C](C(F)F)C(Br)Br smiles:F[C](C(F)F)C(Br)Br H298:-106.69 kcal/mol
library:CHOFBr_G4 label:C[C](F)CC(F)Br smiles:C[C](F)CC(F)Br H298:-75.12 kcal/mol
library:CHOFBr_G4 label:FC[C](F)C(Br)Br smiles:FC[C](F)C(Br)Br H298:-55.75 kcal/mol
library:CHOFBr_G4 label:FC[C](F)C(Br)OBr smiles:FC[C](F)C(Br)OBr H298:-63.96 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)[C](F)CF smiles:OC(Br)(Br)[C](F)CF H298:-97.22 kcal/mol
library:CHOFBr_G4 label:C[C](F)CC(F)(Br)Br smiles:C[C](F)CC(F)(Br)Br H298:-68.28 kcal/mol
""",
)

entry(
    index = 94,
    label = "CH3",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   H  u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.71,0.34,-0.33,-1.07,-2.43,-3.54,-5.43],'cal/(mol*K)'),
        H298 = (104.81,'kcal/mol','+|-',0.1),
        S298 = (0.52,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated in relation to methane from NIST values""",
    longDesc = 
"""

""",
)

entry(
    index = 95,
    label = "Cs_P",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   C  u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.77,-1.36,-1.91,-2.4,-3.16,-3.74,-4.66],'cal/(mol*K)'),
        H298 = (101.1,'kcal/mol'),
        S298 = (2.61,'cal/(mol*K)'),
    ),
    shortDesc = """Generic primary radical. (CHEN & BOZZELLI) #""",
    longDesc = 
"""

""",
)

entry(
    index = 96,
    label = "CJCO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   C   u0 {1,S} {5,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.8,-1.5,-4.1,-6.7,-11.1,-14.3,-19.2],'J/(mol*K)'),
        H298 = (430,'kJ/mol'),
        S298 = (6.1,'J/(mol*K)'),
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
    index = 97,
    label = "C=C(O)CJ",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,S} {6,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   O2s u0 {2,S}
6   C   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.7,-2.3,-4.6,-7.1,-11,-13.5,-16.6],'J/(mol*K)'),
        H298 = (376.8,'kJ/mol'),
        S298 = (-3.9,'J/(mol*K)'),
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
    index = 98,
    label = "CJCOOH",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   Cs  u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2s u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.25,-0.76,-1.34,-1.91,-2.87,-3.6,-4.69],'cal/(mol*K)'),
        H298 = (103.26,'kcal/mol'),
        S298 = (3.54,'cal/(mol*K)'),
    ),
    shortDesc = """WIJAYA et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 99,
    label = "CJC(C)OC",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S}
2 * Cs  u1 {1,S} {5,S} {6,S}
3   O2s u0 {1,S} {7,S}
4   C   u0 {1,S}
5   H   u0 {2,S}
6   H   u0 {2,S}
7   C   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.5,1.8,-2,-5.5,-11,-14.7,-19.8],'J/(mol*K)'),
        H298 = (429.9,'kJ/mol'),
        S298 = (7,'J/(mol*K)'),
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
    index = 100,
    label = "CJC(C)2O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   O2s u0 {1,S}
6   H   u0 {2,S}
7   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.1,1.1,-2.1,-5.1,-9.7,-13.1,-18.5],'J/(mol*K)'),
        H298 = (431.1,'kJ/mol'),
        S298 = (5.1,'J/(mol*K)'),
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
    index = 101,
    label = "C=CC(C)(O)CJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   Cd  u0 {1,S} {8,D}
4   O2s u0 {1,S}
5   C   u0 {1,S}
6   H   u0 {2,S}
7   H   u0 {2,S}
8   C   u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.5,-2.7,-5.5,-7.9,-11.8,-14.6,-19],'J/(mol*K)'),
        H298 = (431.9,'kJ/mol'),
        S298 = (9,'J/(mol*K)'),
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
    index = 102,
    label = "C=CC(O)(C=O)CJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   CO  u0 {1,S} {9,D}
4   Cd  u0 {1,S} {8,D}
5   O2s u0 {1,S}
6   H   u0 {2,S}
7   H   u0 {2,S}
8   C   u0 {4,D}
9   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4,0.9,-2.4,-5.2,-9.7,-13,-18.1],'J/(mol*K)'),
        H298 = (432.3,'kJ/mol'),
        S298 = (6.9,'J/(mol*K)'),
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
    index = 103,
    label = "CJC(C)(C=O)O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   CO  u0 {1,S} {8,D}
4   C   u0 {1,S}
5   O2s u0 {1,S}
6   H   u0 {2,S}
7   H   u0 {2,S}
8   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.6,5.1,2.3,-0.9,-6.8,-11.3,-17.8],'J/(mol*K)'),
        H298 = (430.9,'kJ/mol'),
        S298 = (3.7,'J/(mol*K)'),
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
    index = 104,
    label = "CJC(O)2C",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   C   u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   H   u0 {2,S}
7   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.4,-1.5,-5,-7.4,-10.8,-13.6,-18.2],'J/(mol*K)'),
        H298 = (435.3,'kJ/mol'),
        S298 = (8.1,'J/(mol*K)'),
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
    index = 105,
    label = "C=CC(O)2CJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   Cd  u0 {1,S} {8,D}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   H   u0 {2,S}
7   H   u0 {2,S}
8   C   u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1,-0.2,-2,-4,-8.1,-11.6,-17.2],'J/(mol*K)'),
        H298 = (431.8,'kJ/mol'),
        S298 = (6.7,'J/(mol*K)'),
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
    index = 106,
    label = "CJCC=O",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   C   u0 {1,S} {3,S}
3   CO  u0 {2,S} {6,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.8,-1.5,-4.1,-6.7,-11.1,-14.3,-19.2],'J/(mol*K)'),
        H298 = (430,'kJ/mol'),
        S298 = (6.1,'J/(mol*K)'),
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
    index = 107,
    label = "CJC(C)2C=O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   CO  u0 {1,S} {8,D}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   H   u0 {2,S}
7   H   u0 {2,S}
8   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.9,2.5,-1.1,-4.4,-9.7,-13.6,-19],'J/(mol*K)'),
        H298 = (429.5,'kJ/mol'),
        S298 = (7.9,'J/(mol*K)'),
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
    index = 108,
    label = "CJC(C=O)2C",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   CO  u0 {1,S} {8,D}
4   CO  u0 {1,S} {9,D}
5   C   u0 {1,S}
6   H   u0 {2,S}
7   H   u0 {2,S}
8   O2d u0 {3,D}
9   O2d u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.8,2.5,0.6,-1.9,-6.9,-10.9,-17.1],'J/(mol*K)'),
        H298 = (427,'kJ/mol'),
        S298 = (8.8,'J/(mol*K)'),
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
    label = "C=CC(C=O)2CJ",
    group = 
"""
1    Cs  u0 {2,S} {3,S} {4,S} {5,S}
2  * Cs  u1 {1,S} {6,S} {7,S}
3    CO  u0 {1,S} {9,D}
4    CO  u0 {1,S} {10,D}
5    Cd  u0 {1,S} {8,D}
6    H   u0 {2,S}
7    H   u0 {2,S}
8    C   u0 {5,D}
9    O2d u0 {3,D}
10   O2d u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.7,2.4,-0.6,-3.5,-8.4,-12.1,-17.6],'J/(mol*K)'),
        H298 = (429.8,'kJ/mol'),
        S298 = (5.5,'J/(mol*K)'),
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
    index = 110,
    label = "C=CC(C)(C=O)CJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   CO  u0 {1,S} {9,D}
4   Cd  u0 {1,S} {8,D}
5   C   u0 {1,S}
6   H   u0 {2,S}
7   H   u0 {2,S}
8   C   u0 {4,D}
9   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.8,0.6,-2.7,-5.8,-10.8,-14.4,-19.3],'J/(mol*K)'),
        H298 = (430.6,'kJ/mol'),
        S298 = (9.8,'J/(mol*K)'),
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
    index = 111,
    label = "CJC(C)C=O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S}
2 * Cs  u1 {1,S} {5,S} {6,S}
3   CO  u0 {1,S} {7,D}
4   C   u0 {1,S}
5   H   u0 {2,S}
6   H   u0 {2,S}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.6,0.2,-3,-5.8,-10.5,-14.1,-19.3],'J/(mol*K)'),
        H298 = (429.5,'kJ/mol'),
        S298 = (8.7,'J/(mol*K)'),
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
    index = 112,
    label = "C=C(C=O)CJ",
    group = 
"""
1   Cd  u0 {2,S} {3,S} {4,D}
2 * Cs  u1 {1,S} {5,S} {6,S}
3   CO  u0 {1,S} {7,D}
4   C   u0 {1,D}
5   H   u0 {2,S}
6   H   u0 {2,S}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.8,-1.2,-2.4,-4.4,-8.2,-11.3,-15.9],'J/(mol*K)'),
        H298 = (374,'kJ/mol'),
        S298 = (-16.5,'J/(mol*K)'),
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
    index = 113,
    label = "CJCC=C=O",
    group = 
"""
1 * Cs  u1 {2,S} {5,S} {6,S}
2   C   u0 {1,S} {3,S}
3   Cd  u0 {2,S} {4,D}
4   Cdd u0 {3,D} {7,D}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   O2d u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.3,-5.8,-8.1,-10.1,-13.4,-15.9,-19.9],'J/(mol*K)'),
        H298 = (420.3,'kJ/mol'),
        S298 = (16.4,'J/(mol*K)'),
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
    label = "CJC(C)C=C=O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {5,S}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   Cd  u0 {1,S} {4,D}
4   Cdd u0 {3,D} {8,D}
5   C   u0 {1,S}
6   H   u0 {2,S}
7   H   u0 {2,S}
8   O2d u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.2,-0.5,-4.1,-7.2,-11.8,-15,-19.5],'J/(mol*K)'),
        H298 = (430.1,'kJ/mol'),
        S298 = (9.7,'J/(mol*K)'),
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
    index = 115,
    label = "C=C(CJ)C=C=O",
    group = 
"""
1   Cd  u0 {2,S} {3,S} {5,D}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   Cd  u0 {1,S} {4,D}
4   Cdd u0 {3,D} {8,D}
5   C   u0 {1,D}
6   H   u0 {2,S}
7   H   u0 {2,S}
8   O2d u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.2,-5.6,-5.7,-6.4,-8.2,-10,-12.8],'J/(mol*K)'),
        H298 = (374.9,'kJ/mol'),
        S298 = (-8.1,'J/(mol*K)'),
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
    index = 116,
    label = "CsCsJ",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cs u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = 'Cs_P',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 117,
    label = "CCJ",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u1 {1,S} {6,S} {7,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   H  u0 {2,S}
7   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.65,-1.21,-1.75,-2.24,-3.02,-3.63,-3.63],'cal/(mol*K)'),
        H298 = (101.1,'kcal/mol','+|-',0.2),
        S298 = (2.61,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 118,
    label = "RCCJ",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u1 {1,S} {6,S} {7,S}
3   C  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   H  u0 {2,S}
7   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.77,-1.36,-1.91,-2.4,-3.16,-3.74,-4.66],'cal/(mol*K)'),
        H298 = (101.1,'kcal/mol','+|-',0.2),
        S298 = (2.61,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
"""

""",
)

entry(
    index = 119,
    label = "Neopentyl",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u1 {1,S} {6,S} {7,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   C  u0 {1,S}
6   H  u0 {2,S}
7   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.59,-1.32,-2.05,-2.65,-3.5,-4.06,-4.87],'cal/(mol*K)'),
        H298 = (101.1,'kcal/mol'),
        S298 = (3.03,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
"""

""",
)

entry(
    index = 120,
    label = "Isobutyl",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u1 {1,S} {6,S} {7,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   H  u0 {1,S}
6   H  u0 {2,S}
7   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.54,-1.26,-1.92,-2.46,-3.27,-3.84,-3.84],'cal/(mol*K)'),
        H298 = (101.1,'kcal/mol'),
        S298 = (2.91,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 121,
    label = "Benzyl_P",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cb u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.492,0.642,0.109,-0.656,-1.606,-2.293,-4.101],'cal/(mol*K)'),
        H298 = (90.788,'kcal/mol','+|-',2.4),
        S298 = (-5.163,'cal/(mol*K)'),
    ),
    shortDesc = """Fitted From  Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 7/2017, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds Include
[CH2]C1C=CC=CC=1
""",
)

entry(
    index = 122,
    label = "Allyl_P",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.62,-0.56,-0.78,-1.12,-1.84,-2.46,-3.49],'cal/(mol*K)'),
        H298 = (88.2,'kcal/mol'),
        S298 = (-2.56,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
"""

""",
)

entry(
    index = 123,
    label = "C=CC=CCJ",
    group = 
"""
1 * Cs u1 {2,S} {4,S} {5,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {6,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.83,-1.86,-1.98,-1.99,-2.3,-2.5,-2.5],'cal/(mol*K)'),
        H298 = (80,'kcal/mol'),
        S298 = (-1.55,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 124,
    label = "CTCC=CCJ",
    group = 
"""
1 * Cs u1 {2,S} {4,S} {5,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {6,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Ct u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.09,-1.62,-2.01,-2.63,-3.07,-3.48,-3.48],'cal/(mol*K)'),
        H298 = (81,'kcal/mol'),
        S298 = (-3.55,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 125,
    label = "CJC=C=O",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.2,-0.7,-2.6,-4.5,-8.1,-11,-15.6],'J/(mol*K)'),
        H298 = (373.5,'kJ/mol'),
        S298 = (-1.3,'J/(mol*K)'),
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
    index = 126,
    label = "Propargyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Ct u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.84,-1.17,-1.56,-1.95,-2.7,-3.31,-5.31],'cal/(mol*K)'),
        H298 = (89.4,'kcal/mol'),
        S298 = (-0.51,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
"""

""",
)

entry(
    index = 127,
    label = "CJC=O",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.5,1.1,-0.4,-2.3,-6.1,-9.2,-14.4],'J/(mol*K)'),
        H298 = (402.4,'kJ/mol'),
        S298 = (-7.8,'J/(mol*K)'),
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
    index = 128,
    label = "C2JC=O",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D} {6,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   O2d u0 {2,D}
6   C   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.32,0.19,-0.15,-0.57,-1.43,-2.22,-3.67],'cal/(mol*K)'),
        H298 = (94.4,'kcal/mol'),
        S298 = (-1.16,'cal/(mol*K)'),
    ),
    shortDesc = """CHEN & BOZZELLI""",
    longDesc = 
"""

""",
)

entry(
    index = 129,
    label = "Cs_S",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.5,-2.33,-3.1,-3.39,-3.75,-4.45,-5.2],'cal/(mol*K)'),
        H298 = (98.45,'kcal/mol'),
        S298 = (4.44,'cal/(mol*K)'),
    ),
    shortDesc = """Generic secondary radical. (CHEN & BOZZELLI) #""",
    longDesc = 
"""

""",
)

entry(
    index = 130,
    label = "CCJCO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   C   u0 {1,S} {5,S}
3   C   u0 {1,S}
4   H   u0 {1,S}
5   O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.9,-8.3,-10,-11.6,-14.5,-16.8,-20.3],'J/(mol*K)'),
        H298 = (416.9,'kJ/mol'),
        S298 = (13.8,'J/(mol*K)'),
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
    label = "C=CCJCO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   C   u0 {1,S} {5,S}
3   Cd  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   O2s u0 {2,S}
6   C   u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3,3.2,2.4,1,-1.8,-4.5,-9.8],'J/(mol*K)'),
        H298 = (335.4,'kJ/mol'),
        S298 = (-19.9,'J/(mol*K)'),
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
    label = "C=CCJC(O)C=C",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {5,S}
2   Cs  u0 {1,S} {4,S} {6,S}
3   Cd  u0 {1,S} {8,D}
4   Cd  u0 {2,S} {7,D}
5   H   u0 {1,S}
6   O2s u0 {2,S}
7   C   u0 {4,D}
8   C   u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.3,-4.5,-3,-2.8,-3.9,-5.6,-10.2],'J/(mol*K)'),
        H298 = (286.3,'kJ/mol'),
        S298 = (-9.6,'J/(mol*K)'),
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
    index = 133,
    label = "CCJCOOH",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   Cs  u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   O2s u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.65,-1.4,-2,-2.5,-3.27,-3.84,-4.73],'cal/(mol*K)'),
        H298 = (99.98,'kcal/mol'),
        S298 = (4.79,'cal/(mol*K)'),
    ),
    shortDesc = """WIJAYA et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 134,
    label = "CCJCC=O",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   C   u0 {1,S} {3,S}
3   CO  u0 {2,S} {6,D}
4   C   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.9,-8.3,-10,-11.6,-14.5,-16.8,-20.3],'J/(mol*K)'),
        H298 = (416.9,'kJ/mol'),
        S298 = (13.8,'J/(mol*K)'),
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
    index = 135,
    label = "CCJC(C)=C=O",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {5,S}
2   Cd  u0 {1,S} {4,D}
3   C   u0 {1,S} {6,S}
4   Cdd u0 {2,D} {7,D}
5   H   u0 {1,S}
6   C   u0 {3,S}
7   O2d u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-4,-6.2,-7.9,-10.8,-12.9,-16.9],'J/(mol*K)'),
        H298 = (365.4,'kJ/mol'),
        S298 = (8.3,'J/(mol*K)'),
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
    index = 136,
    label = "(Cs)2CsJ",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = 'Cs_S',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 137,
    label = "cyclopentene-4",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {5,S}
3   Cs u0 {1,S} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {2,S} {4,D}
6   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (96.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Allyl_S""",
    longDesc = 
"""

""",
)

entry(
    index = 138,
    label = "bicyclo[2.1.1]hex-2-ene-C5",
    group = 
"""
1   Cs u0 {3,S} {4,S} {6,S}
2   Cs u0 {3,S} {4,S} {5,S}
3 * Cs u1 {1,S} {2,S} {7,S}
4   C  u0 {1,S} {2,S}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {1,S} {5,D}
7   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (104.8,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 139,
    label = "tricyclo[2.1.1.0(1,4)]hex-2-ene-C5",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {6,S}
2   Cs u0 {1,S} {3,S} {4,S} {5,S}
3 * Cs u1 {1,S} {2,S} {7,S}
4   C  u0 {1,S} {2,S}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {1,S} {5,D}
7   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (105.2,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 140,
    label = "bicyclo[2.1.0]pent-2-ene-C5",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3 * Cs u1 {1,S} {2,S} {6,S}
4   Cd u0 {2,S} {5,D}
5   Cd u0 {1,S} {4,D}
6   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (106.9,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 141,
    label = "bicyclo[1.1.1]pentane-C2",
    group = 
"""
1   Cs u0 {3,S} {4,S} {5,S}
2   Cs u0 {3,S} {4,S} {5,S}
3 * Cs u1 {1,S} {2,S} {6,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {1,S} {2,S}
6   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (106.5,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 142,
    label = "tricyclo[1.1.1.0(1,3)]pentane-C2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S} {5,S}
3 * Cs u1 {1,S} {2,S} {6,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {1,S} {2,S}
6   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (111.5,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 143,
    label = "bicyclo[2.1.1]hexane-C5",
    group = 
"""
1   Cs u0 {3,S} {4,S} {6,S}
2   Cs u0 {3,S} {4,S} {5,S}
3 * Cs u1 {1,S} {2,S} {7,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {2,S} {6,S}
6   C  u0 {1,S} {5,S}
7   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (105.4,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 144,
    label = "tricyclo[2.1.1.0(1,4)]hexane-C5",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {6,S}
2   Cs u0 {1,S} {3,S} {4,S} {5,S}
3 * Cs u1 {1,S} {2,S} {7,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {2,S} {6,S}
6   C  u0 {1,S} {5,S}
7   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (103.4,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 145,
    label = "cyclopropane",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {1,S} {2,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (106,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """D.F. McMillen, D.M. Golden, HYDROCARBON BOND-DISSOCIATION ENERGIES, Annual Review of Physical Chemistry, 33 (1982) 493-532.. S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 146,
    label = "spiro[2.2]pentane-secondary",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u1 {1,S} {3,S} {6,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {5,S}
5   Cs u0 {1,S} {4,S}
6   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (107.3,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 147,
    label = "tricyclo[2.2.1.0(1,4)]heptane-C7",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S} {7,S}
2   Cs u0 {1,S} {3,S} {4,S} {6,S}
3 * Cs u1 {1,S} {2,S} {8,S}
4   C  u0 {2,S} {5,S}
5   C  u0 {1,S} {4,S}
6   C  u0 {2,S} {7,S}
7   C  u0 {1,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (106.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 148,
    label = "bicyclo[2.1.0]pentane-secondary-C3",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3 * Cs u1 {1,S} {2,S} {6,S}
4   Cs u0 {2,S} {5,S}
5   Cs u0 {1,S} {4,S}
6   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (105.9,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 149,
    label = "tricyclo[3.1.1.0(1,5)]heptane-C6",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {6,S}
2   Cs u0 {1,S} {3,S} {4,S} {5,S}
3 * Cs u1 {1,S} {2,S} {8,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {2,S} {7,S}
6   C  u0 {1,S} {7,S}
7   C  u0 {5,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (100,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 150,
    label = "bicyclo[1.1.0]butane-secondary",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {3,S} {4,S}
3 * Cs u1 {1,S} {2,S} {5,S}
4   Cs u0 {1,S} {2,S}
5   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (101.1,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 151,
    label = "bicyclo[3.1.0]hexane-C3",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3 * Cs u1 {1,S} {2,S} {7,S}
4   Cs u0 {2,S} {6,S}
5   Cs u0 {1,S} {6,S}
6   Cs u0 {4,S} {5,S}
7   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (108.3,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 153,
    label = "bicyclo[4.1.0]heptane-C3-7",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3 * Cs u1 {1,S} {2,S} {8,S}
4   C  u0 {2,S} {6,S}
5   C  u0 {1,S} {7,S}
6   C  u0 {4,S} {7,S}
7   C  u0 {5,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (108.1,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 153,
    label = "bicyclo[4.1.0]heptane-C3-7",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3 * Cs u1 {1,S} {2,S} {8,S}
4   C  u0 {2,S} {6,S}
5   C  u0 {1,S} {7,S}
6   C  u0 {4,S} {7,S}
7   C  u0 {5,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (108.1,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 154,
    label = "tricyclo[2.1.1.0(1,4)]hexane-C2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S} {4,S} {5,S} {6,S}
3 * Cs u1 {1,S} {6,S} {7,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {1,S} {2,S}
6   Cs u0 {2,S} {3,S}
7   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (100.1,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 155,
    label = "bicyclo[3.1.1]heptane-C6",
    group = 
"""
1   Cs u0 {3,S} {4,S} {6,S}
2   Cs u0 {3,S} {4,S} {5,S}
3 * Cs u1 {1,S} {2,S} {8,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {2,S} {7,S}
6   C  u0 {1,S} {7,S}
7   C  u0 {5,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (103,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 164,
    label = "tricyclo[2.2.1.0(1,4)]heptane-C2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S} {7,S}
3 * Cs u1 {1,S} {5,S} {8,S}
4   C  u0 {1,S} {2,S}
5   Cs u0 {2,S} {3,S}
6   C  u0 {1,S} {7,S}
7   C  u0 {2,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (96.8,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 165,
    label = "bicyclo[4.2.0]octane-C4-7",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {4,S} {6,S}
3 * Cs u1 {1,S} {4,S} {9,S}
4   Cs u0 {2,S} {3,S}
5   C  u0 {1,S} {8,S}
6   C  u0 {2,S} {7,S}
7   C  u0 {6,S} {8,S}
8   C  u0 {5,S} {7,S}
9   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (100.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 158,
    label = "bicyclo[2.2.2]octane-C2",
    group = 
"""
1   Cs u0 {3,S} {5,S} {6,S}
2   Cs u0 {4,S} {7,S} {8,S}
3 * Cs u1 {1,S} {4,S} {9,S}
4   Cs u0 {2,S} {3,S}
5   C  u0 {1,S} {7,S}
6   C  u0 {1,S} {8,S}
7   C  u0 {2,S} {5,S}
8   C  u0 {2,S} {6,S}
9   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.8,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 159,
    label = "tricyclo[2.2.2.0(1,4)]octane-C2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S} {6,S}
2   Cs u0 {1,S} {4,S} {7,S} {8,S}
3 * Cs u1 {1,S} {4,S} {9,S}
4   Cs u0 {2,S} {3,S}
5   C  u0 {1,S} {7,S}
6   C  u0 {1,S} {8,S}
7   C  u0 {2,S} {5,S}
8   C  u0 {2,S} {6,S}
9   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (99.3,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 160,
    label = "cyclobutane",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {4,S}
3   Cs u0 {1,S} {4,S}
4   Cs u0 {2,S} {3,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (96.9,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Tian, Z.; Fattahi, A.; Lis, L.; Kass, S. R., "Cycloalkane and Cycloalkene C-H Bond Dissociation Energies," J. Am. Chem. Soc. 2006, 128, 17087-17092, DOI: 10.1021/ja065348u. S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 161,
    label = "bicyclo[2.1.0]pentane-secondary-C4",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {4,S} {5,S}
3 * Cs u1 {1,S} {5,S} {6,S}
4   Cs u0 {1,S} {2,S}
5   Cs u0 {2,S} {3,S}
6   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (99.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 162,
    label = "bicyclo[2.2.0]hexane-secondary",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {4,S} {6,S}
3 * Cs u1 {1,S} {4,S} {7,S}
4   Cs u0 {2,S} {3,S}
5   Cs u0 {1,S} {6,S}
6   Cs u0 {2,S} {5,S}
7   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (98.6,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 163,
    label = "bicyclo[3.2.0]heptane-C5-6",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {4,S} {6,S}
3 * Cs u1 {1,S} {4,S} {8,S}
4   Cs u0 {2,S} {3,S}
5   Cs u0 {1,S} {7,S}
6   Cs u0 {2,S} {7,S}
7   Cs u0 {5,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (99,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 164,
    label = "tricyclo[2.2.1.0(1,4)]heptane-C2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S} {7,S}
3 * Cs u1 {1,S} {5,S} {8,S}
4   C  u0 {1,S} {2,S}
5   Cs u0 {2,S} {3,S}
6   C  u0 {1,S} {7,S}
7   C  u0 {2,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (96.8,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 165,
    label = "bicyclo[4.2.0]octane-C4-7",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {4,S} {6,S}
3 * Cs u1 {1,S} {4,S} {9,S}
4   Cs u0 {2,S} {3,S}
5   C  u0 {1,S} {8,S}
6   C  u0 {2,S} {7,S}
7   C  u0 {6,S} {8,S}
8   C  u0 {5,S} {7,S}
9   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (100.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 166,
    label = "bicyclo[3.1.1]heptane-C2",
    group = 
"""
1   Cs u0 {3,S} {4,S} {5,S}
2   Cs u0 {4,S} {5,S} {6,S}
3 * Cs u1 {1,S} {7,S} {8,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {1,S} {2,S}
6   C  u0 {2,S} {7,S}
7   Cs u0 {3,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.6,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 167,
    label = "tricyclo[3.1.1.0(1,5)]heptane-C2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S} {4,S} {5,S} {6,S}
3 * Cs u1 {1,S} {7,S} {8,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {1,S} {2,S}
6   C  u0 {2,S} {7,S}
7   Cs u0 {3,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (98.5,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 168,
    label = "bicyclo[3.1.0]hexane-C5-2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {4,S} {5,S}
3 * Cs u1 {1,S} {6,S} {7,S}
4   Cs u0 {1,S} {2,S}
5   Cs u0 {2,S} {6,S}
6   Cs u0 {3,S} {5,S}
7   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (93.6,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 169,
    label = "bicyclo[3.1.0]hexane-C5-3",
    group = 
"""
1   Cs u0 {2,S} {4,S} {5,S} {7,S}
2   Cs u0 {1,S} {4,S} {6,S}
3 * Cs u1 {5,S} {6,S} {8,S}
4   Cs u0 {1,S} {2,S}
5   Cs u0 {1,S} {3,S}
6   Cs u0 {2,S} {3,S}
7   H  u0 {1,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (94.1,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 170,
    label = "bicyclo[2.1.1]hexane-C2",
    group = 
"""
1   Cs u0 {3,S} {4,S} {5,S}
2   Cs u0 {4,S} {5,S} {6,S}
3 * Cs u1 {1,S} {6,S} {7,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {1,S} {2,S}
6   Cs u0 {2,S} {3,S}
7   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (100.8,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 171,
    label = "7-norbornyl",
    group = 
"""
1   Cs u0 {3,S} {4,S} {7,S}
2   Cs u0 {3,S} {5,S} {6,S}
3 * Cs u1 {1,S} {2,S} {8,S}
4   Cs u0 {1,S} {5,S}
5   Cs u0 {2,S} {4,S}
6   Cs u0 {2,S} {7,S}
7   Cs u0 {1,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (98.8,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """P.M. Nunes, S.G. Estacio, G.T. Lopes, B.J. Costa Cabral, R.M. Borges dos Santos, J.A. Martinho Simoes, CH Bond Dissociation Enthalpies in Norbornane. An Experimental and Computational Study, Organic Letters, 10 (2008) 1613-1616. S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 172,
    label = "2-norbornyl",
    group = 
"""
1   Cs u0 {2,S} {4,S} {6,S} {8,S}
2 * Cs u1 {1,S} {5,S} {9,S}
3   Cs u0 {4,S} {5,S} {7,S}
4   Cs u0 {1,S} {3,S}
5   Cs u0 {2,S} {3,S}
6   Cs u0 {1,S} {7,S}
7   Cs u0 {3,S} {6,S}
8   H  u0 {1,S}
9   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (105.02,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """P.M. Nunes, S.G. Estacio, G.T. Lopes, B.J. Costa Cabral, R.M. Borges dos Santos, J.A. Martinho Simoes, CH Bond Dissociation Enthalpies in Norbornane. An Experimental and Computational Study, Organic Letters, 10 (2008) 1613-1616. S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 179,
    label = "bicyclo[4.1.0]heptane-C6-2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {4,S} {5,S}
3 * Cs u1 {1,S} {6,S} {8,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {2,S} {7,S}
6   Cs u0 {3,S} {7,S}
7   C  u0 {5,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (94.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 175,
    label = "bicyclo[4.1.0]heptane-C6-3",
    group = 
"""
1   Cs u0 {2,S} {4,S} {5,S}
2   Cs u0 {1,S} {4,S} {6,S}
3 * Cs u1 {5,S} {7,S} {8,S}
4   C  u0 {1,S} {2,S}
5   Cs u0 {1,S} {3,S}
6   C  u0 {2,S} {7,S}
7   Cs u0 {3,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.6,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 175,
    label = "bicyclo[4.1.0]heptane-C6-3",
    group = 
"""
1   Cs u0 {2,S} {4,S} {5,S}
2   Cs u0 {1,S} {4,S} {6,S}
3 * Cs u1 {5,S} {7,S} {8,S}
4   C  u0 {1,S} {2,S}
5   Cs u0 {1,S} {3,S}
6   C  u0 {2,S} {7,S}
7   Cs u0 {3,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.6,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 176,
    label = "cycloheptane",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {8,S}
2   Cs u0 {1,S} {4,S}
3   Cs u0 {1,S} {5,S}
4   Cs u0 {2,S} {6,S}
5   Cs u0 {3,S} {7,S}
6   Cs u0 {4,S} {7,S}
7   Cs u0 {5,S} {6,S}
8   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (92.5,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 177,
    label = "bicyclo[3.2.0]heptane-C5-2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {5,S} {6,S}
3 * Cs u1 {1,S} {7,S} {8,S}
4   Cs u0 {1,S} {5,S}
5   Cs u0 {2,S} {4,S}
6   Cs u0 {2,S} {7,S}
7   Cs u0 {3,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.9,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 178,
    label = "bicyclo[3.2.0]heptane-C5-3",
    group = 
"""
1   Cs u0 {2,S} {5,S} {6,S}
2   Cs u0 {1,S} {4,S} {7,S}
3 * Cs u1 {4,S} {5,S} {8,S}
4   Cs u0 {2,S} {3,S}
5   Cs u0 {1,S} {3,S}
6   Cs u0 {1,S} {7,S}
7   Cs u0 {2,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (99.5,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 179,
    label = "bicyclo[4.1.0]heptane-C6-2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {4,S} {5,S}
3 * Cs u1 {1,S} {6,S} {8,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {2,S} {7,S}
6   Cs u0 {3,S} {7,S}
7   C  u0 {5,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (94.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 180,
    label = "bicyclo[3.1.1]heptane-C3",
    group = 
"""
1   Cs u0 {4,S} {5,S} {7,S}
2   Cs u0 {4,S} {5,S} {6,S}
3 * Cs u1 {6,S} {7,S} {8,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {1,S} {2,S}
6   Cs u0 {2,S} {3,S}
7   Cs u0 {1,S} {3,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.3,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 181,
    label = "tricyclo[3.1.1.0(1,5)]heptane-C3",
    group = 
"""
1   Cs u0 {2,S} {4,S} {5,S} {7,S}
2   Cs u0 {1,S} {4,S} {5,S} {6,S}
3 * Cs u1 {6,S} {7,S} {8,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {1,S} {2,S}
6   Cs u0 {2,S} {3,S}
7   Cs u0 {1,S} {3,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 182,
    label = "octahydro-pentalene-C5-2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {5,S} {6,S}
3 * Cs u1 {1,S} {7,S} {9,S}
4   C  u0 {1,S} {8,S}
5   C  u0 {2,S} {7,S}
6   C  u0 {2,S} {8,S}
7   Cs u0 {3,S} {5,S}
8   C  u0 {4,S} {6,S}
9   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.8,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 183,
    label = "octahydro-pentalene-C5-3",
    group = 
"""
1   Cs u0 {2,S} {4,S} {6,S}
2   Cs u0 {1,S} {5,S} {7,S}
3 * Cs u1 {4,S} {5,S} {9,S}
4   Cs u0 {1,S} {3,S}
5   Cs u0 {2,S} {3,S}
6   C  u0 {1,S} {8,S}
7   C  u0 {2,S} {8,S}
8   C  u0 {6,S} {7,S}
9   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (98.1,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 184,
    label = "bicyclo[4.2.0]octane-C6-2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {5,S} {6,S}
3 * Cs u1 {1,S} {7,S} {9,S}
4   C  u0 {1,S} {5,S}
5   C  u0 {2,S} {4,S}
6   C  u0 {2,S} {8,S}
7   Cs u0 {3,S} {8,S}
8   C  u0 {6,S} {7,S}
9   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (96.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 185,
    label = "bicyclo[4.2.0]octane-C6-3",
    group = 
"""
1   Cs u0 {2,S} {4,S} {6,S}
2   Cs u0 {1,S} {5,S} {7,S}
3 * Cs u1 {4,S} {8,S} {9,S}
4   Cs u0 {1,S} {3,S}
5   C  u0 {2,S} {6,S}
6   C  u0 {1,S} {5,S}
7   C  u0 {2,S} {8,S}
8   Cs u0 {3,S} {7,S}
9   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (99,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 186,
    label = "CCJC",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cs u0 {3,S} {7,S} {8,S} {9,S}
3  * Cs u1 {1,S} {2,S} {10,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    H  u0 {2,S}
8    H  u0 {2,S}
9    H  u0 {2,S}
10   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (98.45,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
"""

""",
)

entry(
    index = 187,
    label = "RCCJC",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cs u0 {3,S} {7,S} {8,S} {9,S}
3  * Cs u1 {1,S} {2,S} {10,S}
4    C  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    H  u0 {2,S}
8    H  u0 {2,S}
9    H  u0 {2,S}
10   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54,-2.77,-3.49,-3.9,-4.35,-4.64,-4.64],'cal/(mol*K)'),
        H298 = (98.45,'kcal/mol'),
        S298 = (5.13,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 188,
    label = "RCCJCC",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cs u0 {3,S} {7,S} {8,S} {9,S}
3  * Cs u1 {1,S} {2,S} {10,S}
4    C  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    C  u0 {2,S}
8    H  u0 {2,S}
9    H  u0 {2,S}
10   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.71,-3.14,-3.92,-4.33,-4.71,-4.92,-4.92],'cal/(mol*K)'),
        H298 = (98.45,'kcal/mol'),
        S298 = (4.9,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 189,
    label = "cyclopentane",
    group = 
"""
1    Cs u0 {3,S} {4,S} {6,S} {7,S}
2    Cs u0 {3,S} {5,S} {8,S} {9,S}
3  * Cs u1 {1,S} {2,S} {10,S}
4    C  u0 {1,S} {5,S}
5    C  u0 {2,S} {4,S}
6    H  u0 {1,S}
7    H  u0 {1,S}
8    H  u0 {2,S}
9    H  u0 {2,S}
10   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.71,-3.14,-3.92,-4.33,-4.71,-4.92,-4.92],'cal/(mol*K)'),
        H298 = (96.4,'kcal/mol'),
        S298 = (4.9,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from RCCJCC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 190,
    label = "cyclohexane",
    group = 
"""
1    Cs u0 {3,S} {4,S} {7,S} {8,S}
2    Cs u0 {3,S} {5,S} {9,S} {10,S}
3  * Cs u1 {1,S} {2,S} {11,S}
4    C  u0 {1,S} {6,S}
5    C  u0 {2,S} {6,S}
6    C  u0 {4,S} {5,S}
7    H  u0 {1,S}
8    H  u0 {1,S}
9    H  u0 {2,S}
10   H  u0 {2,S}
11   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.71,-3.14,-3.92,-4.33,-4.71,-4.92,-4.92],'cal/(mol*K)'),
        H298 = (95.5,'kcal/mol'),
        S298 = (4.9,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from RCCJCC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 191,
    label = "Benzyl_S",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cb u0 {1,S}
3   C  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0448,-1.3002,-2.199,-2.5546,-2.5872,-2.8074,-5.6336],'cal/(mol*K)'),
        H298 = (88.064,'kcal/mol','+|-',2.4),
        S298 = (-4.8554,'cal/(mol*K)'),
    ),
    shortDesc = """Fitted From Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 7/2017, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds Include
C[CH]C1C=CC=CC=1
CC[CH]C1C=CC=CC=1
CCC[CH]C1C=CC=CC=1
CCCC[CH]C1C=CC=CC=1
CCCCC[CH]C1C=CC=CC=1
""",
)

entry(
    index = 192,
    label = "Indenyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cb u0 {1,S} {4,B}
3   Cd u0 {1,S} {5,D}
4   Cb u0 {2,B} {5,S}
5   Cd u0 {3,D} {4,S}
6   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.36,-0.72,-1.23,-1.77,-2.7,-3.43,-4.54],'cal/(mol*K)'),
        H298 = (81.62,'kcal/mol'),
        S298 = (0.69,'cal/(mol*K)'),
    ),
    shortDesc = """A.G. Vandeputte CBS-QB3""",
    longDesc = 
"""

""",
)

entry(
    index = 193,
    label = "Benzyl_S_Fused5",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cb u0 {1,S} {5,B}
3   C  u0 {1,S} {6,[S,D,T]}
4   H  u0 {1,S}
5   Cb u0 {2,B} {6,S}
6   C  u0 {3,[S,D,T]} {5,S}
""",
    thermo = None,
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds Include
C1=CC=C2CC[CH]C2=C1
CC1C[CH]C2=CC=CC=C21
CCC1C[CH]C2=CC=CC=C21
CCCC1C[CH]C2=CC=CC=C21
""",
)

entry(
    index = 194,
    label = "Benzyl_S_Fused6",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cb u0 {1,S} {5,B}
3   C  u0 {1,S} {7,[S,D,T,B]}
4   H  u0 {1,S}
5   Cb u0 {2,B} {6,S}
6   C  u0 {5,S} {7,[S,D,T,B]}
7   C  u0 {3,[S,D,T,B]} {6,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds Include
C1=CC=C2CCC[CH]C2=C1
CC1CC[CH]C2=CC=CC=C21
CCC1CC[CH]C2=CC=CC=C21
""",
)

entry(
    index = 195,
    label = "Benzyl_S_dihydronaphthalene",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cb u0 {1,S} {5,B}
3   C  u0 {1,S} {7,[S,D,B]}
4   H  u0 {1,S}
5   Cb u0 {2,B} {6,S}
6   Cd u0 {5,S} {7,D}
7   Cd u0 {3,[S,D,B]} {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.762975,-1.09193,-1.45447,-1.90836,-2.74844,-3.44654,-4.57653],'cal/(mol*K)','+|-',[0.226952,0.226952,0.226952,0.226952,0.226952,0.226952,0.226952]),
        H298 = (83.6682,'kcal/mol','+|-',0.869131),
        S298 = (1.4331,'cal/(mol*K)','+|-',0.350884),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 07/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
C1=CC=C2C=CC[CH]C2=C1
CC1=CC[CH]C2=CC=CC=C12
CCC1=CC[CH]C2=CC=CC=C12

Modified 10/2019 by Max Liu. Added enthalpy of H atom so that GAV predicted
enthalpy for C1=CC=C2C=CC[CH]C2=C1 matches calculated value.
""",
)

entry(
    index = 196,
    label = "Benzyl_S_Fused7",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cb u0 {1,S} {5,B}
3   C  u0 {1,S} {8,[S,D,T,B]}
4   H  u0 {1,S}
5   Cb u0 {2,B} {6,S}
6   C  u0 {5,S} {7,[S,D,T,B]}
7   C  u0 {6,[S,D,T,B]} {8,[S,D,T,B]}
8   C  u0 {3,[S,D,T,B]} {7,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 04/2019, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds include:
C1=CC=C2CCCC[CH]C2=C1
""",
)

entry(
    index = 197,
    label = "Allyl_S",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S}
3   Cs u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54,-1.82,-2.08,-2.32,-2.75,-3.14,-3.85],'cal/(mol*K)'),
        H298 = (85.6,'kcal/mol'),
        S298 = (-3.81,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
"""

""",
)

entry(
    index = 198,
    label = "Aromatic_pi_S_1_3",
    group = 
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {1,S} {5,S}
7   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.013276,-1.28931,-2.31258,-2.92159,-3.39846,-3.6762,-4.8642],'cal/(mol*K)','+|-',[0.023461,0.023461,0.023461,0.023461,0.023461,0.023461,0.023461]),
        H298 = (75.4692,'kcal/mol','+|-',0.139824),
        S298 = (1.48461,'cal/(mol*K)','+|-',0.036353),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 08/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
CC1=CC=C[CH]C1
CC1[CH]CC=CC=1
CC1C=CC[CH]C=1
CC1[CH]C=CC=C1
""",
)

entry(
    index = 199,
    label = "Aromatic_pi_S_(CH3_CH3_Ortho)_1_3",
    group = 
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S} {8,S}
6   Cs u0 {1,S} {5,S} {9,S}
7   H  u0 {1,S}
8   C  u0 {5,S}
9   C  u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.104911,-1.14065,-2.32405,-3.03895,-3.75201,-4.05481,-5.14193],'cal/(mol*K)','+|-',[0.061305,0.061305,0.061305,0.061305,0.061305,0.061305,0.061305]),
        H298 = (75.5447,'kcal/mol','+|-',0.399656),
        S298 = (2.79083,'cal/(mol*K)','+|-',0.079011),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 08/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
CC1=CC=C[CH]C1C
CC1[CH]C(C)C=CC=1
CC1C=CC(C)[CH]C=1
CC1(C)[CH]C=CC=C1
""",
)

entry(
    index = 200,
    label = "Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cd u0 {3,S} {5,D}
5    Cd u0 {4,D} {6,S} {8,S}
6    Cs u0 {1,S} {5,S} {9,S}
7    H  u0 {1,S}
8    C  u0 {5,S}
9    C  u0 {6,S} {10,S}
10   C  u0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.453462,-1.20244,-2.43607,-2.95615,-3.47107,-3.9488,-5.03407],'cal/(mol*K)','+|-',[0.068504,0.068504,0.068504,0.068504,0.068504,0.068504,0.068504]),
        H298 = (74.982,'kcal/mol','+|-',0.417781),
        S298 = (1.24362,'cal/(mol*K)','+|-',0.106961),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 08/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
CCC1[CH]C=CC=C1C
CCC1[CH]C(C)=CC=C1
CCC1[CH]C=C(C)C=C1
CCC1(C)[CH]C=CC=C1
""",
)

entry(
    index = 201,
    label = "Aromatic_pi_S_(fused5)_1_3",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cd u0 {3,S} {5,D}
5    Cd u0 {4,D} {6,S} {8,S}
6    Cs u0 {1,S} {5,S} {9,S}
7    H  u0 {1,S}
8    C  u0 {5,S} {10,S}
9    C  u0 {6,S} {10,S}
10   C  u0 {8,S} {9,S}
""",
    thermo = 'Aromatic_pi_S_(fused5)_1_4',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
C1=CC=C2CCCC2[CH]1
CC1CCC2=CC=C[CH]C21
CCC1CCC2=CC=C[CH]C21
CCCC1CCC2=CC=C[CH]C21
C1=CC=C2CCCCC2[CH]1
CC1CCCC2=CC=C[CH]C21
CCC1CCCC2=CC=C[CH]C21
""",
)

entry(
    index = 202,
    label = "Aromatic_pi_S_(fused6)_1_3",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cd u0 {3,S} {5,D}
5    Cd u0 {4,D} {6,S} {8,S}
6    Cs u0 {1,S} {5,S} {9,S}
7    H  u0 {1,S}
8    C  u0 {5,S} {11,S}
9    C  u0 {6,S} {10,S}
10   C  u0 {9,S} {11,S}
11   C  u0 {8,S} {10,S}
""",
    thermo = 'Aromatic_pi_S_(fused5)_1_4',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
C1=CC=C2CCCC2[CH]1
CC1CCC2=CC=C[CH]C21
CCC1CCC2=CC=C[CH]C21
CCCC1CCC2=CC=C[CH]C21
C1=CC=C2CCCCC2[CH]1
CC1CCCC2=CC=C[CH]C21
CCC1CCCC2=CC=C[CH]C21
""",
)

entry(
    index = 203,
    label = "Aromatic_pi_S_(fused7)_1_3",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cd u0 {3,S} {5,D}
5    Cd u0 {4,D} {6,S} {8,S}
6    Cs u0 {1,S} {5,S} {9,S}
7    H  u0 {1,S}
8    C  u0 {5,S} {12,S}
9    C  u0 {6,S} {10,S}
10   C  u0 {9,S} {11,S}
11   C  u0 {10,S} {12,S}
12   C  u0 {8,S} {11,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.084287,-0.439484,-1.00984,-1.6168,-2.48415,-3.29208,-4.57923],'cal/(mol*K)','+|-',[1.08001,1.08001,1.08001,1.08001,1.08001,1.08001,1.08001]),
        H298 = (76.4252,'kcal/mol','+|-',4.19016),
        S298 = (0.527688,'cal/(mol*K)','+|-',2.02975),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 04/2019, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds include:
C1=CC=C2CCCCCC2[CH]1
C1=CC=C2CCCCC(C)C2[CH]1
""",
)

entry(
    index = 204,
    label = "Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cd u0 {3,S} {5,D}
5    Cd u0 {4,D} {6,S} {8,S}
6    Cs u0 {1,S} {5,S} {9,S}
7    H  u0 {1,S}
8    C  u0 {5,S}
9    C  u0 {6,S} {10,S}
10   Cb u0 {9,S} {11,B} {15,B}
11   Cb u0 {10,B} {12,B}
12   Cb u0 {11,B} {13,B}
13   Cb u0 {12,B} {14,B}
14   Cb u0 {13,B} {15,B}
15   Cb u0 {10,B} {14,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.831072,-0.828879,-1.89888,-2.14323,-2.47359,-2.80572,-3.59479],'cal/(mol*K)','+|-',[0.208059,0.208059,0.208059,0.208059,0.208059,0.208059,0.208059]),
        H298 = (74.1331,'kcal/mol','+|-',0.742606),
        S298 = (-0.854817,'cal/(mol*K)','+|-',0.322012),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 08/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
""",
)

entry(
    index = 205,
    label = "Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cd u0 {3,S} {5,D}
5    Cd u0 {4,D} {6,S} {8,S}
6    Cs u0 {1,S} {5,S} {9,S}
7    H  u0 {1,S}
8    C  u0 {5,S}
9    Cs u0 {6,S} {10,S} {16,S}
10   Cb u0 {9,S} {11,B} {15,B}
11   Cb u0 {10,B} {12,B}
12   Cb u0 {11,B} {13,B}
13   Cb u0 {12,B} {14,B}
14   Cb u0 {13,B} {15,B}
15   Cb u0 {10,B} {14,B}
16   C  u0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.67718,-0.360591,-1.61836,-2.06586,-2.45313,-2.74791,-3.50658],'cal/(mol*K)','+|-',[0.245046,0.245046,0.245046,0.245046,0.245046,0.245046,0.245046]),
        H298 = (74.3294,'kcal/mol','+|-',0.850906),
        S298 = (-3.58784,'cal/(mol*K)','+|-',0.338262),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 08/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
""",
)

entry(
    index = 206,
    label = "Aromatic_pi_S_(CH3_CH3_Meta)_1_3_1",
    group = 
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D} {8,S}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {1,S} {5,S} {9,S}
7   H  u0 {1,S}
8   C  u0 {2,S}
9   C  u0 {6,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 207,
    label = "Aromatic_pi_S_(CH3_C2H5_Meta)_1_3_1",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D} {8,S}
3    Cd u0 {2,D} {4,S}
4    Cd u0 {3,S} {5,D}
5    Cd u0 {4,D} {6,S}
6    Cs u0 {1,S} {5,S} {9,S}
7    H  u0 {1,S}
8    C  u0 {2,S}
9    C  u0 {6,S} {10,S}
10   C  u0 {9,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
""",
)

entry(
    index = 208,
    label = "Aromatic_pi_S_(CH3_Benzyl_Meta)_1_3_1",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D} {8,S}
3    Cd u0 {2,D} {4,S}
4    Cd u0 {3,S} {5,D}
5    Cd u0 {4,D} {6,S}
6    Cs u0 {1,S} {5,S} {9,S}
7    H  u0 {1,S}
8    C  u0 {2,S}
9    C  u0 {6,S} {10,S}
10   Cb u0 {9,S} {11,B} {15,B}
11   Cb u0 {10,B} {12,B}
12   Cb u0 {11,B} {13,B}
13   Cb u0 {12,B} {14,B}
14   Cb u0 {13,B} {15,B}
15   Cb u0 {10,B} {14,B}
""",
    thermo = 'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 209,
    label = "Aromatic_pi_S_(CH3_EBenzyl_Meta)_1_3_1",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D} {8,S}
3    Cd u0 {2,D} {4,S}
4    Cd u0 {3,S} {5,D}
5    Cd u0 {4,D} {6,S}
6    Cs u0 {1,S} {5,S} {9,S}
7    H  u0 {1,S}
8    C  u0 {2,S}
9    Cs u0 {6,S} {10,S} {16,S}
10   Cb u0 {9,S} {11,B} {15,B}
11   Cb u0 {10,B} {12,B}
12   Cb u0 {11,B} {13,B}
13   Cb u0 {12,B} {14,B}
14   Cb u0 {13,B} {15,B}
15   Cb u0 {10,B} {14,B}
16   C  u0 {9,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 210,
    label = "Aromatic_pi_S_(CH3_CH3_Meta)_1_3_2",
    group = 
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D} {8,S}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {1,S} {5,S} {9,S}
7   H  u0 {1,S}
8   C  u0 {4,S}
9   C  u0 {6,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 211,
    label = "Aromatic_pi_S_(CH3_C2H5_Meta)_1_3_2",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cd u0 {3,S} {5,D} {8,S}
5    Cd u0 {4,D} {6,S}
6    Cs u0 {1,S} {5,S} {9,S}
7    H  u0 {1,S}
8    C  u0 {4,S}
9    C  u0 {6,S} {10,S}
10   C  u0 {9,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
""",
)

entry(
    index = 212,
    label = "Aromatic_pi_S_(CH3_Benzyl_Meta)_1_3_2",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cd u0 {3,S} {5,D} {8,S}
5    Cd u0 {4,D} {6,S}
6    Cs u0 {1,S} {5,S} {9,S}
7    H  u0 {1,S}
8    C  u0 {4,S}
9    C  u0 {6,S} {10,S}
10   Cb u0 {9,S} {11,B} {15,B}
11   Cb u0 {10,B} {12,B}
12   Cb u0 {11,B} {13,B}
13   Cb u0 {12,B} {14,B}
14   Cb u0 {13,B} {15,B}
15   Cb u0 {10,B} {14,B}
""",
    thermo = 'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 213,
    label = "Aromatic_pi_S_(CH3_EBenzyl_Meta)_1_3_2",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cd u0 {3,S} {5,D} {8,S}
5    Cd u0 {4,D} {6,S}
6    Cs u0 {1,S} {5,S} {9,S}
7    H  u0 {1,S}
8    C  u0 {4,S}
9    Cs u0 {6,S} {10,S} {16,S}
10   Cb u0 {9,S} {11,B} {15,B}
11   Cb u0 {10,B} {12,B}
12   Cb u0 {11,B} {13,B}
13   Cb u0 {12,B} {14,B}
14   Cb u0 {13,B} {15,B}
15   Cb u0 {10,B} {14,B}
16   C  u0 {9,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 214,
    label = "Aromatic_pi_S_(CH3_CH3_Para)_1_3",
    group = 
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S} {8,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {1,S} {5,S} {9,S}
7   H  u0 {1,S}
8   C  u0 {3,S}
9   C  u0 {6,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 215,
    label = "Aromatic_pi_S_(CH3_C2H5_Para)_1_3",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S} {8,S}
4    Cd u0 {3,S} {5,D}
5    Cd u0 {4,D} {6,S}
6    Cs u0 {1,S} {5,S} {9,S}
7    H  u0 {1,S}
8    C  u0 {3,S}
9    C  u0 {6,S} {10,S}
10   C  u0 {9,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
""",
)

entry(
    index = 216,
    label = "Aromatic_pi_S_(CH3_Benzyl_Para)_1_3",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S} {8,S}
4    Cd u0 {3,S} {5,D}
5    Cd u0 {4,D} {6,S}
6    Cs u0 {1,S} {5,S} {9,S}
7    H  u0 {1,S}
8    C  u0 {3,S}
9    C  u0 {6,S} {10,S}
10   Cb u0 {9,S} {11,B} {15,B}
11   Cb u0 {10,B} {12,B}
12   Cb u0 {11,B} {13,B}
13   Cb u0 {12,B} {14,B}
14   Cb u0 {13,B} {15,B}
15   Cb u0 {10,B} {14,B}
""",
    thermo = 'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 217,
    label = "Aromatic_pi_S_(CH3_EBenzyl_Para)_1_3",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S} {8,S}
4    Cd u0 {3,S} {5,D}
5    Cd u0 {4,D} {6,S}
6    Cs u0 {1,S} {5,S} {9,S}
7    H  u0 {1,S}
8    C  u0 {3,S}
9    Cs u0 {6,S} {10,S} {16,S}
10   Cb u0 {9,S} {11,B} {15,B}
11   Cb u0 {10,B} {12,B}
12   Cb u0 {11,B} {13,B}
13   Cb u0 {12,B} {14,B}
14   Cb u0 {13,B} {15,B}
15   Cb u0 {10,B} {14,B}
16   C  u0 {9,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 218,
    label = "Aromatic_pi_S_(CH3_CH3_Sub)_1_3",
    group = 
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {1,S} {5,S} {8,S} {9,S}
7   H  u0 {1,S}
8   C  u0 {6,S}
9   C  u0 {6,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 219,
    label = "Aromatic_pi_S_(s1_3_6_diene_1_4)_1_3",
    group = 
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {1,S} {5,S} {8,S} {9,S}
7   H  u0 {1,S}
8   C  u0 {6,S} {9,S}
9   C  u0 {6,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.48192,0.127981,-0.882314,-1.47156,-2.2164,-3.23195,-4.40182],'cal/(mol*K)','+|-',[0.7049,0.7049,0.7049,0.7049,0.7049,0.7049,0.7049]),
        H298 = (70.66,'kcal/mol','+|-',4.28202),
        S298 = (-1.77936,'cal/(mol*K)','+|-',1.91485),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
CCCCC1CC12C=C[CH]C=C2
""",
)

entry(
    index = 220,
    label = "Aromatic_pi_S_(CH3_C2H5_Sub)_1_3",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cd u0 {3,S} {5,D}
5    Cd u0 {4,D} {6,S}
6    Cs u0 {1,S} {5,S} {8,S} {9,S}
7    H  u0 {1,S}
8    C  u0 {6,S}
9    C  u0 {6,S} {10,S}
10   C  u0 {9,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
""",
)

entry(
    index = 221,
    label = "Aromatic_pi_S_(s1_4_6_diene_1_4)_1_3",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cd u0 {3,S} {5,D}
5    Cd u0 {4,D} {6,S}
6    Cs u0 {1,S} {5,S} {8,S} {9,S}
7    H  u0 {1,S}
8    C  u0 {6,S} {10,S}
9    C  u0 {6,S} {10,S}
10   C  u0 {8,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.85011,2.02306,1.41734,0.955199,-0.252841,-1.61161,-3.21428],'cal/(mol*K)','+|-',[0.733897,0.733897,0.733897,0.733897,0.733897,0.733897,0.733897]),
        H298 = (72.4956,'kcal/mol','+|-',4.45566),
        S298 = (2.72,'cal/(mol*K)','+|-',2.01098),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
CCCC1CCC12C=C[CH]C=C2
""",
)

entry(
    index = 222,
    label = "Aromatic_pi_S_(s1_5_6_diene_1_4)_1_3",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cd u0 {3,S} {5,D}
5    Cd u0 {4,D} {6,S}
6    Cs u0 {1,S} {5,S} {8,S} {9,S}
7    H  u0 {1,S}
8    C  u0 {6,S} {11,S}
9    C  u0 {6,S} {10,S}
10   C  u0 {9,S} {11,S}
11   C  u0 {8,S} {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.344733,-0.12429,-0.432103,-0.924571,-2.30122,-3.16695,-4.31502],'cal/(mol*K)','+|-',[0.781339,0.781339,0.781339,0.781339,0.781339,0.781339,0.781339]),
        H298 = (73.496,'kcal/mol','+|-',4.73954),
        S298 = (-3.2868,'cal/(mol*K)','+|-',2.17587),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
CCC1CCCC12C=C[CH]C=C2
""",
)

entry(
    index = 223,
    label = "Aromatic_pi_S_(s1_6_6_diene_1_4)_1_3",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cd u0 {3,S} {5,D}
5    Cd u0 {4,D} {6,S}
6    Cs u0 {1,S} {5,S} {8,S} {9,S}
7    H  u0 {1,S}
8    C  u0 {6,S} {12,S}
9    C  u0 {6,S} {10,S}
10   C  u0 {9,S} {11,S}
11   C  u0 {10,S} {12,S}
12   C  u0 {8,S} {11,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.226242,-0.404788,-1.08177,-1.65237,-2.56959,-3.27321,-4.6477],'cal/(mol*K)','+|-',[0.872202,0.872202,0.872202,0.872202,0.872202,0.872202,0.872202]),
        H298 = (74.0097,'kcal/mol','+|-',5.28577),
        S298 = (-1.20585,'cal/(mol*K)','+|-',2.5221),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
CC1CCCCC12C=C[CH]C=C2
""",
)

entry(
    index = 224,
    label = "Aromatic_pi_S_(CH3_Benzyl_Sub)_1_3",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cd u0 {3,S} {5,D}
5    Cd u0 {4,D} {6,S}
6    Cs u0 {1,S} {5,S} {8,S} {9,S}
7    H  u0 {1,S}
8    C  u0 {6,S}
9    C  u0 {6,S} {10,S}
10   Cb u0 {9,S} {11,B} {15,B}
11   Cb u0 {10,B} {12,B}
12   Cb u0 {11,B} {13,B}
13   Cb u0 {12,B} {14,B}
14   Cb u0 {13,B} {15,B}
15   Cb u0 {10,B} {14,B}
""",
    thermo = 'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 225,
    label = "Aromatic_pi_S_(CH3_EBenzyl_Sub)_1_3",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cd u0 {3,S} {5,D}
5    Cd u0 {4,D} {6,S}
6    Cs u0 {1,S} {5,S} {8,S} {9,S}
7    H  u0 {1,S}
8    C  u0 {6,S}
9    Cs u0 {6,S} {10,S} {16,S}
10   Cb u0 {9,S} {11,B} {15,B}
11   Cb u0 {10,B} {12,B}
12   Cb u0 {11,B} {13,B}
13   Cb u0 {12,B} {14,B}
14   Cb u0 {13,B} {15,B}
15   Cb u0 {10,B} {14,B}
16   C  u0 {9,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 226,
    label = "CJ-Cd-Benzene",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cs u0 {1,S} {7,S}
4   H  u0 {1,S}
5   Cd u0 {2,D} {6,S}
6   Cb u0 {5,S} {7,B}
7   Cb u0 {3,S} {6,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.038694,-0.486795,-1.26614,-1.94355,-2.84643,-3.50953,-4.60995],'cal/(mol*K)','+|-',[0.244001,0.244001,0.244001,0.244001,0.244001,0.244001,0.244001]),
        H298 = (80.0557,'kcal/mol','+|-',0.913362),
        S298 = (1.93251,'cal/(mol*K)','+|-',0.367823),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds Include
C1=CC=C2C=C[CH]CC2=C1
CC1[CH]C=CC2=CC=CC=C12
CC1=C[CH]CC2=CC=CC=C12
CCC1[CH]C=CC2=CC=CC=C12
CCC1=C[CH]CC2=CC=CC=C12
""",
)

entry(
    index = 227,
    label = "CJ-Cd-Benzene7",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cs u0 {1,S} {8,S}
4   H  u0 {1,S}
5   Cd u0 {2,D} {6,S}
6   Cb u0 {5,S} {7,B}
7   Cb u0 {6,B} {8,S}
8   Cs u0 {3,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.3,-0.5,-1,-1.5,-2.5,-3.3,-4.5],'cal/(mol*K)','+|-',[2.4642,2.4642,2.4642,2.4642,2.4642,2.4642,2.4642]),
        H298 = (80.7,'kcal/mol','+|-',7.3256),
        S298 = (1,'cal/(mol*K)','+|-',3.8642),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 04/2019, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds include:
C1=CC=C2CC[CH]C=CC2=C1
""",
)

entry(
    index = 228,
    label = "cyclobutene-allyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {4,S}
3   Cd u0 {1,S} {4,D}
4   Cd u0 {2,S} {3,D}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54,-1.82,-2.08,-2.32,-2.75,-3.14,-3.85],'cal/(mol*K)'),
        H298 = (91.2,'kcal/mol'),
        S298 = (-3.81,'cal/(mol*K)'),
    ),
    shortDesc = """Tian, Z.; Fattahi, A.; Lis, L.; Kass, S. R., "Cycloalkane and Cycloalkene C-H Bond Dissociation Energies," J. Am. Chem. Soc. 2006, 128, 17087-17092, DOI: 10.1021/ja065348u S, Cp copied from Allyl_S""",
    longDesc = 
"""

""",
)

entry(
    index = 229,
    label = "cyclopentene-allyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {4,S}
3   Cd u0 {1,S} {5,D}
4   C  u0 {2,S} {5,S}
5   Cd u0 {3,D} {4,S}
6   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54,-1.82,-2.08,-2.32,-2.75,-3.14,-3.85],'cal/(mol*K)'),
        H298 = (82.3,'kcal/mol'),
        S298 = (-3.81,'cal/(mol*K)'),
    ),
    shortDesc = """Furuyama, S.; Golden, D. M.; Benson, S. W., "Kinetic Study of the Gas-Phase Reaction c-C5H8+I2 c-C5H6+2HI. Heat of Formation and the Stabilization Energy of the Cyclopentenyl Radical,"Int. J. Chem. Kinet. 1970, 2, 93-99. S, Cp copied from Allyl_S""",
    longDesc = 
"""

""",
)

entry(
    index = 230,
    label = "cyclohexene-allyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {7,S}
2   Cs u0 {1,S} {4,S}
3   Cd u0 {1,S} {5,D}
4   C  u0 {2,S} {6,S}
5   Cd u0 {3,D} {6,S}
6   C  u0 {4,S} {5,S}
7   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54,-1.82,-2.08,-2.32,-2.75,-3.14,-3.85],'cal/(mol*K)'),
        H298 = (85,'kcal/mol'),
        S298 = (-3.81,'cal/(mol*K)'),
    ),
    shortDesc = """Alfassi, Z. B.; Feldman, L., "The Kinetics of Radiation-Induced Hydrogen Abstraction by Trichloromethyl Radicals in the Liquid Phase: Cyclohexene," Int. J. Chem. Kinet. 1981, 13, 771-783. S, Cp copied from Allyl_S""",
    longDesc = 
"""

""",
)

entry(
    index = 231,
    label = "C=CCJC=C",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S}
3   Cd u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.13,-1.96,-1.88,-1.89,-2.2,-2.6,-2.6],'cal/(mol*K)'),
        H298 = (76,'kcal/mol'),
        S298 = (-4.05,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 232,
    label = "Aromatic_pi_S_1_4",
    group = 
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {1,S} {5,D}
7   H  u0 {1,S}
""",
    thermo = 'Aromatic_pi_S_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_1_3
""",
)

entry(
    index = 233,
    label = "Aromatic_pi_S_(CH3_CH3_Ortho)_1_4",
    group = 
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S} {8,S}
4   Cs u0 {3,S} {5,S} {9,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {1,S} {5,D}
7   H  u0 {1,S}
8   C  u0 {3,S}
9   C  u0 {4,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 234,
    label = "Aromatic_pi_S_(CH3_C2H5_Ortho)_1_4",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S} {8,S}
4    Cs u0 {3,S} {5,S} {9,S}
5    Cd u0 {4,S} {6,D}
6    Cd u0 {1,S} {5,D}
7    H  u0 {1,S}
8    C  u0 {3,S}
9    C  u0 {4,S} {10,S}
10   C  u0 {9,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
""",
)

entry(
    index = 235,
    label = "Aromatic_pi_S_(fused5)_1_4",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S} {8,S}
4    Cs u0 {3,S} {5,S} {9,S}
5    Cd u0 {4,S} {6,D}
6    Cd u0 {1,S} {5,D}
7    H  u0 {1,S}
8    C  u0 {3,S} {10,S}
9    C  u0 {4,S} {10,S}
10   C  u0 {8,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.748775,0.045256,-0.710099,-1.36165,-2.51235,-3.30599,-4.5709],'cal/(mol*K)','+|-',[0.098378,0.098378,0.098378,0.098378,0.098378,0.098378,0.098378]),
        H298 = (74.4829,'kcal/mol','+|-',1.11628),
        S298 = (0.780097,'cal/(mol*K)','+|-',0.163349),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
C1=CC=C2CCCC2[CH]1
CC1CCC2=CC=C[CH]C21
CCC1CCC2=CC=C[CH]C21
CCCC1CCC2=CC=C[CH]C21
""",
)

entry(
    index = 236,
    label = "Aromatic_pi_S_(fused6)_1_4",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S} {8,S}
4    Cs u0 {3,S} {5,S} {9,S}
5    Cd u0 {4,S} {6,D}
6    Cd u0 {1,S} {5,D}
7    H  u0 {1,S}
8    C  u0 {3,S} {11,S}
9    C  u0 {4,S} {10,S}
10   C  u0 {9,S} {11,S}
11   C  u0 {8,S} {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.01284,-0.508381,-1.05994,-1.55009,-2.56531,-3.36004,-4.58598],'cal/(mol*K)','+|-',[0.129371,0.129371,0.129371,0.129371,0.129371,0.129371,0.129371]),
        H298 = (73.7347,'kcal/mol','+|-',1.66562),
        S298 = (0.399676,'cal/(mol*K)','+|-',0.285184),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
C1=CC=C2CCCCC2[CH]1
CC1CCCC2=CC=C[CH]C21
CCC1CCCC2=CC=C[CH]C21
""",
)

entry(
    index = 237,
    label = "Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_4",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S} {8,S}
4    Cs u0 {3,S} {5,S} {9,S}
5    Cd u0 {4,S} {6,D}
6    Cd u0 {1,S} {5,D}
7    H  u0 {1,S}
8    C  u0 {3,S}
9    C  u0 {4,S} {10,S}
10   Cb u0 {9,S} {11,B} {15,B}
11   Cb u0 {10,B} {12,B}
12   Cb u0 {11,B} {13,B}
13   Cb u0 {12,B} {14,B}
14   Cb u0 {13,B} {15,B}
15   Cb u0 {10,B} {14,B}
""",
    thermo = 'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 238,
    label = "Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_4",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S} {8,S}
4    Cs u0 {3,S} {5,S} {9,S}
5    Cd u0 {4,S} {6,D}
6    Cd u0 {1,S} {5,D}
7    H  u0 {1,S}
8    C  u0 {3,S}
9    Cs u0 {4,S} {10,S} {16,S}
10   Cb u0 {9,S} {11,B} {15,B}
11   Cb u0 {10,B} {12,B}
12   Cb u0 {11,B} {13,B}
13   Cb u0 {12,B} {14,B}
14   Cb u0 {13,B} {15,B}
15   Cb u0 {10,B} {14,B}
16   C  u0 {9,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 239,
    label = "Aromatic_pi_S_(CH3_CH3_Meta)_1_4",
    group = 
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D} {8,S}
3   Cd u0 {2,D} {4,S}
4   Cs u0 {3,S} {5,S} {9,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {1,S} {5,D}
7   H  u0 {1,S}
8   C  u0 {2,S}
9   C  u0 {4,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 240,
    label = "Aromatic_pi_S_(CH3_C2H5_Meta)_1_4",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D} {8,S}
3    Cd u0 {2,D} {4,S}
4    Cs u0 {3,S} {5,S} {9,S}
5    Cd u0 {4,S} {6,D}
6    Cd u0 {1,S} {5,D}
7    H  u0 {1,S}
8    C  u0 {2,S}
9    C  u0 {4,S} {10,S}
10   C  u0 {9,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
""",
)

entry(
    index = 241,
    label = "Aromatic_pi_S_(CH3_Benzyl_Meta)_1_4",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D} {8,S}
3    Cd u0 {2,D} {4,S}
4    Cs u0 {3,S} {5,S} {9,S}
5    Cd u0 {4,S} {6,D}
6    Cd u0 {1,S} {5,D}
7    H  u0 {1,S}
8    C  u0 {2,S}
9    C  u0 {4,S} {10,S}
10   Cb u0 {9,S} {11,B} {15,B}
11   Cb u0 {10,B} {12,B}
12   Cb u0 {11,B} {13,B}
13   Cb u0 {12,B} {14,B}
14   Cb u0 {13,B} {15,B}
15   Cb u0 {10,B} {14,B}
""",
    thermo = 'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 242,
    label = "Aromatic_pi_S_(CH3_EBenzyl_Meta)_1_4",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D} {8,S}
3    Cd u0 {2,D} {4,S}
4    Cs u0 {3,S} {5,S} {9,S}
5    Cd u0 {4,S} {6,D}
6    Cd u0 {1,S} {5,D}
7    H  u0 {1,S}
8    C  u0 {2,S}
9    Cs u0 {4,S} {10,S} {16,S}
10   Cb u0 {9,S} {11,B} {15,B}
11   Cb u0 {10,B} {12,B}
12   Cb u0 {11,B} {13,B}
13   Cb u0 {12,B} {14,B}
14   Cb u0 {13,B} {15,B}
15   Cb u0 {10,B} {14,B}
16   C  u0 {9,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 243,
    label = "Aromatic_pi_S_(CH3_CH3_Sub)_1_4",
    group = 
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cs u0 {3,S} {5,S} {8,S} {9,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {1,S} {5,D}
7   H  u0 {1,S}
8   C  u0 {4,S}
9   C  u0 {4,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 244,
    label = "Aromatic_pi_S_(s1_3_6_diene_1_4)_1_4",
    group = 
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cs u0 {3,S} {5,S} {8,S} {9,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {1,S} {5,D}
7   H  u0 {1,S}
8   C  u0 {4,S} {9,S}
9   C  u0 {4,S} {8,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(s1_3_6_diene_1_4)_1_3
""",
)

entry(
    index = 245,
    label = "Aromatic_pi_S_(CH3_C2H5_Sub)_1_4",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cs u0 {3,S} {5,S} {8,S} {9,S}
5    Cd u0 {4,S} {6,D}
6    Cd u0 {1,S} {5,D}
7    H  u0 {1,S}
8    C  u0 {4,S}
9    C  u0 {4,S} {10,S}
10   C  u0 {9,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
""",
)

entry(
    index = 246,
    label = "Aromatic_pi_S_(s1_4_6_diene_1_4)_1_4",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cs u0 {3,S} {5,S} {8,S} {9,S}
5    Cd u0 {4,S} {6,D}
6    Cd u0 {1,S} {5,D}
7    H  u0 {1,S}
8    C  u0 {4,S} {10,S}
9    C  u0 {4,S} {10,S}
10   C  u0 {8,S} {9,S}
""",
    thermo = 'Aromatic_pi_S_(s1_4_6_diene_1_4)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(s1_4_6_diene_1_4)_1_3
""",
)

entry(
    index = 247,
    label = "Aromatic_pi_S_(s1_5_6_diene_1_4)_1_4",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cs u0 {3,S} {5,S} {8,S} {9,S}
5    Cd u0 {4,S} {6,D}
6    Cd u0 {1,S} {5,D}
7    H  u0 {1,S}
8    C  u0 {4,S} {11,S}
9    C  u0 {4,S} {10,S}
10   C  u0 {9,S} {11,S}
11   C  u0 {8,S} {10,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(s1_5_6_diene_1_4)_1_3
""",
)

entry(
    index = 248,
    label = "Aromatic_pi_S_(s1_6_6_diene_1_4)_1_4",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cs u0 {3,S} {5,S} {8,S} {9,S}
5    Cd u0 {4,S} {6,D}
6    Cd u0 {1,S} {5,D}
7    H  u0 {1,S}
8    C  u0 {4,S} {12,S}
9    C  u0 {4,S} {10,S}
10   C  u0 {9,S} {11,S}
11   C  u0 {10,S} {12,S}
12   C  u0 {8,S} {11,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(s1_6_6_diene_1_4)_1_3
""",
)

entry(
    index = 249,
    label = "Aromatic_pi_S_(CH3_Benzyl_Sub)_1_4",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cs u0 {3,S} {5,S} {8,S} {9,S}
5    Cd u0 {4,S} {6,D}
6    Cd u0 {1,S} {5,D}
7    H  u0 {1,S}
8    C  u0 {4,S}
9    C  u0 {4,S} {10,S}
10   Cb u0 {9,S} {11,B} {15,B}
11   Cb u0 {10,B} {12,B}
12   Cb u0 {11,B} {13,B}
13   Cb u0 {12,B} {14,B}
14   Cb u0 {13,B} {15,B}
15   Cb u0 {10,B} {14,B}
""",
    thermo = 'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 250,
    label = "Aromatic_pi_S_(CH3_EBenzyl_Sub)_1_4",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cs u0 {3,S} {5,S} {8,S} {9,S}
5    Cd u0 {4,S} {6,D}
6    Cd u0 {1,S} {5,D}
7    H  u0 {1,S}
8    C  u0 {4,S}
9    Cs u0 {4,S} {10,S} {16,S}
10   Cb u0 {9,S} {11,B} {15,B}
11   Cb u0 {10,B} {12,B}
12   Cb u0 {11,B} {13,B}
13   Cb u0 {12,B} {14,B}
14   Cb u0 {13,B} {15,B}
15   Cb u0 {10,B} {14,B}
16   C  u0 {9,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 251,
    label = "cyclopropenyl-allyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {1,S} {2,D}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.13,-1.96,-1.88,-1.89,-2.2,-2.6,-2.6],'cal/(mol*K)'),
        H298 = (90.6,'kcal/mol'),
        S298 = (-4.05,'cal/(mol*K)'),
    ),
    shortDesc = """DeFrees, D. J.; McIver, R. T., Jr.; Hehre, W. J., "Heats of Formation of Gaseous Free Radicals via Ion Cyclotron Double Resonance Spectroscopy," J. Am. Chem. Soc. 1980, 102, 3334-3338, DOI: 10.1021/ja00530a005 S, Cp copied from C=CCJC=C""",
    longDesc = 
"""

""",
)

entry(
    index = 252,
    label = "1,3-cyclopentadiene-allyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cd u0 {1,S} {4,D}
3   Cd u0 {1,S} {5,D}
4   Cd u0 {2,D} {5,S}
5   Cd u0 {3,D} {4,S}
6   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.157,0.892,-0.937,-2.776,-4.931,-3.793,-4.855],'cal/(mol*K)'),
        H298 = (84.912,'kcal/mol'),
        S298 = (-2.047,'cal/(mol*K)'),
    ),
    shortDesc = """Combined experimental and theoretical results of Tranter for 1,2-CPD'yl""",
    longDesc = 
"""
Absolute Enthalpy of formation at 298 K from experiment (1998 Kern and Tranter).
All other  values from theory (2001 Kiefer and Tranter).
""",
)

entry(
    index = 253,
    label = "C=CCJC=C=O",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {6,D}
4   Cdd u0 {2,D} {7,D}
5   H   u0 {1,S}
6   C   u0 {3,D}
7   O2d u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.5,-3.8,-3.7,-4.3,-6.1,-8.1,-11.5],'J/(mol*K)'),
        H298 = (318,'kJ/mol'),
        S298 = (-22,'J/(mol*K)'),
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
    index = 254,
    label = "Sec_Propargyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Ct u0 {1,S}
3   Cs u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.59,-1.2,-1.75,-2.19,-2.91,-3.49,-3.49],'cal/(mol*K)'),
        H298 = (87,'kcal/mol'),
        S298 = (-0.45,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 255,
    label = "CCJC=O",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   C   u0 {1,S}
4   H   u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.9,-3.4,-3.4,-4.2,-6.7,-9.2,-13.9],'J/(mol*K)'),
        H298 = (379.1,'kJ/mol'),
        S298 = (-5.7,'J/(mol*K)'),
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
    index = 256,
    label = "CCJCHO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D} {6,S}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   O2d u0 {2,D}
6   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.36,-1.57,-1.73,-1.89,-2.66,-3.11,-3.5],'cal/(mol*K)'),
        H298 = (91.9,'kcal/mol'),
        S298 = (-2.37,'cal/(mol*K)'),
    ),
    shortDesc = """CHEN & BOZZELLI #""",
    longDesc = 
"""

""",
)

entry(
    index = 257,
    label = "C=OCJC=O",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   CO  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   O2d u0 {2,D}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.9,1.5,0.9,0,-2.5,-5.1,-10.2],'J/(mol*K)'),
        H298 = (382.7,'kJ/mol'),
        S298 = (-13,'J/(mol*K)'),
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
    index = 258,
    label = "Cs_T",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
""",
    thermo = 'Tertalkyl',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 259,
    label = "CCJ(C)CO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   C   u0 {1,S} {5,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.8,-9.3,-10.3,-11,-12.4,-13.7,-16.1],'J/(mol*K)'),
        H298 = (369.4,'kJ/mol'),
        S298 = (-0.8,'J/(mol*K)'),
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
    index = 260,
    label = "C2CJCOOH",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   Cs  u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   O2s u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.54,-4.16,-4.44,-4.58,-4.74,-4.88,-5.23],'cal/(mol*K)'),
        H298 = (97.2,'kcal/mol'),
        S298 = (7.31,'cal/(mol*K)'),
    ),
    shortDesc = """WIJAYA et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 261,
    label = "Tertalkyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (96.5,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
"""

""",
)

entry(
    index = 262,
    label = "bicyclo[1.1.0]butane-tertiary",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2 * Cs u1 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (113.8,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 263,
    label = "bicyclo[2.1.0]pentane-tertiary",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {2,S} {5,S}
5   Cs u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (110.2,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 264,
    label = "bicyclo[1.1.1]pentane-C1",
    group = 
"""
1 * Cs u1 {3,S} {4,S} {5,S}
2   Cs u0 {3,S} {4,S} {5,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {2,S}
5   Cs u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (106.2,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 265,
    label = "bicyclo[3.1.0]hexane-tertiary",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {2,S} {6,S}
5   Cs u0 {1,S} {6,S}
6   Cs u0 {4,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (108.6,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 266,
    label = "bicyclo[2.2.0]hexane-tertiary",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S}
3   Cs u0 {1,S} {4,S}
4   Cs u0 {2,S} {3,S}
5   Cs u0 {2,S} {6,S}
6   Cs u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (104,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 267,
    label = "bicyclo[2.1.1]hexane-C1",
    group = 
"""
1 * Cs u1 {3,S} {4,S} {6,S}
2   Cs u0 {3,S} {4,S} {5,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {2,S}
5   C  u0 {2,S} {6,S}
6   Cs u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (108.9,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 268,
    label = "bridgehead_norbornyl",
    group = 
"""
1 * Cs u1 {3,S} {4,S} {7,S}
2   Cs u0 {3,S} {5,S} {6,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {5,S}
5   Cs u0 {2,S} {4,S}
6   Cs u0 {2,S} {7,S}
7   Cs u0 {1,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (107.42,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """P.M. Nunes, S.G. Estacio, G.T. Lopes, B.J. Costa Cabral, R.M. Borges dos Santos, J.A. Martinho Simoes, CH Bond Dissociation Enthalpies in Norbornane. An Experimental and Computational Study, Organic Letters, 10 (2008) 1613-1616. S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 269,
    label = "bicyclo[3.2.0]heptane-tertiary",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S}
3   Cs u0 {1,S} {4,S}
4   Cs u0 {2,S} {3,S}
5   Cs u0 {2,S} {7,S}
6   Cs u0 {1,S} {7,S}
7   Cs u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (102.6,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 270,
    label = "bicyclo[4.1.0]heptane-tertiary",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {2,S} {6,S}
5   Cs u0 {1,S} {7,S}
6   Cs u0 {4,S} {7,S}
7   Cs u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (105.4,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 271,
    label = "bicyclo[3.1.1]heptane-C1",
    group = 
"""
1 * Cs u1 {3,S} {4,S} {6,S}
2   Cs u0 {3,S} {4,S} {5,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {2,S}
5   C  u0 {2,S} {7,S}
6   Cs u0 {1,S} {7,S}
7   C  u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (103.6,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 272,
    label = "octahydro-pentalene-tertiary",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {5,S} {6,S}
3   Cs u0 {1,S} {8,S}
4   Cs u0 {1,S} {7,S}
5   C  u0 {2,S} {7,S}
6   C  u0 {2,S} {8,S}
7   C  u0 {4,S} {5,S}
8   C  u0 {3,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (95.7,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 273,
    label = "bicyclo[4.2.0]octane-tertiary",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S}
3   Cs u0 {1,S} {4,S}
4   C  u0 {2,S} {3,S}
5   C  u0 {2,S} {7,S}
6   Cs u0 {1,S} {8,S}
7   C  u0 {5,S} {8,S}
8   C  u0 {6,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (97,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 274,
    label = "bicyclo[2.2.2]octane-C1",
    group = 
"""
1 * Cs u1 {3,S} {6,S} {8,S}
2   Cs u0 {4,S} {5,S} {7,S}
3   Cs u0 {1,S} {4,S}
4   C  u0 {2,S} {3,S}
5   C  u0 {2,S} {6,S}
6   Cs u0 {1,S} {5,S}
7   C  u0 {2,S} {8,S}
8   Cs u0 {1,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (101.9,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 275,
    label = "Benzyl_T",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cb u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.27,-0.78,-1.54,-2.06,-2.74,-3.19,-3.19],'cal/(mol*K)'),
        H298 = (83.8,'kcal/mol'),
        S298 = (-5.34,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 276,
    label = "Benzyl_T_Fused5",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cb u0 {1,S} {5,B}
3   C  u0 {1,S} {6,[S,B,T]}
4   C  u0 {1,S}
5   Cb u0 {2,B} {6,S}
6   C  u0 {3,[S,B,T]} {5,S}
""",
    thermo = None,
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds Include
CC1C[CH]C2=CC=CC=C21
CCC1C[CH]C2=CC=CC=C21
CCCC1C[CH]C2=CC=CC=C21
""",
)

entry(
    index = 277,
    label = "Benzyl_T_Fused6",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cb u0 {1,S} {5,B}
3   C  u0 {1,S} {7,[S,D,T,B]}
4   C  u0 {1,S}
5   Cb u0 {2,B} {6,S}
6   C  u0 {5,S} {7,[S,D,T,B]}
7   C  u0 {3,[S,D,T,B]} {6,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds Include
C[C]1CCCC2=CC=CC=C21
CC[C]1CCCC2=CC=CC=C21
""",
)

entry(
    index = 278,
    label = "Benzyl_T_dihydronaphthalene",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cb u0 {1,S} {5,B}
3   C  u0 {1,S} {7,[S,D,T,B]}
4   C  u0 {1,S}
5   Cb u0 {2,B} {6,S}
6   Cd u0 {5,S} {7,D}
7   Cd u0 {3,[S,D,T,B]} {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.264274,-0.237466,-0.864612,-1.639,-2.84087,-3.59047,-4.6789],'cal/(mol*K)','+|-',[0.546927,0.546927,0.546927,0.546927,0.546927,0.546927,0.546927]),
        H298 = (83.3368,'kcal/mol','+|-',2.01563),
        S298 = (2.12045,'cal/(mol*K)','+|-',0.802466),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 07/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
C[C]1CC=CC2=CC=CC=C12
CC[C]1CC=CC2=CC=CC=C12
""",
)

entry(
    index = 279,
    label = "CCJ(C)C=C=O",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.1,-10,-11.8,-12.9,-14.1,-15.1,-16.9],'J/(mol*K)'),
        H298 = (361.8,'kJ/mol'),
        S298 = (3.5,'J/(mol*K)'),
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
    index = 280,
    label = "C=CCJ(C)C=C=O",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {6,D}
4   Cdd u0 {2,D} {7,D}
5   C   u0 {1,S}
6   C   u0 {3,D}
7   O2d u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.8,-8.2,-8.9,-9.3,-10.1,-11,-12.9],'J/(mol*K)'),
        H298 = (313.4,'kJ/mol'),
        S298 = (0.5,'J/(mol*K)'),
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
    index = 281,
    label = "C=CCJ(C=C=O)C=C",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {8,D}
6   C   u0 {3,D}
7   C   u0 {4,D}
8   O2d u0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10.7,-9.3,-8.1,-7.2,-6.8,-7.2,-8.8],'J/(mol*K)'),
        H298 = (287.1,'kJ/mol'),
        S298 = (-27.5,'J/(mol*K)'),
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
    index = 282,
    label = "Allyl_T",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.79,-2.38,-2.74,-2.97,-3.28,-3.55,-3.55],'cal/(mol*K)'),
        H298 = (83.4,'kcal/mol'),
        S298 = (-3.69,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 283,
    label = "Aromatic_pi_T_1_3",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {7,D}
3   C  u0 {1,S}
4   Cs u0 {1,S} {5,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {7,S}
7   Cd u0 {2,D} {6,S}
""",
    thermo = 'Aromatic_pi_S_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_1_3
""",
)

entry(
    index = 284,
    label = "Aromatic_pi_T_(CH3_CH3_Ortho)_1_3",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {7,D}
3   C  u0 {1,S}
4   Cs u0 {1,S} {5,S} {8,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {7,S}
7   Cd u0 {2,D} {6,S}
8   C  u0 {4,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 285,
    label = "Aromatic_pi_T_(CH3_C2H5_Ortho)_1_3",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {7,D}
3   C  u0 {1,S}
4   Cs u0 {1,S} {5,S} {8,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {7,S}
7   Cd u0 {2,D} {6,S}
8   C  u0 {4,S} {9,S}
9   C  u0 {8,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
""",
)

entry(
    index = 286,
    label = "Aromatic_pi_T_(fused5)_1_3",
    group = 
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {1,S} {5,S} {8,S}
7   C  u0 {1,S} {9,S}
8   C  u0 {6,S} {9,S}
9   C  u0 {7,S} {8,S}
""",
    thermo = 'Aromatic_pi_S_(fused5)_1_4',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
C1=CC=C2CCCC2[CH]1
CC1CCC2=CC=C[CH]C21
CCC1CCC2=CC=C[CH]C21
CCCC1CCC2=CC=C[CH]C21
C1=CC=C2CCCCC2[CH]1
CC1CCCC2=CC=C[CH]C21
CCC1CCCC2=CC=C[CH]C21
""",
)

entry(
    index = 287,
    label = "Aromatic_pi_T_(fused6)_1_3",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cd u0 {3,S} {5,D}
5    Cd u0 {4,D} {6,S}
6    Cs u0 {1,S} {5,S} {8,S}
7    C  u0 {1,S} {10,S}
8    C  u0 {6,S} {9,S}
9    C  u0 {8,S} {10,S}
10   C  u0 {7,S} {9,S}
""",
    thermo = 'Aromatic_pi_S_(fused5)_1_4',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
C1=CC=C2CCCC2[CH]1
CC1CCC2=CC=C[CH]C21
CCC1CCC2=CC=C[CH]C21
CCCC1CCC2=CC=C[CH]C21
C1=CC=C2CCCCC2[CH]1
CC1CCCC2=CC=C[CH]C21
CCC1CCCC2=CC=C[CH]C21
""",
)

entry(
    index = 288,
    label = "Aromatic_pi_T_(CH3_Benzyl_Ortho)_1_3",
    group = 
"""
1  * Cs u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {7,D}
3    C  u0 {1,S}
4    Cs u0 {1,S} {5,S} {8,S}
5    Cd u0 {4,S} {6,D}
6    Cd u0 {5,D} {7,S}
7    Cd u0 {2,D} {6,S}
8    C  u0 {4,S} {9,S}
9    Cb u0 {8,S} {10,B} {14,B}
10   Cb u0 {9,B} {11,B}
11   Cb u0 {10,B} {12,B}
12   Cb u0 {11,B} {13,B}
13   Cb u0 {12,B} {14,B}
14   Cb u0 {9,B} {13,B}
""",
    thermo = 'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 289,
    label = "Aromatic_pi_T_(CH3_EBenzyl_Ortho)_1_3",
    group = 
"""
1  * Cs u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {7,D}
3    C  u0 {1,S}
4    Cs u0 {1,S} {5,S} {8,S}
5    Cd u0 {4,S} {6,D}
6    Cd u0 {5,D} {7,S}
7    Cd u0 {2,D} {6,S}
8    Cs u0 {4,S} {9,S} {15,S}
9    Cb u0 {8,S} {10,B} {14,B}
10   Cb u0 {9,B} {11,B}
11   Cb u0 {10,B} {12,B}
12   Cb u0 {11,B} {13,B}
13   Cb u0 {12,B} {14,B}
14   Cb u0 {9,B} {13,B}
15   C  u0 {8,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 290,
    label = "Aromatic_pi_T_1_4",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {7,D}
3   C  u0 {1,S}
4   Cd u0 {1,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cd u0 {2,D} {6,S}
""",
    thermo = 'Aromatic_pi_S_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_1_3
""",
)

entry(
    index = 291,
    label = "Aromatic_pi_T_(CH3_CH3_Para)_1_4",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {7,D}
3   C  u0 {1,S}
4   Cd u0 {1,S} {5,D} {8,S}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cd u0 {2,D} {6,S}
8   C  u0 {4,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 292,
    label = "Aromatic_pi_T_(CH3_C2H5_Para)_1_4",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {7,D}
3   C  u0 {1,S}
4   Cd u0 {1,S} {5,D} {8,S}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cd u0 {2,D} {6,S}
8   C  u0 {4,S} {9,S}
9   C  u0 {8,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
""",
)

entry(
    index = 293,
    label = "Aromatic_pi_T_(CH3_Benzyl_Para)_1_4",
    group = 
"""
1  * Cs u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {7,D}
3    C  u0 {1,S}
4    Cd u0 {1,S} {5,D} {8,S}
5    Cd u0 {4,D} {6,S}
6    Cs u0 {5,S} {7,S}
7    Cd u0 {2,D} {6,S}
8    C  u0 {4,S} {9,S}
9    Cb u0 {8,S} {10,B} {14,B}
10   Cb u0 {9,B} {11,B}
11   Cb u0 {10,B} {12,B}
12   Cb u0 {11,B} {13,B}
13   Cb u0 {12,B} {14,B}
14   Cb u0 {9,B} {13,B}
""",
    thermo = 'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 294,
    label = "Aromatic_pi_T_(CH3_EBenzyl_Para)_1_4",
    group = 
"""
1  * Cs u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {7,D}
3    C  u0 {1,S}
4    Cd u0 {1,S} {5,D} {8,S}
5    Cd u0 {4,D} {6,S}
6    Cs u0 {5,S} {7,S}
7    Cd u0 {2,D} {6,S}
8    Cs u0 {4,S} {9,S} {15,S}
9    Cb u0 {8,S} {10,B} {14,B}
10   Cb u0 {9,B} {11,B}
11   Cb u0 {10,B} {12,B}
12   Cb u0 {11,B} {13,B}
13   Cb u0 {12,B} {14,B}
14   Cb u0 {9,B} {13,B}
15   C  u0 {8,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 295,
    label = "bicyclo[2.1.0]pent-2-ene-C1",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S}
4   Cd u0 {2,S} {5,D}
5   Cd u0 {1,S} {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (112.1,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 296,
    label = "bicyclo[2.1.1]hex-2-ene-C1",
    group = 
"""
1 * Cs u1 {3,S} {4,S} {6,S}
2   Cs u0 {3,S} {4,S} {5,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {2,S}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (110.1,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 297,
    label = "bicyclo[2.2.0]hexa-2,5-diene-C1",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S}
3   Cd u0 {1,S} {4,D}
4   Cd u0 {2,S} {3,D}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (102.8,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 298,
    label = "C=CCJ(C)C=O",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {6,D}
4   C   u0 {1,S}
5   C   u0 {2,D}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-12.2,-10.5,-9.4,-9,-9.1,-9.7,-11.5],'J/(mol*K)'),
        H298 = (335.4,'kJ/mol'),
        S298 = (-17.3,'J/(mol*K)'),
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
    index = 299,
    label = "C=CCJ(C=O)C=C",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {6,D}
5   C   u0 {2,D}
6   C   u0 {4,D}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10,-7.5,-6.1,-5.5,-5.6,-6.4,-8.5],'J/(mol*K)'),
        H298 = (307.4,'kJ/mol'),
        S298 = (-27.9,'J/(mol*K)'),
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
    index = 300,
    label = "Tert_Propargyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Ct u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.04,-1.01,-1.74,-2.41,-3.19,-3.65,-3.65],'cal/(mol*K)'),
        H298 = (84.5,'kcal/mol'),
        S298 = (1.48,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 301,
    label = "C2CJCO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D} {6,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   O2d u0 {2,D}
6   R   u0 {2,S}
""",
    thermo = 'C2CJCHO',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 302,
    label = "C2CJCHO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D} {6,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   O2d u0 {2,D}
6   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.62,-0.2,-1.23,-1.82,-2.87,-3.47,-3.47],'cal/(mol*K)'),
        H298 = (89.8,'kcal/mol'),
        S298 = (-1.71,'cal/(mol*K)'),
    ),
    shortDesc = """CHEN & BOZZELLI #. Value for Cp1500 taken as equal to Cp1000""",
    longDesc = 
"""

""",
)

entry(
    index = 303,
    label = "CsJO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.9,3.7,1.6,-0.9,-5.9,-10.3,-17.5],'J/(mol*K)'),
        H298 = (413.3,'kJ/mol'),
        S298 = (1.2,'J/(mol*K)'),
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
    index = 304,
    label = "CsJOH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.25,0.18,-0.26,-0.83,-1.95,-2.85,-4.22],'cal/(mol*K)'),
        H298 = (96.51,'kcal/mol'),
        S298 = (0.09,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 305,
    label = "CsJOC",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   C   u0 {2,S}
""",
    thermo = 'CsJOCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 306,
    label = "CsJOCs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   Cs  u0 {2,S}
""",
    thermo = 'CsJOCH3',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 307,
    label = "CsJOCH3",
    group = 
"""
1   Cs  u0 {3,S} {4,S} {5,S} {6,S}
2 * Cs  u1 {3,S} {7,S} {8,S}
3   O2s u0 {1,S} {2,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   H   u0 {2,S}
8   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.16,-0.4,-0.82,-1.33,-2.32,-3.13,-4.37],'cal/(mol*K)'),
        H298 = (97,'kcal/mol'),
        S298 = (0.78,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN #""",
    longDesc = 
"""

""",
)

entry(
    index = 308,
    label = "CsJOCC",
    group = 
"""
1   Cs  u0 {3,S} {4,S} {5,S} {6,S}
2 * Cs  u1 {3,S} {7,S} {8,S}
3   O2s u0 {1,S} {2,S}
4   C   u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   H   u0 {2,S}
8   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.01,-1.22,-1.4,-1.71,-3.5,-3.24,-4.42],'cal/(mol*K)'),
        H298 = (96.83,'kcal/mol'),
        S298 = (1.41,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated from data in SUMATHI & GREEN. Values might have large error bars.""",
    longDesc = 
"""

""",
)

entry(
    index = 309,
    label = "CsJOCC2",
    group = 
"""
1   Cs  u0 {3,S} {4,S} {5,S} {6,S}
2 * Cs  u1 {3,S} {7,S} {8,S}
3   O2s u0 {1,S} {2,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   H   u0 {1,S}
7   H   u0 {2,S}
8   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.95,0.75,0.23,-0.43,-1.71,-2.72,-4.19],'cal/(mol*K)'),
        H298 = (96.16,'kcal/mol'),
        S298 = (-0.59,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 310,
    label = "CsJOCC3",
    group = 
"""
1   Cs  u0 {3,S} {4,S} {5,S} {6,S}
2 * Cs  u1 {3,S} {7,S} {8,S}
3   O2s u0 {1,S} {2,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   C   u0 {1,S}
7   H   u0 {2,S}
8   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.08,-0.09,-0.52,-1.06,-2.11,-2.96,-4.27],'cal/(mol*K)'),
        H298 = (95.75,'kcal/mol'),
        S298 = (0.27,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 311,
    label = "CsJOCds",
    group = 
"""
1 * Cs      u1 {2,S} {3,S} {4,S}
2   O2s     u0 {1,S} {5,S}
3   H       u0 {1,S}
4   H       u0 {1,S}
5   [Cd,CO] u0 {2,S}
""",
    thermo = 'CsJOC(O)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 312,
    label = "CsJOC(O)",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   CO  u0 {2,S} {6,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.91,0.89,0.42,-0.21,-1.5,-2.62,-4.43],'cal/(mol*K)'),
        H298 = (100.7,'kcal/mol'),
        S298 = (-0.18,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 313,
    label = "CsJOC(O)H",
    group = 
"""
1 * Cs  u1 {3,S} {4,S} {5,S}
2   CO  u0 {3,S} {6,D} {7,S}
3   O2s u0 {1,S} {2,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
7   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.95,0.97,0.53,-0.12,-1.54,-2.76,-4.53],'cal/(mol*K)'),
        H298 = (100.88,'kcal/mol'),
        S298 = (-0.18,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 314,
    label = "CsJOC(O)C",
    group = 
"""
1 * Cs  u1 {3,S} {4,S} {5,S}
2   CO  u0 {3,S} {6,D} {7,S}
3   O2s u0 {1,S} {2,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
7   C   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.88,0.81,0.31,-0.3,-1.45,-2.47,-4.33],'cal/(mol*K)'),
        H298 = (100.48,'kcal/mol'),
        S298 = (-0.17,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 315,
    label = "C=COCJ",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   Cd  u0 {2,S} {6,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   C   u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.9,-7.2,-8.9,-10.6,-13.6,-15.9,-19.7],'J/(mol*K)'),
        H298 = (409.4,'kJ/mol'),
        S298 = (13.7,'J/(mol*K)'),
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
    index = 316,
    label = "CsJOO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.18,-0.42,-0.79,-1.2,-1.99,-2.63,-3.65],'cal/(mol*K)'),
        H298 = (98.5,'kcal/mol'),
        S298 = (-1.57,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 317,
    label = "CsJOOH",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.06,-0.35,-0.76,-1.19,-1.99,-2.64,-3.68],'cal/(mol*K)'),
        H298 = (98.91,'kcal/mol'),
        S298 = (-1.52,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 318,
    label = "CsJOOC",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   C   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.31,-0.48,-0.82,-1.22,-1.99,-2.62,-3.63],'cal/(mol*K)'),
        H298 = (98.34,'kcal/mol'),
        S298 = (-1.62,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 319,
    label = "CCsJO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S}
3   C   u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.2,0.4,-1.5,-3.9,-8.6,-12.5,-18.7],'J/(mol*K)'),
        H298 = (402,'kJ/mol'),
        S298 = (3.9,'J/(mol*K)'),
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
    index = 320,
    label = "CCsJOC",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   C   u0 {1,S}
4   H   u0 {1,S}
5   C   u0 {2,S}
""",
    thermo = 'CCsJOCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 321,
    label = "C=CCJ(O)C",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   O2s u0 {1,S} {6,S}
4   H   u0 {1,S}
5   C   u0 {2,D}
6   C   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.7,-8.4,-10,-11,-12.1,-13.1,-15.5],'J/(mol*K)'),
        H298 = (328.3,'kJ/mol'),
        S298 = (4.5,'J/(mol*K)'),
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
    index = 322,
    label = "CCsJOCs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   C   u0 {1,S}
4   H   u0 {1,S}
5   Cs  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.82,0.53,-0.11,-0.86,-2.2,-3.18,-4.51],'cal/(mol*K)'),
        H298 = (95.41,'kcal/mol'),
        S298 = (0.33,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 323,
    label = "CCsJOCds",
    group = 
"""
1 * Cs      u1 {2,S} {3,S} {4,S}
2   O2s     u0 {1,S} {5,S}
3   C       u0 {1,S}
4   H       u0 {1,S}
5   [CO,Cd] u0 {2,S}
""",
    thermo = 'CCsJOC(O)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 324,
    label = "CCsJOC(O)",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   CO  u0 {2,S} {6,D}
4   C   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.16,0.78,0.05,-0.73,-2.13,-3.24,-4.9],'cal/(mol*K)'),
        H298 = (98.7,'kcal/mol'),
        S298 = (0.98,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 325,
    label = "CCsJOC(O)H",
    group = 
"""
1 * Cs  u1 {3,S} {4,S} {5,S}
2   CO  u0 {3,S} {6,D} {7,S}
3   O2s u0 {1,S} {2,S}
4   C   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
7   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.2,0.88,0.16,-0.67,-2.22,-3.43,-5],'cal/(mol*K)'),
        H298 = (98.87,'kcal/mol'),
        S298 = (0.98,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 326,
    label = "CCsJOC(O)C",
    group = 
"""
1 * Cs  u1 {3,S} {4,S} {5,S}
2   CO  u0 {3,S} {6,D} {7,S}
3   O2s u0 {1,S} {2,S}
4   C   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
7   C   u0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 327,
    label = "C=CCJO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   O2s u0 {1,S}
4   H   u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6,-3.9,-3,-3.2,-5.7,-8.6,-13.8],'J/(mol*K)'),
        H298 = (333.9,'kJ/mol'),
        S298 = (-7.4,'J/(mol*K)'),
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
    index = 328,
    label = "OCJC=O",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   O2s u0 {1,S}
4   H   u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-3.3,-5.6,-7.4,-9.8,-11.2,-14],'J/(mol*K)'),
        H298 = (356.6,'kJ/mol'),
        S298 = (0.2,'J/(mol*K)'),
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
    index = 329,
    label = "CCsJOH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   C   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.65,-0.01,-0.75,-1.43,-2.52,-3.31,-4.47],'cal/(mol*K)'),
        H298 = (95.39,'kcal/mol'),
        S298 = (0.92,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 330,
    label = "CCsJOO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   C   u0 {1,S}
4   H   u0 {1,S}
5   O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.48,-1.15,-1.68,-2.11,-2.77,-3.26,-4.02],'cal/(mol*K)'),
        H298 = (96.9,'kcal/mol'),
        S298 = (0.76,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 331,
    label = "CCsJOOH",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   C   u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.39,-1.08,-1.64,-2.08,-2.75,-3.26,-4.03],'cal/(mol*K)'),
        H298 = (97.19,'kcal/mol'),
        S298 = (0.77,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 332,
    label = "CCsJOOC",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   C   u0 {1,S}
5   H   u0 {1,S}
6   C   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.58,-1.21,-1.73,-2.15,-2.8,-3.27,-4.01],'cal/(mol*K)'),
        H298 = (96.64,'kcal/mol'),
        S298 = (0.74,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 333,
    label = "C2CsJO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2,-7.1,-10.7,-13.4,-16.6,-18.5,-21.2],'J/(mol*K)'),
        H298 = (398.4,'kJ/mol'),
        S298 = (14.4,'J/(mol*K)'),
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
    index = 334,
    label = "C2CsJOH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.31,-0.66,-1.54,-2.23,-3.17,-3.8,-4.72],'cal/(mol*K)'),
        H298 = (94.5,'kcal/mol'),
        S298 = (2.17,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 335,
    label = "C2CsJOC",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   C   u0 {2,S}
""",
    thermo = 'C2CsJOCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 336,
    label = "C2CsJOCs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   Cs  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.09,-1.37,-2.49,-3.26,-4.15,-4.63,-5.23],'cal/(mol*K)'),
        H298 = (95.5,'kcal/mol'),
        S298 = (3.71,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 337,
    label = "C2CsJOCds",
    group = 
"""
1 * Cs      u1 {2,S} {3,S} {4,S}
2   O2s     u0 {1,S} {5,S}
3   C       u0 {1,S}
4   C       u0 {1,S}
5   [Cd,CO] u0 {2,S}
""",
    thermo = 'C2CsJOC(O)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 338,
    label = "C2CsJOC(O)",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   CO  u0 {2,S} {6,D}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.04,-1.34,-2.3,-2.99,-3.99,-4.77,-5.98],'cal/(mol*K)'),
        H298 = (100.1,'kcal/mol'),
        S298 = (4.77,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 339,
    label = "C2CsJOC(O)H",
    group = 
"""
1 * Cs  u1 {3,S} {4,S} {5,S}
2   CO  u0 {3,S} {6,D} {7,S}
3   O2s u0 {1,S} {2,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   O2d u0 {2,D}
7   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.03,-1.28,-2.28,-3.1,-4.35,-5.19,-6.06],'cal/(mol*K)'),
        H298 = (99.97,'kcal/mol'),
        S298 = (4.88,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 340,
    label = "C2CsJOC(O)C",
    group = 
"""
1 * Cs  u1 {3,S} {4,S} {5,S}
2   CO  u0 {3,S} {6,D} {7,S}
3   O2s u0 {1,S} {2,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   O2d u0 {2,D}
7   C   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.04,-1.4,-2.32,-2.89,-3.62,-4.36,-5.9],'cal/(mol*K)'),
        H298 = (100.25,'kcal/mol'),
        S298 = (4.66,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 341,
    label = "C2CsJOO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.89,-2.09,-2.81,-3.24,-3.69,-3.97,-4.43],'cal/(mol*K)'),
        H298 = (96.7,'kcal/mol'),
        S298 = (2.22,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 342,
    label = "C2CsJOOH",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   H   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.01,-2.17,-2.87,-3.3,-3.77,-4.05,-4.49],'cal/(mol*K)'),
        H298 = (96.74,'kcal/mol'),
        S298 = (2.37,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 343,
    label = "C2CsJOOC",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   C   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.02,-2.75,-3.18,-3.62,-3.88,-4.37],'cal/(mol*K)'),
        H298 = (96.58,'kcal/mol'),
        S298 = (2.08,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 344,
    label = "CsJ-S",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   S  ux {1,S}
3   R  ux {1,S}
4   R  ux {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 345,
    label = "CsJ-SsHH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   S2s u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.07,-0.32,-0.73,-1.22,-2.18,-2.99,-4.27],'cal/(mol*K)'),
        H298 = (95.34,'kcal/mol'),
        S298 = (1.18,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 346,
    label = "CsJ-CSH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
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
    index = 347,
    label = "CsJ-CsSsH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   S2s u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.25,-0.79,-1.36,-1.9,-2.82,-3.53,-4.64],'cal/(mol*K)'),
        H298 = (92.87,'kcal/mol'),
        S298 = (1.91,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 348,
    label = "CsJ-CtSsH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Ct  u0 {1,S}
3   S2s u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.26,-0.02,-0.47,-0.97,-1.95,-2.77,-4.12],'cal/(mol*K)'),
        H298 = (83.48,'kcal/mol'),
        S298 = (-0.16,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 349,
    label = "CsJ-CbSsH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cb  u0 {1,S}
3   S2s u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.32,-0.38,-0.65,-1.01,-1.75,-2.4,-3.57],'cal/(mol*K)'),
        H298 = (84.88,'kcal/mol'),
        S298 = (-0.98,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 350,
    label = "CsJ-CdSsH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   S2s u0 {1,S}
4   H   u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.21,-2.77,-2.39,-2.24,-2.39,-2.74,-3.56],'cal/(mol*K)'),
        H298 = (81.92,'kcal/mol'),
        S298 = (0.66,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 351,
    label = "CsJ-C=SSsH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CS  u0 {1,S} {5,D}
3   S2s u0 {1,S}
4   H   u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.75,-2.93,-2.07,-1.54,-1.2,-1.31,-2.01],'cal/(mol*K)'),
        H298 = (71.51,'kcal/mol'),
        S298 = (-3.81,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 352,
    label = "CsJ-CCS",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 353,
    label = "CsJ-CsCsSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.72,-2.04,-2.88,-3.4,-3.99,-4.36,-4.96],'cal/(mol*K)'),
        H298 = (92.32,'kcal/mol'),
        S298 = (3.87,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 354,
    label = "CsJ-CsCtSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   Ct  u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.99,-1.64,-2.18,-2.62,-3.3,-3.82,-4.65],'cal/(mol*K)'),
        H298 = (81.17,'kcal/mol'),
        S298 = (3.05,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 355,
    label = "CsJ-CsCbSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   Cb  u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.99,-2.26,-2.53,-2.75,-3.12,-3.49,-4.43],'cal/(mol*K)'),
        H298 = (84.1,'kcal/mol'),
        S298 = (0.96,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 356,
    label = "CsJ-CsCdSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cs  u0 {1,S}
4   S2s u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4,-4.74,-4.81,-4.59,-4.17,-3.99,-4.12],'cal/(mol*K)'),
        H298 = (80.07,'kcal/mol'),
        S298 = (2.53,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 357,
    label = "CsJ-CsC=SSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CS  u0 {1,S} {5,D}
3   Cs  u0 {1,S}
4   S2s u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.86,-3.83,-3.41,-2.93,-2.28,-2.07,-2.36],'cal/(mol*K)'),
        H298 = (69.17,'kcal/mol'),
        S298 = (-1.97,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 358,
    label = "CsJ-SS",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   S2s u0 {1,S}
3   S2s u0 {1,S}
4   R   u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 359,
    label = "CsJ-SsSsH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   S2s u0 {1,S}
3   S2s u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.52,-4,-3.64,-3.53,-3.68,-4,-4.72],'cal/(mol*K)'),
        H298 = (90.16,'kcal/mol'),
        S298 = (1.31,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 360,
    label = "CsJ-CSS",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
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
    index = 361,
    label = "CsJ-CsSsSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.36,-4,-4.17,-4.24,-4.37,-4.55,-5],'cal/(mol*K)'),
        H298 = (89.98,'kcal/mol'),
        S298 = (5.5,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 362,
    label = "CsJ-CtSsSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Ct  u0 {1,S}
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
    index = 363,
    label = "CsJ-CbSsSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cb  u0 {1,S}
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
    index = 364,
    label = "CsJ-CdSsSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
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
    index = 365,
    label = "CsJ-C=SSsSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CS  u0 {1,S} {5,D}
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
    index = 366,
    label = "CsJ-SsSsSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   S2s u0 {1,S}
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
    index = 367,
    label = "CCsJOS",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   O2s u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = 'CCsJOHSH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 368,
    label = "CCsJOHSH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   S2s u0 {1,S} {6,S}
4   C   u0 {1,S}
5   H   u0 {2,S}
6   H   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.21,-2.38,-2.47,-2.55,-2.89,-3.33,-4.54],'cal/(mol*K)'),
        H298 = (92.6,'kcal/mol'),
        S298 = (1.67,'cal/(mol*K)'),
    ),
    shortDesc = """CAC CBS-QB3 1d-hr""",
    longDesc = 
"""

""",
)

entry(
    index = 369,
    label = "CsJ-SsOsH",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   S  ux {1,S}
3   O  ux {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.95,-2.6,-2.88,-2.9,-2.72,-2.63,-3.06],'cal/(mol*K)'),
        H298 = (96.64,'kcal/mol'),
        S298 = (-0.74,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 370,
    label = "OCJO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S}
3   O2s u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1,-8.2,-14.4,-17.5,-19.4,-20.1,-21.5],'J/(mol*K)'),
        H298 = (408.4,'kJ/mol'),
        S298 = (15.1,'J/(mol*K)'),
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
    index = 371,
    label = "CsJ-HNN",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   N  u0 {1,S}
3   N  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.8532,11.0458,6.19232,1.63176,-4.64424,-8.53536,-15.9829],'J/(mol*K)'),
        H298 = (438.663,'kJ/mol'),
        S298 = (7.12357,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 372,
    label = "CsJ-HNN3ds",
    group = 
"""
1 * Cs        u1 {2,S} {3,S} {4,S}
2   N         u0 {1,S}
3   [N3d,N3s] u0 {1,S}
4   H         u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.58597,-5.80395,-8.7662,-11.0768,-14.324,-16.3676,-18.708],'J/(mol*K)'),
        H298 = (393.258,'kJ/mol'),
        S298 = (0.575878,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 373,
    label = "CsJ-HN(N3dCd)",
    group = 
"""
1 * Cs       u1 {2,S} {3,S} {4,S}
2   N3d      u0 {1,S} {5,D}
3   N        u0 {1,S}
4   H        u0 {1,S}
5   [Cd,Cdd] u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.17364,0.526339,-1.56312,-4.04119,-8.28715,-11.0029,-15.4736],'J/(mol*K)'),
        H298 = (342.422,'kJ/mol'),
        S298 = (-4.66094,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 374,
    label = "CsJ-HN(N3dOd)",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   N3d u0 {1,S} {5,D}
3   N   u0 {1,S}
4   H   u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.31137,-4.08151,-5.05929,-6.59864,-9.61356,-12.7552,-18.2312],'J/(mol*K)'),
        H298 = (303.519,'kJ/mol'),
        S298 = (-8.01983,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 375,
    label = "CsJ-HN(N3dN5dc)",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   N3d  u0 {1,S} {5,D}
3   N    u0 {1,S}
4   H    u0 {1,S}
5   N5dc u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.95318,3.13485,0.33421,-2.701,-7.67123,-10.5415,-15.8149],'J/(mol*K)'),
        H298 = (275.434,'kJ/mol'),
        S298 = (4.69758,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 376,
    label = "CsJ-HN5scN5sc",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   N5sc u0 {1,S}
3   N5sc u0 {1,S}
4   H    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0538838,-1.876,-4.04855,-6.08546,-9.70524,-12.7382,-17.9892],'J/(mol*K)'),
        H298 = (436.377,'kJ/mol'),
        S298 = (7.19164,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 377,
    label = "CsJ-NNN",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   N  u0 {1,S}
3   N  u0 {1,S}
4   N  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.26669,-1.87614,-5.88538,-8.95583,-13.0988,-15.6997,-18.3991],'J/(mol*K)'),
        H298 = (388.334,'kJ/mol'),
        S298 = (-4.02418,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 378,
    label = "CsJ-HNO",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   O  u0 {1,S}
3   N  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.29692,-8.29409,-11.2699,-13.4031,-16.5816,-18.4631,-19.9014],'J/(mol*K)'),
        H298 = (371.563,'kJ/mol'),
        S298 = (2.01997,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 379,
    label = "CsJ-HON1sc",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   O    u0 {1,S}
3   N1sc u0 {1,S}
4   H    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80826,-12.344,-15.0884,-16.9587,-18.722,-18.5848,-14.5979],'J/(mol*K)'),
        H298 = (273.333,'kJ/mol'),
        S298 = (-3.14275,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 380,
    label = "CsJ-NNO",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   O  u0 {1,S}
3   N  u0 {1,S}
4   N  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.60436,-6.81991,-9.0924,-11.5084,-13.7941,-14.5737,-13.827],'J/(mol*K)'),
        H298 = (311.145,'kJ/mol'),
        S298 = (4.53151,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 381,
    label = "CsJ-NOO",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   O  u0 {1,S}
3   O  u0 {1,S}
4   N  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.42994,-4.90751,-5.57809,-6.41818,-8.08512,-9.63419,-13.0091],'J/(mol*K)'),
        H298 = (324.92,'kJ/mol'),
        S298 = (-3.22872,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 382,
    label = "CsJ-CNN",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   C  u0 {1,S}
3   N  u0 {1,S}
4   N  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.80085,-5.80744,-7.57663,-9.14825,-11.7549,-13.7367,-16.6315],'J/(mol*K)'),
        H298 = (383.839,'kJ/mol'),
        S298 = (-5.21955,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 383,
    label = "CsJ-CNO",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   C  u0 {1,S}
3   O  u0 {1,S}
4   N  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.889156,-3.17426,-6.57797,-9.40356,-13.6201,-16.3703,-19.6483],'J/(mol*K)'),
        H298 = (390.332,'kJ/mol'),
        S298 = (4.50509,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 384,
    label = "CsJN",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   N  u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = 'CCsJN',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 385,
    label = "CsJN3s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   N3s u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.34639,0.0642418,-2.22164,-4.63062,-8.66372,-11.6685,-16.1145],'J/(mol*K)'),
        H298 = (388.92,'kJ/mol'),
        S298 = (-10.2036,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 386,
    label = "CsJN5sdtc",
    group = 
"""
1 * Cs                     u1 {2,S} {3,S} {4,S}
2   [N5sc,N5dc,N5ddc,N5tc] u0 {1,S}
3   H                      u0 {1,S}
4   H                      u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.81722,3.24544,2.72474,1.22104,-2.23308,-5.66919,-12.8356],'J/(mol*K)'),
        H298 = (404.243,'kJ/mol'),
        S298 = (-14.4918,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 387,
    label = "CsJN5sc",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   N5sc u0 {1,S}
3   H    u0 {1,S}
4   H    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.491933,-0.720255,-2.86803,-5.09749,-8.94641,-12.0652,-17.2889],'J/(mol*K)'),
        H298 = (432.825,'kJ/mol'),
        S298 = (-2.63962,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 388,
    label = "CsJN5dcOdO0sc",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   N5dc u0 {1,S} {5,D} {6,S}
3   H    u0 {1,S}
4   H    u0 {1,S}
5   O2d  u0 {2,D}
6   O0sc u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.05016,0.29288,-2.17568,-4.97896,-10.1671,-14.393,-21.2966],'J/(mol*K)'),
        H298 = (424.73,'kJ/mol'),
        S298 = (-14.8665,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 389,
    label = "CsJN5dcN3dO0sc",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   N5dc u0 {1,S} {5,D} {6,S}
3   H    u0 {1,S}
4   H    u0 {1,S}
5   N3d  u0 {2,D}
6   O0sc u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.27482,3.34223,2.42357,0.716726,-3.09483,-6.83265,-14.3794],'J/(mol*K)'),
        H298 = (421.503,'kJ/mol'),
        S298 = (-9.69349,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 390,
    label = "CsJN3dCd",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   N3d u0 {1,S} {5,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   Cd  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.334539,-0.181647,-0.845982,-1.98298,-4.81941,-7.87964,-14.2395],'J/(mol*K)'),
        H298 = (374.018,'kJ/mol'),
        S298 = (-11.1917,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 391,
    label = "CsJN3dCdd",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   N3d u0 {1,S} {5,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   Cdd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.55707,4.38485,1.99807,-0.696803,-5.27072,-8.57746,-14.1022],'J/(mol*K)'),
        H298 = (389.255,'kJ/mol'),
        S298 = (-9.12797,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 392,
    label = "CsJN3dN5dc",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   N3d  u0 {1,S} {5,D}
3   H    u0 {1,S}
4   H    u0 {1,S}
5   N5dc u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.315332,0.568578,-0.652395,-2.70945,-6.57117,-9.32981,-14.8325],'J/(mol*K)'),
        H298 = (331.765,'kJ/mol'),
        S298 = (-9.5881,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 393,
    label = "CCsJN",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   N  u0 {1,S}
3   C  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.2,-0.7,-1.4,-1.9,-2.8,-3.4,-4.5],'cal/(mol*K)'),
        H298 = (92.1,'kcal/mol'),
        S298 = (2.5,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 394,
    label = "CdCsJN",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   N  u0 {1,S}
3   Cd u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.49236,-8.5813,-8.63032,-9.10002,-10.0385,-11.4238,-14.1214],'J/(mol*K)'),
        H298 = (329.078,'kJ/mol'),
        S298 = (-10.2951,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 395,
    label = "C2CsJN",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   N  u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.4665,-7.70578,-11.17,-13.75,-16.6445,-18.2536,-20.0442],'J/(mol*K)'),
        H298 = (392.461,'kJ/mol'),
        S298 = (-9.03706,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 396,
    label = "CdsJ",
    group = 
"""
1 * [Cd,CO] u1
""",
    thermo = 'Cds_P',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 397,
    label = "CdBr1sCdd",
    group = 
"""
1 * Cd   u1 {2,S} {3,D}
2   Br1s u0 {1,S}
3   Cdd  u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.500795,-1.45715,-2.09245,-2.57767,-3.35609,-3.95866,-4.89919],'cal/(mol*K)','+|-',[0.373589,0.38358,0.359654,0.335925,0.296461,0.259425,0.190009]),
        H298 = (95.3899,'kcal/mol','+|-',0.596805),
        S298 = (-0.245925,'cal/(mol*K)','+|-',1.01424),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:OCDCD[C]Br smiles:OC=C=[C]Br H298:54.70 kcal/mol
library:CHOBr_G4 label:Br[C]DCDCDCBr smiles:Br[C]=C=C=CBr H298:134.65 kcal/mol
library:CHOBr_G4 label:CDCDCD[C]Br smiles:C=C=C=[C]Br H298:129.92 kcal/mol
library:CHOBr_G4 label:Br[C]DCDCCBr smiles:Br[C]=C=CCBr H298:91.40 kcal/mol
library:CHOBr_G4 label:ODCD[C]Br smiles:O=C=[C]Br H298:53.55 kcal/mol
library:CHOBr_G4 label:OC(Br)DCD[C]Br smiles:OC(Br)=C=[C]Br H298:61.22 kcal/mol
library:CHOBr_G4 label:ODCDCD[C]Br smiles:O=C=C=[C]Br H298:74.61 kcal/mol
""",
)

entry(
    index = 398,
    label = "CdCddCl1s",
    group = 
"""
1 * Cd   u1 {2,S} {3,D}
2   Cl1s u0 {1,S}
3   Cdd  u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.138551,-0.966398,-1.61384,-2.17883,-3.08606,-3.72396,-4.5964],'cal/(mol*K)','+|-',[0.312567,0.320926,0.300908,0.281055,0.248037,0.217051,0.158973]),
        H298 = (95.1673,'kcal/mol','+|-',0.499323),
        S298 = (2.29414,'cal/(mol*K)','+|-',0.848578),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOCl_G4 label:Cl[C]DCDCDCCl smiles:Cl[C]=C=C=CCl H298:113.22 kcal/mol
library:CHOCl_G4 label:OC(Cl)DCD[C]Cl smiles:OC(Cl)=C=[C]Cl H298:38.02 kcal/mol
library:CHOCl_G4 label:ODCDCD[C]Cl smiles:O=C=C=[C]Cl H298:63.49 kcal/mol
library:CHOCl_G4 label:ODCD[C]Cl smiles:O=C=[C]Cl H298:39.72 kcal/mol
library:CHOCl_G4 label:CDCDCD[C]Cl smiles:C=C=C=[C]Cl H298:119.05 kcal/mol
library:CHOCl_G4 label:Cl[C]DCDCDC(Cl)Cl smiles:Cl[C]=C=C=C(Cl)Cl H298:109.57 kcal/mol
library:CHOCl_G4 label:OCDCD[C]Cl smiles:OC=C=[C]Cl H298:43.83 kcal/mol
library:CHOClBr_G4 label:Cl[C]DCDCDC(Cl)Br smiles:Cl[C]=C=C=C(Cl)Br H298:120.42 kcal/mol
library:CHOClBr_G4 label:OC(Br)DCD[C]Cl smiles:OC(Br)=C=[C]Cl H298:49.91 kcal/mol
library:CHOClBr_G4 label:Cl[C]DCDC(Cl)CBr smiles:Cl[C]=C=C(Cl)CBr H298:72.97 kcal/mol
""",
)

entry(
    index = 399,
    label = "CdCddF1s",
    group = 
"""
1 * Cd  u1 {2,S} {3,D}
2   F1s u0 {1,S}
3   Cdd u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.420021,-1.06908,-1.66887,-2.18795,-2.99319,-3.55053,-4.3308],'cal/(mol*K)','+|-',[0.232974,0.239204,0.224283,0.209486,0.184876,0.16178,0.118491]),
        H298 = (103.204,'kcal/mol','+|-',0.372173),
        S298 = (1.35765,'cal/(mol*K)','+|-',0.632492),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:F[C]DCDC(F)F smiles:F[C]=C=C(F)F H298:-32.16 kcal/mol
library:CHOF_G4 label:F[C]DCDCDC(F)F smiles:F[C]=C=C=C(F)F H298:4.94 kcal/mol
library:CHOF_G4 label:CDCDCD[C]F smiles:C=C=C=[C]F H298:89.93 kcal/mol
library:CHOF_G4 label:CC(F)DCD[C]F smiles:CC(F)=C=[C]F H298:2.14 kcal/mol
library:CHOF_G4 label:F[C]DCDCC(F)(F)F smiles:F[C]=C=CC(F)(F)F H298:-104.59 kcal/mol
library:CHOF_G4 label:OC(F)DCD[C]F smiles:OC(F)=C=[C]F H298:-31.85 kcal/mol
library:CHOF_G4 label:ODCDCD[C]F smiles:O=C=C=[C]F H298:29.19 kcal/mol
library:CHOF_G4 label:ODCD[C]F smiles:O=C=[C]F H298:11.09 kcal/mol
library:CHOF_G4 label:OCDCD[C]F smiles:OC=C=[C]F H298:14.90 kcal/mol
library:CHOFCl_G4 label:F[C]DCDCDC(F)Cl smiles:F[C]=C=C=C(F)Cl H298:44.80 kcal/mol
library:CHOFCl_G4 label:F[C]DCDCDCCl smiles:F[C]=C=C=CCl H298:86.89 kcal/mol
library:CHOFCl_G4 label:F[C]DCDC(Cl)OCl smiles:F[C]=C=C(Cl)OCl H298:48.07 kcal/mol
library:CHOFCl_G4 label:F[C]DCDCOCl smiles:F[C]=C=COCl H298:52.59 kcal/mol
library:CHOFCl_G4 label:F[C]DCDC(F)OCl smiles:F[C]=C=C(F)OCl H298:8.95 kcal/mol
library:CHOFCl_G4 label:OC(Cl)DCD[C]F smiles:OC(Cl)=C=[C]F H298:9.17 kcal/mol
library:CHOFClBr_G4 label:F[C]DCDCDC(Cl)Br smiles:F[C]=C=C=C(Cl)Br H298:94.93 kcal/mol
library:CHOFBr_G4 label:F[C]DCDCOBr smiles:F[C]=C=COBr H298:55.02 kcal/mol
library:CHOFBr_G4 label:OC(Br)DCD[C]F smiles:OC(Br)=C=[C]F H298:21.63 kcal/mol
""",
)

entry(
    index = 400,
    label = "CdBr1sCd",
    group = 
"""
1 * Cd   u1 {2,S} {3,D}
2   Br1s u0 {1,S}
3   Cd   u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.223916,-0.944778,-1.6301,-2.2287,-3.14045,-3.76793,-4.68754],'cal/(mol*K)','+|-',[0.132084,0.135616,0.127157,0.118768,0.104815,0.0917207,0.0671782]),
        H298 = (108.532,'kcal/mol','+|-',0.211002),
        S298 = (1.41173,'cal/(mol*K)','+|-',0.35859),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:CDCCD[C]Br smiles:C=CC=[C]Br H298:87.95 kcal/mol
library:CHOBr_G4 label:CC(Br)C(Br)D[C]Br smiles:CC(Br)C(Br)=[C]Br H298:67.12 kcal/mol
library:CHOBr_G4 label:Br[C]DC(Br)OBr smiles:Br[C]=C(Br)OBr H298:80.08 kcal/mol
library:CHOBr_G4 label:OC(O)D[C]Br smiles:OC(O)=[C]Br H298:-6.38 kcal/mol
library:CHOBr_G4 label:Br[C]DC(Br)CDCBr smiles:Br[C]=C(Br)C=CBr H298:98.01 kcal/mol
library:CHOBr_G4 label:OCC(Br)D[C]Br smiles:OCC(Br)=[C]Br H298:33.84 kcal/mol
library:CHOBr_G4 label:CC(C)D[C]Br smiles:CC(C)=[C]Br H298:56.37 kcal/mol
library:CHOBr_G4 label:CC(D[C]Br)CBr smiles:CC(=[C]Br)CBr H298:61.66 kcal/mol
library:CHOBr_G4 label:ODC(Br)CD[C]Br smiles:O=C(Br)C=[C]Br H298:42.13 kcal/mol
library:CHOBr_G4 label:Br[C]DCOC(Br)Br smiles:Br[C]=COC(Br)Br H298:51.13 kcal/mol
library:CHOBr_G4 label:Br[C]DCC(Br)OBr smiles:Br[C]=CC(Br)OBr H298:70.99 kcal/mol
library:CHOBr_G4 label:CDCC(Br)D[C]Br smiles:C=CC(Br)=[C]Br H298:92.33 kcal/mol
library:CHOBr_G4 label:Br[C]DC(Br)Br smiles:Br[C]=C(Br)Br H298:87.72 kcal/mol
library:CHOBr_G4 label:Br[C]DC(OBr)OBr smiles:Br[C]=C(OBr)OBr H298:74.26 kcal/mol
library:CHOBr_G4 label:OC(Br)D[C]Br smiles:OC(Br)=[C]Br H298:41.50 kcal/mol
library:CHOBr_G4 label:Br[C]DC(Br)CCBr smiles:Br[C]=C(Br)CCBr H298:69.47 kcal/mol
library:CHOBr_G4 label:OOC(Br)D[C]Br smiles:OOC(Br)=[C]Br H298:62.77 kcal/mol
library:CHOBr_G4 label:Br[C]DC(Br)OCBr smiles:Br[C]=C(Br)OCBr H298:48.84 kcal/mol
library:CHOBr_G4 label:Br[C]DCOBr smiles:Br[C]=COBr H298:74.51 kcal/mol
library:CHOBr_G4 label:ODCCD[C]Br smiles:O=CC=[C]Br H298:45.04 kcal/mol
library:CHOBr_G4 label:CC(Br)CD[C]Br smiles:CC(Br)C=[C]Br H298:62.59 kcal/mol
library:CHOBr_G4 label:Br[C]DCOCBr smiles:Br[C]=COCBr H298:43.04 kcal/mol
library:CHOBr_G4 label:Br[C]DCCCBr smiles:Br[C]=CCCBr H298:65.33 kcal/mol
library:CHOBr_G4 label:CCCD[C]Br smiles:CCC=[C]Br H298:59.83 kcal/mol
library:CHOBr_G4 label:Br[C]DC(Br)C#CBr smiles:Br[C]=C(Br)C#CBr H298:148.33 kcal/mol
library:CHOBr_G4 label:Br[C]DC(CBr)OBr smiles:Br[C]=C(CBr)OBr H298:73.16 kcal/mol
library:CHOBr_G4 label:OCD[C]Br smiles:OC=[C]Br H298:35.05 kcal/mol
library:CHOBr_G4 label:CC(Br)D[C]Br smiles:CC(Br)=[C]Br H298:68.44 kcal/mol
library:CHOBr_G4 label:OCCD[C]Br smiles:OCC=[C]Br H298:30.64 kcal/mol
library:CHOBr_G4 label:Br[C]DC(CBr)CBr smiles:Br[C]=C(CBr)CBr H298:67.15 kcal/mol
library:CHOBr_G4 label:Br[C]DCCC(Br)Br smiles:Br[C]=CCC(Br)Br H298:71.50 kcal/mol
library:CHOBr_G4 label:Br[C]DCC#CBr smiles:Br[C]=CC#CBr H298:141.93 kcal/mol
library:CHOBr_G4 label:CCC(Br)D[C]Br smiles:CCC(Br)=[C]Br H298:62.82 kcal/mol
library:CHOBr_G4 label:CC(O)D[C]Br smiles:CC(O)=[C]Br H298:23.53 kcal/mol
library:CHOBr_G4 label:Br[C]DCCOBr smiles:Br[C]=CCOBr H298:67.30 kcal/mol
library:CHOBr_G4 label:OC(D[C]Br)CBr smiles:OC(=[C]Br)CBr H298:31.24 kcal/mol
library:CHOBr_G4 label:Br[C]DCBr smiles:Br[C]=CBr H298:78.82 kcal/mol
library:CHOBr_G4 label:C#CC(Br)D[C]Br smiles:C#CC(Br)=[C]Br H298:137.92 kcal/mol
library:CHOBr_G4 label:C#CCD[C]Br smiles:C#CC=[C]Br H298:131.36 kcal/mol
library:CHOBr_G4 label:Br[C]DCCBr smiles:Br[C]=CCBr H298:71.49 kcal/mol
library:CHOBr_G4 label:Br[C]DC(Br)OOBr smiles:Br[C]=C(Br)OOBr H298:97.09 kcal/mol
library:CHOBr_G4 label:Br[C]DCC(Br)Br smiles:Br[C]=CC(Br)Br H298:78.72 kcal/mol
library:CHOBr_G4 label:Br[C]DC(Br)COBr smiles:Br[C]=C(Br)COBr H298:70.59 kcal/mol
library:CHOBr_G4 label:OOCD[C]Br smiles:OOC=[C]Br H298:57.34 kcal/mol
library:CHOBr_G4 label:ODCC(Br)D[C]Br smiles:O=CC(Br)=[C]Br H298:50.72 kcal/mol
library:CHOBr_G4 label:CCD[C]Br smiles:CC=[C]Br H298:65.16 kcal/mol
library:CHOBr_G4 label:CDC(Br)CD[C]Br smiles:C=C(Br)C=[C]Br H298:92.91 kcal/mol
library:CHOBr_G4 label:OC(Br)CD[C]Br smiles:OC(Br)C=[C]Br H298:32.40 kcal/mol
library:CHOBr_G4 label:CC(D[C]Br)OBr smiles:CC(=[C]Br)OBr H298:62.39 kcal/mol
library:CHOBr_G4 label:COCD[C]Br smiles:COC=[C]Br H298:41.22 kcal/mol
library:CHOBr_G4 label:CC(Br)(Br)CD[C]Br smiles:CC(Br)(Br)C=[C]Br H298:68.76 kcal/mol
library:CHOBr_G4 label:COC(Br)D[C]Br smiles:COC(Br)=[C]Br H298:43.76 kcal/mol
library:CHOBr_G4 label:Br[C]DC(Br)CBr smiles:Br[C]=C(Br)CBr H298:75.83 kcal/mol
library:CHOBr_G4 label:Br[C]DCCDCBr smiles:Br[C]=CC=CBr H298:92.76 kcal/mol
library:CHOBr_G4 label:CD[C]Br smiles:C=[C]Br H298:72.97 kcal/mol
library:CHOBr_G4 label:CC(D[C]Br)C(Br)Br smiles:CC(=[C]Br)C(Br)Br H298:68.45 kcal/mol
""",
)

entry(
    index = 401,
    label = "CdCdCl1s",
    group = 
"""
1 * Cd   u1 {2,S} {3,D}
2   Cl1s u0 {1,S}
3   Cd   u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.361032,-1.11363,-1.76098,-2.31345,-3.1642,-3.76063,-4.63429],'cal/(mol*K)','+|-',[0.0730664,0.0750205,0.0703409,0.0657001,0.0579817,0.0507383,0.0371618]),
        H298 = (108.792,'kcal/mol','+|-',0.116723),
        S298 = (1.70863,'cal/(mol*K)','+|-',0.198365),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOCl_G4 label:CD[C]Cl smiles:C=[C]Cl H298:61.11 kcal/mol
library:CHOCl_G4 label:OOC(Cl)D[C]Cl smiles:OOC(Cl)=[C]Cl H298:40.11 kcal/mol
library:CHOCl_G4 label:Cl[C]DC(Cl)C(Cl)DCCl smiles:Cl[C]=C(Cl)C(Cl)=CCl H298:59.19 kcal/mol
library:CHOCl_G4 label:COCD[C]Cl smiles:COC=[C]Cl H298:29.97 kcal/mol
library:CHOCl_G4 label:Cl[C]DC(Cl)C(Cl)(Cl)Cl smiles:Cl[C]=C(Cl)C(Cl)(Cl)Cl H298:38.52 kcal/mol
library:CHOCl_G4 label:Cl[C]DCC(Cl)(Cl)C(Cl)Cl smiles:Cl[C]=CC(Cl)(Cl)C(Cl)Cl H298:28.24 kcal/mol
library:CHOCl_G4 label:CCD[C]Cl smiles:CC=[C]Cl H298:53.65 kcal/mol
library:CHOCl_G4 label:OC(D[C]Cl)CCl smiles:OC(=[C]Cl)CCl H298:9.52 kcal/mol
library:CHOCl_G4 label:CC(Cl)D[C]Cl smiles:CC(Cl)=[C]Cl H298:46.43 kcal/mol
library:CHOCl_G4 label:Cl[C]DCOCl smiles:Cl[C]=COCl H298:61.08 kcal/mol
library:CHOCl_G4 label:OC(Cl)(Cl)CD[C]Cl smiles:OC(Cl)(Cl)C=[C]Cl H298:2.85 kcal/mol
library:CHOCl_G4 label:Cl[C]DC(Cl)C(Cl)(Cl)C(Cl)Cl smiles:Cl[C]=C(Cl)C(Cl)(Cl)C(Cl)Cl H298:24.65 kcal/mol
library:CHOCl_G4 label:Cl[C]DCC(Cl)CCl smiles:Cl[C]=CC(Cl)CCl H298:35.30 kcal/mol
library:CHOCl_G4 label:OOCD[C]Cl smiles:OOC=[C]Cl H298:46.01 kcal/mol
library:CHOCl_G4 label:CC(Cl)CD[C]Cl smiles:CC(Cl)C=[C]Cl H298:40.19 kcal/mol
library:CHOCl_G4 label:Cl[C]DC(Cl)C(Cl)C(Cl)Cl smiles:Cl[C]=C(Cl)C(Cl)C(Cl)Cl H298:27.12 kcal/mol
library:CHOCl_G4 label:Cl[C]DCC(Cl)(Cl)CCl smiles:Cl[C]=CC(Cl)(Cl)CCl H298:32.46 kcal/mol
library:CHOCl_G4 label:Cl[C]DC(Cl)Cl smiles:Cl[C]=C(Cl)Cl H298:54.55 kcal/mol
library:CHOCl_G4 label:Cl[C]DC(Cl)COCl smiles:Cl[C]=C(Cl)COCl H298:45.75 kcal/mol
library:CHOCl_G4 label:Cl[C]DC(Cl)OOCl smiles:Cl[C]=C(Cl)OOCl H298:71.55 kcal/mol
library:CHOCl_G4 label:ODC(Cl)CD[C]Cl smiles:O=C(Cl)C=[C]Cl H298:17.96 kcal/mol
library:CHOCl_G4 label:Cl[C]DC(Cl)C(Cl)Cl smiles:Cl[C]=C(Cl)C(Cl)Cl H298:39.77 kcal/mol
library:CHOCl_G4 label:Cl[C]DC(Cl)OCl smiles:Cl[C]=C(Cl)OCl H298:57.11 kcal/mol
library:CHOCl_G4 label:C#CCD[C]Cl smiles:C#CC=[C]Cl H298:119.66 kcal/mol
library:CHOCl_G4 label:ODC(Cl)C(Cl)D[C]Cl smiles:O=C(Cl)C(Cl)=[C]Cl H298:14.46 kcal/mol
library:CHOCl_G4 label:Cl[C]DC(OCl)C(Cl)Cl smiles:Cl[C]=C(OCl)C(Cl)Cl H298:44.24 kcal/mol
library:CHOCl_G4 label:CC(O)D[C]Cl smiles:CC(O)=[C]Cl H298:12.60 kcal/mol
library:CHOCl_G4 label:OCC(Cl)D[C]Cl smiles:OCC(Cl)=[C]Cl H298:12.05 kcal/mol
library:CHOCl_G4 label:CC(Cl)(Cl)CD[C]Cl smiles:CC(Cl)(Cl)C=[C]Cl H298:34.21 kcal/mol
library:CHOCl_G4 label:CDCC(Cl)D[C]Cl smiles:C=CC(Cl)=[C]Cl H298:70.17 kcal/mol
library:CHOCl_G4 label:Cl[C]DCC(Cl)C(Cl)Cl smiles:Cl[C]=CC(Cl)C(Cl)Cl H298:31.07 kcal/mol
library:CHOCl_G4 label:Cl[C]DC(Cl)C(Cl)(Cl)CCl smiles:Cl[C]=C(Cl)C(Cl)(Cl)CCl H298:25.07 kcal/mol
library:CHOCl_G4 label:Cl[C]DC(Cl)C(Cl)OCl smiles:Cl[C]=C(Cl)C(Cl)OCl H298:39.21 kcal/mol
library:CHOCl_G4 label:Cl[C]DC(CCl)CCl smiles:Cl[C]=C(CCl)CCl H298:34.57 kcal/mol
library:CHOCl_G4 label:Cl[C]DCCDC(Cl)Cl smiles:Cl[C]=CC=C(Cl)Cl H298:64.71 kcal/mol
library:CHOCl_G4 label:CC(D[C]Cl)OCl smiles:CC(=[C]Cl)OCl H298:51.58 kcal/mol
library:CHOCl_G4 label:Cl[C]DC(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:Cl[C]=C(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:24.57 kcal/mol
library:CHOCl_G4 label:Cl[C]DCCC(Cl)Cl smiles:Cl[C]=CCC(Cl)Cl H298:36.43 kcal/mol
library:CHOCl_G4 label:Cl[C]DC(Cl)OC(Cl)Cl smiles:Cl[C]=C(Cl)OC(Cl)Cl H298:11.30 kcal/mol
library:CHOCl_G4 label:OC(Cl)D[C]Cl smiles:OC(Cl)=[C]Cl H298:18.79 kcal/mol
library:CHOCl_G4 label:Cl[C]DCCCCl smiles:Cl[C]=CCCCl H298:42.77 kcal/mol
library:CHOCl_G4 label:Cl[C]DC(CCl)C(Cl)(Cl)Cl smiles:Cl[C]=C(CCl)C(Cl)(Cl)Cl H298:30.13 kcal/mol
library:CHOCl_G4 label:Cl[C]DCOCCl smiles:Cl[C]=COCCl H298:20.28 kcal/mol
library:CHOCl_G4 label:OCCD[C]Cl smiles:OCC=[C]Cl H298:19.17 kcal/mol
library:CHOCl_G4 label:OC(Cl)CD[C]Cl smiles:OC(Cl)C=[C]Cl H298:9.02 kcal/mol
library:CHOCl_G4 label:Cl[C]DCOOCl smiles:Cl[C]=COOCl H298:77.11 kcal/mol
library:CHOCl_G4 label:Cl[C]DC(Cl)CDCCl smiles:Cl[C]=C(Cl)C=CCl H298:64.11 kcal/mol
library:CHOCl_G4 label:Cl[C]DCCOCl smiles:Cl[C]=CCOCl H298:52.22 kcal/mol
library:CHOCl_G4 label:CC(Cl)C(Cl)D[C]Cl smiles:CC(Cl)C(Cl)=[C]Cl H298:34.39 kcal/mol
library:CHOCl_G4 label:OC(D[C]Cl)C(Cl)Cl smiles:OC(=[C]Cl)C(Cl)Cl H298:6.15 kcal/mol
library:CHOCl_G4 label:OCD[C]Cl smiles:OC=[C]Cl H298:23.96 kcal/mol
library:CHOCl_G4 label:CC(D[C]Cl)CCl smiles:CC(=[C]Cl)CCl H298:39.59 kcal/mol
library:CHOCl_G4 label:Cl[C]DCC(Cl)(Cl)Cl smiles:Cl[C]=CC(Cl)(Cl)Cl H298:43.01 kcal/mol
library:CHOCl_G4 label:CC(D[C]Cl)C(Cl)(Cl)Cl smiles:CC(=[C]Cl)C(Cl)(Cl)Cl H298:32.86 kcal/mol
library:CHOCl_G4 label:Cl[C]DC(Cl)C(Cl)CCl smiles:Cl[C]=C(Cl)C(Cl)CCl H298:30.21 kcal/mol
library:CHOCl_G4 label:Cl[C]DC(CCl)OCl smiles:Cl[C]=C(CCl)OCl H298:46.67 kcal/mol
library:CHOCl_G4 label:Cl[C]DC(OCl)C(Cl)(Cl)Cl smiles:Cl[C]=C(OCl)C(Cl)(Cl)Cl H298:44.04 kcal/mol
library:CHOCl_G4 label:ODCC(Cl)D[C]Cl smiles:O=CC(Cl)=[C]Cl H298:28.84 kcal/mol
library:CHOCl_G4 label:Cl[C]DC(Cl)C(Cl)(Cl)OCl smiles:Cl[C]=C(Cl)C(Cl)(Cl)OCl H298:35.32 kcal/mol
library:CHOCl_G4 label:Cl[C]DC(C(Cl)Cl)C(Cl)(Cl)Cl smiles:Cl[C]=C(C(Cl)Cl)C(Cl)(Cl)Cl H298:26.91 kcal/mol
library:CHOCl_G4 label:OC(Cl)(Cl)C(Cl)D[C]Cl smiles:OC(Cl)(Cl)C(Cl)=[C]Cl H298:-1.87 kcal/mol
library:CHOCl_G4 label:CCCD[C]Cl smiles:CCC=[C]Cl H298:48.44 kcal/mol
library:CHOCl_G4 label:ODCCD[C]Cl smiles:O=CC=[C]Cl H298:33.36 kcal/mol
library:CHOCl_G4 label:Cl[C]DC(C(Cl)Cl)C(Cl)Cl smiles:Cl[C]=C(C(Cl)Cl)C(Cl)Cl H298:28.17 kcal/mol
library:CHOCl_G4 label:CDC(Cl)C(Cl)D[C]Cl smiles:C=C(Cl)C(Cl)=[C]Cl H298:64.07 kcal/mol
library:CHOCl_G4 label:Cl[C]DC(Cl)OC(Cl)(Cl)Cl smiles:Cl[C]=C(Cl)OC(Cl)(Cl)Cl H298:9.89 kcal/mol
library:CHOCl_G4 label:Cl[C]DC(Cl)CCl smiles:Cl[C]=C(Cl)CCl H298:43.15 kcal/mol
library:CHOCl_G4 label:Cl[C]DC(Cl)OCCl smiles:Cl[C]=C(Cl)OCCl H298:14.94 kcal/mol
library:CHOCl_G4 label:Cl[C]DCCC(Cl)(Cl)Cl smiles:Cl[C]=CCC(Cl)(Cl)Cl H298:32.80 kcal/mol
library:CHOCl_G4 label:CDC(Cl)CD[C]Cl smiles:C=C(Cl)C=[C]Cl H298:69.41 kcal/mol
library:CHOCl_G4 label:COC(Cl)D[C]Cl smiles:COC(Cl)=[C]Cl H298:21.28 kcal/mol
library:CHOCl_G4 label:Cl[C]DCC(Cl)DCCl smiles:Cl[C]=CC(Cl)=CCl H298:64.14 kcal/mol
library:CHOCl_G4 label:Cl[C]DCCDCCl smiles:Cl[C]=CC=CCl H298:69.26 kcal/mol
library:CHOCl_G4 label:Cl[C]DC(Cl)CCCl smiles:Cl[C]=C(Cl)CCCl H298:35.02 kcal/mol
library:CHOCl_G4 label:Cl[C]DCOC(Cl)Cl smiles:Cl[C]=COC(Cl)Cl H298:15.51 kcal/mol
library:CHOCl_G4 label:Cl[C]DCC(Cl)(Cl)OCl smiles:Cl[C]=CC(Cl)(Cl)OCl H298:40.90 kcal/mol
library:CHOCl_G4 label:Cl[C]DC(Cl)CC(Cl)Cl smiles:Cl[C]=C(Cl)CC(Cl)Cl H298:29.66 kcal/mol
library:CHOCl_G4 label:Cl[C]DCC(Cl)C(Cl)(Cl)Cl smiles:Cl[C]=CC(Cl)C(Cl)(Cl)Cl H298:28.64 kcal/mol
library:CHOCl_G4 label:Cl[C]DC(OCl)OCl smiles:Cl[C]=C(OCl)OCl H298:58.00 kcal/mol
library:CHOCl_G4 label:Cl[C]DCC(Cl)OCl smiles:Cl[C]=CC(Cl)OCl H298:43.79 kcal/mol
library:CHOCl_G4 label:Cl[C]DC(Cl)C#CCl smiles:Cl[C]=C(Cl)C#CCl H298:115.67 kcal/mol
library:CHOCl_G4 label:Cl[C]DCCCl smiles:Cl[C]=CCCl H298:49.22 kcal/mol
library:CHOCl_G4 label:Cl[C]DC(Cl)CDC(Cl)Cl smiles:Cl[C]=C(Cl)C=C(Cl)Cl H298:61.65 kcal/mol
library:CHOCl_G4 label:OC(D[C]Cl)OCl smiles:OC(=[C]Cl)OCl H298:21.38 kcal/mol
library:CHOCl_G4 label:CC(Cl)(Cl)C(Cl)D[C]Cl smiles:CC(Cl)(Cl)C(Cl)=[C]Cl H298:29.25 kcal/mol
library:CHOCl_G4 label:Cl[C]DCC(Cl)(Cl)C(Cl)(Cl)Cl smiles:Cl[C]=CC(Cl)(Cl)C(Cl)(Cl)Cl H298:27.40 kcal/mol
library:CHOCl_G4 label:Cl[C]DCCl smiles:Cl[C]=CCl H298:56.78 kcal/mol
library:CHOCl_G4 label:C#CC(Cl)D[C]Cl smiles:C#CC(Cl)=[C]Cl H298:116.11 kcal/mol
library:CHOCl_G4 label:Cl[C]DC(Cl)CC(Cl)(Cl)Cl smiles:Cl[C]=C(Cl)CC(Cl)(Cl)Cl H298:28.14 kcal/mol
library:CHOCl_G4 label:Cl[C]DCC(Cl)Cl smiles:Cl[C]=CC(Cl)Cl H298:44.66 kcal/mol
library:CHOCl_G4 label:Cl[C]DCC#CCl smiles:Cl[C]=CC#CCl H298:119.39 kcal/mol
library:CHOCl_G4 label:Cl[C]DCOC(Cl)(Cl)Cl smiles:Cl[C]=COC(Cl)(Cl)Cl H298:14.98 kcal/mol
library:CHOCl_G4 label:CC(C)D[C]Cl smiles:CC(C)=[C]Cl H298:45.02 kcal/mol
library:CHOCl_G4 label:CCC(Cl)D[C]Cl smiles:CCC(Cl)=[C]Cl H298:41.02 kcal/mol
library:CHOCl_G4 label:OC(D[C]Cl)C(Cl)(Cl)Cl smiles:OC(=[C]Cl)C(Cl)(Cl)Cl H298:4.94 kcal/mol
library:CHOCl_G4 label:Cl[C]DC(Cl)C(Cl)C(Cl)(Cl)Cl smiles:Cl[C]=C(Cl)C(Cl)C(Cl)(Cl)Cl H298:27.19 kcal/mol
library:CHOCl_G4 label:OC(Cl)C(Cl)D[C]Cl smiles:OC(Cl)C(Cl)=[C]Cl H298:2.48 kcal/mol
library:CHOCl_G4 label:Cl[C]DC(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:Cl[C]=C(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:31.84 kcal/mol
library:CHOCl_G4 label:OC(O)D[C]Cl smiles:OC(O)=[C]Cl H298:-17.15 kcal/mol
library:CHOCl_G4 label:Cl[C]DC(CCl)C(Cl)Cl smiles:Cl[C]=C(CCl)C(Cl)Cl H298:31.61 kcal/mol
library:CHOCl_G4 label:CC(D[C]Cl)C(Cl)Cl smiles:CC(=[C]Cl)C(Cl)Cl H298:34.44 kcal/mol
library:CHOCl_G4 label:CDCCD[C]Cl smiles:C=CC=[C]Cl H298:76.43 kcal/mol
library:CHOClBr_G4 label:CC(D[C]Cl)C(Cl)Br smiles:CC(=[C]Cl)C(Cl)Br H298:46.13 kcal/mol
library:CHOClBr_G4 label:Cl[C]DCC(Cl)(Br)Br smiles:Cl[C]=CC(Cl)(Br)Br H298:66.54 kcal/mol
library:CHOClBr_G4 label:COC(Br)D[C]Cl smiles:COC(Br)=[C]Cl H298:32.84 kcal/mol
library:CHOClBr_G4 label:CC(Br)(Br)CD[C]Cl smiles:CC(Br)(Br)C=[C]Cl H298:57.33 kcal/mol
library:CHOClBr_G4 label:OC(D[C]Cl)C(Br)Br smiles:OC(=[C]Cl)C(Br)Br H298:28.63 kcal/mol
library:CHOClBr_G4 label:Cl[C]DC(CBr)OBr smiles:Cl[C]=C(CBr)OBr H298:59.23 kcal/mol
library:CHOClBr_G4 label:Cl[C]DCC(Cl)Br smiles:Cl[C]=CC(Cl)Br H298:56.09 kcal/mol
library:CHOClBr_G4 label:Cl[C]DCBr smiles:Cl[C]=CBr H298:67.30 kcal/mol
library:CHOClBr_G4 label:OC(Br)CD[C]Cl smiles:OC(Br)C=[C]Cl H298:21.00 kcal/mol
library:CHOClBr_G4 label:CDC(Br)CD[C]Cl smiles:C=C(Br)C=[C]Cl H298:81.24 kcal/mol
library:CHOClBr_G4 label:OC(D[C]Cl)OBr smiles:OC(=[C]Cl)OBr H298:25.07 kcal/mol
library:CHOClBr_G4 label:Cl[C]DCCBr smiles:Cl[C]=CCBr H298:60.02 kcal/mol
library:CHOClBr_G4 label:ODCC(Br)D[C]Cl smiles:O=CC(Br)=[C]Cl H298:39.19 kcal/mol
library:CHOClBr_G4 label:Cl[C]DCC(Cl)OBr smiles:Cl[C]=CC(Cl)OBr H298:46.62 kcal/mol
library:CHOClBr_G4 label:ODC(Br)C(Br)D[C]Cl smiles:O=C(Br)C(Br)=[C]Cl H298:36.92 kcal/mol
library:CHOClBr_G4 label:Cl[C]DC(OCl)OBr smiles:Cl[C]=C(OCl)OBr H298:60.69 kcal/mol
library:CHOClBr_G4 label:OC(Br)C(Cl)D[C]Cl smiles:OC(Br)C(Cl)=[C]Cl H298:14.33 kcal/mol
library:CHOClBr_G4 label:Cl[C]DC(Br)OCBr smiles:Cl[C]=C(Br)OCBr H298:37.93 kcal/mol
library:CHOClBr_G4 label:Cl[C]DC(Br)CBr smiles:Cl[C]=C(Br)CBr H298:64.48 kcal/mol
library:CHOClBr_G4 label:Cl[C]DC(Br)CCBr smiles:Cl[C]=C(Br)CCBr H298:57.01 kcal/mol
library:CHOClBr_G4 label:Cl[C]DCOC(Cl)Br smiles:Cl[C]=COC(Cl)Br H298:27.69 kcal/mol
library:CHOClBr_G4 label:Cl[C]DCC(Br)DCBr smiles:Cl[C]=CC(Br)=CBr H298:87.09 kcal/mol
library:CHOClBr_G4 label:Cl[C]DCCDCBr smiles:Cl[C]=CC=CBr H298:81.19 kcal/mol
library:CHOClBr_G4 label:Cl[C]DC(Cl)CCBr smiles:Cl[C]=C(Cl)CCBr H298:46.64 kcal/mol
library:CHOClBr_G4 label:Cl[C]DCC(Cl)DCBr smiles:Cl[C]=CC(Cl)=CBr H298:75.80 kcal/mol
library:CHOClBr_G4 label:Cl[C]DC(OBr)OBr smiles:Cl[C]=C(OBr)OBr H298:63.28 kcal/mol
library:CHOClBr_G4 label:Cl[C]DC(Cl)OCBr smiles:Cl[C]=C(Cl)OCBr H298:26.62 kcal/mol
library:CHOClBr_G4 label:Cl[C]DC(Cl)CBr smiles:Cl[C]=C(Cl)CBr H298:53.96 kcal/mol
library:CHOClBr_G4 label:Cl[C]DC(Br)C(Br)Br smiles:Cl[C]=C(Br)C(Br)Br H298:72.75 kcal/mol
library:CHOClBr_G4 label:CC(Br)C(Cl)D[C]Cl smiles:CC(Br)C(Cl)=[C]Cl H298:45.38 kcal/mol
library:CHOClBr_G4 label:Cl[C]DCOC(Br)Br smiles:Cl[C]=COC(Br)Br H298:39.80 kcal/mol
library:CHOClBr_G4 label:Cl[C]DCC(Br)OBr smiles:Cl[C]=CC(Br)OBr H298:59.38 kcal/mol
library:CHOClBr_G4 label:CCC(Br)D[C]Cl smiles:CCC(Br)=[C]Cl H298:51.57 kcal/mol
library:CHOClBr_G4 label:Cl[C]DC(CCl)OBr smiles:Cl[C]=C(CCl)OBr H298:48.73 kcal/mol
library:CHOClBr_G4 label:CC(D[C]Cl)C(Br)Br smiles:CC(=[C]Cl)C(Br)Br H298:57.14 kcal/mol
library:CHOClBr_G4 label:Cl[C]DCC(Cl)(Cl)Br smiles:Cl[C]=CC(Cl)(Cl)Br H298:54.86 kcal/mol
library:CHOClBr_G4 label:CC(D[C]Cl)CBr smiles:CC(=[C]Cl)CBr H298:50.29 kcal/mol
library:CHOClBr_G4 label:Cl[C]DCC(Br)Br smiles:Cl[C]=CC(Br)Br H298:67.36 kcal/mol
library:CHOClBr_G4 label:OC(D[C]Cl)C(Cl)Br smiles:OC(=[C]Cl)C(Cl)Br H298:18.31 kcal/mol
library:CHOClBr_G4 label:OC(Br)(Br)CD[C]Cl smiles:OC(Br)(Br)C=[C]Cl H298:27.04 kcal/mol
library:CHOClBr_G4 label:Cl[C]DCCOBr smiles:Cl[C]=CCOBr H298:55.64 kcal/mol
library:CHOClBr_G4 label:Cl[C]DC(Cl)CDCBr smiles:Cl[C]=C(Cl)C=CBr H298:75.98 kcal/mol
library:CHOClBr_G4 label:CDC(Br)C(Cl)D[C]Cl smiles:C=C(Br)C(Cl)=[C]Cl H298:75.66 kcal/mol
library:CHOClBr_G4 label:Cl[C]DCOCBr smiles:Cl[C]=COCBr H298:31.86 kcal/mol
library:CHOClBr_G4 label:Cl[C]DCCCBr smiles:Cl[C]=CCCBr H298:53.85 kcal/mol
library:CHOClBr_G4 label:Cl[C]DCCC(Cl)Br smiles:Cl[C]=CCC(Cl)Br H298:48.11 kcal/mol
library:CHOClBr_G4 label:OC(Br)C(Br)D[C]Cl smiles:OC(Br)C(Br)=[C]Cl H298:24.67 kcal/mol
library:CHOClBr_G4 label:CC(Br)D[C]Cl smiles:CC(Br)=[C]Cl H298:57.09 kcal/mol
library:CHOClBr_G4 label:CC(D[C]Cl)OBr smiles:CC(=[C]Cl)OBr H298:51.37 kcal/mol
library:CHOClBr_G4 label:Cl[C]DCCDC(Cl)Br smiles:Cl[C]=CC=C(Cl)Br H298:76.68 kcal/mol
library:CHOClBr_G4 label:Cl[C]DC(CCl)CBr smiles:Cl[C]=C(CCl)CBr H298:45.29 kcal/mol
library:CHOClBr_G4 label:ODC(Br)C(Cl)D[C]Cl smiles:O=C(Br)C(Cl)=[C]Cl H298:26.59 kcal/mol
library:CHOClBr_G4 label:Cl[C]DCC(Br)CBr smiles:Cl[C]=CC(Br)CBr H298:57.16 kcal/mol
library:CHOClBr_G4 label:CC(Br)CD[C]Cl smiles:CC(Br)C=[C]Cl H298:51.26 kcal/mol
library:CHOClBr_G4 label:OC(Cl)(Br)CD[C]Cl smiles:OC(Cl)(Br)C=[C]Cl H298:15.01 kcal/mol
library:CHOClBr_G4 label:Cl[C]DC(Cl)OBr smiles:Cl[C]=C(Cl)OBr H298:60.42 kcal/mol
library:CHOClBr_G4 label:Cl[C]DC(Cl)C(Cl)Br smiles:Cl[C]=C(Cl)C(Cl)Br H298:52.89 kcal/mol
library:CHOClBr_G4 label:Cl[C]DC(Cl)OOBr smiles:Cl[C]=C(Cl)OOBr H298:74.53 kcal/mol
library:CHOClBr_G4 label:OOC(Br)D[C]Cl smiles:OOC(Br)=[C]Cl H298:51.43 kcal/mol
library:CHOClBr_G4 label:Cl[C]DC(Cl)COBr smiles:Cl[C]=C(Cl)COBr H298:48.92 kcal/mol
library:CHOClBr_G4 label:Cl[C]DC(Cl)Br smiles:Cl[C]=C(Cl)Br H298:65.46 kcal/mol
library:CHOClBr_G4 label:Cl[C]DCC(Br)(Br)Br smiles:Cl[C]=CC(Br)(Br)Br H298:77.93 kcal/mol
library:CHOClBr_G4 label:OC(Br)D[C]Cl smiles:OC(Br)=[C]Cl H298:30.49 kcal/mol
library:CHOClBr_G4 label:Cl[C]DC(Br)OBr smiles:Cl[C]=C(Br)OBr H298:71.62 kcal/mol
library:CHOClBr_G4 label:Cl[C]DC(Br)COBr smiles:Cl[C]=C(Br)COBr H298:59.26 kcal/mol
library:CHOClBr_G4 label:CC(Cl)(Br)CD[C]Cl smiles:CC(Cl)(Br)C=[C]Cl H298:47.45 kcal/mol
library:CHOClBr_G4 label:Cl[C]DC(Br)OOBr smiles:Cl[C]=C(Br)OOBr H298:85.78 kcal/mol
library:CHOClBr_G4 label:CDC(Br)C(Br)D[C]Cl smiles:C=C(Br)C(Br)=[C]Cl H298:86.29 kcal/mol
library:CHOClBr_G4 label:Cl[C]DCC(Cl)CBr smiles:Cl[C]=CC(Cl)CBr H298:46.27 kcal/mol
library:CHOClBr_G4 label:Cl[C]DC(Cl)C(Br)Br smiles:Cl[C]=C(Cl)C(Br)Br H298:62.31 kcal/mol
library:CHOClBr_G4 label:Cl[C]DCOBr smiles:Cl[C]=COBr H298:65.70 kcal/mol
library:CHOClBr_G4 label:CDCC(Br)D[C]Cl smiles:C=CC(Br)=[C]Cl H298:80.88 kcal/mol
library:CHOClBr_G4 label:OC(D[C]Cl)CBr smiles:OC(=[C]Cl)CBr H298:20.20 kcal/mol
library:CHOClBr_G4 label:Cl[C]DC(Br)Br smiles:Cl[C]=C(Br)Br H298:76.58 kcal/mol
library:CHOClBr_G4 label:ODC(Br)CD[C]Cl smiles:O=C(Br)C=[C]Cl H298:30.33 kcal/mol
library:CHOClBr_G4 label:Cl[C]DCCC(Br)Br smiles:Cl[C]=CCC(Br)Br H298:60.04 kcal/mol
library:CHOClBr_G4 label:Cl[C]DC(Br)CDCBr smiles:Cl[C]=C(Br)C=CBr H298:86.63 kcal/mol
library:CHOClBr_G4 label:OCC(Br)D[C]Cl smiles:OCC(Br)=[C]Cl H298:22.52 kcal/mol
library:CHOClBr_G4 label:Cl[C]DC(CBr)CBr smiles:Cl[C]=C(CBr)CBr H298:55.86 kcal/mol
library:CHOClBr_G4 label:Cl[C]DCCDC(Br)Br smiles:Cl[C]=CC=C(Br)Br H298:88.54 kcal/mol
library:CHOClBr_G4 label:CC(Br)C(Br)D[C]Cl smiles:CC(Br)C(Br)=[C]Cl H298:55.89 kcal/mol
""",
)

entry(
    index = 402,
    label = "CdCdF1s",
    group = 
"""
1 * Cd  u1 {2,S} {3,D}
2   F1s u0 {1,S}
3   Cd  u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.396155,-1.1388,-1.77979,-2.31667,-3.14722,-3.74198,-4.63668],'cal/(mol*K)','+|-',[0.053138,0.0545591,0.0511559,0.0477808,0.0421676,0.0368997,0.0270262]),
        H298 = (113.471,'kcal/mol','+|-',0.0848875),
        S298 = (1.72419,'cal/(mol*K)','+|-',0.144263),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:OC(F)D[C]F smiles:OC(F)=[C]F H298:-51.47 kcal/mol
library:CHOF_G4 label:OC(F)(F)CD[C]F smiles:OC(F)(F)C=[C]F H298:-127.84 kcal/mol
library:CHOF_G4 label:F[C]DC(F)F smiles:F[C]=C(F)F H298:-54.10 kcal/mol
library:CHOF_G4 label:OOC(F)D[C]F smiles:OOC(F)=[C]F H298:-30.93 kcal/mol
library:CHOF_G4 label:F[C]DC(F)C(F)DC(F)F smiles:F[C]=C(F)C(F)=C(F)F H298:-123.96 kcal/mol
library:CHOF_G4 label:F[C]DCC(F)(F)C(F)F smiles:F[C]=CC(F)(F)C(F)F H298:-179.71 kcal/mol
library:CHOF_G4 label:F[C]DCC(F)DCF smiles:F[C]=CC(F)=CF H298:-43.84 kcal/mol
library:CHOF_G4 label:CC(F)C(F)D[C]F smiles:CC(F)C(F)=[C]F H298:-72.74 kcal/mol
library:CHOF_G4 label:F[C]DCCC(F)F smiles:F[C]=CCC(F)F H298:-84.84 kcal/mol
library:CHOF_G4 label:CC(F)CD[C]F smiles:CC(F)C=[C]F H298:-33.59 kcal/mol
library:CHOF_G4 label:F[C]DC(F)CDCF smiles:F[C]=C(F)C=CF H298:-41.57 kcal/mol
library:CHOF_G4 label:F[C]DC(C(F)F)C(F)(F)F smiles:F[C]=C(C(F)F)C(F)(F)F H298:-233.05 kcal/mol
library:CHOF_G4 label:OOCD[C]F smiles:OOC=[C]F H298:13.98 kcal/mol
library:CHOF_G4 label:F[C]DC(F)OC(F)F smiles:F[C]=C(F)OC(F)F H298:-152.76 kcal/mol
library:CHOF_G4 label:F[C]DCCDCF smiles:F[C]=CC=CF H298:-3.19 kcal/mol
library:CHOF_G4 label:CDCC(F)D[C]F smiles:C=CC(F)=[C]F H298:1.75 kcal/mol
library:CHOF_G4 label:F[C]DC(F)CC(F)F smiles:F[C]=C(F)CC(F)F H298:-124.82 kcal/mol
library:CHOF_G4 label:F[C]DC(F)C#CF smiles:F[C]=C(F)C#CF H298:20.06 kcal/mol
library:CHOF_G4 label:OC(D[C]F)C(F)F smiles:OC(=[C]F)C(F)F H298:-111.38 kcal/mol
library:CHOF_G4 label:OC(D[C]F)CF smiles:OC(=[C]F)CF H298:-59.81 kcal/mol
library:CHOF_G4 label:OCC(F)D[C]F smiles:OCC(F)=[C]F H298:-55.68 kcal/mol
library:CHOF_G4 label:CDC(F)C(F)D[C]F smiles:C=C(F)C(F)=[C]F H298:-42.68 kcal/mol
library:CHOF_G4 label:F[C]DC(F)C(F)F smiles:F[C]=C(F)C(F)F H298:-113.09 kcal/mol
library:CHOF_G4 label:F[C]DC(F)OC(F)(F)F smiles:F[C]=C(F)OC(F)(F)F H298:-209.09 kcal/mol
library:CHOF_G4 label:F[C]DCC(F)DC(F)F smiles:F[C]=CC(F)=C(F)F H298:-88.31 kcal/mol
library:CHOF_G4 label:CDCCD[C]F smiles:C=CC=[C]F H298:41.84 kcal/mol
library:CHOF_G4 label:F[C]DCOC(F)(F)F smiles:F[C]=COC(F)(F)F H298:-167.75 kcal/mol
library:CHOF_G4 label:F[C]DCC#CF smiles:F[C]=CC#CF H298:57.49 kcal/mol
library:CHOF_G4 label:F[C]DC(F)C(F)(F)C(F)F smiles:F[C]=C(F)C(F)(F)C(F)F H298:-214.57 kcal/mol
library:CHOF_G4 label:F[C]DCOC(F)F smiles:F[C]=COC(F)F H298:-111.13 kcal/mol
library:CHOF_G4 label:C#CCD[C]F smiles:C#CC=[C]F H298:85.37 kcal/mol
library:CHOF_G4 label:CC(F)D[C]F smiles:CC(F)=[C]F H298:-22.27 kcal/mol
library:CHOF_G4 label:F[C]DC(F)CDC(F)F smiles:F[C]=C(F)C=C(F)F H298:-88.35 kcal/mol
library:CHOF_G4 label:OCCD[C]F smiles:OCC=[C]F H298:-15.61 kcal/mol
library:CHOF_G4 label:F[C]DCCOF smiles:F[C]=CCOF H298:11.55 kcal/mol
library:CHOF_G4 label:F[C]DC(F)C(F)(F)OF smiles:F[C]=C(F)C(F)(F)OF H298:-125.82 kcal/mol
library:CHOF_G4 label:F[C]DC(F)CC(F)(F)F smiles:F[C]=C(F)CC(F)(F)F H298:-183.12 kcal/mol
library:CHOF_G4 label:F[C]DCC(F)(F)CF smiles:F[C]=CC(F)(F)CF H298:-127.54 kcal/mol
library:CHOF_G4 label:F[C]DC(CF)C(F)F smiles:F[C]=C(CF)C(F)F H298:-125.56 kcal/mol
library:CHOF_G4 label:F[C]DC(CF)OF smiles:F[C]=C(CF)OF H298:-26.23 kcal/mol
library:CHOF_G4 label:ODCC(F)D[C]F smiles:O=CC(F)=[C]F H298:-38.28 kcal/mol
library:CHOF_G4 label:F[C]DCC(F)F smiles:F[C]=CC(F)F H298:-75.93 kcal/mol
library:CHOF_G4 label:F[C]DCCCF smiles:F[C]=CCCF H298:-30.02 kcal/mol
library:CHOF_G4 label:ODCCD[C]F smiles:O=CC=[C]F H298:-1.65 kcal/mol
library:CHOF_G4 label:F[C]DCCC(F)(F)F smiles:F[C]=CCC(F)(F)F H298:-144.32 kcal/mol
library:CHOF_G4 label:F[C]DC(F)C(F)(F)CF smiles:F[C]=C(F)C(F)(F)CF H298:-165.05 kcal/mol
library:CHOF_G4 label:F[C]DCC(F)(F)OF smiles:F[C]=CC(F)(F)OF H298:-90.60 kcal/mol
library:CHOF_G4 label:F[C]DC(CF)C(F)(F)F smiles:F[C]=C(CF)C(F)(F)F H298:-183.13 kcal/mol
library:CHOF_G4 label:F[C]DC(CF)CF smiles:F[C]=C(CF)CF H298:-74.15 kcal/mol
library:CHOF_G4 label:F[C]DC(F)OCF smiles:F[C]=C(F)OCF H298:-96.76 kcal/mol
library:CHOF_G4 label:F[C]DC(F)CCF smiles:F[C]=C(F)CCF H298:-70.66 kcal/mol
library:CHOF_G4 label:OC(F)CD[C]F smiles:OC(F)C=[C]F H298:-68.65 kcal/mol
library:CHOF_G4 label:F[C]DC(F)C(F)DCF smiles:F[C]=C(F)C(F)=CF H298:-81.20 kcal/mol
library:CHOF_G4 label:CD[C]F smiles:C=[C]F H298:25.82 kcal/mol
library:CHOF_G4 label:COCD[C]F smiles:COC=[C]F H298:-4.69 kcal/mol
library:CHOF_G4 label:F[C]DCC(F)C(F)F smiles:F[C]=CC(F)C(F)F H298:-127.78 kcal/mol
library:CHOF_G4 label:F[C]DC(F)CF smiles:F[C]=C(F)CF H298:-62.76 kcal/mol
library:CHOF_G4 label:F[C]DC(C(F)(F)F)C(F)(F)F smiles:F[C]=C(C(F)(F)F)C(F)(F)F H298:-289.46 kcal/mol
library:CHOF_G4 label:F[C]DCOCF smiles:F[C]=COCF H298:-53.78 kcal/mol
library:CHOF_G4 label:CC(D[C]F)C(F)(F)F smiles:CC(=[C]F)C(F)(F)F H298:-143.22 kcal/mol
library:CHOF_G4 label:F[C]DC(F)COF smiles:F[C]=C(F)COF H298:-26.91 kcal/mol
library:CHOF_G4 label:F[C]DC(F)C(F)C(F)F smiles:F[C]=C(F)C(F)C(F)F H298:-165.08 kcal/mol
library:CHOF_G4 label:F[C]DC(F)OF smiles:F[C]=C(F)OF H298:-22.93 kcal/mol
library:CHOF_G4 label:F[C]DCOOF smiles:F[C]=COOF H298:35.17 kcal/mol
library:CHOF_G4 label:OCD[C]F smiles:OC=[C]F H298:-8.13 kcal/mol
library:CHOF_G4 label:F[C]DC(F)C(F)CF smiles:F[C]=C(F)C(F)CF H298:-113.02 kcal/mol
library:CHOF_G4 label:ODC(F)CD[C]F smiles:O=C(F)C=[C]F H298:-62.38 kcal/mol
library:CHOF_G4 label:F[C]DC(F)C(F)(F)C(F)(F)F smiles:F[C]=C(F)C(F)(F)C(F)(F)F H298:-270.42 kcal/mol
library:CHOF_G4 label:F[C]DC(F)C(F)C(F)(F)F smiles:F[C]=C(F)C(F)C(F)(F)F H298:-221.13 kcal/mol
library:CHOF_G4 label:ODC(F)C(F)D[C]F smiles:O=C(F)C(F)=[C]F H298:-98.57 kcal/mol
library:CHOF_G4 label:F[C]DCC(F)(F)F smiles:F[C]=CC(F)(F)F H298:-133.94 kcal/mol
library:CHOF_G4 label:F[C]DC(F)C(F)OF smiles:F[C]=C(F)C(F)OF H298:-74.26 kcal/mol
library:CHOF_G4 label:C#CC(F)D[C]F smiles:C#CC(F)=[C]F H298:48.13 kcal/mol
library:CHOF_G4 label:COC(F)D[C]F smiles:COC(F)=[C]F H298:-48.20 kcal/mol
library:CHOF_G4 label:CC(F)(F)C(F)D[C]F smiles:CC(F)(F)C(F)=[C]F H298:-125.90 kcal/mol
library:CHOF_G4 label:CC(C)D[C]F smiles:CC(C)=[C]F H298:11.00 kcal/mol
library:CHOF_G4 label:CC(D[C]F)C(F)F smiles:CC(=[C]F)C(F)F H298:-86.00 kcal/mol
library:CHOF_G4 label:OC(O)D[C]F smiles:OC(O)=[C]F H298:-51.48 kcal/mol
library:CHOF_G4 label:OC(F)(F)C(F)D[C]F smiles:OC(F)(F)C(F)=[C]F H298:-164.70 kcal/mol
library:CHOF_G4 label:F[C]DCC(F)(F)C(F)(F)F smiles:F[C]=CC(F)(F)C(F)(F)F H298:-235.67 kcal/mol
library:CHOF_G4 label:F[C]DC(C(F)F)C(F)F smiles:F[C]=C(C(F)F)C(F)F H298:-177.10 kcal/mol
library:CHOF_G4 label:F[C]DCC(F)CF smiles:F[C]=CC(F)CF H298:-74.97 kcal/mol
library:CHOF_G4 label:CCCD[C]F smiles:CCC=[C]F H298:14.25 kcal/mol
library:CHOF_G4 label:F[C]DC(OF)C(F)F smiles:F[C]=C(OF)C(F)F H298:-80.26 kcal/mol
library:CHOF_G4 label:OC(F)C(F)D[C]F smiles:OC(F)C(F)=[C]F H298:-108.16 kcal/mol
library:CHOF_G4 label:F[C]DCCF smiles:F[C]=CCF H298:-23.52 kcal/mol
library:CHOF_G4 label:F[C]DCC(F)OF smiles:F[C]=CC(F)OF H298:-37.63 kcal/mol
library:CHOF_G4 label:F[C]DCC(F)C(F)(F)F smiles:F[C]=CC(F)C(F)(F)F H298:-185.31 kcal/mol
library:CHOF_G4 label:CC(D[C]F)CF smiles:CC(=[C]F)CF H298:-32.28 kcal/mol
library:CHOF_G4 label:CCC(F)D[C]F smiles:CCC(F)=[C]F H298:-27.33 kcal/mol
library:CHOF_G4 label:CC(O)D[C]F smiles:CC(O)=[C]F H298:-19.15 kcal/mol
library:CHOF_G4 label:F[C]DC(F)C(F)(F)F smiles:F[C]=C(F)C(F)(F)F H298:-169.26 kcal/mol
library:CHOF_G4 label:CC(F)(F)CD[C]F smiles:CC(F)(F)C=[C]F H298:-88.31 kcal/mol
library:CHOF_G4 label:CDC(F)CD[C]F smiles:C=C(F)C=[C]F H298:-4.65 kcal/mol
library:CHOF_G4 label:CCD[C]F smiles:CC=[C]F H298:19.28 kcal/mol
library:CHOF_G4 label:OC(D[C]F)C(F)(F)F smiles:OC(=[C]F)C(F)(F)F H298:-168.12 kcal/mol
library:CHOF_G4 label:F[C]DCCDC(F)F smiles:F[C]=CC=C(F)F H298:-51.48 kcal/mol
library:CHOFCl_G4 label:OC(D[C]F)C(F)Cl smiles:OC(=[C]F)C(F)Cl H298:-65.77 kcal/mol
library:CHOFCl_G4 label:CC(Cl)C(F)D[C]F smiles:CC(Cl)C(F)=[C]F H298:-32.88 kcal/mol
library:CHOFCl_G4 label:F[C]DCCl smiles:F[C]=CCl H298:23.79 kcal/mol
library:CHOFCl_G4 label:F[C]DCC(F)DCCl smiles:F[C]=CC(F)=CCl H298:-7.86 kcal/mol
library:CHOFCl_G4 label:F[C]DCC(F)Cl smiles:F[C]=CC(F)Cl H298:-30.41 kcal/mol
library:CHOFCl_G4 label:ODC(Cl)C(Cl)D[C]F smiles:O=C(Cl)C(Cl)=[C]F H298:-18.02 kcal/mol
library:CHOFCl_G4 label:F[C]DCC(Cl)OCl smiles:F[C]=CC(Cl)OCl H298:9.57 kcal/mol
library:CHOFCl_G4 label:F[C]DC(CF)CCl smiles:F[C]=C(CF)CCl H298:-36.36 kcal/mol
library:CHOFCl_G4 label:OC(D[C]F)C(Cl)Cl smiles:OC(=[C]F)C(Cl)Cl H298:-25.76 kcal/mol
library:CHOFCl_G4 label:CC(Cl)C(Cl)D[C]F smiles:CC(Cl)C(Cl)=[C]F H298:2.09 kcal/mol
library:CHOFCl_G4 label:ODC(Cl)C(F)D[C]F smiles:O=C(Cl)C(F)=[C]F H298:-52.61 kcal/mol
library:CHOFCl_G4 label:CDCC(Cl)D[C]F smiles:C=CC(Cl)=[C]F H298:37.45 kcal/mol
library:CHOFCl_G4 label:ODC(Cl)CD[C]F smiles:O=C(Cl)C=[C]F H298:-16.34 kcal/mol
library:CHOFCl_G4 label:F[C]DCOC(Cl)Cl smiles:F[C]=COC(Cl)Cl H298:-15.36 kcal/mol
library:CHOFCl_G4 label:OCC(Cl)D[C]F smiles:OCC(Cl)=[C]F H298:-20.52 kcal/mol
library:CHOFCl_G4 label:F[C]DCC(Cl)Cl smiles:F[C]=CC(Cl)Cl H298:10.98 kcal/mol
library:CHOFCl_G4 label:F[C]DC(OCl)OCl smiles:F[C]=C(OCl)OCl H298:26.73 kcal/mol
library:CHOFCl_G4 label:F[C]DCCDC(Cl)Cl smiles:F[C]=CC=C(Cl)Cl H298:30.44 kcal/mol
library:CHOFCl_G4 label:F[C]DCOOCl smiles:F[C]=COOCl H298:44.12 kcal/mol
library:CHOFCl_G4 label:F[C]DCC(Cl)(Cl)Cl smiles:F[C]=CC(Cl)(Cl)Cl H298:9.28 kcal/mol
library:CHOFCl_G4 label:F[C]DCCOCl smiles:F[C]=CCOCl H298:17.61 kcal/mol
library:CHOFCl_G4 label:F[C]DC(Cl)OCCl smiles:F[C]=C(Cl)OCCl H298:-16.37 kcal/mol
library:CHOFCl_G4 label:F[C]DC(Cl)CCCl smiles:F[C]=C(Cl)CCCl H298:2.63 kcal/mol
library:CHOFCl_G4 label:F[C]DC(F)CCl smiles:F[C]=C(F)CCl H298:-24.69 kcal/mol
library:CHOFCl_G4 label:F[C]DC(F)COCl smiles:F[C]=C(F)COCl H298:-21.77 kcal/mol
library:CHOFCl_G4 label:CC(D[C]F)OCl smiles:CC(=[C]F)OCl H298:17.71 kcal/mol
library:CHOFCl_G4 label:F[C]DC(F)Cl smiles:F[C]=C(F)Cl H298:-14.58 kcal/mol
library:CHOFCl_G4 label:F[C]DCOCl smiles:F[C]=COCl H298:29.40 kcal/mol
library:CHOFCl_G4 label:F[C]DC(Cl)CCl smiles:F[C]=C(Cl)CCl H298:10.66 kcal/mol
library:CHOFCl_G4 label:F[C]DCC(F)OCl smiles:F[C]=CC(F)OCl H298:-33.74 kcal/mol
library:CHOFCl_G4 label:CDC(Cl)C(Cl)D[C]F smiles:C=C(Cl)C(Cl)=[C]F H298:31.43 kcal/mol
library:CHOFCl_G4 label:F[C]DC(CCl)OCl smiles:F[C]=C(CCl)OCl H298:15.38 kcal/mol
library:CHOFCl_G4 label:CC(F)(Cl)CD[C]F smiles:CC(F)(Cl)C=[C]F H298:-41.35 kcal/mol
library:CHOFCl_G4 label:CCC(Cl)D[C]F smiles:CCC(Cl)=[C]F H298:8.30 kcal/mol
library:CHOFCl_G4 label:OC(Cl)(Cl)CD[C]F smiles:OC(Cl)(Cl)C=[C]F H298:-30.74 kcal/mol
library:CHOFCl_G4 label:F[C]DC(F)C(F)Cl smiles:F[C]=C(F)C(F)Cl H298:-67.01 kcal/mol
library:CHOFCl_G4 label:CC(Cl)D[C]F smiles:CC(Cl)=[C]F H298:13.82 kcal/mol
library:CHOFCl_G4 label:F[C]DCCC(Cl)Cl smiles:F[C]=CCC(Cl)Cl H298:2.31 kcal/mol
library:CHOFCl_G4 label:F[C]DCOC(F)Cl smiles:F[C]=COC(F)Cl H298:-61.85 kcal/mol
library:CHOFCl_G4 label:OC(Cl)CD[C]F smiles:OC(Cl)C=[C]F H298:-24.93 kcal/mol
library:CHOFCl_G4 label:F[C]DCC(F)(Cl)Cl smiles:F[C]=CC(F)(Cl)Cl H298:-34.84 kcal/mol
library:CHOFCl_G4 label:OC(F)(Cl)CD[C]F smiles:OC(F)(Cl)C=[C]F H298:-77.67 kcal/mol
library:CHOFCl_G4 label:ODCC(Cl)D[C]F smiles:O=CC(Cl)=[C]F H298:-3.95 kcal/mol
library:CHOFCl_G4 label:OOC(Cl)D[C]F smiles:OOC(Cl)=[C]F H298:7.86 kcal/mol
library:CHOFCl_G4 label:F[C]DCC(Cl)DCCl smiles:F[C]=CC(Cl)=CCl H298:29.81 kcal/mol
library:CHOFCl_G4 label:F[C]DC(CCl)CCl smiles:F[C]=C(CCl)CCl H298:0.97 kcal/mol
library:CHOFCl_G4 label:CC(Cl)(Cl)CD[C]F smiles:CC(Cl)(Cl)C=[C]F H298:0.41 kcal/mol
library:CHOFCl_G4 label:F[C]DC(Cl)OCl smiles:F[C]=C(Cl)OCl H298:25.88 kcal/mol
library:CHOFCl_G4 label:CDC(Cl)CD[C]F smiles:C=C(Cl)C=[C]F H298:35.01 kcal/mol
library:CHOFCl_G4 label:F[C]DC(Cl)C(Cl)Cl smiles:F[C]=C(Cl)C(Cl)Cl H298:7.44 kcal/mol
library:CHOFCl_G4 label:F[C]DCC(F)CCl smiles:F[C]=CC(F)CCl H298:-36.94 kcal/mol
library:CHOFCl_G4 label:F[C]DCCCl smiles:F[C]=CCCl H298:15.07 kcal/mol
library:CHOFCl_G4 label:F[C]DC(F)C(Cl)Cl smiles:F[C]=C(F)C(Cl)Cl H298:-27.15 kcal/mol
library:CHOFCl_G4 label:F[C]DC(F)OCCl smiles:F[C]=C(F)OCCl H298:-53.81 kcal/mol
library:CHOFCl_G4 label:CC(D[C]F)CCl smiles:CC(=[C]F)CCl H298:5.70 kcal/mol
library:CHOFCl_G4 label:F[C]DC(Cl)CDCCl smiles:F[C]=C(Cl)C=CCl H298:33.34 kcal/mol
library:CHOFCl_G4 label:F[C]DC(F)OCl smiles:F[C]=C(F)OCl H298:-11.05 kcal/mol
library:CHOFCl_G4 label:F[C]DC(F)CCCl smiles:F[C]=C(F)CCCl H298:-31.77 kcal/mol
library:CHOFCl_G4 label:F[C]DC(Cl)COCl smiles:F[C]=C(Cl)COCl H298:13.10 kcal/mol
library:CHOFCl_G4 label:F[C]DC(Cl)OOCl smiles:F[C]=C(Cl)OOCl H298:39.97 kcal/mol
library:CHOFCl_G4 label:F[C]DCC(F)(F)Cl smiles:F[C]=CC(F)(F)Cl H298:-82.68 kcal/mol
library:CHOFCl_G4 label:F[C]DCCCCl smiles:F[C]=CCCCl H298:8.53 kcal/mol
library:CHOFCl_G4 label:F[C]DCOCCl smiles:F[C]=COCCl H298:-10.36 kcal/mol
library:CHOFCl_G4 label:COC(Cl)D[C]F smiles:COC(Cl)=[C]F H298:-7.77 kcal/mol
library:CHOFCl_G4 label:OC(Cl)C(Cl)D[C]F smiles:OC(Cl)C(Cl)=[C]F H298:-29.65 kcal/mol
library:CHOFCl_G4 label:CC(D[C]F)C(Cl)Cl smiles:CC(=[C]F)C(Cl)Cl H298:0.90 kcal/mol
library:CHOFCl_G4 label:CDC(Cl)C(F)D[C]F smiles:C=C(Cl)C(F)=[C]F H298:-4.03 kcal/mol
library:CHOFCl_G4 label:F[C]DCCC(F)Cl smiles:F[C]=CCC(F)Cl H298:-39.28 kcal/mol
library:CHOFCl_G4 label:F[C]DCCDCCl smiles:F[C]=CC=CCl H298:34.82 kcal/mol
library:CHOFCl_G4 label:OC(Cl)D[C]F smiles:OC(Cl)=[C]F H298:-12.58 kcal/mol
library:CHOFCl_G4 label:CC(Cl)CD[C]F smiles:CC(Cl)C=[C]F H298:6.33 kcal/mol
library:CHOFCl_G4 label:F[C]DCC(Cl)CCl smiles:F[C]=CC(Cl)CCl H298:2.19 kcal/mol
library:CHOFCl_G4 label:F[C]DC(CF)OCl smiles:F[C]=C(CF)OCl H298:-22.14 kcal/mol
library:CHOFCl_G4 label:OC(Cl)C(F)D[C]F smiles:OC(Cl)C(F)=[C]F H298:-63.30 kcal/mol
library:CHOFCl_G4 label:CC(D[C]F)C(F)Cl smiles:CC(=[C]F)C(F)Cl H298:-39.60 kcal/mol
library:CHOFCl_G4 label:F[C]DCCDC(F)Cl smiles:F[C]=CC=C(F)Cl H298:-8.98 kcal/mol
library:CHOFCl_G4 label:F[C]DC(F)CDCCl smiles:F[C]=C(F)C=CCl H298:-3.42 kcal/mol
library:CHOFCl_G4 label:F[C]DC(Cl)Cl smiles:F[C]=C(Cl)Cl H298:40.48 kcal/mol
library:CHOFCl_G4 label:OC(D[C]F)CCl smiles:OC(=[C]F)CCl H298:-22.48 kcal/mol
library:CHOFClBr_G4 label:F[C]DC(Cl)C(Br)Br smiles:F[C]=C(Cl)C(Br)Br H298:30.06 kcal/mol
library:CHOFClBr_G4 label:F[C]DC(Cl)Br smiles:F[C]=C(Cl)Br H298:33.83 kcal/mol
library:CHOFClBr_G4 label:F[C]DCC(Cl)CBr smiles:F[C]=CC(Cl)CBr H298:12.48 kcal/mol
library:CHOFClBr_G4 label:OC(Br)C(Cl)D[C]F smiles:OC(Br)C(Cl)=[C]F H298:-17.67 kcal/mol
library:CHOFClBr_G4 label:CC(Cl)(Br)CD[C]F smiles:CC(Cl)(Br)C=[C]F H298:13.20 kcal/mol
library:CHOFClBr_G4 label:CC(D[C]F)C(Cl)Br smiles:CC(=[C]F)C(Cl)Br H298:12.86 kcal/mol
library:CHOFClBr_G4 label:F[C]DC(Cl)OOBr smiles:F[C]=C(Cl)OOBr H298:42.76 kcal/mol
library:CHOFClBr_G4 label:F[C]DC(Cl)COBr smiles:F[C]=C(Cl)COBr H298:16.33 kcal/mol
library:CHOFClBr_G4 label:F[C]DC(Cl)CDCBr smiles:F[C]=C(Cl)C=CBr H298:43.54 kcal/mol
library:CHOFClBr_G4 label:F[C]DC(F)C(Cl)Br smiles:F[C]=C(F)C(Cl)Br H298:-15.12 kcal/mol
library:CHOFClBr_G4 label:F[C]DC(Cl)C(Cl)Br smiles:F[C]=C(Cl)C(Cl)Br H298:20.79 kcal/mol
library:CHOFClBr_G4 label:F[C]DC(Cl)OBr smiles:F[C]=C(Cl)OBr H298:29.37 kcal/mol
library:CHOFClBr_G4 label:F[C]DC(CCl)CBr smiles:F[C]=C(CCl)CBr H298:11.80 kcal/mol
library:CHOFClBr_G4 label:F[C]DCC(Cl)DCBr smiles:F[C]=CC(Cl)=CBr H298:41.71 kcal/mol
library:CHOFClBr_G4 label:F[C]DCC(F)(Cl)Br smiles:F[C]=CC(F)(Cl)Br H298:-21.26 kcal/mol
library:CHOFClBr_G4 label:F[C]DCCC(Cl)Br smiles:F[C]=CCC(Cl)Br H298:14.04 kcal/mol
library:CHOFClBr_G4 label:CDC(Br)C(Cl)D[C]F smiles:C=C(Br)C(Cl)=[C]F H298:43.09 kcal/mol
library:CHOFClBr_G4 label:F[C]DC(CCl)OBr smiles:F[C]=C(CCl)OBr H298:17.63 kcal/mol
library:CHOFClBr_G4 label:F[C]DC(Cl)CBr smiles:F[C]=C(Cl)CBr H298:21.56 kcal/mol
library:CHOFClBr_G4 label:F[C]DC(Cl)CCBr smiles:F[C]=C(Cl)CCBr H298:13.69 kcal/mol
library:CHOFClBr_G4 label:F[C]DC(Cl)OCBr smiles:F[C]=C(Cl)OCBr H298:-3.95 kcal/mol
library:CHOFClBr_G4 label:F[C]DCC(Cl)(Cl)Br smiles:F[C]=CC(Cl)(Cl)Br H298:21.21 kcal/mol
library:CHOFClBr_G4 label:F[C]DCCDC(Cl)Br smiles:F[C]=CC=C(Cl)Br H298:42.44 kcal/mol
library:CHOFClBr_G4 label:F[C]DC(OCl)OBr smiles:F[C]=C(OCl)OBr H298:29.54 kcal/mol
library:CHOFClBr_G4 label:F[C]DCC(Cl)Br smiles:F[C]=CC(Cl)Br H298:22.50 kcal/mol
library:CHOFClBr_G4 label:OC(Cl)(Br)CD[C]F smiles:OC(Cl)(Br)C=[C]F H298:-18.52 kcal/mol
library:CHOFClBr_G4 label:CC(Br)C(Cl)D[C]F smiles:CC(Br)C(Cl)=[C]F H298:13.18 kcal/mol
library:CHOFClBr_G4 label:F[C]DCOC(Cl)Br smiles:F[C]=COC(Cl)Br H298:-3.32 kcal/mol
library:CHOFClBr_G4 label:OC(D[C]F)C(Cl)Br smiles:OC(=[C]F)C(Cl)Br H298:-14.36 kcal/mol
library:CHOFClBr_G4 label:F[C]DCC(Cl)OBr smiles:F[C]=CC(Cl)OBr H298:12.77 kcal/mol
library:CHOFClBr_G4 label:F[C]DCC(Cl)(Br)Br smiles:F[C]=CC(Cl)(Br)Br H298:32.93 kcal/mol
library:CHOFClBr_G4 label:ODC(Br)C(Cl)D[C]F smiles:O=C(Br)C(Cl)=[C]F H298:-5.67 kcal/mol
library:CHOFBr_G4 label:F[C]DC(F)C(F)OBr smiles:F[C]=C(F)C(F)OBr H298:-67.13 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)D[C]F smiles:O=CC(Br)=[C]F H298:6.41 kcal/mol
library:CHOFBr_G4 label:OC(D[C]F)CBr smiles:OC(=[C]F)CBr H298:-11.64 kcal/mol
library:CHOFBr_G4 label:OOC(Br)D[C]F smiles:OOC(Br)=[C]F H298:19.23 kcal/mol
library:CHOFBr_G4 label:F[C]DCOC(F)(F)Br smiles:F[C]=COC(F)(F)Br H298:-101.80 kcal/mol
library:CHOFBr_G4 label:F[C]DC(F)C(Br)DCBr smiles:F[C]=C(F)C(Br)=CBr H298:14.61 kcal/mol
library:CHOFBr_G4 label:F[C]DC(F)C(Br)CBr smiles:F[C]=C(F)C(Br)CBr H298:-16.64 kcal/mol
library:CHOFBr_G4 label:F[C]DC(CBr)C(Br)Br smiles:F[C]=C(CBr)C(Br)Br H298:31.35 kcal/mol
library:CHOFBr_G4 label:F[C]DC(F)CDCBr smiles:F[C]=C(F)C=CBr H298:8.01 kcal/mol
library:CHOFBr_G4 label:F[C]DCC(F)DC(F)Br smiles:F[C]=CC(F)=C(F)Br H298:-36.14 kcal/mol
library:CHOFBr_G4 label:CDC(Br)C(Br)D[C]F smiles:C=C(Br)C(Br)=[C]F H298:53.71 kcal/mol
library:CHOFBr_G4 label:F[C]DCCDC(F)Br smiles:F[C]=CC=C(F)Br H298:3.81 kcal/mol
library:CHOFBr_G4 label:F[C]DC(Br)OBr smiles:F[C]=C(Br)OBr H298:40.67 kcal/mol
library:CHOFBr_G4 label:F[C]DCC(F)(Br)Br smiles:F[C]=CC(F)(Br)Br H298:-9.63 kcal/mol
library:CHOFBr_G4 label:F[C]DCC(Br)DCBr smiles:F[C]=CC(Br)=CBr H298:52.85 kcal/mol
library:CHOFBr_G4 label:F[C]DC(CBr)C(F)F smiles:F[C]=C(CBr)C(F)F H298:-77.02 kcal/mol
library:CHOFBr_G4 label:F[C]DCCC(Br)Br smiles:F[C]=CCC(Br)Br H298:25.60 kcal/mol
library:CHOFBr_G4 label:F[C]DC(CF)C(F)Br smiles:F[C]=C(CF)C(F)Br H298:-67.89 kcal/mol
library:CHOFBr_G4 label:CC(D[C]F)C(F)Br smiles:CC(=[C]F)C(F)Br H298:-27.21 kcal/mol
library:CHOFBr_G4 label:F[C]DCC(F)C(Br)Br smiles:F[C]=CC(F)C(Br)Br H298:-18.83 kcal/mol
library:CHOFBr_G4 label:F[C]DC(CBr)CBr smiles:F[C]=C(CBr)CBr H298:22.49 kcal/mol
library:CHOFBr_G4 label:F[C]DC(CF)OBr smiles:F[C]=C(CF)OBr H298:-19.82 kcal/mol
library:CHOFBr_G4 label:F[C]DCC(Br)(Br)OBr smiles:F[C]=CC(Br)(Br)OBr H298:31.99 kcal/mol
library:CHOFBr_G4 label:F[C]DC(Br)C(Br)(Br)Br smiles:F[C]=C(Br)C(Br)(Br)Br H298:51.55 kcal/mol
library:CHOFBr_G4 label:CDC(Br)CD[C]F smiles:C=C(Br)C=[C]F H298:46.94 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)CD[C]F smiles:OC(Br)(Br)C=[C]F H298:-6.44 kcal/mol
library:CHOFBr_G4 label:F[C]DCCDCBr smiles:F[C]=CC=CBr H298:46.94 kcal/mol
library:CHOFBr_G4 label:F[C]DCCC(F)Br smiles:F[C]=CCC(F)Br H298:-26.65 kcal/mol
library:CHOFBr_G4 label:F[C]DCC(F)(F)OBr smiles:F[C]=CC(F)(F)OBr H298:-86.50 kcal/mol
library:CHOFBr_G4 label:OC(Br)CD[C]F smiles:OC(Br)C=[C]F H298:-12.80 kcal/mol
library:CHOFBr_G4 label:F[C]DC(Br)COBr smiles:F[C]=C(Br)COBr H298:26.74 kcal/mol
library:CHOFBr_G4 label:F[C]DCCC(F)(Br)Br smiles:F[C]=CCC(F)(Br)Br H298:-19.96 kcal/mol
library:CHOFBr_G4 label:F[C]DC(Br)C(Br)CBr smiles:F[C]=C(Br)C(Br)CBr H298:30.39 kcal/mol
library:CHOFBr_G4 label:F[C]DC(OBr)C(F)F smiles:F[C]=C(OBr)C(F)F H298:-68.66 kcal/mol
library:CHOFBr_G4 label:F[C]DCOC(Br)(Br)Br smiles:F[C]=COC(Br)(Br)Br H298:19.68 kcal/mol
library:CHOFBr_G4 label:F[C]DC(Br)OOBr smiles:F[C]=C(Br)OOBr H298:54.08 kcal/mol
library:CHOFBr_G4 label:F[C]DC(F)C(Br)Br smiles:F[C]=C(F)C(Br)Br H298:-4.56 kcal/mol
library:CHOFBr_G4 label:CC(D[C]F)C(Br)(Br)Br smiles:CC(=[C]F)C(Br)(Br)Br H298:34.41 kcal/mol
library:CHOFBr_G4 label:CC(D[C]F)C(F)(Br)Br smiles:CC(=[C]F)C(F)(Br)Br H298:-19.42 kcal/mol
library:CHOFBr_G4 label:OC(F)(Br)CD[C]F smiles:OC(F)(Br)C=[C]F H298:-64.65 kcal/mol
library:CHOFBr_G4 label:CC(D[C]F)C(F)(F)Br smiles:CC(=[C]F)C(F)(F)Br H298:-78.86 kcal/mol
library:CHOFBr_G4 label:OC(F)(Br)C(F)D[C]F smiles:OC(F)(Br)C(F)=[C]F H298:-101.19 kcal/mol
library:CHOFBr_G4 label:OC(Br)D[C]F smiles:OC(Br)=[C]F H298:-1.02 kcal/mol
library:CHOFBr_G4 label:F[C]DCOCBr smiles:F[C]=COCBr H298:0.18 kcal/mol
library:CHOFBr_G4 label:F[C]DC(F)C(F)(Br)Br smiles:F[C]=C(F)C(F)(Br)Br H298:-46.84 kcal/mol
library:CHOFBr_G4 label:F[C]DCC(F)(F)Br smiles:F[C]=CC(F)(F)Br H298:-69.23 kcal/mol
library:CHOFBr_G4 label:F[C]DCCCBr smiles:F[C]=CCCBr H298:19.52 kcal/mol
library:CHOFBr_G4 label:F[C]DC(F)CC(Br)Br smiles:F[C]=C(F)CC(Br)Br H298:-14.38 kcal/mol
library:CHOFBr_G4 label:F[C]DC(F)CDC(F)Br smiles:F[C]=C(F)C=C(F)Br H298:-32.83 kcal/mol
library:CHOFBr_G4 label:F[C]DCC(F)DC(Br)Br smiles:F[C]=CC(F)=C(Br)Br H298:12.32 kcal/mol
library:CHOFBr_G4 label:CC(D[C]F)C(Br)Br smiles:CC(=[C]F)C(Br)Br H298:23.77 kcal/mol
library:CHOFBr_G4 label:OC(D[C]F)C(Br)(Br)Br smiles:OC(=[C]F)C(Br)(Br)Br H298:7.57 kcal/mol
library:CHOFBr_G4 label:F[C]DCC(F)(Br)CBr smiles:F[C]=CC(F)(Br)CBr H298:-20.89 kcal/mol
library:CHOFBr_G4 label:F[C]DCCC(F)(F)Br smiles:F[C]=CCC(F)(F)Br H298:-82.00 kcal/mol
library:CHOFBr_G4 label:CC(D[C]F)CBr smiles:CC(=[C]F)CBr H298:16.63 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(F)D[C]F smiles:OC(Br)C(F)=[C]F H298:-51.30 kcal/mol
library:CHOFBr_G4 label:COC(Br)D[C]F smiles:COC(Br)=[C]F H298:2.15 kcal/mol
library:CHOFBr_G4 label:F[C]DCC(Br)CBr smiles:F[C]=CC(Br)CBr H298:23.19 kcal/mol
library:CHOFBr_G4 label:F[C]DC(F)OCBr smiles:F[C]=C(F)OCBr H298:-42.01 kcal/mol
library:CHOFBr_G4 label:F[C]DC(F)C(F)(F)Br smiles:F[C]=C(F)C(F)(F)Br H298:-105.47 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(Br)D[C]F smiles:CC(Br)C(Br)=[C]F H298:23.69 kcal/mol
library:CHOFBr_G4 label:F[C]DCCBr smiles:F[C]=CCBr H298:26.00 kcal/mol
library:CHOFBr_G4 label:CC(Br)CD[C]F smiles:CC(Br)C=[C]F H298:17.76 kcal/mol
library:CHOFBr_G4 label:F[C]DCC(F)CBr smiles:F[C]=CC(F)CBr H298:-26.22 kcal/mol
library:CHOFBr_G4 label:F[C]DCCC(Br)(Br)Br smiles:F[C]=CCC(Br)(Br)Br H298:34.33 kcal/mol
library:CHOFBr_G4 label:F[C]DC(Br)CDC(Br)Br smiles:F[C]=C(Br)C=C(Br)Br H298:63.52 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(Br)D[C]F smiles:O=C(Br)C(Br)=[C]F H298:4.66 kcal/mol
library:CHOFBr_G4 label:F[C]DCC(Br)(Br)Br smiles:F[C]=CC(Br)(Br)Br H298:44.46 kcal/mol
library:CHOFBr_G4 label:F[C]DC(Br)Br smiles:F[C]=C(Br)Br H298:45.01 kcal/mol
library:CHOFBr_G4 label:F[C]DC(CF)C(Br)Br smiles:F[C]=C(CF)C(Br)Br H298:-16.53 kcal/mol
library:CHOFBr_G4 label:F[C]DCOC(F)Br smiles:F[C]=COC(F)Br H298:-48.10 kcal/mol
library:CHOFBr_G4 label:F[C]DC(F)C(Br)(Br)Br smiles:F[C]=C(F)C(Br)(Br)Br H298:6.37 kcal/mol
library:CHOFBr_G4 label:F[C]DC(Br)CC(Br)Br smiles:F[C]=C(Br)CC(Br)Br H298:30.91 kcal/mol
library:CHOFBr_G4 label:OC(D[C]F)C(F)(Br)Br smiles:OC(=[C]F)C(F)(Br)Br H298:-45.23 kcal/mol
library:CHOFBr_G4 label:CDC(Br)C(F)D[C]F smiles:C=C(Br)C(F)=[C]F H298:7.72 kcal/mol
library:CHOFBr_G4 label:F[C]DC(F)C(F)Br smiles:F[C]=C(F)C(F)Br H298:-54.80 kcal/mol
library:CHOFBr_G4 label:F[C]DCC(Br)C(Br)Br smiles:F[C]=CC(Br)C(Br)Br H298:31.13 kcal/mol
library:CHOFBr_G4 label:F[C]DC(CBr)C(F)Br smiles:F[C]=C(CBr)C(F)Br H298:-19.71 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(F)D[C]F smiles:O=C(Br)C(F)=[C]F H298:-40.11 kcal/mol
library:CHOFBr_G4 label:F[C]DCC(F)OBr smiles:F[C]=CC(F)OBr H298:-30.88 kcal/mol
library:CHOFBr_G4 label:F[C]DCC(F)C(F)Br smiles:F[C]=CC(F)C(F)Br H298:-69.71 kcal/mol
library:CHOFBr_G4 label:F[C]DC(Br)C(Br)Br smiles:F[C]=C(Br)C(Br)Br H298:41.14 kcal/mol
library:CHOFBr_G4 label:ODC(Br)CD[C]F smiles:O=C(Br)C=[C]F H298:-3.74 kcal/mol
library:CHOFBr_G4 label:F[C]DCOC(F)(Br)Br smiles:F[C]=COC(F)(Br)Br H298:-38.87 kcal/mol
library:CHOFBr_G4 label:F[C]DC(OBr)C(Br)Br smiles:F[C]=C(OBr)C(Br)Br H298:39.42 kcal/mol
library:CHOFBr_G4 label:F[C]DCOBr smiles:F[C]=COBr H298:31.94 kcal/mol
library:CHOFBr_G4 label:F[C]DC(F)Br smiles:F[C]=C(F)Br H298:-2.68 kcal/mol
library:CHOFBr_G4 label:F[C]DCC(Br)Br smiles:F[C]=CC(Br)Br H298:33.85 kcal/mol
library:CHOFBr_G4 label:CC(D[C]F)OBr smiles:CC(=[C]F)OBr H298:20.14 kcal/mol
library:CHOFBr_G4 label:F[C]DCOC(Br)Br smiles:F[C]=COC(Br)Br H298:7.49 kcal/mol
library:CHOFBr_G4 label:F[C]DC(F)OOBr smiles:F[C]=C(F)OOBr H298:5.44 kcal/mol
library:CHOFBr_G4 label:F[C]DCC(Br)OBr smiles:F[C]=CC(Br)OBr H298:25.34 kcal/mol
library:CHOFBr_G4 label:F[C]DC(Br)C(Br)DCBr smiles:F[C]=C(Br)C(Br)=CBr H298:60.51 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)C(Br)D[C]F smiles:OC(Br)(Br)C(Br)=[C]F H298:0.55 kcal/mol
library:CHOFBr_G4 label:OCC(Br)D[C]F smiles:OCC(Br)=[C]F H298:-10.01 kcal/mol
library:CHOFBr_G4 label:F[C]DC(F)C(F)DCBr smiles:F[C]=C(F)C(F)=CBr H298:-34.11 kcal/mol
library:CHOFBr_G4 label:F[C]DC(F)COBr smiles:F[C]=C(F)COBr H298:-18.48 kcal/mol
library:CHOFBr_G4 label:F[C]DC(F)CBr smiles:F[C]=C(F)CBr H298:-13.84 kcal/mol
library:CHOFBr_G4 label:F[C]DCC(F)(Br)OBr smiles:F[C]=CC(F)(Br)OBr H298:-24.32 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(Br)D[C]F smiles:OC(Br)C(Br)=[C]F H298:-7.33 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(F)D[C]F smiles:CC(Br)C(F)=[C]F H298:-22.14 kcal/mol
library:CHOFBr_G4 label:CDCC(Br)D[C]F smiles:C=CC(Br)=[C]F H298:48.15 kcal/mol
library:CHOFBr_G4 label:F[C]DC(F)CC(F)Br smiles:F[C]=C(F)CC(F)Br H298:-66.37 kcal/mol
library:CHOFBr_G4 label:F[C]DC(OBr)OBr smiles:F[C]=C(OBr)OBr H298:32.33 kcal/mol
library:CHOFBr_G4 label:OC(D[C]F)C(Br)Br smiles:OC(=[C]F)C(Br)Br H298:-3.14 kcal/mol
library:CHOFBr_G4 label:F[C]DCCOBr smiles:F[C]=CCOBr H298:21.06 kcal/mol
library:CHOFBr_G4 label:CC(Br)(Br)C(F)D[C]F smiles:CC(Br)(Br)C(F)=[C]F H298:-14.79 kcal/mol
library:CHOFBr_G4 label:F[C]DCOOBr smiles:F[C]=COOBr H298:47.57 kcal/mol
library:CHOFBr_G4 label:CC(Br)(Br)CD[C]F smiles:CC(Br)(Br)C=[C]F H298:23.69 kcal/mol
library:CHOFBr_G4 label:F[C]DC(Br)CDCBr smiles:F[C]=C(Br)C=CBr H298:54.17 kcal/mol
library:CHOFBr_G4 label:CC(Br)(Br)C(Br)D[C]F smiles:CC(Br)(Br)C(Br)=[C]F H298:30.48 kcal/mol
library:CHOFBr_G4 label:F[C]DC(OBr)C(F)Br smiles:F[C]=C(OBr)C(F)Br H298:-13.04 kcal/mol
library:CHOFBr_G4 label:F[C]DC(F)CDC(Br)Br smiles:F[C]=C(F)C=C(Br)Br H298:17.56 kcal/mol
library:CHOFBr_G4 label:F[C]DC(Br)OCBr smiles:F[C]=C(Br)OCBr H298:6.73 kcal/mol
library:CHOFBr_G4 label:F[C]DC(Br)CCBr smiles:F[C]=C(Br)CCBr H298:24.08 kcal/mol
library:CHOFBr_G4 label:F[C]DC(Br)OC(Br)Br smiles:F[C]=C(Br)OC(Br)Br H298:15.70 kcal/mol
library:CHOFBr_G4 label:F[C]DC(Br)C(Br)OBr smiles:F[C]=C(Br)C(Br)OBr H298:34.32 kcal/mol
library:CHOFBr_G4 label:F[C]DCC(F)(F)CBr smiles:F[C]=CC(F)(F)CBr H298:-79.60 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)C(F)D[C]F smiles:CC(F)(Br)C(F)=[C]F H298:-67.43 kcal/mol
library:CHOFBr_G4 label:OC(D[C]F)C(F)(F)Br smiles:OC(=[C]F)C(F)(F)Br H298:-103.72 kcal/mol
library:CHOFBr_G4 label:F[C]DCCDC(Br)Br smiles:F[C]=CC=C(Br)Br H298:54.27 kcal/mol
library:CHOFBr_G4 label:F[C]DC(CF)CBr smiles:F[C]=C(CF)CBr H298:-25.48 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)CD[C]F smiles:CC(F)(Br)C=[C]F H298:-28.82 kcal/mol
library:CHOFBr_G4 label:F[C]DCC(Br)(Br)CBr smiles:F[C]=CC(Br)(Br)CBr H298:31.30 kcal/mol
library:CHOFBr_G4 label:F[C]DC(CBr)OBr smiles:F[C]=C(CBr)OBr H298:28.26 kcal/mol
library:CHOFBr_G4 label:F[C]DCC(F)Br smiles:F[C]=CC(F)Br H298:-17.91 kcal/mol
library:CHOFBr_G4 label:F[C]DCC(Br)DC(Br)Br smiles:F[C]=CC(Br)=C(Br)Br H298:61.60 kcal/mol
library:CHOFBr_G4 label:F[C]DC(F)OC(F)Br smiles:F[C]=C(F)OC(F)Br H298:-90.28 kcal/mol
library:CHOFBr_G4 label:F[C]DC(Br)CBr smiles:F[C]=C(Br)CBr H298:32.10 kcal/mol
library:CHOFBr_G4 label:CC(Br)D[C]F smiles:CC(Br)=[C]F H298:24.55 kcal/mol
library:CHOFBr_G4 label:F[C]DCC(F)DCBr smiles:F[C]=CC(F)=CBr H298:3.50 kcal/mol
library:CHOFBr_G4 label:F[C]DCBr smiles:F[C]=CBr H298:34.35 kcal/mol
library:CHOFBr_G4 label:F[C]DC(F)C(Br)OBr smiles:F[C]=C(F)C(Br)OBr H298:-11.90 kcal/mol
library:CHOFBr_G4 label:F[C]DC(F)OC(Br)Br smiles:F[C]=C(F)OC(Br)Br H298:-33.01 kcal/mol
library:CHOFBr_G4 label:CCC(Br)D[C]F smiles:CCC(Br)=[C]F H298:19.21 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)C(F)D[C]F smiles:OC(Br)(Br)C(F)=[C]F H298:-44.52 kcal/mol
library:CHOFBr_G4 label:OC(D[C]F)C(F)Br smiles:OC(=[C]F)C(F)Br H298:-53.53 kcal/mol
library:CHOFBr_G4 label:F[C]DC(F)C(F)CBr smiles:F[C]=C(F)C(F)CBr H298:-65.66 kcal/mol
""",
)

entry(
    index = 403,
    label = "CdsJO",
    group = 
"""
1 * CO  u1 {2,D}
2   O2d u0 {1,D}
""",
    thermo = 'CCJ=O',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 404,
    label = "COBr1sO2d",
    group = 
"""
1 * CO   u1 {2,S} {3,D}
2   Br1s u0 {1,S}
3   O2d  u0 {1,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 405,
    label = "COCl1sO2d",
    group = 
"""
1 * CO   u1 {2,S} {3,D}
2   Cl1s u0 {1,S}
3   O2d  u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.174031,-0.863816,-1.52171,-2.09023,-2.99954,-3.66182,-4.61006],'cal/(mol*K)','+|-',[0.988423,1.01486,0.951553,0.888774,0.784361,0.686374,0.502715]),
        H298 = (90.9819,'kcal/mol','+|-',1.579),
        S298 = (1.16039,'cal/(mol*K)','+|-',2.68344),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:ATcT_halogens label:Chloroformyl smiles:O=[C]Cl H298:-4.91 kcal/mol
""",
)

entry(
    index = 406,
    label = "COF1sO2d",
    group = 
"""
1 * CO  u1 {2,S} {3,D}
2   F1s u0 {1,S}
3   O2d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.402717,-0.899898,-1.45939,-2.01242,-2.89452,-3.54367,-4.54736],'cal/(mol*K)','+|-',[0.988423,1.01486,0.951553,0.888774,0.784361,0.686374,0.502715]),
        H298 = (101.384,'kcal/mol','+|-',1.579),
        S298 = (0.552887,'cal/(mol*K)','+|-',2.68344),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:ATcT_halogens label:Fluoroformyl smiles:O=[C]F H298:-42.07 kcal/mol
""",
)

entry(
    index = 407,
    label = "COJ-NOd",
    group = 
"""
1 * CO  u1 {2,S} {3,D}
2   N   u0 {1,S}
3   O2d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.499049,-2.566,-5.4926,-8.03919,-12.3239,-15.6108,-20.2366],'J/(mol*K)'),
        H298 = (352.267,'kJ/mol'),
        S298 = (5.58481,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 408,
    label = "HCdsJO",
    group = 
"""
1 * CO  u1 {2,D} {3,S}
2   O2d u0 {1,D}
3   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.19,-0.65,-1.19,-1.73,-2.63,-3.32,-4.42],'cal/(mol*K)'),
        H298 = (88.45,'kcal/mol'),
        S298 = (-0.01,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated in relation to formaldehyde from NIST values""",
    longDesc = 
"""

""",
)

entry(
    index = 409,
    label = "CCJ=O",
    group = 
"""
1 * CO  u1 {2,D} {3,S}
2   O2d u0 {1,D}
3   C   u0 {1,S}
""",
    thermo = 'CsCJ=O',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 410,
    label = "CC(C)CJ=O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S}
2 * CO  u1 {1,S} {5,D}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.1,-5.8,-7.9,-9.9,-13.5,-16.2,-20.3],'J/(mol*K)'),
        H298 = (376.2,'kJ/mol'),
        S298 = (6.7,'J/(mol*K)'),
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
    index = 411,
    label = "CC(C)2CJ=O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * CO  u1 {1,S} {6,D}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.7,-5,-7.4,-9.6,-13.1,-15.6,-19.9],'J/(mol*K)'),
        H298 = (373.3,'kJ/mol'),
        S298 = (7.5,'J/(mol*K)'),
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
    index = 412,
    label = "CC(C)(C=O)CJ=O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * CO  u1 {1,S} {6,D}
3   CO  u0 {1,S} {7,D}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.7,-4,-5.4,-7.2,-10.9,-13.9,-18.6],'J/(mol*K)'),
        H298 = (375.2,'kJ/mol'),
        S298 = (10.4,'J/(mol*K)'),
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
    index = 413,
    label = "C=CC(C)(C=O)CJ=O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * CO  u1 {1,S} {7,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   C   u0 {1,S}
6   C   u0 {4,D}
7   O2d u0 {2,D}
8   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.5,2.6,-2.4,-6.5,-12,-15.3,-19.7],'J/(mol*K)'),
        H298 = (373.6,'kJ/mol'),
        S298 = (1.2,'J/(mol*K)'),
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
    index = 414,
    label = "C=CC(C)2CJ=O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * CO  u1 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   C   u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.5,-4.2,-7,-9.3,-12.8,-15.4,-19.4],'J/(mol*K)'),
        H298 = (371.9,'kJ/mol'),
        S298 = (10.6,'J/(mol*K)'),
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
    index = 415,
    label = "CC(C)(O)CJ=O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * CO  u1 {1,S} {6,D}
3   C   u0 {1,S}
4   O2s u0 {1,S}
5   C   u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.9,-2.6,-5.6,-8.1,-12,-14.9,-19.6],'J/(mol*K)'),
        H298 = (374.9,'kJ/mol'),
        S298 = (6.8,'J/(mol*K)'),
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
    index = 416,
    label = "C=CC(C)(O)CJ=O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * CO  u1 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   O2s u0 {1,S}
5   C   u0 {1,S}
6   C   u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1,-4.5,-7.4,-9.7,-12.7,-15.1,-19.5],'J/(mol*K)'),
        H298 = (375.3,'kJ/mol'),
        S298 = (8.7,'J/(mol*K)'),
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
    index = 417,
    label = "CCCJ=O",
    group = 
"""
1 * CO  u1 {2,S} {4,D}
2   C   u0 {1,S} {3,S}
3   C   u0 {2,S}
4   O2d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.7,-3.9,-7,-9.9,-14.5,-17.5,-21.4],'J/(mol*K)'),
        H298 = (378,'kJ/mol'),
        S298 = (8.3,'J/(mol*K)'),
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
    index = 418,
    label = "C=OCCJ=O",
    group = 
"""
1   C   u0 {2,S} {3,S}
2 * CO  u1 {1,S} {4,D}
3   CO  u0 {1,S} {5,D}
4   O2d u0 {2,D}
5   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.2,1.4,-2.8,-6.4,-12,-15.8,-20.4],'J/(mol*K)'),
        H298 = (379.4,'kJ/mol'),
        S298 = (0.8,'J/(mol*K)'),
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
    index = 419,
    label = "C=OC=OCJ=O",
    group = 
"""
1   CO  u0 {2,S} {3,S} {4,D}
2 * CO  u1 {1,S} {5,D}
3   CO  u0 {1,S} {6,D}
4   O2d u0 {1,D}
5   O2d u0 {2,D}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.2,-4.6,-4.4,-4.5,-4.9,-5.7,-7.8],'J/(mol*K)'),
        H298 = (330.2,'kJ/mol'),
        S298 = (-19.6,'J/(mol*K)'),
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
    index = 420,
    label = "C=C(C)CJ=O",
    group = 
"""
1   Cd  u0 {2,S} {3,S} {4,D}
2 * CO  u1 {1,S} {5,D}
3   C   u0 {1,S}
4   C   u0 {1,D}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-3.8,-6.4,-8.8,-12.5,-15.3,-19.5],'J/(mol*K)'),
        H298 = (381.7,'kJ/mol'),
        S298 = (6.7,'J/(mol*K)'),
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
    index = 421,
    label = "CsCJ=O",
    group = 
"""
1 * CO  u1 {2,D} {3,S}
2   O2d u0 {1,D}
3   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.83,-1.43,-1.96,-2.42,-3.16,-3.73,-4.64],'cal/(mol*K)'),
        H298 = (89,'kcal/mol'),
        S298 = (1.12,'cal/(mol*K)'),
    ),
    shortDesc = """CHEN & BOZZELLI #""",
    longDesc = 
"""

""",
)

entry(
    index = 422,
    label = "C=CCJ=O",
    group = 
"""
1 * CO  u1 {2,S} {3,D}
2   Cd  u0 {1,S} {4,D}
3   O2d u0 {1,D}
4   Cd  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.3,2.5,-1.1,-4.5,-9.9,-13.7,-18.9],'J/(mol*K)'),
        H298 = (379.9,'kJ/mol'),
        S298 = (7.2,'J/(mol*K)'),
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
    index = 423,
    label = "OC=OCJ=O",
    group = 
"""
1   CO  u0 {2,S} {3,S} {4,D}
2 * CO  u1 {1,S} {5,D}
3   O2s u0 {1,S}
4   O2d u0 {1,D}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3,-4.7,-7,-9.5,-14,-17.2,-21.1],'J/(mol*K)'),
        H298 = (376.2,'kJ/mol'),
        S298 = (4.6,'J/(mol*K)'),
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
    index = 424,
    label = "(O)CJO",
    group = 
"""
1 * CO  u1 {2,D} {3,S}
2   O2d u0 {1,D}
3   O2s u0 {1,S}
""",
    thermo = '(O)CJOC',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 425,
    label = "(O)CJOH",
    group = 
"""
1 * CO  u1 {2,S} {3,D}
2   O2s u0 {1,S} {4,S}
3   O2d u0 {1,D}
4   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.02,-0.66,-1.4,-2.12,-3.41,-4.44,-5.79],'cal/(mol*K)'),
        H298 = (100.75,'kcal/mol'),
        S298 = (0.78,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN #""",
    longDesc = 
"""

""",
)

entry(
    index = 426,
    label = "(O)CJOC",
    group = 
"""
1 * CO  u1 {2,S} {3,D}
2   O2s u0 {1,S} {4,S}
3   O2d u0 {1,D}
4   C   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.2,-0.2,-3.5,-6.5,-10.9,-13.6,-17],'J/(mol*K)'),
        H298 = (415.2,'kJ/mol'),
        S298 = (-4.3,'J/(mol*K)'),
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
    index = 427,
    label = "(O)CJOCH3",
    group = 
"""
1   Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   O2s u0 {1,S} {3,S}
3 * CO  u1 {2,S} {7,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.51,-0.11,-0.94,-1.8,-3.34,-4.48,-5.79],'cal/(mol*K)'),
        H298 = (100.1,'kcal/mol'),
        S298 = (0.72,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 428,
    label = "(O)CJOCC",
    group = 
"""
1   Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   O2s u0 {1,S} {3,S}
3 * CO  u1 {2,S} {7,D}
4   C   u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.45,-0.13,-0.98,-1.86,-3.43,-4.56,-5.79],'cal/(mol*K)'),
        H298 = (99.49,'kcal/mol'),
        S298 = (0.55,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN (values from (O)CJOCH2CH3)""",
    longDesc = 
"""

""",
)

entry(
    index = 429,
    label = "(O)CJOCC2",
    group = 
"""
1   Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   O2s u0 {1,S} {3,S}
3 * CO  u1 {2,S} {7,D}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   H   u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.74,-0.06,-1.04,-2.01,-3.6,-4.66,-5.77],'cal/(mol*K)'),
        H298 = (98.99,'kcal/mol'),
        S298 = (0.82,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN (values from (O)CJOCH(CH3)2)""",
    longDesc = 
"""

""",
)

entry(
    index = 430,
    label = "(O)CJOCC3",
    group = 
"""
1   Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   O2s u0 {1,S} {3,S}
3 * CO  u1 {2,S} {7,D}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   C   u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.11,-0.79,-1.8,-2.73,-4.17,-5.06,-5.87],'cal/(mol*K)'),
        H298 = (97.98,'kcal/mol'),
        S298 = (0.76,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN (values from (O)CJOC(CH3)3)""",
    longDesc = 
"""

""",
)

entry(
    index = 431,
    label = "SCJ=O",
    group = 
"""
1 * CO  u1 {2,D} {3,S}
2   O2d u0 {1,D}
3   S   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.3,-0.86,-1.5,-2.06,-2.99,-3.68,-4.7],'cal/(mol*K)'),
        H298 = (86.68,'kcal/mol'),
        S298 = (-1.02,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 432,
    label = "Cds_P",
    group = 
"""
1 * Cd u1 {2,D} {3,S}
2   C  u0 {1,D}
3   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.19,-0.75,-1.36,-1.92,-2.82,-3.49,-4.53],'cal/(mol*K)'),
        H298 = (111.2,'kcal/mol'),
        S298 = (1.39,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
"""

""",
)

entry(
    index = 433,
    label = "C=C=CJ",
    group = 
"""
1 * Cd  u1 {2,D} {3,S}
2   Cdd u0 {1,D} {4,D}
3   H   u0 {1,S}
4   C   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.45,-1.05,-1.64,-2.15,-2.98,-3.6,-3.6],'cal/(mol*K)'),
        H298 = (89,'kcal/mol'),
        S298 = (1.29,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 434,
    label = "N=C=CJ",
    group = 
"""
1 * Cd  u1 {2,D} {3,S}
2   Cdd u0 {1,D} {4,D}
3   H   u0 {1,S}
4   N   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.92302,-3.87776,-5.86459,-7.91273,-11.031,-13.2669,-16.8954],'J/(mol*K)'),
        H298 = (369.234,'kJ/mol'),
        S298 = (-5.93117,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 435,
    label = "Cds_S",
    group = 
"""
1 * Cd u1 {2,D} {3,S}
2   C  u0 {1,D}
3   C  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (109,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
"""

""",
)

entry(
    index = 436,
    label = "C=CJC=O",
    group = 
"""
1 * Cd  u1 {2,S} {3,D}
2   CO  u0 {1,S} {4,D}
3   C   u0 {1,D}
4   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.4,-2.2,-4.8,-7.2,-11.6,-15.5,-22],'J/(mol*K)'),
        H298 = (462.3,'kJ/mol'),
        S298 = (9.6,'J/(mol*K)'),
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
    index = 437,
    label = "C=CJC=C",
    group = 
"""
1 * Cd      u1 {2,D} {3,S}
2   Cd      u0 {1,D}
3   [Cd,CO] u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.19,-0.76,-1.51,-2.01,-2.7,-3.17,-3.17],'cal/(mol*K)'),
        H298 = (99.8,'kcal/mol'),
        S298 = (0.71,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 438,
    label = "cyclobutadiene-C1",
    group = 
"""
1 * Cd u1 {2,D} {4,S}
2   Cd u0 {1,D} {3,S}
3   Cd u0 {2,S} {4,D}
4   Cd u0 {1,S} {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (104.6,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
"""

""",
)

entry(
    index = 439,
    label = "bicyclo[2.2.0]hexa-1(4),2,5-triene-C2",
    group = 
"""
1   Cd u0 {2,D} {3,S} {6,S}
2   Cd u0 {1,D} {4,S} {5,S}
3 * Cd u1 {1,S} {4,D}
4   Cd u0 {2,S} {3,D}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (102.9,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
"""

""",
)

entry(
    index = 440,
    label = "1,3-cyclopentadiene-vinyl-2",
    group = 
"""
1   C  u0 {2,S} {3,S}
2   Cd u0 {1,S} {4,D}
3   Cd u0 {1,S} {5,D}
4 * Cd u1 {2,D} {5,S}
5   Cd u0 {3,D} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (116.2,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
"""

""",
)

entry(
    index = 441,
    label = "cyclopropenyl-vinyl",
    group = 
"""
1   C  u0 {2,S} {3,S}
2 * Cd u1 {1,S} {3,D}
3   Cd u0 {1,S} {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (106.7,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = """Fattahi, A.; McCarthy, R. E.; Ahmad, M. R.; Kass, S. R., "Why Does Cyclopropene Have the Acidity of an Acetylene but the Bond Energy of Methane?," J. Am. Chem. Soc. 2003, 125, 11746-11750, DOI: 10.1021/ja035725s. S, Cp copied from Cds_S""",
    longDesc = 
"""

""",
)

entry(
    index = 442,
    label = "cyclobutene-vinyl",
    group = 
"""
1   C  u0 {2,S} {4,S}
2   C  u0 {1,S} {3,S}
3 * Cd u1 {2,S} {4,D}
4   Cd u0 {1,S} {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (112.5,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = """Tian, Z.; Fattahi, A.; Lis, L.; Kass, S. R., "Cycloalkane and Cycloalkene C-H Bond Dissociation Energies," J. Am. Chem. Soc. 2006, 128, 17087-17092, DOI: 10.1021/ja065348u S, Cp copied from Cds_S""",
    longDesc = 
"""

""",
)

entry(
    index = 443,
    label = "bicyclo[2.1.0]pent-2-ene-C2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   C  u0 {1,S} {2,S}
4 * Cd u1 {2,S} {5,D}
5   Cd u0 {1,S} {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (109.8,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
"""

""",
)

entry(
    index = 444,
    label = "tricyclo[2.1.1.0(1,4)]hex-2-ene-C2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {6,S}
2   Cs u0 {1,S} {3,S} {4,S} {5,S}
3   C  u0 {1,S} {2,S}
4   C  u0 {1,S} {2,S}
5 * Cd u1 {2,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (108.6,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
"""

""",
)

entry(
    index = 445,
    label = "bicyclo[2.2.0]hexa-2,5-diene-C2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S}
3 * Cd u1 {1,S} {4,D}
4   Cd u0 {2,S} {3,D}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (111.6,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
"""

""",
)

entry(
    index = 446,
    label = "cyclopentene-vinyl",
    group = 
"""
1   C  u0 {2,S} {3,S}
2   C  u0 {1,S} {5,S}
3   C  u0 {1,S} {4,S}
4 * Cd u1 {3,S} {5,D}
5   Cd u0 {2,S} {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (113.7,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
"""

""",
)

entry(
    index = 447,
    label = "bicyclo[2.1.1]hex-2-ene-C2",
    group = 
"""
1   Cs u0 {3,S} {4,S} {6,S}
2   Cs u0 {3,S} {4,S} {5,S}
3   C  u0 {1,S} {2,S}
4   C  u0 {1,S} {2,S}
5 * Cd u1 {2,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (115.9,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
"""

""",
)

entry(
    index = 448,
    label = "1,3-cyclopentadiene-vinyl-1",
    group = 
"""
1   C  u0 {2,S} {3,S}
2 * Cd u1 {1,S} {4,D}
3   Cd u0 {1,S} {5,D}
4   Cd u0 {2,D} {5,S}
5   Cd u0 {3,D} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (116.9,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
"""

""",
)

entry(
    index = 449,
    label = "CCCJ=C=O",
    group = 
"""
1 * Cd  u1 {2,S} {3,D}
2   C   u0 {1,S} {4,S}
3   Cdd u0 {1,D} {5,D}
4   C   u0 {2,S}
5   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.6,-3,-4.9,-6.5,-9.4,-11.6,-15.1],'J/(mol*K)'),
        H298 = (420.2,'kJ/mol'),
        S298 = (-2.3,'J/(mol*K)'),
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
    index = 450,
    label = "CC(C)CJ=C=O",
    group = 
"""
1   Cs  u0 {2,S} {4,S} {5,S}
2 * Cd  u1 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.8,-3.6,-6,-7.8,-10.6,-12.6,-15.8],'J/(mol*K)'),
        H298 = (424,'kJ/mol'),
        S298 = (1.7,'J/(mol*K)'),
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
    index = 451,
    label = "C=C(C)CJ=C=O",
    group = 
"""
1   Cd  u0 {2,S} {4,D} {5,S}
2 * Cd  u1 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   C   u0 {1,D}
5   C   u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-11.5,-13.7,-14.6,-15,-15.7,-16.3,-17.8],'J/(mol*K)'),
        H298 = (404,'kJ/mol'),
        S298 = (5.6,'J/(mol*K)'),
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
    index = 452,
    label = "OC=CJCb",
    group = 
"""
1 * Cd  u1 {2,D} {3,S}
2   C   u0 {1,D} {4,S}
3   Cb  u0 {1,S}
4   O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.047,0.607,0.374,-0.3,-1.28,-1.972,-3.196],'cal/(mol*K)'),
        H298 = (123.797,'kcal/mol'),
        S298 = (2.661,'cal/(mol*K)'),
    ),
    shortDesc = """Fit to CCSD(T)-F12/cc-pVDZ-F12//M06/vtz calculations""",
    longDesc = 
"""
Fit to CCSD(T)-F12/cc-pVDZ-F12//M06/vtz calculations for OC=[C]c1ccccc1
""",
)

entry(
    index = 453,
    label = "N=C=CJC",
    group = 
"""
1 * Cd u1 {2,D} {3,S}
2   C  u0 {1,D} {4,D}
3   C  u0 {1,S}
4   N  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.07662,-4.81991,-7.34354,-9.45507,-12.8991,-15.5773,-19.5204],'J/(mol*K)'),
        H298 = (345.84,'kJ/mol'),
        S298 = (0.774208,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 454,
    label = "S2s-CJ=C",
    group = 
"""
1 * Cd  u1 {2,S} {3,D}
2   S2s u0 {1,S}
3   C   u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.16,-0.48,-1.16,-1.76,-2.68,-3.35,-4.45],'cal/(mol*K)'),
        H298 = (104.73,'kcal/mol'),
        S298 = (0.37,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 455,
    label = "C=CJO",
    group = 
"""
1 * Cd  u1 {2,D} {3,S}
2   C   u0 {1,D}
3   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.1,-11.8,-15.2,-17.2,-19.2,-20.3,-22],'J/(mol*K)'),
        H298 = (457.4,'kJ/mol'),
        S298 = (26.7,'J/(mol*K)'),
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
    index = 456,
    label = "CdJ-NN",
    group = 
"""
1 * Cd u1 {2,S} {3,D}
2   N  u0 {1,S}
3   N  u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.97657,-2.2041,-5.32888,-7.99133,-12.3333,-15.391,-19.6103],'J/(mol*K)'),
        H298 = (404.968,'kJ/mol'),
        S298 = (8.19458,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 457,
    label = "CdJ-CdN",
    group = 
"""
1 * Cd u1 {2,S} {3,D}
2   N  u0 {1,S}
3   C  u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.18369,-4.23173,-7.03311,-9.35183,-12.8111,-15.2187,-18.7271],'J/(mol*K)'),
        H298 = (445.085,'kJ/mol'),
        S298 = (5.80115,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 458,
    label = "CdJ-CddN",
    group = 
"""
1 * Cd  u1 {2,S} {3,D}
2   N   u0 {1,S}
3   Cdd u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.3921,-2.08105,-5.04651,-7.48487,-11.2668,-13.9403,-17.7653],'J/(mol*K)'),
        H298 = (371.87,'kJ/mol'),
        S298 = (2.60652,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 459,
    label = "CdJ-NdO",
    group = 
"""
1 * Cd u1 {2,S} {3,D}
2   O  u0 {1,S}
3   N  u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.33945,-1.92324,-6.02047,-9.57875,-15.2601,-19.0789,-23.7518],'J/(mol*K)'),
        H298 = (437.007,'kJ/mol'),
        S298 = (7.57533,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 460,
    label = "CdJ-NdC",
    group = 
"""
1 * Cd u1 {2,S} {3,D}
2   C  u0 {1,S}
3   N  u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.00763889,-2.36896,-5.21801,-7.8464,-11.991,-15.0452,-19.5882],'J/(mol*K)'),
        H298 = (431.362,'kJ/mol'),
        S298 = (4.60475,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 461,
    label = "CdJ-HN3d",
    group = 
"""
1 * Cd  u1 {2,S} {3,D}
2   H   u0 {1,S}
3   N3d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.535181,-3.60589,-6.39413,-8.86095,-12.7727,-15.5717,-19.8329],'J/(mol*K)'),
        H298 = (415.298,'kJ/mol'),
        S298 = (5.57767,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 462,
    label = "CdJ-H(N3dOs)",
    group = 
"""
1 * Cd  u1 {2,D} {3,S}
2   N3d u0 {1,D} {4,S}
3   H   u0 {1,S}
4   O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.72438,-0.600728,-4.42251,-7.70232,-13.0613,-16.7127,-21.0715],'J/(mol*K)'),
        H298 = (440.68,'kJ/mol'),
        S298 = (7.40719,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 463,
    label = "CdJ-H(N3dCO)",
    group = 
"""
1   N3d u0 {2,D} {3,S}
2 * Cd  u1 {1,D} {4,S}
3   CO  u0 {1,S} {5,D}
4   H   u0 {2,S}
5   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.19479,-3.60166,-4.82249,-6.06327,-8.74387,-11.0941,-15.1265],'J/(mol*K)'),
        H298 = (411.286,'kJ/mol'),
        S298 = (-2.27887,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 464,
    label = "CdJ-H(N3dN3d)",
    group = 
"""
1 * Cd  u1 {2,D} {3,S}
2   N3d u0 {1,D} {4,S}
3   H   u0 {1,S}
4   N3d u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.175838,-2.38908,-4.71217,-6.73125,-10.4295,-13.5563,-18.2391],'J/(mol*K)'),
        H298 = (426.882,'kJ/mol'),
        S298 = (5.53135,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 465,
    label = "CdJ-H(N3dCd)",
    group = 
"""
1 * Cd       u1 {2,D} {3,S}
2   N3d      u0 {1,D} {4,S}
3   H        u0 {1,S}
4   [Cd,Cdd] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.23929,-2.28161,-6.55411,-9.87574,-14.8878,-18.2186,-21.9295],'J/(mol*K)'),
        H298 = (422.544,'kJ/mol'),
        S298 = (13.1379,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 466,
    label = "CdJ-HN5dc",
    group = 
"""
1 * Cd   u1 {2,S} {3,D}
2   H    u0 {1,S}
3   N5dc u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.58018,-0.431227,-3.62097,-6.67779,-11.585,-15.0896,-19.8118],'J/(mol*K)'),
        H298 = (490.037,'kJ/mol'),
        S298 = (7.65582,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 467,
    label = "CtJ",
    group = 
"""
1 * Ct u1 {2,T}
2   Ct u0 {1,T}
""",
    thermo = 'Acetyl',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 468,
    label = "Acetyl",
    group = 
"""
1   Ct u0 {2,T} {3,S}
2 * Ct u1 {1,T}
3   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.51,-1.56,-2.27,-2.78,-3.47,-3.97,-3.97],'cal/(mol*K)'),
        H298 = (132.7,'kcal/mol'),
        S298 = (2.11,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 469,
    label = "CbJ",
    group = 
"""
1 * Cb u1 {2,B} {3,B}
2   C  u0 {1,B}
3   C  u0 {1,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.41,-1.18,-1.93,-2.69,-3.75,-4.48,-5.24],'cal/(mol*K)'),
        H298 = (113,'kcal/mol'),
        S298 = (1.48,'cal/(mol*K)'),
    ),
    shortDesc = """BDE from TSANG, S and Cp from THERM""",
    longDesc = 
"""

""",
)

entry(
    index = 470,
    label = "C=SJ",
    group = 
"""
1 * CS  u1 {2,D}
2   S2d u0 p2 {1,D}
""",
    thermo = 'C=SJ-H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 471,
    label = "C=SJ-S2s",
    group = 
"""
1 * CS  u1 {2,S} {3,D}
2   S2s u0 p2 {1,S}
3   S2d u0 p2 {1,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 472,
    label = "C=SJ-H",
    group = 
"""
1 * CS  u1 {2,S} {3,D}
2   H   u0 {1,S}
3   S2d u0 p2 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.31,-0.88,-1.47,-1.99,-2.85,-3.49,-4.52],'cal/(mol*K)'),
        H298 = (92.39,'kcal/mol'),
        S298 = (-0.14,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 473,
    label = "C=SJ-C",
    group = 
"""
1 * CS  u1 {2,S} {3,D}
2   C   u0 {1,S}
3   S2d u0 p2 {1,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 474,
    label = "C=SJ-Cd",
    group = 
"""
1 * CS  u1 {2,S} {3,D}
2   Cd  u0 {1,S}
3   S2d u0 p2 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.21,-1.76,-2.24,-2.65,-3.3,-3.81,-4.67],'cal/(mol*K)'),
        H298 = (77.87,'kcal/mol'),
        S298 = (0.48,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 475,
    label = "C=SJ-Cs",
    group = 
"""
1 * CS  u1 {2,S} {3,D}
2   Cs  u0 {1,S}
3   S2d u0 p2 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.2,-1.8,-2.25,-2.63,-3.24,-3.74,-4.64],'cal/(mol*K)'),
        H298 = (91.94,'kcal/mol'),
        S298 = (0.65,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 476,
    label = "OJ",
    group = 
"""
1 * O u1
""",
    thermo = 'COJ',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 477,
    label = "HOJ",
    group = 
"""
1 * O2s u1 {2,S}
2   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.87,-1.1,-1.36,-1.62,-2.11,-2.53,-3.38],'cal/(mol*K)'),
        H298 = (119.22,'kcal/mol'),
        S298 = (-2.6,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated from NIST values for H2O, OH and H""",
    longDesc = 
"""

""",
)

entry(
    index = 478,
    label = "COJ",
    group = 
"""
1 * O2s u1 {2,S}
2   C   ux {1,S}
""",
    thermo = 'CsOJ',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 479,
    label = "CCOJ",
    group = 
"""
1   C   u0 {2,S} {3,S}
2 * O2s u1 {1,S}
3   C   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.1,-12.2,-14.4,-15.1,-14.7,-14.5,-15.6],'J/(mol*K)'),
        H298 = (442.9,'kJ/mol'),
        S298 = (3.8,'J/(mol*K)'),
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
    index = 480,
    label = "C=OCOJ",
    group = 
"""
1   C   u0 {2,S} {3,S}
2   CO  u0 {1,S} {4,D}
3 * O2s u1 {1,S}
4   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.6,-9.3,-11.5,-13.2,-15,-16,-17.5],'J/(mol*K)'),
        H298 = (461,'kJ/mol'),
        S298 = (2.6,'J/(mol*K)'),
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
    index = 481,
    label = "C=CC(C)(C=O)OJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4 * O2s u1 {1,S}
5   C   u0 {1,S}
6   C   u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.5,-11.3,-14.6,-16.2,-17.2,-17.4,-18.4],'J/(mol*K)'),
        H298 = (462.1,'kJ/mol'),
        S298 = (10.4,'J/(mol*K)'),
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
    index = 482,
    label = "CC(C)(C=O)OJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3 * O2s u1 {1,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.6,-13.9,-16.3,-17.5,-18.4,-18.8,-19.1],'J/(mol*K)'),
        H298 = (459.1,'kJ/mol'),
        S298 = (16.3,'J/(mol*K)'),
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
    index = 483,
    label = "C=OC=OOJ",
    group = 
"""
1   CO  u0 {2,S} {3,S} {4,D}
2   CO  u0 {1,S} {5,D}
3 * O2s u1 {1,S}
4   O2d u0 {1,D}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.1,-6.8,-10.1,-13,-17.5,-20.9,-25.9],'J/(mol*K)'),
        H298 = (479.5,'kJ/mol'),
        S298 = (16,'J/(mol*K)'),
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
    index = 484,
    label = "CC(C)OJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S}
2 * O2s u1 {1,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.3,-6.3,-7.3,-8.3,-9.8,-11.2,-14.2],'J/(mol*K)'),
        H298 = (447.6,'kJ/mol'),
        S298 = (-6.8,'J/(mol*K)'),
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
    index = 485,
    label = "CC(C)2OJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * O2s u1 {1,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.2,-7.9,-9,-9.9,-10.7,-11.7,-14.6],'J/(mol*K)'),
        H298 = (446.1,'kJ/mol'),
        S298 = (-4.6,'J/(mol*K)'),
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
    index = 486,
    label = "C=CC(C)2OJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3 * O2s u1 {1,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   C   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.9,-12.1,-12.9,-12.9,-12.6,-12.9,-14.8],'J/(mol*K)'),
        H298 = (445.9,'kJ/mol'),
        S298 = (2.7,'J/(mol*K)'),
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
    index = 487,
    label = "CC(C)(O)OJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * O2s u1 {1,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-11.8,-18.8,-22.1,-22.3,-19.5,-17.2,-16],'J/(mol*K)'),
        H298 = (449,'kJ/mol'),
        S298 = (8,'J/(mol*K)'),
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
    index = 488,
    label = "C=CC(C)(O)OJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3 * O2s u1 {1,S}
4   C   u0 {1,S}
5   O2s u0 {1,S}
6   C   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.2,-12.5,-16.7,-19.1,-20.1,-19.4,-18.2],'J/(mol*K)'),
        H298 = (450.7,'kJ/mol'),
        S298 = (8.5,'J/(mol*K)'),
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
    index = 489,
    label = "C=C(C)OJ",
    group = 
"""
1   Cd  u0 {2,S} {3,D} {4,S}
2 * O2s u1 {1,S}
3   C   u0 {1,D}
4   C   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.2,-13.1,-15.6,-17,-17.7,-17.6,-17.6],'J/(mol*K)'),
        H298 = (354.8,'kJ/mol'),
        S298 = (7.4,'J/(mol*K)'),
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
    index = 490,
    label = "CdsOJ",
    group = 
"""
1 * O2s     u1 {2,S}
2   [Cd,CO] u0 {1,S}
""",
    thermo = 'RC=COJ',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 491,
    label = "RC=COJ",
    group = 
"""
1 * O2s u1 {2,S}
2   Cd  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.34,-1.99,-2.48,-2.79,-3.13,-3.33,-3.79],'cal/(mol*K)'),
        H298 = (88,'kcal/mol'),
        S298 = (-1.11,'cal/(mol*K)'),
    ),
    shortDesc = """CHEN & BOZZELLI""",
    longDesc = 
"""

""",
)

entry(
    index = 492,
    label = "C=COJ",
    group = 
"""
1   Cd  u0 {2,S} {3,D}
2 * O2s u1 {1,S}
3   C   u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10.1,-13.5,-14.6,-14.6,-14.3,-14.5,-16],'J/(mol*K)'),
        H298 = (358.1,'kJ/mol'),
        S298 = (3.3,'J/(mol*K)'),
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
    index = 493,
    label = "N=COJ",
    group = 
"""
1   Cd  u0 {2,S} {3,D}
2 * O2s u1 {1,S}
3   N   u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.58496,-8.79662,-8.0527,-8.55566,-10.0922,-11.8503,-16.2634],'J/(mol*K)'),
        H298 = (158.992,'kJ/mol'),
        S298 = (-7.51805,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 494,
    label = "OJC=O",
    group = 
"""
1   CO  u0 {2,S} {3,D}
2 * O2s u1 {1,S}
3   O2d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.31,-1.87,-2.32,-2.69,-3.28,-3.74,-4.56],'cal/(mol*K)'),
        H298 = (104,'kcal/mol'),
        S298 = (0.79,'cal/(mol*K)'),
    ),
    shortDesc = """CHEN & BOZZELLI""",
    longDesc = 
"""

""",
)

entry(
    index = 495,
    label = "OC=OOJ",
    group = 
"""
1   CO  u0 {2,S} {3,S} {4,D}
2 * O2s u1 {1,S}
3   O2s u0 {1,S}
4   O2d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.5,-13.1,-16.3,-18.3,-20.4,-21.2,-21.4],'J/(mol*K)'),
        H298 = (460.9,'kJ/mol'),
        S298 = (6,'J/(mol*K)'),
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
    index = 496,
    label = "OCOJ",
    group = 
"""
1   C   u0 {2,S} {3,S}
2 * O2s u1 {1,S}
3   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10.9,-17.5,-19.8,-19.3,-16.2,-14.3,-14.3],'J/(mol*K)'),
        H298 = (444.4,'kJ/mol'),
        S298 = (0.8,'J/(mol*K)'),
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
    index = 497,
    label = "SCOJ",
    group = 
"""
1   C   ux {2,S} {3,S}
2 * O2s u1 {1,S}
3   S   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.09,-4.17,-4.38,-4.16,-3.24,-2.43,-1.96],'cal/(mol*K)'),
        H298 = (104.33,'kcal/mol'),
        S298 = (1.24,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 498,
    label = "CsOJ",
    group = 
"""
1 * O2s u1 {2,S}
2   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.98,-1.3,-1.61,-1.89,-2.38,-2.8,-3.59],'cal/(mol*K)'),
        H298 = (104.06,'kcal/mol'),
        S298 = (-1.46,'cal/(mol*K)'),
    ),
    shortDesc = """CHEN & BOZZELLI(ROJ)""",
    longDesc = 
"""

""",
)

entry(
    index = 499,
    label = "H3COJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * O2s u1 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.11,-1.29,-1.62,-1.97,-2.59,-3.07,-3.84],'cal/(mol*K)'),
        H298 = (104.27,'kcal/mol'),
        S298 = (0.51,'cal/(mol*K)'),
    ),
    shortDesc = """Enthalpy HBI calculated from NIST values, entropy and Cp from B3LYP/6-31G* for CH3OH, CH3O and H""",
    longDesc = 
"""

""",
)

entry(
    index = 500,
    label = "CbOJ",
    group = 
"""
1 * O2s u1 {2,S}
2   Cb  u0 {1,S}
""",
    thermo = 'RC=COJ',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 501,
    label = "OOJ",
    group = 
"""
1 * O2s u1 {2,S}
2   O2s u0 {1,S}
""",
    thermo = 'ROOJ',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 502,
    label = "ROOJ",
    group = 
"""
1   O2s u0 {2,S} {3,S}
2 * O2s u1 {1,S}
3   R!H u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.05,-2.84,-3.55,-4.09,-4.72,-4.97,-5.08],'cal/(mol*K)'),
        H298 = (88.2,'kcal/mol'),
        S298 = (0.22,'cal/(mol*K)'),
    ),
    shortDesc = """CHEN & BOZZELLI""",
    longDesc = 
"""

""",
)

entry(
    index = 503,
    label = "C(=O)OOJ",
    group = 
"""
1   O2s u0 {2,S} {3,S}
2   CO  u0 {1,S} {4,D}
3 * O2s u1 {1,S}
4   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.05,-2.84,-3.55,-4.09,-4.72,-4.97,-5.08],'cal/(mol*K)'),
        H298 = (98.33,'kcal/mol'),
        S298 = (0.22,'cal/(mol*K)'),
    ),
    shortDesc = """HBI for enthalpy from CHEN & BOZZELLI. Cp and S values taken from ROOJ""",
    longDesc = 
"""

""",
)

entry(
    index = 504,
    label = "C3COOJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S} {6,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
6 * O2s u1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.05,-2.84,-3.55,-4.09,-4.72,-4.97,-5.08],'cal/(mol*K)'),
        H298 = (85.3,'kcal/mol'),
        S298 = (0.22,'cal/(mol*K)'),
    ),
    shortDesc = """CHEN & BOZZELLI""",
    longDesc = 
"""

""",
)

entry(
    index = 505,
    label = "SOOJ",
    group = 
"""
1   O2s u0 {2,S} {3,S}
2 * O2s u1 {1,S}
3   S   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.39,-2.62,-2.95,-3.22,-3.66,-3.98,-4.52],'cal/(mol*K)'),
        H298 = (91.79,'kcal/mol'),
        S298 = (1.36,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 506,
    label = "HOOJ",
    group = 
"""
1   O2s u0 {2,S} {3,S}
2 * O2s u1 {1,S}
3   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.99,-2.68,-3.07,-3.3,-3.55,-3.66,-3.9],'cal/(mol*K)'),
        H298 = (85.13,'kcal/mol'),
        S298 = (-0.92,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated from NIST values for H2O2, O2H and H""",
    longDesc = 
"""

""",
)

entry(
    index = 507,
    label = "SOJ",
    group = 
"""
1 * O u1 p2 c0 {2,S}
2   S ux c0 {1,S}
""",
    thermo = 'O2sJ-S2s',
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
""",
)

entry(
    index = 508,
    label = "O2sJ-S2s",
    group = 
"""
1 * O2s u1 p2 c0 {2,S}
2   S2s u0 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.53,-0.81,-0.99,-1.17,-1.56,-1.88,-2.49],'cal/(mol*K)'),
        H298 = (79.78,'kcal/mol'),
        S298 = (1.28,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 509,
    label = "O2sJ-S4d",
    group = 
"""
1 * O2s u1 p2 c0 {2,S}
2   S4d u0 p1 c0 {1,S}
""",
    thermo = 'O2sJ-(S4d-OdO)',
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value of 52.103 kcal/mol, 4/2017, Ryan Gillis
""",
)

entry(
    index = 510,
    label = "O2sJ-(S4d-OdO)",
    group = 
"""
1 * O2s u1 p2 c0 {2,S}
2   S4d u0 p1 c0 {1,S} {3,D} {4,S}
3   O2d u0 p2 c0 {2,D}
4   O   u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.62,-0.07,-0.61,-0.93,-1.55,-2,-2.49],'cal/(mol*K)'),
        H298 = (28.13,'kcal/mol'),
        S298 = (2.64,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 511,
    label = "O2sJ-(S4d-OdC)",
    group = 
"""
1 * O2s u1 p2 c0 {2,S}
2   S4d u0 p1 c0 {1,S} {3,D} {4,S}
3   O   u0 p2 c0 {2,D}
4   C   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.33,-2.94,-3.19,-3.38,-3.72,-4.01,-4.59],'cal/(mol*K)'),
        H298 = (78.16,'kcal/mol'),
        S298 = (-0.19,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 512,
    label = "O2sJ-(S4d-OdH)",
    group = 
"""
1 * O2s u1 p2 c0 {2,S}
2   S4d u0 p1 c0 {1,S} {3,D} {4,S}
3   O   u0 p2 c0 {2,D}
4   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.69,-3.3,-3.74,-4.07,-4.4,-4.54,-4.927],'cal/(mol*K)'),
        H298 = (79.582,'kcal/mol'),
        S298 = (-1.49,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 513,
    label = "O2sJ-(S4d-CdC)",
    group = 
"""
1 * O2s u1 p2 c0 {2,S}
2   S4d u0 p1 c0 {1,S} {3,D} {4,S}
3   C   u0 p0 c0 {2,D}
4   C   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.13,-1.86,-2.28,-2.63,-3.2,-3.64,-4.39],'cal/(mol*K)'),
        H298 = (74.659,'kcal/mol'),
        S298 = (0.698,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 514,
    label = "O2sJ-S6d",
    group = 
"""
1 * O2s u1 p2 c0 {2,S}
2   S6d u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.68,-2.09,-2.45,-2.77,-3.3,-3.71,-4.41],'cal/(mol*K)'),
        H298 = (106.21,'kcal/mol'),
        S298 = (-1.07,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 515,
    label = "O2sJ-N",
    group = 
"""
1 * O2s u1 {2,S}
2   N   u0 {1,S}
""",
    thermo = 'O2sJ-N3s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 516,
    label = "O2sJ-N3s",
    group = 
"""
1 * O2s u1 {2,S}
2   N3s u0 {1,S}
""",
    thermo = 'O2sJ-N3sC',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 517,
    label = "O2sJ-N3sC",
    group = 
"""
1   N3s u0 {2,S} {3,S}
2 * O2s u1 {1,S}
3   C   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.95666,-8.30392,-10.4418,-11.9018,-14.2655,-16.1736,-18.5966],'J/(mol*K)'),
        H298 = (327.882,'kJ/mol'),
        S298 = (3.22862,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 518,
    label = "O2sJ-N3sCO",
    group = 
"""
1   N3s u0 {2,S} {3,S}
2   CO  u0 {1,S} {4,D}
3 * O2s u1 {1,S}
4   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.80695,-9.17585,-11.1673,-12.1719,-13.6433,-14.6347,-16.2533],'J/(mol*K)'),
        H298 = (317.059,'kJ/mol'),
        S298 = (3.29589,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 519,
    label = "O2sJ-N3sO2s",
    group = 
"""
1   N3s u0 {2,S} {3,S}
2 * O2s u1 {1,S}
3   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.49247,-14.5591,-18.7597,-21.1308,-24.037,-25.4752,-25.7812],'J/(mol*K)'),
        H298 = (337.881,'kJ/mol'),
        S298 = (3.72329,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 520,
    label = "O2sJ-N3s(N5sdcO0sc)",
    group = 
"""
1   N3s         u0 {2,S} {3,S}
2   [N5sc,N5dc] u0 {1,S} {4,S}
3 * O2s         u1 {1,S}
4   O0sc        u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.50052,-2.35159,-6.76321,-10.6251,-17.0766,-21.9786,-28.6277],'J/(mol*K)'),
        H298 = (340.144,'kJ/mol'),
        S298 = (17.5768,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 521,
    label = "O2sJ-N5sdtc",
    group = 
"""
1 * O2s                    u1 {2,S}
2   [N5sc,N5dc,N5ddc,N5tc] u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-12.452,-13.7444,-13.9339,-14.0699,-14.6564,-15.3839,-17.2753],'J/(mol*K)'),
        H298 = (431.96,'kJ/mol'),
        S298 = (-8.08566,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 522,
    label = "O2sJ-N5dcOd",
    group = 
"""
1   [N5dc,N5ddc] u0 {2,S} {3,D}
2 * O2s          u1 {1,S}
3   O2d          u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.39039,-6.26822,-9.33998,-11.4358,-14.5602,-16.8834,-20.3064],'J/(mol*K)'),
        H298 = (400.951,'kJ/mol'),
        S298 = (16.5987,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 523,
    label = "O2sJ-N5dcOdO0sc",
    group = 
"""
1   N5dc u0 {2,S} {3,D} {4,S}
2 * O2s  u1 {1,S}
3   O2d  u0 {1,D}
4   O0sc u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.87864,-2.55224,-5.6484,-7.7404,-10.9202,-13.2633,-16.6105],'J/(mol*K)'),
        H298 = (431.801,'kJ/mol'),
        S298 = (-4.97896,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 524,
    label = "O2sJ-N1sc",
    group = 
"""
1 * O2s  u1 {2,S}
2   N1sc u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.37293,-7.06222,-9.51612,-11.2729,-13.4699,-14.9722,-17.077],'J/(mol*K)'),
        H298 = (347.821,'kJ/mol'),
        S298 = (2.24576,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 525,
    label = "O2sJ-N3dN3d",
    group = 
"""
1   N3d u0 {2,S} {3,D}
2 * O2s u1 {1,S}
3   N3d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.29692,-10.2926,-12.6566,-14.1838,-16.3385,-17.5728,-18.6188],'J/(mol*K)'),
        H298 = (664.976,'kJ/mol'),
        S298 = (5.17262,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 526,
    label = "O2sJ-N3dCd",
    group = 
"""
1   N3d      u0 {2,S} {3,D}
2 * O2s      u1 {1,S}
3   [Cd,Cdd] u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.28771,-10.3803,-11.9598,-13.1984,-15.0803,-16.3293,-16.2292],'J/(mol*K)'),
        H298 = (355.56,'kJ/mol'),
        S298 = (-8.0332,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 527,
    label = "SiJ",
    group = 
"""
1 * Si u1
""",
    thermo = 'CJ',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 528,
    label = "SJ",
    group = 
"""
1 * S u1
""",
    thermo = 'S2J',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 529,
    label = "S2J",
    group = 
"""
1 * S2s u1 p2
""",
    thermo = 'S2J-C',
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
""",
)

entry(
    index = 530,
    label = "S2J-H",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.2,-1.52,-1.84,-2.17,-2.73,-3.2,-3.95],'cal/(mol*K)'),
        H298 = (91.82,'kcal/mol'),
        S298 = (-4.62,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 531,
    label = "S2J-C",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   C   u0 {1,S}
""",
    thermo = 'S2J-Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 532,
    label = "S2J-Cs",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   Cs  u0 {1,S}
""",
    thermo = 'S2sJ-(CsHHH)',
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 533,
    label = "S2sJ-(CsHHH)",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   H   u0 {2,S}
4   H   u0 {2,S}
5   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.35,-1.58,-1.87,-2.16,-2.66,-3.11,-3.95],'cal/(mol*K)'),
        H298 = (87.08,'kcal/mol'),
        S298 = (-3.45,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 534,
    label = "S2J-(Cs-Cb)",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   Cs  u0 {1,S} {3,S}
3   Cb  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.29,-3.84,-4.16,-4.58,-5.31,-5.9,-6.84],'cal/(mol*K)'),
        H298 = (86.83,'kcal/mol'),
        S298 = (-4.81,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 535,
    label = "S2J-Ct",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   Ct  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.18,-2.05,-2.66,-3.12,-3.76,-4.24,-4.99],'cal/(mol*K)'),
        H298 = (77.56,'kcal/mol'),
        S298 = (-4.6,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 536,
    label = "S2J-Cb",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   Cb  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.92,-2.1,-2.3,-2.51,-2.93,-3.32,-3.96],'cal/(mol*K)'),
        H298 = (81.36,'kcal/mol'),
        S298 = (-3.66,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 537,
    label = "S2J-Cd",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   Cd  u0 {1,S} {3,D}
3   C   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.29,-2.56,-2.72,-2.87,-3.19,-3.52,-4.13],'cal/(mol*K)'),
        H298 = (79.29,'kcal/mol'),
        S298 = (-1.79,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 538,
    label = "S2J-C=S",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   CS  u0 {1,S} {3,D}
3   S2d u0 p2 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.93,-3.56,-3.88,-4.08,-4.41,-4.74,-5.25],'cal/(mol*K)'),
        H298 = (80.07,'kcal/mol'),
        S298 = (-0.7,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 539,
    label = "S2J-CO",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   CO  u0 {1,S} {3,D}
3   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.26,-2.82,-3.17,-3.44,-3.89,-4.29,-4.95],'cal/(mol*K)'),
        H298 = (89.6,'kcal/mol'),
        S298 = (-0.42,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 CAC""",
    longDesc = 
"""

""",
)

entry(
    index = 540,
    label = "S2J-S2s",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   S2s u0 p2 {1,S}
""",
    thermo = 'S2J-S2s-H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 541,
    label = "S2J-S2s-H",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   S2s u0 p2 {1,S} {3,S}
3   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.93,-2.7,-3.26,-3.67,-4.24,-4.59,-5],'cal/(mol*K)'),
        H298 = (73.97,'kcal/mol'),
        S298 = (-2.53,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 542,
    label = "S2J-S2s-Cs",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   S2s u0 p2 {1,S} {3,S}
3   C   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.95,-3.43,-3.78,-4.06,-4.47,-4.74,-5.03],'cal/(mol*K)'),
        H298 = (71.05,'kcal/mol'),
        S298 = (-1.7,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 543,
    label = "S2J-S2s-S2s",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   S2s u0 p2 {1,S} {3,S}
3   S2s u0 p2 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.63,-4.32,-4.84,-5.26,-5.82,-6.07,-5.99],'cal/(mol*K)'),
        H298 = (72.74,'kcal/mol'),
        S298 = (0.6,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 544,
    label = "S2sJ-O",
    group = 
"""
1 * S2s u1 p2 c0 {2,S}
2   O2s u0 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.15904,-4.00975,-4.36187,-4.91092,-5.32059,-5.53025,-5.75797],'cal/(mol*K)'),
        H298 = (108.577,'kcal/mol'),
        S298 = (-7.47722,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 4/2017, Ryan Gillis
""",
)

entry(
    index = 545,
    label = "S4sJ",
    group = 
"""
1 * S4s u1 p1
""",
    thermo = 'S4sJ-CCC',
    shortDesc = """Sulfur Oxygen Extension""",
    longDesc = 
"""
"
""",
)

entry(
    index = 546,
    label = "S4sJ-CCC",
    group = 
"""
1 * S4s u1 p1 c0 {2,S} {3,S} {4,S}
2   C   ux {1,S}
3   C   ux {1,S}
4   C   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.055,-3.801,-4.696,-5.408,-6.524,-7.325,-8.52],'cal/(mol*K)'),
        H298 = (63.249,'kcal/mol'),
        S298 = (12.849,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
Calculated at CBS-QB3
""",
)

entry(
    index = 547,
    label = "S4sJ-OCC",
    group = 
"""
1 * S4s u1 p1 c0 {2,S} {3,S} {4,S}
2   O   ux {1,S}
3   C   ux {1,S}
4   C   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.475,-0.55,-2.75,-4.66,-7.27,-9.325,-8.64],'cal/(mol*K)'),
        H298 = (21.67,'kcal/mol'),
        S298 = (15.449,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
Based on radical calculations at CBS-QB3
""",
)

entry(
    index = 548,
    label = "S4dJ",
    group = 
"""
1 * S4d u1 p1
""",
    thermo = 'S4dJ-OdO',
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
""",
)

entry(
    index = 549,
    label = "S4dJ-OdH",
    group = 
"""
1   O2d u0 p2 c0 {2,D}
2 * S4d u1 p1 c0 {1,D} {3,S}
3   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.51,-1.2,-1.93,-2.59,-3.6,-4.27,-5.1],'cal/(mol*K)'),
        H298 = (58,'kcal/mol'),
        S298 = (0.54,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 4/2017, Ryan Gillis
""",
)

entry(
    index = 550,
    label = "S4dJ-OdO",
    group = 
"""
1   O2d u0 p2 c0 {2,D}
2 * S4d u1 p1 c0 {1,D} {3,S}
3   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.71,-2.41,-3.09,-3.65,-4.42,-4.89,-5.45],'cal/(mol*K)'),
        H298 = (58.9,'kcal/mol'),
        S298 = (0.14,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 4/2017, Ryan Gillis
""",
)

entry(
    index = 551,
    label = "S6sJ",
    group = 
"""
1 * S6s u1 p0
""",
    thermo = 'S6sJ-CCCCC',
    shortDesc = """Calculated at CBS-QB3""",
    longDesc = 
"""
"
""",
)

entry(
    index = 552,
    label = "S6sJ-CCCCC",
    group = 
"""
1 * S6s u1 p0 c0 {2,S} {3,S} {4,S} {5,S} {6,S}
2   C   ux {1,S}
3   C   ux {1,S}
4   C   ux {1,S}
5   C   ux {1,S}
6   C   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.815,3.48,2.34,1.364,-0.161,-1.233,-2.644],'cal/(mol*K)'),
        H298 = (60.164,'kcal/mol'),
        S298 = (9.723,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 4/2017, Ryan Gillis
""",
)

entry(
    index = 553,
    label = "S6dJ",
    group = 
"""
1 * S6d u1 p0
""",
    thermo = 'S6dJ-OdOCC',
    shortDesc = """Calculated at CBS-QB3""",
    longDesc = 
"""
"
""",
)

entry(
    index = 554,
    label = "S6dJ-OdOCC",
    group = 
"""
1 * S6d u1 p0 c0 {2,S} {3,S} {4,S} {5,D}
2   O   ux {1,S}
3   C   ux {1,S}
4   C   ux {1,S}
5   O   ux {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.35,1.6,-0.19,-0.45,-0.95,-1.42,-3.65],'cal/(mol*K)'),
        H298 = (56.531,'kcal/mol'),
        S298 = (3.34,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
Based on radical calculations at CBS-QB3
""",
)

entry(
    index = 555,
    label = "S6ddJ",
    group = 
"""
1 * S6dd u1 p0
""",
    thermo = 'S6ddJ-OdOdO',
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
""",
)

entry(
    index = 556,
    label = "S6ddJ-OdOdH",
    group = 
"""
1   O2d  u0 p2 c0 {2,D}
2 * S6dd u1 p0 c0 {1,D} {3,D} {4,S}
3   O2d  u0 p2 c0 {2,D}
4   H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.977,0.64,-0.027,-0.741,-1.913,-2.873,-4.269],'cal/(mol*K)'),
        H298 = (75.948,'kcal/mol'),
        S298 = (3.331,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 4/2017, Ryan Gillis
""",
)

entry(
    index = 557,
    label = "S6ddJ-OdOdO",
    group = 
"""
1   O2d  u0 p2 c0 {2,D}
2 * S6dd u1 p0 c0 {1,D} {3,D} {4,S}
3   O2d  u0 p2 c0 {2,D}
4   O2s  u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.539,-1.537,-2.332,-2.933,-4.01,-4.785,-5.701],'cal/(mol*K)'),
        H298 = (86.194,'kcal/mol'),
        S298 = (4.146,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 4/2017, Ryan Gillis
""",
)

entry(
    index = 558,
    label = "NJ",
    group = 
"""
1 * N u1
""",
    thermo = 'N3sJ',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 559,
    label = "N5scJ-HNO",
    group = 
"""
1 * N5sc u1 {2,S} {3,S} {4,S}
2   O    u0 {1,S}
3   N    u0 {1,S}
4   H    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.23096,2.78632,-0.890733,-4.71711,-11.537,-16.9037,-24.8648],'J/(mol*K)'),
        H298 = (244.093,'kJ/mol'),
        S298 = (9.44819,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 560,
    label = "N5scJ-NNO",
    group = 
"""
1 * N5sc u1 {2,S} {3,S} {4,S}
2   O    u0 {1,S}
3   N    u0 {1,S}
4   N    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.26078,-4.51709,-6.33547,-8.68178,-12.6875,-15.8402,-20.7728],'J/(mol*K)'),
        H298 = (243.145,'kJ/mol'),
        S298 = (6.887,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 561,
    label = "N5scJ-HOO",
    group = 
"""
1 * N5sc u1 {2,S} {3,S} {4,S}
2   O    u0 {1,S}
3   O    u0 {1,S}
4   H    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.33189,-3.30638,-6.33549,-9.29979,-13.9065,-17.5137,-22.8214],'J/(mol*K)'),
        H298 = (249.25,'kJ/mol'),
        S298 = (-4.29011,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 562,
    label = "N5scJ-NOO",
    group = 
"""
1 * N5sc u1 {2,S} {3,S} {4,S}
2   O    u0 {1,S}
3   O    u0 {1,S}
4   N    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.490477,-4.77156,-9.06461,-12.6536,-18.0458,-21.5371,-25.0925],'J/(mol*K)'),
        H298 = (268.345,'kJ/mol'),
        S298 = (16.9494,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 563,
    label = "N5scJ-CHO",
    group = 
"""
1 * N5sc u1 {2,S} {3,S} {4,S}
2   C    u0 {1,S}
3   O    u0 {1,S}
4   H    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.68916,-0.596662,-3.96519,-7.11111,-12.1745,-15.8829,-21.1153],'J/(mol*K)'),
        H298 = (221.895,'kJ/mol'),
        S298 = (9.67402,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 564,
    label = "N5scJ-CNO",
    group = 
"""
1 * N5sc u1 {2,S} {3,S} {4,S}
2   C    u0 {1,S}
3   O    u0 {1,S}
4   N    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.18288,-10.1337,-12.6351,-14.4515,-17.1056,-18.8129,-21.0934],'J/(mol*K)'),
        H298 = (242.269,'kJ/mol'),
        S298 = (21.4951,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 565,
    label = "N5scJ-COO",
    group = 
"""
1 * N5sc u1 {2,S} {3,S} {4,S}
2   C    u0 {1,S}
3   O    u0 {1,S}
4   O    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.5935,-4.28154,-7.14307,-9.65718,-13.7651,-16.838,-21.2973],'J/(mol*K)'),
        H298 = (252.716,'kJ/mol'),
        S298 = (2.97211,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 566,
    label = "N5scJ-CCO",
    group = 
"""
1 * N5sc u1 {2,S} {3,S} {4,S}
2   C    u0 {1,S}
3   C    u0 {1,S}
4   O    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.68915,-13.5775,-15.5782,-17.0545,-19.0312,-20.0961,-21.1052],'J/(mol*K)'),
        H298 = (231.664,'kJ/mol'),
        S298 = (-4.55651,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 567,
    label = "N5dcJ-NOd",
    group = 
"""
1 * N5dc u1 {2,S} {3,D}
2   N    u0 {1,S}
3   O    u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.39198,-3.81228,-7.35331,-10.7644,-15.958,-19.1788,-22.8709],'J/(mol*K)'),
        H298 = (334.654,'kJ/mol'),
        S298 = (10.2785,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 568,
    label = "N5dcJ-NdO",
    group = 
"""
1 * N5dc u1 {2,S} {3,D}
2   O    u0 {1,S}
3   N    u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.499652,-2.21608,-5.07031,-7.71348,-12.0168,-14.9458,-19.6336],'J/(mol*K)'),
        H298 = (330.642,'kJ/mol'),
        S298 = (6.64296,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 569,
    label = "N5dcJ-CdO",
    group = 
"""
1 * N5dc u1 {2,S} {3,D}
2   O    u0 {1,S}
3   C    u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.630065,-3.07143,-5.60254,-7.95144,-11.7011,-14.4828,-19.0124],'J/(mol*K)'),
        H298 = (292.28,'kJ/mol'),
        S298 = (1.06787,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 570,
    label = "N3sJ-NN",
    group = 
"""
1 * N3s u1 {2,S} {3,S}
2   N   u0 {1,S}
3   N   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.34071,-5.69699,-7.91406,-9.88987,-12.9386,-14.9969,-17.7496],'J/(mol*K)'),
        H298 = (312.632,'kJ/mol'),
        S298 = (-0.792667,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 571,
    label = "N3sJ-NO",
    group = 
"""
1 * N3s u1 {2,S} {3,S}
2   O   u0 {1,S}
3   N   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.34109,-6.50259,-10.1593,-12.9651,-16.8921,-19.2488,-21.4789],'J/(mol*K)'),
        H298 = (324.57,'kJ/mol'),
        S298 = (5.85483,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 572,
    label = "N3sJ-OO",
    group = 
"""
1 * N3s u1 {2,S} {3,S}
2   O   u0 {1,S}
3   O   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.13984,-7.76932,-11.2129,-13.2285,-15.9222,-17.5188,-19.276],'J/(mol*K)'),
        H298 = (311.479,'kJ/mol'),
        S298 = (2.11221,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 573,
    label = "N3sJ-CN",
    group = 
"""
1 * N3s u1 {2,S} {3,S}
2   C   u0 {1,S}
3   N   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.80393,-7.37641,-9.47396,-11.2655,-13.9993,-15.8916,-18.271],'J/(mol*K)'),
        H298 = (351.185,'kJ/mol'),
        S298 = (-2.7415,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 574,
    label = "N3sJ-CO",
    group = 
"""
1 * N3s u1 {2,S} {3,S}
2   C   u0 {1,S}
3   O   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.19861,-11.8128,-13.9282,-15.0709,-16.1492,-16.3336,-16.3143],'J/(mol*K)'),
        H298 = (332.252,'kJ/mol'),
        S298 = (-0.98057,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 575,
    label = "N3sJ-CtO",
    group = 
"""
1 * N3s u1 {2,S} {3,S}
2   Ct  u0 {1,S}
3   O   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-26.6987,-32.4179,-35.63,-37.6419,-41.0509,-44.038,-47.8704],'J/(mol*K)'),
        H298 = (301.079,'kJ/mol'),
        S298 = (-75.7278,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 576,
    label = "N3sJ",
    group = 
"""
1 * N3s u1 p1
""",
    thermo = 'NHJ_C',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 577,
    label = "NH2J",
    group = 
"""
1 * N3s u1 p1 {2,S} {3,S}
2   H   u0 p0 {1,S}
3   H   u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.43,-0.82,-1.27,-1.72,-2.48,-3.08,-4.1],'cal/(mol*K)'),
        H298 = (107.183,'kcal/mol'),
        S298 = (0.53,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated in relation to ammonia from thermo_DFT_CCSDTF12_BAC values""",
    longDesc = 
"""

""",
)

entry(
    index = 578,
    label = "NHJ_C",
    group = 
"""
1 * N3s u1 p1 {2,S} {3,S}
2   C   u0 p0 {1,S}
3   H   u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.79,-1.23,-1.64,-2.02,-2.66,-3.2,-4.16],'cal/(mol*K)'),
        H298 = (99.653,'kcal/mol'),
        S298 = (0.92,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated in relation to CH3NH2 from thermo_DFT_CCSDTF12_BAC values""",
    longDesc = 
"""

""",
)

entry(
    index = 579,
    label = "NHJ_Cd",
    group = 
"""
1 * N3s      u1 p1 {2,S} {3,S}
2   [Cd,Cdd] u0 p0 {1,S}
3   H        u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.36968,-7.21186,-7.55213,-8.1556,-9.51515,-10.9959,-14.5568],'J/(mol*K)'),
        H298 = (353.261,'kJ/mol'),
        S298 = (-3.90709,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 580,
    label = "NHJ_O",
    group = 
"""
1 * N3s u1 p1 {2,S} {3,S}
2   O   u0 p2 {1,S}
3   H   u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.26,-1.89,-2.4,-2.79,-3.17,-3.37,-3.65],'cal/(mol*K)'),
        H298 = (85.023,'kcal/mol'),
        S298 = (-0.27,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated w.r.t NH2OH and [NH]OH, both from thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
"""

""",
)

entry(
    index = 581,
    label = "NHJ_N",
    group = 
"""
1 * N3s u1 p1 {2,S} {3,S}
2   N   u0 {1,S}
3   H   u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.77,-2.62,-3.28,-3.79,-4.57,-5.11,-5.85],'cal/(mol*K)'),
        H298 = (82.283,'kcal/mol'),
        S298 = (-0.33,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated w.r.t NH2NH2 and [NH]NH2, both from thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
"""

""",
)

entry(
    index = 582,
    label = "NHJ_N3d",
    group = 
"""
1 * N3s u1 p1 {2,S} {3,S}
2   N3d u0 {1,S}
3   H   u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.70038,-4.63454,-6.10735,-7.60395,-10.2929,-12.3802,-15.6322],'J/(mol*K)'),
        H298 = (339.161,'kJ/mol'),
        S298 = (1.25886,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 583,
    label = "NHJ_N5dc",
    group = 
"""
1 * N3s  u1 p1 {2,S} {3,S}
2   N5dc u0 {1,S}
3   H    u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.78518,1.52507,-3.04956,-6.60718,-12.0808,-15.9009,-20.6874],'J/(mol*K)'),
        H298 = (434.288,'kJ/mol'),
        S298 = (2.72516,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 584,
    label = "NJ_CC",
    group = 
"""
1 * N3s u1 p1 {2,S} {3,S}
2   C   u0 p0 {1,S}
3   C   u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.88844,-7.02096,-9.05679,-10.9554,-13.6124,-15.7099,-19.2836],'J/(mol*K)'),
        H298 = (389.974,'kJ/mol'),
        S298 = (-10.0809,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 585,
    label = "NJ_CCd",
    group = 
"""
1 * N3s      u1 p1 {2,S} {3,S}
2   C        u0 p0 {1,S}
3   [Cd,Cdd] u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.94584,-1.87787,-2.86025,-4.58312,-8.42517,-11.1267,-15.6176],'J/(mol*K)'),
        H298 = (350.499,'kJ/mol'),
        S298 = (-11.7385,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 586,
    label = "NJ_CCO",
    group = 
"""
1 * N3s u1 p1 {2,S} {3,S}
2   CO  u0 p0 {1,S} {4,D}
3   C   u0 p0 {1,S}
4   O2d u0 p2 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.961761,-0.807363,-3.28705,-5.60897,-9.76264,-13.2901,-19.6482],'J/(mol*K)'),
        H298 = (450.927,'kJ/mol'),
        S298 = (3.87449,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 587,
    label = "N3dJ",
    group = 
"""
1 * N3d u1 p1
""",
    thermo = 'N3dJ_C',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 588,
    label = "N3dJ_C",
    group = 
"""
1 * N3d u1 p1 {2,D}
2   C   u0 p0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.2,-0.6,-1.07,-1.56,-2.44,-3.15,-4.26],'cal/(mol*K)'),
        H298 = (88.343,'kcal/mol'),
        S298 = (-0.71,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated w.r.t NH=CH2 and [N]=CH2, both from thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
"""

""",
)

entry(
    index = 589,
    label = "N3dJ_Cdd",
    group = 
"""
1 * N3d u1 p1 {2,D}
2   Cdd u0 p0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.67103,-7.14899,-8.76464,-10.2906,-12.8917,-14.9076,-18.0576],'J/(mol*K)'),
        H298 = (257.412,'kJ/mol'),
        S298 = (-1.20388,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 590,
    label = "N3dJ_O",
    group = 
"""
1 * N3d u1 p1 {2,D}
2   O   u0 p2 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.12,-1.36,-1.67,-2,-2.62,-3.11,-3.89],'cal/(mol*K)'),
        H298 = (48.613,'kcal/mol'),
        S298 = (-3.69,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated w.r.t HN=O and [N]=O, both from thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
"""

""",
)

entry(
    index = 591,
    label = "N3dJ_N",
    group = 
"""
1 * N3d u1 p1 {2,D}
2   N   u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.14,-0.51,-0.97,-1.46,-2.33,-3.02,-4.16],'cal/(mol*K)'),
        H298 = (64.083,'kcal/mol'),
        S298 = (1.49,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated w.r.t HN=NH and [N]=NH, both from thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
"""

""",
)

entry(
    index = 592,
    label = "N3dJ_N5dc",
    group = 
"""
1 * N3d  u1 p1 {2,D}
2   N5dc u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0356123,-2.98703,-5.6088,-7.86526,-11.8936,-15.0898,-19.6396],'J/(mol*K)'),
        H298 = (413.171,'kJ/mol'),
        S298 = (2.89249,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 593,
    label = "N3dJ_N3d",
    group = 
"""
1 * N3d u1 p1 {2,D}
2   N3d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.05081,-2.13979,-6.00346,-9.14917,-13.5357,-16.2931,-19.6448],'J/(mol*K)'),
        H298 = (306.397,'kJ/mol'),
        S298 = (18.8295,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 594,
    label = "RJ2_triplet",
    group = 
"""
1 * R!H u2
""",
    thermo = 'CJ2_triplet',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 595,
    label = "CJ2_triplet",
    group = 
"""
1 * C u2
""",
    thermo = 'CsJ2_triplet',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 596,
    label = "OsCsJ2H_triplet",
    group = 
"""
1 * Cs u2 {2,S} {3,S}
2   O  u0 p2 {1,S} {4,S}
3   H  u0 {1,S}
4   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.444,-1.111,-1.988,-2.889,-4.529,-5.915,-8.422],'cal/(mol*K)'),
        H298 = (205.773,'kcal/mol'),
        S298 = (-2.011,'cal/(mol*K)'),
    ),
    shortDesc = """Fittted to DFT_QCI_thermo library""",
    longDesc = 
"""
Fitted to RQCISD(T)/cc-PV(infinity)(Q)Z calculations of:

Goldsmith, C. F.; Magoon, G. R.; Green, W. H., Database of Small Molecule Thermochemistry for Combustion.
J. Phys. Chem. A 2012, 116, 9033-9057.
""",
)

entry(
    index = 597,
    label = "CsJ2_triplet",
    group = 
"""
1 * Cs u2
""",
    thermo = 'CH2_triplet',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 598,
    label = "CH2_triplet",
    group = 
"""
1 * Cs u2 {2,S} {3,S}
2   H  u0 {1,S}
3   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.27,-1.08,-2.14,-3.23,-5.18,-6.74,-9.47],'cal/(mol*K)'),
        H298 = (214.44,'kcal/mol'),
        S298 = (-1.73,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated for methylene in relation to methane from NIST values""",
    longDesc = 
"""

""",
)

entry(
    index = 599,
    label = "CsJ2_P_triplet",
    group = 
"""
1 * Cs       u2 {2,S} {3,S}
2   C        u0 {1,S}
3   [H,Val7] u0 {1,S}
""",
    thermo = 'CsCsJ2_triplet',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 600,
    label = "CsCVal7_triplet",
    group = 
"""
1 * Cs   u2 {2,S} {3,S}
2   C    u0 {1,S}
3   Val7 u0 {1,S}
""",
    thermo = 'CsCCl_triplet',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 601,
    label = "CsCF_triplet",
    group = 
"""
1 * Cs u2 {2,S} {3,S}
2   C  u0 {1,S}
3   F  u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 602,
    label = "CsCCl_triplet",
    group = 
"""
1 * Cs u2 {2,S} {3,S}
2   C  u0 {1,S}
3   Cl u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.46058,-2.59924,-3.68621,-4.60621,-6.0777,-7.22296,-9.13333],'cal/(mol*K)','+|-',[0.570667,0.585929,0.54938,0.513134,0.452851,0.396279,0.290243]),
        H298 = (192.67,'kcal/mol','+|-',0.911635),
        S298 = (-1.68686,'cal/(mol*K)','+|-',1.54928),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOCl_G4 label:ODC[C]Cl smiles:O=C[C]Cl H298:49.20 kcal/mol
library:CHOCl_G4 label:CC(DO)[C]Cl smiles:CC(=O)[C]Cl H298:35.44 kcal/mol
library:CHOCl_G4 label:C#C[C]Cl smiles:C#C[C]Cl H298:127.19 kcal/mol
""",
)

entry(
    index = 603,
    label = "CsCBr_triplet",
    group = 
"""
1 * Cs u2 {2,S} {3,S}
2   C  u0 {1,S}
3   Br u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.814423,-2.05803,-3.13571,-4.0568,-5.59406,-6.82149,-8.78544],'cal/(mol*K)','+|-',[0.442037,0.453859,0.425548,0.397472,0.350777,0.306956,0.224821]),
        H298 = (196.466,'kcal/mol','+|-',0.706149),
        S298 = (-0.141293,'cal/(mol*K)','+|-',1.20007),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:C#C[C]Br smiles:C#C[C]Br H298:138.67 kcal/mol
library:CHOBr_G4 label:ODC(Br)[C]Br smiles:O=C(Br)[C]Br H298:59.23 kcal/mol
library:CHOBr_G4 label:CC(DO)[C]Br smiles:CC(=O)[C]Br H298:47.98 kcal/mol
library:CHOBr_G4 label:CC(Br)(Br)[C]Br smiles:CC(Br)(Br)[C]Br H298:87.04 kcal/mol
library:CHOBr_G4 label:ODC[C]Br smiles:O=C[C]Br H298:61.35 kcal/mol
""",
)

entry(
    index = 604,
    label = "CsCsJ2_triplet",
    group = 
"""
1 * Cs u2 {2,S} {3,S}
2   Cs u0 {1,S}
3   H  u0 {1,S}
""",
    thermo = 'CCJ2_triplet',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 605,
    label = "CCJ2_triplet",
    group = 
"""
1 * Cs u2 {2,S} {3,S}
2   Cs u0 {1,S} {4,S} {5,S} {6,S}
3   H  u0 {1,S}
4   H  u0 {2,S}
5   H  u0 {2,S}
6   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.81,-1.74,-2.69,-3.61,-5.18,-6.42,-8.36],'cal/(mol*K)'),
        H298 = (211.3,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """BDE and Cp calculated from data in KIM et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 606,
    label = "PhCH_triplet",
    group = 
"""
1 * Cs u2 {2,S} {3,S}
2   Cb u0 {1,S}
3   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (195,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """BDE from PUTSMA et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 607,
    label = "AllylJ2_triplet",
    group = 
"""
1 * Cs u2 {2,S} {3,S}
2   Cd u0 {1,S}
3   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (192.8,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """BDE from PUTSMA et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 608,
    label = "CsJ2_S_triplet",
    group = 
"""
1 * Cs u2 {2,S} {3,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
""",
    thermo = 'CsJ2_P_triplet',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 609,
    label = "CdJ2_triplet",
    group = 
"""
1 * [Cd,CO] u2
""",
    thermo = 'CCdJ2_triplet',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 610,
    label = "CCdJ2_triplet",
    group = 
"""
1 * Cd u2 {2,D}
2   C  u0 {1,D}
""",
    thermo = 'CdCdJ2_triplet',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 611,
    label = "CdCdJ2_triplet",
    group = 
"""
1 * Cd u2 {2,D}
2   Cd u0 {1,D} {3,S} {4,S}
3   H  u0 {2,S}
4   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.904,-2.152,-3.433,-4.583,-6.214,-7.197,-9.27],'cal/(mol*K)'),
        H298 = (237.632,'kcal/mol'),
        S298 = (1.79,'cal/(mol*K)'),
    ),
    shortDesc = """Fittted to DFT_QCI_thermo library""",
    longDesc = 
"""
Fitted to RQCISD(T)/cc-PV(infinity)(Q)Z calculations of:

    Goldsmith, C. F.; Magoon, G. R.; Green, W. H., Database of Small Molecule Thermochemistry for Combustion.
    J. Phys. Chem. A 2012, 116, 9033-9057.
""",
)

entry(
    index = 612,
    label = "(CO)CdJ2_triplet",
    group = 
"""
1 * Cd  u2 {2,D}
2   Cdd u0 {1,D} {3,D}
3   O   u0 p2 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.763,-2.732,-3.654,-4.473,-5.712,-6.563,-8.315],'cal/(mol*K)'),
        H298 = (206.595,'kcal/mol'),
        S298 = (-1.634,'cal/(mol*K)'),
    ),
    shortDesc = """Fittted to DFT_QCI_thermo library""",
    longDesc = 
"""
Fitted to RQCISD(T)/cc-PV(infinity)(Q)Z calculations of:

    Goldsmith, C. F.; Magoon, G. R.; Green, W. H., Database of Small Molecule Thermochemistry for Combustion.
    J. Phys. Chem. A 2012, 116, 9033-9057.
""",
)

entry(
    index = 613,
    label = "NCdJ2_triplet",
    group = 
"""
1 * Cd  u2 {2,D}
2   N3d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.67688,-8.56951,-13.0936,-17.1322,-23.6155,-28.3134,-35.4124],'J/(mol*K)'),
        H298 = (587.145,'kJ/mol'),
        S298 = (22.0742,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 614,
    label = "CdJ2-Sd_triplet",
    group = 
"""
1 * CS  u2 {2,D}
2   S2d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.42,-2.3,-3.22,-4.04,-5.42,-6.5,-8.29],'cal/(mol*K)'),
        H298 = (238.75,'kcal/mol'),
        S298 = (-3.31,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 615,
    label = "Oa_triplet",
    group = 
"""
1 * O u2
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.8,-3.05,-3.33,-3.62,-4.24,-4.86,-6.28],'cal/(mol*K)'),
        H298 = (221.55,'kcal/mol'),
        S298 = (-8.02,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated for atomic oxygen in relation to water from NIST values""",
    longDesc = 
"""

""",
)

entry(
    index = 616,
    label = "SiJ2_triplet",
    group = 
"""
1 * Si u2
""",
    thermo = 'CJ2_triplet',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 617,
    label = "SJ2_triplet",
    group = 
"""
1 * S u2
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.19,-3.52,-3.89,-4.3,-5.12,-5.86,-7.14],'cal/(mol*K)'),
        H298 = (176.42,'kcal/mol'),
        S298 = (-12.02,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 618,
    label = "NJ2_triplet",
    group = 
"""
1 * N u2
""",
    thermo = 'NJ2_C',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 619,
    label = "N3sJ2",
    group = 
"""
1 * N3s u2 p1
""",
    thermo = 'NJ2_C',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 620,
    label = "NHJ2",
    group = 
"""
1 * N3s u2 p1 {2,S}
2   H   u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54,-2.1,-2.78,-3.47,-4.75,-5.77,-7.61],'cal/(mol*K)'),
        H298 = (200.636,'kcal/mol'),
        S298 = (-2.72,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated w.r.t NH3 and [N], both from thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
"""

""",
)

entry(
    index = 621,
    label = "NJ2_C",
    group = 
"""
1 * N3s u2 p1 {2,S}
2   C   u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.36,-2.97,-3.51,-4,-5,-5.96,-7.75],'cal/(mol*K)'),
        H298 = (184.816,'kcal/mol'),
        S298 = (-3.04,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated w.r.t NH2CH3 and [N]CH3, both from thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
"""

""",
)

entry(
    index = 622,
    label = "NJ2_O",
    group = 
"""
1 * N3s u2 p1 {2,S}
2   O   u0 p2 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.05,-3.22,-4.34,-5.36,-6.88,-7.91,-9.25],'cal/(mol*K)'),
        H298 = (166.156,'kcal/mol'),
        S298 = (-0.91,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated w.r.t NH2OH and [N]OH, both from thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
"""

""",
)

entry(
    index = 623,
    label = "RJ3",
    group = 
"""
1 * R!H u3
""",
    thermo = 'CJ3',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 624,
    label = "CJ3",
    group = 
"""
1 * Cs u3
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.57,-2.73,-4.11,-5.5,-7.92,-9.85,-12.95],'cal/(mol*K)'),
        H298 = (316.19,'kcal/mol'),
        S298 = (-5.7,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated for methylidyene in relation to methane from NIST values""",
    longDesc = 
"""

""",
)

entry(
    index = 625,
    label = "SiJ3",
    group = 
"""
1 * Sis u3
""",
    thermo = 'CJ3',
    shortDesc = """""",
    longDesc = 
"""

""",
)

tree(
"""
L1: Radical
    L2: RJ
        L3: CJ
            L4: CsJ
                L5: CsBr1sBr1sCO
                L5: CsBr1sCOCl1s
                L5: CsCOCl1sCl1s
                L5: CsBr1sCOF1s
                L5: CsCOCl1sF1s
                L5: CsCOF1sF1s
                L5: CsBr1sCOH
                L5: CsCOCl1sH
                L5: CsCOF1sH
                L5: CsBr1sCOO2s
                L5: CsCOCl1sO2s
                L5: CsCOF1sO2s
                L5: CsBr1sCOCO
                L5: CsCOCOCl1s
                L5: CsCOCOF1s
                L5: CsBr1sCOCt
                L5: CsCOCl1sCt
                L5: CsCOCtF1s
                L5: CsBr1sCOCd
                L5: CsCOCdCl1s
                L5: CsCOCdF1s
                L5: CsBr1sCOCs
                L5: CsCOCl1sCs
                L5: CsCOCsF1s
                L5: CsBr1sBr1sO2s
                L5: CsBr1sCl1sO2s
                L5: CsCl1sCl1sO2s
                L5: CsBr1sF1sO2s
                L5: CsCl1sF1sO2s
                L5: CsF1sF1sO2s
                L5: CsBr1sHO2s
                L5: CsCl1sHO2s
                L5: CsF1sHO2s
                L5: CsBr1sO2sO2s
                L5: CsCl1sO2sO2s
                L5: CsF1sO2sO2s
                L5: CsBr1sBr1sCt
                L5: CsBr1sCl1sCt
                L5: CsCl1sCl1sCt
                L5: CsBr1sCtF1s
                L5: CsCl1sCtF1s
                L5: CsCtF1sF1s
                L5: CsBr1sCtH
                L5: CsCl1sCtH
                L5: CsCtF1sH
                L5: CsBr1sCtO2s
                L5: CsCl1sCtO2s
                L5: CsCtF1sO2s
                L5: CsBr1sCtCt
                L5: CsCl1sCtCt
                L5: CsCtCtF1s
                L5: CsBr1sBr1sCd
                L5: CsBr1sCdCl1s
                L5: CsCdCl1sCl1s
                L5: CsBr1sCdF1s
                L5: CsCdCl1sF1s
                L5: CsCdF1sF1s
                L5: CsBr1sCdH
                L5: CsCdCl1sH
                L5: CsCdF1sH
                L5: CsBr1sCdO2s
                L5: CsCdCl1sO2s
                L5: CsCdF1sO2s
                L5: CsBr1sCdCt
                L5: CsCdCl1sCt
                L5: CsCdCtF1s
                L5: CsBr1sCdCd
                L5: CsCdCdCl1s
                L5: CsCdCdF1s
                L5: CsBr1sBr1sCs
                L5: CsBr1sCl1sCs
                L5: CsCl1sCl1sCs
                L5: CsBr1sCsF1s
                L5: CsCl1sCsF1s
                L5: CsCsF1sF1s
                L5: CsBr1sCsH
                L5: CsCl1sCsH
                L5: CsCsF1sH
                L5: CsBr1sCsO2s
                L5: CsCl1sCsO2s
                L5: CsCsF1sO2s
                L5: CsBr1sCsCt
                L5: CsCl1sCsCt
                L5: CsCsCtF1s
                L5: CsBr1sCdCs
                L5: CsCdCl1sCs
                L5: CsCdCsF1s
                L5: CsBr1sCsCs
                L5: CsCl1sCsCs
                L5: CsCsCsF1s
                L5: CH3
                L5: Cs_P
                    L6: CJCO
                        L7: C=C(O)CJ
                        L7: CJCOOH
                        L7: CJC(C)OC
                        L7: CJC(C)2O
                            L8: C=CC(C)(O)CJ
                                L9: C=CC(O)(C=O)CJ
                            L8: CJC(C)(C=O)O
                        L7: CJC(O)2C
                            L8: C=CC(O)2CJ
                    L6: CJCC=O
                        L7: CJC(C)2C=O
                            L8: CJC(C=O)2C
                                L9: C=CC(C=O)2CJ
                            L8: C=CC(C)(C=O)CJ
                        L7: CJC(C)C=O
                        L7: C=C(C=O)CJ
                    L6: CJCC=C=O
                        L7: CJC(C)C=C=O
                        L7: C=C(CJ)C=C=O
                    L6: CsCsJ
                        L7: CCJ
                        L7: RCCJ
                        L7: Neopentyl
                        L7: Isobutyl
                    L6: Benzyl_P
                    L6: Allyl_P
                        L7: C=CC=CCJ
                        L7: CTCC=CCJ
                        L7: CJC=C=O
                    L6: Propargyl
                    L6: CJC=O
                        L7: C2JC=O
                L5: Cs_S
                    L6: CCJCO
                        L7: C=CCJCO
                            L8: C=CCJC(O)C=C
                        L7: CCJCOOH
                    L6: CCJCC=O
                    L6: CCJC(C)=C=O
                    L6: (Cs)2CsJ
                        L7: cyclopentene-4
                            L8: bicyclo[2.1.1]hex-2-ene-C5
                                L9: tricyclo[2.1.1.0(1,4)]hex-2-ene-C5
                            L8: bicyclo[2.1.0]pent-2-ene-C5
                        L7: bicyclo[1.1.1]pentane-C2
                            L8: tricyclo[1.1.1.0(1,3)]pentane-C2
                        L7: bicyclo[2.1.1]hexane-C5
                            L8: tricyclo[2.1.1.0(1,4)]hexane-C5
                        L7: cyclopropane
                            L8: spiro[2.2]pentane-secondary
                            L8: tricyclo[2.2.1.0(1,4)]heptane-C7
                            L8: bicyclo[2.1.0]pentane-secondary-C3
                            L8: tricyclo[3.1.1.0(1,5)]heptane-C6
                            L8: bicyclo[1.1.0]butane-secondary
                            L8: bicyclo[3.1.0]hexane-C3
                            L8: bicyclo[4.1.0]heptane-C3-7
                            L8: bicyclo[4.1.0]heptane-C3-7
                        L7: tricyclo[2.1.1.0(1,4)]hexane-C2
                        L7: bicyclo[3.1.1]heptane-C6
                        L7: tricyclo[2.2.1.0(1,4)]heptane-C2
                        L7: bicyclo[4.2.0]octane-C4-7
                        L7: bicyclo[2.2.2]octane-C2
                            L8: tricyclo[2.2.2.0(1,4)]octane-C2
                        L7: cyclobutane
                            L8: bicyclo[2.1.0]pentane-secondary-C4
                            L8: bicyclo[2.2.0]hexane-secondary
                            L8: bicyclo[3.2.0]heptane-C5-6
                            L8: tricyclo[2.2.1.0(1,4)]heptane-C2
                            L8: bicyclo[4.2.0]octane-C4-7
                        L7: bicyclo[3.1.1]heptane-C2
                            L8: tricyclo[3.1.1.0(1,5)]heptane-C2
                        L7: bicyclo[3.1.0]hexane-C5-2
                        L7: bicyclo[3.1.0]hexane-C5-3
                        L7: bicyclo[2.1.1]hexane-C2
                        L7: 7-norbornyl
                        L7: 2-norbornyl
                        L7: bicyclo[4.1.0]heptane-C6-2
                        L7: bicyclo[4.1.0]heptane-C6-3
                        L7: bicyclo[4.1.0]heptane-C6-3
                        L7: cycloheptane
                            L8: bicyclo[3.2.0]heptane-C5-2
                            L8: bicyclo[3.2.0]heptane-C5-3
                        L7: bicyclo[4.1.0]heptane-C6-2
                        L7: bicyclo[3.1.1]heptane-C3
                            L8: tricyclo[3.1.1.0(1,5)]heptane-C3
                        L7: octahydro-pentalene-C5-2
                        L7: octahydro-pentalene-C5-3
                        L7: bicyclo[4.2.0]octane-C6-2
                        L7: bicyclo[4.2.0]octane-C6-3
                        L7: CCJC
                        L7: RCCJC
                        L7: RCCJCC
                            L8: cyclopentane
                            L8: cyclohexane
                    L6: Benzyl_S
                        L7: Indenyl
                        L7: Benzyl_S_Fused5
                        L7: Benzyl_S_Fused6
                            L8: Benzyl_S_dihydronaphthalene
                        L7: Benzyl_S_Fused7
                    L6: Allyl_S
                        L7: Aromatic_pi_S_1_3
                            L8: Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
                                L9: Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
                                    L10: Aromatic_pi_S_(fused5)_1_3
                                    L10: Aromatic_pi_S_(fused6)_1_3
                                    L10: Aromatic_pi_S_(fused7)_1_3
                                    L10: Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3
                                        L11: Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3
                            L8: Aromatic_pi_S_(CH3_CH3_Meta)_1_3_1
                                L9: Aromatic_pi_S_(CH3_C2H5_Meta)_1_3_1
                                    L10: Aromatic_pi_S_(CH3_Benzyl_Meta)_1_3_1
                                        L11: Aromatic_pi_S_(CH3_EBenzyl_Meta)_1_3_1
                            L8: Aromatic_pi_S_(CH3_CH3_Meta)_1_3_2
                                L9: Aromatic_pi_S_(CH3_C2H5_Meta)_1_3_2
                                    L10: Aromatic_pi_S_(CH3_Benzyl_Meta)_1_3_2
                                        L11: Aromatic_pi_S_(CH3_EBenzyl_Meta)_1_3_2
                            L8: Aromatic_pi_S_(CH3_CH3_Para)_1_3
                                L9: Aromatic_pi_S_(CH3_C2H5_Para)_1_3
                                    L10: Aromatic_pi_S_(CH3_Benzyl_Para)_1_3
                                        L11: Aromatic_pi_S_(CH3_EBenzyl_Para)_1_3
                            L8: Aromatic_pi_S_(CH3_CH3_Sub)_1_3
                                L9: Aromatic_pi_S_(s1_3_6_diene_1_4)_1_3
                                L9: Aromatic_pi_S_(CH3_C2H5_Sub)_1_3
                                    L10: Aromatic_pi_S_(s1_4_6_diene_1_4)_1_3
                                    L10: Aromatic_pi_S_(s1_5_6_diene_1_4)_1_3
                                    L10: Aromatic_pi_S_(s1_6_6_diene_1_4)_1_3
                                    L10: Aromatic_pi_S_(CH3_Benzyl_Sub)_1_3
                                        L11: Aromatic_pi_S_(CH3_EBenzyl_Sub)_1_3
                        L7: CJ-Cd-Benzene
                        L7: CJ-Cd-Benzene7
                        L7: cyclobutene-allyl
                        L7: cyclopentene-allyl
                        L7: cyclohexene-allyl
                    L6: C=CCJC=C
                        L7: Aromatic_pi_S_1_4
                            L8: Aromatic_pi_S_(CH3_CH3_Ortho)_1_4
                                L9: Aromatic_pi_S_(CH3_C2H5_Ortho)_1_4
                                    L10: Aromatic_pi_S_(fused5)_1_4
                                    L10: Aromatic_pi_S_(fused6)_1_4
                                    L10: Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_4
                                        L11: Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_4
                            L8: Aromatic_pi_S_(CH3_CH3_Meta)_1_4
                                L9: Aromatic_pi_S_(CH3_C2H5_Meta)_1_4
                                    L10: Aromatic_pi_S_(CH3_Benzyl_Meta)_1_4
                                        L11: Aromatic_pi_S_(CH3_EBenzyl_Meta)_1_4
                            L8: Aromatic_pi_S_(CH3_CH3_Sub)_1_4
                                L9: Aromatic_pi_S_(s1_3_6_diene_1_4)_1_4
                                L9: Aromatic_pi_S_(CH3_C2H5_Sub)_1_4
                                    L10: Aromatic_pi_S_(s1_4_6_diene_1_4)_1_4
                                    L10: Aromatic_pi_S_(s1_5_6_diene_1_4)_1_4
                                    L10: Aromatic_pi_S_(s1_6_6_diene_1_4)_1_4
                                    L10: Aromatic_pi_S_(CH3_Benzyl_Sub)_1_4
                                        L11: Aromatic_pi_S_(CH3_EBenzyl_Sub)_1_4
                        L7: cyclopropenyl-allyl
                        L7: 1,3-cyclopentadiene-allyl
                        L7: C=CCJC=C=O
                    L6: Sec_Propargyl
                    L6: CCJC=O
                        L7: CCJCHO
                        L7: C=OCJC=O
                L5: Cs_T
                    L6: CCJ(C)CO
                        L7: C2CJCOOH
                    L6: Tertalkyl
                        L7: bicyclo[1.1.0]butane-tertiary
                        L7: bicyclo[2.1.0]pentane-tertiary
                        L7: bicyclo[1.1.1]pentane-C1
                        L7: bicyclo[3.1.0]hexane-tertiary
                        L7: bicyclo[2.2.0]hexane-tertiary
                        L7: bicyclo[2.1.1]hexane-C1
                        L7: bridgehead_norbornyl
                        L7: bicyclo[3.2.0]heptane-tertiary
                        L7: bicyclo[4.1.0]heptane-tertiary
                        L7: bicyclo[3.1.1]heptane-C1
                        L7: octahydro-pentalene-tertiary
                        L7: bicyclo[4.2.0]octane-tertiary
                        L7: bicyclo[2.2.2]octane-C1
                    L6: Benzyl_T
                        L7: Benzyl_T_Fused5
                        L7: Benzyl_T_Fused6
                            L8: Benzyl_T_dihydronaphthalene
                    L6: CCJ(C)C=C=O
                        L7: C=CCJ(C)C=C=O
                            L8: C=CCJ(C=C=O)C=C
                    L6: Allyl_T
                        L7: Aromatic_pi_T_1_3
                            L8: Aromatic_pi_T_(CH3_CH3_Ortho)_1_3
                                L9: Aromatic_pi_T_(CH3_C2H5_Ortho)_1_3
                                    L10: Aromatic_pi_T_(fused5)_1_3
                                    L10: Aromatic_pi_T_(fused6)_1_3
                                    L10: Aromatic_pi_T_(CH3_Benzyl_Ortho)_1_3
                                        L11: Aromatic_pi_T_(CH3_EBenzyl_Ortho)_1_3
                        L7: Aromatic_pi_T_1_4
                            L8: Aromatic_pi_T_(CH3_CH3_Para)_1_4
                                L9: Aromatic_pi_T_(CH3_C2H5_Para)_1_4
                                    L10: Aromatic_pi_T_(CH3_Benzyl_Para)_1_4
                                        L11: Aromatic_pi_T_(CH3_EBenzyl_Para)_1_4
                        L7: bicyclo[2.1.0]pent-2-ene-C1
                        L7: bicyclo[2.1.1]hex-2-ene-C1
                        L7: bicyclo[2.2.0]hexa-2,5-diene-C1
                        L7: C=CCJ(C)C=O
                            L8: C=CCJ(C=O)C=C
                    L6: Tert_Propargyl
                    L6: C2CJCO
                        L7: C2CJCHO
                L5: CsJO
                    L6: CsJOH
                    L6: CsJOC
                        L7: CsJOCs
                            L8: CsJOCH3
                            L8: CsJOCC
                            L8: CsJOCC2
                            L8: CsJOCC3
                        L7: CsJOCds
                            L8: CsJOC(O)
                                L9: CsJOC(O)H
                                L9: CsJOC(O)C
                            L8: C=COCJ
                    L6: CsJOO
                        L7: CsJOOH
                        L7: CsJOOC
                L5: CCsJO
                    L6: CCsJOC
                        L7: C=CCJ(O)C
                        L7: CCsJOCs
                        L7: CCsJOCds
                            L8: CCsJOC(O)
                                L9: CCsJOC(O)H
                                L9: CCsJOC(O)C
                    L6: C=CCJO
                    L6: OCJC=O
                    L6: CCsJOH
                    L6: CCsJOO
                        L7: CCsJOOH
                        L7: CCsJOOC
                L5: C2CsJO
                    L6: C2CsJOH
                    L6: C2CsJOC
                        L7: C2CsJOCs
                        L7: C2CsJOCds
                            L8: C2CsJOC(O)
                                L9: C2CsJOC(O)H
                                L9: C2CsJOC(O)C
                    L6: C2CsJOO
                        L7: C2CsJOOH
                        L7: C2CsJOOC
                L5: CsJ-S
                    L6: CsJ-SsHH
                    L6: CsJ-CSH
                        L7: CsJ-CsSsH
                        L7: CsJ-CtSsH
                        L7: CsJ-CbSsH
                        L7: CsJ-CdSsH
                        L7: CsJ-C=SSsH
                    L6: CsJ-CCS
                        L7: CsJ-CsCsSs
                        L7: CsJ-CsCtSs
                        L7: CsJ-CsCbSs
                        L7: CsJ-CsCdSs
                        L7: CsJ-CsC=SSs
                    L6: CsJ-SS
                        L7: CsJ-SsSsH
                        L7: CsJ-CSS
                            L8: CsJ-CsSsSs
                            L8: CsJ-CtSsSs
                            L8: CsJ-CbSsSs
                            L8: CsJ-CdSsSs
                            L8: CsJ-C=SSsSs
                        L7: CsJ-SsSsSs
                    L6: CCsJOS
                        L7: CCsJOHSH
                    L6: CsJ-SsOsH
                L5: OCJO
                L5: CsJ-HNN
                    L6: CsJ-HNN3ds
                        L7: CsJ-HN(N3dCd)
                        L7: CsJ-HN(N3dOd)
                        L7: CsJ-HN(N3dN5dc)
                    L6: CsJ-HN5scN5sc
                L5: CsJ-NNN
                L5: CsJ-HNO
                    L6: CsJ-HON1sc
                L5: CsJ-NNO
                L5: CsJ-NOO
                L5: CsJ-CNN
                L5: CsJ-CNO
                L5: CsJN
                    L6: CsJN3s
                    L6: CsJN5sdtc
                        L7: CsJN5sc
                        L7: CsJN5dcOdO0sc
                        L7: CsJN5dcN3dO0sc
                    L6: CsJN3dCd
                    L6: CsJN3dCdd
                    L6: CsJN3dN5dc
                L5: CCsJN
                    L6: CdCsJN
                L5: C2CsJN
            L4: CdsJ
                L5: CdBr1sCdd
                L5: CdCddCl1s
                L5: CdCddF1s
                L5: CdBr1sCd
                L5: CdCdCl1s
                L5: CdCdF1s
                L5: CdsJO
                    L6: COBr1sO2d
                    L6: COCl1sO2d
                    L6: COF1sO2d
                    L6: COJ-NOd
                    L6: HCdsJO
                    L6: CCJ=O
                        L7: CC(C)CJ=O
                            L8: CC(C)2CJ=O
                                L9: CC(C)(C=O)CJ=O
                                    L10: C=CC(C)(C=O)CJ=O
                                L9: C=CC(C)2CJ=O
                            L8: CC(C)(O)CJ=O
                                L9: C=CC(C)(O)CJ=O
                        L7: CCCJ=O
                            L8: C=OCCJ=O
                                L9: C=OC=OCJ=O
                            L8: C=C(C)CJ=O
                        L7: CsCJ=O
                        L7: C=CCJ=O
                        L7: OC=OCJ=O
                    L6: (O)CJO
                        L7: (O)CJOH
                        L7: (O)CJOC
                            L8: (O)CJOCH3
                            L8: (O)CJOCC
                            L8: (O)CJOCC2
                            L8: (O)CJOCC3
                    L6: SCJ=O
                L5: Cds_P
                    L6: C=C=CJ
                    L6: N=C=CJ
                L5: Cds_S
                    L6: C=CJC=O
                    L6: C=CJC=C
                        L7: cyclobutadiene-C1
                            L8: bicyclo[2.2.0]hexa-1(4),2,5-triene-C2
                        L7: 1,3-cyclopentadiene-vinyl-2
                    L6: cyclopropenyl-vinyl
                    L6: cyclobutene-vinyl
                        L7: bicyclo[2.1.0]pent-2-ene-C2
                            L8: tricyclo[2.1.1.0(1,4)]hex-2-ene-C2
                        L7: bicyclo[2.2.0]hexa-2,5-diene-C2
                    L6: cyclopentene-vinyl
                        L7: bicyclo[2.1.1]hex-2-ene-C2
                    L6: 1,3-cyclopentadiene-vinyl-1
                    L6: CCCJ=C=O
                        L7: CC(C)CJ=C=O
                        L7: C=C(C)CJ=C=O
                    L6: OC=CJCb
                    L6: N=C=CJC
                L5: S2s-CJ=C
                L5: C=CJO
                L5: CdJ-NN
                L5: CdJ-CdN
                    L6: CdJ-CddN
                L5: CdJ-NdO
                L5: CdJ-NdC
                L5: CdJ-HN3d
                    L6: CdJ-H(N3dOs)
                    L6: CdJ-H(N3dCO)
                    L6: CdJ-H(N3dN3d)
                    L6: CdJ-H(N3dCd)
                L5: CdJ-HN5dc
            L4: CtJ
                L5: Acetyl
            L4: CbJ
            L4: C=SJ
                L5: C=SJ-S2s
                L5: C=SJ-H
                L5: C=SJ-C
                    L6: C=SJ-Cd
                    L6: C=SJ-Cs
        L3: OJ
            L4: HOJ
            L4: COJ
                L5: CCOJ
                    L6: C=OCOJ
                        L7: C=CC(C)(C=O)OJ
                        L7: CC(C)(C=O)OJ
                        L7: C=OC=OOJ
                    L6: CC(C)OJ
                        L7: CC(C)2OJ
                            L8: C=CC(C)2OJ
                        L7: CC(C)(O)OJ
                            L8: C=CC(C)(O)OJ
                    L6: C=C(C)OJ
                L5: CdsOJ
                    L6: RC=COJ
                        L7: C=COJ
                        L7: N=COJ
                    L6: OJC=O
                        L7: OC=OOJ
                L5: OCOJ
                L5: SCOJ
                L5: CsOJ
                    L6: H3COJ
                L5: CbOJ
            L4: OOJ
                L5: ROOJ
                    L6: C(=O)OOJ
                    L6: C3COOJ
                    L6: SOOJ
                L5: HOOJ
            L4: SOJ
                L5: O2sJ-S2s
                L5: O2sJ-S4d
                    L6: O2sJ-(S4d-OdO)
                    L6: O2sJ-(S4d-OdC)
                    L6: O2sJ-(S4d-OdH)
                    L6: O2sJ-(S4d-CdC)
                L5: O2sJ-S6d
            L4: O2sJ-N
                L5: O2sJ-N3s
                    L6: O2sJ-N3sC
                        L7: O2sJ-N3sCO
                    L6: O2sJ-N3sO2s
                    L6: O2sJ-N3s(N5sdcO0sc)
                L5: O2sJ-N5sdtc
                    L6: O2sJ-N5dcOd
                        L7: O2sJ-N5dcOdO0sc
                L5: O2sJ-N1sc
                L5: O2sJ-N3dN3d
                L5: O2sJ-N3dCd
        L3: SiJ
        L3: SJ
            L4: S2J
                L5: S2J-H
                L5: S2J-C
                    L6: S2J-Cs
                        L7: S2sJ-(CsHHH)
                        L7: S2J-(Cs-Cb)
                    L6: S2J-Ct
                    L6: S2J-Cb
                    L6: S2J-Cd
                    L6: S2J-C=S
                    L6: S2J-CO
                L5: S2J-S2s
                    L6: S2J-S2s-H
                    L6: S2J-S2s-Cs
                    L6: S2J-S2s-S2s
                L5: S2sJ-O
            L4: S4sJ
                L5: S4sJ-CCC
                L5: S4sJ-OCC
            L4: S4dJ
                L5: S4dJ-OdH
                L5: S4dJ-OdO
            L4: S6sJ
                L5: S6sJ-CCCCC
            L4: S6dJ
                L5: S6dJ-OdOCC
            L4: S6ddJ
                L5: S6ddJ-OdOdH
                L5: S6ddJ-OdOdO
        L3: NJ
            L4: N5scJ-HNO
            L4: N5scJ-NNO
            L4: N5scJ-HOO
            L4: N5scJ-NOO
            L4: N5scJ-CHO
            L4: N5scJ-CNO
            L4: N5scJ-COO
            L4: N5scJ-CCO
            L4: N5dcJ-NOd
            L4: N5dcJ-NdO
            L4: N5dcJ-CdO
            L4: N3sJ-NN
            L4: N3sJ-NO
            L4: N3sJ-OO
            L4: N3sJ-CN
            L4: N3sJ-CO
                L5: N3sJ-CtO
            L4: N3sJ
                L5: NH2J
                L5: NHJ_C
                    L6: NHJ_Cd
                L5: NHJ_O
                L5: NHJ_N
                    L6: NHJ_N3d
                    L6: NHJ_N5dc
                L5: NJ_CC
                    L6: NJ_CCd
                    L6: NJ_CCO
            L4: N3dJ
                L5: N3dJ_C
                    L6: N3dJ_Cdd
                L5: N3dJ_O
                L5: N3dJ_N
                    L6: N3dJ_N5dc
                    L6: N3dJ_N3d
    L2: RJ2_triplet
        L3: CJ2_triplet
            L4: OsCsJ2H_triplet
            L4: CsJ2_triplet
                L5: CH2_triplet
                L5: CsJ2_P_triplet
                    L6: CsCVal7_triplet
                        L7: CsCF_triplet
                        L7: CsCCl_triplet
                        L7: CsCBr_triplet
                    L6: CsCsJ2_triplet
                        L7: CCJ2_triplet
                    L6: PhCH_triplet
                    L6: AllylJ2_triplet
                L5: CsJ2_S_triplet
            L4: CdJ2_triplet
                L5: CCdJ2_triplet
                    L6: CdCdJ2_triplet
                    L6: (CO)CdJ2_triplet
                L5: NCdJ2_triplet
            L4: CdJ2-Sd_triplet
        L3: Oa_triplet
        L3: SiJ2_triplet
        L3: SJ2_triplet
        L3: NJ2_triplet
            L4: N3sJ2
                L5: NHJ2
                L5: NJ2_C
                L5: NJ2_O
    L2: RJ3
        L3: CJ3
        L3: SiJ3
"""
)

