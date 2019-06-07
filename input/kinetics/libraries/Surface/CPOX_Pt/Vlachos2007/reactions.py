#!/usr/bin/env python
# encoding: utf-8

name = "Vlachos_Pt"
shortDesc = u""
longDesc = u"""
test surface mechanism: based upon D.G. Vlachos' work:
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
Mhadeshwar and Vlachos
Ind. Eng. Chem. Res., 2007, 56, 5310-5324

Note: The pre-exponential values are for surface coverage 2.72E-5 mol/m2 (same as in the Deutschmann 2006 mechanism). The pre-exponenitals listed here are calculated as follows: A = A_from_paper/(surface coverage)^(n-1)*(300K)^b), where n is order of reaction and b is the given temperature exponent. The activation energy is for 300K and does not include coverage or temperature dependence terms. Also note that the activation energy was converted from kcal/mol to J/mol.
"""

#Oxygen Adsorption-Desorption Steps
#CFG: O2 is a special case: we need to treat it separately
entry(
    index = 1,
    label = "O2 + Pt + Pt <=> OX + OX",
    kinetics = StickingCoefficient(
        A = 5.42E-2,
        n = 0.766,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R1"""
)

#endothermic - reverse of R1
#entry(
#    index = 2,
#    label = "OX + OX <=> O2 + Pt + Pt",
#    kinetics = SurfaceArrhenius(
#        A=(2.90E19, 'm^2/(mol*s)'),
#        n = -0.796,
#        Ea=(212966.0, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R2"""
#)


entry(
    index = 3,
    label = "O + Pt <=> OX",
    kinetics = StickingCoefficient(
        A = 4.91E-2,
        n = 0.25,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R3"""
)

#endothermic - reverse of R3
#entry(
#    index = 4,
#    label = "OX <=> O + Pt",
#    kinetics = SurfaceArrhenius(
#        A=(5.99E13, '1/s'),
#        n = -0.25,
#        Ea=(355640.0, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R4"""
#)


#CO Oxidation on Platinum
#CFG: CO is a special case: we need to treat it separately
entry(
    index = 5,
    label = "CO + Pt <=> OCX",
    kinetics = StickingCoefficient(
        A = 1.0E0,
        n = 0,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R5"""
)

#endothermic - reverse of R5
#entry(
#    index = 6,
#    label = "OCX <=> CO + Pt",
#    kinetics = SurfaceArrhenius(
#        A=(9.80E16, '1/s)'),
#        n = -0.5,
#        Ea=(167360.0, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R6"""
#)

entry(
    index = 7,
    label = "CO2 + Pt <=> CO2X",
    kinetics = StickingCoefficient(
        A = 1.95E-1,
        n = 0.25,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R7. CO2X is vdW CO2."""
)


#endothermic - reverse of R7
#entry(
#    index = 8,
#    label = "CO2X <=> CO2 + Pt",
#    kinetics = SurfaceArrhenius(
#        A=(1.51E13, '1/s'),
#        n = -0.25,
#        Ea=(15062.0, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R8. CO2X is vdW CO2."""
#)

#endothermic - reverse of R10
#entry(
#    index = 9,
#    label = "CO2X + Pt <=> OCX + OX",
#    kinetics = SurfaceArrhenius(
#        A=(5.61E14, 'm^2/(mol*s)'),
#        n = 0.177,
#        Ea=(110039.0, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R9. CO2X is vdW CO2."""
#)

entry(
    index = 10,
    label = "OCX + OX <=> CO2X + Pt",
    kinetics = SurfaceArrhenius(
        A=(2.41E16, 'm^2/(mol*s)'),
        n = -0.177,
        Ea=(86190.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R10. CO2X is vdW CO2."""
)


#H2 Oxidation on Platinum
entry(
    index = 11,
    label = "H2 + Pt + Pt <=> HX + HX",
    kinetics = StickingCoefficient(
        A = 1.29E-1,
        n = 0.858,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R11"""
)

#endothermic - reverse of R11
#entry(
#    index = 12,
#    label = "HX + HX <=> H2 + Pt + Pt",
#    kinetics = SurfaceArrhenius(
#        A=(2.94E17, 'm^2/(mol*s)'),
#        n = -0.001,
#        Ea=(82843, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R12"""
#)

#endothermic - reverse of R14
#entry(
#    index = 13,
#    label = "HOX + Pt <=> HX + OX",
#    kinetics = SurfaceArrhenius(
#        A=(1.65E12, 'm^2/(mol*s)'),
#        n = 1.872,
#        Ea=(113386, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R13"""
#)


entry(
    index = 14,
    label = "HX + OX <=> HOX + Pt",
    kinetics = SurfaceArrhenius(
        A=(6.63E15, 'm^2/(mol*s)'),
        n = 0.624,
        Ea=(36819.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R14"""
)

#endothermic - reverse of R16
#entry(
#    index = 15,
#    label = "H2OX + Pt <=> HX + HOX",
#    kinetics = SurfaceArrhenius(
#        A=(6.74E17, 'm^2/(mol*s)'),
#        n = -0.118,
#        Ea=(74475, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R15. H2OX is vdW H2O."""
#)

entry(
    index = 16,
    label = "HX + HOX <=> H2OX + Pt",
    kinetics = SurfaceArrhenius(
        A=(1.46E20, 'm^2/(mol*s)'),
        n = -1.049,
        Ea=(56484.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R16. H2OX is vdW H2O."""
)

entry(
    index = 17,
    label = "H2OX + OX <=> HOX + HOX",
    kinetics = SurfaceArrhenius(
        A=(9.96E14, 'm^2/(mol*s)'),
        n = 0.082,
        Ea=(36819.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R17. H2OX is vdW H2O."""
)


#endothermic - reverse of R17
#entry(
#    index = 18,
#    label = "HOX + HOX <=> H2OX + OX",
#    kinetics = SurfaceArrhenius(
#        A=(9.79E13, 'm^2/(mol*s)'),
#        n = 0.325,
#        Ea=(94977, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R18. H2OX is vdW H2O."""
#)

entry(
    index = 19,
    label = "OH + Pt <=> HOX",
    kinetics = StickingCoefficient(
        A = 9.99E-1,
        n = 2.0,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R19"""
)

#endothermic - reverse of R19
#entry(
#    index = 20,
#    label = "HOX <=> OH + Pt",
#    kinetics = SurfaceArrhenius(
#        A=(1.60E9, '1/s'),
#        n = 2.0,
#        Ea=(263592, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R20"""
#)

entry(
    index = 21,
    label = "H2O + Pt <=> H2OX",
    kinetics = StickingCoefficient(
        A = 1.08E-1,
        n = 1.162,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R21. H2OX is vdW H2O."""
)

#endothermic - reverse of R21
#entry(
#    index = 22,
#    label = "H2OX <=> H2O + Pt",
#    kinetics = SurfaceArrhenius(
#        A=(8.11E8, '1/s'),
#        n = 1.372,
#        Ea=(41840, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R22. H2OX is vdW H2O."""
#)

entry(
    index = 23,
    label = "H + Pt <=> HX",
    kinetics = StickingCoefficient(
        A = 3.84E-1,
        n = 1.832,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R23"""
)

#endothermic - reverse of R23
#entry(
#    index = 24,
#    label = "HX <=> H + Pt",
#    kinetics = SurfaceArrhenius(
#        A=(9.10E8, '1/s'),
#        n = 1.890,
#        Ea=(259408, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R24"""
#)


#Coupling between CO and H2 Chemistries on Platinum
entry(
    index = 25,
    label = "CO2X + HX <=> OCX + HOX",
    kinetics = SurfaceArrhenius(
        A=(6.10E14, 'm^2/(mol*s)'),
        n = -0.531,
        Ea=(25104.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R25. CO2X is vdW CO2."""
)

#endothermic - reverse of R25
#entry(
#    index = 26,
#    label = "OCX + HOX <=> CO2X + HX",
#    kinetics = SurfaceArrhenius(
#        A=(2.23E12, 'm^2/(mol*s)'),
#        n = 0.531,
#        Ea=(77404, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R26. CO2X is vdW CO2."""
#)

entry(
    index = 27,
    label = "COOH + Pt <=> HOCXO",
    kinetics = StickingCoefficient(
        A = 6.34E-2,
        n = -0.089,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R27"""
)

#endothermic - reverse of R27
#entry(
#    index = 28,
#    label = "HOCXO <=> COOH + Pt",
#    kinetics = SurfaceArrhenius(
#        A=(6.74E12, '1/s'),
#        n = 0.089,
#        Ea=(231375, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R28"""
#)


entry(
    index = 29,
    label = "HOCXO + Pt <=> OCX + HOX",
    kinetics = SurfaceArrhenius(
        A=(2.70E13, 'm^2/(mol*s)'),
        n = 0.024,
        Ea=(22175.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R29"""
)

#endothermic - reverse of R29
#entry(
#    index = 30,
#    label = "OCX + HOX <=> HOCXO + Pt",
#    kinetics = SurfaceArrhenius(
#        A=(5.02E13, 'm^2/(mol*s)'),
#        n = -0.024,
#        Ea=(79914, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R30"""
#)

entry(
    index = 31,
    label = "HOCXO + Pt <=> CO2X + HX",
    kinetics = SurfaceArrhenius(
        A=(1.70E14, 'm^2/(mol*s)'),
        n = 0.549,
        Ea=(4184.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R31. CO2X is vdW CO2."""
)

#endothermic - reverse of R31
#entry(
#    index = 32,
#    label = "CO2X + HX <=> HOCXO + Pt",
#    kinetics = SurfaceArrhenius(
#        A=(7.95E16, 'm^2/(mol*s)'),
#        n = -0.549,
#        Ea=(10042, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R32. CO2X is vdW CO2."""
#)

#endothermic - reverse of R34
#entry(
#    index = 33,
#    label = "OCX + H2OX <=> HOCXO + HX",
#    kinetics = SurfaceArrhenius(
#        A=(2.44E14, 'm^2/(mol*s)'),
#        n = 0.492,
#        Ea=(99161, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R33. H2OX is vdW H2O."""
#)


entry(
    index = 34,
    label = "HOCXO + HX <=> OCX + H2OX",
    kinetics = SurfaceArrhenius(
        A=(5.51E16, 'm^2/(mol*s)'),
        n = -0.492,
        Ea=(23430, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R34. H2OX is vdW H2O."""
)

#endothermic - reverse of R36
#entry(
#    index = 35,
#    label = "CO2X + HOX <=> HOCXO + OX",
#    kinetics = SurfaceArrhenius(
#        A=(1.13E15, 'm^2/(mol*s)'),
#        n = 0.097,
#        Ea=(110876, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R35. CO2X is vdW CO2."""
#)

entry(
    index = 36,
    label = "HOCXO + OX <=> CO2X + HOX",
    kinetics = SurfaceArrhenius(
        A=(1.20E16, 'm^2/(mol*s)'),
        n = -0.097,
        Ea=(29288, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R36. CO2X is vdW CO2."""
)

#endothermic - reverse of R38
#entry(
#    index = 37,
#    label = "CO2X + H2OX <=> HOCXO + HOX",
#    kinetics = SurfaceArrhenius(
#        A=(3.80E15, 'm^2/(mol*s)'),
#        n = -0.031,
#        Ea=(73220, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R37. CO2X is vdW CO2 and H2OX is vdW H2O."""
#)

entry(
    index = 38,
    label = "HOCXO + HOX <=> CO2X + H2OX",
    kinetics = SurfaceArrhenius(
        A=(3.57E15, 'm^2/(mol*s)'),
        n = 0.031,
        Ea=(49790, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R38. CO2X is vdW CO2 and H2OX is vdW H2O."""
)

entry(
    index = 39,
    label = "HCOO + Pt + Pt <=> OCHXOX",
    kinetics = StickingCoefficient(
        A = 1.46E-1,
        n = 0.201,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R39"""
)

#endothermic - reverse of R39
#entry(
#    index = 40,
#    label = "OCHXOX <=> HCOO + Pt + Pt",
#    kinetics = SurfaceArrhenius(
#        A=(1.52E13, '1/s'),
#        n = -0.201,
#        Ea=(221752, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R40"""
#)

#endothermic - reverse of R42
#entry(
#    index = 41,
#    label = "CO2X + HX <=> OCHXOX",
#    kinetics = SurfaceArrhenius(
#        A=(4.57E16, 'm^2/(mol*s)'),
#        n = -0.422,
#        Ea=(77404, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R41"""
#)

entry(
    index = 42,
    label = "OCHXOX <=> CO2X + HX",
    kinetics = SurfaceArrhenius(
        A=(8.07E9, '1/s'),
        n = 0.422,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R42"""
)

#endothermic - reverse of R44
#entry(
#    index = 43,
#    label = "CO2X + HOX + Pt <=> OCHXOX + OX",
#    kinetics = SurfaceArrhenius(
#        A=(2.17E19, 'm^4/(mol^2*s)'),
#        n = 0.236,
#        Ea=(153971, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R43. CO2X is vdW CO2."""
#)

entry(
    index = 44,
    label = "OCHXOX + OX <=> CO2X + HOX + Pt",
    kinetics = SurfaceArrhenius(
        A=(2.29E16, 'm^2/(mol*s)'),
        n = -0.236,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R44. CO2X is vdW CO2."""
)

#endothermic - reverse of R46
#entry(
#    index = 45,
#    label = "CO2X + H2OX + Pt <=> OCHXOX + HOX",
#    kinetics = SurfaceArrhenius(
#        A=(8.02E19, 'm^4/(mol^2*s)'),
#        n = 0.095,
#        Ea=(107947, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R45. CO2X is vdW CO2 and H2OX is vdW H2O."""
#)

entry(
    index = 46,
    label = "OCHXOX + HOX <=> CO2X + H2OX + Pt",
    kinetics = SurfaceArrhenius(
        A=(6.24E15, 'm^2/(mol*s)'),
        n = -0.095,
        Ea=(12552, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R46. CO2X is vdW CO2."""
)

#CH4 Oxidation and Reforming on Platinum
entry(
    index = 47,
    label = "C + Pt <=> CX",
    kinetics = StickingCoefficient(
        A = 1.64E-2,
        n = 0.156,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R47"""
)

#endothermic - reverse of R47
#entry(
#    index = 48,
#    label = "CX <=> C + Pt",
#    kinetics = SurfaceArrhenius(
#        A=(1.05E14, '1/s'),
#        n = -0.156,
#        Ea=(659817, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R48"""
#)


entry(
    index = 49,
    label = "CH + Pt <=> CHX",
    kinetics = StickingCoefficient(
        A = 1.35E-2,
        n = 0.051,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R49"""
)

#endothermic - reverse of R49
#entry(
#    index = 50,
#    label = "CHX <=> CH + Pt",
#    kinetics = SurfaceArrhenius(
#        A=(6.98E13, '1/s'),
#        n = -0.051,
#        Ea=(657306, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R50"""
#)

entry(
    index = 51,
    label = "CH2 + Pt <=> CH2X",
    kinetics = StickingCoefficient(
        A = 4.50E-2,
        n = 0.118,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R51"""
)

#endothermic - reverse of R51
#entry(
#    index = 52,
#    label = "CH2X <=> CH2 + Pt",
#    kinetics = SurfaceArrhenius(
#        A=(3.08E13, '1/s'),
#        n = -0.118,
#        Ea=(383254, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R52"""
#)

entry(
    index = 53,
    label = "CH3 + Pt <=> CH3X",
    kinetics = StickingCoefficient(
        A = 1.60E-1,
        n = -0.099,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R53"""
)

#endothermic - reverse of R53
#entry(
#    index = 54,
#    label = "CH3X <=> CH3 + Pt",
#    kinetics = SurfaceArrhenius(
#        A=(2.51E12, '1/s'),
#        n = 0.099,
#        Ea=(189535, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R54"""
#)

entry(
    index = 55,
    label = "CH4 + Pt + Pt <=> CH3X + HX",
    kinetics = StickingCoefficient(
        A = 1.16E-1,
        n = 0.154,
        Ea=(37656, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R55"""
)

#endothermic - reverse of R55
#entry(
#    index = 56,
#    label = "CH3X + HX <=> CH4 + Pt + Pt",
#    kinetics = SurfaceArrhenius(
#        A=(5.42E15, 'm^2/(mol*s)'),
#        n = -0.154,
#        Ea=(47279, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R56"""
#)

#endothermic - reverse of R58
#entry(
#    index = 57,
#    label = "CH3X + Pt <=> CH2X + HX",
#    kinetics = SurfaceArrhenius(
#        A=(3.74E14, 'm^2/(mol*s)'),
#        n = 0.419,
#        Ea=(66107, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R57"""
#)

entry(
    index = 58,
    label = "CH2X + HX <=> CH3X + Pt",
    kinetics = SurfaceArrhenius(
        A=(3.61E16, 'm^2/(mol*s)'),
        n = -0.419,
        Ea=(55647, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R58"""
)

entry(
    index = 59,
    label = "CH2X + Pt <=> CHX + HX",
    kinetics = SurfaceArrhenius(
        A=(5.41E14, 'm^2/(mol*s)'),
        n = 0.222,
        Ea=(37656, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R59"""
)

#endothermic - reverse of R59
#entry(
#    index = 60,
#    label = "CHX + HX <=> CH2X + Pt",
#    kinetics = SurfaceArrhenius(
#        A=(2.50E16, 'm^2/(mol*s)'),
#        n = -0.222,
#        Ea=(148114, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R60"""
#)

#endothermic - reverse of R62
#entry(
#    index = 61,
#    label = "CHX + Pt <=> CX + HX",
#    kinetics = SurfaceArrhenius(
#        A=(3.46E14, 'm^2/(mol*s)'),
#        n = 0.398,
#        Ea=(130959, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R61"""
#)

entry(
    index = 62,
    label = "CX + HX <=> CHX + Pt",
    kinetics = SurfaceArrhenius(
        A=(7.01E16, 'm^2/(mol*s)'),
        n = -0.398,
        Ea=(55229, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R62"""
)

entry(
    index = 63,
    label = "CH3X + OX <=> CH2X + HOX",
    kinetics = SurfaceArrhenius(
        A=(2.69E16, 'm^2/(mol*s)'),
        n = -0.230,
        Ea=(45187, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R63"""
)

#endothermic - reverse of R63
#entry(
#    index = 64,
#    label = "CH2X + HOX <=> CH3X + OX",
#    kinetics = SurfaceArrhenius(
#        A=(5.04E14, 'm^2/(mol*s)'),
#        n = 0.230,
#        Ea=(111294, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R64"""
#)

#endothermic - reverse of R66
#entry(
#    index = 65,
#    label = "CHX + HOX <=> CH2X + OX",
#    kinetics = SurfaceArrhenius(
#        A=(3.81E14, 'm^2/(mol*s)'),
#        n = 0.414,
#        Ea=(187025, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R65"""
#)

entry(
    index = 66,
    label = "CH2X + OX <=> CHX + HOX",
    kinetics = SurfaceArrhenius(
        A=(3.55E16, 'm^2/(mol*s)'),
        n = -0.414,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R66"""
)

entry(
    index = 67,
    label = "CX + HOX <=> CHX + OX",
    kinetics = SurfaceArrhenius(
        A=(6.48E14, 'm^2/(mol*s)'),
        n = 0.225,
        Ea=(115897, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R67"""
)

#reverse of R67
#entry(
#    index = 68,
#    label = "CHX + OX <=> CX + HOX",
#    kinetics = SurfaceArrhenius(
#        A=(2.08E16, 'm^2/(mol*s)'),
#        n = -0.225,
#        Ea=(115060, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R68"""
#)

#endothermic - reverse of R70
#entry(
#    index = 69,
#    label = "CH2X + H2OX <=> CH3X + HOX",
#    kinetics = SurfaceArrhenius(
#        A=(1.71E15, 'm^2/(mol*s)'),
#        n = 0.099,
#        Ea=(58994, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R69. H2OX is vdW H2O."""
#)

entry(
    index = 70,
    label = "CH3X + HOX <=> CH2X + H2OX",
    kinetics = SurfaceArrhenius(
        A=(7.90E15, 'm^2/(mol*s)'),
        n = -0.099,
        Ea=(51463, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R70. H2OX is vdW H2O."""
)

#endothermic - reverse of R72
#entry(
#    index = 71,
#    label = "CHX + H2OX <=> CH2X + HOX",
#    kinetics = SurfaceArrhenius(
#        A=(1.43E15, 'm^2/(mol*s)'),
#        n = 0.269,
#        Ea=(142256, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R71. H2OX is vdW H2O."""
#)

entry(
    index = 72,
    label = "CH2X + HOX <=> CHX + H2OX",
    kinetics = SurfaceArrhenius(
        A=(9.42E15, 'm^2/(mol*s)'),
        n = -0.269,
        Ea=(13807, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R72. H2OX is vdW H2O."""
)

entry(
    index = 73,
    label = "CX + H2OX <=> CHX + HOX",
    kinetics = SurfaceArrhenius(
        A=(2.29E15, 'm^2/(mol*s)'),
        n = 0.090,
        Ea=(65270, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R73. H2OX is vdW H2O."""
)

#endothermic - reverse of R73
#entry(
#    index = 74,
#    label = "CHX + HOX <=> CX + H2OX",
#    kinetics = SurfaceArrhenius(
#        A=(5.90E15, 'm^2/(mol*s)'),
#        n = -0.090,
#        Ea=(122591, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R74. H2OX is vdW H2O."""
#)

#endothermic - reverse of R76
#entry(
#    index = 75,
#    label = "OCX + Pt <=> CX + OX",
#    kinetics = SurfaceArrhenius(
#        A=(7.28E14, 'm^2/(mol*s)'),
#        n = 0.468,
#        Ea=(321331, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R75"""
#)

entry(
    index = 76,
    label = "CX + OX <=> OCX + Pt",
    kinetics = SurfaceArrhenius(
        A=(1.86E16, 'm^2/(mol*s)'),
        n = -0.468,
        Ea=(93303, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R76"""
)

#endothermic - reverse of R78
#entry(
#    index = 77,
#    label = "OCX + HX <=> CHX + OX",
#    kinetics = SurfaceArrhenius(
#        A=(7.58E15, 'm^2/(mol*s)'),
#        n = 0.073,
#        Ea=(191627, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R77"""
#)

entry(
    index = 78,
    label = "CHX + OX <=> OCX + HX",
    kinetics = SurfaceArrhenius(
        A=(1.79E15, 'm^2/(mol*s)'),
        n = -0.073,
        Ea=(38911, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R78"""
)

#endothermic - reverse of R80
#entry(
#    index = 79,
#    label = "OCX + HX <=> CX + HOX",
#    kinetics = SurfaceArrhenius(
#        A=(4.77E16, 'm^2/(mol*s)'),
#        n = -0.168,
#        Ea=(170289, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R79"""
#)


#not an elementary reaction according to our families
entry(
    index = 80,
    label = "CX + HOX <=> OCX + HX",
    kinetics = SurfaceArrhenius(
        A=(2.83E14, 'm^2/(mol*s)'),
        n = 0.168,
        Ea=(18410.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R80"""
)

#endothermic - reverse of R82
#entry(
#    index = 81,
#    label = "OCX + OCX <=> CX + CO2X",
#    kinetics = SurfaceArrhenius(
#        A=(2.32E15, 'm^2/(mol*s)'),
#        n = 0.393,
#        Ea=(204179, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R81. CO2X is vdW CO2."""
#)

entry(
    index = 82,
    label = "CX + CO2X <=> OCX + OCX",
    kinetics = SurfaceArrhenius(
        A=(5.81E15, 'm^2/(mol*s)'),
        n = -0.393,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R82. CO2X is vdW CO2."""
)

#Oxygenates Decomposition on Platinum
entry(
    index = 83,
    label = "CH3OH + Pt <=> CH3OHX",
    kinetics = StickingCoefficient(
        A = 3.34E-1,
        n = 0.258,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R83. CH3OHX is vdW CH3OH."""
)

#endothermic - reverse of R83
#entry(
#    index = 84,
#    label = "CH3OHX <=> CH3OH + Pt",
#    kinetics = SurfaceArrhenius(
#        A=(9.19E12, '1/s'),
#        n = -0.258,
#        Ea=(39748, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R84. CH3OHX is vdW CH3OH."""
#)

entry(
    index = 85,
    label = "CH3O + Pt <=> CH3OX",
    kinetics = StickingCoefficient(
        A = 1.49E-1,
        n = 0.054,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R85"""
)

#endothermic - reverse of R85
#entry(
#    index = 86,
#    label = "CH3OX <=> CH3O + Pt",
#    kinetics = SurfaceArrhenius(
#        A=(6.44E12, '1/s'),
#        n = -0.054,
#        Ea=(154808, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R86"""
#)

entry(
    index = 87,
    label = "CH2O + Pt <=> CH2OX",
    kinetics = StickingCoefficient(
        A = 8.77E-2,
        n = 0.098,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R87. CH2OX is vdW CH2O."""
)

#endothermic - reverse of R87
#entry(
#    index = 88,
#    label = "CH2OX <=> CH2O + Pt",
#    kinetics = SurfaceArrhenius(
#        A=(1.41E13, '1/s'),
#        n = -0.098,
#        Ea=(50208, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R88. CH2OX is vdW CH2O."""
#)

entry(
    index = 89,
    label = "HCO + Pt <=> CXHO",
    kinetics = StickingCoefficient(
        A = 1.14E-2,
        n = 0.096,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R89"""
)

#endothermic - reverse of R89
#entry(
#    index = 90,
#    label = "CXHO <=> HCO + Pt",
#    kinetics = SurfaceArrhenius(
#        A=(1.07E14, '1/s'),
#        n = -0.096,
#        Ea=(232212, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R90"""
#)

entry(
    index = 91,
    label = "CH2OH + Pt <=> H2CXOH",
    kinetics = StickingCoefficient(
        A = 5.26E-2,
        n = 0.233,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R91"""
)

#endothermic - reverse of R91
#entry(
#    index = 92,
#    label = "H2CXOH <=> CH2OH + Pt",
#    kinetics = SurfaceArrhenius(
#        A=(5.10E13, '1/s'),
#        n = -0.233,
#        Ea=(209200, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R92"""
#)

#endothermic - reverse of R94
#entry(
#    index = 93,
#    label = "CH3OHX + Pt <=> CH3OX + HX",
#    kinetics = SurfaceArrhenius(
#        A=(1.61E15, 'm^2/(mol*s)'),
#        n = 0.102,
#        Ea=(78659, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R93. CH3OHX is vdW CH3OH."""
#)

entry(
    index = 94,
    label = "CH3OX + HX <=> CH3OHX + Pt",
    kinetics = SurfaceArrhenius(
        A=(8.43E15, 'm^2/(mol*s)'),
        n = -0.102,
        Ea=(17991, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R94. CH3OHX is vdW CH3OH."""
)

entry(
    index = 95,
    label = "CH3OX + Pt <=> CH2OX + HX",
    kinetics = SurfaceArrhenius(
        A=(1.54E15, 'm^2/(mol*s)'),
        n = 0.192,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R95. CH2OX is vdW CH2O."""
)

#endothermic - reverse of R95
#entry(
#    index = 96,
#    label = "CH2OX + HX <=> CH3OX + Pt",
#    kinetics = SurfaceArrhenius(
#        A=(8.82E15, 'm^2/(mol*s)'),
#        n = -0.192,
#        Ea=(61505, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R96. CH2OX is vdW CH2O."""
#)

entry(
    index = 97,
    label = "CH2OX + Pt <=> CXHO + HX",
    kinetics = SurfaceArrhenius(
        A=(5.64E14, 'm^2/(mol*s)'),
        n = 0.270,
        Ea=(15062, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R97. CH2OX is vdW CH2O."""
)

#endothermic - reverse of R97
#entry(
#    index = 98,
#    label = "CXHO + HX <=> CH2OX + Pt",
#    kinetics = SurfaceArrhenius(
#        A=(2.40E16, 'm^2/(mol*s)'),
#        n = -0.270,
#        Ea=(87864, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R98. CH2OX is vdW CH2O."""
#)

entry(
    index = 99,
    label = "CXHO + Pt <=> OCX + HX",
    kinetics = SurfaceArrhenius(
        A=(3.97E14, 'm^2/(mol*s)'),
        n = 0.330,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R99"""
)

#endothermic - reverse of R99
#entry(
#    index = 100,
#    label = "OCX + HX <=> CXHO + Pt",
#    kinetics = SurfaceArrhenius(
#        A=(3.40E16, 'm^2/(mol*s)'),
#        n = -0.330,
#        Ea=(128867, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R100"""
#)

entry(
    index = 101,
    label = "CH3OHX + Pt <=> H2CXOH + HX",
    kinetics = SurfaceArrhenius(
        A=(3.13E14, 'm^2/(mol*s)'),
        n = 0.403,
        Ea=(36401, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R101. CH3OHX is vdW CH3OH."""
)

#endothermic - reverse of R101
#entry(
#    index = 102,
#    label = "H2CXOH + HX <=> CH3OHX + Pt",
#    kinetics = SurfaceArrhenius(
#        A=(4.32E16, 'm^2/(mol*s)'),
#        n = -0.403,
#        Ea=(61086, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R102. CH3OHX is vdW CH3OH."""
#)

#endothermic - reverse of R104
#entry(
#    index = 103,
#    label = "H2CXOH + Pt <=> CH2OX + HX",
#    kinetics = SurfaceArrhenius(
#        A=(7.58E15, 'm^2/(mol*s)'),
#        n = -0.104,
#        Ea=(33054, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R103. CH2OX is vdW CH2O."""
#)

entry(
    index = 104,
    label = "CH2OX + HX <=> H2CXOH + Pt",
    kinetics = SurfaceArrhenius(
        A=(1.78E15, 'm^2/(mol*s)'),
        n = 0.104,
        Ea=(9205, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R104. CH2OX is vdW CH2O."""
)
