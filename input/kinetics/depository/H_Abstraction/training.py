#!/usr/bin/env python
# encoding: utf-8

name = "H_Abstraction/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""

entry(
    index = 301,
    reactant1 = 
"""
H2O2
1  *1 O 0 {2,S} {3,S}
2     O 0 {1,S} {4,S}
3  *2 H 0 {1,S}
4     H 0 {2,S}
""",
    reactant2 = 
"""
butan-1-ol-4-yl
1  *3 C 1 {2,S}
2     C 0 {1,S} {3,S}
3     C 0 {2,S} {4,S}
4     C 0 {3,S} {5,S}
5     O 0 {4,S}
""",
    product1 = 
"""
HO2
1  *3 O 1 {2,S}
2     O 0 {1,S}
""",
    product2 = 
"""
n-butanol
1  *1 C 0 {2,S} {6,S}
2     C 0 {1,S} {3,S}
3     C 0 {2,S} {4,S}
4     C 0 {3,S} {5,S}
5     O 0 {4,S}
6  *2 H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (2.88*2,"cm^3/(mol*s)"),
        n = 3.16,
        Ea = (0.75,"kcal/mol"),
        T0 = (1,"K"),
        Tmin = (600,"K"),
        Tmax = (2000,"K"),
    ),
    degeneracy = 2,
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/o HR corrections
H2O2 + *CH2CH2CH2CH2OH = nButanol + HO2

CBS-QB3 method was used to calculate electronic energy of reactants, products, and TS; frequencies were
calculated using B3LYP/CBSB7 method.  Arrhenius expression was computed using CanTherm: an asymmetric Eckart
tunneling correction was employed and the frequencies were scaled by 0.99 (as suggested by Montgomery et al.
J.Chem.Phys. 110 (1999) 2822-2827).  The external symmetry number for H2O2 was 2; the external symmetry number
for the remaining species and TS were set to 1.  The rate coefficient was computed at 600-2000K (in 200 K increments).

For nButanol+HO2=H2O2+*CH2CH2CH2CH2OH:
Moc et al. (AIP Conference Proceedings (2009) 1148 161-164 "The Unimolecular Decomposition
and H Abstraction Reactions by HO and HO2 from n-Butanol") report reaction barriers and
enthalpies(0 K); our CBS-QB3 calculations are shown in comparison (all units are kcal/mol).
                G3      CCSD(T)/cc-pVTZ     CBS-QB3
Barrier:        18.8        19.62           17.57
Enthalpy:       14.25       14.66           13.70
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 302,
    reactant1 = 
"""
H2O2
1  *1 O 0 {2,S} {3,S}
2     O 0 {1,S} {4,S}
3  *2 H 0 {1,S}
4     H 0 {2,S}
""",
    reactant2 = 
"""
butan-1-ol-3-yl
1     C 0 {2,S}
2  *3 C 1 {1,S} {3,S}
3     C 0 {2,S} {4,S}
4     C 0 {3,S} {5,S}
5     O 0 {4,S}
""",
    product1 = 
"""
HO2
1  *3 O 1 {2,S}
2     O 0 {1,S}
""",
    product2 = 
"""
n-butanol
1     C 0 {2,S}
2  *1 C 0 {1,S} {3,S} {6,S}
3     C 0 {2,S} {4,S}
4     C 0 {3,S} {5,S}
5     O 0 {4,S}
6  *2 H 0 {2,S}
""",
    kinetics = Arrhenius(
        A = (0.675*2,"cm^3/(mol*s)"),
        n = 3.42,
        Ea = (1.43,"kcal/mol"),
        T0 = (1,"K"),
        Tmin = (600,"K"),
        Tmax = (2000,"K"),
    ),
    degeneracy = 2,
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/o HR corrections
H2O2 + CH3*CHCH2CH2OH = nButanol + HO2

CBS-QB3 method was used to calculate electronic energy of reactants, products, and TS; frequencies were
calculated using B3LYP/CBSB7 method.  Arrhenius expression was computed using CanTherm: an asymmetric Eckart
tunneling correction was employed and the frequencies were scaled by 0.99 (as suggested by Montgomery et al.
J.Chem.Phys. 110 (1999) 2822-2827).  The external symmetry number for H2O2 was 2; the external symmetry number
for the remaining species and TS were set to 1.  The rate coefficient was computed at 600-2000K (in 200 K increments).

For nButanol+HO2=H2O2+CH3*CHCH2CH2OH:
Moc et al. (AIP Conference Proceedings (2009) 1148 161-164 "The Unimolecular Decomposition
and H Abstraction Reactions by HO and HO2 from n-Butanol") report reaction barriers and
enthalpies(0 K); our CBS-QB3 calculations are shown in comparison (all units are kcal/mol).
                G3      CCSD(T)/cc-pVTZ     CBS-QB3
Barrier:        14.64       15.47           14.72
Enthalpy:       11.05       12.41           10.11
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 303,
    reactant1 = 
"""
H2O2
1  *1 O 0 {2,S} {3,S}
2     O 0 {1,S} {4,S}
3  *2 H 0 {1,S}
4     H 0 {2,S}
""",
    reactant2 = 
"""
butan-1-ol-2-yl
1     C 0 {2,S}
2     C 0 {1,S} {3,S}
3  *3 C 1 {2,S} {4,S}
4     C 0 {3,S} {5,S}
5     O 0 {4,S}
""",
    product1 = 
"""
HO2
1  *3 O 1 {2,S}
2     O 0 {1,S}
""",
    product2 = 
"""
n-butanol
1     C 0 {2,S}
2     C 0 {1,S} {3,S}
3  *1 C 0 {2,S} {4,S} {6,S}
4     C 0 {3,S} {5,S}
5     O 0 {4,S}
6  *2 H 0 {3,S}
""",
    kinetics = Arrhenius(
        A = (0.3145*2,"cm^3/(mol*s)"),
        n = 3.52,
        Ea = (1.61,"kcal/mol"),
        T0 = (1,"K"),
        Tmin = (600,"K"),
        Tmax = (2000,"K"),
    ),
    degeneracy = 2,
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/o HR corrections
H2O2 + CH3CH2*CHCH2OH = nButanol + HO2

CBS-QB3 method was used to calculate electronic energy of reactants, products, and TS; frequencies were
calculated using B3LYP/CBSB7 method.  Arrhenius expression was computed using CanTherm: an asymmetric Eckart
tunneling correction was employed and the frequencies were scaled by 0.99 (as suggested by Montgomery et al.
J.Chem.Phys. 110 (1999) 2822-2827).  The external symmetry number for H2O2 was 2; the external symmetry number
for the remaining species and TS were set to 1.  The rate coefficient was computed at 600-2000K (in 200 K increments).

For nButanol+HO2=H2O2+CH3CH2*CHCH2OH:
Moc et al. (AIP Conference Proceedings (2009) 1148 161-164 "The Unimolecular Decomposition
and H Abstraction Reactions by HO and HO2 from n-Butanol") report reaction barriers and
enthalpies(0 K); our CBS-QB3 calculations are shown in comparison (all units are kcal/mol).
                G3      CCSD(T)/cc-pVTZ     CBS-QB3
Barrier:        15.43       16.37           16.33
Enthalpy:       13.53       14.02           11.48
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 304,
    reactant1 = 
"""
H2O2
1  *1 O 0 {2,S} {3,S}
2     O 0 {1,S} {4,S}
3  *2 H 0 {1,S}
4     H 0 {2,S}
""",
    reactant2 = 
"""
butan-1-ol-2-yl
1     C 0 {2,S}
2     C 0 {1,S} {3,S}
3     C 0 {2,S} {4,S}
4  *3 C 1 {3,S} {5,S}
5     O 0 {4,S}
""",
    product1 = 
"""
HO2
1  *3 O 1 {2,S}
2     O 0 {1,S}
""",
    product2 = 
"""
n-butanol
1     C 0 {2,S}
2     C 0 {1,S} {3,S}
3     C 0 {2,S} {4,S}
4  *1 C 0 {3,S} {5,S} {6,S}
5     O 0 {4,S}
6  *2 H 0 {4,S}
""",
    kinetics = Arrhenius(
        A = (1.485*2,"cm^3/(mol*s)"),
        n = 3.39,
        Ea = (1.4,"kcal/mol"),
        T0 = (1,"K"),
        Tmin = (600,"K"),
        Tmax = (2000,"K"),
    ),
    degeneracy = 2,
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/o HR corrections
H2O2 + CH3CH2CH2*CHOH = nButanol + HO2

CBS-QB3 method was used to calculate electronic energy of reactants, products, and TS; frequencies were
calculated using B3LYP/CBSB7 method.  Arrhenius expression was computed using CanTherm: an asymmetric Eckart
tunneling correction was employed and the frequencies were scaled by 0.99 (as suggested by Montgomery et al.
J.Chem.Phys. 110 (1999) 2822-2827).  The external symmetry number for H2O2 was 2; the external symmetry number
for the remaining species and TS were set to 1.  The rate coefficient was computed at 600-2000K (in 200 K increments).

For nButanol+HO2=H2O2+CH3CH2CH2*CHOH:
Moc et al. (AIP Conference Proceedings (2009) 1148 161-164 "The Unimolecular Decomposition
and H Abstraction Reactions by HO and HO2 from n-Butanol") report reaction barriers and
enthalpies(0 K); our CBS-QB3 calculations are shown in comparison (all units are kcal/mol).
                G3      CCSD(T)/cc-pVTZ     CBS-QB3
Barrier:        12.62       13.23           11.74
Enthalpy:        8.35        8.63            7.17
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 305,
    reactant1 = 
"""
H2O2
1  *1 O 0 {2,S} {3,S}
2     O 0 {1,S} {4,S}
3  *2 H 0 {1,S}
4     H 0 {2,S}
""",
    reactant2 = 
"""
butan-2-ol-4-yl
1  *3 C 1 {2,S}
2     C 0 {1,S} {3,S}
3     C 0 {2,S} {4,S} {5,S}
4     C 0 {3,S}
5     O 0 {3,S}
""",
    product1 = 
"""
HO2
1  *3 O 1 {2,S}
2     O 0 {1,S}
""",
    product2 = 
"""
2-butanol
1  *1 C 0 {2,S} {6,S}
2     C 0 {1,S} {3,S}
3     C 0 {2,S} {4,S} {5,S}
4     C 0 {3,S}
5     O 0 {3,S}
6  *2 H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (5.75*2,"cm^3/(mol*s)"),
        n = 2.94,
        Ea = (0.46,"kcal/mol"),
        T0 = (1,"K"),
        Tmin = (600,"K"),
        Tmax = (2000,"K"),
    ),
    degeneracy = 2,
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/o HR corrections
H2O2 + *CH2CH2CH[OH]CH3 = 2-Butanol + HO2

