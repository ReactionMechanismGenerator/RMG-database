#!/usr/bin/env python
# encoding: utf-8

name = "SOxNOx"
shortDesc = u""
longDesc =u"""
This library includes important SOx and NOx related reactions.
It is by no means comprehensive: Reactions with kinetics in agreement with DeanBozz2000 were not duplicated here
(although some reactions that do appear in DeanBozz2000 are given here with better rate estimates)
This library should be used conjointly with other RMG library as detailed below, yet it should be given priority
Prepared by Alon Grinberg Dana
Notes for users:
- Consider setting an appropriate maximumRadicalElectrons value in your input file to allow the [N] quartet radicat
- For NOx, the Nitrogen_Dean_and_Bozzelli library should be used conjointly with this one.
- It is reccomended to consider the NitrogenCurran, SulfurLibrary, thermo_DFT_CCSDTF12_BAC, primaryThermoLibrary,
  CHN, CHON, BurcatNS, and SOxNOx thermo libraries for your model generation
- Some reactions have different kinetics coefficients reported for different T range,
  'The Low T' rate is reported in the comments.
- This library should be used along with the FFCM kinetic & thermo libraries which handle well the transition of ground/excited states of small radicals
At present (when this library was written) RMG does not differentiate between cis and trans conformers.
When data was available seperately for the production or consumption of two conformers
(e.g.: 'A + B <=> cis-X + C' and 'A + B <=> trans-X + C')
the two rates were summed and reported in this library as a duplicate reaction (using MultiArrhenius, unless otherwise mentioned).
Such instances are marked with the comment 'conformer-dup'.
Some excited species were combined with their ground state in this library (e.g.: NCN, CH2NCN).
This library consists of the following subsets:
* Thermal NO (1-3)
* Prompt NO (4-53)
* N2O Pathway (54-61)
* NNH Pathway (62-68)
* N2H4 + N2O4 (69-101)
* N2O5 (102)
* CH3NO2 (103-107)
* Thermal de-NOx (108-127)
* SOx (128-145)
* C-S (146-147)
* SOx-NOx (148)
Reference legend:
[Baulch1992] R. Atkinson, D.L. Baulch, R.A. Cox, R.F. Hampson, J.A. Kerr, J. Troe, Journal of Physical and Chemical Reference Data, 1992, 21, 1125, doi: 10.1063/1.555918
[Baulch1994] Baulch et al., Journal of Physical and Chemical Reference Data, 1994, 23, 847, doi: 10.1063/1.555953
[Baulch2009] D.L. Baulch et al., Journal of Physical and Chemical Reference Data, 2009, 23(6), 847, doi: 10.1063/1.555953
[Bozzelli1994] J.W. Bozzelli, A.Y. Chang, A.M. Dean, Symp. (Int.) Comb., 1994, 25(1), 965-974, doi: 10.1016/S0082-0784(06)80733-2
[Bozzelli1996] P. Glarborg, D. Kubel, K. Dam-Johansen, H-M. Chiang, J.W. Bozzelli, Int. J. Chem. Kin., 1996, 28(10), 773-790, doi: 10.1002/(SICI)1097-4601(1996)28:10<773::AID-KIN8>3.0.CO;2-K
[Cohen1991] N. Cohen, K. R. Westberg, Journal of Physical and Chemical Reference Data, 1991, 20, 1211,; doi: 10.1063/1.555901
[Cohen1992] Cohen, N. (1992). Chemical Kinetic Data Sheets for High-Temperature Chemical Reactions, Vol. III., Aerospace Corporation Report ATR-91 (7189)-2.
[DeanBozz2000] (RMG's Nitrogen_Dean_and_Bozzelli library) Anthony M. Dean, Joseph W. Bozzelli, Combustion Chemistry of Nitrogen, in: Gas-Phase Combustion Chemistry, Editor: W.C. Gardiner, 2000, 125-341, doi: 10.1007/978-1-4612-1310-9_2
[DeRuyck2001] A.A. Konnov, J. De Ruyck, Comb. Flame, 2001, 125(4), 1258-1264, doi: 10.1016/S0010-2180(01)00250-4
[Dupre1993] K. Tsuchiya, H. Matsui, M. Oya, G. Dupre, in: R. Burn, L.Z. Dumitrescu (Ed.) Shock Waves @ Marseille II (Proceedings Marseille France), 1993, 71-76, doi: 10.1007/978-3-642-78832-1
[Flower1977] W. L. Flower , R. K. Hanson, c. H. Kruger, Comb. Sci. Tech., 1977, 15(3-4), 115-128, doi: 10.1080/00102207708946777
[Friedrichs2011] J. Dammeier, G. Friedrichs, J. Phys. Chem. A, 2011, 115, 14382-14390, doi: 10.1021/jp208715c
[GlarBozz] (RMG's Sulfur/GlarborgBozzelli library) P. Glarborg, D. Kubel, K. Dam-Johansen, H-M. Chiang, J.W. Bozzelli, Int. J. Chem. Kin., 1996, 28, 773-790, doi: 10.1002/(SICI)1097-4601(1996)28:10<773::AID-KIN8>3.0.CO;2-K
[GlarGim] (RMG's Nitrogen_Glarborg_Gimenez_et_al library) Gimenez Lopeza et al., Proceedings of the Combustion Institute, 2009, 32(1), 367–375, doi: 10.1016/j.proci.2008.06.188
[GlarZha] (RMG's Nitrogen_Glarborg_Zhang_et_al library) Kuiwen Zhang et al. Proceedings of the Combustion Institute, 2013, 34, 617–624, doi: 10.1016/j.proci.2012.06.010
[GRI] (RMG's GRI-Mech3.0-N library) GRI-Mech 3.0, http://www.me.berkeley.edu/gri_mech/
[Hanson1981] T.R. Roose, R.K. Hanson, C.H. Kruger, Symposium (International) on Combustion, 1981, 18(1), 853-862, doi: 10.1016/S0082-0784(81)80089-6
[Hanson1984a] M.Y. Louge, R.K. Hanson, Int. J. Chem. Kin., 1984, 16(3), 231-250, doi: 10.1002/kin.550160306
[Hanson1984b] M.Y. Louge, R.K. Hanson, Int. J. Chem. Kin., 1984, 58(3), 291-300, doi: 10.1016/0010-2180(84)90113-5
[Hanson1984c] R.K. Hanson, S. Salimian, In: Combustion Chemistry, W.C. Gardiner (Ed.), 1984, 361-421, doi: 10.1007/978-1-4684-0186-8_6
[Hanson1989]  J.D. Mertens, A.Y. Chang, R.K. Hanson, C.T. Bowman, Int. J. Chem. Kin., 1989, 21(11), 1049-1067, doi: 10.1002/kin.550211107
[Hanson1990a] D.F. Davidson, K. Kohse-Hoinghaus, A.Y. Chang, R.K. Hanson, Int. J. Chem. Kin., 1990, 22(5), 513-535, doi: 10.1002/kin.550220508
[Hanson1990b] D.F. Davidson, R.K. Hanson, Int. J. Chem. Kin., 1990, 22(8), 843–861, doi: 10.1002/kin.550220805
[Hanson1991a] A.J. Dean, R.K. Hanson, C.T. Bowman, J. Phys. Chem., 1991, 95(8), 3180–3189, doi: 10.1021/j100161a042
[Hanson1991b] D.F. Davidson, R.K. Hanson, Symposium (International) on Combustion, 1991, 23(1), 267-273, doi: 10.1016/S0082-0784(06)80269-9
[Hanson1993] M.S. Wooldridge, R.K. Hanson, C.T. Bowman, in: R. Burn, L.Z. Dumitrescu (Ed.) Shock Waves @ Marseille II (Proceedings Marseille France), 1993, 83-88, doi: 10.1007/978-3-642-78832-1
[Hanson1996] S.T. Wooldridge, R.K. Hanson, C.T. Bowman, Int. J. Chem. Kin., 1996, 28(4), 254-258, doi: 10.1002/(SICI)1097-4601(1996)28:4<245::AID-KIN2>3.0.CO;2-V
[Hanson1997] M. Rohrig, E.L. Petersen, D.F. Davidson, R.K. Hanson, Int. J. Chem. Kin., 1997, 29(7), 483-493, doi: 10.1002/(SICI)1097-4601(1997)29:7<483::AID-KIN2>3.0.CO;2-Q
[Herron1991] W. Tsang, J.T. Herron, Journal of Physical and Chemical Reference Data, 1991, 20, 609, doi: 10.1063/1.555890
[Hindelang1993] M.L. Thoma, F.J. Hindelang in: R. Burn, L.Z. Dumitrescu (Ed.) Shock Waves @ Marseille II (Proceedings Marseille France), 1993, 59-64, doi: 10.1007/978-3-642-78832-1
[Howard1988] J.F. Gleason, C.J. Howard, J. Phys. Chem., 1988, 92(12), 3414–3417, doi: 10.1021/j100323a021
[Klemm1985] J.V. Michael, J.W. Sutherland, R.B. Klemm, Int. J. Chem. Kin., 1985, 17(3), 315-326, doi: 10.1002/kin.550170308
[Klemm1990] J.W. Sutherland, P.M. Patterson, R.B. Klemm, J. Phys. Chem., 1990, 94(6), 2471-2475, doi: 10.1021/j100369a049
[Klippenstein2009] S.J. Klippenstein, L.B. Harding, B. Ruscic, R. Sivaramakrishnan, N.K. Srinivasan, M.-C. Su†, J.V. Michael, J. Phys. Chem. A, 2009, 113(38), 10241–10259, doi: 10.1021/jp905454k
[Lin1990] C-Y. Lin, H-T. Wang, M.C. Lin, C.F. Melius, Int. J. Chem. Kin., 1990, 22(5), 455-482, doi: 10.1002/kin.550220504
[Lin1993] Y. He, C.H. Wu, M.C. Lin, C.F. Melius, in: R. Burn, L.Z. Dumitrescu (Ed.) Shock Waves @ Marseille II (Proceedings Marseille France), 1993, 89-94, doi: 10.1007/978-3-642-78832-1
[Lin1996a] A.M. Mebel, E.W.G. Diau, M.C. Lin, K.Morokuma, J. Phys. Chem., 1996, 100, 7517-7525, doi: 10.1021/jp953644f
[Lin1996b] A.M. Mebel, M.C. Lin, K. Morokuma, C.F. Melius, Int. J. Chem. Kin., 1996, 28(9), 693-703, doi: 10.1002/(SICI)1097-4601(1996)28:9<693::AID-KIN8>3.0.CO;2-Q
[Lin1997a] C.C. Hsu, M.C. Lin, A.M. Mebel, C.F. Melius, J. Phys. Chem. A, 1997, 101(1), 60–66, doi: 10.1021/jp962286t
[Lin1997b] J.W. Boughton, S. Kristyan, M.C. Lin, Chemical Physics, 1997, 214(2-3), 219-227, doi: 10.1016/S0301-0104(96)00313-8
[Lin1998a] D. Chakraborty, J. Park, M.C. Lin, Chemical Phisics, 1998, 231(1), 39-49, doi: 10.1016/S0301-0104(98)00033-0
[Lin1998b] J. Park, N.D. Giles, J. Moore, M.C. Lin, J. Phys. Chem. A, 1998, 102(49), 10099–10105, doi: 10.1021/jp983139t
[Lin1998c] A.M. Mebel, M.C. Lin, C.F. Melius, J. Phys. Chem. A, 1998, 102(10), 1803–1807, doi: 10.1021/jp973449w
[Lin1998d] D. Chakraborty, C.C. Hsu, M.C. Lin, J. Chem. Phys., 1998, 109, 8887, doi: 10.1063/1.477560
[Lin1998e] R.N. Musin, M.C. Lin, J. Phys. Chem. A, 1998, 102(10), 1808–1814, doi: 10.1021/jp9801370
[Lin1998f] A.M. Mebel, M.C. Lin, K. Morokuma, Int. J. Chem. Kin., 1998, 30(10), 729-736, doi: 10.1002/(SICI)1097-4601(1998)30:10<729::AID-KIN5>3.0.CO;2-X
[Lin1999a] J. Park, M.C. Lin, J. Phys Chem. A, 1999, 103, 8906-8907, doi: 10.1021/jp990954f
[Lin1999b] A.M. Mebel, L.V. Moskaleva, M.C. Lin, J. Molec. Struc. (Theochem), 1999, 461-462, 223-238, doi: 10.1016/S0166-1280(98)00423-0
[Lin2000a] L.V Moskaleva, M.C. Lin, Proceedings of the Combustion Institute, 2000, 28(2), 2393-2401, doi: 10.1016/S0082-0784(00)80652-9
[Lin2000b] X. Lu, J. Park, M.C. Lin, J. Phys. Chem. A, 2000, 104(38), 8730–8738, doi: 10.1021/jp001610o
[Lin2000c] X. Lu, R.N. Musin, M.C. Lin, J. Phys. Chem. A, 2000, 104(21), 5141–5148, doi: 10.1021/jp000464j
[Lin2001] W.S. Xia, M.C. Lin, J. Chem. Phys., 2001, 114, 4522-4532, doi: 10.1063/1.1337061
[Lin2003a] C-W. Lu, Y-J. Wu, Y-P. Lee, R.S. Zhu, M.C. Lin, J. Phys. Chem. A, 2003, 107(50), 11020–11029, doi: 10.1021/jp036025c
[Lin2003b] R.S. Zhu, M.C. Lin, J. Chem. Phys., 2003, 119, 10667, doi: 10.1063/1.1619373
[Lin2003c] Z.F. Xu, M.C. Lin, Int. J. Chem. Kin., 2003, 35(5), 184-190, doi: 10.1002/kin.10115
[Lin2004] Z.F. Xu, M.C. Lin, Int. J. Chem. Kin., 2004, 36(4), 205-215, doi: 10.1002/kin.10178
[Lin2005a] R.S. Zhu, M.C. Lin, Int. J. Chem. Kin., 2005, 37(10), 593-598, doi: 10.1002/kin.20066
[Lin2005b] R.S. Zhu, M.C. Lin, Ab initio study on the oxidation of NCN by O and HO radicals: Prediction of the total rate constant and product branching ratios, in: 6th International Conference of Chemical Kinetics, NIST, Gaithersberg, MD, 2005
[Lin2005c] Z.F. Xu, C.-H. Hsu, M.C. Lin, J. Chem. Phys., 2005, 122, 234308, doi: 10.1063/1.1917834
[Lin2007a] R.S. Zhu, M.C. Lin, J. Phys. Chem. A, 2007, 111, 6766-6771, doi: 10.1021/jp068991b
[Lin2007b] S. Xu, M.C. Lin, J. Phys. Chem. A, 2007, 111, 6730-6740, doi: 10.1021/jp069038+
[Lin2009a] S. Xu, M.C. Lin, Proceedings of the Combustion Institute, 2009, 32, 99-106, doi: 10.1016/j.proci.2008.07.011
[Lin2009b] S-Y. Tzeng, P-H. Chen, N.S. Wang, L.C. Lee, Z.F. Xu, M.C. Lin, J. Phys. Chem. A, 2009, 113, 6314-6325, doi: 10.1021/jp901903n
[Lin2010a] S. Xu, M.C. Lin, J. Phys. Chem. A, 2010, 114, 5195-5204, doi: 10.1021/jp911048p
[Lin2010b] R.S. Zhu, S.C. Xu, M.C. Lin, Chem. Phys. Letters, 2010, 488(4-6), 121-125, doi: 10.1016/j.cplett.2010.02.003
[Lin2010c] S. Xu, M.C. Lin, Int. J. Chem. Kin., 2010, 42(2), 69-78, doi: 10.1002/kin.20463
[Lin2012] R.S. Zhu, K-Y. Lai, M.C. Lin, J. Phys. Chem. A, 2012, 116, 4466-4472, doi: 10.1021/jp302247k
[Lin2013a] R.S. Zhu, P. Raghunath, M.C. Lin, J. Phys. Chem. A, 2013, 117, 7308-7313, doi: 10.1021/jp401148q
[Lin2013b] W.-S. Teng, L.V. Moskaleva, H.-L. Chen, M.C. Lin, J. Phys. Chem. A, 2013, 117(28), 5775–5784, doi: 10.1021/jp402903t
[Lin2014a] P. Raghunath, Y.H. Lin, M.C. Lin, Computational and Theoretical Chemistry, 2014, 1046, 73-80, doi: 10.1016/j.comptc.2014.07.011
[Lin2014b] P. Raghunath, N.T. Nghia, M.C. Lin, Advances in Quantum Chemistry, 2014, 69, 253-301, doi: 10.1016/B978-0-12-800345-9.00007-6
[Marshall1999a] A. Goumri, J-D.R. Rocha, D. Laakso, C.E. Smith, P. Marshall, J. Phys. Chem. A, 1999, 103(51), 11328–11335 doi: 10.1021/jp9924070
[Marshall1999b] J. Peng, X. Hu, P. Marshall, J. Phys. Chem. A, 1999, 103, 5307-5311, doi: 10.1021/jp984242l
[Marshall2004] A. Goumri, D.D. Shao, P. Marshall, J. Chem. Phys., 2004, 121, 9999, doi: 10.1063/1.1806419
[Marshall2005] J. Naidoo, A. Goumri, P. Marshall, Proceedings of the Combustion Institute, 2005, 30(1), 1219-1225, doi: 10.1016/j.proci.2004.08.214
[Marshall2006] A. Yilmaz, L. Hindiyarti, A.D. Jensen, P. Glarbotg, P. Marshall, J. Phys. Chem. A, 2006, 110 (21), 6654–6659, doi: 10.1021/jp0557215
[Marshall2007a] L. Hindiyarti, P. Glarborg, P. Marshall, J. Phys. Chem. A, 2007, 111(19), 3984–3991, doi: 10.1021/jp067499p
[Marshall2007b] C.L. Rasmussen, P. Glarborg, P. Marshall, Proceedings of the Combustion Institute, 2007, 31, 339–347, doi: 10.1016/j.proci.2006.07.249
[Marshall2011] Y. Gao, P. Marshall, J. Chem. Phys., 2011, 135, 144306, doi: 10.1063/1.3644773
[Marshall2012] K.M. Thompson, Y. Gao, P. Marshall, Int. J. Chem. Kin., 2012, 44(1), 90-99, doi: 10.1002/kin.20612
[Marshall2013] S.J. Klippenstein, L.B. Harding, P. Glarborg, Y. Gao, H. Hu, P. Marshall, J. Phys. Chem. A, 2013, 117, 9011-9022, doi: 10.1021/jp4068069
[Marshall2014] I.M. Alecu, P. Marshall, J. Phys. Chem. A, 2014, 118(48), 11405–11416, doi: 10.1021/jp509301t
[Marshall2015a] S. Ayling, Y. Gao, P. Marshall, Proceedings of the Combustion Institute, 2015, 35(1), 215-222, doi: 10.1016/j.proci.2014.05.079
[Marshall2015b] K.E. Kerr, I.M. Alecu, K.M. Thompson, Y. Gao, P. Marshall, J. Phys. CHem. A, 2015, 119, 7352-7360, doi: 10.1021/jp512966a
[Mukarami1979] T. Higashihara, K. Saito, I. Murakami, Bulletin of the Chemical Society of Japan, 1980, 53(1), 15-18, doi: 10.1246/bcsj.53.15
[Matsui1994] M. Oya, H. Shiina, K. Tsuchiya, H. Matsui, Bulletin of the Chemical Society of Japan, 1994, 67(8), 2311-2313, doi: 10.1246/bcsj.67.2311
[Matsui1996a] H. Shiina, M. Oya, K. Yamashita, A. Miyoshi, H. Matsui, J. Phys. Chem., 1996, 100(6), 2136–2140, doi: 10.1021/jp952472j
[Matsui1996b] K. Tsuchiya, K. Yamashita, A. Miyoshi, H. Matsui, J. Phys. Chem., 1996, 100(43), 17202–17206, doi: 10.1021/jp961252i
[Matsui1998] H. Shiina, A. Miyoshi, H. Matsui, J. Phys. Chem. A, 1998, 102(20), 3556–3559, doi: 10.1021/jp980650d
[Miller1992] J.A. Miller, C.F. Melius, Simp. (Int.) Comb., 1992, 24(1), 719-726, doi: 10.1016/S0082-0784(06)80088-3
[Miller2008] L.B. Harding, S.J. Klippenstein, J.A. Miller, J. Phys. Chem. A, 2008, 112 (3), pp 522–532, doi: 10.1021/jp077526r
[Miller2011] S.J. Klippenstein, L.B. Harding, P. Glarborg, J.A. Miller, Comb. Flame, 2011, 158(4), 774-789, doi: 
[Molina1997] J.T. Jayne, U. Poschl, Y-m. Chen, D. Dai, L.T. Molina, D.R. Worsnop, C.E. Kolb, M.J. Molina, J. Phys. Chem. A, 1997, 101(51), 10000-10011, doi: 10.1021/jp972549z
[Morley1976] C. Morley, Combustion and Flame, 1976, 27, 189-204, doi: 10.1016/0010-2180(76)90022-5
[Page1992] M.R. Soto, M. Page, J. Chem. Phys., 1992, 97, 7287, doi: 10.1063/1.463501
[Palmer1977] H. Freund, H.B. Palmer, Int. J. Chem. Kin., 1977, 9(6), 887-905, doi: 10.1002/kin.550090605
[Perry1984] R.A. Perry, Chem. Phys. Lett., 1984, 106(3), 223-228, doi: 10.1016/0009-2614(84)80230-4
[Perry1985] R.A. Perry, J. Chem. Phys, 1985, 82, 5485, doi: 10.1063/1.448583
[Pilling2002] M.A. Blitz, K.W. McKee, M.J. Pilling, J. Phys. Chem. A, 2002, 106(36), 8406–8410, doi: 10.1021/jp025508y
[Pilling2003] M.A. Blitz, K.J. Hughes, M.J. Pilling, J. Phys. Chem. A, 2003, 107(12), 1971-1978, doi: 10.1021/jp026524y
[Pilling2006] M.A. Blitz, K.J. Hughes, M.J. Pilling, S.H. Robertson, J. Phys. Chem. A, 2006, 110(9), 2996–3009, doi: 10.1021/jp054722u
[Rabinowitz2010] S.M. Hwang, J.A. Cooke, K.J. De Witt, M.J. Rabinowitz, Int. J. Chem. Kin., 2010, 42(3), 168-180, doi: 10.1002/kin.20472
[Roth1993] D. Woiki, P. Roth, in: R. Burn, L.Z. Dumitrescu (Ed.) Shock Waves @ Marseille II (Proceedings Marseille France), 1993, 53-58, doi: 10.1007/978-3-642-78832-1_9
[Roth1996a] D. Woiki, P. Roth, Israel Journal of Chemistry, 1996, 36(3), 279-283, doi: 10.1002/ijch.199600039
[Roth1996b] D. Woiki, P. Roth, Symposium (International) on Combustion, 1996, 26(1), 583-588, doi: 10.1016/S0082-0784(96)80263-3
[Sendt2002] K. Sendt, M. Jazbec, B.S. Haynes, Proceedings of the Combustion Institute, 2002, 29, 2439-2446, doi: 10.1016/S1540-7489(02)80297-8
[Sendt2008] C.R. Zhou, K. Sendt, B.S. Haynes, J. Phys. Chem. A, 2008, 112, 3239-3247, doi: 10.1021/jp710488d
[Somnitz2004] H. Somnitz, Phys. Chem. Chem. Phys., 2004, 6(14), 3844-3851, doi: 10.1039/B317055A
[Troe1984] H.J. Plach, J. Troe, Int. J. Chem. Kin., 1984, 16(12), 1531-1542, doi: 10.1002/kin.550161207
[Tezaki2003] N. Isshiki, Y. Murakami, K. Tsuchiya, A. Tezaki, H. Matsui, J. Phys. Chem. A, 2003, 107(14), 2464–2469, doi: 10.1021/jp0200829
[Varandas2005] P.J.S.B. Caridade, S.P.J. Rodrigues, F. Sousa, A.J.C. Varandas, J. Phys. Chem. A ,2005, 109, 2356-2363, doi: 10.1021/jp045102g
[Wang1982] O.I. Smith, S. Tseregounis, S-N. Wang, Int. J. Chem. Kin., 1982, 14(6), 679-697, doi: 10.1002/kin.550140610
[Yang2012] Y. Guan, B. Yang, J. Comp. Chem., 2012, 33(23), 1870-1879, doi: 10.1002/jcc.23020
"""

