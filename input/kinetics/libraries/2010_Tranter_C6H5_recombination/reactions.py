#!/usr/bin/env python
# encoding: utf-8

name = "2010_Tranter_C6H5_recombination"
shortDesc = u""
longDesc = u"""
Robert S. Tranter, Stephen J. Klippenstein, Lawrence B. Harding, Binod R. Giri, Xueliang Yang, and John H. Kiefer, Experimental and Theoretical Investigation of the Self-Reaction of Phenyl Radicals, J. Phys. Chem. A 2010, 114, 8240–8261

The rovibrational properties of the stationary points on this PES were studied with B3LYP DFT employing the 6-311++G(d,p). Higher level estimates for the energies of the stationary points are obtained by including +MP2/6-311++G(3df,2pd), -MP2/6-311++G(d,p), +QCISD(t)/6-311++G(3df,2pd),+B3LYP/6-311++G(d,p). In case of barrierless reaction such as index1, VRC-TST has been applied. The interaction between the two reacting radicals for arbitrary orientation and separation are evaluated directly with multireference second order perturbation theory (CASPT2) employing a two-electron two-orbital (2e,2o) complete active space consisting of the radical orbitals on each of the phenyl radicals. The basis set used in this CASPT2 is cc-pvdz (Dunning's correlation consistent polarized valence double zeta)
"""
entry(
    index = 1,
    label = "C6H5 + C6H5 <=> C12H10",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.66e+64, 'cm^3/(mol*s)'),
                n = -14.68,
                Ea = (16740, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (6.14e+37, 'cm^3/(mol*s)'),
                n = -7.140,
                Ea = (7903, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.34e+20, 'cm^3/(mol*s)'),
                n = -2.335,
                Ea = (2076, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.11e+14, 'cm^3/(mol*s)'),
                n = -0.405,
                Ea = (-307, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.09e+12, 'cm^3/(mol*s)'),
                n = 0.036,
                Ea = (-857, 'cal/mol'),
                T0 = (1, 'K'),
            ),

        ],
    ),
)

entry(
    index = 2,
    label = "C6H5 + C6H5 <=> o-C12H9 + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.51e+76, 'cm^3/(mol*s)'),
                n = -16.8,
                Ea = (39390, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.20e+48, 'cm^3/(mol*s)'),
                n = -8.82,
                Ea = (32270, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.44e+13, 'cm^3/(mol*s)'),
                n = 0.885,
                Ea = (21730, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.76e-12, 'cm^3/(mol*s)'),
                n = 7.72,
                Ea = (13750, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.65e-20, 'cm^3/(mol*s)'),
                n = 9.58,
                Ea = (11520, 'cal/mol'),
                T0 = (1, 'K'),
            ),

        ],
    ),
)

entry(
    index = 3,
    label = "C6H5 + C6H5 <=> m-C12H9 + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (2.44e+76, 'cm^3/(mol*s)'),
                n = -16.86,
                Ea = (39440, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.81e+48, 'cm^3/(mol*s)'),
                n = -8.90,
                Ea = (32390, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.44e+13, 'cm^3/(mol*s)'),
                n = 0.868,
                Ea = (21750, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (6.92e-12, 'cm^3/(mol*s)'),
                n = 7.63,
                Ea = (13870, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.60e-19, 'cm^3/(mol*s)'),
                n = 9.52,
                Ea = (11620, 'cal/mol'),
                T0 = (1, 'K'),
            ),

        ],
    ),
)

entry(
    index = 4,
    label = "C6H5 + C6H5 <=> p-C12H9 + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.25e+76, 'cm^3/(mol*s)'),
                n = -16.88,
                Ea = (39520, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.10e+48, 'cm^3/(mol*s)'),
                n = -8.89,
                Ea = (32410, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.13e+35, 'cm^3/(mol*s)'),
                n = 0.826,
                Ea = (21870, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.34e-12, 'cm^3/(mol*s)'),
                n = 7.62,
                Ea = (13940, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (8.61e-20, 'cm^3/(mol*s)'),
                n = 9.49,
                Ea = (11710, 'cal/mol'),
                T0 = (1, 'K'),
            ),

        ],
    ),
)
