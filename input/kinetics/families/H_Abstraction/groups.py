#!/usr/bin/env python
# encoding: utf-8

name = "H_Abstraction/groups"
shortDesc = ""
longDesc = """

"""

template(reactants=["X_H", "Y_rad_birad"], products=["X_H", "Y_rad_birad"], ownReverse=True)

recipe(actions=[
    ['BREAK_BOND', '*1', 'S', '*2'],
    ['FORM_BOND', '*2', 'S', '*3'],
    ['GAIN_RADICAL', '*1', '1'],
    ['LOSE_RADICAL', '*3', '1'],
])

entry(
    index = 1,
    label = "X_H",
    group = 
"""
1  *1 R 0 {2,S}
2  *2 H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0002269,0.0553017,1.62283,16.2981,320.872,2080.87,29949.7,130306],"m^3/(mol*s)","*|/",[11123.2,1290.32,403.152,200.205,93.2277,63.4879,43.2027,39.4158])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [315, 315, 315, 315, 315, 315, 315, 315] rates.
[<Entry index=10 label="H2O2">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=10 label="H2O2">, <Entry index=120 label="InChI=1/C4H9O/c1-2-3-4-5/h2,5H,3-4H2,1H3">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=69 label="H_rad">]
[<Entry index=17 label="Cd/H/NonDeO">, <Entry index=69 label="H_rad">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=67 label="CH2_triplet">]
[<Entry index=4 label="Ct_H">, <Entry index=71 label="O2b">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=71 label="O2b">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=11 label="O/H/OneDe">, <Entry index=69 label="H_rad">]
[<Entry index=26 label="C_methane">, <Entry index=94 label="Cb_rad">]
[<Entry index=36 label="C/H3/Cb">, <Entry index=101 label="C_methyl">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=101 label="C_methyl">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=109 label="InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3">]
[<Entry index=21 label="CO_pri">, <Entry index=69 label="H_rad">]
[<Entry index=6 label="O_pri">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=26 label="C_methane">, <Entry index=98 label="CO_rad/NonDe">]
[<Entry index=10 label="H2O2">, <Entry index=121 label="InChI=1/C4H9O/c1-2-3-4-5/h3,5H,2,4H2,1H3">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=75 label="O_pri_rad">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=3 label="H2">, <Entry index=101 label="C_methyl">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=126 label="InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3">]
[<Entry index=6 label="O_pri">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=49 label="InChI=1/C4H8/c1-3-4-2/h3H,1,4H2,2H3">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=69 label="H_rad">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=71 label="O2b">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=69 label="H_rad">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=67 label="CH2_triplet">]
[<Entry index=10 label="H2O2">, <Entry index=106 label="InChI=1/C4H9O/c1-3-4(2)5/h4-5H,2-3H2,1H3">]
[<Entry index=19 label="Cb_H">, <Entry index=69 label="H_rad">]
[<Entry index=37 label="C/H3/CO">, <Entry index=75 label="O_pri_rad">]
[<Entry index=26 label="C_methane">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=38 label="C/H3/O">, <Entry index=69 label="H_rad">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=78 label="InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=101 label="C_methyl">]
[<Entry index=14 label="Cd_pri">, <Entry index=75 label="O_pri_rad">]
[<Entry index=6 label="O_pri">, <Entry index=69 label="H_rad">]
[<Entry index=6 label="O_pri">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=101 label="C_methyl">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=101 label="C_methyl">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=89 label="Cd_rad/NonDeC">]
[<Entry index=3 label="H2">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=4 label="Ct_H">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=32 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=78 label="InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3">]
[<Entry index=21 label="CO_pri">, <Entry index=67 label="CH2_triplet">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=98 label="CO_rad/NonDe">]
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=90 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=73 label="Ct_rad">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=96 label="CO_pri_rad">]
[<Entry index=3 label="H2">, <Entry index=94 label="Cb_rad">]
[<Entry index=10 label="H2O2">, <Entry index=89 label="Cd_rad/NonDeC">]
[<Entry index=26 label="C_methane">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=26 label="C_methane">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=98 label="CO_rad/NonDe">]
[<Entry index=18 label="Cd/H/OneDe">, <Entry index=101 label="C_methyl">]
[<Entry index=19 label="Cb_H">, <Entry index=71 label="O2b">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=101 label="C_methyl">]
[<Entry index=26 label="C_methane">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=10 label="H2O2">, <Entry index=111 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=10 label="H2O2">, <Entry index=105 label="InChI=1/C4H9O/c1-2-3-4-5/h5H,1-4H2">]
[<Entry index=14 label="Cd_pri">, <Entry index=140 label="C_rad/Cs2">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=71 label="O2b">]
[<Entry index=6 label="O_pri">, <Entry index=96 label="CO_pri_rad">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=113 label="C_rad/H2/Ct">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=75 label="O_pri_rad">]
[<Entry index=29 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=109 label="InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3">]
[<Entry index=11 label="O/H/OneDe">, <Entry index=101 label="C_methyl">]
[<Entry index=51 label="C/H2/TwoDe">, <Entry index=101 label="C_methyl">]
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=130 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c">]
[<Entry index=26 label="C_methane">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=26 label="C_methane">, <Entry index=71 label="O2b">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=10 label="H2O2">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=69 label="H_rad">]
[<Entry index=6 label="O_pri">, <Entry index=71 label="O2b">]
[<Entry index=26 label="C_methane">, <Entry index=96 label="CO_pri_rad">]
[<Entry index=58 label="C/H/Cs2">, <Entry index=69 label="H_rad">]
[<Entry index=14 label="Cd_pri">, <Entry index=129 label="C_rad/H/OneDeC">]
[<Entry index=29 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=78 label="InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3">]
[<Entry index=19 label="Cb_H">, <Entry index=75 label="O_pri_rad">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=26 label="C_methane">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=93 label="Cd_rad/OneDe">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=69 label="H_rad">]
[<Entry index=6 label="O_pri">, <Entry index=75 label="O_pri_rad">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=129 label="C_rad/H/OneDeC">]
[<Entry index=10 label="H2O2">, <Entry index=87 label="InChI=1/C4H7/c1-3-4-2/h1,3H,4H2,2H3">]
[<Entry index=14 label="Cd_pri">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=69 label="H_rad">]
[<Entry index=14 label="Cd_pri">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=21 label="CO_pri">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=3 label="H2">, <Entry index=98 label="CO_rad/NonDe">]
[<Entry index=21 label="CO_pri">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=130 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c">]
[<Entry index=26 label="C_methane">, <Entry index=69 label="H_rad">]
[<Entry index=47 label="C/H2/OneDeC">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=21 label="CO_pri">, <Entry index=98 label="CO_rad/NonDe">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=83 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/o">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=14 label="Cd_pri">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=73 label="Ct_rad">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=73 label="Ct_rad">]
[<Entry index=4 label="Ct_H">, <Entry index=101 label="C_methyl">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=75 label="O_pri_rad">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=93 label="Cd_rad/OneDe">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=101 label="C_methyl">]
[<Entry index=26 label="C_methane">, <Entry index=73 label="Ct_rad">]
[<Entry index=21 label="CO_pri">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=3 label="H2">, <Entry index=113 label="C_rad/H2/Ct">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=96 label="CO_pri_rad">]
[<Entry index=59 label="InChI=1/C4H8O/c1-4(2)3-5/h3-4H,1-2H3">, <Entry index=69 label="H_rad">]
[<Entry index=3 label="H2">, <Entry index=73 label="Ct_rad">]
[<Entry index=14 label="Cd_pri">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=26 label="C_methane">, <Entry index=101 label="C_methyl">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=26 label="C_methane">, <Entry index=72 label="C2b">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=86 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=73 label="Ct_rad">]
[<Entry index=6 label="O_pri">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=21 label="CO_pri">, <Entry index=71 label="O2b">]
[<Entry index=10 label="H2O2">, <Entry index=125 label="InChI=1/C4H9O/c1-2-3-4-5/h4-5H,2-3H2,1H3">]
[<Entry index=14 label="Cd_pri">, <Entry index=93 label="Cd_rad/OneDe">]
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=104 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=119 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=89 label="Cd_rad/NonDeC">]
[<Entry index=21 label="CO_pri">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=140 label="C_rad/Cs2">]
[<Entry index=14 label="Cd_pri">, <Entry index=113 label="C_rad/H2/Ct">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=14 label="Cd_pri">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=104 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=35 label="C/H3/Ct">, <Entry index=101 label="C_methyl">]
[<Entry index=32 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=126 label="InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=34 label="InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=10 label="H2O2">, <Entry index=91 label="InChI=1/C4H7/c1-3-4-2/h3H,1-2H3">]
[<Entry index=3 label="H2">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=14 label="Cd_pri">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=6 label="O_pri">, <Entry index=101 label="C_methyl">]
[<Entry index=3 label="H2">, <Entry index=93 label="Cd_rad/OneDe">]
[<Entry index=38 label="C/H3/O">, <Entry index=75 label="O_pri_rad">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=21 label="CO_pri">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=94 label="Cb_rad">]
[<Entry index=12 label="Orad_O_H">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=3 label="H2">, <Entry index=89 label="Cd_rad/NonDeC">]
[<Entry index=3 label="H2">, <Entry index=129 label="C_rad/H/OneDeC">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=75 label="O_pri_rad">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=18 label="Cd/H/OneDe">, <Entry index=69 label="H_rad">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=73 label="Ct_rad">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=69 label="H_rad">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=19 label="Cb_H">, <Entry index=101 label="C_methyl">]
[<Entry index=3 label="H2">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=71 label="O2b">]
[<Entry index=41 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=136 label="InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3">]
[<Entry index=32 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=109 label="InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3">]
[<Entry index=14 label="Cd_pri">, <Entry index=89 label="Cd_rad/NonDeC">]
[<Entry index=4 label="Ct_H">, <Entry index=75 label="O_pri_rad">]
[<Entry index=48 label="InChI=1/C3H6O/c1-2-3-4/h3H,2H2,1H3/beta">, <Entry index=109 label="InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3">]
[<Entry index=10 label="H2O2">, <Entry index=108 label="InChI=1/C4H9O/c1-4(2,3)5/h5H,1H2,2-3H3">]
[<Entry index=10 label="H2O2">, <Entry index=80 label="OOCH3">]
[<Entry index=10 label="H2O2">, <Entry index=81 label="O_rad/OneDe">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=129 label="C_rad/H/OneDeC">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=10 label="H2O2">, <Entry index=138 label="InChI=1/C4H9O/c1-3-4(2)5/h5H,3H2,1-2H3">]
[<Entry index=30 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/gamma">, <Entry index=90 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=3 label="H2">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=3 label="H2">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=47 label="C/H2/OneDeC">, <Entry index=101 label="C_methyl">]
[<Entry index=38 label="C/H3/O">, <Entry index=101 label="C_methyl">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=136 label="InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=47 label="C/H2/OneDeC">, <Entry index=69 label="H_rad">]
[<Entry index=51 label="C/H2/TwoDe">, <Entry index=69 label="H_rad">]
[<Entry index=21 label="CO_pri">, <Entry index=101 label="C_methyl">]
[<Entry index=35 label="C/H3/Ct">, <Entry index=69 label="H_rad">]
[<Entry index=21 label="CO_pri">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=14 label="Cd_pri">, <Entry index=101 label="C_methyl">]
[<Entry index=10 label="H2O2">, <Entry index=107 label="InChI=1/C4H9O/c1-3-4(2)5/h4-5H,1,3H2,2H3">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=140 label="C_rad/Cs2">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=98 label="CO_rad/NonDe">]
[<Entry index=1 label="X_H">, <Entry index=2 label="Y_rad_birad">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=71 label="O2b">]
[<Entry index=58 label="C/H/Cs2">, <Entry index=101 label="C_methyl">]
[<Entry index=49 label="InChI=1/C4H8/c1-3-4-2/h3H,1,4H2,2H3">, <Entry index=80 label="OOCH3">]
[<Entry index=3 label="H2">, <Entry index=140 label="C_rad/Cs2">]
[<Entry index=3 label="H2">, <Entry index=69 label="H_rad">]
[<Entry index=4 label="Ct_H">, <Entry index=69 label="H_rad">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=67 label="CH2_triplet">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=21 label="CO_pri">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=32 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=136 label="InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=10 label="H2O2">, <Entry index=82 label="InChI=1/C4H7O/c1-2-3-4-5/h3-4H,2H2,1H3">]
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=119 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=113 label="C_rad/H2/Ct">]
[<Entry index=21 label="CO_pri">, <Entry index=75 label="O_pri_rad">]
[<Entry index=21 label="CO_pri">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=75 label="O_pri_rad">]
[<Entry index=62 label="C/H/Cs">, <Entry index=101 label="C_methyl">]
[<Entry index=10 label="H2O2">, <Entry index=122 label="InChI=1/C4H9O/c1-3-4(2)5/h3-5H,1-2H3">]
[<Entry index=14 label="Cd_pri">, <Entry index=69 label="H_rad">]
[<Entry index=19 label="Cb_H">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=3 label="H2">, <Entry index=71 label="O2b">]
[<Entry index=14 label="Cd_pri">, <Entry index=71 label="O2b">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=96 label="CO_pri_rad">]
[<Entry index=3 label="H2">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=101 label="C_methyl">]
[<Entry index=26 label="C_methane">, <Entry index=75 label="O_pri_rad">]
[<Entry index=26 label="C_methane">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=3 label="H2">, <Entry index=96 label="CO_pri_rad">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=75 label="O_pri_rad">]
[<Entry index=3 label="H2">, <Entry index=75 label="O_pri_rad">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=116 label="C_rad/H2/O">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=118 label="C_rad/H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 2,
    label = "Y_rad_birad",
    group = "OR{Y_1centerbirad, Y_rad}",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 3,
    label = "H2",
    group = 
"""
1  *1 H 0 {2,S}
2  *2 H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.00416538,0.0189178,0.0447561,0.07703,0.143664,0.199256,0.278846,0.304883],"m^3/(mol*s)","*|/",[1792.12,260.148,88.5361,45.5481,22.057,15.854,13.4569,15.7795])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [24, 24, 24, 24, 24, 24, 24, 24] rates.
[<Entry index=3 label="H2">, <Entry index=89 label="Cd_rad/NonDeC">]
[<Entry index=3 label="H2">, <Entry index=94 label="Cb_rad">]
[<Entry index=3 label="H2">, <Entry index=140 label="C_rad/Cs2">]
[<Entry index=3 label="H2">, <Entry index=69 label="H_rad">]
[<Entry index=3 label="H2">, <Entry index=96 label="CO_pri_rad">]
[<Entry index=3 label="H2">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=3 label="H2">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=3 label="H2">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=3 label="H2">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=3 label="H2">, <Entry index=129 label="C_rad/H/OneDeC">]
[<Entry index=3 label="H2">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=3 label="H2">, <Entry index=101 label="C_methyl">]
[<Entry index=3 label="H2">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=3 label="H2">, <Entry index=71 label="O2b">]
[<Entry index=3 label="H2">, <Entry index=113 label="C_rad/H2/Ct">]
[<Entry index=3 label="H2">, <Entry index=98 label="CO_rad/NonDe">]
[<Entry index=3 label="H2">, <Entry index=93 label="Cd_rad/OneDe">]
[<Entry index=3 label="H2">, <Entry index=75 label="O_pri_rad">]
[<Entry index=3 label="H2">, <Entry index=73 label="Ct_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 4,
    label = "Ct_H",
    group = 
"""
1  *1 C 0 {2,T} {3,S}
2     C 0 {1,T}
3  *2 H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([7.64709e-12,1.08738e-08,8.16066e-07,1.41603e-05,0.00047959,0.00382263,0.0561499,0.201974],"m^3/(mol*s)","*|/",[7.16681e+12,6.04838e+10,4.32041e+09,8.50327e+08,1.36321e+08,5.21995e+07,1.81255e+07,1.22566e+07])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [5, 5, 5, 5, 5, 5, 5, 5] rates.
[<Entry index=4 label="Ct_H">, <Entry index=71 label="O2b">]
[<Entry index=4 label="Ct_H">, <Entry index=101 label="C_methyl">]
[<Entry index=4 label="Ct_H">, <Entry index=75 label="O_pri_rad">]
[<Entry index=4 label="Ct_H">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=4 label="Ct_H">, <Entry index=69 label="H_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 5,
    label = "O_H",
    group = 
"""
1  *1 O 0 {2,S} {3,S}
2  *2 H 0 {1,S}
3     R 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([12.9872,3.84411,1.95524,1.29172,0.820526,0.65991,0.554412,0.556856],"m^3/(mol*s)","*|/",[185722,7337.96,1164.49,363.585,94.3944,45.6885,20.423,15.486])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [44, 44, 44, 44, 44, 44, 44, 44] rates.
[<Entry index=10 label="H2O2">, <Entry index=120 label="InChI=1/C4H9O/c1-2-3-4-5/h2,5H,3-4H2,1H3">]
[<Entry index=10 label="H2O2">, <Entry index=81 label="O_rad/OneDe">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=69 label="H_rad">]
[<Entry index=6 label="O_pri">, <Entry index=101 label="C_methyl">]
[<Entry index=10 label="H2O2">, <Entry index=138 label="InChI=1/C4H9O/c1-3-4(2)5/h5H,3H2,1-2H3">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=6 label="O_pri">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=6 label="O_pri">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=10 label="H2O2">, <Entry index=125 label="InChI=1/C4H9O/c1-2-3-4-5/h4-5H,2-3H2,1H3">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=11 label="O/H/OneDe">, <Entry index=69 label="H_rad">]
[<Entry index=10 label="H2O2">, <Entry index=105 label="InChI=1/C4H9O/c1-2-3-4-5/h5H,1-4H2">]
[<Entry index=6 label="O_pri">, <Entry index=96 label="CO_pri_rad">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=10 label="H2O2">, <Entry index=87 label="InChI=1/C4H7/c1-3-4-2/h1,3H,4H2,2H3">]
[<Entry index=11 label="O/H/OneDe">, <Entry index=101 label="C_methyl">]
[<Entry index=10 label="H2O2">, <Entry index=80 label="OOCH3">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=73 label="Ct_rad">]
[<Entry index=10 label="H2O2">, <Entry index=91 label="InChI=1/C4H7/c1-3-4-2/h3H,1-2H3">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=6 label="O_pri">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=6 label="O_pri">, <Entry index=69 label="H_rad">]
[<Entry index=10 label="H2O2">, <Entry index=107 label="InChI=1/C4H9O/c1-3-4(2)5/h4-5H,1,3H2,2H3">]
[<Entry index=6 label="O_pri">, <Entry index=71 label="O2b">]
[<Entry index=10 label="H2O2">, <Entry index=111 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=6 label="O_pri">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=10 label="H2O2">, <Entry index=106 label="InChI=1/C4H9O/c1-3-4(2)5/h4-5H,2-3H2,1H3">]
[<Entry index=10 label="H2O2">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=6 label="O_pri">, <Entry index=75 label="O_pri_rad">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=67 label="CH2_triplet">]
[<Entry index=10 label="H2O2">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=101 label="C_methyl">]
[<Entry index=10 label="H2O2">, <Entry index=82 label="InChI=1/C4H7O/c1-2-3-4-5/h3-4H,2H2,1H3">]
[<Entry index=10 label="H2O2">, <Entry index=89 label="Cd_rad/NonDeC">]
[<Entry index=10 label="H2O2">, <Entry index=121 label="InChI=1/C4H9O/c1-2-3-4-5/h3,5H,2,4H2,1H3">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=75 label="O_pri_rad">]
[<Entry index=10 label="H2O2">, <Entry index=122 label="InChI=1/C4H9O/c1-3-4(2)5/h3-5H,1-2H3">]
[<Entry index=10 label="H2O2">, <Entry index=108 label="InChI=1/C4H9O/c1-4(2,3)5/h5H,1H2,2-3H3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 6,
    label = "O_pri",
    group = 
"""
1  *1 O 0 {2,S} {3,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.21132e-07,4.5963e-06,4.24564e-05,0.000192139,0.00133216,0.00443777,0.0241281,0.0603305],"m^3/(mol*s)","*|/",[1.69068e+08,852158,41554.3,6133.82,668.26,203.619,55.5713,36.247])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [11, 11, 11, 11, 11, 11, 11, 11] rates.
[<Entry index=6 label="O_pri">, <Entry index=75 label="O_pri_rad">]
[<Entry index=6 label="O_pri">, <Entry index=101 label="C_methyl">]
[<Entry index=6 label="O_pri">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=6 label="O_pri">, <Entry index=69 label="H_rad">]
[<Entry index=6 label="O_pri">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=6 label="O_pri">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=6 label="O_pri">, <Entry index=71 label="O2b">]
[<Entry index=6 label="O_pri">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=6 label="O_pri">, <Entry index=96 label="CO_pri_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 7,
    label = "O_sec",
    group = 
"""
1  *1 O 0 {2,S} {3,S}
2  *2 H 0 {1,S}
3     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1757.94,143.479,33.8048,13.4006,4.51362,2.48936,1.27399,1.00448],"m^3/(mol*s)","*|/",[32649,2298.07,506.892,194.717,64.0176,35.0085,17.7065,13.8945])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [33, 33, 33, 33, 33, 33, 33, 33] rates.
[<Entry index=10 label="H2O2">, <Entry index=120 label="InChI=1/C4H9O/c1-2-3-4-5/h2,5H,3-4H2,1H3">]
[<Entry index=10 label="H2O2">, <Entry index=81 label="O_rad/OneDe">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=69 label="H_rad">]
[<Entry index=10 label="H2O2">, <Entry index=121 label="InChI=1/C4H9O/c1-2-3-4-5/h3,5H,2,4H2,1H3">]
[<Entry index=10 label="H2O2">, <Entry index=138 label="InChI=1/C4H9O/c1-3-4(2)5/h5H,3H2,1-2H3">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=10 label="H2O2">, <Entry index=125 label="InChI=1/C4H9O/c1-2-3-4-5/h4-5H,2-3H2,1H3">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=11 label="O/H/OneDe">, <Entry index=69 label="H_rad">]
[<Entry index=10 label="H2O2">, <Entry index=105 label="InChI=1/C4H9O/c1-2-3-4-5/h5H,1-4H2">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=10 label="H2O2">, <Entry index=87 label="InChI=1/C4H7/c1-3-4-2/h1,3H,4H2,2H3">]
[<Entry index=11 label="O/H/OneDe">, <Entry index=101 label="C_methyl">]
[<Entry index=10 label="H2O2">, <Entry index=80 label="OOCH3">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=73 label="Ct_rad">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=10 label="H2O2">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=10 label="H2O2">, <Entry index=107 label="InChI=1/C4H9O/c1-3-4(2)5/h4-5H,1,3H2,2H3">]
[<Entry index=10 label="H2O2">, <Entry index=91 label="InChI=1/C4H7/c1-3-4-2/h3H,1-2H3">]
[<Entry index=10 label="H2O2">, <Entry index=111 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=10 label="H2O2">, <Entry index=106 label="InChI=1/C4H9O/c1-3-4(2)5/h4-5H,2-3H2,1H3">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=67 label="CH2_triplet">]
[<Entry index=10 label="H2O2">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=101 label="C_methyl">]
[<Entry index=10 label="H2O2">, <Entry index=82 label="InChI=1/C4H7O/c1-2-3-4-5/h3-4H,2H2,1H3">]
[<Entry index=10 label="H2O2">, <Entry index=89 label="Cd_rad/NonDeC">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=75 label="O_pri_rad">]
[<Entry index=10 label="H2O2">, <Entry index=122 label="InChI=1/C4H9O/c1-3-4(2)5/h3-5H,1-2H3">]
[<Entry index=10 label="H2O2">, <Entry index=108 label="InChI=1/C4H9O/c1-4(2,3)5/h5H,1H2,2-3H3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 8,
    label = "O/H/NonDeC",
    group = 
"""
1  *1 O 0 {2,S} {3,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([57.3699,13.0439,5.51831,3.16922,1.63876,1.13506,0.739219,0.625806],"m^3/(mol*s)","*|/",[345811,15984.7,2772.83,909.604,245.026,118.878,52.9307,41.7392])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [12, 12, 12, 12, 12, 12, 12, 12] rates.
[<Entry index=8 label="O/H/NonDeC">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=67 label="CH2_triplet">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=73 label="Ct_rad">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=69 label="H_rad">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=101 label="C_methyl">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=75 label="O_pri_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 9,
    label = "O/H/NonDeO",
    group = 
"""
1  *1 O 0 {2,S} {3,S}
2  *2 H 0 {1,S}
3     O 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([15712.9,636.358,100.382,30.8461,7.73116,3.64049,1.57245,1.17647],"m^3/(mol*s)","*|/",[6173.59,460.012,103.355,39.9961,13.3394,7.48582,4.15141,3.50841])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [18, 18, 18, 18, 18, 18, 18, 18] rates.
[<Entry index=10 label="H2O2">, <Entry index=120 label="InChI=1/C4H9O/c1-2-3-4-5/h2,5H,3-4H2,1H3">]
[<Entry index=10 label="H2O2">, <Entry index=87 label="InChI=1/C4H7/c1-3-4-2/h1,3H,4H2,2H3">]
[<Entry index=10 label="H2O2">, <Entry index=81 label="O_rad/OneDe">]
[<Entry index=10 label="H2O2">, <Entry index=121 label="InChI=1/C4H9O/c1-2-3-4-5/h3,5H,2,4H2,1H3">]
[<Entry index=10 label="H2O2">, <Entry index=122 label="InChI=1/C4H9O/c1-3-4(2)5/h3-5H,1-2H3">]
[<Entry index=10 label="H2O2">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=10 label="H2O2">, <Entry index=89 label="Cd_rad/NonDeC">]
[<Entry index=10 label="H2O2">, <Entry index=125 label="InChI=1/C4H9O/c1-2-3-4-5/h4-5H,2-3H2,1H3">]
[<Entry index=10 label="H2O2">, <Entry index=91 label="InChI=1/C4H7/c1-3-4-2/h3H,1-2H3">]
[<Entry index=10 label="H2O2">, <Entry index=111 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=10 label="H2O2">, <Entry index=107 label="InChI=1/C4H9O/c1-3-4(2)5/h4-5H,1,3H2,2H3">]
[<Entry index=10 label="H2O2">, <Entry index=106 label="InChI=1/C4H9O/c1-3-4(2)5/h4-5H,2-3H2,1H3">]
[<Entry index=10 label="H2O2">, <Entry index=82 label="InChI=1/C4H7O/c1-2-3-4-5/h3-4H,2H2,1H3">]
[<Entry index=10 label="H2O2">, <Entry index=105 label="InChI=1/C4H9O/c1-2-3-4-5/h5H,1-4H2">]
[<Entry index=10 label="H2O2">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=10 label="H2O2">, <Entry index=108 label="InChI=1/C4H9O/c1-4(2,3)5/h5H,1H2,2-3H3">]
[<Entry index=10 label="H2O2">, <Entry index=138 label="InChI=1/C4H9O/c1-3-4(2)5/h5H,3H2,1-2H3">]
[<Entry index=10 label="H2O2">, <Entry index=80 label="OOCH3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 10,
    label = "H2O2",
    group = 
"""
1  *1 O 0 {2,S} {3,S}
2     O 0 {1,S} {4,S}
3  *2 H 0 {1,S}
4     H 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([15712.9,636.358,100.382,30.8461,7.73116,3.64049,1.57245,1.17647],"m^3/(mol*s)","*|/",[6173.59,460.012,103.355,39.9961,13.3394,7.48582,4.15141,3.50841])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [18, 18, 18, 18, 18, 18, 18, 18] rates.
[<Entry index=10 label="H2O2">, <Entry index=120 label="InChI=1/C4H9O/c1-2-3-4-5/h2,5H,3-4H2,1H3">]
[<Entry index=10 label="H2O2">, <Entry index=87 label="InChI=1/C4H7/c1-3-4-2/h1,3H,4H2,2H3">]
[<Entry index=10 label="H2O2">, <Entry index=81 label="O_rad/OneDe">]
[<Entry index=10 label="H2O2">, <Entry index=121 label="InChI=1/C4H9O/c1-2-3-4-5/h3,5H,2,4H2,1H3">]
[<Entry index=10 label="H2O2">, <Entry index=122 label="InChI=1/C4H9O/c1-3-4(2)5/h3-5H,1-2H3">]
[<Entry index=10 label="H2O2">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=10 label="H2O2">, <Entry index=89 label="Cd_rad/NonDeC">]
[<Entry index=10 label="H2O2">, <Entry index=125 label="InChI=1/C4H9O/c1-2-3-4-5/h4-5H,2-3H2,1H3">]
[<Entry index=10 label="H2O2">, <Entry index=91 label="InChI=1/C4H7/c1-3-4-2/h3H,1-2H3">]
[<Entry index=10 label="H2O2">, <Entry index=111 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=10 label="H2O2">, <Entry index=107 label="InChI=1/C4H9O/c1-3-4(2)5/h4-5H,1,3H2,2H3">]
[<Entry index=10 label="H2O2">, <Entry index=106 label="InChI=1/C4H9O/c1-3-4(2)5/h4-5H,2-3H2,1H3">]
[<Entry index=10 label="H2O2">, <Entry index=82 label="InChI=1/C4H7O/c1-2-3-4-5/h3-4H,2H2,1H3">]
[<Entry index=10 label="H2O2">, <Entry index=105 label="InChI=1/C4H9O/c1-2-3-4-5/h5H,1-4H2">]
[<Entry index=10 label="H2O2">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=10 label="H2O2">, <Entry index=108 label="InChI=1/C4H9O/c1-4(2,3)5/h5H,1H2,2-3H3">]
[<Entry index=10 label="H2O2">, <Entry index=138 label="InChI=1/C4H9O/c1-3-4(2)5/h5H,3H2,1-2H3">]
[<Entry index=10 label="H2O2">, <Entry index=80 label="OOCH3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 11,
    label = "O/H/OneDe",
    group = 
"""
1  *1 O 0 {2,S} {3,S}
2  *2 H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([3.06432,2.67612,2.46352,2.32894,2.16715,2.07242,1.94627,1.88136],"m^3/(mol*s)","*|/",[2.36147e+17,3.84518e+13,2.45823e+11,9.37792e+09,1.81113e+08,1.81831e+07,866105,176945])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [3, 3, 3, 3, 3, 3, 3, 3] rates.
[<Entry index=11 label="O/H/OneDe">, <Entry index=101 label="C_methyl">]
[<Entry index=11 label="O/H/OneDe">, <Entry index=69 label="H_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 12,
    label = "Orad_O_H",
    group = 
"""
1  *1 O 0 {2,S} {3,S}
2  *2 H 0 {1,S}
3     O 1 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.15522e+10,1.67064e+07,298838,19121.9,546.51,58.5681,2.40618,0.412008],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=12 label="Orad_O_H">, <Entry index=79 label="O_rad/NonDeO">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 13,
    label = "Cd_H",
    group = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     R 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.88699e-05,0.000497069,0.00340004,0.0119315,0.054666,0.130922,0.385248,0.618002],"m^3/(mol*s)","*|/",[485296,18792.9,2976.67,930.262,239.379,112.542,43.8678,27.7912])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [41, 41, 41, 41, 41, 41, 41, 41] rates.
[<Entry index=17 label="Cd/H/NonDeO">, <Entry index=69 label="H_rad">]
[<Entry index=18 label="Cd/H/OneDe">, <Entry index=101 label="C_methyl">]
[<Entry index=14 label="Cd_pri">, <Entry index=89 label="Cd_rad/NonDeC">]
[<Entry index=14 label="Cd_pri">, <Entry index=140 label="C_rad/Cs2">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=71 label="O2b">]
[<Entry index=14 label="Cd_pri">, <Entry index=113 label="C_rad/H2/Ct">]
[<Entry index=14 label="Cd_pri">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=14 label="Cd_pri">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=69 label="H_rad">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=73 label="Ct_rad">]
[<Entry index=14 label="Cd_pri">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=14 label="Cd_pri">, <Entry index=129 label="C_rad/H/OneDeC">]
[<Entry index=14 label="Cd_pri">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=14 label="Cd_pri">, <Entry index=75 label="O_pri_rad">]
[<Entry index=18 label="Cd/H/OneDe">, <Entry index=69 label="H_rad">]
[<Entry index=14 label="Cd_pri">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=14 label="Cd_pri">, <Entry index=69 label="H_rad">]
[<Entry index=14 label="Cd_pri">, <Entry index=71 label="O2b">]
[<Entry index=14 label="Cd_pri">, <Entry index=93 label="Cd_rad/OneDe">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=101 label="C_methyl">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=75 label="O_pri_rad">]
[<Entry index=14 label="Cd_pri">, <Entry index=101 label="C_methyl">]
[<Entry index=14 label="Cd_pri">, <Entry index=110 label="C_rad/H2/Cd">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 14,
    label = "Cd_pri",
    group = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([5.16195e-07,3.65537e-05,0.000446617,0.00228711,0.0165459,0.0514358,0.208336,0.383476],"m^3/(mol*s)","*|/",[4.21074e+06,77261.6,7988.42,1913.5,367.105,149.816,51.5666,31.7834])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [25, 25, 25, 25, 25, 25, 25, 25] rates.
[<Entry index=14 label="Cd_pri">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=14 label="Cd_pri">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=14 label="Cd_pri">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=14 label="Cd_pri">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=14 label="Cd_pri">, <Entry index=69 label="H_rad">]
[<Entry index=14 label="Cd_pri">, <Entry index=101 label="C_methyl">]
[<Entry index=14 label="Cd_pri">, <Entry index=71 label="O2b">]
[<Entry index=14 label="Cd_pri">, <Entry index=89 label="Cd_rad/NonDeC">]
[<Entry index=14 label="Cd_pri">, <Entry index=75 label="O_pri_rad">]
[<Entry index=14 label="Cd_pri">, <Entry index=129 label="C_rad/H/OneDeC">]
[<Entry index=14 label="Cd_pri">, <Entry index=93 label="Cd_rad/OneDe">]
[<Entry index=14 label="Cd_pri">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=14 label="Cd_pri">, <Entry index=140 label="C_rad/Cs2">]
[<Entry index=14 label="Cd_pri">, <Entry index=113 label="C_rad/H2/Ct">]
[<Entry index=14 label="Cd_pri">, <Entry index=110 label="C_rad/H2/Cd">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 15,
    label = "Cd_sec",
    group = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.022225,0.0838717,0.183506,0.306433,0.572217,0.820854,1.28922,1.57842],"m^3/(mol*s)","*|/",[38306,4587.3,1350.93,609.992,228.212,125.436,53.752,33.6755])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [16, 16, 16, 16, 16, 16, 16, 16] rates.
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=69 label="H_rad">]
[<Entry index=17 label="Cd/H/NonDeO">, <Entry index=69 label="H_rad">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=18 label="Cd/H/OneDe">, <Entry index=101 label="C_methyl">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=101 label="C_methyl">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=75 label="O_pri_rad">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=73 label="Ct_rad">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=71 label="O2b">]
[<Entry index=18 label="Cd/H/OneDe">, <Entry index=69 label="H_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 16,
    label = "Cd/H/NonDeC",
    group = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.000734383,0.00502686,0.0159484,0.0344451,0.0902342,0.160884,0.348167,0.512572],"m^3/(mol*s)","*|/",[40496.7,4015.14,1105.98,489.207,183.066,101.392,43.1236,26.0979])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [10, 10, 10, 10, 10, 10, 10, 10] rates.
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=69 label="H_rad">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=101 label="C_methyl">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=75 label="O_pri_rad">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=73 label="Ct_rad">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=71 label="O2b">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 17,
    label = "Cd/H/NonDeO",
    group = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     O 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([4.35149,6.71739,8.54057,9.88857,11.5937,12.4975,13.2247,13.1459],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=17 label="Cd/H/NonDeO">, <Entry index=69 label="H_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 18,
    label = "Cd/H/OneDe",
    group = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([8.44726,11.2458,12.8099,13.5921,13.9368,13.573,11.9921,10.5131],"m^3/(mol*s)","*|/",[2.39224e+06,183423,38744.7,13510,3478.96,1485.67,445.549,236.276])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [5, 5, 5, 5, 5, 5, 5, 5] rates.
[<Entry index=18 label="Cd/H/OneDe">, <Entry index=69 label="H_rad">]
[<Entry index=18 label="Cd/H/OneDe">, <Entry index=101 label="C_methyl">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 19,
    label = "Cb_H",
    group = 
"""
1  *1 Cb 0 {2,B} {3,B} {4,S}
2     {Cb,Cbf} 0 {1,B}
3     {Cb,Cbf} 0 {1,B}
4  *2 H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.000369037,0.00368803,0.0138916,0.032424,0.0876526,0.15067,0.275871,0.340335],"m^3/(mol*s)","*|/",[3.7925e+06,58281.4,5679.8,1432.05,388.366,263.998,325.361,534.749])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [6, 6, 6, 6, 6, 6, 6, 6] rates.
[<Entry index=19 label="Cb_H">, <Entry index=75 label="O_pri_rad">]
[<Entry index=19 label="Cb_H">, <Entry index=69 label="H_rad">]
[<Entry index=19 label="Cb_H">, <Entry index=71 label="O2b">]
[<Entry index=19 label="Cb_H">, <Entry index=101 label="C_methyl">]
[<Entry index=19 label="Cb_H">, <Entry index=103 label="C_rad/H2/Cs">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 20,
    label = "CO_H",
    group = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     O 0 {1,D}
3  *2 H 0 {1,S}
4     R 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2663.65,326.045,91.4145,38.8649,13.1641,6.79746,2.74831,1.71442],"m^3/(mol*s)","*|/",[148395,10702.1,2402.51,931.548,311.249,176.592,110.464,118.599])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [26, 26, 26, 26, 26, 26, 26, 26] rates.
[<Entry index=23 label="CO/H/NonDe">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=71 label="O2b">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=21 label="CO_pri">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=21 label="CO_pri">, <Entry index=69 label="H_rad">]
[<Entry index=21 label="CO_pri">, <Entry index=71 label="O2b">]
[<Entry index=21 label="CO_pri">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=21 label="CO_pri">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=21 label="CO_pri">, <Entry index=101 label="C_methyl">]
[<Entry index=21 label="CO_pri">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=21 label="CO_pri">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=21 label="CO_pri">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=21 label="CO_pri">, <Entry index=98 label="CO_rad/NonDe">]
[<Entry index=21 label="CO_pri">, <Entry index=75 label="O_pri_rad">]
[<Entry index=21 label="CO_pri">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=69 label="H_rad">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=101 label="C_methyl">]
[<Entry index=21 label="CO_pri">, <Entry index=67 label="CH2_triplet">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=75 label="O_pri_rad">]
[<Entry index=21 label="CO_pri">, <Entry index=118 label="C_rad/H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 21,
    label = "CO_pri",
    group = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     O 0 {1,D}
3  *2 H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([969.611,132.712,40.1441,18.0599,6.63449,3.629,1.61483,1.07273],"m^3/(mol*s)","*|/",[74586.6,5896.67,1470.1,637.361,267.882,189.648,187.147,274.05])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [14, 14, 14, 14, 14, 14, 14, 14] rates.
[<Entry index=21 label="CO_pri">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=21 label="CO_pri">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=21 label="CO_pri">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=21 label="CO_pri">, <Entry index=101 label="C_methyl">]
[<Entry index=21 label="CO_pri">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=21 label="CO_pri">, <Entry index=75 label="O_pri_rad">]
[<Entry index=21 label="CO_pri">, <Entry index=71 label="O2b">]
[<Entry index=21 label="CO_pri">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=21 label="CO_pri">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=21 label="CO_pri">, <Entry index=67 label="CH2_triplet">]
[<Entry index=21 label="CO_pri">, <Entry index=98 label="CO_rad/NonDe">]
[<Entry index=21 label="CO_pri">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=21 label="CO_pri">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=21 label="CO_pri">, <Entry index=69 label="H_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 22,
    label = "CO_sec",
    group = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     O 0 {1,D}
3  *2 H 0 {1,S}
4     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([9887.53,1046.95,265.99,105.086,32.0341,15.3495,5.48015,3.15064],"m^3/(mol*s)","*|/",[2.22619e+06,93391,14669.5,4346.71,963.06,394.546,132.441,93.0439])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [12, 12, 12, 12, 12, 12, 12, 12] rates.
[<Entry index=23 label="CO/H/NonDe">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=69 label="H_rad">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=75 label="O_pri_rad">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=71 label="O2b">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=101 label="C_methyl">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 23,
    label = "CO/H/NonDe",
    group = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     O 0 {1,D}
3  *2 H 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([9887.53,1046.95,265.99,105.086,32.0341,15.3495,5.48015,3.15064],"m^3/(mol*s)","*|/",[2.22619e+06,93391,14669.5,4346.71,963.06,394.546,132.441,93.0439])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [12, 12, 12, 12, 12, 12, 12, 12] rates.
[<Entry index=23 label="CO/H/NonDe">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=69 label="H_rad">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=75 label="O_pri_rad">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=71 label="O2b">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=101 label="C_methyl">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 24,
    label = "CO/H/OneDe",
    group = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     O 0 {1,D}
3  *2 H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 25,
    label = "Cs_H",
    group = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     R 0 {1,S}
4     R 0 {1,S}
5     R 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([8.88431,5.18641,3.77792,3.07089,2.38726,2.06501,1.72422,1.59171],"m^3/(mol*s)","*|/",[805.052,174.754,79.5775,50.0802,29.8822,22.4335,15.5928,13.4743])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [167, 167, 167, 167, 167, 167, 167, 167] rates.
[<Entry index=26 label="C_methane">, <Entry index=98 label="CO_rad/NonDe">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=67 label="CH2_triplet">]
[<Entry index=26 label="C_methane">, <Entry index=94 label="Cb_rad">]
[<Entry index=36 label="C/H3/Cb">, <Entry index=101 label="C_methyl">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=101 label="C_methyl">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=75 label="O_pri_rad">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=69 label="H_rad">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=71 label="O2b">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=69 label="H_rad">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=67 label="CH2_triplet">]
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=90 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=26 label="C_methane">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=38 label="C/H3/O">, <Entry index=69 label="H_rad">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=78 label="InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=101 label="C_methyl">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=89 label="Cd_rad/NonDeC">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=98 label="CO_rad/NonDe">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=96 label="CO_pri_rad">]
[<Entry index=26 label="C_methane">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=71 label="O2b">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=98 label="CO_rad/NonDe">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=101 label="C_methyl">]
[<Entry index=26 label="C_methane">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=47 label="C/H2/OneDeC">, <Entry index=69 label="H_rad">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=113 label="C_rad/H2/Ct">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=75 label="O_pri_rad">]
[<Entry index=29 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=109 label="InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3">]
[<Entry index=51 label="C/H2/TwoDe">, <Entry index=101 label="C_methyl">]
[<Entry index=26 label="C_methane">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=26 label="C_methane">, <Entry index=71 label="O2b">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=126 label="InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=69 label="H_rad">]
[<Entry index=26 label="C_methane">, <Entry index=96 label="CO_pri_rad">]
[<Entry index=58 label="C/H/Cs2">, <Entry index=69 label="H_rad">]
[<Entry index=29 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=78 label="InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=26 label="C_methane">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=93 label="Cd_rad/OneDe">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=129 label="C_rad/H/OneDeC">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=69 label="H_rad">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=26 label="C_methane">, <Entry index=69 label="H_rad">]
[<Entry index=47 label="C/H2/OneDeC">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=83 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/o">]
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=130 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=73 label="Ct_rad">]
[<Entry index=48 label="InChI=1/C3H6O/c1-2-3-4/h3H,2H2,1H3/beta">, <Entry index=109 label="InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=93 label="Cd_rad/OneDe">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=26 label="C_methane">, <Entry index=73 label="Ct_rad">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=96 label="CO_pri_rad">]
[<Entry index=59 label="InChI=1/C4H8O/c1-4(2)3-5/h3-4H,1-2H3">, <Entry index=69 label="H_rad">]
[<Entry index=26 label="C_methane">, <Entry index=101 label="C_methyl">]
[<Entry index=26 label="C_methane">, <Entry index=72 label="C2b">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=86 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=73 label="Ct_rad">]
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=104 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=119 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=89 label="Cd_rad/NonDeC">]
[<Entry index=32 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=78 label="InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=140 label="C_rad/Cs2">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=109 label="InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=104 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=35 label="C/H3/Ct">, <Entry index=101 label="C_methyl">]
[<Entry index=32 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=126 label="InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=34 label="InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=38 label="C/H3/O">, <Entry index=75 label="O_pri_rad">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=94 label="Cb_rad">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=73 label="Ct_rad">]
[<Entry index=37 label="C/H3/CO">, <Entry index=75 label="O_pri_rad">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=26 label="C_methane">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=41 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=136 label="InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3">]
[<Entry index=32 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=109 label="InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=129 label="C_rad/H/OneDeC">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=101 label="C_methyl">]
[<Entry index=30 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/gamma">, <Entry index=90 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=47 label="C/H2/OneDeC">, <Entry index=101 label="C_methyl">]
[<Entry index=38 label="C/H3/O">, <Entry index=101 label="C_methyl">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=136 label="InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=51 label="C/H2/TwoDe">, <Entry index=69 label="H_rad">]
[<Entry index=35 label="C/H3/Ct">, <Entry index=69 label="H_rad">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=140 label="C_rad/Cs2">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=71 label="O2b">]
[<Entry index=58 label="C/H/Cs2">, <Entry index=101 label="C_methyl">]
[<Entry index=49 label="InChI=1/C4H8/c1-3-4-2/h3H,1,4H2,2H3">, <Entry index=80 label="OOCH3">]
[<Entry index=49 label="InChI=1/C4H8/c1-3-4-2/h3H,1,4H2,2H3">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=130 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=32 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=136 label="InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=119 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=113 label="C_rad/H2/Ct">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=75 label="O_pri_rad">]
[<Entry index=62 label="C/H/Cs">, <Entry index=101 label="C_methyl">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=96 label="CO_pri_rad">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=98 label="CO_rad/NonDe">]
[<Entry index=26 label="C_methane">, <Entry index=75 label="O_pri_rad">]
[<Entry index=26 label="C_methane">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=116 label="C_rad/H2/O">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=118 label="C_rad/H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 26,
    label = "C_methane",
    group = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0306008,0.0903781,0.172519,0.264896,0.451011,0.618631,0.936229,1.14542],"m^3/(mol*s)","*|/",[4963.75,568.249,189.325,102.346,55.799,42.7221,34.4286,34.4376])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [21, 21, 21, 21, 21, 21, 21, 21] rates.
[<Entry index=26 label="C_methane">, <Entry index=72 label="C2b">]
[<Entry index=26 label="C_methane">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=26 label="C_methane">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=26 label="C_methane">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=26 label="C_methane">, <Entry index=98 label="CO_rad/NonDe">]
[<Entry index=26 label="C_methane">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=26 label="C_methane">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=26 label="C_methane">, <Entry index=73 label="Ct_rad">]
[<Entry index=26 label="C_methane">, <Entry index=69 label="H_rad">]
[<Entry index=26 label="C_methane">, <Entry index=101 label="C_methyl">]
[<Entry index=26 label="C_methane">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=26 label="C_methane">, <Entry index=71 label="O2b">]
[<Entry index=26 label="C_methane">, <Entry index=94 label="Cb_rad">]
[<Entry index=26 label="C_methane">, <Entry index=75 label="O_pri_rad">]
[<Entry index=26 label="C_methane">, <Entry index=96 label="CO_pri_rad">]
[<Entry index=26 label="C_methane">, <Entry index=135 label="C_rad/Cs3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 27,
    label = "C_pri",
    group = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([3.35109,2.25556,1.81398,1.58935,1.37897,1.29149,1.23417,1.247],"m^3/(mol*s)","*|/",[837.797,167.615,73.6314,45.3522,26.1678,19.0278,12.3572,10.2962])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [57, 57, 57, 57, 57, 57, 57, 57] rates.
[<Entry index=31 label="C/H3/Cd">, <Entry index=101 label="C_methyl">]
[<Entry index=38 label="C/H3/O">, <Entry index=69 label="H_rad">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=129 label="C_rad/H/OneDeC">]
[<Entry index=30 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/gamma">, <Entry index=90 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=34 label="InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=89 label="Cd_rad/NonDeC">]
[<Entry index=38 label="C/H3/O">, <Entry index=101 label="C_methyl">]
[<Entry index=36 label="C/H3/Cb">, <Entry index=101 label="C_methyl">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=136 label="InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=101 label="C_methyl">]
[<Entry index=29 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=109 label="InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=35 label="C/H3/Ct">, <Entry index=101 label="C_methyl">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=126 label="InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=75 label="O_pri_rad">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=83 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/o">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=140 label="C_rad/Cs2">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=71 label="O2b">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=93 label="Cd_rad/OneDe">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=69 label="H_rad">]
[<Entry index=38 label="C/H3/O">, <Entry index=75 label="O_pri_rad">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=94 label="Cb_rad">]
[<Entry index=29 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=78 label="InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=32 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=136 label="InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=78 label="InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=109 label="InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=113 label="C_rad/H2/Ct">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=69 label="H_rad">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=73 label="Ct_rad">]
[<Entry index=37 label="C/H3/CO">, <Entry index=75 label="O_pri_rad">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=35 label="C/H3/Ct">, <Entry index=69 label="H_rad">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=32 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=109 label="InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3">]
[<Entry index=32 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=126 label="InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=98 label="CO_rad/NonDe">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=96 label="CO_pri_rad">]
[<Entry index=32 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=78 label="InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 28,
    label = "C/H3/Cs",
    group = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cs 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.291217,0.393676,0.480452,0.555403,0.680331,0.782608,0.980937,1.13257],"m^3/(mol*s)","*|/",[199.585,38.3724,17.0158,11.242,8.30607,8.01384,9.44756,11.7811])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [22, 22, 22, 22, 22, 22, 22, 22] rates.
[<Entry index=28 label="C/H3/Cs">, <Entry index=73 label="Ct_rad">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=69 label="H_rad">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=94 label="Cb_rad">]
[<Entry index=29 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=109 label="InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=29 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=78 label="InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3">]
[<Entry index=30 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/gamma">, <Entry index=90 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=75 label="O_pri_rad">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=98 label="CO_rad/NonDe">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=71 label="O2b">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=101 label="C_methyl">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=96 label="CO_pri_rad">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=135 label="C_rad/Cs3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 29,
    label = "InChI=1/C2H6/c1-2/h1-2H3",
    group = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 {1,S} {6,S} {7,S} {8,S}
3  *2 H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {2,S}
8     H 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([27.0436,8.22976,4.61977,3.44177,2.79938,2.83446,3.85668,5.65807],"m^3/(mol*s)","*|/",[7.9262e+30,5.46491e+19,4.09199e+13,8.0382e+09,901911,16269.7,2913.17,18755.5])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [2, 2, 2, 2, 2, 2, 2, 2] rates.
[<Entry index=29 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=78 label="InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3">]
[<Entry index=29 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=109 label="InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 30,
    label = "InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/gamma",
    group = 
"""
1     C 0 {2,S} {3,S} {4,S} {6,S}
2     C 0 {1,S} {5,S} {7,S} {8,S}
3  *1 C 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 {1,S} {12,S} {13,S} {14,S}
5     O 0 {2,S} {15,S}
6     H 0 {1,S}
7     H 0 {2,S}
8     H 0 {2,S}
9  *2 H 0 {3,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {4,S}
14    H 0 {4,S}
15    H 0 {5,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.16371,0.709126,0.421163,0.328381,0.286737,0.306592,0.460167,0.723389],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=30 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/gamma">, <Entry index=90 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 31,
    label = "C/H3/Cd",
    group = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cd 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([5.30025,2.83981,1.99129,1.59211,1.23174,1.0767,0.938083,0.904726],"m^3/(mol*s)","*|/",[156.401,43.9207,26.5679,20.7782,15.5965,12.4393,7.7363,5.67109])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [28, 28, 28, 28, 28, 28, 28, 28] rates.
[<Entry index=31 label="C/H3/Cd">, <Entry index=129 label="C_rad/H/OneDeC">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=89 label="Cd_rad/NonDeC">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=136 label="InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=126 label="InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3">]
[<Entry index=34 label="InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=140 label="C_rad/Cs2">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=69 label="H_rad">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=93 label="Cd_rad/OneDe">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=32 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=109 label="InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3">]
[<Entry index=32 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=136 label="InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=78 label="InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=109 label="InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=113 label="C_rad/H2/Ct">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=83 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/o">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=101 label="C_methyl">]
[<Entry index=32 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=126 label="InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3">]
[<Entry index=32 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=78 label="InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 32,
    label = "InChI=1/C3H6/c1-3-2/h3H,1H2,2H3",
    group = 
"""
1  *1 C 0 {2,S} {4,S} {5,S} {6,S}
2     C 0 {1,S} {3,D} {7,S}
3     C 0 {2,D} {8,S} {9,S}
4  *2 H 0 {1,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {2,S}
8     H 0 {3,S}
9     H 0 {3,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([185.164,20.7508,6.28826,3.07091,1.44369,1.03421,0.855299,0.950528],"m^3/(mol*s)","*|/",[104629,755.619,62.7924,17.9156,8.54045,8.35261,7.93167,6.68049])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [4, 4, 4, 4, 4, 4, 4, 4] rates.
[<Entry index=32 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=136 label="InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3">]
[<Entry index=32 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=126 label="InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3">]
[<Entry index=32 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=109 label="InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3">]
[<Entry index=32 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=78 label="InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 33,
    label = "InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3",
    group = 
"""
1  *1 C 0 {3,S} {5,S} {6,S} {7,S}
2     C 0 {3,S} {8,S} {9,S} {10,S}
3     C 0 {1,S} {2,S} {4,D}
4     C 0 {3,D} {11,S} {12,S}
5  *2 H 0 {1,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {4,S}
12    H 0 {4,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([46.9122,7.79578,3,1.72096,0.992386,0.805645,0.791512,0.962874],"m^3/(mol*s)","*|/",[76.5484,8.52993,5.62069,6.54281,8.32341,8.11614,5.1111,3.53135])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [5, 5, 5, 5, 5, 5, 5, 5] rates.
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=126 label="InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=109 label="InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=136 label="InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=83 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/o">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=78 label="InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 34,
    label = "InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+",
    group = 
"""
1  *1 C 0 {3,S} {5,S} {6,S} {7,S}
2     C 0 {4,S} {8,S} {9,S} {10,S}
3     C 0 {1,S} {4,D} {11,S}
4     C 0 {2,S} {3,D} {12,S}
5     H 0 {1,S}
6     H 0 {1,S}
7  *2 H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {4,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0389095,0.0511481,0.0689553,0.0920221,0.154782,0.241931,0.585084,1.14098],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=34 label="InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+">, <Entry index=79 label="O_rad/NonDeO">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 35,
    label = "C/H3/Ct",
    group = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Ct 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([588.844,263.855,157.258,108.752,65.7344,46.885,27.6754,20.0192],"m^3/(mol*s)","*|/",[1.02627e+36,3.92971e+30,1.73833e+27,8.19916e+24,6.54481e+21,6.01929e+19,4.59024e+16,6.14021e+14])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [2, 2, 2, 2, 2, 2, 2, 2] rates.
[<Entry index=35 label="C/H3/Ct">, <Entry index=101 label="C_methyl">]
[<Entry index=35 label="C/H3/Ct">, <Entry index=69 label="H_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 36,
    label = "C/H3/Cb",
    group = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cb 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([5.98577,5.50093,4.85981,4.26206,3.31698,2.65223,1.68331,1.18569],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=36 label="C/H3/Cb">, <Entry index=101 label="C_methyl">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 37,
    label = "C/H3/CO",
    group = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     CO 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([326627,17631.3,3120.56,996.738,245.018,107.69,37.5433,22.9181],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=37 label="C/H3/CO">, <Entry index=75 label="O_pri_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 38,
    label = "C/H3/O",
    group = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     O 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([6785.62,633.612,169.355,75.2587,30.8526,20.0341,14.0444,13.9875],"m^3/(mol*s)","*|/",[2.03868e+16,1.22477e+13,1.445e+11,7.3055e+09,1.59677e+08,1.44802e+07,459723,70342.4])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [3, 3, 3, 3, 3, 3, 3, 3] rates.
[<Entry index=38 label="C/H3/O">, <Entry index=101 label="C_methyl">]
[<Entry index=38 label="C/H3/O">, <Entry index=75 label="O_pri_rad">]
[<Entry index=38 label="C/H3/O">, <Entry index=69 label="H_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 39,
    label = "C_sec",
    group = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     R!H 0 {1,S}
5     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([36.0179,13.0783,7.30927,5.04575,3.27423,2.5925,2.00757,1.84562],"m^3/(mol*s)","*|/",[322.649,91.1247,48.0615,32.999,21.497,16.7395,11.91,10.287])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [41, 41, 41, 41, 41, 41, 41, 41] rates.
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=67 label="CH2_triplet">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=101 label="C_methyl">]
[<Entry index=41 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=136 label="InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3">]
[<Entry index=47 label="C/H2/OneDeC">, <Entry index=101 label="C_methyl">]
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=119 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=47 label="C/H2/OneDeC">, <Entry index=69 label="H_rad">]
[<Entry index=49 label="InChI=1/C4H8/c1-3-4-2/h3H,1,4H2,2H3">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=75 label="O_pri_rad">]
[<Entry index=51 label="C/H2/TwoDe">, <Entry index=69 label="H_rad">]
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=104 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=71 label="O2b">]
[<Entry index=49 label="InChI=1/C4H8/c1-3-4-2/h3H,1,4H2,2H3">, <Entry index=80 label="OOCH3">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=69 label="H_rad">]
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=90 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=47 label="C/H2/OneDeC">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=51 label="C/H2/TwoDe">, <Entry index=101 label="C_methyl">]
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=130 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=73 label="Ct_rad">]
[<Entry index=48 label="InChI=1/C3H6O/c1-2-3-4/h3H,2H2,1H3/beta">, <Entry index=109 label="InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=96 label="CO_pri_rad">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=98 label="CO_rad/NonDe">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=116 label="C_rad/H2/O">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=118 label="C_rad/H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 40,
    label = "C/H2/NonDeC",
    group = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([4.20106,2.90029,2.33395,2.02607,1.70789,1.54933,1.37538,1.30696],"m^3/(mol*s)","*|/",[678.917,146.183,63.7599,38.6495,22.3544,17.0448,13.4272,13.398])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [24, 24, 24, 24, 24, 24, 24, 24] rates.
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=75 label="O_pri_rad">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=73 label="Ct_rad">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=69 label="H_rad">]
[<Entry index=41 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=136 label="InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=67 label="CH2_triplet">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=101 label="C_methyl">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=96 label="CO_pri_rad">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=98 label="CO_rad/NonDe">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=116 label="C_rad/H2/O">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=71 label="O2b">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=118 label="C_rad/H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 41,
    label = "InChI=1/C3H8/c1-3-2/h3H2,1-2H3",
    group = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 {1,S} {9,S} {10,S} {11,S}
4  *2 H 0 {1,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {3,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([3.02701,0.7846,0.405249,0.288092,0.224419,0.22432,0.308478,0.465037],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=41 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=136 label="InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 42,
    label = "C/H2/NonDeO",
    group = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     O 0 {1,S}
5     {Cs,O} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([39.5633,5.54947,1.93389,1.04012,0.554985,0.431127,0.401537,0.477605],"m^3/(mol*s)","*|/",[35.9058,13.5286,27.6813,49.3283,81.1852,83.9329,47.7041,22.6597])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [4, 4, 4, 4, 4, 4, 4, 4] rates.
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=119 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=130 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c">]
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=104 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=90 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 43,
    label = "C/H2/CsO",
    group = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     O 0 {1,S}
5     Cs 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([39.5633,5.54947,1.93389,1.04012,0.554985,0.431127,0.401537,0.477605],"m^3/(mol*s)","*|/",[35.9058,13.5286,27.6813,49.3283,81.1852,83.9329,47.7041,22.6597])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [4, 4, 4, 4, 4, 4, 4, 4] rates.
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=119 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=130 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c">]
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=104 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=90 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 44,
    label = "InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha",
    group = 
"""
1     C 0 {2,S} {3,S} {4,S} {6,S}
2  *1 C 0 {1,S} {5,S} {7,S} {8,S}
3     C 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 {1,S} {12,S} {13,S} {14,S}
5     O 0 {2,S} {15,S}
6     H 0 {1,S}
7  *2 H 0 {2,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {4,S}
14    H 0 {4,S}
15    H 0 {5,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([39.5633,5.54947,1.93389,1.04012,0.554985,0.431127,0.401537,0.477605],"m^3/(mol*s)","*|/",[35.9058,13.5286,27.6813,49.3283,81.1852,83.9329,47.7041,22.6597])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [4, 4, 4, 4, 4, 4, 4, 4] rates.
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=119 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=130 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c">]
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=104 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=90 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 45,
    label = "C/H2/O2",
    group = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     O 0 {1,S}
5     O 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 46,
    label = "C/H2/OneDe",
    group = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     {Cd,Ct,CO,Cb} 0 {1,S}
5     {Cs,O} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([328.296,71.6952,29.7955,16.9813,8.76269,6.10048,4.05485,3.50516],"m^3/(mol*s)","*|/",[250.397,77.1488,43.4434,30.5765,19.1754,13.5232,6.97214,4.44921])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [10, 10, 10, 10, 10, 10, 10, 10] rates.
[<Entry index=49 label="InChI=1/C4H8/c1-3-4-2/h3H,1,4H2,2H3">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=47 label="C/H2/OneDeC">, <Entry index=101 label="C_methyl">]
[<Entry index=47 label="C/H2/OneDeC">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=47 label="C/H2/OneDeC">, <Entry index=69 label="H_rad">]
[<Entry index=48 label="InChI=1/C3H6O/c1-2-3-4/h3H,2H2,1H3/beta">, <Entry index=109 label="InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3">]
[<Entry index=49 label="InChI=1/C4H8/c1-3-4-2/h3H,1,4H2,2H3">, <Entry index=80 label="OOCH3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 47,
    label = "C/H2/OneDeC",
    group = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     {Cd,Ct,CO,Cb} 0 {1,S}
5     Cs 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([328.296,71.6952,29.7955,16.9813,8.76269,6.10048,4.05485,3.50516],"m^3/(mol*s)","*|/",[250.397,77.1488,43.4434,30.5765,19.1754,13.5232,6.97214,4.44921])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [10, 10, 10, 10, 10, 10, 10, 10] rates.
[<Entry index=49 label="InChI=1/C4H8/c1-3-4-2/h3H,1,4H2,2H3">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=47 label="C/H2/OneDeC">, <Entry index=101 label="C_methyl">]
[<Entry index=47 label="C/H2/OneDeC">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=47 label="C/H2/OneDeC">, <Entry index=69 label="H_rad">]
[<Entry index=48 label="InChI=1/C3H6O/c1-2-3-4/h3H,2H2,1H3/beta">, <Entry index=109 label="InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3">]
[<Entry index=49 label="InChI=1/C4H8/c1-3-4-2/h3H,1,4H2,2H3">, <Entry index=80 label="OOCH3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 48,
    label = "InChI=1/C3H6O/c1-2-3-4/h3H,2H2,1H3/beta",
    group = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 {1,S} {9,D} {10,S}
4  *2 H 0 {1,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     O 0 {3,D}
10    H 0 {3,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([227.608,16.2227,3.6849,1.4685,0.524965,0.313781,0.196682,0.185017],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=48 label="InChI=1/C3H6O/c1-2-3-4/h3H,2H2,1H3/beta">, <Entry index=109 label="InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 49,
    label = "InChI=1/C4H8/c1-3-4-2/h3H,1,4H2,2H3",
    group = 
"""
1  *1 C 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 {1,S} {7,S} {8,S} {9,S}
3     C 0 {1,S} {4,D} {10,S}
4     C 0 {3,D} {11,S} {12,S}
5  *2 H 0 {1,S}
6     H 0 {1,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {4,S}
12    H 0 {4,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.5217,0.727064,0.52527,0.457404,0.442424,0.488006,0.715657,1.05687],"m^3/(mol*s)","*|/",[1.77011e+26,1.14984e+20,1.58089e+16,3.16421e+13,7.31682e+09,2.69159e+07,3753.9,13.4603])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [2, 2, 2, 2, 2, 2, 2, 2] rates.
[<Entry index=49 label="InChI=1/C4H8/c1-3-4-2/h3H,1,4H2,2H3">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=49 label="InChI=1/C4H8/c1-3-4-2/h3H,1,4H2,2H3">, <Entry index=80 label="OOCH3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 50,
    label = "C/H2/OneDeO",
    group = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     {Cd,Ct,CO,Cb} 0 {1,S}
5     O 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 51,
    label = "C/H2/TwoDe",
    group = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     {Cd,Ct,CO,Cb} 0 {1,S}
5     {Cd,Ct,CO,Cb} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.30475e+06,135455,23847.9,7311.85,1597.72,618.492,161.408,77.5494],"m^3/(mol*s)","*|/",[2.7559e+08,2.0377e+07,5.10534e+06,2.07713e+06,619270,259081,53072.7,16621.4])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [3, 3, 3, 3, 3, 3, 3, 3] rates.
[<Entry index=51 label="C/H2/TwoDe">, <Entry index=101 label="C_methyl">]
[<Entry index=51 label="C/H2/TwoDe">, <Entry index=69 label="H_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 52,
    label = "C_ter",
    group = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     R!H 0 {1,S}
4     R!H 0 {1,S}
5     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([94.829,35.6462,19.342,12.6615,7.24396,5.05727,2.97365,2.18894],"m^3/(mol*s)","*|/",[1443.67,316.636,141.249,86.5066,49.1968,35.6748,23.3969,19.1993])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [48, 48, 48, 48, 48, 48, 48, 48] rates.
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=119 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=86 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=71 label="O2b">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=73 label="Ct_rad">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=98 label="CO_rad/NonDe">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=140 label="C_rad/Cs2">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=104 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=69 label="H_rad">]
[<Entry index=58 label="C/H/Cs2">, <Entry index=69 label="H_rad">]
[<Entry index=58 label="C/H/Cs2">, <Entry index=101 label="C_methyl">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=129 label="C_rad/H/OneDeC">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=67 label="CH2_triplet">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=113 label="C_rad/H2/Ct">]
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=130 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=89 label="Cd_rad/NonDeC">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=75 label="O_pri_rad">]
[<Entry index=62 label="C/H/Cs">, <Entry index=101 label="C_methyl">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=93 label="Cd_rad/OneDe">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=101 label="C_methyl">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=96 label="CO_pri_rad">]
[<Entry index=59 label="InChI=1/C4H8O/c1-4(2)3-5/h3-4H,1-2H3">, <Entry index=69 label="H_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 53,
    label = "C/H/NonDeC",
    group = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
5     {Cs,O} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([25.6154,12.3984,7.85617,5.7159,3.74711,2.84834,1.88978,1.48618],"m^3/(mol*s)","*|/",[797.675,187.698,89.5522,58.062,35.8996,27.5019,19.5062,16.7731])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [40, 40, 40, 40, 40, 40, 40, 40] rates.
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=119 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=86 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=71 label="O2b">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=73 label="Ct_rad">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=98 label="CO_rad/NonDe">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=140 label="C_rad/Cs2">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=104 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=69 label="H_rad">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=129 label="C_rad/H/OneDeC">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=67 label="CH2_triplet">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=113 label="C_rad/H2/Ct">]
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=130 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=89 label="Cd_rad/NonDeC">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=75 label="O_pri_rad">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=93 label="Cd_rad/OneDe">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=101 label="C_methyl">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=96 label="CO_pri_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 54,
    label = "C/H/Cs3",
    group = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([25.6154,12.3984,7.85617,5.7159,3.74711,2.84834,1.88978,1.48618],"m^3/(mol*s)","*|/",[797.675,187.698,89.5522,58.062,35.8996,27.5019,19.5062,16.7731])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [40, 40, 40, 40, 40, 40, 40, 40] rates.
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=119 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=86 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=71 label="O2b">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=73 label="Ct_rad">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=98 label="CO_rad/NonDe">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=140 label="C_rad/Cs2">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=104 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=69 label="H_rad">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=129 label="C_rad/H/OneDeC">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=67 label="CH2_triplet">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=113 label="C_rad/H2/Ct">]
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=130 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=89 label="Cd_rad/NonDeC">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=75 label="O_pri_rad">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=93 label="Cd_rad/OneDe">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=101 label="C_methyl">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=96 label="CO_pri_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 55,
    label = "InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta",
    group = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {6,S}
2     C 0 {1,S} {5,S} {7,S} {8,S}
3     C 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 {1,S} {12,S} {13,S} {14,S}
5     O 0 {2,S} {15,S}
6  *2 H 0 {1,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {4,S}
14    H 0 {4,S}
15    H 0 {5,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([49.8874,7.02899,2.43603,1.29831,0.678311,0.516069,0.459379,0.526877],"m^3/(mol*s)","*|/",[121.792,5.45895,6.58038,14.6675,34.6521,44.5414,33.6678,18.4264])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [4, 4, 4, 4, 4, 4, 4, 4] rates.
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=86 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=119 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=130 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c">]
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=104 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 56,
    label = "C/H/NDMustO",
    group = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     O 0 {1,S}
4     {Cs,O} 0 {1,S}
5     {Cs,O} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 57,
    label = "C/H/OneDe",
    group = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cs,O} 0 {1,S}
5     {Cs,O} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([376380,28191,5743.77,1941.9,479.792,200.053,57.7129,29.1814],"m^3/(mol*s)","*|/",[4.62031e+06,219551,37102.3,11620.7,2796.95,1202.05,388.208,217.939])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [6, 6, 6, 6, 6, 6, 6, 6] rates.
[<Entry index=58 label="C/H/Cs2">, <Entry index=69 label="H_rad">]
[<Entry index=59 label="InChI=1/C4H8O/c1-4(2)3-5/h3-4H,1-2H3">, <Entry index=69 label="H_rad">]
[<Entry index=58 label="C/H/Cs2">, <Entry index=101 label="C_methyl">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 58,
    label = "C/H/Cs2",
    group = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([376380,28191,5743.77,1941.9,479.792,200.053,57.7129,29.1814],"m^3/(mol*s)","*|/",[4.62031e+06,219551,37102.3,11620.7,2796.95,1202.05,388.208,217.939])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [6, 6, 6, 6, 6, 6, 6, 6] rates.
[<Entry index=58 label="C/H/Cs2">, <Entry index=69 label="H_rad">]
[<Entry index=59 label="InChI=1/C4H8O/c1-4(2)3-5/h3-4H,1-2H3">, <Entry index=69 label="H_rad">]
[<Entry index=58 label="C/H/Cs2">, <Entry index=101 label="C_methyl">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 59,
    label = "InChI=1/C4H8O/c1-4(2)3-5/h3-4H,1-2H3",
    group = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 {1,S} {12,D} {13,S}
5  *2 H 0 {1,S}
6     H 0 {2,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    O 0 {4,D}
13    H 0 {4,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([618003,30102.2,4962.48,1502.38,341.582,141.926,44.996,25.7843],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=59 label="InChI=1/C4H8O/c1-4(2)3-5/h3-4H,1-2H3">, <Entry index=69 label="H_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 60,
    label = "C/H/ODMustO",
    group = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     O 0 {1,S}
5     {Cs,O} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 61,
    label = "C/H/TwoDe",
    group = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cs,O} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([557966,40559.4,7819.43,2485.66,544.064,203.221,46.7507,19.8258],"m^3/(mol*s)","*|/",[1.51828e+18,6.90328e+16,7.26336e+15,1.2459e+15,8.67114e+13,1.19317e+13,3.80986e+11,3.71209e+10])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [2, 2, 2, 2, 2, 2, 2, 2] rates.
[<Entry index=62 label="C/H/Cs">, <Entry index=101 label="C_methyl">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 62,
    label = "C/H/Cs",
    group = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     Cs 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([557966,40559.4,7819.43,2485.66,544.064,203.221,46.7507,19.8258],"m^3/(mol*s)","*|/",[1.51828e+18,6.90328e+16,7.26336e+15,1.2459e+15,8.67114e+13,1.19317e+13,3.80986e+11,3.71209e+10])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [2, 2, 2, 2, 2, 2, 2, 2] rates.
[<Entry index=62 label="C/H/Cs">, <Entry index=101 label="C_methyl">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 63,
    label = "C/H/TDMustO",
    group = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     O 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 64,
    label = "C/H/ThreeDe",
    group = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 65,
    label = "Y_1centerbirad",
    group = 
"""
1  *3 {Cs,Cd,O} 2T
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([81650.9,5823.44,1196.25,416.926,111.865,50.8852,17.8638,10.6136],"m^3/(mol*s)","*|/",[82923.2,3221.14,488.631,145.31,35.1498,16.8044,9.26014,10.0201])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [16, 16, 16, 16, 16, 16, 16, 16] rates.
[<Entry index=8 label="O/H/NonDeC">, <Entry index=67 label="CH2_triplet">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=67 label="CH2_triplet">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=67 label="CH2_triplet">]
[<Entry index=21 label="CO_pri">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=21 label="CO_pri">, <Entry index=67 label="CH2_triplet">]
[<Entry index=14 label="Cd_pri">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=6 label="O_pri">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=66 label="O_atom_triplet">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 66,
    label = "O_atom_triplet",
    group = 
"""
1  *3 O 2T
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([598272,33953.5,6095.53,1944.98,468.646,200.326,65.0579,37.3248],"m^3/(mol*s)","*|/",[118294,3188.24,401.708,107.73,23.5663,10.7657,5.64547,5.9549])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [12, 12, 12, 12, 12, 12, 12, 12] rates.
[<Entry index=54 label="C/H/Cs3">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=21 label="CO_pri">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=14 label="Cd_pri">, <Entry index=66 label="O_atom_triplet">]
[<Entry index=6 label="O_pri">, <Entry index=66 label="O_atom_triplet">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 67,
    label = "CH2_triplet",
    group = 
"""
1  *3 C 2T {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([266.235,36.6248,11.083,4.9785,1.81978,0.989795,0.43467,0.285579],"m^3/(mol*s)","*|/",[3.22448e+08,3.65682e+06,223737,33306.8,3113.55,847.314,292.696,364.653])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [4, 4, 4, 4, 4, 4, 4, 4] rates.
[<Entry index=8 label="O/H/NonDeC">, <Entry index=67 label="CH2_triplet">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=67 label="CH2_triplet">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=67 label="CH2_triplet">]
[<Entry index=21 label="CO_pri">, <Entry index=67 label="CH2_triplet">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 68,
    label = "Y_rad",
    group = 
"""
1  *3 R 1
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.550547,0.634944,0.69166,0.73225,0.786337,0.820673,0.868767,0.893834],"m^3/(mol*s)","*|/",[9983.54,1142.95,348.485,168.189,73.9353,47.8169,29.5413,25.3783])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [298, 298, 298, 298, 298, 298, 298, 298] rates.
[<Entry index=10 label="H2O2">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=10 label="H2O2">, <Entry index=120 label="InChI=1/C4H9O/c1-2-3-4-5/h2,5H,3-4H2,1H3">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=69 label="H_rad">]
[<Entry index=17 label="Cd/H/NonDeO">, <Entry index=69 label="H_rad">]
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=119 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=4 label="Ct_H">, <Entry index=71 label="O2b">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=71 label="O2b">]
[<Entry index=11 label="O/H/OneDe">, <Entry index=69 label="H_rad">]
[<Entry index=26 label="C_methane">, <Entry index=94 label="Cb_rad">]
[<Entry index=36 label="C/H3/Cb">, <Entry index=101 label="C_methyl">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=101 label="C_methyl">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=21 label="CO_pri">, <Entry index=69 label="H_rad">]
[<Entry index=6 label="O_pri">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=26 label="C_methane">, <Entry index=98 label="CO_rad/NonDe">]
[<Entry index=10 label="H2O2">, <Entry index=121 label="InChI=1/C4H9O/c1-2-3-4-5/h3,5H,2,4H2,1H3">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=75 label="O_pri_rad">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=3 label="H2">, <Entry index=101 label="C_methyl">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=126 label="InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3">]
[<Entry index=49 label="InChI=1/C4H8/c1-3-4-2/h3H,1,4H2,2H3">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=69 label="H_rad">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=71 label="O2b">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=69 label="H_rad">]
[<Entry index=19 label="Cb_H">, <Entry index=69 label="H_rad">]
[<Entry index=37 label="C/H3/CO">, <Entry index=75 label="O_pri_rad">]
[<Entry index=26 label="C_methane">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=38 label="C/H3/O">, <Entry index=69 label="H_rad">]
[<Entry index=32 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=109 label="InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=78 label="InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=101 label="C_methyl">]
[<Entry index=14 label="Cd_pri">, <Entry index=75 label="O_pri_rad">]
[<Entry index=6 label="O_pri">, <Entry index=69 label="H_rad">]
[<Entry index=6 label="O_pri">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=101 label="C_methyl">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=101 label="C_methyl">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=89 label="Cd_rad/NonDeC">]
[<Entry index=3 label="H2">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=4 label="Ct_H">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=32 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=78 label="InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=98 label="CO_rad/NonDe">]
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=90 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=73 label="Ct_rad">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=96 label="CO_pri_rad">]
[<Entry index=3 label="H2">, <Entry index=94 label="Cb_rad">]
[<Entry index=10 label="H2O2">, <Entry index=89 label="Cd_rad/NonDeC">]
[<Entry index=26 label="C_methane">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=26 label="C_methane">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=98 label="CO_rad/NonDe">]
[<Entry index=3 label="H2">, <Entry index=89 label="Cd_rad/NonDeC">]
[<Entry index=19 label="Cb_H">, <Entry index=71 label="O2b">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=101 label="C_methyl">]
[<Entry index=26 label="C_methane">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=10 label="H2O2">, <Entry index=111 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=10 label="H2O2">, <Entry index=105 label="InChI=1/C4H9O/c1-2-3-4-5/h5H,1-4H2">]
[<Entry index=14 label="Cd_pri">, <Entry index=140 label="C_rad/Cs2">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=71 label="O2b">]
[<Entry index=6 label="O_pri">, <Entry index=96 label="CO_pri_rad">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=113 label="C_rad/H2/Ct">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=75 label="O_pri_rad">]
[<Entry index=29 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=109 label="InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3">]
[<Entry index=11 label="O/H/OneDe">, <Entry index=101 label="C_methyl">]
[<Entry index=51 label="C/H2/TwoDe">, <Entry index=101 label="C_methyl">]
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=130 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c">]
[<Entry index=26 label="C_methane">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=26 label="C_methane">, <Entry index=71 label="O2b">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=10 label="H2O2">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=69 label="H_rad">]
[<Entry index=6 label="O_pri">, <Entry index=71 label="O2b">]
[<Entry index=26 label="C_methane">, <Entry index=96 label="CO_pri_rad">]
[<Entry index=58 label="C/H/Cs2">, <Entry index=69 label="H_rad">]
[<Entry index=14 label="Cd_pri">, <Entry index=129 label="C_rad/H/OneDeC">]
[<Entry index=19 label="Cb_H">, <Entry index=75 label="O_pri_rad">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=26 label="C_methane">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=93 label="Cd_rad/OneDe">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=69 label="H_rad">]
[<Entry index=6 label="O_pri">, <Entry index=75 label="O_pri_rad">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=129 label="C_rad/H/OneDeC">]
[<Entry index=10 label="H2O2">, <Entry index=87 label="InChI=1/C4H7/c1-3-4-2/h1,3H,4H2,2H3">]
[<Entry index=14 label="Cd_pri">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=69 label="H_rad">]
[<Entry index=14 label="Cd_pri">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=21 label="CO_pri">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=3 label="H2">, <Entry index=98 label="CO_rad/NonDe">]
[<Entry index=48 label="InChI=1/C3H6O/c1-2-3-4/h3H,2H2,1H3/beta">, <Entry index=109 label="InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=130 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c">]
[<Entry index=26 label="C_methane">, <Entry index=69 label="H_rad">]
[<Entry index=47 label="C/H2/OneDeC">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=21 label="CO_pri">, <Entry index=98 label="CO_rad/NonDe">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=83 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/o">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=14 label="Cd_pri">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=73 label="Ct_rad">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=73 label="Ct_rad">]
[<Entry index=4 label="Ct_H">, <Entry index=101 label="C_methyl">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=75 label="O_pri_rad">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=93 label="Cd_rad/OneDe">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=101 label="C_methyl">]
[<Entry index=26 label="C_methane">, <Entry index=73 label="Ct_rad">]
[<Entry index=21 label="CO_pri">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=3 label="H2">, <Entry index=113 label="C_rad/H2/Ct">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=96 label="CO_pri_rad">]
[<Entry index=59 label="InChI=1/C4H8O/c1-4(2)3-5/h3-4H,1-2H3">, <Entry index=69 label="H_rad">]
[<Entry index=3 label="H2">, <Entry index=73 label="Ct_rad">]
[<Entry index=14 label="Cd_pri">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=26 label="C_methane">, <Entry index=101 label="C_methyl">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=26 label="C_methane">, <Entry index=72 label="C2b">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=86 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=73 label="Ct_rad">]
[<Entry index=6 label="O_pri">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=21 label="CO_pri">, <Entry index=71 label="O2b">]
[<Entry index=10 label="H2O2">, <Entry index=125 label="InChI=1/C4H9O/c1-2-3-4-5/h4-5H,2-3H2,1H3">]
[<Entry index=14 label="Cd_pri">, <Entry index=93 label="Cd_rad/OneDe">]
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=104 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=119 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=89 label="Cd_rad/NonDeC">]
[<Entry index=21 label="CO_pri">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=140 label="C_rad/Cs2">]
[<Entry index=14 label="Cd_pri">, <Entry index=113 label="C_rad/H2/Ct">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=14 label="Cd_pri">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=104 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=35 label="C/H3/Ct">, <Entry index=101 label="C_methyl">]
[<Entry index=32 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=126 label="InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=34 label="InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=10 label="H2O2">, <Entry index=91 label="InChI=1/C4H7/c1-3-4-2/h3H,1-2H3">]
[<Entry index=3 label="H2">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=6 label="O_pri">, <Entry index=101 label="C_methyl">]
[<Entry index=3 label="H2">, <Entry index=93 label="Cd_rad/OneDe">]
[<Entry index=38 label="C/H3/O">, <Entry index=75 label="O_pri_rad">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=21 label="CO_pri">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=94 label="Cb_rad">]
[<Entry index=12 label="Orad_O_H">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=18 label="Cd/H/OneDe">, <Entry index=101 label="C_methyl">]
[<Entry index=3 label="H2">, <Entry index=129 label="C_rad/H/OneDeC">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=75 label="O_pri_rad">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=18 label="Cd/H/OneDe">, <Entry index=69 label="H_rad">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=73 label="Ct_rad">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=69 label="H_rad">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=19 label="Cb_H">, <Entry index=101 label="C_methyl">]
[<Entry index=3 label="H2">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=71 label="O2b">]
[<Entry index=41 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=136 label="InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3">]
[<Entry index=14 label="Cd_pri">, <Entry index=89 label="Cd_rad/NonDeC">]
[<Entry index=4 label="Ct_H">, <Entry index=75 label="O_pri_rad">]
[<Entry index=10 label="H2O2">, <Entry index=108 label="InChI=1/C4H9O/c1-4(2,3)5/h5H,1H2,2-3H3">]
[<Entry index=10 label="H2O2">, <Entry index=80 label="OOCH3">]
[<Entry index=10 label="H2O2">, <Entry index=81 label="O_rad/OneDe">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=129 label="C_rad/H/OneDeC">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=10 label="H2O2">, <Entry index=138 label="InChI=1/C4H9O/c1-3-4(2)5/h5H,3H2,1-2H3">]
[<Entry index=30 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/gamma">, <Entry index=90 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=3 label="H2">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=3 label="H2">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=47 label="C/H2/OneDeC">, <Entry index=101 label="C_methyl">]
[<Entry index=38 label="C/H3/O">, <Entry index=101 label="C_methyl">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=136 label="InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=47 label="C/H2/OneDeC">, <Entry index=69 label="H_rad">]
[<Entry index=51 label="C/H2/TwoDe">, <Entry index=69 label="H_rad">]
[<Entry index=21 label="CO_pri">, <Entry index=101 label="C_methyl">]
[<Entry index=35 label="C/H3/Ct">, <Entry index=69 label="H_rad">]
[<Entry index=21 label="CO_pri">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=14 label="Cd_pri">, <Entry index=101 label="C_methyl">]
[<Entry index=10 label="H2O2">, <Entry index=107 label="InChI=1/C4H9O/c1-3-4(2)5/h4-5H,1,3H2,2H3">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=140 label="C_rad/Cs2">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=98 label="CO_rad/NonDe">]
[<Entry index=10 label="H2O2">, <Entry index=106 label="InChI=1/C4H9O/c1-3-4(2)5/h4-5H,2-3H2,1H3">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=71 label="O2b">]
[<Entry index=58 label="C/H/Cs2">, <Entry index=101 label="C_methyl">]
[<Entry index=49 label="InChI=1/C4H8/c1-3-4-2/h3H,1,4H2,2H3">, <Entry index=80 label="OOCH3">]
[<Entry index=3 label="H2">, <Entry index=140 label="C_rad/Cs2">]
[<Entry index=3 label="H2">, <Entry index=69 label="H_rad">]
[<Entry index=4 label="Ct_H">, <Entry index=69 label="H_rad">]
[<Entry index=29 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=78 label="InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=21 label="CO_pri">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=32 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=136 label="InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=10 label="H2O2">, <Entry index=82 label="InChI=1/C4H7O/c1-2-3-4-5/h3-4H,2H2,1H3">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=109 label="InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=113 label="C_rad/H2/Ct">]
[<Entry index=21 label="CO_pri">, <Entry index=75 label="O_pri_rad">]
[<Entry index=21 label="CO_pri">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=75 label="O_pri_rad">]
[<Entry index=62 label="C/H/Cs">, <Entry index=101 label="C_methyl">]
[<Entry index=10 label="H2O2">, <Entry index=122 label="InChI=1/C4H9O/c1-3-4(2)5/h3-5H,1-2H3">]
[<Entry index=14 label="Cd_pri">, <Entry index=69 label="H_rad">]
[<Entry index=19 label="Cb_H">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=3 label="H2">, <Entry index=71 label="O2b">]
[<Entry index=14 label="Cd_pri">, <Entry index=71 label="O2b">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=96 label="CO_pri_rad">]
[<Entry index=3 label="H2">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=101 label="C_methyl">]
[<Entry index=26 label="C_methane">, <Entry index=75 label="O_pri_rad">]
[<Entry index=26 label="C_methane">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=3 label="H2">, <Entry index=96 label="CO_pri_rad">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=75 label="O_pri_rad">]
[<Entry index=3 label="H2">, <Entry index=75 label="O_pri_rad">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=116 label="C_rad/H2/O">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=118 label="C_rad/H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 69,
    label = "H_rad",
    group = 
"""
1  *3 H 1
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([66789.6,7662.61,2096.72,885.568,302.646,159.414,68.2695,44.9126],"m^3/(mol*s)","*|/",[104627,5905.91,1169.36,424.493,132.842,71.1794,34.5727,25.6295])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [36, 36, 36, 36, 36, 36, 36, 36] rates.
[<Entry index=8 label="O/H/NonDeC">, <Entry index=69 label="H_rad">]
[<Entry index=17 label="Cd/H/NonDeO">, <Entry index=69 label="H_rad">]
[<Entry index=11 label="O/H/OneDe">, <Entry index=69 label="H_rad">]
[<Entry index=47 label="C/H2/OneDeC">, <Entry index=69 label="H_rad">]
[<Entry index=51 label="C/H2/TwoDe">, <Entry index=69 label="H_rad">]
[<Entry index=3 label="H2">, <Entry index=69 label="H_rad">]
[<Entry index=35 label="C/H3/Ct">, <Entry index=69 label="H_rad">]
[<Entry index=6 label="O_pri">, <Entry index=69 label="H_rad">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=69 label="H_rad">]
[<Entry index=58 label="C/H/Cs2">, <Entry index=69 label="H_rad">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=69 label="H_rad">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=69 label="H_rad">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=69 label="H_rad">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=69 label="H_rad">]
[<Entry index=19 label="Cb_H">, <Entry index=69 label="H_rad">]
[<Entry index=4 label="Ct_H">, <Entry index=69 label="H_rad">]
[<Entry index=26 label="C_methane">, <Entry index=69 label="H_rad">]
[<Entry index=18 label="Cd/H/OneDe">, <Entry index=69 label="H_rad">]
[<Entry index=21 label="CO_pri">, <Entry index=69 label="H_rad">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=69 label="H_rad">]
[<Entry index=38 label="C/H3/O">, <Entry index=69 label="H_rad">]
[<Entry index=14 label="Cd_pri">, <Entry index=69 label="H_rad">]
[<Entry index=59 label="InChI=1/C4H8O/c1-4(2)3-5/h3-4H,1-2H3">, <Entry index=69 label="H_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 70,
    label = "Y_2centeradjbirad",
    group = 
"""
1  *3 {Ct,Os} 1 {2,{S,T}}
2     {Ct,Os} 1 {1,{S,T}}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.00732e-26,9.54e-20,9.02428e-16,3.85363e-13,6.88815e-10,5.74311e-08,1.80231e-05,0.00028395],"m^3/(mol*s)","*|/",[1.38429e+08,1.91236e+06,154768,30046,4136.59,1331.4,331.134,181.614])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [19, 19, 19, 19, 19, 19, 19, 19] rates.
[<Entry index=26 label="C_methane">, <Entry index=72 label="C2b">]
[<Entry index=6 label="O_pri">, <Entry index=71 label="O2b">]
[<Entry index=26 label="C_methane">, <Entry index=71 label="O2b">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=71 label="O2b">]
[<Entry index=21 label="CO_pri">, <Entry index=71 label="O2b">]
[<Entry index=3 label="H2">, <Entry index=71 label="O2b">]
[<Entry index=4 label="Ct_H">, <Entry index=71 label="O2b">]
[<Entry index=14 label="Cd_pri">, <Entry index=71 label="O2b">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=71 label="O2b">]
[<Entry index=19 label="Cb_H">, <Entry index=71 label="O2b">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=71 label="O2b">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=71 label="O2b">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=71 label="O2b">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 71,
    label = "O2b",
    group = 
"""
1  *3 O 1 {2,S}
2     O 1 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([3.78519e-28,4.87703e-21,8.39784e-17,5.34852e-14,1.57686e-10,1.77623e-08,8.33613e-06,0.000160775],"m^3/(mol*s)","*|/",[2.42841e+08,2.97451e+06,224247,41556,5404.96,1682.98,401.381,215.994])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [18, 18, 18, 18, 18, 18, 18, 18] rates.
[<Entry index=6 label="O_pri">, <Entry index=71 label="O2b">]
[<Entry index=26 label="C_methane">, <Entry index=71 label="O2b">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=71 label="O2b">]
[<Entry index=21 label="CO_pri">, <Entry index=71 label="O2b">]
[<Entry index=3 label="H2">, <Entry index=71 label="O2b">]
[<Entry index=4 label="Ct_H">, <Entry index=71 label="O2b">]
[<Entry index=14 label="Cd_pri">, <Entry index=71 label="O2b">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=71 label="O2b">]
[<Entry index=19 label="Cb_H">, <Entry index=71 label="O2b">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=71 label="O2b">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=71 label="O2b">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=71 label="O2b">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 72,
    label = "C2b",
    group = 
"""
1  *3 C 1 {2,T}
2     C 1 {1,T}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([8.76731e+09,4.65942e+07,1.85273e+06,204342,11781.3,1958.36,150.094,36.1757],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=26 label="C_methane">, <Entry index=72 label="C2b">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 73,
    label = "Ct_rad",
    group = 
"""
1  *3 C 1 {2,T}
2     C 0 {1,T}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.93782e+09,9.48776e+06,358592,38194.8,2104.32,339.863,24.9836,5.8819],"m^3/(mol*s)","*|/",[44283.2,2805.47,580.377,216.157,71.5927,41.5862,25.8958,24.1252])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [7, 7, 7, 7, 7, 7, 7, 7] rates.
[<Entry index=28 label="C/H3/Cs">, <Entry index=73 label="Ct_rad">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=73 label="Ct_rad">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=73 label="Ct_rad">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=73 label="Ct_rad">]
[<Entry index=26 label="C_methane">, <Entry index=73 label="Ct_rad">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=73 label="Ct_rad">]
[<Entry index=3 label="H2">, <Entry index=73 label="Ct_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 74,
    label = "O_rad",
    group = 
"""
1  *3 O 1 {2,S}
2     R 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([911.022,127.524,40.1999,18.9358,7.614,4.52071,2.38133,1.80347],"m^3/(mol*s)","*|/",[3898.25,349.909,93.4214,42.2679,18.5561,13.2322,12.0498,15.1579])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [51, 51, 51, 51, 51, 51, 51, 51] rates.
[<Entry index=23 label="CO/H/NonDe">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=10 label="H2O2">, <Entry index=81 label="O_rad/OneDe">]
[<Entry index=6 label="O_pri">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=34 label="InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=21 label="CO_pri">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=75 label="O_pri_rad">]
[<Entry index=21 label="CO_pri">, <Entry index=75 label="O_pri_rad">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=12 label="Orad_O_H">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=75 label="O_pri_rad">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=49 label="InChI=1/C4H8/c1-3-4-2/h3H,1,4H2,2H3">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=49 label="InChI=1/C4H8/c1-3-4-2/h3H,1,4H2,2H3">, <Entry index=80 label="OOCH3">]
[<Entry index=6 label="O_pri">, <Entry index=75 label="O_pri_rad">]
[<Entry index=38 label="C/H3/O">, <Entry index=75 label="O_pri_rad">]
[<Entry index=21 label="CO_pri">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=26 label="C_methane">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=29 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=78 label="InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3">]
[<Entry index=10 label="H2O2">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=78 label="InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3">]
[<Entry index=3 label="H2">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=14 label="Cd_pri">, <Entry index=75 label="O_pri_rad">]
[<Entry index=32 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=78 label="InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3">]
[<Entry index=47 label="C/H2/OneDeC">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=10 label="H2O2">, <Entry index=82 label="InChI=1/C4H7O/c1-2-3-4-5/h3-4H,2H2,1H3">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=83 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/o">]
[<Entry index=10 label="H2O2">, <Entry index=80 label="OOCH3">]
[<Entry index=37 label="C/H3/CO">, <Entry index=75 label="O_pri_rad">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=75 label="O_pri_rad">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=75 label="O_pri_rad">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=75 label="O_pri_rad">]
[<Entry index=26 label="C_methane">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=26 label="C_methane">, <Entry index=75 label="O_pri_rad">]
[<Entry index=19 label="Cb_H">, <Entry index=75 label="O_pri_rad">]
[<Entry index=4 label="Ct_H">, <Entry index=75 label="O_pri_rad">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=75 label="O_pri_rad">]
[<Entry index=3 label="H2">, <Entry index=75 label="O_pri_rad">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=79 label="O_rad/NonDeO">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 75,
    label = "O_pri_rad",
    group = 
"""
1  *3 O 1 {2,S}
2     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([3.62095e+07,503751,39299.8,7242.96,889.376,256.286,50.2754,22.8029],"m^3/(mol*s)","*|/",[67308.6,2757.59,448.343,142.426,37.7859,18.4754,8.24196,6.16565])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [22, 22, 22, 22, 22, 22, 22, 22] rates.
[<Entry index=6 label="O_pri">, <Entry index=75 label="O_pri_rad">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=75 label="O_pri_rad">]
[<Entry index=38 label="C/H3/O">, <Entry index=75 label="O_pri_rad">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=75 label="O_pri_rad">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=75 label="O_pri_rad">]
[<Entry index=21 label="CO_pri">, <Entry index=75 label="O_pri_rad">]
[<Entry index=37 label="C/H3/CO">, <Entry index=75 label="O_pri_rad">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=75 label="O_pri_rad">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=75 label="O_pri_rad">]
[<Entry index=14 label="Cd_pri">, <Entry index=75 label="O_pri_rad">]
[<Entry index=26 label="C_methane">, <Entry index=75 label="O_pri_rad">]
[<Entry index=19 label="Cb_H">, <Entry index=75 label="O_pri_rad">]
[<Entry index=4 label="Ct_H">, <Entry index=75 label="O_pri_rad">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=75 label="O_pri_rad">]
[<Entry index=3 label="H2">, <Entry index=75 label="O_pri_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 76,
    label = "O_sec_rad",
    group = 
"""
1  *3 O 1 {2,S}
2     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.16527,0.696945,0.528827,0.449493,0.381158,0.356605,0.349657,0.365588],"m^3/(mol*s)","*|/",[439.714,70.0806,28.0152,17.3459,12.1727,12.0585,17.7364,28.9123])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [29, 29, 29, 29, 29, 29, 29, 29] rates.
[<Entry index=23 label="CO/H/NonDe">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=10 label="H2O2">, <Entry index=81 label="O_rad/OneDe">]
[<Entry index=6 label="O_pri">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=21 label="CO_pri">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=10 label="H2O2">, <Entry index=80 label="OOCH3">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=34 label="InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=49 label="InChI=1/C4H8/c1-3-4-2/h3H,1,4H2,2H3">, <Entry index=80 label="OOCH3">]
[<Entry index=21 label="CO_pri">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=49 label="InChI=1/C4H8/c1-3-4-2/h3H,1,4H2,2H3">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=12 label="Orad_O_H">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=29 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=78 label="InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3">]
[<Entry index=10 label="H2O2">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=78 label="InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3">]
[<Entry index=3 label="H2">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=32 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=78 label="InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3">]
[<Entry index=47 label="C/H2/OneDeC">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=10 label="H2O2">, <Entry index=82 label="InChI=1/C4H7O/c1-2-3-4-5/h3-4H,2H2,1H3">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=83 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/o">]
[<Entry index=26 label="C_methane">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=26 label="C_methane">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=79 label="O_rad/NonDeO">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 77,
    label = "O_rad/NonDeC",
    group = 
"""
1  *3 O 1 {2,S}
2     Cs 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([7711.31,447.09,81.5694,26.3667,6.48212,2.81375,0.939333,0.549438],"m^3/(mol*s)","*|/",[84.2328,17.3023,8.17639,6.0401,6.50354,9.60503,28.1064,70.8396])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [12, 12, 12, 12, 12, 12, 12, 12] rates.
[<Entry index=54 label="C/H/Cs3">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=29 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=78 label="InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=78 label="InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3">]
[<Entry index=3 label="H2">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=6 label="O_pri">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=26 label="C_methane">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=21 label="CO_pri">, <Entry index=77 label="O_rad/NonDeC">]
[<Entry index=32 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=78 label="InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 78,
    label = "InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3",
    group = 
"""
1     C 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 {1,S} {7,S} {8,S} {9,S}
3     C 0 {1,S} {6,S} {10,S} {11,S}
4     C 0 {1,S} {12,S} {13,S} {14,S}
5     H 0 {1,S}
6  *3 O 1 {3,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {4,S}
14    H 0 {4,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([28839.8,1505.86,280.027,96.7991,28.5127,14.972,7.67391,6.38276],"m^3/(mol*s)","*|/",[1.55644e+06,4441.19,247.828,56.5339,17.737,12.0042,8.25539,10.8059])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [3, 3, 3, 3, 3, 3, 3, 3] rates.
[<Entry index=29 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=78 label="InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3">]
[<Entry index=32 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=78 label="InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=78 label="InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 79,
    label = "O_rad/NonDeO",
    group = 
"""
1  *3 O 1 {2,S}
2     O 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0192699,0.0382171,0.0597816,0.0825384,0.12899,0.174896,0.283796,0.384432],"m^3/(mol*s)","*|/",[2353.93,266.813,89.1491,49.074,28.7189,24.184,25.2779,32.1598])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [14, 14, 14, 14, 14, 14, 14, 14] rates.
[<Entry index=23 label="CO/H/NonDe">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=10 label="H2O2">, <Entry index=80 label="OOCH3">]
[<Entry index=21 label="CO_pri">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=49 label="InChI=1/C4H8/c1-3-4-2/h3H,1,4H2,2H3">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=12 label="Orad_O_H">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=26 label="C_methane">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=34 label="InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=10 label="H2O2">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=47 label="C/H2/OneDeC">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=49 label="InChI=1/C4H8/c1-3-4-2/h3H,1,4H2,2H3">, <Entry index=80 label="OOCH3">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=79 label="O_rad/NonDeO">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=79 label="O_rad/NonDeO">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 80,
    label = "OOCH3",
    group = 
"""
1     O 0 {2,S} {3,S}
2  *3 O 1 {1,S}
3     C 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.113767,0.139253,0.17101,0.207379,0.291523,0.389009,0.684007,1.04481],"m^3/(mol*s)","*|/",[3.11841e+25,1.17023e+18,7.11157e+13,1.43218e+11,7.75405e+07,841840,1247.33,44.1837])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [2, 2, 2, 2, 2, 2, 2, 2] rates.
[<Entry index=10 label="H2O2">, <Entry index=80 label="OOCH3">]
[<Entry index=49 label="InChI=1/C4H8/c1-3-4-2/h3H,1,4H2,2H3">, <Entry index=80 label="OOCH3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 81,
    label = "O_rad/OneDe",
    group = 
"""
1  *3 O 1 {2,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.21655e-05,9.72738e-05,0.000372505,0.000971392,0.00360343,0.00870411,0.0345834,0.080921],"m^3/(mol*s)","*|/",[5.9889e+07,137711,5263.1,765.77,102.841,40.3326,16.584,14.172])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [3, 3, 3, 3, 3, 3, 3, 3] rates.
[<Entry index=10 label="H2O2">, <Entry index=82 label="InChI=1/C4H7O/c1-2-3-4-5/h3-4H,2H2,1H3">]
[<Entry index=10 label="H2O2">, <Entry index=81 label="O_rad/OneDe">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=83 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/o">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 82,
    label = "InChI=1/C4H7O/c1-2-3-4-5/h3-4H,2H2,1H3",
    group = 
"""
1     C 0 {2,S} {3,D}
2     C 0 {1,S} {4,S}
3     C 0 {1,D} {5,S}
4     C 0 {2,S}
5  *3 O 1 {3,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([9.84962e-06,8.68447e-05,0.000338608,0.000869849,0.0030181,0.00672461,0.0219952,0.0436111],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=10 label="H2O2">, <Entry index=82 label="InChI=1/C4H7O/c1-2-3-4-5/h3-4H,2H2,1H3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 83,
    label = "InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/o",
    group = 
"""
1     C 0 {2,S} {4,S} {5,S} {6,S}
2     C 0 {1,S} {3,D} {7,S}
3     C 0 {2,D} {8,S} {9,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {2,S}
8  *3 O 1 {3,S}
9     H 0 {3,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.85587e-05,0.00012204,0.000450821,0.00121142,0.00513663,0.0145827,0.0854966,0.278605],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=83 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/o">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 84,
    label = "Cd_rad",
    group = 
"""
1  *3 C 1 {2,D} {3,S}
2     C 0 {1,D}
3     R 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([3753.74,427.065,116.691,49.3561,16.9699,9.00346,3.92309,2.61911],"m^3/(mol*s)","*|/",[14680.6,1700.44,515.392,244.419,101.829,61.7881,32.5132,24.2741])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [30, 30, 30, 30, 30, 30, 30, 30] rates.
[<Entry index=54 label="C/H/Cs3">, <Entry index=93 label="Cd_rad/OneDe">]
[<Entry index=26 label="C_methane">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=86 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=3 label="H2">, <Entry index=89 label="Cd_rad/NonDeC">]
[<Entry index=6 label="O_pri">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=14 label="Cd_pri">, <Entry index=89 label="Cd_rad/NonDeC">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=89 label="Cd_rad/NonDeC">]
[<Entry index=10 label="H2O2">, <Entry index=87 label="InChI=1/C4H7/c1-3-4-2/h1,3H,4H2,2H3">]
[<Entry index=14 label="Cd_pri">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=90 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=10 label="H2O2">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=10 label="H2O2">, <Entry index=91 label="InChI=1/C4H7/c1-3-4-2/h3H,1-2H3">]
[<Entry index=3 label="H2">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=3 label="H2">, <Entry index=93 label="Cd_rad/OneDe">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=93 label="Cd_rad/OneDe">]
[<Entry index=30 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/gamma">, <Entry index=90 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=21 label="CO_pri">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=10 label="H2O2">, <Entry index=89 label="Cd_rad/NonDeC">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=89 label="Cd_rad/NonDeC">]
[<Entry index=14 label="Cd_pri">, <Entry index=93 label="Cd_rad/OneDe">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 85,
    label = "Cd_pri_rad",
    group = 
"""
1  *3 C 1 {2,D} {3,S}
2     C 0 {1,D}
3     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([10637.2,912.627,213.283,81.9906,25.4054,12.8294,5.38157,3.60319],"m^3/(mol*s)","*|/",[114626,8189.78,1857.04,726.746,239.252,126.66,56.1064,38.6881])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [18, 18, 18, 18, 18, 18, 18, 18] rates.
[<Entry index=10 label="H2O2">, <Entry index=87 label="InChI=1/C4H7/c1-3-4-2/h1,3H,4H2,2H3">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=14 label="Cd_pri">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=10 label="H2O2">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=26 label="C_methane">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=86 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=21 label="CO_pri">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=3 label="H2">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=85 label="Cd_pri_rad">]
[<Entry index=6 label="O_pri">, <Entry index=85 label="Cd_pri_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 86,
    label = "InChI=1/C2H3/c1-2/h1H,2H2",
    group = 
"""
1     C 0 {2,D} {3,S} {4,S}
2  *3 C 1 {1,D} {5,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([85805.2,2716.87,369.849,103.037,22.8547,10.0044,3.92309,2.79814],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=86 label="InChI=1/C2H3/c1-2/h1H,2H2">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 87,
    label = "InChI=1/C4H7/c1-3-4-2/h1,3H,4H2,2H3",
    group = 
"""
1     C 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 {1,S} {7,S} {8,S} {9,S}
3     C 0 {1,S} {4,D} {10,S}
4  *3 C 1 {3,D} {11,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {4,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.83015e+09,6.81572e+06,248221,28063.9,1936.07,406.346,55.5686,22.0928],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=10 label="H2O2">, <Entry index=87 label="InChI=1/C4H7/c1-3-4-2/h1,3H,4H2,2H3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 88,
    label = "Cd_sec_rad",
    group = 
"""
1  *3 C 1 {2,D} {3,S}
2     C 0 {1,D}
3     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([922.914,153.559,51.7901,24.914,9.85453,5.58799,2.56283,1.70435],"m^3/(mol*s)","*|/",[1431.11,296.187,131.291,81.0021,46.8502,34.2916,22.638,18.7216])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [12, 12, 12, 12, 12, 12, 12, 12] rates.
[<Entry index=54 label="C/H/Cs3">, <Entry index=93 label="Cd_rad/OneDe">]
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=90 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=89 label="Cd_rad/NonDeC">]
[<Entry index=30 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/gamma">, <Entry index=90 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=3 label="H2">, <Entry index=89 label="Cd_rad/NonDeC">]
[<Entry index=10 label="H2O2">, <Entry index=89 label="Cd_rad/NonDeC">]
[<Entry index=10 label="H2O2">, <Entry index=91 label="InChI=1/C4H7/c1-3-4-2/h3H,1-2H3">]
[<Entry index=14 label="Cd_pri">, <Entry index=93 label="Cd_rad/OneDe">]
[<Entry index=3 label="H2">, <Entry index=93 label="Cd_rad/OneDe">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=89 label="Cd_rad/NonDeC">]
[<Entry index=14 label="Cd_pri">, <Entry index=89 label="Cd_rad/NonDeC">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=93 label="Cd_rad/OneDe">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 89,
    label = "Cd_rad/NonDeC",
    group = 
"""
1  *3 C 1 {2,D} {3,S}
2     C 0 {1,D}
3     Cs 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([31563.6,1860.41,344.768,113.041,28.482,12.6194,4.38289,2.64025],"m^3/(mol*s)","*|/",[2252.07,574.336,293.696,197.609,123.217,91.5026,58.4992,46.5524])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [8, 8, 8, 8, 8, 8, 8, 8] rates.
[<Entry index=54 label="C/H/Cs3">, <Entry index=89 label="Cd_rad/NonDeC">]
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=90 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=30 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/gamma">, <Entry index=90 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=3 label="H2">, <Entry index=89 label="Cd_rad/NonDeC">]
[<Entry index=10 label="H2O2">, <Entry index=89 label="Cd_rad/NonDeC">]
[<Entry index=10 label="H2O2">, <Entry index=91 label="InChI=1/C4H7/c1-3-4-2/h3H,1-2H3">]
[<Entry index=14 label="Cd_pri">, <Entry index=89 label="Cd_rad/NonDeC">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=89 label="Cd_rad/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 90,
    label = "InChI=1/C3H5/c1-3-2/h1H2,2H3",
    group = 
"""
1     C 0 {3,S} {4,S} {5,S} {6,S}
2     C 0 {3,D} {7,S} {8,S}
3  *3 C 1 {1,S} {2,D}
4     H 0 {1,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {2,S}
8     H 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1300.37,116.211,29.8205,12.7732,4.91636,3.02976,1.92068,1.7754],"m^3/(mol*s)","*|/",[3.26405e+10,1.01342e+08,1.17977e+08,2.65184e+08,4.49626e+08,2.34092e+08,8.09513e+06,241122])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [2, 2, 2, 2, 2, 2, 2, 2] rates.
[<Entry index=30 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/gamma">, <Entry index=90 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=90 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 91,
    label = "InChI=1/C4H7/c1-3-4-2/h3H,1-2H3",
    group = 
"""
1     C 0 {3,S} {5,S} {6,S} {7,S}
2     C 0 {4,S} {8,S} {9,S} {10,S}
3     C 0 {1,S} {4,D} {11,S}
4  *3 C 1 {2,S} {3,D}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([3.66094e+06,59112.8,5209.33,1064.05,154.397,50.8034,12.7491,6.90733],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=10 label="H2O2">, <Entry index=91 label="InChI=1/C4H7/c1-3-4-2/h3H,1-2H3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 92,
    label = "Cd_rad/NonDeO",
    group = 
"""
1  *3 C 1 {2,D} {3,S}
2     C 0 {1,D}
3     O 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 93,
    label = "Cd_rad/OneDe",
    group = 
"""
1  *3 C 1 {2,D} {3,S}
2     C 0 {1,D}
3     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.134926,0.300564,0.452945,0.568154,0.693901,0.729122,0.670067,0.570616],"m^3/(mol*s)","*|/",[234279,6726.38,874.775,237.677,51.2869,22.0886,8.59593,6.41732])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [4, 4, 4, 4, 4, 4, 4, 4] rates.
[<Entry index=14 label="Cd_pri">, <Entry index=93 label="Cd_rad/OneDe">]
[<Entry index=3 label="H2">, <Entry index=93 label="Cd_rad/OneDe">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=93 label="Cd_rad/OneDe">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=93 label="Cd_rad/OneDe">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 94,
    label = "Cb_rad",
    group = 
"""
1  *3 Cb 1 {2,B} {3,B}
2     {Cb,Cbf} 0 {1,B}
3     {Cb,Cbf} 0 {1,B}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([17279.1,965.895,162.118,47.5846,9.64181,3.50454,0.80967,0.35528],"m^3/(mol*s)","*|/",[3.0194e+06,69735.8,11067.2,4694.55,3518.35,5791.32,39514.7,244742])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [3, 3, 3, 3, 3, 3, 3, 3] rates.
[<Entry index=3 label="H2">, <Entry index=94 label="Cb_rad">]
[<Entry index=26 label="C_methane">, <Entry index=94 label="Cb_rad">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=94 label="Cb_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 95,
    label = "CO_rad",
    group = 
"""
1  *3 C 1 {2,D} {3,S}
2     O 0 {1,D}
3     R 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.65679e-05,0.000368542,0.00183541,0.00545144,0.0219606,0.0520825,0.174711,0.335162],"m^3/(mol*s)","*|/",[8912.24,1143.54,338.943,152.122,57.1228,32.7152,17.6518,15.2049])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [12, 12, 12, 12, 12, 12, 12, 12] rates.
[<Entry index=21 label="CO_pri">, <Entry index=98 label="CO_rad/NonDe">]
[<Entry index=26 label="C_methane">, <Entry index=98 label="CO_rad/NonDe">]
[<Entry index=3 label="H2">, <Entry index=96 label="CO_pri_rad">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=98 label="CO_rad/NonDe">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=96 label="CO_pri_rad">]
[<Entry index=3 label="H2">, <Entry index=98 label="CO_rad/NonDe">]
[<Entry index=26 label="C_methane">, <Entry index=96 label="CO_pri_rad">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=98 label="CO_rad/NonDe">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=98 label="CO_rad/NonDe">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=96 label="CO_pri_rad">]
[<Entry index=6 label="O_pri">, <Entry index=96 label="CO_pri_rad">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=96 label="CO_pri_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 96,
    label = "CO_pri_rad",
    group = 
"""
1  *3 C 1 {2,D} {3,S}
2     O 0 {1,D}
3     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([9.50456e-06,0.000188453,0.00116515,0.00400266,0.0193852,0.0514473,0.201341,0.418566],"m^3/(mol*s)","*|/",[283297,14801.4,2539.61,781.504,175.482,69.7998,19.3814,10.2336])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [6, 6, 6, 6, 6, 6, 6, 6] rates.
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=96 label="CO_pri_rad">]
[<Entry index=26 label="C_methane">, <Entry index=96 label="CO_pri_rad">]
[<Entry index=3 label="H2">, <Entry index=96 label="CO_pri_rad">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=96 label="CO_pri_rad">]
[<Entry index=6 label="O_pri">, <Entry index=96 label="CO_pri_rad">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=96 label="CO_pri_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 97,
    label = "CO_sec_rad",
    group = 
"""
1  *3 C 1 {2,D} {3,S}
2     O 0 {1,D}
3     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([7.42648e-05,0.000720727,0.00289123,0.00742462,0.0248781,0.0527255,0.151604,0.268377],"m^3/(mol*s)","*|/",[13630.8,1850.81,575.523,271.226,113.648,73.6194,54.2264,60.4101])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [6, 6, 6, 6, 6, 6, 6, 6] rates.
[<Entry index=26 label="C_methane">, <Entry index=98 label="CO_rad/NonDe">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=98 label="CO_rad/NonDe">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=98 label="CO_rad/NonDe">]
[<Entry index=3 label="H2">, <Entry index=98 label="CO_rad/NonDe">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=98 label="CO_rad/NonDe">]
[<Entry index=21 label="CO_pri">, <Entry index=98 label="CO_rad/NonDe">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 98,
    label = "CO_rad/NonDe",
    group = 
"""
1  *3 C 1 {2,D} {3,S}
2     O 0 {1,D}
3     {Cs,O} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([7.42648e-05,0.000720727,0.00289123,0.00742462,0.0248781,0.0527255,0.151604,0.268377],"m^3/(mol*s)","*|/",[13630.8,1850.81,575.523,271.226,113.648,73.6194,54.2264,60.4101])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [6, 6, 6, 6, 6, 6, 6, 6] rates.
[<Entry index=26 label="C_methane">, <Entry index=98 label="CO_rad/NonDe">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=98 label="CO_rad/NonDe">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=98 label="CO_rad/NonDe">]
[<Entry index=3 label="H2">, <Entry index=98 label="CO_rad/NonDe">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=98 label="CO_rad/NonDe">]
[<Entry index=21 label="CO_pri">, <Entry index=98 label="CO_rad/NonDe">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 99,
    label = "CO_rad/OneDe",
    group = 
"""
1  *3 C 1 {2,D} {3,S}
2     O 0 {1,D}
3     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 100,
    label = "Cs_rad",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     R 0 {1,S}
3     R 0 {1,S}
4     R 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.209023,0.278418,0.330504,0.370409,0.426874,0.464567,0.519483,0.548857],"m^3/(mol*s)","*|/",[2270.22,433.123,184.976,112.261,64.5746,47.7093,32.7648,28.2066])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [140, 140, 140, 140, 140, 140, 140, 140] rates.
[<Entry index=10 label="H2O2">, <Entry index=120 label="InChI=1/C4H9O/c1-2-3-4-5/h2,5H,3-4H2,1H3">]
[<Entry index=3 label="H2">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=36 label="C/H3/Cb">, <Entry index=101 label="C_methyl">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=101 label="C_methyl">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=10 label="H2O2">, <Entry index=121 label="InChI=1/C4H9O/c1-2-3-4-5/h3,5H,2,4H2,1H3">]
[<Entry index=10 label="H2O2">, <Entry index=111 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=26 label="C_methane">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=32 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=109 label="InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=101 label="C_methyl">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=101 label="C_methyl">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=101 label="C_methyl">]
[<Entry index=3 label="H2">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=4 label="Ct_H">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=48 label="InChI=1/C3H6O/c1-2-3-4/h3H,2H2,1H3/beta">, <Entry index=109 label="InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3">]
[<Entry index=21 label="CO_pri">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=101 label="C_methyl">]
[<Entry index=18 label="Cd/H/OneDe">, <Entry index=101 label="C_methyl">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=101 label="C_methyl">]
[<Entry index=26 label="C_methane">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=10 label="H2O2">, <Entry index=105 label="InChI=1/C4H9O/c1-2-3-4-5/h5H,1-4H2">]
[<Entry index=14 label="Cd_pri">, <Entry index=140 label="C_rad/Cs2">]
[<Entry index=29 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=109 label="InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3">]
[<Entry index=11 label="O/H/OneDe">, <Entry index=101 label="C_methyl">]
[<Entry index=51 label="C/H2/TwoDe">, <Entry index=101 label="C_methyl">]
[<Entry index=26 label="C_methane">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=126 label="InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3">]
[<Entry index=14 label="Cd_pri">, <Entry index=129 label="C_rad/H/OneDeC">]
[<Entry index=26 label="C_methane">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=129 label="C_rad/H/OneDeC">]
[<Entry index=14 label="Cd_pri">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=113 label="C_rad/H2/Ct">]
[<Entry index=14 label="Cd_pri">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=21 label="CO_pri">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=26 label="C_methane">, <Entry index=101 label="C_methyl">]
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=130 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c">]
[<Entry index=14 label="Cd_pri">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=4 label="Ct_H">, <Entry index=101 label="C_methyl">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=3 label="H2">, <Entry index=113 label="C_rad/H2/Ct">]
[<Entry index=14 label="Cd_pri">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=119 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=10 label="H2O2">, <Entry index=125 label="InChI=1/C4H9O/c1-2-3-4-5/h4-5H,2-3H2,1H3">]
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=119 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=140 label="C_rad/Cs2">]
[<Entry index=14 label="Cd_pri">, <Entry index=113 label="C_rad/H2/Ct">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=104 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=35 label="C/H3/Ct">, <Entry index=101 label="C_methyl">]
[<Entry index=32 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=126 label="InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=6 label="O_pri">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=3 label="H2">, <Entry index=101 label="C_methyl">]
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=104 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=3 label="H2">, <Entry index=129 label="C_rad/H/OneDeC">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=19 label="Cb_H">, <Entry index=101 label="C_methyl">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=10 label="H2O2">, <Entry index=122 label="InChI=1/C4H9O/c1-3-4(2)5/h3-5H,1-2H3">]
[<Entry index=41 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=136 label="InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3">]
[<Entry index=10 label="H2O2">, <Entry index=108 label="InChI=1/C4H9O/c1-4(2,3)5/h5H,1H2,2-3H3">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=129 label="C_rad/H/OneDeC">]
[<Entry index=6 label="O_pri">, <Entry index=101 label="C_methyl">]
[<Entry index=10 label="H2O2">, <Entry index=138 label="InChI=1/C4H9O/c1-3-4(2)5/h5H,3H2,1-2H3">]
[<Entry index=3 label="H2">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=3 label="H2">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=47 label="C/H2/OneDeC">, <Entry index=101 label="C_methyl">]
[<Entry index=38 label="C/H3/O">, <Entry index=101 label="C_methyl">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=136 label="InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=21 label="CO_pri">, <Entry index=101 label="C_methyl">]
[<Entry index=14 label="Cd_pri">, <Entry index=101 label="C_methyl">]
[<Entry index=10 label="H2O2">, <Entry index=107 label="InChI=1/C4H9O/c1-3-4(2)5/h4-5H,1,3H2,2H3">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=140 label="C_rad/Cs2">]
[<Entry index=10 label="H2O2">, <Entry index=106 label="InChI=1/C4H9O/c1-3-4(2)5/h4-5H,2-3H2,1H3">]
[<Entry index=58 label="C/H/Cs2">, <Entry index=101 label="C_methyl">]
[<Entry index=3 label="H2">, <Entry index=140 label="C_rad/Cs2">]
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=130 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=21 label="CO_pri">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=32 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=136 label="InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=109 label="InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=113 label="C_rad/H2/Ct">]
[<Entry index=21 label="CO_pri">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=62 label="C/H/Cs">, <Entry index=101 label="C_methyl">]
[<Entry index=19 label="Cb_H">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=101 label="C_methyl">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=116 label="C_rad/H2/O">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=118 label="C_rad/H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 101,
    label = "C_methyl",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([9.89491,8.93779,8.13958,7.48412,6.48428,5.75937,4.58742,3.87642],"m^3/(mol*s)","*|/",[7175.46,1677.09,798.266,509.657,298.406,214.64,132.228,101.929])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [53, 53, 53, 53, 53, 53, 53, 53] rates.
[<Entry index=6 label="O_pri">, <Entry index=101 label="C_methyl">]
[<Entry index=18 label="Cd/H/OneDe">, <Entry index=101 label="C_methyl">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=101 label="C_methyl">]
[<Entry index=47 label="C/H2/OneDeC">, <Entry index=101 label="C_methyl">]
[<Entry index=38 label="C/H3/O">, <Entry index=101 label="C_methyl">]
[<Entry index=36 label="C/H3/Cb">, <Entry index=101 label="C_methyl">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=101 label="C_methyl">]
[<Entry index=11 label="O/H/OneDe">, <Entry index=101 label="C_methyl">]
[<Entry index=51 label="C/H2/TwoDe">, <Entry index=101 label="C_methyl">]
[<Entry index=21 label="CO_pri">, <Entry index=101 label="C_methyl">]
[<Entry index=35 label="C/H3/Ct">, <Entry index=101 label="C_methyl">]
[<Entry index=14 label="Cd_pri">, <Entry index=101 label="C_methyl">]
[<Entry index=3 label="H2">, <Entry index=101 label="C_methyl">]
[<Entry index=58 label="C/H/Cs2">, <Entry index=101 label="C_methyl">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=101 label="C_methyl">]
[<Entry index=26 label="C_methane">, <Entry index=101 label="C_methyl">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=101 label="C_methyl">]
[<Entry index=62 label="C/H/Cs">, <Entry index=101 label="C_methyl">]
[<Entry index=19 label="Cb_H">, <Entry index=101 label="C_methyl">]
[<Entry index=4 label="Ct_H">, <Entry index=101 label="C_methyl">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=101 label="C_methyl">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=101 label="C_methyl">]
[<Entry index=16 label="Cd/H/NonDeC">, <Entry index=101 label="C_methyl">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 102,
    label = "C_pri_rad",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0457175,0.0702339,0.0931769,0.114387,0.152259,0.185348,0.25416,0.310426],"m^3/(mol*s)","*|/",[1842.77,210.11,64.3143,31.5501,14.7592,10.3863,8.09802,8.61261])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [37, 37, 37, 37, 37, 37, 37, 37] rates.
[<Entry index=54 label="C/H/Cs3">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=3 label="H2">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=10 label="H2O2">, <Entry index=105 label="InChI=1/C4H9O/c1-2-3-4-5/h5H,1-4H2">]
[<Entry index=14 label="Cd_pri">, <Entry index=113 label="C_rad/H2/Ct">]
[<Entry index=29 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=109 label="InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3">]
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=104 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=26 label="C_methane">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=10 label="H2O2">, <Entry index=108 label="InChI=1/C4H9O/c1-4(2,3)5/h5H,1H2,2-3H3">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=6 label="O_pri">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=104 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=10 label="H2O2">, <Entry index=107 label="InChI=1/C4H9O/c1-3-4(2)5/h4-5H,1,3H2,2H3">]
[<Entry index=10 label="H2O2">, <Entry index=111 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=10 label="H2O2">, <Entry index=106 label="InChI=1/C4H9O/c1-3-4(2)5/h4-5H,2-3H2,1H3">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=113 label="C_rad/H2/Ct">]
[<Entry index=14 label="Cd_pri">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=26 label="C_methane">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=21 label="CO_pri">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=109 label="InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=113 label="C_rad/H2/Ct">]
[<Entry index=21 label="CO_pri">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=32 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=109 label="InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=48 label="InChI=1/C3H6O/c1-2-3-4/h3H,2H2,1H3/beta">, <Entry index=109 label="InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3">]
[<Entry index=3 label="H2">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=19 label="Cb_H">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=4 label="Ct_H">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=3 label="H2">, <Entry index=113 label="C_rad/H2/Ct">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=116 label="C_rad/H2/O">]
[<Entry index=14 label="Cd_pri">, <Entry index=110 label="C_rad/H2/Cd">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 103,
    label = "C_rad/H2/Cs",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.19492,0.596441,0.413994,0.335902,0.275004,0.256865,0.261956,0.288599],"m^3/(mol*s)","*|/",[684.778,105.639,40.0778,23.0693,13.3757,10.7178,9.8738,11.4775])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [24, 24, 24, 24, 24, 24, 24, 24] rates.
[<Entry index=54 label="C/H/Cs3">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=3 label="H2">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=10 label="H2O2">, <Entry index=105 label="InChI=1/C4H9O/c1-2-3-4-5/h5H,1-4H2">]
[<Entry index=29 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=109 label="InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3">]
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=104 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=26 label="C_methane">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=6 label="O_pri">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=104 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=10 label="H2O2">, <Entry index=107 label="InChI=1/C4H9O/c1-3-4(2)5/h4-5H,1,3H2,2H3">]
[<Entry index=10 label="H2O2">, <Entry index=106 label="InChI=1/C4H9O/c1-3-4(2)5/h4-5H,2-3H2,1H3">]
[<Entry index=14 label="Cd_pri">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=109 label="InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3">]
[<Entry index=21 label="CO_pri">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=32 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=109 label="InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=10 label="H2O2">, <Entry index=108 label="InChI=1/C4H9O/c1-4(2,3)5/h5H,1H2,2-3H3">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=19 label="Cb_H">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=4 label="Ct_H">, <Entry index=103 label="C_rad/H2/Cs">]
[<Entry index=48 label="InChI=1/C3H6O/c1-2-3-4/h3H,2H2,1H3/beta">, <Entry index=109 label="InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 104,
    label = "InChI=1/C2H5/c1-2/h1H2,2H3",
    group = 
"""
1     C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 C 1 {1,S} {6,S} {7,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.19038,0.403059,0.239369,0.184211,0.154611,0.158301,0.21504,0.311163],"m^3/(mol*s)","*|/",[3.26589e+08,506.53,8913.43,482725,2.29382e+07,6.02703e+07,1.02191e+07,370386])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [2, 2, 2, 2, 2, 2, 2, 2] rates.
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=104 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=104 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 105,
    label = "InChI=1/C4H9O/c1-2-3-4-5/h5H,1-4H2",
    group = 
"""
1     C 0 {2,S} {3,S} {6,S} {7,S}
2     C 0 {1,S} {4,S} {8,S} {9,S}
3     C 0 {1,S} {5,S} {10,S} {11,S}
4  *3 C 1 {2,S} {12,S} {13,S}
5     O 0 {3,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([683.426,72.376,19.2907,8.12259,2.83738,1.54761,0.727351,0.519947],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=10 label="H2O2">, <Entry index=105 label="InChI=1/C4H9O/c1-2-3-4-5/h5H,1-4H2">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 106,
    label = "InChI=1/C4H9O/c1-3-4(2)5/h4-5H,2-3H2,1H3",
    group = 
"""
1     C 0 {2,S} {3,S} {6,S} {7,S}
2     C 0 {1,S} {4,S} {5,S} {8,S}
3     C 0 {1,S} {9,S} {10,S} {11,S}
4  *3 C 1 {2,S} {12,S} {13,S}
5     O 0 {2,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([164.404,26.7471,9.39777,4.81684,2.19953,1.43549,0.891929,0.756517],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=10 label="H2O2">, <Entry index=106 label="InChI=1/C4H9O/c1-3-4(2)5/h4-5H,2-3H2,1H3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 107,
    label = "InChI=1/C4H9O/c1-3-4(2)5/h4-5H,1,3H2,2H3",
    group = 
"""
1     C 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 {1,S} {4,S} {7,S} {8,S}
3     C 0 {1,S} {9,S} {10,S} {11,S}
4  *3 C 1 {2,S} {12,S} {13,S}
5     O 0 {1,S} {14,S}
6     H 0 {1,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([632.792,55.7009,13.1403,5.06298,1.56219,0.782194,0.320281,0.209747],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=10 label="H2O2">, <Entry index=107 label="InChI=1/C4H9O/c1-3-4(2)5/h4-5H,1,3H2,2H3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 108,
    label = "InChI=1/C4H9O/c1-4(2,3)5/h5H,1H2,2-3H3",
    group = 
"""
1     C 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 {1,S} {9,S} {10,S} {11,S}
4  *3 C 1 {1,S} {12,S} {13,S}
5     O 0 {1,S} {14,S}
6     H 0 {2,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([105.677,17.4835,6.20511,3.20185,1.47438,0.967089,0.604937,0.51482],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=10 label="H2O2">, <Entry index=108 label="InChI=1/C4H9O/c1-4(2,3)5/h5H,1H2,2-3H3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 109,
    label = "InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3",
    group = 
"""
1     C 0 {2,S} {3,S} {4,S} {6,S}
2     C 0 {1,S} {5,S} {7,S} {8,S}
3     C 0 {1,S} {9,S} {10,S} {11,S}
4  *3 C 1 {1,S} {12,S} {13,S}
5     O 0 {2,S} {14,S}
6     H 0 {1,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.1047,0.560123,0.287158,0.200013,0.147753,0.139767,0.169919,0.231607],"m^3/(mol*s)","*|/",[28168,430.483,65.7295,30.1273,20.733,19.0738,12.662,7.23521])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [4, 4, 4, 4, 4, 4, 4, 4] rates.
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=109 label="InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3">]
[<Entry index=48 label="InChI=1/C3H6O/c1-2-3-4/h3H,2H2,1H3/beta">, <Entry index=109 label="InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3">]
[<Entry index=32 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=109 label="InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3">]
[<Entry index=29 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=109 label="InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 110,
    label = "C_rad/H2/Cd",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cd 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.27137e-05,0.000297782,0.0019256,0.00657101,0.0295681,0.0710606,0.216591,0.362217],"m^3/(mol*s)","*|/",[1.28531e+06,20341.8,1883.16,414.121,71.086,27.7726,10.6682,8.75264])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [8, 8, 8, 8, 8, 8, 8, 8] rates.
[<Entry index=31 label="C/H3/Cd">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=26 label="C_methane">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=3 label="H2">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=21 label="CO_pri">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=10 label="H2O2">, <Entry index=111 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=23 label="CO/H/NonDe">, <Entry index=110 label="C_rad/H2/Cd">]
[<Entry index=14 label="Cd_pri">, <Entry index=110 label="C_rad/H2/Cd">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 111,
    label = "InChI=1/C3H5/c1-3-2/h3H,1-2H2",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     C 0 {1,S} {5,D}
3     H 0 {1,S}
4     H 0 {1,S}
5     C 0 {2,D}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.000406289,0.00266254,0.00889705,0.0209495,0.0670492,0.145747,0.485275,1.01033],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=10 label="H2O2">, <Entry index=111 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 112,
    label = "InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3",
    group = 
"""
1     C 0 {2,S} {5,S} {6,S} {7,S}
2     C 0 {1,S} {3,D} {4,S}
3     C 0 {2,D} {8,S} {9,S}
4  *3 C 1 {2,S} {10,S} {11,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {3,S}
9     H 0 {3,S}
10    H 0 {4,S}
11    H 0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 113,
    label = "C_rad/H2/Ct",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Ct 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.000250568,0.00370606,0.0173904,0.0465144,0.146384,0.271418,0.531882,0.66141],"m^3/(mol*s)","*|/",[2356.79,364.465,143.321,84.8657,49.2498,37.0672,25.2415,20.1807])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [4, 4, 4, 4, 4, 4, 4, 4] rates.
[<Entry index=3 label="H2">, <Entry index=113 label="C_rad/H2/Ct">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=113 label="C_rad/H2/Ct">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=113 label="C_rad/H2/Ct">]
[<Entry index=14 label="Cd_pri">, <Entry index=113 label="C_rad/H2/Ct">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 114,
    label = "C_rad/H2/Cb",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cb 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 115,
    label = "C_rad/H2/CO",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     CO 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 116,
    label = "C_rad/H2/O",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     O 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.000836211,0.00196993,0.00349177,0.00531602,0.00963181,0.0145846,0.0287219,0.0444556],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=116 label="C_rad/H2/O">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 117,
    label = "C_sec_rad",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     R!H 0 {1,S}
4     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0282235,0.0394479,0.0494871,0.0585584,0.0745134,0.0883572,0.117189,0.140952],"m^3/(mol*s)","*|/",[437.166,76.3578,31.2272,18.6547,10.7216,7.94663,5.39603,4.65096])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [28, 28, 28, 28, 28, 28, 28, 28] rates.
[<Entry index=10 label="H2O2">, <Entry index=120 label="InChI=1/C4H9O/c1-2-3-4-5/h2,5H,3-4H2,1H3">]
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=119 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=129 label="C_rad/H/OneDeC">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=126 label="InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3">]
[<Entry index=3 label="H2">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=10 label="H2O2">, <Entry index=125 label="InChI=1/C4H9O/c1-2-3-4-5/h4-5H,2-3H2,1H3">]
[<Entry index=26 label="C_methane">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=119 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=32 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=126 label="InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3">]
[<Entry index=10 label="H2O2">, <Entry index=121 label="InChI=1/C4H9O/c1-2-3-4-5/h3,5H,2,4H2,1H3">]
[<Entry index=14 label="Cd_pri">, <Entry index=129 label="C_rad/H/OneDeC">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=129 label="C_rad/H/OneDeC">]
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=130 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c">]
[<Entry index=3 label="H2">, <Entry index=129 label="C_rad/H/OneDeC">]
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=130 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=14 label="Cd_pri">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=10 label="H2O2">, <Entry index=122 label="InChI=1/C4H9O/c1-3-4(2)5/h3-5H,1-2H3">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=21 label="CO_pri">, <Entry index=118 label="C_rad/H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 118,
    label = "C_rad/H/NonDeC",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.875068,0.447698,0.310765,0.249694,0.198449,0.179421,0.169767,0.175741],"m^3/(mol*s)","*|/",[745.958,143.725,60.5781,35.8327,19.2461,13.216,7.90449,6.57586])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [15, 15, 15, 15, 15, 15, 15, 15] rates.
[<Entry index=8 label="O/H/NonDeC">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=10 label="H2O2">, <Entry index=120 label="InChI=1/C4H9O/c1-2-3-4-5/h2,5H,3-4H2,1H3">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=14 label="Cd_pri">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=10 label="H2O2">, <Entry index=122 label="InChI=1/C4H9O/c1-3-4(2)5/h3-5H,1-2H3">]
[<Entry index=10 label="H2O2">, <Entry index=121 label="InChI=1/C4H9O/c1-2-3-4-5/h3,5H,2,4H2,1H3">]
[<Entry index=3 label="H2">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=26 label="C_methane">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=21 label="CO_pri">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=119 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=119 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=118 label="C_rad/H/NonDeC">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=118 label="C_rad/H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 119,
    label = "InChI=1/C3H7/c1-3-2/h3H,1-2H3",
    group = 
"""
1     C 0 {3,S} {4,S} {5,S} {6,S}
2     C 0 {3,S} {7,S} {8,S} {9,S}
3  *3 C 1 {1,S} {2,S} {10,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.346349,0.112957,0.0656901,0.0499011,0.0412825,0.0419669,0.0566515,0.0819259],"m^3/(mol*s)","*|/",[4.5774e+07,1.9303,3289.96,434843,3.63696e+07,1.2767e+08,3.78878e+07,2.54473e+06])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [2, 2, 2, 2, 2, 2, 2, 2] rates.
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=119 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=119 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 120,
    label = "InChI=1/C4H9O/c1-2-3-4-5/h2,5H,3-4H2,1H3",
    group = 
"""
1     C 0 {2,S} {4,S} {6,S} {7,S}
2     C 0 {1,S} {5,S} {8,S} {9,S}
3     C 0 {4,S} {10,S} {11,S} {12,S}
4  *3 C 1 {1,S} {3,S} {13,S}
5     O 0 {2,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([225.572,34.2385,11.4754,5.67859,2.46529,1.55225,0.908585,0.741024],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=10 label="H2O2">, <Entry index=120 label="InChI=1/C4H9O/c1-2-3-4-5/h2,5H,3-4H2,1H3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 121,
    label = "InChI=1/C4H9O/c1-2-3-4-5/h3,5H,2,4H2,1H3",
    group = 
"""
1     C 0 {3,S} {4,S} {6,S} {7,S}
2     C 0 {4,S} {5,S} {11,S} {12,S}
3     C 0 {1,S} {8,S} {9,S} {10,S}
4  *3 C 1 {1,S} {2,S} {13,S}
5     O 0 {2,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {3,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {2,S}
12    H 0 {2,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([137.463,23.1575,8.30437,4.31329,2.00134,1.31808,0.828068,0.70564],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=10 label="H2O2">, <Entry index=121 label="InChI=1/C4H9O/c1-2-3-4-5/h3,5H,2,4H2,1H3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 122,
    label = "InChI=1/C4H9O/c1-3-4(2)5/h3-5H,1-2H3",
    group = 
"""
1     C 0 {2,S} {4,S} {5,S} {6,S}
2     C 0 {1,S} {7,S} {8,S} {9,S}
3     C 0 {4,S} {10,S} {11,S} {12,S}
4  *3 C 1 {1,S} {3,S} {13,S}
5     O 0 {1,S} {14,S}
6     H 0 {1,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([349.195,21.1581,3.98332,1.31915,0.336241,0.149896,0.0524017,0.0316281],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=10 label="H2O2">, <Entry index=122 label="InChI=1/C4H9O/c1-3-4(2)5/h3-5H,1-2H3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 123,
    label = "C_rad/H/NonDeO",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     O 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([46.4435,7.35372,2.70269,1.48673,0.797351,0.609313,0.532559,0.593863],"m^3/(mol*s)","*|/",[2.18094e+07,44850.7,1927.83,353.035,80.0469,45.8151,23.6763,15.4788])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [3, 3, 3, 3, 3, 3, 3, 3] rates.
[<Entry index=10 label="H2O2">, <Entry index=125 label="InChI=1/C4H9O/c1-2-3-4-5/h4-5H,2-3H2,1H3">]
[<Entry index=32 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=126 label="InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=126 label="InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 124,
    label = "C_rad/H/CsO",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
4     O 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([46.4435,7.35372,2.70269,1.48673,0.797351,0.609313,0.532559,0.593863],"m^3/(mol*s)","*|/",[2.18094e+07,44850.7,1927.83,353.035,80.0469,45.8151,23.6763,15.4788])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [3, 3, 3, 3, 3, 3, 3, 3] rates.
[<Entry index=10 label="H2O2">, <Entry index=125 label="InChI=1/C4H9O/c1-2-3-4-5/h4-5H,2-3H2,1H3">]
[<Entry index=32 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=126 label="InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=126 label="InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 125,
    label = "InChI=1/C4H9O/c1-2-3-4-5/h4-5H,2-3H2,1H3",
    group = 
"""
1     C 0 {2,S} {3,S} {6,S} {7,S}
2     C 0 {1,S} {4,S} {8,S} {9,S}
3     C 0 {1,S} {10,S} {11,S} {12,S}
4  *3 C 1 {2,S} {5,S} {13,S}
5     O 0 {4,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([439.794,65.3531,21.5941,10.5742,4.52266,2.818,1.62135,1.30768],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=10 label="H2O2">, <Entry index=125 label="InChI=1/C4H9O/c1-2-3-4-5/h4-5H,2-3H2,1H3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 126,
    label = "InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3",
    group = 
"""
1     C 0 {2,S} {3,S} {4,S} {6,S}
2     C 0 {1,S} {7,S} {8,S} {9,S}
3     C 0 {1,S} {10,S} {11,S} {12,S}
4  *3 C 1 {1,S} {5,S} {13,S}
5     O 0 {4,S} {14,S}
6     H 0 {1,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([15.0926,2.46676,0.956153,0.557475,0.334794,0.283328,0.30522,0.400201],"m^3/(mol*s)","*|/",[2.52959e+22,1.07722e+13,4.65401e+08,5.93061e+06,794688,705598,264320,67105.6])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [2, 2, 2, 2, 2, 2, 2, 2] rates.
[<Entry index=32 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=126 label="InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=126 label="InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 127,
    label = "C_rad/H/O2",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     O 0 {1,S}
4     O 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 128,
    label = "C_rad/H/OneDe",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([7.21443e-06,0.000113934,0.000583847,0.00171056,0.00639057,0.0137897,0.0367098,0.0577501],"m^3/(mol*s)","*|/",[630.619,76.2637,25.6407,13.9448,7.7776,6.04418,4.63187,4.13657])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [10, 10, 10, 10, 10, 10, 10, 10] rates.
[<Entry index=54 label="C/H/Cs3">, <Entry index=129 label="C_rad/H/OneDeC">]
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=130 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c">]
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=130 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=129 label="C_rad/H/OneDeC">]
[<Entry index=3 label="H2">, <Entry index=129 label="C_rad/H/OneDeC">]
[<Entry index=14 label="Cd_pri">, <Entry index=129 label="C_rad/H/OneDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 129,
    label = "C_rad/H/OneDeC",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([7.21443e-06,0.000113934,0.000583847,0.00171056,0.00639057,0.0137897,0.0367098,0.0577501],"m^3/(mol*s)","*|/",[630.619,76.2637,25.6407,13.9448,7.7776,6.04418,4.63187,4.13657])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [10, 10, 10, 10, 10, 10, 10, 10] rates.
[<Entry index=54 label="C/H/Cs3">, <Entry index=129 label="C_rad/H/OneDeC">]
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=130 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c">]
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=130 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=129 label="C_rad/H/OneDeC">]
[<Entry index=3 label="H2">, <Entry index=129 label="C_rad/H/OneDeC">]
[<Entry index=14 label="Cd_pri">, <Entry index=129 label="C_rad/H/OneDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 130,
    label = "InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c",
    group = 
"""
1     C 0 {2,S} {4,S} {5,S} {6,S}
2  *3 C 1 {1,S} {3,S} {7,S}
3     C 0 {2,S} {8,D} {9,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {2,S}
8     O 0 {3,D}
9     H 0 {3,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.00239587,0.00367504,0.00520859,0.00698618,0.0112443,0.016403,0.0330348,0.0547266],"m^3/(mol*s)","*|/",[1.94951e+12,3.08797e+06,425639,1.91193e+06,2.5482e+07,5.90884e+07,1.91783e+07,2.25562e+06])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [2, 2, 2, 2, 2, 2, 2, 2] rates.
[<Entry index=44 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha">, <Entry index=130 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c">]
[<Entry index=55 label="InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta">, <Entry index=130 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 131,
    label = "C_rad/H/OneDeO",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     O 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 132,
    label = "C_rad/H/TwoDe",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 133,
    label = "C_ter_rad",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     R!H 0 {1,S}
3     R!H 0 {1,S}
4     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.00331696,0.00846339,0.0148141,0.0214849,0.0341059,0.0449052,0.0644994,0.0770172],"m^3/(mol*s)","*|/",[6435.8,942.861,337.634,181.691,90.9658,63.1339,42.5425,38.4508])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [22, 22, 22, 22, 22, 22, 22, 22] rates.
[<Entry index=54 label="C/H/Cs3">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=14 label="Cd_pri">, <Entry index=140 label="C_rad/Cs2">]
[<Entry index=14 label="Cd_pri">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=3 label="H2">, <Entry index=140 label="C_rad/Cs2">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=41 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=136 label="InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3">]
[<Entry index=3 label="H2">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=21 label="CO_pri">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=32 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=136 label="InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=140 label="C_rad/Cs2">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=140 label="C_rad/Cs2">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=136 label="InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3">]
[<Entry index=10 label="H2O2">, <Entry index=138 label="InChI=1/C4H9O/c1-3-4(2)5/h5H,3H2,1-2H3">]
[<Entry index=26 label="C_methane">, <Entry index=135 label="C_rad/Cs3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 134,
    label = "C_rad/NonDeC",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     {Cs,O} 0 {1,S}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.4261,0.651369,0.419996,0.32006,0.236491,0.203506,0.178103,0.17563],"m^3/(mol*s)","*|/",[3386.48,644.324,303.906,206.153,142.68,120.624,104.005,105.477])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [14, 14, 14, 14, 14, 14, 14, 14] rates.
[<Entry index=54 label="C/H/Cs3">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=14 label="Cd_pri">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=3 label="H2">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=21 label="CO_pri">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=32 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=136 label="InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=41 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=136 label="InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=136 label="InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3">]
[<Entry index=10 label="H2O2">, <Entry index=138 label="InChI=1/C4H9O/c1-3-4(2)5/h5H,3H2,1-2H3">]
[<Entry index=26 label="C_methane">, <Entry index=135 label="C_rad/Cs3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 135,
    label = "C_rad/Cs3",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     Cs 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.73561,0.383667,0.268196,0.215852,0.170995,0.153601,0.142698,0.145264],"m^3/(mol*s)","*|/",[3611.29,726.481,356.829,248.337,176.219,150.35,130.404,132.723])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [13, 13, 13, 13, 13, 13, 13, 13] rates.
[<Entry index=54 label="C/H/Cs3">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=14 label="Cd_pri">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=31 label="C/H3/Cd">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=3 label="H2">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=21 label="CO_pri">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=32 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=136 label="InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3">]
[<Entry index=8 label="O/H/NonDeC">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=41 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=136 label="InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3">]
[<Entry index=40 label="C/H2/NonDeC">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=28 label="C/H3/Cs">, <Entry index=135 label="C_rad/Cs3">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=136 label="InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3">]
[<Entry index=26 label="C_methane">, <Entry index=135 label="C_rad/Cs3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 136,
    label = "InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3",
    group = 
"""
1     C 0 {4,S} {5,S} {6,S} {7,S}
2     C 0 {4,S} {8,S} {9,S} {10,S}
3     C 0 {4,S} {11,S} {12,S} {13,S}
4  *3 C 1 {1,S} {2,S} {3,S}
5     O 0 {1,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {3,S}
14    H 0 {5,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([7.03509,0.991312,0.348387,0.18915,0.102816,0.0812267,0.0783196,0.0956998],"m^3/(mol*s)","*|/",[261322,669.39,56.1699,30.0817,42.7267,57.9549,53.5015,39.5706])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [3, 3, 3, 3, 3, 3, 3, 3] rates.
[<Entry index=32 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=136 label="InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3">]
[<Entry index=41 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=136 label="InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3">]
[<Entry index=33 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=136 label="InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 137,
    label = "C_rad/NDMustO",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     O 0 {1,S}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1393.71,160.141,44.5758,19.2489,6.89401,3.79584,1.78521,1.26472],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=10 label="H2O2">, <Entry index=138 label="InChI=1/C4H9O/c1-3-4(2)5/h5H,3H2,1-2H3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 138,
    label = "InChI=1/C4H9O/c1-3-4(2)5/h5H,3H2,1-2H3",
    group = 
"""
1     C 0 {2,S} {4,S} {6,S} {7,S}
2     C 0 {1,S} {8,S} {9,S} {10,S}
3     C 0 {4,S} {11,S} {12,S} {13,S}
4  *3 C 1 {1,S} {3,S} {5,S}
5     O 0 {4,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {3,S}
14    H 0 {5,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1393.71,160.141,44.5758,19.2489,6.89401,3.79584,1.78521,1.26472],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=10 label="H2O2">, <Entry index=138 label="InChI=1/C4H9O/c1-3-4(2)5/h5H,3H2,1-2H3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 139,
    label = "C_rad/OneDe",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.44501e-08,1.22352e-06,1.63554e-05,8.79104e-05,0.000661944,0.00207154,0.00815778,0.0143806],"m^3/(mol*s)","*|/",[219977,12409.2,2132.83,642.305,136.345,51.5357,12.9641,6.27249])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [8, 8, 8, 8, 8, 8, 8, 8] rates.
[<Entry index=31 label="C/H3/Cd">, <Entry index=140 label="C_rad/Cs2">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=140 label="C_rad/Cs2">]
[<Entry index=14 label="Cd_pri">, <Entry index=140 label="C_rad/Cs2">]
[<Entry index=3 label="H2">, <Entry index=140 label="C_rad/Cs2">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 140,
    label = "C_rad/Cs2",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.44501e-08,1.22352e-06,1.63554e-05,8.79104e-05,0.000661944,0.00207154,0.00815778,0.0143806],"m^3/(mol*s)","*|/",[219977,12409.2,2132.83,642.305,136.345,51.5357,12.9641,6.27249])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [8, 8, 8, 8, 8, 8, 8, 8] rates.
[<Entry index=31 label="C/H3/Cd">, <Entry index=140 label="C_rad/Cs2">]
[<Entry index=54 label="C/H/Cs3">, <Entry index=140 label="C_rad/Cs2">]
[<Entry index=14 label="Cd_pri">, <Entry index=140 label="C_rad/Cs2">]
[<Entry index=3 label="H2">, <Entry index=140 label="C_rad/Cs2">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:24:46 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 141,
    label = "C_rad/ODMustO",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     O 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 142,
    label = "C_rad/TwoDe",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 143,
    label = "C_rad/Cs",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 144,
    label = "C_rad/TDMustO",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     O 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 145,
    label = "C_rad/ThreeDe",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

tree(
"""
L1: X_H
    L2: H2
    L2: Ct_H
    L2: O_H
        L3: O_pri
        L3: O_sec
            L4: O/H/NonDeC
            L4: O/H/NonDeO
                L5: H2O2
            L4: O/H/OneDe
    L2: Orad_O_H
    L2: Cd_H
        L3: Cd_pri
        L3: Cd_sec
            L4: Cd/H/NonDeC
            L4: Cd/H/NonDeO
            L4: Cd/H/OneDe
    L2: Cb_H
    L2: CO_H
        L3: CO_pri
        L3: CO_sec
            L4: CO/H/NonDe
            L4: CO/H/OneDe
    L2: Cs_H
        L3: C_methane
        L3: C_pri
            L4: C/H3/Cs
                L5: InChI=1/C2H6/c1-2/h1-2H3
                L5: InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/gamma
            L4: C/H3/Cd
                L5: InChI=1/C3H6/c1-3-2/h3H,1H2,2H3
                L5: InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3
                L5: InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+
            L4: C/H3/Ct
            L4: C/H3/Cb
            L4: C/H3/CO
            L4: C/H3/O
        L3: C_sec
            L4: C/H2/NonDeC
                L5: InChI=1/C3H8/c1-3-2/h3H2,1-2H3
            L4: C/H2/NonDeO
                L5: C/H2/CsO
                    L6: InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha
                L5: C/H2/O2
            L4: C/H2/OneDe
                L5: C/H2/OneDeC
                    L6: InChI=1/C3H6O/c1-2-3-4/h3H,2H2,1H3/beta
                    L6: InChI=1/C4H8/c1-3-4-2/h3H,1,4H2,2H3
                L5: C/H2/OneDeO
            L4: C/H2/TwoDe
        L3: C_ter
            L4: C/H/NonDeC
                L5: C/H/Cs3
                    L6: InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta
                L5: C/H/NDMustO
            L4: C/H/OneDe
                L5: C/H/Cs2
                    L6: InChI=1/C4H8O/c1-4(2)3-5/h3-4H,1-2H3
                L5: C/H/ODMustO
            L4: C/H/TwoDe
                L5: C/H/Cs
                L5: C/H/TDMustO
            L4: C/H/ThreeDe
L1: Y_rad_birad
    L2: Y_1centerbirad
        L3: O_atom_triplet
        L3: CH2_triplet
    L2: Y_rad
        L3: H_rad
        L3: Y_2centeradjbirad
            L4: O2b
            L4: C2b
        L3: Ct_rad
        L3: O_rad
            L4: O_pri_rad
            L4: O_sec_rad
                L5: O_rad/NonDeC
                    L6: InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3
                L5: O_rad/NonDeO
                    L6: OOCH3
                L5: O_rad/OneDe
                    L6: InChI=1/C4H7O/c1-2-3-4-5/h3-4H,2H2,1H3
                    L6: InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/o
        L3: Cd_rad
            L4: Cd_pri_rad
                L5: InChI=1/C2H3/c1-2/h1H,2H2
                L5: InChI=1/C4H7/c1-3-4-2/h1,3H,4H2,2H3
            L4: Cd_sec_rad
                L5: Cd_rad/NonDeC
                    L6: InChI=1/C3H5/c1-3-2/h1H2,2H3
                    L6: InChI=1/C4H7/c1-3-4-2/h3H,1-2H3
                L5: Cd_rad/NonDeO
                L5: Cd_rad/OneDe
        L3: Cb_rad
        L3: CO_rad
            L4: CO_pri_rad
            L4: CO_sec_rad
                L5: CO_rad/NonDe
                L5: CO_rad/OneDe
        L3: Cs_rad
            L4: C_methyl
            L4: C_pri_rad
                L5: C_rad/H2/Cs
                    L6: InChI=1/C2H5/c1-2/h1H2,2H3
                    L6: InChI=1/C4H9O/c1-2-3-4-5/h5H,1-4H2
                    L6: InChI=1/C4H9O/c1-3-4(2)5/h4-5H,2-3H2,1H3
                    L6: InChI=1/C4H9O/c1-3-4(2)5/h4-5H,1,3H2,2H3
                    L6: InChI=1/C4H9O/c1-4(2,3)5/h5H,1H2,2-3H3
                    L6: InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3
                L5: C_rad/H2/Cd
                    L6: InChI=1/C3H5/c1-3-2/h3H,1-2H2
                    L6: InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3
                L5: C_rad/H2/Ct
                L5: C_rad/H2/Cb
                L5: C_rad/H2/CO
                L5: C_rad/H2/O
            L4: C_sec_rad
                L5: C_rad/H/NonDeC
                    L6: InChI=1/C3H7/c1-3-2/h3H,1-2H3
                    L6: InChI=1/C4H9O/c1-2-3-4-5/h2,5H,3-4H2,1H3
                    L6: InChI=1/C4H9O/c1-2-3-4-5/h3,5H,2,4H2,1H3
                    L6: InChI=1/C4H9O/c1-3-4(2)5/h3-5H,1-2H3
                L5: C_rad/H/NonDeO
                    L6: C_rad/H/CsO
                        L7: InChI=1/C4H9O/c1-2-3-4-5/h4-5H,2-3H2,1H3
                        L7: InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3
                    L6: C_rad/H/O2
                L5: C_rad/H/OneDe
                    L6: C_rad/H/OneDeC
                        L7: InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c
                    L6: C_rad/H/OneDeO
                L5: C_rad/H/TwoDe
            L4: C_ter_rad
                L5: C_rad/NonDeC
                    L6: C_rad/Cs3
                        L7: InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3
                    L6: C_rad/NDMustO
                        L7: InChI=1/C4H9O/c1-3-4(2)5/h5H,3H2,1-2H3
                L5: C_rad/OneDe
                    L6: C_rad/Cs2
                    L6: C_rad/ODMustO
                L5: C_rad/TwoDe
                    L6: C_rad/Cs
                    L6: C_rad/TDMustO
                L5: C_rad/ThreeDe
"""
)

