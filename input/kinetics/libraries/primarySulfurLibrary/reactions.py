#!/usr/bin/env python
# encoding: utf-8

name = "primarySulfurLibrary"
shortDesc = u"primarySulfurLibrary"
longDesc =u"""
This library includes important sulfur-related reactions.
Prepared by Alon Grinberg Dana

This library consists of the following subsets:
* SOx
* COS
* HxSy
* CxHySz
* C-S
* HOSO2 + O2 surface

Reference legend:
[Baulch1992a] D.L. Baulch, C.J. Cobos, R.A. Cox, C. Esser, P. Frank, Th. Just, J.A. Kerr, M.J. Philling, J. Troe, R.W. Walker, J. Warnatz, "Evaluated Kinetic Data for Combustion Modelling", Journal of Physical and Chemical Reference Data, 1992, 21(3), 411, doi: 10.1063/1.555908
[Calvert1973] F.B. Wampler, K. Otsuka, J.G. Calvert, E.K. Damon, Int. J. Chem. Kin., 1973, 5(4), 669-690, doi: 10.1002/kin.550050417
[Dupre1993] K. Tsuchiya, H. Matsui, M. Oya, G. Dupre, in: R. Burn, L.Z. Dumitrescu (Ed.) Shock Waves @ Marseille II (Proceedings Marseille France), 1993, 71-76, doi: 10.1007/978-3-642-78832-1
[Garland1998] N.L. Garland, Chem. Phys. Lett., 1998, 290(4-6), 385-390, doi: 10.1016/S0009-2614(98)00553-3
[GlarBozz] (RMG's Sulfur/GlarborgBozzelli library) P. Glarborg, D. Kubel, K. Dam-Johansen, H-M. Chiang, J.W. Bozzelli, Int. J. Chem. Kin., 1996, 28, 773-790, doi: 10.1002/(SICI)1097-4601(1996)28:10<773::AID-KIN8>3.0.CO;2-K
[Haynes2013] Chenlai (Ryan) Zhou, Karina Sendt, Brian S. Haynes, Proceedings of the Combustion Institute 2013, 34(1), 625-632, doi: 10.1016/j.proci.2012.05.083
[Lin2003a] C-W. Lu, Y-J. Wu, Y-P. Lee, R.S. Zhu, M.C. Lin, J. Phys. Chem. A, 2003, 107(50), 11020-11029, doi: 10.1021/jp036025c
[Lin2004] C-W. Lu, Y-J. Wu, Y-P. Lee, R.S. Zhu, M.C. Lin, J. Chem. Phys., 2004, 121(17), 8271-8278, doi: 10.1063/1.1792611
[Marshall1995] A. Goumri, D. Laakso, J‐D.R. Rocha, C.E. Smith, P. Marshall, J. Chem. Phys., 1995, 102, 161-169, doi: 10.1063/1.469387
[Marshall1999a] A. Goumri, J-D.R. Rocha, D. Laakso, C.E. Smith, P. Marshall, J. Phys. Chem. A, 1999, 103(51), 11328-11335 doi: 10.1021/jp9924070
[Marshall1999b] J. Peng, X. Hu, P. Marshall, J. Phys. Chem. A, 1999, 103, 5307-5311, doi: 10.1021/jp984242l
[Marshall2004] A. Goumri, D.D. Shao, P. Marshall, J. Chem. Phys., 2004, 121, 9999, doi: 10.1063/1.1806419
[Marshall2005] J. Naidoo, A. Goumri, P. Marshall, Proceedings of the Combustion Institute, 2005, 30(1), 1219-1225, doi: 10.1016/j.proci.2004.08.214
[Marshall2006] A. Yilmaz, L. Hindiyarti, A.D. Jensen, P. Glarbotg, P. Marshall, J. Phys. Chem. A, 2006, 110 (21), 6654-6659, doi: 10.1021/jp0557215
[Marshall2007a] L. Hindiyarti, P. Glarborg, P. Marshall, J. Phys. Chem. A, 2007, 111(19), 3984-3991, doi: 10.1021/jp067499p
[Marshall2007b] C.L. Rasmussen, P. Glarborg, P. Marshall, Proceedings of the Combustion Institute, 2007, 31, 339-347, doi: 10.1016/j.proci.2006.07.249
[Marshall2011a] Y. Gao, P. Marshall, J. Chem. Phys., 2011, 135, 144306, doi: 10.1063/1.3644773
[Marshall2011b] Y. Gao, C.R. Zhou, K. Sendt, B.S. Haynes, P. Marshall, Proc. Comb. Inst., 2011, 33, 459-465, doi: 10.1016/j.proci.2010.05.020
[Marshall2012] K.M. Thompson, Y. Gao, P. Marshall, Int. J. Chem. Kin., 2012, 44(1), 90-99, doi: 10.1002/kin.20612
[Marshall2015a] S. Ayling, Y. Gao, P. Marshall, Proceedings of the Combustion Institute, 2015, 35(1), 215-222, doi: 10.1016/j.proci.2014.05.079
[Marshall2015b] K.E. Kerr, I.M. Alecu, K.M. Thompson, Y. Gao, P. Marshall, J. Phys. CHem. A, 2015, 119, 7352-7360, doi: 10.1021/jp512966a
[Matsui1994] M. Oya, H. Shiina, K. Tsuchiya, H. Matsui, Bulletin of the Chemical Society of Japan, 1994, 67(8), 2311-2313, doi: 10.1246/bcsj.67.2311
[Matsui1996a] H. Shiina, M. Oya, K. Yamashita, A. Miyoshi, H. Matsui, J. Phys. Chem., 1996, 100(6), 2136-2140, doi: 10.1021/jp952472j
[Matsui1996b] K. Tsuchiya, K. Yamashita, A. Miyoshi, H. Matsui, J. Phys. Chem., 1996, 100(43), 17202-17206, doi: 10.1021/jp961252i
[Matsui1997] K. Tsuchiya, K. Kamiya, H. Matsui, Int. J. Chem. Kin., 1997, 29(1), 57-66, doi: 10.1002/(SICI)1097-4601(1997)29:1<57::AID-KIN7>3.0.CO;2-K
[Matsui1998] H. Shiina, A. Miyoshi, H. Matsui, J. Phys. Chem. A, 1998, 102(20), 3556-3559, doi: 10.1021/jp980650d
[Molina1997] J.T. Jayne, U. Poschl, Y-m. Chen, D. Dai, L.T. Molina, D.R. Worsnop, C.E. Kolb, M.J. Molina, J. Phys. Chem. A, 1997, 101(51), 10000-10011, doi: 10.1021/jp972549z
[Mukarami1980] T. Higashihara, K. Saito, I. Murakami, Bulletin of the Chemical Society of Japan, 1980, 53(1), 15-18, doi: 10.1246/bcsj.53.15
[Palmer1977] H. Freund, H.B. Palmer, Int. J. Chem. Kin., 1977, 9(6), 887-905, doi: 10.1002/kin.550090605
[Peterson2008] S. Du, J.S. Francisco, B.C. Shepler, K.A. Peterson, J. Chem. Phys., 2008, 128, 204306, doi: 10.1063/1.2919569
[Pilling2002a] M.A. Blitz, K.W. McKee, M.J. Pilling, J. Phys. Chem. A, 2002, 106(36), 8406-8410, doi: 10.1021/jp025508y
[Pilling2002b] K.J. Hughes, M.A. Blitz, M.J. Pilling, S.H. Robertson, Proc. Comb. Inst., 2002, 29(2), 2431-2437, doi: 10.1016/S1540-7489(02)80296-6
[Pilling2003] M.A. Blitz, K.J. Hughes, M.J. Pilling, J. Phys. Chem. A, 2003, 107(12), 1971-1978, doi: 10.1021/jp026524y
[Pilling2006] M.A. Blitz, K.J. Hughes, M.J. Pilling, S.H. Robertson, J. Phys. Chem. A, 2006, 110(9), 2996-3009, doi: 10.1021/jp054722u
[Rabinowitz2010] S.M. Hwang, J.A. Cooke, K.J. De Witt, M.J. Rabinowitz, Int. J. Chem. Kin., 2010, 42(3), 168-180, doi: 10.1002/kin.20472
[Roth1993] D. Woiki, P. Roth, in: R. Burn, L.Z. Dumitrescu (Ed.) Shock Waves @ Marseille II (Proceedings Marseille France), 1993, 53-58, doi: 10.1007/978-3-642-78832-1_9
[Roth1996a] D. Woiki, P. Roth, Israel Journal of Chemistry, 1996, 36(3), 279-283, doi: 10.1002/ijch.199600039
[Roth1996b] D. Woiki, P. Roth, Symposium (International) on Combustion, 1996, 26(1), 583-588, doi: 10.1016/S0082-0784(96)80263-3
[Sendt2002] K. Sendt, M. Jazbec, B.S. Haynes, Proceedings of the Combustion Institute, 2002, 29, 2439-2446, doi: 10.1016/S1540-7489(02)80297-8
[Sendt2007] K. Sendt, B.S. Haynes, Proceedings of the Combustion Institute, 2007, 31(1), 257-265, doi: 10.1016/j.proci.2006.08.067
[Sendt2008] C.R. Zhou, K. Sendt, B.S. Haynes, J. Phys. Chem. A, 2008, 112, 3239-3247, doi: 10.1021/jp710488d
[Sendt2009a] C.R. Zhou, K. Sendt, B.S. Haynes, J. Phys. Chem. A, 2009, 113, 2975-2981, doi: 10.1021/jp810105e
[Sendt2009b] C.R. Zhou, K. Sendt, B.S. Haynes, J. Phys. Chem. A, 2009, 113, 8299-8306, doi: 10.1021/jp903185k
[Sitha2011] S. Sitha, L.L. Jewell, S.J. Piketh, G. Fourie, Atmospheric Rnvironment, 2011, 45, 745-754, doi: 10.1016/j.atmosenv.2010.09.018
[Somnitz2004] H. Somnitz, Phys. Chem. Chem. Phys., 2004, 6(14), 3844-3851, doi: 10.1039/B317055A
[Tezaki2003] N. Isshiki, Y. Murakami, K. Tsuchiya, A. Tezaki, H. Matsui, J. Phys. Chem. A, 2003, 107(14), 2464-2469, doi: 10.1021/jp0200829
[Troe1984] H.J. Plach, J. Troe, Int. J. Chem. Kin., 1984, 16(12), 1531-1542, doi: 10.1002/kin.550161207
[Truhlar2007] B.A. Ellingson, D.G. Truhlar, JACS 2007, 129(42), 12765-12771, doi: 10.1021/ja072538b
"""

