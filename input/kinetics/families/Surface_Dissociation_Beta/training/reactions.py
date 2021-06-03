#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_Beta/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 1,
    label = "CO* + H* <=> COH* + X",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (3.799e17, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (2.26, 'eV/molecule'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 27 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/c s200055d

A factor from paper / surface site density of Cu
1.118e13 1/s / 2.943e‐5 mol/m^2 = 3.799e17 m^2/(mol*s)
""", 
    metal = "Cu",
)

entry(
    index = 2,
    label = "HCO* + H* <=> HCOH* + X",
    degeneracy = 4,
    kinetics = SurfaceArrhenius(
        A = (3.048e17, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (0.91, 'eV/molecule'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 29 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/c s200055d

A factor from paper / surface site density of Cu
8.971e12 1/s / 2.943e‐5 mol/m^2 = 3.048e17 m^2/(mol*s)
""", 
    metal = "Cu",
)

entry(
    index = 3,
    label = "X + H2N2X <=> HN2X + H*",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.09e19,'cm^2/(mol*s)'), n=1.002, Ea=(108069,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_Beta""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Cu111
Original entry: NN=[Pt] + X <=> [Pt]N=N + H_X
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This reaction used RMG's surface site density of Cu111 = 2.943E-9(mol/cm^2) to estimate A factor.
A and n was calculated by numpy.linalg.lstsq from Table 1

This is R14 in Table 1
""",
    metal = "Cu",
    facet = "111",
)

