#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Bidentate_Dissociation/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

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
        A=(2.202E12, '1/s'), 
        n = 0.09, 
        Ea=(103497.2, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=8,
    shortDesc = u"""Default""",
    longDesc = u"""
Calculated with DFT by Katrín Blöndal at Brown University, using the vdW-DF-cx functional in Quantum ESPRESSO. 
""",
    metal = "Pt",
)

entry(
    index = 2,
    label = "CCH_2X <=> CX_3 + CHX_4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(5.272E11, '1/s'), 
        n = 0.126, 
        Ea=(76699.8, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=8,
    shortDesc = u"""Default""",
    longDesc = u"""
Calculated with DFT by Katrín Blöndal at Brown University, using the vdW-DF-cx functional in Quantum ESPRESSO. 
""",
    metal = "Pt",
)

entry(
    index = 3,
    label = "HCCH_2X <=> CHX_3 + CHX_4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(7.062E11, '1/s'), 
        n = 0.320, 
        Ea=(88220.0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=10,
    shortDesc = u"""Default""",
    longDesc = u"""
Calculated with DFT by Katrín Blöndal at Brown University, using the vdW-DF-cx functional in Quantum ESPRESSO. 
""",
    metal = "Pt",
)

entry( 
    index = 4,
    label = "CHX_3 + CH2X_4 <=> HCCH2_2X",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(4.256E17, 'm^2/(mol*s)'),
        n = 0.106, 
        Ea=(138024.4, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=8,
    shortDesc = u"""Default""",
    longDesc = u"""
Calculated with DFT by Katrín Blöndal at Brown University, using the vdW-DF-cx functional in Quantum ESPRESSO.
""",
    metal = "Pt",
)

entry( 
    index = 5,
    label = "CH2X_3 + CH2X_4 <=> H2CCH2_2X",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(1.161E19, 'm^2/(mol*s)'),
        n = 0.281, 
        Ea=(152439.3, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=8,
    shortDesc = u"""Default""",
    longDesc = u"""
Calculated with DFT by Katrín Blöndal at Brown University, using the vdW-DF-cx functional in Quantum ESPRESSO.
""",
    metal = "Pt",
)

entry(
    index = 6,
    label = "CHX_3 + OX_4 <=> HCO_2X",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(6.922E17, 'm^2/(mol*s)'),
        n = 0.049, 
        Ea=(142325.0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=8,
    shortDesc = u"""Default""",
    longDesc = u"""
Calculated with DFT by Katrín Blöndal at Brown University, using the vdW-DF-cx functional in Quantum ESPRESSO.
""",
    metal = "Pt",
)

entry(
    index = 7,
    label = "CH2X_3 + OX_4 <=> H2CO_2X",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(1.174E18, 'm^2/(mol*s)'),
        n = 0.082, 
        Ea=(114251.7, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=8,
    shortDesc = u"""Default""",
    longDesc = u"""
Calculated with DFT by Katrín Blöndal at Brown University, using the vdW-DF-cx functional in Quantum ESPRESSO.
""",
    metal = "Pt",
)
