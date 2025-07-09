#!/usr/bin/env python
# encoding: utf-8

name = "Elliott_OOQOOH"
shortDesc = ""
longDesc = """
Thermo added from Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

They used five methodologies, with M1 at the highest (CBH_ANL with CCSD(T)-F12/ccpVTZ-F12 for energies)
and M5 at the lowest (also CBH_ANL but B2PLYP-D3/cc-pVTZ for energies and a different protocol for torsions)

In cases where they computed the same species using multiple methodologies, I defaulted to the highest level of theory
because RMG can only handle one thermo entry per species for a given library.
"""
entry(
    index = 0,
    label = "aC2H4O2H-2O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3  O u0 p2 c0 {1,S} {5,S}
4  O u0 p2 c0 {2,S} {10,S}
5  O u0 p2 c0 {3,S} {11,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 O u1 p2 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.09779,0.0239146,-1.1369e-06,-1.33835e-08,6.50201e-12,-13548.5,-0.169569], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.20372,0.0227973,-1.1569e-05,2.83434e-09,-2.72182e-13,-14318,-12.0957], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 1
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvtz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/cc-pvtz//RUwb97xd/cc-pvtz
CBH reference scheme: cbh2
""",
)

entry(
    index = 1,
    label = "aNC3H6O2H-2O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  O u0 p2 c0 {2,S} {6,S}
5  O u0 p2 c0 {1,S} {13,S}
6  O u0 p2 c0 {4,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u1 p2 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.20595,0.0207016,5.03907e-05,-8.42811e-08,3.60785e-11,-17262.7,9.36396], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.42573,0.0326372,-1.66774e-05,4.10577e-09,-3.95606e-13,-18896.2,-11.6228], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 1
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvtz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/cc-pvtz//RUwb97xd/cc-pvtz
CBH reference scheme: cbh2
""",
)

entry(
    index = 2,
    label = "aNC3H6O2H-3O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
4  O u0 p2 c0 {2,S} {6,S}
5  O u0 p2 c0 {3,S} {13,S}
6  O u0 p2 c0 {4,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 O u1 p2 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.037,0.00661828,8.28227e-05,-1.18484e-07,4.90169e-11,-17830.1,-10.862], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.0847,0.0298241,-1.53129e-05,3.77967e-09,-3.64729e-13,-19458.5,-27.5543], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 1
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvtz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/cc-pvtz//RUwb97xd/cc-pvtz
CBH reference scheme: cbh2
""",
)

entry(
    index = 3,
    label = "aIC3H6O2H1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  O u0 p2 c0 {1,S} {6,S}
5  O u0 p2 c0 {2,S} {13,S}
6  O u0 p2 c0 {4,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u1 p2 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.74478,0.0184842,5.70414e-05,-9.13564e-08,3.86405e-11,-17767.2,5.63888], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.5846,0.033455,-1.73935e-05,4.32845e-09,-4.20063e-13,-19389.9,-13.861], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 1
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvtz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/cc-pvtz//RUwb97xd/cc-pvtz
CBH reference scheme: cbh2
""",
)

entry(
    index = 4,
    label = "aNBT1O2H-2O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {3,S} {7,S}
6  O u0 p2 c0 {1,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.1219,0.0191113,6.81787e-05,-1.06565e-07,4.49475e-11,-21190,-9.68478], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.6311,0.0381858,-1.92716e-05,4.69785e-09,-4.49123e-13,-22822.8,-28.1057], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 1
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvtz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/cc-pvtz//RUwb97xd/cc-pvtz
CBH reference scheme: cbh2
""",
)

entry(
    index = 5,
    label = "aNBT1O2H-3O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {3,S} {7,S}
6  O u0 p2 c0 {1,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.34258,0.0320409,3.4407e-05,-7.00254e-08,3.07632e-11,-23021.6,-9.1506], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.9836,0.0375478,-1.93261e-05,4.78659e-09,-4.63532e-13,-24962.6,-36.9803], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 1
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvtz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/cc-pvtz//RUwb97xd/cc-pvtz
CBH reference scheme: cbh2
""",
)

entry(
    index = 6,
    label = "aNBT1O2H-4O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
5  O u0 p2 c0 {3,S} {7,S}
6  O u0 p2 c0 {4,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.80172,0.0276826,4.90001e-05,-8.98038e-08,3.96709e-11,-21000,-10.2832], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.1527,0.0365996,-1.84644e-05,4.49205e-09,-4.28387e-13,-22875.4,-36.9302], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 1
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvtz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/cc-pvtz//RUwb97xd/cc-pvtz
CBH reference scheme: cbh2
""",
)

entry(
    index = 7,
    label = "aNBT2O2H-1O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {3,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.62421,0.0568602,-1.94422e-05,-2.30466e-08,1.62559e-11,-21051.8,6.49583], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.3721,0.0358564,-1.78759e-05,4.30633e-09,-4.0743e-13,-23325.4,-38.6635], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 1
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvtz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/cc-pvtz//RUwb97xd/cc-pvtz
CBH reference scheme: cbh2
""",
)

entry(
    index = 8,
    label = "aNBT2O2H-3O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {8,S}
3  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {2,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.29687,0.0614033,-2.18826e-05,-2.60597e-08,1.86286e-11,-22850.1,11.2989], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[15.0318,0.0350181,-1.74889e-05,4.22674e-09,-4.01307e-13,-25622.6,-44.005], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 1
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvtz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/cc-pvtz//RUwb97xd/cc-pvtz
CBH reference scheme: cbh2
""",
)

entry(
    index = 9,
    label = "aNBT2O2H-4O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {3,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.03537,0.0477684,1.1865e-05,-5.91734e-08,3.00703e-11,-22377.6,5.78262], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[15.1009,0.0354018,-1.78835e-05,4.36403e-09,-4.1769e-13,-25130.5,-43.1562], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 1
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvtz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/cc-pvtz//RUwb97xd/cc-pvtz
CBH reference scheme: cbh2
""",
)

entry(
    index = 10,
    label = "aIBT1O2H-2O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {1,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.68665,0.0492002,-6.64963e-06,-3.03469e-08,1.72457e-11,-23847.9,0.386978], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.2399,0.0377258,-1.90043e-05,4.61366e-09,-4.39142e-13,-25749,-34.4621], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 1
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvtz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/cc-pvtz//RUwb97xd/cc-pvtz
CBH reference scheme: cbh2
""",
)

entry(
    index = 11,
    label = "aIBT1O2H-3O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {3,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.45977,0.0316529,5.28378e-05,-1.00947e-07,4.5272e-11,-21111.9,1.6347], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.9654,0.0368545,-1.86734e-05,4.56622e-09,-4.37639e-13,-23617.7,-36.4942], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 1
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvtz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/cc-pvtz//RUwb97xd/cc-pvtz
CBH reference scheme: cbh2
""",
)

entry(
    index = 12,
    label = "aIBT2O2H-1O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {2,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.35529,0.0573877,-2.0289e-05,-2.10414e-08,1.49365e-11,-23507.9,5.7485], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.4488,0.0359873,-1.80397e-05,4.36787e-09,-4.15146e-13,-25933,-41.4236], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 1
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvtz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/cc-pvtz//RUwb97xd/cc-pvtz
CBH reference scheme: cbh2
""",
)

entry(
    index = 13,
    label = "aNPT1O2H-2O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  O u0 p2 c0 {4,S} {8,S}
7  O u0 p2 c0 {1,S} {19,S}
8  O u0 p2 c0 {6,S} {20,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 O u1 p2 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.59339,0.0264525,8.81735e-05,-1.42205e-07,6.09034e-11,-23872.6,1.9276], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.3846,0.0470666,-2.37825e-05,5.80497e-09,-5.55602e-13,-26362.8,-29.7767], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 2
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/cc-pvtz//RUwb97xd/cc-pvtz
CBH reference scheme: cbh2
""",
)

entry(
    index = 14,
    label = "aNPT1O2H-3O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  O u0 p2 c0 {4,S} {8,S}
7  O u0 p2 c0 {1,S} {19,S}
8  O u0 p2 c0 {6,S} {20,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 O u1 p2 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.27996,0.0207109,0.000111836,-1.70923e-07,7.20847e-11,-25103.3,-2.956], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.7043,0.0472582,-2.44577e-05,6.07155e-09,-5.88418e-13,-28084.2,-39.6565], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 2
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/cc-pvtz//RUwb97xd/cc-pvtz
CBH reference scheme: cbh2
""",
)

entry(
    index = 15,
    label = "aNPT1O2H-4O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  O u0 p2 c0 {4,S} {8,S}
7  O u0 p2 c0 {1,S} {19,S}
8  O u0 p2 c0 {6,S} {20,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 O u1 p2 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.40328,0.0500027,2.49512e-05,-7.80007e-08,3.78312e-11,-25992.7,-4.70829], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[17.1856,0.0428742,-2.16362e-05,5.2666e-09,-5.02591e-13,-28831.8,-53.1248], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 2
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/cc-pvtz//RUwb97xd/cc-pvtz
CBH reference scheme: cbh2
""",
)

entry(
    index = 16,
    label = "aNPT1O2H-5O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {6,S} {17,S} {18,S}
5  C u0 p0 c0 {2,S} {7,S} {15,S} {16,S}
6  O u0 p2 c0 {4,S} {8,S}
7  O u0 p2 c0 {5,S} {19,S}
8  O u0 p2 c0 {6,S} {20,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 O u1 p2 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.5511,0.010607,0.000120842,-1.72666e-07,7.14068e-11,-23796.2,-17.7604], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.589,0.0467433,-2.3899e-05,5.87154e-09,-5.64092e-13,-25895.5,-37.1229], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 2
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/cc-pvtz//RUwb97xd/cc-pvtz
CBH reference scheme: cbh2
""",
)

entry(
    index = 17,
    label = "aNPT2O2H-1O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  O u0 p2 c0 {1,S} {8,S}
7  O u0 p2 c0 {4,S} {19,S}
8  O u0 p2 c0 {6,S} {20,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 O u1 p2 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.46254,0.0193076,0.000100244,-1.48321e-07,6.12706e-11,-23454.9,-1.49041], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.7374,0.0504052,-2.59963e-05,6.44089e-09,-6.23415e-13,-25510.1,-21.296], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 2
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/cc-pvtz//RUwb97xd/cc-pvtz
CBH reference scheme: cbh2
""",
)