entry(
    index = 1,
    label = "S + S <=> S2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.40e+14, 'cm^6/(mol^2*s)'), n=-0.09, Ea=(-331, 'cal/mol'), T0=(1, 'K'),
                                 Tmin=(100, 'K'), Tmax=(6000, 'K'))),
    shortDesc = u"""[Mukarami1980],[Peterson2008]""",
    longDesc =
u"""
Part of the "SOx" mechanism
The rate here was determined by combining low and high T experimental data.
Low T data was taken from [Peterson2008] in the 100-500 K range (theoretical - quasiclassical trajectory)
High T data was taken from [Mukarami1980] in the 4500-6000 K (experimental)
The rate by [Mukarami1980] was first reversed using thermo from [Haynes2013]
([Lin2003a] reports [Mukarami1980]'s rate as k26, which is probably problematic for combustion temperatures)
""",
)

entry(
    index = 2,
    label = "SO + O <=> SO2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.75e+17, 'cm^6/(mol^2*s)'), n=-2.17, Ea=(0, 'cal/mol'), T0=(298, 'K')),
        efficiencies = {'O=S=O': 10, 'O': 10, 'N#N': 1.5},
    ),
    shortDesc = u"""[Lin2003a]""",
    longDesc =
u"""
Part of the "SOx" mechanism
k10a
calculations done at the G2M(RCC2)//B3LYP/6-311+(3df) level of theory
also validated experimentally in the same study
efficiencies from: Y. Song, H. Hashemi, J.M. Christensen, C. Zou, B.S. Haynes, P. Marshall, P. Glarborg
International Journal of Chemical Kinetics 49(1), 2017, 37-52
doi: 10.1002/kin.21055
Also available from [Lin2003a] in reverse:
    label = "SO2 <=> SO + O",
    kinetics = Arrhenius(A=(2.84e+16, 'cm^3/(mol*s)'), n=0, Ea=(109674, 'cal/mol'), T0=(1, 'K')),
""",
)

