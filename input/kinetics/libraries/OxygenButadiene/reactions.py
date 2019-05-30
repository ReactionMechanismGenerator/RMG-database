#!/usr/bin/env python
# encoding: utf-8

name = "OxygenButadiene"
shortDesc = u"Reactions for singlet oxygen + butadiene"
longDesc = u"""
In conjunction with the OxygenButadiene thermo library,
this reaction library contains CBS-QB3 calculations for reactions
relevant to the fundamentals of polymer fouling in ethylene crackers.

All calculations are done in CBS-QB3 level of theory.

Specifics of the calculations performed:
1. CBS-QB3 Level of theory was used after a B3LYP/6-311G(d,p) geometry optimization was performed
2. Frequency was calculated using B3LYP/CBSB7 iop(7/33=1) (Hessian was calculated)
3. 1D Hindered Rotors were calculated for steps of 10 degrees up to the full 360 degree cycle, with geometry optimization on each step, using B3LYP/CBSB7
4. All files generated were fed to Arkane.
5. Frequency scaling factor was 0.99
6. Bond additivity corrections were not used.

Disclaimer: The number of significant figures displayed does not reflect the accuracy of thermochemistry values. Sommers and Simmie esimates
the error in enthalpy of formation (and therefore the activation energy) by CBS-QB3 calculations to be + or - 2.4kcal/mol 
(http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448). 
"""
entry(
    index = 1,
    label = "O2_singlet + BD <=> C4H6O2_23",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (304364, 'cm^3/(mol*s)'),
        n = 2.08896,
        Ea = (-2.86206, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K')),
    shortDesc = u"Calculation performed by Duminda Ranasinghe, April 2019, CBS-QB3 level of theory",
    longDesc = 
    u"""
CBS-QB3 with frequency calculated using B3LYP/CBSB7 iop(7/33=1), frequency scaling factor 0.99, and 1D hindered rotors. Bond additivity corrections were not used.
    """
)

entry(
    index = 2,
    label = "O2_triplet + BD <=> C4H6O2_23",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (320891, 'cm^3/(mol*s)'),
        n = 2.07889,
        Ea = (107.83, 'kJ/mol'),
        T0 = (1, 'K')),
    shortDesc = u"Calculation performed by Duminda Ranasinghe, April 2019, CBS-QB3 level of theory",
    longDesc = 
    u"""
CBS-QB3 with frequency calculated using B3LYP/CBSB7 iop(7/33=1), frequency scaling factor 0.99, and 1D hindered rotors. Bond additivity corrections were not used.
    """
)

entry(
    index = 3,
    label = "O2_singlet + BD <=> C4H6O2_25",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (138013, 'cm^3/(mol*s)'),
        n = 2.0607,
        Ea = (-1.8136, 'kJ/mol'),
        T0 = (1, 'K')),
    shortDesc = u"Calculation performed by Duminda Ranasinghe, April 2019, CBS-QB3 level of theory",
    longDesc = 
    u"""
CBS-QB3 with frequency calculated using B3LYP/CBSB7 iop(7/33=1), frequency scaling factor 0.99, and 1D hindered rotors. Bond additivity corrections were not used.
    """
)

entry(
    index = 4,
    label = "C4H6O2_23 <=> C4H6O2_25",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.79293e+08, 's^-1'),
        n = 0.466473,
        Ea = (11.5036, 'kJ/mol'),
        T0 = (1, 'K')),
    shortDesc = u"Calculation performed by Duminda Ranasinghe, April 2019, CBS-QB3 level of theory",
    longDesc = 
    u"""
CBS-QB3 with frequency calculated using B3LYP/CBSB7 iop(7/33=1), frequency scaling factor 0.99, and 1D hindered rotors. Bond additivity corrections were not used.
    """
)

entry(
    index = 5,
    label = "",
    degeneracy = 1,
    kinetics = 
    shortDesc = u"Calculation performed by Duminda Ranasinghe, April 2019, CBS-QB3 level of theory",
    longDesc = 
    u"""
CBS-QB3 with frequency calculated using B3LYP/CBSB7 iop(7/33=1), frequency scaling factor 0.99, and 1D hindered rotors. Bond additivity corrections were not used.
    """
)

entry(
    index = 6,
    label = "S_412_singlet <=> C4H6O2_25",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.15063e+11, 's^-1'),
        n = 0.0923366,
        Ea = (10.8852, 'kJ/mol'),
        T0 = (1, 'K')),
    shortDesc = u"Calculation performed by Duminda Ranasinghe, April 2019, CBS-QB3 level of theory",
    longDesc = 
    u"""
CBS-QB3 with frequency calculated using B3LYP/CBSB7 iop(7/33=1), frequency scaling factor 0.99, and 1D hindered rotors. Bond additivity corrections were not used.
    """
)

entry(
    index = 7,
    label = "C4H6O2_23 <=> S_266",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.78369e+09, 's^-1'),
        n = 0.618967,
        Ea = (5.79636, 'kJ/mol'),
        T0 = (1, 'K') 
    shortDesc = u"Calculation performed by Duminda Ranasinghe, April 2019, CBS-QB3 level of theory",
    longDesc = 
    u"""
CBS-QB3 with frequency calculated using B3LYP/CBSB7 iop(7/33=1), frequency scaling factor 0.99, and 1D hindered rotors. Bond additivity corrections were not used.
    """
)

entry(
    index = 8,
    label = "S_266 <=> CH2O_532 + C3H4O_611",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.19602e+11, 's^-1'),
        n = 0.61843,
        Ea = (141.689, 'kJ/mol'),
        T0 = (1, 'K')),
    shortDesc = u"Calculation performed by Duminda Ranasinghe, April 2019, CBS-QB3 level of theory",
    longDesc = 
    u"""
CBS-QB3 with frequency calculated using B3LYP/CBSB7 iop(7/33=1), frequency scaling factor 0.99, and 1D hindered rotors. Bond additivity corrections were not used.
    """
)
