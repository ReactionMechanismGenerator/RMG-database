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

# entry(
#     index=2,
#     label="cyanoisopropylOO + CH3OH <=> cyanoisopropylOOH + CH2OH",
#     kinetics=Arrhenius(A=(0.234766, 'cm^3/(mol*s)'), n=3.50344, Ea=(25.4103, 'kJ/mol'), T0=(1, 'K'), Tmin=(250, 'K'),
#                        Tmax=(500, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.05474, dn = +|- 0.00777691,
#                        dEa = +|- 0.0221566 kJ/mol"""),
#     shortDesc=u"""ccsd(t)/cc-pvtz//wb97xd/def2tzvp using ARC""",
#     longDesc=
#     u"""
#     CO[O] + CH3OH <=> COOH + CH2OH
#     NOx2018 has a different value Arrhenius(A=(4.0e+13, 'cm^3/(mol*s)'), n=0, Ea=(19.40, 'kcal/mol'), T0=(1, 'K'))
# """,
# )
#
# entry(
#     index=3,
#     label="cyanoisopropylOO + CH3OH <=> cyanoisopropylOOH + CH3O",
#     kinetics=Arrhenius(A=(1.89162e-06, 'cm^3/(mol*s)'), n=5.47458, Ea=(64.6665, 'kJ/mol'), T0=(1, 'K'), Tmin=(250, 'K'),
#                        Tmax=(500, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.14859, dn = +|- 0.0202144, dEa
#                        = +|- 0.0575912 kJ/mol"""),
#     shortDesc=u"""H_abstraction""",
#     longDesc=
#     u"""
#     CO[O] + CH3OH <=> COOH + CH3[O]
#     H_abstraction has a different value Arrhenius(A=(1.17e-2, 'cm^3/(mol*s)'), n=4.29, Ea=(32.92, 'kcal/mol'),
#     T0=(1, 'K'))
# """,
# )

entry(
    index=4,
    label="CH3OH + HO2 <=> CH2OH + H2O2",
    kinetics=Arrhenius(A=(3.5e-4, 'cm^3/(mol*s)'), n=4.85, Ea=(10.35, 'kcal/mol'), T0=(1, 'K')),
    shortDesc=u"""NOx2018""",
    longDesc=
    u"""
""",
)

entry(
    index=5,
    label="CH3OH + HO2 <=> CH3O + H2O2",
    kinetics=Arrhenius(A=(1.5e-3, 'cm^3/(mol*s)'), n=4.61, Ea=(15.93, 'kcal/mol'), T0=(1, 'K')),
    shortDesc=u"""NOx2018""",
    longDesc=
    u"""
""",
)

entry(
    index=6,
    label="CH3OH + OH <=> CH2OH + H2O",
    kinetics=Arrhenius(A=(1.5e+8, 'cm^3/(mol*s)'), n=1.44, Ea=(0.11, 'kcal/mol'), T0=(1, 'K')),
    shortDesc=u"""Klippenstein_Glarborg2016""",
    longDesc=
    u"""
""",
)

entry(
    index=7,
    label="CH3OH + OH <=> CH3O + H2O",
    kinetics=Arrhenius(A=(2.7e+7, 'cm^3/(mol*s)'), n=1.44, Ea=(0.11, 'kcal/mol'), T0=(1, 'K')),
    shortDesc=u"""NOx2018""",
    longDesc=
    u"""
""",
)

entry(
    index=8,
    label="CH3OH + CH3O <=> CH2OH + CH3OH",
    kinetics=Arrhenius(A=(3.0e+11, 'cm^3/(mol*s)'), n=0, Ea=(4.07, 'kcal/mol'), T0=(1, 'K')),
    shortDesc=u"""CurranPentane""",
    longDesc=
    u"""
""",
)

entry(
    index=9,
    label="CH3O + O2 <=> CH2O + HO2",
    kinetics=Arrhenius(A=(0.48, 'cm^3/(mol*s)'), n=3.57, Ea=(1.05, 'kcal/mol'), T0=(1, 'K')),
    shortDesc=u"""NOx2018""",
    longDesc=
    u"""
""",
)

