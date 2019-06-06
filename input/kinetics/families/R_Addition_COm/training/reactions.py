#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_COm/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "CH3 + CO <=> C2H3O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.634e+07, 'cm^3/(mol*s)'),
        n = 1.512,
        Ea = (6.013, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['Senosiain, J. P.', 'Klippenstein, S. J.', 'Miller, J. A.'],
        title = 'Pathways and Rate Coefficients for the Decomposition of Vinoxy and Acetyl Radicals',
        journal = 'The Journal of Physical Chemistry A',
        volume = '110 (17)',
        pages = '5772-5781',
        year = '2006',
    ),
    referenceType = "theory",
    rank = 5,
    longDesc = 
u"""
RQCISD(T)/cc-pVinfZ //UQCISD/UB3LYP
""",
)

entry(
    index = 1,
    label = "C2H3O <=> CO + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.07e+12, 's^-1'), n=0.63, Ea=(70698, 'J/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Senosiain, J. P.', 'Klippenstein, S. J.', 'Miller, J. A.'],
        title = 'Pathways and Rate Coefficients for the Decomposition of Vinoxy and Acetyl Radicals',
        journal = 'The Journal of Physical Chemistry A',
        volume = '110 (17)',
        pages = '5772-5781',
        year = '2006',
    ),
    referenceType = "theory",
    rank = 5,
    longDesc = 
u"""
RQCISD(T)/cc-pVinfZ //UQCISD/UB3LYP
""",
)

entry(
    index = 2,
    label = "C3H5O <=> CO + C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.417e+12, 's^-1'), n=0.428, Ea=(15.009, 'kcal/mol'), T0=(1, 'K')),
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
    index = 3,
    label = "H + CO <=> CHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (20.92, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    longDesc = 
u"""
Converted to training reaction from rate rule: COm;Y_rad
""",
)

