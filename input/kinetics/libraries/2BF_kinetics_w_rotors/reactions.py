#!/usr/bin/env python
# encoding: utf-8

name = "2BF_kinetics"
shortDesc = u""
longDesc = u"""ARC v1.1.0

Levels of theory used:

Conformers:       wb97xd/def2svp, software: gaussian (dft)
TS guesses:       wb97xd/def2svp, software: gaussian (dft)
Composite method: cbs-qb3, software: gaussian (composite) (using a fine grid)
Frequencies:      b3lyp/cbsb7, software: gaussian (dft)
Rotor scans:      b3lyp/cbsb7, software: gaussian (dft)
Using p-type bond additivity corrections for thermo

Using the following ESS settings: {'gaussian': ['local'], 'molpro': ['local']}
"""

entry(
    index = 0,
    label = "R1_2 <=> P1_2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(100141,'s^-1'), n=2.22566, Ea=(335.982,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
TS method summary for TS0 in R1 <=> P1:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
O       0.20271600   -2.19516900    1.18722000
C      -2.13614100   -0.26237300   -1.10770200
C      -1.77946000   -0.11951700    0.39375500
C      -1.82285000    0.97883800   -1.94589600
C      -0.32994400    0.07587900    0.69151900
C       0.50770400   -1.03156700    0.91875300
C       1.93455400   -0.67259200    0.50795900
C       2.58716100    0.63488700    0.88795500
C       3.45625300    0.08635100    1.68598200
H      -3.20456400   -0.49318700   -1.18105700
H      -1.60264700   -1.13022700   -1.50832500
H      -2.10477200   -1.02590500    0.91322400
H      -2.34173100    0.73107600    0.80152800
H      -2.11754800    0.83480800   -2.98900100
H      -0.75362000    1.20915600   -1.93329400
H      -2.35776100    1.85695500   -1.56893200
H       0.09644500    1.06882200    0.63128500
H       2.26385300   -1.06483500   -0.45616600
H       2.41252500    1.63881600    0.52434300
H       2.69882800   -1.24887500    1.32141700
H       4.39090100    0.12856100    2.22553500

1D rotors:
pivots: [2, 4], dihedral: [3, 2, 4, 14], rotor symmetry: 3, max scan energy: 12.49 kJ/mol
pivots: [2, 3], dihedral: [4, 2, 3, 5], rotor symmetry: 1, max scan energy: 20.99 kJ/mol
pivots: [3, 5], dihedral: [2, 3, 5, 6], rotor symmetry: 1, max scan energy: 11.89 kJ/mol
* Invalidated! pivots: [6, 7], dihedral: [1, 6, 7, 8], invalidation reason: Pivots participate in the TS reaction zone (code: pivTS). Another conformer for TS0 exists which is 19.93 kJ/mol lower.
* Invalidated! pivots: [7, 8], dihedral: [6, 7, 8, 9], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
""",
)

entry(
    index = 1,
    label = "R1_3 <=> P1_3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.37891e+11,'s^-1'), n=0.390718, Ea=(122.16,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
TS method summary for TS0 in R1 <=> P1:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
C       2.61423600   -1.01037300    0.75953200
C       1.75187000   -0.45775000   -0.12212800
C       2.12965100   -0.13600700   -1.45618700
C       1.24305200    0.22006600   -2.55003800
O       1.38863000   -0.77925500   -3.33685300
C       0.46680200    1.34609900   -2.67271500
C       0.24260000    2.37634000   -1.61275900
C       0.81747900    3.76359500   -1.98348100
C       0.53259500    4.82771000   -0.92073000
H       3.62651300   -1.26862400    0.46701500
H       2.32892400   -1.21412500    1.78466600
H       0.73366800   -0.23947800    0.18466200
H       3.13781300   -0.38528400   -1.77226800
H      -0.05469100    1.46702600   -3.61909700
H      -0.83505900    2.49651600   -1.43110800
H       0.69147000    2.06263800   -0.66418500
H       1.89676700    3.66482200   -2.13922900
H       0.39641400    4.07737000   -2.94500600
H       0.97007700    4.55237400    0.04423300
H       0.94925800    5.79662700   -1.20875300
H      -0.54338500    4.96018800   -0.77044700

1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 2, max scan energy: 53.96 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Pivots participate in the TS reaction zone (code: pivTS). initial and final points are inconsistent by more than 5.00 kJ/mol
pivots: [6, 7], dihedral: [4, 6, 7, 8], rotor symmetry: 1, max scan energy: 21.36 kJ/mol
pivots: [7, 8], dihedral: [6, 7, 8, 9], rotor symmetry: 1, max scan energy: 21.48 kJ/mol
pivots: [8, 9], dihedral: [7, 8, 9, 19], rotor symmetry: 3, max scan energy: 11.72 kJ/mol
""",
)

