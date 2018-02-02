#!/usr/bin/env python
# encoding: utf-8

name = "SOx"
shortDesc = u"SOx"
longDesc =u"""
This library includes important SOx-related reactions.
Prepared by Alon Grinberg Dana


This library consists of the following subsets:
* SOx
* COS
* HxSy
* CxHySz
* C-S
* SOx-NOx
* HOSO2 + O2 surface

Reference legend:
[Baulch1992a] D.L. Baulch, C.J. Cobos, R.A. Cox, C. Esser, P. Frank, Th. Just, J.A. Kerr, M.J. Philling, J. Troe, R.W. Walker, J. Warnatz, "Evaluated Kinetic Data for Combustion Modelling", Journal of Physical and Chemical Reference Data, 1992, 21(3), 411, doi: 10.1063/1.555908
[Calvert1973] F.B. Wampler, K. Otsuka, J.G. Calvert, E.K. Damon, Int. J. Chem. Kin., 1973, 5(4), 669-690, doi: 10.1002/kin.550050417
[Dupre1993] K. Tsuchiya, H. Matsui, M. Oya, G. Dupre, in: R. Burn, L.Z. Dumitrescu (Ed.) Shock Waves @ Marseille II (Proceedings Marseille France), 1993, 71-76, doi: 10.1007/978-3-642-78832-1
[GlarBozz] (RMG's Sulfur/GlarborgBozzelli library) P. Glarborg, D. Kubel, K. Dam-Johansen, H-M. Chiang, J.W. Bozzelli, Int. J. Chem. Kin., 1996, 28, 773-790, doi: 10.1002/(SICI)1097-4601(1996)28:10<773::AID-KIN8>3.0.CO;2-K
[Lin2003a] C-W. Lu, Y-J. Wu, Y-P. Lee, R.S. Zhu, M.C. Lin, J. Phys. Chem. A, 2003, 107(50), 11020-11029, doi: 10.1021/jp036025c
[Lin2004] C-W. Lu, Y-J. Wu, Y-P. Lee, R.S. Zhu, M.C. Lin, J. Chem. Phys., 2004, 121(17), 8271-8278, doi: 10.1063/1.1792611
[Marshall1999a] A. Goumri, J-D.R. Rocha, D. Laakso, C.E. Smith, P. Marshall, J. Phys. Chem. A, 1999, 103(51), 11328-11335 doi: 10.1021/jp9924070
[Marshall1999b] J. Peng, X. Hu, P. Marshall, J. Phys. Chem. A, 1999, 103, 5307-5311, doi: 10.1021/jp984242l
[Marshall2004] A. Goumri, D.D. Shao, P. Marshall, J. Chem. Phys., 2004, 121, 9999, doi: 10.1063/1.1806419
[Marshall2005] J. Naidoo, A. Goumri, P. Marshall, Proceedings of the Combustion Institute, 2005, 30(1), 1219-1225, doi: 10.1016/j.proci.2004.08.214
[Marshall2006] A. Yilmaz, L. Hindiyarti, A.D. Jensen, P. Glarbotg, P. Marshall, J. Phys. Chem. A, 2006, 110 (21), 6654-6659, doi: 10.1021/jp0557215
[Marshall2007a] L. Hindiyarti, P. Glarborg, P. Marshall, J. Phys. Chem. A, 2007, 111(19), 3984-3991, doi: 10.1021/jp067499p
[Marshall2007b] C.L. Rasmussen, P. Glarborg, P. Marshall, Proceedings of the Combustion Institute, 2007, 31, 339-347, doi: 10.1016/j.proci.2006.07.249
[Marshall2011] Y. Gao, P. Marshall, J. Chem. Phys., 2011, 135, 144306, doi: 10.1063/1.3644773
[Marshall2012] K.M. Thompson, Y. Gao, P. Marshall, Int. J. Chem. Kin., 2012, 44(1), 90-99, doi: 10.1002/kin.20612
[Marshall2015a] S. Ayling, Y. Gao, P. Marshall, Proceedings of the Combustion Institute, 2015, 35(1), 215-222, doi: 10.1016/j.proci.2014.05.079
[Marshall2015b] K.E. Kerr, I.M. Alecu, K.M. Thompson, Y. Gao, P. Marshall, J. Phys. CHem. A, 2015, 119, 7352-7360, doi: 10.1021/jp512966a
[Matsui1994] M. Oya, H. Shiina, K. Tsuchiya, H. Matsui, Bulletin of the Chemical Society of Japan, 1994, 67(8), 2311-2313, doi: 10.1246/bcsj.67.2311
[Matsui1996a] H. Shiina, M. Oya, K. Yamashita, A. Miyoshi, H. Matsui, J. Phys. Chem., 1996, 100(6), 2136-2140, doi: 10.1021/jp952472j
[Matsui1996b] K. Tsuchiya, K. Yamashita, A. Miyoshi, H. Matsui, J. Phys. Chem., 1996, 100(43), 17202-17206, doi: 10.1021/jp961252i
[Matsui1998] H. Shiina, A. Miyoshi, H. Matsui, J. Phys. Chem. A, 1998, 102(20), 3556-3559, doi: 10.1021/jp980650d
[Molina1997] J.T. Jayne, U. Poschl, Y-m. Chen, D. Dai, L.T. Molina, D.R. Worsnop, C.E. Kolb, M.J. Molina, J. Phys. Chem. A, 1997, 101(51), 10000-10011, doi: 10.1021/jp972549z
[Mukarami1979] T. Higashihara, K. Saito, I. Murakami, Bulletin of the Chemical Society of Japan, 1980, 53(1), 15-18, doi: 10.1246/bcsj.53.15
[Palmer1977] H. Freund, H.B. Palmer, Int. J. Chem. Kin., 1977, 9(6), 887-905, doi: 10.1002/kin.550090605
[Pilling2002] M.A. Blitz, K.W. McKee, M.J. Pilling, J. Phys. Chem. A, 2002, 106(36), 8406-8410, doi: 10.1021/jp025508y
[Pilling2003] M.A. Blitz, K.J. Hughes, M.J. Pilling, J. Phys. Chem. A, 2003, 107(12), 1971-1978, doi: 10.1021/jp026524y
[Pilling2006] M.A. Blitz, K.J. Hughes, M.J. Pilling, S.H. Robertson, J. Phys. Chem. A, 2006, 110(9), 2996-3009, doi: 10.1021/jp054722u
[Roth1993] D. Woiki, P. Roth, in: R. Burn, L.Z. Dumitrescu (Ed.) Shock Waves @ Marseille II (Proceedings Marseille France), 1993, 53-58, doi: 10.1007/978-3-642-78832-1_9
[Roth1996a] D. Woiki, P. Roth, Israel Journal of Chemistry, 1996, 36(3), 279-283, doi: 10.1002/ijch.199600039
[Roth1996b] D. Woiki, P. Roth, Symposium (International) on Combustion, 1996, 26(1), 583-588, doi: 10.1016/S0082-0784(96)80263-3
[Sendt2002] K. Sendt, M. Jazbec, B.S. Haynes, Proceedings of the Combustion Institute, 2002, 29, 2439-2446, doi: 10.1016/S1540-7489(02)80297-8
[Sendt2008] C.R. Zhou, K. Sendt, B.S. Haynes, J. Phys. Chem. A, 2008, 112, 3239-3247, doi: 10.1021/jp710488d
[Somnitz2004] H. Somnitz, Phys. Chem. Chem. Phys., 2004, 6(14), 3844-3851, doi: 10.1039/B317055A
[Tezaki2003] N. Isshiki, Y. Murakami, K. Tsuchiya, A. Tezaki, H. Matsui, J. Phys. Chem. A, 2003, 107(14), 2464-2469, doi: 10.1021/jp0200829
[Troe1984] H.J. Plach, J. Troe, Int. J. Chem. Kin., 1984, 16(12), 1531-1542, doi: 10.1002/kin.550161207
"""

