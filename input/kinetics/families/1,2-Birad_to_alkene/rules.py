#!/usr/bin/env python
# encoding: utf-8

name = "1,2-Birad_to_alkene/rules"
shortDesc = ""
longDesc = """
Reaction family added by gmagoon, 3/1/10

Correlation used for #1-16 below:
        log10(tau(s)) = -8.0 + 0.2 * m + 0.3 * n
        where m = number of alkyl substituents, n = number of aryl/vinyl substituents

References for this correlation and for treatment of alkene triplets as 1,2-biradicals:
1. R. A. Caldwell, Intersystem crossing in organic photochemical intermediates, Pure Appl. Chem., 56 (1984) 1167-1177. DOI: 10.1351/pac198456091167
2. R. A. Caldwell, Laser flash photolysis studies of intersystem crossing in biradicals and alkene triplets, p. 110, in Kinetics and spectroscopy of carbenes and biradicals, ed. M. S. Platz, 1990. DOI: 10.1007/978-1-4899-3707-0_4
3. D. J. Unett and R. A. Caldwell, The triplet state of alkenes: structure, dynamics, energetics and chemistry, Res. Chem. Intermed., 21 (1995) 665-709. DOI: 10.1163/156856795X00639
4. T. Ni, R. A. Caldwell, and L. A. Melton, The relaxed and spectroscopic energies of olefin triplets, J. Am. Chem. Soc., 111 (1989) 457-464. DOI: 10.1021/ja00184a008

To extrapolate to other groups, I am basing my (rough) assignments on the author's argument in Ref. 1,
that this effect is mainly related to number of hydrogens and mass of substituents, rather than electronic
stabilization/polar effects; note however, that this will not correctly account for large mass of extended groups like
large alkyl chains (in any case, the effect is relatively small, and the resulting estimate should still be within an
order or magnitude or so of what we would obtain if we assigned groups differently)

The assignments I use are:
                    no slow-down: H
                    m slow-down: Cs, Os
                    n slow-down: Cd, Ct, Cb, CO

it is assumed that k = 1/tau(s)
nomenclature used is `Y_12_mn`, where m and n are defined as above

No. Y_12birad   Temp.       A         n    a    E0     DA   Dn   Da   DE0  Rank
1.  Y_12birad   300-1500    1.0E+8    0    0    0.0    0    0    0    0    0
2.  Y_12_00     300-1500    1.0E+8    0    0    0.0    0    0    0    0    5
3.  Y_12_10     300-1500    6.31E+7   0    0    0.0    0    0    0    0    5
4.  Y_12_20     300-1500    3.98E+7   0    0    0.0    0    0    0    0    5
5.  Y_12_30     300-1500    2.51E+7   0    0    0.0    0    0    0    0    5
6.  Y_12_40     300-1500    1.58E+7   0    0    0.0    0    0    0    0    5
7.  Y_12_01     300-1500    5.01E+7   0    0    0.0    0    0    0    0    5
8.  Y_12_02     300-1500    2.51E+7   0    0    0.0    0    0    0    0    5
9.  Y_12_03     300-1500    1.26E+7   0    0    0.0    0    0    0    0    5
10. Y_12_04     300-1500    6.31E+6   0    0    0.0    0    0    0    0    5
11. Y_12_11     300-1500    3.16E+7   0    0    0.0    0    0    0    0    5
12. Y_12_12     300-1500    1.58E+7   0    0    0.0    0    0    0    0    5
13. Y_12_21     300-1500    2.00E+7   0    0    0.0    0    0    0    0    5
14. Y_12_22     300-1500    1.0E+7    0    0    0.0    0    0    0    0    5
15. Y_12_13     300-1500    7.94E+6   0    0    0.0    0    0    0    0    5
16. Y_12_31     300-1500    1.26E+7   0    0    0.0    0    0    0    0    5
"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(9.88805e+09,'s^-1'), n=5.89217e-08, w0=(128050,'J/mol'), E0=(12805,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-6.118039481230491, var=75.64106497048724, Tref=1000.0, N=10, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 10 training reactions at node Root
    Total Standard Deviation in ln(k): 32.80751472454549"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root
Total Standard Deviation in ln(k): 32.80751472454549""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root
Total Standard Deviation in ln(k): 32.80751472454549
""",
)

