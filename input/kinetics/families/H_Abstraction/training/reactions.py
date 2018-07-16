#!/usr/bin/env python
# encoding: utf-8

name = "H_Abstraction/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
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
    index = 35,
    label = "H2O2 + C4H7-5 <=> HO2 + C4H8-5",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2, 'cm^3/(mol*s)'),
        n = 3.52,
        Ea = (-7.48, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
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
    label = "C3H6O-3 + OH <=> C3H5O-3 + H2O",
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
    label = "C4H8O-4 + OH <=> C4H7O-4 + H2O",
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
    label = "C4H8O-5 + OH <=> C4H7O-5 + H2O",
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
    label = "C4H8O-6 + OH <=> C4H7O-6 + H2O",
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
    label = "C5H10O + OH <=> C5H9O + H2O",
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
    label = "C5H10O-2 + OH <=> C5H9O-2 + H2O",
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
    label = "C5H10O-3 + OH <=> C5H9O-3 + H2O",
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
    label = "C4H10O-4 + OH <=> H2O + C4H9O-4",
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
    label = "CH4b + SH <=> CH3_p1 + H2S",
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
    index = 58,
    label = "C4H8-6 + SH <=> CH2CCH2CH3 + H2S",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (162, 'cm^3/(mol*s)'),
        n = 3.32,
        Ea = (36.5, 'kJ/mol'),
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
    label = "N + H2 <=> NH_p + H_p",
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
    label = "N2H4 + NO <=> N2H3 + HNO_p",
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
    label = "HNCN + OH <=> H2O_p + NCN",
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
    label = "NH3_r + NO <=> NH2_p + HNO_p",
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
    label = "NH2 + H2 <=> NH3 + H_p",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (323000, 'cm^3/(mol*s)'),
        n = 2.23,
        Ea = (7168, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (5000, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Training reaction from kinetics library: primaryNitrogenLibrary""",
    longDesc = 
u"""
A.M. Mebel, L.V. Moskaleva, M.C. Lin, J. Molec. Struc. (Theochem), 1999, 461-462, 223-238, doi: 10.1016/S0166-1280(98)00423-0
k1_theo on p. 229
calculations done at the G2M//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 68,
    label = "NH2 + CH4b <=> NH3 + CH3_p1",
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
    label = "NH2 + H2O <=> NH3 + OH_p1",
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
    index = 72,
    label = "H2 + S_rad <=> SH + H_p",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.58e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (19700, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (2740, 'K'),
        Tmax = (3570, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Training reaction from kinetics library: primarySulfurLibrary""",
    longDesc = 
u"""
Shock Tube
H. Shiina, M. Oya, K. Yamashita, A. Miyoshi, H. Matsui, J. Phys. Chem., 1996, 100(6), 2136-2140, doi: 10.1021/jp952472j
""",
)

entry(
    index = 73,
    label = "CH4b + S_rad <=> SH + CH3_p1",
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
    label = "HNO3_r + OH <=> H2O_p + NO3_p",
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
        Tmin = (500, 'K'),
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
    label = "HCN_r + OH <=> CN_p + H2O_p",
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
    label = "NH2 + C2H6 <=> NH3 + C2H5b",
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
    label = "NH2 + C3H8b <=> NH3 + CH2CH2CH3",
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
    label = "NH2 + C3H8 <=> NH3 + CH3CHCH3",
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
    label = "NH2 + C4H10 <=> NH3 + pC4H9",
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
    label = "NH2 + C4H10b <=> NH3 + CH3CHCH2CH3",
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
    label = "NH2 + iC4H10 <=> NH3 + ipC4H9",
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
    label = "NH2 + iC4H10b <=> NH3 + tC4H9",
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
    label = "NH2 + C5H12 <=> NH3 + tC5H11",
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
    label = "NH2 + C3H6-3 <=> NH3 + vC3H5",
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
    label = "NH2 + C3H6 <=> NH3 + CH2CHCH2",
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
    label = "NH2 + C4H8-7 <=> NH3 + pC4H7",
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
    label = "NH2 + C4H8-2 <=> NH3 + aC4H7",
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
    label = "NH2 + C5H10-1 <=> NH3 + C5H9-1",
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
    label = "NH2 + C5H10-2 <=> NH3 + C5H9-2",
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
    label = "NH2 + C5H10-3 <=> NH3 + C5H9-3",
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
    label = "NH2 + C5H10-4 <=> NH3 + C5H9-4",
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
    label = "NH2 + C2H4 <=> NH3 + CHCH2",
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
    label = "NH2 + C4H6 <=> NH3 + CHCCHCH3",
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
    label = "NH2 + C4H6-2 <=> NH3 + C4H5-2",
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
    label = "NH2 + C5H8 <=> NH3 + C5H7",
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
    label = "CH3CH2NH2_1 + CH3_r3 <=> CH2CH2NH2 + CH4",
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
    label = "CH3CH2NH2_2 + CH3_r3 <=> CH3CHNH2 + CH4",
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
    label = "CH3CH2NH2_3 + CH3_r3 <=> CH3CH2NH + CH4",
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
    label = "CH3CH2NH2_1 + NH2 <=> CH2CH2NH2 + NH3",
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
    label = "CH3CH2NH2_2 + NH2 <=> CH3CHNH2 + NH3",
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
    label = "CH3CH2NH2_3 + NH2 <=> CH3CH2NH + NH3",
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
    label = "CH3CH2NH2_1 + OH <=> CH2CH2NH2 + H2O",
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
    label = "CH3CH2NH2_2 + OH <=> CH3CHNH2 + H2O",
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
    label = "CH3CH2NH2_3 + OH <=> CH3CH2NH + H2O",
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
    label = "N2H4 + H <=> N2H3 + H2",
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
    label = "N2H4 + CH3_r3 <=> N2H3 + CH4",
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
    label = "N2H4 + NH2 <=> N2H3 + NH3",
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
    label = "NH + CH4b <=> NH2b + CH3_p1",
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
    label = "NH + C2H6 <=> NH2b + C2H5b",
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
    index = 130,
    label = "NH + HNCO <=> NH2b + NCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.26e+12, 'cm^3/(mol*s)'),
        n = 1.82,
        Ea = (99.82, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sun""",
    longDesc = 
u"""
calculated at UQCISD(T)/6-311G** level
Zhen-Feng Xu and Jia-Zhong Sun
Theoretical Study on the Reaction Path and Variational Rate Constant of the Reaction HNCO + NH => NCO + NH2
J. Phys. Chem. A, 1998, 102 (7), pp 1194-1199
DOI: 10.1021/jp972959n
""",
)

entry(
    index = 131,
    label = "Cl + CH4b <=> HCl + CH3_p23",
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
    index = 135,
    label = "Cl + C4H10 <=> HCl + C4H9",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (9.02e-11, 'cm^3/(molecule*s)'),
        n = 0,
        Ea = (997.737, 'J/mol'),
        T0 = (1, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Cl + nC4H10 <=> HCl + C4H9-1""",
    longDesc = 
u"""
IUPAC recommendation: http://iupac.pole-ether.fr
from 290-600 K
""",
)

entry(
    index = 136,
    label = "Cl + C4H10b <=> HCl + C4H9-2",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (1.21e-10, 'cm^3/(molecule*s)'),
        n = 0,
        Ea = (-457.296, 'J/mol'),
        T0 = (1, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Cl + nC4H10 <=> HCl + C4H9-2""",
    longDesc = 
u"""
IUPAC recommendation: http://iupac.pole-ether.fr 
from 290-600 K
""",
)

entry(
    index = 137,
    label = "Cl + CH2O <=> HCl + HCO_r3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (8.1e-11, 'cm^3/(molecule*s)'),
        n = 0,
        Ea = (282.692, 'J/mol'),
        T0 = (1, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Cl + HCHO <=> HCl + HCO""",
    longDesc = 
u"""
IUPAC recommendation: http://iupac.pole-ether.fr 
from 200-500 K
""",
)

entry(
    index = 138,
    label = "Cl + C2H4O <=> HCl + C2H3O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8e-11, 'cm^3/(molecule*s)'), n=0, Ea=(0, 'J/mol'), T0=(1, 'K')),
    rank = 1,
    shortDesc = u"""Cl + CH3CHO <=> HCl + CH3CO""",
    longDesc = 
u"""
IUPAC recommendation: http://iupac.pole-ether.fr 
from 210-340 K
""",
)

entry(
    index = 139,
    label = "Cl + C3H6O-3 <=> HCl + C3H5O-3",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (1.5e-11, 'cm^3/(molecule*s)'),
        n = 0,
        Ea = (4905.54, 'J/mol'),
        T0 = (1, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Cl + CH3COCH3 <=> HCl + CH3COCH2""",
    longDesc = 
u"""
IUPAC recommendation: http://iupac.pole-ether.fr 
from 215-440 K
""",
)

entry(
    index = 140,
    label = "Cl + CH4O <=> HCl + CH3O",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (7.1e-11, 'cm^3/(molecule*s)'),
        n = 0,
        Ea = (623.585, 'J/mol'),
        T0 = (1, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Cl + CH3OH <=> HCl + CH2OH""",
    longDesc = 
u"""
IUPAC recommendation: http://iupac.pole-ether.fr 
from 200-500 K
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
    index = 142,
    label = "Cl + C2H6O <=> HCl + C2H5O",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.44e-10, 'cm^3/(molecule*s)'),
        n = -0.089,
        Ea = (-374.151, 'J/mol'),
        T0 = (1, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Cl + C2H5OH <=> HCl + CH3CHOH""",
    longDesc = 
u"""
Absolute and Site-Specific Abstraction Rate Coefficients for Reactions of Cl with CH3CH2 OH, CH3CD2OH, and CD3CH2OH Between 295 and 600 K
Taatjes, C. A., Christensen, L. K., Hurley M. D. and Wallington, T. J.: J. Phys. Chem. A, 103, 9805, 1999.
LP-IR experiments from 295-600 K
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
    label = "Cl + H2O <=> HCl + OH",
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
        A = (3.32e-10, 'cm^3/(molecule*s)'),
        n = 0,
        Ea = (1249.67, 'J/mol'),
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
    index = 150,
    label = "Cl + C5H12-2 <=> HCl + C5H11",
    degeneracy = 12.0,
    kinetics = Arrhenius(
        A = (2.79e-10, 'cm^3/(molecule*s)'),
        n = 0,
        Ea = (3849.6, 'J/mol'),
        T0 = (1, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Cl + neoC5H12 <=> HCl + neoC5H11""",
    longDesc = 
u"""
Competitive chlorination reactions in the gas phase: hydrogen and C1-C5 saturated hydrocarbons
Knox, J.H.; Nelson, R.L., Trans. Faraday Soc., 55, 1959
193-593 K, experimental measurement
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
    index = 152,
    label = "Cl + C5H10 <=> HCl + C5H9",
    degeneracy = 10.0,
    kinetics = Arrhenius(
        A = (4.87e-10, 'cm^3/(molecule*s)'),
        n = 0,
        Ea = (2419.51, 'J/mol'),
        T0 = (1, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Cl + cC5H10 <=> HCl + cC5H9""",
    longDesc = 
u"""
The study of chlorine atom reactions in the gas phase
Pritchard, H.O.; Pyke, J.B.; Trotman-Dickenson, A.F., JACS, 77, 1955
298-484 K, experimental measurement
""",
)

entry(
    index = 153,
    label = "Cl + C4H8-8 <=> HCl + C4H7-6",
    degeneracy = 8.0,
    kinetics = Arrhenius(
        A = (4.25e-10, 'cm^3/(molecule*s)'),
        n = 0,
        Ea = (3449.67, 'J/mol'),
        T0 = (1, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Cl + cC4H8 <=> HCl + cC4H7""",
    longDesc = 
u"""
Competitive chlorination reactions in the gas phase: hydrogen and C1-C5 saturated hydrocarbons
Knox, J.H.; Nelson, R.L., Trans. Faraday Soc., 55, 1959
193-593 K, experimental measurement
""",
)

entry(
    index = 154,
    label = "Cl + C4H8O2 <=> HCl + C4H7O2",
    degeneracy = 8.0,
    kinetics = Arrhenius(
        A = (2.27e-10, 'cm^3/(molecule*s)'),
        n = 0,
        Ea = (300.152, 'J/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Cl + Dioxane14 <=> HCl + Dioxanyl14""",
    longDesc = 
u"""
Experimental and Theoretical Investigation of the Kinetics of the Reaction of Atomic Chlorine with 1,4-Dioxane
Giri, B.R.; Roscoe, J.M.; Gonzalez-Garcia, N.; Olzmann, M.; Lo, J.MH.; Marriott, R.A., JPCA, 115, 2011, 5105-5111
292-360 K, theoretical prediction matched to experiment
""",
)

entry(
    index = 155,
    label = "Cl + C6H12O2 <=> HCl + C6H11O2",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.32e-11, 'cm^3/(molecule*s)'),
        n = 0,
        Ea = (2930.02, 'J/mol'),
        T0 = (1, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Cl + C4H9OC(CH3)O <=> HCl + C4H8OC(CH3)O-1""",
    longDesc = 
u"""
Free-radical substitution in aliphatic compounds. Part XIV. The halogenation of esters of butan-1-ol 
Singh, H.; Tedder, J.M., J. Chem. Soc. B, 1966 
313-433 K, experimental measurement
""",
)

entry(
    index = 156,
    label = "Cl + C6H12O2-2 <=> HCl + C6H11O2-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.32e-11, 'cm^3/(molecule*s)'),
        n = 0,
        Ea = (1249.67, 'J/mol'),
        T0 = (1, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Cl + C4H9OC(CH3)O <=> HCl + C4H8OC(CH3)O-2""",
    longDesc = 
u"""
Free-radical substitution in aliphatic compounds. Part XIV. The halogenation of esters of butan-1-ol 
Singh, H.; Tedder, J.M., J. Chem. Soc. B, 1966 
313-433 K, experimental measurement
""",
)

entry(
    index = 157,
    label = "Cl + C6H12O2-3 <=> HCl + C6H11O2-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.62e-11, 'cm^3/(molecule*s)'),
        n = 0,
        Ea = (2089.43, 'J/mol'),
        T0 = (1, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Cl + C4H9OC(CH3)O <=> HCl + C4H8OC(CH3)O-3""",
    longDesc = 
u"""
Free-radical substitution in aliphatic compounds. Part XIV. The halogenation of esters of butan-1-ol 
Singh, H.; Tedder, J.M., J. Chem. Soc. B, 1966 
313-433 K, experimental measurement
""",
)

entry(
    index = 158,
    label = "Cl + C6H12O2-4 <=> HCl + C6H11O2-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.66e-12, 'cm^3/(molecule*s)'),
        n = 0,
        Ea = (3759.8, 'J/mol'),
        T0 = (1, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Cl + C4H9OC(CH3)O <=> HCl + C4H8OC(CH3)O-4""",
    longDesc = 
u"""
Free-radical substitution in aliphatic compounds. Part XIV. The halogenation of esters of butan-1-ol 
Singh, H.; Tedder, J.M., J. Chem. Soc. B, 1966 
313-433 K, experimental measurement
""",
)

entry(
    index = 159,
    label = "Cl + C2H6O-3 <=> HCl + C2H5O-3",
    degeneracy = 6.0,
    kinetics = Arrhenius(A=(1.76e-10, 'cm^3/(molecule*s)'), n=0, Ea=(0, 'J/mol'), T0=(1, 'K')),
    rank = 1,
    shortDesc = u"""Cl + CH3OCH3 <=> HCl + CH3OCH2""",
    longDesc = 
u"""
Rate constants for the reaction of atomic chlorine with methanol and dimethyl ether from 200 to 500 K
Michael, J.V.; Nava, D.F.; Payne, W.A.; Stief, L.J., J. Chem. Phys., 70, 1979
200-500 K, experimental measurement
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
    index = 161,
    label = "Cl + C6H12 <=> HCl + C6H11",
    degeneracy = 12.0,
    kinetics = Arrhenius(A=(2.41e-10, 'cm^3/(molecule*s)'), n=0, Ea=(0, 'J/mol'), T0=(1, 'K')),
    rank = 1,
    shortDesc = u"""Cl + cC6H12 <=> HCl + cC6H11""",
    longDesc = 
u"""
Kinetic and mechanistic studies of the reactions of cyclopentylperoxy and cyclohexylperoxy radicals with HO2
Rowley, D.M.; Lesclaux, R.; Lightfoot, P.D.; Noziere, B.; Wallingotn, T.J.; Hurley, M.D., JPC, 96, 1992, 4889-4894
248-364 K, experimental measurement
""",
)

entry(
    index = 162,
    label = "Cl + C7H8 <=> HCl + C7H7",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.59e-12, 'cm^3/(molecule*s)'),
        n = 1.073,
        Ea = (6406.3, 'J/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Cl + C6H5CH3 <=> HCl + C6H5CH2""",
    longDesc = 
u"""
DFT study on the abstraction and addition of Cl atom with toluene
Huang, M.Q.; Wang, Z.Y.; Hao, L.Q.; Zhang, W.J., Comput. Theor. Chem., 996, 44-50, 2012
Theoretical predictions from 298-1000 K, agrees well with 298 K experiments
""",
)

entry(
    index = 163,
    label = "Cl + C7H8-2 <=> HCl + C7H7-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (6.88e-45, 'cm^3/(molecule*s)'),
        n = 10.876,
        Ea = (-22746.7, 'J/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Cl + C6H5CH3 <=> HCl + o-C6H4CH3""",
    longDesc = 
u"""
DFT study on the abstraction and addition of Cl atom with toluene
Huang, M.Q.; Wang, Z.Y.; Hao, L.Q.; Zhang, W.J., Comput. Theor. Chem., 996, 44-50, 2012
Theoretical predictions from 298-1000 K
""",
)

entry(
    index = 164,
    label = "Cl + C7H8-3 <=> HCl + C7H7-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (4.98e-43, 'cm^3/(molecule*s)'),
        n = 10.407,
        Ea = (-20733.8, 'J/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Cl + C6H5CH3 <=> HCl + m-C6H4CH3""",
    longDesc = 
u"""
DFT study on the abstraction and addition of Cl atom with toluene
Huang, M.Q.; Wang, Z.Y.; Hao, L.Q.; Zhang, W.J., Comput. Theor. Chem., 996, 44-50, 2012
Theoretical predictions from 298-1000 K
""",
)

entry(
    index = 165,
    label = "Cl + C7H8-4 <=> HCl + C7H7-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.75e-27, 'cm^3/(molecule*s)'),
        n = 5.626,
        Ea = (-1163.19, 'J/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Cl + C6H5CH3 <=> HCl + p-C6H4CH3""",
    longDesc = 
u"""
DFT study on the abstraction and addition of Cl atom with toluene 
Huang, M.Q.; Wang, Z.Y.; Hao, L.Q.; Zhang, W.J., Comput. Theor. Chem., 996, 44-50, 2012 
Theoretical predictions from 298-1000 K
""",
)

entry(
    index = 166,
    label = "Cl + iC4H10 <=> HCl + C4H9-3",
    degeneracy = 9.0,
    kinetics = Arrhenius(
        A = (1.94e-10, 'cm^3/(molecule*s)'),
        n = 0,
        Ea = (3429.72, 'J/mol'),
        T0 = (1, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Cl + iC4H10 <=> HCl + iC4H9""",
    longDesc = 
u"""
Competitive chlorination reactions in the gas phase: hydrogen and C1-C5 saturated hydrocarbons
Knox, J.H.; Nelson, R.L., Trans. Faraday Soc., 55, 1959
193-593 K, experimental measurement
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
    index = 172,
    label = "Cl + C8H10 <=> HCl + C8H9",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.06e-12, 'cm^3/(molecule*s)'),
        n = 1.073,
        Ea = (6406.3, 'J/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Cl + C6H5CH2CH3 <=> HCl + C6H5CHCH3""",
    longDesc = 
u"""
DFT study on the abstraction and addition of Cl atom with toluene 
Huang, M.Q.; Wang, Z.Y.; Hao, L.Q.; Zhang, W.J., Comput. Theor. Chem., 996, 44-50, 2012 
Theoretical predictions from 298-1000 K, agrees well with 298 K experiments
A-factor multiplied by 2/3 to account for different degeneracy of ethylbenzene vs. toluene
""",
)

entry(
    index = 173,
    label = "Cl + C9H12 <=> HCl + C9H11",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.3e-13, 'cm^3/(molecule*s)'),
        n = 1.073,
        Ea = (6406.3, 'J/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Cl + C6H5CH(CH3)CH3 <=> HCl + C6H5C(CH3)CH3""",
    longDesc = 
u"""
DFT study on the abstraction and addition of Cl atom with toluene 
Huang, M.Q.; Wang, Z.Y.; Hao, L.Q.; Zhang, W.J., Comput. Theor. Chem., 996, 44-50, 2012 
Theoretical predictions from 298-1000 K, agrees well with 298 K experiments
A-factor multiplied by 1/3 to account for different degeneracy of isopropylbenzene vs. toluene
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
    index = 180,
    label = "C4H6-3 + C6H5 <=> C6H6 + C4H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(31600, 'cm^3/(mol*s)'), n=3.11, Ea=(16.7, 'kJ/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2005_Ismail_C6H5_C4H6_highP""",
    longDesc = 
u"""
Taken from entry: phenyl + 1_3_butadiene <=> benzene + 1_3_butadien_1_yl
""",
)

entry(
    index = 181,
    label = "C6H6 + CH3_p23 <=> CH4b + C6H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5151, 'cm^3/(mol*s)'),
        n = 2.896,
        Ea = (15.308, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: kislovB""",
    longDesc = 
u"""
Taken from entry: benzene_1 + methyl_7 <=> phenyl_16 + CH4_26
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
        authors = ["'Li, S.-H.'", "'Guo, J.-J.'", "'Li, R.'", "'Wang, F.'", "'Li, X.-Y.'"],
        title = 'Theoretical Prediction of Rate Constants for Hydrogen Abstraction by OH, H, O, CH3, and HO2 Radicals from Toluene',
        journal = "'The Journal of Physical Chemistry A'",
        volume = "'120 (20)'",
        pages = """'3424-3432'""",
        year = "'2016'",
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
        authors = ["'Li, S.-H.'", "'Guo, J.-J.'", "'Li, R.'", "'Wang, F.'", "'Li, X.-Y.'"],
        title = 'Theoretical Prediction of Rate Constants for Hydrogen Abstraction by OH, H, O, CH3, and HO2 Radicals from Toluene',
        journal = "'The Journal of Physical Chemistry A'",
        volume = "'120 (20)'",
        pages = """'3424-3432'""",
        year = "'2016'",
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
    label = "CH4b + H <=> CH3_p1 + H2_p",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(4100, 'cm^3/(mol*s)'), n=3.156, Ea=(8755, 'cal/mol'), T0=(1, 'K')),
    rank = 1,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, Experimental, original source: doi 10.1002/kin.1064""",
)

entry(
    index = 187,
    label = "CH4b + O_rad <=> CH3_p1 + OH_p23",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(440000, 'cm^3/(mol*s)'), n=2.5, Ea=(6577, 'cal/mol'), T0=(1, 'K')),
    rank = 1,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, Experimental, original source: doi 10.1063/1.1748524""",
)

entry(
    index = 188,
    label = "CH4b + OH <=> CH3_p1 + H2O_p",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(1e+06, 'cm^3/(mol*s)'), n=2.182, Ea=(2506, 'cal/mol'), T0=(1, 'K')),
    rank = 1,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, Experimental, original source: doi 10.1021/jp040679j""",
)

entry(
    index = 189,
    label = "CH4b + HO2_r3 <=> CH3_p1 + H2O2_p13",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(47000, 'cm^3/(mol*s)'), n=2.5, Ea=(21000, 'cal/mol'), T0=(1, 'K')),
    rank = 1,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, Experimental, original source: doi 10.1063/1.1748524""",
)

entry(
    index = 190,
    label = "CH4b + O2 <=> CH3_p1 + HO2",
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
    label = "CH4O + OH <=> CH2OH_p + H2O_p",
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
    label = "CH4O-2 + OH <=> CH3O_p + H2O_p",
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
    label = "CH4O + CH3_r3 <=> CH2OH_p + CH4",
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
    label = "CH4O2 + OH <=> CH3OO_p + H2O_p",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.1e+12, 'cm^3/(mol*s)'), n=0, Ea=(-437, 'cal/mol'), T0=(1, 'K')),
    rank = 1,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, Experimental, original source: doi 10.1063/1.1748524""",
)

entry(
    index = 207,
    label = "CH3OOH_rC + OH <=> CH2OOH_p + H2O_p",
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
    label = "CH3O2 + CH4b <=> CH3OOH_p + CH3_p1",
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
    label = "C2H6 + OH <=> C2H5b + H2O_p",
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
    label = "C2H6 + CH3_r3 <=> C2H5b + CH4",
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
    label = "C2H4 + OH <=> C2H3_p + H2O_p",
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
    label = "C2H6O + OH <=> CH3CHOH_p + H2O_p",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(450, 'cm^3/(mol*s)'), n=3.11, Ea=(-2666, 'cal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, MP-VTST, original source: doi 10.1039/C2FD20012K""",
)

entry(
    index = 227,
    label = "C2H6O-2 + OH <=> CH2CH2OH_p + H2O_p",
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
    label = "C2H6O + CH3_r3 <=> CH3CHOH_p + CH4",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(20, 'cm^3/(mol*s)'), n=3.37, Ea=(7630, 'cal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016""",
)

entry(
    index = 232,
    label = "C2H6O-2 + CH3_r3 <=> CH2CH2OH_p + CH4",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(2, 'cm^3/(mol*s)'), n=3.57, Ea=(7717, 'cal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016""",
)

entry(
    index = 233,
    label = "CH3CH2OH_rO + CH3_r3 <=> CH3CH2O_p + CH4",
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
    label = "C2H4O + OH <=> CH3CO_p + H2O_p",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(-709, 'cal/mol'), T0=(1, 'K')),
    rank = 1,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, Experimental, original source: doi 10.1016/j.proci.2014.06.112""",
)

entry(
    index = 238,
    label = "CH3CHO_r1 + OH <=> CH2CHO_p + H2O_p",
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
    label = "C2H4O + CH3_r3 <=> CH3CO_p + CH4",
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
        authors = ["'Narendrapurapu, B. S.'", "'Simmonett, A. C.'", "'Schaefer, H. F.'", "'Miller, J. A.'", "'Klippenstein, S. J.'"],
        title = 'Combustion Chemistry: Important Features of the C3H5 Potential Energy Surface, Including Allyl Radical, Propargyl + H2, Allene + H, and Eight Transition States',
        journal = "'The Journal of Physical Chemistry A'",
        volume = "'115 (49)'",
        pages = """'14209-14214'""",
        year = "'2011'",
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
        authors = ["'Narendrapurapu, B. S.'", "'Simmonett, A. C.'", "'Schaefer, H. F.'", "'Miller, J. A.'", "'Klippenstein, S. J.'"],
        title = 'Combustion Chemistry: Important Features of the C3H5 Potential Energy Surface, Including Allyl Radical, Propargyl + H2, Allene + H, and Eight Transition States',
        journal = "'The Journal of Physical Chemistry A'",
        volume = "'115 (49)'",
        pages = """'14209-14214'""",
        year = "'2011'",
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
        authors = ["'Narendrapurapu, B. S.'", "'Simmonett, A. C.'", "'Schaefer, H. F.'", "'Miller, J. A.'", "'Klippenstein, S. J.'"],
        title = 'Combustion Chemistry: Important Features of the C3H5 Potential Energy Surface, Including Allyl Radical, Propargyl + H2, Allene + H, and Eight Transition States',
        journal = "'The Journal of Physical Chemistry A'",
        volume = "'115 (49)'",
        pages = """'14209-14214'""",
        year = "'2011'",
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
        authors = ["'Narendrapurapu, B. S.'", "'Simmonett, A. C.'", "'Schaefer, H. F.'", "'Miller, J. A.'", "'Klippenstein, S. J.'"],
        title = 'Combustion Chemistry: Important Features of the C3H5 Potential Energy Surface, Including Allyl Radical, Propargyl + H2, Allene + H, and Eight Transition States',
        journal = "'The Journal of Physical Chemistry A'",
        volume = "'115 (49)'",
        pages = """'14209-14214'""",
        year = "'2011'",
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
    label = "C4H4 + CH3_p23 <=> CH4b + C4H3",
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
    label = "C4H6-5 + CH3_p23 <=> CH4b + C4H5-4",
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
    label = "C4H6 + CH3_p23 <=> CH4b + C4H5-5",
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
    label = "C3H4 + OH <=> H2O + C3H3-2",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (12560, 'cm^3/(mol*s)'),
        n = 2.794,
        Ea = (0.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["'Zador, J.'", "'Miller, J. A.'"],
        title = 'Adventures on the C3H5O potential energy surface: OH + propyne, OH + allene and related reactions',
        journal = "'Proceedings of the Combustion Institute'",
        volume = "'35 (1)'",
        pages = """'181-188'""",
        year = "'2015'",
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
    label = "C3H4-1 + OH <=> H2O + C3H3",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (33830, 'cm^3/(mol*s)'),
        n = 2.802,
        Ea = (0.933, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["'Zador, J.'", "'Miller, J. A.'"],
        title = 'Adventures on the C3H5O potential energy surface: OH + propyne, OH + allene and related reactions',
        journal = "'Proceedings of the Combustion Institute'",
        volume = "'35 (1)'",
        pages = """'181-188'""",
        year = "'2015'",
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
    label = "C7H8 + OH <=> H2O + C7H7",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (130169, 'cm^3/(mol*s)'),
        n = 2.28048,
        Ea = (-572.972, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["'Li, S.-H.'", "'Guo, J.-J.'", "'Li, R.'", "'Wang, F.'", "'Li, X.-Y.'"],
        title = 'Theoretical Prediction of Rate Constants for Hydrogen Abstraction by OH, H, O, CH3, and HO2 Radicals from Toluene',
        journal = "'The Journal of Physical Chemistry A'",
        volume = "'120 (20)'",
        pages = """'3424-3432'""",
        year = "'2016'",
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
    label = "C7H8-2 + OH <=> H2O + C7H7-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (277.731, 'cm^3/(mol*s)'),
        n = 2.99789,
        Ea = (1245.72, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["'Li, S.-H.'", "'Guo, J.-J.'", "'Li, R.'", "'Wang, F.'", "'Li, X.-Y.'"],
        title = 'Theoretical Prediction of Rate Constants for Hydrogen Abstraction by OH, H, O, CH3, and HO2 Radicals from Toluene',
        journal = "'The Journal of Physical Chemistry A'",
        volume = "'120 (20)'",
        pages = """'3424-3432'""",
        year = "'2016'",
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
    label = "C7H8-3 + OH <=> H2O + C7H7-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (819.665, 'cm^3/(mol*s)'),
        n = 3.09594,
        Ea = (1507.71, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["'Li, S.-H.'", "'Guo, J.-J.'", "'Li, R.'", "'Wang, F.'", "'Li, X.-Y.'"],
        title = 'Theoretical Prediction of Rate Constants for Hydrogen Abstraction by OH, H, O, CH3, and HO2 Radicals from Toluene',
        journal = "'The Journal of Physical Chemistry A'",
        volume = "'120 (20)'",
        pages = """'3424-3432'""",
        year = "'2016'",
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
    label = "C7H8-4 + OH <=> H2O + C7H7-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (763.895, 'cm^3/(mol*s)'),
        n = 3.10443,
        Ea = (1688.65, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["'Li, S.-H.'", "'Guo, J.-J.'", "'Li, R.'", "'Wang, F.'", "'Li, X.-Y.'"],
        title = 'Theoretical Prediction of Rate Constants for Hydrogen Abstraction by OH, H, O, CH3, and HO2 Radicals from Toluene',
        journal = "'The Journal of Physical Chemistry A'",
        volume = "'120 (20)'",
        pages = """'3424-3432'""",
        year = "'2016'",
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
        authors = ["'Li, S.-H.'", "'Guo, J.-J.'", "'Li, R.'", "'Wang, F.'", "'Li, X.-Y.'"],
        title = 'Theoretical Prediction of Rate Constants for Hydrogen Abstraction by OH, H, O, CH3, and HO2 Radicals from Toluene',
        journal = "'The Journal of Physical Chemistry A'",
        volume = "'120 (20)'",
        pages = """'3424-3432'""",
        year = "'2016'",
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
        authors = ["'Li, S.-H.'", "'Guo, J.-J.'", "'Li, R.'", "'Wang, F.'", "'Li, X.-Y.'"],
        title = 'Theoretical Prediction of Rate Constants for Hydrogen Abstraction by OH, H, O, CH3, and HO2 Radicals from Toluene',
        journal = "'The Journal of Physical Chemistry A'",
        volume = "'120 (20)'",
        pages = """'3424-3432'""",
        year = "'2016'",
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
        authors = ["'Li, S.-H.'", "'Guo, J.-J.'", "'Li, R.'", "'Wang, F.'", "'Li, X.-Y.'"],
        title = 'Theoretical Prediction of Rate Constants for Hydrogen Abstraction by OH, H, O, CH3, and HO2 Radicals from Toluene',
        journal = "'The Journal of Physical Chemistry A'",
        volume = "'120 (20)'",
        pages = """'3424-3432'""",
        year = "'2016'",
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
        authors = ["'Li, S.-H.'", "'Guo, J.-J.'", "'Li, R.'", "'Wang, F.'", "'Li, X.-Y.'"],
        title = 'Theoretical Prediction of Rate Constants for Hydrogen Abstraction by OH, H, O, CH3, and HO2 Radicals from Toluene',
        journal = "'The Journal of Physical Chemistry A'",
        volume = "'120 (20)'",
        pages = """'3424-3432'""",
        year = "'2016'",
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
        authors = ["'Li, S.-H.'", "'Guo, J.-J.'", "'Li, R.'", "'Wang, F.'", "'Li, X.-Y.'"],
        title = 'Theoretical Prediction of Rate Constants for Hydrogen Abstraction by OH, H, O, CH3, and HO2 Radicals from Toluene',
        journal = "'The Journal of Physical Chemistry A'",
        volume = "'120 (20)'",
        pages = """'3424-3432'""",
        year = "'2016'",
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
        authors = ["'Li, S.-H.'", "'Guo, J.-J.'", "'Li, R.'", "'Wang, F.'", "'Li, X.-Y.'"],
        title = 'Theoretical Prediction of Rate Constants for Hydrogen Abstraction by OH, H, O, CH3, and HO2 Radicals from Toluene',
        journal = "'The Journal of Physical Chemistry A'",
        volume = "'120 (20)'",
        pages = """'3424-3432'""",
        year = "'2016'",
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
    label = "C7H8 + CH3_p23 <=> CH4b + C7H7",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.07e+06, 'cm^3/(mol*s)'),
        n = 2.26764,
        Ea = (4392.37, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["'Li, S.-H.'", "'Guo, J.-J.'", "'Li, R.'", "'Wang, F.'", "'Li, X.-Y.'"],
        title = 'Theoretical Prediction of Rate Constants for Hydrogen Abstraction by OH, H, O, CH3, and HO2 Radicals from Toluene',
        journal = "'The Journal of Physical Chemistry A'",
        volume = "'120 (20)'",
        pages = """'3424-3432'""",
        year = "'2016'",
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
    label = "C7H8-2 + CH3_p23 <=> CH4b + C7H7-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.21e+07, 'cm^3/(mol*s)'),
        n = 1.81483,
        Ea = (14155.6, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["'Li, S.-H.'", "'Guo, J.-J.'", "'Li, R.'", "'Wang, F.'", "'Li, X.-Y.'"],
        title = 'Theoretical Prediction of Rate Constants for Hydrogen Abstraction by OH, H, O, CH3, and HO2 Radicals from Toluene',
        journal = "'The Journal of Physical Chemistry A'",
        volume = "'120 (20)'",
        pages = """'3424-3432'""",
        year = "'2016'",
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
    label = "C7H8-3 + CH3_p23 <=> CH4b + C7H7-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.11e+08, 'cm^3/(mol*s)'),
        n = 1.80464,
        Ea = (14389, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["'Li, S.-H.'", "'Guo, J.-J.'", "'Li, R.'", "'Wang, F.'", "'Li, X.-Y.'"],
        title = 'Theoretical Prediction of Rate Constants for Hydrogen Abstraction by OH, H, O, CH3, and HO2 Radicals from Toluene',
        journal = "'The Journal of Physical Chemistry A'",
        volume = "'120 (20)'",
        pages = """'3424-3432'""",
        year = "'2016'",
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
    label = "C7H8-4 + CH3_p23 <=> CH4b + C7H7-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.05e+08, 'cm^3/(mol*s)'),
        n = 1.81188,
        Ea = (14672.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["'Li, S.-H.'", "'Guo, J.-J.'", "'Li, R.'", "'Wang, F.'", "'Li, X.-Y.'"],
        title = 'Theoretical Prediction of Rate Constants for Hydrogen Abstraction by OH, H, O, CH3, and HO2 Radicals from Toluene',
        journal = "'The Journal of Physical Chemistry A'",
        volume = "'120 (20)'",
        pages = """'3424-3432'""",
        year = "'2016'",
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
        authors = ["'Li, S.-H.'", "'Guo, J.-J.'", "'Li, R.'", "'Wang, F.'", "'Li, X.-Y.'"],
        title = 'Theoretical Prediction of Rate Constants for Hydrogen Abstraction by OH, H, O, CH3, and HO2 Radicals from Toluene',
        journal = "'The Journal of Physical Chemistry A'",
        volume = "'120 (20)'",
        pages = """'3424-3432'""",
        year = "'2016'",
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
        A = (91.4407, 'cm^3/(mol*s)'),
        n = 3.28308,
        Ea = (14233.3, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["'Li, S.-H.'", "'Guo, J.-J.'", "'Li, R.'", "'Wang, F.'", "'Li, X.-Y.'"],
        title = 'Theoretical Prediction of Rate Constants for Hydrogen Abstraction by OH, H, O, CH3, and HO2 Radicals from Toluene',
        journal = "'The Journal of Physical Chemistry A'",
        volume = "'120 (20)'",
        pages = """'3424-3432'""",
        year = "'2016'",
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
        A = (197.267, 'cm^3/(mol*s)'),
        n = 3.28482,
        Ea = (14542.4, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["'Li, S.-H.'", "'Guo, J.-J.'", "'Li, R.'", "'Wang, F.'", "'Li, X.-Y.'"],
        title = 'Theoretical Prediction of Rate Constants for Hydrogen Abstraction by OH, H, O, CH3, and HO2 Radicals from Toluene',
        journal = "'The Journal of Physical Chemistry A'",
        volume = "'120 (20)'",
        pages = """'3424-3432'""",
        year = "'2016'",
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
    label = "C7H8-4 + HO2_r3 <=> H2O2 + C7H7-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (204.902, 'cm^3/(mol*s)'),
        n = 3.30806,
        Ea = (14723.9, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["'Li, S.-H.'", "'Guo, J.-J.'", "'Li, R.'", "'Wang, F.'", "'Li, X.-Y.'"],
        title = 'Theoretical Prediction of Rate Constants for Hydrogen Abstraction by OH, H, O, CH3, and HO2 Radicals from Toluene',
        journal = "'The Journal of Physical Chemistry A'",
        volume = "'120 (20)'",
        pages = """'3424-3432'""",
        year = "'2016'",
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
        authors = ["'Semenikhin, A. S.'", "'Savchenkova, A. S.'", "'Chechet, I. V.'", "'Matveev, S. G.'", "'Liu, Z.'", "'Frenklach, M.'", "'Mebel, A. M.'"],
        title = 'Rate constants for H abstraction from benzo(a)pyrene and chrysene: a theoretical study',
        journal = "'Physical Chemistry Chemical Physics'",
        volume = "'19 (37)'",
        pages = """'25401-25413'""",
        year = "'2017'",
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
        authors = ["'Violi, A.'", "'Truong, T. N.'", "'Sarofim, A. F.'"],
        title = 'Kinetics of Hydrogen Abstraction Reactions from Polycyclic Aromatic Hydrocarbons by H Atoms',
        journal = "'The Journal of Physical Chemistry A'",
        volume = "'108 (22)'",
        pages = """'4846-4852'""",
        year = "'2004'",
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
    label = "C6H6 + OH <=> H2O + C6H5",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (3.88e-20, 'cm^3/(molecule*s)'),
        n = 2.683,
        Ea = (0.7333, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["'Seta, T.'", "'Nakajima, M.'", "'Miyoshi, A.'"],
        title = 'High-Temperature Reactions of OH Radicals with Benzene and Toluene',
        journal = "'The Journal of Physical Chemistry A'",
        volume = "'110 (15)'",
        pages = """'5081-5090'""",
        year = "'2006'",
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
    label = "C6H6 + CH3_p23 <=> CH4b + C6H5",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (3.07e-21, 'cm^3/(molecule*s)'),
        n = 2.88,
        Ea = (13.332, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["'Mai, T. V. T.'", "'Ratkiewicz, A.'", "'Duong, M. v.'", "'Huynh, L. K.'"],
        title = 'Direct ab initio study of the C6H6+CH3/C2H5=C6H5+CH4/C2H6 reactions',
        journal = "'Chemical Physics Letters'",
        volume = "'646'",
        pages = """'102-109'""",
        year = "'2016'",
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
        authors = ["'Mai, T. V. T.'", "'Ratkiewicz, A.'", "'Duong, M. v.'", "'Huynh, L. K.'"],
        title = 'Direct ab initio study of the C6H6+CH3/C2H5=C6H5+CH4/C2H6 reactions',
        journal = "'Chemical Physics Letters'",
        volume = "'646'",
        pages = """'102-109'""",
        year = "'2016'",
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
        authors = ["'Semenikhin, A. S.'", "'Savchenkova, A. S.'", "'Chechet, I. V.'", "'Matveev, S. G.'", "'Liu, Z.'", "'Frenklach, M.'", "'Mebel, A. M.'"],
        title = 'Rate constants for H abstraction from benzo(a)pyrene and chrysene: a theoretical study',
        journal = "'Physical Chemistry Chemical Physics'",
        volume = "'19 (37)'",
        pages = """'25401-25413'""",
        year = "'2017'",
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
        authors = ["'Semenikhin, A. S.'", "'Savchenkova, A. S.'", "'Chechet, I. V.'", "'Matveev, S. G.'", "'Liu, Z.'", "'Frenklach, M.'", "'Mebel, A. M.'"],
        title = 'Rate constants for H abstraction from benzo(a)pyrene and chrysene: a theoretical study',
        journal = "'Physical Chemistry Chemical Physics'",
        volume = "'19 (37)'",
        pages = """'25401-25413'""",
        year = "'2017'",
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
        authors = ["'Semenikhin, A. S.'", "'Savchenkova, A. S.'", "'Chechet, I. V.'", "'Matveev, S. G.'", "'Liu, Z.'", "'Frenklach, M.'", "'Mebel, A. M.'"],
        title = 'Rate constants for H abstraction from benzo(a)pyrene and chrysene: a theoretical study',
        journal = "'Physical Chemistry Chemical Physics'",
        volume = "'19 (37)'",
        pages = """'25401-25413'""",
        year = "'2017'",
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
        authors = ["'Semenikhin, A. S.'", "'Savchenkova, A. S.'", "'Chechet, I. V.'", "'Matveev, S. G.'", "'Liu, Z.'", "'Frenklach, M.'", "'Mebel, A. M.'"],
        title = 'Rate constants for H abstraction from benzo(a)pyrene and chrysene: a theoretical study',
        journal = "'Physical Chemistry Chemical Physics'",
        volume = "'19 (37)'",
        pages = """'25401-25413'""",
        year = "'2017'",
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
        authors = ["'Semenikhin, A. S.'", "'Savchenkova, A. S.'", "'Chechet, I. V.'", "'Matveev, S. G.'", "'Liu, Z.'", "'Frenklach, M.'", "'Mebel, A. M.'"],
        title = 'Rate constants for H abstraction from benzo(a)pyrene and chrysene: a theoretical study',
        journal = "'Physical Chemistry Chemical Physics'",
        volume = "'19 (37)'",
        pages = """'25401-25413'""",
        year = "'2017'",
    ),
    referenceType = "theory",
    rank = 5,
    longDesc = 
u"""
G3(MP2,CC)//B3LYP
""",
)

