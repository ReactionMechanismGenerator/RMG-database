#!/usr/bin/env python
# encoding: utf-8

name = "CO2_Elimination_From_Carboxylic_Acid/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "C2HF2O2 <=> CHF2 + CO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.85e-12,'s^-1'), n=6.85, Ea=(32530.5,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/CO2_Elimination_From_Carboxylic_Acid_Rad/
Original entry: CF2C(O)OH <=> CF2H+CO2
""",
)

entry(
    index = 1,
    label = "C3HF4O2 <=> C2HF4 + CO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.54e-21,'s^-1'), n=9.6, Ea=(27803.9,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/CO2_Elimination_From_Carboxylic_Acid_Rad/
Original entry: CF3CFC(O)OH <=> CF3CFH+CO2
""",
)

entry(
    index = 2,
    label = "C3HF4O3 <=> C2HF4O + CO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.15e-12,'s^-1'), n=7.1, Ea=(32688.4,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/CO2_Elimination_From_Carboxylic_Acid_Rad/
Original entry: CF3OCFC(O)OH <=> CF3OCFH+CO2
""",
)

entry(
    index = 3,
    label = "C4HF6O3 <=> C3HF6O + CO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.1e-13,'s^-1'), n=7.32, Ea=(32895.4,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/CO2_Elimination_From_Carboxylic_Acid_Rad/
Original entry: C2F5OCFC(O)OH <=> C2F5OCFH+CO2
""",
)

entry(
    index = 4,
    label = "C2H3O2 <=> CH3 + CO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.38e-17,'s^-1'), n=8.39, Ea=(24346.7,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/CO2_Elimination_From_Carboxylic_Acid_Rad/
Original entry: CH2C(O)OH <=> CH3+CO2
""",
)

entry(
    index = 5,
    label = "C3H5O3 <=> C2H5O + CO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(181000,'s^-1'), n=2.09, Ea=(42692.4,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/CO2_Elimination_From_Carboxylic_Acid_Rad/
Original entry: CH3OCHC(O)OH <=> CH3OCH2+CO2
""",
)

entry(
    index = 6,
    label = "C4H7O3 <=> C3H7O + CO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.36e+06,'s^-1'), n=1.81, Ea=(43859.2,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/CO2_Elimination_From_Carboxylic_Acid_Rad/
Original entry: C2H5OCHC(O)OH <=> C2H5OCH2+CO2
""",
)

