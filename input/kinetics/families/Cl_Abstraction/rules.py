#!/usr/bin/env python
# encoding: utf-8

name = "Cl_Abstraction/rules"
shortDesc = u""
longDesc = u"""
General comments go at the top of the file,

or in a section(s) titled 'General'

.. the ID must match those in the rateLibrary AS A STRING (ie. '2' is different from '02')


.. [MRHCBSQB3RRHO] M.R. Harper (mrharper_at_mit_dot_edu or michael.harper.jr_at_gmail_dot_com)
The geometries of all reactants, products, and the transition state were optimized using the CBS-QB3 calculations.  The zero-point
energy is that computed by the CBS-QB3 calculations.  The frequencies were computed with B3LYP/CBSB7.
In computing k(T), an asymmetric tunneling correction was employed, the calculated frequencies were scaled by 0.99, and the
temperatures used were: 300, 331, 370, 419, 482, 568, 692, 885, 1227, 2000 (evenly spaced on inverse temperature scale).

.. [Tsang1990] W. Tsang; "Chemical kinetic database for combustion chemistry. Part IV. Isobutane" J. Phys. Chem. Ref. Data 19 (1990) 1-68

.. [Tsang1991] W. Tsang; "Chemical kinetic database for combustion chemistry. Part V. Propene" J. Phys. Chem. Ref. Data 20 (1991) 221-273
"""
entry(
    index = 0,
    label = "X_Cl_or_Xrad_Cl_Xbirad_Cl_Xtrirad_Cl;Y_rad_birad_trirad_quadrad",
    kinetics = ArrheniusEP(
        A = (7.046e+12, 'cm^3/(mol*s)'),
        n = 1.73,
        alpha = 0,
        E0 = (35.88, 'kJ/mol'),
        Tmin = (300, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc =
u"""
CH3Cl + H -> CH3 + HCl
A = 1.17E-11c m3/molecule/s * 6.02214E23 molecule/mol
https://kinetics.nist.gov/kinetics/Detail?id=2004LOU/GON10586-10593:2
""",
)

# entry(
#     index = 1,
#     label = "X_H;Y_rad_birad_trirad_quadrad",
#     kinetics = ArrheniusEP(
#         A = (100000, 'cm^3/(mol*s)'),
#         n = 0,
#         alpha = 0,
#         E0 = (10, 'kcal/mol'),
#         Tmin = (300, 'K'),
#         Tmax = (1500, 'K'),
#     ),
#     rank = 0,
#     shortDesc = u"""Default""",
# )