# entry(
#     index=10,
#     label="CH2OH + O2 <=> CH2O + HO2",
#     kinetics=MultiArrhenius(
#         arrhenius=[
#             Arrhenius(A=(7.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(3736, 'cal/mol'), T0=(1, 'K')),
#             Arrhenius(A=(2.9e+16, 'cm^3/(mol*s)'), n=-1.5, Ea=(0, 'cal/mol'), T0=(1, 'K'))]),
#     shortDesc=u"""NOx2018""",
#     longDesc=
#     u"""
# """,
# )

entry(
    index = 11,
    label = "OOCH2OH <=> CH2OH + O2",
    kinetics = Arrhenius(A=(2.0e+15,'s^-1'), n=0, Ea=(35.8,'kcal/mol'), T0=(1,'K')),
    longDesc =
u"""
We get the following sequence of reactions because of the high CH3OH concentration:
1. CH3OO + CH3OH = CH3OOH + CH2OH
2. CH2OH + O2 = OOCH2OH
3. OOCH2OH + API = HOOCH2OH + API_rad

We have a bad rate estimate for reaction 2, this entry tries to fix it.
Taken from: T.S. Dibble, Mechanism and dynamics of the CH2OH + O2 reaction, Chem. Phys. Lett. 2002, 355, 193-200
doi: 10.1016/S0009-2614(02)00211-7
""",
)

entry(
    index=12,
    label="CH3OO + O <=> CH3O + O2",
    kinetics=Arrhenius(A=(2.9e+10, 'cm^3/(mol*s)'), n=1.0, Ea=(0.72, 'kcal/mol'), T0=(1, 'K')),
    shortDesc=u"""NOx2018""",
    longDesc=
    u"""
""",
)

entry(
    index=13,
    label="OHCH2OO <=> OCH2OOH",
    kinetics=Arrhenius(A=(3.0e+11, 's^-1'), n=0, Ea=(8.6, 'kcal/mol'), T0=(1, 'K')),
    shortDesc=u"""CurranPentane""",
    longDesc=
    u"""
""",
)

