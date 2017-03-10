#!/usr/bin/env python
# encoding: utf-8

name = "Polycyclic Ring Corrections"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 0,
    label = "PolycyclicRing",
    group = 
"""
1 * R u0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Properties of Liquids and Gases, Poling 5th Ed.
""",
)

entry(
    index = 0,
    label = "s1_3_3",
    group = 
"""
1   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2 * R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {1,[S,D,T,B]} {5,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1,
    label = "s1_3_3_ane",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S} {5,S}
2 * R!H u0 {1,S} {3,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {5,S}
5   R!H u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-22.0868,-24.4911,-25.6002,-25.9787,-24.2912,-21.2391,-15.3261],'J/(mol*K)'),
        H298 = (251.424,'kJ/mol'),
        S298 = (270.513,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_3_3_ane from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 2,
    label = "s1_3_3_ene",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S} {5,S}
2 * R!H u0 {1,S} {3,D}
3   R!H u0 {1,S} {2,D}
4   R!H u0 {1,S} {5,S}
5   R!H u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-12.9943,-15.581,-17.9972,-19.8676,-20.5392,-19.2294,-15.2695],'J/(mol*K)'),
        H298 = (362.37,'kJ/mol'),
        S298 = (282.734,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_3_3_ene from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s1_3_4",
    group = 
"""
1 * R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
6   R!H u0 {4,[S,D,T,B]} {5,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "s1_3_4_ane",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {4,S} {5,S}
2   R!H u0 {1,S} {3,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {6,S}
5   R!H u0 {1,S} {6,S}
6   R!H u0 {4,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-27.6421,-29.3789,-29.5092,-28.6401,-24.6481,-20.0126,-12.3621],'J/(mol*K)'),
        H298 = (233.734,'kJ/mol'),
        S298 = (265.753,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_3_4_ane from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 4,
    label = "s1_3_4_ene",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {4,S} {5,S}
2   R!H u0 {1,S} {3,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {6,D}
5   R!H u0 {1,S} {6,S}
6   R!H u0 {4,D} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-20.2706,-23.1082,-24.2741,-24.6598,-22.8417,-19.6877,-13.4427],'J/(mol*K)'),
        H298 = (251.097,'kJ/mol'),
        S298 = (265.64,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_3_4_ene from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s1_3_5",
    group = 
"""
1   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6 * R!H u0 {4,[S,D,T,B]} {7,[S,D,T,B]}
7   R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "s1_3_5_ane",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S} {5,S}
2   R!H u0 {1,S} {3,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {6,S}
5   R!H u0 {1,S} {7,S}
6 * R!H u0 {4,S} {7,S}
7   R!H u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-34.6141,-35.1657,-34.1402,-32.0945,-25.894,-19.7012,-10.1761],'J/(mol*K)'),
        H298 = (155.625,'kJ/mol'),
        S298 = (243.924,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_3_5_ane from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s1_3_5_ene",
    group = "OR{s1_3_5_ene_1, s1_3_5_ene_2}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "s1_3_5_ene_1",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S} {5,S}
2   R!H u0 {1,S} {3,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {7,S}
5   R!H u0 {1,S} {6,D}
6 * R!H u0 {5,D} {7,S}
7   R!H u0 {4,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-26.3541,-28.352,-28.5221,-27.7502,-23.7846,-19.1362,-11.1587],'J/(mol*K)'),
        H298 = (144.568,'kJ/mol'),
        S298 = (248.507,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_3_5_ene_1 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 7,
    label = "s1_3_5_ene_2",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S} {5,S}
2   R!H u0 {1,S} {3,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {7,S}
5   R!H u0 {1,S} {6,S}
6 * R!H u0 {5,S} {7,D}
7   R!H u0 {4,S} {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-26.3511,-28.35,-28.5211,-27.7492,-23.7836,-18.8842,-11.1587],'J/(mol*K)'),
        H298 = (148.792,'kJ/mol'),
        S298 = (248.513,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_3_5_ene_2 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s1_3_5_diene",
    group = "OR{s1_3_5_diene_1_3}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "s1_3_5_diene_1_3",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S} {5,S}
2   R!H u0 {1,S} {3,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {7,D}
5   R!H u0 {1,S} {6,D}
6 * R!H u0 {5,D} {7,S}
7   R!H u0 {4,D} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-27.6823,-30.4947,-30.7122,-29.9232,-26.144,-21.5337,-14.1921],'J/(mol*K)'),
        H298 = (138.847,'kJ/mol'),
        S298 = (257.869,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_3_5_diene_1_3 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s1_3_6",
    group = 
"""
1   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   R!H u0 {4,[S,D,T,B]} {8,[S,D,T,B]}
7   R!H u0 {5,[S,D,T,B]} {8,[S,D,T,B]}
8 * R!H u0 {6,[S,D,T,B]} {7,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "s1_3_6_ane",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S} {5,S}
2   R!H u0 {1,S} {3,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {6,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {4,S} {8,S}
7   R!H u0 {5,S} {8,S}
8 * R!H u0 {6,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-39.6941,-38.8855,-37.0422,-34.2189,-26.3128,-18.8698,-7.70508],'J/(mol*K)'),
        H298 = (125.887,'kJ/mol'),
        S298 = (217.99,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_3_6_ane from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s1_3_6_ene",
    group = "OR{s1_3_6_ene_1, s1_3_6_ene_2}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "s1_3_6_ene_1",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S} {5,S}
2   R!H u0 {1,S} {3,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {6,S}
5   R!H u0 {1,S} {7,D}
6   R!H u0 {4,S} {8,S}
7   R!H u0 {5,D} {8,S}
8 * R!H u0 {6,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-31.4951,-32.3948,-31.8831,-30.3166,-24.5445,-18.5698,-8.84772],'J/(mol*K)'),
        H298 = (120.489,'kJ/mol'),
        S298 = (224.341,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_3_6_ene_1 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 11,
    label = "s1_3_6_ene_2",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S} {5,S}
2   R!H u0 {1,S} {3,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {6,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {4,S} {8,D}
7   R!H u0 {5,S} {8,S}
8 * R!H u0 {6,D} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-31.4971,-32.3948,-31.8811,-30.3146,-24.5415,-18.3168,-8.84572],'J/(mol*K)'),
        H298 = (124.709,'kJ/mol'),
        S298 = (224.329,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_3_6_ene_2 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s1_3_6_diene",
    group = "OR{s1_3_6_diene_1_4, s1_3_6_diene_1_3}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "s1_3_6_diene_1_4",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S} {5,S}
2   R!H u0 {1,S} {3,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {7,D}
5   R!H u0 {1,S} {6,D}
6   R!H u0 {5,D} {8,S}
7   R!H u0 {4,D} {8,S}
8 * R!H u0 {6,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-25.2737,-26.7232,-26.6259,-25.813,-21.9426,-17.4094,-9.23724],'J/(mol*K)'),
        H298 = (111.585,'kJ/mol'),
        S298 = (224.703,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_3_6_diene_1_4 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 13,
    label = "s1_3_6_diene_1_3",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S} {5,S}
2   R!H u0 {1,S} {3,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {7,S}
5   R!H u0 {1,S} {6,D}
6   R!H u0 {5,D} {8,S}
7   R!H u0 {4,S} {8,D}
8 * R!H u0 {6,S} {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-29.2644,-32.873,-33.5991,-32.5024,-27.0025,-21.061,-11.9334],'J/(mol*K)'),
        H298 = (134.387,'kJ/mol'),
        S298 = (244.923,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_3_6_diene_1_3 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s1_4_4",
    group = 
"""
1   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2 * R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
4   R!H u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
6   R!H u0 {4,[S,D,T,B]} {5,[S,D,T,B]}
7   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "s1_4_4_ane",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S} {5,S}
2 * R!H u0 {1,S} {7,S}
3   R!H u0 {1,S} {7,S}
4   R!H u0 {1,S} {6,S}
5   R!H u0 {1,S} {6,S}
6   R!H u0 {4,S} {5,S}
7   R!H u0 {2,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-34.4141,-34.9857,-33.9212,-31.7785,-25.403,-19.1222,-9.61308],'J/(mol*K)'),
        H298 = (232.497,'kJ/mol'),
        S298 = (237.342,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_4_4_ane from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s1_4_4_ene",
    group = "OR{s1_4_4_ene_1}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "s1_4_4_ene_1",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S} {5,S}
2 * R!H u0 {1,S} {7,S}
3   R!H u0 {1,S} {6,S}
4   R!H u0 {1,S} {7,D}
5   R!H u0 {1,S} {6,S}
6   R!H u0 {3,S} {5,S}
7   R!H u0 {2,S} {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-26.1201,-28.208,-28.3591,-27.4622,-23.2576,-18.4732,-10.4567],'J/(mol*K)'),
        H298 = (249.653,'kJ/mol'),
        S298 = (247.253,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_4_4_ene_1 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s1_4_4_diene",
    group = "OR{s1_4_4_diene_1_5}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "s1_4_4_diene_1_5",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S} {5,S}
2 * R!H u0 {1,S} {7,D}
3   R!H u0 {1,S} {6,S}
4   R!H u0 {1,S} {7,S}
5   R!H u0 {1,S} {6,D}
6   R!H u0 {3,S} {5,D}
7   R!H u0 {2,D} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-19.5711,-22.1439,-22.977,-23.0552,-20.8926,-17.3085,-10.9841],'J/(mol*K)'),
        H298 = (272.769,'kJ/mol'),
        S298 = (247.04,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_4_4_diene_1_5 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s1_4_5",
    group = 
"""
1   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2 * R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
4   R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
6   R!H u0 {3,[S,D,T,B]} {5,[S,D,T,B]}
7   R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
8   R!H u0 {4,[S,D,T,B]} {7,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "s1_4_5_ane",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S} {5,S}
2 * R!H u0 {1,S} {7,S}
3   R!H u0 {1,S} {6,S}
4   R!H u0 {1,S} {8,S}
5   R!H u0 {1,S} {6,S}
6   R!H u0 {3,S} {5,S}
7   R!H u0 {2,S} {8,S}
8   R!H u0 {4,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-38.8501,-39.2525,-38.0342,-34.9049,-26.3428,-18.5328,-7.24008],'J/(mol*K)'),
        H298 = (158.252,'kJ/mol'),
        S298 = (228.958,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_4_5_ane from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s1_4_5_ene",
    group = "OR{s1_4_5_ene_1, s1_4_5_ene_2, s1_4_5_ene_6}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "s1_4_5_ene_1",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S} {5,S}
2 * R!H u0 {1,S} {7,S}
3   R!H u0 {1,S} {6,S}
4   R!H u0 {1,S} {8,D}
5   R!H u0 {1,S} {6,S}
6   R!H u0 {3,S} {5,S}
7   R!H u0 {2,S} {8,S}
8   R!H u0 {4,D} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-32.3121,-33.3038,-32.4721,-30.4876,-24.1735,-17.9258,-8.20272],'J/(mol*K)'),
        H298 = (149.993,'kJ/mol'),
        S298 = (226.194,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_4_5_ene_1 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 19,
    label = "s1_4_5_ene_2",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S} {5,S}
2 * R!H u0 {1,S} {8,S}
3   R!H u0 {1,S} {7,S}
4   R!H u0 {1,S} {6,S}
5   R!H u0 {1,S} {6,S}
6   R!H u0 {4,S} {5,S}
7   R!H u0 {3,S} {8,D}
8   R!H u0 {2,S} {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-33.0771,-33.7548,-32.6151,-30.5196,-24.1875,-17.6688,-8.15672],'J/(mol*K)'),
        H298 = (155.471,'kJ/mol'),
        S298 = (224.108,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_4_5_ene_2 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 20,
    label = "s1_4_5_ene_6",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S} {5,S}
2 * R!H u0 {1,S} {8,S}
3   R!H u0 {1,S} {6,D}
4   R!H u0 {1,S} {6,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {3,D} {4,S}
7   R!H u0 {5,S} {8,S}
8   R!H u0 {2,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-30.7491,-32.9668,-33.0891,-31.0506,-24.4285,-18.0408,-8.29972],'J/(mol*K)'),
        H298 = (177.587,'kJ/mol'),
        S298 = (233.799,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_4_5_ene_6 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s1_4_5_diene",
    group = "OR{s1_4_5_diene_1_3, s1_4_5_diene_1_6, s1_4_5_diene_2_6}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "s1_4_5_diene_1_3",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S} {5,S}
2   R!H u0 {1,S} {6,S}
3 * R!H u0 {1,S} {7,D}
4   R!H u0 {1,S} {8,D}
5   R!H u0 {1,S} {6,S}
6   R!H u0 {2,S} {5,S}
7   R!H u0 {3,D} {8,S}
8   R!H u0 {4,D} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-32.4653,-34.6175,-34.0002,-32.0846,-26.0869,-19.9662,-11.0011],'J/(mol*K)'),
        H298 = (159.233,'kJ/mol'),
        S298 = (245.609,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_4_5_diene_1_3 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 22,
    label = "s1_4_5_diene_1_6",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S} {5,S}
2   R!H u0 {1,S} {6,D}
3 * R!H u0 {1,S} {7,S}
4   R!H u0 {1,S} {8,D}
5   R!H u0 {1,S} {6,S}
6   R!H u0 {2,D} {5,S}
7   R!H u0 {3,S} {8,S}
8   R!H u0 {4,D} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-25.7311,-27.2637,-27.115,-26.0826,-21.8165,-16.779,-8.78112],'J/(mol*K)'),
        H298 = (172.771,'kJ/mol'),
        S298 = (232.662,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_4_5_diene_1_6 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 23,
    label = "s1_4_5_diene_2_6",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S} {5,S}
2 * R!H u0 {1,S} {8,S}
3   R!H u0 {1,S} {6,D}
4   R!H u0 {1,S} {7,S}
5   R!H u0 {1,S} {6,S}
6   R!H u0 {3,D} {5,S}
7   R!H u0 {4,S} {8,D}
8   R!H u0 {2,S} {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-24.5532,-26.8942,-27.1269,-26.3423,-22.1881,-17.1588,-9.09736],'J/(mol*K)'),
        H298 = (174.143,'kJ/mol'),
        S298 = (228.266,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_4_5_diene_2_6 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s1_4_6",
    group = 
"""
1   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
4   R!H u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   R!H u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
7 * R!H u0 {5,[S,D,T,B]} {9,[S,D,T,B]}
8   R!H u0 {3,[S,D,T,B]} {9,[S,D,T,B]}
9   R!H u0 {7,[S,D,T,B]} {8,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "s1_4_6_ane",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S} {5,S}
2   R!H u0 {1,S} {6,S}
3   R!H u0 {1,S} {8,S}
4   R!H u0 {1,S} {6,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {2,S} {4,S}
7 * R!H u0 {5,S} {9,S}
8   R!H u0 {3,S} {9,S}
9   R!H u0 {7,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-44.3881,-43.1843,-40.8282,-36.6503,-26.2877,-17.2703,-4.60108],'J/(mol*K)'),
        H298 = (131.017,'kJ/mol'),
        S298 = (198.451,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_4_6_ane from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s1_4_6_ene",
    group = "OR{s1_4_6_ene_1, s1_4_6_ene_2, s1_4_6_ene_7}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "s1_4_6_ene_1",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S} {5,S}
2   R!H u0 {1,S} {6,S}
3   R!H u0 {1,S} {8,D}
4   R!H u0 {1,S} {6,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {2,S} {4,S}
7 * R!H u0 {5,S} {9,S}
8   R!H u0 {3,D} {9,S}
9   R!H u0 {7,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-36.3381,-36.6606,-35.5501,-32.746,-24.6404,-17.1154,-5.79572],'J/(mol*K)'),
        H298 = (129.446,'kJ/mol'),
        S298 = (204.194,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_4_6_ene_1 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 26,
    label = "s1_4_6_ene_2",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S} {5,S}
2   R!H u0 {1,S} {7,S}
3   R!H u0 {1,S} {6,S}
4   R!H u0 {1,S} {6,S}
5   R!H u0 {1,S} {8,S}
6   R!H u0 {3,S} {4,S}
7 * R!H u0 {2,S} {9,S}
8   R!H u0 {5,S} {9,D}
9   R!H u0 {7,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-36.4171,-36.7376,-35.6121,-32.799,-24.6814,-16.8973,-5.81872],'J/(mol*K)'),
        H298 = (133.632,'kJ/mol'),
        S298 = (204.379,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_4_6_ene_2 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 27,
    label = "s1_4_6_ene_7",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S} {5,S}
2   R!H u0 {1,S} {6,D}
3   R!H u0 {1,S} {8,S}
4   R!H u0 {1,S} {7,S}
5   R!H u0 {1,S} {6,S}
6   R!H u0 {2,D} {5,S}
7 * R!H u0 {4,S} {9,S}
8   R!H u0 {3,S} {9,S}
9   R!H u0 {7,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-36.9731,-37.1476,-35.8791,-33.054,-24.9074,-17.3164,-5.82472],'J/(mol*K)'),
        H298 = (150.365,'kJ/mol'),
        S298 = (201.589,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_4_6_ene_7 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s1_4_6_diene",
    group = "OR{s1_4_6_diene_1_3, s1_4_6_diene_1_4, s1_4_6_diene_1_7, s1_4_6_diene_2_7}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "s1_4_6_diene_1_3",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S} {5,S}
2   R!H u0 {1,S} {8,S}
3   R!H u0 {1,S} {6,S}
4   R!H u0 {1,S} {7,D}
5   R!H u0 {1,S} {6,S}
6   R!H u0 {3,S} {5,S}
7 * R!H u0 {4,D} {9,S}
8   R!H u0 {2,S} {9,D}
9   R!H u0 {7,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-34.3964,-38.5478,-38.7261,-35.7498,-27.2334,-19.7056,-9.56136],'J/(mol*K)'),
        H298 = (144.043,'kJ/mol'),
        S298 = (223.141,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_4_6_diene_1_3 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 29,
    label = "s1_4_6_diene_1_4",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S} {5,S}
2   R!H u0 {1,S} {8,D}
3   R!H u0 {1,S} {6,S}
4   R!H u0 {1,S} {6,S}
5   R!H u0 {1,S} {7,D}
6   R!H u0 {3,S} {4,S}
7 * R!H u0 {5,D} {9,S}
8   R!H u0 {2,D} {9,S}
9   R!H u0 {7,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-29.6317,-31.556,-31.0009,-28.4484,-21.7675,-15.7389,-6.57024],'J/(mol*K)'),
        H298 = (125.442,'kJ/mol'),
        S298 = (213.238,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_4_6_diene_1_4 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 30,
    label = "s1_4_6_diene_1_7",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S} {5,S}
2   R!H u0 {1,S} {6,D}
3   R!H u0 {1,S} {6,S}
4   R!H u0 {1,S} {8,D}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {2,D} {3,S}
7 * R!H u0 {5,S} {9,S}
8   R!H u0 {4,D} {9,S}
9   R!H u0 {7,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-30.0071,-31.6435,-31.139,-28.718,-22.1294,-15.8216,-6.75412],'J/(mol*K)'),
        H298 = (152.104,'kJ/mol'),
        S298 = (209.901,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_4_6_diene_1_7 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 31,
    label = "s1_4_6_diene_2_7",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S} {5,S}
2   R!H u0 {1,S} {6,D}
3   R!H u0 {1,S} {8,S}
4   R!H u0 {1,S} {6,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {2,D} {4,S}
7 * R!H u0 {5,S} {9,D}
8   R!H u0 {3,S} {9,S}
9   R!H u0 {7,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-28.6922,-31.496,-31.5769,-29.3817,-22.756,-16.3784,-7.21036],'J/(mol*K)'),
        H298 = (150.509,'kJ/mol'),
        S298 = (206.455,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_4_6_diene_2_7 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s1_5_5",
    group = 
"""
1   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2 * R!H u0 {1,[S,D,T,B]} {9,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
4   R!H u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
6   R!H u0 {4,[S,D,T,B]} {7,[S,D,T,B]}
7   R!H u0 {3,[S,D,T,B]} {6,[S,D,T,B]}
8   R!H u0 {5,[S,D,T,B]} {9,[S,D,T,B]}
9   R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "s1_5_5_ane",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S} {5,S}
2 * R!H u0 {1,S} {9,S}
3   R!H u0 {1,S} {7,S}
4   R!H u0 {1,S} {6,S}
5   R!H u0 {1,S} {8,S}
6   R!H u0 {4,S} {7,S}
7   R!H u0 {3,S} {6,S}
8   R!H u0 {5,S} {9,S}
9   R!H u0 {2,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-45.1931,-44.3703,-42.0522,-37.8283,-27.2707,-17.9943,-4.82308],'J/(mol*K)'),
        H298 = (87.6682,'kJ/mol'),
        S298 = (203.343,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_5_5_ane from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s1_5_5_ene",
    group = "OR{s1_5_5_ene_1, s1_5_5_ene_2}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "s1_5_5_ene_1",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S} {5,S}
2 * R!H u0 {1,S} {9,S}
3   R!H u0 {1,S} {6,D}
4   R!H u0 {1,S} {8,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {3,D} {8,S}
7   R!H u0 {5,S} {9,S}
8   R!H u0 {4,S} {6,S}
9   R!H u0 {2,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-38.1021,-38.3606,-36.8641,-33.736,-25.1844,-17.4014,-5.93172],'J/(mol*K)'),
        H298 = (79.864,'kJ/mol'),
        S298 = (216.968,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_5_5_ene_1 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 34,
    label = "s1_5_5_ene_2",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S} {5,S}
2 * R!H u0 {1,S} {7,S}
3   R!H u0 {1,S} {6,S}
4   R!H u0 {1,S} {9,S}
5   R!H u0 {1,S} {8,S}
6   R!H u0 {3,S} {9,D}
7   R!H u0 {2,S} {8,S}
8   R!H u0 {5,S} {7,S}
9   R!H u0 {4,S} {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-37.8711,-38.2586,-36.8731,-33.721,-25.1134,-17.0473,-5.80572],'J/(mol*K)'),
        H298 = (82.2446,'kJ/mol'),
        S298 = (206.076,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_5_5_ene_2 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s1_5_5_diene",
    group = "OR{s1_5_5_diene_1_3, s1_5_5_diene_1_6, s1_5_5_diene_1_7, s1_5_5_diene_2_7}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "s1_5_5_diene_1_3",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S} {5,S}
2 * R!H u0 {1,S} {7,D}
3   R!H u0 {1,S} {8,D}
4   R!H u0 {1,S} {9,S}
5   R!H u0 {1,S} {6,S}
6   R!H u0 {5,S} {9,S}
7   R!H u0 {2,D} {8,S}
8   R!H u0 {3,D} {7,S}
9   R!H u0 {4,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-37.7383,-39.5883,-38.5872,-35.656,-27.3708,-19.6608,-8.84312],'J/(mol*K)'),
        H298 = (86.8912,'kJ/mol'),
        S298 = (227.719,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_5_5_diene_1_3 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 36,
    label = "s1_5_5_diene_1_6",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S} {5,S}
2 * R!H u0 {1,S} {6,S}
3   R!H u0 {1,S} {8,S}
4   R!H u0 {1,S} {9,D}
5   R!H u0 {1,S} {7,D}
6   R!H u0 {2,S} {7,S}
7   R!H u0 {5,D} {6,S}
8   R!H u0 {3,S} {9,S}
9   R!H u0 {4,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-31.5551,-32.0635,-31.03,-28.893,-22.5374,-16.0736,-6.47112],'J/(mol*K)'),
        H298 = (77.6426,'kJ/mol'),
        S298 = (212.966,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_5_5_diene_1_6 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 37,
    label = "s1_5_5_diene_1_7",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S} {5,S}
2 * R!H u0 {1,S} {7,D}
3   R!H u0 {1,S} {6,S}
4   R!H u0 {1,S} {9,S}
5   R!H u0 {1,S} {8,S}
6   R!H u0 {3,S} {9,D}
7   R!H u0 {2,D} {8,S}
8   R!H u0 {5,S} {7,S}
9   R!H u0 {4,S} {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-30.8112,-32.131,-31.3959,-29.4797,-23.177,-16.6584,-6.86736],'J/(mol*K)'),
        H298 = (76.7183,'kJ/mol'),
        S298 = (207.406,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_5_5_diene_1_7 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 38,
    label = "s1_5_5_diene_2_7",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S} {5,S}
