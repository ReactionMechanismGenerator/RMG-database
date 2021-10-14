#!/usr/bin/env python
# encoding: utf-8

name = "halocarbene_recombination_double/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 1,
    label = "CH2 + CHF <=> C2H3F",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.1e+24,'cm^3/(mol*s)'), n=-3.8, Ea=(2830,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is CH2(S) + CHF <=> CH2CHF""",
    longDesc = 
"""
Training reaction from kinetics library: NIST_Fluorine/seed
Original entry: CH2(S) + CHF <=> CH2CHF
""",
)

entry(
    index = 2,
    label = "CH2 + CF2 <=> C2H2F2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.1e+24,'cm^3/(mol*s)'), n=-3.8, Ea=(2830,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is CH2(S) + CF2 <=> CH2CF2""",
    longDesc = 
"""
Training reaction from kinetics library: NIST_Fluorine/seed
Original entry: CH2(S) + CF2 <=> CH2CF2
""",
)

entry(
    index = 3,
    label = "CHF + CHF-2 <=> C2H2F2-2",
    degeneracy = 0.5,
    kinetics = Arrhenius(A=(3.1e+24,'cm^3/(mol*s)'), n=-3.8, Ea=(2830,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is CHF + CHF <=> CHFCHF[Z]""",
    longDesc = 
"""
Training reaction from kinetics library: NIST_Fluorine/seed
Original entry: CHF + CHF <=> CHFCHF[Z]
""",
)

entry(
    index = 4,
    label = "CHF + CF2-2 <=> C2HF3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.1e+24,'cm^3/(mol*s)'), n=-3.8, Ea=(2830,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is CHF + CF2 <=> CHFCF2""",
    longDesc = 
"""
Training reaction from kinetics library: NIST_Fluorine/seed
Original entry: CHF + CF2 <=> CHFCF2
""",
)

entry(
    index = 5,
    label = "CCl2 + CCl2-2 <=> C2Cl4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.25e+11,'cm^3/(mol*s)'), T0=(300,'K'), n=0.7, Ea=(0, 'kJ/mol')),
    rank = 1,
    shortDesc = """CCl2 self recombination""",
    longDesc = 
"""
high pressure rate constant
k∞ (SACM/CT) = (5.4 ± 3.0) × 10−13 (T/300)0.7 ± 0.1 cm3 molecule−1 s−1.
Quantum chemical and kinetic study of the CCl2 self-recombination reaction
https://doi.org/10.1016/j.comptc.2017.10.004
simplified statistical adiabatic channel model with classical trajectory calculations (SACM/CT)
""",
)

entry(
    index = 6,
    label = "CF2 + CF2-2 <=> C2F4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.26e+10,'cm^3/(mol*s)'), T0=(300,'K'), n=1.53, Ea=(0, 'kJ/mol')),
    rank = 1,
    shortDesc = """CF2 self recombination""",
    longDesc = 
"""
high pressure rate constant
SACM/CT (statistical adiabatic channel model/classical trajectories)
Experimental and Modeling Study of the Reaction C2F4 (+M)⇔CF2 +CF2 (+M)
J. Phys. Chem. A 2013, 117, 45, 11420–11429
https://doi.org/10.1021/jp408363s
""",
)
