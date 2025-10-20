#!/usr/bin/env python
# encoding: utf-8

name = "CO_CF_bond_dissociation/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "C3F6O <=> CF2O + C2F4",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(1.7e+09,'s^-1'), n=1.16, Ea=(83135.3,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/CO_CF_bond_dissociation/
Original entry: CF3OCFCF2 <=> CF2O+CF2CF2
""",
)

entry(
    index = 1,
    label = "C3F6O-2 <=> CF2O + C2F4-2",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(2.43e+08,'s^-1'), n=1.22, Ea=(48702.3,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/CO_CF_bond_dissociation/
Original entry: CF3OCCF3 <=> CF3CF+CF2O
""",
)

entry(
    index = 2,
    label = "C3HF7O <=> CF2O + C2HF5",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(3.59e+11,'s^-1'), n=0.77, Ea=(82880,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/CO_CF_bond_dissociation/
Original entry: CF3OCFHCF3 <=> CF2O+C2F5H
""",
)

entry(
    index = 3,
    label = "C3F6O2 <=> CF2O + C2F4O",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(1.87e+11,'s^-1'), n=0.42, Ea=(49974.7,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/CO_CF_bond_dissociation/
Original entry: CF3OC(O)CF3 <=> CF2O+CF3CFO
""",
)

entry(
    index = 4,
    label = "C4F8O <=> C2F4O-2 + C2F4",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(5.3e+08,'s^-1'), n=1.02, Ea=(81186.6,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/CO_CF_bond_dissociation/
Original entry: C2F5OCFCF2 <=> CF3CFO+CF2CF2
""",
)

entry(
    index = 5,
    label = "C4F8O-2 <=> C2F4O-2 + C2F4-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.53e+09,'s^-1'), n=0.9, Ea=(52188.2,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/CO_CF_bond_dissociation/
Original entry: C2F5OCCF3 <=> CF3CFO+CF3CF
""",
)

entry(
    index = 6,
    label = "C4F8O2 <=> C2F4O-2 + C2F4O",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.16e+12,'s^-1'), n=-0.04, Ea=(50928.4,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/CO_CF_bond_dissociation/
Original entry: C2F5OC(O)CF3 <=> CF3CFO+CF3CFO
""",
)

entry(
    index = 7,
    label = "C5F10O <=> C3F6O-3 + C2F4",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(9.54e+08,'s^-1'), n=1.06, Ea=(80760.3,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/CO_CF_bond_dissociation/
Original entry: C3F7OCFCF2 <=> C2F5CFO+CF2CF2
""",
)

entry(
    index = 8,
    label = "C5F10O-2 <=> C3F6O-3 + C2F4-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(3.26e+08,'s^-1'), n=1.07, Ea=(51125.8,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/CO_CF_bond_dissociation/
Original entry: C3F7OCCF3 <=> C2F5CFO+CF3CF
""",
)

entry(
    index = 9,
    label = "C5HF11O <=> C3F6O-3 + C2HF5",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.18e+10,'s^-1'), n=0.8, Ea=(79374.9,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/CO_CF_bond_dissociation/
Original entry: C3F7OCFHCF3 <=> C2F5CFO+C2F5H
""",
)

entry(
    index = 10,
    label = "C5F10O2 <=> C3F6O-3 + C2F4O",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(4.47e+11,'s^-1'), n=0.12, Ea=(50136.7,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/CO_CF_bond_dissociation/
Original entry: C3F7OC(O)CF3 <=> C2F5CFO+CF3CFO
""",
)

entry(
    index = 11,
    label = "C3H6O <=> CH2O + C2H4",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(841000,'s^-1'), n=2.05, Ea=(97010.1,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/CO_CF_bond_dissociation/
Original entry: CH3OCHCH2 <=> CH2O+CH2CH2
""",
)

entry(
    index = 12,
    label = "C4H8O <=> C2H4O + C2H4",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(7.79e+06,'s^-1'), n=1.63, Ea=(93876.2,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/CO_CF_bond_dissociation/
Original entry: C2H5OCHCH2 <=> CH3CHO+CH2CH2
""",
)

entry(
    index = 13,
    label = "C4H8O-2 <=> C2H4O + C2H4-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(4.11e+06,'s^-1'), n=1.75, Ea=(44653.7,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/CO_CF_bond_dissociation/
Original entry: C2H5OCCH3 <=> CH3CHO+CH3CH
""",
)

entry(
    index = 14,
    label = "C5H10O <=> C3H6O-2 + C2H4-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.12e+06,'s^-1'), n=1.87, Ea=(44732.4,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/CO_CF_bond_dissociation/
Original entry: C3H7OCCH3 <=> C2H5CHO+CH3CH
""",
)

entry(
    index = 15,
    label = "C3H8O <=> CH2O + C2H6",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(8.23e+07,'s^-1'), n=1.63, Ea=(91694.6,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/CO_CF_bond_dissociation/
Original entry: CH3OC2H5 <=> CH2O+C2H6
""",
)

entry(
    index = 16,
    label = "C4H10O <=> C2H4O + C2H6",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(6.64e+07,'s^-1'), n=1.5, Ea=(91491.1,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/CO_CF_bond_dissociation/
Original entry: C2H5OC2H5 <=> CH3CHO+C2H6
""",
)

entry(
    index = 17,
    label = "C3H6O2 <=> CH2O + C2H4O-2",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(2.32e+06,'s^-1'), n=1.94, Ea=(76374.9,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/CO_CF_bond_dissociation/
Original entry: CH3OC(O)CH3 <=> CH3CHO+CH2O
""",
)

entry(
    index = 18,
    label = "C4H8O2 <=> C2H4O + C2H4O-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(3.73e+06,'s^-1'), n=1.71, Ea=(71885.4,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/CO_CF_bond_dissociation/
Original entry: C2H5OC(O)CH3 <=> CH3CHO+CH3CHO
""",
)

entry(
    index = 19,
    label = "C2F5OCFHCF3 <=> CF3CFO+C2F5H",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(4.98e+09,'s^-1'), n=0.79, Ea=(79774,'cal/mol'), T0=(1,'K')),
)

entry(
    index = 20,
    label = "C3HF4O3 <=> CF2O + C2HF2O2",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(1.02e+07,'s^-1'), n=1.62, Ea=(30984.3,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/R_Addition_MultipleBond/ (actually matched to CO_CF_Bond_Diss.)
Original entry: CF3OCFC(O)OH <=> CF2O+CF2C(O)OH
""",
)

entry(
    index = 21,
    label = "C4HF6O3 <=> C2F4O-2 + C2HF2O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.85e+07,'s^-1'), n=1.44, Ea=(23859.7,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/R_Addition_MultipleBond/ (actually matched to CO_CF_Bond_Diss.)
Original entry: C2F5OCFC(O)OH <=> CF3CFO+CF2C(O)OH
""",
)

entry(
    index = 22,
    label = "C5HF8O3 <=> C3F6O-3 + C2HF2O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(9e+06,'s^-1'), n=1.39, Ea=(21512.2,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/R_Addition_MultipleBond/ (actually matched to CO_CF_Bond_Diss.)
Original entry: C3F7OCFC(O)OH <=> C2F5CFO+CF2C(O)OH
""",
)

entry(
    index = 23,
    label = "C4F9O2 <=> CF2O + C3F7O",
    degeneracy = 6.0,
    kinetics = Arrhenius(A=(2480,'s^-1'), n=2.51, Ea=(65844.2,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/R_Addition_MultipleBond/ (actually matched to CO_CF_Bond_Diss.)
Original entry: CF3OC(CF3)OCF3 <=> CF3OCFCF3+CF2O
""",
)

entry(
    index = 24,
    label = "C5F11O2 <=> CF2O + C4F9O",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(15200,'s^-1'), n=2.17, Ea=(66752.6,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/R_Addition_MultipleBond/ (actually matched to CO_CF_Bond_Diss.)
Original entry: C2F5OC(CF3)OCF3 <=> C2F5OCFCF3+CF2O
""",
)

entry(
    index = 25,
    label = "CH3OCHC(O)OH <=> CH2C(O)OH+CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.75e+07,'s^-1'), n=1.52, Ea=(27913,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/R_Addition_MultipleBond/ (actually matched to CO_CF_Bond_Diss.)
Original entry: CH3OCHC(O)OH <=> CH2C(O)OH+CH2O
""",
)

entry(
    index = 26,
    label = "C4F9O-2 <=> C2F4O-2 + C2F5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.59e+10,'s^-1'), n=0.65, Ea=(22327.4,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/R_Addition_MultipleBond/ (MULTIPLE MATCHING with CO_CF_Bond_Diss & R_Addition_multiple_bond. Only added training reaction in here.)
Original entry: C2F5OCFCF3 <=> CF3CFO+C2F5
""",
)

entry(
    index = 27,
    label = "CF3OCF2 <=> CF3+CF2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.95e+09,'s^-1'), n=1.2, Ea=(27353.5,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/R_Addition_MultipleBond/ (MULTIPLE MATCHING with CO_CF_Bond_Diss & R_Addition_multiple_bond. Only added training reaction in here.)
Original entry: CF3OCF2 <=> CF3+CF2O
""",
)

entry(
    index = 28,
    label = "C2H5OCHCH3 <=> C2H4O+C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.78e+10,'s^-1'), n=0.74, Ea=(22459.6,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/R_Addition_MultipleBond/ (MULTIPLE MATCHING with CO_CF_Bond_Diss & R_Addition_multiple_bond. Only added training reaction in here.)
Original entry: C2H5OCHCH3 <=> CH3CHO+C2H5
""",
)

