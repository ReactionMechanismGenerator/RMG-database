#!/usr/bin/env python
# encoding: utf-8

name = "imipramine"
shortDesc = ""
longDesc = """
Calculated using Arkane v2.4.1.

Indices are 1-indexed, corresponding to the following atom order of imipramine:

 N                 -0.00634640   -0.33884115    0.59014543
 C                  1.34971160   -0.59332915    0.28011243
 C                 -0.33884640    1.02531185    0.80935343
 C                  1.90724860   -1.99720215    0.28906443
 H                  1.54683540   -0.24043385   -0.74445243
 H                  2.01383960    0.10240385    0.81678743
 C                 -1.04087840   -1.29842115    0.44492743
 C                  0.01734260    1.63227285    2.01649843
 C                 -0.96251440    1.76363785   -0.20843657
 C                  3.36262660   -1.96925415   -0.18238057
 H                  1.84605060   -2.43910815    1.30009143
 H                  1.31932360   -2.66123715   -0.36605157
 C                 -0.98498540   -2.42954315    1.27978143
 C                 -2.12109040   -1.15216515   -0.45091657
 C                 -0.25921040    2.98164885    2.22905943
 H                  0.51102860    1.03046785    2.78373243
 C                 -1.27502340    1.08404885   -1.50705857
 C                 -1.25012340    3.11152385    0.02862343
 N                  4.20026960   -1.13768215    0.65915443
 H                  3.38114260   -1.55505415   -1.20088257
 H                  3.75199360   -3.00993915   -0.25151957
 C                 -1.94181640   -3.43312815    1.21393843
 H                 -0.17359640   -2.49346015    2.00576243
 C                 -2.36378440    0.02234685   -1.37389557
 C                 -3.08445640   -2.17367815   -0.48437757
 C                 -0.90050640    3.72118885    1.23368643
 H                  0.01841160    3.45358985    3.17527243
 H                 -1.60779740    1.83365885   -2.24172757
 H                 -0.34933940    0.64413985   -1.91332857
 H                 -1.73933540    3.69591885   -0.75661957
 C                  5.30282460   -0.53382415   -0.04745657
 C                  4.60551260   -1.78583115    1.87822243
 C                 -3.00436540   -3.30587615    0.31758043
 H                 -1.86875240   -4.30196615    1.87337043
 H                 -2.58743840   -0.38168415   -2.37611257
 H                 -3.29548040    0.51591885   -1.04184457
 H                 -3.92342640   -2.06790415   -1.17971757
 H                 -1.12568540    4.77886885    1.39528643
 H                  5.84454960    0.15200385    0.62333943
 H                  6.04077360   -1.27564415   -0.43015257
 H                  4.92157960    0.05386585   -0.89461757
 H                  5.12651860   -1.07235215    2.53562043
 H                  5.28861260   -2.65058115    1.70831543
 H                  3.73034460   -2.16058715    2.43060043
 H                 -3.77247840   -4.08092015    0.25152943
"""

# imipramine + CH3OO updated to two para arrhenius fit (same as in training reaction)

entry(
    index = 0,
    label = "imipramine + CH3OO <=> imipramine_rad_2 + CH3OOH",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.13218e+09,'cm^3/(mol*s)'), n=0, Ea=(58.5589,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
                         Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.02664, dn = +|- 0, 
                         dEa = +|- 0.0671562 kJ/mol"""),
    shortDesc = u"""k5+k6""",
    longDesc =
u"""
H6 is blocked, H5 and H6 have the same 2D connectivity
k6 = 0  =>  k5 + k6 = k5
""",
)

entry(
    index = 1,
    label = "imipramine + CH3OO <=> imipramine_rad_3 + CH3OOH",
    degeneracy = 2.0,
    # duplicate = True,
    kinetics = Arrhenius(A=(1.18283e+09,'cm^3/(mol*s)'), n=0, Ea=(71.1023,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
                         Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00034, dn = +|- 0, 
                         dEa = +|- 0.000870252 kJ/mol"""),
    # kinetics = MultiArrhenius(
    #     arrhenius = [
    #         Arrhenius(A=(1.1882e-10,'cm^3/(mol*s)'), n=6.39356, Ea=(55.874,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k11, Fitted to 100 data points; dA = *|/ 1.14786, dn = +|- 0.020122, dEa = +|- 0.057328 kJ/mol"""),
    #         # Arrhenius(A=(2.92217e-08,'cm^3/(mol*s)'), n=5.58651, Ea=(56.1606,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.08935, dn = +|- 0.0124883, dEa = +|- 0.0355794 kJ/mol"""),
    #     ],
    # ),
    shortDesc = u"""k11+k12""",
)

