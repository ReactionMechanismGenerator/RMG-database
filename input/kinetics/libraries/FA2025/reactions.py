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
    index=8,
    label="H2O + CO <=> HOCHO",
    kinetics = Chebyshev(
        coeffs = [
            [-13.01, 0.5493, -0.06648, -0.0007528],
            [18.73, 0.8176, -0.06179, -0.008216],
            [0.1737, 0.3255, 0.03136, -0.009101],
            [-0.3576, 0.05542, 0.03466, 0.001874],
            [-0.008352, -0.009932, 0.006160, 0.005114],
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
    index=9,
    label="H + HOCO <=> HOCHO",
    kinetics = Chebyshev(
        coeffs = [
            [8.892, 1.959, -0.02789, -0.01461],
            [-2.874, 0.04621, 0.03077, 0.01582],
            [-1.084, -0.005837, -0.003578, -0.001550],
            [-0.4483, -0.002429, -0.001712, -0.0009681],
            [-0.1706, -0.0001125, -0.0001092, -0.00008881],
            [-0.05004, -0.0002787, -0.0001888, -0.0001002],
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
            [15.92, 2.000, -0.00005052, -0.00002803],
            [-1.927, 0.00008546, 0.00005946, 0.00003299],
            [-0.5948, -0.00001273, -0.000008851, -0.000004906],
            [-0.1942, -0.000006535, -0.000004546, -0.000002521],
            [-0.05613, 0.000005313, 0.000003694, 0.000002047],
            [0.006021, -0.000002833, -0.000001971, -0.000001093],
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
    index=12,
    label="OH + HCO <=> HOCHO",
    kinetics = Chebyshev(
        coeffs = [
            [6.257, 2.000, -2.792e-09, -1.550e-09],
            [-0.9233, 4.343e-09, 3.023e-09, 1.678e-09],
            [-0.3803, -3.394e-10, -2.362e-10, -1.311e-10],
            [-0.1273, -2.112e-10, -1.470e-10, -8.162e-11],
            [-0.03026, -6.627e-12, -4.607e-12, -2.555e-12],
            [0.01311, -4.415e-11, -3.073e-11, -1.705e-11],
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
            [-16.32, 0.7110, -0.05305, -0.008839],
            [20.51, 0.9595, -0.04531, -0.01125],
            [0.3948, 0.2292, 0.02869, 0.0001402],
            [-0.1414, -0.02865, 0.02227, 0.004466],
            [0.04390, -0.004201, 0.001357, 0.001804],
            [-0.006536, 0.001000, 0.0007015, 0.0003123],
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
            [7.124, 1.952, -0.03219, -0.01700],
            [-2.265, 0.04952, 0.03307, 0.01710],
            [-0.7044, -0.009306, -0.005977, -0.002868],
            [-0.3172, -0.003320, -0.002335, -0.001317],
            [-0.1685, -0.0004574, -0.0003472, -0.0002191],
            [-0.08148, -0.0005683, -0.0003883, -0.0002091],
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
            [14.32, 1.997, -0.002240, -0.001240],
            [-1.340, 0.001443, 0.001002, 0.0005538],
            [-0.1912, -0.001303, -0.0009039, -0.0004991],
            [-0.04140, -0.0003956, -0.0002749, -0.0001522],
            [-0.04221, -0.0001094, -0.00007568, -0.00004157],
            [-0.01999, -0.00006956, -0.00004806, -0.00002635],
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
            [-19.83, 0.6520, -0.01940, -0.003508],
            [23.97, 1.099, -0.06153, -0.009494],
            [0.3260, 0.3189, 0.02130, -0.01288],
            [-0.1497, -0.1112, 0.02932, 0.01057],
            [0.05798, -0.02494, -0.004920, 0.006388],
            [-0.005273, 0.001965, 0.004679, -0.002187],
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
            [4.771, 1.998, -0.001417, -0.0007852],
            [-0.2949, 0.001202, 0.0008349, 0.0004620],
            [0.04091, -0.0007670, -0.0005326, -0.0002946],
            [0.03333, -0.0001653, -0.0001151, -0.00006392],
            [-0.01281, -0.00002560, -0.00001772, -0.000009742],
            [-0.01093, -0.00001752, -0.00001212, -0.000006658],
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
            [11.62, -0.04022, -0.02708, -0.01421],
            [-2.081, 0.04522, 0.03014, 0.01552],
            [-0.9312, -0.006450, -0.004008, -0.001791],
            [-0.4509, -0.002285, -0.001620, -0.0009254],
            [-0.2011, 0.00002244, -0.00001500, -0.00003627],
            [-0.08504, -0.0002766, -0.0001861, -0.00009768],
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
            [19.02, -0.0001877, -0.0001303, -0.00007211],
            [-1.172, 0.0001315, 0.00009132, 0.00005047],
            [-0.3786, -0.00006165, -0.00004270, -0.00002352],
            [-0.1413, -0.00002093, -0.00001455, -0.000008061],
            [-0.05645, 0.000001406, 0.0000009968, 0.0000005702],
            [-0.01466, -0.000004405, -0.000003049, -0.000001677],
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
            [-16.83, -1.009, -0.1218, 0.004346],
            [24.68, 0.9991, 0.02992, -0.02510],
            [0.2021, 0.1252, 0.09434, 0.004165],
            [-0.03730, -0.07801, 0.01425, 0.01375],
            [-0.02648, -0.05011, -0.01687, 0.002150],
            [-0.02234, -0.01357, -0.01116, -0.002794],
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
            [9.613, -0.00008800, -0.00006112, -0.00003381],
            [-0.08011, 0.00004696, 0.00003254, 0.00001794],
            [-0.1295, -0.00003350, -0.00002323, -0.00001281],
            [-0.06012, -0.000008243, -0.000005742, -0.000003193],
            [-0.02490, -0.000001419, -0.0000009823, -0.0000005407],
            [-0.004674, -0.0000009317, -0.0000006442, -0.0000003537],
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
            [15.74, -0.00005162, -0.00003592, -0.00001993],
            [-2.304, 0.00006853, 0.00004768, 0.00002645],
            [-0.5025, -0.00001465, -0.00001019, -0.000005650],
            [-0.1259, -0.000004927, -0.000003428, -0.000001902],
            [-0.03338, 0.000004433, 0.000003083, 0.000001709],
            [-0.004062, -0.000001131, -0.0000007866, -0.0000004362],
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
            [-29.53, -0.04021, -0.02708, -0.01421],
            [32.11, 0.04514, 0.03009, 0.01550],
            [-0.8386, -0.006564, -0.004087, -0.001835],
            [-0.4172, -0.002290, -0.001625, -0.0009285],
            [-0.1903, 0.00002429, -0.00001355, -0.00003532],
            [-0.08189, -0.0002848, -0.0001917, -0.0001006],
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
            [6.901, -2.905e-09, -2.022e-09, -1.123e-09],
            [-1.219, 3.623e-09, 2.522e-09, 1.400e-09],
            [-0.3153, -5.510e-10, -3.835e-10, -2.129e-10],
            [-0.09406, -1.974e-10, -1.374e-10, -7.630e-11],
            [-0.03192, 2.004e-11, 1.395e-11, 7.743e-12],
            [-0.007052, -8.888e-12, -6.186e-12, -3.434e-12],
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
            [-27.38, -0.0002873, -0.0001995, -0.0001103],
            [36.27, 0.0001682, 0.0001166, 0.00006437],
            [-0.4730, -0.0001039, -0.00007197, -0.00003962],
            [-0.1704, -0.00003467, -0.00002410, -0.00001335],
            [-0.06663, -0.000002921, -0.000001998, -0.000001077],
            [-0.01811, -0.000006523, -0.000004512, -0.000002479],
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
            [16.73, -1.996e-09, -1.389e-09, -7.712e-10],
            [0.4512, 2.636e-09, 1.834e-09, 1.019e-09],
            [0.1172, -5.732e-10, -3.990e-10, -2.215e-10],
            [0.04059, -1.113e-10, -7.745e-11, -4.301e-11],
            [0.01581, 4.041e-11, 2.813e-11, 1.562e-11],
            [0.006570, -1.459e-12, -1.015e-12, -5.636e-13],
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
            [8.627, -0.0001696, -0.0001178, -0.00006516],
            [-0.05488, 0.00008533, 0.00005913, 0.00003259],
            [-0.1122, -0.00006604, -0.00004579, -0.00002526],
            [-0.05204, -0.00001731, -0.00001205, -0.000006701],
            [-0.02164, -0.000003755, -0.000002603, -0.000001436],
            [-0.002912, -0.000002168, -0.000001501, -0.0000008260],
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
    label = 'HOCHO + H <=> HOCO + H2', 
    kinetics = Arrhenius(
        A = (2797.48, 'cm^3/(mol*s)'),
        n = 3.068,
        Ea = (51.1098, 'kJ/mol'),
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
    index=30,
    label = 'HOCHO + H <=> OCHO + H2', 
    kinetics = Arrhenius(
        A = (3.81289e+06, 'cm^3/(mol*s)'),
        n = 2.26614,
        Ea = (89.9775, 'kJ/mol'),
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

entry(
    index=31,
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