CBS-QB3 method was used to calculate electronic energy of reactants, products, and TS; frequencies were
calculated using B3LYP/CBSB7 method.  Arrhenius expression was computed using CanTherm: an asymmetric Eckart
tunneling correction was employed and the frequencies were scaled by 0.99 (as suggested by Montgomery et al.
J.Chem.Phys. 110 (1999) 2822-2827).  The external symmetry number for H2O2 was 2; the external symmetry number
for the remaining species and TS were set to 1.  The rate coefficient was computed at 600-2000K (in 200 K increments).
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 306,
    reactant1 = 
"""
H2O2
1  *1 O 0 {2,S} {3,S}
2     O 0 {1,S} {4,S}
3  *2 H 0 {1,S}
4     H 0 {2,S}
""",
    reactant2 = 
"""
butan-2-ol-3-yl
1     C 0 {2,S}
2  *3 C 1 {1,S} {3,S}
3     C 0 {2,S} {4,S} {5,S}
4     C 0 {3,S}
5     O 0 {3,S}
""",
    product1 = 
"""
HO2
1  *3 O 1 {2,S}
2     O 0 {1,S}
""",
    product2 = 
"""
2-butanol
1     C 0 {2,S}
2  *1 C 0 {1,S} {3,S} {6,S}
3     C 0 {2,S} {4,S} {5,S}
4     C 0 {3,S}
5     O 0 {3,S}
6  *2 H 0 {2,S}
""",
    kinetics = Arrhenius(
        A = (0.875*2,"cm^3/(mol*s)"),
        n = 2.91,
        Ea = (-0.41,"kcal/mol"),
        T0 = (1,"K"),
        Tmin = (600,"K"),
        Tmax = (2000,"K"),
    ),
    degeneracy = 2,
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/o HR corrections
H2O2 + CH3*CHCH[OH]CH3 = 2-Butanol + HO2

