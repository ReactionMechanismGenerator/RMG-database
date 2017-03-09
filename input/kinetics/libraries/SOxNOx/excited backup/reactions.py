#!/usr/bin/env python
# encoding: utf-8

name = "SOx-NOx"
shortDesc = u""
longDesc =u"""
This library includes important SOx and NOx reactions.
Prepared by Alon Grinberg Dana

Notes for users:
- Consider setting an appropriate maximumRadicalElectrons value in your input file to allow N, CH, C radicals.
- For NOx, the Nitrogen_Dean_and_Bozzelli library should be used conjointly with this one.

This library consists of the following subsets:
* Thermal NO (1-3)
* Prompt NO (4-55)
* N2O Pathway (56-63)
* NNH Pathway (64-70)
* N2H4 + N2O4 (71-105)
* N2O5 (106)
* CH3NO2 (107-111)
* Thermal de-NOx (112-128)
* NH2 + NO2 (129-131)
* SOx (132-150)
* C-S (151-152)
* SOx-NOx (153)


Reference legend:
[Baulch1994] Baulch et al., Journal of Physical and Chemical Reference Data, 1994, 23, 847, doi: 10.1063/1.555953
[Baulch2009] D.L. Baulch et al., Journal of Physical and Chemical Reference Data, 2009, 23(6), 847, doi: 10.1063/1.555953
[Bozzelli1996] P. Glarborg, D. Kubel, K. Dam-Johansen, H-M. Chiang, J.W. Bozzelli, Int. J. Chem. Kin., 1996, 28(10), 773-790, doi: 10.1002/(SICI)1097-4601(1996)28:10<773::AID-KIN8>3.0.CO;2-K
[Cohen1991] N. Cohen, K. R. Westberg, Journal of Physical and Chemical Reference Data, 1991, 20, 1211,; doi: 10.1063/1.555901
[Cohen1992] Cohen, N. (1992). Chemical Kinetic Data Sheets for High-Temperature Chemical Reactions, Vol. III., Aerospace Corporation Report ATR-91 (7189)-2.
[DeanBozz] (RMG's Nitrogen_Dean_and_Bozzelli library) Anthony M. Dean, Joseph W. Bozzelli, Combustion Chemistry of Nitrogen, in: Gas-Phase Combustion Chemistry, Editor: W.C. Gardiner, 2000, 125-341, doi: 10.1007/978-1-4612-1310-9_2
[Flower1977] W. L. Flower , R. K. Hanson, c. H. Kruger, Comb. Sci. Tech., 1977, 15(3-4), 115-128, doi: 10.1080/00102207708946777
[Friedrichs2011] J. Dammeier, G. Friedrichs, J. Phys. Chem. A, 2011, 115, 14382-14390, doi: 10.1021/jp208715c
[GlarZha] (RMG's Nitrogen_Glarborg_Zhang_et_al library) Kuiwen Zhang et al. Proceedings of the Combustion Institute, 2013, 34, 617–624, doi: 10.1016/j.proci.2012.06.010
[GlarGim] (RMG's Nitrogen_Glarborg_Gimenez_et_al) Gimenez Lopeza et al., Proceedings of the Combustion Institute, 2009, 32(1), 367–375, doi: 10.1016/j.proci.2008.06.188
[GRI] (RMG's GRI-Mech3.0-N library) GRI-Mech 3.0, http://www.me.berkeley.edu/gri_mech/
[Hanson1990] D.F. Davidson, R.K. Hanson, Int. J. Chem. Kin., 1990, 22(8), 843–861, doi: 10.1002/kin.550220805
[Lin1996a] A.M. Mebel, E.W.G. Diau, M.C. Lin, K.Morokuma, J. Phys. Chem., 1996, 100, 7517-7525, doi: 10.1021/jp953644f
[Lin1996b] A.M. Mebel, M.C. Lin, K. Morokuma, C.F. Melius, Int. J. Chem. Kin., 1996, 28(9), 693-703, doi: 10.1002/(SICI)1097-4601(1996)28:9<693::AID-KIN8>3.0.CO;2-Q
[Lin1998] D. Chakraborty, J. Park, M.C. Lin, Chemical Phisics, 1998, 231(1), 39-49, doi: 10.1016/S0301-0104(98)00033-0
[Lin1999a] J. Park, M.C. Lin, J. Phys Chem. A, 1999, 103, 8906-8907, doi: 10.1021/jp990954f
[Lin1999b] A.M. Mebel, L.V. Moskaleva, M.C. Lin, J. Molec. Struc. (Theochem), 1999, 461-462, 223-238, doi: 10.1016/S0166-1280(98)00423-0
[Lin2000] L.V Moskaleva, M.C. Lin, Proceedings of the Combustion Institute, 2000, 28(2), 2393-2401, doi: 10.1016/S0082-0784(00)80652-9
[Lin2001] W.S. Xia, M.C. Lin, J. Chem. Phys., 2001, 114, 4522-4532, doi: 10.1063/1.1337061
[Lin2005a] R.S. Zhu, M.C. Lin, Int. J. Chem. Kin., 2005, 37(10), 593-598, doi: 10.1002/kin.20066
[Lin2005b] R.S. Zhu, M.C. Lin, Ab initio study on the oxidation of NCN by O and HO radicals: Prediction of the total rate constant and product branching ratios, in: 6th International Conference of Chemical Kinetics, NIST, Gaithersberg, MD, 2005
[Lin2007a] R.S. Zhu, M.C. Lin, J. Phys. Chem. A, 2007, 111, 6766-6771, doi: 10.1021/jp068991b
[Lin2007b] S. Xu, M.C. Lin, J. Phys. Chem. A, 2007, 111, 6730-6740, doi: 10.1021/jp069038+
[Lin2009a] S. Xu, M.C. Lin, Proceedings of the Combustion Institute, 2009, 32, 99-106, doi: 10.1016/j.proci.2008.07.011
[Lin2009b] S-Y. Tzeng, P-H. Chen, N.S. Wang, L.C. Lee, Z.F. Xu, M.C. Lin, J. Phys. Chem. A, 2009, 113, 6314-6325, doi: 10.1021/jp901903n
[Lin2010a] S. Xu, M.C. Lin, J. Phys. Chem. A, 2010, 114, 5195-5204, doi: 10.1021/jp911048p
[Lin2010b] R.S. Zhu, S.C. Xu, M.C. Lin, Chem. Phys. Letters, 2010, 488(4-6), 121-125, doi: 10.1016/j.cplett.2010.02.003
[Lin2010c] S. Xu, M.C. Lin, Int. J. Chem. Kin., 2010, 42(2), 69-78, doi: 10.1002/kin.20463
[Lin2012] R.S. Zhu, K-Y. Lai, M.C. Lin, J. Phys. Chem. A, 2012, 116, 4466-4472, doi: 10.1021/jp302247k
[Lin2013] R.S. Zhu, P. Raghunath, M.C. Lin, J. Phys. Chem. A, 2013, 117, 7308-7313, doi: 10.1021/jp401148q
[Lin2014a] P. Raghunath, Y.H. Lin, M.C. Lin, Computational and Theoretical Chemistry, 2014, 1046, 73-80, doi: 10.1016/j.comptc.2014.07.011
[Lin2014b] P. Raghunath, N.T. Nghia, M.C. Lin, Advances in Quantum Chemistry, 2014, 69, 253-301, doi: 10.1016/B978-0-12-800345-9.00007-6
[Marshall1999] A. Goumri, J-D.R. Rocha, D. Laakso, C.E. Smith, P. Marshall, J. Phys. Chem. A, 1999, 103(51), 11328–11335 doi: 10.1021/jp9924070
[Marshall2005a] J. Naidoo, A. Goumri, P. Marshall, Proceedings of the Combustion Institute, 2005, 30(1), 1219-1225, doi: 10.1016/j.proci.2004.08.214
[Marshall2005b] A. Yilmaz, L. Hindiyarti, A.D. Jensen, P. Glarbotg, P. Marshall, J. Phys. Chem. A, 2006, 110 (21), 6654–6659, doi: 10.1021/jp0557215
[Marshall2007a] L. Hindiyarti, P. Glarborg, P. Marshall, J. Phys. Chem. A, 2007, 111(19), 3984–3991, doi: 10.1021/jp067499p
[Marshall2007b] C.L. Rasmussen, P. Glarborg, P. Marshall, Proceedings of the Combustion Institute, 2007, 31, 339–347, doi: 10.1016/j.proci.2006.07.249
[Marshall2011] Y. Gao, P. Marshall, J. Chem. Phys., 2011, 135, 144306, doi: 10.1063/1.3644773
[Marshall2013] S.J. Klippenstein, L.B. Harding, P. Glarborg, Y. Gao, H. Hu, P. Marshall, J. Phys. Chem. A, 2013, 117, 9011-9022, doi: 10.1021/jp4068069
[Marshall2014] I.M. Alecu, P. Marshall, J. Phys. Chem. A, 2014, 118(48), 11405–11416, doi: 10.1021/jp509301t
[Marshall2015] S. Ayling, Y. Gao, P. Marshall, Proceedings of the Combustion Institute, 2015, 35(1), 215-222, doi: 10.1016/j.proci.2014.05.079
[Pilling2002] M.A. Blitz, K.W. McKee, M.J. Pilling, J. Phys. Chem. A, 2002, 106(36), 8406–8410, doi: 10.1021/jp025508y
[Pilling2003] M.A. Blitz, K.J. Hughes, M.J. Pilling, J. Phys. Chem. A, 2003, 107(12), 1971-1978, doi: 10.1021/jp026524y
[Pilling2006] M.A. Blitz, K.J. Hughes, M.J. Pilling, S.H. Robertson, J. Phys. Chem. A, 2006, 110(9), 2996–3009, doi: 10.1021/jp054722u
[Rabinowitz2010] S.M. Hwang, J.A. Cooke, K.J. De Witt, M.J. Rabinowitz, Int. J. Chem. Kin., 2010, 42(3), 168-180, doi: 10.1002/kin.20472
[Varandas2005] P.J.S.B. Caridade, S.P.J. Rodrigues, F. Sousa, A.J.C. Varandas, J. Phys. Chem. A ,2005, 109, 2356-2363, doi: 10.1021/jp045102g
[Wang1982] O.I. Smith, S. Tseregounis, S-N. Wang, Int. J. Chem. Kin., 1982, 14(6), 679-697, doi: 10.1002/kin.550140610

"""

entry(
    index = 1,
    label = "N + NO <=> O + N2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.29e+13, 'cm^3/(mol*s)'), n=0, Ea=(1564, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Hanson1990]""",
    longDesc =
u"""
Part of the "Thermal (Zeldovich) NO" mechanism
See [Hanson1990] R1; p. 856

[DeanBozz] reccomend using [Hanson1990]'s value, which shock-tube measurements are in close agreement with 5 other studies (see Fig 2.1 in [DeanBozz] p. 142)
[GRI] fitted to the data of 3 of the sources in [DeanBozz]

Also available in RMG's libraries as:
[DeanBozz] *reverse direction given: A = 2e+14 cm^3/(mol*s); n = 0; Ea = 76774 cal/mol (although the paper gave 1.95e14, not 2e14 for A)
[GlarZha]  A = 2.1e13 cm^3/(mol*s); n = 0; Ea = 0
[GlarGim]  A = 3.3e12 cm^3/(mol*s); n = 0.3; Ea = 0 cal/mol
[GRI]      A = 2.7e13 cm^3/(mol*s); n = 0; Ea = 355 cal/mol
""",
)