# entry(
#     index = 2,
#     label = "R1_4 <=> P1_4",
#     degeneracy = 1.0,
#     kinetics = Arrhenius(A=(0.000124169,'s^-1'), n=4.86016, Ea=(120.639,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
#     longDesc = 
# """
# TS method summary for TS0 in R1 <=> P1:

# The method that generated the best TS guess and its output used for the optimization: user guess 0


# TS external symmetry: 1, TS optical isomers: 2

# Optimized TS geometry:
# C       3.06119000   -1.17552800   -0.34179400
# C       1.71722800   -0.90703000   -1.02466800
# C       0.80314000   -0.00277200   -0.18791100
# C      -0.57073800    0.28171400   -0.83032600
# C      -1.41495200    1.35154800   -0.02885400
# C      -2.47264500    0.54070800    0.63881500
# C      -2.52826100   -0.83898200    0.12340500
# C      -1.45874600   -0.98434500   -0.87641900
# O      -1.28517300   -1.93863000   -1.61423200
# H       2.92398600   -1.68558500    0.61694400
# H       3.60486600   -0.24537600   -0.14693000
# H       3.69960600   -1.80853600   -0.96350900
# H       1.88802700   -0.43228900   -1.99823500
# H       1.20581000   -1.84927000   -1.23488000
# H       1.30598500    0.95774500   -0.02070300
# H       0.65738400   -0.44711800    0.80600700
# H      -0.40958100    0.62702300   -1.85567400
# H      -0.78867900    1.92890500    0.65630300
# H      -1.88047400    2.06253600   -0.72407200
# H      -1.95504600   -0.55836500    1.21403700
# H      -3.34686400   -1.53371200    0.24441300

# 1D rotors:
# pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 11.84 kJ/mol
# pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 27.38 kJ/mol
# pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 21.38 kJ/mol
# """,
# )

# entry(
#     index = 3,
#     label = "R1_6 <=> P1_6",
#     degeneracy = 1.0,
#     kinetics = Arrhenius(A=(1.04212e-18,'s^-1'), n=9.10001, Ea=(108.465,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
#     longDesc = 
# """
# TS method summary for TS0 in R1 <=> P1:

# The method that generated the best TS guess and its output used for the optimization: user guess 0


# TS external symmetry: 1, TS optical isomers: 2

# Optimized TS geometry:
# C      -3.06811700    1.68094600    1.04223300
# C      -1.86657100    1.29813700    0.33366100
# C      -0.92410800    0.16115900    0.34473600
# C      -1.55268000   -1.19158400   -0.04368500
# O      -2.74604700   -1.35158000   -0.12369800
# C      -0.55267200   -2.31103900   -0.34003000
# C      -1.13512100   -3.68955800   -0.23451600
# C      -0.57662000   -4.69365300    0.43722500
# C      -1.14542200   -6.07742700    0.55012800
# H      -3.10574500    2.58383300    1.64910000
# H      -2.89613300    1.79751100   -0.26630000
# H      -0.50070000    0.01556000    1.35579300
# H      -0.06735400    0.34004300   -0.31586300
# H      -0.20668800   -2.11699300   -1.36811800
# H       0.33101800   -2.19818800    0.29603000
# H      -2.08490200   -3.83826700   -0.74094500
# H       0.36804100   -4.52105600    0.95308200
# H      -0.45263100   -6.82415200    0.14602200
# H      -2.09225800   -6.16589500    0.01278600
# H      -1.32151300   -6.34715000    1.59740300
# H      -3.84111300    0.92912500    1.19051100

# 1D rotors:
# * Invalidated! pivots: [1, 2], dihedral: [10, 1, 2, 3], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
# * Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Two consecutive points are inconsistent by more than 2.36 kJ/molTwo consecutive points are inconsistent by more than 2.36 kJ/molTwo consecutive points are inconsistent by more than 2.36 kJ/mol
# pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 7.64 kJ/mol
# pivots: [4, 6], dihedral: [3, 4, 6, 7], rotor symmetry: 1, max scan energy: 6.44 kJ/mol
# pivots: [6, 7], dihedral: [4, 6, 7, 8], rotor symmetry: 1, max scan energy: 16.29 kJ/mol
# * Invalidated! pivots: [7, 8], dihedral: [6, 7, 8, 9], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
# pivots: [8, 9], dihedral: [7, 8, 9, 18], rotor symmetry: 3, max scan energy: 7.94 kJ/mol
# """,
# )

