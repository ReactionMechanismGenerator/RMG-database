#!/usr/bin/env python
# encoding: utf-8

name = "HAN"
shortDesc = "Things needed for HAN modeling"
longDesc = """
Collection of things needed for the modeling of Hydroxyl Ammonium Nitrate
"""

entry(
    index = 1,
    label = 'HAN',
    molecule = 
"""
1  O u0 p3 c-1 {2,S} {10,H}
2  N u0 p0 c+1 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,S} {7,S}
5  N u0 p1 c0 {6,S} {8,S} {9,S} {7,H}
6  O u0 p2 c0 {5,S} {10,S}
7  H u0 p0 c0 {4,S} {5,H}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S} {1,H}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.53818, 0.0464979, -0.000105474, 2.05017e-07, -1.60235e-10, -30604.1, 11.6971],
                Tmin = (10, 'K'),
                Tmax = (404.918, 'K'),
            ),
            NASAPolynomial(
                coeffs = [3.8657, 0.0334818, -2.10245e-05, 6.32509e-09, -7.30793e-13, -30550.5, 11.4032],
                Tmin = (404.918, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (
            -211.468,
            'kJ/mol',
        ),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (232.805, 'J/(mol*K)'),
    ),
    shortDesc = """G4""",
    longDesc = 
"""
G4 calculation, no BACs, calculated by David Farina.
Based on geometry from Banerjee 2016 http://dx.doi.org/10.1016/j.susc.2016.05.005
Looks like it made the "Covalent" structure during optimization,
so the adjacency list is drawn that way.  [O-][N+](=O)O.NO 

 Thermodynamics for HAN:
   Enthalpy of formation (0 K)     =   -50.542 kcal/mol
   Enthalpy of formation (298 K)   =   -55.814 kcal/mol
   Entropy of formation (298 K)    =    84.496 cal/(mol*K)
""",
)

entry(
    index = 2,
    label = 'HANionic',
    molecule = 
"""
1  O u0 p3 c-1 {2,S} {10,H}
2  N u0 p0 c+1 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  O u0 p3 c-1 {2,S} {7,H}
5  N u0 p0 c+1 {6,S} {8,S} {9,S} {7,S}
6  O u0 p2 c0 {5,S} {10,S}
7  H u0 p0 c0 {4,H} {5,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S} {1,H}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.53818, 0.0464979, -0.000105474, 2.05017e-07, -1.60235e-10, -30604.1, 11.6971],
                Tmin = (10, 'K'),
                Tmax = (404.918, 'K'),
            ),
            NASAPolynomial(
                coeffs = [3.8657, 0.0334818, -2.10245e-05, 6.32509e-09, -7.30793e-13, -30550.5, 11.4032],
                Tmin = (404.918, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (
            -211.468,
            'kJ/mol',
        ),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (232.805, 'J/(mol*K)'),
    ),
    shortDesc = """G4""",
    longDesc = 
"""
G4 calculation, no BACs, calculated by David Farina.
Based on geometry from Banerjee 2016 http://dx.doi.org/10.1016/j.susc.2016.05.005

This thermo is for the "covalent" form but the adjacency list
is for the "ionic" form, so that if we come across it in a model
(eg as an adsorbate) we still have thermo.

 Thermodynamics for HAN:
   Enthalpy of formation (0 K)     =   -50.542 kcal/mol
   Enthalpy of formation (298 K)   =   -55.814 kcal/mol
   Entropy of formation (298 K)    =    84.496 cal/(mol*K)
""",
)


entry(
    index = 3,
    label = 'NH4NO3', # Ammonium Nitrate, AN
    molecule = 
"""
1 O u0 p3 c-1 {2,S} {6,H}
2 N u0 p0 c+1 {1,S} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 O u0 p3 c-1 {2,S} {7,H}
5 N u0 p0 c+1 {6,S} {7,S} {8,S} {9,S}
6 H u0 p0 c0 {5,S} {1,H}
7 H u0 p0 c0 {5,S} {4,H}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([  300., 400., 500., 600., 700., 800., 900.,1000],'K'),
        Cpdata = ([22.37,25.83,28.84,31.39,33.54,35.36,36.92,38.27],'cal/(mol*K)'),
        H298 = (-61.8,'kcal/mol','+|-',5.),
        S298 = (81.82,'cal/(mol*K)'),
    ),
    shortDesc = """Hildenbrand 2010 Revised Thermochemistry of Gaseous Ammonium Nitrate, NH4NO3(g)""",
    longDesc = 
"""
Table 3 from:

Revised Thermochemistry of Gaseous Ammonium Nitrate, NH4NO3(g)
D. L. Hildenbrand, K. H. Lau, and D. Chandra
J. Phys. Chem. A 2010, 114, 43, 11654–11655
https://doi-org.ezproxy.neu.edu/10.1021/jp105773q

Does not agree, even within uncertainty, with an adjoining theoretical calculation.
""",
)
