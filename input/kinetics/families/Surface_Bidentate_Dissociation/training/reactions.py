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
    label = "CC_2X <=> CX_3 + CX_4  ",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(4.22E12, '1/s'),
        n = 0.0,
        Ea=(104, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=8,
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
    index = 2,
    label = "CCH_2X <=> CX_3 + CHX_4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(1.3E12, '1/s'),
        n = 0.126, 
        Ea=(77, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=8,
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
    index = 3,
    label = "HCCH_2X <=> CHX_3 + CHX_4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(7.93E12, '1/s'),
        n = 0.0,
        Ea=(90, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=8,
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
    label = "HCCH2_2X <=> CHX_3 + CH2X_4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(2.74E13, '1/s'),
        n = 0.0,
        Ea=(140, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=8,
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
    index = 5,
    label = "CH2X_3 + CH2X_4 <=> H2CCH2_2X",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(9.89E23, 'cm^2/(mol*s)'),
        n = 0.0,
        Ea=(154, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=8,
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
    index = 6,
    label = "CHX_3 + OX_4 <=> HCO_2X",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(6.54E21, 'cm^2/(mol*s)'),
        n = 0.0,
        Ea=(142, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=8,
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
    index = 7,
    label = "CH2X_3 + OX_4 <=> H2CO_2X",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(2.2E22, 'cm^2/(mol*s)'),
        n = 0.0,
        Ea=(115, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=8,
    shortDesc = u"""Default""",
    longDesc = u"""
Calculated with DFT by Katrín Blöndal and Bjarne Kreitz at Brown University, using the vdW-DF-cx functional in Quantum ESPRESSO. 
Details on the computational method to derive the rate constants are provided in "Automatic mechanism generation involving 
kinetics of surface reactions with bidentate adsorbates" by B. Kreitz, K. Blöndal, K. Badger, R. H. West and C. F. Goldsmith, Digital Discovery, 2024, 3, 173
doi:10.1039/d3dd00184a
""",
    metal = "Pt",
)