entry(
    index = 2,
    label = "N + O2 <=> NO + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.0e+09, 'cm^3/(mol*s)'), n=1, Ea=(6500, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Baulch1994]""",
    longDesc =
u"""
Part of the "Thermal (Zeldovich) NO" mechanism
See [Baulch1994] p. 859

[DeanBozz] (p. 230) cite [Cohen1992], which I couldn't access.
[GRI] gives an identical rate based on [Baulch1994].

Also available in RMG's libraries as:
[DeanBozz] A = 9e+09 cm^3/(mol*s); n = 1; Ea = 6494 cal/mol
[GlarZha]  A = 6.4e9 cm^3/(mol*s); n = 1; Ea = 6280 cal/mol
[GlarGim]  A = 6.4e9 cm^3/(mol*s); n = 1; Ea = 6280 cal/mol
[GRI]      A = 9e+09 cm^3/(mol*s); n = 1; Ea = 6500 cal/mol
""",
)

entry(
    index = 3,
    label = "NO + H <=> N + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.22e+14, 'cm^3/(mol*s)'), n=0, Ea=(50500, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Flower1977]""",
    longDesc =
u"""
Part of the "Thermal (Zeldovich) NO" mechanism
(1) in [Flower1977]

[DeanBozz] (p. 231) give A = 6.4e+12 cm^3/(mol*s); n = 0.1; Ea = 21300 cal/mol, citing [Cohen1991]
But [Cohen1991] says that this rate "cannot be fixed more precisely" than an upper boundary of 4.1e+10 (p. 95, k2a)

[GRI] used a fit to low and high T expressions from Atkinson et al., (1989) J. Phys. Chem. Ref. Data 18 88 and Hanson et al., Combustion Chemistry , Springer-Verlag, N.Y., p. 361
[GRI] this optimized this rate and reccomend 59% of the fit's A factor.

[GlarGim] has a ridiculously long citation chain:
Skreiberg et al, Combust. Flame 136, 501-518 (2004) <-- P. Glarborg et al., Combust. Flame 115 (1998) 1–27 <-- P. Glarborg et al., Int. J. Chem. Kinet., 27 (1995), p. 1207 <-- P. Glarborg et al., Int. J. Chem. Kinet., 26, 421 (1994) <-- J.A. Miller, C. T. Bowman, Prog. Energy and Comb. Sci., 15, 287 (1989) <-- J.A. Miller et al., 20th Symp. (Int.) Combust., pp. 673-684, The Combustion Institute, Pittsburgh (1985) <-- W.L. Flower et al., Comb. Sci. Tech. 15, 115 (1977).
The origin of the data is in shock tube experiments by [Flower1977] (p. 14, Fig. 7)

Also available in other RMG libraries as:
[DeanBozz] *reverse direction given: A = 1.1e+14 cm^3/(mol*s); n = 0; Ea = 1122 cal/mol
[GlarZha]  *reverse direction given: A = 3.8e+13 cm^3/(mol*s); n = 0; Ea = 0 cal/mol
[GlarGim]  *reverse direction given: A = 3.8e+13 cm^3/(mol*s); n = 0; Ea = 0 cal/mol
[GRI]      *reverse direction given: A = 3.36e+13 cm^3/(mol*s); n = 0; Ea = 385 cal/mol
""",
)

entry(
    index = 4,
    label = "CH(u1) + N2 <=> NCN(u2) + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.22e+07, 'cm^3/(mol*s)'), n=1.48, Ea=(23367, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2000]""",
    longDesc =
u"""
Part of the "Prompt NO" mechanism. This is the MAIN Prompt NO reaction
k3 in [Lin2000], also first on p. 2397

T range: 1500-4000 K
Done at the G2M(RCC2)//B3LYP/6-311G(d,p) level of theory

This mechanism was first suggested by Fenimore in 1971 (C.P. Fenimore, Symposium (International) on Combustion 13(1) 1971, 373-380)
He found that 'post-flame' NO profiles extrapolated to zero at the burner surface
for H2 and CO flames, but had non-zero intercepts in all the hydrocarbon flames.
He named it `prompt NO`, since it was apparently formed in the primary reaction zones of the hydrocarbon flames.
He suggested that this prompt NO was due to the reaction of molecular nitrogen with a hydrocarbon free radical,
the products of which were rapidly oxidized to NO.
The well-known thermal (Zeldovich) NO mechanism was felt to be too slow to account for the non-zero intercepts.

Fenimore suggested the following reactions:
CH+N2=HCN+N
C2+N2=CN+CN
Although criticized, the idea gained acceptance, and Miller and Bowman (J.A. Miller, C.T. Bowman, Progress in Energy and Combustion Science, 15(4) 1989 287-338)
that the only plausible candidate for the prompt-NO reaction was:
CH+N2=HCN+N
with possibly some contribution from:
C+N2=CN+N
at very high temperatures.
The problem with CH+N2=HCN+N is that it does not conserve electron spin (CH's ground state is a doublet).

The final piece to the puzzle has apparently been put into place by Moskaleva and Lin (L.V Moskaleva, M.C. Lin, Proceedings of the Combustion Institute 28(2) 2000, 2393-2401),
who realized that the only way that everyone could be correct was if there was another reaction path and a different set of products.
The cyanonitrene (NCN) radical was suggested as the product of this reaction.

In the end, it appears that Fenimore's prompt NO is due to a reaction between CH and N2,
as he suggested. However, the reaction does conserve electron spin, producing NCN+H rather than HCN + N.

More info available in Miller & Troe 2005 (J.A. Miller, M.J. Pillingb, J. Troe, Proceedings of the Combustion Institute 30(1) 2005, 43–88).
""",
)

entry(
    index = 5,
    label = "CH(u1) + N2 <=> HNCN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.65e+21, 'cm^3/(mol*s)'), n=-3.62, Ea=(14196, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2000]""",
    longDesc =
u"""
Part of the "Prompt NO" mechanism
See Table 1 on p. 2397 in [Lin2000]
T range: 2000-4000 K
Done at the G2M(RCC2)//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 6,
    label = "CH2(u0) + N2 <=> CH2N2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 10, 100, 300, 760, 7600], 'torr'),
        arrhenius = [
            Arrhenius(A=(1.22e+30, 'cm^3/(mol*s)'), n=-7.25, Ea=(2730, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(9.45e+30, 'cm^3/(mol*s)'), n=-7.22, Ea=(2734, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(4.55e+31, 'cm^3/(mol*s)'), n=-7.13, Ea=(2653, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(1.46e+32, 'cm^3/(mol*s)'), n=-7.13, Ea=(2774, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(7.41e+32, 'cm^3/(mol*s)'), n=-7.21, Ea=(3088, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(1.39e+34, 'cm^3/(mol*s)'), n=-7.28, Ea=(3804, 'cal/mol'), T0 = (1, 'K')),
        ],
    ),
    shortDesc = u"""[Lin2010a]""",
    longDesc =
u"""
Part of the "Prompt NO" mechanism
k1 in [Lin2010a]
T range: 300-3000 K
Done at the CCSD(T)/6-311+G(3df,2p)//B3LYP/6-311+G(3df,2p) level of theory
""",
)

entry(
    index = 7,
    label = "CH2(u0) + N2 <=> CHN2 + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 10, 100, 300, 760, 7600], 'torr'),
        arrhenius = [
            Arrhenius(A=(2.27e+12, 'cm^3/(mol*s)'), n=0, Ea=(59358, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(2.31e+12, 'cm^3/(mol*s)'), n=0, Ea=(60093, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(4.02e+12, 'cm^3/(mol*s)'), n=0, Ea=(61146, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(4.51e+12, 'cm^3/(mol*s)'), n=0, Ea=(61365, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(5.40e+12, 'cm^3/(mol*s)'), n=0, Ea=(61643, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(5.55e+12, 'cm^3/(mol*s)'), n=0, Ea=(61723, 'cal/mol'), T0 = (1, 'K')),
        ],
    ),
    shortDesc = u"""[Lin2010a]""",
    longDesc =
u"""
Part of the "Prompt NO" mechanism
k2 and k4 in [Lin2010a]
T range: 500-3000 K
Done at the CCSD(T)/6-311+G(3df,2p)//B3LYP/6-311+G(3df,2p) level of theory
The singlet CH2 may transform to its ground state triplet CH2 by collisional
quenching during the reaction. The triplet CH2 can also react with N2.
The rates of the two PDepArrhenius reactions were summed-up, and an Arrhenius expression was fitted
with coefficients of determination ranging 0.9967 to 0.9988 (improving as pressure increases).
""",
)

entry(
    index = 8,
    label = "CH2(u0) + N2 <=> cN2CH2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 10, 100, 300, 760, 7600], 'torr'),
        arrhenius = [
            Arrhenius(A=(2.76e+27, 'cm^3/(mol*s)'), n=-6.92, Ea=(2615, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(1.60e+28, 'cm^3/(mol*s)'), n=-6.86, Ea=(2542, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(2.38e+29, 'cm^3/(mol*s)'), n=-6.90, Ea=(2790, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(8.25e+29, 'cm^3/(mol*s)'), n=-6.92, Ea=(2941, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(2.31e+30, 'cm^3/(mol*s)'), n=-6.92, Ea=(3094, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(4.38e+31, 'cm^3/(mol*s)'), n=-6.99, Ea=(3718, 'cal/mol'), T0 = (1, 'K')),
        ],
    ),
    shortDesc = u"""[Lin2010a]""",
    longDesc =
u"""
Part of the "Prompt NO" mechanism
k3 in [Lin2010a]
T range: 300-3000 K
Done at the CCSD(T)/6-311+G(3df,2p)//B3LYP/6-311+G(3df,2p) level of theory
""",
)

entry(
    index = 9,
    label = "CH2(u0) + N2 <=> HCN + NH(u0)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.46e+18, 'cm^3/(mol*s)'), n=-1.52, Ea=(66373, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2010a]""",
    longDesc =
u"""
Part of the "Prompt NO" mechanism
k5 in [Lin2010a]
T range: 300-3000 K
Done at the CCSD(T)/6-311+G(3df,2p)//B3LYP/6-311+G(3df,2p) level of theory
""",
)

entry(
    index = 10,
    label = "CH2(u0) + N2 <=> CNNH + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.68e+09, 'cm^3/(mol*s)'), n=0.92, Ea=(65180, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2010a]""",
    longDesc =
u"""
Part of the "Prompt NO" mechanism
k6 in [Lin2010a]
T range: 300-3000 K
Done at the CCSD(T)/6-311+G(3df,2p)//B3LYP/6-311+G(3df,2p) level of theory
""",
)

entry(
    index = 11,
    label = "C(u4) + N2 <=> CN + N",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.24e+13, 'cm^3/(mol*s)'), n=0, Ea=(44900, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Baulch2009]""",
    longDesc =
u"""
Part of the "Prompt NO" mechanism
[Baulch2009] p. 860
Uncertainty: +/- 20%
T range: 2000-5000 K
""",
)

entry(
    index = 12,
    label = "CCO(u0) + N2 <=> cNCN + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.13e+04, 'cm^3/(mol*s)'), n=0, Ea=(27700, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2010b]""",
    longDesc =
u"""
"Prompt NO" in C2 or higher hydrocarbons
k3 in [Lin2010b] (p. 124)
T range: 800-3000 K
Done at the CCSD(T)/6-311+G(3df)//B3LYP/6-311+G(3df) level of theory
""",
)

entry(
    index = 13,
    label = "CCO(u2) + N2 <=> CNN(u2) + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(36800, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2010b]""",
    longDesc =
u"""
"Prompt NO" in C2 or higher hydrocarbons
k1 in [Lin2010b] (p. 124)
T range: 800-3000 K
Done at the CCSD(T)/6-311+G(3df)//B3LYP/6-311+G(3df) level of theory

The sister reaction "CCO(u2) + N2 <=> CNN(u0) + CO"
has a rate lower or equal to 1.75e+12exp(33.2 kcal/mol/RT)

formation of NCO + CN and 1CNN/3NCN + CO are too small to be important
in the temperature range of 800–3000 K

Predicted values imply that C2O + N2 may not compete with the CH + N2 reaction and
thus the reaction is not expected to be important for the ‘prompt-NO’ formation in combustion.
""",
)

