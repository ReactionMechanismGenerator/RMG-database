#!/usr/bin/env python
# encoding: utf-8

name = "Other Corrections"
shortDesc = ""
longDesc = """

"""
entry(
    index = 0,
    label = "R",
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
    shortDesc = """dummy root""",
    longDesc = 
"""

""",
)

entry(
    index = 1,
    label = "ketene",
    group = 
"""
1 * C u0 {2,D} {3,S} {4,S}
2   C u0 {1,D} {5,D}
3   R u0 {1,S}
4   R u0 {1,S}
5   O u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """All the corrections from this family are from Sumathi & Green, J. Phys. Chem. A, 2002, 106, 7937-7949""",
    longDesc = 
"""

""",
)

entry(
    index = 2,
    label = "ketene_2C-C",
    group = 
"""
1 * C       u0 {2,D} {3,S} {4,S}
2   C       u0 {1,D} {5,D}
3   [Cs,Cd] u0 {1,S} {6,S}
4   [Cs,Cd] u0 {1,S} {7,S}
5   O       u0 {2,D}
6   C       u0 {3,S}
7   C       u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (-1.6,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """This is correction NN2 from Sumathi & Green, J. Phys. Chem. A, 2002, 106, 7937-7949""",
    longDesc = 
"""

""",
)

entry(
    index = 3,
    label = "ketene_1C-C_1C-H",
    group = 
"""
1 * C       u0 {2,D} {3,S} {4,S}
2   C       u0 {1,D} {5,D}
3   [Cs,Cd] u0 {1,S} {6,S}
4   C       u0 {1,S} {7,S} {8,S} {9,S}
5   O       u0 {2,D}
6   C       u0 {3,S}
7   H       u0 {4,S}
8   H       u0 {4,S}
9   H       u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (-0.5,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """This is correction NN1 from Sumathi & Green, J. Phys. Chem. A, 2002, 106, 7937-7949""",
    longDesc = 
"""

""",
)

entry(
    index = 4,
    label = "biketene",
    group = 
"""
1    C   u0 {2,S} {3,S} {4,S} {5,S}
2    C   u0 {1,S} {6,D}
3  * C   u0 {1,S} {7,D} {10,S}
4    R!H u0 {1,S}
5    R!H u0 {1,S}
6    C   u0 {2,D} {8,D}
7    C   u0 {3,D} {9,D}
8    O   u0 {6,D}
9    O   u0 {7,D}
10   R   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (-0.9,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """This is correction NN3 from Sumathi & Green, J. Phys. Chem. A, 2002, 106, 7937-7949""",
    longDesc = 
"""

""",
)

entry(
    index = 5,
    label = "ketene_2C-H",
    group = 
"""
1  * C u0 {2,D} {3,S} {4,S}
2    C u0 {1,D} {5,D}
3    C u0 {1,S} {6,S} {7,S} {8,S}
4    C u0 {1,S} {9,S} {10,S} {11,S}
5    O u0 {2,D}
6    H u0 {3,S}
7    H u0 {3,S}
8    H u0 {3,S}
9    H u0 {4,S}
10   H u0 {4,S}
11   H u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """This is correction NN0 from Sumathi & Green, J. Phys. Chem. A, 2002, 106, 7937-7949""",
    longDesc = 
"""

""",
)

entry(
    index = 6,
    label = "ThreeMember-Val7",
    group = 
"""
1 * R!H  u0 {2,[S,D]} {3,S} {4,S}
2   R!H  u0 {1,[S,D]} {3,[S,D]}
3   R!H  u0 {1,S} {2,[S,D]}
4   Val7 u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78146,-0.885078,-0.939453,-0.933319,-0.787376,-0.563773,-0.414499],'cal/(mol*K)','+|-',[0.0580655,0.0609285,0.0702088,0.0721244,0.0619547,0.0535603,0.112046]),
        H298 = (2.80367,'kcal/mol','+|-',3.33658),
        S298 = (1.822,'cal/(mol*K)','+|-',1.0015),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 7,
    label = "ThreeMember-F",
    group = 
"""
1 * R!H u0 {2,[S,D]} {3,S} {4,S}
2   R!H u0 {1,[S,D]} {3,[S,D]}
3   R!H u0 {1,S} {2,[S,D]}
4   F1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.86579,-0.850107,-0.803115,-0.724983,-0.506891,-0.262168,-0.142953],'cal/(mol*K)','+|-',[0.0580655,0.0609285,0.0702088,0.0721244,0.0619547,0.0535603,0.112046]),
        H298 = (4.72584,'kcal/mol','+|-',0.31926),
        S298 = (1.31408,'cal/(mol*K)','+|-',0.175644),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library         | Number of Species
library:CHOF_G4 |         142
""",
)