entry(
    index = 4,
    label = "R1_9 <=> P1_9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.19541e-05,'s^-1'), n=4.9103, Ea=(249.983,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
TS method summary for TS0 in R1 <=> P1:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
O      -1.07656900   -0.95783100   -0.87178100
C       2.12304700    1.25939000    0.24551100
C       1.28548400   -0.01237700    0.43537600
C      -2.57689700   -0.09370200    0.61163600
C       3.59646300    0.96207100   -0.04467600
C      -1.23569300   -0.57586200    0.45775100
C      -0.15814200    0.27193800    0.78138900
C      -2.91693800    0.35330600   -0.64013200
C      -1.78420300    0.08175500   -1.47406000
H       1.69519100    1.84635500   -0.57429200
H       2.04584300    1.88490000    1.14329600
H       1.72395300   -0.60556400    1.25025200
H       1.32981400   -0.63056100   -0.46403400
H      -3.06440300    0.12217200    1.55017700
H       3.70605900    0.36020600   -0.95202300
H       4.16758600    1.88348100   -0.18623700
H       4.05936700    0.40715300    0.77737200
H      -0.29437300    0.89085600    1.66882400
H      -3.77733000    0.93995200   -0.92712700
H      -0.73199700    0.99359800   -0.57698200
H      -1.79255100    0.07079400   -2.55814600

1D rotors:
pivots: [2, 5], dihedral: [3, 2, 5, 15], rotor symmetry: 3, max scan energy: 11.94 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [5, 2, 3, 7], invalidation reason: Another conformer for TS0 exists which is 5.23 kJ/mol lower.
pivots: [3, 7], dihedral: [2, 3, 7, 6], rotor symmetry: 1, max scan energy: 15.31 kJ/mol
""",
)

entry(
    index = 5,
    label = "R1_10 <=> P1_10",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.00016379,'s^-1'), n=4.60084, Ea=(296.633,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
TS method summary for TS0 in R1 <=> P1:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
O      -1.19763900    0.06523800   -1.50080500
C       2.43375400   -0.69650400    0.37015000
C       1.09923100   -0.45710900   -0.30801400
C      -1.72078000   -0.38865500    0.68780200
C       3.43920900   -1.44485900   -0.51800300
C      -1.17528700   -0.88331200   -0.50669800
C       0.08750400   -1.44892700   -0.24772900
C      -1.36058900    0.97667900    0.59439400
C      -1.54401600    1.33533500   -0.86243500
H       2.85811600    0.27154200    0.65812800
H       2.28260000   -1.25076700    1.30327100
H       1.16156500    0.14385000   -1.20861500
H       0.18580600    0.60866100    0.44067100
H      -1.74405100   -0.96284600    1.60351600
H       3.62654800   -0.89676500   -1.44611100
H       4.39755100   -1.57605700   -0.00680700
H       3.06106000   -2.43419200   -0.78989900
H       0.15436500   -2.24915300    0.48283300
H      -1.51244400    1.70249500    1.38439000
H      -0.86139200    2.09926700   -1.23691000
H      -2.57238500    1.60168600   -1.13355100

1D rotors:
pivots: [2, 5], dihedral: [3, 2, 5, 15], rotor symmetry: 3, max scan energy: 12.64 kJ/mol
pivots: [2, 3], dihedral: [5, 2, 3, 7], rotor symmetry: 1, max scan energy: 12.97 kJ/mol
* Invalidated! pivots: [6, 7], dihedral: [1, 6, 7, 3], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
""",
)

