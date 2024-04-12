#!/usr/bin/env python
# encoding: utf-8

name = "Surface_vdW_to_Bidentate/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""


entry(
    index = 1,
    label = "HCCHX_vdW + X  <=> HCCH_2X",
    kinetics = SurfaceArrhenius(
        A = (1.0E21, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 8,
    shortDesc = u"""Default""",
    longDesc = u"""
    Barrierless according to DFT calculations by Katrín Blöndal at Brown University, using the vdW-DF-cx functional in Quantum ESPRESSO.
    Details on the computational method to derive the rate constants are provided in "Automatic mechanism generation involving 
    kinetics of surface reactions with bidentate adsorbates" by B. Kreitz, K. Blöndal, K. Badger, R. H. West and C. F. Goldsmith, Digital Discovery, 2024, 3, 173
    doi:10.1039/d3dd00184a
    """,
	metal = "Pt",
)


entry(
    index = 2,
    label = "H2CCH2X_vdW + X <=> H2CCH2_2X",
    kinetics = SurfaceArrhenius(
        A = (1.78E21, 'cm^2/(mol*s)'),
        n = 0.0,
        Ea = (12, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 8,
    shortDesc = u"""Default""",
    longDesc = u"""
    Calculated with DFT by Katrín Blöndal at Brown University, using the vdW-DF-cx functional in Quantum ESPRESSO.
    Details on the computational method to derive the rate constants are provided in "Automatic mechanism generation involving 
    kinetics of surface reactions with bidentate adsorbates" by B. Kreitz, K. Blöndal, K. Badger, R. H. West and C. F. Goldsmith, Digital Discovery, 2024, 3, 173
    doi:10.1039/d3dd00184a
    """,
	metal = "Pt",
)

entry(
    index = 3,
    label = "H2COX_vdW + X <=> H2CO_2X",
    kinetics = SurfaceArrhenius(
        A = (1.0E21, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 8,
    shortDesc = u"""Default""",
    longDesc = u"""
    Barrierless according to DFT calculations by Katrín Blöndal at Brown University, using the vdW-DF-cx functional in Quantum ESPRESSO.
    Details on the computational method to derive the rate constants are provided in "Automatic mechanism generation involving 
    kinetics of surface reactions with bidentate adsorbates" by B. Kreitz, K. Blöndal, K. Badger, R. H. West and C. F. Goldsmith, Digital Discovery, 2024, 3, 173
    doi:10.1039/d3dd00184a
    """,
	metal = "Pt",
)