entry(
    index=14,
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
    index=15,
    label="OHCH2OOH <=> CH2O + H2O2",
    kinetics=Arrhenius(A=(3.16e11, 's^-1'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    shortDesc=u""" """,
    longDesc=
    u"""
est.
""",
)

entry(
    index=16,
    label="cyanoisopropyl + CH3OH <=> cyanoisopropane + CH2OH",
    kinetics=Arrhenius(A=(1.20521e-20, 'cm^3/(mol*s)'), n=9.67402, Ea=(28.0373, 'kJ/mol'), T0=(1, 'K'), Tmin=(250, 'K'),
                       Tmax=(500, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.79835, dn = +|- 0.0856346, 
                       dEa = +|- 0.243975 kJ/mol"""),
    shortDesc=u"""ccsd(t)/cc-pvtz//wb97xd/def2tzvp using ARC""",
    longDesc=
    u"""
    C[C](C#N)C + CO <=> CC(C#N)C + [CH2]O
""",
)

entry(
    index=17,
    label="cyanoisopropyl + CH3OH <=> cyanoisopropane + CH3O",
    kinetics=Arrhenius(A=(0.109341, 'cm^3/(mol*s)'), n=3.92562, Ea=(66.4122, 'kJ/mol'), T0=(1, 'K'), Tmin=(250, 'K'),
                       Tmax=(500, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.01558, dn = +|- 0.00225605, 
                       dEa = +|- 0.00642752 kJ/mol"""),
    shortDesc=u"""ccsd(t)/cc-pvtz//wb97xd/def2tzvp using ARC""",
    longDesc=
    u"""
    C[C](C#N)C + CO <=> CC(C#N)C + C[O]
""",
)

entry(
    index=18,
    label="cyanoisopropylOO <=> cyclic_cyanoisopropylOO",
    kinetics=Arrhenius(A=(1e-30, 's^-1'), n=0, Ea=(1000, 'kJ/mol'), T0=(1, 'K'), Tmin=(250, 'K'), Tmax=(500, 'K')),
    shortDesc=u"""""",
    longDesc=
    u"""
forbidding this reaction in Intra_R_Add_Endocyclic didn't work, assigning here a low rate instead
""",
)

entry(
    index=19,
    label="iC3H6CNOO <=> cyclic_cyanoisopropylOO",
    kinetics=Arrhenius(A=(1e-20, 's^-1'), n=0, Ea=(100, 'kJ/mol'), T0=(1, 'K'), Tmin=(250, 'K'), Tmax=(500, 'K')),
    shortDesc=u"""""",
    longDesc=
    u"""
""",
)

entry(
    index=20,
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
    index=21,
    label="cyanoisopropanol + H2O <=> C3_ketone + HCN + H2O",
    # kinetics=Arrhenius(A=(4.10e14, 'cm^3/(mol*s)'), n=-0.410127, Ea=(157.792, 'kJ/mol'),
    #                    T0=(1, 'K'), Tmin=(250, 'K'), Tmax=(500, 'K')),
    kinetics=Arrhenius(A=(1e3, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(250, 'K'), Tmax=(500, 'K')),
    shortDesc=u"""""",
    longDesc=
    u"""
Calculated at CCSD(T)/cc-pVTZ//APFD/def2TZVpp + PCM water
Calculated for VDW1 (cyznoisopropane + H2O) <=> VDW2 (C3_ketone + H2O) + HCN
multiplied by 18 ml/mol to account for water as the reactant and convert from s^-1 to cm^3/(mol*s)
""",
)

# entry(
#     index=22,
#     label="iC3H6NHCH2OH + HCN <=> iC3H6NHCH2CN + H2O",
#     # kinetics=Arrhenius(A=(283.024, 'cm^3/(mol*s)'), n=2.54221, Ea=(232.434, 'kJ/mol'),
#     #                    T0=(1, 'K'), Tmin=(250, 'K'), Tmax=(500, 'K')),
#     kinetics=Arrhenius(A=(1e3, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'),
#                        T0=(1, 'K'), Tmin=(250, 'K'), Tmax=(500, 'K')),
#     shortDesc=u"""""",
#     longDesc=
#     u"""
# Calculated at CBS-QB3 + PCM water
# Added as a training reaction to amine_COH_HCN
# """,
# )

entry(
    index = 22,
    label = "CH2O + HO2 <=> OCH2OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""CurranPentane""",
)

entry(
    index = 23,
    label = "CH3OH + cyanoisopropylOO <=> CH3O + cyanoisopropylOOH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.47388e-06,'cm^3/(mol*s)'), n=5.28149, Ea=(78.3254,'kJ/mol'),
                         T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc =
"""
CBS-QB3 PCM water

TS external symmetry: 1, TS optical isomers: 1

Optimized TS geometry:
C       1.79455300   -0.16943700   -0.41097100
O       0.55934800   -0.92153100   -0.58881900
O      -0.10136700   -0.48790700   -1.74852800
H      -1.11674700   -0.20081900   -1.41108400
O      -2.08389000    0.44361000   -0.90499700
C      -2.18212000    0.17411500    0.45011400
H      -2.82885800   -0.69603800    0.63935000
H      -1.18306000   -0.12479800    0.82673900
H      -2.51702700    1.04839400    1.01582800
C       1.44485500    1.26116200   -0.26745800
N       1.18695600    2.37711500   -0.14226500
C       2.37446800   -0.71406700    0.89672500
H       2.56398400   -1.78184100    0.77985500
H       3.31595400   -0.21078700    1.11851500
H       1.68431000   -0.55851800    1.72624500
C       2.72661400   -0.37911700   -1.60675600
H       3.65405800    0.17622700   -1.45857400
H       2.95870000   -1.44224000   -1.68798600
H       2.25144500   -0.04112100   -2.52637100

1D rotors:
pivots: [1, 12], dihedral: [2, 1, 12, 13], rotor symmetry: 3, max scan energy: 11.68 kJ/mol
pivots: [1, 16], dihedral: [2, 1, 16, 17], rotor symmetry: 3, max scan energy: 13.45 kJ/mol
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 1, max scan energy: 17.93 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 32.83 kJ/mol
""",
)

entry(
    index = 24,
    label = "CH2OH + OHCH2OOH <=> CH3OH + OHCH2OO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.25793e-05,'cm^3/(mol*s)'), n=4.36536, Ea=(46.701,'kJ/mol'),
                         T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc =
"""
CBS-QB3 PCM water

TS external symmetry: 1, TS optical isomers: 1

Optimized TS geometry:
C      -2.05710800   -0.24645300   -0.08534400
H      -2.37002900   -0.96482200   -0.84836900
H      -2.71771300   -0.26255100    0.78075100
O      -1.99745700    1.06340200   -0.54056500
H      -1.57022600    1.07695400   -1.40535500
O      -0.77344100   -0.76509200    0.30981900
O      -0.32867000   -0.10435000    1.46306400
H       0.11734800    0.82655200    1.10702700
O       0.95763500    1.70014200    0.68788800
C       1.85923800    1.16903300   -0.22358200
H       2.76496000    0.77172400    0.25061300
H       1.39133300    0.41332200   -0.87031100
H       2.15903900    1.99673500   -0.88879100


No rotors considered for this TS.
""",
)

entry(
    index = 25,
    label = "H2O + CH3OOH <=> H2O2 + CH3OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.123672,'cm^3/(mol*s)'), n=3.80899, Ea=(319.315,'kJ/mol'),
                         T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc =
"""
CBS-QB3 PCM water

TS external symmetry: 1, TS optical isomers: 1

Optimized TS geometry:
C       0.59075300   -0.27141000    0.18760900
O      -2.00374200    1.00876600    0.39810900
H      -2.60844800    0.26238400    0.50183600
O       0.97638000    1.57888900   -0.78680400
H       1.36266100    1.33234300   -1.63793600
O      -1.24626400    0.61132500   -0.75799600
H      -0.04072600    1.45390400   -0.88891300
H      -0.05374000   -0.04431000    1.02399800
H       1.65101300   -0.15102600    0.34377800
H       0.28530900   -1.07532000   -0.46433100


No rotors considered for this TS.
""",
)

entry(
    index = 26,
    label = "CH3OOH + cyanoisopropylOO <=> CH3OO + cyanoisopropylOOH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.59209e-07,'cm^3/(mol*s)'), n=5.23714, Ea=(20.5943,'kJ/mol'),
                         T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc =
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
    index = 27,
    label = "CH3OOH + CH3OCH2OO <=> CH3OO + CH3OCH2OOH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.87227e-07,'cm^3/(mol*s)'), n=5.41371, Ea=(17.9795,'kJ/mol'),
                         T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc =
"""
CBS-QB3 PCM water

TS external symmetry: 1, TS optical isomers: 1

Optimized TS geometry:
C      -2.40940900   -0.29404300   -0.00786500
H      -2.93771800   -0.83385500   -0.80142000
H      -2.93466700   -0.33999300    0.94485500
O      -2.18443200    1.03168100   -0.30750800
O      -1.18385000   -1.06278300    0.12532700
O      -0.53596400   -0.71905700    1.29125600
H       0.28702700    0.10640200    0.98898700
C       2.45875600   -0.62332200   -0.51782300
H       2.69277500   -0.91322700   -1.54147900
H       3.33639300   -0.20877300   -0.01952500
H       2.06342300   -1.47208500    0.04376800
O       1.44529800    0.39039200   -0.63830700
O       1.09243200    0.85324000    0.60919200
C      -1.76232000    1.27662500   -1.65751800
H      -1.69120800    2.35755500   -1.76433100
H      -0.78673400    0.82681400   -1.85182100
H      -2.50117400    0.88730000   -2.36639400

1D rotors:
pivots: [1, 4], dihedral: [5, 1, 4, 14], rotor symmetry: 1, max scan energy: 35.44 kJ/mol
pivots: [1, 5], dihedral: [4, 1, 5, 6], rotor symmetry: 1, max scan energy: 19.94 kJ/mol
pivots: [4, 14], dihedral: [1, 4, 14, 15], rotor symmetry: 3, max scan energy: 6.13 kJ/mol
pivots: [8, 12], dihedral: [9, 8, 12, 13], rotor symmetry: 3, max scan energy: 7.67 kJ/mol
""",
)

entry(
    index = 28,
    label = "H2O + cyanoisopropylOOH <=> H2O2 + cyanoisopropylOH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.92734,'cm^3/(mol*s)'), n=3.1402, Ea=(309.899,'kJ/mol'),
                         T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc =
"""
CBS-QB3 PCM water

TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
C      -0.84504100    0.08842700    0.47150000
C      -1.28849000   -0.92834000   -0.42038900
N      -1.75417600   -1.81078900   -1.01037000
C      -0.74174800   -0.29566100    1.90806400
H      -0.07598000    0.38036900    2.44179400
H      -1.75348200   -0.16815100    2.32410600
H      -0.44090100   -1.32969700    2.05485100
C      -0.98175400    1.49858300    0.10303100
H      -1.77159500    1.63846200   -0.63856600
H      -1.13896300    2.11945100    0.98451800
H      -0.05893500    1.83980400   -0.41961000
O       0.95781700    1.48099700   -2.01711900
H       0.34571200    1.88950700   -2.64644300
O       1.48170500   -0.37324300    0.30548500
H       1.62984400   -1.31471100    0.45576100
O       0.50566300    0.12662900   -1.97040700
H       1.25247100   -0.27563500   -0.68048600

1D rotors:
* Invalidated! pivots: [1, 4], dihedral: [2, 1, 4, 5], invalidation reason: Two consecutive points are inconsistent by more than 5.59 kJ/mol
pivots: [1, 8], dihedral: [2, 1, 8, 9], rotor symmetry: 3, max scan energy: 8.31 kJ/mol
""",
)

entry(
    index = 29,
    label = "CH3OH + cyanoisopropylOO <=> CH2OH + cyanoisopropylOOH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.43114e-07,'cm^3/(mol*s)'), n=5.32109, Ea=(35.9739,'kJ/mol'),
                         T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc =
"""
CBS-QB3 PCM water

TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
C       1.85286600    0.16013400   -0.70155100
O       0.90247500   -0.83377700   -0.24384100
O      -0.32412000   -0.71007200   -0.92681100
H      -1.09199800   -0.11130300   -0.15219200
O      -3.09141300   -0.24708700    0.74289400
C      -1.93530200    0.49183300    0.65301100
H      -2.12968100    1.44321900    0.16226200
H      -1.35268100    0.56670200    1.57479100
H      -2.95769300   -0.97932700    1.35728700
C       1.31447700    1.50204900   -0.37832100
N       0.89735900    2.54500500   -0.11928000
C       3.10731700   -0.11760400    0.13248300
H       3.45835600   -1.12663900   -0.08835300
H       3.89293200    0.59401500   -0.12386900
H       2.88789000   -0.03917600    1.19774600
C       2.10244500    0.03592200   -2.20655400
H       2.81988500    0.78936800   -2.53615400
H       2.50960400   -0.95554400   -2.41253600
H       1.17165600    0.16394800   -2.75706700

1D rotors:
pivots: [1, 12], dihedral: [2, 1, 12, 13], rotor symmetry: 3, max scan energy: 11.85 kJ/mol
pivots: [1, 16], dihedral: [2, 1, 16, 17], rotor symmetry: 3, max scan energy: 13.25 kJ/mol
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 19.25 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: 
* Invalidated! pivots: [5, 6], dihedral: [9, 5, 6, 7], invalidation reason:
""",
)

entry(
    index = 30,
    label = "CH2OH + CH3OCH2OOH <=> CH3OH + CH3OCH2OO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.34895e-05,'cm^3/(mol*s)'), n=4.32686, Ea=(6.76111,'kJ/mol'),
                         T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc =
"""
CBS-QB3 PCM water

TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
C      -1.60428400   -0.67208600    0.22905200
H      -2.61311600   -0.63425300   -0.19959100
H      -1.53301200   -1.39948200    1.03726500
O      -1.21357900    0.56162900    0.74784200
O      -0.79531900   -1.10572900   -0.85926200
O       0.42166800   -1.62006900   -0.35977600
H       1.18681000   -0.66103500   -0.22901500
O       3.29231000   -0.00082800   -0.36015200
C       2.00230700    0.35202100   -0.02972400
H       1.92046700    0.53007800    1.04045000
H       1.55923100    1.13345200   -0.65178100
C      -1.55785400    1.67476900   -0.08330200
H      -1.20957800    2.56993500    0.42958900
H      -1.07509300    1.60703700   -1.06229000
H      -2.64381400    1.73387700   -0.21979300
H       3.40187800    0.04988400   -1.31744800

1D rotors:
pivots: [1, 4], dihedral: [5, 1, 4, 12], rotor symmetry: 1, max scan energy: 38.42 kJ/mol
pivots: [1, 5], dihedral: [4, 1, 5, 6], rotor symmetry: 3, max scan energy: 36.88 kJ/mol
pivots: [4, 12], dihedral: [1, 4, 12, 13], rotor symmetry: 3, max scan energy: 6.18 kJ/mol
* Invalidated! pivots: [5, 6], dihedral: [1, 5, 6, 7], invalidation reason: 
pivots: [8, 9], dihedral: [16, 8, 9, 10], rotor symmetry: 1, max scan energy: 29.14 kJ/mol
""",
)

entry(
    index = 31,
    label = "OHCH2OO + CH3OOH <=> OHCH2OOH + CH3OO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.66421e-09,'cm^3/(mol*s)'), n=5.91097, Ea=(22.4993,'kJ/mol'),
                         T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc =
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
    index = 32,
    label = "OH + CH3OCH2OOH <=> CH3O + OHCH2OOH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(113.383,'cm^3/(mol*s)'), n=3.37577, Ea=(254.75,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
                         Tmax=(350,'K')),
    longDesc =
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
    index = 33,
    label = "H2O + CH3OCH2OO <=> OH + CH3OCH2OOH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.02901e+10,'cm^3/(mol*s)'), n=0, Ea=(137.202,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
                         Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.01273, dn = +|- 0, 
                         dEa = +|- 0.0326164 kJ/mol"""),
    longDesc =
"""
CBS-QB3 SMD water

TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
C       0.98277800   -1.03895700   -0.11961800
H       1.77495300   -1.31849800    0.58390200
H       0.92899400   -1.72222000   -0.96690400
O       1.14859100    0.24653000   -0.63512000
O      -0.19876500   -1.17500600    0.67803600
O      -1.34777000   -1.07183400   -0.15480200
H      -1.38986300   -0.08403100   -0.42895300
O      -1.95805700    1.26056600   -0.30588900
C       1.47651700    1.23378200    0.35506400
H       1.58841900    2.17844400   -0.17503200
H       0.68259200    1.32897800    1.09991800
H       2.41746600    0.97764200    0.85360000
H      -1.59459300    1.58275300    0.53959600

1D rotors:
pivots: [1, 4], dihedral: [5, 1, 4, 9], rotor symmetry: 1, max scan energy: 37.14 kJ/mol
pivots: [1, 5], dihedral: [4, 1, 5, 6], rotor symmetry: 1, max scan energy: 36.89 kJ/mol
pivots: [4, 9], dihedral: [1, 4, 9, 10], rotor symmetry: 3, max scan energy: 5.19 kJ/mol
* Invalidated! pivots: [5, 6], dihedral: [1, 5, 6, 7], invalidation reason:
""",
)

entry(
    index = 34,
    label = "CH3O + OHCH2OOH <=> CH3OH + OHCH2OO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.87252e+09,'cm^3/(mol*s)'), n=0, Ea=(24.6093,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
                         Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.03866, dn = +|- 0, 
                         dEa = +|- 0.0978258 kJ/mol"""),
    longDesc =
"""
CBS-QB3 SMD water

TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
C       1.57679800    0.01805400    0.10381800
H       2.02580100   -0.20817100    1.07380500
H       2.30395100   -0.03089000   -0.70538300
O       0.96690200    1.27182400    0.05314700
H       0.46256500    1.40214300    0.86696600
O       0.64243200   -1.07140100   -0.06044400
O       0.11002600   -1.05971600   -1.35373900
H      -0.71627700   -0.32934800   -1.33240900
O      -1.85835100    0.20979600   -1.16793200
C      -2.21505300    0.23441100    0.18115500
H      -3.19972700   -0.21121800    0.35451000
H      -1.46058400   -0.33005700    0.76299600
H      -2.17098400    1.26107500    0.57311000

1D rotors:
pivots: [1, 4], dihedral: [6, 1, 4, 5], rotor symmetry: 1, max scan energy: 18.31 kJ/mol
pivots: [1, 6], dihedral: [4, 1, 6, 7], rotor symmetry: 1, max scan energy: 23.10 kJ/mol
pivots: [6, 7], dihedral: [1, 6, 7, 8], rotor symmetry: 1, max scan energy: 30.02 kJ/mol
""",
)

entry(
    index = 35,
    label = "cyanoisopropylOO + cyanoisopropylOO <=> cyanoisopropyl2_O4",
    kinetics = Arrhenius(A=(1.1e+7,'cm^3/(mol*s)'), n=0.0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'), Tmax=(350,'K')),
    longDesc =
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
    index = 38,
    label = "cyanoisopropyl2_O4 <=> cyanoisopropylO + cyanoisopropylO + O2",
    kinetics = Arrhenius(A=(4.5e+16,'s^-1'), n=0.0, Ea=(72.35,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'), Tmax=(350,'K')),
    longDesc =
"""
Taken from
SERGEY L. KHURSAN, Organic tetroxides and mechanism of peroxy radical recombination,
doi: 10.1002/9780470682531.pat0827
Table 3, an average of sources 66 and 79
""",
)

# entry(
#     index = 36,
#     label = "HO2 + OHCH2OO <=> O2 + OHCH2OOH",
#     degeneracy = 1.0,
#     kinetics = Arrhenius(A=(0,'cm^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
#                          Tmax=(350,'K')),
#     longDesc =
# """
# We assume that at **basic conditions** HO2 is in the O2(-) form and does not react in the same pathway
# """,
# )
#
# entry(
#     index = 37,
#     label = "HO2 + cyanoisopropylOO <=> O2 + cyanoisopropylOOH",
#     degeneracy = 1.0,
#     kinetics = Arrhenius(A=(0,'cm^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
#                          Tmax=(350,'K')),
#     longDesc =
# """
# We assume that at **basic conditions** HO2 is in the O2(-) form and does not react in the same pathway
# """,
# )

entry(
    index = 1052,
    label = 'OHCHOH + OHCH2OOH <=> OHCH2OH + OHCH2OO',
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.04944e+07,'cm^3/(mol*s)'), n=0, Ea=(17.4814,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
                         Tmax=(350,'K')),
    longDesc =
"""
dlpno-ccsd(T)/def2tzvp//wb97xd/def2tzvp with APFD SMD water for solvation sp correction 
""",
)

entry(
    index = 1053,
    label = 'OHCHOH + cyanoisopropylOOH <=> OHCH2OH + cyanoisopropylOO',
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.90093e+07,'cm^3/(mol*s)'), n=0, Ea=(23.8264,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
                         Tmax=(350,'K')),
    longDesc =
"""
dlpno-ccsd(T)/def2tzvp//wb97xd/def2tzvp with APFD SMD water for solvation sp correction 
""",
)

entry(
    index = 1055,
    label = 'CH2O + cyanoisopropylOO <=> CHO + cyanoisopropylOOH',
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(9.25121e+08,'cm^3/(mol*s)'), n=0, Ea=(41.2887,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
                         Tmax=(350,'K')),
    longDesc =
"""
dlpno-ccsd(T)/def2tzvp//wb97xd/def2tzvp with APFD SMD water for solvation sp correction 
""",
)

entry(
    index = 1058,
    label = 'H2O2 + OHCH2OO <=> HO2 + OHCH2OOH',
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(221744,'cm^3/(mol*s)'), n=0, Ea=(31.4438,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
                         Tmax=(350,'K')),
    longDesc =
"""
dlpno-ccsd(T)/def2tzvp//wb97xd/def2tzvp with APFD SMD water for solvation sp correction 
""",
)