entry(
    index = 18,
    label = "aNPT2O2H-3O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
6  O u0 p2 c0 {2,S} {8,S}
7  O u0 p2 c0 {1,S} {19,S}
8  O u0 p2 c0 {6,S} {20,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 O u1 p2 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.87152,0.0596419,9.59872e-06,-6.93204e-08,3.64717e-11,-26415.6,-0.456057], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[19.1252,0.0393513,-1.94313e-05,4.65767e-09,-4.39506e-13,-29959.6,-65.7275], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 2
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/cc-pvtz//RUwb97xd/cc-pvtz
CBH reference scheme: cbh2
""",
)

entry(
    index = 19,
    label = "aNPT2O2H-4O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {10,S}
2  C u0 p0 c0 {3,S} {4,S} {7,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  O u0 p2 c0 {1,S} {8,S}
7  O u0 p2 c0 {2,S} {19,S}
8  O u0 p2 c0 {6,S} {20,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 O u1 p2 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.68556,0.0384364,5.0069e-05,-9.78702e-08,4.32252e-11,-26985.7,-3.7429], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.6176,0.0463436,-2.36868e-05,5.83395e-09,-5.62399e-13,-29454.7,-39.3707], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 2
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/cc-pvtz//RUwb97xd/cc-pvtz
CBH reference scheme: cbh2
""",
)

entry(
    index = 20,
    label = "aNPT2O2H-5O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {7,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  O u0 p2 c0 {1,S} {8,S}
7  O u0 p2 c0 {4,S} {19,S}
8  O u0 p2 c0 {6,S} {20,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 O u1 p2 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.1371,0.0332694,4.28982e-05,-7.77643e-08,3.27725e-11,-25664.5,-14.5271], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.7644,0.0473544,-2.41818e-05,5.94858e-09,-5.72758e-13,-27233.5,-32.789], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 2
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/cc-pvtz//RUwb97xd/cc-pvtz
CBH reference scheme: cbh2
""",
)

entry(
    index = 21,
    label = "aNPT3O2H-1O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {7,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  O u0 p2 c0 {1,S} {8,S}
7  O u0 p2 c0 {4,S} {19,S}
8  O u0 p2 c0 {6,S} {20,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 O u1 p2 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[15.9479,-0.0102417,0.00015728,-1.98775e-07,7.80195e-11,-25457.1,-32.3079], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.0514,0.0485264,-2.4899e-05,6.14388e-09,-5.92702e-13,-26725.8,-28.6319], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 2
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/cc-pvtz//RUwb97xd/cc-pvtz
CBH reference scheme: cbh2
""",
)

entry(
    index = 22,
    label = "aNPT3O2H-2O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
6  O u0 p2 c0 {1,S} {8,S}
7  O u0 p2 c0 {2,S} {19,S}
8  O u0 p2 c0 {6,S} {20,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 O u1 p2 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.39088,0.100502,-0.000102185,5.35483e-08,-1.04607e-11,-25535.5,23.1783], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[16.1009,0.0439531,-2.21214e-05,5.37547e-09,-5.12469e-13,-28605.4,-48.3473], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 2
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/cc-pvtz//RUwb97xd/cc-pvtz
CBH reference scheme: cbh2
""",
)

entry(
    index = 23,
    label = "aIPT1O2H-2O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
6  O u0 p2 c0 {3,S} {8,S}
7  O u0 p2 c0 {1,S} {19,S}
8  O u0 p2 c0 {6,S} {20,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 O u1 p2 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.95266,0.0676135,-3.17949e-05,-9.59926e-09,1.01637e-11,-26267.2,5.48973], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.7312,0.0454508,-2.28789e-05,5.56336e-09,-5.30774e-13,-28588.2,-39.8262], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 2
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/cc-pvtz//RUwb97xd/cc-pvtz
CBH reference scheme: cbh2
""",
)

entry(
    index = 24,
    label = "aIPT1O2H-3O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {10,S}
3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
6  O u0 p2 c0 {3,S} {8,S}
7  O u0 p2 c0 {2,S} {19,S}
8  O u0 p2 c0 {6,S} {20,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 O u1 p2 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.8497,0.0454284,5.08499e-05,-1.12262e-07,5.21386e-11,-25336.8,3.62001], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[16.0967,0.0445271,-2.26258e-05,5.53684e-09,-5.30568e-13,-28557.2,-48.7159], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 2
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/cc-pvtz//RUwb97xd/cc-pvtz
CBH reference scheme: cbh2
""",
)

entry(
    index = 25,
    label = "aIPT1O2H-4O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {6,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {7,S} {12,S} {13,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  O u0 p2 c0 {3,S} {8,S}
7  O u0 p2 c0 {4,S} {19,S}
8  O u0 p2 c0 {6,S} {20,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 O u1 p2 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.22997,0.0351805,7.10532e-05,-1.29564e-07,5.76958e-11,-24108.2,0.309663], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[15.2185,0.0451728,-2.28268e-05,5.56271e-09,-5.31276e-13,-26935.7,-41.5028], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 2
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/cc-pvtz//RUwb97xd/cc-pvtz
CBH reference scheme: cbh2
""",
)

entry(
    index = 26,
    label = "aIPT1O2H-5O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {6,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
5  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
6  O u0 p2 c0 {3,S} {8,S}
7  O u0 p2 c0 {4,S} {19,S}
8  O u0 p2 c0 {6,S} {20,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 O u1 p2 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.81792,0.0302598,7.294e-05,-1.2222e-07,5.23683e-11,-23475.4,-0.806519], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.3888,0.0477156,-2.43494e-05,5.98778e-09,-5.76436e-13,-25807.3,-30.692], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 2
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/cc-pvtz//RUwb97xd/cc-pvtz
CBH reference scheme: cbh2
""",
)

entry(
    index = 27,
    label = "aIPT2O2H-1O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
6  O u0 p2 c0 {1,S} {8,S}
7  O u0 p2 c0 {3,S} {19,S}
8  O u0 p2 c0 {6,S} {20,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 O u1 p2 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.07888,0.044482,4.39391e-05,-9.87783e-08,4.52955e-11,-26443.1,-3.26085], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[17.3919,0.042075,-2.10701e-05,5.10665e-09,-4.86202e-13,-29697.8,-55.8642], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 2
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/cc-pvtz//RUwb97xd/cc-pvtz
CBH reference scheme: cbh2
""",
)

entry(
    index = 28,
    label = "aIPT2O2H-3O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {9,S}
3  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
6  O u0 p2 c0 {1,S} {8,S}
7  O u0 p2 c0 {2,S} {19,S}
8  O u0 p2 c0 {6,S} {20,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 O u1 p2 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.96558,0.0564387,2.66078e-05,-9.08983e-08,4.51439e-11,-28255.8,3.87681], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[18.6061,0.0403273,-2.00475e-05,4.82924e-09,-4.57436e-13,-32100.5,-64.5109], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 2
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/cc-pvtz//RUwb97xd/cc-pvtz
CBH reference scheme: cbh2
""",
)

entry(
    index = 29,
    label = "aIPT2O2H-4O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  O u0 p2 c0 {1,S} {8,S}
7  O u0 p2 c0 {3,S} {19,S}
8  O u0 p2 c0 {6,S} {20,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 O u1 p2 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.32311,0.0452429,2.99263e-05,-7.60236e-08,3.50633e-11,-27195.7,-3.9108], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.9491,0.0455927,-2.31267e-05,5.65983e-09,-5.4283e-13,-29611.9,-41.8309], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 2
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/cc-pvtz//RUwb97xd/cc-pvtz
CBH reference scheme: cbh2
""",
)

entry(
    index = 30,
    label = "aIPT3O2H-1O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {10,S}
3  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
6  O u0 p2 c0 {2,S} {8,S}
7  O u0 p2 c0 {3,S} {19,S}
8  O u0 p2 c0 {6,S} {20,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 O u1 p2 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.64524,0.0367346,5.6045e-05,-1.05665e-07,4.66304e-11,-25392.1,-3.23898], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.4334,0.0462713,-2.35322e-05,5.77273e-09,-5.54723e-13,-27845.2,-38.3201], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 2
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/cc-pvtz//RUwb97xd/cc-pvtz
CBH reference scheme: cbh2
""",
)

entry(
    index = 31,
    label = "aIPT3O2H-2O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {9,S}
3  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
6  O u0 p2 c0 {2,S} {8,S}
7  O u0 p2 c0 {1,S} {19,S}
8  O u0 p2 c0 {6,S} {20,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 O u1 p2 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.01479,0.0577763,-2.00888e-06,-4.37182e-08,2.34911e-11,-28108.4,-0.304493], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[15.389,0.0447716,-2.25803e-05,5.5003e-09,-5.25525e-13,-30624.4,-45.2632], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 2
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/cc-pvtz//RUwb97xd/cc-pvtz
CBH reference scheme: cbh2
""",
)

entry(
    index = 32,
    label = "aIPT3O2H-4O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {10,S}
3  C u0 p0 c0 {2,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  O u0 p2 c0 {2,S} {8,S}
7  O u0 p2 c0 {3,S} {19,S}
8  O u0 p2 c0 {6,S} {20,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 O u1 p2 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.1865,0.0309353,6.57247e-05,-1.12782e-07,4.85284e-11,-24734.5,-11.2334], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.7662,0.0460493,-2.34016e-05,5.72812e-09,-5.49043e-13,-26974.5,-40.6539], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 2
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/cc-pvtz//RUwb97xd/cc-pvtz
CBH reference scheme: cbh2
""",
)

entry(
    index = 33,
    label = "aIPT4O2H-3O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {10,S}
3  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  O u0 p2 c0 {3,S} {8,S}
7  O u0 p2 c0 {2,S} {19,S}
8  O u0 p2 c0 {6,S} {20,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 O u1 p2 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.49132,0.0621218,-4.03391e-06,-5.00597e-08,2.82861e-11,-24848.3,2.23324], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[17.0121,0.0422498,-2.10551e-05,5.08053e-09,-4.81763e-13,-27790.8,-53.2472], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 2
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/cc-pvtz//RUwb97xd/cc-pvtz
CBH reference scheme: cbh2
""",
)

entry(
    index = 34,
    label = "aIPT4O2H-2O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  O u0 p2 c0 {3,S} {8,S}
7  O u0 p2 c0 {1,S} {19,S}
8  O u0 p2 c0 {6,S} {20,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 O u1 p2 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.73773,0.0602192,-6.79301e-07,-4.92293e-08,2.6533e-11,-27118.3,7.51477], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.7797,0.0459313,-2.32638e-05,5.67692e-09,-5.42763e-13,-29799.5,-40.8977], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 2
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/cc-pvtz//RUwb97xd/cc-pvtz
CBH reference scheme: cbh2
""",
)

entry(
    index = 35,
    label = "aIPT4O2H-1O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {6,S} {12,S} {13,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  O u0 p2 c0 {4,S} {8,S}
7  O u0 p2 c0 {3,S} {19,S}
8  O u0 p2 c0 {6,S} {20,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 O u1 p2 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.94107,0.0288784,7.26638e-05,-1.20052e-07,5.11422e-11,-24009.2,-7.6855], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.9581,0.047635,-2.44841e-05,6.04845e-09,-5.84032e-13,-26201.8,-34.7191], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 2
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/cc-pvtz//RUwb97xd/cc-pvtz
CBH reference scheme: cbh2
""",
)

