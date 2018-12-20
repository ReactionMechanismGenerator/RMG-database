#!/usr/bin/env python
# encoding: utf-8

name = "OneDMinN2"
shortDesc = u"OneDMinN2"
longDesc = u"""
A transport library of species calculated using the OneDMin software for N2 as a bath gas.

The citation for OneDMin is:
1. A. W. Jasper and J. A. Miller, "Lennard-Jones parameters for combustion and chemical kinetics modeling from
   full-dimensional intermolecular potentials," Combust. Flame, 161, 101 (2014).
2. A. W. Jasper and J. A. Miller, OneDMin, July 2014.

Listed below are pure-gas A+A Lennard-Jones parameters
LJ Parameters employed a DF-MP2/aug-cc-pVDZ potential energy surface.
Dipole Moment and Polarizability were computed at the B2PLYPD3/cc-pVTZ level

(1) Shape Index, indicating 0 (atom), 1 (linear molecule), or 2 (nonlinear molecule);
(2) Epsilon, the Lennard-Jones well depth, in K; and
(3) Sigma, the Lennard-Jones collision diameter, in Angstrom.
(4) Mu, total dipole moment, in Debye
(5) Alpha, mean static polarizability, in Angstrom^3
(6) Rotational Relacation Collision Number was *NOT* determined, and a default value of 1 is given here!
"""

