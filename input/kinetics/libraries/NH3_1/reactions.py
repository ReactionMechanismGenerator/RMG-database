#!/usr/bin/env python
# encoding: utf-8

name = "NH3_1"
shortDesc = u"NH3_1"
longDesc =u"""
"""

entry(
    index=1,
    label="NH2 + HO2 <=> NH3 + O2",
    # kinetics=Arrhenius(A=(2.424e+5, 'cm^3/(mol*s)'), n=2.359, Ea=(-22170, 'J/mol'),
    #                    T0=(1, 'K'), Tmin=(500, 'K'), Tmax=(3000, 'K')),
    kinetics=Arrhenius(A=(2.179e+6, 'cm^3/(mol*s)'), n=2.080, Ea=(-19920, 'J/mol'),
                       T0=(1, 'K'), Tmin=(500, 'K'), Tmax=(1700, 'K')),
    shortDesc=u"""""",
    longDesc=
    u"""
    NH3-1 R1
    """,
)

entry(
    index=2,
    label="NNH + O2 <=> N2 + HO2",
    kinetics=Arrhenius(A=(5.6e+14, 'cm^3/(mol*s)'), n=-0.358, Ea=(-56, 'J/mol'),
                       T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(2400, 'K')),
    shortDesc=u"""""",
    longDesc=
    u"""
    NH3-1 R2
    """,
)

entry(
    index=3,
    label="HNO + HNO <=> N2O + H2O",
    kinetics=Arrhenius(A=(8.4e+8, 'cm^3/(mol*s)'), n=0.0, Ea=(13000, 'J/mol'),
                       T0=(1, 'K'), Tmin=(450, 'K'), Tmax=(520, 'K')),
    shortDesc=u"""""",
    longDesc=
    u"""
    NH3-1 R3
    """,
)

entry(
    index=4,
    label="HNO2 <=> HONO",
    kinetics=PDepArrhenius(
        pressures=([0.1000, 0.2154, 0.4641, 1.000, 2.154, 4.641, 10.00, 21.54, 46.41, 100.0], 'atm'),
        arrhenius=[
            Arrhenius(A=(1.09e+47, 's^-1'), n=-11.48, Ea=(218200, 'cal/mol'), T0=(1, 'K'), Tmin=(250, 'K'), Tmax=(2000, 'K')),
            Arrhenius(A=(1.60e+44, 's^-1'), n=-10.63, Ea=(212500, 'cal/mol'), T0=(1, 'K'), Tmin=(250, 'K'), Tmax=(2000, 'K')),
            Arrhenius(A=(2.01e+41, 's^-1'), n=-9.74, Ea=(206900, 'cal/mol'), T0=(1, 'K'), Tmin=(250, 'K'), Tmax=(2000, 'K')),
            Arrhenius(A=(1.65e+38, 's^-1'), n=-8.79, Ea=(201500, 'cal/mol'), T0=(1, 'K'), Tmin=(250, 'K'), Tmax=(2000, 'K')),
            Arrhenius(A=(7.49e+34, 's^-1'), n=-7.73, Ea=(196100, 'cal/mol'), T0=(1, 'K'), Tmin=(250, 'K'), Tmax=(2000, 'K')),
            Arrhenius(A=(2.32e+31, 's^-1'), n=-6.60, Ea=(191100, 'cal/mol'), T0=(1, 'K'), Tmin=(250, 'K'), Tmax=(2000, 'K')),
            Arrhenius(A=(9.05e+27, 's^-1'), n=-5.47, Ea=(186900, 'cal/mol'), T0=(1, 'K'), Tmin=(250, 'K'), Tmax=(2000, 'K')),
            Arrhenius(A=(8.53e+24, 's^-1'), n=-4.44, Ea=(183600, 'cal/mol'), T0=(1, 'K'), Tmin=(250, 'K'), Tmax=(2000, 'K')),
            Arrhenius(A=(2.73e+22, 's^-1'), n=-3.55, Ea=(181500, 'cal/mol'), T0=(1, 'K'), Tmin=(250, 'K'), Tmax=(2000, 'K')),
            Arrhenius(A=(2.67e+20, 's^-1'), n=-2.80, Ea=(180400, 'cal/mol'), T0=(1, 'K'), Tmin=(250, 'K'), Tmax=(2000, 'K')),
        ],
    ),
    shortDesc=u"""""",
    longDesc=
    u"""
    NH3-1 R4
    """,
)

entry(
    index=5,
    label="NH2 + NH2 <=> N2H2 + H2",
    kinetics=ThirdBody(
        arrheniusLow=Arrhenius(A=(1.74e+8, 'cm^6/(mol^2*s)'), n=1.02, Ea=(11800, 'cal/mol'),
                               T0=(1, 'K'), Tmin=(500, 'K'), Tmax=(2250, 'K'))),
    shortDesc=u"""""",
    longDesc=
    u"""
    NH3-1 R5
    """,
)