entry(
    index = 1,
    label = "N + NO <=> O + N2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.29e+13, 'cm^3/(mol*s)','+|-',8.58e+12), n=0, Ea=(1564, 'cal/mol'), T0=(1, 'K'), Tmin=(1400, 'K'), Tmax=(3500, 'K')),
    shortDesc = u"""[Hanson1990b]""",
    longDesc =
u"""
Part of the "Thermal (Zeldovich) NO" mechanism
See [Hanson1990b] R1; p. 856
Uncertainty: +/-20% at 1400 K to +/- 10% at 3500 K
[DeanBozz2000] reccomend using [Hanson1990b]'s value, which shock-tube measurements are in close agreement with 5 other studies (see Fig 2.1 in [DeanBozz2000] p. 142)
[GRI] fitted to the data of 3 of the sources in [DeanBozz2000]
Also available in RMG's libraries as:
[DeanBozz2000] *reverse direction given: A = 2e+14 cm^3/(mol*s); n = 0; Ea = 76774 cal/mol
[GlarZha]  A = 2.1e13 cm^3/(mol*s); n = 0; Ea = 0
[GlarGim]  A = 3.3e12 cm^3/(mol*s); n = 0.3; Ea = 0 cal/mol
[GRI]      A = 2.7e13 cm^3/(mol*s); n = 0; Ea = 355 cal/mol
""",
)

entry(
    index = 2,
    label = "N + O2 <=> NO + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.0e+09, 'cm^3/(mol*s)'), n=1, Ea=(6500, 'cal/mol'), T0=(1, 'K'), Tmin=(298, 'K'), Tmax=(5000, 'K')),
    shortDesc = u"""[Baulch1994]""",
    longDesc =
u"""
Part of the "Thermal (Zeldovich) NO" mechanism
See [Baulch1994] p. 859
[DeanBozz2000] (p. 230) cite [Cohen1992], which I couldn't access.
[GRI] gives an identical rate based on [Baulch1994].
Also available in RMG's libraries as:
[DeanBozz2000] A = 9e+09 cm^3/(mol*s); n = 1; Ea = 6494 cal/mol
[GlarZha]  A = 6.4e9 cm^3/(mol*s); n = 1; Ea = 6280 cal/mol
[GlarGim]  A = 6.4e9 cm^3/(mol*s); n = 1; Ea = 6280 cal/mol
[GRI]      A = 9e+09 cm^3/(mol*s); n = 1; Ea = 6500 cal/mol
""",
)

entry(
    index = 3,
    label = "NO + H <=> N + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.70e+14, 'cm^3/(mol*s)'), n=0, Ea=(47574, 'cal/mol'), T0=(1, 'K'), Tmin=(1750, 'K'), Tmax=(4200, 'K')),
    shortDesc = u"""[Hanson1984c]""",
    longDesc =
u"""
Part of the "Thermal (Zeldovich) NO" mechanism
5.4 on p. 398
T range: 1750-4200 K
[DeanBozz2000] (p. 231) give A = 6.4e+12 cm^3/(mol*s); n = 0.1; Ea = 21300 cal/mol, citing [Cohen1991]
But [Cohen1991] says that this rate "cannot be fixed more precisely" than an upper boundary of 4.1e+10 (p. 95, k2a)
[GRI] used a fit to low and high T expressions from Atkinson et al., (1989) J. Phys. Chem. Ref. Data 18 88 and Hanson et al., Combustion Chemistry , Springer-Verlag, N.Y., p. 361
[GRI] this optimized this rate and reccomend 59% of the fit's A factor.
[GlarGim] has a ridiculously long citation chain:
Skreiberg et al, Combust. Flame 136, 501-518 (2004) <-- P. Glarborg et al., Combust. Flame 115 (1998) 1–27 <-- P. Glarborg et al., Int. J. Chem. Kinet., 27 (1995), p. 1207 <-- P. Glarborg et al., Int. J. Chem. Kinet., 26, 421 (1994) <-- J.A. Miller, C. T. Bowman, Prog. Energy and Comb. Sci., 15, 287 (1989) <-- J.A. Miller et al., 20th Symp. (Int.) Combust., pp. 673-684, The Combustion Institute, Pittsburgh (1985) <-- W.L. Flower et al., Comb. Sci. Tech. 15, 115 (1977).
The origin of the data is in shock tube experiments by [Flower1977] (p. 14, Fig. 7)
Also available in other RMG libraries as:
[DeanBozz2000] *reverse direction given: A = 1.1e+14 cm^3/(mol*s); n = 0; Ea = 1122 cal/mol
[GlarZha]  *reverse direction given: A = 3.8e+13 cm^3/(mol*s); n = 0; Ea = 0 cal/mol
[GlarGim]  *reverse direction given: A = 3.8e+13 cm^3/(mol*s); n = 0; Ea = 0 cal/mol
[GRI]      *reverse direction given: A = 3.36e+13 cm^3/(mol*s); n = 0; Ea = 385 cal/mol
[Flower1977]                         A = 2.22e+14 cm^3/(mol*s), n = 0; Ea = 50500 cal/mol
""",
)

entry(
    index = 4,
    label = "CH + N2 <=> NCN + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+09, 'cm^3/(mol*s)'), n=0.90, Ea=(17420, 'cal/mol'), T0=(1, 'K'), Tmin=(800, 'K'), Tmax=(4000, 'K')),
    shortDesc = u"""[Lin2013b]""",
    longDesc =
u"""
Part of the "Prompt NO" mechanism. This is the MAIN Prompt NO reaction
calculated at the CCSD(T)/CBS//B3LYP/6-311++G(3df,2p) level of theory
k_A&B on p. 5782
T range: 800-4000 K, 1 atm
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
Also available from [Lin2000a]:
    kinetics = Arrhenius(A=(2.22e+07, 'cm^3/(mol*s)'), n=1.48, Ea=(23367, 'cal/mol'), T0=(1, 'K')),
k3 in [Lin2000a], also first on p. 2397, T range: 1500-4000 K, Done at the G2M(RCC2)//B3LYP/6-311G(d,p) level of theory
Also available from [Miller2008]:
    kinetics = Arrhenius(A=(4.10e+08, 'cm^3/(mol*s)'), n=1.122, Ea=(17525, 'cal/mol'), T0=(1, 'K')),
calculated at the CASPT2,CAS+1+2+QC,CCSD-(T)/aug-cc-pvtz levels of theory, T range: 400-3000
""",
)

entry(
    index = 5,
    label = "CH + N2 <=> HNCN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.65e+21, 'cm^3/(mol*s)'), n=-3.62, Ea=(14196, 'cal/mol'), T0=(1, 'K'), Tmin=(2000, 'K'), Tmax=(4000, 'K')),
    shortDesc = u"""[Lin2000a]""",
    longDesc =
u"""
Part of the "Prompt NO" mechanism
See Table 1 on p. 2397 in [Lin2000a]
T range: 2000-4000 K
Done at the G2M(RCC2)//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 6,
    label = "CH2(S) + N2 <=> CH2N2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 10, 100, 300, 760, 7600], 'torr'),
        arrhenius = [
            Arrhenius(A=(1.22e+30, 'cm^3/(mol*s)'), n=-7.25, Ea=(2730, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(9.45e+30, 'cm^3/(mol*s)'), n=-7.22, Ea=(2734, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(4.55e+31, 'cm^3/(mol*s)'), n=-7.13, Ea=(2653, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(1.46e+32, 'cm^3/(mol*s)'), n=-7.13, Ea=(2774, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(7.41e+32, 'cm^3/(mol*s)'), n=-7.21, Ea=(3088, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(1.39e+34, 'cm^3/(mol*s)'), n=-7.28, Ea=(3804, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
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
    label = "CH2(S) + N2 <=> CHN2 + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 10, 100, 300, 760, 7600], 'torr'),
        arrhenius = [
            Arrhenius(A=(2.27e+12, 'cm^3/(mol*s)'), n=0, Ea=(59358, 'cal/mol'), T0 = (1, 'K'), Tmin=(500, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(2.31e+12, 'cm^3/(mol*s)'), n=0, Ea=(60093, 'cal/mol'), T0 = (1, 'K'), Tmin=(500, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(4.02e+12, 'cm^3/(mol*s)'), n=0, Ea=(61146, 'cal/mol'), T0 = (1, 'K'), Tmin=(500, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(4.51e+12, 'cm^3/(mol*s)'), n=0, Ea=(61365, 'cal/mol'), T0 = (1, 'K'), Tmin=(500, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(5.40e+12, 'cm^3/(mol*s)'), n=0, Ea=(61643, 'cal/mol'), T0 = (1, 'K'), Tmin=(500, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(5.55e+12, 'cm^3/(mol*s)'), n=0, Ea=(61723, 'cal/mol'), T0 = (1, 'K'), Tmin=(500, 'K'), Tmax=(3000, 'K')),
        ],
    ),
    shortDesc = u"""[Lin2010a]""",
    longDesc =
u"""
Part of the "Prompt NO" mechanism
k2 and k4 in [Lin2010a]
T range: 500-3000 K
Done at the CCSD(T)/6-311+G(3df,2p)//B3LYP/6-311+G(3df,2p) level of theory
The rates of  two PDepArrhenius reactions were summed-up, and an Arrhenius expression was fitted and given here (for each P seperately).
The two reactions differ only by the transition state (diazomethane vs. 3H-diazirine)
for each pressure with coefficients of determination ranging 0.9967 to 0.9988 (improving as pressure increases).
""",
)

entry(
    index = 8,
    label = "CH2(S) + N2 <=> cN2CH2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 10, 100, 300, 760, 7600], 'torr'),
        arrhenius = [
            Arrhenius(A=(2.76e+27, 'cm^3/(mol*s)'), n=-6.92, Ea=(2615, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(1.60e+28, 'cm^3/(mol*s)'), n=-6.86, Ea=(2542, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(2.38e+29, 'cm^3/(mol*s)'), n=-6.90, Ea=(2790, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(8.25e+29, 'cm^3/(mol*s)'), n=-6.92, Ea=(2941, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(2.31e+30, 'cm^3/(mol*s)'), n=-6.92, Ea=(3094, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(4.38e+31, 'cm^3/(mol*s)'), n=-6.99, Ea=(3718, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
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
    label = "CH2(S) + N2 <=> HCN + NH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.46e+18, 'cm^3/(mol*s)'), n=-1.52, Ea=(66373, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
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
    label = "CH2(S) + N2 <=> CNNH + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.68e+09, 'cm^3/(mol*s)'), n=0.92, Ea=(65180, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
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
    label = "C(T) + N2 <=> CN + N",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.24e+13, 'cm^3/(mol*s)','+|-',1.05e+13), n=0, Ea=(44900, 'cal/mol'), T0=(1, 'K'), Tmin=(2000, 'K'), Tmax=(5000, 'K')),
    shortDesc = u"""[Baulch2009]""",
    longDesc =
u"""
Part of the "Prompt NO" mechanism
[Baulch2009] p. 860
Uncertainty: +/- 20%
T range: 2000-5000 K
Also available by Hanson 1991 (10.1016/S0082-0784(06)80268-7) shock tube
""",
)

entry(
    index = 12,
    label = "C(T) + NO <=> CO + N",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.0e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K'), Tmin=(1330, 'K'), Tmax=(4000, 'K')),
    shortDesc = u"""[Hanson1991a]""",
    longDesc =
u"""
Part of the "Prompt NO" mechanism
T range: 1330-4000 K
Shock tube measurement, no T dependence
""",
)

entry(
    index = 13,
    label = "C(T) + NO <=> CN + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K'), Tmin=(1330, 'K'), Tmax=(4000, 'K')),
    shortDesc = u"""[Hanson1991a]""",
    longDesc =
u"""
Part of the "Prompt NO" mechanism
T range: 1330-4000 K
Shock tube measurement, no T dependence
""",
)

entry(
    index = 14,
    label = "CH + NO <=> HCN + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.0e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K'), Tmin=(1330, 'K'), Tmax=(4000, 'K')),
    shortDesc = u"""[Hanson1991a]""",
    longDesc =
u"""
Part of the "Prompt NO" mechanism
T range: 1330-4000 K
Shock tube measurement, no T dependence
""",
)

entry(
    index = 15,
    label = "CH3 + N <=> H2CN + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.1e+13, 'cm^3/(mol*s)','+|-',2.5e+13), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K'), Tmin=(1600, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"""[Hanson1991b]""",
    longDesc =
u"""
Part of the "Prompt NO" mechanism
T range: 1600-2000 K
Uncertainty: +/- 35%
Shock tube measurement, no T dependence
""",
)

entry(
    index = 16,
    label = "C2O + N2 <=> cNCN + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.13e+04, 'cm^3/(mol*s)'), n=0, Ea=(27700, 'cal/mol'), T0=(1, 'K'), Tmin=(800, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Lin2010b]""",
    longDesc =
u"""
Part of the "Prompt NO" mechanism in C2 or higher hydrocarbons
k3 in [Lin2010b] (p. 124)
T range: 800-3000 K
Done at the CCSD(T)/6-311+G(3df)//B3LYP/6-311+G(3df) level of theory
""",
)

entry(
    index = 17,
    label = "C2O + N2 <=> CNN + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(36800, 'cal/mol'), T0=(1, 'K'), Tmin=(800, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Lin2010b]""",
    longDesc =
u"""
Part of the "Prompt NO" mechanism in C2 or higher hydrocarbons
k1 in [Lin2010b] (p. 124)
T range: 800-3000 K
Done at the CCSD(T)/6-311+G(3df)//B3LYP/6-311+G(3df) level of theory
The sister reaction "C2O + N2 <=> CNN(Singlet) + CO"
has a rate lower or equal to 1.75e+12exp(33.2 kcal/mol/RT)
formation of NCO + CN and 1CNN/3NCN + CO are too small to be important in the temperature range of 800–3000 K
Predicted values imply that C2O + N2 may not compete with the CH + N2 reaction and
thus the reaction is not expected to be important for the ‘prompt-NO’ formation in combustion.
""",
)

entry(
    index = 18,
    label = "HNCN <=> H + NCN",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.79e+28, 'cm^3/(mol*s)'), n=-3.44, Ea=(64502, 'cal/mol'), T0 = (1, 'K'), Tmin=(2000, 'K'), Tmax=(4000, 'K'))),
    shortDesc = u"""[Lin2000a]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
See Table 1 on p. 2397 in [Lin2000a]
T range: 2000-4000 K
Done at the G2M(RCC2)//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 19,
    label = "NCN <=> N + CN",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(3.25e+15, 'cm^3/(mol*s)'), n=0, Ea=(112921, 'cal/mol'), T0 = (1, 'K'), Tmin=(2000, 'K'), Tmax=(4000, 'K'))),
    shortDesc = u"""[Lin2000a]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