entry(
    index = 14,
    label = "HNCN <=> H + NCN(u2)",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.79e+28, 'cm^3/(mol*s)'), n=-3.44, Ea=(64502, 'cal/mol'), T0 = (1, 'K'))),
    shortDesc = u"""[Lin2000]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
See Table 1 on p. 2397 in [Lin2000]
T range: 2000-4000 K
Done at the G2M(RCC2)//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 15,
    label = "NCN(u2) <=> N + CN",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(3.25e+15, 'cm^3/(mol*s)'), n=0, Ea=(112921, 'cal/mol'), T0 = (1, 'K'))),
    shortDesc = u"""[Lin2000]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
See Table 1 on p. 2397 in [Lin2000]
T range: 2000-4000 K
Done at the G2M(RCC2)//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 16,
    label = "H + NCN(u2) <=> HCN + N",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.89e+14, 'cm^3/(mol*s)'), n=0, Ea=(8425, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2000]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
See Table 1 on p. 2397 in [Lin2000]
T range: 2000-4000 K
Done at the G2M(RCC2)//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 17,
    label = "CH2(u0) + NCN(u2) <=> CH2CN + N",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.566e+13, 'cm^3/(mol*s)'), n=0, Ea=(-5184, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2000]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
See Table 1 on p. 2397 in [Lin2000]
T range: 2000-4000 K
Done at the G2M(RCC2)//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 18,
    label = "CH2(u0) + NCN(u2) <=> CH2NC + N",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.605e+13, 'cm^3/(mol*s)'), n=0, Ea=(4012, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2000]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
See Table 1 on p. 2397 in [Lin2000]
T range: 2000-4000 K
Done at the G2M(RCC2)//B3LYP/6-311G(d,p) level of theory

Isocyanomethyl radical, CH2CN, propably should have a lone pair and not be a quartet,
but in the dictionary I defined it as a quarted since RMG currently don't have rate rules for carbon with lone pairs.
""",
)

entry(
    index = 19,
    label = "CH2(u0) + NCN(u2) <=> CH2NCN(u2)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.350e+08, 'cm^3/(mol*s)'), n=0, Ea=(-25608, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2000]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
See Table 1 on p. 2397 in [Lin2000]
T range: 2000-4000 K
Done at the G2M(RCC2)//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 20,
    label = "CH2(u0) + NCN(u2) <=> CH2NCN(u0)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.259e+08, 'cm^3/(mol*s)'), n=0, Ea=(-19811, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2000]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
See Table 1 on p. 2397 in [Lin2000]
T range: 2000-4000 K
Done at the G2M(RCC2)//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 21,
    label = "CH2(u0) + NCN(u2) <=> CH2N + CN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.992e+13, 'cm^3/(mol*s)'), n=0, Ea=(4630, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2000]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
See Table 1 on p. 2397 in [Lin2000]
T range: 2000-4000 K
Done at the G2M(RCC2)//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 22,
    label = "CH2(u0) + NCN(u2) <=> HCN + HNC",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.694e+12, 'cm^3/(mol*s)'), n=0, Ea=(4633, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2000]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
See Table 1 on p. 2397 in [Lin2000]
T range: 2000-4000 K
Done at the G2M(RCC2)//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 23,
    label = "CH(u1) + NCN(u2) <=> HCCN + N",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.291e+14, 'cm^3/(mol*s)'), n=0, Ea=(5094, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2000]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
See Table 1 on p. 2397 in [Lin2000]
T range: 2000-4000 K
Done at the G2M(RCC2)//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 24,
    label = "CH(u1) + NCN(u2) <=> HCN + CN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.214e+13, 'cm^3/(mol*s)'), n=0, Ea=(-860, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2000]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
See Table 1 on p. 2397 in [Lin2000]
T range: 2000-4000 K
Done at the G2M(RCC2)//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 25,
    label = "CN + CN <=> NCCN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.251e+14, 'cm^3/(mol*s)'), n=0, Ea=(8020, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2000]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
See Table 1 on p. 2397 in [Lin2000]
T range: 2000-4000 K
Done at the G2M(RCC2)//B3LYP/6-311G(d,p) level of theory
In the original paper this reaction appears as "CN + NCN = (CN)2", which is not stoichiometric.
It is assumed that the explicit dimer product is correct, and that the reactants are two CN rads.
""",
)

entry(
    index = 26,
    label = "CN + NCN(u2) <=> NCNCN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.251e+14, 'cm^3/(mol*s)'), n=0, Ea=(8020, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2000]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
See Table 1 on p. 2397 in [Lin2000]
T range: 2000-4000 K
Done at the G2M(RCC2)//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 27,
    label = "CH3 + NCN(u2) <=> CH3CN + N",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.062e+10, 'cm^3/(mol*s)'), n=0, Ea=(13332, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2000]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
See Table 1 on p. 2397 in [Lin2000]
T range: 2000-4000 K
Done at the G2M(RCC2)//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 28,
    label = "CH3 + NCN(u2) <=> CH2NH + CN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.378e+7, 'cm^3/(mol*s)'), n=0, Ea=(-49933, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2000]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
See Table 1 on p. 2397 in [Lin2000]
T range: 2000-4000 K
Done at the G2M(RCC2)//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 29,
    label = "N + NCN(u2) <=> N2 + CN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2000]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
See Table 1 on p. 2397 in [Lin2000]
T range: 2000-4000 K
Done at the G2M(RCC2)//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 30,
    label = "C + NCN(u2) <=> CN + CN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2000]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
See Table 1 on p. 2397 in [Lin2000]
T range: 2000-4000 K
Taken from: Y. He, C.H. Wu, M.C. Lin, C.F. Melius, Proc. Nineteenth Int. Symp. Shock Waves, 1995, pp. 89–94, as reported by [Lin2000]
""",
)

entry(
    index = 31,
    label = "NCN(u2) + O2 <=> NCO + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.80e+09, 'cm^3/(mol*s)'), n=0.51, Ea=(24596, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2005a]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k1 in [Lin2005a]
This path (producing NCO+NO) is faster than the competing path (producing CNO+NO) described below
T range: 1000-3000 K
The stationary points of species on the low-energy paths were also examined with the third-order Rayleigh–
Schrodinger perturbation (CASPT3) and the multireference configuration interaction including
Davidson’s correction for higher excitations (MRCI + Q) theories at the CASPT3 (4, 4)/aug-cc-
PVTZ//CASSCF(4,4)/cc-pVDZ(4,4) and MRCI+Q(4,4)/aug-cc-PVTZ //CASSCF (4, 4)/cc-pVDZ(4, 4)
levels. The rate constants have been calculated based on the energies obtained at the G2M(CC1) level.
""",
)

entry(
    index = 32,
    label = "NCN(u2) + O2 <=> CNO + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.08e+08, 'cm^3/(mol*s)'), n=0.54, Ea=(24461, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2005a]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k2 in [Lin2005a]
T range: 1000-3000 K
The stationary points of species on the low-energy paths were also examined with the third-order Rayleigh–
Schrodinger perturbation (CASPT3) and the multireference configuration interaction including
Davidson’s correction for higher excitations (MRCI + Q) theories at the CASPT3 (4, 4)/aug-cc-
PVTZ//CASSCF(4,4)/cc-pVDZ(4,4) and MRCI+Q(4,4)/aug-cc-PVTZ //CASSCF (4, 4)/cc-pVDZ(4, 4)
levels. The rate constants have been calculated based on the energies obtained at the G2M(CC1) level.
""",
)

entry(
    index = 33,
    label = "NCN(u2) + O <=> CO + N2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.43e+02, 'cm^3/(mol*s)'), n=2.32, Ea=(-1135, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2007a]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k1 in [Lin2007a]
T range: 200-3000 K
""",
)

