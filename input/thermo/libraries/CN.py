#!/usr/bin/env python
# encoding: utf-8

name = "CN"
shortDesc = u""
longDesc = u"""
Yaws' Critical Property Data for Chemical Engineers and Chemists
Table 30. Heat Capacity of Gas - Organic Compounds
Table 38. Enthalpy of Formation of Gas - Organic Compounds
Table 46. Entropy of Gas - Organic Compounds
"""
entry(
    index        = 1,
    label        = "C2N2",
    multiplicity = 1,
    molecule = 
"""
1 N U0 L1 E0  {2,T}
2 C U0 L0 E0  {1,T} {3,S}
3 C U0 L0 E0  {2,S} {4,T}
4 N U0 L1 E0  {3,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.629,14.857,15.65,16.297,17.431,18.25,19.914],'cal/(mol*K)'),
        H298 = (73.828,'kcal/mol'),
        S298 = (57.911,'cal/(mol*K)'),
    ),
    shortDesc = u"""cyanogen""",
    longDesc = 
u"""

""",
)