entry(
    index = 1,
    label = "S + S <=> S2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(3.98e+14, 'cm^6/(mol^2*s)'), n=0, Ea=(-22455, 'cal/mol'), T0 = (1, 'K'),
                                 Tmin=(4500, 'K'), Tmax=(6000, 'K'))),
    shortDesc = u"""[Mukarami1979]""",
    longDesc =
u"""
Part of the "SOx" mechanism
Shock tube experimental study, done in Ar.
T range: 4500-6000 K
As reported by [Lin2003a] as k26
""",
)

entry(
    index = 2,
    label = "SO2 <=> SO + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.84e+16, 'cm^3/(mol*s)'), n=0, Ea=(109674, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2003a]""",
    longDesc =
u"""
Part of the "SOx" mechanism
k1a p. 11028
calculations done at the G2M(RCC2)//B3LYP/6-311+(3df) level of theory
also validated experimentally in the same study
""",
)

entry(
    index = 3,
    label = "S + O2 <=> O + SO",
    degeneracy = 1,
    kinetics=Arrhenius(A=(5.43e+05, 'cm^3/(mol*s)', '+|-', 1.63E+04), n=2.11, Ea=(1451, 'cal/mol', '+|-', 238),
                       T0=(1, 'K'), Tmin=(298, 'K'), Tmax=(3460, 'K')),
    shortDesc = u"""[Lin2004]""",
    longDesc =
u"""
Part of the "SOx" mechanism
Experimental and theoretical investigation
Theoretical calculations done at the  G2M(RCC2) level, using geometries optimized with the B3LYP/6-311+G(3df) method
T range: 298-3460 K
The uncertainty for n is +|- 0.15

Kinetics is a also available for the reverse direction:

entry(
    index = -3,
    label = "SO + O <=> S + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.36e+07, 'cm^3/(mol*s)'), n=1.51, Ea=(5042, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u'[Lin2003a]',
    longDesc =
u'
Part of the "SOx" mechanism
k10b p. 11028
calculations done at the G2M(RCC2)//B3LYP/6-311+(3df) level of theory
also validated experimentally in the same study
',
)
""",
)

entry(
    index = 4,
    label = "SO <=> S + O",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(3.98e+14, 'cm^3/(mol*s)'), n=0, Ea=(107000, 'cal/mol'), T0 = (1, 'K'),
                                 Tmin=(3000, 'K'), Tmax=(5000, 'K'))),
    shortDesc = u"""[Troe1984]""",
    longDesc =
u"""
Part of the "SOx" mechanism
Shock tube experimental study, done in Ar.
T range: 3000-5000 K
""",
)

entry(
    index = 5,
    label = "SO2 + O <=> SO3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.7e+11, 'cm^3/(mol*s)'), n=0, Ea=(1689, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(2.4e+27, 'cm^6/(mol^2*s)'), n=-3.6, Ea=(5186, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.442, T3=(316, 'K'), T1=(7442, 'K'), efficiencies={'O=S=O': 10, 'O': 10, 'O=C=O': 2.5, 'N#N': 0}),
    shortDesc = u"""[Marshall2005],[Marshall2006]""",
    longDesc =
u"""
Part of the "SOx" mechanism
Calculated for Ar as the main bath gas
SO2 and H2O efficiencies taken from P. Glarborg, P. Marshall, Int. J. Chem. Kin. 2013, 45(7), 429-439, doi: 10.1002/kin.20778
CO2 collider efficiency taken from J. Gimenez-Lopez, M. Martinez, A. Millera, R. Bilbao, M.U. Alzueta, Comb. Flame 2011, 158(1), 48-56, doi: 10.1016/j.combustflame.2010.07.017
Experimental data also available from [Rabinowitz2010]:
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(2.9e+35, 'cm^3/(mol*s)'), n=-6.0, Ea=(9500, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.1e+24, 'cm^3/(mol*s)'), n=-3.0, Ea=(3935, 'cal/mol'), T0=(1, 'K')),
        ],),
""",
)