CBS-QB3 method was used to calculate electronic energy of reactants, products, and TS; frequencies were
calculated using B3LYP/CBSB7 method.  Arrhenius expression was computed using CanTherm: an asymmetric Eckart
tunneling correction was employed and the frequencies were scaled by 0.99 (as suggested by Montgomery et al.
J.Chem.Phys. 110 (1999) 2822-2827).  The external symmetry number for H2O2 was 2; the external symmetry number
for the remaining species and TS were set to 1.  The rate coefficient was computed at 600-2000K (in 200 K increments).
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 307,
    reactant1 = 
"""
H2O2
1  *1 O 0 {2,S} {3,S}
2     O 0 {1,S} {4,S}
3  *2 H 0 {1,S}
4     H 0 {2,S}
""",
    reactant2 = 
"""
butan-2-ol-2-yl
1     C 0 {2,S}
2     C 0 {1,S} {3,S}
3  *3 C 1 {2,S} {4,S} {5,S}
4     C 0 {3,S}
5     O 0 {3,S}
""",
    product1 = 
"""
HO2
1  *3 O 1 {2,S}
2     O 0 {1,S}
""",
    product2 = 
"""
2-butanol
1     C 0 {2,S}
2     C 0 {1,S} {3,S}
3  *1 C 0 {2,S} {4,S} {5,S} {6,S}
4     C 0 {3,S}
5     O 0 {3,S}
6  *2 H 0 {3,S}
""",
    kinetics = Arrhenius(
        A = (17.3*2,"cm^3/(mol*s)"),
        n = 3.05,
        Ea = (1.02,"kcal/mol"),
        T0 = (1,"K"),
        Tmin = (600,"K"),
        Tmax = (2000,"K"),
    ),
    degeneracy = 2,
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/o HR corrections
H2O2 + CH3CH2*C[OH]CH3 = 2-Butanol + HO2

CBS-QB3 method was used to calculate electronic energy of reactants, products, and TS; frequencies were
calculated using B3LYP/CBSB7 method.  Arrhenius expression was computed using CanTherm: an asymmetric Eckart
tunneling correction was employed and the frequencies were scaled by 0.99 (as suggested by Montgomery et al.
J.Chem.Phys. 110 (1999) 2822-2827).  The external symmetry number for H2O2 was 2; the external symmetry number
for the remaining species and TS were set to 1.  The rate coefficient was computed at 600-2000K (in 200 K increments).
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 308,
    reactant1 = 
"""
H2O2
1  *1 O 0 {2,S} {3,S}
2     O 0 {1,S} {4,S}
3  *2 H 0 {1,S}
4     H 0 {2,S}
""",
    reactant2 = 
"""
butan-2-ol-1-yl
1     C 0 {2,S}
2     C 0 {1,S} {3,S}
3     C 0 {2,S} {4,S} {5,S}
4  *3 C 1 {3,S}
5     O 0 {3,S}
""",
    product1 = 
"""
HO2
1  *3 O 1 {2,S}
2     O 0 {1,S}
""",
    product2 = 
"""
2-butanol
1     C 0 {2,S}
2     C 0 {1,S} {3,S}
3     C 0 {2,S} {4,S} {5,S}
4  *1 C 0 {3,S} {6,S}
5     O 0 {3,S}
6  *2 H 0 {4,S}
""",
    kinetics = Arrhenius(
        A = (0.3055*2,"cm^3/(mol*s)"),
        n = 3.53,
        Ea = (1.52,"kcal/mol"),
        T0 = (1,"K"),
        Tmin = (600,"K"),
        Tmax = (2000,"K"),
    ),
    degeneracy = 2,
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/o HR corrections
H2O2 + CH3CH2CH[OH]*CH2 = 2-Butanol + HO2

CBS-QB3 method was used to calculate electronic energy of reactants, products, and TS; frequencies were
calculated using B3LYP/CBSB7 method.  Arrhenius expression was computed using CanTherm: an asymmetric Eckart
tunneling correction was employed and the frequencies were scaled by 0.99 (as suggested by Montgomery et al.
J.Chem.Phys. 110 (1999) 2822-2827).  The external symmetry number for H2O2 was 2; the external symmetry number
for the remaining species and TS were set to 1.  The rate coefficient was computed at 600-2000K (in 200 K increments).
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 309,
    reactant1 = 
"""
H2O2
1  *1 O 0 {2,S} {3,S}
2     O 0 {1,S} {4,S}
3  *2 H 0 {1,S}
4     H 0 {2,S}
""",
    reactant2 = 
"""
t-butanol-yl
1     C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 C 1 {1,S}
3     C 0 {1,S}
4     C 0 {1,S}
5     O 0 {1,S}
""",
    product1 = 
"""
HO2
1  *3 O 1 {2,S}
2     O 0 {1,S}
""",
    product2 = 
"""
t-butanol
1     C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 {1,S} {6,S}
3     C 0 {1,S}
4     C 0 {1,S}
5     O 0 {1,S}
6  *2 H 0 {2,S}
""",
    kinetics = Arrhenius(
        A = (0.21*2,"cm^3/(mol*s)"),
        n = 3.53,
        Ea = (1.56,"kcal/mol"),
        T0 = (1,"K"),
        Tmin = (600,"K"),
        Tmax = (2000,"K"),
    ),
    degeneracy = 2,
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/o HR corrections
H2O2 + HOC[*CH2][CH3][CH3] = tert-Butanol + HO2

CBS-QB3 method was used to calculate electronic energy of reactants, products, and TS; frequencies were
calculated using B3LYP/CBSB7 method.  Arrhenius expression was computed using CanTherm: an asymmetric Eckart
tunneling correction was employed and the frequencies were scaled by 0.99 (as suggested by Montgomery et al.
J.Chem.Phys. 110 (1999) 2822-2827).  The external symmetry number for H2O2 was 2; the external symmetry number
for the remaining species and TS were set to 1.  The rate coefficient was computed at 600-2000K (in 200 K increments).
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 500,
    reactant1 = 
"""
formaldehyde
1  *1 C 0 {2,D} {3,S} {4,S}
2     O 0 {1,D}
3  *2 H 0 {1,S}
4     H 0 {1,S}
""",
    reactant2 = 
"""
isobuten-1-yl
1     C 0 {2,D}
2     C 0 {1,D} {3,S} {4,S}
3  *3 C 1 {2,S}
4     C 0 {2,S}
""",
    product1 = 
"""
formyl
1  *3 C 1 {2,D}
2     O 0 {1,D}
""",
    product2 = 
