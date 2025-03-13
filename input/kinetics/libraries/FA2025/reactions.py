#!/usr/bin/env python
# encoding: utf-8

name = "FA2025"
shortDesc = u""
longDesc = u"""

"""
entry(
    index=1,
    label="OH + CO <=> OCHO",
    # duplicate=True,
    kinetics = Chebyshev(
        coeffs = [
            [4.3144, 2.16685, -0.191872, -0.0754371],
            [2.71074, 0.310411, 0.15135, 0.0344218],
            [0.698371, -0.0868949, -0.0366576, -0.00322531],
            [0.0822985, -0.0124795, -0.00774385, -0.00272848],
            [0.0516165, 0.0134097, 0.00614428, 0.000892738],
            [0.0396562, 0.00378249, 0.00188146, 0.000408778],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (200, 'K'),
        Tmax = (3500, 'K'),
        Pmin = (0.001, 'bar'),
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
    # duplicate=True,
    kinetics = Chebyshev(
        coeffs = [
            [1.50522, 2.33967, -0.033188, -0.0176838],
            [7.62178, 0.160091, 0.0163864, 0.00816226],
            [-0.184695, 1.81955e-05, 0.00970307, 0.00473321],
            [-0.0744726, -0.0011671, 0.0042209, 0.00219901],
            [0.0333992, -0.00544072, -0.0025601, -0.00110414],
            [0.0250803, -0.00273038, -0.00151603, -0.000533905],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (200, 'K'),
        Tmax = (3500, 'K'),
        Pmin = (0.001, 'bar'),
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
    # duplicate=True,
    kinetics = Chebyshev(
        coeffs = [
            [-1.46297, -0.476331, -0.259657, -0.0884551],
            [13.5945, 0.396521, 0.186427, 0.0366261],
            [0.135265, -0.00889128, 0.0046469, 0.00811368],
            [0.0525983, -0.0158211, -0.00688472, -0.000532276],
            [0.023796, -0.00178191, -0.000983392, -0.000202166],
            [0.0133096, 0.00333609, 0.00113239, -3.05019e-05],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (200, 'K'),
        Tmax = (3500, 'K'),
        Pmin = (0.001, 'bar'),
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
    # duplicate=True,
    kinetics = Chebyshev(
        coeffs=[
            [6.58394,4.14886,-0.388135,-0.0803019],
            [-1.28515,0.50893,0.204486,0.0187442],
            [-0.480447,0.0892484,0.0450583,0.00947765],
            [-0.194321,0.0355073,0.0146188,0.00117895],
            [-0.113036,0.0242455,0.00644526,-0.00143275],
            [-0.054565,0.0190498,0.00604817,-0.000912222]], 
        kunits='1/s', 
        Tmin=(200,'K'), 
        Tmax=(3500,'K'), 
        Pmin=(0.001,'bar'), 
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
    # duplicate=True,
    kinetics = Chebyshev(
        coeffs=[
            [9.76826,1.85531,-0.331084,-0.0954915],
            [-0.269939,0.423631,0.188067,0.0282622],
            [-0.141954,0.0441295,0.0278617,0.0104283],
            [-0.0689165,0.0139601,0.00731867,0.00208372],
            [-0.123684,0.0140781,0.00617378,0.000968709],
            [-0.0248549,0.0122604,0.00463306,0.000142529]], 
        kunits='cm^3/(mol*s)', 
        Tmin=(200,'K'), 
        Tmax=(3500,'K'), 
        Pmin=(0.001,'bar'), 
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
    # duplicate=True,
    kinetics = Chebyshev(
        coeffs=[
            [1.19718,0.652264,-0.0555182,-0.00417684],
            [7.22575,1.04709,-0.0611236,-0.0057369],
            [0.996493,0.476073,0.00780211,-0.00659928],
            [-0.282335,0.0792554,0.0339519,-0.00270462],
            [-0.231326,-0.00680381,0.0184806,0.000815143],
            [-0.0224118,0.0121531,-0.00384774,-0.00218397]], 
        kunits='cm^3/(mol*s)', 
        Tmin=(200,'K'), 
        Tmax=(3500,'K'), 
        Pmin=(0.001,'bar'), 
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
    # duplicate=True,
    kinetics = Chebyshev(
        coeffs = [
            [-2.87371, 0.850045, -0.0338471, -0.0209988],
            [9.1246, 1.37394, -0.0397108, -0.0320743],
            [1.05759, 0.678156, 0.00955695, -0.0107424],
            [-0.537326, 0.132108, 0.0264001, 0.00538895],
            [-0.398891, -0.0449216, 0.00838438, 0.00805344],
            [-0.0495276, -0.0138136, -0.00837503, 0.00301241],
        ],
        kunits = 's^-1',
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.01, 'bar'),
        Pmax = (100, 'bar'),
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
    # duplicate=True,
    kinetics = Chebyshev(
        coeffs = [
            [-21.6751, 0.42692, -0.0493726, -0.00113116],
            [26.1863, 0.721593, -0.0668592, -0.00477213],
            [1.76942, 0.424907, -0.00404361, -0.00763168],
            [-0.455569, 0.156743, 0.0326864, -0.00465252],
            [-0.357562, 0.0208238, 0.0269964, 0.00175124],
            [0.0453817, -0.0125325, 0.00634136, 0.00455498],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.01, 'bar'),
        Pmax = (100, 'bar'),
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
    # duplicate=True,
    kinetics = Chebyshev(
        coeffs = [
            [9.58121, 1.93187, -0.0448922, -0.0226526],
            [-2.96515, 0.0736932, 0.0477807, 0.0233747],
            [-1.24808, -0.00333071, -0.00133646, 0.000130228],
            [-0.613647, -0.00426453, -0.00291272, -0.00156156],
            [-0.29612, -0.0019128, -0.0013357, -0.000745708],
            [-0.134903, 0.000216329, 0.000103264, 1.44854e-05],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.01, 'bar'),
        Pmax = (100, 'bar'),
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
    # duplicate=True,
    kinetics = Chebyshev(
        coeffs = [
            [16.4255, 1.99988, -8.66805e-05, -4.80792e-05],
            [-2.07077, 0.000151101, 0.000105096, 5.8281e-05],
            [-0.731465, -2.65874e-05, -1.84727e-05, -1.02259e-05],
            [-0.307652, 1.8544e-06, 1.27918e-06, 6.99646e-07],
            [-0.113141, -1.06565e-05, -7.40784e-06, -4.10423e-06],
            [-0.0424272, 5.27703e-06, 3.66859e-06, 2.03279e-06],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.01, 'bar'),
        Pmax = (100, 'bar'),
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
    # duplicate=True,
    kinetics = Chebyshev(
        coeffs = [
            [-23.2647, 0.408814, -0.0334878, -0.00535858],
            [26.7105, 0.711613, -0.0492294, -0.00936619],
            [2.28905, 0.456861, -0.0103781, -0.00570787],
            [0.127372, 0.191821, 0.0202763, -0.00104179],
            [-0.483454, 0.0252859, 0.0252136, 0.00264465],
            [-0.226305, -0.0264557, 0.0109024, 0.00379773],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.01, 'bar'),
        Pmax = (100, 'bar'),
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
    label="H2O + CO <=> DHC",
    # duplicate=True,
    kinetics = Chebyshev(
        coeffs = [
            [-26.189, 0.546554, -0.0390953, -0.00680951],
            [29.328, 0.878994, -0.0512818, -0.0105133],
            [1.64736, 0.422258, 0.000167698, -0.00366018],
            [-0.211015, 0.0662012, 0.0266907, 0.00198147],
            [-0.165485, -0.0425872, 0.0177651, 0.00349848],
            [0.071464, -0.0134652, 0.00128152, 0.00194351],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.01, 'bar'),
        Pmax = (100, 'bar'),
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
    label="H + HOCO <=> DHC",
    # duplicate=True,
    kinetics = Chebyshev(
        coeffs = [
            [7.75551, 1.9202, -0.0529664, -0.027087],
            [-2.48134, 0.0849599, 0.0555377, 0.0276036],
            [-0.847136, -0.00818383, -0.00465588, -0.0016593],
            [-0.395399, -0.00578939, -0.00398374, -0.00216493],
            [-0.21531, -0.0025231, -0.00176023, -0.000981186],
            [-0.136266, 2.20842e-05, -3.0657e-05, -5.8714e-05],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.01, 'bar'),
        Pmax = (100, 'bar'),
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
    label="H + OCHO <=> DHC",
    # duplicate=True,
    kinetics = Chebyshev(
        coeffs = [
            [14.7816, 1.99472, -0.00366264, -0.00202284],
            [-1.62572, 0.00436027, 0.00301974, 0.00166271],
            [-0.319135, -0.0017518, -0.00121133, -0.000665236],
            [-0.0684795, -0.000594421, -0.000414229, -0.000230428],
            [-0.0161269, -0.000291736, -0.000202335, -0.000111676],
            [-0.0341879, -5.80201e-05, -4.00739e-05, -2.19657e-05],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.01, 'bar'),
        Pmax = (100, 'bar'),
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
    label="H2 + CO2 <=> DHC",
    # duplicate=True,
    kinetics = Chebyshev(
        coeffs = [
            [-31.667, 0.522897, -0.019709, -0.00302859],
            [34.7849, 0.914974, -0.0397511, -0.00717651],
            [1.56329, 0.540395, -0.0183491, -0.00875676],
            [-0.232004, 0.101217, 0.0218444, -0.00450443],
            [-0.180387, -0.110002, 0.0274342, 0.00565735],
            [0.0866223, -0.0583163, -0.000422565, 0.00893891],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.01, 'bar'),
        Pmax = (100, 'bar'),
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
    label="H + HOCO <=> H2O + CO",
    # duplicate=True,
    kinetics = Chebyshev(
        coeffs = [
            [12.0864, -0.0671522, -0.0442775, -0.0223677],
            [-2.08567, 0.0734853, 0.0476957, 0.0233805],
            [-0.995704, -0.00427452, -0.00197494, -0.000207113],
            [-0.565771, -0.00448205, -0.00307373, -0.0016596],
            [-0.313242, -0.00175388, -0.00123237, -0.000694984],
            [-0.160288, 0.000353816, 0.000199452, 6.82881e-05],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.01, 'bar'),
        Pmax = (100, 'bar'),
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
    label="H + OCHO <=> H2O + CO",
    # duplicate=True,
    kinetics = Chebyshev(
        coeffs = [
            [19.3338, -0.000310804, -0.000215444, -0.000118806],
            [-1.26553, 0.000298356, 0.000206485, 0.000113562],
            [-0.447474, -8.97436e-05, -6.18764e-05, -3.38169e-05],
            [-0.205352, -2.02704e-05, -1.41693e-05, -7.92176e-06],
            [-0.0889385, -2.1902e-05, -1.51907e-05, -8.38478e-06],
            [-0.0434277, 3.93461e-06, 2.74333e-06, 1.52741e-06],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.01, 'bar'),
        Pmax = (100, 'bar'),
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
    label="H2 + CO2 <=> H2O + CO",
    # duplicate=True,
    kinetics = Chebyshev(
        coeffs = [
            [-29.93, -1.26183, -0.0807457, 0.00183216],
            [37.3409, 1.04695, -0.0467202, -0.0116431],
            [0.741089, 0.334196, 0.0825994, -0.0129043],
            [-0.152316, -0.0157214, 0.059837, 0.0087312],
            [0.0346726, -0.0707432, 0.00297817, 0.0118106],
            [-0.0494529, -0.044082, -0.0152136, 0.0022522],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.01, 'bar'),
        Pmax = (100, 'bar'),
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
    label="H + OCHO <=> H + HOCO",
    # duplicate=True,
    kinetics = Chebyshev(
        coeffs = [
            [16.4755, -0.000100954, -7.02252e-05, -3.89506e-05],
            [-2.67493, 0.000132114, 9.18909e-05, 5.09587e-05],
            [-0.69499, -2.90749e-05, -2.02075e-05, -1.11921e-05],
            [-0.230913, 1.43954e-06, 9.91127e-07, 5.40367e-07],
            [-0.0694769, -7.98601e-06, -5.55096e-06, -3.07499e-06],
            [-0.0249574, 5.0333e-06, 3.49964e-06, 1.93963e-06],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.01, 'bar'),
        Pmax = (100, 'bar'),
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
    label="H2 + CO2 <=> H + HOCO",
    # duplicate=True,
    kinetics = Chebyshev(
        coeffs = [
            [-47.9914, -0.067232, -0.0443375, -0.0224048],
            [50.9791, 0.0735858, 0.0477691, 0.0234243],
            [-0.890529, -0.00443737, -0.00208514, -0.000265397],
            [-0.513974, -0.00453028, -0.00310844, -0.0016799],
            [-0.291291, -0.0017508, -0.00123088, -0.00069476],
            [-0.152395, 0.000359174, 0.000203332, 7.05739e-05],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.01, 'bar'),
        Pmax = (100, 'bar'),
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
    label="H2 + CO2 <=> H + OCHO",
    # duplicate=True,
    kinetics = Chebyshev(
        coeffs = [
            [-47.9671, -0.00047171, -0.000326764, -0.000179993],
            [57.1419, 0.000423939, 0.000292991, 0.000160765],
            [-0.577183, -0.000146064, -0.000100624, -5.49152e-05],
            [-0.250356, -4.0059e-05, -2.79863e-05, -1.56325e-05],
            [-0.106481, -3.16949e-05, -2.19762e-05, -1.21242e-05],
            [-0.0517872, 1.15012e-06, 8.14878e-07, 4.65548e-07],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.01, 'bar'),
        Pmax = (100, 'bar'),
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
    label="CHO + OH <=> HOCHO",
    # duplicate=True,
    kinetics = Chebyshev(
        coeffs = [
            [12.76, 1.985, -0.01045, -0.005674],
            [-1.208, 0.01794, 0.01229, 0.006641],
            [-0.6302, -0.001956, -0.001297, -0.0006609],
            [-0.2888, -0.0009004, -0.0006287, -0.0003508],
            [-0.1224, -0.0002553, -0.0001785, -9.978e-05],
            [-0.04927, 0.0001015, 6.870e-05, 3.637e-05],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.01, 'bar'),
        Pmax = (100, 'bar'),
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
    label="HOCHO + OH <=> HOCO + H2O",
    degeneracy=1,
    kinetics=Arrhenius(A=(2.70E-01, 'cm^3/(mol*s)'), n=3.93, Ea=(12500, 'cal/mol'), T0=(1, 'K')),
),

entry(
    index=24,
    label="HOCO + HO2 <=> HOCOO + OH",
    degeneracy=1,
    kinetics=Arrhenius(A=(7.28E+12, 'cm^3/(mol*s)'), n=0.02, Ea=(118.6, 'cal/mol'), T0=(1, 'K')),
),

entry(
    index=25,
    label="HOCO + HO2 <=> H2O + CO3",
    degeneracy=1,
    kinetics=Arrhenius(A=(9.23E+08, 'cm^3/(mol*s)'), n=0.68, Ea=(-549.0, 'cal/mol'), T0=(1, 'K')),
),