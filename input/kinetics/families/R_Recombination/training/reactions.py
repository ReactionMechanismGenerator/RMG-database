#!/usr/bin/env python
# encoding: utf-8

name = "R_Recombination/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 1,
    label = "CH3O2 <=> O2 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.09e+14, 's^-1'), n=0.25, Ea=(33.3, 'kcal/mol'), T0=(1, 'K')),
    shortDesc = u"""Method CBS-QB3 w/ 1-d Hindered rotor corrections""",
    longDesc = 
u"""
High-Pressure Rate Rules for Alkyl + O2 Reactions. 1. The Dissociation, Concerted Elimination, and Isomerization Channels of the Alkyl Peroxy Radical
Stephanie M. Villano, Lam K. Huynh, Hans-Heinrich Carstensen, and Anthony M. Dean
The Journal of Physical Chemistry A 2011 115 (46), 13425-13442
dx.doi.org/10.1021/jp2079204

Method CBS-QB3 w/ 1-d Hindered rotor corrections
""",
)

entry(
    index = 2,
    label = "C2H5O2 <=> O2 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.49e+21, 's^-1'), n=-2.41, Ea=(35.8, 'kcal/mol'), T0=(1, 'K')),
    shortDesc = u"""Method CBS-QB3 w/ 1-d Hindered rotor corrections""",
    longDesc = 
u"""
High-Pressure Rate Rules for Alkyl + O2 Reactions. 1. The Dissociation, Concerted Elimination, and Isomerization Channels of the Alkyl Peroxy Radical
Stephanie M. Villano, Lam K. Huynh, Hans-Heinrich Carstensen, and Anthony M. Dean
The Journal of Physical Chemistry A 2011 115 (46), 13425-13442
dx.doi.org/10.1021/jp2079204

Method CBS-QB3 w/ 1-d Hindered rotor corrections
""",
)

entry(
    index = 3,
    label = "C3H7O2 <=> O2 + C3H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.52e+23, 's^-1'), n=-2.71, Ea=(36.4, 'kcal/mol'), T0=(1, 'K')),
    shortDesc = u"""Method CBS-QB3 w/ 1-d Hindered rotor corrections""",
    longDesc = 
u"""
High-Pressure Rate Rules for Alkyl + O2 Reactions. 1. The Dissociation, Concerted Elimination, and Isomerization Channels of the Alkyl Peroxy Radical
Stephanie M. Villano, Lam K. Huynh, Hans-Heinrich Carstensen, and Anthony M. Dean
The Journal of Physical Chemistry A 2011 115 (46), 13425-13442
dx.doi.org/10.1021/jp2079204

Method CBS-QB3 w/ 1-d Hindered rotor corrections
""",
)

