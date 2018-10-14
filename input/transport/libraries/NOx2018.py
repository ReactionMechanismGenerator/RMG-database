#!/usr/bin/env python
# encoding: utf-8

name = "NOx2018"
shortDesc = u"NOx2018"
longDesc = u"""
P. Glarborg, J.A. Miller, B. Ruscic, S.J. Klippenstein
Modeling nitrogen chemistry in combustion
Progress in Energy and Combustion Science
Volume 67, July 2018, Pages 31-68
https://doi.org/10.1016/j.pecs.2018.01.002


 Hydrocarbon subset:

H. Hashemi, J.M. Christensen, S. Gersen, H. Levinsky, S.J. Klippenstein, P. Glarborg,
“High-Pressure Oxidation of Methane”, Combust. Flame 172 (2016) 349-364.

J. Gimenez-Lopez, C.T. Rasmussen, H. Hashemi, M.U. Alzueta, Y. Gao, P. Marshall, C.F. Goldsmith, P. Glarborg,
“Experimental and Kinetic Modeling Study of C2H2 Oxidation at High Pressure, Int. J. Chem. Kinet. 48 (2016) 724-738.

H. Hashemi, J.G. Jacobsen, C.T. Rasmussen, J.M. Christensen, P. Glarborg, S. Gersen, M. van Essen, H.B. Levinsky, S.J. Klippenstein, 
“High-Pressure Oxidation of Ethane”, Combust. Flame 182 (2017) 150-166.

 Nitrogen subset

P. Glarborg, J.A. Miller, B. Ruscic, S.J. Klippenstein
Modeling nitrogen chemistry in combustion
Progress in Energy and Combustion Science
Volume 67, July 2018, Pages 31-68
https://doi.org/10.1016/j.pecs.2018.01.002
"""

