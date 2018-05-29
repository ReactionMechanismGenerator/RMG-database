#!/usr/bin/env python
# encoding: utf-8

name = "Iodinated_Hydrocarbons"

shortDesc = u"Iodinated Hydrocarbons"
longDesc = u"""

1. JPL NASA Evaluation #18 for H298 and S298 (no Cp data reported, no values for C6H5I)
reference: Burkholder,J. B. et al.Chemical Kinetics and Photochemical Data for Use in Atmospheric Studies; Evaluation No. 18, JPL Publication 15–10; Jet Propulsion Laboratory: Pasadena, CA, 2015
Table 6-2

2. webbook.nist.gov for some Cp data (I, HI, I2)
Experimental values curated in the following references:

3. 1976 Benson or iodoalkanes  = Thermochemical Kinetics (book), 2nd edition, by Sidney Benson

"""

entry(
    index = 0,
    label = "I",
    molecule =
"""
multiplicity 2
1 I u1 p3 c0
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000], 'K'),
        Cpdata=([20.79, 20.79, 20.79, 20.79, 20.79, 20.80, 20.93, 21.31], 'cal/(mol*K)'),
        H298=(106.760, 'kJ/mol'),
        S298=(180.787, 'J/(mol*K)'),
    ),
    shortDesc=u"""JPL Evaluation 18 + webbook.nist.gov (Cp data)""",
    longDesc=
    u"""
Burkholder,J. B. et al.Chemical Kinetics and Photochemical Data for Use in Atmospheric Studies; Evaluation No. 18, JPL Publication 15–10; Jet Propulsion Laboratory: Pasadena, CA, 2015
Table 6-2
https://webbook.nist.gov/cgi/cbook.cgi?ID=C14362448&Units=SI&Mask=1&Type=JANAFG&Table=on#JANAFG (Cp data)
    """,
)

entry(
    index = 1,
    label = "I2",
    molecule =
"""
1 I u0 p3 c0 {2,S}
2 I u0 p3 c0 {1,S}
""",
    thermo=ThermoData(
        Tdata=([500, 600, 800, 1000, 1500, 2000], 'K'),
        Cpdata=([37.48, 37.60, 37.79, 38.06, 39.54, 42.86], 'J/(mol*K)'),
        H298=(62.42, 'kJ/mol'),
        S298=(260.687, 'J/(mol*K)'),
    ),
    shortDesc=u"""JPL Evaluation 18 + webbook.nist.gov""",
    longDesc=
    u"""
Burkholder,J. B. et al.Chemical Kinetics and Photochemical Data for Use in Atmospheric Studies; Evaluation No. 18, JPL Publication 15–10; Jet Propulsion Laboratory: Pasadena, CA, 2015
Table 6-2
https://webbook.nist.gov/cgi/cbook.cgi?ID=C7553562&Units=SI&Mask=1&Type=JANAFG&Table=on#JANAFG (Cp data)
    """,
)

entry(
    index = 2,
    label = "HI",
    molecule =
"""
1 I  u0 p3 c0 {2,S}
2 H  u0 p0 c0 {1,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500, 2000], 'K'),
        Cpdata=([29.17, 29.30, 29.77, 30.39, 31.77, 33.11, 35.39, 36.63], 'cal/(mol*K)'),
        H298=(26.50, 'kJ/mol'),
        S298=(206.589, 'J/(mol*K)'),
    ),
    shortDesc=u"""JPL Evaluation 18 + webbook.nist.gov""",
    longDesc=
    u"""
Burkholder,J. B. et al.Chemical Kinetics and Photochemical Data for Use in Atmospheric Studies; Evaluation No. 18, JPL Publication 15–10; Jet Propulsion Laboratory: Pasadena, CA, 2015
Table 6-2
https://webbook.nist.gov/cgi/cbook.cgi?ID=C10034852&Units=SI&Type=JANAFG&Table=on#JANAFG (Cp data)
    """,
)

