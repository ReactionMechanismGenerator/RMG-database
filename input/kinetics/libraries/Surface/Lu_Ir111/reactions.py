#!/usr/bin/env python
# encoding: utf-8

name = "Lu_Ir111"
shortDesc = u""
longDesc = u"""
Based primarily on 
"Mechanistic study of hydrazine decomposition on Ir(111)"
Xiuyuan Lu et al. Phys.Chem.Chem.Phys., 2020, 22, 3883
DOI: 10.1039/c9cp06525c

and

"Kinetic and mechanistic analysis of NH3 decomposition 
on Ru(0001), Ru(111) and Ir(111) surfaces"
Xiuyuan Lu et al. Nanoscale Adv., 2021, 3, 1624
DOI: 10.1039/d1na00015b
"""
#skip R1

entry(
    index = 2,
    label = "NH3_X <=> NH3 + X",
    kinetics = SurfaceArrhenius(
        A = (3.68E16, '1/s'),  
        n = 0.0,
        Ea = (88574.75, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_vdW""",
    longDesc = u"""
"Kinetic and mechanistic analysis of NH3 decomposition 
on Ru(0001), Ru(111) and Ir(111) surfaces"
Xiuyuan Lu et al. Nanoscale Adv., 2021, 3, 1624
DOI: 10.1039/d1na00015b

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2) to calculate the A factor.
A = 9.53E7(mol/cm^2/s)/2.587E-9(mol/cm^2) = 3.68E16 (1/s)
Ea was calculated from A factor and k rate constant in Table 3

This is D1 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 3,
    label = "N2_X <=> N2 + X + X",
    kinetics = SurfaceArrhenius(
        A = (3.68E16, '1/s'),  
        n = 0.0,
        Ea = (10806.96, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Bidentate""",
    longDesc = u"""
"Kinetic and mechanistic analysis of NH3 decomposition 
on Ru(0001), Ru(111) and Ir(111) surfaces"
Xiuyuan Lu et al. Nanoscale Adv., 2021, 3, 1624
DOI: 10.1039/d1na00015b

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2) to calculate the A factor.
A = 9.52E7(mol/cm^2/s)/2.587E-9(mol/cm^2) = 3.68E16 (1/s)
Ea was calculated from A factor and k rate constant in Table 3

This is D2 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 4,
    label = "H2_X <=> H2 + X",
    kinetics = SurfaceArrhenius(
        A = (3.69E16, '1/s'),  
        n = 0.0,
        Ea = (30972.36, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""H2 Surface_Adsorption_vdW""",
    longDesc = u"""
"Kinetic and mechanistic analysis of NH3 decomposition 
on Ru(0001), Ru(111) and Ir(111) surfaces"
Xiuyuan Lu et al. Nanoscale Adv., 2021, 3, 1624
DOI: 10.1039/d1na00015b

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2) to calculate the A factor.
A = 9.54E7(mol/cm^2/s)/2.587E-9(mol/cm^2) = 3.69E16 (1/s)
Ea was calculated from A factor and k rate constant in Table 3

This is D3 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 5,
    label = "N2H4_X + X <=> N2H3_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (3.87E21, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (104209.2, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""
"Mechanistic study of hydrazine decomposition on Ir(111)"
Xiuyuan Lu et al. Phys.Chem.Chem.Phys., 2020, 22, 3883
DOI: 10.1039/c9cp06525c

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2)
to estimate a default(1E13) A factor.
A = 1E13(1/s)/2.587E-9(mol/cm^2) = 3.87E21 cm^2/(mol*s)
Ea = 1.08eV = 104209.2J/mol

This is R5 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 6,
    label = "N2H3_X + X <=> NN=[Pt] + H_X",
    kinetics = SurfaceArrhenius(
        A = (3.87E21, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (98419.8, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"Mechanistic study of hydrazine decomposition on Ir(111)"
Xiuyuan Lu et al. Phys.Chem.Chem.Phys., 2020, 22, 3883
DOI: 10.1039/c9cp06525c

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2)
to estimate a default(1E13) A factor.
A = 1E13(1/s)/2.587E-9(mol/cm^2) = 3.87E21 cm^2/(mol*s)
Ea = 1.02eV = 98419.8J/mol

This is R6 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

#Skip 7 

entry(
    index = 8,
    label = "[Pt]NN[Pt] + X <=> [Pt]NN=[Pt] + H_X",
    kinetics = SurfaceArrhenius(
        A = (3.87E21, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (67543, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"Mechanistic study of hydrazine decomposition on Ir(111)"
Xiuyuan Lu et al. Phys.Chem.Chem.Phys., 2020, 22, 3883
DOI: 10.1039/c9cp06525c

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2)
to estimate a default(1E13) A factor.
A = 1E13(1/s)/2.587E-9(mol/cm^2) = 3.87E21 cm^2/(mol*s)
Ea = 0.7eV = 67543J/mol

This is R8 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

#skip R9

entry(
    index = 10,
    label = "[Pt]NN=[Pt] + X <=> N2_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (3.87E21, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (126401.9, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"Mechanistic study of hydrazine decomposition on Ir(111)"
Xiuyuan Lu et al. Phys.Chem.Chem.Phys., 2020, 22, 3883
DOI: 10.1039/c9cp06525c

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2)
to estimate a default(1E13) A factor.
A = 1E13(1/s)/2.587E-9(mol/cm^2) = 3.87E21 cm^2/(mol*s)
Ea = 1.31eV = 126401.9J/mol

This is R10 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 11,
    label = "N2H4_X + X <=> NH2_X + NH2_X",
    kinetics = SurfaceArrhenius(
        A = (3.87E21, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (68507.9, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""
"Mechanistic study of hydrazine decomposition on Ir(111)"
Xiuyuan Lu et al. Phys.Chem.Chem.Phys., 2020, 22, 3883
DOI: 10.1039/c9cp06525c

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2)
to estimate a default(1E13) A factor.
A = 1E13(1/s)/2.587E-9(mol/cm^2) = 3.87E21 cm^2/(mol*s)
Ea = 0.71eV = 68507.9J/mol

This is R11 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 12,
    label = "N2H3_X + X <=> NH2_X + NH_X",
    kinetics = SurfaceArrhenius(
        A = (3.87E21, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (75262.2, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"Mechanistic study of hydrazine decomposition on Ir(111)"
Xiuyuan Lu et al. Phys.Chem.Chem.Phys., 2020, 22, 3883
DOI: 10.1039/c9cp06525c

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2)
to estimate a default(1E13) A factor.
A = 1E13(1/s)/2.587E-9(mol/cm^2) = 3.87E21 cm^2/(mol*s)
Ea = 0.78eV = 75262.2J/mol

This is R12 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 13,
    label = "NN=[Pt] + X <=> NH2_X + N_X",
    kinetics = SurfaceArrhenius(
        A = (3.87E21, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (70437.7, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"Mechanistic study of hydrazine decomposition on Ir(111)"
Xiuyuan Lu et al. Phys.Chem.Chem.Phys., 2020, 22, 3883
DOI: 10.1039/c9cp06525c

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2)
to estimate a default(1E13) A factor.
A = 1E13(1/s)/2.587E-9(mol/cm^2) = 3.87E21 cm^2/(mol*s)
Ea = 0.73eV = 70437.7J/mol

This is R13 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 14,
    label = "N2H2_X + X <=> NH_X + NH_X",
    kinetics = SurfaceArrhenius(
        A = (3.87E21, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (70437.7, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_Double_vdW""",
    longDesc = u"""
"Mechanistic study of hydrazine decomposition on Ir(111)"
Xiuyuan Lu et al. Phys.Chem.Chem.Phys., 2020, 22, 3883
DOI: 10.1039/c9cp06525c

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2)
to estimate a default(1E13) A factor.
A = 1E13(1/s)/2.587E-9(mol/cm^2) = 3.87E21 cm^2/(mol*s)
Ea = 0.73eV = 70437.7J/mol

This is R14 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 15,
    label = "[Pt]NN=[Pt] <=> NH_X + N_X",
    kinetics = SurfaceArrhenius(
        A = (3.87E21, '1/s'),  
        n = 0.0,
        Ea = (137980.7, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Bidentate_Dissociation""",
    longDesc = u"""
"Mechanistic study of hydrazine decomposition on Ir(111)"
Xiuyuan Lu et al. Phys.Chem.Chem.Phys., 2020, 22, 3883
DOI: 10.1039/c9cp06525c

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2)
to estimate a default(1E13) A factor.
A = 1E13(1/s)/2.587E-9(mol/cm^2) = 3.87E21 cm^2/(mol*s)
Ea = 1.43eV = 137980.7J/mol

This is R15 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 16,
    label = "N2H4_X + NH2_X <=> N2H3_X + NH3_X",
    kinetics = SurfaceArrhenius(
        A = (3.87E21, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (19298, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""
"Mechanistic study of hydrazine decomposition on Ir(111)"
Xiuyuan Lu et al. Phys.Chem.Chem.Phys., 2020, 22, 3883
DOI: 10.1039/c9cp06525c

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2)
to estimate a default(1E13) A factor.
A = 1E13(1/s)/2.587E-9(mol/cm^2) = 3.87E21 cm^2/(mol*s)
Ea = 0.2eV = 19298J/mol

This is R16 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 17,
    label = "N2H3_X + NH2_X <=> N2H2_X + NH3_X",
    kinetics = SurfaceArrhenius(
        A = (3.87E21, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (22192.7, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"Mechanistic study of hydrazine decomposition on Ir(111)"
Xiuyuan Lu et al. Phys.Chem.Chem.Phys., 2020, 22, 3883
DOI: 10.1039/c9cp06525c

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2)
to estimate a default(1E13) A factor.
A = 1E13(1/s)/2.587E-9(mol/cm^2) = 3.87E21 cm^2/(mol*s)
Ea = 0.23eV = 22192.7J/mol

This is R17 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 18,
    label = "[Pt]NN[Pt] + NH2_X <=> [Pt]NN=[Pt] + NH3_X",
    kinetics = SurfaceArrhenius(
        A = (3.87E21, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (18333.1, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"Mechanistic study of hydrazine decomposition on Ir(111)"
Xiuyuan Lu et al. Phys.Chem.Chem.Phys., 2020, 22, 3883
DOI: 10.1039/c9cp06525c

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2)
to estimate a default(1E13) A factor.
A = 1E13(1/s)/2.587E-9(mol/cm^2) = 3.87E21 cm^2/(mol*s)
Ea = 0.19eV = 18333.1J/mol

This is R18 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 19,
    label = "N2H3_X + NH2_X <=> NN=[Pt] + NH3_X",
    kinetics = SurfaceArrhenius(
        A = (3.87E21, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (35701.3, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"Mechanistic study of hydrazine decomposition on Ir(111)"
Xiuyuan Lu et al. Phys.Chem.Chem.Phys., 2020, 22, 3883
DOI: 10.1039/c9cp06525c

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2)
to estimate a default(1E13) A factor.
A = 1E13(1/s)/2.587E-9(mol/cm^2) = 3.87E21 cm^2/(mol*s)
Ea = 0.37eV = 35701.3J/mol

This is R19 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 20,
    label = "N2H2_X + NH2_X <=> N2H_X + NH3_X",
    kinetics = SurfaceArrhenius(
        A = (3.87E21, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (98419.8, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""
"Mechanistic study of hydrazine decomposition on Ir(111)"
Xiuyuan Lu et al. Phys.Chem.Chem.Phys., 2020, 22, 3883
DOI: 10.1039/c9cp06525c

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2)
to estimate a default(1E13) A factor.
A = 1E13(1/s)/2.587E-9(mol/cm^2) = 3.87E21 cm^2/(mol*s)
Ea = 1.02eV = 98419.8J/mol

This is R20 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 21,
    label = "[Pt]NN=[Pt] + NH2_X <=> N2_X + NH3_X",
    kinetics = SurfaceArrhenius(
        A = (3.87E21, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (53069.5, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"Mechanistic study of hydrazine decomposition on Ir(111)"
Xiuyuan Lu et al. Phys.Chem.Chem.Phys., 2020, 22, 3883
DOI: 10.1039/c9cp06525c

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2)
to estimate a default(1E13) A factor.
A = 1E13(1/s)/2.587E-9(mol/cm^2) = 3.87E21 cm^2/(mol*s)
Ea = 0.55eV = 53069.5J/mol

This is R21 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 22,
    label = "NH3_X + X <=> NH2_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (1.22E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (147114.22, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""
"Kinetic and mechanistic analysis of NH3 decomposition 
on Ru(0001), Ru(111) and Ir(111) surfaces"
Xiuyuan Lu et al. Nanoscale Adv., 2021, 3, 1624
DOI: 10.1039/d1na00015b

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2) to calculate the A factor.
A = 3.15E12(1/s)/2.587E-9(mol/cm^2) = 1.22E21 cm^2/(mol*s)
Ea was calculated from A factor and k rate constant in Table 3

This is R1 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 23,
    label = "NH2_X + X <=> NH_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (1.43E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (151612.95, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"Kinetic and mechanistic analysis of NH3 decomposition 
on Ru(0001), Ru(111) and Ir(111) surfaces"
Xiuyuan Lu et al. Nanoscale Adv., 2021, 3, 1624
DOI: 10.1039/d1na00015b

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2) to calculate the A factor.
A = 3.71E12(1/s)/2.587E-9(mol/cm^2) = 1.43E21 cm^2/(mol*s)
Ea was calculated from A factor and k rate constant in Table 3

This is R3 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 24,
    label = "NH_X + X <=> N_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (2.68E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (88354.08, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"Kinetic and mechanistic analysis of NH3 decomposition 
on Ru(0001), Ru(111) and Ir(111) surfaces"
Xiuyuan Lu et al. Nanoscale Adv., 2021, 3, 1624
DOI: 10.1039/d1na00015b

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2) to calculate the A factor.
A = 6.93E12(1/s)/2.587E-9(mol/cm^2) = 2.68E21 cm^2/(mol*s)
Ea was calculated from A factor and k rate constant in Table 3

This is R5 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 25,
    label = "NH2_X + NH2_X <=> NH_X + NH3_X",
    kinetics = SurfaceArrhenius(
        A = (3.87E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (32806.6, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"Mechanistic study of hydrazine decomposition on Ir(111)"
Xiuyuan Lu et al. Phys.Chem.Chem.Phys., 2020, 22, 3883
DOI: 10.1039/c9cp06525c

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2)
to estimate a default(1E13) A factor.
A = 1E13(1/s)/2.587E-9(mol/cm^2) = 3.87E21 cm^2/(mol*s)
Ea = 0.34eV = 32806.6J/mol

This is R25 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 26,
    label = "NH_X + NH2_X <=> N_X + NH3_X",
    kinetics = SurfaceArrhenius(
        A = (3.87E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (94560.2, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"Mechanistic study of hydrazine decomposition on Ir(111)"
Xiuyuan Lu et al. Phys.Chem.Chem.Phys., 2020, 22, 3883
DOI: 10.1039/c9cp06525c

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2)
to estimate a default(1E13) A factor.
A = 1E13(1/s)/2.587E-9(mol/cm^2) = 3.87E21 cm^2/(mol*s)
Ea = 0.98eV = 94560.2J/mol

This is R26 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 27,
    label = "N_X + N_X <=> [Pt]=NN=[Pt]",
    kinetics = SurfaceArrhenius(
        A = (3.55E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (187423.24, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Bidentate_Dissociation""",
    longDesc = u"""
"Kinetic and mechanistic analysis of NH3 decomposition 
on Ru(0001), Ru(111) and Ir(111) surfaces"
Xiuyuan Lu et al. Nanoscale Adv., 2021, 3, 1624
DOI: 10.1039/d1na00015b

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2) to estimate A factor.
A = 9.18E12(1/s)/2.587E-9(mol/cm^2) = 3.55E21 cm^2/(mol*s)
Ea was calculated from A factor and k rate constant in Table 3

This is R7 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 28,
    label = "H_X + H_X <=> H2_X + X",
    kinetics = SurfaceArrhenius(
        A = (2.42E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (60127.72, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""
"Kinetic and mechanistic analysis of NH3 decomposition 
on Ru(0001), Ru(111) and Ir(111) surfaces"
Xiuyuan Lu et al. Nanoscale Adv., 2021, 3, 1624
DOI: 10.1039/d1na00015b

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2) to estimate A factor.
A = 6.25E12(1/s)/2.587E-9(mol/cm^2) = 2.42E21 cm^2/(mol*s)
Ea was calculated from A factor and k rate constant in Table 3

This is R9 in Table 3
""",
    metal = "Ir",
    facet = "111",
)