entry(
    index = 8,
    label = "ThreeMember-F2",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {4,S} {5,S}
2   R!H u0 {1,S} {3,[S,D]}
3   R!H u0 {1,S} {2,[S,D]}
4   F1s u0 {1,S}
5   F1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.25141,-1.10602,-0.998775,-0.969281,-0.641556,-0.284231,-0.477653],'cal/(mol*K)','+|-',[0.177999,0.186775,0.215224,0.221096,0.189921,0.164188,0.343477]),
        H298 = (7.41421,'kcal/mol','+|-',0.978687),
        S298 = (2.87195,'cal/(mol*K)','+|-',0.538432),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library         | Number of Species
library:CHOF_G4 |         67
""",
)

entry(
    index = 9,
    label = "ThreeMember-Cl",
    group = 
"""
1 * R!H  u0 {2,[S,D]} {3,S} {4,S}
2   R!H  u0 {1,[S,D]} {3,[S,D]}
3   R!H  u0 {1,S} {2,[S,D]}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.705382,-0.859737,-0.950073,-0.972614,-0.859689,-0.646368,-0.479236],'cal/(mol*K)','+|-',[0.0589861,0.0618945,0.0713219,0.0732679,0.062937,0.0544094,0.113823]),
        H298 = (1.95271,'kcal/mol','+|-',0.324322),
        S298 = (1.83665,'cal/(mol*K)','+|-',0.178428),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library          | Number of Species
library:CHOCl_G4 |         133
""",
)

entry(
    index = 10,
    label = "ThreeMember-Cl2",
    group = 
"""
1 * R!H  u0 {2,S} {3,S} {4,S} {5,S}
2   R!H  u0 {1,S} {3,[S,D]}
3   R!H  u0 {1,S} {2,[S,D]}
4   Cl1s u0 {1,S}
5   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.33592,-1.42883,-1.6255,-1.71524,-1.41342,-1.04232,-1.09548],'cal/(mol*K)','+|-',[0.193025,0.202542,0.233392,0.23976,0.205954,0.178048,0.372472]),
        H298 = (2.41127,'kcal/mol','+|-',1.0613),
        S298 = (4.35706,'cal/(mol*K)','+|-',0.583885),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library          | Number of Species
library:CHOCl_G4 |         60
""",
)

entry(
    index = 11,
    label = "ThreeMember-Br",
    group = 
"""
1 * R!H  u0 {2,[S,D]} {3,S} {4,S}
2   R!H  u0 {1,[S,D]} {3,[S,D]}
3   R!H  u0 {1,S} {2,[S,D]}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.773208,-0.94539,-1.06517,-1.10236,-0.995548,-0.782784,-0.621308],'cal/(mol*K)','+|-',[0.0605086,0.0634921,0.0731628,0.075159,0.0645614,0.0558138,0.116761]),
        H298 = (1.73245,'kcal/mol','+|-',0.332693),
        S298 = (2.31526,'cal/(mol*K)','+|-',0.183034),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library          | Number of Species
library:CHOBr_G4 |         125
""",
)

entry(
    index = 12,
    label = "ThreeMember-Br2",
    group = 
"""
1 * R!H  u0 {2,S} {3,S} {4,S} {5,S}
2   R!H  u0 {1,S} {3,[S,D]}
3   R!H  u0 {1,S} {2,[S,D]}
4   Br1s u0 {1,S}
5   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.19793,-1.45646,-1.74957,-1.82557,-1.52434,-1.1999,-1.43018],'cal/(mol*K)','+|-',[0.205946,0.2161,0.249015,0.25581,0.21974,0.189967,0.397404]),
        H298 = (2.17974,'kcal/mol','+|-',1.13235),
        S298 = (4.96142,'cal/(mol*K)','+|-',0.62297),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library          | Number of Species
