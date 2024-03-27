#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_to_Bidentate/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 1,
    label = "H2CCH3_X + Pt_5 + Pt_6 <=> H2CCH2_2X + H_X",
    degeneracy = 3,
    kinetics = SurfaceArrhenius(
        A=(0.557E30, 'cm^4/(mol^2*s)'),
        n = 0.0,
        Ea=(46, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 8,
    shortDesc = u"""Deutschmann Ni""",
    longDesc = u"""
Calculated with DFT by Katrín Blöndal and Bjarne Kreitz at Brown University, using the vdW-DF-cx functional in Quantum ESPRESSO. 
Details on the computational method to derive the rate constants are provided in "Automatic mechanism generation involving 
kinetics of surface reactions with bidentate adsorbates" by B. Kreitz, K. Blöndal, K. Badger, R. H. West and C. F. Goldsmith, Digital Discovery, 2024, 3, 173
doi:10.1039/d3dd00184a
A divided by 3 due to the degeneracy.
""",
	metal = "Pt",
)

entry(
    index = 2,
    label = "HCCH3_X + Pt_5 + Pt_6 <=> HCCH2_2X + H_X",
    degeneracy = 3,
    kinetics = SurfaceArrhenius(
        A=(0.65E30, 'cm^4/(mol^2*s)'),
        n = 0.0,
        Ea=(49, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 8,
    shortDesc = u"""Default""",
    longDesc = u"""
Calculated with DFT by Katrín Blöndal and Bjarne Kreitz at Brown University, using the vdW-DF-cx functional in Quantum ESPRESSO. 
Details on the computational method to derive the rate constants are provided in "Automatic mechanism generation involving 
kinetics of surface reactions with bidentate adsorbates" by B. Kreitz, K. Blöndal, K. Badger, R. H. West and C. F. Goldsmith, Digital Discovery, 2024, 3, 173
doi:10.1039/d3dd00184a
A divided by 3 due to the degeneracy.
""",
	metal = "Pt",
)

entry(
    index = 3,
    label = "H2CO_2X + H_X <=> H2COH_X + Pt_5 + Pt_6",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(8.22E20, 'cm^2/(mol*s)'),
        n = 0.0,
        Ea=(29, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 8,
    shortDesc = u"""Default""",
    longDesc = u"""
Calculated with DFT by Katrín Blöndal and Bjarne Kreitz at Brown University, using the vdW-DF-cx functional in Quantum ESPRESSO. 
Details on the computational method to derive the rate constants are provided in "Automatic mechanism generation involving 
kinetics of surface reactions with bidentate adsorbates" by B. Kreitz, K. Blöndal, K. Badger, R. H. West and C. F. Goldsmith, Digital Discovery, 2024, 3, 173
doi:10.1039/d3dd00184a
""",
	metal = "Pt",
)

entry(
    index = 4,
    label = "XCXCH2 + H_X <=> XCCH3 + Pt_5 + Pt_6",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(1.07E22, 'cm^2/(mol*s)'),
        n = 0.0,
        Ea=(72, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 8,
    shortDesc = u"""Default""",
    longDesc = u"""
Calculated with DFT by Katrín Blöndal and Bjarne Kreitz at Brown University, using the vdW-DF-cx functional in Quantum ESPRESSO. 
Details on the computational method to derive the rate constants are provided in "Automatic mechanism generation involving 
kinetics of surface reactions with bidentate adsorbates" by B. Kreitz, K. Blöndal, K. Badger, R. H. West and C. F. Goldsmith, Digital Discovery, 2024, 3, 173
doi:10.1039/d3dd00184a
""",
	metal = "Pt",
)