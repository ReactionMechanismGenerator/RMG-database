#!/usr/bin/env python
# encoding: utf-8

name = "XY-Addition_MultipleBond/training"
shortDesc = "Kinetics used to train group additivity values"
longDesc = """
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""

entry(
    index = 0,
    label = "C2H5F <=> C2H4 + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.63e+13,'s^-1'), n=0, Ea=(59900,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is CH3-CH2F <=> C2H4 + HF""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: CH3-CH2F <=> C2H4 + HF
""",
)

entry(
    index = 1,
    label = "C2H4F2 <=> CH2CHF + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.94e+13,'s^-1'), n=0, Ea=(61900,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is CH3-CHF2 <=> CH2:CHF + HF""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: CH3-CHF2 <=> CH2:CHF + HF
""",
)

entry(
    index = 2,
    label = "C2H3F3 <=> CH2CF2 + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+14,'s^-1'), n=0, Ea=(68700,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is CH3-CF3 <=> CH2:CF2 + HF""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: CH3-CF3 <=> CH2:CF2 + HF
""",
)

entry(
    index = 3,
    label = "C2H4F2-2 <=> C2H3F + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+13,'s^-1'), n=0, Ea=(62900,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is CH2F-CH2F <=> CH2:CHF + HF""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: CH2F-CH2F <=> CH2:CHF + HF
""",
)

entry(
    index = 4,
    label = "C2H3F3-2 <=> CHFCHF + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.26e+14,'s^-1'), n=0, Ea=(69100,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is CH2F-CHF2 <=> CHF:CHF[Z] + HF""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: CH2F-CHF2 <=> CHF:CHF[Z] + HF
""",
)

entry(
    index = 5,
    label = "C2H3F3-3 <=> C2H2F2 + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'s^-1'), n=0, Ea=(65400,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is CH2F-CHF2 <=> CH2:CF2 + HF""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: CH2F-CHF2 <=> CH2:CF2 + HF
""",
)

entry(
    index = 6,
    label = "C2H2F4 <=> CHFCF2 + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.63e+13,'s^-1'), n=0, Ea=(70700,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is CH2F-CF3 <=> CHF:CF2 + HF""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: CH2F-CF3 <=> CHF:CF2 + HF
""",
)

entry(
    index = 7,
    label = "C2H2F4-2 <=> C2HF3 + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'s^-1'), n=0, Ea=(69400,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is CHF2-CHF2 <=> CHF:CF2 + HF""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: CHF2-CHF2 <=> CHF:CF2 + HF
""",
)

entry(
    index = 8,
    label = "C2HF5 <=> CF2CF2 + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+13,'s^-1'), n=0, Ea=(71600,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is CHF2-CF3 <=> CF2:CF2 + HF""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: CHF2-CF3 <=> CF2:CF2 + HF
""",
)

entry(
    index = 9,
    label = "C2H5Br <=> C2H4 + BrH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.7e+13,'s^-1'), n=0, Ea=(53000,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is C2H5BR <=> C2H4 + HBR""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: C2H5BR <=> C2H4 + HBR
""",
)

entry(
    index = 10,
    label = "BrH + C3HF3 <=> C3H2BrF3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+12,'cm^3/(mol*s)'), n=0, Ea=(51390,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CF3CCH + HBR <=> BTP""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: CF3CCH + HBR <=> BTP
""",
)

entry(
    index = 11,
    label = "C3H2F4 <=> C3HF3-2 + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+51,'s^-1'), n=-10.897, Ea=(102870,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is CHFCHCF3 <=> HF + CF3CCH""",
    longDesc = 
"""
Training reaction from kinetics library: NIST_Fluorine/reduced
Original entry: CHFCHCF3 <=> HF + CF3CCH
""",
)