entry(
    index = 6,
    label = "SO2 + O (+N2) <=> SO3 (+N2)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.7e+11, 'cm^6/(mol^2*s)'), n=0, Ea=(1689, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(2.9e+27, 'cm^9/(mol^3*s)'), n=-3.58, Ea=(5206, 'cal/mol'), T0=(1, 'K')),
        alpha=0.43, T3=(371, 'K'), T1=(7442, 'K'), efficiencies={}),
    shortDesc = u"""[Marshall2005],[Marshall2006]""",
    longDesc =
u"""
Part of the "SOx" mechanism
Complementary to the reaction above for N2 as the main bath gas
""",
)

entry(
    index = 7,
    label = "SO2 + H <=> HOSO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.37e+08, 'cm^3/(mol*s)'), n=1.63, Ea=(7339, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(1700, 'K')),
        arrheniusLow = Arrhenius(A=(1.85e+37, 'cm^6/(mol^2*s)'), n=-6.14, Ea=(11075, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(1700, 'K')),
        alpha=0.283, T3=(272, 'K'), T1=(3995, 'K'), efficiencies={'O=S=O': 10, 'O': 10, 'O=C=O': 2.5}),
    shortDesc = u"""[Pilling2006]""",
    longDesc =
u"""
Part of the "SOx" mechanism
T range: 300-1700 K
As reported by Gimenez-Lopez, M. Martinez, A. Millera, R. Bilbao, M.U. Alzueta, Comb. Flame 2011, 158(1), 48-56, doi: 10.1016/j.combustflame.2010.07.017
Added as a training reaction to R_Addition_MultipleBond
""",
)

entry(
    index = 8,
    label = "SO2 + H <=> HSO2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.31e+08, 'cm^3/(mol*s)'), n=1.59, Ea=(2472, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(1000, 'K')),
        arrheniusLow = Arrhenius(A=(1.41e+31, 'cm^6/(mol^2*s)'), n=-5.19, Ea=(4513, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(1000, 'K')),
        alpha=0.39, T3=(167, 'K'), T1=(2191, 'K'), efficiencies={'O=S=O': 10, 'O': 10, 'O=C=O': 2.5}),
    shortDesc = u"""[Pilling2006]""",
    longDesc =
u"""
Part of the "SOx" mechanism
T range: 200-1000 K
As reported by Gimenez-Lopez, M. Martinez, A. Millera, R. Bilbao, M.U. Alzueta, Comb. Flame 2011, 158(1), 48-56, doi: 10.1016/j.combustflame.2010.07.017
""",
)

entry(
    index = 9,
    label = "SO2 + H <=> SO + OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(9.19e+25, 'cm^3/(mol*s)'), n=2.77, Ea=(20850, 'cal/mol'), T0=(1, 'K'), Tmin=(900, 'K'), Tmax=(1800, 'K')),
        arrheniusLow = Arrhenius(A=(1.35e+22, 'cm^6/(mol^2*s)'), n=-2.30, Ea=(30965, 'cal/mol'), T0=(1, 'K'), Tmin=(900, 'K'), Tmax=(1800, 'K')),
        alpha=0.283, T3=(272, 'K'), T1=(3995, 'K'), efficiencies={'O=S=O': 10, 'O': 10, 'O=C=O': 2.5}),
    shortDesc = u"""[Pilling2006]""",
    longDesc =
u"""
Part of the "SOx" mechanism
T range: 900-1800 K
As reported by Gimenez-Lopez, M. Martinez, A. Millera, R. Bilbao, M.U. Alzueta, Comb. Flame 2011, 158(1), 48-56, doi: 10.1016/j.combustflame.2010.07.017
""",
)

entry(
    index = 10,
    label = "SO3 + H <=> SO2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.4e+09, 'cm^3/(mol*s)'), n=1.22, Ea=(3320, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(700, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"""[Marshall2007a]""",
    longDesc =
u"""
Part of the "SOx" mechanism
T range: 700-2000 K
calculations done at the CBS-QB3/CCSD(T)//B3LYP/6-311G(2d,d,p) level of theory
""",
)

entry(
    index = 11,
    label = "SO3 + O <=> SO2 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+04, 'cm^3/(mol*s)'), n=2.57, Ea=(29210, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Marshall2007a]""",
    longDesc =
u"""
Part of the "SOx" mechanism
T > 1000 K
calculations done at the CBS-QB3/CCSD(T)//B3LYP/6-311G(2d,d,p) level of theory
Also available from [Wang1982] and [Marshall2006], about O(5) faster!, as:
    kinetics = Arrhenius(A=(7.8e+11, 'cm^3/(mol*s)'), n=0.00, Ea=(6100, 'cal/mol'), T0=(1, 'K')),
""",
)

