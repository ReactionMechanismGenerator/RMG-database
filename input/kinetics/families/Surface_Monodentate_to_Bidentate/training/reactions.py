#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Monodentate_to_Bidentate/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 1,
    label = "XCCH2 + Pt_4 <=> XCXCH2",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(1E21, 'cm^2/(mol*s)'),
        n = 0.0,
        Ea=(0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Automatic mechanism generation involving 
kinetics of surface reactions with bidentate adsorbates
Authors:  B. Kreitz, K. Blöndal, K. Badger, R. H. West and C. F. Goldsmith
doi:10.1039/d3dd00184a
""",
    metal = "Pt",
)

entry(
    index = 2,
    label = "XCHCH2 + Pt_4 <=> XCHXCH2",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(7.15E20, 'cm^2/(mol*s)'),
        n = 0.0,
        Ea=(3, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Automatic mechanism generation involving 
kinetics of surface reactions with bidentate adsorbates
Authors:  B. Kreitz, K. Blöndal, K. Badger, R. H. West and C. F. Goldsmith
doi:10.1039/d3dd00184a
""",
    metal = "Pt",
)

entry(
    index = 3,
    label = "HXCO + Pt_4 <=> HXCXO",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(1E21, 'cm^2/(mol*s)'),
        n = 0.0,
        Ea=(0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Automatic mechanism generation involving 
kinetics of surface reactions with bidentate adsorbates
Authors:  B. Kreitz, K. Blöndal, K. Badger, R. H. West and C. F. Goldsmith
doi:10.1039/d3dd00184a
""",
    metal = "Pt",
)