#!/usr/bin/env python
# encoding: utf-8

name = "2BF_H_Abs"
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
    label = "2BF + H_rad <=> PB1 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.16141e+06,'cm^3/(mol*s)'), n=2.42715, Ea=(41.9992,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
RXN_24
TS method summary for TS0 in 2BF + H_rad <=> PB1 + H2:
Methods that successfully generated a TS guess:
autotst,autotst,autotst,autotst,heuristics,
The method that generated the best TS guess and its output used for the optimization: autotst


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
O      -2.28197900    0.80914800    0.29435600
C       0.73354300    0.19996100    0.14004900
C      -0.30286500    0.22550700   -0.99912300
C       2.14396900    0.57010900   -0.33351300
C      -1.69052000   -0.08736200   -0.55591300
C      -2.54954900   -1.11459600   -0.80127900
C      -3.74693700   -0.83943300   -0.05999300
C      -3.52901400    0.33420900    0.58332300
C       3.17270200    0.56485700    0.77088100
H       0.74624700   -0.79740900    0.59182700
H       0.41677900    0.89449800    0.92501500
H       2.11785100    1.57026900   -0.79279900
H       2.45936100   -0.11311000   -1.13198600
H      -0.29008100    1.21454400   -1.47441400
H      -0.02432300   -0.49750700   -1.77167200
H      -2.35580500   -1.96581200   -1.43485100
H      -4.64342800   -1.43732700   -0.01720300
H       4.19582500    0.78453300    0.46807700
H       2.88889600    1.08598900    1.68548000
H      -4.11983600    0.94151000    1.24767700
H       3.36718000   -1.61403200    1.46178200
H       3.29208300   -0.72854600    1.20418200

1D rotors:
pivots: [2, 4], dihedral: [3, 2, 4, 9], rotor symmetry: 1, max scan energy: 23.07 kJ/mol
pivots: [2, 3], dihedral: [4, 2, 3, 5], rotor symmetry: 1, max scan energy: 18.39 kJ/mol
pivots: [3, 5], dihedral: [2, 3, 5, 1], rotor symmetry: 1, max scan energy: 8.48 kJ/mol
pivots: [4, 9], dihedral: [2, 4, 9, 18], rotor symmetry: 1, max scan energy: 12.23 kJ/mol
""",
)

entry(
    index = 1,
    label = "2BF + OH_rad <=> PB1 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.91773,'cm^3/(mol*s)'), n=3.44955, Ea=(9.59285,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
RXN 25
TS method summary for TS0 in 2BF + OH_rad <=> PB1 + H2O:
Methods that successfully generated a TS guess:
autotst,autotst,autotst,autotst,heuristics,heuristics,heuristics,heuristics,heuristics,heuristics,
The method that generated the best TS guess and its output used for the optimization: autotst


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
O      -2.88948300    0.61186300    0.12640000
O       2.73660300    0.85385200   -1.07465200
C       0.21508500   -1.49836300   -0.21990200
C       1.04598400   -1.02912000    0.98374600
C      -1.28591800   -1.20387900   -0.08922400
C       2.53638800   -1.00449600    0.70285000
C      -1.61871800    0.24694900   -0.22821700
C      -0.93774900    1.33866600   -0.67771600
C      -1.84541400    2.44829900   -0.59693500
C      -3.00797100    1.95236400   -0.10646500
H       0.85254700   -1.68917600    1.84107600
H       0.71905600   -0.03155400    1.29246700
H       0.35419700   -2.57602100   -0.35504700
H       0.59791700   -1.02327100   -1.12821800
H      -1.66162800   -1.56207900    0.87712500
H      -1.83637500   -1.76849600   -0.85186900
H       2.73595700   -0.23041400   -0.17102000
H       2.93053500   -1.94159100    0.29968600
H       3.14334500   -0.67092500    1.54686300
H       0.08642400    1.35357700   -1.01827400
H      -1.65058400    3.47332900   -0.87017900
H      -3.96487400    2.38626300    0.12877700
H       2.74457400    1.56412200   -0.41127500

1D rotors:
* Invalidated! pivots: [3, 4], dihedral: [5, 3, 4, 6], invalidation reason: Two consecutive points are inconsistent by more than 10.52 kJ/molTwo consecutive points are inconsistent by more than 10.52 kJ/mol
pivots: [3, 5], dihedral: [4, 3, 5, 7], rotor symmetry: 1, max scan energy: 17.69 kJ/mol
pivots: [4, 6], dihedral: [3, 4, 6, 17], rotor symmetry: 4, max scan energy: 17.84 kJ/mol
* Invalidated! pivots: [5, 7], dihedral: [3, 5, 7, 1], invalidation reason: Two consecutive points are inconsistent by more than 3.56 kJ/molTwo consecutive points are inconsistent by more than 3.56 kJ/mol
""",
)

