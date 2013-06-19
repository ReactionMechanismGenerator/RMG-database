#!/usr/bin/env python
# encoding: utf-8

name = "H_Abstraction/TS_training"
shortDesc = u"Distances used to train group additivity values for TS geometries"
longDesc = u"""
Put interatomic distances for reactions to use as a training set for fitting
group additivity values in this file.
"""
recommended = True

entry(
    index = 301,
    reactant1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,S}
2    C 0 {1,S} {3,S}
3    C 0 {2,S} {4,S}
4    C 0 {3,S} {5,S}
5    O 0 {4,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S} {5,S}
4 *1 C 0 {2,S} {6,S}
5    O 0 {3,S}
6 *2 H 0 {4,S}
""",
    degeneracy = 2,
    distances = {},
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
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S} {3,S}
3    C 0 {2,S} {4,S}
4    C 0 {3,S} {5,S}
5    O 0 {4,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S}
2 *1 C 0 {1,S} {4,S} {6,S}
3    C 0 {1,S} {5,S}
4    C 0 {2,S}
5    O 0 {3,S}
6 *2 H 0 {2,S}
""",
    degeneracy = 2,
    distances = DistanceGeom(
        # d12 = 1.1,
        # d23 = 1.4,
        # d13 = 2.5,
    ),
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
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,S}
3 *3 C 1 {2,S} {4,S}
4    C 0 {3,S} {5,S}
5    O 0 {4,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product2 = 
"""
1 *1 C 0 {2,S} {3,S} {6,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S} {5,S}
4    C 0 {2,S}
5    O 0 {3,S}
6 *2 H 0 {1,S}
""",
    degeneracy = 2,
    distances = {},
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
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,S}
3    C 0 {2,S} {4,S}
4 *3 C 1 {3,S} {5,S}
5    O 0 {4,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3 *1 C 0 {1,S} {5,S} {6,S}
4    C 0 {2,S}
5    O 0 {3,S}
6 *2 H 0 {3,S}
""",
    degeneracy = 2,
    distances = {},
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
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,S}
2    C 0 {1,S} {3,S}
3    C 0 {2,S} {4,S} {5,S}
4    C 0 {3,S}
5    O 0 {3,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S} {5,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S}
4 *1 C 0 {2,S} {6,S}
5    O 0 {1,S}
6 *2 H 0 {4,S}
""",
    degeneracy = 2,
    distances = {},
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
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S} {3,S}
3    C 0 {2,S} {4,S} {5,S}
4    C 0 {3,S}
5    O 0 {3,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S} {5,S}
2 *1 C 0 {1,S} {4,S} {6,S}
3    C 0 {1,S}
4    C 0 {2,S}
5    O 0 {1,S}
6 *2 H 0 {2,S}
""",
    degeneracy = 2,
    distances = {},
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
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,S}
3 *3 C 1 {2,S} {4,S} {5,S}
4    C 0 {3,S}
5    O 0 {3,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product2 = 
"""
1 *1 C 0 {2,S} {3,S} {5,S} {6,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S}
4    C 0 {2,S}
5    O 0 {1,S}
6 *2 H 0 {1,S}
""",
    degeneracy = 2,
    distances = {},
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
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,S}
3    C 0 {2,S} {4,S} {5,S}
4 *3 C 1 {3,S}
5    O 0 {3,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S} {5,S}
2    C 0 {1,S} {4,S}
3 *1 C 0 {1,S} {6,S}
4    C 0 {2,S}
5    O 0 {1,S}
6 *2 H 0 {3,S}
""",
    degeneracy = 2,
    distances = {},
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
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 {1,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    O 0 {1,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S} {4,S} {5,S}
2 *1 C 0 {1,S} {6,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    O 0 {1,S}
6 *2 H 0 {2,S}
""",
    degeneracy = 2,
    distances = {},
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
1 *1 C 0 {2,D} {3,S}
2    O 0 {1,D}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,D}
2    C 0 {1,D} {3,S} {4,S}
3 *3 C 1 {2,S}
4    C 0 {2,S}
""",
    product1 = 
"""
1 *3 C 1 {2,D}
2    O 0 {1,D}
""",
    product2 = 
"""
1    C 0 {2,D}
2    C 0 {1,D} {3,S} {4,S}
3 *1 C 0 {2,S} {5,S}
4    C 0 {2,S}
5 *2 H 0 {3,S}
""",
    degeneracy = 2,
    distances = {},
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
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,S} {4,S}
3    C 0 {2,S}
4 *2 H 0 {2,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S} {3,S} {5,S}
3    C 0 {2,S} {4,S}
4    O 0 {3,S}
5    C 0 {2,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S} {3,S}
3    C 0 {2,S}
""",
    product2 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {6,S}
2    C 0 {1,S} {5,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    O 0 {2,S}
6 *2 H 0 {1,S}
""",
    degeneracy = 2,
    distances = {},
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
1    C 0 {2,S} {3,S} {4,S}
2 *1 C 0 {1,S} {5,S} {6,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    O 0 {2,S}
6 *2 H 0 {2,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S} {3,S}
3    C 0 {2,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,S} {5,S}
3 *3 C 1 {2,S} {4,S}
4    O 0 {3,S}
5    C 0 {2,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,S} {4,S}
3    C 0 {2,S}
4 *2 H 0 {2,S}
""",
    degeneracy = 2,
    distances = {},
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
1    C 0 {2,D}
2    C 0 {1,D} {3,S} {4,S}
3 *1 C 0 {2,S} {5,S}
4    C 0 {2,S}
5 *2 H 0 {3,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,S}
2    C 0 {1,S} {3,S} {5,S}
3    C 0 {2,S} {4,S}
4    O 0 {3,S}
5    C 0 {2,S}
""",
    product1 = 
"""
1    C 0 {2,D}
2    C 0 {1,D} {3,S} {4,S}
3 *3 C 1 {2,S}
4    C 0 {2,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S} {5,S}
3 *1 C 0 {1,S} {6,S}
4    C 0 {1,S}
5    O 0 {2,S}
6 *2 H 0 {3,S}
""",
    degeneracy = 6,
    distances = {},
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
1    C 0 {2,D}
2    C 0 {1,D} {3,S} {4,S}
3 *1 C 0 {2,S} {5,S}
4    C 0 {2,S}
5 *2 H 0 {3,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S} {3,S} {5,S}
3    C 0 {2,S} {4,S}
4    O 0 {3,S}
5    C 0 {2,S}
""",
    product1 = 
"""
1    C 0 {2,D}
2    C 0 {1,D} {3,S} {4,S}
3 *3 C 1 {2,S}
4    C 0 {2,S}
""",
    product2 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {6,S}
2    C 0 {1,S} {5,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    O 0 {2,S}
6 *2 H 0 {1,S}
""",
    degeneracy = 6,
    distances = {},
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
1    C 0 {2,D}
2    C 0 {1,D} {3,S} {4,S}
3 *1 C 0 {2,S} {5,S}
4    C 0 {2,S}
5 *2 H 0 {3,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,S} {5,S}
3 *3 C 1 {2,S} {4,S}
4    O 0 {3,S}
5    C 0 {2,S}
""",
    product1 = 
"""
1    C 0 {2,D}
2    C 0 {1,D} {3,S} {4,S}
3 *3 C 1 {2,S}
4    C 0 {2,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S} {4,S}
2 *1 C 0 {1,S} {5,S} {6,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    O 0 {2,S}
6 *2 H 0 {2,S}
""",
    degeneracy = 6,
    distances = {},
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
1    C 0 {2,D}
2    C 0 {1,D} {3,S} {4,S}
3 *1 C 0 {2,S} {5,S}
4    C 0 {2,S}
5 *2 H 0 {3,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,S} {5,S}
3    C 0 {2,S} {4,S}
4 *3 O 1 {3,S}
5    C 0 {2,S}
""",
    product1 = 
"""
1    C 0 {2,D}
2    C 0 {1,D} {3,S} {4,S}
3 *3 C 1 {2,S}
4    C 0 {2,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S} {5,S}
3    C 0 {1,S}
4    C 0 {1,S}
5 *1 O 0 {2,S} {6,S}
6 *2 H 0 {5,S}
""",
    degeneracy = 6,
    distances = {},
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
1 *1 C 0 {2,S} {4,S}
2    C 0 {1,S} {3,D}
3    C 0 {2,D}
4 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,S}
2    C 0 {1,S} {3,S} {5,S}
3    C 0 {2,S} {4,S}
4    O 0 {3,S}
5    C 0 {2,S}
""",
    product1 = 
"""
1 *3 C 1 {2,S}
2    C 0 {1,S} {3,D}
3    C 0 {2,D}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S} {5,S}
3 *1 C 0 {1,S} {6,S}
4    C 0 {1,S}
5    O 0 {2,S}
6 *2 H 0 {3,S}
""",
    degeneracy = 3,
    distances = {},
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
1 *1 C 0 {2,S} {4,S}
2    C 0 {1,S} {3,D}
3    C 0 {2,D}
4 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S} {3,S} {5,S}
3    C 0 {2,S} {4,S}
4    O 0 {3,S}
5    C 0 {2,S}
""",
    product1 = 
"""
1 *3 C 1 {2,S}
2    C 0 {1,S} {3,D}
3    C 0 {2,D}
""",
    product2 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {6,S}
2    C 0 {1,S} {5,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    O 0 {2,S}
6 *2 H 0 {1,S}
""",
    degeneracy = 3,
    distances = {},
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
1 *1 C 0 {2,S} {4,S}
2    C 0 {1,S} {3,D}
3    C 0 {2,D}
4 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,S} {5,S}
3 *3 C 1 {2,S} {4,S}
4    O 0 {3,S}
5    C 0 {2,S}
""",
    product1 = 
"""
1 *3 C 1 {2,S}
2    C 0 {1,S} {3,D}
3    C 0 {2,D}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S} {4,S}
2 *1 C 0 {1,S} {5,S} {6,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    O 0 {2,S}
6 *2 H 0 {2,S}
""",
    degeneracy = 3,
    distances = {},
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
1 *1 C 0 {2,S} {4,S}
2    C 0 {1,S} {3,D}
3    C 0 {2,D}
4 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,S} {5,S}
3    C 0 {2,S} {4,S}
4 *3 O 1 {3,S}
5    C 0 {2,S}
""",
    product1 = 
"""
1 *3 C 1 {2,S}
2    C 0 {1,S} {3,D}
3    C 0 {2,D}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S} {5,S}
3    C 0 {1,S}
4    C 0 {1,S}
5 *1 O 0 {2,S} {6,S}
6 *2 H 0 {5,S}
""",
    degeneracy = 3,
    distances = {},
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
1 *1 C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,S}
2    C 0 {1,S} {3,S} {5,S}
3    C 0 {2,S} {4,S}
4    O 0 {3,S}
5    C 0 {2,S}
""",
    product1 = 
