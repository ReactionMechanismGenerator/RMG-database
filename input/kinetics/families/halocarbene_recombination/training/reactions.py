#!/usr/bin/env python
# encoding: utf-8

name = "halocarbene_recombination/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 1,
    label = "CF2 + CH3 <=> CF2CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.1e+13,'cm^3/(mol*s)'), n=-0.207, Ea=(0,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CF3-CF2 <=> CF2 + CF3""",
    longDesc = 
"""
Experimental and Quantum Chemical Study of the Reaction CF2 + CH3 ↔ CF2CH3 → CH2CF2 + H:  
A Key Mechanism in the Reaction between Methane and Fluorocarbons
https://doi.org/10.1021/ie060221z
https://kinetics.nist.gov/kinetics/Detail?id=2006YU/MAC3758-3762:1

CF2 + CH3 -> CF2CH3 -> CF2=CH2 + H

PES calculated at the G3 level of theory
The authors investigated the potential energy surface for the reaction via both density functional and MP2 methods. 
They conclude that CF2CH3 is formed as an intermediate but undergoes essentially no stabilization 
under the reported conditions. We will make the intermediate CF2CH3 and let RMG decide via the PDEP module whether or not
to skip the well
""",
)
entry(
    index = 2,
    label = "CF2 + H <=> CHF2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.75e+06,'cm^3/(mol*s)'), n=-0.32, Ea=(7696,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CF2 + H <=> CHF2""",
    longDesc = 
"""
Training reaction from kinetics library: CF2BrCl
Original entry: CF2 + H <=> CHF2
""",
)

entry(
    index = 3,
    label = "C2F5 <=> CF3 + CF2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.27e+15,'s^-1'), n=0, Ea=(56240,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CF3-CF2 <=> CF2 + CF3""",
    longDesc = 
"""
Training reaction from kinetics library: CF2BrCl
Original entry: CF3-CF2 <=> CF2 + CF3
""",
)

entry(
    index = 4,
    label = "CCl2 + Cl <=> CCl3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.58e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CCL2 + CL <=> CCL3""",
    longDesc = 
"""
Training reaction from kinetics library: CF2BrCl
Original entry: CCL2 + CL <=> CCL3
""",
)

entry(
    index = 5,
    label = "CCl2 + H <=> CHCl2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CCL2 + H <=> CHCL2""",
    longDesc = 
"""
Training reaction from kinetics library: CF2BrCl
Original entry: CCL2 + H <=> CHCL2
""",
)

entry(
    index = 6,
    label = "CClF + Cl <=> CCl2F",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CFCL + CL <=> CFCL2""",
    longDesc = 
"""
Training reaction from kinetics library: CF2BrCl
Original entry: CFCL + CL <=> CFCL2
""",
)

entry(
    index = 7,
    label = "C2Cl2F3 <=> CF3 + CCl2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+15,'s^-1'), n=0, Ea=(79000,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CF3CCL2 <=> CF3 + CCL2""",
    longDesc = 
"""
Training reaction from kinetics library: CF2BrCl
Original entry: CF3CCL2 <=> CF3 + CCL2
""",
)

entry(
    index = 8,
    label = "C2ClF4 <=> CClF2 + CF2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.27e+15,'s^-1'), n=0, Ea=(56240,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C2F4CL <=> CF2 + CF2CL""",
    longDesc = 
"""
Training reaction from kinetics library: CF2BrCl
Original entry: C2F4CL <=> CF2 + CF2CL
""",
)

entry(
    index = 9,
    label = "C2BrF4 <=> CBrF2 + CF2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.27e+15,'s^-1'), n=0, Ea=(56240,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C2F4BR <=> CF2 + CF2BR""",
    longDesc = 
"""
Training reaction from kinetics library: CF2BrCl
Original entry: C2F4BR <=> CF2 + CF2BR
""",
)