entry(
    index = 6,
    label = "R1_13 <=> P1_13",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.15282e-05,'s^-1'), n=4.97677, Ea=(127.561,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
TS method summary for TS0 in R1 <=> P1:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
O      -0.37686400    2.15910000    0.26514200
C       2.81342500   -0.59261100   -0.78310900
C       1.78959300    0.34838500   -0.22854300
C       4.24628600   -0.28438900   -0.33276300
C       0.37231600   -0.04708400   -0.04819400
C      -0.67626700    0.96185600    0.12071100
C      -2.09585200    0.58457800    0.15763300
C      -2.65314400   -0.66963000   -0.08308400
C      -4.00160400   -0.94035700   -0.02406700
H       2.55345800   -1.62448800   -0.51762100
H       2.76487000   -0.55576000   -1.88385200
H       1.16990300   -0.02278700    0.92168900
H       1.98036200    1.41355800   -0.17844700
H       4.34586800   -0.37806300    0.75195000
H       4.53064300    0.73568400   -0.60575700
H       4.96064200   -0.96655900   -0.80072900
H       0.12101600   -1.08144500   -0.25034200
H      -1.99069200   -1.49257800   -0.33957800
H      -2.75069000    1.41866000    0.39148700
H      -4.38909400   -1.93015700   -0.22892400
H      -4.71700000   -0.16600500    0.22945100

1D rotors:
pivots: [2, 4], dihedral: [3, 2, 4, 14], rotor symmetry: 3, max scan energy: 11.93 kJ/mol
pivots: [2, 3], dihedral: [4, 2, 3, 5], rotor symmetry: 1, max scan energy: 11.17 kJ/mol
pivots: [5, 6], dihedral: [3, 5, 6, 1], rotor symmetry: 1, max scan energy: 47.37 kJ/mol
pivots: [7, 8], dihedral: [6, 7, 8, 9], rotor symmetry: 1, max scan energy: 59.02 kJ/mol
""",
)

entry(
    index = 7,
    label = "R1_8_0 <=> P1_8_0",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.2431e+10,'s^-1'), n=0.480246, Ea=(116.905,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
TS method summary for TS0 in R1 <=> P1:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
C      -3.37935600    0.12521900   -0.75181600
C      -3.85766000   -0.32235000    0.44378900
C      -3.02777500   -0.65931500    1.55478400
C      -1.77975900   -1.15574700    1.25630200
O      -0.76977400   -1.58776300    1.89862100
C      -1.29020700   -1.45636100   -0.08188000
C      -1.60634400   -2.72506800   -0.78924200
C      -0.71708200   -3.91303400   -0.31289000
C       0.77616100   -3.73937800   -0.59077200
H      -2.39721300    0.57128500   -0.84003400
H      -4.01710600    0.18271900   -1.62690000
H      -4.93109600   -0.48364200    0.54101300
H      -3.39482400   -0.66045200    2.57323100
H      -0.38621100   -0.92616200   -0.36823100
H      -1.43935100   -2.58087200   -1.86224900
H      -0.88000200   -4.05925300    0.75673800
H       1.19598400   -2.92030700   -0.00317100
H       0.96776300   -3.54005600   -1.65035500
H       1.32154100   -4.64761200   -0.32227600
H      -2.65558600   -2.98127300   -0.62907600
H      -1.09207200   -4.80472500   -0.82535100

1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [10, 1, 2, 3], invalidation reason: Pivots participate in the TS reaction zone (code: pivTS). initial and final points are inconsistent by more than 5.00 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
* Invalidated! pivots: [6, 7], dihedral: [4, 6, 7, 8], invalidation reason: Another conformer for TS0 exists which is 6.41 kJ/mol lower.Pivots participate in the TS reaction zone (code: pivTS). 
pivots: [7, 8], dihedral: [6, 7, 8, 9], rotor symmetry: 1, max scan energy: 24.88 kJ/mol
pivots: [8, 9], dihedral: [7, 8, 9, 17], rotor symmetry: 3, max scan energy: 12.37 kJ/mol
""",
)

