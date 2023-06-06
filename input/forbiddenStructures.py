#!/usr/bin/env python
# encoding: utf-8

name = ""
shortDesc = u""
longDesc = u"""

"""
entry(
    label = "Ods",
    group =
"""
1 O ux c0 {2,D} {3,S}
2 R ux {1,D}
3 R ux {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
This forbids O with both single and double bonds WHILE keeping a zero partial charge.
This does not forbid ozone, [O-][O+]=O
""",
)

entry(
    label = "Od_rad",
    group = 
"""
1 O u1 {2,D}
2 R ux {1,D}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    label = "N_birad_triplet_2singleBonds",
    group = 
"""
1 N u2 p0 {2,S} {3,S}
2 R ux {1,S}
3 R ux {1,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    label = "C_quintet",
    molecule =
"""
1 C u4 p0
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    label = "Carbene_D_triplet",
    group =
"""
1 C u2 p0 {2,D}
2 C u0 {1,D}
""",
    shortDesc = u"""""",
    longDesc =
u"""
restricts C2O, see RMG-Py issue #514
""",
)

entry(
    label = "Carbene_S_triplet",
    group =
"""
1 C   u2 p0 {2,S}
2 R!H u0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    label = "O3",
    group = 
"""
1 O u[0,1] {2,S}
2 O u0     {1,S} {3,S}
3 O u[0,1] {2,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    label = "O4..",
    group = 
"""
1 O u1 {2,S}
2 O u0 {1,S} {3,S}
3 O u0 {2,S} {4,S}
4 O u1 {3,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    label = "cyclic-C3O",
    group = 
"""
1 C u0 {2,D} {3,S} {4,S}
2 O u0 {1,D}
3 C u0 {1,S} {4,T}
4 C u0 {1,S} {3,T}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    label = "cyclobutyne",
    group =
"""
1 R!H ux {2,T} {4,S}
2 R!H ux {1,T} {3,S}
3 R!H ux {2,S} {4,[S,D,T,B]}
4 R!H ux {1,S} {3,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
""",
)

entry(
    label = "CO_birad",
    species =
"""
multiplicity 3
1 C u2 p0 c0 {2,D}
2 O u0 p2 c0 {1,D}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbidden after discussion with whgreen.
This species should quickly transform into a closed shell [C-]#[O+].
We don't need it as a resonance structure of carbon monoxide for reactivity since carbon monoxide has its designated
reaction families (CO_Disprop, R_Add_COm).
""",
)

entry(
    label = "CS_birad",
    species =
"""
multiplicity 3
1 C u2 p0 c0 {2,D}
2 S u0 p2 c0 {1,D}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbidden after discussion with whgreen.
This species should quickly transform into a closed shell [C-]#[S+] similar to the carbon monoxide case above.
We don't need it as a resonance structure of carbon monsulfide for reactivity since carbon monsulfide has its designated
reaction families (CO_Disprop [also deals with CS], R_Add_CSm).
""",
)

entry(
    label = "N-N(S)",
    species =
"""
1 N u0 p2 c0 {2,S}
2 N u0 p2 c0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
This structure is not a stationary point, and should quickly become N#N
""",
)

entry(
    label = "[N][N]",
    species =
"""
multiplicity 5
1 N u2 p1 c0 {2,S}
2 N u2 p1 c0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
N#N can be excited to [N]=[N], but we shouldn't allow it to reach [N][N]
""",
)

entry(
    label = "SOO2",
    species =
"""
multiplicity 3
1 S u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 O u1 p2 c0 {1,S}
4 O u1 p2 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
The SO--O2 complex isn't a sable species (i.e., its geometry cannot be optimized with a reasonable SO--OO bond length),
yet it is predicted by RMG, e.g, by R_Recombination of [S][O] and [O][O].

Another resonance structure of it which is forbidden as well via this entry is:
multiplicity 3
1 S u1 p1 c0 {2,S} {3,D}
2 O u0 p2 c0 {1,S} {4,S}
3 O u0 p2 c0 {1,D}
4 O u1 p2 c0 {2,S}
""",
)

entry(
    label = "SO2O2",
    species =
"""
multiplicity 3
1 S u0 p1 c0 {2,S} {3,S} {4,D}
2 O u0 p2 c0 {1,S} {5,S}
3 O u1 p2 c0 {1,S}
4 O u0 p2 c0 {1,D}
5 O u1 p2 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
The SO2--O2 complex isn't a sable species (i.e., its geometry cannot be optimized with a reasonable O2S--OO bond length),
yet it is predicted by RMG, e.g, by R_Addition_Multiple_Bond of O=S=O and [O][O].
Also, it is described as a TS in doi: 10.1021/jp067499p (Fig. 1 structure 5, Fig. 2)

Another resonance structure of it which is forbidden as well via this entry is:
multiplicity 3
1 S u1 p0 c0 {2,S} {3,D} {4,D}
2 O u0 p2 c0 {1,S} {5,S}
3 O u0 p2 c0 {1,D}
4 O u0 p2 c0 {1,D}
5 O u1 p2 c0 {2,S}
""",
)

entry(
    label = "S2O2",
    species =
"""
multiplicity 3
1 O u0 p2 c0 {2,S} {3,S}
2 S u0 p2 c0 {1,S} {4,S}
3 O u1 p2 c0 {1,S}
4 S u1 p2 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
The S2--O2 complex isn't a sable species (has an imaginary frequency),
yet it is predicted by RMG, e.g, by R_Recombination of [S][S] and [O][O].

Another resonance structure of it which is forbidden as well via this entry is:
multiplicity 3
1 O u0 p2 c0 {2,S} {3,S}
2 S u1 p1 c0 {1,S} {4,D}
3 O u1 p2 c0 {1,S}
4 S u0 p2 c0 {2,D}
""",
)

entry(
    label = "N2SH",
    species =
"""
multiplicity 2
1 N u0 p0 c+1 {2,D} {3,D}
2 S u1 p1 c0 {1,D} {4,S}
3 N u0 p2 c-1 {1,D}
4 H u0 p0 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
The N2--SH complex isn't a sable species (i.e., its geometry cannot be optimized with a reasonable NN--SH bond length),
yet it is predicted by RMG, e.g, by R_Addition_Multiple_Bond of [SH] to N#N.

Other resonance structures of it which are forbidden as well via this entry are:
multiplicity 2
1 N u0 p1 c0 {2,S} {3,D}
2 S u0 p2 c0 {1,S} {4,S}
3 N u1 p1 c0 {1,D}
4 H u0 p0 c0 {2,S}

multiplicity 2
1 N u1 p0 c+1 {2,S} {3,D}
2 S u0 p2 c0 {1,S} {4,S}
3 N u0 p2 c-1 {1,D}
4 H u0 p0 c0 {2,S}
""",
)

entry(
    label = "N2SO",
    group =
"""
1 O u0 {2,[S,D]}
2 S u0 {1,[S,D]} {3,[S,D]}
3 N u0 {2,[S,D]} {4,[S,D]}
4 N u0 {3,[S,D]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
The N2--SO complex isn't sable (i.e., NNSO's geometry cannot be optimized with a reasonable NN--SO bond length),
yet it is predicted by RMG, e.g, by R_Addition_Multiple_Bond of [S][O] to N#N.
N2SO2 is forbidden as well in this group for the same reason.
""",
)

entry(
    label = "SO3(T)",
    species =
"""
multiplicity 3
1 O u0 p2 c0 {2,D}
2 S u1 p0 c0 {1,D} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 O u1 p2 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
The geometry of SO3(T) could not be stabilized at either B3LYP/6-311G(2d,d,p) nor M06-2x
without getting negative frequency/ies.
""",
)

entry(
    label = "cN3HNH2",
    species =
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 N u0 p1 c0 {1,S} {4,S} {5,S}
3 N u0 p1 c0 {1,S} {6,S} {7,S}
4 N u1 p1 c0 {1,S} {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Geometry could not converge at CBS-QB3
""",
)

entry(
    label = "cN3HN",
    group =
"""
1 N u0     p1 c0 {2,S} {3,S} {5,S}
2 N u[0,1] p1 c0 {1,S} {3,S}
3 N u0     p0 c+1 {1,S} {2,S} {4,D}
4 N u0     p2 c-1 {3,D}
5 R ux     px cx {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Geometry of the following species in this group could not converge at CBS-QB3
[N-]=[N+]1[N]N1
[N-]=[N+]1NN1
""",
)

entry(
    label = "NH3NNH",
    species =
"""
multiplicity 2
1 N u0 p0 c+1 {2,S} {4,S} {5,S} {6,S}
2 N u0 p2 c-1 {1,S} {3,S}
3 N u1 p1 c0 {2,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Geometry could not converge at wB97x-D3/6-311++G(3df,3pd) (alongd ref - xq1488)
""",
)

entry(
    label = "NNHNH",
    species =
"""
multiplicity 2
1 N u0 p0 c+1 {2,S} {3,D} {5,S}
2 N u0 p1 c0 {1,S} {4,D}
3 N u0 p2 c-1 {1,D}
4 N u1 p1 c0 {2,D}
5 H u0 p0 c0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Geometry could not converge at wB97x-D3/6-311++G(3df,3pd) (alongd ref - xq1492)
""",
)

entry(
    label = "C2_triplebond",
    species =
"""
1 C u0 p1 c-1 {2,T}
2 C u0 p0 c+1 {1,T}
""",
    shortDesc = u"""""",
    longDesc =
u"""
https://pubs.acs.org/doi/pdf/10.1021/ct400867h discusses complex wavefunction for C2
and that it cannot be assigned definitive bond order. We are forbidding the C2 triple bond
becuase we do not have good thermo for `Ctc` (C u0 p0 c+1 {1,T}) atomtype
""",
)

entry(
    label = "CO2X2",
    species =
"""
1 O u0 p2 c0 {3,S} {5,S}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,S} {2,D} {4,S}
4 X u0 p0 c0 {3,S}
5 X u0 p0 c0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
We assume that CO2 binds only via physisorption to the surface
""",
)

entry(
    label = "CO2X3",
    species =
"""
1 O u0 p2 c0 {3,S} {6,S}
2 O u0 p2 c0 {3,S} {5,S}
3 C u0 p0 c0 {1,S} {2,S} {4,D}
4 X u0 p0 c0 {3,D}
5 X u0 p0 c0 {2,S}
6 X u0 p0 c0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
We assume that CO2 binds only via physisorption to the surface
""",
)

entry(
    label = "O2X2",
    species =
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 X u0 p0 c0 {1,S}
4 X u0 p0 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
O2 dissociates upon adsorption
""",
)

entry(
    label = "OCX2",
    species =
"""
1 O u0 p2 c0 {2,S} {3,S}
2 C u0 p0 c0 {1,S} {4,T}
3 X u0 p0 c0 {1,S}
4 X u0 p0 c0 {2,T}
""",
    shortDesc = u"""""",
    longDesc =
u"""
CO binds in a monodentate configuration
""",
)

entry(
    label = "NcNOO",
    molecule =
"""
1 N u0 p2 c-1 {2,D}
2 N u0 p0 c+1 {1,D} {3,S} {4,S}
3 O u0 p2 c0 {2,S} {4,S}
4 O u0 p2 c0 {2,S} {3,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
A B2PLYP/aug-cc-pVTZ optimization gave a "chain" that can be represented as [N-]=[N+]=[O+][O-]
instead of the cyclic structure [N-]=[N+]1OO1
""",
)

entry(
    label = "HNOH2NO",
    molecule =
"""
multiplicity 2
1 N u1 p1 c0 {2,S} {5,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {4,S}
4 N u0 p1 c0 {3,S} {6,S} {7,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
An wb97xd/def2svp conformer search was unable to optimize any of the conformer, they break down into HNO and H2NO
""",
)

entry(
    label = "HNOONH",
    molecule =
"""
multiplicity 3
1 N u1 p1 c0 {2,S} {5,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {4,S}
4 N u1 p1 c0 {3,S} {6,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
A CBS-QB3 job was unable to optimize this structure, got two HNO fragments
(one of them looks like a TS with the H a bit detached)
""",
)

entry(
    label = "ONH2ONH",
    molecule =
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,S} {5,S} {6,S}
3 O u0 p2 c0 {2,S} {4,S}
4 N u1 p1 c0 {3,S} {7,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
A CBS-QB3 job was unable to optimize this structure, got HNO + H2NO
""",
)

entry(
    label = "ONH2NO",
    molecule =
"""
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,S} {5,S} {6,S}
3 N u0 p1 c0 {2,S} {4,D}
4 O u0 p2 c0 {3,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
A CBS-QB3 job was unable to optimize this structure, got NO + H2NO
""",
)

entry(
    label = "HNONOH(T)",
    molecule =
"""
multiplicity 3
1 N u1 p1 c0 {2,S} {5,S}
2 O u0 p2 c0 {1,S} {3,S}
3 N u1 p1 c0 {2,S} {4,S}
4 O u0 p2 c0 {3,S} {6,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
A CBS-QB3 job was unable to optimize this structure, got NO + H2NO
""",
)

entry(
    label = "HNNH2OO",
    molecule =
"""
multiplicity 2
1 N u0 p2 c-1 {2,S} {5,S}
2 N u0 p0 c+1 {1,S} {3,S} {6,S} {7,S}
3 O u0 p2 c0 {2,S} {4,S}
4 O u1 p2 c0 {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
An wb97xd/def2svp conformer search was unable to optimize any of the conformer, they break down into O2 + H2NN
""",
)

entry(
    label = "NNH2OO",
    molecule =
"""
multiplicity 3
1 N u1 p2 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,S} {5,S} {6,S}
3 O u0 p2 c0 {2,S} {4,S}
4 O u1 p2 c0 {3,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
An wb97xd/def2svp conformer search was unable to optimize any of the conformer, they break down into O2 + H2NN
""",
)

entry(
    label = "NNH2OOH",
    molecule =
"""
multiplicity 2
1 N u1 p2 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,S} {5,S} {6,S}
3 O u0 p2 c0 {2,S} {4,S}
4 O u0 p2 c0 {3,S} {7,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
A CBS-QB3 job was unable to optimize this structure, got HO2 + H2NO
""",
)

entry(
    label = "NNH2OH",
    molecule =
"""
multiplicity 2
1 N u1 p2 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,S} {4,S} {5,S}
3 O u0 p2 c0 {2,S} {6,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
A CBS-QB3 job was unable to optimize this structure, got H2O + HNN
""",
)

entry(
    label = "NNHOO",
    molecule =
"""
multiplicity 2
1 N u0 p2 c-1 {2,D}
2 N u0 p0 c+1 {1,D} {3,S} {5,S}
3 O u0 p2 c0 {2,S} {4,S}
4 O u1 p2 c0 {3,S}
5 H u0 p0 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
An wb97xd/def2svp conformer search was unable to optimize any of the conformer, they break down into O2 + HNN
""",
)

entry(
    label = "NNHOOH",
    molecule =
"""
1 N u0 p2 c-1 {2,D}
2 N u0 p0 c+1 {1,D} {3,S} {5,S}
3 O u0 p2 c0 {2,S} {4,S}
4 O u0 p2 c0 {3,S} {6,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
A CBS-QB3 job was unable to optimize this structure, got N2, H2O and O
""",
)

entry(
    label = "NcNHOO",
    molecule =
"""
multiplicity 2
1 N u1 p2 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,S} {4,S} {5,S}
3 O u0 p2 c0 {2,S} {4,S}
4 O u0 p2 c0 {2,S} {3,S}
5 H u0 p0 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
A CBS-QB3 job was unable to optimize this structure, got O2 and HNN
""",
)

entry(
    label = "NHcNOO",
    molecule =
"""
multiplicity 2
1 N u1 p1 c0 {2,S} {5,S}
2 N u0 p1 c0 {1,S} {3,S} {4,S}
3 O u0 p2 c0 {2,S} {4,S}
4 O u0 p2 c0 {2,S} {3,S}
5 H u0 p0 c0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
A CBS-QB3 job was unable to optimize this structure, got O2 and HNN
""",
)

entry(
    label = "NH2NOOH",
    molecule =
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {5,S} {6,S}
2 N u1 p1 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {4,S}
4 O u0 p2 c0 {3,S} {7,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
A CBS-QB3 job was unable to optimize this structure, got OH and NH2NO
""",
)

entry(
    label = "NNHOO",
    molecule =
"""
multiplicity 3
1 N u0 p1 c0 {2,S} {5,S} {6,S}
2 O u0 p2 c0 {1,S} {3,S}
3 N u1 p1 c0 {2,S} {4,S}
4 O u1 p2 c0 {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
An wb97xd/def2svp conformer search was unable to optimize any of the conformer, they break down into NO + H2NO
""",
)

entry(
    label = "NHONOH",
    molecule =
"""
multiplicity 3
1 N u1 p1 c0 {2,S} {5,S}
2 O u0 p2 c0 {1,S} {3,S}
3 N u1 p1 c0 {2,S} {4,S}
4 O u0 p2 c0 {3,S} {6,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
A CBS-QB3 job was unable to optimize this structure, got NO + H2NO
""",
)

entry(
    label = "ONH2NO(T)",
    molecule =
"""
multiplicity 3
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,S} {5,S} {6,S}
3 N u1 p1 c0 {2,S} {4,S}
4 O u1 p2 c0 {3,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
A CBS-QB3 job was unable to optimize this structure, got NO + H2NO
""",
)

entry(
    label = "NHNH2OO",
    molecule =
"""
multiplicity 2
1 N u0 p2 c-1 {2,S} {5,S}
2 N u0 p0 c+1 {1,S} {3,S} {6,S} {7,S}
3 O u0 p2 c0 {2,S} {4,S}
4 O u1 p2 c0 {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
An wb97xd/def2svp conformer search was unable to optimize any of the conformer, they break down into O2 + N2H3
""",
)

entry(
    label = "NH3NO",
    molecule =
"""
multiplicity 2
1 N u0 p2 c-1 {2,S} {3,S}
2 N u0 p0 c+1 {1,S} {4,S} {5,S} {6,S}
3 O u1 p2 c0 {1,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
An wb97xd/def2svp conformer search was unable to optimize any of the conformer, they break down into NH3 + NO
""",
)

entry(
    label = "HONH2NOH",
    molecule =
"""
1 O u0 p2 c0 {2,S} {5,S}
2 N u0 p0 c+1 {1,S} {3,S} {6,S} {7,S}
3 N u0 p2 c-1 {2,S} {4,S}
4 O u0 p2 c0 {3,S} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
A CBS-QB3 job was unable to optimize this structure, got H2O + HNNOH
""",
)

entry(
    label = "NNHOO",
    molecule =
"""
multiplicity 2
1 N u0 p2 c-1 {2,D}
2 N u0 p0 c+1 {1,D} {3,S} {5,S}
3 O u0 p2 c0 {2,S} {4,S}
4 O u1 p2 c0 {3,S}
5 H u0 p0 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
An wb97xd/def2svp conformer search was unable to optimize any of the conformer, they break down into N2 + HO2
""",
)

entry(
    label = "HONH2NO",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {5,S}
2 N u0 p0 c+1 {1,S} {3,S} {6,S} {7,S}
3 N u0 p2 c-1 {2,S} {4,S}
4 O u1 p2 c0 {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
An wb97xd/def2svp conformer search was unable to optimize any of the conformer, they break down into NO + H2NOH
""",
)

entry(
    label = "N3H(T)",
    molecule =
"""
multiplicity 3
1 N u1 p1 c0 {2,S} {4,S}
2 N u0 p1 c0 {1,S} {3,D}
3 N u1 p1 c0 {2,D}
4 H u0 p0 c0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
An wb97xd/def2svp conformer search was unable to optimize any of the conformer, they break down into N2 and NH
""",
)

entry(
    label = "[O]ON=[N](T)",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 N u0 p1 c0 {1,S} {4,D}
4 N u1 p1 c0 {3,D}
""",
    shortDesc = u"""""",
    longDesc =
u"""
An wb97xd/def2svp conformer search was unable to optimize any of the conformer, they break down into N2 and O2
""",
)

entry(
    label = "OON=[N]",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {5,S}
3 N u0 p1 c0 {1,S} {4,D}
4 N u1 p1 c0 {3,D}
5 H u0 p0 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
A CBS-QB3 job was unable to optimize this structure, got N2 and HO2
""",
)

entry(
    label = "NOON=[N]",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 N u0 p1 c0 {1,S} {6,S} {7,S}
4 N u0 p1 c0 {2,S} {5,D}
5 N u1 p1 c0 {4,D}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
An wb97xd/def2svp conformer search was unable to optimize any of the conformer, they break down into N2 and NH2OO
""",
)

entry(
    label = "NON=[N]",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 N u0 p1 c0 {1,S} {5,S} {6,S}
3 N u0 p1 c0 {1,S} {4,D}
4 N u1 p1 c0 {3,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
An wb97xd/def2svp conformer search was unable to optimize any of the conformer, they break down into N2 and NH2O
""",
)

entry(
    label = "[O-][NH2p]N=[N]",
    molecule =
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,S} {5,S} {6,S}
3 N u0 p1 c0 {2,S} {4,D}
4 N u1 p1 c0 {3,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
An wb97xd/def2svp conformer search was unable to optimize any of the conformer, they break down into N2 and NH2O
""",
)

entry(
    label = "[O]NN=[N]",
    molecule =
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 N u0 p1 c0 {1,S} {3,S} {5,S}
3 N u0 p1 c0 {2,S} {4,D}
4 N u1 p1 c0 {3,D}
5 H u0 p0 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
A CBS-QB3 job was unable to optimize this structure, got N2 and HNO
""",
)

entry(
    label = "[NH]ON=[N]",
    molecule =
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,S} {5,S} {6,S}
3 N u0 p1 c0 {2,S} {4,D}
4 N u1 p1 c0 {3,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
An wb97xd/def2svp conformer search was unable to optimize any of the conformer, they break down into N2 and NH2O
""",
)

entry(
    label = "N2H3NO2",
    molecule =
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u0 p1 c0 {1,S} {3,S} {5,S}
3 N u0 p0 c+1 {2,S} {4,S} {6,S} {7,S}
4 N u0 p1 c0 {3,S} {8,S} {9,S}
5 O u1 p2 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
A b2plypd3/aug-cc-pvtz optimization did not gibe a single covalently-bonded species, it breaks down into N2H4 and NO2
""",
)

entry(
    label = "[NH]OON",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 N u0 p1 c0 {1,S} {5,S} {6,S}
4 N u1 p1 c0 {2,S} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
An wb97xd/def2svp conformer search was unable to optimize any of the conformer, they break down into HNO and H2NO
""",
)

entry(
    label = "[O-][NH2p]O[NH]",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p3 c-1 {3,S}
3 N u0 p0 c+1 {1,S} {2,S} {5,S} {6,S}
4 N u1 p1 c0 {1,S} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
A CBS-QB3 job was unable to optimize this structure, got HNO and H2NO
""",
)

entry(
    label = "[NH]OO[NH]",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 N u1 p1 c0 {1,S} {5,S}
4 N u1 p1 c0 {2,S} {6,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
A CBS-QB3 job was unable to optimize this structure, got HNO and HNO
""",
)

entry(
    label = "[N]=NN=O",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 N u0 p1 c0 {1,D} {3,S}
3 N u0 p1 c0 {2,S} {4,D}
4 N u1 p1 c0 {3,D}
""",
    shortDesc = u"""""",
    longDesc =
u"""
A CBS-QB3 job was unable to optimize this structure, got N2 and NO
""",
)

entry(
    label = "O[N]N=[N]",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {2,S} {5,S}
2 N u1 p1 c0 {1,S} {3,S}
3 N u0 p1 c0 {2,S} {4,D}
4 N u1 p1 c0 {3,D}
5 H u0 p0 c0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
A CBS-QB3 job was unable to optimize this structure, got N2 and HON
""",
)

entry(
    label = "[N]NN=O",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {3,D}
2 N u0 p1 c0 {3,S} {4,S} {5,S}
3 N u0 p1 c0 {1,D} {2,S}
4 N u2 p1 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
A CBS-QB3 job was unable to optimize this structure, got NO and HNN
""",
)

entry(
    label = "[N]=NON=O",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {3,D}
3 N u0 p1 c0 {1,S} {2,D}
4 N u0 p1 c0 {1,S} {5,D}
5 N u1 p1 c0 {4,D}
""",
    shortDesc = u"""""",
    longDesc =
u"""
A CBS-QB3 job was unable to optimize this structure, got N2 and NO2
""",
)

entry(
    label = "[O-][N+](=O)N=[N]",
    molecule =
"""
multiplicity 2
1 O u0 p3 c-1 {3,S}
2 O u0 p2 c0 {3,D}
3 N u0 p0 c+1 {1,S} {2,D} {4,S}
4 N u0 p1 c0 {3,S} {5,D}
5 N u1 p1 c0 {4,D}
""",
    shortDesc = u"""""",
    longDesc =
u"""
A CBS-QB3 job was unable to optimize this structure, got N2 and NO2
""",
)

entry(
    label = "NO[N][O]",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {3,S} {4,S}
2 O u1 p2 c0 {4,S}
3 N u0 p1 c0 {1,S} {5,S} {6,S}
4 N u1 p1 c0 {1,S} {2,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
An wb97xd/def2svp conformer search was unable to optimize any of the conformer, they break down into NO and H2NO
""",
)

entry(
    label = "[NH]O[N]O",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {3,S} {5,S}
3 N u1 p1 c0 {1,S} {2,S}
4 N u1 p1 c0 {1,S} {6,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
A CBS-QB3 job was unable to optimize this structure, got NO and H2NO
""",
)

entry(
    label = "[O-][NH+](N=[N])O",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {7,S}
2 O u0 p3 c-1 {3,S}
3 N u0 p0 c+1 {1,S} {2,S} {4,S} {6,S}
4 N u0 p1 c0 {3,S} {5,D}
5 N u1 p1 c0 {4,D}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
An wb97xd/def2svp conformer search was unable to optimize any of the conformer, they break down into N2 and HONHO
""",
)

entry(
    label = "ONON=[N]",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {3,S} {7,S}
3 N u0 p1 c0 {1,S} {2,S} {6,S}
4 N u0 p1 c0 {1,S} {5,D}
5 N u1 p1 c0 {4,D}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[O-][NH+]([O])[NH]",
    molecule =
"""
multiplicity 3
1 O u1 p2 c0 {3,S}
2 O u0 p3 c-1 {3,S}
3 N u0 p0 c+1 {1,S} {2,S} {4,S} {5,S}
4 N u1 p1 c0 {3,S} {6,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "ONN=[N]",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {6,S}
2 N u0 p1 c0 {1,S} {3,S} {5,S}
3 N u0 p1 c0 {2,S} {4,D}
4 N u1 p1 c0 {3,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[NH-][NH2+]O[O]",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 N u0 p0 c+1 {1,S} {4,S} {5,S} {6,S}
4 N u0 p2 c-1 {3,S} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[NH-][NH2+]O[NH]",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 N u0 p0 c+1 {1,S} {3,S} {5,S} {6,S}
3 N u0 p2 c-1 {2,S} {7,S}
4 N u1 p1 c0 {1,S} {8,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[NH-][NH2+]N[O]",
    molecule =
"""
multiplicity 2
1 O u1 p2 c0 {3,S}
2 N u0 p0 c+1 {3,S} {4,S} {5,S} {6,S}
3 N u0 p1 c0 {1,S} {2,S} {7,S}
4 N u0 p2 c-1 {2,S} {8,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "NNO[N][O]",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {3,S} {5,S}
2 O u1 p2 c0 {5,S}
3 N u0 p1 c0 {1,S} {4,S} {6,S}
4 N u0 p1 c0 {3,S} {7,S} {8,S}
5 N u1 p1 c0 {1,S} {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[O]N([NH2+][NH-])[O]",
    molecule =
"""
multiplicity 3
1 O u1 p2 c0 {4,S}
2 O u1 p2 c0 {4,S}
3 N u0 p0 c+1 {4,S} {5,S} {6,S} {7,S}
4 N u0 p1 c0 {1,S} {2,S} {3,S}
5 N u0 p2 c-1 {3,S} {8,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {5,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[NH-][NH2+]ON[O]",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 O u1 p2 c0 {4,S}
3 N u0 p0 c+1 {1,S} {5,S} {6,S} {7,S}
4 N u0 p1 c0 {1,S} {2,S} {8,S}
5 N u0 p2 c-1 {3,S} {9,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {5,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[NH-][NH2+][NH+]([O])[O-]",
    molecule =
"""
multiplicity 2
1 O u1 p2 c0 {4,S}
2 O u0 p3 c-1 {4,S}
3 N u0 p0 c+1 {4,S} {5,S} {6,S} {7,S}
4 N u0 p0 c+1 {1,S} {2,S} {3,S} {8,S}
5 N u0 p2 c-1 {3,S} {9,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {5,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[NH-][NH+]O[O]",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 N u1 p0 c+1 {1,S} {4,S} {5,S}
4 N u0 p2 c-1 {3,S} {6,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[NH]NOON",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 N u0 p1 c0 {1,S} {5,S} {6,S}
4 N u0 p1 c0 {2,S} {7,S} {8,S}
5 N u1 p1 c0 {3,S} {9,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {5,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[NH]ON[NH]",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {2,S} {4,S}
2 N u0 p1 c0 {1,S} {3,S} {5,S}
3 N u1 p1 c0 {2,S} {6,S}
4 N u1 p1 c0 {1,S} {7,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-]=[NH+]O[O]",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 N u0 p0 c+1 {1,S} {4,D} {5,S}
4 N u0 p2 c-1 {3,D}
5 H u0 p0 c0 {3,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-]=[NH+]O[NH]",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 N u0 p0 c+1 {1,S} {4,D} {5,S}
3 N u1 p1 c0 {1,S} {6,S}
4 N u0 p2 c-1 {2,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-]=[NH+]N[O]",
    molecule =
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 N u0 p1 c0 {1,S} {3,S} {6,S}
3 N u0 p0 c+1 {2,S} {4,D} {5,S}
4 N u0 p2 c-1 {3,D}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[O][N]ON=N",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {3,S} {4,S}
2 O u1 p2 c0 {4,S}
3 N u0 p1 c0 {1,S} {5,D}
4 N u1 p1 c0 {1,S} {2,S}
5 N u0 p1 c0 {3,D} {6,S}
6 H u0 p0 c0 {5,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[O-][N+](=O)[N][NH]",
    molecule =
"""
multiplicity 3
1 O u0 p3 c-1 {3,S}
2 O u0 p2 c0 {3,D}
3 N u0 p0 c+1 {1,S} {2,D} {4,S}
4 N u1 p1 c0 {3,S} {5,S}
5 N u1 p1 c0 {4,S} {6,S}
6 H u0 p0 c0 {5,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-]=[NH+]O[N][O]",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {3,S} {4,S}
2 O u1 p2 c0 {4,S}
3 N u0 p0 c+1 {1,S} {5,D} {6,S}
4 N u1 p1 c0 {1,S} {2,S}
5 N u0 p2 c-1 {3,D}
6 H u0 p0 c0 {3,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[O]NON=N",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 O u1 p2 c0 {3,S}
3 N u0 p1 c0 {1,S} {2,S} {6,S}
4 N u0 p1 c0 {1,S} {5,D}
5 N u0 p1 c0 {4,D} {7,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {5,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-]=[NH+]ON[O]",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 O u1 p2 c0 {3,S}
3 N u0 p1 c0 {1,S} {2,S} {7,S}
4 N u0 p0 c+1 {1,S} {5,D} {6,S}
5 N u0 p2 c-1 {4,D}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {3,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[O-][NH+]([NH+]=[N-])[O]",
    molecule =
"""
multiplicity 2
1 O u1 p2 c0 {3,S}
2 O u0 p3 c-1 {3,S}
3 N u0 p0 c+1 {1,S} {2,S} {4,S} {6,S}
4 N u0 p0 c+1 {3,S} {5,D} {7,S}
5 N u0 p2 c-1 {4,D}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-][NH+]1OO1",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {3,S}
3 N u0 p0 c+1 {1,S} {2,S} {4,S} {5,S}
4 N u1 p2 c-1 {3,S}
5 H u0 p0 c0 {3,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "N[N]OO",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {7,S}
3 N u0 p1 c0 {4,S} {5,S} {6,S}
4 N u1 p1 c0 {1,S} {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "NO[N][NH]",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {2,S} {3,S}
2 N u0 p1 c0 {1,S} {5,S} {6,S}
3 N u1 p1 c0 {1,S} {4,S}
4 N u1 p1 c0 {3,S} {7,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-][NH2+]O[NH]",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {2,S} {3,S}
2 N u0 p0 c+1 {1,S} {4,S} {5,S} {6,S}
3 N u1 p1 c0 {1,S} {7,S}
4 N u1 p2 c-1 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[O-][NH2+][N][NH]",
    molecule =
"""
multiplicity 3
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,S} {5,S} {6,S}
3 N u1 p1 c0 {2,S} {4,S}
4 N u1 p1 c0 {3,S} {7,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "NN[N][O]",
    molecule =
"""
multiplicity 3
1 O u1 p2 c0 {4,S}
2 N u0 p1 c0 {3,S} {4,S} {5,S}
3 N u0 p1 c0 {2,S} {6,S} {7,S}
4 N u1 p1 c0 {1,S} {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[NH-][NH2+][N][O]",
    molecule =
"""
multiplicity 3
1 O u1 p2 c0 {3,S}
2 N u0 p0 c+1 {3,S} {4,S} {5,S} {6,S}
3 N u1 p1 c0 {1,S} {2,S}
4 N u0 p2 c-1 {2,S} {7,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-][NH2+]N[O]",
    molecule =
"""
multiplicity 3
1 O u1 p2 c0 {3,S}
2 N u0 p0 c+1 {3,S} {4,S} {5,S} {6,S}
3 N u0 p1 c0 {1,S} {2,S} {7,S}
4 N u1 p2 c-1 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-][NH2+]O[O]",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 N u0 p0 c+1 {1,S} {4,S} {5,S} {6,S}
4 N u1 p2 c-1 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-][NH2+]OO",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 N u0 p0 c+1 {1,S} {5,S} {6,S} {7,S}
4 N u0 p1 c0 {2,S} {8,S} {9,S}
5 N u1 p2 c-1 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-][NH2+]OON",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 N u0 p0 c+1 {1,S} {5,S} {6,S} {7,S}
4 N u0 p1 c0 {2,S} {8,S} {9,S}
5 N u1 p2 c-1 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "N[N]OON",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 N u0 p1 c0 {5,S} {6,S} {7,S}
4 N u0 p1 c0 {1,S} {8,S} {9,S}
5 N u1 p1 c0 {2,S} {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-][NH2+]ON",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 N u0 p0 c+1 {1,S} {4,S} {5,S} {6,S}
3 N u0 p1 c0 {1,S} {7,S} {8,S}
4 N u1 p2 c-1 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-][NH2+][NH2+][O-]",
    molecule =
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,S} {5,S} {6,S}
3 N u0 p0 c+1 {2,S} {4,S} {7,S} {8,S}
4 N u1 p2 c-1 {3,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-][NH2+]O",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {6,S}
2 N u0 p0 c+1 {1,S} {3,S} {4,S} {5,S}
3 N u1 p2 c-1 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-][NH2+]N=O",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {3,D}
2 N u0 p0 c+1 {3,S} {4,S} {5,S} {6,S}
3 N u0 p1 c0 {1,D} {2,S}
4 N u1 p2 c-1 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-][NH2+]ON=O",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {4,D}
3 N u0 p0 c+1 {1,S} {5,S} {6,S} {7,S}
4 N u0 p1 c0 {1,S} {2,D}
5 N u1 p2 c-1 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "N[N]ON=O",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {5,S}
2 O u0 p2 c0 {5,D}
3 N u0 p1 c0 {4,S} {6,S} {7,S}
4 N u1 p1 c0 {1,S} {3,S}
5 N u0 p1 c0 {1,S} {2,D}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-][NH2+][N+](=O)[O-]",
    molecule =
"""
multiplicity 2
1 O u0 p3 c-1 {4,S}
2 O u0 p2 c0 {4,D}
3 N u0 p0 c+1 {4,S} {5,S} {6,S} {7,S}
4 N u0 p0 c+1 {1,S} {2,D} {3,S}
5 N u1 p2 c-1 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[O-][N+](=O)[N]N",
    molecule =
"""
multiplicity 2
1 O u0 p3 c-1 {4,S}
2 O u0 p2 c0 {4,D}
3 N u0 p1 c0 {5,S} {6,S} {7,S}
4 N u0 p0 c+1 {1,S} {2,D} {5,S}
5 N u1 p1 c0 {3,S} {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-][NH2+][NH+](O)[O-]",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {9,S}
2 O u0 p3 c-1 {3,S}
3 N u0 p0 c+1 {1,S} {2,S} {4,S} {6,S}
4 N u0 p0 c+1 {3,S} {5,S} {7,S} {8,S}
5 N u1 p2 c-1 {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-][NH2+]ONO",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {4,S} {9,S}
3 N u0 p0 c+1 {1,S} {5,S} {6,S} {7,S}
4 N u0 p1 c0 {1,S} {2,S} {8,S}
5 N u1 p2 c-1 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-][NH2+]NO",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {8,S}
2 N u0 p0 c+1 {3,S} {4,S} {5,S} {6,S}
3 N u0 p1 c0 {1,S} {2,S} {7,S}
4 N u1 p2 c-1 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "N[N]ON[O]",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {4,S} {5,S}
2 O u1 p2 c0 {4,S}
3 N u0 p1 c0 {5,S} {6,S} {7,S}
4 N u0 p1 c0 {1,S} {2,S} {8,S}
5 N u1 p1 c0 {1,S} {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-][NH2+]ON[O]",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {3,S} {4,S}
2 O u1 p2 c0 {4,S}
3 N u0 p0 c+1 {1,S} {5,S} {6,S} {7,S}
4 N u0 p1 c0 {1,S} {2,S} {8,S}
5 N u1 p2 c-1 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-][NH2+][NH+]([O])[O-]",
    molecule =
"""
multiplicity 3
1 O u1 p2 c0 {4,S}
2 O u0 p3 c-1 {4,S}
3 N u0 p0 c+1 {4,S} {5,S} {6,S} {7,S}
4 N u0 p0 c+1 {1,S} {2,S} {3,S} {8,S}
5 N u1 p2 c-1 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-]=[N+](ON)[O]",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 O u1 p2 c0 {4,S}
3 N u0 p1 c0 {1,S} {6,S} {7,S}
4 N u0 p0 c+1 {1,S} {2,S} {5,D}
5 N u0 p2 c-1 {4,D}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[O-][NH2+]ON=[N]",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p3 c-1 {3,S}
3 N u0 p0 c+1 {1,S} {2,S} {6,S} {7,S}
4 N u0 p1 c0 {1,S} {5,D}
5 N u1 p1 c0 {4,D}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-][N+](=O)[NH2+][O-]",
    molecule =
"""
multiplicity 2
1 O u0 p3 c-1 {3,S}
2 O u0 p2 c0 {4,D}
3 N u0 p0 c+1 {1,S} {4,S} {6,S} {7,S}
4 N u0 p0 c+1 {2,D} {3,S} {5,S}
5 N u1 p2 c-1 {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[O-][NH2+][N]N=O",
    molecule =
"""
multiplicity 2
1 O u0 p3 c-1 {3,S}
2 O u0 p2 c0 {5,D}
3 N u0 p0 c+1 {1,S} {4,S} {6,S} {7,S}
4 N u1 p1 c0 {3,S} {5,S}
5 N u0 p1 c0 {2,D} {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "O=N[N+](=O)[N-]",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {3,D}
2 O u0 p2 c0 {4,D}
3 N u0 p0 c+1 {1,D} {4,S} {5,S}
4 N u0 p1 c0 {2,D} {3,S}
5 N u1 p2 c-1 {3,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-][N+](=O)NO",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {7,S}
2 O u0 p2 c0 {4,D}
3 N u0 p1 c0 {1,S} {4,S} {6,S}
4 N u0 p0 c+1 {2,D} {3,S} {5,S}
5 N u1 p2 c-1 {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-]OO[NH2+]",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 N u1 p0 c+1 {1,S} {5,S} {6,S}
4 N u1 p2 c-1 {2,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[NH]N1OO1",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {3,S}
3 N u0 p1 c0 {1,S} {2,S} {4,S}
4 N u1 p1 c0 {3,S} {5,S}
5 H u0 p0 c0 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N]=NN(O)[O]",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {3,S} {6,S}
2 O u1 p2 c0 {3,S}
3 N u0 p1 c0 {1,S} {2,S} {4,S}
4 N u0 p1 c0 {3,S} {5,D}
5 N u1 p1 c0 {4,D}
6 H u0 p0 c0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "O[N]ON=[N]",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {3,S} {6,S}
3 N u1 p1 c0 {1,S} {2,S}
4 N u0 p1 c0 {1,S} {5,D}
5 N u1 p1 c0 {4,D}
6 H u0 p0 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[NH-][NH2+]O[N]O",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {5,S}
2 O u0 p2 c0 {5,S} {9,S}
3 N u0 p0 c+1 {1,S} {4,S} {6,S} {7,S}
4 N u0 p2 c-1 {3,S} {8,S}
5 N u1 p1 c0 {1,S} {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[O]N([NH2+][NH-])O",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {9,S}
2 O u1 p2 c0 {4,S}
3 N u0 p0 c+1 {4,S} {5,S} {6,S} {7,S}
4 N u0 p1 c0 {1,S} {2,S} {3,S}
5 N u0 p2 c-1 {3,S} {8,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[NH]NO[N]O",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {4,S} {8,S}
3 N u0 p1 c0 {1,S} {5,S} {6,S}
4 N u1 p1 c0 {1,S} {2,S}
5 N u1 p1 c0 {3,S} {7,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "O[N]ON=N",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {3,S} {6,S}
3 N u1 p1 c0 {1,S} {2,S}
4 N u0 p1 c0 {1,S} {5,D}
5 N u0 p1 c0 {4,D} {7,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {5,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-]=[NH+]O[N]O",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {4,S} {7,S}
3 N u0 p0 c+1 {1,S} {5,D} {6,S}
4 N u1 p1 c0 {1,S} {2,S}
5 N u0 p2 c-1 {3,D}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[O]N([NH+]=[N-])O",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {7,S}
2 O u1 p2 c0 {3,S}
3 N u0 p1 c0 {1,S} {2,S} {4,S}
4 N u0 p0 c+1 {3,S} {5,D} {6,S}
5 N u0 p2 c-1 {4,D}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-][NH2+]O[N]O",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {4,S} {8,S}
3 N u0 p0 c+1 {1,S} {5,S} {6,S} {7,S}
4 N u1 p1 c0 {1,S} {2,S}
5 N u1 p2 c-1 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[O]N([NH2+][N-])O",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {4,S} {8,S}
2 O u1 p2 c0 {4,S}
3 N u0 p0 c+1 {4,S} {5,S} {6,S} {7,S}
4 N u0 p1 c0 {1,S} {2,S} {3,S}
5 N u1 p2 c-1 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[O]NON=[N]",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {3,S} {4,S}
2 O u1 p2 c0 {3,S}
3 N u0 p1 c0 {1,S} {2,S} {6,S}
4 N u0 p1 c0 {1,S} {5,D}
5 N u1 p1 c0 {4,D}
6 H u0 p0 c0 {3,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "OO[N]N=[N]",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {6,S}
3 N u1 p1 c0 {1,S} {4,S}
4 N u0 p1 c0 {3,S} {5,D}
5 N u1 p1 c0 {4,D}
6 H u0 p0 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[O-][NH+](N=[N])[O]",
    molecule =
"""
multiplicity 3
1 O u1 p2 c0 {3,S}
2 O u0 p3 c-1 {3,S}
3 N u0 p0 c+1 {1,S} {2,S} {4,S} {6,S}
4 N u0 p1 c0 {3,S} {5,D}
5 N u1 p1 c0 {4,D}
6 H u0 p0 c0 {3,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N]1ON[N]O1",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {3,S} {5,S}
2 O u0 p2 c0 {4,S} {5,S}
3 N u0 p1 c0 {1,S} {4,S} {6,S}
4 N u1 p1 c0 {2,S} {3,S}
5 N u1 p1 c0 {1,S} {2,S}
6 H u0 p0 c0 {3,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "NON([O])N",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {5,S}
2 O u1 p2 c0 {3,S}
3 N u0 p1 c0 {1,S} {2,S} {4,S}
4 N u0 p1 c0 {3,S} {6,S} {7,S}
5 N u0 p1 c0 {1,S} {8,S} {9,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {5,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[NH]ON([O])N",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {3,S} {5,S}
2 O u1 p2 c0 {3,S}
3 N u0 p1 c0 {1,S} {2,S} {4,S}
4 N u0 p1 c0 {3,S} {6,S} {7,S}
5 N u1 p1 c0 {1,S} {8,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[NH]NON[O]",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {3,S} {4,S}
2 O u1 p2 c0 {4,S}
3 N u0 p1 c0 {1,S} {5,S} {6,S}
4 N u0 p1 c0 {1,S} {2,S} {7,S}
5 N u1 p1 c0 {3,S} {8,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[NH][N]ONO",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {3,S} {7,S}
3 N u0 p1 c0 {1,S} {2,S} {6,S}
4 N u1 p1 c0 {1,S} {5,S}
5 N u1 p1 c0 {4,S} {8,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {5,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N]NONO",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {3,S} {8,S}
3 N u0 p1 c0 {1,S} {2,S} {6,S}
4 N u0 p1 c0 {1,S} {5,S} {7,S}
5 N u2 p1 c0 {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[NH][N]N(O)O",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {3,S} {6,S}
2 O u0 p2 c0 {3,S} {7,S}
3 N u0 p1 c0 {1,S} {2,S} {4,S}
4 N u1 p1 c0 {3,S} {5,S}
5 N u1 p1 c0 {4,S} {8,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {5,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[NH]N[N]OO",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {8,S}
3 N u0 p1 c0 {4,S} {5,S} {6,S}
4 N u1 p1 c0 {1,S} {3,S}
5 N u1 p1 c0 {3,S} {7,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[O-][NH+]([N][NH])O",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {3,S} {7,S}
2 O u0 p3 c-1 {3,S}
3 N u0 p0 c+1 {1,S} {2,S} {4,S} {6,S}
4 N u1 p1 c0 {3,S} {5,S}
5 N u1 p1 c0 {4,S} {8,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {5,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-]([NH3+])[O]",
    molecule =
"""
multiplicity 2
1 O u1 p2 c0 {3,S}
2 N u0 p0 c+1 {3,S} {4,S} {5,S} {6,S}
3 N u0 p2 c-1 {1,S} {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[O-][NH2+]O[N]N",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {5,S}
2 O u0 p3 c-1 {3,S}
3 N u0 p0 c+1 {1,S} {2,S} {6,S} {7,S}
4 N u0 p1 c0 {5,S} {8,S} {9,S}
5 N u1 p1 c0 {1,S} {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[O-][NH2+]N([O])N",
    molecule =
"""
multiplicity 2
1 O u0 p3 c-1 {3,S}
2 O u1 p2 c0 {4,S}
3 N u0 p0 c+1 {1,S} {4,S} {6,S} {7,S}
4 N u0 p1 c0 {2,S} {3,S} {5,S}
5 N u0 p1 c0 {4,S} {8,S} {9,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {5,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "N[N]OO[NH]",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 N u0 p1 c0 {4,S} {6,S} {7,S}
4 N u1 p1 c0 {1,S} {3,S}
5 N u1 p1 c0 {2,S} {8,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {5,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "O[NH2+][N-][O]",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {7,S}
2 O u1 p2 c0 {4,S}
3 N u0 p0 c+1 {1,S} {4,S} {5,S} {6,S}
4 N u0 p2 c-1 {2,S} {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-]([NH2+]N=O)[O]",
    molecule =
"""
multiplicity 2
1 O u1 p2 c0 {4,S}
2 O u0 p2 c0 {5,D}
3 N u0 p0 c+1 {4,S} {5,S} {6,S} {7,S}
4 N u0 p2 c-1 {1,S} {3,S}
5 N u0 p1 c0 {2,D} {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[O][N-][NH2+]NO",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {9,S}
2 O u1 p2 c0 {5,S}
3 N u0 p0 c+1 {4,S} {5,S} {6,S} {7,S}
4 N u0 p1 c0 {1,S} {3,S} {8,S}
5 N u0 p2 c-1 {2,S} {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "NNOO[NH]",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {5,S}
3 N u0 p1 c0 {1,S} {4,S} {6,S}
4 N u0 p1 c0 {3,S} {7,S} {8,S}
5 N u1 p1 c0 {2,S} {9,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {5,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N]1ON1N=O",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {5,D}
3 N u0 p1 c0 {1,S} {4,S} {5,S}
4 N u1 p1 c0 {1,S} {3,S}
5 N u0 p1 c0 {2,D} {3,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-]1N([N+]1=O)[O]",
    molecule =
"""
multiplicity 2
1 O u1 p2 c0 {3,S}
2 O u0 p2 c0 {4,D}
3 N u0 p1 c0 {1,S} {4,S} {5,S}
4 N u0 p0 c+1 {2,D} {3,S} {5,S}
5 N u0 p2 c-1 {3,S} {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-]=[N+]1ON1[O]",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 O u1 p2 c0 {3,S}
3 N u0 p1 c0 {1,S} {2,S} {4,S}
4 N u0 p0 c+1 {1,S} {3,S} {5,D}
5 N u0 p2 c-1 {4,D}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-]([N+]#N)O[O]",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 N u0 p2 c-1 {1,S} {4,S}
4 N u0 p0 c+1 {3,S} {5,T}
5 N u0 p1 c0 {4,T}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[NH]O[NH+](N)[O-]",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {5,S}
2 O u0 p3 c-1 {3,S}
3 N u0 p0 c+1 {1,S} {2,S} {4,S} {6,S}
4 N u0 p1 c0 {3,S} {7,S} {8,S}
5 N u1 p1 c0 {1,S} {9,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {5,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[NH]ON(O)N",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {5,S}
2 O u0 p2 c0 {3,S} {8,S}
3 N u0 p1 c0 {1,S} {2,S} {4,S}
4 N u0 p1 c0 {3,S} {6,S} {7,S}
5 N u1 p1 c0 {1,S} {9,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {5,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-]([NH2+]O[NH])O",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {5,S}
2 O u0 p2 c0 {4,S} {8,S}
3 N u0 p0 c+1 {1,S} {4,S} {6,S} {7,S}
4 N u0 p2 c-1 {2,S} {3,S}
5 N u1 p1 c0 {1,S} {9,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {5,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "O[N-][NH2+]N[O]",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {5,S} {9,S}
2 O u1 p2 c0 {4,S}
3 N u0 p0 c+1 {4,S} {5,S} {6,S} {7,S}
4 N u0 p1 c0 {2,S} {3,S} {8,S}
5 N u0 p2 c-1 {1,S} {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-][NH2+][N]O",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {3,S} {7,S}
2 N u0 p0 c+1 {3,S} {4,S} {5,S} {6,S}
3 N u1 p1 c0 {1,S} {2,S}
4 N u1 p2 c-1 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-][N+](=O)[N]O",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {4,S} {6,S}
2 O u0 p2 c0 {3,D}
3 N u0 p0 c+1 {2,D} {4,S} {5,S}
4 N u1 p1 c0 {1,S} {3,S}
5 N u1 p2 c-1 {3,S}
6 H u0 p0 c0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[O][N]N=NO",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {3,S} {6,S}
2 O u1 p2 c0 {5,S}
3 N u0 p1 c0 {1,S} {4,D}
4 N u0 p1 c0 {3,D} {5,S}
5 N u1 p1 c0 {2,S} {4,S}
6 H u0 p0 c0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[O-][NH+]([N]O)N",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {5,S} {9,S}
2 O u0 p3 c-1 {3,S}
3 N u0 p0 c+1 {2,S} {4,S} {5,S} {6,S}
4 N u0 p1 c0 {3,S} {7,S} {8,S}
5 N u1 p1 c0 {1,S} {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[NH]NOO[NH]",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {5,S}
3 N u0 p1 c0 {1,S} {4,S} {6,S}
4 N u1 p1 c0 {3,S} {7,S}
5 N u1 p1 c0 {2,S} {8,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[NH][N]OON",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 N u0 p1 c0 {1,S} {6,S} {7,S}
4 N u1 p1 c0 {2,S} {5,S}
5 N u1 p1 c0 {4,S} {8,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {5,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[NH]ON(O)[NH]",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {3,S} {5,S}
2 O u0 p2 c0 {3,S} {6,S}
3 N u0 p1 c0 {1,S} {2,S} {4,S}
4 N u1 p1 c0 {3,S} {7,S}
5 N u1 p1 c0 {1,S} {8,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[O-][N+](=N)O[NH]",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {5,S}
2 O u0 p3 c-1 {3,S}
3 N u0 p0 c+1 {1,S} {2,S} {4,D}
4 N u0 p1 c0 {3,D} {6,S}
5 N u1 p1 c0 {1,S} {7,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {5,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[NH]O[NH+]([NH])[O-]",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {3,S} {5,S}
2 O u0 p3 c-1 {3,S}
3 N u0 p0 c+1 {1,S} {2,S} {4,S} {6,S}
4 N u1 p1 c0 {3,S} {7,S}
5 N u1 p1 c0 {1,S} {8,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[O-][NH2+]O[N][NH]",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p3 c-1 {3,S}
3 N u0 p0 c+1 {1,S} {2,S} {6,S} {7,S}
4 N u1 p1 c0 {1,S} {5,S}
5 N u1 p1 c0 {4,S} {8,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {5,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-]([NH3+])O[N][O]",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {4,S} {5,S}
2 O u1 p2 c0 {5,S}
3 N u0 p0 c+1 {4,S} {6,S} {7,S} {8,S}
4 N u0 p2 c-1 {1,S} {3,S}
5 N u1 p1 c0 {1,S} {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[O][N]N(O)N",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {3,S} {8,S}
2 O u1 p2 c0 {5,S}
3 N u0 p1 c0 {1,S} {4,S} {5,S}
4 N u0 p1 c0 {3,S} {6,S} {7,S}
5 N u1 p1 c0 {2,S} {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[O-][NH+](N[O])[NH]",
    molecule =
"""
multiplicity 3
1 O u0 p3 c-1 {3,S}
2 O u1 p2 c0 {4,S}
3 N u0 p0 c+1 {1,S} {4,S} {5,S} {6,S}
4 N u0 p1 c0 {2,S} {3,S} {7,S}
5 N u1 p1 c0 {3,S} {8,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[O-][NH+]([N][O])N",
    molecule =
"""
multiplicity 3
1 O u0 p3 c-1 {3,S}
2 O u1 p2 c0 {5,S}
3 N u0 p0 c+1 {1,S} {4,S} {5,S} {6,S}
4 N u0 p1 c0 {3,S} {7,S} {8,S}
5 N u1 p1 c0 {2,S} {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[O-][NH2+]N([O])[NH]",
    molecule =
"""
multiplicity 3
1 O u0 p3 c-1 {3,S}
2 O u1 p2 c0 {4,S}
3 N u0 p0 c+1 {1,S} {4,S} {6,S} {7,S}
4 N u0 p1 c0 {2,S} {3,S} {5,S}
5 N u1 p1 c0 {4,S} {8,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {5,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-][N+](=O)N[O]",
    molecule =
"""
multiplicity 3
1 O u1 p2 c0 {3,S}
2 O u0 p2 c0 {4,D}
3 N u0 p1 c0 {1,S} {4,S} {6,S}
4 N u0 p0 c+1 {2,D} {3,S} {5,S}
5 N u1 p2 c-1 {4,S}
6 H u0 p0 c0 {3,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[O][N-][NH2+]N[O]",
    molecule =
"""
multiplicity 3
1 O u1 p2 c0 {4,S}
2 O u1 p2 c0 {5,S}
3 N u0 p0 c+1 {4,S} {5,S} {6,S} {7,S}
4 N u0 p1 c0 {1,S} {3,S} {8,S}
5 N u0 p2 c-1 {2,S} {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-][N+](=N)OO",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {7,S}
3 N u0 p0 c+1 {1,S} {4,D} {5,S}
4 N u0 p1 c0 {3,D} {6,S}
5 N u1 p2 c-1 {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "ONN1[N]O1",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {5,S}
2 O u0 p2 c0 {4,S} {7,S}
3 N u0 p1 c0 {1,S} {4,S} {5,S}
4 N u0 p1 c0 {2,S} {3,S} {6,S}
5 N u1 p1 c0 {1,S} {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[NH]N(N=O)[O]",
    molecule =
"""
multiplicity 3
1 O u1 p2 c0 {3,S}
2 O u0 p2 c0 {5,D}
3 N u0 p1 c0 {1,S} {4,S} {5,S}
4 N u1 p1 c0 {3,S} {6,S}
5 N u0 p1 c0 {2,D} {3,S}
6 H u0 p0 c0 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[O-][NH+](N=O)[NH]",
    molecule =
"""
multiplicity 2
1 O u0 p3 c-1 {3,S}
2 O u0 p2 c0 {5,D}
3 N u0 p0 c+1 {1,S} {4,S} {5,S} {6,S}
4 N u1 p1 c0 {3,S} {7,S}
5 N u0 p1 c0 {2,D} {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N]ON=O",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {3,D}
3 N u0 p1 c0 {1,S} {2,D}
4 N u2 p1 c0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-]O[NH+]=O",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {3,D}
3 N u0 p0 c+1 {1,S} {2,D} {5,S}
4 N u1 p2 c-1 {1,S}
5 H u0 p0 c0 {3,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N]=NN(O)O",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {7,S}
2 O u0 p2 c0 {3,S} {6,S}
3 N u0 p1 c0 {1,S} {2,S} {4,S}
4 N u0 p1 c0 {3,S} {5,D}
5 N u1 p1 c0 {4,D}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "ON([NH2+][N-])O",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {9,S}
2 O u0 p2 c0 {4,S} {8,S}
3 N u0 p0 c+1 {4,S} {5,S} {6,S} {7,S}
4 N u0 p1 c0 {1,S} {2,S} {3,S}
5 N u1 p2 c-1 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N]OO",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {7,S}
3 N u0 p1 c0 {1,S} {4,S} {6,S}
4 N u0 p1 c0 {3,S} {5,D}
5 N u1 p1 c0 {4,D}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "OONN=[N]",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {7,S}
3 N u0 p1 c0 {1,S} {4,S} {6,S}
4 N u0 p1 c0 {3,S} {5,D}
5 N u1 p1 c0 {4,D}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-][NH2+]NOO",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {9,S}
3 N u0 p0 c+1 {4,S} {5,S} {6,S} {7,S}
4 N u0 p1 c0 {1,S} {3,S} {8,S}
5 N u1 p2 c-1 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[O-][NH2+]N1[N]O1",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {5,S}
2 O u0 p3 c-1 {3,S}
3 N u0 p0 c+1 {2,S} {4,S} {6,S} {7,S}
4 N u0 p1 c0 {1,S} {3,S} {5,S}
5 N u1 p1 c0 {1,S} {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-][NH2+]N1OO1",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {3,S}
3 N u0 p1 c0 {1,S} {2,S} {5,S}
4 N u0 p1 c0 {5,S} {6,S} {7,S}
5 N u1 p1 c0 {3,S} {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "N[N]N1OO1",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {3,S}
3 N u0 p1 c0 {1,S} {2,S} {5,S}
4 N u0 p1 c0 {5,S} {6,S} {7,S}
5 N u1 p1 c0 {3,S} {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "NON[N][O]",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {3,S} {4,S}
2 O u1 p2 c0 {5,S}
3 N u0 p1 c0 {1,S} {5,S} {6,S}
4 N u0 p1 c0 {1,S} {7,S} {8,S}
5 N u1 p1 c0 {2,S} {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[O-][NH2+]N[N][O]",
    molecule =
"""
multiplicity 3
1 O u0 p3 c-1 {3,S}
2 O u1 p2 c0 {5,S}
3 N u0 p0 c+1 {1,S} {4,S} {6,S} {7,S}
4 N u0 p1 c0 {3,S} {5,S} {8,S}
5 N u1 p1 c0 {2,S} {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[O][N]NNO",
    molecule =
"""
multiplicity 3
1 O u0 p2 c0 {4,S} {8,S}
2 O u1 p2 c0 {5,S}
3 N u0 p1 c0 {4,S} {5,S} {6,S}
4 N u0 p1 c0 {1,S} {3,S} {7,S}
5 N u1 p1 c0 {2,S} {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[O]N1NN1",
    molecule =
"""
multiplicity 2
1 O u1 p2 c0 {3,S}
2 N u0 p1 c0 {3,S} {4,S} {5,S}
3 N u0 p1 c0 {1,S} {2,S} {4,S}
4 N u0 p1 c0 {2,S} {3,S} {6,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "NN1[N]O1",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 N u0 p1 c0 {1,S} {3,S} {4,S}
3 N u0 p1 c0 {2,S} {5,S} {6,S}
4 N u1 p1 c0 {1,S} {2,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-]1[N]O[NH2+]1",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 N u0 p0 c+1 {1,S} {3,S} {5,S} {6,S}
3 N u0 p2 c-1 {2,S} {4,S}
4 N u1 p1 c0 {1,S} {3,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)

entry(
    label = "[N-]1N([NH2+]1)[O]",
    molecule =
"""
multiplicity 2
1 O u1 p2 c0 {3,S}
2 N u0 p0 c+1 {3,S} {4,S} {5,S} {6,S}
3 N u0 p1 c0 {1,S} {2,S} {4,S}
4 N u0 p2 c-1 {2,S} {3,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Did not converge either on a wb97xd/def2svp conformer search or a CBS-QB3 optimization.
""",
)
