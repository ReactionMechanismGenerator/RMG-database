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
1   C u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2 * C u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   C u0 {1,[S,D,T,B]} {5,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {4,[S,D,T,B]}
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
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u0 {1,S} {3,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {5,S}
5   Cs u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.93,-6.5,-6.24,-5.5,-4.4,-4.35,-2.38],'cal/(mol*K)'),
        H298 = (63.59,'kcal/mol'),
        S298 = (67.15,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Properties of Liquids and Gases, Poling 5th Ed. S, Cp from PM7 calculation
""",
)

entry(
    index = 2,
    label = "s1_3_3_ene",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cd u0 {1,S} {3,D}
3   Cd u0 {1,S} {2,D}
4   Cs u0 {1,S} {5,S}
5   Cs u0 {1,S} {4,S}
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
Fitted from molecule s1_3_3_ene from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 0,
    label = "s1_3_4",
    group = 
"""
1 * C u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2   C u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   C u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
6   C u0 {4,[S,D,T,B]} {5,[S,D,T,B]}
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
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {6,S}
5   Cs u0 {1,S} {6,S}
6   Cs u0 {4,S} {5,S}
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
Fitted from molecule s1_3_4_ane from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 4,
    label = "s1_3_4_ene",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {1,S} {2,S}
4   Cd u0 {1,S} {6,D}
5   Cs u0 {1,S} {6,S}
6   Cd u0 {4,D} {5,S}
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
Fitted from molecule s1_3_4_ene from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 0,
    label = "s1_3_5",
    group = 
"""
1   C u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2   C u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   C u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6 * C u0 {4,[S,D,T,B]} {7,[S,D,T,B]}
7   C u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
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
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {6,S}
5   Cs u0 {1,S} {7,S}
6 * Cs u0 {4,S} {7,S}
7   Cs u0 {5,S} {6,S}
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
Fitted from molecule s1_3_5_ane from polycyclic_all_thermoLiabrary library.
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
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {7,S}
5   Cd u0 {1,S} {6,D}
6 * Cd u0 {5,D} {7,S}
7   Cs u0 {4,S} {6,S}
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
Fitted from molecule s1_3_5_ene_1 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 7,
    label = "s1_3_5_ene_2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {7,S}
5   Cs u0 {1,S} {6,S}
6 * Cd u0 {5,S} {7,D}
7   Cd u0 {4,S} {6,D}
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
Fitted from molecule s1_3_5_ene_2 from polycyclic_all_thermoLiabrary library.
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
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {1,S} {2,S}
4   Cd u0 {1,S} {7,D}
5   Cd u0 {1,S} {6,D}
6 * Cd u0 {5,D} {7,S}
7   Cd u0 {4,D} {6,S}
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
Fitted from molecule s1_3_5_diene_1_3 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 0,
    label = "s1_3_6",
    group = 
"""
1   C u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2   C u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   C u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   C u0 {4,[S,D,T,B]} {8,[S,D,T,B]}
7   C u0 {5,[S,D,T,B]} {8,[S,D,T,B]}
8 * C u0 {6,[S,D,T,B]} {7,[S,D,T,B]}
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
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {6,S}
5   Cs u0 {1,S} {7,S}
6   Cs u0 {4,S} {8,S}
7   Cs u0 {5,S} {8,S}
8 * Cs u0 {6,S} {7,S}
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
Fitted from molecule s1_3_6_ane from polycyclic_all_thermoLiabrary library.
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
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {6,S}
5   Cd u0 {1,S} {7,D}
6   Cs u0 {4,S} {8,S}
7   Cd u0 {5,D} {8,S}
8 * Cs u0 {6,S} {7,S}
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
Fitted from molecule s1_3_6_ene_1 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 11,
    label = "s1_3_6_ene_2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {6,S}
5   Cs u0 {1,S} {7,S}
6   Cd u0 {4,S} {8,D}
7   Cs u0 {5,S} {8,S}
8 * Cd u0 {6,D} {7,S}
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
Fitted from molecule s1_3_6_ene_2 from polycyclic_all_thermoLiabrary library.
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
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {1,S} {2,S}
4   Cd u0 {1,S} {7,D}
5   Cd u0 {1,S} {6,D}
6   Cd u0 {5,D} {8,S}
7   Cd u0 {4,D} {8,S}
8 * Cs u0 {6,S} {7,S}
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
Fitted from molecule s1_3_6_diene_1_4 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 13,
    label = "s1_3_6_diene_1_3",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {7,S}
5   Cd u0 {1,S} {6,D}
6   Cd u0 {5,D} {8,S}
7   Cd u0 {4,S} {8,D}
8 * Cd u0 {6,S} {7,D}
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
Fitted from molecule s1_3_6_diene_1_3 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 0,
    label = "s1_4_4",
    group = 
"""
1   C u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2 * C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
4   C u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
6   C u0 {4,[S,D,T,B]} {5,[S,D,T,B]}
7   C u0 {2,[S,D,T,B]} {3,[S,D,T,B]}
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
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u0 {1,S} {7,S}
3   Cs u0 {1,S} {7,S}
4   Cs u0 {1,S} {6,S}
5   Cs u0 {1,S} {6,S}
6   Cs u0 {4,S} {5,S}
7   Cs u0 {2,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-34.4131,-34.9857,-33.9212,-31.7785,-25.403,-19.1222,-9.61308],'J/(mol*K)'),
        H298 = (232.497,'kJ/mol'),
        S298 = (237.342,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_4_4_ane from polycyclic_all_thermoLiabrary library.
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
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u0 {1,S} {7,S}
3   Cs u0 {1,S} {6,S}
4   Cd u0 {1,S} {7,D}
5   Cs u0 {1,S} {6,S}
6   Cs u0 {3,S} {5,S}
7   Cd u0 {2,S} {4,D}
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
Fitted from molecule s1_4_4_ene_1 from polycyclic_all_thermoLiabrary library.
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
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cd u0 {1,S} {7,D}
3   Cs u0 {1,S} {6,S}
4   Cs u0 {1,S} {7,S}
5   Cd u0 {1,S} {6,D}
6   Cd u0 {3,S} {5,D}
7   Cd u0 {2,D} {4,S}
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
Fitted from molecule s1_4_4_diene_1_5 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 0,
    label = "s1_4_5",
    group = 
"""
1   C u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2 * C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
4   C u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
6   C u0 {3,[S,D,T,B]} {5,[S,D,T,B]}
7   C u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
8   C u0 {4,[S,D,T,B]} {7,[S,D,T,B]}
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
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u0 {1,S} {7,S}
3   Cs u0 {1,S} {6,S}
4   Cs u0 {1,S} {8,S}
5   Cs u0 {1,S} {6,S}
6   Cs u0 {3,S} {5,S}
7   Cs u0 {2,S} {8,S}
8   Cs u0 {4,S} {7,S}
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
Fitted from molecule s1_4_5_ane from polycyclic_all_thermoLiabrary library.
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
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u0 {1,S} {7,S}
3   Cs u0 {1,S} {6,S}
4   Cd u0 {1,S} {8,D}
5   Cs u0 {1,S} {6,S}
6   Cs u0 {3,S} {5,S}
7   Cs u0 {2,S} {8,S}
8   Cd u0 {4,D} {7,S}
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
Fitted from molecule s1_4_5_ene_1 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 19,
    label = "s1_4_5_ene_2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u0 {1,S} {8,S}
3   Cs u0 {1,S} {7,S}
4   Cs u0 {1,S} {6,S}
5   Cs u0 {1,S} {6,S}
6   Cs u0 {4,S} {5,S}
7   Cd u0 {3,S} {8,D}
8   Cd u0 {2,S} {7,D}
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
Fitted from molecule s1_4_5_ene_2 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 20,
    label = "s1_4_5_ene_6",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u0 {1,S} {8,S}
3   Cd u0 {1,S} {6,D}
4   Cs u0 {1,S} {6,S}
5   Cs u0 {1,S} {7,S}
6   Cd u0 {3,D} {4,S}
7   Cs u0 {5,S} {8,S}
8   Cs u0 {2,S} {7,S}
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
Fitted from molecule s1_4_5_ene_6 from polycyclic_all_thermoLiabrary library.
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
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S} {6,S}
3 * Cd u0 {1,S} {7,D}
4   Cd u0 {1,S} {8,D}
5   Cs u0 {1,S} {6,S}
6   Cs u0 {2,S} {5,S}
7   Cd u0 {3,D} {8,S}
8   Cd u0 {4,D} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-32.4653,-34.6175,-34.0012,-32.0846,-26.0869,-19.9662,-11.0011],'J/(mol*K)'),
        H298 = (159.233,'kJ/mol'),
        S298 = (245.609,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_4_5_diene_1_3 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 22,
    label = "s1_4_5_diene_1_6",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3 * Cs u0 {1,S} {7,S}
4   Cd u0 {1,S} {8,D}
5   Cs u0 {1,S} {6,S}
6   Cd u0 {2,D} {5,S}
7   Cs u0 {3,S} {8,S}
8   Cd u0 {4,D} {7,S}
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
Fitted from molecule s1_4_5_diene_1_6 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 23,
    label = "s1_4_5_diene_2_6",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u0 {1,S} {8,S}
3   Cd u0 {1,S} {6,D}
4   Cs u0 {1,S} {7,S}
5   Cs u0 {1,S} {6,S}
6   Cd u0 {3,D} {5,S}
7   Cd u0 {4,S} {8,D}
8   Cd u0 {2,S} {7,D}
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
Fitted from molecule s1_4_5_diene_2_6 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 0,
    label = "s1_4_6",
    group = 
"""
1   C u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2   C u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
4   C u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   C u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
7 * C u0 {5,[S,D,T,B]} {9,[S,D,T,B]}
8   C u0 {3,[S,D,T,B]} {9,[S,D,T,B]}
9   C u0 {7,[S,D,T,B]} {8,[S,D,T,B]}
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
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S} {6,S}
3   Cs u0 {1,S} {8,S}
4   Cs u0 {1,S} {6,S}
5   Cs u0 {1,S} {7,S}
6   Cs u0 {2,S} {4,S}
7 * Cs u0 {5,S} {9,S}
8   Cs u0 {3,S} {9,S}
9   Cs u0 {7,S} {8,S}
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
Fitted from molecule s1_4_6_ane from polycyclic_all_thermoLiabrary library.
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
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S} {6,S}
3   Cd u0 {1,S} {8,D}
4   Cs u0 {1,S} {6,S}
5   Cs u0 {1,S} {7,S}
6   Cs u0 {2,S} {4,S}
7 * Cs u0 {5,S} {9,S}
8   Cd u0 {3,D} {9,S}
9   Cs u0 {7,S} {8,S}
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
Fitted from molecule s1_4_6_ene_1 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 26,
    label = "s1_4_6_ene_2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S} {7,S}
3   Cs u0 {1,S} {6,S}
4   Cs u0 {1,S} {6,S}
5   Cs u0 {1,S} {8,S}
6   Cs u0 {3,S} {4,S}
7 * Cs u0 {2,S} {9,S}
8   Cd u0 {5,S} {9,D}
9   Cd u0 {7,S} {8,D}
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
Fitted from molecule s1_4_6_ene_2 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 27,
    label = "s1_4_6_ene_7",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S} {8,S}
4   Cs u0 {1,S} {7,S}
5   Cs u0 {1,S} {6,S}
6   Cd u0 {2,D} {5,S}
7 * Cs u0 {4,S} {9,S}
8   Cs u0 {3,S} {9,S}
9   Cs u0 {7,S} {8,S}
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
Fitted from molecule s1_4_6_ene_7 from polycyclic_all_thermoLiabrary library.
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
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S} {8,S}
3   Cs u0 {1,S} {6,S}
4   Cd u0 {1,S} {7,D}
5   Cs u0 {1,S} {6,S}
6   Cs u0 {3,S} {5,S}
7 * Cd u0 {4,D} {9,S}
8   Cd u0 {2,S} {9,D}
9   Cd u0 {7,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-34.3954,-38.5478,-38.7261,-35.7498,-27.2334,-19.7066,-9.56136],'J/(mol*K)'),
        H298 = (144.043,'kJ/mol'),
        S298 = (223.141,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_4_6_diene_1_3 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 29,
    label = "s1_4_6_diene_1_4",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {8,D}
3   Cs u0 {1,S} {6,S}
4   Cs u0 {1,S} {6,S}
5   Cd u0 {1,S} {7,D}
6   Cs u0 {3,S} {4,S}
7 * Cd u0 {5,D} {9,S}
8   Cd u0 {2,D} {9,S}
9   Cs u0 {7,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-29.6317,-31.557,-31.0009,-28.4484,-21.7675,-15.7389,-6.57024],'J/(mol*K)'),
        H298 = (125.442,'kJ/mol'),
        S298 = (213.238,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_4_6_diene_1_4 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 30,
    label = "s1_4_6_diene_1_7",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S} {6,S}
4   Cd u0 {1,S} {8,D}
5   Cs u0 {1,S} {7,S}
6   Cd u0 {2,D} {3,S}
7 * Cs u0 {5,S} {9,S}
8   Cd u0 {4,D} {9,S}
9   Cs u0 {7,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-30.0071,-31.6425,-31.139,-28.718,-22.1294,-15.8216,-6.75412],'J/(mol*K)'),
        H298 = (152.104,'kJ/mol'),
        S298 = (209.901,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_4_6_diene_1_7 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 31,
    label = "s1_4_6_diene_2_7",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S} {8,S}
4   Cs u0 {1,S} {6,S}
5   Cs u0 {1,S} {7,S}
6   Cd u0 {2,D} {4,S}
7 * Cd u0 {5,S} {9,D}
8   Cs u0 {3,S} {9,S}
9   Cd u0 {7,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-28.6922,-31.497,-31.5769,-29.3817,-22.756,-16.3784,-7.21136],'J/(mol*K)'),
        H298 = (150.509,'kJ/mol'),
        S298 = (206.455,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_4_6_diene_2_7 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 0,
    label = "s1_5_5",
    group = 
"""
1   C u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2 * C u0 {1,[S,D,T,B]} {9,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
4   C u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
6   C u0 {4,[S,D,T,B]} {7,[S,D,T,B]}
7   C u0 {3,[S,D,T,B]} {6,[S,D,T,B]}
8   C u0 {5,[S,D,T,B]} {9,[S,D,T,B]}
9   C u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
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
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u0 {1,S} {9,S}
3   Cs u0 {1,S} {7,S}
4   Cs u0 {1,S} {6,S}
5   Cs u0 {1,S} {8,S}
6   Cs u0 {4,S} {7,S}
7   Cs u0 {3,S} {6,S}
8   Cs u0 {5,S} {9,S}
9   Cs u0 {2,S} {8,S}
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
Fitted from molecule s1_5_5_ane from polycyclic_all_thermoLiabrary library.
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
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u0 {1,S} {9,S}
3   Cd u0 {1,S} {6,D}
4   Cs u0 {1,S} {8,S}
5   Cs u0 {1,S} {7,S}
6   Cd u0 {3,D} {8,S}
7   Cs u0 {5,S} {9,S}
8   Cs u0 {4,S} {6,S}
9   Cs u0 {2,S} {7,S}
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
Fitted from molecule s1_5_5_ene_1 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 34,
    label = "s1_5_5_ene_2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u0 {1,S} {7,S}
3   Cs u0 {1,S} {6,S}
4   Cs u0 {1,S} {9,S}
5   Cs u0 {1,S} {8,S}
6   Cd u0 {3,S} {9,D}
7   Cs u0 {2,S} {8,S}
8   Cs u0 {5,S} {7,S}
9   Cd u0 {4,S} {6,D}
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
Fitted from molecule s1_5_5_ene_2 from polycyclic_all_thermoLiabrary library.
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
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cd u0 {1,S} {7,D}
3   Cd u0 {1,S} {8,D}
4   Cs u0 {1,S} {9,S}
5   Cs u0 {1,S} {6,S}
6   Cs u0 {5,S} {9,S}
7   Cd u0 {2,D} {8,S}
8   Cd u0 {3,D} {7,S}
9   Cs u0 {4,S} {6,S}
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
Fitted from molecule s1_5_5_diene_1_3 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 36,
    label = "s1_5_5_diene_1_6",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u0 {1,S} {6,S}
3   Cs u0 {1,S} {8,S}
4   Cd u0 {1,S} {9,D}
5   Cd u0 {1,S} {7,D}
6   Cs u0 {2,S} {7,S}
7   Cd u0 {5,D} {6,S}
8   Cs u0 {3,S} {9,S}
9   Cd u0 {4,D} {8,S}
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
Fitted from molecule s1_5_5_diene_1_6 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 37,
    label = "s1_5_5_diene_1_7",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cd u0 {1,S} {7,D}
3   Cs u0 {1,S} {6,S}
4   Cs u0 {1,S} {9,S}
5   Cs u0 {1,S} {8,S}
6   Cd u0 {3,S} {9,D}
7   Cd u0 {2,D} {8,S}
8   Cs u0 {5,S} {7,S}
9   Cd u0 {4,S} {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-30.8102,-32.131,-31.3959,-29.4797,-23.177,-16.6584,-6.86736],'J/(mol*K)'),
        H298 = (76.7183,'kJ/mol'),
        S298 = (207.406,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_5_5_diene_1_7 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 38,
    label = "s1_5_5_diene_2_7",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u0 {1,S} {9,S}
3   Cs u0 {1,S} {8,S}
4   Cs u0 {1,S} {7,S}
5   Cs u0 {1,S} {6,S}
6   Cd u0 {5,S} {8,D}
7   Cd u0 {4,S} {9,D}
8   Cd u0 {3,S} {6,D}
9   Cd u0 {2,S} {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-18.2652,-21.792,-24.7369,-25.4717,-23.139,-19.1903,-12.9414],'J/(mol*K)'),
        H298 = (797.365,'kJ/mol'),
        S298 = (219.58,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_5_5_diene_2_7 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 0,
    label = "s1_5_6",
    group = 
"""
1    C u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2    C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
3    C u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
4    C u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
5    C u0 {1,[S,D,T,B]} {9,[S,D,T,B]}
6  * C u0 {3,[S,D,T,B]} {7,[S,D,T,B]}
7    C u0 {2,[S,D,T,B]} {6,[S,D,T,B]}
8    C u0 {4,[S,D,T,B]} {10,[S,D,T,B]}
9    C u0 {5,[S,D,T,B]} {10,[S,D,T,B]}
10   C u0 {8,[S,D,T,B]} {9,[S,D,T,B]}
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
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {7,S}
3    Cs u0 {1,S} {6,S}
4    Cs u0 {1,S} {8,S}
5    Cs u0 {1,S} {9,S}
6  * Cs u0 {3,S} {7,S}
7    Cs u0 {2,S} {6,S}
8    Cs u0 {4,S} {10,S}
9    Cs u0 {5,S} {10,S}
10   Cs u0 {8,S} {9,S}
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
Fitted from molecule s1_5_6_ane from polycyclic_all_thermoLiabrary library.
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
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S} {8,S}
5    Cs u0 {1,S} {9,S}
6  * Cs u0 {2,S} {9,S}
7    Cd u0 {3,D} {10,S}
8    Cs u0 {4,S} {10,S}
9    Cs u0 {5,S} {6,S}
10   Cs u0 {7,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-42.0821,-41.9684,-39.8751,-35.7244,-25.4772,-16.6259,-3.82272],'J/(mol*K)'),
        H298 = (62.2061,'kJ/mol'),
        S298 = (190.267,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_5_6_ene_1 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 41,
    label = "s1_5_6_ene_2",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S}
3    Cs u0 {1,S} {8,S}
4    Cs u0 {1,S} {7,S}
5    Cs u0 {1,S} {9,S}
6    Cs u0 {2,S} {10,S}
7  * Cs u0 {4,S} {9,S}
8    Cd u0 {3,S} {10,D}
9    Cs u0 {5,S} {7,S}
10   Cd u0 {6,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-42.4501,-42.3864,-40.2891,-36.1214,-25.8242,-16.6629,-3.97572],'J/(mol*K)'),
        H298 = (63.2789,'kJ/mol'),
        S298 = (181.962,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_5_6_ene_2 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 42,
    label = "s1_5_6_ene_7",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {7,S}
3    Cd u0 {1,S} {8,D}
4    Cs u0 {1,S} {6,S}
5    Cs u0 {1,S} {9,S}
6    Cs u0 {4,S} {10,S}
7    Cs u0 {2,S} {10,S}
8  * Cd u0 {3,D} {9,S}
9    Cs u0 {5,S} {8,S}
10   Cs u0 {6,S} {7,S}
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
Fitted from molecule s1_5_6_ene_7 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 43,
    label = "s1_5_6_ene_8",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {7,S}
3    Cs u0 {1,S} {6,S}
4    Cs u0 {1,S} {9,S}
5    Cs u0 {1,S} {8,S}
6  * Cd u0 {3,S} {8,D}
7    Cs u0 {2,S} {10,S}
8    Cd u0 {5,S} {6,D}
9    Cs u0 {4,S} {10,S}
10   Cs u0 {7,S} {9,S}
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
Fitted from molecule s1_5_6_ene_8 from polycyclic_all_thermoLiabrary library.
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
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {9,S}
3    Cs u0 {1,S} {8,S}
4    Cd u0 {1,S} {6,D}
5    Cs u0 {1,S} {7,S}
6    Cd u0 {4,D} {10,S}
7  * Cs u0 {5,S} {9,S}
8    Cd u0 {3,S} {10,D}
9    Cs u0 {2,S} {7,S}
10   Cd u0 {6,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-39.7954,-42.8746,-42.2591,-38.4302,-28.2193,-19.3441,-7.24736],'J/(mol*K)'),
        H298 = (72.801,'kJ/mol'),
        S298 = (204.461,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_5_6_diene_1_3 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 45,
    label = "s1_5_6_diene_1_4",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S}
3    Cd u0 {1,S} {8,D}
4    Cd u0 {1,S} {9,D}
5    Cs u0 {1,S} {7,S}
6  * Cs u0 {2,S} {7,S}
7    Cs u0 {5,S} {6,S}
8    Cd u0 {3,D} {10,S}
9    Cd u0 {4,D} {10,S}
10   Cs u0 {8,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-35.6657,-36.4898,-35.0189,-31.5118,-22.9934,-15.5385,-4.36224],'J/(mol*K)'),
        H298 = (59.3275,'kJ/mol'),
        S298 = (200.02,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_5_6_diene_1_4 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 46,
    label = "s1_5_6_diene_1_7",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {7,S}
3    Cs u0 {1,S} {6,S}
4    Cd u0 {1,S} {9,D}
5    Cd u0 {1,S} {8,D}
6    Cs u0 {3,S} {10,S}
7  * Cs u0 {2,S} {9,S}
8    Cd u0 {5,D} {10,S}
9    Cd u0 {4,D} {7,S}
10   Cs u0 {6,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-35.9881,-36.4223,-34.915,-31.4934,-23.0673,-15.4092,-4.57912],'J/(mol*K)'),
        H298 = (58.6857,'kJ/mol'),
        S298 = (188.477,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_5_6_diene_1_7 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 47,
    label = "s1_5_6_diene_1_8",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {8,D}
3    Cs u0 {1,S} {6,S}
4    Cs u0 {1,S} {9,S}
5    Cs u0 {1,S} {7,S}
6  * Cd u0 {3,S} {9,D}
7    Cs u0 {5,S} {10,S}
8    Cd u0 {2,D} {10,S}
9    Cd u0 {4,S} {6,D}
10   Cs u0 {7,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-34.6342,-36.1588,-35.1599,-31.9161,-23.4179,-15.7109,-4.90436],'J/(mol*K)'),
        H298 = (57.6654,'kJ/mol'),
        S298 = (185.08,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_5_6_diene_1_8 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 48,
    label = "s1_5_6_diene_2_7",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {7,S}
3    Cd u0 {1,S} {9,D}
4    Cs u0 {1,S} {8,S}
5    Cs u0 {1,S} {6,S}
6  * Cs u0 {5,S} {9,S}
7    Cs u0 {2,S} {10,S}
8    Cd u0 {4,S} {10,D}
9    Cd u0 {3,D} {6,S}
10   Cd u0 {7,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-34.7112,-36.2698,-35.2949,-32.0641,-23.5659,-15.8379,-4.96036],'J/(mol*K)'),
        H298 = (53.8784,'kJ/mol'),
        S298 = (184.339,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_5_6_diene_2_7 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 49,
    label = "s1_5_6_diene_2_8",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S}
3    Cs u0 {1,S} {9,S}
4    Cs u0 {1,S} {7,S}
5    Cs u0 {1,S} {8,S}
6  * Cd u0 {2,S} {7,D}
7    Cd u0 {4,S} {6,D}
8    Cd u0 {5,S} {10,D}
9    Cs u0 {3,S} {10,S}
10   Cd u0 {8,D} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-35.2712,-36.7778,-35.6669,-32.3211,-23.6669,-15.6059,-4.94136],'J/(mol*K)'),
        H298 = (60.7522,'kJ/mol'),
        S298 = (183.826,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_5_6_diene_2_8 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 50,
    label = "s1_5_6_diene_7_9",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3    Cs u0 {1,S} {7,S}
4    Cs u0 {1,S} {9,S}
5    Cd u0 {1,S} {8,D}
6  * Cd u0 {2,D} {8,S}
7    Cs u0 {3,S} {10,S}
8    Cd u0 {5,D} {6,S}
9    Cs u0 {4,S} {10,S}
10   Cs u0 {7,S} {9,S}
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
Fitted from molecule s1_5_6_diene_7_9 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 0,
    label = "s1_6_6",
    group = 
"""
1    C u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2    C u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
3    C u0 {1,[S,D,T,B]} {9,[S,D,T,B]}
4    C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
5    C u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
6    C u0 {5,[S,D,T,B]} {11,[S,D,T,B]}
7    C u0 {4,[S,D,T,B]} {10,[S,D,T,B]}
8    C u0 {2,[S,D,T,B]} {11,[S,D,T,B]}
9    C u0 {3,[S,D,T,B]} {10,[S,D,T,B]}
10 * C u0 {7,[S,D,T,B]} {9,[S,D,T,B]}
11   C u0 {6,[S,D,T,B]} {8,[S,D,T,B]}
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
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {8,S}
3    Cs u0 {1,S} {9,S}
4    Cs u0 {1,S} {7,S}
5    Cs u0 {1,S} {6,S}
6    Cs u0 {5,S} {11,S}
7    Cs u0 {4,S} {10,S}
8    Cs u0 {2,S} {11,S}
9    Cs u0 {3,S} {10,S}
10 * Cs u0 {7,S} {9,S}
11   Cs u0 {6,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-55.7171,-52.1059,-47.8292,-41.7251,-27.7865,-16.1164,0.04892],'J/(mol*K)'),
        H298 = (46.8142,'kJ/mol'),
        S298 = (148.984,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_6_6_ane from polycyclic_all_thermoLiabrary library.
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
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {9,S}
3    Cs u0 {1,S} {8,S}
4    Cs u0 {1,S} {7,S}
5    Cd u0 {1,S} {6,D}
6    Cd u0 {5,D} {11,S}
7    Cs u0 {4,S} {11,S}
8    Cs u0 {3,S} {10,S}
9    Cs u0 {2,S} {10,S}
10 * Cs u0 {8,S} {9,S}
11   Cs u0 {6,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-47.3531,-46.0382,-43.0651,-38.0298,-26.1211,-16.0345,-1.56372],'J/(mol*K)'),
        H298 = (43.6103,'kJ/mol'),
        S298 = (157.914,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_6_6_ene_1 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 53,
    label = "s1_6_6_ene_2",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {9,S}
3    Cs u0 {1,S} {8,S}
4    Cs u0 {1,S} {7,S}
5    Cs u0 {1,S} {6,S}
6    Cs u0 {5,S} {10,S}
7    Cs u0 {4,S} {11,S}
8    Cd u0 {3,S} {10,D}
9    Cs u0 {2,S} {11,S}
10 * Cd u0 {6,S} {8,D}
11   Cs u0 {7,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-47.8381,-46.4782,-43.3751,-38.2268,-26.1521,-15.7124,-1.41572],'J/(mol*K)'),
        H298 = (44.1274,'kJ/mol'),
        S298 = (154.518,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_6_6_ene_2 from polycyclic_all_thermoLiabrary library.
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
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3    Cs u0 {1,S} {9,S}
4    Cs u0 {1,S} {8,S}
5    Cs u0 {1,S} {7,S}
6    Cd u0 {2,D} {11,S}
7    Cs u0 {5,S} {10,S}
8    Cs u0 {4,S} {10,S}
9    Cd u0 {3,S} {11,D}
10 * Cs u0 {7,S} {8,S}
11   Cd u0 {6,S} {9,D}
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
Fitted from molecule s1_6_6_diene_1_3 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 55,
    label = "s1_6_6_diene_1_4",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {9,D}
3    Cd u0 {1,S} {6,D}
4    Cs u0 {1,S} {7,S}
5    Cs u0 {1,S} {8,S}
6    Cd u0 {3,D} {10,S}
7    Cs u0 {4,S} {11,S}
8    Cs u0 {5,S} {11,S}
9    Cd u0 {2,D} {10,S}
10 * Cs u0 {6,S} {9,S}
11   Cs u0 {7,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-40.5047,-40.1906,-37.9209,-33.5862,-23.4803,-14.826,-2.00624],'J/(mol*K)'),
        H298 = (39.1356,'kJ/mol'),
        S298 = (169.445,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_6_6_diene_1_4 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 56,
    label = "s1_6_6_diene_1_7",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {9,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S} {6,S}
5    Cd u0 {1,S} {8,D}
6    Cs u0 {4,S} {10,S}
7    Cd u0 {3,D} {11,S}
8    Cd u0 {5,D} {10,S}
9    Cs u0 {2,S} {11,S}
10 * Cs u0 {6,S} {8,S}
11   Cs u0 {7,S} {9,S}
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
Fitted from molecule s1_6_6_diene_1_7 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 57,
    label = "s1_6_6_diene_1_8",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S}
3    Cs u0 {1,S} {9,S}
4    Cs u0 {1,S} {7,S}
5    Cd u0 {1,S} {8,D}
6    Cs u0 {2,S} {10,S}
7    Cs u0 {4,S} {11,S}
8    Cd u0 {5,D} {10,S}
9    Cd u0 {3,S} {11,D}
10 * Cs u0 {6,S} {8,S}
11   Cd u0 {7,S} {9,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-38.8102,-39.3236,-37.7479,-33.8445,-23.9558,-15.1125,-2.58536],'J/(mol*K)'),
        H298 = (42.1676,'kJ/mol'),
        S298 = (164.025,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s1_6_6_diene_1_8 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 58,
    label = "s1_6_6_diene_2_8",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S}
