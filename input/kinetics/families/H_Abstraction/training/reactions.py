#!/usr/bin/env python
# encoding: utf-8

name = "H_Abstraction/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "H2O2 + C4H9O <=> HO2 + C4H10O",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (5.76, 'cm^3/(mol*s)'),
        n = 3.16,
        Ea = (0.75, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
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
)

entry(
    index = 1,
    label = "H2O2 + C4H9O-2 <=> HO2 + C4H10O-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.35, 'cm^3/(mol*s)'),
        n = 3.42,
        Ea = (1.43, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
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
)

entry(
    index = 2,
    label = "H2O2 + C4H9O-3 <=> HO2 + C4H10O-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.629, 'cm^3/(mol*s)'),
        n = 3.52,
        Ea = (1.61, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
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
)

entry(
    index = 3,
    label = "H2O2 + C4H9O-4 <=> HO2 + C4H10O-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.97, 'cm^3/(mol*s)'),
        n = 3.39,
        Ea = (1.4, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
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
)

entry(
    index = 4,
    label = "H2O2 + C4H9O-5 <=> HO2 + C4H10O-5",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (11.5, 'cm^3/(mol*s)'),
        n = 2.94,
        Ea = (0.46, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
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
)

entry(
    index = 5,
    label = "H2O2 + C4H9O-6 <=> HO2 + C4H10O-6",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.75, 'cm^3/(mol*s)'),
        n = 2.91,
        Ea = (-0.41, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
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
)

entry(
    index = 6,
    label = "H2O2 + C4H9O-7 <=> HO2 + C4H10O-7",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (34.6, 'cm^3/(mol*s)'),
        n = 3.05,
        Ea = (1.02, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
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
)

entry(
    index = 7,
    label = "H2O2 + C4H9O-8 <=> HO2 + C4H10O-8",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.611, 'cm^3/(mol*s)'),
        n = 3.53,
        Ea = (1.52, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
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
)

entry(
    index = 8,
    label = "H2O2 + C4H9O-9 <=> HO2 + C4H10O-9",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.42, 'cm^3/(mol*s)'),
        n = 3.53,
        Ea = (1.56, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
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
)

entry(
    index = 9,
    label = "CH2O + C4H7 <=> HCO_r3 + C4H8",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (0.0613, 'cm^3/(mol*s)'),
        n = 3.95,
        Ea = (12.22, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
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
)

entry(
    index = 10,
    label = "C3H8 + C4H9O-10 <=> C3H7 + C4H10O-10",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.822e-06, 'cm^3/(mol*s)'),
        n = 5.11,
        Ea = (5.69, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
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
)

entry(
    index = 11,
    label = "C4H10O-11 + C3H7 <=> C4H9O-11 + C3H8",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.12e-06, 'cm^3/(mol*s)'),
        n = 5.06,
        Ea = (4.89, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
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
)

entry(
    index = 12,
    label = "C4H8 + C4H9O-12 <=> C4H7 + C4H10O-12",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (5.034e-05, 'cm^3/(mol*s)'),
        n = 4.89,
        Ea = (4.32, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
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
)

entry(
    index = 13,
    label = "C4H8 + C4H9O-10 <=> C4H7 + C4H10O-10",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (8.64e-05, 'cm^3/(mol*s)'),
        n = 4.52,
        Ea = (1.46, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
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
)

entry(
    index = 14,
    label = "C4H8 + C4H9O-11 <=> C4H7 + C4H10O-11",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (2.946e-05, 'cm^3/(mol*s)'),
        n = 5.07,
        Ea = (3.66, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
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
)

entry(
    index = 15,
    label = "C4H8 + C4H9O-13 <=> C4H7 + C4H10O-13",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (3.498, 'cm^3/(mol*s)'),
        n = 3.74,
        Ea = (1.45, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
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
)

entry(
    index = 16,
    label = "C3H6 + C4H9O-12 <=> C3H5 + C4H10O-12",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (0.0001008, 'cm^3/(mol*s)'),
        n = 4.75,
        Ea = (4.13, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
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
)

entry(
    index = 17,
    label = "C3H6 + C4H9O-10 <=> C3H5 + C4H10O-10",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (4.92e-06, 'cm^3/(mol*s)'),
        n = 4.98,
        Ea = (3.18, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
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
)

entry(
    index = 18,
    label = "C3H6 + C4H9O-11 <=> C3H5 + C4H10O-11",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (9.33e-06, 'cm^3/(mol*s)'),
        n = 4.97,
        Ea = (3.64, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
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
)

entry(
    index = 19,
    label = "C3H6 + C4H9O-13 <=> C3H5 + C4H10O-13",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (0.357, 'cm^3/(mol*s)'),
        n = 3.9,
        Ea = (1.81, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
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
)

entry(
    index = 20,
    label = "C2H6 + C4H9O-12 <=> C2H5 + C4H10O-12",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (1.926e-05, 'cm^3/(mol*s)'),
        n = 5.28,
        Ea = (7.78, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
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
)

entry(
    index = 21,
    label = "C4H10O-10 + C2H5 <=> C4H9O-10 + C2H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.41e-05, 'cm^3/(mol*s)'),
        n = 4.83,
        Ea = (4.37, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
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
)

entry(
    index = 22,
    label = "C4H10O-11 + C2H5 <=> C4H9O-11 + C2H6",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (8.5e-06, 'cm^3/(mol*s)'),
        n = 5.01,
        Ea = (5.01, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
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
)

entry(
    index = 23,
    label = "C2H6 + C4H9O-13 <=> C2H5 + C4H10O-13",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (0.03042, 'cm^3/(mol*s)'),
        n = 4.52,
        Ea = (2.34, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
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
)

entry(
    index = 24,
    label = "C4H10O-10 + C2H3 <=> C4H9O-10 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.49, 'cm^3/(mol*s)'),
        n = 3.33,
        Ea = (0.63, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
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
)

entry(
    index = 25,
    label = "C4H10O-12 + C3H5-2 <=> C4H9O-12 + C3H6-2",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (0.0001866, 'cm^3/(mol*s)'),
        n = 4.87,
        Ea = (3.5, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
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
)

entry(
    index = 26,
    label = "C4H10O-11 + C3H5-2 <=> C4H9O-11 + C3H6-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.0256, 'cm^3/(mol*s)'),
        n = 4.09,
        Ea = (1.31, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
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
)

entry(
    index = 27,
    label = "C3H6O + C4H9O-12 <=> C3H5O + C4H10O-12",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.000312, 'cm^3/(mol*s)'),
        n = 4.31,
        Ea = (3.39, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
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
)

entry(
    index = 28,
    label = "C4H10O-10 + C3H5O <=> C4H9O-10 + C3H6O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.000485, 'cm^3/(mol*s)'),
        n = 4.37,
        Ea = (9.66, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
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
)

entry(
    index = 29,
    label = "C4H10O-11 + C3H5O <=> C4H9O-11 + C3H6O",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.00368, 'cm^3/(mol*s)'),
        n = 4.02,
        Ea = (7.92, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
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
)

entry(
    index = 30,
    label = "C4H8O + H <=> C4H7O + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.08e+07, 'cm^3/(mol*s)'),
        n = 1.84,
        Ea = (3.03, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
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
)

entry(
    index = 31,
    label = "C4H8 + C3H5O-2 <=> C4H7 + C3H6O-2",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (4.512e-07, 'cm^3/(mol*s)'),
        n = 5.77,
        Ea = (12.04, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
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
)

entry(
    index = 32,
    label = "C4H8-2 + HO2_r3 <=> C4H7-2 + H2O2",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (0.00346998, 'cm^3/(mol*s)'),
        n = 4.65,
        Ea = (9.78, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
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
)

entry(
    index = 33,
    label = "H2O2 + C4H7-3 <=> HO2 + C4H8-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.875, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
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
)

entry(
    index = 34,
    label = "C4H8-4 + HO2_r3 <=> C4H7-4 + H2O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.000508, 'cm^3/(mol*s)'),
        n = 4.59,
        Ea = (7.16, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
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
)

entry(
    index = 36,
    label = "H2O2 + C4H7O-2 <=> HO2 + C4H8O-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.0699, 'cm^3/(mol*s)', '*|/', 3),
        n = 3.75,
        Ea = (10.89, 'kcal/mol', '+|-', 2),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
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
)

entry(
    index = 37,
    label = "H2O2 + CH3O2 <=> HO2 + CH4O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.184, 'cm^3/(mol*s)', '*|/', 3),
        n = 3.96,
        Ea = (6.63, 'kcal/mol', '+|-', 2),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
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
)

entry(
    index = 38,
    label = "C4H8-4 + CH3O2 <=> C4H7-4 + CH4O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.01482, 'cm^3/(mol*s)', '*|/', 3),
        n = 4.313,
        Ea = (8.016, 'kcal/mol', '+|-', 2),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
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
)

entry(
    index = 39,
    label = "H2O2 + C3H5 <=> HO2 + C3H6",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (0.0351, 'cm^3/(mol*s)', '*|/', 3),
        n = 4.22,
        Ea = (9.86, 'kcal/mol', '+|-', 2),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
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
)

entry(
    index = 40,
    label = "C4H8O-3 + HO2_r3 <=> C4H7O-3 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.000191, 'cm^3/(mol*s)', '*|/', 3),
        n = 4.25,
        Ea = (0.81, 'kcal/mol', '+|-', 2),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
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
)

entry(
    index = 41,
    label = "C4H10O-10 + C3H7 <=> C4H9O-10 + C3H8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.35e-06, 'cm^3/(mol*s)'),
        n = 4.84,
        Ea = (4.27, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
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
)

entry(
    index = 42,
    label = "C3H6O-3 + OH_r3 <=> C3H5O-3 + H2O_p23",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (132.6, 'cm^3/(mol*s)'),
        n = 3.29,
        Ea = (-1, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""John Simmie, G3 calculations. Rate constant per H atom.""",
    longDesc =
u"""
CC(=O)C + OH --> CJC(=O)C + H2O

G3 PES calculations using Variflex including tunneling corrections.

High-pressure limit rate constants of the title reactions have been calculated in the temperature range
of 5002000 K using the Variflex code including Eckart tunneling corrections. Variable reaction coordinate
transition state theory (VRC-TST) has been used for the rate constants of the barrier-less entrance channel.

Chong-Wen Zhou, John M. Simmie and Henry J. Curran
Phys. Chem. Chem. Phys., 2011, 13, 11175-11192
DOI: 10.1039/C0CP02754E
""",
)

entry(
    index = 43,
    label = "C4H8O-4 + OH_r3 <=> C4H7O-4 + H2O_p23",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (399, 'cm^3/(mol*s)'),
        n = 3.08,
        Ea = (-0.9433, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""John Simmie, G3 calculations. Rate constant per H atom.""",
    longDesc =
u"""
CC(=O)CC + OH --> CJC(=O)CC + H2O

G3 PES calculations using Variflex including tunneling corrections.

High-pressure limit rate constants of the title reactions have been calculated in the temperature range
of 5002000 K using the Variflex code including Eckart tunneling corrections. Variable reaction coordinate
transition state theory (VRC-TST) has been used for the rate constants of the barrier-less entrance channel.

Chong-Wen Zhou, John M. Simmie and Henry J. Curran
Phys. Chem. Chem. Phys., 2011, 13, 11175-11192
DOI: 10.1039/C0CP02754E
""",
)

entry(
    index = 44,
    label = "C4H8O-5 + OH_r3 <=> C4H7O-5 + H2O_p23",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (236, 'cm^3/(mol*s)'),
        n = 3.15,
        Ea = (-3.048, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""John Simmie, G3 calculations. Rate constant per H atom.""",
    longDesc =
u"""
CC(=O)CC + OH --> CC(=)CJC + H2O

G3 PES calculations using Variflex including tunneling corrections.

High-pressure limit rate constants of the title reactions have been calculated in the temperature range
of 5002000 K using the Variflex code including Eckart tunneling corrections. Variable reaction coordinate
transition state theory (VRC-TST) has been used for the rate constants of the barrier-less entrance channel.

Chong-Wen Zhou, John M. Simmie and Henry J. Curran
Phys. Chem. Chem. Phys., 2011, 13, 11175-11192
DOI: 10.1039/C0CP02754E
""",
)

entry(
    index = 45,
    label = "C4H8O-6 + OH_r3 <=> C4H7O-6 + H2O_p23",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.35, 'cm^3/(mol*s)'),
        n = 3.81,
        Ea = (-2.897, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""John Simmie, G3 calculations. Rate constant per H atom.""",
    longDesc =
u"""
CC(=O)CC + OH --> CC(=O)CCJ + H2O

G3 PES calculations using Variflex including tunneling corrections.

High-pressure limit rate constants of the title reactions have been calculated in the temperature range
of 5002000 K using the Variflex code including Eckart tunneling corrections. Variable reaction coordinate
transition state theory (VRC-TST) has been used for the rate constants of the barrier-less entrance channel.

Chong-Wen Zhou, John M. Simmie and Henry J. Curran
Phys. Chem. Chem. Phys., 2011, 13, 11175-11192
DOI: 10.1039/C0CP02754E
""",
)

entry(
    index = 46,
    label = "C5H10O + OH_r3 <=> C5H9O + H2O_p23",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (2568, 'cm^3/(mol*s)'),
        n = 2.9,
        Ea = (-1.0505, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""John Simmie, G3 calculations. Rate constant per H atom.""",
    longDesc =
u"""
CC(=O)C(C)C + OH --> CJC(=O)C(C)C

G3 PES calculations using Variflex including tunneling corrections.

High-pressure limit rate constants of the title reactions have been calculated in the temperature range
of 5002000 K using the Variflex code including Eckart tunneling corrections. Variable reaction coordinate
transition state theory (VRC-TST) has been used for the rate constants of the barrier-less entrance channel.

Chong-Wen Zhou, John M. Simmie and Henry J. Curran
Phys. Chem. Chem. Phys., 2011, 13, 11175-11192
DOI: 10.1039/C0CP02754E
""",
)

entry(
    index = 47,
    label = "C5H10O-2 + OH_r3 <=> C5H9O-2 + H2O_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4920, 'cm^3/(mol*s)'),
        n = 2.7,
        Ea = (-4.033, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""John Simmie, G3 calculations. Rate constant per H atom.""",
    longDesc =
u"""
CC(=O)C(C)C + OH --> CC(=O)CJ(C)C

G3 PES calculations using Variflex including tunneling corrections.

High-pressure limit rate constants of the title reactions have been calculated in the temperature range
of 5002000 K using the Variflex code including Eckart tunneling corrections. Variable reaction coordinate
transition state theory (VRC-TST) has been used for the rate constants of the barrier-less entrance channel.

Chong-Wen Zhou, John M. Simmie and Henry J. Curran
Phys. Chem. Chem. Phys., 2011, 13, 11175-11192
DOI: 10.1039/C0CP02754E
""",
)

entry(
    index = 48,
    label = "C5H10O-3 + OH_r3 <=> C5H9O-3 + H2O_p23",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (15.54, 'cm^3/(mol*s)'),
        n = 3.54,
        Ea = (-2.907, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""John Simmie, G3 calculations. Rate constant per H atom.""",
    longDesc =
u"""
CC(=O)C(C)C + OH --> CC(=O)C(C)CJ + H2O

G3 PES calculations using Variflex including tunneling corrections.

High-pressure limit rate constants of the title reactions have been calculated in the temperature range
of 5002000 K using the Variflex code including Eckart tunneling corrections. Variable reaction coordinate
transition state theory (VRC-TST) has been used for the rate constants of the barrier-less entrance channel.

Chong-Wen Zhou, John M. Simmie and Henry J. Curran
Phys. Chem. Chem. Phys., 2011, 13, 11175-11192
DOI: 10.1039/C0CP02754E
""",
)

entry(
    index = 49,
    label = "C4H10O-4 + OH_r3 <=> H2O_p23 + C4H9O-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3610, 'cm^3/(mol*s)'),
        n = 2.89,
        Ea = (-2291, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Zador CCSD(T) calc""",
    longDesc =
u"""
Rate comes from quantum calculation by J. Zador at CCSD(T) level
[ This rate was obtained by personal communication as of Sept 2012]
""",
)

entry(
    index = 50,
    label = "CH4_r12 + SH <=> CH3_p1 + H2S",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (469, 'cm^3/(mol*s)'),
        n = 3.02,
        Ea = (66.3, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Glarborg CBS-QB3 calc""",
    longDesc =
u"""
Rate comes from quantum calculation at CBS-QB3 level
J. Phys. Chem. A 2016, 120, 8941-8948; doi: 10.1021/acs.jpca.6b09357
""",
)

entry(
    index = 51,
    label = "C2H6 + SH <=> C2H5b + H2S",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (263, 'cm^3/(mol*s)'),
        n = 3.41,
        Ea = (42.2, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Glarborg CBS-QB3 calc""",
    longDesc =
u"""
Rate comes from quantum calculation at CBS-QB3 level
J. Phys. Chem. A 2016, 120, 8941-8948; doi: 10.1021/acs.jpca.6b09357
""",
)

entry(
    index = 52,
    label = "C3H8b + SH <=> CH2CH2CH3 + H2S",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (512, 'cm^3/(mol*s)'),
        n = 3.39,
        Ea = (43.2, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Glarborg CBS-QB3 calc""",
    longDesc =
u"""
Rate comes from quantum calculation at CBS-QB3 level
J. Phys. Chem. A 2016, 120, 8941-8948; doi: 10.1021/acs.jpca.6b09357
""",
)

entry(
    index = 53,
    label = "C3H8 + SH <=> CH3CHCH3 + H2S",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.16e+06, 'cm^3/(mol*s)'),
        n = 1.79,
        Ea = (34.6, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Glarborg CBS-QB3 calc""",
    longDesc =
u"""
Rate comes from quantum calculation at CBS-QB3 level
J. Phys. Chem. A 2016, 120, 8941-8948; doi: 10.1021/acs.jpca.6b09357
""",
)

entry(
    index = 54,
    label = "C4H10b + SH <=> CH3CHCH2CH3 + H2S",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (19400, 'cm^3/(mol*s)'),
        n = 2.53,
        Ea = (31.3, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Glarborg CBS-QB3 calc""",
    longDesc =
u"""
Rate comes from quantum calculation at CBS-QB3 level
J. Phys. Chem. A 2016, 120, 8941-8948; doi: 10.1021/acs.jpca.6b09357
""",
)

entry(
    index = 55,
    label = "C2H4 + SH <=> CHCH2 + H2S",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (0.178, 'cm^3/(mol*s)'),
        n = 3.31,
        Ea = (81.3, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Glarborg CBS-QB3 calc""",
    longDesc =
u"""
Rate comes from quantum calculation at CBS-QB3 level
J. Phys. Chem. A 2016, 120, 8941-8948; doi: 10.1021/acs.jpca.6b09357
""",
)

entry(
    index = 56,
    label = "C3H6 + SH <=> CH2CHCH2 + H2S",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.2, 'cm^3/(mol*s)'),
        n = 3.79,
        Ea = (9.9, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Glarborg CBS-QB3 calc""",
    longDesc =
u"""
Rate comes from quantum calculation at CBS-QB3 level
J. Phys. Chem. A 2016, 120, 8941-8948; doi: 10.1021/acs.jpca.6b09357
""",
)

entry(
    index = 57,
    label = "C4H8-4 + SH <=> CH2CHCHCH3 + H2S",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (13.2, 'cm^3/(mol*s)'),
        n = 3.4,
        Ea = (0.4, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Glarborg CBS-QB3 calc""",
    longDesc =
u"""
Rate comes from quantum calculation at CBS-QB3 level
J. Phys. Chem. A 2016, 120, 8941-8948; doi: 10.1021/acs.jpca.6b09357
""",
)

entry(
    index = 59,
    label = "C3H4-1 + SH <=> CH2CCH + H2S",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (151, 'cm^3/(mol*s)'),
        n = 3.37,
        Ea = (30.2, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Glarborg CBS-QB3 calc""",
    longDesc =
u"""
Rate comes from quantum calculation at CBS-QB3 level
J. Phys. Chem. A 2016, 120, 8941-8948; doi: 10.1021/acs.jpca.6b09357
""",
)

entry(
    index = 60,
    label = "C4H6 + SH <=> CHCCHCH3 + H2S",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (66.2, 'cm^3/(mol*s)'),
        n = 3.32,
        Ea = (8.01, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Glarborg CBS-QB3 calc""",
    longDesc =
u"""
Rate comes from quantum calculation at CBS-QB3 level
J. Phys. Chem. A 2016, 120, 8941-8948; doi: 10.1021/acs.jpca.6b09357
""",
)

entry(
    index = 61,
    label = "O_rad + HNCN <=> OH_p23 + NCN",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.48e+22, 'cm^3/(mol*s)'),
        n = -3.37,
        Ea = (5429, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Training reaction from kinetics library: primaryNitrogenLibrary""",
    longDesc =
u"""
k8 in S. Xu, M.C. Lin, Proceedings of the Combustion Institute, 2009, 32, 99-106, doi: 10.1016/j.proci.2008.07.011
Done at the CCSD(T)/6-311+G(3df,2p)//CCSD/6-311++G(d,p) level of theory
The paper reports on four pathways to get to the same products, but only one is considered hydrogen abstraction.
""",
)

entry(
    index = 62,
    label = "O2 + HNCN <=> HO2 + NCN",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.61e+08, 'cm^3/(mol*s)'),
        n = 1.25,
        Ea = (24443, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Training reaction from kinetics library: primaryNitrogenLibrary""",
    longDesc =
u"""
k13 in S. Xu, M.C. Lin, Proceedings of the Combustion Institute, 2009, 32, 99-106, doi: 10.1016/j.proci.2008.07.011
Done at the CCSD(T)/6-311+G(3df,2p)//CCSD/6-311++G(d,p) level of theory
The paper reports on two pathways to get to the same products, but only one is considered hydrogen abstraction.
""",
)

entry(
    index = 63,
    label = "N + H2 <=> NH_p23 + H_p",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.6e+14, 'cm^3/(mol*s)'), n=0, Ea=(25138, 'cal/mol'), T0=(1, 'K')),
    rank = 1,
    shortDesc = u"""Training reaction from kinetics library: primaryNitrogenLibrary""",
    longDesc =
u"""
D.F. Davidson, R.K. Hanson, Int. J. Chem. Kin., 1990, 22(8), 843-861, doi: 10.1002/kin.550220805
""",
)

entry(
    index = 64,
    label = "N2H4_r12 + NO <=> N2H3_p1 + HNO_p",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (64.4, 'cm^3/(mol*s)'),
        n = 3.16,
        Ea = (30488, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Training reaction from kinetics library: primaryNitrogenLibrary""",
    longDesc =
u"""
P. Raghunath, Y.H. Lin, M.C. Lin, Computational and Theoretical Chemistry, 2014, 1046, 73-80, doi: 10.1016/j.comptc.2014.07.011
calculations done at the CCSD(T)/CBS//CCSD level of theoty,
and the moment of inertia and harmonic vibrational frequencies were obtained by the CCSD/6-31G(d,p) level
""",
)

entry(
    index = 65,
    label = "HNCN + OH_r3 <=> H2O_p23 + NCN",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (104000, 'cm^3/(mol*s)'),
        n = 2.48,
        Ea = (-1886, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Training reaction from kinetics library: primaryNitrogenLibrary""",
    longDesc =
u"""
k7 in: S. Xu, M.C. Lin, J. Phys. Chem. A, 2007, 111, 6730-6740, doi: 10.1021/jp069038+
Done at the CCSD(T)/6-311+G(3df,2p)//B3LYP/6-311+G(3df,2p) level of theory
""",
)

entry(
    index = 66,
    label = "NH3_r12 + NO <=> NH2_p1 + HNO_p",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.04e+07, 'cm^3/(mol*s)'),
        n = 1.73,
        Ea = (56544, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (5000, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Training reaction from kinetics library: primaryNitrogenLibrary""",
    longDesc =
u"""
A.M. Mebel, E.W.G. Diau, M.C. Lin, K.Morokuma, J. Phys. Chem., 1996, 100, 7517-7525, doi: 10.1021/jp953644f
k1 on p. 7519
calculations done at the UMP2/6-311G-(d,p)//UMP2/6-311G(d,p) level of theory
""",
)

entry(
    index = 67,
    label = "NH2_r3 + H2 <=> NH3_p23 + H_p",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.03e+04, 'cm^3/(mol*s)'), n=2.58163, Ea=(6538, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(300, 'K'), Tmax=(2500, 'K')),
    rank = 1,
    shortDesc = u"""HEAT""",
    longDesc =
u"""
T.L. Nguyen, J.F. Staton, IJCK 2019, doi: 10.1002/kin.21255
calculations done at the HEAT-456QP level of theory
""",
)

entry(
    index = 68,
    label = "NH2_r3 + CH4_r12 <=> NH3_p23 + CH3_p1",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (13600, 'cm^3/(mol*s)'),
        n = 2.87,
        Ea = (10691, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (5000, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Training reaction from kinetics library: primaryNitrogenLibrary""",
    longDesc =
u"""
A.M. Mebel, L.V. Moskaleva, M.C. Lin, J. Molec. Struc. (Theochem), 1999, 461-462, 223-238, doi: 10.1016/S0166-1280(98)00423-0
k2 on p. 232
calculations done at the G2M//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 69,
    label = "NH2_r3 + H2O_r12 <=> NH3_p23 + OH_p1",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.62e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (16846, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (5000, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Training reaction from kinetics library: primaryNitrogenLibrary""",
    longDesc =
u"""
A.M. Mebel, L.V. Moskaleva, M.C. Lin, J. Molec. Struc. (Theochem), 1999, 461-462, 223-238, doi: 10.1016/S0166-1280(98)00423-0
k4 on p. 233
calculations done at the G2M//B3LYP/6-311G(d,p) level of theory
A lower and upper rate limits were given. Here an average rate was taken.
Fitted to a 2 parameter Arrhenius with a coefficient of determination of 0.9943
""",
)

entry(
    index = 70,
    label = "H2S_r + H <=> SH_p1 + H2_p",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.5e+07, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (904, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (190, 'K'),
        Tmax = (2237, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Training reaction from kinetics library: primarySulfurLibrary""",
    longDesc =
u"""
J. Peng, X. Hu, P. Marshall, J. Phys. Chem. A, 1999, 103, 5307-5311, doi: 10.1021/jp984242l
Combined experimental (298-598 K) and computational calculation at the QCISD(T)/6-311+G(3df,2p) level
(also available from D. Woiki, P. Roth, Israel Journal of Chemistry, 1996, 36(3), 279-283, doi: 10.1002/ijch.199600039)
""",
)

entry(
    index = 71,
    label = "H2S_r + S_rad <=> SH_p1 + SH",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.7e+06, 'cm^3/(mol*s)'),
        n = 2.297,
        Ea = (9010, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Training reaction from kinetics library: primarySulfurLibrary""",
    longDesc =
u"""
C.R. Zhou, K. Sendt, B.S. Haynes, J. Phys. Chem. A, 2008, 112, 3239-3247, doi: 10.1021/jp710488d
calculations done at the MRCI/aug-cc-pV(Q+d)Z//MRCI/aug-cc-pVTZ level of theory
""",
)

entry(
    index = 73,
    label = "CH4_r12 + S_rad <=> SH + CH3_p1",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (2.04e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (19910, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (830, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Training reaction from kinetics library: primarySulfurLibrary""",
    longDesc =
u"""
K. Tsuchiya, K. Yamashita, A. Miyoshi, H. Matsui, J. Phys. Chem., 1996, 100(43), 17202-17206, doi: 10.1021/jp961252i
Shock Tube
T > 830 K
""",
)

entry(
    index = 74,
    label = "C2H6 + S_rad <=> SH + C2H5b",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (1.23e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (14750, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (830, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Training reaction from kinetics library: primarySulfurLibrary""",
    longDesc =
u"""
K. Tsuchiya, K. Yamashita, A. Miyoshi, H. Matsui, J. Phys. Chem., 1996, 100(43), 17202-17206, doi: 10.1021/jp961252i
Shock Tube
T > 830 K
""",
)

entry(
    index = 75,
    label = "S_rad + HSS_r12 <=> SH_p1 + S2_p1",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.17e+06, 'cm^3/(mol*s)'),
        n = 2.2,
        Ea = (-600, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (873, 'K'),
        Tmax = (1423, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: primarySulfurLibrary""",
    longDesc =
u"""
K. Sendt, M. Jazbec, B.S. Haynes, Proceedings of the Combustion Institute, 2002, 29, 2439-2446, doi: 10.1016/S1540-7489(02)80297-8
TST
""",
)

entry(
    index = 76,
    label = "HSS_r12 + HSS_r3 <=> HSSH_p23 + S2_p1",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (9.56, 'cm^3/(mol*s)'),
        n = 3.37,
        Ea = (-1672, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (873, 'K'),
        Tmax = (1423, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: primarySulfurLibrary""",
    longDesc =
u"""
K. Sendt, M. Jazbec, B.S. Haynes, Proceedings of the Combustion Institute, 2002, 29, 2439-2446, doi: 10.1016/S1540-7489(02)80297-8
TST
""",
)

entry(
    index = 77,
    label = "HSSH_r12 + H <=> HSS_p1 + H2_p",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (9.56, 'cm^3/(mol*s)'),
        n = 3.37,
        Ea = (-1672, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (873, 'K'),
        Tmax = (1423, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: primarySulfurLibrary""",
    longDesc =
u"""
K. Sendt, M. Jazbec, B.S. Haynes, Proceedings of the Combustion Institute, 2002, 29, 2439-2446, doi: 10.1016/S1540-7489(02)80297-8
TST
""",
)

entry(
    index = 78,
    label = "HSSH_r12 + SH <=> H2S + HSS_p1",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (6400, 'cm^3/(mol*s)'),
        n = 2.98,
        Ea = (-1480, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (873, 'K'),
        Tmax = (1423, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: primarySulfurLibrary""",
    longDesc =
u"""
K. Sendt, M. Jazbec, B.S. Haynes, Proceedings of the Combustion Institute, 2002, 29, 2439-2446, doi: 10.1016/S1540-7489(02)80297-8
TST
""",
)

entry(
    index = 79,
    label = "HSSH_r12 + S_rad <=> HSS_p1 + SH",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (6400, 'cm^3/(mol*s)'),
        n = 2.98,
        Ea = (-1480, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (873, 'K'),
        Tmax = (1423, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: primarySulfurLibrary""",
    longDesc =
u"""
K. Sendt, M. Jazbec, B.S. Haynes, Proceedings of the Combustion Institute, 2002, 29, 2439-2446, doi: 10.1016/S1540-7489(02)80297-8
TST
""",
)

entry(
    index = 80,
    label = "HONO_r + H <=> H2_p + NO2_p",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.01e+08, 'cm^3/(mol*s)'),
        n = 1.55,
        Ea = (6614, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (3500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Training reaction from kinetics library: primaryNitrogenLibrary""",
    longDesc =
u"""
C.C. Hsu, M.C. Lin, A.M. Mebel, C.F. Melius, J. Phys. Chem. A, 1997, 101(1), 60-66, doi: 10.1021/jp962286t
G2 and BAC-MP4
""",
)

entry(
    index = 81,
    label = "HNO_r + H <=> NO_p + H2_p",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.46e+11, 'cm^3/(mol*s)'),
        n = 0.72,
        Ea = (655, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Training reaction from kinetics library: primaryNitrogenLibrary""",
    longDesc =
u"""
M.R. Soto, M. Page, J. Chem. Phys., 1992, 97, 7287, doi: 10.1063/1.463501
calculations done at the CASSCF//(CASSCF and CISD) levels of theory
""",
)

entry(
    index = 82,
    label = "HNO3_r + H <=> H2_p + NO3_p",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.56e+08, 'cm^3/(mol*s)'),
        n = 1.53,
        Ea = (16400, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Training reaction from kinetics library: primaryNitrogenLibrary""",
    longDesc =
u"""
J.W. Boughton, S. Kristyan, M.C. Lin, Chemical Physics, 1997, 214(2-3), 219-227, doi: 10.1016/S0301-0104(96)00313-8
CTST
""",
)

entry(
    index = 83,
    label = "HCO_r3 + HNO_r <=> CH2O_p + NO_p",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.583, 'cm^3/(mol*s)'),
        n = 3.84,
        Ea = (115, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Training reaction from kinetics library: primaryNitrogenLibrary""",
    longDesc =
u"""
Z.F. Xu, M.C. Lin, Int. J. Chem. Kin., 2004, 36(4), 205-215, doi: 10.1002/kin.10178
calculations done at the G2M//BH&HLYP/6-311G(d, p) level of theory
""",
)

entry(
    index = 84,
    label = "CH2O + NO2 <=> CHO_p1 + HONO_p",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (1.42e-07, 'cm^3/(mol*s)'),
        n = 5.64,
        Ea = (9221, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Training reaction from kinetics library: primaryNitrogenLibrary""",
    longDesc =
u"""
Z.F. Xu, M.C. Lin, Int. J. Chem. Kin., 2003, 35(5), 184-190, doi: 10.1002/kin.10115
calculations done at the G2M//B3LYP/6-311+G(d,p) and G2M//MPW1PW91/6-311+G(3df,2p) levels of theory
* There are two other pathways for the formation of these products, this is the fastest one. k_tot was also given in the paper.
""",
)

entry(
    index = 85,
    label = "HNO3_r + OH_r3 <=> H2O_p23 + NO3_p",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.73, 'cm^3/(mol*s)'),
        n = 3.5,
        Ea = (-1667, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (750, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Training reaction from kinetics library: primaryNitrogenLibrary""",
    longDesc =
u"""
W.S. Xia, M.C. Lin, J. Chem. Phys., 2001, 114, 4522-4532, doi: 10.1063/1.1337061
calculations done at the B3LYP/6-311G(d,p)//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 86,
    label = "HCN_r + O_rad <=> CN_p + OH_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2e+08, 'cm^3/(mol*s)'),
        n = 1.47,
        Ea = (7550, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (575, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Training reaction from kinetics library: primaryNitrogenLibrary""",
    longDesc =
u"""
W. Tsang, J.T. Herron, Journal of Physical and Chemical Reference Data, 1991, 20, 609, doi: 10.1063/1.555890
Review and reccomendation, based on 5 different experimental studies
""",
)

entry(
    index = 87,
    label = "HCN_r + H <=> CN_p + H2_p",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.8e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (24600, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Training reaction from kinetics library: primaryNitrogenLibrary""",
    longDesc =
u"""
W. Tsang, J.T. Herron, Journal of Physical and Chemical Reference Data, 1991, 20, 609, doi: 10.1063/1.555890
Review and reccomendation, based on experimental studies
""",
)

entry(
    index = 88,
    label = "HCN_r + OH_r3 <=> CN_p + H2O_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.8e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (24600, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2840, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Training reaction from kinetics library: primaryNitrogenLibrary""",
    longDesc =
u"""
W. Tsang, J.T. Herron, Journal of Physical and Chemical Reference Data, 1991, 20, 609, doi: 10.1063/1.555890
Review and reccomendation, based on experimental studies
""",
)

entry(
    index = 89,
    label = "CH3SH_r1 + H <=> CH3S_p + H2_p",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.39e+08, 'cm^3/(mol*s)'),
        n = 1.729,
        Ea = (986, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (250, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Training reaction from kinetics library: primarySulfurLibrary""",
    longDesc =
u"""
WK.E. Kerr, I.M. Alecu, K.M. Thompson, Y. Gao, P. Marshall, J. Phys. CHem. A, 2015, 119, 7352-7360, doi: 10.1021/jp512966a
Table 5, R1
calculations done at the QCISD/6-311G(d,p) level
""",
)

entry(
    index = 90,
    label = "CH3SH_r2 + H <=> CH2SH_p + H2_p",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (4160, 'cm^3/(mol*s)'),
        n = 2.925,
        Ea = (4747, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (250, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Training reaction from kinetics library: primarySulfurLibrary""",
    longDesc =
u"""
WK.E. Kerr, I.M. Alecu, K.M. Thompson, Y. Gao, P. Marshall, J. Phys. CHem. A, 2015, 119, 7352-7360, doi: 10.1021/jp512966a
Table 5, R2
calculations done at the QCISD/6-311G(d,p) level
""",
)

entry(
    index = 91,
    label = "NH2_r3 + C2H6 <=> NH3_p23 + C2H5b",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (3.46e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (13800, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3""",
    longDesc =
u"""
(R2) in:
K. Siddique, M. Altarawneh, J. Gore, P.R. Westmoreland, B.Z. Dlugogorski, J. Chem. Phys. A 2017, 121, 3332-2231,
doi: 10.1021/acs.jpca.6b12890
""",
)

entry(
    index = 92,
    label = "NH2_r3 + C3H8b <=> NH3_p23 + CH2CH2CH3",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (1.37e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (10000, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3""",
    longDesc =
u"""
(R3a) in:
K. Siddique, M. Altarawneh, J. Gore, P.R. Westmoreland, B.Z. Dlugogorski, J. Chem. Phys. A 2017, 121, 3332-2231,
doi: 10.1021/acs.jpca.6b12890
""",
)

entry(
    index = 93,
    label = "NH2_r3 + C3H8 <=> NH3_p23 + CH3CHCH3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.48e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8533, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3""",
    longDesc =
u"""
(R3b) in:
K. Siddique, M. Altarawneh, J. Gore, P.R. Westmoreland, B.Z. Dlugogorski, J. Chem. Phys. A 2017, 121, 3332-2231,
doi: 10.1021/acs.jpca.6b12890
""",
)

entry(
    index = 94,
    label = "NH2_r3 + C4H10 <=> NH3_p23 + pC4H9",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (2.11e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (9870, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3""",
    longDesc =
u"""
(R4a) in:
K. Siddique, M. Altarawneh, J. Gore, P.R. Westmoreland, B.Z. Dlugogorski, J. Chem. Phys. A 2017, 121, 3332-2231,
doi: 10.1021/acs.jpca.6b12890
""",
)

entry(
    index = 95,
    label = "NH2_r3 + C4H10b <=> NH3_p23 + CH3CHCH2CH3",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (1.72e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7770, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3""",
    longDesc =
u"""
(R4b) in:
K. Siddique, M. Altarawneh, J. Gore, P.R. Westmoreland, B.Z. Dlugogorski, J. Chem. Phys. A 2017, 121, 3332-2231,
doi: 10.1021/acs.jpca.6b12890
""",
)

entry(
    index = 96,
    label = "NH2_r3 + iC4H10 <=> NH3_p23 + ipC4H9",
    degeneracy = 9.0,
    kinetics = Arrhenius(
        A = (1.84e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (10100, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3""",
    longDesc =
u"""
(R5a) in:
K. Siddique, M. Altarawneh, J. Gore, P.R. Westmoreland, B.Z. Dlugogorski, J. Chem. Phys. A 2017, 121, 3332-2231,
doi: 10.1021/acs.jpca.6b12890
""",
)

entry(
    index = 97,
    label = "NH2_r3 + iC4H10b <=> NH3_p23 + tC4H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.35e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6450, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3""",
    longDesc =
u"""
(R5b) in:
K. Siddique, M. Altarawneh, J. Gore, P.R. Westmoreland, B.Z. Dlugogorski, J. Chem. Phys. A 2017, 121, 3332-2231,
doi: 10.1021/acs.jpca.6b12890
""",
)

entry(
    index = 98,
    label = "NH2_r3 + C5H12 <=> NH3_p23 + tC5H11",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.76e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6450, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3""",
    longDesc =
u"""
(R6) in:
K. Siddique, M. Altarawneh, J. Gore, P.R. Westmoreland, B.Z. Dlugogorski, J. Chem. Phys. A 2017, 121, 3332-2231,
doi: 10.1021/acs.jpca.6b12890
""",
)

entry(
    index = 99,
    label = "NH2_r3 + C3H6-3 <=> NH3_p23 + vC3H5",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.42e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11900, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3""",
    longDesc =
u"""
(R7a) in:
K. Siddique, M. Altarawneh, J. Gore, P.R. Westmoreland, B.Z. Dlugogorski, J. Chem. Phys. A 2017, 121, 3332-2231,
doi: 10.1021/acs.jpca.6b12890
""",
)

entry(
    index = 100,
    label = "NH2_r3 + C3H6 <=> NH3_p23 + CH2CHCH2",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6670, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3""",
    longDesc =
u"""
(R7b) in:
K. Siddique, M. Altarawneh, J. Gore, P.R. Westmoreland, B.Z. Dlugogorski, J. Chem. Phys. A 2017, 121, 3332-2231,
doi: 10.1021/acs.jpca.6b12890
""",
)

entry(
    index = 101,
    label = "NH2_r3 + C4H8-7 <=> NH3_p23 + pC4H7",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (4.33e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8700, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3""",
    longDesc =
u"""
(R8) in:
K. Siddique, M. Altarawneh, J. Gore, P.R. Westmoreland, B.Z. Dlugogorski, J. Chem. Phys. A 2017, 121, 3332-2231,
doi: 10.1021/acs.jpca.6b12890
""",
)

entry(
    index = 102,
    label = "NH2_r3 + C4H8-2 <=> NH3_p23 + aC4H7",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (1.37e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8010, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3""",
    longDesc =
u"""
(R9) in:
K. Siddique, M. Altarawneh, J. Gore, P.R. Westmoreland, B.Z. Dlugogorski, J. Chem. Phys. A 2017, 121, 3332-2231,
doi: 10.1021/acs.jpca.6b12890
""",
)

entry(
    index = 103,
    label = "NH2_r3 + C5H10-1 <=> NH3_p23 + C5H9-1",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (6.14e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5810, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3""",
    longDesc =
u"""
(R10) in:
K. Siddique, M. Altarawneh, J. Gore, P.R. Westmoreland, B.Z. Dlugogorski, J. Chem. Phys. A 2017, 121, 3332-2231,
doi: 10.1021/acs.jpca.6b12890
""",
)

entry(
    index = 104,
    label = "NH2_r3 + C5H10-2 <=> NH3_p23 + C5H9-2",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (1.54e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (9570, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3""",
    longDesc =
u"""
(R11a) in:
K. Siddique, M. Altarawneh, J. Gore, P.R. Westmoreland, B.Z. Dlugogorski, J. Chem. Phys. A 2017, 121, 3332-2231,
doi: 10.1021/acs.jpca.6b12890
""",
)

entry(
    index = 105,
    label = "NH2_r3 + C5H10-3 <=> NH3_p23 + C5H9-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.87e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5400, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3""",
    longDesc =
u"""
(R11b) in:
K. Siddique, M. Altarawneh, J. Gore, P.R. Westmoreland, B.Z. Dlugogorski, J. Chem. Phys. A 2017, 121, 3332-2231,
doi: 10.1021/acs.jpca.6b12890
""",
)

entry(
    index = 106,
    label = "NH2_r3 + C5H10-4 <=> NH3_p23 + C5H9-4",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (1.13e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7720, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3""",
    longDesc =
u"""
(R13) in:
K. Siddique, M. Altarawneh, J. Gore, P.R. Westmoreland, B.Z. Dlugogorski, J. Chem. Phys. A 2017, 121, 3332-2231,
doi: 10.1021/acs.jpca.6b12890
""",
)

entry(
    index = 107,
    label = "NH2_r3 + C2H4 <=> NH3_p23 + CHCH2",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (1.56e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (13410, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3""",
    longDesc =
u"""
(R12) in:
K. Siddique, M. Altarawneh, J. Gore, P.R. Westmoreland, B.Z. Dlugogorski, J. Chem. Phys. A 2017, 121, 3332-2231,
doi: 10.1021/acs.jpca.6b12890
""",
)

entry(
    index = 108,
    label = "NH2_r3 + C4H6 <=> NH3_p23 + CHCCHCH3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.62e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5975, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3""",
    longDesc =
u"""
(R14) in:
K. Siddique, M. Altarawneh, J. Gore, P.R. Westmoreland, B.Z. Dlugogorski, J. Chem. Phys. A 2017, 121, 3332-2231,
doi: 10.1021/acs.jpca.6b12890
""",
)

entry(
    index = 109,
    label = "NH2_r3 + C4H6-2 <=> NH3_p23 + C4H5-2",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (9.94e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8510, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3""",
    longDesc =
u"""
(R15) in:
K. Siddique, M. Altarawneh, J. Gore, P.R. Westmoreland, B.Z. Dlugogorski, J. Chem. Phys. A 2017, 121, 3332-2231,
doi: 10.1021/acs.jpca.6b12890
""",
)

entry(
    index = 110,
    label = "NH2_r3 + C5H8 <=> NH3_p23 + C5H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.67e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3270, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3""",
    longDesc =
u"""
(R16) in:
K. Siddique, M. Altarawneh, J. Gore, P.R. Westmoreland, B.Z. Dlugogorski, J. Chem. Phys. A 2017, 121, 3332-2231,
doi: 10.1021/acs.jpca.6b12890
""",
)

entry(
    index = 111,
    label = "CH3CH2NH2_1 + H <=> CH2CH2NH2 + H2",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8174, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: Ethylamine""",
    longDesc =
u"""
CBS-QB3
doi: 10.1016/j.combustflame.2015.10.032
""",
)

entry(
    index = 112,
    label = "CH3CH2NH2_2 + H <=> CH3CHNH2 + H2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.16e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3585, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: Ethylamine""",
    longDesc =
u"""
CBS-QB3
doi: 10.1016/j.combustflame.2015.10.032
""",
)

entry(
    index = 113,
    label = "CH3CH2NH2_3 + H <=> CH3CH2NH + H2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (5.47e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6907, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: Ethylamine""",
    longDesc =
u"""
CBS-QB3
doi: 10.1016/j.combustflame.2015.10.032
""",
)

entry(
    index = 114,
    label = "CH3CH2NH2_1 + CH3_r3 <=> CH2CH2NH2 + CH4_p23",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (6e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (12620, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: Ethylamine""",
    longDesc =
u"""
CBS-QB3
doi: 10.1016/j.combustflame.2015.10.032
""",
)

entry(
    index = 115,
    label = "CH3CH2NH2_2 + CH3_r3 <=> CH3CHNH2 + CH4_p23",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.23e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7911, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: Ethylamine""",
    longDesc =
u"""
CBS-QB3
doi: 10.1016/j.combustflame.2015.10.032
""",
)

entry(
    index = 116,
    label = "CH3CH2NH2_3 + CH3_r3 <=> CH3CH2NH + CH4_p23",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.23e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (9441, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: Ethylamine""",
    longDesc =
u"""
CBS-QB3
doi: 10.1016/j.combustflame.2015.10.032
""",
)

entry(
    index = 117,
    label = "CH3CH2NH2_1 + NH2_r3 <=> CH2CH2NH2 + NH3_p23",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (9.21e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (9393, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: Ethylamine""",
    longDesc =
u"""
CBS-QB3
doi: 10.1016/j.combustflame.2015.10.032
""",
)

entry(
    index = 118,
    label = "CH3CH2NH2_2 + NH2_r3 <=> CH3CHNH2 + NH3_p23",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (8.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4493, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: Ethylamine""",
    longDesc =
u"""
CBS-QB3
doi: 10.1016/j.combustflame.2015.10.032
""",
)

entry(
    index = 119,
    label = "CH3CH2NH2_3 + NH2_r3 <=> CH3CH2NH + NH3_p23",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.14e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5927, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: Ethylamine""",
    longDesc =
u"""
CBS-QB3
doi: 10.1016/j.combustflame.2015.10.032
""",
)

entry(
    index = 120,
    label = "CH3CH2NH2_1 + OH_r3 <=> CH2CH2NH2 + H2O_p23",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (794, 'cm^3/(mol*s)'),
        n = 2.97,
        Ea = (-1040, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""VTST CCSD(T)/6-311++g(2d,2p)""",
    longDesc =
u"""
S. Li, E. Dames, D.F. Davidson, R.K. Hanson
"High-Temperature Measurements of the Reactions of OH with Ethylamine and Dimethylamine"
The Journal of Physical Chemistry A, 2014, 118, 70-77
doi: 10.1021/jp411141w
(with geometries from http://dx.doi.org/10.1021/ct7002786 CCSD(T)/6-311++G(2d,2p) single-point calculations)
""",
)

entry(
    index = 121,
    label = "CH3CH2NH2_2 + OH_r3 <=> CH3CHNH2 + H2O_p23",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (328000, 'cm^3/(mol*s)'),
        n = 2.24,
        Ea = (-3040, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""VTST CCSD(T)/6-311++g(2d,2p)""",
    longDesc =
u"""
S. Li, E. Dames, D.F. Davidson, R.K. Hanson
"High-Temperature Measurements of the Reactions of OH with Ethylamine and Dimethylamine"
The Journal of Physical Chemistry A, 2014, 118, 70-77
doi: 10.1021/jp411141w
(with geometries from http://dx.doi.org/10.1021/ct7002786 CCSD(T)/6-311++G(2d,2p) single-point calculations)
""",
)

entry(
    index = 122,
    label = "CH3CH2NH2_3 + OH_r3 <=> CH3CH2NH + H2O_p23",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (112000, 'cm^3/(mol*s)'),
        n = 2.36,
        Ea = (-2860, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""VTST CCSD(T)/6-311++g(2d,2p)""",
    longDesc =
u"""
S. Li, E. Dames, D.F. Davidson, R.K. Hanson
"High-Temperature Measurements of the Reactions of OH with Ethylamine and Dimethylamine"
The Journal of Physical Chemistry A, 2014, 118, 70-77
doi: 10.1021/jp411141w
(with geometries from http://dx.doi.org/10.1021/ct7002786 CCSD(T)/6-311++G(2d,2p) single-point calculations)
""",
)

entry(
    index = 123,
    label = "N2H4_r12 + H <=> N2H3_p1 + H2",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (1.48e+08, 'cm^3/(mol*s)'),
        n = 1.69,
        Ea = (4000, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: Ethylamine""",
    longDesc =
u"""
CBS-QB3
""",
)

entry(
    index = 124,
    label = "N2H4_r12 + CH3_r3 <=> N2H3_p1 + CH4_p23",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (17.7, 'cm^3/(mol*s)'),
        n = 3.6,
        Ea = (3500, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: Ethylamine""",
    longDesc =
u"""
CBS-QB3
""",
)

entry(
    index = 125,
    label = "N2H4_r12 + NH2_r3 <=> N2H3_p1 + NH3_p23",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (2590, 'cm^3/(mol*s)'),
        n = 2.83,
        Ea = (700, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: Ethylamine""",
    longDesc =
u"""
CBS-QB3
""",
)

entry(
    index = 126,
    label = "CH3CHNH_1 + H <=> CH2CHNH + H2",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (39800, 'cm^3/(mol*s)'),
        n = 2.76,
        Ea = (4400, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: Ethylamine""",
    longDesc =
u"""
CBS-QB3
""",
)

entry(
    index = 127,
    label = "CH3CHNH_2 + H <=> CH3CHN + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.19e+07, 'cm^3/(mol*s)'),
        n = 1.96,
        Ea = (2400, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: Ethylamine""",
    longDesc =
u"""
CBS-QB3
""",
)

entry(
    index = 128,
    label = "NH_r3 + CH4_r12 <=> NH2_p23 + CH3_p1",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (9e+13, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (84, 'kJ/mol', '+|-', 5),
        T0 = (1, 'K'),
        Tmin = (1150, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Wagner""",
    longDesc =
u"""
Experimental measurements

Michael Rohrig and Heinz Georg Wagner
A kinetic study about the reactions of NH(X3\Sigma-) with hydrocarbons part 1: Saturated hydrocarbons and acetaldehyde
Berichte der Bunsengesellschaft fur physikalische Chemie Volume 98, Issue 6, pages 858-863, June 1994
DOI: 10.1002/bbpc.19940980615
""",
)

entry(
    index = 129,
    label = "NH_r3 + C2H6 <=> NH2_p23 + C2H5b",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (7e+13, 'cm^3/(mol*s)', '*|/', 1.75),
        n = 0,
        Ea = (70, 'kJ/mol', '+|-', 5),
        T0 = (1, 'K'),
        Tmin = (1150, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Wagner""",
    longDesc =
u"""
Experimental measurements

Michael Rohrig and Heinz Georg Wagner
A kinetic study about the reactions of NH(X3\Sigma-) with hydrocarbons part 1: Saturated hydrocarbons and acetaldehyde
Berichte der Bunsengesellschaft fur physikalische Chemie Volume 98, Issue 6, pages 858-863, June 1994
DOI: 10.1002/bbpc.19940980615
""",
)

entry(
    index = 131,
    label = "Cl + CH4_r12 <=> HCl + CH3_p1",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (1.36534e-19, 'cm^3/(molecule*s)'),
        n = 2.6,
        Ea = (3201.07, 'J/mol'),
        T0 = (1, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Cl + CH4 <=> HCl + CH3""",
    longDesc =
u"""
Kinetics of Cl atom reactions with methane, ethane, and propane from 292 to 800 K
J. S. Pilgrim, A. McIlroy, and C. A. Taatjes, J. Phys. Chem. A 101, 1873 (1997)
PLP-LIF Measurement from 292-800 K
""",
)

entry(
    index = 132,
    label = "Cl + C2H6 <=> HCl + C2H5",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (7.23e-13, 'cm^3/(molecule*s)'),
        n = 0.7,
        Ea = (-972.793, 'J/mol'),
        T0 = (1, 'K'),
        Tmin = (200.0,'K'),
        Tmax = (1000.0, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Cl + C2H6 <=> HCl + C2H5""",
    longDesc =
u"""
Kinetics of Reactions of Cl Atoms with Ethane, Chloroethane, and 1,1-Dichloroethane
Bryukov, M. G., Slagle, I. R., and Knyazev, V. D.: J. Phys. Chem. A., 107, 6565, 2003.
Fit to multiple experimental measurements from 200-1000 K, including PLP experiments of 1997 Pilgrim
""",
)

entry(
    index = 133,
    label = "Cl + C3H8b <=> HCl + C3H7-2",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (8.26e-11, 'cm^3/(molecule*s)'),
        n = 0,
        Ea = (748.302, 'J/mol'),
        T0 = (1, 'K'),
        Tmin = (200.0, 'K'),
        Tmax = (700.0, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Cl + C3H8 <=> HCl + nC3H7""",
    longDesc =
u"""
IUPAC recommendation: http://iupac.pole-ether.fr
from 200-700 K
""",
)

entry(
    index = 134,
    label = "Cl + C3H8 <=> HCl + C3H7",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (6.02e-11, 'cm^3/(molecule*s)'),
        n = 0,
        Ea = (-623.585, 'J/mol'),
        T0 = (1, 'K'),
        Tmin = (200.0, 'K'),
        Tmax = (700.0, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Cl + C3H8 <=> HCl + iC3H7""",
    longDesc =
u"""
IUPAC recommendation: http://iupac.pole-ether.fr
from 200-700 K
""",
)

entry(
    index = 141,
    label = "Cl + CH4O-2 <=> HCl + CH3O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.65431e-19, 'cm^3/(molecule*s)'),
        n = 2.5,
        Ea = (30470, 'J/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Cl + CH3OH <=> HCl + CH3O""",
    longDesc =
u"""
Theoretical study of the kinetics of the hydrogen abstraction from methanol. 2. Reaction of methanol with chlorine and bromine atoms
Jodkowski, J.T.; Rayez, M-T.; Rayez, J-C.; Berces, T.; Dobe, S., JPCA, 102, 9230-9243, 1998
300-1000 K, Theoretical Predictions
""",
)

entry(
    index = 143,
    label = "Cl + C2H6O-2 <=> HCl + C2H5O-2",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.13e-13, 'cm^3/(molecule*s)'),
        n = 0.7494,
        Ea = (-374.151, 'J/mol'),
        T0 = (1, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Cl + C2H5OH <=> HCl + CH2CH2OH""",
    longDesc =
u"""
Absolute and Site-Specific Abstraction Rate Coefficients for Reactions of Cl with CH3CH2 OH, CH3CD2OH, and CD3CH2OH Between 295 and 600 K
Taatjes, C. A., Christensen, L. K., Hurley M. D. and Wallington, T. J.: J. Phys. Chem. A, 103, 9805, 1999.
LP-IR experiments from 295-600 K
""",
)

entry(
    index = 144,
    label = "Cl + H2O_r12 <=> HCl + OH_p1",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.79e-11, 'cm^3/(molecule*s)'),
        n = 0,
        Ea = (72086.5, 'J/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Cl + H2O <=> HCl + OH""",
    longDesc =
u"""
Evaluated kinetic data for high temperature reactions. Volume 4 Homogeneous gas phase reactions of halogen- and cyanide- containing species
Baulch, D.L.; Duxbury, J.; Grant, S.J.; Montague, D.C., J. Phys. Chem. Ref. Data, 10, 1981.
210-500 K
""",
)

entry(
    index = 145,
    label = "Cl + H2O2 <=> HCl + HO2_r3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.1e-11, 'cm^3/(molecule*s)'),
        n = 0,
        Ea = (8148.18, 'J/mol'),
        T0 = (1, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Cl + H2O2 <=> HCl + HO2""",
    longDesc =
u"""
Evaluated kinetic and photochemical data for atmospheric chemistry: Volume III - gas phase reactions of inorganic halogens
Atkinson, R.;Baulch, D.L.;Cox, R.A.;Crowley, J.N.;Hampson, R.F.;Hynes, R.G.;Jenkin, M.E.;Rossi, M.J.;Troe, J., Atmos. Chem. Phys., 7, 981-1191, 2007
260-430 K
""",
)

entry(
    index = 146,
    label = "Cl + H2 <=> HCl + H",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (4.59e-16, 'cm^3/(molecule*s)'),
        n = 1.588,
        Ea = (13984.9, 'J/mol'),
        T0 = (1, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Cl + H2 <=> HCl + H""",
    longDesc =
u"""
Thermal rate constants for the Cl+H2 and Cl+D2 reactions between 296 and 3000 K
Kumaran, S.S.; Lim, K.P.; Michael, J.V., J. Chem. Phys., 101, 9487 - 9498, 1994
200-2950 K, from fit to experimental data
""",
)

entry(
    index = 147,
    label = "Cl + C5H10O2 <=> HCl + C5H9O2",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.24e-11, 'cm^3/(molecule*s)'),
        n = 0,
        Ea = (2500.16, 'J/mol'),
        T0 = (1, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Cl + C4H9OCHO <=> HCl + C4H8OCHO-1""",
    longDesc =
u"""
Free-radical substitution in aliphatic compounds. Part XIV. The halogenation of esters of butan-1-ol
Singh, H.; Tedder, J.M., J. Chem. Soc. B, 1966
212-423 K, experimental measurement
""",
)

entry(
    index = 148,
    label = "Cl + C5H10O2-2 <=> HCl + C5H9O2-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.32e-11, 'cm^3/(molecule*s)'),
        n = 0,
        Ea = (1255.2, 'J/mol'),
        T0 = (1, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Cl + C4H9OCHO <=> HCl + C4H8OCHO-2""",
    longDesc =
u"""
Free-radical substitution in aliphatic compounds. Part XIV. The halogenation of esters of butan-1-ol
Singh, H.; Tedder, J.M., J. Chem. Soc. B, 1966
212-423 K, experimental measurement
""",
)

entry(
    index = 149,
    label = "Cl + C5H10O2-3 <=> HCl + C5H9O2-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.05e-11, 'cm^3/(molecule*s)'),
        n = 0,
        Ea = (1249.67, 'J/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Cl + C4H9OCHO <=> HCl + C4H8OCHO-3""",
    longDesc =
u"""
Free-radical substitution in aliphatic compounds. Part XIV. The halogenation of esters of butan-1-ol
Singh, H.; Tedder, J.M., J. Chem. Soc. B, 1966
212-423 K, experimental measurement
""",
)

entry(
    index = 151,
    label = "Cl + C3H4-1 <=> HCl + C3H3",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (1.40759e-16, 'cm^3/(molecule*s)'),
        n = 2,
        Ea = (4400.02, 'J/mol'),
        T0 = (1, 'K'),
        Tmin = (292.0, 'K'),
        Tmax = (850.0, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Cl + aC3H4 <=> HCl + C3H3""",
    longDesc =
u"""
Infrared frequency-modulation probing of Cl + C3H4 (allene, propyne) reactions: kinetics of HCl production from 292 to 850 K
Farrell, J.T.; Taatjes, C.A., J. Phys. Chem. A, 102, 1998, 4846-4856
292-850 K, experimental measurement
""",
)

entry(
    index = 160,
    label = "Cl + C3H6 <=> HCl + C3H5",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (4.9e-11, 'cm^3/(molecule*s)'),
        n = 0,
        Ea = (748.302, 'J/mol'),
        T0 = (1, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Cl + C3H6 <=> HCl + aC3H5""",
    longDesc =
u"""
Infrared absorption probing of the Cl + C3H6 reaction: rate coefficients for HCl production between 290 and 800 K
Pilgrim, J.S.; Taatjes, C.A., JPCA, 101, 5776-5782, 1997
293-800 K, experimental measurement
""",
)

entry(
    index = 167,
    label = "Cl + iC4H10b <=> HCl + C4H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.82e-11, 'cm^3/(molecule*s)'),
        n = 0,
        Ea = (79.8189, 'J/mol'),
        T0 = (1, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Cl + iC4H10 <=> HCl + tC4H9""",
    longDesc =
u"""
Competitive chlorination reactions in the gas phase: hydrogen and C1-C5 saturated hydrocarbons
Knox, J.H.; Nelson, R.L., Trans. Faraday Soc., 55, 1959
193-593 K, experimental measurement
""",
)

entry(
    index = 168,
    label = "Cl + C3H6-4 <=> HCl + C3H5-3",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (8.97e-11, 'cm^3/(molecule*s)'),
        n = 0,
        Ea = (17289.9, 'J/mol'),
        T0 = (1, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Cl + cC3H6 <=> HCl + cC3H5""",
    longDesc =
u"""
Competitive chlorination reactions in the gas phase: hydrogen and C1-C5 saturated hydrocarbons
Knox, J.H.; Nelson, R.L., Trans. Faraday Soc., 55, 1959
193-593 K, experimental measurement
""",
)

entry(
    index = 169,
    label = "Cl + C3H4 <=> HCl + C3H3-2",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.41e-17, 'cm^3/(molecule*s)'),
        n = 2,
        Ea = (4159.73, 'J/mol'),
        T0 = (1, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Cl + pC3H4 <=> HCl + C3H3""",
    longDesc =
u"""
Infrared frequency-modulation probing of Cl + C3H4 (allene, propyne) reactions: kinetics of HCl production from 292 to 850 K
Farrell, J.T.; Taatjes, C.A., J. Phys. Chem. A, 102, 1998, 4846-4856
292-850 K, experimental measurement
""",
)

entry(
    index = 170,
    label = "Cl + C2H4 <=> HCl + C2H3",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (6.19e-11, 'cm^3/(molecule*s)'),
        n = 0,
        Ea = (28269.2, 'J/mol'),
        T0 = (1, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Cl + Ethene <=> HCl + C2H3""",
    longDesc =
u"""
Infrared absorption probing of the Cl + Ethene reaction: direct measurement of Arrhenius parameters for hydrogen abstraction
Pilgrim, J.S.; Taatjes, C.A., J. Phys. Chem. A, 101, 1997, 4172-4177
500-800 K, experimental measurement
""",
)

entry(
    index = 171,
    label = "Cl + C6H6 <=> HCl + C6H5",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (6.1e-11, 'cm^3/(molecule*s)'),
        n = 0,
        Ea = (31600, 'J/mol'),
        T0 = (1, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Cl + C6H6 <=> HCl + C6H5""",
    longDesc =
u"""
Studies of the kinetics and thermochemistry of the forward and reverse reaction Cl+C6H6=HCl+C6H5
Alecu, I.M.; Gao, Y.D.; Hsieh, P.C.; Sand, J.P.; Ors, A.; McLeod, A.; Marshall, P., JPCA, 111, 3970-3976, 2007
296-922 K, experimental measurement
""",
)

entry(
    index = 174,
    label = "C3H6-3 + C6H5 <=> C6H6 + C3H5-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.00551, 'cm^3/(mol*s)'),
        n = 4.401,
        Ea = (4.745, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Buras_C6H5_C3H6_highP""",
    longDesc =
u"""
Taken from entry: C6H5 + C3H6 <=> C6H6 + CH3CHCH
""",
)

entry(
    index = 175,
    label = "C3H6-2 + C6H5 <=> C6H6 + C3H5-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.06725, 'cm^3/(mol*s)'),
        n = 4.149,
        Ea = (3.361, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Buras_C6H5_C3H6_highP""",
    longDesc =
u"""
Taken from entry: C6H5 + C3H6 <=> C6H6 + CH3CCH2
""",
)

entry(
    index = 176,
    label = "C3H6 + C6H5 <=> C6H6 + C3H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.2601, 'cm^3/(mol*s)'),
        n = 4.002,
        Ea = (1.735, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Buras_C6H5_C3H6_highP""",
    longDesc =
u"""
Taken from entry: C6H5 + C3H6 <=> C6H6 + CH2CHCH2
""",
)

entry(
    index = 177,
    label = "C4H6-3 + C2H3 <=> C2H4 + C4H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.0003437, 'cm^3/(mol*s)'),
        n = 4.732,
        Ea = (6.579, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: 2015_Buras_C2H3_C4H6_highP""",
    longDesc =
u"""
Taken from entry: C2H3 + C4H6 <=> C2H4 + nC4H5
""",
)

entry(
    index = 178,
    label = "C4H6-4 + C2H3 <=> C2H4 + C4H5-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.000621, 'cm^3/(mol*s)'),
        n = 4.814,
        Ea = (4.902, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: 2015_Buras_C2H3_C4H6_highP""",
    longDesc =
u"""
Taken from entry: C2H3 + C4H6 <=> C2H4 + iC4H5
""",
)

entry(
    index = 179,
    label = "C4H6-4 + C6H5 <=> C6H6 + C4H5-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8710, 'cm^3/(mol*s)'), n=3.12, Ea=(8.1, 'kJ/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2005_Ismail_C6H5_C4H6_highP""",
    longDesc =
u"""
Taken from entry: phenyl + 1_3_butadiene <=> benzene + 1_3_butadien_2_yl
""",
)

entry(
    index = 182,
    label = "C7H8 + H <=> H2 + C7H7",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (75372.2, 'cm^3/(mol*s)'),
        n = 2.57378,
        Ea = (3145.75, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['Li, S.-H.', 'Guo, J.-J.', 'Li, R.', 'Wang, F.', 'Li, X.-Y.'],
        title = 'Theoretical Prediction of Rate Constants for Hydrogen Abstraction by OH, H, O, CH3, and HO2 Radicals from Toluene',
        journal = 'The Journal of Physical Chemistry A',
        volume = '120 (20)',
        pages = '3424-3432',
        year = '2016',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc =
u"""
G4//B3LYP/6-31G(2df,p)
""",
)

entry(
    index = 183,
    label = "C7H8-2 + H <=> H2 + C7H7-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (281049, 'cm^3/(mol*s)'),
        n = 2.41207,
        Ea = (8837.35, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['Li, S.-H.', 'Guo, J.-J.', 'Li, R.', 'Wang, F.', 'Li, X.-Y.'],
        title = 'Theoretical Prediction of Rate Constants for Hydrogen Abstraction by OH, H, O, CH3, and HO2 Radicals from Toluene',
        journal = 'The Journal of Physical Chemistry A',
        volume = '120 (20)',
        pages = '3424-3432',
        year = '2016',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc =
u"""
G4//B3LYP/6-31G(2df,p)
""",
)

entry(
    index = 184,
    label = "C9H8 + H <=> H2 + C9H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.54e+07, 'cm^3/(mol*s)'),
        n = 1.901,
        Ea = (15.418, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: kislovB""",
    longDesc =
u"""
Taken from entry: C9H8_20 + H_15 <=> C9H7_18 + H2_23
""",
)

entry(
    index = 185,
    label = "C9H8-2 + H <=> H2 + C9H7-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.725e+07, 'cm^3/(mol*s)'),
        n = 1.892,
        Ea = (16.619, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: kislovB""",
    longDesc =
u"""
Taken from entry: C9H8_21 + H_15 <=> C9H7_22 + H2_23
""",
)

entry(
    index = 186,
    label = "CH4_r12 + H <=> CH3_p1 + H2_p",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(4100, 'cm^3/(mol*s)'), n=3.156, Ea=(8755, 'cal/mol'), T0=(1, 'K')),
    rank = 1,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, Experimental, original source: doi 10.1002/kin.1064""",
)

entry(
    index = 187,
    label = "CH4_r12 + O_rad <=> CH3_p1 + OH_p23",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(440000, 'cm^3/(mol*s)'), n=2.5, Ea=(6577, 'cal/mol'), T0=(1, 'K')),
    rank = 1,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, Experimental, original source: doi 10.1063/1.1748524""",
)

entry(
    index = 188,
    label = "CH4_r12 + OH_r3 <=> CH3_p1 + H2O_p23",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(1e+06, 'cm^3/(mol*s)'), n=2.182, Ea=(2506, 'cal/mol'), T0=(1, 'K')),
    rank = 1,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, Experimental, original source: doi 10.1021/jp040679j""",
)

entry(
    index = 189,
    label = "CH4_r12 + HO2_r3 <=> CH3_p1 + H2O2_p13",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(47000, 'cm^3/(mol*s)'), n=2.5, Ea=(21000, 'cal/mol'), T0=(1, 'K')),
    rank = 1,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, Experimental, original source: doi 10.1063/1.1748524""",
)

entry(
    index = 190,
    label = "CH4_r12 + O2 <=> CH3_p1 + HO2",
    degeneracy = 8.0,
    kinetics = Arrhenius(
        A = (203000, 'cm^3/(mol*s)'),
        n = 2.745,
        Ea = (51714, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, Experimental, original source: doi 10.1039/B702267K""",
)

entry(
    index = 191,
    label = "CH4O + H <=> CH2OH_p + H2_p",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(66000, 'cm^3/(mol*s)'), n=2.728, Ea=(4449, 'cal/mol'), T0=(1, 'K')),
    rank = 4,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, QCISD(T)/CBS//QCISD(T)/cc-pVTZ, original source: doi 10.1088/0004-637X/737/1/15""",
)

entry(
    index = 192,
    label = "CH4O-2 + H <=> CH3O_p + H2_p",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(41000, 'cm^3/(mol*s)'), n=2.658, Ea=(9221, 'cal/mol'), T0=(1, 'K')),
    rank = 1,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, Experimental, original source: doi 10.1063/1.1748524""",
)

entry(
    index = 193,
    label = "CH4O + O_rad <=> CH2OH_p + OH_p23",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(2.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(5305, 'cal/mol'), T0=(1, 'K')),
    rank = 1,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, Experimental, original source: doi 10.1063/1.1748524""",
)

entry(
    index = 194,
    label = "CH4O-2 + O_rad <=> CH3O_p + OH_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(5305, 'cal/mol'), T0=(1, 'K')),
    rank = 1,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, Experimental, original source: doi 10.1063/1.1748524""",
)

entry(
    index = 195,
    label = "CH4O + OH_r3 <=> CH2OH_p + H2O_p23",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.5e+08, 'cm^3/(mol*s)'),
        n = 1.4434,
        Ea = (113, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, Experimental, original source: doi 10.1063/1.1748524""",
)

entry(
    index = 196,
    label = "CH4O-2 + OH_r3 <=> CH3O_p + H2O_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.7e+07, 'cm^3/(mol*s)'),
        n = 1.4434,
        Ea = (113, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, Experimental, original source: doi 10.1063/1.1748524""",
)

entry(
    index = 197,
    label = "CH4O + HO2_r3 <=> CH2OH_p + H2O2_p13",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (0.00035, 'cm^3/(mol*s)'),
        n = 4.85,
        Ea = (10346, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (100, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, MS-CVT/MT, original source: doi 10.1021/jp209029p""",
)

entry(
    index = 198,
    label = "CH4O-2 + HO2_r3 <=> CH3O_p + H2O2_p13",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.0015, 'cm^3/(mol*s)'),
        n = 4.61,
        Ea = (15828, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, MS-CVT/MT, original source: doi 10.1021/jp209029p""",
)

entry(
    index = 199,
    label = "CH4O + O2 <=> CH2OH_p + HO2",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (360000, 'cm^3/(mol*s)'),
        n = 2.27,
        Ea = (42760, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, CCSD(T)/CBS//CASPT2/cc-pvtz, original source: doi 10.1016/j.proci.2010.05.066""",
)

entry(
    index = 200,
    label = "CH3O-2 + HO2_r12 <=> CH3OH_p + O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.4e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, Multichannel RRKM, original source: doi 10.1021/jp112081r""",
)

entry(
    index = 201,
    label = "CH4O + CH3_r3 <=> CH2OH_p + CH4_p23",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (2.19e-07, 'cm^3/(mol*s)'),
        n = 5.58,
        Ea = (3896.3, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, MP2//B3LYP/6-311++G(3df,3pd), original source: doi 10.1016/j.comptc.2015.10.009""",
)

entry(
    index = 202,
    label = "CH3OOH_rC + H <=> CH2OOH_p + H2_p",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(5.4e+10, 'cm^3/(mol*s)'), n=0, Ea=(1860, 'cal/mol'), T0=(1, 'K')),
    rank = 1,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, Experimental, original source: doi 10.1002/kin.550090209""",
)

entry(
    index = 203,
    label = "CH4O2 + H <=> CH3OO_p + H2_p",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.4e+10, 'cm^3/(mol*s)'), n=0, Ea=(1860, 'cal/mol'), T0=(1, 'K')),
    rank = 1,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, Experimental, original source: doi 10.1002/kin.550090209""",
)

entry(
    index = 204,
    label = "CH3OOH_rC + O_rad <=> CH2OOH_p + OH_p23",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(1.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(4750, 'cal/mol'), T0=(1, 'K')),
    rank = 1,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, Experimental, original source: doi 10.1063/1.1748524""",
)

entry(
    index = 205,
    label = "CH4O2 + O_rad <=> CH3OO_p + OH_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(4750, 'cal/mol'), T0=(1, 'K')),
    rank = 1,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, Experimental, original source: doi 10.1063/1.1748524""",
)

entry(
    index = 206,
    label = "CH4O2 + OH_r3 <=> CH3OO_p + H2O_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.1e+12, 'cm^3/(mol*s)'), n=0, Ea=(-437, 'cal/mol'), T0=(1, 'K')),
    rank = 1,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, Experimental, original source: doi 10.1063/1.1748524""",
)

entry(
    index = 207,
    label = "CH3OOH_rC + OH_r3 <=> CH2OOH_p + H2O_p23",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(7.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(-258, 'cal/mol'), T0=(1, 'K')),
    rank = 1,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, Experimental, original source: doi 10.1063/1.1748524""",
)

entry(
    index = 208,
    label = "CH4O2 + HO2_r3 <=> CH3OO_p + H2O2_p13",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(41000, 'cm^3/(mol*s)'), n=2.5, Ea=(10206, 'cal/mol'), T0=(1, 'K')),
    rank = 1,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, Experimental, original source: doi 10.1002/kin.20352""",
)

entry(
    index = 209,
    label = "CH3O2 + CH4_r12 <=> CH3OOH_p + CH3_p1",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (0.00445, 'cm^3/(mol*s)'),
        n = 4.691,
        Ea = (19868, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (400, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, Experimental, original source: doi 10.1016/j.combustflame.2016.07.016""",
)

entry(
    index = 210,
    label = "C2H6 + H <=> C2H5b + H2_p",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (1.15e+08, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (7530, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: GRI-Mech3.0""",
    longDesc =
u"""
The respective reaction in the more recent Klippenstein_Glarborg2016 library is in a duplicate form
and cannot be added as training unless refitting the data

C2H6+H=C2H5+H2  7.35E+03	3.1	5340.02
DUPLICATE
C2H6+H=C2H5+H2	3.26E+14	0	13666.81
DUPLICATE
! R. Sivaramakrishnan, et al.,  Int. J. Chem. Kinet. 44 (2012) 194205.
""",
)

entry(
    index = 211,
    label = "C2H6 + O_rad <=> C2H5b + OH_p23",
    degeneracy = 6.0,
    kinetics = Arrhenius(A=(180000, 'cm^3/(mol*s)'), n=2.8, Ea=(5800, 'cal/mol'), T0=(1, 'K')),
    rank = 1,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, Experimental, original source: doi 10.1063/1.1748524""",
)

entry(
    index = 212,
    label = "C2H6 + OH_r3 <=> C2H5b + H2O_p23",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (1.61e+06, 'cm^3/(mol*s)'),
        n = 2.224,
        Ea = (740.73, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, Experimental, original source: doi 10.1021/jp040186e""",
)

entry(
    index = 213,
    label = "C2H6 + HO2_r3 <=> C2H5b + H2O2_p13",
    degeneracy = 6.0,
    kinetics = Arrhenius(A=(26, 'cm^3/(mol*s)'), n=3.37, Ea=(15900, 'cal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, CBS-QB3, original source: doi 10.1016/j.proci.2004.08.076""",
)

entry(
    index = 214,
    label = "C2H6 + O2 <=> C2H5b + HO2",
    degeneracy = 12.0,
    kinetics = Arrhenius(
        A = (2.92e+07, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (49548, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, CBS-Q, original source: doi 10.1021/jp304906u""",
)

entry(
    index = 215,
    label = "C2H6 + CH3_r3 <=> C2H5b + CH4_p23",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (35, 'cm^3/(mol*s)'),
        n = 3.44,
        Ea = (10384, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, Experimental, original source: doi 10.1021/jp4073153""",
)

entry(
    index = 216,
    label = "CH3O2 + C2H6 <=> CH3OOH_p + C2H5b",
    degeneracy = 6.0,
    kinetics = Arrhenius(A=(19, 'cm^3/(mol*s)'), n=3.64, Ea=(17100, 'cal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, CBS-QB3, original source: doi 10.1021/jp0451142""",
)

entry(
    index = 217,
    label = "C2H4 + H <=> C2H3_p + H2_p",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(240, 'cm^3/(mol*s)'), n=3.62, Ea=(11266, 'cal/mol'), T0=(1, 'K')),
    rank = 1,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, Experimental, original source: doi 10.1063/1.1748524""",
)

entry(
    index = 218,
    label = "C2H4 + OH_r3 <=> C2H3_p + H2O_p23",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(0.13, 'cm^3/(mol*s)'), n=4.2, Ea=(-860, 'cal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016""",
)

entry(
    index = 219,
    label = "C2H4 + O2 <=> C2H3_p + HO2",
    degeneracy = 8.0,
    kinetics = Arrhenius(A=(7.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(60010, 'cal/mol'), T0=(1, 'K')),
    rank = 4,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, RQCISD(T)//QCISD, original source: doi 10.1021/jp0566820""",
)

entry(
    index = 220,
    label = "C2H6O + H <=> CH3CHOH_p + H2_p",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(8800, 'cm^3/(mol*s)'), n=2.68, Ea=(2913, 'cal/mol'), T0=(1, 'K')),
    rank = 1,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, Experimental, original source: doi 10.1021/jp104759d""",
)

entry(
    index = 221,
    label = "C2H6O-2 + H <=> CH2CH2OH_p + H2_p",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(5300, 'cm^3/(mol*s)'), n=2.81, Ea=(7491, 'cal/mol'), T0=(1, 'K')),
    rank = 1,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, Experimental, original source: doi 10.1021/jp104759d""",
)

entry(
    index = 222,
    label = "CH3CH2OH_rO + H <=> CH3CH2O_p + H2_p",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(950, 'cm^3/(mol*s)'), n=3.14, Ea=(8696, 'cal/mol'), T0=(1, 'K')),
    rank = 1,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, Experimental, original source: doi 10.1021/jp104759d""",
)

entry(
    index = 223,
    label = "C2H6O-2 + O_rad <=> CH2CH2OH_p + OH_p23",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(970, 'cm^3/(mol*s)'), n=3.23, Ea=(4660, 'cal/mol'), T0=(1, 'K')),
    rank = 4,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, CCSD(T)/6-311+G(3df,2p)//B3LYP/6-311+G(3df), original source: doi 10.1021/jp068977z""",
)

entry(
    index = 224,
    label = "C2H6O + O_rad <=> CH3CHOH_p + OH_p23",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(150000, 'cm^3/(mol*s)'), n=2.47, Ea=(876, 'cal/mol'), T0=(1, 'K')),
    rank = 4,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, CCSD(T)/6-311+G(3df,2p)//B3LYP/6-311+G(3df), original source: doi 10.1021/jp068977z""",
)

entry(
    index = 225,
    label = "CH3CH2OH_rO + O_rad <=> CH3CH2O_p + OH_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.0015, 'cm^3/(mol*s)'), n=4.7, Ea=(1730, 'cal/mol'), T0=(1, 'K')),
    rank = 4,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, CCSD(T)/6-311+G(3df,2p)//B3LYP/6-311+G(3df), original source: doi 10.1021/jp068977z""",
)

entry(
    index = 226,
    label = "C2H6O + OH_r3 <=> CH3CHOH_p + H2O_p23",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(450, 'cm^3/(mol*s)'), n=3.11, Ea=(-2666, 'cal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, MP-VTST, original source: doi 10.1039/C2FD20012K""",
)

entry(
    index = 227,
    label = "C2H6O-2 + OH_r3 <=> CH2CH2OH_p + H2O_p23",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(9400, 'cm^3/(mol*s)'), n=2.67, Ea=(-1004, 'cal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, MP-VTST, original source: doi 10.1039/C2FD20012K""",
)

entry(
    index = 228,
    label = "C2H6O + HO2_r3 <=> CH3CHOH_p + H2O2_p13",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(8200, 'cm^3/(mol*s)'), n=2.55, Ea=(10750, 'cal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, RRKM, original source: doi 10.1002/(SICI)1097-4601(1999)31:3<183::AID-KIN3>3.0.CO;2-X""",
)

entry(
    index = 229,
    label = "C2H6O-2 + HO2_r3 <=> CH2CH2OH_p + H2O2_p13",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(12000, 'cm^3/(mol*s)'), n=2.55, Ea=(15750, 'cal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, RRKM, original source: doi 10.1002/(SICI)1097-4601(1999)31:3<183::AID-KIN3>3.0.CO;2-X""",
)

entry(
    index = 230,
    label = "CH3CH2OH_rO + HO2_r3 <=> CH3CH2O_p + H2O2_p13",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(24000, 'cal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, RRKM, original source: doi 10.1002/(SICI)1097-4601(1999)31:3<183::AID-KIN3>3.0.CO;2-X""",
)

entry(
    index = 231,
    label = "C2H6O + CH3_r3 <=> CH3CHOH_p + CH4_p23",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(20, 'cm^3/(mol*s)'), n=3.37, Ea=(7630, 'cal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016""",
)

entry(
    index = 232,
    label = "C2H6O-2 + CH3_r3 <=> CH2CH2OH_p + CH4_p23",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(2, 'cm^3/(mol*s)'), n=3.57, Ea=(7717, 'cal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016""",
)

entry(
    index = 233,
    label = "CH3CH2OH_rO + CH3_r3 <=> CH3CH2O_p + CH4_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(330, 'cm^3/(mol*s)'), n=3.3, Ea=(12283, 'cal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016""",
)

entry(
    index = 234,
    label = "C2H4O + H <=> CH3CO_p + H2_p",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(130000, 'cm^3/(mol*s)'), n=2.58, Ea=(1219, 'cal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, RRKM, original source: doi 10.1002/kin.20844""",
)

entry(
    index = 235,
    label = "CH3CHO_r1 + H <=> CH2CHO_p + H2_p",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(2700, 'cm^3/(mol*s)'), n=3.1, Ea=(5203, 'cal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, RRKM, original source: doi 10.1002/kin.20844""",
)

entry(
    index = 236,
    label = "C2H4O + O_rad <=> CH3CO_p + OH_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(1808, 'cal/mol'), T0=(1, 'K')),
    rank = 1,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, Experimental, original source: doi 10.1063/1.1748524""",
)

entry(
    index = 237,
    label = "C2H4O + OH_r3 <=> CH3CO_p + H2O_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(-709, 'cal/mol'), T0=(1, 'K')),
    rank = 1,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, Experimental, original source: doi 10.1016/j.proci.2014.06.112""",
)

entry(
    index = 238,
    label = "CH3CHO_r1 + OH_r3 <=> CH2CHO_p + H2O_p23",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(8.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(5313, 'cal/mol'), T0=(1, 'K')),
    rank = 1,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, Experimental, original source: doi 10.1016/j.proci.2014.06.112""",
)

entry(
    index = 239,
    label = "C2H4O + HO2_r3 <=> CH3CO_p + H2O2_p13",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(16293, 'cal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, DFT, original source: doi 10.1002/jcc.21756""",
)

entry(
    index = 240,
    label = "CH3CHO_r1 + HO2_r3 <=> CH2CHO_p + H2O2_p13",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(1.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(23248, 'cal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, DFT, original source: doi 10.1002/jcc.21756""",
)

entry(
    index = 241,
    label = "C2H4O + O2 <=> CH3CO_p + HO2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(120000, 'cm^3/(mol*s)'), n=2.5, Ea=(37554, 'cal/mol'), T0=(1, 'K')),
    rank = 1,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, Experimental, original source: doi 10.1063/1.1748524""",
)

entry(
    index = 242,
    label = "C2H4O + CH3_r3 <=> CH3CO_p + CH4_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.5e-08, 'cm^3/(mol*s)'),
        n = 6.21,
        Ea = (1629, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, Experimental, original source: doi 10.1063/1.1748524""",
)

entry(
    index = 243,
    label = "CH3CH2OO_r3 + HO2_r12 <=> CH3CH2OOH_p + O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1391, 'cal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016""",
)

entry(
    index = 244,
    label = "CH3C(O)OO_r3 + HO2_r12 <=> CH3C(O)OOH_p + O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1950, 'cal/mol'), T0=(1, 'K')),
    rank = 1,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, Experimental, original source: doi 10.1063/1.1748524""",
)

entry(
    index = 245,
    label = "C3H3-2 + H2 <=> C3H4 + H",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.056, 'cm^3/(mol*s)'),
        n = 3.503,
        Ea = (15.039, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['Narendrapurapu, B. S.', 'Simmonett, A. C.', 'Schaefer, H. F.', 'Miller, J. A.', 'Klippenstein, S. J.'],
        title = 'Combustion Chemistry: Important Features of the C3H5 Potential Energy Surface, Including Allyl Radical, Propargyl + H2, Allene + H, and Eight Transition States',
        journal = 'The Journal of Physical Chemistry A',
        volume = '115 (49)',
        pages = '14209-14214',
        year = '2011',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc =
u"""
Accurate geometries are obtained using coupled cluster theory with single, double, and perturbative triple excitations [CCSD(T)] combined with Dunnings correlation consistent quadruple- basis set cc pVQZ. The energies for these stationary points are then refined by a systematic series of computations, within the focal point scheme, using the cc-pVXZ (X = D, T, Q, 5, 6) basis sets and correlation treatments as extensive as coupled cluster with full single, double, and triple excitation and perturbative quadruple excitations [CCSDT(Q)]. TST rates calculated in CanTherm
""",
)

entry(
    index = 246,
    label = "C3H3 + H2 <=> C3H4-1 + H",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.07496, 'cm^3/(mol*s)'),
        n = 3.944,
        Ea = (16.255, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['Narendrapurapu, B. S.', 'Simmonett, A. C.', 'Schaefer, H. F.', 'Miller, J. A.', 'Klippenstein, S. J.'],
        title = 'Combustion Chemistry: Important Features of the C3H5 Potential Energy Surface, Including Allyl Radical, Propargyl + H2, Allene + H, and Eight Transition States',
        journal = 'The Journal of Physical Chemistry A',
        volume = '115 (49)',
        pages = '14209-14214',
        year = '2011',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc =
u"""
Accurate geometries are obtained using coupled cluster theory with single, double, and perturbative triple excitations [CCSD(T)] combined with Dunnings correlation consistent quadruple- basis set cc pVQZ. The energies for these stationary points are then refined by a systematic series of computations, within the focal point scheme, using the cc-pVXZ (X = D, T, Q, 5, 6) basis sets and correlation treatments as extensive as coupled cluster with full single, double, and triple excitation and perturbative quadruple excitations [CCSDT(Q)]. TST rates calculated in CanTherm
""",
)

entry(
    index = 247,
    label = "C3H4 + H <=> H2 + C3H3-2",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (196.3, 'cm^3/(mol*s)'),
        n = 3.47,
        Ea = (3.214, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['Narendrapurapu, B. S.', 'Simmonett, A. C.', 'Schaefer, H. F.', 'Miller, J. A.', 'Klippenstein, S. J.'],
        title = 'Combustion Chemistry: Important Features of the C3H5 Potential Energy Surface, Including Allyl Radical, Propargyl + H2, Allene + H, and Eight Transition States',
        journal = 'The Journal of Physical Chemistry A',
        volume = '115 (49)',
        pages = '14209-14214',
        year = '2011',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc =
u"""
Accurate geometries are obtained using coupled cluster theory with single, double, and perturbative triple excitations [CCSD(T)] combined with Dunnings correlation consistent quadruple- basis set cc pVQZ. The energies for these stationary points are then refined by a systematic series of computations, within the focal point scheme, using the cc-pVXZ (X = D, T, Q, 5, 6) basis sets and correlation treatments as extensive as coupled cluster with full single, double, and triple excitation and perturbative quadruple excitations [CCSDT(Q)]. TST rates calculated in CanTherm
""",
)

entry(
    index = 248,
    label = "C3H4-1 + H <=> H2 + C3H3",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (14.13, 'cm^3/(mol*s)'),
        n = 3.852,
        Ea = (3.502, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['Narendrapurapu, B. S.', 'Simmonett, A. C.', 'Schaefer, H. F.', 'Miller, J. A.', 'Klippenstein, S. J.'],
        title = 'Combustion Chemistry: Important Features of the C3H5 Potential Energy Surface, Including Allyl Radical, Propargyl + H2, Allene + H, and Eight Transition States',
        journal = 'The Journal of Physical Chemistry A',
        volume = '115 (49)',
        pages = '14209-14214',
        year = '2011',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc =
u"""
Accurate geometries are obtained using coupled cluster theory with single, double, and perturbative triple excitations [CCSD(T)] combined with Dunnings correlation consistent quadruple- basis set cc pVQZ. The energies for these stationary points are then refined by a systematic series of computations, within the focal point scheme, using the cc-pVXZ (X = D, T, Q, 5, 6) basis sets and correlation treatments as extensive as coupled cluster with full single, double, and triple excitation and perturbative quadruple excitations [CCSDT(Q)]. TST rates calculated in CanTherm
""",
)

entry(
    index = 249,
    label = "C4H4 + CH3_r3 <=> CH4_p23 + C4H3_p",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.24, 'cm^3/(mol*s)'), n=3.335, Ea=(7.75, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    longDesc =
u"""
TST calculation based on the CBS-QB3 level of theory with 1D hinder rotoer consideration
Jim Chu's calculation
""",
)

entry(
    index = 250,
    label = "C4H4 + H <=> H2 + C4H3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.092e+06, 'cm^3/(mol*s)'),
        n = 2.211,
        Ea = (7.181, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    longDesc =
u"""
TST calculation based on the CBS-QB3 level of theory with 1D hinder rotoer consideration
Jim Chu's calculation
""",
)

entry(
    index = 251,
    label = "C4H6-5 + CH3_r3 <=> CH4_p23 + C4H5-4_p",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (14.26, 'cm^3/(mol*s)'),
        n = 3.317,
        Ea = (6.61, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    longDesc =
u"""
TST calculation based on the CBS-QB3 level of theory with 1D hinder rotoer consideration
Jim Chu's calculation
""",
)

entry(
    index = 252,
    label = "C4H6-5 + H <=> H2 + C4H5-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.867e+06, 'cm^3/(mol*s)'),
        n = 2.242,
        Ea = (5.318, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    longDesc =
u"""
TST calculation based on the CBS-QB3 level of theory with 1D hinder rotoer consideration
Jim Chu's calculation
""",
)

entry(
    index = 253,
    label = "C4H6 + CH3_r3 <=> CH4_p23 + CHCCHCH3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (29.41, 'cm^3/(mol*s)'),
        n = 3.184,
        Ea = (5.529, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    longDesc =
u"""
TST calculation based on the CBS-QB3 level of theory with 1D hinder rotoer consideration
Jim Chu's calculation
""",
)

entry(
    index = 254,
    label = "C4H6 + H <=> H2 + C4H5-5",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (8.501e+06, 'cm^3/(mol*s)'),
        n = 2.027,
        Ea = (4.069, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    longDesc =
u"""
TST calculation based on the CBS-QB3 level of theory with 1D hinder rotoer consideration
Jim Chu's calculation
""",
)

entry(
    index = 255,
    label = "C3H4 + OH_r3 <=> H2O_p23 + C3H3-2",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (12560, 'cm^3/(mol*s)'),
        n = 2.794,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['Zador, J.', 'Miller, J. A.'],
        title = 'Adventures on the C3H5O potential energy surface: OH + propyne, OH + allene and related reactions',
        journal = 'Proceedings of the Combustion Institute',
        volume = '35 (1)',
        pages = '181-188',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc =
u"""
UCCSD(T)-F12b/cc-pVQZ-F12//M06-2X/6-311++G(d,p)
""",
)

entry(
    index = 256,
    label = "C3H4-1 + OH_r3 <=> H2O_p23 + C3H3",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (33830, 'cm^3/(mol*s)'),
        n = 2.802,
        Ea = (0.933, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['Zador, J.', 'Miller, J. A.'],
        title = 'Adventures on the C3H5O potential energy surface: OH + propyne, OH + allene and related reactions',
        journal = 'Proceedings of the Combustion Institute',
        volume = '35 (1)',
        pages = '181-188',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc =
u"""
UCCSD(T)-F12b/cc-pVQZ-F12//M06-2X/6-311++G(d,p)
""",
)

entry(
    index = 257,
    label = "C7H8 + OH_r3 <=> H2O_p23 + C7H7",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (130169, 'cm^3/(mol*s)'),
        n = 2.28048,
        Ea = (-572.972, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['Li, S.-H.', 'Guo, J.-J.', 'Li, R.', 'Wang, F.', 'Li, X.-Y.'],
        title = 'Theoretical Prediction of Rate Constants for Hydrogen Abstraction by OH, H, O, CH3, and HO2 Radicals from Toluene',
        journal = 'The Journal of Physical Chemistry A',
        volume = '120 (20)',
        pages = '3424-3432',
        year = '2016',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc =
u"""
G4//B3LYP/6-31G(2df,p)
""",
)

entry(
    index = 258,
    label = "C7H8-2 + OH_r3 <=> H2O_p23 + C7H7-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (277.731, 'cm^3/(mol*s)'),
        n = 2.99789,
        Ea = (1245.72, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['Li, S.-H.', 'Guo, J.-J.', 'Li, R.', 'Wang, F.', 'Li, X.-Y.'],
        title = 'Theoretical Prediction of Rate Constants for Hydrogen Abstraction by OH, H, O, CH3, and HO2 Radicals from Toluene',
        journal = 'The Journal of Physical Chemistry A',
        volume = '120 (20)',
        pages = '3424-3432',
        year = '2016',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc =
u"""
G4//B3LYP/6-31G(2df,p)
""",
)

entry(
    index = 259,
    label = "C7H8-3 + OH_r3 <=> H2O_p23 + C7H7-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (819.665, 'cm^3/(mol*s)'),
        n = 3.09594,
        Ea = (1507.71, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['Li, S.-H.', 'Guo, J.-J.', 'Li, R.', 'Wang, F.', 'Li, X.-Y.'],
        title = 'Theoretical Prediction of Rate Constants for Hydrogen Abstraction by OH, H, O, CH3, and HO2 Radicals from Toluene',
        journal = 'The Journal of Physical Chemistry A',
        volume = '120 (20)',
        pages = '3424-3432',
        year = '2016',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc =
u"""
G4//B3LYP/6-31G(2df,p)
""",
)

entry(
    index = 260,
    label = "C7H8-4 + OH_r3 <=> H2O_p23 + C7H7-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (763.895, 'cm^3/(mol*s)'),
        n = 3.10443,
        Ea = (1688.65, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['Li, S.-H.', 'Guo, J.-J.', 'Li, R.', 'Wang, F.', 'Li, X.-Y.'],
        title = 'Theoretical Prediction of Rate Constants for Hydrogen Abstraction by OH, H, O, CH3, and HO2 Radicals from Toluene',
        journal = 'The Journal of Physical Chemistry A',
        volume = '120 (20)',
        pages = '3424-3432',
        year = '2016',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc =
u"""
G4//B3LYP/6-31G(2df,p)
""",
)

entry(
    index = 261,
    label = "C7H8-3 + H <=> H2 + C7H7-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.16e+06, 'cm^3/(mol*s)'),
        n = 2.44202,
        Ea = (9052.88, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['Li, S.-H.', 'Guo, J.-J.', 'Li, R.', 'Wang, F.', 'Li, X.-Y.'],
        title = 'Theoretical Prediction of Rate Constants for Hydrogen Abstraction by OH, H, O, CH3, and HO2 Radicals from Toluene',
        journal = 'The Journal of Physical Chemistry A',
        volume = '120 (20)',
        pages = '3424-3432',
        year = '2016',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc =
u"""
G4//B3LYP/6-31G(2df,p)
""",
)

entry(
    index = 262,
    label = "C7H8-4 + H <=> H2 + C7H7-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.57e+06, 'cm^3/(mol*s)'),
        n = 2.40693,
        Ea = (9440.52, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['Li, S.-H.', 'Guo, J.-J.', 'Li, R.', 'Wang, F.', 'Li, X.-Y.'],
        title = 'Theoretical Prediction of Rate Constants for Hydrogen Abstraction by OH, H, O, CH3, and HO2 Radicals from Toluene',
        journal = 'The Journal of Physical Chemistry A',
        volume = '120 (20)',
        pages = '3424-3432',
        year = '2016',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc =
u"""
G4//B3LYP/6-31G(2df,p)
""",
)

entry(
    index = 263,
    label = "C7H8 + O_rad <=> HO + C7H7",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (0.00788, 'cm^3/(mol*s)'),
        n = 4.29278,
        Ea = (11250.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['Li, S.-H.', 'Guo, J.-J.', 'Li, R.', 'Wang, F.', 'Li, X.-Y.'],
        title = 'Theoretical Prediction of Rate Constants for Hydrogen Abstraction by OH, H, O, CH3, and HO2 Radicals from Toluene',
        journal = 'The Journal of Physical Chemistry A',
        volume = '120 (20)',
        pages = '3424-3432',
        year = '2016',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc =
u"""
G4//B3LYP/6-31G(2df,p)
""",
)

entry(
    index = 264,
    label = "C7H8-2 + O_rad <=> HO + C7H7-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.71418, 'cm^3/(mol*s)'),
        n = 3.64569,
        Ea = (21743.3, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['Li, S.-H.', 'Guo, J.-J.', 'Li, R.', 'Wang, F.', 'Li, X.-Y.'],
        title = 'Theoretical Prediction of Rate Constants for Hydrogen Abstraction by OH, H, O, CH3, and HO2 Radicals from Toluene',
        journal = 'The Journal of Physical Chemistry A',
        volume = '120 (20)',
        pages = '3424-3432',
        year = '2016',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc =
u"""
G4//B3LYP/6-31G(2df,p)
""",
)

entry(
    index = 265,
    label = "C7H8-3 + O_rad <=> HO + C7H7-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.02029, 'cm^3/(mol*s)'),
        n = 3.64209,
        Ea = (22208.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['Li, S.-H.', 'Guo, J.-J.', 'Li, R.', 'Wang, F.', 'Li, X.-Y.'],
        title = 'Theoretical Prediction of Rate Constants for Hydrogen Abstraction by OH, H, O, CH3, and HO2 Radicals from Toluene',
        journal = 'The Journal of Physical Chemistry A',
        volume = '120 (20)',
        pages = '3424-3432',
        year = '2016',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc =
u"""
G4//B3LYP/6-31G(2df,p)
""",
)

entry(
    index = 266,
    label = "C7H8-4 + O_rad <=> HO + C7H7-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.79741, 'cm^3/(mol*s)'),
        n = 3.6191,
        Ea = (22697.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['Li, S.-H.', 'Guo, J.-J.', 'Li, R.', 'Wang, F.', 'Li, X.-Y.'],
        title = 'Theoretical Prediction of Rate Constants for Hydrogen Abstraction by OH, H, O, CH3, and HO2 Radicals from Toluene',
        journal = 'The Journal of Physical Chemistry A',
        volume = '120 (20)',
        pages = '3424-3432',
        year = '2016',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc =
u"""
G4//B3LYP/6-31G(2df,p)
""",
)

entry(
    index = 267,
    label = "C7H8 + CH3_r3 <=> CH4_p23 + C7H7_p",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.07e+06, 'cm^3/(mol*s)'),
        n = 2.26764,
        Ea = (4392.37, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['Li, S.-H.', 'Guo, J.-J.', 'Li, R.', 'Wang, F.', 'Li, X.-Y.'],
        title = 'Theoretical Prediction of Rate Constants for Hydrogen Abstraction by OH, H, O, CH3, and HO2 Radicals from Toluene',
        journal = 'The Journal of Physical Chemistry A',
        volume = '120 (20)',
        pages = '3424-3432',
        year = '2016',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc =
u"""
G4//B3LYP/6-31G(2df,p)
""",
)

entry(
    index = 268,
    label = "C7H8-2 + CH3_r3 <=> CH4_p23 + C7H7-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.21e+07, 'cm^3/(mol*s)'),
        n = 1.81483,
        Ea = (14155.6, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['Li, S.-H.', 'Guo, J.-J.', 'Li, R.', 'Wang, F.', 'Li, X.-Y.'],
        title = 'Theoretical Prediction of Rate Constants for Hydrogen Abstraction by OH, H, O, CH3, and HO2 Radicals from Toluene',
        journal = 'The Journal of Physical Chemistry A',
        volume = '120 (20)',
        pages = '3424-3432',
        year = '2016',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc =
u"""
G4//B3LYP/6-31G(2df,p)
""",
)

entry(
    index = 269,
    label = "C7H8-3 + CH3_r3 <=> CH4_p23 + C7H7-3_p",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.11e+08, 'cm^3/(mol*s)'),
        n = 1.80464,
        Ea = (14389, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['Li, S.-H.', 'Guo, J.-J.', 'Li, R.', 'Wang, F.', 'Li, X.-Y.'],
        title = 'Theoretical Prediction of Rate Constants for Hydrogen Abstraction by OH, H, O, CH3, and HO2 Radicals from Toluene',
        journal = 'The Journal of Physical Chemistry A',
        volume = '120 (20)',
        pages = '3424-3432',
        year = '2016',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc =
u"""
G4//B3LYP/6-31G(2df,p)
""",
)

entry(
    index = 270,
    label = "C7H8-4 + CH3_r3 <=> CH4_p23 + C7H7-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.05e+08, 'cm^3/(mol*s)'),
        n = 1.81188,
        Ea = (14672.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['Li, S.-H.', 'Guo, J.-J.', 'Li, R.', 'Wang, F.', 'Li, X.-Y.'],
        title = 'Theoretical Prediction of Rate Constants for Hydrogen Abstraction by OH, H, O, CH3, and HO2 Radicals from Toluene',
        journal = 'The Journal of Physical Chemistry A',
        volume = '120 (20)',
        pages = '3424-3432',
        year = '2016',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc =
u"""
G4//B3LYP/6-31G(2df,p)
""",
)

entry(
    index = 271,
    label = "C7H8 + HO2_r3 <=> H2O2 + C7H7",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (2.55836, 'cm^3/(mol*s)'),
        n = 3.80712,
        Ea = (7395.74, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['Li, S.-H.', 'Guo, J.-J.', 'Li, R.', 'Wang, F.', 'Li, X.-Y.'],
        title = 'Theoretical Prediction of Rate Constants for Hydrogen Abstraction by OH, H, O, CH3, and HO2 Radicals from Toluene',
        journal = 'The Journal of Physical Chemistry A',
        volume = '120 (20)',
        pages = '3424-3432',
        year = '2016',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc =
u"""
G4//B3LYP/6-31G(2df,p)
""",
)

entry(
    index = 272,
    label = "C7H8-2 + HO2_r3 <=> H2O2 + C7H7-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.71418, 'cm^3/(mol*s)'),
        n = 3.64569,
        Ea = (21743.27, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['Li, S.-H.', 'Guo, J.-J.', 'Li, R.', 'Wang, F.', 'Li, X.-Y.'],
        title = 'Theoretical Prediction of Rate Constants for Hydrogen Abstraction by OH, H, O, CH3, and HO2 Radicals from Toluene',
        journal = 'The Journal of Physical Chemistry A',
        volume = '120 (20)',
        pages = '3424-3432',
        year = '2016',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc =
u"""
G4//B3LYP/6-31G(2df,p)
""",
)

entry(
    index = 273,
    label = "C7H8-3 + HO2_r3 <=> H2O2 + C7H7-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.02029, 'cm^3/(mol*s)'),
        n = 3.64209,
        Ea = (22208.17, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['Li, S.-H.', 'Guo, J.-J.', 'Li, R.', 'Wang, F.', 'Li, X.-Y.'],
        title = 'Theoretical Prediction of Rate Constants for Hydrogen Abstraction by OH, H, O, CH3, and HO2 Radicals from Toluene',
        journal = 'The Journal of Physical Chemistry A',
        volume = '120 (20)',
        pages = '3424-3432',
        year = '2016',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc =
u"""
G4//B3LYP/6-31G(2df,p)
""",
)

entry(
    index = 274,
    label = "C7H8-4 + CH3_r3 <=> CH4_p23 + C7H7-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (204.902, 'cm^3/(mol*s)'),
        n = 3.30806,
        Ea = (14723.9, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['Li, S.-H.', 'Guo, J.-J.', 'Li, R.', 'Wang, F.', 'Li, X.-Y.'],
        title = 'Theoretical Prediction of Rate Constants for Hydrogen Abstraction by OH, H, O, CH3, and HO2 Radicals from Toluene',
        journal = 'The Journal of Physical Chemistry A',
        volume = '120 (20)',
        pages = '3424-3432',
        year = '2016',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc =
u"""
G4//B3LYP/6-31G(2df,p)
""",
)

entry(
    index = 275,
    label = "C6H6 + H <=> H2 + C6H5",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (4.57e+08, 'cm^3/(mol*s)'),
        n = 1.88,
        Ea = (14.839, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['Semenikhin, A. S.', 'Savchenkova, A. S.', 'Chechet, I. V.', 'Matveev, S. G.', 'Liu, Z.', 'Frenklach, M.', 'Mebel, A. M.'],
        title = 'Rate constants for H abstraction from benzo(a)pyrene and chrysene: a theoretical study',
        journal = 'Physical Chemistry Chemical Physics',
        volume = '19 (37)',
        pages = '25401-25413',
        year = '2017',
    ),
    referenceType = "theory",
    rank = 5,
    longDesc =
u"""
G3(MP2,CC)//B3LYP
""",
)

entry(
    index = 276,
    label = "C12H8 + H <=> H2 + C12H7",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.27e+08, 'cm^3/(mol*s)'),
        n = 1.71,
        Ea = (16.236, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['Violi, A.', 'Truong, T. N.', 'Sarofim, A. F.'],
        title = 'Kinetics of Hydrogen Abstraction Reactions from Polycyclic Aromatic Hydrocarbons by H Atoms',
        journal = 'The Journal of Physical Chemistry A',
        volume = '108 (22)',
        pages = '4846-4852',
        year = '2004',
    ),
    referenceType = "theory",
    rank = 9,
    longDesc =
u"""
B3LYP structural and vibrational information with BH&HLYP corrected barrier
""",
)

entry(
    index = 277,
    label = "C6H6 + OH_r3 <=> H2O_p23 + C6H5",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (3.88e-20, 'cm^3/(molecule*s)'),
        n = 2.683,
        Ea = (0.7333, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['Seta, T.', 'Nakajima, M.', 'Miyoshi, A.'],
        title = 'High-Temperature Reactions of OH Radicals with Benzene and Toluene',
        journal = 'The Journal of Physical Chemistry A',
        volume = '110 (15)',
        pages = '5081-5090',
        year = '2006',
    ),
    referenceType = "theory",
    rank = 1,
    longDesc =
u"""
CBS-QB3 + Exp.
""",
)

entry(
    index = 278,
    label = "C6H6 + CH3_r3 <=> CH4_p23 + C6H5",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (3.07e-21, 'cm^3/(molecule*s)'),
        n = 2.88,
        Ea = (13.332, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['Mai, T. V. T.', 'Ratkiewicz, A.', 'Duong, M. v.', 'Huynh, L. K.'],
        title = 'Direct ab initio study of the C6H6+CH3/C2H5=C6H5+CH4/C2H6 reactions',
        journal = 'Chemical Physics Letters',
        volume = '646',
        pages = '102-109',
        year = '2016',
    ),
    referenceType = "theory",
    rank = 5,
    longDesc =
u"""
CCSD(T)/CBS//BH&HLYP/cc-pVDZ, and canonical variational transition state theory (CVT) with corrections for small curvaturetunneling (SCT) and hindered internal rotation (HIR)
""",
)

entry(
    index = 279,
    label = "C6H6 + C2H5 <=> C2H6 + C6H5",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (2.62e-22, 'cm^3/(molecule*s)'),
        n = 3.11,
        Ea = (18.66, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['Mai, T. V. T.', 'Ratkiewicz, A.', 'Duong, M. v.', 'Huynh, L. K.'],
        title = 'Direct ab initio study of the C6H6+CH3/C2H5=C6H5+CH4/C2H6 reactions',
        journal = 'Chemical Physics Letters',
        volume = '646',
        pages = '102-109',
        year = '2016',
    ),
    referenceType = "theory",
    rank = 5,
    longDesc =
u"""
CCSD(T)/CBS//BH&HLYP/cc-pVDZ, and canonical variational transition state theory (CVT) with corrections for small curvaturetunneling (SCT) and hindered internal rotation (HIR)
""",
)

entry(
    index = 280,
    label = "C10H8 + H <=> H2 + C10H7",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (3.91e+08, 'cm^3/(mol*s)'),
        n = 1.84,
        Ea = (14.973, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['Semenikhin, A. S.', 'Savchenkova, A. S.', 'Chechet, I. V.', 'Matveev, S. G.', 'Liu, Z.', 'Frenklach, M.', 'Mebel, A. M.'],
        title = 'Rate constants for H abstraction from benzo(a)pyrene and chrysene: a theoretical study',
        journal = 'Physical Chemistry Chemical Physics',
        volume = '19 (37)',
        pages = '25401-25413',
        year = '2017',
    ),
    referenceType = "theory",
    rank = 5,
    longDesc =
u"""
G3(MP2,CC)//B3LYP
""",
)

entry(
    index = 281,
    label = "C10H8-2 + H <=> H2 + C10H7-2",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (4.04e+08, 'cm^3/(mol*s)'),
        n = 1.83,
        Ea = (14.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['Semenikhin, A. S.', 'Savchenkova, A. S.', 'Chechet, I. V.', 'Matveev, S. G.', 'Liu, Z.', 'Frenklach, M.', 'Mebel, A. M.'],
        title = 'Rate constants for H abstraction from benzo(a)pyrene and chrysene: a theoretical study',
        journal = 'Physical Chemistry Chemical Physics',
        volume = '19 (37)',
        pages = '25401-25413',
        year = '2017',
    ),
    referenceType = "theory",
    rank = 5,
    longDesc =
u"""
G3(MP2,CC)//B3LYP
""",
)

entry(
    index = 282,
    label = "C6H5 + H2 <=> C6H6 + H",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (16900, 'cm^3/(mol*s)'),
        n = 2.63,
        Ea = (4.559, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['Semenikhin, A. S.', 'Savchenkova, A. S.', 'Chechet, I. V.', 'Matveev, S. G.', 'Liu, Z.', 'Frenklach, M.', 'Mebel, A. M.'],
        title = 'Rate constants for H abstraction from benzo(a)pyrene and chrysene: a theoretical study',
        journal = 'Physical Chemistry Chemical Physics',
        volume = '19 (37)',
        pages = '25401-25413',
        year = '2017',
    ),
    referenceType = "theory",
    rank = 5,
    longDesc =
u"""
G3(MP2,CC)//B3LYP
""",
)

entry(
    index = 283,
    label = "C10H7 + H2 <=> C10H8 + H",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (15800, 'cm^3/(mol*s)'),
        n = 2.63,
        Ea = (4.107, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['Semenikhin, A. S.', 'Savchenkova, A. S.', 'Chechet, I. V.', 'Matveev, S. G.', 'Liu, Z.', 'Frenklach, M.', 'Mebel, A. M.'],
        title = 'Rate constants for H abstraction from benzo(a)pyrene and chrysene: a theoretical study',
        journal = 'Physical Chemistry Chemical Physics',
        volume = '19 (37)',
        pages = '25401-25413',
        year = '2017',
    ),
    referenceType = "theory",
    rank = 5,
    longDesc =
u"""
G3(MP2,CC)//B3LYP
""",
)

entry(
    index = 284,
    label = "C10H7-2 + H2 <=> C10H8-2 + H",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (18400, 'cm^3/(mol*s)'),
        n = 2.61,
        Ea = (4.446, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['Semenikhin, A. S.', 'Savchenkova, A. S.', 'Chechet, I. V.', 'Matveev, S. G.', 'Liu, Z.', 'Frenklach, M.', 'Mebel, A. M.'],
        title = 'Rate constants for H abstraction from benzo(a)pyrene and chrysene: a theoretical study',
        journal = 'Physical Chemistry Chemical Physics',
        volume = '19 (37)',
        pages = '25401-25413',
        year = '2017',
    ),
    referenceType = "theory",
    rank = 5,
    longDesc =
u"""
G3(MP2,CC)//B3LYP
""",
)

entry(
    index = 285,
    label = "H2 + O_rad <=> HO + H",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.4e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (96.0228, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Dean, A. M. [118]""",
    longDesc =
u"""
[118] Dean, A.M. Development and application of Detailed Kinetic Mechanisms for Free Radical Systems.

Converted to training reaction from rate rule: X_H;O_atom_triplet
""",
)


entry(
    index = 292,
    label = "OH_r3 + C3H8 <=> H2O_p23 + C3H7",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (900000, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-4.74047, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Curran et al. [8] Rate expressions for H atom abstraction from fuels. (changed to per H)""",
    longDesc =
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
http://dx.doi.org/10.1016/S0010-2180(01)00373-X

Rate expressions for H atom abstraction from fuels.
pg 257 A Comprehensive Modelling Study of iso-Octane Oxidation, Table 1. Radical:OH, Site: secondary (b)

Verified by Karma James

These numbers reported by Curran et al. were apparently taken from
N. Cohen, *Intl. J. Chem. Kinet.* 14 (1982), p. 1339 http://dx.doi.org/10.1002/kin.550141206


Rate expression is changed to per H.(divided by 2)
Yushi Suzuki

Converted to training reaction from rate rule: C/H2/NonDeC;O_pri_rad
""",
)

entry(
    index = 293,
    label = "OH_r3 + iC4H10b <=> H2O_p23 + C4H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.7e+06, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (-6.07098, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Curran et al. [8] Rate expressions for H atom abstraction from fuels.""",
    longDesc =
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
http://dx.doi.org/10.1016/S0010-2180(01)00373-X

Rate expressions for H atom abstraction from fuels.
pg 257 A Comprehensive Modelling Study of iso-Octane Oxidation, Table 1. Radical:OH, Site: tertiary (c)

Verified by Karma James

These numbers reported by Curran et al. were apparently taken from
N. Cohen, *Intl. J. Chem. Kinet.* 14 (1982), p. 1339 http://dx.doi.org/10.1002/kin.550141206

Converted to training reaction from rate rule: C/H/Cs3;O_pri_rad
""",
)

entry(
    index = 294,
    label = "C2H6 + O_rad <=> HO + C2H5",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (5700, 'cm^3/(mol*s)'),
        n = 3.05,
        Ea = (46.4424, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Curran et al. [8] Rate expressions for H atom abstraction from fuels. (changed to per H)""",
    longDesc =
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Rate expressions for H atom abstraction from fuels.

pg 257 A Comprehensive Modelling Study of iso-Octane Oxidation, Table 1. Radical:O, Site: primary (a)

Verified by Karma James

Rate expression is changed to per H.(divided by 9)
Yushi Suzuki

Converted to training reaction from rate rule: C/H3/Cs;O_atom_triplet
""",
)

entry(
    index = 295,
    label = "C3H8 + O_rad <=> HO + C3H7",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (47800, 'cm^3/(mol*s)'),
        n = 2.71,
        Ea = (57.4045, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Curran et al. [8] Rate expressions for H atom abstraction from fuels. (changed to per H)""",
    longDesc =
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Rate expressions for H atom abstraction from fuels.

pg 257 A Comprehensive Modelling Study of iso-Octane Oxidation, Table 1. Radical:O, Site: secondary (b)

Verified by Karma James


Rate expression is changed to per H.(divided by 2)
Yushi Suzuki

Converted to training reaction from rate rule: C/H2/NonDeC;O_atom_triplet
""",
)

entry(
    index = 296,
    label = "iC4H10b + O_rad <=> HO + C4H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (383000, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (61.9232, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Curran et al. [8] Rate expressions for H atom abstraction from fuels.""",
    longDesc =
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Rate expressions for H atom abstraction from fuels.

pg 257 A Comprehensive Modelling Study of iso-Octane Oxidation, Table 1. Radical:O, Site: tertiary (c)

Verified by Karma James


This rate parameter actually comes from following new mechanism for PRF.

https://www-pls.llnl.gov/data/docs/science_and_technology/chemistry/combustion/prf_2d_mech.txt

Yushi Suzuki

Converted to training reaction from rate rule: C/H/Cs3;O_atom_triplet
""",
)

entry(
    index = 298,
    label = "HO2_r3 + C3H8 <=> H2O2 + C3H7",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (5.6e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (73.9982, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Curran et al. [8] Rate expressions for H atom abstraction from fuels. (changed to per H)""",
    longDesc =
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Rate expressions for H atom abstraction from fuels.

pg 257 A Comprehensive Modelling Study of iso-Octane Oxidation, Table 1. Radical:HO2, Site: secondary (b)

Verified by Karma James

Rate expression is changed to per H.(divided by 2)
Yushi Suzuki

Converted to training reaction from rate rule: C/H2/NonDeC;O_rad/NonDeO
""",
)

entry(
    index = 299,
    label = "HO2_r3 + iC4H10b <=> H2O2 + C4H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.8e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (66.9984, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Curran et al. [8] Rate expressions for H atom abstraction from fuels.""",
    longDesc =
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Rate expressions for H atom abstraction from fuels.

pg 257 A Comprehensive Modelling Study of iso-Octane Oxidation, Table 1. Radical:HO2, Site: tertiary (c)

Verified by Karma James

Converted to training reaction from rate rule: C/H/Cs3;O_rad/NonDeO
""",
)

entry(
    index = 300,
    label = "CH3O-2 + C2H6 <=> CH4O-2 + C2H5",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (3.162e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (29.288, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Curran et al. [8] Rate expressions for H atom abstraction from fuels. (changed to per H)""",
    longDesc =
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Rate expressions for H atom abstraction from fuels.

pg 257 A Comprehensive Modelling Study of iso-Octane Oxidation, Table 1. Radical:CH3O, Site: primary (a)

Verified by Karma James

Rate expression is changed to per H.(divided by 9)
Yushi Suzuki

Converted to training reaction from rate rule: C/H3/Cs;O_rad/NonDeC
""",
)

entry(
    index = 301,
    label = "CH3O-2 + C3H8 <=> CH4O-2 + C3H7",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.1e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (36.0818, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Curran et al. [8] Rate expressions for H atom abstraction from fuels. (changed to per H)""",
    longDesc =
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Rate expressions for H atom abstraction from fuels.

pg 257 A Comprehensive Modelling Study of iso-Octane Oxidation, Table 1. Radical:CH3O, Site: secondary (b)

Verified by Karma James

Rate expression is changed to per H.(divided by 2)
Yushi Suzuki

Converted to training reaction from rate rule: C/H2/NonDeC;O_rad/NonDeC
""",
)

entry(
    index = 302,
    label = "CH3O-2 + iC4H10b <=> CH4O-2 + C4H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.9e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (40.6005, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Curran et al. [8] Rate expressions for H atom abstraction from fuels.""",
    longDesc =
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Rate expressions for H atom abstraction from fuels.

pg 257 A Comprehensive Modelling Study of iso-Octane Oxidation, Table 1. Radical:CH3O, Site: tertiary (c)

Verified by Karma James

Converted to training reaction from rate rule: C/H/Cs3;O_rad/NonDeC
""",
)

entry(
    index = 303,
    label = "C2H6 + O2 <=> HO2_r12 + C2H5",
    degeneracy = 12.0,
    kinetics = Arrhenius(
        A = (8.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (212.38, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Curran et al. [8] Rate expressions for H atom abstraction from fuels. (changed to per H)""",
    longDesc =
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Rate expressions for H atom abstraction from fuels.

pg 257 A Comprehensive Modelling Study of iso-Octane Oxidation, Table 1. Radical:O2, Site: primary (a)

Verified by Karma James

Rate expression is changed to per H.(divided by 9)
Yushi Suzuki

Converted to training reaction from rate rule: C/H3/Cs;O2b
""",
)

entry(
    index = 304,
    label = "C3H8 + O2 <=> HO2_r12 + C3H7",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (2.8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (201.711, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Curran et al. [8] Rate expressions for H atom abstraction from fuels. (changed to per H)""",
    longDesc =
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Rate expressions for H atom abstraction from fuels.

pg 257 A Comprehensive Modelling Study of iso-Octane Oxidation, Table 1. Radical:O2, Site: secondary (b)

Verified by Karma James

Rate expression is changed to per H.(divided by 2)
Yushi Suzuki

Converted to training reaction from rate rule: C/H2/NonDeC;O2b
""",
)

entry(
    index = 305,
    label = "iC4H10b + O2 <=> HO2_r12 + C4H9-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (192.715, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Curran et al. [8] Rate expressions for H atom abstraction from fuels.""",
    longDesc =
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Rate expressions for H atom abstraction from fuels.

pg 257 A Comprehensive Modelling Study of iso-Octane Oxidation, Table 1. Radical:O2, Site: tertiary (c)

Verified by Karma James

Converted to training reaction from rate rule: C/H/Cs3;O2b
""",
)

entry(
    index = 306,
    label = "H2 + O2 <=> HO2_r12 + H",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (2.9e+14, 'cm^3/(mol*s)', '*|/', 5),
        n = 0,
        Ea = (236.982, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (800, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang et al. [89] literature review.""",
    longDesc =
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
H2 + O2 --> H + HO2 C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 1091, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 3,2.

Verified by Karma James

pg. 1109: Discussion of evaluated data

Recommended value computed using reverse rate and thermodynamics

MRH 28-Aug-2009

Converted to training reaction from rate rule: H2;O2b
""",
)

entry(
    index = 307,
    label = "H2 + C2H3 <=> C2H4 + H",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (9460, 'cm^3/(mol*s)'),
        n = 2.56,
        Ea = (21.0455, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Knyazev et al. [119] Transition state theory.""",
    longDesc =
u"""
[119] Knyazev, V.D; Bencsura, A.; Stoliarov, S.I.; Slagle, I.R. J. Phys. Chem. 1996, 100, 11346.
H2 + C2H3 --> H + C2H4 C.D.W divided original rate expression by 2 ( from A = 9.45E+03), to get rate expression per H atom.

Converted to training reaction from rate rule: H2;Cd_pri_rad
""",
)

entry(
    index = 308,
    label = "H2 + C2H <=> C2H2 + H",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.08e+13, 'cm^3/(mol*s)', '*|/', 3.16),
        n = 0,
        Ea = (9.07928, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Baulch et al. [94] literature review.""",
    longDesc =
u"""
[94] Baulch, D.L.; Cobos, C.J.; Cox, R.A.; Frank, P.; Hayman, G,; Just, T.; Kerr, J.A.; Murrells, T.; Pilling, M.J.;
Troe, J.; Walker, R.W.; Warnatz, J. J. Phys. Chem. Ref. Data 1994, 23, 847.

H2 + C2H --> H + C2H2 C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 863 Evaluated Kinetic Data for Combustion Modelling Supplement 1, Table 1. Bimolecular reactions - C2H Radical Reactions.

Verified by Karma James

pg.1013-1014: Discussion on evaluated data

C2H+H2-->C2H2+H: Recommended rate coefficient is that reported by Koshi et al.  Rate

coefficient was computed for low temperatures, but extrapolation to higher temperatures
fits other reported data reasonably well.
MRH 31-Aug-2009

Converted to training reaction from rate rule: H2;Ct_rad
""",
)

entry(
    index = 309,
    label = "H2 + C6H5 <=> C6H6 + H",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (57200, 'cm^3/(mol*s)'),
        n = 2.43,
        Ea = (26.2755, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (5000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Mebel et al. [122] Transition state theory.""",
    longDesc =
u"""
[122] Mebel, A.M.; Lin, M.C.; Yu, T.; Morokuma, K. J. Phys. Chem. A. 1997, 101, 3189.
H2 + phenyl --> H + benzene C.D.W divided original rate expression by 2 ( from A = 5.71E+04), to get rate expression per H atom.

Converted to training reaction from rate rule: H2;Cb_rad
""",
)

entry(
    index = 310,
    label = "H2 + HCO_r3 <=> CH2O + H",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.8e+06, 'cm^3/(mol*s)', '*|/', 5),
        n = 2,
        Ea = (204.765, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang et al. [89] literature review.""",
    longDesc =
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
H2 + HCO --> H + CH2O C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 1094, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 15,2.

Verified by Karma James

pg. 1147: Discussion of evaluated data

Recommended value computed using reverse rate and thermodynamics

MRH 28-Aug-2009

Converted to training reaction from rate rule: H2;CO_pri_rad
""",
)

entry(
    index = 312,
    label = "H2 + OH_r3 <=> H2O_p23 + H_p",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.82e+09, 'cm^3/(mol*s)'),
        n = 1.21,
        Ea = (83.9729, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (2400, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Isaacson [123] Transition state theory.""",
    longDesc =
u"""
[123] Isaacson, A.D. J. Chem. Phys. 1997, 107, 3832.
H2 + O2 --> H + H2O C.D.W divided original rate expression by 2, to get rate expression per H atom.

166. [100] Jodkowski, J.T.; Rauez, M.-T.; Rayez, J.-C. J. Phys. Chem. A. 1999, 103, 3750.

H2 + CH3O --> H + CH3OH The calculated reverse rate constants are in good agreement with experiment. (This is -R1 in the paper)

C.D.W divided original rate expression by 2, to get rate expression per H atom.

Verified by Greg Magoon; maximum error of fitted expression from tabular data for forward rate constant, kr1 is 15% (cf. p. 3758)

Converted to training reaction from rate rule: H2;O_pri_rad
""",
)

entry(
    index = 314,
    label = "CH4_r12 + O2 <=> HO2_p23 + CH3_p1",
    degeneracy = 8.0,
    kinetics = Arrhenius(
        A = (7.94e+13, 'cm^3/(mol*s)', '*|/', 10),
        n = 0,
        Ea = (237.777, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Baulch et al. [95] literature review.""",
    longDesc =
u"""
[95] Baulch, D.L.; Cobos, C.J.; Cox, R.A.; Esser, C.; Frank, P.; Just, T.; Kerr, J.A.; Pilling, M.J.;
Troe, J.; Walker, R.W.; Warnatz, J. J. Phys. Chem. Ref. Data 1992, 21, 411.

CH4 + O2 --> CH3 + HO2 C.D.W divided original rate expression by 4, to get rate expression per H atom.

pg 417 Evaluated Kinetic Data for Combustion Modelling, Table 1. Bimolecular reactions - O2 Reactions.

Verified by Karma James

pg.483: Discussion on evaluated data

O2+CH4 --> HO2+CH3: Recommended data based on experimental value for CH2O + O2 -->

HO2 + HCO.  Assumes equal A factor per C-H bond and Ea = deltaH.
MRH 31-Aug-2009

Converted to training reaction from rate rule: C_methane;O2b
""",
)

entry(
    index = 316,
    label = "C3H7 + CH4_r12 <=> C3H8 + CH3_p1",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (0.000724, 'cm^3/(mol*s)', '*|/', 2),
        n = 4.4,
        Ea = (45.1454, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang et al. [91] literature review.""",
    longDesc =
u"""
[91] Tsang, W. J. Phys. Chem. Ref. Data 1988, 17, 887.
CH4 + iso-C3H7 --> CH3 + C3H8 C.D.W divided original rate expression by 4, to get rate expression per H atom.

pg 894, Chemical Kinetic Database For Combustion Chemistry, Part 3. Index of Reactions and Summary of Recommended Rate Expressions. No. 42,10.

Verified by Karma James

pg. 935: Discussion on evaluated data

Entry 42,10: No data available at the time.  Author recommends rate coefficient

expression based on reverse rate and equilibrium constant.
MRH 30-Aug-2009

Converted to training reaction from rate rule: C_methane;C_rad/H/NonDeC
""",
)

entry(
    index = 317,
    label = "C2H + CH4_r12 <=> C2H2 + CH3_p1",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (1.812e+12, 'cm^3/(mol*s)', '*|/', 10),
        n = 0,
        Ea = (2.092, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang et al. [89] literature review.""",
    longDesc =
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
CH4 + C2H --> CH3 + C2H2 C.D.W divided original rate expression by 4, to get rate expression per H atom.

pg 1101, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 21,10.

Verified by Karma James

pg. 1220: Discussion of evaluated data

Recommended data is expression given by Brown and Laufer (1981).

They computed the pre-exponential factor by the bond energy-bond order (BEBO) method

and combined that with experimental k at room temperature to yield Arrhenius expression
MRH 28-Aug-2009

Converted to training reaction from rate rule: C_methane;Ct_rad
""",
)

entry(
    index = 319,
    label = "HCO_r3 + CH4_r12 <=> CH2O + CH3_p1",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (7280, 'cm^3/(mol*s)', '*|/', 5),
        n = 2.85,
        Ea = (143.302, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang et al. [89] literature review.""",
    longDesc =
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
CH4 + HCO --> CH3 + CH2O C.D.W divided original rate expression by 4, to get rate expression per H atom.

pg 1094, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 15,10.

Verified by Karma James

pg. 1150: Discussion on evaluated data

Recommended data computed using reverse rate and equilibrium constant

MRH 28-Aug-2009

Converted to training reaction from rate rule: C_methane;CO_pri_rad
""",
)

entry(
    index = 321,
    label = "OH_r3 + CH4_r12 <=> H2O_p23 + CH3_p1",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (1.54, 'cm^3/(mol*s)'),
        n = 3.95,
        Ea = (22.5099, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (223, 'K'),
        Tmax = (2400, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Melissas and Truhlar [125] Transition state theory.""",
    longDesc =
u"""
[125] Melissas, V.S.; Truhlar, D.G. J. Chem. Phys. 1993,99,1010.
CH4 + OH --> CH3 + H2O C.D.W divided original rate expression by 4, to get rate expression per H atom.

Converted to training reaction from rate rule: C_methane;O_pri_rad
""",
)

entry(
    index = 322,
    label = "CH3O-2 + CH4_r12 <=> CH4O-2 + CH3_p1",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (0.00062, 'cm^3/(mol*s)'),
        n = 5,
        Ea = (23.3467, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Jodkowski et al. [100] ab initio calculations.""",
    longDesc =
u"""
[100] Jodkowski, J.T.; Rauez, M.-T.; Rayez, J.-C. J. Phys. Chem. A. 1999, 103, 3750.
CH4 + CH3O --> CH3 + CH3OH The calculated reverse rate constants are in good agreement with experiment. (Rxn. -R3 in paper)

C.D.W divided original rate expression by 4 ( from A= 1.51E+09), to get rate expression per H atom.

Verified by Greg Magoon; cf. reverse reaction, #261, below

Converted to training reaction from rate rule: C_methane;O_rad/NonDeC
""",
)

entry(
    index = 323,
    label = "HO2_r3 + CH4_r12 <=> H2O2 + CH3_p1",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (1.812e+11, 'cm^3/(mol*s)', '*|/', 5),
        n = 0,
        Ea = (77.7387, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang et al. [89] literature review.""",
    longDesc =
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
CH4 + HO2 --> CH3 + H2O2 C.D.W divided original rate expression by 4, to get rate expression per H atom.

pg 1093, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 10,7.

Verified by Karma James

pg. 1131: Discussion on evaluated data

Recommended data is based on expression for HO2 attach on alkanes (Walker)

MRH 28-Aug-2009

Converted to training reaction from rate rule: C_methane;O_rad/NonDeO
""",
)

entry(
    index = 324,
    label = "C2H + C2H6 <=> C2H2 + C2H5",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (3.612e+12, 'cm^3/(mol*s)', '*|/', 3),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang et al. [89] literature review.""",
    longDesc =
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
C2H6 + C2H --> C2H5 + C2H2 C.D.W divided original rate expression by 6, to get rate expression per H atom.

pg 1101, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 21,11.

Verified by Karma James

pg. 1221: Discussion on evaluated data

Recommended data is based on expression given by Brown and Laufer (1981).

Brown and Laufer calculated pre-exponential factor by BEBO method and
combined calculation with experimental measurement of k at room temperature.
MRH 28-Aug-2009

Converted to training reaction from rate rule: C/H3/Cs;Ct_rad
""",
)

entry(
    index = 325,
    label = "C6H5 + C2H6 <=> C6H6 + C2H5",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (2.088e+11, 'cm^3/(mol*s)', '*|/', 2.35),
        n = 0,
        Ea = (18.577, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (565, 'K'),
        Tmax = (1000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Park et al. [126]""",
    longDesc =
u"""
[126] Park, J.; Gheyas, S.; Lin, M.C. Int. J. Chem. Kinet. 2001, 33, 64.
Absolute value measured directly. Static or low flow, flash photolysis excitation, Vis-UV absoprtion analysis.

Phenyl radicals are produced from 193 nm photolysis of C6H5COCH3. The cavity ringdown spectroscopy and/or mass spectroscopy

have been used to monitor reactant and/or products. C2H6 + phenyl --> C2H5 + benzene.

C.D.W divided original rate expression by 6 ( from A= 2.09E+11), to get rate expression per H atom. Original delta A = 2.0E+10.

Converted to training reaction from rate rule: C/H3/Cs;Cb_rad
""",
)

entry(
    index = 326,
    label = "HCO_r3 + C2H6 <=> CH2O + C2H5",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (46920, 'cm^3/(mol*s)', '*|/', 5),
        n = 2.72,
        Ea = (159.996, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang et al. [89] literature review.""",
    longDesc =
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
C2H6 + HCO --> C2H5 + CH2O C.D.W divided original rate expression by 6(from A = 4.69E+04), to get rate expression per H atom.

pg 1094, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 15,11.

Verified by Karma James

pg. 1150: Discussion on evaluated data

Recommended data computed from reverse rate and equilibrium constant

MRH 28-Aug-2009

Converted to training reaction from rate rule: C/H3/Cs;CO_pri_rad
""",
)

entry(
    index = 327,
    label = "C2H3O + C2H6 <=> C2H4O + C2H5",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (18120, 'cm^3/(mol*s)', '*|/', 5),
        n = 2.75,
        Ea = (172.52, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang et al. [89] literature review.""",
    longDesc =
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
C2H6 + CH3CO --> C2H5 + CH3CHO C.D.W divided original rate expression by 6(from A = 1.81E+04), to get rate expression per H atom.

pg 1102, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 22,11.

Verified by Karma James

pg. 1231: Discussion on evaluated data

Recommended data computed using rate of C2H5+CH2O divided by 2 (since only one O=C-H

hydrogen is present in CH3CHO) and equilibrium constant
MRH 28-Aug-2009

Converted to training reaction from rate rule: C/H3/Cs;CO_rad/NonDe
""",
)

entry(
    index = 328,
    label = "OH_r3 + CH3CHO_r1 <=> H2O_p23 + C2H3O-2",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.551e+06, 'cm^3/(mol*s)'),
        n = 2.2,
        Ea = (18.3785, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (295, 'K'),
        Tmax = (600, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Taylor et al. [127] Transition state theory.""",
    longDesc =
u"""
[127] Taylor, P.H.; Rahman, M.S.; Arif, M.; Dellinger, B.; Marshall, P. Sypm. Int. Combust. Proc. 1996, 26, 497.
CH3CHO + OH --> CH2CHO + H2O Rate constant is high pressure limit (pressure 0.13-0.97atm?)

C.D.W divided original rate expression by 3(from A = 1.55E+06), to get rate expression per H atom.

Converted to training reaction from rate rule: C/H3/CO;O_pri_rad
""",
)

entry(
    index = 329,
    label = "CH4O + CH3_r3 <=> CH4_p23 + CH3O_p1",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (0.000615, 'cm^3/(mol*s)'),
        n = 4.9,
        Ea = (28.1165, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Jodkowski et al. [100] ab initio calculations.""",
    longDesc =
u"""
[100] Jodkowski, J.T.; Rauez, M.-T.; Rayez, J.-C. J. Phys. Chem. A. 1999, 103, 3750.
CH3OH + CH3 --> CH2OH + CH4 The calculated rate constants are in good agreement with experiment. (Rxn. R4 in paper)

C.D.W divided original rate expression by 3 ( from A= 8.43E+08), to get rate expression per H atom.

Verified by Greg Magoon

Converted to training reaction from rate rule: C/H3/O;C_methyl
""",
)

entry(
    index = 330,
    label = "OH_r3 + CH4O <=> H2O_p23 + CH3O",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (24420, 'cm^3/(mol*s)'),
        n = 2.8,
        Ea = (-1.75728, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Jodkowski et al. [100] ab initio calculations.""",
    longDesc =
u"""
[100] Jodkowski, J.T.; Rauez, M.-T.; Rayez, J.-C. J. Phys. Chem. A. 1999, 103, 3750.
CH3OH + OH --> CH2OH + H2O The calculated rate constants are in good agreement with experiment. (Rxn. R6 in paper)

C.D.W divided original rate expression by 3 ( from A= 2.11E+11), to get rate expression per H atom.

Verified by Greg Magoon
**Note that R2 from this paper appears to be missing from the RMG library, so I have added it as 1001**

Converted to training reaction from rate rule: C/H3/O;O_pri_rad
""",
)

entry(
    index = 331,
    label = "CH2 + C3H8 <=> CH3_p23 + CH3CHCH3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.51, 'cm^3/(mol*s)', '*|/', 10),
        n = 3.46,
        Ea = (31.2545, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang [91] literature review.""",
    longDesc =
u"""
[91] Tsang, W. J. Phys. Chem. Ref. Data 1988, 17, 887.
C3H8 + CH2 --> iso-C3H7 + CH3  C.D.W divided original rate expression by 2(from A = 1.51), to get rate expression per H atom.

pg 892, Chemical Kinetic Database For Combustion Chemistry, Part 3. Index of Reactions and Summary of Recommended Rate Expressions. No. 40,26.
Verified by Karma James

pg. 910: Discussion on evaluated data

Entry 40,26 (b): No data available at the time.  Author estimates the rate coefficient

expression as that of CH3+C3H8=i-C3H7+CH4.
MRH 30-Aug-2009

Converted to training reaction from rate rule: C/H2/NonDeC;CH2_triplet
""",
)

entry(
    index = 332,
    label = "CH3O + C3H8 <=> CH4O + C3H7",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (60.4, 'cm^3/(mol*s)', '*|/', 5),
        n = 2.95,
        Ea = (50.1243, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang [91] literature review.""",
    longDesc =
u"""
[91] Tsang, W. J. Phys. Chem. Ref. Data 1988, 17, 887.
C3H8 + CH2OH --> iso-C3H7 + CH3OH  C.D.W divided original rate expression by 2(from A = 6.03E+01), to get rate expression per H atom.

//WAS UNABLE TO VERIFY DATA!!! DATA NOT FOUND IN REFERENCE.

pg. 910: Discussion on evaluated data

Entry 40,39 (b)

No experimental data, at the time

Recommended value for C3H8+CH2OH-->n-C3H7+CH3OH comes from rate for C2H6+CH2OH-->C2H5+CH3OH

No discussion on where rate for C3H8+CH2OH-->i-C3H7+CH3OH comes from:

A is ~ factor of 3 smaller (6 hydrogens vs 2 ... seems reasonable to MRH)
E is 1 kcal/mol smaller (more stable to form secondary radical than primary)
Verified by MRH on 10Aug2009

MRH 30-Aug-2009

Converted to training reaction from rate rule: C/H2/NonDeC;C_rad/H2/O
""",
)

entry(
    index = 333,
    label = "C2H3 + C3H8 <=> C2H4 + C3H7",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1020, 'cm^3/(mol*s)', '*|/', 10),
        n = 3.1,
        Ea = (36.9029, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang [91] literature review.""",
    longDesc =
u"""
[91] Tsang, W. J. Phys. Chem. Ref. Data 1988, 17, 887.
C3H8 + C2H3 --> iso-C3H7 + C2H4  C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 891, Chemical Kinetic Database For Combustion Chemistry, Part 3. Index of Reactions and Summary of Recommended Rate Expressions. No. 40,19.

Verified by Karma James

pg. 906: Discussion on evaluated data

Entry 40,19 (b): No data available at the time.  The author recommends the rate coefficient

expression of C2H3+C2H6=C2H5+C2H4 for the rxn C2H3+C3H8=n-C3H7+C2H4.  The author
assumes the ratio of secondary-to-primary H-atom abstraction for the rxn CH3+C3H8
to obtain the recommended rate coefficient expression.
MRH 30-Aug-2009

Converted to training reaction from rate rule: C/H2/NonDeC;Cd_pri_rad
""",
)

entry(
    index = 334,
    label = "C2H + C3H8 <=> C2H2 + C3H7",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.21e+12, 'cm^3/(mol*s)', '*|/', 3),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang [91] literature review.""",
    longDesc =
u"""
[91] Tsang, W. J. Phys. Chem. Ref. Data 1988, 17, 887.
C3H8 + C2H --> iso-C3H7 + C2H2  C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 891, Chemical Kinetic Database For Combustion Chemistry, Part 3. Index of Reactions and Summary of Recommended Rate Expressions. No. 40,21.

Verified by Karma James

pg. 906-907: Discussion on evaluated data

Entry 40,21 (b): No data available at the time.  The author recommends the rate coefficient

of C2H6+C2H=C2H2+C2H5 for the rxn C3H8+C2H=C2H2+n-C3H7.  Due to the high exothermicity
of the rxn, the author assumes the H-atom abstraction rxn is limited to the number
of H-atoms available, thus recommedning a rate coefficient equal to one-third that
recommended for C3H8+C2H=C2H2+n-C3H7.
MRH 30-Aug-2009

Converted to training reaction from rate rule: C/H2/NonDeC;Ct_rad
""",
)

entry(
    index = 335,
    label = "HCO_r3 + C3H8 <=> CH2O + C3H7",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.08e+07, 'cm^3/(mol*s)', '*|/', 3),
        n = 1.9,
        Ea = (170.958, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang [91] literature review.""",
    longDesc =
u"""
[91] Tsang, W. J. Phys. Chem. Ref. Data 1988, 17, 887.
C3H8 + HCO --> iso-C3H7 + CH2O  C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 891, Chemical Kinetic Database For Combustion Chemistry, Part 3. Index of Reactions and Summary of Recommended Rate Expressions. No. 40,15.

Verified by Karma James

pg. 904: Discussion on evaluated data

Entry 40,15 (b): No data available at the time.  The author recommends a rate coefficient

expression based on the reverse rxn (note: the author uses the rate of the rxn
n-C3H7+CH2O=HCO+C3H8 instead of i-C3H7+CH2O=HCO+C3H8) and equilibrium constant.
MRH 30-Aug-2009

Converted to training reaction from rate rule: C/H2/NonDeC;CO_pri_rad
""",
)

entry(
    index = 336,
    label = "C2H3O + C3H8 <=> C2H4O + C3H7",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (5.3e+06, 'cm^3/(mol*s)', '*|/', 3),
        n = 2,
        Ea = (183.482, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang [91] literature review.""",
    longDesc =
u"""
[91] Tsang, W. J. Phys. Chem. Ref. Data 1988, 17, 887.
C3H8 + CH3CO --> iso-C3H7 + CH3CHO  C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 891, Chemical Kinetic Database For Combustion Chemistry, Part 3. Index of Reactions and Summary of Recommended Rate Expressions. No. 40,22.

Verified by Karma James

pg. 907: Discussion on evaluated data

Entry 40,22 (b): No data available at the time.  The author recommends a rate coefficient

expression based on the equilibrium constant and the reverse rate (note: the author
estimates this reverse rate using the suggestions of Kerr, J.A. and Trotman-Dickenson, A.F.).
MRH 30-Aug-2009

Converted to training reaction from rate rule: C/H2/NonDeC;CO_rad/NonDe
""",
)

entry(
    index = 337,
    label = "CH2 + iC4H10b <=> CH3_p23 + tC4H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.09e+12, 'cm^3/(mol*s)', '*|/', 5),
        n = 0,
        Ea = (20.5434, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang [92] literature review.""",
    longDesc =
u"""
[92] Tsang, W. J. Phys. Chem. Ref. Data 1990, 19, 1.
Iso-C4H10 + CH2 --> tert-C4H9 + CH3

pg 6, Chemical Kinetic Database For Combustion Chemistry, Part 4 - Isobutane.

Index of Reactions and Summary of Recommended Rate Expressions. No. 43,25.

Verified by Karma James

pg.23-24: Discussion on evaluated data

Entry 43,25(b): Tsang recommends the rate coefficient expression reported by Bohland et al.

Tsang notes that the rate for CH2_triplet abstracting a H-atom is faster than
the recommended value for CH3 abstracting a H-atom.
MRH 31-Aug-2009

Converted to training reaction from rate rule: C/H/Cs3;CH2_triplet
""",
)

entry(
    index = 338,
    label = "C2H3 + iC4H10b <=> C2H4 + C4H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.904, 'cm^3/(mol*s)', '*|/', 5),
        n = 3.46,
        Ea = (10.8784, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang [92] literature review.""",
    longDesc =
u"""
[92] Tsang, W. J. Phys. Chem. Ref. Data 1990, 19, 1.
Iso-C4H10 + C2H3 --> tert-C4H9 + C2H4

pg 5, Chemical Kinetic Database For Combustion Chemistry, Part 4 - Isobutane.

Index of Reactions and Summary of Recommended Rate Expressions. No. 43,19.

Verified by Karma James

pg.20: Discussion on evaluated data

Entry 43,19(b): No data available at the time.  Author recommends rate coefficient expression

based on the rxn CH3+iC4H10=CH4+tC4H9: same Arrhenius A and n parameters, Ea decreased
by 8.5 kJ/mol.
MRH 31-Aug-2009

Converted to training reaction from rate rule: C/H/Cs3;Cd_pri_rad
""",
)

entry(
    index = 339,
    label = "C2H + iC4H10b <=> C2H2 + C4H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.62e+11, 'cm^3/(mol*s)', '*|/', 3),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang [92] literature review.""",
    longDesc =
u"""
[92] Tsang, W. J. Phys. Chem. Ref. Data 1990, 19, 1.
Iso-C4H10 + C2H --> tert-C4H9 + C2H2

pg 5, Chemical Kinetic Database For Combustion Chemistry, Part 4 - Isobutane.

Index of Reactions and Summary of Recommended Rate Expressions. No. 43,21.

Verified by Karma James

pg.21: Discussion on evaluated data

Entry 43,21(b): No data available at the time.  For the rxn iC4H10+C2H=C2H2+iC4H9, author

recommends 1.5x the rate of the rxn C2H6+C2H=C2H2+C2H5 (9 vs. 6 primary H-atoms).
The author then recommends a rate coefficient for iC4H10+C2H=C2H2+tC4H9 that appears
to be 1/9 the rate of iC4H10+C2H=C2H2+iC4H9 (9 vs. 1 H-atom).
MRH 31-Aug-2009

Converted to training reaction from rate rule: C/H/Cs3;Ct_rad
""",
)

entry(
    index = 340,
    label = "HCO_r3 + iC4H10b <=> CH2O + C4H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (34300, 'cm^3/(mol*s)', '*|/', 5),
        n = 2.5,
        Ea = (175.477, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang [92] literature review.""",
    longDesc =
u"""
[92] Tsang, W. J. Phys. Chem. Ref. Data 1990, 19, 1.
Iso-C4H10 + HCO --> tert-C4H9 + CH2O

pg 5, Chemical Kinetic Database For Combustion Chemistry, Part 4 - Isobutane.

Index of Reactions and Summary of Recommended Rate Expressions. No. 43,15.

Verified by Karma James

pg.18: Discussion on evaluated data

Entry 43,15(b): No data available at the time.  For the rxn iC4H10+HCO=CH2O+iC4H9, author

recommends 1.5x the rate of the rxn C3H8+HCO+CH2O+nC3H7 (9 vs. 6 primary H-atoms).
The author then recommends the rate coefficient for iC4H10+HCO=CH2O+tC4H9 to be the
rate coefficient of iC4H10+HCO=CH2O+iC4H9, with the A factor divided by 9 (9 vs. 1
H-atoms) and the Ea decreased by 20 kJ/mol.
MRH 31-Aug-2009

Converted to training reaction from rate rule: C/H/Cs3;CO_pri_rad
""",
)

entry(
    index = 341,
    label = "C2H3O + iC4H10b <=> C2H4O + C4H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (34300, 'cm^3/(mol*s)', '*|/', 10),
        n = 2.5,
        Ea = (188.001, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang [92] literature review.""",
    longDesc =
u"""
[92] Tsang, W. J. Phys. Chem. Ref. Data 1990, 19, 1.
Iso-C4H10 + CH3CO --> tert-C4H9 + CH3CHO

pg 5, Chemical Kinetic Database For Combustion Chemistry, Part 4 - Isobutane.

Index of Reactions and Summary of Recommended Rate Expressions. No. 43,22.

Verified by Karma James

pg.21: Discussion on evaluated data

Entry 43,22(b): No data available at the time.  Author recommends rate coefficient expression

based on the rxn iC4H10+HCO=CH2O+tC4H9.
MRH 31-Aug-2009

Converted to training reaction from rate rule: C/H/Cs3;CO_rad/NonDe
""",
)

entry(
    index = 342,
    label = "C2H4 + O2 <=> HO2_r12 + C2H3",
    degeneracy = 8.0,
    kinetics = Arrhenius(
        A = (1.4336e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (251.082, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Hua, Ruscic, and Wang 2005, transition state theory.""",
    longDesc =
u"""
FORMER RATES
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
C2H4 + O2 --> C2H3 + HO2 C.D.W divided original rate expression by 4, to get rate expression per H atom.

pg 1097, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 18,3.

Verified by Karma James

pg. 1184: Discussion on evaluated data

Recommended data follows Walker's estimates for O2+alkane

Note: The authors note that a lower lying channel, involving addition and
rearrangement prior to decomposition, may exist.
MRH 28-Aug-2009


CURRENT RATES
Hua, H.; B. Ruscic; B. Wang.  Chemical Physics 2005, 311, 335-341.
C2H4 + O2 --> C2H3 + HO2.

Divided rate expression by 4 to get the rate expression per H atom.  See page 338.
Overall, this agrees with the earlier rate that we used.
JDM 15-Jun-2010.

Converted to training reaction from rate rule: Cd_pri;O2b
""",
)

entry(
    index = 343,
    label = "C2H4 + O_rad <=> HO + C2H3",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (1.512e+07, 'cm^3/(mol*s)'),
        n = 1.91,
        Ea = (116.399, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (290, 'K'),
        Tmax = (1510, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Mahmud et al. [128] Transition state theory""",
    longDesc =
u"""
[128] Mahmud, K.; Marshall, P.; Fontijn, A. J Phys. Chem. 1987, 91, `568.
C2H4 + O --> C2H3 + OH C.D.W divided original rate expression by 4(from A= 1.51E+07), to get rate expression per H atom.

Converted to training reaction from rate rule: Cd_pri;O_atom_triplet
""",
)

entry(
    index = 346,
    label = "C3H6-2 + O_rad <=> HO + C3H5-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.02e+10, 'cm^3/(mol*s)', '*|/', 3),
        n = 0.7,
        Ea = (116.943, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang [93] literature review.""",
    longDesc =
u"""
[93] Tsang, W. J. Phys. Chem. Ref. Data 1991, 20, 221.
CH3CH=CH2 + O --> CH3C=CH2 + OH

pg 233-234: Discussion on evaluated data

Verified by MRH on 6Aug2009

Entry 46,5(f): No measurements on H-atom abstraction rxns. Recommended rate coefficient

is computed as follows:

The rate of O + C3H6 --> OH + H2C=CH-*CH2 is computed using the expression:
[k(O+C2H6-->C2H5+HO)/k(OH+C2H6-->C2H5+H2O)] * k(OH+C3H6-->H2C=CH-*CH2+H2O).
The author uses this expression because he notes that OH and O H-atom abstraction
rxns generally follow the same trend.  The O+C2H6, OH+C2H6, and OH+C3H6
are from other Tsang review articles.
The rate of O+C3H6 --> OH+CH3C=CH2 is computed by adjusting the O+C3H6 --> OH+H2C=CH-*CH2
rate coefficient: increasing the Ea/R by 880 Kelvin and multiplying the A
by ~0.345; these values come from the relative difference between the rxns
OH+C3H6 --> H2O+H2C=CH-*CH2 and OH+C3H6 --> H2O+CH3C=CH2
MRH 31-Aug-2009

Converted to training reaction from rate rule: Cd/H/NonDeC;O_atom_triplet
""",
)

entry(
    index = 347,
    label = "H + C3H6-2 <=> H2 + C3H5-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (409000, 'cm^3/(mol*s)', '*|/', 4),
        n = 2.5,
        Ea = (40.9614, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang [93] literature review.""",
    longDesc =
u"""
[93] Tsang, W. J. Phys. Chem. Ref. Data 1991, 20, 221.
CH3CH=CH2 + H --> CH3C=CH2 + H2

pg 231: Discussion on evaluated data

Previous modified Arrhenius parameters were for RELATIVE rate (kc/ka)

Multipled kc/ka by ka to get kc (only one H to abstract, so no division necessary)

Certified by MRH on 6Aug2009

Entry 46,4(c): No data available for H-atom abstraction rxns.  The recommended rate

coefficient is based on the author's assumption that methyl substitution has the
same influence in olefins as in alkanes.
MRH 31-Aug-2009

Converted to training reaction from rate rule: Cd/H/NonDeC;H_rad
""",
)

entry(
    index = 348,
    label = "CH3_r3 + C3H6-2 <=> CH4_p23 + C3H5-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.842, 'cm^3/(mol*s)', '*|/', 6),
        n = 3.5,
        Ea = (87.1946, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang [93] literature review.""",
    longDesc =
u"""
[93] Tsang, W. J. Phys. Chem. Ref. Data 1991, 20, 221.
CH3CH=CH2 + CH3 --> CH3C=CH2 + CH4

pg 237-239

Previous modified Arrhenius parameters were for RELATIVE rate (ke/kc)

Multiplied ke/kc by kc to get ke (only one H to abstract, so no division necessary)

Certified by MRH on 6Aug2009

Entry 46,16(e): Recommended rate coefficient is based on the author's assumption

that methyl substitution has the same influence in olefins as in alkanes.
MRH 31-Aug-2009

Converted to training reaction from rate rule: Cd/H/NonDeC;C_methyl
""",
)

entry(
    index = 349,
    label = "C2H3 + C3H6-2 <=> C2H4 + C3H5-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.842, 'cm^3/(mol*s)', '*|/', 6),
        n = 3.5,
        Ea = (40.4593, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang [93] literature review.""",
    longDesc =
u"""
[93] Tsang, W. J. Phys. Chem. Ref. Data 1991, 20, 221.
CH3CH=CH2 + C2H3 --> CH3C=CH2 + C2H4

pg 240-241

Previous modified Arrhenius parameters were for RELATIVE rate (kc/ka)

Multiplied kc/ka by ka to get kc (only one H to abstract, so no division necessary)

Certified by MRH on 6Aug2009

Entry 46,19(c): No data available at the time.  The recommended rate coefficient

is based on the rate expressions for CH3 abstracting a H-atom from C3H6; all of
the Ea's have been decreased by 4kJ/mol.
MRH 31-Aug-2009

Converted to training reaction from rate rule: Cd/H/NonDeC;Cd_pri_rad
""",
)

entry(
    index = 350,
    label = "C2H + C3H6-2 <=> C2H2 + C3H5-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.21e+12, 'cm^3/(mol*s)', '*|/', 5),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang [93] literature review.""",
    longDesc =
u"""
[93] Tsang, W. J. Phys. Chem. Ref. Data 1991, 20, 221.
CH3CH=CH2 + C2H --> CH3C=CH2 + C2H2

pg 241

Verified by MRH on 6Aug2009

Entry 46,21(e): No data available at the time.  Recommended rate expression is "somewhat

smaller" than the rate of rxn C3H6+C2H --> C2H2+H2C=CH-*CH2.  The rate of this rxn
is assumed to be the rate of the rxn C2H+C2H6 --> C2H2+C2H5.
MRH 31-Aug-2009

Converted to training reaction from rate rule: Cd/H/NonDeC;Ct_rad
""",
)

entry(
    index = 351,
    label = "OH_r3 + C3H6-2 <=> H2O_p23 + C3H5-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.11e+06, 'cm^3/(mol*s)', '*|/', 2),
        n = 2,
        Ea = (109.704, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang [93] literature review.""",
    longDesc =
u"""
[93] Tsang, W. J. Phys. Chem. Ref. Data 1991, 20, 221.
CH3CH=CH2 + OH --> CH3C=CH2 + H2O

pg 235-236

Valid T range in reference suggested 700-2500K

Uncertainty stated in reference was *2.0

Verified by MRH on 6Aug2009

Entry 46,6(d): No direct measurements of H-atom abstraction rxns.  The recommended

H-atom abstraction rxns are based on "the results of Tully (1988) for the rxn
of OH + C2H4 and the rate constant ratio of OH + primary Hydrogens in ethane by
Tully et al. (1986) to OH + secondary Hydrogens by Droege and Tully (1986)".  The
author has also introduced a T^2 dependence in the A-factor.
MRH 31-Aug-2009

Converted to training reaction from rate rule: Cd/H/NonDeC;O_pri_rad
""",
)


entry(
    index = 353,
    label = "C2H2 + C2H5 <=> C2H6 + C2H",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.72e+11, 'cm^3/(mol*s)', '*|/', 5),
        n = 0,
        Ea = (174.389, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc =
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
C2H2 + C2H5 --> C2H + C2H6 C.D.W divided original rate expression by 2 (from A= 2.71E+11), to get rate expression per H atom.

pg 1100, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 20,17.

Verified by Karma James

pg. 1215: Discussion on evaluated data

Recommended data based on reverse rate and equilibrium constant

MRH 28-Aug-2009

Converted to training reaction from rate rule: Ct_H;C_rad/H2/Cs
""",
)

entry(
    index = 354,
    label = "OH_r3 + C2H2 <=> H2O_p23 + C2H",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (14500, 'cm^3/(mol*s)', '*|/', 10),
        n = 2.68,
        Ea = (213.593, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc =
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
C2H2 + OH --> C2H + H2O C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 1100, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 20,6.

Verified by Karma James

pg. 1213: Discussion on evaluated data

Recommended data is derived from BEBO method calculation

MRH 28-Aug-2009

Converted to training reaction from rate rule: Ct_H;O_pri_rad
""",
)

entry(
    index = 358,
    label = "OH_r3 + C6H6 <=> H2O_p23 + C6H5",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (1.632e+08, 'cm^3/(mol*s)', '*|/', 2),
        n = 1.42,
        Ea = (124.516, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (400, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Baulch et al. [95] literature review.""",
    longDesc =
u"""
[95] Baulch, D.L.; Cobos, C.J.; Cox, R.A.; Esser, C.; Frank, P.; Just, T.; Kerr, J.A.; Pilling, M.J.;
Troe, J.; Walker, R.W.; Warnatz, J. J. Phys. Chem. Ref. Data 1992, 21, 411.

Benzene + OH --> phenyl + H2O  C.D.W divided original rate expression by 6(from A = 1.63E+08), to get rate expression per H atom.

pg 420 Evaluated Kinetic Data for Combustion Modelling, Table 1. Bimolecular reactions - OH Radical Reactions.

Verified by Karma James

pg.595-597: Discussion on evaluated data

OH+C6H6 --> H2O+C6H5: Authors note that this rxn should be dominant at temperatures

above 500K.  No other comment on where the recommended rate expression comes from
(although MRH believes it is a best-fit to the available data, based on graph).
MRH 31-Aug-2009

Converted to training reaction from rate rule: Cb_H;O_pri_rad
""",
)

entry(
    index = 359,
    label = "CH2O + O2 <=> HO2_r12 + HCO_r3",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (9.36e+07, 'cm^3/(mol*s)'),
        n = 2.05,
        Ea = (158.699, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2200, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Michael et al. [132] Transition state theory.""",
    longDesc =
u"""
[132] Michael, J.V.; Kumaran, S.S.; Su, M.-C. J. Phys. Chem. A. 1999, 103, 5942.
CH2O + O2 --> HCO + HO2 C.D.W divided original rate expression by 2, to get rate expression per H atom.

Converted to training reaction from rate rule: CO_pri;O2b
""",
)

entry(
    index = 360,
    label = "CH2O + O_rad <=> HO + HCO_r3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (4.16e+11, 'cm^3/(mol*s)', '*|/', 2),
        n = 0.57,
        Ea = (11.5478, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (250, 'K'),
        Tmax = (2200, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Baulch et al. [95] literature review.""",
    longDesc =
u"""
[95] Baulch, D.L.; Cobos, C.J.; Cox, R.A.; Esser, C.; Frank, P.; Just, T.; Kerr, J.A.; Pilling, M.J.;
Troe, J.; Walker, R.W.; Warnatz, J. J. Phys. Chem. Ref. Data 1992, 21, 411.

CH2O + O --> HCO + OH C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 416 Evaluated Kinetic Data for Combustion Modelling, Table 1. Bimolecular reactions - O Atom Reactions.

Verified by Karma James

pg.449-450: Discussion on evaluated data

O+CH2O --> OH+HCO: "The preferred values are based on the low temperature data which are

all in good agreement, and on the higher temperature value of Bowman."
MRH 31-Aug-2009

Converted to training reaction from rate rule: CO_pri;O_atom_triplet
""",
)

entry(
    index = 361,
    label = "CH2 + CH2O <=> CH3_p23 + CHO_p1",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (6.04e+09, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc =
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
Rate constant is an upper limit. CH2O + CH2 --> HCO + CH3

C.D.W divided original rate expression by 2 (from A= 6.03E+09), to get rate expression per H atom.

pg 1106, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 26,12.

Verified by Karma James

pg. 1267: Discussion on evaluated data

Recommended data based on triplet methylene's general lack of reactivity in H-atom abstractions

NOTE: Rate coefficient is an upper limit
MRH 28-Aug-2009

Converted to training reaction from rate rule: CO_pri;CH2_triplet
""",
)

entry(
    index = 362,
    label = "CH3_r3 + CH2O <=> CH4_p23 + HCO_r3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (7.78e-08, 'cm^3/(mol*s)', '*|/', 1.58),
        n = 6.1,
        Ea = (8.24248, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Baulch et al. [94] literature review.""",
    longDesc =
u"""
[94] Baulch, D.L.; Cobos, C.J.; Cox, R.A.; Frank, P.; Hayman, G,; Just, T.; Kerr, J.A.; Murrells, T.; Pilling, M.J.;
Troe, J.; Walker, R.W.; Warnatz, J. J. Phys. Chem. Ref. Data 1994, 23, 847.

CH2O + CH3 --> HCO + CH4 C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 862 Evaluated Kinetic Data for Combustion Modelling Supplement 1, Table 1. Bimolecular reactions - CH3 Radical Reactions.

Verified by Karma James

pg.989-990: Discussion on evaluated data

CH3+HCHO --> CH4+HCO: The recommended value is a "best fit to the data of Choudhury et al.,

the reworked data from Anastasi, together with those at lower temperatures from
Refs. 4, 5, and 7."
MRH 31-Aug-2009

Converted to training reaction from rate rule: CO_pri;C_methyl
""",
)

entry(
    index = 363,
    label = "CH2O + C2H5 <=> C2H6 + HCO_r3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (5500, 'cm^3/(mol*s)', '*|/', 5),
        n = 2.81,
        Ea = (24.5182, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc =
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
CH2O + C2H5 --> HCO + C2H6 C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 1096, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 17,12.

Verified by Karma James

pg. 1178: Discussion on evaluated data

Recommended data is the rate of CH2O+CH3-->HCO+CH4.

Authors note that rate coefficients for alkyl radicals w/aldehydic H-atoms are
similar (as noted by Kerr, J.A. and Trotman-Dickenson, A.F.
MRH 28-Aug-2009

Converted to training reaction from rate rule: CO_pri;C_rad/H2/Cs
""",
)

entry(
    index = 364,
    label = "CH2O + C3H7 <=> C3H8 + HCO_r3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.08e+11, 'cm^3/(mol*s)', '*|/', 2.5),
        n = 0,
        Ea = (29.1206, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang [91] literature review.""",
    longDesc =
u"""
[91] Tsang, W. J. Phys. Chem. Ref. Data 1988, 17, 887.
CH2O + iso-C3H7 --> HCO + C3H8 C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 894, Chemical Kinetic Database For Combustion Chemistry, Part 3. Index of Reactions and Summary of Recommended Rate Expressions. No. 42,12.

Verified by Karma James

pg. 936: Discussion on evaluated data

Entry 42,12: No data available at the time.  The author recommends a rate coefficient

expression that is twice that of the rxn i-C3H7+(CH3)2CHCHO, taken from a study
by Kerr, J.A. and Trotman-Dickenson, A.F. (1959).  The author states that a correction
was made to the 1959 report, taking the recommended rate of i-C3H7 recombination
(reported by Tsang) into consideration.
MRH 30-Aug-2009

Converted to training reaction from rate rule: CO_pri;C_rad/H/NonDeC
""",
)

entry(
    index = 365,
    label = "CH2O + C4H9-4 <=> iC4H10b + HCO_r3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.26e+09, 'cm^3/(mol*s)', '*|/', 5),
        n = 0,
        Ea = (14.895, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang [92] literature review.""",
    longDesc =
u"""
[92] Tsang, W. J. Phys. Chem. Ref. Data 1990, 19, 1.
CH2O + tert-C4H9 --> HCO + iso-C4H10 C.D.W divided original rate expression by 2 (from A= 3.25E+09), to get rate expression per H atom.

pg 7, Chemical Kinetic Database For Combustion Chemistry, Part 4 - Isobutane.

Index of Reactions and Summary of Recommended Rate Expressions. No. 44,12.

Verified by Karma James

pg.35: Discussion on evaluated data

Entry 44,12: No data available at the time.  The author recommends 2x the rate coefficient

of the rxn tC4H9+tC4H9-CHO=iC4H10+tC4H9-CO (2 vs. 1 aldehydic H-atoms); this value
was reported by Birrell and Trotman-Dickenson.  The author also notes that he has
taken into account tC4H9 combination (perhaps meaning he used a geometric mean rule
to derive the final form of the expression?)
MRH 31-Aug-2009

Converted to training reaction from rate rule: CO_pri;C_rad/Cs3
""",
)

entry(
    index = 366,
    label = "C2H3 + CH2O <=> C2H4 + HCO_r3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (5420, 'cm^3/(mol*s)', '*|/', 5),
        n = 2.81,
        Ea = (24.5182, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc =
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
CH2O + C2H3 --> HCO + C2H4 C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 1099, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 19,12.

Verified by Karma James

pg. 1197: Discussion on evaluated data

Recommended data is the rate of CH2O+CH3-->HCO+CH4.

Authors note that rate coefficients for alkyl radicals w/aldehydic H-atoms are
similar (as noted by Kerr, J.A. and Trotman-Dickenson, A.F.
MRH 28-Aug-2009

Converted to training reaction from rate rule: CO_pri;Cd_pri_rad
""",
)

entry(
    index = 367,
    label = "CH2O + C2H3O <=> C2H4O + HCO_r3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.81e+11, 'cm^3/(mol*s)', '*|/', 10),
        n = 0,
        Ea = (54.0573, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc =
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
CH2O + CH3CO --> HCO + CH3CHO C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 1102, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 22,12.

Verified by Karma James

pg. 1231: Discussion on evaluated data

Recommended data based on "analogous systems"

MRH 28-Aug-2009

Converted to training reaction from rate rule: CO_pri;CO_rad/NonDe
""",
)

entry(
    index = 368,
    label = "OH_r3 + CH2O <=> H2O_p23 + HCO_r3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.44e+09, 'cm^3/(mol*s)', '*|/', 5),
        n = 1.18,
        Ea = (-1.8828, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Baulch et al. [95] literature review.""",
    longDesc =
u"""
[95] Baulch, D.L.; Cobos, C.J.; Cox, R.A.; Esser, C.; Frank, P.; Just, T.; Kerr, J.A.; Pilling, M.J.;
Troe, J.; Walker, R.W.; Warnatz, J. J. Phys. Chem. Ref. Data 1992, 21, 411.

CH2O + OH --> HCO + H2O C.D.W divided original rate expression by 2 (from A= 3.43E+09), to get rate expression per H atom.

pg 419 Evaluated Kinetic Data for Combustion Modelling, Table 1. Bimolecular reactions - OH Radical Reactions.

Verified by Karma James

pg.575-576: Discussion on evaluated data

OH+CH2O --> H2O+HCO: The recommended rate coefficient is the value reported by Tsang

and Hampson.
MRH 31-Aug-2009

Converted to training reaction from rate rule: CO_pri;O_pri_rad
""",
)

entry(
    index = 369,
    label = "CH2O + CH3O-2 <=> CH4O-2 + HCO_r3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.02e+11, 'cm^3/(mol*s)', '*|/', 3),
        n = 0,
        Ea = (12.4683, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc =
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
CH2O + CH3O --> HCO + CH3OH C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 1104, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 24,12.

Verified by Karma James

pg. 1245: Discussion on evaluated data

Recommended data based on review by Gray, based on experiments performed by Hoare and Wellington.

Authors note that experimental conditions were such that rxn of interest was
in competition with the disproportionation of two CH3O radicals (CH3O+CH3O-->CH3OH+CH2O)
MRH 28-Aug-2009

Converted to training reaction from rate rule: CO_pri;O_rad/NonDeC
""",
)

entry(
    index = 370,
    label = "HO2_r3 + CH2O <=> H2O2 + HCO_r3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (41200, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (42.7186, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (641, 'K'),
        Tmax = (1600, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Eiteneer et al. [133] literature review.""",
    longDesc =
u"""
[133] Eiteneer, B.; Yu, C.-L.; Goldenberg, M.; Frenklach, M. J. Phys. Chem. A. 1998, 102, 5196.
CH2O + HO2 --> HCO + H2O2 C.D.W divided original rate expression by 2 (from A= 4.11E+04), to get rate expression per H atom.

Converted to training reaction from rate rule: CO_pri;O_rad/NonDeO
""",
)

entry(
    index = 371,
    label = "C2H4O + O2 <=> HO2_r12 + C2H3O",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (6.02e+13, 'cm^3/(mol*s)', '*|/', 10),
        n = 0,
        Ea = (163.804, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (1100, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Baulch et al. [95] literature review.""",
    longDesc =
u"""
[95] Baulch, D.L.; Cobos, C.J.; Cox, R.A.; Esser, C.; Frank, P.; Just, T.; Kerr, J.A.; Pilling, M.J.;
Troe, J.; Walker, R.W.; Warnatz, J. J. Phys. Chem. Ref. Data 1992, 21, 411.

CH3CHO + O2 --> CH3CO + HO2

pg 417 Evaluated Kinetic Data for Combustion Modelling, Table 1. Bimolecular reactions - O2 Reactions.

Verified by Karma James

pg.485: Discussion on evaluated data

O2+CH3CHO --> HO2+CH3CO: "For this evaluation we prefer the approach of Walker and

the recommended value is based on the best current deltaH298 value (=163.8 kJ/mol
using deltaHf(CH3CO)=11.0 kJ/mol and deltaHf(HO2)=14.6 kJ/mol) and A=5.0x10^-11
cm3/molecule/s."
MRH 31-Aug-2009

Converted to training reaction from rate rule: CO/H/NonDe;O2b
""",
)

entry(
    index = 372,
    label = "C2H4O + O_rad <=> HO + C2H3O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5e+12, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (7.48936, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Warnatz [134] literature review""",
    longDesc =
u"""
[134] Warnatz, J. Rate coefficeints in the C/H/O system. In Combustion Chemistry, 1984; pp 197.
CH3CHO + O --> CH3CO + OH

Converted to training reaction from rate rule: CO/H/NonDe;O_atom_triplet
""",
)

entry(
    index = 375,
    label = "C3H5 + C2H4O <=> C3H6 + C2H3O",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (7.6e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (30.1666, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (790, 'K'),
        Tmax = (810, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Loser et al. [135] bond strength-bond length method.""",
    longDesc =
u"""
[135] Loser, U.; Scherzer, K.; Weber, K. Z. Phys. Chem. (Leipzig) 1989, 270, 237.
CH3CHO + CH2CH=CH2 --> CH3CO + CH3CH=CH2

Converted to training reaction from rate rule: CO/H/NonDe;C_rad/H2/Cd
""",
)

entry(
    index = 376,
    label = "C2H3 + C2H4O <=> C2H4 + C2H3O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.13e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (15.3971, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (480, 'K'),
        Tmax = (520, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Scherzer et al. [136] bond energy-bond order method.""",
    longDesc =
u"""
[136] Scherzer, K.; Loser, U.; Stiller, W. Z. Phys. Chem. 1987, 27, 300.
CH3CHO + C2H3 --> CH3CO + C2H4

Converted to training reaction from rate rule: CO/H/NonDe;Cd_pri_rad
""",
)

entry(
    index = 379,
    label = "H2O_r12 + O2 <=> HO2_r12 + OH_p1",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (9.3e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (310.118, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1000, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Mayer et al. [137] Bond energy-bond order.""",
    longDesc =
u"""
[137] Mayer, S.W.; Schieler, L. J. Phys. Chem. 1968, 72, 2628.
http://dx.doi.org/10.1021/j100853a066

H2O + O2 --> OH + HO2.
C.D.W divided original rate expression by 2, to get rate expression per H atom.

Converted to training reaction from rate rule: O_pri;O2b
""",
)

entry(
    index = 380,
    label = "H2O_r12 + O_rad <=> HO + OH_p1",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (5.26e+09, 'cm^3/(mol*s)'),
        n = 1.2,
        Ea = (74.6007, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Karach et al. [138] Transition state theory.""",
    longDesc =
u"""
[138] Karach, S.P.; Oscherov, V.I. J. Phys. Chem. 1999, 110, 11918.
H2O + O --> OH + OH. C.D.W divided original rate expression by 2 (from A= 2.95E+39), to get rate expression per H atom.

Converted to training reaction from rate rule: O_pri;O_atom_triplet
""",
)

entry(
    index = 385,
    label = "H2O_r12 + HCO_r3 <=> CH2O + OH_p1",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.36e+08, 'cm^3/(mol*s)', '*|/', 5),
        n = 1.35,
        Ea = (120.792, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc =
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
H2O + HCO --> OH + CH2O. C.D.W divided original rate expression by 2 (from A= 2.35E+08), to get rate expression per H atom.

pg 1094, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 15,9.

Verified by Karma James

pg. 1150: Discussion on evaluated data

Recommended data based on reverse rate and equilibrium constant

MRH 28-Aug-2009

Converted to training reaction from rate rule: O_pri;CO_pri_rad
""",
)

entry(
    index = 387,
    label = "CH4O-2 + O_rad <=> HO + CH3O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)', '*|/', 2.51),
        n = 0,
        Ea = (21.3227, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Warnatz [134] literature review""",
    longDesc =
u"""
[134] Warnatz, J. Rate coefficeints in the C/H/O system. In Combustion Chemistry, 1984; pp 197.
CH3OH + O --> CH3O + OH

Converted to training reaction from rate rule: O/H/NonDeC;O_atom_triplet
""",
)

entry(
    index = 388,
    label = "CH2 + CH4O-2 <=> CH3_p23 + CH3O_p1",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (14.4, 'cm^3/(mol*s)', '*|/', 3),
        n = 3.1,
        Ea = (29.037, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang [90] literature review.""",
    longDesc =
u"""
[90] Tsang, W. J. Phys. Chem. Ref. Data 1987, 16, 471.
CH3OH + CH2 --> CH3O + CH3

pg 475, Chemical Kinetic Database For Combustion Chemistry, Part 2 - Methanol.

//Index of Reactions and Summary of Recommended Rate Expressions. No. 38,25.

Verified by Karma James

Data for Rate Expression 38,26 (pg. 493)

Stated uncertainty factor is 3

Verified by MRH on 11Aug2009

Entry 38,26 (b): No data available at the time.  Author suggests the rate coefficient

expression for CH3+CH3OH=CH4+CH3O
MRH 30-Aug-2009

Converted to training reaction from rate rule: O/H/NonDeC;CH2_triplet
""",
)

entry(
    index = 389,
    label = "CH4O-2 + CH3_r3 <=> CH4_p23 + CH3O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.00037, 'cm^3/(mol*s)'),
        n = 4.7,
        Ea = (24.1835, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Jodkowski et al. [100] ab initio calculations.""",
    longDesc =
u"""
[100] Jodkowski, J.T.; Rauez, M.-T.; Rayez, J.-C. J. Phys. Chem. A. 1999, 103, 3750.
The calculated rate constants are in good agreement with experiment. CH3OH + CH3 --> CH3O + CH4 (Rxn. R3 from paper)

Verified by Greg Magoon: I changed upper temperature to 2000 K (was 2500) in line with other reactions from same paper; note that according to the paper, this reaction is very slightly endothermic; the exothermic reverse (-R3) is included above as #177

Converted to training reaction from rate rule: O/H/NonDeC;C_methyl
""",
)

entry(
    index = 390,
    label = "CH4O-2 + C2H5 <=> C2H6 + CH3O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (14.4, 'cm^3/(mol*s)', '*|/', 3),
        n = 3.1,
        Ea = (37.405, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang [90] literature review.""",
    longDesc =
u"""
[90] Tsang, W. J. Phys. Chem. Ref. Data 1987, 16, 471.
CH3OH + C2H5 --> CH3O + C2H6

pg 475, Chemical Kinetic Database For Combustion Chemistry, Part 2 - Methanol.

Index of Reactions and Summary of Recommended Rate Expressions. No. 38,17.

Verified by Karma James

pg. 489: Discussion on evaluated data

Entry 38,17 (b): No data available at the time.  Author notes ethyl radicals are known

to be considerably less reactive than methyl.  Author recommends the rate coefficient
expression of CH3+CH3OH=CH4+CH3O, with a slight adjustment (based on the observed
trends in methyl vs. ethyl radical reactivity with hydrocarbons).
MRH 30-Aug-2009

//263: [90] Tsang, W. J. Phys. Chem. Ref. Data 1987, 16, 471.

Converted to training reaction from rate rule: O/H/NonDeC;C_rad/H2/Cs
""",
)

entry(
    index = 391,
    label = "CH4O-2 + C3H7 <=> C3H8 + CH3O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (14.5, 'cm^3/(mol*s)', '*|/', 5),
        n = 3.1,
        Ea = (43.2207, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang [91] literature review.""",
    longDesc =
u"""
[91] Tsang, W. J. Phys. Chem. Ref. Data 1988, 17, 887.
CH3OH + iso-C3H7 --> CH3O + C3H8

//WAS UNABLE TO VERIFY DATA!!! DATA NOT FOUND IN REFERENCE.

Ref[90] was incorrect; rate matches that reported in Ref[91].

pg. 944: Discussion on evaluated data

Entry 42,38 (b)

No experimental data, at the time

Recommended rate is based on C2H5+CH3OH=C2H6+CH3O

Verified by MRH on 10Aug2009

MRH 30-Aug-2009

//264: [90] Tsang, W. J. Phys. Chem. Ref. Data 1987, 16, 471.

Converted to training reaction from rate rule: O/H/NonDeC;C_rad/H/NonDeC
""",
)

entry(
    index = 392,
    label = "CH4O-2 + C4H9-4 <=> iC4H10b + CH3O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1510, 'cm^3/(mol*s)', '*|/', 10),
        n = 1.8,
        Ea = (39.1622, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang [92] literature review.""",
    longDesc =
u"""
[92] Tsang, W. J. Phys. Chem. Ref. Data 1990, 19, 1.
CH3OH + tert-C4H9 --> CH3O + iso-C4H10

//WAS UNABLE TO VERIFY DATA!!! DATA NOT FOUND IN REFERENCE.

Ref[90] was incorrect; rate matches that reported in Ref[92].

pg.44: Discussion on evaluated data

Entry 44,38(b)

Reference reports reaction as: t-C4H9+CH3OH=t-C4H10+CH3O

This is a typo: no t-C4H10 molecule exists (should be i-C4H10)
No experimental data, at the time

Recommended rate is based on reverse rxn and equilibrium constant

Verified by MRH on 10Aug2009

Converted to training reaction from rate rule: O/H/NonDeC;C_rad/Cs3
""",
)

entry(
    index = 393,
    label = "C2H3 + CH4O-2 <=> C2H4 + CH3O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (14.4, 'cm^3/(mol*s)', '*|/', 10),
        n = 3.1,
        Ea = (29.037, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang [90] literature review.""",
    longDesc =
u"""
[90] Tsang, W. J. Phys. Chem. Ref. Data 1987, 16, 471.
CH3OH + C2H3 --> CH3O + C2H4

pg 475, Chemical Kinetic Database For Combustion Chemistry, Part 2 - Methanol.

Index of Reactions and Summary of Recommended Rate Expressions. No. 38,19.

Verified by Karma James

pg. 489: Discussion on evaluated data

Entry 38,19 (b): No data available at the time.  Author recommends the rate coefficient

expression for CH3+CH3OH=CH4+CH3O.
MRH 30-Aug-2009

Converted to training reaction from rate rule: O/H/NonDeC;Cd_pri_rad
""",
)

entry(
    index = 394,
    label = "C2H + CH4O-2 <=> C2H2 + CH3O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.21e+12, 'cm^3/(mol*s)', '*|/', 5),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang [90] literature review.""",
    longDesc =
u"""
[90] Tsang, W. J. Phys. Chem. Ref. Data 1987, 16, 471.
CH3OH + C2H --> CH3O + C2H2

pg 475, Chemical Kinetic Database For Combustion Chemistry, Part 2 - Methanol.

Index of Reactions and Summary of Recommended Rate Expressions. No. 38,21.

Verified by Karma James

pg. 490: Discussion on evaluated data

Entry 38,21 (b): No data available at the time.  Author recommends a rate coefficient

expression based on measurements of C2H+CH4 and C2H+C2H6 rxns
MRH 30-Aug-2009

Converted to training reaction from rate rule: O/H/NonDeC;Ct_rad
""",
)

entry(
    index = 396,
    label = "H2O2 + C4H9O <=> C4H10O + HO2_r3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (5.76, 'cm^3/(mol*s)'),
        n = 3.16,
        Ea = (3.138, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
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
The computed pre-exponential factor was divided by 2 and this is the reported value.

For nButanol+HO2=H2O2+*CH2CH2CH2CH2OH:
Moc et al. (AIP Conference Proceedings (2009) 1148 161-164 "The Unimolecular Decomposition
and H Abstraction Reactions by HO and HO2 from n-Butanol") report reaction barriers and
enthalpies(0 K); our CBS-QB3 calculations are shown in comparison (all units are kcal/mol).
				G3		CCSD(T)/cc-pVTZ		CBS-QB3
Barrier:		18.8		19.62			17.57
Enthalpy:		14.25		14.66			13.70

Converted to training reaction from rate rule: H2O2;C_rad/H2/Cs\H2\Cs|Cs#O
""",
)

entry(
    index = 397,
    label = "H2O2 + C4H9O-2 <=> C4H10O-2 + HO2_r3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.35, 'cm^3/(mol*s)'),
        n = 3.42,
        Ea = (5.98312, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
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
The computed pre-exponential factor was divided by 2 and this is the reported value.

For nButanol+HO2=H2O2+CH3*CHCH2CH2OH:
Moc et al. (AIP Conference Proceedings (2009) 1148 161-164 "The Unimolecular Decomposition
and H Abstraction Reactions by HO and HO2 from n-Butanol") report reaction barriers and
enthalpies(0 K); our CBS-QB3 calculations are shown in comparison (all units are kcal/mol).
				G3		CCSD(T)/cc-pVTZ		CBS-QB3
Barrier:		14.64		15.47			14.72
Enthalpy:		11.05		12.41			10.11

Converted to training reaction from rate rule: H2O2;C_rad/H/Cs\H2\Cs|O/Cs
""",
)

entry(
    index = 398,
    label = "H2O2 + C4H9O-3 <=> C4H10O-3 + HO2_r3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.629, 'cm^3/(mol*s)'),
        n = 3.52,
        Ea = (6.73624, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
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
The computed pre-exponential factor was divided by 2 and this is the reported value.

For nButanol+HO2=H2O2+CH3CH2*CHCH2OH:
Moc et al. (AIP Conference Proceedings (2009) 1148 161-164 "The Unimolecular Decomposition
and H Abstraction Reactions by HO and HO2 from n-Butanol") report reaction barriers and
enthalpies(0 K); our CBS-QB3 calculations are shown in comparison (all units are kcal/mol).
				G3		CCSD(T)/cc-pVTZ		CBS-QB3
Barrier:		15.43		16.37			16.33
Enthalpy:		13.53		14.02			11.48

Converted to training reaction from rate rule: H2O2;C_rad/H/Cs\H2\Cs/Cs\H2\O
""",
)

entry(
    index = 399,
    label = "H2O2 + C4H9O-4 <=> C4H10O-4 + HO2_r3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.97, 'cm^3/(mol*s)'),
        n = 3.39,
        Ea = (7.3132, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
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
The computed pre-exponential factor was divided by 2 and this is the reported value.

For nButanol+HO2=H2O2+CH3CH2CH2*CHOH:
Moc et al. (AIP Conference Proceedings (2009) 1148 161-164 "The Unimolecular Decomposition
and H Abstraction Reactions by HO and HO2 from n-Butanol") report reaction barriers and
enthalpies(0 K); our CBS-QB3 calculations are shown in comparison (all units are kcal/mol).
				G3		CCSD(T)/cc-pVTZ		CBS-QB3
Barrier:		12.62		13.23			11.74
Enthalpy:		 8.35		 8.63			 7.17

Converted to training reaction from rate rule: H2O2;C_rad/H/Cs\H2\Cs|H2|Cs/O
""",
)

entry(
    index = 400,
    label = "H2O2 + C4H9O-5 <=> C4H10O-5 + HO2_r3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (11.5, 'cm^3/(mol*s)'),
        n = 2.94,
        Ea = (1.92464, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
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
The computed pre-exponential factor was divided by 2 and this is the reported value.

Converted to training reaction from rate rule: H2O2;C_rad/H2/Cs\H2\Cs|Cs|O
""",
)

entry(
    index = 401,
    label = "H2O2 + C4H9O-6 <=> C4H10O-6 + HO2_r3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.75, 'cm^3/(mol*s)'),
        n = 2.91,
        Ea = (-1.71544, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
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
The computed pre-exponential factor was divided by 2 and this is the reported value.

Converted to training reaction from rate rule: H2O2;C_rad/H/Cs\H\Cs\O/Cs
""",
)

entry(
    index = 402,
    label = "H2O2 + C4H9O-7 <=> C4H10O-7 + HO2_r3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (34.6, 'cm^3/(mol*s)'),
        n = 3.05,
        Ea = (4.26768, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
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
The computed pre-exponential factor was divided by 2 and this is the reported value.

Converted to training reaction from rate rule: H2O2;C_rad/O/Cs/Cs\Cs
""",
)

entry(
    index = 403,
    label = "H2O2 + C4H9O-12 <=> C4H10O-12 + HO2_r3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.611, 'cm^3/(mol*s)'),
        n = 3.53,
        Ea = (6.35968, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
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
The computed pre-exponential factor was divided by 2 and this is the reported value.

Converted to training reaction from rate rule: H2O2;C_rad/H2/Cs\H\Cs\Cs|O
""",
)

entry(
    index = 404,
    label = "H2O2 + C4H9O-9 <=> C4H10O-9 + HO2_r3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.42, 'cm^3/(mol*s)'),
        n = 3.53,
        Ea = (6.52704, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
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
The computed pre-exponential factor was divided by 2 and this is the reported value.

Converted to training reaction from rate rule: H2O2;C_rad/H2/Cs\Cs2\O
""",
)

entry(
    index = 405,
    label = "HO2_r3 + HO2_r12 <=> H2O2 + O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.75e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-13.7026, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""[8] Curran's estimation in reaction type 13, RO2 + HO2 --> RO2H + O2""",
    longDesc =
u"""
Converted to training reaction from rate rule: Orad_O_H;O_rad/NonDeO
""",
)

entry(
    index = 406,
    label = "CH2O + C4H7 <=> C4H8 + HCO_r3",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (0.1226, 'cm^3/(mol*s)'),
        n = 3.95,
        Ea = (51.1285, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
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
The computed pre-exponential factor was divided by 2 (symmetry of CH2O), from 6.13e-02 to 3.065e-02.

There are no rate coefficients for this reaction in the literature (based on MRH's limited search).
   Tsang {J. Phys. Chem. Ref. Data 20 (1991) 221-273} recommends the following for the reaction of
   CH2O + H2C=CH-*CH2 = HCO + H2C=CH-CH3: k(T) = 1.26e+08 * T^1.9 * exp(-18.184 kcal/mol / RT) cm3 mol-1 s-1.
   This rate coefficient is 25-85x faster than MRH's calculation over the range 600-2000K.

   The previous estimate by RMG for this reaction was: k(T) = 5.500e+03 * T^2.81 * exp(-5.86 kcal/mol / RT) cm3 mol-1 s-1.
   This rate coefficient is 80-13,000x faster than MRH's calculation over the range 600-2000K.

Converted to training reaction from rate rule: CO_pri;C_rad/H2/Cd\Cs_Cd\H2
""",
)

entry(
    index = 407,
    label = "C4H9O-10 + C3H8 <=> C4H10O-10 + C3H7",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.822e-06, 'cm^3/(mol*s)'),
        n = 5.11,
        Ea = (29.8373, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc =
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.  Pre-exponential was divided by 2 to get per-H value.

InChI=1/C3H8/c1-3-2/h3H2,1-2H3 (external symmetry number = 2, spin multiplicity = 1)
 +
InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C3H7/c1-3-2/h3H,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)

Converted to training reaction from rate rule: C/H2/Cs\H3/Cs\H3;C_rad/Cs2/Cs\O
""",
)

entry(
    index = 408,
    label = "C4H10O-11 + C3H7 <=> C3H8 + C4H9O-11",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.12e-06, 'cm^3/(mol*s)'),
        n = 5.06,
        Ea = (20.4598, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc =
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.  Pre-exponential was divided by 2 to get per-H value.

InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)
 +
InChI=1/C3H7/c1-3-2/h3H,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C3H8/c1-3-2/h3H2,1-2H3 (external symmetry number = 2, spin multiplicity = 1)

Converted to training reaction from rate rule: C/H2/Cs\Cs2/O;C_rad/H/Cs\H3/Cs\H3
""",
)

entry(
    index = 409,
    label = "C4H9O-12 + C4H8 <=> C4H10O-12 + C4H7",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (5.034e-05, 'cm^3/(mol*s)'),
        n = 4.89,
        Ea = (18.0749, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc =
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.  Pre-exponential was divided by 6 to get per-H value.

InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3 (external symmetry number = 2, spin multiplicity = 1)
 +
InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)

Converted to training reaction from rate rule: C/H3/Cd\Cs_Cd\H2;C_rad/H2/Cs\H\Cs\Cs|O
""",
)

entry(
    index = 410,
    label = "C4H9O-10 + C4H8 <=> C4H10O-10 + C4H7",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (8.64e-05, 'cm^3/(mol*s)'),
        n = 4.52,
        Ea = (6.10864, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc =
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.  Pre-exponential was divided by 6 to get per-H value.

InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3 (external symmetry number = 2, spin multiplicity = 1)
 +
InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)

Converted to training reaction from rate rule: C/H3/Cd\Cs_Cd\H2;C_rad/Cs2/Cs\O
""",
)

entry(
    index = 411,
    label = "C4H9O-11 + C4H8 <=> C4H10O-11 + C4H7",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (2.946e-05, 'cm^3/(mol*s)'),
        n = 5.07,
        Ea = (15.3134, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc =
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.  Pre-exponential was divided by 6 to get per-H value.

InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3 (external symmetry number = 2, spin multiplicity = 1)
 +
InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)

Converted to training reaction from rate rule: C/H3/Cd\Cs_Cd\H2;C_rad/H/Cs\H\Cs2/O
""",
)

entry(
    index = 412,
    label = "C4H8 + C4H9O-13 <=> C4H10O-13 + C4H7",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (3.498, 'cm^3/(mol*s)'),
        n = 3.74,
        Ea = (6.0668, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc =
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.  Pre-exponential was divided by 6 to get per-H value.

InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3 (external symmetry number = 2, spin multiplicity = 1)
 +
InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)

Converted to training reaction from rate rule: C/H3/Cd\Cs_Cd\H2;O_rad/Cs\H2\Cs|H|Cs2
""",
)

entry(
    index = 413,
    label = "C4H9O-12 + C3H6 <=> C4H10O-12 + C3H5",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (0.0001008, 'cm^3/(mol*s)'),
        n = 4.75,
        Ea = (17.2799, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc =
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.  Pre-exponential was divided by 3 to get per-H value.

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

Converted to training reaction from rate rule: C/H3/Cd\H_Cd\H2;C_rad/H2/Cs\H\Cs\Cs|O
""",
)

entry(
    index = 414,
    label = "C4H9O-10 + C3H6 <=> C4H10O-10 + C3H5",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (4.92e-06, 'cm^3/(mol*s)'),
        n = 4.98,
        Ea = (13.3051, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc =
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.  Pre-exponential was divided by 3 to get per-H value.

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

Converted to training reaction from rate rule: C/H3/Cd\H_Cd\H2;C_rad/Cs2/Cs\O
""",
)

entry(
    index = 415,
    label = "C4H9O-11 + C3H6 <=> C4H10O-11 + C3H5",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (9.33e-06, 'cm^3/(mol*s)'),
        n = 4.97,
        Ea = (15.2298, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc =
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.  Pre-exponential was divided by 3 to get per-H value.

InChI=1/C3H6/c1-3-2/h3H,1H2,2H3 (external symmetry number = 1, spin multiplicity = 1)
 +
InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C3H5/c1-3-2/h3H,1-2H2 (external symmetry number = 2, spin multiplicity = 2)
 +
InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)

Converted to training reaction from rate rule: C/H3/Cd\H_Cd\H2;C_rad/H/Cs\H\Cs2/O
""",
)

entry(
    index = 416,
    label = "C3H6 + C4H9O-13 <=> C4H10O-13 + C3H5",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (0.357, 'cm^3/(mol*s)'),
        n = 3.9,
        Ea = (7.57304, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc =
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.  Pre-exponential was divided by 3 to get per-H value.

InChI=1/C3H6/c1-3-2/h3H,1H2,2H3 (external symmetry number = 1, spin multiplicity = 1)
 +
InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C3H5/c1-3-2/h3H,1-2H2 (external symmetry number = 2, spin multiplicity = 2)
 +
InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)

Converted to training reaction from rate rule: C/H3/Cd\H_Cd\H2;O_rad/Cs\H2\Cs|H|Cs2
""",
)

entry(
    index = 417,
    label = "C4H9O-12 + C2H6 <=> C4H10O-12 + C2H5",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (1.926e-05, 'cm^3/(mol*s)'),
        n = 5.28,
        Ea = (32.5515, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc =
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.  Pre-exponential was divided by 6 to get per-H value.

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

Converted to training reaction from rate rule: C/H3/Cs\H3;C_rad/H2/Cs\H\Cs\Cs|O
""",
)

entry(
    index = 418,
    label = "C4H10O-10 + C2H5 <=> C2H6 + C4H9O-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.41e-05, 'cm^3/(mol*s)'),
        n = 4.83,
        Ea = (18.2841, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
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

Converted to training reaction from rate rule: C/H/Cs2/Cs\O;C_rad/H2/Cs\H3
""",
)

entry(
    index = 419,
    label = "C4H10O-11 + C2H5 <=> C2H6 + C4H9O-11",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (8.5e-06, 'cm^3/(mol*s)'),
        n = 5.01,
        Ea = (20.9618, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc =
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.  Pre-exponential was divided by 2 to get per-H value.

InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)
 +
InChI=1/C2H5/c1-2/h1H2,2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C2H6/c1-2/h1-2H3 (external symmetry number = 6, spin multiplicity = 1)

Converted to training reaction from rate rule: C/H2/Cs\Cs2/O;C_rad/H2/Cs\H3
""",
)

entry(
    index = 420,
    label = "C4H9O-13 + C2H6 <=> C4H10O-13 + C2H5",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (0.03042, 'cm^3/(mol*s)'),
        n = 4.52,
        Ea = (18.4854, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc =
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.  Pre-exponential was divided by 6 to get per-H value.

InChI=1/C2H6/c1-2/h1-2H3 (external symmetry number = 6, spin multiplicity = 1)
 +
InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C2H5/c1-2/h1H2,2H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)

Converted to training reaction from rate rule: C/H3/Cs\H3;O_rad/Cs\H2\Cs|H|Cs2
""",
)

entry(
    index = 421,
    label = "C2H3 + C4H10O-10 <=> C2H4 + C4H9O-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.49, 'cm^3/(mol*s)'),
        n = 3.33,
        Ea = (2.63592, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
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

Converted to training reaction from rate rule: C/H/Cs2/Cs\O;Cd_Cd\H2_pri_rad
""",
)

entry(
    index = 422,
    label = "C3H8O + C3H5-2 <=> C3H6-2 + C3H7O",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (9.33e-05, 'cm^3/(mol*s)'),
        n = 4.87,
        Ea = (14.644, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc =
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.  Pre-exponential was divided by 6 to get per-H value.

InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)
 +
InChI=1/C3H5/c1-3-2/h1H2,2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C3H6/c1-3-2/h3H,1H2,2H3 (external symmetry number = 1, spin multiplicity = 1)

Converted to training reaction from rate rule: C/H3/Cs\H2\Cs|O;Cd_Cd\H2_rad/Cs
""",
)

entry(
    index = 423,
    label = "C4H10O-11 + C3H5-2 <=> C3H6-2 + C4H9O-11",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.0256, 'cm^3/(mol*s)'),
        n = 4.09,
        Ea = (5.48104, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc =
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.  Pre-exponential was divided by 2 to get per-H value.

InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)
 +
InChI=1/C3H5/c1-3-2/h1H2,2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C3H6/c1-3-2/h3H,1H2,2H3 (external symmetry number = 1, spin multiplicity = 1)

Converted to training reaction from rate rule: C/H2/Cs\Cs2/O;Cd_Cd\H2_rad/Cs
""",
)

entry(
    index = 424,
    label = "C4H9O-12 + C3H6O <=> C4H10O-12 + C3H5O",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.000312, 'cm^3/(mol*s)'),
        n = 4.31,
        Ea = (14.1838, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc =
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.  Pre-exponential was divided by 2 to get per-H value.

InChI=1/C3H6O/c1-2-3-4/h3H,2H2,1H3 (external symmetry number = 1, spin multiplicity = 1)
 +
InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)

Converted to training reaction from rate rule: C/H2/CO\H/Cs\H3;C_rad/H2/Cs\H\Cs\Cs|O
""",
)

entry(
    index = 425,
    label = "C4H10O-10 + C3H5O <=> C3H6O + C4H9O-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.000485, 'cm^3/(mol*s)'),
        n = 4.37,
        Ea = (40.4174, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
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

Converted to training reaction from rate rule: C/H/Cs2/Cs\O;C_rad/H/CO\H/Cs\H3
""",
)

entry(
    index = 426,
    label = "C4H10O-11 + C3H5O <=> C3H6O + C4H9O-11",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.00368, 'cm^3/(mol*s)'),
        n = 4.02,
        Ea = (33.1373, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc =
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.  Pre-exponential was divided by 2 to get per-H value.

InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3 (external symmetry number = 1, spin multiplicity = 1)
 +
InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C3H6O/c1-2-3-4/h3H,2H2,1H3 (external symmetry number = 1, spin multiplicity = 1)

Converted to training reaction from rate rule: C/H2/Cs\Cs2/O;C_rad/H/CO\H/Cs\H3
""",
)

entry(
    index = 427,
    label = "H + C4H8O <=> H2 + C4H7O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.08e+07, 'cm^3/(mol*s)'),
        n = 1.84,
        Ea = (12.6775, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
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

Converted to training reaction from rate rule: C/H/Cs2CO;H_rad
""",
)

entry(
    index = 428,
    label = "C4H8 + C3H5O-2 <=> C3H6O-2 + C4H7",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (4.512e-07, 'cm^3/(mol*s)'),
        n = 5.77,
        Ea = (72.2118, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""MRH CBS-QB3 calculations w/o HR corrections""",
    longDesc =
u"""
MRH CBS-QB3 calculations w/RRHO [MRHCBSQB3RRHO]_.  Pre-exponential was divided by 6 to get per-H value.

InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3 (external symmetry number = 2, spin multiplicity = 1)
 +
InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3 (external symmetry number = 1, spin multiplicity = 2)
 +
InChI=1/C3H6O/c1-2-3-4/h2-4H,1H3/ (external symmetry number = 1, spin multiplicity = 1)

Converted to training reaction from rate rule: C/H3/Cd\Cs_Cd\H2;O_rad/Cd\H_Cd\H\Cs
""",
)

entry(
    index = 430,
    label = "HO2_r3 + C4H8-2 <=> H2O2 + C4H7-2",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (0.00346998, 'cm^3/(mol*s)'),
        n = 4.65,
        Ea = (40.9195, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""SSM CBS-QB3 calculations w/o HR corrections""",
    longDesc =
u"""
SSM CBS-QB3 calculations w/RRHO .  Pre-exponential was divided by 6 to get per-H value.

InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+ (external symmetry number = 2, spin multiplicity = 1)
 +
HO2 (external symmetry number = 1, spin multiplicity = 2)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H7/c1-3-4-2/h3-4H,1H2,2H3  (external symmetry number = 1, spin multiplicity = 2)
 +
H2O2 (external symmetry number = 2, spin multiplicity = 1)

Converted to training reaction from rate rule: C/H3/Cd\H_Cd\H\Cs;O_rad/NonDeO
""",
)

entry(
    index = 431,
    label = "H2O2 + C3H5-2 <=> C3H6-2 + HO2_r3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.875, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-16.8615, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""SSM due to lack of better value ref rate rule 527""",
    longDesc =
u"""
This rate rules matches C=C*-C + H2O2 <=> C=C-C + HO-O*

Due to lack of better estimate SSM has given this node the value obtained from 2-Butene + HO2 calculations (Rate rule 527)
The rate was calculated using CBS-QB3 w/o hindered rotors and is valid in a range of temperature from 300 -2000 K.
The Wigner tunneling currection that was used to account for tunneling.

Converted to training reaction from rate rule: H2O2;Cd_rad/NonDeC
""",
)

entry(
    index = 432,
    label = "H2O2 + C4H7-3 <=> C4H8-3 + HO2_r3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.875, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-16.8615, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""SSM CBS-QB3 calculations w/o HR corrections""",
    longDesc =
u"""
SSM CBS-QB3 calculations w/RRHO .  Pre-exponential was divided by 2 to account for summetry of H2O2
The rate rule is valid in a range of temperature from 300 -2000 K.
The Wigner tunneling currection that was used to account for tunneling.

InChI=1/C4H7/c1-3-4-2/h3H,1-2H3 (external symmetry number = 1, spin multiplicity = 2)
 +
H2O2 (external symmetry number = 2, spin multiplicity = 1)
 <=> (TS: external symmetry number = 1, spin multiplicity = 2)
InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+  (external symmetry number = 2, spin multiplicity = 1)
 +
HO2 (external symmetry number = 1, spin multiplicity = 2)

Converted to training reaction from rate rule: H2O2;Cd_Cd\H\Cs_rad/Cs
""",
)

entry(
    index = 437,
    label = "CH4_r12 + C2 <=> C2H-2 + CH3_p1",
    degeneracy = 8.0,
    kinetics = Arrhenius(
        A = (6e+13, 'cm^3/(mol*s)', '+|-', 1.6e+12),
        n = 0,
        Ea = (4.3932, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (294, 'K'),
        Tmax = (376, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Matsugi et al 10.1021/jp1012494""",
    longDesc =
u"""
For CH4 + C2 = CH3 + C2H

J. Phys. Chem. A 2010, 114, 4580-4585
http://dx.doi.org/10.1021/jp1012494

Rate Constants and Kinetic Isotope Effects on the Reaction of C2($X^1\Sigma_g^+$) with CH4 and CD4.
Akira Matsugi, Kohsuke Suma, and Akira Miyoshi

It was measured at pretty low temperatures (294-376), but also calculated ab initio. The calculated
rates are plotted but the expression is not reported.

    k = (10.0 +- 2.1)E-11 exp[-(4.4+-0.5 kJ mol)/RT] cm3 molecule-1 s-1
which gives
    A = 6e13+-1.3e13 cm3/mole/s
    n = 0
    Ea = 1.05+-0.12  kcal/mol
The degeneracy of this reaction is 8 though, so per-site A is:
    A = 7.5e12+-1.6e12

(See also  doi:10.1063/1.3480395  for reactions of C2, but that may be the wrong electronic state.)

Converted to training reaction from rate rule: C_methane;C2b
""",
)

entry(
    index = 438,
    label = "H2O2 + C3H5O-2 <=> C3H6O-2 + HO2_r3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.0699, 'cm^3/(mol*s)', '*|/', 3),
        n = 3.75,
        Ea = (117.985, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
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

Converted to training reaction from rate rule: H2O2;O_rad/Cd\H_Cd\H\Cs
""",
)

entry(
    index = 439,
    label = "H2O2 + C2H3O-3 <=> C2H4O-2 + HO2_r3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.0699, 'cm^3/(mol*s)', '*|/', 3),
        n = 3.75,
        Ea = (117.985, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""MHS CBS-QB3 w/1dHR calculations, see node 534.""",
    longDesc =
u"""
Rxn family nodes: H2O2 + O_rad/OneDeC

The rate coefficient for this node was taken from node 534 (H2O2 + InChI=1/C4H7O/c1-2-3-4-5/h3-4H,2H2,1H3)
by analogy: HOOH + *O-C=R.  Discussed with MRH.

Converted to training reaction from rate rule: H2O2;O_rad/OneDe
""",
)

entry(
    index = 441,
    label = "C4H8-4 + CH3O2 <=> CH4O2 + C4H7-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.01482, 'cm^3/(mol*s)', '*|/', 3),
        n = 4.313,
        Ea = (33.5389, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
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
MRH divided the pre-exponential by 2 to account for the reaction path degeneracy.

NOTE: Running PopulateReactions before and after this number produced results that differed by less than a factor
of three.  New numbers in the RMG database thus lead to an improvement in the RMG estimate (RMG works!).  Also,
this computed rate coefficient is a factor of 10 faster than Tsang's recommendation for C3H6 + OOCH3 = HOOCH3 + allyl;
his stated uncertainty is a factor of ten.  However, one would expect abstraction from the secondary carbon of
1-butane to be faster than the primary carbon of propene, because the C-H bond strength should be weaker.  So,
this calculation is in reasonable agreement with the literature.

Converted to training reaction from rate rule: C/H2/Cd\H_Cd\H2/Cs\H3;OOC
""",
)

entry(
    index = 443,
    label = "HO2_r3 + C4H8O-3 <=> H2O2 + C4H7O-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.000191, 'cm^3/(mol*s)', '*|/', 3),
        n = 4.25,
        Ea = (3.38904, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
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

Converted to training reaction from rate rule: CO/H/Cs\Cs|Cs;O_rad/NonDeO
""",
)

entry(
    index = 444,
    label = "OH_r3 + C7H8 <=> H2O_p23 + C7H7",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.26e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (10.8366, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (1000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Tully et al. experimental data (changed to per H)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H3/Cb;O_pri_rad
""",
)

entry(
    index = 445,
    label = "HO2_r3 + C7H8 <=> H2O2 + C7H7",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (3.96e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (58.9107, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (1000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Baulch et al. literature review (value for HO2 + toluene) (changed to per H)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H3/Cb;O_rad/NonDeO
""",
)

entry(
    index = 446,
    label = "HO2_r3 + C8H10 <=> H2O2 + C8H9",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.66e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47.2792, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (1000, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Baulch et al. literature review (value for HO2 + ethylbenzene) (changed to per H)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/CbCs;O_rad/NonDeO
""",
)

entry(
    index = 447,
    label = "HO2_r3 + C9H12 <=> H2O2 + C9H11",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.33e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47.2792, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (1000, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Baulch et al. literature review (value for HO2 + ethylbenzene) (changed to per H)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs2Cb;O_rad/NonDeO
""",
)

entry(
    index = 448,
    label = "C7H8 + O2 <=> HO2_r12 + C7H7",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (3.6e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (166.147, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (1200, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Baulch et al. literature review (value for HO2 + toluene entered here) (changed to per H)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H3/Cb;O2b
""",
)

entry(
    index = 449,
    label = "C8H10 + O2 <=> HO2_r12 + C8H9",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (2.4e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (166.147, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (1200, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Baulch et al. literature review (value for HO2 + toluene entered here) (changed to per H)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/CbCs;O2b
""",
)

entry(
    index = 450,
    label = "C9H12 + O2 <=> HO2_r12 + C9H11",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (166.147, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (1200, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Baulch et al. literature review (value for HO2 + toluene entered here) (changed to per H)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs2Cb;O2b
""",
)

entry(
    index = 451,
    label = "C2H6O2 + C3H7 <=> C3H8 + CH3CH2OO_r3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.51e-11, 'cm^3/(mol*s)'),
        n = 6.77,
        Ea = (-35.9824, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (1000, 'K'),
    ),
    rank = 11,
    shortDesc = u"""[AJ]Assumed to be same as for ROOH_sec""",
    longDesc =
u"""
Converted to training reaction from rate rule: ROOH_pri;C_rad/H/NonDeC
""",
)

entry(
    index = 452,
    label = "C3H8O2 + C3H7 <=> C3H8 + C3H7O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.51e-11, 'cm^3/(mol*s)'),
        n = 6.77,
        Ea = (-35.9824, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (1000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""[AJ]CBS-QB3 calculations with 1DHR corrections, reverse rates computed using DFT_QCI_thermo""",
    longDesc =
u"""
Converted to training reaction from rate rule: ROOH_sec;C_rad/H/NonDeC
""",
)

entry(
    index = 453,
    label = "C2H6O2 + C2H5 <=> C2H6 + CH3CH2OO_r3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.51e-11, 'cm^3/(mol*s)'),
        n = 6.77,
        Ea = (-35.9824, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (1000, 'K'),
    ),
    rank = 11,
    shortDesc = u"""[AJ]Assumed to be same as for C_rad/H/NonDeC""",
    longDesc =
u"""
Converted to training reaction from rate rule: ROOH_pri;C_rad/H2/Cs
""",
)

entry(
    index = 454,
    label = "C3H8O2 + C2H5 <=> C2H6 + C3H7O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.51e-11, 'cm^3/(mol*s)'),
        n = 6.77,
        Ea = (-35.9824, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (1000, 'K'),
    ),
    rank = 11,
    shortDesc = u"""[AJ]Assumed to be same as for C_rad/H/NonDeC""",
    longDesc =
u"""
Converted to training reaction from rate rule: ROOH_sec;C_rad/H2/Cs
""",
)

entry(
    index = 455,
    label = "C3H7O2-2 + C2H6O2 <=> C3H8O2-2 + CH3CH2OO_r3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.066e-14, 'cm^3/(mol*s)'),
        n = 7.18,
        Ea = (-22.0497, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (1000, 'K'),
    ),
    rank = 11,
    shortDesc = u"""[AJ] Assumed to be same as for ROOH_sec""",
    longDesc =
u"""
Converted to training reaction from rate rule: ROOH_pri;C_rad/OOH/Cs/Cs
""",
)

entry(
    index = 456,
    label = "C3H7O2-2 + C3H8O2 <=> C3H8O2-2 + C3H7O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.066e-14, 'cm^3/(mol*s)'),
        n = 7.18,
        Ea = (-22.0497, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (1000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""[AJ] CBS-QB3 calculations with 1DHR corrections""",
    longDesc =
u"""
Converted to training reaction from rate rule: ROOH_sec;C_rad/OOH/Cs/Cs
""",
)

entry(
    index = 457,
    label = "C2H6O2 + C2H3O <=> C2H4O + CH3CH2OO_r3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.0009569, 'cm^3/(mol*s)'),
        n = 4.45,
        Ea = (177.164, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (1000, 'K'),
    ),
    rank = 11,
    shortDesc = u"""[AJ] Assumed to be same as for ROOH_sec""",
    longDesc =
u"""
Converted to training reaction from rate rule: ROOH_pri;CO_rad/NonDe
""",
)

entry(
    index = 458,
    label = "C3H8O2 + C2H3O <=> C2H4O + C3H7O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.0009569, 'cm^3/(mol*s)'),
        n = 4.45,
        Ea = (177.164, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (1000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""[AJ] CBS-QB3 calculations with 1DHR corrections""",
    longDesc =
u"""
Converted to training reaction from rate rule: ROOH_sec;CO_rad/NonDe
""",
)

entry(
    index = 459,
    label = "C2H6O2 + C3H5O <=> C3H6O + CH3CH2OO_r3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.73e-10, 'cm^3/(mol*s)'),
        n = 6.3,
        Ea = (-8.95376, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (1000, 'K'),
    ),
    rank = 11,
    shortDesc = u"""[AJ] Assumed to be same as for ROOH_sec""",
    longDesc =
u"""
Converted to training reaction from rate rule: ROOH_pri;C_rad/H/CO/Cs
""",
)

entry(
    index = 460,
    label = "C3H8O2 + C3H5O <=> C3H6O + C3H7O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.73e-10, 'cm^3/(mol*s)'),
        n = 6.3,
        Ea = (-8.95376, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (1000, 'K'),
    ),
    rank = 11,
    shortDesc = u"""[AJ] Assumed to be same as for C_rad/H2/CO""",
    longDesc =
u"""
Converted to training reaction from rate rule: ROOH_sec;C_rad/H/CO/Cs
""",
)

entry(
    index = 461,
    label = "C2H6O2 + C2H3O-2 <=> CH3CHO_r1 + CH3CH2OO_r3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.73e-10, 'cm^3/(mol*s)'),
        n = 6.3,
        Ea = (-8.95376, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (1000, 'K'),
    ),
    rank = 11,
    shortDesc = u"""[AJ] Assumed to be same as for ROOH_sec""",
    longDesc =
u"""
Converted to training reaction from rate rule: ROOH_pri;C_rad/H2/CO
""",
)

entry(
    index = 462,
    label = "C3H8O2 + C2H3O-2 <=> CH3CHO_r1 + C3H7O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.73e-10, 'cm^3/(mol*s)'),
        n = 6.3,
        Ea = (-8.95376, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (1000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""[AJ] CBS-QB3 calculations with 1DHR corrections""",
    longDesc =
u"""
Converted to training reaction from rate rule: ROOH_sec;C_rad/H2/CO
""",
)

entry(
    index = 463,
    label = "C2H5S + C2H4S <=> C2H6S + C2H3S",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.36e-10, 'cm^3/(mol*s)'),
        n = 4.56,
        Ea = (89.9142, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""CAC CBS-QB3 calc, 1dhr""",
    longDesc =
u"""
Converted to training reaction from rate rule: CS/H/NonDeC;C_rad/H/CsS
""",
)

entry(
    index = 464,
    label = "C2H5 + C2H4S <=> C2H6 + C2H3S",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.377, 'cm^3/(mol*s)'),
        n = 3.63,
        Ea = (77.4877, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""CAC CBS-QB3 calc, 1dhr""",
    longDesc =
u"""
Converted to training reaction from rate rule: CS/H/NonDeC;C_rad/H2/Cs
""",
)

entry(
    index = 465,
    label = "SH + C3H6S <=> H2S_r + C3H5S",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (192.2, 'cm^3/(mol*s)'),
        n = 3.34,
        Ea = (-1.12968, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""CAC CBS-QB3 1dhr""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/CSCs;S_pri_rad
""",
)

entry(
    index = 466,
    label = "CH3_r3 + C3H6S <=> CH4_p23 + C3H5S",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (24.2, 'cm^3/(mol*s)'),
        n = 3.35,
        Ea = (27.8236, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""CAC CBS-QB3 1dhr""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/CSCs;Cs_rad
""",
)

entry(
    index = 467,
    label = "C3H6S-2 + CH3S <=> CH3SH_r1 + C3H5S-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.0376, 'cm^3/(mol*s)'),
        n = 4.57,
        Ea = (16.987, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""CAC CBS-QB3, HO approx""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/CdS;S_rad/NonDeC
""",
)

entry(
    index = 469,
    label = "C4H10O-10 + C3H7 <=> C3H8 + C4H9O-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.35e-06, 'cm^3/(mol*s)'),
        n = 4.84,
        Ea = (17.8657, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
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

Converted to training reaction from rate rule: C/H/Cs2/Cs\O;C_rad/H/Cs\H3/Cs\H3
""",
)

entry(
    index = 470,
    label = "CHS + CH3SH_r1 <=> CH2S + CH3S",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (395, 'cm^3/(mol*s)'),
        n = 3.17,
        Ea = (2.5104, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs""",
    longDesc =
u"""
Converted to training reaction from rate rule: S/H/NonDeC;CS_pri_rad
""",
)

entry(
    index = 471,
    label = "CH2S + CH3_r3 <=> CH4_p23 + CHS_p1",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (166400, 'cm^3/(mol*s)'),
        n = 2.3,
        Ea = (-0.4184, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs""",
    longDesc =
u"""
Converted to training reaction from rate rule: CS_pri;C_methyl
""",
)

entry(
    index = 472,
    label = "OH_r3 + H2S_r <=> H2O_p23 + SH_p1",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.26e+08, 'cm^3/(mol*s)'),
        n = 1.71,
        Ea = (-2.80328, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CAC calculation CBS-QB3 1dhr, F12a energy""",
    longDesc =
u"""
Converted to training reaction from rate rule: S_pri;O_pri_rad
""",
)

entry(
    index = 473,
    label = "OH_r3 + CH3SH_r1 <=> H2O_p23 + CH3S",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (203000, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (-17.531, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CAC calculation CBS-QB3 1dhr, F12a energy""",
    longDesc =
u"""
Converted to training reaction from rate rule: S/H/NonDeC;O_pri_rad
""",
)

entry(
    index = 474,
    label = "CH3SH_r1 + CH3O-2 <=> CH4O-2 + CH3S",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.32e+06, 'cm^3/(mol*s)'),
        n = 2.09,
        Ea = (-1.96648, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CAC calculation CBS-QB3 1dhr, F12a energy""",
    longDesc =
u"""
Converted to training reaction from rate rule: S/H/NonDeC;O_rad/NonDeC
""",
)

entry(
    index = 475,
    label = "H2S_r + CH3O-2 <=> CH4O-2 + SH_p1",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (41800, 'cm^3/(mol*s)'),
        n = 2.44,
        Ea = (4.97896, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CAC calculation CBS-QB3 1dhr, F12a energy""",
    longDesc =
u"""
Converted to training reaction from rate rule: S_pri;O_rad/NonDeC
""",
)

entry(
    index = 476,
    label = "C2H5S + C2H4O <=> C2H6S + C2H3O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.000194, 'cm^3/(mol*s)'),
        n = 4.68,
        Ea = (26.401, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CAC calculation CBS-QB3 1dhr, F12a energy""",
    longDesc =
u"""
Converted to training reaction from rate rule: CO/H/NonDe;C_rad/H/CsS
""",
)

entry(
    index = 477,
    label = "C2H6OS + CH3_r3 <=> CH4_p23 + C2H5OS",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.512, 'cm^3/(mol*s)'),
        n = 3.74,
        Ea = (15.5645, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""CAC calculation CBS-QB3 1dhr""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/CsOS;Cs_rad
""",
)

entry(
    index = 478,
    label = "CH2OS + CH3_r3 <=> CH4_p23 + CHOS",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.34, 'cm^3/(mol*s)'),
        n = 3.51,
        Ea = (-3.5564, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CAC calculation CBS-QB3 1dhr, F12a energy""",
    longDesc =
u"""
Converted to training reaction from rate rule: S/H/CO;Cs_rad
""",
)

entry(
    index = 479,
    label = "SH + C2H6OS <=> H2S + C2H5OS",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (111000, 'cm^3/(mol*s)'),
        n = 2.47,
        Ea = (24.9366, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""CAC calculation CBS-QB3 1dhr, F12a energy""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/CsOS;S_pri_rad
""",
)

entry(
    index = 480,
    label = "SH + C2H4O <=> H2S + C2H3O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (11900, 'cm^3/(mol*s)'),
        n = 2.9,
        Ea = (0.75312, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CAC calculation CBS-QB3 1dhr, F12a energy""",
    longDesc =
u"""
Converted to training reaction from rate rule: CO/H/NonDe;S_pri_rad
""",
)

entry(
    index = 481,
    label = "SH + C2H4O-2 <=> H2S + C2H3O-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.0204, 'cm^3/(mol*s)'),
        n = 4.42,
        Ea = (27.8236, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CAC calculation CBS-QB3 1dhr, F12a energy""",
    longDesc =
u"""
Converted to training reaction from rate rule: O/H/OneDe;S_pri_rad
""",
)

entry(
    index = 482,
    label = "C2H4O-2 + CH3S <=> CH3SH_r1 + C2H3O-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.95e-06, 'cm^3/(mol*s)'),
        n = 5.63,
        Ea = (49.162, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CAC calculation CBS-QB3 1dhr, F12a energy""",
    longDesc =
u"""
Converted to training reaction from rate rule: O/H/OneDe;S_rad/NonDeC
""",
)

entry(
    index = 483,
    label = "NH2_r3 + C2H6 <=> NH3_p23 + C2H5",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (5.52e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (21.1707, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli""",
    longDesc =
u"""
Converted to training reaction from rate rule: C_pri;NH2_rad
""",
)

entry(
    index = 484,
    label = "CH3_r3+ C7H12 <=> CH4_p23 + C7H11",
    degeneracy = 8.0,
    kinetics = Arrhenius(
        A = (0.1016, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (55.1451, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_1;C_methyl
""",
)

entry(
    index = 485,
    label = "NH2_r3 + C3H8 <=> NH3_p23 + C3H7",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.84e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (23.6919, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Dean and Bozzelli chapter 2, estimation same as C_pri;NH2_rad""",
    longDesc =
u"""
Converted to training reaction from rate rule: C_sec;NH2_rad
""",
)

entry(
    index = 486,
    label = "C2H5 + C7H12 <=> C2H6 + C7H11",
    degeneracy = 8.0,
    kinetics = Arrhenius(
        A = (0.01176, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (38.451, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_1;C_rad/H2/Cs
""",
)

entry(
    index = 487,
    label = "NH2_r3 + iC4H10b <=> NH3_p23 + C4H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (920000, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (24.7312, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Dean and Bozzelli chapter 2, estimation same as C_pri;NH2_rad""",
    longDesc =
u"""
Converted to training reaction from rate rule: C_ter;NH2_rad
""",
)

entry(
    index = 488,
    label = "C3H7 + C7H12 <=> C3H8 + C7H11",
    degeneracy = 8.0,
    kinetics = Arrhenius(
        A = (0.01768, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (30.5432, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_1;C_rad/H/NonDeC
""",
)

entry(
    index = 489,
    label = "H + NH3_r12 <=> H2 + NH2_p23",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (7.2e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (48.8667, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli""",
    longDesc =
u"""
Converted to training reaction from rate rule: N3s_H;H_rad
""",
)

entry(
    index = 490,
    label = "C4H9-4 + C7H12 <=> iC4H10b + C7H11",
    degeneracy = 8.0,
    kinetics = Arrhenius(
        A = (0.00528, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (28.8696, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_1;C_rad/Cs3
""",
)

entry(
    index = 491,
    label = "NH3_r12 + O_rad <=> HO + NH2_p23",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (5.1e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (116.662, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli""",
    longDesc =
u"""
Converted to training reaction from rate rule: N3s_H;O_atom_triplet
""",
)

entry(
    index = 492,
    label = "C3H5 + C7H12 <=> C3H6 + C7H11",
    degeneracy = 16.0,
    kinetics = Arrhenius(
        A = (0.2016, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (92.4246, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_1;C_rad/H2/Cd
""",
)

entry(
    index = 493,
    label = "OH_r3 + NH3_r12 <=> H2O_p23 + NH2_p23",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (3.6e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (109.424, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli""",
    longDesc =
u"""
Converted to training reaction from rate rule: N3s_H;O_pri_rad
""",
)

entry(
    index = 494,
    label = "C4H7-4 + C7H12 <=> C4H8-4 + C7H11",
    degeneracy = 8.0,
    kinetics = Arrhenius(
        A = (0.04536, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (80.542, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_1;C_rad/H/CdCs
""",
)

entry(
    index = 495,
    label = "CH3_r3+ NH3_r12 <=> CH4_p23 + NH2_p23",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (2.43e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (86.9142, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli""",
    longDesc =
u"""
Converted to training reaction from rate rule: N3s_H;C_methyl
""",
)

entry(
    index = 496,
    label = "C5H9-5 + C7H12 <=> C5H10-3 + C7H11",
    degeneracy = 8.0,
    kinetics = Arrhenius(
        A = (0.007048, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (76.0233, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_1;C_rad/CdCs2
""",
)

entry(
    index = 497,
    label = "C5H7-2 + C7H12 <=> C5H8-2 + C7H11",
    degeneracy = 8.0,
    kinetics = Arrhenius(
        A = (0.152, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (118.742, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_1;C_rad/H/CdCd
""",
)

entry(
    index = 498,
    label = "C6H9 + C7H12 <=> C6H10 + C7H11",
    degeneracy = 8.0,
    kinetics = Arrhenius(
        A = (0.007688, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (103.763, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_1;C_rad/CdCdCs
""",
)

entry(
    index = 499,
    label = "C3H3-2 + C7H12 <=> C3H4 + C7H11",
    degeneracy = 8.0,
    kinetics = Arrhenius(
        A = (0.046, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (87.4038, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_1;C_rad/H2/Ct
""",
)

entry(
    index = 500,
    label = "C4H5-5 + C7H12 <=> C4H6 + C7H11",
    degeneracy = 8.0,
    kinetics = Arrhenius(
        A = (0.01088, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (74.5589, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_1;C_rad/H/CtCs
""",
)

entry(
    index = 501,
    label = "C5H7-3 + C7H12 <=> C5H8 + C7H11",
    degeneracy = 8.0,
    kinetics = Arrhenius(
        A = (0.004392, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (72.425, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_1;C_rad/CtCs2
""",
)

entry(
    index = 502,
    label = "C5H3 + C7H12 <=> C5H4 + C7H11",
    degeneracy = 8.0,
    kinetics = Arrhenius(
        A = (0.04616, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (79.496, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_1;C_rad/H/CtCt
""",
)

entry(
    index = 503,
    label = "C6H5-2 + C7H12 <=> C6H6-2 + C7H11",
    degeneracy = 8.0,
    kinetics = Arrhenius(
        A = (0.001288, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (82.4248, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_1;C_rad/CtCtCs
""",
)

entry(
    index = 504,
    label = "C7H7 + C7H12 <=> C7H8 + C7H11",
    degeneracy = 8.0,
    kinetics = Arrhenius(
        A = (0.0984, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (81.5964, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_1;C_rad/H2/Cb
""",
)

entry(
    index = 505,
    label = "C8H9 + C7H12 <=> C8H10 + C7H11",
    degeneracy = 8.0,
    kinetics = Arrhenius(
        A = (0.02888, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (70.651, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_1;C_rad/H/CbCs
""",
)

entry(
    index = 506,
    label = "C9H11 + C7H12 <=> C9H12 + C7H11",
    degeneracy = 8.0,
    kinetics = Arrhenius(
        A = (0.0007816, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (72.2577, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_1;C_rad/CbCs2
""",
)

entry(
    index = 507,
    label = "C2H3 + C7H12 <=> C2H4 + C7H11",
    degeneracy = 8.0,
    kinetics = Arrhenius(
        A = (0.0952, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (5.0208, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_1;Cd_pri_rad
""",
)

entry(
    index = 508,
    label = "C3H5-2 + C7H12 <=> C3H6-2 + C7H11",
    degeneracy = 8.0,
    kinetics = Arrhenius(
        A = (0.05376, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (7.1128, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_1;Cd_rad/NonDeC
""",
)

entry(
    index = 509,
    label = "C4H5-3 + C7H12 <=> C4H6-4 + C7H11",
    degeneracy = 8.0,
    kinetics = Arrhenius(
        A = (0.04512, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (37.2376, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_1;Cd_rad/Cd
""",
)

entry(
    index = 510,
    label = "C6H5 + C7H12 <=> C6H6 + C7H11",
    degeneracy = 8.0,
    kinetics = Arrhenius(
        A = (0.1136, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (-6.276, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_1;Cb_rad
""",
)

entry(
    index = 511,
    label = "C4H3 + C7H12 <=> C4H4 + C7H11",
    degeneracy = 8.0,
    kinetics = Arrhenius(
        A = (0.00968, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (25.9408, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_1;Cd_rad/Ct
""",
)

entry(
    index = 512,
    label = "CH3_r3+ C7H12-2 <=> CH4_p23 + C7H11-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.0366, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (77.8642, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_fused6;C_methyl
""",
)

entry(
    index = 513,
    label = "C2H5 + C7H12-2 <=> C2H6 + C7H11-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.0032, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (61.1701, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_fused6;C_rad/H2/Cs
""",
)

entry(
    index = 514,
    label = "C3H7 + C7H12-2 <=> C3H8 + C7H11-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.00362, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (50.208, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_fused6;C_rad/H/NonDeC
""",
)

entry(
    index = 515,
    label = "C4H9-4 + C7H12-2 <=> iC4H10b + C7H11-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.000816, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (45.6893, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_fused6;C_rad/Cs3
""",
)

entry(
    index = 516,
    label = "C3H5 + C7H12-2 <=> C3H6 + C7H11-2",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (0.05, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (115.144, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_fused6;C_rad/H2/Cd
""",
)

entry(
    index = 517,
    label = "C4H7-4 + C7H12-2 <=> C4H8-4 + C7H11-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.00848, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (103.261, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_fused6;C_rad/H/CdCs
""",
)

entry(
    index = 518,
    label = "C5H9-5 + C7H12-2 <=> C5H10-3 + C7H11-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.000996, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (98.7424, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_fused6;C_rad/CdCs2
""",
)

entry(
    index = 519,
    label = "C5H7-2 + C7H12-2 <=> C5H8-2 + C7H11-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.026, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (141.461, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_fused6;C_rad/H/CdCd
""",
)

entry(
    index = 520,
    label = "C6H9 + C7H12-2 <=> C6H10 + C7H11-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.00099, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (103.345, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_fused6;C_rad/CdCdCs
""",
)

entry(
    index = 521,
    label = "C3H3-2 + C7H12-2 <=> C3H4 + C7H11-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.0114, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (110.123, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_fused6;C_rad/H2/Ct
""",
)

entry(
    index = 522,
    label = "C4H5-5 + C7H12-2 <=> C4H6 + C7H11-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.00204, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (97.278, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_fused6;C_rad/H/CtCs
""",
)

entry(
    index = 523,
    label = "C5H7-3 + C7H12-2 <=> C5H8 + C7H11-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.00062, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (95.1442, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_fused6;C_rad/CtCs2
""",
)

entry(
    index = 524,
    label = "C5H3 + C7H12-2 <=> C5H4 + C7H11-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.00788, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (79.496, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_fused6;C_rad/H/CtCt
""",
)

entry(
    index = 525,
    label = "C6H5-2 + C7H12-2 <=> C6H6-2 + C7H11-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.0001664, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (81.588, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_fused6;C_rad/CtCtCs
""",
)

entry(
    index = 526,
    label = "C7H7 + C7H12-2 <=> C7H8 + C7H11-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.0244, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (104.315, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_fused6;C_rad/H2/Cb
""",
)

entry(
    index = 527,
    label = "C8H9 + C7H12-2 <=> C8H10 + C7H11-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.0054, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (93.3701, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_fused6;C_rad/H/CbCs
""",
)

entry(
    index = 528,
    label = "C9H11 + C7H12-2 <=> C9H12 + C7H11-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.0001104, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (94.9768, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_fused6;C_rad/CbCs2
""",
)

entry(
    index = 529,
    label = "C2H3 + C7H12-2 <=> C2H4 + C7H11-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.0344, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (13.8072, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_fused6;Cd_pri_rad
""",
)

entry(
    index = 530,
    label = "C3H5-2 + C7H12-2 <=> C3H6-2 + C7H11-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.0146, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (14.644, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_fused6;Cd_rad/NonDeC
""",
)

entry(
    index = 531,
    label = "C4H5-3 + C7H12-2 <=> C4H6-4 + C7H11-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.01626, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (45.6056, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_fused6;Cd_rad/Cd
""",
)

entry(
    index = 532,
    label = "C6H5 + C7H12-2 <=> C6H6 + C7H11-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.041, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (2.092, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_fused6;Cb_rad
""",
)

entry(
    index = 533,
    label = "C4H3 + C7H12-2 <=> C4H4 + C7H11-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.00348, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (34.3088, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_fused6;Cd_rad/Ct
""",
)

entry(
    index = 534,
    label = "CH3_r3+ C7H12-3 <=> CH4_p23 + C7H11-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.01452, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (32.6352, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_2;C_methyl
""",
)

entry(
    index = 535,
    label = "C2H5 + C7H12-3 <=> C2H6 + C7H11-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.001684, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (36.8192, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_2;C_rad/H2/Cs
""",
)

entry(
    index = 536,
    label = "C3H7 + C7H12-3 <=> C3H8 + C7H11-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.00254, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (38.9112, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_2;C_rad/H/NonDeC
""",
)

entry(
    index = 537,
    label = "C4H9-4 + C7H12-3 <=> iC4H10b + C7H11-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.000756, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (37.2376, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_2;C_rad/Cs3
""",
)

entry(
    index = 538,
    label = "C3H5 + C7H12-3 <=> C3H6 + C7H11-3",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (0.02896, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (77.8224, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_2;C_rad/H2/Cd
""",
)

entry(
    index = 539,
    label = "C4H7-4 + C7H12-3 <=> C4H8-4 + C7H11-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.0065, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (83.68, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_2;C_rad/H/CdCs
""",
)

entry(
    index = 540,
    label = "C5H9-5 + C7H12-3 <=> C5H10-3 + C7H11-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.00101, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (84.0984, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_2;C_rad/CdCs2
""",
)

entry(
    index = 541,
    label = "C5H7-2 + C7H12-3 <=> C5H8-2 + C7H11-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.0218, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (111.713, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_2;C_rad/H/CdCd
""",
)

entry(
    index = 542,
    label = "C6H9 + C7H12-3 <=> C6H10 + C7H11-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.0011, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (112.131, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_2;C_rad/CdCdCs
""",
)

entry(
    index = 543,
    label = "C3H3-2 + C7H12-3 <=> C3H4 + C7H11-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.00658, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (62.3416, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_2;C_rad/H2/Ct
""",
)

entry(
    index = 544,
    label = "C4H5-5 + C7H12-3 <=> C4H6 + C7H11-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.001558, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (66.944, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_2;C_rad/H/CtCs
""",
)

entry(
    index = 545,
    label = "C5H7-3 + C7H12-3 <=> C5H8 + C7H11-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.000628, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (69.036, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_2;C_rad/CtCs2
""",
)

entry(
    index = 546,
    label = "C5H3 + C7H12-3 <=> C5H4 + C7H11-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.00662, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (87.864, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_2;C_rad/H/CtCt
""",
)

entry(
    index = 547,
    label = "C6H5-2 + C7H12-3 <=> C6H6-2 + C7H11-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.000185, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (90.3744, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_2;C_rad/CtCtCs
""",
)

entry(
    index = 548,
    label = "C7H7 + C7H12-3 <=> C7H8 + C7H11-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.01412, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (69.036, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_2;C_rad/H2/Cb
""",
)

entry(
    index = 549,
    label = "C8H9 + C7H12-3 <=> C8H10 + C7H11-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.00412, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (71.128, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_2;C_rad/H/CbCs
""",
)

entry(
    index = 550,
    label = "C9H11 + C7H12-3 <=> C9H12 + C7H11-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.000112, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (67.7808, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_2;C_rad/CbCs2
""",
)

entry(
    index = 551,
    label = "C2H3 + C7H12-3 <=> C2H4 + C7H11-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.01368, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (13.3888, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_2;Cd_pri_rad
""",
)

entry(
    index = 552,
    label = "C3H5-2 + C7H12-3 <=> C3H6-2 + C7H11-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.0077, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (15.4808, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_2;Cd_rad/NonDeC
""",
)

entry(
    index = 553,
    label = "C4H5-3 + C7H12-3 <=> C4H6-4 + C7H11-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.00646, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (45.6056, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_2;Cd_rad/Cd
""",
)

entry(
    index = 554,
    label = "C6H5 + C7H12-3 <=> C6H6 + C7H11-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.01626, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (2.092, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_2;Cb_rad
""",
)

entry(
    index = 555,
    label = "C4H3 + C7H12-3 <=> C4H4 + C7H11-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.001386, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (34.3088, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_2;Cd_rad/Ct
""",
)

entry(
    index = 556,
    label = "CH3_r3+ C8H14 <=> CH4_p23 + C8H13",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.0133, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (28.8278, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_adj5;C_methyl
""",
)

entry(
    index = 557,
    label = "C2H5 + C8H14 <=> C2H6 + C8H13",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.001164, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (25.9408, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_adj5;C_rad/H2/Cs
""",
)

entry(
    index = 558,
    label = "C3H7 + C8H14 <=> C3H8 + C8H13",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.00132, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (26.7776, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_adj5;C_rad/H/NonDeC
""",
)

entry(
    index = 559,
    label = "C4H9-4 + C8H14 <=> iC4H10b + C8H13",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.000298, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (24.6856, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_adj5;C_rad/Cs3
""",
)

entry(
    index = 560,
    label = "C3H5 + C8H14 <=> C3H6 + C8H13",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (0.01828, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (66.1072, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_adj5;C_rad/H2/Cd
""",
)

entry(
    index = 561,
    label = "C4H7-4 + C8H14 <=> C4H8-4 + C8H13",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.00308, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (68.6176, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_adj5;C_rad/H/CdCs
""",
)

entry(
    index = 562,
    label = "C5H9-5 + C8H14 <=> C5H10-3 + C8H13",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.000362, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (68.1992, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_adj5;C_rad/CdCs2
""",
)

entry(
    index = 563,
    label = "C5H7-2 + C8H14 <=> C5H8-2 + C8H13",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.00946, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (93.3032, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_adj5;C_rad/H/CdCd
""",
)

entry(
    index = 564,
    label = "C6H9 + C8H14 <=> C6H10 + C8H13",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.00036, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (92.8848, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_adj5;C_rad/CdCdCs
""",
)

entry(
    index = 565,
    label = "C3H3-2 + C8H14 <=> C3H4 + C8H13",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.00416, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (61.0864, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_adj5;C_rad/H2/Ct
""",
)

entry(
    index = 566,
    label = "C4H5-5 + C8H14 <=> C4H6 + C8H13",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.000742, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (51.8816, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_adj5;C_rad/H/CtCs
""",
)

entry(
    index = 567,
    label = "C5H7-3 + C8H14 <=> C5H8 + C8H13",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.000226, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (53.1368, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_adj5;C_rad/CtCs2
""",
)

entry(
    index = 568,
    label = "C5H3 + C8H14 <=> C5H4 + C8H13",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.00288, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (69.4544, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_adj5;C_rad/H/CtCt
""",
)

entry(
    index = 569,
    label = "C6H5-2 + C8H14 <=> C6H6-2 + C8H13",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (6.06e-05, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (71.128, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_adj5;C_rad/CtCtCs
""",
)

entry(
    index = 570,
    label = "C7H7 + C8H14 <=> C7H8 + C8H13",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.00892, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (55.279, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_adj5;C_rad/H2/Cb
""",
)

entry(
    index = 571,
    label = "C8H9 + C8H14 <=> C8H10 + C8H13",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.001966, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (56.0656, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_adj5;C_rad/H/CbCs
""",
)

entry(
    index = 572,
    label = "C9H11 + C8H14 <=> C9H12 + C8H13",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (4.02e-05, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (51.8816, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_adj5;C_rad/CbCs2
""",
)

entry(
    index = 573,
    label = "C2H3 + C8H14 <=> C2H4 + C8H13",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.01254, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (3.3472, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_adj5;Cd_pri_rad
""",
)

entry(
    index = 574,
    label = "C3H5-2 + C8H14 <=> C3H6-2 + C8H13",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.00532, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (4.184, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_adj5;Cd_rad/NonDeC
""",
)

entry(
    index = 575,
    label = "C4H5-3 + C8H14 <=> C4H6-4 + C8H13",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.00592, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (35.564, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_adj5;Cd_rad/Cd
""",
)

entry(
    index = 576,
    label = "C6H5 + C8H14 <=> C6H6 + C8H13",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.0149, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (-7.9496, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_adj5;Cb_rad
""",
)

entry(
    index = 577,
    label = "C4H3 + C8H14 <=> C4H4 + C8H13",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.00127, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (23.8488, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_adj5;Cd_rad/Ct
""",
)

entry(
    index = 578,
    label = "CH3_r3+ C9H16 <=> CH4_p23 + C9H15",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (0.0416, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (27.6562, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_alpha6ring;C_methyl
""",
)

entry(
    index = 579,
    label = "C2H5 + C9H16 <=> C2H6 + C9H15",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (0.00484, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (30.5432, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_alpha6ring;C_rad/H2/Cs
""",
)

entry(
    index = 580,
    label = "C3H7 + C9H16 <=> C3H8 + C9H15",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (0.00728, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (32.2168, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_alpha6ring;C_rad/H/NonDeC
""",
)

entry(
    index = 581,
    label = "C4H9-4 + C9H16 <=> iC4H10b + C9H15",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (0.002172, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (30.9616, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_alpha6ring;C_rad/Cs3
""",
)

entry(
    index = 582,
    label = "C3H5 + C9H16 <=> C3H6 + C9H15",
    degeneracy = 8.0,
    kinetics = Arrhenius(
        A = (0.0832, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (71.5464, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_alpha6ring;C_rad/H2/Cd
""",
)

entry(
    index = 583,
    label = "C4H7-4 + C9H16 <=> C4H8-4 + C9H15",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (0.01864, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (77.404, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_alpha6ring;C_rad/H/CdCs
""",
)

entry(
    index = 584,
    label = "C5H9-5 + C9H16 <=> C5H10-3 + C9H15",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (0.002896, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (77.8224, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_alpha6ring;C_rad/CdCs2
""",
)

entry(
    index = 585,
    label = "C5H7-2 + C9H16 <=> C5H8-2 + C9H15",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (0.0624, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (105.437, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_alpha6ring;C_rad/H/CdCd
""",
)

entry(
    index = 586,
    label = "C6H9 + C9H16 <=> C6H10 + C9H15",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (0.003156, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (105.855, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_alpha6ring;C_rad/CdCdCs
""",
)

entry(
    index = 587,
    label = "C3H3-2 + C9H16 <=> C3H4 + C9H15",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (0.01888, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (59.9149, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_alpha6ring;C_rad/H2/Ct
""",
)

entry(
    index = 588,
    label = "C4H5-5 + C9H16 <=> C4H6 + C9H15",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (0.00448, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (60.668, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_alpha6ring;C_rad/H/CtCs
""",
)

entry(
    index = 589,
    label = "C5H7-3 + C9H16 <=> C5H8 + C9H15",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (0.001804, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (62.76, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_alpha6ring;C_rad/CtCs2
""",
)

entry(
    index = 590,
    label = "C5H3 + C9H16 <=> C5H4 + C9H15",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (0.01896, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (81.588, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_alpha6ring;C_rad/H/CtCt
""",
)

entry(
    index = 591,
    label = "C6H5-2 + C9H16 <=> C6H6-2 + C9H15",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (0.000532, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (84.0984, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_alpha6ring;C_rad/CtCtCs
""",
)

entry(
    index = 592,
    label = "C7H7 + C9H16 <=> C7H8 + C9H15",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (0.0404, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (62.76, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_alpha6ring;C_rad/H2/Cb
""",
)

entry(
    index = 593,
    label = "C8H9 + C9H16 <=> C8H10 + C9H15",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (0.01184, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (64.4336, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_alpha6ring;C_rad/H/CbCs
""",
)

entry(
    index = 594,
    label = "C9H11 + C9H16 <=> C9H12 + C9H15",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (0.0003212, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (61.5048, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_alpha6ring;C_rad/CbCs2
""",
)

entry(
    index = 595,
    label = "C2H3 + C9H16 <=> C2H4 + C9H15",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (0.03924, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (7.1128, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_alpha6ring;Cd_pri_rad
""",
)

entry(
    index = 596,
    label = "C3H5-2 + C9H16 <=> C3H6-2 + C9H15",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (0.02208, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (8.7864, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_alpha6ring;Cd_rad/NonDeC
""",
)

entry(
    index = 597,
    label = "C4H5-3 + C9H16 <=> C4H6-4 + C9H15",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (0.01852, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (39.3296, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_alpha6ring;Cd_rad/Cd
""",
)

entry(
    index = 598,
    label = "C6H5 + C9H16 <=> C6H6 + C9H15",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (0.0468, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (-4.184, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_alpha6ring;Cb_rad
""",
)

entry(
    index = 599,
    label = "C4H3 + C9H16 <=> C4H4 + C9H15",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (0.003976, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (27.6144, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_alpha6ring;Cd_rad/Ct
""",
)

entry(
    index = 600,
    label = "CH3_r3+ C9H16-2 <=> CH4_p23 + C9H15-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.0302, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (24.6856, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_beta6ring;C_methyl
""",
)

entry(
    index = 601,
    label = "C2H5 + C9H16-2 <=> C2H6 + C9H15-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.0035, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (29.288, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_beta6ring;C_rad/H2/Cs
""",
)

entry(
    index = 602,
    label = "C3H7 + C9H16-2 <=> C3H8 + C9H15-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.00526, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (30.9616, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_beta6ring;C_rad/H/NonDeC
""",
)

entry(
    index = 603,
    label = "C4H9-4 + C9H16-2 <=> iC4H10b + C9H15-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.001574, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (29.288, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_beta6ring;C_rad/Cs3
""",
)

entry(
    index = 604,
    label = "C3H5 + C9H16-2 <=> C3H6 + C9H15-2",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (0.0604, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (70.2912, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_beta6ring;C_rad/H2/Cd
""",
)

entry(
    index = 605,
    label = "C4H7-4 + C9H16-2 <=> C4H8-4 + C9H15-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.0135, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (76.1488, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_beta6ring;C_rad/H/CdCs
""",
)

entry(
    index = 606,
    label = "C5H9-5 + C9H16-2 <=> C5H10-3 + C9H15-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.0021, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (76.1488, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_beta6ring;C_rad/CdCs2
""",
)

entry(
    index = 607,
    label = "C5H7-2 + C9H16-2 <=> C5H8-2 + C9H15-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.0452, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (104.182, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_beta6ring;C_rad/H/CdCd
""",
)

entry(
    index = 608,
    label = "C6H9 + C9H16-2 <=> C6H10 + C9H15-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.00228, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (104.182, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_beta6ring;C_rad/CdCdCs
""",
)

entry(
    index = 609,
    label = "C3H3-2 + C9H16-2 <=> C3H4 + C9H15-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.0137, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (54.392, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_beta6ring;C_rad/H2/Ct
""",
)

entry(
    index = 610,
    label = "C4H5-5 + C9H16-2 <=> C4H6 + C9H15-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.00324, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (59.4128, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_beta6ring;C_rad/H/CtCs
""",
)

entry(
    index = 611,
    label = "C5H7-3 + C9H16-2 <=> C5H8 + C9H15-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.001308, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (61.0864, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_beta6ring;C_rad/CtCs2
""",
)

entry(
    index = 612,
    label = "C5H3 + C9H16-2 <=> C5H4 + C9H15-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.01376, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (79.9144, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_beta6ring;C_rad/H/CtCt
""",
)

entry(
    index = 613,
    label = "C6H5-2 + C9H16-2 <=> C6H6-2 + C9H15-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.000384, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (82.8432, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_beta6ring;C_rad/CtCtCs
""",
)

entry(
    index = 614,
    label = "C7H7 + C9H16-2 <=> C7H8 + C9H15-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.0294, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (61.5048, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_beta6ring;C_rad/H2/Cb
""",
)

entry(
    index = 615,
    label = "C8H9 + C9H16-2 <=> C8H10 + C9H15-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.0086, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (63.1784, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_beta6ring;C_rad/H/CbCs
""",
)

entry(
    index = 616,
    label = "C9H11 + C9H16-2 <=> C9H12 + C9H15-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.000232, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (59.8312, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_beta6ring;C_rad/CbCs2
""",
)

entry(
    index = 617,
    label = "C2H3 + C9H16-2 <=> C2H4 + C9H15-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.0284, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (5.8576, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_beta6ring;Cd_pri_rad
""",
)

entry(
    index = 618,
    label = "C3H5-2 + C9H16-2 <=> C3H6-2 + C9H15-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.016, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (7.5312, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_beta6ring;Cd_rad/NonDeC
""",
)

entry(
    index = 619,
    label = "C4H5-3 + C9H16-2 <=> C4H6-4 + C9H15-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.01344, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (38.0744, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_beta6ring;Cd_rad/Cd
""",
)

entry(
    index = 620,
    label = "C6H5 + C9H16-2 <=> C6H6 + C9H15-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.0338, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (-5.8576, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_beta6ring;Cb_rad
""",
)

entry(
    index = 621,
    label = "C4H3 + C9H16-2 <=> C4H4 + C9H15-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.00288, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (26.3592, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs BMK/6-311G(2,d,p)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_beta6ring;Cd_rad/Ct
""",
)

entry(
    index = 622,
    label = "H + NH3_r12 <=> H2 + NH2_p23",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(2.89e+06, 'cm^3/(mol*s)'), n=2.23036, Ea=(10407, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(300, 'K'), Tmax=(2500, 'K')),
    rank = 1,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: NH3 + H = NH2_r3 + H2 (B&D #6) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: NH3;H_rad
""",
)

entry(
    index = 623,
    label = "OH_r3 + NH3_r12 <=> H2O_p23 + NH2_p23",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.5e+08, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (109.424, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: NH3 + OH = NH2_r3 + H2O (B&D #7) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: NH3;O_pri_rad
""",
)

entry(
    index = 624,
    label = "NH3_r12 + O_rad <=> HO + NH2_p23",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (2.82e+07, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (116.662, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: NH3 + O = NH2_r3 + OH (B&D #8) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: NH3;O_atom_triplet
""",
)

entry(
    index = 625,
    label = "H + NH2_r12 <=> H2 + NH_p23",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (9.6e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (33.221, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: NH2_r3 + H = NH + H2 (B&D #9) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",
""",
)

entry(
    index = 626,
    label = "NH2_r12 + O_rad <=> HO + NH_p23",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: NH2_r3 + O = NH + OH (B&D #15d2) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",
""",
)

entry(
    index = 627,
    label = "OH_r3 + NH2_r12<=> H2O_p23 + NH_p1",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (4.8e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (83.4834, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: NH2_r3 + OH = NH + H2O (B&D #16b) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",
""",
)

entry(
    index = 628,
    label = "NH2_r12 + NH2_r3 <=> NH3_p23 + NH_p1",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (41.589, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: NH2_r3 + NH2_r3 = NH3 + NH (B&D #17e) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: NH2_rad_H;NH2_rad
""",
)

entry(
    index = 629,
    label = "NH2_r12 + CH3_r3 <=> CH4_p23 + NH_p1",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (5.6e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (60.9734, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: CH3 + NH2_r3 = CH4 + NH (B&D #21e) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: NH2_rad_H;C_methyl
""",
)

entry(
    index = 630,
    label = "NH2_r3 + CH3_r12 <=> NH3_p23 + CH2_p1",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (4.8e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (31.6729, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: CH3 + NH2_r3 = CH2 + NH3 (B&D #21f) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: CH3_rad_H;NH2_rad
""",
)

entry(
    index = 631,
    label = "HO + N <=> HN + O_rad",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.4e+12, 'cm^3/(mol*s)'),
        n = 0.1,
        Ea = (88.9518, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: N + OH = NH + O (B&D #26b) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: OH_rad_H;N_atom_quartet
""",
)

entry(
    index = 632,
    label = "HN + NH2_r3 <=> NH3_p23 + N",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (920000, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (101.215, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: NH + NH2_r3 = NH3 + N (B&D #27b2) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: NH_triplet_H;NH2_rad
""",
)

entry(
    index = 633,
    label = "OH_r3 + HN <=> H2O_p23 + N",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.2e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-2.05016, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: NH + OH = N + H2O (B&D #27c2) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: NH_triplet_H;O_pri_rad
""",
)

entry(
    index = 634,
    label = "H + HN <=> H2_p + N",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (126.666, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: NH + H = N + H2 (B&D #27d) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: NH_triplet_H;H_rad
""",
)

entry(
    index = 635,
    label = "HN + O_rad <=> HO + N",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.7e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (217.878, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: NH + O = N + OH (B&D #27e2) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: NH_triplet_H;O_atom_triplet
""",
)

entry(
    index = 636,
    label = "HN + CH3_r3 <=> CH4_p23 + N",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (820000, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (188.129, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: NH + CH3 = CH4 + N (B&D #27f2) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: NH_triplet_H;C_methyl
""",
)

entry(
    index = 637,
    label = "H + H2N2 <=> H2 + HN2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (9.6e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (6.61072, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: N2H2 + H = NNH + H2 (B&D #29c1) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3d/H/NonDeN;H_rad
""",
)

entry(
    index = 638,
    label = "H2N2 + O_rad <=> HO + HN2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (6.6e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (21.2673, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: N2H2 + O = NNH + OH (B&D #29c2) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3d/H/NonDeN;O_atom_triplet
""",
)

entry(
    index = 639,
    label = "OH_r3 + H2N2 <=> H2O_p23 + HN2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (4.8e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-4.97896, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: N2H2 + OH = NNH + H2O (B&D #29c3) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3d/H/NonDeN;O_pri_rad
""",
)

entry(
    index = 640,
    label = "NH2_r3 + H2N2 <=> NH3_p23 + HN2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.6e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (-4.8116, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: N2H2 + NH2_r3 = NNH + NH3 (B&D #29c4) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3d/H/NonDeN;NH2_rad
""",
)

entry(
    index = 641,
    label = "H2N2 + CH3_r3 <=> CH4_p23 + HN2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.2e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (12.4265, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: N2H2 + CH3 = NNH + CH4 (B&D #29c5) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3d/H/NonDeN;C_methyl
""",
)

entry(
    index = 642,
    label = "NH_r3 + H2N2 <=> NH2_r12 + HN2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (4.8e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-4.97896, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: N2H2 + NH = NNH + NH2_r3 (B&D #29d) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3d/H/NonDeN;NH_triplet
""",
)

entry(
    index = 643,
    label = "OH_r3 + N2H3_r12 <=> H2O_p23 + H2N2-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: N2H3 + OH = H2NN + H2O (B&D #31d2)  in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3s_rad_H/H/NonDeN;O_pri_rad
""",
)

entry(
    index = 644,
    label = "N2H3_r12 + CH3_r3 <=> CH4_p23 + H2N2-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: N2H3 + CH3 = H2NN + CH4 (B&D #31e2) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3s_rad_H/H/NonDeN;C_methyl
""",
)

entry(
    index = 645,
    label = "NH2_r3 + N2H3_r12 <=> NH3_p23 + H2N2-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: N2H3 + NH2_r3 = H2NN + NH3 (B&D #31f2) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3s_rad_H/H/NonDeN;NH2_rad
""",
)

entry(
    index = 646,
    label = "H + N2H4_r12 <=> H2_p + N2H3_p1",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (3.84e+09, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (20.2506, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: N2H4 + H = N2H3 + H2 (B&D #32a) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3s/H2/NonDeN;H_rad
""",
)

entry(
    index = 647,
    label = "N2H4_r12 + O_rad <=> HO + N2H3_p1",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (2.68e+09, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (40.0953, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: N2H4 + O = N2H3 + OH (B&D #32b) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3s/H2/NonDeN;O_atom_triplet
""",
)

entry(
    index = 648,
    label = "OH_r3 + N2H4_r12 <=> H2O_p23 + N2H3_p1",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (1.92e+07, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-2.7196, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: N2H4 + OH = N2H3 + H2O (B&D #32c) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3s/H2/NonDeN;O_pri_rad
""",
)

entry(
    index = 649,
    label = "CH3_r3+ N2H4_r12 <=> CH4_p23 + N2H3_p1",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (1.32e+07, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (22.3007, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: N2H4 + CH3 = N2H3 + CH4 (B&D #32d) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3s/H2/NonDeN;C_methyl
""",
)

entry(
    index = 650,
    label = "NH2_r3 + N2H4_r12 <=> NH3_p23 + N2H3_p1",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (1.48e+07, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (6.81992, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: N2H4 + NH2_r3 = N2H3 + NH3 (B&D #32e) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3s/H2/NonDeN;NH2_rad
""",
)

entry(
    index = 651,
    label = "OH_r3 + HNO_r <=> H2O_p23 + NO",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.3e+07, 'cm^3/(mol*s)'),
        n = 1.88,
        Ea = (-3.9748, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: HNO + OH = NO + H2O (B&D #36c) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3d/H/NonDeO;O_pri_rad
""",
)

entry(
    index = 652,
    label = "H + HNO_r <=> H2 + NO",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.5e+11, 'cm^3/(mol*s)'),
        n = 0.72,
        Ea = (2.76144, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: HNO + H = H2 + NO (B&D #36d1) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3d/H/NonDeO;H_rad
""",
)

entry(
    index = 653,
    label = "HNO_r + O_rad <=> HO + NO",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.5e+11, 'cm^3/(mol*s)'),
        n = 0.72,
        Ea = (2.76144, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: HNO + O = OH + NO (B&D #36e) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3d/H/NonDeO;O_atom_triplet
""",
)

entry(
    index = 654,
    label = "HNO_r + NH2_r3 <=> NH3_p23 + NO_p",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (920000, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (-4.8116, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: HNO + NH2_r3 = NH3 + NO (B&D #36f) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3d/H/NonDeO;NH2_rad
""",
)

entry(
    index = 655,
    label = "HNO_r + O2 <=> HO2_p23 + NO_p",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (66.5256, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: HNO + O2 = NO + HO2 (B&D #36h) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3d/H/NonDeO;O2b
""",
)

entry(
    index = 656,
    label = "HNO_r + CH3_r3 <=> CH4_p23 + NO_p",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (820000, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (3.9748, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: HNO + CH3 = NO + CH4 (B&D #36i) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3d/H/NonDeO;C_methyl
""",
)

entry(
    index = 657,
    label = "H + CH3NO <=> H2_p + CH2NO",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2e+08, 'cm^3/(mol*s)'),
        n = 1.55,
        Ea = (27.6981, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: HONO + H = H2 + NO2 (B&D #40b1) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: O/H/OneDeN;H_rad
""",
)

entry(
    index = 658,
    label = "CH3NO + O_rad <=> HO + CH2NO",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.7e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (103.596, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: HONO + O = OH + NO2 (B&D #40c) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: O/H/OneDeN;O_atom_triplet
""",
)

entry(
    index = 659,
    label = "OH_r3 + CH3NO <=> H2O_p23 + CH2NO",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.2e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-2.5104, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: HONO + OH = H2O + NO2 (B&D #40d) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: O/H/OneDeN;O_pri_rad
""",
)

entry(
    index = 660,
    label = "CH3NO + CH3_r3 <=> CH4_p23 + CH2NO",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (810000, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (73.8476, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: HONO + CH3 = NO2 + CH4 (B&D #40e) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: O/H/OneDeN;C_methyl
""",
)

entry(
    index = 661,
    label = "NH2_r3 + CH3NO <=> NH3_p23 + CH2NO",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (920000, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (8.03328, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: HONO + NH2_r3 = NO2 + NH3 (B&D #40f) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: O/H/OneDeN;NH2_rad
""",
)

entry(
    index = 662,
    label = "OH_r3 + HCN_r <=> H2O_p23 + CN",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.9e+06, 'cm^3/(mol*s)'),
        n = 1.83,
        Ea = (83.9729, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: HCN + OH = CN + H2O (B&D #42a) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: Ct/H/NonDeN;O_pri_rad
""",
)

entry(
    index = 663,
    label = "HCN_r + O_rad <=> HO + CN",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.2e+10, 'cm^3/(mol*s)'),
        n = 0.4,
        Ea = (86.507, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Matt Johnson""",
    longDesc =
u"""
Added by Matt Johnson, value for reaction: HCN + O = CN + OH (B&D #42c3) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: Ct/H/NonDeN;O_atom_triplet
""",
)

entry(
    index = 664,
    label = "H2 + CN <=> HCN_r + H",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (7.2e+08, 'cm^3/(mol*s)'),
        n = 1.55,
        Ea = (12.552, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: CN + H2 = HCN + H (B&D #44a) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: H2;Ct_rad/N
""",
)

entry(
    index = 665,
    label = "H2O_r12 + CN <=> HCN_r + OH_p1",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.56e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (31.1708, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: CN + H2O = HCN + OH (B&D #44b) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: O_pri;Ct_rad/N
""",
)

entry(
    index = 666,
    label = "CH4_r12 + CN <=> HCN_r + CH3_p1",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (480000, 'cm^3/(mol*s)'),
        n = 2.64,
        Ea = (-0.66944, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: CN + CH4 = HCN + CH3 (B&D #44i) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: C_methane;Ct_rad/N
""",
)

entry(
    index = 667,
    label = "NH3_r12 + CN <=> HCN_r + NH2_p23",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (2.76e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1.50624, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: CN + NH3 = HCN + NH2_r3 (B&D #44j) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: NH3;Ct_rad/N
""",
)

entry(
    index = 668,
    label = "H + CH3N <=> H2 + CH2N",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.4e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (30.6269, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: H2CNH + H = H2CN + H2 (B&D #48a1) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3d/H/NonDeC;H_rad
""",
)

entry(
    index = 669,
    label = "CH3N + O_rad <=> HO + CH2N",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.7e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (85.9519, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: H2CNH + O = H2CN + OH (B&D #48a2) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3d/H/NonDeC;O_atom_triplet
""",
)

entry(
    index = 670,
    label = "OH_r3 + CH3N <=> H2O_p23 + CH2N",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.2e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-0.37656, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: H2CNH + OH = H2CN + H2O (B&D #48a3) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3d/H/NonDeC;O_pri_rad
""",
)

entry(
    index = 671,
    label = "CH3N + CH3_r3 <=> CH4_p23 + CH2N",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (820000, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (56.2037, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: H2CNH + CH3 = H2CN + CH4 (B&D #48a4) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3d/H/NonDeC;C_methyl
""",
)

entry(
    index = 672,
    label = "NH2_r3 + CH3N <=> NH3_p23 + CH2N",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (920000, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (18.577, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: H2CNH + NH2_r3 = H2CN + NH3 (B&D #48a5) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3d/H/NonDeC;NH2_rad
""",
)

entry(
    index = 673,
    label = "H + CH3N-2 <=> H2_p + CH2N-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (6e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (25.6479, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: H2CNH + H = HCNH + H2 (B&D #48b1) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: Cd/H2/NonDeN;H_rad
""",
)

entry(
    index = 674,
    label = "CH3N-2 + O_rad <=> HO + CH2N-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (4.4e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (108.617, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: H2CNH + O = HCNH + OH (B&D #48b2)  in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: Cd/H2/NonDeN;O_atom_triplet
""",
)

entry(
    index = 675,
    label = "OH_r3 + CH3N-2 <=> H2O_p23 + CH2N-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (4.8e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (101.378, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: H2CNH + OH = HCNH + H2O (B&D #48b3) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: Cd/H2/NonDeN;O_pri_rad
""",
)

entry(
    index = 676,
    label = "CH3N-2 + CH3_r3 <=> CH4_p23 + CH2N-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.06e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (78.8684, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: H2CNH + CH3 = HCNH + CH4 (B&D #48b4) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: Cd/H2/NonDeN;C_methyl
""",
)

entry(
    index = 677,
    label = "NH2_r3 + CH3N-2 <=> NH3_p23 + CH2N-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.6e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (25.4806, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: H2CNH + NH2_r3 = HCNH + NH3 (B&D #48b5)  in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: Cd/H2/NonDeN;NH2_rad
""",
)

entry(
    index = 678,
    label = "H + CH5N <=> H2_p + CH4N",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.68e+09, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (22.8446, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: CH3NH2 + H = CH2NH2 + H2 (B&D #51a1) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: Cs/H3/NonDeN;H_rad
""",
)

entry(
    index = 679,
    label = "CH5N + O_rad <=> HO + CH4N",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.2e+09, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (21.7568, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: CH3NH2 + O = CH2NH2 + OH (B&D #51a2) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: Cs/H3/NonDeN;O_atom_triplet
""",
)

entry(
    index = 680,
    label = "OH_r3 + CH5N <=> H2O_p23 + CH4N",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.08e+07, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (2.05016, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: CH3NH2 + OH = CH2NH2 + H2O (B&D #51a3) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: Cs/H3/NonDeN;O_pri_rad
""",
)

entry(
    index = 681,
    label = "CH3_r3 + CH5N <=> CH4_p23 + CH4N",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (4.5e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (38.3673, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: CH3NH2 + CH3 = CH2NH2 + CH4 (B&D #51a4) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: Cs/H3/NonDeN;C_methyl
""",
)

entry(
    index = 682,
    label = "NH2_r3 + CH5N <=> NH3_p23 + CH4N",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (8.4e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (22.9702, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: CH3NH2 + NH2_r3 = CH2NH2 + NH3 (B&D #51a5) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: Cs/H3/NonDeN;NH2_rad
""",
)

entry(
    index = 683,
    label = "H + CH5N-2 <=> H2_p + CH4N-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (9.6e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (40.6266, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: CH3NH2 + H = CH3NH + H2 (B&D #51b1) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3s/H2/NonDeC;H_rad
""",
)

entry(
    index = 684,
    label = "CH5N-2 + O_rad <=> HO + CH4N-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (6.6e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (85.157, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: CH3NH2 + O = CH3NH + OH (B&D #51b2) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3s/H2/NonDeC;O_atom_triplet
""",
)

entry(
    index = 685,
    label = "OH_r3 + CH5N-2 <=> H2O_p23 + CH4N-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (4.8e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (77.9186, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: CH3NH2 + OH = CH3NH + H2O (B&D #51b3) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3s/H2/NonDeC;O_pri_rad
""",
)

entry(
    index = 686,
    label = "CH3_r3 + CH5N-2 <=> CH4_p23 + CH4N-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.2e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (55.4087, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: CH3NH2 + CH3 = CH3NH + CH4 (B&D #51b4) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3s/H2/NonDeC;C_methyl
""",
)

entry(
    index = 687,
    label = "NH2_r3 + CH5N-2 <=> NH3_p23 + CH4N-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.6e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (29.8738, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: CH3NH2 + NH2_r3 = CH3NH + NH3 (B&D #51b5) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3s/H2/NonDeC;NH2_rad
""",
)

entry(
    index = 688,
    label = "H2 + CNO <=> HNCO + H",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1520, 'cm^3/(mol*s)'),
        n = 3,
        Ea = (16.6105, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: NCO + H2 = HNCO + H (B&D #53c) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: H2;N3d_rad/OneDeCdd_O
""",
)

entry(
    index = 689,
    label = "CH4_r12 + CNO <=> HNCO + CH3_p1",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (3.92e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (34.0159, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: NCO + CH4 = HNCO + CH3 (B&D #53i) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: C_methane;N3d_rad/OneDeCdd_O
""",
)

entry(
    index = 690,
    label = "NH3_r12 + CNO <=> HNCO + NH2_p23",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (84000, 'cm^3/(mol*s)'),
        n = 2.48,
        Ea = (30.7106, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: NCO + NH3 = HNCO + NH2_r3 (B&D #53j) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: NH3;N3d_rad/OneDeCdd_O
""",
)

entry(
    index = 691,
    label = "H + C2H4O-2 <=> H2 + C2H3O-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.4e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (27.6981, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: HOCN + H = H2 + NCO (B&D #55d) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: O/H/OneDeC;H_rad
""",
)

entry(
    index = 692,
    label = "C2H4O-2 + O_rad <=> HO + C2H3O-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.7e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (17.2799, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: HOCN + O = OH + NCO (B&D #55e) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: O/H/OneDeC;O_atom_triplet
""",
)

entry(
    index = 693,
    label = "OH_r3 + C2H4O-2 <=> H2O_p23 + C2H3O-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.2e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1.046, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: HOCN + OH = H2O + NCO (B&D #55f) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: O/H/OneDeC;O_pri_rad
""",
)

entry(
    index = 694,
    label = "C2H4O-2 + CH3_r3 <=> CH4_p23 + C2H3O-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (820000, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (27.6981, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: HOCN + CH3 = CH4 + NCO (B&D #55g) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: O/H/OneDeC;C_methyl
""",
)

entry(
    index = 695,
    label = "NH2_r3 + C2H4O-2 <=> NH3_p23 + C2H3O-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (920000, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (15.2716, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: HOCN + NH2_r3 = NH3 + NCO (B&D #55h) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: O/H/OneDeC;NH2_rad
""",
)

entry(
    index = 696,
    label = "OH_r3 + HNCO <=> H2O_p23 + CNO",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.2e+10, 'cm^3/(mol*s)'),
        n = -0.03,
        Ea = (78.7136, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: HNCO + OH = NCO + H2O (B&D #56d2) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3d/H/CddO;O_pri_rad
""",
)

entry(
    index = 697,
    label = "H + HNCO <=> H2 + CNO",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (180000, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (41.5053, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: HNCO + H = NCO + H2 (B&D #56e) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3d/H/CddO;H_rad
""",
)

entry(
    index = 698,
    label = "HNCO + O_rad <=> HO + CNO",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.1e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (85.9519, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: HNCO + O = NCO + OH (B&D #56f) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3d/H/CddO;O_atom_triplet
""",
)

entry(
    index = 699,
    label = "HNCO + CH3_r3 <=> CH4_p23 + CNO",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (56.2037, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: HNCO + CH3 = NCO + CH4 (B&D #56h) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3d/H/CddO;C_methyl
""",
)

entry(
    index = 700,
    label = "NH2_r3 + HNCO <=> NH3_p23 + CNO",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (37.405, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: HNCO + NH2_r3 = NCO + NH3 (B&D #56i) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3d/H/CddO;NH2_rad
""",
)

entry(
    index = 702,
    label = "H + C2H5N <=> H2 + C2H4N-2",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.32e+09, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (1.58992, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: CH3NO + H = CH2NO + H2 (B&D #58a) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: Cs/H3/OneDeN;H_rad
""",
)

entry(
    index = 703,
    label = "C2H5N + O_rad <=> HO + C2H4N-2",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (9.9e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (27.6144, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: CH3NO + O = CH2NO + OH (B&D #58b) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: Cs/H3/OneDeN;O_atom_triplet
""",
)

entry(
    index = 704,
    label = "OH_r3 + C2H5N <=> H2O_p23 + C2H4N-2",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.08e+07, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-4.97896, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: CH3NO + OH = CH2NO + H2O (B&D #58c) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: Cs/H3/OneDeN;O_pri_rad
""",
)

entry(
    index = 705,
    label = "CH3_r3 + C2H5N <=> CH4_p23 + C2H4N-2",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (2.37e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (22.6354, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: CH3NO + CH3 = CH2NO + CH4 (B&D #58d) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: Cs/H3/OneDeN;C_methyl
""",
)

entry(
    index = 706,
    label = "NH2_r3 + C2H5N <=> NH3_p23 + C2H4N-2",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (8.4e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (4.47688, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: CH3NO + NH2_r3 = CH2NO + NH3 (B&D #58e) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: Cs/H3/OneDeN;NH2_rad
""",
)

entry(
    index = 707,
    label = "H + H3NO <=> H2 + H2NO",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (9.6e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (26.15, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: NH2OH + H = HNOH + H2 (B&D #61b1) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3s/H2/NonDeO;H_rad
""",
)

entry(
    index = 708,
    label = "H3NO + O_rad <=> HO + H2NO",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (6.6e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (51.5594, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: NH2OH + O = HNOH + OH (B&D #61c1) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3s/H2/NonDeO;O_atom_triplet
""",
)

entry(
    index = 709,
    label = "OH_r3 + H3NO <=> H2O_p23 + H2NO",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (4.8e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1.38072, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: NH2OH + OH = HNOH + H2O (B&D #61d1) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3s/H2/NonDeO;O_pri_rad
""",
)

entry(
    index = 710,
    label = "H3NO + CH3_r3 <=> CH4_p23 + H2NO",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.2e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (26.5684, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: NH2OH + CH3 = HNOH + CH4 (B&D #61e1) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3s/H2/NonDeO;C_methyl
""",
)

entry(
    index = 711,
    label = "NH2_r3 + H3NO <=> NH3_p23 + H2NO",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.6e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (13.5143, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: NH2OH + NH2_r3 = HNOH + NH3 (B&D #61f1)  in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3s/H2/NonDeO;NH2_rad
""",
)

entry(
    index = 712,
    label = "HO2_r3 + H3NO <=> H2O2 + H2NO",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (58000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (39.999, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: NH2OH + HO2 = HNOH + H2O2 (B&D #61g1) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3s/H2/NonDeO;O_rad/NonDeO
""",
)

entry(
    index = 713,
    label = "H + H3NO-2 <=> H2 + H2NO-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.4e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (21.2129, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: NH2OH + H = NH2O + H2 (B&D #61b2) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: O/H/NonDeN;H_rad
""",
)

entry(
    index = 714,
    label = "H3NO-2 + O_rad <=> HO + H2NO-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.7e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (103.596, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: NH2OH + O = NH2O + OH (B&D #61c2) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: O/H/NonDeN;O_atom_triplet
""",
)

entry(
    index = 715,
    label = "OH_r3 + H3NO-2 <=> H2O_p23 + H2NO-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.2e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-2.5104, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: NH2OH + OH = NH2O + H2O (B&D #61d2) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: O/H/NonDeN;O_pri_rad
""",
)

entry(
    index = 716,
    label = "H3NO-2 + CH3_r3 <=> CH4_p23 + H2NO-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (820000, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (73.8476, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: NH2OH + CH3 = NH2O + CH4 (B&D #61e2) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: O/H/NonDeN;C_methyl
""",
)

entry(
    index = 717,
    label = "NH2_r3 + H3NO-2 <=> NH3_p23 + H2NO-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (920000, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (7.90776, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: NH2OH + NH2_r3 = NH2O + NH3 (B&D #61f2) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: O/H/NonDeN;NH2_rad
""",
)

entry(
    index = 718,
    label = "HO2_r3 + H3NO-2 <=> H2O2 + H2NO-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (14000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (65.3541, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: NH2OH + HO2 = NH2O + H2O2 (B&D #61g2) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: O/H/NonDeN;O_rad/NonDeO
""",
)

entry(
    index = 719,
    label = "H + CH4N2 <=> H2 + CH3N2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (9.6e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (31.0034, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: NH2NO + H = HNNO + H2 (B&D #62b) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3s/H2/OneDeN;H_rad
""",
)

entry(
    index = 720,
    label = "CH4N2 + O_rad <=> HO + CH3N2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (6.6e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (40.0953, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: NH2NO + O = HNNO + OH (B&D #62c) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3s/H2/OneDeN;O_atom_triplet
""",
)

entry(
    index = 721,
    label = "OH_r3 + CH4N2 <=> H2O_p23 + CH3N2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (4.8e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-0.29288, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: NH2NO + OH = HNNO + H2O (B&D #62d) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3s/H2/OneDeN;O_pri_rad
""",
)

entry(
    index = 722,
    label = "CH3_r3 + CH4N2 <=> CH4_p23 + CH3N2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.2e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (30.0411, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: NH2NO + CH3 = HNNO + CH4 (B&D #62e) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3s/H2/OneDeN;C_methyl
""",
)

entry(
    index = 723,
    label = "NH2_r3 + CH4N2 <=> NH3_p23 + CH3N2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.6e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (18.9954, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: NH2NO + NH2_r3 = HNNO + NH3 (B&D #62f) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3s/H2/OneDeN;NH2_rad
""",
)

entry(
    index = 724,
    label = "HO2_r3 + CH4N2 <=> H2O2 + CH3N2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (58000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (52.8439, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: NH2NO + HO2 = HNNO + H2O2 (B&D #62g) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3s/H2/OneDeN;O_rad/NonDeO
""",
)

entry(
    index = 725,
    label = "HO2_r3 + N2H4_r12 <=> H2O2 + N2H3_p1",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (116000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-6.6944, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc =
u"""
Added by Beat Buesser, value for reaction: H2NNHO + HO2 = HNNHO + H2O2 (B&D #63g) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",

Converted to training reaction from rate rule: N3s/H2/NonDeN;O_rad/NonDeO
""",
)

entry(
    index = 726,
    label = "OH_r3 + C7H12 <=> H2O_p23 + C7H11",
    degeneracy = 8.0,
    kinetics = Arrhenius(
        A = (688800, 'cm^3/(mol*s)'),
        n = 2.38,
        Ea = (-7.5312, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte BMK/6-311G(2,d,p) OH + JP10""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_1;O_pri_rad
""",
)

entry(
    index = 727,
    label = "OH_r3 + C7H12-2 <=> H2O_p23 + C7H11-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (556000, 'cm^3/(mol*s)'),
        n = 2.38,
        Ea = (-4.184, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte BMK/6-311G(2,d,p) OH + JP10""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_fused6;O_pri_rad
""",
)

entry(
    index = 728,
    label = "OH_r3 + C7H12-3 <=> H2O_p23 + C7H11-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (168800, 'cm^3/(mol*s)'),
        n = 2.38,
        Ea = (-3.7656, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte BMK/6-311G(2,d,p) OH + JP10""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_2;O_pri_rad
""",
)

entry(
    index = 729,
    label = "OH_r3 + C8H14 <=> H2O_p23 + C8H13",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (113400, 'cm^3/(mol*s)'),
        n = 2.38,
        Ea = (-11.2968, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte BMK/6-311G(2,d,p) OH + JP10""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_adj5;O_pri_rad
""",
)

entry(
    index = 730,
    label = "OH_r3 + C9H16 <=> H2O_p23 + C9H15",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (275200, 'cm^3/(mol*s)'),
        n = 2.38,
        Ea = (-6.6944, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte BMK/6-311G(2,d,p) OH + JP10""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_alpha6ring;O_pri_rad
""",
)

entry(
    index = 731,
    label = "OH_r3 + C9H16-2 <=> H2O_p23 + C9H15-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (302000, 'cm^3/(mol*s)'),
        n = 2.38,
        Ea = (-6.276, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte BMK/6-311G(2,d,p) OH + JP10""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_beta6ring;O_pri_rad
""",
)

entry(
    index = 732,
    label = "H + C7H12 <=> H2 + C7H11",
    degeneracy = 8.0,
    kinetics = Arrhenius(
        A = (22960, 'cm^3/(mol*s)'),
        n = 3.02,
        Ea = (18.828, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte BMK/6-311G(2,d,p) H + JP10""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_1;H_rad
""",
)

entry(
    index = 733,
    label = "H + C7H12-2 <=> H2 + C7H11-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (9040, 'cm^3/(mol*s)'),
        n = 3.02,
        Ea = (34.7272, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte BMK/6-311G(2,d,p) H + JP10""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_fused6;H_rad
""",
)

entry(
    index = 734,
    label = "H + C7H12-3 <=> H2 + C7H11-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (6360, 'cm^3/(mol*s)'),
        n = 3.02,
        Ea = (32.2168, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte BMK/6-311G(2,d,p) H + JP10""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_fused6_2;H_rad
""",
)

entry(
    index = 735,
    label = "H + C8H14 <=> H2 + C8H13",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (7680, 'cm^3/(mol*s)'),
        n = 3.02,
        Ea = (15.8992, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte BMK/6-311G(2,d,p) H + JP10""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs3_5ring_adj5;H_rad
""",
)

entry(
    index = 736,
    label = "H + C9H16 <=> H2 + C9H15",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (8880, 'cm^3/(mol*s)'),
        n = 3.02,
        Ea = (22.1752, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte BMK/6-311G(2,d,p) H + JP10""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_alpha6ring;H_rad
""",
)

entry(
    index = 737,
    label = "H + C9H16-2 <=> H2 + C9H15-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (8040, 'cm^3/(mol*s)'),
        n = 3.02,
        Ea = (20.5016, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte BMK/6-311G(2,d,p) H + JP10""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/NonDeC_5ring_beta6ring;H_rad
""",
)

entry(
    index = 738,
    label = "C3H6 + C7H11 <=> C7H12 + C3H5",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (0.002442, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (28.4512, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte BMK""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H3/Cd;C_rad/H/NonDeC_5ring_fused6_1
""",
)

entry(
    index = 739,
    label = "C3H6 + C8H13 <=> C8H14 + C3H5",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (0.001323, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (24.6856, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte BMK""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H3/Cd;C_rad/Cs3_5ring_adj5
""",
)

entry(
    index = 740,
    label = "C3H6 + C9H15 <=> C9H16 + C3H5",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (0.000948, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (34.3088, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte BMK""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H3/Cd;C_rad/H/NonDeC_5ring_alpha6ring
""",
)

entry(
    index = 741,
    label = "C3H6 + C9H15-2 <=> C9H16-2 + C3H5",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (0.0002901, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (31.7984, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte BMK""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H3/Cd;C_rad/H/NonDeC_5ring_beta6ring
""",
)

entry(
    index = 742,
    label = "C3H6 + C7H11-3 <=> C7H12-3 + C3H5",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (0.001323, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (24.6856, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte BMK""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H3/Cd;C_rad/H/NonDeC_5ring_fused6_2
""",
)

entry(
    index = 743,
    label = "C3H6 + C7H11-2 <=> C7H12-2 + C3H5",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (0.001323, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (24.6856, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte BMK""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H3/Cd;C_rad/Cs3_5ring_fused6
""",
)

entry(
    index = 744,
    label = "C5H8-2 + C7H11 <=> C7H12 + C5H7-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.001628, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (28.4512, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Estimated value""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/CdCd;C_rad/H/NonDeC_5ring_fused6_1
""",
)

entry(
    index = 745,
    label = "C5H8-2 + C8H13 <=> C8H14 + C5H7-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.000882, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (24.6856, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Estimated value""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/CdCd;C_rad/Cs3_5ring_adj5
""",
)

entry(
    index = 746,
    label = "C5H8-2 + C9H15 <=> C9H16 + C5H7-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.000632, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (34.3088, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Estimated value""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/CdCd;C_rad/H/NonDeC_5ring_alpha6ring
""",
)

entry(
    index = 747,
    label = "C5H8-2 + C9H15-2 <=> C9H16-2 + C5H7-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.0001934, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (31.7984, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Estimated value""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/CdCd;C_rad/H/NonDeC_5ring_beta6ring
""",
)

entry(
    index = 748,
    label = "C5H8-2 + C7H11-2 <=> C7H12-2 + C5H7-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.000882, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (24.6856, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Estimated value""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/CdCd;C_rad/Cs3_5ring_fused6
""",
)

entry(
    index = 749,
    label = "C5H8-2 + C7H11-3 <=> C7H12-3 + C5H7-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.000882, 'cm^3/(mol*s)'),
        n = 4.24,
        Ea = (24.6856, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Estimated value""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/CdCd;C_rad/H/NonDeC_5ring_fused6_2
""",
)

entry(
    index = 750,
    label = "H + C3H8O-2 <=> H2 + C3H7O-2",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (1.134e+07, 'cm^3/(mol*s)'),
        n = 2.21,
        Ea = (31.38, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""MRH CBS-QB3 with 1-dHR corrections ref: doi: 10.1021/ie1005349""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H3/Cs\H\Cs\O;H_rad
""",
)

entry(
    index = 751,
    label = "H + C3H8O-3 <=> H2 + C3H7O-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (414000, 'cm^3/(mol*s)'),
        n = 2.34,
        Ea = (11.2131, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""MRH CBS-QB3 with 1-dHR corrections ref: doi: 10.1021/ie1005349""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs2O;H_rad
""",
)

entry(
    index = 752,
    label = "C3H8O-2 + CH3_r3 <=> CH4_p23 + C3H7O-2",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (2.838, 'cm^3/(mol*s)'),
        n = 3.6,
        Ea = (46.2332, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""MRH CBS-QB3 with 1-dHR corrections ref: doi: 10.1021/ie1005349""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H3/Cs\H\Cs\O;C_methyl
""",
)

entry(
    index = 753,
    label = "C3H8O-3 + CH3_r3 <=> CH4_p23 + C3H7O-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.389, 'cm^3/(mol*s)'),
        n = 3.53,
        Ea = (16.7778, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""MRH CBS-QB3 with 1-dHR corrections ref: doi: 10.1021/ie1005349""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs2O;C_methyl
""",
)

entry(
    index = 754,
    label = "H + C4H8-4 <=> H2 + C4H7-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (45000, 'cm^3/(mol*s)'),
        n = 2.67,
        Ea = (14.5603, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""MRH CBS-QB3 with 1-dHR corrections ref: doi: 10.1021/ie1005349""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/CdCs;H_rad
""",
)

entry(
    index = 755,
    label = "CH3_r3 + C4H8-4 <=> CH4_p23 + C4H7-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.204, 'cm^3/(mol*s)'),
        n = 3.99,
        Ea = (26.2337, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""MRH CBS-QB3 with 1-dHR corrections ref: doi: 10.1021/ie1005349""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/CdCs;C_methyl
""",
)

entry(
    index = 756,
    label = "H + C3H6 <=> H2 + C3H5",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (3360, 'cm^3/(mol*s)'),
        n = 3.14,
        Ea = (17.9494, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""same as rule 3072. ref: doi: 10.1021/ie1005349""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H3/Cd\H_Cd\H2;H_rad
""",
)

entry(
    index = 757,
    label = "H + C4H8-2 <=> H2 + C4H7-2",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (6720, 'cm^3/(mol*s)'),
        n = 3.14,
        Ea = (17.9494, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""MRH CBS-QB3 with 1-dHR corrections ref: doi: 10.1021/ie1005349""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H3/Cd\H_Cd\H\Cs;H_rad
""",
)

entry(
    index = 758,
    label = "CH3_r3 + C3H6 <=> CH4_p23 + C3H5",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (0.072, 'cm^3/(mol*s)'),
        n = 4.25,
        Ea = (31.5055, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""same as rule 3072. ref: doi: 10.1021/ie1005349""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H3/Cd\H_Cd\H2;C_methyl
""",
)

entry(
    index = 759,
    label = "CH3_r3 + C4H8-2 <=> CH4_p23 + C4H7-2",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (0.144, 'cm^3/(mol*s)'),
        n = 4.25,
        Ea = (31.5055, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""MRH CBS-QB3 with 1-dHR corrections ref: doi: 10.1021/ie1005349""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H3/Cd\H_Cd\H\Cs;C_methyl
""",
)

entry(
    index = 760,
    label = "H + C4H8 <=> H2 + C4H7",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (5028, 'cm^3/(mol*s)'),
        n = 3.18,
        Ea = (18.2841, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""MRH CBS-QB3 with 1-dHR corrections ref: doi: 10.1021/ie1005349""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H3/Cd\Cs_Cd\H2;H_rad
""",
)

entry(
    index = 761,
    label = "CH3_r3 + C4H8 <=> CH4_p23 + C4H7",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (0.1188, 'cm^3/(mol*s)'),
        n = 4.26,
        Ea = (31.5892, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""MRH CBS-QB3 with 1-dHR corrections ref: doi: 10.1021/ie1005349""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H3/Cd\Cs_Cd\H2;C_methyl
""",
)

entry(
    index = 762,
    label = "C3H6-2 + C2H5 <=> C2H6 + C3H5-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.00128, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (70.5004, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc =
u"""
Converted to training reaction from rate rule: Cd/H/NonDeC;C_rad/H2/Cs
""",
)

entry(
    index = 763,
    label = "C3H6-2 + C3H7 <=> C3H8 + C3H5-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.00148, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (59.5383, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc =
u"""
Converted to training reaction from rate rule: Cd/H/NonDeC;C_rad/H/NonDeC
""",
)

entry(
    index = 764,
    label = "C3H6-2 + C4H9-4 <=> iC4H10b + C3H5-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.00148, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (55.0196, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc =
u"""
Converted to training reaction from rate rule: Cd/H/NonDeC;C_rad/Cs3
""",
)

entry(
    index = 765,
    label = "OH_r3 + C2H6O <=> H2O_p23 + C2H5O",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (4.32e+06, 'cm^3/(mol*s)'),
        n = 2.002,
        Ea = (-0.472792, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""iBuOH + OH (communication from truhlar group) refitted to arrhenius form""",
    longDesc =
u"""
""",
)

entry(
    index = 766,
    label = "OH_r3 + C4H10O-10 <=> H2O_p23 + C4H9O-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (34760, 'cm^3/(mol*s)'),
        n = 2.458,
        Ea = (-0.64852, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""iBuOH + OH (communication from truhlar group) refitted to arrhenius form""",
    longDesc =
u"""
""",
)

entry(
    index = 767,
    label = "H + CH4O-2 <=> H2 + CH3O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.293, 'cm^3/(mol*s)'),
        n = 4.14,
        Ea = (20.0832, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""iBuOH AG Vandeputte CBS-QB3 1dHR """,
    longDesc =
u"""
""",
)

entry(
    index = 768,
    label = "H + C2H6O <=> H2 + C2H5O",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (5220, 'cm^3/(mol*s)'),
        n = 3.04,
        Ea = (10.46, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""iBuOH AG Vandeputte CBS-QB3 1dHR """,
    longDesc =
u"""
""",
)

entry(
    index = 769,
    label = "H + C4H10O-10 <=> H2 + C4H9O-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5760, 'cm^3/(mol*s)'),
        n = 3.02,
        Ea = (14.644, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""iBuOH AG Vandeputte CBS-QB3 1dHR """,
    longDesc =
u"""
""",
)

entry(
    index = 770,
    label = "H + C2H6 <=> H2 + C2H5",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (6180, 'cm^3/(mol*s)'),
        n = 3.24,
        Ea = (29.7064, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""iBuOH AG Vandeputte CBS-QB3 1dHR """,
    longDesc =
u"""
""",
)

entry(
    index = 771,
    label = "CH3_r3 + C2H6 <=> CH4_p23 + C2H5",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (4.488e-05, 'cm^3/(mol*s)'),
        n = 4.99,
        Ea = (33.472, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""iBuOH & iPtOH AG Vandeputte CBS-QB3 1dHR""",
    longDesc =
u"""
""",
)

entry(
    index = 772,
    label = "C4H10O-10 + CH3_r3 <=> CH4_p23 + C4H9O-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.0146, 'cm^3/(mol*s)'),
        n = 4.47,
        Ea = (30.1248, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""iBuOH & iPtOH AG Vandeputte CBS-QB3 1dHR""",
    longDesc =
u"""
""",
)

entry(
    index = 773,
    label = "C5H12O + CH3_r3 <=> CH4_p23 + C5H11O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.0719, 'cm^3/(mol*s)'),
        n = 3.96,
        Ea = (32.175, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""iBuOH & iPtOH AG Vandeputte CBS-QB3 1dHR""",
    longDesc =
u"""
Value for ipentanol, x3 lower mainly because of gamma O restricting rotation of abstracting methyl
""",
)

entry(
    index = 774,
    label = "C2H6O + CH3_r3 <=> CH4_p23 + C2H5O",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.00248, 'cm^3/(mol*s)'),
        n = 4.44,
        Ea = (18.828, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""iBuOH & iPtOH AG Vandeputte CBS-QB3 1dHR""",
    longDesc =
u"""
""",
)

entry(
    index = 775,
    label = "C2H3 + C2H6 <=> C2H4 + C2H5",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (0.00108, 'cm^3/(mol*s)'),
        n = 4.55,
        Ea = (14.644, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""SSM CBS-QB3 with 1-dHR corrections""",
    longDesc =
u"""
""",
)

entry(
    index = 776,
    label = "C2H3 + C2H6O <=> C2H4 + C2H5O",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.052, 'cm^3/(mol*s)'),
        n = 3.9,
        Ea = (3.59824, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""SSM CBS-QB3 with 1-dHR corrections""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/CsO;Cd_Cd\H2_pri_rad
""",
)

entry(
    index = 777,
    label = "C4H10O-10 + O_rad <=> HO + C4H9O-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (78000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (27.5672, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 11,
    shortDesc = u"""iso-butane + O = OH + tert-C4H9""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H/Cs2/Cs\O;O_atom_triplet
""",
)

entry(
    index = 778,
    label = "C4H10O-11 + O_rad <=> HO + C4H9O-11",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (145000, 'cm^3/(mol*s)'),
        n = 2.47,
        Ea = (30.9286, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 11,
    shortDesc = u"""C2H5OH+O=OH+CH3CHOH""",
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/Cs\Cs2/O;O_atom_triplet
""",
)

entry(
    index = 780,
    label = "H2O2 + C4H9O-10 <=> C4H10O-10 + HO2_r3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.91, 'cm^3/(mol*s)'),
        n = 3.31,
        Ea = (10.6746, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 11,
    shortDesc = u"""SSM CBS-QB3 without 1-dHR corrections""",
    longDesc =
u"""
Converted to training reaction from rate rule: H2O2;C_rad/Cs2/Cs\O
""",
)

entry(
    index = 781,
    label = "H2O2 + C2H5O <=> C2H6O + HO2_r3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (57, 'cm^3/(mol*s)'),
        n = 3.04,
        Ea = (7.3132, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 11,
    shortDesc = u"""SSM CBS-QB3 without 1-dHR corrections""",
    longDesc =
u"""
Converted to training reaction from rate rule: H2O2;C_rad/H/CsO
""",
)

entry(
    index = 782,
    label = "C3H8O-4 + O_rad <=> HO + C3H7O-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (169, 'cm^3/(mol*s)'),
        n = 3.43,
        Ea = (62.3897, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 11,
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/Cs/Cs\O;O_atom_triplet
""",
)

entry(
    index = 783,
    label = "OH_r3 + C3H8O-4 <=> H2O_p23 + C3H7O-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (28.7, 'cm^3/(mol*s)'),
        n = 3.42,
        Ea = (-5.25092, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CCSD(T)-F12a/pVTZ with MS-VTST treatment for rotors""",
    longDesc =
u"""
Seal, Prasenjit Oyedepo, Gbenga Truhlar, Donald G
doi: 10.1021/jp310910f

Converted to training reaction from rate rule: C/H2/Cs/Cs\O;O_pri_rad
""",
)

entry(
    index = 784,
    label = "OH_r3 + C4H10O-2 <=> H2O_p23 + C4H9O-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (26, 'cm^3/(mol*s)'),
        n = 3.44,
        Ea = (-10.2173, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CCSD(T)-F12a/pVTZ with MS-VTST treatment for rotors""",
    longDesc =
u"""
Seal, Prasenjit Oyedepo, Gbenga Truhlar, Donald G
doi: 10.1021/jp310910f

Converted to training reaction from rate rule: C/H2/Cs/Cs\Cs|O;O_pri_rad
""",
)

entry(
    index = 785,
    label = "C4H10O-2 + O_rad <=> HO + C4H9O-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (169, 'cm^3/(mol*s)'),
        n = 3.43,
        Ea = (57.4045, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 11,
    longDesc =
u"""
Converted to training reaction from rate rule: C/H2/Cs/Cs\Cs|O;O_atom_triplet
""",
)

entry(
    index = 3073,
    label = "NO3 + C3H4 <=> C3H3-2_p + HNO3_p",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (4.86, 'm^3/(mol*s)'),
        n = 1.87,
        Ea = (32393.57, 'J/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli""",
    longDesc =
u"""
Degeneracy not recalculated

Converted to training reaction manually from rate rule: C/H3/Ct;InChI=1S/NO3/c2-1(3)4
""",
)

entry(
    index = 3074,
    label = "HNO2 + H <=> H2_p + NO2_p",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.4e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (4.16, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Added by Beat Buesser, value for reaction: HNO2 + H = H2 + NO2 (B&D #41a) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli""",
    longDesc =
u"""
Converted to training reaction manually from rate rule: N5dc/H/NonDeOO;H_rad
""",
)

entry(
    index = 3075,
    label = "HNO2 + O_rad <=> OH_p23 + NO2_p",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.7e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (2.36, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Added by Beat Buesser, value for reaction: HNO2 + O = OH + NO2 (B&D #41b) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli""",
    longDesc =
u"""
Converted to training reaction manually from rate rule: N5dc/H/NonDeOO;O_atom_triplet
""",
)

entry(
    index = 3076,
    label = "HNO2 + OH_r3 <=> H2O_p23 + NO2_p",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.2e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-0.79, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Added by Beat Buesser, value for reaction: HNO2 + OH = H2O + NO2 (B&D #41c) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli""",
    longDesc =
u"""
Converted to training reaction manually from rate rule: N5dc/H/NonDeOO;O_pri_rad
""",
)

entry(
    index = 3077,
    label = "HNO2 + CH3_r3 <=> CH4_p23 + NO2_p",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (810000, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (4.84, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Added by Beat Buesser, value for reaction: HNO2 + CH3 = NO2 + CH4 (B&D #41d) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli""",
    longDesc =
u"""
Converted to training reaction manually from rate rule: N5dc/H/NonDeOO;C_methyl
""",
)

entry(
    index = 3078,
    label = "HNO2 + NH2_r3 <=> NH3_p23 + NO2_p",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (920000, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (0.87, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Added by Beat Buesser, value for reaction: HNO2 + NH2_r3 = NO2 + NH3 (B&D #413) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli""",
    longDesc =
u"""
Converted to training reaction manually from rate rule: N5dc/H/NonDeOO;NH2_rad
""",
)

entry(
    index = 3079,
    label = "N2H3_r12 + NH2_r3 <=> H2N2-3 + NH3_p23",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.65e+00, 'cm^3/(mol*s)'), n=3.41, Ea=(-4.0, 'kJ/mol'),
        T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K'),
        comment = 'Fitted to 51 data points; dA = *|/ 1.13644, dn = +|- 0.0159552, dEa = +|- 0.120945 kJ/mol'),
    rank = 3,
    shortDesc = u"""CCSD(T)-F12a/aug-cc-pVTZ//wB97x-D3/6-311++G(3df,3pd)""",
    longDesc =
u"""
Calculated by alongd (xq1453 f)
opt, freq: wB97x-D3/6-311++G(3df,3pd)
sp: CCSD(T)-F12a/aug-cc-pVTZ
rotors: B3LYP/6-311++G(3df,3pd)
""",
)

entry(
    index = 3080,
    label = "H2NN(T)_r3 + NH3_r12 <=> N2H3_p23 + NH2_p1",
    degeneracy = 3,
    kinetics = Arrhenius(A=(7.14e+00, 'cm^3/(mol*s)'), n=3.59, Ea=(81.1, 'kJ/mol'),
        T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K'),
        comment = 'Fitted to 51 data points; dA = *|/ 1.04766, dn = +|- 0.00580835, dEa = +|- 0.044029 kJ/mol'),
    rank = 3,
    shortDesc = u"""CCSD(T)-F12a/aug-cc-pVTZ//wB97x-D3/6-311++G(3df,3pd)""",
    longDesc =
u"""
Calculated by alongd (xq1453 r)
opt, freq: wB97x-D3/6-311++G(3df,3pd)
sp: CCSD(T)-F12a/aug-cc-pVTZ
rotors: B3LYP/6-311++G(3df,3pd)
""",
)

entry(
    index = 3081,
    label = "N2H3_r3 + NH2_r12 <=> N2H4_p23 + NH_p1",
    degeneracy = 2,
    kinetics = Arrhenius(A=(2.31e-01, 'cm^3/(mol*s)'), n=3.93, Ea=(70.1, 'kJ/mol'),
        T0=(1, 'K'), Tmin=(500, 'K'), Tmax=(3000, 'K'),
        comment = 'Fitted to 51 data points; dA = *|/ 1.2035, dn = +|- 0.0225658, dEa = +|- 0.225133 kJ/mol'),
    rank = 3,
    shortDesc = u"""CCSD(T)-F12a/aug-cc-pVTZ//wB97x-D3/6-311++G(3df,3pd)""",
    longDesc =
u"""
Calculated by alongd (xq1330 f)
opt, freq: wB97x-D3/6-311++G(3df,3pd)
sp: CCSD(T)-F12a/aug-cc-pVTZ
rotors: B3LYP/6-311++G(3df,3pd)
""",
)

entry(
    index = 3082,
    label = "N2H4_r12 + NH_r3 <=> N2H3_p1 + NH2_p23",
    degeneracy = 4,
    kinetics = Arrhenius(A=(2.98e+01, 'cm^3/(mol*s)'), n=3.61, Ea=(24.3, 'kJ/mol'),
        T0=(1, 'K'), Tmin=(500, 'K'), Tmax=(3000, 'K'),
        comment = 'Fitted to 51 data points; dA = *|/ 1.21122, dn = +|- 0.0233453, dEa = +|- 0.232911 kJ/mol'),
    rank = 3,
    shortDesc = u"""CCSD(T)-F12a/aug-cc-pVTZ//wB97x-D3/6-311++G(3df,3pd)""",
    longDesc =
u"""
Calculated by alongd (xq1330 r)
opt, freq: wB97x-D3/6-311++G(3df,3pd)
sp: CCSD(T)-F12a/aug-cc-pVTZ
rotors: B3LYP/6-311++G(3df,3pd)
""",
)

entry(
    index = 3083,
    label = "NH2_r12 + N2H2(T)_r3 = NH_p1 + N2H3_p23",
    degeneracy = 2,
    kinetics = Arrhenius(A=(4.22e-01, 'cm^3/(mol*s)'), n=3.93, Ea=(70.1, 'kJ/mol'),
        T0=(1, 'K'), Tmin=(500, 'K'), Tmax=(3000, 'K'),
        comment = 'Fitted to 51 data points; dA = *|/ 1.35051, dn = +|- 0.0366059, dEa = +|- 0.365208 kJ/mol'),
    rank = 3,
    shortDesc = u"""CCSD(T)-F12a/aug-cc-pVTZ//wB97x-D3/6-311++G(3df,3pd)""",
    longDesc =
u"""
Calculated by alongd (xq1485 f)
opt, freq: wB97x-D3/6-311++G(3df,3pd)
sp: CCSD(T)-F12a/aug-cc-pVTZ
rotors: B3LYP/6-311++G(3df,3pd)
""",
)

entry(
    index = 3084,
    label = "NH_r3 + N2H3_r12b <=> NH2_p23 + N2H2(T)_p1",
    degeneracy = 4,
    kinetics = Arrhenius(A=(3.53e-01, 'cm^3/(mol*s)'), n=3.81, Ea=(40.0, 'kJ/mol'),
        T0=(1, 'K'), Tmin=(500, 'K'), Tmax=(3000, 'K'),
        comment = 'Fitted to 51 data points; dA = *|/ 1.40215, dn = +|- 0.0411776, dEa = +|- 0.410819 kJ/mol'),
    rank = 3,
    shortDesc = u"""CCSD(T)-F12a/aug-cc-pVTZ//wB97x-D3/6-311++G(3df,3pd)""",
    longDesc =
u"""
Calculated by alongd (xq1485 r)
opt, freq: wB97x-D3/6-311++G(3df,3pd)
sp: CCSD(T)-F12a/aug-cc-pVTZ
rotors: B3LYP/6-311++G(3df,3pd)
""",
)
