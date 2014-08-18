#!/usr/bin/env python
# encoding: utf-8

name = "Birad_recombination/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 480,
    label = "Rn;Y_rad_out;Ypri_rad_out",
    kinetics = ArrheniusEP(
        A = (500000000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (30, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = 
u"""

""",
)

entry(
    index = 482,
    label = "R6_SSSDS;C_rad_out_H/OneDe;Cpri_rad_out_2H",
    kinetics = ArrheniusEP(
        A = (2000000000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (1.8, 'kcal/mol', '+|-', 1),
        Tmin = (550, 'K'),
        Tmax = (650, 'K'),
    ),
    rank = 4,
    shortDesc = u"""[186] Benson et al.""",
    longDesc = 
u"""
[186] Benson, S.W. J. Chem. Phys. 1967, 46, 4920.

CH2=CHCH(.)CH2CH2CH(.)CH=CH2 --> 4-vinylcyclohexene. (Rxn. -c); arises from birad recombination of resonance isomer: .CH2CH=CHCH2CH2CH(.)CH=CH2

Data are estimated.

***this only considers cis-cis isomer reaction*** cis-trans A prefactor is 50% of the value used here; also, on p. 4923, it is stated that cis trans rate is 5/6 of the overall rate, so maybe the k that should be used is 0.6 of the value currently in place?
Verified by Greg Magoon: Rxn. -d. also looks to be of interest here; whether the rate is high-pressure limit was not investigated, but p. 4922 says that pressures involved were low; DE0 uncertainty added; regarding temperature range, I considered dropping lower temperature limit from 550 K to 400 K (based on p. 4923), but it seems that experiments were performed at or around 600 K, so I will leave it at 550-650 K

Note: after some preliminary confusion on my part, it looks like the existing groups are correct (the correct resonance form for the CH2 radical is taken into account with the Ypri_rad_out (i.e. Cpri_rad_out_H2)), but arguably, another, a more-specific group (C_rad_out_H2/OneDe and Cpri_rad_out_H2/OneDe) should be specified to account for delocalizing group at this site
""",
)

entry(
    index = 485,
    label = "R4_SSS;C_rad_out_2H;Cpri_rad_out_2H",
    kinetics = ArrheniusEP(
        A = (1620000000000.0, 's^-1'),
        n = -0.305,
        alpha = 0,
        E0 = (1.98, 'kcal/mol'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""[x] Sirjean et al.""",
    longDesc = 
u"""
[x] Sirjean, B.; Glaude, P. A.; Ruiz-Lopez, M. F.; Fournet, R.; J. Phys. Chem. A. 2006, 110, 12693-12704. 
http://dx.doi.org/10.1021/jp0651081
.CH2CH2CH2CH2CH2. -> cyclopentane (k4-1 in Scheme 5/Table 7)

TST calculation

Added by Greg Magoon: Stated pressure is 1 atm, but I believe they are actually calculating the high-pressure limit rate constant
""",
)

entry(
    index = 486,
    label = "R5_SSSS;C_rad_out_2H;Cpri_rad_out_2H",
    kinetics = ArrheniusEP(
        A = (7760000000.0, 's^-1'),
        n = 0.311,
        alpha = 0,
        E0 = (1.7, 'kcal/mol'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""[x] Sirjean et al.""",
    longDesc = 
u"""
[x] Sirjean, B.; Glaude, P. A.; Ruiz-Lopez, M. F.; Fournet, R.; J. Phys. Chem. A. 2006, 110, 12693-12704. 
http://dx.doi.org/10.1021/jp0651081
.CH2CH2CH2CH2CH2CH2. -> cyclohexane (k5-1+k5-2 in Scheme 7/Table 10) (includes formation of both boat and chair conformations)

TST calculation

Added by Greg Magoon: Stated pressure is 1 atm, but I believe they are actually calculating the high-pressure limit rate constant; the rate constant added here was found my performing least squares fit for log(ktot) from 600-2000 K (where ktot is the sum of k5-1 and k5-2)

Note: Recent experimental/RRKM study by Kiefer, Gupte, Harding, and Klippenstein (http://www.combustion.org.uk/ECM_2009/P810069.pdf) (stated uncertainty is +/- 30%) appears to agree with Sirjean et al. results, but they only report forward rate constant
""",
)

entry(
    index = 487,
    label = "R6_SSSSS;C_rad_out_2H;Cpri_rad_out_2H",
    kinetics = ArrheniusEP(
        A = (32100000000.0, 's^-1'),
        n = 0.137,
        alpha = 0,
        E0 = (2.12, 'kcal/mol'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""[x] Sirjean et al.""",
    longDesc = 
u"""

""",
)

entry(
    index = 488,
    label = "R3_SS;S_rad;Spri_rad",
    kinetics = ArrheniusEP(
        A = (2.18e+16, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (0.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""A.G. Vandeputte""",
    longDesc = 
u"""

""",
)

