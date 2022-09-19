#!/usr/bin/env python
# encoding: utf-8

name = "Metal Binding Energies"
shortDesc = ""
longDesc = """
Metal binding energies and surface site densities. 
The DFT calculations were performed by Katrin Blondal and Bjarne Kreitz (both Brown University) using Quantum Espresso with PAW PBE pseudopotentials. PBE was used as the xc-functional and a vdW-corr (DFT-D3) was applied. A 3x3 cell was used for the fcc(111) and hcp(0001) facets with 4 layers and a 1x3 cell with 12 layers for the (211) facets. Further the following settings were used: vaccum=10A (above and below), dftd3_version=4, dftd3_threebody=True, occupations='smearing', smearing='marzari-vanderbilt', degauss=0.005, mixing_mode='local-TF', tprnfor=True, nosym=True. 
Structures were optimized in a multistep procedure according to Blondal et al. (https://doi.org/10.1021/acs.iecr.9b01464) with (1) a (2,2,1) k-point grid ((2,1,1) for (211) facets) and 40 Ry cutoff and (2) (4,4,1) grid ((4,2,1) for (211) facets) and 50 Ry until forces were below 0.01 eV/A. The single point energy was computed on a (6,6,1) grid ((6,4,1) for (211) facets) and 60 Ry. Prior to the relaxation, the lattice constant of the bulk metal was determined through optimization with the calculator settings using a k-point grid of (21,21,21).
"""
entry(
    index = 0,
    label = "Pt111",
    bindingEnergies = {
        'H': (-2.75368,'eV/molecule'),
        'C': (-7.02516,'eV/molecule'),
        'N': (-4.63225,'eV/molecule'),
        'O': (-3.81153,'eV/molecule'),
    },
    surfaceSiteDensity = (2.483e-09, 'mol/cm^2'),
    facet = "111",
    metal = "Pt",
    shortDesc = """fcc""",
    longDesc = 
"""
Calculated by Katrin Blondal and Bjarne Kreitz at Brown University. The lattice constant is a=3.93 Angstrom.
""",
)

entry(
    index = 1,
    label = "Ru0001",
    bindingEnergies = {
        'H': (-2.85192,'eV/molecule'),
        'C': (-7.5979,'eV/molecule'),
        'N': (-5.969,'eV/molecule'),
        'O': (-5.4492,'eV/molecule'),
    },
    surfaceSiteDensity = (2.6300000000000002e-09, 'mol/cm^2'),
    facet = "0001",
    metal = "Ru",
    shortDesc = """hcp""",
    longDesc = 
"""
Calculated by Katrin Blondal and Bjarne Kreitz at Brown University. The lattice constant is a=2.70 Angstrom and c=4.27 Angstrom.
""",
)

entry(
    index = 2,
    label = "Rh111",
    bindingEnergies = {
        'H': (-2.83001,'eV/molecule'),
        'C': (-7.33484,'eV/molecule'),
        'N': (-5.30055,'eV/molecule'),
        'O': (-4.71419,'eV/molecule'),
    },
    surfaceSiteDensity = (2.656e-09, 'mol/cm^2'),
    facet = "111",
    metal = "Rh",
    shortDesc = """fcc""",
    longDesc = 
"""
Calculated by Katrin Blondal and Bjarne Kreitz at Brown University. The lattice constant is a=3.8 Angstrom.
""",
)

entry(
    index = 3,
    label = "Ir111",
    bindingEnergies = {
        'H': (-2.67674,'eV/molecule'),
        'C': (-7.25234,'eV/molecule'),
        'N': (-5.06204,'eV/molecule'),
        'O': (-4.35236,'eV/molecule'),
    },
    surfaceSiteDensity = (2.587e-09, 'mol/cm^2'),
    facet = "111",
    metal = "Ir",
    shortDesc = """fcc""",
    longDesc = 
"""
Calculated by Katrin Blondal and Bjarne Kreitz at Brown University. The lattice constant is a=3.85 Angstrom.
""",
)

entry(
    index = 4,
    label = "Au111",
    bindingEnergies = {
        'H': (-2.20848,'eV/molecule'),
        'C': (-4.5465,'eV/molecule'),
        'N': (-2.41078,'eV/molecule'),
        'O': (-2.71822,'eV/molecule'),
    },
    surfaceSiteDensity = (2.2700000000000002e-09, 'mol/cm^2'),
    facet = "111",
    metal = "Au",
    shortDesc = """fcc""",
    longDesc = 
"""
Calculated by Katrin Blondal and Bjarne Kreitz at Brown University. The lattice constant is a=4.11 Angstrom.
""",
)