entry(
    index = 3,
    label = "CH3I",
    molecule =
"""
1 C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H  u0 p0 c0 {1,S}
3 H  u0 p0 c0 {1,S}
4 H  u0 p0 c0 {1,S}
5 I  u0 p3 c0 {1,S}
""",
    thermo=ThermoData(
        Tdata=([300, 500, 800, 1000, 1500], 'K'),
        Cpdata=([10.6, 14.0, 17.5, 19.2, 21.9], 'cal/(mol*K)'),
        H298=(13.22, 'kJ/mol'),
        S298=(253.70, 'J/(mol*K)'),
    ),
    shortDesc = u"""JPL Evaluation 18 (H298, S298) + 1976 Benson (Cp data)""",
    longDesc =
u"""
Burkholder,J. B. et al.Chemical Kinetics and Photochemical Data for Use in Atmospheric Studies; Evaluation No. 18, JPL Publication 15–10; Jet Propulsion Laboratory: Pasadena, CA, 2015
Table 6-2 (H298 and S298)
1976 Benson (Cp data), Table A.11. p.297
""",
)

entry(
    index = 4,
    label = "CH2I2",
    molecule =
"""
1 C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H  u0 p0 c0 {1,S}
3 H  u0 p0 c0 {1,S}
4 I  u0 p3 c0 {1,S}
5 I  u0 p3 c0 {1,S}
""",
    thermo=ThermoData(
        Tdata=([300, 500, 800, 1000, 1500], 'K'),
        Cpdata=([13.9, 17.3, 20.1, 21.3, 23.2], 'cal/(mol*K)'),
        H298=(107.9, 'kJ/mol'),
        S298=(309.39, 'J/(mol*K)'),
    ),
    shortDesc = u"""JPL Evaluation 18 (H298, S298) + 1976 Benson (Cp data)""",
    longDesc =
u"""
Burkholder,J. B. et al.Chemical Kinetics and Photochemical Data for Use in Atmospheric Studies; Evaluation No. 18, JPL Publication 15–10; Jet Propulsion Laboratory: Pasadena, CA, 2015
Table 6-2 (H298 and S298)
1976 Benson (Cp data), Table A.11. p.297
""",
)

entry(
    index = 5,
    label = "C2H5I",
    molecule =
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 I u0 p3 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 500, 800, 1000], 'K'),
        Cpdata=([15.4, 22.3, 28.8, 32.0], 'cal/(mol*K)'),
        H298=(-2.1, 'kcal/mol'),
        S298=(70.7, 'cal/(mol*K)'),
    ),
    shortDesc = u""" 1976 Benson""",
    longDesc =
u"""
1976 Benson, Table A.11. p.297
""",
)

entry(
    index = 6,
    label = "C2H3I",
    molecule =
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 I u0 p3 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 500, 800, 1000], 'K'),
        Cpdata=([13.6, 18.4, 22.7, 24.6], 'cal/(mol*K)'),
        H298=(30.8, 'kcal/mol'),
        S298=(68.1, 'cal/(mol*K)'),
    ),
    shortDesc = u""" 1976 Benson, CH2=CHI""",
    longDesc =
u"""
1976 Benson, Table A.11. p.297
""",
)

entry(
    index = 7,
    label = "CH3COI",
    molecule =
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 O u0 p2 c0 {2,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 I u0 p3 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 500], 'K'),
        Cpdata=([17.5, 20.9], 'cal/(mol*K)'),
        H298=(-30.3, 'kcal/mol'),
        S298=(76.0, 'cal/(mol*K)'),
    ),
    shortDesc = u""" 1976 Benson""",
    longDesc =
u"""
1976 Benson, Table A.11. p.297
""",
)

entry(
    index = 8,
    label = "C3H5I",
    molecule =
"""
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {3,S} {6,S}
3 C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 I u0 p3 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000], 'K'),
        Cpdata=([18.5, 22.4, 26.2, 28.9, 33.5, 36.9], 'cal/(mol*K)'),
        H298=(22.9, 'kcal/mol'),
        S298=(78.6, 'cal/(mol*K)'),
    ),
    shortDesc = u""" 1976 Benson, Zach supplementary Info""",
    longDesc =
u"""
1976 Benson, Zach Supplementary Info Table S1 (p10-I)
SUPPLEMENTARY INFORMATION for 
Phenyl Radical + Propene: A Prototypical Reaction Surface for Aromatic-Catalyzed 1,2Hydrogen-Migration and Subsequent Resonance Stabilized Radical Formation 
Buras, Z. J. et al.
""",
)

entry(
    index = 9,
    label = "C6H5I",
    molecule =
"""
1  C u0 p0 c0 {2,D} {6,S} {7,S}
2  C u0 p0 c0 {1,D} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {5,S} {10,S}
5  C u0 p0 c0 {4,S} {6,D} {11,S}
6  C u0 p0 c0 {1,S} {5,D} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 I u0 p3 c0 {6,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000], 'K'),
        Cpdata=([24.0, 30.6, 36.3, 41.1, 47.7, 52.3], 'cal/(mol*K)'),
        H298=(38.7, 'kcal/mol'),
        S298=(80.1, 'cal/(mol*K)'),
    ),
    shortDesc = u""" 1976 Benson, Zach supplementary Info""",
    longDesc =