entry(
    index = 2,
    label = "2BF + H_rad <=> PB2 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.14855e+06,'cm^3/(mol*s)'), n=2.32566, Ea=(31.257,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
RXN 27
TS method summary for TS0 in 2BF + H_rad <=> PB2 + H2:
Methods that successfully generated a TS guess:
autotst,autotst,autotst,autotst,heuristics,
The method that generated the best TS guess and its output used for the optimization: autotst


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
O       1.65971700    0.62867700    1.51647100
C      -0.78204700    0.10215800   -0.27394700
C       0.49536700   -0.74684800   -0.12195400
C      -3.29774700    0.05398200   -0.81969700
C       1.69335000    0.04310600    0.27885900
C      -1.99667600   -0.70492400   -0.68131100
C       2.87168500    0.34346800   -0.33338600
C       3.61563200    1.16326500    0.57958600
C       2.83519200    1.30352600    1.67962500
H      -0.98326300    0.62356700    0.66806200
H      -0.60057200    0.88691800   -1.02258200
H       0.72231700   -1.24767400   -1.06775700
H       0.31403200   -1.53496500    0.61805000
H      -3.52846800    0.61444700    0.09113200
H      -3.24420300    0.77573100   -1.64437900
H      -4.13452900   -0.61861800   -1.02440600
H      -1.80217200   -1.38266900   -1.51737100
H       3.17727300    0.01830200   -1.31545300
H       4.59682800    1.58549200    0.43134000
H       2.95408100    1.81806300    2.61789700
H      -2.36802900   -2.15995000    1.04200400
H      -2.19767100   -1.56485600    0.29942000

1D rotors:
pivots: [2, 6], dihedral: [3, 2, 6, 4], rotor symmetry: 1, max scan energy: 18.06 kJ/mol
pivots: [2, 3], dihedral: [6, 2, 3, 5], rotor symmetry: 1, max scan energy: 20.94 kJ/mol
pivots: [3, 5], dihedral: [2, 3, 5, 1], rotor symmetry: 1, max scan energy: 8.57 kJ/mol
pivots: [4, 6], dihedral: [14, 4, 6, 2], rotor symmetry: 3, max scan energy: 8.88 kJ/mol
""",
)

entry(
    index = 3,
    label = "2BF + H_rad <=> PB3 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.89638e+06,'cm^3/(mol*s)'), n=2.37908, Ea=(33.5525,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
RXN 30
TS method summary for TS0 in 2BF + H_rad <=> PB3 + H2:
Methods that successfully generated a TS guess:
autotst,autotst,autotst,autotst,heuristics,
The method that generated the best TS guess and its output used for the optimization: autotst


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
O       1.23679200    0.84501200    0.86247100
C      -1.80503700   -0.17644200    0.26487800
C       0.23246400    0.35122500   -1.30767200
C      -2.25195900    1.25786000    0.59554300
C       1.26584600    0.06964200   -0.26809800
C      -1.12993500   -0.30551900   -1.08620400
C       2.28364000   -0.82945200   -0.17387000
C       2.92295000   -0.60147000    1.08944800
C       2.25008000    0.42115700    1.67322300
H      -1.13102500   -0.53429000    1.04905500
H      -2.67811200   -0.83791500    0.27928800
H       0.10202100    1.43917700   -1.38044000
H       0.62398900    0.02752100   -2.27649600
H      -2.92331200    1.65221700   -0.17348900
H      -2.78662300    1.28266000    1.54919700
H      -1.39520300    1.93002100    0.67920800
H      -1.80688300   -0.09839000   -1.92025100
H       2.54623900   -1.56885900   -0.91375200
H       3.77055700   -1.12765800    1.49890600
H       2.35477900    0.94661500    2.60707000
H      -0.76284100   -2.53984300   -1.39085000
H      -0.91852700   -1.60307000   -1.25716500

1D rotors:
pivots: [2, 4], dihedral: [6, 2, 4, 14], rotor symmetry: 3, max scan energy: 12.19 kJ/mol
pivots: [2, 6], dihedral: [4, 2, 6, 3], rotor symmetry: 1, max scan energy: 22.43 kJ/mol
pivots: [3, 6], dihedral: [5, 3, 6, 2], rotor symmetry: 1, max scan energy: 12.58 kJ/mol
pivots: [3, 5], dihedral: [6, 3, 5, 1], rotor symmetry: 1, max scan energy: 11.26 kJ/mol
""",
)