entry(
    index = 5,
    label = "Pd111",
    bindingEnergies = {
        'H': (-2.92249,'eV/molecule'),
        'C': (-7.16786,'eV/molecule'),
        'N': (-4.78496,'eV/molecule'),
        'O': (-4.13577,'eV/molecule'),
    },
    surfaceSiteDensity = (2.534e-09, 'mol/cm^2'),
    facet = "111",
    metal = "Pd",
    shortDesc = """fcc""",
    longDesc = 
"""
Calculated by Katrin Blondal and Bjarne Kreitz at Brown University. The lattice constant is a=3.96 Angstrom.
""",
)

entry(
    index = 6,
    label = "Cu111",
    bindingEnergies = {
        'H': (-2.58383,'eV/molecule'),
        'C': (-4.96034,'eV/molecule'),
        'N': (-3.58447,'eV/molecule'),
        'O': (-4.20764,'eV/molecule'),
    },
    surfaceSiteDensity = (2.943e-09, 'mol/cm^2'),
    facet = "111",
    metal = "Cu",
    shortDesc = """fcc""",
    longDesc = 
"""
Calculated by Katrin Blondal and Bjarne Kreitz at Brown University. The lattice constant is a=3.56 Angstrom.
""",
)

entry(
    index = 7,
    label = "Ag111",
    bindingEnergies = {
        'H': (-2.10527,'eV/molecule'),
        'C': (-3.50609,'eV/molecule'),
        'N': (-1.97974,'eV/molecule'),
        'O': (-3.11159,'eV/molecule'),
    },
    surfaceSiteDensity = (2.2920000000000004e-09, 'mol/cm^2'),
    facet = "111",
    metal = "Ag",
    shortDesc = """fcc""",
    longDesc = 
"""
Calculated by Katrin Blondal and Bjarne Kreitz at Brown University. The lattice constant is a=4.09 Angstrom.
""",
)

entry(
    index = 8,
    label = "Ni111",
    bindingEnergies = {
        'H': (-2.89203,'eV/molecule'),
        'C': (-6.79794,'eV/molecule'),
        'N': (-5.16381,'eV/molecule'),
        'O': (-4.98902,'eV/molecule'),
    },
    surfaceSiteDensity = (3.148e-09, 'mol/cm^2'),
    facet = "111",
    metal = "Ni",
    shortDesc = """fcc""",
    longDesc = 
"""
Calculated by Katrin Blondal and Bjarne Kreitz at Brown University. The lattice constant is a=3.49 Angstrom.
""",
)

entry(
    index = 9,
    label = "Co0001",
    bindingEnergies = {
        'H': (-3.02059,'eV/molecule'),
        'C': (-7.09133,'eV/molecule'),
        'N': (-5.58561,'eV/molecule'),
        'O': (-5.38368,'eV/molecule'),
    },
    surfaceSiteDensity = (3.1180000000000006e-09, 'mol/cm^2'),
    facet = "0001",
    metal = "Co",
    shortDesc = """hcp""",
    longDesc = 
"""
Calculated by Katrin Blondal and Bjarne Kreitz at Brown University. The lattice constant is a=2.48 Angstrom and c=4.01 Angstrom.
""",
)

entry(
    index = 10,
    label = "Pt211",
    bindingEnergies = {
        'H': (-2.89,'eV/molecule'),
        'C': (-7.205,'eV/molecule'),
        'N': (-4.635,'eV/molecule'),
        'O': (-4.15,'eV/molecule'),
    },
    surfaceSiteDensity = (2.634e-09, 'mol/cm^2'),
    facet = "211",
    metal = "Pt",
    shortDesc = """fcc""",
    longDesc = 
"""
Calculated by Katrin Blondal and Bjarne Kreitz at Brown University. The lattice constant is a=3.93 Angstrom.
""",
)

entry(
    index = 11,
    label = "Rh211",
    bindingEnergies = {
        'H': (-2.82805,'eV/molecule'),
        'C': (-7.80574,'eV/molecule'),
        'N': (-5.4916,'eV/molecule'),
        'O': (-4.7766,'eV/molecule'),
    },
    surfaceSiteDensity = (2.817e-09, 'mol/cm^2'),
    facet = "211",
    metal = "Rh",
    shortDesc = """fcc""",
    longDesc = 
"""
Calculated by Katrin Blondal and Bjarne Kreitz at Brown University. The lattice constant is a=3.8 Angstrom.
""",
)

entry(
    index = 12,
    label = "Ag211",
    bindingEnergies = {
        'H': (-2.036,'eV/molecule'),
        'C': (-4.045,'eV/molecule'),
        'N': (-2.051,'eV/molecule'),
        'O': (-3.126,'eV/molecule'),
    },
    surfaceSiteDensity = (2.432e-09, 'mol/cm^2'),
    facet = "211",
    metal = "Ag",
    shortDesc = """fcc""",
    longDesc = 
"""
Calculated by Katrin Blondal and Bjarne Kreitz at Brown University. The lattice constant is a=4.09 Angstrom.
""",
)