2 * R!H u0 {1,S} {9,S}
3   R!H u0 {1,S} {8,S}
4   R!H u0 {1,S} {7,S}
5   R!H u0 {1,S} {6,S}
6   R!H u0 {5,S} {8,D}
7   R!H u0 {4,S} {9,D}
8   R!H u0 {3,S} {6,D}
9   R!H u0 {2,S} {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-18.2662,-21.791,-24.7349,-25.4707,-23.14,-19.1903,-12.9414],'J/(mol*K)'),
        H298 = (797.365,'kJ/mol'),
        S298 = (219.58,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_5_5_diene_2_7 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s1_5_6",
    group = 
"""
1    R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2    R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
3    R!H u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
4    R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
5    R!H u0 {1,[S,D,T,B]} {9,[S,D,T,B]}
6  * R!H u0 {3,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H u0 {2,[S,D,T,B]} {6,[S,D,T,B]}
8    R!H u0 {4,[S,D,T,B]} {10,[S,D,T,B]}
9    R!H u0 {5,[S,D,T,B]} {10,[S,D,T,B]}
10   R!H u0 {8,[S,D,T,B]} {9,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "s1_5_6_ane",
    group = 
"""
1    R!H u0 {2,S} {3,S} {4,S} {5,S}
2    R!H u0 {1,S} {7,S}
3    R!H u0 {1,S} {6,S}
4    R!H u0 {1,S} {8,S}
5    R!H u0 {1,S} {9,S}
6  * R!H u0 {3,S} {7,S}
7    R!H u0 {2,S} {6,S}
8    R!H u0 {4,S} {10,S}
9    R!H u0 {5,S} {10,S}
10   R!H u0 {8,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-51.2701,-48.9971,-45.5842,-40.3227,-27.9276,-17.3569,-2.56608],'J/(mol*K)'),
        H298 = (66.0771,'kJ/mol'),
        S298 = (177.423,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_5_6_ane from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s1_5_6_ene",
    group = "OR{s1_5_6_ene_1, s1_5_6_ene_2, s1_5_6_ene_7, s1_5_6_ene_8}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "s1_5_6_ene_1",
    group = 
"""
1    R!H u0 {2,S} {3,S} {4,S} {5,S}
2    R!H u0 {1,S} {6,S}
3    R!H u0 {1,S} {7,D}
4    R!H u0 {1,S} {8,S}
5    R!H u0 {1,S} {9,S}
6  * R!H u0 {2,S} {9,S}
7    R!H u0 {3,D} {10,S}
8    R!H u0 {4,S} {10,S}
9    R!H u0 {5,S} {6,S}
10   R!H u0 {7,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-42.0821,-41.9694,-39.8751,-35.7244,-25.4762,-16.6259,-3.82272],'J/(mol*K)'),
        H298 = (62.2061,'kJ/mol'),
        S298 = (190.267,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_5_6_ene_1 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 41,
    label = "s1_5_6_ene_2",
    group = 
"""
1    R!H u0 {2,S} {3,S} {4,S} {5,S}
2    R!H u0 {1,S} {6,S}
3    R!H u0 {1,S} {8,S}
4    R!H u0 {1,S} {7,S}
5    R!H u0 {1,S} {9,S}
6    R!H u0 {2,S} {10,S}
7  * R!H u0 {4,S} {9,S}
8    R!H u0 {3,S} {10,D}
9    R!H u0 {5,S} {7,S}
10   R!H u0 {6,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-42.4521,-42.3884,-40.2891,-36.1204,-25.8232,-16.6619,-3.97672],'J/(mol*K)'),
        H298 = (63.2789,'kJ/mol'),
        S298 = (181.962,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_5_6_ene_2 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 42,
    label = "s1_5_6_ene_7",
    group = 
"""
1    R!H u0 {2,S} {3,S} {4,S} {5,S}
2    R!H u0 {1,S} {7,S}
3    R!H u0 {1,S} {8,D}
4    R!H u0 {1,S} {6,S}
5    R!H u0 {1,S} {9,S}
6    R!H u0 {4,S} {10,S}
7    R!H u0 {2,S} {10,S}
8  * R!H u0 {3,D} {9,S}
9    R!H u0 {5,S} {8,S}
10   R!H u0 {6,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-42.5471,-42.0614,-40.0281,-35.9024,-25.5642,-16.5469,-3.57872],'J/(mol*K)'),
        H298 = (56.3477,'kJ/mol'),
        S298 = (180.355,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_5_6_ene_7 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 43,
    label = "s1_5_6_ene_8",
    group = 
"""
1    R!H u0 {2,S} {3,S} {4,S} {5,S}
2    R!H u0 {1,S} {7,S}
3    R!H u0 {1,S} {6,S}
4    R!H u0 {1,S} {9,S}
5    R!H u0 {1,S} {8,S}
6  * R!H u0 {3,S} {8,D}
7    R!H u0 {2,S} {10,S}
8    R!H u0 {5,S} {6,D}
9    R!H u0 {4,S} {10,S}
10   R!H u0 {7,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-42.5531,-42.0654,-40.0311,-35.9034,-25.5642,-16.2959,-3.57872],'J/(mol*K)'),
        H298 = (60.5733,'kJ/mol'),
        S298 = (180.335,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_5_6_ene_8 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s1_5_6_diene",
    group = "OR{s1_5_6_diene_1_3, s1_5_6_diene_1_4, s1_5_6_diene_1_7, s1_5_6_diene_1_8, s1_5_6_diene_2_7, s1_5_6_diene_2_8, s1_5_6_diene_7_9}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "s1_5_6_diene_1_3",
    group = 
"""
1    R!H u0 {2,S} {3,S} {4,S} {5,S}
2    R!H u0 {1,S} {9,S}
3    R!H u0 {1,S} {8,S}
4    R!H u0 {1,S} {6,D}
5    R!H u0 {1,S} {7,S}
6    R!H u0 {4,D} {10,S}
7  * R!H u0 {5,S} {9,S}
8    R!H u0 {3,S} {10,D}
9    R!H u0 {2,S} {7,S}
10   R!H u0 {6,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-39.7954,-42.8746,-42.2591,-38.4302,-28.2183,-19.3441,-7.24736],'J/(mol*K)'),
        H298 = (72.801,'kJ/mol'),
        S298 = (204.461,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_5_6_diene_1_3 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 45,
    label = "s1_5_6_diene_1_4",
    group = 
"""
1    R!H u0 {2,S} {3,S} {4,S} {5,S}
2    R!H u0 {1,S} {6,S}
3    R!H u0 {1,S} {8,D}
4    R!H u0 {1,S} {9,D}
5    R!H u0 {1,S} {7,S}
6  * R!H u0 {2,S} {7,S}
7    R!H u0 {5,S} {6,S}
8    R!H u0 {3,D} {10,S}
9    R!H u0 {4,D} {10,S}
10   R!H u0 {8,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-35.6667,-36.4898,-35.0189,-31.5118,-22.9934,-15.5375,-4.36224],'J/(mol*K)'),
        H298 = (59.3275,'kJ/mol'),
        S298 = (200.02,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_5_6_diene_1_4 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 46,
    label = "s1_5_6_diene_1_7",
    group = 
"""
1    R!H u0 {2,S} {3,S} {4,S} {5,S}
2    R!H u0 {1,S} {7,S}
3    R!H u0 {1,S} {6,S}
4    R!H u0 {1,S} {9,D}
5    R!H u0 {1,S} {8,D}
6    R!H u0 {3,S} {10,S}
7  * R!H u0 {2,S} {9,S}
8    R!H u0 {5,D} {10,S}
9    R!H u0 {4,D} {7,S}
10   R!H u0 {6,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-35.9891,-36.4223,-34.915,-31.4934,-23.0673,-15.4092,-4.57912],'J/(mol*K)'),
        H298 = (58.6857,'kJ/mol'),
        S298 = (188.477,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_5_6_diene_1_7 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 47,
    label = "s1_5_6_diene_1_8",
    group = 
"""
1    R!H u0 {2,S} {3,S} {4,S} {5,S}
2    R!H u0 {1,S} {8,D}
3    R!H u0 {1,S} {6,S}
4    R!H u0 {1,S} {9,S}
5    R!H u0 {1,S} {7,S}
6  * R!H u0 {3,S} {9,D}
7    R!H u0 {5,S} {10,S}
8    R!H u0 {2,D} {10,S}
9    R!H u0 {4,S} {6,D}
10   R!H u0 {7,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-34.6352,-36.1588,-35.1599,-31.9161,-23.4179,-15.7099,-4.90436],'J/(mol*K)'),
        H298 = (57.6654,'kJ/mol'),
        S298 = (185.08,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_5_6_diene_1_8 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 48,
    label = "s1_5_6_diene_2_7",
    group = 
"""
1    R!H u0 {2,S} {3,S} {4,S} {5,S}
2    R!H u0 {1,S} {7,S}
3    R!H u0 {1,S} {9,D}
4    R!H u0 {1,S} {8,S}
5    R!H u0 {1,S} {6,S}
6  * R!H u0 {5,S} {9,S}
7    R!H u0 {2,S} {10,S}
8    R!H u0 {4,S} {10,D}
9    R!H u0 {3,D} {6,S}
10   R!H u0 {7,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-34.7112,-36.2688,-35.2949,-32.0641,-23.5669,-15.8379,-4.95936],'J/(mol*K)'),
        H298 = (53.8784,'kJ/mol'),
        S298 = (184.339,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_5_6_diene_2_7 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 49,
    label = "s1_5_6_diene_2_8",
    group = 
"""
1    R!H u0 {2,S} {3,S} {4,S} {5,S}
2    R!H u0 {1,S} {6,S}
3    R!H u0 {1,S} {9,S}
4    R!H u0 {1,S} {7,S}
5    R!H u0 {1,S} {8,S}
6  * R!H u0 {2,S} {7,D}
7    R!H u0 {4,S} {6,D}
8    R!H u0 {5,S} {10,D}
9    R!H u0 {3,S} {10,S}
10   R!H u0 {8,D} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-35.2712,-36.7788,-35.6669,-32.3201,-23.6669,-15.6059,-4.94136],'J/(mol*K)'),
        H298 = (60.7522,'kJ/mol'),
        S298 = (183.826,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_5_6_diene_2_8 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 50,
    label = "s1_5_6_diene_7_9",
    group = 
"""
1    R!H u0 {2,S} {3,S} {4,S} {5,S}
2    R!H u0 {1,S} {6,D}
3    R!H u0 {1,S} {7,S}
4    R!H u0 {1,S} {9,S}
5    R!H u0 {1,S} {8,D}
6  * R!H u0 {2,D} {8,S}
7    R!H u0 {3,S} {10,S}
8    R!H u0 {5,D} {6,S}
9    R!H u0 {4,S} {10,S}
10   R!H u0 {7,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-43.7003,-43.9141,-41.7872,-37.9574,-27.9957,-19.0344,-6.51312],'J/(mol*K)'),
        H298 = (65.9717,'kJ/mol'),
        S298 = (199.055,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_5_6_diene_7_9 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s1_5_6_triene",
    group = "OR{s1_5_6_triene_1_3_7, s1_5_6_triene_1_3_8}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "s1_5_6_triene_1_3_7",
    group = 
"""
1    R!H u0 {2,S} {3,S} {4,S} {5,S}
2    R!H u0 {1,S} {8,S}
3    R!H u0 {1,S} {7,D}
4    R!H u0 {1,S} {6,D}
5    R!H u0 {1,S} {9,S}
6  * R!H u0 {4,D} {9,S}
7    R!H u0 {3,D} {10,S}
8    R!H u0 {2,S} {10,D}
9    R!H u0 {5,S} {6,S}
10   R!H u0 {7,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.72,-6.82,-6.48,-5.99,-5.19,-4.29,-2.12],'cal/(mol*K)'),
        H298 = (14.743,'kcal/mol'),
        S298 = (57.75,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt17 from C10H11 library.
""",
)

entry(
    index = 44,
    label = "s1_5_6_triene_1_3_8",
    group = 
"""
1    R!H u0 {2,S} {3,S} {4,S} {5,S}
2    R!H u0 {1,S} {8,S}
3    R!H u0 {1,S} {9,S}
4    R!H u0 {1,S} {7,S}
5    R!H u0 {1,S} {6,D}
6    R!H u0 {5,D} {10,S}
7  * R!H u0 {4,S} {8,D}
8    R!H u0 {2,S} {7,D}
9    R!H u0 {3,S} {10,D}
10   R!H u0 {6,S} {9,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.34,-6.73,-6.55,-6.13,-5.34,-4.43,-2.23],'cal/(mol*K)'),
        H298 = (14.573,'kcal/mol'),
        S298 = (57.37,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt17 from C10H11 library.
""",
)

entry(
    index = 0,
    label = "s1_5_6_tetraene",
    group = "OR{s1_5_6_tetraene_1_3_7_9, s1_5_6_tetraene_1_4_7_9}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "s1_5_6_tetraene_1_3_7_9",
    group = 
"""
1    R!H u0 {2,S} {3,S} {4,S} {5,S}
2    R!H u0 {1,S} {8,S}
3    R!H u0 {1,S} {6,D}
4    R!H u0 {1,S} {9,D}
5    R!H u0 {1,S} {7,D}
6    R!H u0 {3,D} {10,S}
7  * R!H u0 {5,D} {9,S}
8    R!H u0 {2,S} {10,D}
9    R!H u0 {4,D} {7,S}
10   R!H u0 {6,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.54,-7.38,-7.43,-7.04,-6.22,-5.38,-3.12],'cal/(mol*K)'),
        H298 = (3.583,'kcal/mol'),
        S298 = (59.28,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species prod2 from naphthalene_H library.
""",
)

entry(
    index = 44,
    label = "s1_5_6_tetraene_1_4_7_9",
    group = 
"""
1    R!H u0 {2,S} {3,S} {4,S} {5,S}
2    R!H u0 {1,S} {7,D}
3    R!H u0 {1,S} {9,D}
4    R!H u0 {1,S} {8,D}
5    R!H u0 {1,S} {6,D}
6  * R!H u0 {5,D} {8,S}
7    R!H u0 {2,D} {10,S}
8    R!H u0 {4,D} {6,S}
9    R!H u0 {3,D} {10,S}
10   R!H u0 {7,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.98,-5.93,-5.62,-5.32,-5,-4.36,-3.36],'cal/(mol*K)'),
        H298 = (11.133,'kcal/mol'),
        S298 = (57.08,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species prod2 from naphthalene_H library.
""",
)

entry(
    index = 0,
    label = "s1_6_6",
    group = 
"""
1    R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2    R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
3    R!H u0 {1,[S,D,T,B]} {9,[S,D,T,B]}
4    R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
5    R!H u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H u0 {5,[S,D,T,B]} {11,[S,D,T,B]}
7    R!H u0 {4,[S,D,T,B]} {10,[S,D,T,B]}
8    R!H u0 {2,[S,D,T,B]} {11,[S,D,T,B]}
9    R!H u0 {3,[S,D,T,B]} {10,[S,D,T,B]}
10 * R!H u0 {7,[S,D,T,B]} {9,[S,D,T,B]}
11   R!H u0 {6,[S,D,T,B]} {8,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
    label = "s1_6_6_ane",
    group = 
"""
1    R!H u0 {2,S} {3,S} {4,S} {5,S}
2    R!H u0 {1,S} {8,S}
3    R!H u0 {1,S} {9,S}
4    R!H u0 {1,S} {7,S}
5    R!H u0 {1,S} {6,S}
6    R!H u0 {5,S} {11,S}
7    R!H u0 {4,S} {10,S}
8    R!H u0 {2,S} {11,S}
9    R!H u0 {3,S} {10,S}
10 * R!H u0 {7,S} {9,S}
11   R!H u0 {6,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-55.7171,-52.1049,-47.8292,-41.7251,-27.7865,-16.1164,0.04892],'J/(mol*K)'),
        H298 = (46.8142,'kJ/mol'),
        S298 = (148.984,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_6_6_ane from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s1_6_6_ene",
    group = "OR{s1_6_6_ene_1, s1_6_6_ene_2}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
    label = "s1_6_6_ene_1",
    group = 
"""
1    R!H u0 {2,S} {3,S} {4,S} {5,S}
2    R!H u0 {1,S} {9,S}
3    R!H u0 {1,S} {8,S}
4    R!H u0 {1,S} {7,S}
5    R!H u0 {1,S} {6,D}
6    R!H u0 {5,D} {11,S}
7    R!H u0 {4,S} {11,S}
8    R!H u0 {3,S} {10,S}
9    R!H u0 {2,S} {10,S}
10 * R!H u0 {8,S} {9,S}
11   R!H u0 {6,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-47.3541,-46.0382,-43.0651,-38.0298,-26.1211,-16.0345,-1.56372],'J/(mol*K)'),
        H298 = (43.6103,'kJ/mol'),
        S298 = (157.914,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_6_6_ene_1 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 53,
    label = "s1_6_6_ene_2",
    group = 
"""
1    R!H u0 {2,S} {3,S} {4,S} {5,S}
2    R!H u0 {1,S} {9,S}
3    R!H u0 {1,S} {8,S}
4    R!H u0 {1,S} {7,S}
5    R!H u0 {1,S} {6,S}
6    R!H u0 {5,S} {10,S}
7    R!H u0 {4,S} {11,S}
8    R!H u0 {3,S} {10,D}
9    R!H u0 {2,S} {11,S}
10 * R!H u0 {6,S} {8,D}
11   R!H u0 {7,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-47.8371,-46.4772,-43.3751,-38.2268,-26.1521,-15.7134,-1.41472],'J/(mol*K)'),
        H298 = (44.1274,'kJ/mol'),
        S298 = (154.518,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_6_6_ene_2 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s1_6_6_diene",
    group = "OR{s1_6_6_diene_1_3, s1_6_6_diene_1_4, s1_6_6_diene_1_7, s1_6_6_diene_1_8, s1_6_6_diene_2_8}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 54,
    label = "s1_6_6_diene_1_3",
    group = 
"""
1    R!H u0 {2,S} {3,S} {4,S} {5,S}
2    R!H u0 {1,S} {6,D}
3    R!H u0 {1,S} {9,S}
4    R!H u0 {1,S} {8,S}
5    R!H u0 {1,S} {7,S}
6    R!H u0 {2,D} {11,S}
7    R!H u0 {5,S} {10,S}
8    R!H u0 {4,S} {10,S}
9    R!H u0 {3,S} {11,D}
10 * R!H u0 {7,S} {8,S}
11   R!H u0 {6,S} {9,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-44.2714,-46.0734,-44.5631,-39.8526,-28.0332,-18.0187,-4.52436],'J/(mol*K)'),
        H298 = (53.0262,'kJ/mol'),
        S298 = (178.633,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_6_6_diene_1_3 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 55,
    label = "s1_6_6_diene_1_4",
    group = 
"""
1    R!H u0 {2,S} {3,S} {4,S} {5,S}
2    R!H u0 {1,S} {9,D}
3    R!H u0 {1,S} {6,D}
4    R!H u0 {1,S} {7,S}
5    R!H u0 {1,S} {8,S}
6    R!H u0 {3,D} {10,S}
7    R!H u0 {4,S} {11,S}
8    R!H u0 {5,S} {11,S}
9    R!H u0 {2,D} {10,S}
10 * R!H u0 {6,S} {9,S}
11   R!H u0 {7,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-40.5047,-40.1916,-37.9209,-33.5862,-23.4803,-14.826,-2.00624],'J/(mol*K)'),
        H298 = (39.1356,'kJ/mol'),
        S298 = (169.445,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_6_6_diene_1_4 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 56,
    label = "s1_6_6_diene_1_7",
    group = 
"""
1    R!H u0 {2,S} {3,S} {4,S} {5,S}
2    R!H u0 {1,S} {9,S}
3    R!H u0 {1,S} {7,D}
4    R!H u0 {1,S} {6,S}
5    R!H u0 {1,S} {8,D}
6    R!H u0 {4,S} {10,S}
7    R!H u0 {3,D} {11,S}
8    R!H u0 {5,D} {10,S}
9    R!H u0 {2,S} {11,S}
10 * R!H u0 {6,S} {8,S}
11   R!H u0 {7,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-40.4071,-39.8001,-37.642,-33.4998,-23.6002,-14.7647,-2.20412],'J/(mol*K)'),
        H298 = (44.4007,'kJ/mol'),
        S298 = (161.695,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_6_6_diene_1_7 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 57,
    label = "s1_6_6_diene_1_8",
    group = 
"""
1    R!H u0 {2,S} {3,S} {4,S} {5,S}
2    R!H u0 {1,S} {6,S}
3    R!H u0 {1,S} {9,S}
4    R!H u0 {1,S} {7,S}
5    R!H u0 {1,S} {8,D}
6    R!H u0 {2,S} {10,S}
7    R!H u0 {4,S} {11,S}
8    R!H u0 {5,D} {10,S}
9    R!H u0 {3,S} {11,D}
10 * R!H u0 {6,S} {8,S}
11   R!H u0 {7,S} {9,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-38.8102,-39.3246,-37.7479,-33.8445,-23.9548,-15.1125,-2.58536],'J/(mol*K)'),
        H298 = (42.1676,'kJ/mol'),
        S298 = (164.025,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_6_6_diene_1_8 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 58,
    label = "s1_6_6_diene_2_8",
    group = 
"""
1    R!H u0 {2,S} {3,S} {4,S} {5,S}
2    R!H u0 {1,S} {6,S}
3    R!H u0 {1,S} {7,S}
4    R!H u0 {1,S} {8,S}
5    R!H u0 {1,S} {9,S}
6    R!H u0 {2,S} {10,S}
7    R!H u0 {3,S} {11,D}
8    R!H u0 {4,S} {11,S}
9    R!H u0 {5,S} {10,D}
10 * R!H u0 {6,S} {9,D}
11   R!H u0 {7,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-39.2022,-39.6126,-37.8839,-33.8635,-23.8298,-14.6794,-2.43436],'J/(mol*K)'),
        H298 = (39.5522,'kJ/mol'),
        S298 = (153.945,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_6_6_diene_2_8 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s2_3_3",
    group = 
"""
1   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]}
3 * R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 59,
    label = "s2_3_3_ane",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S}
2   R!H u0 {1,S} {3,S} {4,S}
3 * R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-19.1641,-21.2261,-21.3966,-21.0012,-20.5848,-18.9855,-17.7496],'J/(mol*K)'),
        H298 = (265.181,'kJ/mol'),
        S298 = (281.033,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_3_3_ane from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 60,
    label = "s2_3_3_ene",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S}
2   R!H u0 {1,S} {3,S} {4,D}
3 * R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-18.1001,-18.8362,-18.9708,-18.8323,-18.5781,-18.025,-17.5057],'J/(mol*K)'),
        H298 = (421.625,'kJ/mol'),
        S298 = (294.969,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_3_3_ene from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s2_3_4",
    group = 
"""
1 * R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {1,[S,D,T,B]} {5,[S,D,T,B]}
5   R!H u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 61,
    label = "s2_3_4_ane",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {4,S}
2   R!H u0 {1,S} {3,S} {5,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {5,S}
5   R!H u0 {2,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-26.6855,-27.0954,-25.6766,-23.9346,-21.4297,-18.3751,-15.4426],'J/(mol*K)'),
        H298 = (235.153,'kJ/mol'),
        S298 = (259.976,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_3_4_ane from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s2_3_4_ene",
    group = "OR{s2_3_4_ene_1, s2_3_4_ene_m}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 62,
    label = "s2_3_4_ene_1",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {5,S}
2   R!H u0 {1,S} {3,S} {4,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {2,S} {5,D}
5   R!H u0 {1,S} {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-17.8212,-19.1667,-19.7442,-18.7173,-18.5644,-16.8951,-16.0612],'J/(mol*K)'),
        H298 = (292.756,'kJ/mol'),
        S298 = (268.817,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_3_4_ene_1 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 63,
    label = "s2_3_4_ene_m",
    group = 
"""
1 * R!H u0 {2,D} {3,S} {5,S}
2   R!H u0 {1,D} {3,S} {4,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {2,S} {5,S}
5   R!H u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.52,-5.35,-5.15,-4.39,-3.54,-3.73,-2.7],'cal/(mol*K)'),
        H298 = (126,'kcal/mol'),
        S298 = (66.41,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Wiberg, K. Angew. Chem., Int. Ed. Engl. 1986, 25, 312 1986 ab initio, S, Cp from PM7 calculation
""",
)

entry(
    index = 0,
    label = "s2_3_5",
    group = 
"""
1 * R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {6,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
6   R!H u0 {4,[S,D,T,B]} {5,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 64,
    label = "s2_3_5_ane",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {5,S}
2   R!H u0 {1,S} {3,S} {4,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {2,S} {6,S}
5   R!H u0 {1,S} {6,S}
6   R!H u0 {4,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-31.3918,-30.9812,-28.7286,-26.071,-21.6806,-17.2716,-12.7686],'J/(mol*K)'),
        H298 = (155.862,'kJ/mol'),
        S298 = (249.315,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_3_5_ane from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s2_3_5_ene",
    group = "OR{s2_3_5_ene_1, s2_3_5_ene_side, s2_3_5_ene_1_side}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 65,
    label = "s2_3_5_ene_1",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {5,S}
2   R!H u0 {1,S} {3,S} {4,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {2,S} {6,D}
5   R!H u0 {1,S} {6,S}
6   R!H u0 {4,D} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-24.7584,-24.8025,-23.7178,-21.9727,-19.7792,-16.6276,-13.9142],'J/(mol*K)'),
        H298 = (143.681,'kJ/mol'),
        S298 = (247.197,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_3_5_ene_1 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 65,
    label = "s2_3_5_ene_side",
    group = 
"""
1 * R!H   u0 {2,S} {4,S} {6,S}
2   R!H   u0 {1,S} {4,S} {5,S}
3   R!H   u0 {5,S} {6,S} {7,D}
4   R!H   u0 {1,S} {2,S}
5   R!H   u0 {2,S} {3,S}
6   R!H   u0 {1,S} {3,S}
7   R!H ux {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.97,-4.68,-4.47,-4.27,-4.21,-3.94,-3.36],'cal/(mol*K)'),
        H298 = (32.543,'kcal/mol'),
        S298 = (65.1674,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species product36 from vinylCPD_H library.
""",
)

entry(
    index = 65,
    label = "s2_3_5_ene_1_side",
    group = 
"""
1 * R!H   u0 {2,S} {3,S} {4,S}
2   R!H   u0 {1,S} {3,S} {5,S}
3   R!H   u0 {1,S} {2,S} {7,D}
4   R!H   u0 {1,S} {6,S}
5   R!H   u0 {2,S} {6,D}
6   R!H   u0 {4,S} {5,D}
7   R!H ux {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.48,-3.9,-3.81,-3.6,-3.7,-3.68,-3.44],'cal/(mol*K)'),
        H298 = (47.323,'kcal/mol'),
        S298 = (66.8874,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species product42 from vinylCPD_H library.
""",
)

entry(
    index = 65,
    label = "s2_3_5_diene",
    group = "OR{s2_3_5_diene_0_2}",
    thermo = None,
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 65,
    label = "s2_3_5_diene_0_2",
    group=
    """
    1 * R!H u0 {2,S} {3,S} {5,S}
    2   R!H u0 {1,S} {3,S} {4,D}
    3   R!H u0 {1,S} {2,S}
    4   R!H u0 {2,D} {6,S}
    5   R!H u0 {1,S} {6,D}
    6   R!H u0 {4,S} {5,D}
    """,
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-7.289, -6.524, -6.162, -6.421, -5.93, -4.094, -3.76], 'cal/(mol*K)'),
        H298=(68.847, 'kcal/mol'),
        S298=(65.182, 'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
Fitted to RQCISD(T)/cc-PV(infinity)(Q)Z calculations for "Intermediate B" of:

Miller, J. A.; Klippenstein, S. J., The Recombination of Propargyl Radicals and Other Reactions on a C6H6 Potential.
J. Phys. Chem. A 2003, 107, 7783-7799.
""",
)

entry(
    index = 0,
    label = "s2_3_6",
    group = 
"""
1   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {6,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6 * R!H u0 {4,[S,D,T,B]} {7,[S,D,T,B]}
7   R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 66,
    label = "s2_3_6_ane",
    group = 
"""
1   R!H u0 {2,S} {3,S} {5,S}
2   R!H u0 {1,S} {3,S} {4,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {2,S} {6,S}
5   R!H u0 {1,S} {7,S}
6 * R!H u0 {4,S} {7,S}
7   R!H u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-34.1217,-33.381,-31.0886,-28.1514,-22.0855,-16.4152,-10.3396],'J/(mol*K)'),
        H298 = (154.711,'kJ/mol'),
        S298 = (236.447,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc=
    u"""
    Fitted from molecule s2_3_6_ane from Bicyclics_QM_190_isomorphic library.
    """,
)

entry(
    index = 0,
    label = "s2_3_6_ene",
    group = "OR{s2_3_6_ene_1, s2_3_6_ene_2, s2_3_6_ene_5}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 67,
    label = "s2_3_6_ene_1",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S}
2   R!H u0 {1,S} {3,S} {5,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {6,D}
5   R!H u0 {2,S} {7,S}
6 * R!H u0 {4,D} {7,S}
7   R!H u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-28.4108,-28.0783,-26.7728,-24.5521,-20.6811,-16.2322,-11.7072],'J/(mol*K)'),
        H298 = (127.466,'kJ/mol'),
        S298 = (229.109,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_3_6_ene_1 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 68,
    label = "s2_3_6_ene_2",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S}
2   R!H u0 {1,S} {3,S} {5,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {7,S}
5   R!H u0 {2,S} {6,S}
6 * R!H u0 {5,S} {7,D}
7   R!H u0 {4,S} {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-27.3578,-27.8213,-26.4574,-24.6241,-20.6081,-16.0552,-11.4352],'J/(mol*K)'),
        H298 = (129.473,'kJ/mol'),
        S298 = (228.854,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_3_6_ene_2 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s2_3_6_diene",
    group = "OR{s2_3_6_diene_0_2, s2_3_6_diene_0_3, s2_3_6_diene_1_3, s2_3_6_diene_2_5, s2_3_6_diene_1_6}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 69,
    label = "s2_3_6_diene_0_2",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,D}
2   R!H u0 {1,S} {3,S} {5,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {1,D} {6,S}
5   R!H u0 {2,S} {7,S}
6 * R!H u0 {4,S} {7,D}
7   R!H u0 {5,S} {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.31,-5.83,-5.92,-5.53,-5.17,-4.71,-3.89],'cal/(mol*K)'),
        H298 = (48.433,'kcal/mol'),
        S298 = (65.9,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species product46 from vinylCPD_H library.
""",
)

entry(
    index = 69,
    label = "s2_3_6_diene_0_3",
    group = 
"""
1   R!H u0 {2,S} {3,S} {5,D}
2   R!H u0 {1,S} {3,S} {4,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {2,S} {7,D}
5   R!H u0 {1,D} {6,S}
6 * R!H u0 {5,S} {7,S}
7   R!H u0 {4,D} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.82,-4.74,-4.65,-4.52,-4.39,-4.28,-4.42],'cal/(mol*K)'),
        H298 = (53.563,'kcal/mol'),
        S298 = (63.9,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species product46 from vinylCPD_H library.
""",
)

entry(
    index = 69,
    label = "s2_3_6_diene_1_3",
    group = 
"""
1   R!H u0 {2,S} {3,S} {5,S}
2   R!H u0 {1,S} {3,S} {4,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {2,S} {6,D}
5   R!H u0 {1,S} {7,D}
6 * R!H u0 {4,D} {7,S}
7   R!H u0 {5,D} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-26.895,-29.0314,-29.3182,-27.1409,-23.4002,-18.9034,-14.9088],'J/(mol*K)'),
        H298 = (117.743,'kJ/mol'),
        S298 = (247.955,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_3_6_diene_1_3 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 69,
    label = "s2_3_6_ben",
    group = 
"""
1   R!H u0 {2,B} {3,S} {4,B}
2   R!H u0 {1,B} {3,S} {5,B}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {1,B} {6,B}
5   R!H u0 {2,B} {7,B}
6 * R!H u0 {4,B} {7,B}
7   R!H u0 {5,B} {6,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.23868,-6.14716,-7.46984,-9.00368,-10.5504,-10.8542,-11.9072],'J/(mol*K)'),
        H298 = (286.99,'kJ/mol'),
        S298 = (144.432,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_3_6_ben from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s2_3_7",
    group = 
"""
1 * R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {6,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   R!H u0 {4,[S,D,T,B]} {8,[S,D,T,B]}
7   R!H u0 {5,[S,D,T,B]} {8,[S,D,T,B]}
8   R!H u0 {6,[S,D,T,B]} {7,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 70,
    label = "s2_3_7_ane",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {5,S}
2   R!H u0 {1,S} {3,S} {4,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {2,S} {6,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {4,S} {8,S}
7   R!H u0 {5,S} {8,S}
8   R!H u0 {6,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10.29,-9.54,-7.86,-5.68,-2.67,-2.04,0.13],'cal/(mol*K)'),
        H298 = (29.64,'kcal/mol'),
        S298 = (51.29,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Properties of Liquids and Gases, Poling 5th Ed. S, Cp from PM7 calculation
""",
)

entry(
    index = 0,
    label = "s2_3_8",
    group = 
"""
1 * R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {6,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   R!H u0 {4,[S,D,T,B]} {8,[S,D,T,B]}
7   R!H u0 {5,[S,D,T,B]} {9,[S,D,T,B]}
8   R!H u0 {6,[S,D,T,B]} {9,[S,D,T,B]}
9   R!H u0 {7,[S,D,T,B]} {8,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 71,
    label = "s2_3_8_ane",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {5,S}
2   R!H u0 {1,S} {3,S} {4,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {2,S} {6,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {4,S} {8,S}
7   R!H u0 {5,S} {9,S}
8   R!H u0 {6,S} {9,S}
9   R!H u0 {7,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-11.04,-10.02,-8.09,-5.64,-2.16,-1.32,1.06],'cal/(mol*K)'),
        H298 = (31.14,'kcal/mol'),
        S298 = (48.46,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Properties of Liquids and Gases, Poling 5th Ed. S, Cp from PM7 calculation
""",
)

entry(
    index = 0,
    label = "s2_4_4",
    group = 
"""
1   R!H u0 {2,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {6,[S,D,T,B]}
3 * R!H u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
4   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
6   R!H u0 {2,[S,D,T,B]} {5,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 72,
    label = "s2_4_4_ane",
    group = 
"""
1   R!H u0 {2,S} {4,S} {5,S}
2   R!H u0 {1,S} {3,S} {6,S}
3 * R!H u0 {2,S} {4,S}
4   R!H u0 {1,S} {3,S}
5   R!H u0 {1,S} {6,S}
6   R!H u0 {2,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-30.7295,-30.4822,-28.2596,-25.503,-20.9696,-16.5226,-12.1466],'J/(mol*K)'),
        H298 = (242.33,'kJ/mol'),
        S298 = (246.529,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_4_4_ane from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s2_4_4_ene",
    group = "OR{s2_4_4_ene_1, s2_4_4_ene_m}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 73,
    label = "s2_4_4_ene_1",
    group = 
"""
1   R!H u0 {2,S} {3,S} {5,S}
2   R!H u0 {1,S} {4,S} {6,S}
3 * R!H u0 {1,S} {4,S}
4   R!H u0 {2,S} {3,S}
5   R!H u0 {1,S} {6,D}
6   R!H u0 {2,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-21.6067,-23.7095,-24.7172,-23.3277,-21.1902,-17.8256,-14.2532],'J/(mol*K)'),
        H298 = (107.279,'kJ/mol'),
        S298 = (249.266,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_4_4_ene_1 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 74,
    label = "s2_4_4_ene_m",
    group = 
"""
1   R!H u0 {2,D} {4,S} {6,S}
2   R!H u0 {1,D} {3,S} {5,S}
3 * R!H u0 {2,S} {4,S}
4   R!H u0 {1,S} {3,S}
5   R!H u0 {2,S} {6,S}
6   R!H u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.4,-6.61,-5.83,-4.57,-3.17,-3.27,-1.87],'cal/(mol*K)'),
        H298 = (87,'kcal/mol'),
        S298 = (58.64,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Wiberg, K. Angew. Chem., Int. Ed. Engl. 1986, 25, 312 1986 ab initio S, Cp from PM7 calculation
""",
)

entry(
    index = 0,
    label = "s2_4_5",
    group = 
"""
1 * R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
7   R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 75,
    label = "s2_4_5_ane",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {5,S}
2   R!H u0 {1,S} {4,S} {6,S}
3   R!H u0 {1,S} {4,S}
4   R!H u0 {2,S} {3,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {2,S} {7,S}
7   R!H u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-37.4357,-35.921,-32.5766,-28.8184,-22.2445,-16.2852,-9.99256],'J/(mol*K)'),
        H298 = (158.515,'kJ/mol'),
        S298 = (222.223,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_4_5_ane from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s2_4_5_ene",
    group = "OR{s2_4_5_ene_0, s2_4_5_ene_1}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 76,
    label = "s2_4_5_ene_0",
    group = 
"""
1 * R!H u0 {2,S} {4,S} {6,D}
2   R!H u0 {1,S} {3,S} {5,S}
3   R!H u0 {2,S} {4,S}
4   R!H u0 {1,S} {3,S}
5   R!H u0 {2,S} {7,S}
6   R!H u0 {1,D} {7,S}
7   R!H u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.32,-5.85,-5.4,-4.81,-4.34,-3.92,-3.03],'cal/(mol*K)'),
        H298 = (45.173,'kcal/mol'),
        S298 = (60.95,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species product25 from vinylCPD_H library.
""",
)

entry(
    index = 76,
    label = "s2_4_5_ene_1",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {6,S}
2   R!H u0 {1,S} {4,S} {5,S}
3   R!H u0 {1,S} {4,S}
4   R!H u0 {2,S} {3,S}
5   R!H u0 {2,S} {7,S}
6   R!H u0 {1,S} {7,D}
7   R!H u0 {5,S} {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-30.3838,-30.0633,-28.0708,-25.0151,-20.5371,-15.7662,-11.1222],'J/(mol*K)'),
        H298 = (145.91,'kJ/mol'),
        S298 = (229.455,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_4_5_ene_1 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s2_4_5_diene",
    group = "OR{s2_4_5_diene_0_3, s2_4_5_diene_1_5, s2_4_5_diene_4_6}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 76,
    label = "s2_4_5_diene_0_3",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {5,D}
2   R!H u0 {1,S} {4,S} {6,D}
3   R!H u0 {1,S} {4,S}
4   R!H u0 {2,S} {3,S}
5   R!H u0 {1,D} {7,S}
6   R!H u0 {2,D} {7,S}
7   R!H u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-28.322,-31.1459,-30.1867,-27.682,-22.5644,-18.2478,-12.9942],'J/(mol*K)'),
        H298 = (220.315,'kJ/mol'),
        S298 = (247.242,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_4_5_diene_0_3 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 76,
    label = "s2_4_5_diene_1_5",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {6,S}
2   R!H u0 {1,S} {4,S} {5,S}
3   R!H u0 {1,S} {4,D}
4   R!H u0 {2,S} {3,D}
5   R!H u0 {2,S} {7,D}
6   R!H u0 {1,S} {7,S}
7   R!H u0 {5,D} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.23,-4.36,-3.97,-3.6,-3.53,-3.44,-3.16],'cal/(mol*K)'),
        H298 = (39.483,'kcal/mol'),
        S298 = (62.16,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species product45 from vinylCPD_H library.
""",
)

entry(
    index = 76,
    label = "s2_4_5_diene_4_6",
    group = 
"""
1 * R!H u0 {2,S} {3,D} {6,S}
2   R!H u0 {1,S} {4,D} {5,S}
3   R!H u0 {1,D} {4,S}
4   R!H u0 {2,D} {3,S}
5   R!H u0 {2,S} {7,S}
6   R!H u0 {1,S} {7,S}
7   R!H u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-37.8976,-43.0012,-43.237,-40.8415,-34.8466,-29.5607,-23.5751],'J/(mol*K)'),
        H298 = (427.842,'kJ/mol'),
        S298 = (261.07,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_4_5_diene_4_6 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s2_4_6",
    group = 
"""
1   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {6,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]}
5   R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
6   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
7 * R!H u0 {6,[S,D,T,B]} {8,[S,D,T,B]}
8   R!H u0 {5,[S,D,T,B]} {7,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 77,
    label = "s2_4_6_ane",
    group = 
"""
1   R!H u0 {2,S} {3,S} {6,S}
2   R!H u0 {1,S} {4,S} {5,S}
3   R!H u0 {1,S} {4,S}
4   R!H u0 {2,S} {3,S}
5   R!H u0 {2,S} {8,S}
6   R!H u0 {1,S} {7,S}
7 * R!H u0 {6,S} {8,S}
8   R!H u0 {5,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-41.7977,-39.2888,-35.4246,-31.1778,-22.8764,-15.6108,-7.57856],'J/(mol*K)'),
        H298 = (142,'kJ/mol'),
        S298 = (204.981,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_4_6_ane from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s2_4_6_ene",
    group = "OR{s2_4_6_ene_1, s2_4_6_ene_2, s2_4_6_ene_6}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 78,
    label = "s2_4_6_ene_1",
    group = 
"""
1   R!H u0 {2,S} {3,S} {5,S}
2   R!H u0 {1,S} {4,S} {6,S}
3   R!H u0 {1,S} {4,S}
4   R!H u0 {2,S} {3,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {2,S} {8,D}
7 * R!H u0 {5,S} {8,S}
8   R!H u0 {6,D} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-34.0688,-33.2111,-30.9698,-27.4685,-21.216,-15.1138,-8.7302],'J/(mol*K)'),
        H298 = (131.146,'kJ/mol'),
        S298 = (210.041,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_4_6_ene_1 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 79,
    label = "s2_4_6_ene_2",
    group = 
"""
1   R!H u0 {2,S} {4,S} {6,S}
2   R!H u0 {1,S} {3,S} {5,S}
3   R!H u0 {2,S} {4,S}
4   R!H u0 {1,S} {3,S}
5   R!H u0 {2,S} {7,S}
6   R!H u0 {1,S} {8,S}
7 * R!H u0 {5,S} {8,D}
8   R!H u0 {6,S} {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-33.6208,-33.1691,-30.7394,-27.6625,-21.257,-15.0638,-8.6292],'J/(mol*K)'),
        H298 = (147.009,'kJ/mol'),
        S298 = (217.246,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_4_6_ene_2 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 79,
    label = "s2_4_6_ene_6",
    group = 
"""
1   R!H u0 {2,S} {4,S} {5,S}
2   R!H u0 {1,S} {3,S} {6,S}
3   R!H u0 {2,S} {4,D}
4   R!H u0 {1,S} {3,D}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {2,S} {8,S}
7 * R!H u0 {5,S} {8,S}
8   R!H u0 {6,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-34.5248,-33.2711,-31.3482,-27.5195,-21.339,-15.2388,-8.7172],'J/(mol*K)'),
        H298 = (220.778,'kJ/mol'),
        S298 = (206.929,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_4_6_ene_6 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s2_4_6_diene",
    group = "OR{s2_4_6_diene_1_3, s2_4_6_diene_1_6, s2_4_6_diene_2_6, s2_4_6_diene_5_7}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 180,
    label = "s2_4_6_diene_1_3",
    group = 
"""
1   R!H u0 {2,S} {3,S} {6,S}
2   R!H u0 {1,S} {4,S} {5,S}
3   R!H u0 {1,S} {4,S}
4   R!H u0 {2,S} {3,S}
5   R!H u0 {2,S} {8,D}
6   R!H u0 {1,S} {7,D}
7 * R!H u0 {6,D} {8,S}
8   R!H u0 {5,D} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-31.986,-33.8622,-33.2742,-29.8063,-23.812,-17.728,-11.9048],'J/(mol*K)'),
        H298 = (142.193,'kJ/mol'),
        S298 = (230.904,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_4_6_diene_1_3 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 181,
    label = "s2_4_6_diene_1_6",
    group = 
"""
1   R!H u0 {2,S} {4,S} {6,S}
2   R!H u0 {1,S} {3,S} {5,S}
3   R!H u0 {2,S} {4,D}
4   R!H u0 {1,S} {3,D}
5   R!H u0 {2,S} {8,S}
6   R!H u0 {1,S} {7,D}
7 * R!H u0 {6,D} {8,S}
8   R!H u0 {5,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-31.9988,-29.4179,-26.9519,-23.8658,-18.4622,-13.6342,-8.98624],'J/(mol*K)'),
        H298 = (152.835,'kJ/mol'),
        S298 = (221.861,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_4_6_diene_1_6 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 182,
    label = "s2_4_6_diene_2_6",
    group = 
"""
1   R!H u0 {2,S} {4,S} {5,S}
2   R!H u0 {1,S} {3,S} {6,S}
3   R!H u0 {2,S} {4,D}
4   R!H u0 {1,S} {3,D}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {2,S} {8,S}
7 * R!H u0 {5,S} {8,D}
8   R!H u0 {6,S} {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-24.2298,-25.4244,-25.289,-22.7942,-18.6756,-13.8318,-9.32484],'J/(mol*K)'),
        H298 = (159.306,'kJ/mol'),
        S298 = (218.773,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_4_6_diene_2_6 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 182,
    label = "s2_4_6_diene_5_7",
    group = 
"""
1   R!H u0 {2,S} {4,D} {6,S}
2   R!H u0 {1,S} {3,D} {5,S}
3   R!H u0 {2,D} {4,S}
4   R!H u0 {1,D} {3,S}
5   R!H u0 {2,S} {7,S}
6   R!H u0 {1,S} {8,S}
7 * R!H u0 {5,S} {8,S}
8   R!H u0 {6,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-33.7626,-39.097,-39.354,-35.5619,-26.8375,-20.0782,-13.0261],'J/(mol*K)'),
        H298 = (358.647,'kJ/mol'),
        S298 = (250.961,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_4_6_diene_5_7 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 183,
    label = "s2_4_6_ben",
    group = 
"""
1   R!H u0 {2,B} {4,S} {5,B}
2   R!H u0 {1,B} {3,S} {6,B}
3   R!H u0 {2,S} {4,S}
4   R!H u0 {1,S} {3,S}
5   R!H u0 {1,B} {7,B}
6   R!H u0 {2,B} {8,B}
7 * R!H u0 {5,B} {8,B}
8   R!H u0 {6,B} {7,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-13.1733,-12.9918,-12.2974,-11.6067,-9.36104,-6.5744,-1.5936],'J/(mol*K)'),
        H298 = (148.973,'kJ/mol'),
        S298 = (117.954,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_4_6_ben from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s2_5_5",
    group = 
"""
1   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
3 * R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
6   R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
7   R!H u0 {3,[S,D,T,B]} {4,[S,D,T,B]}
8   R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 80,
    label = "s2_5_5_ane",
    group = 
"""
1   R!H u0 {2,S} {3,S} {5,S}
2   R!H u0 {1,S} {4,S} {6,S}
3 * R!H u0 {1,S} {7,S}
4   R!H u0 {2,S} {7,S}
5   R!H u0 {1,S} {8,S}
6   R!H u0 {2,S} {8,S}
7   R!H u0 {3,S} {4,S}
8   R!H u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-44.0917,-41.3868,-36.9456,-32.1488,-23.4874,-16.0248,-7.87556],'J/(mol*K)'),
        H298 = (79.0986,'kJ/mol'),
        S298 = (198.831,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_5_ane from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s2_5_5_ene",
    group = "OR{s2_5_5_ene_0, s2_5_5_ene_1, s2_5_5_ene_m}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 81,
    label = "s2_5_5_ene_0",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S}
2   R!H u0 {1,S} {5,D} {6,S}
3 * R!H u0 {1,S} {8,S}
4   R!H u0 {1,S} {7,S}
5   R!H u0 {2,D} {7,S}
6   R!H u0 {2,S} {8,S}
7   R!H u0 {4,S} {5,S}
8   R!H u0 {3,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-35.6044,-35.1281,-32.8865,-28.9033,-21.809,-15.5238,-8.38732],'J/(mol*K)'),
        H298 = (88.2847,'kJ/mol'),
        S298 = (209.932,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_5_ene_0 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 82,
    label = "s2_5_5_ene_1",
    group = 
"""
1   R!H u0 {2,S} {4,S} {5,S}
2   R!H u0 {1,S} {3,S} {6,S}
3 * R!H u0 {2,S} {7,D}
4   R!H u0 {1,S} {8,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {2,S} {8,S}
7   R!H u0 {3,D} {5,S}
8   R!H u0 {4,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-35.5098,-34.6031,-31.9528,-27.9945,-21.362,-15.0548,-8.5992],'J/(mol*K)'),
        H298 = (71.0703,'kJ/mol'),
        S298 = (213.583,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_5_ene_1 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 83,
    label = "s2_5_5_ene_m",
    group = 
"""
1   R!H u0 {2,D} {3,S} {5,S}
2   R!H u0 {1,D} {4,S} {6,S}
3 * R!H u0 {1,S} {8,S}
4   R!H u0 {2,S} {7,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {2,S} {8,S}
7   R!H u0 {4,S} {5,S}
8   R!H u0 {3,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-36.0191,-36.797,-35.0088,-31.1401,-23.1831,-16.6038,-8.33044],'J/(mol*K)'),
        H298 = (86.2088,'kJ/mol'),
        S298 = (204.403,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_5_ene_m from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s2_5_5_diene",
    group = "OR{s2_5_5_diene_0_2, s2_5_5_diene_0_3, s2_5_5_diene_m_2, s2_5_5_diene_0_4, s2_5_5_diene_0_5, s2_5_5_diene_0_6, s2_5_5_diene_1_5, s2_5_5_diene_1_6}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 84,
    label = "s2_5_5_diene_0_2",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S}
2   R!H u0 {1,S} {5,S} {6,D}
3 * R!H u0 {1,S} {8,S}
4   R!H u0 {1,S} {7,D}
5   R!H u0 {2,S} {8,S}
6   R!H u0 {2,D} {7,S}
7   R!H u0 {4,D} {6,S}
8   R!H u0 {3,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-40.8587,-39.2967,-35.8144,-31.5587,-23.4596,-17.2834,-10.8314],'J/(mol*K)'),
        H298 = (98.2803,'kJ/mol'),
        S298 = (234.449,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_5_diene_0_2 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 85,
    label = "s2_5_5_diene_0_3",
    group = 
"""
1   R!H u0 {2,S} {4,D} {5,S}
2   R!H u0 {1,S} {3,D} {6,S}
3 * R!H u0 {2,D} {7,S}
4   R!H u0 {1,D} {7,S}
5   R!H u0 {1,S} {8,S}
6   R!H u0 {2,S} {8,S}
7   R!H u0 {3,S} {4,S}
8   R!H u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-34.896,-36.5947,-34.5687,-30.9814,-23.7952,-17.9894,-10.8592],'J/(mol*K)'),
        H298 = (84.3022,'kJ/mol'),
        S298 = (224.084,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_5_diene_0_3 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 86,
    label = "s2_5_5_diene_m_2",
    group = 
"""
1   R!H u0 {2,D} {3,S} {5,S}
2   R!H u0 {1,D} {4,S} {6,S}
3 * R!H u0 {1,S} {7,S}
4   R!H u0 {2,S} {8,D}
5   R!H u0 {1,S} {8,S}
6   R!H u0 {2,S} {7,S}
7   R!H u0 {3,S} {6,S}
8   R!H u0 {4,D} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-34.86,-37.5217,-35.9527,-32.3014,-24.7302,-18.6154,-11.0332],'J/(mol*K)'),
        H298 = (91.2676,'kJ/mol'),
        S298 = (226.061,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_5_diene_m_2 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 87,
    label = "s2_5_5_diene_0_4",
    group = 
"""
1   R!H u0 {2,S} {3,D} {4,S}
2   R!H u0 {1,S} {5,D} {6,S}
3 * R!H u0 {1,D} {7,S}
4   R!H u0 {1,S} {8,S}
5   R!H u0 {2,D} {8,S}
6   R!H u0 {2,S} {7,S}
7   R!H u0 {3,S} {6,S}
8   R!H u0 {4,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-34.0244,-37.3252,-36.5328,-33.1039,-25.4191,-18.94,-11.4871],'J/(mol*K)'),
        H298 = (89.4864,'kJ/mol'),
        S298 = (233.918,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_5_diene_0_4 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 88,
    label = "s2_5_5_diene_0_5",
    group = 
"""
1   R!H u0 {2,S} {3,S} {6,S}
2   R!H u0 {1,S} {4,D} {5,S}
3 * R!H u0 {1,S} {7,D}
4   R!H u0 {2,D} {8,S}
5   R!H u0 {2,S} {7,S}
6   R!H u0 {1,S} {8,S}
7   R!H u0 {3,D} {5,S}
8   R!H u0 {4,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-35.4021,-32.6164,-28.914,-25.3201,-18.9664,-14.1865,-8.53448],'J/(mol*K)'),
        H298 = (90.1575,'kJ/mol'),
        S298 = (215.235,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_5_diene_0_5 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 89,
    label = "s2_5_5_diene_0_6",
    group = 
"""
1   R!H u0 {2,S} {4,S} {6,S}
2   R!H u0 {1,S} {3,S} {5,D}
3 * R!H u0 {2,S} {7,D}
4   R!H u0 {1,S} {8,S}
5   R!H u0 {2,D} {8,S}
6   R!H u0 {1,S} {7,S}
7   R!H u0 {3,D} {6,S}
8   R!H u0 {4,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-35.3767,-36.9132,-35.2885,-31.4991,-24.6371,-18.318,-11.578],'J/(mol*K)'),
        H298 = (94.0296,'kJ/mol'),
        S298 = (225.35,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_5_diene_0_6 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 90,
    label = "s2_5_5_diene_1_5",
    group = 
"""
1   R!H u0 {2,S} {3,S} {5,S}
2   R!H u0 {1,S} {4,S} {6,S}
3 * R!H u0 {1,S} {7,D}
4   R!H u0 {2,S} {8,D}
5   R!H u0 {1,S} {8,S}
6   R!H u0 {2,S} {7,S}
7   R!H u0 {3,D} {6,S}
8   R!H u0 {4,D} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-28.5408,-28.8784,-27.579,-24.3002,-19.7766,-14.6598,-9.82684],'J/(mol*K)'),
        H298 = (65.5921,'kJ/mol'),
        S298 = (213.858,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_5_diene_1_5 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 91,
    label = "s2_5_5_diene_1_6",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S}
2   R!H u0 {1,S} {5,S} {6,S}
3 * R!H u0 {1,S} {7,D}
4   R!H u0 {1,S} {8,D}
5   R!H u0 {2,S} {7,S}
6   R!H u0 {2,S} {8,S}
7   R!H u0 {3,D} {5,S}
8   R!H u0 {4,D} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-34.3528,-31.4209,-27.8175,-24.5448,-18.7812,-13.7652,-9.05624],'J/(mol*K)'),
        H298 = (70.8954,'kJ/mol'),
        S298 = (222.397,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_5_diene_1_6 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s2_5_5_tetraene",
    group = "OR{s2_5_5_tetraene_0_2_4_6}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 84,
    label = "s2_5_5_tetraene_0_2_4_6",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,D}
2   R!H u0 {1,S} {5,D} {6,S}
3 * R!H u0 {1,S} {8,D}
4   R!H u0 {1,D} {7,S}
5   R!H u0 {2,D} {8,S}
6   R!H u0 {2,S} {7,D}
7   R!H u0 {4,S} {6,D}
8   R!H u0 {3,D} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-21.677,-25.8011,-27.002,-27.3347,-26.4292,-23.2292,-24.6771],'J/(mol*K)'),
        H298 = (135.898,'kJ/mol'),
        S298 = (289.394,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_5_tetraene_0_2_4_6 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s2_5_6",
    group = 
"""
1 * R!H u0 {2,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {6,[S,D,T,B]}
3   R!H u0 {2,[S,D,T,B]} {9,[S,D,T,B]}
4   R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
7   R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
8   R!H u0 {4,[S,D,T,B]} {9,[S,D,T,B]}
9   R!H u0 {3,[S,D,T,B]} {8,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 92,
    label = "s2_5_6_ane",
    group = 
"""
1 * R!H u0 {2,S} {4,S} {5,S}
2   R!H u0 {1,S} {3,S} {6,S}
3   R!H u0 {2,S} {9,S}
4   R!H u0 {1,S} {8,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {2,S} {7,S}
7   R!H u0 {5,S} {6,S}
8   R!H u0 {4,S} {9,S}
9   R!H u0 {3,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-45.4257,-43.1666,-39.5136,-34.3712,-23.6742,-14.7923,-5.00656],'J/(mol*K)'),
        H298 = (62.1536,'kJ/mol'),
        S298 = (191.783,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_6_ane from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s2_5_6_ene",
    group = "OR{s2_5_6_ene_0, s2_5_6_ene_1, s2_5_6_ene_m, s2_5_6_ene_2, s2_5_6_ene_5, s2_5_6_ene_6}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 93,
    label = "s2_5_6_ene_0",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {5,S}
2   R!H u0 {1,S} {4,D} {6,S}
3   R!H u0 {1,S} {7,S}
4   R!H u0 {2,D} {8,S}
5   R!H u0 {1,S} {9,S}
6   R!H u0 {2,S} {7,S}
7   R!H u0 {3,S} {6,S}
8   R!H u0 {4,S} {9,S}
9   R!H u0 {5,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-39.2214,-38.2609,-35.9235,-31.2167,-22.2379,-14.6334,-5.90732],'J/(mol*K)'),
        H298 = (56.657,'kJ/mol'),
        S298 = (190.173,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_6_ene_0 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 94,
    label = "s2_5_6_ene_1",
    group = 
"""
1 * R!H u0 {2,S} {4,S} {6,S}
2   R!H u0 {1,S} {3,S} {5,S}
3   R!H u0 {2,S} {8,D}
4   R!H u0 {1,S} {7,S}
5   R!H u0 {2,S} {7,S}
6   R!H u0 {1,S} {9,S}
7   R!H u0 {4,S} {5,S}
8   R!H u0 {3,D} {9,S}
9   R!H u0 {6,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-38.9638,-37.7409,-35.1268,-30.7369,-22.2439,-14.5863,-6.4012],'J/(mol*K)'),
        H298 = (62.9293,'kJ/mol'),
        S298 = (193.573,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_6_ene_1 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 95,
    label = "s2_5_6_ene_m",
    group = 
"""
1 * R!H u0 {2,D} {5,S} {6,S}
2   R!H u0 {1,D} {3,S} {4,S}
3   R!H u0 {2,S} {8,S}
4   R!H u0 {2,S} {7,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {1,S} {9,S}
7   R!H u0 {4,S} {5,S}
8   R!H u0 {3,S} {9,S}
9   R!H u0 {6,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-40.1771,-39.8658,-37.3698,-32.7555,-23.303,-15.5544,-5.64344],'J/(mol*K)'),
        H298 = (50.6094,'kJ/mol'),
        S298 = (188.699,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_6_ene_m from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 96,
    label = "s2_5_6_ene_2",
    group = 
"""
1 * R!H u0 {2,S} {5,S} {6,S}
2   R!H u0 {1,S} {3,S} {4,S}
3   R!H u0 {2,S} {7,S}
4   R!H u0 {2,S} {8,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {1,S} {9,S}
7   R!H u0 {3,S} {5,S}
8   R!H u0 {4,S} {9,D}
9   R!H u0 {6,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-39.3458,-37.6139,-34.2104,-30.2029,-21.8979,-14.3743,-6.3532],'J/(mol*K)'),
        H298 = (71.772,'kJ/mol'),
        S298 = (190.136,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_6_ene_2 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 97,
    label = "s2_5_6_ene_5",
    group = 
"""
1 * R!H u0 {2,S} {3,D} {6,S}
2   R!H u0 {1,S} {4,S} {5,S}
3   R!H u0 {1,D} {7,S}
4   R!H u0 {2,S} {9,S}
5   R!H u0 {2,S} {7,S}
6   R!H u0 {1,S} {8,S}
7   R!H u0 {3,S} {5,S}
8   R!H u0 {6,S} {9,S}
9   R!H u0 {4,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-38.5174,-38.0049,-35.9905,-31.2567,-22.2409,-14.6394,-5.97532],'J/(mol*K)'),
        H298 = (74.4929,'kJ/mol'),
        S298 = (191.696,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_6_ene_5 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 98,
    label = "s2_5_6_ene_6",
    group = 
"""
1 * R!H u0 {2,S} {4,S} {6,S}
2   R!H u0 {1,S} {3,S} {5,S}
3   R!H u0 {2,S} {8,S}
4   R!H u0 {1,S} {7,S}
5   R!H u0 {2,S} {7,D}
6   R!H u0 {1,S} {9,S}
7   R!H u0 {4,S} {5,D}
8   R!H u0 {3,S} {9,S}
9   R!H u0 {6,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-38.4628,-37.1559,-34.5418,-30.1859,-21.7599,-14.1703,-6.1302],'J/(mol*K)'),
        H298 = (72.3374,'kJ/mol'),
        S298 = (192.941,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_6_ene_6 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s2_5_6_diene",
    group = "OR{s2_5_6_diene_m_1, s2_5_6_diene_m_2, s2_5_6_diene_m_7, s2_5_6_diene_0_2, s2_5_6_diene_0_3, s2_5_6_diene_0_4, s2_5_6_diene_0_5, s2_5_6_diene_0_6, s2_5_6_diene_0_7, s2_5_6_diene_1_3, s2_5_6_diene_1_5, s2_5_6_diene_1_6, s2_5_6_diene_1_7, s2_5_6_diene_1_8, s2_5_6_diene_2_5, s2_5_6_diene_2_6, s2_5_6_diene_5_7, s2_5_6_diene_5_8}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 99,
    label = "s2_5_6_diene_m_1",
    group = 
"""
1 * R!H u0 {2,D} {4,S} {6,S}
2   R!H u0 {1,D} {3,S} {5,S}
3   R!H u0 {2,S} {8,D}
4   R!H u0 {1,S} {7,S}
5   R!H u0 {2,S} {7,S}
6   R!H u0 {1,S} {9,S}
7   R!H u0 {4,S} {5,S}
8   R!H u0 {3,D} {9,S}
9   R!H u0 {6,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-37.8264,-40.67,-39.3488,-34.8713,-25.392,-17.7936,-9.05308],'J/(mol*K)'),
        H298 = (64.8989,'kJ/mol'),
        S298 = (210.302,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_6_diene_m_1 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 100,
    label = "s2_5_6_diene_m_2",
    group = 
"""
1 * R!H u0 {2,D} {3,S} {6,S}
2   R!H u0 {1,D} {4,S} {5,S}
3   R!H u0 {1,S} {9,S}
4   R!H u0 {2,S} {8,S}
5   R!H u0 {2,S} {7,S}
6   R!H u0 {1,S} {7,S}
7   R!H u0 {5,S} {6,S}
8   R!H u0 {4,S} {9,D}
9   R!H u0 {3,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-32.3004,-34.4352,-32.8344,-28.7852,-20.8258,-14.759,-6.48532],'J/(mol*K)'),
        H298 = (42.7943,'kJ/mol'),
        S298 = (193.491,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_6_diene_m_2 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 101,
    label = "s2_5_6_diene_m_7",
    group = 
"""
1 * R!H u0 {2,D} {3,S} {5,S}
2   R!H u0 {1,D} {4,S} {6,S}
3   R!H u0 {1,S} {8,S}
4   R!H u0 {2,S} {7,S}
5   R!H u0 {1,S} {7,D}
6   R!H u0 {2,S} {9,S}
7   R!H u0 {4,S} {5,D}
8   R!H u0 {3,S} {9,S}
9   R!H u0 {6,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-38.629,-40.3085,-38.2637,-33.8928,-24.6281,-17.3259,-8.3302],'J/(mol*K)'),
        H298 = (51.5473,'kJ/mol'),
        S298 = (204.962,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_6_diene_m_7 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 102,
    label = "s2_5_6_diene_0_2",
    group = 
"""
1 * R!H u0 {2,S} {4,S} {6,D}
2   R!H u0 {1,S} {3,S} {5,S}
3   R!H u0 {2,S} {7,S}
4   R!H u0 {1,S} {7,S}
5   R!H u0 {2,S} {9,S}
6   R!H u0 {1,D} {8,S}
7   R!H u0 {3,S} {4,S}
8   R!H u0 {6,S} {9,D}
9   R!H u0 {5,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-38.1067,-39.288,-37.6375,-33.3805,-24.832,-17.3106,-9.09196],'J/(mol*K)'),
        H298 = (65.0161,'kJ/mol'),
        S298 = (206.507,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_6_diene_0_2 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 103,
    label = "s2_5_6_diene_0_3",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {6,S}
2   R!H u0 {1,S} {4,D} {5,S}
3   R!H u0 {1,S} {8,D}
4   R!H u0 {2,D} {9,S}
5   R!H u0 {2,S} {7,S}
6   R!H u0 {1,S} {7,S}
7   R!H u0 {5,S} {6,S}
8   R!H u0 {3,D} {9,S}
9   R!H u0 {4,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-37.6961,-35.2802,-32.024,-27.9105,-19.5952,-13.4391,-6.14448],'J/(mol*K)'),
        H298 = (55.6806,'kJ/mol'),
        S298 = (204.632,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_6_diene_0_3 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 104,
    label = "s2_5_6_diene_0_4",
    group = 
"""
1 * R!H u0 {2,S} {4,D} {5,S}
2   R!H u0 {1,S} {3,D} {6,S}
3   R!H u0 {2,D} {9,S}
4   R!H u0 {1,D} {8,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {2,S} {7,S}
7   R!H u0 {5,S} {6,S}
8   R!H u0 {4,S} {9,S}
9   R!H u0 {3,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-38.3034,-40.053,-38.4158,-34.2833,-25.205,-17.6956,-8.86208],'J/(mol*K)'),
        H298 = (66.4995,'kJ/mol'),
        S298 = (207.57,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_6_diene_0_4 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 105,
    label = "s2_5_6_diene_0_5",
    group = 
"""
1 * R!H u0 {2,S} {4,S} {5,D}
2   R!H u0 {1,S} {3,D} {6,S}
3   R!H u0 {2,D} {8,S}
4   R!H u0 {1,S} {9,S}
5   R!H u0 {1,D} {7,S}
6   R!H u0 {2,S} {7,S}
7   R!H u0 {5,S} {6,S}
8   R!H u0 {3,S} {9,S}
9   R!H u0 {4,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-38.7904,-40.956,-39.4838,-35.1923,-25.819,-18.1126,-9.06408],'J/(mol*K)'),
        H298 = (53.2024,'kJ/mol'),
        S298 = (211.109,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_6_diene_0_5 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 106,
    label = "s2_5_6_diene_0_6",
    group = 
"""
1 * R!H u0 {2,S} {4,S} {6,S}
2   R!H u0 {1,S} {3,D} {5,S}
3   R!H u0 {2,D} {9,S}
4   R!H u0 {1,S} {8,S}
5   R!H u0 {2,S} {7,S}
6   R!H u0 {1,S} {7,D}
7   R!H u0 {5,S} {6,D}
8   R!H u0 {4,S} {9,S}
9   R!H u0 {3,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-38.8671,-35.6932,-31.843,-27.6605,-19.4782,-13.3821,-6.07848],'J/(mol*K)'),
        H298 = (57.4666,'kJ/mol'),
        S298 = (196.684,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_6_diene_0_6 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 107,
    label = "s2_5_6_diene_0_7",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {6,S}
2   R!H u0 {1,S} {4,S} {5,D}
3   R!H u0 {1,S} {7,S}
4   R!H u0 {2,S} {7,D}
5   R!H u0 {2,D} {8,S}
6   R!H u0 {1,S} {9,S}
7   R!H u0 {3,S} {4,D}
8   R!H u0 {5,S} {9,S}
9   R!H u0 {6,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-38.6977,-39.934,-38.2265,-33.8805,-25.189,-17.5506,-9.15296],'J/(mol*K)'),
        H298 = (59.0127,'kJ/mol'),
        S298 = (207.242,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_6_diene_0_7 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 108,
    label = "s2_5_6_diene_1_3",
    group = 
"""
1 * R!H u0 {2,S} {5,S} {6,S}
2   R!H u0 {1,S} {3,S} {4,S}
3   R!H u0 {2,S} {9,D}
4   R!H u0 {2,S} {7,S}
5   R!H u0 {1,S} {8,D}
6   R!H u0 {1,S} {7,S}
7   R!H u0 {4,S} {6,S}
8   R!H u0 {5,D} {9,S}
9   R!H u0 {3,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-37.026,-38.605,-37.5762,-33.1727,-24.9369,-17.2835,-9.61384],'J/(mol*K)'),
        H298 = (70.9548,'kJ/mol'),
        S298 = (222.284,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_6_diene_1_3 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 109,
    label = "s2_5_6_diene_1_5",
    group = 
"""
1 * R!H u0 {2,S} {4,S} {5,S}
2   R!H u0 {1,S} {3,D} {6,S}
3   R!H u0 {2,D} {7,S}
4   R!H u0 {1,S} {9,D}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {2,S} {8,S}
7   R!H u0 {3,S} {5,S}
8   R!H u0 {6,S} {9,S}
9   R!H u0 {4,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-37.4345,-34.5147,-31.2592,-27.367,-19.3641,-13.1188,-6.23436],'J/(mol*K)'),
        H298 = (69.3468,'kJ/mol'),
        S298 = (201.962,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_6_diene_1_5 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 110,
    label = "s2_5_6_diene_1_6",
    group = 
"""
1 * R!H u0 {2,S} {4,S} {6,S}
2   R!H u0 {1,S} {3,S} {5,S}
3   R!H u0 {2,S} {7,S}
4   R!H u0 {1,S} {7,D}
5   R!H u0 {2,S} {8,D}
6   R!H u0 {1,S} {9,S}
7   R!H u0 {3,S} {4,D}
8   R!H u0 {5,D} {9,S}
9   R!H u0 {6,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-31.5058,-31.2702,-29.863,-26.2216,-20.0285,-13.6933,-7.29984],'J/(mol*K)'),
        H298 = (55.7592,'kJ/mol'),
        S298 = (193.829,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_6_diene_1_6 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 111,
    label = "s2_5_6_diene_1_7",
    group = 
"""
1 * R!H u0 {2,S} {4,S} {5,S}
2   R!H u0 {1,S} {3,S} {6,S}
3   R!H u0 {2,S} {8,S}
4   R!H u0 {1,S} {9,D}
5   R!H u0 {1,S} {7,D}
6   R!H u0 {2,S} {7,S}
7   R!H u0 {5,D} {6,S}
8   R!H u0 {3,S} {9,S}
9   R!H u0 {4,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-38.0238,-34.4577,-30.6305,-26.9062,-19.4011,-13.0957,-6.69124],'J/(mol*K)'),
        H298 = (59.3536,'kJ/mol'),
        S298 = (201.065,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_6_diene_1_7 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 112,
    label = "s2_5_6_diene_1_8",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {6,S}
2   R!H u0 {1,S} {4,D} {5,S}
3   R!H u0 {1,S} {7,S}
4   R!H u0 {2,D} {7,S}
5   R!H u0 {2,S} {8,D}
6   R!H u0 {1,S} {9,S}
7   R!H u0 {3,S} {4,S}
8   R!H u0 {5,D} {9,S}
9   R!H u0 {6,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8,-7.6,-6.8,-5.7,-4.3,-3.3,-2.1],'cal/(mol*K)'),
        H298 = (10.1,'kcal/mol'),
        S298 = (45.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Copied from entry: 2.3.3a.7a-tetrahydro-1H-indene
""",
)

entry(
    index = 113,
    label = "s2_5_6_diene_2_5",
    group = 
"""
1 * R!H u0 {2,S} {5,S} {6,S}
2   R!H u0 {1,S} {3,S} {4,D}
3   R!H u0 {2,S} {9,S}
4   R!H u0 {2,D} {7,S}
5   R!H u0 {1,S} {8,S}
6   R!H u0 {1,S} {7,S}
7   R!H u0 {4,S} {6,S}
8   R!H u0 {5,S} {9,D}
9   R!H u0 {3,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-31.0551,-32.1807,-31.0592,-27.3609,-20.2177,-13.9547,-6.64408],'J/(mol*K)'),
        H298 = (56.3662,'kJ/mol'),
        S298 = (198.571,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_6_diene_2_5 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 114,
    label = "s2_5_6_diene_2_6",
    group = 
"""
1 * R!H u0 {2,S} {4,S} {5,S}
2   R!H u0 {1,S} {3,S} {6,S}
3   R!H u0 {2,S} {8,S}
4   R!H u0 {1,S} {7,S}
5   R!H u0 {1,S} {9,S}
6   R!H u0 {2,S} {7,D}
7   R!H u0 {4,S} {6,D}
8   R!H u0 {3,S} {9,D}
9   R!H u0 {5,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-31.8178,-31.2752,-29.2986,-26.0706,-19.9045,-13.5623,-7.10184],'J/(mol*K)'),
        H298 = (65.0092,'kJ/mol'),
        S298 = (191.089,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_6_diene_2_6 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 115,
    label = "s2_5_6_diene_5_7",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {4,S}
2   R!H u0 {1,S} {5,S} {6,D}
3   R!H u0 {1,S} {7,D}
4   R!H u0 {1,S} {9,S}
5   R!H u0 {2,S} {8,S}
6   R!H u0 {2,D} {7,S}
7   R!H u0 {3,D} {6,S}
8   R!H u0 {5,S} {9,S}
9   R!H u0 {4,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-45.5487,-42.9525,-38.8744,-33.9631,-24.0885,-16.616,-8.47836],'J/(mol*K)'),
        H298 = (56.3114,'kJ/mol'),
        S298 = (210.982,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_6_diene_5_7 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 116,
    label = "s2_5_6_diene_5_8",
    group = 
"""
1 * R!H u0 {2,S} {3,D} {5,S}
2   R!H u0 {1,S} {4,D} {6,S}
3   R!H u0 {1,D} {7,S}
4   R!H u0 {2,D} {7,S}
5   R!H u0 {1,S} {9,S}
6   R!H u0 {2,S} {8,S}
7   R!H u0 {3,S} {4,S}
8   R!H u0 {6,S} {9,S}
9   R!H u0 {5,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-38.594,-40.0215,-37.8257,-33.4848,-24.3491,-17.1569,-8.3362],'J/(mol*K)'),
        H298 = (56.0623,'kJ/mol'),
        S298 = (201.108,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_6_diene_5_8 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s2_5_6_triene",
    group = "OR{s2_5_6_triene_0_2_6, s2_5_6_triene_0_2_7, s2_5_6_triene_0_3_7, s2_5_6_triene_1_3_5, s2_5_6_triene_1_3_6, s2_5_6_triene_1_6_8, s2_5_6_triene_2_5_7, s2_5_6_triene_m_1_7, s2_5_6_triene_m_2_6}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 99,
    label = "s2_5_6_triene_0_2_6",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {6,D}
2   R!H u0 {1,S} {4,S} {5,S}
3   R!H u0 {1,S} {7,S}
4   R!H u0 {2,S} {8,S}
5   R!H u0 {2,S} {7,D}
6   R!H u0 {1,D} {9,S}
7   R!H u0 {3,S} {5,D}
8   R!H u0 {4,S} {9,D}
9   R!H u0 {6,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.68,-6.81,-6.56,-5.84,-4.8,-3.99,-3.4],'cal/(mol*K)'),
        H298 = (6.863,'kcal/mol'),
        S298 = (57.6932,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt21 from C10H11 library.
""",
)

entry(
    index = 99,
    label = "s2_5_6_triene_0_2_7",
    group = 
"""
1 * R!H u0 {2,S} {4,S} {5,S}
2   R!H u0 {1,S} {3,D} {6,S}
3   R!H u0 {2,D} {8,S}
4   R!H u0 {1,S} {9,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {2,S} {7,D}
7   R!H u0 {5,S} {6,D}
8   R!H u0 {3,S} {9,D}
9   R!H u0 {4,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.07,-7.77333,-7.70333,-6.73333,-5.47333,-4.32333,-2.97333],'cal/(mol*K)','+|-',[3.26137,4.03866,3.95722,3.57416,2.7068,2.08753,1.35534]),
        H298 = (2.643,'kcal/mol','+|-',4.3516),
        S298 = (60.4632,'cal/(mol*K)','+|-',1.24756),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt21 from C10H11 library.
Fitted from species pdt27 from C10H11 library.
Fitted from species pdt32 from C10H11 library.
""",
)

entry(
    index = 99,
    label = "s2_5_6_triene_0_3_7",
    group = 
"""
1 * R!H u0 {2,S} {4,D} {5,S}
2   R!H u0 {1,S} {3,S} {6,S}
3   R!H u0 {2,S} {7,S}
4   R!H u0 {1,D} {8,S}
5   R!H u0 {1,S} {7,D}
6   R!H u0 {2,S} {9,D}
7   R!H u0 {3,S} {5,D}
8   R!H u0 {4,S} {9,S}
9   R!H u0 {6,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.91,-7.09,-6.83,-6.08,-4.95,-4.08,-3.42],'cal/(mol*K)'),
        H298 = (5.483,'kcal/mol'),
        S298 = (58.2132,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt32 from C10H11 library.
""",
)

entry(
    index = 99,
    label = "s2_5_6_triene_1_3_5",
    group = 
"""
1 * R!H u0 {2,S} {4,S} {6,S}
2   R!H u0 {1,S} {3,D} {5,S}
3   R!H u0 {2,D} {7,S}
4   R!H u0 {1,S} {7,S}
5   R!H u0 {2,S} {9,D}
6   R!H u0 {1,S} {8,D}
7   R!H u0 {3,S} {4,S}
8   R!H u0 {6,D} {9,S}
9   R!H u0 {5,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.9,-8.9,-8.26,-7.24,-5.57,-4.36,-2.74],'cal/(mol*K)'),
        H298 = (3.693,'kcal/mol'),
        S298 = (61.9332,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt32 from C10H11 library.
""",
)

entry(
    index = 99,
    label = "s2_5_6_triene_1_3_6",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {6,S}
2   R!H u0 {1,S} {4,S} {5,S}
3   R!H u0 {1,S} {7,S}
4   R!H u0 {2,S} {8,D}
5   R!H u0 {2,S} {7,D}
6   R!H u0 {1,S} {9,D}
7   R!H u0 {3,S} {5,D}
8   R!H u0 {4,D} {9,S}
9   R!H u0 {6,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.78,-6.1,-4.92,-3.65,-2.41,-1.62,-0.77],'cal/(mol*K)'),
        H298 = (-15.727,'kcal/mol'),
        S298 = (49.8332,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt32 from C10H11 library.
""",
)

entry(
    index = 99,
    label = "s2_5_6_triene_1_6_8",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {5,S}
2   R!H u0 {1,S} {4,D} {6,S}
3   R!H u0 {1,S} {8,S}
4   R!H u0 {2,D} {7,S}
5   R!H u0 {1,S} {7,D}
6   R!H u0 {2,S} {9,D}
7   R!H u0 {4,S} {5,D}
8   R!H u0 {3,S} {9,S}
9   R!H u0 {6,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.67,-8.62,-7.99,-7,-5.42,-4.27,-2.72],'cal/(mol*K)'),
        H298 = (2.023,'kcal/mol'),
        S298 = (61.7232,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt21 from C10H11 library.
""",
)

entry(
    index = 99,
    label = "s2_5_6_triene_2_5_7",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {4,S}
2   R!H u0 {1,S} {5,D} {6,S}
3   R!H u0 {1,S} {9,S}
4   R!H u0 {1,S} {7,D}
5   R!H u0 {2,D} {7,S}
6   R!H u0 {2,S} {8,S}
7   R!H u0 {4,D} {5,S}
8   R!H u0 {6,S} {9,D}
9   R!H u0 {3,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.68,-6.81,-6.56,-5.84,-4.8,-3.99,-3.4],'cal/(mol*K)'),
        H298 = (6.863,'kcal/mol'),
        S298 = (57.6932,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt21 from C10H11 library.
""",
)

entry(
    index = 99,
    label = "s2_5_6_triene_m_1_7",
    group = 
"""
1 * R!H u0 {2,D} {3,S} {6,S}
2   R!H u0 {1,D} {4,S} {5,S}
3   R!H u0 {1,S} {9,D}
4   R!H u0 {2,S} {8,S}
5   R!H u0 {2,S} {7,S}
6   R!H u0 {1,S} {7,D}
7   R!H u0 {5,S} {6,D}
8   R!H u0 {4,S} {9,S}
9   R!H u0 {3,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.57,-4.83,-4.71,-4.26,-4,-3.54,-3.01],'cal/(mol*K)'),
        H298 = (-2.777,'kcal/mol'),
        S298 = (59.5532,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt27 from C10H11 library.
""",
)

entry(
    index = 99,
    label = "s2_5_6_triene_m_2_6",
    group = 
"""
1 * R!H u0 {2,D} {3,S} {5,S}
2   R!H u0 {1,D} {4,S} {6,S}
3   R!H u0 {1,S} {7,D}
4   R!H u0 {2,S} {8,S}
5   R!H u0 {1,S} {9,S}
6   R!H u0 {2,S} {7,S}
7   R!H u0 {3,D} {6,S}
8   R!H u0 {4,S} {9,D}
9   R!H u0 {5,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.88,-7.18,-6.81,-6.07,-4.85,-4.06,-3.25],'cal/(mol*K)'),
        H298 = (6.883,'kcal/mol'),
        S298 = (58.0732,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt27 from C10H11 library.
""",
)

entry(
    index = 0,
    label = "s2_5_6_tetraene",
    group = "OR{s2_5_6_tetraene_1_3_5_7, s2_5_6_tetraene_1_3_5_8}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 99,
    label = "s2_5_6_tetraene_1_3_5_7",
    group = 
"""
1 * R!H u0 {2,S} {4,S} {5,D}
2   R!H u0 {1,S} {3,S} {6,S}
3   R!H u0 {2,S} {8,D}
4   R!H u0 {1,S} {9,D}
5   R!H u0 {1,D} {7,S}
6   R!H u0 {2,S} {7,D}
7   R!H u0 {5,S} {6,D}
8   R!H u0 {3,D} {9,S}
9   R!H u0 {4,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.63,-9.81,-9.04,-7.82,-5.95,-4.71,-3.23],'cal/(mol*K)'),
        H298 = (14.05,'kcal/mol'),
        S298 = (60.39,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt22 from C10H11 library.
""",
)

entry(
    index = 99,
    label = "s2_5_6_tetraene_1_3_5_8",
    group = 
"""
1 * R!H u0 {2,S} {5,S} {6,D}
2   R!H u0 {1,S} {3,S} {4,D}
3   R!H u0 {2,S} {8,D}
4   R!H u0 {2,D} {7,S}
5   R!H u0 {1,S} {9,D}
6   R!H u0 {1,D} {7,S}
7   R!H u0 {4,S} {6,S}
8   R!H u0 {3,D} {9,S}
9   R!H u0 {5,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.49,-4.75,-4.62,-4.45,-4.55,-4.28,-4.48],'cal/(mol*K)'),
        H298 = (-0.61,'kcal/mol'),
        S298 = (58.88,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species 2HINDENE from C10H11 library.
""",
)

entry(
    index = 184,
    label = "s2_5_6_ben",
    group = 
"""
1 * R!H u0 {2,B} {3,S} {5,B}
2   R!H u0 {1,B} {4,S} {6,B}
3   R!H u0 {1,S} {7,S}
4   R!H u0 {2,S} {7,S}
5   R!H u0 {1,B} {9,B}
6   R!H u0 {2,B} {8,B}
7   R!H u0 {3,S} {4,S}
8   R!H u0 {6,B} {9,B}
9   R!H u0 {5,B} {8,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-18.9363,-17.9366,-16.3584,-14.6161,-10.2889,-6.03196,0.7134],'J/(mol*K)'),
        H298 = (37.0186,'kJ/mol'),
        S298 = (96.7074,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_6_ben from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 117,
    label = "s2_5_6_indene",
    group =
"""
1 * R!H u0 {2,B} {3,S} {4,B}
2   R!H u0 {1,B} {5,S} {6,B}
3   R!H u0 {1,S} {7,S}
4   R!H u0 {1,B} {8,B}
5   R!H u0 {2,S} {7,D}
6   R!H u0 {2,B} {9,B}
7   R!H u0 {3,S} {5,D}
8   R!H u0 {4,B} {9,B}
9   R!H u0 {6,B} {8,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.88,-4.29,-3.89,-2.96,-1.83,-2.2,-1.31],'cal/(mol*K)'),
        H298 = (2.1,'kcal/mol'),
        S298 = (33.08,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
Verevkin (2011), experimental, S and cp from PM7
""",
)

entry(
    index = 0,
    label = "s2_5_7",
    group = 
"""
1  * R!H u0 {2,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2    R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {6,[S,D,T,B]}
3    R!H u0 {2,[S,D,T,B]} {9,[S,D,T,B]}
4    R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
5    R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6    R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
8    R!H u0 {4,[S,D,T,B]} {10,[S,D,T,B]}
9    R!H u0 {3,[S,D,T,B]} {10,[S,D,T,B]}
10   R!H u0 {8,[S,D,T,B]} {9,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 0,
    label = "s2_5_7_triene",
    group = "OR{s2_5_7_triene_0_2_8, s2_5_7_triene_0_3_8, s2_5_7_triene_1_3_7, s2_5_7_triene_1_3_8, s2_5_7_triene_1_3_9, s2_5_7_triene_1_4_7}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 118,
    label = "s2_5_7_triene_0_2_8",
    group = 
"""
1  * R!H u0 {2,S} {4,D} {6,S}
2    R!H u0 {1,S} {3,S} {5,S}
3    R!H u0 {2,S} {7,S}
4    R!H u0 {1,D} {8,S}
5    R!H u0 {2,S} {9,S}
6    R!H u0 {1,S} {7,D}
7    R!H u0 {3,S} {6,D}
8    R!H u0 {4,S} {10,D}
9    R!H u0 {5,S} {10,S}
10   R!H u0 {8,D} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.56,-9.04,-8.6,-7.5,-5.91,-4.62,-2.75],'cal/(mol*K)'),
        H298 = (0.693,'kcal/mol'),
        S298 = (56.96,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt29 from C10H11 library.
""",
)

entry(
    index = 118,
    label = "s2_5_7_triene_0_3_8",
    group = 
"""
1  * R!H u0 {2,S} {5,S} {6,S}
2    R!H u0 {1,S} {3,D} {4,S}
3    R!H u0 {2,D} {8,S}
4    R!H u0 {2,S} {7,D}
5    R!H u0 {1,S} {9,S}
6    R!H u0 {1,S} {7,S}
7    R!H u0 {4,D} {6,S}
8    R!H u0 {3,S} {10,S}
9    R!H u0 {5,S} {10,D}
10   R!H u0 {8,S} {9,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.57,-7.23,-7.07,-6.34,-5.29,-4.34,-3.43],'cal/(mol*K)'),
        H298 = (6.033,'kcal/mol'),
        S298 = (53.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt29 from C10H11 library.
""",
)

entry(
    index = 118,
    label = "s2_5_7_triene_1_3_7",
    group = 
"""
1  * R!H u0 {2,S} {3,S} {4,S}
2    R!H u0 {1,S} {5,S} {6,S}
3    R!H u0 {1,S} {7,D}
4    R!H u0 {1,S} {9,S}
5    R!H u0 {2,S} {7,S}
6    R!H u0 {2,S} {8,D}
7    R!H u0 {3,D} {5,S}
8    R!H u0 {6,D} {10,S}
9    R!H u0 {4,S} {10,D}
10   R!H u0 {8,S} {9,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.535,-6.635,-6.36,-5.495,-4.605,-3.68,-2.31],'cal/(mol*K)','+|-',[3.13605,3.13605,2.84019,2.426,1.71595,1.18341,0.473366]),
        H298 = (13.728,'kcal/mol','+|-',10.9884),
        S298 = (54.235,'cal/(mol*K)','+|-',0.296985),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt8 from C10H11 library.
Fitted from species pdt23 from C10H11 library.
""",
)

entry(
    index = 118,
    label = "s2_5_7_triene_1_3_8",
    group = 
"""
1  * R!H u0 {2,S} {3,S} {6,S}
2    R!H u0 {1,S} {4,S} {5,S}
3    R!H u0 {1,S} {7,D}
4    R!H u0 {2,S} {9,S}
5    R!H u0 {2,S} {7,S}
6    R!H u0 {1,S} {8,D}
7    R!H u0 {3,D} {5,S}
8    R!H u0 {6,D} {10,S}
9    R!H u0 {4,S} {10,D}
10   R!H u0 {8,S} {9,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.3425,-7.0575,-5.85,-4.7975,-3.47,-2.58,-1.35],'cal/(mol*K)','+|-',[4.00405,3.66182,6.7465,8.34184,9.49513,9.23012,7.85553]),
        H298 = (6.758,'kcal/mol','+|-',29.8859),
        S298 = (51.8325,'cal/(mol*K)','+|-',9.6992),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt8 from C10H11 library.
Fitted from species pdt23 from C10H11 library.
Fitted from species pdt28 from C10H11 library.
Fitted from species pdt29 from C10H11 library.
""",
)

entry(
    index = 118,
    label = "s2_5_7_triene_1_3_9",
    group = 
"""
1  * R!H u0 {2,S} {3,S} {6,S}
2    R!H u0 {1,S} {4,S} {5,D}
3    R!H u0 {1,S} {8,S}
4    R!H u0 {2,S} {9,D}
5    R!H u0 {2,D} {7,S}
6    R!H u0 {1,S} {7,S}
7    R!H u0 {5,S} {6,S}
8    R!H u0 {3,S} {10,D}
9    R!H u0 {4,D} {10,S}
10   R!H u0 {8,D} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.56,-9.04,-8.6,-7.5,-5.91,-4.62,-2.75],'cal/(mol*K)'),
        H298 = (3.993,'kcal/mol'),
        S298 = (56.96,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt29 from C10H11 library.
""",
)

entry(
    index = 118,
    label = "s2_5_7_triene_1_4_7",
    group = 
"""
1  * R!H u0 {2,S} {4,S} {6,S}
2    R!H u0 {1,S} {3,S} {5,S}
3    R!H u0 {2,S} {7,S}
4    R!H u0 {1,S} {7,D}
5    R!H u0 {2,S} {8,D}
6    R!H u0 {1,S} {9,D}
7    R!H u0 {3,S} {4,D}
8    R!H u0 {5,D} {10,S}
9    R!H u0 {6,D} {10,S}
10   R!H u0 {8,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.31,-5.81,-5.33,-4.69,-3.97,-3.35,-2.88],'cal/(mol*K)'),
        H298 = (14.973,'kcal/mol'),
        S298 = (52.13,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt8 from C10H11 library.
""",
)

entry(
    index = 0,
    label = "s2_5_7_tetraene",
    group = "OR{s2_5_7_tetraene_0_2_4_8, s2_5_7_tetraene_1_3_7_9, s2_5_7_tetraene_m_1_3_8}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 118,
    label = "s2_5_7_tetraene_0_2_4_8",
    group = 
"""
1  * R!H u0 {2,S} {4,S} {6,S}
2    R!H u0 {1,S} {3,D} {5,S}
3    R!H u0 {2,D} {9,S}
4    R!H u0 {1,S} {8,D}
5    R!H u0 {2,S} {7,D}
6    R!H u0 {1,S} {7,S}
7    R!H u0 {5,D} {6,S}
8    R!H u0 {4,D} {10,S}
9    R!H u0 {3,S} {10,D}
10   R!H u0 {8,S} {9,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10.94,-11.19,-10.38,-8.99,-6.63,-5,-2.79],'cal/(mol*K)'),
        H298 = (11.73,'kcal/mol'),
        S298 = (57.98,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt31 from C10H11 library.
""",
)

entry(
    index = 118,
    label = "s2_5_7_tetraene_1_3_7_9",
    group = 
"""
1  * R!H u0 {2,S} {3,S} {5,S}
2    R!H u0 {1,S} {4,S} {6,D}
3    R!H u0 {1,S} {8,S}
4    R!H u0 {2,S} {9,D}
5    R!H u0 {1,S} {7,D}
6    R!H u0 {2,D} {7,S}
7    R!H u0 {5,D} {6,S}
8    R!H u0 {3,S} {10,D}
9    R!H u0 {4,D} {10,S}
10   R!H u0 {8,D} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10.84,-11.12,-10.33,-8.95,-6.62,-4.99,-2.8],'cal/(mol*K)'),
        H298 = (14.29,'kcal/mol'),
        S298 = (58.23,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt30 from C10H11 library.
""",
)

entry(
    index = 118,
    label = "s2_5_7_tetraene_m_1_3_8",
    group = 
"""
1  * R!H u0 {2,D} {3,S} {6,S}
2    R!H u0 {1,D} {4,S} {5,S}
3    R!H u0 {1,S} {8,S}
4    R!H u0 {2,S} {9,D}
5    R!H u0 {2,S} {7,D}
6    R!H u0 {1,S} {7,S}
7    R!H u0 {5,D} {6,S}
8    R!H u0 {3,S} {10,D}
9    R!H u0 {4,D} {10,S}
10   R!H u0 {8,D} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.52,-7.11,-6.7,-5.92,-4.93,-4.1,-2.95],'cal/(mol*K)'),
        H298 = (8.12,'kcal/mol'),
        S298 = (54.6,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt35 from C10H11 library.
""",
)

entry(
    index = 0,
    label = "s2_6_6",
    group = 
"""
1    R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {6,[S,D,T,B]}
2    R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3    R!H u0 {1,[S,D,T,B]} {9,[S,D,T,B]}
4    R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
5    R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
6    R!H u0 {1,[S,D,T,B]} {10,[S,D,T,B]}
7  * R!H u0 {4,[S,D,T,B]} {9,[S,D,T,B]}
8    R!H u0 {5,[S,D,T,B]} {10,[S,D,T,B]}
9    R!H u0 {3,[S,D,T,B]} {7,[S,D,T,B]}
10   R!H u0 {6,[S,D,T,B]} {8,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 118,
    label = "s2_6_6_ane",
    group = 
"""
1    R!H u0 {2,S} {3,S} {6,S}
2    R!H u0 {1,S} {4,S} {5,S}
3    R!H u0 {1,S} {9,S}
4    R!H u0 {2,S} {7,S}
5    R!H u0 {2,S} {8,S}
6    R!H u0 {1,S} {10,S}
7  * R!H u0 {4,S} {9,S}
8    R!H u0 {5,S} {10,S}
9    R!H u0 {3,S} {7,S}
10   R!H u0 {6,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-49.7767,-46.2154,-41.7236,-35.7646,-23.5151,-13.4829,-2.18756],'J/(mol*K)'),
        H298 = (32.3362,'kJ/mol'),
        S298 = (158.965,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_6_6_ane from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s2_6_6_ene",
    group = "OR{s2_6_6_ene_0, s2_6_6_ene_1, s2_6_6_ene_2, s2_6_6_ene_m}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 119,
    label = "s2_6_6_ene_0",
    group = 
"""
1    R!H u0 {2,S} {3,S} {5,S}
2    R!H u0 {1,S} {4,D} {6,S}
3    R!H u0 {1,S} {7,S}
4    R!H u0 {2,D} {8,S}
5    R!H u0 {1,S} {10,S}
6    R!H u0 {2,S} {9,S}
7  * R!H u0 {3,S} {8,S}
8    R!H u0 {4,S} {7,S}
9    R!H u0 {6,S} {10,S}
10   R!H u0 {5,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-44.2594,-42.4977,-39.4955,-33.7781,-22.9408,-13.9889,-3.53732],'J/(mol*K)'),
        H298 = (36.1393,'kJ/mol'),
        S298 = (166.332,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_6_6_ene_0 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 120,
    label = "s2_6_6_ene_1",
    group = 
"""
1    R!H u0 {2,S} {3,S} {5,S}
2    R!H u0 {1,S} {4,S} {6,S}
3    R!H u0 {1,S} {9,D}
4    R!H u0 {2,S} {7,S}
5    R!H u0 {1,S} {10,S}
6    R!H u0 {2,S} {8,S}
7  * R!H u0 {4,S} {10,S}
8    R!H u0 {6,S} {9,S}
9    R!H u0 {3,D} {8,S}
10   R!H u0 {5,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-42.9588,-40.6357,-37.4708,-32.3113,-22.1888,-13.3879,-3.8232],'J/(mol*K)'),
        H298 = (62.7273,'kJ/mol'),
        S298 = (169.342,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_6_6_ene_1 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 121,
    label = "s2_6_6_ene_2",
    group = 
"""
1    R!H u0 {2,S} {3,S} {4,S}
2    R!H u0 {1,S} {5,S} {6,S}
3    R!H u0 {1,S} {10,S}
4    R!H u0 {1,S} {7,S}
5    R!H u0 {2,S} {8,S}
6    R!H u0 {2,S} {9,S}
7  * R!H u0 {4,S} {8,S}
8    R!H u0 {5,S} {7,S}
9    R!H u0 {6,S} {10,D}
10   R!H u0 {3,S} {9,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-41.5288,-39.9877,-36.9724,-32.1913,-21.9528,-13.0719,-3.4222],'J/(mol*K)'),
        H298 = (34.7553,'kJ/mol'),
        S298 = (166.049,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_6_6_ene_2 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 122,
    label = "s2_6_6_ene_m",
    group = 
"""
1    R!H u0 {2,D} {5,S} {6,S}
2    R!H u0 {1,D} {3,S} {4,S}
3    R!H u0 {2,S} {7,S}
4    R!H u0 {2,S} {8,S}
5    R!H u0 {1,S} {10,S}
6    R!H u0 {1,S} {9,S}
7  * R!H u0 {3,S} {9,S}
8    R!H u0 {4,S} {10,S}
9    R!H u0 {6,S} {7,S}
10   R!H u0 {5,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-45.2251,-43.8136,-40.2788,-34.6869,-23.5968,-14.78,-3.51744],'J/(mol*K)'),
        H298 = (34.5594,'kJ/mol'),
        S298 = (154.144,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_6_6_ene_m from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s2_6_6_diene",
    group = "OR{s2_6_6_diene_m_1, s2_6_6_diene_m_2, s2_6_6_diene_0_2, s2_6_6_diene_0_3, s2_6_6_diene_0_4, s2_6_6_diene_0_5, s2_6_6_diene_0_6, s2_6_6_diene_0_7, s2_6_6_diene_0_8, s2_6_6_diene_1_3, s2_6_6_diene_1_6, s2_6_6_diene_1_7, s2_6_6_diene_1_8, s2_6_6_diene_2_7}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 123,
    label = "s2_6_6_diene_m_1",
    group = 
"""
1    R!H u0 {2,D} {4,S} {6,S}
2    R!H u0 {1,D} {3,S} {5,S}
3    R!H u0 {2,S} {9,S}
4    R!H u0 {1,S} {8,S}
5    R!H u0 {2,S} {7,D}
6    R!H u0 {1,S} {10,S}
7  * R!H u0 {5,D} {8,S}
8    R!H u0 {4,S} {7,S}
9    R!H u0 {3,S} {10,S}
10   R!H u0 {6,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-42.4834,-44.2058,-42.1578,-36.9087,-25.8969,-17.1002,-6.65608],'J/(mol*K)'),
        H298 = (47.0401,'kJ/mol'),
        S298 = (188.632,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_6_6_diene_m_1 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 124,
    label = "s2_6_6_diene_m_2",
    group = 
"""
1    R!H u0 {2,D} {5,S} {6,S}
2    R!H u0 {1,D} {3,S} {4,S}
3    R!H u0 {2,S} {8,S}
4    R!H u0 {2,S} {10,S}
5    R!H u0 {1,S} {9,S}
6    R!H u0 {1,S} {7,S}
7  * R!H u0 {6,S} {10,S}
8    R!H u0 {3,S} {9,D}
9    R!H u0 {5,S} {8,D}
10   R!H u0 {4,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-36.4704,-37.506,-35.2594,-30.5046,-21.0927,-13.8636,-3.90332],'J/(mol*K)'),
        H298 = (27.5712,'kJ/mol'),
        S298 = (167.901,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_6_6_diene_m_2 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 125,
    label = "s2_6_6_diene_0_2",
    group = 
"""
1    R!H u0 {2,S} {3,S} {5,S}
2    R!H u0 {1,S} {4,S} {6,D}
3    R!H u0 {1,S} {8,S}
4    R!H u0 {2,S} {10,S}
5    R!H u0 {1,S} {9,S}
6    R!H u0 {2,D} {7,S}
7  * R!H u0 {6,S} {8,D}
8    R!H u0 {3,S} {7,D}
9    R!H u0 {5,S} {10,S}
10   R!H u0 {4,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-41.1697,-42.9508,-41.3835,-35.9799,-25.3008,-16.5271,-7.06396],'J/(mol*K)'),
        H298 = (63.4493,'kJ/mol'),
        S298 = (189.537,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_6_6_diene_0_2 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 126,
    label = "s2_6_6_diene_0_3",
    group = 
"""
1    R!H u0 {2,S} {4,S} {6,D}
2    R!H u0 {1,S} {3,S} {5,S}
3    R!H u0 {2,S} {10,S}
4    R!H u0 {1,S} {9,S}
5    R!H u0 {2,S} {7,D}
6    R!H u0 {1,D} {8,S}
7  * R!H u0 {5,D} {8,S}
8    R!H u0 {6,S} {7,S}
9    R!H u0 {4,S} {10,S}
10   R!H u0 {3,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-42.7321,-39.342,-35.424,-30.3159,-20.1131,-12.6136,-3.65148],'J/(mol*K)'),
        H298 = (28.0356,'kJ/mol'),
        S298 = (178.832,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_6_6_diene_0_3 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 127,
    label = "s2_6_6_diene_0_4",
    group = 
"""
1    R!H u0 {2,S} {3,S} {5,D}
2    R!H u0 {1,S} {4,D} {6,S}
3    R!H u0 {1,S} {10,S}
4    R!H u0 {2,D} {8,S}
5    R!H u0 {1,D} {7,S}
6    R!H u0 {2,S} {9,S}
7  * R!H u0 {5,S} {8,S}
8    R!H u0 {4,S} {7,S}
9    R!H u0 {6,S} {10,S}
10   R!H u0 {3,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-42.7644,-44.3168,-42.0638,-36.6797,-25.5709,-16.8262,-6.67908],'J/(mol*K)'),
        H298 = (53.8256,'kJ/mol'),
        S298 = (181.405,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_6_6_diene_0_4 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 128,
    label = "s2_6_6_diene_0_5",
    group = 
"""
1    R!H u0 {2,S} {3,S} {5,D}
2    R!H u0 {1,S} {4,D} {6,S}
3    R!H u0 {1,S} {9,S}
4    R!H u0 {2,D} {7,S}
5    R!H u0 {1,D} {10,S}
6    R!H u0 {2,S} {8,S}
7  * R!H u0 {4,S} {9,S}
8    R!H u0 {6,S} {10,S}
9    R!H u0 {3,S} {7,S}
10   R!H u0 {5,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-43.7554,-45.3278,-42.9508,-37.4467,-26.1409,-17.2492,-6.89208],'J/(mol*K)'),
        H298 = (34.4058,'kJ/mol'),
        S298 = (180.245,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_6_6_diene_0_5 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 129,
    label = "s2_6_6_diene_0_6",
    group = 
"""
1    R!H u0 {2,S} {5,S} {6,D}
2    R!H u0 {1,S} {3,S} {4,S}
3    R!H u0 {2,S} {10,S}
4    R!H u0 {2,S} {9,D}
5    R!H u0 {1,S} {8,S}
6    R!H u0 {1,D} {7,S}
7  * R!H u0 {6,S} {10,S}
8    R!H u0 {5,S} {9,S}
9    R!H u0 {4,D} {8,S}
10   R!H u0 {3,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-40.4485,-37.0315,-33.0252,-27.7344,-17.702,-10.5593,-3.47236],'J/(mol*K)'),
        H298 = (259.528,'kJ/mol'),
        S298 = (176.442,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_6_6_diene_0_6 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 130,
    label = "s2_6_6_diene_0_7",
    group = 
"""
1    R!H u0 {2,S} {4,S} {6,D}
2    R!H u0 {1,S} {3,S} {5,S}
3    R!H u0 {2,S} {8,S}
4    R!H u0 {1,S} {9,S}
5    R!H u0 {2,S} {10,S}
6    R!H u0 {1,D} {7,S}
7  * R!H u0 {6,S} {10,S}
8    R!H u0 {3,S} {9,D}
9    R!H u0 {4,S} {8,D}
10   R!H u0 {5,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-35.6501,-36.3445,-34.5142,-29.6673,-20.6586,-13.2452,-4.61508],'J/(mol*K)'),
        H298 = (40.2236,'kJ/mol'),
        S298 = (173.573,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_6_6_diene_0_7 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 131,
    label = "s2_6_6_diene_0_8",
    group = 
"""
1    R!H u0 {2,S} {4,S} {6,D}
2    R!H u0 {1,S} {3,S} {5,S}
3    R!H u0 {2,S} {9,S}
4    R!H u0 {1,S} {10,D}
5    R!H u0 {2,S} {8,S}
6    R!H u0 {1,D} {7,S}
7  * R!H u0 {6,S} {8,S}
8    R!H u0 {5,S} {7,S}
9    R!H u0 {3,S} {10,S}
10   R!H u0 {4,D} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-42.3927,-43.3708,-41.6165,-36.4059,-25.7778,-16.7901,-6.78596],'J/(mol*K)'),
        H298 = (45.2815,'kJ/mol'),
        S298 = (188.16,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_6_6_diene_0_8 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 132,
    label = "s2_6_6_diene_1_3",
    group = 
"""
1    R!H u0 {2,S} {5,S} {6,S}
2    R!H u0 {1,S} {3,S} {4,S}
3    R!H u0 {2,S} {7,D}
4    R!H u0 {2,S} {8,S}
5    R!H u0 {1,S} {10,S}
6    R!H u0 {1,S} {9,D}
7  * R!H u0 {3,D} {9,S}
8    R!H u0 {4,S} {10,S}
9    R!H u0 {6,D} {7,S}
10   R!H u0 {5,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-40.963,-41.2288,-39.5802,-34.4991,-24.6798,-15.8711,-6.70784],'J/(mol*K)'),
        H298 = (49.5297,'kJ/mol'),
        S298 = (182.032,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_6_6_diene_1_3 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 133,
    label = "s2_6_6_diene_1_6",
    group = 
"""
1    R!H u0 {2,S} {5,S} {6,S}
2    R!H u0 {1,S} {3,S} {4,S}
3    R!H u0 {2,S} {10,S}
4    R!H u0 {2,S} {8,D}
5    R!H u0 {1,S} {9,S}
6    R!H u0 {1,S} {7,D}
7  * R!H u0 {6,D} {10,S}
8    R!H u0 {4,D} {9,S}
9    R!H u0 {5,S} {8,S}
10   R!H u0 {3,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-35.1458,-34.522,-33.034,-28.671,-20.6054,-12.9339,-4.88284],'J/(mol*K)'),
        H298 = (37.2373,'kJ/mol'),
        S298 = (167.685,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_6_6_diene_1_6 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 134,
    label = "s2_6_6_diene_1_7",
    group = 
"""
1    R!H u0 {2,S} {4,S} {6,S}
2    R!H u0 {1,S} {3,S} {5,S}
3    R!H u0 {2,S} {10,S}
4    R!H u0 {1,S} {7,S}
5    R!H u0 {2,S} {8,D}
6    R!H u0 {1,S} {9,S}
7  * R!H u0 {4,S} {10,D}
8    R!H u0 {5,D} {9,S}
9    R!H u0 {6,S} {8,S}
10   R!H u0 {3,S} {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-32.4608,-29.344,-26.6036,-23.175,-16.3694,-9.75388,-3.41684],'J/(mol*K)'),
        H298 = (491.058,'kJ/mol'),
        S298 = (167.365,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_6_6_diene_1_7 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 135,
    label = "s2_6_6_diene_1_8",
    group = 
"""
1    R!H u0 {2,S} {4,S} {5,S}
2    R!H u0 {1,S} {3,S} {6,S}
3    R!H u0 {2,S} {7,S}
4    R!H u0 {1,S} {10,D}
5    R!H u0 {1,S} {8,D}
6    R!H u0 {2,S} {9,S}
7  * R!H u0 {3,S} {8,S}
8    R!H u0 {5,D} {7,S}
9    R!H u0 {6,S} {10,S}
10   R!H u0 {4,D} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-41.6858,-37.5635,-33.5415,-29.1196,-19.793,-12.1923,-4.18924],'J/(mol*K)'),
        H298 = (40.4249,'kJ/mol'),
        S298 = (179.403,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_6_6_diene_1_8 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 136,
    label = "s2_6_6_diene_2_7",
    group = 
"""
1    R!H u0 {2,S} {4,S} {6,S}
2    R!H u0 {1,S} {3,S} {5,S}
3    R!H u0 {2,S} {8,S}
4    R!H u0 {1,S} {9,S}
5    R!H u0 {2,S} {7,S}
6    R!H u0 {1,S} {10,S}
7  * R!H u0 {5,S} {9,D}
8    R!H u0 {3,S} {10,D}
9    R!H u0 {4,S} {7,D}
10   R!H u0 {6,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-35.1668,-34.287,-31.7922,-28.274,-20.2824,-12.6709,-4.71884],'J/(mol*K)'),
        H298 = (38.2803,'kJ/mol'),
        S298 = (171.725,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_6_6_diene_2_7 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s2_6_6_triene",
    group = "OR{s2_6_6_triene_0_2_6, s2_6_6_triene_0_2_7, s2_6_6_triene_0_3_7, s2_6_6_triene_1_3_6, s2_6_6_triene_1_3_7}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 123,
    label = "s2_6_6_triene_0_2_6",
    group = 
"""
1    R!H u0 {2,S} {4,S} {6,S}
2    R!H u0 {1,S} {3,S} {5,D}
3    R!H u0 {2,S} {10,S}
4    R!H u0 {1,S} {7,D}
5    R!H u0 {2,D} {8,S}
6    R!H u0 {1,S} {9,S}
7  * R!H u0 {4,D} {10,S}
8    R!H u0 {5,S} {9,D}
9    R!H u0 {6,S} {8,D}
10   R!H u0 {3,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.27,-7.7,-6.87,-5.9,-4.53,-3.57,-2.03],'cal/(mol*K)'),
        H298 = (7.693,'kcal/mol'),
        S298 = (54.74,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt19 from C10H11 library.
""",
)

entry(
    index = 123,
    label = "s2_6_6_triene_0_2_7",
    group = 
"""
1    R!H u0 {2,S} {4,S} {6,S}
2    R!H u0 {1,S} {3,D} {5,S}
3    R!H u0 {2,D} {7,S}
4    R!H u0 {1,S} {9,S}
5    R!H u0 {2,S} {8,S}
6    R!H u0 {1,S} {10,S}
7  * R!H u0 {3,S} {9,D}
8    R!H u0 {5,S} {10,D}
9    R!H u0 {4,S} {7,D}
10   R!H u0 {6,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.98,-7.21,-6.77,-5.84,-4.695,-3.755,-2.135],'cal/(mol*K)','+|-',[2.95853,2.36683,1.77512,1.4201,0.88756,0.650878,0.295853]),
        H298 = (2.333,'kcal/mol','+|-',14.9058),
        S298 = (51.955,'cal/(mol*K)','+|-',2.95571),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt19 from C10H11 library.
Fitted from species pdt37 from C10H11 library.
""",
)

entry(
    index = 123,
    label = "s2_6_6_triene_0_3_7",
    group = 
"""
1    R!H u0 {2,S} {4,D} {6,S}
2    R!H u0 {1,S} {3,S} {5,S}
3    R!H u0 {2,S} {10,D}
4    R!H u0 {1,D} {7,S}
5    R!H u0 {2,S} {8,S}
6    R!H u0 {1,S} {9,S}
7  * R!H u0 {4,S} {10,S}
8    R!H u0 {5,S} {9,D}
9    R!H u0 {6,S} {8,D}
10   R!H u0 {3,D} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.74,-6.32,-5.65,-4.95,-3.99,-3.38,-2.69],'cal/(mol*K)'),
        H298 = (2.193,'kcal/mol'),
        S298 = (48.91,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt37 from C10H11 library.
""",
)

entry(
    index = 123,
    label = "s2_6_6_triene_1_3_6",
    group = 
"""
1    R!H u0 {2,S} {3,S} {4,S}
2    R!H u0 {1,S} {5,S} {6,S}
3    R!H u0 {1,S} {9,S}
4    R!H u0 {1,S} {10,D}
5    R!H u0 {2,S} {8,D}
6    R!H u0 {2,S} {7,D}
7  * R!H u0 {6,D} {9,S}
8    R!H u0 {5,D} {10,S}
9    R!H u0 {3,S} {7,S}
10   R!H u0 {4,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.91,-7.26,-6.54,-5.57,-4.35,-3.43,-2.07],'cal/(mol*K)'),
        H298 = (7.733,'kcal/mol'),
        S298 = (54.59,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt10bis from C10H11 library.
""",
)

entry(
    index = 123,
    label = "s2_6_6_triene_1_3_7",
    group = 
"""
1    R!H u0 {2,S} {4,S} {6,S}
2    R!H u0 {1,S} {3,S} {5,S}
3    R!H u0 {2,S} {7,S}
4    R!H u0 {1,S} {8,S}
5    R!H u0 {2,S} {10,D}
6    R!H u0 {1,S} {9,D}
7  * R!H u0 {3,S} {8,D}
8    R!H u0 {4,S} {7,D}
9    R!H u0 {6,D} {10,S}
10   R!H u0 {5,D} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.455,-6.46,-6.15,-5.28,-4.38,-3.47,-2.41],'cal/(mol*K)','+|-',[0.532536,0.946731,1.53844,1.65678,1.53844,1.30176,2.24849]),
        H298 = (3.073,'kcal/mol','+|-',13.7744),
        S298 = (52.44,'cal/(mol*K)','+|-',1.21622),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt10bis from C10H11 library.
Fitted from species pdt37 from C10H11 library.
""",
)

entry(
    index = 0,
    label = "s2_6_6_tetraene",
    group = "OR{s2_6_6_tetraene_0_2_4_7, s2_6_6_tetraene_0_2_5_7, s2_6_6_tetraene_0_2_6_8, s2_6_6_tetraene_0_3_6_8, s2_6_6_tetraene_1_3_6_8}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 123,
    label = "s2_6_6_tetraene_0_2_4_7",
    group = 
"""
1    R!H u0 {2,S} {3,S} {4,D}
2    R!H u0 {1,S} {5,D} {6,S}
3    R!H u0 {1,S} {8,S}
4    R!H u0 {1,D} {7,S}
5    R!H u0 {2,D} {10,S}
6    R!H u0 {2,S} {9,S}
7  * R!H u0 {4,S} {10,D}
8    R!H u0 {3,S} {9,D}
9    R!H u0 {6,S} {8,D}
10   R!H u0 {5,S} {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10.4,-11.67,-11.09,-9.63,-7.17,-5.47,-2.85],'cal/(mol*K)'),
        H298 = (-17.82,'kcal/mol'),
        S298 = (53.93,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt38 from C10H11 library.
""",
)

entry(
    index = 123,
    label = "s2_6_6_tetraene_0_2_5_7",
    group = 
"""
1    R!H u0 {2,S} {3,D} {5,S}
2    R!H u0 {1,S} {4,S} {6,D}
3    R!H u0 {1,D} {8,S}
4    R!H u0 {2,S} {10,S}
5    R!H u0 {1,S} {9,S}
6    R!H u0 {2,D} {7,S}
7  * R!H u0 {6,S} {9,D}
8    R!H u0 {3,S} {10,D}
9    R!H u0 {5,S} {7,D}
10   R!H u0 {4,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.51,-10.83,-10.38,-9.04,-6.78,-5.2,-2.72],'cal/(mol*K)'),
        H298 = (10.33,'kcal/mol'),
        S298 = (53.47,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt26 from C10H11 library.
""",
)

entry(
    index = 123,
    label = "s2_6_6_tetraene_0_2_6_8",
    group = 
"""
1    R!H u0 {2,S} {3,S} {6,S}
2    R!H u0 {1,S} {4,D} {5,S}
3    R!H u0 {1,S} {8,D}
4    R!H u0 {2,D} {7,S}
5    R!H u0 {2,S} {10,D}
6    R!H u0 {1,S} {9,S}
7  * R!H u0 {4,S} {9,D}
8    R!H u0 {3,D} {10,S}
9    R!H u0 {6,S} {7,D}
10   R!H u0 {5,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10.475,-10.72,-10,-8.715,-6.555,-5.06,-3.055],'cal/(mol*K)','+|-',[6.21292,6.62712,5.79873,4.4378,1.71595,0.355024,3.13605]),
        H298 = (1.5665,'kcal/mol','+|-',21.2797),
        S298 = (58.74,'cal/(mol*K)','+|-',4.18607),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt11 from C10H11 library.
Fitted from species prod4 from naphthalene_H library.
""",
)

entry(
    index = 123,
    label = "s2_6_6_tetraene_0_3_6_8",
    group = 
"""
1    R!H u0 {2,S} {5,D} {6,S}
2    R!H u0 {1,S} {3,S} {4,S}
3    R!H u0 {2,S} {8,D}
4    R!H u0 {2,S} {10,D}
5    R!H u0 {1,D} {7,S}
6    R!H u0 {1,S} {9,D}
7  * R!H u0 {5,S} {8,S}
8    R!H u0 {3,D} {7,S}
9    R!H u0 {6,D} {10,S}
10   R!H u0 {4,D} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.57,-7.86,-7.37,-6.54,-5.25,-4.39,-3.88],'cal/(mol*K)'),
        H298 = (-1.957,'kcal/mol'),
        S298 = (55.67,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species prod4 from naphthalene_H library.
""",
)

entry(
    index = 123,
    label = "s2_6_6_tetraene_1_3_6_8",
    group = 
"""
1    R!H u0 {2,S} {3,S} {4,S}
2    R!H u0 {1,S} {5,S} {6,S}
3    R!H u0 {1,S} {8,D}
4    R!H u0 {1,S} {9,D}
5    R!H u0 {2,S} {10,D}
6    R!H u0 {2,S} {7,D}
7  * R!H u0 {6,D} {8,S}
8    R!H u0 {3,D} {7,S}
9    R!H u0 {4,D} {10,S}
10   R!H u0 {5,D} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10.33,-8.08,-6.33,-4.9,-3.09,-2.2,-1.2],'cal/(mol*K)'),
        H298 = (-22.037,'kcal/mol'),
        S298 = (49.84,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species prod4 from naphthalene_H library.
""",
)

entry(
    index = 185,
    label = "s2_6_6_ben",
    group = 
"""
1    R!H u0 {2,B} {3,B} {5,S}
2    R!H u0 {1,B} {4,B} {6,S}
3    R!H u0 {1,B} {7,B}
4    R!H u0 {2,B} {9,B}
5    R!H u0 {1,S} {10,S}
6    R!H u0 {2,S} {8,S}
7  * R!H u0 {3,B} {9,B}
8    R!H u0 {6,S} {10,S}
9    R!H u0 {4,B} {7,B}
10   R!H u0 {5,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-22.6673,-21.2954,-19.5434,-17.0615,-10.7908,-5.16852,3.2034],'J/(mol*K)'),
        H298 = (24.5885,'kJ/mol'),
        S298 = (78.9822,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_6_6_ben from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s2_6_6_ben_ene",
    group = "OR{s2_6_6_ben_ene_1, s2_6_6_ben_ene_2}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 123,
    label = "s2_6_6_ben_ene_1",
    group = 
"""
1    R!H u0 {2,B} {3,S} {4,B}
2    R!H u0 {1,B} {5,B} {6,S}
3    R!H u0 {1,S} {7,D}
4    R!H u0 {1,B} {8,B}
5    R!H u0 {2,B} {9,B}
6    R!H u0 {2,S} {10,S}
7  * R!H u0 {3,D} {10,S}
8    R!H u0 {4,B} {9,B}
9    R!H u0 {5,B} {8,B}
10   R!H u0 {6,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-20.9962,-19.5374,-17.8098,-15.9012,-10.8962,-6.2246,-0.13508],'J/(mol*K)'),
        H298 = (17.9864,'kJ/mol'),
        S298 = (87.3879,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_6_6_ben_ene_1 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 123,
    label = "s2_6_6_ben_ene_2",
    group = 
"""
1    R!H u0 {2,B} {4,B} {5,S}
2    R!H u0 {1,B} {3,S} {6,B}
3    R!H u0 {2,S} {8,S}
4    R!H u0 {1,B} {10,B}
5    R!H u0 {1,S} {7,S}
6    R!H u0 {2,B} {9,B}
7  * R!H u0 {5,S} {8,D}
8    R!H u0 {3,S} {7,D}
9    R!H u0 {6,B} {10,B}
10   R!H u0 {4,B} {9,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.68,-1.73,-1.85,-1.91,-2.19,-2.39,-2.51],'cal/(mol*K)'),
        H298 = (2.84,'kcal/mol'),
        S298 = (35.91,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt38 from C10H11 library.
""",
)

entry(
    index = 185,
    label = "s2_6_6_naphthalene",
    group = 
"""
1    R!H u0 {2,B} {3,B} {4,B}
2    R!H u0 {1,B} {5,B} {6,B}
3    R!H u0 {1,B} {9,B}
4    R!H u0 {1,B} {8,B}
5    R!H u0 {2,B} {10,B}
6    R!H u0 {2,B} {7,B}
7  * R!H u0 {6,B} {8,B}
8    R!H u0 {4,B} {7,B}
9    R!H u0 {3,B} {10,B}
10   R!H u0 {5,B} {9,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.79295e-15,0,-1.35859e-14,-6.79295e-15,0,1.35859e-14,-1.35859e-14],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (-2.75,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species naphthalene from naphthalene_H library.
""",
)

entry(
    index = 0,
    label = "s3_4_4",
    group = 
"""
1   R!H u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 * R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 137,
    label = "s3_4_4_ane",
    group = 
"""
1   R!H u0 {3,S} {4,S} {5,S}
2   R!H u0 {3,S} {4,S} {5,S}
3 * R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {2,S}
5   R!H u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-31.8958,-31.3184,-28.5346,-25.5786,-22.0387,-18.4691,-15.1146],'J/(mol*K)'),
        H298 = (286.729,'kJ/mol'),
        S298 = (243.588,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_4_4_ane from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s3_4_4_ene",
    group = "OR{s3_4_4_ene_0}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 138,
    label = "s3_4_4_ene_0",
    group = 
"""
1   R!H u0 {3,S} {4,S} {5,D}
2   R!H u0 {3,S} {4,S} {5,S}
3 * R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {2,S}
5   R!H u0 {1,D} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-18.7988,-20.3137,-20.4825,-19.5821,-18.8254,-17.0791,-15.4903],'J/(mol*K)'),
        H298 = (435.842,'kJ/mol'),
        S298 = (265.377,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_4_4_ene_0 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s3_4_4_diene",
    group = "OR{s3_4_4_diene_0_2}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 139,
    label = "s3_4_4_diene_0_2",
    group = 
"""
1   R!H u0 {3,S} {4,S} {5,D}
2   R!H u0 {3,D} {4,S} {5,S}
3 * R!H u0 {1,S} {2,D}
4   R!H u0 {1,S} {2,S}
5   R!H u0 {1,D} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-26.5955,-32.5565,-32.8788,-30.8172,-27.042,-23.8509,-20.2932],'J/(mol*K)'),
        H298 = (523.255,'kJ/mol'),
        S298 = (291.241,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_4_4_diene_0_2 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s3_4_5",
    group = 
"""
1   R!H u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
2   R!H u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 * R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
5   R!H u0 {2,[S,D,T,B]} {6,[S,D,T,B]}
6   R!H u0 {1,[S,D,T,B]} {5,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 140,
    label = "s3_4_5_ane",
    group = 
"""
1   R!H u0 {3,S} {4,S} {6,S}
2   R!H u0 {3,S} {4,S} {5,S}
3 * R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {2,S}
5   R!H u0 {2,S} {6,S}
6   R!H u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-37.0449,-34.9162,-31.0466,-27.379,-22.2946,-17.5206,-12.7226],'J/(mol*K)'),
        H298 = (177.11,'kJ/mol'),
        S298 = (231.443,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_4_5_ane from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s3_4_5_ene",
    group = "OR{s3_4_5_ene_0, s3_4_5_ene_1, s3_4_5_ene_3}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 141,
    label = "s3_4_5_ene_0",
    group = 
"""
1   R!H u0 {3,S} {4,S} {6,D}
2   R!H u0 {3,S} {4,S} {5,S}
3 * R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {2,S}
5   R!H u0 {2,S} {6,S}
6   R!H u0 {1,D} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-24.4259,-24.6635,-24.0391,-21.9755,-17.9093,-14.5987,-12.7203],'J/(mol*K)'),
        H298 = (533.055,'kJ/mol'),
        S298 = (241.141,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_4_5_ene_0 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 142,
    label = "s3_4_5_ene_1",
    group = 
"""
1   R!H u0 {3,S} {4,S} {5,S}
2   R!H u0 {3,S} {4,S} {6,S}
3 * R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {2,S}
5   R!H u0 {1,S} {6,D}
6   R!H u0 {2,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-28.5725,-27.2005,-25.2092,-22.2387,-19.5652,-16.2286,-13.6072],'J/(mol*K)'),
        H298 = (234.64,'kJ/mol'),
        S298 = (234.403,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_4_5_ene_1 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 143,
    label = "s3_4_5_ene_3",
    group = 
"""
1   R!H u0 {3,D} {4,S} {6,S}
2   R!H u0 {3,S} {4,S} {5,S}
3 * R!H u0 {1,D} {2,S}
4   R!H u0 {1,S} {2,S}
5   R!H u0 {2,S} {6,S}
6   R!H u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-21.1077,-22.3405,-21.9755,-20.2055,-17.8073,-14.9817,-12.3823],'J/(mol*K)'),
        H298 = (402.876,'kJ/mol'),
        S298 = (254.658,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_4_5_ene_3 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s3_4_5_diene",
    group = "OR{s3_4_5_diene_0_2, s3_4_5_diene_0_3, s3_4_5_diene_1_3, s3_4_5_diene_3_4}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 144,
    label = "s3_4_5_diene_0_2",
    group = 
"""
1   R!H u0 {3,S} {4,S} {6,D}
2   R!H u0 {3,S} {4,S} {5,D}
3 * R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {2,S}
5   R!H u0 {2,D} {6,S}
6   R!H u0 {1,D} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-27.0139,-29.9076,-28.7385,-26.467,-22.6216,-19.5906,-15.5143],'J/(mol*K)'),
        H298 = (387.717,'kJ/mol'),
        S298 = (249.869,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_4_5_diene_0_2 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 145,
    label = "s3_4_5_diene_0_3",
    group = 
"""
1   R!H u0 {3,S} {4,S} {6,D}
2   R!H u0 {3,S} {4,D} {5,S}
3 * R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {2,D}
5   R!H u0 {2,S} {6,S}
6   R!H u0 {1,D} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-16.0956,-23.1066,-25.1175,-23.8,-20.3886,-17.9916,-15.1753],'J/(mol*K)'),
        H298 = (425.803,'kJ/mol'),
        S298 = (275.729,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_4_5_diene_0_3 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 146,
    label = "s3_4_5_diene_1_3",
    group = 
"""
1   R!H u0 {3,S} {4,S} {5,S}
2   R!H u0 {3,D} {4,S} {6,S}
3 * R!H u0 {1,S} {2,D}
4   R!H u0 {1,S} {2,S}
5   R!H u0 {1,S} {6,D}
6   R!H u0 {2,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-29.1089,-28.7021,-26.8164,-24.6529,-20.7769,-17.6863,-15.1744],'J/(mol*K)'),
        H298 = (412.175,'kJ/mol'),
        S298 = (273.542,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_4_5_diene_1_3 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 147,
    label = "s3_4_5_diene_3_4",
    group = 
"""
1   R!H u0 {3,D} {4,S} {5,S}
2   R!H u0 {3,S} {4,D} {6,S}
3 * R!H u0 {1,D} {2,S}
4   R!H u0 {1,S} {2,D}
5   R!H u0 {1,S} {6,S}
6   R!H u0 {2,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-28.6891,-33.3444,-33.386,-31.2361,-26.3748,-22.0771,-17.7121],'J/(mol*K)'),
        H298 = (518.447,'kJ/mol'),
        S298 = (276.231,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_4_5_diene_3_4 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s3_4_6",
    group = 
"""
1   R!H u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
2   R!H u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 * R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
5   R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
6   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
7   R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 148,
    label = "s3_4_6_ane",
    group = 
"""
1   R!H u0 {3,S} {4,S} {6,S}
2   R!H u0 {3,S} {4,S} {5,S}
3 * R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {2,S}
5   R!H u0 {2,S} {7,S}
6   R!H u0 {1,S} {7,S}
7   R!H u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-40.1137,-37.796,-33.8196,-29.7774,-23.0415,-16.9282,-10.2826],'J/(mol*K)'),
        H298 = (158.25,'kJ/mol'),
        S298 = (220.201,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_4_6_ane from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s3_4_6_ene",
    group = "OR{s3_4_6_ene_0, s3_4_6_ene_1, s3_4_6_ene_4}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 149,
    label = "s3_4_6_ene_0",
    group = 
"""
1   R!H u0 {3,S} {4,S} {6,D}
2   R!H u0 {3,S} {4,S} {5,S}
3 * R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {2,S}
5   R!H u0 {2,S} {7,S}
6   R!H u0 {1,D} {7,S}
7   R!H u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-32.4104,-30.8903,-28.9091,-25.5799,-19.3522,-14.5632,-10.9473],'J/(mol*K)'),
        H298 = (345.216,'kJ/mol'),
        S298 = (215.635,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_4_6_ene_0 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 150,
    label = "s3_4_6_ene_1",
    group = 
"""
1   R!H u0 {3,S} {4,S} {6,S}
2   R!H u0 {3,S} {4,S} {5,S}
3 * R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {2,S}
5   R!H u0 {2,S} {7,S}
6   R!H u0 {1,S} {7,D}
7   R!H u0 {5,S} {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-33.1708,-31.5223,-28.8028,-25.6321,-21.0411,-16.1772,-11.3632],'J/(mol*K)'),
        H298 = (152.46,'kJ/mol'),
        S298 = (220.803,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_4_6_ene_1 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 151,
    label = "s3_4_6_ene_4",
    group = 
"""
1   R!H u0 {3,S} {4,S} {5,S}
2   R!H u0 {3,D} {4,S} {6,S}
3 * R!H u0 {1,S} {2,D}
4   R!H u0 {1,S} {2,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {2,S} {7,S}
7   R!H u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-31.9504,-30.3993,-27.8705,-24.6859,-19.9692,-15.4412,-10.5613],'J/(mol*K)'),
        H298 = (345.152,'kJ/mol'),
        S298 = (220.251,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_4_6_ene_4 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s3_4_6_diene",
    group = "OR{s3_4_6_diene_0_2, s3_4_6_diene_0_3, s3_4_6_diene_0_4, s3_4_6_diene_1_4, s3_4_6_diene_1_5}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 152,
    label = "s3_4_6_diene_0_2",
    group = 
"""
1   R!H u0 {3,S} {4,S} {6,S}
2   R!H u0 {3,S} {4,S} {5,D}
3 * R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {2,S}
5   R!H u0 {2,D} {7,S}
6   R!H u0 {1,S} {7,D}
7   R!H u0 {5,S} {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-30.0137,-30.4274,-29.0735,-26.5357,-21.9972,-17.5084,-13.398],'J/(mol*K)'),
        H298 = (395.317,'kJ/mol'),
        S298 = (237.586,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_4_6_diene_0_2 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 153,
    label = "s3_4_6_diene_0_3",
    group = 
"""
1   R!H u0 {3,S} {4,S} {5,D}
2   R!H u0 {3,S} {4,S} {6,D}
3 * R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {2,S}
5   R!H u0 {1,D} {7,S}
6   R!H u0 {2,D} {7,S}
7   R!H u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-26.3691,-28.1941,-27.0762,-23.8649,-18.3822,-15.0822,-11.2364],'J/(mol*K)'),
        H298 = (239.177,'kJ/mol'),
        S298 = (217.83,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_4_6_diene_0_3 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 154,
    label = "s3_4_6_diene_0_4",
    group = 
"""
1   R!H u0 {3,S} {4,D} {5,S}
2   R!H u0 {3,S} {4,S} {6,D}
3 * R!H u0 {1,S} {2,S}
4   R!H u0 {1,D} {2,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {2,D} {7,S}
7   R!H u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-21.7,-27.1089,-28.1797,-26.06,-21.1454,-17.4238,-13.5212],'J/(mol*K)'),
        H298 = (302.238,'kJ/mol'),
        S298 = (253.297,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_4_6_diene_0_4 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 155,
    label = "s3_4_6_diene_1_4",
    group = 
"""
1   R!H u0 {3,S} {4,S} {5,S}
2   R!H u0 {3,D} {4,S} {6,S}
3 * R!H u0 {1,S} {2,D}
4   R!H u0 {1,S} {2,S}
5   R!H u0 {1,S} {7,D}
6   R!H u0 {2,S} {7,S}
7   R!H u0 {5,D} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-31.1701,-27.2286,-23.56,-20.9957,-16.7835,-13.692,-10.4635],'J/(mol*K)'),
        H298 = (352.615,'kJ/mol'),
        S298 = (227.735,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_4_6_diene_1_4 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 156,
    label = "s3_4_6_diene_1_5",
    group = 
"""
1   R!H u0 {3,S} {4,S} {5,S}
2   R!H u0 {3,D} {4,S} {6,S}
3 * R!H u0 {1,S} {2,D}
4   R!H u0 {1,S} {2,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {2,S} {7,D}
7   R!H u0 {5,S} {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-29.9567,-30.9094,-29.7075,-27.0867,-22.4192,-17.7874,-13.389],'J/(mol*K)'),
        H298 = (396.195,'kJ/mol'),
        S298 = (240.272,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_4_6_diene_1_5 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s3_5_5",
    group = 
"""
1   R!H u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {3,[S,D,T,B]} {6,[S,D,T,B]} {7,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4 * R!H u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   R!H u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
7   R!H u0 {2,[S,D,T,B]} {5,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 157,
    label = "s3_5_5_ane",
    group = 
"""
1   R!H u0 {3,S} {4,S} {5,S}
2   R!H u0 {3,S} {6,S} {7,S}
3   R!H u0 {1,S} {2,S}
4 * R!H u0 {1,S} {6,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {2,S} {4,S}
7   R!H u0 {2,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-42.5947,-39.827,-35.1536,-30.5014,-23.4375,-17.2012,-10.5366],'J/(mol*K)'),
        H298 = (91.4539,'kJ/mol'),
        S298 = (212.089,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_5_5_ane from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s3_5_5_ene",
    group = "OR{s3_5_5_ene_0, s3_5_5_ene_1, s3_5_5_ene_side, s3_5_5_ene_m}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 158,
    label = "s3_5_5_ene_0",
    group = 
"""
1   R!H u0 {3,S} {4,S} {6,D}
2   R!H u0 {3,S} {5,S} {7,S}
3   R!H u0 {1,S} {2,S}
4 * R!H u0 {1,S} {5,S}
5   R!H u0 {2,S} {4,S}
6   R!H u0 {1,D} {7,S}
7   R!H u0 {2,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.785,-6.005,-5.34,-4.815,-4.35,-3.915,-3.05],'cal/(mol*K)','+|-',[8.69809,7.63302,6.62712,5.8579,4.61531,3.60941,2.13015]),
        H298 = (71.868,'kcal/mol','+|-',63.5123),
        S298 = (58.32,'cal/(mol*K)','+|-',1.69706),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species product23 from vinylCPD_H library.
Fitted from species product29 from vinylCPD_H library.
""",
)

entry(
    index = 158,
    label = "s3_5_5_ene_1",
    group = 
"""
1   R!H u0 {3,S} {5,S} {6,S}
2   R!H u0 {3,S} {4,S} {7,S}
3   R!H u0 {1,S} {2,S}
4 * R!H u0 {2,S} {5,S}
5   R!H u0 {1,S} {4,S}
6   R!H u0 {1,S} {7,D}
7   R!H u0 {2,S} {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-34.8478,-32.5933,-29.6322,-25.6211,-20.9501,-16.1252,-11.5392],'J/(mol*K)'),
        H298 = (112.159,'kJ/mol'),
        S298 = (218.255,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_5_5_ene_1 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 159,
    label = "s3_5_5_ene_side",
    group = 
"""
1   R!H   u0 {3,S} {4,S} {6,S}
2   R!H   u0 {4,S} {5,S} {7,S}
3 * R!H   u0 {1,S} {5,S} {8,D}
4   R!H   u0 {1,S} {2,S}
5   R!H   u0 {2,S} {3,S}
6   R!H   u0 {1,S} {7,S}
7   R!H   u0 {2,S} {6,S}
8   R!H ux {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.27,-8.28,-7.29,-6.18,-4.88,-3.81,-2.22],'cal/(mol*K)'),
        H298 = (14.6,'kcal/mol'),
        S298 = (50.85,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
A.G. Vandeputte isodesmic reactions + B3LYP/cbsb7 S and cp, CHECK!
""",
)

entry(
    index = 159,
    label = "s3_5_5_ene_m",
    group = 
"""
1   R!H u0 {3,D} {5,S} {7,S}
2   R!H u0 {3,S} {4,S} {6,S}
3   R!H u0 {1,D} {2,S}
4 * R!H u0 {2,S} {7,S}
5   R!H u0 {1,S} {6,S}
6   R!H u0 {2,S} {5,S}
7   R!H u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.05,-5.36,-4.88,-4.32,-3.96,-3.61,-2.87],'cal/(mol*K)'),
        H298 = (94.073,'kcal/mol'),
        S298 = (58.92,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species product29 from vinylCPD_H library.
""",
)

entry(
    index = 0,
    label = "s3_5_5_diene",
    group = "OR{s3_5_5_diene_1_4, s3_5_5_diene_0_4}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 160,
    label = "s3_5_5_diene_1_4",
    group = 
"""
1   R!H u0 {3,S} {6,S} {7,S}
2   R!H u0 {3,S} {4,S} {5,S}
3   R!H u0 {1,S} {2,S}
4 * R!H u0 {2,S} {6,D}
5   R!H u0 {2,S} {7,D}
6   R!H u0 {1,S} {4,D}
7   R!H u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-38.7328,-30.4776,-24.7887,-21.517,-16.6359,-13.376,-11.0656],'J/(mol*K)'),
        H298 = (155.943,'kJ/mol'),
        S298 = (229.303,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_5_5_diene_1_4 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s3_5_6",
    group = 
"""
1   R!H u0 {3,[S,D,T,B]} {5,[S,D,T,B]} {6,[S,D,T,B]}
2   R!H u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {7,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {5,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]}
6   R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
7   R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
8 * R!H u0 {6,[S,D,T,B]} {7,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 161,
    label = "s3_5_6_ane",
    group = 
"""
1   R!H u0 {3,S} {5,S} {6,S}
2   R!H u0 {3,S} {4,S} {7,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {2,S} {5,S}
5   R!H u0 {1,S} {4,S}
6   R!H u0 {1,S} {8,S}
7   R!H u0 {2,S} {8,S}
8 * R!H u0 {6,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-46.2517,-42.6158,-37.5346,-32.5278,-23.8414,-16.3148,-7.93156],'J/(mol*K)'),
        H298 = (67.4227,'kJ/mol'),
        S298 = (196.089,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_5_6_ane from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s3_5_6_ene",
    group = "OR{s3_5_6_ene_1, s3_5_6_ene_5}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 162,
    label = "s3_5_6_ene_1",
    group = 
"""
1   R!H u0 {3,S} {4,S} {7,S}
2   R!H u0 {3,S} {5,S} {6,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {5,S}
5   R!H u0 {2,S} {4,S}
6   R!H u0 {2,S} {8,S}
7   R!H u0 {1,S} {8,D}
8 * R!H u0 {6,S} {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-38.5888,-36.5861,-33.1328,-28.8915,-22.253,-15.8878,-9.1482],'J/(mol*K)'),
        H298 = (68.0263,'kJ/mol'),
        S298 = (201.64,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_5_6_ene_1 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 163,
    label = "s3_5_6_ene_5",
    group = 
"""
1   R!H u0 {3,S} {4,S} {7,S}
2   R!H u0 {3,S} {5,S} {6,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {5,D}
5   R!H u0 {2,S} {4,D}
6   R!H u0 {2,S} {8,S}
7   R!H u0 {1,S} {8,S}
8 * R!H u0 {6,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-38.8558,-36.1891,-32.9482,-28.4195,-21.938,-15.6968,-9.1362],'J/(mol*K)'),
        H298 = (82.5909,'kJ/mol'),
        S298 = (198.184,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_5_6_ene_5 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s3_5_6_diene",
    group = "OR{s3_5_6_diene_1_5}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 164,
    label = "s3_5_6_diene_1_5",
    group = 
"""
1   R!H u0 {3,S} {4,S} {6,S}
2   R!H u0 {3,S} {5,S} {7,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {5,D}
5   R!H u0 {2,S} {4,D}
6   R!H u0 {1,S} {8,D}
7   R!H u0 {2,S} {8,S}
8 * R!H u0 {6,D} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-35.7878,-32.3139,-29.8959,-25.7148,-18.5232,-13.2892,-9.78224],'J/(mol*K)'),
        H298 = (86.0654,'kJ/mol'),
        S298 = (209.421,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_5_6_diene_1_5 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s3_6_6",
    group = 
"""
1   R!H u0 {3,[S,D,T,B]} {6,[S,D,T,B]} {7,[S,D,T,B]}
2   R!H u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4 * R!H u0 {2,[S,D,T,B]} {9,[S,D,T,B]}
5   R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
6   R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
7   R!H u0 {1,[S,D,T,B]} {9,[S,D,T,B]}
8   R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
9   R!H u0 {4,[S,D,T,B]} {7,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 165,
    label = "s3_6_6_ane",
    group = 
"""
1   R!H u0 {3,S} {6,S} {7,S}
2   R!H u0 {3,S} {4,S} {5,S}
3   R!H u0 {1,S} {2,S}
4 * R!H u0 {2,S} {9,S}
5   R!H u0 {2,S} {8,S}
6   R!H u0 {1,S} {8,S}
7   R!H u0 {1,S} {9,S}
8   R!H u0 {5,S} {6,S}
9   R!H u0 {4,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-51.2247,-47.4056,-42.0986,-36.4622,-25.7252,-16.6263,-6.05456],'J/(mol*K)'),
        H298 = (65.8567,'kJ/mol'),
        S298 = (170.519,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_6_6_ane from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s3_6_6_ene",
    group = "OR{s3_6_6_ene_0, s3_6_6_ene_1, s3_6_6_ene_4}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 166,
    label = "s3_6_6_ene_0",
    group = 
"""
1   R!H u0 {3,S} {4,S} {7,S}
2   R!H u0 {3,S} {5,S} {6,D}
3   R!H u0 {1,S} {2,S}
4 * R!H u0 {1,S} {8,S}
5   R!H u0 {2,S} {8,S}
6   R!H u0 {2,D} {9,S}
7   R!H u0 {1,S} {9,S}
8   R!H u0 {4,S} {5,S}
9   R!H u0 {6,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-42.7994,-38.8219,-34.0181,-29.4987,-21.0879,-13.9144,-5.76432],'J/(mol*K)'),
        H298 = (277.792,'kJ/mol'),
        S298 = (173.865,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_6_6_ene_0 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 167,
    label = "s3_6_6_ene_1",
    group = 
"""
1   R!H u0 {3,S} {4,S} {6,S}
2   R!H u0 {3,S} {5,S} {7,S}
3   R!H u0 {1,S} {2,S}
4 * R!H u0 {1,S} {9,S}
5   R!H u0 {2,S} {8,S}
6   R!H u0 {1,S} {8,D}
7   R!H u0 {2,S} {9,S}
8   R!H u0 {5,S} {6,D}
9   R!H u0 {4,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-42.2638,-39.4379,-35.5818,-30.8459,-22.4699,-14.8223,-6.4372],'J/(mol*K)'),
        H298 = (45.0863,'kJ/mol'),
        S298 = (180.213,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_6_6_ene_1 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 168,
    label = "s3_6_6_ene_4",
    group = 
"""
1   R!H u0 {3,D} {4,S} {6,S}
2   R!H u0 {3,S} {5,S} {7,S}
3   R!H u0 {1,D} {2,S}
4 * R!H u0 {1,S} {8,S}
5   R!H u0 {2,S} {9,S}
6   R!H u0 {1,S} {9,S}
7   R!H u0 {2,S} {8,S}
8   R!H u0 {4,S} {7,S}
9   R!H u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-31.5534,-30.7939,-29.0665,-24.8047,-17.0319,-10.8034,-4.68532],'J/(mol*K)'),
        H298 = (449.093,'kJ/mol'),
        S298 = (191.929,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_6_6_ene_4 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s3_6_6_diene",
    group = "OR{s3_6_6_diene_0_m, s3_6_6_diene_0_2, s3_6_6_diene_0_3, s3_6_6_diene_0_4, s3_6_6_diene_0_5, s3_6_6_diene_0_6, s3_6_6_diene_1_m, s3_6_6_diene_1_5, s3_6_6_diene_1_6, s3_6_6_diene_1_8}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 169,
    label = "s3_6_6_diene_0_m",
    group = 
"""
1   R!H u0 {3,S} {4,D} {5,S}
2   R!H u0 {3,D} {6,S} {7,S}
3   R!H u0 {1,S} {2,D}
4 * R!H u0 {1,D} {9,S}
5   R!H u0 {1,S} {8,S}
6   R!H u0 {2,S} {9,S}
7   R!H u0 {2,S} {8,S}
8   R!H u0 {5,S} {7,S}
9   R!H u0 {4,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-39.9064,-38.035,-34.4788,-30.3233,-21.956,-15.1636,-7.74008],'J/(mol*K)'),
        H298 = (480.046,'kJ/mol'),
        S298 = (192.008,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_6_6_diene_0_m from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 170,
    label = "s3_6_6_diene_0_2",
    group = 
"""
1   R!H u0 {3,S} {6,S} {7,S}
2   R!H u0 {3,S} {4,S} {5,D}
3   R!H u0 {1,S} {2,S}
4 * R!H u0 {2,S} {9,S}
5   R!H u0 {2,D} {8,S}
6   R!H u0 {1,S} {8,D}
7   R!H u0 {1,S} {9,S}
8   R!H u0 {5,S} {6,D}
9   R!H u0 {4,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-41.7507,-41.054,-38.0975,-33.4925,-24.951,-17.4536,-9.27396],'J/(mol*K)'),
        H298 = (159.635,'kJ/mol'),
        S298 = (194.707,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_6_6_diene_0_2 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 171,
    label = "s3_6_6_diene_0_3",
    group = 
"""
1   R!H u0 {3,S} {6,S} {7,D}
2   R!H u0 {3,S} {4,D} {5,S}
3   R!H u0 {1,S} {2,S}
4 * R!H u0 {2,D} {9,S}
5   R!H u0 {2,S} {8,S}
6   R!H u0 {1,S} {8,S}
7   R!H u0 {1,D} {9,S}
8   R!H u0 {5,S} {6,S}
9   R!H u0 {4,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-36.4904,-33.8182,-29.7564,-25.8412,-18.7638,-13.343,-6.10632],'J/(mol*K)'),
        H298 = (212.164,'kJ/mol'),
        S298 = (171.661,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_6_6_diene_0_3 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 172,
    label = "s3_6_6_diene_0_4",
    group = 
"""
1   R!H u0 {3,S} {5,S} {7,D}
2   R!H u0 {3,S} {4,S} {6,D}
3   R!H u0 {1,S} {2,S}
4 * R!H u0 {2,S} {9,S}
5   R!H u0 {1,S} {8,S}
6   R!H u0 {2,D} {8,S}
7   R!H u0 {1,D} {9,S}
8   R!H u0 {5,S} {6,S}
9   R!H u0 {4,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-35.8668,-33.3357,-29.6275,-25.9707,-19.1327,-13.5237,-6.4542],'J/(mol*K)'),
        H298 = (193.512,'kJ/mol'),
        S298 = (167.901,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_6_6_diene_0_4 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 173,
    label = "s3_6_6_diene_0_5",
    group = 
"""
1   R!H u0 {3,S} {4,S} {7,S}
2   R!H u0 {3,S} {5,D} {6,S}
3   R!H u0 {1,S} {2,S}
4 * R!H u0 {1,S} {9,S}
5   R!H u0 {2,D} {9,S}
6   R!H u0 {2,S} {8,S}
7   R!H u0 {1,S} {8,D}
8   R!H u0 {6,S} {7,D}
9   R!H u0 {4,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-36.0971,-34.0457,-30.7062,-26.6639,-19.9177,-13.9307,-6.89608],'J/(mol*K)'),
        H298 = (116.979,'kJ/mol'),
        S298 = (177.925,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_6_6_diene_0_5 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 174,
    label = "s3_6_6_diene_0_6",
    group = 
"""
1   R!H u0 {3,S} {6,S} {7,S}
2   R!H u0 {3,S} {4,D} {5,S}
3   R!H u0 {1,S} {2,S}
4 * R!H u0 {2,D} {8,S}
5   R!H u0 {2,S} {9,D}
6   R!H u0 {1,S} {8,S}
7   R!H u0 {1,S} {9,S}
8   R!H u0 {4,S} {6,S}
9   R!H u0 {5,D} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-40.8277,-38.867,-35.5841,-31.8915,-23.871,-16.8376,-9.39096],'J/(mol*K)'),
        H298 = (414.371,'kJ/mol'),
        S298 = (192.642,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_6_6_diene_0_6 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 175,
    label = "s3_6_6_diene_1_m",
    group = 
"""
1   R!H u0 {3,D} {6,S} {7,S}
2   R!H u0 {3,S} {4,S} {5,S}
3   R!H u0 {1,D} {2,S}
4 * R!H u0 {2,S} {9,D}
5   R!H u0 {2,S} {8,S}
6   R!H u0 {1,S} {8,S}
7   R!H u0 {1,S} {9,S}
8   R!H u0 {5,S} {6,S}
9   R!H u0 {4,D} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-40.4851,-35.1412,-30.136,-25.8755,-18.0682,-12.3311,-5.67248],'J/(mol*K)'),
        H298 = (261.359,'kJ/mol'),
        S298 = (186.547,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_6_6_diene_1_m from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 176,
    label = "s3_6_6_diene_1_5",
    group = 
"""
1   R!H u0 {3,S} {4,S} {6,S}
2   R!H u0 {3,S} {5,S} {7,S}
3   R!H u0 {1,S} {2,S}
4 * R!H u0 {1,S} {9,S}
5   R!H u0 {2,S} {9,D}
6   R!H u0 {1,S} {8,D}
7   R!H u0 {2,S} {8,S}
8   R!H u0 {6,D} {7,S}
9   R!H u0 {4,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-35.0388,-33.6712,-31.392,-27.4376,-21.1105,-14.6073,-7.78784],'J/(mol*K)'),
        H298 = (41.2142,'kJ/mol'),
        S298 = (177.784,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_6_6_diene_1_5 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 177,
    label = "s3_6_6_diene_1_6",
    group = 
"""
1   R!H u0 {3,S} {5,S} {6,S}
2   R!H u0 {3,S} {4,S} {7,S}
3   R!H u0 {1,S} {2,S}
4 * R!H u0 {2,S} {9,S}
5   R!H u0 {1,S} {9,D}
6   R!H u0 {1,S} {8,D}
7   R!H u0 {2,S} {8,S}
8   R!H u0 {6,D} {7,S}
9   R!H u0 {4,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-40.1728,-36.2497,-32.0185,-28.0902,-20.4641,-14.0107,-7.23424],'J/(mol*K)'),
        H298 = (56.6206,'kJ/mol'),
        S298 = (198.656,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_6_6_diene_1_6 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 178,
    label = "s3_6_6_diene_1_8",
    group = 
"""
1   R!H u0 {3,S} {4,S} {6,S}
2   R!H u0 {3,D} {5,S} {7,S}
3   R!H u0 {1,S} {2,D}
4 * R!H u0 {1,S} {8,S}
5   R!H u0 {2,S} {8,D}
6   R!H u0 {1,S} {9,S}
7   R!H u0 {2,S} {9,S}
8   R!H u0 {4,S} {5,D}
9   R!H u0 {6,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-39.8147,-39.201,-36.5305,-32.1675,-23.902,-16.6376,-8.84996],'J/(mol*K)'),
        H298 = (273.832,'kJ/mol'),
        S298 = (198.59,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_6_6_diene_1_8 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s3_6_7",
    group = 
"""
1    R!H u0 {3,[S,D,T,B]} {6,[S,D,T,B]} {7,[S,D,T,B]}
2    R!H u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3    R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4  * R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
5    R!H u0 {2,[S,D,T,B]} {9,[S,D,T,B]}
6    R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
7    R!H u0 {1,[S,D,T,B]} {10,[S,D,T,B]}
8    R!H u0 {4,[S,D,T,B]} {6,[S,D,T,B]}
9    R!H u0 {5,[S,D,T,B]} {10,[S,D,T,B]}
10   R!H u0 {7,[S,D,T,B]} {9,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 186,
    label = "s3_6_7_ane",
    group = 
"""
1    R!H u0 {3,S} {6,S} {7,S}
2    R!H u0 {3,S} {4,S} {5,S}
3    R!H u0 {1,S} {2,S}
4  * R!H u0 {2,S} {8,S}
5    R!H u0 {2,S} {9,S}
6    R!H u0 {1,S} {8,S}
7    R!H u0 {1,S} {10,S}
8    R!H u0 {4,S} {6,S}
9    R!H u0 {5,S} {10,S}
10   R!H u0 {7,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-52.0757,-47.7534,-42.6136,-36.6226,-24.3801,-14.2979,-2.76456],'J/(mol*K)'),
        H298 = (80.8622,'kJ/mol'),
        S298 = (157.986,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_6_7_ane from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s3_6_7_ene",
    group = "OR{s3_6_7_ene_6}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 187,
    label = "s3_6_7_ene_6",
    group = 
"""
1    R!H u0 {3,S} {6,S} {7,S}
2    R!H u0 {3,S} {4,S} {5,S}
3    R!H u0 {1,S} {2,S}
4    R!H u0 {2,S} {9,S}
5  * R!H u0 {2,S} {8,D}
6    R!H u0 {1,S} {10,S}
7    R!H u0 {1,S} {8,S}
8    R!H u0 {5,D} {7,S}
9    R!H u0 {4,S} {10,S}
10   R!H u0 {6,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-46.6388,-42.4017,-37.8678,-32.5923,-22.7928,-14.1219,-4.4222],'J/(mol*K)'),
        H298 = (184.655,'kJ/mol'),
        S298 = (156.543,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_6_7_ene_6 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s3_6_7_diene",
    group = "OR{s3_6_7_diene_6_9-0}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 188,
    label = "s3_6_7_diene_6_9-0",
    group = 
"""
1    R!H u0 {3,D} {4,S} {7,S}
2    R!H u0 {3,S} {5,S} {6,S}
3    R!H u0 {1,D} {2,S}
4    R!H u0 {1,S} {10,S}
5  * R!H u0 {2,S} {8,D}
6    R!H u0 {2,S} {9,S}
7    R!H u0 {1,S} {8,S}
8    R!H u0 {5,D} {7,S}
9    R!H u0 {6,S} {10,S}
10   R!H u0 {4,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-40.7561,-34.753,-29.908,-25.4219,-16.5741,-10.1356,-2.73148],'J/(mol*K)'),
        H298 = (447.124,'kJ/mol'),
        S298 = (169.068,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_6_7_diene_6_9-0 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s4_6_6",
    group = 
"""
1 * R!H u0 {3,[S,D,T,B]} {6,[S,D,T,B]} {8,[S,D,T,B]}
2   R!H u0 {4,[S,D,T,B]} {5,[S,D,T,B]} {7,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]}
5   R!H u0 {2,[S,D,T,B]} {6,[S,D,T,B]}
6   R!H u0 {1,[S,D,T,B]} {5,[S,D,T,B]}
7   R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
8   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 179,
    label = "s4_6_6_ane",
    group = 
"""
1 * R!H u0 {3,S} {6,S} {8,S}
2   R!H u0 {4,S} {5,S} {7,S}
3   R!H u0 {1,S} {4,S}
4   R!H u0 {2,S} {3,S}
5   R!H u0 {2,S} {6,S}
6   R!H u0 {1,S} {5,S}
7   R!H u0 {2,S} {8,S}
8   R!H u0 {1,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-12,-11.01,-8.96,-6.42,-3.03,-2.4,0.05],'cal/(mol*K)'),
        H298 = (7.4,'kcal/mol'),
        S298 = (48.92,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Wiberg, K. Angew. Chem., Int. Ed. Engl. 1986, 25, 312 1986 experimental S, Cp from PM7 calculation
""",
)

entry(
    index = 0,
    label = "s4_6_8",
    group = 
"""
1    R!H u0 {4,[S,D,T,B]} {5,[S,D,T,B]} {7,[S,D,T,B]}
2    R!H u0 {3,[S,D,T,B]} {6,[S,D,T,B]} {8,[S,D,T,B]}
3  * R!H u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
5    R!H u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H u0 {2,[S,D,T,B]} {5,[S,D,T,B]}
7    R!H u0 {1,[S,D,T,B]} {10,[S,D,T,B]}
8    R!H u0 {2,[S,D,T,B]} {9,[S,D,T,B]}
9    R!H u0 {8,[S,D,T,B]} {10,[S,D,T,B]}
10   R!H u0 {7,[S,D,T,B]} {9,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 189,
    label = "s4_6_8_ane",
    group = 
"""
1    R!H u0 {4,S} {5,S} {7,S}
2    R!H u0 {3,S} {6,S} {8,S}
3  * R!H u0 {2,S} {4,S}
4    R!H u0 {1,S} {3,S}
5    R!H u0 {1,S} {6,S}
6    R!H u0 {2,S} {5,S}
7    R!H u0 {1,S} {10,S}
8    R!H u0 {2,S} {9,S}
9    R!H u0 {8,S} {10,S}
10   R!H u0 {7,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-46.2777,-42.7734,-38.8706,-33.5046,-22.3041,-13.1179,-3.02056],'J/(mol*K)'),
        H298 = (292.061,'kJ/mol'),
        S298 = (169.335,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s4_6_8_ane from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s4_6_8_ene",
    group = "OR{s4_6_8_ene_7}",
    thermo = None,
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 190,
    label = "s4_6_8_ene_7",
    group = 
"""
1    R!H u0 {3,S} {4,S} {8,S}
2    R!H u0 {5,D} {6,S} {7,S}
3  * R!H u0 {1,S} {5,S}
4    R!H u0 {1,S} {6,S}
5    R!H u0 {2,D} {3,S}
6    R!H u0 {2,S} {4,S}
7    R!H u0 {2,S} {9,S}
8    R!H u0 {1,S} {10,S}
9    R!H u0 {7,S} {10,S}
10   R!H u0 {8,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-44.5304,-41.3997,-37.2241,-32.1561,-21.8408,-13.2809,-3.36732],'J/(mol*K)'),
        H298 = (136.419,'kJ/mol'),
        S298 = (159.81,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s4_6_8_ene_7 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 0,
    label = "s4_6_8_diene",
    group = "OR{s4_6_8_diene_7_9}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 191,
    label = "s4_6_8_diene_7_9",
    group = 
"""
1    R!H u0 {3,D} {5,S} {7,S}
2    R!H u0 {4,S} {6,S} {8,S}
3  * R!H u0 {1,D} {4,S}
4    R!H u0 {2,S} {3,S}
5    R!H u0 {1,S} {6,D}
6    R!H u0 {2,S} {5,D}
7    R!H u0 {1,S} {10,S}
8    R!H u0 {2,S} {9,S}
9    R!H u0 {8,S} {10,S}
10   R!H u0 {7,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-43.5867,-42.4018,-39.4395,-34.4239,-24.4858,-15.9891,-6.57996],'J/(mol*K)'),
        H298 = (144.295,'kJ/mol'),
        S298 = (176.495,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s4_6_8_diene_7_9 from Bicyclics_QM_190_isomorphic library.
""",
)

entry(
    index = 3,
    label = "s2-3_5_5_5_ane",
    group = 
"""
1    R!H u0 {2,S} {4,S} {9,S}
2    R!H u0 {1,S} {3,S} {8,S}
3  * R!H u0 {2,S} {5,S} {6,S}
4    R!H u0 {1,S} {5,S} {7,S}
5    R!H u0 {3,S} {4,S}
6    R!H u0 {3,S} {7,S}
7    R!H u0 {4,S} {6,S}
8    R!H u0 {2,S} {10,S}
9    R!H u0 {1,S} {10,S}
10   R!H u0 {8,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-15.018,-13.783,-12.193,-10.63,-8.502,-6.688,-4.111],'cal/(mol*K)'),
        H298 = (17.68,'kcal/mol'),
        S298 = (78.53,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Modified Aaron G. Vandeputte to make estimates in agreement with value of Hudzik et al. 2010
""",
)

entry(
    index = 4,
    label = "s2-3_5d1_5_5_ene",
    group = 
"""
1    R!H u0 {2,S} {4,S} {9,S}
2    R!H u0 {1,S} {3,S} {8,S}
3  * R!H u0 {2,S} {5,S} {6,S}
4    R!H u0 {1,S} {5,S} {7,S}
5    R!H u0 {3,S} {4,S}
6    R!H u0 {3,S} {7,S}
7    R!H u0 {4,S} {6,S}
8    R!H u0 {2,S} {10,D}
9    R!H u0 {1,S} {10,S}
10   R!H u0 {8,D} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-15.018,-13.783,-12.193,-10.63,-8.502,-6.688,-4.111],'cal/(mol*K)'),
        H298 = (22.65,'kcal/mol'),
        S298 = (78.53,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Automated Estimation of Ring Strain Energies, Gasteiger, 1978 S, Cp from exo-tricyclo[5.2.1.0(2.6)]decane
""",
)

entry(
    index = 5,
    label = "s2-3f0_5_5_5_ane",
    group = 
"""
1  * R!H u0 {2,S} {4,S} {6,S} {7,S}
2    R!H u0 {1,S} {5,S} {8,S}
3    R!H u0 {4,S} {5,S} {9,S}
4    R!H u0 {1,S} {3,S}
5    R!H u0 {2,S} {3,S}
6    R!H u0 {1,S} {9,S}
7    R!H u0 {1,S} {10,S}
8    R!H u0 {2,S} {10,S}
9    R!H u0 {3,S} {6,S}
10   R!H u0 {7,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-15.018,-13.783,-12.193,-10.63,-8.502,-6.688,-4.111],'cal/(mol*K)'),
        H298 = (23.86,'kcal/mol'),
        S298 = (78.53,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Automated Estimation of Ring Strain Energies, Gasteiger, 1978 S, Cp from exo-tricyclo[5.2.1.0(2.6)]decane
""",
)

entry(
    index = 6,
    label = "s2-3f1_6_5_5_ane",
    group = 
"""
1    R!H u0 {2,S} {3,S} {5,S}
2    R!H u0 {1,S} {7,S} {8,S}
3    R!H u0 {1,S} {6,S} {9,S}
4  * R!H u0 {5,S} {6,S} {7,S}
5    R!H u0 {1,S} {4,S}
6    R!H u0 {3,S} {4,S}
7    R!H u0 {2,S} {4,S}
8    R!H u0 {2,S} {10,S}
9    R!H u0 {3,S} {10,S}
10   R!H u0 {8,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-15.018,-13.783,-12.193,-10.63,-8.502,-6.688,-4.111],'cal/(mol*K)'),
        H298 = (19.26,'kcal/mol'),
        S298 = (78.53,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Automated Estimation of Ring Strain Energies, Gasteiger, 1978 S, Cp from exo-tricyclo[5.2.1.0(2.6)]decane
""",
)

entry(
    index = 8,
    label = "s2-3_5_5_5d1_ene",
    group = 
"""
1    R!H u0 {2,S} {3,S} {8,S}
2    R!H u0 {1,S} {4,S} {9,S}
3  * R!H u0 {1,S} {5,S} {7,S}
4    R!H u0 {2,S} {5,S} {6,S}
5    R!H u0 {3,S} {4,S}
6    R!H u0 {4,S} {7,D}
7    R!H u0 {3,S} {6,D}
8    R!H u0 {1,S} {10,S}
9    R!H u0 {2,S} {10,S}
10   R!H u0 {8,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-12.29,-11.16,-10.04,-8.64,-7.12,-5.72,-3.81],'cal/(mol*K)'),
        H298 = (22.83,'kcal/mol'),
        S298 = (79.45,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
A. G. Vandeputte CBS-QB3 isodesmic reaction, S and cp match B3LYP/cbsb7 data, CHECK
""",
)

entry(
    index = 72,
    label = "s3-3_5_6_5_ane",
    group = 
"""
1  * R!H u0 {2,S} {6,S} {8,S}
2    R!H u0 {1,S} {5,S} {9,S}
3    R!H u0 {4,S} {5,S} {10,S}
4    R!H u0 {3,S} {6,S} {7,S}
5    R!H u0 {2,S} {3,S}
6    R!H u0 {1,S} {4,S}
7    R!H u0 {4,S} {8,S}
8    R!H u0 {1,S} {7,S}
9    R!H u0 {2,S} {10,S}
10   R!H u0 {3,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-15.1,-13.4,-11.6,-10,-7.8,-6.1,-3.7],'cal/(mol*K)'),
        H298 = (22.5,'kcal/mol'),
        S298 = (77.13,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
A.G Vandeputte CBS-QB3, reaction JP10 <-> tricyclo[4.2.1.1(2.5)]decane
""",
)

entry(
    index = 13,
    label = "s2-4f1_5_6_7_ane",
    group = 
"""
1    R!H u0 {2,S} {3,S} {7,S}
2  * R!H u0 {1,S} {5,S} {8,S}
3    R!H u0 {1,S} {6,S} {9,S}
4    R!H u0 {5,S} {6,S} {10,S}
5    R!H u0 {2,S} {4,S}
6    R!H u0 {3,S} {4,S}
7    R!H u0 {1,S} {10,S}
8    R!H u0 {2,S} {9,S}
9    R!H u0 {3,S} {8,S}
10   R!H u0 {4,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-15.58,-14.7,-12.37,-9.37,-5.42,-4.64,-1.58],'cal/(mol*K)'),
        H298 = (20.77,'kcal/mol'),
        S298 = (78.58,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Automated Estimation of Ring Strain Energies, Gasteiger, 1978 S, Cp from PM7
""",
)

entry(
    index = 14,
    label = "s2-4f2_5_6_8_ane",
    group = 
"""
1  * R!H u0 {2,S} {5,S} {6,S}
2    R!H u0 {1,S} {7,S} {9,S}
3    R!H u0 {5,S} {7,S} {8,S}
4    R!H u0 {6,S} {8,S} {10,S}
5    R!H u0 {1,S} {3,S}
6    R!H u0 {1,S} {4,S}
7    R!H u0 {2,S} {3,S}
8    R!H u0 {3,S} {4,S}
9    R!H u0 {2,S} {10,S}
10   R!H u0 {4,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-16.03,-15.03,-12.57,-9.46,-5.47,-4.74,-1.59],'cal/(mol*K)'),
        H298 = (18.29,'kcal/mol'),
        S298 = (75.75,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Automated Estimation of Ring Strain Energies, Gasteiger, 1978 S, Cp from PM7
""",
)

entry(
    index = 32,
    label = "s2-2f1_5_5_2_ane",
    group = 
"""
1    R!H u0 {2,S} {3,S} {4,S}
2  * R!H u0 {1,S} {5,S} {10,S}
3    R!H u0 {1,S} {6,S} {7,S}
4    R!H u0 {1,S} {8,S} {9,S}
5    R!H u0 {2,S} {6,S}
6    R!H u0 {3,S} {5,S}
7    R!H u0 {3,S} {8,S}
8    R!H u0 {4,S} {7,S}
9    R!H u0 {4,S} {10,S}
10   R!H u0 {2,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-15.018,-13.783,-12.193,-10.63,-8.502,-6.688,-4.111],'cal/(mol*K)'),
        H298 = (15.68,'kcal/mol'),
        S298 = (78.53,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Modified Aaron G. Vandeputte, kept enthalpy Nick Vandewiele, modified S and cp to be equal to exo-tricyclo[5.2.1.0(2.6)]
""",
)

entry(
    index = 33,
    label = "s2-3f1_5_5_6_ane",
    group = 
"""
1    R!H u0 {2,S} {3,S} {5,S}
2  * R!H u0 {1,S} {6,S} {7,S}
3    R!H u0 {1,S} {8,S} {9,S}
4    R!H u0 {5,S} {6,S} {10,S}
5    R!H u0 {1,S} {4,S}
6    R!H u0 {2,S} {4,S}
7    R!H u0 {2,S} {8,S}
8    R!H u0 {3,S} {7,S}
9    R!H u0 {3,S} {10,S}
10   R!H u0 {4,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-15.6,-14.69,-12.36,-9.34,-5.4,-4.64,-1.58],'cal/(mol*K)'),
        H298 = (21.48,'kcal/mol'),
        S298 = (78.96,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Automated Estimation of Ring Strain Energies, Gasteiger, 1978 S, Cp from PM7
""",
)

entry(
    index = 34,
    label = "s2-4f0_5_5_6_ane",
    group = 
"""
1  * R!H u0 {2,S} {4,S} {5,S} {6,S}
2    R!H u0 {1,S} {3,S} {7,S}
3    R!H u0 {2,S} {8,S} {9,S}
4    R!H u0 {1,S} {8,S}
5    R!H u0 {1,S} {9,S}
6    R!H u0 {1,S} {10,S}
7    R!H u0 {2,S} {10,S}
8    R!H u0 {3,S} {4,S}
9    R!H u0 {3,S} {5,S}
10   R!H u0 {6,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-15.15,-14.51,-12.47,-9.72,-5.97,-5.19,-1.39],'cal/(mol*K)'),
        H298 = (29.65,'kcal/mol'),
        S298 = (82.23,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Automated Estimation of Ring Strain Energies, Gasteiger, 1978 S, Cp from PM7
""",
)

entry(
    index = 35,
    label = "s2-4f1_5_5_7_ane",
    group = 
"""
1  * R!H u0 {2,S} {3,S} {6,S}
2    R!H u0 {1,S} {4,S} {5,S}
3    R!H u0 {1,S} {7,S} {8,S}
4    R!H u0 {2,S} {9,S} {10,S}
5    R!H u0 {2,S} {7,S}
6    R!H u0 {1,S} {10,S}
7    R!H u0 {3,S} {5,S}
8    R!H u0 {3,S} {9,S}
9    R!H u0 {4,S} {8,S}
10   R!H u0 {4,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-15.5,-14.55,-12.19,-9.17,-5.28,-4.57,-1.53],'cal/(mol*K)'),
        H298 = (20.74,'kcal/mol'),
        S298 = (77.45,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Automated Estimation of Ring Strain Energies, Gasteiger, 1978 S, Cp from PM7
""",
)

entry(
    index = 69,
    label = "s4-3f1_6_6_6_ane",
    group = 
"""
1  * R!H u0 {3,S} {6,S} {7,S}
2    R!H u0 {4,S} {5,S} {8,S}
3    R!H u0 {1,S} {5,S} {9,S}
4    R!H u0 {2,S} {6,S} {10,S}
5    R!H u0 {2,S} {3,S}
6    R!H u0 {1,S} {4,S}
7    R!H u0 {1,S} {8,S}
8    R!H u0 {2,S} {7,S}
9    R!H u0 {3,S} {10,S}
10   R!H u0 {4,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-16.13,-15.02,-12.47,-9.29,-5.32,-4.7,-1.53],'cal/(mol*K)'),
        H298 = (26.12,'kcal/mol'),
        S298 = (75.25,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Automated Estimation of Ring Strain Energies, Gasteiger, 1978 S, Cp copied from cyclohexane
""",
)

entry(
    index = 67,
    label = "s3-3f1_6_5_6_ane",
    group = 
"""
1  * R!H u0 {4,S} {5,S} {6,S}
2    R!H u0 {3,S} {5,S} {7,S}
3    R!H u0 {2,S} {6,S} {10,S}
4    R!H u0 {1,S} {8,S} {9,S}
5    R!H u0 {1,S} {2,S}
6    R!H u0 {1,S} {3,S}
7    R!H u0 {2,S} {8,S}
8    R!H u0 {4,S} {7,S}
9    R!H u0 {4,S} {10,S}
10   R!H u0 {3,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-16.09,-14.97,-12.4,-9.23,-5.27,-4.66,-1.5],'cal/(mol*K)'),
        H298 = (30.9,'kcal/mol'),
        S298 = (75.36,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Automated Estimation of Ring Strain Energies, Gasteiger, 1978 S, Cp copied from cyclopentane
""",
)

entry(
    index = 0,
    label = "s2_4_4_diene",
    group = "OR{s2_4_4_diene_1_m}",
    thermo = None,
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 75,
    label = "s2_4_4_diene_1_m",
    group =
"""
1   R!H u0 {2,D} {4,S} {6,S}
2   R!H u0 {1,D} {3,S} {5,S}
3 * R!H u0 {2,S} {4,S}
4   R!H u0 {1,S} {3,S}
5   R!H u0 {2,S} {6,D}
6   R!H u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.911294694, -6.76788695, -7.426491396, -7.70704517, -6.76857218, -4.65110325, -4.246702677],'cal/(mol*K)'),
        H298 = (134.9052041,'kcal/mol'),
        S298 = (69.47292352,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
Fitted to M06 calculations
""",
)

entry(
    index = 76,
    label = "s2_3_6_ene_5",
    group =
"""
1   R!H u0 {2,S} {3,D} {4,S}
2   R!H u0 {1,S} {3,S} {5,S}
3   R!H u0 {1,D} {2,S}
4   R!H u0 {1,S} {7,S}
5   R!H u0 {2,S} {6,S}
6 * R!H u0 {5,S} {7,S}
7   R!H u0 {4,S} {6,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-33.0644, -30.4388, -27.9344, -25.2475, -19.6467, -15.2896, -10.1737], 'J/(mol*K)'),
        H298=(262.495, 'kJ/mol'),
        S298=(238.794, 'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
Fitted to M06 calculations
""",
)

entry(
    index = 77,
    label = "s2_3_6_diene_2_5",
    group =
"""
1   R!H u0 {2,S} {3,D} {4,S}
2   R!H u0 {1,S} {3,S} {5,S}
3   R!H u0 {1,D} {2,S}
4   R!H u0 {1,S} {7,S}
5   R!H u0 {2,S} {6,S}
6 * R!H u0 {5,S} {7,D}
7   R!H u0 {4,S} {6,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-25.6671, -24.8396, -23.399, -21.6937, -17.9095, -14.865, -11.0665], 'J/(mol*K)'),
        H298=(259.334, 'kJ/mol'),
        S298=(242.952, 'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
Fitted to M06 calculations
""",
)

entry(
    index = 0,
    label = "s3_5_6_ben_ane",
    group = "OR{s3_5_6_ben_ane_res1, s3_5_6_ben_ane_res2}",
    thermo = None,
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 78,
    label = "s3_5_6_ben_ane_res1",
    group =
"""
1   R!H u0 {3,B} {5,S} {6,B}
2   R!H u0 {3,B} {4,S} {7,B}
3   R!H u0 {1,B} {2,B}
4   R!H u0 {2,S} {5,S}
5   R!H u0 {1,S} {4,S}
6   R!H u0 {1,B} {8,B}
7   R!H u0 {2,B} {8,B}
8 * R!H u0 {6,B} {7,B}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.469, -0.262, -0.442, -0.825, -0.747, 0.339, 0.354], 'cal/(mol*K)'),
        H298=(166.291, 'kcal/mol'),
        S298=(30.103, 'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
Fitted to CBS-QB3 calculations
""",
)

entry(
    index = 78,
    label = "s3_5_6_ben_ane_res2",
    group =
"""
1   R!H u0 {3,S} {5,S} {6,D}
2   R!H u0 {3,D} {4,S} {7,S}
3   R!H u0 {1,S} {2,D}
4   R!H u0 {2,S} {5,S}
5   R!H u0 {1,S} {4,S}
6   R!H u0 {1,D} {8,S}
7   R!H u0 {2,S} {8,D}
8 * R!H u0 {6,S} {7,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-7.466, -8.33, -8.73, -8.665, -6.596, -3.859, -3.506], 'cal/(mol*K)'),
        H298=(145.431, 'kcal/mol'),
        S298=(63.603, 'cal/(mol*K)'),
    ),
    shortDesc=u"""""",
    longDesc=
    u"""
    Fitted to CBS-QB3 calculations
    """,
)

entry(
    index = 0,
    label = "s3_5_6_ben_ene",
    group = "OR{s3_5_6_ben_ene_res1, s3_5_6_ben_ene_res2}",
    thermo = None,
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 79,
    label = "s3_5_6_ben_ene_res1",
    group =
"""
1   R!H u0 {3,B} {5,S} {6,B}
2   R!H u0 {3,B} {4,S} {7,B}
3   R!H u0 {1,B} {2,B}
4   R!H u0 {2,S} {5,D}
5   R!H u0 {1,S} {4,D}
6   R!H u0 {1,B} {8,B}
7   R!H u0 {2,B} {8,B}
8 * R!H u0 {6,B} {7,B}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-7.96404, -8.74552, -8.7074, -8.03332, -5.94428, -4.49956, -4.93892], 'J/(mol*K)'),
        H298=(708.321, 'kJ/mol'),
        S298=(145.354, 'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
Fitted to M06 calculations
""",
)

entry(
    index = 80,
    label = "s3_5_6_ben_ene_res2",
    group =
"""
1   R!H u0 {3,S} {5,S} {6,D}
2   R!H u0 {3,D} {4,S} {7,S}
3   R!H u0 {1,S} {2,D}
4   R!H u0 {2,S} {5,D}
5   R!H u0 {1,S} {4,D}
6   R!H u0 {1,D} {8,S}
7   R!H u0 {2,S} {8,D}
8 * R!H u0 {6,S} {7,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-14.24, -20.6281, -22.933, -23.0957, -21.9272, -19.2272, -22.6791], 'J/(mol*K)'),
        H298=(600.625, 'kJ/mol'),
        S298=(297.401, 'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
Fitted to M06 calculations
""",
)

entry(
    index = 0,
    label = "s2_3_(1_2_CPD)",
    group="OR{s2_3_5_diene_1_2, s2_3_5_diene_0_1}",
    thermo=None,
    shortDesc = u"""Should capture all 1,2-CPD containing s2_3_5 bicyclics""",
    longDesc =
u"""

""",
)

entry(
    index = 81,
    label = "s2_3_5_diene_1_2",
    group =
"""
1 * R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {6,D}
5   R!H u0 {1,[S,D,T,B]} {6,D}
6   R!H u0 {4,D} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.613047801, -5.125049713, -5.284617591, -5.291850861, -4.885019121, -3.867795411, -3.991783938],'cal/(mol*K)'),
        H298 = (96.80534417,'kcal/mol'),
        S298 = (59.04001913,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained 1,2-cyclopentadiene ring:
polycyclic(s2_3_5_diene_1_2) = polycyclic(s2_3_5_ane) - ring(Cyclopentane) + ring(1,2-Cyclopentadiene)
""",
)

entry(
    index = 183,
    label = "s2_3_5_diene_0_1",
    group =
"""
1 * R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {4,D}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {2,D} {6,D}
5   R!H u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
6   R!H u0 {4,D} {5,[S,D,T,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.613047801, -5.125049713, -5.284617591, -5.291850861, -4.885019121, -3.867795411, -3.991783938],'cal/(mol*K)'),
        H298 = (96.80534417,'kcal/mol'),
        S298 = (59.04001913,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained 1,2-cyclopentadiene ring:
polycyclic(s2_3_5_diene_1_2) = polycyclic(s2_3_5_ane) - ring(Cyclopentane) + ring(1,2-Cyclopentadiene)
""",
)

# entry(
#     index = 184,
#     label = "s2_3_5_diene_m_0",
#     group =
# """
# 1 * R!H u0 {2,D} {3,[S,D,T,B]} {5,[S,D,T,B]}
# 2   R!H u0 {1,D} {3,[S,D,T,B]} {4,D}
# 3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
# 4   R!H u0 {2,D} {6,[S,D,T,B]}
# 5   R!H u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
# 6   R!H u0 {4,[S,D,T,B]} {5,[S,D,T,B]}
# """,
#     thermo = ThermoData(
#         Tdata = ([300,400,500,600,800,1000,1500],'K'),
#         Cpdata = ([-4.613047801, -5.125049713, -5.284617591, -5.291850861, -4.885019121, -3.867795411, -3.991783938],'cal/(mol*K)'),
#         H298 = (96.80534417,'kcal/mol'),
#         S298 = (59.04001913,'cal/(mol*K)'),
#     ),
#     shortDesc = u"""Estimated""",
#     longDesc =
# u"""
# Estimated according to the following equation in order to take into account the highly strained 1,2-cyclopentadiene ring:
# polycyclic(s2_3_5_diene_1_2) = polycyclic(s2_3_5_ane) - ring(Cyclopentane) + ring(1,2-Cyclopentadiene)
# """,
# )

entry(
    index = 0,
    label = "s2_4_(1_2_CPD)",
    group="OR{s2_4_5_diene_1_2, s2_4_5_diene_0_1}",
    thermo=None,
    shortDesc = u"""Should capture all 1,2-CPD containing s2_4_5 bicyclics""",
    longDesc =
u"""

""",
)

entry(
    index = 82,
    label = "s2_4_5_diene_1_2",
    group =
"""
1 * R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {7,D}
6   R!H u0 {2,[S,D,T,B]} {7,D}
7   R!H u0 {5,D} {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.057574569, -6.305690249, -6.204311664, -5.94849522, -5.019794456, -3.632040153, -3.328294455],'cal/(mol*K)'),
        H298 = (97.43942638,'kcal/mol'),
        S298 = (52.56487572,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained 1,2-cyclopentadiene ring:
polycyclic(s2_4_5_diene_1_2) = polycyclic(s2_4_5_ane) - ring(Cyclopentane) + ring(1,2-Cyclopentadiene)
""",
)

entry(
    index = 185,
    label = "s2_4_5_diene_0_1",
    group =
"""
1 * R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,D}
2   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]}
5   R!H u0 {1,D} {7,D}
6   R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
7   R!H u0 {5,D} {6,[S,D,T,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.057574569, -6.305690249, -6.204311664, -5.94849522, -5.019794456, -3.632040153, -3.328294455],'cal/(mol*K)'),
        H298 = (97.43942638,'kcal/mol'),
        S298 = (52.56487572,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained 1,2-cyclopentadiene ring:
polycyclic(s2_4_5_diene_1_2) = polycyclic(s2_4_5_ane) - ring(Cyclopentane) + ring(1,2-Cyclopentadiene)
""",
)

# entry(
#     index = 186,
#     label = "s2_4_5_diene_m_0",
#     group =
# """
# 1 * R!H u0 {2,D} {3,[S,D,T,B]} {5,D}
# 2   R!H u0 {1,D} {4,[S,D,T,B]} {6,[S,D,T,B]}
# 3   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]}
# 4   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]}
# 5   R!H u0 {1,D} {7,[S,D,T,B]}
# 6   R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
# 7   R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
# """,
#     thermo = ThermoData(
#         Tdata = ([300,400,500,600,800,1000,1500],'K'),
#         Cpdata = ([-6.057574569, -6.305690249, -6.204311664, -5.94849522, -5.019794456, -3.632040153, -3.328294455],'cal/(mol*K)'),
#         H298 = (97.43942638,'kcal/mol'),
#         S298 = (52.56487572,'cal/(mol*K)'),
#     ),
#     shortDesc = u"""Estimated""",
#     longDesc =
# u"""
# Estimated according to the following equation in order to take into account the highly strained 1,2-cyclopentadiene ring:
# polycyclic(s2_4_5_diene_1_2) = polycyclic(s2_4_5_ane) - ring(Cyclopentane) + ring(1,2-Cyclopentadiene)
# """,
# )

entry(
    index = 0,
    label = "s2_5_(1_2_CPD)",
    group="OR{s2_5_5_diene_1_2, s2_5_5_diene_0_1}",
    thermo=None,
    shortDesc = u"""Should capture all 1,2-CPD containing s2_5_5 bicyclics""",
    longDesc =
u"""

""",
)

entry(
    index = 83,
    label = "s2_5_5_diene_1_2",
    group =
"""
1   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
3 * R!H u0 {1,[S,D,T,B]} {7,D}
4   R!H u0 {2,[S,D,T,B]} {7,D}
5   R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
6   R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
7   R!H u0 {3,D} {4,D}
8   R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.648396749, -7.612047801, -7.248527725, -6.744479924, -5.316854685, -3.569803059, -2.822319311],'cal/(mol*K)'),
        H298 = (78.45845124,'kcal/mol'),
        S298 = (46.97405354,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained 1,2-cyclopentadiene ring:
polycyclic(s2_5_5_diene_1_2) = polycyclic(s2_5_5_ane) - ring(Cyclopentane) + ring(1,2-Cyclopentadiene)
""",
)

entry(
    index = 187,
    label = "s2_5_5_diene_0_1",
    group =
"""
1   R!H u0 {2,[S,D,T,B]} {3,D} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
3 * R!H u0 {1,D} {7,D}
4   R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
6   R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
7   R!H u0 {3,D} {4,[S,D,T,B]}
8   R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.648396749, -7.612047801, -7.248527725, -6.744479924, -5.316854685, -3.569803059, -2.822319311],'cal/(mol*K)'),
        H298 = (78.45845124,'kcal/mol'),
        S298 = (46.97405354,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained 1,2-cyclopentadiene ring:
polycyclic(s2_5_5_diene_1_2) = polycyclic(s2_5_5_ane) - ring(Cyclopentane) + ring(1,2-Cyclopentadiene)
""",
)

# entry(
#     index = 188,
#     label = "s2_5_5_diene_m_0",
#     group =
# """
# 1   R!H u0 {2,D} {3,D} {5,[S,D,T,B]}
# 2   R!H u0 {1,D} {4,[S,D,T,B]} {6,[S,D,T,B]}
# 3 * R!H u0 {1,D} {7,[S,D,T,B]}
# 4   R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
# 5   R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
# 6   R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
# 7   R!H u0 {3,[S,D,T,B]} {4,[S,D,T,B]}
# 8   R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
# """,
#     thermo = ThermoData(
#         Tdata = ([300,400,500,600,800,1000,1500],'K'),
#         Cpdata = ([-7.648396749, -7.612047801, -7.248527725, -6.744479924, -5.316854685, -3.569803059, -2.822319311],'cal/(mol*K)'),
#         H298 = (78.45845124,'kcal/mol'),
#         S298 = (46.97405354,'cal/(mol*K)'),
#     ),
#     shortDesc = u"""Estimated""",
#     longDesc =
# u"""
# Estimated according to the following equation in order to take into account the highly strained 1,2-cyclopentadiene ring:
# polycyclic(s2_5_5_diene_1_2) = polycyclic(s2_5_5_ane) - ring(Cyclopentane) + ring(1,2-Cyclopentadiene)
# """,
# )

entry(
    index = 0,
    label = "s2_(1_2_CPD)_6",
    group="OR{s2_5_6_diene_6_7, s2_5_6_diene_5_6}",
    thermo=None,
    shortDesc = u"""Should capture all 1,2-CPD containing s2_5_6 bicyclics""",
    longDesc =
u"""

""",
)

entry(
    index = 84,
    label = "s2_5_6_diene_6_7",
    group =
"""
1 * R!H u0 {2,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {6,[S,D,T,B]}
3   R!H u0 {2,[S,D,T,B]} {9,[S,D,T,B]}
4   R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {7,D}
6   R!H u0 {2,[S,D,T,B]} {7,D}
7   R!H u0 {5,D} {6,D}
8   R!H u0 {4,[S,D,T,B]} {9,[S,D,T,B]}
9   R!H u0 {3,[S,D,T,B]} {8,[S,D,T,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.967230401, -8.037430211, -7.862294455, -7.275646272, -5.361500956, -3.27522849, -2.136611854],'cal/(mol*K)'),
        H298 = (74.40849904,'kcal/mol'),
        S298 = (45.28954111,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained 1,2-cyclopentadiene ring:
polycyclic(s2_5_6_diene_6_7) = polycyclic(s2_5_6_ane) - ring(Cyclopentane) + ring(1,2-Cyclopentadiene)
""",
)

entry(
    index = 189,
    label = "s2_5_6_diene_5_6",
    group =
"""
1 * R!H u0 {2,[S,D,T,B]} {4,[S,D,T,B]} {5,D}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {6,[S,D,T,B]}
3   R!H u0 {2,[S,D,T,B]} {9,[S,D,T,B]}
4   R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
5   R!H u0 {1,D} {7,D}
6   R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
7   R!H u0 {5,D} {6,[S,D,T,B]}
8   R!H u0 {4,[S,D,T,B]} {9,[S,D,T,B]}
9   R!H u0 {3,[S,D,T,B]} {8,[S,D,T,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.967230401, -8.037430211, -7.862294455, -7.275646272, -5.361500956, -3.27522849, -2.136611854],'cal/(mol*K)'),
        H298 = (74.40849904,'kcal/mol'),
        S298 = (45.28954111,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained 1,2-cyclopentadiene ring:
polycyclic(s2_5_6_diene_6_7) = polycyclic(s2_5_6_ane) - ring(Cyclopentane) + ring(1,2-Cyclopentadiene)
""",
)

# entry(
#     index = 190,
#     label = "s2_5_6_diene_m_5",
#     group =
# """
# 1 * R!H u0 {2,D} {4,[S,D,T,B]} {5,D}
# 2   R!H u0 {1,D} {3,[S,D,T,B]} {6,[S,D,T,B]}
# 3   R!H u0 {2,[S,D,T,B]} {9,[S,D,T,B]}
# 4   R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
# 5   R!H u0 {1,D} {7,[S,D,T,B]}
# 6   R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
# 7   R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
# 8   R!H u0 {4,[S,D,T,B]} {9,[S,D,T,B]}
# 9   R!H u0 {3,[S,D,T,B]} {8,[S,D,T,B]}
# """,
#     thermo = ThermoData(
#         Tdata = ([300,400,500,600,800,1000,1500],'K'),
#         Cpdata = ([-7.967230401, -8.037430211, -7.862294455, -7.275646272, -5.361500956, -3.27522849, -2.136611854],'cal/(mol*K)'),
#         H298 = (74.40849904,'kcal/mol'),
#         S298 = (45.28954111,'cal/(mol*K)'),
#     ),
#     shortDesc = u"""Estimated""",
#     longDesc =
# u"""
# Estimated according to the following equation in order to take into account the highly strained 1,2-cyclopentadiene ring:
# polycyclic(s2_5_6_diene_6_7) = polycyclic(s2_5_6_ane) - ring(Cyclopentane) + ring(1,2-Cyclopentadiene)
# """,
# )

entry(
    index = 0,
    label = "s2_(1_2_CPD)_7",
    group="OR{s2_5_7_diene_7_8, s2_5_7_diene_6_7}",
    thermo=None,
    shortDesc = u"""Should capture all 1,2-CPD containing s2_5_7 bicyclics""",
    longDesc =
u"""

""",
)

entry(
    index = 85,
    label = "s2_5_7_diene_7_8",
    group =
"""
1  * R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]}
2    R!H u0 {1,[S,D,T,B]} {5,[S,D,T,B]} {6,[S,D,T,B]}
3    R!H u0 {1,[S,D,T,B]} {7,D}
4    R!H u0 {1,[S,D,T,B]} {9,[S,D,T,B]}
5    R!H u0 {2,[S,D,T,B]} {7,D}
6    R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
7    R!H u0 {3,D} {5,D}
8    R!H u0 {6,[S,D,T,B]} {10,[S,D,T,B]}
9    R!H u0 {4,[S,D,T,B]} {10,[S,D,T,B]}
10   R!H u0 {8,[S,D,T,B]} {9,[S,D,T,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.645227533, -5.913365201, -5.9873174, -5.596732314, -5.028231358, -3.721783939, -2.722015296],'cal/(mol*K)'),
        H298 = (73.61143212,'kcal/mol'),
        S298 = (55.15890402,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained 1,2-cyclopentadiene ring:
polycyclic(s2_5_7_diene_7_8) = polycyclic(s2_5_7_triene_1_3_7) - ring(Cyclopentene) + ring(1,2-Cyclopentadiene)
""",
)

entry(
    index = 191,
    label = "s2_5_7_diene_6_7",
    group =
"""
1  * R!H u0 {2,[S,D,T,B]} {3,D} {4,[S,D,T,B]}
2    R!H u0 {1,[S,D,T,B]} {5,[S,D,T,B]} {6,[S,D,T,B]}
3    R!H u0 {1,D} {7,D}
4    R!H u0 {1,[S,D,T,B]} {9,[S,D,T,B]}
5    R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
6    R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
7    R!H u0 {3,D} {5,[S,D,T,B]}
8    R!H u0 {6,[S,D,T,B]} {10,[S,D,T,B]}
9    R!H u0 {4,[S,D,T,B]} {10,[S,D,T,B]}
10   R!H u0 {8,[S,D,T,B]} {9,[S,D,T,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.645227533, -5.913365201, -5.9873174, -5.596732314, -5.028231358, -3.721783939, -2.722015296],'cal/(mol*K)'),
        H298 = (73.61143212,'kcal/mol'),
        S298 = (55.15890402,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained 1,2-cyclopentadiene ring:
polycyclic(s2_5_7_diene_7_8) = polycyclic(s2_5_7_triene_1_3_7) - ring(Cyclopentene) + ring(1,2-Cyclopentadiene)
""",
)

# entry(
#     index = 192,
#     label = "s2_5_7_diene_m_6",
#     group =
# """
# 1  * R!H u0 {2,D} {3,D} {4,[S,D,T,B]}
# 2    R!H u0 {1,D} {5,[S,D,T,B]} {6,[S,D,T,B]}
# 3    R!H u0 {1,D} {7,[S,D,T,B]}
# 4    R!H u0 {1,[S,D,T,B]} {9,[S,D,T,B]}
# 5    R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
# 6    R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
# 7    R!H u0 {3,[S,D,T,B]} {5,[S,D,T,B]}
# 8    R!H u0 {6,[S,D,T,B]} {10,[S,D,T,B]}
# 9    R!H u0 {4,[S,D,T,B]} {10,[S,D,T,B]}
# 10   R!H u0 {8,[S,D,T,B]} {9,[S,D,T,B]}
# """,
#     thermo = ThermoData(
#         Tdata = ([300,400,500,600,800,1000,1500],'K'),
#         Cpdata = ([-5.645227533, -5.913365201, -5.9873174, -5.596732314, -5.028231358, -3.721783939, -2.722015296],'cal/(mol*K)'),
#         H298 = (73.61143212,'kcal/mol'),
#         S298 = (55.15890402,'cal/(mol*K)'),
#     ),
#     shortDesc = u"""Estimated""",
#     longDesc =
# u"""
# Estimated according to the following equation in order to take into account the highly strained 1,2-cyclopentadiene ring:
# polycyclic(s2_5_7_diene_7_8) = polycyclic(s2_5_7_triene_1_3_7) - ring(Cyclopentene) + ring(1,2-Cyclopentadiene)
# """,
# )

entry(
    index = 86,
    label = "s1-2_5d1d3_3_5d1_triene",
    group =
"""
1 * R!H u0 {2,S} {3,S} {4,S} {5,S}
2 R!H u0 {1,S} {3,S} {6,S}
3 R!H u0 {1,S} {2,S} {7,S}
4 R!H u0 {1,S} {9,D}
5 R!H u0 {1,S} {10,D}
6 R!H u0 {2,S} {8,D}
7 R!H u0 {3,S} {8,S}
8 R!H u0 {6,D} {7,S}
9 R!H u0 {4,D} {10,S}
10 R!H u0 {5,D} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.108, -7.764, -7.893, -7.784, -7.495, -7.132, -5.2],'cal/(mol*K)'),
        H298 = (38.553,'kcal/mol'),
        S298 = (95.09,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 87,
    label = "s2-2_5d1_3_6d1d3_triene",
    group =
"""
1 * R!H u0 {2,S} {3,S} {4,S} {5,S}
2 R!H u0 {1,S} {3,S} {7,S}
3 R!H u0 {1,S} {2,S} {6,S}
4 R!H u0 {1,S} {8,S}
5 R!H u0 {1,S} {10,D}
6 R!H u0 {3,S} {8,D}
7 R!H u0 {2,S} {9,D}
8 R!H u0 {4,S} {6,D}
9 R!H u0 {7,D} {10,S}
10 R!H u0 {5,D} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.846, -7.913, -8.399, -8.495, -8.078, -7.325, -5.437],'cal/(mol*K)'),
        H298 = (32.243,'kcal/mol'),
        S298 = (93.33,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 88,
    label = "s2_3_6_diene_1_6",
    group =
"""
1   R!H u0 {2,S} {3,D} {4,S}
2   R!H u0 {1,S} {3,S} {5,S}
3   R!H u0 {1,D} {2,S}
4   R!H u0 {1,S} {7,D}
5   R!H u0 {2,S} {6,S}
6 * R!H u0 {5,S} {7,S}
7   R!H u0 {4,D} {6,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-4.032344168, -4.650874761, -4.815852772, -4.625092734, -4.20190153, -3.46458891, -2.754087954], 'cal/(mol*K)'),
        H298=(58.40530516, 'kcal/mol'),
        S298=(56.0752652, 'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained cyclopropene ring:
polycyclic(s2_3_6_diene_1_6) = polycyclic(s2_3_6_ene_1) - ring(Cyclopropane) + ring(Cyclopropene)
""",
)

entry(
    index = 0,
    label = "s2_5_6_ben_yne_1",
    group = "OR{s2_5_6_ben_yne_1_res1, s2_5_6_ben_yne_1_res2, s2_5_6_ben_yne_1_res3}",
    thermo = None,
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 118,
    label = "s2_5_6_ben_yne_1_res1",
    group =
"""
1 * R!H u0 {2,B} {3,S} {4,B}
2   R!H u0 {1,B} {5,S} {6,B}
3   R!H u0 {1,S} {7,S}
4   R!H u0 {1,B} {8,B}
5   R!H u0 {2,S} {7,T}
6   R!H u0 {2,B} {9,B}
7   R!H u0 {3,S} {5,T}
8   R!H u0 {4,B} {9,B}
9   R!H u0 {6,B} {8,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.5365, -2.13592, -2.3522, -2.02817, -1.28741, -1.73936, -3.47344],'cal/(mol*K)'),
        H298 = (68.097,'kcal/mol'),
        S298 = (34.0579,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained cyclopentyne ring:
polycyclic(s2_5_6_ben_yne_1) = polycyclic(s2_5_6_indene) - ring(Cyclopentadiene) + ring(Cyclopentyne)
""",
)

entry(
    index = 118,
    label = "s2_5_6_ben_yne_1_res2",
    group =
"""
1 * R!H u0 {2,D} {3,S} {4,S}
2   R!H u0 {1,D} {5,S} {6,S}
3   R!H u0 {1,S} {7,S}
4   R!H u0 {1,S} {8,D}
5   R!H u0 {2,S} {7,T}
6   R!H u0 {2,S} {9,D}
7   R!H u0 {3,S} {5,T}
8   R!H u0 {4,D} {9,S}
9   R!H u0 {6,D} {8,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-8.783, -10.22, -10.545, -9.975, -7.334, -5.254, -6.393], 'cal/(mol*K)'),
        H298=(44.627, 'kcal/mol'),
        S298=(68.948, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Estimated""",
    longDesc=
    u"""
    Estimated according to the following equation in order to take into account the highly strained cyclopentyne ring:
    polycyclic(s2_5_6_ben_yne_1) = polycyclic(s2_5_6_indene) - ring(Cyclopentadiene) + ring(Cyclopentyne)
    """,
)

entry(
    index = 118,
    label = "s2_5_6_ben_yne_1_res3",
    group =
"""
1 * R!H u0 {2,S} {3,S} {4,D}
2   R!H u0 {1,S} {5,S} {6,D}
3   R!H u0 {1,S} {7,S}
4   R!H u0 {1,D} {8,S}
5   R!H u0 {2,S} {7,T}
6   R!H u0 {2,D} {9,S}
7   R!H u0 {3,S} {5,T}
8   R!H u0 {4,S} {9,D}
9   R!H u0 {6,S} {8,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-8.783, -10.22, -10.545, -9.975, -7.334, -5.254, -6.393], 'cal/(mol*K)'),
        H298=(44.627, 'kcal/mol'),
        S298=(68.948, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Estimated""",
    longDesc=
    u"""
    Estimated according to the following equation in order to take into account the highly strained cyclopentyne ring:
    polycyclic(s2_5_6_ben_yne_1) = polycyclic(s2_5_6_indene) - ring(Cyclopentadiene) + ring(Cyclopentyne)
    """,
)

entry(
    index = 119,
    label = "s3_5_5_diene_0_4",
    group =
"""
1   R!H u0 {3,S} {6,S} {7,S}
2   R!H u0 {3,S} {4,D} {5,S}
3   R!H u0 {1,S} {2,S}
4 * R!H u0 {2,D} {6,S}
5   R!H u0 {2,S} {7,D}
6   R!H u0 {1,S} {4,S}
7   R!H u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.117, -6.624, -6.352, -6.401, -5.37, -3.457, -3.059],'cal/(mol*K)'),
        H298 = (86.425,'kcal/mol'),
        S298 = (57.025,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted to CBS-QB3 calculation""",
    longDesc =
u"""
Fitted to CBS-QB3 calculation.
""",
)

entry(
    index = 0,
    label = "s4_6_6_ben_ben",
    group = "OR{s4_6_6_ben_ben_res1, s4_6_6_ben_ben_res2, s4_6_6_ben_ben_res3}",
    thermo = None,
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 180,
    label = "s4_6_6_ben_ben_res1",
    group =
"""
1 * R!H u0 {3,B} {6,B} {8,B}
2   R!H u0 {4,B} {5,B} {7,B}
3   R!H u0 {1,B} {4,B}
4   R!H u0 {2,B} {3,B}
5   R!H u0 {2,B} {6,B}
6   R!H u0 {1,B} {5,B}
7   R!H u0 {2,B} {8,B}
8   R!H u0 {1,B} {7,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.711, 2.163, 2.154, 1.273, 0.527, 0.897, -1.267],'cal/(mol*K)'),
        H298 = (165.718,'kcal/mol'),
        S298 = (12.735,'cal/(mol*K)'),
    ),
    shortDesc=u"""Fitted to CBS-QB3 calculation""",
    longDesc=
    u"""
    Fitted to CBS-QB3 calculation.
    """,
)

entry(
    index = 181,
    label = "s4_6_6_ben_ben_res2",
    group =
"""
1 * R!H u0 {3,S} {6,B} {8,B}
2   R!H u0 {4,S} {5,B} {7,B}
3   R!H u0 {1,S} {4,D}
4   R!H u0 {2,S} {3,D}
5   R!H u0 {2,B} {6,B}
6   R!H u0 {1,B} {5,B}
7   R!H u0 {2,B} {8,B}
8   R!H u0 {1,B} {7,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.829, -1.234, -0.797, -1.155, -1.114, -0.25, -0.824],'cal/(mol*K)'),
        H298 = (156.978,'kcal/mol'),
        S298 = (28.635,'cal/(mol*K)'),
    ),
    shortDesc=u"""Fitted to CBS-QB3 calculation""",
    longDesc=
    u"""
    Fitted to CBS-QB3 calculation.
    """,
)