entry(
    index = 34,
    label = "NCN(u2) + O <=> CN + NO",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(4.87e+12, 'cm^3/(mol*s)'), n=0.18, Ea=(-46, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.07e+13, 'cm^3/(mol*s)'), n=0.15, Ea=(-30, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    shortDesc = u"""[Lin2007a]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k2 and k3 in [Lin2007a]
T range: 200-3000 K
Measured rate constant is also available by [Friedrichs2011]
""",
)

entry(
    index = 35,
    label = "NCN(u2) + O <=> N + NCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.21e+09, 'cm^3/(mol*s)'), n=0.42, Ea=(-157, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2007a]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k4 in [Lin2007a]
T range: 200-3000 K
""",
)

entry(
    index = 36,
    label = "NCN(u2) + NO <=> CN + N2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.89e+12, 'cm^3/(mol*s)'), n=0, Ea=(6286, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Friedrichs2011]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k10 in [Friedrichs2011]
rate expression on p. 14386
Experimental T range: 764-1944 K
Uncertainty estimate: +/- 7%; activation energy uncertainty: +/- 380 cal/mol
""",
)

entry(
    index = 37,
    label = "NCN(u2) + NO2 <=> NCNO + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(9082, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Friedrichs2011]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k11 in [Friedrichs2011]
rate expression on p. 14388
Experimental T range: 704-1659 K
Uncertainty estimate: +/- 19%; activation energy uncertainty: +/- 910 cal/mol
""",
)

entry(
    index = 38,
    label = "HNCN + OH <=> OHNHCN",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 10, 100, 300, 760, 7600], 'torr'),
        arrhenius = [
            Arrhenius(A=(2.43e+40, 'cm^3/(mol*s)'), n=-10.14, Ea=(4261, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(3.16e+41, 'cm^3/(mol*s)'), n=-10.17, Ea=(4539, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(5.17e+42, 'cm^3/(mol*s)'), n=-10.22, Ea=(5065, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(1.96e+43, 'cm^3/(mol*s)'), n=-10.24, Ea=(5425, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(5.47e+43, 'cm^3/(mol*s)'), n=-10.24, Ea=(5773, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(4.35e+44, 'cm^3/(mol*s)'), n=-10.19, Ea=(6818, 'cal/mol'), T0 = (1, 'K')),
        ],
    ),
    shortDesc = u"""[Lin2007b]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k1 in [Lin2007b] (see reactions on p. 6735, and rates on p. 6738)
T range: 300-3000 K
Done at the CCSD(T)/6-311+G(3df,2p)//B3LYP/6-311+G(3df,2p) level of theory
""",
)

entry(
    index = 39,
    label = "HNCN + OH <=> H2O + NCN(u0)",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 10, 100, 300, 760, 7600], 'torr'),
        arrhenius = [
            Arrhenius(A=(2.37e+01, 'cm^3/(mol*s)'), n=2.99, Ea=(-346, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(2.92e+01, 'cm^3/(mol*s)'), n=2.97, Ea=(-284, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(2.99e+01, 'cm^3/(mol*s)'), n=2.97, Ea=(-284, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(3.28e+01, 'cm^3/(mol*s)'), n=2.95, Ea=(-264, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(4.16e+01, 'cm^3/(mol*s)'), n=2.92, Ea=(-203, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(2.79e+02, 'cm^3/(mol*s)'), n=2.69, Ea=(-344, 'cal/mol'), T0 = (1, 'K')),
        ],
    ),
    shortDesc = u"""[Lin2007b]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k2 in [Lin2007b] (see reactions on p. 6735, and rates on p. 6738)
T range: 300-3000 K
Done at the CCSD(T)/6-311+G(3df,2p)//B3LYP/6-311+G(3df,2p) level of theory
""",
)

entry(
    index = 40,
    label = "HNCN + OH <=> HCN + HNO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.77e+11, 'cm^3/(mol*s)'), n=0, Ea=(14387, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2007b]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k3 and k6 in [Lin2007b] (see reactions on p. 6735, and rates on p. 6738)
T range: 300-3000 K
Done at the CCSD(T)/6-311+G(3df,2p)//B3LYP/6-311+G(3df,2p) level of theory

Since this reaction proncipally has a degeneracy of 2 (already taken into account in the above rate),
The rates of the two PDepArrhenius reactions were summed-up.
Since k3 is almost independent on pressure, and k6 is more than an order of magnitude lower,
the overall rate had an almost insignificant pressure dependent rate:
    kinetics = PDepArrhenius(
        pressures = ([1, 10, 100, 300, 760, 7600], 'torr'),
        arrhenius = [
            Arrhenius(A=(1.76e+11, 'cm^3/(mol*s)'), n=0, Ea=(14377, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(1.78e+11, 'cm^3/(mol*s)'), n=0, Ea=(14389, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(1.76e+11, 'cm^3/(mol*s)'), n=0, Ea=(14385, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(1.78e+11, 'cm^3/(mol*s)'), n=0, Ea=(14389, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(1.77e+11, 'cm^3/(mol*s)'), n=0, Ea=(14387, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(1.77e+11, 'cm^3/(mol*s)'), n=0, Ea=(14395, 'cal/mol'), T0 = (1, 'K')),
        ],
    ),
(This was calculated by fitting an Arrhenius expression to the sum of the rates with a coefficient of determination = 0.9993)
Hence, the final fitted rate is the average of the above PDepArrhenius rates.
""",
)

entry(
    index = 41,
    label = "HNCN + OH <=> HONCNH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 10, 100, 300, 760, 7600], 'torr'),
        arrhenius = [
            Arrhenius(A=(8.85e+35, 'cm^3/(mol*s)'), n=-9.02, Ea=(1304, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(6.26e+38, 'cm^3/(mol*s)'), n=-9.54, Ea=(2579, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(2.05e+41, 'cm^3/(mol*s)'), n=-9.95, Ea=(3768, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(5.49e+41, 'cm^3/(mol*s)'), n=-9.93, Ea=(3873, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(1.87e+43, 'cm^3/(mol*s)'), n=-10.25, Ea=(4660, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(2.46e+44, 'cm^3/(mol*s)'), n=-10.26, Ea=(5475, 'cal/mol'), T0 = (1, 'K')),
        ],
    ),
    shortDesc = u"""[Lin2007b]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k4 in [Lin2007b] (see reactions on p. 6735, and rates on p. 6738)
T range: 300-3000 K
Done at the CCSD(T)/6-311+G(3df,2p)//B3LYP/6-311+G(3df,2p) level of theory
""",
)

entry(
    index = 42,
    label = "HNCN + OH <=> NH2 + NCO",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 10, 100, 300, 760, 7600], 'torr'),
        arrhenius = [
            Arrhenius(A=(1.92e+11, 'cm^3/(mol*s)'), n=0, Ea=(7591, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(2.06e+11, 'cm^3/(mol*s)'), n=0, Ea=(7681, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(2.49e+11, 'cm^3/(mol*s)'), n=0, Ea=(8239, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(5.89e+11, 'cm^3/(mol*s)'), n=0, Ea=(8833, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(3.41e+11, 'cm^3/(mol*s)'), n=0, Ea=(9187, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(4.89e+11, 'cm^3/(mol*s)'), n=0, Ea=(10761, 'cal/mol'), T0 = (1, 'K')),
        ],
    ),
    shortDesc = u"""[Lin2007b]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k5 and k10 in [Lin2007b] (see reactions on p. 6735, and rates on p. 6738)
T range: 500-3000 K
Done at the CCSD(T)/6-311+G(3df,2p)//B3LYP/6-311+G(3df,2p) level of theory
Since this reaction proncipally has a degeneracy of 2 (already taken into account in the above rate),
The rates of the two PDepArrhenius reactions were summed-up, and an Arrhenius expression was fitted
with coefficients of determination ranging 0.9981 to practically 1 (improving as pressure increases).
It is noted that the deviation was higher at T < 500 K,since at lower temperatures k5 becomes
significant relative to k10; therefore this reaction was fitted at the 500-3000 K range.
""",
)

entry(
    index = 43,
    label = "HNCN + OH <=> H2O + NCN(u2)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.04e+05, 'cm^3/(mol*s)'), n=2.48, Ea=(-1886, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2007b]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k7 in [Lin2007b] (see reactions on p. 6735, and rates on p. 6738)
T range: 300-3000 K
Done at the CCSD(T)/6-311+G(3df,2p)//B3LYP/6-311+G(3df,2p) level of theory
""",
)

entry(
    index = 44,
    label = "HNCN + OH <=> NCOHNH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 10, 100, 300, 760, 7600], 'torr'),
        arrhenius = [
            Arrhenius(A=(1.72e+37, 'cm^3/(mol*s)'), n=-9.55, Ea=(7019, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(1.96e+38, 'cm^3/(mol*s)'), n=-9.54, Ea=(7836, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(8.43e+38, 'cm^3/(mol*s)'), n=-9.39, Ea=(6683, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(8.55e+38, 'cm^3/(mol*s)'), n=-9.23, Ea=(9364, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(5.02e+38, 'cm^3/(mol*s)'), n=-9.03, Ea=(9731, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(8.67e+36, 'cm^3/(mol*s)'), n=-8.19, Ea=(10264, 'cal/mol'), T0 = (1, 'K')),
        ],
    ),
    shortDesc = u"""[Lin2007b]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k8 in [Lin2007b] (see reactions on p. 6735, and rates on p. 6738)
T range: 300-3000 K
Done at the CCSD(T)/6-311+G(3df,2p)//B3LYP/6-311+G(3df,2p) level of theory
""",
)

entry(
    index = 45,
    label = "HNCN + OH <=> NCOH + NH(u2)",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 10, 100, 300, 760, 7600], 'torr'),
        arrhenius = [
            Arrhenius(A=(2.04e+06, 'cm^3/(mol*s)'), n=1.72, Ea=(5892, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(4.53e+06, 'cm^3/(mol*s)'), n=1.62, Ea=(6168, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(3.17e+05, 'cm^3/(mol*s)'), n=1.39, Ea=(6866, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(1.60e+08, 'cm^3/(mol*s)'), n=1.19, Ea=(7472, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(8.97e+08, 'cm^3/(mol*s)'), n=1.00, Ea=(8157, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(6.02e+10, 'cm^3/(mol*s)'), n=0.51, Ea=(10278, 'cal/mol'), T0 = (1, 'K')),
        ],
    ),
    shortDesc = u"""[Lin2007b]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k9 in [Lin2007b] (see reactions on p. 6735, and rates on p. 6738)
T range: 300-3000 K
Done at the CCSD(T)/6-311+G(3df,2p)//B3LYP/6-311+G(3df,2p) level of theory
""",
)

entry(
    index = 46,
    label = "NCN(u2) + OH <=> HCN + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.23e+11, 'cm^3/(mol*s)'), n=0.35, Ea=(4660, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2005b]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
from [Lin2005b] as reported by B.A. Williams et al., Proceedings of the Combustion Institute 2009, 32(1), 343-350, doi: 10.1016/j.proci.2008.06.175
See Table 1 (p. 345) in B.A. Williams et al.
(Note that in Table 1 in B.A. Williams et al. the Ea values are stated to be in kcal/mol, but are actually in cal/mol)
T range: 200-3000 K
""",
)

entry(
    index = 47,
    label = "O + HNCN <=> NO + CNH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.48e+14, 'cm^3/(mol*s)'), n=-0.08, Ea=(22, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2009a]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k1 in [Lin2009a]
T range: 300-3000 K
Done at the CCSD(T)/6-311+G(3df,2p)//CCSD/6-311++G(d,p) level of theory
""",
)

entry(
    index = 48,
    label = "O + HNCN <=> NH(u2) + NCO",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1.14e+14, 'cm^3/(mol*s)'), n=-0.13, Ea=(310, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8.61e+25, 'cm^3/(mol*s)'), n=-5.14, Ea=(10014, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    shortDesc = u"""[Lin2009a]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k2 and k9 in [Lin2009a]
T range: 300-3000 K
Done at the CCSD(T)/6-311+G(3df,2p)//CCSD/6-311++G(d,p) level of theory
""",
)

entry(
    index = 49,
    label = "O + HNCN <=> OH + NCN(u2)",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(4.00e-04, 'cm^3/(mol*s)'), n=4.02, Ea=(2560, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.08e+09, 'cm^3/(mol*s)'), n=0.47, Ea=(-1677, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.55e+28, 'cm^3/(mol*s)'), n=-5.79, Ea=(17237, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.48e+22, 'cm^3/(mol*s)'), n=-3.37, Ea=(5429, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    shortDesc = u"""[Lin2009a]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k3, k5, k7, and k8 in [Lin2009a]
T range: 300-3000 K
Done at the CCSD(T)/6-311+G(3df,2p)//CCSD/6-311++G(d,p) level of theory
""",
)

entry(
    index = 50,
    label = "O + HNCN <=> HN(O)CN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.45e+39, 'cm^3/(mol*s)'), n=-10.47, Ea=(5316, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2009a]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k4 in [Lin2009a]
T range: 300-3000 K
Done at the CCSD(T)/6-311+G(3df,2p)//CCSD/6-311++G(d,p) level of theory
""",
)

entry(
    index = 51,
    label = "O + HNCN <=> CN + HNO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.32e+10, 'cm^3/(mol*s)'), n=0.62, Ea=(189, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2009a]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k6 in [Lin2009a]
T range: 300-3000 K
Done at the CCSD(T)/6-311+G(3df,2p)//CCSD/6-311++G(d,p) level of theory
""",
)

entry(
    index = 52,
    label = "O2 + HNCN <=> OH + NCNO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.31e-22, 'cm^3/(mol*s)'), n=8.55, Ea=(12102, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2009a]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k10 in [Lin2009a]
T range: 300-3000 K
Done at the CCSD(T)/6-311+G(3df,2p)//CCSD/6-311++G(d,p) level of theory
""",
)

entry(
    index = 53,
    label = "O2 + HNCN <=> HO2 + NCN(u2)",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1.04e-10, 'cm^3/(mol*s)'), n=5.92, Ea=(21661, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.61e+08, 'cm^3/(mol*s)'), n=1.25, Ea=(24443, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    shortDesc = u"""[Lin2009a]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k11 and k13 in [Lin2009a]
T range: 300-3000 K
Done at the CCSD(T)/6-311+G(3df,2p)//CCSD/6-311++G(d,p) level of theory
""",
)

entry(
    index = 54,
    label = "O2 + HNCN <=> O + HNC(O)N",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.98e+09, 'cm^3/(mol*s)'), n=0.64, Ea=(38154, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2009a]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k12 in [Lin2009a]
T range: 300-3000 K
Done at the CCSD(T)/6-311+G(3df,2p)//CCSD/6-311++G(d,p) level of theory
""",
)

entry(
    index = 55,
    label = "CN + NCO <=> NCN(u0) + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.46e+14, 'cm^3/(mol*s)'), n=0.30, Ea=(952, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2009b]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
See p. 6324 in [Lin2000]
T range: 1000-3000 K

Because k_triplet is much less than k_singlet by a factor of 20-80,
the contribution of the triplet channel to the NCO(u2) + CN reaction is negligible.

Several levels of theory were used:
G2M//B3LYP/6-311+G(d), QCISD(T)/6-311+G(3df)//QCISD/6-311+G(d), CCSD(T)/6-311+G(3df)//CCSD/6-311+G(d),
CASPT2(10,10)/6-311+G(d)//CAS(10,10)/6-311+G(d).
""",
)

entry(
    index = 56,
    label = "N2O <=> N2 + O",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(4.0e+14, 'cm^3/(mol*s)'), n=0, Ea=(56099, 'cal/mol'), T0 = (1, 'K'))),
    shortDesc = u"""[DeanBozz]""",
    longDesc =
u"""
Part of the "N2O Pathway"
Rate taken from:
Johnsson, J.E., Glarborg, P., & Dam-Johansen, K. (1992). 24th Symposium (International) on Combustion, p. 917
As reported by Dean & Bozzeli, see 2.5.3 on p. 143
Measured in a flow reactor with Ar as bath gas.
T range: 1000-3000 K
""",
)

entry(
    index = 57,
    label = "O + N2O <=> N2 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10810, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[DeanBozz]""",
    longDesc =
u"""
Part of the "N2O Pathway"
Rate taken from:
Davidson, D.E, DiRosa, M.D., Chang, A.Y., & Hanson, R.K. (1991). 18th International Symposium on Shock Waves, Sendai, p. 813
As reported by Dean & Bozzeli, see 2.5.4 omn p. 145
""",
)

entry(
    index = 58,
    label = "O + N2O <=> NO + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+13, 'cm^3/(mol*s)'), n=0, Ea=(23151, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[DeanBozz]""",
    longDesc =
u"""
Part of the "N2O Pathway"
Rate taken from:
Davidson, D.E, DiRosa, M.D., Chang, A.Y., & Hanson, R.K. (1991). 18th International Symposium on Shock Waves, Sendai, p. 813
As reported by Dean & Bozzeli, see 2.5.4 omn p. 145
""",
)

entry(
    index = 59,
    label = "H + N2O <=> HNNO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(9082, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[DeanBozz]""",
    longDesc =
u"""
Part of the "N2O Pathway"
See [DeanBozz] 2.6.3, p. 158, and Table 2.6 on p. 163
""",
)

entry(
    index = 60,
    label = "H + N2O <=> NNOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+14, 'cm^3/(mol*s)'), n=0, Ea=(18403, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[DeanBozz]""",
    longDesc =
u"""
Part of the "N2O Pathway"
See [DeanBozz] 2.6.3, p. 158, and Table 2.6 on p. 163
""",
)

entry(
    index = 61,
    label = "HNNO <=> NH(u2) + NO",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(4.0e+15, 'cm^3/(mol*s)'), n=0, Ea=(49952, 'cal/mol'), T0 = (1, 'K'))),
    shortDesc = u"""[DeanBozz]""",
    longDesc =
u"""
Part of the "N2O Pathway"
See [DeanBozz] 2.6.3, p. 158, and Table 2.6 on p. 163
""",
)

entry(
    index = 62,
    label = "HNNO <=> O + NNH",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(4.9e+15, 'cm^3/(mol*s)'), n=0, Ea=(61663, 'cal/mol'), T0 = (1, 'K'))),
    shortDesc = u"""[DeanBozz]""",
    longDesc =
u"""
Part of the "N2O Pathway"
See [DeanBozz] 2.6.3, p. 158, and Table 2.6 on p. 163
""",
)