See Table 1 on p. 2397 in [Lin2000a]
T range: 2000-4000 K
Done at the G2M(RCC2)//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 20,
    label = "H + NCN <=> HCN + N",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.89e+14, 'cm^3/(mol*s)'), n=0, Ea=(8425, 'cal/mol'), T0=(1, 'K'), Tmin=(2000, 'K'), Tmax=(4000, 'K')),
    shortDesc = u"""[Lin2000a]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
See Table 1 on p. 2397 in [Lin2000a]
T range: 2000-4000 K
Done at the G2M(RCC2)//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 21,
    label = "CH2(T) + NCN <=> CH2CN + N",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.566e+13, 'cm^3/(mol*s)'), n=0, Ea=(-5184, 'cal/mol'), T0=(1, 'K'), Tmin=(2000, 'K'), Tmax=(4000, 'K')),
    shortDesc = u"""[Lin2000a]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
See Table 1 on p. 2397 in [Lin2000a]
T range: 2000-4000 K
Done at the G2M(RCC2)//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 22,
    label = "CH2(T) + NCN <=> CH2NC + N",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.605e+13, 'cm^3/(mol*s)'), n=0, Ea=(4012, 'cal/mol'), T0=(1, 'K'), Tmin=(2000, 'K'), Tmax=(4000, 'K')),
    shortDesc = u"""[Lin2000a]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
See Table 1 on p. 2397 in [Lin2000a]
T range: 2000-4000 K
Done at the G2M(RCC2)//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 23,
    label = "CH2(T) + NCN <=> CH2NCN",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(2.350e+08, 'cm^3/(mol*s)'), n=0, Ea=(-25608, 'cal/mol'), T0=(1, 'K'), Tmin=(2000, 'K'), Tmax=(4000, 'K')),
            Arrhenius(A=(1.259e+08, 'cm^3/(mol*s)'), n=0, Ea=(-19811, 'cal/mol'), T0=(1, 'K'), Tmin=(2000, 'K'), Tmax=(4000, 'K')),
        ],
    ),
    shortDesc = u"""[Lin2000a]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
See Table 1 on p. 2397 in [Lin2000a]
Excited: Both CH2NCN products (ground + excited states) were taken into account, summing-up their rates
T range: 2000-4000 K
Done at the G2M(RCC2)//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 24,
    label = "CH2(T) + NCN <=> H2CN + CN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.992e+13, 'cm^3/(mol*s)'), n=0, Ea=(4630, 'cal/mol'), T0=(1, 'K'), Tmin=(2000, 'K'), Tmax=(4000, 'K')),
    shortDesc = u"""[Lin2000a]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
See Table 1 on p. 2397 in [Lin2000a]
T range: 2000-4000 K
Done at the G2M(RCC2)//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 25,
    label = "CH2(T) + NCN <=> HCN + HNC",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.694e+12, 'cm^3/(mol*s)'), n=0, Ea=(4633, 'cal/mol'), T0=(1, 'K'), Tmin=(2000, 'K'), Tmax=(4000, 'K')),
    shortDesc = u"""[Lin2000a]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
See Table 1 on p. 2397 in [Lin2000a]
T range: 2000-4000 K
Done at the G2M(RCC2)//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 26,
    label = "CH + NCN <=> HCCN + N",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.291e+14, 'cm^3/(mol*s)'), n=0, Ea=(5094, 'cal/mol'), T0=(1, 'K'), Tmin=(2000, 'K'), Tmax=(4000, 'K')),
    shortDesc = u"""[Lin2000a]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
See Table 1 on p. 2397 in [Lin2000a]
T range: 2000-4000 K
Done at the G2M(RCC2)//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 27,
    label = "CH + NCN <=> HCN + CN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.214e+13, 'cm^3/(mol*s)'), n=0, Ea=(-860, 'cal/mol'), T0=(1, 'K'), Tmin=(2000, 'K'), Tmax=(4000, 'K')),
    shortDesc = u"""[Lin2000a]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
See Table 1 on p. 2397 in [Lin2000a]
T range: 2000-4000 K
Done at the G2M(RCC2)//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 28,
    label = "CN + CN <=> C2N2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.251e+14, 'cm^3/(mol*s)'), n=0, Ea=(8020, 'cal/mol'), T0=(1, 'K'), Tmin=(2000, 'K'), Tmax=(4000, 'K')),
    shortDesc = u"""[Lin2000a]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
See Table 1 on p. 2397 in [Lin2000a]
T range: 2000-4000 K
Done at the G2M(RCC2)//B3LYP/6-311G(d,p) level of theory
In the original paper this reaction appears as "CN + NCN = (CN)2", which is not stoichiometric.
It is ASSUMED that the explicit dimer product is correct, and that the reactants are two CN rads.
Added as a training reaction to R_Recombination
""",
)

entry(
    index = 29,
    label = "CN + NCN <=> NCNCN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.010e+09, 'cm^3/(mol*s)'), n=0, Ea=(-34691, 'cal/mol'), T0=(1, 'K'), Tmin=(2000, 'K'), Tmax=(4000, 'K')),
    shortDesc = u"""[Lin2000a]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
See Table 1 on p. 2397 in [Lin2000a]
T range: 2000-4000 K
Done at the G2M(RCC2)//B3LYP/6-311G(d,p) level of theory
Added as a training reaction to R_Recombination
""",
)

entry(
    index = 30,
    label = "CH3 + NCN <=> CH3CN + N",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.062e+10, 'cm^3/(mol*s)'), n=0, Ea=(13332, 'cal/mol'), T0=(1, 'K'), Tmin=(2000, 'K'), Tmax=(4000, 'K')),
    shortDesc = u"""[Lin2000a]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
See Table 1 on p. 2397 in [Lin2000a]
T range: 2000-4000 K
Done at the G2M(RCC2)//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 31,
    label = "CH3 + NCN <=> CH2NH + CN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.378e+7, 'cm^3/(mol*s)'), n=0, Ea=(-49933, 'cal/mol'), T0=(1, 'K'), Tmin=(2000, 'K'), Tmax=(4000, 'K')),
    shortDesc = u"""[Lin2000a]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
See Table 1 on p. 2397 in [Lin2000a]
T range: 2000-4000 K
Done at the G2M(RCC2)//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 32,
    label = "N + NCN <=> N2 + CN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K'), Tmin=(2000, 'K'), Tmax=(4000, 'K')),
    shortDesc = u"""[Lin2000a]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
See Table 1 on p. 2397 in [Lin2000a]
T range: 2000-4000 K
Done at the G2M(RCC2)//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 33,
    label = "C(T) + NCN <=> CN + CN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K'), Tmin=(2000, 'K'), Tmax=(4000, 'K')),
    shortDesc = u"""[Lin2000a]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
See Table 1 on p. 2397 in [Lin2000a]
T range: 2000-4000 K
Taken from: Y. He, C.H. Wu, M.C. Lin, C.F. Melius, Proc. Nineteenth Int. Symp. Shock Waves, 1995, pp. 89–94, as reported by [Lin2000a]
""",
)

entry(
    index = 34,
    label = "NCN + O2 <=> NCO + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.80e+09, 'cm^3/(mol*s)'), n=0.51, Ea=(24596, 'cal/mol'), T0=(1, 'K'), Tmin=(1000, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Lin2005a]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k1
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
    index = 35,
    label = "NCN + O2 <=> CNO + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.08e+08, 'cm^3/(mol*s)'), n=0.54, Ea=(24461, 'cal/mol'), T0=(1, 'K'), Tmin=(1000, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Lin2005a]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k2
T range: 1000-3000 K
The stationary points of species on the low-energy paths were also examined with the third-order Rayleigh–
Schrodinger perturbation (CASPT3) and the multireference configuration interaction including
Davidson’s correction for higher excitations (MRCI + Q) theories at the CASPT3 (4, 4)/aug-cc-
PVTZ//CASSCF(4,4)/cc-pVDZ(4,4) and MRCI+Q(4,4)/aug-cc-PVTZ //CASSCF (4, 4)/cc-pVDZ(4, 4)
levels. The rate constants have been calculated based on the energies obtained at the G2M(CC1) level.
""",
)

entry(
    index = 36,
    label = "NCN + O <=> CO + N2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.43e+02, 'cm^3/(mol*s)'), n=2.32, Ea=(-1135, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Lin2007a]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k1
T range: 200-3000 K
""",
)

entry(
    index = 37,
    label = "NCN + O <=> CN + NO",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(4.87e+12, 'cm^3/(mol*s)'), n=0.18, Ea=(-46, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(2.07e+13, 'cm^3/(mol*s)'), n=0.15, Ea=(-30, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(3000, 'K')),
        ],
    ),
    shortDesc = u"""[Lin2007a]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k2 and k3
T range: 200-3000 K
Measured rate constant is also available by [Friedrichs2011]
""",
)

entry(
    index = 38,
    label = "CN + NO <=> NCO + N",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(30623, 'cal/mol'), T0=(1, 'K'), Tmin=(2200, 'K'), Tmax=(2810, 'K')),
    shortDesc = u"""[Lin1993]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k1
T range: 2200-2810 K
Shock Tube + BAC-MP4
""",
)

entry(
    index = 39,
    label = "CN + NO <=> CO + N2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.9e+11, 'cm^3/(mol*s)'), n=0, Ea=(27820, 'cal/mol'), T0=(1, 'K'), Tmin=(2200, 'K'), Tmax=(2810, 'K')),
    shortDesc = u"""[Lin1993]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k2
T range: 2200-2810 K
Shock Tube + BAC-MP4
""",
)

entry(
    index = 40,
    label = "NCN + O <=> N + NCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.21e+09, 'cm^3/(mol*s)'), n=0.42, Ea=(-157, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Lin2007a]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k4
T range: 200-3000 K
""",
)

entry(
    index = 41,
    label = "NCN + NO <=> CN + N2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.89e+12, 'cm^3/(mol*s)','+|-',1.32e+11), n=0, Ea=(6286, 'cal/mol','+|-',380), T0=(1, 'K'), Tmin=(764, 'K'), Tmax=(1944, 'K')),
    shortDesc = u"""[Friedrichs2011]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k10
rate expression on p. 14386
Experimental T range: 764-1944 K
Uncertainty estimate: +/- 7%; activation energy uncertainty: +/- 380 cal/mol
""",
)

entry(
    index = 42,
    label = "NCN + NO2 <=> NCNO + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.7e+12, 'cm^3/(mol*s)','+|-',8.9e+11), n=0, Ea=(9082, 'cal/mol','+|-',910), T0=(1, 'K'), Tmin=(704, 'K'), Tmax=(1659, 'K')),
    shortDesc = u"""[Friedrichs2011]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k11
rate expression on p. 14388
Experimental T range: 704-1659 K
Uncertainty estimate: +/- 19%; activation energy uncertainty: +/- 910 cal/mol
""",
)

