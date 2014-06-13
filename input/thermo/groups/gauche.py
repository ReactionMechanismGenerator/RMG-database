#!/usr/bin/env python
# encoding: utf-8

name = "Gauche Interaction Corrections"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 0,
    label = "CsOsCd",
    group = 
"""
1 * {Cs,Os,Cd} 0
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

""",
)

entry(
    index = 1,
    label = "Cs(RRRR)",
    group = 
"""
1 * Cs 0
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

""",
)

entry(
    index = 2,
    label = "Cs(CsRRR)",
    group = 
"""
1 * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2   Cs                         0 {1,S}
3   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
4   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
5   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
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

""",
)

entry(
    index = 3,
    label = "Cs(Cs(CsRR)RRR)",
    group = 
"""
1 * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2   Cs                         0 {1,S} {6,S} {7,S} {8,S}
3   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
4   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
5   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
6   Cs                         0 {2,S}
7   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
8   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
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

""",
)

entry(
    index = 4,
    label = "Cs(Cs(CsCsR)RRR)",
    group = 
"""
1 * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2   Cs                         0 {1,S} {6,S} {7,S} {8,S}
3   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
4   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
5   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
6   Cs                         0 {2,S}
7   Cs                         0 {2,S}
8   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
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

""",
)

entry(
    index = 5,
    label = "Cs(Cs(CsCsCs)RRR)",
    group = 
"""
1 * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2   Cs                         0 {1,S} {6,S} {7,S} {8,S}
3   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
4   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
5   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
6   Cs                         0 {2,S}
7   Cs                         0 {2,S}
8   Cs                         0 {2,S}
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

""",
)

entry(
    index = 6,
    label = "Cs(CsCsRR)",
    group = 
"""
1 * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2   Cs                         0 {1,S}
3   Cs                         0 {1,S}
4   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
5   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
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

""",
)

entry(
    index = 7,
    label = "Cs(Cs(CsRR)CsRR)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
5    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
6    Cs                         0 {2,S}
7    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
8    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
9    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
10   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
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

""",
)

entry(
    index = 8,
    label = "Cs(Cs(CsRR)Cs(CsRR)RR)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
5    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
6    Cs                         0 {2,S}
7    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
8    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
9    Cs                         0 {3,S}
10   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
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

""",
)