entry(
    index = 4,
    label = "2BF + O2 <=> PB4 + OO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.10782,'cm^3/(mol*s)'), n=3.62706, Ea=(139.781,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
RXN 32
TS method summary for TS0 in 2BF + O2 <=> PB4 + OO:
Methods that successfully generated a TS guess:
user guess 0 + heuristics,autotst,autotst,autotst,autotst,heuristics,
The method that generated the best TS guess and its output used for the optimization: autotst


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
O      -1.48759800   -0.33253000    0.77779700
O      -0.44521700    3.20926800   -0.13778400
O      -1.73445100    3.24697500   -0.18680700
C       1.27776100    0.37103400    0.27084800
C       1.89615100   -1.01633300    0.00124100
C       0.13290000    0.71118100   -0.65856700
C       3.07226400   -1.32678500    0.93074000
C      -1.16101400    0.17383200   -0.46064500
C      -2.28629200    0.09585500   -1.27904700
C      -3.32076900   -0.48224500   -0.50752700
C      -2.79058300   -0.72167200    0.72842000
H       1.11937800   -1.77897200    0.11744200
H       2.22637400   -1.06622400   -1.04261400
H       0.93090800    0.41305700    1.30758000
H       2.06015100    1.13166300    0.17028300
H      -0.14912400    2.14301000   -0.35237200
H       0.38795300    0.85766200   -1.70767000
H       3.49154300   -2.31463100    0.72182200
H       2.76135800   -1.31230400    1.97975800
H       3.87573200   -0.59306300    0.81307100
H      -2.33695900    0.42925100   -2.30290400
H      -4.33190700   -0.69212600   -0.81764400
H      -3.18856300   -1.14600400    1.63467800

1D rotors:
* Invalidated! pivots: [4, 5], dihedral: [6, 4, 5, 7], invalidation reason: Another conformer for TS0 exists which is 2.72 kJ/mol lower.Another conformer for TS0 exists which is 2.72 kJ/mol lower.
pivots: [4, 6], dihedral: [5, 4, 6, 8], rotor symmetry: 1, max scan energy: 18.65 kJ/mol
pivots: [5, 7], dihedral: [4, 5, 7, 18], rotor symmetry: 3, max scan energy: 11.76 kJ/mol
""",
)

entry(
    index = 5,
    label = "2BF + H_rad <=> PB4 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(577896,'cm^3/(mol*s)'), n=2.32877, Ea=(19.8163,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
RXN 33
TS method summary for TS0 in 2BF + H_rad <=> PB4 + H2:
Methods that successfully generated a TS guess:
autotst,autotst,autotst,autotst,heuristics,
The method that generated the best TS guess and its output used for the optimization: autotst


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
O      -1.79527700    0.38964000    0.42251800
C       1.78722200    0.52475200    0.05222800
C       0.97808100   -0.54801400    0.79487800
C       2.83820700    1.19417400    0.94239600
C      -1.21395800   -0.42822600   -0.51194300
C      -0.06903500   -1.24248900   -0.07907300
C      -1.90333000   -0.32905900   -1.68858600
C      -2.96512500    0.60374700   -1.46981000
C      -2.85223700    1.00603900   -0.17723400
H       1.10475600    1.28382900   -0.34432100
H       2.27809300    0.06967400   -0.81654400
H       0.47875100   -0.09769100    1.65840400
H       1.65894400   -1.31022100    1.18987600
H       3.40097600    1.95216300    0.39094200
H       3.55544400    0.46316400    1.32857400
H       2.37208100    1.68592500    1.80166900
H       0.38028000   -1.73151700   -0.94742100
H      -1.67580600   -0.85774000   -2.60074800
H      -3.70756900    0.93122700   -2.18002600
H      -3.40785100    1.69125800    0.44017000
H      -0.76158800   -3.09232700    1.22753600
H      -0.48115900   -2.15830900    0.56641800

1D rotors:
pivots: [2, 4], dihedral: [3, 2, 4, 14], rotor symmetry: 3, max scan energy: 11.85 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [4, 2, 3, 6], invalidation reason: Another conformer for TS0 exists which is 2.88 kJ/mol lower.Another conformer for TS0 exists which is 2.88 kJ/mol lower.
pivots: [3, 6], dihedral: [2, 3, 6, 5], rotor symmetry: 1, max scan energy: 19.06 kJ/mol
pivots: [5, 6], dihedral: [1, 5, 6, 3], rotor symmetry: 1, max scan energy: 26.37 kJ/mol
""",
)