entry(
    index = 12,
    label = "SO3 + OH <=> SO2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.8e+04, 'cm^3/(mol*s)'), n=2.46, Ea=(27225, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(800, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"""[Marshall2007a]""",
    longDesc =
u"""
Part of the "SOx" mechanism
T range: 800-2000 K
calculations done at the CBS-QB3/CCSD(T)//B3LYP/6-311G(2d,d,p) level of theory
""",
)

entry(
    index = 13,
    label = "SO + HO2 <=> SO2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.7e+03, 'cm^3/(mol*s)'), n=2.42, Ea=(7660, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Marshall2007b]""",
    longDesc =
u"""
Part of the "SOx" mechanism
calculations done at the CBS-QB3 level
* Consider improving if a higher level of theory is available
""",
)

entry(
    index = 14,
    label = "HSO + O2 <=> HSO2 + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.4e-07, 'cm^3/(mol*s)'), n=5.10, Ea=(11312, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Marshall2007b]""",
    longDesc =
u"""
Part of the "SOx" mechanism
calculations done at the CBS-QB3 level
* Consider improving if a higher level of theory is available
""",
)

entry(
    index = 15,
    label = "HOSO + O2 <=> SO2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.6e+01, 'cm^3/(mol*s)'), n=2.36, Ea=(-10130, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Marshall2007b]""",
    longDesc =
u"""
Part of the "SOx" mechanism
calculations done at the CBS-QB3 level
* Consider improving if a higher level of theory is available
""",
)

entry(
    index = 16,
    label = "HSO2 + O2 <=> SO2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+03, 'cm^3/(mol*s)'), n=3.20, Ea=(-235, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Marshall2007b]""",
    longDesc =
u"""
Part of the "SOx" mechanism
calculations done at the CBS-QB3 level
* Consider improving if a higher level of theory is available
""",
)

entry(
    index = 17,
    label = "HOSO <=> HSO2",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(1.03e+9, 's^-1'), n=1.03, Ea=(49980, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(2000, 'K')),
        arrheniusLow = Arrhenius(A=(1.72e+35, 'cm^3/(mol*s)'), n=-5.64, Ea=(55423, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(2000, 'K'))),
    shortDesc = u"""[Marshall1999a]""",
    longDesc =
u"""
Part of the "SOx" subset
T range: 200-2000 K
Table 7 on p. 11333
calculations done at the QCISD(T)/6-311+G(3df,2p)//MP2=FULL/6-31G(d) level of theory
""",
)

entry(
    index = 18,
    label = "HSOO <=> SH + O2",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(4.41e+18, 's^-1'), n=-1.07, Ea=(7750, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(2000, 'K')),
        arrheniusLow = Arrhenius(A=(1.56e+23, 'cm^3/(mol*s)'), n=-2.82, Ea=(-7450, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(2000, 'K'))),
    shortDesc = u"""[Marshall1999a]""",
    longDesc =
u"""
Part of the "SOx" subset
T range: 200-2000 K
Table 7 on p. 11333
calculations done at the QCISD(T)/6-311+G(3df,2p)//MP2=FULL/6-31G(d) level of theory
Added as a training reaction to R_Recombination
""",
)

entry(
    index = 19,
    label = "HOSO <=> OH + SO",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(1.65e+16, 's^-1'), n=-0.32, Ea=(67720, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(2000, 'K')),
        arrheniusLow = Arrhenius(A=(1.25e+32, 'cm^3/(mol*s)'), n=-4.33, Ea=(69115, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(2000, 'K'))),
    shortDesc = u"""[Marshall1999a]""",
    longDesc =
u"""
Part of the "SOx" subset
T range: 200-2000 K
Table 7 on p. 11333
calculations done at the QCISD(T)/6-311+G(3df,2p)//MP2=FULL/6-31G(d) level of theory
""",
)

entry(
    index = 20,
    label = "HSOO <=> HSO + O",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(2.01e+19, 's^-1'), n=-1.07, Ea=(28377, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(2000, 'K')),
        arrheniusLow = Arrhenius(A=(9.27e+34, 'cm^3/(mol*s)'), n=-5.87, Ea=(30960, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(2000, 'K'))),
    shortDesc = u"""[Marshall1999a]""",
    longDesc =
u"""
Part of the "SOx" subset
T range: 200-2000 K
Table 7 on p. 11333
calculations done at the QCISD(T)/6-311+G(3df,2p)//MP2=FULL/6-31G(d) level of theory
Added as a training reaction to Birad_R_Recombination
""",
)

entry(
    index = 21,
    label = "SO2 + CO <=> SO + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(48300, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[GlarBozz]""",
    longDesc =
u"""
Part of the "SOx" subset
Experimental shock tube measurement
Taken from: S.H. Bauer, P. Jeffers, A. Lifshitz, B.P. Jadava, Proceedings of the Eighth International Shock Tube Symposium, 1971, 13, 417
As reported by [GlarBozz] (8)
""",
)

entry(
    index = 22,
    label = "SO + O2 <=> SO2 + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.2e+03, 'cm^3/(mol*s)'), n=2.42, Ea=(3050, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(230, 'K'), Tmax=(2980, 'K')),
    shortDesc = u"""[GlarBozz]""",
    longDesc =
u"""
Part of the "SOx" subset
High T range (2570-2980 K) rate taken from experimental shock tube measurement: D. Woiki, P. Roth, Int. J. Chem. Kin., 1995, 27(1), 59-71, doi: 10.1002/kin.550270108
Low T range (230-420 K) rate taken from: [Baulch1992a]
As reported by [GlarBozz] (14)
""",
)

entry(
    index = 23,
    label = "S + SO2 <=> SO + SO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.89e+12, 'cm^3/(mol*s)'), n=0, Ea=(9034, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(1120, 'K'), Tmax=(1540, 'K')),
    shortDesc = u"""[Tezaki2003]""",
    longDesc =
u"""
Part of the "SOx" subset
Sock Tube
T range: 1120-1540 K
k2, p. 2467
""",
)