entry(
    index = 63,
    label = "HNNO <=> N2 + OH",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(6.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(29398, 'cal/mol'), T0 = (1, 'K'))),
    shortDesc = u"""[DeanBozz]""",
    longDesc =
u"""
Part of the "N2O Pathway"
See [DeanBozz] 2.6.3, p. 158, and Table 2.6 on p. 163
""",
)

entry(
    index = 64,
    label = "N2 + H <=> NNH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.6e+15, 'cm^3/(mol*s)'), n=-0.64, Ea=(15333, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Varandas2005]""",
    longDesc =
u"""
Part of the "NNH Pathway"
reaction -3 in [Varandas2005]
Fits to a total of 972 MRCI energies (based on the aug-cc-pVQZ basis set of Dunning27), scaled by the DMBE-SEC
method to account for excitations higher than singles and doubles and the incompleteness of the one-electron basis set.
The paper reports a HO-RR rate, and a sum-over-states rate (where vib-rot aren't assumed to be independent).
The sum-over-states rate was taken here.
""",
)

entry(
    index = 65,
    label = "N + NH(u2) <=> N2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.41e+11, 'cm^3/(mol*s)'), n=0.51, Ea=(18, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Varandas2005]""",
    longDesc =
u"""
Part of the "NNH Pathway"
reaction 1 in [Varandas2005]
Fits to a total of 972 MRCI energies (based on the aug-cc-pVQZ basis set of Dunning27), scaled by the DMBE-SEC
method to account for excitations higher than singles and doubles and the incompleteness of the one-electron basis set.
""",
)

entry(
    index = 66,
    label = "N + H2 <=> NH(u2) + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.60e+14, 'cm^3/(mol*s)'), n=0, Ea=(25138, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Hanson1990]""",
    longDesc =
u"""
Part of the "NNH Pathway"
See [Hanson1990] R2; p. 860
""",
)

entry(
    index = 67,
    label = "NNH + O2 <=> HO2 + N2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+12, 'cm^3/(mol*s)'), n=-0.34, Ea=(149, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[DeanBozz]""",
    longDesc =
u"""
Part of the "NNH Pathway"
reaction 28b1, p. 236
calculated using the QRRK approach
""",
)

entry(
    index = 68,
    label = "NNH + O2 <=> N2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+11, 'cm^3/(mol*s)'), n=-0.34, Ea=(149, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[DeanBozz]""",
    longDesc =
u"""
Part of the "NNH Pathway"
reaction 28b2, p. 236
calculated using the QRRK approach
""",
)

entry(
    index = 69,
    label = "NNH + H <=> H2 + N2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(-894, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[DeanBozz]""",
    longDesc =
u"""
Part of the "NNH Pathway"
reaction 28c, p. 237
DHT estimate
""",
)

