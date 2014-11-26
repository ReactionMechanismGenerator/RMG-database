#!/usr/bin/env python
# encoding: utf-8

name = "Silylene_Insertion/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 1,
    label = "SiH2 + H2 <=> SiH4",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.05E6, 'cm^3/(mol*s)'),
        n = 1.97,
        Ea = (-1.9, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (400, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Walch, S.P.", "Dateo, C.E."],
        title = "Thermal decomposition pathways and rates for silane, chlorosilane, dichlorosilane, and trichlorosilane",
        journal = "J. Phys. Chem. A",
        pages = """2015-2022""",
        year = "2001",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2001WAL/DAT2015-2022:2",
    ),
    longDesc = 
u"""
Calculations using CASSCF/cc-pVDZ for geometries and vibrational frequencies. Energies of reactats, products and TS computed with CCSD(T)/aug-cc-pVTZ extrapolated to complete basis set using MP2/aug-cc-pVnZ(n=2,3,4). Rate founded with conventional TST. Error in barrier at most 2 kcal/mol, likely about 1 kcal/mol.
""",
)

#entry(
#    index = 2,
#    label = "SiH2 + SiH4 <=> Si2H6",
#    degeneracy = 2,
#    kinetics = Arrhenius(
#    ),
#    reference = Article(
#        authors = ["Matsumoto, K.", "Klippenstein, S.J.", "Tonokura, K.", "Koshi, T."],
#        title = "Channel specific rate constants relevant to the thermal decomposition of disilane",
#        journal = "J. Phys. Chem. A",
#        pages = """4911-4920""",
#        year = "2005",
#    ),
#    longDesc = 
#u"""
#Potential energy surface was calculated with G3/B3LYP//6-3111++G(d,p) basis set, VARIFLEX was used to compute rate expressions from TST.
#""",
#)

entry(
    index = 3,
    label = "SiH2 + Si2H6 <=> Si3H8",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.86E14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1.9, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (295, 'K'),
        Tmax = (595, 'K'),
	),
    reference = Article(
        authors = ["Becerra, R.", "Frey, H.M.", "Mason, B.P.", "Walsh, R."],
        title = "Time-resolved gas-phase kinetic studies of the reactions of silylene with disilane and trisilane",
        journal = "J. Organometal. Chem.",
        pages = """343-349""",
        year = "1996",
    ),
    longDesc = 
u"""
Laser flash photolysis was used to measure rates and fit to Arrhenius form. Error in logA +/- 0.04 and error in Ea +/- 0.3 kJ/mol. Authors note the Arrhenius plot is slightly curved.
""",
)

entry(
    index = 4,
    label = "SiH2 + Si3H8 <=> Si4H10",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.24E14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-2.0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (295, 'K'),
        Tmax = (595, 'K'),
	),
    reference = Article(
        authors = ["Becerra, R.", "Frey, H.M.", "Mason, B.P.", "Walsh, R."],
        title = "Time-resolved gas-phase kinetic studies of the reactions of silylene with disilane and trisilane",
        journal = "J. Organometal. Chem.",
        pages = """343-349""",
        year = "1996",
    ),
    longDesc = 
u"""
Laser flash photolysis was used to measure rates and fit to Arrhenius form. Error in logA +/- 0.06 and error in Ea +/- 0.4 kJ/mol. Authors note the Arrhenius plot is slightly curved.
""",
)