3    Cs u0 {1,S} {7,S}
4    Cs u0 {1,S} {8,S}
5    Cs u0 {1,S} {9,S}
6    Cs u0 {2,S} {10,S}
7    Cd u0 {3,S} {11,D}
8    Cs u0 {4,S} {11,S}
9    Cd u0 {5,S} {10,D}
10 * Cd u0 {6,S} {9,D}
11   Cd u0 {7,D} {8,S}
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
Fitted from molecule s1_6_6_diene_2_8 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 0,
    label = "s2_3_3",
    group = 
"""
1   C u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]}
2   C u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]}
3 * C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
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
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {3,S} {4,S}
3 * Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.74,-5.18,-4.85,-4.17,-3.61,-4.01,-3.22],'cal/(mol*K)'),
        H298 = (65.52,'kcal/mol'),
        S298 = (69.9,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Modified to match experimental data from NIST, S and cp from PM7 calculation
""",
)

entry(
    index = 60,
    label = "s2_3_3_ene",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {3,S} {4,D}
3 * Cs u0 {1,S} {2,S}
4   Cd u0 {1,S} {2,D}
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
Fitted from molecule s2_3_3_ene from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 0,
    label = "s2_3_4",
    group = 
"""
1 * C u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]}
2   C u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   C u0 {1,[S,D,T,B]} {5,[S,D,T,B]}
5   C u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
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
1 * Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {3,S} {5,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {5,S}
5   Cs u0 {2,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.7,-6.66,-5.78,-4.57,-3.31,-3.56,-2.35],'cal/(mol*K)'),
        H298 = (55.38,'kcal/mol'),
        S298 = (64.73,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Properties of Liquids and Gases, Poling 5th Ed. S, Cp from PM7 calculation
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
1 * Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S}
4   Cd u0 {2,S} {5,D}
5   Cd u0 {1,S} {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.56,-5.1,-4.92,-3.97,-3.38,-3.81,-2.92],'cal/(mol*K)'),
        H298 = (67.9,'kcal/mol'),
        S298 = (65.71,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Wiberg, K. Angew. Chem., Int. Ed. Engl. 1986, 25, 312 1986 experimental S, Cp from PM7 calculation
""",
)

