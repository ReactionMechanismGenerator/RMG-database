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
    rank = 5,
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
    rank = 10,
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
    rank = 10,
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
    rank = 10,
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
    rank = 10,
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
    rank = 10,
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
    rank = 10,
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
    rank = 10,
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
    rank = 10,
    shortDesc = """The chemkin file reaction is C2F4BR <=> CF2 + CF2BR""",
    longDesc = 
"""
Training reaction from kinetics library: CF2BrCl
Original entry: C2F4BR <=> CF2 + CF2BR
""",
)

entry(
    index = 10,
    label = "O2 + CF2 <=> CF2O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2560.47,'cm^3/(mol*s)'), n=2.72845, Ea=(64.1698,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.0708, dn = +|- 0.00898775, dEa = +|- 0.048911 kJ/mol"""),
    rank = 5,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 71.944 kJ/mol

Coordinates (Angstoms):
F    -0.746829    1.189537    -0.240732
F    -1.545064    -0.687194    0.261703
O    0.870414    -0.603846    0.187929
O    1.76486    0.176978    -0.102154
C    -0.665311    0.205825    0.604695
""",
)

entry(
    index = 11,
    label = "O2 + CHF <=> CHFO2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(47280.1,'cm^3/(mol*s)'), n=2.41746, Ea=(6.84749,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.05108, dn = +|- 0.00654561, dEa = +|- 0.035621 kJ/mol"""),
    rank = 5,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 12.781 kJ/mol

Coordinates (Angstoms):
H    -0.508707    -0.95089    0.234354
F    -1.388965    0.648677    -0.38389
O    1.179152    0.711778    0.316595
O    1.634311    -0.144637    -0.39772
C    -0.763631    0.068213    0.60273
""",
)

entry(
    index = 12,
    label = "CF2 + F <=> CF3_p",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.18506e+11,'cm^3/(mol*s)'), n=0.4717, Ea=(2.886,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K')),
    rank = 2,
    shortDesc = """VRC-TST high-pressure limit""",
    longDesc = 
"""
VRC-TST CASPT2 aug-cc-pVDZ
Thermal Decomposition of CF3 and the Reaction of CF2 + OH → CF2O + H
N. K. Srinivasan, M.-C. Su, J. V. Michael, A. W. Jasper, S. J. Klippenstein, and L. B. Harding
The Journal of Physical Chemistry A 2008 112 (1), 31-37
DOI: 10.1021/jp076344u
""",
)

entry(
    index = 13,
    label = "CF2 + OH <=> CF2OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.70189e+10,'cm^3/(mol*s)'), n=0.7539, Ea=(3.775,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K')),
    rank = 2,
    shortDesc = """VRC-TST high-pressure limit""",
    longDesc = 
"""
VRC-TST CASPT2 aug-cc-pVDZ
Thermal Decomposition of CF3 and the Reaction of CF2 + OH → CF2O + H
N. K. Srinivasan, M.-C. Su, J. V. Michael, A. W. Jasper, S. J. Klippenstein, and L. B. Harding
The Journal of Physical Chemistry A 2008 112 (1), 31-37
DOI: 10.1021/jp076344u

We are using rate for CF2 + OH -> CF2O + H
For the CF2 + OH reaction, the CF2O + H product channel is highly exothermic 
(55.0 kcal/mol at the QCISD(T)/CBS level). With such a large exothermicity there 
should be essentially no collisional stabilization of the CF2OH complex 
(69.4 kcal/mol exothermic) except perhaps at very low temperature and extraordinarily high pressures.

We will let the RMG PDEP module skip the CF2OH intermediate
""",
)