entry(
    index = 24,
    label = "H2S + O <=> HSO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.0e+13, 'cm^3/(mol*s)','+|-',1.52e+13), n=0, Ea=(7650, 'cal/mol','+|-',482), T0=(1, 'K'),
                         Tmin=(1520, 'K'), Tmax=(1820, 'K')),
    shortDesc = u"""[Dupre1993]""",
    longDesc =
u"""
Part of the "SOx" subset
Sock Tube
T range: 1520-1820 K
Uncertainty: A 38%, Ea 6.3%
""",
)

entry(
    index = 25,
    label = "SO3 + H2O + H2O <=> H2SO4 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.41e+07, 'cm^6/(mol^2*s)','+|-',2.82e+06), n=0, Ea=(-13500, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(283, 'K'), Tmax=(370, 'K')),
    shortDesc = u"""[Molina1997]""",
    longDesc =
u"""
Part of the "SOx" subset
Flow reactor
T range: 283-370 K, LOW!
Uncertainty: +/- 20%
Measured in 100-760 torr N2
""",
)

entry(
    index = 26,
    label = "HOSO2 <=> SO2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.34e+14, 's^-1'), n=0, Ea=(25832, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(150, 'K'), Tmax=(1500, 'K')),
    shortDesc = u"""[Somnitz2004]""",
    longDesc =
u"""
Part of the "SOx" subset
T range: 150-1500 K
k_dec_inf, p. 3847 in Fig. 2
calculated at the B3LYP/apVTZþ1//UB3LYP/apVTZþ1 level of theory
Also available in reverse from [Pilling2003], but for a relatively low T range (up to 673):
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(1.23e+12, 'cm^3/(mol*s)'), n=-0.27, Ea=(0, 'cal/mol'), T0=(300, 'K')),
        arrheniusLow = Arrhenius(A=(1.25e+17, 'cm^6/(mol^2*s)'), n=-4.09, Ea=(0, 'cal/mol'), T0=(300, 'K'))),
    Collider efficiencies taken from: Gimenez-Lopez, M. Martinez, A. Millera, R. Bilbao, M.U. Alzueta, Comb. Flame 2011, 158(1), 48-56, doi: 10.1016/j.combustflame.2010.07.017
""",
)

entry(
    index = 27,
    label = "COS + O <=> SO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.43e+13, 'cm^3/(mol*s)'), n=0, Ea=(4830, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(1120, 'K'), Tmax=(1540, 'K')),
    shortDesc = u"""[Tezaki2003]""",
    longDesc =
u"""
Part of the "COS" subset
Sock Tube
T range: 1120-1540 K
k1a
Calculated by a branching ratio givin in the paper
""",
)

entry(
    index = 28,
    label = "COS + O <=> S + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.73e+13, 'cm^3/(mol*s)'), n=0, Ea=(6900, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(1120, 'K'), Tmax=(1540, 'K')),
    shortDesc = u"""[Tezaki2003]""",
    longDesc =
u"""
Part of the "COS" subset
Sock Tube
T range: 1120-1540 K
k1b
Calculated by a branching ratio givin in the paper
""",
)

entry(
    index = 29,
    label = "COS + H <=> CO + SH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+14, 'cm^3/(mol*s)'), n=0, Ea=(6786, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(1170, 'K'), Tmax=(1830, 'K')),
    shortDesc = u"""[Roth1996a]""",
    longDesc =
u"""
Part of the "COS" subset
Sock Tube
T range: 1170-1830 K
""",
)

entry(
    index = 30,
    label = "CS2 + H <=> CS + SH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+15, 'cm^3/(mol*s)'), n=0, Ea=(18380, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(1170, 'K'), Tmax=(1830, 'K')),
    shortDesc = u"""[Roth1996a]""",
    longDesc =
u"""
Part of the "COS" subset
Sock Tube
T range: 1170-1830 K
""",
)

entry(
    index = 31,
    label = "COS <=> CO + S",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(2.45e+14, 'cm^3/(mol*s)'), n=0, Ea=(61400, 'cal/mol'), T0 = (1, 'K'),
                                 Tmin=(1140, 'K'), Tmax=(3230, 'K'))),
    shortDesc = u"""[Matsui1994]""",
    longDesc =
u"""
Part of the "COS" subset
Sock Tube
k1
T range: 1140-3230 K
Available from [Roth1993] as well, T range: 1830-3020 K (Sock Tube)
""",
)

entry(
    index = 32,
    label = "COS + S <=> CO + S2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.35e+13, 'cm^3/(mol*s)'), n=0, Ea=(6764, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(1140, 'K'), Tmax=(3230, 'K')),
    shortDesc = u"""[Matsui1994]""",
    longDesc =
u"""
Part of the "COS" subset
Sock Tube
k2
T range: 1140-3230 K
""",
)

entry(
    index = 33,
    label = "COS <=> CO + Sa",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(4.8e+22, 'cm^3/(mol*s)'), n=0, Ea=(71800, 'cal/mol'), T0 = (1, 'K'),
                                 Tmin=(1830, 'K'), Tmax=(3020, 'K'))),
    shortDesc = u"""[Roth1993]""",
    longDesc =
u"""
Part of the "COS" subset
T range: 1830-3020 K
Sock Tube
Measured in Ar
""",
)

entry(
    index = 34,
    label = "H2S + H <=> SH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.5e+07, 'cm^3/(mol*s)'), n=1.94, Ea=(904, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(190, 'K'), Tmax=(2237, 'K')),
    shortDesc = u"""[Marshall1999b]""",
    longDesc =
u"""
Part of the "HxSy" subset
Combined experimental (298-598 K) and computational calculation at the QCISD(T)/6-311+G(3df,2p) level
T range: 190-2237 K
Also available from [Roth1996a]
Added as a training reaction to H_Abstraction
""",
)