entry(
    index = 43,
    label = "HNCN + OH <=> OHNHCN",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 10, 100, 300, 760, 7600], 'torr'),
        arrhenius = [
            Arrhenius(A=(2.43e+40, 'cm^3/(mol*s)'), n=-10.14, Ea=(4261, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(3.16e+41, 'cm^3/(mol*s)'), n=-10.17, Ea=(4539, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(5.17e+42, 'cm^3/(mol*s)'), n=-10.22, Ea=(5065, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(1.96e+43, 'cm^3/(mol*s)'), n=-10.24, Ea=(5425, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(5.47e+43, 'cm^3/(mol*s)'), n=-10.24, Ea=(5773, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(4.35e+44, 'cm^3/(mol*s)'), n=-10.19, Ea=(6818, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
        ],
    ),
    shortDesc = u"""[Lin2007b]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k1 (see reactions on p. 6735, and rates on p. 6738)
T range: 300-3000 K
Done at the CCSD(T)/6-311+G(3df,2p)//B3LYP/6-311+G(3df,2p) level of theory
""",
)

entry(
    index = 44,
    label = "HNCN + OH <=> HCN + HNO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.77e+11, 'cm^3/(mol*s)'), n=0, Ea=(14387, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Lin2007b]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k3 and k6 (see reactions on p. 6735, and rates on p. 6738)
T range: 300-3000 K
Done at the CCSD(T)/6-311+G(3df,2p)//B3LYP/6-311+G(3df,2p) level of theory
Since this reaction principally has a degeneracy of 2 (already taken into account in the above rate),
The rates of the two PDepArrhenius reactions were summed-up.
Since k3 is almost independent on pressure, and k6 is more than an order of magnitude lower,
the overall rate had an almost insignificant pressure dependent rate:
    kinetics = PDepArrhenius(
        pressures = ([1, 10, 100, 300, 760, 7600], 'torr'),
        arrhenius = [
            Arrhenius(A=(1.76e+11, 'cm^3/(mol*s)'), n=0, Ea=(14377, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(1.78e+11, 'cm^3/(mol*s)'), n=0, Ea=(14389, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(1.76e+11, 'cm^3/(mol*s)'), n=0, Ea=(14385, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(1.78e+11, 'cm^3/(mol*s)'), n=0, Ea=(14389, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(1.77e+11, 'cm^3/(mol*s)'), n=0, Ea=(14387, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(1.77e+11, 'cm^3/(mol*s)'), n=0, Ea=(14395, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
        ],
    ),
(This was calculated by fitting an Arrhenius expression to the sum of the rates with a coefficient of determination = 0.9993)
Hence, the final fitted rate is the average of the above PDepArrhenius rates.
""",
)

entry(
    index = 45,
    label = "HNCN + OH <=> HONCNH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 10, 100, 300, 760, 7600], 'torr'),
        arrhenius = [
            Arrhenius(A=(8.85e+35, 'cm^3/(mol*s)'), n=-9.02, Ea=(1304, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(6.26e+38, 'cm^3/(mol*s)'), n=-9.54, Ea=(2579, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(2.05e+41, 'cm^3/(mol*s)'), n=-9.95, Ea=(3768, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(5.49e+41, 'cm^3/(mol*s)'), n=-9.93, Ea=(3873, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(1.87e+43, 'cm^3/(mol*s)'), n=-10.25, Ea=(4660, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(2.46e+44, 'cm^3/(mol*s)'), n=-10.26, Ea=(5475, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
        ],
    ),
    shortDesc = u"""[Lin2007b]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k4 (see reactions on p. 6735, and rates on p. 6738)
T range: 300-3000 K
Done at the CCSD(T)/6-311+G(3df,2p)//B3LYP/6-311+G(3df,2p) level of theory
""",
)

entry(
    index = 46,
    label = "HNCN + OH <=> NH2 + NCO",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 10, 100, 300, 760, 7600], 'torr'),
        arrhenius = [
            Arrhenius(A=(1.92e+11, 'cm^3/(mol*s)'), n=0, Ea=(7591, 'cal/mol'), T0 = (1, 'K'), Tmin=(500, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(2.06e+11, 'cm^3/(mol*s)'), n=0, Ea=(7681, 'cal/mol'), T0 = (1, 'K'), Tmin=(500, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(2.49e+11, 'cm^3/(mol*s)'), n=0, Ea=(8239, 'cal/mol'), T0 = (1, 'K'), Tmin=(500, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(5.89e+11, 'cm^3/(mol*s)'), n=0, Ea=(8833, 'cal/mol'), T0 = (1, 'K'), Tmin=(500, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(3.41e+11, 'cm^3/(mol*s)'), n=0, Ea=(9187, 'cal/mol'), T0 = (1, 'K'), Tmin=(500, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(4.89e+11, 'cm^3/(mol*s)'), n=0, Ea=(10761, 'cal/mol'), T0 = (1, 'K'), Tmin=(500, 'K'), Tmax=(3000, 'K')),
        ],
    ),
    shortDesc = u"""[Lin2007b]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k5 and k10 (see reactions on p. 6735, and rates on p. 6738)
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
    index = 47,
    label = "HNCN + OH <=> H2O + NCN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.04e+05, 'cm^3/(mol*s)'), n=2.48, Ea=(-1886, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Lin2007b]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k7 (see reactions on p. 6735, and rates on p. 6738)
T range: 300-3000 K
Done at the CCSD(T)/6-311+G(3df,2p)//B3LYP/6-311+G(3df,2p) level of theory
Excited: This rate represents the reaction with NCN(T) as the product.
Kinetics for producing NCN(S) were also given from the same source:
    kinetics = PDepArrhenius(
        pressures = ([1, 10, 100, 300, 760, 7600], 'torr'),
        arrhenius = [
            Arrhenius(A=(2.37e+01, 'cm^3/(mol*s)'), n=2.99, Ea=(-346, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(2.92e+01, 'cm^3/(mol*s)'), n=2.97, Ea=(-284, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(2.99e+01, 'cm^3/(mol*s)'), n=2.97, Ea=(-284, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(3.28e+01, 'cm^3/(mol*s)'), n=2.95, Ea=(-264, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(4.16e+01, 'cm^3/(mol*s)'), n=2.92, Ea=(-203, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(2.79e+02, 'cm^3/(mol*s)'), n=2.69, Ea=(-344, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
        ],
    ),
Added as a training reaction to H_Abstraction
""",
)

entry(
    index = 48,
    label = "HNCN + OH <=> NCOHNH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 10, 100, 300, 760, 7600], 'torr'),
        arrhenius = [
            Arrhenius(A=(1.72e+37, 'cm^3/(mol*s)'), n=-9.55, Ea=(7019, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(1.96e+38, 'cm^3/(mol*s)'), n=-9.54, Ea=(7836, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(8.43e+38, 'cm^3/(mol*s)'), n=-9.39, Ea=(6683, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(8.55e+38, 'cm^3/(mol*s)'), n=-9.23, Ea=(9364, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(5.02e+38, 'cm^3/(mol*s)'), n=-9.03, Ea=(9731, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(8.67e+36, 'cm^3/(mol*s)'), n=-8.19, Ea=(10264, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
        ],
    ),
    shortDesc = u"""[Lin2007b]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k8 (see reactions on p. 6735, and rates on p. 6738)
T range: 300-3000 K
Done at the CCSD(T)/6-311+G(3df,2p)//B3LYP/6-311+G(3df,2p) level of theory
""",
)

entry(
    index = 49,
    label = "HNCN + OH <=> NCOH + NH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 10, 100, 300, 760, 7600], 'torr'),
        arrhenius = [
            Arrhenius(A=(2.04e+06, 'cm^3/(mol*s)'), n=1.72, Ea=(5892, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(4.53e+06, 'cm^3/(mol*s)'), n=1.62, Ea=(6168, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(3.17e+05, 'cm^3/(mol*s)'), n=1.39, Ea=(6866, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(1.60e+08, 'cm^3/(mol*s)'), n=1.19, Ea=(7472, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(8.97e+08, 'cm^3/(mol*s)'), n=1.00, Ea=(8157, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(6.02e+10, 'cm^3/(mol*s)'), n=0.51, Ea=(10278, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
        ],
    ),
    shortDesc = u"""[Lin2007b]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k9 (see reactions on p. 6735, and rates on p. 6738)
T range: 300-3000 K
Done at the CCSD(T)/6-311+G(3df,2p)//B3LYP/6-311+G(3df,2p) level of theory
""",
)

entry(
    index = 50,
    label = "NCN + OH <=> HCN + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.23e+11, 'cm^3/(mol*s)'), n=0.35, Ea=(4660, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(3000, 'K')),
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
    index = 51,
    label = "O + HNCN <=> NO + HNC",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.48e+14, 'cm^3/(mol*s)'), n=-0.08, Ea=(22, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
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
    index = 52,
    label = "O + HNCN <=> NH + NCO",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1.14e+14, 'cm^3/(mol*s)'), n=-0.13, Ea=(310, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(8.61e+25, 'cm^3/(mol*s)'), n=-5.14, Ea=(10014, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
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
    index = 53,
    label = "O + HNCN <=> OH + NCN",
    degeneracy = 4,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(4.00e-04, 'cm^3/(mol*s)'), n=4.02, Ea=(2560, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(2.08e+09, 'cm^3/(mol*s)'), n=0.47, Ea=(-1677, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(3.55e+28, 'cm^3/(mol*s)'), n=-5.79, Ea=(17237, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(1.48e+22, 'cm^3/(mol*s)'), n=-3.37, Ea=(5429, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
        ],
    ),
    shortDesc = u"""[Lin2009a]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k3, k5, k7, and k8 (all form the exact same products, degeneracy = 4)
T range: 300-3000 K
Done at the CCSD(T)/6-311+G(3df,2p)//CCSD/6-311++G(d,p) level of theory
Added as a training reaction to H_Abstraction (k8 only)
""",
)

entry(
    index = 54,
    label = "O + HNCN <=> HN(O)CN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.45e+39, 'cm^3/(mol*s)'), n=-10.47, Ea=(5316, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
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
    index = 55,
    label = "O + HNCN <=> CN + HNO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.32e+10, 'cm^3/(mol*s)'), n=0.62, Ea=(189, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Lin2009a]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k6
T range: 300-3000 K
Done at the CCSD(T)/6-311+G(3df,2p)//CCSD/6-311++G(d,p) level of theory
""",
)

entry(
    index = 56,
    label = "O2 + HNCN <=> OH + NCNO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.31e-22, 'cm^3/(mol*s)'), n=8.55, Ea=(12102, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Lin2009a]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k10
T range: 300-3000 K
Done at the CCSD(T)/6-311+G(3df,2p)//CCSD/6-311++G(d,p) level of theory
""",
)

entry(
    index = 57,
    label = "O2 + HNCN <=> HO2 + NCN",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1.04e-10, 'cm^3/(mol*s)'), n=5.92, Ea=(21661, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(1.61e+08, 'cm^3/(mol*s)'), n=1.25, Ea=(24443, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
        ],
    ),
    shortDesc = u"""[Lin2009a]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k11 and k13
T range: 300-3000 K
Done at the CCSD(T)/6-311+G(3df,2p)//CCSD/6-311++G(d,p) level of theory
Added as a training reaction to H_Abstraction (k13 only)
""",
)

entry(
    index = 58,
    label = "O2 + HNCN <=> O + HNC(O)N",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.98e+09, 'cm^3/(mol*s)'), n=0.64, Ea=(38154, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Lin2009a]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k12
T range: 300-3000 K
Done at the CCSD(T)/6-311+G(3df,2p)//CCSD/6-311++G(d,p) level of theory
""",
)

entry(
    index = 59,
    label = "CN + NCO <=> NCN + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.46e+14, 'cm^3/(mol*s)'), n=0.30, Ea=(952, 'cal/mol'), T0=(1, 'K'), Tmin=(1000, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Lin2009b]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
See p. 6324 in [Lin2000a]
T range: 1000-3000 K
Excited: Because k_triplet is much less than k_singlet by a factor of 20-80,
the contribution of the triplet channel to the NCO(T) + CN reaction is negligible.
Several levels of theory were used:
G2M//B3LYP/6-311+G(d), QCISD(T)/6-311+G(3df)//QCISD/6-311+G(d), CCSD(T)/6-311+G(3df)//CCSD/6-311+G(d),
CASPT2(10,10)/6-311+G(d)//CAS(10,10)/6-311+G(d).
""",
)

entry(
    index = 60,
    label = "C2N2 + O <=> CN + NCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.01e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K'), Tmin=(1920, 'K'), Tmax=(2110, 'K')),
    shortDesc = u"""[Hanson1984a]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k2
T range: 1920-2110 K
Shock Tube
""",
)

entry(
    index = 61,
    label = "CN + HCN <=> C2N2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.51e+07, 'cm^3/(mol*s)'), n=1.71, Ea=(1530, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Hanson1996]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
T range: 300-3000 K
k2 Table 1, p. 249
Shock Tube
""",
)

entry(
    index = 62,
    label = "CN + O <=> CO + N",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K'), Tmin=(1920, 'K'), Tmax=(2110, 'K')),
    shortDesc = u"""[Hanson1984a]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k3
T range: 1920-2110 K
Shock Tube
""",
)

entry(
    index = 64,
    label = "CN + O2 <=> NCO + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K'), Tmin=(1920, 'K'), Tmax=(2110, 'K')),
    shortDesc = u"""[Hanson1984a]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k4
T range: 1920-2110 K
Shock Tube
""",
)

entry(
    index = 65,
    label = "NCO + H2 <=> HNCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.61e+12, 'cm^3/(mol*s)','+|-',1.46e+12), n=0, Ea=(9000, 'cal/mol'), T0=(1, 'K'), Tmin=(592, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"""[Perry1985]""",
    longDesc =
u"""
Part of the "Prompt NO, NCN subset" mechanism
k6
T range: 592-913(-2000) K
Ea uncertainty: 17%
Shock Tube
""",
)

entry(
    index = 66,
    label = "N2O <=> N2 + O",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(4.0e+14, 'cm^3/(mol*s)'), n=0, Ea=(56099, 'cal/mol'), T0 = (1, 'K'), Tmin=(1000, 'K'), Tmax=(3000, 'K'))),
    shortDesc = u"""[DeanBozz2000]""",
    longDesc =
u"""
Part of the "N2O Pathway"
Rate taken from:
Johnsson, J.E., Glarborg, P., & Dam-Johansen, K. (1992). 24th Symposium (International) on Combustion, p. 917
As reported by Dean & Bozzelli, see 2.5.3 on p. 143
Measured in a flow reactor with Ar as bath gas.
T range: 1000-3000 K
""",
)

entry(
    index = 67,
    label = "O + N2O <=> N2 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10810, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[DeanBozz2000]""",
    longDesc =
u"""
Part of the "N2O Pathway"
Rate taken from:
Davidson, D.E, DiRosa, M.D., Chang, A.Y., & Hanson, R.K. (1991). 18th International Symposium on Shock Waves, Sendai, p. 813
As reported by Dean & Bozzelli, see 2.5.4 omn p. 145
""",
)

entry(
    index = 68,
    label = "O + N2O <=> NO + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+13, 'cm^3/(mol*s)'), n=0, Ea=(23151, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[DeanBozz2000]""",
    longDesc =
u"""
Part of the "N2O Pathway"
Rate taken from:
Davidson, D.E, DiRosa, M.D., Chang, A.Y., & Hanson, R.K. (1991). 18th International Symposium on Shock Waves, Sendai, p. 813
As reported by Dean & Bozzelli, see 2.5.4 omn p. 145
""",
)

entry(
    index = 69,
    label = "H + N2O <=> HNNO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(9082, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[DeanBozz2000]""",
    longDesc =
u"""
Part of the "N2O Pathway"
See [DeanBozz2000] 2.6.3, p. 158, and Table 2.6 on p. 163
""",
)

entry(
    index = 70,
    label = "H + N2O <=> NNOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+14, 'cm^3/(mol*s)'), n=0, Ea=(18403, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[DeanBozz2000]""",
    longDesc =
u"""
Part of the "N2O Pathway"
See [DeanBozz2000] 2.6.3, p. 158, and Table 2.6 on p. 163
""",
)

entry(
    index = 71,
    label = "HNNO <=> NH + NO",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(4.0e+15, 'cm^3/(mol*s)'), n=0, Ea=(49952, 'cal/mol'), T0 = (1, 'K'))),
    shortDesc = u"""[DeanBozz2000]""",
    longDesc =
u"""
Part of the "N2O Pathway"
See [DeanBozz2000] 2.6.3, p. 158, and Table 2.6 on p. 163
""",
)

entry(
    index = 72,
    label = "HNNO <=> N2 + OH",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(6.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(29398, 'cal/mol'), T0 = (1, 'K'))),
    shortDesc = u"""[DeanBozz2000]""",
    longDesc =
u"""
Part of the "N2O Pathway"
See [DeanBozz2000] 2.6.3, p. 158, and Table 2.6 on p. 163
""",
)

entry(
    index = 73,
    label = "N2O + NO <=> N2 + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.26e+05, 'cm^3/(mol*s)'), n=2.23, Ea=(46286, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(5000, 'K')),
    shortDesc = u"""[Lin1996b]""",
    longDesc =
u"""
Part of the "N2O Pathway"
k1 on p. 695
T range: 300-5000 K
calculations done at the B3LYP/6-311G(d,p)//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 74,
    label = "N2O + OH <=> N2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.29e-02, 'cm^3/(mol*s)'), n=4.72, Ea=(36565, 'cal/mol'), T0=(1, 'K'), Tmin=(1000, 'K'), Tmax=(5000, 'K')),
    shortDesc = u"""[Lin1996b]""",
    longDesc =
u"""
Part of the "N2O Pathway"
k2A on p. 702
T range: 1000-5000 K
calculations done at the B3LYP/6-311G(d,p)//B3LYP/6-311G(d,p) level of theory
For the low T range (300-1000 K) the reccomended rate for both "N2O + OH <=> N2 + HO2" and "N2O + OH <=> HNO + NO" is:
    kinetics = Arrhenius(A=(2.87e+08, 'cm^3/(mol*s)'), n=0, Ea=(20436, 'cal/mol'), T0=(1, 'K')),
""",
)

entry(
    index = 75,
    label = "N2O + OH <=> HNO + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.18e-04, 'cm^3/(mol*s)'), n=4.33, Ea=(25039, 'cal/mol'), T0=(1, 'K'), Tmin=(1000, 'K'), Tmax=(5000, 'K')),
    shortDesc = u"""[Lin1996b]""",
    longDesc =
u"""
Part of the "N2O Pathway"
k2B on p. 702
T range: 1000-5000 K
calculations done at the B3LYP/6-311G(d,p)//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 76,
    label = "HNNO <=> O + NNH",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(4.9e+15, 'cm^3/(mol*s)'), n=0, Ea=(61663, 'cal/mol'), T0 = (1, 'K'))),
    shortDesc = u"""[DeanBozz2000]""",
    longDesc =
u"""
Part of the "NNH Pathway"
See [DeanBozz2000] 2.6.3, p. 158, and Table 2.6 on p. 163
""",
)

entry(
    index = 77,
    label = "NNH + O <=> N2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.9e+14, 'cm^3/(mol*s)'), n=-0.274, Ea=(-22, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2500, 'K')),
    shortDesc = u"""[Miller2011]""",
    longDesc =
u"""
Part of the "NNH Pathway"
calculated at the (CCSD(T) and QCISD(T)) and multireference CASPT2 and CAS + 1 + 2 + QC electronic structure calculations level
Also available from [Bozzelli1994]:
    kinetics = Arrhenius(A=(5.5e+18, 'cm^3/(mol*s)'), n=-1.06, Ea=(47300, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(4000, 'K')),
T range: 300-4000 K, k1d, QRRK
""",
)

entry(
    index = 78,
    label = "NNH + O <=> N2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0.145, Ea=(-217, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2500, 'K')),
    shortDesc = u"""[Miller2011]""",
    longDesc =
u"""
Part of the "NNH Pathway"
calculated at the (CCSD(T) and QCISD(T)) and multireference CASPT2 and CAS + 1 + 2 + QC electronic structure calculations level
""",
)

entry(
    index = 79,
    label = "NNH + O <=> NH + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.2e+11, 'cm^3/(mol*s)','+|-',2.6e+11), n=0.388, Ea=(-409, 'cal/mol','+|-',102), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2500, 'K')),
    shortDesc = u"""[Miller2011]""",
    longDesc =
u"""
Part of the "NNH Pathway"
calculated at the (CCSD(T) and QCISD(T)) and multireference CASPT2 and CAS + 1 + 2 + QC electronic structure calculations level
Also available from [DeRuyck2001]:
    kinetics = Arrhenius(A=(2e+14, 'cm^3/(mol*s)'), n=0, Ea=(4015, 'cal/mol'), T0=(1, 'K'), Tmin=(1200, 'K'), Tmax=(2500, 'K')),
k1, T range: 1200-2500 K, Uncertainty: A 50%, Ea 25%
""",
)

entry(
    index = 80,
    label = "N2 + H <=> NNH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.6e+15, 'cm^3/(mol*s)'), n=-0.64, Ea=(15333, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(25000, 'K')),
    shortDesc = u"""[Varandas2005]""",
    longDesc =
u"""
Part of the "NNH Pathway"
T range: 300-25000 K
reaction -3 in [Varandas2005]
Fits to a total of 972 MRCI energies (based on the aug-cc-pVQZ basis set of Dunning27), scaled by the DMBE-SEC
method to account for excitations higher than singles and doubles and the incompleteness of the one-electron basis set.
The paper reports a HO-RR rate, and a sum-over-states rate (where vib-rot aren't assumed to be independent).
The sum-over-states rate was taken here.
Added as a training reaction to R_Addition_MultipleBond
""",
)

entry(
    index = 81,
    label = "N + NH <=> N2 + H",
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
    index = 82,
    label = "N + NH <=> N + N + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.75e+14, 'cm^3/(mol*s)'), n=-0.20, Ea=(54159, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Varandas2005]""",
    longDesc =
u"""
Part of the "NNH Pathway"
reaction 1 in [Varandas2005]
Fits to a total of 972 MRCI energies (based on the aug-cc-pVQZ basis set of Dunning27), scaled by the DMBE-SEC
method to account for excitations higher than singles and doubles and the incompleteness of the one-electron basis set.
The fragmentation channel (N + NH <=> N + N + H) opens up at ~3000 K, and even at very high T (25000 K) it rate is
an order of magnitute lower than N + NH <=> N2 + H. Although probably insignificant, it is brought here for completeness.
""",
)

entry(
    index = 83,
    label = "N + H2 <=> NH + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.60e+14, 'cm^3/(mol*s)'), n=0, Ea=(25138, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Hanson1990b]""",
    longDesc =
u"""
Part of the "NNH Pathway"
See [Hanson1990b] R2; p. 860
Shock Tube
Added as a training reaction to H_Abstraction
""",
)

entry(
    index = 84,
    label = "NNH + O2 <=> N2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.55e+13, 'cm^3/(mol*s)','*|/',1.5), n=-0.385, Ea=(-13.4, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(2400, 'K')),
    shortDesc = u"""[Miller2011]""",
    longDesc =
u"""
Part of the "NNH Pathway"
p. 776
T range: 200-2400 K
Uncertainty: a factor of 1.5
calculated at the (CCSD(T) and QCISD(T)) and multireference CASPT2 and CAS + 1 + 2 + QC electronic structure calculations level
""",
)

entry(
    index = 85,
    label = "NNH + H <=> H2 + N2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(-894, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[DeanBozz2000]""",
    longDesc =
u"""
Part of the "NNH Pathway"
reaction 28c, p. 237
DHT estimate
""",
)

entry(
    index = 86,
    label = "NNH + OH <=> H2O + N2",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(2.4e+22, 'cm^3/(mol*s)'), n=-2.88, Ea=(2444, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.25e+06, 'cm^3/(mol*s)'), n=2.00, Ea=(-1192, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    shortDesc = u"""[DeanBozz2000]""",
    longDesc =
u"""
Part of the "NNH Pathway"
reaction 28d1 and 28d2, p. 237-238
calculated using  QRRK / DHT
""",
)

entry(
    index = 87,
    label = "NH3 <=> NH2 + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(2.20e+16, 'cm^3/(mol*s)'), n=0, Ea=(93468, 'cal/mol'), T0 = (1, 'K'), Tmin=(2200, 'K'), Tmax=(2800, 'K'))),
    shortDesc = u"""[Hanson1990a]""",
    longDesc =
u"""
Part of the "NHx" subset
R1 in Table 1, p. 521
T range: 2200-2800 K
Shock Tube
The competing reaction "NH3 <=> NH + H2" is spin-hindered, and is ~40 times lower in rate, and can be neglected. Source: [Hanson1984c]
Train!
""",
)

entry(
    index = 88,
    label = "NH2 + H <=> NH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.00e+13, 'cm^3/(mol*s)'), n=0, Ea=(3650, 'cal/mol'), T0=(1, 'K'), Tmin=(2200, 'K'), Tmax=(2800, 'K')),
    shortDesc = u"""[Hanson1990a]""",
    longDesc =
u"""
Part of the "NHx" subset
R9 in Table 1, p. 521
T range: 2200-2800 K
Shock Tube
Train!
""",
)

entry(
    index = 90,
    label = "HNCO <=> NH + CO",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(3.26e+35, 'cm^3/(mol*s)'), n=-5.11, Ea=(110000, 'cal/mol'), T0 = (1, 'K'), Tmin=(1830, 'K'), Tmax=(3340, 'K'))),
    shortDesc = u"""[Hanson1989]""",
    longDesc =
u"""
Part of the "NHx" subset
T range: 1830-3340 K
Shock Tube
k1a
Measured in Ar
""",
)

entry(
    index = 91,
    label = "NH <=> N + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(2.65e+14, 'cm^3/(mol*s)'), n=0, Ea=(75500, 'cal/mol'), T0 = (1, 'K'), Tmin=(3140, 'K'), Tmax=(3320, 'K'))),
    shortDesc = u"""[Hanson1989]""",
    longDesc =
u"""
Part of the "NHx" subset
T range: 3140-3320 K
Shock Tube
k3
Measured in Ar
""",
)

entry(
    index = 92,
    label = "N2H4 + NO <=> N2H3 + HNO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.44e+01, 'cm^3/(mol*s)'), n=3.16, Ea=(30488, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"""[Lin2014a]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
reaction (1), p. 78
T range: 300-2000 K
calculations done at the CCSD(T)/CBS//CCSD level of theoty,
and the moment of inertia and harmonic vibrational frequencies were obtained by the CCSD/6-31G(d,p) level
Added as a training reaction to H_Abstraction
""",
)

entry(
    index = 93,
    label = "N2H4 + NO <=> NH2 + H2NNO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.03e+01, 'cm^3/(mol*s)'), n=2.98, Ea=(35609, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2000, 'K')),
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
    index = 94,
    label = "N2H4 + NO2 <=> N2H3 + HNO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e-02, 'cm^3/(mol*s)'), n=4.14, Ea=(7947, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"""[Lin2014a]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
reaction (4), p. 78
T range: 300-2000 K
calculations done at the CCSD(T)/CBS//CCSD level of theoty,
and the moment of inertia and harmonic vibrational frequencies were obtained by the CCSD/6-31G(d,p) level
Added as a training reaction to H_Abstraction
""",
)

entry(
    index = 95,
    label = "N2H3 + HNO <=> N2H3NO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.65e-02, 'cm^3/(mol*s)'), n=3.82, Ea=(17780, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2000, 'K')),
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
    index = 96,
    label = "N2H3 + HNO <=> N2H2 + HONH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.85e-17, 'cm^3/(mol*s)'), n=8.15, Ea=(904, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2000, 'K')),
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
    index = 97,
    label = "N2H3 + HONO <=> N2H3NO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.69e+00, 'cm^3/(mol*s)'), n=2.94, Ea=(15379, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2000, 'K')),
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
    index = 98,
    label = "N2H3 + HONO <=> N2H2 + H2O + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.79e-08, 'cm^3/(mol*s)'), n=5.51, Ea=(11112, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2000, 'K')),
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
    index = 99,
    label = "N2H4 <=> NH2 + NH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.57e+21, 's^-1'), n=-1.04, Ea=(66565, 'cal/mol'), T0=(1, 'K'), Tmin=(700, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"""[Lin2014b]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
p. 264
T range: 700-2000 K
calculations done at the RCCSD(T)/6-311þG(3df,2p)//B3LYP/6-311G(d,p) level of theoty
Only High Pressure Limit rate was taken; low limit and 1 atm rate are also available from the same source
Also available from [Klippenstein2009]:
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(9.33e-10, 's^-1'), n=-0.414, Ea=(33, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(4.48e-14, 'cm^3/(mol*s)'), n=-5.49, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
        alpha=0.31, T3=(1e-30, 'K'), T1=(1e+30, 'K'), efficiencies={}),
Table 3, p. 10245, T range: 300-2500 K, calculated at the (CCSD(T) and CAS+1+2+QC level
Added as a training reaction to R_Recombination
""",
)

entry(
    index = 100,
    label = "N2H4 <=> N2H3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.69e+14, 's^-1'), n=-0.28, Ea=(76678, 'cal/mol'), T0=(1, 'K'), Tmin=(700, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"""[Lin2014b]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
p. 264
T range: 700-2000 K
calculations done at the RCCSD(T)/6-311þG(3df,2p)//B3LYP/6-311G(d,p) level of theoty
Only High Pressure Limit rate was taken low limit and 1 atm rate are also available from the same source
Added as a training reaction to R_Recombination
""",
)

entry(
    index = 101,
    label = "ONONO2 <=> NO2 + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.69e+23, 's^-1'), n=-2.43, Ea=(8148, 'cal/mol'), T0=(1, 'K'), Tmin=(700, 'K'), Tmax=(2000, 'K')),
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
    index = 102,
    label = "ONONO2 <=> NO + NO3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+21, 's^-1'), n=-1.76, Ea=(31535, 'cal/mol'), T0=(1, 'K'), Tmin=(700, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"""[Lin2014b]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
p. 265
T range: 700-2000 K
calculations done at the UCCSD(T)/CBS//UB3LYP/6-311þþG(3df,2p) level of theoty
Only High Pressure Limit rate was taken low limit and 1 atm rate are also available from the same source
Added as a training reaction to R_Recombination
""",
)

entry(
    index = 103,
    label = "N2H4 + NO2 <=> N2H3 + HONO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.23e+00, 'cm^3/(mol*s)'), n=3.56, Ea=(763, 'cal/mol'), T0=(1, 'K'), Tmin=(250, 'K'), Tmax=(2500, 'K')),
    shortDesc = u"""[Lin2014b]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
p. 265
T range: 250-2500 K
calculations done at the G2M(CC2)//B3LYP/6-311þþG(3df,2p) level of theoty
Also available from [Lin2014a], calculated at the CCSD(T)/CBS//CCSD level of theoty:
    kinetics = Arrhenius(A=(8.25e+01, 'cm^3/(mol*s)'), n=3.13, Ea=(8863, 'cal/mol'), T0=(1, 'K')),
Added as a training reaction to H_Abstraction
""",
)

entry(
    index = 104,
    label = "N2H4 + NO3 <=> N2H3 + HNO3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.28e+04, 'cm^3/(mol*s)'), n=2.53, Ea=(-2947, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Lin2014b]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
p. 269
T range: 300-3000 K
calculations done at the CCSD(T)//BHandHLYP/6-311þþG(3df,2p) level of theoty
Pressure independent at least up to 100 atm
A different rate for the same reaction is available from the same author (M.C. Lin) published at the same year: [Lin2014a]
But this [Lin2014a] rate is a factor of 3 lower at 1500 K:
    kinetics = Arrhenius(A=(6.20e+03, 'cm^3/(mol*s)'), n=2.64, Ea=(594, 'cal/mol'), T0=(1, 'K')),
[Lin2014a] reaction (6), p. 79
T range: 300-2000 K
calculations done at the CCSD(T)/CBS//CCSD level of theoty,
and the moment of inertia and harmonic vibrational frequencies were obtained by the CCSD/6-31G(d,p) level
Added as a training reaction to H_Abstraction
""",
)

entry(
    index = 105,
    label = "N2H4 + NO3 <=> HONO + N2H3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.46e+03, 'cm^3/(mol*s)'), n=2.51, Ea=(-7452, 'cal/mol'), T0=(1, 'K'), Tmin=(1000, 'K'), Tmax=(3000, 'K')),
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
A different rate for the same reaction is available from the same author (M.C. Lin) published at the same year: [Lin2014a]
But this [Lin2014a] rate is a O(2) lower at 1500 K:
    kinetics = Arrhenius(A=(2.04e+03, 'cm^3/(mol*s)'), n=2.59, Ea=(5612, 'cal/mol'), T0=(1, 'K')),
T range: 1000-2000 K
    kinetics = Arrhenius(A=(1.63e+11, 'cm^3/(mol*s)'), n=0.20, Ea=(2180, 'cal/mol'), T0=(1, 'K')),
T range: 300-1000 K
[Lin2014a] reaction (7), p. 79
calculations done at the CCSD(T)/CBS//CCSD level of theoty,
and the moment of inertia and harmonic vibrational frequencies were obtained by the CCSD/6-31G(d,p) level
""",
)

entry(
    index = 106,
    label = "N2H4 + N2O4 <=> HONO + NH2NHNO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.39e+02, 'cm^3/(mol*s)'), n=2.62, Ea=(13112, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(2500, 'K')),
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
    index = 107,
    label = "N2H4 + ONONO2 <=> HNO3 + NH2NHNO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.7e+14, 'cm^3/(mol*s)','+|-',6.1e+13), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K'), Tmin=(250, 'K'), Tmax=(2500, 'K')),
    shortDesc = u"""[Lin2014b]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
p. 272
T range: 250-2500 K
calculations done at the G2M(CC3)//B3LYP level of theoty
Reaction has a negligible T dependence in the explored range
uncertainty: +/- 13%
conformer-dup: The T-dependency of both cis-ONONO2 and trans-ONONO2 reacting with N2H4
in this pathway is negligable. The summation of the two constant rate coefficients is taken here.
""",
)

entry(
    index = 108,
    label = "NH2NHNO <=> N2H3 + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.24e+15, 's^-1'), n=-0.15, Ea=(35611, 'cal/mol'), T0=(1, 'K'), Tmin=(250, 'K'), Tmax=(1500, 'K')),
    shortDesc = u"""[Lin2014b]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
p. 274
T range: 250-1500 K
calculations done at the CCSD(T)/6-311þG(3df,2p) level of theoty
Added as a training reaction to R_Recombination
""",
)

entry(
    index = 109,
    label = "N2H3 + NO2 <=> N2H2 + HONO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.40e+55, 'cm^3/(mol*s)'), n=-16.7, Ea=(-14397, 'cal/mol'), T0=(1, 'K'), Tmin=(800, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Lin2014b]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
k5, p. 278
T range: 800-3000 K, P = 1 atm
calculations done at the CCSD(T)/6-311++G(3df,2p)//B3LYP/6-311++G(3df,2p) level of theoty
The Low T (300-800 K) rate is:
    kinetics = Arrhenius(A=(4.99e+46, 'cm^3/(mol*s)'), n=-11.8, Ea=(6055, 'cal/mol'), T0=(1, 'K')),
Added as a training reaction to Disproportionation
""",
)

entry(
    index = 110,
    label = "N2H3 + NO2 <=> N2H2 + HNO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.12e+07, 'cm^3/(mol*s)'), n=-0.2, Ea=(-2736, 'cal/mol'), T0=(1, 'K'), Tmin=(1500, 'K'), Tmax=(3000, 'K')),
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
    index = 111,
    label = "N2H3 + NO2 <=> N2H3O + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.14e+00, 'cm^3/(mol*s)'), n=2.8, Ea=(-8853, 'cal/mol'), T0=(1, 'K'), Tmin=(1000, 'K'), Tmax=(3000, 'K')),
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
    index = 112,
    label = "N2H3 + N2O4 <=> NH2NHNO2 + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.10e+10, 'cm^3/(mol*s)'), n=0.87, Ea=(11772, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
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
    index = 113,
    label = "N2H3 + N2O4 <=> N2H2 + HONO + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.55e+10, 'cm^3/(mol*s)'), n=0.74, Ea=(11707, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
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
    index = 114,
    label = "N2H3 + N2O4 <=> NH2NHONO + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.54e+13, 'cm^3/(mol*s)'), n=0.76, Ea=(15960, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
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
    index = 115,
    label = "N2H3 + N2O4 <=> N2H3O + N2O3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.69e+11, 'cm^3/(mol*s)'), n=0.87, Ea=(8047.4, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
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
    index = 116,
    label = "N2H3O <=> NH3 + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.86e+22, 's^-1'), n=-2.80, Ea=(79296, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
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
    index = 117,
    label = "N2H3O <=> NH2 + HNO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.12e+33, 's^-1'), n=-6.68, Ea=(35217, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Lin2014b]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
p. 284
T range: 300-3000 K, P = 1 atm
calculations done at the CCSD(T)/6-311þG(3df,2p)//CCSD/6-311þþG(d,p) level of theoty
Added as a training reaction to R_Additiom_MultipleBond
""",
)

entry(
    index = 118,
    label = "N2H3O <=> NH2NO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.57e+34, 's^-1'), n=-6.63, Ea=(44953, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Lin2014b]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
p. 284
T range: 300-3000 K, P = 1 atm
calculations done at the CCSD(T)/6-311þG(3df,2p)//CCSD/6-311þþG(d,p) level of theoty
Added as a training reaction to R_Additiom_MultipleBond
""",
)

entry(
    index = 119,
    label = "N2H2 + NO2 <=> HONO + NNH",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1.25e+00, 'cm^3/(mol*s)'), n=3.80, Ea=(10410, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2500, 'K')),
            Arrhenius(A=(2.33e-01, 'cm^3/(mol*s)'), n=3.50, Ea=(-129, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2500, 'K')),
        ],
    ),
    shortDesc = u"""[Lin2014b]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
p. 287
T range: 300-2500 K
calculations done at the CCSD(T)/6-311þþG(3df,2p)//B3LYP/6-311þþG(3df,2p) level of theoty
conformer-dup: rates summed for trans/cis-N2H2
""",
)

entry(
    index = 120,
    label = "N2H2 + N2O4 <=> HONO + NO2 + NNH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.79e+00, 'cm^3/(mol*s)'), n=3.10, Ea=(28787, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2500, 'K')),
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
    index = 121,
    label = "N2H2 + N2O4 <=> HONO + HNO2 + N2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.38e-02, 'cm^3/(mol*s)'), n=3.90, Ea=(13360, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2500, 'K')),
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
    index = 122,
    label = "N2H2 + OH <=> NNH + H2O",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(6.74e+03, 'cm^3/(mol*s)'), n=2.80, Ea=(-507, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2500, 'K')),
            Arrhenius(A=(7.65e+04, 'cm^3/(mol*s)'), n=2.25, Ea=(-2351, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2500, 'K')),
        ],
    ),
    shortDesc = u"""[Lin2014b]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
p. 292
T range: 300-2500 K
calculations done at the CCSD(T)/6-311++G(3df,2p)//B3LYP/6311++G(3df,2p) level of theory
conformer-dup: rates summed for trans/cis-N2H2
""",
)

entry(
    index = 123,
    label = "N2O4 + H2O <=> HONO + HNO3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.58e-02, 'cm^3/(mol*s)'), n=4.53, Ea=(29830, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(2500, 'K')),
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
    index = 124,
    label = "ONONO2 + H2O <=> HONO + HNO3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.93e+06, 'cm^3/(mol*s)'), n=1.88, Ea=(4064, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(2500, 'K')),
    shortDesc = u"""[Lin2012]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
p. 4469
T range: 200-2500 K
calculations done at the CCSD(T)/6-311++G(3df,2p)//B3LYP/6-311++G(3df,2p) level of theory
conformer-dup: Taken as the sum of the trans-HONO and cis-HONO rates (k2+k3, as reported)
""",
)

entry(
    index = 125,
    label = "CH3NO2 <=> CH3 + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.88e+24, 's^-1'), n=-2.35, Ea=(62398, 'cal/mol'), T0=(1, 'K'), Tmin=(500, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Lin2013a]""",
    longDesc =
u"""
Part of the "CH3NO2" subset
p. 7311
T range: 500-3000 K
calculations done at the UCCSD(T)/CBS//UB3LYP/6-311+G(3df,2p) level of theory
The high pressure limit rate is giving here. A 1 atm rate is also available from the same source.
Added as a training reaction to R_Recombination
""",
)

entry(
    index = 126,
    label = "CH3NO2 <=> CH3ONO",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(7.05e+54, 'cm^3/(mol*s)'), n=-10.94, Ea=(64344, 'cal/mol'), T0=(1, 'K'))),
    shortDesc = u"""[Lin2013a]""",
    longDesc =
u"""
Part of the "CH3NO2" subset
p. 7311
calculations done at the UCCSD(T)/CBS//UB3LYP/6-311+G(3df,2p) level of theory
""",
)

entry(
    index = 127,
    label = "CH3NO2 <=> CH3O + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.91e+19, 's^-1'), n=-1.84, Ea=(60809, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Lin2013a]""",
    longDesc =
u"""
Part of the "CH3NO2" subset
p. 7311
T range: 300-3000 K, valid for 10e-5 to 760 torr
calculations done at the UCCSD(T)/CBS//UB3LYP/6-311+G(3df,2p) level of theory
""",
)

entry(
    index = 128,
    label = "CH3NO2 <=> CH2O + HNO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.15e+17, 's^-1'), n=-0.75, Ea=(60014, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Lin2013a]""",
    longDesc =
u"""
Part of the "CH3NO2" subset
p. 7311
T range: 300-3000 K, valid for 10e-5 to 760 torr
calculations done at the UCCSD(T)/CBS//UB3LYP/6-311+G(3df,2p) level of theory
""",
)

entry(
    index = 129,
    label = "CH3ONO <=> CH3O + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.58e+23, 's^-1'), n=-2.18, Ea=(41930, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Lin2013a]""",
    longDesc =
u"""
Part of the "CH3NO2" subset
p. 7311
T range: 300-3000 K
calculations done at the UCCSD(T)/CBS//UB3LYP/6-311+G(3df,2p) level of theory
The high pressure limit rate is giving here. A 1 atm rate is akso available from the same source.
Added as a training reaction to R_Recombination
""",
)

entry(
    index = 130,
    label = "NH3 + NO <=> NH2 + HNO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.04e+07, 'cm^3/(mol*s)'), n=1.73, Ea=(56544, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(5000, 'K')),
    shortDesc = u"""[Lin1996a]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
k1 on p. 7519
T range: 300-5000 K
calculations done at the UMP2/6-311G-(d,p)//UMP2/6-311G(d,p) level of theory
Added as a training reaction to H_Abstraction
""",
)

entry(
    index = 131,
    label = "NH2 + NO <=> NNH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.43e+07, 'cm^3/(mol*s)'), n=1.40, Ea=(-1777, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2500, 'K')),
    shortDesc = u"""[Lin1999a]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
k1a
T range: 300-2500 K
""",
)

entry(
    index = 132,
    label = "NH2 + NO <=> N2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.20e+17, 'cm^3/(mol*s)'), n=-1.61, Ea=(298, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2500, 'K')),
    shortDesc = u"""[Lin1999a]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
k1b
T range: 300-2500 K
""",
)

entry(
    index = 133,
    label = "NH2 + NO <=> N2O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+13, 'cm^3/(mol*s)','*|/',2), n=0, Ea=(15700, 'cal/mol'), T0=(1, 'K'), Tmin=(1680, 'K'), Tmax=(2850, 'K')),
    shortDesc = u"""[Hanson1981]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
k2
Uncertainty: +100%, -70%
T range: 1680-2850 K
Shocktube measurement
""",
)

entry(
    index = 134,
    label = "NH + NO <=> N2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+14, 'cm^3/(mol*s)','*|/',3), n=-0.351, Ea=(-244, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Miller2011]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
calculated at the (CCSD(T) and QCISD(T)) and multireference CASPT2 and CAS + 1 + 2 + QC electronic structure calculations level
Also available from [Hanson1981], k3, Shock Tube, Uncertainty: +200%, -70%, T range: 1680-2850 K:
    kinetics = Arrhenius(A=(8e+13, 'cm^3/(mol*s)'), n=0, Ea=(29400, 'cal/mol'), T0=(1, 'K'), Tmin=(1680, 'K'), Tmax=(2850, 'K')),
""",
)

entry(
    index = 135,
    label = "NH + NO <=> N2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.7e+12, 'cm^3/(mol*s)'), n=-0.0721, Ea=(-512, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Miller2011]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
calculated at the (CCSD(T) and QCISD(T)) and multireference CASPT2 and CAS + 1 + 2 + QC electronic structure calculations level
Also availabvle from [Bozzelli1994]:
    kinetics = Arrhenius(A=(6.1e+13, 'cm^3/(mol*s)'), n=-0.50, Ea=(120, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(4000, 'K')),
T range: 300-4000 K, k2a, QRRK
""",
)

entry(
    index = 136,
    label = "NH2 + O2 <=> H2NO + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.6e+11, 'cm^3/(mol*s)'), n=0.4872, Ea=(29050, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Miller2011]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
calculated at the (CCSD(T) and QCISD(T)) and multireference CASPT2 and CAS + 1 + 2 + QC electronic structure calculations level
""",
)

entry(
    index = 137,
    label = "NH2 + O2 <=> HNO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e-02, 'cm^3/(mol*s)'), n=3.764, Ea=(18185, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Miller2011]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
calculated at the (CCSD(T) and QCISD(T)) and multireference CASPT2 and CAS + 1 + 2 + QC electronic structure calculations level
""",
)

entry(
    index = 138,
    label = "NH2OH <=> NH2 + OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(8.43e+43, 's^-1'), n=-1.31, Ea=(64087, 'cal/mol'), T0=(1, 'K'), Tmin=(450, 'K'), Tmax=(2500, 'K')),
        arrheniusLow = Arrhenius(A=(5.45e+37, 'cm^3/(mol*s)'), n=-5.96, Ea=(66790, 'cal/mol'), T0=(1, 'K'), Tmin=(450, 'K'), Tmax=(2500, 'K')),
        alpha=0.35, T3=(1e-30, 'K'), T1=(1e+30, 'K'), efficiencies={}),
    shortDesc = u"""[Klippenstein2009]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
Table 3, p. 10245
T range: 450-2500 K
calculated at the (CCSD(T) and CAS+1+2+QC level
Train!
""",
)

entry(
    index = 139,
    label = "NH2 + OH <=> NH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.84e+06, 'cm^3/(mol*s)'), n=1.97, Ea=(-2246, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2500, 'K')),
    shortDesc = u"""[Klippenstein2009]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
Table 3, p. 10245
T range: 300-2500 K
calculated at the (CCSD(T) and CAS+1+2+QC level
Train!
""",
)

entry(
    index = 140,
    label = "NH2 + OH <=> NH3 + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.72e+00, 'cm^3/(mol*s)','+|-',9.30e-01), n=3.50, Ea=(-203, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2500, 'K')),
    shortDesc = u"""[Klippenstein2009]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
Table 3, p. 10245
T range: 300-2500 K
calculated at the (CCSD(T) and CAS+1+2+QC level
Also available from [Klemm1990]:
    kinetics = Arrhenius(A=(9.39e+06, 'cm^3/(mol*s)'), n=1.94, Ea=(6461, 'cal/mol'), T0=(1, 'K')),
T range: 448-1790 K, Experimental, Uncertainty: 25%
Train!
""",
)

entry(
    index = 141,
    label = "NH2OH + OH <=> HNOH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.54e+04, 'cm^3/(mol*s)'), n=2.61, Ea=(-3537, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2500, 'K')),
    shortDesc = u"""[Klippenstein2009]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
Table 3, p. 10245
T range: 300-2500 K
calculated at the (CCSD(T) and CAS+1+2+QC level
Train!
""",
)

entry(
    index = 142,
    label = "NH2OH + OH <=> H2NO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.53e+05, 'cm^3/(mol*s)'), n=2.28, Ea=(-1296, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2500, 'K')),
    shortDesc = u"""[Klippenstein2009]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
Table 3, p. 10245
T range: 300-2500 K
calculated at the (CCSD(T) and CAS+1+2+QC level
Train!
""",
)

entry(
    index = 143,
    label = "NH2OH + NH2 <=> HNOH + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.08e-01, 'cm^3/(mol*s)'), n=4.00, Ea=(-97, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2500, 'K')),
    shortDesc = u"""[Klippenstein2009]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
Table 3, p. 10245
T range: 300-2500 K
calculated at the (CCSD(T) and CAS+1+2+QC level
Train!
""",
)

entry(
    index = 144,
    label = "NH2OH + NH2 <=> H2NO + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.45e+00, 'cm^3/(mol*s)'), n=3.42, Ea=(-1013, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2500, 'K')),
    shortDesc = u"""[Klippenstein2009]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
Table 3, p. 10245
T range: 300-2500 K
calculated at the (CCSD(T) and CAS+1+2+QC level
Train!
""",
)

entry(
    index = 145,
    label = "NH2OH + NH <=> HNOH + NH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.91e-03, 'cm^3/(mol*s)'), n=4.40, Ea=(1564, 'cal/mol'), T0=(1, 'K'), Tmin=(400, 'K'), Tmax=(2500, 'K')),
    shortDesc = u"""[Klippenstein2009]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
Table 3, p. 10245
T range: 400-2500 K
calculated at the (CCSD(T) and CAS+1+2+QC level
Train!
""",
)

entry(
    index = 146,
    label = "NH2OH + NH <=> H2NO + NH2",
    degeneracy = 1,
   kinetics = Arrhenius(A=(1.46e-03, 'cm^3/(mol*s)'), n=4.60, Ea=(2424, 'cal/mol'), T0=(1, 'K'), Tmin=(400, 'K'), Tmax=(2500, 'K')),
    shortDesc = u"""[Klippenstein2009]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
Table 3, p. 10245
T range: 400-2500 K
calculated at the (CCSD(T) and CAS+1+2+QC level
Train!
""",
)

entry(
    index = 147,
    label = "NH + OH <=> H2O + N",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.59e+07, 'cm^6/(mol^2*s)'), n=1.737, Ea=(-576, 'cal/mol'), T0 = (1, 'K'), Tmin=(200, 'K'), Tmax=(2500, 'K'))),
    shortDesc = u"""[Klippenstein2009]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
Table 3, p. 10245
T range: 200-2500 K
calculated at the (CCSD(T) and CAS+1+2+QC level
Train!
""",
)

entry(
    index = 148,
    label = "NH + OH <=> HNO + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(3.25e+14, 'cm^6/(mol^2*s)'), n=-0.376, Ea=(-46, 'cal/mol'), T0 = (1, 'K'), Tmin=(200, 'K'), Tmax=(2500, 'K'))),
    shortDesc = u"""[Klippenstein2009]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
Table 3, p. 10245
T range: 200-2500 K
calculated at the (CCSD(T) and CAS+1+2+QC level
""",
)

entry(
    index = 149,
    label = "NH + NH <=> N2H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=-0.036, Ea=(-161, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(2500, 'K')),
    shortDesc = u"""[Klippenstein2009]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
Table 3, p. 10245
T range: 200-2500 K, high pressure limit
calculated at the (CCSD(T) and CAS+1+2+QC level
Train!
""",
)

entry(
    index = 150,
    label = "NH + NH <=> NH2 + N",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.66e-01, 'cm^3/(mol*s)'), n=3.88, Ea=(342, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2500, 'K')),
    shortDesc = u"""[Klippenstein2009]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
Table 3, p. 10245
T range: 300-2500 K
calculated at the (CCSD(T) and CAS+1+2+QC level
Train!
""",
)