entry(
    index = 70,
    label = "NNH + OH <=> H2 + N2",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(2.4e+22, 'cm^3/(mol*s)'), n=-2.88, Ea=(2444, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.25e+06, 'cm^3/(mol*s)'), n=2.00, Ea=(-1192, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    shortDesc = u"""[DeanBozz]""",
    longDesc =
u"""
Part of the "NNH Pathway"
reaction 28d1 and 28d2, p. 237-238
calculated using  QRRK / DHT
""",
)

entry(
    index = 71,
    label = "N2H4 + NO <=> N2H3 + HNO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.44e+01, 'cm^3/(mol*s)'), n=3.16, Ea=(30488, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2014a]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
reaction (1), p. 78
T range: 300-2000 K
calculations done at the CCSD(T)/CBS//CCSD level of theoty,
and the moment of inertia and harmonic vibrational frequencies were obtained by the CCSD/6-31G(d,p) level
""",
)

entry(
    index = 72,
    label = "N2H4 + NO <=> NH2 + H2NNO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.03e+01, 'cm^3/(mol*s)'), n=2.98, Ea=(35609, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2014a]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
reaction (2), p. 78
T range: 300-2000 K
calculations done at the CCSD(T)/CBS//CCSD level of theoty,
and the moment of inertia and harmonic vibrational frequencies were obtained by the CCSD/6-31G(d,p) level
""",
)

entry(
    index = 73,
    label = "N2H4 + NO2 <=> N2H3 + HNO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e-02, 'cm^3/(mol*s)'), n=4.14, Ea=(7947, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2014a]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
reaction (4), p. 78
T range: 300-2000 K
calculations done at the CCSD(T)/CBS//CCSD level of theoty,
and the moment of inertia and harmonic vibrational frequencies were obtained by the CCSD/6-31G(d,p) level
""",
)

entry(
    index = 74,
    label = "N2H4 + NO3 <=> N2H3 + HNO3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.20e+03, 'cm^3/(mol*s)'), n=2.64, Ea=(594, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2014a]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
reaction (6), p. 79
T range: 300-2000 K
calculations done at the CCSD(T)/CBS//CCSD level of theoty,
and the moment of inertia and harmonic vibrational frequencies were obtained by the CCSD/6-31G(d,p) level
""",
)

entry(
    index = 75,
    label = "N2H4 + NO3 <=> HONO + N2H3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.04e+03, 'cm^3/(mol*s)'), n=2.59, Ea=(5612, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2014a]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
reaction (7), p. 79
T range: 1000-2000 K
calculations done at the CCSD(T)/CBS//CCSD level of theoty,
and the moment of inertia and harmonic vibrational frequencies were obtained by the CCSD/6-31G(d,p) level

The Low T (300-1000 K) rate is:
    kinetics = Arrhenius(A=(1.63e+11, 'cm^3/(mol*s)'), n=0.20, Ea=(2180, 'cal/mol'), T0=(1, 'K')),
""",
)

entry(
    index = 76,
    label = "N2H3 + HNO <=> N2H3NO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.65e-02, 'cm^3/(mol*s)'), n=3.82, Ea=(17780, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2014a]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
reaction (9), p. 79
T range: 300-2000 K
calculations done at the CCSD(T)/CBS//CCSD level of theoty,
and the moment of inertia and harmonic vibrational frequencies were obtained by the CCSD/6-31G(d,p) level
""",
)

entry(
    index = 77,
    label = "N2H3 + HNO <=> N2H2 + HONH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.85e-17, 'cm^3/(mol*s)'), n=8.15, Ea=(904, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2014a]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
reaction (10), p. 79
T range: 300-2000 K
calculations done at the CCSD(T)/CBS//CCSD level of theoty,
and the moment of inertia and harmonic vibrational frequencies were obtained by the CCSD/6-31G(d,p) level
""",
)

entry(
    index = 78,
    label = "N2H3 + HONO <=> N2H3NO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.69e+00, 'cm^3/(mol*s)'), n=2.94, Ea=(15379, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2014a]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
reaction (11), p. 79
T range: 300-2000 K
calculations done at the CCSD(T)/CBS//CCSD level of theoty,
and the moment of inertia and harmonic vibrational frequencies were obtained by the CCSD/6-31G(d,p) level
""",
)

entry(
    index = 79,
    label = "N2H3 + HONO <=> N2H2 + H2O + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.79e-08, 'cm^3/(mol*s)'), n=5.51, Ea=(11112, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2014a]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
reaction (12), p. 79
T range: 300-2000 K
calculations done at the CCSD(T)/CBS//CCSD level of theoty,
and the moment of inertia and harmonic vibrational frequencies were obtained by the CCSD/6-31G(d,p) level
""",
)

entry(
    index = 80,
    label = "N2H4 <=> NH2 + NH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.57e+21, 's^-1'), n=-1.04, Ea=(66565, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2014b]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
p. 264
T range: 700-2000 K
calculations done at the RCCSD(T)/6-311þG(3df,2p)//B3LYP/6-311G(d,p) level of theoty
Only High Pressure Limit rate was taken low limit and 1 atm rate are also available from the same source
""",
)

entry(
    index = 81,
    label = "N2H4 <=> N2H3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.69e+14, 's^-1'), n=-0.28, Ea=(76678, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2014b]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
p. 264
T range: 700-2000 K
calculations done at the RCCSD(T)/6-311þG(3df,2p)//B3LYP/6-311G(d,p) level of theoty
Only High Pressure Limit rate was taken low limit and 1 atm rate are also available from the same source
""",
)

entry(
    index = 82,
    label = "ONONO2 <=> NO2 + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.69e+23, 's^-1'), n=-2.43, Ea=(8148, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2014b]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
p. 265
T range: 700-2000 K
calculations done at the UCCSD(T)/CBS//UB3LYP/6-311þþG(3df,2p) level of theoty
Only High Pressure Limit rate was taken low limit and 1 atm rate are also available from the same source
""",
)

entry(
    index = 83,
    label = "ONONO2 <=> NO + NO3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+21, 's^-1'), n=-1.76, Ea=(31535, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2014b]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
p. 265
T range: 700-2000 K
calculations done at the UCCSD(T)/CBS//UB3LYP/6-311þþG(3df,2p) level of theoty
Only High Pressure Limit rate was taken low limit and 1 atm rate are also available from the same source
""",
)

entry(
    index = 84,
    label = "N2H4 + NO2 <=> N2H3 + HONO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.23e+00, 'cm^3/(mol*s)'), n=3.56, Ea=(763, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2014b]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
p. 265
T range: 250-2500 K
calculations done at the G2M(CC2)//B3LYP/6-311þþG(3df,2p) level of theoty
Also available from [Lin2014a], calculated at the CCSD(T)/CBS//CCSD level of theoty:
    kinetics = Arrhenius(A=(8.25e+01, 'cm^3/(mol*s)'), n=3.13, Ea=(8863, 'cal/mol'), T0=(1, 'K')),
""",
)

entry(
    index = 85,
    label = "N2H4 + NO3 <=> N2H3 + HNO3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.28e+04, 'cm^3/(mol*s)'), n=2.53, Ea=(-2947, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2014b]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
p. 269
T range: 300-3000 K
calculations done at the CCSD(T)//BHandHLYP/6-311þþG(3df,2p) level of theoty
Pressure independent at least up to 100 atm
""",
)

entry(
    index = 86,
    label = "N2H4 + NO3 <=> HONO + N2H3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.46e+03, 'cm^3/(mol*s)'), n=2.51, Ea=(-7452, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2014b]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
p. 269
T range: 1000-3000 K
calculations done at the CCSD(T)//BHandHLYP/6-311þþG(3df,2p) level of theoty
Pressure independent at least up to 100 atm

The Low T (300-1000 K) rate is:
    kinetics = Arrhenius(A=(1.10e+18, 'cm^3/(mol*s)'), n=-1.84, Ea=(-642, 'cal/mol'), T0=(1, 'K')),
""",
)

entry(
    index = 87,
    label = "N2H4 + N2O4 <=> HONO + NH2NHNO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.39e+02, 'cm^3/(mol*s)'), n=2.62, Ea=(13112, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2014b]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
p. 271
T range: 200-2500 K
calculations done at the G2M(CC3)//B3LYP level of theoty
""",
)

entry(
    index = 88,
    label = "N2H4 + ONONO2 <=> HNO3 + NH2NHNO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.6e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2014b]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
p. 272
T range: 250-2500 K
calculations done at the G2M(CC3)//B3LYP level of theoty
Reaction has a negligible T dependence in the explored range
The reaction with trans-N2O4 was taken here, data available for cis-N2O4 as well
uncertainty: +/- 12%
""",
)

entry(
    index = 89,
    label = "NH2NHNO <=> N2H3 + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.24e+15, 's^-1'), n=-0.15, Ea=(35611, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2014b]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
p. 274
T range: 250-1500 K
calculations done at the CCSD(T)/6-311þG(3df,2p) level of theoty
""",
)

entry(
    index = 90,
    label = "N2H3 + NO2 <=> N2H2 + HONO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.40e+55, 'cm^3/(mol*s)'), n=-16.7, Ea=(-14397, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2014b]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
k5, p. 278
T range: 800-3000 K, P = 1 atm
calculations done at the CCSD(T)/6-311++G(3df,2p)//B3LYP/6-311++G(3df,2p) level of theoty

The Low T (300-800 K) rate is:
    kinetics = Arrhenius(A=(4.99e+46, 'cm^3/(mol*s)'), n=-11.8, Ea=(6055, 'cal/mol'), T0=(1, 'K')),
""",
)

entry(
    index = 91,
    label = "N2H3 + NO2 <=> N2H3O + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.14e+00, 'cm^3/(mol*s)'), n=2.8, Ea=(-8853, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2014b]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
k6, p. 278
T range: 1000-3000 K, P = 1 atm
calculations done at the CCSD(T)/6-311++G(3df,2p)//B3LYP/6-311++G(3df,2p) level of theoty

The Low T (300-1000 K) rate is:
    kinetics = Arrhenius(A=(1.08e+20, 'cm^3/(mol*s)'), n=-2.9, Ea=(792.3, 'cal/mol'), T0=(1, 'K')),
""",
)

entry(
    index = 92,
    label = "N2H3 + NO2 <=> N2H2 + HNO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.12e+07, 'cm^3/(mol*s)'), n=-0.2, Ea=(-2736, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2014b]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
k7 p. 278
T range: 1500-3000 K, P = 1 atm
calculations done at the CCSD(T)/6-311++G(3df,2p)//B3LYP/6-311++G(3df,2p) level of theoty

The Low T (300-1500 K) rate is:
    kinetics = Arrhenius(A=(4.07e+08, 'cm^3/(mol*s)'), n=0.5, Ea=(-2395, 'cal/mol'), T0=(1, 'K')),
""",
)

entry(
    index = 93,
    label = "N2H3 + N2O4 <=> NH2NHNO2 + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.10e+10, 'cm^3/(mol*s)'), n=0.87, Ea=(11772, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2014b]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
p. 281
T range: 300-3000 K
calculations done at the CCSD(T)/6-311þþG(3df,2p)//B3LYP/6-311þþG(3df,2p) level of theoty
""",
)

entry(
    index = 94,
    label = "N2H3 + N2O4 <=> N2H2 + HONO + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.55e+10, 'cm^3/(mol*s)'), n=0.74, Ea=(11707, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2014b]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
p. 281
T range: 300-3000 K
calculations done at the CCSD(T)/6-311þþG(3df,2p)//B3LYP/6-311þþG(3df,2p) level of theoty
""",
)

entry(
    index = 95,
    label = "N2H3 + N2O4 <=> NH2NHONO + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.54e+13, 'cm^3/(mol*s)'), n=0.76, Ea=(15960, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2014b]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
p. 281
T range: 300-3000 K
calculations done at the CCSD(T)/6-311þþG(3df,2p)//B3LYP/6-311þþG(3df,2p) level of theoty
""",
)

entry(
    index = 96,
    label = "N2H3 + N2O4 <=> N2H3O + N2O3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.69e+11, 'cm^3/(mol*s)'), n=0.87, Ea=(8047.4, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2014b]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
p. 281
T range: 300-3000 K
calculations done at the CCSD(T)/6-311þþG(3df,2p)//B3LYP/6-311þþG(3df,2p) level of theoty
""",
)

entry(
    index = 97,
    label = "N2H3O <=> NH3 + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.86e+22, 's^-1'), n=-2.80, Ea=(79296, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2014b]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
p. 284
T range: 300-3000 K, P = 1 atm
calculations done at the CCSD(T)/6-311þG(3df,2p)//CCSD/6-311þþG(d,p) level of theoty
""",
)

entry(
    index = 98,
    label = "N2H3O <=> NH2 + HNO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.12e+33, 's^-1'), n=-6.68, Ea=(35217, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2014b]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
p. 284
T range: 300-3000 K, P = 1 atm
calculations done at the CCSD(T)/6-311þG(3df,2p)//CCSD/6-311þþG(d,p) level of theoty
""",
)

entry(
    index = 99,
    label = "N2H3O <=> NH2NO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.57e+34, 's^-1'), n=-6.63, Ea=(44953, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2014b]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
p. 284
T range: 300-3000 K, P = 1 atm
calculations done at the CCSD(T)/6-311þG(3df,2p)//CCSD/6-311þþG(d,p) level of theoty
""",
)

entry(
    index = 100,
    label = "N2H2 + NO2 <=> HONO + NNH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.25e+00, 'cm^3/(mol*s)'), n=3.80, Ea=(10410, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2014b]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
p. 287
T range: 300-2500 K
calculations done at the CCSD(T)/6-311þþG(3df,2p)//B3LYP/6-311þþG(3df,2p) level of theoty

The trans-N2H2 conformer react faster above 1400 K, hence its rate is taken here.
For low T (below 1400 K) it is reccomended to take the rate of the reacting cis-N2H2 conformer, which is faster:
    kinetics = Arrhenius(A=(2.33e-01, 'cm^3/(mol*s)'), n=3.50, Ea=(-129, 'cal/mol'), T0=(1, 'K')),
""",
)

entry(
    index = 101,
    label = "N2H2 + N2O4 <=> HONO + NO2 + NNH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.79e+00, 'cm^3/(mol*s)'), n=3.10, Ea=(28787, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2014b]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
p. 288
T range: 300-2500 K
calculations done at the B3LYP/6-311þþG(3df,2p) level
""",
)

entry(
    index = 102,
    label = "N2H2 + N2O4 <=> HONO + OHNO + NNH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.38e-02, 'cm^3/(mol*s)'), n=3.90, Ea=(13360, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2014b]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
p. 288
T range: 300-2500 K
calculations done at the B3LYP/6-311þþG(3df,2p) level
""",
)

entry(
    index = 103,
    label = "N2H2 + OH <=> NNH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.74e+03, 'cm^3/(mol*s)'), n=2.80, Ea=(-507, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2014b]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
p. 292
T range: 300-2500 K
calculations done at the CCSD(T)/6-311++G(3df,2p)//B3LYP/6311++G(3df,2p) level of theory

The trans-N2H2 conformer react faster above 750 K, hence its rate is taken here.
For low T (below 750 K) it is reccomended to take the rate of the reacting cis-N2H2 conformer, which is faster:
    kinetics = Arrhenius(A=(7.65e+04, 'cm^3/(mol*s)'), n=2.25, Ea=(-2351, 'cal/mol'), T0=(1, 'K')),
""",
)

entry(
    index = 104,
    label = "N2O4 + H2O <=> HONO + HNO3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.58e-02, 'cm^3/(mol*s)'), n=4.53, Ea=(29830, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2012]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
p. 4469
T range: 200-2500 K
calculations done at the CCSD(T)/6-311++G(3df,2p)//B3LYP/6-311++G(3df,2p) level of theory
""",
)

entry(
    index = 105,
    label = "ONONO2 + H2O <=> HONO + HNO3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.93e+06, 'cm^3/(mol*s)'), n=1.88, Ea=(4064, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2012]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
p. 4469
T range: 200-2500 K
calculations done at the CCSD(T)/6-311++G(3df,2p)//B3LYP/6-311++G(3df,2p) level of theory
Taken as the sum of the trans-HONO and cis-HONO rates (k2+k3)
""",
)

entry(
    index = 106,
    label = "N2O5 + H2O <=> HNO3 + HNO3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.73e+07, 'cm^3/(mol*s)'), n=3.354, Ea=(15700, 'cal/mol'), T0=(298, 'K')),
    shortDesc = u"""[Marshall2014]""",
    longDesc =
u"""
Part of the "N2O5" subset
p. 11413
T range: 180-1800 K
calculations done at the CCSD(T)-F12a/cc-pVTZ-F12//M06-2X/MG3S level of theory
""",
)

entry(
    index = 107,
    label = "CH3NO2 <=> CH3 + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.88e+24, 's^-1'), n=-2.35, Ea=(62398, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2013]""",
    longDesc =
u"""
Part of the "CH3NO2" subset
p. 7311
T range: 500-3000 K
calculations done at the UCCSD(T)/CBS//UB3LYP/6-311+G(3df,2p) level of theory
The high pressure limit rate is giving here. A 1 atm rate is akso available from the same source.
""",
)

entry(
    index = 108,
    label = "CH3NO2 <=> CH3ONO",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(7.05e+54, 'cm^3/(mol*s)'), n=-2.35, Ea=(62398, 'kcal/mol'), T0=(1, 'K'))),
    shortDesc = u"""[Lin2013]""",
    longDesc =
u"""
Part of the "CH3NO2" subset
p. 7311
calculations done at the UCCSD(T)/CBS//UB3LYP/6-311+G(3df,2p) level of theory
""",
)

entry(
    index = 109,
    label = "CH3NO2 <=> CH3O + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.91e+19, 's^-1'), n=-1.84, Ea=(60809, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2013]""",
    longDesc =
u"""
Part of the "CH3NO2" subset
p. 7311
T range: 300-3000 K, valid for 10e-5 to 760 torr
calculations done at the UCCSD(T)/CBS//UB3LYP/6-311+G(3df,2p) level of theory
""",
)

entry(
    index = 110,
    label = "CH3NO2 <=> CH2O + HNO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.15e+17, 's^-1'), n=-0.75, Ea=(60014, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2013]""",
    longDesc =
u"""
Part of the "CH3NO2" subset
p. 7311
T range: 300-3000 K, valid for 10e-5 to 760 torr
calculations done at the UCCSD(T)/CBS//UB3LYP/6-311+G(3df,2p) level of theory
""",
)