library:CHOBr_G4 |         55
""",
)

entry(
    index = 13,
    label = "ThreeMember-CdVal7",
    group = 
"""
1 * R!H  u0 {2,S} {3,S} {4,D}
2   R!H  u0 {1,S} {3,S}
3   R!H  u0 {1,S} {2,S}
4   C    u0 {1,D} {5,S}
5   Val7 u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.00195667,-0.255638,-0.297799,-0.274036,-0.198539,0.0268909,0.604749],'cal/(mol*K)','+|-',[0.323068,0.338997,0.390631,0.40129,0.344707,0.298001,0.62341]),
        H298 = (1.97788,'kcal/mol','+|-',2.60504),
        S298 = (3.10832,'cal/(mol*K)','+|-',0.723557),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 14,
    label = "ThreeMember-CdF",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {4,D}
2   R!H u0 {1,S} {3,S}
3   R!H u0 {1,S} {2,S}
4   C   u0 {1,D} {5,S}
5   F   u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.022716,-0.305765,-0.364063,-0.33675,-0.257481,-0.0460683,0.55639],'cal/(mol*K)','+|-',[0.323068,0.338997,0.390631,0.40129,0.344707,0.298001,0.62341]),
        H298 = (3.02346,'kcal/mol','+|-',1.77632),
        S298 = (3.20911,'cal/(mol*K)','+|-',0.977255),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library         | Number of Species
library:CHOF_G4 |         10
""",
)

entry(
    index = 15,
    label = "ThreeMember-CdF2",
    group = 
"""
1 * R!H u0 {2,D} {3,S} {4,S}
2   C   u0 {1,D} {5,S} {6,S}
3   R!H u0 {1,S} {4,S}
4   R!H u0 {1,S} {3,S}
5   F   u0 {2,S}
6   F   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.345459,0.00240052,-0.106856,-0.103819,-0.114526,0.032674,0.604743],'cal/(mol*K)','+|-',[0.33839,0.355074,0.409157,0.420321,0.361055,0.312134,0.652975]),
        H298 = (5.17501,'kcal/mol','+|-',1.86056),
        S298 = (4.30409,'cal/(mol*K)','+|-',1.0236),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library         | Number of Species
library:CHOF_G4 |         9
""",
)

entry(
    index = 16,
    label = "ThreeMember-CdCl",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {4,D}
2   R!H u0 {1,S} {3,S}
3   R!H u0 {1,S} {2,S}
4   C   u0 {1,D} {5,S}
5   Cl  u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0215411,-0.0836937,-0.0375076,-0.0142938,0.00428104,0.14122,0.675329],'cal/(mol*K)','+|-',[0.3387,0.3554,0.409533,0.420707,0.361386,0.312421,0.653575]),
        H298 = (0.518802,'kcal/mol','+|-',1.86227),
        S298 = (2.70683,'cal/(mol*K)','+|-',1.02454),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library          | Number of Species
library:CHOCl_G4 |         9
""",
)

entry(
    index = 17,
    label = "ThreeMember-CdCl2",
    group = 
"""
1 * R!H u0 {2,D} {3,S} {4,S}
2   C   u0 {1,D} {5,S} {6,S}
3   R!H u0 {1,S} {4,S}
4   R!H u0 {1,S} {3,S}
5   Cl  u0 {2,S}
6   Cl  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.848086,0.435201,0.180933,0.102383,-0.0172815,0.0869509,0.435387],'cal/(mol*K)','+|-',[0.383057,0.401944,0.463166,0.475803,0.408713,0.353335,0.739167]),
        H298 = (1.24675,'kcal/mol','+|-',2.10615),
        S298 = (3.43067,'cal/(mol*K)','+|-',1.15872),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library          | Number of Species
library:CHOCl_G4 |         7
""",
)

