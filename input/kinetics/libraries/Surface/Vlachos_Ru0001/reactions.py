#!/usr/bin/env python
# encoding: utf-8

name = "Vlachos_Ru0001"
shortDesc = u""
longDesc = u"""
Primarily based on:
"The role of adsorbate–adsorbate interactions in the rate controlling step 
and the most abundant reaction intermediate of NH3 decomposition on Ru"
D.G. Vlachos et al. (2004). Catalysis Letters 96, 13–22. 
https://doi.org/10.1023/B:CATL.0000029523.22277.e1
"""

entry(
    index = 1,
    label = "H2 + X + X <=> H_X + H_X",
    kinetics = StickingCoefficient(
        A = 0.87,
        n = 0,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""H2 Surface_Adsorption_Dissociative""",
    longDesc = u"""
"The role of adsorbate–adsorbate interactions in the rate controlling step 
and the most abundant reaction intermediate of NH3 decomposition on Ru"
D.G. Vlachos et al. (2004). Catalysis Letters 96, 13–22. 
https://doi.org/10.1023/B:CATL.0000029523.22277.e1

This is R1 in Table 2 (set A)
""",
    metal = "Ru",
    facet = "0001",
)

#skip R2 (reverse reaction of R1)

entry(
    index = 2,
    label = "N2 + X + X <=> N_X + N_X",
    kinetics = StickingCoefficient(
        A = 0.2,
        n = 0,
        Ea = (7.1, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    #    coverage_dependence = {'N_X': {'E': (26.3, 'kacl/mol'), 'm':0.0, 'a':0.0},},
    ),
    shortDesc = u"""N2 Surface_Adsorption_Dissociative""",
        longDesc = u"""
"The role of adsorbate–adsorbate interactions in the rate controlling step 
and the most abundant reaction intermediate of NH3 decomposition on Ru"
D.G. Vlachos et al. (2004). Catalysis Letters 96, 13–22. 
https://doi.org/10.1023/B:CATL.0000029523.22277.e1

This is R3 in Table 2 (set A)
""",
    metal = "Ru",
    facet = "0001",
)

#skip R4 (reverse reaction of R3)

entry(
    index = 3,
    label = "NH_X + X <=> N_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (7.22E20, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (5.3, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    #    coverage_dependence = {'N_X': {'E': (15.5, 'kacl/mol'), 'm':0.0, 'a':0.0},},
    #    coverage_dependence = {'H_X': {'E': (1, 'kacl/mol'), 'm':0.0, 'a':0.0},},
    ),
    shortDesc = u"""Surface_Dissociation""",
        longDesc = u"""
"The role of adsorbate–adsorbate interactions in the rate controlling step 
and the most abundant reaction intermediate of NH3 decomposition on Ru"
D.G. Vlachos et al. (2004). Catalysis Letters 96, 13–22. 
https://doi.org/10.1023/B:CATL.0000029523.22277.e1

This reaction used RMG's surface site density of Ru0001 = 2.630E-9(mol/cm^2) to calculate the A factor.
A = 1.9E12(1/s)/2.630E-9(mol/cm^2) = 7.22E20 cm^2/(mol*s)

This is R5 in Table 2 (set A)
""",
    metal = "Ru",
    facet = "0001",
)

#skip R6 (reverse reaction of R5)

entry(
    index = 4,
    label = "NH2_X + X <=> NH_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (7.60E20, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (20.1, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    #    coverage_dependence = {'H_X': {'E': (1.2, 'kacl/mol'), 'm':0.0, 'a':0.0},},
    ),
    shortDesc = u"""Surface_Dissociation""",
        longDesc = u"""
"The role of adsorbate–adsorbate interactions in the rate controlling step 
and the most abundant reaction intermediate of NH3 decomposition on Ru"
D.G. Vlachos et al. (2004). Catalysis Letters 96, 13–22. 
https://doi.org/10.1023/B:CATL.0000029523.22277.e1

This reaction used RMG's surface site density of Ru0001 = 2.630E-9(mol/cm^2) to calculate the A factor.
A = 2E12(1/s)/2.630E-9(mol/cm^2) = 7.60E20 cm^2/(mol*s)

This is R7 in Table 2 (set A)
""",
    metal = "Ru",
    facet = "0001",
)

#skip R9 (reverse reaction of R7)

entry(
    index = 5,
    label = "NH3_X + X <=> NH2_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (7.60E20, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (18.7, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    #    coverage_dependence = {'H_X': {'E': (1.3, 'kacl/mol'), 'm':0.0, 'a':0.0},},
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
        longDesc = u"""
"The role of adsorbate–adsorbate interactions in the rate controlling step 
and the most abundant reaction intermediate of NH3 decomposition on Ru"
D.G. Vlachos et al. (2004). Catalysis Letters 96, 13–22. 
https://doi.org/10.1023/B:CATL.0000029523.22277.e1

This reaction used RMG's surface site density of Ru0001 = 2.630E-9(mol/cm^2) to calculate the A factor.
A = 2E12(1/s)/2.630E-9(mol/cm^2) = 7.60E20 cm^2/(mol*s)

This is R9 in Table 2 (set A)
""",
    metal = "Ru",
    facet = "0001",
)

#skip R10 (reverse reaction of R9)

entry(
    index = 6,
    label = "NH3 + X <=> NH3_X",
    kinetics = StickingCoefficient(
        A = 0.00015,
        n = 0,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_vdW""",
        longDesc = u"""
"The role of adsorbate–adsorbate interactions in the rate controlling step 
and the most abundant reaction intermediate of NH3 decomposition on Ru"
D.G. Vlachos et al. (2004). Catalysis Letters 96, 13–22. 
https://doi.org/10.1023/B:CATL.0000029523.22277.e1

This is R11 in Table 2 (set A)
""",
    metal = "Ru",
    facet = "0001",
)

#skip R12 (reverse reaction of R11)