entry(
    index = 151,
    label = "NH2 + NH <=> N2H2 + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(4.26e+14, 'cm^6/(mol^2*s)'), n=-0.272, Ea=(-78, 'cal/mol'), T0 = (1, 'K'), Tmin=(200, 'K'), Tmax=(2500, 'K'))),
    shortDesc = u"""[Klippenstein2009]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
Table 3, p. 10245
T range: 200-2500 K
calculated at the (CCSD(T) and CAS+1+2+QC level
Also available from [Hanson1990a]:
    kinetics = Arrhenius(A=(1.50e+15, 'cm^3/(mol*s)'), n=-0.5, Ea=(0, 'cal/mol'), T0=(1, 'K')),
R11 in Table 1, p. 521, T range: 2200-2800 K, Shock Tube
""",
)

entry(
    index = 152,
    label = "NH2 + NH <=> NH3 + N",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.58e+03, 'cm^3/(mol*s)'), n=2.46, Ea=(107, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(2500, 'K')),
    shortDesc = u"""[Klippenstein2009]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
Table 3, p. 10245
T range: 200-2500 K
calculated at the (CCSD(T) and CAS+1+2+QC level
Train!
""",
)

entry(
    index = 153,
    label = "NH2 + NH2 <=> N2H2 + H2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.74e+08, 'cm^6/(mol^2*s)'), n=1.02, Ea=(11784, 'cal/mol'), T0 = (1, 'K'), Tmin=(500, 'K'), Tmax=(2500, 'K'))),
    shortDesc = u"""[Klippenstein2009]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
Table 3, p. 10245
T range: 500-2500 K
calculated at the (CCSD(T) and CAS+1+2+QC level
""",
)

