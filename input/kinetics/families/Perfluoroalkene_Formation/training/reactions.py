#!/usr/bin/env python
# encoding: utf-8

name = "Perfluoroalkene_Formation/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "C3F8 <=> CF4 + C2F4",
    degeneracy = 6.0,
    kinetics = Arrhenius(A=(3.8e+10,'s^-1'), n=1.49, Ea=(137246,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/Perfluoroalkene_Formation/
Original entry: C3F8 <=> CF2CF2+CF4
""",
)

entry(
    index = 1,
    label = "C3F6O <=> CF2O + C2F4",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(1.87e+08,'s^-1'), n=1.21, Ea=(82079.9,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/Perfluoroalkene_Formation/
Original entry: C2F5CFO <=> CF2CF2+CF2O
""",
)

entry(
    index = 2,
    label = "C4F8O <=> CF2O + C3F6",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.46e+06,'s^-1'), n=1.56, Ea=(80833,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/Perfluoroalkene_Formation/
Original entry: C3F7CFO <=> CF3CFCF2+CF2O
""",
)

entry(
    index = 3,
    label = "C3H8 <=> CH4 + C2H4",
    degeneracy = 6.0,
    kinetics = Arrhenius(A=(5.72e-35,'s^-1'), n=14.26, Ea=(87732.9,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/Perfluoroalkene_Formation/
Original entry: C3H8 <=> CH2CH2+CH4
""",
)

entry(
    index = 4,
    label = "C3H6O <=> CH2O + C2H4",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(1570,'s^-1'), n=2.7, Ea=(76386.5,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/Perfluoroalkene_Formation/
Original entry: C2H5CHO <=> CH2O+CH2CH2
""",
)

entry(
    index = 5,
    label = "C4H8O <=> CH2O + C3H6",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(413000,'s^-1'), n=1.73, Ea=(69957.8,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/Perfluoroalkene_Formation/
Original entry: C3H7CHO <=> CH2O+CH3CHCH2
""",
)