entry(
    index = 6,
    label = "2BF + H_rad <=> PB5 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.66097e+09,'cm^3/(mol*s)'), n=1.75193, Ea=(91.7471,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
RXN 36
TS method summary for TS0 in 2BF + H_rad <=> PB5 + H2:
Methods that successfully generated a TS guess:
autotst,autotst,autotst,autotst,heuristics,
The method that generated the best TS guess and its output used for the optimization: heuristics


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
C      -0.11490600   -2.39489300   -3.37135500
C      -0.10920400   -2.39698800   -1.84017700
C      -0.09768800   -0.98825100   -1.23809100
C      -0.09130700   -0.99488100    0.30268300
C      -0.05125200    0.36317400    0.90982700
C      -0.90407300    1.11432300    1.64548900
C      -0.30579700    2.37659100    1.93201500
C       0.91186400    2.31447400    1.33136000
O       1.09118800    1.11188300    0.70797200
H       0.76860000   -1.88587100   -3.76869800
H      -0.12033000   -3.41231900   -3.77153400
H      -0.99710900   -1.87905500   -3.76279200
H       0.76554600   -2.95119100   -1.47875500
H      -0.98754600   -2.94131000   -1.47224500
H      -0.97284600   -0.42881400   -1.58797500
H       0.78226100   -0.44242000   -1.59501100
H       0.77143500   -1.57239900    0.65712100
H      -0.98483100   -1.50233900    0.67728600
H      -2.36149700    0.62443600    2.12380100
H      -0.71304700    3.20056100    2.49486500
H       1.73481900    3.00556000    1.25626700
H      -3.09571800    0.37595500    2.36681800

1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 11.89 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 23.54 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 18.92 kJ/mol
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 8.06 kJ/mol
""",
)

entry(
    index = 7,
    label = "2BF + OH_rad <=> PB5 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(12.6483,'cm^3/(mol*s)'), n=3.64572, Ea=(19.2953,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
RXN 37
TS method summary for TS0 in 2BF + OH_rad <=> PB5 + H2O:
Methods that successfully generated a TS guess:
autotst,autotst,autotst,autotst,heuristics,heuristics,
The method that generated the best TS guess and its output used for the optimization: autotst


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
O      -1.57137900   -1.87556900   -1.39671300
O      -1.27045900    1.58342000    1.61278900
C       1.02957200    0.79245400   -0.82320000
C       1.81547800    0.13512000    0.31796400
C       0.16900000   -0.18531900   -1.63860600
C       2.59790800    1.14934800    1.15673000
C      -1.02007700   -0.71648200   -0.90826100
C      -1.78296100   -0.30672400    0.14034400
C      -2.82934300   -1.25661900    0.35334600
C      -2.65609100   -2.18338200   -0.62272300
H       2.50359700   -0.61039800   -0.09884800
H       1.12595200   -0.41812300    0.96454000
H       0.39496400    1.58401300   -0.41434400
H       1.73323000    1.27902100   -1.50738300
H      -0.17854300    0.31157000   -2.55322000
H       0.77271600   -1.03759500   -1.97022500
H       3.30812500    1.71025400    0.54124000
H       1.92126200    1.87236300    1.62182100
H       3.16498400    0.65815700    1.95225000
H      -3.60555600   -1.23271100    1.10043200
H      -1.62223900    0.80150900    0.82351600
H      -3.19204500   -3.07436100   -0.90312300
H      -0.80839600    1.02015200    2.25157200

1D rotors:
pivots: [3, 4], dihedral: [5, 3, 4, 6], rotor symmetry: 1, max scan energy: 24.48 kJ/mol
pivots: [3, 5], dihedral: [4, 3, 5, 7], rotor symmetry: 1, max scan energy: 17.65 kJ/mol
pivots: [4, 6], dihedral: [3, 4, 6, 17], rotor symmetry: 3, max scan energy: 12.04 kJ/mol
pivots: [5, 7], dihedral: [3, 5, 7, 1], rotor symmetry: 1, max scan energy: 10.27 kJ/mol
""",
)

