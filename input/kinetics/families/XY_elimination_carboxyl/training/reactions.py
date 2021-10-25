#!/usr/bin/env python
# encoding: utf-8

name = "XY_elimination_carboxyl/training"
shortDesc = "Kinetics used to train group additivity values"
longDesc = """
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""

entry(
    index = 0,
    label = "FCH2CH2COOH <=> C2H4 + HF + CO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.6978e+09, 's^-1'),
        n = 1.11971,
        Ea = (202.466, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 50 data points; dA = *|/ 1.30282, dn = +|- 0.0347546, dEa = +|- 0.189133 kJ/mol',
    ),
    rank = 5,
    shortDesc = """M062XD3/JUN-CC-PVTZ RRHO""",
    longDesc = 
"""
Calculated at DFT level (M062XD3/JUN-CC-PVTZ) with Gaussian 16 with RRHO approx
# Coordinates for TS in Input Orientation (angstroms):
#   F    1.78140   -0.88970   -0.00034
#   C    1.39546    1.03531    0.00035
#   C    0.01477    1.25721   -0.00016
#   C   -1.11019   -0.21156    0.00003
#   O   -2.22439    0.17596   -0.00018
#   O   -0.49584   -1.28313    0.00038
#   H    1.96509    1.08982    0.91568
#   H    1.96585    1.09019   -0.91449
#   H   -0.37988    1.68603    0.91290
#   H   -0.37935    1.68579   -0.91356
#   H    0.75728   -1.17288   -0.00034
""",
)

entry(
    index = 1,
    label = "CH3CH2COOH <=> C2H4 + H2 + CO2",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (205359, 's^-1'),
        n = 2.17099,
        Ea = (342.051, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 50 data points; dA = *|/ 2.11965, dn = +|- 0.0986994, dEa = +|- 0.537118 kJ/mol',
    ),
    rank = 5,
    shortDesc = """M062XD3/JUN-CC-PVTZ RRHO""",
    longDesc = 
"""
Calculated at DFT level (M062XD3/JUN-CC-PVTZ) with Gaussian 16 with RRHO approx
# Coordinates for TS in Input Orientation (angstroms):
#   H    1.6460   -0.6292   -0.0004
#   C    1.3976    0.9388    0.0003
#   C    0.0496    1.2643   -0.0002
#   C   -1.1556   -0.2720    0.0001
#   O   -2.2477    0.1918    0.0002
#   O   -0.5321   -1.3076    0.0001
#   H    1.9759    0.9869    0.9145
#   H    1.9768    0.9876   -0.9131
#   H   -0.3684    1.6608    0.9146
#   H   -0.3678    1.6604   -0.9156
#   H    0.9157   -1.0188   -0.0001
""",
)

entry(
    index = 2,
    label = "FCH2OCOOH <=> CH2O + HF + CO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.52249e+10, 's^-1'),
        n = 0.94147,
        Ea = (137.605, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 50 data points; dA = *|/ 1.19939, dn = +|- 0.0238861, dEa = +|- 0.129987 kJ/mol',
    ),
    rank = 5,
    shortDesc = """M062XD3/JUN-CC-PVTZ RRHO""",
    longDesc = 
"""
Calculated at DFT level (M062XD3/JUN-CC-PVTZ) with Gaussian 16 with RRHO approx
# Coordinates for TS in Input Orientation (angstroms):
#   F    1.8258   -0.8533    0.2952
#   C    1.2606    0.9028    0.0822
#   O    0.1192    0.9028    0.6038
#   C   -0.9883   -0.1007   -0.1051
#   O   -2.0460    0.3914   -0.1662
#   O   -0.3847   -1.1529   -0.3605
#   H    2.0655    1.3687    0.6424
#   H    1.3786    0.7891   -0.9936
#   H    0.8189   -1.1568    0.0026
""",
)

entry(
    index = 3,
    label = "BrCH2CH2COOH <=> C2H4 + HBr + CO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.23964e+08, 's^-1'),
        n = 1.60341,
        Ea = (216.691, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 50 data points; dA = *|/ 1.56427, dn = +|- 0.0587822, dEa = +|- 0.31989 kJ/mol',
    ),
    rank = 5,
    shortDesc = """M062XD3/JUN-CC-PVTZ RRHO""",
    longDesc = 
"""
Calculated at DFT level (M062XD3/JUN-CC-PVTZ) with Gaussian 16 with RRHO approx
# Coordinates for TS in Input Orientation (angstroms):
#   Br    2.2819   -1.3507   -0.0019
#   C    1.3912    1.1940    0.0004
#   C    0.0276    1.3616   -0.0002
#   C   -1.2006   -0.2289    0.0001
#   O   -2.2752    0.2266   -0.0015
#   O   -0.5837   -1.2871    0.0020
#   H    1.9591    1.2265    0.9176
#   H    1.9601    1.2279   -0.9161
#   H   -0.4316    1.6961    0.9212
#   H   -0.4309    1.6964   -0.9218
#   H    0.5922   -1.2992    0.0004
""",
)

entry(
    index = 4,
    label = "ClCH2CH2COOH <=> C2H4 + HCl + CO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.20378e+08, 's^-1'),
        n = 1.70445,
        Ea = (215.418, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 50 data points; dA = *|/ 1.65788, dn = +|- 0.0664175, dEa = +|- 0.361442 kJ/mol',
    ),
    rank = 5,
    shortDesc = """M062XD3/JUN-CC-PVTZ RRHO""",
    longDesc = 
"""
Calculated at DFT level (M062XD3/JUN-CC-PVTZ) with Gaussian 16 with RRHO approx
# Coordinates for TS in Input Orientation (angstroms):
#   Cl    2.1486   -1.2321   -0.0001
#   C    1.3958    1.1554    0.0002
#   C    0.0265    1.3275    0.0000
#   C   -1.1773   -0.2210   -0.0002
#   O   -2.2618    0.2199   -0.0004
#   O   -0.5661   -1.2848    0.0002
#   H    1.9634    1.2028    0.9168
#   H    1.9638    1.2032   -0.9161
#   H   -0.4171    1.6873    0.9197
#   H   -0.4168    1.6873   -0.9199
#   H    0.6312   -1.2825    0.0000
""",
)

entry(
    index = 5,
    label = "BrCH2OCOOH <=> CH2O + HBr + CO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.74683e+09, 's^-1'),
        n = 1.36442,
        Ea = (132.064, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 50 data points; dA = *|/ 1.36618, dn = +|- 0.0409934, dEa = +|- 0.223085 kJ/mol',
    ),
    rank = 5,
    shortDesc = """M062XD3/JUN-CC-PVTZ RRHO""",
    longDesc = 
"""
Calculated at DFT level (M062XD3/JUN-CC-PVTZ) with Gaussian 16 with RRHO approx
# Coordinates for TS in Input Orientation (angstroms):
#   Br    2.3645   -0.9936    0.3766
#   C    1.0191    1.1327   -0.3806
#   O   -0.0107    1.0880    0.3033
#   C   -1.1627   -0.2164   -0.0123
#   O   -2.2341    0.2237    0.0319
#   O   -0.4737   -1.2171   -0.1698
#   H    1.8086    1.8235   -0.0914
#   H    1.0717    0.6577   -1.3597
#   H    0.7409   -1.2048    0.1010
""",
)

entry(
    index = 6,
    label = "CF3CF2COOH <=> CF2CF2 + HF + CO2",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (4.71181e+11, 's^-1'),
        n = 0.715494,
        Ea = (287.921, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 50 data points; dA = *|/ 1.1823, dn = +|- 0.0220008, dEa = +|- 0.119728 kJ/mol',
    ),
    rank = 5,
    shortDesc = """M062XD3/JUN-CC-PVTZ RRHO""",
    longDesc = 
"""
Calculated at DFT level (M062XD3/JUN-CC-PVTZ) with Gaussian 16 with RRHO approx
# Coordinates for TS in Input Orientation (angstroms):
#   F    1.7337   -0.9728   -0.0463
#   C    1.4104    1.0756   -0.0217
#   C   -0.0257    1.2048    0.0154
#   C   -1.1421   -0.3277   -0.0221
#   O   -2.2084    0.1442   -0.1795
#   O   -0.5557   -1.3862    0.1514
#   F    2.1088    1.1380    1.0302
#   F    2.0518    1.1682   -1.1069
#   F   -0.4030    1.7936    1.1628
#   F   -0.4476    1.9156   -1.0385
#   H    0.7681   -1.2900    0.0555
""",
)

entry(
    index = 7,
    label = "ClCH2OCOOH <=> CH2O + HCl + CO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.42848e+09, 's^-1'),
        n = 1.33002,
        Ea = (133.295, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 50 data points; dA = *|/ 1.35693, dn = +|- 0.0401007, dEa = +|- 0.218227 kJ/mol',
    ),
    rank = 5,
    shortDesc = """M062XD3/JUN-CC-PVTZ RRHO""",
    longDesc = 
"""
Calculated at DFT level (M062XD3/JUN-CC-PVTZ) with Gaussian 16 with RRHO approx
# Coordinates for TS in Input Orientation (angstroms):
#   Cl   -2.0185   -0.9990    0.0721
#   C   -0.7511    1.0037    0.6016
#   O    0.2027    0.9662   -0.1921
#   C    1.3650   -0.2989    0.0144
#   O    2.4361    0.1365   -0.1017
#   O    0.7073   -1.3186    0.2069
#   H   -1.5728    1.6830    0.3883
#   H   -0.6743    0.5712    1.5980
#   H   -0.5378   -1.2784    0.1065
""",
)