entry(
    index = 8,
    label = "R1_11 <=> P1_11",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.56452,'s^-1'), n=2.434, Ea=(284.983,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
TS method summary for TS0 in R1 <=> P1:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
C      -3.39157500   -1.29754700   -0.67191700
C      -2.51079800   -0.48608400   -0.05273400
C      -1.11607000   -0.75937000    0.12252900
C      -0.14250400    0.25514300    0.62261100
C      -0.33271700    1.65080700    0.35127400
O      -0.94646100    2.61054300    0.63592400
C       1.31055900   -0.17738200    0.79677800
C       2.05874600   -0.43615000   -0.52046300
C       3.51894300   -0.83738000   -0.29779400
H      -3.09048200   -2.25249800   -1.08953300
H      -4.43351100   -1.02216000   -0.76998500
H      -0.70122400   -1.67054200   -0.29843200
H      -0.82960000   -0.25213400    1.46831700
H       1.84389000    0.58923400    1.36988400
H       1.31490500   -1.08818700    1.40709400
H       1.54603000   -1.22063900   -1.08693200
H       2.00884600    0.47071000   -1.13160800
H       4.06780800   -0.05488500    0.23528800
H       4.02971600   -1.01129600   -1.24818000
H       3.59465000   -1.75610700    0.29229100
H      -2.87334300    0.46371800    0.33794900

1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 50.21 kJ/mol
pivots: [4, 7], dihedral: [3, 4, 7, 8], rotor symmetry: 1, max scan energy: 19.33 kJ/mol
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: Pivots participate in the TS reaction zone (code: pivTS). initial and final points are inconsistent by more than 5.00 kJ/mol
pivots: [7, 8], dihedral: [4, 7, 8, 9], rotor symmetry: 1, max scan energy: 20.61 kJ/mol
pivots: [8, 9], dihedral: [7, 8, 9, 18], rotor symmetry: 3, max scan energy: 11.87 kJ/mol
""",
)

entry(
    index = 9,
    label = "R1_18 <=> P1_18",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.68355e-13,'s^-1'), n=7.07862, Ea=(78.0114,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
TS method summary for TS0 in R1 <=> P1:
Methods that successfully generated a TS guess:
user guess 0 + autotst,autotst,autotst,autotst,
The method that generated the best TS guess and its output used for the optimization: autotst


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
O      -2.20917500   -0.20117700    1.20579900
C       1.08775400   -1.20757400   -0.44126600
C      -0.03813900   -1.00399900    0.57757500
C       2.67112700    0.86706100   -0.14809300
C      -1.24367700   -0.29272800    0.23003500
C       2.11603700   -0.42563600    0.38222300
C      -1.65795800    0.41436300   -0.87570300
C      -2.94093800    0.95673100   -0.56220500
C      -3.22620400    0.55588100    0.70476300
H       0.87867200   -0.73546600   -1.40345800
H       1.33754900   -2.25368500   -0.62682700
H       0.90836300   -0.24217400    1.20729500
H      -0.17443700   -1.81549900    1.28917700
H       1.87346900    1.52012700   -0.51729700
H       3.22527200    1.41268900    0.61939200
H       3.35756400    0.69234900   -0.99012200
H       2.78745200   -1.03263900    0.98796800
H      -1.11740200    0.52474500   -1.80155400
H      -3.56872400    1.56032200   -1.19850700
H      -4.06660400    0.70660900    1.36080900

1D rotors:
* Invalidated! pivots: [2, 6], dihedral: [3, 2, 6, 4], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 3], dihedral: [6, 2, 3, 5], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
pivots: [3, 5], dihedral: [2, 3, 5, 1], rotor symmetry: 1, max scan energy: 29.65 kJ/mol
pivots: [4, 6], dihedral: [14, 4, 6, 2], rotor symmetry: 3, max scan energy: 9.63 kJ/mol
""",
)

entry(
    index = 10,
    label = "R1_19 <=> P1_19",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(170942,'s^-1'), n=1.74266, Ea=(10.3317,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
TS method summary for TS0 in R1 <=> P1:
Methods that successfully generated a TS guess:
user guess 0 + autotst,autotst,autotst,autotst,
The method that generated the best TS guess and its output used for the optimization: user guess 0 + autotst


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
O       2.64979800   -0.66848200   -0.29196500
C      -1.06624800   -1.12748900   -0.27488900
C      -1.40784700    0.12783300    0.52107600
C       0.36755200   -1.63914100   -0.01033000
C      -2.62774300    0.90010800    0.06242000
C       1.30852000   -0.48573500   -0.07779500
C       3.21990500    0.57776500   -0.25116300
C       2.28557400    1.53895200   -0.01886900
C       1.04320100    0.83126000    0.08242800
H      -0.37923100    0.84799900    0.35701800
H      -1.39949200   -0.05072900    1.60073700
H      -1.16413900   -0.90111400   -1.34243300
H      -1.78760000   -1.92372000   -0.05241800
H       0.42247100   -2.11860500    0.97626600
H       0.64137200   -2.40392300   -0.74324400
H      -2.54208700    1.18812800   -0.98953800
H      -3.53705000    0.29319600    0.16307200
H      -2.77385000    1.80844800    0.65223700
H       2.46260100    2.60004200    0.05405300
H       4.28419600    0.60530700   -0.41686700

1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [4, 2, 3, 5], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 4], dihedral: [3, 2, 4, 6], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
pivots: [3, 5], dihedral: [2, 3, 5, 16], rotor symmetry: 3, max scan energy: 9.80 kJ/mol
* Invalidated! pivots: [4, 6], dihedral: [2, 4, 6, 1], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
""",
)

entry(
    index = 11,
    label = "R1_22 + R2_22 <=> P1_22 + P2_22",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.0012455,'cm^3/(mol*s)'), n=3.61814, Ea=(21.8068,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
TS method summary for TS0 in R1 + R2 <=> P1 + P2:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
O       1.83236300    0.60869400   -0.20943400
C      -2.33237200    1.62600600   -0.76355500
C      -1.00309500    0.85415800   -0.79895800
C      -3.51112600    0.81767800   -0.21077300
C       0.93755000    0.46616000    0.81643400
C      -0.47414200    0.38263300    0.49545200
C       1.62135700    0.38872800    2.00552800
C       3.00546800    0.49878700    1.69154600
C       3.07533400    0.62684800    0.33733600
H      -2.19993000    2.54732200   -0.18395000
H      -2.56250300    1.93716500   -1.78720700
H      -0.23501500    1.36855300   -1.37968400
H      -1.20789700   -0.09827400   -1.41208400
H      -3.37050300    0.55031500    0.84073000
H      -4.43883100    1.39141300   -0.27792500
H      -3.63489000   -0.11154900   -0.77168100
H      -1.10734400    0.53846200    1.36845400
H       1.17883800    0.26739300    2.98158700
H       3.83747500    0.48597900    2.37697400
H       3.89127700    0.73943100   -0.35632100
O      -1.06421500   -1.95011300   -0.12993300
O      -1.45839600   -1.71348600   -1.34946000
H      -0.68037900   -0.89680000    0.36191900

1D rotors:
pivots: [2, 4], dihedral: [3, 2, 4, 14], rotor symmetry: 3, max scan energy: 12.14 kJ/mol
pivots: [2, 3], dihedral: [4, 2, 3, 6], rotor symmetry: 1, max scan energy: 18.52 kJ/mol
* Invalidated! pivots: [3, 6], dihedral: [2, 3, 6, 5], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
""",
)

