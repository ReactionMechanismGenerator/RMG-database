#!/usr/bin/env python
# encoding: utf-8

# rename to original

name = "Sulfur/HSSH_1bar"
shortDesc = u"HSSH PES at 1bar"
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
[Sendt2009a] C.R. Zhou, K. Sendt, B.S. Haynes, J. Phys. Chem. A, 2009, 113, 2975-2981, doi: 10.1021/jp810105e
[Sendt2009b] C.R. Zhou, K. Sendt, B.S. Haynes, J. Phys. Chem. A, 2009, 113, 8299-8306, doi: 10.1021/jp903185k
"""

entry(
    index = 1,
    label = "H2S + S <=> SH + SH",
    degeneracy = 2,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1.18e+18, 'cm^3/(mol*s)'), n=-1.685, Ea=(5975, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2000, 'K')),
            Arrhenius(A=(7.40e+06, 'cm^3/(mol*s)'), n=2.297, Ea=(9011, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2000, 'K')),
        ],
    ),
    shortDesc = u"""[Marshall2011b],[Sendt2008]""",
    longDesc =
u"""
computed at 1 bar, Table 1, 3rd entry from [Marshall2011b]
k_abstraction from [Sendt2008] p. 3242
calculations done at the MRCI/aug-cc-pV(Q+d)Z//MRCI/aug-cc-pVTZ level of theory

Also available from [Sendt2008]. NOTE that [Sendt2008] has a correction to this rate (!): doi: 10.1021/jp810800a
Also available from [Sendt2009b]

(note that t[Sendt2008] has a CORRECTION, doi: 10.1021/jp810800a, and the original rate should be multiplied by a factor
of x2: i.e., A = 7.4e+06 cm^3/(mol*s), NOT 3.7e+06 cm^3/(mol*s))
""",
)

entry(
    index = 2,
    label = "HSS + H <=> S2 + H2",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(2.91e+16, 'cm^3/(mol*s)'), n=-0.894, Ea=(0, 'kJ/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2000, 'K')),
            Arrhenius(A=(1.05e+08, 'cm^3/(mol*s)'), n=1.750, Ea=(-4, 'kJ/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2000, 'K')),
        ],
    ),
    shortDesc = u"""[Sendt2009b]""",
    longDesc =
u"""
R10
calculations done at the MRCI/aug-cc-pV(Q+d)Z//CASSCF/cc-pVTZ level of theory
One rate is not PDep, the other is PDep given at 1 bar
also available from [Sendt2008] and [Marshall2011b]
""",
)

entry(
    index = 3,
    label = "HSS + H <=> H2S + S",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(4.19e+18, 'cm^3/(mol*s)'), n=-1.563, Ea=(2, 'kJ/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2000, 'K')),
            Arrhenius(A=(1.50e+08, 'cm^3/(mol*s)'), n=1.551, Ea=(9, 'kJ/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2000, 'K')),
        ],
    ),
    shortDesc = u"""[Sendt2009b]""",
    longDesc =
u"""
R9
calculations done at the MRCI/aug-cc-pV(Q+d)Z//CASSCF/cc-pVTZ level of theory
One rate is not PDep, the other is PDep given at 1 bar
also available from [Sendt2002]
""",
)
