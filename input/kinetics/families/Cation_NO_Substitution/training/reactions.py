#!/usr/bin/env python
# encoding: utf-8

name = "Cation_NO_Substitution/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 1,
    label = "C3H8O + Li <=> CH3LiO + C2H5",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(236.033,'cm^3/(mol*s)'), n=3.84908, Ea=(56.4483,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.07254, dn = +|- 0.00912116, dEa = +|- 0.0521614 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Lip] + COCC <=> [Li]OC + C[CH2]
""",
)

entry(
    index = 2,
    label = "C2H7N + Li <=> CH4LiN + CH3",
    degeneracy = 2.0,
    kinetics = ArrheniusChargeTransfer(A=(5.84081e+06,'cm^3/(mol*s)'), n=2.5402, Ea=(97.8358,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=5.9720845035693655,B=-11.11835148496454,E=1.2672065293713617,L=34.51723438776737,A=-10.461680798130194,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.31573, dn = +|- 0.0357396, dEa = +|- 0.204385 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Lip] + CNC <=> [Li]NC + [CH3]
""",
)

entry(
    index = 3,
    label = "C2H7N-2 + Li <=> C2H6LiN + H",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(20017.2,'cm^3/(mol*s)'), n=2.76621, Ea=(72.0709,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.996332219215656,B=1.029302623121347,E=1.007550487792502,L=7.3685642232941575,A=0.4814345945968402,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.20383, dn = +|- 0.024163, dEa = +|- 0.138181 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Lip] + CNC <=> [Li]N(C)C + [H]
""",
)

entry(
    index = 4,
    label = "C3H9N + Li <=> CH4LiN + C2H5",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(1.17529e+08,'cm^3/(mol*s)'), n=2.07905, Ea=(110.968,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=0.9175438008860265,B=1.1395826064596657,E=0.4944811262263229,L=5.415263196320309,A=0.6943364764189893,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.06164, dn = +|- 0.00779066, dEa = +|- 0.0445526 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Lip] + CNCC <=> [Li]NC + C[CH2]
""",
)

entry(
    index = 5,
    label = "C3H9N-2 + Li <=> C2H6LiN-2 + CH3",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(1.61257e+06,'cm^3/(mol*s)'), n=2.55041, Ea=(96.84,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.877486735996646,B=0.6916407047808263,E=0.748415650862252,L=5.385263016210897,A=0.5210754074032086,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.25373, dn = +|- 0.029453, dEa = +|- 0.168434 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Lip] + CNCC <=> [Li]NCC + [CH3]
""",
)

entry(
    index = 6,
    label = "C3H9N-3 + Li <=> C3H8LiN + H",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(3319.61,'cm^3/(mol*s)'), n=3.0459, Ea=(70.8277,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=2.1131935806214712,B=1.1556454917670655,E=1.2169728270193971,L=7.839572648134702,A=0.31656236651087616,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.28575, dn = +|- 0.0327372, dEa = +|- 0.187215 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Lip] + CNCC <=> [Li]N(C)CC + [H]
""",
)