entry(
    index = 13,
    label = "Pd211",
    bindingEnergies = {
        'H': (-2.785,'eV/molecule'),
        'C': (-7.826,'eV/molecule'),
        'N': (-4.774,'eV/molecule'),
        'O': (-3.98,'eV/molecule'),
    },
    surfaceSiteDensity = (2.688e-09, 'mol/cm^2'),
    facet = "211",
    metal = "Pd",
    shortDesc = """fcc""",
    longDesc = 
"""
Calculated by Katrin Blondal and Bjarne Kreitz at Brown University. The lattice constant is a=3.96 Angstrom.
""",
)

entry(
    index = 14,
    label = "Au211",
    bindingEnergies = {
        'H': (-2.19121,'eV/molecule'),
        'C': (-4.75864,'eV/molecule'),
        'N': (-2.45501,'eV/molecule'),
        'O': (-2.75366,'eV/molecule'),
    },
    surfaceSiteDensity = (2.408e-09, 'mol/cm^2'),
    facet = "211",
    metal = "Au",
    shortDesc = """fcc""",
    longDesc = 
"""
Calculated by Katrin Blondal and Bjarne Kreitz at Brown University. The lattice constant is a=4.11 Angstrom.
""",
)

entry(
    index = 15,
    label = "Ir211",
    bindingEnergies = {
        'H': (-3.04938,'eV/molecule'),
        'C': (-7.51874,'eV/molecule'),
        'N': (-5.38689,'eV/molecule'),
        'O': (-5.15358,'eV/molecule'),
    },
    surfaceSiteDensity = (2.7440000000000005e-09, 'mol/cm^2'),
    facet = "211",
    metal = "Ir",
    shortDesc = """fcc""",
    longDesc = 
"""
Calculated by Katrin Blondal and Bjarne Kreitz at Brown University. The lattice constant is a=3.85 Angstrom.
""",
)

entry(
    index = 16,
    label = "Ru211",
    bindingEnergies = {
        'H': (-2.99021,'eV/molecule'),
        'C': (-7.76706,'eV/molecule'),
        'N': (-6.16793,'eV/molecule'),
        'O': (-5.85841,'eV/molecule'),
    },
    surfaceSiteDensity = (3.199e-09, 'mol/cm^2'),
    facet = "211",
    metal = "Ru",
    shortDesc = """hcp""",
    longDesc = 
"""
Calculated by Katrin Blondal and Bjarne Kreitz at Brown University. The lattice constant is a=2.70 Angstrom and c=4.27 Angstrom.
""",
)

entry(
    index = 17,
    label = "Co211",
    bindingEnergies = {
        'H': (-2.95858,'eV/molecule'),
        'C': (-7.51741,'eV/molecule'),
        'N': (-5.69353,'eV/molecule'),
        'O': (-5.73947,'eV/molecule'),
    },
    surfaceSiteDensity = (3.7110000000000005e-09, 'mol/cm^2'),
    facet = "211",
    metal = "Co",
    shortDesc = """hcp""",
    longDesc = 
"""
Calculated by Katrin Blondal and Bjarne Kreitz at Brown University. The lattice constant is a=2.48 Angstrom and c=4.01 Angstrom.
""",
)

entry(
    index = 18,
    label = "Ni211",
    bindingEnergies = {
        'H': (-2.901,'eV/molecule'),
        'C': (-7.775,'eV/molecule'),
        'N': (-5.31,'eV/molecule'),
        'O': (-5.086,'eV/molecule'),
    },
    surfaceSiteDensity = (3.3390000000000006e-09, 'mol/cm^2'),
    facet = "211",
    metal = "Ni",
    shortDesc = """fcc""",
    longDesc = 
"""
Calculated by Katrin Blondal and Bjarne Kreitz at Brown University. The lattice constant is a=3.49 Angstrom.
""",
)

entry(
    index = 19,
    label = "Cu211",
    bindingEnergies = {
        'H': (-2.582,'eV/molecule'),
        'C': (-5.831,'eV/molecule'),
        'N': (-3.723,'eV/molecule'),
        'O': (-4.307,'eV/molecule'),
    },
    surfaceSiteDensity = (3.1210000000000003e-09, 'mol/cm^2'),
    facet = "211",
    metal = "Cu",
    shortDesc = """fcc""",
    longDesc = 
"""
Calculated by Katrin Blondal and Bjarne Kreitz at Brown University. The lattice constant is a=3.56 Angstrom.
""",
)