entry(
    index = 9,
    label = "Cs(Cs(CsCsR)CsRR)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
5    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
9    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
10   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0.4,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "Cs(Cs(CsCsR)Cs(CsRR)RR)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
5    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
9    Cs                         0 {3,S}
10   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0.4,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "Cs(Cs(CsCsR)Cs(CsCsR)RR)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
5    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
9    Cs                         0 {3,S}
10   Cs                         0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0.8,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "Cs(Cs(CsCsCs)CsRR)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
5    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    Cs                         0 {2,S}
9    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
10   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0.8,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "Cs(Cs(CsCsCs)Cs(CsRR)RR)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
5    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    Cs                         0 {2,S}
9    Cs                         0 {3,S}
10   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0.8,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "Cs(Cs(CsCsCs)Cs(CsCsR)RR)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
5    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    Cs                         0 {2,S}
9    Cs                         0 {3,S}
10   Cs                         0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (1.2,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "Cs(Cs(CsCsCs)Cs(CsCsCs)RR)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
5    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    Cs                         0 {2,S}
9    Cs                         0 {3,S}
10   Cs                         0 {3,S}
11   Cs                         0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (1.6,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "Cs(CsCsCsR)",
    group = 
"""
1 * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2   Cs                         0 {1,S}
3   Cs                         0 {1,S}
4   Cs                         0 {1,S}
5   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
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

""",
)

entry(
    index = 17,
    label = "Cs(Cs(CsRR)CsCsR)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
6    Cs                         0 {2,S}
7    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
8    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
9    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
10   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
12   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
13   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0.4,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "Cs(Cs(CsRR)Cs(CsRR)CsR)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
6    Cs                         0 {2,S}
7    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
8    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
9    Cs                         0 {3,S}
10   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
12   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
13   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0.8,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "Cs(Cs(CsRR)Cs(CsRR)Cs(CsRR)R)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
6    Cs                         0 {2,S}
7    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
8    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
9    Cs                         0 {3,S}
10   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
12   Cs                         0 {4,S}
13   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (1.2,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "Cs(Cs(CsCsR)CsCsR)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
9    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
10   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
12   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
13   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0.8,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "Cs(Cs(CsCsR)Cs(CsRR)CsR)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
9    Cs                         0 {3,S}
10   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
12   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
13   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (1.2,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "Cs(Cs(CsCsR)Cs(CsRR)Cs(CsRR)R)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
9    Cs                         0 {3,S}
10   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
12   Cs                         0 {4,S}
13   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (1.6,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "Cs(Cs(CsCsR)Cs(CsCsR)CsR)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
9    Cs                         0 {3,S}
10   Cs                         0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
12   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
13   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (2.4,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "Cs(Cs(CsCsR)Cs(CsCsR)Cs(CsRR)R)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
9    Cs                         0 {3,S}
10   Cs                         0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
12   Cs                         0 {4,S}
13   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (2.8,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "Cs(Cs(CsCsR)Cs(CsCsR)Cs(CsCsR)R)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
9    Cs                         0 {3,S}
10   Cs                         0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
12   Cs                         0 {4,S}
13   Cs                         0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (3.2,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "Cs(Cs(CsCsCs)CsCsR)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    Cs                         0 {2,S}
9    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
10   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
12   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
13   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (1.6,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "Cs(Cs(CsCsCs)Cs(CsRR)CsR)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    Cs                         0 {2,S}
9    Cs                         0 {3,S}
10   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
12   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
13   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (2,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "Cs(Cs(CsCsCs)Cs(CsRR)Cs(CsRR)R)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    Cs                         0 {2,S}
9    Cs                         0 {3,S}
10   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
12   Cs                         0 {4,S}
13   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (2.4,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "Cs(Cs(CsCsCs)Cs(CsCsR)CsR)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    Cs                         0 {2,S}
9    Cs                         0 {3,S}
10   Cs                         0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
12   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
13   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (2.4,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "Cs(Cs(CsCsCs)Cs(CsCsR)Cs(CsRR)R)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    Cs                         0 {2,S}
9    Cs                         0 {3,S}
10   Cs                         0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
12   Cs                         0 {4,S}
13   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (2.8,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "Cs(Cs(CsCsCs)Cs(CsCsR)Cs(CsCsR)R)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    Cs                         0 {2,S}
9    Cs                         0 {3,S}
10   Cs                         0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
12   Cs                         0 {4,S}
13   Cs                         0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (4,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "Cs(Cs(CsCsCs)Cs(CsCsCs)CsR)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    Cs                         0 {2,S}
9    Cs                         0 {3,S}
10   Cs                         0 {3,S}
11   Cs                         0 {3,S}
12   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
13   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (3.2,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "Cs(Cs(CsCsCs)Cs(CsCsCs)Cs(CsRR)R)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    Cs                         0 {2,S}
9    Cs                         0 {3,S}
10   Cs                         0 {3,S}
11   Cs                         0 {3,S}
12   Cs                         0 {4,S}
13   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (3.6,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    label = "Cs(Cs(CsCsCs)Cs(CsCsCs)Cs(CsCsR)R)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    Cs                         0 {2,S}
9    Cs                         0 {3,S}
10   Cs                         0 {3,S}
11   Cs                         0 {3,S}
12   Cs                         0 {4,S}
13   Cs                         0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (4,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "Cs(Cs(CsCsCs)Cs(CsCsCs)Cs(CsCsCs)R)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    Cs                         0 {2,S}
9    Cs                         0 {3,S}
10   Cs                         0 {3,S}
11   Cs                         0 {3,S}
12   Cs                         0 {4,S}
13   Cs                         0 {4,S}
14   Cs                         0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (4.8,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
    label = "Cs(CsCsCsCs)",
    group = 
"""
1 * Cs 0 {2,S} {3,S} {4,S} {5,S}
2   Cs 0 {1,S}
3   Cs 0 {1,S}
4   Cs 0 {1,S}
5   Cs 0 {1,S}
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

""",
)

entry(
    index = 37,
    label = "Cs(Cs(CsRR)CsCsCs)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    Cs                         0 {1,S} {15,S} {16,S} {17,S}
6    Cs                         0 {2,S}
7    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
8    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
9    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
10   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
12   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
13   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
15   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
16   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
17   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0.8,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "Cs(Cs(CsRR)Cs(CsRR)CsCs)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    Cs                         0 {1,S} {15,S} {16,S} {17,S}
6    Cs                         0 {2,S}
7    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
8    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
9    Cs                         0 {3,S}
10   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
12   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
13   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
15   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
16   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
17   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (1.6,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "Cs(Cs(CsRR)Cs(CsRR)Cs(CsRR)Cs)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    Cs                         0 {1,S} {15,S} {16,S} {17,S}
6    Cs                         0 {2,S}
7    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
8    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
9    Cs                         0 {3,S}
10   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
12   Cs                         0 {4,S}
13   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
15   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
16   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
17   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (2.4,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "Cs(Cs(CsRR)Cs(CsRR)Cs(CsRR)Cs(CsRR))",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    Cs                         0 {1,S} {15,S} {16,S} {17,S}
6    Cs                         0 {2,S}
7    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
8    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
9    Cs                         0 {3,S}
10   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
12   Cs                         0 {4,S}
13   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
15   Cs                         0 {5,S}
16   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
17   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (3.2,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    label = "Cs(Cs(CsCsR)CsCsCs)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    Cs                         0 {1,S} {15,S} {16,S} {17,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
9    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
10   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
12   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
13   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
15   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
16   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
17   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (1.6,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "Cs(Cs(CsCsR)Cs(CsRR)CsCs)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    Cs                         0 {1,S} {15,S} {16,S} {17,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
9    Cs                         0 {3,S}
10   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
12   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
13   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
15   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
16   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
17   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (2.4,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    label = "Cs(Cs(CsCsR)Cs(CsRR)Cs(CsRR)Cs)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    Cs                         0 {1,S} {15,S} {16,S} {17,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
9    Cs                         0 {3,S}
10   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
12   Cs                         0 {4,S}
13   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
15   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
16   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
17   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (3.2,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "Cs(Cs(CsCsR)Cs(CsRR)Cs(CsRR)Cs(CsRR))",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    Cs                         0 {1,S} {15,S} {16,S} {17,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
9    Cs                         0 {3,S}
10   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
12   Cs                         0 {4,S}
13   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
15   Cs                         0 {5,S}
16   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
17   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (4,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    label = "Cs(Cs(CsCsR)Cs(CsCsR)CsCs)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    Cs                         0 {1,S} {15,S} {16,S} {17,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
9    Cs                         0 {3,S}
10   Cs                         0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
12   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
13   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
15   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
16   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
17   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (3.2,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 46,
    label = "Cs(Cs(CsCsR)Cs(CsCsR)Cs(CsRR)Cs)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    Cs                         0 {1,S} {15,S} {16,S} {17,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
9    Cs                         0 {3,S}
10   Cs                         0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
12   Cs                         0 {4,S}
13   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
15   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
16   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
17   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (4,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
    label = "Cs(Cs(CsCsR)Cs(CsCsR)Cs(CsRR)Cs(CsRR))",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    Cs                         0 {1,S} {15,S} {16,S} {17,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
9    Cs                         0 {3,S}
10   Cs                         0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
12   Cs                         0 {4,S}
13   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
15   Cs                         0 {5,S}
16   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
17   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (4.8,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    label = "Cs(Cs(CsCsR)Cs(CsCsR)Cs(CsCsR)Cs)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    Cs                         0 {1,S} {15,S} {16,S} {17,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
9    Cs                         0 {3,S}
10   Cs                         0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
12   Cs                         0 {4,S}
13   Cs                         0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
15   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
16   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
17   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (4.8,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    label = "Cs(Cs(CsCsR)Cs(CsCsR)Cs(CsCsR)Cs(CsRR))",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    Cs                         0 {1,S} {15,S} {16,S} {17,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
9    Cs                         0 {3,S}
10   Cs                         0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
12   Cs                         0 {4,S}
13   Cs                         0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
15   Cs                         0 {5,S}
16   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
17   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (5.6,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 50,
    label = "Cs(Cs(CsCsR)Cs(CsCsR)Cs(CsCsR)Cs(CsCsR))",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    Cs                         0 {1,S} {15,S} {16,S} {17,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
9    Cs                         0 {3,S}
10   Cs                         0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
12   Cs                         0 {4,S}
13   Cs                         0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
15   Cs                         0 {5,S}
16   Cs                         0 {5,S}
17   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (6.4,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
    label = "Cs(Cs(CsCsCs)CsCsCs)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    Cs                         0 {1,S} {15,S} {16,S} {17,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    Cs                         0 {2,S}
9    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
10   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
12   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
13   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
15   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
16   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
17   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (2.4,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
    label = "Cs(Cs(CsCsCs)Cs(CsRR)CsCs)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    Cs                         0 {1,S} {15,S} {16,S} {17,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    Cs                         0 {2,S}
9    Cs                         0 {3,S}
10   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
12   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
13   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
15   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
16   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
17   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (3.2,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 53,
    label = "Cs(Cs(CsCsCs)Cs(CsRR)Cs(CsRR)Cs)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    Cs                         0 {1,S} {15,S} {16,S} {17,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    Cs                         0 {2,S}
9    Cs                         0 {3,S}
10   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
12   Cs                         0 {4,S}
13   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
15   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
16   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
17   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (4,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 54,
    label = "Cs(Cs(CsCsCs)Cs(CsRR)Cs(CsRR)Cs(CsRR))",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    Cs                         0 {1,S} {15,S} {16,S} {17,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    Cs                         0 {2,S}
9    Cs                         0 {3,S}
10   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
12   Cs                         0 {4,S}
13   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
15   Cs                         0 {5,S}
16   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
17   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (4.8,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 55,
    label = "Cs(Cs(CsCsCs)Cs(CsCsR)CsCs)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    Cs                         0 {1,S} {15,S} {16,S} {17,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    Cs                         0 {2,S}
9    Cs                         0 {3,S}
10   Cs                         0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
12   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
13   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
15   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
16   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
17   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (4,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 56,
    label = "Cs(Cs(CsCsCs)Cs(CsCsR)Cs(CsRR)Cs)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    Cs                         0 {1,S} {15,S} {16,S} {17,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    Cs                         0 {2,S}
9    Cs                         0 {3,S}
10   Cs                         0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
12   Cs                         0 {4,S}
13   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
15   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
16   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
17   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (4.8,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 57,
    label = "Cs(Cs(CsCsCs)Cs(CsCsR)Cs(CsRR)Cs(CsRR))",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    Cs                         0 {1,S} {15,S} {16,S} {17,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    Cs                         0 {2,S}
9    Cs                         0 {3,S}
10   Cs                         0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
12   Cs                         0 {4,S}
13   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
15   Cs                         0 {5,S}
16   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
17   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (5.6,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 58,
    label = "Cs(Cs(CsCsCs)Cs(CsCsR)Cs(CsCsR)Cs)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    Cs                         0 {1,S} {15,S} {16,S} {17,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    Cs                         0 {2,S}
9    Cs                         0 {3,S}
10   Cs                         0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
12   Cs                         0 {4,S}
13   Cs                         0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
15   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
16   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
17   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (5.6,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 59,
    label = "Cs(Cs(CsCsCs)Cs(CsCsR)Cs(CsCsR)Cs(CsRR))",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    Cs                         0 {1,S} {15,S} {16,S} {17,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    Cs                         0 {2,S}
9    Cs                         0 {3,S}
10   Cs                         0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
12   Cs                         0 {4,S}
13   Cs                         0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
15   Cs                         0 {5,S}
16   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
17   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (6.4,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 60,
    label = "Cs(Cs(CsCsCs)Cs(CsCsR)Cs(CsCsR)Cs(CsCsR))",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    Cs                         0 {1,S} {15,S} {16,S} {17,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    Cs                         0 {2,S}
9    Cs                         0 {3,S}
10   Cs                         0 {3,S}
11   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
12   Cs                         0 {4,S}
13   Cs                         0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
15   Cs                         0 {5,S}
16   Cs                         0 {5,S}
17   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (7.2,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 61,
    label = "Cs(Cs(CsCsCs)Cs(CsCsCs)CsCs)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    Cs                         0 {1,S} {15,S} {16,S} {17,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    Cs                         0 {2,S}
9    Cs                         0 {3,S}
10   Cs                         0 {3,S}
11   Cs                         0 {3,S}
12   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
13   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
15   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
16   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
17   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (4.8,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 62,
    label = "Cs(Cs(CsCsCs)Cs(CsCsCs)Cs(CsRR)Cs)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    Cs                         0 {1,S} {15,S} {16,S} {17,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    Cs                         0 {2,S}
9    Cs                         0 {3,S}
10   Cs                         0 {3,S}
11   Cs                         0 {3,S}
12   Cs                         0 {4,S}
13   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
15   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
16   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
17   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (5.6,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 63,
    label = "Cs(Cs(CsCsCs)Cs(CsCsCs)Cs(CsRR)Cs(CsRR))",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    Cs                         0 {1,S} {15,S} {16,S} {17,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    Cs                         0 {2,S}
9    Cs                         0 {3,S}
10   Cs                         0 {3,S}
11   Cs                         0 {3,S}
12   Cs                         0 {4,S}
13   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
15   Cs                         0 {5,S}
16   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
17   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (6.4,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 64,
    label = "Cs(Cs(CsCsCs)Cs(CsCsCs)Cs(CsCsR)Cs)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    Cs                         0 {1,S} {15,S} {16,S} {17,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    Cs                         0 {2,S}
9    Cs                         0 {3,S}
10   Cs                         0 {3,S}
11   Cs                         0 {3,S}
12   Cs                         0 {4,S}
13   Cs                         0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
15   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
16   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
17   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (6.4,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 65,
    label = "Cs(Cs(CsCsCs)Cs(CsCsCs)Cs(CsCsR)Cs(CsRR))",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    Cs                         0 {1,S} {15,S} {16,S} {17,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    Cs                         0 {2,S}
9    Cs                         0 {3,S}
10   Cs                         0 {3,S}
11   Cs                         0 {3,S}
12   Cs                         0 {4,S}
13   Cs                         0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
15   Cs                         0 {5,S}
16   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
17   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (7.2,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 66,
    label = "Cs(Cs(CsCsCs)Cs(CsCsCs)Cs(CsCsR)Cs(CsCsR))",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    Cs                         0 {1,S} {15,S} {16,S} {17,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    Cs                         0 {2,S}
9    Cs                         0 {3,S}
10   Cs                         0 {3,S}
11   Cs                         0 {3,S}
12   Cs                         0 {4,S}
13   Cs                         0 {4,S}
14   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
15   Cs                         0 {5,S}
16   Cs                         0 {5,S}
17   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (8,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 67,
    label = "Cs(Cs(CsCsCs)Cs(CsCsCs)Cs(CsCsCs)Cs)",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    Cs                         0 {1,S} {15,S} {16,S} {17,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    Cs                         0 {2,S}
9    Cs                         0 {3,S}
10   Cs                         0 {3,S}
11   Cs                         0 {3,S}
12   Cs                         0 {4,S}
13   Cs                         0 {4,S}
14   Cs                         0 {4,S}
15   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
16   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
17   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (7.2,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 68,
    label = "Cs(Cs(CsCsCs)Cs(CsCsCs)Cs(CsCsCs)Cs(CsRR))",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    Cs                         0 {1,S} {15,S} {16,S} {17,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    Cs                         0 {2,S}
9    Cs                         0 {3,S}
10   Cs                         0 {3,S}
11   Cs                         0 {3,S}
12   Cs                         0 {4,S}
13   Cs                         0 {4,S}
14   Cs                         0 {4,S}
15   Cs                         0 {5,S}
16   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
17   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (8,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 69,
    label = "Cs(Cs(CsCsCs)Cs(CsCsCs)Cs(CsCsCs)Cs(CsCsR))",
    group = 
"""
1  * Cs                         0 {2,S} {3,S} {4,S} {5,S}
2    Cs                         0 {1,S} {6,S} {7,S} {8,S}
3    Cs                         0 {1,S} {9,S} {10,S} {11,S}
4    Cs                         0 {1,S} {12,S} {13,S} {14,S}
5    Cs                         0 {1,S} {15,S} {16,S} {17,S}
6    Cs                         0 {2,S}
7    Cs                         0 {2,S}
8    Cs                         0 {2,S}
9    Cs                         0 {3,S}
10   Cs                         0 {3,S}
11   Cs                         0 {3,S}
12   Cs                         0 {4,S}
13   Cs                         0 {4,S}
14   Cs                         0 {4,S}
15   Cs                         0 {5,S}
16   Cs                         0 {5,S}
17   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (8.8,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 70,
    label = "Cs(Cs(CsCsCs)Cs(CsCsCs)Cs(CsCsCs)Cs(CsCsCs))",
    group = 
"""
1  * Cs 0 {2,S} {3,S} {4,S} {5,S}
2    Cs 0 {1,S} {6,S} {7,S} {8,S}
3    Cs 0 {1,S} {9,S} {10,S} {11,S}
4    Cs 0 {1,S} {12,S} {13,S} {14,S}
5    Cs 0 {1,S} {15,S} {16,S} {17,S}
6    Cs 0 {2,S}
7    Cs 0 {2,S}
8    Cs 0 {2,S}
9    Cs 0 {3,S}
10   Cs 0 {3,S}
11   Cs 0 {3,S}
12   Cs 0 {4,S}
13   Cs 0 {4,S}
14   Cs 0 {4,S}
15   Cs 0 {5,S}
16   Cs 0 {5,S}
17   Cs 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (9.6,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 71,
    label = "Os(RR)",
    group = 
"""
1 * Os 0
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

""",
)

entry(
    index = 72,
    label = "Os(CsR)",
    group = 
"""
1 * Os                         0 {2,S} {3,S}
2   Cs                         0 {1,S}
3   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
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

""",
)

entry(
    index = 73,
    label = "Os(Cs(CsRR)R)",
    group = 
"""
1 * Os                         0 {2,S} {3,S}
2   Cs                         0 {1,S} {4,S} {5,S} {6,S}
3   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
4   Cs                         0 {2,S}
5   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
6   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
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

""",
)

entry(
    index = 74,
    label = "Os(Cs(CsCsR)R)",
    group = 
"""
1 * Os                         0 {2,S} {3,S}
2   Cs                         0 {1,S} {4,S} {5,S} {6,S}
3   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
4   Cs                         0 {2,S}
5   Cs                         0 {2,S}
6   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
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

""",
)

entry(
    index = 75,
    label = "Os(Cs(CsCsCs)R)",
    group = 
"""
1 * Os                         0 {2,S} {3,S}
2   Cs                         0 {1,S} {4,S} {5,S} {6,S}
3   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {1,S}
4   Cs                         0 {2,S}
5   Cs                         0 {2,S}
6   Cs                         0 {2,S}
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

""",
)

entry(
    index = 76,
    label = "Os(CsCs)",
    group = 
"""
1 * Os 0 {2,S} {3,S}
2   Cs 0 {1,S}
3   Cs 0 {1,S}
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

""",
)

entry(
    index = 77,
    label = "Os(Cs(CsRR)Cs)",
    group = 
"""
1 * Os                         0 {2,S} {3,S}
2   Cs                         0 {1,S} {4,S} {5,S} {6,S}
3   Cs                         0 {1,S} {7,S} {8,S} {9,S}
4   Cs                         0 {2,S}
5   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
6   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
7   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
8   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
9   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
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

""",
)

entry(
    index = 78,
    label = "Os(Cs(CsRR)Cs(CsRR))",
    group = 
"""
1 * Os                         0 {2,S} {3,S}
2   Cs                         0 {1,S} {4,S} {5,S} {6,S}
3   Cs                         0 {1,S} {7,S} {8,S} {9,S}
4   Cs                         0 {2,S}
5   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
6   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
7   Cs                         0 {3,S}
8   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
9   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
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

""",
)

entry(
    index = 79,
    label = "Os(Cs(CsCsR)Cs)",
    group = 
"""
1 * Os                         0 {2,S} {3,S}
2   Cs                         0 {1,S} {4,S} {5,S} {6,S}
3   Cs                         0 {1,S} {7,S} {8,S} {9,S}
4   Cs                         0 {2,S}
5   Cs                         0 {2,S}
6   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
7   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
8   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
9   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0.5,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 80,
    label = "Os(Cs(CsCsR)Cs(CsRR))",
    group = 
"""
1 * Os                         0 {2,S} {3,S}
2   Cs                         0 {1,S} {4,S} {5,S} {6,S}
3   Cs                         0 {1,S} {7,S} {8,S} {9,S}
4   Cs                         0 {2,S}
5   Cs                         0 {2,S}
6   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
7   Cs                         0 {3,S}
8   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
9   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0.5,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 81,
    label = "Os(Cs(CsCsR)Cs(CsCsR))",
    group = 
"""
1 * Os                         0 {2,S} {3,S}
2   Cs                         0 {1,S} {4,S} {5,S} {6,S}
3   Cs                         0 {1,S} {7,S} {8,S} {9,S}
4   Cs                         0 {2,S}
5   Cs                         0 {2,S}
6   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {2,S}
7   Cs                         0 {3,S}
8   Cs                         0 {3,S}
9   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (1,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 82,
    label = "Os(Cs(CsCsCs)Cs)",
    group = 
"""
1 * Os                         0 {2,S} {3,S}
2   Cs                         0 {1,S} {4,S} {5,S} {6,S}
3   Cs                         0 {1,S} {7,S} {8,S} {9,S}
4   Cs                         0 {2,S}
5   Cs                         0 {2,S}
6   Cs                         0 {2,S}
7   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
8   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
9   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (1,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 83,
    label = "Os(Cs(CsCsCs)Cs(CsRR))",
    group = 
"""
1 * Os                         0 {2,S} {3,S}
2   Cs                         0 {1,S} {4,S} {5,S} {6,S}
3   Cs                         0 {1,S} {7,S} {8,S} {9,S}
4   Cs                         0 {2,S}
5   Cs                         0 {2,S}
6   Cs                         0 {2,S}
7   Cs                         0 {3,S}
8   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
9   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (1,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 84,
    label = "Os(Cs(CsCsCs)Cs(CsCsR))",
    group = 
"""
1 * Os                         0 {2,S} {3,S}
2   Cs                         0 {1,S} {4,S} {5,S} {6,S}
3   Cs                         0 {1,S} {7,S} {8,S} {9,S}
4   Cs                         0 {2,S}
5   Cs                         0 {2,S}
6   Cs                         0 {2,S}
7   Cs                         0 {3,S}
8   Cs                         0 {3,S}
9   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (1.5,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 85,
    label = "Os(Cs(CsCsCs)Cs(CsCsCs))",
    group = 
"""
1 * Os 0 {2,S} {3,S}
2   Cs 0 {1,S} {4,S} {5,S} {6,S}
3   Cs 0 {1,S} {7,S} {8,S} {9,S}
4   Cs 0 {2,S}
5   Cs 0 {2,S}
6   Cs 0 {2,S}
7   Cs 0 {3,S}
8   Cs 0 {3,S}
9   Cs 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (2,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 86,
    label = "Cd(CsCs)",
    group = 
"""
1 * Cd 0 {2,D} {3,S} {4,S}
2   Cd 0 {1,D}
3   Cs 0 {1,S}
4   Cs 0 {1,S}
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

""",
)

entry(
    index = 87,
    label = "Cd(Cs(CsRR)Cs)",
    group = 
"""
1  * Cd                         0 {2,D} {3,S} {4,S}
2    Cd                         0 {1,D}
3    Cs                         0 {1,S} {5,S} {6,S} {7,S}
4    Cs                         0 {1,S} {8,S} {9,S} {10,S}
5    Cs                         0 {3,S}
6    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
7    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
8    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
9    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
10   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
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

""",
)

entry(
    index = 88,
    label = "Cd(Cs(CsRR)Cs(CsRR))",
    group = 
"""
1  * Cd                         0 {2,D} {3,S} {4,S}
2    Cd                         0 {1,D}
3    Cs                         0 {1,S} {5,S} {6,S} {7,S}
4    Cs                         0 {1,S} {8,S} {9,S} {10,S}
5    Cs                         0 {3,S}
6    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
7    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
8    Cs                         0 {4,S}
9    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
10   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
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

""",
)

entry(
    index = 89,
    label = "Cd(Cs(CsCsR)Cs)",
    group = 
"""
1  * Cd                         0 {2,D} {3,S} {4,S}
2    Cd                         0 {1,D}
3    Cs                         0 {1,S} {5,S} {6,S} {7,S}
4    Cs                         0 {1,S} {8,S} {9,S} {10,S}
5    Cs                         0 {3,S}
6    Cs                         0 {3,S}
7    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
8    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
9    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
10   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (1,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 90,
    label = "Cd(Cs(CsCsR)Cs(CsRR))",
    group = 
"""
1  * Cd                         0 {2,D} {3,S} {4,S}
2    Cd                         0 {1,D}
3    Cs                         0 {1,S} {5,S} {6,S} {7,S}
4    Cs                         0 {1,S} {8,S} {9,S} {10,S}
5    Cs                         0 {3,S}
6    Cs                         0 {3,S}
7    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
8    Cs                         0 {4,S}
9    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
10   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (1,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 91,
    label = "Cd(Cs(CsCsR)Cs(CsCsR))",
    group = 
"""
1  * Cd                         0 {2,D} {3,S} {4,S}
2    Cd                         0 {1,D}
3    Cs                         0 {1,S} {5,S} {6,S} {7,S}
4    Cs                         0 {1,S} {8,S} {9,S} {10,S}
5    Cs                         0 {3,S}
6    Cs                         0 {3,S}
7    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {3,S}
8    Cs                         0 {4,S}
9    Cs                         0 {4,S}
10   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (2,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 92,
    label = "Cd(Cs(CsCsCs)Cs)",
    group = 
"""
1  * Cd                         0 {2,D} {3,S} {4,S}
2    Cd                         0 {1,D}
3    Cs                         0 {1,S} {5,S} {6,S} {7,S}
4    Cs                         0 {1,S} {8,S} {9,S} {10,S}
5    Cs                         0 {3,S}
6    Cs                         0 {3,S}
7    Cs                         0 {3,S}
8    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
9    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
10   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (1,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 93,
    label = "Cd(Cs(CsCsCs)Cs(CsRR))",
    group = 
"""
1  * Cd                         0 {2,D} {3,S} {4,S}
2    Cd                         0 {1,D}
3    Cs                         0 {1,S} {5,S} {6,S} {7,S}
4    Cs                         0 {1,S} {8,S} {9,S} {10,S}
5    Cs                         0 {3,S}
6    Cs                         0 {3,S}
7    Cs                         0 {3,S}
8    Cs                         0 {4,S}
9    {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
10   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (1,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 94,
    label = "Cd(Cs(CsCsCs)Cs(CsCsR))",
    group = 
"""
1  * Cd                         0 {2,D} {3,S} {4,S}
2    Cd                         0 {1,D}
3    Cs                         0 {1,S} {5,S} {6,S} {7,S}
4    Cs                         0 {1,S} {8,S} {9,S} {10,S}
5    Cs                         0 {3,S}
6    Cs                         0 {3,S}
7    Cs                         0 {3,S}
8    Cs                         0 {4,S}
9    Cs                         0 {4,S}
10   {Cd,Cdd,Ct,Cb,Cbf,Os,CO,H} 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (2,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 95,
    label = "Cd(Cs(CsCsCs)Cs(CsCsCs))",
    group = 
"""
1  * Cd 0 {2,D} {3,S} {4,S}
2    Cd 0 {1,D}
3    Cs 0 {1,S} {5,S} {6,S} {7,S}
4    Cs 0 {1,S} {8,S} {9,S} {10,S}
5    Cs 0 {3,S}
6    Cs 0 {3,S}
7    Cs 0 {3,S}
8    Cs 0 {4,S}
9    Cs 0 {4,S}
10   Cs 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (2,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

tree(
"""
L1: CsOsCd
    L2: Cs(RRRR)
        L3: Cs(CsRRR)
            L4: Cs(Cs(CsRR)RRR)
            L4: Cs(Cs(CsCsR)RRR)
            L4: Cs(Cs(CsCsCs)RRR)
        L3: Cs(CsCsRR)
            L4: Cs(Cs(CsRR)CsRR)
            L4: Cs(Cs(CsRR)Cs(CsRR)RR)
            L4: Cs(Cs(CsCsR)CsRR)
            L4: Cs(Cs(CsCsR)Cs(CsRR)RR)
            L4: Cs(Cs(CsCsR)Cs(CsCsR)RR)
            L4: Cs(Cs(CsCsCs)CsRR)
            L4: Cs(Cs(CsCsCs)Cs(CsRR)RR)
            L4: Cs(Cs(CsCsCs)Cs(CsCsR)RR)
            L4: Cs(Cs(CsCsCs)Cs(CsCsCs)RR)
        L3: Cs(CsCsCsR)
            L4: Cs(Cs(CsRR)CsCsR)
            L4: Cs(Cs(CsRR)Cs(CsRR)CsR)
            L4: Cs(Cs(CsRR)Cs(CsRR)Cs(CsRR)R)
            L4: Cs(Cs(CsCsR)CsCsR)
            L4: Cs(Cs(CsCsR)Cs(CsRR)CsR)
            L4: Cs(Cs(CsCsR)Cs(CsRR)Cs(CsRR)R)
            L4: Cs(Cs(CsCsR)Cs(CsCsR)CsR)
            L4: Cs(Cs(CsCsR)Cs(CsCsR)Cs(CsRR)R)
            L4: Cs(Cs(CsCsR)Cs(CsCsR)Cs(CsCsR)R)
            L4: Cs(Cs(CsCsCs)CsCsR)
            L4: Cs(Cs(CsCsCs)Cs(CsRR)CsR)
            L4: Cs(Cs(CsCsCs)Cs(CsRR)Cs(CsRR)R)
            L4: Cs(Cs(CsCsCs)Cs(CsCsR)CsR)
            L4: Cs(Cs(CsCsCs)Cs(CsCsR)Cs(CsRR)R)
            L4: Cs(Cs(CsCsCs)Cs(CsCsR)Cs(CsCsR)R)
            L4: Cs(Cs(CsCsCs)Cs(CsCsCs)CsR)
            L4: Cs(Cs(CsCsCs)Cs(CsCsCs)Cs(CsRR)R)
            L4: Cs(Cs(CsCsCs)Cs(CsCsCs)Cs(CsCsR)R)
            L4: Cs(Cs(CsCsCs)Cs(CsCsCs)Cs(CsCsCs)R)
        L3: Cs(CsCsCsCs)
            L4: Cs(Cs(CsRR)CsCsCs)
            L4: Cs(Cs(CsRR)Cs(CsRR)CsCs)
            L4: Cs(Cs(CsRR)Cs(CsRR)Cs(CsRR)Cs)
            L4: Cs(Cs(CsRR)Cs(CsRR)Cs(CsRR)Cs(CsRR))
            L4: Cs(Cs(CsCsR)CsCsCs)
            L4: Cs(Cs(CsCsR)Cs(CsRR)CsCs)
            L4: Cs(Cs(CsCsR)Cs(CsRR)Cs(CsRR)Cs)
            L4: Cs(Cs(CsCsR)Cs(CsRR)Cs(CsRR)Cs(CsRR))
            L4: Cs(Cs(CsCsR)Cs(CsCsR)CsCs)
            L4: Cs(Cs(CsCsR)Cs(CsCsR)Cs(CsRR)Cs)
            L4: Cs(Cs(CsCsR)Cs(CsCsR)Cs(CsRR)Cs(CsRR))
            L4: Cs(Cs(CsCsR)Cs(CsCsR)Cs(CsCsR)Cs)
            L4: Cs(Cs(CsCsR)Cs(CsCsR)Cs(CsCsR)Cs(CsRR))
            L4: Cs(Cs(CsCsR)Cs(CsCsR)Cs(CsCsR)Cs(CsCsR))
            L4: Cs(Cs(CsCsCs)CsCsCs)
            L4: Cs(Cs(CsCsCs)Cs(CsRR)CsCs)
            L4: Cs(Cs(CsCsCs)Cs(CsRR)Cs(CsRR)Cs)
            L4: Cs(Cs(CsCsCs)Cs(CsRR)Cs(CsRR)Cs(CsRR))
            L4: Cs(Cs(CsCsCs)Cs(CsCsR)CsCs)
            L4: Cs(Cs(CsCsCs)Cs(CsCsR)Cs(CsRR)Cs)
            L4: Cs(Cs(CsCsCs)Cs(CsCsR)Cs(CsRR)Cs(CsRR))
            L4: Cs(Cs(CsCsCs)Cs(CsCsR)Cs(CsCsR)Cs)
            L4: Cs(Cs(CsCsCs)Cs(CsCsR)Cs(CsCsR)Cs(CsRR))
            L4: Cs(Cs(CsCsCs)Cs(CsCsR)Cs(CsCsR)Cs(CsCsR))
            L4: Cs(Cs(CsCsCs)Cs(CsCsCs)CsCs)
            L4: Cs(Cs(CsCsCs)Cs(CsCsCs)Cs(CsRR)Cs)
            L4: Cs(Cs(CsCsCs)Cs(CsCsCs)Cs(CsRR)Cs(CsRR))
            L4: Cs(Cs(CsCsCs)Cs(CsCsCs)Cs(CsCsR)Cs)
            L4: Cs(Cs(CsCsCs)Cs(CsCsCs)Cs(CsCsR)Cs(CsRR))
            L4: Cs(Cs(CsCsCs)Cs(CsCsCs)Cs(CsCsR)Cs(CsCsR))
            L4: Cs(Cs(CsCsCs)Cs(CsCsCs)Cs(CsCsCs)Cs)
            L4: Cs(Cs(CsCsCs)Cs(CsCsCs)Cs(CsCsCs)Cs(CsRR))
            L4: Cs(Cs(CsCsCs)Cs(CsCsCs)Cs(CsCsCs)Cs(CsCsR))
            L4: Cs(Cs(CsCsCs)Cs(CsCsCs)Cs(CsCsCs)Cs(CsCsCs))
    L2: Os(RR)
        L3: Os(CsR)
            L4: Os(Cs(CsRR)R)
            L4: Os(Cs(CsCsR)R)
            L4: Os(Cs(CsCsCs)R)
        L3: Os(CsCs)
            L4: Os(Cs(CsRR)Cs)
            L4: Os(Cs(CsRR)Cs(CsRR))
            L4: Os(Cs(CsCsR)Cs)
            L4: Os(Cs(CsCsR)Cs(CsRR))
            L4: Os(Cs(CsCsR)Cs(CsCsR))
            L4: Os(Cs(CsCsCs)Cs)
            L4: Os(Cs(CsCsCs)Cs(CsRR))
            L4: Os(Cs(CsCsCs)Cs(CsCsR))
            L4: Os(Cs(CsCsCs)Cs(CsCsCs))
    L2: Cd(CsCs)
        L3: Cd(Cs(CsRR)Cs)
        L3: Cd(Cs(CsRR)Cs(CsRR))
        L3: Cd(Cs(CsCsR)Cs)
        L3: Cd(Cs(CsCsR)Cs(CsRR))
        L3: Cd(Cs(CsCsR)Cs(CsCsR))
        L3: Cd(Cs(CsCsCs)Cs)
        L3: Cd(Cs(CsCsCs)Cs(CsRR))
        L3: Cd(Cs(CsCsCs)Cs(CsCsR))
        L3: Cd(Cs(CsCsCs)Cs(CsCsCs))
"""
)

