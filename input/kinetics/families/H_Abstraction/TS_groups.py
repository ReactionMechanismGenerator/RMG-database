#!/usr/bin/env python
# encoding: utf-8

name = "H_Abstraction/TS_groups"
shortDesc = u""
longDesc = u"""

"""

entry(
	index = 1,
	label = "X_H_or_Xrad_H_Xbirad_H_Xtrirad_H",
	group = "OR{H2, C_H, O_H}",
	distances = DistanceData(distances={}),
)

entry(
	index = 3,
	label = "H2",
	group =
 """
 1 *1 H u0 {2,S}
 2 *2 H u0 {1,S}
 """,
	distances = DistanceData(distances={}),
)

entry(
	index = 4,
	label = "C_H",
	group =
"""
1 *1 C ux {2,S}
2 *2 H u0 {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 11,
	label = "Cs_H",
	group =
"""
1 *1 Cs ux {2,S}
2 *2 H  u0 {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 22,
	label = "Csnorad_H",
	group =
"""
1 *1 Cs u0 {2,S}
2 *2 H  u0 {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 43,
	label = "C_methane",
	group =
"""
1 *1 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 44,
	label = "CsRHHH",
	group =
"""
1 *1 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   u0 {1,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    R!H ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 69,
	label = "CsCHHH",
	group =
"""
1 *1 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    C  ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 70,
	label = "CsOHHH",
	group =
"""
1 *1 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    O  ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 45,
	label = "CsRRHH",
	group =
"""
1 *1 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   u0 {1,S}
3    H   u0 {1,S}
4    R!H ux {1,S}
5    R!H ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 71,
	label = "CsCCHH",
	group =
"""
1 *1 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    C  ux {1,S}
5    C  ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 72,
	label = "CsCOHH",
	group =
"""
1 *1 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    C  ux {1,S}
5    O  ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 73,
	label = "CsOOHH",
	group =
"""
1 *1 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    O  ux {1,S}
5    O  ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 46,
	label = "CsRRRH",
	group =
"""
1 *1 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   u0 {1,S}
3    R!H ux {1,S}
4    R!H ux {1,S}
5    R!H ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 74,
	label = "CsCCCH",
	group =
"""
1 *1 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    C  ux {1,S}
4    C  ux {1,S}
5    C  ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 75,
	label = "CsCCOH",
	group =
"""
1 *1 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    C  ux {1,S}
4    C  ux {1,S}
5    O  ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 76,
	label = "CsCOOH",
	group =
"""
1 *1 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    C  ux {1,S}
4    O  ux {1,S}
5    O  ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 77,
	label = "CsOOOH",
	group =
"""
1 *1 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    O  ux {1,S}
4    O  ux {1,S}
5    O  ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 23,
	label = "Csrad_H",
	group =
"""
1 *1 Cs u1 {2,S}
2 *2 H  u0 {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 47,
	label = "C_methyl",
	group =
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 48,
	label = "CsRHjH",
	group =
"""
1 *1 Cs   u1 {2,S} {3,S} {4,S}
2 *2 H    u0 {1,S}
3    H    u0 {1,S}
4    R!H  ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 78,
	label = "CsCHjH",
	group =
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    C  ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 79,
	label = "CsOHjH",
	group =
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    O  ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 49,
	label = "CsRRjH",
	group =
"""
1 *1 Cs   u1 {2,S} {3,S} {4,S}
2 *2 H    u0 {1,S}
3    R!H  ux {1,S}
4    R!H  ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 80,
	label = "CsCCjH",
	group =
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 H  u0 {1,S}
3    C  ux {1,S}
4    C  ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 81,
	label = "CsCOjH",
	group =
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 H  u0 {1,S}
3    C  ux {1,S}
4    O  ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 82,
	label = "CsOOjH",
	group =
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 H  u0 {1,S}
3    O  ux {1,S}
4    O  ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 24,
	label = "CsbiradH",
	group = "OR{Cs_singletH, Cs_tripletH}",
	distances = DistanceData(distances={}),
)

entry(
	index = 50,
	label = "Cs_singletH",
	group =
"""
1 *1 Cs u0 p1 {2,S} {3,S}
2 *2 H  u0    {1,S}
3    R  ux    {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 83,
	label = "Cs_singletHH",
	group =
"""
1 *1 Cs u0 p1 {2,S} {3,S}
2 *2 H  u0 	  {1,S}
3    H  u0 	  {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 84,
	label = "Cs_singletRH",
	group =
"""
1 *1 Cs  u0 p1 {2,S} {3,S}
2 *2 H   u0    {1,S}
3    R!H ux    {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 108,
	label = "C_singletCH",
	group =
"""
1 *1 Cs u0 p1 {2,S} {3,S}
2 *2 H  u0    {1,S}
3    C  ux    {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 109,
	label = "C_singletOH",
	group =
"""
1 *1 Cs u0 p1 {2,S} {3,S}
2 *2 H  u0    {1,S}
3    C  ux    {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 51,
	label = "Cs_tripletH",
	group =
"""
1 *1 Cs u2 {2,S} {3,S}
2 *2 H  u0 {1,S}
3    R  ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 85,
	label = "Cs_tripletHH",
	group =
"""
1 *1 Cs u2 {2,S} {3,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 86,
	label = "Cs_tripletRH",
	group =
"""
1 *1 Cs  u2 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    R!H ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 110,
	label = "Cs_tripletCH",
	group =
"""
1 *1 Cs u2 {2,S} {3,S}
2 *2 H  u0 {1,S}
3    C  ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 111,
	label = "Cs_tripletOH",
	group =
"""
1 *1 Cs u2 {2,S} {3,S}
2 *2 H  u0 {1,S}
3    O  ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 25,
	label = "CstriradH",
	group = "OR{Cdoublet_H, Cquartet_H}",
	distances = DistanceData(distances={}),
)

entry(
	index = 52,
	label = "Cdoublet_H",
	group =
"""
1 *1 C u1 p1 {2,S}
2 *2 H u0 p0 {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 53,
	label = "Cquartet_H",
	group =
"""
1 *1 C u3 p0 {2,S}
2 *2 H u0 p0 {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 12,
	label = "Cd_H",
	group =
"""
1 *1 Cd ux {2,S}
2 *2 H  u0 {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 26,
	label = "Cdnorad_H",
	group =
"""
1 *1 Cd u0 {2,S}
2 *2 H  u0 {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 54,
	label = "Cd(=C)RH",
	group =
"""
1 *1 Cd u0 {2,S} {3,D}
2 *2 H  u0 {1,S}
3    C  ux {1,D}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 87,
	label = "Cd(=C)HH",
	group =
"""
1 *1 Cd u0 {2,S} {3,D} {4,S}
2 *2 H  u0 {1,S}
3    C  ux {1,D}
4    H  u0 {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 88,
	label = "Cd(=C)CH",
	group =
"""
1 *1 Cd u0 {2,S} {3,D} {4,S}
2 *2 H  u0 {1,S}
3    C  ux {1,D}
4    C  ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 89,
	label = "Cd(=C)OH",
	group =
"""
1 *1 Cd u0 {2,S} {3,D} {4,S}
2 *2 H  u0 {1,S}
3    C  ux {1,D}
4    O  ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 55,
	label = "Cd(=O)RH",
	group =
"""
1 *1 Cd u0 {2,S} {3,D}
2 *2 H  u0 {1,S}
3    O  u0 {1,D}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 90,
	label = "Cd(=O)HH",
	group =
"""
1 *1 Cd u0 {2,S} {3,D} {4,S}
2 *2 H  u0 {1,S}
3    O  u0 {1,D}
4    H  u0 {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 91,
	label = "Cd(=O)CH",
	group =
"""
1 *1 Cd u0 {2,S} {3,D} {4,S}
2 *2 H  u0 {1,S}
3    O  u0 {1,D}
4    C  ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 92,
	label = "Cd(=O)OH",
	group =
"""
1 *1 Cd u0 {2,S} {3,D} {4,S}
2 *2 H  u0 {1,S}
3    O  u0 {1,D}
4    O  ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 27,
	label = "Cdrad_H",
	group =
"""
1 *1 Cd u1 {2,S}
2 *2 H  u0 {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 56,
	label = "Cd(=C)jH",
	group =
"""
1 *1 Cd u1 {2,S} {3,D}
2 *2 H  u0 {1,S}
3    C  ux {1,D}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 57,
	label = "Cd(=O)jH",
	group =
"""
1 *1 Cd u1 {2,S} {3,D}
2 *2 H  u0 {1,S}
3    O  u0 {1,D}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 13,
	label = "Ct_H",
	group =
"""
1 *1 Ct u0 {2,S}
2 *2 H  u0 {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 28,
	label = "CtCH",
	group =
"""
1 *1 Ct u0 {2,S} {3,T}
2 *2 H  u0 {1,S}
3    C  ux {1,T}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 14,
	label = "Cb_H",
	group =
"""
1 *1 Cb u0 {2,S}
2 *2 H  u0 {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 5,
	label = "O_H",
	group =
"""
1 *1 O ux {2,S}
2 *2 H u0 {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 13,
	label = "OradH",
	group =
"""
1 *1 O u1 {2,S}
2 *2 H u0 {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 14,
	label = "ORH",
	group =
"""
1 *1 O u0 {2,S}
2 *2 H u0 {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 27,
	label = "OHH",
	group =
"""
1 *1 O u1 {2,S} {3,S}
2 *2 H u0 {1,S}
3    H u0 {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 28,
	label = "OCH",
	group =
"""
1 *1 O u1 {2,S} {3,S}
2 *2 H u0 {1,S}
3    C ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 29,
	label = "OOH",
	group =
"""
1 *1 O u1 {2,S} {3,S}
2 *2 H u0 {1,S}
3    O ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 2,
	label = "Y_rad_birad_trirad_quadrad",
	group = "OR{Hrad, Orad, Crad}",
	distances = DistanceData(distances={}),
)

entry(
	index = 6,
	label = "Hrad",
	group =
"""
1 *3 H u1
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 7,
	label = "Orad",
	group =
"""
1 *3 O u[1,2]
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 15,
	label = "OjR",
	group =
"""
1 *3 O u1 {2,S}
2    R ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 30,
	label = "OjH",
	group =
"""
1 *3 O u1 {2,S}
2    H u0 {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 31,
	label = "OjC",
	group =
"""
1 *3 O u1 {2,S}
2    C ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 32,
	label = "OjO",
	group =
"""
1 *3 O u1 {2,S}
2    O ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 16,
	label = "O_atom_triplet",
	group =
"""
1 *3 O u2
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 8,
	label = "Crad",
	group =
"""
1 *3 C u[1,2,3]
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 17,
	label = "Cj",
	group =
"""
1 *3 C u1
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 33,
	label = "Csj",
	group =
"""
1 *3 Cs u1
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 56,
	label = "Cs_methyl",
	group =
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 57,
	label = "CsRHHj",
	group =
"""
1 *3 Cs  u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3    H   u0 {1,S}
4    R!H ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 91,
	label = "CsCHHj",
	group =
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    C  ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 92,
	label = "CsOHHj",
	group =
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    O  ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 58,
	label = "CsRRHj",
	group =
"""
1 *3 Cs  u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3    R!H ux {1,S}
4    R!H ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 93,
	label = "CsCCHj",
	group =
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    C  ux {1,S}
4    C  ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 94,
	label = "CsCOHj",
	group =
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    C  ux {1,S}
4    O  ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 95,
	label = "CsOOHj",
	group =
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    O  ux {1,S}
4    O  ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 59,
	label = "CsRRRj",
	group =
"""
1 *3 Cs  u1 {2,S} {3,S} {4,S}
2    R!H ux {1,S}
3    R!H ux {1,S}
4    R!H ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 96,
	label = "CsCCCj",
	group =
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    C  ux {1,S}
3    C  ux {1,S}
4    C  ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 97,
	label = "CsCCOj",
	group =
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    C  ux {1,S}
3    C  ux {1,S}
4    O  ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 98,
	label = "CsCOOj",
	group =
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    C  ux {1,S}
3    O  ux {1,S}
4    O  ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 99,
	label = "CsOOOj",
	group =
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    O  ux {1,S}
3    O  ux {1,S}
4    O  ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 34,
	label = "Cdj",
	group =
"""
1 *3 Cd u1
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 60,
	label = "Cd(=C)Rj",
	group =
"""
1 *3 Cd u1 {2,D}
2    C  ux {1,D}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 100,
	label = "Cd(=C)Hj",
	group =
"""
1 *3 Cd u1 {2,D} {3,S}
2    C  ux {1,D}
3    H  u0 {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 101,
	label = "Cd(=C)Cj",
	group =
"""
1 *3 Cd u1 {2,D} {3,S}
2    C  ux {1,D}
3    C  ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 102,
	label = "Cd(=C)Oj",
	group =
"""
1 *3 Cd u1 {2,D} {3,S}
2    C  ux {1,D}
3    O  ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 61,
	label = "Cd(=O)Rj",
	group =
"""
1 *3 Cd u1 {2,D}
2    O  u0 {1,D}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 103,
	label = "Cd(=O)Hj",
	group =
"""
1 *3 Cd u1 {2,D} {3,S}
2    O  u0 {1,D}
3    H  u0 {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 104,
	label = "Cd(=O)Cj",
	group =
"""
1 *3 Cd u1 {2,D} {3,S}
2    O  u0 {1,D}
3    C  ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 105,
	label = "Cd(=O)Oj",
	group =
"""
1 *3 Cd u1 {2,D} {3,S}
2    O  u0 {1,D}
3    O  ux {1,S}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 35,
	label = "Ctj",
	group =
"""
1 *3 Ct u1
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 62,
	label = "CtCj",
	group =
"""
1 *3 Cd u1 {2,T}
2    C  ux {1,T}
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 36,
	label = "Cbj",
	group =
"""
1 *3 Cb u1
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 18,
	label = "Cjj",
	group = "OR{Csjj, Cdjj}",
	distances = DistanceData(distances={}),
)

entry(
	index = 37,
	label = "Csjj",
	group = "OR{C_singletRR, C_tripletRR}",
	distances = DistanceData(distances={}),
)

entry(
	index = 63,
	label = "C_singletRR",
	group =
"""
1 *3 Cs u0 p1
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 64,
	label = "C_tripletRR",
	group =
"""
1 *3 Cs u2 p0
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 38,
	label = "Cdjj",
	group = "OR{C_singletR, C_tripletR}",
	distances = DistanceData(distances={}),
)

entry(
	index = 65,
	label = "C_singletR",
	group =
"""
1 *3 Cd u0 p1
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 66,
	label = "C_tripletR",
	group =
"""
1 *3 Cd u2 p0
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 19,
	label = "Cjjj",
	group = "OR{C_doubletR, C_quartetR}",
	distances = DistanceData(distances={}),
)

entry(
	index = 39,
	label = "C_doubletR",
	group =
"""
1 *3 C u1 p1 
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 40,
	label = "C_quartetR",
	group =
"""
1 *3 C u3 
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 112,
	label = "Cjjjj",
	group = "OR{C_quintet, C_triplet}",
	distances = DistanceData(distances={}),
)

entry(
	index = 113,
	label = "C_quintet",
	group =
"""
1 *3 C u4 p0
""",
	distances = DistanceData(distances={}),
)

entry(
	index = 114,
	label = "C_triplet",
	group =
"""
1 *3 C u2 p1
""",
	distances = DistanceData(distances={}),
)

tree(
"""
L1: X_H_or_Xrad_H_Xbirad_H_Xtrirad_H
	L2: H2
	L2: C_H
		L3: Cs_H
			L4: Csnorad_H
				L5: C_methane
				L5: CsRHHH
					L6: CsCHHH
					L6: CsOHHH
				L5: CsRRHH
					L6: CsCCHH
					L6: CsCOHH
					L6: CsOOHH
				L5: CsRRRH
					L6: CsCCCH
					L6: CsCCOH
					L6: CsCOOH
					L6: CsOOOH
			L4: Csrad_H
				L5: C_methyl
				L5: CsRHjH
					L6: CsCHjH
					L6: CsOHjH
				L5: CsRRjH
					L6: CsCCjH
					L6: CsCOjH
					L6: CsOOjH
			L4: CsbiradH
				L5: Cs_singletH
					L6: Cs_singletHH
					L6: Cs_singletRH
						L7: C_singletCH
						L7: C_singletOH
				L5: Cs_tripletH
					L6: Cs_tripletHH
					L6: Cs_tripletRH
						L7: Cs_tripletCH
						L7: Cs_tripletOH
			L4: CstriradH
				L5: Cdoublet_H
				L5: Cquartet_H
		L3: Cd_H
			L4: Cdnorad_H
				L5: Cd(=C)RH
					L6: Cd(=C)HH
					L6: Cd(=C)CH
					L6: Cd(=C)OH
				L5: Cd(=O)RH
					L6: Cd(=O)HH
					L6: Cd(=O)CH
					L6: Cd(=O)OH
			L4: Cdrad_H
				L5: Cd(=C)jH
				L5: Cd(=O)jH
		L3: Ct_H
			L4: CtCH
		L3: Cb_H
	L2: O_H
		L3: OradH
		L3: ORH
			L4: OHH
			L4: OCH
			L4: OOH		
L1: Y_rad_birad_trirad_quadrad
	L2: Hrad
	L2: Orad
		L3: OjR
			L4: OjH
			L4: OjC
			L4: OjO
		L3: O_atom_triplet
	L2: Crad
		L3: Cj
			L4: Csj
				L5: Cs_methyl
				L5: CsRHHj
					L6: CsCHHj
					L6: CsOHHj
				L5: CsRRHj
					L6: CsCCHj
					L6: CsCOHj
					L6: CsOOHj
				L5: CsRRRj
					L6: CsCCCj
					L6: CsCCOj
					L6: CsCOOj
					L6: CsOOOj
			L4: Cdj
				L5: Cd(=C)Rj
					L6: Cd(=C)Hj
					L6: Cd(=C)Cj
					L6: Cd(=C)Oj
				L5: Cd(=O)Rj
					L6: Cd(=O)Hj
					L6: Cd(=O)Cj
					L6: Cd(=O)Oj
			L4: Ctj
				L5: CtCj
			L4: Cbj
		L3: Cjj
			L4: Csjj
				L5: C_singletRR
				L5: C_tripletRR
			L4: Cdjj
				L5: C_singletR
				L5: C_tripletR
		L3: Cjjj
			L4: C_doubletR
			L4: C_quartetR
		L3: Cjjjj
			L4: C_quintet
			L4: C_triplet
"""
)

