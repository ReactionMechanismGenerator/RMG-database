#!/usr/bin/env python
# encoding: utf-8

name = "1,1_HY_elimination/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Sources:
[1] Characterization of the 1,1-HCl Elimination Reaction of Vibrationally Excited CD3CHFCl Molecules and Assignment of Threshold Energies for 1,1-HCl and 1,2-DCl plus 1,1-HF and 1,2-DF Elimination Reactions
    Timothy M. Brown, Matthew J. Nestler, Samuel M. Rossabi, George L. Heard, D. W. Setser, and Bert E. Holmes
    The Journal of Physical Chemistry A 2015 119 (36), 9441-9451
    DOI: 10.1021/acs.jpca.5b06638

[2] Unimolecular HBr and HF Elimination Reactions of Vibrationally Excited C2H5CH2Br and C2D5CHFBr: Identification of the 1,1-HBr Elimination Reaction from C2D5CHFBr and Search for the C2D5(F)C:HBr Adduct
    Timothy M. Brown, Blanton R. Gillespie, Mallory M. Rothrock, Anthony J. Ranieri, Melinda K. Schueneman, George L. Heard, Donald W. Setser, and Bert E. Holmes
    The Journal of Physical Chemistry A 2019 123 (41), 8776-8786
    DOI: 10.1021/acs.jpca.9b07029

[3] The Unimolecular Reactions of CF3CHF2 Studied by Chemical Activation: Assignment of Rate Constants and Threshold Energies to the 1,2-H Atom Transfer, 1,1-HF and 1,2-HF Elimination Reactions, and the Dependence of Threshold Energies on the Number of F-Atom Substituents in the Fluoroethane Molecules
    Caleb A. Smith, Blanton R. Gillespie, George L. Heard, D. W. Setser, and Bert E. Holmes
    The Journal of Physical Chemistry A 2017 121 (46), 8746-8756
    DOI: 10.1021/acs.jpca.7b06769
"""

entry(
    index = 0,
    label = "CH3CHFCl <=> CH3CF + HCl",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(13.9e+14,'s^-1'), n=0, Ea=(73,'kcal/mol'), T0=(1,'K')),
    rank = 5,
    shortDesc = """MP2/6-311+G(2d,p)""",
    longDesc =
"""
From [1]
Arrhenius form (s−1) at 1000 K
"""
)

entry(
    index = 1,
    label = "CH3CHFCl_2 <=> CH3CCl + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.97e+14,'s^-1'), n=0, Ea=(75.5,'kcal/mol'), T0=(1,'K')),
    rank = 5,
    shortDesc = """MP2/6-311+G(2d,p)""",
longDesc =
"""
From [1]
Arrhenius form (s−1) at 1000 K
"""
)

entry(
    index = 2,
    label = "CH3CHFBr <=> CH3CF + HBr",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(13.9e+14,'s^-1'), n=0, Ea=(65.8,'kcal/mol'), T0=(1,'K')),
    rank = 5,
    shortDesc = """MP2/6-311+G(2d,p)""",
longDesc =
"""
Ea taken from Table 3 in [2]
A factor taken for CH3CHFCl <=> CH3CF + HCl in [1]
"""
)

entry(
    index = 3,
    label = "CH2FCHFBr <=> CH2FCF + HBr",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(13.9e+14,'s^-1'), n=0, Ea=(70.7,'kcal/mol'), T0=(1,'K')),
    rank = 5,
    shortDesc = """MP2/6-311+G(2d,p)""",
longDesc =
"""
Ea taken from Table 3 in [2]
A factor taken for CH3CHFCl <=> CH3CF + HCl in [1]
"""
)

entry(
    index = 4,
    label = "CHF2CHFBr <=> CHF2CF + HBr",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(13.9e+14,'s^-1'), n=0, Ea=(75.5,'kcal/mol'), T0=(1,'K')),
    rank = 5,
    shortDesc = """MP2/6-311+G(2d,p)""",
longDesc =
"""
Ea taken from Table 3 in [2]
A factor taken for CH3CHFCl <=> CH3CF + HCl in [1]
"""
)

entry(
    index = 5,
    label = "CF3CHFBr <=> CF3CF + HBr",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(13.9e+14,'s^-1'), n=0, Ea=(77.3,'kcal/mol'), T0=(1,'K')),
    rank = 5,
    shortDesc = """MP2/6-311+G(2d,p)""",
longDesc =
"""
Ea taken from Table 3 in [2]
A factor taken for CH3CHFCl <=> CH3CF + HCl in [1]
"""
)

entry(
    index = 6,
    label = "CH3CH2CHFBr <=> CH3CH2CF + HBr",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(13.9e+14,'s^-1'), n=0, Ea=(66.0,'kcal/mol'), T0=(1,'K')),
    rank = 5,
    shortDesc = """MP2/6-311+G(2d,p)""",
longDesc =
"""
Ea taken from Table 3 in [2]
A factor taken for CH3CHFCl <=> CH3CF + HCl in [1]
"""
)

entry(
    index = 7,
    label = "CH3CHF2 <=> CH3CF + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.97e+14,'s^-1'), n=0, Ea=(74,'kcal/mol'), T0=(1,'K')),
    rank = 5,
    shortDesc = """experimental""",
longDesc =
"""
Ea taken from Table 2 in [3]
A factor taken for CH3CHFCl <=> CH3CCl + HF in [1]
"""
)

entry(
    index = 8,
    label = "CH2FCHF2 <=> CH2FCF + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.97e+14,'s^-1'), n=0, Ea=(77,'kcal/mol'), T0=(1,'K')),
    rank = 5,
    shortDesc = """experimental""",
longDesc =
"""
Ea taken from Table 2 in [3]
A factor taken for CH3CHFCl <=> CH3CCl + HF in [1]
"""
)

entry(
    index = 9,
    label = "CHF2CHF2 <=> CHF2CF + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.97e+14,'s^-1'), n=0, Ea=(84,'kcal/mol'), T0=(1,'K')),
    rank = 5,
    shortDesc = """M062X/6-311G(2d,p)""",
longDesc =
"""
Ea taken from Table 2 in [3]
A factor taken for CH3CHFCl <=> CH3CCl + HF in [1]
"""
)

entry(
    index = 10,
    label = "CF3CHF2 <=> CF3CF + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.97e+14,'s^-1'), n=0, Ea=(85,'kcal/mol'), T0=(1,'K')),
    rank = 5,
    shortDesc = """M062X/6-311G(2d,p)""",
longDesc =
"""
Ea taken from Table 2 in [3]
A factor taken for CH3CHFCl <=> CH3CCl + HF in [1]
"""
)