entry(
    index = 182,
    label = "s4_6_6_ben_ben_res3",
    group =
"""
1 * R!H u0 {3,S} {6,D} {8,S}
2   R!H u0 {4,S} {5,D} {7,S}
3   R!H u0 {1,S} {4,D}
4   R!H u0 {2,S} {3,D}
5   R!H u0 {2,D} {6,S}
6   R!H u0 {1,D} {5,S}
7   R!H u0 {2,S} {8,D}
8   R!H u0 {1,S} {7,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.711, 2.163, 2.154, 1.273, 0.527, 0.897, -1.267], 'cal/(mol*K)'),
        H298=(165.718, 'kcal/mol'),
        S298=(12.735, 'cal/(mol*K)'),
    ),
    shortDesc=u"""""",
    longDesc=
    u"""
    Copy of res 1 correction.
    """,
)

entry(
    index = 183,
    label = "s2_3_5_yne_1",
    group =
"""
1 * R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {6,T}
5   R!H u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
6   R!H u0 {4,T} {5,[S,D,T,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.443820268, -3.477684512, -4.097300191, -4.243118547, -3.892787763, -3.392011472, -5.832768642],'cal/(mol*K)'),
        H298 = (102.998912,'kcal/mol'),
        S298 = (61.24771511,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained 1,2-cyclopentadiene ring:
polycyclic(s2_3_5_yne_1) = polycyclic(s2_3_5_ane) - ring(Cyclopentane) + ring(Cyclopentyne)
""",
)

entry(
    index = 184,
    label = "s2_3_5_yne_1",
    group =
"""
1 * R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {6,T}
5   R!H u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
6   R!H u0 {4,T} {5,[S,D,T,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.443820268, -3.477684512, -4.097300191, -4.243118547, -3.892787763, -3.392011472, -5.832768642],'cal/(mol*K)'),
        H298 = (102.998912,'kcal/mol'),
        S298 = (61.24771511,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained cyclopentyne ring:
polycyclic(s2_3_5_yne_1) = polycyclic(s2_3_5_ane) - ring(Cyclopentane) + ring(Cyclopentyne)
""",
)

entry(
    index = 185,
    label = "s2_4_5_yne_1",
    group =
"""
1 * R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {7,T}
6   R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
7   R!H u0 {5,T} {6,[S,D,T,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.888347036, -4.658325048, -5.016994264, -4.899762906, -4.027563098, -3.156256214, -5.169279159],'cal/(mol*K)'),
        H298 = (103.6329943,'kcal/mol'),
        S298 = (54.7725717,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained cyclopentyne ring:
polycyclic(s2_4_5_yne_1) = polycyclic(s2_4_5_ane) - ring(Cyclopentane) + ring(Cyclopentyne)
""",
)
entry(
    index = 186,
    label = "s2_5_5_yne_1",
    group =
"""
1   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
3 * R!H u0 {1,[S,D,T,B]} {7,T}
4   R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
6   R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
7   R!H u0 {3,T} {4,[S,D,T,B]}
8   R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.479169216, -5.9646826, -6.061210325, -5.69574761, -4.324623327, -3.09401912, -4.663304015],'cal/(mol*K)'),
        H298 = (84.65201912,'kcal/mol'),
        S298 = (49.18174952,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained cyclopentyne ring:
polycyclic(s2_5_5_yne_1) = polycyclic(s2_5_5_ane) - ring(Cyclopentane) + ring(cyclopentyne)
""",
)

entry(
    index = 187,
    label = "s2_5_6_yne_6",
    group =
"""
1 * R!H u0 {2,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {6,[S,D,T,B]}
3   R!H u0 {2,[S,D,T,B]} {9,[S,D,T,B]}
4   R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {7,T}
6   R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
7   R!H u0 {5,T} {6,[S,D,T,B]}
8   R!H u0 {4,[S,D,T,B]} {9,[S,D,T,B]}
9   R!H u0 {3,[S,D,T,B]} {8,[S,D,T,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.798002868, -6.39006501, -6.674977055, -6.226913958, -4.369269598, -2.799444551, -3.977596558],'cal/(mol*K)'),
        H298 = (80.60206692,'kcal/mol'),
        S298 = (47.49723709,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained cyclopentyne ring:
polycyclic(s2_5_6_yne_6) = polycyclic(s2_5_6_ane) - ring(Cyclopentane) + ring(cyclopentyne)
""",
)

entry(
    index = 188,
    label = "s2_5_7_yne_7",
    group =
"""
1  * R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]}
2    R!H u0 {1,[S,D,T,B]} {5,[S,D,T,B]} {6,[S,D,T,B]}
3    R!H u0 {1,[S,D,T,B]} {7,T}
4    R!H u0 {1,[S,D,T,B]} {9,[S,D,T,B]}
5    R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
6    R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
7    R!H u0 {3,T} {5,[S,D,T,B]}
8    R!H u0 {6,[S,D,T,B]} {10,[S,D,T,B]}
9    R!H u0 {4,[S,D,T,B]} {10,[S,D,T,B]}
10   R!H u0 {8,[S,D,T,B]} {9,[S,D,T,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.476, -4.266, -4.8, -4.548, -4.036, -3.246, -4.563],'cal/(mol*K)'),
        H298 = (79.805,'kcal/mol'),
        S298 = (57.3666,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained cyclopentyne ring:
polycyclics(s2_5_7_yne_7) = polycyclic(s2_5_7_triene_1_3_7) - ring(Cyclopentene) + ring(cyclopentyne)
""",
)

entry(
    index = 0,
    label = "s2_3_6_yne",
    group="OR{s2_3_6_yne_1, s2_3_6_yne_2}",
    thermo=None,
    shortDesc = u"""Should capture all cyclohexyne containing s2_3_6 bicyclics""",
    longDesc =
u"""

""",
)

entry(
    index = 189,
    label = "s2_3_6_yne_1",
    group =
"""
1   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,S}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {4,S}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {2,S} {6,T}
5   R!H u0 {1,S} {7,S}
6 * R!H u0 {4,T} {7,S}
7   R!H u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.661282027,-6.727250478,-6.982353728,-7.65734608,-7.901561185,-7.01532696,-8.006223709],'cal/(mol*K)'),
        H298 = (76.75381644,'kcal/mol'),
        S298 = (60.24648929,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained cyclohexyne ring:
polycyclic(s2_3_6_yne_1) = polycyclic(s2_3_6_ane) - ring(Cyclohexane) + ring(cyclohexyne)
""",
)

entry(
    index = 190,
    label = "s2_3_6_yne_2",
    group =
"""
1   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,S}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {4,S}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {2,S} {6,S}
5   R!H u0 {1,S} {7,S}
6 * R!H u0 {4,S} {7,T}
7   R!H u0 {5,S} {6,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.661282027,-6.727250478,-6.982353728,-7.65734608,-7.901561185,-7.01532696,-8.006223709],'cal/(mol*K)'),
        H298 = (76.75381644,'kcal/mol'),
        S298 = (60.24648929,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained cyclohexyne ring:
polycyclic(s2_3_6_yne_2) = polycyclic(s2_3_6_ane) - ring(Cyclohexane) + ring(cyclohexyne)
""",
)

entry(
    index = 0,
    label = "s2_4_6_yne",
    group="OR{s2_4_6_yne_1, s2_4_6_yne_2}",
    thermo=None,
    shortDesc = u"""Should capture all cyclohexyne containing s2_4_6 bicyclics""",
    longDesc =
u"""

""",
)

entry(
    index = 191,
    label = "s2_4_6_yne_1",
    group =
"""
1   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {6,S}
2   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {5,S}
3   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]}
5   R!H u0 {2,S} {8,S}
6   R!H u0 {1,S} {7,T}
7 * R!H u0 {6,T} {8,S}
8   R!H u0 {5,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.495890057,-8.139248566,-8.0186826,-8.38067304,-8.090590822,-6.82307074,-7.346319312],'cal/(mol*K)'),
        H298 = (73.71581453,'kcal/mol'),
        S298 = (52.7259348,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained cyclohexyne ring:
polycyclic(s2_4_6_yne_1) = polycyclic(s2_4_6_ane) - ring(Cyclohexane) + ring(cyclohexyne)
""",
)

entry(
    index = 192,
    label = "s2_4_6_yne_2",
    group =
"""
1   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {6,S}
2   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {5,S}
3   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]}
5   R!H u0 {2,S} {8,S}
6   R!H u0 {1,S} {7,S}
7 * R!H u0 {6,S} {8,T}
8   R!H u0 {5,S} {7,T}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-7.495890057,-8.139248566,-8.0186826,-8.38067304,-8.090590822,-6.82307074,-7.346319312], 'cal/(mol*K)'),
        H298=(73.71581453, 'kcal/mol'),
        S298=(52.7259348, 'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained cyclohexyne ring:
polycyclic(s2_4_6_yne_2) = polycyclic(s2_4_6_ane) - ring(Cyclohexane) + ring(cyclohexyne)
""",
)

entry(
    index = 0,
    label = "s2_5_6_hexyne",
    group="OR{s2_5_6_yne_1, s2_5_6_yne_2}",
    thermo=None,
    shortDesc = u"""Should capture all cyclohexyne containing s2_5_6 bicyclics""",
    longDesc =
u"""

""",
)

entry(
    index = 193,
    label = "s2_5_6_yne_1",
    group =
"""
1 * R!H u0 {2,[S,D,T,B]} {4,S} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {3,S} {6,[S,D,T,B]}
3   R!H u0 {2,S} {9,S}
4   R!H u0 {1,S} {8,T}
5   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
7   R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
8   R!H u0 {4,T} {9,S}
9   R!H u0 {3,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.363002868,-9.06606501, -8.995977055, -9.143913958, -8.281269598, -6.627444551, -6.731596558],'cal/(mol*K)'),
        H298 = (54.63206692,'kcal/mol'),
        S298 = (49.57153709,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained cyclohexyne ring:
polycyclic(s2_5_6_yne_1) = polycyclic(s2_5_6_ane) - ring(Cyclohexane) + ring(cyclohexyne)
""",
)

entry(
    index = 194,
    label = "s2_5_6_yne_2",
    group =
"""
1 * R!H u0 {2,[S,D,T,B]} {4,S} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {3,S} {6,[S,D,T,B]}
3   R!H u0 {2,S} {9,S}
4   R!H u0 {1,S} {8,S}
5   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
7   R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
8   R!H u0 {4,S} {9,T}
9   R!H u0 {3,S} {8,T}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-8.363002868, -9.06606501, -8.995977055, -9.143913958, -8.281269598, -6.627444551, -6.731596558],'cal/(mol*K)'),
        H298=(54.63206692, 'kcal/mol'),
        S298=(49.57153709, 'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained cyclohexyne ring:
polycyclic(s2_5_6_yne_2) = polycyclic(s2_5_6_ane) - ring(Cyclohexane) + ring(cyclohexyne)
""",
)

entry(
    index = 0,
    label = "s2_6_6_yne",
    group="OR{s2_6_6_yne_1, s2_6_6_yne_2}",
    thermo=None,
    shortDesc = u"""Should capture all cyclohexyne containing s2_6_6 bicyclics""",
    longDesc =
u"""

""",
)

entry(
    index = 195,
    label = "s2_6_6_yne_1",
    group =
"""
1    R!H u0 {2,[S,D,T,B]} {3,S} {6,[S,D,T,B]}
2    R!H u0 {1,[S,D,T,B]} {4,S} {5,[S,D,T,B]}
3    R!H u0 {1,S} {9,S}
4    R!H u0 {2,S} {7,T}
5    R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
6    R!H u0 {1,[S,D,T,B]} {10,[S,D,T,B]}
7  * R!H u0 {4,T} {9,S}
8    R!H u0 {5,[S,D,T,B]} {10,[S,D,T,B]}
9    R!H u0 {3,S} {7,S}
10   R!H u0 {6,[S,D,T,B]} {8,[S,D,T,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.402916826,-9.794745698,-9.524179732,-9.476944551,-8.243243786,-6.31449044,-6.057839388],'cal/(mol*K)'),
        H298 = (47.50553728,'kcal/mol'),
        S298 = (41.72784685,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained cyclohexyne ring:
polycyclic(s2_6_6_yne_1) = polycyclic(s2_6_6_ane) - ring(Cyclohexane) + ring(cyclohexyne)
""",
)

entry(
    index = 196,
    label = "s2_6_6_yne_2",
    group =
"""
1    R!H u0 {2,[S,D,T,B]} {3,S} {6,[S,D,T,B]}
2    R!H u0 {1,[S,D,T,B]} {4,S} {5,[S,D,T,B]}
3    R!H u0 {1,S} {9,S}
4    R!H u0 {2,S} {7,S}
5    R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
6    R!H u0 {1,[S,D,T,B]} {10,[S,D,T,B]}
7  * R!H u0 {4,S} {9,T}
8    R!H u0 {5,[S,D,T,B]} {10,[S,D,T,B]}
9    R!H u0 {3,S} {7,T}
10   R!H u0 {6,[S,D,T,B]} {8,[S,D,T,B]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-9.402916826,-9.794745698,-9.524179732,-9.476944551,-8.243243786,-6.31449044,-6.057839388],'cal/(mol*K)'),
        H298=(47.50553728, 'kcal/mol'),
        S298=(41.72784685, 'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained cyclohexyne ring:
polycyclic(s2_6_6_yne_2) = polycyclic(s2_6_6_ane) - ring(Cyclohexane) + ring(cyclohexyne)
""",
)

entry(
    index = 0,
    label = "s2_3_6_yne_ene",
    group="OR{s2_3_6_yne_1_ene_4, s2_3_6_yne_1_ene_3, s2_3_6_yne_2_ene_4}",
    thermo=None,
    shortDesc = u"""Should capture all cyclohex-yne-ene containing s2_3_6 bicyclics""",
    longDesc =
u"""

""",
)

entry(
    index = 197,
    label = "s2_3_6_yne_1_ene_4",
    group =
"""
1   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,D}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {4,S}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {2,S} {6,T}
5   R!H u0 {1,D} {7,S}
6 * R!H u0 {4,T} {7,S}
7   R!H u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.786282027, -4.653250478, -5.838353728, -6.94334608, -7.652561185, -6.45232696, -6.507223709],'cal/(mol*K)'),
        H298 = (75.38081644,'kcal/mol'),
        S298 = (63.59818929,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained cyclohex_1_yne_4_ene ring:
polycyclic(s2_3_6_yne_1_ene_4) = polycyclic(s2_3_6_ane) - ring(Cyclohexane) + ring(six-inringonetripleonedouble-14)
""",
)

entry(
    index = 201,
    label = "s2_3_6_yne_1_ene_3",
    group =
"""
1   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,S}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {4,S}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {2,S} {6,T}
5   R!H u0 {1,S} {7,D}
6 * R!H u0 {4,T} {7,S}
7   R!H u0 {5,D} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.647282027, -5.916250478, -7.386353728, -8.61534608, -9.172561185, -7.72232696, -8.035223709],'cal/(mol*K)'),
        H298 = (84.93081644,'kcal/mol'),
        S298 = (64.01718929,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained cyclohex_1_yne_3_ene ring:
polycyclic(s2_3_6_yne_1_ene_3) = polycyclic(s2_3_6_ane) - ring(Cyclohexane) + ring(six-inringonetripleonedouble-13)
""",
)

entry(
    index = 202,
    label = "s2_3_6_yne_2_ene_4",
    group =
"""
1   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,D}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {4,S}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {2,S} {6,S}
5   R!H u0 {1,D} {7,S}
6 * R!H u0 {4,S} {7,T}
7   R!H u0 {5,S} {6,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.647282027, -5.916250478, -7.386353728, -8.61534608, -9.172561185, -7.72232696, -8.035223709],'cal/(mol*K)'),
        H298 = (84.93081644,'kcal/mol'),
        S298 = (64.01718929,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained cyclohex_2_yne_4_ene ring:
polycyclic(s2_3_6_yne_2_ene_4) = polycyclic(s2_3_6_ane) - ring(Cyclohexane) + ring(six-inringonetripleonedouble-13)
""",
)

entry(
    index = 0,
    label = "s2_4_6_yne_ene",
    group="OR{s2_4_6_yne_1_ene_4, s2_4_6_yne_1_ene_3, s2_4_6_yne_2_ene_4}",
    thermo=None,
    shortDesc = u"""Should capture all cyclohex-yne-ene containing s2_4_6 bicyclics""",
    longDesc =
u"""

""",
)

entry(
    index = 198,
    label = "s2_4_6_yne_1_ene_4",
    group =
"""
1   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {6,S}
2   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {5,D}
3   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]}
5   R!H u0 {2,D} {8,S}
6   R!H u0 {1,S} {7,T}
7 * R!H u0 {6,T} {8,S}
8   R!H u0 {5,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.620890057, -6.065248566, -6.8746826, -7.66667304, -7.841590822, -6.260070746, -5.847319312],'cal/(mol*K)'),
        H298 = (72.34281453,'kcal/mol'),
        S298 = (56.0776348,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained cyclohex_1_yne_4_ene ring:
polycyclic(s2_4_6_yne_1_ene_4) = polycyclic(s2_4_6_ane) - ring(Cyclohexane) + ring(six-inringonetripleonedouble-14)
""",
)

entry(
    index = 203,
    label = "s2_4_6_yne_1_ene_3",
    group =
"""
1   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {6,S}
2   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {5,S}
3   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]}
5   R!H u0 {2,S} {8,D}
6   R!H u0 {1,S} {7,T}
7 * R!H u0 {6,T} {8,S}
8   R!H u0 {5,D} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.481890057, -7.328248566, -8.4226826, -9.33867304, -9.361590822, -7.530070746, -7.375319312],'cal/(mol*K)'),
        H298 = (81.89281453,'kcal/mol'),
        S298 = (56.4966348,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained cyclohex_1_yne_3_ene ring:
polycyclic(s2_4_6_yne_1_ene_3) = polycyclic(s2_4_6_ane) - ring(Cyclohexane) + ring(six-inringonetripleonedouble-13)
""",
)

entry(
    index = 204,
    label = "s2_4_6_yne_2_ene_4",
    group =
"""
1   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {6,S}
2   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {5,D}
3   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]}
5   R!H u0 {2,D} {8,S}
6   R!H u0 {1,S} {7,S}
7 * R!H u0 {6,S} {8,T}
8   R!H u0 {5,S} {7,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.481890057, -7.328248566, -8.4226826, -9.33867304, -9.361590822, -7.530070746, -7.375319312],'cal/(mol*K)'),
        H298 = (81.89281453,'kcal/mol'),
        S298 = (56.4966348,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained cyclohex_1_yne_3_ene ring:
polycyclic(s2_4_6_yne_2_ene_4) = polycyclic(s2_4_6_ane) - ring(Cyclohexane) + ring(six-inringonetripleonedouble-13)
""",
)

entry(
    index = 0,
    label = "s2_5_6_yne_ene",
    group="OR{s2_5_6_yne_1_ene_4, s2_5_6_yne_1_ene_3, s2_5_6_yne_2_ene_4}",
    thermo=None,
    shortDesc = u"""Should capture all cyclohex-yne-ene containing s2_5_6 bicyclics""",
    longDesc =
u"""

""",
)

entry(
    index = 199,
    label = "s2_5_6_yne_1_ene_4",
    group =
"""
1 * R!H u0 {2,[S,D,T,B]} {4,S} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {3,D} {6,[S,D,T,B]}
3   R!H u0 {2,D} {9,S}
4   R!H u0 {1,S} {8,T}
5   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
7   R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
8   R!H u0 {4,T} {9,S}
9   R!H u0 {3,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.488002868, -6.99206501, -7.851977055, -8.429913958, -8.032269598, -6.064444551, -5.232596558],'cal/(mol*K)'),
        H298 = (53.25906692,'kcal/mol'),
        S298 = (52.92323709,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained cyclohex_1_yne_4_ene ring:
polycyclic(s2_5_6_yne_1_ene_4) = polycyclic(s2_5_6_ane) - ring(Cyclohexane) + ring(six-inringonetripleonedouble-14)
""",
)

entry(
    index = 205,
    label = "s2_5_6_yne_1_ene_3",
    group =
"""
1 * R!H u0 {2,[S,D,T,B]} {4,S} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {3,S} {6,[S,D,T,B]}
3   R!H u0 {2,S} {9,D}
4   R!H u0 {1,S} {8,T}
5   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
7   R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
8   R!H u0 {4,T} {9,S}
9   R!H u0 {3,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.349002868, -8.25506501, -9.399977055, -10.10191396, -9.552269598, -7.334444551, -6.760596558],'cal/(mol*K)'),
        H298 = (62.80906692,'kcal/mol'),
        S298 = (53.34223709,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained cyclohex_1_yne_3_ene ring:
polycyclic(s2_5_6_yne_1_ene_3) = polycyclic(s2_5_6_ane) - ring(Cyclohexane) + ring(six-inringonetripleonedouble-13)
""",
)

entry(
    index = 206,
    label = "s2_5_6_yne_2_ene_4",
    group =
"""
1 * R!H u0 {2,[S,D,T,B]} {4,S} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {3,D} {6,[S,D,T,B]}
3   R!H u0 {2,D} {9,S}
4   R!H u0 {1,S} {8,S}
5   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
7   R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
8   R!H u0 {4,S} {9,T}
9   R!H u0 {3,S} {8,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.349002868, -8.25506501, -9.399977055, -10.10191396, -9.552269598, -7.334444551, -6.760596558],'cal/(mol*K)'),
        H298 = (62.80906692,'kcal/mol'),
        S298 = (53.34223709,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained cyclohex_1_yne_3_ene ring:
polycyclic(s2_5_6_yne_2_ene_4) = polycyclic(s2_5_6_ane) - ring(Cyclohexane) + ring(six-inringonetripleonedouble-13)
""",
)

entry(
    index = 0,
    label = "s2_6_6_yne_ene",
    group="OR{s2_6_6_yne_1_ene_4, s2_6_6_yne_1_ene_3, s2_6_6_yne_2_ene_4}",
    thermo=None,
    shortDesc = u"""Should capture all cyclohex-yne-ene containing s2_6_6 bicyclics""",
    longDesc =
u"""

""",
)

entry(
    index = 200,
    label = "s2_6_6_yne_1_ene_4",
    group =
"""
1    R!H u0 {2,[S,D,T,B]} {3,D} {6,[S,D,T,B]}
2    R!H u0 {1,[S,D,T,B]} {4,S} {5,[S,D,T,B]}
3    R!H u0 {1,D} {9,S}
4    R!H u0 {2,S} {7,T}
5    R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
6    R!H u0 {1,[S,D,T,B]} {10,[S,D,T,B]}
7  * R!H u0 {4,T} {9,S}
8    R!H u0 {5,[S,D,T,B]} {10,[S,D,T,B]}
9    R!H u0 {3,S} {7,S}
10   R!H u0 {6,[S,D,T,B]} {8,[S,D,T,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.527916826, -7.720745698, -8.380179732, -8.762944551, -7.994243786, -5.75149044, -4.558839388],'cal/(mol*K)'),
        H298 = (46.13253728,'kcal/mol'),
        S298 = (45.07954685,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained cyclohex_1_yne_4_ene ring:
polycyclic(s2_6_6_yne_1_ene_4) = polycyclic(s2_6_6_ane) - ring(Cyclohexane) + ring(six-inringonetripleonedouble-14)
""",
)

entry(
    index = 207,
    label = "s2_6_6_yne_1_ene_3",
    group =
"""
1    R!H u0 {2,[S,D,T,B]} {3,S} {6,[S,D,T,B]}
2    R!H u0 {1,[S,D,T,B]} {4,S} {5,[S,D,T,B]}
3    R!H u0 {1,S} {9,D}
4    R!H u0 {2,S} {7,T}
5    R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
6    R!H u0 {1,[S,D,T,B]} {10,[S,D,T,B]}
7  * R!H u0 {4,T} {9,S}
8    R!H u0 {5,[S,D,T,B]} {10,[S,D,T,B]}
9    R!H u0 {3,D} {7,S}
10   R!H u0 {6,[S,D,T,B]} {8,[S,D,T,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.388916826,-8.983745698,-9.928179732,-10.43494455,-9.514243786,-7.02149044,-6.086839388],'cal/(mol*K)'),
        H298 = (55.68253728,'kcal/mol'),
        S298 = (45.49854685,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained cyclohex_1_yne_3_ene ring:
polycyclic(s2_6_6_yne_1_ene_3) = polycyclic(s2_6_6_ane) - ring(Cyclohexane) + ring(six-inringonetripleonedouble-13)
""",
)

entry(
    index = 208,
    label = "s2_6_6_yne_2_ene_4",
    group =
"""
1    R!H u0 {2,[S,D,T,B]} {3,D} {6,[S,D,T,B]}
2    R!H u0 {1,[S,D,T,B]} {4,S} {5,[S,D,T,B]}
3    R!H u0 {1,D} {9,S}
4    R!H u0 {2,S} {7,S}
5    R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
6    R!H u0 {1,[S,D,T,B]} {10,[S,D,T,B]}
7  * R!H u0 {4,S} {9,T}
8    R!H u0 {5,[S,D,T,B]} {10,[S,D,T,B]}
9    R!H u0 {3,S} {7,T}
10   R!H u0 {6,[S,D,T,B]} {8,[S,D,T,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.388916826,-8.983745698,-9.928179732,-10.43494455,-9.514243786,-7.02149044,-6.086839388],'cal/(mol*K)'),
        H298 = (55.68253728,'kcal/mol'),
        S298 = (45.49854685,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained cyclohex_1_yne_3_ene ring:
polycyclic(s2_6_6_yne_2_ene_4) = polycyclic(s2_6_6_ane) - ring(Cyclohexane) + ring(six-inringonetripleonedouble-13)
""",
)

entry(
    index = 209,
    label = "s2_3_6_diyne_1_3",
    group =
"""
1   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,S}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {4,S}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {2,S} {6,T}
5   R!H u0 {1,S} {7,T}
6 * R!H u0 {4,T} {7,S}
7   R!H u0 {5,T} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.441282027, -5.336250478, -6.222353728, -7.17534608, -7.823561185, -7.48632696, -9.183223709],'cal/(mol*K)'),
        H298 = (140.3808164,'kcal/mol'),
        S298 = (69.60548929,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained 1_3_cyclohexadiyne ring:
polycyclic(s2_3_6_diyne_1_3) = polycyclic(s2_3_6_ane) - ring(Cyclohexane) + ring(six-inringtwotriple-13)
""",
)

entry(
    index = 210,
    label = "s2_4_6_diyne_1_3",
    group =
"""
1   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {6,S}
2   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {5,S}
3   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]}
5   R!H u0 {2,S} {8,T}
6   R!H u0 {1,S} {7,T}
7 * R!H u0 {6,T} {8,S}
8   R!H u0 {5,T} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.275890057, -6.748248566, -7.2586826, -7.89867304, -8.012590822, -7.294070746, -8.523319312],'cal/(mol*K)'),
        H298 = (137.3428145,'kcal/mol'),
        S298 = (62.0849348,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained 1_3_cyclohexadiyne ring:
polycyclic(s2_4_6_diyne_1_3) = polycyclic(s2_4_6_ane) - ring(Cyclohexane) + ring(six-inringtwotriple-13)
""",
)

entry(
    index = 211,
    label = "s2_5_6_diyne_1_3",
    group =
"""
1 * R!H u0 {2,[S,D,T,B]} {4,S} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {3,S} {6,[S,D,T,B]}
3   R!H u0 {2,S} {9,T}
4   R!H u0 {1,S} {8,T}
5   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
7   R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
8   R!H u0 {4,T} {9,S}
9   R!H u0 {3,T} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.143002868, -7.67506501, -8.235977055, -8.661913958, -8.203269598, -7.098444551, -7.908596558],'cal/(mol*K)'),
        H298 = (118.2590669,'kcal/mol'),
        S298 = (58.93053709,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained 1_3_cyclohexadiyne ring:
polycyclic(s2_5_6_diyne_1_3) = polycyclic(s2_5_6_ane) - ring(Cyclohexane) + ring(six-inringtwotriple-13)
""",
)

entry(
    index = 212,
    label = "s2_6_6_diyne_1_3",
    group =
"""
1    R!H u0 {2,[S,D,T,B]} {3,S} {6,[S,D,T,B]}
2    R!H u0 {1,[S,D,T,B]} {4,S} {5,[S,D,T,B]}
3    R!H u0 {1,S} {9,T}
4    R!H u0 {2,S} {7,T}
5    R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
6    R!H u0 {1,[S,D,T,B]} {10,[S,D,T,B]}
7  * R!H u0 {4,T} {9,S}
8    R!H u0 {5,[S,D,T,B]} {10,[S,D,T,B]}
9    R!H u0 {3,T} {7,S}
10   R!H u0 {6,[S,D,T,B]} {8,[S,D,T,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.182916826, -8.403745698, -8.764179732, -8.994944551, -8.165243786, -6.78549044, -7.234839388],'cal/(mol*K)'),
        H298 = (111.1325373,'kcal/mol'),
        S298 = (51.08684685,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained 1_3_cyclohexadiyne ring:
polycyclic(s2_6_6_diyne_1_3) = polycyclic(s2_6_6_ane) - ring(Cyclohexane) + ring(six-inringtwotriple-13)
""",
)

entry(
    index = 0,
    label = "s3_4_6_ben_ane",
    group = "OR{s3_4_6_ben_ane_res1, s3_4_6_ben_ane_res2}",
    thermo = None,
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 213,
    label = "s3_4_6_ben_ane_res1",
    group =
"""
1   R!H u0 {3,B} {4,S} {6,B}
2   R!H u0 {3,B} {4,S} {7,B}
3   R!H u0 {1,B} {2,B}
4 * R!H u0 {2,S} {1,S}
6   R!H u0 {1,B} {8,B}
7   R!H u0 {2,B} {8,B}
8   R!H u0 {6,B} {7,B}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.971, 1.615, 1.051, -0.042, -1.098, -0.849, -2.199], 'cal/(mol*K)'),
        H298=(150.622, 'kcal/mol'),
        S298=(34.822, 'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
Fitted to CBS-QB3 calculations
""",
)

entry(
    index = 214,
    label = "s3_4_6_ben_ane_res2",
    group =
"""
1   R!H u0 {3,S} {4,S} {6,D}
2   R!H u0 {3,D} {4,S} {7,S}
3   R!H u0 {1,S} {2,D}
4 * R!H u0 {2,S} {1,S}
6   R!H u0 {1,D} {8,S}
7   R!H u0 {2,S} {8,D}
8   R!H u0 {6,S} {7,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-6.57, -6.954, -7.598, -8.045, -6.641, -4.264, -4.149], 'cal/(mol*K)'),
        H298=(129.962, 'kcal/mol'),
        S298=(67.112, 'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
Fitted to CBS-QB3 calculations
""",
)

entry(
    index = 0,
    label = "s3_4_6_yne",
    group = "OR{s3_4_6_yne_1}",
    thermo = None,
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 215,
    label = "s3_4_6_yne_1",
    group =
"""
1   R!H u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {6,S}
2   R!H u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,S}
3 * R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
5   R!H u0 {2,S} {7,T}
6   R!H u0 {1,S} {7,S}
7   R!H u0 {5,T} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.093404398, -7.782460803, -7.635078394, -8.045969407, -8.130050669, -7.137936902, -7.992600382],'cal/(mol*K)'),
        H298 = (77.59965774,'kcal/mol'),
        S298 = (56.3636021,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained cyclohexadyne ring:
polycyclic(s3_4_6_yne_1) = polycyclic(s3_4_6_ane) - ring(Cyclohexane) + ring(cyclohexyne)
""",
)

entry(
    index = 0,
    label = "s3_4_6_yne_ene",
    group = "OR{s3_4_6_yne_1_ene_3}",
    thermo = None,
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 216,
    label = "s3_4_6_yne_1_ene_3",
    group =
"""
1   R!H u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {6,D}
2   R!H u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,S}
3 * R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
5   R!H u0 {2,S} {7,T}
6   R!H u0 {1,D} {7,S}
7   R!H u0 {5,T} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.079404398, -6.971460803, -8.039078394, -9.003969407, -9.401050669, -7.844936902, -8.021600382],'cal/(mol*K)'),
        H298 = (85.77665774,'kcal/mol'),
        S298 = (60.1343021,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained cyclohex_1_yne_3_ene ring:
polycyclic(s3_4_6_yne_1_ene_3) = polycyclic(s3_4_6_ane) - ring(Cyclohexane) + ring(cyclohex_1_yne_3_ene)
""",
)

entry(
    index = 0,
    label = "s3_5_6_yne",
    group = "OR{s3_5_6_yne_1}",
    thermo = None,
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 217,
    label = "s3_5_6_yne_1",
    group =
"""
1   R!H u0 {3,[S,D,T,B]} {5,[S,D,T,B]} {6,S}
2   R!H u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {7,S}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {5,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]}
6   R!H u0 {1,S} {8,T}
7   R!H u0 {2,S} {8,S}
8 * R!H u0 {6,T} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.560421606, -8.93442065, -8.522984704, -8.703330784, -8.321231358, -6.991330784, -7.430688337],'cal/(mol*K)'),
        H298 = (55.89141205,'kcal/mol'),
        S298 = (50.60069579,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained cyclohexadyne ring:
polycyclic(s3_5_6_yne_1) = polycyclic(s3_5_6_ane) - ring(Cyclohexane) + ring(cyclohexyne)
""",
)

entry(
    index = 0,
    label = "s3_5_6_yne_ene",
    group = "OR{s3_5_6_yne_1_ene_3}",
    thermo = None,
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 218,
    label = "s3_5_6_yne_1_ene_3",
    group =
"""
1   R!H u0 {3,[S,D,T,B]} {5,[S,D,T,B]} {6,S}
2   R!H u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {7,D}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {5,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]}
6   R!H u0 {1,S} {8,T}
7   R!H u0 {2,D} {8,S}
8 * R!H u0 {6,T} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.546421606, -8.12342065, -8.926984704, -9.661330784, -9.592231358, -7.698330784, -7.459688337],'cal/(mol*K)'),
        H298 = (64.06841205,'kcal/mol'),
        S298 = (54.37139579,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained cyclohex_1_yne_3_ene ring:
polycyclic(s3_5_6_yne_1_ene_3) = polycyclic(s3_5_6_ane) - ring(Cyclohexane) + ring(cyclohex_1_yne_3_ene)
""",
)

entry(
    index = 0,
    label = "s3_6_6_yne",
    group = "OR{s3_6_6_yne_1}",
    thermo = None,
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 219,
    label = "s3_6_6_yne_1",
    group =
"""
1   R!H u0 {3,[S,D,T,B]} {6,[S,D,T,B]} {7,S}
2   R!H u0 {3,[S,D,T,B]} {4,S} {5,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4 * R!H u0 {2,S} {9,T}
5   R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
6   R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
7   R!H u0 {1,S} {9,S}
8   R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
9   R!H u0 {4,T} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.748997132, -10.07921033, -9.613806883, -9.643674952, -8.771470363, -7.065781071, -6.98207457],'cal/(mol*K)'),
        H298 = (55.51712906,'kcal/mol'),
        S298 = (44.48931912,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained cyclohexadyne ring:
polycyclic(s3_6_6_yne_1) = polycyclic(s3_6_6_ane) - ring(Cyclohexane) + ring(cyclohexyne)
""",
)

entry(
    index = 0,
    label = "s3_6_6_yne_ene",
    group = "OR{s3_6_6_yne_1_ene_3}",
    thermo = None,
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 220,
    label = "s3_6_6_yne_1_ene_3",
    group =
"""
1   R!H u0 {3,[S,D,T,B]} {6,[S,D,T,B]} {7,D}
2   R!H u0 {3,[S,D,T,B]} {4,S} {5,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4 * R!H u0 {2,S} {9,T}
5   R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
6   R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
7   R!H u0 {1,D} {9,S}
8   R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
9   R!H u0 {4,T} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.734997132, -9.268210325, -10.01780688, -10.60167495, -10.04247036, -7.772781071, -7.01107457],'cal/(mol*K)'),
        H298 = (63.69412906,'kcal/mol'),
        S298 = (48.26001912,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained cyclohex_1_yne_3_ene ring:
polycyclic(s3_6_6_yne_1_ene_3) = polycyclic(s3_6_6_ane) - ring(Cyclohexane) + ring(cyclohex_1_yne_3_ene)
""",
)

entry(
    index = 0,
    label = "s3_6_7_yne",
    group = "OR{s3_6_7_yne_6}",
    thermo = None,
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 221,
    label = "s3_6_7_yne_6",
    group =
"""
1    R!H u0 {3,[S,D,T,B]} {6,S} {7,[S,D,T,B]}
2    R!H u0 {3,[S,D,T,B]} {4,S} {5,[S,D,T,B]}
3    R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4  * R!H u0 {2,S} {8,T}
5    R!H u0 {2,[S,D,T,B]} {9,[S,D,T,B]}
6    R!H u0 {1,S} {8,S}
7    R!H u0 {1,[S,D,T,B]} {10,[S,D,T,B]}
8    R!H u0 {4,T} {6,S}
9    R!H u0 {5,[S,D,T,B]} {10,[S,D,T,B]}
10   R!H u0 {7,[S,D,T,B]} {9,[S,D,T,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.952391013, -10.16233652, -9.736894837, -9.682011472, -8.449983748, -6.509280115, -6.195745698],'cal/(mol*K)'),
        H298 = (59.10352964,'kcal/mol'),
        S298 = (41.49386023,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained cyclohexadyne ring:
polycyclic(s3_6_7_yne_6) = polycyclic(s3_6_7_ane) - ring(Cyclohexane) + ring(cyclohexyne)
""",
)

entry(
    index = 0,
    label = "s3_6_7_yne_ene",
    group = "OR{s3_6_7_yne_6_ene_8}",
    thermo = None,
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 221,
    label = "s3_6_7_yne_6_ene_8",
    group =
"""
1    R!H u0 {3,[S,D,T,B]} {6,D} {7,[S,D,T,B]}
2    R!H u0 {3,[S,D,T,B]} {4,S} {5,[S,D,T,B]}
3    R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4  * R!H u0 {2,S} {8,T}
5    R!H u0 {2,[S,D,T,B]} {9,[S,D,T,B]}
6    R!H u0 {1,D} {8,S}
7    R!H u0 {1,[S,D,T,B]} {10,[S,D,T,B]}
8    R!H u0 {4,T} {6,S}
9    R!H u0 {5,[S,D,T,B]} {10,[S,D,T,B]}
10   R!H u0 {7,[S,D,T,B]} {9,[S,D,T,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.938391013, -9.35133652, -10.14089484, -10.64001147, -9.720983748, -7.216280115, -6.224745698],'cal/(mol*K)'),
        H298 = (67.28052964,'kcal/mol'),
        S298 = (45.26456023,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated""",
    longDesc =
u"""
Estimated according to the following equation in order to take into account the highly strained cyclohex_1_yne_3_ene ring:
polycyclic(s3_6_7_yne_6_ene_8) = polycyclic(s3_6_7_ane) - ring(Cyclohexane) + ring(cyclohex_1_yne_3_ene)
""",
)

tree(
"""
L1: PolycyclicRing
    L2: s2-3_5_5_5_ane
    L2: s2-3_5d1_5_5_ene
    L2: s2-3f0_5_5_5_ane
    L2: s2-3f1_6_5_5_ane
    L2: s2-3_5_5_5d1_ene
    L2: s3-3_5_6_5_ane
    L2: s2-4f1_5_6_7_ane
    L2: s2-4f2_5_6_8_ane
    L2: s2-2f1_5_5_2_ane
    L2: s2-3f1_5_5_6_ane
    L2: s2-4f0_5_5_6_ane
    L2: s2-4f1_5_5_7_ane
    L2: s4-3f1_6_6_6_ane
    L2: s3-3f1_6_5_6_ane
    L2: s1-2_5d1d3_3_5d1_triene
    L2: s2-2_5d1_3_6d1d3_triene
    L2: s1_3_3
        L3: s1_3_3_ane
        L3: s1_3_3_ene
    L2: s1_3_4
        L3: s1_3_4_ane
        L3: s1_3_4_ene
    L2: s1_3_5
        L3: s1_3_5_ane
        L3: s1_3_5_ene
            L4: s1_3_5_ene_1
            L4: s1_3_5_ene_2
        L3: s1_3_5_diene
            L4: s1_3_5_diene_1_3
    L2: s1_3_6
        L3: s1_3_6_ane
        L3: s1_3_6_ene
            L4: s1_3_6_ene_1
            L4: s1_3_6_ene_2
        L3: s1_3_6_diene
            L4: s1_3_6_diene_1_4
            L4: s1_3_6_diene_1_3
    L2: s1_4_4
        L3: s1_4_4_ane
        L3: s1_4_4_ene
            L4: s1_4_4_ene_1
        L3: s1_4_4_diene
            L4: s1_4_4_diene_1_5
    L2: s1_4_5
        L3: s1_4_5_ane
        L3: s1_4_5_ene
            L4: s1_4_5_ene_1
            L4: s1_4_5_ene_2
            L4: s1_4_5_ene_6
        L3: s1_4_5_diene
            L4: s1_4_5_diene_1_3
            L4: s1_4_5_diene_1_6
            L4: s1_4_5_diene_2_6
    L2: s1_4_6
        L3: s1_4_6_ane
        L3: s1_4_6_ene
            L4: s1_4_6_ene_1
            L4: s1_4_6_ene_2
            L4: s1_4_6_ene_7
        L3: s1_4_6_diene
            L4: s1_4_6_diene_1_3
            L4: s1_4_6_diene_1_4
            L4: s1_4_6_diene_1_7
            L4: s1_4_6_diene_2_7
    L2: s1_5_5
        L3: s1_5_5_ane
        L3: s1_5_5_ene
            L4: s1_5_5_ene_1
            L4: s1_5_5_ene_2
        L3: s1_5_5_diene
            L4: s1_5_5_diene_1_3
            L4: s1_5_5_diene_1_6
            L4: s1_5_5_diene_1_7
            L4: s1_5_5_diene_2_7
    L2: s1_5_6
        L3: s1_5_6_ane
        L3: s1_5_6_ene
            L4: s1_5_6_ene_1
            L4: s1_5_6_ene_2
            L4: s1_5_6_ene_7
            L4: s1_5_6_ene_8
        L3: s1_5_6_diene
            L4: s1_5_6_diene_1_3
            L4: s1_5_6_diene_1_4
            L4: s1_5_6_diene_1_7
            L4: s1_5_6_diene_1_8
            L4: s1_5_6_diene_2_7
            L4: s1_5_6_diene_2_8
            L4: s1_5_6_diene_7_9
        L3: s1_5_6_triene
            L4: s1_5_6_triene_1_3_7
            L4: s1_5_6_triene_1_3_8
        L3: s1_5_6_tetraene
            L4: s1_5_6_tetraene_1_3_7_9
            L4: s1_5_6_tetraene_1_4_7_9
    L2: s1_6_6
        L3: s1_6_6_ane
        L3: s1_6_6_ene
            L4: s1_6_6_ene_1
            L4: s1_6_6_ene_2
        L3: s1_6_6_diene
            L4: s1_6_6_diene_1_3
            L4: s1_6_6_diene_1_4
            L4: s1_6_6_diene_1_7
            L4: s1_6_6_diene_1_8
            L4: s1_6_6_diene_2_8
    L2: s2_3_3
        L3: s2_3_3_ane
        L3: s2_3_3_ene
    L2: s2_3_4
        L3: s2_3_4_ane
        L3: s2_3_4_ene
            L4: s2_3_4_ene_1
            L4: s2_3_4_ene_m
    L2: s2_3_5
        L3: s2_3_5_ene
            L4: s2_3_5_ene_1_side
            L4: s2_3_5_ene_1
            L4: s2_3_5_ene_side 
        L3: s2_3_5_ane
        L3: s2_3_5_diene
            L4: s2_3_5_diene_0_2
        L3: s2_3_(1_2_CPD)
            L4: s2_3_5_diene_1_2
            L4: s2_3_5_diene_0_1
        L3: s2_3_5_yne_1
    L2: s2_3_6
        L3: s2_3_6_ane
        L3: s2_3_6_ene
            L4: s2_3_6_ene_1
            L4: s2_3_6_ene_2
            L4: s2_3_6_ene_5
        L3: s2_3_6_diene
            L4: s2_3_6_diene_0_2
            L4: s2_3_6_diene_0_3
            L4: s2_3_6_diene_1_3
            L4: s2_3_6_diene_2_5
            L4: s2_3_6_diene_1_6
        L3: s2_3_6_ben
        L3: s2_3_6_yne
            L4: s2_3_6_yne_1
            L4: s2_3_6_yne_2
        L3: s2_3_6_yne_ene
            L4: s2_3_6_yne_1_ene_4
            L4: s2_3_6_yne_1_ene_3
            L4: s2_3_6_yne_2_ene_4
        L3: s2_3_6_diyne_1_3
    L2: s2_3_7
        L3: s2_3_7_ane
    L2: s2_3_8
        L3: s2_3_8_ane
    L2: s2_4_4
        L3: s2_4_4_ane
        L3: s2_4_4_ene
            L4: s2_4_4_ene_1
            L4: s2_4_4_ene_m
        L3: s2_4_4_diene
            L4: s2_4_4_diene_1_m
    L2: s2_4_5
        L3: s2_4_5_ane
        L3: s2_4_5_ene
            L4: s2_4_5_ene_0
            L4: s2_4_5_ene_1
        L3: s2_4_5_diene
            L4: s2_4_5_diene_0_3
            L4: s2_4_5_diene_1_5
            L4: s2_4_5_diene_4_6
        L3: s2_4_(1_2_CPD)
            L4: s2_4_5_diene_1_2
            L4: s2_4_5_diene_0_1
        L3: s2_4_5_yne_1
    L2: s2_4_6
        L3: s2_4_6_ane
        L3: s2_4_6_ene
            L4: s2_4_6_ene_1
            L4: s2_4_6_ene_2
            L4: s2_4_6_ene_6
        L3: s2_4_6_diene
            L4: s2_4_6_diene_1_3
            L4: s2_4_6_diene_1_6
            L4: s2_4_6_diene_2_6
            L4: s2_4_6_diene_5_7
        L3: s2_4_6_ben
        L3: s2_4_6_yne
            L4: s2_4_6_yne_1
            L4: s2_4_6_yne_2
        L3: s2_4_6_yne_ene
            L4: s2_4_6_yne_1_ene_4
            L4: s2_4_6_yne_1_ene_3
            L4: s2_4_6_yne_2_ene_4
        L3: s2_4_6_diyne_1_3
    L2: s2_5_5
        L3: s2_5_5_ane
        L3: s2_5_5_ene
            L4: s2_5_5_ene_0
            L4: s2_5_5_ene_1
            L4: s2_5_5_ene_m
        L3: s2_5_5_diene
            L4: s2_5_5_diene_0_2
            L4: s2_5_5_diene_0_3
            L4: s2_5_5_diene_m_2
            L4: s2_5_5_diene_0_4
            L4: s2_5_5_diene_0_5
            L4: s2_5_5_diene_0_6
            L4: s2_5_5_diene_1_5
            L4: s2_5_5_diene_1_6
        L3: s2_5_5_tetraene
            L4: s2_5_5_tetraene_0_2_4_6
        L3: s2_5_(1_2_CPD)
            L4: s2_5_5_diene_1_2
            L4: s2_5_5_diene_0_1
        L3: s2_5_5_yne_1
    L2: s2_5_6
        L3: s2_5_6_ane
        L3: s2_5_6_ene
            L4: s2_5_6_ene_0
            L4: s2_5_6_ene_1
            L4: s2_5_6_ene_m
            L4: s2_5_6_ene_2
            L4: s2_5_6_ene_5
            L4: s2_5_6_ene_6
        L3: s2_5_6_diene
            L4: s2_5_6_diene_m_1
            L4: s2_5_6_diene_m_2
            L4: s2_5_6_diene_m_7
            L4: s2_5_6_diene_0_2
            L4: s2_5_6_diene_0_3
            L4: s2_5_6_diene_0_4
            L4: s2_5_6_diene_0_5
            L4: s2_5_6_diene_0_6
            L4: s2_5_6_diene_0_7
            L4: s2_5_6_diene_1_3
            L4: s2_5_6_diene_1_5
            L4: s2_5_6_diene_1_6
            L4: s2_5_6_diene_1_7
            L4: s2_5_6_diene_1_8
            L4: s2_5_6_diene_2_5
            L4: s2_5_6_diene_2_6
            L4: s2_5_6_diene_5_7
            L4: s2_5_6_diene_5_8
        L3: s2_5_6_triene
            L4: s2_5_6_triene_0_2_6
            L4: s2_5_6_triene_0_2_7
            L4: s2_5_6_triene_0_3_7
            L4: s2_5_6_triene_1_3_5
            L4: s2_5_6_triene_1_3_6
            L4: s2_5_6_triene_1_6_8
            L4: s2_5_6_triene_2_5_7
            L4: s2_5_6_triene_m_1_7
            L4: s2_5_6_triene_m_2_6
        L3: s2_5_6_tetraene
            L4: s2_5_6_tetraene_1_3_5_7
            L4: s2_5_6_tetraene_1_3_5_8
        L3: s2_5_6_ben
        L3: s2_5_6_indene
        L3: s2_5_6_ben_yne_1
            L4: s2_5_6_ben_yne_1_res1
            L4: s2_5_6_ben_yne_1_res2
            L4: s2_5_6_ben_yne_1_res3
        L3: s2_(1_2_CPD)_6
            L4: s2_5_6_diene_6_7
            L4: s2_5_6_diene_5_6
        L3: s2_5_6_yne_6
        L3: s2_5_6_hexyne
            L4: s2_5_6_yne_1
            L4: s2_5_6_yne_2
        L3: s2_5_6_yne_ene
            L4: s2_5_6_yne_1_ene_4
            L4: s2_5_6_yne_1_ene_3
            L4: s2_5_6_yne_2_ene_4
        L3: s2_5_6_diyne_1_3
    L2: s2_5_7
        L3: s2_5_7_triene
            L4: s2_5_7_triene_0_2_8
            L4: s2_5_7_triene_0_3_8
            L4: s2_5_7_triene_1_3_7
            L4: s2_5_7_triene_1_3_8
            L4: s2_5_7_triene_1_3_9
            L4: s2_5_7_triene_1_4_7
        L3: s2_5_7_tetraene
            L4: s2_5_7_tetraene_0_2_4_8
            L4: s2_5_7_tetraene_1_3_7_9
            L4: s2_5_7_tetraene_m_1_3_8
        L3: s2_(1_2_CPD)_7
            L4: s2_5_7_diene_7_8
            L4: s2_5_7_diene_6_7
        L3: s2_5_7_yne_7
    L2: s2_6_6
        L3: s2_6_6_ane
        L3: s2_6_6_ene
            L4: s2_6_6_ene_0
            L4: s2_6_6_ene_1
            L4: s2_6_6_ene_2
            L4: s2_6_6_ene_m
        L3: s2_6_6_diene
            L4: s2_6_6_diene_m_1
            L4: s2_6_6_diene_m_2
            L4: s2_6_6_diene_0_2
            L4: s2_6_6_diene_0_3
            L4: s2_6_6_diene_0_4
            L4: s2_6_6_diene_0_5
            L4: s2_6_6_diene_0_6
            L4: s2_6_6_diene_0_7
            L4: s2_6_6_diene_0_8
            L4: s2_6_6_diene_1_3
            L4: s2_6_6_diene_1_6
            L4: s2_6_6_diene_1_7
            L4: s2_6_6_diene_1_8
            L4: s2_6_6_diene_2_7
        L3: s2_6_6_triene
            L4: s2_6_6_triene_0_2_6
            L4: s2_6_6_triene_0_2_7
            L4: s2_6_6_triene_0_3_7
            L4: s2_6_6_triene_1_3_6
            L4: s2_6_6_triene_1_3_7
        L3: s2_6_6_tetraene
            L4: s2_6_6_tetraene_0_2_4_7
            L4: s2_6_6_tetraene_0_2_5_7
            L4: s2_6_6_tetraene_0_2_6_8
            L4: s2_6_6_tetraene_0_3_6_8
            L4: s2_6_6_tetraene_1_3_6_8
        L3: s2_6_6_ben
        L3: s2_6_6_ben_ene
            L4: s2_6_6_ben_ene_1
            L4: s2_6_6_ben_ene_2
        L3: s2_6_6_naphthalene
        L3: s2_6_6_yne
            L4: s2_6_6_yne_1
            L4: s2_6_6_yne_2
        L3: s2_6_6_yne_ene
            L4: s2_6_6_yne_1_ene_4
            L4: s2_6_6_yne_1_ene_3
            L4: s2_6_6_yne_2_ene_4
        L3: s2_6_6_diyne_1_3
    L2: s3_4_4
        L3: s3_4_4_ane
        L3: s3_4_4_ene
            L4: s3_4_4_ene_0
        L3: s3_4_4_diene
            L4: s3_4_4_diene_0_2
    L2: s3_4_5
        L3: s3_4_5_ane
        L3: s3_4_5_ene
            L4: s3_4_5_ene_0
            L4: s3_4_5_ene_1
            L4: s3_4_5_ene_3
        L3: s3_4_5_diene
            L4: s3_4_5_diene_0_2
            L4: s3_4_5_diene_0_3
            L4: s3_4_5_diene_1_3
            L4: s3_4_5_diene_3_4
    L2: s3_4_6
        L3: s3_4_6_ane
        L3: s3_4_6_ene
            L4: s3_4_6_ene_0
            L4: s3_4_6_ene_1
            L4: s3_4_6_ene_4
        L3: s3_4_6_diene
            L4: s3_4_6_diene_0_2
            L4: s3_4_6_diene_0_3
            L4: s3_4_6_diene_0_4
            L4: s3_4_6_diene_1_4
            L4: s3_4_6_diene_1_5
        L3: s3_4_6_ben_ane
            L4: s3_4_6_ben_ane_res1
            L4: s3_4_6_ben_ane_res2
        L3: s3_4_6_yne
            L4: s3_4_6_yne_1
        L3: s3_4_6_yne_ene
            L4: s3_4_6_yne_1_ene_3
    L2: s3_5_5
        L3: s3_5_5_ene
            L4: s3_5_5_ene_0
            L4: s3_5_5_ene_1
            L4: s3_5_5_ene_side
            L4: s3_5_5_ene_m
        L3: s3_5_5_ane
        L3: s3_5_5_diene
            L4: s3_5_5_diene_1_4
            L4: s3_5_5_diene_0_4
    L2: s3_5_6
        L3: s3_5_6_ane
        L3: s3_5_6_ene
            L4: s3_5_6_ene_1
            L4: s3_5_6_ene_5
        L3: s3_5_6_diene
            L4: s3_5_6_diene_1_5
        L3: s3_5_6_ben_ane
            L4: s3_5_6_ben_ane_res1
            L4: s3_5_6_ben_ane_res2
        L3: s3_5_6_ben_ene
            L4: s3_5_6_ben_ene_res1
            L4: s3_5_6_ben_ene_res2
        L3: s3_5_6_yne
            L4: s3_5_6_yne_1
        L3: s3_5_6_yne_ene
            L4: s3_5_6_yne_1_ene_3
    L2: s3_6_6
        L3: s3_6_6_ane
        L3: s3_6_6_ene
            L4: s3_6_6_ene_0
            L4: s3_6_6_ene_1
            L4: s3_6_6_ene_4
        L3: s3_6_6_diene
            L4: s3_6_6_diene_0_m
            L4: s3_6_6_diene_0_2
            L4: s3_6_6_diene_0_3
            L4: s3_6_6_diene_0_4
            L4: s3_6_6_diene_0_5
            L4: s3_6_6_diene_0_6
            L4: s3_6_6_diene_1_m
            L4: s3_6_6_diene_1_5
            L4: s3_6_6_diene_1_6
            L4: s3_6_6_diene_1_8
        L3: s3_6_6_yne
            L4: s3_6_6_yne_1
        L3: s3_6_6_yne_ene
            L4: s3_6_6_yne_1_ene_3
    L2: s3_6_7
        L3: s3_6_7_ane
        L3: s3_6_7_ene
            L4: s3_6_7_ene_6
        L3: s3_6_7_diene
            L4: s3_6_7_diene_6_9-0
        L3: s3_6_7_yne
            L4: s3_6_7_yne_6
        L3: s3_6_7_yne_ene
            L4: s3_6_7_yne_6_ene_8
    L2: s4_6_6
        L3: s4_6_6_ane
        L3: s4_6_6_ben_ben
            L4: s4_6_6_ben_ben_res1
            L4: s4_6_6_ben_ben_res2
            L4: s4_6_6_ben_ben_res3
    L2: s4_6_8
        L3: s4_6_8_ane
        L3: s4_6_8_ene
            L4: s4_6_8_ene_7
        L3: s4_6_8_diene
            L4: s4_6_8_diene_7_9
"""
)

