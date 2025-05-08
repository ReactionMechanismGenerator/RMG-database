#!/usr/bin/env python
# encoding: utf-8

name = "FA2025"
shortDesc = u""
longDesc = u"""

"""
entry(
    index=1,
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
    index=2,
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
    index=3,
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
    index=4,
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
    index=5,
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
    index=6,
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
    index=7,
    label="DHC <=> HOCHO",
    kinetics = Chebyshev(
        coeffs = [
            [-0.2356, 1.312, -0.1004, -0.01986],
            [6.933, 1.672, -0.06118, -0.0285],
            [-0.08348, 0.312, 0.05804, 0.002357],
            [-0.4065, -0.07591, 0.01701, 0.01092],
            [-0.04935, -0.008376, -0.01196, 0.001186],
            [-0.005589, -0.001824, -0.003267, -0.0004731],
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
    index=8,
    label="H2O + CO <=> HOCHO",
    kinetics = Chebyshev(
        coeffs = [
            [-13.16, 0.7318, -0.1133, 0.001098],
            [18.6, 0.9495, -0.07393, -0.01476],
            [0.2438, 0.2118, 0.08228, -0.01592],
            [-0.2838, -0.0195, 0.04515, 0.005777],
            [0.02699, -0.0214, -0.004309, 0.008237],
            [-0.003118, -0.02063, -0.005772, 0.000837],
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
    label="H + HOCO <=> HOCHO",
    kinetics = Chebyshev(
        coeffs = [
            [8.813, 1.966, -0.02288, -0.01212],
            [-2.836, 0.03771, 0.02532, 0.01321],
            [-1.037, -0.005686, -0.003621, -0.001705],
            [-0.4081, -0.002276, -0.001605, -0.0009088],
            [-0.1448, -0.0002298, -0.0001797, -0.0001179],
            [-0.03898, -0.0002603, -0.0001776, -9.539e-05],
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
    label="H + OCHO <=> HOCHO",
    kinetics = Chebyshev(
        coeffs = [
            [15.92, 2.0, -4.807e-05, -2.667e-05],
            [-1.89, 8.135e-05, 5.659e-05, 3.14e-05],
            [-0.5479, -1.346e-05, -9.36e-06, -5.189e-06],
            [-0.1542, -6.692e-06, -4.655e-06, -2.582e-06],
            [-0.03072, 4.761e-06, 3.311e-06, 1.835e-06],
            [0.01682, -2.614e-06, -1.819e-06, -1.009e-06],
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
    label="H2 + CO2 <=> HOCHO",
    kinetics = Chebyshev(
        coeffs = [
            [-11.61, 0.4107, -0.05204, 0.001297],
            [17.5, 0.6713, -0.06798, -0.001057],
            [1.112, 0.3515, -0.001517, -0.005535],
            [-0.4769, 0.0946, 0.02961, -0.003149],
            [-0.1662, -0.00678, 0.01801, 0.002105],
            [0.06211, -0.01546, 0.0002729, 0.002985],
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
    label="OH + HCO <=> HOCHO",
    kinetics = Chebyshev(
        coeffs = [
            [11.58, 1.984, -0.01079, -0.005883],
            [-2.279, 0.01542, 0.01057, 0.005716],
            [-0.8214, -0.001615, -0.001072, -0.000548],
            [-0.2693, -0.000967, -0.000673, -0.0003735],
            [-0.08004, -0.0003324, -0.0002337, -0.0001318],
            [-0.01976, -0.0002941, -0.0002038, -0.0001123],
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
    label="H2O + CO <=> DHC",
    kinetics = Chebyshev(
        coeffs = [
            [-16.36, 0.7484, -0.06015, -0.008612],
            [20.48, 0.9762, -0.04118, -0.01234],
            [0.4026, 0.1975, 0.03933, 0.001081],
            [-0.1345, -0.04175, 0.02003, 0.006116],
            [0.04622, -0.00384, -0.002386, 0.001159],
            [-0.003537, 0.001566, 0.0001021, -0.0005531],
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
    label="H + HOCO <=> DHC",
    kinetics = Chebyshev(
        coeffs = [
            [7.044, 1.96, -0.02726, -0.01455],
            [-2.265, 0.04111, 0.02767, 0.01452],
            [-0.7044, -0.009089, -0.005973, -0.002997],
            [-0.317, -0.003169, -0.002228, -0.001256],
            [-0.1681, -0.0005862, -0.0004257, -0.0002524],
            [-0.08123, -0.0005528, -0.0003792, -0.0002055],
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
    label="H + OCHO <=> DHC",
    kinetics = Chebyshev(
        coeffs = [
            [14.32, 1.997, -0.002237, -0.001239],
            [-1.34, 0.001439, 0.0009992, 0.0005523],
            [-0.1912, -0.001303, -0.0009042, -0.0004993],
            [-0.04142, -0.0003955, -0.0002749, -0.0001522],
            [-0.04218, -0.0001099, -7.597e-05, -4.173e-05],
            [-0.02002, -6.926e-05, -4.785e-05, -2.624e-05],
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
    label="H2 + CO2 <=> DHC",
    kinetics = Chebyshev(
        coeffs = [
            [-19.03, 0.1371, -0.06868, 0.01575],
            [23.85, 1.497, -0.09968, -0.05925],
            [0.07659, 0.3313, 0.1422, 0.01694],
            [-0.163, -0.1262, -0.02241, 0.01664],
            [0.01338, 0.01294, -0.002797, -0.007617],
            [-0.01762, -0.01349, 0.00326, 0.005047],
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
    label="OH + HCO <=> DHC",
    kinetics = Chebyshev(
        coeffs = [
            [9.921, 1.98, -0.01351, -0.007385],
            [-1.778, 0.01615, 0.01107, 0.005996],
            [-0.4953, -0.00361, -0.002456, -0.001312],
            [-0.1739, -0.001818, -0.001264, -0.0007],
            [-0.1015, -0.0007466, -0.0005205, -0.0002897],
            [-0.06223, -0.0005516, -0.0003819, -0.0002102],
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
    label="H + HOCO <=> H2O + CO",
    kinetics = Chebyshev(
        coeffs = [
            [11.55, -0.03284, -0.02225, -0.01181],
            [-2.081, 0.03693, 0.02481, 0.01297],
            [-0.9312, -0.006152, -0.003948, -0.00189],
            [-0.4506, -0.002147, -0.001521, -0.0008671],
            [-0.2006, -0.0001243, -0.0001058, -7.642e-05],
            [-0.08479, -0.0002634, -0.0001789, -9.534e-05],
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
    label="H + OCHO <=> H2O + CO",
    kinetics = Chebyshev(
        coeffs = [
            [19.02, -0.0001843, -0.0001280, -0.00007081],
            [-1.171, 0.0001278, 0.00008871, 0.00004903],
            [-0.3786, -0.00006204, -0.00004297, -0.00002367],
            [-0.1414, -0.00002085, -0.00001450, -0.000008032],
            [-0.05643, 0.000001024, 7.314e-07, 4.232e-07],
            [-0.01469, -0.000004143, -0.000002867, -0.000001576],
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
    label="H2 + CO2 <=> H2O + CO",
    kinetics = Chebyshev(
        coeffs = [
            [-15.43, -0.9728, -0.1509, 0.01017],
            [23.84, 0.9456, 0.04833, -0.03482],
            [0.1688, 0.1115, 0.1034, 0.003298],
            [-0.06766, -0.05972, 0.01066, 0.01651],
            [-0.03343, -0.04402, -0.01761, 0.002552],
            [-0.02114, -0.01484, -0.01094, -0.003242],
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
    label="OH + HCO <=> H2O + CO",
    kinetics = Chebyshev(
        coeffs = [
            [14.55, -0.01574, -0.01084, -0.005909],
            [-1.682, 0.01537, 0.01053, 0.005697],
            [-0.7289, -0.001665, -0.001107, -0.0005676],
            [-0.3013, -0.0009907, -0.0006893, -0.0003824],
            [-0.1320, -0.0003420, -0.0002402, -0.0001354],
            [-0.06619, -0.0002991, -0.0002072, -0.0001141],
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
    index=22,
    label="H + OCHO <=> H + HOCO",
    kinetics = Chebyshev(
        coeffs = [
            [15.74, -4.905e-05, -3.412e-05, -1.893e-05],
            [-2.304, 6.551e-05, 4.558e-05, 2.529e-05],
            [-0.5025, -1.451e-05, -1.009e-05, -5.596e-06],
            [-0.1259, -4.616e-06, -3.212e-06, -1.782e-06],
            [-0.03337, 4.207e-06, 2.926e-06, 1.622e-06],
            [-0.004076, -9.852e-07, -6.852e-07, -3.800e-07],
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
    index=23,
    label="H2 + CO2 <=> H + HOCO",
    kinetics = Chebyshev(
        coeffs = [
            [-29.06, -0.03291, -0.02230, -0.01183],
            [32.07, 0.03701, 0.02486, 0.01299],
            [-0.8415, -0.006049, -0.003876, -0.001849],
            [-0.4144, -0.002161, -0.001530, -0.0008713],
            [-0.1893, -0.0001348, -0.0001134, -8.076e-05],
            [-0.08169, -0.0002575, -0.0001750, -9.333e-05],
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
    index=24,
    label="OH + HCO <=> H + HOCO",
    kinetics = Chebyshev(
        coeffs = [
            [10.78, -0.01522, -0.01048, -0.005714],
            [-3.292, 0.01525, 0.01046, 0.005663],
            [-1.128, -0.001329, -0.0008762, -0.0004420],
            [-0.4212, -0.0007726, -0.0005375, -0.0002981],
            [-0.1671, -0.0001702, -0.0001208, -0.00006924],
            [-0.07465, -0.0001598, -0.0001104, -0.00006059],
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
    index=25,
    label="H2 + CO2 <=> H + OCHO",
    kinetics = Chebyshev(
        coeffs = [
            [-26.92, -1.412e-04, -9.808e-05, -5.429e-05],
            [36.23, 1.007e-04, 6.992e-05, 3.869e-05],
            [-0.4950, -4.831e-05, -3.349e-05, -1.846e-05],
            [-0.1833, -1.919e-05, -1.334e-05, -7.387e-06],
            [-0.07432, -3.569e-07, -2.327e-07, -1.149e-07],
            [-0.02223, -5.055e-06, -3.504e-06, -1.933e-06],
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
    index=26,
    label="OH + HCO <=> H + OCHO",
    kinetics = Chebyshev(
        coeffs = [
            [16.67, -1.654e-05, -1.151e-05, -6.385e-06],
            [0.5377, 2.510e-05, 1.746e-05, 9.688e-06],
            [0.08323, -9.845e-06, -6.849e-06, -3.800e-06],
            [0.04499, 3.334e-07, 2.318e-07, 1.284e-07],
            [0.01633, 1.475e-06, 1.026e-06, 5.690e-07],
            [0.006717, -3.201e-07, -2.226e-07, -1.234e-07],
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
    index=27,
    label="OH + HCO <=> H2 + CO2",
    kinetics = Chebyshev(
        coeffs = [
            [14.02, -1.569e-02, -1.080e-02, -5.889e-03],
            [-1.685, 1.536e-02, 1.053e-02, 5.697e-03],
            [-0.7257, -1.637e-03, -1.088e-03, -5.571e-04],
            [-0.3007, -9.787e-04, -6.810e-04, -3.779e-04],
            [-0.1329, -3.368e-04, -2.366e-04, -1.334e-04],
            [-0.06643, -2.959e-04, -2.050e-04, -1.129e-04],
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
    index=28,
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
    index=29,
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