entry(
    index = 35,
    label = "H2S + S <=> SH + SH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.7e+06, 'cm^3/(mol*s)'), n=2.297, Ea=(9010, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(300, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Sendt2008]""",
    longDesc =
u"""
Part of the "HxSy" subset
k_abstraction, (R4a)
T range: 300-3000 K
calculations done at the MRCI/aug-cc-pV(Q+d)Z//MRCI/aug-cc-pVTZ level of theory
Added as a training reaction to H_Abstraction
""",
)

entry(
    index = 36,
    label = "S + H2 <=> SH + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.58e+14, 'cm^3/(mol*s)'), n=0, Ea=(19700, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(2740, 'K'), Tmax=(3570, 'K')),
    shortDesc = u"""[Matsui1996a]""",
    longDesc =
u"""
Part of the "HxSy" subset
Shock Tube
T range: 2740-3570 K
Added as a training reaction to H_Abstraction
""",
)

entry(
    index = 37,
    label = "S + CH4 <=> SH + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.04e+14, 'cm^3/(mol*s)'), n=0, Ea=(19910, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Matsui1996b]""",
    longDesc =
u"""
Part of the "HxSy" subset
k3
Shock Tube
T > 830 K
Added as a training reaction to H_Abstraction
""",
)

entry(
    index = 38,
    label = "S + C2H6 <=> SH + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.23e+14, 'cm^3/(mol*s)'), n=0, Ea=(14750, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Matsui1996b]""",
    longDesc =
u"""
Part of the "HxSy" subset
k4
Shock Tube
T > 830 K
More S + alkane reactions are available from the same source
Added as a training reaction to H_Abstraction
""",
)

entry(
    index = 39,
    label = "H2S <=> H2 + S",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.60e+24, 'cm^3/(mol*s)'), n=-2.613, Ea=(89173, 'cal/mol'), T0 = (1, 'K'),
                                 Tmin=(900, 'K'), Tmax=(3600, 'K'))),
    shortDesc = u"""[Matsui1998]""",
    longDesc =
u"""
Part of the "HxSy" subset
k1
Shock Tube
T range: 900-3600 K
""",
)

entry(
    index = 40,
    label = "H + S2 <=> HSS",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.60e+24, 'cm^6/(mol^2*s)'), n=-2.613, Ea=(89173, 'cal/mol'), T0 = (1, 'K'),
                                 Tmin=(873, 'K'), Tmax=(1423, 'K')),
        efficiencies={'N#N': 1, 'S': 1.1, '[Ar]': 0.88, '[He]': 1.39}),
    shortDesc = u"""[Sendt2002]""",
    longDesc =
u"""
Part of the "HxSy" subset
k6
UNIMOL calculation
Validated in T range: 873-1423 K
""",
)

entry(
    index = 41,
    label = "H + HSS <=> SH + SH",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(9.72e+07, 'cm^3/(mol*s)'), n=1.620, Ea=(-1030, 'cal/mol'), T0=(1, 'K'), Tmin=(873, 'K'), Tmax=(1423, 'K')),
            Arrhenius(A=(1.10e+13, 'cm^3/(mol*s)'), n=0.353, Ea=(210, 'cal/mol'), T0=(1, 'K'), Tmin=(873, 'K'), Tmax=(1423, 'K')),
        ],
    ),
    shortDesc = u"""[Sendt2002]""",
    longDesc =
u"""
Part of the "HxSy" subset
k7 + k8
TST\QRRK
Validated in T range: 873-1423 K
""",
)

entry(
    index = 42,
    label = "HSSH <=> SH + SH",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(2.31e+14, 'cm^3/(mol*s)'), n=1, Ea=(57030, 'cal/mol'), T0 = (1, 'K'),
                                 Tmin=(873, 'K'), Tmax=(1423, 'K')),
        efficiencies={'N#N': 1, 'S': 1.1, '[Ar]': 0.88, '[He]': 1.39}),
    shortDesc = u"""[Sendt2002]""",
    longDesc =
u"""
Part of the "HxSy" subset
k9
UNIMOL calculation
Validated in T range: 873-1423 K
""",
)

entry(
    index = 43,
    label = "SH + HSS <=> H2S + S2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.27e+03, 'cm^3/(mol*s)'), n=3.050, Ea=(-1105, 'cal/mol'), T0 = (1, 'K'),
                         Tmin=(873, 'K'), Tmax=(1423, 'K')),
    shortDesc = u"""[Sendt2002]""",
    longDesc =
u"""
Part of the "HxSy" subset
k10
TST
Validated in T range: 873-1423 K
""",
)

entry(
    index = 44,
    label = "H + HSS <=> H2 + S2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.23e+08, 'cm^3/(mol*s)'), n=1.653, Ea=(-1105, 'cal/mol'), T0 = (1, 'K'),
                         Tmin=(873, 'K'), Tmax=(1423, 'K')),
    shortDesc = u"""[Sendt2002]""",
    longDesc =
u"""
Part of the "HxSy" subset
k11
TST
Validated in T range: 873-1423 K
Added as a training reaction to H_Abstraction
""",
)

entry(
    index = 45,
    label = "H + HSS <=> H2S + S",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(6326, 'cal/mol'), T0 = (1, 'K'),
                         Tmin=(873, 'K'), Tmax=(1423, 'K')),
    shortDesc = u"""[Sendt2002]""",
    longDesc =
u"""
Part of the "HxSy" subset
k12
TST
Validated in T range: 873-1423 K
""",
)

