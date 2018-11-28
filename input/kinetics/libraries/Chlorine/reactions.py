#!/usr/bin/env python
# encoding: utf-8

name = "Chlorine"
shortDesc = u"Reactions of Chlorine Containting Species"
longDesc = u"""
Compilation of reactions involving Cl containing species mostly from
Wang, H., Hahn, T. O., Sung, C. J., & Law, C. K. (1996).
Detailed oxidation kinetics and flame inhibition effects of chloromethane.
Combustion and Flame, 105(3), 291–307. https://doi.org/10.1016/0010-2180(95)00206-5

Reference legend:
[Wang1996] Wang, H., Hahn, T. O., Sung, C. J., & Law, C. K. (1996). Detailed oxidation kinetics and flame inhibition effects of chloromethane. Combustion and Flame, 105(3), 291–307. https://doi.org/10.1016/0010-2180(95)00206-5
[Schading1994] Schading, G. N., and Roth, P., Combust. Flame 99:467-474 (1994)
[Ho1992] Ho, W. P., Barat, R. B., and Bozzelli, J. W., Cornbust. Flame 88:265-295 (1992)
[Ho1992_2] Ho, W. P., Yu, Q.-R., and Bozzelli, J. W., Cornbust. Sci. Technol. 85:23-63 (1992)
[Bozzelli1994] Bozzelli, J. W., personal communication, 1994
[Kerr1981] Kerr, J. A., and Moss, S. J., Handbook of Bimolecular and Termolecular Gas Reaction, CRC Press, 1981, Vols. I, II
[Bryukov2001] M. G. Bryukov, I. R. Slagle and V. D. Knyazev, J. Phys. Chem. A, 2001, 105, 3107–3122.
[Karra1988] Karra, S. B., and Senkan, S. M., Cornbust. Sci. Tech- nol. 541333-347 (1987). Karra, S. B., Gutman, D., Senkan, S. M., Cornbust. Sci. Technol. 60:45-62 (1988)

"""

entry(
    index = 1,
    label = "H + Cl <=> HCl",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(5.30e+21, 'cm^6/(mol^2*s)'), n=-2.0, Ea=(-2000, 'cal/mol'), T0=(1, 'K'),
                                 Tmin=(873, 'K'), Tmax=(4600, 'K')),
        #efficiencies = {'H2': 2, 'H2O': 6, 'CH4': 2, 'CO': 1.5, 'CO2': 2, 'C2H6': 3, 'Ar': 0.7}, #'CH3Cl': 3},
        ),
    shortDesc = u"""[Wang1996],[Schading1994],[Ho1992],[Bozzelli1994]""",
    longDesc =
u"""
Evaluated in [Wang1996] by combining the reverse rate coefficient data over the temperature range of 2500-4600 K
reported by [Schading1994], and a rate coefficient value of 1 X 10” cm6/mo12s used by [Ho1992] and [Bozzelli1994]
in the kinetic modeling studies of CH,Cl and CH,Cl, oxidation over the temperature range of 873-1273 K.
""",
)

entry(
    index = 2,
    label = "Cl + Cl <=> Cl2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(3.34e+14, 'cm^6/(mol^2*s)'), n=0, Ea=(-1800, 'cal/mol'), T0=(1, 'K'),
                                 Tmin=(873, 'K'), Tmax=(4600, 'K')),
        #efficiencies = {'H2': 2, 'H2O': 6, 'CH4': 2, 'CO': 1.5, 'CO2': 2, 'C2H6': 3, 'Ar': 0.7,'CH3Cl': 3},
        ),
    shortDesc = u"""[Wang1996],[Kerr1981]""",
    longDesc =
u"""

""",
)

entry(
    index = 3,
    label = "Cl + HO2 <=> HCl + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.08E+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-338, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""[Ho1992_2]""",
    longDesc =
u"""

""",
)

entry(
    index = 4,
    label = "Cl + HO2 <=> ClO+ OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.47E+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (894, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""[Ho1992_2]""",
    longDesc =
u"""

""",
)

entry(
    index = 5,
    label = "Cl + H2O2 <=> HCl+ HO2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.62E+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1950, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""[Ho1992_2]""",
    longDesc =
u"""

""",
)

entry(
    index = 6,
    label = "Cl + HOCl <=> Cl2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81E+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (260, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""[Ho1992_2]""",
    longDesc =
u"""

""",
)

entry(
    index = 7,
    label = "Cl + HOCl <=> HCl + ClO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.28E+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (100, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""[Ho1992_2]""",
    longDesc =
u"""

""",
)

entry(
    index = 8,
    label = "Cl + CH4 <=> CH3 + HCl",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.09E+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""[Ho1992_2]""",
    longDesc =
u"""

""",
)

entry(
    index = 9,
    label = "Cl + CH3O <=> HCl + CH2O",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (4.00E+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""[Bozzelli1994]""",
    longDesc =
u"""

""",
)

entry(
    index = 10,
    label = "Cl + CH2OH <=> HCl + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.00E+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""[Bozzelli1994]""",
    longDesc =
u"""

""",
)

