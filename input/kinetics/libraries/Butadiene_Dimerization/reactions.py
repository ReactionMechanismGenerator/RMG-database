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
5. Bond and atom additivity corrections were not used for the rate calculation.
"""
entry(
    index = 1,
    label = "BD <=> CB",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.70652e+13, 's^-1'),
        n = -0.361171,
        Ea = (185.835, 'kJ/mol'),
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
        A = (3707.14, 'cm^3/(mol*s)'),
        n = 2.00692,
        Ea = (80.6973, 'kJ/mol'),
        T0 = (1, 'K')),
    shortDesc = u"""Level of theory: CBS-QB3 with 1D rotors in B3LYP/CBSB7""",
    longDesc = 
u"""
library value for butadiene dimerization reactions calculated by Duminda Ranasinghe and Hao-Wei Pang in March 2019. This reaction rate is fitted using Arkane with the default temperature point plus additional 17 temperature points at 303.3 - 473.3. To be specific, the Tlist = ([303.3, 310.0, 320.0, 330.0, 340.0, 341.2, 343.0, 353.0, 363.0, 373.0, 379.0, 383.0, 393.0, 403.0, 413.0, 416.9, 423.0, 433.0, 443.0, 453.0, 454.8, 463.0, 473.0, 492.7, 530.5, 568.4, 606.3, 644.2, 682.0, 719.9, 757.8, 795.7, 833.5, 871.4, 909.3, 947.2, 985.0, 1022.9, 1060.8, 1098.7, 1136.5, 1174.4, 1212.3, 1250.2, 1288.0, 1325.9, 1363.8, 1401.7, 1439.5, 1477.4, 1515.3, 1553.1, 1591.0, 1628.9, 1666.8, 1704.6, 1742.5, 1780.4, 1818.3, 1856.1, 1894.0, 1931.9, 1969.8, 2007.6, 2045.5, 2083.4, 2121.3, 2159.1, 2197.0, 2234.9, 2272.8, 2310.6, 2348.5, 2386.4, 2424.3, 2462.1, 2500.0], 'K')

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
        A = (8.79656e+11, 's^-1'),
        n = -0.10273,
        Ea = (12.1976, 'kJ/mol'),
        T0 = (1, 'K')),
    shortDesc = u"""Level of theory: CBS-QB3 with 1D rotors in B3LYP/CBSB7""",
    longDesc = 
u"""
library value for butadiene dimerization reactions calculated by Duminda Ranasinghe and Hao-Wei Pang in March 2019
""",
)

entry(
    index = 8,
    label = "VCH + BD <=> 4-cyclohex-3-en-1-ylcyclohexene",
    degeneracy = 2,
     kinetics = Arrhenius(
        A = (3.60449, 'cm^3/(mol*s)'),
        n = 2.55723,
        Ea = (87.7601, 'kJ/mol'),
        T0 = (1, 'K'),)
    shortDesc = u"""Level of theory: CBS-QB3 with 1D rotors in B3LYP/CBSB7""",
    longDesc = 
u"""
library value for butadiene polymerization reactions calculated by Duminda Ranasinghe in May 2019
""",
)