entry(
    index = 18,
    label = "ThreeMember-CdBr",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {4,D}
2   R!H u0 {1,S} {3,S}
3   R!H u0 {1,S} {2,S}
4   C   u0 {1,D} {5,S}
5   Br  u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0383871,-0.377454,-0.491825,-0.471063,-0.342417,-0.0144789,0.582528],'cal/(mol*K)','+|-',[0.358919,0.376616,0.433981,0.445821,0.38296,0.331071,0.69259]),
        H298 = (2.39137,'kcal/mol','+|-',1.97344),
        S298 = (3.40901,'cal/(mol*K)','+|-',1.0857),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library          | Number of Species
library:CHOBr_G4 |         8
""",
)

entry(
    index = 19,
    label = "ThreeMember-CdBr2",
    group = 
"""
1 * R!H u0 {2,D} {3,S} {4,S}
2   C   u0 {1,D} {5,S} {6,S}
3   R!H u0 {1,S} {4,S}
4   R!H u0 {1,S} {3,S}
5   Br  u0 {2,S}
6   Br  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.667834,0.280434,0.103722,0.135757,0.083518,0.225796,0.611691],'cal/(mol*K)','+|-',[0.414775,0.435226,0.501518,0.515201,0.442557,0.382593,0.800373]),
        H298 = (0.267743,'kcal/mol','+|-',2.28055),
        S298 = (3.12234,'cal/(mol*K)','+|-',1.25466),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library          | Number of Species
library:CHOBr_G4 |         6
""",
)

entry(
    index = 20,
    label = "ThreeMember-CVal7",
    group = 
"""
1 * R!H  u0 {2,[S,D]} {3,S} {4,S}
2   R!H  u0 {1,[S,D]} {3,S}
3   R!H  u0 {1,S} {2,S}
4   C    u0 {1,S} {5,S}
5   Val7 u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.10507,-1.24873,-1.19204,-0.977486,-0.60092,-0.305864,-0.104514],'cal/(mol*K)','+|-',[0.258123,0.27085,0.312105,0.320621,0.275412,0.238096,0.498089]),
        H298 = (-0.5401,'kcal/mol','+|-',0.915302),
        S298 = (1.80846,'cal/(mol*K)','+|-',0.141277),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 21,
    label = "ThreeMember-CF",
    group = 
"""
1 * R!H u0 {2,[S,D]} {3,S} {4,S}
2   R!H u0 {1,[S,D]} {3,S}
3   R!H u0 {1,S} {2,S}
4   C   u0 {1,S} {5,S}
5   F   u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.04902,-1.20103,-1.1361,-0.880379,-0.475989,-0.206761,-0.0233559],'cal/(mol*K)','+|-',[0.258123,0.27085,0.312105,0.320621,0.275412,0.238096,0.498089]),
        H298 = (-0.0735936,'kcal/mol','+|-',1.41923),
        S298 = (1.79496,'cal/(mol*K)','+|-',0.780802),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library         | Number of Species
library:CHOF_G4 |         16
""",
)

entry(
    index = 22,
    label = "ThreeMember-CF2",
    group = 
"""
1 * R!H u0 {2,S} {3,[S,D]} {4,S}
2   C   u0 {1,S} {5,S} {6,S}
3   R!H u0 {1,[S,D]} {4,S}
4   R!H u0 {1,S} {3,S}
5   F   u0 {2,S}
6   F   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.24429,-1.38002,-1.25062,-0.964808,-0.590301,-0.31222,-0.170333],'cal/(mol*K)','+|-',[0.264366,0.277401,0.319653,0.328374,0.282073,0.243854,0.510135]),
        H298 = (2.20085,'kcal/mol','+|-',1.45356),
        S298 = (1.47084,'cal/(mol*K)','+|-',0.799685),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library         | Number of Species
library:CHOF_G4 |         15
""",
)

entry(
    index = 23,
    label = "ThreeMember-CF3",
    group = 
"""
1   C   u0 {2,S} {5,S} {6,S} {7,S}
2 * R!H u0 {1,S} {3,[S,D]} {4,S}
3   R!H u0 {2,[S,D]} {4,S}
4   R!H u0 {2,S} {3,S}
5   F   u0 {1,S}
6   F   u0 {1,S}
7   F   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.419572,-0.281444,-0.15824,-0.0473225,0.0996705,0.29577,0.0148071],'cal/(mol*K)','+|-',[0.272337,0.285764,0.329291,0.338275,0.290578,0.251206,0.525516]),
        H298 = (3.02752,'kcal/mol','+|-',1.49738),
        S298 = (1.95951,'cal/(mol*K)','+|-',0.823797),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library         | Number of Species
library:CHOF_G4 |         14
""",
)