"""
1 *3 C 1 {2,S}
2    C 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S} {5,S}
3 *1 C 0 {1,S} {6,S}
4    C 0 {1,S}
5    O 0 {2,S}
6 *2 H 0 {3,S}
""",
    degeneracy = 6,
    distances = {},
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
1 *1 C 0 {2,S} {3,S} {4,S} {6,S}
2    C 0 {1,S} {5,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    O 0 {2,S}
6 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,S}
2    C 0 {1,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S} {3,S} {5,S}
3    C 0 {2,S} {4,S}
4    O 0 {3,S}
5    C 0 {2,S}
""",
    product2 = 
"""
1 *1 C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *2 H 0 {1,S}
""",
    degeneracy = 1,
    distances = {},
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
1    C 0 {2,S} {3,S} {4,S}
2 *1 C 0 {1,S} {5,S} {6,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    O 0 {2,S}
6 *2 H 0 {2,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,S}
2    C 0 {1,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,S} {5,S}
3 *3 C 1 {2,S} {4,S}
4    O 0 {3,S}
5    C 0 {2,S}
""",
    product2 = 
"""
1 *1 C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *2 H 0 {1,S}
""",
    degeneracy = 2,
    distances = {},
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
1 *1 C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,S} {5,S}
3    C 0 {2,S} {4,S}
4 *3 O 1 {3,S}
5    C 0 {2,S}
""",
    product1 = 
"""
1 *3 C 1 {2,S}
2    C 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S} {5,S}
3    C 0 {1,S}
4    C 0 {1,S}
5 *1 O 0 {2,S} {6,S}
6 *2 H 0 {5,S}
""",
    degeneracy = 6,
    distances = {},
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
1 *1 C 0 {2,S} {3,S} {4,S} {6,S}
2    C 0 {1,S} {5,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    O 0 {2,S}
6 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,D}
2    C 0 {1,D}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S} {3,S} {5,S}
3    C 0 {2,S} {4,S}
4    O 0 {3,S}
5    C 0 {2,S}
""",
    product2 = 
