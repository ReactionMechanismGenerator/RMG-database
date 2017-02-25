#!/usr/bin/env python
# encoding: utf-8

name = "R_Recombination/rules"
shortDesc = u""
longDesc = u"""
For some reason the definition of Cs_rad::

 Cs_rad
 1 * C 1 

which is not mutually exclusive from its L2 siblings such as::

 Cd_rad
 1 * C 1 {2,D}, {3,S}
 2   C 0 {1,D}
 3   R 0 {1,S}

is apparently not causing a problem
"""
entry(
    index = 424,
    label = "Y_rad;Y_rad",
    kinetics = ArrheniusEP(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
)

entry(
    index = 425,
    label = "H_rad;H_rad",
    kinetics = ArrheniusEP(
        A = (1.09e+11, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (1.5, 'kcal/mol'),
        Tmin = (278, 'K'),
        Tmax = (372, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Dingle et al. [167]""",
    longDesc = 
u"""
[167] Dingle, J.R.; Le Roy, D.J.; J. Chem. Phys. 1950, 18, 1632.

Absolute value measured directly. Excitation: thermal. H + H --> H2 Bath gas: C2H2

NIST record: http://kinetics.nist.gov/kinetics/Detail?id=1950DIN/LER1632-1637:1
***high probability of inaccuracy***
Checked by Greg Magoon; I suspect the parameters in the paper come from a different reaction (maybe H + C2H2 -> products?); (even if it was the correct reaction, the parameters used by NIST and RMG appear to be based off of values from the abstract, but p. 1637 seems to suggest that it may be more complicated, perhaps a collision theory-type form as alluded to in the abstract...p. 1637 states "In calculating E1 allowance was made for the term T^1/2 appearing in the frequency factor.";if this is the case, then the NIST record is inaccurate; almost all the other papers in NIST database report 3rd order rate constant, which is proportional to [M]; the best assessment I have found is Stace and Murrell, IJCK, v. 10, p. 197-212, which seems to suggest bimolecular rate constant of at least ~10^14 at high pressure (over 3 orders of magnitude higher than this value); this paper and Troe, Ann. Rev. Phys. Chem. 1978. 29: 223-250. make reference to "diffusion" limitations at very high pressure; another (relatively minor) consideration is that we will probably want to divide the reported rate coefficient by 2 to correctly account for stoichiometry
""",
)

entry(
    index = 426,
    label = "H_rad;C_methyl",
    kinetics = ArrheniusEP(
        A = (1.93e+14, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Takahashi et al. [168] Transition state theory.""",
    longDesc = 
u"""
[168] Takahashi, J.; Momose, T.; Shida, T. Bull. Chem. Soc. Jpn. 1994, 67, 74.

H + CH3 --> CH4

CVTST calculation
NIST record: http://kinetics.nist.gov/kinetics/Detail?id=1994TAK/MOM74-85:2
Verified by Greg Magoon: RMG value agrees with NIST record, and the points in the NIST record agree with the values in Table 3 in the paper within 10%; note that a 3000K data point is also available in the paper, but doesn't seem to be considered in the NIST fit; also, note that a lot of other data for this reaction is available on the NIST site and in the paper
""",
)

entry(
    index = 427,
    label = "H_rad;C_methyl",
    kinetics = ArrheniusEP(
        A = (2.11e+14, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1000, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Baulch et al. [94] literature review.""",
    longDesc = 
u"""
[94] Baulch, D.L.; Cobos, C.J.; Cox, R.A.; Frank, P.; Hayman, G,; Just, T.; Kerr, J.A.; Murrells, T.; Pilling, M.J.; 
Troe, J.; Walker, R.W.; Warnatz, J. J. Phys. Chem. Ref. Data 1994, 23, 847.

H + CH3 --> CH4

pg 870 Evaluated Kinetic Data for Combustion Modelling Supplement 1, Table 3. Combination reactions.

RMG data matches reference data for k(infinity).
 Verified by Karma James

pg.903-906: Discussion on evaluated data

H+CH3(+m) --> CH4(+m): RMG stores the recommended rate coefficient for k_inf.  Recommended

rate coefficient is that reported by Baulch et al. in previous literature review
(since no new experimental data had been reported since).
MRH 31-Aug-2009
""",
)

entry(
    index = 428,
    label = "H_rad;C_rad/H2/Cs",
    kinetics = ArrheniusEP(
        A = (1e+14, 'cm^3/(mol*s)', '+|-', 1e+13),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (298, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sillensen et al [169]""",
    longDesc = 
u"""
[169] Sillesen , A.; Ratajczak, E.; Pagsberg, P. Chem. Phys. Lett. 1993, 201, 171.
Data derived from fitting to a complex mechanism. Excitation: radiolysis, analysis: IR absroption. Pressure 0.10 bar

H + C2H5 (+ M) --> C2H6 (+ M) (Rxn. 2b)

***NHP***
Verified by Greg Magoon; I changed the DA uncertainty from (times/divide)1.1 to (+/-)1E13, as this is what the abstract reports (also, Table 3 mentions uncertainties in the range of 10%-20%)
""",
)

entry(
    index = 429,
    label = "H_rad;C_rad/H/NonDeC",
    kinetics = ArrheniusEP(
        A = (2e+13, 'cm^3/(mol*s)', '*|/', 3.16),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Warnatz [134] literature review.""",
    longDesc = 
u"""
[134] Warnatz, J. Rate coefficeints in the C/H/O system. In Combustion Chemistry, 1984; pp 197.
""",
)

entry(
    index = 430,
    label = "H_rad;C_rad/H/NonDeC",
    kinetics = ArrheniusEP(
        A = (1.5e+14, 'cm^3/(mol*s)', '+|-', 3e+13),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (298, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Munk et al. [170]""",
    longDesc = 
u"""
[170] Munk, J; Pagsberg, P.; Ratajczak, E.; Sillensen, A. Chem. Phys. Lett. 1986, 132, 417.
Data derived from fitting to a complex mechanism. Excitation: electron beam, analysis: Vis-UV absorption. Pressure 1.0 atm

H + isoC3H7 (+ M) --> C3H8 (+ M) (Rxn. 7)

***NHP***
Verified by Greg Magoon; I changed the DA uncertainty from (times/divide)1.25 to 0.3E+14, as reported in the paper
""",
)

entry(
    index = 431,
    label = "H_rad;Cd_pri_rad",
    kinetics = ArrheniusEP(
        A = (1.21e+14, 'cm^3/(mol*s)', '+|-', 4.82e+13),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (298, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Fahr et al. [171]""",
    longDesc = 
u"""
[171] Fahr, A.; Laufer, A.; Klein, R.; Braun, W. J. Phys. Chem. 1991, 95, 3218.
Absolute value measured directly. Excitation: flash photolysis, analysis : Vis-UV absorption. Pressure 0.13 atm. Original uncertainty 4.8E+13

H + C2H3 -> C2H4 (Rxn. VIIC)

***NHP***
Verified by Greg Magoon; note that the value in rateLibrary agrees with value reported in abstract, the value in Table III also includes contribution from Rxn. VIID, which apparently dominates at low pressures (p. 3222); DA uncertainty updated, as I have done elsewhere; also, for k, I calculate 1.2044E14 (which is very slightly different from 1.21 used here)
""",
)

entry(
    index = 432,
    label = "H_rad;Cd_pri_rad",
    kinetics = ArrheniusEP(
        A = (5.36e+14, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0.98, 'kcal/mol'),
        Tmin = (700, 'K'),
        Tmax = (1300, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Duran et al. [165]""",
    longDesc = 
u"""
[165] Duran, R. P.; Amorebieta, V. T.; Colussi, A. J. J. Phys. Chem. 1988, 92, 636.
Ab initio

H + C2H3 --> C2H4 (Rxn. 13)

NIST Record: http://kinetics.nist.gov/kinetics/Detail?id=1988DUR/AMO636:10
Verified by Greg Magoon; RMG and NIST data seem to be the same; presumably, NIST fit is based off of data in Table 3, but the fit isn't quite right, especially at 1500 K ; using the 700 and 1300 table values, I get Ea=1.03 kcal/mol; using 1300 K value, I get A = 5.66E14 cm^3/mol-s; fit seems to be essentially indistinguishable from data at end points, and error is just under 10% at 1000 K...since the NIST fit has a slightly lower maximum error, I will just leave it the way it is; aside: 10^9.7 prefactor mentioned on p. 637 doesn't seem consistent with NIST data or paper data in Table III; this is presumably high-pressure limit since no pressure-dependence is indicated in the table
""",
)

entry(
    index = 433,
    label = "H_rad;Ct_rad/Ct",
    kinetics = ArrheniusEP(
        A = (1.81e+14, 'cm^3/(mol*s)', '*|/', 3),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R. F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
H + C2H --> C2H2

pg 1101, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 21,4.

Verified by Karma James

NOTE: Reported rate coefficients are for k_inf (MRH 11Aug2009)

pg. 1218-1219: Discussion on evaluated data

Recommended data (k_inf) based on reverse rate and equilibrium constant

Fall-off and collisional efficiencies are available in reference
(although we do not store them in RMG_database)
MRH 28-Aug-2009
""",
)

entry(
    index = 434,
    label = "H_rad;Cb_rad",
    kinetics = ArrheniusEP(
        A = (2.2e+14, 'cm^3/(mol*s)', '+|-', 8e+13),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1200, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Davis et al. [172] Ackermann et al. [173] Emdee et al. [172b]""",
    longDesc = 
u"""
[172] Davis, S. G.; Wang, H.; Brezinsky K.; Law C. K. Symp. Int. Combust. Proc. 1996, 26, 1025.
(1000-1200K, excitation : thermal, pressure 1.0 atm)

[173] Ackerman, L.; Hippler, H.; Pagsberg, P.; Reihs, C.; Troe, J. J. Phys. Chem. 1990, 94, 5247. 
(300K, absolute value measured directly, excitation : flash photolysis, analysis : VIS-UV absorption, pressure 0.01-0.99 atm) 

[172b] Emdee, J. L., Brezinsky, K., and Glassman, I., J. Phys. Chem. 96:21512161 (1992) DOI: 10.1021/j100184a025
H + phenyl --> benzene (R1 in [172]) (Reaction 1 in [172b])
Verified by Greg Magoon
[172]: reported rate coefficient is for k_inf (see Table 1); temperature range considered is 1000-1200 K; this paper cites: Emdee, J. L., Brezinsky, K., and Glassman, I., J. Phys. Chem. 96:21512161 (1992) DOI: 10.1021/j100184a025 (included as 172b, above), which, in turn, references [173] (Troe) paper...conditions for this paper are 1100 K - 1200 K
[173]: this contains the uncertainty estimate (see Table 2); I updated the DA uncertainty as I have done elsewhere; this seems to be the actual raw value that was subsequently interpreted/used in the paper cited by Ref. 172; conditions are 300 K and 1 bar, so apparently, the paper cited by Ref. 172 and/or Ref. 172 itself has assumed that it is in high-pressure limit and that it is temperature independent
[172b]: see Table III
""",
)

entry(
    index = 435,
    label = "H_rad;CO_pri_rad",
    kinetics = ArrheniusEP(
        A = (4.68e+10, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (-4.53, 'kcal/mol'),
        Tmin = (1500, 'K'),
        Tmax = (1900, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Tsuboi et al. [174]""",
    longDesc = 
u"""
[174] Tsuboi, T.; Katoh, M.; Kikuchi, S.; Hashimoto, K. Jpn J. Appl. Phys. 1981, 20, 985.
Data is estimated. Pressure 7.0 atm. 

H + HCO (+M) --> H2CO (+M) (Rxn -9)

***NHP*** possible improvement for A (for rho = 1E-4): 6.61E10
Verified by Greg Magoon; three A factors have been reported (for 3 different densities); the value currently used in the rateLibrary appears to come from the middle density: 5E-5 (mol/cm^3, I think);I have assumed that the 2nd two columns in Table II are for the reverse reaction reference for this value is apparently in Japanese (see *** note in Table 2); minor issue: I calculate -19/4.184 = -4.54 kcal/mol (vs. -4.53 in rateLibrary)
""",
)

entry(
    index = 436,
    label = "H_rad;O_pri_rad",
    kinetics = ArrheniusEP(
        A = (1.62e+14, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2100, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Cobos et al. [106]""",
    longDesc = 
u"""
[106] Cobos, C. J.; Troe, J. J. Chem. Phys. 1985, 83, 1010. 
Transition State Theory

H + OH --> H2O
""",
)

entry(
    index = 437,
    label = "C_methyl;C_methyl",
    kinetics = ArrheniusEP(
        A = (8.26e+17, 'cm^3/(mol*s)'),
        n = -1.4,
        alpha = 0,
        E0 = (1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Pesa et al. [175]""",
    longDesc = 
u"""
[175] Pesa, M. ; Pilling, M. J.; Robertson, S. H.; Wardlaw. J. Phys. Chem. A 1998, 102, 8526.
Canonical Flexible Transition State Theory 

CH3 + CH3 --> C2H6 (Same as 438) (Rxn. R1)

NIST record: http://kinetics.nist.gov/kinetics/Detail?id=1998PES/PIL8526-8536:1
Verified by Greg Magoon; NIST record has slightly different parameters than RMG (it doesn't seem like best-fit parameters are reported in the paper); paper values for k_inf with alpha = 1 appear in Tables 5/11 and values for alpha = 0.7 appear in Tables 6/12; NIST parameters agree within 10% of k_inf values in the paper with alpha = 1 A^-1 (Tables 11) (though in paper, they seem to suggest that alpha = 0.7 A^-1 (Table 6/12) matches experimental data better); I am assuming that their k is for the reaction, as written, so that no factor of two correction is needed; RMG parameters seem to agree with Table 5 values within 10% (agreement may not be quite as good as NIST fit, though it is not immediately obvious which fit is better without looking closer/doing calculations)
""",
)

entry(
    index = 438,
    label = "C_methyl;C_methyl",
    kinetics = ArrheniusEP(
        A = (3.61e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Baulch et al. [94] literature review.""",
    longDesc = 
u"""
[94] Baulch, D. L.; Cobos, C. J.; Cox, R. A.; Frank, P.; Hayman, G.; Just, T.; Kerr, J. A.; 
Murrells, T.; Pilling, M. J.; Troe, J.; Walker, R. W.; Warnatz, J. J. Phys. Chem. Ref. Data 1994, 23, 847.

CH3 + CH3 --> C2H6 (Same as 437)

pg 871 Evaluated Kinetic Data for Combustion Modelling Supplement 1, Table 3. Combination reactions.

RMG data matches reference data for k(infinity).

Verified by Karma James

pg.980-983: Discussion on evaluated data

CH3+CH3(+m) --> C2H6(+m): RMG stores the recommended high-pressure limit rate coefficient,

k_inf.  "The recommended values are based mainly on the extensive sets of data
from Refs. 4, 10, 11, and 14 up to 1000K ..."
MRH 31-Aug-2009
""",
)

entry(
    index = 439,
    label = "C_methyl;C_rad/H2/Cs",
    kinetics = ArrheniusEP(
        A = (3.37e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Baulch et al. [94] literature review.""",
    longDesc = 
u"""
[94] Baulch, D. L.; Cobos, C. J.; Cox, R. A.; Frank, P.; Hayman, G.; Just, T.; Kerr, J. A.;
Murrells, T.; Pilling, M. J.; Troe, J.; Walker, R. W.; Warnatz, J. J. Phys. Chem. Ref. Data 1994, 23, 847.

CH3 + C2H5 --> C3H8

pg 871 Evaluated Kinetic Data for Combustion Modelling Supplement 1, Table 3. Combination reactions.

RMG data matches reference data for k(infinity).

Verified by Karma James

pg.991: Discussion on evaluated data

CH3+C2H5(+m) --> C3H8(+m): RMG stores the recommended high-pressure limit rate coefficient,

k_inf.  "The recommended value for k_inf is a weighted average of earlier experiments
in agreement with SACM calculations following Ref.10.  A temperature independent value
of k_inf is assumed until more definite experimental information is available."
MRH 31-Aug-2009
""",
)

entry(
    index = 440,
    label = "C_methyl;C_rad/H/NonDeC",
    kinetics = ArrheniusEP(
        A = (6.64e+14, 'cm^3/(mol*s)'),
        n = -0.57,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (713, 'K'),
        Tmax = (1800, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Tsang [176] RRK(M) extrapolation.""",
    longDesc = 
u"""
[176] Tsang, W. Combust. Flame 1989, 78, 71. 
RRK(M) extrapolation. 

CH3 + iso-C3H7 --> iso-C4H10 

Verified by Greg Magoon; high-pressure rate constants are reported here; 
I don't immediately see an explicit temperature range for the polynomial fits, 
but the domain of the graphs agrees pretty well with the range in the rateLibrary 
(though the graphs seem to go slightly higher, to 2000 K); the abstract says 
"from room to combustion temperatures", so if anything, the range specified in 
the rateLibrary is probably too narrow; minor: I calculate 1.1E-9*6.022141E23=6.624E14, 
but rateLibrary has slightly different value of 6.64E14
""",
)

entry(
    index = 441,
    label = "C_methyl;C_rad/Cs3",
    kinetics = ArrheniusEP(
        A = (4.88e+15, 'cm^3/(mol*s)', '*|/', 2),
        n = -1,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Tsang [92] literature review.""",
    longDesc = 
u"""
[92] Tsang, W. J. Phys. Chem. Ref. Data 1990, 19, 1.

CH3 + tert-C4H9 --> neo-C5H12

pg 7, Chemical Kinetic Database For Combustion Chemistry, Part 4 - Isobutane. 

Index of Reactions and Summary of Recommended Rate Expressions. No. 44,16.
Verified by Karma James

NOTE: Data entry was not consistent w/recommended value in reference (pg. 36)

MRH computes A=4.88E+15, n=-1, E=0, dA=*2.0 (11Aug2009)

MRH interprets data in reference as 2.7E-11*(300/T)^-1, NOT 2.7E-11*exp(300/T)

NOTE: kinetics.nist.gov has 2.7E-11*exp(300/T) expression in database

kinetics.nist.gov also has A/n/E from 2006 paper by Klippenstein et al.;
the new rate expression matches Klippenstein's value better across the valid T range
pg.36: Discussion on evaluated data

Entry 44,16(b)

MRH computed geometric mean of CH3+CH3-->adduct (1.68x10^-9 * T^-0.64) and tC4H9+tC4H9-->adduct

(4x10^-12 * (300/T)^1.5) to obtain: 5.909x10^-9 * T^-1.07.  Setting the temperature
exponent equal to one and multiplying by 1 (*300/300) results in: 1.970x10^-11 * (300/T)
which is somewhat in agreement with the value recommended by Tsang.
MRH 31-Aug-2009
""",
)

entry(
    index = 442,
    label = "C_methyl;Cd_pri_rad",
    kinetics = ArrheniusEP(
        A = (7.23e+13, 'cm^3/(mol*s)', '+|-', 1.81e+13),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (298, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Fahr et al. [171]""",
    longDesc = 
u"""
[171] Fahr, A.; Laufer, A.; Klein, R.; Braun, W. J. Phys. Chem. 1991, 95, 3218.
Absolute value measured directly. Excitation: flash photolysis, analysis : Vis-UV absorption. Pressure 0.13 atm. Original Uncertainty 1.8E+13

CH3. + .HC=CH2 --> CH3HC=CH2 (Rxn. IIIC)

***NHP***
Verified by Greg Magoon; DA uncertainty updated, as I have done elsewhere
""",
)

entry(
    index = 443,
    label = "C_methyl;Cb_rad",
    kinetics = ArrheniusEP(
        A = (1.38e+13, 'cm^3/(mol*s)', '+|-', 8e+11),
        n = 0,
        alpha = 0,
        E0 = (0.046, 'kcal/mol', '+|-', 0.072),
        Tmin = (300, 'K'),
        Tmax = (980, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Tokmakov et al. [177]""",
    longDesc = 
u"""
[177] Tokmakov, I. V.; Park, J.; Gheyas, S. I.; Lin, M. C. J. Phys. Chem. A. 1999, 103, 3636.
Data Derived from detailed balance/reverse rate. Uncertainty 8.0E-2. 

CH3 + phenyl --> C6H5CH3 (Rxn. 2) (cf. #444, below)

***NHP***
Verified by Greg Magoon; 0.05 kcal barrier changed to 0.046 as reported in paper; uncertainties are in abstract; more precise values appear in Tables 3,4; however, note: in text on p. 3639, A factor uncertainty is expressed as additive on log scale...value is relatively small, so it probably doesn't make that much of a difference; DA uncertainty was added and DE0 uncertainty was refined
""",
)

entry(
    index = 444,
    label = "C_methyl;Cb_rad",
    kinetics = ArrheniusEP(
        A = (1.39e+13, 'cm^3/(mol*s)', '+|-', 7e+11),
        n = 0,
        alpha = 0,
        E0 = (0.03, 'kcal/mol', '+|-', 0.07),
        Tmin = (424, 'K'),
        Tmax = (972, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Park et al. [178]""",
    longDesc = 
u"""
[178] Park, J.; Cheyas, s. I.; Lin, M. C. Int. J. Chem. Kinet. 1999, 31, 645.
Absolute value measured directly. Excitation: flash photolysis, analysis : mass spectometry. Pressure 0.05 atm. Uncertainty 7.0E-02 

CH3 + phenyl --> C6H5CH3 (Rxn. 4) (cf. #443, above)

***NHP***
Verified by Greg Magoon; values appear in Appendix A and (with uncertainty) on p. 649; total pressure around 3 torr (Table II); DA uncertainty was added and DE0 uncertainty was refined
""",
)

entry(
    index = 445,
    label = "C_methyl;CO_pri_rad",
    kinetics = ArrheniusEP(
        A = (1.81e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R. F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
CH3 + HCO --> CH3CHO 

pg 1095, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 16,15.

Verified by Karma James

pg. 1167: Discussion on evaluated data

Recommended data calculated using reverse rate and equilibrium constant

Authors note that their RRKM calculations suggest that rxn is very close
to high-P limit at low temperatures.
MRH 28-Aug-2009
""",
)

entry(
    index = 446,
    label = "C_methyl;CO_rad/NonDe",
    kinetics = ArrheniusEP(
        A = (4.2e+13, 'cm^3/(mol*s)', '+|-', 8.4e+12),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (298, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Hassinen et al [179]""",
    longDesc = 
u"""
[179] Hassinen, E.; Kalliorinne, K; Koskikallio, J. Int. J. Chem. Kinet. 1990, 22, 741
Data derived from fitting to a complex mechanism. Excitation : direct photolysis, analysis : GC. Pressure 96? and 99 kPa with He, 5.5 kPa and 25 kPa with CO2. 

CH3CO. + .CH3 --> (CH3)2CO (Rxn. 6)

paper states reaction occurs close to high pressure limit (p. 742)
Verified by Greg Magoon; Note that the paper cites 4 other values for k6 from literature; perhaps uncertainty could be assigned based on these values; also, page 744 discusses "relatively large value of k6" potentially due to other reactions; p. 744: uncertainty estimated to be 20% -> I changed DA uncertainty from 0 to 8.4E+12
""",
)

entry(
    index = 447,
    label = "C_methyl;CO_rad/NonDe",
    kinetics = ArrheniusEP(
        A = (4.04e+15, 'cm^3/(mol*s)', '*|/', 1.5),
        n = -0.8,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R. F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
CH3 + CH3CO --> (CH3)2CO 

pg 1103, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 22,16.

Verified by Karma James

NOTE: Reported rate coefficients are for k_inf (MRH 11Aug2009)

pg. 1232-1233: Discussion on evaluated data

Recommended data computed using reverse rate constant (assuming pre-exponential factor

of 5x10^16 s^-1) and equilibrium constant.
Fall-off curves and collisional efficiencies are reported (although we do not

store them in RMG_database)
Rate coefficient expression given on pg. 1232 different from that reported in

table on pg. 1103.  Value in RMG and on kinetics.nist.gov agree with the
expression reported in table.
MRH 28-Aug-2009
""",
)

entry(
    index = 448,
    label = "C_methyl;O_pri_rad",
    kinetics = ArrheniusEP(
        A = (6.03e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Baulch et al. [94] literature review.""",
    longDesc = 
u"""
[94] Baulch, D. L.; Cobos, C. J.; Cox, R. A.; Frank, P.; Hayman, G.; Just, T.; Kerr, J. A.;
Murrells, T.; Pilling, M. J.; Troe, J.; Walker, R. W.; Warnatz, J. J. Phys. Chem. Ref. Data 1994, 23, 847.

CH3 + .OH --> CH3OH

pg 871 Evaluated Kinetic Data for Combustion Modelling Supplement 1, Table 3. Combination reactions.

RMG data matches reference data for k(infinity).

Verified by Karma James

pg.933-934: Discussion of evaluated data

OH+CH3(+m) --> CH3OH(+m): RMG stores the recommended high-pressure limit rate coefficient,

k_inf.  "The available database is still limited and more measurements are needed.
... The preferred k_inf is consistent with SACM estimates ..."
MRH 31-Aug-2009
""",
)

entry(
    index = 449,
    label = "C_methyl;O_rad/NonDe",
    kinetics = ArrheniusEP(
        A = (1.21e+13, 'cm^3/(mol*s)', '*|/', 5),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R. F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
CH3 + CH3O --> (CH3)2O

pg 1104, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 24,16.

Verified by Karma James

pg. 1247: Discussion on evaluated data

Recommended data from study by Gray, Shaw, and Thynne (1967).  Expression was

estimated from rates of CH3+CH3=C2H6 and CH3O+CH3O=CH3OOCH3.
MRH 28-Aug-2009
""",
)

entry(
    index = 450,
    label = "C_rad/H2/Cs;C_rad/H2/Cs",
    kinetics = ArrheniusEP(
        A = (1.15e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1200, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Baulch et al. [95] literature review.""",
    longDesc = 
u"""
[95] Baulch, D. L.; Cobos, C. J.; Cox, R. A.; Esser, C.; Frank, P.; Just, T.; Kerr, 
J. A.; Pilling, M. J.; Troe, J.; Walker, R. W.; Warnatz, J. J. Phys. Chem. Ref. Data 1992, 21, 411.

.C2H5 + .C2H5 --> n-C4H10 

pg.707: Discussion on evaluated data

C2H5+C2H5 --> nC4H10: "The preferred rate coefficient is the mean of the results of

Parkes and Quinn, Adachi et al., Demissy and Lesclaux, Pacey and Wimalasena,
Munk et al., Arthur, and Anastasi and Arthur which are all in substantial 
agreement."
MRH 31-Aug-2009
""",
)

entry(
    index = 451,
    label = "C_rad/H2/Cs;C_rad/H/NonDeC",
    kinetics = ArrheniusEP(
        A = (1.15e+14, 'cm^3/(mol*s)', '*|/', 2),
        n = -0.35,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Tsang [91] literature review.""",
    longDesc = 
u"""
[91] Tsang, W. J. Phys. Chem. Ref. Data 1988, 17, 887.
C2H5 + iso-C3H7 --> iso-C5H12

pg 894, Chemical Kinetic Database For Combustion Chemistry, Part 3. Index of Reactions and Summary of Recommended Rate Expressions. No. 42,17.

Verified by Karma James

pg. 937-938: Discussion on evaluated data

Entry 42,17 (a): No data available at the time.  The author obtains the recommended

rate coefficient expression by using the geometric mean rule (using the rxn rates
of C2H5+C2H5-->adduct and i-C3H7+i-C3H7-->adduct).
MRH 30-Aug-2009
""",
)

entry(
    index = 452,
    label = "C_rad/H2/Cs;C_rad/Cs3",
    kinetics = ArrheniusEP(
        A = (6.91e+14, 'cm^3/(mol*s)', '*|/', 2),
        n = -0.75,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Tsang [92] literature review.""",
    longDesc = 
u"""
[92] Tsang, W. J Phys. Chem. Ref. Data 1990, 19, 1.
C2H5 + tert-C4H9 --> (CH3)3CCH2CH3

//DOES NOT MATCH! Reference: A = 9.6E+12, E0 = 0, n = -0.75, Database: A = 6.91E+14, E0 = 0, n = -0.75

//pg 7, Chemical Kinetic Database For Combustion Chemistry, Part 4 - Isobutane. 

//Index of Reactions and Summary of Recommended Rate Expressions. No. 44,17.

//Verified by Karma James

pg. 37

Data reported as kc = 1.6e-11 * (300/T)^0.75

When lumping the 1.6e-11 * 300^0.75, attain A=6.94e+14
No experimental data, at the time

Verified by MRH on 10Aug2009

pg.37: Discussion on evaluated data

Entry 44,17(c): Recommended rate calculated by taking geometric mean of C2H5+C2H5-->adduct

and tC4H9+tC4H9-->adduct rxns.
MRH 31-Aug-2009
""",
)

entry(
    index = 453,
    label = "C_rad/H2/Cs;CO_pri_rad",
    kinetics = ArrheniusEP(
        A = (1.81e+13, 'cm^3/(mol*s)', '*|/', 3),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R. F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
C2H5 + HCO --> C2H5CHO

pg 1097, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 17,15.

Verified by Karma James

pg. 1179: Discussion on evaluated data

Recommended data is based on the rate expression for CH3+CHO-->H3CCHO

MRH 28-Aug-2009
""",
)

entry(
    index = 454,
    label = "C_rad/H2/Cs;CO_rad/NonDe",
    kinetics = ArrheniusEP(
        A = (3.12e+14, 'cm^3/(mol*s)', '*|/', 3),
        n = -0.5,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R. F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
C2H5 + CH3CO --> C2H5COCH3

pg 1103, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 22,17.

Verified by Karma James

pg. 1234: Discussion on evaluated data

Recommended data is based on the rate expression for CH3+CH3CO-->(CH3)2CO

MRH 28-Aug-2009
""",
)

entry(
    index = 455,
    label = "C_rad/H2/Cs;O_pri_rad",
    kinetics = ArrheniusEP(
        A = (7.7e+13, 'cm^3/(mol*s)', '+|-', 1e+13),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (400, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Fagerstrom et al. [180]""",
    longDesc = 
u"""
[180] Fagerstrom, K.; Lund, A.; Mahmoud, G.; Jodkowski, J. T.; Ratajczak, E. Chem. Phys. Lett. 1993, 208, 321
Excitation : radiolysis, analysis : VIS-UV absorption. Pressure 0.25-0.99 bar SF6. Original Uncertainty 1.0E+13. 

C2H5 + OH (+M) --> C2H5OH (+M) (Rxn. 1a)

Verified by Greg Magoon; value reported for k1a,Infinity (high-pressure) appears to be theoretical rather than experimentally based; value in paper is 7.7+/-1.0E13 (rateLibrary originally had 7.69E13 with uncertainty of *1.1, so I changed it to match paper values); there doesn't seem to be an experimental value for k1a, but k(1a+1b) is slightly lower (6.5E13); experimentally, they say no pressure dependence observed in studied pressure range (p. 326)
""",
)

entry(
    index = 456,
    label = "C_rad/H/NonDeC;C_rad/H/NonDeC",
    kinetics = ArrheniusEP(
        A = (3.25e+14, 'cm^3/(mol*s)', '*|/', 2),
        n = -0.7,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Tsang [91] literature review.""",
    longDesc = 
u"""
[91] Tsang, W. J. Phys. Chem. Ref. Data 1988, 17, 887.
Iso-C3H7 + iso-C3H7 --> (CH3)2CHCH(CH3)2

pg 895, Chemical Kinetic Database For Combustion Chemistry, Part 3. Index of Reactions and Summary of Recommended Rate Expressions. No. 42,42.

//NOTE: For A value, Database value = 3.25E+14 and Reference value = 6.023E+12

Verified by Karma James

MRH computes reference A value = 3.26E+14 (11Aug2009)

pg. 946-947: Discussion on evaluated data

Entry 42,42 (a): Multiple data available at low T.  Author fit experimentally reported

data to obtain recommended rate coefficient expression.  Note: the author states
that more high-Temperature data points are necessary (to ensure a reasonable
fit at high-T).
MRH 30-Aug-2009
""",
)

entry(
    index = 457,
    label = "C_rad/H/NonDeC;C_rad/Cs3",
    kinetics = ArrheniusEP(
        A = (4.12e+15, 'cm^3/(mol*s)', '*|/', 1.5),
        n = -1.1,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Tsang [92] literature review.""",
    longDesc = 
u"""
[92] Tsang, W. J Phys. Chem. Ref. Data 1990, 19, 1.
Iso-C3H7 + tert-C4H9 --> 2,2,3-trimethyl-butane

//DOES NOT MATCH! Reference: A = 7.83E+12, E0 = 0, n = -1.1, Database: A = 4.12E+15, E0 = 0, n = -1.1

//pg 8, Chemical Kinetic Database For Combustion Chemistry, Part 4 - Isobutane. 

//Index of Reactions and Summary of Recommended Rate Expressions. No. 44,42.

//Verified by Karma James

pg. 46

Data reported as kc = 1.3e-11 * (300/T)^1.1

When lumping the 1.3e-11 * 300^1.1, attain A=4.15e+15
No experimental data, at the time

Verified by MRH on 10Aug2009

Entry 44,42(c): Recommended rate computed using geometric mean of iC3H7+iC3H7-->adduct

and tC4H9+tC4H9-->adduct rxns.
MRH 31-Aug-2009
""",
)

entry(
    index = 458,
    label = "C_rad/H/NonDeC;CO_rad/NonDe",
    kinetics = ArrheniusEP(
        A = (6.64e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = -0.35,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Tsang [91] literature review.""",
    longDesc = 
u"""
[91] Tsang, W. J. Phys. Chem. Ref. Data 1988, 17, 887.
Iso-C3H7 + CH3CO --> iso-C3H7COCH3

pg 895, Chemical Kinetic Database For Combustion Chemistry, Part 3. Index of Reactions and Summary of Recommended Rate Expressions. No. 42,22.

//NOTE: For A value, Database value = 6.64E+13 and Reference value = 9.03E+12

Verified by Karma James

MRH computes reference A value = 6.65E+13 (11Aug2009)

pg. 943: Discussion on evaluated data

Entry 42,22: No data available at the time.  Author uses the geometrical mean rule

(for the rxns i-C3H7+i-C3H7-->adduct and CH3CO+CH3CO-->adduct) to obtain 
recommended rate coefficient expression
MRH 30-Aug-2009
""",
)

entry(
    index = 459,
    label = "C_rad/H/NonDeC;O_rad/NonDe",
    kinetics = ArrheniusEP(
        A = (6.03e+12, 'cm^3/(mol*s)', '*|/', 5),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Tsang [91] literature review.""",
    longDesc = 
u"""
[91] Tsang, W. J. Phys. Chem. Ref. Data 1988, 17, 887.
Iso-C3H7 + CH3O --> i-C3H7OCH3

pg 895, Chemical Kinetic Database For Combustion Chemistry, Part 3. Index of Reactions and Summary of Recommended Rate Expressions. No. 42,24.

Verified by Karma James

pg. 943: Discussion on evaluated data

Entry 42,24 (b): No data available at the time.  Author recommends rate coefficient

based on CH3+CH3O-->adduct.
MRH 30-Aug-2009
""",
)

entry(
    index = 460,
    label = "C_rad/Cs3;C_rad/Cs3",
    kinetics = ArrheniusEP(
        A = (1.24e+16, 'cm^3/(mol*s)', '*|/', 2),
        n = -1.5,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Tsang [92] literature review.""",
    longDesc = 
u"""
[92] Tsang, W. J Phys. Chem. Ref. Data 1990, 19, 1.
Tert-C4H9 + tert- C4H9 --> (CH3)3CC(CH3)3

//DOES NOT MATCH! Reference: A = 2.4E+12, E0 = 0, n = -1.5, Database: A = 1.24E+16, E0 = 0, n = -1.5

//pg 8, Chemical Kinetic Database For Combustion Chemistry, Part 4 - Isobutane. 

//Index of Reactions and Summary of Recommended Rate Expressions. No. 44,44.

//Verified by Karma James

pg. 47

Data reported as ka = 4e-12 * (300/T)^1.5

When lumping the 4e-12 * 300^1.5, attain A=1.25e+16
Recommended data taken from expression computed by Parkes, Quinn (1976)

Verified by MRH on 10Aug2009

Entry 44,44(a)

MRH 31-Aug-2009
""",
)

entry(
    index = 461,
    label = "C_rad/Cs3;CO_pri_rad",
    kinetics = ArrheniusEP(
        A = (1.21e+13, 'cm^3/(mol*s)', '*|/', 5),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Tsang [92] literature review.""",
    longDesc = 
u"""
[92] Tsang, W. J Phys. Chem. Ref. Data 1990, 19, 1.
Tert-C4H9 + HCO --> tert-C4H9CHO

pg 7, Chemical Kinetic Database For Combustion Chemistry, Part 4 - Isobutane. 

Index of Reactions and Summary of Recommended Rate Expressions. No. 44,15.

Verified by Karma James

pg.36: Discussion on evaluated data

Entry 44,15(b): No data available at the time.  Recommended rate coefficient is based

on rate of rxn tC4H9+CH3-->adduct, but "slightly smaller"
MRH 31-Aug-2009
""",
)

entry(
    index = 462,
    label = "C_rad/Cs3;CO_rad/NonDe",
    kinetics = ArrheniusEP(
        A = (7.75e+14, 'cm^3/(mol*s)', '*|/', 2),
        n = -0.75,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Tsang [92] literature review.""",
    longDesc = 
u"""
[92] Tsang, W. J Phys. Chem. Ref. Data 1990, 19, 1.
Tert-C4H9 + CH3CO --> tert-C4H9COCH3

//DOES NOT MATCH! Reference: A = 1.08E+13, E0 = 0, n = -0.75, Database: A = 7.75E+14, E0 = 0, n = -0.75

//pg 7, Chemical Kinetic Database For Combustion Chemistry, Part 4 - Isobutane. 

//Index of Reactions and Summary of Recommended Rate Expressions. No. 44,22.

//Verified by Karma James

pg. 42

Data reported as k = 1.8e-11 * (300/T)^0.75

When lumping the 1.8e-11 * 300^0.75, attain A=7.81e+14
No experimental data, at the time

Verified by MRH on 10Aug2009

Entry 44,22: Recommended rate coefficient computed using geometric mean rule of

tC4H9+tC4H9-->adduct and CH3CO+CH3CO-->adduct rxns
MRH 31-Aug-2009
""",
)

entry(
    index = 463,
    label = "C_rad/Cs3;O_rad/NonDe",
    kinetics = ArrheniusEP(
        A = (9.04e+12, 'cm^3/(mol*s)', '*|/', 3),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Tsang [92] literature review.""",
    longDesc = 
u"""
[92] Tsang, W. J Phys. Chem. Ref. Data 1990, 19, 1.
Tert-C4H9 + CH3O --> tert-C4H9OCH3

pg 8, Chemical Kinetic Database For Combustion Chemistry, Part 4 - Isobutane. 

Index of Reactions and Summary of Recommended Rate Expressions. No. 44,24.

Verified by Karma James

pg.42-43: Discussion on evaluated data

Entry 44,24(b): Rate coefficient calculated using geometric mean rule of tC4H9+tC4H9-->adduct

and CH3O+CH3O-->adduct rxns
MRH 31-Aug-2009
""",
)

entry(
    index = 464,
    label = "Cd_pri_rad;Cd_pri_rad",
    kinetics = ArrheniusEP(
        A = (7.23e+13, 'cm^3/(mol*s)', '+|-', 1.2e+13),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (298, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Fahr et al. [171]""",
    longDesc = 
u"""
[171] Fahr, A.; Laufer, A.; Klein, R.; Braun, W. J. Phys. Chem. 1991, 95, 3218.
Absolute value measured directly. Excitation: flash photolysis, analysis : Vis-UV absorption. Original Uncertainty 1.2E+13. 

C2H3 + C2H3 --> (E)-CH2=CHCH=CH2 (Rxn. IIC)

Verified by Greg Magoon; DA uncertainty updated, as I have done elsewhere; based on Eqs. 3, 6, it looks like a factor of two correction is not needed
""",
)

entry(
    index = 465,
    label = "Cd_pri_rad;Ct_rad/Ct",
    kinetics = ArrheniusEP(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (700, 'K'),
        Tmax = (1300, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Duran et al. [165]""",
    longDesc = 
u"""
[165] Duran, R. P.; Amorebieta, V. T.; Colussi, A. J. J. Phys. Chem. 1988, 92, 636.
Ab initio. Pressure 0.10-1.0 atm. 

C2H3 +.C2H --> CH2=CHC=CH (Rxn. 25)

NIST record: http://kinetics.nist.gov/kinetics/Detail?id=1988DUR/AMO636:4
Verified by Greg Magoon; value confirmed from paper data in Table III; this is presumably high-pressure limit since no pressure-dependence is indicated in the table
""",
)

entry(
    index = 466,
    label = "Cd_pri_rad;CO_pri_rad",
    kinetics = ArrheniusEP(
        A = (1.81e+13, 'cm^3/(mol*s)', '*|/', 3),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R. F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
C2H3 + HCO --> CH2=CHCHO

pg 1099, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 19,15.

Verified by Karma James

pg. 1199: Discussion on evaluated data

Recommended data based on rate expression for CH3+HCO-->CH3CHO

Authors note that rate expression will be in fall-off region at high temperatures
MRH 28-Aug-2009
""",
)

entry(
    index = 467,
    label = "Cb_rad;Cb_rad",
    kinetics = ArrheniusEP(
        A = (5.7e+12, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (1100, 'K'),
        Tmax = (1400, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Heckmann et al. [124]""",
    longDesc = 
u"""
[124] Heckmann, E.; Hippler, H.; Troe, J. Symp. Int. Combust. Proc.1996, 26, 543.
Absolute value measured directly. Excitation : thermal, analysis : Vis-UV absorption. 

Phenyl + Phenyl --> Biphenyl
""",
)

entry(
    index = 468,
    label = "Cb_rad;Cb_rad",
    kinetics = ArrheniusEP(
        A = (1.39e+13, 'cm^3/(mol*s)', '+|-', 1.1e+12),
        n = 0,
        alpha = 0,
        E0 = (0.11, 'kcal/mol', '+|-', 0.072),
        Tmin = (300, 'K'),
        Tmax = (500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Park et al. [181]""",
    longDesc = 
u"""
[181] Park, J. ; Lin, M. C. J. Phys. Chem. A. 1997, 101, 14
Absolute value measured directly. Excitation : flash photolysis, analysis : mass spectometry. Original Uncertainty 1.1E+12.   

phenyl + phenyl --> biphenyl (Reaction 1)

***NHP***
Verified by Greg Magoon: total pressure ~7 torr; DA uncertainty changed to additive, as reported in paper, and DE0 uncertainty was refined
""",
)

entry(
    index = 469,
    label = "CO_pri_rad;CO_pri_rad",
    kinetics = ArrheniusEP(
        A = (1.51e+13, 'cm^3/(mol*s)', '+|-', 6.02e+12),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (298, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Stoeckel et al. [182]""",
    longDesc = 
u"""
[182] Stoeckel, F.; Schuh, M. D.; Goldstein, N.; Atkinson, G.H. Chem. Phys. 1985, 95, 135
Absolute value measured directly. Excitation : flash photolysis, abalysis : VIS-UV absorption. Original uncertainty 1.2E+13. Pressure: 10 Torr (this is total pressure; see p. 141)

HCO + HCO --> (CHO)2 

***NHP***
Verified by Greg Magoon: the existing k in the rateLibrary appeared to be off by a factor of two, since the paper uses d[HCO]/dt=-k*[HCO]^2; they report k=(5+/-2)*10^-11 molecules^-1*cm^3/s (references 9, 19, and 20 in this paper could have better data); I think in rateLibrary, we should have half of this (2.5 +/- 1), so I have changed the value in the rateLibrary accordingly (with 2nd opinion to confirm from MRH)
""",
)

entry(
    index = 470,
    label = "CO_pri_rad;CO_rad/NonDe",
    kinetics = ArrheniusEP(
        A = (1.81e+13, 'cm^3/(mol*s)', '*|/', 3),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R. F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
HCO + CH3CO --> CH3COCHO

pg 1102, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 22,15.

Verified by Karma James

pg. 1232: Discussion on evaluated data

Recommended data is assigned a value of 3x10^-11 cm3/molecule*s (This appears to be

the default value the authors assign for recombination rxns)
MRH 28-Aug-2009
""",
)

entry(
    index = 471,
    label = "CO_rad/NonDe;CO_rad/NonDe",
    kinetics = ArrheniusEP(
        A = (1.21e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R. F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
CH3CO + CH3CO --> (CH3CO)2

pg 1103, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 22,22.

Verified by Karma James

pg. 1234-1235: Discussion on evaluated data

Recommended data is assigned based on 5 reported direct measurements of rate coefficient

MRH 28-Aug-2009
""",
)

entry(
    index = 472,
    label = "O_pri_rad;O_pri_rad",
    kinetics = ArrheniusEP(
        A = (1.57e+13, 'cm^3/(mol*s)', '+|-', 6.02e+12),
        n = (0, '', '+|-', 0.5),
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (400, 'K'),
    ),
    rank = 4,
    shortDesc = u"""DeMore et al. [183] literature review.""",
    longDesc = 
u"""
[183] DeMore, W. B.; Sander, S. P.; Golden, D. M.; Hampson, R. F.; Kurylo, M.J.; 
Howard, C. J.; Ravishankara, A. R.; Kolb, C. E.; Molina, M .J. JPL publication 97-4 1997, 1.

(Rate constant is high pressure limit, original uncertainty 6.0E+12) 

[97] Atkinson, R.; Baulch, D. L.; Cox, R. A.; Hampson, R. F., jr.; Kerr, J. A.; Rossi, M. J.; Troe, J. 

J. Phys. Chem. Ref. Data 1997, 26, 1329

OH + OH --> H2O2

Literature review: OH + OH (+m) --> H2OH

pg.126: Recommended low-pressure and high-pressure limit rate coefficient

pg.130 B2: Discussion on evaluated data.

Authors recommend the fits by Zellner et al. in N2 and by Forster et al.
in 1-150kbar He scaled to N2.  RMG stores the high-pressure limit (k_inf)
rate coefficient.
*** High-pressure rate coefficient. ***

MRH 1-Sept-2009
""",
)

entry(
    index = 473,
    label = "O_rad/NonDe;O_rad/NonDe",
    kinetics = ArrheniusEP(
        A = (1.81e+12, 'cm^3/(mol*s)', '*|/', 5),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R. F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
CH3O + CH3O --> CH3OOCH3

pg 1105, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 24,24.

Verified by Karma James

pg. 1251: Discussion on evaluated data (in theory)

Online reference does not contain pg. 1251.  The following discussion is based
on the information provided in the table on pg. 1105
Entry 24,24 (b)

MRH 28-Aug-2009
""",
)

entry(
    index = 474,
    label = "H_rad;Cs_rad",
    kinetics = ArrheniusEP(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran's [8] estimation.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253. 
Curran's estimation, based on half that recommended by Allara and Shaw [146] for H (rad) and R (rad) recombination reactions
""",
)

entry(
    index = 475,
    label = "C_methyl;C_ter_rad",
    kinetics = ArrheniusEP(
        A = (1.63e+13, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0.596, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran's [8] estimation.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimation, based on recommendations of Tsang [92] for CH3 + tC4H9
""",
)

entry(
    index = 476,
    label = "C_methyl;C_sec_rad",
    kinetics = ArrheniusEP(
        A = (6.8e+14, 'cm^3/(mol*s)'),
        n = -0.68,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran's [8] estimation.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimation based on half Tsang's [91] recommendation for CH3 + iC3H7
""",
)

entry(
    index = 477,
    label = "C_pri_rad;C_sec_rad",
    kinetics = ArrheniusEP(
        A = (4.79e+14, 'cm^3/(mol*s)'),
        n = -0.75,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran's [8] estimation.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimation for neoC5H11 + iC3H7, similar to tC4H9 + iC4H9
""",
)

entry(
    index = 478,
    label = "C_pri_rad;C_ter_rad",
    kinetics = ArrheniusEP(
        A = (3.59e+14, 'cm^3/(mol*s)'),
        n = -0.75,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran's [8] estimation.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimation based on Tsang's [92] reccomendation for tC4H9 Curran's estimation. About a factor of 2 slower than other 

values from literature for smaller alkyl, based upon the consideration that rate constants decrease with the increasing size of R radical.
""",
)

entry(
    index = 479,
    label = "O_pri_rad;O_sec_rad",
    kinetics = ArrheniusEP(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran's [159] estimation.""",
    longDesc = 
u"""
[159] Curran, H.J.; Pitz, W.J.; Westbrook, C.K.; Dagaut, P.; Boettner, J.-C.; Cathonnet, M. Int. J. Chem. Kinet. 1998, 30, 229.
Curran's estimation in DME modeling for ketohydroperoxide decomposition 

Apparently the number comes from estimate for reverse of Rxn. 337: HO2CH2OCHO -> .OCH2OCHO + .OH (2E13) (p. 234); reverse of Rxn. 191 (p. 238) would also be informative, but it doesn't seem to be disucussed in paper
Verified by Greg Magoon; it is not immediately clear whether this rate constant is for high pressure limit, but based on other references to high pressure limit in the paper, I suspect that it is a high pressure limit value

*NHP = Not necessarily at high pressure limit
""",
)

entry(
    index = 480,
    label = "O2_birad;H_rad",
    kinetics = ArrheniusEP(
        A = (4.395e+10, 'cm^3/(mol*s)'),
        n = 1,
        alpha = 0,
        E0 = (0.45, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Duchovic et al. [142] RRK(M) extrapolation. Probably could do better.""",
    longDesc = 
u"""
[142] Duchovic,R.J; Pettigrew,J D; Welling B; Shipchandler,T. *J. Chem Phys.* **105**, 10367 (1996) http://dx.doi.org/10.1063/1.472992

RRK(M) extrapolation. H + O2 --> OH + O

C.D.W. divided rate expression by 2, to get rate of addition per site.

Values (4.395E+10	1.00	0	0.45) confirmed to fit table (divided by 2) 
by rwest@mit.edu  7-Sep-2009

Agreement with experimental data from Cobos et al. 
(C. J. Cobos, H. Hippler, and J. Troe, *J. Phys. Chem.* 89, 342, 1985)
was promising **at low pressures**, but 
"Significant deviations are observed between theory and experiment as the 
high-pressure limit is approached."
    
E.g., at 298 K

    "However, the value of 
    the high-pressure limit rate coefficient at 298.15 K for the
    termolecular process computed with TST, model I, and 
    model II does not agree with the estimated high-pressure 
    limit value of Cobos et al. at that temperature. TST, 
    model I, and model II agree with one another, predicting a 
    value of Log10(k)=-10.7 where the value of the limiting 
    high-pressure rate coefficient k=2E-11 cm3/molecule/s at 298.15 K, 
    while Cobos et al. estimate a value of Log10(k)=-10.12 
    (that is, k=7.5E-11 cm3/molecule/s)"
    
The calculations used the *ab initio* PES of Walch et al., which was the best available in 1991.
(63) Walch, S. P.; Rohlfing, C. M.; Melius, C. F.; Bauschlicher, C. W. J. Chem. Phys. 1988, 88, 6273. 
(64) Walch, S. P.; Rohlfing, C. M. J. Chem. Phys. 1989, 91, 2373. 
(67) Walch, S. P.; Duchovic, R. J. J. Chem. Phys. 1991, 94, 7068. 

Many extensions and improvements are suggested for future work, which may well 
have happened since the paper was published in 1996. Revision of this rate is recommended.

Moved from R_Addition_MultipleBond on 3-Jun-2010, JDM.
""",
)

entry(
    index = 480,
    label = "SsJ-Ss;C_methyl",
    kinetics = ArrheniusEP(
        A = (3.94e+09, 'cm^3/(mol*s)'),
        n = 1.25,
        alpha = 0,
        E0 = (-0.74, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""A.G. Vandeputte""",
    longDesc = 
u"""
""",
)

entry(
    index = 481,
    label = "SsJ-Cs;SsJ-Cs",
    kinetics = ArrheniusEP(
        A = (1.06e+11, 'cm^3/(mol*s)'),
        n = 1.21,
        alpha = 0,
        E0 = (-0.95, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""A.G. Vandeputte""",
    longDesc = 
u"""
""",
)

entry(
    index = 482,
    label = "CsJ-SsHH;H_rad",
    kinetics = ArrheniusEP(
        A = (5e+11, 'cm^3/(mol*s)'),
        n = 0.65,
        alpha = 0,
        E0 = (-0.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""A.G. Vandeputte""",
    longDesc = 
u"""
""",
)

entry(
    index = 483,
    label = "SsJ-H;H_rad",
    kinetics = ArrheniusEP(
        A = (7.07e+12, 'cm^3/(mol*s)'),
        n = 0.56,
        alpha = 0,
        E0 = (-0.08, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""A.G. Vandeputte""",
    longDesc = 
u"""
""",
)

entry(
    index = 484,
    label = "SsJ-Ss;C_rad/Cs3",
    kinetics = ArrheniusEP(
        A = (3.94e+09, 'cm^3/(mol*s)'),
        n = 1.25,
        alpha = 0,
        E0 = (-0.74, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""A.G. Vandeputte""",
    longDesc = 
u"""
""",
)

entry(
    index = 485,
    label = "SsJ-Cs;C_rad/H2/Cs",
    kinetics = ArrheniusEP(
        A = (8.94e+07, 'cm^3/(mol*s)'),
        n = 1.54,
        alpha = 0,
        E0 = (-1.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""A.G. Vandeputte, calculated""",
)

entry(
    index = 486,
    label = "SsJ-Cs;C_methyl",
    kinetics = ArrheniusEP(
        A = (8.94e+07, 'cm^3/(mol*s)'),
        n = 1.54,
        alpha = 0,
        E0 = (-1.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""A.G. Vandeputte, calculated""",
)

entry(
    index = 487,
    label = "SsJ-Cs;C_rad/Cs3",
    kinetics = ArrheniusEP(
        A = (8.94e+07, 'cm^3/(mol*s)'),
        n = 1.54,
        alpha = 0,
        E0 = (-1.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""A.G. Vandeputte, calculated""",
)

entry(
    index = 481,
    label = "O2_birad;H_rad",
    kinetics = ArrheniusEP(
        A = (8.15e+12, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Cobos, C.J and Troe, J. [106] Transition state theory.""",
    longDesc = 
u"""
[106] Cobos,C.J.;Troe,J.J. Chem. Phys 1985, 83,1010.

Transition state theory. H+O2 -->HO2 

C.D.W. divided rate expression by 2, to get rate of addition per site 

Moved from R_Addition_MultipleBond on 3-Jun-2010, JDM.
""",
)

entry(
    index = 482,
    label = "O2_birad;C_methyl",
    kinetics = ArrheniusEP(
        A = (2.26e+12, 'cm^3/(mol*s)', '+|-', 4.2e+11),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran et al. [8] From Lenhardt et al. [143]. (Measured at 300K) (n-butyl not methyl)""",
    longDesc = 
u"""
We are using a primary R. radical as a methyl radical. The rate comes from n-butyl.

[8]   Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. *Combust. Flame* 2002, 129, 253-280. http://dx.doi.org/10.1016/S0010-2180(01)00373-X

In their study modelling iso-octane oxidation, Curran et al [8] chose to use the rate measured by Lenhardt et al [143] described below.

[143] Lenhardt, T.M.; McDade, C.E.; Bayes, K.D.; *J. Chem. Phys.* 1980, 72,304 http://dx.doi.org/10.1063/1.438848

Rates measurement of **n-butyl** + O2 at 300 K. High pressure limit from flash photolysis experiments.

C.D.W. divided rate expression by 2, to get rate of addition rate per site,
giving  (2.260.42)E12 cm3/mole/sec.

    Rate constants for the reaction of four different butyl radicals with molecular oxygen 
    have been measured **at room temperature**. The radicals were generated by flash photolysis 
    and their time decay was followed with a photoionization mass spectrometer. The radical 
    concentrations were kept low to avoid complications from radicalradical reactions. 
    Radical lifetimes were long, up to 50 msec, thus assuring that thermalized radicals were being studied. 
    
    The rate constants, in units of 10E11 cm3/molecule/sec, are:
    
     * **n-butyl (0.750.14); (gives (2.260.42)E12 cm3/mole/sec when divided by 2 to get rate per site)**
     * s-butyl (1.660.22); (gives (5.000.66)E12 cm3/mole/sec when divided by 2 to get rate per site)
     * t-butyl (2.340.39); (gives (7.051.17)E12 cm3/mole/sec when divided by 2 to get rate per site)
     * 3-hydroxy s-butyl (2.81.8). (gives (8.435.42)E12 cm3/mole/sec when divided by 2 to get rate per site)
     
    No pressure dependence of the rate constants was observed over the range 1 to 4 Torr. 

Because radical addition to a double bond is probably barrierless, the temperature range 300-1500K
has been assigned although the rate was only measured at 300K. 
rwest@mit.edu  7-Sep-2009

Moved from R_Addition_MultipleBond on 3-Jun-2010, JDM.
""",
)

entry(
    index = 483,
    label = "O2_birad;C_pri_rad",
    kinetics = ArrheniusEP(
        A = (2.26e+12, 'cm^3/(mol*s)', '+|-', 4.2e+11),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran et al. [8] From Lenhardt et al. [143]. (Measured at 300K)""",
    longDesc = 
u"""
[8]   Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. *Combust. Flame* 2002, 129, 253-280. http://dx.doi.org/10.1016/S0010-2180(01)00373-X

In their study modelling iso-octane oxidation, Curran et al [8] chose to use the rate measured by Lenhardt et al [143] described below.

[143] Lenhardt, T.M.; McDade, C.E.; Bayes, K.D.; *J. Chem. Phys.* 1980, 72,304 http://dx.doi.org/10.1063/1.438848

Rates measurement of **n-butyl** + O2 at 300 K. High pressure limit from flash photolysis experiments.
C.D.W. divided rate expression by 2, to get rate of addition rate per site, 
giving  (2.260.42)E12 cm3/mole/sec.

    Rate constants for the reaction of four different butyl radicals with molecular oxygen 
    have been measured **at room temperature**. The radicals were generated by flash photolysis 
    and their time decay was followed with a photoionization mass spectrometer. The radical 
    concentrations were kept low to avoid complications from radicalradical reactions. 
    Radical lifetimes were long, up to 50 msec, thus assuring that thermalized radicals were being studied. 
    
    The rate constants, in units of 10E11 cm3/molecule/sec, are:
    
     * n-butyl (0.750.14); (gives (2.260.42)E12 cm3/mole/sec when divided by 2 to get rate per site)
     * s-butyl (1.660.22); (gives (5.000.66)E12 cm3/mole/sec when divided by 2 to get rate per site)
     * t-butyl (2.340.39); (gives (7.051.17)E12 cm3/mole/sec when divided by 2 to get rate per site)
     * 3-hydroxy s-butyl (2.81.8). (gives (8.435.42)E12 cm3/mole/sec when divided by 2 to get rate per site)
     
    No pressure dependence of the rate constants was observed over the range 1 to 4 Torr. 

Because radical addition to a double bond is probably barrierless, the temperature range 300-1500K
has been assigned although the rate was only measured at 300K. 

rwest@mit.edu  7-Sep-2009

Moved from R_Addition_MultipleBond on 3-Jun-2010, JDM.
""",
)

entry(
    index = 484,
    label = "O2_birad;C_sec_rad",
    kinetics = ArrheniusEP(
        A = (3.77e+12, 'cm^3/(mol*s)', '+|-', 1e+12),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran et al. [8]. (Estimated at 300K)""",
    longDesc = 
u"""
Lenhardt [143] measured (10.01.3)E12 cm3/mole/sec (at 300K, high pressure limit, from flash photolysis experiments.)
Atkinson [96], in their review, recommend 6.62E12 cm3/mole/sec. (according to Curran [8]).
Curran [8], in their modelling paper, refer to both these and chose and "intermediate" value of 7.54E12 cm3/mol/sec.

Curran [8] is the rate adopted here, giving 3.77E+12 cm3/mole/sec when divided by two to give the rate of addition per site.
The uncertainty of 1E12 cm3/mole/sec was estimated from these values

 * [8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. *Combust. Flame* 2002, 129, 253-280. http://dx.doi.org/10.1016/S0010-2180(01)00373-X
 * [96] Atkinson,R; Baulch,D. L.; Cox R.A.;Hampson,R.F.,Jr.;Kerr,J.A;Rossi,M.J.;Troe,J. *J Phys. Chem. Ref. Data* 1997,26,521.
 * [143] Lenhardt,T.M.;McDade,C.E.;Bayes,K.D.; *J. Chem Phys* 1980, 72,304 http://dx.doi.org/10.1063/1.438848

Because radical addition to a double bond is probably barrierless, the temperature range 300-1500K
has been assigned although the rate was only measured/estimated at 300K. 

rwest@mit.edu  7-Sep-2009

Moved from R_Addition_MultipleBond on 3-Jun-2010, JDM.
""",
)

entry(
    index = 485,
    label = "O2_birad;C_ter_rad",
    kinetics = ArrheniusEP(
        A = (7.05e+12, 'cm^3/(mol*s)', '+|-', 1.17e+12),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran et al. [8] From Lenhardt et al. [143]. (Measured at 300K)""",
    longDesc = 
u"""
[8]   Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. *Combust. Flame* 2002, 129, 253-280. http://dx.doi.org/10.1016/S0010-2180(01)00373-X

In their study modelling iso-octane oxidation, Curran et al [8] chose to use the rate measured by Lenhardt et al [143] described below.

[143] Lenhardt, T.M.; McDade, C.E.; Bayes, K.D.; *J. Chem. Phys.* 1980, 72,304 http://dx.doi.org/10.1063/1.438848

Rates measurement of **t-butyl** + O2 at 300 K. High pressure limit from flash photolysis experiments.
C.D.W. divided rate expression by 2, to get rate of addition rate per site, 
giving  (7.051.17)E12 cm3/mole/sec.

    Rate constants for the reaction of four different butyl radicals with molecular oxygen 
    have been measured **at room temperature**. The radicals were generated by flash photolysis 
    and their time decay was followed with a photoionization mass spectrometer. The radical 
    concentrations were kept low to avoid complications from radicalradical reactions. 
    Radical lifetimes were long, up to 50 msec, thus assuring that thermalized radicals were being studied. 
    
    The rate constants, in units of 10E11 cm3/molecule/sec, are:
    
     * n-butyl (0.750.14); (gives (2.260.42)E12 cm3/mole/sec when divided by 2 to get rate per site)
     * s-butyl (1.660.22); (gives (5.000.66)E12 cm3/mole/sec when divided by 2 to get rate per site)
     * **t-butyl (2.340.39); (gives (7.051.17)E12 cm3/mole/sec when divided by 2 to get rate per site)**
     * 3-hydroxy s-butyl (2.81.8). (gives (8.435.42)E12 cm3/mole/sec when divided by 2 to get rate per site)
     
    No pressure dependence of the rate constants was observed over the range 1 to 4 Torr. 

Because radical addition to a double bond is probably barrierless, the temperature range 300-1500K
has been assigned although the rate was only measured at 300K. 

rwest@mit.edu  7-Sep-2009

Moved from R_Addition_MultipleBond on 3-Jun-2010, JDM.
""",
)

entry(
    index = 486,
    label = "O2_birad;Cd_pri_rad",
    kinetics = ArrheniusEP(
        A = (3e+12, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Bozzelli et al. [144] RRKM extrapolation ( adjusted to match data).""",
    longDesc = 
u"""
[144] Bozzelli,J.W. J phys. Chem 1993, 97,4427.
RRKM extrapolation (adjusted to match data).O2 +CH = CH2CHOO. C.D.W. divided rate expression by 2, to get rate of addition per site

Moved from R_Addition_MultipleBond on 3-Jun-2010, JDM.
""",
)

entry(
    index = 488,
    label = "O2_birad;Cb_rad",
    kinetics = ArrheniusEP(
        A = (3.015e+12, 'cm^3/(mol*s)', '*|/', 1.2),
        n = 0,
        alpha = 0,
        E0 = (0.32, 'kcal/mol', '+|-', 0.13),
        Tmin = (297, 'K'),
        Tmax = (473, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Yu, T. and Lin, M.C. [145]""",
    longDesc = 
u"""
[145] Yu,T.; Lin, M.C.J. Am. Chem.Soc.1994,116,9571.
O2+ phenyl --> phenyl dioxy. Absolute value measured directly. Pressure 0.03-0.11 atm. Excitation: Flash photolysis, analysis: Vis- UV absorption. C.D.W. divided rate epxression by 2, to get rate of addition per site

Moved from R_Addition_MultipleBond on 3-Jun-2010, JDM.
""",
)

entry(
    index = 489,
    label = "O2_birad;CO_pri_rad",
    kinetics = ArrheniusEP(
        A = (3.5e+12, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Bozzelli et al. [144] RRKM extrapolation.""",
    longDesc = 
u"""
[144] Bozzelli,J.W. J Phys. Chem. 1993, 97 , 4427.
RRKM extrapolation. O2 +HCO -->HC(O)O2. C.D.W. divided rate expression by 2, to get rate of addition per site

Moved from R_Addition_MultipleBond on 3-Jun-2010, JDM.
""",
)

entry(
    index = 490,
    label = "O2_birad;CO_rad/NonDe",
    kinetics = ArrheniusEP(
        A = (1.505e+12, 'cm^3/(mol*s)', '*|/', 3.16),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (300, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Atkinson et al [96] literature review.""",
    longDesc = 
u"""
[96] Atkinson,R; Baulch,D. L.; Cox R.A.;Hampson,R.F.,Jr.;Kerr,J.A;Rossi,M.J.;Troe,J.J Phys. Chem. Ref. Data 1997,26,521.
literature review. Rate constant is high pressure limit. O2+ CH3CO --> CH3C(O)OO C.D.W. divided rate expression by 2, to get rate of addition per site

Moved from R_Addition_MultipleBond on 3-Jun-2010, JDM.
""",
)

entry(
    index = 491,
    label = "SsJ-Ss;C_methyl",
    kinetics = ArrheniusEP(
        A = (6.44e+09, 'cm^3/(mol*s)'),
        n = 1.19,
        alpha = 0,
        E0 = (0.51, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""A.G. Vandeputte""",
    longDesc = 
u"""
""",
)

entry(
    index = 495,
    label = "H_rad;C_rad/H2/Cd",
    kinetics = ArrheniusEP(
        A = (2.92e+13, 'cm^3/(mol*s)'),
        n = 0.18,
        alpha = 0,
        E0 = (0.124, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Harding et al. (2007HAR/KLI3789-3801), value devided by 2 to account for two addition sites""",
)

entry(
    index = 496,
    label = "H_rad;C_rad/H/OneDeC",
    kinetics = ArrheniusEP(
        A = (2.92e+13, 'cm^3/(mol*s)'),
        n = 0.18,
        alpha = 0,
        E0 = (0.124, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Estimated by 495""",
)

entry(
    index = 497,
    label = "H_rad;C_rad/OneDe",
    kinetics = ArrheniusEP(
        A = (2.92e+13, 'cm^3/(mol*s)'),
        n = 0.18,
        alpha = 0,
        E0 = (0.124, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Estimated by 495""",
)

entry(
    index = 498,
    label = "H_rad;C_rad/TwoDe",
    kinetics = ArrheniusEP(
        A = (2.92e+13, 'cm^3/(mol*s)'),
        n = 0.18,
        alpha = 0,
        E0 = (0.124, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Estimated by 495""",
)

entry(
    index = 499,
    label = "C_rad/H2/Cd;C_rad/H2/Cd",
    kinetics = ArrheniusEP(
        A = (1.02e+13, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (-0.26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Tsang (1991) Chemical kinetic data base for combustion chemistry. Part V. Propene Literature review""",
)

entry(
    index = 500,
    label = "C_rad/H2/Cd;C_rad/H2/Cs",
    kinetics = ArrheniusEP(
        A = (2.05e+13, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (-0.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Tsang (1991) Chemical kinetic data base for combustion chemistry. Part V. Propene Literature review""",
)

entry(
    index = 501,
    label = "C_rad/H2/Cd;C_methyl",
    kinetics = ArrheniusEP(
        A = (1.02e+14, 'cm^3/(mol*s)'),
        n = -0.32,
        alpha = 0,
        E0 = (-0.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Tsang (1991) Chemical kinetic data base for combustion chemistry. Part V. Propene Literature review""",
)

entry(
    index = 502,
    label = "C_rad/H2/Cd;C_rad/H/NonDeC",
    kinetics = ArrheniusEP(
        A = (1.15e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        alpha = 0,
        E0 = (-0.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Tsang (1991) Chemical kinetic data base for combustion chemistry. Part V. Propene Literature review""",
)

entry(
    index = 503,
    label = "C_rad/H2/Cd;C_rad/Cs3",
    kinetics = ArrheniusEP(
        A = (7.24e+14, 'cm^3/(mol*s)'),
        n = -0.75,
        alpha = 0,
        E0 = (-0.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Tsang (1991) Chemical kinetic data base for combustion chemistry. Part V. Propene Literature review""",
)

entry(
    index = 504,
    label = "C_rad/H2/Cd;C_rad/H/CdCd",
    kinetics = ArrheniusEP(
        A = (1.02e+13, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (-0.26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Better estimate then averaging out, Tsang (1991) Chemical kinetic data base for combustion chemistry. Part V. Propene Literature review""",
)

entry(
    index = 505,
    label = "Cd_allenic;Cd_allenic",
    kinetics = ArrheniusEP(
        A = (4.29E+9, 'cm^3/(mol*s)'),
        n = 0.8,
        alpha = 0,
        E0 = (-1.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""2007GEO/MIL4259-4268""",
    longDesc = """
A. G. Vandeputte
Some estimated values for propyne recombination reactions
""",
)

entry(
    index = 506,
    label = "Cd_allenic;C_methyl",
    kinetics = ArrheniusEP(
        A = (5.00E+12, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""1987WU/KER6291""",
    longDesc = """
Estimated value, agrees with 1987WU/KER6291
""",
)

entry(
    index = 507,
    label = "Cd_allenic;H_rad",
    kinetics = ArrheniusEP(
        A = (1.00E+13, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""A. G. Vandeputte estimated value""",
)

# entry(
#     index = 508,
#     label = "C_rad_cyclopentadiene;H_rad",
#     kinetics = ArrheniusEP(
#         A = (1.00E+14, 'cm^3/(mol*s)'),
#         n = 0,
#         alpha = 0,
#         E0 = (0, 'kcal/mol'),
#         Tmin = (300, 'K'),
#         Tmax = (2000, 'K'),
#     ),
#     rank = 3,
#     shortDesc = u"""BENZENE OXIDATION TAKEN FROM DACOSTA 2003 IJCK""",
# )

entry(
    index = 508,
    label = "C_rad_cyclopentadiene;H_rad",
    kinetics = ArrheniusEP(
        A = (5.00E+14, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""From 2001 Roy IJCK high-P value""",
)

entry(
    index = 509,
    label = "C_rad_cyclopentadiene;C_methyl",
    kinetics = ArrheniusEP(
        A = (8.34E+15, 'cm^3/(mol*s)'),
        n = -0.7,
        alpha = 0,
        E0 = (0.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Sharma J. Phys. Chem. A 113 8871 - 8882 (2009)""",
)

entry(
    index = 510,
    label = "C_rad_cyclopentadiene;C_rad_cyclopentadiene",
    kinetics = ArrheniusEP(
        A = (5.00E+13, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""A. G. Vandeputte estimated value""",
)

entry(
    index = 511,
    label = "H_rad;C_rad/H/CdCd",
    kinetics = ArrheniusEP(
        A = (2.00E+13, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""A. G. Vandeputte estimated value""",
)

entry(
    index = 600,
    label = "N5d-OdOs;O_rad",
    kinetics = ArrheniusEP(
        A = (3.5e+12, 'cm^3/(mol*s)'),
        n = 0.24,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Experimental, J. Hahn, K. Luther and J. Troe""",
    longDesc = 
u"""
J. Hahn, K. Luther and J. Troe
Experimental and theoretical study of the temperature and pressure dependences of the recombination reactions O + NO2(+M) → NO3(+M) and NO2 + NO3(+M) → N2O5(+M)
Phys. Chem. Chem. Phys., 2000, 2, 5098-5104
DOI: 10.1039/B005756H

NO2 + O <=> NO3

Also appears in the Nitrogen_Glarborg_Zhang_et_al library (index 712)
and in the Nitrogen_Glarborg_Gimenez_et_al library (index 936)

The high-pressure limit kinetics was taken. Troe coefficients are:
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.5e+12, 'cm^3/(mol*s)'), n=0.24, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(2.5e+20, 'cm^6/(mol^2*s)'), n=-1.5, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.71,
        T3 = (1e-30, 'K'),
        T1 = (1700, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {},
    ),
""",
)

entry(
    index = 601,
    label = "N5d-OdOs;O_pri_rad",
    kinetics = ArrheniusEP(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""J. Troe""",
    longDesc = 
u"""
J. Troe
Analysis of the temperature and pressure dependence of the reaction HO + NO2 + M ⇔ HONO2 + M
International Journal of Chemical Kinetics, Volume 33, Issue 12 December 2001 Pages 878–889
DOI: 10.1002/kin.10019

NO2 + OH <=> HONO2; T range: 50 to 1400 K, P range: 10E-4 to 10E3 bar

Also appears in the Nitrogen_Glarborg_Zhang_et_al library (index 713)
and in the Nitrogen_Glarborg_Gimenez_et_al library (index 937)

The high-pressure limit kinetics was taken. Troe coefficients are:
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(2.938e+25, 'cm^6/(mol^2*s)'), n=-3, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.4,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {},
    ),
""",
)

entry(
    index = 3000,
    label = "H_rad;SsJ-H",
    kinetics = ArrheniusEP(
        A = (5.77e+15, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0.43, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""GA Jonas x 3 for spinorbit""",
)