entry(
    index = 12,
    label = "C3H2F4-2 <=> C3HF3 + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.1e+44,'s^-1'), n=-8.492, Ea=(99304,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is CH2CFCF3 <=> CF3CCH + HF""",
    longDesc = 
"""
Training reaction from kinetics library: NIST_Fluorine/reduced
Original entry: CH2CFCF3 <=> CF3CCH + HF
""",
)

entry(
    index = 13,
    label = "CF3OH <=> CF2O + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.94e+11,'s^-1'), n=0.45, Ea=(45.2,'kcal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """CF3OH Decomposition""",
    longDesc = 
"""
https://pubs.acs.org/doi/pdf/10.1021/jp709796n
""",
)


entry(
    index = 14,
    label = "C2H5Cl <=> C2H4 + ClH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.81e+19,'s^-1'), n=-2, Ea=(60660,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C2H5CL <=> C2H4 + HCL""",
    longDesc = 
"""
Training reaction from kinetics library: CF2BrCl
Original entry: C2H5CL <=> C2H4 + HCL
""",
)

entry(
    index = 15,
    label = "C2H4Cl2 <=> C2H3Cl + ClH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.94e+21,'s^-1'), n=-2.37, Ea=(59460,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CH3CHCL2 <=> C2H3CL + HCL""",
    longDesc = 
"""
Training reaction from kinetics library: CF2BrCl
Original entry: CH3CHCL2 <=> C2H3CL + HCL
""",
)

entry(
    index = 16,
    label = "C2H3Cl3 <=> C2H2Cl2 + ClH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.94e+21,'s^-1'), n=-2.37, Ea=(59460,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CH3CCL3 <=> CH2CCL2 + HCL""",
    longDesc = 
"""
Training reaction from kinetics library: CF2BrCl
Original entry: CH3CCL3 <=> CH2CCL2 + HCL
""",
)

entry(
    index = 17,
    label = "C2H4Cl2-2 <=> C2H3Cl-2 + ClH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.76e+19,'s^-1'), n=-1.93, Ea=(58710,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CH2CLCH2CL <=> C2H3CL + HCL""",
    longDesc = 
"""
Training reaction from kinetics library: CF2BrCl
Original entry: CH2CLCH2CL <=> C2H3CL + HCL
""",
)

entry(
    index = 18,
    label = "C2H3Cl3-2 <=> C2H2Cl2-2 + ClH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.39e+20,'s^-1'), n=-2.03, Ea=(60450,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CH2CLCHCL2 <=> CHCLCHCL + HCL""",
    longDesc = 
"""
Training reaction from kinetics library: CF2BrCl
Original entry: CH2CLCHCL2 <=> CHCLCHCL + HCL
""",
)

entry(
    index = 19,
    label = "C2H3Cl3-3 <=> C2H2Cl2-3 + ClH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.13e+19,'s^-1'), n=-2.02, Ea=(60330,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CH2CLCHCL2 <=> CH2CCL2 + HCL""",
    longDesc = 
"""
Training reaction from kinetics library: CF2BrCl
Original entry: CH2CLCHCL2 <=> CH2CCL2 + HCL
""",
)

entry(
    index = 20,
    label = "C2H2Cl4 <=> C2HCl3 + ClH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.62e+21,'s^-1'), n=-2.57, Ea=(51870,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CHCL2CHCL2 <=> C2HCL3 + HCL""",
    longDesc = 
"""
Training reaction from kinetics library: CF2BrCl
Original entry: CHCL2CHCL2 <=> C2HCL3 + HCL
""",
)

entry(
    index = 21,
    label = "C2HCl5 <=> C2Cl4 + ClH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.6e+13,'s^-1'), n=0, Ea=(57100,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C2HCL5 <=> C2CL4 + HCL""",
    longDesc = 
"""
Training reaction from kinetics library: CF2BrCl
Original entry: C2HCL5 <=> C2CL4 + HCL
""",
)

entry(
    index = 22,
    label = "C2H3Cl-3 <=> C2H2 + ClH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.62e+28,'s^-1'), n=-4.29, Ea=(75780,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C2H3CL <=> C2H2 + HCL""",
    longDesc = 
"""
Training reaction from kinetics library: CF2BrCl
Original entry: C2H3CL <=> C2H2 + HCL
""",
)

