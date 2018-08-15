#!/usr/bin/env python
# encoding: utf-8

name = "Frenklach2019_ProcCombInst"
shortDesc = u""
longDesc = u"""
Re-evaluated kinetics of key HACA reaction steps at 1 atm, such as H abstraction by H in forward and reverse direction and C2H2 additions to radical sites at the armchair and zigzag edges forming both aromatic and aliphatic products.
"""
entry(
    index = 1,
    label = "C6H6 + H <=> C6H5 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.57e+8, 'cm^3/(mol*s)'), n=1.88, Ea=(14839, 'cal/mol'), T0=(1, 'K')),
)

#entry(
#    index = 2,
#    label = "C6H5 + H2 <=> C6H6 + H",
#    degeneracy = 1,
#    kinetics = Arrhenius(A=(1.69e+4, 'cm^3/(mol*s)'), n=2.62, Ea=(4559, 'cal/mol'), T0=(1, 'K')),
#)

entry(
    index = 3,
    label = "C10H8 + H <=> 1-naphthyl + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.91e+8, 'cm^3/(mol*s)'), n=1.84, Ea=(14973, 'cal/mol'), T0=(1, 'K')),
)

#entry(
#    index = 4,
#    label = "1-naphthyl + H2 <=> C10H8 + H",
#    degeneracy = 1,
#    kinetics = Arrhenius(A=(1.58e+4, 'cm^3/(mol*s)'), n=2.63, Ea=(4107, 'cal/mol'), T0=(1, 'K')),
#)

entry(
    index = 5,
    label = "C10H8 + H <=> 2-naphthyl + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.04e+8, 'cm^3/(mol*s)'), n=1.83, Ea=(14980, 'cal/mol'), T0=(1, 'K')),
)

#entry(
#    index = 6,
#    label = "2-naphthyl + H2 <=> C10H8 + H",
#    degeneracy = 1,
#    kinetics = Arrhenius(A=(1.84e+4, 'cm^3/(mol*s)'), n=2.61, Ea=(4446, 'cal/mol'), T0=(1, 'K')),
#)

entry(
    index = 7,
    label = "phenanthryl + C2H2 <=> pyrene + H",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (1.19e+22, 'cm^3/(mol*s)'),
                n = -2.45,
                Ea = (18890, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.06e+14, 'cm^3/(mol*s)'),
                n = -0.49,
                Ea = (8204, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    longDesc = u"""The multiArrhenius form is to capture both high and low temperature behavior""",
)

entry(
    index = 8,
    label = "phenanthryl + C2H2 <=> ethynylphenanthrene + H",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (4.24e+14, 'cm^3/(mol*s)'),
                n = 0.025,
                Ea = (33080, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.64e-2, 'cm^3/(mol*s)'),
                n = 3.95,
                Ea = (16495, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    longDesc = u"""The multiArrhenius form is to capture both high and low temperature behavior""",
)

entry(
    index = 9,
    label = "1-naphthyl + C2H2 <=> acenaphthalene + H",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (1.25e+27, 'cm^3/(mol*s)'),
                n = -3.95,
                Ea = (16779, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.09e+20, 'cm^3/(mol*s)'),
                n = -2.78,
                Ea = (8890, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    longDesc = u"""The multiArrhenius form is to capture both high and low temperature behavior""",
)

entry(
    index = 10,
    label = "1-naphthyl + C2H2 <=> 1-ethynylnaphthalene + H",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (3.09e+25, 'cm^3/(mol*s)'),
                n = -3.11,
                Ea = (31586, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.85e+7, 'cm^3/(mol*s)'),
                n = 1.52,
                Ea = (13190, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    longDesc = u"""The multiArrhenius form is to capture both high and low temperature behavior""",
)

entry(
    index = 11,
    label = "2-naphthyl + C2H2 <=> 2-ethynylnaphthalene + H",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (1.75e+41, 'cm^3/(mol*s)'),
                n = -7.59,
                Ea = (33490, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.45e+172, 'cm^3/(mol*s)'),
                n = -50.63,
                Ea = (66060, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    longDesc = u"""The multiArrhenius form is to capture both high and low temperature behavior""",
)

entry(
    index = 12,
    label = "2-naphthyl + C2H2 <=> w1",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (1.32e+40, 'cm^3/(mol*s)'),
                n = -8.25,
                Ea = (16340, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (8.10e+8, 'cm^3/(mol*s)'),
                n = 0.0,
                Ea = (-4058, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    longDesc = u"""The multiArrhenius form is to capture both high and low temperature behavior""",
)

entry(
    index = 13,
    label = "pentacyl + C2H2 <=> acepentacene + H",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (9.47e+17, 'cm^3/(mol*s)'),
                n = -1.23,
                Ea = (22004, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.87e+66, 'cm^3/(mol*s)'),
                n = -14.23,
                Ea = (61906, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    longDesc = u"""The multiArrhenius form is to capture both high and low temperature behavior""",
)

entry(
    index = 14,
    label = "pentacyl + C2H2 <=> ethynylpentacene + H",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (2.1e+25, 'cm^3/(mol*s)'),
                n = -2.87,
                Ea = (35800, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (8.15e+4, 'cm^3/(mol*s)'),
                n = 2.4,
                Ea = (15108, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    longDesc = u"""The multiArrhenius form is to capture both high and low temperature behavior""",
)

entry(
    index = 15,
    label = "pentacyl + C2H2 <=> w4",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (5.77e+0, 'cm^3/(mol*s)'),
                n = 3.79,
                Ea = (-577, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (-2.28e+29, 'cm^3/(mol*s)'),
                n = -3.88,
                Ea = (29350, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    longDesc = u"""The multiArrhenius form is to capture both high and low temperature behavior""",
)

entry(
    index = 16,
    label = "w4 <=> acepentacene + H",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (2.23e+69, 'cm^3/(mol*s)'),
                n = -15.57,
                Ea = (96283, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.75e+27, 'cm^3/(mol*s)'),
                n = -4.07,
                Ea = (61446, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    longDesc = u"""The multiArrhenius form is to capture both high and low temperature behavior""",
)