entry(
    index = 111,
    label = "CH3ONO <=> CH3O + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.58e+23, 's^-1'), n=-2.18, Ea=(41930, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2013]""",
    longDesc =
u"""
Part of the "CH3NO2" subset
p. 7311
T range: 300-3000 K
calculations done at the UCCSD(T)/CBS//UB3LYP/6-311+G(3df,2p) level of theory
The high pressure limit rate is giving here. A 1 atm rate is akso available from the same source.
""",
)

entry(
    index = 112,
    label = "NH3 + NO <=> NH2 + HNO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.04e+07, 'cm^3/(mol*s)'), n=1.73, Ea=(56544, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin1996a]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
k1 on p. 7519
T range: 300-5000 K
calculations done at the UMP2/6-311G-(d,p)//UMP2/6-311G(d,p) level of theory
""",
)

entry(
    index = 113,
    label = "NH2 + NO <=> NNH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.43e+07, 'cm^3/(mol*s)'), n=1.40, Ea=(-1777, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin1999a]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
k1a
T range: 300-2500 K
""",
)

entry(
    index = 114,
    label = "NH2 + NO <=> N2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.20e+17, 'cm^3/(mol*s)'), n=1.61, Ea=(298, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin1999a]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
k1b
T range: 300-2500 K
""",
)

entry(
    index = 115,
    label = "NH2 + H2 <=> NH3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.23e+05, 'cm^3/(mol*s)'), n=2.23, Ea=(7168, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin1999b]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
k1theo on p. 229
T range: 300-5000 K
calculations done at the G2M//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 116,
    label = "NH2 + CH4 <=> NH3 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.36e+04, 'cm^3/(mol*s)'), n=2.87, Ea=(10691, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin1999b]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
k2 on p. 232
T range: 300-5000 K
calculations done at the G2M//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 117,
    label = "NH2 + NH3 <=> NH3 + NH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.99e+01, 'cm^3/(mol*s)'), n=3.28, Ea=(9197, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin1999b]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
k3 on p. 233
T range: 300-5000 K
calculations done at the G2M//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 118,
    label = "NH2 + H2O <=> NH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.62e+13, 'cm^3/(mol*s)'), n=0, Ea=(16846, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin1999b]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
k4 on p. 233
T range: 300-5000 K
calculations done at the G2M//B3LYP/6-311G(d,p) level of theory
A lower and upper rate limits were given. Here an average rate was taken.
Fitted to a 2 parameter Arrhenius with a coefficient of determination of 0.9943
""",
)

entry(
    index = 119,
    label = "NH3 + NO2 <=> NH2 + HNO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.91e+00, 'cm^3/(mol*s)'), n=3.41, Ea=(29880, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin1996a]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
(2a) on p. 7524
T range: 300-5000 K
calculations done at the UMP2/6-311G-(d,p)//UMP2/6-311G(d,p) level of theory
""",
)

entry(
    index = 120,
    label = "NH3 + NO2 <=> NH2 + HONO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.35e+00, 'cm^3/(mol*s)'), n=3.30, Ea=(22290, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin1996a]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
(2b) on p. 7523
T range: 300-5000 K
calculations done at the UMP2/6-311G-(d,p)//UMP2/6-311G(d,p) level of theory
NH3+NO2 can give (2a) NH2 + HNO2 (see above), (2b) NH2 + cis-HONO, (2c) NH2 + trans-HONO.
The cis-HONO is more stable, and only reaction (2b) is taken here.
""",
)

entry(
    index = 121,
    label = "N2O + NO <=> N2 + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.26e+05, 'cm^3/(mol*s)'), n=2.23, Ea=(46286, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin1996b]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
k1 on p. 695
T range: 300-5000 K
calculations done at the B3LYP/6-311G(d,p)//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 122,
    label = "N2O + OH <=> N2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.29e-02, 'cm^3/(mol*s)'), n=4.72, Ea=(36565, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin1996b]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
k2A on p. 702
T range: 1000-5000 K
calculations done at the B3LYP/6-311G(d,p)//B3LYP/6-311G(d,p) level of theory
For the low T range (300-1000 K) the reccomended rate for both "N2O + OH <=> N2 + HO2" and "N2O + OH <=> HNO + NO" is:
    kinetics = Arrhenius(A=(2.87e+08, 'cm^3/(mol*s)'), n=0, Ea=(20436, 'cal/mol'), T0=(1, 'K')),
""",
)

entry(
    index = 123,
    label = "N2O + OH <=> HNO + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.18e-04, 'cm^3/(mol*s)'), n=4.33, Ea=(25039, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin1996b]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
k2B on p. 702
T range: 1000-5000 K
calculations done at the B3LYP/6-311G(d,p)//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 124,
    label = "NH3 + NO3 <=> HNO3 + NH2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 10, 100, 760, 7600, 76000], 'torr'),
        arrhenius = [
            Arrhenius(A=(2.57e+00, 'cm^3/(mol*s)'), n=3.61, Ea=(964, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(5.67e+00, 'cm^3/(mol*s)'), n=3.53, Ea=(1598, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(4.61e+00, 'cm^3/(mol*s)'), n=3.56, Ea=(1691, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(4.06e+00, 'cm^3/(mol*s)'), n=3.57, Ea=(1689, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(3.85e+00, 'cm^3/(mol*s)'), n=3.58, Ea=(1679, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(3.63e+00, 'cm^3/(mol*s)'), n=3.59, Ea=(1669, 'cal/mol'), T0 = (1, 'K')),
        ],
    ),
    shortDesc = u"""[Lin2010c]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
k-1 p. 76
T range 200-3000 K
calculations done at the CCSD(T)/6-311+G(3df,2p)//B3LYP/6-311+G(3df,2p) level of theory
k-1 was addopted here due to the strange T dependence of k+1
""",
)

entry(
    index = 125,
    label = "HNO3 + NH2 <=> H2NO + HONO",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 10, 100, 760, 7600, 76000], 'torr'),
        arrhenius = [
            Arrhenius(A=(8.91e+04, 'cm^3/(mol*s)'), n=2.00, Ea=(24641, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(1.36e+07, 'cm^3/(mol*s)'), n=1.40, Ea=(26390, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(5.09e+08, 'cm^3/(mol*s)'), n=0.99, Ea=(28353, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(1.73e+08, 'cm^3/(mol*s)'), n=1.17, Ea=(29562, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(7.17e+04, 'cm^3/(mol*s)'), n=2.19, Ea=(29870, 'cal/mol'), T0 = (1, 'K')),
            Arrhenius(A=(3.46e-02, 'cm^3/(mol*s)'), n=4.04, Ea=(28946, 'cal/mol'), T0 = (1, 'K')),
        ],
    ),
    shortDesc = u"""[Lin2010c]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
k3 p. 76
T range 200-3000 K
calculations done at the CCSD(T)/6-311+G(3df,2p)//B3LYP/6-311+G(3df,2p) level of theory
""",
)

entry(
    index = 126,
    label = "HNO3 + OH <=> H2O + NO3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.73e+00, 'cm^3/(mol*s)'), n=3.50, Ea=(-1667, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2001]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
kNO3 on p. 4530
T range: 750-1500 K
calculations done at the B3LYP/6-311G(d,p)//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 127,
    label = "OH + NO2 <=> HNO3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.45e+13, 'cm^3/(mol*s)'), n=0, Ea=(-477, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin1998]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
k_inf_a on p. 44
T range: 300-2000 K
calculations done at the B3LYP/6-311G(d,p)//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 128,
    label = "OH + NO2 <=> HO2 + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.00e+06, 'cm^3/(mol*s)'), n=2.00, Ea=(3000, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin1998]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
Table 3 on p. 46
T range: 300-2000 K
calculations done at the B3LYP/6-311G(d,p)//B3LYP/6-311G(d,p) level of theory
The 3-parameter Arrhenius parametes were fitted from the data in the table using Excel.
Probably not the best fit... but deviated only by ~5% above 1000 K (larger deviation at T < 1000 K)
""",
)

entry(
    index = 129,
    label = "NH2 + NO2 <=> N2O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.60e+18, 'cm^3/(mol*s)'), n=-2.191, Ea=(455, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Marshall2013]""",
    longDesc =
u"""
Part of the "NH2 + NO2" subset
k1a 3 on p. 9019
T range: 300-2000 K
calculations done at the RQCISD(T)/CBS(QZ,5Z)//B3LYP/6-311++G(d,p) level of theory
+UCCSD(T)/cc-pVTZ rovibrational analysis with UCCSD-(T)/CBS(aug-cc-pVQZ′,aug-cc-pV5Z′) energies,
CCSDT(Q)/cc-pVDZ higher order corrections, CCSD(T,full)/CBS-(TZ,QZ) core−valence corrections,
CI/aug-cc-pcVTZ relativistic corrections, HF/cc-pVTZ diagonal Born−Oppenheimer corrections,
and B3LYP/6-311++G(d,p) anharmonic ZPE corrections
""",
)

entry(
    index = 130,
    label = "NH2 + NO2 <=> H2NO + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.09e+11, 'cm^3/(mol*s)'), n=0.0321, Ea=(-1512, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Marshall2013]""",
    longDesc =
u"""
Part of the "NH2 + NO2" subset
k1b 3 on p. 9019
T range: 300-2000 K
calculations done at the RQCISD(T)/CBS(QZ,5Z)//B3LYP/6-311++G(d,p) level of theory
+UCCSD(T)/cc-pVTZ rovibrational analysis with UCCSD-(T)/CBS(aug-cc-pVQZ′,aug-cc-pV5Z′) energies,
CCSDT(Q)/cc-pVDZ higher order corrections, CCSD(T,full)/CBS-(TZ,QZ) core−valence corrections,
CI/aug-cc-pcVTZ relativistic corrections, HF/cc-pVTZ diagonal Born−Oppenheimer corrections,
and B3LYP/6-311++G(d,p) anharmonic ZPE corrections
""",
)

entry(
    index = 131,
    label = "NH2 + NO2 <=> HNNO + OH",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(3.35e+14, 'cm^3/(mol*s)'), n=-0.926, Ea=(5477, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.38e+12, 'cm^3/(mol*s)'), n=-0.107, Ea=(11238, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    shortDesc = u"""[Marshall2013]""",
    longDesc =
u"""
Part of the "NH2 + NO2" subset
k1c + k1d 3 on p. 9019
T range: 300-2000 K
The rate of the reactions leading to the formation of trans-HNNO and cis-HNNO were summed-up
calculations done at the RQCISD(T)/CBS(QZ,5Z)//B3LYP/6-311++G(d,p) level of theory
+UCCSD(T)/cc-pVTZ rovibrational analysis with UCCSD-(T)/CBS(aug-cc-pVQZ′,aug-cc-pV5Z′) energies,
CCSDT(Q)/cc-pVDZ higher order corrections, CCSD(T,full)/CBS-(TZ,QZ) core−valence corrections,
CI/aug-cc-pcVTZ relativistic corrections, HF/cc-pVTZ diagonal Born−Oppenheimer corrections,
and B3LYP/6-311++G(d,p) anharmonic ZPE corrections
""",
)

entry(
    index = 132,
    label = "SO2 + O <=> SO3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.7e+11, 'cm^3/(mol*s)'), n=0, Ea=(1689, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(2.4e+27, 'cm^6/(mol^2*s)'), n=-3.6, Ea=(5186, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.442, T3=(316, 'K'), T1=(7442, 'K'), efficiencies={'O=S=O': 10, 'O': 10, 'O=C=O': 2.5, 'N#N': 0}),
    shortDesc = u"""[Marshall2005a],[Marshall2005b]""",
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
    index = 133,
    label = "SO2 + O + N2 <=> SO3 + N2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.7e+11, 'cm^6/(mol^2*s)'), n=0, Ea=(1689, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(2.9e+27, 'cm^9/(mol^3*s)'), n=-3.58, Ea=(5206, 'cal/mol'), T0=(1, 'K')),
        alpha=0.43, T3=(371, 'K'), T1=(7442, 'K'), efficiencies={}),
    shortDesc = u"""[Marshall2005a],[Marshall2005b]""",
    longDesc =
u"""
Part of the "SOx" mechanism
Complementary to the reaction above for N2 as the main bath gas
""",
)