entry(
    index = 154,
    label = "NH2 + NH2 <=> H2NN + H2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(7.17e+04, 'cm^6/(mol^2*s)'), n=1.88, Ea=(8803, 'cal/mol'), T0 = (1, 'K'), Tmin=(500, 'K'), Tmax=(2500, 'K'))),
    shortDesc = u"""[Klippenstein2009]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
Table 3, p. 10245
T range: 500-2500 K
calculated at the (CCSD(T) and CAS+1+2+QC level
""",
)

entry(
    index = 155,
    label = "NH2 + NH2 <=> NH3 + NH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.64e+00, 'cm^3/(mol*s)'), n=3.53, Ea=(552, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2500, 'K')),
    shortDesc = u"""[Klippenstein2009]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
Table 3, p. 10245
T range: 300-2500 K
calculated at the (CCSD(T) and CAS+1+2+QC level
Also available from [Hanson1990a]:
    kinetics = Arrhenius(A=(5.00e+13, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
R12 in Table 1, p. 521, T range: 2200-2800 K, Shock Tube
Also available from [Klippenstein2009] in reverse direction:
    kinetics = Arrhenius(A=(5.14e+01, 'cm^3/(mol*s)'), n=3.41, Ea=(14606, 'cal/mol'), T0=(1, 'K')),
Train both!!!
""",
)

entry(
    index = 157,
    label = "NH2 + H2 <=> NH3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.23e+05, 'cm^3/(mol*s)'), n=2.23, Ea=(7168, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(5000, 'K')),
    shortDesc = u"""[Lin1999b]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
k1_theo on p. 229
T range: 300-5000 K
calculations done at the G2M//B3LYP/6-311G(d,p) level of theory
Also available (shock tube) from [Klemm1985]
Added as a training reaction to H_Abstraction
""",
)

entry(
    index = 158,
    label = "NH2 + CH4 <=> NH3 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.36e+04, 'cm^3/(mol*s)'), n=2.87, Ea=(10691, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(5000, 'K')),
    shortDesc = u"""[Lin1999b]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
k2 on p. 232
T range: 300-5000 K
calculations done at the G2M//B3LYP/6-311G(d,p) level of theory
Added as a training reaction to H_Abstraction
""",
)

entry(
    index = 159,
    label = "NH2 + H2O <=> NH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.62e+13, 'cm^3/(mol*s)'), n=0, Ea=(16846, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(5000, 'K')),
    shortDesc = u"""[Lin1999b]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
k4 on p. 233
T range: 300-5000 K
calculations done at the G2M//B3LYP/6-311G(d,p) level of theory
A lower and upper rate limits were given. Here an average rate was taken.
Fitted to a 2 parameter Arrhenius with a coefficient of determination of 0.9943
Added as a training reaction to H_Abstraction
""",
)

entry(
    index = 160,
    label = "NH3 + NO2 <=> NH2 + HNO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.91e+00, 'cm^3/(mol*s)'), n=3.41, Ea=(29880, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(5000, 'K')),
    shortDesc = u"""[Lin1996a]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
k2a on p. 7524
T range: 300-5000 K
calculations done at the UMP2/6-311G-(d,p)//UMP2/6-311G(d,p) level of theory
""",
)

entry(
    index = 161,
    label = "NH3 + NO2 <=> NH2 + HONO",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(2.36e+01, 'cm^3/(mol*s)'), n=3.41, Ea=(22290, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(5000, 'K')),
            Arrhenius(A=(1.88e+01, 'cm^3/(mol*s)'), n=3.52, Ea=(32598, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(5000, 'K')),
        ],
    ),
    shortDesc = u"""[Lin1996a]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
k2b, k2c on p. 7523-7524
T range: 300-5000 K
calculations done at the UMP2/6-311G-(d,p)//UMP2/6-311G(d,p) level of theory
NH3+NO2 can give (2a) NH2 + HNO2 (see above), (2b) NH2 + cis-HONO, (2c) NH2 + trans-HONO.
k2c has tunneling correction
conformer-dup: cis/trans-HONO
""",
)