"""
isobutene
1     C 0 {2,D}
2     C 0 {1,D} {3,S} {4,S}
3  *1 C 1 {2,S} {5,S}
4     C 0 {2,S}
5  *2 H 0 {3,S}
""",
    kinetics = Arrhenius(
        A = (0.0613,"cm^3/(mol*s)"),
        n = 3.95,
        Ea = (12.22,"kcal/mol"),
        T0 = (1,"K"),
        Tmin = (600,"K"),
        Tmax = (2000,"K"),
    ),
    degeneracy = 2,
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/o HR corrections
CH2O + H2C=C[*CH2][CH3] = HCO + H2C=C[CH3]2

Geometries and energies of reactants, products, and TS were computed using the CBS-QB3 methodology; frequencies
were calculated at B3LYP/CBSB7.  Arrhenius expression was computed using CanTherm; an asymmetric Eckart tunneling
correction was employed and the frequencies were scaled by 0.99 (as suggested by Montgomergy et al.; J. Chem. Phys.
110 (1999) 2822-2827).  The Arrhenius fit was based on k(T) at T=600, 800, 1000, 1200, 1400, 1600, 1800, and 2000K.
The external symmetry number for CH2O and iso-butene was 2; the external symmetry for all others was 1.  The
electronic spin multiplicity was 1 for CH2O and iso-butene; the electronic spin multiplicity for all others was 2.

