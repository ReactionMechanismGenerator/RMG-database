#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Bidentate_Dissociation/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 1,
    label = "H2N2X2 <=> HNX + HNX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.49e+20,'1/s'), n=0.299, Ea=(76227,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Cu111
Original entry: [Pt]NN[Pt] <=> NH_X + NH_X
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This reaction used RMG's surface site density of Cu111 = 2.943E-9(mol/cm^2) to estimate A factor.
A and n was calculated by numpy.linalg.lstsq from Table 1

This is R26 in Table 1
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 2,
    label = "HN2X2 <=> HNX + NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(8.81e+19,'1/s'), n=0.619, Ea=(137016,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Bidentate_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Cu111
Original entry: [Pt]NN=[Pt] <=> NH_X + N_X
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This reaction used RMG's surface site density of Cu111 = 2.943E-9(mol/cm^2) to estimate A factor.
A and n was calculated by numpy.linalg.lstsq from Table 1

This is R28 in Table 1
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 3,
    label = "N2X2 <=> NX-2 + NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.62e+20,'1/s'), n=0.06, Ea=(452538,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Bidentate_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Cu111
Original entry: [Pt]=NN=[Pt] <=> N_X + N_X
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This reaction used RMG's surface site density of Cu111 = 2.943E-9(mol/cm^2) to estimate A factor.
A and n was calculated by numpy.linalg.lstsq from Table 1

This is R50 in Table 1
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 4,
    label = "HN2X2 <=> HNX + NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.87e+21,'1/s'), n=0, Ea=(137981,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Bidentate_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Ir111
Original entry: [Pt]NN=[Pt] <=> NH_X + N_X
"Mechanistic study of hydrazine decomposition on Ir(111)"
Alberto Roldan et al. Phys.Chem.Chem.Phys., 2020, 22, 3883
DOI: 10.1039/c9cp06525c

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2)
to estimate a default(1E13) A factor.
A = 1E13(mol/cm^2/s)/2.587E-9(mol/cm^2) = 3.87E21 (1/s)
Ea = 1.43eV = 137980.7J/mol

This is R15 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 5,
    label = "NX-2 + NX <=> N2X2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.55e+21,'cm^2/(mol*s)'), n=0, Ea=(187423,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Bidentate_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Ir111
Original entry: N_X + N_X <=> [Pt]=NN=[Pt]
"Kinetic and mechanistic analysis of NH3 decomposition 
on Ru(0001), Ru(111) and Ir(111) surfaces"
Alberto Roldan et al. Nanoscale Adv., 2021, 3, 1624
DOI: 10.1039/d1na00015b

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2) to estimate A factor.
A = 9.18E12(1/s)/2.587E-9(mol/cm^2) = 3.55E21 cm^2/(mol*s)
Ea was calculated from A factor and k rate constant in Table 3

This is R7 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