entry(
    index = 4,
    label = "1-hydroxybutyl + O2 <=> 1-hydroxybutylO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.36e+12, 'cm^3/(mol*s)'),
        n = -0.085,
        Ea = (-567.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""CBS-QB3 w/ 1-d HR""",
    longDesc = 
u"""
Reference: Low-Temperature Combustion Chemistry of n-Butanol: Principal Oxidation Pathways of Hydroxybutyl Radicals 
DOI: 10.1021/jp403792t
""",
)

entry(
    index = 5,
    label = "NO2 + NO2 <=> N2O4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.63e+08, 'm^3/(mol*s)', '+|-', 3.16e+07),
        n = -1.1,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (600, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (2.09e+07, 'Pa'),
    ),
    reference = Article(
        authors = ["Borrell, P.", "Cobos, C.J.", "Luther, K."],
        title = u'Falloff curve and specific rate constants for the reaction NO2 + NO2 N2O4',
        journal = "J. Phys. Chem.",
        volume = "92",
        pages = """4377-4384""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988BOR/COB4377-4384:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
Bath gas: N2
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 6,
    label = "NO + O2 <=> NO3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (117000, 'm^3/(mol*s)', '*|/', -1),
        n = 0,
        Ea = (13.386, 'kJ/mol', '+|-', -0.001),
        T0 = (1, 'K'),
        Tmin = (473, 'K'),
        Tmax = (703, 'K'),
        Pmin = (1333, 'Pa'),
        Pmax = (33600, 'Pa'),
    ),
    reference = Article(
        authors = ["Ashmore, P.G.", "Burnett, M.G."],
        title = u'Concurrent molecular and free radical mechanisms in the thermal decomposition of nitrogen dioxide',
        journal = "J. Chem. Soc. Faraday Trans. 2",
        volume = "58",
        pages = """253""",
        year = "1962",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1962ASH/BUR253:5",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
Uncertainty: 3.0
Bath gas: NO2
Excitation technique: Thermal
Analytical technique: Pressure measurement
""",
)

entry(
    index = 7,
    label = "NO2 + NO3-2 <=> N2O5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (366000, 'm^3/(mol*s)', '+|-', 57700),
        n = 0.2,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (400, 'K'),
        Pmin = (100000, 'Pa'),
        Pmax = (9e+07, 'Pa'),
    ),
    reference = Article(
        authors = ["Hahn, J.", "Luther, K.", "Troe, J."],
        title = u'Experimental and Theoretical Study of the Temperature and Pressure Dependences of the Recombination Reactions O+NO2(+M)\u2192\x92NO3(+M) and NO2+NO3(+M)\u2192\x92N-2O5(+M)',
        journal = "Phys. Chem. Chem. Phys.",
        pages = """5098-5104""",
        year = "2000",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2000HAH/LUT5098-5104:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
Pressure dependence: Rate constant is high pressure limit
Experimental procedure: Static or low flow - Data taken vs time
Excitation technique: Flash photolysis (laser or conventional)
Time resolution: In real time
Analytical technique: Vis-UV absorption

Theoretical modeling of k0, k and Fc=0.38 exp(-T/4900K) led to consistency with the experimental data.
""",
)

entry(
    index = 8,
    label = "NO2 + OH <=> HNO3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+07, 'm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (400, 'K'),
    ),
    reference = Article(
        authors = ["Williams, C.F.", "Pogrebnya, S.K.", "Clary, D.C."],
        title = u'Quantum study on the branching ratio of the reaction NO2+OH',
        journal = "J. Chem. Phys.",
        volume = "126",
        pages = """154321""",
        year = "2007",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2007WIL/POG154321:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Other theoretical""",
    longDesc = 
u"""
Pressure dependence: Rate constant is high pressure limit

Quantum dynamics calculations. Reaction potential energy suraface was studied using quantum chemistry.
""",
)

entry(
    index = 9,
    label = "NO2-2 + OH <=> HNO3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.205e+06, 'm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (400, 'K'),
    ),
    reference = Article(
        authors = ["Williams, C.F.", "Pogrebnya, S.K.", "Clary, D.C."],
        title = u'Quantum study on the branching ratio of the reaction NO2+OH',
        journal = "J. Chem. Phys.",
        volume = "126",
        pages = """154321""",
        year = "2007",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2007WIL/POG154321:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Other theoretical""",
    longDesc = 
u"""
Pressure dependence: Rate constant is high pressure limit
Reference reaction: 2007WIL/POG154321:4
Branching ration: 0.05
Quantum dynamics calculations. Reaction potential energy suraface was studied using quantum chemistry.
""",
)

entry(
    index = 10,
    label = "C5H5 + C2H5 <=> C7H10",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.34e+15, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (-0.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: ethyl + CPDyl <=> ethylCPD
""",
)

entry(
    index = 15,
    label = "CH3NO2 <=> CH3 + NO2",
    kinetics = Arrhenius(A=(1.8e+16, 's^-1'), n=0, Ea=(58500, 'cal/mol'), T0=(1, 'K')),
    rank = 1,
    shortDesc = u"""Experimental, P. Glarborg, A.B. Bendtsen, J.A. Miller""",
    longDesc = 
u"""
P. Glarborg, A.B. Bendtsen, J.A. Miller
Nitromethane Dissociation: Implications for the CH3 + NO2 Reaction
International Journal of Chemical Kinetics Volume 31, Issue 9, pages 591-602, 1999
DOI: 10.1002/(SICI)1097-4601(1999)31:9<591::AID-KIN1>3.0.CO;2-E

Also appears in the Nitrogen_Glarborg_Zhang_et_al library (index 671)
and in the Nitrogen_Glarborg_Gimenez_et_al library (index 953)

The high-pressure limit kinetics was taken. Troe coefficients are:
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.8e+16, 's^-1'), n=0, Ea=(58500, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.259e+17, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (42000, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.183,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        efficiencies = {},
    ),
""",
)

entry(
    index = 20,
    label = "CH3 + CH3 <=> C2H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.45e+14, 'cm^3/(mol*s)'), n=-0.538, Ea=(135.1, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(2000, 'K')),
    rank = 2,
    shortDesc = u"""CASPT2/cc-pvdz""",
    longDesc = 
u"""
S.J. Klippenstein, Y. Georgievskiia, L.B. Hardingb
Predictive theory for the combination kinetics of two alkyl radicals
Phys. Chem. Chem. Phys., 2006, 8, 1133-1147
doi: 10.1039/B515914H
""",
)

entry(
    index = 21,
    label = "CH3 + C2H5 <=> C3H8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.23e+15, 'cm^3/(mol*s)'), n=-0.562, Ea=(20.5, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(2000, 'K')),
    rank = 2,
    shortDesc = u"""CASPT2/cc-pvdz""",
    longDesc = 
u"""
S.J. Klippenstein, Y. Georgievskiia, L.B. Hardingb
Predictive theory for the combination kinetics of two alkyl radicals
Phys. Chem. Chem. Phys., 2006, 8, 1133-1147
doi: 10.1039/B515914H
""",
)

entry(
    index = 22,
    label = "C2H5 + C2H5 <=> C4H10",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.73e+14, 'cm^3/(mol*s)'), n=-0.699, Ea=(-3.2, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(2000, 'K')),
    rank = 2,
    shortDesc = u"""CASPT2/cc-pvdz""",
    longDesc = 
u"""
S.J. Klippenstein, Y. Georgievskiia, L.B. Hardingb
Predictive theory for the combination kinetics of two alkyl radicals
Phys. Chem. Chem. Phys., 2006, 8, 1133-1147
doi: 10.1039/B515914H
""",
)



entry(
    index = 23,
    label = "C5H5 + CH3 <=> C6H8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.38482e-08, 'cm^3/(molecule*s)'),
        n = -0.7,
        Ea = (-0.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2009_Sharma_C5H5_CH3_highP""",
    longDesc = 
u"""
Taken from entry: c-C5H5 + CH3 <=> C5H5CH3-5
""",
)

entry(
    index = 24,
    label = "C6H7 + H <=> C6H8-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.582e-10, 'cm^3/(molecule*s)'),
        n = -0.1,
        Ea = (0.4, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2009_Sharma_C5H5_CH3_highP""",
    longDesc = 
u"""
Taken from entry: R2 + H <=> C5H5CH3-5
""",
)

entry(
    index = 25,
    label = "C6H7-2 + H <=> C6H8-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.7982e-11, 'cm^3/(molecule*s)'),
        n = 0.3,
        Ea = (0.1, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2009_Sharma_C5H5_CH3_highP""",
    longDesc = 
u"""
Taken from entry: R2 + H <=> C5H5CH3-1
""",
)

entry(
    index = 26,
    label = "C6H7-3 + H <=> C6H8-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.74338e-12, 'cm^3/(molecule*s)'),
        n = 0.6,
        Ea = (-0.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2009_Sharma_C5H5_CH3_highP""",
    longDesc = 
u"""
Taken from entry: R1 + H <=> C5H5CH3-1
""",
)

entry(
    index = 27,
    label = "C6H7-4 + H <=> C6H8-5",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.50356e-10, 'cm^3/(molecule*s)'),
        n = 0.1,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2009_Sharma_C5H5_CH3_highP""",
    longDesc = 
u"""
Taken from entry: R2 + H <=> C5H5CH3-2
""",
)

entry(
    index = 28,
    label = "C6H7-5 + H <=> C6H8-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.6921e-12, 'cm^3/(molecule*s)'),
        n = 0.5,
        Ea = (-0.1, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2009_Sharma_C5H5_CH3_highP""",
    longDesc = 
u"""
Taken from entry: R3 + H <=> C5H5CH3-2
""",
)

entry(
    index = 29,
    label = "C6H7-6 + H <=> C6H8-7",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.48677e-12, 'cm^3/(molecule*s)'),
        n = 0.6,
        Ea = (-0.8, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2009_Sharma_C5H5_CH3_highP""",
    longDesc = 
u"""
Taken from entry: R4 + H <=> C5H5CH3-5
""",
)



entry(
    index = 30,
    label = "C10H9 <=> C10H8 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.89e+16, 's^-1'), n=-0.28, Ea=(68.378, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring\2016_Mebel_C10H9_highP""",
    longDesc = 
u"""
Taken from entry: W111 <=> P114 + H
""",
)



entry(
    index = 31,
    label = "C3H3 + C7H7 <=> C10H10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.781e+17, 'cm^3/(mol*s)'),
        n = -1.568,
        Ea = (0.4547, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring\2012_Matsugi_C3H3_C7H7_highP""",
    longDesc = 
u"""
Taken from entry: C3H3 + C7H7 <=> W1
""",
)

entry(
    index = 32,
    label = "C3H3-2 + C7H7 <=> C10H10-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.144e+19, 'cm^3/(mol*s)'),
        n = -2.163,
        Ea = (1.195, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring\2012_Matsugi_C3H3_C7H7_highP""",
    longDesc = 
u"""
Taken from entry: C3H3 + C7H7 <=> W2
""",
)

entry(
    index = 33,
    label = "C10H10-3 <=> C10H9-2 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.431e+15, 's^-1'), n=-0.34, Ea=(77.615, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring\2012_Matsugi_C3H3_C7H7_highP""",
    longDesc = 
u"""
Taken from entry: W10 <=> P5 + H
""",
)

entry(
    index = 34,
    label = "C10H10-4 <=> C10H9-3 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.081e+15, 's^-1'), n=-0.263, Ea=(86.584, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring\2012_Matsugi_C3H3_C7H7_highP""",
    longDesc = 
u"""
Taken from entry: W17 <=> P9 + H
""",
)

entry(
    index = 35,
    label = "C10H10-5 <=> C10H9-4 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.899e+16, 's^-1'), n=-0.42, Ea=(88.738, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring\2012_Matsugi_C3H3_C7H7_highP""",
    longDesc = 
u"""
Taken from entry: W17 <=> P10 + H
""",
)

