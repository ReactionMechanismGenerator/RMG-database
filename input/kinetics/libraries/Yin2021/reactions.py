#!/usr/bin/env python
# encoding: utf-8

name = "Yin2021"
shortDesc = u""
longDesc = u"""

"""
entry(
    index=1,
    label="HOCHO <=> CO + H2O",
    degeneracy=1,
    kinetics=Arrhenius(A=(7.5E+14, 's^-1'), n=0.0, Ea=(68710, 'cal/mol'), T0=(1, 'K')),
),

entry(
    index=2,
    label="HOCHO <=> CO2 + H2",
    degeneracy=1,
    kinetics=Arrhenius(A=(1.42E-07, 's^-1'), n=5.33, Ea=(43479, 'cal/mol'), T0=(1, 'K')),
),

entry(
    index=3,
    label="HOCHO + OH <=> HOCO + H2O",
    degeneracy=1,
    kinetics=Arrhenius(A=(2.70E-01, 'cm^3/(mol*s)'), n=3.93, Ea=(12500, 'cal/mol'), T0=(1, 'K')),
),

entry(
    index=4,
    label="HOCHO + HO2 <=> OCHO + H2O2",
    degeneracy=1,
    kinetics=Arrhenius(A=(3.7E+01, 'cm^3/(mol*s)'), n=2.98, Ea=(25348, 'cal/mol'), T0=(1, 'K')),
),

entry(
    index=5,
    label="HOCHO + H <=> HOCO + H2",
    degeneracy=1,
    kinetics=Arrhenius(A=(4.3E+02, 'cm^3/(mol*s)'), n=3.272, Ea=(4858, 'cal/mol'), T0=(1, 'K')),
),

entry(
    index=6,
    label="HOCO + O2 <=> HOC(O)OO",
    degeneracy=1,
    kinetics=PDepArrhenius(
        pressures=([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius=[
            Arrhenius(A=(4.49E-09, 'cm^3/(mol*s)'), n=0.00, Ea=(-17910.0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.68E-06, 'cm^3/(mol*s)'), n=0.00, Ea=(-10760.0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.51E-11, 'cm^3/(mol*s)'), n=0.00, Ea=(-24300.0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.70E-12, 'cm^3/(mol*s)'), n=5.21, Ea=(4355.0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8.71E+00, 'cm^3/(mol*s)'), n=2.17, Ea=(-2871.0, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
),

entry(
    index=7,
    label="HOC(O)OO <=> CO2 + HO2",
    degeneracy=1,
    kinetics=PDepArrhenius(
        pressures=([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius=[
            Arrhenius(A=(8.16E+07, 's^-1'), n=0.00, Ea=(2680.0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.42E+08, 's^-1'), n=0.11, Ea=(3091.0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.35E+10, 's^-1'), n=-0.31, Ea=(4084.0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.04E+12, 's^-1'), n=-0.40, Ea=(4916.0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.22E+12, 's^-1'), n=-0.33, Ea=(5655.0, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
),

entry(
    index=8,
    label="HOCO + O2 <=> CO2 + HO2",
    degeneracy=1,
    kinetics=Arrhenius(A=(1.79E+16, 'cm^3/(mol*s)'), n=-1.23, Ea=(909.6, 'cal/mol'), T0=(1, 'K')),
),

entry(
    index=9,
    label="HOCO + HO2 <=> HOCOO + OH",
    degeneracy=1,
    kinetics=Arrhenius(A=(7.28E+12, 'cm^3/(mol*s)'), n=0.02, Ea=(118.6, 'cal/mol'), T0=(1, 'K')),
),

entry(
    index=10,
    label="HOCO + HO2 <=> H2O + CO3",
    degeneracy=1,
    kinetics=Arrhenius(A=(9.23E+08, 'cm^3/(mol*s)'), n=0.68, Ea=(-549.0, 'cal/mol'), T0=(1, 'K')),
),

entry(
    index=11,
    label="HOCO + HO2 <=> H2O2 + CO2",
    degeneracy=1,
    kinetics=Arrhenius(A=(3.31E+11, 'cm^3/(mol*s)'), n=0.16, Ea=(-196.5, 'cal/mol'), T0=(1, 'K')),
),

entry(
    index=12,
    label="HOCO + HO2 <=> HOC(O)OOH",
    degeneracy=1,
    kinetics=PDepArrhenius(
        pressures=([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius=[
            Arrhenius(A=(2.63E+96, 'cm^3/(mol*s)'), n=-27.42, Ea=(55100.0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.81E+15, 'cm^3/(mol*s)'), n=-3.25, Ea=(15410.0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.31E+18, 'cm^3/(mol*s)'), n=-3.72, Ea=(6721.0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.59E+28, 'cm^3/(mol*s)'), n=-5.94, Ea=(4270.0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.11E+32, 'cm^3/(mol*s)'), n=-6.34, Ea=(5754.0, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
),

entry(
    index=13,
    label="HOC(O)OOH <=> HOCOO + OH",
    degeneracy=1,
    kinetics=PDepArrhenius(
        pressures=([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius=[
            Arrhenius(A=(1.23E+46, 's^-1'), n=-10.57, Ea=(60710.0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.29E+48, 's^-1'), n=-10.80, Ea=(62760.0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.84E+46, 's^-1'), n=-9.84, Ea=(63380.0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.69E+40, 's^-1'), n=-7.79, Ea=(62080.0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.29E+32, 's^-1'), n=-5.22, Ea=(59410.0, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
),

entry(
    index=14,
    label="HOCHO + OH <=> HCO(OH)2",
    degeneracy=1,
    kinetics=PDepArrhenius(
        pressures=([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius=[
            Arrhenius(A=(3.46E+00, 'cm^3/(mol*s)'), n=0.00, Ea=(0.0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.19E+05, 'cm^3/(mol*s)'), n=0.00, Ea=(4474.0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.99E+04, 'cm^3/(mol*s)'), n=0.56, Ea=(1352.0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8.04E+10, 'cm^3/(mol*s)'), n=-1.11, Ea=(564.0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.78E+17, 'cm^3/(mol*s)'), n=-2.50, Ea=(1980.0, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
),

# entry(
#     index=15,
#     label="HOCHO + OH <=> HCO(OH)2", ########### Yin is not balanced ##########
#     degeneracy=1,
#     kinetics=Arrhenius(A=(7.46E+07, 'cm^3/(mol*s)'), n=1.36, Ea=(1421.0, 'cal/mol'), T0=(1, 'K')),
# ),

entry(
    index=16,
    label="HCO(OH)2 <=> H + CO(OH)2",
    degeneracy=1,
    kinetics=PDepArrhenius(
        pressures=([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius=[
            Arrhenius(A=(2.73E+06, 's^-1'), n=0.00, Ea=(0.0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.38E+08, 's^-1'), n=0.00, Ea=(3300.0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.27E+11, 's^-1'), n=-0.65, Ea=(4610.0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.11E+14, 's^-1'), n=-1.17, Ea=(6039.0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.77E+15, 's^-1'), n=-1.22, Ea=(7245.0, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)