entry(
    index = 12,
    label = "R1_30 <=> P1_30",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.247407,'s^-1'), n=3.54516, Ea=(40.9301,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
TS method summary for TS0 in R1 <=> P1:
Methods that successfully generated a TS guess:
user guess 0 + autotst,autotst,autotst,autotst,
The method that generated the best TS guess and its output used for the optimization: user guess 0 + autotst


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
O       1.99810900    1.01139900   -0.87807900
C      -2.59608000   -0.13683700    0.06612800
C      -1.30055300   -0.79516600   -0.46899600
C      -2.14356200    0.88744800    1.08726600
C       1.11593500    0.08557500   -0.37136500
C      -0.29275600    0.34975200   -0.56998300
C       1.82646700   -0.89139500    0.28687600
C       3.20691800   -0.54841600    0.17299500
C       3.25427200    0.60949400   -0.53841200
H      -3.28667400   -0.88045600    0.47759200
H      -3.11871400    0.36453700   -0.75503500
H      -1.44555500   -1.31920200   -1.41778700
H      -0.94489100   -1.53363300    0.25664800
H      -0.84052700    1.02745200    0.40207000
H      -1.84131400    0.50699300    2.06196700
H      -2.64618300    1.84952600    1.12980000
H      -0.46630100    1.01676000   -1.41666800
H       1.41221200   -1.75160900    0.78718600
H       4.05118200   -1.09319900    0.56502300
H       4.05781500    1.24107900   -0.87742200

1D rotors:
* Invalidated! pivots: [2, 4], dihedral: [3, 2, 4, 15], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 3], dihedral: [4, 2, 3, 6], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 6], dihedral: [2, 3, 6, 5], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
pivots: [5, 6], dihedral: [1, 5, 6, 3], rotor symmetry: 1, max scan energy: 31.59 kJ/mol
""",
)

entry(
    index = 13,
    label = "R1_21 + R2_21 <=> P1_21 + P2_21",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.00593909,'cm^3/(mol*s)'), n=3.90095, Ea=(11.2656,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
TS method summary for TS0 in R1 + R2 <=> P1 + P2:
Methods that successfully generated a TS guess:
user guess 0,autotst,autotst,autotst,autotst,heuristics,heuristics,heuristics,heuristics,heuristics,heuristics,heuristics,
The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
O       0.38262500   -2.83523400    1.67003100
C      -1.67283700   -2.29167100   -0.34573100
C      -1.83598800   -3.66044600   -1.02673700
C      -0.25141100   -1.74101900   -0.39735400
C      -3.27490300   -4.18214300   -0.97462100
C       0.75896400   -2.39958300    0.42105700
C       2.09888100   -2.64194700    0.25077600
C       2.56695800   -3.26095000    1.45112200
C       1.49073800   -3.35512900    2.27456300
H      -1.51033700   -3.58363000   -2.07103300
H      -1.16542300   -4.38213500   -0.54866400
H      -1.99110500   -2.36984700    0.69882700
H      -2.34620900   -1.57078200   -0.82436300
H      -0.35231800   -0.50814400    0.00351600
H       0.11458100   -1.60824600   -1.41814400
H      -3.96522300   -3.49390500   -1.47275900
H      -3.36391900   -5.15477800   -1.46631400
H      -3.61463700   -4.30030300    0.05902000
H       2.67340200   -2.41265700   -0.63275000
H       3.56870600   -3.59715500    1.66765600
H       1.34303700   -3.74989400    3.26533900
O       0.48328100    3.72367500   -1.88107100
C       0.88762800    1.44328400    0.14089700
C       1.00907900    2.97477000    0.37511000
C      -0.94393400    0.79799400    1.85002100
C       0.18005800    3.80057200   -0.54706200
C      -0.48312200    0.86722700    0.41363600
C      -0.86515200    4.65504200   -0.36927800
C      -1.23144000    5.13941400   -1.66944200
C      -0.38431800    4.54305600   -2.54440300
H       1.17640500    1.23948500   -0.89543400
H       1.62770200    0.94551300    0.77828700
H       0.72630000    3.22380600    1.40110200
H       2.06268100    3.25723800    0.26183100
H      -1.09970900    1.79777900    2.27961400
H      -0.20964300    0.28496100    2.47943000
H      -1.89347800    0.26371800    1.94054000
H      -1.25116300    1.21371000   -0.28048100
H      -1.31956900    4.91266100    0.57443100
H      -2.01791900    5.83632000   -1.91204400
H      -0.26347900    4.58727900   -3.61340100

1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [4, 2, 3, 5], invalidation reason: Another conformer for TS0 exists which is 2.77 kJ/mol lower.
pivots: [2, 4], dihedral: [3, 2, 4, 6], rotor symmetry: 1, max scan energy: 18.98 kJ/mol
pivots: [3, 5], dihedral: [2, 3, 5, 16], rotor symmetry: 3, max scan energy: 11.81 kJ/mol
pivots: [4, 6], dihedral: [2, 4, 6, 1], rotor symmetry: 1, max scan energy: 27.14 kJ/mol
* Invalidated! pivots: [23, 27], dihedral: [24, 23, 27, 25], invalidation reason: Two consecutive points are inconsistent by more than 6.72 kJ/molTwo consecutive points are inconsistent by more than 8.77 kJ/molTwo consecutive points are inconsistent by more than 8.77 kJ/mol
pivots: [23, 24], dihedral: [27, 23, 24, 26], rotor symmetry: 1, max scan energy: 20.62 kJ/mol
pivots: [24, 26], dihedral: [23, 24, 26, 22], rotor symmetry: 1, max scan energy: 9.79 kJ/mol
pivots: [25, 27], dihedral: [35, 25, 27, 23], rotor symmetry: 3, max scan energy: 6.92 kJ/mol
""",
)