entry(
    index = 162,
    label = "NH3 + NO3 <=> HNO3 + NH2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 10, 100, 760, 7600, 76000], 'torr'),
        arrhenius = [
            Arrhenius(A=(2.57e+00, 'cm^3/(mol*s)'), n=3.61, Ea=(964, 'cal/mol'), T0 = (1, 'K'), Tmin=(200, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(5.67e+00, 'cm^3/(mol*s)'), n=3.53, Ea=(1598, 'cal/mol'), T0 = (1, 'K'), Tmin=(200, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(4.61e+00, 'cm^3/(mol*s)'), n=3.56, Ea=(1691, 'cal/mol'), T0 = (1, 'K'), Tmin=(200, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(4.06e+00, 'cm^3/(mol*s)'), n=3.57, Ea=(1689, 'cal/mol'), T0 = (1, 'K'), Tmin=(200, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(3.85e+00, 'cm^3/(mol*s)'), n=3.58, Ea=(1679, 'cal/mol'), T0 = (1, 'K'), Tmin=(200, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(3.63e+00, 'cm^3/(mol*s)'), n=3.59, Ea=(1669, 'cal/mol'), T0 = (1, 'K'), Tmin=(200, 'K'), Tmax=(3000, 'K')),
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
    index = 163,
    label = "HNO3 + NH2 <=> H2NO + HONO",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 10, 100, 760, 7600, 76000], 'torr'),
        arrhenius = [
            Arrhenius(A=(8.91e+04, 'cm^3/(mol*s)'), n=2.00, Ea=(24641, 'cal/mol'), T0 = (1, 'K'), Tmin=(200, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(1.36e+07, 'cm^3/(mol*s)'), n=1.40, Ea=(26390, 'cal/mol'), T0 = (1, 'K'), Tmin=(200, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(5.09e+08, 'cm^3/(mol*s)'), n=0.99, Ea=(28353, 'cal/mol'), T0 = (1, 'K'), Tmin=(200, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(1.73e+08, 'cm^3/(mol*s)'), n=1.17, Ea=(29562, 'cal/mol'), T0 = (1, 'K'), Tmin=(200, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(7.17e+04, 'cm^3/(mol*s)'), n=2.19, Ea=(29870, 'cal/mol'), T0 = (1, 'K'), Tmin=(200, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(3.46e-02, 'cm^3/(mol*s)'), n=4.04, Ea=(28946, 'cal/mol'), T0 = (1, 'K'), Tmin=(200, 'K'), Tmax=(3000, 'K')),
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
    index = 164,
    label = "NH2 + NO2 <=> N2O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.60e+18, 'cm^3/(mol*s)'), n=-2.191, Ea=(455, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"""[Marshall2013]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
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
    index = 165,
    label = "NH2 + NO2 <=> H2NO + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.09e+11, 'cm^3/(mol*s)'), n=0.0321, Ea=(-1512, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"""[Marshall2013]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
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
    index = 166,
    label = "NH2 + NO2 <=> HNNO + OH",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(3.35e+14, 'cm^3/(mol*s)'), n=-0.926, Ea=(5477, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2000, 'K')),
            Arrhenius(A=(2.38e+12, 'cm^3/(mol*s)'), n=-0.107, Ea=(11238, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2000, 'K')),
        ],
    ),
    shortDesc = u"""[Marshall2013]""",
    longDesc =
u"""
Part of the "Thermal de-NOx" mechanism
k1c + k1d 3 on p. 9019
T range: 300-2000 K
calculations done at the RQCISD(T)/CBS(QZ,5Z)//B3LYP/6-311++G(d,p) level of theory
+UCCSD(T)/cc-pVTZ rovibrational analysis with UCCSD-(T)/CBS(aug-cc-pVQZ′,aug-cc-pV5Z′) energies,
CCSDT(Q)/cc-pVDZ higher order corrections, CCSD(T,full)/CBS-(TZ,QZ) core−valence corrections,
CI/aug-cc-pcVTZ relativistic corrections, HF/cc-pVTZ diagonal Born−Oppenheimer corrections,
and B3LYP/6-311++G(d,p) anharmonic ZPE corrections
conformer-dup: cis/trans-HNNO
""",
)

entry(
    index = 167,
    label = "NO2 <=> NO + O",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.98e+14, 's^-1'), n=0, Ea=(71700, 'cal/mol'), T0=(1, 'K'), Tmin=(1350, 'K'), Tmax=(2100, 'K')),
        arrheniusLow = Arrhenius(A=(3.98e+15, 'cm^3/(mol*s)'), n=0, Ea=(60000, 'cal/mol'), T0=(1, 'K'), Tmin=(1350, 'K'), Tmax=(2100, 'K')),
        alpha=1, T3=(1e-30, 'K'), T1=(1e+30, 'K'), efficiencies={}),
    shortDesc = u"""[Hanson1997]""",
    longDesc =
u"""
Part of the "NO2 decomposition" subset
T range: 1350-2100 K
Shock tube measurement
Added as a training reaction to Birad_R_Recombination
""",
)

entry(
    index = 168,
    label = "NO2 + NO2 <=> NO + NO + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.51e+12, 'cm^3/(mol*s)'), n=0, Ea=(27600, 'cal/mol'), T0=(1, 'K'), Tmin=(625, 'K'), Tmax=(2100, 'K')),
    shortDesc = u"""[Lin1998b]""",
    longDesc =
u"""
Part of the "NO2 decomposition" subset
T range: 625-2100 K
Shock tube measurement by [Hanson1997], and rate improvement by [Lin1998b]
""",
)

entry(
    index = 169,
    label = "NO2 + NO2 <=> NO3 + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.00e+13, 'cm^3/(mol*s)'), n=0, Ea=(25800, 'cal/mol'), T0=(1, 'K'), Tmin=(1350, 'K'), Tmax=(2100, 'K')),
    shortDesc = u"""[Hanson1997]""",
    longDesc =
u"""
Part of the "NO2 decomposition" subset
T range: 1350-2100 K
Shock tube measurement
""",
)

entry(
    index = 170,
    label = "HONO + NO2 <=> HNO3 + NO",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(3.03e+02, 'cm^3/(mol*s)'), n=3.33, Ea=(32644, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(2.00e+02, 'cm^3/(mol*s)'), n=3.28, Ea=(30692, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
        ],
    ),
    shortDesc = u"""[Lin2000b]""",
    longDesc =
u"""
Part of the "NO2 decomposition" subset
T range: 300-3000 K
calculations done at the B3LYP/6-311G-(d,p)//B3LYP/6-311G(d,p) level of theory
conformer-dup: rate are for both cis-HONO and trans-HONO reactants
Also available from [Lin1998b] (altough cited as "unpublished work"):
    kinetics = Arrhenius(A=(2.00e+11, 'cm^3/(mol*s)'), n=0, Ea=(32700, 'cal/mol'), T0=(1, 'K')),
""",
)

entry(
    index = 171,
    label = "HNO + NO2 <=> HONO + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.42e+04, 'cm^3/(mol*s)'), n=2.64, Ea=(4042, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(5000, 'K')),
    shortDesc = u"""[Lin1998f]""",
    longDesc =
u"""
Part of the "NO2 decomposition" subset
T range: 300-5000 K
calculations done at the B3LYP/6-311G-(d,p)//B3LYP/6-311G(d,p) level of theory
This route produces the cis-HONO, two other routs that produce the trans-HONO product exist, yet their rates are much smaller
""",
)

entry(
    index = 172,
    label = "N2O + H <=> N2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.4e+07, 'cm^3/(mol*s)'), n=1.835, Ea=(13492, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Miller2011]""",
    longDesc =
u"""
Part of the "NO2 decomposition" subset
calculated at the (CCSD(T) and QCISD(T)) and multireference CASPT2 and CAS + 1 + 2 + QC electronic structure calculations level
Also available from [Herron1991]:
    kinetics = Arrhenius(A=(9.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(15100, 'cal/mol'), T0=(1, 'K'), Tmin=(700, 'K'), Tmax=(2500, 'K')),
T range: 700-2500 K, Review and reccomendation, p. 660, 14,4
""",
)

entry(
    index = 173,
    label = "N2O + CO <=> N2 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(20330, 'cal/mol'), T0=(1, 'K'), Tmin=(700, 'K'), Tmax=(2500, 'K')),
    shortDesc = u"""[Herron1991]""",
    longDesc =
u"""
Part of the "NO2 decomposition" subset
T range: 700-2500 K
Review and reccomendation, p. 662, 14,8
""",
)

entry(
    index = 174,
    label = "NO2 + HCO <=> CO + HONO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.24e+23, 'cm^3/(mol*s)'), n=-3.29, Ea=(2355, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"""[Lin1990]""",
    longDesc =
u"""
Part of the "NO2 decomposition" subset
T range: 300-2000 K
k2, p. 471
""",
)

entry(
    index = 175,
    label = "HONO + H <=> H2 + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.01e+08, 'cm^3/(mol*s)'), n=1.55, Ea=(6614, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3500, 'K')),
    shortDesc = u"""[Lin1997a]""",
    longDesc =
u"""
Part of the "NO2 decomposition" subset
T range: 300-3500 K
G2 and BAC-MP4
Added as a training reaction to H_Abstraction
""",
)

entry(
    index = 176,
    label = "NO <=> N + O",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(9.6e+14, 'cm^3/(mol*s)'), n=0, Ea=(148000, 'cal/mol'), T0 = (1, 'K'), Tmin=(2400, 'K'), Tmax=(6200, 'K')),
        efficiencies={'N#N': 1.5, 'O=C=O': 2.5}),
    shortDesc = u"""[Herron1991]""",
    longDesc =
u"""
Part of the "NOx" subset
T range: 2400-6200 K
Shock tube measurement by Thielen and Roth 1984, as reported by [Herron1991]
This reaction is not expected to be important except at the highest temperatures
""",
)

entry(
    index = 177,
    label = "NO2 + HCO <=> H + CO2 + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.39e+15, 'cm^3/(mol*s)'), n=-0.75, Ea=(1930, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"""[Lin1990]""",
    longDesc =
u"""
Part of the "NOx" subset
T range: 300-2000 K
k2, p. 471
""",
)

entry(
    index = 178,
    label = "HNO + H <=> NO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.46e+11, 'cm^3/(mol*s)'), n=0.720, Ea=(655, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Page1992]""",
    longDesc =
u"""
Part of the "NOx" subset
T range: 200-3000 K
calculations done at the CASSCF//(CASSCF and CISD) levels of theory
Also available (in reverse direction) from Tando and Asaba 1976, as reported by [Herron1991] in T range: 2020-3250 K:
    kinetics = Arrhenius(A=(1.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(56500, 'cal/mol'), T0=(1, 'K')),
Added as a training reaction to H_Abstraction
""",
)

entry(
    index = 179,
    label = "HONO + H <=> OH + HNO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.64e+10, 'cm^3/(mol*s)'), n=0.86, Ea=(4970, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3500, 'K')),
    shortDesc = u"""[Lin1997a]""",
    longDesc =
u"""
Part of the "NOx" subset
T range: 300-3500 K
G2 and BAC-MP4
""",
)

entry(
    index = 180,
    label = "HONO + H <=> H2O + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.13e+06, 'cm^3/(mol*s)'), n=1.89, Ea=(3847, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3500, 'K')),
    shortDesc = u"""[Lin1997a]""",
    longDesc =
u"""
Part of the "NOx" subset
T range: 300-3500 K
G2 and BAC-MP4
""",
)

entry(
    index = 181,
    label = "HONO + HONO <=> H2O + NO2 + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.49e-01, 'cm^3/(mol*s)'), n=3.64, Ea=(12140, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(5000, 'K')),
    shortDesc = u"""[Lin1998c]""",
    longDesc =
u"""
Part of the "NOx" subset
T range: 300-5000 K
G2M
""",
)

entry(
    index = 182,
    label = "HNO3 + H <=> H2 + NO3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.56e+08, 'cm^3/(mol*s)'), n=1.53, Ea=(16400, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Lin1997b]""",
    longDesc =
u"""
Part of the "NOx" subset
T range: 300-3000 K
CTST
Added as a training reaction to H_Abstraction
""",
)

entry(
    index = 183,
    label = "HNO3 + H <=> OH + HONO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.82e+05, 'cm^3/(mol*s)'), n=2.30, Ea=(6977, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Lin1997b]""",
    longDesc =
u"""
Part of the "NOx" subset
T range: 300-3000 K
The product is the cis-HONO conformer
RRKM
""",
)

entry(
    index = 184,
    label = "HNO3 + H <=> H2O + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.08e+01, 'cm^3/(mol*s)'), n=3.29, Ea=(6286, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Lin1997b]""",
    longDesc =
u"""
Part of the "NOx" subset
T range: 300-3000 K
RRKM
""",
)

entry(
    index = 185,
    label = "HNNO2 <=> N2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.43e+12, 's^-1'), n=0, Ea=(32220, 'cal/mol'), T0=(1, 'K'), Tmin=(500, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"""[Lin1998d]""",
    longDesc =
u"""
Part of the "NOx" subset
T range: 500-2000 K
calculations done at the B3LYP/6-311D(d,p)//B3LYP/6-311D(d,p) level of theory
k1b_inf, p. 8892
k_inf was taken. the study also reports k_200atm and k_1atm.
""",
)

entry(
    index = 186,
    label = "NH + NO2 <=> HNNO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.42e+16, 'cm^3/(mol*s)'), n=-0.75, Ea=(1226, 'cal/mol'), T0=(1, 'K'), Tmin=(500, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Lin1998d]""",
    longDesc =
u"""
Part of the "NOx" subset
T range: 500-3000 K
calculations done at the B3LYP/6-311D(d,p)//B3LYP/6-311D(d,p) level of theory
k3a, p. 8893
No stabilization at low pressures, only K3a_inf is given (k3a_low = 0)
reverse rate also available from the same study (k1a)
Added as a training reaction to Birad_R_Recombination
""",
)

entry(
    index = 187,
    label = "NH + NO2 <=> N2O + OH",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(2.08e+13, 'cm^6/(mol^2*s)'), n=-0.49, Ea=(715, 'cal/mol'), T0 = (1, 'K'), Tmin=(500, 'K'), Tmax=(3000, 'K'))),
    shortDesc = u"""[Lin1998d]""",
    longDesc =
u"""
Part of the "NOx" subset
T range: 500-3000 K
calculations done at the B3LYP/6-311D(d,p)//B3LYP/6-311D(d,p) level of theory
k3b, p. 8893
No production of N2O at the high pressure limit (k3b_inf = 0)
""",
)

entry(
    index = 188,
    label = "NH + NO2 <=> HNO + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.25e+06, 'cm^3/(mol*s)'), n=1.96, Ea=(2345, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Lin1998d]""",
    longDesc =
u"""
Part of the "NOx" subset
T range: 300-3000 K
calculations done at the B3LYP/6-311D(d,p)//B3LYP/6-311D(d,p) level of theory
k4, p. 8894
""",
)

entry(
    index = 189,
    label = "HCO + HNO <=> CH2O + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.83e-01, 'cm^3/(mol*s)'), n=3.84, Ea=(115, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Lin2004]""",
    longDesc =
u"""
Part of the "NOx" subset
T range: 200-3000 K
calculations done at the G2M//BH&HLYP/6-311G(d, p) level of theory
k1, p. 211
Added as a training reaction to H_Abstraction
""",
)

entry(
    index = 190,
    label = "HCO + HNO <=> H2NO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.90e+01, 'cm^3/(mol*s)'), n=3.27, Ea=(1755, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Lin2004]""",
    longDesc =
u"""
Part of the "NOx" subset
T range: 200-3000 K
calculations done at the G2M//BH&HLYP/6-311G(d, p) level of theory
k2, p. 211
""",
)

entry(
    index = 191,
    label = "HCO + HNO <=> HNOH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.31e+13, 'cm^3/(mol*s)'), n=-0.205, Ea=(3647, 'cal/mol'), T0=(1, 'K'), Tmin=(1000, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Lin2004]""",
    longDesc =
u"""
Part of the "NOx" subset
T range: 1000-3000 K
calculations done at the G2M//BH&HLYP/6-311G(d, p) level of theory
k4(HNOH+CO), p. 213
The Low T (200-400 K) rate is:
    kinetics = Arrhenius(A=(1.04e-07, 'cm^3/(mol*s)'), n=6.23, Ea=(-3291, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(400, 'K')),

The Low T (400-1000 K) rate is:
    kinetics = Arrhenius(A=(2.16e+08, 'cm^3/(mol*s)'), n=1.19, Ea=(914, 'cal/mol'), T0=(1, 'K'), Tmin=(400, 'K'), Tmax=(1000, 'K')),
""",
)

entry(
    index = 192,
    label = "HCO + NO <=> HNO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.04e+08, 'cm^3/(mol*s)'), n=1.47, Ea=(-1765, 'cal/mol'), T0=(1, 'K'), Tmin=(500, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Lin2005c]""",
    longDesc =
u"""
Part of the "NOx" subset
T range: 500-3000 K
calculations done at the G2M(CC5)//B3LYP/6-311G(d, p) level of theory
k(HNO+CO), p. 234308-10
The Low T (200-500 K) rate is:
    kinetics = Arrhenius(A=(1.85e+12, 'cm^3/(mol*s)'), n=0.10, Ea=(-481, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(500, 'K')),
""",
)

entry(
    index = 193,
    label = "NH3 + HNO3 <=> H2NNO2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.1e-01, 'cm^3/(mol*s)'), n=3.47, Ea=(43060, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Lin1998e]""",
    longDesc =
u"""
Part of the "NOx" subset
T range: 300-3000 K
calculations done at the G2M//PMP4/6-311G(d, p) level of theory
""",
)

entry(
    index = 194,
    label = "NH3 + HNO3 <=> H2NONO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.32e+01, 'cm^3/(mol*s)'), n=3.50, Ea=(44930, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Lin1998e]""",
    longDesc =
u"""
Part of the "NOx" subset
T range: 300-3000 K
calculations done at the G2M//PMP4/6-311G(d, p) level of theory
""",
)

entry(
    index = 195,
    label = "CH2O + NO2 <=> CHO + HONO",
    degeneracy = 3,
    kinetics = Arrhenius(A=(1.42e-07, 'cm^3/(mol*s)'), n=5.64, Ea=(9221, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Lin2003c]""",
    longDesc =
u"""
Part of the "NOx" subset
T range: 200-3000 K
calculations done at the G2M//B3LYP/6−311+G(d,p) and G2M//MPW1PW91/6−311+G(3df,2p) levels of theory
* There are two other pathways for the formation of these products, this is the fastest one. k_tot was also given in the paper.
Added as a training reaction to H_Abstraction
""",
)

entry(
    index = 196,
    label = "CH2O + NO2 <=> CHO + HNO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.07e-01, 'cm^3/(mol*s)'), n=4.22, Ea=(19852, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Lin2003c]""",
    longDesc =
u"""
Part of the "NOx" subset
T range: 200-3000 K
calculations done at the G2M//B3LYP/6−311+G(d,p) and G2M//MPW1PW91/6−311+G(3df,2p) levels of theory
""",
)

entry(
    index = 197,
    label = "HONO + O3 <=> HNO3 + O2",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1.53e-01, 'cm^3/(mol*s)'), n=3.22, Ea=(21539, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(7.07e-01, 'cm^3/(mol*s)'), n=3.41, Ea=(13127, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
        ],
    ),
    shortDesc = u"""[Lin2000b]""",
    longDesc =
u"""
Part of the "NOx" subset
T range: 300-3000 K
calculations done at the B3LYP/6-311G-(d,p)//B3LYP/6-311G(d,p) level of theory
conformer-dup: rate are for both cis-HONO and trans-HONO reactants
""",
)

entry(
    index = 198,
    label = "O3 <=> O2 + O",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.25e+19, 'cm^3/(mol*s)'), n=-1.25, Ea=(24367, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K'))),
    shortDesc = u"""[Hindelang1993]""",
    longDesc =
u"""
Part of the "NOx" subset
T range: 300-3000 K
Shock Tube
""",
)

entry(
    index = 199,
    label = "HONO + NH3 <=> H2NNO + H2O",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(9.64e-04, 'cm^3/(mol*s)'), n=4.24, Ea=(29013, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(1.08e-03, 'cm^3/(mol*s)'), n=4.26, Ea=(30206, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
        ],
    ),
    shortDesc = u"""[Lin2000c]""",
    longDesc =
u"""
Part of the "NOx" subset
T range: 300-3000 K
calculations done at the QCISD(T)/6-311G(d,p)//B3LYP/6-311G(d,p) level of theory
conformer-dup: rate are for both cis-HONO and trans-HONO reactants
""",
)

entry(
    index = 200,
    label = "HNO3 + OH <=> H2O + NO3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.73e+00, 'cm^3/(mol*s)'), n=3.50, Ea=(-1667, 'cal/mol'), T0=(1, 'K'), Tmin=(750, 'K'), Tmax=(1500, 'K')),
    shortDesc = u"""[Lin2001]""",
    longDesc =
u"""
Part of the "NOx" subset
kNO3 on p. 4530
T range: 750-1500 K
calculations done at the B3LYP/6-311G(d,p)//B3LYP/6-311G(d,p) level of theory
Added as a training reaction to H_Abstraction
""",
)

entry(
    index = 201,
    label = "OH + NO2 <=> HNO3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.85e+15, 'cm^3/(mol*s)'), n=-0.82, Ea=(-42, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(2000, 'K')),
        arrheniusLow = Arrhenius(A=(1.20e+42, 'cm^6/(mol^2*s)'), n=-8.8, Ea=(3118, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(2000, 'K')),
        alpha=1, T3=(1e-30, 'K'), T1=(1e+30, 'K'), efficiencies={}),
    shortDesc = u"""[Lin2003b]""",
    longDesc =
u"""
Part of the "NOx" subset
k_inf_a on p. 44
T range: 200-2000 K
Also available from [Lin1998a] at the B3LYP/6-311G(d,p)//B3LYP/6-311G(d,p) level of theory, T range: 300-2000 K (k_inf_a on p. 44):
    kinetics = Arrhenius(A=(1.45e+13, 'cm^3/(mol*s)'), n=0, Ea=(-477, 'cal/mol'), T0=(1, 'K')),
""",
)

entry(
    index = 202,
    label = "OH + NO2 <=> HOONO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.32e-06, 'cm^3/(mol*s)'), n=-0.24, Ea=(-200, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(2000, 'K')),
        arrheniusLow = Arrhenius(A=(1.14e+50, 'cm^6/(mol^2*s)'), n=-12.3, Ea=(5137, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(2000, 'K')),
        alpha=1, T3=(1e-30, 'K'), T1=(1e+30, 'K'), efficiencies={}),
    shortDesc = u"""[Lin2003b]""",
    longDesc =
u"""
Part of the "NOx" subset
k_inf_a on p. 44
T range: 200-2000 K
""",
)

entry(
    index = 203,
    label = "OH + NO2 <=> HO2 + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.00e+06, 'cm^3/(mol*s)'), n=2.00, Ea=(3000, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"""[Lin1998a]""",
    longDesc =
u"""
Part of the "NOx" subset
Table 3 on p. 46
T range: 300-2000 K
calculations done at the B3LYP/6-311G(d,p)//B3LYP/6-311G(d,p) level of theory
The 3-parameter Arrhenius parametes were fitted from the data in the table using Excel.
Probably not the best fit... but deviated only by ~5% above 1000 K (larger deviation at T < 1000 K)
""",
)

entry(
    index = 204,
    label = "NO2 + CO <=> NO + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.91e+13, 'cm^3/(mol*s)'), n=0, Ea=(67200, 'cal/mol'), T0=(1, 'K'), Tmin=(500, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"""[Palmer1977]""",
    longDesc =
u"""
Part of the "NOx" subset
T range: 500-2000 K
Shock tube measurement
""",
)

entry(
    index = 205,
    label = "NH + O2 <=> HNO + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.61e+05, 'cm^3/(mol*s)'), n=2.0, Ea=(6500, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3300, 'K')),
    shortDesc = u"""[Miller1992]""",
    longDesc =
u"""
Part of the "NOx" subset
T range: 300-3300 K
k3
BAC-MP4
""",
)

entry(
    index = 206,
    label = "NH + O2 <=> NO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.28e+06, 'cm^3/(mol*s)'), n=1.5, Ea=(100, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3300, 'K')),
    shortDesc = u"""[Miller1992]""",
    longDesc =
u"""
Part of the "NOx" subset
T range: 300-3300 K
k4
BAC-MP4
""",
)

entry(
    index = 207,
    label = "N2O5 + H2O <=> HNO3 + HNO3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.73e+07, 'cm^3/(mol*s)'), n=3.354, Ea=(15700, 'cal/mol'), T0=(298, 'K'), Tmin=(180, 'K'), Tmax=(1800, 'K')),
    shortDesc = u"""[Marshall2014]""",
    longDesc =
u"""
Part of the "NOx" subset
p. 11413
T range: 180-1800 K
calculations done at the CCSD(T)-F12a/cc-pVTZ-F12//M06-2X/MG3S level of theory
""",
)

entry(
    index = 209,
    label = "CN + OH <=> NCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.00e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K'), Tmin=(1250, 'K'), Tmax=(1863, 'K')),
    shortDesc = u"""[Hanson1996]""",
    longDesc =
u"""
Part of the "HCN" subset
T range: 1250-1863 K
k1 Table 1, p. 249
Shock Tube
""",
)

entry(
    index = 210,
    label = "HCN + O <=> NH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.4e+08, 'cm^3/(mol*s)'), n=1.21, Ea=(7650, 'cal/mol'), T0=(1, 'K'), Tmin=(500, 'K'), Tmax=(2500, 'K')),
    shortDesc = u"""[Herron1991]""",
    longDesc =
u"""
Part of the "HCN" subset
T range: 500-2500 K
Review and reccomendation, p. 653, 13,3(b)
""",
)

entry(
    index = 212,
    label = "HCN + H <=> H2 + CN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+14, 'cm^3/(mol*s)'), n=0, Ea=(24600, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(1000, 'K')),
    shortDesc = u"""[Herron1991]""",
    longDesc =
u"""
Part of the "HCN" subset
T range: 300-1000 K
Reviewed by Bailch et al. 1981, as reported by [Herron1991] p. 654
Added as a training reaction to H_Abstraction
""",
)

entry(
    index = 213,
    label = "HCN + OH <=> H2O + CN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.2e+07, 'cm^3/(mol*s)'), n=1.5, Ea=(7724, 'cal/mol'), T0=(1, 'K'), Tmin=(298, 'K'), Tmax=(2840, 'K')),
    shortDesc = u"""[Herron1991]""",
    longDesc =
u"""
Part of the "HCN" subset
T range: 298-2840 K
Review and reccomendation, p. 656, 13,5(a)
Added as a training reaction to H_Abstraction
""",
)

entry(
    index = 214,
    label = "HCN + OH <=> H + OHCN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.2e+04, 'cm^3/(mol*s)'), n=2.45, Ea=(12120, 'cal/mol'), T0=(1, 'K'), Tmin=(298, 'K'), Tmax=(2840, 'K')),
    shortDesc = u"""[Herron1991]""",
    longDesc =
u"""
Part of the "HCN" subset
T range: 298-2840 K
Review and reccomendation, p. 656, 13,5(b)
""",
)

entry(
    index = 215,
    label = "HCN + OH <=> NH2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.83e-04, 'cm^3/(mol*s)'), n=4.00, Ea=(4000, 'cal/mol'), T0=(1, 'K'), Tmin=(500, 'K'), Tmax=(2500, 'K')),
    shortDesc = u"""[Hanson1996]""",
    longDesc =
u"""
Part of the "HCN" subset
T range: 500-2500 K
BAC-MP4
J.A. Miller, C.F. Melius, Symposium (International) on Combustion, 1988, 21(1), 919-927, doi: 10.1016/S0082-0784(88)80324-2
as reported by [Hanson1996] (4d in Table 1, p. 249)
""",
)

entry(
    index = 216,
    label = "HCN + OH <=> H + HNCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.6e-06, 'cm^3/(mol*s)'), n=4.71, Ea=(-493, 'cal/mol'), T0=(1, 'K'), Tmin=(298, 'K'), Tmax=(2840, 'K')),
    shortDesc = u"""[Herron1991]""",
    longDesc =
u"""
Part of the "HCN" subset
T range: 298-2840 K
Review and reccomendation, p. 656, 13,5(c)
""",
)

entry(
    index = 217,
    label = "S + S <=> S2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(3.98e+14, 'cm^6/(mol^2*s)'), n=0, Ea=(-22455, 'cal/mol'), T0 = (1, 'K'), Tmin=(4500, 'K'), Tmax=(6000, 'K'))),
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
    index = 218,
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
    index = 219,
    label = "SO + O <=> S + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.36e+07, 'cm^3/(mol*s)'), n=1.51, Ea=(5042, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Lin2003a]""",
    longDesc =
u"""
Part of the "SOx" mechanism
k10b p. 11028
calculations done at the G2M(RCC2)//B3LYP/6-311+(3df) level of theory
also validated experimentally in the same study
""",
)

entry(
    index = 220,
    label = "SO <=> S + O",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(3.98e+14, 'cm^3/(mol*s)'), n=0, Ea=(107000, 'cal/mol'), T0 = (1, 'K'), Tmin=(3000, 'K'), Tmax=(5000, 'K'))),
    shortDesc = u"""[Troe1984]""",
    longDesc =
u"""
Part of the "SOx" mechanism
Shock tube experimental study, done in Ar.
T range: 3000-5000 K
""",
)