entry(
    index = 63,
    label = "s2_3_4_ene_m",
    group = 
"""
1 * C u0 {2,D} {3,S} {5,S}
2   C u0 {1,D} {3,S} {4,S}
3   C u0 {1,S} {2,S}
4   C u0 {2,S} {5,S}
5   C u0 {1,S} {4,S}
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
1 * C u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
2   C u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   C u0 {2,[S,D,T,B]} {6,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
6   C u0 {4,[S,D,T,B]} {5,[S,D,T,B]}
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
1 * Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {2,S} {6,S}
5   Cs u0 {1,S} {6,S}
6   Cs u0 {4,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.27,-8.01,-6.85,-5.27,-3.32,-3.2,-1.6],'cal/(mol*K)'),
        H298 = (32.75,'kcal/mol'),
        S298 = (61.25,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Properties of Liquids and Gases, Poling 5th Ed. S, Cp from PM7 calculation
""",
)

entry(
    index = 0,
    label = "s2_3_5_ene",
    group = "OR{s2_3_5_ene_1}",
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
1 * Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S}
4   Cd u0 {2,S} {6,D}
5   Cs u0 {1,S} {6,S}
6   Cd u0 {4,D} {5,S}
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
Fitted from molecule s2_3_5_ene_1 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 0,
    label = "s2_3_6",
    group = 
"""
1   C u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
2   C u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   C u0 {2,[S,D,T,B]} {6,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6 * C u0 {4,[S,D,T,B]} {7,[S,D,T,B]}
7   C u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
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
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {2,S} {6,S}
5   Cs u0 {1,S} {7,S}
6 * Cs u0 {4,S} {7,S}
7   Cs u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.33,-8.86,-7.46,-5.59,-3.08,-2.67,-0.76],'cal/(mol*K)'),
        H298 = (28.95,'kcal/mol'),
        S298 = (57.69,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Properties of Liquids and Gases, Poling 5th Ed. S, Cp from PM7 calculation
""",
)