entry(
    index = 14,
    label = "R1_31 + R2_31 <=> P1_31 + P2_31",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.00593909,'cm^3/(mol*s)'), n=3.90095, Ea=(11.2656,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
TS method summary for TS0 in R1 + R2 <=> P1 + P2:
Methods that successfully generated a TS guess:
user guess 0,autotst,autotst,autotst,autotst,heuristics,heuristics,heuristics,heuristics,heuristics,heuristics,heuristics,
The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
O       0.38262500   -2.83523400    1.67003100
C      -1.67283700   -2.29167100   -0.34573100
C      -1.83598800   -3.66044600   -1.02673700
C      -0.25141100   -1.74101900   -0.39735400
C      -3.27490300   -4.18214300   -0.97462100
C       0.75896400   -2.39958300    0.42105700
C       2.09888100   -2.64194700    0.25077600
C       2.56695800   -3.26095000    1.45112200
C       1.49073800   -3.35512900    2.27456300
H      -1.51033700   -3.58363000   -2.07103300
H      -1.16542300   -4.38213500   -0.54866400
H      -1.99110500   -2.36984700    0.69882700
H      -2.34620900   -1.57078200   -0.82436300
H      -0.35231800   -0.50814400    0.00351600
H       0.11458100   -1.60824600   -1.41814400
H      -3.96522300   -3.49390500   -1.47275900
H      -3.36391900   -5.15477800   -1.46631400
H      -3.61463700   -4.30030300    0.05902000
H       2.67340200   -2.41265700   -0.63275000
H       3.56870600   -3.59715500    1.66765600
H       1.34303700   -3.74989400    3.26533900
O       0.48328100    3.72367500   -1.88107100
C       0.88762800    1.44328400    0.14089700
C       1.00907900    2.97477000    0.37511000
C      -0.94393400    0.79799400    1.85002100
C       0.18005800    3.80057200   -0.54706200
C      -0.48312200    0.86722700    0.41363600
C      -0.86515200    4.65504200   -0.36927800
C      -1.23144000    5.13941400   -1.66944200
C      -0.38431800    4.54305600   -2.54440300
H       1.17640500    1.23948500   -0.89543400
H       1.62770200    0.94551300    0.77828700
H       0.72630000    3.22380600    1.40110200
H       2.06268100    3.25723800    0.26183100
H      -1.09970900    1.79777900    2.27961400
H      -0.20964300    0.28496100    2.47943000
H      -1.89347800    0.26371800    1.94054000
H      -1.25116300    1.21371000   -0.28048100
H      -1.31956900    4.91266100    0.57443100
H      -2.01791900    5.83632000   -1.91204400
H      -0.26347900    4.58727900   -3.61340100

1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [4, 2, 3, 5], invalidation reason: Another conformer for TS0 exists which is 2.77 kJ/mol lower.
pivots: [2, 4], dihedral: [3, 2, 4, 6], rotor symmetry: 1, max scan energy: 18.98 kJ/mol
pivots: [3, 5], dihedral: [2, 3, 5, 16], rotor symmetry: 3, max scan energy: 11.81 kJ/mol
pivots: [4, 6], dihedral: [2, 4, 6, 1], rotor symmetry: 1, max scan energy: 27.14 kJ/mol
* Invalidated! pivots: [23, 27], dihedral: [24, 23, 27, 25], invalidation reason: Two consecutive points are inconsistent by more than 6.72 kJ/molTwo consecutive points are inconsistent by more than 8.77 kJ/molTwo consecutive points are inconsistent by more than 8.77 kJ/mol
pivots: [23, 24], dihedral: [27, 23, 24, 26], rotor symmetry: 1, max scan energy: 20.62 kJ/mol
pivots: [24, 26], dihedral: [23, 24, 26, 22], rotor symmetry: 1, max scan energy: 9.79 kJ/mol
pivots: [25, 27], dihedral: [35, 25, 27, 23], rotor symmetry: 3, max scan energy: 6.92 kJ/mol
""",
)

entry(
    index = 15,
    label = "R1_32 + R2_32 <=> P1_32 + P2_32",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.0012455,'cm^3/(mol*s)'), n=3.61814, Ea=(21.8068,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
TS method summary for TS0 in R1 + R2 <=> P1 + P2:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
O       1.83236300    0.60869400   -0.20943400
C      -2.33237200    1.62600600   -0.76355500
C      -1.00309500    0.85415800   -0.79895800
C      -3.51112600    0.81767800   -0.21077300
C       0.93755000    0.46616000    0.81643400
C      -0.47414200    0.38263300    0.49545200
C       1.62135700    0.38872800    2.00552800
C       3.00546800    0.49878700    1.69154600
C       3.07533400    0.62684800    0.33733600
H      -2.19993000    2.54732200   -0.18395000
H      -2.56250300    1.93716500   -1.78720700
H      -0.23501500    1.36855300   -1.37968400
H      -1.20789700   -0.09827400   -1.41208400
H      -3.37050300    0.55031500    0.84073000
H      -4.43883100    1.39141300   -0.27792500
H      -3.63489000   -0.11154900   -0.77168100
H      -1.10734400    0.53846200    1.36845400
H       1.17883800    0.26739300    2.98158700
H       3.83747500    0.48597900    2.37697400
H       3.89127700    0.73943100   -0.35632100
O      -1.06421500   -1.95011300   -0.12993300
O      -1.45839600   -1.71348600   -1.34946000
H      -0.68037900   -0.89680000    0.36191900

1D rotors:
pivots: [2, 4], dihedral: [3, 2, 4, 14], rotor symmetry: 3, max scan energy: 12.14 kJ/mol
pivots: [2, 3], dihedral: [4, 2, 3, 6], rotor symmetry: 1, max scan energy: 18.52 kJ/mol
* Invalidated! pivots: [3, 6], dihedral: [2, 3, 6, 5], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
""",
)