entry(
    index = 46,
    label = "S + HSS <=> S2 + SH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.17e+06, 'cm^3/(mol*s)'), n=2.200, Ea=(-600, 'cal/mol'), T0 = (1, 'K'),
                         Tmin=(873, 'K'), Tmax=(1423, 'K')),
    shortDesc = u"""[Sendt2002]""",
    longDesc =
u"""
Part of the "HxSy" subset
k13
TST
Validated in T range: 873-1423 K
Added as a training reaction to H_Abstraction
""",
)

entry(
    index = 47,
    label = "HSS + HSS <=> HSSH + S2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.56e+00, 'cm^3/(mol*s)'), n=3.370, Ea=(-1672, 'cal/mol'), T0 = (1, 'K'),
                         Tmin=(873, 'K'), Tmax=(1423, 'K')),
    shortDesc = u"""[Sendt2002]""",
    longDesc =
u"""
Part of the "HxSy" subset
k14
TST
Validated in T range: 873-1423 K
Added as a training reaction to H_Abstraction
""",
)

entry(
    index = 48,
    label = "HSSH + H <=> HSS + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.99e+07, 'cm^3/(mol*s)'), n=1.933, Ea=(-1408, 'cal/mol'), T0 = (1, 'K'),
                         Tmin=(873, 'K'), Tmax=(1423, 'K')),
    shortDesc = u"""[Sendt2002]""",
    longDesc =
u"""
Part of the "HxSy" subset
k15
TST
Validated in T range: 873-1423 K
Added as a training reaction to H_Abstraction
""",
)

entry(
    index = 49,
    label = "HSSH + H <=> H2S + SH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.66e+08, 'cm^3/(mol*s)'), n=1.724, Ea=(467, 'cal/mol'), T0 = (1, 'K'),
                         Tmin=(873, 'K'), Tmax=(1423, 'K')),
    shortDesc = u"""[Sendt2002]""",
    longDesc =
u"""
Part of the "HxSy" subset
k16
TST
Validated in T range: 873-1423 K
""",
)

entry(
    index = 50,
    label = "HSSH + SH <=> H2S + HSS",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.40e+03, 'cm^3/(mol*s)'), n=2.980, Ea=(-1480, 'cal/mol'), T0 = (1, 'K'),
                         Tmin=(873, 'K'), Tmax=(1423, 'K')),
    shortDesc = u"""[Sendt2002]""",
    longDesc =
u"""
Part of the "HxSy" subset
k17
TST
Validated in T range: 873-1423 K
Added as a training reaction to H_Abstraction
""",
)

entry(
    index = 51,
    label = "HSSH + S <=> HSS + SH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.85e+06, 'cm^3/(mol*s)'), n=2.310, Ea=(-1204, 'cal/mol'), T0 = (1, 'K'),
                         Tmin=(873, 'K'), Tmax=(1423, 'K')),
    shortDesc = u"""[Sendt2002]""",
    longDesc =
u"""
Part of the "HxSy" subset
k18
TST
Validated in T range: 873-1423 K
Added as a training reaction to H_Abstraction
""",
)

entry(
    index = 52,
    label = "CH3SH + H <=> CH3S + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.39e+08, 'cm^3/(mol*s)'), n=1.729, Ea=(986, 'cal/mol'), T0 = (1, 'K'),
                         Tmin=(200, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Marshall2015b]""",
    longDesc =
u"""
Part of the "CxHySz" subset
Table 5, R1
T range: 200-3000 K
calculations done at the QCISD/6-311G(d,p) level
Train!
""",
)

entry(
    index = 53,
    label = "CH3SH + H <=> CH2SH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.16e+03, 'cm^3/(mol*s)'), n=2.925, Ea=(4747, 'cal/mol'), T0 = (1, 'K'),
                         Tmin=(250, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Marshall2015b]""",
    longDesc =
u"""
Part of the "CxHySz" subset
Table 5, R2
T range: 250-3000 K
calculations done at the QCISD/6-311G(d,p) level
""",
)

entry(
    index = 54,
    label = "CH3SH + H <=> CH3 + H2S",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.17e+10, 'cm^3/(mol*s)'), n=0.766, Ea=(3225, 'cal/mol'), T0 = (1, 'K'),
                         Tmin=(200, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Marshall2015b]""",
    longDesc =
u"""
Part of the "CxHySz" subset
Table 5, R3
T range: 200-3000 K
calculations done at the QCISD/6-311G(d,p) level
""",
)

entry(
    index = 55,
    label = "CH3SH + H <=> CH4 + SH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.99e+06, 'cm^3/(mol*s)'), n=1.983, Ea=(16536, 'cal/mol'), T0 = (1, 'K'),
                         Tmin=(400, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Marshall2015b]""",
    longDesc =
u"""
Part of the "CxHySz" subset
Table 5, R3
T range: 400-3000 K
calculations done at the QCISD/6-311G(d,p) level
""",
)

entry(
    index = 56,
    label = "S + C2H2 <=> HCCS + H",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.26e+13, 'cm^3/(mol*s)'), n=0.00, Ea=(2677, 'cal/mol'), T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(1000, 'K')),
        arrheniusLow = Arrhenius(A=(3.6e+29, 'cm^6/(mol^2*s)'), n=-3.55, Ea=(3955, 'cal/mol'), T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(1000, 'K')),
        alpha=0.60, T3=(1e-30, 'K'), T1=(1e+30, 'K'), efficiencies={}),
    shortDesc = u"""[Marshall2015a]""",
    longDesc =
u"""
Part of the "C-S" mechanism
T range: 300-1000 K
""",
)