entry(
    index = 7,
    label = "H2O + Li <=> HLiO + H",
    degeneracy = 2.0,
    kinetics = ArrheniusChargeTransfer(A=(2.20642e+09,'cm^3/(mol*s)'), n=1.35569, Ea=(48.8442,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.6576610150461983,B=2.4435784684265482,E=0.404796645816695,L=7.698368077501874,A=0.9750486732350473,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.12448, dn = +|- 0.0152811, dEa = +|- 0.0873886 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Lip] + O <=> [Li]O + [H]
""",
)

entry(
    index = 8,
    label = "H3N + Li <=> H2LiN + H",
    degeneracy = 3.0,
    kinetics = ArrheniusChargeTransfer(A=(1.86167e+06,'cm^3/(mol*s)'), n=2.44198, Ea=(87.1355,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.9471505265788214,B=1.7274624400621788,E=0.6115119617819315,L=6.871072605917964,A=0.6704069036466952,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.22038, dn = +|- 0.025941, dEa = +|- 0.148349 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Lip] + N <=> [Li]N + [H]
""",
)

entry(
    index = 9,
    label = "CH4O + Li <=> CH3LiO + H",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(4.02602e+06,'cm^3/(mol*s)'), n=2.23116, Ea=(40.7702,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=2.4067121409688057,B=1.4628968939845368,E=0.9656443938025181,L=7.661570379273675,A=0.443175955652443,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.0796, dn = +|- 0.00997547, dEa = +|- 0.057047 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Lip] + CO <=> [Li]OC + [H]
""",
)

entry(
    index = 10,
    label = "CH4O-2 + Li <=> HLiO + CH3",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(1.53764e+08,'cm^3/(mol*s)'), n=2.01928, Ea=(47.7262,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.4173362998736376,B=2.357499252462657,E=0.5167298959343533,L=7.9017680525604375,A=1.0064038665607862,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.49606, dn = +|- 0.0524693, dEa = +|- 0.300058 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Lip] + CO <=> [Li]O + [CH3]
""",
)

entry(
    index = 11,
    label = "CH5N + Li <=> CH4LiN + H",
    degeneracy = 2.0,
    kinetics = ArrheniusChargeTransfer(A=(88554.1,'cm^3/(mol*s)'), n=2.76407, Ea=(81.1221,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=-5.4761368991675985,B=-6.829449919467144,E=14.43663245128814,L=28.957970295010895,A=0.4259943743771139,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.19079, dn = +|- 0.0227446, dEa = +|- 0.13007 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Lip] + CN <=> [Li]NC + [H]
""",
)

entry(
    index = 12,
    label = "C2H6O + Li <=> HLiO + C2H5",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(609636,'cm^3/(mol*s)'), n=2.90468, Ea=(55.2021,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.9913576154323054,B=3.1755887609180435,E=-0.2623364392566645,L=7.244831699370673,A=0.5572363451823703,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.27825, dn = +|- 0.0319751, dEa = +|- 0.182857 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Lip] + CCO <=> [Li]O + C[CH2]
""",
)

entry(
    index = 13,
    label = "C2H6O-2 + Li <=> C2H5LiO + H",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(3.88747e+06,'cm^3/(mol*s)'), n=2.22783, Ea=(40.8372,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=-8.623486006056842,B=14.917486429580572,E=-5.719694357458241,L=40.120001635540106,A=-6.502228345652631,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.09972, dn = +|- 0.0123813, dEa = +|- 0.0708054 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Lip] + CCO <=> [Li]OCC + [H]
""",
)

entry(
    index = 14,
    label = "C2H7N-3 + Li <=> H2LiN + C2H5",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(1309.46,'cm^3/(mol*s)'), n=3.2505, Ea=(88.6985,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.6195332200790409,B=2.120893670736446,E=10.142480436000628,L=-0.8781474558081529,A=3.410407959634951,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.25466, dn = +|- 0.0295493, dEa = +|- 0.168984 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Lip] + CCN <=> [Li]N + C[CH2]
""",
)

entry(
    index = 15,
    label = "C2H6O-3 + Li <=> CH3LiO + CH3",
    degeneracy = 2.0,
    kinetics = ArrheniusChargeTransfer(A=(327198,'cm^3/(mol*s)'), n=2.90093, Ea=(61.3447,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=2.223920620501668,B=0.8264175269682525,E=0.40415741933873844,L=5.605210034978575,A=0.4397271958947774,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.20785, dn = +|- 0.0245968, dEa = +|- 0.140662 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Lip] + COC <=> [Li]OC + [CH3]
""",
)

entry(
    index = 16,
    label = "C3H8O-2 + Li <=> C2H5LiO + CH3",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(137812,'cm^3/(mol*s)'), n=2.70251, Ea=(63.027,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=2.091886494292463,B=0.5254418313743373,E=1.2963729646265112,L=5.721969023897385,A=0.6575614317431779,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.12328, dn = +|- 0.0151425, dEa = +|- 0.086596 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Lip] + COCC <=> [Li]OCC + [CH3]
""",
)

entry(
    index = 17,
    label = "CH5N-2 + Li <=> H2LiN + CH3",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(141645,'cm^3/(mol*s)'), n=2.88935, Ea=(85.5741,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=0.8306578175990244,B=1.956506108230911,E=0.011774617070094268,L=6.100850860272114,A=1.0441801517777485,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.50683, dn = +|- 0.0534042, dEa = +|- 0.305404 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Lip] + CN <=> [Li]N + [CH3]
""",
)

entry(
    index = 18,
    label = "C2H7N-4 + Li <=> C2H6LiN-2 + H",
    degeneracy = 2.0,
    kinetics = ArrheniusChargeTransfer(A=(4503.32,'cm^3/(mol*s)'), n=2.99604, Ea=(78.6799,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.9852422925798727,B=1.2991389460904967,E=1.413033851489418,L=7.445245509701895,A=0.5371087291175491,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.17557, dn = +|- 0.0210685, dEa = +|- 0.120485 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Lip] + CCN <=> [Li]NCC + [H]
""",
)

