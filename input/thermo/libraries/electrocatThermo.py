#!/usr/bin/env python
# encoding: utf-8

name = "electrocatThermo"
shortDesc = u"Surface adsorbates on Pt(111)"
longDesc = u"""
Some surface species adsorbed on Pt(111),
Mostly calculated by Katrin Blondal at Brown University around 2018,
based on DFT calculations by Jelena Jelic at KIT.
Note: "-h" means "horizontal".
"""


entry(
    index = 1,
    label = "vacant",
    molecule =
"""
1 X  u0 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             0.000000000E+00,   0.000000000E+00,   0.000000000E+00,   0.000000000E+00,
             0.000000000E+00,   0.000000000E+00,   0.000000000E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             0.000000000E+00,   0.000000000E+00,   0.000000000E+00,   0.000000000E+00,
             0.000000000E+00,   0.000000000E+00,   0.000000000E+00], Tmin=(1000.0,'K'), Tmax=(3000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (3000.0, 'K'),
    ),
    metal = "Pt",
    facet = "111",
)

entry(
    index = 2,
    label = "electron",
    molecule =
"""
1 e u0 p0 c-1
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             0.000000000E+00,   0.000000000E+00,   0.000000000E+00,   0.000000000E+00,
             0.000000000E+00,   0.000000000E+00,   0.000000000E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             0.000000000E+00,   0.000000000E+00,   0.000000000E+00,   0.000000000E+00,
             0.000000000E+00,   0.000000000E+00,   0.000000000E+00], Tmin=(1000.0,'K'), Tmax=(3000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (3000.0, 'K'),
    ),
)

entry(
    index = 3,
    label = "proton",
    molecule =
"""
1 H u0 p0 c+1
""",
    thermo = ThermoData(
        Tdata=([300,400,500,600,800,1000,1500],'K'), 
        Cpdata=([3.4475,3.4875,3.497,3.5045,3.5405,3.6095,3.86],'cal/(mol*K)'), 
        H298=(0,'kcal/mol'), S298=(15.6165,'cal/(mol*K)','+|-',0.0007),
        comment = '1/2 free energy of H2(g)')
)

entry(
    index = 4,
    label = "H3O",
    molecule =
"""
1 H u0 p0 c0 {3,S}
2 H u0 p0 c0 {3,S}
3 O u0 p2 c0 {1,S} {2,S}
4 H u0 p0 c+1
""",
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), 
        Cpdata=([11.4855,11.6675,11.876,12.1285,12.7355,13.3755,14.879],'cal/(mol*K)'), 
        H298=(-57.797,'kcal/mol'), S298=(60.7005,'cal/(mol*K)','+|-',0.0007), 
        comment="""1/2 free energy of H2(g) + H2O(g)""")
)

entry(
    index = 5,
    label = "H2O",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.038,8.18,8.379,8.624,9.195,9.766,11.019],'cal/(mol*K)'),
        H298 = (-57.797,'kcal/mol'),
        S298 = (45.084,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
H298: ATcT version 1.110
level of theory energy: CCSD(T)F12A/cc-pVQZ-F12//CCSD(T)/cc-pVQZ
level of theory frequency: B3LYP/6-311++g(d,p)//B3LYP/6-311++g(d,p)
""",
)


# entry(
#     index = 4,
#     label = "CO2X",
#     molecule = 
# """
# 1 C u0 p0 {2,D} {3,D}
# 2 O u0 p2 {1,D}
# 3 O u0 p2 {1,D}
# 4 X u0 p0
# """,
#     thermo = ThermoData(
#         Tdata = ([300,400,500,600,800,1000,1500],'K'),
#         Cpdata = ([8.869,9.845,10.626,11.264,12.229,12.898,13.822],'cal/(mol*K)'),
#         H298 = (-98,'kcal/mol'),
#         S298 = (28.54,'cal/(mol*K)'),
#     ),
#     shortDesc = u"""""",
#     longDesc = 
# u"""

# """,
#     metal = "Pt",
#     facet = "111",
# )

# entry(
#     index = 6,
#     label = "O=CX-CX=O",
#     molecule = 
# """
# 1 C u0 p0 c0 {2,S} {3,D} {5,S}
# 2 C u0 p0 c0 {1,S} {4,D} {6,S}
# 3 O u0 p2 c0 {1,D}
# 4 O u0 p2 c0 {2,D}
# 5 X u0 p0 c0 {1,S}
# 6 X u0 p0 c0 {2,S}
# """,
#     thermo = ThermoData(
#         Tdata = ([300,400,500,600,800,1000,1500],'K'),
#         Cpdata = ([15.24,17.52,19.03,20.13,21.6,22.53,23.69],'cal/(mol*K)'),
#         H298 = (-17.02,'kcal/mol'),
#         S298 = (49.17,'cal/(mol*K)'),
#     ),
#     shortDesc = u"""""",
#     longDesc = 
# u"""
# OCCO from primary thermo library + Thermo group additivity estimation: adsorptionPt111(C-*R2C-*R2)

# instead of OCCO(S)
# """,
#     metal = "Pt",
#     facet = "111",
# )