entry(
    index = 4,
    label = "H + CO <=> CHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.18e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.3805, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (345, 'K'),
        Tmax = (449, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Arai et al [102].""",
    longDesc = 
u"""
[102] Arai, H.; Nagai, S.; Hatada, M.; Radiat. Phys. Chem. 1981, 17, 211.
CO + H --> HCO. Data estimated

pg.215, Table 2: Estimated values of k2 and the reference value of k3 used for the estimation of k2

Raw data is (Temperature [=] degC, k2 [=] cm3/molecule/s):

(72, 3.9x10^-15), (120, 5.6x10^-15), (176, 9.8x10^-15)
Plotting ln(k) vs. 1000/T[=K] and performing a "Linear" regression in Microsoft Excel results

in "y = -1.3657x - 29.258" with an R^2 value of 0.9762.  The A and Ea values calculated
by MRH are thus: A=1.18x10^11 cm3/mol/s, Ea=2.71 kcal/mol, in agreement w/database.
The authors performed an electron beam irradiation of a CH4 gas stream, containing small

amounts of CO, in a flow system at 1atm.  Authors observe a large decrease in H2 with 
the addition of small amounts of CO.  They assume that this observation must be due to 
H+CO-->HCO.  They propose the following mechanism:
(1) CH4 = H + CH3		k1
(2) H + CO = HCO		k2
(3) H + CH4 = H2 + CH3	k3
The rate of H2 formation:

d[H2]/dt = RM(H2) + k3[H][CH4]
where RM(H2) is the production of H2 through reactions NOT involving H atoms.

Using PSSA on [H]:

d[H]/dt = k1*I*[CH4] - k2[H][CO] - k3[H][CH4] = 0
where I is the dosage rate.

Solving for [H] and substituting into the rate of [H2] formation:

d[H2]/dt = RM(H2) + k1*k3*I*[CH4]^2 / (k2[CO] + k3[CH4])
Subtracting RM(H2) from both sides, taking the inverse of the expression, and rearrangement yields:

{d[H2]/dt - RM(H2)}^-1 = {1 + (k2/k3)*([CO]/[CH4])} / {k1*I*[CH4]}
The authors then introduce this "G-value" (proportional to how they detect H2 and CH4???):

{G(H2) - GM(H2)}^-1 = {1 + (k2/k3)*([CO]/[CH4])} / G(H)
The authors present a plot of {G(H2) - GM(H2)}^-1 vs. [CO]/[CH4] to show it is linear.

*** NOTE: The authors assume a value of GM(H2) of 4.63, according to Okazaki et al. ***

From the plot, they extract a (k2/k3) ratio for each temperature tested.  Using the k3 values

reported by Sepehrad et al., they estimate a value of k2.
*** NOTE: Value of k3 used: (72C, 1.52x10^-18 cm3/molecule/s), (120C, 1.51x10^-17 cm3/molecule/s),

(176C, 1.23x10^-16 cm3/molecule/s). ***
MRH 1-Sept-2009

Converted to training reaction from rate rule: COm;H_rad
""",
)

entry(
    index = 5,
    label = "CH3 + CO <=> C2H3O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.06e+11, 'cm^3/(mol*s)', '*|/', 3.16),
        n = 0,
        Ea = (28.7859, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Baulch et al. [94]""",
    longDesc = 
u"""
[94] Baulch, D.L.; Cobos, C.J.; Cox, R.A.; Frank, P.; Hayman, G,; Just, T.; Kerr, J.A.; Murrells, T.; Pilling, M.J.; 
Troe, J.; Walker, R.W.; Warnatz, J. J. Phys. Chem. Ref. Data 1994, 23, 847.

CO + CH3 --> CH3C0. Extensive literature review.

pg 871 Evaluated Kinetic Data for Combustion Modelling Supplement 1, Table 3. Combination reactions.

RMG data matches reference data for k(infinity).

Verified by Karma James

pg.973-974: Discussion on evaluated data

CH3+CO(+m) --> CH3CO(+m): RMG stores k_inf rate coefficient.  The recommended rate

coefficient comes from the preferred (from this reference) rxn rate and the equilibrium
constant (from Bencsura et al.)
MRH 31-Aug-2009

Converted to training reaction from rate rule: COm;C_methyl
""",
)

entry(
    index = 6,
    label = "C2H5 + CO <=> C3H5O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.51e+11, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (20.125, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang et al [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J.Phys. Chem. Ref. Data 1986, 15, 1087.
CO + C2H5 --> C2H5CO.

pg 1096, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 17,14.

Verified by Karma James

NOTE: Reported rate coefficients are for k_inf (MRH 11Aug2009)

pg. 1178-1179: Discussion on evaluated data

Recommended data (in the form of k_inf) comes from expression given by Watkins and Thompson

Fall-off corrections and collision efficiencies are also available
(although we do not store them in RMG_database)
MRH 28-Aug-2009

Converted to training reaction from rate rule: COm;C_rad/H2/Cs
""",
)

entry(
    index = 7,
    label = "C2H3 + CO <=> C3H3O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.51e+11, 'cm^3/(mol*s)', '*|/', 5),
        n = 0,
        Ea = (20.125, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Tsang et al [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J.Phys. Chem. Ref. Data 1986, 15, 1087.
CO + C2H3 --> CH2=CHCO.

pg 1099, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 19,14.

Verified by Karma James

NOTE: Reported rate coefficients are for k_inf (MRH 11Aug2009)

pg. 1198-1199: Discussion of evaluated data

Recommended data (in the form of k_inf) is assumed to be equal to the rate expression

for CO+C2H5-->H3C-CH2-C=O.  Authors note the rxn is in the fall-off region
under all conditions.
Fall-off corrections and collision efficiencies are also available
(although we do not store them in RMG_database).
MRH 28-Aug-2009

Converted to training reaction from rate rule: COm;Cd_pri_rad
""",
)

entry(
    index = 8,
    label = "C6H5 + CO <=> C7H5O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.48e+12, 'cm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (13.9327, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (295, 'K'),
        Tmax = (500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Nam et al [104].""",
    longDesc = 
u"""
[104] Nam, G.-J.; Xia, W.; Park, J.; Lin, M. Phys. Chem. A 2000, 104, 1233.	
Phenyl + CO --> Benzoyl. Original deltaA = 2.8E+11

Absolute value measrued directly. Rate constant is high pressure limit. 

Pressure 0.02-0.16 atm. Excitation: flash photolysis, analysis: Vis-UV absorption.

Authors use a Beer-Lambert law type expression:

1/tc = 1/tc_0 + (c*l*epsilon / n*L) * [A](t)
where tc and tc_0 are the decay times of the injected probing photons in the presence

and absence of absorbing species, c is the speed of light, l is the length of the
absorbing medium, epsilon is the extinction coefficient, n is the refractive index
of the medium, L is the length of the cavity, and [A](t) is the concentration of
the absorbing species at time t.
Assuming a simple association rxn, A decays exponentially: [A](t) = [A](0)*exp(-k'*t).

Combining this with the previous expression yields:
ln(1/tc - 1/tc_0) = B - k'*t		eq. (*)
However, the authors assume the reverse rxn will be significant (C6H5 + CO <--> C6H5CO).

Thus, they propose the following rate equation:
dx/dt = kf([A](0) - x)[CO] - kr*x
where x is defined as [A](0) - [A](t), [A](t) is the concentration of
the C6H5CO radical at time t, kf is the rate coefficient for C6H5+CO-->C6H5CO,
and kr is the rate coefficient for C6H5CO-->C6H5+CO.
Integrating the above differential equation, assuming constant [CO], yields:

x = (a/b) * (1-exp(-b*t))
where a = kf*[CO]*[A](0) and b = kf*[CO] + kr
Recalling that x = [A](0) - [A](t):

[A](t) = [A](0) - x = [A](0) * {kr + kf*[CO]*exp(-b*t)} / b
Substituting this into the Beer-Lambert law expression:

1/tc - 1/tc_0 = [A](0) * {kr + kf*[CO]*exp(-b*t)} / b		eq. (**)
C6H5 radical was generated from C6H5NO.  The rate coefficient for the C6H5+CO reaction

was measured in the temperature range 295-500K at 12-120 torr, with Ar as the
carrier gas.  The authors note that plots of ln(1/tc - 1/tc_0) vs. t exhibited
linear behavior (for a given Temperature and [CO] concentration).  The slope of
the plot, computed using a "standard weighted least-squares analysis", yielded k',
the pseudo first-order rate coefficient {eq. (*)}.  The authors also note that above 400K,
the plots became nonlinear with time, which the authors attribute to C6H5
re-generation from the reverse rxn C6H5CO --> C6H5 + CO.  This data was analyzed
using eq. (**), to yield b.  The pseudo first-order rate coefficients (either k' or b)
were plotted against [CO] to yield the second-order rate coefficient for C6H5+CO.
The authors note that the evaluated kf calculated above and below 400K differ greatly.
The authors performed a "weighted least-squares analysis" on all data to arrive at
the reported bimolecular rate coefficient:
k1 = 10^11.93+/-0.14 * exp[(-1507+/-109)/T] cm3/mole/s
valid from 295-500K at 40 torr Ar pressure.
The authors also investigated the pressure dependence of the rxn at 347K, from 12-120 torr.

At 347K, the authors do not observe any significant difference.  However, at higher
temperatures, pressure effects become significant.  The authors performed RRKM
calculations to account for falloff effects, and report the adjusted second-order
rate coefficient as:
k1_inf = 10^12.17+/-0.18 * exp[(-1676+/-149)/T] cm3/mole/s
*** NOTE: RMG database was storing reported k1 value.  MRH has changed this so that RMG

now stores the k1_inf value. ***
MRH 1-Sept-2009

Converted to training reaction from rate rule: COm;Cb_rad
""",
)

entry(
    index = 9,
    label = "CH3O + CO <=> C2H3O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.41e+07, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (12.552, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (250, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Wang et al. [105].""",
    longDesc = 
u"""
[105] Wang, B.; Hou, H.; Gu, Y. Phys. Chem. A 1999, 103, 8021.
RRK(M) extrapolation. CH3O + CO --> CH3OCO, 250K and 2500K

Data stored in RMG appears to be linear fit of the following data, presented on pg.8028

in the right-hand column under the section heading "3.Implications for Atmospheric
and Combustion Chemistry.": (250K, 5torr, 1.39x10^-19 cm3/molecule/s) and 
(2500K, 760torr, 3.10x10^-17 cm3/molecule/s).
Plotting ln(k) vs. 1000/T[=K] and performing a "Linear" regression in Microsoft Excel results

in "y = -1.502x - 37.412" with an R^2 value of 1.  The A and Ea values calculated
by MRH are thus: A=3.40x10^7 cm3/mol/s, Ea=2.98 kcal/mol, in agreement w/database.
MRH 1-Sept-2009

Converted to training reaction from rate rule: COm;O_rad/NonDe
""",
)

entry(
    index = 10,
    label = "C2H5 + CO <=> C3H5O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.7e+07, 'cm^3/(mol*s)', '*|/', 3),
        n = 1.37,
        Ea = (23.807, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""MRH CBS-QB3 calculations with 1dHR corrections""",
    longDesc = 
u"""
CH3CH2 + CO = CH3CH2CO
MRH CBS-QB3 calculations with 1D hindered rotor corrections [MRHCBSQB31DHR]_.

Ethyl (doublet): external symmetry number (EXTSYM) = 1, one hindered rotor (methyl group, symmetry = 6)
CO (singlet): EXTSYM = 1
TS (doublet): EXTSYM = 1, two hindered rotors (methyl group, symmetry = 3; ethyl group, symmetry = 1)
CH3CH2CO (doublet): EXTSYM = 1, two hindered rotors (methyl group, symmetry = 3; ethyl group, symmetry = 1)

Converted to training reaction from rate rule: COm;CH2CH3
""",
)

entry(
    index = 11,
    label = "C3H7 + CO <=> C4H7O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.51e+10, 'cm^3/(mol*s)', '*|/', 3),
        n = 0.45,
        Ea = (27.9491, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""MRH CBS-QB3 calculations with 1dHR corrections""",
    longDesc = 
u"""
CH3CH2CH2 + CO = CH3CH2CH2CO
MRH CBS-QB3 calculations with 1D hindered rotor corrections [MRHCBSQB31DHR]_.

n-Propyl (doublet): external symmetry number (EXTSYM) = 1, two hindered rotors (methyl group, symmetry = 3; ethyl group, symmetry = 4)
CO (singlet): EXTSYM = 1
TS (doublet): EXTSYM = 1, three hindered rotors (methyl group, symmetry = 3; ethyl group, symmetry = 2; propyl group, symmetry = 1)
CH3CH2CH2CO (doublet): EXTSYM = 1, three hindered rotors (methyl group, symmetry = 3; ethyl group, symmetry = 1; propyl group, symmetry = 1)

Converted to training reaction from rate rule: COm;CH2CH2CH3
""",
)

entry(
    index = 12,
    label = "C3H7-2 + CO <=> C4H7O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.61e+07, 'cm^3/(mol*s)', '*|/', 3),
        n = 1.36,
        Ea = (20.0832, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""MRH CBS-QB3 calculations with 1dHR corrections""",
    longDesc = 
u"""
CH3CHCH3 + CO = CH3CH(CO)CH3
MRH CBS-QB3 calculations with 1D hindered rotor corrections [MRHCBSQB31DHR]_.

iso-Propyl (doublet): external symmetry number (EXTSYM) = 1, two hindered rotors (methyl group, symmetry = 6; methyl group, symmetry = 6)
CO (singlet): EXTSYM = 1
TS (doublet): EXTSYM = 1, three hindered rotors (methyl group, symmetry = 3; methyl group, symmetry = 3; propyl group, symmetry = 1)
CH3CH(CO)CH3 (doublet): EXTSYM = 1, three hindered rotors (methyl group, symmetry = 3; methyl group, symmetry = 3; propyl group, symmetry = 1)

Converted to training reaction from rate rule: COm;CH(CH3)2
""",
)

entry(
    index = 13,
    label = "CH3S + CO <=> C2H3OS",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (78500, 'cm^3/(mol*s)'),
        n = 2.33,
        Ea = (9.33032, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""CAC CBS-QB3 calcs, HO""",
    longDesc = 
u"""
Converted to training reaction from rate rule: COm;S_rad/NonDe
""",
)

entry(
    index = 14,
    label = "C5H5O + CO <=> C6H5O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (14420, 'cm^3/(mol*s)'),
        n = 2.333,
        Ea = (18.929, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['I. V. Tokmakov', 'G. Kim', 'V. V. Kislov', 'A. M. Mebel', 'M. C. Lin'],
        title = 'The Reaction of Phenyl Radical with Molecular Oxygen: A G2M Study of the Potential Energy Surface',
        journal = 'J. Phys. Chem. A',
        volume = '109 (27)',
        pages = '6114-6127',
        year = '2005',
    ),
    referenceType = "theory",
    rank = 5,
    longDesc = 
u"""
Using CanTherm to calculate TST rates from the PES at the G2M(MP2)//B3LYP/6-311++G** level of theory
The rates have been validated by the rates reported in Proceedings of the Combustion Institute 35 (2015) 1861–1869,
where only 1500, 2000, 2500 K rates were reported.
""",
)