entry(
    index = 57,
    label = "S + CS2 <=> CS + S2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.87e+13, 'cm^3/(mol*s)'), n=0.00, Ea=(8843, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(690, 'K'), Tmax=(1040, 'K')),
    shortDesc = u"""[Marshall2011]""",
    longDesc =
u"""
Part of the "C-S" mechanism
T range: 690-1040 K
""",
)

entry(
    index = 58,
    label = "NS + NO2 <=> N2 + SO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.55e+13, 'cm^3/(mol*s)'), n=-1.10, Ea=(0, 'cal/mol'), T0=(295, 'K')),
    shortDesc = u"""[Pilling2002]""",
    longDesc =
u"""
Part of the "SOx-NOx" direct interactions subset
calculations done at the BD-(T)//B3LYP/6-31G++ level of theory
""",
)

entry(
    index = 59,
    label = "NO2 + SO2 <=> NO + SO3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.31e+12, 'cm^3/(mol*s)'), n=0, Ea=(53700, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(700, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"""[Palmer1977]""",
    longDesc =
u"""
Part of the "SOx-NOx" direct interactions subset
T range: 700-2000 K
Shock tube measurement
Also given by [doi: 10.1016/S0010-2180(71)80077-9] for 700-1200 K
""",
)

entry(
    index = 60,
    label = "NO2 + S <=> SO + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.14e+13, 'cm^3/(mol*s)'), n=0, Ea=(-980, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(292, 'K'), Tmax=(656, 'K')),
    shortDesc = u"""[Marshall2012]""",
    longDesc =
u"""
Part of the "SOx-NOx" direct interactions subset
T range: 292-656 K
Experimentally measured, and PES verified using QCISD/6-311G(d,p)
""",
)

entry(
    index = 61,
    label = "S + NO <=> SNO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.3e+14, 'cm^3/(mol*s)'), n=0.24, Ea=(0, 'cal/mol'), T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(800, 'K')),
        arrheniusLow = Arrhenius(A=(2.25e+15, 'cm^6/(mol^2*s)'), n=0, Ea=(-1868, 'cal/mol'), T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(800, 'K')),
        alpha=0.22, T3=(7445, 'K'), T1=(1e-30, 'K'), efficiencies={}),
    shortDesc = u"""[Marshall2004]""",
    longDesc =
u"""
Part of the "SOx-NOx" direct interactions subset
T range: 300-800 K
Experimentally measured, and PES verified using CBS-QB3
Added as a training reaction to Birad_R_Recombination
""",
)

entry(
    index = 62,
    label = "S + NO <=> SO + N",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.08e+14, 'cm^3/(mol*s)'), n=0, Ea=(40100, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(2420, 'K'), Tmax=(3870, 'K')),
    shortDesc = u"""[Roth1996b]""",
    longDesc =
u"""
Part of the "SOx-NOx" direct interactions subset
T range: 2420-3870 K
Shock tube
The overall rate "S + NO <=> products" was determined, and the branching ratio for SO + N products is 80%-95%.
A branching ratio of 90% was ASSUMED here.
""",
)

entry(
    index = 63,
    label = "S + NO <=> NS + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(40100, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(2420, 'K'), Tmax=(3870, 'K')),
    shortDesc = u"""[Roth1996b]""",
    longDesc =
u"""
Part of the "SOx-NOx" direct interactions subset
T range: 2420-3870 K
Shock tube
The overall rate "S + NO <=> products" was determined, and the branching ratio for NS + O products is 5%-20%.
A branching ratio of 10% was ASSUMED here.
""",
)

entry(
    index = 64,
    label = "HOSO2 + O2 <=> SO3 + HO2",
    degeneracy = 1,
    duplicate=True,
    kinetics = Arrhenius(A=(1.84751e-06, 'cm^3/(mol*s)','*|/',5.17556), n=5.40472, Ea=(94.0211, 'kJ/mol'), T0=(1, 'K'),
                         Tmin=(300, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"""CBS-QB3""",
    longDesc =
u"""
Calculated by Yi-Pei Li
HOSO2 + O2 -> TS2 -> SO3 + HO2
Disproportionation reaction
Bath gas: N2
""",
)

entry(
    index = 65,
    label = "HOSO2 + O2 <=> SO3 + HO2",
    degeneracy = 1,
    duplicate=True,
    kinetics = Chebyshev(
        coeffs = [
            [12.2121, -0.0588331, -0.0369469, -0.0170237],
            [-0.966321, 0.0601562, 0.0379397, 0.0176167],
            [-0.198689, 0.00650242, 0.00363656, 0.00127762],
            [0.0023904, -0.00384118, -0.00232335, -0.000985026],
            [0.0234029, -0.00579278, -0.0033169, -0.0012383],
            [0.0162687, 3.28822e-06, -5.07497e-05, -7.44263e-05],
        ],
        kunits = 'cm^3/(mol*s)',Tmin = (300, 'K'),Tmax = (2000, 'K'),Pmin = (0.01, 'bar'),Pmax = (100, 'bar')),
    shortDesc = u"""CBS-QB3""",
    longDesc =
u"""
Calculated by Yi-Pei Li
HO + O2 -> SOSO4 -> TS1 -> SO3-HO2 (VDW complex) -> SO3 + HO2
Bath gas: N2
""",
)

entry(
    index = 66,
    label = "SO2(T) <=> SO2",
    degeneracy = 1,
    duplicate=True,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.82e+16, 'cm^3/(mol*s)'), n=0, Ea=(2800, 'cal/mol'), T0 = (1, 'K'),
                                 Tmin=(298, 'K'), Tmax=(400, 'K'))),
    shortDesc = u"""[Calvert1973]""",
    longDesc =
u"""
Experimental measurement
Value for CO2 as third body collider was taken here
p. 680, Table V
T range: 298-400 K
""",
)