entry(
    index = 134,
    label = "SO3 + O <=> SO2 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.8e+11, 'cm^3/(mol*s)'), n=0.00, Ea=(6100, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Wang1982],[Marshall2005b]""",
    longDesc =
u"""
Part of the "SOx" mechanism
""",
)

entry(
    index = 135,
    label = "SO2 + OH <=> HOSO2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.23e+12, 'cm^3/(mol*s)'), n=-0.27, Ea=(0, 'cal/mol'), T0=(300, 'K')),
        arrheniusLow = Arrhenius(A=(1.25e+17, 'cm^6/(mol^2*s)'), n=-4.09, Ea=(0, 'cal/mol'), T0=(300, 'K')),
        alpha=1.0, T3=(1e-30, 'K'), T1=(412, 'K'), efficiencies={'O=S=O': 5, 'O': 5, 'O=C=O': 2.5}),
    shortDesc = u"""[Pilling2003]""",
    longDesc =
u"""
Part of the "SOx" mechanism
Collider efficiencies taken from: Gimenez-Lopez, M. Martinez, A. Millera, R. Bilbao, M.U. Alzueta, Comb. Flame 2011, 158(1), 48-56, doi: 10.1016/j.combustflame.2010.07.017
""",
)

entry(
    index = 136,
    label = "HOSO2 + O2 <=> SO3 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.8e+11, 'cm^3/(mol*s)'), n=0.00, Ea=(655, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Marshall2005b],[Marshall2007a]""",
    longDesc =
u"""
Part of the "SOx" mechanism
Data from: R. Atkinson, D.L. Baulch, R.A. Cox, R.F. Hampson, J. Kerr, J. Phys. Chem. Ref. Data 1992, 21, 1125-1568: Evaluated kinetic and photochemical data for atmospheric chemistry
""",
)

entry(
    index = 137,
    label = "SO2 + H <=> HOSO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.37e+08, 'cm^3/(mol*s)'), n=1.63, Ea=(7339, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(1.85e+37, 'cm^6/(mol^2*s)'), n=-6.14, Ea=(11075, 'cal/mol'), T0=(1, 'K')),
        alpha=0.283, T3=(272, 'K'), T1=(3995, 'K'), efficiencies={'O=S=O': 10, 'O': 10, 'O=C=O': 2.5}),
    shortDesc = u"""[Pilling2006]""",
    longDesc =
u"""
Part of the "SOx" mechanism
T range: 300-1700 K
As reported by Gimenez-Lopez, M. Martinez, A. Millera, R. Bilbao, M.U. Alzueta, Comb. Flame 2011, 158(1), 48-56, doi: 10.1016/j.combustflame.2010.07.017
""",
)

entry(
    index = 138,
    label = "SO2 + H <=> HSO2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.31e+08, 'cm^3/(mol*s)'), n=1.59, Ea=(2472, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(1.41e+31, 'cm^6/(mol^2*s)'), n=-5.19, Ea=(4513, 'cal/mol'), T0=(1, 'K')),
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
    index = 139,
    label = "SO2 + H <=> SO + OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(9.19e+25, 'cm^3/(mol*s)'), n=2.77, Ea=(20850, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(1.35e+22, 'cm^6/(mol^2*s)'), n=-2.30, Ea=(30965, 'cal/mol'), T0=(1, 'K')),
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
    index = 140,
    label = "SO3 + H <=> SO2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.4e+09, 'cm^3/(mol*s)'), n=1.22, Ea=(3320, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Marshall2007a]""",
    longDesc =
u"""
Part of the "SOx" mechanism
T range: 700-2000 K
calculations done at the CBS-QB3/CCSD(T)//B3LYP/6-311G(2d,d,p) level of theory
""",
)

entry(
    index = 141,
    label = "SO3 + O <=> SO2 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+04, 'cm^3/(mol*s)'), n=2.57, Ea=(29210, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Marshall2007a]""",
    longDesc =
u"""
Part of the "SOx" mechanism
T > 1000 K
calculations done at the CBS-QB3/CCSD(T)//B3LYP/6-311G(2d,d,p) level of theory
""",
)

entry(
    index = 142,
    label = "SO3 + OH <=> SO2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.8e+04, 'cm^3/(mol*s)'), n=2.46, Ea=(27225, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Marshall2007a]""",
    longDesc =
u"""
Part of the "SOx" mechanism
T range: 800-2000 K
calculations done at the CBS-QB3/CCSD(T)//B3LYP/6-311G(2d,d,p) level of theory
""",
)

entry(
    index = 143,
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
    index = 144,
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
    index = 145,
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
    index = 146,
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
    index = 147,
    label = "HOSO <=> HSO2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.03e+9, 's^-1'), n=1.03, Ea=(49980, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(1.72e+35, 'cm^3/(mol*s)'), n=-5.64, Ea=(55423, 'cal/mol'), T0=(1, 'K')),
        alpha=1, T3=(1e-30, 'K'), T1=(1e+30, 'K'), efficiencies={}),
    shortDesc = u"""[Marshall1999]""",
    longDesc =
u"""
Part of the "SOx" subset
T range: 200-2000 K
Table 7 on p. 11333
calculations done at the QCISD(T)/6-311+G(3df,2p)//MP2=FULL/6-31G(d) level of theory
""",
)

entry(
    index = 148,
    label = "HSOO <=> SH + O2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(4.41e+18, 's^-1'), n=-1.07, Ea=(7750, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(1.56e+23, 'cm^3/(mol*s)'), n=-2.82, Ea=(-7450, 'cal/mol'), T0=(1, 'K')),
        alpha=1, T3=(1e-30, 'K'), T1=(1e+30, 'K'), efficiencies={}),
    shortDesc = u"""[Marshall1999]""",
    longDesc =
u"""
Part of the "SOx" subset
T range: 200-2000 K
Table 7 on p. 11333
calculations done at the QCISD(T)/6-311+G(3df,2p)//MP2=FULL/6-31G(d) level of theory
""",
)

entry(
    index = 149,
    label = "HOSO <=> OH + SO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.65e+16, 's^-1'), n=-0.32, Ea=(67720, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(1.25e+32, 'cm^3/(mol*s)'), n=-4.33, Ea=(69115, 'cal/mol'), T0=(1, 'K')),
        alpha=1, T3=(1e-30, 'K'), T1=(1e+30, 'K'), efficiencies={}),
    shortDesc = u"""[Marshall1999]""",
    longDesc =
u"""
Part of the "SOx" subset
T range: 200-2000 K
Table 7 on p. 11333
calculations done at the QCISD(T)/6-311+G(3df,2p)//MP2=FULL/6-31G(d) level of theory
""",
)

entry(
    index = 150,
    label = "HSOO <=> HSO + O",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.01e+19, 's^-1'), n=-1.07, Ea=(28377, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(9.27e+34, 'cm^3/(mol*s)'), n=-5.87, Ea=(30960, 'cal/mol'), T0=(1, 'K')),
        alpha=1, T3=(1e-30, 'K'), T1=(1e+30, 'K'), efficiencies={}),
    shortDesc = u"""[Marshall1999]""",
    longDesc =
u"""
Part of the "SOx" subset
T range: 200-2000 K
Table 7 on p. 11333
calculations done at the QCISD(T)/6-311+G(3df,2p)//MP2=FULL/6-31G(d) level of theory
""",
)

entry(
    index = 151,
    label = "S + C2H2 <=> HCCS + H",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.26e+13, 'cm^3/(mol*s)'), n=0.00, Ea=(2677, 'cal/mol'), T0=(300, 'K')),
        arrheniusLow = Arrhenius(A=(3.6e+29, 'cm^6/(mol^2*s)'), n=-3.55, Ea=(3955, 'cal/mol'), T0=(300, 'K')),
        alpha=0.60, T3=(1e-30, 'K'), T1=(1e+30, 'K'), efficiencies={}),
    shortDesc = u"""[Marshall2015]""",
    longDesc =
u"""
Part of the "C-S" mechanism
T range: 300-1000 K
""",
)

entry(
    index = 152,
    label = "S + CS2 <=> CS + S2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.87e+13, 'cm^3/(mol*s)'), n=0.00, Ea=(8843, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Marshall2011]""",
    longDesc =
u"""
Part of the "C-S" mechanism
T range: 690-1040 K
""",
)

entry(
    index = 153,
    label = "NS + NO2 <=> N2 + SO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.55e+13, 'cm^3/(mol*s)'), n=-1.10, Ea=(0, 'cal/mol'), T0=(295, 'K')),
    shortDesc = u"""[Pilling2002]""",
    longDesc =
u"""
Part of the "SOx-NOx" subset
calculations done at the BD-(T)//B3LYP/6-31G++ level of theory
""",
)









"""

SO2+SO2=SO3+SO take from [Marshall2007a]:37 if RMG can't generate it

Change SO in GlarBozzeli to a triplet


SO2 + NO2 <=> NO + SO3
SO + N <=> S + NO
SO2 + N <=> SO + NO
SO + NO2 <=> SO2 + NO
HSO + NO2 <=> HOSO + NO
S + NO2 <=> SO + NO
SO3 + N <=> SO2 + NO
SH + NO2 <=> HSO + NO
SH + N2O <=> HSO + N2



SO3 + H2O <=> H2SO4 dimer?



Gimenez-Lopez, M. Martinez, A. Millera, R. Bilbao, M.U. Alzueta, Comb. Flame 2011, 158(1), 48-56, doi: 10.1016/j.combustflame.2010.07.017
report on:
SO+O2=SO2+O2
SO+OH=HOSO
but the source [24] isn't clear
also HOSO + H, HOSO2 + O2




add eq:
H2O = H2Odimer
C(u4)=C(u2)
CH(u3)=CH(u1) as well as add in FFCM
NH(u2)=NH(u0)
NCN(u0)=NCN(u2)


Or collaps to having just one state, e.g., NH, not NH(u0) and NH(u2)





H2Odimer
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 O u0 p2 c0 {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}







S Thermo:
http://onlinelibrary.wiley.com/doi/10.1002/(SICI)1097-4601(1996)28:10%3C773::AID-KIN8%3E3.0.CO;2-K/epdf
http://pubs.acs.org/doi/abs/10.1021/jp5058012
http://pubs.acs.org/doi/abs/10.1021/jp026524y
[Bozzelli1996]
http://www.sciencedirect.com/science/article/pii/S001021800100325X Appendix A
N2O5: http://pubs.acs.org/doi/abs/10.1021/jp509301t + erratum http://pubs.acs.org/doi/abs/10.1021/acs.jpca.6b12514
http://pubs.acs.org/doi/abs/10.1021/jp9924070
http://onlinelibrary.wiley.com/doi/10.1002/(SICI)1097-4601(1996)28:10%3C773::AID-KIN8%3E3.0.CO;2-K/epdf



N thermo:
http://onlinelibrary.wiley.com/doi/10.1002/kin.20327/epdf




Frequencies:
http://pubs.acs.org/doi/abs/10.1021/jp054722u
http://pubs.acs.org/doi/abs/10.1021/jp067499p
http://pubs.acs.org/doi/abs/10.1021/j100185a016




Out of scope:
HNC: http://pubs.acs.org/doi/abs/10.1021/acs.energyfuels.6b02085

H + H2S = H2 + SH   http://pubs.acs.org/doi/abs/10.1021/jp984242l

Train RMG with Table 5 for CH3SH + H: http://pubs.acs.org/doi/abs/10.1021/jp512966a



"""