u"""
1976 Benson, Zach Supplementary Info Table S1 (p10-I)
SUPPLEMENTARY INFORMATION for 
Phenyl Radical + Propene: A Prototypical Reaction Surface for Aromatic-Catalyzed 1,2Hydrogen-Migration and Subsequent Resonance Stabilized Radical Formation 
Buras, Z. J. et al.
""",
)

entry(
    index = 10,
    label = "C6H5CH2I",
    molecule =
"""
1  C u0 p0 c0 {2,S} {4,D} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  I u0 p3 c0 {2,S}
4  C u0 p0 c0 {1,D} {5,S} {11,S}
5  C u0 p0 c0 {4,S} {6,D} {12,S}
6  C u0 p0 c0 {5,D} {7,S} {13,S}
7  C u0 p0 c0 {6,S} {8,D} {14,S}
8  C u0 p0 c0 {1,S} {7,D} {15,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000], 'K'),
        Cpdata=([28.1, 36.3, 34.9, 49.6, 58.5, 64.7], 'cal/(mol*K)'),
        H298=(30.0, 'kcal/mol'),
        S298=(93.0, 'cal/(mol*K)'),
    ),
    shortDesc = u""" 1976 Benson, Zach supplementary Info""",
    longDesc =
u"""
1976 Benson, Zach Supplementary Info Table S1 (p10-I)
SUPPLEMENTARY INFORMATION for 
Phenyl Radical + Propene: A Prototypical Reaction Surface for Aromatic-Catalyzed 1,2Hydrogen-Migration and Subsequent Resonance Stabilized Radical Formation 
Buras, Z. J. et al.
""",
)

entry(
    index = 11,
    label = "C6H5CH2CHICH3",
    molecule =
"""
1  C u0 p0 c0 {2,S} {6,D} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {13,S}
4  I u0 p3 c0 {3,S} 
5  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
6  C u0 p0 c0 {1,D} {7,S} {17,S}
7  C u0 p0 c0 {6,S} {8,D} {18,S}
8  C u0 p0 c0 {7,D} {9,S} {19,S}
9  C u0 p0 c0 {8,S} {10,D} {20,S}
10 C u0 p0 c0 {1,S} {9,D} {21,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000], 'K'),
        Cpdata=([40.1, 51.7, 61.6, 69.5, 81.4, 89.6], 'cal/(mol*K)'),
        H298=(17.5, 'kcal/mol'),
        S298=(111.0, 'cal/(mol*K)'),
    ),
    shortDesc = u""" 1976 Benson, Zach supplementary Info""",
    longDesc =
u"""
1976 Benson, Zach Supplementary Info Table S1 (p10-I)
SUPPLEMENTARY INFORMATION for 
Phenyl Radical + Propene: A Prototypical Reaction Surface for Aromatic-Catalyzed 1,2Hydrogen-Migration and Subsequent Resonance Stabilized Radical Formation 
Buras, Z. J. et al.
""",
)

entry(
    index = 12,
    label = "INO",
    molecule =
"""
1 O u0 p2 c0 {2,D}
2 N u0 p1 c0 {1,D} {3,S}
3 I u0 p3 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 500, 800, 1000, 1500], 'K'),
        Cpdata=([11.2, 11.9, 12.7, 13.0, 13.5], 'cal/(mol*K)'),
        H298=(121, 'kJ/mol'),
        S298=(282.8, 'J/(mol*K)'),
    ),
    shortDesc = u""" JPL Evaluation 18 (H298, S298) + 1976 Benson (Cp)""",
    longDesc =
u"""
Burkholder,J. B. et al.Chemical Kinetics and Photochemical Data for Use in Atmospheric Studies; Evaluation No. 18, JPL Publication 15–10; Jet Propulsion Laboratory: Pasadena, CA, 2015
Table 6-2 (H298 and S298)
1976 Benson (Table A.9, p. 292)
""",
)
