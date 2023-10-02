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

entry(
    index = 2,
    label = "R1_4 <=> P1_4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.000124169,'s^-1'), n=4.86016, Ea=(120.639,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
TS method summary for TS0 in R1 <=> P1:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
C       3.06119000   -1.17552800   -0.34179400
C       1.71722800   -0.90703000   -1.02466800
C       0.80314000   -0.00277200   -0.18791100
C      -0.57073800    0.28171400   -0.83032600
C      -1.41495200    1.35154800   -0.02885400
C      -2.47264500    0.54070800    0.63881500
C      -2.52826100   -0.83898200    0.12340500
C      -1.45874600   -0.98434500   -0.87641900
O      -1.28517300   -1.93863000   -1.61423200
H       2.92398600   -1.68558500    0.61694400
H       3.60486600   -0.24537600   -0.14693000
H       3.69960600   -1.80853600   -0.96350900
H       1.88802700   -0.43228900   -1.99823500
H       1.20581000   -1.84927000   -1.23488000
H       1.30598500    0.95774500   -0.02070300
H       0.65738400   -0.44711800    0.80600700
H      -0.40958100    0.62702300   -1.85567400
H      -0.78867900    1.92890500    0.65630300
H      -1.88047400    2.06253600   -0.72407200
H      -1.95504600   -0.55836500    1.21403700
H      -3.34686400   -1.53371200    0.24441300

1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 11.84 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 27.38 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 21.38 kJ/mol
""",
)

entry(
    index = 3,
    label = "R1_6 <=> P1_6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.04212e-18,'s^-1'), n=9.10001, Ea=(108.465,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
TS method summary for TS0 in R1 <=> P1:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
C      -3.06811700    1.68094600    1.04223300
C      -1.86657100    1.29813700    0.33366100
C      -0.92410800    0.16115900    0.34473600
C      -1.55268000   -1.19158400   -0.04368500
O      -2.74604700   -1.35158000   -0.12369800
C      -0.55267200   -2.31103900   -0.34003000
C      -1.13512100   -3.68955800   -0.23451600
C      -0.57662000   -4.69365300    0.43722500
C      -1.14542200   -6.07742700    0.55012800
H      -3.10574500    2.58383300    1.64910000
H      -2.89613300    1.79751100   -0.26630000
H      -0.50070000    0.01556000    1.35579300
H      -0.06735400    0.34004300   -0.31586300
H      -0.20668800   -2.11699300   -1.36811800
H       0.33101800   -2.19818800    0.29603000
H      -2.08490200   -3.83826700   -0.74094500
H       0.36804100   -4.52105600    0.95308200
H      -0.45263100   -6.82415200    0.14602200
H      -2.09225800   -6.16589500    0.01278600
H      -1.32151300   -6.34715000    1.59740300
H      -3.84111300    0.92912500    1.19051100

1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [10, 1, 2, 3], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Two consecutive points are inconsistent by more than 2.36 kJ/molTwo consecutive points are inconsistent by more than 2.36 kJ/molTwo consecutive points are inconsistent by more than 2.36 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 7.64 kJ/mol
pivots: [4, 6], dihedral: [3, 4, 6, 7], rotor symmetry: 1, max scan energy: 6.44 kJ/mol
pivots: [6, 7], dihedral: [4, 6, 7, 8], rotor symmetry: 1, max scan energy: 16.29 kJ/mol
* Invalidated! pivots: [7, 8], dihedral: [6, 7, 8, 9], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
pivots: [8, 9], dihedral: [7, 8, 9, 18], rotor symmetry: 3, max scan energy: 7.94 kJ/mol
""",
)

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
    index = 4,
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
    index = 5,
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
    index = 6,
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
    index = 7,
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