entry(
    index = 221,
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
    index = 222,
    label = "SO2 + O + N2 <=> SO3 + N2",
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
    index = 225,
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
    index = 226,
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
    index = 227,
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
    index = 228,
    label = "SO3 + H <=> SO2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.4e+09, 'cm^3/(mol*s)'), n=1.22, Ea=(3320, 'cal/mol'), T0=(1, 'K'), Tmin=(700, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"""[Marshall2007a]""",
    longDesc =
u"""
Part of the "SOx" mechanism
T range: 700-2000 K
calculations done at the CBS-QB3/CCSD(T)//B3LYP/6-311G(2d,d,p) level of theory
""",
)

entry(
    index = 229,
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
    index = 230,
    label = "SO3 + OH <=> SO2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.8e+04, 'cm^3/(mol*s)'), n=2.46, Ea=(27225, 'cal/mol'), T0=(1, 'K'), Tmin=(800, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"""[Marshall2007a]""",
    longDesc =
u"""
Part of the "SOx" mechanism
T range: 800-2000 K
calculations done at the CBS-QB3/CCSD(T)//B3LYP/6-311G(2d,d,p) level of theory
""",
)

entry(
    index = 231,
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
    index = 232,
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
    index = 233,
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
    index = 234,
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
    index = 235,
    label = "HOSO <=> HSO2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.03e+9, 's^-1'), n=1.03, Ea=(49980, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(2000, 'K')),
        arrheniusLow = Arrhenius(A=(1.72e+35, 'cm^3/(mol*s)'), n=-5.64, Ea=(55423, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(2000, 'K')),
        alpha=1, T3=(1e-30, 'K'), T1=(1e+30, 'K'), efficiencies={}),
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
    index = 236,
    label = "HSOO <=> SH + O2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(4.41e+18, 's^-1'), n=-1.07, Ea=(7750, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(2000, 'K')),
        arrheniusLow = Arrhenius(A=(1.56e+23, 'cm^3/(mol*s)'), n=-2.82, Ea=(-7450, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(2000, 'K')),
        alpha=1, T3=(1e-30, 'K'), T1=(1e+30, 'K'), efficiencies={}),
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
    index = 237,
    label = "HOSO <=> OH + SO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.65e+16, 's^-1'), n=-0.32, Ea=(67720, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(2000, 'K')),
        arrheniusLow = Arrhenius(A=(1.25e+32, 'cm^3/(mol*s)'), n=-4.33, Ea=(69115, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(2000, 'K')),
        alpha=1, T3=(1e-30, 'K'), T1=(1e+30, 'K'), efficiencies={}),
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
    index = 238,
    label = "HSOO <=> HSO + O",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.01e+19, 's^-1'), n=-1.07, Ea=(28377, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(2000, 'K')),
        arrheniusLow = Arrhenius(A=(9.27e+34, 'cm^3/(mol*s)'), n=-5.87, Ea=(30960, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(2000, 'K')),
        alpha=1, T3=(1e-30, 'K'), T1=(1e+30, 'K'), efficiencies={}),
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
    index = 239,
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
    index = 240,
    label = "SO + O2 <=> SO2 + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.2e+03, 'cm^3/(mol*s)'), n=2.42, Ea=(3050, 'cal/mol'), T0=(1, 'K'), Tmin=(230, 'K'), Tmax=(2980, 'K')),
    shortDesc = u"""[GlarBozz]""",
    longDesc =
u"""
Part of the "SOx" subset
High T range (2570-2980 K) rate taken from experimental shock tube measurement: D. Woiki, P. Roth, Int. J. Chem. Kin., 1995, 27(1), 59-71, doi: 10.1002/kin.550270108
Low T range (230-420 K) rate taken from: [Baulch1992]
As reported by [GlarBozz] (14)
""",
)

entry(
    index = 241,
    label = "S + SO2 <=> SO + SO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.89e+12, 'cm^3/(mol*s)'), n=0, Ea=(9034, 'cal/mol'), T0=(1, 'K'), Tmin=(1120, 'K'), Tmax=(1540, 'K')),
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
    index = 242,
    label = "H2S + O <=> HSO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.0e+13, 'cm^3/(mol*s)','+|-',1.52e+13), n=0, Ea=(7650, 'cal/mol','+|-',482), T0=(1, 'K'), Tmin=(1520, 'K'), Tmax=(1820, 'K')),
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
    index = 243,
    label = "SO3 + H2O + H2O <=> H2SO4 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.41e+07, 'cm^6/(mol^2*s)','+|-',2.82e+06), n=0, Ea=(-13500, 'cal/mol'), T0=(1, 'K'), Tmin=(283, 'K'), Tmax=(370, 'K')),
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
    index = 244,
    label = "HOSO2 <=> SO2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.34e+14, 's^-1'), n=0, Ea=(25832, 'cal/mol'), T0=(1, 'K'), Tmin=(150, 'K'), Tmax=(1500, 'K')),
    shortDesc = u"""[Somnitz2004]""",
    longDesc =
u"""
Part of the "SOx" subset
T range: 150-1500 K
k_dec_inf, p. 3847 in Fig. 2
calculated at the B3LYP/apVTZþ1//UB3LYP/apVTZþ1 level of theory
Also available in reverse from [Pilling2003], but for a relatively low T range (up to 673):
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.23e+12, 'cm^3/(mol*s)'), n=-0.27, Ea=(0, 'cal/mol'), T0=(300, 'K')),
        arrheniusLow = Arrhenius(A=(1.25e+17, 'cm^6/(mol^2*s)'), n=-4.09, Ea=(0, 'cal/mol'), T0=(300, 'K')),
        alpha=1.0, T3=(1e-30, 'K'), T1=(412, 'K'), efficiencies={'O=S=O': 5, 'O': 5, 'O=C=O': 2.5}),
    Collider efficiencies taken from: Gimenez-Lopez, M. Martinez, A. Millera, R. Bilbao, M.U. Alzueta, Comb. Flame 2011, 158(1), 48-56, doi: 10.1016/j.combustflame.2010.07.017
""",
)

entry(
    index = 246,
    label = "COS + O <=> SO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.43e+13, 'cm^3/(mol*s)'), n=0, Ea=(4830, 'cal/mol'), T0=(1, 'K'), Tmin=(1120, 'K'), Tmax=(1540, 'K')),
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
    index = 247,
    label = "COS + O <=> S + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.73e+13, 'cm^3/(mol*s)'), n=0, Ea=(6900, 'cal/mol'), T0=(1, 'K'), Tmin=(1120, 'K'), Tmax=(1540, 'K')),
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
    index = 248,
    label = "COS + H <=> CO + SH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+14, 'cm^3/(mol*s)'), n=0, Ea=(6786, 'cal/mol'), T0=(1, 'K'), Tmin=(1170, 'K'), Tmax=(1830, 'K')),
    shortDesc = u"""[Roth1996a]""",
    longDesc =
u"""
Part of the "COS" subset
Sock Tube
T range: 1170-1830 K
""",
)

entry(
    index = 249,
    label = "CS2 + H <=> CS + SH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+15, 'cm^3/(mol*s)'), n=0, Ea=(18380, 'cal/mol'), T0=(1, 'K'), Tmin=(1170, 'K'), Tmax=(1830, 'K')),
    shortDesc = u"""[Roth1996a]""",
    longDesc =
u"""
Part of the "COS" subset
Sock Tube
T range: 1170-1830 K
""",
)

entry(
    index = 250,
    label = "COS <=> CO + S",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(2.45e+14, 'cm^3/(mol*s)'), n=0, Ea=(61400, 'cal/mol'), T0 = (1, 'K'), Tmin=(1140, 'K'), Tmax=(3230, 'K'))),
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
    index = 251,
    label = "COS + S <=> CO + S2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.35e+13, 'cm^3/(mol*s)'), n=0, Ea=(6764, 'cal/mol'), T0=(1, 'K'), Tmin=(1140, 'K'), Tmax=(3230, 'K')),
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
    index = 252,
    label = "COS <=> CO + Sa",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(4.8e+22, 'cm^3/(mol*s)'), n=0, Ea=(71800, 'cal/mol'), T0 = (1, 'K'), Tmin=(1830, 'K'), Tmax=(3020, 'K'))),
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
    index = 253,
    label = "H2S + H <=> SH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.5e+07, 'cm^3/(mol*s)'), n=1.94, Ea=(904, 'cal/mol'), T0=(1, 'K'), Tmin=(190, 'K'), Tmax=(2237, 'K')),
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
    index = 254,
    label = "H2S + S <=> SH + SH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.7e+06, 'cm^3/(mol*s)'), n=2.297, Ea=(9010, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
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
    index = 255,
    label = "S + H2 <=> SH + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.58e+14, 'cm^3/(mol*s)'), n=0, Ea=(19700, 'cal/mol'), T0=(1, 'K'), Tmin=(2740, 'K'), Tmax=(3570, 'K')),
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
    index = 256,
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
    index = 257,
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
    index = 258,
    label = "H2S <=> H2 + S",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.60e+24, 'cm^3/(mol*s)'), n=-2.613, Ea=(89173, 'cal/mol'), T0 = (1, 'K'), Tmin=(900, 'K'), Tmax=(3600, 'K'))),
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
    index = 259,
    label = "H + S2 <=> HSS",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.60e+24, 'cm^6/(mol^2*s)'), n=-2.613, Ea=(89173, 'cal/mol'), T0 = (1, 'K'), Tmin=(873, 'K'), Tmax=(1423, 'K')),
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
    index = 260,
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
    index = 261,
    label = "HSSH <=> SH + SH",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(2.31e+14, 'cm^3/(mol*s)'), n=1, Ea=(57030, 'cal/mol'), T0 = (1, 'K'), Tmin=(873, 'K'), Tmax=(1423, 'K')),
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
    index = 262,
    label = "SH + HSS <=> H2S + S2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.27e+03, 'cm^3/(mol*s)'), n=3.050, Ea=(-1105, 'cal/mol'), T0 = (1, 'K'), Tmin=(873, 'K'), Tmax=(1423, 'K')),
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
    index = 263,
    label = "H + HSS <=> H2 + S2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.23e+08, 'cm^3/(mol*s)'), n=1.653, Ea=(-1105, 'cal/mol'), T0 = (1, 'K'), Tmin=(873, 'K'), Tmax=(1423, 'K')),
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
    index = 264,
    label = "H + HSS <=> H2S + S",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(6326, 'cal/mol'), T0 = (1, 'K'), Tmin=(873, 'K'), Tmax=(1423, 'K')),
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
    index = 265,
    label = "S + HSS <=> S2 + SH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.17e+06, 'cm^3/(mol*s)'), n=2.200, Ea=(-600, 'cal/mol'), T0 = (1, 'K'), Tmin=(873, 'K'), Tmax=(1423, 'K')),
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
    index = 266,
    label = "HSS + HSS <=> HSSH + S2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.56e+00, 'cm^3/(mol*s)'), n=3.370, Ea=(-1672, 'cal/mol'), T0 = (1, 'K'), Tmin=(873, 'K'), Tmax=(1423, 'K')),
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
    index = 267,
    label = "HSSH + H <=> HSS + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.99e+07, 'cm^3/(mol*s)'), n=1.933, Ea=(-1408, 'cal/mol'), T0 = (1, 'K'), Tmin=(873, 'K'), Tmax=(1423, 'K')),
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
    index = 268,
    label = "HSSH + H <=> H2S + SH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.66e+08, 'cm^3/(mol*s)'), n=1.724, Ea=(467, 'cal/mol'), T0 = (1, 'K'), Tmin=(873, 'K'), Tmax=(1423, 'K')),
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
    index = 269,
    label = "HSSH + SH <=> H2S + HSS",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.40e+03, 'cm^3/(mol*s)'), n=2.980, Ea=(-1480, 'cal/mol'), T0 = (1, 'K'), Tmin=(873, 'K'), Tmax=(1423, 'K')),
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
    index = 270,
    label = "HSSH + S <=> HSS + SH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.85e+06, 'cm^3/(mol*s)'), n=2.310, Ea=(-1204, 'cal/mol'), T0 = (1, 'K'), Tmin=(873, 'K'), Tmax=(1423, 'K')),
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
    index = 271,
    label = "CH3SH + H <=> CH3S + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.39e+08, 'cm^3/(mol*s)'), n=1.729, Ea=(986, 'cal/mol'), T0 = (1, 'K'), Tmin=(200, 'K'), Tmax=(3000, 'K')),
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
    index = 272,
    label = "CH3SH + H <=> CH2SH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.16e+03, 'cm^3/(mol*s)'), n=2.925, Ea=(4747, 'cal/mol'), T0 = (1, 'K'), Tmin=(250, 'K'), Tmax=(3000, 'K')),
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
    index = 273,
    label = "CH3SH + H <=> CH3 + H2S",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.17e+10, 'cm^3/(mol*s)'), n=0.766, Ea=(3225, 'cal/mol'), T0 = (1, 'K'), Tmin=(200, 'K'), Tmax=(3000, 'K')),
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
    index = 274,
    label = "CH3SH + H <=> CH4 + SH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.99e+06, 'cm^3/(mol*s)'), n=1.983, Ea=(16536, 'cal/mol'), T0 = (1, 'K'), Tmin=(400, 'K'), Tmax=(3000, 'K')),
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
    index = 275,
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
    index = 276,
    label = "S + CS2 <=> CS + S2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.87e+13, 'cm^3/(mol*s)'), n=0.00, Ea=(8843, 'cal/mol'), T0=(1, 'K'), Tmin=(690, 'K'), Tmax=(1040, 'K')),
    shortDesc = u"""[Marshall2011]""",
    longDesc =
u"""
Part of the "C-S" mechanism
T range: 690-1040 K
""",
)

entry(
    index = 277,
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
    index = 278,
    label = "NO2 + SO2 <=> NO + SO3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.31e+12, 'cm^3/(mol*s)'), n=0, Ea=(53700, 'cal/mol'), T0=(1, 'K'), Tmin=(700, 'K'), Tmax=(2000, 'K')),
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
    index = 279,
    label = "NO2 + S <=> SO + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.14e+13, 'cm^3/(mol*s)'), n=0, Ea=(-980, 'cal/mol'), T0=(1, 'K'), Tmin=(292, 'K'), Tmax=(656, 'K')),
    shortDesc = u"""[Marshall2012]""",
    longDesc =
u"""
Part of the "SOx-NOx" direct interactions subset
T range: 292-656 K
Experimentally measured, and PES verified using QCISD/6-311G(d,p)
""",
)

entry(
    index = 280,
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
    index = 281,
    label = "S + NO <=> SO + N",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.08e+14, 'cm^3/(mol*s)'), n=0, Ea=(40100, 'cal/mol'), T0=(1, 'K'), Tmin=(2420, 'K'), Tmax=(3870, 'K')),
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
    index = 282,
    label = "S + NO <=> NS + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(40100, 'cal/mol'), T0=(1, 'K'), Tmin=(2420, 'K'), Tmax=(3870, 'K')),
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
    index = 283,
    label = "CH4 + NO2 <=> HONO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.71e+13, 'cm^3/(mol*s)'), n=0, Ea=(32450, 'cal/mol'), T0=(1, 'K'), Tmin=(500, 'K'), Tmax=(1650, 'K')),
    shortDesc = u"""[Yang2012]""",
    longDesc =
u"""
Part of the "C1-oxygenates" subset
k1a + k1b
originally given for 400-4000 K in a custom Arrhenius form with T-dependent Ea.
Manually converted to a normal modified Arrhenius form here for a smaller T range with coefficients of determination 0.9985
T range: 500-1650 K
calculated at the B3LYP/6-311G(2d,d,p)//M06-2X/MG3S level of theory
conformer-dup: rates summed for trans/cis-HONO
Train!
""",
)

entry(
    index = 283,
    label = "CH4 + NO2 <=> HNO2 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.985e+13, 'cm^3/(mol*s)'), n=0, Ea=(36685, 'cal/mol'), T0=(1, 'K'), Tmin=(500, 'K'), Tmax=(1650, 'K')),
    shortDesc = u"""[Yang2012]""",
    longDesc =
u"""
Part of the "C1-oxygenates" subset
k1c
originally given for 400-4000 K in a custom Arrhenius form with T-dependent Ea.
Manually converted to a normal modified Arrhenius form here for a smaller T range with coefficients of determination 0.9995
T range: 500-1650 K
calculated at the B3LYP/6-311G(2d,d,p)//M06-2X/MG3S level of theory
Train!
""",
)







"""
check refs:
http://pubs.acs.org/doi/abs/10.1021/jp961568q
http://aip.scitation.org/doi/abs/10.1063/1.3253112
http://dx.doi.org/10.1063/1.3253112
SO + SO3 <=> SO2 + SO2
S + SH <=> S2 + H
H + S <=> SH
NO + H <=> HNO
SO3 + H <=> HOSO + O
SO2 + OH <=> HOSO + O
SO + H <=> HSO
HSO + H <=> HSOH
HSO + H <=> SH + OH
HSO + H <=> S + H2O
HSO + H <=> H2SO
HSO + H <=> SO + H2
HSO + O <=> SO2 + H
HSO + O <=> HOS + O
HSO + O <=> SO + OH
HSO + O <=> HOSO
HSO + OH <=> HOSHO
HSO + OH <=> HOSHO + H
HSO + OH <=> SO + H2O
HSO + O2 <=> SO2 + OH
HSOH <=> SH + OH
HSOH <=> S + H2O
HSOH <=> H2S + O
H2SO <=> H2S + O
HOSO <=> HOS + O
HOSO + H <=> SO + H2O
HOSO + OH <=> SO2 + HO2
HOSO2 <=> HOSO + O
HOSO2 <=> SO3 + H
HOSO2 + H <=> SO2 + H2O
HOSO2 + O <=> SO3 + OH
HOSO2 + OH <=> SO3 + H2O
HOSHO <=> HOSO + H
HOSHO <=> SO + H2O
HOSHO + H <=> HOSO + H2
HOSHO + O <=> HOSO + OH
HOSHO + OH <=> HOSO + H2O
Glarborg, no real reference... DOI: 10.1002/(SICI)1097-4601(1996)28:10<773::AID-KIN8>3.0.CO;2-K
S-N interactions:
SH + NO2 <=> HSO + NO (available only for low T at NIST)
SH + N2O <=> HSO + N2 (available only for low T at NIST)
SO + NO2 <=> SO2 + NO (available only for low T at NIST)
SO2 + N <=> SO + NO
HSO + NO2 <=> HOSO + NO (available only for low T at NIST)
SO3 + N <=> SO2 + NO (available only for low T at NIST)
SO2 + SO2 = SO3 + SO take from [Marshall2007a]:37 if RMG can't generate it
If no better source, try tracing HSO2+H=SO2+H2 and HSO2+OH=SO2+H2O from http://dx.doi.org/10.1080/00102208308923623
Gimenez-Lopez, M. Martinez, A. Millera, R. Bilbao, M.U. Alzueta, Comb. Flame 2011, 158(1), 48-56, doi: 10.1016/j.combustflame.2010.07.017
report on:
SO + O2 = SO2 + O2
SO + OH = HOSO
but the source [24] isn't clear
also HOSO + H, HOSO2 + O2
SO3 + H2O <=> H2SO4 dimer?
http://pubs.acs.org/doi/abs/10.1021/jp962414d - gives experimental rate for 250-360 K, 20-80 torr
http://pubs.acs.org/doi/abs/10.1021/jp972549z - gives experimental rate for 283-370 K, 100-760 torr
SO2 + H2O <=> H2SO3 ?
http://pubs.acs.org/doi/abs/10.1021/jp972389r - give estimated geometry if i want to calc...
add eq:
H2O = H2Odimer
H2Odimer
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 O u0 p2 c0 {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
Frequencies:
[Lin2014] desktop
J. Phys. Chem. A 2008, 112, 3239-3247, doi: 10.1021/jp710488d
http://aip.scitation.org/doi/abs/10.1063/1.477560
http://onlinelibrary.wiley.com/wol1/doi/10.1002/kin.10178/full
http://pubs.acs.org/doi/abs/10.1021/jp9801370
http://pubs.acs.org/doi/abs/10.1021/jp001610o
http://pubs.acs.org/doi/abs/10.1021/jp000464j
http://pubs.acs.org/doi/abs/10.1021/jp054722u
http://pubs.acs.org/doi/abs/10.1021/jp067499p
http://pubs.acs.org/doi/abs/10.1021/j100185a016
http://pubs.acs.org/doi/abs/10.1021/jp054722u
http://pubs.acs.org/doi/abs/10.1021/jp0544585
go through all Lin's papers
http://pubs.acs.org/doi/abs/10.1021/jp905454k
, Tmin=(700, 'K'), Tmax=(2000, 'K')
Thermo data (only H & S) for various sulfur species and compounds:
http://pubs.acs.org/doi/abs/10.1021/jp972389r
OLD NSRDS with combustion relevant reactions, some at high T: http://dx.doi.org/10.6028/NBS.NSRDS.73p1 (from: https://www.nist.gov/srd/srd-publications/national-standard-reference-data-series-nsrds)
"""

