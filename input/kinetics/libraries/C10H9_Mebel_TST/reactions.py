#!/usr/bin/env python
# encoding: utf-8

name = "C10H9_Mebel_TST"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "W5 <=> W6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.57e+10, 's^-1'), n=0.43, Ea=(1.924, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2,
    label = "W5 <=> W8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.311e+09, 's^-1'), n=0.537, Ea=(2.307, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3,
    label = "W8 <=> W13",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.588e+10, 's^-1'), n=0.535, Ea=(9.58, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 4,
    label = "W6 <=> W13",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.53e+12, 's^-1'), n=0.189, Ea=(29.234, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 5,
    label = "W101 <=> W8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.964e+07, 's^-1'), n=1.633, Ea=(47.984, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 6,
    label = "W8 <=> W102",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.429e+08, 's^-1'), n=1.267, Ea=(24.384, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 7,
    label = "W5 <=> W103",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.193e+07, 's^-1'), n=1.425, Ea=(7.283, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 8,
    label = "W104 <=> W6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.09e+11, 's^-1'), n=0.703, Ea=(23.53, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 9,
    label = "W102 <=> W103",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.017e+13, 's^-1'), n=0.272, Ea=(49.677, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 10,
    label = "W103 <=> W104",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.69e+10, 's^-1'), n=0.239, Ea=(33.778, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 11,
    label = "W106 <=> W107",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.423e+08, 's^-1'), n=1.522, Ea=(63.602, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 12,
    label = "W106 <=> W108",
    degeneracy = 1,
    kinetics = Arrhenius(A=(68.8, 's^-1'), n=3.351, Ea=(60.931, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 13,
    label = "W107 <=> W108",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.548e+09, 's^-1'), n=0.934, Ea=(9.114, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 14,
    label = "W108 <=> W111",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.279e+13, 's^-1'), n=0.395, Ea=(53.699, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 15,
    label = "W112 <=> W118",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.753e+08, 's^-1'), n=1.291, Ea=(40.177, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 16,
    label = "W6 <=> W118",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.93e+07, 's^-1'), n=1.684, Ea=(33.806, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 17,
    label = "W13 <=> W107",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.161e+12, 's^-1'), n=0.277, Ea=(28.025, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 18,
    label = "W108 <=> W115",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.473e+12, 's^-1'), n=0.247, Ea=(55.262, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 19,
    label = "W111 <=> W112",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.748e+10, 's^-1'), n=0.262, Ea=(19.926, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 20,
    label = "W115 <=> W117",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.401e+08, 's^-1'), n=1.453, Ea=(42.614, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 21,
    label = "W117 <=> W118",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.998e+12, 's^-1'), n=0.237, Ea=(16.277, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 22,
    label = "W102 <=> W119",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.181e+10, 's^-1'), n=0.964, Ea=(32.063, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 23,
    label = "C6H4C2H3 + C2H2 <=> W5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.12e+07, 'cm^3/(mol*s)'),
        n = 1.489,
        Ea = (4.331, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 24,
    label = "W6 <=> P1 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.567e+11, 's^-1'), n=0.787, Ea=(28.205, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 25,
    label = "W8 <=> P2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.191e+09, 's^-1'), n=1.264, Ea=(30.816, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 26,
    label = "W5 <=> P5 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.304e+10, 's^-1'), n=1.16, Ea=(37.552, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 27,
    label = "W101 <=> P2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.05e+10, 's^-1'), n=1.329, Ea=(52.477, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 28,
    label = "W102 <=> P2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.923e+11, 's^-1'), n=0.777, Ea=(40.274, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 29,
    label = "W103 <=> P105 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.568e+11, 's^-1'), n=0.972, Ea=(78.037, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 30,
    label = "W107 <=> P109 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.249e+08, 's^-1'), n=1.2, Ea=(27.426, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 31,
    label = "W118 <=> P1 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.956e+11, 's^-1'), n=0.789, Ea=(32.262, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 32,
    label = "W106 <=> P109 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.427e+09, 's^-1'), n=1.431, Ea=(66.532, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 33,
    label = "W108 <=> P109 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.893e+15, 's^-1'), n=-0.16, Ea=(65.494, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 34,
    label = "W111 <=> P114 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.89e+16, 's^-1'), n=-0.28, Ea=(68.378, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 35,
    label = "W119 <=> P2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.234e+12, 's^-1'), n=0.766, Ea=(43.611, 'kcal/mol'), T0=(1, 'K')),
)