"""
1 *1 C 0 {2,D} {3,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
""",
    degeneracy = 1,
    distances = {},
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
1    C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S} {5,S}
3 *1 C 0 {1,S} {6,S}
4    C 0 {1,S}
5    O 0 {2,S}
6 *2 H 0 {3,S}
""",
    reactant2 = 
"""
1    C 0 {2,D}
2 *3 C 1 {1,D} {3,S}
3    C 0 {2,S}
""",
    product1 = 
"""
1 *3 C 1 {2,S}
2    C 0 {1,S} {3,S} {5,S}
3    C 0 {2,S} {4,S}
4    O 0 {3,S}
5    C 0 {2,S}
""",
    product2 = 
"""
1    C 0 {2,D}
2 *1 C 0 {1,D} {3,S} {4,S}
3    C 0 {2,S}
4 *2 H 0 {2,S}
""",
    degeneracy = 6,
    distances = {},
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
1    C 0 {2,S} {3,S} {4,S}
2 *1 C 0 {1,S} {5,S} {6,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    O 0 {2,S}
6 *2 H 0 {2,S}
""",
    reactant2 = 
"""
1    C 0 {2,D}
2 *3 C 1 {1,D} {3,S}
3    C 0 {2,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,S} {5,S}
3 *3 C 1 {2,S} {4,S}
4    O 0 {3,S}
5    C 0 {2,S}
""",
    product2 = 