entry(
    index=1,
    label="N2",
    molecule=
    """
    1 N u0 p1 c0 {2,T}
    2 N u0 p1 c0 {1,T}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(322.846, 'K'),
        sigma=(3.461, 'angstroms'),
        dipoleMoment=(1.781, 'De'),
        polarizability=(0.000, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
)

entry(
    index=2,
    label="NNH",
    molecule=
    """
    multiplicity 2
    1 N u1 p1 c0 {2,D}
    2 N u0 p1 c0 {1,D} {3,S}
    3 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(292.088, 'K'),
        sigma=(3.459, 'angstroms'),
        dipoleMoment=(1.858, 'De'),
        polarizability=(2.016, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
)

entry(
    index=3,
    label="H2NN(S)",
    molecule=
    """
    1 N u0 p0 c+1 {2,S} {3,S} {4,D}
    2 H u0 p0 c0 {1,S}
    3 H u0 p0 c0 {1,S}
    4 N u0 p2 c-1 {1,D}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(387.557, 'K'),
        sigma=(3.467, 'angstroms'),
        dipoleMoment=(3.507, 'De'),
        polarizability=(2.349, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
)

entry(
    index=4,
    label="H2NN(T)",
    molecule=
    """
    multiplicity 3
    1 N u0 p1 c0 {2,S} {3,S} {4,S}
    2 N u2 p1 c0 {1,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(338.122, 'K'),
        sigma=(3.528, 'angstroms'),
        dipoleMoment=(2.363, 'De'),
        polarizability=(2.371, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
)

entry(
    index=5,
    label="N2H2",
    molecule=
    """
    1 N u0 p1 c0 {2,D} {3,S}
    2 N u0 p1 c0 {1,D} {4,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(323.008, 'K'),
        sigma=(3.531, 'angstroms'),
        dipoleMoment=(0.000, 'De'),
        polarizability=(2.297, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
)

entry(
    index=6,
    label="N2H2(T)",
    molecule=
    """
    multiplicity 3
    1 N u1 p1 c0 {2,S} {3,S}
    2 H u0 p0 c0 {1,S}
    3 N u1 p1 c0 {1,S} {4,S}
    4 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(349.270, 'K'),
        sigma=(3.500, 'angstroms'),
        dipoleMoment=(0.001, 'De'),
        polarizability=(3.776, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
)

entry(
    index=7,
    label="N2H3",
    molecule=
    """
    multiplicity 2
    1 N u1 p1 c0 {2,S} {3,S}
    2 H u0 p0 c0 {1,S}
    3 N u0 p1 c0 {1,S} {4,S} {5,S}
    4 H u0 p0 c0 {3,S}
    5 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(327.797, 'K'),
        sigma=(3.595, 'angstroms'),
        dipoleMoment=(2.254, 'De'),
        polarizability=(2.772, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
)

entry(
    index=8,
    label="N2H4",
    molecule=
    """
    1 N u0 p1 c0 {2,S} {3,S} {4,S}
    2 N u0 p1 c0 {1,S} {5,S} {6,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {2,S}
    6 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(344.722, 'K'),
        sigma=(3.617, 'angstroms'),
        dipoleMoment=(0.000, 'De'),
        polarizability=(2.799, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
)

entry(
    index=9,
    label="NH3NH",
    molecule=
    """
    1 N u0 p0 c+1 {2,S} {3,S} {4,S} {5,S}
    2 H u0 p0 c0 {1,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 N u0 p2 c-1 {1,S} {6,S}
    6 H u0 p0 c0 {5,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(469.217, 'K'),
        sigma=(3.360, 'angstroms'),
        dipoleMoment=(5.526, 'De'),
        polarizability=(3.738, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
)

entry(
    index=10,
    label="nN3H4",
    molecule=
    """
    multiplicity 2
    1 N u1 p1 c0 {2,S} {3,S}
    2 H u0 p0 c0 {1,S}
    3 N u0 p1 c0 {1,S} {4,S} {5,S}
    4 N u0 p1 c0 {3,S} {6,S} {7,S}
    5 H u0 p0 c0 {3,S}
    6 H u0 p0 c0 {4,S}
    7 H u0 p0 c0 {4,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(406.129, 'K'),
        sigma=(3.790, 'angstroms'),
        dipoleMoment=(2.193, 'De'),
        polarizability=(4.090, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
)

entry(
    index=11,
    label="iN3H4",
    molecule=
    """
    multiplicity 2
    1 N u0 p1 c0 {2,S} {4,S} {5,S}
    2 N u1 p1 c0 {1,S} {3,S}
    3 N u0 p1 c0 {2,S} {6,S} {7,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {3,S}
    7 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(384.690, 'K'),
        sigma=(3.765, 'angstroms'),
        dipoleMoment=(1.143, 'De'),
        polarizability=(3.950, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
)

entry(
    index=12,
    label="nN3H5",
    molecule=
    """
    1 N u0 p1 c0 {2,S} {4,S} {5,S}
    2 N u0 p1 c0 {1,S} {3,S} {6,S}
    3 N u0 p1 c0 {2,S} {7,S} {8,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {2,S}
    7 H u0 p0 c0 {3,S}
    8 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(404.086, 'K'),
        sigma=(3.812, 'angstroms'),
        dipoleMoment=(2.182, 'De'),
        polarizability=(4.126, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
)

entry(
    index=13,
    label="1,2-z-N3H5",
    molecule=
    """
    1 N u0 p1 c0 {2,S} {7,S} {8,S}
    2 N u0 p0 c+1 {1,S} {3,S} {4,S} {5,S}
    3 H u0 p0 c0 {2,S}
    4 H u0 p0 c0 {2,S}
    5 N u0 p2 c-1 {2,S} {6,S}
    6 H u0 p0 c0 {5,S}
    7 H u0 p0 c0 {1,S}
    8 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(463.718, 'K'),
        sigma=(3.814, 'angstroms'),
        dipoleMoment=(3.384, 'De'),
        polarizability=(4.466, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
)

entry(
    index=14,
    label="NH2NHN",
    molecule=
    """
    1 N u0 p1 c0 {2,S} {5,S} {6,S}
    2 N u0 p0 c+1 {1,S} {3,S} {4,D}
    3 H u0 p0 c0 {2,S}
    4 N u0 p2 c-1 {2,D}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(422.694, 'K'),
        sigma=(3.704, 'angstroms'),
        dipoleMoment=(4.161, 'De'),
        polarizability=(4.008, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
)

entry(
    index=15,
    label="NH2NNH",
    molecule=
    """
    1 N u0 p1 c0 {2,S} {4,S} {5,S}
    2 N u0 p1 c0 {1,S} {3,D}
    3 N u0 p1 c0 {2,D} {6,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(392.041, 'K'),
        sigma=(3.687, 'angstroms'),
        dipoleMoment=(1.327, 'De'),
        polarizability=(3.749, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
)

entry(
    index=16,
    label="nN4H6",
    molecule=
    """
    1  N u0 p1 c0 {2,S} {5,S} {6,S}
    2  N u0 p1 c0 {1,S} {3,S} {7,S}
    3  N u0 p1 c0 {2,S} {4,S} {8,S}
    4  N u0 p1 c0 {3,S} {9,S} {10,S}
    5  H u0 p0 c0 {1,S}
    6  H u0 p0 c0 {1,S}
    7  H u0 p0 c0 {2,S}
    8  H u0 p0 c0 {3,S}
    9  H u0 p0 c0 {4,S}
    10 H u0 p0 c0 {4,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(457.953, 'K'),
        sigma=(3.976, 'angstroms'),
        dipoleMoment=(2.401, 'De'),
        polarizability=(5.481, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
)

entry(
    index=17,
    label="1,2-z-N4H6",
    molecule=
    """
    1  N u0 p1 c0 {2,S} {8,S} {9,S}
    2  N u0 p1 c0 {1,S} {3,S} {10,S}
    3  N u0 p0 c+1 {2,S} {4,S} {5,S} {6,S}
    4  H u0 p0 c0 {3,S}
    5  H u0 p0 c0 {3,S}
    6  N u0 p2 c-1 {3,S} {7,S}
    7  H u0 p0 c0 {6,S}
    8  H u0 p0 c0 {1,S}
    9  H u0 p0 c0 {1,S}
    10 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(516.985, 'K'),
        sigma=(3.959, 'angstroms'),
        dipoleMoment=(3.264, 'De'),
        polarizability=(5.472, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
)

entry(
    index=18,
    label="1,3-z-N4H6",
    molecule=
    """
    1  N u0 p1 c0 {2,S} {7,S} {8,S}
    2  N u0 p0 c+1 {1,S} {3,S} {4,S} {5,S}
    3  H u0 p0 c0 {2,S}
    4  H u0 p0 c0 {2,S}
    5  N u0 p2 c-1 {2,S} {6,S}
    6  N u0 p1 c0 {5,S} {9,S} {10,S}
    7  H u0 p0 c0 {1,S}
    8  H u0 p0 c0 {1,S}
    9  H u0 p0 c0 {6,S}
    10 H u0 p0 c0 {6,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(514.807, 'K'),
        sigma=(3.911, 'angstroms'),
        dipoleMoment=(3.493, 'De'),
        polarizability=(5.750, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
)