entry(
    index = 36,
    label = "aNEOPTO2H-3O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {7,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  O u0 p2 c0 {2,S} {8,S}
7  O u0 p2 c0 {3,S} {19,S}
8  O u0 p2 c0 {6,S} {20,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 O u1 p2 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.55731,0.0283897,8.26491e-05,-1.3649e-07,5.86523e-11,-25314.6,-8.02869], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[15.2945,0.0455162,-2.3204e-05,5.70003e-09,-5.48249e-13,-28038.1,-44.4566], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 2
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/cc-pvtz//RUwb97xd/cc-pvtz
CBH reference scheme: cbh2
""",
)

entry(
    index = 37,
    label = "aNHX1O2H-2O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {4,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {6,S} {11,S} {12,S}
5  C u0 p0 c0 {1,S} {7,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {5,S} {9,S}
8  O u0 p2 c0 {1,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.32783,0.0907784,-6.21227e-05,1.0377e-08,5.26126e-12,-27001.3,15.5309], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[16.4308,0.0529116,-2.65499e-05,6.44311e-09,-6.13862e-13,-29870,-45.2132], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 38,
    label = "aNHX1O2H-3O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {5,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
5  C u0 p0 c0 {3,S} {7,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {5,S} {9,S}
8  O u0 p2 c0 {1,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.0368,0.0184754,0.000139484,-2.05575e-07,8.57858e-11,-28508.9,-7.97143], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[15.3433,0.0565078,-2.91665e-05,7.22028e-09,-6.97965e-13,-31516.8,-40.7374], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 39,
    label = "aNHX1O2H-4O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {5,S} {15,S} {16,S}
5  C u0 p0 c0 {4,S} {7,S} {17,S} {18,S}
6  C u0 p0 c0 {3,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {5,S} {9,S}
8  O u0 p2 c0 {1,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.20542,0.0425208,8.15916e-05,-1.5107e-07,6.74124e-11,-28312,-4.05333], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[18.2547,0.0519619,-2.63886e-05,6.45002e-09,-6.17284e-13,-31862.4,-57.5136], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 40,
    label = "aNHX1O2H-5O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {5,S} {15,S} {16,S}
5  C u0 p0 c0 {4,S} {7,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {5,S} {9,S}
8  O u0 p2 c0 {1,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.4913,0.0394524,8.48539e-05,-1.48148e-07,6.44155e-11,-28038.6,3.09819], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[15.6199,0.055585,-2.84775e-05,7.01319e-09,-6.75468e-13,-31228.5,-41.0591], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 41,
    label = "aNHX1O2H-6O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {4,S} {14,S} {15,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {6,S} {16,S} {17,S}
5  C u0 p0 c0 {3,S} {7,S} {18,S} {19,S}
6  C u0 p0 c0 {4,S} {8,S} {20,S} {21,S}
7  O u0 p2 c0 {5,S} {9,S}
8  O u0 p2 c0 {6,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.93479,0.0256068,0.000119134,-1.83293e-07,7.74411e-11,-26172.9,-1.53939], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.4588,0.0571842,-2.93578e-05,7.23582e-09,-6.96971e-13,-28992.8,-34.0966], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 42,
    label = "aNHX2O2H-1O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {7,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {4,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {6,S} {11,S} {12,S}
5  C u0 p0 c0 {1,S} {8,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {1,S} {9,S}
8  O u0 p2 c0 {5,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.8345,0.0378746,6.3369e-05,-1.12819e-07,4.86209e-11,-27447.6,-16.2117], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[16.2769,0.05393,-2.73924e-05,6.70968e-09,-6.43814e-13,-29693,-45.0998], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 43,
    label = "aNHX2O2H-3O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {10,S}
3  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {2,S} {9,S}
8  O u0 p2 c0 {1,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.96458,0.0469104,6.23226e-05,-1.28782e-07,5.89648e-11,-29551.4,-10.69], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[19.6856,0.0485219,-2.40653e-05,5.78445e-09,-5.46784e-13,-33021.7,-66.236], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 44,
    label = "aNHX2O2H-4O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {8,S} {11,S}
2  C u0 p0 c0 {3,S} {5,S} {7,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {2,S} {9,S}
8  O u0 p2 c0 {1,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.73296,0.0684863,1.97514e-05,-8.93028e-08,4.53406e-11,-29801.7,15.5213], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[17.2119,0.0524261,-2.6465e-05,6.45243e-09,-6.16964e-13,-33592.4,-51.9408], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 45,
    label = "aNHX2O2H-5O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {7,S} {10,S}
2  C u0 p0 c0 {4,S} {6,S} {8,S} {11,S}
3  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {3,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {1,S} {9,S}
8  O u0 p2 c0 {2,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.92029,0.0543346,4.21215e-05,-1.01567e-07,4.66699e-11,-30428.6,0.133876], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[17.052,0.054005,-2.77871e-05,6.87418e-09,-6.64805e-13,-33736.1,-51.9755], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 46,
    label = "aNHX2O2H-6O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {5,S} {15,S} {16,S}
5  C u0 p0 c0 {4,S} {8,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {1,S} {9,S}
8  O u0 p2 c0 {5,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.3345,0.00847238,0.000146049,-2.02611e-07,8.26291e-11,-28673.8,-23.745], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[15.3944,0.0555745,-2.84074e-05,6.98444e-09,-6.71701e-13,-30871.2,-39.9798], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 47,
    label = "aNHX3O2H-1O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {5,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
5  C u0 p0 c0 {3,S} {8,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {1,S} {9,S}
8  O u0 p2 c0 {5,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.95162,0.0702671,1.41329e-05,-8.2142e-08,4.20318e-11,-27754.6,6.93077], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[19.0953,0.0519944,-2.68664e-05,6.66355e-09,-6.45509e-13,-31761.5,-64.0231], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 48,
    label = "aNHX3O2H-2O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {10,S}
3  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {1,S} {9,S}
8  O u0 p2 c0 {2,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.30055,0.0515127,6.13906e-05,-1.30007e-07,5.90269e-11,-29096.9,-3.75818], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[20.1436,0.0499601,-2.55815e-05,6.31116e-09,-6.09458e-13,-33325.2,-71.0583], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 49,
    label = "aNHX3O2H-4O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {11,S}
3  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {1,S} {9,S}
8  O u0 p2 c0 {2,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.33405,0.0594834,2.44542e-05,-8.11992e-08,3.88799e-11,-28305.5,2.75217], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[16.4682,0.0537947,-2.73887e-05,6.72482e-09,-6.46654e-13,-31390,-48.1606], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 50,
    label = "aNHX3O2H-5O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {7,S} {10,S}
2  C u0 p0 c0 {3,S} {5,S} {8,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
5  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {4,S} {16,S} {17,S} {18,S}
7  O u0 p2 c0 {1,S} {9,S}
8  O u0 p2 c0 {2,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.5563,0.0659883,2.16641e-05,-8.80872e-08,4.39601e-11,-29830.3,11.2928], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[17.5139,0.0520482,-2.62763e-05,6.40879e-09,-6.13077e-13,-33547.2,-53.7527], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 51,
    label = "aNHX3O2H-6O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {5,S} {15,S} {16,S}
5  C u0 p0 c0 {4,S} {8,S} {17,S} {18,S}
6  C u0 p0 c0 {3,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {1,S} {9,S}
8  O u0 p2 c0 {5,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.98171,0.0440903,5.24902e-05,-1.04037e-07,4.60349e-11,-28117.3,-6.4785], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[15.2488,0.0550666,-2.79339e-05,6.83363e-09,-6.54957e-13,-30444.1,-38.9106], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 52,
    label = "a2MPT1O2H-2O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
7  O u0 p2 c0 {4,S} {9,S}
8  O u0 p2 c0 {1,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.79142,0.0662177,-3.64113e-08,-5.52443e-08,2.97355e-11,-29644.3,-8.43012], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[18.6031,0.0507215,-2.54278e-05,6.15073e-09,-5.83693e-13,-32529.1,-60.9003], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 53,
    label = "a2MPT1O2H-3O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {11,S}
3  C u0 p0 c0 {2,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
7  O u0 p2 c0 {4,S} {9,S}
8  O u0 p2 c0 {2,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.84557,0.0693091,4.98335e-06,-6.66383e-08,3.53448e-11,-28225.3,9.14846], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[16.7294,0.0528952,-2.66432e-05,6.48168e-09,-6.18535e-13,-31447.3,-49.1896], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 54,
    label = "a2MPT1O2H-4O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {10,S}
2  C u0 p0 c0 {3,S} {6,S} {8,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
7  O u0 p2 c0 {4,S} {9,S}
8  O u0 p2 c0 {2,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.04521,0.0549766,4.06224e-05,-1.00995e-07,4.70869e-11,-28805.1,6.02823], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[15.4655,0.0551069,-2.80592e-05,6.88402e-09,-6.61296e-13,-31816.8,-41.9492], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 55,
    label = "a2MPT1O2H-5O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {5,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {7,S} {17,S} {18,S}
5  C u0 p0 c0 {3,S} {8,S} {15,S} {16,S}
6  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {4,S} {9,S}
8  O u0 p2 c0 {5,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.37282,0.0393152,8.77907e-05,-1.568e-07,6.96037e-11,-27288.2,-3.64133], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[17.1053,0.0531907,-2.69641e-05,6.57902e-09,-6.2857e-13,-30505.1,-50.4549], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 56,
    label = "a2MPT1O2H-6O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {7,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {8,S} {15,S} {16,S}
6  C u0 p0 c0 {3,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {4,S} {9,S}
8  O u0 p2 c0 {5,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.87475,0.0575351,2.73457e-05,-8.44954e-08,4.04977e-11,-26676.7,1.67108], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[16.4078,0.0533126,-2.6885e-05,6.54791e-09,-6.25478e-13,-29557.8,-46.0024], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 57,
    label = "a2MPT2O2H-1O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {8,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {3,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {1,S} {9,S}
8  O u0 p2 c0 {4,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.28005,0.0730199,1.3223e-05,-8.55126e-08,4.45657e-11,-28760.5,15.5548], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[18.2325,0.0516888,-2.60861e-05,6.34634e-09,-6.05461e-13,-32874.8,-59.1665], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 58,
    label = "aMPT2O2H-3O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {10,S}
3  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {3,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {1,S} {9,S}
8  O u0 p2 c0 {2,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.45339,0.0648749,6.02058e-06,-6.11053e-08,3.16012e-11,-30820.3,-0.346721], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[16.7829,0.0527696,-2.65418e-05,6.44885e-09,-6.14766e-13,-33688.4,-50.8703], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 59,
    label = "a2MPT2O2H-4O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {3,S} {6,S} {8,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {1,S} {9,S}
8  O u0 p2 c0 {2,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.40596,0.0694892,-6.15036e-06,-4.44929e-08,2.36777e-11,-32463.3,-2.62676], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[17.4563,0.0545018,-2.84509e-05,7.11654e-09,-6.9402e-13,-35614.4,-57.0243], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 60,
    label = "a2MPT2O2H-5O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {8,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {1,S} {9,S}
8  O u0 p2 c0 {4,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.16209,0.0512458,4.80439e-05,-1.08787e-07,4.98517e-11,-30786.7,-7.70585], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[18.4966,0.0512785,-2.60177e-05,6.36994e-09,-6.11155e-13,-34147.1,-60.9582], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 61,
    label = "a2MPT3O2H-1O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {11,S}
3  C u0 p0 c0 {2,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {8,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {3,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {2,S} {9,S}
8  O u0 p2 c0 {4,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.38075,0.0484987,4.99764e-05,-1.04917e-07,4.68565e-11,-28019.9,-0.261904], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[15.1713,0.0559375,-2.87283e-05,7.10134e-09,-6.8648e-13,-30790.9,-40.7092], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 62,
    label = "a2MPT3O2H-2O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {10,S}
3  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {3,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {2,S} {9,S}
8  O u0 p2 c0 {1,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.0564214,0.126404,-0.000131863,6.44587e-08,-9.6166e-12,-30665.7,27.3072], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[20.7451,0.0462407,-2.24756e-05,5.3119e-09,-4.95207e-13,-34885.6,-73.4799], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 63,
    label = "a2MPT3O2H-5O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {8,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {2,S} {9,S}
8  O u0 p2 c0 {4,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.33063,0.0956504,-7.118e-05,1.83765e-08,2.56977e-12,-27865.8,18.1715], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[16.1778,0.0536921,-2.709e-05,6.59737e-09,-6.30051e-13,-30845.8,-45.934], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 64,
    label = "a2MPT4O2H-1O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {10,S}
2  C u0 p0 c0 {3,S} {6,S} {7,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {8,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
7  O u0 p2 c0 {2,S} {9,S}
8  O u0 p2 c0 {4,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.2644,0.047299,5.97631e-05,-1.18494e-07,5.26882e-11,-28203.7,7.46965], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.141,0.0571447,-2.9291e-05,7.22285e-09,-6.96577e-13,-31070.6,-33.91], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 65,
    label = "a2MPT4O2H-2O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {3,S} {6,S} {7,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {2,S} {9,S}
8  O u0 p2 c0 {1,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.57408,0.0814871,-3.21607e-05,-2.21468e-08,1.69797e-11,-32191.7,5.37849], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[17.4432,0.0538433,-2.77573e-05,6.86784e-09,-6.63753e-13,-35431.7,-56.4294], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 66,
    label = "a2MPT4O2H-3O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {11,S}
3  C u0 p0 c0 {2,S} {6,S} {7,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {3,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {3,S} {9,S}
8  O u0 p2 c0 {2,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.05736,0.0651463,1.81719e-05,-8.06134e-08,4.00008e-11,-29295.2,-0.148913], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[19.0498,0.0509431,-2.60248e-05,6.41393e-09,-6.19049e-13,-33086.7,-65.5421], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 67,
    label = "a2MPT4O2H-5O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {10,S}
2  C u0 p0 c0 {3,S} {4,S} {7,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {8,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {2,S} {9,S}
8  O u0 p2 c0 {4,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.92522,0.0404091,6.36483e-05,-1.15059e-07,4.97097e-11,-27804.5,-6.80229], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.6113,0.0564867,-2.88901e-05,7.10916e-09,-6.84355e-13,-30146.7,-37.1056], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 68,
    label = "a2MPT5O2H-1O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {5,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {8,S} {17,S} {18,S}
5  C u0 p0 c0 {3,S} {7,S} {15,S} {16,S}
6  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {5,S} {9,S}
8  O u0 p2 c0 {4,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.51873,0.039096,7.23977e-05,-1.27594e-07,5.51927e-11,-27143.2,-2.27301], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.6841,0.0562856,-2.87457e-05,7.06636e-09,-6.7972e-13,-29679.6,-35.4911], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 69,
    label = "a2MPT5O2H-2O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {7,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {4,S} {9,S}
8  O u0 p2 c0 {1,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.92631,0.0646479,-1.09685e-05,-3.18149e-08,1.78769e-11,-30989.9,-7.1059], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[15.9338,0.0539173,-2.71563e-05,6.60249e-09,-6.29637e-13,-33139.2,-44.8668], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 70,
    label = "a2MPT5O2H-3O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {7,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {4,S} {9,S}
8  O u0 p2 c0 {2,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.85332,0.0271727,0.000127726,-1.9927e-07,8.47271e-11,-28771.1,0.860074], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[15.9303,0.0554618,-2.85713e-05,7.0722e-09,-6.84111e-13,-32396.9,-45.5942], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 71,
    label = "a2MPT5O2H-4O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {10,S}
2  C u0 p0 c0 {3,S} {4,S} {8,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {7,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {4,S} {9,S}
8  O u0 p2 c0 {2,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.04022,0.0530394,6.99329e-05,-1.50994e-07,7.0784e-11,-28064.8,3.41173], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[19.3189,0.0500756,-2.50653e-05,6.04544e-09,-5.71949e-13,-32184.2,-65.4511], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 72,
    label = "a3MPT1O2H-2O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {11,S}
3  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {7,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
7  O u0 p2 c0 {4,S} {9,S}
8  O u0 p2 c0 {2,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.04539,0.0701304,-1.29159e-05,-3.7616e-08,2.2026e-11,-27271.2,2.73807], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[16.0019,0.0538792,-2.72131e-05,6.63655e-09,-6.34651e-13,-29867.4,-44.8173], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 73,
    label = "a3MPT1O2H-3O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {7,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
7  O u0 p2 c0 {4,S} {9,S}
8  O u0 p2 c0 {1,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.35707,0.0985484,-7.23515e-05,1.58685e-08,4.11819e-12,-29994.7,15.7454], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[18.3535,0.0515282,-2.61111e-05,6.38131e-09,-6.11237e-13,-33576.8,-59.6018], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 74,
    label = "a3MPT1O2H-4O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {10,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {11,S}
3  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {7,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
7  O u0 p2 c0 {4,S} {9,S}
8  O u0 p2 c0 {2,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.20683,0.0376568,0.000107813,-1.84791e-07,8.09736e-11,-28617.3,0.478553], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[18.6857,0.0516698,-2.6335e-05,6.45936e-09,-6.20215e-13,-32880.4,-62.1975], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 75,
    label = "a3MPT1O2H-5O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {4,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {7,S} {17,S} {18,S}
5  C u0 p0 c0 {2,S} {8,S} {15,S} {16,S}
6  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {4,S} {9,S}
8  O u0 p2 c0 {5,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[13.6461,0.00937878,0.000138307,-1.89535e-07,7.64856e-11,-26972.6,-18.9901], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.3592,0.0579809,-2.96482e-05,7.29132e-09,-7.01337e-13,-28771.1,-27.9451], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 76,
    label = "a3MPT1O2H-6O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {8,S} {15,S} {16,S}
5  C u0 p0 c0 {2,S} {7,S} {17,S} {18,S}
6  C u0 p0 c0 {3,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {5,S} {9,S}
8  O u0 p2 c0 {4,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.4602,0.00608411,0.000141762,-1.89049e-07,7.51485e-11,-26896.5,-23.0712], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.9802,0.0590689,-3.0449e-05,7.53408e-09,-7.28105e-13,-28475.6,-26.2854], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 77,
    label = "a3MPT2O2H-1O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {11,S}
3  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {8,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
7  O u0 p2 c0 {2,S} {9,S}
8  O u0 p2 c0 {4,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.60414,0.0352488,0.000148291,-2.49314e-07,1.09762e-10,-27895,-0.520123], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[24.8158,0.0444429,-2.27305e-05,5.60521e-09,-5.41308e-13,-34365.6,-100.494], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 78,
    label = "a3MPT2O2H-3O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {10,S}
3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
6  C u0 p0 c0 {3,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {2,S} {9,S}
8  O u0 p2 c0 {1,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.71696,0.108963,-9.42797e-05,3.50234e-08,-1.90574e-12,-30298.1,20.816], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[18.531,0.0509865,-2.562e-05,6.21194e-09,-5.90989e-13,-34070.2,-62.4088], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 79,
    label = "a3MPT2O2H-4O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {11,S}
3  C u0 p0 c0 {1,S} {6,S} {8,S} {12,S}
4  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
6  C u0 p0 c0 {3,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {2,S} {9,S}
8  O u0 p2 c0 {3,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.3585,0.0377364,8.10525e-05,-1.39585e-07,6.007e-11,-30338.7,-12.3931], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[16.6712,0.0551824,-2.86682e-05,7.14081e-09,-6.93948e-13,-33329.5,-52.3031], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 80,
    label = "a3MPT2O2H-5O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {10,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {11,S}
3  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {8,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
7  O u0 p2 c0 {2,S} {9,S}
8  O u0 p2 c0 {4,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.72976,0.0282027,0.000120164,-1.88175e-07,7.97397e-11,-28065.4,-5.69995], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[16.5013,0.0554699,-2.87649e-05,7.14876e-09,-6.93347e-13,-31571.8,-50.2786], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 81,
    label = "a3MPT2O2H-6O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {11,S}
3  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {8,S} {14,S} {15,S}
5  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {3,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {2,S} {9,S}
8  O u0 p2 c0 {4,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.29569,0.0540254,5.17502e-05,-1.19998e-07,5.60841e-11,-28105.2,3.34901], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[17.4707,0.0522214,-2.63284e-05,6.4044e-09,-6.10814e-13,-31613.7,-54.0547], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 82,
    label = "a3MPT3O2H-1O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {8,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
7  O u0 p2 c0 {1,S} {9,S}
8  O u0 p2 c0 {4,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.07716,0.0484881,6.35397e-05,-1.27778e-07,5.7244e-11,-29558.7,-0.563491], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[17.4835,0.0534119,-2.74573e-05,6.78912e-09,-6.56375e-13,-33156.3,-55.3461], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 83,
    label = "a3MPT3O2H-2O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {10,S}
3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
6  C u0 p0 c0 {3,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {1,S} {9,S}
8  O u0 p2 c0 {2,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.00465,0.0420183,8.86521e-05,-1.60542e-07,7.07333e-11,-30904.6,-6.90546], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[21.0179,0.0473094,-2.36473e-05,5.73229e-09,-5.46371e-13,-35443,-76.6363], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 84,
    label = "a3MPT3O2H-6O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {8,S} {14,S} {15,S}
5  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {3,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {1,S} {9,S}
8  O u0 p2 c0 {4,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.96744,0.0894677,-2.07578e-05,-6.01277e-08,3.82418e-11,-28681.6,17.39], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[21.2926,0.046263,-2.2628e-05,5.36474e-09,-5.00943e-13,-33405.6,-77.2009], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 85,
    label = "a3MPT6O2H-1O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {7,S} {15,S} {16,S}
5  C u0 p0 c0 {2,S} {8,S} {17,S} {18,S}
6  C u0 p0 c0 {3,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {4,S} {9,S}
8  O u0 p2 c0 {5,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.942,0.00136492,0.000199451,-2.7733e-07,1.13913e-10,-26111.8,-10.4236], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[18.8964,0.0501163,-2.52395e-05,6.15655e-09,-5.89754e-13,-30516.4,-60.7396], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 86,
    label = "a3MPT6O2H-2O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {11,S}
3  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
5  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {3,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {4,S} {9,S}
8  O u0 p2 c0 {2,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[13.1129,0.0207049,0.00011017,-1.62144e-07,6.68853e-11,-28520.7,-21.1449], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[15.1885,0.0556322,-2.84e-05,6.97978e-09,-6.71262e-13,-30639.5,-40.6105], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 87,
    label = "a3MPT6O2H-3O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
5  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {3,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {4,S} {9,S}
8  O u0 p2 c0 {1,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.29278,0.0612576,1.71581e-05,-7.23215e-08,3.51455e-11,-29072,-5.23676], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[18.2525,0.0517152,-2.62394e-05,6.41968e-09,-6.15461e-13,-32327.8,-60.1015], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 3
vib model: harm
tors model: 1dhr
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 88,
    label = "aNHPT1O2H-2O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {9,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {18,S} {19,S}
3  C u0 p0 c0 {4,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {3,S} {16,S} {17,S}
5  C u0 p0 c0 {3,S} {7,S} {12,S} {13,S}
6  C u0 p0 c0 {1,S} {8,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {22,S} {23,S} {24,S}
8  O u0 p2 c0 {6,S} {10,S}
9  O u0 p2 c0 {1,S} {25,S}
10 O u0 p2 c0 {8,S} {26,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 O u1 p2 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.128,0.0441484,0.000103882,-1.82725e-07,8.06449e-11,-30452.1,-5.83054], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[18.6913,0.0622822,-3.20452e-05,7.91411e-09,-7.63544e-13,-34151.2,-58.3482], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 89,
    label = "aNHPT1O2H-3O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {9,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {6,S} {18,S} {19,S}
5  C u0 p0 c0 {3,S} {7,S} {12,S} {13,S}
6  C u0 p0 c0 {4,S} {8,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {22,S} {23,S} {24,S}
8  O u0 p2 c0 {6,S} {10,S}
9  O u0 p2 c0 {1,S} {25,S}
10 O u0 p2 c0 {8,S} {26,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 O u1 p2 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.6416,0.0291665,0.000161308,-2.54932e-07,1.10394e-10,-31011,-7.62248], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[19.9292,0.0605675,-3.06606e-05,7.45154e-09,-7.09227e-13,-35384.9,-66.8812], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 90,
    label = "aNHPT1O2H-4O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {9,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {14,S} {15,S}
3  C u0 p0 c0 {1,S} {4,S} {16,S} {17,S}
4  C u0 p0 c0 {3,S} {6,S} {18,S} {19,S}
5  C u0 p0 c0 {2,S} {7,S} {12,S} {13,S}
6  C u0 p0 c0 {4,S} {8,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {22,S} {23,S} {24,S}
8  O u0 p2 c0 {6,S} {10,S}
9  O u0 p2 c0 {1,S} {25,S}
10 O u0 p2 c0 {8,S} {26,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 O u1 p2 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.9731,0.05105,8.91606e-05,-1.70439e-07,7.67793e-11,-31799.3,-7.64369], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[21.3133,0.0580169,-2.92291e-05,7.09967e-09,-6.76426e-13,-36053.1,-73.5664], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 91,
    label = "aNHPT1O2H-5O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {9,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {5,S} {16,S} {17,S}
4  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {6,S} {18,S} {19,S}
6  C u0 p0 c0 {5,S} {8,S} {20,S} {21,S}
7  C u0 p0 c0 {4,S} {22,S} {23,S} {24,S}
8  O u0 p2 c0 {6,S} {10,S}
9  O u0 p2 c0 {1,S} {25,S}
10 O u0 p2 c0 {8,S} {26,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 O u1 p2 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[15.9048,0.0138622,0.000150844,-2.10661e-07,8.55992e-11,-31855.2,-30.4516], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[16.6252,0.0648461,-3.33629e-05,8.23504e-09,-7.94015e-13,-34110.6,-45.6757], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 92,
    label = "aNHPT1O2H-6O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {9,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {4,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {5,S} {16,S} {17,S}
5  C u0 p0 c0 {4,S} {6,S} {18,S} {19,S}
6  C u0 p0 c0 {5,S} {8,S} {20,S} {21,S}
7  C u0 p0 c0 {1,S} {22,S} {23,S} {24,S}
8  O u0 p2 c0 {6,S} {10,S}
9  O u0 p2 c0 {1,S} {25,S}
10 O u0 p2 c0 {8,S} {26,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 O u1 p2 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.0395,0.0330279,0.000110411,-1.71375e-07,7.14322e-11,-31363.7,-11.9681], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[15.6736,0.0666156,-3.44728e-05,8.54547e-09,-8.26762e-13,-34025.6,-40.1266], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 93,
    label = "aNHPT1O2H-7O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {5,S} {17,S} {18,S}
4  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
5  C u0 p0 c0 {3,S} {7,S} {19,S} {20,S}
6  C u0 p0 c0 {4,S} {8,S} {21,S} {22,S}
7  C u0 p0 c0 {5,S} {9,S} {23,S} {24,S}
8  O u0 p2 c0 {6,S} {10,S}
9  O u0 p2 c0 {7,S} {25,S}
10 O u0 p2 c0 {8,S} {26,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 O u1 p2 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[17.337,-0.00493133,0.000203352,-2.67265e-07,1.06917e-10,-30084.7,-32.8995], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[15.8434,0.0659424,-3.39474e-05,8.37888e-09,-8.0768e-13,-32294.2,-39.756], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 94,
    label = "aNHPT2O2H-1O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {8,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {18,S} {19,S}
3  C u0 p0 c0 {4,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {3,S} {16,S} {17,S}
5  C u0 p0 c0 {3,S} {7,S} {12,S} {13,S}
6  C u0 p0 c0 {1,S} {9,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {22,S} {23,S} {24,S}
8  O u0 p2 c0 {1,S} {10,S}
9  O u0 p2 c0 {6,S} {25,S}
10 O u0 p2 c0 {8,S} {26,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 O u1 p2 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.3999,0.0640495,5.79905e-05,-1.29792e-07,5.84725e-11,-29379.3,8.97967], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[16.7719,0.06867,-3.67265e-05,9.32249e-09,-9.18044e-13,-33389.9,-51.454], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 95,
    label = "aNHPT2O2H-3O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {9,S} {12,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {11,S}
3  C u0 p0 c0 {1,S} {4,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {5,S} {15,S} {16,S}
5  C u0 p0 c0 {4,S} {7,S} {17,S} {18,S}
6  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {22,S} {23,S} {24,S}
8  O u0 p2 c0 {2,S} {10,S}
9  O u0 p2 c0 {1,S} {25,S}
10 O u0 p2 c0 {8,S} {26,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 O u1 p2 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.33882,0.0698275,3.03275e-05,-9.95351e-08,4.80475e-11,-31738.9,3.00706], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[17.871,0.0636575,-3.2872e-05,8.13547e-09,-7.85909e-13,-35270.6,-55.6587], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 96,
    label = "aNHPT2O2H-4O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {9,S} {12,S}
2  C u0 p0 c0 {3,S} {6,S} {8,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {5,S} {15,S} {16,S}
5  C u0 p0 c0 {4,S} {7,S} {17,S} {18,S}
6  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {22,S} {23,S} {24,S}
8  O u0 p2 c0 {2,S} {10,S}
9  O u0 p2 c0 {1,S} {25,S}
10 O u0 p2 c0 {8,S} {26,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 O u1 p2 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.3676,0.0441839,8.8233e-05,-1.51942e-07,6.50795e-11,-32712.7,-7.4421], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[15.9332,0.0673286,-3.53333e-05,8.85765e-09,-8.64464e-13,-35673,-44.3634], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 97,
    label = "aNHPT2O2H-5O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {9,S} {12,S}
2  C u0 p0 c0 {3,S} {6,S} {8,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {7,S} {17,S} {18,S}
6  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {22,S} {23,S} {24,S}
8  O u0 p2 c0 {2,S} {10,S}
9  O u0 p2 c0 {1,S} {25,S}
10 O u0 p2 c0 {8,S} {26,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 O u1 p2 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.4089,0.0327002,0.000129349,-2.01868e-07,8.5185e-11,-32307,-5.34915], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[16.4313,0.0657775,-3.40688e-05,8.45318e-09,-8.18603e-13,-35775.3,-46.9256], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 98,
    label = "aNHPT2O2H-6O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {8,S} {11,S}
2  C u0 p0 c0 {4,S} {7,S} {9,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {5,S} {17,S} {18,S}
5  C u0 p0 c0 {3,S} {4,S} {15,S} {16,S}
6  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {2,S} {22,S} {23,S} {24,S}
8  O u0 p2 c0 {1,S} {10,S}
9  O u0 p2 c0 {2,S} {25,S}
10 O u0 p2 c0 {8,S} {26,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 O u1 p2 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.10717,0.0645509,4.07899e-05,-1.06221e-07,4.90314e-11,-32737.2,0.0117319], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[17.8538,0.0642959,-3.33926e-05,8.307e-09,-8.0609e-13,-36293.4,-55.6858], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 99,
    label = "aNHPT2O2H-7O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {4,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {5,S} {16,S} {17,S}
5  C u0 p0 c0 {4,S} {6,S} {18,S} {19,S}
6  C u0 p0 c0 {5,S} {9,S} {20,S} {21,S}
7  C u0 p0 c0 {1,S} {22,S} {23,S} {24,S}
8  O u0 p2 c0 {1,S} {10,S}
9  O u0 p2 c0 {6,S} {25,S}
10 O u0 p2 c0 {8,S} {26,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 O u1 p2 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[16.2305,-0.000134706,0.000197208,-2.65315e-07,1.07368e-10,-31573.1,-28.4885], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[16.2458,0.0651471,-3.35136e-05,8.27536e-09,-7.98235e-13,-34086.5,-42.6708], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 100,
    label = "aNHPT3O2H-1O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {8,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {6,S} {18,S} {19,S}
5  C u0 p0 c0 {3,S} {7,S} {12,S} {13,S}
6  C u0 p0 c0 {4,S} {9,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {22,S} {23,S} {24,S}
8  O u0 p2 c0 {1,S} {10,S}
9  O u0 p2 c0 {6,S} {25,S}
10 O u0 p2 c0 {8,S} {26,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 O u1 p2 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.09123,0.0564591,7.35483e-05,-1.48142e-07,6.63418e-11,-31549.6,-4.80614], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[19.4261,0.0638376,-3.35382e-05,8.38905e-09,-8.16309e-13,-35579.4,-65.4195], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 101,
    label = "aNHPT3O2H-2O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {12,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {11,S}
3  C u0 p0 c0 {1,S} {4,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {5,S} {15,S} {16,S}
5  C u0 p0 c0 {4,S} {7,S} {17,S} {18,S}
6  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {22,S} {23,S} {24,S}
8  O u0 p2 c0 {1,S} {10,S}
9  O u0 p2 c0 {2,S} {25,S}
10 O u0 p2 c0 {8,S} {26,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 O u1 p2 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.4318,0.0427568,9.93753e-05,-1.63788e-07,6.86168e-11,-32313.4,-10.748], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[16.1962,0.0711661,-3.91052e-05,1.01528e-08,-1.01768e-12,-35680.8,-50.3081], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 102,
    label = "aNHPT3O2H-4O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {8,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {12,S}
3  C u0 p0 c0 {2,S} {5,S} {15,S} {16,S}
4  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {7,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {22,S} {23,S} {24,S}
8  O u0 p2 c0 {1,S} {10,S}
9  O u0 p2 c0 {2,S} {25,S}
10 O u0 p2 c0 {8,S} {26,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 O u1 p2 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.9824,0.0352146,0.000110883,-1.77703e-07,7.50951e-11,-32816.1,-22.4255], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[19.7391,0.0616748,-3.22418e-05,8.09238e-09,-7.9221e-13,-36366,-66.9568], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 103,
    label = "aNHPT3O2H-5O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {8,S} {11,S}
2  C u0 p0 c0 {3,S} {5,S} {9,S} {12,S}
3  C u0 p0 c0 {1,S} {2,S} {15,S} {16,S}
4  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {2,S} {7,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {22,S} {23,S} {24,S}
8  O u0 p2 c0 {1,S} {10,S}
9  O u0 p2 c0 {2,S} {25,S}
10 O u0 p2 c0 {8,S} {26,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 O u1 p2 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.2143,0.0387378,0.000118247,-1.92991e-07,8.25306e-11,-32663.3,-7.98463], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[16.8313,0.0677198,-3.60266e-05,9.10891e-09,-8.93891e-13,-36186.7,-52.0489], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 104,
    label = "aNHPT3O2H-6O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {8,S} {11,S}
2  C u0 p0 c0 {4,S} {6,S} {9,S} {12,S}
3  C u0 p0 c0 {1,S} {4,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {3,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
6  C u0 p0 c0 {2,S} {22,S} {23,S} {24,S}
7  C u0 p0 c0 {5,S} {19,S} {20,S} {21,S}
8  O u0 p2 c0 {1,S} {10,S}
9  O u0 p2 c0 {2,S} {25,S}
10 O u0 p2 c0 {8,S} {26,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 O u1 p2 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.3252,0.0523208,7.98251e-05,-1.58869e-07,7.24823e-11,-33684.3,-10.3359], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[20.6748,0.0583074,-2.93372e-05,7.11664e-09,-6.76808e-13,-37504.2,-70.2724], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 105,
    label = "aNHPT3O2H-7O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {8,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {5,S} {16,S} {17,S}
4  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {6,S} {18,S} {19,S}
6  C u0 p0 c0 {5,S} {9,S} {20,S} {21,S}
7  C u0 p0 c0 {4,S} {22,S} {23,S} {24,S}
8  O u0 p2 c0 {1,S} {10,S}
9  O u0 p2 c0 {6,S} {25,S}
10 O u0 p2 c0 {8,S} {26,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 O u1 p2 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.46543,0.0719969,1.64994e-05,-7.70233e-08,3.75215e-11,-30189.6,10.3527], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[15.1203,0.0673566,-3.47946e-05,8.60919e-09,-8.31623e-13,-33163.9,-38.1017], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 106,
    label = "aNHPT4O2H-1O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {14,S} {15,S}
3  C u0 p0 c0 {1,S} {4,S} {16,S} {17,S}
4  C u0 p0 c0 {3,S} {6,S} {18,S} {19,S}
5  C u0 p0 c0 {2,S} {7,S} {12,S} {13,S}
6  C u0 p0 c0 {4,S} {9,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {22,S} {23,S} {24,S}
8  O u0 p2 c0 {1,S} {10,S}
9  O u0 p2 c0 {6,S} {25,S}
10 O u0 p2 c0 {8,S} {26,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 O u1 p2 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.9299,0.0300208,0.000149874,-2.34099e-07,9.96594e-11,-31345.4,-16.2499], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[21.0842,0.0608668,-3.16884e-05,7.8876e-09,-7.65407e-13,-35813.7,-75.1068], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 107,
    label = "aNHPT4O2H-2O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {8,S} {12,S}
2  C u0 p0 c0 {3,S} {6,S} {9,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {5,S} {15,S} {16,S}
5  C u0 p0 c0 {4,S} {7,S} {17,S} {18,S}
6  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {22,S} {23,S} {24,S}
8  O u0 p2 c0 {1,S} {10,S}
9  O u0 p2 c0 {2,S} {25,S}
10 O u0 p2 c0 {8,S} {26,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 O u1 p2 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.83144,0.0635632,3.57775e-05,-9.87648e-08,4.62315e-11,-32756.6,-3.07427], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[17.4937,0.0634454,-3.25505e-05,8.02326e-09,-7.73072e-13,-35880.1,-52.4745], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 108,
    label = "aNHPT4O2H-3O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {12,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {11,S}
3  C u0 p0 c0 {1,S} {5,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {7,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {22,S} {23,S} {24,S}
8  O u0 p2 c0 {1,S} {10,S}
9  O u0 p2 c0 {2,S} {25,S}
10 O u0 p2 c0 {8,S} {26,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 O u1 p2 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.883,0.041079,0.000106654,-1.74884e-07,7.37042e-11,-32310,-13.4518], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[17.968,0.0678323,-3.69617e-05,9.55364e-09,-9.55451e-13,-36077,-60.1523], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 109,
    label = "a22DMB1O2H-3O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {10,S}
3  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
7  O u0 p2 c0 {3,S} {9,S}
8  O u0 p2 c0 {2,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.5445,0.0351058,7.27646e-05,-1.22083e-07,5.15647e-11,-29774.6,-17.2619], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[15.9324,0.0547425,-2.8025e-05,6.91411e-09,-6.67559e-13,-32187.3,-46.7556], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 110,
    label = "a22DMB1O2H-4O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {8,S} {12,S} {13,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {3,S} {9,S}
8  O u0 p2 c0 {4,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.6868,0.0111767,0.000142766,-1.98905e-07,8.09375e-11,-27812.9,-17.1972], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.5423,0.0584891,-3.00685e-05,7.41268e-09,-7.13815e-13,-29962.3,-32.3622], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 111,
    label = "a22DMB1O2H-5O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {8,S} {12,S} {13,S}
5  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
7  O u0 p2 c0 {3,S} {9,S}
8  O u0 p2 c0 {4,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.18273,0.0429995,7.60763e-05,-1.40497e-07,6.18834e-11,-27771.8,-5.7931], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[18.1194,0.0524221,-2.69025e-05,6.64853e-09,-6.42789e-13,-31374.8,-58.8759], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 112,
    label = "a22DMB3O2H-1O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {10,S}
3  C u0 p0 c0 {1,S} {8,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
7  O u0 p2 c0 {2,S} {9,S}
8  O u0 p2 c0 {3,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.91642,0.0450218,6.98964e-05,-1.34561e-07,6.00153e-11,-29413,-5.46192], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[18.1768,0.0513705,-2.6014e-05,6.36654e-09,-6.11026e-13,-32984.2,-59.6432], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 113,
    label = "a22DMB3O2H-4O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {10,S}
3  C u0 p0 c0 {2,S} {8,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {2,S} {9,S}
8  O u0 p2 c0 {3,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.0812,0.0502682,6.0107e-05,-1.25132e-07,5.66428e-11,-28399.1,-4.28932], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[16.8773,0.0556618,-2.91638e-05,7.30404e-09,-7.12343e-13,-31773.1,-55.6153], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 114,
    label = "a22DMB4O2H-1O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {8,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {7,S} {12,S} {13,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {4,S} {9,S}
8  O u0 p2 c0 {3,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.85481,0.0257445,0.00011482,-1.75395e-07,7.34813e-11,-27469.8,-3.4705], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.2954,0.0568864,-2.91897e-05,7.21011e-09,-6.96528e-13,-30293.8,-35.606], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 115,
    label = "a22DMB4O2H-3O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {10,S}
3  C u0 p0 c0 {2,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {3,S} {9,S}
8  O u0 p2 c0 {2,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.7504,0.0481781,6.76611e-05,-1.31425e-07,5.81396e-11,-28336.5,-2.30081], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[15.934,0.0586462,-3.15492e-05,8.07435e-09,-8.01403e-13,-31770.8,-51.4589], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 116,
    label = "a23DMB1O2H-2O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {10,S}
3  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
5  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
6  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
7  O u0 p2 c0 {3,S} {9,S}
8  O u0 p2 c0 {1,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.89171,0.0788746,-2.44186e-05,-2.93428e-08,1.89851e-11,-29960.8,3.1913], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[18.4417,0.0527815,-2.74061e-05,6.83954e-09,-6.66628e-13,-33583.6,-63.0618], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 117,
    label = "a23DMB1O2H-3O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {10,S}
3  C u0 p0 c0 {2,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
7  O u0 p2 c0 {3,S} {9,S}
8  O u0 p2 c0 {1,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.0272,0.0511413,5.37591e-05,-1.15187e-07,5.19672e-11,-30221.4,-2.5141], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[17.0393,0.0546373,-2.83359e-05,7.05297e-09,-6.85431e-13,-33645.8,-54.7992], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 118,
    label = "a23DMB1O2H-4O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {11,S}
3  C u0 p0 c0 {2,S} {7,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {8,S} {12,S} {13,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {3,S} {9,S}
8  O u0 p2 c0 {4,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.20681,0.0577069,3.51765e-05,-9.78961e-08,4.67527e-11,-27107.9,3.78667], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[16.617,0.0533185,-2.69158e-05,6.5524e-09,-6.25242e-13,-30263,-48.7535], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 119,
    label = "a23DMB1O2H-5O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {10,S}
3  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {8,S} {12,S} {13,S}
5  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {3,S} {9,S}
8  O u0 p2 c0 {4,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.93011,0.0140058,0.000182481,-2.59407e-07,1.05289e-10,-27358.3,-8.54425], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[20.1781,0.0562286,-3.16614e-05,8.41455e-09,-8.6107e-13,-33062.3,-77.2227], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 120,
    label = "a23DMB2O2H-1O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {10,S}
3  C u0 p0 c0 {1,S} {8,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
5  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
6  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
7  O u0 p2 c0 {1,S} {9,S}
8  O u0 p2 c0 {3,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.91233,0.0470675,0.000104517,-1.85068e-07,8.04765e-11,-30368,3.93755], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[16.1764,0.0652298,-3.74295e-05,9.93468e-09,-1.00649e-12,-34851.9,-58.7834], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 121,
    label = "a23DMB2O2H-3O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {8,S}
3  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {1,S} {9,S}
8  O u0 p2 c0 {2,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.42496,0.0699088,-1.60918e-05,-3.16247e-08,1.90493e-11,-32177.5,-2.97765], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[16.1407,0.0535751,-2.69904e-05,6.56837e-09,-6.27096e-13,-34706.5,-49.2126], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 122,
    label = "a23DMB2O2H-4O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {10,S}
3  C u0 p0 c0 {2,S} {8,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
7  O u0 p2 c0 {1,S} {9,S}
8  O u0 p2 c0 {3,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.68222,0.0585992,3.77857e-05,-1.03456e-07,4.93644e-11,-29895.1,4.71995], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[17.345,0.0520723,-2.62091e-05,6.37577e-09,-6.08583e-13,-33426.2,-54.5288], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 123,
    label = "a24DMP1O2H-2O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {9,S}
2  C u0 p0 c0 {3,S} {6,S} {7,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {8,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {22,S} {23,S} {24,S}
6  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
7  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
8  O u0 p2 c0 {4,S} {10,S}
9  O u0 p2 c0 {1,S} {25,S}
10 O u0 p2 c0 {8,S} {26,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 O u1 p2 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.76447,0.0883433,-2.09117e-05,-3.87163e-08,2.27598e-11,-32580.1,4.42452], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[18.3555,0.0662034,-3.54663e-05,9.04183e-09,-8.94877e-13,-36458.3,-63.1399], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 124,
    label = "a24DMP1O2H-3O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {7,S} {12,S}
2  C u0 p0 c0 {3,S} {5,S} {6,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {9,S} {13,S}
4  C u0 p0 c0 {1,S} {8,S} {14,S} {15,S}
5  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {1,S} {22,S} {23,S} {24,S}
8  O u0 p2 c0 {4,S} {10,S}
9  O u0 p2 c0 {3,S} {25,S}
10 O u0 p2 c0 {8,S} {26,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 O u1 p2 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.13542,0.0552766,9.92793e-05,-1.88889e-07,8.44115e-11,-32007.4,3.02398], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[22.1814,0.058875,-3.08389e-05,7.75691e-09,-7.61018e-13,-37606.9,-83.7052], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 125,
    label = "a24DMP1O2H-4O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {9,S}
2  C u0 p0 c0 {3,S} {4,S} {7,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {8,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {1,S} {22,S} {23,S} {24,S}
7  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
8  O u0 p2 c0 {4,S} {10,S}
9  O u0 p2 c0 {1,S} {25,S}
10 O u0 p2 c0 {8,S} {26,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 O u1 p2 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.09072,0.0536593,9.48129e-05,-1.78587e-07,7.92689e-11,-34114.2,-1.46032], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[21.3064,0.0605356,-3.1822e-05,8.01089e-09,-7.85697e-13,-39194.9,-78.4954], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 126,
    label = "a24DMP1O2H-5O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {11,S}
2  C u0 p0 c0 {3,S} {4,S} {7,S} {12,S}
3  C u0 p0 c0 {1,S} {2,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {8,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {9,S} {15,S} {16,S}
6  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {2,S} {22,S} {23,S} {24,S}
8  O u0 p2 c0 {4,S} {10,S}
9  O u0 p2 c0 {5,S} {25,S}
10 O u0 p2 c0 {8,S} {26,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 O u1 p2 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.11417,0.0413553,0.000125074,-2.11169e-07,9.2205e-11,-30471.4,-2.2402], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[19.2123,0.0624517,-3.23165e-05,8.00517e-09,-7.73722e-13,-34852.2,-64.2104], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 127,
    label = "a24DMP1O2H-6O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {12,S}
2  C u0 p0 c0 {3,S} {6,S} {7,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {8,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {9,S} {15,S} {16,S}
6  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {2,S} {22,S} {23,S} {24,S}
8  O u0 p2 c0 {4,S} {10,S}
9  O u0 p2 c0 {5,S} {25,S}
10 O u0 p2 c0 {8,S} {26,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 O u1 p2 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.81718,0.0742315,3.79442e-05,-1.17463e-07,5.65885e-11,-30800.9,8.4844], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[19.7065,0.0632849,-3.35038e-05,8.46186e-09,-8.30846e-13,-35398.3,-68.4093], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 128,
    label = "a24DMP2O2H-1O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {3,S} {6,S} {7,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {9,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {22,S} {23,S} {24,S}
6  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
7  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
8  O u0 p2 c0 {1,S} {10,S}
9  O u0 p2 c0 {4,S} {25,S}
10 O u0 p2 c0 {8,S} {26,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 O u1 p2 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.38561,0.0675217,4.23915e-05,-1.10785e-07,5.05813e-11,-32626,0.0304632], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[20.0083,0.0628752,-3.34575e-05,8.51043e-09,-8.41759e-13,-37181.7,-71.5024], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 129,
    label = "a24DMP2O2H-3O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {3,S} {6,S} {7,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {9,S} {12,S}
4  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
5  C u0 p0 c0 {1,S} {22,S} {23,S} {24,S}
6  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
7  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
8  O u0 p2 c0 {1,S} {10,S}
9  O u0 p2 c0 {3,S} {25,S}
10 O u0 p2 c0 {8,S} {26,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 O u1 p2 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.0132,0.0568997,7.68532e-05,-1.5202e-07,6.72215e-11,-33534.2,-2.77932], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[20.617,0.0615311,-3.26746e-05,8.31881e-09,-8.24395e-13,-38419.9,-76.1456], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 130,
    label = "a24DMP2O2H-4O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {4,S} {5,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {1,S} {22,S} {23,S} {24,S}
8  O u0 p2 c0 {1,S} {10,S}
9  O u0 p2 c0 {2,S} {25,S}
10 O u0 p2 c0 {8,S} {26,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 O u1 p2 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.45814,0.0860805,-4.33515e-06,-6.1864e-08,3.27064e-11,-36986.5,3.07208], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[17.2436,0.0704868,-3.8675e-05,9.98468e-09,-9.94255e-13,-40750.6,-61.1], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 131,
    label = "a24DMP2O2H-5O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {8,S}
2  C u0 p0 c0 {3,S} {4,S} {7,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {9,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {1,S} {22,S} {23,S} {24,S}
7  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
8  O u0 p2 c0 {1,S} {10,S}
9  O u0 p2 c0 {4,S} {25,S}
10 O u0 p2 c0 {8,S} {26,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 O u1 p2 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.7961,0.0371775,0.000122511,-1.92274e-07,7.99143e-11,-34197.2,-14.3804], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[17.0893,0.0714502,-3.97822e-05,1.04181e-08,-1.05053e-12,-38009.1,-58.3009], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 132,
    label = "a24DMP3O2H-1O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {7,S} {12,S}
2  C u0 p0 c0 {3,S} {5,S} {6,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {8,S} {13,S}
4  C u0 p0 c0 {1,S} {9,S} {14,S} {15,S}
5  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {1,S} {22,S} {23,S} {24,S}
8  O u0 p2 c0 {3,S} {10,S}
9  O u0 p2 c0 {4,S} {25,S}
10 O u0 p2 c0 {8,S} {26,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 O u1 p2 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.63431,0.0602116,4.47744e-05,-1.07243e-07,4.91692e-11,-30951.5,-2.96652], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[15.7512,0.0662632,-3.40305e-05,8.36622e-09,-8.0321e-13,-33733.6,-44.8208], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 133,
    label = "a24DMP3O2H-2O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {9,S}
2  C u0 p0 c0 {3,S} {6,S} {7,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {8,S} {12,S}
4  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
5  C u0 p0 c0 {1,S} {22,S} {23,S} {24,S}
6  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
7  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
8  O u0 p2 c0 {3,S} {10,S}
9  O u0 p2 c0 {1,S} {25,S}
10 O u0 p2 c0 {8,S} {26,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 O u1 p2 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.13922,0.0764965,3.40353e-05,-1.10795e-07,5.28911e-11,-33301.3,7.68433], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[18.8614,0.0668836,-3.64472e-05,9.40833e-09,-9.39436e-13,-38007.7,-68.8613], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 134,
    label = "a2MPT3O2H-4O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {11,S}
3  C u0 p0 c0 {2,S} {6,S} {8,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {3,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {2,S} {9,S}
8  O u0 p2 c0 {3,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.19559,0.0860004,-4.72487e-05,-4.84314e-09,1.045e-11,-28951.1,6.10668], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[16.7911,0.0543074,-2.76716e-05,6.77713e-09,-6.49798e-13,-31910.9,-53.1863], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 4
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RRccsd(t)-f12/cc-pvdz-f12//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 135,
    label = "aTMP1O2H-3O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {12,S}
3  C u0 p0 c0 {1,S} {2,S} {10,S} {13,S}
4  C u0 p0 c0 {1,S} {9,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {22,S} {23,S} {24,S}
6  C u0 p0 c0 {1,S} {25,S} {26,S} {27,S}
7  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
8  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
9  O u0 p2 c0 {4,S} {11,S}
10 O u0 p2 c0 {3,S} {28,S}
11 O u0 p2 c0 {9,S} {29,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {6,S}
28 O u1 p2 c0 {10,S}
29 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.31561,0.0819242,3.09732e-05,-1.08762e-07,5.18902e-11,-34916,-0.734959], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[22.1938,0.0692405,-3.63498e-05,9.15601e-09,-8.99073e-13,-39932.9,-83.273], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 5
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RUb2plypd3/cc-pvtz//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 136,
    label = "aTMP1O2H-4O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {9,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {2,S} {22,S} {23,S} {24,S}
8  C u0 p0 c0 {2,S} {25,S} {26,S} {27,S}
9  O u0 p2 c0 {4,S} {11,S}
10 O u0 p2 c0 {2,S} {28,S}
11 O u0 p2 c0 {9,S} {29,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 O u1 p2 c0 {10,S}
29 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.97737,0.0717601,6.76008e-05,-1.49823e-07,6.7218e-11,-37244.6,-4.93725], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[21.086,0.0754082,-4.14643e-05,1.07871e-08,-1.08371e-12,-42314.5,-81.0654], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 5
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RUb2plypd3/cc-pvtz//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 137,
    label = "aTMP1O2H-5O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {5,S} {8,S} {12,S}
3  C u0 p0 c0 {1,S} {2,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {9,S} {17,S} {18,S}
5  C u0 p0 c0 {2,S} {10,S} {15,S} {16,S}
6  C u0 p0 c0 {1,S} {22,S} {23,S} {24,S}
7  C u0 p0 c0 {1,S} {25,S} {26,S} {27,S}
8  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
9  O u0 p2 c0 {4,S} {11,S}
10 O u0 p2 c0 {5,S} {28,S}
11 O u0 p2 c0 {9,S} {29,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 O u1 p2 c0 {10,S}
29 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.4629,0.0774681,4.03504e-05,-1.16256e-07,5.42591e-11,-34408.5,1.96578], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[19.4456,0.0742303,-3.93656e-05,9.95237e-09,-9.77833e-13,-38704.9,-65.972], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 5
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RUb2plypd3/cc-pvtz//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 138,
    label = "aTMP1O2H-6O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {12,S}
3  C u0 p0 c0 {1,S} {2,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {9,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {10,S} {15,S} {16,S}
6  C u0 p0 c0 {1,S} {25,S} {26,S} {27,S}
7  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
8  C u0 p0 c0 {2,S} {22,S} {23,S} {24,S}
9  O u0 p2 c0 {4,S} {11,S}
10 O u0 p2 c0 {5,S} {28,S}
11 O u0 p2 c0 {9,S} {29,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {6,S}
28 O u1 p2 c0 {10,S}
29 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.207,0.053446,8.67002e-05,-1.58877e-07,6.93163e-11,-33801.7,-11.8043], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[19.1728,0.070758,-3.61985e-05,8.92053e-09,-8.60193e-13,-37371.3,-61.0809], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 5
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RUb2plypd3/cc-pvtz//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 139,
    label = "aTMP3O2H-1O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {12,S}
3  C u0 p0 c0 {1,S} {2,S} {9,S} {13,S}
4  C u0 p0 c0 {1,S} {10,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {22,S} {23,S} {24,S}
6  C u0 p0 c0 {1,S} {25,S} {26,S} {27,S}
7  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
8  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
9  O u0 p2 c0 {3,S} {11,S}
10 O u0 p2 c0 {4,S} {28,S}
11 O u0 p2 c0 {9,S} {29,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {6,S}
28 O u1 p2 c0 {10,S}
29 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.505,0.0582405,7.50588e-05,-1.45147e-07,6.35186e-11,-34263.3,-11.0412], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[18.7955,0.0726087,-3.77195e-05,9.40695e-09,-9.1559e-13,-37896.8,-61.6982], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 5
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RUb2plypd3/cc-pvtz//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 140,
    label = "aTMP3O2H-4O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {9,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {2,S} {22,S} {23,S} {24,S}
8  C u0 p0 c0 {2,S} {25,S} {26,S} {27,S}
9  O u0 p2 c0 {3,S} {11,S}
10 O u0 p2 c0 {2,S} {28,S}
11 O u0 p2 c0 {9,S} {29,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 O u1 p2 c0 {10,S}
29 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.63355,0.0832599,2.24246e-05,-9.34383e-08,4.50176e-11,-36185.8,-0.326935], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.8683,0.086742,-4.78593e-05,1.23785e-08,-1.23203e-12,-38937.8,-42.3525], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 5
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RUb2plypd3/cc-pvtz//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 141,
    label = "aTMP3O2H-5O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {4,S} {8,S} {12,S}
3  C u0 p0 c0 {1,S} {2,S} {9,S} {13,S}
4  C u0 p0 c0 {2,S} {10,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {1,S} {22,S} {23,S} {24,S}
7  C u0 p0 c0 {1,S} {25,S} {26,S} {27,S}
8  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
9  O u0 p2 c0 {3,S} {11,S}
10 O u0 p2 c0 {4,S} {28,S}
11 O u0 p2 c0 {9,S} {29,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 O u1 p2 c0 {10,S}
29 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.89517,0.0610016,6.67501e-05,-1.31835e-07,5.71481e-11,-35378.8,-10.4791], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[15.2629,0.0816343,-4.41073e-05,1.1288e-08,-1.118e-12,-38238,-45.903], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 5
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RUb2plypd3/cc-pvtz//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 142,
    label = "aTMP4O2H-1O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {10,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {2,S} {22,S} {23,S} {24,S}
8  C u0 p0 c0 {2,S} {25,S} {26,S} {27,S}
9  O u0 p2 c0 {2,S} {11,S}
10 O u0 p2 c0 {4,S} {28,S}
11 O u0 p2 c0 {9,S} {29,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 O u1 p2 c0 {10,S}
29 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.13681,0.052557,0.000121704,-2.05648e-07,8.70302e-11,-36229.2,-7.401], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[21.1535,0.0750526,-4.09556e-05,1.05888e-08,-1.0592e-12,-41715.2,-81.6319], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 5
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RUb2plypd3/cc-pvtz//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 143,
    label = "aTMP4O2H-3O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {2,S} {22,S} {23,S} {24,S}
8  C u0 p0 c0 {2,S} {25,S} {26,S} {27,S}
9  O u0 p2 c0 {2,S} {11,S}
10 O u0 p2 c0 {3,S} {28,S}
11 O u0 p2 c0 {9,S} {29,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 O u1 p2 c0 {10,S}
29 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.09808,0.0819123,3.28235e-05,-1.05311e-07,4.86581e-11,-36145,2.88342], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[17.2423,0.0818964,-4.58202e-05,1.2091e-08,-1.22842e-12,-40439.8,-61.4226], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 5
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RUb2plypd3/cc-pvtz//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 144,
    label = "aTMP4O2H-5O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {10,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {1,S} {22,S} {23,S} {24,S}
8  C u0 p0 c0 {2,S} {25,S} {26,S} {27,S}
9  O u0 p2 c0 {2,S} {11,S}
10 O u0 p2 c0 {4,S} {28,S}
11 O u0 p2 c0 {9,S} {29,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 O u1 p2 c0 {10,S}
29 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.62419,0.0687957,7.12342e-05,-1.49299e-07,6.56817e-11,-35218.5,-1.29466], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[20.4783,0.0747605,-4.0669e-05,1.05215e-08,-1.05426e-12,-40361.8,-76.6904], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 5
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RUb2plypd3/cc-pvtz//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 145,
    label = "aTMP5O2H-1O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {5,S} {8,S} {12,S}
3  C u0 p0 c0 {1,S} {2,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {10,S} {17,S} {18,S}
5  C u0 p0 c0 {2,S} {9,S} {15,S} {16,S}
6  C u0 p0 c0 {1,S} {22,S} {23,S} {24,S}
7  C u0 p0 c0 {1,S} {25,S} {26,S} {27,S}
8  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
9  O u0 p2 c0 {5,S} {11,S}
10 O u0 p2 c0 {4,S} {28,S}
11 O u0 p2 c0 {9,S} {29,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 O u1 p2 c0 {10,S}
29 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.9544,0.02618,0.000171709,-2.49037e-07,1.01963e-10,-32967.9,-11.4151], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[15.7383,0.0801503,-4.29935e-05,1.09565e-08,-1.0827e-12,-36558.9,-45.0759], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 5
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RUb2plypd3/cc-pvtz//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 146,
    label = "aTMP5O2H-3O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {4,S} {8,S} {12,S}
3  C u0 p0 c0 {1,S} {2,S} {10,S} {13,S}
4  C u0 p0 c0 {2,S} {9,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {1,S} {22,S} {23,S} {24,S}
7  C u0 p0 c0 {1,S} {25,S} {26,S} {27,S}
8  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
9  O u0 p2 c0 {4,S} {11,S}
10 O u0 p2 c0 {3,S} {28,S}
11 O u0 p2 c0 {9,S} {29,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 O u1 p2 c0 {10,S}
29 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.10857,0.0801156,1.72882e-05,-8.28232e-08,3.98545e-11,-34868.1,-4.13013], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[18.4765,0.0738087,-3.83584e-05,9.5429e-09,-9.26119e-13,-38469.2,-62.2124], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 5
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RUb2plypd3/cc-pvtz//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 147,
    label = "aTMP5O2H-4O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {4,S} {8,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {9,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {1,S} {22,S} {23,S} {24,S}
8  C u0 p0 c0 {2,S} {25,S} {26,S} {27,S}
9  O u0 p2 c0 {4,S} {11,S}
10 O u0 p2 c0 {2,S} {28,S}
11 O u0 p2 c0 {9,S} {29,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 O u1 p2 c0 {10,S}
29 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.52422,0.0932413,1.72938e-06,-7.60812e-08,3.94617e-11,-35448.3,5.32097], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[17.8585,0.078643,-4.23478e-05,1.07848e-08,-1.06308e-12,-39402.6,-62.0687], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 5
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RUb2plypd3/cc-pvtz//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

entry(
    index = 148,
    label = "aTMP5O2H-8O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {4,S} {5,S} {12,S}
3  C u0 p0 c0 {1,S} {2,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {9,S} {17,S} {18,S}
5  C u0 p0 c0 {2,S} {10,S} {15,S} {16,S}
6  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {1,S} {22,S} {23,S} {24,S}
8  C u0 p0 c0 {1,S} {25,S} {26,S} {27,S}
9  O u0 p2 c0 {4,S} {11,S}
10 O u0 p2 c0 {5,S} {28,S}
11 O u0 p2 c0 {9,S} {29,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 O u1 p2 c0 {10,S}
29 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.52596,0.0997539,-2.90415e-06,-8.21758e-08,4.45788e-11,-34537.5,10.9654], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[21.7668,0.0709336,-3.74167e-05,9.41675e-09,-9.21707e-13,-39662,-81.2091], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Elliott SN, Mulvihill CR, Ghosh MK, Curran HJ, Klippenstein SJ.
Systematic exploration of the thermochemistry for a set of peroxy hydroperoxy-alkyl radicals.
Proceedings of the Combustion Institute. 2024;40(1-4):105618-. doi:10.1016/j.proci.2024.105618

Methodology 5
vib model: harm
tors model: 1dhrf
sym model: HCO_model
sort freqs level: RUwb97xd/cc-pvtz
sort sp    level: RUb2plypd3/cc-pvtz
sort G(700.0 K) minimum
energy level:
    1.000 x RUb2plypd3/cc-pvtz//RUb2plypd3/cc-pvtz
tors level: RUwb97xd/6-31g*//RUwb97xd/6-31g*
CBH reference scheme: cbh2
""",
)

