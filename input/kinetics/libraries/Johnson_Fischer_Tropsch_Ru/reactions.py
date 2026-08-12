#!/usr/bin/env python
# encoding: utf-8

name = "Johnson_Fischer_Tropsch_Ru"
shortDesc = u""
longDesc = u""""""
entry(
    index = 0,
    label = "OC=[Pt] + vacantX <=> O[Pt] + C#[Pt]",
    kinetics = SurfaceArrhenius(A=(3.36614e-10,'m^2/(molecule*s)'), n=1.1734, Ea=(25.8091,'kJ/mol'), T0=(1,'K'), Tmin=(298.15,'K'), Tmax=(2000,'K'), comment="""Fitted to 172 data points; dA = *|/ 1.06174, dn = +|- 0.00771875, dEa = +|- 0.0486125 kJ/mol"""),
    shortDesc = u"Computed using Pynta",
    longDesc = u"""Computed using Pynta
reactants:
1 *1 H u0 p0 c0 {2,S}
2 *2 C u0 p0 c0 {1,S} {3,S} {5,D}
3 *3 O u0 p2 c0 {2,S} {4,S}
4 *4 H u0 p0 c0 {3,S}
5 *5 X u0 p0 c0 {2,D}
6 *6 X u0 p0 c0
products:
1 *1 H u0 p0 c0 {2,S}
2 *2 C u0 p0 c0 {1,S} {5,T}
3 *3 O u0 p2 c0 {4,S} {6,S}
4 *4 H u0 p0 c0 {3,S}
5 *5 X u0 p0 c0 {2,T}
6 *6 X u0 p0 c0 {3,S}
""",
    metal = "Ru",
    facet = "0001",
)
entry(
    index = 1,
    label = "O=C=[Pt] + vacantX <=> O=[Pt] + C$[Pt]",
    kinetics = SurfaceArrhenius(A=(7.62364e-11,'m^2/(molecule*s)'), n=1.49102, Ea=(210.673,'kJ/mol'), T0=(1,'K'), Tmin=(298.15,'K'), Tmax=(2000,'K'), comment="""Fitted to 172 data points; dA = *|/ 1.04117, dn = +|- 0.00519756, dEa = +|- 0.0327341 kJ/mol"""),
    shortDesc = u"Computed using Pynta",
    longDesc = u"""Computed using Pynta
reactants:
1 *1 C u0 p0 c0 {2,D} {3,D}
2 *2 O u0 p2 c0 {1,D}
3 *3 X u0 p0 c0 {1,D}
4 *4 X u0 p0 c0
products:
1 *1 C u0 p0 c0 {3,Q}
2 *2 O u0 p2 c0 {4,D}
3 *3 X u0 p0 c0 {1,Q}
4 *4 X u0 p0 c0 {2,D}
""",
    metal = "Ru",
    facet = "0001",
)
entry(
    index = 2,
    label = "C#[Pt] + vacantX <=> [Pt] + C$[Pt]",
    kinetics = SurfaceArrhenius(A=(5.4942e-08,'m^2/(molecule*s)'), n=0.459103, Ea=(75.8873,'kJ/mol'), T0=(1,'K'), Tmin=(298.15,'K'), Tmax=(2000,'K'), comment="""Fitted to 172 data points; dA = *|/ 1.01589, dn = +|- 0.00203051, dEa = +|- 0.0127881 kJ/mol"""),
    shortDesc = u"Computed using Pynta",
    longDesc = u"""Computed using Pynta
reactants:
1 *1 C u0 p0 c0 {2,S} {3,T}
2 *2 H u0 p0 c0 {1,S}
3 *3 X u0 p0 c0 {1,T}
4 *4 X u0 p0 c0
products:
1 *1 C u0 p0 c0 {3,Q}
2 *2 H u0 p0 c0 {4,S}
3 *3 X u0 p0 c0 {1,Q}
4 *4 X u0 p0 c0 {2,S}
""",
    metal = "Ru",
    facet = "0001",
)
entry(
    index = 3,
    label = "OC=[Pt] + vacantX <=> [Pt] + O=C[Pt]",
    kinetics = SurfaceArrhenius(A=(2.48507e-12,'m^2/(molecule*s)'), n=2.13217, Ea=(-5.2585,'kJ/mol'), T0=(1,'K'), Tmin=(298.15,'K'), Tmax=(2000,'K'), comment="""Fitted to 172 data points; dA = *|/ 1.0434, dn = +|- 0.00547327, dEa = +|- 0.0344705 kJ/mol"""),
    shortDesc = u"Computed using Pynta",
    longDesc = u"""Computed using Pynta
reactants:
1 *1 H u0 p0 c0 {2,S}
2 *2 C u0 p0 c0 {1,S} {3,S} {5,D}
3 *3 O u0 p2 c0 {2,S} {4,S}
4 *4 H u0 p0 c0 {3,S}
5 *5 X u0 p0 c0 {2,D}
6 *6 X u0 p0 c0
products:
1 *1 H u0 p0 c0 {2,S}
2 *2 C u0 p0 c0 {1,S} {3,D} {5,S}
3 *3 O u0 p2 c0 {2,D}
4 *4 H u0 p0 c0 {6,S}
5 *5 X u0 p0 c0 {2,S}
6 *6 X u0 p0 c0 {4,S}
""",
    metal = "Ru",
    facet = "0001",
)
entry(
    index = 4,
    label = "CC(=O)[Pt] + vacantX <=> O=C=[Pt] + C[Pt]",
    kinetics = SurfaceArrhenius(A=(7.76895e-14,'m^2/(molecule*s)'), n=1.09399, Ea=(15.0217,'kJ/mol'), T0=(1,'K'), Tmin=(298.15,'K'), Tmax=(2000,'K'), comment="""Fitted to 172 data points; dA = *|/ 1.00736, dn = +|- 0.000944485, dEa = +|- 0.00594834 kJ/mol"""),
    shortDesc = u"Computed using Pynta",
    longDesc = u"""Computed using Pynta
reactants:
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 p0 c0 {1,S}
3 *3 H u0 p0 c0 {1,S}
4 *4 H u0 p0 c0 {1,S}
5 *5 C u0 p0 c0 {1,S} {6,D} {8,S}
6 *6 O u0 p2 c0 {5,D}
7 *7 X u0 p0 c0
8 *8 X u0 p0 c0 {5,S}
products:
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *2 H u0 p0 c0 {1,S}
3 *3 H u0 p0 c0 {1,S}
4 *4 H u0 p0 c0 {1,S}
5 *5 C u0 p0 c0 {6,D} {8,D}
6 *6 O u0 p2 c0 {5,D}
7 *7 X u0 p0 c0 {1,S}
8 *8 X u0 p0 c0 {5,D}
""",
    metal = "Ru",
    facet = "0001",
)
entry(
    index = 5,
    label = "CC(=O)[Pt] + vacantX <=> CC#[Pt] + O=[Pt]",
    kinetics = SurfaceArrhenius(A=(1.97817e-11,'m^2/(molecule*s)'), n=0.334956, Ea=(88.1743,'kJ/mol'), T0=(1,'K'), Tmin=(298.15,'K'), Tmax=(2000,'K'), comment="""Fitted to 172 data points; dA = *|/ 1.04219, dn = +|- 0.00532425, dEa = +|- 0.033532 kJ/mol"""),
    shortDesc = u"Computed using Pynta",
    longDesc = u"""Computed using Pynta
reactants:
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 p0 c0 {1,S}
3 *3 H u0 p0 c0 {1,S}
4 *4 H u0 p0 c0 {1,S}
5 *5 C u0 p0 c0 {1,S} {6,D} {8,S}
6 *6 O u0 p2 c0 {5,D}
7 *7 X u0 p0 c0
8 *8 X u0 p0 c0 {5,S}
products:
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 p0 c0 {1,S}
3 *3 H u0 p0 c0 {1,S}
4 *4 H u0 p0 c0 {1,S}
5 *5 C u0 p0 c0 {1,S} {8,T}
6 *6 O u0 p2 c0 {7,D}
7 *7 X u0 p0 c0 {6,D}
8 *8 X u0 p0 c0 {5,T}
""",
    metal = "Ru",
    facet = "0001",
)
entry(
    index = 6,
    label = "C=[Pt] + vacantX <=> [Pt] + C#[Pt]",
    kinetics = SurfaceArrhenius(A=(8.60808e-08,'m^2/(molecule*s)'), n=0.321739, Ea=(5.03302,'kJ/mol'), T0=(1,'K'), Tmin=(298.15,'K'), Tmax=(2000,'K'), comment="""Fitted to 172 data points; dA = *|/ 1.02731, dn = +|- 0.00347199, dEa = +|- 0.0218665 kJ/mol"""),
    shortDesc = u"Computed using Pynta",
    longDesc = u"""Computed using Pynta
reactants:
1 *1 H u0 p0 c0 {2,S}
2 *2 C u0 p0 c0 {1,S} {3,S} {4,D}
3 *3 H u0 p0 c0 {2,S}
4 *4 X u0 p0 c0 {2,D}
5 *5 X u0 p0 c0
products:
1 *1 H u0 p0 c0 {2,S}
2 *2 C u0 p0 c0 {1,S} {4,T}
3 *3 H u0 p0 c0 {5,S}
4 *4 X u0 p0 c0 {2,T}
5 *5 X u0 p0 c0 {3,S}
""",
    metal = "Ru",
    facet = "0001",
)
entry(
    index = 7,
    label = "O=C[Pt] + vacantX <=> O=C=[Pt] + [Pt]",
    kinetics = SurfaceArrhenius(A=(2.98618e-09,'m^2/(molecule*s)'), n=0.53959, Ea=(-108.896,'kJ/mol'), T0=(1,'K'), Tmin=(298.15,'K'), Tmax=(2000,'K'), comment="""Fitted to 172 data points; dA = *|/ 1.0249, dn = +|- 0.00316937, dEa = +|- 0.0199606 kJ/mol"""),
    shortDesc = u"Computed using Pynta",
    longDesc = u"""Computed using Pynta
reactants:
1 *1 H u0 p0 c0 {2,S}
2 *2 C u0 p0 c0 {1,S} {3,D} {5,S}
3 *3 O u0 p2 c0 {2,D}
4 *4 X u0 p0 c0
5 *5 X u0 p0 c0 {2,S}
products:
1 *1 H u0 p0 c0 {4,S}
2 *2 C u0 p0 c0 {3,D} {5,D}
3 *3 O u0 p2 c0 {2,D}
4 *4 X u0 p0 c0 {1,S}
5 *5 X u0 p0 c0 {2,D}
""",
    metal = "Ru",
    facet = "0001",
)
entry(
    index = 8,
    label = "O[Pt] + vacantX <=> [Pt] + O=[Pt]",
    kinetics = SurfaceArrhenius(A=(7.04881e-09,'m^2/(molecule*s)'), n=0.673431, Ea=(85.1807,'kJ/mol'), T0=(1,'K'), Tmin=(298.15,'K'), Tmax=(2000,'K'), comment="""Fitted to 172 data points; dA = *|/ 1.01055, dn = +|- 0.00135189, dEa = +|- 0.00851418 kJ/mol"""),
    shortDesc = u"Computed using Pynta",
    longDesc = u"""Computed using Pynta
reactants:
1 *1 H u0 p0 c0 {2,S}
2 *2 O u0 p2 c0 {1,S} {3,S}
3 *3 X u0 p0 c0 {2,S}
4 *4 X u0 p0 c0
products:
1 *1 H u0 p0 c0 {4,S}
2 *2 O u0 p2 c0 {3,D}
3 *3 X u0 p0 c0 {2,D}
4 *4 X u0 p0 c0 {1,S}
""",
    metal = "Ru",
    facet = "0001",
)
entry(
    index = 9,
    label = "O[Pt] + [Pt] <=> O + vacantX + vacantX",
    kinetics = SurfaceArrhenius(A=(6.6189e-07,'m^2/(molecule*s)'), n=0.297662, Ea=(117.334,'kJ/mol'), T0=(1,'K'), Tmin=(298.15,'K'), Tmax=(2000,'K'), comment="""Fitted to 172 data points; dA = *|/ 1.0461, dn = +|- 0.00580697, dEa = +|- 0.0365722 kJ/mol"""),
    shortDesc = u"Computed using Pynta",
    longDesc = u"""Computed using Pynta
reactants:
1 *1 H u0 p0 c0 {2,S}
2 *2 O u0 p2 c0 {1,S} {4,S}
3 *3 H u0 p0 c0 {5,S}
4 *4 X u0 p0 c0 {2,S}
5 *5 X u0 p0 c0 {3,S}
products:
1 *1 H u0 p0 c0 {2,S}
2 *2 O u0 p2 c0 {1,S} {3,S}
3 *3 H u0 p0 c0 {2,S}
4 *4 X u0 p0 c0
5 *5 X u0 p0 c0
""",
    metal = "Ru",
    facet = "0001",
)
entry(
    index = 10,
    label = "[Pt] + [Pt] <=> [H][H] + vacantX + vacantX",
    kinetics = SurfaceArrhenius(A=(8.74435e-07,'m^2/(molecule*s)'), n=0.0266268, Ea=(11.3926,'kJ/mol'), T0=(1,'K'), Tmin=(298.15,'K'), Tmax=(2000,'K'), comment="""Fitted to 172 data points; dA = *|/ 1.01313, dn = +|- 0.00168107, dEa = +|- 0.0105873 kJ/mol"""),
    shortDesc = u"Computed using Pynta",
    longDesc = u"""Computed using Pynta
reactants:
1 *1 H u0 p0 c0 {3,S}
2 *2 H u0 p0 c0 {4,S}
3 *3 X u0 p0 c0 {1,S}
4 *4 X u0 p0 c0 {2,S}
products:
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
3 *3 X u0 p0 c0
4 *4 X u0 p0 c0
""",
    metal = "Ru",
    facet = "0001",
)
entry(
    index = 11,
    label = "C[Pt] + vacantX <=> [Pt] + C=[Pt]",
    kinetics = SurfaceArrhenius(A=(4.26137e-09,'m^2/(molecule*s)'), n=0.585311, Ea=(38.3311,'kJ/mol'), T0=(1,'K'), Tmin=(298.15,'K'), Tmax=(2000,'K'), comment="""Fitted to 172 data points; dA = *|/ 1.01677, dn = +|- 0.00214233, dEa = +|- 0.0134924 kJ/mol"""),
    shortDesc = u"Computed using Pynta",
    longDesc = u"""Computed using Pynta
reactants:
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 p0 c0 {1,S}
3 *3 H u0 p0 c0 {1,S}
4 *4 H u0 p0 c0 {1,S}
5 *5 X u0 p0 c0 {1,S}
6 *6 X u0 p0 c0
products:
1 *1 C u0 p0 c0 {2,S} {3,S} {5,D}
2 *2 H u0 p0 c0 {1,S}
3 *3 H u0 p0 c0 {1,S}
4 *4 H u0 p0 c0 {6,S}
5 *5 X u0 p0 c0 {1,D}
6 *6 X u0 p0 c0 {4,S}
""",
    metal = "Ru",
    facet = "0001",
)
entry(
    index = 12,
    label = "C#[Pt] + C#[Pt] <=> C#C + vacantX + vacantX",
    kinetics = SurfaceArrhenius(A=(1.51326e-06,'m^2/(molecule*s)'), n=-0.151277, Ea=(110.227,'kJ/mol'), T0=(1,'K'), Tmin=(298.15,'K'), Tmax=(2000,'K'), comment="""Fitted to 172 data points; dA = *|/ 1.01496, dn = +|- 0.00191327, dEa = +|- 0.0120497 kJ/mol"""),
    shortDesc = u"Computed using Pynta",
    longDesc = u"""Computed using Pynta
reactants:
1 *1 C u0 p0 c0 {2,S} {5,T}
2 *2 H u0 p0 c0 {1,S}
3 *3 C u0 p0 c0 {4,S} {6,T}
4 *4 H u0 p0 c0 {3,S}
5 *5 X u0 p0 c0 {1,T}
6 *6 X u0 p0 c0 {3,T}
products:
1 *1 C u0 p0 c0 {2,S} {3,T}
2 *2 H u0 p0 c0 {1,S}
3 *3 C u0 p0 c0 {1,T} {4,S}
4 *4 H u0 p0 c0 {3,S}
5 *5 X u0 p0 c0
6 *6 X u0 p0 c0
""",
    metal = "Ru",
    facet = "0001",
)
entry(
    index = 13,
    label = "C[Pt] + [Pt] <=> C + vacantX + vacantX",
    kinetics = SurfaceArrhenius(A=(0.757996,'m^2/(molecule*s)'), n=-2.2098, Ea=(96.0116,'kJ/mol'), T0=(1,'K'), Tmin=(298.15,'K'), Tmax=(2000,'K'), comment="""Fitted to 172 data points; dA = *|/ 1.02832, dn = +|- 0.00359789, dEa = +|- 0.0226594 kJ/mol"""),
    shortDesc = u"Computed using Pynta",
    longDesc = u"""Computed using Pynta
reactants:
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *2 H u0 p0 c0 {1,S}
3 *3 H u0 p0 c0 {1,S}
4 *4 H u0 p0 c0 {1,S}
5 *5 H u0 p0 c0 {7,S}
6 *6 X u0 p0 c0 {1,S}
7 *7 X u0 p0 c0 {5,S}
products:
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 p0 c0 {1,S}
3 *3 H u0 p0 c0 {1,S}
4 *4 H u0 p0 c0 {1,S}
5 *5 H u0 p0 c0 {1,S}
6 *6 X u0 p0 c0
7 *7 X u0 p0 c0
""",
    metal = "Ru",
    facet = "0001",
)
