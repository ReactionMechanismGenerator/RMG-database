#!/usr/bin/env python
# encoding: utf-8

name = "Birad_recombination/rules"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 480,
    label = "Rn;Y_rad_out;Ypri_rad_out",
    group1 = "OR{R3, R4, R5, R6}",
    group2 = 
"""
1  *1 R!H 1
""",
    group3 = 
"""
1  *2 R!H 1
""",
    kinetics = ArrheniusEP(
        A = (5e+11,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (30,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 482,
    label = "R6_SSSDS;C_rad_out_H/OneDe;Cpri_rad_out_2H",
    group1 = 
"""
1  *1 {Cs,Cd,CO,Os} 1 {2,S}
2  *3 {Cs,Cd,CO,Os} 0 {1,S} {3,S}
3     {Cs,Cd,CO,Os} 0 {2,S} {4,S}
4     Cd 0 {3,S} {5,D}
5  *4 Cd 0 {4,D} {6,S}
6  *2 {Cs,Cd,CO,Os} 1 {5,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    group3 = 
"""
1  *2 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2e+12,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (1.8,"kcal/mol","+|-",1),
        Tmin = (550,"K"),
        Tmax = (650,"K"),
    ),
    reference = None,
    referenceType = "",
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
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 485,
    label = "R4_SSS;C_rad_out_2H;Cpri_rad_out_2H",
    group1 = 
"""
1  *1 {Cs,Cd,CO,Os} 1 {2,S}
2  *3 {Cs,Cd,CO,Os} 0 {1,S} {3,S}
3  *4 {Cs,Cd,CO,Os} 0 {2,S} {4,S}
4  *2 {Cs,Cd,CO,Os} 1 {3,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    group3 = 
"""
1  *2 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.62e+12,"s^-1"),
        n = -0.305,
        alpha = 0,
        E0 = (1.98,"kcal/mol"),
        Tmin = (600,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "",
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
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 486,
    label = "R6_SSSSS;C_rad_out_2H;Cpri_rad_out_2H",
    group1 = 
"""
1  *1 {Cs,Cd,CO,Os} 1 {2,S}
2  *3 {Cs,Cd,CO,Os} 0 {1,S} {3,S}
3     {Cs,Cd,CO,Os} 0 {2,S} {4,S}
4     {Cs,Cd,CO,Os} 0 {3,S} {5,S}
5  *4 {Cs,Cd,CO,Os} 0 {4,S} {6,S}
6  *2 {Cs,Cd,CO,Os} 1 {5,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    group3 = 
"""
1  *2 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.21e+10,"s^-1"),
        n = 0.137,
        alpha = 0,
        E0 = (2.12,"kcal/mol"),
        Tmin = (600,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "",
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
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