entry(
    index = 8,
    label = "2BF + H_rad <=> PB6 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.35339e+09,'cm^3/(mol*s)'), n=1.75359, Ea=(91.8854,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
RXN 39
TS method summary for TS0 in 2BF + H_rad <=> PB6 + H2:
Methods that successfully generated a TS guess:
autotst,autotst,autotst,autotst,heuristics,
The method that generated the best TS guess and its output used for the optimization: heuristics


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
C      -0.12965400   -2.44615600   -3.37862400
C      -0.12536600   -2.44743400   -1.84743500
C      -0.12319500   -1.03817100   -1.24627000
C      -0.11783900   -1.04321500    0.29457800
C      -0.08564700    0.31778100    0.90115300
C      -0.97896100    1.03153300    1.64699800
C      -0.33853300    2.28076000    1.89468500
C       0.87560100    2.27270100    1.30813100
O       1.04790800    1.05784700    0.68536100
H       0.75093600   -1.93168600   -3.77531700
H      -0.12809600   -3.46382400   -3.77817100
H      -1.01475200   -1.93623300   -3.77127200
H       0.75255400   -2.99577000   -1.48485900
H      -1.00056800   -2.99726200   -1.48004900
H      -1.00138300   -0.48445600   -1.59794600
H       0.75363400   -0.48713300   -1.60242000
H       0.74902400   -1.61438400    0.64969000
H      -1.00767700   -1.55882300    0.66822100
H      -1.95348800    0.70370200    1.97074400
H      -0.92853700    3.51914200    2.73513000
H       1.69076100    2.96965800    1.22884400
H      -1.22270100    4.14635300    3.15919300

1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 11.88 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 23.55 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 19.09 kJ/mol
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 8.02 kJ/mol
""",
)

entry(
    index = 9,
    label = "2BF + OH_rad <=> PB6 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.94312,'cm^3/(mol*s)'), n=3.75576, Ea=(18.8657,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
RXN 40
TS method summary for TS0 in 2BF + OH_rad <=> PB6 + H2O:
Methods that successfully generated a TS guess:
autotst,autotst,autotst,autotst,heuristics,heuristics,heuristics,
The method that generated the best TS guess and its output used for the optimization: autotst


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
O       1.42961600   -1.06101700    0.67200200
O       4.29789900    2.50916900    0.54615100
C      -1.45790100   -1.23743000   -0.34520300
C      -2.08427200    0.14655700   -0.14669800
C      -0.15438700   -1.22654500   -1.17078600
C      -3.37583600    0.10385600    0.67471700
C       0.98327400   -0.52443200   -0.50989600
C       1.72541100    0.57350400   -0.83183900
C       2.69025100    0.69857500    0.21408400
C       2.47365800   -0.29024400    1.10981200
H      -2.28900000    0.59282000   -1.12787900
H      -1.36057900    0.80725400    0.34272700
H      -1.25463800   -1.69342500    0.62972900
H      -2.17693600   -1.89315600   -0.84971400
H       0.14297300   -2.26044500   -1.38143400
H      -0.32906300   -0.74664100   -2.13852600
H      -3.19507200   -0.30574900    1.67331500
H      -4.13276300   -0.52295100    0.19281400
H      -3.80236800    1.10287900    0.79825900
H       1.61359500    1.19215600   -1.70717700
H       3.66968600    1.57640000    0.28364200
H       2.93307900   -0.58362700    2.03703400
H       3.65336800    3.04248900    1.03486700

1D rotors:
* Invalidated! pivots: [3, 4], dihedral: [5, 3, 4, 6], invalidation reason: Another conformer for TS0 exists which is 3.00 kJ/mol lower.Another conformer for TS0 exists which is 3.00 kJ/mol lower.
pivots: [3, 5], dihedral: [4, 3, 5, 7], rotor symmetry: 1, max scan energy: 19.11 kJ/mol
pivots: [4, 6], dihedral: [3, 4, 6, 17], rotor symmetry: 3, max scan energy: 11.87 kJ/mol
pivots: [5, 7], dihedral: [3, 5, 7, 1], rotor symmetry: 1, max scan energy: 9.51 kJ/mol
""",
)

