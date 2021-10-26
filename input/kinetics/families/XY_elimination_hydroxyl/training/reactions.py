#!/usr/bin/env python
# encoding: utf-8

name = "XY_elimination_hydroxyl/training"
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

entry(
    index = 8,
    label = "CH3CH(OH)CH2CH2F <=> C2H4 + HF + CH3CHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.13544e+09, 's^-1'),
        n = 1.07219,
        Ea = (220.082, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 50 data points; dA = *|/ 1.28453, dn = +|- 0.0328971, dEa = +|- 0.179025 kJ/mol',
    ),
    rank = 5,
    shortDesc = """M062XD3/JUN-CC-PVTZ RRHO""",
    longDesc = 
"""
Calculated at DFT level (M062XD3/JUN-CC-PVTZ) with Gaussian 16 with RRHO approx
# Coordinates for TS in Input Orientation (angstroms):
#   F    1.7600   -0.9125   -0.2789
#   C    1.4122    1.0894    0.0362
#   C    0.0615    1.3739    0.1241
#   C   -0.8577   -0.2773   -0.2930
#   O   -0.3906   -1.2037    0.4809
#   H    2.0094    0.9095    0.9153
#   H    1.9581    1.2489   -0.8809
#   H   -0.3538    1.5333    1.1103
#   H   -0.3697    1.9623   -0.6758
#   H    0.6772   -1.2615    0.1736
#   C   -2.2986    0.0895   -0.0878
#   H   -2.8988   -0.7606   -0.4177
#   H   -2.5842    0.9647   -0.6663
#   H   -2.4994    0.2558    0.9684
#   H   -0.5200   -0.3000   -1.3308
""",
)

entry(
    index = 9,
    label = 'CH2C(OH)CH2CH2F <=> C2H4 + HF + CH2CO',
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.52349e+10, 's^-1'),
        n = 1.11612,
        Ea = (246.995, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 50 data points; dA = *|/ 1.24468, dn = +|- 0.0287562, dEa = +|- 0.15649 kJ/mol',
    ),
    rank = 5,
    shortDesc = """M062XD3/JUN-CC-PVTZ RRHO""",
    longDesc = 
"""
Calculated at DFT level (M062XD3/JUN-CC-PVTZ) with Gaussian 16 with RRHO approx
# Coordinates for TS in Input Orientation (angstroms):
#   F    1.4462   -1.0912    0.2511
#   C    1.3971    1.0389    0.1686
#   C    0.1871    1.4644   -0.3802
#   C   -0.9826    0.1545   -0.2400
#   O   -0.5963   -0.8810   -0.8307
#   H    1.5516    1.0670    1.2383
#   H    2.2601    0.8090   -0.4356
#   H   -0.3257    2.1960    0.2312
#   H    0.1950    1.6694   -1.4442
#   H    0.5378   -1.1617   -0.2793
#   C   -2.0782    0.5191    0.4245
#   H   -2.8634   -0.2170    0.5207
#   H   -2.2184    1.5036    0.8309
""",
)

entry(
    index = 10,
    label = 'CH2(OH)CH2CH2F <=> C2H4 + HF + CH2O-2',
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.83092e+09, 's^-1'),
        n = 1.14718,
        Ea = (230.441, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 50 data points; dA = *|/ 1.29992, dn = +|- 0.0344614, dEa = +|- 0.187538 kJ/mol',
    ),
    rank = 5,
    shortDesc = """M062XD3/JUN-CC-PVTZ RRHO""",
    longDesc = 
"""
Calculated at DFT level (M062XD3/JUN-CC-PVTZ) with Gaussian 16 with RRHO approx
# Coordinates for TS in Input Orientation (angstroms):
#   F    1.5095   -1.0080   -0.3332
#   C    1.2575    1.0695   -0.0995
#   C   -0.0578    1.4054    0.1639
#   C   -1.0195   -0.1945   -0.1093
#   O   -0.5589   -1.1303    0.6515
#   H    1.9665    0.8849    0.6909
#   H    1.6664    1.1460   -1.0957
#   H   -0.3251    1.6112    1.1916
#   H   -0.5753    1.9884   -0.5889
#   H    0.4816   -1.2726    0.2328
#   H   -2.0006    0.1989    0.1540
#   H   -0.8381   -0.2799   -1.1817
""",
)