entry(
    index=1,
    label="CHCHOH",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,D} {3,S} {4,S}
    2 C u1 p0 c0 {1,D} {5,S}
    3 O u0 p2 c0 {1,S} {6,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {2,S}
    6 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(224.700, 'K'),
        sigma=(4.162, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=2,
    label="OCHCO",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,D} {3,S} {4,S}
    2 C u0 p0 c0 {1,D} {5,D}
    3 O u1 p2 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 O u0 p2 c0 {2,D}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(440.200, 'K'),
        sigma=(4.010, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=3,
    label="HCOH",
    molecule=
    """
    multiplicity 3
    1 C u2 p0 c0 {2,S} {3,S}
    2 O u0 p2 c0 {1,S} {4,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(498.000, 'K'),
        sigma=(3.590, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=4,
    label="CH2CHOOH",
    molecule=
    """
    1 C u0 p0 c0 {2,D} {3,S} {5,S}
    2 C u0 p0 c0 {1,D} {6,S} {7,S}
    3 O u0 p2 c0 {1,S} {4,S}
    4 O u0 p2 c0 {3,S} {8,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {2,S}
    7 H u0 p0 c0 {2,S}
    8 H u0 p0 c0 {4,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(395.0, 'K'),
        sigma=(4.037, 'angstroms'),
        dipoleMoment=(1.3, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=5,
    label="CH2CHOO",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,D} {3,S} {4,S}
    2 C u0 p0 c0 {1,D} {5,S} {6,S}
    3 O u0 p2 c0 {1,S} {7,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {2,S}
    6 H u0 p0 c0 {2,S}
    7 O u1 p2 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(395.0, 'K'),
        sigma=(4.037, 'angstroms'),
        dipoleMoment=(1.3, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=6,
    label="CH3CHOH",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
    2 C u1 p0 c0 {1,S} {3,S} {7,S}
    3 O u0 p2 c0 {2,S} {8,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {1,S}
    7 H u0 p0 c0 {2,S}
    8 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(362.600, 'K'),
        sigma=(4.530, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.5,
    ),
    shortDesc=u"""""",
)

entry(
    index=7,
    label="H2CC",
    molecule=
    """
    1 C u0 p0 c0 {2,D} {3,S} {4,S}
    2 C u0 p1 c0 {1,D}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(209.000, 'K'),
        sigma=(4.100, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.5,
    ),
    shortDesc=u"""""",
)

entry(
    index=8,
    label="CH2OOH",
    molecule=
    """
    multiplicity 2
    1 C u1 p0 c0 {2,S} {4,S} {5,S}
    2 O u0 p2 c0 {1,S} {3,S}
    3 O u0 p2 c0 {2,S} {6,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(417.000, 'K'),
        sigma=(3.690, 'angstroms'),
        dipoleMoment=(1.700, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=9,
    label="CH2CH2OH",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 C u1 p0 c0 {1,S} {6,S} {7,S}
    3 O u0 p2 c0 {1,S} {8,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {2,S}
    7 H u0 p0 c0 {2,S}
    8 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(362.600, 'K'),
        sigma=(4.530, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.5,
    ),
    shortDesc=u"""""",
)

entry(
    index=10,
    label="CH2CHOH",
    molecule=
    """
    1 C u0 p0 c0 {2,D} {3,S} {4,S}
    2 C u0 p0 c0 {1,D} {5,S} {6,S}
    3 O u0 p2 c0 {1,S} {7,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {2,S}
    6 H u0 p0 c0 {2,S}
    7 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(436.000, 'K'),
        sigma=(3.970, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=11,
    label="cC2H4O",
    molecule=
    """
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
    3 O u0 p2 c0 {1,S} {2,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {2,S}
    7 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(436.000, 'K'),
        sigma=(3.970, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=12,
    label="cC2H3O",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 C u1 p0 c0 {1,S} {3,S} {6,S}
    3 O u0 p2 c0 {1,S} {2,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(436.000, 'K'),
        sigma=(3.970, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=13,
    label="CH3CH2OOH",
    molecule=
    """
    1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
    2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
    3  O u0 p2 c0 {1,S} {4,S}
    4  O u0 p2 c0 {3,S} {10,S}
    5  H u0 p0 c0 {1,S}
    6  H u0 p0 c0 {1,S}
    7  H u0 p0 c0 {2,S}
    8  H u0 p0 c0 {2,S}
    9  H u0 p0 c0 {2,S}
    10 H u0 p0 c0 {4,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(395.0, 'K'),
        sigma=(4.037, 'angstroms'),
        dipoleMoment=(1.3, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=14,
    label="CH3CH2OO",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
    3 O u0 p2 c0 {1,S} {9,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {2,S}
    7 H u0 p0 c0 {2,S}
    8 H u0 p0 c0 {2,S}
    9 O u1 p2 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(395.0, 'K'),
        sigma=(4.037, 'angstroms'),
        dipoleMoment=(1.3, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=15,
    label="CH2CH2OOH",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
    2 C u1 p0 c0 {1,S} {7,S} {8,S}
    3 O u0 p2 c0 {1,S} {4,S}
    4 O u0 p2 c0 {3,S} {9,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {1,S}
    7 H u0 p0 c0 {2,S}
    8 H u0 p0 c0 {2,S}
    9 H u0 p0 c0 {4,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(395.0, 'K'),
        sigma=(4.037, 'angstroms'),
        dipoleMoment=(1.3, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=16,
    label="CH3CHOOH",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
    2 C u1 p0 c0 {1,S} {3,S} {8,S}
    3 O u0 p2 c0 {2,S} {4,S}
    4 O u0 p2 c0 {3,S} {9,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {1,S}
    7 H u0 p0 c0 {1,S}
    8 H u0 p0 c0 {2,S}
    9 H u0 p0 c0 {4,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(395.0, 'K'),
        sigma=(4.037, 'angstroms'),
        dipoleMoment=(1.3, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=17,
    label="HOCH2CH2OO",
    molecule=
    """
    multiplicity 2
    1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
    2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
    3  O u0 p2 c0 {1,S} {9,S}
    4  O u0 p2 c0 {2,S} {10,S}
    5  H u0 p0 c0 {1,S}
    6  H u0 p0 c0 {1,S}
    7  H u0 p0 c0 {2,S}
    8  H u0 p0 c0 {2,S}
    9  O u1 p2 c0 {3,S}
    10 H u0 p0 c0 {4,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(395.0, 'K'),
        sigma=(4.037, 'angstroms'),
        dipoleMoment=(1.3, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=18,
    label="HON",
    molecule=
    """
    1 O u0 p1 c+1 {2,D} {3,S}
    2 N u0 p2 c-1 {1,D}
    3 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(116.700, 'K'),
        sigma=(3.492, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=19,
    label="HNO2",
    molecule=
    """
    1 N u0 p0 c+1 {2,S} {3,D} {4,S}
    2 H u0 p0 c0 {1,S}
    3 O u0 p2 c0 {1,D}
    4 O u0 p3 c-1 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(350.000, 'K'),
        sigma=(3.950, 'angstroms'),
        dipoleMoment=(1.639, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=20,
    label="HONO2",
    molecule=
    """
    1 N u0 p0 c+1 {2,S} {3,D} {4,S}
    2 O u0 p2 c0 {1,S} {5,S}
    3 O u0 p2 c0 {1,D}
    4 O u0 p3 c-1 {1,S}
    5 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(400.000, 'K'),
        sigma=(4.200, 'angstroms'),
        dipoleMoment=(0.200, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=21,
    label="H2NN(S)",
    molecule=
    """
    1 N u0 p0 c+1 {2,D} {3,S} {4,S}
    2 N u0 p2 c-1 {1,D}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(71.400, 'K'),
        sigma=(3.798, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=22,
    label="NH2OH",
    molecule=
    """
    1 N u0 p1 c0 {2,S} {3,S} {4,S}
    2 O u0 p2 c0 {1,S} {5,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(116.700, 'K'),
        sigma=(3.492, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=23,
    label="HNC",
    molecule=
    """
    1 N u0 p0 c+1 {2,S} {3,T}
    2 H u0 p0 c0 {1,S}
    3 C u0 p1 c-1 {1,T}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(569.000, 'K'),
        sigma=(3.630, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=24,
    label="HCNH",
    molecule=
    """
    multiplicity 2
    1 C u1 p0 c0 {2,D} {3,S}
    2 N u0 p1 c0 {1,D} {4,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(569.000, 'K'),
        sigma=(3.630, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=25,
    label="CH3NO",
    molecule=
    """
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 N u0 p1 c0 {1,S} {6,D}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 O u0 p2 c0 {2,D}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(436.000, 'K'),
        sigma=(3.970, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=26,
    label="CH3NH2",
    molecule=
    """
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 N u0 p1 c0 {1,S} {6,S} {7,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {2,S}
    7 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(481.800, 'K'),
        sigma=(3.626, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=27,
    label="CH3NH",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 N u1 p1 c0 {1,S} {6,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(481.800, 'K'),
        sigma=(3.626, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=28,
    label="CH2NH2",
    molecule=
    """
    multiplicity 2
    1 C u1 p0 c0 {2,S} {3,S} {4,S}
    2 N u0 p1 c0 {1,S} {5,S} {6,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {2,S}
    6 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(481.800, 'K'),
        sigma=(3.626, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=29,
    label="CH2NH",
    molecule=
    """
    1 C u0 p0 c0 {2,D} {3,S} {4,S}
    2 N u0 p1 c0 {1,D} {5,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(417.000, 'K'),
        sigma=(3.690, 'angstroms'),
        dipoleMoment=(1.7, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=30,
    label="CH3OO",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 O u0 p2 c0 {1,S} {6,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 O u1 p2 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(417.000, 'K'),
        sigma=(3.690, 'angstroms'),
        dipoleMoment=(1.7, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=31,
    label="CH3OOH",
    molecule=
    """
    1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
    2 O u0 p2 c0 {1,S} {3,S}
    3 O u0 p2 c0 {2,S} {7,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {1,S}
    7 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(481.800, 'K'),
        sigma=(3.626, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=32,
    label="HOCH2O",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 O u0 p2 c0 {1,S} {6,S}
    3 O u1 p2 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(470.600, 'K'),
        sigma=(4.410, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.5,
    ),
    shortDesc=u"""""",
)

entry(
    index=33,
    label="HOCO",
    molecule=
    """
    multiplicity 2
    1 C u1 p0 c0 {2,S} {3,D}
    2 O u0 p2 c0 {1,S} {4,S}
    3 O u0 p2 c0 {1,D}
    4 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(498.000, 'K'),
        sigma=(3.590, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=34,
    label="HOCHO",
    molecule=
    """
    1 C u0 p0 c0 {2,S} {3,D} {4,S}
    2 O u0 p2 c0 {1,S} {5,S}
    3 O u0 p2 c0 {1,D}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(481.800, 'K'),
        sigma=(3.626, 'angstroms'),
        dipoleMoment=(1.7, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=35,
    label="OCHO",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {3,D} {4,S}
    2 O u1 p2 c0 {1,S}
    3 O u0 p2 c0 {1,D}
    4 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(498.000, 'K'),
        sigma=(3.590, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=36,
    label="AR",
    molecule=
    """
    1 Ar u0 p4 c0
    """,
    transport=TransportData(
        shapeIndex=0,
        epsilon=(136.500, 'K'),
        sigma=(3.330, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=0.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=37,
    label="C",
    molecule=
    """
    1 C u2 p1 c0
    """,
    transport=TransportData(
        shapeIndex=0,
        epsilon=(97.530, 'K'),
        sigma=(3.621, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(1.76, 'angstroms^3'),
        rotrelaxcollnum=4.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=38,
    label="CH",
    molecule=
    """
    multiplicity 2
    1 C u1 p1 c0 {2,S}
    2 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(80.000, 'K'),
        sigma=(2.750, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=0.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=39,
    label="CH2(S)",
    molecule=
    """
    1 C u0 p1 c0 {2,S} {3,S}
    2 H u0 p0 c0 {1,S}
    3 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(144.000, 'K'),
        sigma=(3.800, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=0.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=40,
    label="CH2",
    molecule=
    """
    multiplicity 3
    1 C u2 p0 c0 {2,S} {3,S}
    2 H u0 p0 c0 {1,S}
    3 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(144.000, 'K'),
        sigma=(3.800, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=0.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=41,
    label="CH3",
    molecule=
    """
    multiplicity 2
    1 C u1 p0 c0 {2,S} {3,S} {4,S}
    2 H u0 p0 c0 {1,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(144.000, 'K'),
        sigma=(3.800, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=0.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=42,
    label="CH4",
    molecule=
    """
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 H u0 p0 c0 {1,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(141.400, 'K'),
        sigma=(3.746, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(2.600, 'angstroms^3'),
        rotrelaxcollnum=13.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=43,
    label="CO",
    molecule=
    """
    1 C u0 p1 c-1 {2,T}
    2 O u0 p1 c+1 {1,T}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(98.100, 'K'),
        sigma=(3.650, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(1.950, 'angstroms^3'),
        rotrelaxcollnum=1.800,
    ),
    shortDesc=u"""""",
)

entry(
    index=44,
    label="CO2",
    molecule=
    """
    1 C u0 p0 c0 {2,D} {3,D}
    2 O u0 p2 c0 {1,D}
    3 O u0 p2 c0 {1,D}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(244.000, 'K'),
        sigma=(3.650, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(2.650, 'angstroms^3'),
        rotrelaxcollnum=2.100,
    ),
    shortDesc=u"""""",
)

entry(
    index=45,
    label="HCO",
    molecule=
    """
    multiplicity 2
    1 C u1 p0 c0 {2,S} {3,D}
    2 H u0 p0 c0 {1,S}
    3 O u0 p2 c0 {1,D}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(498.000, 'K'),
        sigma=(3.590, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=0.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=46,
    label="CH2O",
    molecule=
    """
    1 C u0 p0 c0 {2,D} {3,S} {4,S}
    2 O u0 p2 c0 {1,D}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(498.000, 'K'),
        sigma=(3.590, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=47,
    label="CH2OH",
    molecule=
    """
    multiplicity 2
    1 C u1 p0 c0 {2,S} {3,S} {4,S}
    2 O u0 p2 c0 {1,S} {5,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(417.000, 'K'),
        sigma=(3.690, 'angstroms'),
        dipoleMoment=(1.7, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=48,
    label="CH3O",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 O u1 p2 c0 {1,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(417.000, 'K'),
        sigma=(3.690, 'angstroms'),
        dipoleMoment=(1.7, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=49,
    label="CH3OH",
    molecule=
    """
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 O u0 p2 c0 {1,S} {6,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(481.800, 'K'),
        sigma=(3.626, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=50,
    label="C2",
    molecule=
    """
    multiplicity 3
    1 C u1 p0 c0 {2,T}
    2 C u1 p0 c0 {1,T}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(97.530, 'K'),
        sigma=(3.621, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(1.76, 'angstroms^3'),
        rotrelaxcollnum=4.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=51,
    label="C2O",
    molecule=
    """
    multiplicity 3
    1 C u0 p0 c0 {2,T} {3,S}
    2 C u1 p0 c0 {1,T}
    3 O u1 p2 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(232.400, 'K'),
        sigma=(3.828, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=52,
    label="C2H",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,T} {3,S}
    2 C u1 p0 c0 {1,T}
    3 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(209.000, 'K'),
        sigma=(4.100, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.5,
    ),
    shortDesc=u"""""",
)

entry(
    index=53,
    label="C2H2",
    molecule=
    """
    1 C u0 p0 c0 {2,T} {3,S}
    2 C u0 p0 c0 {1,T} {4,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(209.000, 'K'),
        sigma=(4.100, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.5,
    ),
    shortDesc=u"""""",
)

entry(
    index=54,
    label="C2H3",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,D} {3,S} {4,S}
    2 C u1 p0 c0 {1,D} {5,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(209.000, 'K'),
        sigma=(4.100, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=55,
    label="C2H4",
    molecule=
    """
    1 C u0 p0 c0 {2,D} {3,S} {4,S}
    2 C u0 p0 c0 {1,D} {5,S} {6,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {2,S}
    6 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(280.800, 'K'),
        sigma=(3.971, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.5,
    ),
    shortDesc=u"""""",
)

entry(
    index=56,
    label="C2H5",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 C u1 p0 c0 {1,S} {6,S} {7,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {2,S}
    7 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(252.300, 'K'),
        sigma=(4.302, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.5,
    ),
    shortDesc=u"""""",
)

entry(
    index=57,
    label="C2H6",
    molecule=
    """
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {2,S}
    7 H u0 p0 c0 {2,S}
    8 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(252.300, 'K'),
        sigma=(4.302, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.5,
    ),
    shortDesc=u"""""",
)

entry(
    index=58,
    label="HCCO",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,T} {4,S}
    2 C u0 p0 c0 {1,T} {3,S}
    3 O u1 p2 c0 {2,S}
    4 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(150.000, 'K'),
        sigma=(2.500, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=59,
    label="HCCOH",
    molecule=
    """
    1 C u0 p0 c0 {2,T} {3,S}
    2 C u0 p0 c0 {1,T} {4,S}
    3 O u0 p2 c0 {1,S} {5,S}
    4 H u0 p0 c0 {2,S}
    5 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(436.000, 'K'),
        sigma=(3.970, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=60,
    label="CH2CO",
    molecule=
    """
    1 C u0 p0 c0 {2,D} {3,S} {4,S}
    2 C u0 p0 c0 {1,D} {5,D}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 O u0 p2 c0 {2,D}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(436.000, 'K'),
        sigma=(3.970, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=61,
    label="CH2CHO",
    molecule=
    """
    multiplicity 2
    1 C u1 p0 c0 {2,S} {3,S} {4,S}
    2 C u0 p0 c0 {1,S} {5,D} {6,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 O u0 p2 c0 {2,D}
    6 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(436.000, 'K'),
        sigma=(3.970, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=62,
    label="H",
    molecule=
    """
    multiplicity 2
    1 H u1 p0 c0
    """,
    transport=TransportData(
        shapeIndex=0,
        epsilon=(145.000, 'K'),
        sigma=(2.050, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=0.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=63,
    label="H2",
    molecule=
    """
    1 H u0 p0 c0 {2,S}
    2 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(38.000, 'K'),
        sigma=(2.920, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.790, 'angstroms^3'),
        rotrelaxcollnum=280.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=64,
    label="H2O",
    molecule=
    """
    1 O u0 p2 c0 {2,S} {3,S}
    2 H u0 p0 c0 {1,S}
    3 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(572.400, 'K'),
        sigma=(2.605, 'angstroms'),
        dipoleMoment=(1.844, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=4.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=65,
    label="H2O2",
    molecule=
    """
    1 O u0 p2 c0 {2,S} {3,S}
    2 O u0 p2 c0 {1,S} {4,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(107.400, 'K'),
        sigma=(3.458, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=3.8,
    ),
    shortDesc=u"""""",
)

entry(
    index=66,
    label="HO2",
    molecule=
    """
    multiplicity 2
    1 O u0 p2 c0 {2,S} {3,S}
    2 O u1 p2 c0 {1,S}
    3 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(107.400, 'K'),
        sigma=(3.458, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=67,
    label="N2",
    molecule=
    """
    1 N u0 p1 c0 {2,T}
    2 N u0 p1 c0 {1,T}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(97.530, 'K'),
        sigma=(3.621, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(1.76, 'angstroms^3'),
        rotrelaxcollnum=4.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=68,
    label="O",
    molecule=
    """
    multiplicity 3
    1 O u2 p2 c0
    """,
    transport=TransportData(
        shapeIndex=0,
        epsilon=(80.000, 'K'),
        sigma=(2.750, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=0.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=69,
    label="O2",
    molecule=
    """
    multiplicity 3
    1 O u1 p2 c0 {2,S}
    2 O u1 p2 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(107.400, 'K'),
        sigma=(3.458, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(1.6, 'angstroms^3'),
        rotrelaxcollnum=3.8,
    ),
    shortDesc=u"""""",
)

entry(
    index=70,
    label="OH",
    molecule=
    """
    multiplicity 2
    1 O u1 p2 c0 {2,S}
    2 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(80.000, 'K'),
        sigma=(2.750, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=0.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=71,
    label="HE",
    molecule=
    """
    1 He u0 p1 c0
    """,
    transport=TransportData(
        shapeIndex=0,
        epsilon=(10.200, 'K'),
        sigma=(2.576, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=0.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=72,
    label="HONO",
    molecule=
    """
    1 N u0 p1 c0 {2,S} {3,D}
    2 O u0 p2 c0 {1,S} {4,S}
    3 O u0 p2 c0 {1,D}
    4 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(350.000, 'K'),
        sigma=(3.950, 'angstroms'),
        dipoleMoment=(1.639, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=73,
    label="NO",
    molecule=
    """
    multiplicity 2
    1 N u1 p1 c0 {2,D}
    2 O u0 p2 c0 {1,D}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(139.320, 'K'),
        sigma=(3.339, 'angstroms'),
        dipoleMoment=(0.2, 'De'),
        polarizability=(1.76, 'angstroms^3'),
        rotrelaxcollnum=4.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=74,
    label="HNO",
    molecule=
    """
    1 N u0 p1 c0 {2,D} {3,S}
    2 O u0 p2 c0 {1,D}
    3 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(170.000, 'K'),
        sigma=(3.430, 'angstroms'),
        dipoleMoment=(1.62, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=75,
    label="NO2",
    molecule=
    """
    multiplicity 2
    1 N u0 p1 c0 {2,D} {3,S}
    2 O u0 p2 c0 {1,D}
    3 O u1 p2 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(333.590, 'K'),
        sigma=(3.852, 'angstroms'),
        dipoleMoment=(0.4, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=76,
    label="CH3CH2OH",
    molecule=
    """
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
    3 O u0 p2 c0 {1,S} {9,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {2,S}
    7 H u0 p0 c0 {2,S}
    8 H u0 p0 c0 {2,S}
    9 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(362.600, 'K'),
        sigma=(4.530, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.5,
    ),
    shortDesc=u"""""",
)

entry(
    index=77,
    label="CH3CH2O",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
    2 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
    3 O u1 p2 c0 {2,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {1,S}
    7 H u0 p0 c0 {2,S}
    8 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(362.600, 'K'),
        sigma=(4.530, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.5,
    ),
    shortDesc=u"""""",
)

entry(
    index=78,
    label="CH3CO",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 C u1 p0 c0 {1,S} {6,D}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 O u0 p2 c0 {2,D}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(436.000, 'K'),
        sigma=(3.970, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=79,
    label="CH3CHO",
    molecule=
    """
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 C u0 p0 c0 {1,S} {6,D} {7,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 O u0 p2 c0 {2,D}
    7 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(436.000, 'K'),
        sigma=(3.970, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=80,
    label="OCHCHO",
    molecule=
    """
    1 C u0 p0 c0 {2,S} {3,D} {5,S}
    2 C u0 p0 c0 {1,S} {4,D} {6,S}
    3 O u0 p2 c0 {1,D}
    4 O u0 p2 c0 {2,D}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(440.200, 'K'),
        sigma=(4.010, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=81,
    label="NO3",
    molecule=
    """
    multiplicity 2
    1 N u0 p0 c+1 {2,D} {3,S} {4,S}
    2 O u0 p2 c0 {1,D}
    3 O u0 p3 c-1 {1,S}
    4 O u1 p2 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(400.000, 'K'),
        sigma=(4.200, 'angstroms'),
        dipoleMoment=(0.2, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=82,
    label="N2O",
    molecule=
    """
    1 N u0 p0 c+1 {2,D} {3,D}
    2 N u0 p2 c-1 {1,D}
    3 O u0 p2 c0 {1,D}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(232.400, 'K'),
        sigma=(3.828, 'angstroms'),
        dipoleMoment=(0.2, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=83,
    label="H2NO",
    molecule=
    """
    multiplicity 2
    1 N u1 p0 c+1 {2,S} {3,S} {4,S}
    2 O u0 p3 c-1 {1,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(116.700, 'K'),
        sigma=(3.492, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=84,
    label="HNOH",
    molecule=
    """
    multiplicity 2
    1 N u1 p1 c0 {2,S} {3,S}
    2 O u0 p2 c0 {1,S} {4,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(116.700, 'K'),
        sigma=(3.492, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=85,
    label="CH2CN",
    molecule=
    """
    multiplicity 2
    1 C u1 p0 c0 {2,S} {3,S} {4,S}
    2 C u0 p0 c0 {1,S} {5,T}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 N u0 p1 c0 {2,T}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(422.220, 'K'),
        sigma=(5.329, 'angstroms'),
        dipoleMoment=(3.5, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=86,
    label="CH3CN",
    molecule=
    """
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 C u0 p0 c0 {1,S} {6,T}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 N u0 p1 c0 {2,T}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(422.220, 'K'),
        sigma=(5.329, 'angstroms'),
        dipoleMoment=(3.5, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=87,
    label="NCN",
    molecule=
    """
    multiplicity 3
    1 C u0 p0 c0 {2,D} {3,D}
    2 N u1 p1 c0 {1,D}
    3 N u1 p1 c0 {1,D}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(422.220, 'K'),
        sigma=(5.329, 'angstroms'),
        dipoleMoment=(2.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=88,
    label="HNCN",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {3,T}
    2 N u1 p1 c0 {1,S} {4,S}
    3 N u0 p1 c0 {1,T}
    4 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(422.220, 'K'),
        sigma=(5.329, 'angstroms'),
        dipoleMoment=(2.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=89,
    label="HNCNH",
    molecule=
    """
    1 C u0 p0 c0 {2,D} {3,D}
    2 N u0 p1 c0 {1,D} {4,S}
    3 N u0 p1 c0 {1,D} {5,S}
    4 H u0 p0 c0 {2,S}
    5 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(422.220, 'K'),
        sigma=(5.329, 'angstroms'),
        dipoleMoment=(2.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=90,
    label="CN",
    molecule=
    """
    multiplicity 2
    1 C u1 p0 c0 {2,T}
    2 N u0 p1 c0 {1,T}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(75.000, 'K'),
        sigma=(3.856, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=91,
    label="H2CN",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,D} {3,S} {4,S}
    2 N u1 p1 c0 {1,D}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(569.000, 'K'),
        sigma=(3.630, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=92,
    label="HCN",
    molecule=
    """
    1 C u0 p0 c0 {2,T} {3,S}
    2 N u0 p1 c0 {1,T}
    3 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(569.000, 'K'),
        sigma=(3.630, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=93,
    label="HCNO",
    molecule=
    """
    1 N u0 p0 c+1 {2,T} {3,S}
    2 C u0 p0 c0 {1,T} {4,S}
    3 O u0 p3 c-1 {1,S}
    4 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(232.400, 'K'),
        sigma=(3.828, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=94,
    label="HOCN",
    molecule=
    """
    1 C u0 p0 c0 {2,S} {3,T}
    2 O u0 p2 c0 {1,S} {4,S}
    3 N u0 p1 c0 {1,T}
    4 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(232.400, 'K'),
        sigma=(3.828, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=95,
    label="HNCO",
    molecule=
    """
    1 N u0 p1 c0 {2,D} {4,S}
    2 C u0 p0 c0 {1,D} {3,D}
    3 O u0 p2 c0 {2,D}
    4 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(232.400, 'K'),
        sigma=(3.828, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=96,
    label="HNNO",
    molecule=
    """
    multiplicity 2
    1 O u0 p2 c0 {2,D}
    2 N u0 p1 c0 {1,D} {3,S}
    3 N u1 p1 c0 {2,S} {4,S}
    4 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(232.400, 'K'),
        sigma=(3.828, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=97,
    label="N",
    molecule=
    """
    multiplicity 4
    1 N u3 p1 c0
    """,
    transport=TransportData(
        shapeIndex=0,
        epsilon=(71.400, 'K'),
        sigma=(3.298, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=0.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=98,
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
        epsilon=(71.400, 'K'),
        sigma=(3.798, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=99,
    label="N2H3",
    molecule=
    """
    multiplicity 2
    1 N u0 p1 c0 {2,S} {3,S} {4,S}
    2 N u1 p1 c0 {1,S} {5,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(200.000, 'K'),
        sigma=(3.900, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=100,
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
        epsilon=(205.000, 'K'),
        sigma=(4.230, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(4.26, 'angstroms^3'),
        rotrelaxcollnum=1.5,
    ),
    shortDesc=u"""""",
)

entry(
    index=101,
    label="NCO",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,D} {3,D}
    2 N u1 p1 c0 {1,D}
    3 O u0 p2 c0 {1,D}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(232.400, 'K'),
        sigma=(3.828, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=102,
    label="NH",
    molecule=
    """
    multiplicity 3
    1 N u2 p1 c0 {2,S}
    2 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(80.000, 'K'),
        sigma=(2.650, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=4.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=103,
    label="NH2",
    molecule=
    """
    multiplicity 2
    1 N u1 p1 c0 {2,S} {3,S}
    2 H u0 p0 c0 {1,S}
    3 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(80.000, 'K'),
        sigma=(2.650, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(2.26, 'angstroms^3'),
        rotrelaxcollnum=4.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=104,
    label="NH3",
    molecule=
    """
    1 N u0 p1 c0 {2,S} {3,S} {4,S}
    2 H u0 p0 c0 {1,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(481.000, 'K'),
        sigma=(2.920, 'angstroms'),
        dipoleMoment=(1.47, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=10.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=105,
    label="NNH",
    molecule=
    """
    multiplicity 2
    1 N u0 p1 c0 {2,D} {3,S}
    2 N u1 p1 c0 {1,D}
    3 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(71.400, 'K'),
        sigma=(3.798, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=106,
    label="NCNO",
    molecule=
    """
    1 N u0 p1 c0 {2,S} {3,D}
    2 C u0 p0 c0 {1,S} {4,T}
    3 O u0 p2 c0 {1,D}
    4 N u0 p1 c0 {2,T}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(232.400, 'K'),
        sigma=(3.828, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=107,
    label="NCCN",
    molecule=
    """
    multiplicity 3
    1 C u0 p0 c0 {2,S} {3,T}
    2 C u1 p0 c0 {1,S} {4,D}
    3 N u0 p1 c0 {1,T}
    4 N u1 p1 c0 {2,D}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(374.000, 'K'),
        sigma=(4.361, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=108,
    label="O3",
    molecule=
    """
    1 O u0 p3 c-1 {2,S}
    2 O u0 p1 c+1 {1,S} {3,D}
    3 O u0 p2 c0 {2,D}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(180.000, 'K'),
        sigma=(4.100, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=109,
    label="Cl",
    molecule=
    """
    multiplicity 2
    1 Cl u1 p3 c0
    """,
    transport=TransportData(
        shapeIndex=0,
        epsilon=(130.800, 'K'),
        sigma=(3.613, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=110,
    label="HCl",
    molecule=
    """
    1 H  u0 p0 c0 {2,S}
    2 Cl u0 p3 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(344.700, 'K'),
        sigma=(3.339, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

# entry(
#    index = 111,
#    label = "F",
#    molecule =
# """
# multiplicity 2
# 1 F u1 p3 c0
# """,
#    transport = TransportData(
#        shapeIndex = 0,
#        epsilon = (80.000,'K'),
#        sigma = (2.750,'angstroms'),
#        dipoleMoment = (0.0,'De'),
#        polarizability = (0.0,'angstroms^3'),
#        rotrelaxcollnum = 0.0,
#    ),
#    shortDesc = u"""""",
# )

# entry(
#    index = 112,
#    label = "HF",
#    molecule =
# """
# 1 H u0 p0 c0 {2,S}
# 2 F u0 p3 c0 {1,S}
# """,
#    transport = TransportData(
#        shapeIndex = 1,
#        epsilon = (330.000,'K'),
#        sigma = (3.148,'angstroms'),
#        dipoleMoment = (1.92,'De'),
#        polarizability = (2.46,'angstroms^3'),
#        rotrelaxcollnum = 1.0,
#    ),
#    shortDesc = u"""""",
# )

# entry(
#    index = 113,
#    label = "F2",
#    molecule =
# """
# 1 F u0 p3 c0 {2,S}
# 2 F u0 p3 c0 {1,S}
# """,
#    transport = TransportData(
#        shapeIndex = 1,
#        epsilon = (80.000,'K'),
#        sigma = (2.750,'angstroms'),
#        dipoleMoment = (0.0,'De'),
#        polarizability = (0.0,'angstroms^3'),
#        rotrelaxcollnum = 0.0,
#    ),
#    shortDesc = u"""""",
# )

entry(
    index=114,
    label="H2S",
    molecule=
    """
    1 S u0 p2 c0 {2,S} {3,S}
    2 H u0 p0 c0 {1,S}
    3 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(301.000, 'K'),
        sigma=(3.600, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=115,
    label="HSO2",
    molecule=
    """
    multiplicity 2
    1 O u0 p2 c0 {2,D}
    2 S u1 p0 c0 {1,D} {3,S} {4,D}
    3 H u0 p0 c0 {2,S}
    4 O u0 p2 c0 {2,D}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(252.000, 'K'),
        sigma=(4.290, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=116,
    label="S",
    molecule=
    """
    multiplicity 3
    1 S u2 p2 c0
    """,
    transport=TransportData(
        shapeIndex=0,
        epsilon=(847.000, 'K'),
        sigma=(3.839, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=0.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=117,
    label="S2",
    molecule=
    """
    multiplicity 3
    1 S u1 p2 c0 {2,S}
    2 S u1 p2 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(847.000, 'K'),
        sigma=(3.900, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=118,
    label="SH",
    molecule=
    """
    multiplicity 2
    1 S u1 p2 c0 {2,S}
    2 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(847.000, 'K'),
        sigma=(3.900, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=119,
    label="SO",
    molecule=
    """
    multiplicity 3
    1 S u1 p2 c0 {2,S}
    2 O u1 p2 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(301.000, 'K'),
        sigma=(3.993, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=120,
    label="SO2",
    molecule=
    """
    1 O u0 p2 c0 {2,D}
    2 S u0 p1 c0 {1,D} {3,D}
    3 O u0 p2 c0 {2,D}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(252.000, 'K'),
        sigma=(4.290, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=121,
    label="SO3",
    molecule=
    """
    1 O u0 p2 c0 {2,D}
    2 S u0 p0 c0 {1,D} {3,D} {4,D}
    3 O u0 p2 c0 {2,D}
    4 O u0 p2 c0 {2,D}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(378.400, 'K'),
        sigma=(4.175, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=122,
    label="CH2NO",
    molecule=
    """
    multiplicity 2
    1 C u1 p0 c0 {2,S} {3,S} {4,S}
    2 N u0 p1 c0 {1,S} {5,D}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 O u0 p2 c0 {2,D}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(232.400, 'K'),
        sigma=(3.828, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=123,
    label="C2H5NO",
    molecule=
    """
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
    3 N u0 p1 c0 {1,S} {9,D}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {2,S}
    7 H u0 p0 c0 {2,S}
    8 H u0 p0 c0 {2,S}
    9 O u0 p2 c0 {3,D}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(252.000, 'K'),
        sigma=(4.760, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=124,
    label="CH3CHNO",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
    2 C u0 p0 c0 {1,S} {3,D} {7,S}
    3 N u0 p1 c0 {2,D} {8,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {1,S}
    7 H u0 p0 c0 {2,S}
    8 O u1 p2 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(252.000, 'K'),
        sigma=(4.760, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=125,
    label="CHCHNO",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,D} {3,S} {4,S}
    2 C u1 p0 c0 {1,D} {5,S}
    3 N u0 p1 c0 {1,S} {6,D}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {2,S}
    6 O u0 p2 c0 {3,D}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(357.000, 'K'),
        sigma=(5.180, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=126,
    label="CH2CHNO",
    molecule=
    """
    1 C u0 p0 c0 {2,D} {3,S} {4,S}
    2 C u0 p0 c0 {1,D} {5,S} {6,S}
    3 N u0 p1 c0 {1,S} {7,D}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {2,S}
    6 H u0 p0 c0 {2,S}
    7 O u0 p2 c0 {3,D}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(357.000, 'K'),
        sigma=(5.176, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=127,
    label="CH3NO2",
    molecule=
    """
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 N u0 p0 c+1 {1,S} {6,D} {7,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 O u0 p2 c0 {2,D}
    7 O u0 p3 c-1 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(232.400, 'K'),
        sigma=(3.828, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=128,
    label="CH3ONO",
    molecule=
    """
    1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
    2 O u0 p2 c0 {1,S} {3,S}
    3 N u0 p1 c0 {2,S} {7,D}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {1,S}
    7 O u0 p2 c0 {3,D}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(232.400, 'K'),
        sigma=(3.828, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=129,
    label="CH2NO2",
    molecule=
    """
    multiplicity 2
    1 N u0 p0 c+1 {2,S} {3,D} {6,S}
    2 C u1 p0 c0 {1,S} {4,S} {5,S}
    3 O u0 p2 c0 {1,D}
    4 H u0 p0 c0 {2,S}
    5 H u0 p0 c0 {2,S}
    6 O u0 p3 c-1 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(232.400, 'K'),
        sigma=(3.828, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=130,
    label="C2H5NO2",
    molecule=
    """
    1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
    3  N u0 p0 c+1 {1,S} {9,D} {10,S}
    4  H u0 p0 c0 {1,S}
    5  H u0 p0 c0 {1,S}
    6  H u0 p0 c0 {2,S}
    7  H u0 p0 c0 {2,S}
    8  H u0 p0 c0 {2,S}
    9  O u0 p2 c0 {3,D}
    10 O u0 p3 c-1 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(503.072, 'K'),
        sigma=(5.340, 'angstroms'),
        dipoleMoment=(1.67, 'De'),
        polarizability=(8.88, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=131,
    label="CH2CH2NO2",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 N u0 p0 c+1 {1,S} {6,D} {7,S}
    3 C u1 p0 c0 {1,S} {8,S} {9,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 O u0 p2 c0 {2,D}
    7 O u0 p3 c-1 {2,S}
    8 H u0 p0 c0 {3,S}
    9 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(503.072, 'K'),
        sigma=(5.340, 'angstroms'),
        dipoleMoment=(1.67, 'De'),
        polarizability=(8.88, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=132,
    label="CH3CHNO2",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
    2 C u1 p0 c0 {1,S} {3,S} {7,S}
    3 N u0 p0 c+1 {2,S} {8,D} {9,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {1,S}
    7 H u0 p0 c0 {2,S}
    8 O u0 p2 c0 {3,D}
    9 O u0 p3 c-1 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(503.072, 'K'),
        sigma=(5.340, 'angstroms'),
        dipoleMoment=(1.67, 'De'),
        polarizability=(8.88, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=133,
    label="CH3ONO2",
    molecule=
    """
    1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
    2 N u0 p0 c+1 {3,S} {7,D} {8,S}
    3 O u0 p2 c0 {1,S} {2,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {1,S}
    7 O u0 p2 c0 {2,D}
    8 O u0 p3 c-1 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(459.500, 'K'),
        sigma=(5.036, 'angstroms'),
        dipoleMoment=(1.7, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=134,
    label="CH3CH2ONO",
    molecule=
    """
    1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
    2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
    3  O u0 p2 c0 {1,S} {4,S}
    4  N u0 p1 c0 {3,S} {10,D}
    5  H u0 p0 c0 {1,S}
    6  H u0 p0 c0 {1,S}
    7  H u0 p0 c0 {2,S}
    8  H u0 p0 c0 {2,S}
    9  H u0 p0 c0 {2,S}
    10 O u0 p2 c0 {4,D}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(503.072, 'K'),
        sigma=(5.340, 'angstroms'),
        dipoleMoment=(1.67, 'De'),
        polarizability=(8.8, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=135,
    label="CH3CH2ONO2",
    molecule=
    """
    1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
    2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
    3  N u0 p0 c+1 {4,S} {10,D} {11,S}
    4  O u0 p2 c0 {1,S} {3,S}
    5  H u0 p0 c0 {1,S}
    6  H u0 p0 c0 {1,S}
    7  H u0 p0 c0 {2,S}
    8  H u0 p0 c0 {2,S}
    9  H u0 p0 c0 {2,S}
    10 O u0 p2 c0 {3,D}
    11 O u0 p3 c-1 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(496.000, 'K'),
        sigma=(5.200, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=136,
    label="HNC",
    molecule=
    """
    1 N u0 p0 c+1 {2,S} {3,T}
    2 H u0 p0 c0 {1,S}
    3 C u0 p1 c-1 {1,T}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(569.000, 'K'),
        sigma=(3.630, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=137,
    label="CH3CH2NH2",
    molecule=
    """
    1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
    3  N u0 p1 c0 {1,S} {9,S} {10,S}
    4  H u0 p0 c0 {1,S}
    5  H u0 p0 c0 {1,S}
    6  H u0 p0 c0 {2,S}
    7  H u0 p0 c0 {2,S}
    8  H u0 p0 c0 {2,S}
    9  H u0 p0 c0 {3,S}
    10 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(436.000, 'K'),
        sigma=(3.970, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=138,
    label="CH3NHCH3",
    molecule=
    """
    1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
    2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
    3  N u0 p1 c0 {1,S} {2,S} {10,S}
    4  H u0 p0 c0 {1,S}
    5  H u0 p0 c0 {1,S}
    6  H u0 p0 c0 {1,S}
    7  H u0 p0 c0 {2,S}
    8  H u0 p0 c0 {2,S}
    9  H u0 p0 c0 {2,S}
    10 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(436.000, 'K'),
        sigma=(3.970, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=139,
    label="CH2CH2NH2",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 C u1 p0 c0 {1,S} {6,S} {7,S}
    3 N u0 p1 c0 {1,S} {8,S} {9,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {2,S}
    7 H u0 p0 c0 {2,S}
    8 H u0 p0 c0 {3,S}
    9 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(436.000, 'K'),
        sigma=(3.970, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=140,
    label="CH3NCH3",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
    2 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
    3 N u1 p1 c0 {1,S} {2,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {1,S}
    7 H u0 p0 c0 {2,S}
    8 H u0 p0 c0 {2,S}
    9 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(436.000, 'K'),
        sigma=(3.970, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=141,
    label="CH3NHCH2",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
    2 N u0 p1 c0 {1,S} {3,S} {7,S}
    3 C u1 p0 c0 {2,S} {8,S} {9,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {1,S}
    7 H u0 p0 c0 {2,S}
    8 H u0 p0 c0 {3,S}
    9 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(436.000, 'K'),
        sigma=(3.970, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=142,
    label="CH3CHNH2",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
    2 C u1 p0 c0 {1,S} {3,S} {7,S}
    3 N u0 p1 c0 {2,S} {8,S} {9,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {1,S}
    7 H u0 p0 c0 {2,S}
    8 H u0 p0 c0 {3,S}
    9 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(436.000, 'K'),
        sigma=(3.970, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=143,
    label="CH3CH2NH",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
    3 N u1 p1 c0 {1,S} {9,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {2,S}
    7 H u0 p0 c0 {2,S}
    8 H u0 p0 c0 {2,S}
    9 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(436.000, 'K'),
        sigma=(3.970, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=144,
    label="CH2CHNH2",
    molecule=
    """
    1 C u0 p0 c0 {2,S} {3,D} {4,S}
    2 N u0 p1 c0 {1,S} {5,S} {6,S}
    3 C u0 p0 c0 {1,D} {7,S} {8,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {2,S}
    6 H u0 p0 c0 {2,S}
    7 H u0 p0 c0 {3,S}
    8 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(303.400, 'K'),
        sigma=(4.810, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=145,
    label="CH3CHNH",
    molecule=
    """
    1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
    2 C u0 p0 c0 {1,S} {3,D} {7,S}
    3 N u0 p1 c0 {2,D} {8,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {1,S}
    7 H u0 p0 c0 {2,S}
    8 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(303.400, 'K'),
        sigma=(4.810, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=146,
    label="CH3NCH2",
    molecule=
    """
    1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
    2 C u0 p0 c0 {3,D} {7,S} {8,S}
    3 N u0 p1 c0 {1,S} {2,D}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {1,S}
    7 H u0 p0 c0 {2,S}
    8 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(303.400, 'K'),
        sigma=(4.810, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=147,
    label="CH2CHNH",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {3,D} {4,S}
    2 C u1 p0 c0 {1,S} {5,S} {6,S}
    3 N u0 p1 c0 {1,D} {7,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {2,S}
    6 H u0 p0 c0 {2,S}
    7 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(307.800, 'K'),
        sigma=(4.140, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=148,
    label="CHCHNH2",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {3,D} {4,S}
    2 N u0 p1 c0 {1,S} {5,S} {6,S}
    3 C u1 p0 c0 {1,D} {7,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {2,S}
    6 H u0 p0 c0 {2,S}
    7 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(307.800, 'K'),
        sigma=(4.140, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=149,
    label="CH2NCH2",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {3,D} {6,S} {7,S}
    2 C u1 p0 c0 {3,S} {4,S} {5,S}
    3 N u0 p1 c0 {1,D} {2,S}
    4 H u0 p0 c0 {2,S}
    5 H u0 p0 c0 {2,S}
    6 H u0 p0 c0 {1,S}
    7 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(307.800, 'K'),
        sigma=(4.140, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=150,
    label="CH3CHN",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 C u0 p0 c0 {1,S} {6,D} {7,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 N u1 p1 c0 {2,D}
    7 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(307.800, 'K'),
        sigma=(4.140, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=151,
    label="CH3NCH",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
    2 N u0 p1 c0 {1,S} {3,D}
    3 C u1 p0 c0 {2,D} {7,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {1,S}
    7 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(307.800, 'K'),
        sigma=(4.140, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=152,
    label="CH3CNH",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
    2 C u1 p0 c0 {1,S} {3,D}
    3 N u0 p1 c0 {2,D} {7,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {1,S}
    7 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(307.800, 'K'),
        sigma=(4.140, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=153,
    label="CH2CNH2",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {3,D} {4,S} {5,S}
    2 N u0 p1 c0 {3,S} {6,S} {7,S}
    3 C u1 p0 c0 {1,D} {2,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {2,S}
    7 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(307.800, 'K'),
        sigma=(4.140, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=154,
    label="CH2CNH",
    molecule=
    """
    1 C u0 p0 c0 {2,D} {4,S} {5,S}
    2 C u0 p0 c0 {1,D} {3,D}
    3 N u0 p1 c0 {2,D} {6,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(260.000, 'K'),
        sigma=(4.850, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=155,
    label="CH2CHN",
    molecule=
    """
    multiplicity 3
    1 C u0 p0 c0 {2,S} {3,D} {6,S}
    2 C u1 p0 c0 {1,S} {4,S} {5,S}
    3 N u1 p1 c0 {1,D}
    4 H u0 p0 c0 {2,S}
    5 H u0 p0 c0 {2,S}
    6 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(260.000, 'K'),
        sigma=(4.850, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=156,
    label="CH2CHN(S)",
    molecule=
    """
    1 C u0 p0 c0 {2,D} {4,S} {5,S}
    2 C u0 p0 c0 {1,D} {3,S} {6,S}
    3 N u0 p2 c0 {2,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(260.000, 'K'),
        sigma=(4.850, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=157,
    label="c-C2H3N",
    molecule=
    """
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 C u0 p0 c0 {1,S} {3,D} {6,S}
    3 N u0 p1 c0 {1,S} {2,D}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(260.000, 'K'),
        sigma=(4.850, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=158,
    label="CHCNH2",
    molecule=
    """
    1 N u0 p1 c0 {2,S} {4,S} {5,S}
    2 C u0 p0 c0 {1,S} {3,T}
    3 C u0 p0 c0 {2,T} {6,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(260.000, 'K'),
        sigma=(4.850, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=159,
    label="CHCNH",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,T} {3,S}
    2 C u0 p0 c0 {1,T} {5,S}
    3 N u1 p1 c0 {1,S} {4,S}
    4 H u0 p0 c0 {3,S}
    5 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(252.000, 'K'),
        sigma=(4.760, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=160,
    label="H2NCHO",
    molecule=
    """
    1 N u0 p1 c0 {2,S} {4,S} {5,S}
    2 C u0 p0 c0 {1,S} {3,D} {6,S}
    3 O u0 p2 c0 {2,D}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(307.800, 'K'),
        sigma=(4.140, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=161,
    label="H2NCO",
    molecule=
    """
    multiplicity 2
    1 N u0 p1 c0 {2,S} {3,S} {4,S}
    2 C u1 p0 c0 {1,S} {5,D}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 O u0 p2 c0 {2,D}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(307.800, 'K'),
        sigma=(4.140, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=162,
    label="CH3NC",
    molecule=
    """
    multiplicity 3
    1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
    2 N u0 p1 c0 {1,S} {3,D}
    3 C u2 p0 c0 {2,D}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(422.220, 'K'),
        sigma=(5.329, 'angstroms'),
        dipoleMoment=(3.5, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=163,
    label="CH3C(O)OO",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
    2 C u0 p0 c0 {1,S} {3,S} {7,D}
    3 O u0 p2 c0 {2,S} {8,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {1,S}
    7 O u0 p2 c0 {2,D}
    8 O u1 p2 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(435.500, 'K'),
        sigma=(4.860, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=164,
    label="CHCHO",
    molecule=
    """
    multiplicity 3
    1 C u0 p0 c0 {2,D} {3,S} {4,S}
    2 C u1 p0 c0 {1,D} {5,S}
    3 O u1 p2 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(436.000, 'K'),
        sigma=(3.970, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

"""
Comments weee not parsed correctly, and can be found in the original paper's Supplementary Information's transport file.
Note that additional species which weren't added to this library were also given in the transport file this library was
imported from. These species were not added here since they were not described by the respective kinetics/thermo files.
"""