There are no rate coefficients for this reaction in the literature (based on MRH's limited search).
   Tsang {J. Phys. Chem. Ref. Data 20 (1991) 221-273} recommends the following for the reaction of 
   CH2O + H2C=CH-*CH2 = HCO + H2C=CH-CH3: k(T) = 1.26e+08 * T^1.9 * exp(-18.184 kcal/mol / RT) cm3 mol-1 s-1.
   This rate coefficient is 25-85x faster than MRH's calculation over the range 600-2000K.
   
   The previous estimate by RMG for this reaction was: k(T) = 5.500e+03 * T^2.81 * exp(-5.86 kcal/mol / RT) cm3 mol-1 s-1.
   This rate coefficient is 80-13,000x faster than MRH's calculation over the range 600-2000K.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 501,
    reactant1 = 
"""
1     C 0 {2,S}
2  *1 C 0 {1,S} {3,S} {4,S}
3     C 0 {2,S}
4  *2 H 0 {2,S}
""",
    reactant2 = 
"""
1     C 0 {2,S}
2  *3 C 1 {1,S} {3,S} {5,S}
3     C 0 {2,S} {4,S}
4     O 0 {3,S}
5     C 0 {2,S}
""",
    product1 = 
"""
1     C 0 {2,S}
2  *3 C 1 {1,S} {3,S}
3     C 0 {2,S}
""",
    product2 = 
"""
1     C 0 {2,S}
2  *1 C 0 {1,S} {3,S} {5,S} {6,S}
3     C 0 {2,S} {4,S}
4     O 0 {3,S}
5     C 0 {2,S}
6  *2 H 0 {2,S}
""",
    kinetics = Arrhenius(
        A = (9.11e-07*2,"cm^3/(mol*s)"),
        n = 5.11,
        Ea = (5.69,"kcal/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    degeneracy = 2,
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.

InChI=1/C3H8/c1-3-2/h3H2,1-2H3 (external symmetry number = 2, spin multiplicity = 1)
 +
InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C3H7/c1-3-2/h3H,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 502,
    reactant1 = 
"""
1     C 0 {2,S}
2     C 0 {1,S} {3,S} {5,S}
3  *1 C 0 {2,S} {4,S} {6,S}
4     O 0 {3,S}
5     C 0 {2,S}
6  *2 H 0 {3,S}
""",
    reactant2 = 
"""
1     C 0 {2,S}
2  *3 C 1 {1,S} {3,S}
3     C 0 {2,S}
""",
    product1 = 
"""
1     C 0 {2,S}
2     C 0 {1,S} {3,S} {5,S}
3  *3 C 1 {2,S} {4,S}
4     O 0 {3,S}
5     C 0 {2,S}
""",
    product2 = 
"""
1     C 0 {2,S}
2  *1 C 0 {1,S} {3,S} {4,S}
3     C 0 {2,S}
4  *2 H 0 {2,S}
""",
    kinetics = Arrhenius(
        A = (1.06e-06*2,"cm^3/(mol*s)"),
        n = 5.06,
        Ea = (4.89,"kcal/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    degeneracy = 2,
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.

InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)
 +
InChI=1/C3H7/c1-3-2/h3H,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C3H8/c1-3-2/h3H2,1-2H3 (external symmetry number = 2, spin multiplicity = 1)
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 503,
    reactant1 = 
"""
1     C 0 {2,D}
2     C 0 {1,D} {3,S} {4,S}
3  *1 C 0 {2,S} {5,S}
4     C 0 {2,S}
5  *2 H 0 {3,S}
""",
    reactant2 = 
"""
1  *3 C 1 {2,S}
2     C 0 {1,S} {3,S} {5,S}
3     C 0 {2,S} {4,S}
4     O 0 {3,S}
5     C 0 {2,S}
""",
    product1 = 
"""
1     C 0 {2,D}
2     C 0 {1,D} {3,S} {4,S}
3  *3 C 1 {2,S}
4     C 0 {2,S}
""",
    product2 = 
"""
1  *1 C 0 {2,S} {6,S}
2     C 0 {1,S} {3,S} {5,S}
3     C 0 {2,S} {4,S}
4     O 0 {3,S}
5     C 0 {2,S}
6  *2 H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (8.39e-06*6,"cm^3/(mol*s)"),
        n = 4.89,
        Ea = (4.32,"kcal/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    degeneracy = 6,
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.

InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3 (external symmetry number = 2, spin multiplicity = 1)
 +
InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 504,
    reactant1 = 
"""
1     C 0 {2,D}
2     C 0 {1,D} {3,S} {4,S}
3  *1 C 0 {2,S} {5,S}
4     C 0 {2,S}
5  *2 H 0 {3,S}
""",
    reactant2 = 
"""
1     C 0 {2,S}
2  *3 C 1 {1,S} {3,S} {5,S}
3     C 0 {2,S} {4,S}
4     O 0 {3,S}
5     C 0 {2,S}
""",
    product1 = 
"""
1     C 0 {2,D}
2     C 0 {1,D} {3,S} {4,S}
3  *3 C 0 {2,S}
4     C 0 {2,S}
""",
    product2 = 
"""
1     C 0 {2,S}
2  *1 C 0 {1,S} {3,S} {5,S} {6,S}
3     C 0 {2,S} {4,S}
4     O 0 {3,S}
5     C 0 {2,S}
6  *2 H 0 {2,S}
""",
    kinetics = Arrhenius(
        A = (1.44e-05*6,"cm^3/(mol*s)"),
        n = 4.52,
        Ea = (1.46,"kcal/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    degeneracy = 6,
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.

InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3 (external symmetry number = 2, spin multiplicity = 1)
 +
InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 505,
    reactant1 = 
"""
1     C 0 {2,D}
2     C 0 {1,D} {3,S} {4,S}
3  *1 C 0 {2,S} {5,S}
4     C 0 {2,S}
5  *2 H 0 {3,S}
""",
    reactant2 = 
"""
1     C 0 {2,S}
2     C 0 {1,S} {3,S} {5,S}
3  *3 C 1 {2,S} {4,S}
4     O 0 {3,S}
5     C 0 {2,S}
""",
    product1 = 
"""
1     C 0 {2,D}
2     C 0 {1,D} {3,S} {4,S}
3  *3 C 1 {2,S}
4     C 0 {2,S}
""",
    product2 = 
"""
1     C 0 {2,S}
2     C 0 {1,S} {3,S} {5,S}
3  *1 C 0 {2,S} {4,S} {6,S}
4     O 0 {3,S}
5     C 0 {2,S}
6  *2 H 0 {3,S}
""",
    kinetics = Arrhenius(
        A = (4.91e-06*6,"cm^3/(mol*s)"),
        n = 5.07,
        Ea = (3.66,"kcal/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    degeneracy = 6,
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.

InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3 (external symmetry number = 2, spin multiplicity = 1)
 +
InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 506,
    reactant1 = 
"""
1     C 0 {2,D}
2     C 0 {1,D} {3,S} {4,S}
3  *1 C 0 {2,S} {5,S}
4     C 0 {2,S}
5  *2 H 0 {3,S}
""",
    reactant2 = 
"""
1     C 0 {2,S}
2     C 0 {1,S} {3,S} {5,S}
3     C 0 {2,S} {4,S}
4  *3 O 1 {3,S}
5     C 0 {2,S}
""",
    product1 = 
"""
1     C 0 {2,D}
2     C 0 {1,D} {3,S} {4,S}
3  *3 C 1 {2,S}
4     C 0 {2,S}
""",
    product2 = 
"""
1     C 0 {2,S}
2     C 0 {1,S} {3,S} {5,S}
3     C 0 {2,S} {4,S}
4  *1 O 0 {3,S} {6,S}
5     C 0 {2,S}
6  *2 H 0 {4,S}
""",
    kinetics = Arrhenius(
        A = (0.583*6,"cm^3/(mol*s)"),
        n = 3.74,
        Ea = (1.45,"kcal/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    degeneracy = 6,
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.

InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3 (external symmetry number = 2, spin multiplicity = 1)
 +
InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 507,
    reactant1 = 
"""
1  *1 C 0 {2,S} {4,S}
2     C 0 {1,S} {3,D}
3     C 0 {2,D}
4  *2 H 0 {1,S}
""",
    reactant2 = 
"""
1  *3 C 1 {2,S}
2     C 0 {1,S} {3,S} {5,S}
3     C 0 {2,S} {4,S}
4     O 0 {3,S}
5     C 0 {2,S}
""",
    product1 = 
"""
1  *3 C 1 {2,S}
2     C 0 {1,S} {3,D}
3     C 0 {2,D}
""",
    product2 = 
"""
1  *1 C 0 {2,S} {6,S}
2     C 0 {1,S} {3,S} {5,S}
3     C 0 {2,S} {4,S}
4     O 0 {3,S}
5     C 0 {2,S}
6  *2 H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (3.36e-05*3,"cm^3/(mol*s)"),
        n = 4.75,
        Ea = (4.13,"kcal/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    degeneracy = 3,
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.

InChI=1/C3H6/c1-3-2/h3H,1H2,2H3 (external symmetry number = 1, spin multiplicity = 1)
 +
InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C3H5/c1-3-2/h3H,1-2H2 (external symmetry number = 2, spin multiplicity = 2)
 +
InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)

Tsang [Tsang1991]_ recommends k(T) = 2.23e+00 * (T/K)^3.5 * exp(-6.64 kcal/mol /RT) cm3 mol-1 s-1
for the reaction C3H6 + iso-C4H9 = iso-C4H10 + C3H5.  The new rate coefficient expression is
in good agreement with this expression (within 10% over most of the valid temperature range).
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 508,
    reactant1 = 
"""
1  *1 C 0 {2,S} {4,S}
2     C 0 {1,S} {3,D}
3     C 0 {2,D}
4  *2 H 0 {1,S}
""",
    reactant2 = 
"""
1     C 0 {2,S}
2  *3 C 1 {1,S} {3,S} {5,S}
3     C 0 {2,S} {4,S}
4     O 0 {3,S}
5     C 0 {2,S}
""",
    product1 = 
"""
1  *3 C 1 {2,S}
2     C 0 {1,S} {3,D}
3     C 0 {2,D}
""",
    product2 = 
"""
1     C 0 {2,S}
2  *1 C 0 {1,S} {3,S} {5,S} {6,S}
3     C 0 {2,S} {4,S}
4     O 0 {3,S}
5     C 0 {2,S}
6  *2 H 0 {2,S}
""",
    kinetics = Arrhenius(
        A = (1.64e-06*3,"cm^3/(mol*s)"),
        n = 4.98,
        Ea = (3.18,"kcal/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    degeneracy = 3,
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.

InChI=1/C3H6/c1-3-2/h3H,1H2,2H3 (external symmetry number = 1, spin multiplicity = 1)
 +
InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C3H5/c1-3-2/h3H,1-2H2 (external symmetry number = 2, spin multiplicity = 2)
 +
InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)

Tsang [Tsang1991]_ recommends k(T) = 3.01e-05 * (T/K)^4.9 * exp(-7.95 kcal/mol /RT) cm3 mol-1 s-1
for the reaction C3H6 + tert-C4H9 = iso-C4H10 + C3H5.  The new rate coefficient expression is faster
by as much as 10x over of the valid temperature range.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 509,
    reactant1 = 
"""
1  *1 C 0 {2,S} {4,S}
2     C 0 {1,S} {3,D}
3     C 0 {2,D}
4  *2 H 0 {1,S}
""",
    reactant2 = 
"""
1     C 0 {2,S}
2     C 0 {1,S} {3,S} {5,S}
3  *3 C 1 {2,S} {4,S}
4     O 0 {3,S}
5     C 0 {2,S}
""",
    product1 = 
"""
1  *3 C 1 {2,S}
2     C 0 {1,S} {3,D}
3     C 0 {2,D}
""",
    product2 = 
"""
1     C 0 {2,S}
2     C 0 {1,S} {3,S} {5,S}
3  *1 C 0 {2,S} {4,S} {6,S}
4     O 0 {3,S}
5     C 0 {2,S}
6  *2 H 0 {3,S}
""",
    kinetics = Arrhenius(
        A = (3.11e-06*3,"cm^3/(mol*s)"),
        n = 4.97,
        Ea = (3.64,"kcal/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    degeneracy = 3,
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.

InChI=1/C3H6/c1-3-2/h3H,1H2,2H3 (external symmetry number = 1, spin multiplicity = 1)
 +
InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C3H5/c1-3-2/h3H,1-2H2 (external symmetry number = 2, spin multiplicity = 2)
 +
InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 510,
    reactant1 = 
"""
1  *1 C 0 {2,S} {4,S}
2     C 0 {1,S} {3,D}
3     C 0 {2,D}
4  *2 H 0 {1,S}
""",
    reactant2 = 
"""
1     C 0 {2,S}
2     C 0 {1,S} {3,S} {5,S}
3     C 0 {2,S} {4,S}
4  *3 O 1 {3,S}
5     C 0 {2,S}
""",
    product1 = 
"""
1  *3 C 1 {2,S}
2     C 0 {1,S} {3,D}
3     C 0 {2,D}
""",
    product2 = 
"""
1     C 0 {2,S}
2     C 0 {1,S} {3,S} {5,S}
3     C 0 {2,S} {4,S}
4  *1 O 0 {3,S} {6,S}
5     C 0 {2,S}
6  *2 H 0 {4,S}
""",
    kinetics = Arrhenius(
        A = (0.119*3,"cm^3/(mol*s)"),
        n = 3.9,
        Ea = (1.81,"kcal/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    degeneracy = 3,
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.

InChI=1/C3H6/c1-3-2/h3H,1H2,2H3 (external symmetry number = 1, spin multiplicity = 1)
 +
InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C3H5/c1-3-2/h3H,1-2H2 (external symmetry number = 2, spin multiplicity = 2)
 +
InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 511,
    reactant1 = 
"""
1  *1 C 0 {2,S} {3,S}
2     C 0 {1,S}
3  *2 H 0 {1,S}
""",
    reactant2 = 
"""
1  *3 C 1 {2,S}
2     C 0 {1,S} {3,S} {5,S}
3     C 0 {2,S} {4,S}
4     O 0 {3,S}
5     C 0 {2,S}
""",
    product1 = 
"""
1  *3 C 1 {2,S}
2     C 0 {1,S}
""",
    product2 = 
"""
1  *1 C 0 {2,S} {6,S}
2     C 0 {1,S} {3,S} {5,S}
3     C 0 {2,S} {4,S}
4     O 0 {3,S}
5     C 0 {2,S}
6  *2 H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (3.21e-06*6,"cm^3/(mol*s)"),
        n = 5.28,
        Ea = (7.78,"kcal/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    degeneracy = 6,
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.

InChI=1/C2H6/c1-2/h1-2H3 (external symmetry number = 6, spin multiplicity = 1)
 +
InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C2H5/c1-2/h1H2,2H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)

Tsang [Tsang1990]_ recommends k(T) = 2.894e-01 * (T/K)^3.7 * exp(-9.78 kcal/mol /RT) cm3 mol-1 s-1
for the reaction C2H6 + iso-C4H9 = iso-C4H10 + C2H5.  The new rate coefficient expression is faster
by 10-100x over of the valid temperature range.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 512,
    reactant1 = 
"""
1     C 0 {2,S}
2  *1 C 0 {1,S} {3,S} {5,S} {6,S}
3     C 0 {2,S} {4,S}
4     O 0 {3,S}
5     C 0 {2,S}
6  *2 H 0 {2,S}
""",
    reactant2 = 
"""
1  *3 C 1 {2,S}
2     C 0 {1,S}
""",
    product1 = 
"""
1     C 0 {2,S}
2  *3 C 1 {1,S} {3,S} {5,S}
3     C 0 {2,S} {4,S}
4     O 0 {3,S}
5     C 0 {2,S}
""",
    product2 = 
"""
1  *1 C 0 {2,S} {3,S}
2     C 0 {1,S}
3  *2 H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (1.41e-05,"cm^3/(mol*s)"),
        n = 4.83,
        Ea = (4.37,"kcal/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    degeneracy = 1,
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.

InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)
 +
InChI=1/C2H5/c1-2/h1H2,2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C2H6/c1-2/h1-2H3 (external symmetry number = 6, spin multiplicity = 1)

Tsang [Tsang1990]_ recommends k(T) = 5.41e-01 * (T/K)^3.46 * exp(-5.96 kcal/mol /RT) cm3 mol-1 s-1
for the reaction iso-C4H10 + C2H5 = C2H6 + tert-C4H9.  The new rate coefficient expression is
in good agreement with this expression (within a factor of 1.6 over the valid temperature range).
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 513,
    reactant1 = 
"""
1     C 0 {2,S}
2     C 0 {1,S} {3,S} {5,S}
3  *1 C 0 {2,S} {4,S} {6,S}
4     O 0 {3,S}
5     C 0 {2,S}
6  *2 H 0 {3,S}
""",
    reactant2 = 
"""
1  *3 C 1 {2,S}
2     C 0 {1,S}
""",
    product1 = 
"""
1     C 0 {2,S}
2     C 0 {1,S} {3,S} {5,S}
3  *3 C 1 {2,S} {4,S}
4     O 0 {3,S}
5     C 0 {2,S}
""",
    product2 = 
"""
1  *1 C 0 {2,S} {3,S}
2     C 0 {1,S}
3  *2 H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (4.25e-06*2,"cm^3/(mol*s)"),
        n = 5.01,
        Ea = (5.01,"kcal/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    degeneracy = 2,
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.

InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)
 +
InChI=1/C2H5/c1-2/h1H2,2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C2H6/c1-2/h1-2H3 (external symmetry number = 6, spin multiplicity = 1)
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 514,
    reactant1 = 
"""
1  *1 C 0 {2,S} {3,S}
2     C 0 {1,S}
3  *2 H 0 {1,S}
""",
    reactant2 = 
"""
1     C 0 {2,S}
2     C 0 {1,S} {3,S} {5,S}
3     C 0 {2,S} {4,S}
4  *3 O 1 {3,S}
5     C 0 {2,S}
""",
    product1 = 
"""
1  *3 C 1 {2,S}
2     C 0 {1,S}
""",
    product2 = 
"""
1     C 0 {2,S}
2     C 0 {1,S} {3,S} {5,S}
3     C 0 {2,S} {4,S}
4  *1 O 0 {3,S} {6,S}
5     C 0 {2,S}
6  *2 H 0 {4,S}
""",
    kinetics = Arrhenius(
        A = (0.00507*6,"cm^3/(mol*s)"),
        n = 4.52,
        Ea = (2.34,"kcal/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    degeneracy = 6,
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.

InChI=1/C2H6/c1-2/h1-2H3 (external symmetry number = 6, spin multiplicity = 1)
 +
InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C2H5/c1-2/h1H2,2H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 515,
    reactant1 = 
"""
1     C 0 {2,S}
2  *1 C 0 {1,S} {3,S} {5,S} {6,S}
3     C 0 {2,S} {4,S}
4     O 0 {3,S}
5     C 0 {2,S}
6  *2 H 0 {2,S}
""",
    reactant2 = 
"""
1  *3 C 1 {2,D}
2     C 0 {1,D}
""",
    product1 = 
"""
1     C 0 {2,S}
2  *3 C 1 {1,S} {3,S} {5,S}
3     C 0 {2,S} {4,S}
4     O 0 {3,S}
5     C 0 {2,S}
""",
    product2 = 
"""
1  *1 C 0 {2,D} {3,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (5.49,"cm^3/(mol*s)"),
        n = 3.33,
        Ea = (0.63,"kcal/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    degeneracy = 1,
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.

InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)
 +
InChI=1/C2H3/c1-2/h1H,2H2 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C2H4/c1-2/h1-2H2 (external symmetry number = 4, spin multiplicity = 1)

Tsang [Tsang1990]_ recommends k(T) = 9.04e-01 * (T/K)^3.46 * exp(-2.60 kcal/mol /RT) cm3 mol-1 s-1
for the reaction iso-C4H10 + C2H3 = C2H4 + tert-C4H9.  The new rate coefficient is faster by 4-10x
over the valid temperature range.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 516,
    reactant1 = 
"""
1  *1 C 0 {2,S} {6,S}
2     C 0 {1,S} {3,S} {5,S}
3     C 0 {2,S} {4,S}
4     O 0 {3,S}
5     C 0 {2,S}
6  *2 H 0 {1,S}
""",
    reactant2 = 
"""
1     C 0 {2,D}
2  *3 C 1 {1,D} {3,S}
3     C 0 {2,S}
""",
    product1 = 
"""
1  *3 C 1 {2,S}
2     C 0 {1,S} {3,S} {5,S}
3     C 0 {2,S} {4,S}
4     O 0 {3,S}
5     C 0 {2,S}
""",
    product2 = 
"""
1     C 0 {2,D}
2  *1 C 0 {1,D} {3,S} {4,S}
3     C 0 {2,S}
4  *2 H 0 {2,S}
""",
    kinetics = Arrhenius(
        A = (3.11e-05*6,"cm^3/(mol*s)"),
        n = 4.87,
        Ea = (3.5,"kcal/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    degeneracy = 6,
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.

InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)
 +
InChI=1/C3H5/c1-3-2/h1H2,2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C3H6/c1-3-2/h3H,1H2,2H3 (external symmetry number = 1, spin multiplicity = 1)
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 517,
    reactant1 = 
"""
1     C 0 {2,S}
2     C 0 {1,S} {3,S} {5,S}
3  *1 C 0 {2,S} {4,S} {6,S}
4     O 0 {3,S}
5     C 0 {2,S}
6  *2 H 0 {3,S}
""",
    reactant2 = 
"""
1     C 0 {2,D}
2  *3 C 1 {1,D} {3,S}
3     C 0 {2,S}
""",
    product1 = 
"""
1     C 0 {2,S}
2     C 0 {1,S} {3,S} {5,S}
3  *3 C 1 {2,S} {4,S}
4     O 0 {3,S}
5     C 0 {2,S}
""",
    product2 = 
"""
1     C 0 {2,D}
2  *1 C 0 {1,D} {3,S} {4,S}
3     C 0 {2,S}
4  *2 H 0 {2,S}
""",
    kinetics = Arrhenius(
        A = (0.0128*2,"cm^3/(mol*s)"),
        n = 4.09,
        Ea = (1.31,"kcal/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    degeneracy = 2,
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.

InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)
 +
InChI=1/C3H5/c1-3-2/h1H2,2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C3H6/c1-3-2/h3H,1H2,2H3 (external symmetry number = 1, spin multiplicity = 1)
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 518,
    reactant1 = 
"""
1     C 0 {2,S}
2  *1 C 0 {1,S} {3,S} {5,S}
3     C 0 {2,S} {4,D}
4     O 0 {3,D}
5  *2 H 0 {2,S}
""",
    reactant2 = 
"""
1  *3 C 1 {2,S}
2     C 0 {1,S} {3,S} {5,S}
3     C 0 {2,S} {4,S}
4     O 0 {3,S}
5     C 0 {2,S}
""",
    product1 = 
"""
1     C 0 {2,S}
2  *3 C 1 {1,S} {3,S}
3     C 0 {2,S} {4,D}
4     O 0 {3,D}
""",
    product2 = 
"""
1  *1 C 0 {2,S} {6,S}
2     C 0 {1,S} {3,S} {5,S}
3     C 0 {2,S} {4,S}
4     O 0 {3,S}
5     C 0 {2,S}
6  *2 H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.000156*2,"cm^3/(mol*s)"),
        n = 4.31,
        Ea = (3.39,"kcal/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    degeneracy = 2,
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.

InChI=1/C3H6O/c1-2-3-4/h3H,2H2,1H3 (external symmetry number = 1, spin multiplicity = 1)
 +
InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 519,
    reactant1 = 
"""
1     C 0 {2,S}
2  *1 C 0 {1,S} {3,S} {5,S} {6,S}
3     C 0 {2,S} {4,S}
4     O 0 {3,S}
5     C 0 {2,S}
6  *2 H 0 {2,S}
""",
    reactant2 = 
"""
1     C 0 {2,S}
2  *3 C 1 {1,S} {3,S}
3     C 0 {2,S} {4,D}
4     O 0 {3,D}
""",
    product1 = 
"""
1     C 0 {2,S}
2  *3 C 1 {1,S} {3,S} {5,S}
3     C 0 {2,S} {4,S}
4     O 0 {3,S}
5     C 0 {2,S}
""",
    product2 = 
"""
1     C 0 {2,S}
2  *1 C 0 {1,S} {3,S} {5,S}
3     C 0 {2,S} {4,D}
4     O 0 {3,D}
5  *2 H 0 {2,S}
""",
    kinetics = Arrhenius(
        A = (0.000485,"cm^3/(mol*s)"),
        n = 4.37,
        Ea = (9.66,"kcal/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    degeneracy = 1,
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.

InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)
 +
InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C3H6O/c1-2-3-4/h3H,2H2,1H3 (external symmetry number = 1, spin multiplicity = 1)
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 520,
    reactant1 = 
"""
1     C 0 {2,S}
2     C 0 {1,S} {3,S} {5,S}
3  *1 C 0 {2,S} {4,S} {6,S}
4     O 0 {3,S}
5     C 0 {2,S}
6  *2 H 0 {3,S}
""",
    reactant2 = 
"""
1     C 0 {2,S}
2  *3 C 1 {1,S} {3,S}
3     C 0 {2,S} {4,D}
4     O 0 {3,D}
""",
    product1 = 
"""
1     C 0 {2,S}
2     C 0 {1,S} {3,S} {5,S}
3  *3 C 1 {2,S} {4,S}
4     O 0 {3,S}
5     C 0 {2,S}
""",
    product2 = 
"""
1     C 0 {2,S}
2  *1 C 0 {1,S} {3,S} {5,S}
3     C 0 {2,S} {4,D}
4     O 0 {3,D}
5  *2 H 0 {2,S}
""",
    kinetics = Arrhenius(
        A = (0.00184*2,"cm^3/(mol*s)"),
        n = 4.02,
        Ea = (7.92,"kcal/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    degeneracy = 2,
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.

InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)
 +
InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C3H6O/c1-2-3-4/h3H,2H2,1H3 (external symmetry number = 1, spin multiplicity = 1)
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 521,
    reactant1 = 
"""
1     C 0 {2,S}
2  *1 C 0 {1,S} {3,S} {5,S} {6,S}
3     C 0 {2,S} {4,D}
4     O 0 {3,D}
5     C 0 {2,S}
6  *2 H 0 {2,S}
""",
    reactant2 = 
"""
1  *3 H 1
""",
    product1 = 
"""
1     C 0 {2,S}
2  *3 C 1 {1,S} {3,S} {5,S}
3     C 0 {2,S} {4,D}
4     O 0 {3,D}
5     C 0 {2,S}
""",
    product2 = 
"""
1  *1 H 0 {2,S}
2  *2 H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (2.08e+07,"cm^3/(mol*s)"),
        n = 1.84,
        Ea = (3.03,"kcal/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    degeneracy = 1,
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.

InChI=1/C4H8O/c1-4(2)3-5/h3-4H,1-2H3 (external symmetry number = 1, spin multiplicity = 1)
 +
InChI=1/H (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H7O/c1-4(2)3-5/h3H,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/H2/h1H (external symmetry number = 2, spin multiplicity = 1)
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 522,
    reactant1 = 
"""
1     C 0 {2,D}
2     C 0 {1,D} {3,S} {4,S}
3  *1 C 0 {2,S} {5,S}
4     C 0 {2,S}
5  *2 H 0 {3,S}
""",
    reactant2 = 
"""
1     C 0 {2,S}
2     C 0 {1,S} {3,D}
3     C 0 {2,D} {4,S}
4  *3 O 1 {3,S}
""",
    product1 = 
"""
1     C 0 {2,D}
2     C 0 {1,D} {3,S} {4,S}
3  *3 C 1 {2,S}
4     C 0 {2,S}
""",
    product2 = 
"""
1     C 0 {2,S}
2     C 0 {1,S} {3,D}
3     C 0 {2,D} {4,S}
4  *1 O 0 {3,S} {5,S}
5  *2 H 0 {4,S}
""",
    kinetics = Arrhenius(
        A = (7.52e-08*6,"cm^3/(mol*s)"),
        n = 5.77,
        Ea = (12.04,"kcal/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    degeneracy = 6,
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.

InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3 (external symmetry number = 2, spin multiplicity = 1)
 +
InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C3H6O/c1-2-3-4/h2-4H,1H3/ (external symmetry number = 1, spin multiplicity = 1)
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1002,
    reactant1 = 
"""
1     C 0 {2,S}
2  *1 C 0 {1,S} {3,S} {5,S} {6,S}
3     C 0 {2,S} {4,S}
4     O 0 {3,S}
5     C 0 {2,S}
6  *2 H 0 {2,S}
""",
    reactant2 = 
"""
1     C 0 {2,S}
2  *3 C 1 {1,S} {3,S}
3     C 0 {2,S}
""",
    product1 = 
"""
1     C 0 {2,S}
2  *3 C 1 {1,S} {3,S} {5,S}
3     C 0 {2,S} {4,S}
4     O 0 {3,S}
5     C 0 {2,S}
""",
    product2 = 
"""
1     C 0 {2,S}
2  *1 C 0 {1,S} {3,S} {4,S}
3     C 0 {2,S}
4  *2 H 0 {2,S}
""",
    kinetics = Arrhenius(
        A = (2.35e-06,"cm^3/(mol*s)"),
        n = 4.84,
        Ea = (4.27,"kcal/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    degeneracy = 1,
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.

InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)
 +
InChI=1/C3H7/c1-3-2/h3H,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C3H8/c1-3-2/h3H2,1-2H3 (external symmetry number = 2, spin multiplicity = 1)

Tsang [Tsang1990]_ recommends k(T) = 1.51e-03 * (T/K)^4.2 * exp(-5.96 kcal/mol /RT) cm3 mol-1 s-1
for the reaction iso-C4H10 + iso-C3H7 = C3H8 + tert-C4H9.  The new rate coefficient expression is
in good agreement with this expression (within a factor of 3.5 over the valid temperature range).
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

