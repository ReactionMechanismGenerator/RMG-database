
name = "2+2_cycloaddition/groups"
shortDesc = ""
longDesc = """

"""

template(reactants=["db"], products=["four_ring"], ownReverse=False)

reverse = "Four_Ring_Cleavage"
reversible = True

recipe(actions=[
    ['CHANGE_BOND', '*1', -1, '*2'],
    ['CHANGE_BOND', '*3', -1, '*4'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['FORM_BOND', '*2', 1, '*4'],
])

entry(
    index = 0,
    label = "db",
    group = 
"""
1 *1 [Cd,Cdd,CO,CS]         u0 {2,D}
2 *2 [Cd,Cdd,CO,CS,O2d,S2d] u0 {1,D}
3 *3 [Cd,Cdd,CO,CS]            u0 {4,D}
4 *4 [Cdd,CO,CS,O2d,S2d]    u0 {3,D}
""",
    kinetics = None,
)

tree(
"""
L1: db
"""
)

forbidden(
    label = "benzene_db",
    group = 
"""
1 *1 Cd u0 {2,D} {6,S}
2 *2 Cd u0 {1,D} {3,S}
3    Cd ux {2,S} {4,D}
4    Cd ux {3,D} {5,S}
5    Cd ux {4,S} {6,D}
6    Cd ux {1,S} {5,D}
""",
    shortDesc = u"""Benzene doublebond *1 *2""",
    longDesc = 
u"""
Banning the doublebond within Benzene from reacting in 2+2 cycloaddition.
""",
)

forbidden(
    label = "benzene_doublebond",
    group = 
"""
1 *3 Cd u0 {2,D} {6,S}
2 *4 Cd u0 {1,D} {3,S}
3    Cd ux {2,S} {4,D}
4    Cd ux {3,D} {5,S}
5    Cd ux {4,S} {6,D}
6    Cd ux {1,S} {5,D}
""",
    shortDesc = u"""Benzene doublebond *3 *4""",
    longDesc = 
u"""
Banning the doublebond within Benzene from reacting in 2+2 cycloaddition.
""",
)
