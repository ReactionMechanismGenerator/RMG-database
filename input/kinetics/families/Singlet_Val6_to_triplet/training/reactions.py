#!/usr/bin/env python
# encoding: utf-8

name = "Singlet_Val6_to_triplet/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "O2(S) => O2(T)",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(4.5e+10, 's^-1'), n=0, Ea=(397, 'cal/mol'), T0=(1, 'K')),
    rank = 1,
    longDesc = 
u"""
taken from:
R. Atkinson, D.L. Baulch, R.A. Cox, R.F. Hampson, J.A. Kerr, J. Troe,
Evaluated Kinetic and Photochemical Data for Atmospheric Chemistry: Supplement IV.
IUPAC Subcommittee on Gas Kinetic Data Evaluation for Atmospheric Chemistry
Journal of Physical and Chemical Reference Data 21, 1125 (1992)
doi: 10.1063/1.555918

Adjusted to a first order reaction at 1 atm by alongd:
n/V = P/RT = 1 bar / (83 cm^3 bar K^-1 mol^-1 * 300 K) = 4E-05 mol cm^-3
1.81E+06 mol cm^-3 s^-1 / 4E-05 mol cm^-3 = 4.5E+10 s^-1
Original reaction is O2(1D) + M => O2 + M
""",
)

entry(
    index = 1,
    label = "SO(S) => SO(T)",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+17, 's^-1'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    rank = 1,
    longDesc = 
u"""
taken from:
H2S oxidation at high pressures
An Exploratory Flow Reactor Study of H2S Oxidation at 30-100 Bar
Y. Song, H. Hashemi, J.M. Christensen, C. Zou, B.S. Haynes, P. Marshall, P. Glarborg
International Journal of Chemical Kinetics 49(1), 2017, 37-52
doi: 10.1002/kin.21055

As reported by:
Rasmussen CL GlArborg P MArshall P Proc Combust Inst 2007, 31, 339-347

Adjusted to a first order reaction at 1 atm by alongd:
n/V = P/RT = 1 bar / (83 cm^3 bar K^-1 mol^-1 * 300 K) = 4E-05 mol cm^-3
1E+13 mol cm^-3 s^-1 / 4E-05 mol cm^-3 = 2.5E+17 s^-1
Original reaction is:
   label = "SO(S) <=> SO",
   degeneracy = 1,
   kinetics = ThirdBody(
       arrheniusLow = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
       efficiencies = {},
   ),
""",
)