entry(
    index = 2,
    label = "Root_1CNOS->S",
    kinetics = ArrheniusBM(A=(1e+10,'s^-1'), n=0, w0=(128500,'J/mol'), E0=(12850,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1CNOS->S',), comment="""BM rule fitted to 1 training reactions at node Root_1CNOS->S
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1CNOS->S
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1CNOS->S
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 3,
    label = "Root_N-1CNOS->S",
    kinetics = ArrheniusBM(A=(2.15377e+07,'s^-1'), n=-2.07423e-07, w0=(128000,'J/mol'), E0=(12800,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-7.007630323923653e-08, var=1.174290528492398, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1CNOS->S',), comment="""BM rule fitted to 9 training reactions at node Root_N-1CNOS->S
    Total Standard Deviation in ln(k): 2.1724250582777613"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1CNOS->S
Total Standard Deviation in ln(k): 2.1724250582777613""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1CNOS->S
Total Standard Deviation in ln(k): 2.1724250582777613
""",
)

entry(
    index = 4,
    label = "Root_N-1CNOS->S_Ext-2CNOS-R",
    kinetics = ArrheniusBM(A=(1.21103e+07,'s^-1'), n=-2.20815e-07, w0=(128000,'J/mol'), E0=(12800,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-8.1353150249139e-08, var=0.3479747299190572, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1CNOS->S_Ext-2CNOS-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1CNOS->S_Ext-2CNOS-R
    Total Standard Deviation in ln(k): 1.1825810560647294"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1CNOS->S_Ext-2CNOS-R
Total Standard Deviation in ln(k): 1.1825810560647294""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1CNOS->S_Ext-2CNOS-R
Total Standard Deviation in ln(k): 1.1825810560647294
""",
)

entry(
    index = 5,
    label = "Root_N-1CNOS->S_Ext-1CNO-R",
    kinetics = ArrheniusBM(A=(5.62257e+07,'s^-1'), n=-5.42083e-07, w0=(128000,'J/mol'), E0=(12800,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-4.305460834090209e-17, var=0.10644475987203207, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1CNOS->S_Ext-1CNO-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1CNOS->S_Ext-1CNO-R
    Total Standard Deviation in ln(k): 0.6540623233197181"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1CNOS->S_Ext-1CNO-R
Total Standard Deviation in ln(k): 0.6540623233197181""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1CNOS->S_Ext-1CNO-R
Total Standard Deviation in ln(k): 0.6540623233197181
""",
)

entry(
    index = 6,
    label = "Root_N-1CNOS->S_Ext-2CNOS-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(9.44385e+06,'s^-1'), n=-4.93451e-07, w0=(128000,'J/mol'), E0=(12800,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.3601896725538097e-07, var=0.21271097658282923, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1CNOS->S_Ext-2CNOS-R_Ext-3R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1CNOS->S_Ext-2CNOS-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 0.9245961925266748"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1CNOS->S_Ext-2CNOS-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 0.9245961925266748""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1CNOS->S_Ext-2CNOS-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 0.9245961925266748
""",
)

entry(
    index = 7,
    label = "Root_N-1CNOS->S_Ext-2CNOS-R_Ext-2CNOS-R",
    kinetics = ArrheniusBM(A=(1.58e+07,'s^-1'), n=0, w0=(128000,'J/mol'), E0=(12800,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1CNOS->S_Ext-2CNOS-R_Ext-2CNOS-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1CNOS->S_Ext-2CNOS-R_Ext-2CNOS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1CNOS->S_Ext-2CNOS-R_Ext-2CNOS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1CNOS->S_Ext-2CNOS-R_Ext-2CNOS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 8,
    label = "Root_N-1CNOS->S_Ext-1CNO-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(5.01e+07,'s^-1'), n=0, w0=(128000,'J/mol'), E0=(12800,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1CNOS->S_Ext-1CNO-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1CNOS->S_Ext-1CNO-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1CNOS->S_Ext-1CNO-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1CNOS->S_Ext-1CNO-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 9,
    label = "Root_N-1CNOS->S_Ext-2CNOS-R_Ext-3R!H-R_Ext-2CNOS-R",
    kinetics = ArrheniusBM(A=(8.57843e+06,'s^-1'), n=-2.81195e-07, w0=(128000,'J/mol'), E0=(12800,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-9.033603721174606e-08, var=0.2791118967387258, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1CNOS->S_Ext-2CNOS-R_Ext-3R!H-R_Ext-2CNOS-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1CNOS->S_Ext-2CNOS-R_Ext-3R!H-R_Ext-2CNOS-R
    Total Standard Deviation in ln(k): 1.0591226517407373"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1CNOS->S_Ext-2CNOS-R_Ext-3R!H-R_Ext-2CNOS-R
Total Standard Deviation in ln(k): 1.0591226517407373""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1CNOS->S_Ext-2CNOS-R_Ext-3R!H-R_Ext-2CNOS-R
Total Standard Deviation in ln(k): 1.0591226517407373
""",
)

entry(
    index = 10,
    label = "Root_N-1CNOS->S_Ext-2CNOS-R_Ext-3R!H-R_Ext-2CNOS-R_Ext-1CNO-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(7.07822e+06,'s^-1'), n=3.06366e-07, w0=(128000,'J/mol'), E0=(12800,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.10559548973411999, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1CNOS->S_Ext-2CNOS-R_Ext-3R!H-R_Ext-2CNOS-R_Ext-1CNO-R_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1CNOS->S_Ext-2CNOS-R_Ext-3R!H-R_Ext-2CNOS-R_Ext-1CNO-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 0.651447878002502"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1CNOS->S_Ext-2CNOS-R_Ext-3R!H-R_Ext-2CNOS-R_Ext-1CNO-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 0.651447878002502""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1CNOS->S_Ext-2CNOS-R_Ext-3R!H-R_Ext-2CNOS-R_Ext-1CNO-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 0.651447878002502
""",
)

entry(
    index = 11,
    label = "Root_N-1CNOS->S_Ext-2CNOS-R_Ext-3R!H-R_Ext-2CNOS-R_Ext-1CNO-R_Ext-6R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(6.31e+06,'s^-1'), n=0, w0=(128000,'J/mol'), E0=(12800,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1CNOS->S_Ext-2CNOS-R_Ext-3R!H-R_Ext-2CNOS-R_Ext-1CNO-R_Ext-6R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1CNOS->S_Ext-2CNOS-R_Ext-3R!H-R_Ext-2CNOS-R_Ext-1CNO-R_Ext-6R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1CNOS->S_Ext-2CNOS-R_Ext-3R!H-R_Ext-2CNOS-R_Ext-1CNO-R_Ext-6R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1CNOS->S_Ext-2CNOS-R_Ext-3R!H-R_Ext-2CNOS-R_Ext-1CNO-R_Ext-6R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

