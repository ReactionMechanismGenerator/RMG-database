#!/usr/bin/env python
# encoding: utf-8

name = "Butadiene_Dimerization"
shortDesc = u"Reactions for Butadiene Dimerization"
longDesc = u"""
In conjunction with the Butadiene_Dimerization thermo library,
this reaction library contains CBS-QB3 calculations for reactions
relevant to Butadiene_Dimerization.
Both calculations are done in CBS-QB3 level of theory.
Specifics of the calculations performed:
1. CBS-QB3 Level of theory was used after a B3LYP/6-311G(d,p) geometry optimization was performed with frequency scale factor: 0.99
2. Frequency was calculated using B3LYP/CBSB7 iop(7/33=1) (Hessian was calculated)
3. 1D Hindered Rotors were calculated for steps of 10 degrees up to the full 360 degree cycle, with geometry optimization on each step, using B3LYP/CBSB7
4. All files generated were fed to Arkane.
5. Bond additivity correction was not used for the rate calculation.
"""
entry(
    index = 1,
    label = "BD <=> CB",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.70652e+13, 's^-1'),
        n = -0.361171,
        Ea = (187.676, 'kJ/mol'),
        T0 = (1, 'K')
    ),
    shortDesc = u"""Level of theory: CBS-QB3 with 1D rotors in B3LYP/CBSB7""",
    longDesc = 
u"""
library value for butadiene dimerization reactions calculated by Duminda Ranasinghe and Hao-Wei Pang in March 2019
""",
)

entry(
    index = 2,
    label = "DVCB <=> COD",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.33836e+08, 's^-1'),
        n = 0.725968,
        Ea = (102.12, 'kJ/mol'),
        T0 = (1, 'K')),
    shortDesc = u"""Level of theory: CBS-QB3 with 1D rotors in B3LYP/CBSB7""",
    longDesc = 
u"""
library value for butadiene dimerization reactions calculated by Duminda Ranasinghe and Hao-Wei Pang in March 2019
""",
)

entry(
    index = 3,
    label = "BD + BD <=> VCH",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (17635, 'cm^3/(mol*s)'),
        n = 1.8055,
        Ea = (81.8512, 'kJ/mol'),
        T0 = (1, 'K')
    ),
    shortDesc = u"""Level of theory: CBS-QB3 with 1D rotors in B3LYP/CBSB7""",
    longDesc = 
u"""
library value for butadiene dimerization reactions calculated by Duminda Ranasinghe and Hao-Wei Pang in March 2019
""",
)

entry(
    index = 4,
    label = "DVT <=> BD + BD",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.42238e+12, 's^-1'),
        n = -0.0448663,
        Ea = (52.0893, 'kJ/mol'),
        T0 = (1, 'K')),
    shortDesc = u"""Level of theory: CBS-QB3 with 1D rotors in B3LYP/CBSB7""",
    longDesc = 
u"""
library value for butadiene dimerization reactions calculated by Duminda Ranasinghe and Hao-Wei Pang in March 2019
""",
)

entry(
    index = 5,
    label = "DVT <=> VCH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.49424e+11, 's^-1'),
        n = -0.0806221,
        Ea = (12.5388, 'kJ/mol'),
        T0 = (1, 'K')),
    shortDesc = u"""Level of theory: CBS-QB3 with 1D rotors in B3LYP/CBSB7""",
    longDesc = 
u"""
library value for butadiene dimerization reactions calculated by Duminda Ranasinghe and Hao-Wei Pang in March 2019
""",
)

entry(
    index = 6,
    label = "DVT <=> COD",
    degeneracy = 1,
     kinetics = Arrhenius(
        A = (1.56665e+11, 's^-1'),
        n = -0.0961041,
        Ea = (25.7391, 'kJ/mol'),
        T0 = (1, 'K')),
    shortDesc = u"""Level of theory: CBS-QB3 with 1D rotors in B3LYP/CBSB7""",
    longDesc = 
u"""
library value for butadiene dimerization reactions calculated by Duminda Ranasinghe and Hao-Wei Pang in March 2019
""",
)

entry(
    index = 7,
    label = "DVT <=> DVCB",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3971e+12, 's^-1'),
        n = -0.104026,
        Ea = (16.1686, 'kJ/mol'),
        T0 = (1, 'K')
    ),
    shortDesc = u"""Level of theory: CBS-QB3 with 1D rotors in B3LYP/CBSB7""",
    longDesc = 
u"""
library value for butadiene dimerization reactions calculated by Duminda Ranasinghe and Hao-Wei Pang in March 2019
""",
)