entry(
    index = 24,
    label = "ThreeMember-CCl",
    group = 
"""
1 * R!H u0 {2,[S,D]} {3,S} {4,S}
2   R!H u0 {1,[S,D]} {3,S}
3   R!H u0 {1,S} {2,S}
4   C   u0 {1,S} {5,S}
5   Cl  u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.12505,-1.23725,-1.16093,-0.963398,-0.637799,-0.334364,-0.102508],'cal/(mol*K)','+|-',[0.293113,0.307565,0.354411,0.364081,0.312745,0.27037,0.565606]),
        H298 = (-0.558357,'kcal/mol','+|-',1.61161),
        S298 = (1.88487,'cal/(mol*K)','+|-',0.886642),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library          | Number of Species
library:CHOCl_G4 |         12
""",
)

entry(
    index = 25,
    label = "ThreeMember-CCl2",
    group = 
"""
1 * R!H u0 {2,S} {3,[S,D]} {4,S}
2   C   u0 {1,S} {5,S} {6,S}
3   R!H u0 {1,[S,D]} {4,S}
4   R!H u0 {1,S} {3,S}
5   Cl  u0 {2,S}
6   Cl  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.793992,-0.879415,-0.864124,-0.81897,-0.722568,-0.485267,-0.258727],'cal/(mol*K)','+|-',[0.266016,0.279132,0.321648,0.330424,0.283833,0.245376,0.513319]),
        H298 = (-0.458055,'kcal/mol','+|-',1.46263),
        S298 = (1.75866,'cal/(mol*K)','+|-',0.804676),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library          | Number of Species
library:CHOCl_G4 |         15
""",
)

entry(
    index = 26,
    label = "ThreeMember-CCl3",
    group = 
"""
1   C   u0 {2,S} {5,S} {6,S} {7,S}
2 * R!H u0 {1,S} {3,[S,D]} {4,S}
3   R!H u0 {2,[S,D]} {4,S}
4   R!H u0 {2,S} {3,S}
5   Cl  u0 {1,S}
6   Cl  u0 {1,S}
7   Cl  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.140917,0.108082,-0.131251,-0.201776,-0.160737,-0.0772849,-0.58716],'cal/(mol*K)','+|-',[0.295026,0.309572,0.356725,0.366458,0.314786,0.272135,0.569298]),
        H298 = (0.0727587,'kcal/mol','+|-',1.62213),
        S298 = (2.16962,'cal/(mol*K)','+|-',0.892429),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library          | Number of Species
library:CHOCl_G4 |         12
""",
)

entry(
    index = 27,
    label = "ThreeMember-CBr",
    group = 
"""
1 * R!H u0 {2,[S,D]} {3,S} {4,S}
2   R!H u0 {1,[S,D]} {3,S}
3   R!H u0 {1,S} {2,S}
4   C   u0 {1,S} {5,S}
5   Br  u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.14114,-1.30791,-1.27908,-1.08868,-0.688973,-0.376466,-0.187677],'cal/(mol*K)','+|-',[0.28324,0.297205,0.342474,0.351818,0.302211,0.261263,0.546555]),
        H298 = (-0.988349,'kcal/mol','+|-',1.55733),
        S298 = (1.74554,'cal/(mol*K)','+|-',0.856777),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library          | Number of Species
library:CHOBr_G4 |         13
""",
)

entry(
    index = 28,
    label = "ThreeMember-CBr2",
    group = 
"""
1 * R!H u0 {2,S} {3,[S,D]} {4,S}
2   C   u0 {1,S} {5,S} {6,S}
3   R!H u0 {1,[S,D]} {4,S}
4   R!H u0 {1,S} {3,S}
5   Br  u0 {2,S}
6   Br  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.904345,-1.18948,-1.34606,-1.29421,-0.977039,-0.663189,-0.688732],'cal/(mol*K)','+|-',[0.295073,0.309622,0.356782,0.366516,0.314836,0.272178,0.569389]),
        H298 = (-0.760935,'kcal/mol','+|-',1.62239),
        S298 = (1.83493,'cal/(mol*K)','+|-',0.892571),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library          | Number of Species
library:CHOBr_G4 |         12
""",
)

