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
    label = "C2H5 + CH3LiO <=> C3H8O + Li",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(0.00266112,'cm^3/(mol*s)'), n=4.54216, Ea=(65.2952,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Li]OC + C[CH2] <=> [Lip] + COCC
""",
)

entry(
    index = 2,
    label = "CH3 + CH4LiN <=> C2H7N + Li",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(514.959,'cm^3/(mol*s)'), n=2.75171, Ea=(19.1236,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=5.9720845035693655,B=-11.11835148496454,E=1.2672065293713617,L=34.51723438776737,A=-10.461680798130194,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Li]NC + [CH3] <=> [Lip] + CNC
""",
)

entry(
    index = 3,
    label = "H + C2H6LiN <=> C2H7N-2 + Li",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(8.98085e+08,'cm^3/(mol*s)'), n=1.22191, Ea=(-78.8037,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.996332219215656,B=1.029302623121347,E=1.007550487792502,L=7.3685642232941575,A=0.4814345945968402,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Li]N(C)C + [H] <=> [Lip] + CNC
""",
)

entry(
    index = 4,
    label = "C2H5 + CH4LiN <=> C3H9N + Li",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(57.4636,'cm^3/(mol*s)'), n=2.93295, Ea=(29.2672,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=0.9175438008860265,B=1.1395826064596657,E=0.4944811262263229,L=5.415263196320309,A=0.6943364764189893,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Li]NC + C[CH2] <=> [Lip] + CNCC
""",
)

entry(
    index = 5,
    label = "CH3 + C2H6LiN-2 <=> C3H9N-2 + Li",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(563.399,'cm^3/(mol*s)'), n=2.71918, Ea=(25.4344,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.877486735996646,B=0.6916407047808263,E=0.748415650862252,L=5.385263016210897,A=0.5210754074032086,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Li]NCC + [CH3] <=> [Lip] + CNCC
""",
)

entry(
    index = 6,
    label = "H + C3H8LiN <=> C3H9N-3 + Li",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(2.33693e+09,'cm^3/(mol*s)'), n=1.12822, Ea=(-71.4349,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=2.1131935806214712,B=1.1556454917670655,E=1.2169728270193971,L=7.839572648134702,A=0.31656236651087616,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Li]N(C)CC + [H] <=> [Lip] + CNCC
""",
)

entry(
    index = 7,
    label = "H + HLiO <=> H2O + Li",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(2.03649e+11,'cm^3/(mol*s)'), n=0.812216, Ea=(-21.6525,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.6576610150461983,B=2.4435784684265482,E=0.404796645816695,L=7.698368077501874,A=0.9750486732350473,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Li]O + [H] <=> [Lip] + O
""",
)

entry(
    index = 8,
    label = "H + H2LiN <=> H3N + Li",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(4.12322e+09,'cm^3/(mol*s)'), n=1.12657, Ea=(-57.4909,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.9471505265788214,B=1.7274624400621788,E=0.6115119617819315,L=6.871072605917964,A=0.6704069036466952,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Li]N + [H] <=> [Lip] + N
""",
)

entry(
    index = 9,
    label = "H + CH3LiO <=> CH4O + Li",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(2.47113e+11,'cm^3/(mol*s)'), n=0.774968, Ea=(-24.6724,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=2.4067121409688057,B=1.4628968939845368,E=0.9656443938025181,L=7.661570379273675,A=0.443175955652443,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Li]OC + [H] <=> [Lip] + CO
""",
)

entry(
    index = 10,
    label = "CH3 + HLiO <=> CH4O-2 + Li",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(1.07712e+06,'cm^3/(mol*s)'), n=2.28023, Ea=(85.5904,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.4173362998736376,B=2.357499252462657,E=0.5167298959343533,L=7.9017680525604375,A=1.0064038665607862,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Li]O + [CH3] <=> [Lip] + CO
""",
)

entry(
    index = 11,
    label = "H + CH4LiN <=> CH5N + Li",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(7.62458e+07,'cm^3/(mol*s)'), n=1.49444, Ea=(-71.5589,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=-5.4761368991675985,B=-6.829449919467144,E=14.43663245128814,L=28.957970295010895,A=0.4259943743771139,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Li]NC + [H] <=> [Lip] + CN
""",
)

entry(
    index = 12,
    label = "C2H5 + HLiO <=> C2H6O + Li",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(26.5507,'cm^3/(mol*s)'), n=3.72095, Ea=(84.1068,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.9913576154323054,B=3.1755887609180435,E=-0.2623364392566645,L=7.244831699370673,A=0.5572363451823703,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Li]O + C[CH2] <=> [Lip] + CCO
""",
)

entry(
    index = 13,
    label = "H + C2H5LiO <=> C2H6O-2 + Li",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(6.77483e+09,'cm^3/(mol*s)'), n=1.18598, Ea=(-23.16,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=-8.623486006056842,B=14.917486429580572,E=-5.719694357458241,L=40.120001635540106,A=-6.502228345652631,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Li]OCC + [H] <=> [Lip] + CCO
""",
)

entry(
    index = 14,
    label = "C2H5 + H2LiN <=> C2H7N-3 + Li",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(0.337329,'cm^3/(mol*s)'), n=3.54967, Ea=(34.4127,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.6195332200790409,B=2.120893670736446,E=10.142480436000628,L=-0.8781474558081529,A=3.410407959634951,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Li]N + C[CH2] <=> [Lip] + CCN
""",
)

entry(
    index = 15,
    label = "CH3 + CH3LiO <=> C2H6O-3 + Li",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(3026.56,'cm^3/(mol*s)'), n=2.80221, Ea=(80.834,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=2.223920620501668,B=0.8264175269682525,E=0.40415741933873844,L=5.605210034978575,A=0.4397271958947774,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Li]OC + [CH3] <=> [Lip] + COC
""",
)

entry(
    index = 16,
    label = "CH3 + C2H5LiO <=> C3H8O-2 + Li",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(7.09569,'cm^3/(mol*s)'), n=3.2546, Ea=(82.2788,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=2.091886494292463,B=0.5254418313743373,E=1.2963729646265112,L=5.721969023897385,A=0.6575614317431779,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Li]OCC + [CH3] <=> [Lip] + COCC
""",
)

entry(
    index = 17,
    label = "CH3 + H2LiN <=> CH5N-2 + Li",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(5347.09,'cm^3/(mol*s)'), n=2.59727, Ea=(34.8806,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=0.8306578175990244,B=1.956506108230911,E=0.011774617070094268,L=6.100850860272114,A=1.0441801517777485,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Li]N + [CH3] <=> [Lip] + CN
""",
)

entry(
    index = 18,
    label = "H + C2H6LiN-2 <=> C2H7N-4 + Li",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(1.89074e+07,'cm^3/(mol*s)'), n=1.63253, Ea=(-67.2986,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.9852422925798727,B=1.2991389460904967,E=1.413033851489418,L=7.445245509701895,A=0.5371087291175491,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Li]NCC + [H] <=> [Lip] + CCN
""",
)