"""
1    C 0 {2,D}
2 *1 C 0 {1,D} {3,S} {4,S}
3    C 0 {2,S}
4 *2 H 0 {2,S}
""",
    degeneracy = 2,
    distances = {},
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
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,S} {5,S}
3    C 0 {2,S} {4,D}
4    O 0 {3,D}
5 *2 H 0 {2,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,S}
2    C 0 {1,S} {3,S} {5,S}
3    C 0 {2,S} {4,S}
4    O 0 {3,S}
5    C 0 {2,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S} {3,S}
3    C 0 {2,S} {4,D}
4    O 0 {3,D}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S} {5,S}
3 *1 C 0 {1,S} {6,S}
4    C 0 {1,S}
5    O 0 {2,S}
6 *2 H 0 {3,S}
""",
    degeneracy = 2,
    distances = {},
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
1 *1 C 0 {2,S} {3,S} {4,S} {6,S}
2    C 0 {1,S} {5,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    O 0 {2,S}
6 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S} {3,S}
3    C 0 {2,S} {4,D}
4    O 0 {3,D}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S} {3,S} {5,S}
3    C 0 {2,S} {4,S}
4    O 0 {3,S}
5    C 0 {2,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,S} {5,S}
3    C 0 {2,S} {4,D}
4    O 0 {3,D}
5 *2 H 0 {2,S}
""",
    degeneracy = 1,
    distances = {},
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
1    C 0 {2,S} {3,S} {4,S}
2 *1 C 0 {1,S} {5,S} {6,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    O 0 {2,S}
6 *2 H 0 {2,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S} {3,S}
3    C 0 {2,S} {4,D}
4    O 0 {3,D}
""",
    product1 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,S} {5,S}
3 *3 C 1 {2,S} {4,S}
4    O 0 {3,S}
5    C 0 {2,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,S} {5,S}
3    C 0 {2,S} {4,D}
4    O 0 {3,D}
5 *2 H 0 {2,S}
""",
    degeneracy = 2,
    distances = {},
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
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,S} {5,S} {6,S}
3    C 0 {2,S} {4,D}
4    O 0 {3,D}
5    C 0 {2,S}
6 *2 H 0 {2,S}
""",
    reactant2 = 
"""
1 *3 H 1
""",
    product1 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S} {3,S} {5,S}
3    C 0 {2,S} {4,D}
4    O 0 {3,D}
5    C 0 {2,S}
""",
    product2 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    degeneracy = 1,
    distances = {},
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
1    C 0 {2,D}
2    C 0 {1,D} {3,S} {4,S}
3 *1 C 0 {2,S} {5,S}
4    C 0 {2,S}
5 *2 H 0 {3,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,D}
3    C 0 {2,D} {4,S}
4 *3 O 1 {3,S}
""",
    product1 = 
"""
1    C 0 {2,D}
2    C 0 {1,D} {3,S} {4,S}
3 *3 C 1 {2,S}
4    C 0 {2,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,D}
3    C 0 {2,D} {4,S}
4 *1 O 0 {3,S} {5,S}
5 *2 H 0 {4,S}
""",
    degeneracy = 6,
    distances = {},
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
    index = 525,
    reactant1 = 
"""
1 *1 C 0 {2,S} {5,S}
2    C 0 {1,S} {3,D}
3    C 0 {2,D} {4,S}
4    C 0 {3,S}
5 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product1 = 
"""
1 *3 C 1 {2,S}
2    C 0 {1,S} {3,D}
3    C 0 {2,D} {4,S}
4    C 0 {3,S}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S}
3 *2 H 0 {1,S}
""",
    degeneracy = 6,
    distances = {},
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""SSM CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
SSM CBS-QB3 calculations w/RRHO.

InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+ (external symmetry number = 2, spin multiplicity = 1)
 +
HO2 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H7/c1-3-4-2/h3-4H,1H2,2H3  (external symmetry number = 1, spin multiplicity = 2)
 +
H2O2 (external symmetry number = 2, spin multiplicity = 1)
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 527,
    reactant1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S} {3,D}
3    C 0 {2,D} {4,S}
4    C 0 {3,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,D} {5,S}
3    C 0 {2,D} {4,S}
4    C 0 {3,S}
5 *2 H 0 {2,S}
""",
    degeneracy = 2,
    distances = {},
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""SSM CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
SSM CBS-QB3 calculations w/RRHO.
The rate rule is valid in a range of temperature from 300 -2000 K.
The Wigner tunneling currection that was used to account for tunneling.

InChI=1/C4H7/c1-3-4-2/h3H,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 +
H2O2 (external symmetry number = 2, spin multiplicity = 1)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+  (external symmetry number = 2, spin multiplicity = 1)
 +
HO2 (external symmetry number = 1, spin multiplicity = 2)
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 529,
    reactant1 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,S} {5,S}
3    C 0 {2,S} {4,D}
4    C 0 {3,D}
5 *2 H 0 {2,S}
""",
    reactant2 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S} {3,S}
3    C 0 {2,S} {4,D}
4    C 0 {3,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S}
3 *2 H 0 {1,S}
""",
    degeneracy = 2,
    distances = {},
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""SSM CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
SSM CBS-QB3 calculations w/RRHO.
The rate rule is valid in a range of temperature from 300 -2000 K.
The Wigner tunneling currection that was used to account for tunneling.

InChI=1/C4H8/c1-3-4-2/h3H,1,4H2,2H3 (external symmetry number = 1, spin multiplicity = 1)
 +
HO2 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H7/c1-3-4-2/h3-4H,1H2,2H3   (external symmetry number = 1, spin multiplicity = 2)
 +
H2O2 (external symmetry number = 2, spin multiplicity = 1)
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 531,
    reactant1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,S}
3    C 0 {2,S} {4,D}
4 *3 C 1 {3,D}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,S}
3    C 0 {2,S} {4,D}
4 *1 C 0 {3,D} {5,S}
5 *2 H 0 {4,S}
""",
    degeneracy = 2,
    distances = {},
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""SSM CBS-QB3 calculations w/o HR corrections""",
    longDesc = 
u"""
SSM CBS-QB3 calculations w/RRHO .  Pre-exponential was divided by 2 to account for summetry of H2O2
The rate rule is valid in a range of temperature from 300 -2000 K.
The Wigner tunneling currection that was used to account for tunneling.