entry(
    index = 11,
    label = "Cl + CH2O <=> HCO + HCl",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.00E+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (500, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""[Ho1992_2]""",
    longDesc =
u"""

""",
)

entry(
    index = 12,
    label = "Cl + C2H6 <=> C2H5 + HCl",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (4.37E+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (100, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""[Bozzelli1994]""",
    longDesc =
u"""

""",
)

entry(
    index = 13,
    label = "Cl + C2H4 <=> C2H3 + HCl",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (2.39E+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""[Bozzelli1994]""",
    longDesc =
u"""

""",
)

entry(
    index = 14,
    label = "Cl + C2H2 <=> C2H + HCl",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.58E+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (16900, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""[Ho1992_2]""",
    longDesc =
u"""

""",
)

entry(
    index = 15,
    label = "ClO + O <=> Cl + O2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (9.70E+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (507, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""[Karra1988]""",
    longDesc =
u"""

""",
)

entry(
    index = 16,
    label = "ClO + H2 <=> HOCl + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.03E+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (14100, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""[Ho1992_2]""",
    longDesc =
u"""

""",
)

entry(
    index = 17,
    label = "ClO + CH4 <=> CH3 + HOCl",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (6.03E+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (15000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""[Ho1992_2]""",
    longDesc =
u"""

""",
)

entry(
    index = 18,
    label = "ClO + CH3 <=> CH3O + Cl",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.33E+11, 'cm^3/(mol*s)'),
        n = 0.46,
        Ea = (30, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""[Ho1992_2]""",
    longDesc =
u"""

""",
)

entry(
    index = 19,
    label = "ClO + CH3 <=> CH2O + HCl",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.33E+11, 'cm^3/(mol*s)'),
        n = 0.46,
        Ea = (30, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""[Ho1992_2]""",
    longDesc =
u"""

""",
)

entry(
    index = 20,
    label = "ClO + CH3O <=> HOCl + CH2O",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.41E+13, 'cm^3/(mol*s)'),
        n = 0.,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""[Ho1992_2]""",
    longDesc =
u"""

""",
)

entry(
    index = 21,
    label = "ClO + CH2O <=> HCO + HOCl",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.50E+03, 'cm^3/(mol*s)'),
        n = 2.81,
        Ea = (5860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""[Ho1992_2]""",
    longDesc =
u"""

""",
)

# entry(
#     index = 22,
#     label = "ClO + CO <=> Cl + CO2",
#     degeneracy = 1,
#     kinetics = Arrhenius(
#         A = (6.03E+11, 'cm^3/(mol*s)'),
#         n = 2.81,
#         Ea = (17400, 'cal/mol'),
#         T0 = (1, 'K'),
#     ),
#     shortDesc = u"""[Ho1992]""",
#     longDesc =
# u"""
#
# """,
# )
#exceeds the collision limit at 1000 K, 1 bar of 706314070.93 mol/(m3*s) at 25564098629.0 mol/(m3*s)

entry(
    index = 23,
    label = "HOCl <=> Cl + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.76E+20, 'cm^3/(mol*s)'),
        n = -3.01,
        Ea = (56720, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""[Ho1992_2]""",
    longDesc =
u"""

""",
)

entry(
    index = 24,
    label = "HOCl <=> H + ClO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.12E+14, 'cm^3/(mol*s)'),
        n = -2.09,
        Ea = (93690, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""[Ho1992_2]""",
    longDesc =
u"""

""",
)

entry(
    index = 25,
    label = "HOCl + H <=> HCl + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.55E+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7620, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""[Ho1992_2]""",
    longDesc =
u"""

""",
)

entry(
    index = 26,
    label = "HOCl + O <=> OH + ClO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.03E+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4370, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""[Ho1992_2]""",
    longDesc =
u"""

""",
)

entry(
    index = 999,
    label = "Cl + CH3 <=> CH3Cl",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.07e+13, 'cm^3/(mol*s)'),
        n = 0.30,
        Ea = (-0.45, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
        Pmin = (133, 'Pa'),
        Pmax = (1.33E+7, 'Pa'),
    ),
    reference = Article(
        authors = ["Parker, J.K.;Payne, W.A.;Cody, R.J.;Nesbitt, F.L.;Stief, L.J.;Klippenstein, S.J.;Harding, L.B."],
        title = u'Direct measurement and theoretical calculation of the rate coefficient for Cl + CH3 in the range from T=202-298 K',
        journal = "J. Phys. Chem. A",
        volume = "111",
        pages = """1015-1023""",
        year = "2007",
        url = "https://kinetics.nist.gov/kinetics/Detail?id=2007PAR/PAY1015-1023:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc =
u"""

""",
)

entry(
    index = 37,
    label = "CH3Cl + H <=> HCl + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.64E+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7620, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""[Ho1992]""",
    longDesc =
u"""

""",
)

entry(
    index = 57,
    label = "CH2Cl + H <=> CH3Cl",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.04E+25, 'cm^3/(mol*s)'),
        n = -4.47,
        Ea = (3490, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""[Bozzelli1994]""",
    longDesc =
u"""

""",
)

entry(
    index = 38,
    label = "CH3Cl + Cl <=> HCl + CH2Cl",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (3.16E+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3300, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""[Ho1992_2]""",
    longDesc =
u"""

""",
)

# entry(
#     index = 998,
#     label = "CH3Cl + H <=> H2 + CH2Cl",
#     degeneracy = 3,
#     kinetics = Arrhenius(
#         A = (7.17E11, 'cm^3/(mol*s)'),
#         n = 2.59,
#         Ea = (7645, 'cal/mol'),
#         T0 = (1, 'K'),
#     ),
#     shortDesc = u"""[Bryukov2001]""",
#     longDesc =
# u"""
#
# """,
# )
#exceeds the collision limit at 1000 K, 1 bar of 706314070.93 mol/(m3*s) at 9.01033522312e+11 mol/(m3*s)

entry(
    index = 42,
    label = "CH3Cl + O2 <=> CH2Cl + HO2",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.02E+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (54000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""[Bozzelli1994]""",
    longDesc =
u"""

""",
)
