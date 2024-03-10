#!/usr/bin/env python
# encoding: utf-8

name = "Cation_R_Recombination/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "NH2 + Li <=> NH2Li",
    degeneracy = 1.0,
    kinetics = Marcus(A=(1.73e+06,'m^3/(mol*s)'), n=2, lmbd_i_coefs=[21824.5,-0.0341626,-0.0013254,4.92966e-07], beta=(1.2e+10,'m^-1'), wr=(0,'J/mol'), wp=(0,'J/mol'), lmbd_o=(0,'J/mol')),
    rank = 3,
    longDesc = 
"""
Calculated using a geometric mean with the four point method at ccsd(t)-f12/cc-pvdz-f12//wb97x-d3/def2-tzvp
""",
)

entry(
    index = 1,
    label = "C2H5 + Li <=> C2H5Li",
    degeneracy = 1.0,
    kinetics = Marcus(A=(1.73e+06,'m^3/(mol*s)'), n=2, lmbd_i_coefs=[51072.9,0.770449,0.00461441,-2.38037e-06], beta=(1.2e+10,'m^-1'), wr=(0,'J/mol'), wp=(0,'J/mol'), lmbd_o=(0,'J/mol')),
    rank = 3,
    longDesc = 
"""
Calculated using a geometric mean with the four point method at ccsd(t)-f12/cc-pvdz-f12//wb97x-d3/def2-tzvp
""",
)

entry(
    index = 2,
    label = "CH3 + Li <=> CH3Li",
    degeneracy = 1.0,
    kinetics = Marcus(A=(1.73e+06,'m^3/(mol*s)'), n=2, lmbd_i_coefs=[51902.4,-1.10249,-0.00813508,3.26585e-06], beta=(1.2e+10,'m^-1'), wr=(0,'J/mol'), wp=(0,'J/mol'), lmbd_o=(0,'J/mol')),
    rank = 3,
    longDesc = 
"""
Calculated using a geometric mean with the four point method at ccsd(t)-f12/cc-pvdz-f12//wb97x-d3/def2-tzvp
""",
)

entry(
    index = 3,
    label = "CH3NH + Li <=> CH3NHLi",
    degeneracy = 1.0,
    kinetics = Marcus(A=(1.73e+06,'m^3/(mol*s)'), n=2, lmbd_i_coefs=[22140,-3.52755,-0.00528491,2.76922e-06], beta=(1.2e+10,'m^-1'), wr=(0,'J/mol'), wp=(0,'J/mol'), lmbd_o=(0,'J/mol')),
    rank = 3,
    longDesc = 
"""
Calculated using a geometric mean with the four point method at ccsd(t)-f12/cc-pvdz-f12//wb97x-d3/def2-tzvp
""",
)

entry(
    index = 4,
    label = "SH + Li <=> SHLi",
    degeneracy = 1.0,
    kinetics = Marcus(A=(1.73e+06,'m^3/(mol*s)'), n=2, lmbd_i_coefs=[20364.7,0.177444,-0.000702861,-3.39533e-08], beta=(1.2e+10,'m^-1'), wr=(0,'J/mol'), wp=(0,'J/mol'), lmbd_o=(0,'J/mol')),
    rank = 3,
    longDesc = 
"""
Calculated using a geometric mean with the four point method at ccsd(t)-f12/cc-pvdz-f12//wb97x-d3/def2-tzvp
""",
)