entry(
    index = 3,
    label = "S + O2 <=> SO + O",
    degeneracy = 2,
    kinetics=Arrhenius(A=(5.43e+05, 'cm^3/(mol*s)', '+|-', 1.63E+04), n=2.11, Ea=(-1451, 'cal/mol', '+|-', 238),
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

This reaction appears in the GlarborgH2S library with N2 efficiency = 1.
Pay attention when using along with this SOx library: if GlarborgH2S has priority over SOx, the reaction for N2 as the
third body collider will appear twice: once with N2 efficiency = 1,
and once as a specific collider as in SO2 + O (+N2) <=> SO3 (+N2)
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
    degeneracy = 2,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.59e+12, 'cm^3/(mol*s)'), n=1.63, Ea=(7339, 'cal/mol'), T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(1700, 'K')),
        arrheniusLow = Arrhenius(A=(1.14e+22, 'cm^6/(mol^2*s)'), n=-6.14, Ea=(11075, 'cal/mol'), T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(1700, 'K')),
        alpha=0.283, T3=(272, 'K'), T1=(3995, 'K'), efficiencies={'O=S=O': 10, 'O': 10, 'O=C=O': 2.5}),
    shortDesc = u"""[Pilling2006]""",
    longDesc =
u"""
Part of the "SOx" mechanism
T range: 300-1700 K
k2, Table 3
efficiencies taken from Gimenez-Lopez, M. Martinez, A. Millera, R. Bilbao, M.U. Alzueta, Comb. Flame 2011, 158(1), 48-56, doi: 10.1016/j.combustflame.2010.07.017
Added as a training reaction to R_Addition_MultipleBond
Also available from [Pilling2002b]
""",
)

entry(
    index = 8,
    label = "SO2 + H <=> HSO2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(4.61e+12, 'cm^3/(mol*s)'), n=1.59, Ea=(2472, 'cal/mol'), T0=(300, 'K'), Tmin=(200, 'K'), Tmax=(1000, 'K')),
        arrheniusLow = Arrhenius(A=(1.97e+18, 'cm^6/(mol^2*s)'), n=-5.19, Ea=(4513, 'cal/mol'), T0=(300, 'K'), Tmin=(200, 'K'), Tmax=(1000, 'K')),
        alpha=0.390, T3=(167, 'K'), T1=(2191, 'K'), efficiencies={'O=S=O': 10, 'O': 10, 'O=C=O': 2.5}),
    shortDesc = u"""[Pilling2006]""",
    longDesc =