InChI=1/C4H7/c1-3-4-2/h1,3H,4H2,2H3  (external symmetry number = 1, spin multiplicity = 2)
 +
H2O2 (external symmetry number = 2, spin multiplicity = 1)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H8/c1-3-4-2/h3H,1,4H2,2H3  (external symmetry number = 1, spin multiplicity = 1)
 +
HO2 (external symmetry number = 1, spin multiplicity = 2)
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 534,
    reactant1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,S}
3    C 0 {2,S} {4,D}
4    C 0 {3,D} {5,S}
5 *3 O 1 {4,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,S}
3    C 0 {2,S} {4,D}
4    C 0 {3,D} {5,S}
5 *1 O 0 {4,S} {6,S}
6 *2 H 0 {5,S}
""",
    degeneracy = 2,
    distances = {},
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MHS CBS-QB3 w/1dHR calculations""",
    longDesc = 
u"""
Exact reaction: HOOH + *O-CH=CH-C2H5 <=> HO-CH=CH-C2H5 + HOO*
Rxn family nodes: H2O2 + InChI=1/C4H7O/c1-2-3-4-5/h3-4H,2H2,1H3

MHS computed rate coefficient using CBS-QB3 method, see _[MRHCBSQB3RRHO] for general algorithm
employed.  Two differences::
    1) the k(T) was calculated from 600 to 2000 K, in 200 K increments.
    2) Low-frequency torsional modes were treated as 1-d separable hindered rotors.  The scans
        were performed at the B3LYP/6-31G(d) level.

MHS computed the fitted Arrhenius expression to be: k(T) = 6.99e-2 (T/1K)^3.75 exp(-10.89 kcal mol-1 / RT) cm3 mol-1 s-1.
The pre-exponential was divided by 2 to get the per-H event.  The uncertainty in the E0
was estimated to be 2 kcal mol-1 (general accuracy of CBS-QB3 calculations) and the uncertainty
in the A parameter was MRH guess.

RMG previously estimated the kinetics of the titled reaction to be ~10^3 times faster
than calculations of MHS.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 536,
    reactant1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S} {3,S}
3    C 0 {2,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {4,S}
2    O 0 {1,S} {3,S}
3    C 0 {2,S}
4 *2 H 0 {1,S}
""",
    degeneracy = 2,
    distances = {},
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MHS CBS-QB3 w/1dHR calculations""",
    longDesc = 
u"""
Exact reaction: HOOH + *O-O-CH3 <=> HO-O-CH3 + HOO*
Rxn family nodes: H2O2 + OOCH3

MHS computed rate coefficient using CBS-QB3 method, see _[MRHCBSQB3RRHO] for general algorithm
employed.  Two differences::
    1) the k(T) was calculated from 600 to 2000 K, in 200 K increments.
    2) Low-frequency torsional modes were treated as 1-d separable hindered rotors.  The scans
        were performed at the B3LYP/6-31G(d) level.

MHS computed the fitted Arrhenius expression to be: k(T) = 1.84e-1 (T/1K)^3.96 exp(-6.63 kcal mol-1 / RT) cm3 mol-1 s-1.
The pre-exponential was divided by 2 to get the per-H event.  The uncertainty in the E0
was estimated to be 2 kcal mol-1 (general accuracy of CBS-QB3 calculations) and the uncertainty
in the A parameter was MRH guess.

RMG previously estimated the kinetics of the titled reaction to be 1-3 orders of magnitude faster
than calculations of MHS.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 538,
    reactant1 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,S} {5,S}
3    C 0 {2,S} {4,D}
4    C 0 {3,D}
5 *2 H 0 {2,S}
""",
    reactant2 = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S} {3,S}
3    C 0 {2,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S} {3,S}
3    C 0 {2,S} {4,D}
4    C 0 {3,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {4,S}
2    O 0 {1,S} {3,S}
3    C 0 {2,S}
4 *2 H 0 {1,S}
""",
    degeneracy = 2,
    distances = {},
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations, w/1dHR corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations w/1d hindered rotor corrections
Exact reaction: CH3CH2CH=CH2 + OOCH3 = HOOCH3 + CH3CHCH=CH2

This reaction was of interest to MRH/MHS because the butanol model was sensitive to its kinetics
(in particular, the C4H8-1 predicted concentration for 10-atm JSR simulations between 800-1000 K).
The original mechanism had an estimate that was much faster than these new calculations (the RMG old
k(T) was 50-100x faster than these calculations between 800-1000 K).

