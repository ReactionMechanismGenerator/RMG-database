# encoding: utf-8
name = "ZarasCyclopentanone"
shortDesc = u"Library for Cyclopentanone pyrolysis"
longDesc = u"""
Computational Kinetic Study for the Unimolecular Decomposition of Cyclopentanone
ARISTOTELIS M. ZARAS, SEBASTIEN THION, PHILIPPE DAGAUT
"""
entry(
    index = 1,
    label = "CPO <=> CPO-birad",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.51e27, '1/s'), n=-3.460, Ea=(356.9, 'kJ/mol'), T0=(1, 'K'), Tmin=(500,'K'), Tmax = (2000,'K')),
    shortDesc = u"""G3B3 level calculation""",
    longDesc = """
    Zaras et al. 2015, Computational Kinetic Study for the Unimolecular Decomposition of Cyclopentanone 
    G3B3 level calculations
    """
)

#entry(
#    index = 2,
#    label = "CPO <=> C2H4 + C2H4 + CO",
#    degeneracy = 1,
#    kinetics = Arrhenius(A=(1.62e23, '1/s'), n=-1.980, Ea=(358.6, 'kJ/mol'), T0=(1, 'K'), Tmin=(500,'K'), Tmax = (2000,'K')),
#    shortDesc = u"""G3B3 level calculation""",
#    longDesc = """
#    Zaras et al. 2015, Computational Kinetic Study for the Unimolecular Decomposition of Cyclopentanone 
#    G3B3 level calculations
#    """
#)

#entry(
#    index = 3,
#    label = "CPO <=> Butene + CO",
#    degeneracy = 1,
#    kinetics = Arrhenius(A=(7.54e18, '1/s'), n=-.970, Ea=(484.1, 'kJ/mol'), T0=(1, 'K'), Tmin=(500,'K'), Tmax = (2000,'K')),
#    shortDesc = u"""G3B3 level calculation""",
#    longDesc = """
#    Zaras et al. 2015, Computational Kinetic Study for the Unimolecular Decomposition of Cyclopentanone 
#    G3B3 level calculations
#    """
#)

#entry(
#    index = 4,
#    label = "CPO <=> H2 + CPO-eneend",
#    degeneracy = 1,
#    kinetics = Arrhenius(A=(2.13e16, '1/s'), n=-.670, Ea=(485.8, 'kJ/mol'), T0=(1, 'K'), Tmin=(500,'K'), Tmax = (2000,'K')),
#    shortDesc = u"""G3B3 level calculation""",
#    longDesc = """
#    Zaras et al. 2015, Computational Kinetic Study for the Unimolecular Decomposition of Cyclopentanone 
#    G3B3 level calculations
#    """
#)

#entry(
#    index = 5,
#    label = "CPO <=> H2 + CPO-eneside",
#    degeneracy = 1,
#    kinetics = Arrhenius(A=(1.24e16, '1/s'), n=-.750, Ea=(423.4, 'kJ/mol'), T0=(1, 'K'), Tmin=(500,'K'), Tmax = (2000,'K')),
#    shortDesc = u"""G3B3 level calculation""",
#    longDesc = """
#    Zaras et al. 2015, Computational Kinetic Study for the Unimolecular Decomposition of Cyclopentanone 
#    G3B3 level calculations
#    """
#)

entry(
    index = 6,
    label = "CPO <=> CPO-enol",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.77e16, '1/s'), n=-1.020, Ea=(318.0, 'kJ/mol'), T0=(1, 'K'), Tmin=(500,'K'), Tmax = (2000,'K')),
    shortDesc = u"""G3B3 level calculation""",
    longDesc = """
    Zaras et al. 2015, Computational Kinetic Study for the Unimolecular Decomposition of Cyclopentanone 
    G3B3 level calculations
    """
)

entry(
    index = 7,
    label = "CPO <=> CPO-enechain",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.20e18, '1/s'), n=-1.040, Ea=(524.7, 'kJ/mol'), T0=(1, 'K'), Tmin=(500,'K'), Tmax = (2000,'K')),
    shortDesc = u"""G3B3 level calculation""",
    longDesc = """
    Zaras et al. 2015, Computational Kinetic Study for the Unimolecular Decomposition of Cyclopentanone 
    G3B3 level calculations
    """
)