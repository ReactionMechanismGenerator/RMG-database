"""
API Soup kinetics
"""

name = "api_soup"
shortDesc = ""
longDesc = """
Various small radical reactions relevant to API oxidation
"""

entry(
    index=0,
    label="AIBN <=> N2 + cyanoisopropyl + cyanoisopropyl",
    kinetics=Arrhenius(A=(5.40379e+15, 's^-1'), n=0, Ea=(132.417, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(363.6, 'K'), Tmax=(380.2, 'K')),
    shortDesc=u"""Juang 1992""",
    longDesc=
    u"""
Measured
Fig 4, k
R-S Juang, J-F Lianf, J. Chem. Tech. Biotechnol. 1992, 55, 379-383, doi: 10.1002/jctb.280550413

Another source:
    kinetics=Arrhenius(A=(2.14e+17, 's^-1'), n=0, Ea=(143, 'kJ/mol'), T0=(1, 'K')),
P.S. Eagel, Mechanism of the thermal and photochemical decomposition of azoalkanes
Chem. Rev. 1980, 80, 99-150

Juang is ~x2 faster than Eagel at the relevant temperatures
""",
)

entry(
    index=1,
    label="cyanoisopropyl + O2 <=> cyanoisopropylOO",
    kinetics=Arrhenius(A=(5.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
    shortDesc=u"""R_Recombination (RMG-Py rate rules)""",
    longDesc=
    u"""
""",
)

entry(
    index=2,
    label="CH3OH + HO2 <=> CH2OH + H2O2",
    kinetics=Arrhenius(A=(3.5e-4, 'cm^3/(mol*s)'), n=4.85, Ea=(10.35, 'kcal/mol'), T0=(1, 'K')),
    shortDesc=u"""NOx2018""",
    longDesc=
    u"""
""",
)

entry(
    index=3,
    label="CH3OH + HO2 <=> CH3O + H2O2",
    kinetics=Arrhenius(A=(1.5e-3, 'cm^3/(mol*s)'), n=4.61, Ea=(15.93, 'kcal/mol'), T0=(1, 'K')),
    shortDesc=u"""NOx2018""",
    longDesc=
    u"""
""",
)

entry(
    index=4,
    label="CH3OH + OH <=> CH2OH + H2O",
    kinetics=Arrhenius(A=(1.5e+8, 'cm^3/(mol*s)'), n=1.44, Ea=(0.11, 'kcal/mol'), T0=(1, 'K')),
    shortDesc=u"""Klippenstein_Glarborg2016""",
    longDesc=
    u"""
""",
)

entry(
    index=5,
    label="CH3OH + OH <=> CH3O + H2O",
    kinetics=Arrhenius(A=(2.7e+7, 'cm^3/(mol*s)'), n=1.44, Ea=(0.11, 'kcal/mol'), T0=(1, 'K')),
    shortDesc=u"""NOx2018""",
    longDesc=
    u"""
""",
)

entry(
    index=6,
    label="CH3OH + CH3O <=> CH2OH + CH3OH",
    kinetics=Arrhenius(A=(3.0e+11, 'cm^3/(mol*s)'), n=0, Ea=(4.07, 'kcal/mol'), T0=(1, 'K')),
    shortDesc=u"""CurranPentane""",
    longDesc=
    u"""
""",
)

entry(
    index=7,
    label="CH3O + O2 <=> CH2O + HO2",
    kinetics=Arrhenius(A=(0.48, 'cm^3/(mol*s)'), n=3.57, Ea=(1.05, 'kcal/mol'), T0=(1, 'K')),
    shortDesc=u"""NOx2018""",
    longDesc=
    u"""
""",
)

entry(
    index=8,
    label="OOCH2OH <=> CH2OH + O2",
    kinetics=Arrhenius(A=(2.0e+15, 's^-1'), n=0, Ea=(35.8, 'kcal/mol'), T0=(1, 'K')),
    longDesc=
    u"""
We get the following sequence of reactions because of the high CH3OH concentration:
1. CH3OO + CH3OH = CH3OOH + CH2OH
2. CH2OH + O2 = OOCH2OH
3. OOCH2OH + API = HOOCH2OH + API_rad

We have a bad rate estimate for reaction 2, this entry tries to fix it.
Taken from: T.S. Dibble, Mechanism and dynamics of the CH2OH + O2 reaction, Chem. Phys. Lett. 2002, 355, 193-200
doi: 10.1016/S0009-2614(02)00211-7

Reverse rate check: 1.053350e+12 cm^3/(mol*s), close to the diffusion limit of 1e+13
""",
)

entry(
    index=9,
    label="CH3OO + O <=> CH3O + O2",
    kinetics=Arrhenius(A=(2.9e+10, 'cm^3/(mol*s)'), n=1.0, Ea=(0.72, 'kcal/mol'), T0=(1, 'K')),
    shortDesc=u"""NOx2018""",
    longDesc=
    u"""
""",
)

entry(
    index=10,
    label="OHCH2OO <=> OCH2OOH",
    kinetics=Arrhenius(A=(3.0e+11, 's^-1'), n=0, Ea=(8.6, 'kcal/mol'), T0=(1, 'K')),
    shortDesc=u"""CurranPentane""",
    longDesc=
    u"""
""",
)

entry(
    index=11,
    label="OHCH2OO <=> CH2O + HO2",
    kinetics=Arrhenius(A=(6.38e+12, 's^-1'), n=0, Ea=(29.45, 'kcal/mol'), T0=(1, 'K')),
    shortDesc=u""" """,
    longDesc=
    u"""
Hermans et al. 2005 (doi:10.1021/jp044080v) G2M calculations
Training reaction in HO2_Elimination_from_PeroxyRadical 
""",
)

entry(
    index=12,
    label="OHCH2OOH <=> CH2O + H2O2",
    kinetics=Arrhenius(A=(3.16e11, 's^-1'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    shortDesc=u""" """,
    longDesc=
    u"""
est.
""",
)

entry(
    index=13,
    label="cyanoisopropyl + CH3OH <=> cyanoisopropane + CH2OH",
    kinetics=Arrhenius(A=(20715.6, 'm^3/(mol*s)'), n=0, Ea=(52.3057, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(275, 'K'), Tmax=(350, 'K')),
    shortDesc=u"""ccsd(t)/cc-pvtz//wb97xd/def2tzvp using ARC""",
    longDesc=
    u"""
sr1001

C[C](C#N)C + CO <=> CC(C#N)C + [CH2]O
""",
)

entry(
    index=14,
    label="cyanoisopropyl + CH3OH <=> cyanoisopropane + CH3O",
    kinetics=Arrhenius(A=(547414, 'm^3/(mol*s)'), n=0, Ea=(90.402, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(275, 'K'), Tmax=(350, 'K')),
    shortDesc=u"""ccsd(t)/cc-pvtz//wb97xd/def2tzvp using ARC""",
    longDesc=
    u"""
sr1002
C[C](C#N)C + CO <=> CC(C#N)C + C[O]

Calculated by ACS using multiple-structure local-harmonic 
conventional transition state theory with Eckart tunneling 
(MS-LH-CTST/Eckart).

Optfreq: CBS-QB3 in vacuum
SP: CBS-QB3 + Cosmo-RS TZVPD-Fine 
Solvent: H2O:MeOH = 0.7:0.3 (mol%)
""",
)

entry(
    index=15,
    label="cyanoisopropylO + CH3OH <=> cyanoisopropylOH + CH2OH",
    kinetics=Arrhenius(A=(903104, 'm^3/(mol*s)'), n=0, Ea=(7.4835, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(275, 'K'), Tmax=(350, 'K')),
    longDesc=
    u"""
sr1003

Calculated by ACS using multiple-structure local-harmonic 
conventional transition state theory with Eckart tunneling 
(MS-LH-CTST/Eckart).

Optfreq: CBS-QB3 in vacuum
SP: CBS-QB3 + Cosmo-RS TZVPD-Fine 
Solvent: H2O:MeOH = 0.7:0.3 (mol%)
""",
)

entry(
    index=16,
    label="cyanoisopropylO + CH3OH <=> cyanoisopropylOH + CH3O",
    kinetics=Arrhenius(A=(26562.3, 'm^3/(mol*s)'), n=0, Ea=(22.8263, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(275, 'K'), Tmax=(350, 'K')),
    longDesc=
    u"""
sr1004

Calculated by ACS using multiple-structure local-harmonic 
conventional transition state theory with Eckart tunneling 
(MS-LH-CTST/Eckart).

Optfreq: CBS-QB3 in vacuum
SP: CBS-QB3 + Cosmo-RS TZVPD-Fine 
Solvent: H2O:MeOH = 0.7:0.3 (mol%)
""",
)

entry(
    index=17,
    label="cyanoisopropylOO <=> cyclic_cyanoisopropylOO",
    kinetics=Arrhenius(A=(1e-30, 's^-1'), n=0, Ea=(1000, 'kJ/mol'), T0=(1, 'K'), Tmin=(250, 'K'), Tmax=(500, 'K')),
    shortDesc=u"""""",
    longDesc=
    u"""
forbidding this reaction in Intra_R_Add_Endocyclic didn't work, assigning here a low rate instead
""",
)

entry(
    index=18,
    label="iC3H6CNOO <=> cyclic_cyanoisopropylOO",
    kinetics=Arrhenius(A=(1e-20, 's^-1'), n=0, Ea=(100, 'kJ/mol'), T0=(1, 'K'), Tmin=(250, 'K'), Tmax=(500, 'K')),
    shortDesc=u"""""",
    longDesc=
    u"""
""",
)

entry(
    index=19,
    label="CH2O + H2O <=> OHCH2OH",
    kinetics=Arrhenius(A=(3.67e+06, 'cm^3/(mol*s)'), n=0, Ea=(5.83, 'kcal/mol'),
                       T0=(1, 'K'), Tmin=(285, 'K'), Tmax=(345, 'K')),
    shortDesc=u"""""",
    longDesc=
    u"""
J.G.M. Winkelman, O.K. Voorwinde, M. Ottens, A.A.C.M. Beenackers, L.P.B.M. Janssen
Chemical Engineering Science, Volume 57, Issue 19, October 2002, Pages 4067-4076
https://doi.org/10.1016/S0009-2509(02)00358-5
The original rate was multiplied by 18 cm3/mol to convert units into a second order reaction.
""",
)

entry(
    index=20,
    label="cyanoisopropylOH + H2O <=> C3_ketone + HCN + H2O",
    kinetics=Arrhenius(A=(1e3, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(250, 'K'), Tmax=(500, 'K')),
    shortDesc=u"""""",
    longDesc=
    u"""
sr1005

estimated
""",
)

entry(
    index=21,
    label="CH2O + HO2 <=> OCH2OOH",
    degeneracy=1,
    kinetics=Arrhenius(A=(1.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
    shortDesc=u"""CurranPentane""",
)

entry(
    index=22,
    label="CH3OH + cyanoisopropylOO <=> CH3O + cyanoisopropylOOH",
    degeneracy=1.0,
    kinetics=Arrhenius(A=(174094, 'm^3/(mol*s)'), n=0, Ea=(94.4368, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(275, 'K'), Tmax=(350, 'K')),
    longDesc=
    """
sr1007

Calculated by ACS using multiple-structure local-harmonic 
conventional transition state theory with Eckart tunneling 
(MS-LH-CTST/Eckart).

Optfreq: CBS-QB3 in vacuum
SP: CBS-QB3 + Cosmo-RS TZVPD-Fine 
Solvent: H2O:MeOH = 0.7:0.3 (mol%)
""",
)

entry(
    index=23,
    label="CH3OH + cyanoisopropylOO <=> CH2OH + cyanoisopropylOOH",
    degeneracy=1.0,
    kinetics=Arrhenius(A=(63533.4, 'm^3/(mol*s)'), n=0, Ea=(34.1105, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(275, 'K'), Tmax=(350, 'K')),
    longDesc=
    """
sr1006

Calculated by ACS using multiple-structure local-harmonic 
conventional transition state theory with Eckart tunneling 
(MS-LH-CTST/Eckart).

Optfreq: CBS-QB3 in vacuum
SP: CBS-QB3 + Cosmo-RS TZVPD-Fine 
Solvent: H2O:MeOH = 0.7:0.3 (mol%)
""",
)

entry(
    index=24,
    label="CH3OH + OHCH2OO <=> CH2OH + OHCH2OOH",
    degeneracy=1.0,
    kinetics=Arrhenius(A=(14238.7, 'm^3/(mol*s)'), n=0, Ea=(40.2342, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(275, 'K'), Tmax=(350, 'K')),
    longDesc=
    """
sr1014 reverse

Calculated by ACS using multiple-structure local-harmonic 
conventional transition state theory with Eckart tunneling 
(MS-LH-CTST/Eckart).

Optfreq: CBS-QB3 in vacuum
SP: CBS-QB3 + Cosmo-RS TZVPD-Fine 
Solvent: H2O:MeOH = 0.7:0.3 (mol%)
""",
)

entry(
    index=25,
    label="CH3O + OHCH2OOH <=> CH3OH + OHCH2OO",
    degeneracy=1.0,
    kinetics=Arrhenius(A=(163753, 'm^3/(mol*s)'), n=0, Ea=(98.6637, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(275, 'K'), Tmax=(350, 'K')),
    longDesc=
    """
sr1015 reverse

Calculated by ACS using multiple-structure local-harmonic 
conventional transition state theory with Eckart tunneling 
(MS-LH-CTST/Eckart).

Optfreq: CBS-QB3 in vacuum
SP: CBS-QB3 + Cosmo-RS TZVPD-Fine 
Solvent: H2O:MeOH = 0.7:0.3 (mol%)
""",
)

# entry(
#     index=26,
#     label="H2O + CH3OOH <=> H2O2 + CH3OH",
#     degeneracy=1.0,
#     kinetics=Arrhenius(A=(0.123672, 'cm^3/(mol*s)'), n=3.80899, Ea=(319.315, 'kJ/mol'),
#                        T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
#     longDesc=
#     """
# CBS-QB3 PCM water
#
# TS external symmetry: 1, TS optical isomers: 1
#
# Optimized TS geometry:
# C       0.59075300   -0.27141000    0.18760900
# O      -2.00374200    1.00876600    0.39810900
# H      -2.60844800    0.26238400    0.50183600
# O       0.97638000    1.57888900   -0.78680400
# H       1.36266100    1.33234300   -1.63793600
# O      -1.24626400    0.61132500   -0.75799600
# H      -0.04072600    1.45390400   -0.88891300
# H      -0.05374000   -0.04431000    1.02399800
# H       1.65101300   -0.15102600    0.34377800
# H       0.28530900   -1.07532000   -0.46433100
#
#
# No rotors considered for this TS.
# """,
# )

entry(
    index=27,
    label="CH3OOH + cyanoisopropylOO <=> CH3OO + cyanoisopropylOOH",
    degeneracy=1.0,
    kinetics=Arrhenius(A=(6.59209e-07, 'cm^3/(mol*s)'), n=5.23714, Ea=(20.5943, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
    longDesc=
    """
CBS-QB3 PCM water

TS external symmetry: 1, TS optical isomers: 1

Optimized TS geometry:
C       1.99238800   -0.64622600    0.05424400
O       0.64322900   -1.20710100    0.19138600
O       0.06111200   -1.44348800   -1.03267000
H      -0.77902500   -0.55996500   -1.12410700
C      -2.38517500    0.00873500    1.04434100
H      -2.26286300    0.39014100    2.05717200
H      -3.38978800    0.21007200    0.66995500
H      -2.16571800   -1.05936500    1.00380500
O      -1.42422300    0.73585200    0.25566200
O      -1.49541600    0.33980300   -1.05947400
C       1.91111500    0.59417300   -0.74282800
N       1.89058500    1.56834000   -1.35724100
C       2.90310000   -1.66607900   -0.63265100
H       3.91054600   -1.25957100   -0.73330800
H       2.94388800   -2.56916700   -0.02180600
H       2.51745100   -1.91353200   -1.62102400
C       2.40678400   -0.33561400    1.49301400
H       2.40068200   -1.26145900    2.06978300
H       3.41431200    0.08094500    1.50527100
H       1.71899900    0.37785300    1.94703500

1D rotors:
pivots: [1, 13], dihedral: [2, 1, 13, 14], rotor symmetry: 3, max scan energy: 13.86 kJ/mol
pivots: [1, 17], dihedral: [2, 1, 17, 18], rotor symmetry: 3, max scan energy: 11.96 kJ/mol
pivots: [1, 2], dihedral: [11, 1, 2, 3], rotor symmetry: 1, max scan energy: 13.73 kJ/mol
pivots: [5, 9], dihedral: [6, 5, 9, 10], rotor symmetry: 3, max scan energy: 7.14 kJ/mol
* Invalidated! pivots: [9, 10], dihedral: [5, 9, 10, 4], invalidation reason: Two consecutive points are inconsistent by more than 17.77 kJ/mol
""",
)

entry(
    index=28,
    label="H2O + cyanoisopropylOOH <=> H2O2 + cyanoisopropylOH",
    degeneracy=1.0,
    kinetics=Arrhenius(A=(6e+16, 'cm^3/(mol*s)'), n=0, Ea=(25, 'kcal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
    longDesc=
    """
sr1011

Estimated from the hydroperoxide_to_alcohol family
""",
)

entry(
    index=29,
    label="OHCH2OO + CH3OOH <=> OHCH2OOH + CH3OO",
    degeneracy=1.0,
    kinetics=Arrhenius(A=(3.66421e-09, 'cm^3/(mol*s)'), n=5.91097, Ea=(22.4993, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
    longDesc=
    """
CBS-QB3 PCM water

TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
C      -0.26550200   -0.37807700    0.40113100
H       0.26569800   -1.31022400    0.19330600
H      -0.85795800   -0.43759300    1.31272600
O      -1.10340800    0.03159100   -0.62510300
H      -0.64517800   -0.08029600   -1.46707500
O       0.81572300    0.55607000    0.62311700
O       0.32423000    1.72451900    1.16153600
H      -0.02089900    2.43115600    0.24452500
C       1.70016200    4.23409500   -0.95668800
H       2.12509300    5.22806300   -0.82065700
H       2.27650000    3.49139500   -0.40024200
H       1.65516900    3.97108100   -2.01463700
O       0.37188400    4.31773600   -0.41602400
O      -0.29696900    3.13302600   -0.63039100

1D rotors:
pivots: [1, 4], dihedral: [6, 1, 4, 5], rotor symmetry: 1, max scan energy: 21.42 kJ/mol
pivots: [1, 6], dihedral: [4, 1, 6, 7], rotor symmetry: 1, max scan energy: 27.26 kJ/mol
pivots: [9, 13], dihedral: [10, 9, 13, 14], rotor symmetry: 3, max scan energy: 7.85 kJ/mol
* Invalidated! pivots: [13, 14], dihedral: [9, 13, 14, 8], invalidation reason: Two consecutive points are inconsistent by more than 8.38 kJ/mol
""",
)

entry(
    index=30,
    label="OH + CH3OCH2OOH <=> CH3O + OHCH2OOH",
    degeneracy=1.0,
    kinetics=Arrhenius(A=(113.383, 'cm^3/(mol*s)'), n=3.37577, Ea=(254.75, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
                       Tmax=(350, 'K')),
    longDesc=
    """
CBS-QB3 SMD water, all TS rotors were invalidated
TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
C       0.42059900   -0.58012500    1.00479800
O      -1.72510000    0.03855500    0.56766500
H      -0.27906600   -1.35235700    1.27807800
C      -2.05675400   -0.28962700   -0.75315500
H      -2.36120200    0.59116600   -1.33738600
H      -1.24007800   -0.79657100   -1.29170800
H      -2.91098900   -0.98489900   -0.73283100
O      -0.13801600    1.54031700    0.27359700
O       1.11548000   -0.93843600   -0.01607400
H       0.81243300    0.12971400    1.71353400
O       2.20708400   -0.02298400   -0.27063600
H       2.59193400   -0.45205300   -1.05495500
H      -0.14171000    1.31562500   -0.66618400
""",
)

entry(
    index=31,
    label="cyanoisopropylOO + cyanoisopropylOO <=> cyanoisopropyl2_O4",
    kinetics=Arrhenius(A=(1.1e+7, 'cm^3/(mol*s)'), n=0.0, Ea=(0, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
                       Tmax=(350, 'K')),
    longDesc=
    """
Based on https://doi.org/10.1134/S0023158416010031
for 1,1-dimethylpropyl peroxy radicals recombination in polar solvents (water, methanol)

The measured rate constants of recombination at 298 K are
k = 0.5 * (3.9 ± 0.4) × 1E+7 cm^3/(mol*s) for water, and
k = 0.5 * (5.2 ± 0.5) × 1E+6 cm^3/(mol*s) for methanol.

using an average: 1.1E+7

RMG's estimate is:
Arrhenius(A=(5.32385e+10, 'cm^3/(mol*s)'), n=0.35, Ea=(0, 'kJ/mol'))
""",
)

entry(
    index=32,
    label="cyanoisopropyl2_O4 <=> cyanoisopropylO + cyanoisopropylO + O2",
    kinetics=Arrhenius(A=(4.5e+16, 's^-1'), n=0.0, Ea=(72.35, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'), Tmax=(350, 'K')),
    longDesc=
    """
Taken from
SERGEY L. KHURSAN, Organic tetroxides and mechanism of peroxy radical recombination,
doi: 10.1002/9780470682531.pat0827
Table 3, an average of sources 66 and 79
""",
)

entry(
    index=33,
    label="HO2 + OHCH2OO <=> H2O + O2 + OHCHO",
    degeneracy=1.0,
    kinetics=Arrhenius(A=(1.1e+9, 'cm^3/(mol*s)'), n=0.0, Ea=(0, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
                       Tmax=(350, 'K')),
    longDesc=
    """
rate taken as 100x the RDS of:
cyanoisopropylOO + cyanoisopropylOO <=> cyanoisopropyl2_O4 <=> cyanoisopropylO + cyanoisopropylO + O2
""",
)

entry(
    index=34,
    label="HO2 + cyanoisopropylOO <=> OH + O2 + cyanoisopropylO",
    degeneracy=1.0,
    kinetics=Arrhenius(A=(1.1e+7, 'cm^3/(mol*s)'), n=0.0, Ea=(0, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
                       Tmax=(350, 'K')),
    longDesc=
    """
rate taken from RDS of:
cyanoisopropylOO + cyanoisopropylOO <=> cyanoisopropyl2_O4 <=> cyanoisopropylO + cyanoisopropylO + O2
""",
)

entry(
    index=35,
    label="H2O2 + cyanoisopropylOO <=> HO2 + cyanoisopropylOOH",
    degeneracy=1.0,
    kinetics=Arrhenius(A=(1013.78, 'm^3/(mol*s)'), n=0, Ea=(23.9464, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(275, 'K'), Tmax=(350, 'K')),
    longDesc=
    """
sr1009

Calculated by ACS using multiple-structure local-harmonic 
conventional transition state theory with Eckart tunneling 
(MS-LH-CTST/Eckart).

Optfreq: CBS-QB3 in vacuum
SP: CBS-QB3 + Cosmo-RS TZVPD-Fine 
Solvent: H2O:MeOH = 0.7:0.3 (mol%)
""",
)

entry(
    index=36,
    label="OHCH2OO + OHCH2OO <=> OHCHO + OHCHO + H2O2",
    kinetics=Arrhenius(A=(7.92e+13, 'cm^3/(mol*s)'), n=0.0, Ea=(2.772, 'kcal/mol'),
                       T0=(1, 'K'), Tmin=(278, 'K'), Tmax=(331, 'K')),
    longDesc=
    """
Source for rate (experimental, pH=7):
R.E. Huie, C.L. Clifton
Kinetics of the self-reaction of hydromethylperoxyl radicals
Chemical Physics Letters 1993, 205
https://doi.org/10.1016/0009-2614(93)89222-4

This pathway is also supported by:
https://doi.org/10.1016/S1352-2310(00)00191-6
""",
)

entry(
    index=37,
    label="OHCH2OO + OHCH2OO <=> OHCHO + OHCH2OH + O2",
    kinetics=Arrhenius(A=(7.92e+12, 'cm^3/(mol*s)'), n=0.0, Ea=(2.772, 'kcal/mol'),
                       T0=(1, 'K'), Tmin=(278, 'K'), Tmax=(331, 'K')),
    longDesc=
    """
Set to 10% of the main channel yielding OHCHO + OHCHO + H2O2
https://doi.org/10.1016/0009-2614(93)89222-4
""",
)

entry(
    index=38,
    label="OHCH2OO + OHCH2OO <=> OHCH2O + OHCH2O + O2",
    kinetics=Arrhenius(A=(7.92e+12, 'cm^3/(mol*s)'), n=0.0, Ea=(2.772, 'kcal/mol'),
                       T0=(1, 'K'), Tmin=(278, 'K'), Tmax=(331, 'K')),
    longDesc=
    """
Set to 1% of the main channel yielding OHCHO + OHCHO + H2O2
""",
)

entry(
    index=39,
    label="OHCH2OO + cyanoisopropylOO <=> OHCH2O + cyanoisopropylO + O2",
    kinetics=Arrhenius(A=(1.1e+7, 'cm^3/(mol*s)'), n=0.0, Ea=(0, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
                       Tmax=(350, 'K')),
    longDesc=
    """
Taken as:
cyanoisopropylOO + cyanoisopropylOO <=> cyanoisopropyl2_O4
(rate could be improved)
""",
)

entry(
    index=40,
    label="OHCH2OOH + cyanoisopropylOO <=> OHCH2OO + cyanoisopropylOOH",
    kinetics=Arrhenius(A=(143.492, 'm^3/(mol*s)'), n=0, Ea=(25.9299, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(275, 'K'), Tmax=(350, 'K')),
    longDesc=
    """
sr1010

Calculated by ACS using multiple-structure local-harmonic 
conventional transition state theory with Eckart tunneling 
(MS-LH-CTST/Eckart).

Optfreq: CBS-QB3 in vacuum
SP: CBS-QB3 + Cosmo-RS TZVPD-Fine 
Solvent: H2O:MeOH = 0.7:0.3 (mol%)
""",
)

entry(
    index=41,
    label="OHCH2O + CH3OH <=> OHCH2OH + CH2OH",
    kinetics=Arrhenius(A=(170530, 'm^3/(mol*s)'), n=0, Ea=(5.493, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(275, 'K'), Tmax=(350, 'K')),
    longDesc=
    """
sr1012

Calculated by ACS using multiple-structure local-harmonic 
conventional transition state theory with Eckart tunneling 
(MS-LH-CTST/Eckart).

Optfreq: CBS-QB3 in vacuum
SP: CBS-QB3 + Cosmo-RS TZVPD-Fine 
Solvent: H2O:MeOH = 0.7:0.3 (mol%)
""",
)

entry(
    index=42,
    label="OHCH2O + CH3OH <=> OHCH2OH + CH3O",
    kinetics=Arrhenius(A=(18638.8, 'm^3/(mol*s)'), n=0, Ea=(31.9596, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(275, 'K'), Tmax=(350, 'K')),
    longDesc=
    """
sr1013

Calculated by ACS using multiple-structure local-harmonic 
conventional transition state theory with Eckart tunneling 
(MS-LH-CTST/Eckart).

Optfreq: CBS-QB3 in vacuum
SP: CBS-QB3 + Cosmo-RS TZVPD-Fine 
Solvent: H2O:MeOH = 0.7:0.3 (mol%)
""",
)

entry(
    index=43,
    label="OHCH2O <=> OHCHO + H",
    kinetics=Arrhenius(A=(1e14, 's^-1'), n=0.0, Ea=(62.34, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(275, 'K'), Tmax=(350, 'K')),
    longDesc=
    """
sr1018

NOx2018
""",
)

entry(
    index=44,
    label='OHCHOH + OHCH2OOH <=> OHCH2OH + OHCH2OO',
    degeneracy=1.0,
    kinetics=Arrhenius(A=(5.04944e+07, 'cm^3/(mol*s)'), n=0, Ea=(17.4814, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
                       Tmax=(350, 'K')),
    longDesc=
    """
dlpno-ccsd(T)/def2tzvp//wb97xd/def2tzvp with APFD SMD water for solvation sp correction 
""",
)

entry(
    index=45,
    label='OHCHOH + cyanoisopropylOOH <=> OHCH2OH + cyanoisopropylOO',
    degeneracy=1.0,
    kinetics=Arrhenius(A=(8.90093e+07, 'cm^3/(mol*s)'), n=0, Ea=(23.8264, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
                       Tmax=(350, 'K')),
    longDesc=
    """
dlpno-ccsd(T)/def2tzvp//wb97xd/def2tzvp with APFD SMD water for solvation sp correction 
""",
)

entry(
    index=46,
    label='CH2O + cyanoisopropylOO <=> CHO + cyanoisopropylOOH',
    degeneracy=2.0,
    kinetics=Arrhenius(A=(9.25121e+08, 'cm^3/(mol*s)'), n=0, Ea=(41.2887, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
                       Tmax=(350, 'K')),
    longDesc=
    """
dlpno-ccsd(T)/def2tzvp//wb97xd/def2tzvp with APFD SMD water for solvation sp correction 
""",
)

entry(
    index=47,
    label='CH2OH + cyanoisopropylOO <=> CH2O + cyanoisopropylOOH',
    degeneracy=2.0,
    kinetics=Arrhenius(A=(1.21e13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(275, 'K'), Tmax=(350, 'K')),
    longDesc=
    """
sr1008

estimated using RMG's website
""",
)

entry(
    index=48,
    label='H2O2 + OHCH2OO <=> HO2 + OHCH2OOH',
    degeneracy=2.0,
    kinetics=Arrhenius(A=(3579.97, 'm^3/(mol*s)'), n=0, Ea=(32.2689, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(275, 'K'), Tmax=(350, 'K')),
    longDesc=
    """
sr1016

Calculated by ACS using multiple-structure local-harmonic 
conventional transition state theory with Eckart tunneling 
(MS-LH-CTST/Eckart).

Optfreq: CBS-QB3 in vacuum
SP: CBS-QB3 + Cosmo-RS TZVPD-Fine 
Solvent: H2O:MeOH = 0.7:0.3 (mol%)
""",
)

entry(
    index=49,
    label='CH2OH + OHCH2OO <=> CH2O + OHCH2OOH',
    degeneracy=2.0,
    kinetics=Arrhenius(A=(1.21e13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(275, 'K'), Tmax=(350, 'K')),
    longDesc=
    """
sr1017

estimated from the RMG website
""",
)

entry(
    index=50,
    label="CH2OH + O2 <=> CH2O + HO2",
    kinetics=Arrhenius(A=(7.23e+13, 'cm^3/(mol*s)'), n=0, Ea=(3736, 'cal/mol'), T0=(1, 'K')),
    longDesc=
    u"""
https://doi.org/10.1063/1.1748524
p. 37
Keeping only the second term
""",
)

entry(
    index=51,
    label="H + H <=> H2",
    kinetics=Arrhenius(A=(1.0e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc=
    u"""
Should be fast in liquid phase, WHG est.
""",
)

entry(
    index=52,
    label="O2 + H <=> HO2",
    kinetics=Arrhenius(A=(4.7e+12, 'cm^3/(mol*s)'), n=0.440, Ea=(0.0, 'cal/mol'), T0=(1, 'K')),
    longDesc=
    u"""
Klippenstein_Glarborg2016
Probably high-P VTST
""",
)