MRH computed these kinetics using the CBS-QB3 method.  Hindered rotor corrections were accounted for in all species:
    CH3CH2CH=CH2: -CH3 and -CH2CH3 rotor
    OOCH3: -CH3 rotor
    TS: -CH3 and -CH=CH2 rotor of react1, -CH3 and -OCH3 of react2, and -OOCH3 between react1 and react2
    HOOCH3: -CH3 and -OCH3 rotor
    CH3CHCH=CH2: -CH3 and -CH=CH2 rotor
External symmetry number of all speces was 1.  k(T) was computed from 600 - 2000 K, in 200 K intervals.  An
asymmetric Eckart tunneling correction was used.

The computed k(T) was 1.482e-02 * (T/1K)^4.313 * exp(-8.016 kcal/mol / RT) cm3 mol-1 s-1.

NOTE: Running PopulateReactions before and after this number produced results that differed by less than a factor
of three.  New numbers in the RMG database thus lead to an improvement in the RMG estimate (RMG works!).  Also,
this computed rate coefficient is a factor of 10 faster than Tsang's recommendation for C3H6 + OOCH3 = HOOCH3 + allyl;
his stated uncertainty is a factor of ten.  However, one would expect abstraction from the secondary carbon of
1-butane to be faster than the primary carbon of propene, because the C-H bond strength should be weaker.  So,
this calculation is in reasonable agreement with the literature.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 539,
    reactant1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,S}
2    C 0 {1,S} {3,D}
3    C 0 {2,D}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product2 = 
"""
1 *1 C 0 {2,S} {4,S}
2    C 0 {1,S} {3,D}
3    C 0 {2,D}
4 *2 H 0 {1,S}
""",
    degeneracy = 2,
    distances = {},
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MHS CBS-QB3 w/1dHR calculations""",
    longDesc = 
u"""
MHS CBS-QB3 calculations w/1d hindered rotor corrections
Exact reaction: *CH2-CH=CH2 + H2O2 = CH3-CH=CH2 + HO2

MHS computed rate coefficient using CBS-QB3 method, see _[MRHCBSQB3RRHO] for general algorithm
employed.  Two differences::
    1) the k(T) was calculated from 600 to 2000 K, in 200 K increments.
    2) Low-frequency torsional modes were treated as 1-d separable hindered rotors.  The scans
        were performed at the B3LYP/6-31G(d) level.

MHS computed the fitted Arrhenius expression to be: k(T) = 3.51e-2 (T/1K)^4.22 exp(-9.86 kcal mol-1 / RT) cm3 mol-1 s-1.
The uncertainty in the E0
was estimated to be 2 kcal mol-1 (general accuracy of CBS-QB3 calculations) and the uncertainty
in the A parameter was MRH guess.

RMG previously estimated the kinetics of the titled reaction to be ~2 orders of magnitude faster
than calculations of MHS.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 540,
    reactant1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S}
4 *1 C 0 {2,S} {5,D} {6,S}
5    O 0 {4,D}
6 *2 H 0 {4,S}
""",
    reactant2 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S}
4 *3 C 1 {2,S} {5,D}
5    O 0 {4,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S}
3 *2 H 0 {1,S}
""",
    degeneracy = 1,
    distances = {},
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MHS CBS-QB3 w/o 1dHR calculations""",
    longDesc = 
u"""
MHS CBS-QB3 calculations without 1d hindered rotor correction (due to presence of hydrogen bond interactions)
Exact reaction: HO2 + CH3-CH2-CH2-CH=O = H2O2 + CH3-CH2-CH2-C*=O

MHS computed rate coefficient using CBS-QB3 method, see _[MRHCBSQB3RRHO] for general algorithm
employed.  With the difference that the k(T) was calculated from 600 to 2000 K, in 200 K increments.

MHS computed the fitted Arrhenius expression to be: k(T) = 1.91e-4 (T/1K)^4.25 exp(-0.81 kcal mol-1 / RT) cm3 mol-1 s-1.
The uncertainty in the E0 was estimated to be 2 kcal mol-1 (general accuracy of CBS-QB3 calculations) and the uncertainty
in the A parameter was MRH guess.
""",
    history = [
        ("Thu Sep  8 09:54:43 2011","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1002,
    reactant1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {6,S}
2    C 0 {1,S} {5,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    O 0 {2,S}
6 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S} {3,S}
3    C 0 {2,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S} {3,S} {5,S}
3    C 0 {2,S} {4,S}
4    O 0 {3,S}
5    C 0 {2,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,S} {4,S}
3    C 0 {2,S}
4 *2 H 0 {2,S}
""",
    degeneracy = 1,
    distances = {},
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