entry(
    index = 10,
    label = "2BF + H_rad <=> PB7 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.87238e+08,'cm^3/(mol*s)'), n=1.83311, Ea=(92.8854,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
RXN 42
TS method summary for TS0 in 2BF + H_rad <=> PB7 + H2:
Methods that successfully generated a TS guess:
autotst,autotst,autotst,autotst,heuristics,
The method that generated the best TS guess and its output used for the optimization: heuristics


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
C      -0.15734000   -2.43563900   -3.35823000
C      -0.16103200   -2.44013600   -1.82705800
C      -0.17039600   -1.03229800   -1.22272200
C      -0.17249900   -1.04042300    0.31795600
C      -0.15584400    0.31539300    0.93152700
C      -1.03568600    1.03483600    1.67931600
C      -0.42872400    2.31439800    1.95753300
C       0.77527400    2.24909500    1.34250100
O       0.98287900    1.07995800    0.72030500
H       0.72224900   -1.91513500   -3.74920100
H      -0.14772300   -3.45240900   -3.75995800
H      -1.04335000   -1.93004500   -3.75442700
H       0.71825900   -2.98402700   -1.46111200
H      -1.03481700   -2.99608400   -1.46543700
H      -1.04990700   -0.48265200   -1.57739500
H       0.70499600   -0.47541500   -1.57355400
H       0.69328500   -1.61135700    0.67608500
H      -1.06302600   -1.55961800    0.68634500
H      -2.00959500    0.70175500    2.00423000
H      -0.83510700    3.13529200    2.52385300
H       1.97829900    3.29687700    1.23519500
H       2.59789400    3.82087900    1.17379800

1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 11.88 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 23.56 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 19.14 kJ/mol
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 8.78 kJ/mol
""",
)

entry(
    index = 11,
    label = "2BF + OH_rad <=> PB7 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(14.406,'cm^3/(mol*s)'), n=3.77816, Ea=(24.5123,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
RXN 43
TS method summary for TS0 in 2BF + OH_rad <=> PB7 + H2O:
Methods that successfully generated a TS guess:
user guess 0,autotst,autotst,autotst,autotst,heuristics,heuristics,
The method that generated the best TS guess and its output used for the optimization: autotst


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
O       1.61211000   -0.32173700    0.52349300
O       4.13917500    1.63521300    1.21851300
C      -1.40446200   -0.76174800    0.76305100
C      -2.06067800    0.29967000   -0.12596500
C      -0.37759800   -1.64878000    0.02961100
C      -3.07549500    1.16360900    0.62788000
C       0.83375600   -0.92289700   -0.44328300
C       1.41420300   -0.73474400   -1.66384700
C       2.61002600    0.03053200   -1.45440800
C       2.69166400    0.18877200   -0.10575600
H      -2.55671100   -0.19490600   -0.97042100
H      -1.28597000    0.94012100   -0.56139100
H      -2.17879200   -1.41223300    1.18548000
H      -0.91032400   -0.27782600    1.61234400
H      -0.84279600   -2.12124000   -0.84131000
H      -0.06680800   -2.46120900    0.69724400
H      -3.88270000    0.55430600    1.04640300
H      -2.60089700    1.69718300    1.45713200
H      -3.52983500    1.90938400   -0.02982000
H       1.04105900   -1.10781700   -2.60511100
H       3.31564400    0.37841000   -2.19040500
H       3.60616900    0.79912300    0.66081400
H       3.50936000    2.36871300    1.16985200

1D rotors:
pivots: [3, 4], dihedral: [5, 3, 4, 6], rotor symmetry: 1, max scan energy: 26.74 kJ/mol
pivots: [3, 5], dihedral: [4, 3, 5, 7], rotor symmetry: 1, max scan energy: 19.28 kJ/mol
pivots: [4, 6], dihedral: [3, 4, 6, 17], rotor symmetry: 3, max scan energy: 11.87 kJ/mol
pivots: [5, 7], dihedral: [3, 5, 7, 1], rotor symmetry: 1, max scan energy: 9.67 kJ/mol
""",
)



