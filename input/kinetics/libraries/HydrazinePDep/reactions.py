#!/usr/bin/env python
# encoding: utf-8

name = "HydrazinePDep"
shortDesc = u"HydrazinePDep"
longDesc =u"""
This library includes well-skipping pressure-dependent reactions on the N3H3, N3H5 and N4H6 PESs
Calculated by alongd at CCSD(T)-F12a/aug-cc-pVTZ//wB97x-D3/6-311++G(3df,3pd)
Using the modified strong collision method

opt, freq: wB97x-D3/6-311++G(3df,3pd)
sp: CCSD(T)-F12a/aug-cc-pVTZ
rotors: B3LYP/6-311++G(3df,3pd)
Each TS was traced with an IRC calculation in both direction to verify adjacent wells
"""

entry(
    index = 1,
    label = "N2H3 + NH2 <=> H2NN(S) + NH3",
    duplicate = True,
    kinetics = Chebyshev(
        coeffs = [
            [10.9462, -0.657135, -0.128688, -0.00271182],
            [0.241821, 0.71835, 0.111562, -0.0107844],
            [0.0324133, 0.0210824, 0.0310451, 0.0117424],
            [0.0493565, -0.0703768, -0.00729241, 0.00220777],
            [0.0511379, -0.0237852, -0.00892897, -0.00106884],
            [0.0307409, -0.00144177, -0.00197003, -0.000844388],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (300, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.01, 'bar'),
        Pmax = (100, 'bar'),
    ),
)

entry(
    index = 2,
    label = 'N2H3 + NH2 <=> H2NN(S) + NH3',
    duplicate = True,
    kinetics = Arrhenius(A=(1.03+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"""estimated""",
    longDesc =
u"""
This is the direct non-PDep route.
Estimated by alongd as having the same A factor as 'N2H3 + NH2 <=> H2NN(T) + NH3' with Ea = 0 (barrierless)
The A factor was refitted into a classical (non-modified) Arrhenius form:
Arrhenius(A=(1.03198e+12,'cm^3/(mol*s)'), n=0, Ea=(20.0354,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'),
Fitted to 51 data points; dA = *|/ 1.18263, dn = +|- 0, dEa = +|- 1.27006 kJ/mol
Note that the 'N2H3 + NH2 <=> H2NN(T) + NH3' reaction has a barrier of ~5 kJ/mol in the forward direction although
it's Ea in the modified Arrhenius form is negative: Arrhenius(A=(1.65e+00, 'cm^3/(mol*s)'), n=3.41, Ea=(-4.0, 'kJ/mol')
""",
)

entry(
    index = 3,
    label = "N2H3 + NH2 <=> N2H2 + NH3",
    duplicate = True,
    kinetics = Chebyshev(
        coeffs = [
            [7.37428, -0.243911, -0.117704, -0.0296756],
            [1.93272, 0.284799, 0.13145, 0.0280048],
            [0.255368, -0.0123912, 0.000382405, 0.00528724],
            [0.120498, -0.032321, -0.0148317, -0.00296796],
            [0.0611435, -0.0037763, -0.0034587, -0.00210558],
            [0.0281733, 0.00220506, 0.000816488, -7.96944e-05],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (300, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.01, 'bar'),
        Pmax = (100, 'bar'),
    ),
)

entry(
    index = 4,
    label = "N2H3 + NH2 <=> N2H2 + NH3",
    duplicate = True,
    kinetics = Arrhenius(A = (9.2e+05, 'cm^3/(mol*s)'), n = 1.94, Ea = (-1.152, 'kcal/mol'), T0 = (1, 'K')),
    longDesc =
u"""
Taken from the Nitrogen_Dean_and_Bozzelli library
The same rate appears in the NOx2018 library
D&B estimated this rate of the direct hydrogen transfer reaction (not including the well-skipping rate)
""",
)

entry(
    index = 5,
    label = "N2H4 + H2NN(S) <=> NH2NHN + NH3",
    kinetics = Chebyshev(
        coeffs = [
            [-1.55265, -0.0140652, -0.00364304, -0.00475792],
            [8.16525, 0.022775, 0.00442085, 0.00762827],
            [0.932463, -0.012555, 0.000526219, -0.00410226],
            [0.302518, 0.00545572, -0.00293815, 0.00176768],
            [0.115424, -0.00292304, 0.00262053, -0.00102677],
            [0.0483531, 0.00216986, -0.00180048, 0.000821751],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (300, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.01, 'bar'),
        Pmax = (100, 'bar'),
    ),
)

entry(
    index = 6,
    label = "N2H4 + H2NN(S) <=> NH2NNH + NH3",
    kinetics = Chebyshev(
        coeffs = [
            [1.98699, -0.113914, -0.0537849, -0.0121151],
            [5.822, 0.139207, 0.0653166, 0.0139627],
            [0.546096, -0.0112129, -0.0051465, -0.000481112],
            [0.300471, -0.0115437, -0.00529662, -0.000995669],
            [0.134121, -0.00768304, -0.00294748, -0.000409043],
            [0.0511549, 0.00223963, 0.000397523, -0.000455515],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (300, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.01, 'bar'),
        Pmax = (100, 'bar'),
    ),
)

entry(
    index = 7,
    label = "N2H3 + N2H3 <=> N2H4 + H2NN(S)",
    kinetics = Chebyshev(
        coeffs = [
            [6.72919, -0.0451526, -0.0253983, -0.00967862],
            [2.11267, 0.0664785, 0.0366096, 0.0132979],
            [0.377432, -0.0233198, -0.0115621, -0.00313543],
            [0.132845, -0.00043906, -0.00117434, -0.00118497],
            [0.0561352, 0.00288429, 0.00154656, 0.000542858],
            [0.0215875, -0.000883902, -0.000109065, 0.000199072],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (300, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.01, 'bar'),
        Pmax = (100, 'bar'),
    ),
)

entry(
    index = 8,
    label = "N2H3 + N2H3 <=> NH2NHN + NH3",
    kinetics = Chebyshev(
        coeffs = [
            [6.46331, -0.0324498, -0.0174104, -0.00612641],
            [2.84097, 0.0510255, 0.0266958, 0.00881363],
            [0.465032, -0.024192, -0.011517, -0.00281626],
            [0.122197, 0.00563674, 0.00192429, -0.000256464],
            [0.0574612, 0.000459166, 0.000416254, 0.000335902],
            [0.021859, -0.00124046, -0.000315222, 8.0687e-05],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (300, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.01, 'bar'),
        Pmax = (100, 'bar'),
    ),
)

entry(
    index = 9,
    label = "N2H3 + N2H3 <=> NH2NNH + NH3",
    kinetics = Chebyshev(
        coeffs = [
            [1.56796, -0.00820358, -0.00432153, -0.00146642],
            [5.52511, 0.0142817, 0.00736381, 0.0023531],
            [0.560388, -0.0104517, -0.00522695, -0.00151849],
            [0.084983, 0.00627954, 0.00300335, 0.000735817],
            [0.0868149, -0.00320761, -0.00150592, -0.000328358],
            [0.0220066, 0.00110911, 0.00051976, 9.05161e-05],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (300, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.01, 'bar'),
        Pmax = (100, 'bar'),
    ),
)

entry(
    index = 10,
    label = "NH2NHN <=> N2 + NH3",
    kinetics = Chebyshev(
        coeffs = [
            [7.24651, 1.33077, -0.0909997, -0.0172313],
            [2.52875, 0.63286, 0.048242, 0.00519734],
            [-0.370152, 0.0453117, 0.0325405, 0.0067369],
            [-0.150952, -0.00677141, 0.00539954, 0.00183354],
            [-0.0235124, -0.016207, -0.00242366, 0.000184513],
            [0.0112949, -0.0102983, -0.00270927, -0.00031368],
        ],
        kunits = 's^-1',
        Tmin = (500, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.01, 'bar'),
        Pmax = (100, 'bar'),
    ),
)

entry(
    index = 11,
    label = "NH2NNH <=> N2 + NH3",
    kinetics = Chebyshev(
        coeffs = [
            [3.54055, 0.877848, -0.113778, -0.00793179],
            [5.73339, 0.788821, -0.00922299, -0.0153393],
            [-0.186452, 0.102511, 0.0400612, 0.00313661],
            [-0.0816744, 0.0044157, 0.00712108, 0.00249208],
            [-0.0264087, 0.00607652, 0.00134873, -0.000298492],
            [-0.0137462, 0.00258801, 0.00136165, 8.93085e-05],
        ],
        kunits = 's^-1',
        Tmin = (500, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.01, 'bar'),
        Pmax = (100, 'bar'),
    ),
)

entry(
    index = 12,
    label = "NHNHNH <=> N2 + NH3",
    kinetics = Chebyshev(
        coeffs = [
            [1.33071, 0.545182, -0.143043, -0.011935],
            [7.31447, 0.749515, -0.0490195, -0.00777693],
            [-0.176431, 0.178021, 0.0179486, -0.0158657],
            [-0.0786998, 0.0237858, 0.019679, 0.00279509],
            [-0.0136101, 9.74048e-06, 0.00162918, 0.00213994],
            [-0.00742617, 0.00395407, -0.000434482, -0.00020017],
        ],
        kunits = 's^-1',
        Tmin = (500, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.01, 'bar'),
        Pmax = (100, 'bar'),
    ),
)

entry(
    index = 13,
    label = "cN3H3 <=> N2 + NH3",
    kinetics = Chebyshev(
        coeffs = [
            [3.63634, 0.455083, -0.385569, -0.0243479],
            [5.26594, 1.11309, 0.176089, -0.0324886],
            [-0.273084, 0.0746858, 0.0556383, 0.0147486],
            [-0.0556989, -0.0228168, -0.00313498, 0.00223538],
            [0.00147699, 0.00449178, -0.00187138, -0.00221878],
            [0.000986298, 0.00898812, 0.00196265, -0.000498911],
        ],
        kunits = 's^-1',
        Tmin = (500, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.01, 'bar'),
        Pmax = (100, 'bar'),
    ),
)
