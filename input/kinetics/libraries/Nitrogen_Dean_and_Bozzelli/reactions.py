#!/usr/bin/env python
# encoding: utf-8

name = "Nitrogen_Dean_and_Bozelli"
shortDesc = u""
longDesc = u"""
Anthony M. Dean and Joseph W. Bozzelli
Combustion Chemistry of Nitrogen
in Gas-Phase Combustion Chemistry, 2000, pp 125-341
"""
entry(
    index = 1,
    label = "O + N2 <=> N + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+14, 'cm^3/(mol*s)'), n=0, Ea=(76774, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 2,
    label = "NO <=> N + O",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.4e+15, 'cm^3/(mol*s)'), n=0, Ea=(148345, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 3,
    label = "N2O <=> N2 + O",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(5.7e+14, 'cm^3/(mol*s)'), n=0, Ea=(56061, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 4,
    label = "N2O + O <=> N2 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10803, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 5,
    label = "N2O + O <=> NO + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+13, 'cm^3/(mol*s)'), n=0, Ea=(23135, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 6,
    label = "NH3 <=> NH2 + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(3.6e+16, 'cm^3/(mol*s)'), n=0, Ea=(93733, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 7,
    label = "NH3 + H <=> NH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(540000, 'cm^3/(mol*s)'), n=2.4, Ea=(9910, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 8,
    label = "NH3 + OH <=> NH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+07, 'cm^3/(mol*s)'), n=1.6, Ea=(953, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 9,
    label = "NH3 + O <=> NH2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.4e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (6454, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 10,
    label = "NH2 + H <=> NH(S) + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.8e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(7934, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 11,
    label = "HO2 + NO <=> NO2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(-477, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 12,
    label = "N2O + H <=> HNNO",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.2e+24, 'cm^3/(mol*s)'),
                n = -4.46,
                Ea = (10700, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.3e+25, 'cm^3/(mol*s)'),
                n = -4.48,
                Ea = (10769, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.2e+26, 'cm^3/(mol*s)'),
                n = -4.58,
                Ea = (11226, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 13,
    label = "N2O + H <=> N2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.2e+14, 'cm^3/(mol*s)'), n=0, Ea=(16741, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 14,
    label = "H + N2O <=> NH(T) + NO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.5e+20, 'cm^3/(mol*s)'),
        n = -1.26,
        Ea = (35349, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 15,
    label = "H + N2O <=> NNH + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+19, 'cm^3/(mol*s)'),
        n = -1.26,
        Ea = (47065, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 16,
    label = "NH(T) + NO <=> N2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+17, 'cm^3/(mol*s)'),
        n = -1.49,
        Ea = (1311, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 18,
    label = "NH(T) + NO <=> NNH + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+14, 'cm^3/(mol*s)'),
        n = -0.2,
        Ea = (12193, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 19,
    label = "NH(T) + O2 <=> HNOO",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(3.5e+23, 'cm^3/(mol*s)'), n=-5, Ea=(2275, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.7e+24, 'cm^3/(mol*s)'), n=-5, Ea=(2295, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (5.4e+25, 'cm^3/(mol*s)'),
                n = -5.05,
                Ea = (2454, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 20,
    label = "NH(T) + O2 <=> NO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.6e+10, 'cm^3/(mol*s)'), n=0, Ea=(1529, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 21,
    label = "NH(T) + O2 <=> H + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.3e+10, 'cm^3/(mol*s)'), n=0, Ea=(2482, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 22,
    label = "NH(T) + O2 <=> HNO + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(460000, 'cm^3/(mol*s)'), n=2, Ea=(6494, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 23,
    label = "NH2 + O2 <=> NH2O + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+11, 'cm^3/(mol*s)'),
        n = 0.48,
        Ea = (29570, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 24,
    label = "NH2 + O2 <=> HNO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.2e+07, 'cm^3/(mol*s)'),
        n = 1.23,
        Ea = (35081, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 25,
    label = "NH2 + HO2 <=> NH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 26,
    label = "NH2 + HO2 <=> NH3 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (920000, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (-1152, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 27,
    label = "NH2 + O <=> HNO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 28,
    label = "NH2 + O <=> NH(T) + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 29,
    label = "NH2 + OH <=> NH2OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.8e+32, 'cm^3/(mol*s)'),
                n = -6.91,
                Ea = (4113, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(3.9e+33, 'cm^3/(mol*s)'), n=-7, Ea=(4440, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (5.6e+34, 'cm^3/(mol*s)'),
                n = -7.02,
                Ea = (5365, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 30,
    label = "NH2 + OH <=> NH(S) + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+06, 'cm^3/(mol*s)'), n=2, Ea=(50, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 31,
    label = "NH2 + NH2 <=> N2H4",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (2e+46, 'cm^3/(mol*s)'),
                n = -10.93,
                Ea = (9994, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.6e+48, 'cm^3/(mol*s)'),
                n = -11.3,
                Ea = (11882, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.2e+49, 'cm^3/(mol*s)'),
                n = -11.18,
                Ea = (13988, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 32,
    label = "NH2 + NH2 <=> H2NN + H2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (2.4e+20, 'cm^3/(mol*s)'),
                n = -2.91,
                Ea = (2136, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.2e+21, 'cm^3/(mol*s)'),
                n = -3.08,
                Ea = (3368, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.3e+19, 'cm^3/(mol*s)'),
                n = -2.54,
                Ea = (4182, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 33,
    label = "NH2 + NH2 <=> N2H3 + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (9.2e+11, 'cm^3/(mol*s)'),
                n = -0.01,
                Ea = (10014, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.2e+12, 'cm^3/(mol*s)'),
                n = -0.03,
                Ea = (10084, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.7e+12, 'cm^3/(mol*s)'),
                n = -0.2,
                Ea = (10620, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 34,
    label = "NH2 + NH2 <=> NH3 + NH(T)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(9929, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 35,
    label = "NH2 + NO <=> N2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.7e+12, 'cm^3/(mol*s)'),
        n = -0.25,
        Ea = (-1201, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 36,
    label = "NH2 + NO <=> NNH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.5e+10, 'cm^3/(mol*s)'),
        n = 0.34,
        Ea = (-765, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 37,
    label = "NH2 + NO <=> NH2NO",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.9e+30, 'cm^3/(mol*s)'),
                n = -6.67,
                Ea = (3497, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.5e+31, 'cm^3/(mol*s)'),
                n = -6.75,
                Ea = (3725, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.7e+33, 'cm^3/(mol*s)'),
                n = -6.92,
                Ea = (4609, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 38,
    label = "CH3 + NO + N2 <=> CH3NO + N2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^6/(mol^2*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 39,
    label = "CH3 + NO <=> CH3NO",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (3.6e+35, 'cm^3/(mol*s)'),
                n = -8.25,
                Ea = (4808, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(1e+37, 'cm^3/(mol*s)'), n=-8.38, Ea=(5225, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (4.6e+41, 'cm^3/(mol*s)'),
                n = -9.39,
                Ea = (8266, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 40,
    label = "CH3 + NO <=> H2CN + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+09, 'cm^3/(mol*s)'),
        n = 0.75,
        Ea = (11717, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 41,
    label = "CH3 + NO <=> HCN + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.9e+08, 'cm^3/(mol*s)'),
        n = 0.46,
        Ea = (12392, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 42,
    label = "CH3 + N <=> H2CN + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.1e+14, 'cm^3/(mol*s)'),
        n = -0.31,
        Ea = (288, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 43,
    label = "CH3 + N <=> HCN + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.7e+12, 'cm^3/(mol*s)'), n=0.15, Ea=(-89, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 44,
    label = "CH3 + N <=> HCNH + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+11, 'cm^3/(mol*s)'),
        n = 0.52,
        Ea = (-367, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 45,
    label = "CH3 + NH2 <=> CH3NH2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.3e+54, 'cm^3/(mol*s)'),
                n = -12.72,
                Ea = (15607, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.1e+52, 'cm^3/(mol*s)'),
                n = -11.99,
                Ea = (16790, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.6e+47, 'cm^3/(mol*s)'),
                n = -10.15,
                Ea = (15687, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 46,
    label = "CH3 + NH2 <=> CH2NH2 + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.1e+13, 'cm^3/(mol*s)'),
                n = -0.13,
                Ea = (9905, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.4e+14, 'cm^3/(mol*s)'),
                n = -0.43,
                Ea = (11107, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(7.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(12071, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 47,
    label = "CH3 + NH2 <=> CH3NH + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.2e+13, 'cm^3/(mol*s)'),
                n = -0.15,
                Ea = (16144, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.4e+13, 'cm^3/(mol*s)'),
                n = -0.31,
                Ea = (16641, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.4e+14, 'cm^3/(mol*s)'),
                n = -0.42,
                Ea = (17863, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 48,
    label = "CH3 + NH2 <=> H2CNH + H2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (2.1e+11, 'cm^3/(mol*s)'),
                n = -0.1,
                Ea = (19095, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.8e+11, 'cm^3/(mol*s)'),
                n = -0.2,
                Ea = (19403, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.9e+12, 'cm^3/(mol*s)'),
                n = -0.4,
                Ea = (20506, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 49,
    label = "CH3 + NH2 <=> CH4 + NH(S)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (9205, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 50,
    label = "CH3 + NH2 <=> CH2(T) + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (7566, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 51,
    label = "CH2(T) + N2 <=> CH2NN",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (9.3e+30, 'cm^3/(mol*s)'),
                n = -7.01,
                Ea = (19740, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.6e+32, 'cm^3/(mol*s)'),
                n = -7.07,
                Ea = (19969, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.3e+33, 'cm^3/(mol*s)'),
                n = -7.18,
                Ea = (20863.5, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 52,
    label = "CH2(T) + N2 <=> HCN + NH(T)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(73954, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 53,
    label = "CH2(T) + NO <=> HCNO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.8e+13, 'cm^3/(mol*s)'),
        n = -0.36,
        Ea = (576, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 54,
    label = "CH2(T) + NO <=> HCN + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.9e+14, 'cm^3/(mol*s)'),
        n = -0.69,
        Ea = (755, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 55,
    label = "CH2(T) + NO <=> HNCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.1e+17, 'cm^3/(mol*s)'),
        n = -1.38,
        Ea = (1271, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 56,
    label = "CH2(T) + NO <=> NH2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.3e+16, 'cm^3/(mol*s)'),
        n = -1.43,
        Ea = (1331, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 57,
    label = "CH2(T) + NO <=> H2CN + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.1e+07, 'cm^3/(mol*s)'),
        n = 1.42,
        Ea = (4111, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 58,
    label = "CH + N2 <=> HCNN",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (2.3e+27, 'cm^3/(mol*s)'),
                n = -5.78,
                Ea = (2444, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.6e+28, 'cm^3/(mol*s)'),
                n = -5.84,
                Ea = (2623, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.8e+30, 'cm^3/(mol*s)'),
                n = -6.02,
                Ea = (3447.5, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 59,
    label = "CH + N2 <=> HCN + N",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(21964, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 60,
    label = "CH + NO <=> HCN + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 61,
    label = "CH + NO <=> H + NCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 62,
    label = "CH + NO <=> N + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 63,
    label = "CH + NO <=> NH(T) + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 64,
    label = "CH + NO <=> OH + CN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 65,
    label = "N + O2 <=> NO + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+09, 'cm^3/(mol*s)'), n=1, Ea=(6494, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 66,
    label = "N + OH <=> NH(T) + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.4e+12, 'cm^3/(mol*s)'),
        n = 0.1,
        Ea = (21249, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 67,
    label = "N + OH <=> NO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+14, 'cm^3/(mol*s)'), n=0, Ea=(1122, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 68,
    label = "CH + N <=> CN + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+14, 'cm^3/(mol*s)'), n=-0.09, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 69,
    label = "CH2(T) + N <=> HCN + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 70,
    label = "NH(T) + N <=> N2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 71,
    label = "NH2 + N <=> N2 + H + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 72,
    label = "CN + N <=> C(T) + N2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(-556, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 73,
    label = "NH(T) + NH(T) <=> N2 + H + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 74,
    label = "NH2 + NH(T) <=> N2H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+15, 'cm^3/(mol*s)'), n=-0.5, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 75,
    label = "NH2 + NH(T) <=> NH3 + N",
    degeneracy = 1,
    kinetics = Arrhenius(A=(920000, 'cm^3/(mol*s)'), n=1.94, Ea=(2443, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 76,
    label = "NH(T) + OH <=> HNO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 77,
    label = "NH(T) + OH <=> N + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+06, 'cm^3/(mol*s)'), n=2, Ea=(-487, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 78,
    label = "NH(T) + H <=> N + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(1728, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 79,
    label = "NH(T) + O <=> NO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 81,
    label = "NH(T) + CH3 <=> H2CNH + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 82,
    label = "NH(T) + CH3 <=> CH4 + N",
    degeneracy = 1,
    kinetics = Arrhenius(A=(820000, 'cm^3/(mol*s)'), n=1.87, Ea=(5848, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 83,
    label = "NNH + O2 <=> N2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+12, 'cm^3/(mol*s)'),
        n = -0.34,
        Ea = (-894, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 84,
    label = "NNH + O2 <=> N2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.9e+11, 'cm^3/(mol*s)'),
        n = -0.34,
        Ea = (2453, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 85,
    label = "NNH + H <=> N2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(496, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 86,
    label = "NNH + OH <=> N2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+22, 'cm^3/(mol*s)'),
        n = -2.88,
        Ea = (-1152, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 87,
    label = "NNH + O <=> N2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+16, 'cm^3/(mol*s)'),
        n = -1.23,
        Ea = (-1599, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 88,
    label = "NNH + NH2 <=> N2 + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(920000, 'cm^3/(mol*s)'), n=1.94, Ea=(1698, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 89,
    label = "NNH + HO2 <=> N2 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14000, 'cm^3/(mol*s)'), n=2.69, Ea=(-1192, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 90,
    label = "NNH + HO2 <=> HNNO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(70211, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 91,
    label = "NNH + NO <=> N2 + HNO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+06, 'cm^3/(mol*s)'), n=2, Ea=(70717, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 92,
    label = "N2H2 <=> NNH + H",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.1, 1, 10], 'atm'),
                arrhenius = [
                    Arrhenius(A=(5.6e+36, '1/s'), n=-7.75, Ea=(70250.4, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.8e+40, '1/s'), n=-8.41, Ea=(73390, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(3.1e+41, '1/s'), n=-8.42, Ea=(76043, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.1, 1, 10], 'atm'),
                arrhenius = [
                    Arrhenius(A=(1.6e+37, '1/s'), n=-7.94, Ea=(70757, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(2.6e+40, '1/s'), n=-8.53, Ea=(72923, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.3e+44, '1/s'), n=-9.22, Ea=(77076, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
        ],
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 93,
    label = "N2H2 <=> H2NN",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(9.2e+38, '1/s'), n=-9.01, Ea=(67726, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2e+41, '1/s'), n=-9.38, Ea=(68452, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.3e+45, '1/s'), n=-10.13, Ea=(70757, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 94,
    label = "N2H2 + H <=> NNH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.8e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(496, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 95,
    label = "N2H2 + O <=> NNH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-1192, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 96,
    label = "N2H2 + OH <=> NNH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+06, 'cm^3/(mol*s)'), n=2, Ea=(-1152, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 97,
    label = "N2H2 + NH2 <=> NH3 + NNH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (1969, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 98,
    label = "N2H2 + CH3 <=> NNH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1192, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 99,
    label = "N2H2 + NH(T) <=> NNH + NH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+06, 'cm^3/(mol*s)'), n=2, Ea=(11915, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 100,
    label = "N2H2 + NO <=> N2O + NH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+12, 'cm^3/(mol*s)'), n=0, Ea=(51762, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 101,
    label = "H2NN <=> NNH + H",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.1, 1, 10], 'atm'),
                arrhenius = [
                    Arrhenius(A=(5.9e+32, '1/s'), n=-6.99, Ea=(51791.1, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(9.6e+35, '1/s'), n=-5.57, Ea=(54841.2, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (5e+36, 'cm^3/(mol*s)'),
                        n = -7.43,
                        Ea = (57296, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.1, 1, 10], 'atm'),
                arrhenius = [
                    Arrhenius(A=(7.2e+28, '1/s'), n=-7.77, Ea=(50757.9, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(3.2e+31, '1/s'), n=-6.22, Ea=(52318, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (5.1e+33, 'cm^3/(mol*s)'),
                        n = -6.52,
                        Ea = (54215.3, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 102,
    label = "H2NN + O2 <=> NH2 + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(5958, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 103,
    label = "H2NN + H <=> N2H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+10, 'cm^3/(mol*s)'),
        n = 0.97,
        Ea = (4468, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 104,
    label = "H2NN + H <=> NNH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.8e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(-894, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 105,
    label = "H2NN + O <=> NH2 + NO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.2e+09, 'cm^3/(mol*s)'),
        n = 1.03,
        Ea = (2701, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 106,
    label = "H2NN + O <=> OH + NNH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.3e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(-894, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 107,
    label = "H2NN + OH <=> NH2NO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 108,
    label = "H2NN + OH <=> NNH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+06, 'cm^3/(mol*s)'), n=2, Ea=(-1192, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 109,
    label = "H2NN + CH3 <=> H2CNNH2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(830000, 'cm^3/(mol*s)'), n=1.93, Ea=(6494, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 110,
    label = "H2NN + CH3 <=> CH3NNH + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(830000, 'cm^3/(mol*s)'), n=1.93, Ea=(6494, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 111,
    label = "H2NN + CH3 <=> CH4 + NNH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+06, 'cm^3/(mol*s)'), n=1.87, Ea=(129, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 112,
    label = "H2NN + NH2 <=> HNNNH2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.9e+06, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (-1331, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 113,
    label = "H2NN + NH2 <=> NH3 + NNH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (-1152, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 114,
    label = "H2NN + HO2 <=> NH2NO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(660000, 'cm^3/(mol*s)'), n=1.94, Ea=(7050, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 115,
    label = "H2NN + HO2 <=> NNH + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(29000, 'cm^3/(mol*s)'), n=2.69, Ea=(-1599, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 116,
    label = "N2H3 <=> N2H2 + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(2.3e+43, 's^-1'), n=-9.55, Ea=(64471, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.6e+47, 's^-1'), n=-10.38, Ea=(69012, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.8e+45, 's^-1'), n=-9.39, Ea=(70144, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 117,
    label = "N2H3 + H <=> N2H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 118,
    label = "N2H3 + O <=> NH2 + HNO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 119,
    label = "N2H3 + O <=> NH2NO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 120,
    label = "N2H3 + O <=> N2H2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(-645, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 121,
    label = "N2H3 + OH <=> N2H2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+06, 'cm^3/(mol*s)'), n=2, Ea=(-1192, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 122,
    label = "N2H3 + OH <=> H2NN + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 123,
    label = "N2H3 + CH3 <=> N2H2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(820000, 'cm^3/(mol*s)'), n=1.87, Ea=(1817, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 124,
    label = "N2H3 + CH3 <=> H2NN + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 125,
    label = "N2H3 + NH2 <=> N2H2 + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (920000, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (-1152, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 126,
    label = "N2H3 + NH2 <=> H2NN + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 127,
    label = "N2H3 + HO2 <=> H2NNHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 128,
    label = "N2H3 + HO2 <=> N2H2 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(29000, 'cm^3/(mol*s)'), n=2.69, Ea=(-1599, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 129,
    label = "N2H3 + HO2 <=> N2H4 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(920000, 'cm^3/(mol*s)'), n=1.94, Ea=(2125, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 130,
    label = "N2H4 <=> H2NN + H2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(4e+44, 's^-1'), n=-9.85, Ea=(71357, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.3e+39, 's^-1'), n=-8.35, Ea=(69310, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.5e+39, 's^-1'), n=-8.19, Ea=(69668, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 131,
    label = "N2H4 + H <=> N2H3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.6e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(4836, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 132,
    label = "N2H4 + O <=> N2H3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.7e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(2850, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 133,
    label = "N2H4 + OH <=> N2H3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.8e+06, 'cm^3/(mol*s)'), n=2, Ea=(-645, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 134,
    label = "N2H4 + CH3 <=> N2H3 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (5322, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 135,
    label = "N2H4 + NH2 <=> N2H3 + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.7e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (1628, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 136,
    label = "NO + C(T) <=> CO + N",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 137,
    label = "NO + C(T) <=> CN + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 138,
    label = "NO + HCCO <=> HCNO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(695, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 139,
    label = "NO + HCCO <=> HCN + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(695, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 140,
    label = "NO2 + H <=> NO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+14, 'cm^3/(mol*s)'), n=0, Ea=(357, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 141,
    label = "NO2 + O <=> NO + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-238, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 142,
    label = "NO2 <=> NO + O",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(5.7e+15, 'cm^3/(mol*s)'), n=0, Ea=(59954, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 143,
    label = "NO2 + NH2 <=> N2O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+16, 'cm^3/(mol*s)'),
        n = -1.44,
        Ea = (258, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 144,
    label = "NO2 + NH2 <=> NH2O + NO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.6e+16, 'cm^3/(mol*s)'),
        n = -1.44,
        Ea = (258, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 145,
    label = "NO2 + CH3 <=> NO + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 146,
    label = "N2O + OH <=> N2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.013, 'cm^3/(mol*s)'), n=4.72, Ea=(36540, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 147,
    label = "HNO <=> H + NO",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(2.6e+16, 'cm^3/(mol*s)'), n=0, Ea=(48654, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 148,
    label = "HNO + HNO <=> N2O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.5e+08, 'cm^3/(mol*s)'), n=0, Ea=(3078, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 149,
    label = "HNO + OH <=> NO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+07, 'cm^3/(mol*s)'),
        n = 1.88,
        Ea = (-953, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 150,
    label = "HNO + H <=> H2 + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.5e+11, 'cm^3/(mol*s)'), n=0.72, Ea=(655, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 152,
    label = "HNO + O <=> OH + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.5e+11, 'cm^3/(mol*s)'), n=0.72, Ea=(655, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 153,
    label = "HNO + NH2 <=> NH3 + NO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (920000, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (-1152, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 154,
    label = "HNO + NO <=> N2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(29570, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 155,
    label = "HNO + O2 <=> NO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(15887, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 156,
    label = "HNO + CH3 <=> NO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (820000, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (29252, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 157,
    label = "NH2O <=> HNO + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (2.8e+24, 'cm^3/(mol*s)'),
            n = -2.83,
            Ea = (64879, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 158,
    label = "NH2O <=> HNOH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(8.2e+25, 's^-1'), n=-4.94, Ea=(43796, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.3e+27, 's^-1'), n=-4.99, Ea=(43984, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.6e+28, 's^-1'), n=-5.06, Ea=(44769, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 159,
    label = "NH2O + H <=> NH2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 160,
    label = "NH2O + H <=> HNO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.8e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(1559, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 161,
    label = "NH2O + O <=> HNO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.3e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(487, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 162,
    label = "NH2O + OH <=> HNO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+06, 'cm^3/(mol*s)'), n=2, Ea=(-1192, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 163,
    label = "NH2O + CH3 <=> CH3O + NH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 164,
    label = "NH2O + CH3 <=> CH4 + HNO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (2959, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 165,
    label = "NH2O + NH2 <=> HNO + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (-1152, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 166,
    label = "NH2O + HO2 <=> HNO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(29000, 'cm^3/(mol*s)'), n=2.69, Ea=(-1599, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 167,
    label = "NH2O + HO2 <=> O2 + NH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(29000, 'cm^3/(mol*s)'), n=2.69, Ea=(-1599, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 168,
    label = "HNOH <=> H + HNO",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (2e+24, 'cm^3/(mol*s)'),
            n = -2.84,
            Ea = (58901, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 169,
    label = "HNOH + H <=> NH2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 170,
    label = "HNOH + H <=> HNO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.8e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(377, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 171,
    label = "HNOH + O <=> HNO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 172,
    label = "HNOH + OH <=> HNO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+06, 'cm^3/(mol*s)'), n=2, Ea=(-1192, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 173,
    label = "HNOH + CH3 <=> CH3NH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 174,
    label = "HNOH + CH3 <=> CH4 + HNO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (2095, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 175,
    label = "HNOH + NH2 <=> N2H3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.7e+06, 'cm^3/(mol*s)'), n=1.82, Ea=(715, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 176,
    label = "HNOH + NH2 <=> H2NN + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.6e+19, 'cm^3/(mol*s)'),
        n = -1.94,
        Ea = (1926, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 177,
    label = "HNOH + NH2 <=> HNO + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (-1152, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 178,
    label = "HNOH + HO2 <=> HONHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 179,
    label = "HNOH + HO2 <=> HNO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(29000, 'cm^3/(mol*s)'), n=2.69, Ea=(-1599, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 180,
    label = "HNOH + HO2 <=> NH2OH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(29000, 'cm^3/(mol*s)'), n=2.69, Ea=(-1599, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 181,
    label = "HNOO <=> OH + NO",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.5e+36, 'cm^3/(mol*s)'),
            n = -6.18,
            Ea = (31119, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 182,
    label = "HONO <=> OH + NO",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (2e+31, 'cm^3/(mol*s)'),
            n = -4.56,
            Ea = (51146, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 183,
    label = "HONO + H <=> H2 + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+08, 'cm^3/(mol*s)'), n=1.55, Ea=(6613, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 184,
    label = "HONO + H <=> H2O + NO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.1e+06, 'cm^3/(mol*s)'),
        n = 1.89,
        Ea = (3843, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 185,
    label = "HONO + H <=> OH + HNO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.6e+10, 'cm^3/(mol*s)'),
        n = 0.86,
        Ea = (4965, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 186,
    label = "HONO + O <=> OH + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(3028, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 187,
    label = "HONO + OH <=> H2O + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+06, 'cm^3/(mol*s)'), n=2, Ea=(-596, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 188,
    label = "HONO + CH3 <=> NO2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(810000, 'cm^3/(mol*s)'), n=1.87, Ea=(5501, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 189,
    label = "HONO + NH2 <=> NO2 + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(920000, 'cm^3/(mol*s)'), n=1.94, Ea=(1916, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 190,
    label = "HNO2 <=> HONO",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(7.1e+27, 's^-1'), n=-5.4, Ea=(52539, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.3e+29, 's^-1'), n=-5.47, Ea=(52817, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2e+30, 's^-1'), n=-5.5, Ea=(53691, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 191,
    label = "HNO2 + H <=> H2 + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(4160, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 192,
    label = "HNO2 + O <=> OH + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(2363, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 193,
    label = "HNO2 + OH <=> H2O + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+06, 'cm^3/(mol*s)'), n=2, Ea=(-794, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 194,
    label = "HNO2 + CH3 <=> NO2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(810000, 'cm^3/(mol*s)'), n=1.87, Ea=(4836, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 195,
    label = "HNO2 + NH2 <=> NO2 + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(920000, 'cm^3/(mol*s)'), n=1.94, Ea=(874, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 196,
    label = "HCN <=> HNC",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.5e+23, 's^-1'), n=-4.2, Ea=(49459, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.9e+24, 's^-1'), n=-4.23, Ea=(49578, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.3e+25, 's^-1'), n=-4.34, Ea=(50194, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 198,
    label = "OH + HCN <=> HNCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4400, 'cm^3/(mol*s)'), n=2.26, Ea=(6395, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 199,
    label = "OH + HCN <=> HOCN + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+06, 'cm^3/(mol*s)'),
        n = 2.03,
        Ea = (13365, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 200,
    label = "OH + HCN <=> NH2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(160, 'cm^3/(mol*s)'), n=2.56, Ea=(8996, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 201,
    label = "OH + HCN <=> NCHOH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.7e+29, 'cm^3/(mol*s)'),
                n = -6.31,
                Ea = (5127, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.8e+30, 'cm^3/(mol*s)'),
                n = -6.37,
                Ea = (5345, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.1e+32, 'cm^3/(mol*s)'),
                n = -6.53,
                Ea = (6239, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 202,
    label = "HCN + O <=> NH(T) + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.4e+08, 'cm^3/(mol*s)'),
        n = 1.21,
        Ea = (7487, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 203,
    label = "HCN + O <=> NCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+08, 'cm^3/(mol*s)'), n=1.47, Ea=(7586, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 204,
    label = "HCN + O <=> CN + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.2e+10, 'cm^3/(mol*s)'),
        n = 0.4,
        Ea = (20663, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 205,
    label = "O + HNC <=> NH(T) + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(2184, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 206,
    label = "OH + HNC <=> HNCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(3694, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 207,
    label = "HNC + O2 <=> HNCO + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+12, 'cm^3/(mol*s)'),
        n = 0.01,
        Ea = (4111, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 208,
    label = "HNC + O2 <=> NH(T) + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+19, 'cm^3/(mol*s)'),
        n = -2.25,
        Ea = (1777, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 209,
    label = "CN + H2 <=> HCN + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.6e+08, 'cm^3/(mol*s)'),
        n = 1.55,
        Ea = (2999, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 210,
    label = "CN + H2O <=> HCN + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(7447, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 211,
    label = "CN + O <=> CO + N",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 212,
    label = "CN + O2 <=> NCO + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 213,
    label = "CN + OH <=> NCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 214,
    label = "CN + HCN <=> NCCN + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+07, 'cm^3/(mol*s)'),
        n = 1.71,
        Ea = (1529, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 215,
    label = "CN + N2O <=> NCN + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(7169, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 216,
    label = "CN + NO2 <=> NCO + NO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.2e+15, 'cm^3/(mol*s)'),
        n = -0.75,
        Ea = (348, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 217,
    label = "CN + CH4 <=> HCN + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(120000, 'cm^3/(mol*s)'), n=2.64, Ea=(-159, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 218,
    label = "CN + NH3 <=> HCN + NH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(-357, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 219,
    label = "H2CN <=> HCN + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.3e+29, 's^-1'), n=-6.03, Ea=(29896, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6e+31, 's^-1'), n=-6.46, Ea=(32111, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.5e+29, 's^-1'), n=-5.46, Ea=(32549, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 220,
    label = "H2CN + HO2 <=> CH2NO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 221,
    label = "H2CN + HO2 <=> HCN + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14000, 'cm^3/(mol*s)'), n=2.69, Ea=(-1609, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 222,
    label = "H2CN + HO2 <=> H2CNH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14000, 'cm^3/(mol*s)'), n=2.69, Ea=(-1609, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 223,
    label = "H2CN + O2 <=> CH2O + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=0, Ea=(5958, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 224,
    label = "H2CN + CH3 <=> HCN + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (810000, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1112, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 225,
    label = "H2CN + OH <=> HCN + H2O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (2.1e+17, 'cm^3/(mol*s)'),
                n = -1.68,
                Ea = (318, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.5e+19, 'cm^3/(mol*s)'),
                n = -2.18,
                Ea = (2166, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9.5e+21, 'cm^3/(mol*s)'),
                n = -2.91,
                Ea = (5633, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 226,
    label = "H2CN + N <=> N2 + CH2(T)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(397, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 227,
    label = "H2CN + H <=> HCN + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(-894, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 228,
    label = "H2CN + NH2 <=> HCN + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (920000, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (-1152, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 229,
    label = "H2CN + O <=> HCN + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(-894, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 230,
    label = "H2CN + O <=> HNCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 231,
    label = "H2CN + O <=> HCNO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 232,
    label = "HCNH <=> HCN + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(7.7e+25, 's^-1'), n=-5.2, Ea=(21987, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.1e+28, 's^-1'), n=-5.69, Ea=(24272, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.2e+26, 's^-1'), n=-4.77, Ea=(24819, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 233,
    label = "HCNH + H <=> H2CN + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 234,
    label = "HCNH + H <=> HCN + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(-894, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 235,
    label = "HCNH + O <=> HNCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 236,
    label = "HCNH + O <=> HCN + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(-894, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 237,
    label = "HCNH + OH <=> HCN + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+06, 'cm^3/(mol*s)'), n=2, Ea=(-1192, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 238,
    label = "HCNH + CH3 <=> HCN + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (820000, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1112, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 239,
    label = "HCNN + O2 <=> H + CO2 + N2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 240,
    label = "HCNN + O2 <=> HCO + N2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 241,
    label = "H2CNH + H <=> H2CN + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(7318, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 242,
    label = "H2CNH + O <=> H2CN + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(4627, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 243,
    label = "H2CNH + OH <=> H2CN + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+06, 'cm^3/(mol*s)'), n=2, Ea=(-89, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 244,
    label = "H2CNH + CH3 <=> H2CN + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(820000, 'cm^3/(mol*s)'), n=1.87, Ea=(7119, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 245,
    label = "H2CNH + NH2 <=> H2CN + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(920000, 'cm^3/(mol*s)'), n=1.94, Ea=(4438, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 246,
    label = "H2CNH + H <=> HCNH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(6126, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 247,
    label = "H2CNH + O <=> HCNH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.2e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(5402, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 248,
    label = "H2CNH + OH <=> HCNH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+06, 'cm^3/(mol*s)'), n=2, Ea=(457, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 249,
    label = "H2CNH + CH3 <=> HCNH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(530000, 'cm^3/(mol*s)'), n=1.87, Ea=(9681, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 250,
    label = "H2CNH + NH2 <=> HCNH + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (6087, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 251,
    label = "H2CNH + O <=> CH2O + NH(T)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+06, 'cm^3/(mol*s)'), n=2.08, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 252,
    label = "CH3NH <=> H2CNH + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.6e+36, 's^-1'), n=-7.92, Ea=(36344, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.3e+42, 's^-1'), n=-9.24, Ea=(41341, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.3e+44, 's^-1'), n=-9.51, Ea=(45246, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 253,
    label = "CH3NH + H <=> H2CNH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.2e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(-894, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 254,
    label = "CH3NH + O <=> H2CNH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(-894, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 255,
    label = "CH3NH + OH <=> H2CNH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.6e+06, 'cm^3/(mol*s)'), n=2, Ea=(-1192, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 256,
    label = "CH3NH + CH3 <=> H2CNH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1112, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 257,
    label = "CH2NH2 <=> H2CNH + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.1e+45, 's^-1'), n=-10.24, Ea=(47819, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.4e+48, 's^-1'), n=-10.82, Ea=(52042, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.2e+46, 's^-1'), n=-9.95, Ea=(53532, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 258,
    label = "CH2NH2 + O2 <=> H2CNH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+22, 'cm^3/(mol*s)'), n=-3.09, Ea=(6752, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 259,
    label = "CH2NH2 + O2 <=> NH2 + CH2O + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+18, 'cm^3/(mol*s)'),
        n = -1.59,
        Ea = (30175, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 260,
    label = "CH2NH2 + H <=> H2CNH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(-894, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 261,
    label = "CH2NH2 + O <=> CH2O + NH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 262,
    label = "CH2NH2 + O <=> H2CNH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.3e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(-894, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 263,
    label = "CH2NH2 + OH <=> CH2OH + NH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 264,
    label = "CH2NH2 + OH <=> H2CNH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+06, 'cm^3/(mol*s)'), n=2, Ea=(-1192, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 265,
    label = "CH2NH2 + CH3 <=> C2H5 + NH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(2701, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 266,
    label = "CH2NH2 + CH3 <=> H2CNH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-626, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 267,
    label = "CH3NH2 + H <=> CH2NH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.6e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(5461, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 268,
    label = "CH3NH2 + O <=> CH2NH2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(5193, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 269,
    label = "CH3NH2 + OH <=> CH2NH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.6e+06, 'cm^3/(mol*s)'), n=2, Ea=(238, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 270,
    label = "CH3NH2 + CH3 <=> CH2NH2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (9165, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 271,
    label = "CH3NH2 + NH2 <=> CH2NH2 + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (5491, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 272,
    label = "CH3NH2 + H <=> CH3NH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.8e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(9701, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 273,
    label = "CH3NH2 + O <=> CH3NH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.3e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(6345, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 274,
    label = "CH3NH2 + OH <=> CH3NH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+06, 'cm^3/(mol*s)'), n=2, Ea=(447, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 275,
    label = "CH3NH2 + CH3 <=> CH3NH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (8837, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 276,
    label = "CH3NH2 + NH2 <=> CH3NH + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (7139, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 277,
    label = "NCCN <=> CN + CN",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.6e+34, 'cm^3/(mol*s)'),
            n = -4.32,
            Ea = (130005, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 279,
    label = "NCCN + O <=> NCO + CN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(8877, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 280,
    label = "NCCN + OH <=> HOCN + CN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(18985, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 281,
    label = "NCO + NO <=> CO2 + N2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.8e+17, 'cm^3/(mol*s)'),
        n = -1.73,
        Ea = (765, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 282,
    label = "NCO + NO <=> N2O + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.2e+17, 'cm^3/(mol*s)'),
        n = -1.73,
        Ea = (765, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 283,
    label = "NCO <=> N + CO",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(3.3e+14, 'cm^3/(mol*s)'), n=0, Ea=(54016, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 284,
    label = "NCO + H2 <=> HNCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(760, 'cm^3/(mol*s)'), n=3, Ea=(3972, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 285,
    label = "NCO + O <=> NO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 286,
    label = "NCO + O <=> N + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+12, 'cm^3/(mol*s)'), n=0, Ea=(2502, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 287,
    label = "NCO + H <=> NH(T) + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 288,
    label = "NCO + N <=> N2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 289,
    label = "NCO + OH <=> HNCO + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(78000, 'cm^3/(mol*s)'), n=2.27, Ea=(-993, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 290,
    label = "NCO + OH <=> HON(T) + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.3e+12, 'cm^3/(mol*s)'),
        n = -0.07,
        Ea = (5124, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 291,
    label = "NCO + OH <=> H + CO + NO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.3e+12, 'cm^3/(mol*s)'),
        n = -0.05,
        Ea = (18032, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 292,
    label = "NCO + NO2 <=> CO2 + N2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(-874, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 293,
    label = "NCO + NO2 <=> CO + NO + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.1e+11, 'cm^3/(mol*s)'), n=0, Ea=(-874, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 294,
    label = "NCO + CH4 <=> HNCO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(8122, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 296,
    label = "HCNO <=> HCN + O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(2e+30, 's^-1'), n=-6.03, Ea=(60736, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.2e+31, 's^-1'), n=-6.12, Ea=(61212, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.9e+31, 's^-1'), n=-5.85, Ea=(61938, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 297,
    label = "HCNO + H <=> HNCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.1e+15, 'cm^3/(mol*s)'),
        n = -0.69,
        Ea = (2850, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 298,
    label = "HCNO + H <=> HCN + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.7e+11, 'cm^3/(mol*s)'),
        n = 0.18,
        Ea = (2115, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 299,
    label = "HCNO + H <=> NH2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+14, 'cm^3/(mol*s)'),
        n = -0.75,
        Ea = (2889, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 300,
    label = "HCNO + H <=> HOCN + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+11, 'cm^3/(mol*s)'),
        n = -0.19,
        Ea = (2482, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 301,
    label = "HCNO + O <=> HCO + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 302,
    label = "HCNO + OH <=> HCOH + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 304,
    label = "HOCN + H <=> HNCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.1e+08, 'cm^3/(mol*s)'),
        n = 0.84,
        Ea = (1916, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 305,
    label = "HOCN + H <=> NH2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+08, 'cm^3/(mol*s)'),
        n = 0.61,
        Ea = (2075, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 306,
    label = "HOCN + H <=> H2 + NCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(6613, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 307,
    label = "HOCN + O <=> OH + NCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(4131, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 308,
    label = "HOCN + OH <=> H2O + NCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+06, 'cm^3/(mol*s)'), n=2, Ea=(-248, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 309,
    label = "HOCN + CH3 <=> CH4 + NCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(820000, 'cm^3/(mol*s)'), n=1.87, Ea=(6613, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 310,
    label = "HOCN + NH2 <=> NCO + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (920000, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (36443, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 311,
    label = "HNCO <=> NH(T) + CO",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.3e+16, 'cm^3/(mol*s)'), n=0, Ea=(84320, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 312,
    label = "HNCO + H <=> NH2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(36000, 'cm^3/(mol*s)'), n=2.49, Ea=(2343, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 313,
    label = "HNCO + O <=> HNO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+06, 'cm^3/(mol*s)'), n=2.08, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 314,
    label = "HNCO + O <=> NH(T) + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+06, 'cm^3/(mol*s)'), n=2.08, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 315,
    label = "HNCO + OH <=> NH2 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.3e+10, 'cm^3/(mol*s)'),
        n = -0.06,
        Ea = (11637, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 316,
    label = "HNCO + OH <=> NCO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.2e+10, 'cm^3/(mol*s)'),
        n = -0.03,
        Ea = (17555, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 320,
    label = "HNCO + NH2 <=> NCO + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(8936, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 321,
    label = "CH2NO <=> HNCO + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(6.9e+41, 's^-1'), n=-9.3, Ea=(51704, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.3e+42, 's^-1'), n=-9.11, Ea=(53840, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.7e+38, 's^-1'), n=-7.64, Ea=(53582, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 322,
    label = "CH2NO + O2 <=> CH2O + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+15, 'cm^3/(mol*s)'),
        n = -1.01,
        Ea = (20117, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 323,
    label = "CH2NO + H <=> CH3 + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 324,
    label = "CH2NO + H <=> HCNO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.8e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(-894, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 325,
    label = "CH2NO + O <=> CH2O + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 326,
    label = "CH2NO + O <=> HCNO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.3e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(-894, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 327,
    label = "CH2NO + OH <=> CH2OH + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 328,
    label = "CH2NO + OH <=> HCNO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+06, 'cm^3/(mol*s)'), n=2, Ea=(-1192, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 329,
    label = "CH2NO + CH3 <=> C2H5 + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 330,
    label = "CH2NO + CH3 <=> HCNO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1112, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 331,
    label = "CH2NO + NH2 <=> CH2NH2 + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 332,
    label = "CH2NO + NH2 <=> HCNO + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (-1152, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 333,
    label = "CH3NO + H <=> CH2NO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.4e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(377, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 334,
    label = "CH3NO + O <=> CH2NO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.3e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(3614, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 335,
    label = "CH3NO + OH <=> CH2NO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.6e+06, 'cm^3/(mol*s)'), n=2, Ea=(-1192, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 336,
    label = "CH3NO + CH3 <=> CH2NO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(790000, 'cm^3/(mol*s)'), n=1.87, Ea=(5412, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 337,
    label = "CH3NO + NH2 <=> CH2NO + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (1072, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 338,
    label = "CH3NO + H <=> CH3 + HNO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(2780, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 339,
    label = "CH3NO + O <=> CH3 + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+06, 'cm^3/(mol*s)'), n=2.08, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 340,
    label = "CH3NO + OH <=> CH3 + HONO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(993, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 341,
    label = "HON(S) <=> NO + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (5.1e+19, 'cm^3/(mol*s)'),
            n = -1.73,
            Ea = (16036, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 342,
    label = "HON(S) + H <=> HNO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 343,
    label = "HON(S) + H <=> OH + NH(S)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 344,
    label = "HON(S) + O <=> OH + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 345,
    label = "HON(S) + OH <=> HONO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 346,
    label = "HON(S) + O2 <=> HONO + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(4965, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 347,
    label = "HCOH <=> CH2O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(3.5e+17, 's^-1'), n=-2.86, Ea=(8882, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.1e+19, 's^-1'), n=-3.07, Ea=(9538, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.8e+21, 's^-1'), n=-3.32, Ea=(10859, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 348,
    label = "NH2OH + H <=> HNOH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.8e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(6246, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 349,
    label = "NH2OH + H <=> NH2O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(5064, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 350,
    label = "NH2OH + O <=> HNOH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.3e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(3863, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 351,
    label = "NH2OH + O <=> NH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(3009, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 352,
    label = "NH2OH + OH <=> HNOH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+06, 'cm^3/(mol*s)'), n=2, Ea=(-328, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 353,
    label = "NH2OH + OH <=> NH2O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+06, 'cm^3/(mol*s)'), n=2, Ea=(-596, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 354,
    label = "NH2OH + CH3 <=> HNOH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (6345, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 355,
    label = "NH2OH + CH3 <=> NH2O + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(820000, 'cm^3/(mol*s)'), n=1.87, Ea=(5491, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 356,
    label = "NH2OH + NH2 <=> HNOH + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (3227, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 357,
    label = "NH2OH + NH2 <=> NH2O + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(920000, 'cm^3/(mol*s)'), n=1.94, Ea=(1887, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 358,
    label = "NH2OH + HO2 <=> HNOH + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(29000, 'cm^3/(mol*s)'), n=2.69, Ea=(9552, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 359,
    label = "NH2OH + HO2 <=> NH2O + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14000, 'cm^3/(mol*s)'), n=2.69, Ea=(6414, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 360,
    label = "NH2NO <=> N2 + H2O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(4.1e+33, 's^-1'), n=-7.78, Ea=(35172, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.1e+34, 's^-1'), n=-7.11, Ea=(36284, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.9e+31, 's^-1'), n=-5.91, Ea=(36175, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 361,
    label = "NH2NO + H <=> HNNO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.8e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(7407, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 362,
    label = "NH2NO + O <=> HNNO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.3e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(4697, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 363,
    label = "NH2NO + OH <=> HNNO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+06, 'cm^3/(mol*s)'), n=2, Ea=(-70, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 364,
    label = "NH2NO + CH3 <=> HNNO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (7179, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 365,
    label = "NH2NO + NH2 <=> HNNO + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (4538, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 366,
    label = "NH2NO + HO2 <=> HNNO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(29000, 'cm^3/(mol*s)'), n=2.69, Ea=(12620, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 367,
    label = "H2NNHO <=> NH2 + HNO",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(2.7e+39, 's^-1'), n=-8.74, Ea=(41620, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.4e+40, 's^-1'), n=-8.73, Ea=(41610, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.2e+41, 's^-1'), n=-8.64, Ea=(41580, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 368,
    label = "H2NNHO + H <=> HNNHO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.8e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(-894, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 369,
    label = "H2NNHO + O <=> HNNHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.3e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(-894, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 370,
    label = "H2NNHO + OH <=> HNNHO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+06, 'cm^3/(mol*s)'), n=2, Ea=(-1192, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 371,
    label = "H2NNHO + CH3 <=> HNNHO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+06, 'cm^3/(mol*s)'), n=1.87, Ea=(377, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 372,
    label = "H2NNHO + NH2 <=> HNNHO + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (-1152, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index = 373,
    label = "H2NNHO + HO2 <=> HNNHO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(29000, 'cm^3/(mol*s)'), n=2.69, Ea=(-1599, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