entry(
    index = 2,
    label = "imipramine + CH3OO <=> imipramine_rad_4 + CH3OOH",
    degeneracy = 2.0,
    # duplicate = True,
    kinetics=Arrhenius(A=(1.11619e+10, 'cm^3/(mol*s)'), n=0, Ea=(52.9458, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
                       Tmax=(350, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00001, dn = +|- 0, 
                     dEa = +|- 1.85328e-05 kJ/mol"""),
    # kinetics = MultiArrhenius(
    #     arrhenius = [
    #         Arrhenius(A=(1.60144e-12,'cm^3/(mol*s)'), n=7.44743, Ea=(61.7556,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k20, Fitted to 100 data points; dA = *|/ 1.76345, dn = +|- 0.0827744, dEa = +|- 0.235826 kJ/mol"""),
    #         # Arrhenius(A=(7.00398e-09,'cm^3/(mol*s)'), n=6.21963, Ea=(36.9099,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k21, Fitted to 100 data points; dA = *|/ 1.21987, dn = +|- 0.0290001, dEa = +|- 0.082622 kJ/mol"""),
    #     ],
    # ),
    shortDesc = u"""k20+k21""",
)

entry(
    index = 3,
    label = "imipramine + CH3OO <=> imipramine_rad_1 + CH3OOH",
    degeneracy = 4.0,
    # duplicate = True,
    kinetics=Arrhenius(A=(3.18843e+07, 'cm^3/(mol*s)'), n=0, Ea=(35.8139, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
                       Tmax=(350, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00148, dn = +|- 0, 
                     dEa = +|- 0.00380887 kJ/mol"""),
    # kinetics = MultiArrhenius(
    #     arrhenius = [
    #         Arrhenius(A=(1.69879e-49,'cm^3/(mol*s)'), n=19.1594, Ea=(17.7046,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k28, Fitted to 100 data points; dA = *|/ 12.2045, dn = +|- 0.365056, dEa = +|- 1.04005 kJ/mol"""),
    #         # Arrhenius(A=(2.45476e-50,'cm^3/(mol*s)'), n=19.5114, Ea=(-0.427648,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k29, Fitted to 100 data points; dA = *|/ 6.32046, dn = +|- 0.269041, dEa = +|- 0.766504 kJ/mol"""),
    #         # Arrhenius(A=(3.37035e-33,'cm^3/(mol*s)'), n=13.5841, Ea=(7.70763,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k35, Fitted to 100 data points; dA = *|/ 3.55447, dn = +|- 0.185053, dEa = +|- 0.52722 kJ/mol"""),
    #         # Arrhenius(A=(5.01589e-29,'cm^3/(mol*s)'), n=12.198, Ea=(3.83956,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k36, Fitted to 100 data points; dA = *|/ 2.54252, dn = +|- 0.136163, dEa = +|- 0.387932 kJ/mol"""),
    #     ],
    # ),
    shortDesc = u"""k28+k29+k35+k36""",
)

entry(
    index = 4,
    label = "imipramine + CH3OO <=> imipramine_rad_5 + CH3OOH",
    degeneracy = 6.0,
    # duplicate = True,
    kinetics=Arrhenius(A=(8.81896e+09, 'cm^3/(mol*s)'), n=0, Ea=(56.8704, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
                       Tmax=(350, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00345, dn = +|- 0, 
                     dEa = +|- 0.00889234 kJ/mol"""),
#     kinetics = MultiArrhenius(
# #        arrhenius = [
# #            Arrhenius(A=(1.157e-08,'cm^3/(mol*s)'), n=5.92189, Ea=(46.0794,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k39, Fitted to 100 data points; dA = *|/ 1.28881, dn = +|- 0.0370219, dEa = +|- 0.105476 kJ/mol"""),
# #            Arrhenius(A=(2.63341e-09,'cm^3/(mol*s)'), n=6.19955, Ea=(40.399,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k40, Fitted to 100 data points; dA = *|/ 1.24941, dn = +|- 0.0324912, dEa = +|- 0.092568 kJ/mol"""),
# #            Arrhenius(A=(1.04937e-08,'cm^3/(mol*s)'), n=5.94011, Ea=(48.883,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k41, Fitted to 100 data points; dA = *|/ 1.32039, dn = +|- 0.0405538, dEa = +|- 0.115539 kJ/mol"""),
# #            Arrhenius(A=(9.88708e-07,'cm^3/(mol*s)'), n=5.38234, Ea=(50.9583,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k42, Fitted to 100 data points; dA = *|/ 1.22207, dn = +|- 0.0292627, dEa = +|- 0.0833702 kJ/mol"""),
# #            Arrhenius(A=(7.2759e-10,'cm^3/(mol*s)'), n=6.39346, Ea=(42.8248,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k43, Fitted to 100 data points; dA = *|/ 1.27088, dn = +|- 0.0349779, dEa = +|- 0.0996527 kJ/mol"""),
# #            Arrhenius(A=(1.27688e-07,'cm^3/(mol*s)'), n=5.36061, Ea=(39.9466,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k44, Fitted to 100 data points; dA = *|/ 1.09723, dn = +|- 0.0135395, dEa = +|- 0.0385744 kJ/mol"""),
# #        ],
#         arrhenius = [
#             # Arrhenius(A=(3.471e-08,'cm^3/(mol*s)'), n=5.92189, Ea=(46.0794,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k39, Fitted to 100 data points; dA = *|/ 1.28881, dn = +|- 0.0370219, dEa = +|- 0.105476 kJ/mol"""),
#             # Arrhenius(A=(7.900e-09,'cm^3/(mol*s)'), n=6.19955, Ea=(40.399,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k40, Fitted to 100 data points; dA = *|/ 1.24941, dn = +|- 0.0324912, dEa = +|- 0.092568 kJ/mol"""),
#             Arrhenius(A=(1.04937e-08,'cm^3/(mol*s)'), n=5.94011, Ea=(48.883,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k41, Fitted to 100 data points; dA = *|/ 1.32039, dn = +|- 0.0405538, dEa = +|- 0.115539 kJ/mol"""),
#             # Arrhenius(A=(2.9661e-06,'cm^3/(mol*s)'), n=5.38234, Ea=(50.9583,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k42, Fitted to 100 data points; dA = *|/ 1.22207, dn = +|- 0.0292627, dEa = +|- 0.0833702 kJ/mol"""),
#             # Arrhenius(A=(2.1828e-9,'cm^3/(mol*s)'), n=6.39346, Ea=(42.8248,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k43, Fitted to 100 data points; dA = *|/ 1.27088, dn = +|- 0.0349779, dEa = +|- 0.0996527 kJ/mol"""),
#             # Arrhenius(A=(3.831e-07,'cm^3/(mol*s)'), n=5.36061, Ea=(39.9466,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k44, Fitted to 100 data points; dA = *|/ 1.09723, dn = +|- 0.0135395, dEa = +|- 0.0385744 kJ/mol"""),
#         ],
#     ),
    shortDesc = u"""k39+k40+k41+k42+k43+k44""",
    longDesc =
u"""
Here rotors we not included in the calculation (Eventually we'd like to use rotors).
We're definitely missing a factor of x3 of the torsion missing in the TS,
we might be missing another factor of x3, depends whether the second methyl rotor is active in the TS or not (breaks it).
""",
)



# imipramine + HO2 copied from CH3OO

entry(
    index = 10,
    label = "imipramine + HO2 <=> imipramine_rad_2 + H2O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.13218e+09,'cm^3/(mol*s)'), n=0, Ea=(58.5589,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
                         Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.02664, dn = +|- 0, 
                         dEa = +|- 0.0671562 kJ/mol"""),    shortDesc = u"""k5+k6""",
    longDesc =
u"""
H6 is blocked, H5 and H6 have the same 2D connectivity
k6 = 0  =>  k5 + k6 = k5
""",
)

entry(
    index = 11,
    label = "imipramine + HO2 <=> imipramine_rad_3 + H2O2",
    degeneracy = 2.0,
    # duplicate = True,
    kinetics = Arrhenius(A=(1.18283e+09,'cm^3/(mol*s)'), n=0, Ea=(71.1023,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
                         Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00034, dn = +|- 0, 
                         dEa = +|- 0.000870252 kJ/mol"""),    # kinetics = MultiArrhenius(
    #     arrhenius = [
    #         Arrhenius(A=(1.1882e-10,'cm^3/(mol*s)'), n=6.39356, Ea=(55.874,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k11, Fitted to 100 data points; dA = *|/ 1.14786, dn = +|- 0.020122, dEa = +|- 0.057328 kJ/mol"""),
    #         # Arrhenius(A=(2.92217e-08,'cm^3/(mol*s)'), n=5.58651, Ea=(56.1606,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.08935, dn = +|- 0.0124883, dEa = +|- 0.0355794 kJ/mol"""),
    #     ],
    # ),
    shortDesc = u"""k11+k12""",
)

entry(
    index = 12,
    label = "imipramine + HO2 <=> imipramine_rad_4 + H2O2",
    degeneracy = 2.0,
    # duplicate = True,
    kinetics=Arrhenius(A=(1.11619e+10, 'cm^3/(mol*s)'), n=0, Ea=(52.9458, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
                       Tmax=(350, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00001, dn = +|- 0, 
                     dEa = +|- 1.85328e-05 kJ/mol"""),    # kinetics = MultiArrhenius(
    #     arrhenius = [
    #         Arrhenius(A=(1.60144e-12,'cm^3/(mol*s)'), n=7.44743, Ea=(61.7556,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k20, Fitted to 100 data points; dA = *|/ 1.76345, dn = +|- 0.0827744, dEa = +|- 0.235826 kJ/mol"""),
    #         # Arrhenius(A=(7.00398e-09,'cm^3/(mol*s)'), n=6.21963, Ea=(36.9099,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k21, Fitted to 100 data points; dA = *|/ 1.21987, dn = +|- 0.0290001, dEa = +|- 0.082622 kJ/mol"""),
    #     ],
    # ),
    shortDesc = u"""k20+k21""",
)

entry(
    index = 13,
    label = "imipramine + HO2 <=> imipramine_rad_1 + H2O2",
    degeneracy = 4.0,
    # duplicate = True,
    kinetics=Arrhenius(A=(3.18843e+07, 'cm^3/(mol*s)'), n=0, Ea=(35.8139, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
                       Tmax=(350, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00148, dn = +|- 0, 
                     dEa = +|- 0.00380887 kJ/mol"""),    # kinetics = MultiArrhenius(
    #     arrhenius = [
    #         Arrhenius(A=(1.69879e-49,'cm^3/(mol*s)'), n=19.1594, Ea=(17.7046,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k28, Fitted to 100 data points; dA = *|/ 12.2045, dn = +|- 0.365056, dEa = +|- 1.04005 kJ/mol"""),
    #         # Arrhenius(A=(2.45476e-50,'cm^3/(mol*s)'), n=19.5114, Ea=(-0.427648,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k29, Fitted to 100 data points; dA = *|/ 6.32046, dn = +|- 0.269041, dEa = +|- 0.766504 kJ/mol"""),
    #         # Arrhenius(A=(3.37035e-33,'cm^3/(mol*s)'), n=13.5841, Ea=(7.70763,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k35, Fitted to 100 data points; dA = *|/ 3.55447, dn = +|- 0.185053, dEa = +|- 0.52722 kJ/mol"""),
    #         # Arrhenius(A=(5.01589e-29,'cm^3/(mol*s)'), n=12.198, Ea=(3.83956,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k36, Fitted to 100 data points; dA = *|/ 2.54252, dn = +|- 0.136163, dEa = +|- 0.387932 kJ/mol"""),
    #     ],
    # ),
    shortDesc = u"""k28+k29+k35+k36""",
)

entry(
    index = 14,
    label = "imipramine + HO2 <=> imipramine_rad_5 + H2O2",
    degeneracy = 6.0,
    # duplicate = True,
    kinetics=Arrhenius(A=(8.81896e+09, 'cm^3/(mol*s)'), n=0, Ea=(56.8704, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
                       Tmax=(350, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00345, dn = +|- 0, 
                     dEa = +|- 0.00889234 kJ/mol"""),#     kinetics = MultiArrhenius(
# #        arrhenius = [
# #            Arrhenius(A=(1.157e-08,'cm^3/(mol*s)'), n=5.92189, Ea=(46.0794,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k39, Fitted to 100 data points; dA = *|/ 1.28881, dn = +|- 0.0370219, dEa = +|- 0.105476 kJ/mol"""),
# #            Arrhenius(A=(2.63341e-09,'cm^3/(mol*s)'), n=6.19955, Ea=(40.399,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k40, Fitted to 100 data points; dA = *|/ 1.24941, dn = +|- 0.0324912, dEa = +|- 0.092568 kJ/mol"""),
# #            Arrhenius(A=(1.04937e-08,'cm^3/(mol*s)'), n=5.94011, Ea=(48.883,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k41, Fitted to 100 data points; dA = *|/ 1.32039, dn = +|- 0.0405538, dEa = +|- 0.115539 kJ/mol"""),
# #            Arrhenius(A=(9.88708e-07,'cm^3/(mol*s)'), n=5.38234, Ea=(50.9583,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k42, Fitted to 100 data points; dA = *|/ 1.22207, dn = +|- 0.0292627, dEa = +|- 0.0833702 kJ/mol"""),
# #            Arrhenius(A=(7.2759e-10,'cm^3/(mol*s)'), n=6.39346, Ea=(42.8248,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k43, Fitted to 100 data points; dA = *|/ 1.27088, dn = +|- 0.0349779, dEa = +|- 0.0996527 kJ/mol"""),
# #            Arrhenius(A=(1.27688e-07,'cm^3/(mol*s)'), n=5.36061, Ea=(39.9466,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k44, Fitted to 100 data points; dA = *|/ 1.09723, dn = +|- 0.0135395, dEa = +|- 0.0385744 kJ/mol"""),
# #        ],
#         arrhenius = [
#             # Arrhenius(A=(3.471e-08,'cm^3/(mol*s)'), n=5.92189, Ea=(46.0794,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k39, Fitted to 100 data points; dA = *|/ 1.28881, dn = +|- 0.0370219, dEa = +|- 0.105476 kJ/mol"""),
#             # Arrhenius(A=(7.900e-09,'cm^3/(mol*s)'), n=6.19955, Ea=(40.399,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k40, Fitted to 100 data points; dA = *|/ 1.24941, dn = +|- 0.0324912, dEa = +|- 0.092568 kJ/mol"""),
#             Arrhenius(A=(1.04937e-08,'cm^3/(mol*s)'), n=5.94011, Ea=(48.883,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k41, Fitted to 100 data points; dA = *|/ 1.32039, dn = +|- 0.0405538, dEa = +|- 0.115539 kJ/mol"""),
#             # Arrhenius(A=(2.9661e-06,'cm^3/(mol*s)'), n=5.38234, Ea=(50.9583,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k42, Fitted to 100 data points; dA = *|/ 1.22207, dn = +|- 0.0292627, dEa = +|- 0.0833702 kJ/mol"""),
#             # Arrhenius(A=(2.1828e-9,'cm^3/(mol*s)'), n=6.39346, Ea=(42.8248,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k43, Fitted to 100 data points; dA = *|/ 1.27088, dn = +|- 0.0349779, dEa = +|- 0.0996527 kJ/mol"""),
#             # Arrhenius(A=(3.831e-07,'cm^3/(mol*s)'), n=5.36061, Ea=(39.9466,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k44, Fitted to 100 data points; dA = *|/ 1.09723, dn = +|- 0.0135395, dEa = +|- 0.0385744 kJ/mol"""),
#         ],
#     ),
    shortDesc = u"""k39+k40+k41+k42+k43+k44""",
    longDesc =
u"""
Here rotors we not included in the calculation (Eventually we'd like to use rotors).
We're definitely missing a factor of x3 of the torsion missing in the TS,
we might be missing another factor of x3, depends whether the second methyl rotor is active in the TS or not (breaks it).
""",
)

# imipramine + OHCH2OO updated to two para arrhenius fit (same as in training reaction)


entry(
    index = 20,
    label = "imipramine + OHCH2OO <=> imipramine_rad_2 + OHCH2OOH",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.2408e+08,'cm^3/(mol*s)'), n=0, Ea=(47.4742,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
                         Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00019, dn = +|- 0, 
                         dEa = +|- 0.000483392 kJ/mol"""),    shortDesc = u"""k5+k6""",
    longDesc =
u"""
H6 is blocked, H5 and H6 have the same 2D connectivity
k6 = 0  =>  k5 + k6 = k5
""",
)

entry(
    index = 21,
    label = "imipramine + OHCH2OO <=> imipramine_rad_3 + OHCH2OOH",
    degeneracy = 2.0,
    # duplicate = True,
    kinetics = Arrhenius(A=(3.94097e+07,'cm^3/(mol*s)'), n=0, Ea=(56.0508,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
                         Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00014, dn = +|- 0, 
                         dEa = +|- 0.000364259 kJ/mol"""),    # kinetics = MultiArrhenius(
    #     arrhenius = [
    #         Arrhenius(A=(1.1882e-10,'cm^3/(mol*s)'), n=6.39356, Ea=(55.874,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k11, Fitted to 100 data points; dA = *|/ 1.14786, dn = +|- 0.020122, dEa = +|- 0.057328 kJ/mol"""),
    #         # Arrhenius(A=(2.92217e-08,'cm^3/(mol*s)'), n=5.58651, Ea=(56.1606,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.08935, dn = +|- 0.0124883, dEa = +|- 0.0355794 kJ/mol"""),
    #     ],
    # ),
    shortDesc = u"""k11+k12""",
)

entry(
    index = 22,
    label = "imipramine + OHCH2OO <=> imipramine_rad_4 + OHCH2OOH",
    degeneracy = 2.0,
    # duplicate = True,
    kinetics = Arrhenius(A=(1.32296e+09,'cm^3/(mol*s)'), n=0, Ea=(41.7324,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
                         Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00002, dn = +|- 0, 
                         dEa = +|- 4.59316e-05 kJ/mol"""),    # kinetics = MultiArrhenius(
    #     arrhenius = [
    #         Arrhenius(A=(1.60144e-12,'cm^3/(mol*s)'), n=7.44743, Ea=(61.7556,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k20, Fitted to 100 data points; dA = *|/ 1.76345, dn = +|- 0.0827744, dEa = +|- 0.235826 kJ/mol"""),
    #         # Arrhenius(A=(7.00398e-09,'cm^3/(mol*s)'), n=6.21963, Ea=(36.9099,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k21, Fitted to 100 data points; dA = *|/ 1.21987, dn = +|- 0.0290001, dEa = +|- 0.082622 kJ/mol"""),
    #     ],
    # ),
    shortDesc = u"""k20+k21""",
)

entry(
    index = 23,
    label = "imipramine + OHCH2OO <=> imipramine_rad_1 + OHCH2OOH",
    degeneracy = 4.0,
    # duplicate = True,
    kinetics = Arrhenius(A=(4.7123e+06,'cm^3/(mol*s)'), n=0, Ea=(24.1853,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
                         Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00028, dn = +|- 0, 
                         dEa = +|- 0.000717396 kJ/mol"""),    # kinetics = MultiArrhenius(
    #     arrhenius = [
    #         Arrhenius(A=(1.69879e-49,'cm^3/(mol*s)'), n=19.1594, Ea=(17.7046,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k28, Fitted to 100 data points; dA = *|/ 12.2045, dn = +|- 0.365056, dEa = +|- 1.04005 kJ/mol"""),
    #         # Arrhenius(A=(2.45476e-50,'cm^3/(mol*s)'), n=19.5114, Ea=(-0.427648,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k29, Fitted to 100 data points; dA = *|/ 6.32046, dn = +|- 0.269041, dEa = +|- 0.766504 kJ/mol"""),
    #         # Arrhenius(A=(3.37035e-33,'cm^3/(mol*s)'), n=13.5841, Ea=(7.70763,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k35, Fitted to 100 data points; dA = *|/ 3.55447, dn = +|- 0.185053, dEa = +|- 0.52722 kJ/mol"""),
    #         # Arrhenius(A=(5.01589e-29,'cm^3/(mol*s)'), n=12.198, Ea=(3.83956,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k36, Fitted to 100 data points; dA = *|/ 2.54252, dn = +|- 0.136163, dEa = +|- 0.387932 kJ/mol"""),
    #     ],
    # ),
    shortDesc = u"""k28+k29+k35+k36""",
)

entry(
    index = 24,
    label = "imipramine + OHCH2OO <=> imipramine_rad_5 + OHCH2OOH",
    degeneracy = 6.0,
    # duplicate = True,
    kinetics = Arrhenius(A=(2.1327e+09,'cm^3/(mol*s)'), n=0, Ea=(46.4329,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
                         Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00198, dn = +|- 0, 
                         dEa = +|- 0.00509461 kJ/mol"""),#     kinetics = MultiArrhenius(
# #        arrhenius = [
# #            Arrhenius(A=(1.157e-08,'cm^3/(mol*s)'), n=5.92189, Ea=(46.0794,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k39, Fitted to 100 data points; dA = *|/ 1.28881, dn = +|- 0.0370219, dEa = +|- 0.105476 kJ/mol"""),
# #            Arrhenius(A=(2.63341e-09,'cm^3/(mol*s)'), n=6.19955, Ea=(40.399,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k40, Fitted to 100 data points; dA = *|/ 1.24941, dn = +|- 0.0324912, dEa = +|- 0.092568 kJ/mol"""),
# #            Arrhenius(A=(1.04937e-08,'cm^3/(mol*s)'), n=5.94011, Ea=(48.883,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k41, Fitted to 100 data points; dA = *|/ 1.32039, dn = +|- 0.0405538, dEa = +|- 0.115539 kJ/mol"""),
# #            Arrhenius(A=(9.88708e-07,'cm^3/(mol*s)'), n=5.38234, Ea=(50.9583,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k42, Fitted to 100 data points; dA = *|/ 1.22207, dn = +|- 0.0292627, dEa = +|- 0.0833702 kJ/mol"""),
# #            Arrhenius(A=(7.2759e-10,'cm^3/(mol*s)'), n=6.39346, Ea=(42.8248,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k43, Fitted to 100 data points; dA = *|/ 1.27088, dn = +|- 0.0349779, dEa = +|- 0.0996527 kJ/mol"""),
# #            Arrhenius(A=(1.27688e-07,'cm^3/(mol*s)'), n=5.36061, Ea=(39.9466,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k44, Fitted to 100 data points; dA = *|/ 1.09723, dn = +|- 0.0135395, dEa = +|- 0.0385744 kJ/mol"""),
# #        ],
#         arrhenius = [
#             # Arrhenius(A=(3.471e-08,'cm^3/(mol*s)'), n=5.92189, Ea=(46.0794,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k39, Fitted to 100 data points; dA = *|/ 1.28881, dn = +|- 0.0370219, dEa = +|- 0.105476 kJ/mol"""),
#             # Arrhenius(A=(7.900e-09,'cm^3/(mol*s)'), n=6.19955, Ea=(40.399,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k40, Fitted to 100 data points; dA = *|/ 1.24941, dn = +|- 0.0324912, dEa = +|- 0.092568 kJ/mol"""),
#             Arrhenius(A=(1.04937e-08,'cm^3/(mol*s)'), n=5.94011, Ea=(48.883,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k41, Fitted to 100 data points; dA = *|/ 1.32039, dn = +|- 0.0405538, dEa = +|- 0.115539 kJ/mol"""),
#             # Arrhenius(A=(2.9661e-06,'cm^3/(mol*s)'), n=5.38234, Ea=(50.9583,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k42, Fitted to 100 data points; dA = *|/ 1.22207, dn = +|- 0.0292627, dEa = +|- 0.0833702 kJ/mol"""),
#             # Arrhenius(A=(2.1828e-9,'cm^3/(mol*s)'), n=6.39346, Ea=(42.8248,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k43, Fitted to 100 data points; dA = *|/ 1.27088, dn = +|- 0.0349779, dEa = +|- 0.0996527 kJ/mol"""),
#             # Arrhenius(A=(3.831e-07,'cm^3/(mol*s)'), n=5.36061, Ea=(39.9466,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k44, Fitted to 100 data points; dA = *|/ 1.09723, dn = +|- 0.0135395, dEa = +|- 0.0385744 kJ/mol"""),
#         ],
#     ),
    shortDesc = u"""k39+k40+k41+k42+k43+k44""",
    longDesc =
u"""
Here rotors we not included in the calculation (Eventually we'd like to use rotors).
We're definitely missing a factor of x3 of the torsion missing in the TS,
we might be missing another factor of x3, depends whether the second methyl rotor is active in the TS or not (breaks it).
""",
)

# imipramine + cyanoisopropylOO copied from OHCH2OO


entry(
    index = 25,
    label = "imipramine + cyanoisopropylOO <=> imipramine_rad_2 + cyanoisopropylOOH",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.2408e+08,'cm^3/(mol*s)'), n=0, Ea=(47.4742,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
                         Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00019, dn = +|- 0, 
                         dEa = +|- 0.000483392 kJ/mol"""),
    longDesc =
u"""
copied over, not calculated!!
""",
)

entry(
    index = 26,
    label = "imipramine + cyanoisopropylOO <=> imipramine_rad_3 + cyanoisopropylOOH",
    kinetics=Arrhenius(A=(3.94097e+07, 'cm^3/(mol*s)'), n=0, Ea=(56.0508, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
                       Tmax=(350, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00014, dn = +|- 0, 
                     dEa = +|- 0.000364259 kJ/mol"""),
    shortDesc = u"""k11+k12""",
)

entry(
    index = 27,
    label = "imipramine + cyanoisopropylOO <=> imipramine_rad_4 + cyanoisopropylOOH",
    kinetics=Arrhenius(A=(1.32296e+09, 'cm^3/(mol*s)'), n=0, Ea=(41.7324, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
                       Tmax=(350, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00002, dn = +|- 0, 
                     dEa = +|- 4.59316e-05 kJ/mol"""),
    longDesc=
    u"""
    copied over, not calculated!!
    """,
)

entry(
    index = 28,
    label = "imipramine + cyanoisopropylOO <=> imipramine_rad_1 + cyanoisopropylOOH",
    kinetics=Arrhenius(A=(4.7123e+06, 'cm^3/(mol*s)'), n=0, Ea=(24.1853, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
                       Tmax=(350, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00028, dn = +|- 0, 
                     dEa = +|- 0.000717396 kJ/mol"""),
    longDesc=
    u"""
    copied over, not calculated!!
    """,
)

entry(
    index = 29,
    label = "imipramine + cyanoisopropylOO <=> imipramine_rad_5 + cyanoisopropylOOH",
    kinetics=Arrhenius(A=(2.1327e+09, 'cm^3/(mol*s)'), n=0, Ea=(46.4329, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
                       Tmax=(350, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00198, dn = +|- 0, 
                     dEa = +|- 0.00509461 kJ/mol"""),
    longDesc=
    u"""
    copied over, not calculated!!
    """,
)

entry(
    index = 800,
    label = "imipramine_ol_5 + cyanoisopropylOO <=> imipramine_ol_5_rad_2 + cyanoisopropylOOH",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.2408e+08,'cm^3/(mol*s)'), n=0, Ea=(47.4742,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
                         Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00019, dn = +|- 0, 
                         dEa = +|- 0.000483392 kJ/mol"""),
    longDesc =
u"""
copied over, not calculated!!
""",
)

entry(
    index = 801,
    label = "imipramine_ol_5 + cyanoisopropylOO <=> imipramine_ol_5_rad_3 + cyanoisopropylOOH",
    kinetics=Arrhenius(A=(3.94097e+07, 'cm^3/(mol*s)'), n=0, Ea=(56.0508, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
                       Tmax=(350, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00014, dn = +|- 0, 
                     dEa = +|- 0.000364259 kJ/mol"""),
    shortDesc = u"""k11+k12""",
)

entry(
    index = 802,
    label = "imipramine_ol_5 + cyanoisopropylOO <=> imipramine_ol_5_rad_4 + cyanoisopropylOOH",
    kinetics=Arrhenius(A=(1.32296e+09, 'cm^3/(mol*s)'), n=0, Ea=(41.7324, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
                       Tmax=(350, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00002, dn = +|- 0, 
                     dEa = +|- 4.59316e-05 kJ/mol"""),
    longDesc=
    u"""
    copied over, not calculated!!
    """,
)

entry(
    index = 803,
    label = "imipramine_ol_5 + cyanoisopropylOO <=> imipramine_ol_5_rad_1 + cyanoisopropylOOH",
    kinetics=Arrhenius(A=(4.7123e+06, 'cm^3/(mol*s)'), n=0, Ea=(24.1853, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
                       Tmax=(350, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00028, dn = +|- 0, 
                     dEa = +|- 0.000717396 kJ/mol"""),
    longDesc=
    u"""
    copied over, not calculated!!
    """,
)

entry(
    index = 804,
    label = "imipramine_ol_5 + cyanoisopropylOO <=> imipramine_ol_5_rad_5 + cyanoisopropylOOH",
    kinetics=Arrhenius(A=(2.1327e+09, 'cm^3/(mol*s)'), n=0, Ea=(46.4329, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
                       Tmax=(350, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00198, dn = +|- 0, 
                     dEa = +|- 0.00509461 kJ/mol"""),
    longDesc=
    u"""
    copied over, not calculated!!
    """,
)

entry(
    index = 30,
    label = "imipramine_peroxide_2 + CH2OH <=> imipramine_peroxy_2 + CH3OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.95946e+07,'cm^3/(mol*s)'), n=0, Ea=(26.4854,'kJ/mol'),
                         T0=(1,'K'), Tmin=(275,'K'), Tmax=(350,'K')),
    longDesc =
"""
dlpno-ccsd(t)/def2-tzvp/def2-tzvp/c (APFD SMD solvation scheme) // wb97xd/def2tzvp, no rotors
ts1043 rev

TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
N      -0.38667800   -0.17036500   -0.19575800
C       0.91071800   -0.48833400    0.32187200
C      -1.27357400   -1.22967500   -0.53610800
C       1.77296900   -1.37430200   -0.55933700
C      -0.85172600    1.16059000   -0.06663400
C      -1.12093700   -1.89646100   -1.74884000
C      -2.30018000   -1.60773600    0.33222000
C       2.18844300   -0.66867400   -1.84148200
H       2.65588800   -1.66626500    0.01219400
H       1.24332500   -2.29749100   -0.80502200
C      -0.01869000    2.16039300   -0.58478900
C      -2.06872100    1.52553000    0.52747600
C      -1.94284400   -2.96205500   -2.08518400
H      -0.35855800   -1.56531700   -2.44170000
C      -2.55631900   -0.79932700    1.55991300
C      -3.12734700   -2.66857000   -0.02244000
N       2.90379100    0.57438500   -1.62547200
H       1.29436000   -0.41919800   -2.41828800
C      -0.36302800    3.49677300   -0.52480800
H       0.92182500    1.86139400   -1.03666900
C      -3.05915400    0.59124600    1.18110200
C      -2.40514800    2.88154500    0.54436100
C      -2.94651700   -3.35665300   -1.21311800
H      -1.80550700   -3.47230000   -3.03231300
H      -3.31313800   -1.29582700    2.17310600
H      -1.65254700   -0.71154200    2.16494600
H      -3.92651100   -2.95802800    0.65326400
C       3.05699600    1.29651400   -2.86713900
C       4.17805400    0.39070800   -0.96686400
C      -1.57894600    3.86598900    0.03495900
H       0.30829900    4.24508500   -0.93274100
H      -3.42970800    1.09123600    2.08191200
H      -3.92925900    0.47881000    0.52148200
H      -3.34852700    3.16552100    1.00275400
H      -3.59646800   -4.18751000   -1.46568400
H       3.54097600    2.25728900   -2.68036300
H       3.66486100    0.74769100   -3.60893400
H       2.07759200    1.49094300   -3.31033000
H       4.66557200    1.35985400   -0.84562900
H       4.85923400   -0.26342600   -1.54120900
H       4.04405800   -0.03472400    0.02727800
H      -1.87669300    4.90772700    0.08042700
C       2.77789300    0.25277900    3.32854800
H       3.07670100    1.29204800    3.22023900
H       2.75189200   -0.11372200    4.35907100
O       3.44428300   -0.53922600    2.43220300
H       3.07062500   -1.42838000    2.46390700
H       1.42583200    0.45521400    0.49839100
O       0.84690200   -1.17824100    1.59032900
O       0.44028700   -0.28154400    2.56607500
H       1.46269800    0.14166300    2.98121900
H       2.78231100   -1.36900700   -2.45949100
""",
)

entry(
    index = 31,
    label = "imipramine_peroxy_4 <=> imipramine_peroxide_4_rad_5",
    degeneracy = 6.0,
    kinetics=Arrhenius(A=(7.34524e+10, 's^-1'), n=0, Ea=(68.6755, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(275, 'K'), Tmax=(350, 'K')),
    longDesc =
u"""
dlpno-ccsd(t)/def2-tzvp/def2-tzvp/c//wb97xd/def2tzvp
solvation: SMD water, sp was corrected using APFD/6-311+G(2d,p) SMD water
ts1018

TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
N      -0.34364600   -0.12068400    0.15810200
C       0.87354700   -0.92425800    0.15063200
C      -1.53266700   -0.80105100   -0.21844900
C       1.84092800   -0.48426500    1.24361900
H       0.56479800   -1.94805900    0.35162500
H       1.36983300   -0.93634000   -0.82561900
C      -0.25772200    1.26109000   -0.15246100
C      -1.52831100   -1.74597900   -1.24084700
C      -2.71243600   -0.53493600    0.47954600
C       3.12227800   -1.29361000    1.31091100
H       2.13352300    0.55857500    1.11455600
H       1.34846200   -0.56057700    2.21518600
C       0.84630600    1.72691700   -0.87756400
C      -1.23776300    2.18827900    0.24744900
C      -2.69217700   -2.42101200   -1.57688100
H      -0.61181200   -1.95251000   -1.77907500
C      -2.68538700    0.47808600    1.58020200
C      -3.87402600   -1.20716100    0.11906100
N       3.94358500   -1.23913900    0.09343500
H       3.74792700   -0.91764800    2.12506900
C       1.00261400    3.06232000   -1.19908200
H       1.60137200    1.02758900   -1.20555000
C      -2.49438200    1.89115400    1.04309300
C      -1.06021800    3.52587400   -0.10552800
C      -3.87160800   -2.14867600   -0.90017100
H      -2.67565900   -3.15392800   -2.37395300
H      -3.62412000    0.44426800    2.13449500
H      -1.88293900    0.23675500    2.28114300
H      -4.78975300   -0.99939600    0.66099900
C       3.95520000   -2.41448500   -0.64976600
C       5.23344500   -0.59419500    0.28052800
C       0.03816800    3.97863900   -0.81309600
H       1.87462000    3.37841200   -1.75816400
H      -2.52832000    2.59329300    1.87963500
H      -3.35504200    2.13465600    0.41258700
H      -1.81847900    4.23587600    0.20718700
H      -4.78415000   -2.67058500   -1.15960400
H       2.97134900   -2.74792600   -0.98002600
H       4.72186200   -2.43602600   -1.41713100
H       4.15913000   -3.26477400    0.30403700
H       5.70508000   -0.44610000   -0.68916400
H       5.89298300   -1.20020700    0.91123200
H       5.08969100    0.37679900    0.75252400
H       0.13932000    5.02898300   -1.05493400
O       2.75129700   -2.62981600    1.59473900
O       3.87221400   -3.46673200    1.57020800
""",
)

entry(
    index = 32,
    label = "imipramine_peroxy_4 <=> imipramine_peroxide_4_rad_2",
    degeneracy = 2.0,
    kinetics=Arrhenius(A=(4.27027e+11, 's^-1'), n=0, Ea=(73.8517, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(275, 'K'), Tmax=(350, 'K')),
    longDesc =
u"""
dlpno-ccsd(t)/def2-tzvp/def2-tzvp/c//wb97xd/def2tzvp
solvation: SMD water, sp was corrected using APFD/6-311+G(2d,p) SMD water
ts1019

TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
N      -0.30258700   -0.05606700   -0.42737700
C       0.81265300   -0.72538200    0.09545900
C      -1.49883200   -0.83042900   -0.52898000
C       2.14769400   -0.01983300    0.13847200
H       0.67818300   -0.98580700    1.29313300
H       0.87346000   -1.74185500   -0.30322100
C      -0.39774300    1.36414400   -0.50603700
C      -1.70272000   -1.63677700   -1.63837700
C      -2.42395500   -0.78765000    0.51165800
C       3.15316900   -0.73497100    1.06744400
H       2.57531300    0.05174000   -0.86142400
H       2.00928100    0.99736300    0.50121100
C       0.41719200    1.99677300   -1.44851400
C      -1.27918800    2.11880200    0.27520900
C      -2.85187200   -2.40808900   -1.72666100
H      -0.96016600   -1.65647300   -2.42633900
C      -2.15855400    0.10794800    1.68447600
C      -3.57523400   -1.55870800    0.40322100
N       4.30661100   -1.23617600    0.39436900
H       3.48574600   -0.04132300    1.84180100
C       0.39510500    3.36641300   -1.61243900
H       1.07008500    1.38784600   -2.05974000
C      -2.24231500    1.58488400    1.31359500
C      -1.29173600    3.50255400    0.07796400
C      -3.78979600   -2.36525300   -0.70537400
H      -3.01401200   -3.03738300   -2.59241700
H      -2.89256400   -0.09079000    2.46558600
H      -1.17536100   -0.11088200    2.10772600
H      -4.30594900   -1.53149000    1.20323400
C       4.03070700   -2.24174700   -0.62502200
C       5.34134200   -1.69704400    1.31101400
C      -0.47045400    4.12862800   -0.83868400
H       1.03884400    3.83418000   -2.34628900
H      -2.11022400    2.17899200    2.22044900
H      -3.25677400    1.79579300    0.96147000
H      -1.96991800    4.09788800    0.67917000
H      -4.68992500   -2.96369400   -0.77015600
H       4.93919800   -2.42022400   -1.20139300
H       3.70716700   -3.20025900   -0.20167700
H       3.26230800   -1.89459800   -1.31461700
H       6.26489500   -1.86504100    0.75536000
H       5.07955500   -2.63400200    1.81846800
H       5.53136600   -0.93572800    2.06821600
H      -0.50770200    5.20450700   -0.95387300
O       2.50390000   -1.83474300    1.75752000
O       1.39331200   -1.34656100    2.43079300
""",
)

entry(
    index = 33,
    label = "imipramine_rad_5 <=> imipramine_rad_1",
    degeneracy = 4.0,
    kinetics=Arrhenius(A=(32980, 's^-1'), n=0, Ea=(44.6304, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(275, 'K'), Tmax=(350, 'K')),
    longDesc =
u"""
dlpno-ccsd(t)/def2-tzvp/def2-tzvp/c//wb97xd/def2tzvp
solvation: SMD water, sp was corrected using APFD/6-311+G(2d,p) SMD water
ts1022

This TS restricts 5 rotors, the A factor, originally A=(8.01453e+06, 's^-1'),
was divided by a factor of 3^5 = 243

TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
N      -0.38070300   -0.24956800    0.11972200
C       0.70709000   -1.18047800    0.38654100
C      -1.65446000   -0.80105700   -0.13833900
C       1.68022700   -0.66402600    1.44452100
H       0.24035900   -2.09002300    0.76062400
H       1.26305400   -1.46828300   -0.51424400
C      -0.08605700    1.05853000   -0.30707600
C      -1.77756100   -1.91160900   -0.96898600
C      -2.78987100   -0.27790300    0.50364600
C       0.98925100    0.02206400    2.61721700
H       2.27557400   -1.51450700    1.78598000
H       2.38377600    0.05107400    1.01149500
C       1.04123100    1.27012800   -1.11023800
C      -0.87071300    2.16006700    0.06562000
C      -3.00770900   -2.52028300   -1.16949300
H      -0.89540300   -2.30724100   -1.45729400
C      -2.66778000    0.82840200    1.45440300
C      -4.02011000   -0.90658800    0.28463900
N      -0.10373200   -0.74219000    3.19155000
H       0.57958800    0.97190200    2.27329700
H       1.73887300    0.26290500    3.38610800
C       1.39151100    2.53162700   -1.55369300
H       1.64938600    0.42318000   -1.39835400
C      -2.04763800    2.13574800    1.01830200
C      -0.51246200    3.41709300   -0.42214100
C      -4.13609500   -2.01324200   -0.53998400
H      -3.08204600   -3.38417700   -1.81826400
H      -3.60907600    1.02169600    1.96853200
H      -1.91535300    0.38543200    2.50267200
H      -4.89769600   -0.51676700    0.78813800
C      -1.19982800    0.04066400    3.60012300
C       0.31667500   -1.79780100    4.08922300
C       0.60151500    3.62043200   -1.21653600
H       2.27142300    2.65824500   -2.17243200
H      -1.74866400    2.68796600    1.91700600
H      -2.83586500    2.74530400    0.56283500
H      -1.12483000    4.26681400   -0.13928300
H      -5.10202700   -2.48027400   -0.68745700
H      -1.90624500   -0.51204400    4.21673100
H      -0.96386300    1.02516100    4.02229300
H      -0.54135400   -2.40301100    4.38412300
H       0.79365700   -1.40682200    5.00148300
H       1.03215400   -2.45228800    3.58759700
H       0.85208800    4.61545700   -1.56189000
""",
)

entry(
    index = 34,
    label = "imipramine_rad_5 <=> imipramine_rad_2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.46807e+08,'s^-1'), n=0, Ea=(48.7508,'kJ/mol'),
                         T0=(1,'K'), Tmin=(275,'K'), Tmax=(350,'K')),
    longDesc =
u"""
dlpno-ccsd(t)/def2-tzvp/def2-tzvp/c//wb97xd/def2tzvp
solvation: SMD water, sp was corrected using APFD/6-311+G(2d,p) SMD water
ts1023

TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
N      -0.31000500   -0.21198800    0.31644400
C       0.81520800   -1.07594900    0.47504900
C      -1.51164300   -0.82642400   -0.13385500
C       1.87332800   -0.65914300    1.47462300
H       0.45272000   -2.08012900    0.69172600
H       1.53714600   -1.30051400   -0.56708800
C      -0.11966600    1.14959700   -0.04417800
C      -1.49037400   -1.79342200   -1.13310000
C      -2.71547200   -0.45972300    0.46838200
C       3.15974700   -1.43809700    1.23380700
H       2.08309900    0.40892000    1.39961000
H       1.52343300   -0.84979300    2.49360100
C       1.03336400    1.50059000   -0.75424900
C      -1.05249600    2.14903600    0.27737600
C      -2.67073600   -2.39276000   -1.54642100
H      -0.54828600   -2.07257700   -1.58934400
C      -2.69259500    0.57052000    1.55442100
C      -3.89080600   -1.05837000    0.03123600
N       3.69257400   -1.20198500   -0.10636200
H       2.97702200   -2.51545600    1.39363500
H       3.91246600   -1.13087900    1.96084000
C       1.29057000    2.80672800   -1.12502400
H       1.73897600    0.72969400   -1.02746000
C      -2.35996900    1.95987200    1.02197500
C      -0.77261800    3.45589700   -0.12314700
C      -3.87552000   -2.02111800   -0.96811300
H      -2.64743300   -3.14418900   -2.32580000
H      -3.66823200    0.61385900    2.04000000
H      -1.96293700    0.28144600    2.31429100
H      -4.82875900   -0.77583100    0.49570200
C       2.79961800   -1.73070700   -1.09775700
C       5.02107400   -1.78483300   -0.24210700
C       0.37840500    3.80086500   -0.80721800
H       2.19691200    3.04022600   -1.66975200
H      -2.37320000    2.66721700    1.85479300
H      -3.16783300    2.27029900    0.35247300
H      -1.49224700    4.22780300    0.12777100
H      -4.80052800   -2.48339900   -1.28924400
H       2.96074700   -1.33646200   -2.09906800
H       2.67143100   -2.82211900   -1.07745400
H       5.40663400   -1.59704000   -1.24502800
H       5.01250300   -2.87392600   -0.07815000
H       5.70493500   -1.33463600    0.48015200
H       0.55859300    4.83041200   -1.08926400
""",
)

entry(
    index = 35,
    label = "imipramine_peroxy_5 <=> imipramine_peroxide_5_rad_4",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(7.4259e+09,'s^-1'), n=0, Ea=(58.9622,'kJ/mol'),
                         T0=(1,'K'), Tmin=(275,'K'), Tmax=(350,'K')),
    longDesc =
u"""
dlpno-ccsd(t)/def2-tzvp/def2-tzvp/c//wb97xd/def2tzvp
solvation: SMD water, sp was corrected using APFD/6-311+G(2d,p) SMD water
ts1035

TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
N      -0.38164700    0.67466500   -0.61649500
C       1.03212400    0.71987700   -0.25791800
C      -0.92216900   -0.64019600   -0.70565600
C       1.96401300    0.29362300   -1.39587100
H       1.22576000    0.09592400    0.62354500
C      -1.19252300    1.76242700   -0.19756200
C      -0.97386000   -1.26473700   -1.94539600
C      -1.33422300   -1.32877700    0.43621900
C       3.34115200   -0.09383200   -0.91948100
H       1.51762700   -0.53559900   -1.94925300
H       2.05466100    1.11703600   -2.10574700
C      -0.99112000    2.96588700   -0.88017000
C      -2.13919900    1.71454800    0.83373200
C      -1.39879500   -2.57978800   -2.05823000
H      -0.67708100   -0.70068500   -2.82037100
C      -1.38970400   -0.59756800    1.74380100
C      -1.76478000   -2.64313600    0.31106000
N       3.56503500   -1.41749500   -0.46621400
H       4.14548000    0.20478400   -1.59523100
C      -1.69933100    4.10771600   -0.57050400
H      -0.26352100    2.97392400   -1.68253300
C      -2.44030200    0.51129500    1.70243400
C      -2.86646400    2.87534000    1.10711900
C      -1.78653100   -3.27381500   -0.92386100
H      -1.43084000   -3.05684900   -3.02939300
H      -1.64615600   -1.29607900    2.54178400
H      -0.41571200   -0.17122200    1.99696800
H      -2.08971300   -3.17945600    1.19545300
C       2.46237500   -2.21391700    0.05039100
C       4.75693800   -1.47528300    0.33638000
C      -2.66000600    4.05968600    0.42937900
H      -1.51748200    5.02392400   -1.11771800
H      -2.60356400    0.87651400    2.71878500
H      -3.39012200    0.07069400    1.38148900
H      -3.60402900    2.84230100    1.90177900
H      -2.11878200   -4.30138200   -1.00029000
H       2.79428800   -3.24948500    0.12870600
H       2.12641600   -1.88335700    1.03803000
H       1.61529200   -2.18502900   -0.63164600
H       4.94928900   -2.49407700    0.66963700
H       5.60429400   -1.07173000   -0.22442100
H      -3.23810600    4.93908800    0.68223000
H       1.27430400    1.73977100    0.03932100
H       3.74369700    0.57029600    0.14233900
O       4.55851400   -0.71204500    1.51114200
O       4.51095500    0.63035400    1.15257000
""",
)

# entry(
#     index = 36,
#     label = "imipramine_peroxy_5 + CH3OH <=> imipramine_peroxide_5 + CH2OH",
#     degeneracy = 3.0,
#     kinetics = Arrhenius(A=(5.99556e+08,'cm^3/(mol*s)'), n=0, Ea=(50.5221,'kJ/mol'),
#                          T0=(1,'K'), Tmin=(275,'K'), Tmax=(350,'K')),
#     longDesc =
# """
# dlpno-ccsd(t)/def2-tzvp/def2-tzvp/c (APFD SMD solvation scheme) // wb97xd/def2tzvp, no rotors
# ts1034b
#
# based on a fragment
#
# TS external symmetry: 1, TS optical isomers: 2
#
# Optimized TS geometry:
# N       2.64279400   -0.50044300    1.63237100
# C       2.41271500    0.12615100    0.33930500
# C       1.18277100   -0.33806000   -0.44600500
# H       3.30050000   -0.04256700   -0.27464300
# C      -0.12370300    0.02079700    0.24332100
# H       1.22374800    0.12219900   -1.43705400
# H       1.22956400   -1.42290400   -0.58979400
# N      -1.30465600   -0.58188600   -0.35582200
# H      -0.08928900   -0.33613900    1.27655200
# C      -1.47030900   -0.39072900   -1.74491200
# C      -2.49005300   -0.39773300    0.45999000
# H      -2.39073100   -0.87209300   -2.07850500
# H      -0.61992500   -0.79780500   -2.29428600
# H      -3.34911000   -0.85535400   -0.03050300
# H      -2.72767900    0.65807500    0.64148800
# H      -2.34264100   -0.89206100    1.42321200
# H       2.65867600   -1.50842500    1.54762100
# H       1.91793400   -0.26361900    2.29500400
# H       2.35497900    1.20682900    0.49784000
# H      -0.21903700    1.11719400    0.29014100
# O      -1.49140000    0.97988300   -2.20486000
# O      -2.67855200    1.58136000   -1.82056900
# H      -3.35349600    1.49763500   -2.81034800
# C      -3.74288000    1.33291500   -4.07957900
# H      -4.76337100    0.95969400   -4.07881100
# H      -3.63192700    2.34750500   -4.47131500
# O      -2.88985500    0.40337300   -4.60774500
# H      -1.98637300    0.71920500   -4.50118400
# """,
# )

entry(
    index = 36,
    label = "imipramine_peroxy_5 + CH3OH <=> imipramine_peroxide_5 + CH2OH",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(5.99556e+08,'cm^3/(mol*s)'), n=0, Ea=(20.5221,'kJ/mol'),
                         T0=(1,'K'), Tmin=(275,'K'), Tmax=(350,'K')),
    longDesc =
"""
dlpno-ccsd(t)/def2-tzvp/def2-tzvp/c (APFD SMD solvation scheme) // wb97xd/def2tzvp, no rotors
ts1034b

based on a fragment

TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
N       2.64279400   -0.50044300    1.63237100
C       2.41271500    0.12615100    0.33930500
C       1.18277100   -0.33806000   -0.44600500
H       3.30050000   -0.04256700   -0.27464300
C      -0.12370300    0.02079700    0.24332100
H       1.22374800    0.12219900   -1.43705400
H       1.22956400   -1.42290400   -0.58979400
N      -1.30465600   -0.58188600   -0.35582200
H      -0.08928900   -0.33613900    1.27655200
C      -1.47030900   -0.39072900   -1.74491200
C      -2.49005300   -0.39773300    0.45999000
H      -2.39073100   -0.87209300   -2.07850500
H      -0.61992500   -0.79780500   -2.29428600
H      -3.34911000   -0.85535400   -0.03050300
H      -2.72767900    0.65807500    0.64148800
H      -2.34264100   -0.89206100    1.42321200
H       2.65867600   -1.50842500    1.54762100
H       1.91793400   -0.26361900    2.29500400
H       2.35497900    1.20682900    0.49784000
H      -0.21903700    1.11719400    0.29014100
O      -1.49140000    0.97988300   -2.20486000
O      -2.67855200    1.58136000   -1.82056900
H      -3.35349600    1.49763500   -2.81034800
C      -3.74288000    1.33291500   -4.07957900
H      -4.76337100    0.95969400   -4.07881100
H      -3.63192700    2.34750500   -4.47131500
O      -2.88985500    0.40337300   -4.60774500
H      -1.98637300    0.71920500   -4.50118400
""",
)

entry(
    index = 37,
    label = "N(C)(C)C(OOJ)CC(OOH)NH2 <=> N(C)(C)C(OOH)CCJ(OOH)NH2_p",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.5081e+08,'s^-1'), n=0, Ea=(67.4495,'kJ/mol'),
                         T0=(1,'K'), Tmin=(200,'K'), Tmax=(495, 'K')),
    longDesc =
u"""
This is a fake reaction. products are unstable so forward rate calcualted using '
                                 'reactant as products. Fitted to 60 data points; dA = *|/ 1.62624, dn = +|- 0, '
                                 'dEa = +|- 1.26739 kJ/mol'
                                 
dlpno-ccsd(t)/def2-tzvp/def2-tzvp/c//wb97xd/def2tzvp
solvation: SMD water, sp was corrected using APFD/6-311+G(2d,p) SMD water
ts1038 forward only

TS geom
 N                  2.51752000   -1.07335300   -1.05889900
 C                  1.51453700   -0.47971400   -0.28901200
 C                  0.15956600   -1.13100800   -0.28745500
 C                 -0.98287800   -0.11707700   -0.55433900
 H                  0.11586200   -1.89937400   -1.06110000
 H                 -0.00224800   -1.61576900    0.67755800
 N                 -2.20835100   -0.49660300    0.04572600
 C                 -3.36558800    0.15224000   -0.53792900
 C                 -2.24894800   -0.45253700    1.49624700
 H                 -4.27231500   -0.32399400   -0.15887900
 H                 -3.35011800    0.03386000   -1.62268900
 H                 -3.11261400   -1.02241100    1.84578700
 H                 -2.32837700    0.57124400    1.88501200
 H                 -1.35338100   -0.90033300    1.92488700
 H                  2.56009300   -2.08286300   -0.98646400
 H                  3.42359900   -0.65795000   -0.89194600
 H                 -1.13043800   -0.03219200   -1.63536700
 H                 -3.41755600    1.22528300   -0.30539000
 O                 -0.58359700    1.19063800   -0.09804800
 O                  0.43090900    1.63287600   -0.93751900
 H                  1.19923900    0.70282200   -0.80556700
 O                  1.80871200   -0.13775100    1.04256800
 O                  2.91687200    0.75794600    1.03187500
 H                  2.46077200    1.61028200    0.95028200
""",
)

entry(
    index = 38,
    label = "imipramine_tail_2_OO_rad <=> imipramine_tail_2_OOH_4_rad",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.01382e+10,'s^-1'), n=0, Ea=(64.066,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'), Tmax=(350,'K')),
    longDesc =
"""
dlpno-ccsd(t)/def2-tzvp/def2-tzvp/c//apfd/def2tzvp
solvation: SMD water, sp was corrected using APFD/6-311+G(2d,p) SMD water

ts1051

TS method summary for TS0 in fargment_peroxide_rad_4 <=> fargment_peroxide_4

The method that generated the best TS guess and its output used for the optimization: user guess 0

TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
N       4.71018900    0.25300500   -0.16010100
C       3.74874000   -0.76583200   -0.15633500
C       2.49883600   -0.46247100    0.62972100
H       4.15446700   -1.77120300   -0.01723600
C       1.51579600    0.36330700   -0.21905400
H       2.01459800   -1.39801900    0.91142300
H       2.71950700    0.09316600    1.54939000
N       0.33342600    0.74614300    0.46587900
H       2.02181000    1.26842900   -0.57662500
C      -0.48803600   -0.32717800    0.99150400
C      -0.45572100    1.71490000   -0.26925900
H      -1.27484900    0.10697500    1.61189900
H       0.10091800   -0.98789600    1.62666900
H      -1.22187400    2.13038100    0.38918200
H      -0.95141200    1.28497800   -1.15065200
H       0.18430000    2.53324300   -0.60420800
H       5.66223000    0.00609100   -0.36328600
H       4.61172000    1.00548700    0.50045000
H       3.21003500   -0.80565300   -1.33632300
H      -0.96401600   -0.93113000    0.20678900
O       1.20182400   -0.42476000   -1.38005000
O       2.33004300   -0.46518000   -2.18550600
""",
)

entry(
    index = 39,
    label = "imipramine_rad_1 + HO2 <=> imipramine + O2",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(1.0e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
                         Tmax=(350,'K')),
    shortDesc = u"""diffusion limit""",
    longDesc =
u"""
Use diffusion limit after discussing with Prof. Green
""",
)

entry(
    index = 40,
    label = "imipramine_rad_2 + HO2 <=> imipramine + O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.0e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
                         Tmax=(350,'K')),
    shortDesc = u"""diffusion limit""",
    longDesc =
u"""
Use diffusion limit after discussing with Prof. Green
""",
)

entry(
    index = 41,
    label = "imipramine_rad_3 + HO2 <=> imipramine + O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.0e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
                         Tmax=(350,'K')),
    shortDesc = u"""diffusion limit""",
    longDesc =
u"""
Use diffusion limit after discussing with Prof. Green
""",
)

entry(
    index = 42,
    label = "imipramine_rad_4 + HO2 <=> imipramine + O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.0e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
                         Tmax=(350,'K')),
    shortDesc = u"""diffusion limit""",
    longDesc =
u"""
Use diffusion limit after discussing with Prof. Green
""",
)

entry(
    index = 43,
    label = "imipramine_rad_5 + HO2 <=> imipramine + O2",
    degeneracy = 6.0,
    kinetics = Arrhenius(A=(1.0e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
                         Tmax=(350,'K')),
    shortDesc = u"""diffusion limit""",
    longDesc =
u"""
Use diffusion limit after discussing with Prof. Green
""",
)











