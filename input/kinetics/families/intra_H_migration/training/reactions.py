#!/usr/bin/env python
# encoding: utf-8

name = "intra_H_migration/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 1,
    label = "C2H3O3 <=> C2H3O3-2",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.3e+09, 's^-1', '*|/', 2.51189),
        n = 0.75,
        Ea = (23.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["J. W. Allen", "C. F. Goldsmith", "W. H. Green"],
        title = u'Automatic Estimation of Pressure-Dependent Rate Coefficients',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "???",
        pages = """???-???""",
        year = "2011 (accepted)",
    ),
    referenceType = "theory",
    shortDesc = u"""CFG VTST calculations at RQCISD(T)/CBS//B3LYP/6-311++G(d,p) level""",
    longDesc = 
u"""
Quantum chemistry calculations at the RQCISD(T)/CBS//B3LYP/6-311++G(d,p) level
using Gaussian 03 and MOLPRO. High-pressure-limit rate coefficient computed
using Variflex.
""",
)

entry(
    index = 2,
    label = "S1C4 <=> S1C4b",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.775e+09, 's^-1', '*|/', 3.0),
        n = 0.686,
        Ea = (6.774, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["E. E. Dames", "W. H. Green"],
        title = u'THE EFFECT OF ALCOHOL AND CARBONYL FUNCTIONAL GROUPS ON THE COMPETITION BETWEEN UNIMOLECULAR DECOMPOSITION AND ISOMERIZATION IN C 1 -C 5 ALKOXY RADICALS',
        journal = "Intl. J. Chem. Kin.",
        volume = "???",
        pages = """???-???""",
        year = "2015",
    ),
    referenceType = "theory",
    shortDesc = u"""TST calculations at M08SO/MG3S level""",
    longDesc = 
u"""
Quantum chemistry calculations at the M08SO/MG3S level
using Qchem. High-pressure-limit rate coefficient computed
using Cantherm with 1D hindered rotor treatment.
""",
)

entry(
    index = 3,
    label = "S2C4 <=> S2C4b",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.540e+04, 's^-1', '*|/', 3.0),
        n = 2.338,
        Ea = (7.127, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["E. E. Dames", "W. H. Green"],
        title = u'THE EFFECT OF ALCOHOL AND CARBONYL FUNCTIONAL GROUPS ON THE COMPETITION BETWEEN UNIMOLECULAR DECOMPOSITION AND ISOMERIZATION IN C 1 -C 5 ALKOXY RADICALS',
        journal = "Intl. J. Chem. Kin.",
        volume = "???",
        pages = """???-???""",
        year = "2015",
    ),
    referenceType = "theory",
    shortDesc = u"""TST calculations at M08SO/MG3S level""",
    longDesc = 
u"""
Quantum chemistry calculations at the M08SO/MG3S level
using Qchem. High-pressure-limit rate coefficient computed
using Cantherm with 1D hindered rotor treatment.
""",
)

entry(
    index = 4,
    label = "C4H7O2 <=> C4H7O2b",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (6.358e+01, 's^-1', '*|/', 3.66),
        n = 2.81162,
        Ea = (8.231, 'kcal/mol', '+|-', 1.00),
        T0 = (1, 'K'),
    ),
    reference = "",
    referenceType = "theory",
    shortDesc = u"""TST calculations at M08SO/MG3S level by edames""",
    longDesc = 
u"""
Quantum chemistry calculations at the M08SO/MG3S* level using Qchem. High-pressure-limit rate coefficient computed using Cantherm with 1D hindered rotor treatment for all relevant rotors. (*A computational grid with 75 radial points and 434 angular points per radial point was used in the calculations for all species)
""",
)