entry(
    index = 29,
    label = "ThreeMember-CBr3",
    group = 
"""
1   C   u0 {2,S} {5,S} {6,S} {7,S}
2 * R!H u0 {1,S} {3,[S,D]} {4,S}
3   R!H u0 {2,[S,D]} {4,S}
4   R!H u0 {2,S} {3,S}
5   Br  u0 {1,S}
6   Br  u0 {1,S}
7   Br  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0988102,0.020235,-0.112809,-0.112424,-0.00180092,0.126823,-0.192086],'cal/(mol*K)','+|-',[0.28431,0.298328,0.343768,0.353147,0.303353,0.26225,0.54862]),
        H298 = (-0.724246,'kcal/mol','+|-',1.56321),
        S298 = (2.30485,'cal/(mol*K)','+|-',0.860014),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library          | Number of Species
library:CHOBr_G4 |         13
""",
)

entry(
    index = 30,
    label = "FourMember-Val7",
    group = 
"""
1 * R!H  u0 {2,[S,D]} {3,S} {5,S}
2   R!H  u0 {1,[S,D]} {4,[S,D]}
3   R!H  u0 {1,S} {4,[S,D]}
4   R!H  u0 {2,[S,D]} {3,[S,D]}
5   Val7 u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.374504,-0.547001,-0.67812,-0.75467,-0.737802,-0.625801,-0.526034],'cal/(mol*K)','+|-',[0.0728515,0.0764435,0.088087,0.0904904,0.077731,0.067199,0.140578]),
        H298 = (0.118185,'kcal/mol','+|-',1.79127),
        S298 = (1.08752,'cal/(mol*K)','+|-',0.675673),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 31,
    label = "FourMember-F",
    group = 
"""
1 * R!H u0 {2,[S,D]} {3,S} {5,S}
2   R!H u0 {1,[S,D]} {4,[S,D]}
3   R!H u0 {1,S} {4,[S,D]}
4   R!H u0 {2,[S,D]} {3,[S,D]}
5   F1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.428509,-0.526537,-0.614588,-0.658286,-0.582535,-0.445805,-0.401949],'cal/(mol*K)','+|-',[0.0728515,0.0764435,0.088087,0.0904904,0.077731,0.067199,0.140578]),
        H298 = (1.1512,'kcal/mol','+|-',0.400558),
        S298 = (0.702185,'cal/(mol*K)','+|-',0.22037),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library         | Number of Species
library:CHOF_G4 |         62
""",
)

entry(
    index = 32,
    label = "FourMember-F2",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {5,S} {6,S}
2   R!H u0 {1,S} {4,[S,D]}
3   R!H u0 {1,S} {4,[S,D]}
4   R!H u0 {2,[S,D]} {3,[S,D]}
5   F1s u0 {1,S}
6   F1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.616165,-0.485585,-0.509535,-0.551573,-0.407632,-0.228286,-0.53758],'cal/(mol*K)','+|-',[0.125303,0.131481,0.151508,0.155642,0.133696,0.115581,0.241792]),
        H298 = (-0.22153,'kcal/mol','+|-',0.688951),
        S298 = (-0.866073,'cal/(mol*K)','+|-',0.379032),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library         | Number of Species
library:CHOF_G4 |         39
""",
)

entry(
    index = 33,
    label = "FourMember-Cl",
    group = 
"""
1 * R!H  u0 {2,[S,D]} {3,S} {5,S}
2   R!H  u0 {1,[S,D]} {4,[S,D]}
3   R!H  u0 {1,S} {4,[S,D]}
4   R!H  u0 {2,[S,D]} {3,[S,D]}
5   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.304774,-0.510764,-0.656305,-0.750236,-0.768799,-0.678727,-0.5631],'cal/(mol*K)','+|-',[0.0689122,0.07231,0.0833239,0.0855973,0.0735279,0.0635654,0.132977]),
        H298 = (-0.355615,'kcal/mol','+|-',0.378898),
        S298 = (1.22751,'cal/(mol*K)','+|-',0.208454),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library          | Number of Species
library:CHOCl_G4 |         62
""",
)

