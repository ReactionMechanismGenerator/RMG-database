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
    index        = 1,
    reactant1 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    reactant2 = 
"""
N2
multiplicity 1
1 N U0 L1 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    product1 = 
"""
N_(Q)
multiplicity 4
1 N U3 L1 E0 
""",
    product2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (200000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (76774, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 2,
    reactant1 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    product1 = 
"""
N_(Q)
multiplicity 4
1 N U3 L1 E0 
""",
    product2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1400000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (148345, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 3,
    reactant1 = 
"""
N2O
multiplicity 1
1 N U0 L0 E+1 {2,D} {3,D}
2 N U0 L2 E-1 {1,D}
3 O U0 L2 E0  {1,D}
""",
    product1 = 
"""
N2
multiplicity 1
1 N U0 L1 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (570000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (56061, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 4,
    reactant1 = 
"""
N2O
multiplicity 1
1 N U0 L0 E+1 {2,D} {3,D}
2 N U0 L2 E-1 {1,D}
3 O U0 L2 E0  {1,D}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
N2
multiplicity 1
1 N U0 L1 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1400000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (10803, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 5,
    reactant1 = 
"""
N2O
multiplicity 1
1 N U0 L0 E+1 {2,D} {3,D}
2 N U0 L2 E-1 {1,D}
3 O U0 L2 E0  {1,D}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (29000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (23135, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 6,
    reactant1 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(3.6e+16, 'cm^3/(mol*s)'), n=0, Ea=(93733, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 7,
    reactant1 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (540000, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (9910, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 8,
    reactant1 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000.0, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (953, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 9,
    reactant1 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9400000.0, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (6454, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 10,
    reactant1 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
NH_(S)
multiplicity 1
1 N U2 L1 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (480000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (7934, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 11,
    reactant1 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 O U1 L2 E0  {1,S}
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    product1 = 
"""
NO2
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 O U1 L2 E0  {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-477, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 12,
    reactant1 = 
"""
N2O
multiplicity 1
1 N U0 L0 E+1 {2,D} {3,D}
2 N U0 L2 E-1 {1,D}
3 O U0 L2 E0  {1,D}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
HNNO
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 O U1 L2 E0  {2,S}
""",
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
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 13,
    reactant1 = 
"""
N2O
multiplicity 1
1 N U0 L0 E+1 {2,D} {3,D}
2 N U0 L2 E-1 {1,D}
3 O U0 L2 E0  {1,D}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
N2
multiplicity 1
1 N U0 L1 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (220000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (16741, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 14,
    reactant1 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    reactant2 = 
"""
N2O
multiplicity 1
1 N U0 L0 E+1 {2,D} {3,D}
2 N U0 L2 E-1 {1,D}
3 O U0 L2 E0  {1,D}
""",
    product1 = 
"""
NH_(T)
multiplicity 3
1 N U2 L1 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.5e+20, 'cm^3/(mol*s)'),
        n = -1.26,
        Ea = (35349, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 15,
    reactant1 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    reactant2 = 
"""
N2O
multiplicity 1
1 N U0 L0 E+1 {2,D} {3,D}
2 N U0 L2 E-1 {1,D}
3 O U0 L2 E0  {1,D}
""",
    product1 = 
"""
NNH
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 N U1 L1 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+19, 'cm^3/(mol*s)'),
        n = -1.26,
        Ea = (47065, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 16,
    reactant1 = 
"""
NH_(T)
multiplicity 3
1 N U2 L1 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    product1 = 
"""
N2
multiplicity 1
1 N U0 L1 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+17, 'cm^3/(mol*s)'),
        n = -1.49,
        Ea = (1311, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 18,
    reactant1 = 
"""
NH_(T)
multiplicity 3
1 N U2 L1 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    product1 = 
"""
NNH
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 N U1 L1 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (170000000000000.0, 'cm^3/(mol*s)'),
        n = -0.2,
        Ea = (12193, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 19,
    reactant1 = 
"""
NH_(T)
multiplicity 3
1 N U2 L1 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
HNOO_(T)
multiplicity 3
1 N U1 L1 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 O U1 L2 E0  {2,S}
""",
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
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 20,
    reactant1 = 
"""
NH_(T)
multiplicity 3
1 N U2 L1 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (76000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1529, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 21,
    reactant1 = 
"""
NH_(T)
multiplicity 3
1 N U2 L1 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product2 = 
"""
NO2
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (23000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2482, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 22,
    reactant1 = 
"""
NH_(T)
multiplicity 3
1 N U2 L1 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
HNO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (460000, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (6494, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 23,
    reactant1 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
NH2O
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 O U1 L2 E0  {1,S}
""",
    product2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (250000000000.0, 'cm^3/(mol*s)'),
        n = 0.48,
        Ea = (29570, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 24,
    reactant1 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
HNO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (62000000.0, 'cm^3/(mol*s)'),
        n = 1.23,
        Ea = (35081, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 25,
    reactant1 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
NH2O
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 O U1 L2 E0  {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (25000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 26,
    reactant1 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (920000, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (-1152, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 27,
    reactant1 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
HNO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (46000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 28,
    reactant1 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
NH_(T)
multiplicity 3
1 N U2 L1 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 29,
    reactant1 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
NH2OH
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
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
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 30,
    reactant1 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
NH_(S)
multiplicity 1
1 N U2 L1 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2400000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (50, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 31,
    reactant1 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
N2H4
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
""",
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
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 32,
    reactant1 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
H2NN
multiplicity 1
1 N U0 L0 E+1 {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U0 L2 E-1 {1,D}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
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
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 33,
    reactant1 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
N2H3
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (920000000000.0, 'cm^3/(mol*s)'),
                n = -0.01,
                Ea = (10014, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1200000000000.0, 'cm^3/(mol*s)'),
                n = -0.03,
                Ea = (10084, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4700000000000.0, 'cm^3/(mol*s)'),
                n = -0.2,
                Ea = (10620, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 34,
    reactant1 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
NH_(T)
multiplicity 3
1 N U2 L1 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (9929, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 35,
    reactant1 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    product1 = 
"""
N2
multiplicity 1
1 N U0 L1 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4700000000000.0, 'cm^3/(mol*s)'),
        n = -0.25,
        Ea = (-1201, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 36,
    reactant1 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    product1 = 
"""
NNH
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 N U1 L1 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (35000000000.0, 'cm^3/(mol*s)'),
        n = 0.34,
        Ea = (-765, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 37,
    reactant1 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    product1 = 
"""
NH2NO
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
""",
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
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 38,
    reactant1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    reactant3 = 
"""
N2
multiplicity 1
1 N U0 L1 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    product1 = 
"""
CH3NO
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U0 L1 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U0 L2 E0  {2,D}
""",
    product2 = 
"""
N2
multiplicity 1
1 N U0 L1 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^6/(mol^2*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 39,
    reactant1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    product1 = 
"""
CH3NO
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U0 L1 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U0 L2 E0  {2,D}
""",
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
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 40,
    reactant1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    product1 = 
"""
H2CN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U1 L1 E0  {1,D}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2200000000.0, 'cm^3/(mol*s)'),
        n = 0.75,
        Ea = (11717, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 41,
    reactant1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    product1 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (490000000.0, 'cm^3/(mol*s)'),
        n = 0.46,
        Ea = (12392, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 42,
    reactant1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
N_(Q)
multiplicity 4
1 N U3 L1 E0 
""",
    product1 = 
"""
H2CN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U1 L1 E0  {1,D}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (610000000000000.0, 'cm^3/(mol*s)'),
        n = -0.31,
        Ea = (288, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 43,
    reactant1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
N_(Q)
multiplicity 4
1 N U3 L1 E0 
""",
    product1 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3700000000000.0, 'cm^3/(mol*s)'),
        n = 0.15,
        Ea = (-89, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 44,
    reactant1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
N_(Q)
multiplicity 4
1 N U3 L1 E0 
""",
    product1 = 
"""
HCNH
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (120000000000.0, 'cm^3/(mol*s)'),
        n = 0.52,
        Ea = (-367, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 45,
    reactant1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3NH2
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U0 L1 E0  {1,S} {6,S} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
""",
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
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 46,
    reactant1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2NH2
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (11000000000000.0, 'cm^3/(mol*s)'),
                n = -0.13,
                Ea = (9905, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (140000000000000.0, 'cm^3/(mol*s)'),
                n = -0.43,
                Ea = (11107, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7400000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (12071, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 47,
    reactant1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3NH
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U1 L1 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (12000000000000.0, 'cm^3/(mol*s)'),
                n = -0.15,
                Ea = (16144, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (44000000000000.0, 'cm^3/(mol*s)'),
                n = -0.31,
                Ea = (16641, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (140000000000000.0, 'cm^3/(mol*s)'),
                n = -0.42,
                Ea = (17863, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 48,
    reactant1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
H2CNH
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 N U0 L1 E0  {1,D} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (210000000000.0, 'cm^3/(mol*s)'),
                n = -0.1,
                Ea = (19095, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (480000000000.0, 'cm^3/(mol*s)'),
                n = -0.2,
                Ea = (19403, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2900000000000.0, 'cm^3/(mol*s)'),
                n = -0.4,
                Ea = (20506, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 49,
    reactant1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
NH_(S)
multiplicity 1
1 N U2 L1 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2800000.0, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (9205, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 50,
    reactant1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2_(T)
multiplicity 3
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1600000.0, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (7566, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 51,
    reactant1 = 
"""
CH2_(T)
multiplicity 3
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
N2
multiplicity 1
1 N U0 L1 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    product1 = 
"""
CH2NN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U0 L0 E+1 {1,D} {5,D}
5 N U0 L2 E-1 {4,D}
""",
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
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 52,
    reactant1 = 
"""
CH2_(T)
multiplicity 3
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
N2
multiplicity 1
1 N U0 L1 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    product1 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
NH_(T)
multiplicity 3
1 N U2 L1 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (73954, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 53,
    reactant1 = 
"""
CH2_(T)
multiplicity 3
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    product1 = 
"""
HCNO
multiplicity 1
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L0 E+1 {1,T} {4,S}
3 H U0 L0 E0  {1,S}
4 O U0 L3 E-1 {2,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (38000000000000.0, 'cm^3/(mol*s)'),
        n = -0.36,
        Ea = (576, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 54,
    reactant1 = 
"""
CH2_(T)
multiplicity 3
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    product1 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (290000000000000.0, 'cm^3/(mol*s)'),
        n = -0.69,
        Ea = (755, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 55,
    reactant1 = 
"""
CH2_(T)
multiplicity 3
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    product1 = 
"""
HNCO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 C U0 L0 E0  {1,D} {4,D}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {2,D}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.1e+17, 'cm^3/(mol*s)'),
        n = -1.38,
        Ea = (1271, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 56,
    reactant1 = 
"""
CH2_(T)
multiplicity 3
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    product1 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.3e+16, 'cm^3/(mol*s)'),
        n = -1.43,
        Ea = (1331, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 57,
    reactant1 = 
"""
CH2_(T)
multiplicity 3
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    product1 = 
"""
H2CN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U1 L1 E0  {1,D}
""",
    product2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (81000000.0, 'cm^3/(mol*s)'),
        n = 1.42,
        Ea = (4111, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 58,
    reactant1 = 
"""
CH_(Q)
multiplicity 4
1 C U3 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
N2
multiplicity 1
1 N U0 L1 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    product1 = 
"""
HCNN
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L0 E+1 {1,T} {4,S}
3 H U0 L0 E0  {1,S}
4 N U1 L2 E-1 {2,S}
""",
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
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 59,
    reactant1 = 
"""
CH_(Q)
multiplicity 4
1 C U3 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
N2
multiplicity 1
1 N U0 L1 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    product1 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
N_(Q)
multiplicity 4
1 N U3 L1 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4400000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (21964, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 60,
    reactant1 = 
"""
CH_(Q)
multiplicity 4
1 C U3 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    product1 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (53000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 61,
    reactant1 = 
"""
CH_(Q)
multiplicity 4
1 C U3 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    product1 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product2 = 
"""
NCO
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L1 E0  {1,T}
3 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 62,
    reactant1 = 
"""
CH_(Q)
multiplicity 4
1 C U3 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    product1 = 
"""
N_(Q)
multiplicity 4
1 N U3 L1 E0 
""",
    product2 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,S} {3,D}
2 H U0 L0 E0  {1,S}
3 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (29000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 63,
    reactant1 = 
"""
CH_(Q)
multiplicity 4
1 C U3 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    product1 = 
"""
NH_(T)
multiplicity 3
1 N U2 L1 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5500000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 64,
    reactant1 = 
"""
CH_(Q)
multiplicity 4
1 C U3 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    product1 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CN
multiplicity 2
1 C U1 L0 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 65,
    reactant1 = 
"""
N_(Q)
multiplicity 4
1 N U3 L1 E0 
""",
    reactant2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9000000000.0, 'cm^3/(mol*s)'),
        n = 1,
        Ea = (6494, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 66,
    reactant1 = 
"""
N_(Q)
multiplicity 4
1 N U3 L1 E0 
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
NH_(T)
multiplicity 3
1 N U2 L1 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6400000000000.0, 'cm^3/(mol*s)'),
        n = 0.1,
        Ea = (21249, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 67,
    reactant1 = 
"""
N_(Q)
multiplicity 4
1 N U3 L1 E0 
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (110000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1122, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 68,
    reactant1 = 
"""
CH_(Q)
multiplicity 4
1 C U3 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
N_(Q)
multiplicity 4
1 N U3 L1 E0 
""",
    product1 = 
"""
CN
multiplicity 2
1 C U1 L0 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (170000000000000.0, 'cm^3/(mol*s)'),
        n = -0.09,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 69,
    reactant1 = 
"""
CH2_(T)
multiplicity 3
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
N_(Q)
multiplicity 4
1 N U3 L1 E0 
""",
    product1 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 70,
    reactant1 = 
"""
NH_(T)
multiplicity 3
1 N U2 L1 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
N_(Q)
multiplicity 4
1 N U3 L1 E0 
""",
    product1 = 
"""
N2
multiplicity 1
1 N U0 L1 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (15000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 71,
    reactant1 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
N_(Q)
multiplicity 4
1 N U3 L1 E0 
""",
    product1 = 
"""
N2
multiplicity 1
1 N U0 L1 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product3 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (71000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 72,
    reactant1 = 
"""
CN
multiplicity 2
1 C U1 L0 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    reactant2 = 
"""
N_(Q)
multiplicity 4
1 N U3 L1 E0 
""",
    product1 = 
"""
C_(T)
multiplicity 3
1 C U4 L0 E0 
""",
    product2 = 
"""
N2
multiplicity 1
1 N U0 L1 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (24000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-556, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 73,
    reactant1 = 
"""
NH_(T)
multiplicity 3
1 N U2 L1 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
NH_(T)
multiplicity 3
1 N U2 L1 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
N2
multiplicity 1
1 N U0 L1 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product3 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (51000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 74,
    reactant1 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
NH_(T)
multiplicity 3
1 N U2 L1 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
N2H2
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1500000000000000.0, 'cm^3/(mol*s)'),
        n = -0.5,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 75,
    reactant1 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
NH_(T)
multiplicity 3
1 N U2 L1 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
N_(Q)
multiplicity 4
1 N U3 L1 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (920000, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (2443, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 76,
    reactant1 = 
"""
NH_(T)
multiplicity 3
1 N U2 L1 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HNO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 77,
    reactant1 = 
"""
NH_(T)
multiplicity 3
1 N U2 L1 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
N_(Q)
multiplicity 4
1 N U3 L1 E0 
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1200000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-487, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 78,
    reactant1 = 
"""
NH_(T)
multiplicity 3
1 N U2 L1 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
N_(Q)
multiplicity 4
1 N U3 L1 E0 
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (35000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1728, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 79,
    reactant1 = 
"""
NH_(T)
multiplicity 3
1 N U2 L1 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (60000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 81,
    reactant1 = 
"""
NH_(T)
multiplicity 3
1 N U2 L1 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
H2CNH
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 N U0 L1 E0  {1,D} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (40000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 82,
    reactant1 = 
"""
NH_(T)
multiplicity 3
1 N U2 L1 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
N_(Q)
multiplicity 4
1 N U3 L1 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (820000, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (5848, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 83,
    reactant1 = 
"""
NNH
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 N U1 L1 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
N2
multiplicity 1
1 N U0 L1 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1200000000000.0, 'cm^3/(mol*s)'),
        n = -0.34,
        Ea = (-894, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 84,
    reactant1 = 
"""
NNH
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 N U1 L1 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
N2O
multiplicity 1
1 N U0 L0 E+1 {2,D} {3,D}
2 N U0 L2 E-1 {1,D}
3 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (290000000000.0, 'cm^3/(mol*s)'),
        n = -0.34,
        Ea = (2453, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 85,
    reactant1 = 
"""
NNH
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 N U1 L1 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
N2
multiplicity 1
1 N U0 L1 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (240000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (496, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 86,
    reactant1 = 
"""
NNH
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 N U1 L1 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
N2
multiplicity 1
1 N U0 L1 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+22, 'cm^3/(mol*s)'),
        n = -2.88,
        Ea = (-1152, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 87,
    reactant1 = 
"""
NNH
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 N U1 L1 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
N2
multiplicity 1
1 N U0 L1 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+16, 'cm^3/(mol*s)'),
        n = -1.23,
        Ea = (-1599, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 88,
    reactant1 = 
"""
NNH
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 N U1 L1 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
N2
multiplicity 1
1 N U0 L1 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (920000, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (1698, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 89,
    reactant1 = 
"""
NNH
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 N U1 L1 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
N2
multiplicity 1
1 N U0 L1 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
H2O2
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1192, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 90,
    reactant1 = 
"""
NNH
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 N U1 L1 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
HNNO
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 O U1 L2 E0  {2,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (24000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (70211, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 91,
    reactant1 = 
"""
NNH
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 N U1 L1 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    product1 = 
"""
N2
multiplicity 1
1 N U0 L1 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
HNO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1200000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (70717, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 92,
    reactant1 = 
"""
N2H2
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
NNH
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 N U1 L1 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
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
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 93,
    reactant1 = 
"""
N2H2
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
H2NN
multiplicity 1
1 N U0 L0 E+1 {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U0 L2 E-1 {1,D}
""",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(9.2e+38, '1/s'), n=-9.01, Ea=(67726, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2e+41, '1/s'), n=-9.38, Ea=(68452, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.3e+45, '1/s'), n=-10.13, Ea=(70757, 'cal/mol'), T0=(1, 'K')),
        ],
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 94,
    reactant1 = 
"""
N2H2
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
NNH
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 N U1 L1 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (480000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (496, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 95,
    reactant1 = 
"""
N2H2
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
NNH
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 N U1 L1 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (330000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-1192, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 96,
    reactant1 = 
"""
N2H2
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
NNH
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 N U1 L1 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2400000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1152, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 97,
    reactant1 = 
"""
N2H2
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
NNH
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 N U1 L1 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1800000.0, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (1969, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 98,
    reactant1 = 
"""
N2H2
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
NNH
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 N U1 L1 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1600000.0, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1192, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 99,
    reactant1 = 
"""
N2H2
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
NH_(T)
multiplicity 3
1 N U2 L1 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
NNH
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 N U1 L1 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2400000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (11915, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 100,
    reactant1 = 
"""
N2H2
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    product1 = 
"""
N2O
multiplicity 1
1 N U0 L0 E+1 {2,D} {3,D}
2 N U0 L2 E-1 {1,D}
3 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (51762, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 101,
    reactant1 = 
"""
H2NN
multiplicity 1
1 N U0 L0 E+1 {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U0 L2 E-1 {1,D}
""",
    product1 = 
"""
NNH
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 N U1 L1 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
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
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 102,
    reactant1 = 
"""
H2NN
multiplicity 1
1 N U0 L0 E+1 {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U0 L2 E-1 {1,D}
""",
    reactant2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
NO2
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1500000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5958, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 103,
    reactant1 = 
"""
H2NN
multiplicity 1
1 N U0 L0 E+1 {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U0 L2 E-1 {1,D}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
N2H2
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18000000000.0, 'cm^3/(mol*s)'),
        n = 0.97,
        Ea = (4468, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 104,
    reactant1 = 
"""
H2NN
multiplicity 1
1 N U0 L0 E+1 {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U0 L2 E-1 {1,D}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
NNH
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 N U1 L1 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (480000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-894, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 105,
    reactant1 = 
"""
H2NN
multiplicity 1
1 N U0 L0 E+1 {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U0 L2 E-1 {1,D}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3200000000.0, 'cm^3/(mol*s)'),
        n = 1.03,
        Ea = (2701, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 106,
    reactant1 = 
"""
H2NN
multiplicity 1
1 N U0 L0 E+1 {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U0 L2 E-1 {1,D}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
NNH
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 N U1 L1 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (330000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-894, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 107,
    reactant1 = 
"""
H2NN
multiplicity 1
1 N U0 L0 E+1 {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U0 L2 E-1 {1,D}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
NH2NO
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 108,
    reactant1 = 
"""
H2NN
multiplicity 1
1 N U0 L0 E+1 {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U0 L2 E-1 {1,D}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
NNH
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 N U1 L1 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2400000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1192, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 109,
    reactant1 = 
"""
H2NN
multiplicity 1
1 N U0 L0 E+1 {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U0 L2 E-1 {1,D}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
H2CNNH2
multiplicity 1
1 C U0 L0 E0  {3,D} {4,S} {5,S}
2 N U0 L1 E0  {3,S} {6,S} {7,S}
3 N U0 L1 E0  {1,D} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (830000, 'cm^3/(mol*s)'),
        n = 1.93,
        Ea = (6494, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 110,
    reactant1 = 
"""
H2NN
multiplicity 1
1 N U0 L0 E+1 {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U0 L2 E-1 {1,D}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3NNH
multiplicity 1
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 N U0 L1 E0  {1,S} {3,D}
3 N U0 L1 E0  {2,D} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {3,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (830000, 'cm^3/(mol*s)'),
        n = 1.93,
        Ea = (6494, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 111,
    reactant1 = 
"""
H2NN
multiplicity 1
1 N U0 L0 E+1 {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U0 L2 E-1 {1,D}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
NNH
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 N U1 L1 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1600000.0, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (129, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 112,
    reactant1 = 
"""
H2NN
multiplicity 1
1 N U0 L0 E+1 {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U0 L2 E-1 {1,D}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HNNNH2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 N U0 L1 E0  {1,S} {3,D}
3 N U0 L1 E0  {2,D} {4,S}
4 N U0 L1 E0  {3,S} {5,S} {6,S}
5 H U0 L0 E0  {4,S}
6 H U0 L0 E0  {4,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7900000.0, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (-1331, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 113,
    reactant1 = 
"""
H2NN
multiplicity 1
1 N U0 L0 E+1 {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U0 L2 E-1 {1,D}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
NNH
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 N U1 L1 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1800000.0, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (-1152, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 114,
    reactant1 = 
"""
H2NN
multiplicity 1
1 N U0 L0 E+1 {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U0 L2 E-1 {1,D}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
NH2NO
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (660000, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (7050, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 115,
    reactant1 = 
"""
H2NN
multiplicity 1
1 N U0 L0 E+1 {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U0 L2 E-1 {1,D}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
NNH
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 N U1 L1 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2O2
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (29000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1599, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 116,
    reactant1 = 
"""
N2H3
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
N2H2
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(2.3e+43, 's^-1'), n=-9.55, Ea=(64471, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.6e+47, 's^-1'), n=-10.38, Ea=(69012, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.8e+45, 's^-1'), n=-9.39, Ea=(70144, 'cal/mol'), T0=(1, 'K')),
        ],
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 117,
    reactant1 = 
"""
N2H3
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
N2H2
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (240000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 118,
    reactant1 = 
"""
N2H3
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
HNO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 119,
    reactant1 = 
"""
N2H3
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
NH2NO
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 120,
    reactant1 = 
"""
N2H3
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
N2H2
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (170000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-645, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 121,
    reactant1 = 
"""
N2H3
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
N2H2
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1200000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1192, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 122,
    reactant1 = 
"""
N2H3
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
H2NN
multiplicity 1
1 N U0 L0 E+1 {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U0 L2 E-1 {1,D}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 123,
    reactant1 = 
"""
N2H3
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
N2H2
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (820000, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (1817, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 124,
    reactant1 = 
"""
N2H3
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
H2NN
multiplicity 1
1 N U0 L0 E+1 {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U0 L2 E-1 {1,D}
""",
    product2 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 125,
    reactant1 = 
"""
N2H3
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
N2H2
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (920000, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (-1152, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 126,
    reactant1 = 
"""
N2H3
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
H2NN
multiplicity 1
1 N U0 L0 E+1 {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U0 L2 E-1 {1,D}
""",
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 127,
    reactant1 = 
"""
N2H3
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
H2NNHO
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 O U1 L2 E0  {2,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 128,
    reactant1 = 
"""
N2H3
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
N2H2
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H2O2
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (29000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1599, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 129,
    reactant1 = 
"""
N2H3
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
N2H4
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (920000, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (2125, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 130,
    reactant1 = 
"""
N2H4
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
H2NN
multiplicity 1
1 N U0 L0 E+1 {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U0 L2 E-1 {1,D}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(4e+44, 's^-1'), n=-9.85, Ea=(71357, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.3e+39, 's^-1'), n=-8.35, Ea=(69310, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.5e+39, 's^-1'), n=-8.19, Ea=(69668, 'cal/mol'), T0=(1, 'K')),
        ],
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 131,
    reactant1 = 
"""
N2H4
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
N2H3
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (960000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (4836, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 132,
    reactant1 = 
"""
N2H4
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
N2H3
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (670000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (2850, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 133,
    reactant1 = 
"""
N2H4
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
N2H3
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4800000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-645, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 134,
    reactant1 = 
"""
N2H4
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
N2H3
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3300000.0, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (5322, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 135,
    reactant1 = 
"""
N2H4
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
N2H3
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3700000.0, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (1628, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 136,
    reactant1 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    reactant2 = 
"""
C_(T)
multiplicity 3
1 C U4 L0 E0 
""",
    product1 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    product2 = 
"""
N_(Q)
multiplicity 4
1 N U3 L1 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (17000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 137,
    reactant1 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    reactant2 = 
"""
C_(T)
multiplicity 3
1 C U4 L0 E0 
""",
    product1 = 
"""
CN
multiplicity 2
1 C U1 L0 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (11000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 138,
    reactant1 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    reactant2 = 
"""
HCCO
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 C U0 L0 E0  {1,T} {4,S}
3 H U0 L0 E0  {1,S}
4 O U1 L2 E0  {2,S}
""",
    product1 = 
"""
HCNO
multiplicity 1
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L0 E+1 {1,T} {4,S}
3 H U0 L0 E0  {1,S}
4 O U0 L3 E-1 {2,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (46000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (695, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 139,
    reactant1 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    reactant2 = 
"""
HCCO
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 C U0 L0 E0  {1,T} {4,S}
3 H U0 L0 E0  {1,S}
4 O U1 L2 E0  {2,S}
""",
    product1 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
CO2
multiplicity 1
1 C U0 L0 E0  {2,D} {3,D}
2 O U0 L2 E0  {1,D}
3 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (695, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 140,
    reactant1 = 
"""
NO2
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 O U1 L2 E0  {1,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (130000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (357, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 141,
    reactant1 = 
"""
NO2
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 O U1 L2 E0  {1,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3900000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-238, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 142,
    reactant1 = 
"""
NO2
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (5700000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (59954, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 143,
    reactant1 = 
"""
NO2
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 O U1 L2 E0  {1,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
N2O
multiplicity 1
1 N U0 L0 E+1 {2,D} {3,D}
2 N U0 L2 E-1 {1,D}
3 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+16, 'cm^3/(mol*s)'),
        n = -1.44,
        Ea = (258, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 144,
    reactant1 = 
"""
NO2
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 O U1 L2 E0  {1,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
NH2O
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 O U1 L2 E0  {1,S}
""",
    product2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.6e+16, 'cm^3/(mol*s)'),
        n = -1.44,
        Ea = (258, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 145,
    reactant1 = 
"""
NO2
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 O U1 L2 E0  {1,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
CH3O
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 146,
    reactant1 = 
"""
N2O
multiplicity 1
1 N U0 L0 E+1 {2,D} {3,D}
2 N U0 L2 E-1 {1,D}
3 O U0 L2 E0  {1,D}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
N2
multiplicity 1
1 N U0 L1 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.013, 'cm^3/(mol*s)'),
        n = 4.72,
        Ea = (36540, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 147,
    reactant1 = 
"""
HNO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(2.6e+16, 'cm^3/(mol*s)'), n=0, Ea=(48654, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 148,
    reactant1 = 
"""
HNO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
HNO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
N2O
multiplicity 1
1 N U0 L0 E+1 {2,D} {3,D}
2 N U0 L2 E-1 {1,D}
3 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (850000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3078, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 149,
    reactant1 = 
"""
HNO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (13000000.0, 'cm^3/(mol*s)'),
        n = 1.88,
        Ea = (-953, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 150,
    reactant1 = 
"""
HNO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (450000000000.0, 'cm^3/(mol*s)'),
        n = 0.72,
        Ea = (655, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 152,
    reactant1 = 
"""
HNO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (450000000000.0, 'cm^3/(mol*s)'),
        n = 0.72,
        Ea = (655, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 153,
    reactant1 = 
"""
HNO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (920000, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (-1152, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 154,
    reactant1 = 
"""
HNO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    product1 = 
"""
N2O
multiplicity 1
1 N U0 L0 E+1 {2,D} {3,D}
2 N U0 L2 E-1 {1,D}
3 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8500000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (29570, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 155,
    reactant1 = 
"""
HNO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (15887, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 156,
    reactant1 = 
"""
HNO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (820000, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (29252, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 157,
    reactant1 = 
"""
NH2O
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
HNO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (2.8e+24, 'cm^3/(mol*s)'),
            n = -2.83,
            Ea = (64879, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 158,
    reactant1 = 
"""
NH2O
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
HNOH
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(8.2e+25, 's^-1'), n=-4.94, Ea=(43796, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.3e+27, 's^-1'), n=-4.99, Ea=(43984, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.6e+28, 's^-1'), n=-5.06, Ea=(44769, 'cal/mol'), T0=(1, 'K')),
        ],
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 159,
    reactant1 = 
"""
NH2O
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 O U1 L2 E0  {1,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (40000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 160,
    reactant1 = 
"""
NH2O
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 O U1 L2 E0  {1,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
HNO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (480000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (1559, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 161,
    reactant1 = 
"""
NH2O
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 O U1 L2 E0  {1,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
HNO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (330000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (487, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 162,
    reactant1 = 
"""
NH2O
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 O U1 L2 E0  {1,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HNO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2400000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1192, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 163,
    reactant1 = 
"""
NH2O
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 O U1 L2 E0  {1,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3O
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U1 L2 E0  {1,S}
""",
    product2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 164,
    reactant1 = 
"""
NH2O
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 O U1 L2 E0  {1,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
HNO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1600000.0, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (2959, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 165,
    reactant1 = 
"""
NH2O
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 O U1 L2 E0  {1,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HNO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1800000.0, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (-1152, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 166,
    reactant1 = 
"""
NH2O
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 O U1 L2 E0  {1,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
HNO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2O2
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (29000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1599, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 167,
    reactant1 = 
"""
NH2O
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 O U1 L2 E0  {1,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product2 = 
"""
NH2OH
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (29000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1599, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 168,
    reactant1 = 
"""
HNOH
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product2 = 
"""
HNO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (2e+24, 'cm^3/(mol*s)'),
            n = -2.84,
            Ea = (58901, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 169,
    reactant1 = 
"""
HNOH
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (40000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 170,
    reactant1 = 
"""
HNOH
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
HNO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (480000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (377, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 171,
    reactant1 = 
"""
HNOH
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
HNO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (70000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 172,
    reactant1 = 
"""
HNOH
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HNO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2400000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1192, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 173,
    reactant1 = 
"""
HNOH
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3NH
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U1 L1 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 174,
    reactant1 = 
"""
HNOH
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
HNO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1600000.0, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (2095, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 175,
    reactant1 = 
"""
HNOH
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
N2H3
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6700000.0, 'cm^3/(mol*s)'),
        n = 1.82,
        Ea = (715, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 176,
    reactant1 = 
"""
HNOH
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
H2NN
multiplicity 1
1 N U0 L0 E+1 {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U0 L2 E-1 {1,D}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.6e+19, 'cm^3/(mol*s)'),
        n = -1.94,
        Ea = (1926, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 177,
    reactant1 = 
"""
HNOH
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HNO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1800000.0, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (-1152, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 178,
    reactant1 = 
"""
HNOH
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
HONHO
multiplicity 2
1 H U0 L0 E0  {2,S}
2 O U0 L2 E0  {1,S} {3,S}
3 N U0 L1 E0  {2,S} {4,S} {5,S}
4 H U0 L0 E0  {3,S}
5 O U1 L2 E0  {3,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (40000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 179,
    reactant1 = 
"""
HNOH
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
HNO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2O2
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (29000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1599, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 180,
    reactant1 = 
"""
HNOH
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
NH2OH
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (29000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1599, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 181,
    reactant1 = 
"""
HNOO_(T)
multiplicity 3
1 N U1 L1 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 O U1 L2 E0  {2,S}
""",
    product1 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.5e+36, 'cm^3/(mol*s)'),
            n = -6.18,
            Ea = (31119, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 182,
    reactant1 = 
"""
HONO
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 N U0 L1 E0  {1,S} {4,D}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {2,D}
""",
    product1 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (2e+31, 'cm^3/(mol*s)'),
            n = -4.56,
            Ea = (51146, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 183,
    reactant1 = 
"""
HONO
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 N U0 L1 E0  {1,S} {4,D}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
NO2
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (200000000.0, 'cm^3/(mol*s)'),
        n = 1.55,
        Ea = (6613, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 184,
    reactant1 = 
"""
HONO
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 N U0 L1 E0  {1,S} {4,D}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8100000.0, 'cm^3/(mol*s)'),
        n = 1.89,
        Ea = (3843, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 185,
    reactant1 = 
"""
HONO
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 N U0 L1 E0  {1,S} {4,D}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
HNO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (56000000000.0, 'cm^3/(mol*s)'),
        n = 0.86,
        Ea = (4965, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 186,
    reactant1 = 
"""
HONO
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 N U0 L1 E0  {1,S} {4,D}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
NO2
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (170000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (3028, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 187,
    reactant1 = 
"""
HONO
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 N U0 L1 E0  {1,S} {4,D}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
NO2
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1200000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-596, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 188,
    reactant1 = 
"""
HONO
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 N U0 L1 E0  {1,S} {4,D}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
NO2
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 O U1 L2 E0  {1,S}
""",
    product2 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (810000, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (5501, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 189,
    reactant1 = 
"""
HONO
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 N U0 L1 E0  {1,S} {4,D}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
NO2
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 O U1 L2 E0  {1,S}
""",
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (920000, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (1916, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 190,
    reactant1 = 
"""
HNO2
multiplicity 1
1 N U0 L0 E+1 {2,S} {3,D} {4,S}
2 H U0 L0 E0  {1,S}
3 O U0 L2 E0  {1,D}
4 O U0 L3 E-1 {1,S}
""",
    product1 = 
"""
HONO
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 N U0 L1 E0  {1,S} {4,D}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {2,D}
""",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(7.1e+27, 's^-1'), n=-5.4, Ea=(52539, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.3e+29, 's^-1'), n=-5.47, Ea=(52817, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2e+30, 's^-1'), n=-5.5, Ea=(53691, 'cal/mol'), T0=(1, 'K')),
        ],
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 191,
    reactant1 = 
"""
HNO2
multiplicity 1
1 N U0 L0 E+1 {2,S} {3,D} {4,S}
2 H U0 L0 E0  {1,S}
3 O U0 L2 E0  {1,D}
4 O U0 L3 E-1 {1,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
NO2
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (240000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (4160, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 192,
    reactant1 = 
"""
HNO2
multiplicity 1
1 N U0 L0 E+1 {2,S} {3,D} {4,S}
2 H U0 L0 E0  {1,S}
3 O U0 L2 E0  {1,D}
4 O U0 L3 E-1 {1,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
NO2
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (170000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (2363, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 193,
    reactant1 = 
"""
HNO2
multiplicity 1
1 N U0 L0 E+1 {2,S} {3,D} {4,S}
2 H U0 L0 E0  {1,S}
3 O U0 L2 E0  {1,D}
4 O U0 L3 E-1 {1,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
NO2
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1200000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-794, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 194,
    reactant1 = 
"""
HNO2
multiplicity 1
1 N U0 L0 E+1 {2,S} {3,D} {4,S}
2 H U0 L0 E0  {1,S}
3 O U0 L2 E0  {1,D}
4 O U0 L3 E-1 {1,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
NO2
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 O U1 L2 E0  {1,S}
""",
    product2 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (810000, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (4836, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 195,
    reactant1 = 
"""
HNO2
multiplicity 1
1 N U0 L0 E+1 {2,S} {3,D} {4,S}
2 H U0 L0 E0  {1,S}
3 O U0 L2 E0  {1,D}
4 O U0 L3 E-1 {1,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
NO2
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 O U1 L2 E0  {1,S}
""",
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (920000, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (874, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 196,
    reactant1 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    product1 = 
"""
HNC
multiplicity 1
1 N U0 L0 E+1 {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 C U0 L1 E-1 {1,T}
""",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.5e+23, 's^-1'), n=-4.2, Ea=(49459, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.9e+24, 's^-1'), n=-4.23, Ea=(49578, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.3e+25, 's^-1'), n=-4.34, Ea=(50194, 'cal/mol'), T0=(1, 'K')),
        ],
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 198,
    reactant1 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    product1 = 
"""
HNCO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 C U0 L0 E0  {1,D} {4,D}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {2,D}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4400, 'cm^3/(mol*s)'),
        n = 2.26,
        Ea = (6395, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 199,
    reactant1 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    product1 = 
"""
HOCN
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 C U0 L0 E0  {1,S} {4,T}
3 H U0 L0 E0  {1,S}
4 N U0 L1 E0  {2,T}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1100000.0, 'cm^3/(mol*s)'),
        n = 2.03,
        Ea = (13365, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 200,
    reactant1 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    product1 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (160, 'cm^3/(mol*s)'),
        n = 2.56,
        Ea = (8996, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 201,
    reactant1 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    product1 = 
"""
NCHOH
multiplicity 2
1 C U0 L0 E0  {2,S} {3,D} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 N U1 L1 E0  {1,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
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
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 202,
    reactant1 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
NH_(T)
multiplicity 3
1 N U2 L1 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (540000000.0, 'cm^3/(mol*s)'),
        n = 1.21,
        Ea = (7487, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 203,
    reactant1 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
NCO
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L1 E0  {1,T}
3 O U1 L2 E0  {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (200000000.0, 'cm^3/(mol*s)'),
        n = 1.47,
        Ea = (7586, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 204,
    reactant1 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
CN
multiplicity 2
1 C U1 L0 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (42000000000.0, 'cm^3/(mol*s)'),
        n = 0.4,
        Ea = (20663, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 205,
    reactant1 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    reactant2 = 
"""
HNC
multiplicity 1
1 N U0 L0 E+1 {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 C U0 L1 E-1 {1,T}
""",
    product1 = 
"""
NH_(T)
multiplicity 3
1 N U2 L1 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4600000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2184, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 206,
    reactant1 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
HNC
multiplicity 1
1 N U0 L0 E+1 {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 C U0 L1 E-1 {1,T}
""",
    product1 = 
"""
HNCO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 C U0 L0 E0  {1,D} {4,D}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {2,D}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3694, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 207,
    reactant1 = 
"""
HNC
multiplicity 1
1 N U0 L0 E+1 {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 C U0 L1 E-1 {1,T}
""",
    reactant2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
HNCO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 C U0 L0 E0  {1,D} {4,D}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {2,D}
""",
    product2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1500000000000.0, 'cm^3/(mol*s)'),
        n = 0.01,
        Ea = (4111, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 208,
    reactant1 = 
"""
HNC
multiplicity 1
1 N U0 L0 E+1 {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 C U0 L1 E-1 {1,T}
""",
    reactant2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
NH_(T)
multiplicity 3
1 N U2 L1 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CO2
multiplicity 1
1 C U0 L0 E0  {2,D} {3,D}
2 O U0 L2 E0  {1,D}
3 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+19, 'cm^3/(mol*s)'),
        n = -2.25,
        Ea = (1777, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 209,
    reactant1 = 
"""
CN
multiplicity 2
1 C U1 L0 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    reactant2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (360000000.0, 'cm^3/(mol*s)'),
        n = 1.55,
        Ea = (2999, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 210,
    reactant1 = 
"""
CN
multiplicity 2
1 C U1 L0 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    reactant2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7800000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7447, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 211,
    reactant1 = 
"""
CN
multiplicity 2
1 C U1 L0 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    product2 = 
"""
N_(Q)
multiplicity 4
1 N U3 L1 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (77000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 212,
    reactant1 = 
"""
CN
multiplicity 2
1 C U1 L0 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    reactant2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
NCO
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L1 E0  {1,T}
3 O U1 L2 E0  {1,S}
""",
    product2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 213,
    reactant1 = 
"""
CN
multiplicity 2
1 C U1 L0 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
NCO
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L1 E0  {1,T}
3 O U1 L2 E0  {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (40000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 214,
    reactant1 = 
"""
CN
multiplicity 2
1 C U1 L0 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    reactant2 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    product1 = 
"""
NCCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 C U0 L0 E0  {1,S} {4,T}
3 N U0 L1 E0  {1,T}
4 N U0 L1 E0  {2,T}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (15000000.0, 'cm^3/(mol*s)'),
        n = 1.71,
        Ea = (1529, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 215,
    reactant1 = 
"""
CN
multiplicity 2
1 C U1 L0 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    reactant2 = 
"""
N2O
multiplicity 1
1 N U0 L0 E+1 {2,D} {3,D}
2 N U0 L2 E-1 {1,D}
3 O U0 L2 E0  {1,D}
""",
    product1 = 
"""
NCN_(T)
multiplicity 3
1 N U1 L1 E0  {2,D}
2 C U0 L0 E0  {1,D} {3,D}
3 N U1 L1 E0  {2,D}
""",
    product2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (420000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7169, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 216,
    reactant1 = 
"""
CN
multiplicity 2
1 C U1 L0 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    reactant2 = 
"""
NO2
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
NCO
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L1 E0  {1,T}
3 O U1 L2 E0  {1,S}
""",
    product2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6200000000000000.0, 'cm^3/(mol*s)'),
        n = -0.75,
        Ea = (348, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 217,
    reactant1 = 
"""
CN
multiplicity 2
1 C U1 L0 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    reactant2 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (120000, 'cm^3/(mol*s)'),
        n = 2.64,
        Ea = (-159, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 218,
    reactant1 = 
"""
CN
multiplicity 2
1 C U1 L0 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    reactant2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-357, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 219,
    reactant1 = 
"""
H2CN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U1 L1 E0  {1,D}
""",
    product1 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.3e+29, 's^-1'), n=-6.03, Ea=(29896, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6e+31, 's^-1'), n=-6.46, Ea=(32111, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.5e+29, 's^-1'), n=-5.46, Ea=(32549, 'cal/mol'), T0=(1, 'K')),
        ],
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 220,
    reactant1 = 
"""
H2CN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U1 L1 E0  {1,D}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
CH2NO
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 221,
    reactant1 = 
"""
H2CN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U1 L1 E0  {1,D}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
H2O2
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1609, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 222,
    reactant1 = 
"""
H2CN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U1 L1 E0  {1,D}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
H2CNH
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 N U0 L1 E0  {1,D} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1609, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 223,
    reactant1 = 
"""
H2CN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U1 L1 E0  {1,D}
""",
    reactant2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5958, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 224,
    reactant1 = 
"""
H2CN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U1 L1 E0  {1,D}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (810000, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1112, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 225,
    reactant1 = 
"""
H2CN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U1 L1 E0  {1,D}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
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
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 226,
    reactant1 = 
"""
H2CN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U1 L1 E0  {1,D}
""",
    reactant2 = 
"""
N_(Q)
multiplicity 4
1 N U3 L1 E0 
""",
    product1 = 
"""
N2
multiplicity 1
1 N U0 L1 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
CH2_(T)
multiplicity 3
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (60000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (397, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 227,
    reactant1 = 
"""
H2CN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U1 L1 E0  {1,D}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (240000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-894, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 228,
    reactant1 = 
"""
H2CN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U1 L1 E0  {1,D}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (920000, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (-1152, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 229,
    reactant1 = 
"""
H2CN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U1 L1 E0  {1,D}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (170000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-894, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 230,
    reactant1 = 
"""
H2CN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U1 L1 E0  {1,D}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
HNCO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 C U0 L0 E0  {1,D} {4,D}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {2,D}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (60000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 231,
    reactant1 = 
"""
H2CN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U1 L1 E0  {1,D}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
HCNO
multiplicity 1
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L0 E+1 {1,T} {4,S}
3 H U0 L0 E0  {1,S}
4 O U0 L3 E-1 {2,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 232,
    reactant1 = 
"""
HCNH
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(7.7e+25, 's^-1'), n=-5.2, Ea=(21987, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.1e+28, 's^-1'), n=-5.69, Ea=(24272, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.2e+26, 's^-1'), n=-4.77, Ea=(24819, 'cal/mol'), T0=(1, 'K')),
        ],
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 233,
    reactant1 = 
"""
HCNH
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
H2CN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U1 L1 E0  {1,D}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 234,
    reactant1 = 
"""
HCNH
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (240000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-894, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 235,
    reactant1 = 
"""
HCNH
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
HNCO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 C U0 L0 E0  {1,D} {4,D}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {2,D}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (70000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 236,
    reactant1 = 
"""
HCNH
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (170000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-894, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 237,
    reactant1 = 
"""
HCNH
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1200000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1192, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 238,
    reactant1 = 
"""
HCNH
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (820000, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1112, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 239,
    reactant1 = 
"""
HCNN
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L0 E+1 {1,T} {4,S}
3 H U0 L0 E0  {1,S}
4 N U1 L2 E-1 {2,S}
""",
    reactant2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product2 = 
"""
CO2
multiplicity 1
1 C U0 L0 E0  {2,D} {3,D}
2 O U0 L2 E0  {1,D}
3 O U0 L2 E0  {1,D}
""",
    product3 = 
"""
N2
multiplicity 1
1 N U0 L1 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 240,
    reactant1 = 
"""
HCNN
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L0 E+1 {1,T} {4,S}
3 H U0 L0 E0  {1,S}
4 N U1 L2 E-1 {2,S}
""",
    reactant2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,S} {3,D}
2 H U0 L0 E0  {1,S}
3 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
N2O
multiplicity 1
1 N U0 L0 E+1 {2,D} {3,D}
2 N U0 L2 E-1 {1,D}
3 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 241,
    reactant1 = 
"""
H2CNH
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 N U0 L1 E0  {1,D} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
H2CN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U1 L1 E0  {1,D}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (240000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (7318, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 242,
    reactant1 = 
"""
H2CNH
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 N U0 L1 E0  {1,D} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
H2CN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U1 L1 E0  {1,D}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (170000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (4627, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 243,
    reactant1 = 
"""
H2CNH
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 N U0 L1 E0  {1,D} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
H2CN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U1 L1 E0  {1,D}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1200000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-89, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 244,
    reactant1 = 
"""
H2CNH
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 N U0 L1 E0  {1,D} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
H2CN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U1 L1 E0  {1,D}
""",
    product2 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (820000, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (7119, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 245,
    reactant1 = 
"""
H2CNH
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 N U0 L1 E0  {1,D} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
H2CN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U1 L1 E0  {1,D}
""",
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (920000, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (4438, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 246,
    reactant1 = 
"""
H2CNH
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 N U0 L1 E0  {1,D} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
HCNH
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (300000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (6126, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 247,
    reactant1 = 
"""
H2CNH
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 N U0 L1 E0  {1,D} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
HCNH
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (220000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (5402, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 248,
    reactant1 = 
"""
H2CNH
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 N U0 L1 E0  {1,D} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HCNH
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2400000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (457, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 249,
    reactant1 = 
"""
H2CNH
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 N U0 L1 E0  {1,D} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HCNH
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (530000, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (9681, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 250,
    reactant1 = 
"""
H2CNH
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 N U0 L1 E0  {1,D} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HCNH
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1800000.0, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (6087, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 251,
    reactant1 = 
"""
H2CNH
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 N U0 L1 E0  {1,D} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
NH_(T)
multiplicity 3
1 N U2 L1 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1700000.0, 'cm^3/(mol*s)'),
        n = 2.08,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 252,
    reactant1 = 
"""
CH3NH
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U1 L1 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
H2CNH
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 N U0 L1 E0  {1,D} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.6e+36, 's^-1'), n=-7.92, Ea=(36344, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.3e+42, 's^-1'), n=-9.24, Ea=(41341, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.3e+44, 's^-1'), n=-9.51, Ea=(45246, 'cal/mol'), T0=(1, 'K')),
        ],
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 253,
    reactant1 = 
"""
CH3NH
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U1 L1 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
H2CNH
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 N U0 L1 E0  {1,D} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (720000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-894, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 254,
    reactant1 = 
"""
CH3NH
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U1 L1 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
H2CNH
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 N U0 L1 E0  {1,D} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (500000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-894, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 255,
    reactant1 = 
"""
CH3NH
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U1 L1 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
H2CNH
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 N U0 L1 E0  {1,D} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3600000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1192, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 256,
    reactant1 = 
"""
CH3NH
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U1 L1 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
H2CNH
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 N U0 L1 E0  {1,D} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2400000.0, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1112, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 257,
    reactant1 = 
"""
CH2NH2
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
H2CNH
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 N U0 L1 E0  {1,D} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.1e+45, 's^-1'), n=-10.24, Ea=(47819, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.4e+48, 's^-1'), n=-10.82, Ea=(52042, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.2e+46, 's^-1'), n=-9.95, Ea=(53532, 'cal/mol'), T0=(1, 'K')),
        ],
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 258,
    reactant1 = 
"""
CH2NH2
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
H2CNH
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 N U0 L1 E0  {1,D} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+22, 'cm^3/(mol*s)'),
        n = -3.09,
        Ea = (6752, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 259,
    reactant1 = 
"""
CH2NH2
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {1,D}
""",
    product3 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+18, 'cm^3/(mol*s)'),
        n = -1.59,
        Ea = (30175, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 260,
    reactant1 = 
"""
CH2NH2
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
H2CNH
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 N U0 L1 E0  {1,D} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (400000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-894, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 261,
    reactant1 = 
"""
CH2NH2
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (70000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 262,
    reactant1 = 
"""
CH2NH2
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
H2CNH
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 N U0 L1 E0  {1,D} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (330000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-894, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 263,
    reactant1 = 
"""
CH2NH2
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2OH
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (40000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 264,
    reactant1 = 
"""
CH2NH2
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
H2CNH
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 N U0 L1 E0  {1,D} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2400000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1192, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 265,
    reactant1 = 
"""
CH2NH2
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
C2H5
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,S} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2701, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 266,
    reactant1 = 
"""
CH2NH2
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
H2CNH
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 N U0 L1 E0  {1,D} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1600000.0, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-626, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 267,
    reactant1 = 
"""
CH3NH2
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U0 L1 E0  {1,S} {6,S} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH2NH2
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (560000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (5461, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 268,
    reactant1 = 
"""
CH3NH2
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U0 L1 E0  {1,S} {6,S} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
CH2NH2
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (400000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (5193, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 269,
    reactant1 = 
"""
CH3NH2
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U0 L1 E0  {1,S} {6,S} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2NH2
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3600000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (238, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 270,
    reactant1 = 
"""
CH3NH2
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U0 L1 E0  {1,S} {6,S} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2NH2
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1500000.0, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (9165, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 271,
    reactant1 = 
"""
CH3NH2
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U0 L1 E0  {1,S} {6,S} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2NH2
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2800000.0, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (5491, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 272,
    reactant1 = 
"""
CH3NH2
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U0 L1 E0  {1,S} {6,S} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH3NH
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U1 L1 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (480000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (9701, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 273,
    reactant1 = 
"""
CH3NH2
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U0 L1 E0  {1,S} {6,S} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
CH3NH
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U1 L1 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (330000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (6345, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 274,
    reactant1 = 
"""
CH3NH2
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U0 L1 E0  {1,S} {6,S} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3NH
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U1 L1 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2400000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (447, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 275,
    reactant1 = 
"""
CH3NH2
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U0 L1 E0  {1,S} {6,S} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3NH
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U1 L1 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1600000.0, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (8837, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 276,
    reactant1 = 
"""
CH3NH2
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U0 L1 E0  {1,S} {6,S} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3NH
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U1 L1 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1800000.0, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (7139, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 277,
    reactant1 = 
"""
NCCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 C U0 L0 E0  {1,S} {4,T}
3 N U0 L1 E0  {1,T}
4 N U0 L1 E0  {2,T}
""",
    product1 = 
"""
CN
multiplicity 2
1 C U1 L0 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
CN
multiplicity 2
1 C U1 L0 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.6e+34, 'cm^3/(mol*s)'),
            n = -4.32,
            Ea = (130005, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 279,
    reactant1 = 
"""
NCCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 C U0 L0 E0  {1,S} {4,T}
3 N U0 L1 E0  {1,T}
4 N U0 L1 E0  {2,T}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
NCO
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L1 E0  {1,T}
3 O U1 L2 E0  {1,S}
""",
    product2 = 
"""
CN
multiplicity 2
1 C U1 L0 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4600000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8877, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 280,
    reactant1 = 
"""
NCCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 C U0 L0 E0  {1,S} {4,T}
3 N U0 L1 E0  {1,T}
4 N U0 L1 E0  {2,T}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HOCN
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 C U0 L0 E0  {1,S} {4,T}
3 H U0 L0 E0  {1,S}
4 N U0 L1 E0  {2,T}
""",
    product2 = 
"""
CN
multiplicity 2
1 C U1 L0 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (18985, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 281,
    reactant1 = 
"""
NCO
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L1 E0  {1,T}
3 O U1 L2 E0  {1,S}
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    product1 = 
"""
CO2
multiplicity 1
1 C U0 L0 E0  {2,D} {3,D}
2 O U0 L2 E0  {1,D}
3 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
N2
multiplicity 1
1 N U0 L1 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.8e+17, 'cm^3/(mol*s)'),
        n = -1.73,
        Ea = (765, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 282,
    reactant1 = 
"""
NCO
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L1 E0  {1,T}
3 O U1 L2 E0  {1,S}
""",
    reactant2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    product1 = 
"""
N2O
multiplicity 1
1 N U0 L0 E+1 {2,D} {3,D}
2 N U0 L2 E-1 {1,D}
3 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.2e+17, 'cm^3/(mol*s)'),
        n = -1.73,
        Ea = (765, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 283,
    reactant1 = 
"""
NCO
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L1 E0  {1,T}
3 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
N_(Q)
multiplicity 4
1 N U3 L1 E0 
""",
    product2 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (330000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (54016, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 284,
    reactant1 = 
"""
NCO
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L1 E0  {1,T}
3 O U1 L2 E0  {1,S}
""",
    reactant2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HNCO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 C U0 L0 E0  {1,D} {4,D}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {2,D}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (760, 'cm^3/(mol*s)'),
        n = 3,
        Ea = (3972, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 285,
    reactant1 = 
"""
NCO
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L1 E0  {1,T}
3 O U1 L2 E0  {1,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (42000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 286,
    reactant1 = 
"""
NCO
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L1 E0  {1,T}
3 O U1 L2 E0  {1,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
N_(Q)
multiplicity 4
1 N U3 L1 E0 
""",
    product2 = 
"""
CO2
multiplicity 1
1 C U0 L0 E0  {2,D} {3,D}
2 O U0 L2 E0  {1,D}
3 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2502, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 287,
    reactant1 = 
"""
NCO
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L1 E0  {1,T}
3 O U1 L2 E0  {1,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
NH_(T)
multiplicity 3
1 N U2 L1 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (52000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 288,
    reactant1 = 
"""
NCO
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L1 E0  {1,T}
3 O U1 L2 E0  {1,S}
""",
    reactant2 = 
"""
N_(Q)
multiplicity 4
1 N U3 L1 E0 
""",
    product1 = 
"""
N2
multiplicity 1
1 N U0 L1 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (33000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 289,
    reactant1 = 
"""
NCO
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L1 E0  {1,T}
3 O U1 L2 E0  {1,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HNCO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 C U0 L0 E0  {1,D} {4,D}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {2,D}
""",
    product2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (78000, 'cm^3/(mol*s)'),
        n = 2.27,
        Ea = (-993, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 290,
    reactant1 = 
"""
NCO
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L1 E0  {1,T}
3 O U1 L2 E0  {1,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HON_(T)
multiplicity 3
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 N U2 L1 E0  {1,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5300000000000.0, 'cm^3/(mol*s)'),
        n = -0.07,
        Ea = (5124, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 291,
    reactant1 = 
"""
NCO
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L1 E0  {1,T}
3 O U1 L2 E0  {1,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product2 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    product3 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8300000000000.0, 'cm^3/(mol*s)'),
        n = -0.05,
        Ea = (18032, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 292,
    reactant1 = 
"""
NCO
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L1 E0  {1,T}
3 O U1 L2 E0  {1,S}
""",
    reactant2 = 
"""
NO2
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
CO2
multiplicity 1
1 C U0 L0 E0  {2,D} {3,D}
2 O U0 L2 E0  {1,D}
3 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
N2O
multiplicity 1
1 N U0 L0 E+1 {2,D} {3,D}
2 N U0 L2 E-1 {1,D}
3 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-874, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 293,
    reactant1 = 
"""
NCO
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L1 E0  {1,T}
3 O U1 L2 E0  {1,S}
""",
    reactant2 = 
"""
NO2
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    product2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    product3 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (210000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-874, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 294,
    reactant1 = 
"""
NCO
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L1 E0  {1,T}
3 O U1 L2 E0  {1,S}
""",
    reactant2 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HNCO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 C U0 L0 E0  {1,D} {4,D}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {2,D}
""",
    product2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9800000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8122, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 296,
    reactant1 = 
"""
HCNO
multiplicity 1
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L0 E+1 {1,T} {4,S}
3 H U0 L0 E0  {1,S}
4 O U0 L3 E-1 {2,S}
""",
    product1 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(2e+30, 's^-1'), n=-6.03, Ea=(60736, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.2e+31, 's^-1'), n=-6.12, Ea=(61212, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.9e+31, 's^-1'), n=-5.85, Ea=(61938, 'cal/mol'), T0=(1, 'K')),
        ],
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 297,
    reactant1 = 
"""
HCNO
multiplicity 1
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L0 E+1 {1,T} {4,S}
3 H U0 L0 E0  {1,S}
4 O U0 L3 E-1 {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
HNCO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 C U0 L0 E0  {1,D} {4,D}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {2,D}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2100000000000000.0, 'cm^3/(mol*s)'),
        n = -0.69,
        Ea = (2850, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 298,
    reactant1 = 
"""
HCNO
multiplicity 1
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L0 E+1 {1,T} {4,S}
3 H U0 L0 E0  {1,S}
4 O U0 L3 E-1 {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (270000000000.0, 'cm^3/(mol*s)'),
        n = 0.18,
        Ea = (2115, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 299,
    reactant1 = 
"""
HCNO
multiplicity 1
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L0 E+1 {1,T} {4,S}
3 H U0 L0 E0  {1,S}
4 O U0 L3 E-1 {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (170000000000000.0, 'cm^3/(mol*s)'),
        n = -0.75,
        Ea = (2889, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 300,
    reactant1 = 
"""
HCNO
multiplicity 1
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L0 E+1 {1,T} {4,S}
3 H U0 L0 E0  {1,S}
4 O U0 L3 E-1 {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
HOCN
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 C U0 L0 E0  {1,S} {4,T}
3 H U0 L0 E0  {1,S}
4 N U0 L1 E0  {2,T}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (140000000000.0, 'cm^3/(mol*s)'),
        n = -0.19,
        Ea = (2482, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 301,
    reactant1 = 
"""
HCNO
multiplicity 1
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L0 E+1 {1,T} {4,S}
3 H U0 L0 E0  {1,S}
4 O U0 L3 E-1 {2,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,S} {3,D}
2 H U0 L0 E0  {1,S}
3 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (70000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 302,
    reactant1 = 
"""
HCNO
multiplicity 1
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L0 E+1 {1,T} {4,S}
3 H U0 L0 E0  {1,S}
4 O U0 L3 E-1 {2,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HCOH_(S)
multiplicity 1
1 C U2 L0 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (40000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 304,
    reactant1 = 
"""
HOCN
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 C U0 L0 E0  {1,S} {4,T}
3 H U0 L0 E0  {1,S}
4 N U0 L1 E0  {2,T}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
HNCO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 C U0 L0 E0  {1,D} {4,D}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {2,D}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (310000000.0, 'cm^3/(mol*s)'),
        n = 0.84,
        Ea = (1916, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 305,
    reactant1 = 
"""
HOCN
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 C U0 L0 E0  {1,S} {4,T}
3 H U0 L0 E0  {1,S}
4 N U0 L1 E0  {2,T}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (120000000.0, 'cm^3/(mol*s)'),
        n = 0.61,
        Ea = (2075, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 306,
    reactant1 = 
"""
HOCN
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 C U0 L0 E0  {1,S} {4,T}
3 H U0 L0 E0  {1,S}
4 N U0 L1 E0  {2,T}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
NCO
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L1 E0  {1,T}
3 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (240000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (6613, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 307,
    reactant1 = 
"""
HOCN
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 C U0 L0 E0  {1,S} {4,T}
3 H U0 L0 E0  {1,S}
4 N U0 L1 E0  {2,T}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
NCO
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L1 E0  {1,T}
3 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (170000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (4131, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 308,
    reactant1 = 
"""
HOCN
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 C U0 L0 E0  {1,S} {4,T}
3 H U0 L0 E0  {1,S}
4 N U0 L1 E0  {2,T}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
NCO
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L1 E0  {1,T}
3 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1200000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-248, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 309,
    reactant1 = 
"""
HOCN
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 C U0 L0 E0  {1,S} {4,T}
3 H U0 L0 E0  {1,S}
4 N U0 L1 E0  {2,T}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
NCO
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L1 E0  {1,T}
3 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (820000, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (6613, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 310,
    reactant1 = 
"""
HOCN
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 C U0 L0 E0  {1,S} {4,T}
3 H U0 L0 E0  {1,S}
4 N U0 L1 E0  {2,T}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
NCO
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L1 E0  {1,T}
3 O U1 L2 E0  {1,S}
""",
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (920000, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (36443, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 311,
    reactant1 = 
"""
HNCO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 C U0 L0 E0  {1,D} {4,D}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {2,D}
""",
    product1 = 
"""
NH_(T)
multiplicity 3
1 N U2 L1 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.3e+16, 'cm^3/(mol*s)'), n=0, Ea=(84320, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 312,
    reactant1 = 
"""
HNCO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 C U0 L0 E0  {1,D} {4,D}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (36000, 'cm^3/(mol*s)'),
        n = 2.49,
        Ea = (2343, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 313,
    reactant1 = 
"""
HNCO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 C U0 L0 E0  {1,D} {4,D}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
HNO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1700000.0, 'cm^3/(mol*s)'),
        n = 2.08,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 314,
    reactant1 = 
"""
HNCO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 C U0 L0 E0  {1,D} {4,D}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
NH_(T)
multiplicity 3
1 N U2 L1 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CO2
multiplicity 1
1 C U0 L0 E0  {2,D} {3,D}
2 O U0 L2 E0  {1,D}
3 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1700000.0, 'cm^3/(mol*s)'),
        n = 2.08,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 315,
    reactant1 = 
"""
HNCO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 C U0 L0 E0  {1,D} {4,D}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CO2
multiplicity 1
1 C U0 L0 E0  {2,D} {3,D}
2 O U0 L2 E0  {1,D}
3 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (63000000000.0, 'cm^3/(mol*s)'),
        n = -0.06,
        Ea = (11637, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 316,
    reactant1 = 
"""
HNCO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 C U0 L0 E0  {1,D} {4,D}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
NCO
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L1 E0  {1,T}
3 O U1 L2 E0  {1,S}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (52000000000.0, 'cm^3/(mol*s)'),
        n = -0.03,
        Ea = (17555, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 320,
    reactant1 = 
"""
HNCO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 C U0 L0 E0  {1,D} {4,D}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
NCO
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L1 E0  {1,T}
3 O U1 L2 E0  {1,S}
""",
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8936, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 321,
    reactant1 = 
"""
CH2NO
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
""",
    product1 = 
"""
HNCO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 C U0 L0 E0  {1,D} {4,D}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {2,D}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(6.9e+41, 's^-1'), n=-9.3, Ea=(51704, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.3e+42, 's^-1'), n=-9.11, Ea=(53840, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.7e+38, 's^-1'), n=-7.64, Ea=(53582, 'cal/mol'), T0=(1, 'K')),
        ],
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 322,
    reactant1 = 
"""
CH2NO
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
NO2
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1200000000000000.0, 'cm^3/(mol*s)'),
        n = -1.01,
        Ea = (20117, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 323,
    reactant1 = 
"""
CH2NO
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (40000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 324,
    reactant1 = 
"""
CH2NO
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
HCNO
multiplicity 1
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L0 E+1 {1,T} {4,S}
3 H U0 L0 E0  {1,S}
4 O U0 L3 E-1 {2,S}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (480000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-894, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 325,
    reactant1 = 
"""
CH2NO
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (70000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 326,
    reactant1 = 
"""
CH2NO
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
HCNO
multiplicity 1
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L0 E+1 {1,T} {4,S}
3 H U0 L0 E0  {1,S}
4 O U0 L3 E-1 {2,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (330000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-894, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 327,
    reactant1 = 
"""
CH2NO
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2OH
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (40000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 328,
    reactant1 = 
"""
CH2NO
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HCNO
multiplicity 1
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L0 E+1 {1,T} {4,S}
3 H U0 L0 E0  {1,S}
4 O U0 L3 E-1 {2,S}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2400000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1192, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 329,
    reactant1 = 
"""
CH2NO
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
C2H5
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,S} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 330,
    reactant1 = 
"""
CH2NO
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HCNO
multiplicity 1
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L0 E+1 {1,T} {4,S}
3 H U0 L0 E0  {1,S}
4 O U0 L3 E-1 {2,S}
""",
    product2 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1600000.0, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1112, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 331,
    reactant1 = 
"""
CH2NO
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2NH2
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 332,
    reactant1 = 
"""
CH2NO
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HCNO
multiplicity 1
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L0 E+1 {1,T} {4,S}
3 H U0 L0 E0  {1,S}
4 O U0 L3 E-1 {2,S}
""",
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1800000.0, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (-1152, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 333,
    reactant1 = 
"""
CH3NO
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U0 L1 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH2NO
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (440000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (377, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 334,
    reactant1 = 
"""
CH3NO
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U0 L1 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
CH2NO
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (330000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (3614, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 335,
    reactant1 = 
"""
CH3NO
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U0 L1 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2NO
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3600000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1192, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 336,
    reactant1 = 
"""
CH3NO
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U0 L1 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2NO
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
""",
    product2 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (790000, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (5412, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 337,
    reactant1 = 
"""
CH3NO
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U0 L1 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2NO
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
""",
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2800000.0, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (1072, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 338,
    reactant1 = 
"""
CH3NO
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U0 L1 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
HNO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2780, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 339,
    reactant1 = 
"""
CH3NO
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U0 L1 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
NO2
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1700000.0, 'cm^3/(mol*s)'),
        n = 2.08,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 340,
    reactant1 = 
"""
CH3NO
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U0 L1 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
HONO
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 N U0 L1 E0  {1,S} {4,D}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2500000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (993, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 341,
    reactant1 = 
"""
HON_(S)
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 N U2 L1 E0  {1,S}
""",
    product1 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (5.1e+19, 'cm^3/(mol*s)'),
            n = -1.73,
            Ea = (16036, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 342,
    reactant1 = 
"""
HON_(S)
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 N U2 L1 E0  {1,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
HNO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 343,
    reactant1 = 
"""
HON_(S)
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 N U2 L1 E0  {1,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
NH_(S)
multiplicity 1
1 N U2 L1 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 344,
    reactant1 = 
"""
HON_(S)
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 N U2 L1 E0  {1,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (70000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 345,
    reactant1 = 
"""
HON_(S)
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 N U2 L1 E0  {1,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HONO
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 N U0 L1 E0  {1,S} {4,D}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {2,D}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (40000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 346,
    reactant1 = 
"""
HON_(S)
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 N U2 L1 E0  {1,S}
""",
    reactant2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
HONO
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 N U0 L1 E0  {1,S} {4,D}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {2,D}
""",
    product2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4965, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 347,
    reactant1 = 
"""
HCOH_(S)
multiplicity 1
1 C U2 L0 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(3.5e+17, 's^-1'), n=-2.86, Ea=(8882, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.1e+19, 's^-1'), n=-3.07, Ea=(9538, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.8e+21, 's^-1'), n=-3.32, Ea=(10859, 'cal/mol'), T0=(1, 'K')),
        ],
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 348,
    reactant1 = 
"""
NH2OH
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
HNOH
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (480000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (6246, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 349,
    reactant1 = 
"""
NH2OH
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
NH2O
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 O U1 L2 E0  {1,S}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (240000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (5064, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 350,
    reactant1 = 
"""
NH2OH
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
HNOH
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (330000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (3863, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 351,
    reactant1 = 
"""
NH2OH
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
NH2O
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 O U1 L2 E0  {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (170000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (3009, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 352,
    reactant1 = 
"""
NH2OH
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HNOH
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2400000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-328, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 353,
    reactant1 = 
"""
NH2OH
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
NH2O
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 O U1 L2 E0  {1,S}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1200000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-596, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 354,
    reactant1 = 
"""
NH2OH
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HNOH
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1600000.0, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (6345, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 355,
    reactant1 = 
"""
NH2OH
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
NH2O
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 O U1 L2 E0  {1,S}
""",
    product2 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (820000, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (5491, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 356,
    reactant1 = 
"""
NH2OH
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HNOH
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1800000.0, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (3227, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 357,
    reactant1 = 
"""
NH2OH
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
NH2O
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 O U1 L2 E0  {1,S}
""",
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (920000, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (1887, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 358,
    reactant1 = 
"""
NH2OH
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
HNOH
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H2O2
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (29000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (9552, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 359,
    reactant1 = 
"""
NH2OH
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
NH2O
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 O U1 L2 E0  {1,S}
""",
    product2 = 
"""
H2O2
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (6414, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 360,
    reactant1 = 
"""
NH2NO
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
""",
    product1 = 
"""
N2
multiplicity 1
1 N U0 L1 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(4.1e+33, 's^-1'), n=-7.78, Ea=(35172, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.1e+34, 's^-1'), n=-7.11, Ea=(36284, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.9e+31, 's^-1'), n=-5.91, Ea=(36175, 'cal/mol'), T0=(1, 'K')),
        ],
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 361,
    reactant1 = 
"""
NH2NO
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
HNNO
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 O U1 L2 E0  {2,S}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (480000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (7407, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 362,
    reactant1 = 
"""
NH2NO
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
HNNO
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 O U1 L2 E0  {2,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (330000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (4697, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 363,
    reactant1 = 
"""
NH2NO
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HNNO
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 O U1 L2 E0  {2,S}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2400000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-70, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 364,
    reactant1 = 
"""
NH2NO
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HNNO
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 O U1 L2 E0  {2,S}
""",
    product2 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1600000.0, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (7179, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 365,
    reactant1 = 
"""
NH2NO
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HNNO
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 O U1 L2 E0  {2,S}
""",
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1800000.0, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (4538, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 366,
    reactant1 = 
"""
NH2NO
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
HNNO
multiplicity 2
1 N U0 L1 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 O U1 L2 E0  {2,S}
""",
    product2 = 
"""
H2O2
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (29000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (12620, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 367,
    reactant1 = 
"""
H2NNHO
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 O U1 L2 E0  {2,S}
""",
    product1 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
HNO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(2.7e+39, 's^-1'), n=-8.74, Ea=(41620, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.4e+40, 's^-1'), n=-8.73, Ea=(41610, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.2e+41, 's^-1'), n=-8.64, Ea=(41580, 'cal/mol'), T0=(1, 'K')),
        ],
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 368,
    reactant1 = 
"""
H2NNHO
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 O U1 L2 E0  {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
HNNHO
multiplicity 2
1 N U0 L0 E+1 {2,S} {3,S} {4,D}
2 N U1 L1 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {1,D}
5 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (480000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-894, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 369,
    reactant1 = 
"""
H2NNHO
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 O U1 L2 E0  {2,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
HNNHO
multiplicity 2
1 N U0 L0 E+1 {2,S} {3,S} {4,D}
2 N U1 L1 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {1,D}
5 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (330000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-894, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 370,
    reactant1 = 
"""
H2NNHO
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 O U1 L2 E0  {2,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HNNHO
multiplicity 2
1 N U0 L0 E+1 {2,S} {3,S} {4,D}
2 N U1 L1 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {1,D}
5 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2400000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1192, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 371,
    reactant1 = 
"""
H2NNHO
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 O U1 L2 E0  {2,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HNNHO
multiplicity 2
1 N U0 L0 E+1 {2,S} {3,S} {4,D}
2 N U1 L1 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {1,D}
5 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1600000.0, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (377, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 372,
    reactant1 = 
"""
H2NNHO
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 O U1 L2 E0  {2,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HNNHO
multiplicity 2
1 N U0 L0 E+1 {2,S} {3,S} {4,D}
2 N U1 L1 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {1,D}
5 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1800000.0, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (-1152, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

entry(
    index        = 373,
    reactant1 = 
"""
H2NNHO
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 O U1 L2 E0  {2,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
HNNHO
multiplicity 2
1 N U0 L0 E+1 {2,S} {3,S} {4,D}
2 N U1 L1 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {1,D}
5 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H2O2
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (29000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1599, 'cal/mol'),
        T0 = (1, 'K'),
        comment = "Reaction and kinetics from Nitrogen_Dean_and_Bozzelli.\nAdded by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,",
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli,
""",
)