entry(
    index = 0,
    label = "s2_3_6_ene",
    group = "OR{s2_3_6_ene_1, s2_3_6_ene_2}",
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
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {3,S} {5,S}
3   Cs u0 {1,S} {2,S}
4   Cd u0 {1,S} {6,D}
5   Cs u0 {2,S} {7,S}
6 * Cd u0 {4,D} {7,S}
7   Cs u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.33,-8.86,-7.46,-5.59,-3.08,-2.67,-0.76],'cal/(mol*K)'),
        H298 = (28.95,'kcal/mol'),
        S298 = (57.69,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Copied from entry: bicyclo-(4.1.0)-heptane
""",
)

entry(
    index = 68,
    label = "s2_3_6_ene_2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {3,S} {5,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {7,S}
5   Cs u0 {2,S} {6,S}
6 * Cd u0 {5,S} {7,D}
7   Cd u0 {4,S} {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-28.3318,-27.6573,-25.8654,-24.1171,-20.2121,-15.7602,-11.2882],'J/(mol*K)'),
        H298 = (246.084,'kJ/mol'),
        S298 = (222.479,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_3_6_ene_2 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 0,
    label = "s2_3_6_diene",
    group = "OR{s2_3_6_diene_1_3}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 69,
    label = "s2_3_6_diene_1_3",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S}
4   Cd u0 {2,S} {6,D}
5   Cd u0 {1,S} {7,D}
6 * Cd u0 {4,D} {7,S}
7   Cd u0 {5,D} {6,S}
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
Fitted from molecule s2_3_6_diene_1_3 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 0,
    label = "s2_3_7",
    group = 
"""
1 * C u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
2   C u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   C u0 {2,[S,D,T,B]} {6,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   C u0 {4,[S,D,T,B]} {8,[S,D,T,B]}
7   C u0 {5,[S,D,T,B]} {8,[S,D,T,B]}
8   C u0 {6,[S,D,T,B]} {7,[S,D,T,B]}
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
1 * Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {2,S} {6,S}
5   Cs u0 {1,S} {7,S}
6   Cs u0 {4,S} {8,S}
7   Cs u0 {5,S} {8,S}
8   Cs u0 {6,S} {7,S}
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
1 * C u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
2   C u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   C u0 {2,[S,D,T,B]} {6,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   C u0 {4,[S,D,T,B]} {8,[S,D,T,B]}
7   C u0 {5,[S,D,T,B]} {9,[S,D,T,B]}
8   C u0 {6,[S,D,T,B]} {9,[S,D,T,B]}
9   C u0 {7,[S,D,T,B]} {8,[S,D,T,B]}
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
1 * Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {2,S} {6,S}
5   Cs u0 {1,S} {7,S}
6   Cs u0 {4,S} {8,S}
7   Cs u0 {5,S} {9,S}
8   Cs u0 {6,S} {9,S}
9   Cs u0 {7,S} {8,S}
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
1   C u0 {2,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2   C u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {6,[S,D,T,B]}
3 * C u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
4   C u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
6   C u0 {2,[S,D,T,B]} {5,[S,D,T,B]}
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
1   Cs u0 {2,S} {4,S} {5,S}
2   Cs u0 {1,S} {3,S} {6,S}
3 * Cs u0 {2,S} {4,S}
4   Cs u0 {1,S} {3,S}
5   Cs u0 {1,S} {6,S}
6   Cs u0 {2,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.54,-8.07,-6.7,-4.98,-3.04,-3.1,-1.48],'cal/(mol*K)'),
        H298 = (51.8,'kcal/mol'),
        S298 = (59.94,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Wiberg, K. Angew. Chem., Int. Ed. Engl. 1986, 25, 312 1986 experimental S, Cp from PM7 calculation
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
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {4,S} {6,S}
3 * Cs u0 {1,S} {4,S}
4   Cs u0 {2,S} {3,S}
5   Cd u0 {1,S} {6,D}
6   Cd u0 {2,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.35,-6.47,-5.81,-4.36,-3.1,-3.34,-2.05],'cal/(mol*K)'),
        H298 = (55.7,'kcal/mol'),
        S298 = (60.79,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Wiberg, K. Angew. Chem., Int. Ed. Engl. 1986, 25, 312 1986 experimental S, Cp from PM7 calculation
""",
)

entry(
    index = 74,
    label = "s2_4_4_ene_m",
    group = 
"""
1   C  u0 {2,D} {4,S} {6,S}
2   C  u0 {1,D} {3,S} {5,S}
3 * Cs u0 {2,S} {4,S}
4   Cs u0 {1,S} {3,S}
5   Cs u0 {2,S} {6,S}
6   Cs u0 {1,S} {5,S}
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
1 * C u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
2   C u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {4,[S,D,T,B]}
4   C u0 {2,[S,D,T,B]} {3,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   C u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
7   C u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
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
1 * Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {4,S} {6,S}
3   Cs u0 {1,S} {4,S}
4   Cs u0 {2,S} {3,S}
5   Cs u0 {1,S} {7,S}
6   Cs u0 {2,S} {7,S}
7   Cs u0 {5,S} {6,S}
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
Fitted from molecule s2_4_5_ane from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 0,
    label = "s2_4_5_ene",
    group = "OR{s2_4_5_ene_1}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 76,
    label = "s2_4_5_ene_1",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S}
3   Cs u0 {1,S} {4,S}
4   Cs u0 {2,S} {3,S}
5   Cs u0 {2,S} {7,S}
6   Cd u0 {1,S} {7,D}
7   Cd u0 {5,S} {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-30.3838,-30.0633,-28.0708,-25.0151,-20.5371,-15.7652,-11.1222],'J/(mol*K)'),
        H298 = (145.91,'kJ/mol'),
        S298 = (229.455,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_4_5_ene_1 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 0,
    label = "s2_4_6",
    group = 
"""
1   C u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {6,[S,D,T,B]}
2   C u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {4,[S,D,T,B]}
4   C u0 {2,[S,D,T,B]} {3,[S,D,T,B]}
5   C u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
6   C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
7 * C u0 {6,[S,D,T,B]} {8,[S,D,T,B]}
8   C u0 {5,[S,D,T,B]} {7,[S,D,T,B]}
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
1   Cs u0 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S}
3   Cs u0 {1,S} {4,S}
4   Cs u0 {2,S} {3,S}
5   Cs u0 {2,S} {8,S}
6   Cs u0 {1,S} {7,S}
7 * Cs u0 {6,S} {8,S}
8   Cs u0 {5,S} {7,S}
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
Fitted from molecule s2_4_6_ane from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 0,
    label = "s2_4_6_ene",
    group = "OR{s2_4_6_ene_1, s2_4_6_ene_2}",
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
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {4,S} {6,S}
3   Cs u0 {1,S} {4,S}
4   Cs u0 {2,S} {3,S}
5   Cs u0 {1,S} {7,S}
6   Cd u0 {2,S} {8,D}
7 * Cs u0 {5,S} {8,S}
8   Cd u0 {6,D} {7,S}
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
Fitted from molecule s2_4_6_ene_1 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 79,
    label = "s2_4_6_ene_2",
    group = 
"""
1   Cs u0 {2,S} {4,S} {6,S}
2   Cs u0 {1,S} {3,S} {5,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {1,S} {3,S}
5   Cs u0 {2,S} {7,S}
6   Cs u0 {1,S} {8,S}
7 * Cd u0 {5,S} {8,D}
8   Cd u0 {6,S} {7,D}
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
Fitted from molecule s2_4_6_ene_2 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 0,
    label = "s2_4_6_diene",
    group = "OR{s2_4_6_diene_1_3, s2_4_6_diene_1_6, s2_4_6_diene_2_6}",
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
1   Cs u0 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S}
3   Cs u0 {1,S} {4,S}
4   Cs u0 {2,S} {3,S}
5   Cd u0 {2,S} {8,D}
6   Cd u0 {1,S} {7,D}
7 * Cd u0 {6,D} {8,S}
8   Cd u0 {5,D} {7,S}
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
Fitted from molecule s2_4_6_diene_1_3 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 181,
    label = "s2_4_6_diene_1_6",
    group = 
"""
1   Cs u0 {2,S} {4,S} {6,S}
2   Cs u0 {1,S} {3,S} {5,S}
3   Cd u0 {2,S} {4,D}
4   Cd u0 {1,S} {3,D}
5   Cs u0 {2,S} {8,S}
6   Cd u0 {1,S} {7,D}
7 * Cd u0 {6,D} {8,S}
8   Cs u0 {5,S} {7,S}
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
Fitted from molecule s2_4_6_diene_1_6 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 182,
    label = "s2_4_6_diene_2_6",
    group = 
"""
1   Cs u0 {2,S} {4,S} {5,S}
2   Cs u0 {1,S} {3,S} {6,S}
3   Cd u0 {2,S} {4,D}
4   Cd u0 {1,S} {3,D}
5   Cs u0 {1,S} {7,S}
6   Cs u0 {2,S} {8,S}
7 * Cd u0 {5,S} {8,D}
8   Cd u0 {6,S} {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-26.6518,-26.7244,-25.953,-23.3602,-19.2686,-14.3808,-9.61984],'J/(mol*K)'),
        H298 = (214.322,'kJ/mol'),
        S298 = (210.792,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_4_6_diene_2_6 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 183,
    label = "s2_4_6_ben",
    group = 
"""
1   Cb u0 {2,B} {4,S} {5,B}
2   Cb u0 {1,B} {3,S} {6,B}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {1,S} {3,S}
5   Cb u0 {1,B} {7,B}
6   Cb u0 {2,B} {8,B}
7 * Cb u0 {5,B} {8,B}
8   Cb u0 {6,B} {7,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-13.1643,-12.9828,-12.2894,-11.5987,-9.35604,-6.5714,-1.5946],'J/(mol*K)'),
        H298 = (148.973,'kJ/mol'),
        S298 = (117.967,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_4_6_ben from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 0,
    label = "s2_5_5",
    group = 
"""
1   C u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
2   C u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
3 * C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
4   C u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
6   C u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
7   C u0 {3,[S,D,T,B]} {4,[S,D,T,B]}
8   C u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
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
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {4,S} {6,S}
3 * Cs u0 {1,S} {7,S}
4   Cs u0 {2,S} {7,S}
5   Cs u0 {1,S} {8,S}
6   Cs u0 {2,S} {8,S}
7   Cs u0 {3,S} {4,S}
8   Cs u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-11.52,-10.59,-8.62,-6.18,-2.88,-2.26,0.09],'cal/(mol*K)'),
        H298 = (10.3,'kcal/mol'),
        S298 = (54.09,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Automated Estimation of Ring Strain Energies, Gasteiger, 1978, S, Cp from PM7
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
1   Cs u0 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {5,D} {6,S}
3 * Cs u0 {1,S} {8,S}
4   Cs u0 {1,S} {7,S}
5   Cd u0 {2,D} {7,S}
6   Cs u0 {2,S} {8,S}
7   Cs u0 {4,S} {5,S}
8   Cs u0 {3,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.85,-8.16,-7.22,-6.08,-4.66,-3.57,-1.84],'cal/(mol*K)'),
        H298 = (13.8,'kcal/mol'),
        S298 = (50.57,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
A.G. Vandeputte isodesmic reactions + B3LYP/cbsb7 S and cp
""",
)

entry(
    index = 82,
    label = "s2_5_5_ene_1",
    group = 
"""
1   Cs u0 {2,S} {4,S} {5,S}
2   Cs u0 {1,S} {3,S} {6,S}
3 * Cd u0 {2,S} {7,D}
4   Cs u0 {1,S} {8,S}
5   Cs u0 {1,S} {7,S}
6   Cs u0 {2,S} {8,S}
7   Cd u0 {3,D} {5,S}
8   Cs u0 {4,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.84,-8,-7.03,-5.94,-4.62,-3.53,-1.94],'cal/(mol*K)'),
        H298 = (9.76,'kcal/mol'),
        S298 = (51.17,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
A.G. Vandeputte isodesmic reactions + B3LYP/cbsb7 S and cp
""",
)

entry(
    index = 83,
    label = "s2_5_5_ene_m",
    group = 
"""
1   Cd u0 {2,D} {3,S} {5,S}
2   Cd u0 {1,D} {4,S} {6,S}
3 * Cs u0 {1,S} {8,S}
4   Cs u0 {2,S} {7,S}
5   Cs u0 {1,S} {7,S}
6   Cs u0 {2,S} {8,S}
7   Cs u0 {4,S} {5,S}
8   Cs u0 {3,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-36.0191,-36.796,-35.0088,-31.1401,-23.1831,-16.6038,-8.33044],'J/(mol*K)'),
        H298 = (86.2088,'kJ/mol'),
        S298 = (204.403,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_5_ene_m from polycyclic_all_thermoLiabrary library.
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
1   Cs u0 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {5,S} {6,D}
3 * Cs u0 {1,S} {8,S}
4   Cd u0 {1,S} {7,D}
5   Cs u0 {2,S} {8,S}
6   Cd u0 {2,D} {7,S}
7   Cd u0 {4,D} {6,S}
8   Cs u0 {3,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-40.8587,-39.2957,-35.8144,-31.5597,-23.4596,-17.2834,-10.8314],'J/(mol*K)'),
        H298 = (98.2803,'kJ/mol'),
        S298 = (234.449,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_5_diene_0_2 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 85,
    label = "s2_5_5_diene_0_3",
    group = 
"""
1   Cd u0 {2,S} {4,D} {5,S}
2   Cd u0 {1,S} {3,D} {6,S}
3 * Cd u0 {2,D} {7,S}
4   Cd u0 {1,D} {7,S}
5   Cs u0 {1,S} {8,S}
6   Cs u0 {2,S} {8,S}
7   Cs u0 {3,S} {4,S}
8   Cs u0 {5,S} {6,S}
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
Fitted from molecule s2_5_5_diene_0_3 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 86,
    label = "s2_5_5_diene_m_2",
    group = 
"""
1   Cd u0 {2,D} {3,S} {5,S}
2   Cd u0 {1,D} {4,S} {6,S}
3 * Cs u0 {1,S} {7,S}
4   Cd u0 {2,S} {8,D}
5   Cs u0 {1,S} {8,S}
6   Cs u0 {2,S} {7,S}
7   Cs u0 {3,S} {6,S}
8   Cd u0 {4,D} {5,S}
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
Fitted from molecule s2_5_5_diene_m_2 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 87,
    label = "s2_5_5_diene_0_4",
    group = 
"""
1   Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D} {6,S}
3 * Cd u0 {1,D} {7,S}
4   Cs u0 {1,S} {8,S}
5   Cd u0 {2,D} {8,S}
6   Cs u0 {2,S} {7,S}
7   Cs u0 {3,S} {6,S}
8   Cs u0 {4,S} {5,S}
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
Fitted from molecule s2_5_5_diene_0_4 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 88,
    label = "s2_5_5_diene_0_5",
    group = 
"""
1   Cs u0 {2,S} {3,S} {6,S}
2   Cd u0 {1,S} {4,D} {5,S}
3 * Cd u0 {1,S} {7,D}
4   Cd u0 {2,D} {8,S}
5   Cs u0 {2,S} {7,S}
6   Cs u0 {1,S} {8,S}
7   Cd u0 {3,D} {5,S}
8   Cs u0 {4,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.57,-7.46,-6.33,-5.3,-4.01,-3.25,-1.79],'cal/(mol*K)'),
        H298 = (14.2,'kcal/mol'),
        S298 = (51.64,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
A. G. Vandeputte CBS-QB3 isodesmic reaction, C12CCC=C1CC=C2 + 3 ethane -> cyclopentene + isobutane + 2-methyl-2-butene, experimental data from the NIST Chemical Webbook
""",
)

entry(
    index = 89,
    label = "s2_5_5_diene_0_6",
    group = 
"""
1   Cs u0 {2,S} {4,S} {6,S}
2   Cd u0 {1,S} {3,S} {5,D}
3 * Cd u0 {2,S} {7,D}
4   Cs u0 {1,S} {8,S}
5   Cd u0 {2,D} {8,S}
6   Cs u0 {1,S} {7,S}
7   Cd u0 {3,D} {6,S}
8   Cs u0 {4,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.57,-7.46,-6.33,-5.3,-4.01,-3.25,-1.79],'cal/(mol*K)'),
        H298 = (14.2,'kcal/mol'),
        S298 = (51.64,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Copied from entry: C12CCC=C1CC=C2
""",
)

entry(
    index = 90,
    label = "s2_5_5_diene_1_5",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {4,S} {6,S}
3 * Cd u0 {1,S} {7,D}
4   Cd u0 {2,S} {8,D}
5   Cs u0 {1,S} {8,S}
6   Cs u0 {2,S} {7,S}
7   Cd u0 {3,D} {6,S}
8   Cd u0 {4,D} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.57,-7.46,-6.33,-5.3,-4.01,-3.25,-1.79],'cal/(mol*K)'),
        H298 = (10,'kcal/mol'),
        S298 = (51.64,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
ring strain N. Vandewiele, S and cp taken from C12CCC=C1CC=C2
""",
)

entry(
    index = 91,
    label = "s2_5_5_diene_1_6",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {5,S} {6,S}
3 * Cd u0 {1,S} {7,D}
4   Cd u0 {1,S} {8,D}
5   Cs u0 {2,S} {7,S}
6   Cs u0 {2,S} {8,S}
7   Cd u0 {3,D} {5,S}
8   Cd u0 {4,D} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.57,-7.46,-6.33,-5.3,-4.01,-3.25,-1.79],'cal/(mol*K)'),
        H298 = (14.2,'kcal/mol'),
        S298 = (51.64,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Copied from entry: C12CCC=C1CC=C2
""",
)

entry(
    index = 0,
    label = "s2_5_6",
    group = 
"""
1 * C u0 {2,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2   C u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {6,[S,D,T,B]}
3   C u0 {2,[S,D,T,B]} {9,[S,D,T,B]}
4   C u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   C u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
7   C u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
8   C u0 {4,[S,D,T,B]} {9,[S,D,T,B]}
9   C u0 {3,[S,D,T,B]} {8,[S,D,T,B]}
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
1 * Cs u0 {2,S} {4,S} {5,S}
2   Cs u0 {1,S} {3,S} {6,S}
3   Cs u0 {2,S} {9,S}
4   Cs u0 {1,S} {8,S}
5   Cs u0 {1,S} {7,S}
6   Cs u0 {2,S} {7,S}
7   Cs u0 {5,S} {6,S}
8   Cs u0 {4,S} {9,S}
9   Cs u0 {3,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-11.91,-10.762,-9.241,-7.769,-5.56,-3.888,-1.388],'cal/(mol*K)'),
        H298 = (8.21,'kcal/mol'),
        S298 = (47.72,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
ring strain N. Vandewiele, S and cp modified by A. G. Vandeputte to match BMK/6-311G(2d,d,p) data
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
1 * Cs u0 {2,S} {3,S} {5,S}
2   Cd u0 {1,S} {4,D} {6,S}
3   Cs u0 {1,S} {7,S}
4   Cd u0 {2,D} {8,S}
5   Cs u0 {1,S} {9,S}
6   Cs u0 {2,S} {7,S}
7   Cs u0 {3,S} {6,S}
8   Cs u0 {4,S} {9,S}
9   Cs u0 {5,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.8,-9,-7.9,-6.5,-4.7,-3.4,-1.3],'cal/(mol*K)'),
        H298 = (9,'kcal/mol'),
        S298 = (47.04,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
A. G. Vandeputte CBS-QB3 isodesmic reaction, S and cp match B3LYP/cbsb7 data
""",
)

entry(
    index = 94,
    label = "s2_5_6_ene_1",
    group = 
"""
1 * Cs u0 {2,S} {4,S} {6,S}
2   Cs u0 {1,S} {3,S} {5,S}
3   Cd u0 {2,S} {8,D}
4   Cs u0 {1,S} {7,S}
5   Cs u0 {2,S} {7,S}
6   Cs u0 {1,S} {9,S}
7   Cs u0 {4,S} {5,S}
8   Cd u0 {3,D} {9,S}
9   Cs u0 {6,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8,-7.6,-6.8,-5.7,-4.3,-3.3,-2.1],'cal/(mol*K)'),
        H298 = (9,'kcal/mol'),
        S298 = (45.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Copied from entry: 2.4.5.6.7.7a-hexahydro-1H-indene
""",
)

entry(
    index = 95,
    label = "s2_5_6_ene_m",
    group = 
"""
1 * Cd u0 {2,D} {5,S} {6,S}
2   Cd u0 {1,D} {3,S} {4,S}
3   Cs u0 {2,S} {8,S}
4   Cs u0 {2,S} {7,S}
5   Cs u0 {1,S} {7,S}
6   Cs u0 {1,S} {9,S}
7   Cs u0 {4,S} {5,S}
8   Cs u0 {3,S} {9,S}
9   Cs u0 {6,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8,-7.6,-6.8,-5.7,-4.3,-3.3,-2.1],'cal/(mol*K)'),
        H298 = (9,'kcal/mol'),
        S298 = (45.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Copied from entry: 2.4.5.6.7.7a-hexahydro-1H-indene
""",
)

entry(
    index = 96,
    label = "s2_5_6_ene_2",
    group = 
"""
1 * Cs u0 {2,S} {5,S} {6,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   Cs u0 {2,S} {7,S}
4   Cs u0 {2,S} {8,S}
5   Cs u0 {1,S} {7,S}
6   Cs u0 {1,S} {9,S}
7   Cs u0 {3,S} {5,S}
8   Cd u0 {4,S} {9,D}
9   Cd u0 {6,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8,-7.6,-6.8,-5.7,-4.3,-3.3,-2.1],'cal/(mol*K)'),
        H298 = (9,'kcal/mol'),
        S298 = (45.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Copied from entry: 2.4.5.6.7.7a-hexahydro-1H-indene
""",
)

entry(
    index = 97,
    label = "s2_5_6_ene_5",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {6,S}
2   Cs u0 {1,S} {4,S} {5,S}
3   Cd u0 {1,D} {7,S}
4   Cs u0 {2,S} {9,S}
5   Cs u0 {2,S} {7,S}
6   Cs u0 {1,S} {8,S}
7   Cs u0 {3,S} {5,S}
8   Cs u0 {6,S} {9,S}
9   Cs u0 {4,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8,-7.6,-6.8,-5.7,-4.3,-3.3,-2.1],'cal/(mol*K)'),
        H298 = (9,'kcal/mol'),
        S298 = (45.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
ring strain 2.3.3a.4.5.6-hexahydro-1H-indene, S and cp modified by A. G. Vandeputte to match BMK/6-311G(2d,p) data
""",
)

entry(
    index = 98,
    label = "s2_5_6_ene_6",
    group = 
"""
1 * Cs u0 {2,S} {4,S} {6,S}
2   Cs u0 {1,S} {3,S} {5,S}
3   Cs u0 {2,S} {8,S}
4   Cs u0 {1,S} {7,S}
5   Cd u0 {2,S} {7,D}
6   Cs u0 {1,S} {9,S}
7   Cd u0 {4,S} {5,D}
8   Cs u0 {3,S} {9,S}
9   Cs u0 {6,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8,-7.6,-6.8,-5.7,-4.3,-3.3,-2.1],'cal/(mol*K)'),
        H298 = (9,'kcal/mol'),
        S298 = (45.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Copied from entry: 2.4.5.6.7.7a-hexahydro-1H-indene
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
1 * Cd u0 {2,D} {4,S} {6,S}
2   Cd u0 {1,D} {3,S} {5,S}
3   Cd u0 {2,S} {8,D}
4   Cs u0 {1,S} {7,S}
5   Cs u0 {2,S} {7,S}
6   Cs u0 {1,S} {9,S}
7   Cs u0 {4,S} {5,S}
8   Cd u0 {3,D} {9,S}
9   Cs u0 {6,S} {8,S}
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
    index = 100,
    label = "s2_5_6_diene_m_2",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {6,S}
2   Cd u0 {1,D} {4,S} {5,S}
3   Cs u0 {1,S} {9,S}
4   Cs u0 {2,S} {8,S}
5   Cs u0 {2,S} {7,S}
6   Cs u0 {1,S} {7,S}
7   Cs u0 {5,S} {6,S}
8   Cd u0 {4,S} {9,D}
9   Cd u0 {3,S} {8,D}
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
    index = 101,
    label = "s2_5_6_diene_m_7",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {5,S}
2   Cd u0 {1,D} {4,S} {6,S}
3   Cs u0 {1,S} {8,S}
4   Cs u0 {2,S} {7,S}
5   Cd u0 {1,S} {7,D}
6   Cs u0 {2,S} {9,S}
7   Cd u0 {4,S} {5,D}
8   Cs u0 {3,S} {9,S}
9   Cs u0 {6,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-38.63,-40.3085,-38.2637,-33.8928,-24.6281,-17.3259,-8.3302],'J/(mol*K)'),
        H298 = (51.5473,'kJ/mol'),
        S298 = (204.962,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_6_diene_m_7 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 102,
    label = "s2_5_6_diene_0_2",
    group = 
"""
1 * Cd u0 {2,S} {4,S} {6,D}
2   Cs u0 {1,S} {3,S} {5,S}
3   Cs u0 {2,S} {7,S}
4   Cs u0 {1,S} {7,S}
5   Cs u0 {2,S} {9,S}
6   Cd u0 {1,D} {8,S}
7   Cs u0 {3,S} {4,S}
8   Cd u0 {6,S} {9,D}
9   Cd u0 {5,S} {8,D}
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
    index = 103,
    label = "s2_5_6_diene_0_3",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {6,S}
2   Cd u0 {1,S} {4,D} {5,S}
3   Cd u0 {1,S} {8,D}
4   Cd u0 {2,D} {9,S}
5   Cs u0 {2,S} {7,S}
6   Cs u0 {1,S} {7,S}
7   Cs u0 {5,S} {6,S}
8   Cd u0 {3,D} {9,S}
9   Cs u0 {4,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8,-7.6,-6.8,-5.7,-4.3,-3.3,-2.1],'cal/(mol*K)'),
        H298 = (6.8,'kcal/mol'),
        S298 = (45.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
ring strain N. Vandewiele, S and cp taken from 2.4.5.6.7.7a-hexahydro-1H-indene
""",
)

entry(
    index = 104,
    label = "s2_5_6_diene_0_4",
    group = 
"""
1 * Cd u0 {2,S} {4,D} {5,S}
2   Cd u0 {1,S} {3,D} {6,S}
3   Cd u0 {2,D} {9,S}
4   Cd u0 {1,D} {8,S}
5   Cs u0 {1,S} {7,S}
6   Cs u0 {2,S} {7,S}
7   Cs u0 {5,S} {6,S}
8   Cs u0 {4,S} {9,S}
9   Cs u0 {3,S} {8,S}
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
    index = 105,
    label = "s2_5_6_diene_0_5",
    group = 
"""
1 * Cd u0 {2,S} {4,S} {5,D}
2   Cd u0 {1,S} {3,D} {6,S}
3   Cd u0 {2,D} {8,S}
4   Cs u0 {1,S} {9,S}
5   Cd u0 {1,D} {7,S}
6   Cs u0 {2,S} {7,S}
7   Cs u0 {5,S} {6,S}
8   Cs u0 {3,S} {9,S}
9   Cs u0 {4,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-38.7904,-40.955,-39.4838,-35.1913,-25.819,-18.1126,-9.06408],'J/(mol*K)'),
        H298 = (53.2024,'kJ/mol'),
        S298 = (211.109,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_6_diene_0_5 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 106,
    label = "s2_5_6_diene_0_6",
    group = 
"""
1 * Cs u0 {2,S} {4,S} {6,S}
2   Cd u0 {1,S} {3,D} {5,S}
3   Cd u0 {2,D} {9,S}
4   Cs u0 {1,S} {8,S}
5   Cs u0 {2,S} {7,S}
6   Cd u0 {1,S} {7,D}
7   Cd u0 {5,S} {6,D}
8   Cs u0 {4,S} {9,S}
9   Cs u0 {3,S} {8,S}
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
Fitted from molecule s2_5_6_diene_0_6 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 107,
    label = "s2_5_6_diene_0_7",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {6,S}
2   Cd u0 {1,S} {4,S} {5,D}
3   Cs u0 {1,S} {7,S}
4   Cd u0 {2,S} {7,D}
5   Cd u0 {2,D} {8,S}
6   Cs u0 {1,S} {9,S}
7   Cd u0 {3,S} {4,D}
8   Cs u0 {5,S} {9,S}
9   Cs u0 {6,S} {8,S}
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
Fitted from molecule s2_5_6_diene_0_7 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 108,
    label = "s2_5_6_diene_1_3",
    group = 
"""
1 * Cs u0 {2,S} {5,S} {6,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   Cd u0 {2,S} {9,D}
4   Cs u0 {2,S} {7,S}
5   Cd u0 {1,S} {8,D}
6   Cs u0 {1,S} {7,S}
7   Cs u0 {4,S} {6,S}
8   Cd u0 {5,D} {9,S}
9   Cd u0 {3,D} {8,S}
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
ring strain N. Vandewiele, S and cp taken from 2.4.5.6.7.7a-hexahydro-1H-indene
""",
)

entry(
    index = 109,
    label = "s2_5_6_diene_1_5",
    group = 
"""
1 * Cs u0 {2,S} {4,S} {5,S}
2   Cd u0 {1,S} {3,D} {6,S}
3   Cd u0 {2,D} {7,S}
4   Cd u0 {1,S} {9,D}
5   Cs u0 {1,S} {7,S}
6   Cs u0 {2,S} {8,S}
7   Cs u0 {3,S} {5,S}
8   Cs u0 {6,S} {9,S}
9   Cd u0 {4,D} {8,S}
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
Fitted from molecule s2_5_6_diene_1_5 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 110,
    label = "s2_5_6_diene_1_6",
    group = 
"""
1 * Cs u0 {2,S} {4,S} {6,S}
2   Cs u0 {1,S} {3,S} {5,S}
3   Cs u0 {2,S} {7,S}
4   Cd u0 {1,S} {7,D}
5   Cd u0 {2,S} {8,D}
6   Cs u0 {1,S} {9,S}
7   Cd u0 {3,S} {4,D}
8   Cd u0 {5,D} {9,S}
9   Cs u0 {6,S} {8,S}
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
Fitted from molecule s2_5_6_diene_1_6 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 111,
    label = "s2_5_6_diene_1_7",
    group = 
"""
1 * Cs u0 {2,S} {4,S} {5,S}
2   Cs u0 {1,S} {3,S} {6,S}
3   Cs u0 {2,S} {8,S}
4   Cd u0 {1,S} {9,D}
5   Cd u0 {1,S} {7,D}
6   Cs u0 {2,S} {7,S}
7   Cd u0 {5,D} {6,S}
8   Cs u0 {3,S} {9,S}
9   Cd u0 {4,D} {8,S}
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
Fitted from molecule s2_5_6_diene_1_7 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 112,
    label = "s2_5_6_diene_1_8",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {6,S}
2   Cd u0 {1,S} {4,D} {5,S}
3   Cs u0 {1,S} {7,S}
4   Cd u0 {2,D} {7,S}
5   Cd u0 {2,S} {8,D}
6   Cs u0 {1,S} {9,S}
7   Cs u0 {3,S} {4,S}
8   Cd u0 {5,D} {9,S}
9   Cs u0 {6,S} {8,S}
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
1 * Cs u0 {2,S} {5,S} {6,S}
2   Cd u0 {1,S} {3,S} {4,D}
3   Cs u0 {2,S} {9,S}
4   Cd u0 {2,D} {7,S}
5   Cs u0 {1,S} {8,S}
6   Cs u0 {1,S} {7,S}
7   Cs u0 {4,S} {6,S}
8   Cd u0 {5,S} {9,D}
9   Cd u0 {3,S} {8,D}
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
Fitted from molecule s2_5_6_diene_2_5 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 114,
    label = "s2_5_6_diene_2_6",
    group = 
"""
1 * Cs u0 {2,S} {4,S} {5,S}
2   Cs u0 {1,S} {3,S} {6,S}
3   Cs u0 {2,S} {8,S}
4   Cs u0 {1,S} {7,S}
5   Cs u0 {1,S} {9,S}
6   Cd u0 {2,S} {7,D}
7   Cd u0 {4,S} {6,D}
8   Cd u0 {3,S} {9,D}
9   Cd u0 {5,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-31.8178,-31.2752,-29.2986,-26.0706,-19.9045,-13.5633,-7.10184],'J/(mol*K)'),
        H298 = (65.0092,'kJ/mol'),
        S298 = (191.089,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_6_diene_2_6 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 115,
    label = "s2_5_6_diene_5_7",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {5,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cs u0 {1,S} {9,S}
5   Cs u0 {2,S} {8,S}
6   Cd u0 {2,D} {7,S}
7   Cd u0 {3,D} {6,S}
8   Cs u0 {5,S} {9,S}
9   Cs u0 {4,S} {8,S}
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
Fitted from molecule s2_5_6_diene_5_7 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 116,
    label = "s2_5_6_diene_5_8",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {5,S}
2   Cd u0 {1,S} {4,D} {6,S}
3   Cd u0 {1,D} {7,S}
4   Cd u0 {2,D} {7,S}
5   Cs u0 {1,S} {9,S}
6   Cs u0 {2,S} {8,S}
7   Cs u0 {3,S} {4,S}
8   Cs u0 {6,S} {9,S}
9   Cs u0 {5,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-38.594,-40.0215,-37.8257,-33.4848,-24.3501,-17.1569,-8.3362],'J/(mol*K)'),
        H298 = (56.0623,'kJ/mol'),
        S298 = (201.108,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_5_6_diene_5_8 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 184,
    label = "s2_5_6_ben",
    group = 
"""
1 * Cb u0 {2,B} {3,S} {5,B}
2   Cb u0 {1,B} {4,S} {6,B}
3   Cs u0 {1,S} {7,S}
4   Cs u0 {2,S} {7,S}
5   Cb u0 {1,B} {9,B}
6   Cb u0 {2,B} {8,B}
7   Cs u0 {3,S} {4,S}
8   Cb u0 {6,B} {9,B}
9   Cb u0 {5,B} {8,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.23,-5.21,-4.3,-2.86,-0.88,-0.71,1.4],'cal/(mol*K)'),
        H298 = (5.54,'kcal/mol'),
        S298 = (25.35,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Verevkin (2011), experimental, S and cp from PM7
""",
)

entry(
    index = 117,
    label = "s2_5_6_indene",
    group = 
"""
1 * C  u0 {2,B} {3,S} {4,B}
2   C  u0 {1,B} {5,S} {6,B}
3   Cs u0 {1,S} {7,S}
4   C  u0 {1,B} {8,B}
5   C  u0 {2,S} {7,D}
6   C  u0 {2,B} {9,B}
7   C  u0 {3,S} {5,D}
8   C  u0 {4,B} {9,B}
9   C  u0 {6,B} {8,B}
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
    label = "s2_6_6",
    group = 
"""
1    C u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {6,[S,D,T,B]}
2    C u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3    C u0 {1,[S,D,T,B]} {9,[S,D,T,B]}
4    C u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
5    C u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
6    C u0 {1,[S,D,T,B]} {10,[S,D,T,B]}
7  * C u0 {4,[S,D,T,B]} {9,[S,D,T,B]}
8    C u0 {5,[S,D,T,B]} {10,[S,D,T,B]}
9    C u0 {3,[S,D,T,B]} {7,[S,D,T,B]}
10   C u0 {6,[S,D,T,B]} {8,[S,D,T,B]}
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
1    Cs u0 {2,S} {3,S} {6,S}
2    Cs u0 {1,S} {4,S} {5,S}
3    Cs u0 {1,S} {9,S}
4    Cs u0 {2,S} {7,S}
5    Cs u0 {2,S} {8,S}
6    Cs u0 {1,S} {10,S}
7  * Cs u0 {4,S} {9,S}
8    Cs u0 {5,S} {10,S}
9    Cs u0 {3,S} {7,S}
10   Cs u0 {6,S} {8,S}
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
Fitted from molecule s2_6_6_ane from polycyclic_all_thermoLiabrary library.
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
1    Cs u0 {2,S} {3,S} {5,S}
2    Cd u0 {1,S} {4,D} {6,S}
3    Cs u0 {1,S} {7,S}
4    Cd u0 {2,D} {8,S}
5    Cs u0 {1,S} {10,S}
6    Cs u0 {2,S} {9,S}
7  * Cs u0 {3,S} {8,S}
8    Cs u0 {4,S} {7,S}
9    Cs u0 {6,S} {10,S}
10   Cs u0 {5,S} {9,S}
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
Fitted from molecule s2_6_6_ene_0 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 120,
    label = "s2_6_6_ene_1",
    group = 
"""
1    Cs u0 {2,S} {3,S} {5,S}
2    Cs u0 {1,S} {4,S} {6,S}
3    Cd u0 {1,S} {9,D}
4    Cs u0 {2,S} {7,S}
5    Cs u0 {1,S} {10,S}
6    Cs u0 {2,S} {8,S}
7  * Cs u0 {4,S} {10,S}
8    Cs u0 {6,S} {9,S}
9    Cd u0 {3,D} {8,S}
10   Cs u0 {5,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-41.3108,-37.9067,-34.3308,-29.4523,-19.9858,-11.6909,-2.8732],'J/(mol*K)'),
        H298 = (260.592,'kJ/mol'),
        S298 = (166.041,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_6_6_ene_1 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 121,
    label = "s2_6_6_ene_2",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S}
2    Cs u0 {1,S} {5,S} {6,S}
3    Cs u0 {1,S} {10,S}
4    Cs u0 {1,S} {7,S}
5    Cs u0 {2,S} {8,S}
6    Cs u0 {2,S} {9,S}
7  * Cs u0 {4,S} {8,S}
8    Cs u0 {5,S} {7,S}
9    Cd u0 {6,S} {10,D}
10   Cd u0 {3,S} {9,D}
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
Fitted from molecule s2_6_6_ene_2 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 122,
    label = "s2_6_6_ene_m",
    group = 
"""
1    Cd u0 {2,D} {5,S} {6,S}
2    Cd u0 {1,D} {3,S} {4,S}
3    Cs u0 {2,S} {7,S}
4    Cs u0 {2,S} {8,S}
5    Cs u0 {1,S} {10,S}
6    Cs u0 {1,S} {9,S}
7  * Cs u0 {3,S} {9,S}
8    Cs u0 {4,S} {10,S}
9    Cs u0 {6,S} {7,S}
10   Cs u0 {5,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-45.2261,-43.8146,-40.2788,-34.6869,-23.5958,-14.779,-3.51844],'J/(mol*K)'),
        H298 = (34.5594,'kJ/mol'),
        S298 = (154.144,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_6_6_ene_m from polycyclic_all_thermoLiabrary library.
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
1    Cd u0 {2,D} {4,S} {6,S}
2    Cd u0 {1,D} {3,S} {5,S}
3    Cs u0 {2,S} {9,S}
4    Cs u0 {1,S} {8,S}
5    Cd u0 {2,S} {7,D}
6    Cs u0 {1,S} {10,S}
7  * Cd u0 {5,D} {8,S}
8    Cs u0 {4,S} {7,S}
9    Cs u0 {3,S} {10,S}
10   Cs u0 {6,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-42.4824,-44.2048,-42.1578,-36.9087,-25.8979,-17.1012,-6.65508],'J/(mol*K)'),
        H298 = (47.0401,'kJ/mol'),
        S298 = (188.632,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_6_6_diene_m_1 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 124,
    label = "s2_6_6_diene_m_2",
    group = 
"""
1    Cd u0 {2,D} {5,S} {6,S}
2    Cd u0 {1,D} {3,S} {4,S}
3    Cs u0 {2,S} {8,S}
4    Cs u0 {2,S} {10,S}
5    Cs u0 {1,S} {9,S}
6    Cs u0 {1,S} {7,S}
7  * Cs u0 {6,S} {10,S}
8    Cd u0 {3,S} {9,D}
9    Cd u0 {5,S} {8,D}
10   Cs u0 {4,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-36.4704,-37.505,-35.2594,-30.5046,-21.0927,-13.8636,-3.90332],'J/(mol*K)'),
        H298 = (27.5712,'kJ/mol'),
        S298 = (167.901,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_6_6_diene_m_2 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 125,
    label = "s2_6_6_diene_0_2",
    group = 
"""
1    Cs u0 {2,S} {3,S} {5,S}
2    Cd u0 {1,S} {4,S} {6,D}
3    Cs u0 {1,S} {8,S}
4    Cs u0 {2,S} {10,S}
5    Cs u0 {1,S} {9,S}
6    Cd u0 {2,D} {7,S}
7  * Cd u0 {6,S} {8,D}
8    Cd u0 {3,S} {7,D}
9    Cs u0 {5,S} {10,S}
10   Cs u0 {4,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-41.1707,-42.9518,-41.3835,-35.9789,-25.3008,-16.5271,-7.06396],'J/(mol*K)'),
        H298 = (63.4493,'kJ/mol'),
        S298 = (189.537,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_6_6_diene_0_2 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 126,
    label = "s2_6_6_diene_0_3",
    group = 
"""
1    Cd u0 {2,S} {4,S} {6,D}
2    Cs u0 {1,S} {3,S} {5,S}
3    Cs u0 {2,S} {10,S}
4    Cs u0 {1,S} {9,S}
5    Cd u0 {2,S} {7,D}
6    Cd u0 {1,D} {8,S}
7  * Cd u0 {5,D} {8,S}
8    Cs u0 {6,S} {7,S}
9    Cs u0 {4,S} {10,S}
10   Cs u0 {3,S} {9,S}
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
Fitted from molecule s2_6_6_diene_0_3 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 127,
    label = "s2_6_6_diene_0_4",
    group = 
"""
1    Cd u0 {2,S} {3,S} {5,D}
2    Cd u0 {1,S} {4,D} {6,S}
3    Cs u0 {1,S} {10,S}
4    Cd u0 {2,D} {8,S}
5    Cd u0 {1,D} {7,S}
6    Cs u0 {2,S} {9,S}
7  * Cs u0 {5,S} {8,S}
8    Cs u0 {4,S} {7,S}
9    Cs u0 {6,S} {10,S}
10   Cs u0 {3,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-42.7634,-44.3158,-42.0638,-36.6807,-25.5709,-16.8262,-6.67908],'J/(mol*K)'),
        H298 = (53.8256,'kJ/mol'),
        S298 = (181.405,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_6_6_diene_0_4 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 128,
    label = "s2_6_6_diene_0_5",
    group = 
"""
1    Cd u0 {2,S} {3,S} {5,D}
2    Cd u0 {1,S} {4,D} {6,S}
3    Cs u0 {1,S} {9,S}
4    Cd u0 {2,D} {7,S}
5    Cd u0 {1,D} {10,S}
6    Cs u0 {2,S} {8,S}
7  * Cs u0 {4,S} {9,S}
8    Cs u0 {6,S} {10,S}
9    Cs u0 {3,S} {7,S}
10   Cs u0 {5,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-43.7554,-45.3278,-42.9508,-37.4467,-26.1409,-17.2482,-6.89208],'J/(mol*K)'),
        H298 = (34.4058,'kJ/mol'),
        S298 = (180.245,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_6_6_diene_0_5 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 129,
    label = "s2_6_6_diene_0_6",
    group = 
"""
1    Cd u0 {2,S} {5,S} {6,D}
2    Cs u0 {1,S} {3,S} {4,S}
3    Cs u0 {2,S} {10,S}
4    Cd u0 {2,S} {9,D}
5    Cs u0 {1,S} {8,S}
6    Cd u0 {1,D} {7,S}
7  * Cs u0 {6,S} {10,S}
8    Cs u0 {5,S} {9,S}
9    Cd u0 {4,D} {8,S}
10   Cs u0 {3,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-40.4475,-37.0305,-33.0252,-27.7354,-17.703,-10.5603,-3.47136],'J/(mol*K)'),
        H298 = (259.528,'kJ/mol'),
        S298 = (176.442,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_6_6_diene_0_6 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 130,
    label = "s2_6_6_diene_0_7",
    group = 
"""
1    Cd u0 {2,S} {4,S} {6,D}
2    Cs u0 {1,S} {3,S} {5,S}
3    Cs u0 {2,S} {8,S}
4    Cs u0 {1,S} {9,S}
5    Cs u0 {2,S} {10,S}
6    Cd u0 {1,D} {7,S}
7  * Cs u0 {6,S} {10,S}
8    Cd u0 {3,S} {9,D}
9    Cd u0 {4,S} {8,D}
10   Cs u0 {5,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-35.6501,-36.3455,-34.5142,-29.6663,-20.6586,-13.2452,-4.61608],'J/(mol*K)'),
        H298 = (40.2236,'kJ/mol'),
        S298 = (173.573,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s2_6_6_diene_0_7 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 131,
    label = "s2_6_6_diene_0_8",
    group = 
"""
1    Cd u0 {2,S} {4,S} {6,D}
2    Cs u0 {1,S} {3,S} {5,S}
3    Cs u0 {2,S} {9,S}
4    Cd u0 {1,S} {10,D}
5    Cs u0 {2,S} {8,S}
6    Cd u0 {1,D} {7,S}
7  * Cs u0 {6,S} {8,S}
8    Cs u0 {5,S} {7,S}
9    Cs u0 {3,S} {10,S}
10   Cd u0 {4,D} {9,S}
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
Fitted from molecule s2_6_6_diene_0_8 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 132,
    label = "s2_6_6_diene_1_3",
    group = 
"""
1    Cs u0 {2,S} {5,S} {6,S}
2    Cs u0 {1,S} {3,S} {4,S}
3    Cd u0 {2,S} {7,D}
4    Cs u0 {2,S} {8,S}
5    Cs u0 {1,S} {10,S}
6    Cd u0 {1,S} {9,D}
7  * Cd u0 {3,D} {9,S}
8    Cs u0 {4,S} {10,S}
9    Cd u0 {6,D} {7,S}
10   Cs u0 {5,S} {8,S}
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
Fitted from molecule s2_6_6_diene_1_3 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 133,
    label = "s2_6_6_diene_1_6",
    group = 
"""
1    Cs u0 {2,S} {5,S} {6,S}
2    Cs u0 {1,S} {3,S} {4,S}
3    Cs u0 {2,S} {10,S}
4    Cd u0 {2,S} {8,D}
5    Cs u0 {1,S} {9,S}
6    Cd u0 {1,S} {7,D}
7  * Cd u0 {6,D} {10,S}
8    Cd u0 {4,D} {9,S}
9    Cs u0 {5,S} {8,S}
10   Cs u0 {3,S} {7,S}
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
Fitted from molecule s2_6_6_diene_1_6 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 134,
    label = "s2_6_6_diene_1_7",
    group = 
"""
1    Cs u0 {2,S} {4,S} {6,S}
2    Cs u0 {1,S} {3,S} {5,S}
3    Cs u0 {2,S} {10,S}
4    Cs u0 {1,S} {7,S}
5    Cd u0 {2,S} {8,D}
6    Cs u0 {1,S} {9,S}
7  * Cd u0 {4,S} {10,D}
8    Cd u0 {5,D} {9,S}
9    Cs u0 {6,S} {8,S}
10   Cd u0 {3,S} {7,D}
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
Fitted from molecule s2_6_6_diene_1_7 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 135,
    label = "s2_6_6_diene_1_8",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S}
2    Cs u0 {1,S} {3,S} {6,S}
3    Cs u0 {2,S} {7,S}
4    Cd u0 {1,S} {10,D}
5    Cd u0 {1,S} {8,D}
6    Cs u0 {2,S} {9,S}
7  * Cs u0 {3,S} {8,S}
8    Cd u0 {5,D} {7,S}
9    Cs u0 {6,S} {10,S}
10   Cd u0 {4,D} {9,S}
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
Fitted from molecule s2_6_6_diene_1_8 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 136,
    label = "s2_6_6_diene_2_7",
    group = 
"""
1    Cs u0 {2,S} {4,S} {6,S}
2    Cs u0 {1,S} {3,S} {5,S}
3    Cs u0 {2,S} {8,S}
4    Cs u0 {1,S} {9,S}
5    Cs u0 {2,S} {7,S}
6    Cs u0 {1,S} {10,S}
7  * Cd u0 {5,S} {9,D}
8    Cd u0 {3,S} {10,D}
9    Cd u0 {4,S} {7,D}
10   Cd u0 {6,S} {8,D}
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
Fitted from molecule s2_6_6_diene_2_7 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 185,
    label = "s2_6_6_ben",
    group = 
"""
1    Cb u0 {2,B} {3,B} {5,S}
2    Cb u0 {1,B} {4,B} {6,S}
3    Cb u0 {1,B} {7,B}
4    Cb u0 {2,B} {9,B}
5    Cs u0 {1,S} {10,S}
6    Cs u0 {2,S} {8,S}
7  * Cb u0 {3,B} {9,B}
8    Cs u0 {6,S} {10,S}
9    Cb u0 {4,B} {7,B}
10   Cs u0 {5,S} {8,S}
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
Fitted from molecule s2_6_6_ben from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 0,
    label = "s3_4_4",
    group = 
"""
1   C u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2   C u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 * C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
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
1   Cs u0 {3,S} {4,S} {5,S}
2   Cs u0 {3,S} {4,S} {5,S}
3 * Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {2,S}
5   Cs u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.64,-6.32,-5.24,-3.91,-2.78,-3.31,-2.12],'cal/(mol*K)'),
        H298 = (68,'kcal/mol'),
        S298 = (62.36,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Wiberg, K. Angew. Chem., Int. Ed. Engl. 1986, 25, 312 1986 ab initio S, Cp from PM7 calculation
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
1   Cd u0 {3,S} {4,S} {5,D}
2   Cs u0 {3,S} {4,S} {5,S}
3 * Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {2,S}
5   Cd u0 {1,D} {2,S}
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
Fitted from molecule s3_4_4_ene_0 from polycyclic_all_thermoLiabrary library.
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
1   Cd u0 {3,S} {4,S} {5,D}
2   Cd u0 {3,D} {4,S} {5,S}
3 * Cd u0 {1,S} {2,D}
4   Cs u0 {1,S} {2,S}
5   Cd u0 {1,D} {2,S}
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
Fitted from molecule s3_4_4_diene_0_2 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 0,
    label = "s3_4_5",
    group = 
"""
1   C u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
2   C u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 * C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
5   C u0 {2,[S,D,T,B]} {6,[S,D,T,B]}
6   C u0 {1,[S,D,T,B]} {5,[S,D,T,B]}
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
1   Cs u0 {3,S} {4,S} {6,S}
2   Cs u0 {3,S} {4,S} {5,S}
3 * Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {2,S}
5   Cs u0 {2,S} {6,S}
6   Cs u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.92,-8.22,-6.65,-4.79,-2.85,-3.09,-1.39],'cal/(mol*K)'),
        H298 = (37,'kcal/mol'),
        S298 = (57.98,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Wiberg, K. Angew. Chem., Int. Ed. Engl. 1986, 25, 312 1986 ab initio, S, Cp from PM7 calculation
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
1   Cd u0 {3,S} {4,S} {6,D}
2   Cs u0 {3,S} {4,S} {5,S}
3 * Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {2,S}
5   Cs u0 {2,S} {6,S}
6   Cd u0 {1,D} {5,S}
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
Fitted from molecule s3_4_5_ene_0 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 142,
    label = "s3_4_5_ene_1",
    group = 
"""
1   Cs u0 {3,S} {4,S} {5,S}
2   Cs u0 {3,S} {4,S} {6,S}
3 * Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {2,S}
5   Cd u0 {1,S} {6,D}
6   Cd u0 {2,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.86,-6.73,-5.82,-4.2,-2.93,-3.36,-1.97],'cal/(mol*K)'),
        H298 = (51,'kcal/mol'),
        S298 = (58.93,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Wiberg, K. Angew. Chem., Int. Ed. Engl. 1986, 25, 312 1986 ab initio S, Cp from PM7 calculations
""",
)

entry(
    index = 143,
    label = "s3_4_5_ene_3",
    group = 
"""
1   Cd u0 {3,D} {4,S} {6,S}
2   Cs u0 {3,S} {4,S} {5,S}
3 * Cd u0 {1,D} {2,S}
4   Cs u0 {1,S} {2,S}
5   Cs u0 {2,S} {6,S}
6   Cs u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-21.1076,-22.3405,-21.9755,-20.2055,-17.8073,-14.9817,-12.3823],'J/(mol*K)'),
        H298 = (402.876,'kJ/mol'),
        S298 = (254.658,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_4_5_ene_3 from polycyclic_all_thermoLiabrary library.
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
1   Cd u0 {3,S} {4,S} {6,D}
2   Cd u0 {3,S} {4,S} {5,D}
3 * Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {2,S}
5   Cd u0 {2,D} {6,S}
6   Cd u0 {1,D} {5,S}
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
Fitted from molecule s3_4_5_diene_0_2 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 145,
    label = "s3_4_5_diene_0_3",
    group = 
"""
1   Cd u0 {3,S} {4,S} {6,D}
2   Cd u0 {3,S} {4,D} {5,S}
3 * Cs u0 {1,S} {2,S}
4   Cd u0 {1,S} {2,D}
5   Cs u0 {2,S} {6,S}
6   Cd u0 {1,D} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-16.0961,-23.1066,-25.1175,-23.8,-20.3886,-17.9916,-15.1753],'J/(mol*K)'),
        H298 = (425.803,'kJ/mol'),
        S298 = (275.729,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_4_5_diene_0_3 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 146,
    label = "s3_4_5_diene_1_3",
    group = 
"""
1   Cs u0 {3,S} {4,S} {5,S}
2   Cd u0 {3,D} {4,S} {6,S}
3 * Cd u0 {1,S} {2,D}
4   Cs u0 {1,S} {2,S}
5   Cd u0 {1,S} {6,D}
6   Cd u0 {2,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-29.109,-28.7021,-26.8164,-24.6529,-20.7769,-17.6863,-15.1744],'J/(mol*K)'),
        H298 = (412.175,'kJ/mol'),
        S298 = (273.542,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_4_5_diene_1_3 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 147,
    label = "s3_4_5_diene_3_4",
    group = 
"""
1   Cd u0 {3,D} {4,S} {5,S}
2   Cd u0 {3,S} {4,D} {6,S}
3 * Cd u0 {1,D} {2,S}
4   Cd u0 {1,S} {2,D}
5   Cs u0 {1,S} {6,S}
6   Cs u0 {2,S} {5,S}
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
Fitted from molecule s3_4_5_diene_3_4 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 0,
    label = "s3_4_6",
    group = 
"""
1   C u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
2   C u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 * C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
5   C u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
6   C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
7   C u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
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
1   Cs u0 {3,S} {4,S} {6,S}
2   Cs u0 {3,S} {4,S} {5,S}
3 * Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {2,S}
5   Cs u0 {2,S} {7,S}
6   Cs u0 {1,S} {7,S}
7   Cs u0 {5,S} {6,S}
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
Fitted from molecule s3_4_6_ane from polycyclic_all_thermoLiabrary library.
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
1   Cd u0 {3,S} {4,S} {6,D}
2   Cs u0 {3,S} {4,S} {5,S}
3 * Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {2,S}
5   Cs u0 {2,S} {7,S}
6   Cd u0 {1,D} {7,S}
7   Cs u0 {5,S} {6,S}
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
Fitted from molecule s3_4_6_ene_0 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 150,
    label = "s3_4_6_ene_1",
    group = 
"""
1   Cs u0 {3,S} {4,S} {6,S}
2   Cs u0 {3,S} {4,S} {5,S}
3 * Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {2,S}
5   Cs u0 {2,S} {7,S}
6   Cd u0 {1,S} {7,D}
7   Cd u0 {5,S} {6,D}
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
Fitted from molecule s3_4_6_ene_1 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 151,
    label = "s3_4_6_ene_4",
    group = 
"""
1   Cs u0 {3,S} {4,S} {5,S}
2   Cd u0 {3,D} {4,S} {6,S}
3 * Cd u0 {1,S} {2,D}
4   Cs u0 {1,S} {2,S}
5   Cs u0 {1,S} {7,S}
6   Cs u0 {2,S} {7,S}
7   Cs u0 {5,S} {6,S}
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
Fitted from molecule s3_4_6_ene_4 from polycyclic_all_thermoLiabrary library.
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
1   Cs u0 {3,S} {4,S} {6,S}
2   Cd u0 {3,S} {4,S} {5,D}
3 * Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {2,S}
5   Cd u0 {2,D} {7,S}
6   Cd u0 {1,S} {7,D}
7   Cd u0 {5,S} {6,D}
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
Fitted from molecule s3_4_6_diene_0_2 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 153,
    label = "s3_4_6_diene_0_3",
    group = 
"""
1   Cd u0 {3,S} {4,S} {5,D}
2   Cd u0 {3,S} {4,S} {6,D}
3 * Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {2,S}
5   Cd u0 {1,D} {7,S}
6   Cd u0 {2,D} {7,S}
7   Cs u0 {5,S} {6,S}
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
Fitted from molecule s3_4_6_diene_0_3 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 154,
    label = "s3_4_6_diene_0_4",
    group = 
"""
1   Cd u0 {3,S} {4,D} {5,S}
2   Cd u0 {3,S} {4,S} {6,D}
3 * Cs u0 {1,S} {2,S}
4   Cd u0 {1,D} {2,S}
5   Cs u0 {1,S} {7,S}
6   Cd u0 {2,D} {7,S}
7   Cs u0 {5,S} {6,S}
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
Fitted from molecule s3_4_6_diene_0_4 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 155,
    label = "s3_4_6_diene_1_4",
    group = 
"""
1   Cs u0 {3,S} {4,S} {5,S}
2   Cd u0 {3,D} {4,S} {6,S}
3 * Cd u0 {1,S} {2,D}
4   Cs u0 {1,S} {2,S}
5   Cd u0 {1,S} {7,D}
6   Cs u0 {2,S} {7,S}
7   Cd u0 {5,D} {6,S}
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
Fitted from molecule s3_4_6_diene_1_4 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 156,
    label = "s3_4_6_diene_1_5",
    group = 
"""
1   Cs u0 {3,S} {4,S} {5,S}
2   Cd u0 {3,D} {4,S} {6,S}
3 * Cd u0 {1,S} {2,D}
4   Cs u0 {1,S} {2,S}
5   Cs u0 {1,S} {7,S}
6   Cd u0 {2,S} {7,D}
7   Cd u0 {5,S} {6,D}
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
Fitted from molecule s3_4_6_diene_1_5 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 0,
    label = "s3_5_5",
    group = 
"""
1   C u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2   C u0 {3,[S,D,T,B]} {6,[S,D,T,B]} {7,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4 * C u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   C u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
7   C u0 {2,[S,D,T,B]} {5,[S,D,T,B]}
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
1   Cs u0 {3,S} {4,S} {5,S}
2   Cs u0 {3,S} {6,S} {7,S}
3   Cs u0 {1,S} {2,S}
4 * Cs u0 {1,S} {6,S}
5   Cs u0 {1,S} {7,S}
6   Cs u0 {2,S} {4,S}
7   Cs u0 {2,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.5,-3.942,-3.291,-2.759,-2.08,-1.628,-0.898],'cal/(mol*K)'),
        H298 = (16.14,'kcal/mol'),
        S298 = (53.47,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
ring strain N. Vandewiele, S and cp modified by A. G. Vandeputte to match BMK/6-311G(2d,d,p) data
""",
)

entry(
    index = 0,
    label = "s3_5_5_ene",
    group = "OR{s3_5_5_ene_1, s3_5_5_ene_side}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 158,
    label = "s3_5_5_ene_1",
    group = 
"""
1   Cs u0 {3,S} {5,S} {6,S}
2   Cs u0 {3,S} {4,S} {7,S}
3   Cs u0 {1,S} {2,S}
4 * Cs u0 {2,S} {5,S}
5   Cs u0 {1,S} {4,S}
6   Cd u0 {1,S} {7,D}
7   Cd u0 {2,S} {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.29,-7.302,-6.501,-5.499,-4.58,-3.778,-2.608],'cal/(mol*K)'),
        H298 = (17.8,'kcal/mol'),
        S298 = (53.75,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
A. G. Vandeputte CBS-QB3 isodesmic reaction, norbornene + 7 ethane -> 2-butene + 2 isobutane + 3 propane, experimental data from the NIST Chemical Webbook
""",
)

entry(
    index = 159,
    label = "s3_5_5_ene_side",
    group = 
"""
1   Cs u0 {3,S} {4,S} {7,S}
2   Cs u0 {3,S} {5,S} {6,S}
3   Cs u0 {1,S} {2,S}
4 * Cs u0 {1,S} {5,S}
5   Cs u0 {2,S} {4,S}
6   Cs u0 {2,S} {7,S}
7   Cd u0 {1,S} {6,S}
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
    index = 0,
    label = "s3_5_5_diene",
    group = "OR{s3_5_5_diene_1_4}",
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
1   Cs u0 {3,S} {6,S} {7,S}
2   Cs u0 {3,S} {4,S} {5,S}
3   Cs u0 {1,S} {2,S}
4 * Cd u0 {2,S} {6,D}
5   Cd u0 {2,S} {7,D}
6   Cd u0 {1,S} {4,D}
7   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.88,-8.43,-6.65,-4.77,-2.79,-3.1,-1.54],'cal/(mol*K)'),
        H298 = (31.64,'kcal/mol'),
        S298 = (57.61,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Properties of Liquids and Gases, Poling 5th Ed. S, Cp from PM7 calculation
""",
)

entry(
    index = 0,
    label = "s3_5_6",
    group = 
"""
1   C u0 {3,[S,D,T,B]} {5,[S,D,T,B]} {6,[S,D,T,B]}
2   C u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {7,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   C u0 {2,[S,D,T,B]} {5,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {4,[S,D,T,B]}
6   C u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
7   C u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
8 * C u0 {6,[S,D,T,B]} {7,[S,D,T,B]}
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
1   Cs u0 {3,S} {5,S} {6,S}
2   Cs u0 {3,S} {4,S} {7,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {2,S} {5,S}
5   Cs u0 {1,S} {4,S}
6   Cs u0 {1,S} {8,S}
7   Cs u0 {2,S} {8,S}
8 * Cs u0 {6,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-11.2,-9.9,-8.4,-7.1,-5.2,-3.8,-1.7],'cal/(mol*K)'),
        H298 = (8.5,'kcal/mol'),
        S298 = (48.66,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
A.G Vandeputte CBS-QB3, isodesmic reactions approach
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
1   Cs u0 {3,S} {4,S} {7,S}
2   Cs u0 {3,S} {5,S} {6,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {5,S}
5   Cs u0 {2,S} {4,S}
6   Cs u0 {2,S} {8,S}
7   Cd u0 {1,S} {8,D}
8 * Cd u0 {6,S} {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.3,-8.3,-7.2,-6.1,-4.8,-3.6,-2],'cal/(mol*K)'),
        H298 = (8.5,'kcal/mol'),
        S298 = (48.61,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
A.G Vandeputte CBS-QB3, isodesmic reactions approach
""",
)

entry(
    index = 163,
    label = "s3_5_6_ene_5",
    group = 
"""
1   Cs u0 {3,S} {4,S} {7,S}
2   Cs u0 {3,S} {5,S} {6,S}
3   Cs u0 {1,S} {2,S}
4   Cd u0 {1,S} {5,D}
5   Cd u0 {2,S} {4,D}
6   Cs u0 {2,S} {8,S}
7   Cs u0 {1,S} {8,S}
8 * Cs u0 {6,S} {7,S}
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
Fitted from molecule s3_5_6_ene_5 from polycyclic_all_thermoLiabrary library.
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
1   Cs u0 {3,S} {4,S} {6,S}
2   Cs u0 {3,S} {5,S} {7,S}
3   Cs u0 {1,S} {2,S}
4   Cd u0 {1,S} {5,D}
5   Cd u0 {2,S} {4,D}
6   Cd u0 {1,S} {8,D}
7   Cs u0 {2,S} {8,S}
8 * Cd u0 {6,D} {7,S}
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
Fitted from molecule s3_5_6_diene_1_5 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 0,
    label = "s3_6_6",
    group = 
"""
1   C u0 {3,[S,D,T,B]} {6,[S,D,T,B]} {7,[S,D,T,B]}
2   C u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4 * C u0 {2,[S,D,T,B]} {9,[S,D,T,B]}
5   C u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
6   C u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
7   C u0 {1,[S,D,T,B]} {9,[S,D,T,B]}
8   C u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
9   C u0 {4,[S,D,T,B]} {7,[S,D,T,B]}
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
1   Cs u0 {3,S} {6,S} {7,S}
2   Cs u0 {3,S} {4,S} {5,S}
3   Cs u0 {1,S} {2,S}
4 * Cs u0 {2,S} {9,S}
5   Cs u0 {2,S} {8,S}
6   Cs u0 {1,S} {8,S}
7   Cs u0 {1,S} {9,S}
8   Cs u0 {5,S} {6,S}
9   Cs u0 {4,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-51.2247,-47.4056,-42.0976,-36.4612,-25.7252,-16.6263,-6.05456],'J/(mol*K)'),
        H298 = (65.8567,'kJ/mol'),
        S298 = (170.519,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_6_6_ane from polycyclic_all_thermoLiabrary library.
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
1   Cs u0 {3,S} {4,S} {7,S}
2   Cd u0 {3,S} {5,S} {6,D}
3   Cs u0 {1,S} {2,S}
4 * Cs u0 {1,S} {8,S}
5   Cs u0 {2,S} {8,S}
6   Cd u0 {2,D} {9,S}
7   Cs u0 {1,S} {9,S}
8   Cs u0 {4,S} {5,S}
9   Cs u0 {6,S} {7,S}
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
Fitted from molecule s3_6_6_ene_0 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 167,
    label = "s3_6_6_ene_1",
    group = 
"""
1   Cs u0 {3,S} {4,S} {6,S}
2   Cs u0 {3,S} {5,S} {7,S}
3   Cs u0 {1,S} {2,S}
4 * Cs u0 {1,S} {9,S}
5   Cs u0 {2,S} {8,S}
6   Cd u0 {1,S} {8,D}
7   Cs u0 {2,S} {9,S}
8   Cd u0 {5,S} {6,D}
9   Cs u0 {4,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-42.2258,-39.5459,-35.7798,-31.0779,-22.7329,-15.0973,-6.6942],'J/(mol*K)'),
        H298 = (67.0007,'kJ/mol'),
        S298 = (180.872,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_6_6_ene_1 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 168,
    label = "s3_6_6_ene_4",
    group = 
"""
1   Cd u0 {3,D} {4,S} {6,S}
2   Cs u0 {3,S} {5,S} {7,S}
3   Cd u0 {1,D} {2,S}
4 * Cs u0 {1,S} {8,S}
5   Cs u0 {2,S} {9,S}
6   Cs u0 {1,S} {9,S}
7   Cs u0 {2,S} {8,S}
8   Cs u0 {4,S} {7,S}
9   Cs u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-31.5534,-30.7949,-29.0665,-24.8037,-17.0309,-10.8024,-4.68532],'J/(mol*K)'),
        H298 = (449.093,'kJ/mol'),
        S298 = (191.929,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_6_6_ene_4 from polycyclic_all_thermoLiabrary library.
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
1   Cd u0 {3,S} {4,D} {5,S}
2   Cd u0 {3,D} {6,S} {7,S}
3   Cd u0 {1,S} {2,D}
4 * Cd u0 {1,D} {9,S}
5   Cs u0 {1,S} {8,S}
6   Cs u0 {2,S} {9,S}
7   Cs u0 {2,S} {8,S}
8   Cs u0 {5,S} {7,S}
9   Cs u0 {4,S} {6,S}
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
Fitted from molecule s3_6_6_diene_0_m from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 170,
    label = "s3_6_6_diene_0_2",
    group = 
"""
1   Cs u0 {3,S} {6,S} {7,S}
2   Cd u0 {3,S} {4,S} {5,D}
3   Cs u0 {1,S} {2,S}
4 * Cs u0 {2,S} {9,S}
5   Cd u0 {2,D} {8,S}
6   Cd u0 {1,S} {8,D}
7   Cs u0 {1,S} {9,S}
8   Cd u0 {5,S} {6,D}
9   Cs u0 {4,S} {7,S}
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
Fitted from molecule s3_6_6_diene_0_2 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 171,
    label = "s3_6_6_diene_0_3",
    group = 
"""
1   Cd u0 {3,S} {6,S} {7,D}
2   Cd u0 {3,S} {4,D} {5,S}
3   Cs u0 {1,S} {2,S}
4 * Cd u0 {2,D} {9,S}
5   Cs u0 {2,S} {8,S}
6   Cs u0 {1,S} {8,S}
7   Cd u0 {1,D} {9,S}
8   Cs u0 {5,S} {6,S}
9   Cs u0 {4,S} {7,S}
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
Fitted from molecule s3_6_6_diene_0_3 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 172,
    label = "s3_6_6_diene_0_4",
    group = 
"""
1   Cd u0 {3,S} {5,S} {7,D}
2   Cd u0 {3,S} {4,S} {6,D}
3   Cs u0 {1,S} {2,S}
4 * Cs u0 {2,S} {9,S}
5   Cs u0 {1,S} {8,S}
6   Cd u0 {2,D} {8,S}
7   Cd u0 {1,D} {9,S}
8   Cs u0 {5,S} {6,S}
9   Cs u0 {4,S} {7,S}
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
Fitted from molecule s3_6_6_diene_0_4 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 173,
    label = "s3_6_6_diene_0_5",
    group = 
"""
1   Cs u0 {3,S} {4,S} {7,S}
2   Cd u0 {3,S} {5,D} {6,S}
3   Cs u0 {1,S} {2,S}
4 * Cs u0 {1,S} {9,S}
5   Cd u0 {2,D} {9,S}
6   Cs u0 {2,S} {8,S}
7   Cd u0 {1,S} {8,D}
8   Cd u0 {6,S} {7,D}
9   Cs u0 {4,S} {5,S}
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
Fitted from molecule s3_6_6_diene_0_5 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 174,
    label = "s3_6_6_diene_0_6",
    group = 
"""
1   Cs u0 {3,S} {6,S} {7,S}
2   Cd u0 {3,S} {4,D} {5,S}
3   Cs u0 {1,S} {2,S}
4 * Cd u0 {2,D} {8,S}
5   Cd u0 {2,S} {9,D}
6   Cs u0 {1,S} {8,S}
7   Cs u0 {1,S} {9,S}
8   Cs u0 {4,S} {6,S}
9   Cd u0 {5,D} {7,S}
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
Fitted from molecule s3_6_6_diene_0_6 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 175,
    label = "s3_6_6_diene_1_m",
    group = 
"""
1   Cd u0 {3,D} {6,S} {7,S}
2   Cs u0 {3,S} {4,S} {5,S}
3   Cd u0 {1,D} {2,S}
4 * Cd u0 {2,S} {9,D}
5   Cs u0 {2,S} {8,S}
6   Cs u0 {1,S} {8,S}
7   Cs u0 {1,S} {9,S}
8   Cs u0 {5,S} {6,S}
9   Cd u0 {4,D} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-37.3301,-33.3122,-29.196,-25.2285,-17.6312,-12.0471,-5.61348],'J/(mol*K)'),
        H298 = (292.685,'kJ/mol'),
        S298 = (195.572,'J/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from molecule s3_6_6_diene_1_m from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 176,
    label = "s3_6_6_diene_1_5",
    group = 
"""
1   Cs u0 {3,S} {4,S} {6,S}
2   Cs u0 {3,S} {5,S} {7,S}
3   Cs u0 {1,S} {2,S}
4 * Cs u0 {1,S} {9,S}
5   Cd u0 {2,S} {9,D}
6   Cd u0 {1,S} {8,D}
7   Cs u0 {2,S} {8,S}
8   Cd u0 {6,D} {7,S}
9   Cd u0 {4,S} {5,D}
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
Fitted from molecule s3_6_6_diene_1_5 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 177,
    label = "s3_6_6_diene_1_6",
    group = 
"""
1   Cs u0 {3,S} {5,S} {6,S}
2   Cs u0 {3,S} {4,S} {7,S}
3   Cs u0 {1,S} {2,S}
4 * Cs u0 {2,S} {9,S}
5   Cd u0 {1,S} {9,D}
6   Cd u0 {1,S} {8,D}
7   Cs u0 {2,S} {8,S}
8   Cd u0 {6,D} {7,S}
9   Cd u0 {4,S} {5,D}
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
Fitted from molecule s3_6_6_diene_1_6 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 178,
    label = "s3_6_6_diene_1_8",
    group = 
"""
1   Cs u0 {3,S} {4,S} {6,S}
2   Cd u0 {3,D} {5,S} {7,S}
3   Cd u0 {1,S} {2,D}
4 * Cs u0 {1,S} {8,S}
5   Cd u0 {2,S} {8,D}
6   Cs u0 {1,S} {9,S}
7   Cs u0 {2,S} {9,S}
8   Cd u0 {4,S} {5,D}
9   Cs u0 {6,S} {7,S}
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
Fitted from molecule s3_6_6_diene_1_8 from polycyclic_all_thermoLiabrary library.
""",
)

