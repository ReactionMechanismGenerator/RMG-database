#!/usr/bin/env python
# encoding: utf-8

name = "Sulfur/H2S+S=2SH_1bar"
shortDesc = u"H2S + S = SH + SH at 1bar"
longDesc =u"""
The H2S + S = SH + SH reaction has several pathways.
The direct H-abstraction on the triplet surface has a barrier of 45 kJ/mol
H2S + S can also pass through an inter-system crossing (barrier estimated to be only 3 kJ/mol),
passing through singlet H2SS and HSSH, yielding the same products (SH + SH).
The direct H-abvstraction is significant above 800 K, and dominates above 1000 K.
However, below 700-800 K this reaction is significantly dependent on pressure. 
This reaction should be modeled as two duplicate reactions - Arhennius and PDep.
However, the PDep path is only givin in literature at 1 bar.
This reaction behaves as P-Dep at low P, while its high-P limit is zero(!).
This library should not be used at higher pressures.

[Marshall2011b] Y. Gao, C.(R) Z., K. Sendt, B.S. Haynes, P. Marshall, Proc. Comb. Inst., 2011, 33, 459-465, doi: 10.1016/j.proci.2010.05.020
[Sendt2008] C.R. Zhou, K. Sendt, B.S. Haynes, J. Phys. Chem. A, 2008, 112, 3239-3247, doi: 10.1021/jp710488d
"""

entry(
    index = 1,
    label = "H2S + S <=> SH + SH",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(A=(7.4e+06, 'cm^3/(mol*s)'), n=2.297, Ea=(9011, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(300, 'K'), Tmax=(3000, 'K')),
    shortDesc = u"""[Sendt2008]""",
    longDesc =
u"""
k_abstraction, (R4a)
T range: 300-3000 K
calculations done at the MRCI/aug-cc-pV(Q+d)Z//MRCI/aug-cc-pVTZ level of theory

(note that this source has a CORRECTION, doi: 10.1021/jp810800a, and the original rate should is multiplied by a factor
of x2: i.e., A = 7.4e+06 cm^3/(mol*s), NOT 3.7e+06 cm^3/(mol*s))
""",
)

entry(
    index = 2,
    label = "H2S + S <=> SH + SH",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(A=(1.18e+18, 'cm^3/(mol*s)'), n=-1.685, Ea=(5975, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(300, 'K'), Tmax=(1040, 'K')),
    shortDesc = u"""[Marshall2011b]""",
    longDesc =
u"""
DKCCSD(T)/cc-PVQZ_DK
The H2S+S PES passes through an inter-system crossing with a low barrier, and is infact P-Dep at low T (below 800 K)
The rate here is computed at 1 bar. Bath gas: Ar.
""",
)