u"""
Part of the "SOx" mechanism
T range: 200-1000 K
k1, Table 3
efficiencies taken from Gimenez-Lopez, M. Martinez, A. Millera, R. Bilbao, M.U. Alzueta, Comb. Flame 2011, 158(1), 48-56, doi: 10.1016/j.combustflame.2010.07.017
Also available from [Pilling2002b]
""",
)

entry(
    index = 9,
    label = "SO2 + H <=> SO + OH",
    degeneracy = 2,
    kinetics = Arrhenius(A=(6.74e+21, 'cm^3/(mol*s)'), n=-2.22, Ea=(30736, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(300, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"""[Pilling2002b]""",
    longDesc =
u"""
Part of the "SOx" mechanism
Also available from [Pilling2006]
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(6.68e+32, 'cm^3/(mol*s)'), n=2.77, Ea=(20848, 'cal/mol'), T0=(300, 'K'), Tmin=(900, 'K'), Tmax=(1800, 'K')),
        arrheniusLow = Arrhenius(A=(1.64e+40, 'cm^6/(mol^2*s)'), n=-2.30, Ea=(30965, 'cal/mol'), T0=(300, 'K'), Tmin=(900, 'K'), Tmax=(1800, 'K')),
        alpha=1, T3=(272, 'K'), T1=(27617, 'K')),
    T range: 900-1800 K
    k3, Table 3
The rate from [Pilling2002b] was taken over [Pilling2006] since the units of this reaction aren't clear in [Pilling2006],
and using the common-sence units according to reaction order led to convergence issue in Chemkin (but surprisingly, not in RMG)
""",
)

entry(
    index = 10,
    label = "SO3 + H <=> SO2 + OH",
    degeneracy = 3,
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
    degeneracy = 3,
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
    degeneracy = 3,
    kinetics = Arrhenius(A=(4.8e+04, 'cm^3/(mol*s)'), n=2.46, Ea=(27225, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(800, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"""[Marshall2007a]""",
    longDesc =
u"""
Part of the "SOx" mechanism
T range: 800-2000 K
calculations done at the CBS-QB3/CCSD(T)//B3LYP/6-311G(2d,d,p) level of theory
Also available from Varandas 2007 in 1400-2200 K, doi: 10.1016/j.cplett.2007.03.112
Also available from [Rabinowitz2010]
""",
)

entry(
    index = 13,
    label = "SO + HO2 <=> SO2 + OH",
    degeneracy = 2,
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
    degeneracy = 2,
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
    label = "SH + O2 <=> SO + OH",
    degeneracy = 2,
    kinetics = Arrhenius(A=(7.5e+04, 'cm^3/(mol*s)'), n=2.052, Ea=(16396, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(300, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"""[Sendt2009a]""",
    longDesc =
u"""
Part of the "SOx" subset
k1b
Table 7 on p. 11333
calculations done at the MRCI/aug-cc-pV(Q+d)Z//CASSCF/cc-pVTZ level of theory
""",
)

entry(
    index = 20,
    label = "SH + O2 <=> HSO + O",
    degeneracy = 2,
    kinetics = Arrhenius(A=(2.3e+06, 'cm^3/(mol*s)'), n=1.816, Ea=(20005, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(300, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"""[Sendt2009a]""",
    longDesc =
u"""
Part of the "SOx" subset
k1c
calculations done at the MRCI/aug-cc-pV(Q+d)Z//CASSCF/cc-pVTZ level of theory
""",
)

entry(
    index = 21,
    label = "HOSO <=> SO + OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(9.94e+21, 's^-1'), n=-2.54, Ea=(75891, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2000, 'K')),
        arrheniusLow = Arrhenius(A=(1.16e+46, 'cm^3/(mol*s)'), n=-9.02, Ea=(52953, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2000, 'K')),
        alpha=0.95, T3=(2989, 'K'), T1=(1.1, 'K'), efficiencies={'O=S=O': 10, 'O': 10, 'O=C=O': 2.5}),
    shortDesc = u"""[Pilling2002b]""",
    longDesc =
u"""
Part of the "SOx" subset
RRKM
Also available from [Marshall1999a]:
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(1.65e+16, 's^-1'), n=-0.32, Ea=(67720, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(2000, 'K')),
        arrheniusLow = Arrhenius(A=(1.25e+32, 'cm^3/(mol*s)'), n=-4.33, Ea=(69115, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(2000, 'K'))),
T range: 200-2000 K
Table 7 on p. 11333
calculations done at the QCISD(T)/6-311+G(3df,2p)//MP2=FULL/6-31G(d) level of theory
""",
)

entry(
    index = 22,
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
    index = 77,
    label = "HSO2 <=> HSO + O",
    degeneracy = 2,
    kinetics = Arrhenius(A=(2.02e+13, 's^-1'), n=0, Ea=(88, 'kcal/mol'), T0=(1, 'K')),
    shortDesc = u"""estimated by alongd""",
    longDesc =
u"""
The rate was estimated as follows:

The A factor is taken from the reaction HSO2 <=> SO2 + H
which is taken from [Pilling2006] where the reverse reaction SO2 + H <=> HSO2 (k1) and Keq are given.
(k1 high-P):  3.76e+07 * T^1.59 * exp(-2472 cal/mol / RT), cm^3/mol*s  (originally fitted only in 200-1000K)
(Keq,1):      4.72e-02 * T^0.28 * exp(-16273 cal/mol / RT), cm^3/mol
High-P limit k(-1) is calculated and fitted here into a two parameter Arrhenius form:
(k-1, highP): 2.02e+13 * exp(-11963 cal/mol / RT), s^-1
A = 2.02e+13 s^-1

The Ea is taken as the bond energy of S=O in HSO2:
Ea = H(HSO) + H(O) - H(HSO2)     (values taken at 1000 K)
Ea = 2.19 + 63.12 - (-22.66) =~ 88.0 kcal/mol

k(T) = 2.02e+13 * exp(88 kcal/mol / RT) cm3/mol*s

Also available in reverse from the GlarborgH2S library (doi: 10.1002/kin.21055):
    entry(
        index = 86,
        label = "HSO + O <=> HSO2",
        degeneracy = 1,
        kinetics = ThirdBody(
            arrheniusLow = Arrhenius(
                A = (1.1e+19, 'cm^6/(mol^2*s)'),
                n = -1.73,
                Ea = (-50, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            efficiencies = {},
        ),
        longDesc = u"P Glarborg D Kubel K Dam-Johansen H-M Chiang JW Bozzelli Int J Chem Kinet 28 (1996) 773-790",
    The source P Glarborg D Kubel K Dam-Johansen H-M Chiang JW Bozzelli Int J Chem Kinet 28 (1996) 773-790
    directs to ref 35 in that paper which could not be found.
)
""",
)

entry(
    index = 23,
    label = "SO2 + CO <=> SO + CO2",
    degeneracy = 2,
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
    index = 24,
    label = "SO + O2 <=> SO2 + O",
    degeneracy = 2,
    kinetics = Arrhenius(A=(9.03e+06, 'cm^3/(mol*s)'), n=1.4, Ea=(3712, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(250, 'K'), Tmax=(3500, 'K')),
    shortDesc = u"""[Garland1998]""",
    longDesc =
u"""
Part of the "SOx" subset

Also available from [GlarBozz] (14) combining low T from [Baulch1992a] and high T from: D. Woiki, P. Roth, Int. J. Chem. Kin., 1995, 27(1), 59-71, doi: 10.1002/kin.550270108
Also available from [Matsui1997]
""",
)

entry(
    index = 25,
    label = "SO2 + S <=> SO + SO",
    degeneracy = 2,
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
    index = 26,
    label = "H2S + O <=> HSO + H",
    degeneracy = 2,
    kinetics = Arrhenius(A=(1.4e+09, 'cm^3/(mol*s)'), n=1.10, Ea=(5099, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Marshall1995]""",
    longDesc =
u"""
Part of the "SOx" subset
RRKM
QCISD(T)/6-311+G(3df,2p)//MP2=FULL/6-31G(d)
k1b
As reported by:
Y. Song, H. Hashemi, J.M. Christensen, C. Zou, B.S. Haynes, P. Marshall, P. Glarborg
International Journal of Chemical Kinetics 49(1), 2017, 37-52
doi: 10.1002/kin.21055

Also available from [Dupre1993]:
    kinetics = Arrhenius(A=(4.0e+13, 'cm^3/(mol*s)','+|-',1.52e+13), n=0, Ea=(7650, 'cal/mol','+|-',482), T0=(1, 'K'),
                         Tmin=(1520, 'K'), Tmax=(1820, 'K')),
Sock Tube, Uncertainty: A 38%, Ea 6.3%
""",
)

entry(
    index = 27,
    label = "H2S + O <=> SH + OH",
    degeneracy = 2,
    kinetics = Arrhenius(A=(7.47e+07, 'cm^3/(mol*s)','+|-',4.48e+06), n=1.746, Ea=(2895, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(200, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"""[Marshall1995]""",
    longDesc =
u"""
RRKM
QCISD(T)/6-311+G(3df,2p)//MP2=FULL/6-31G(d)
k1a
""",
)

entry(
    index = 28,
    label = "HOS + H <=> SO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.79e+07, 'cm^3/(mol*s)'), n=1.94, Ea=(1590, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(298, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"""[Marshall1995]""",
    longDesc =
u"""
RRKM
QCISD(T)/6-311+G(3df,2p)//MP2=FULL/6-31G(d)
""",
)

entry(
    index = 29,
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
    index = 30,
    label = "SO2 + OH <=> HOSO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.26e+06, 'cm^3/(mol*s)','*|/',1.12511), n=1.98, Ea=(153, 'cal/mol','+|-',14.4),
                         T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(1025, 'K')),
    shortDesc = u"""[Sitha2011]""",
    longDesc =
u"""
Part of the "SOx" subset
Calculated at QCISD/6-31++G(2df,2p)
Arrhenius parameters generated from discrete values given in the paper

Also available from [Pilling2003], but for a relatively low T range (up to 673):
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(1.23e+12, 'cm^3/(mol*s)'), n=-0.27, Ea=(0, 'cal/mol'), T0=(300, 'K')),
        arrheniusLow = Arrhenius(A=(1.25e+17, 'cm^6/(mol^2*s)'), n=-4.09, Ea=(0, 'cal/mol'), T0=(300, 'K'))),
    Collider efficiencies taken from: Gimenez-Lopez, M. Martinez, A. Millera, R. Bilbao, M.U. Alzueta, Comb. Flame 2011, 158(1), 48-56, doi: 10.1016/j.combustflame.2010.07.017

Also available (in reverse) from [Somnitz2004]:
    kinetics = Arrhenius(A=(4.34e+14, 's^-1'), n=0, Ea=(25832, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(150, 'K'), Tmax=(1500, 'K')),
    k_dec_inf, p. 3847 in Fig. 2
    calculated at the B3LYP/apVTZþ1//UB3LYP/apVTZþ1 level of theory

Also available from doi: 10.1039/A901596E
Also available from doi: 10.1039/B317055A
""",
)

entry(
    index = 31,
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
    index = 32,
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
    index = 33,
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
    index = 34,
    label = "CS2 + H <=> CS + SH",
    degeneracy = 2,
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
    index = 35,
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
    index = 36,
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
    index = 37,
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
    index = 38,
    label = "H2S + H <=> SH + H2",
    degeneracy = 2,
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
    index = 39,
    label = "H2S + S <=> SH + SH",
    degeneracy = 2,
    kinetics = Arrhenius(A=(7.4e+06, 'cm^3/(mol*s)'), n=2.297, Ea=(9011, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(300, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Sendt2008]""",
    longDesc =
u"""
Part of the "HxSy" subset
k_abstraction, (R4a)
T range: 300-3000 K
calculations done at the MRCI/aug-cc-pV(Q+d)Z//MRCI/aug-cc-pVTZ level of theory
Added as a training reaction to H_Abstraction

* Note that this special reaction has two paths: a direct H-abstraction path (reported here),
as well as a P-Dep rate described by [Marshall2011b], with zero high-P rate.
The PDep path is found in the Sulfur/HSSH_1bar reported for 1 bar.
These paths are also described by the [Sulfur/GlarborgH2S] library, but they use a fitted high-P rate for the PDep path,
which theoretically should be zero, but isn't in that library.

(note that this source has a CORRECTION, doi: 10.1021/jp810800a, and the original rate should be multiplied by a factor
of x2: i.e., A = 7.4e+06 cm^3/(mol*s), NOT 3.7e+06 cm^3/(mol*s))
""",
)

entry(
    index = 40,
    label = "S + H2 <=> SH + H",
    degeneracy = 2,
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
    index = 41,
    label = "S + CH4 <=> SH + CH3",
    degeneracy = 4,
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
    index = 42,
    label = "S + C2H6 <=> SH + C2H5",
    degeneracy = 6,
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
    index = 43,
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
    index = 44,
    label = "S2 + H <=> HSS",
    degeneracy = 2,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.15e+25, 'cm^6/(mol^2*s)'), n=-2.840, Ea=(1665, 'cal/mol'), T0 = (1, 'K'),
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
    index = 47,
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

# entry(
#     index = 48,
#     label = "HSS + H <=> S2 + H2",
#     degeneracy = 1,
#     kinetics = Arrhenius(A=(1.23e+08, 'cm^3/(mol*s)'), n=1.653, Ea=(-1105, 'cal/mol'), T0 = (1, 'K'),
#                          Tmin=(873, 'K'), Tmax=(1423, 'K')),
#     shortDesc = u"""[Sendt2002]""",
#     longDesc =
# u"""
# commented out: This reaction has two pathways. The current entry only describes one.
# The other one is PDep and is given at 1 bar in the Sulfur/HSSH_1bar library
#
# Part of the "SOx" subset
# k11
#
# Also available from [Sendt2009b]
# """,
# )

# entry(
#     index = 49,
#     label = "HSS + H <=> H2S + S",
#     degeneracy = 1,
#     kinetics = Arrhenius(A=(4.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(6326, 'cal/mol'), T0 = (1, 'K'),
#                          Tmin=(873, 'K'), Tmax=(1423, 'K')),
#     shortDesc = u"""[Sendt2002]""",
#     longDesc =
# u"""
# commented out: This reaction has two pathways. The current entry only describes one.
# The other one is PDep and is given at 1 bar in the Sulfur/HSSH_1bar library
#
# Part of the "HxSy" subset
# k12
# TST
# Validated in T range: 873-1423 K
#
# Also available from [Sendt2009b]
# """,
# )

entry(
    index = 50,
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
    index = 51,
    label = "HSS + HSS <=> HSSH + S2",
    degeneracy = 2,
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
    index = 52,
    label = "HSSH + H <=> HSS + H2",
    degeneracy = 2,
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
    index = 53,
    label = "HSSH + H <=> H2S + SH",
    degeneracy = 2,
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
    index = 54,
    label = "HSSH + SH <=> H2S + HSS",
    degeneracy = 2,
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
    index = 55,
    label = "HSSH + S <=> HSS + SH",
    degeneracy = 2,
    kinetics = Arrhenius(A=(2.85e+06, 'cm^3/(mol*s)'), n=2.310, Ea=(1204, 'cal/mol'), T0 = (1, 'K'),
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
    index = 56,
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
    index = 57,
    label = "CH3SH + H <=> CH2SH + H2",
    degeneracy = 3,
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
    index = 58,
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
    index = 59,
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
    index = 60,
    label = "S + C2H2 <=> HCCS + H",
    degeneracy = 2,
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
    index = 61,
    label = "S + CS2 <=> CS + S2",
    degeneracy = 2,
    kinetics = Arrhenius(A=(6.87e+13, 'cm^3/(mol*s)'), n=0.00, Ea=(8843, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(690, 'K'), Tmax=(1040, 'K')),
    shortDesc = u"""[Marshall2011a]""",
    longDesc =
u"""
Part of the "C-S" mechanism
T range: 690-1040 K
""",
)

entry(
    index = 62,
    label = "HOSO2 + O2 <=> SO3 + HO2",
    degeneracy = 2,
    duplicate=True,
    kinetics = Arrhenius(A=(1.848e-06, 'cm^3/(mol*s)','*|/',5.17556), n=5.40, Ea=(94.02, 'kJ/mol'), T0=(1, 'K'),
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
    index = 63,
    label = "HOSO2 + O2 <=> SO3 + HO2",
    degeneracy = 2,
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

The energetics of this reaction are available at doi: 10.1063/1.480605 (were not used in the above calculation)
""",
)

entry(
    index = 64,
    label = "H2S + OH <=> H2O + SH",
    degeneracy = 2,
    kinetics = Arrhenius(A=(3.82e+06, 'cm^3/(mol*s)','*|/',1.5773), n=2.04583, Ea=(-1039, 'cal/mol','+|-',65), T0=(1, 'K'),
                         Tmin=(200, 'K'), Tmax=(2400, 'K')),
    shortDesc = u"""[Truhlar2007]""",
    longDesc =
u"""
Calculated at several levels, the MO6-2X was taken here as recommended in [Truhlar2007]
Rates taken from Table 6 and a modified Arrhenius form was fitted using RMG's functions
    Arrhenius(A=(6.33693e-18,'cm^3/(molecule*s)'), n=2.04583, Ea=(-4.34658,'kJ/mol'), T0=(1,'K'),
    Tmin=(200,'K'), Tmax=(2400,'K'),
    comment="Fitted to 9 data points; dA = *|/ 1.57733, dn = +|- 0.0603264, dEa = +|- 0.272582 kJ/mol")
Uncertainties represent averaging error
This reaction is reported to have an unusual temperature dependence, see [Truhlar2007]
""",
)

entry(
    index = 46,
    label = "HSSH <=> SH + SH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.59e+18, 's^-1'), n=-0.957, Ea=(267, 'kJ/mol'), T0 = (1, 'K'),
                         Tmin=(300, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"""[Sendt2009b]""",
    longDesc =
u"""
Table 1, R2
calculations done at the MRCI/aug-cc-pV(Q+d)Z//CASSCF/cc-pVTZ level of theory

Also available from [Sendt2002]:
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(2.31e+14, 'cm^3/(mol*s)'), n=1, Ea=(57030, 'cal/mol'), T0 = (1, 'K'),
                                 Tmin=(873, 'K'), Tmax=(1423, 'K')),
        efficiencies={'N#N': 1, 'S': 1.1, '[Ar]': 0.88, '[He]': 1.39}),
    k9
    UNIMOL calculation
    Validated in T range: 873-1423 K

Also available from [Sendt2009b] in reverse:
     label = "SH + SH <=> HSSH",
     degeneracy = 1,
     kinetics = Troe(
         arrheniusHigh = Arrhenius(A=(3.37e+12, 'cm^3/(mol*s)'), n=0.158, Ea=(-6.01, 'kJ/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2000, 'K')),
         arrheniusLow = Arrhenius(A=(2.33e+31, 'cm^6/(mol^2*s)'), n=-4.943, Ea=(8, 'kJ/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2000, 'K')),
         alpha=1, T3=(254, 'K'), T1=(2373, 'K'), efficiencies={}),
    Table 1, R2 & Table 2 R1a
    high P rate was fitted in reverse using the supplied Keq with average errors:
    dA = *|/ 1.01857, dn = +|- 0.00238486, dEa = +|- 0.013582 kJ/mol
    calculations done at the MRCI/aug-cc-pV(Q+d)Z//CASSCF/cc-pVTZ level of theory
""",
)

entry(
    index = 65,
    label = "HSSH <=> HSS + H",
    degeneracy = 2,
    kinetics = Arrhenius(A=(4.70e+17, 's^-1'), n=-0.076, Ea=(310, 'kJ/mol'), T0=(1, 'K'),
                         Tmin=(300, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"""[Sendt2009b]""",
    longDesc =
u"""
Table 1, R3
calculations done at the MRCI/aug-cc-pV(Q+d)Z//CASSCF/cc-pVTZ level of theory
""",
)

entry(
    index = 66,
    label = "HSSH <=> H2SS",
    degeneracy = 2,
    kinetics = Arrhenius(A=(6.74e+12, 's^-1'), n=0.213, Ea=(193, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"""[Sendt2009b]""",
    longDesc =
u"""
Table 1, R4
calculations done at the MRCI/aug-cc-pV(Q+d)Z//CASSCF/cc-pVTZ level of theory
""",
)

entry(
    index = 67,
    label = "H2SS <=> HSS + H",
    degeneracy = 2,
    kinetics = Arrhenius(A=(1.46e+15, 's^-1'), n=-0.026, Ea=(191, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"""[Sendt2009b]""",
    longDesc =
u"""
Table 1, R5
calculations done at the MRCI/aug-cc-pV(Q+d)Z//CASSCF/cc-pVTZ level of theory
""",
)

entry(
    index = 68,
    label = "H2SS <=> H2S + S",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.53e+11, 's^-1'), n=0.468, Ea=(127, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"""[Sendt2009b]""",
    longDesc =
u"""
Table 1, R6
calculations done at the MRCI/aug-cc-pV(Q+d)Z//CASSCF/cc-pVTZ level of theory
""",
)

entry(
    index = 69,
    label = "H2SS <=> S2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.36e+10, 's^-1'), n=1.125, Ea=(158, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"""[Sendt2009b]""",
    longDesc =
u"""
Table 1, R7
calculations done at the MRCI/aug-cc-pV(Q+d)Z//CASSCF/cc-pVTZ level of theory
""",
)

entry(
    index = 70,
    label = "H2S + S <=> HSSH",
    degeneracy = 2,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(6.38e+07, 'cm^3/(mol*s)'), n=1.280, Ea=(-2, 'kJ/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(2.40e+21, 'cm^6/(mol^2*s)'), n=-1.612, Ea=(7, 'kJ/mol'), T0=(1, 'K')),
        alpha = 0.5, T3=(726, 'K'), T1=(726, 'K'), efficiencies={}),
    shortDesc = u"""[Marshall2011b]""",
    longDesc =
u"""
Table 1
calculations done at the MRCI/aug-cc-pV(Q+d)Z//CASSCF/cc-pVTZ level of theory
""",
)

entry(
    index = 71,
    label = "HSO <=> H + SO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.68e+14, 's^-1'), n=0.0, Ea=(244, 'kJ/mol'), T0=(1, 'K'),
                         Tmin=(300, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"""[Sendt2007]""",
    longDesc =
u"""
Table 2
calculated at MRCI/aug-cc-pV5Z
""",
)

entry(
    index = 72,
    label = "HOS <=> H + SO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.27e+10, 's^-1'), n=1.051, Ea=(231, 'kJ/mol'), T0=(1, 'K'),
                         Tmin=(300, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"""[Sendt2007]""",
    longDesc =
u"""
Table 2
calculated at MRCI/aug-cc-pV5Z
""",
)

entry(
    index = 73,
    label = "HSO <=> HOS",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.08e+11, 's^-1'), n=0.547, Ea=(192, 'kJ/mol'), T0=(1, 'K'),
                         Tmin=(300, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"""[Sendt2007]""",
    longDesc =
u"""
Table 2
calculated at MRCI/aug-cc-pV5Z
""",
)

entry(
    index = 74,
    label = "HSO <=> SH + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.89e+14, 's^-1'), n=0.286, Ea=(410, 'kJ/mol'), T0=(1, 'K'),
                         Tmin=(300, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"""[Sendt2007]""",
    longDesc =
u"""
Table 2
calculated at MRCI/aug-cc-pV5Z
""",
)

entry(
    index = 75,
    label = "HOS <=> OH + S",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.07e+15, 's^-1'), n=-0.013, Ea=(315, 'kJ/mol'), T0=(1, 'K'),
                         Tmin=(300, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"""[Sendt2007]""",
    longDesc =
u"""
Table 2
calculated at MRCI/aug-cc-pV5Z
""",
)

entry(
    index = 76,
    label = "SH + O <=> OH + S",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.32e+06, 'cm^3/(mol*s)'), n=2.103, Ea=(15, 'kJ/mol'), T0=(1, 'K'),
                         Tmin=(300, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"""[Sendt2007]""",
    longDesc =
u"""
Table 2
calculated at MRCI/aug-cc-pV5Z
""",
)