entry(
    index = 34,
    label = "FourMember-Cl2",
    group = 
"""
1 * R!H  u0 {2,S} {3,S} {5,S} {6,S}
2   R!H  u0 {1,S} {4,[S,D]}
3   R!H  u0 {1,S} {4,[S,D]}
4   R!H  u0 {2,[S,D]} {3,[S,D]}
5   Cl1s u0 {1,S}
6   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0896295,-0.400063,-0.818194,-1.06045,-1.11724,-1.02981,-1.43564],'cal/(mol*K)','+|-',[0.121202,0.127178,0.146549,0.150548,0.12932,0.111798,0.233878]),
        H298 = (-0.747637,'kcal/mol','+|-',0.666402),
        S298 = (1.27703,'cal/(mol*K)','+|-',0.366626),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library          | Number of Species
library:CHOCl_G4 |         39
""",
)

entry(
    index = 35,
    label = "FourMember-Br",
    group = 
"""
1 * R!H  u0 {2,[S,D]} {3,S} {5,S}
2   R!H  u0 {1,[S,D]} {4,[S,D]}
3   R!H  u0 {1,S} {4,[S,D]}
4   R!H  u0 {2,[S,D]} {3,[S,D]}
5   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.390229,-0.603702,-0.763466,-0.855487,-0.862073,-0.752871,-0.613053],'cal/(mol*K)','+|-',[0.0701245,0.073582,0.0847897,0.0871031,0.0748214,0.0646836,0.135316]),
        H298 = (-0.441031,'kcal/mol','+|-',0.385564),
        S298 = (1.33285,'cal/(mol*K)','+|-',0.212121),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library          | Number of Species
library:CHOBr_G4 |         61
""",
)

entry(
    index = 36,
    label = "FourMember-Br2",
    group = 
"""
1 * R!H  u0 {2,S} {3,S} {5,S} {6,S}
2   R!H  u0 {1,S} {4,[S,D]}
3   R!H  u0 {1,S} {4,[S,D]}
4   R!H  u0 {2,[S,D]} {3,[S,D]}
5   Br1s u0 {1,S}
6   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.140369,-0.242966,-0.703979,-1.01124,-1.22547,-1.19981,-1.48181],'cal/(mol*K)','+|-',[0.122005,0.128021,0.14752,0.151545,0.130177,0.112539,0.235428]),
        H298 = (0.725085,'kcal/mol','+|-',0.670817),
        S298 = (2.58996,'cal/(mol*K)','+|-',0.369055),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library          | Number of Species
library:CHOBr_G4 |         38
""",
)

tree(
"""
L1: R
    L2: ketene
        L3: ketene_2C-C
        L3: ketene_1C-C_1C-H
        L3: biketene
        L3: ketene_2C-H
    L2: ThreeMember-Val7
        L3: ThreeMember-F
            L4: ThreeMember-F2
        L3: ThreeMember-Cl
            L4: ThreeMember-Cl2
        L3: ThreeMember-Br
            L4: ThreeMember-Br2
    L2: ThreeMember-CdVal7
        L3: ThreeMember-CdF
            L4: ThreeMember-CdF2
        L3: ThreeMember-CdCl
            L4: ThreeMember-CdCl2
        L3: ThreeMember-CdBr
            L4: ThreeMember-CdBr2
    L2: ThreeMember-CVal7
        L3: ThreeMember-CF
            L4: ThreeMember-CF2
                L5: ThreeMember-CF3
        L3: ThreeMember-CCl
            L4: ThreeMember-CCl2
                L5: ThreeMember-CCl3
        L3: ThreeMember-CBr
            L4: ThreeMember-CBr2
                L5: ThreeMember-CBr3
    L2: FourMember-Val7
        L3: FourMember-F
            L4: FourMember-F2
        L3: FourMember-Cl
            L4: FourMember-Cl2
        L3: FourMember-Br
            L4: FourMember-Br2
"""
)

