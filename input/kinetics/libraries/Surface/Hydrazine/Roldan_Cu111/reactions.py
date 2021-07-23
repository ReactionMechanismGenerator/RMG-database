#!/usr/bin/env python
# encoding: utf-8

name = "Roldan_Cu111"
shortDesc = u""
longDesc = u"""
Based primarily on 
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F
"""

entry(
    index = 1,
    label = "N2H4 + X <=> N2H4_X",
    kinetics = StickingCoefficient(
        A = 1.17E-6,  
        n = 0,
        Ea = (0, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_vdW""",
    longDesc = u"""
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This is R0 in Table 2 at T=300K
""",
    metal = "Cu",
    facet = "111",
)

#Skip R1 (reverse of R0)
# entry(
#     index = 2,
#     label = "N2H4_X <=> N2H4 + X",
#     kinetics = SurfaceArrhenius(
#         A = (4.27e19, '1/s'),  
#         n = -3.337,
#         Ea = (0, 'J/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_vdW""",
#     longDesc = u"""
# "Micro-kinetic simulations of the catalytic decomposition 
# of hydrazine on the Cu(111) surface"
# Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
# DOI:10.1039/C6FD00186F

# A and n was calculated by numpy.linalg.lstsq from Table 1

# This is R1 in Table 1
# """,
#     metal = "Cu",
#     facet = "111",
# )

#Skip R2 (reverse of R3)
# entry(
#     index = 3,
#     label = "NH3_X <=> NH3 + X",
#     kinetics = SurfaceArrhenius(
#         A = (1.29E15, '1/s'),  
#         n = -2.186,
#         Ea = (0, 'J/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_vdW""",
#     longDesc = u"""
# "Micro-kinetic simulations of the catalytic decomposition 
# of hydrazine on the Cu(111) surface"
# Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
# DOI:10.1039/C6FD00186F

# A and n was calculated by numpy.linalg.lstsq from Table 1

# This is R2 in Table 1
# """,
#     metal = "Cu",
#     facet = "111",
# )

entry(
    index = 4,
    label = "NH3 + X <=> NH3_X",
    kinetics = StickingCoefficient(
        A = 1.88E-4,  
        n = 0,
        Ea = (0, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_vdW""",
    longDesc = u"""
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This is R3 in Table 2 at T=300K
""",
    metal = "Cu",
    facet = "111",
)

#Skip R4 (reverse of R5)
# entry(
#     index = 5,
#     label = "N2_X <=> N2 + X",
#     kinetics = SurfaceArrhenius(
#         A = (1.27E18, '1/s'),  
#         n = -2.938,
#         Ea = (0, 'J/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_vdW""",
#     longDesc = u"""
# "Micro-kinetic simulations of the catalytic decomposition 
# of hydrazine on the Cu(111) surface"
# Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
# DOI:10.1039/C6FD00186F

# A and n was calculated by numpy.linalg.lstsq from Table 1

# This is R4 in Table 1
# """,
#     metal = "Cu",
#     facet = "111",
# )

entry(
    index = 6,
    label = "N2 + X <=> N2_X",
    kinetics = StickingCoefficient(
        A = 5.5E-5,  
        n = 0,
        Ea = (0, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_vdW""",
    longDesc = u"""
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This is R5 in Table 2 at T=300K
""",
    metal = "Cu",
    facet = "111",
)

#Skip R6 (reverse of R7)
# entry(
#     index = 7,
#     label = "H_X + H_X <=> H2 + X + X",
#     kinetics = SurfaceArrhenius(
#         A = (1.54E21, 'cm^2/(mol*s)'),  
#         n = 0.044,
#         Ea = (104209, 'J/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""H2 Surface_Adsorption_Dissociative""",
#     longDesc = u"""
# "Micro-kinetic simulations of the catalytic decomposition 
# of hydrazine on the Cu(111) surface"
# Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
# DOI:10.1039/C6FD00186F

# This reaction used RMG's surface site density of Cu111 = 2.943E-9(mol/cm^2) to calculate the A factor.
# A and n was calculated by numpy.linalg.lstsq from Table 1

# This is R6 in Table 1
# """,
#     metal = "Cu",
#     facet = "111",
# )

entry(
    index = 8,
    label = "H2 + X + X <=> H_X + H_X",
    kinetics = StickingCoefficient(
        A = 2.36E-2,  
        n = 0,
        Ea = (0, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""H2 Surface_Adsorption_Dissociative""",
    longDesc = u"""
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This is R7 in Table 2 at T=300K
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 9,
    label = "N2H4_X + X <=> N2H3_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (2.69E18, 'cm^2/(mol*s)'),  
        n = 1.22,
        Ea = (125437, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This reaction used RMG's surface site density of Cu111 = 2.943E-9(mol/cm^2) to estimate A factor.
A and n was calculated by numpy.linalg.lstsq from Table 1

This is R8 in Table 1
""",
    metal = "Cu",
    facet = "111",
)

#Skip R9 (reverse of R10)

entry(
    index = 10,
    label = "N2H3_X + X <=> NN=[Pt] + H_X",
    kinetics = SurfaceArrhenius(
        A = (1.34E17, 'cm^2/(mol*s)'),  
        n = 1.942,
        Ea = (121577, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This reaction used RMG's surface site density of Cu111 = 2.943E-9(mol/cm^2) to estimate A factor.
A and n was calculated by numpy.linalg.lstsq from Table 1

This is R10 in Table 1
""",
    metal = "Cu",
    facet = "111",
)

#Skip R11 (reverse of R12)

entry(
    index = 11,
    label = "N2H3_X + X + X <=> [Pt]NN[Pt] + H_X",
    kinetics = SurfaceArrhenius(
        A = (1.95E18, 'cm^4/(mol^2*s)'),  
        n = 1.376,
        Ea = (130262, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This reaction used RMG's surface site density of Cu111 = 2.943E-9(mol/cm^2) to estimate A factor.
A and n was calculated by numpy.linalg.lstsq from Table 1

This is R12 in Table 1
""",
    metal = "Cu",
    facet = "111",
)

#Skip R13 (reverse of R12)    

entry(
    index = 12,
    label = "NN=[Pt] + X <=> [Pt]N=N + H_X",
    kinetics = SurfaceArrhenius(
        A = (1.09E19, 'cm^2/(mol*s)'),  
        n = 1.002,
        Ea = (108069, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_Beta""",
    longDesc = u"""
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

#Skip R15 (reverse of R14)

entry(
    index = 13,
    label = "[Pt]NN[Pt] + X <=> [Pt]NN=[Pt] + H_X",
    kinetics = SurfaceArrhenius(
        A = (1.07E19, 'cm^2/(mol*s)'),  
        n = 1.134,
        Ea = (141840, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This reaction used RMG's surface site density of Cu111 = 2.943E-9(mol/cm^2) to estimate A factor.
A and n was calculated by numpy.linalg.lstsq from Table 1

This is R16 in Table 1
""",
    metal = "Cu",
    facet = "111",
)

#Skip R17 (reverse of R16)

entry(
    index = 14,
    label = "[Pt]NN=[Pt] + X <=> [Pt]=NN=[Pt] + H_X",
    kinetics = SurfaceArrhenius(
        A = (3.43E18, 'cm^2/(mol*s)'),  
        n = 1.285,
        Ea = (16403, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This reaction used RMG's surface site density of Cu111 = 2.943E-9(mol/cm^2) to estimate A factor.
A and n was calculated by numpy.linalg.lstsq from Table 1

This is R18 in Table 1
""",
    metal = "Cu",
    facet = "111",
)

#Skip R19 (reverse of R18)

entry(
    index = 15,
    label = "N2H4_X + X <=> NH2_X + NH2_X",
    kinetics = SurfaceArrhenius(
        A = (6.61E17, 'cm^2/(mol*s)'),  
        n = 1.589,
        Ea = (66578, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This reaction used RMG's surface site density of Cu111 = 2.943E-9(mol/cm^2) to estimate A factor.
A and n was calculated by numpy.linalg.lstsq from Table 1

This is R20 in Table 1
""",
    metal = "Cu",
    facet = "111",
)

#Skip R21 (reverse of R20)

entry(
    index = 16,
    label = "N2H3_X + X <=> NH2_X + NH_X",
    kinetics = SurfaceArrhenius(
        A = (2.87E16, 'cm^2/(mol*s)'),  
        n = 2.065,
        Ea = (86841, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This reaction used RMG's surface site density of Cu111 = 2.943E-9(mol/cm^2) to estimate A factor.
A and n was calculated by numpy.linalg.lstsq from Table 1

This is R22 in Table 1
""",
    metal = "Cu",
    facet = "111",
)

#Skip R23 (reverse of R22)

entry(
    index = 17,
    label = "NN=[Pt] + X <=> NH2_X + N_X",
    kinetics = SurfaceArrhenius(
        A = (4.03E19, 'cm^2/(mol*s)'),  
        n = 0.559,
        Ea = (130262, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This reaction used RMG's surface site density of Cu111 = 2.943E-9(mol/cm^2) to estimate A factor.
A and n was calculated by numpy.linalg.lstsq from Table 1

This is R24 in Table 1
""",
    metal = "Cu",
    facet = "111",
)

#Skip R25 (reverse of R24)

entry(
    index = 18,
    label = "[Pt]NN[Pt] <=> NH_X + NH_X",
    kinetics = SurfaceArrhenius(
        A = (4.39E11, '1/s'),  
        n = 0.299,
        Ea = (76227, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = """Surface_Bidentate_Dissociation""",
    longDesc = u"""
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

A and n was calculated by numpy.linalg.lstsq from Table 1

This is R26 in Table 1
""",
    metal = "Cu",
    facet = "111",
)

#Skip R27 (reverse of R26)

entry(
    index = 19,
    label = "[Pt]NN=[Pt] <=> NH_X + N_X",
    kinetics = SurfaceArrhenius(
        A = (2.59E11, '1/s'),  
        n = 0.619,
        Ea = (137016, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Bidentate_Dissociation""",
    longDesc = u"""
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

A and n was calculated by numpy.linalg.lstsq from Table 1

This is R28 in Table 1
""",
    metal = "Cu",
    facet = "111",
)

#Skip R29 (reverse of R28)

entry(
    index = 20,
    label = "NH3_X + X <=> NH2_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (5.93E17, 'cm^2/(mol*s)'), 
        n = 1.321,
        Ea = (136051, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This reaction used RMG's surface site density of Cu111 = 2.943E-9(mol/cm^2) to estimate A factor.
A and n was calculated by numpy.linalg.lstsq from Table 1

This is R30 in Table 1
""",
    metal = "Cu",
    facet = "111",
)

#Skip R31 (reverse of R30)

entry(
    index = 21,
    label = "NH2_X + X <=> NH_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (5.67E19, 'cm^2/(mol*s)'), 
        n = 0.513,
        Ea = (135086, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This reaction used RMG's surface site density of Cu111 = 2.943E-9(mol/cm^2) to estimate A factor.
A and n was calculated by numpy.linalg.lstsq from Table 1

This is R32 in Table 1
""",
    metal = "Cu",
    facet = "111",
)

#Skip R33 (reverse of R32)

entry(
    index = 22,
    label = "NH_X + X <=> N_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (1.66E19, 'cm^2/(mol*s)'), 
        n = 0.853,
        Ea = (172717, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This reaction used RMG's surface site density of Cu111 = 2.943E-9(mol/cm^2) to estimate A factor.
A and n was calculated by numpy.linalg.lstsq from Table 1

This is R34 in Table 1
""",
    metal = "Cu",
    facet = "111",
)

#Skip R35 (reverse of R34)

entry(
    index = 23,
    label = "NH2_X + NH2_X <=> NH_X + NH3_X",
    kinetics = SurfaceArrhenius(
        A = (1.16E20, 'cm^2/(mol*s)'), 
        n = 0.667,
        Ea = (43420, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This reaction used RMG's surface site density of Cu111 = 2.943E-9(mol/cm^2) to estimate A factor.
A and n was calculated by numpy.linalg.lstsq from Table 1

This is R36 in Table 1
""",
    metal = "Cu",
    facet = "111",
)

#Skip R37 (reverse of R36)

entry(
    index = 24,
    label = "N2H4_X + NH2_X <=> N2H3_X + NH3_X",
    kinetics = SurfaceArrhenius(
        A = (3.38E20, 'cm^2/(mol*s)'),  
        n = 0.156,
        Ea = (40526, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_Single_vdW""",
    longDesc = u"""
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This reaction used RMG's surface site density of Cu111 = 2.943E-9(mol/cm^2) to estimate A factor.
A and n was calculated by numpy.linalg.lstsq from Table 1

This is R38 in Table 1
""",
    metal = "Cu",
    facet = "111",
)

#Skip R39 (reverse of R38)

entry(
    index = 25,
    label = "N2H3_X + NH2_X + X <=> [Pt]NN[Pt] + NH3_X",
    kinetics = SurfaceArrhenius(
        A = (4.46E19, 'cm^4/(mol^2*s)'),  
        n = 0.659,
        Ea = (61754, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This reaction used RMG's surface site density of Cu111 = 2.943E-9(mol/cm^2) to estimate A factor.
A and n was calculated by numpy.linalg.lstsq from Table 1

This is R40 in Table 1
""",
    metal = "Cu",
    facet = "111",
)

#Skip R41 (reverse of R40)

entry(
    index = 26,
    label = "N2H3_X + NH2_X <=> NN=[Pt] + NH3_X",
    kinetics = SurfaceArrhenius(
        A = (1.02E19, 'cm^2/(mol*s)'),  
        n = 1.073,
        Ea = (51140, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This reaction used RMG's surface site density of Cu111 = 2.943E-9(mol/cm^2) to estimate A factor.
A and n was calculated by numpy.linalg.lstsq from Table 1

This is R42 in Table 1
""",
    metal = "Cu",
    facet = "111",
)

#Skip R43 (reverse of R42)

entry(
    index = 27,
    label = "[Pt]NN[Pt] + NH2_X <=> [Pt]NN=[Pt] + NH3_X",
    kinetics = SurfaceArrhenius(
        A = (1.94E20, 'cm^2/(mol*s)'),  
        n = 0.577,
        Ea = (24122, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This reaction used RMG's surface site density of Cu111 = 2.943E-9(mol/cm^2) to estimate A factor.
A and n was calculated by numpy.linalg.lstsq from Table 1

This is R44 in Table 1
""",
    metal = "Cu",
    facet = "111",
)

#Skip R45 (reverse of R44)

entry(
    index = 28,
    label = "NN=[Pt] + NH2_X <=> [Pt]N=N + NH3_X",
    kinetics = SurfaceArrhenius(
        A = (3.51E19, 'cm^2/(mol*s)'),  
        n = 0.966,
        Ea = (28947, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This reaction used RMG's surface site density of Cu111 = 2.943E-9(mol/cm^2) to estimate A factor.
A and n was calculated by numpy.linalg.lstsq from Table 1

This is R46 in Table 1
""",
    metal = "Cu",
    facet = "111",
)

#Skip R47 (reverse of R46)

entry(
    index = 29,
    label = "[Pt]NN=[Pt] + NH2_X <=> [Pt]=NN=[Pt] + NH3_X",
    kinetics = SurfaceArrhenius(
        A = (4.04E19, 'cm^2/(mol*s)'),  
        n = 0.86,
        Ea = (7719, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This reaction used RMG's surface site density of Cu111 = 2.943E-9(mol/cm^2) to estimate A factor.
A and n was calculated by numpy.linalg.lstsq from Table 1

This is R48 in Table 1
""",
    metal = "Cu",
    facet = "111",
)

#Skip R49 (reverse of R48)

entry(
    index = 30,
    label = "[Pt]=NN=[Pt] <=> N_X + N_X",
    kinetics = SurfaceArrhenius(
        A = (4.77E11, '1/s'), 
        n = 0.06,
        Ea = (452538, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Bidentate_Dissociation""",
    longDesc = u"""
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

A and n was calculated by numpy.linalg.lstsq from Table 1

This is R50 in Table 1
""",
    metal = "Cu",
    facet = "111",
)

#Skip R51 (reverse of R50)