entry(
    index = 11,
    label = 'CH2C(OH)OCH2F <=> CH2O + HF + CH2CO',
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.29418e+10, 's^-1'),
        n = 0.745914,
        Ea = (145.547, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 50 data points; dA = *|/ 1.0985, dn = +|- 0.0123427, dEa = +|- 0.0671686 kJ/mol',
    ),
    rank = 5,
    shortDesc = """M062XD3/JUN-CC-PVTZ RRHO""",
    longDesc = 
"""
Calculated at DFT level (M062XD3/JUN-CC-PVTZ) with Gaussian 16 with RRHO approx
# Coordinates for TS in Input Orientation (angstroms):
#   F   -1.8202   -0.7806    0.6417
#   C   -1.1968    0.9386   -0.2359
#   O   -0.0204    0.9830    0.1698
#   C    0.8817   -0.1990   -0.2927
#   O    0.1873   -1.2334   -0.4659
#   H   -1.4531    0.3973   -1.1400
#   H   -1.9009    1.6285    0.2151
#   H   -0.9267   -1.1661    0.1972
#   C    2.1520    0.1723   -0.3615
#   H    2.8915   -0.5700   -0.6103
#   H    2.4362    1.1901   -0.1626
""",
)

entry(
    index = 12,
    label = 'F2C(OH)CH2CH2F <=> C2H4 + HF + CF2O',
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.98542e+10, 's^-1'),
        n = 0.978818,
        Ea = (232.512, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 50 data points; dA = *|/ 1.21021, dn = +|- 0.0250664, dEa = +|- 0.13641 kJ/mol',
    ),
    rank = 5,
    shortDesc = """M062XD3/JUN-CC-PVTZ RRHO""",
    longDesc = 
"""
Calculated at DFT level (M062XD3/JUN-CC-PVTZ) with Gaussian 16 with RRHO approx
# Coordinates for TS in Input Orientation (angstroms):
#   F    1.6320   -1.0022   -0.1166
#   C    1.2776    1.0646   -0.1422
#   C   -0.0408    1.3026    0.2427
#   C   -1.0220   -0.1637   -0.0764
#   O   -0.6009   -1.1628    0.5314
#   H    2.0900    1.0372    0.5667
#   H    1.5489    1.0652   -1.1884
#   H   -0.2170    1.5072    1.2905
#   H   -0.5925    1.9260   -0.4545
#   H    0.6668   -1.2468    0.1920
#   F   -2.2399    0.2879    0.2676
#   F   -0.9960   -0.1964   -1.4364
""",
)

entry(
    index = 13,
    label = 'F2C(OH)OCH2F <=> CH2O + HF + CF2O',
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.14547e+10, 's^-1'),
        n = 0.631481,
        Ea = (131.332, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 50 data points; dA = *|/ 1.07555, dn = +|- 0.00956901, dEa = +|- 0.0520742 kJ/mol',
    ),
    rank = 5,
    shortDesc = """M062XD3/JUN-CC-PVTZ RRHO""",
    longDesc = 
"""
Calculated at DFT level (M062XD3/JUN-CC-PVTZ) with Gaussian 16 with RRHO approx
# Coordinates for TS in Input Orientation (angstroms):
#   F   -2.0440   -0.7770   -0.5350
#   C   -1.3863    0.9640    0.0713
#   O   -0.2619    1.0109   -0.4684
#   C    0.7325   -0.1342    0.0642
#   O    0.2237   -1.2432   -0.1813
#   H   -2.1787    1.5525   -0.3773
#   H   -1.4985    0.5833    1.0827
#   H   -1.0611   -1.1532   -0.4135
#   F    1.8466    0.2114   -0.5596
#   F    0.8779    0.2197    1.3583
""",
)


