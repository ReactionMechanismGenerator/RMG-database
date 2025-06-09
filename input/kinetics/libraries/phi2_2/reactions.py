#!/usr/bin/env python
# encoding: utf-8

name = "phi2_2"
shortDesc = u""
longDesc = u"""

"""

entry(
    index=0,
    label="DHC <=> HOCHO",
    kinetics = Chebyshev(
        coeffs = [
            [-0.05729, 1.105, -0.04740, -0.02741],
            [7.095, 1.504, -0.02855, -0.03402],
            [-0.1435, 0.3940, 0.03444, 0.0009022],
            [-0.4761, -0.01620, 0.01108, 0.009874],
            [-0.08182, 0.001355, -0.009023, 0.002340],
            [-0.02575, 0.003575, -0.003538, 0.0004563],
        ],
        kunits = 's^-1',
        Tmin=(300,'K'), 
        Tmax=(3000,'K'), 
        Pmin=(0.01,'bar'), 
        Pmax=(100,'bar')
    ),
    shortDesc=u"""FA2025""",
    longDesc=
    u"""
    From the pressure-dependent kinetic network of the singlet CH2O2 PES calculated at
    the CCSD(T)-F12/aug-cc-pVTZ-F12//B2PLYP-D3/def2-TZVP level of theory.    
    """,
)