entry(
    index = 23,
    label = "C2H2Cl2-4 <=> C2HCl + ClH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.45e+14,'s^-1'), n=0, Ea=(69220,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CH2CCL2 <=> C2HCL + HCL""",
    longDesc = 
"""
Training reaction from kinetics library: CF2BrCl
Original entry: CH2CCL2 <=> C2HCL + HCL
""",
)

entry(
    index = 24,
    label = "C2H2Cl2-5 <=> C2HCl-2 + ClH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.26e+13,'s^-1'), n=0, Ea=(69090,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CHCLCHCL <=> C2HCL + HCL""",
    longDesc = 
"""
Training reaction from kinetics library: CF2BrCl
Original entry: CHCLCHCL <=> C2HCL + HCL
""",
)

entry(
    index = 25,
    label = "C2HCl3-2 <=> C2Cl2 + ClH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.26e+13,'s^-1'), n=0, Ea=(74440,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C2HCL3 <=> C2CL2 + HCL""",
    longDesc = 
"""
Training reaction from kinetics library: CF2BrCl
Original entry: C2HCL3 <=> C2CL2 + HCL
""",
)

entry(
    index = 26,
    label = "C3H7Cl <=> C3H6 + ClH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.81e+19,'s^-1'), n=-2, Ea=(60660,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is IC3H7CL <=> C3H6 + HCL""",
    longDesc = 
"""
Training reaction from kinetics library: CF2BrCl
Original entry: IC3H7CL <=> C3H6 + HCL
""",
)

entry(
    index = 27,
    label = "C2Cl6 <=> C2Cl4 + Cl2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.01e+13,'s^-1'), n=0, Ea=(54100,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C2CL6 <=> C2CL4 + CL2""",
    longDesc = 
"""
Training reaction from kinetics library: CF2BrCl
Original entry: C2CL6 <=> C2CL4 + CL2
""",
)

entry(
    index = 28,
    label = "C2HClF4 <=> CF2CF2 + ClH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+13,'s^-1'), n=0, Ea=(71600,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C2HF4CL <=> C2F4 + HCL""",
    longDesc = 
"""
Training reaction from kinetics library: CF2BrCl
Original entry: C2HF4CL <=> C2F4 + HCL
""",
)

entry(
    index = 29,
    label = "C2HBrF4 <=> CF2CF2 + BrH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+13,'s^-1'), n=0, Ea=(71600,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C2HF4BR <=> C2F4 + HBR""",
    longDesc = 
"""
Training reaction from kinetics library: CF2BrCl
Original entry: C2HF4BR <=> C2F4 + HBR
""",
)

entry(
    index = 30,
    label = "C2H5Cl <=> C2H4 + ClH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.5e+10,'s^-1'), n=1.05, Ea=(57700,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C2H5CL <=> C2H4 + HCL""",
    longDesc = 
"""
Training reaction from kinetics library: CH3Cl
Original entry: C2H5CL <=> C2H4 + HCL
""",
)

entry(
    index = 31,
    label = "C2H4Cl2-2 <=> C2H3Cl-2 + ClH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.2e+13,'s^-1'), n=0, Ea=(56300,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CH2CLCH2CL <=> C2H3CL + HCL""",
    longDesc = 
"""
Training reaction from kinetics library: CH3Cl
Original entry: CH2CLCH2CL <=> C2H3CL + HCL
""",
)

entry(
    index = 32,
    label = "C2H3Cl-3 <=> C2H2 + ClH",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = Arrhenius(A=(4e+13,'s^-1'), n=0, Ea=(67000,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C2H3CL <=> C2H2 + HCL""",
    longDesc = 
"""
Training reaction from kinetics library: CH3Cl
Original entry: C2H3CL <=> C2H2 + HCL
""",
)