entry(
    index = 1003,
    reactant1 = 
"""
1 *1 C 0 {2,S} {5,S}
2    C 0 {1,S} {3,D} {4,S}
3    O 0 {2,D}
4    C 0 {2,S}
5 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *3 C 1 {2,S}
2    C 0 {1,S} {3,D} {4,S}
3    O 0 {2,D}
4    C 0 {2,S}
""",
    product2 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    degeneracy = 6,
    distances = {},
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""John Simmie, G3 calculations. Rate constant per H atom.""",
    longDesc = 
u"""
CC(=O)C + OH --> CJC(=O)C + H2O

G3 PES calculations using Variflex including tunneling corrections.

High-pressure limit rate constants of the title reactions have been calculated in the temperature range
of 500–2000 K using the Variflex code including Eckart tunneling corrections. Variable reaction coordinate
transition state theory (VRC-TST) has been used for the rate constants of the barrier-less entrance channel.

Chong-Wen Zhou, John M. Simmie and Henry J. Curran
Phys. Chem. Chem. Phys., 2011, 13, 11175-11192
DOI: 10.1039/C0CP02754E
""",
    history = [
        ("Wed Jun  14 13:17:47 2011","Connie Gao <connieg@mit.edu>","action","""connieg added this entry."""),
    ],
)

entry(
    index = 1004,
    reactant1 = 
"""
1 *1 C 0 {2,S} {6,S}
2    C 0 {1,S} {3,D} {4,S}
3    O 0 {2,D}
4    C 0 {2,S} {5,S}
5    C 0 {4,S}
6 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *3 C 1 {2,S}
2    C 0 {1,S} {3,D} {4,S}
3    O 0 {2,D}
4    C 0 {2,S} {5,S}
5    C 0 {4,S}
""",
    product2 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    degeneracy = 3,
    distances = {},
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""John Simmie, G3 calculations. Rate constant per H atom.""",
    longDesc = 
u"""
CC(=O)CC + OH --> CJC(=O)CC + H2O

G3 PES calculations using Variflex including tunneling corrections.

High-pressure limit rate constants of the title reactions have been calculated in the temperature range
of 500–2000 K using the Variflex code including Eckart tunneling corrections. Variable reaction coordinate
transition state theory (VRC-TST) has been used for the rate constants of the barrier-less entrance channel.

Chong-Wen Zhou, John M. Simmie and Henry J. Curran
Phys. Chem. Chem. Phys., 2011, 13, 11175-11192
DOI: 10.1039/C0CP02754E
""",
    history = [
        ("Wed Jun  14 13:17:47 2011","Connie Gao <connieg@mit.edu>","action","""connieg added this entry."""),
    ],
)

entry(
    index = 1005,
    reactant1 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,D} {4,S}
3    O 0 {2,D}
4 *1 C 0 {2,S} {5,S} {6,S}
5    C 0 {4,S}
6 *2 H 0 {4,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,D} {4,S}
3    O 0 {2,D}
4 *3 C 1 {2,S} {5,S}
5    C 0 {4,S}
""",
    product2 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    degeneracy = 2,
    distances = {},
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""John Simmie, G3 calculations. Rate constant per H atom.""",
    longDesc = 
u"""
CC(=O)CC + OH --> CC(=)CJC + H2O

G3 PES calculations using Variflex including tunneling corrections.

High-pressure limit rate constants of the title reactions have been calculated in the temperature range
of 500–2000 K using the Variflex code including Eckart tunneling corrections. Variable reaction coordinate
transition state theory (VRC-TST) has been used for the rate constants of the barrier-less entrance channel.

Chong-Wen Zhou, John M. Simmie and Henry J. Curran
Phys. Chem. Chem. Phys., 2011, 13, 11175-11192
DOI: 10.1039/C0CP02754E
""",
    history = [
        ("Wed Jun  14 13:17:47 2011","Connie Gao <connieg@mit.edu>","action","""connieg added this entry."""),
    ],
)

entry(
    index = 1006,
    reactant1 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,D} {4,S}
3    O 0 {2,D}
4    C 0 {2,S} {5,S}
5 *1 C 0 {4,S} {6,S}
6 *2 H 0 {5,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,D} {4,S}
3    O 0 {2,D}
4    C 0 {2,S} {5,S}
5 *3 C 1 {4,S}
""",
    product2 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    degeneracy = 3,
    distances = {},
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""John Simmie, G3 calculations. Rate constant per H atom.""",
    longDesc = 
u"""
CC(=O)CC + OH --> CC(=O)CCJ + H2O

G3 PES calculations using Variflex including tunneling corrections.

High-pressure limit rate constants of the title reactions have been calculated in the temperature range
of 500–2000 K using the Variflex code including Eckart tunneling corrections. Variable reaction coordinate
transition state theory (VRC-TST) has been used for the rate constants of the barrier-less entrance channel.

Chong-Wen Zhou, John M. Simmie and Henry J. Curran
Phys. Chem. Chem. Phys., 2011, 13, 11175-11192
DOI: 10.1039/C0CP02754E
""",
    history = [
        ("Wed Jun  14 13:17:47 2011","Connie Gao <connieg@mit.edu>","action","""connieg added this entry."""),
    ],
)