entry(
    index=6,
    label="N2H3 <=> N2H2 + H",
    kinetics=Chebyshev(
        coeffs=[
            [-5.72811, 0.827052, -0.151977, 0.0113962],
            [14.4486, 0.752768, 0.0118894, -0.0279321],
            [-0.476783, 0.220683, 0.0593312, -2.61431e-3],
            [-0.25248, 0.0415534, 0.0251892, 6.24707e-3],
            [-0.109789, -3.35344e-3, 4.29793e-3, 3.18557e-3],
            [-0.039966, -8.77395e-3, -1.47381e-3, 4.59193e-4],
        ],
        kunits='s^-1',
        Tmin=(300, 'K'),
        Tmax=(3000, 'K'),
        Pmin=(0.01, 'bar'),
        Pmax=(100, 'bar'),
    ),
    shortDesc=u"""""",
    longDesc=
    u"""
    NH3-1 R6
    """,
)

entry(
    index=71,
    label="N2H3 + NH2 <=> H2NN(S) + NH3",
    kinetics=Arrhenius(A=(1.111e+1, 'cm^3/(mol*s)'), n=3.080, Ea=(883.0, 'J/mol'),
                       T0=(1, 'K'), Tmin=(450, 'K'), Tmax=(520, 'K')),
    duplicate=True,
    shortDesc=u"""""",
    longDesc=
    u"""
    NH3-1 R7 A
    """,
)

entry(
    index=72,
    label="N2H3 + NH2 <=> H2NN(S) + NH3",
    kinetics=Chebyshev(
        coeffs=[
            [11.8587, -0.720541, -0.135785, 1.99697e-3],
            [0.303136, 0.802251, 0.110296, -0.0164717],
            [-0.0197441, 0.0133575, 0.0483838, 0.0121341],
            [0.0146729, -0.0808526, -0.0112121, 4.42436e-3],
            [0.0408972, -0.0273676, -0.0129358, -1.37426e-3],
            [0.0287508, 1.34059e-3, -3.04271e-3, -1.3336e-3],
        ],
        kunits='cm^3/(mol*s)',
        Tmin=(300, 'K'),
        Tmax=(3000, 'K'),
        Pmin=(0.01, 'bar'),
        Pmax=(100, 'bar'),
    ),
    duplicate=True,
    shortDesc=u"""""",
    longDesc=
    u"""
    NH3-1 R7 B
    """,
)

entry(
    index=8,
    label="N2H2 <=> NNH + H",
    kinetics=ThirdBody(
        arrheniusLow=Arrhenius(A=(3.8e+13, 'cm^3/(mol*s)'), n=1.2, Ea=(293000, 'cal/mol'), T0=(1, 'K')),
    ),
    shortDesc=u"""""",
    longDesc=
    u"""
    NH3-1 R8
    """,
)

entry(
    index=10,
    label="N2H4 + H <=> NH3 + NH2",
    kinetics=Arrhenius(A=(2.31e+8, 'cm^3/(mol*s)'), n=1.42, Ea=(34320, 'J/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(5000, 'K')),
    shortDesc=u"""""",
    longDesc=
    u"""
    NH3-1 R10
    """,
)

entry(
    index=11,
    label="N2H3 <=> NH2 + NH(S)",
    kinetics=Chebyshev(
        coeffs=[
            [-32.1519, 1.99777, -0.00154937, -8.58245e-4],
            [34.7665, 0.00206067, 1.43154e-3, 7.92275e-4],
            [-0.366105, 6.67105e-5, 4.69747e-5, 2.6576e-5],
            [-0.1722, -3.28998e-5, -2.2835e-5, -1.26191e-5],
            [-0.063659, -3.33579e-5, -2.32082e-5, -1.28761e-5],
            [-0.0160545, -2.41739e-5, -1.68236e-5, -9.33842e-6],
        ],
        kunits='s^-1',
        Tmin=(300, 'K'),
        Tmax=(3000, 'K'),
        Pmin=(0.01, 'bar'),
        Pmax=(100, 'bar'),
    ),
    shortDesc=u"""""",
    longDesc=
    u"""
    NH3-1 R11
    """,
)

entry(
    index=12,
    label="NH3 + NH2 <=> N2H3 + H2",
    kinetics=Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0.0, Ea=(246000, 'J/mol'),
                       T0=(1, 'K'), Tmin=(1000, 'K'), Tmax=(2500, 'K')),
    shortDesc=u"""""",
    longDesc=
    u"""
    NH3-1 R12
    """,
)
