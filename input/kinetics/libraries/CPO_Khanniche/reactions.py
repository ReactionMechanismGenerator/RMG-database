#!/usr/bin/env python
# enndex = 9,
#coding: utf-8

name = "CPO_sarahkha"
shortDesc = u"Reactions for Hexylbenzene pyrolysis at 450C"
longDesc = u"""
In conjunction with the CPO thermo library,
this reaction library contains CBS-QB3 calculations for reactions
relevant to CPO oxidation.

Both calculations are done in CBS-QB3 level of theory.

Specifics of the calculations performed:
1. CBS-QB3 Level of theory was used after a B3LYP/6-311G(d,p) geometry optimization was performed
2. CBS-QB3 Energy calculation was performed
3. Frequency was calculated using B3LYP/CBSB7 iop(7/33=1) (Hessian was calculated)
4. 1D Hindered Rotors were calculated for steps of 10 degrees up to the full 360 degree cycle, with geometry optimization on each step.
5. All files generated were fed to Cantherm.
6. Frequency scaling factor was 0.99
7. Bond additivity corrections were not used.

"""
entry(
    index = 1,
    label = 'CPO-O2rad_alpha <=> CPO-HO2_alpha-rad_alpha',
    kinetics = Arrhenius(
        A = (4774.94, 's^-1'),
        n = 2.3351,
        Ea = (67.7657, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.34489, dn = +|- 0.0371708, dEa = +|- 0.307905 kJ/mol',
    ),
    degeneracy = 1,
    shortDesc = u"Calculation performed by Sarah Khanniche, entered May 2018, CBS-QB3 level of theory, /home/sarahkha/Cantherm/CPO/R1/radA/reactionA/reaction"
)

entry(
    index = 2,
    label = 'CPO-O2rad_alpha <=> CPO-HO2_alpha-rad_beta',
    kinetics = Arrhenius(
        A = (73841.1, 's^-1'),
        n = 2.00297,
        Ea = (95.6791, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.22845, dn = +|- 0.025811, dEa = +|- 0.213806 kJ/mol',
    ),
    degeneracy = 1,
    shortDesc = u"Calculation performed by Sarah Khanniche, CBS-QB3 level of theory,/home/sarahkha/Cantherm/CPO/R1/radA/reactionB/reaction "
)

entry(
    index = 3,
    label = 'CPO-HO2_alpha-rad_alpha <=> CPOoh-O2_alpha-rad',
    kinetics = Arrhenius(
        A = (2.36996e+13, 's^-1'),
        n = -0.451155,
        Ea = (30.8637, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.05802, dn = +|- 0.0070746, dEa = +|- 0.0586026 kJ/mol',
    ),
    degeneracy = 1,
    shortDesc = u"Calculation performed by Sarah Khanniche, entered May 2018, CBS-QB3 level of theory,/home/sarahkha/Cantherm/CPO/R2/radA/reacion",
)

entry(
    index = 4,
    label = 'CPO-O2rad_beta <=> CPO-HO2_beta-rad_alpha',
    kinetics = Arrhenius(
        A = (8174.36, 's^-1'),
        n = 2.32588,
        Ea = (78.9904, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.34359, dn = +|- 0.0370493, dEa = +|- 0.306899 kJ/mol',
    ),
    degeneracy = 1,
    shortDesc = u"Calculation performed by Sarah Khanniche, entered May 2018, CBS-QB3 level of theory,/home/sarahkha/Cantherm/CPO/R1/radB/reactionA/reaction",
)

entry(
    index = 5,
    label = 'CPO-O2rad_beta <=> CPO-HO2_beta-rad_beta',
     kinetics = Arrhenius(
        A = (10763.1, 's^-1'),
        n = 2.50232,
        Ea = (119.032, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.42627, dn = +|- 0.0445405, dEa = +|- 0.368952 kJ/mol',
    ),
    degeneracy = 1,
    shortDesc = u"Calculation performed by Sarah Khanniche, entered May 2018, CBS-QB3 level of theory,/home/sarahkha/Cantherm/CPO/R1/radB/reactionB/reaction",
)

entry(
    index = 6,
    label = 'CPO-HO2_beta-rad_alpha <=> CPO-HO2_beta-rad_beta',
     kinetics = Arrhenius(
        A = (10763.1, 's^-1'),
        n = 2.50232,
        Ea = (119.032, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.42627, dn = +|- 0.0445405, dEa = +|- 0.368952 kJ/mol',
    ),
    degeneracy = 1,
    shortDesc = u"Calculation performed by Sarah Khanniche, entered May 2018, CBS-QB3 level of theory,/home/sarahkha/Cantherm/CPO/R1/radB/reactionB/reaction",
)

entry(
    index = 7,
    label = 'CPO-HO2_alpha-rad_alpha <=> sciss-HO2_alpha-rad_alpha',
    kinetics = Arrhenius(
        A = (9.58666e+11, 's^-1'),
        n = 0.75713,
        Ea = (170.412, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.02639, dn = +|- 0.00326786, dEa = +|- 0.0270694 kJ/mol',
    ),
    degeneracy = 1,
    shortDesc = u"Calculation performed by Sarah Khanniche,entered May 2018, CBS-QB3 level of theory, /home/sarahkha/Cantherm/CPO/R3/Alpha/radAprim/reaction",
    longDesc = 
"""
"""
)

entry(
    index = 8,
    label = 'CPO-HO2_alpha-rad_beta <=> sciss-HO2_alpha-rad_beta',
    kinetics = Arrhenius(
        A = (1.9222e+17, 's^-1'),
        n = -0.908278,
        Ea = (135.483, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.04414, dn = +|- 0.00541852, dEa = +|- 0.0448845 kJ/mol',
    ),
    degeneracy = 1,
    shortDesc = u"Calculation performed by Sarah Khanniche,entered May 2018, CBS-QB3 level of theory, /home/sarahkha/Cantherm/CPO/R3/Alpha/radBprim/reaction",
    longDesc =
"""
"""
)


entry(
    index = 9,
    label = 'CPO-HO2_beta-rad_alpha <=> CPOoh-O2_beta-rad_alpha',
    kinetics = Arrhenius(
        A = (41019.6, 's^-1'),
        n = 1.84467,
        Ea = (137.701, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.26621, dn = +|- 0.0296084, dEa = +|- 0.245261 kJ/mol',
   ),
   degeneracy = 1,
   shortDesc = u"Calculation performed by Sarah Khanniche,entered May 2018, CBS-QB3 level of theory",
   longDesc =
"""
location: /home/sarahkha/Cantherm/CPO/R1/radB/reactionB/reaction
"""
)