entry(
    index = 1007,
    reactant1 = 
"""
1 *1 C 0 {2,S} {7,S}
2    C 0 {1,S} {3,D} {4,S}
3    O 0 {2,D}
4    C 0 {2,S} {5,S} {6,S}
5    C 0 {4,S}
6    C 0 {4,S}
7 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1    C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S}
3    C 0 {1,S}
4    C 0 {1,S} {5,S} {6,D}
5 *3 C 1 {4,S}
6    O 0 {4,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    degeneracy = 3,
    distances = {},
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""John Simmie, G3 calculations. Rate constant per H atom.""",
    longDesc = 
u"""
CC(=O)C(C)C + OH --> CJC(=O)C(C)C

G3 PES calculations using Variflex including tunneling corrections.

High-pressure limit rate constants of the title reactions have been calculated in the temperature range
of 500–2000 K using the Variflex code including Eckart tunneling corrections. Variable reaction coordinate
transition state theory (VRC-TST) has been used for the rate constants of the barrier-less entrance channel.

Chong-Wen Zhou, John M. Simmie and Henry J. Curran
Phys. Chem. Chem. Phys., 2011, 13, 11175-11192
DOI: 10.1039/C0CP02754E
""",
    history = [
        ("Wed Jun  14 13:17:47 2011","Connie Gao <connieg@mit.edu>","action","""connieg added this entry."""),
    ],
)

entry(
    index = 1008,
    reactant1 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,D} {4,S}
3    O 0 {2,D}
4 *1 C 0 {2,S} {5,S} {6,S} {7,S}
5    C 0 {4,S}
6    C 0 {4,S}
7 *2 H 0 {4,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1    C 0 {4,S}
2    C 0 {4,S}
3    C 0 {5,S}
4 *3 C 1 {1,S} {2,S} {5,S}
5    C 0 {3,S} {4,S} {6,D}
6    O 0 {5,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    degeneracy = 1,
    distances = {},
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""John Simmie, G3 calculations. Rate constant per H atom.""",
    longDesc = 
u"""
CC(=O)C(C)C + OH --> CC(=O)CJ(C)C

G3 PES calculations using Variflex including tunneling corrections.

High-pressure limit rate constants of the title reactions have been calculated in the temperature range
of 500–2000 K using the Variflex code including Eckart tunneling corrections. Variable reaction coordinate
transition state theory (VRC-TST) has been used for the rate constants of the barrier-less entrance channel.

Chong-Wen Zhou, John M. Simmie and Henry J. Curran
Phys. Chem. Chem. Phys., 2011, 13, 11175-11192
DOI: 10.1039/C0CP02754E
""",
    history = [
        ("Wed Jun  14 13:17:47 2011","Connie Gao <connieg@mit.edu>","action","""connieg added this entry."""),
    ],
)

entry(
    index = 1009,
    reactant1 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,D} {4,S}
3    O 0 {2,D}
4    C 0 {2,S} {5,S} {6,S}
5    C 0 {4,S}
6 *1 C 0 {4,S} {7,S}
7 *2 H 0 {6,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1    C 0 {2,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {4,S}
4    C 0 {1,S} {3,S} {6,D}
5 *3 C 1 {1,S}
6    O 0 {4,D}
""",
    product2 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    degeneracy = 6,
    distances = {},
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""John Simmie, G3 calculations. Rate constant per H atom.""",
    longDesc = 
u"""
CC(=O)C(C)C + OH --> CC(=O)C(C)CJ + H2O

G3 PES calculations using Variflex including tunneling corrections.

High-pressure limit rate constants of the title reactions have been calculated in the temperature range
of 500–2000 K using the Variflex code including Eckart tunneling corrections. Variable reaction coordinate
transition state theory (VRC-TST) has been used for the rate constants of the barrier-less entrance channel.

Chong-Wen Zhou, John M. Simmie and Henry J. Curran
Phys. Chem. Chem. Phys., 2011, 13, 11175-11192
DOI: 10.1039/C0CP02754E
""",
    history = [
        ("Wed Jun  14 13:17:47 2011","Connie Gao <connieg@mit.edu>","action","""connieg added this entry."""),
    ],
)

entry(
    index = 1010,
    reactant1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3 *1 C 0 {1,S} {5,S} {6,S}
4    C 0 {2,S}
5    O 0 {3,S}
6 *2 H 0 {3,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S}
4 *3 C 1 {2,S} {5,S}
5    O 0 {4,S}
""",
    degeneracy = 2,
    distances = {},
    reference = None,
    referenceType = "",
    shortDesc = u"""Zador CCSD(T) calc""",
    longDesc = 
u"""
Rate comes from quantum calculation by J. Zador at CCSD(T) level
[ This rate was obtained by personal communication as of Sept 2012]
""",
    history = [
        ("Wed Sep 12 14:33:46 2012","Shamel Merchant <shamel@mit.edu>","action","""New entry. CCCCO + OH = CCC[CH]O + H2O"""),
        ("Wed Sep 12 14:35:29 2012","Shamel Merchant <shamel@mit.edu>","action","""Changed degeneracy to 2"""),
        ("Wed Nov  7 17:13:14 2012","Connie Gao <connieg@mit.edu>","action","""Updated temperature range."""),
    ],
)