entry(
    index = 0,
    label = "s4_6_6",
    group = 
"""
1 * C u0 {3,[S,D,T,B]} {6,[S,D,T,B]} {8,[S,D,T,B]}
2   C u0 {4,[S,D,T,B]} {5,[S,D,T,B]} {7,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {4,[S,D,T,B]}
4   C u0 {2,[S,D,T,B]} {3,[S,D,T,B]}
5   C u0 {2,[S,D,T,B]} {6,[S,D,T,B]}
6   C u0 {1,[S,D,T,B]} {5,[S,D,T,B]}
7   C u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
8   C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
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
1 * Cs u0 {3,S} {6,S} {8,S}
2   Cs u0 {4,S} {5,S} {7,S}
3   Cs u0 {1,S} {4,S}
4   Cs u0 {2,S} {3,S}
5   Cs u0 {2,S} {6,S}
6   Cs u0 {1,S} {5,S}
7   Cs u0 {2,S} {8,S}
8   Cs u0 {1,S} {7,S}
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

tree(
"""
L1: PolycyclicRing
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
        L3: s2_3_5_ane
        L3: s2_3_5_ene
            L4: s2_3_5_ene_1
    L2: s2_3_6
        L3: s2_3_6_ane
        L3: s2_3_6_ene
            L4: s2_3_6_ene_1
            L4: s2_3_6_ene_2
        L3: s2_3_6_diene
            L4: s2_3_6_diene_1_3
    L2: s2_3_7
        L3: s2_3_7_ane
    L2: s2_3_8
        L3: s2_3_8_ane
    L2: s2_4_4
        L3: s2_4_4_ane
        L3: s2_4_4_ene
            L4: s2_4_4_ene_1
            L4: s2_4_4_ene_m
    L2: s2_4_5
        L3: s2_4_5_ane
        L3: s2_4_5_ene
            L4: s2_4_5_ene_1
    L2: s2_4_6
        L3: s2_4_6_ane
        L3: s2_4_6_ene
            L4: s2_4_6_ene_1
            L4: s2_4_6_ene_2
        L3: s2_4_6_diene
            L4: s2_4_6_diene_1_3
            L4: s2_4_6_diene_1_6
            L4: s2_4_6_diene_2_6
        L3: s2_4_6_ben
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
        L3: s2_5_6_ben
        L3: s2_5_6_indene
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
        L3: s2_6_6_ben
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
    L2: s3_5_5
        L3: s3_5_5_ane
        L3: s3_5_5_ene
            L4: s3_5_5_ene_1
            L4: s3_5_5_ene_side
        L3: s3_5_5_diene
            L4: s3_5_5_diene_1_4
    L2: s3_5_6
        L3: s3_5_6_ane
        L3: s3_5_6_ene
            L4: s3_5_6_ene_1
            L4: s3_5_6_ene_5
        L3: s3_5_6_diene
            L4: s3_5_6_diene_1_5
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
    L2: s4_6_6
        L3: s4_6_6_ane
"""
)

