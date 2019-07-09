#!/usr/bin/env python
# encoding: utf-8

name = "c-C5H5_CH3_Sharma"
shortDesc = u"CCSD(T)//B3LYP/6-31g+(d') and MP4SDQ//B3LYP/CBSB4"
longDesc = u"""
Kinetics from:
Computed Rate Coefficients and Product Yields for c-C5H5+CH3->Products
S. Sharma and W. H. Green*
Department of Chemical Engineering, Massachusetts Institute of Technology, Cambridge, MA 02139
Received: January 22, 2009; Revised Manuscript Received: June 1, 2009
J. Phys. Chem. A 2009, 113, 8871-8882

Rates from Table 8 and Table 9 are fitted in Chebyshev form
Duplicated rates (backward rate if there is the forward rate) are deleted after we checked the backward rates are similar to those rates calculated from thermo by using plot kinetics tool in RMG website
The adduct C5H5CH3 in the dictionary is same as C5H5CH3-5 in the paper, because the paper mentioned either C5H5CH3-5, C5H5CH3-2, or C5H5CH3-3 would give similar computational results 
"""
entry(
    index = 1,
    label = "c-C5H5 + CH3 <=> C5H5CH3",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.78, 0.8785, -0.1149, -0.001832],
            [-1.417, 0.7997, 0.01616, -0.01754],
            [-0.415, 0.1124, 0.03576, 0.00678],
            [-0.08073, -0.01799, -0.003221, 0.001208],
            [-0.008975, -0.0145, 0.005056, 0.004415],
            [0.003178, 0.003757, -0.007701, -0.0002603],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (900, 'K'),
        Tmax = (2000, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (100, 'atm'),
    ),
)

entry(
    index = 2,
    label = "c-C5H5 + CH3 <=> fulvene + H2",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [7.023, -0.291, -0.1032, -0.01261],
            [1.241, 0.4052, 0.1259, -0.0006594],
            [-0.0387, -0.1143, -0.01474, 0.01703],
            [-0.005006, -0.01092, -0.01151, -0.001045],
            [-0.006606, 0.01275, -0.001444, -0.007838],
            [-0.002977, -0.001724, 0.005011, 0.005123],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (900, 'K'),
        Tmax = (2000, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (100, 'atm'),
    ),
)

entry(
    index = 3,
    label = "c-C5H5 + CH3 <=> R1 + H",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [10.68, -0.3394, -0.1189, -0.001221],
            [1.026, 0.4646, 0.1445, -0.02713],
            [-0.07897, -0.1189, -0.01222, 0.02883],
            [-0.008973, -0.02412, -0.01698, 0.006258],
            [-0.009998, 0.03201, 0.00705, -0.02773],
            [0.001455, -0.01582, -0.005142, 0.01938],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (900, 'K'),
        Tmax = (2000, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (100, 'atm'),
    ),
)

entry(
    index = 4,
    label = "c-C5H5 + CH3 <=> R2 + H",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.13, -0.3468, -0.1171, -0.01825],
            [0.9468, 0.4634, 0.1337, 0.00258],
            [-0.09063, -0.1085, -0.00735, 0.0157],
            [-0.009971, -0.01848, -0.01469, -0.004846],
            [-0.005178, 0.008227, -0.001395, -0.003285],
            [0.005693, -0.004941, -0.0002623, 0.001006],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (900, 'K'),
        Tmax = (2000, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (100, 'atm'),
    ),
)

entry(
    index = 5,
    label = "c-C5H5 + CH3 <=> R3 + H",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.917, -0.2487, -0.1087, -0.02675],
            [1.33, 0.324, 0.1352, 0.0354],
            [-0.07275, -0.09899, -0.0235, 0.01103],
            [-0.02516, -0.0004024, -0.01376, -0.01475],
            [0.01083, -0.003285, 0.005765, 0.007511],
            [-0.02244, 0.0218, -0.0005671, -0.01805],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (900, 'K'),
        Tmax = (2000, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (100, 'atm'),
    ),
)

entry(
    index = 6,
    label = "c-C5H5 + CH3 <=> R4 + H",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [7.724, -0.0752, -0.04855, -0.02425],
            [2.233, 0.1122, 0.06767, 0.02741],
            [-0.07647, -0.04784, -0.02341, -0.002244],
            [-0.03903, 0.008269, 0.001352, -0.003613],
            [-0.01283, -0.002457, -0.003263, -0.004923],
            [-0.007864, 0.00501, 0.006202, 0.007613],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (900, 'K'),
        Tmax = (2000, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (100, 'atm'),
    ),
)

entry(
    index = 7,
    label = "C5H5CH3 <=> fulvene + H2",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-4.702, 1.599, -0.2011, -0.004738],
            [3.691, 0.9597, 0.04576, -0.006535],
            [-0.407, 0.00685, 0.03557, 0.01094],
            [-0.03281, -0.04635, -0.003769, -0.001537],
            [0.02373, -0.02257, -0.007509, 0.00744],
            [-0.004956, 0.01092, 1.852e-05, -0.005072],
        ],
        kunits = 's^-1',
        Tmin = (900, 'K'),
        Tmax = (2000, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (100, 'atm'),
    ),
)

entry(
    index = 8,
    label = "C5H5CH3 <=> R1 + H",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-0.7895, 1.467, -0.2007, 0.006475],
            [3.641, 0.8966, 0.04984, -0.02043],
            [-0.3922, 0.005744, 0.03384, 0.01197],
            [-0.02872, -0.04813, -0.00581, 0.005204],
            [0.01223, -0.02192, 2.613e-06, -0.004875],
            [0.005099, 0.01693, -0.008695, 0.00185],
        ],
        kunits = 's^-1',
        Tmin = (900, 'K'),
        Tmax = (2000, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (100, 'atm'),
    ),
)

entry(
    index = 9,
    label = "C5H5CH3 <=> R2 + H",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [0.7718, 1.395, -0.1817, -0.003595],
            [3.617, 0.8722, 0.02795, -0.01528],
            [-0.3918, 0.01181, 0.03779, 0.005188],
            [-0.0316, -0.04442, 0.002159, -0.001328],
            [0.01612, -0.02271, -0.01475, 0.004695],
            [0.008212, 0.01305, 0.004678, -0.001408],
        ],
        kunits = 's^-1',
        Tmin = (900, 'K'),
        Tmax = (2000, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (100, 'atm'),
    ),
)

entry(
    index = 10,
    label = "C5H5CH3 <=> R3 + H",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-2.109, 1.956, -0.3158, 0.02151],
            [3.691, 1.109, -0.01262, 0.003726],
            [-0.44, 0.02719, 0.01301, 0.01514],
            [-0.02729, -0.04945, -0.007378, 0.004657],
            [0.01234, -0.007475, -0.004662, 0.001779],
            [0.01267, -0.004197, 0.004348, -0.001516],
        ],
        kunits = 's^-1',
        Tmin = (900, 'K'),
        Tmax = (2000, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (100, 'atm'),
    ),
)

entry(
    index = 11,
    label = "C5H5CH3 <=> R4 + H",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-7.617, 5.607, -1.541, 0.3103],
            [4.296, 0.8383, 0.3637, -0.1109],
            [-0.5101, 0.003561, 0.00764, 0.01172],
            [-0.03686, -0.02883, -0.01314, 0.002551],
            [0.01137, -0.008229, -0.005337, -0.002446],
            [0.01095, -0.001139, 0.0006071, 0.002353],
        ],
        kunits = 's^-1',
        Tmin = (900, 'K'),
        Tmax = (2000, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (100, 'atm'),
    ),
)