entry(
    index=1,
    label="H2O + CO <=> HOCHO",
    kinetics = Chebyshev(
        coeffs = [
            [-13.01, 0.5493, -0.06648, -0.0007533],
            [18.73, 0.8176, -0.06179, -0.008217],
            [0.1737, 0.3255, 0.03136, -0.009102],
            [-0.3576, 0.05542, 0.03466, 0.001873],
            [-0.008352, -0.009932, 0.006160, 0.005113],
            [-0.02481, -0.01576, -0.003219, 0.001076],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin=(300,'K'), 
        Tmax=(3000,'K'), 
        Pmin=(0.01,'bar'), 
        Pmax=(100,'bar')
    ),
    shortDesc=u"""FA2025""",
    longDesc=
    u"""
    From the pressure-dependent kinetic network of the singlet CH2O2 PES calculated at
    the CCSD(T)-F12/aug-cc-pVTZ-F12//B2PLYP-D3/def2-TZVP level of theory.    
    """,
)

entry(
    index=2,
    label="H + HOCO <=> HOCHO",
    kinetics = Chebyshev(
        coeffs = [
            [8.891, 1.959, -0.02788, -0.01461],
            [-2.876, 0.04622, 0.03077, 0.01582],
            [-1.084, -0.005835, -0.003577, -0.00155],
            [-0.4478, -0.002435, -0.001716, -0.0009703],
            [-0.1701, -0.0001163, -0.0001118, -0.00009017],
            [-0.04983, -0.0002779, -0.0001883, -0.00009993],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin=(300,'K'), 
        Tmax=(3000,'K'), 
        Pmin=(0.01,'bar'), 
        Pmax=(100,'bar')
    ),
    shortDesc=u"""FA2025""",
    longDesc=
    u"""
    From the pressure-dependent kinetic network of the singlet CH2O2 PES calculated at
    the CCSD(T)-F12/aug-cc-pVTZ-F12//B2PLYP-D3/def2-TZVP level of theory.    
    """,
)

entry(
    index=3,
    label="H + OCHO <=> HOCHO",
    kinetics = Chebyshev(
        coeffs = [
            [15.92, 2.0, -0.00005003, -0.00002776],
            [-1.927, 0.00008454, 0.00005882, 0.00003263],
            [-0.5948, -0.00001253, -0.000008713, -0.00000483],
            [-0.1942, -0.000006438, -0.000004479, -0.000002484],
            [-0.05612, 0.000005194, 0.000003611, 0.000002002],
            [0.006008, -0.000002801, -0.000001949, -0.000001081],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin=(300,'K'), 
        Tmax=(3000,'K'), 
        Pmin=(0.01,'bar'), 
        Pmax=(100,'bar')
    ),
    shortDesc=u"""FA2025""",
    longDesc=
    u"""
    From the pressure-dependent kinetic network of the singlet CH2O2 PES calculated at
    the CCSD(T)-F12/aug-cc-pVTZ-F12//B2PLYP-D3/def2-TZVP level of theory.    
    """,
)

entry(
    index=4,
    label="H2 + CO2 <=> HOCHO",
    kinetics = Chebyshev(
        coeffs = [
            [-14.56, 0.5218, -0.04411, -0.006758],
            [19.38, 0.8255, -0.05046, -0.01098],
            [1.056, 0.3801, 0.01371, -0.004207],
            [-0.5059, 0.06190, 0.03295, 0.002809],
            [-0.1840, -0.02558, 0.01045, 0.004808],
            [0.06961, -0.01216, -0.007121, 0.001921],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin=(300,'K'), 
        Tmax=(3000,'K'), 
        Pmin=(0.01,'bar'), 
        Pmax=(100,'bar')
    ),
    shortDesc=u"""FA2025""",
    longDesc=
    u"""
    From the pressure-dependent kinetic network of the singlet CH2O2 PES calculated at
    the CCSD(T)-F12/aug-cc-pVTZ-F12//B2PLYP-D3/def2-TZVP level of theory.    
    """,
)

entry(
    index=5,
    label="OH + HCO <=> HOCHO",
    kinetics = Chebyshev(
        coeffs = [
            [11.64, 1.981, -0.01284, -0.006974],
            [-2.313, 0.01846, 0.01261, 0.006787],
            [-0.8677, -0.00132, -0.0008493, -0.0004084],
            [-0.3094, -0.0008318, -0.0005785, -0.0003207],
            [-0.1058, -0.0002435, -0.000173, -0.00009921],
            [-0.03072, -0.0003188, -0.0002205, -0.0001212],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin=(300,'K'), 
        Tmax=(3000,'K'), 
        Pmin=(0.01,'bar'), 
        Pmax=(100,'bar')
    ),
    shortDesc=u"""FA2025""",
    longDesc=
    u"""
    From the pressure-dependent kinetic network of the singlet CH2O2 PES calculated at
    the CCSD(T)-F12/aug-cc-pVTZ-F12//B2PLYP-D3/def2-TZVP level of theory.    
    """,
)

entry(
    index=6,
    label="H2O + CO <=> DHC",
    kinetics = Chebyshev(
        coeffs = [
            [-16.32, 0.711, -0.05305, -0.00884],
            [20.51, 0.9595, -0.04531, -0.01125],
            [0.3948, 0.2292, 0.02868, 0.0001393],
            [-0.1414, -0.02865, 0.02227, 0.004465],
            [0.04388, -0.004205, 0.001356, 0.001804],
            [-0.006544, 0.0009985, 0.0007011, 0.0003122],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin=(300,'K'), 
        Tmax=(3000,'K'), 
        Pmin=(0.01,'bar'), 
        Pmax=(100,'bar')
    ),
    shortDesc=u"""FA2025""",
    longDesc=
    u"""
    From the pressure-dependent kinetic network of the singlet CH2O2 PES calculated at
    the CCSD(T)-F12/aug-cc-pVTZ-F12//B2PLYP-D3/def2-TZVP level of theory.    
    """,
)

entry(
    index=7,
    label="H + HOCO <=> DHC",
    kinetics = Chebyshev(
        coeffs = [
            [7.122, 1.952, -0.03219, -0.01699],
            [-2.268, 0.04953, 0.03308, 0.0171],
            [-0.7048, -0.009307, -0.005978, -0.002868],
            [-0.3166, -0.003328, -0.00234, -0.00132],
            [-0.168, -0.0004618, -0.0003502, -0.0002207],
            [-0.08127, -0.0005667, -0.0003872, -0.0002085],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin=(300,'K'), 
        Tmax=(3000,'K'), 
        Pmin=(0.01,'bar'), 
        Pmax=(100,'bar')
    ),
    shortDesc=u"""FA2025""",
    longDesc=
    u"""
    From the pressure-dependent kinetic network of the singlet CH2O2 PES calculated at
    the CCSD(T)-F12/aug-cc-pVTZ-F12//B2PLYP-D3/def2-TZVP level of theory.    
    """,
)

entry(
    index=8,
    label="H + OCHO <=> DHC",
    kinetics = Chebyshev(
        coeffs = [
            [14.32, 1.997, -0.002239, -0.00124],
            [-1.34, 0.001442, 0.001001, 0.0005534],
            [-0.1912, -0.001303, -0.0009037, -0.000499],
            [-0.04142, -0.0003955, -0.0002748, -0.0001522],
            [-0.04219, -0.0001095, -0.00007576, -0.00004162],
            [-0.02, -0.00006951, -0.00004803, -0.00002634],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin=(300,'K'), 
        Tmax=(3000,'K'), 
        Pmin=(0.01,'bar'), 
        Pmax=(100,'bar')
    ),
    shortDesc=u"""FA2025""",
    longDesc=
    u"""
    From the pressure-dependent kinetic network of the singlet CH2O2 PES calculated at
    the CCSD(T)-F12/aug-cc-pVTZ-F12//B2PLYP-D3/def2-TZVP level of theory.    
    """,
)

entry(
    index=9,
    label="H2 + CO2 <=> DHC",
    kinetics = Chebyshev(
        coeffs = [
            [-19.83, 0.652, -0.0194, -0.003509],
            [23.96, 1.099, -0.06154, -0.009495],
            [0.326, 0.3189, 0.0213, -0.01288],
            [-0.1497, -0.1112, 0.02932, 0.01057],
            [0.05797, -0.02494, -0.004921, 0.006388],
            [-0.00528, 0.001966, 0.004679, -0.002187],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin=(300,'K'), 
        Tmax=(3000,'K'), 
        Pmin=(0.01,'bar'), 
        Pmax=(100,'bar')
    ),
    shortDesc=u"""FA2025""",
    longDesc=
    u"""
    From the pressure-dependent kinetic network of the singlet CH2O2 PES calculated at
    the CCSD(T)-F12/aug-cc-pVTZ-F12//B2PLYP-D3/def2-TZVP level of theory.    
    """,
)

entry(
    index=10,
    label="OH + HCO <=> DHC",
    kinetics = Chebyshev(
        coeffs = [
            [9.986, 1.977, -0.01555, -0.008473],
            [-1.775, 0.01917, 0.01311, 0.007062],
            [-0.4947, -0.003316, -0.002234, -0.001173],
            [-0.1741, -0.001685, -0.001171, -0.0006478],
            [-0.1019, -0.0006591, -0.0004607, -0.0002576],
            [-0.06239, -0.0005773, -0.0003993, -0.0002195],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin=(300,'K'), 
        Tmax=(3000,'K'), 
        Pmin=(0.01,'bar'), 
        Pmax=(100,'bar')
    ),
    shortDesc=u"""FA2025""",
    longDesc=
    u"""
    From the pressure-dependent kinetic network of the singlet CH2O2 PES calculated at
    the CCSD(T)-F12/aug-cc-pVTZ-F12//B2PLYP-D3/def2-TZVP level of theory.    
    """,
)

entry(
    index=11,
    label="H + HOCO <=> H2O + CO",
    kinetics = Chebyshev(
        coeffs = [
            [11.62, -0.0402, -0.02707, -0.0142],
            [-2.084, 0.04523, 0.03015, 0.01553],
            [-0.9314, -0.006453, -0.00401, -0.001792],
            [-0.4501, -0.002296, -0.001628, -0.0009297],
            [-0.2005, 0.0000179, -0.00001805, -0.00003786],
            [-0.08484, -0.0002736, -0.0001841, -0.00009657],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin=(300,'K'), 
        Tmax=(3000,'K'), 
        Pmin=(0.01,'bar'), 
        Pmax=(100,'bar')
    ),
    shortDesc=u"""FA2025""",
    longDesc=
    u"""
    From the pressure-dependent kinetic network of the singlet CH2O2 PES calculated at
    the CCSD(T)-F12/aug-cc-pVTZ-F12//B2PLYP-D3/def2-TZVP level of theory.    
    """,
)

entry(
    index=12,
    label="H + OCHO <=> H2O + CO",
    kinetics = Chebyshev(
        coeffs = [
            [19.02, -0.000187, -0.0001299, -0.00007185],
            [-1.171, 0.0001307, 0.0000907, 0.00005013],
            [-0.3786, -0.00006145, -0.00004256, -0.00002344],
            [-0.1414, -0.00002084, -0.00001449, -0.000008026],
            [-0.05644, 0.000001293, 0.0000009187, 0.0000005269],
            [-0.01467, -0.000004377, -0.00000303, -0.000001667],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin=(300,'K'), 
        Tmax=(3000,'K'), 
        Pmin=(0.01,'bar'), 
        Pmax=(100,'bar')
    ),
    shortDesc=u"""FA2025""",
    longDesc=
    u"""
    From the pressure-dependent kinetic network of the singlet CH2O2 PES calculated at
    the CCSD(T)-F12/aug-cc-pVTZ-F12//B2PLYP-D3/def2-TZVP level of theory.    
    """,
)

entry(
    index=13,
    label="H2 + CO2 <=> H2O + CO",
    kinetics = Chebyshev(
        coeffs = [
            [-16.83, -1.009, -0.1218, 0.004345],
            [24.68, 0.9991, 0.02991, -0.0251],
            [0.2019, 0.1252, 0.09434, 0.004163],
            [-0.03739, -0.07801, 0.01424, 0.01375],
            [-0.02653, -0.0501, -0.01687, 0.002151],
            [-0.02236, -0.01356, -0.01116, -0.002793],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin=(300,'K'), 
        Tmax=(3000,'K'), 
        Pmin=(0.01,'bar'), 
        Pmax=(100,'bar')
    ),
    shortDesc=u"""FA2025""",
    longDesc=
    u"""
    From the pressure-dependent kinetic network of the singlet CH2O2 PES calculated at
    the CCSD(T)-F12/aug-cc-pVTZ-F12//B2PLYP-D3/def2-TZVP level of theory.    
    """,
)

entry(
    index=14,
    label="OH + HCO <=> H2O + CO",
    kinetics = Chebyshev(
        coeffs = [
            [14.62, -0.01874, -0.01287, -0.006992],
            [-1.68, 0.01837, 0.01255, 0.006759],
            [-0.7284, -0.001368, -0.0008837, -0.0004281],
            [-0.3016, -0.0008572, -0.000596, -0.0003302],
            [-0.1324, -0.0002546, -0.0001805, -0.0001033],
            [-0.06638, -0.0003249, -0.0002247, -0.0001234],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin=(300,'K'), 
        Tmax=(3000,'K'), 
        Pmin=(0.01,'bar'), 
        Pmax=(100,'bar')
    ),
    shortDesc=u"""FA2025""",
    longDesc=
    u"""
    From the pressure-dependent kinetic network of the singlet CH2O2 PES calculated at
    the CCSD(T)-F12/aug-cc-pVTZ-F12//B2PLYP-D3/def2-TZVP level of theory.    
    """,
)

entry(
    index=15,
    label="H + OCHO <=> H + HOCO",
    kinetics = Chebyshev(
        coeffs = [
            [15.74, -0.00005110, -0.00003556, -0.00001973],
            [-2.304, 0.00006780, 0.00004717, 0.00002617],
            [-0.5025, -0.00001445, -0.00001005, -0.000005575],
            [-0.1259, -0.000004860, -0.000003381, -0.000001876],
            [-0.03337, 0.000004344, 0.000003020, 0.000001674],
            [-0.004068, -0.000001114, -0.0000007750, -0.0000004298],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin=(300,'K'), 
        Tmax=(3000,'K'), 
        Pmin=(0.01,'bar'), 
        Pmax=(100,'bar')
    ),
    shortDesc=u"""FA2025""",
    longDesc=
    u"""
    From the pressure-dependent kinetic network of the singlet CH2O2 PES calculated at
    the CCSD(T)-F12/aug-cc-pVTZ-F12//B2PLYP-D3/def2-TZVP level of theory.    
    """,
)

entry(
    index=16,
    label="H2 + CO2 <=> H + HOCO",
    kinetics = Chebyshev(
        coeffs = [
            [-29.53, -0.04019, -0.02707, -0.0142],
            [32.11, 0.04516, 0.0301, 0.01551],
            [-0.8388, -0.006567, -0.004089, -0.001836],
            [-0.4164, -0.002302, -0.001633, -0.000933],
            [-0.1897, 0.00001976, -0.00001659, -0.0000369],
            [-0.08169, -0.0002816, -0.0001895, -0.00009936],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin=(300,'K'), 
        Tmax=(3000,'K'), 
        Pmin=(0.01,'bar'), 
        Pmax=(100,'bar')
    ),
    shortDesc=u"""FA2025""",
    longDesc=
    u"""
    From the pressure-dependent kinetic network of the singlet CH2O2 PES calculated at
    the CCSD(T)-F12/aug-cc-pVTZ-F12//B2PLYP-D3/def2-TZVP level of theory.    
    """,
)

entry(
    index=17,
    label="OH + HCO <=> H + HOCO",
    kinetics = Chebyshev(
        coeffs = [
            [10.84, -0.01816, -0.01248, -0.006779],
            [-3.293, 0.01813, 0.01239, 0.006677],
            [-1.132, -0.001064, -0.0006753, -0.0003159],
            [-0.4248, -0.0006782, -0.0004713, -0.0002608],
            [-0.1703, -0.0001173, -0.00008513, -0.00005043],
            [-0.07713, -0.0002142, -0.0001478, -0.0000809],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin=(300,'K'), 
        Tmax=(3000,'K'), 
        Pmin=(0.01,'bar'), 
        Pmax=(100,'bar')
    ),
    shortDesc=u"""FA2025""",
    longDesc=
    u"""
    From the pressure-dependent kinetic network of the singlet CH2O2 PES calculated at
    the CCSD(T)-F12/aug-cc-pVTZ-F12//B2PLYP-D3/def2-TZVP level of theory.    
    """,
)

entry(
    index=18,
    label="H2 + CO2 <=> H + OCHO",
    kinetics = Chebyshev(
        coeffs = [
            [-27.38, -0.0002866, -0.000199, -0.0001100],
            [36.27, 0.0001673, 0.0001160, 0.00006404],
            [-0.4730, -0.0001037, -0.00007183, -0.00003954],
            [-0.1704, -0.00003458, -0.00002404, -0.00001332],
            [-0.06662, -0.000003033, -0.000002076, -0.000001121],
            [-0.01812, -0.000006496, -0.000004493, -0.000002468],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin=(300,'K'), 
        Tmax=(3000,'K'), 
        Pmin=(0.01,'bar'), 
        Pmax=(100,'bar')
    ),
    shortDesc=u"""FA2025""",
    longDesc=
    u"""
    From the pressure-dependent kinetic network of the singlet CH2O2 PES calculated at
    the CCSD(T)-F12/aug-cc-pVTZ-F12//B2PLYP-D3/def2-TZVP level of theory.    
    """,
)

entry(
    index=19,
    label="OH + HCO <=> H + OCHO",
    kinetics = Chebyshev(
        coeffs = [
            [16.67, -0.00001718, -0.00001195, -0.000006631],
            [0.5377, 0.00002599, 0.00001808, 0.00001003],
            [0.08324, -0.00001008, -0.000007013, -0.000003891],
            [0.04499, 0.000000264, 0.0000001835, 0.0000001016],
            [0.01633, 0.000001546, 0.000001075, 0.0000005963],
            [0.006718, -0.0000003296, -0.0000002292, -0.0000001270],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin=(300,'K'), 
        Tmax=(3000,'K'), 
        Pmin=(0.01,'bar'), 
        Pmax=(100,'bar')
    ),
    shortDesc=u"""FA2025""",
    longDesc=
    u"""
    From the pressure-dependent kinetic network of the singlet CH2O2 PES calculated at
    the CCSD(T)-F12/aug-cc-pVTZ-F12//B2PLYP-D3/def2-TZVP level of theory.    
    """,
)

entry(
    index=20,
    label="OH + HCO <=> H2 + CO2",
    kinetics = Chebyshev(
        coeffs = [
            [13.59, -0.01884, -0.01294, -0.007032],
            [-1.678, 0.01838, 0.01256, 0.006763],
            [-0.7243, -0.001424, -0.0009219, -0.0004491],
            [-0.3006, -0.0008813, -0.0006127, -0.0003394],
            [-0.1330, -0.0002660, -0.0001884, -0.0001076],
            [-0.06674, -0.0003317, -0.0002294, -0.0001260],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin=(300,'K'), 
        Tmax=(3000,'K'), 
        Pmin=(0.01,'bar'), 
        Pmax=(100,'bar')
    ),
    shortDesc=u"""FA2025""",
    longDesc=
    u"""
    From the pressure-dependent kinetic network of the singlet CH2O2 PES calculated at
    the CCSD(T)-F12/aug-cc-pVTZ-F12//B2PLYP-D3/def2-TZVP level of theory.    
    """,
)

entry(
    index=21,
    label="OH + CO <=> OCHO",
    kinetics = Chebyshev(
        coeffs = [
            [5.388, 1.727, -0.1527, -0.05968],
            [2.432, 0.1733, 0.07411, 0.01318],
            [0.3921, -0.04661, -0.01441, 0.001791],
            [0.01330, 0.001915, -0.0002359, -0.0008834],
            [-0.02258, 0.009316, 0.003324, 0.0004467],
            [-0.01378, -0.003906, -0.0004662, 0.0005825],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (300, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.01, 'bar'),
        Pmax = (100, 'bar'),
    ),
    shortDesc=u"""FA2025""",
    longDesc=
    u"""
    Calculated based on Nguyen's HEAT protocal.   
    """,
)

entry(
    index=22,
    label="H + CO2 <=> OCHO",
    kinetics = Chebyshev(
        coeffs = [
            [4.637, 1.908, -0.02671, -0.01287],
            [4.796, 0.08414, 0.01357, 0.006043],
            [-0.08730, -0.002177, 0.004252, 0.001830],
            [-0.03090, -0.002453, 0.001155, 0.0005792],
            [-0.04060, 0.002115, 0.001512, 0.0007442],
            [-0.01958, -0.0009371, -0.00007545, -0.00009391],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (300, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.01, 'bar'),
        Pmax = (100, 'bar'),
    ),
    shortDesc=u"""FA2025""",
    longDesc=
    u"""
    Calculated based on Nguyen's HEAT protocal.  
    """,
)

entry(
    index=23,
    label="H + CO2 <=> OH + CO",
    kinetics = Chebyshev(
        coeffs = [
            [3.059, -0.4682, -0.2248, -0.06454],
            [8.829, 0.3524, 0.1352, 0.01461],
            [0.1047, -0.001557, 0.005639, 0.004925],
            [0.01399, -0.03095, -0.008608, 0.0005584],
            [0.01784, 0.006885, 0.0002928, -0.0006501],
            [0.0003425, -0.003347, -0.0001403, 0.0003884],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (300, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.01, 'bar'),
        Pmax = (100, 'bar'),
    ),
    shortDesc=u"""FA2025""",
    longDesc=
    u"""
    Calculated based on Nguyen's HEAT protocal.
    """,
)

entry(
    index=24,
    label="OCHO <=> HOCO",
    kinetics = Chebyshev(
        coeffs=[
            [0.420904,2.57537,0.122185,-0.0347698],
            [3.58675,1.71885,-0.232939,-0.0228968],
            [0.64999,-0.293929,-0.0209092,0.0510844],
            [-0.0172581,-0.175944,0.0797736,-0.0274859],
            [-0.106711,0.0267121,-0.0103067,-0.00999137],
            [-0.0910028,0.0427277,-0.0124742,0.0123547]], 
        kunits='1/s', 
        Tmin=(300,'K'), 
        Tmax=(3000,'K'), 
        Pmin=(0.01,'bar'), 
        Pmax=(100,'bar')
        ),
    shortDesc=u"""FA2025""",
    longDesc=
    u"""
    Calculated based on Nguyen's HEAT protocal.
    """,
)

entry(
    index=25,
    label="OH + CO <=> HOCO",
    kinetics = Chebyshev(
        coeffs=[
            [10.1179,1.31016,-0.294335,-0.0623058],
            [-0.209461,0.426599,0.143929,0.00526051],
            [-0.141944,0.0518631,0.0213173,0.00335184],
            [0.00848119,-0.0199697,-5.42516e-05,0.00254578],
            [-0.0427365,0.0131247,0.00219256,-0.000506071],
            [-0.0140018,3.15098e-07,0.00127432,0.000548326]], 
        kunits='cm^3/(mol*s)', 
        Tmin=(300,'K'), 
        Tmax=(3000,'K'), 
        Pmin=(0.01,'bar'), 
        Pmax=(100,'bar')
        ),
    shortDesc=u"""FA2025""",
    longDesc=
    u"""
    Calculated based on Nguyen's HEAT protocal.
    """,
)

entry(
    index=26,
    label="H + CO2 <=> HOCO",
    kinetics = Chebyshev(
        coeffs=[
            [3.4677,0.606341,-0.0530739,0.000119584],
            [5.85303,0.82429,-0.0432387,-0.00493425],
            [0.182803,0.227552,0.02043,-0.00698013],
            [-0.201013,0.0109382,0.0146266,-0.0029227],
            [-0.0326655,0.0159478,-0.00017484,-0.000757879],
            [-0.0142236,0.0138451,-0.00155517,-0.000505843]], 
        kunits='cm^3/(mol*s)', 
        Tmin=(300,'K'), 
        Tmax=(3000,'K'), 
        Pmin=(0.01,'bar'), 
        Pmax=(100,'bar')
        ),
    shortDesc=u"""FA2025""",
    longDesc=
    u"""
    Based on Nguyen's HEAT protocal.   
    """,
)

entry(
    index=27,
    label = 'HOCHO + OH <=> HOCO + H2O', 
    kinetics = Arrhenius(
        A = (30703.2, 'cm^3/(mol*s)'),
        n = 2.52013,
        Ea = (29.3851, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc=u"""CCSD(T)-F12/aug-cc-pVTZ-F12//B2PLYP-D3/def2-TZVP""",
    longDesc=
    u"""
    Calculated at the CCSD(T)-F12/aug-cc-pVTZ-F12//B2PLYP-D3/def2-TZVP level of theory.
    """,
)

entry(
    index=28,
    label = 'HOCHO + OH <=> OCHO + H2O', 
    kinetics = Arrhenius(
        A = (0.0765648, 'cm^3/(mol*s)'),
        n = 4.05778,
        Ea = (41.3556, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc=u"""CCSD(T)-F12/aug-cc-pVTZ-F12//B2PLYP-D3/def2-TZVP""",
    longDesc=
    u"""
    Calculated at the CCSD(T)-F12/aug-cc-pVTZ-F12//B2PLYP-D3/def2-TZVP level of theory.
    H_abs reaction, ARC couldn't caluclate the reversed reaction rate.   
    """,
)